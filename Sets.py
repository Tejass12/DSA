To create ADT that implement the "set" concept.
a. Add (new Element) -Place a value into the set,
b. Remove (element) Remove the value
c. Contains (element) Return true if element is in collection,
d. Size () Return number of values in collection Iterator () Return an
iterator used to loop over collection,
e. Intersection of two sets,
f. Union of two sets,
g. Difference between two sets,
h. Subset


def main_menu():
    print("1. Insertion of element in sets")
    print("2. Deletion of element from sets")
    print("3. Display elements of sets")
    print("4. Search element in sets")
    print("5. Union of two sets")
    print("6. Intersection of two sets")
    print("7. Difference of two sets")
    print("8. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        r = int(input("In which set you want to insert element (1 or 2): "))
        if r == 1:
            ne = int(input("Enter element you want to insert in set 1: "))
            S1.add(ne)
        elif r == 2:
            ne = int(input("Enter element you want to insert in set 2: "))
            S2.add(ne)
        else:
            print("Invalid input")
        main_menu()
    elif ch == 2:
        r = int(input("In which set you want to delete element (1 or 2): "))
        if r == 1:
            de = int(input("Enter element you want to delete from set 1: "))
            S1.remove(de)
        elif r == 2:
            de = int(input("Enter element you want to delete from set 2: "))
            S2.remove(de)
        else:
            print("Invalid input")
        main_menu()
    elif ch == 3:
        print("First Set is:", S1)
        print("Second Set is:", S2)
        main_menu()
    elif ch == 4:
        s = int(input("In which set you want to search element (1 or 2): "))
        if s == 1:
            se = int(input("Which element you want to search in set 1: "))
            if se in S1:
                print(se, "is present in set 1")
            else:
                print(se, "is not present in set 1")
        elif s == 2:
            se = int(input("Which element you want to search in set 2: "))
            if se in S2:
                print(se, "is present in set 2")
            else:
                print(se, "is not present in set 2")
        else:
            print("Invalid input")
        main_menu()
    elif ch == 5:
        print("Union is:", S1 | S2)
        main_menu()
    elif ch == 6:
        print("Intersection is:", S1 & S2)
        main_menu()
    elif ch == 7:
        print("Difference is:")
        print("Difference of (set 1 - set 2):", S1 - S2)
        print("Difference of (set 2 - set 1):", S2 - S1)
        main_menu()
    elif ch == 8:
        print("Thank you")
    else:
        print("Invalid input")
        main_menu()

n = int(input("Enter the number of elements in set 1: "))
S1 = set()
for i in range(n):
    a = int(input("Enter the values of set 1: "))
    S1.add(a)
print("First Set is:", S1)

n = int(input("Enter the number of elements in set 2: "))
S2 = set()
for i in range(n):
    a = int(input("Enter the values of set 2: "))
    S2.add(a)
print("Second Set is:", S2)

main_menu()



