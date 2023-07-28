class Store:
    def __init__(self, name, location, category, num_employees, is_open):
        self.name = name            # Name of the store
        self.location = location    # Location of the store
        self.category = category    # Category of the store (e.g., grocery, clothing, electronics, etc.)
        self.num_employees = num_employees  # Number of employees working in the store
        self.is_open = is_open      # Boolean flag indicating whether the store is open or closed

    def open_store(self):
        """Open the store."""
        self.is_open = True
        print(f"{self.name} is now open for business.")

    def close_store(self):
        """Close the store."""
        self.is_open = False
        print(f"{self.name} is now closed.")

    def add_employee(self, num_new_employees):
        """Add new employees to the store."""
        self.num_employees += num_new_employees
        print(f"{num_new_employees} new employees added to {self.name}.")

    def remove_employee(self, num_removed_employees):
        """Remove employees from the store."""
        if self.num_employees >= num_removed_employees:
            self.num_employees -= num_removed_employees
            print(f"{num_removed_employees} employees removed from {self.name}.")
        else:
            print("Insufficient employees to remove.")

    def display_info(self):
        """Display information about the store."""
        print(f"Store Name: {self.name}")
        print(f"Location: {self.location}")
        print(f"Category: {self.category}")
        print(f"Number of Employees: {self.num_employees}")
        print(f"Store Status: {'Open' if self.is_open else 'Closed'}")


# Example usage:
if __name__ == "__main__":
    my_store = Store("SuperMart", "Main Street", "Grocery", 10, False)

    my_store.display_info()

    my_store.open_store()
    my_store.add_employee(3)
    my_store.open_store()

    my_store.remove_employee(2)
    my_store.close_store()

    my_store.display_info()
