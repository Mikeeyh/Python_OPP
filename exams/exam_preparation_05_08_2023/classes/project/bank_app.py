from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    VALID_LOAN_TYPES = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    VALID_CLIENT_TYPES = {"Student": Student, "Adult": Adult}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.VALID_LOAN_TYPES:
            raise Exception("Invalid loan type!")

        new_loan = self.VALID_LOAN_TYPES[loan_type]()
        self.loans.append(new_loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.VALID_CLIENT_TYPES:
            raise Exception("Invalid client type!")

        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."

        new_client = self.VALID_CLIENT_TYPES[client_type](client_name, client_id, income)
        self.clients.append(new_client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = next((c for c in self.clients if c.client_id == client_id), None)

        if (loan_type == "StudentLoan" and client.__class__.__name__ == "Student") or (
                loan_type == "MortgageLoan" and client.__class__.__name__ == "Adult"
        ):
            loan = next((l for l in self.loans if l.__class__.__name__ == loan_type), None)
            self.loans.remove(loan)
            client.loans.append(loan)
            return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."
        else:
            raise Exception("Inappropriate loan type!")

    # def grant_loan(self, loan_type: str, client_id: str):
    #     client = [c for c in self.clients if c.client_id == client_id][0]
    #
    #     if (loan_type == "StudentLoan" and client.__class__.__name__ == "Student") or (
    #             loan_type == "MortgageLoan" and client.__class__.__name__ == "Adult"
    #     ):
    #         loan = [l for l in self.loans if l.__class__.__name__ == loan_type][0]
    #         self.loans.remove(loan)
    #         client.loans.append(loan)
    #         return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."
    #     else:
    #         raise Exception("Inappropriate loan type!")

    def remove_client(self, client_id: str):
        client = next((c for c in self.clients if c.client_id == client_id), None)
        if client is None:
            raise ValueError("No such client!")
        if client.loans:
            raise ValueError("The client has loans! Removal is impossible!")
        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        number_of_changed_loans = 0
        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                loan.increase_interest_rate()
                number_of_changed_loans += 1

        return f"Successfully changed {number_of_changed_loans} loans."

    def increase_clients_interest(self, min_rate: float):
        c_count = 0
        for c in self.clients:
            if c.interest < min_rate:
                c.increase_clients_interest()
                c_count += 1
        return f"Number of clients affected: {c_count}."

    def get_statistics(self):
        total_income = sum([client.income for client in self.clients])
        granted_loans_count = sum([len(client.loans) for client in self.clients])
        granted_amount = sum([sum([loan.amount for loan in client.loans]) for client in self.clients])
        # granted_amount = sum([l.amount for c in self.clients for l in c.loans])
        not_granted_sum = sum([loan.amount for loan in self.loans])
        try:
            avg_client_rate = sum([client.interest for client in self.clients]) / len(self.clients)
        except ZeroDivisionError:
            avg_client_rate = 0

        result = f"Active Clients: {len(self.clients)}\n"
        result += f"Total Income: {total_income:.2f}\n"
        result += f"Granted Loans: {granted_loans_count}, Total Sum: {granted_amount:.2f}\n"
        result += f"Available Loans: {len(self.loans)}, Total Sum: {not_granted_sum:.2f}\n"
        result += f"Average Client Interest Rate: {avg_client_rate:.2f}"
        return result
