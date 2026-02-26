library = {}

while True:
    print("\n1.Add Book    2.View Books \n3.Issue Book  4.Return Book \n5.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        book_id = input("Book ID: ")
        title = input("Title: ")
        library[book_id] = {"title": title, "available": True}
        print("Book Added!")

    elif choice == "2":
        for b_id, info in library.items():
            status = "Available" if info["available"] else "Issued"
            print(b_id, "-", info["title"], "-", status)

    elif choice == "3":
        book_id = input("Enter Book ID: ")
        if book_id in library and library[book_id]["available"]:
            library[book_id]["available"] = False
            print("Book Issued!")
        else:
            print("Not Available!")

    elif choice == "4":
        book_id = input("Enter Book ID: ")
        if book_id in library:
            library[book_id]["available"] = True
            print("Book Returned!")

    elif choice == "5":
        break

    else:
        print("Invalid Choice!")