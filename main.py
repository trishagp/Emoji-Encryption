from tkinter import *
from tkinter import messagebox
import json

# ----------------------------CONSTANTS ------------------------------- #
BACKGROUND_COLOUR = "#E3A5C7"
FONT_NAME = "Courier"
LABEL_BG = "#FFF078"
TEXT_COLOUR = "#000000"


# ---------------------------- ENCRYPTION ------------------------------- #
def encrypt():
    message = encrypt_entry.get()
    with open("special_data.json", "r") as data_file:
        data = json.load(data_file)
        try:
            emoji_list = [data[letter] for letter in message]
        except KeyError as error_message:
            # print(f"This {error_message} character does not exist.")
            messagebox.showinfo(title="Oops", message=f"This ' {error_message} ' character does not exist.\n"
                                                      f"Try again")
        else:
            emoji_message = ''.join(emoji_list)
            encrypted_output_label.config(text=emoji_message)


# ---------------------------- DECRYPTION ------------------------------- #
def decrypt():
    message = decrypt_entry.get()
    text_list = []
    with open("special_data.json", "r") as data_file:
        data = json.load(data_file)
        for emoji_letter in message:
            counter = 0
            text = ''
            for (key, value) in data.items():
                if emoji_letter == value:
                    counter += 1
                    text = key
                    break
            if counter > 0:
                text_list.append(text)
            else:
                # print(f"This '{emoji_letter}' character does not exist.")
                messagebox.showinfo(title="Oops", message=f"This '{emoji_letter}' character does not exist.\n"
                                                          f"Try again")
        text_message = ''.join(text_list)
    if text_message != "":
        decrypted_output_label.config(text=text_message)


# -------------------- Creating and saving own custom emoji mappings.  ----------------------- #
def custom():
    key = custom_key.get()
    value = custom_value.get()
    new_data = {
        key: value,
    }
    if key == "" or value == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_okay = messagebox.askokcancel(title="Saving Data", message=f"These are the details entered:\nKey: {key}"
                                                                      f"\nValue: {value} \nIs it okay?")
        if is_okay:
            try:
                with open("special_data.json", "r", encoding="utf8") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                with open("special_data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=2)

            else:
                # Updating old data with new data
                data.update(new_data)
                with open("special_data.json", "w") as data_file:
                    # Saving old data
                    json.dump(data, data_file, indent=2)


# -------------------- Clearing the entered texts and outputs  ----------------------- #
def clear():
    encrypt_entry.delete(0, END)
    encrypt_entry.insert(END, "Enter text")
    encrypted_output_label.config(text="Output")
    decrypt_entry.delete(0, END)
    decrypt_entry.insert(END, "Enter text")
    decrypted_output_label.config(text="Output")
    custom_key.delete(0, END)
    custom_key.insert(END, "Enter key")
    custom_value.delete(0, END)
    custom_value.insert(END, "Enter value")


# ---------------------------- UI ------------------------------- #
window = Tk()
window.title("EmojCrypt ")
window.minsize(height=400, width=300)
window.config(padx=100, pady=50, bg=BACKGROUND_COLOUR)

label = Label(text="Welcome to EmojCrypt\n", bg=BACKGROUND_COLOUR, fg=TEXT_COLOUR, font=(FONT_NAME, 25))
label.grid(row=0, column=0, columnspan=3, sticky=EW)

# ----- UI for Encryption -----#
encrypt_label = Label(text="Encryption", bg=BACKGROUND_COLOUR, fg=TEXT_COLOUR, font=(FONT_NAME, 14))
encrypt_label.grid(row=1, column=1)
encrypt_entry = Entry(width=20)
encrypt_entry.insert(END, "Enter text")
encrypt_entry.grid(row=2, column=0)
arrow_label1 = Label(text="---->", bg=BACKGROUND_COLOUR, fg=TEXT_COLOUR, font=(FONT_NAME, 10))
arrow_label1.grid(row=2, column=1)
encrypted_output_label = Label(text="Output", bg=LABEL_BG, fg=TEXT_COLOUR, font=(FONT_NAME, 10), width=20)
encrypted_output_label.grid(row=2, column=2)
encrypt_button = Button(text="Go", command=encrypt)
encrypt_button.grid(row=2, column=3)

# ----- UI for Decryption -----#
decrypt_label = Label(text="Decryption", bg=BACKGROUND_COLOUR, fg=TEXT_COLOUR, font=(FONT_NAME, 14))
decrypt_label.grid(row=3, column=1)
decrypt_entry = Entry(width=20)
decrypt_entry.insert(END, "Enter text")
decrypt_entry.grid(row=4, column=0)
arrow_label2 = Label(text="---->", bg=BACKGROUND_COLOUR, fg=TEXT_COLOUR, font=(FONT_NAME, 10))
arrow_label2.grid(row=4, column=1)
decrypted_output_label = Label(text="Output", bg=LABEL_BG, fg=TEXT_COLOUR, font=(FONT_NAME, 10), width=20)
decrypted_output_label.grid(row=4, column=2)
decrypt_button = Button(text="Go", command=decrypt)
decrypt_button.grid(row=4, column=3)

# ----- UI for Customization -----#
custom_label = Label(text="Custom", bg=BACKGROUND_COLOUR, fg=TEXT_COLOUR, font=(FONT_NAME, 14))
custom_label.grid(row=5, column=1)
custom_key = Entry(width=20)
custom_key.insert(END, "Enter key")
custom_key.grid(row=6, column=0)
custom_value = Entry(width=20)
custom_value.insert(END, "Enter value")
custom_value.grid(row=6, column=1)
save_button = Button(text="Save", command=custom)
save_button.grid(row=6, column=2)

# ----- UI for Clearing the screen -----#
clear_all_button = Button(text="Clear All", command=clear)
clear_all_button.grid(row=7, column=3)

window.mainloop()

# 😀😁
