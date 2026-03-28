import pandas as pd
import matplotlib.pyplot as plt

def analyze_sudan_mm_infrastructure():
    try:
        # 1. Load the two separate metadata files
        img_df = pd.read_csv('image_metadata.csv')
        vid_df = pd.read_csv('video_metadata.csv')
        
        print(" Image and Video metadata successfully loaded!")

        # 2. Add a 'Type' column to track the modality before merging
        img_df['Modality'] = 'Image'
        vid_df['Modality'] = 'Video'

        # 3. Combine both into one Master Dataset (The '4sparks' Infrastructure)
        master_df = pd.concat([img_df, vid_df], ignore_index=True)
        
        # 4. Global Statistics (Matching the 4sparks Final Report)
        total_items = len(master_df)
        image_count = len(img_df)
        video_count = len(vid_df)

        print(f"\n--- Sudan-MM 2025 Submission Summary ---")
        print(f"Total Multimodal Pairs: {total_items}")
        print(f"Images: {image_count}")
        print(f"Videos: {video_count}")

        # 5. Category Analysis (Sovereign Intelligence Priorities)
        if 'Category' in master_df.columns:
            category_distribution = master_df['Category'].value_counts()
            print("\n--- Distribution Across Strategic Categories ---")
            print(category_distribution)

            # 6. Visualization for the Research Poster
            category_distribution.plot(kind='barh', color='darkorange', figsize=(12, 7))
            plt.title('Sudan-MM 2025: Cross-Modality Category Distribution')
            plt.xlabel('Number of Items (Combined Image & Video)')
            plt.ylabel('Category')
            plt.tight_layout()
            plt.savefig('sudan_mm_distribution.png')
            print("\n Visualization 'sudan_mm_distribution.png' generated.")

    except Exception as e:
        print(f" Error during analysis: {e}")
        print("Tip: Ensure 'image_metadata.csv' and 'video_metadata.csv' are in the same folder.")

if __name__ == "__main__":
    analyze_sudan_mm_infrastructure()
