import tkinter as tk
from views.authentication import AuthenticationScreen
from home import Home

# import controllers.users as u

import sys
import os



# Get the absolute path of the 'mod' directory
main_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(main_dir)

# Add the parent directory (containing 'mod') to the Python path
sys.path.append(parent_dir)

if __name__ == "__main__":
    root = tk.Tk()
    auth_screen = AuthenticationScreen(root)
    root.mainloop()


# if __name__ == "__main__":
#     root = tk.Tk()
#     home_screen = Home(root)
#     root.mainloop()

