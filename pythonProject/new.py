import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def email_regex(mail):
    if (re.fullmatch(regex, mail)):
        print("Valid Email")

    else:
        print("Invalid Email")


if __name__ == '__main__':
    mail = "ankitrai326@gmail.com"

    email_regex(mail)

    mail = "my.ownsite@our-earth.org"
    email_regex(mail)

    mail = "ankitrai326.com"
    email_regex(mail)
