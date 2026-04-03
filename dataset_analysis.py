import pandas as pd
import matplotlib.pyplot as plt


img_df = pd.read_csv('Dataset_Metadata - Images.csv')
vid_df = pd.read_csv('Dataset_Metadata - Videos.csv')


img_df['Modality'] = 'Image'
vid_df['Modality'] = 'Video'


df = pd.concat([img_df, vid_df], ignore_index=True)


print("Total items:", len(df))
print("Images:", len(img_df))
print("Videos:", len(vid_df))


if 'Category' in df.columns:
    df['Category'] = df['Category'].str.strip()   # remove spaces
    df['Category'] = df['Category'].str.lower()   # lowercase everything

    df['Category'] = df['Category'].replace({
        'city & rural life': 'city and rural life',
        'local objects & culture': 'local objects and culture',
        'marketplace': 'marketplaces',
        'public places & infrastructure': 'public places and infrastructure',
        'agriculture, livestock and wild animal': 'agriculture, livestock and wild animals',
        'agriculture,livestock and wild animals': 'agriculture, livestock and wild animals'
    })

    counts = df['Category'].value_counts()
    print("\nCategory distribution:\n", counts)

    counts.plot(kind='barh')
    plt.title("Category Distribution")
    plt.xlabel("Count")
    plt.ylabel("Category")
    plt.tight_layout()
    plt.savefig("cleaned_distribution.png")
    plt.show()

else:
    print("No 'Category' column found.")
