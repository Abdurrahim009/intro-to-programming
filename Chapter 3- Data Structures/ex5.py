guests = ["Nelson Mandela", "Maya Angelou", "Albert Einstein"]

for guest in guests:
    
    print(f"Dear {guest}, I would be honored to invite you to dinner!")


print("\nUnfortunately, Albert Einstein can't make it to the dinner.")

guests[2] = "Isaac Newton"

print("\nUpdated invitations:")

for guest in guests:

    print(f"Dear {guest}, I would be honored to invite you to dinner!")