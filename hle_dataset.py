from datasets import load_dataset
from huggingface_hub import login

# Replace 'your_access_token' with the token from Hugging Face
access_token = input ("Please enter your access token from Hugging Face")
login(access_token)


# Load the dataset (Replace 'your_dataset_name' with the actual name)
dataset = load_dataset("cais/hle")

# Choose the split you need (e.g., "train", "test", "validation")
df = dataset["test"].to_pandas()  # Convert to Pandas DataFrame

# Select only the required columns
columns_to_keep = [
    "question", "answer", "answer_type", "rationale", "raw_subject", "category"
]
df = df[columns_to_keep]

# Save to CSV
df.to_csv("hle_dataset.csv", index=False)

print("Filtered dataset saved as filtered_dataset.csv")
