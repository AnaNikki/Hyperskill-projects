print(f"Prices:")
print(f"Bubblegum: $2")
print(f"Toffee: $0.2")
print(f"Ice cream: $5")
print(f"Milk chocolate: $4")
print(f"Doughnut: $2.5")
print(f"Pancake: $3.2")

gum = 202
tof = 118
ice = 2250
milk = 1680
dough = 1075
cake = 80

total_income = gum + tof + ice + milk + dough + cake

print()
print(f"Earned amount:")
print(f"Bubblegum: ${gum}")
print(f"Toffee: ${tof}")
print(f"Ice cream: ${ice}")
print(f"Milk chocolate: ${milk}")
print(f"Doughnut: ${dough}")
print(f"Pancake: ${cake}")

print()
print(f"Income: ${total_income}")

print(f"Staff expenses:")
staff_expenses = int(input())

print(f"Other expenses:")
other_expenses = int(input())

net_income = total_income - staff_expenses - other_expenses
print(f"Net income: ${net_income}")
