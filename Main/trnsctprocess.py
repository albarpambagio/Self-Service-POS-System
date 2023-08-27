from tabulate import tabulate

class Transaction:
    def __init__(self):
        """
        Initialize a new transaction object. That act as blank placeholder for user's input

        Args:
            None

        Returns:
            None
        """         
        self.items = []

    def add_item(self, item):
        """
        Add an/more item to the transaction.

        Args:
            item (list): A list containing item details [product name, quantity, unit price]

        Returns:
            None
        """      
        self.items.append(item)

    def update_item_name(self, item_name, updated_name):
        """
        Update the name of an/more item in the transaction.

        Args:
            item_name (str): The name of the item to be updated
            updated_name (str): The new name for the item

        Returns:
            str: A message indicating the success of the update
        """      
        for item in self.items:
            if item[0] == item_name:
                item[0] = updated_name
        return f"Nama barang berhasil diperbaharui menjadi '{updated_name}'"

    def update_item_qty(self, item_name, updated_qty):
        """
        Update the quantity of an item in the transaction.

        Args:
            item_name (str): The name of the item to be updated
            updated_qty (int): The new quantity for the item

        Returns:
            str: A message indicating the success of the update of the transaction
        """         
        for item in self.items:
            if item[0] == item_name:
                item[1] = updated_qty
        return f"Jumlah barang berhasil diperbaharui menjadi '{updated_qty}'"

    def update_item_price(self, item_name, updated_price):
        """
        Update the price of an item in the transaction.

        Args:
            item_name (str): The name of the item to be updated
            updated_price (int): The new price for the item

        Returns:
            str: A message indicating the success of the update
        """        
        for item in self.items:
            if item[0] == item_name:
                item[2] = updated_price
        return f"Harga barang berhasil diperbaharui menjadi '{updated_price}'"

    def delete_item(self, item_name):
        """
        Delete an item from the transaction.

        Args:
            item_name (str): The name of the item to be deleted

        Returns:
            str: A message indicating the success of the deletion
        """      
        self.items = [item for item in self.items if item[0] != item_name]
        return f"Barang '{item_name}' berhasil dihapus"

    def check_order(self):
        """
        Check the transaction for input errors.

        Returns:
            str: A message indicating if there are any input errors or if the order is correct
        """          
        for item in self.items:
            if any(value is None for value in item):
                return "Order belum diinput"
        return "Pemesanan sudah benar"

    def get_order_summary(self):
        """
        Get a summary of the current order.

        Returns:
            list: A list containing order summary details
        """       
        order_summary = []
        for idx, item in enumerate(self.items, start=1):
            item_total = item[1] * item[2]
            order_summary.append([idx, item[0], item[1], f"Rp {item[2]:,}", f"Rp {item_total:,}"])
        return order_summary

    def total_price(self):
        """
        Calculate the total price of the transaction.

        Returns:
            float: The total price of the transaction
        """           
        total = sum(item[1] * item[2] for item in self.items)
        if total > 500000:
            total *= 0.9
        elif total > 300000:
            total *= 0.92
        elif total > 200000:
            total *= 0.95
        return total

    def reset_transaction(self):
        """
        Reset the transaction to an empty state.

        Returns:
            str: A message indicating the successful reset of the transaction
        """            
        self.items = []
        return "Daftar belanja berhasil direset"
