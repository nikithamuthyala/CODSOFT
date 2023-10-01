import tkinter as tk
from tkinter import messagebox

# Create an empty list to store contacts
contacts = []

# Function to add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    
    if name and phone:
        contact = {
            'Name': name,
            'Phone': phone,
            'Email': email,
            'Address': address
        }
        contacts.append(contact)
        clear_entries()
        messagebox.showinfo('Success', 'Contact added successfully!')
    else:
        messagebox.showerror('Error', 'Name and phone number are required fields.')

# Function to display the contact list
def view_contacts():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")

# Function to search for a contact
def search_contact():
    query = search_entry.get()
    matching_contacts = []
    
    for contact in contacts:
        if query.lower() in contact['Name'].lower() or query in contact['Phone']:
            matching_contacts.append(f"{contact['Name']} - {contact['Phone']}")
    
    contact_list.delete(0, tk.END)
    for contact in matching_contacts:
        contact_list.insert(tk.END, contact)

# Function to update a contact
def update_contact():
    selected_index = contact_list.curselection()
    
    if selected_index:
        selected_index = int(selected_index[0])
        updated_name = name_entry.get()
        updated_phone = phone_entry.get()
        updated_email = email_entry.get()
        updated_address = address_entry.get()
        
        if updated_name and updated_phone:
            contacts[selected_index]['Name'] = updated_name
            contacts[selected_index]['Phone'] = updated_phone
            contacts[selected_index]['Email'] = updated_email
            contacts[selected_index]['Address'] = updated_address
            clear_entries()
            view_contacts()
            messagebox.showinfo('Success', 'Contact updated successfully!')
        else:
            messagebox.showerror('Error', 'Name and phone number are required fields.')
    else:
        messagebox.showerror('Error', 'Select a contact to update.')

# Function to delete a contact
def delete_contact():
    selected_index = contact_list.curselection()
    
    if selected_index:
        selected_index = int(selected_index[0])
        del contacts[selected_index]
        clear_entries()
        view_contacts()
        messagebox.showinfo('Success', 'Contact deleted successfully!')
    else:
        messagebox.showerror('Error', 'Select a contact to delete.')

# Function to clear input fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    search_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title('Contact Manager')

# Create input fields and labels
name_label = tk.Label(root, text='Name:')
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

phone_label = tk.Label(root, text='Phone:')
phone_label.pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

email_label = tk.Label(root, text='Email:')
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

address_label = tk.Label(root, text='Address:')
address_label.pack()
address_entry = tk.Entry(root)
address_entry.pack()

search_label = tk.Label(root, text='Search:')
search_label.pack()
search_entry = tk.Entry(root)
search_entry.pack()

# Create buttons for various actions
add_button = tk.Button(root, text='Add Contact', command=add_contact)
add_button.pack()

view_button = tk.Button(root, text='View Contacts', command=view_contacts)
view_button.pack()

search_button = tk.Button(root, text='Search Contact', command=search_contact)
search_button.pack()

update_button = tk.Button(root, text='Update Contact', command=update_contact)
update_button.pack()

delete_button = tk.Button(root, text='Delete Contact', command=delete_contact)
delete_button.pack()

# Create a listbox to display contacts
contact_list = tk.Listbox(root, width=40, height=10)
contact_list.pack()

# Start the GUI main loop
root.mainloop()
