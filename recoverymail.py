import imaplib
import re

def extract_verification_code(email_content):
    # Regular expression pattern to match the verification code
    pattern = r"Here is your Mailfence activation code:\s*(\d{6})"
    match = re.search(pattern, email_content)
    if match:
        return match.group(1)  # Return the first matching group (verification code)
    else:
        return None  # Return None if no match is found
    
def get_recovery_mail_code():
    imap_server = 'outlook.office365.com'  # Update the IMAP server address
    username = 'galaxy.supersenior@outlook.com'  # Replace with your recovery email address
    password = 'password2001)*)@'  # Replace with your recovery email password

    imap = imaplib.IMAP4_SSL(imap_server)
    imap.login(username, password)

    # Select the mailbox/folder containing the recovery email
    mailbox = 'INBOX'  # Replace with the appropriate mailbox or folder name
    imap.select(mailbox)

    # Search for the email containing the verification code
    # Modify the search criteria as per your requirement
    search_criteria = '(UNSEEN SUBJECT "activation code")'
    status, email_ids = imap.search(None, search_criteria)

    if status == 'OK':
        email_id_list = email_ids[0].split()
        if email_id_list:
            latest_email_id = email_id_list[-1]
            status, email_data = imap.fetch(latest_email_id, '(RFC822)')

            if status == 'OK':
                # Extract the verification code from the email content
                email_message = email_data[0][1].decode('utf-8')  # Decoding the email data
                verification_code = extract_verification_code(email_message)  # Replace with your code to extract the verification code
                imap.logout()
                return verification_code
        else:
            print("No email found matching the search criteria.")
    imap.logout()