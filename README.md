# WhatsApp Inquiry Bot

This bot automatically logs WhatsApp inquiries into a Google Spreadsheet and sends auto-replies.

## Installation
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set up Google Sheets API and place `google_credentials.json` in the project folder.
3. Configure `.env` file with Twilio and Google API details.
4. Run Flask server:
   ```bash
   python app.py
   ```
5. Use `ngrok` to expose the webhook and set it in Twilio Console.
