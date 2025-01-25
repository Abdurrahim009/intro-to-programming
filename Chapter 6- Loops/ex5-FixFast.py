sandwich_orders = ['tuna', 'ham', 'pastrami', 'turkey', 'pastrami', 'veggie', 'pastrami']

finished_sandwiches = []


print("The deli has run out of pastrami!")


while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')


for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)



print("\nAll sandwiches made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")
