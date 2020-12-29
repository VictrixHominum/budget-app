class Category:
    def __init__(self, name):
        self.name = name
        self.balance = 0.00
        self.spent = 0.00
        self.ledger = []
        self.transaction_history = []
        self.title = f"{self.name:*^30}"
        self.transaction_history.append(self.title)

    def __str__(self):
        return_balance = "\n".join(self.transaction_history)
        return f"{return_balance}\nTotal: {self.balance}"

    def check_funds(self, amount):
        if self.balance - amount < 0.00:
            return False
        else:
            return True

    def deposit(self, amount, description=""):
        self.balance += amount
        self.ledger.append({"amount": amount, "description": description})
        self.transaction_history.append(f"{description[0:23]:<23}{amount:>7.2f}")

    def withdraw(self, amount, description=""):
        if self.check_funds(amount) is False:
            return False
        else:
            self.spent += amount
            self.balance -= amount
            self.ledger.append({"amount": -1 * amount, "description": description})
            self.transaction_history.append(f"{description[0:23]:<23}{-1*amount:>7.2f}")
            return True

    def transfer(self, amount, category):
        if self.check_funds(amount) is False:
            return False
        else:
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True

    def get_balance(self):
        return self.balance

    def get_ledger(self):
        return "\n".join(self.ledger)


def create_spend_chart(categories):
    total_spent = 0.00
    position = [1, 4, 7, 10]
    percent_list = []
    max_len = 0
    chart_list = [["Percentage spent by category"], ["100| "], [" 90| "], [" 80| "], [" 70| "], [" 60| "], [" 50| "], [" 40| "], [" 30| "], [" 20| "], [" 10| "], ["  0| "], ["    -"]]
    for category in categories:
        total_spent += category.spent

    for i in range(1, len(chart_list)):
        for j in range(len(categories)):
            for x in range(3):
                if i == len(chart_list)-1:
                    chart_list[i].append("-")
                else:
                    chart_list[i].append(" ")

    for i in range(len(categories)):
        if len(categories[i].name) > max_len:
            max_len = len(categories[i].name)

    if len(categories) == 1:
        for i in range(max_len):
            chart_list.append(f"{categories[0].name[i:(i + 1)]:>6}  ")
    elif len(categories) == 2:
        for i in range(max_len):
            chart_list.append(f"{categories[0].name[i:(i + 1)]:>6}{categories[1].name[i:i+1]:>3}  ")
    elif len(categories) == 3:
        for i in range(max_len):
            chart_list.append(f"{categories[0].name[i:(i + 1)]:>6}{categories[1].name[i:i+1]:>3}{categories[2].name[i:i+1]:>3}  ")
    elif len(categories) == 4:
        for i in range(max_len):
            chart_list.append(f"{categories[0].name[i:(i + 1)]:>6}{categories[1].name[i:i+1]:>3}{categories[2].name[i:i+1]:>3}{categories[3].name[i:i+1]:>3}  ")

    for i in range(len(categories)):
        percent_list.append(round((categories[i].spent/total_spent)*100)-round((categories[i].spent/total_spent)*100)%10)

    for i in range(len(percent_list)):
        x = 1
        for dec in range(100, 0, -10):
            for row in range(x, 11):
                if percent_list[i] >= dec:
                    chart_list[row][position[i]] = "o"
            x += 1
        chart_list[11][position[i]] = "o"

    for i in range(len(chart_list)):
        chart_list[i] = "".join(chart_list[i])

    return "\n".join(chart_list)



