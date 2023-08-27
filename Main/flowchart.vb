link: https://s.id/1T1LM
Start
  Display Program Title and Menu
    Loop
      Get User Menu Choice
        If Choice == 8, Exit Loop
        If Choice == 1:
          Input Product Details
          Add Item to Transaction
          Check Order
        If Choice == 2:
          Display Edit Menu
          Get Edit Menu Choice
            If Edit Choice == 1:
              Input Item Name and Updated Name
              Update Item Name
            If Edit Choice == 2:
              Input Item Name and Updated Quantity
              Update Item Quantity
            If Edit Choice == 3:
              Input Item Name and Updated Price
              Update Item Price
        If Choice == 3:
          Input Item Name to Delete
          Delete Item from Transaction
          Get Order Summary
          Calculate Total Price
          Display Order Summary and Total Price
        If Choice == 4:
          Get Order Summary
          Calculate Total Price
          If Order is Correct:
            Display Order Summary and Total Price
          If Order is Incorrect:
            Display Error Message
        If Choice == 5:
          Reset Transaction
          Display Reset Message
        If Choice == 6:
          Get Order Summary
          Calculate Total Price
          Display Order Summary and Total Price
          Exit Loop
        If Choice is Invalid:
          Display Invalid Menu Message