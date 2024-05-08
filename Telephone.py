’’’Consider telephone book database of N clients. Make use of a hash table
implementation to quickly look up client’s telephone number. Make use
of two collision handling techniques and compare them using number of
comparisons required to find a set of telephone numbers.’’’

//python assignment 1

class node:
    def __init__(self):
        self.name = ""
        self.phnum = ""
        self.key = 0
        self.next = None

hash = [None] * 10

class Database:
    def sum(self, name):
        sum = 0
        for i in range(len(name)):
            sum = sum + ord(name[i])
        return sum

    def create(self):
        temp = node()
        print("Enter the name:")
        temp.name = input()
        print("Enter the Phone Number:")
        temp.phnum = input()
        temp.next = None
        z = self.sum(temp.name)
        temp.key = z % 10
        return temp

    def position(self, p, key):
        if not hash[key]:
            hash[key] = p
        else:
            q = hash[key]
            while q.next:
                q = q.next
            q.next = p

    def add(self):
        p = self.create()
        self.position(p, p.key)
        while p:
            print(p.name + ":" + p.phnum + " ")
            p = p.next

    def search(self, key, name):
        p = hash[key]
        while p and name != p.name:
            p = p.next
        return p

obj = Database()
n1 = node()
a = ""
key = 0
x = 0
ch = 0

while True:
    print("\n===========HASH TABLE=============")
    print("\n1. Add a Entry in hash table")
    print("\n2. Search a number")
    print("\nEnter your choice :")
    print("========================================")
    ch = int(input())
    
    if ch == 1:
        while True:
            obj.add()
            print("Do you want to Add more Entries?(1.Yes 2.No)")
            x = int(input())
            if x != 1:
                break
    
    elif ch == 2:
        print("Enter the name of the person : ")
        a = input()
        z = obj.sum(a)
        key = z % 10
        p = obj.search(key, a)
        if not p:
            print("No such Entry in DataBase")
        else:
            print("Name : " + p.name)
            print("Phone Number : " + p.phnum)
    
    else:
        print("Invalid Entry")
    
    print("Do you want to continue?(1.Yes 2.No)")
    x = int(input())
    if x != 1:
        break

