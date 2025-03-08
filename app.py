import gspread
from oauth2client.service_account import ServiceAccountCredentials

if __name__ == "__main__":
    # use credentials to create a client to interact with the Google Drive API
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("google_credentials.json", scope)
    client = gspread.authorize(creds)

    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sheet = client.open("WhatsApp-Bot").sheet1

    # Extract and print all of the values
    list_of_lists = sheet.get_all_records()
    print(list_of_lists)