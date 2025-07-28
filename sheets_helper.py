import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_contacts(target, country, niche, limit, min_followers=None, max_followers=None):
    url = {
        "Brand": "https://docs.google.com/spreadsheets/d/1Mf6G8R6IhNaNizezHT03Nji2N4D-IVPGZk9-ZJZ1xCs/edit",
        "Influencer": "https://docs.google.com/spreadsheets/d/1Uvs4baXysRB42M4es8fb-edRQyK8A2jtT6iogi8yNVs/edit"
    }[target]

    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"])
    client = gspread.authorize(creds)
    sheet = client.open_by_url(url).sheet1
    rows = sheet.get_all_records()

    filtered = []
    for row in rows:
        if country.lower() in row['Country'].lower() and niche.lower() in row['Niche'].lower():
            if target == "Influencer" and not (min_followers <= row['Followers'] <= max_followers):
                continue
            filtered.append(row)
        if len(filtered) >= limit:
            break

    return filtered