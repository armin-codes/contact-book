import time


class Contact:
	def __init__(self, name, number, title):
		self.name = name
		self.number = number
		self.title = title


def save_contact(contact):
	with open("contacts.txt", "a") as f:
		f.write(f"{contact.name},{contact.number},{contact.title}\n")
		time.sleep(0.5)


def delete_contact(name):
	with open("contacts.txt", "r") as f:
		lines = f.readlines()

	for i in range(len(lines)):
		line = lines[i]
		name_in_file, number_in_file, title_in_file = line.strip().split(",")
		if name_in_file == name:
			lines.remove(line)
			break

	with open("contacts.txt", "w") as f:
		f.writelines(lines)
		time.sleep(0.5)
	print(f"The contact {name} was deleted successfully.\n")


def edit_contact(name):
	contact = search_contact(name)

	# Validate the user's input.
	while choice not in ["change number", "change name", "change title", "delete contact", "cancel"]:
		print("Invalid input. Please enter change number, change name, change title, delete contact, or cancel.")
		choice = input("Enter your choice: ")
		time.sleep(0.5)

	# If the user wants to delete the contact, remove it from the file and return None.
	if choice == "delete contact":
		delete_contact(name)
		time.sleep(0.5)
		return None

	# If the user wants to change the number, prompt them for the new number and update the contact object.
	elif choice == "change number":
		new_number = input("Enter the new number of the contact: ")
		contact.number = new_number
		time.sleep(0.5)

	# If the user wants to change the name, prompt them for the new name and update the contact object.
	elif choice == "change name":
		new_name = input("Enter the new name of the contact: ")
		contact.name = new_name
		time.sleep(0.5)

	# If the user wants to change the title, prompt them for the new title and update the contact object.
	elif choice == "change title":
		new_title = input("Enter the new title of the contact: ")
		contact.title = new_title
		time.sleep(0.5)

	# If the user cancels, exit the function and return the current contact information.
	else:
		return contact

	# Save the updated contact object to the file.
	delete_contact(name)
	time.sleep(0.5)
	save_contact(contact)
	print(f"\nThe contact {name} has been updated successfully.")


def add():
	name = input("\nEnter the name of the person: ")
	time.sleep(0.5)
	number = input("\nEnter the number of the person: ")
	time.sleep(0.5)
	title = input("\nEnter the title of the person (optional): ")
	time.sleep(0.5)

	# If the title is empty, set it to None.
	if title == "":
		title = None

	# Create a new contact object and save it to the file.
	contact = Contact(name, number, title)
	save_contact(contact)

	print(f"\nThe contact {name} was added successfully.")


def search_contact(query, search_by="name"):
	# Searches for a contact in the file based on the search criteria.
	with open("contacts.txt", "r") as f:
		for line in f:
			name_in_file, number_in_file, title_in_file = line.strip().split(",")
			if search_by == "name" and name_in_file == query:
				return Contact(name_in_file, number_in_file, title_in_file)
			elif search_by == "number" and number_in_file == query:
				return Contact(name_in_file, number_in_file, title_in_file)
	return None


def choice():
	# Ask the user to search, add, edit, or quit
	choice = input("Do you want to...\n(search/add/edit/quit): ")
	choice = choice.lower() # lower the input word for the program to read it

	# Validate the user's input.
	while choice not in ("search", "add", "edit", "quit"):
		print("Invalid input. Please enter 'search', 'add', 'edit', or 'quit'.")
		choice = input("Do you want to search for a contact, add a new contact, edit a contact info, or quit?\n: ")
		choice = choice.lower() # lower the input word for the program to read it
	return choice


def main(choice):
	time.sleep(0.5)
	choice = choice()
	# Run the main loop forever until the user quits.
	while True:
		# If the user wants to search for a contact, prompt them for the name of the contact and search for them.
		if choice == "search":
			name = input("Enter the name of the contact: ")
			number = search_contact(name)

			# If the contact doesn't exist, print a message to the user.
			if name not in 'contact.txt':
				print(f"The contact {name} doesn't exist.")
			else:
				print(f"The number of {name} is {number}.")

		# If the user wants to add a new contact...
		elif choice == "add":
			add() # prompt them for the name and number of the contact and save it to the file.

		# If the user wants to edit an existing contact, prompt them for the name of the contact and edit their information.
		elif choice == "edit":
			name = input("Enter the name of the contact: ")
			contact = search_contact(name)
			if contact:
				edit_contact(contact)

		# If the user wants to quit... break the loop to exit the program.
		elif choice == "quit":
			break # break the loop to exit the program.

		# Ask the user to search, add, edit, or quit again.
		choice = input("Do you want to...\n(search/add/edit/quit): ")
		choice = choice.lower() # lower the input word for the program to read it


if __name__ == '__main__':
	choice = choice()
	main(choice)
