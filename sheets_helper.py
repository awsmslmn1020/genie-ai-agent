import pandas as pd

def get_contacts(target, country, niche, num_to_send, min_followers, max_followers):
    # Load CSV from GitHub
    url = "https://raw.githubusercontent.com/awsmslmn1020/genie-ai-agent/main/influencers.csv"
    df = pd.read_csv(url)

    # Filter logic (adjust column names to your actual CSV)
    df_filtered = df[
        (df["Target"].str.lower() == target.lower()) &
        (df["Country"].str.lower() == country.lower()) &
        (df["Niche"].str.lower() == niche.lower()) &
        (df["Followers"] >= min_followers) &
        (df["Followers"] <= max_followers)
    ]

    return df_filtered.head(num_to_send).to_dict(orient="records")
