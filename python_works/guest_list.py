# 3-4.creating list of invitees to a dinner:
dinner_guest = ['jowe', 'angi', 'bob']

print(f"I am inviting {dinner_guest[0].title()} to my dinner party!")
print(f"I am inviting {dinner_guest[1].title()} to my dinner party!")
print(f"I am inviting {dinner_guest[2].title()} to my dinner party!")

# 3-5.Changing guest list:
# Modifying a dinner guest who can't make to the dinner
print(f"{dinner_guest[1].title()} requested she can't make it to the dinner")

#Replacing/Modifying my initial guest to a new guest
dinner_guest[1] = 'doe'

print(f"I am inviting {dinner_guest[0].title()} to my dinner party!")
print(f"I am inviting {dinner_guest[1].title()} to my dinner party!")
print(f"I am inviting {dinner_guest[2].title()} to my dinner party!")


# 3-6.More Guests:

print("=======================")
print(f"There is an open space at the dinner. Invitation is widely open now")

dinner_guest.insert(0, 'angi')

dinner_guest.insert(2, 'sam')

dinner_guest.append('joe')

print(f"I am inviting {dinner_guest[0].title()} to my dinner party!")
print(f"I am inviting {dinner_guest[1].title()} to my dinner party!")
print(f"I am inviting {dinner_guest[2].title()} to my dinner party!")
print(f"I am inviting {dinner_guest[3].title()} to my dinner party!")
print(f"I am inviting {dinner_guest[4].title()} to my dinner party!")

# 3-7. Shrinking Guest List:
print("========================================")
print(f"My attention has been drawn that spaces have been limited to only two guests.")

poppedup_list1 = dinner_guest.pop()
poppedup_list2 = dinner_guest.pop()
poppedup_list3 = dinner_guest.pop()
poppedup_list4 = dinner_guest.pop()


print(f"{poppedup_list1.title()} i am sorry for the cancelation of your invitation.")
print(f"{poppedup_list2.title()} i am sorry for the cancelation of your invitation.")
print(f"{poppedup_list3.title()} i am sorry for the cancelation of your invitation.")
print(f"{poppedup_list4.title()} i am sorry for the cancelation of your invitation.")

print("===================================")
print(f"{dinner_guest[0].title()} you guys are still invited!")
print(f"{dinner_guest[1].title()} you guys are still invited!")

print("==============================")
del dinner_guest[0]
del dinner_guest[0]


print(dinner_guest)