import tkinter as tk
from tkinter import messagebox
import tkinter as tk
from tkinter import messagebox, simpledialog


class Flight:
    def __init__(self, flight_number, source, destination, capacity, booked_seats):
        self.flight_number = flight_number
        self.source = source
        self.destination = destination
        self.capacity = capacity
        self.booked_seats = booked_seats

    def display_info(self):
        return f"Flight Number: {self.flight_number}\nSource: {self.source}\nDestination: {self.destination}\nAvailable Seats: {self.capacity - self.booked_seats}\n"

class BookingSystem:
    def __init__(self):
        self.flights = []
        self.load_flights()

    def load_flights(self):
        try:
            with open("flights.txt", "r") as file:
                for line in file:
                    data = line.strip().split(',')
                    flight = Flight(*data)
                    self.flights.append(flight)
        except FileNotFoundError:
            # Create an empty file if it doesn't exist
            open("flights.txt", "w").close()

    def save_flights(self):
        with open("flights.txt", "w") as file:
            for flight in self.flights:
                file.write(f"{flight.flight_number},{flight.source},{flight.destination},{flight.capacity},{flight.booked_seats}\n")

    def add_flight(self, flight):
        self.flights.append(flight)
        self.save_flights()

    def display_available_flights(self):
        return [flight.display_info() for flight in self.flights]

    def book_ticket(self, flight_number, num_tickets):
        for flight in self.flights:
            if flight.flight_number == flight_number:
                available_seats = flight.capacity - flight.booked_seats
                if num_tickets <= available_seats:
                    flight.booked_seats += num_tickets
                    self.save_flights()
                    return f"Booking successful! {num_tickets} seat(s) booked for Flight {flight_number}.\nRemaining seats: {available_seats - num_tickets}"
                else:
                    return "Booking failed. Not enough seats available."
        return f"Flight with number {flight_number} not found."

class App:
    def __init__(self, root):
        self.booking_system = BookingSystem()

        root.title("Airline Ticket Booking System")

        self.label = tk.Label(root, text="Welcome to Airline Booking System", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.display_flights_button = tk.Button(root, text="Display Available Flights", command=self.display_flights)
        self.display_flights_button.pack(pady=5)

        self.book_ticket_button = tk.Button(root, text="Book Ticket", command=self.book_ticket)
        self.book_ticket_button.pack(pady=5)

    def display_flights(self):
        flights_info = "\n".join(self.booking_system.display_available_flights())
        messagebox.showinfo("Available Flights", flights_info)

    def book_ticket(self):
        flight_number = simpledialog.askstring("Input", "Enter the flight number:")
        if flight_number is not None:
            num_tickets = simpledialog.askinteger("Input", "Enter the number of tickets to book:")
            if num_tickets is not None:
                result = self.booking_system.book_ticket(flight_number, num_tickets)
                messagebox.showinfo("Booking Result", result)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
