The `Categorgy` class in `budget.py` instantiate objects based on different budget categories like *food*, *clothing*, and *entertainment*. When objects are created, they are passed in the name of the category. The class contains a `ledger` that is an unedit list, off all transactions and a `transaction_history` that contains an edited list for display. 

`Category` also contain the following methods:

* The `deposit` method that accepts an amount and description. If no description is given, it default's to an empty string. The method appends an object to the ledger list in the form of `{"amount": amount, "description": description}` and appends an object to the transaction history in the form of `f"{description[:23]:<23}{amount::>7.2f}"`.
* The `withdraw` method that is similar to the `deposit` method, but the amount passed in is stored in the ledger as a negative number. If there are not enough funds, nothing is added to the ledger. This method returns `True` if the withdrawal took place, and `False` otherwise.
* The `get_balance` method returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
* The `transfer` method that accepts an amount and another budget category as arguments. The method adds a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method then adds a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing is added to either ledger. This method returns `True` if the transfer took place, and `False` otherwise.
* The `check_funds` method accepts an amount as an argument. It returns `False` if the amount is greater than the balance of the budget category and returns `True` otherwise. This method is used by both the `withdraw` method and `transfer` method.
* The `get_ledger` method that returns the ledger entries line by line.

When the budget object is printed it displays:
* The title line of 30 characters where the name of the category is centered in a line of `*` characters.
* The list of the items in the transaction_hisotry. Each line shows the description and amount. The first 23 characters of the descriptionis displayed, then the amount. The amount is right aligned, contains two decimal places, and displays a maximum of 7 characters.
* A line displaying the category total.

Here is an example of the output:
```
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
```

Besides the `Category` class, there is the function called `create_spend_chart` that takes a list of categories as an argument. It returns a string that is a bar chart.

The chart shows the percentage spent in each category passed in to the function. Down the left side of the chart are the labels 0 - 100. The "bars" in the bar chart are made out of the "o" character. The height of each bar is rounded down to the nearest 10. The horizontal line below the bars always goes two spaces past the final bar. Each category name is vertacally below the bar. There is a title at the top that says "Percentage spent by category".

This function will only take up to four categories.

Example output below:

```
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     
```

### Testing 

The unit tests for this project are in `test_module.py`.

The tests are imported from `test_module.py` to `main.py` for your convenience. The tests will run automatically whenever you hit the "run" button.

