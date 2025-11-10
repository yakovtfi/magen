 #x = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34]
#y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#count = 0
#for i in range(len(x) - 2):
   # if x[i] + x[i + 2] == x[i + 1] * 2:
        #y[count] = x[i]
       # count += 1
#print(y)

#list_a, list_b, list_c = [], [], []

#for num in range(4):
   # list_a.append(num * 2)
#print(list_a)
#mid = len(list_a) // 2
#max_val = max(list_a)
#info = {"mid": mid, "max_val": max_val}
#for i in range(info["max_val"]):
    #if i < len(list_a):
       # item = list_a[i]
       # list_b.append(item + 1)
    #else:
       # list_b.append(i % 3)
#print(list_b)
#while len(list_b) > 1:
    #x = list_b.pop(0) * list_b.pop(0)
    #list_c.append(x)
#print(list_c)
#is_max_in_list = info['max_val'] in list_c
#print(is_max_in_list)
#print(is_max_in_list or bool(len(list_a)))

#x = 5
#for i in range(x):
#s = ""
   # for j in range(x - i):
       # s += str(x - i - j)
   # print(s)

#'] in list_3)
from library import Library
from models.book import Book
from models.user import User
import storage
from utils import input_nonempty

def print_menu():
    print("""
---- Library System ----
1. Add Book
2. Add User
3. Borrow Book
4. Return Book
5. Show Available Books
6. Search Book
7. Export CSV
8. Save & Exit
""")

def main():
    books, users = storage.load_data()
    lib = Library(books=books, users=users)
    while True:
        print_menu()
        choice = input("Enter choice: ").strip()
        if choice == "1":
            title = input_nonempty("Title: ")
            author = input_nonempty("Author: ")
            isbn = input_nonempty("ISBN: ")
            try:
                lib.add_book(Book(title=title, author=author, isbn=isbn))
                print("Book added.")
            except ValueError as e:
                print("Error:", e)
        elif choice == "2":
            name = input_nonempty("Name: ")
            id_ = input_nonempty("ID: ")
            try:
                lib.add_user(User(name=name, id=id_))
                print("User added.")
            except ValueError as e:
                print("Error:", e)
        elif choice == "3":
            user_id = input_nonempty("User ID: ")
            isbn = input_nonempty("Book ISBN: ")
            print(lib.borrow_book(user_id, isbn))
        elif choice == "4":
            user_id = input_nonempty("User ID: ")
            isbn = input_nonempty("Book ISBN: ")
            print(lib.return_book(user_id, isbn))
        elif choice == "5":
            available = lib.list_available_books()
            if not available:
                print("No available books.")
            else:
                for b in available:
                    print(b)
        elif choice == "6":
            q = input_nonempty("Enter title or author: ")
            res = lib.search_books(q)
            if not res:
                print("No results.")
            else:
                for b in res:
                    print(b)
        elif choice == "7":
            storage.export_csv(lib.books, lib.users)
            print("Data exported to data/books.csv and data/users.csv")
        elif choice == "8":
            storage.save_data(lib.books, lib.users)
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()