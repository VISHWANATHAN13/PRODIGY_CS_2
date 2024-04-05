import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def encrypt_image(image_path, key):
    """
    Encrypts the image using XOR encryption.
    """
    image = Image.open(image_path)
    encrypted_pixels = []
    for pixel in image.getdata():
        encrypted_pixel = tuple((p ^ key) for p in pixel)
        encrypted_pixels.append(encrypted_pixel)
    encrypted_image = Image.new(image.mode, image.size)
    encrypted_image.putdata(encrypted_pixels)
    return encrypted_image

def select_image():
    """
    Allows user to select an image file.
    """
    file_path = filedialog.askopenfilename()
    if file_path:
        image = Image.open(file_path)
        image.thumbnail((300, 300))
        photo = ImageTk.PhotoImage(image)
        canvas.image = photo
        canvas.create_image(150, 150, image=photo)
        encrypt_button.config(state=tk.NORMAL)
        global selected_image_path
        selected_image_path = file_path

def encrypt_and_save():
    """
    Encrypts the selected image and saves it.
    """
    if selected_image_path:
        key = int(key_entry.get())
        encrypted_image = encrypt_image(selected_image_path, key)
        save_path = filedialog.asksaveasfilename(defaultextension=".png")
        if save_path:
            encrypted_image.save(save_path)


root = tk.Tk()
root.title("Image Encryption")


canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()
select_button = tk.Button(root, text="Select Image", command=select_image)
select_button.pack()
key_label = tk.Label(root, text="Encryption Key:")
key_label.pack()
key_entry = tk.Entry(root)
key_entry.pack()
encrypt_button = tk.Button(root, text="Encrypt & Save", command=encrypt_and_save, state=tk.DISABLED)
encrypt_button.pack()
selected_image_path = None

root.mainloop()
