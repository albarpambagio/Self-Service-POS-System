# Self-Service Point-of-Sale System for Andi's Store

## Background Problems
Managing transactions efficiently is crucial for retail businesses. Traditional manual methods of recording sales and calculating totals can be error-prone and time-consuming. The lack of a digital system can lead to inaccuracies in calculating total prices, the inability to modify orders easily, and challenges in maintaining order records. This project aims to address these problems by developing a Self-Service point-of-sale system for Andi's Store in Python.

## Required Objectives/Requirements for Program Development
- Enable users to create new a transaction and add items to them.
- Allow users to edit items within a transaction, including updating names, quantities, and prices.
- Allow users to delete items within a transaction
- Display order summaries to users, along with the total price.
- Apply discounts based on total purchase value.
- Provide a check for order validity to identify input errors.
- Allow users to reset transactions when needed.
- Create a user-friendly command-line interface.

## Functions and Their Processes
- `add_item(item)`: Add an item to the transaction.
- `update_item_name(item_name, updated_name)`: Update the name of an item in the transaction.
- `update_item_qty(item_name, updated_qty)`: Update the quantity of an item in the transaction.
- `update_item_price(item_name, updated_price)`: Update the price of an item in the transaction.
- `delete_item(item_name)`: Delete an item from the transaction.
- `check_order()`: Check for input errors and validate the correctness of the order.
- `get_order_summary()`: Get a summary of the current order.
- `total_price()`: Calculate the total price of the transaction, applying discounts.
- `reset_transaction()`: Reset the transaction to an empty state.

## Flowchart
![image](https://github.com/albarpambagio/Self-Service-POS-System/assets/46396286/55d020b5-472f-4b59-8756-ab71a0c747c2)
URL: https://s.id/1T1Dp

## Test cases

### add_item(item), get_order_summary(), & total_price()
![image](https://github.com/albarpambagio/Self-Service-POS-System/assets/46396286/bd7532a7-65a5-46dd-b2f1-3032de8f5397)

### delete_item(item_name)
![image](https://github.com/albarpambagio/Self-Service-POS-System/assets/46396286/ffc5744f-9d8a-44e1-a085-2579c3081cce)

### update_item_name(item_name, updated_name)
![image](https://github.com/albarpambagio/Self-Service-POS-System/assets/46396286/253c6bdb-8d0b-43b9-a464-b67430dcfbe6)

### update_item_qty(item_name, updated_qty)
![image](https://github.com/albarpambagio/Self-Service-POS-System/assets/46396286/27d085c0-34d4-4215-9369-3a19355b1456)

### update_item_price(item_name, updated_price)
![image](https://github.com/albarpambagio/Self-Service-POS-System/assets/46396286/9b042165-36dc-4d13-a0a6-a04dd61fbf92)

### check_order()
![image](https://github.com/albarpambagio/Self-Service-POS-System/assets/46396286/d7926300-695b-42e1-8d2a-91e6a62b655a)

### reset_transaction()
![image](https://github.com/albarpambagio/Self-Service-POS-System/assets/46396286/05c4f4d8-28f8-4c94-a190-2a814a25b127)




## Conclusion
The Self-Service Point-of-Sale System for Andi's store streamlines the transaction process, making it easier for customers to create, modify, and manage their orders. By providing a user-friendly interface and ensuring order validity, this system aims to enhance the overall shopping experience and improve accuracy in order management. With the potential for future enhancements, such as user authentication and database integration, this project lays the foundation for an efficient and robust point-of-sale solution.
