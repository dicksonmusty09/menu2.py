import customtkinter as ctk 
from PIL import Image , ImageTk
from CTkMessagebox import CTkMessagebox


ctk.set_appearance_mode('white')
ctk.set_default_color_theme('green')

def start_meeting():
    meeting_id = meeting_id_entry.get()
    CTkMessagebox.showinfo("Meeting App", f"Started meeting with ID: {meeting_id}")

def schedule_meeting():
    meeting_id = meeting_id_entry.get()
    CTkMessagebox.showinfo("Meeting App", f"schedule meeting with ID: {meeting_id}")



# Create the main window
# root = ctk.CTk()
# root.title("Meeting App")

if __name__ == '__main__':
    sub_root = ctk.CTk()
    sub_root.geometry('1920 x 1080')
    sub_root.title('Unikom')
    sub_root.iconbitmap('unikom.ico')
 


# Load the background image
bg_image = ImageTk.PhotoImage(file="image3.png") 
# Create a label to display the background image
bg_label = ctk.CTkLabel(sub_root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)


# Label and Entry for Meeting ID
meeting_id_label = ctk.CTkLabel(sub_root, text="Meeting ID:")
meeting_id_label.grid()
meeting_id_entry = ctk.CTkEntry(sub_root)
meeting_id_entry.grid()




#Buttons to Start and schedule
# Meetings
start_button = ctk.CTkButton(sub_root, text="Start Meeting", command=start_meeting)
start_button.grid(row = 3, column = 0, pady= (0, 20))

schedule_button = ctk.CTkButton(sub_root, text="schedule Meeting", command=schedule_meeting)
schedule_button.grid(row = 3, column = 0, pady= (10, 20))




# Start the Tkinter main loop
sub_root.mainloop()
