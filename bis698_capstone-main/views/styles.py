import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk


class Style():
    page_heading = ('Poppins',20,'bold')
    page_heading_color = "#006064"
    subheading_color = '#424242'
    subheading = ('Poppins',13,'bold')
    caption = ('Arial',10)
    level_one_subheading_color = '#424242'
    level_one_subheading = ('Poppins',15,'bold')
    level_three_subheading = ('Poppins',13)




    top_percent = 20
    bottom_percent = 80
    left_percent = 30
    right_percent = 70

    def __init__(self):
        pass


    @staticmethod
    def center_window(window):
        window.update_idletasks()  # Ensure that window dimensions are updated
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        width = window.winfo_reqwidth()
        height = window.winfo_reqheight()

        x = int((screen_width*Style.left_percent/100) + (screen_width * (1 - Style.right_percent/100) - width) // 2)
        y = int((screen_height * Style.top_percent / 100) + (screen_height * (1 - Style.bottom_percent / 100) - height) // 2)

        window.geometry(f"+{x}+{y}")


    def resize_image(size,image_url):
            # Load the original image
            original_image = Image.open(f'{image_url}')
            resized_image = original_image.resize((size[0], size[1]))   
            tk_image = ImageTk.PhotoImage(resized_image)
            return tk_image
