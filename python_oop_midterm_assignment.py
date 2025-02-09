class Star_Cinema:
    __hall_list = []
    
    @classmethod
    def entry_hall(cls, hall):
        cls.__hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        Star_Cinema.entry_hall(self)
    
    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self.__show_list.append(show_info)
        self.__seats[show_id] = [['Free' for _ in range(self.__cols)] for _ in range(self.__rows)]
    
    def book_seats(self, show_id, seat_positions):
        if show_id not in self.__seats:
            print("Invalid show ID!")
            return
        
        for row, col in seat_positions:
            if not (0 <= row < self.__rows and 0 <= col < self.__cols):
                print(f"Invalid seat position: ({row}, {col})")
                continue
            if self.__seats[show_id][row][col] == 'Booked':
                print(f"Seat ({row}, {col}) is already booked!")
                continue
            self.__seats[show_id][row][col] = 'Booked'
            print(f"Seat ({row}, {col}) booked successfully!")
    
    def view_show_list(self):
        if not self.__show_list:
            print("No shows currently running.")
            return
        print("\nShows running:")
        for show in self.__show_list:
            print(f"Show ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")
    
    def view_available_seats(self, show_id):
        if show_id not in self.__seats:
            print("Invalid show ID!")
            return
        
        print(f"\nAvailable seats for show {show_id}:")
        for row in self.__seats[show_id]:
            print(row)
        print()


hall1 = Hall(5, 5, 1)
hall1.entry_show("S1", "Movie A", "03:00 PM")
hall1.entry_show("S2", "Movie B", "06:00 PM")


while True:
    print("\nOptions:")
    print("1. View all shows")
    print("2. View available seats")
    print("3. Book tickets")
    print("4. Exit")
    choice = input("Choose an option: ").strip()
    
    if choice == '1':
        hall1.view_show_list()
    elif choice == '2':
        show_id = input("Enter show ID: ").strip()
        hall1.view_available_seats(show_id)
    elif choice == '3':
        #hall1.book_seats("S1", [(1, 3), (2, 5), (7, 9), (3,4),(1,3), (1,2),(2,3)])
        show_id = input("Enter show ID: ").strip()
        seat_positions = []
        seat_input = input("Enter row and column (space-separated): ").strip().split()
        row, col = int(seat_input[0]), int(seat_input[1])
        seat_positions.append((row, col))
        hall1.book_seats(show_id, seat_positions)
        
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid option. Please try again.")