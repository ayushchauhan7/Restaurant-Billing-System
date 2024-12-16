import tkinter as tk
from tkinter import messagebox
import sqlite3

# Create a SQLite database connection
conn = sqlite3.connect('restaurant.db')
c = conn.cursor()

# Create tables if they don't exist
c.execute('''CREATE TABLE IF NOT EXISTS menu
             (item_id INTEGER PRIMARY KEY, item_name TEXT, price REAL)''')
c.execute('''CREATE TABLE IF NOT EXISTS orders
             (order_id INTEGER PRIMARY KEY, table_no INTEGER, item_id INTEGER, quantity INTEGER, total REAL)''')
conn.commit()


class RestaurantBillingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Billing System")
        self.root.geometry("800x600")

        # Menu frame
        self.menu_frame = tk.Frame(self.root, bg="light gray")
        self.menu_frame.pack(fill="both", expand=True)

        # Menu labels and entries
        self.item_name_label = tk.Label(self.menu_frame, text="Item Name", font=("Arial", 12))
        self.item_name_label.grid(row=0, column=0, padx=10, pady=10)
        self.item_name_entry = tk.Entry(self.menu_frame, width=20, font=("Arial", 12))
        self.item_name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.price_label = tk.Label(self.menu_frame, text="Price", font=("Arial", 12))
        self.price_label.grid(row=1, column=0, padx=10, pady=10)
        self.price_entry = tk.Entry(self.menu_frame, width=20, font=("Arial", 12))
        self.price_entry.grid(row=1, column=1, padx=10, pady=10)

        # Add item button
        self.add_item_button = tk.Button(self.menu_frame, text="Add Item", command=self.add_item, font=("Arial", 12))
        self.add_item_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Order frame
        self.order_frame = tk.Frame(self.root, bg="light gray")
        self.order_frame.pack(fill="both", expand=True)

        # Order labels and entries
        self.table_no_label = tk.Label(self.order_frame, text="Table No.", font=("Arial", 12))
        self.table_no_label.grid(row=0, column=0, padx=10, pady=10)
        self.table_no_entry = tk.Entry(self.order_frame, width=20, font=("Arial", 12))
        self.table_no_entry.grid(row=0, column=1, padx=10, pady=10)

        self.item_id_label = tk.Label(self.order_frame, text="Item ID", font=("Arial", 12))
        self.item_id_label.grid(row=1, column=0, padx=10, pady=10)
        self.item_id_entry = tk.Entry(self.order_frame, width=20, font=("Arial", 12))
        self.item_id_entry.grid(row=1, column=1, padx=10, pady=10)

        self.quantity_label = tk.Label(self.order_frame, text="Quantity", font=("Arial", 12))
        self.quantity_label.grid(row=2, column=0, padx=10, pady=10)
        self.quantity_entry = tk.Entry(self.order_frame, width=20, font=("Arial", 12))
        self.quantity_entry.grid(row=2, column=1, padx=10, pady=10)

        # Place order button
        self.place_order_button = tk.Button(self.order_frame, text="Place Order", command=self.place_order, font=("Arial", 12))
        self.place_order_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Bill frame
        self.bill_frame = tk.Frame(self.root, bg="light gray")
        self.bill_frame.pack(fill="both", expand=True)

        # Bill labels and text
        self.bill_label = tk.Label(self.bill_frame, text="Bill", font=("Arial", 18))
        self.bill_label.grid(row=0, column=0, padx=10, pady=10)
        self.bill_text = tk.Text(self.bill_frame, width=40, height=10, font=("Arial", 12))
        self.bill_text.grid(row=1, column=0, padx=10, pady=10)

        # Generate bill button
        self.generate_bill_button = tk.Button(self.bill_frame, text="Generate Bill", command=self.generate_bill, font=("Arial", 12))
        self.generate_bill_button.grid(row=2, column=0, padx=10, pady=10)

    def add_item(self):
        item_name = self.item_name_entry.get()
        price = self.price_entry.get()
        if item_name and price:
            c.execute("INSERT INTO menu (item_name, price) VALUES (?, ?)", (item_name, price))
            conn.commit()
            messagebox.showinfo("Success", "Item added successfully!")
            self.item_name_entry.delete(0, tk.END)
            self.price_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please fill in all fields!")

    def place_order(self):
        table_no = self.table_no_entry.get()
        item_id = self.item_id_entry.get()
        quantity = self.quantity_entry.get()
        if table_no and item_id and quantity:
            c.execute("SELECT price FROM menu WHERE item_id=?", (item_id,))
            price = c.fetchone()[0]
            total = int(quantity) * price
            c.execute("INSERT INTO orders (table_no, item_id, quantity, total) VALUES (?, ?, ?, ?)",
                      (table_no, item_id, quantity, total))
            conn.commit()
            messagebox.showinfo("Success", "Order placed successfully!")
            self.table_no_entry.delete(0, tk.END)
            self.item_id_entry.delete(0, tk.END)
            self.quantity_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please fill in all fields!")

    def generate_bill(self):
        self.bill_text.delete(1.0, tk.END)
        table_no = self.table_no_entry.get()
        if table_no:
            c.execute(
                "SELECT o.table_no, m.item_name, o.quantity, m.price, o.total FROM orders o JOIN menu m ON o.item_id=m.item_id WHERE o.table_no=?",
                (table_no,))
            orders = c.fetchall()
            total_bill = 0
            for order in orders:
                self.bill_text.insert(tk.END, f"Table No: {order[0]}\n")
                self.bill_text.insert(tk.END, f"Item: {order[1]}\n")
                self.bill_text.insert(tk.END, f"Quantity: {order[2]}\n")
                self.bill_text.insert(tk.END, f"Price: {order[3]}\n")
                self.bill_text.insert(tk.END, f"Total: {order[4]}\n\n")
                total_bill += order[4]
            self.bill_text.insert(tk.END, f"Total Bill: {total_bill}\n")
        else:
            messagebox.showerror("Error", "Please enter table no!")


root = tk.Tk()
app = RestaurantBillingSystem(root)
root.mainloop()