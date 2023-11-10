total_tickets_sold = 0
students = 0
standard = 0
kids = 0

command = input()

while command != "Finish":
    film_name = command
    available_seats = int(input())
    taken_seat = 0

    for _ in range(1, available_seats + 1):
        ticket_type = input()

        if ticket_type == "End":
            break
        elif ticket_type == "student":
            students += 1
        elif ticket_type == "standard":
            standard += 1
        elif ticket_type == "kid":
            kids += 1

        taken_seat += 1
        total_tickets_sold += 1

    percent_taken_seats = (taken_seat / available_seats) * 100
    print(f"{film_name} - {percent_taken_seats:.2f}% full.")

    command = input()

percent_students = (students / total_tickets_sold) * 100
percent_standard = (standard / total_tickets_sold) * 100
percent_kids = (kids / total_tickets_sold) * 100

print(f"Total tickets: {total_tickets_sold}")
print(f"{percent_students:.2f}% student tickets.")
print(f"{percent_standard:.2f}% standard tickets.")
print(f"{percent_kids:.2f}% kids tickets.")


# Taxi
# 10
# standard
# kid
# student
# student
# standard
# standard
# End
# Scary Movie
# 6
# student
# student
# student
# student
# student
# student
# Finish

