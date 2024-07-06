import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import *
from PIL import Image, ImageTk
from tkinter import *
from turtle import *
import numpy as np
import pandas as pd
from datetime import datetime, timedelta


root = tk.Tk()
img = PhotoImage(file=r"D:\adsa\Screenshot_20240521_213743.png")
lbl = tk.Label(root, image=img)
lbl.image = img
lbl.place(relx=0.5, rely=0.5, anchor='center')

movi = []




def add():
    if no_movie.get() == None:
        messagebox.showinfo('please enter yes or no for ensuring changes', parent=root)


    elif no_movie.get() == 'yes' or 'YES':
        result = schedule_shows(final, movi)
        text_widget.delete("1.0", tk.END)

        text_widget.insert(END, '\t\t**Welcome**\n\n')
        for i in result:
            text_widget.insert(END, f'{i}\n')


        for entry in result:
            print(entry)

    else:
        m = []
        text_widget.delete("1.0", tk.END)
        result =schedule_shows(final,m)
        text_widget.delete("1.0", tk.END)

        text_widget.insert(END, '\t\t**Welcome**\n\n')
        for i in result:
            text_widget.insert(END, f'{i}\n\n')


def adding_movies():
    if movie_name_entry.get() is None or movie_duration.get() is None or movie_start.get() is None:
        messagebox.showerror('PLEASE ENTER THE MOVIE DETAILS!!', parent = root)
    else:
        n1 = movie_duration.get()
        n2  = movie_start.get()
        start_time = datetime.strptime(n2, "%H:%M")

        n1 = int(n1)


        movi.append((movie_name_entry.get(),n1 ,start_time))
        movie_name_entry.delete(0, END)
        movie_duration.delete(0, END)
        movie_start.delete(0, END)
        print(movi)
        messagebox.showinfo('successfully added', parent=root)




movie_name_label = tk.Label(root, text="Movie Name:", font=('times new roman', 15, 'bold'), bg='gray20',
                            fg='gold')
movie_name_label.place(x=1050, y=90)
movie_name_entry = Entry(root, font=('arial', 15), bd=7, width=20)
movie_name_entry.place(x=1200, y=90)

movie_rating_label = tk.Label(root, text="Duration:", font=('times new roman', 15, 'bold'), bg='gray20',
                              fg='gold')
movie_rating_label.place(x=1050, y=150)
#global movie_duration
movie_duration = Entry(root, font=('arial', 15), bd=7, width=20)
movie_duration.place(x=1200, y=150)


movie_rating_label = tk.Label(root, text=f'Starting Time\n Format 24 hrs', font=('times new roman', 15, 'bold'), bg='gray20',
                              fg='gold')
movie_rating_label.place(x=1050, y=210)
movie_start = Entry(root, font=('arial', 15), bd=7, width=20)
movie_start.place(x=1200, y=210)





add_button = tk.Button(root, text="Add Movie", font=('arial', 12, 'bold'), bd=7, width=10,command=adding_movies)
add_button.place(x=1300, y=300)



# Part 2: Project Loan Approval
def trend():
    text_widget.delete("1.0", tk.END)
    text_widget.insert(END, '\t\t**Welcome**\n\n')
    text_widget.insert(END, 'SHOW\t\tPOPULARITY\n\n')
    for i in range(len(opt_show)):
        text_widget.insert(END, f'{opt_show[i][0]}\t\t{opt_show[i][2]}\n')
def movies():
    text_widget.delete("1.0", tk.END)
    
    
    file_path1 = r"D:\adsa\animation movies.xlsx" # Update this with the correct path to your Excel file
    data1 = pd.read_excel(file_path1)

    # Convert the data to a list of tuples
    mov = list(data.itertuples(index=False, name=None))
    text_widget.insert(END, '\t\t**Welcome**\n')
    text_widget.insert(END, '\t\t**avilable movies**\n\n')

    text_widget.insert(END, 'SHOW\t\DURATION\t\tPOPULARITY\n\n')
    for i in range(len(mov)):
        text_widget.insert(END, f'{mov[i][0]}\t{mov[i][1]}\t\t{mov[i][2]}\n')

        
        

def trp():
    text_widget.delete("1.0", tk.END)
    text_widget.insert(END, '\t\t\t**Welcome**\n\n')
    text_widget.insert(END, 'SHOWS\t\t\tTRP RATE\t\tREVENUE\n\n')
    for i in range(len(result_list)):
        text_widget.insert(END, f'{result_list[i][0]}\t\t\t{result_list[i][3]}\t\t{result_list[i][4]}\n')
def showss():
    text_widget.delete("1.0", tk.END)
    text_widget.insert(END, '\t\t\t**Welcome**\n\n')
    text_widget.insert(END, 'SHOWS NAME\t\t\tDURATION\n\n')
    for i in range(len(shows)):
        text_widget.insert(END, f'{shows[i][0]}\t\t\t{shows[i][1]}\n')










root.title("ADVANCE DATA STRUCTURES PROJECT")
root.geometry("2000x850")
'''self.bg_image = tk.PhotoImage(file=r"D:/adsa/download (1).jpeg")
self.bg_label = tk.Label(self, image=self.bg_image)
self.bg_label.place(relwidth=1,relheight=1)'''
#image1=Image.open(r"D:/adsa/download (1).jpeg")
'''img = PhotoImage(file=r"C:\\Users\\adeep\\OneDrive\\Pictures\Screenshots\\Screenshot_20240521_213743.png")
lbl = tk.Label(root, image=img)
lbl.image = img
lbl.place(relx=0.5, rely=0.5, anchor='center')'''
heading = tk.Label(root, text='TV SHOW SCHEDULING', font=('times new roman', 30, 'bold'), bg='gray20',
                   fg='red', bd=12,
                   relief=GROOVE).pack(fill=X)

customer_details_frame = LabelFrame(root, text='CUSTOMER DETAILS', font=('times new roman', 15, 'bold'),
                                    bg='gray20',
                                    fg='gold', bd=8, relief=GROOVE).pack()

frame1 = tk.Frame(root, bd=8, bg='gray20', width=300, height=650, relief=GROOVE)
frame1.place(x=8, y=130)

button1 = tk.Button(frame1, text="TRENDING SHOWS", font=('arial', 12, 'bold'), bd=7, width=20,command=trend)
button1.place(x=35, y=100)

button2 = tk.Button(frame1, text="AVAILABLE MOVIES", font=('arial', 12, 'bold'), bd=7, width=20,command=movies)
button2.place(x=35, y=200)

button3 = tk.Button(frame1, text="TRP RATING", font=('arial', 12, 'bold'), bd=7, width=20,command=trp)
button3.place(x=35, y=300)

button4 = tk.Button(frame1, text="AVAILABLE SHOWS", font=('arial', 12, 'bold'), bd=7, width=20,command=showss)
button4.place(x=35, y=400)

frame2 = tk.Frame(root, bd=8, bg='gray20', width=100, height=100, relief=GROOVE)
frame2.place(x=350, y=150)

frame2 = tk.Frame(root, bd=8, bg='gray20', width=500, height=800, relief=GROOVE)
frame2.place(x=350, y=130)

text_widget = tk.Text(frame2, width=50, height=24)
text_widget.pack(side=tk.LEFT)

# Create a Scrollbar
scrollbar = tk.Scrollbar(frame2)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

frame3 = tk.Frame(root, bd=8, bg='gray20', width=430, height=400, relief=GROOVE)
frame3.place(x=1100, y=400)
# text_widget = tk.Text(frame2, width=50, height=24)
# text_widget.pack(side=tk.BOTTOM, fill=tk.X, pady=10)
nomovies = Label(frame3, text=f"CONFIRMATION:\n[Yes or No]", font=('times new roman', 15, 'bold'), bg='gray20',
                 fg='red')
nomovies.place(x=10, y=60)
no_movie = Entry(frame3, font=('arial', 15), bd=7, width=14)
no_movie.place(x=200, y=60)
#button5 = tk.Button(frame3, text="ADD MOVIES", font=('arial', 12, 'bold'), bd=7, width=10 )
#button5.place(x=150, y=150)
button6 = tk.Button(frame3, text="SCHEDULING", font=('arial', 12, 'bold'), bd=7, width=20,command=add)
button6.place(x=150, y=250)

frame4 = Frame(root, width=1250, height=50, bd=8, bg='gray20', relief=GROOVE).place(x=300, y=730)

# Configure the Text widget to use the Scrollbar
text_widget.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text_widget.yview)


import pandas as pd
from scipy.optimize import linprog

# Load the data from Excel
file_path = r"D:/adsa/cartoon_shows.xlsx" # Update this with the correct path to your Excel file
data = pd.read_excel(file_path)

# Convert the data to a list of tuples
shows = list(data.itertuples(index=False, name=None))

# Knapsack function to select optimal shows
def knapsack(shows, max_duration):
    n = len(shows)
    dp = [[0 for _ in range(max_duration + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for d in range(1, max_duration + 1):
            if shows[i - 1][1] <= d:
                dp[i][d] = max(shows[i - 1][2] + dp[i - 1][d - shows[i - 1][1]], dp[i - 1][d])
            else:
                dp[i][d] = dp[i - 1][d]

    # Trace back to find the selected shows
    schedule = []
    i, d = n, max_duration
    while i > 0 and d > 0:
        if dp[i][d] != dp[i - 1][d]:
            schedule.append(shows[i - 1])
            d -= shows[i - 1][1]
        i -= 1

    return dp[n][max_duration], schedule

# Step 1: Find optimal shows for the entire day (7 am to 10 pm, total 15 hours)
max_duration_day = 15 * 60  # 15 hours in minutes
total_popularity, optimal_shows_day = knapsack(shows, max_duration_day)

# Step 2: Find optimal shows for prime time (6 pm to 8 pm, total 2 hours)
max_duration_prime = 2 * 60  # 2 hours in minutes
total_popularity_prime, optimal_shows_prime = knapsack(optimal_shows_day, max_duration_prime)

# Step 3: Create the list of tuples with the optimal solution
total_population = 1000000  # Example total watching population
result_list = [(name, duration, popularity) for name, duration, popularity in optimal_shows_day]

# Step 4: Calculate TRP and advertisement revenue
for i, (name, duration, popularity) in enumerate(result_list):
    trp = (  popularity/ total_population)*10
    revenue = trp * 5  # revenue
    result_list[i] = (name, duration, popularity, trp, revenue)

# Print the final list of tuples
for show in result_list:
    print(show)

# Print prime time schedule
print("\nPrime Time Schedule (6 pm to 8 pm):")
for show in optimal_shows_prime:
    print(show)



def merge_sort_tuples(arr):
    if len(arr) <= 1:
        return arr

    # Finding the middle of the array
    mid = len(arr) // 2

    # Dividing the array elements into 2 halves
    left_half = merge_sort_tuples(arr[:mid])
    right_half = merge_sort_tuples(arr[mid:])

    # Merging the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    sorted_arr = []
    i = j = 0

    # Merging the arrays while comparing the 3rd element of each tuple
    while i < len(left) and j < len(right):
        if left[i][2] <= right[j][2]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # Checking if any element was left
    while i < len(left):
        sorted_arr.append(left[i])
        i += 1

    while j < len(right):
        sorted_arr.append(right[j])
        j += 1

    return sorted_arr


sorted_tuples = merge_sort_tuples(result_list)
opt_show = merge_sort_tuples(optimal_shows_prime)



print("--------------------------------")

for i in sorted_tuples:
    print(i)

#def scheduling():



def get_user_movies():
    user_movies = []
    add_movie = input("Do you want to add any movies to the schedule at a particular time? (yes/no): ").strip().lower()

    while add_movie == 'yes':
        movie_name = input("Enter the movie name: ").strip()
        duration = int(input(f"Enter the duration of {movie_name} in minutes: ").strip())
        start_time_str = input(f"Enter the start time for {movie_name} (HH:MM, 24-hour format): ").strip()
        start_time = datetime.strptime(start_time_str, "%H:%M")

        user_movies.append((movie_name, duration, start_time))

        add_movie = input("Do you want to add another movie? (yes/no): ").strip().lower()

    return user_movies


def schedule_shows(shows, user):
    # Define the start time and end time
    start_time = datetime.strptime("06:00", "%H:%M")
    end_time = datetime.strptime("22:00", "%H:%M")

    current_time = start_time
    schedule = []
    user_movies = user

    user_movies = sorted(user_movies, key=lambda x: x[2])

    for movie_name, duration, movie_start_time in user_movies:
        # Schedule regular shows until the next movie start time
        while current_time < movie_start_time:
            if current_time + timedelta(minutes=shows[0][1]) > movie_start_time:
                break

            show_name, duration_minutes = shows.pop(0)
            show_duration = timedelta(minutes=duration_minutes)
            break_duration = timedelta(minutes=5)

            show_end_time = current_time + show_duration

            schedule.append(f"{show_name} - {current_time.strftime('%H:%M')} to {show_end_time.strftime('%H:%M')}")
            current_time = show_end_time + break_duration

            if current_time + break_duration > movie_start_time:
                break

            if current_time < movie_start_time:
                schedule.append(f"Break - {show_end_time.strftime('%H:%M')} to {current_time.strftime('%H:%M')}")

        # Schedule the movie
        movie_end_time = movie_start_time + timedelta(minutes=duration)
        schedule.append(f"{movie_name} - {movie_start_time.strftime('%H:%M')} to {movie_end_time.strftime('%H:%M')}")
        current_time = movie_end_time + timedelta(minutes=5)

        if current_time >= end_time:
            break

    # Schedule remaining shows after the last movie
    while shows and current_time < end_time:
        show_name, duration_minutes = shows.pop(0)
        show_duration = timedelta(minutes=duration_minutes)
        break_duration = timedelta(minutes=5)

        show_end_time = current_time + show_duration

        if show_end_time > end_time:
            break

        schedule.append(f"{show_name} - {current_time.strftime('%H:%M')} to {show_end_time.strftime('%H:%M')}")
        current_time = show_end_time + break_duration

        if current_time < end_time:
            schedule.append(f"Break - {show_end_time.strftime('%H:%M')} to {current_time.strftime('%H:%M')}")

    return schedule


# Example usage
final = [(t[0],t[1]) for t in result_list]












root.mainloop()
