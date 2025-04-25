class Train:
    def __init__(self, name, number, total_seats, fare):
        self.name = name
        self.number = number
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.fare = fare 

    def book_ticket(self, num_tickets=1):
        if self.available_seats >= num_tickets:
            self.available_seats -= num_tickets
            print(f"Successfully booked {num_tickets} ticket(s).")
        else:
            print(f"Only {self.available_seats} seat(s) available. Cannot book {num_tickets} ticket(s).")

    def get_status(self):
        print(f"Train {self.name} ({self.number}) has {self.available_seats} seat(s) available.")

    def get_fare_info(self):
        print(f"Fare per ticket for Train {self.name} ({self.number}) is ₹{self.fare}.")


train1 = Train("Rajdhani Express", "12301", 100, 1500)

train1.get_status()
train1.get_fare_info()
train1.book_ticket()
train1.get_status()
train1.book_ticket(2)
train1.get_status()
train1.book_ticket(99)
train1.get_status()
