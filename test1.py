from tkinter import *
from tkinter import filedialog

def upload_resume():
    resume_file = filedialog.askopenfilename(title="Select Resume File", filetypes=(("PDF Files", "*.pdf"), ("All Files", "*.*")))
    if resume_file:
        print("Resume uploaded:", resume_file)
        # You can perform further processing with the resume file here

def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    print("Name:", name)
    print("Email:", email)
    # You can perform further processing with the name and email here

root = Tk()
root.title("Resume Uploader")

# Name Label and Entry
name_label = Label(root, text="Name:")
name_label.pack()
name_entry = Entry(root)
name_entry.pack()

# Email Label and Entry
email_label = Label(root, text="Email:")
email_label.pack()
email_entry = Entry(root)
email_entry.pack()

# Upload Button
upload_button = Button(root, text="Upload Resume", command=upload_resume)
upload_button.pack()

# Submit Button
submit_button = Button(root, text="Submit", command=submit_form)
submit_button.pack()

root.mainloop()