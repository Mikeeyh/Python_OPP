class EmailValidator:
    def __init__(self, min_length: int, mails: list, domains: list):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail):
        return mail in self.mails

    def __is_domain_valid(self, domain):
        return domain in self.domains

    def validate(self, email):
        email_parts = email.split('@')
        if len(email_parts) == 2:
            current_name = email_parts[0]
            data = email_parts[1].split('.')
            if len(data) == 2:
                current_mail, current_domain = data
                return self.__is_name_valid(current_name) and \
                    self.__is_mail_valid(current_mail) and \
                    self.__is_domain_valid(current_domain)
            return False


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
