def is_valid_email(email):
    if " " in email:
        return False
    if email.count("@") != 1:
        return False
    local_part, domain_part = email.split("@")
    if not local_part or not domain_part:
        return False
    if "." not in domain_part:
        return False
    if email.startswith("@") or email.endswith("@") or email.startswith(".") or email.endswith("."):
        return False
    return True

# Input from user
email_input = input("Enter an email address: ")    #    test@example.com    test@.com      test@@example.com
# Check and print result
if is_valid_email(email_input):
    print("Valid email")
else:
    print("Invalid email")
