from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from utils.spreadsheet import save_inquiry

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    incoming_msg = request.values.get("Body", "").strip()
    sender = request.values.get("From", "")

    save_inquiry(sender, incoming_msg)

    response = MessagingResponse()
    response.message("✅ Your inquiry has been saved. We will get back to you soon!")

    return str(response)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
