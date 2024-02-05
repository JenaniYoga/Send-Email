# Send E-Mail.py
This Python script allows you to send an email using Gmail SMTP. It uses `pyqrcode` and `smtplib` libraries to create and send a simple test email.

## Prerequisites
Before running the script, ensure you have the following:
- Python installed on your system.
- Internet connectivity to access Gmail's SMTP server.

## Setup
1. Clone or download the repository to your local machine.
2. Make sure you have the required libraries installed. You can install them using pip:
    pip install pyqrcode
   
4. You need to enable less secure apps in your Gmail account to send emails using SMTP. Follow the instructions [here](https://myaccount.google.com/lesssecureapps) to allow less secure apps.

## Usage
1. Open the `Send E-Mail.py` file in your preferred Python editor.

2. Modify the following variables in the script according to your needs:
    - `sender_email`: Your Gmail email address.
    - `receiver_email`: The recipient's email address.
    - `password`: Your Gmail account password. Ensure it's secured.

3. Run the script by executing the following command in your terminal:
    python Send E-Mail.py
4. Once the script executes successfully, you should see a message indicating that the email was sent.

## Important Notes

- Ensure that you have provided the correct email addresses and password in the script.
- Make sure your Gmail account allows less secure app access, as mentioned in the setup section.

## Security Considerations
- **Password Handling**: Be cautious with storing passwords in scripts. Consider using environment variables or secure methods for handling sensitive information.
- **Less Secure Apps**: Enabling less secure apps can pose a security risk. Consider using app passwords or OAuth2 authentication for better security.

## Disclaimer
This script is provided for educational purposes only. Use it responsibly and at your own risk. The author is not responsible for any misuse or damage caused by this script.

For any issues or inquiries, please contact the author at yohajenany98@gmail.com.
