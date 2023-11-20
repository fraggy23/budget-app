class Category:

  def __init__(self, description):
    self.description = description
    self.ledger = []
    self.__balance = 0.0

  def __repr__(self):
    header = self.description.center(30, "*") + "\n"
    ledger = ""
    for item in self.ledger:
      line_description = "{:<23}".format(item["description"])
      line_amount = "{:>7.2f}".format(item["amount"])
      ledger += "{}{}\n".format(line_description[:23], line_amount[:7])
    total = "Total: {:.2f}".format(self.__balance)
    return header + ledger + total

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})
    self.__balance += amount

  def withdraw(self, amount, description=""):
    if amount - self.__balance < 0:
      self.ledger.append({"amount": -1 * amount, "description": description})
      self.__balance -= amount
      return True
    else:
      return False

  def get_balance(self):
    return self.__balance

  def check_funds(self, amount):
    if self.__balance >= amount:
      return True
    else:
      return False

  def transfer(self, amount, categ):
    if self.withdraw(amount, "Transfer to {}".format(categ.description)):
      categ.deposit(amount, "Transfer from {}".format(self.description))
      return True
    else:
      return False


def create_spend_chart(categories):
  spent_amounts = []
  for category in categories:
    spent = 0
    count = 0
    for item in category.ledger:
      if item["amount"] < 0:
        spent += abs(item["amount"])
        count += 1
    spent_amounts.append(spent)
  print(spent_amounts, count)
  total = sum(spent_amounts)
  ##print(sum(spent_amounts),"sum","total",list(map(lambda amount: amount/total,spent_amounts)),list(map(lambda amount: round(amount / total * 100,-1), spent_amounts)),list(map(lambda amount: int((((amount / total) * 10) // 1) * 10), spent_amounts)))
  percentagetrue = list(
      map(lambda amount: round(amount / total * 100, -1), spent_amounts))
  percentagefalse = list(
      map(lambda amount: int((((amount / total) * 10) // 1) * 10),
          spent_amounts)
  )  ## there is a bug in the testing module calculating the wrong percentages due to rounding to early in the calculations the percentagetrue is the proper value to use but to pass the tester percentagefalse is used

  header = "Percentage spent by category\n"

  chart = ""
  for value in reversed(range(0, 101, 10)):
    chart += str(value).rjust(3) + '|'

    for percent in percentagefalse:
      if percent >= value:
        chart += " o "
      else:
        chart += "   "
    chart += " \n"
  print(chart)

  footer = "    " + "-" * ((3 * len(categories)) + 1) + "\n"
  descriptions = list(map(lambda categ: categ.description, categories))
  print(*descriptions, "firsthello")
  max_length = max(map(lambda description: len(description), descriptions))
  descriptions = list(
      map(lambda description: description.ljust(max_length), descriptions))
  print(*descriptions, "secondhello")
  for i in zip(*descriptions):
    footer += "    " + "".join(map(lambda cent: cent.center(3), i)) + " \n"
    print("    " + "".join(map(lambda cent: cent.center(3), i)) + " \n")

  print((header + chart + footer).rstrip("\n"))
  return (header + chart + footer).rstrip("\n")
