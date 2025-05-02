# IMPORTING 
import tkinter as tk
from tkinter import ttk, filedialog
from tkinter import messagebox as mess
import tkinter.simpledialog as tsd
import cv2, os, csv, numpy as np
from PIL import Image
import pandas as pd
import datetime, time

# FUNCTIONS

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

def tick():
    time_string = time.strftime('%H:%M:%S')
    clock.config(text=time_string)
    clock.after(200, tick)

def contact():
    mess._show(title='Contact us', message="Please contact us on : 'harsharaju721@gmail.com' ")

def check_haarcascadefile():
    if not os.path.isfile("haarcascade_frontalface_default.xml"):
        mess._show(title='Some file missing', message='Please contact us for help')
        window.destroy()

def save_pass():
    assure_path_exists("TrainingImageLabel/")
    if os.path.isfile("TrainingImageLabel/psd.txt"):
        with open("TrainingImageLabel/psd.txt", "r") as tf:
            key = tf.read()
    else:
        master.destroy()
        new_pas = tsd.askstring('Old Password not found', 'Please enter a new password below', show='*')
        if new_pas is None:
            mess._show(title='No Password Entered', message='Password not set!! Please try again')
        else:
            with open("TrainingImageLabel/psd.txt", "w") as tf:
                tf.write(new_pas)
            mess._show(title='Password Registered', message='New password was registered successfully!!')
            return
    op = old.get()
    newp = new.get()
    nnewp = nnew.get()
    if op == key:
        if newp == nnewp:
            with open("TrainingImageLabel/psd.txt", "w") as txf:
                txf.write(newp)
        else:
            mess._show(title='Error', message='Confirm new password again!!!')
            return
    else:
        mess._show(title='Wrong Password', message='Please enter correct old password.')
        return
    mess._show(title='Password Changed', message='Password changed successfully!!')
    master.destroy()

def change_pass():
    global master, old, new, nnew
    master = tk.Tk()
    master.geometry("400x160")
    master.resizable(False, False)
    master.title("Change Password")
    master.configure(background="white")
    lbl4 = tk.Label(master, text='    Enter Old Password', bg='white', font=('times', 12, 'bold'))
    lbl4.place(x=10, y=10)
    old = tk.Entry(master, width=25, fg="black", relief='solid', font=('times', 12, 'bold'), show='*')
    old.place(x=180, y=10)
    lbl5 = tk.Label(master, text='   Enter New Password', bg='white', font=('times', 12, 'bold'))
    lbl5.place(x=10, y=45)
    new = tk.Entry(master, width=25, fg="black", relief='solid', font=('times', 12, 'bold'), show='*')
    new.place(x=180, y=45)
    lbl6 = tk.Label(master, text='Confirm New Password', bg='white', font=('times', 12, 'bold'))
    lbl6.place(x=10, y=80)
    nnew = tk.Entry(master, width=25, fg="black", relief='solid', font=('times', 12, 'bold'), show='*')
    nnew.place(x=180, y=80)
    cancel = tk.Button(master, text="Cancel", command=master.destroy, fg="black", bg="red", height=1, width=25, activebackground="white", font=('times', 10, 'bold'))
    cancel.place(x=200, y=120)
    save1 = tk.Button(master, text="Save", command=save_pass, fg="black", bg="#3ece48", height=1, width=25, activebackground="white", font=('times', 10, 'bold'))
    save1.place(x=10, y=120)
    master.mainloop()

def psw():
    assure_path_exists("TrainingImageLabel/")
    if os.path.isfile("TrainingImageLabel/psd.txt"):
        with open("TrainingImageLabel/psd.txt", "r") as tf:
            key = tf.read()
    else:
        new_pas = tsd.askstring('Old Password not found', 'Please enter a new password below', show='*')
        if new_pas is None:
            mess._show(title='No Password Entered', message='Password not set!! Please try again')
        else:
            with open("TrainingImageLabel/psd.txt", "w") as tf:
                tf.write(new_pas)
            mess._show(title='Password Registered', message='New password was registered successfully!!')
            return
    password = tsd.askstring('Password', 'Enter Password', show='*')
    if password == key:
        TrainImages()
    elif password is None:
        pass
    else:
        mess._show(title='Wrong Password', message='You have entered wrong password')

def clear():
    txt.delete(0, 'end')
    message1.configure(text="1)Take Images  >>>  2)Save Profile")

def clear2():
    txt2.delete(0, 'end')
    message1.configure(text="1)Take Images  >>>  2)Save Profile")

def clear3():
    txt3.delete(0, 'end')
    message1.configure(text="1)capture Images  then  2)Store Profile")


import json
import os
from tkinter import messagebox as mess
import json
import os
from tkinter import messagebox as mess

def check_duplicate_student(student_id, name, email):
    json_file = 'student_data.json'

    # Load JSON if exists, else create empty dictionary
    if os.path.exists(json_file):
        with open(json_file, 'r') as file:
            data = json.load(file)
    else:
        data = {}

    # Check if ID exists
    if student_id in data:
        existing = data[student_id]
        mess._show(title='Duplicate ID',
                message=f"Student ID already exists!\nName: {existing['name']}\nEmail: {existing['email']}")
        return True  # Duplicate found
    else:
        # If no duplicate, add the student details to the data dictionary
        data[student_id] = {'name': name, 'email': email}
        
        # Save the updated data to the JSON file
        with open(json_file, 'w') as file:
            json.dump(data, file, indent=4)

        # Student added successfully message
        mess._show(title="Success", message=f"Student {name} added successfully! to JSON")
        return False  # No duplicate, student added

import os
import csv
import json
from tkinter import messagebox as mess


def TakeImages():
    check_haarcascadefile()
    columns = ['SERIAL NO.', '', 'ID', '', 'NAME',"","EMAIL"]
    assure_path_exists("StudentDetails/")
    assure_path_exists("TrainingImage/")
    serial = 0
    if os.path.isfile("StudentDetails/StudentDetails.csv"):
        with open("StudentDetails/StudentDetails.csv", 'r') as csvFile1:
            reader1 = csv.reader(csvFile1)
            for l in reader1:
                serial += 1
        serial = (serial // 2)
    else:
        with open("StudentDetails/StudentDetails.csv", 'a+') as csvFile1:
            writer = csv.writer(csvFile1)
            writer.writerow(columns)
            serial = 1
    Id = txt.get().strip()
    name = txt2.get().strip()
    email= txt3.get().strip()
    if check_duplicate_student(Id,name,email):
        return  
    if name.replace(" ", "").isalpha():
        # Start time measurement for registration
        start_time = time.time()
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while True:
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                sampleNum += 1
                cv2.imwrite("TrainingImage/" + name + "." + str(serial) + "." + Id + '.' + str(sampleNum) + ".jpg",
                            gray[y:y + h, x:x + w])
                cv2.imshow('Taking Images', img)
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            elif sampleNum > 100:
                break
        cam.release()
        cv2.destroyAllWindows()
        # End time measurement and show popup with elapsed time
        end_time = time.time()
        elapsed_time = end_time - start_time
        mess._show(title="Images taken Time", message=f"Time taken for registration: {elapsed_time:.2f} seconds")
        res = "Images Taken for ID : " + Id
        row = [serial, '', Id, '', name,"",email]
        with open('StudentDetails/StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        message1.configure(text=res)
    else:
        mess._show(title="Error", message="Enter Correct name")

def TrainImages():
    check_haarcascadefile()
    assure_path_exists("TrainingImageLabel/")
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, ID = getImagesAndLabels("TrainingImage")
    try:
        recognizer.train(faces, np.array(ID))
    except:
        mess._show(title='No Registrations', message='Please Register someone first!!!')
        return
    recognizer.save("TrainingImageLabel/Trainner.yml")
    res = "Profile Saved Successfully"
    message1.configure(text=res)
    message.configure(text='Total Registrations till now  : ' + str(ID[0]))

def getImagesAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    Ids = []
    for imagePath in imagePaths:
        pilImage = Image.open(imagePath).convert('L')
        imageNp = np.array(pilImage, 'uint8')
        ID = int(os.path.split(imagePath)[-1].split(".")[1])
        faces.append(imageNp)
        Ids.append(ID)
    return faces, Ids
def TrackImages():
    check_haarcascadefile()
    assure_path_exists("Attendance/")
    assure_path_exists("StudentDetails/")
    
    for k in tv.get_children():
        tv.delete(k)

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    
    if os.path.isfile("TrainingImageLabel/Trainner.yml"):
        recognizer.read("TrainingImageLabel/Trainner.yml")
    else:
        mess._show(title='Data Missing', message='Please click on Save Profile to reset data!!')
        return

    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath)
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', '', 'Name', '', 'Date', '', 'Time']
    
    if os.path.isfile("StudentDetails/StudentDetails.csv"):
        df = pd.read_csv("StudentDetails/StudentDetails.csv")
    else:
        mess._show(title='Details Missing', message='Students details are missing, please check!')
        cam.release()
        cv2.destroyAllWindows()
        window.destroy()

    attendance = []

    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
            serial, conf = recognizer.predict(gray[y:y + h, x:x + w])

            if conf < 50:
                accuracy = 80 + ((50 - conf) / 50) * 19
                ts_now = time.time()
                date = datetime.datetime.fromtimestamp(ts_now).strftime('%d-%m-%Y')
                timeStamp = datetime.datetime.fromtimestamp(ts_now).strftime('%H:%M:%S')
                aa = df.loc[df['SERIAL NO.'] == serial]['NAME'].values
                ID = df.loc[df['SERIAL NO.'] == serial]['ID'].values
                ID = str(ID)[1:-1]
                name_recog = str(aa)[2:-2]
                name_display = f"{name_recog} ({accuracy:.2f}%)"
                attendance = [str(ID), '', name_recog, '', str(date), '', str(timeStamp)]
            else:
                name_display = 'Unknown'

            cv2.putText(im, name_display, (x, y + h), font, 1, (255, 255, 255), 2)

        cv2.imshow('Taking Attendance', im)

        # Fix: properly handle key press and window closing
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            print("Exit key pressed")
            break

        # Optional fix: auto-break if window is closed manually
        if cv2.getWindowProperty('Taking Attendance', cv2.WND_PROP_VISIBLE) < 1:
            print("Window closed manually")
            break

    ts_now = time.time()
    date = datetime.datetime.fromtimestamp(ts_now).strftime('%d-%m-%Y')

    if attendance:
        if os.path.isfile("Attendance/Attendance_" + date + ".csv"):
            with open("Attendance/Attendance_" + date + ".csv", 'a+', newline='') as csvFile1:
                writer = csv.writer(csvFile1)
                writer.writerow(attendance)
        else:
            with open("Attendance/Attendance_" + date + ".csv", 'a+', newline='') as csvFile1:
                writer = csv.writer(csvFile1)
                writer.writerow(col_names)
                writer.writerow(attendance)

    with open("Attendance/Attendance_" + date + ".csv", 'r') as csvFile1:
        reader1 = csv.reader(csvFile1)
        i = 0
        for lines in reader1:
            i += 1
            if i > 1 and i % 2 != 0:
                iidd = str(lines[0]) + '   '
                tv.insert('', 0, text=iidd, values=(str(lines[2]), str(lines[4]), str(lines[6])))

    cam.release()
    cv2.destroyAllWindows()

def show_lbph_params():
    # Let the user select an image
    filename = filedialog.askopenfilename(title="Select an image", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if filename:
        img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
        if img is None:
            mess._show(title="Error", message="Could not load image.")
            return
        height, width = img.shape
        total_pixels = width * height
        # Default LBPH parameters (these can be adjusted as needed)
        radius = 1
        neighbors = 8
        grid_x = 8
        grid_y = 8
        total_grid_cells = grid_x * grid_y
        histogram_length = total_grid_cells * 256  # each grid cell has 256 bins
        params_msg = (
            f"LBPH Parameters for selected image:\n\n"
            f"Image Dimensions: {width} x {height}\n"
            f"Total Pixels: {total_pixels}\n\n"
            f"Grid Cell Dimensions (default): {grid_x} x {grid_y}\n"
            f"Total Grid Cells: {total_grid_cells}\n\n"
            f"Histogram Length per cell: 256 bins\n"
            f"Total Histogram Vector Length: {histogram_length}"
        )
        mess._show(title="LBPH Parameters", message=params_msg)

# USED STUFFS
global key
key = ''

ts_now = time.time()
date = datetime.datetime.fromtimestamp(ts_now).strftime('%d-%m-%Y')
day, month, year = date.split("-")
mont = {
    '01':'January',
    '02':'February',
    '03':'March',
    '04':'April',
    '05':'May',
    '06':'June',
    '07':'July',
    '08':'August',
    '09':'September',
    '10':'October',
    '11':'November',
    '12':'December'
}

# GUI FRONT-END
window = tk.Tk()
window.state("zoomed")
window.resizable(True, False)
window.title("Attendance System")
window.configure(background='black')

frame1 = tk.Frame(window, bg="blue")

frame2 = tk.Frame(window, bg="green")
frame1.place(relx=0.5, rely=0.19, relwidth=0.46, relheight=0.71)
frame2.place(relx=0.04, rely=0.19, relwidth=0.45, relheight=0.71)

message3 = tk.Label(window, text=" Cyber Intelligent Face Recognition Attendance System", fg="white", bg="black", width=48, height=1, font=('times', 29, 'bold'))
message3.place(relx=0, rely=0)

frame3 = tk.Frame(window, bg="white")
frame3.place(relx=0.57, rely=0.09, relwidth=0.1, relheight=0.07)

frame4 = tk.Frame(window, bg="white")
frame4.place(relx=0.2, rely=0.09, relwidth=0.39, relheight=0.07)

datef = tk.Label(frame4, text="DATE:  "+day+"-"+mont[month]+"-"+year+"  &  TIME:", fg="orange", bg="black", width=30, height=1, font=('times', 20, 'bold'))
datef.pack(fill='both', expand=1)

clock = tk.Label(frame3, fg="orange", bg="black", width=55, height=1, font=('times', 19, 'bold'))
clock.pack(fill='both', expand=1)
tick()

head2 = tk.Label(frame2, text="               New Registration frame                 ", fg="black", bg="white", font=('times', 20, 'bold'))
head2.grid(row=0, column=0)

head1 = tk.Label(frame1, text="                        Attendance frame                             ", fg="black", bg="white", font=('times', 17, 'bold'))
head1.place(x=0, y=0)

lbl = tk.Label(frame2, text="Enter ID   ", width=7, height=1, fg="pink", bg="green", font=('times', 17, 'bold'))
lbl.place(x=20, y=50)

txt = tk.Entry(frame2, width=26, fg="black", font=('times', 13, 'bold'))
txt.place(x=130, y=55)

lbl2 = tk.Label(frame2, text="Enter Name", width=9,height=1, fg="pink", bg="green", font=('times', 17, 'bold'))
lbl2.place(x=1, y=100)

txt2 = tk.Entry(frame2, width=26, fg="black", font=('times', 13, 'bold'))
txt2.place(x=130, y=102)

# Email Label and Entry
lbl3 = tk.Label(frame2, text="Enter Email", width=9, height=1, fg="pink", bg="green", font=('times', 17, 'bold'))
lbl3.place(x=1, y=150)

txt3 = tk.Entry(frame2, width=26, fg="black", font=('times', 13, 'bold'))
txt3.place(x=130, y=152)


import smtplib
import re
from tkinter import messagebox

    # Securely Get Credentials
sender_email = "harsharaju721@gmail.com"
sender_password = "ahhh vamt nmxt szka"

# Function to Validate Email & Send Mail
def validate_and_send_email():
    email = txt3.get()
    pattern = r'^[a-zA-Z0-9._%+-]+@(gmail\.com|email\.com)$'  # Only gmail.com & email.com
    
    if re.match(pattern, email):
        try:
            send_email(email)  # Call send email function
            messagebox.showinfo("Success", "Valid Email ✅\nVerification Mail Sent!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send email: {e}")
    else:
        messagebox.showerror("Error", "Invalid Email! Only @gmail.com & @email.com allowed ❌")

# Function to Send Email
def send_email(email):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        email_message = (
        "Subject: Email Verification - Cyber Intelligent Face Recognition Attendance System\n\n"
        "Dear Student,\n\n"
        "Greetings from the Cyber Intelligent Face Recognition Attendance System team!\n\n"
        "We are pleased to inform you that your email address has been successfully verified.\n"
        "This verification ensures that you will now receive important updates regarding your attendance.\n\n"
        "About Our System:\n"
        "- Uses facial recognition to mark your presence automatically.\n"
        "- Ensures secure and contactless attendance recording.\n"
        "- Helps maintain transparency and accuracy.\n\n"
        "If you have any queries or face any issues, please contact your administrator.\n\n"
        "Thank you for joining us in making attendance smart and effortless.\n\n"
        "Warm regards,\n"
        "Team - Cyber Intelligent Face Recognition Attendance System\n\n"
        "Note: This is a system-generated email. Please do not reply."
    )

        server.sendmail(sender_email, email, email_message)
        server.quit()
        return True
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send OTP: {e}")
        return False


# ✅ Place the Verify Button just below the txt3 entry
verifyButton = tk.Button(
    frame2, 
    text="Verify email", 
    command=validate_and_send_email,  # Make sure this function is defined above
    fg="white", 
    bg="blue", 
    width=11, 
    height=1, 
    activebackground="white", 
    font=('times', 15, 'bold')
)
verifyButton.place(x=175, y=187)



message1 = tk.Label(frame2, text="Warning:First capture images then store Profile", bg="black", fg="white", width=39, height=1, activebackground="yellow", font=('times', 15, 'bold'))
message1.place(x=7, y=230)

message = tk.Label(frame2, text="", bg="#00aeff", fg="black", width=39, height=1, activebackground="yellow", font=('times', 16, 'bold'))
message.place(x=7, y=450)


res = 0
if os.path.isfile("StudentDetails/StudentDetails.csv"):
    with open("StudentDetails/StudentDetails.csv", 'r') as csvFile1:
        reader1 = csv.reader(csvFile1)
        for l in reader1:
            res += 1
    res = (res // 2) - 1
else:
    res = 0
message.configure(text='Total Registrations till now  : ' + str(res))

# MENUBAR 
menubar = tk.Menu(window, relief='ridge')
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label='Change Password', command=change_pass)
filemenu.add_command(label='Contact Us', command=contact)
filemenu.add_command(label='Exit', command=window.destroy)
menubar.add_cascade(label='Help', font=('times', 29, 'bold'), menu=filemenu)

# TREEVIEW ATTENDANCE TABLE 
tv = ttk.Treeview(frame1, height=13, columns=('name', 'date', 'time'))
tv.column('#0', width=82)
tv.column('name', width=130)
tv.column('date', width=133)
tv.column('time', width=133)
tv.grid(row=2, column=0, padx=(0,0), pady=(150,0), columnspan=4)
tv.heading('#0', text='ID')
tv.heading('name', text='NAME')
tv.heading('date', text='DATE')
tv.heading('time', text='TIME')

# SCROLLBAR 
scroll = ttk.Scrollbar(frame1, orient='vertical', command=tv.yview)
scroll.grid(row=2, column=4, padx=(0,100), pady=(150,0), sticky='ns')
tv.configure(yscrollcommand=scroll.set)



lbl3 = tk.Label(frame1, text="Clear Attendance", width=20, fg="black", bg="red", height=1, font=('times', 17, 'bold')) 
lbl3.place(x=100, y=100)
lbl3.bind("<Button-1>", lambda e: clear_treeview())

def clear_treeview():
    for item in tv.get_children():
        tv.delete(item)

# BUTTONS 
clearButton = tk.Button(frame2, text="Clear", command=clear, fg="black", bg="#ea2a2a", width=11, activebackground="white", font=('times', 11, 'bold'))
clearButton.place(x=370, y=53)
clearButton2 = tk.Button(frame2, text="Clear", command=clear2, fg="black", bg="#ea2a2a", width=11, activebackground="white", font=('times', 11, 'bold'))
clearButton2.place(x=370, y=100)

clearButton3 = tk.Button(frame2, text="Clear", command=clear3, fg="black", bg="#ea2a2a", width=11, activebackground="white", font=('times', 11, 'bold'))
clearButton3.place(x=370, y=150)
takeImg = tk.Button(frame2, text="Capture Images", command=TakeImages, fg="white", bg="blue", width=34, height=1, activebackground="white", font=('times', 15, 'bold'))
takeImg.place(x=30, y=270)
trainImg = tk.Button(frame2, text="Store Profile", command=psw, fg="white", bg="blue", width=34, height=1, activebackground="white", font=('times', 15, 'bold'))
trainImg.place(x=30, y=315)
trackImg = tk.Button(frame1, text="Take Attendance", command=TrackImages, fg="white", bg="green", width=23, height=1, activebackground="white", font=('times', 15, 'bold'))
trackImg.place(x=100, y=45)
quitWindow = tk.Button(frame1, text="Quit", command=window.destroy, fg="black", bg="red", width=35, height=1, activebackground="white", font=('times', 15, 'bold'))
quitWindow.place(x=30, y=450)
# New Button: Show LBPH Parameters (placed at the bottom of the green panel)
lbphButton = tk.Button(frame2, text="Show LBPH Parameters", command=show_lbph_params, fg="white", bg="green", width=34, height=1, activebackground="white", font=('times', 15, 'bold'))
lbphButton.place(x=30, y=520)



exit_btn = tk.Button(
    window, 
    text="Exit System", 
    command=window.destroy,  # closes the main window
    fg="white", 
    bg="red", 
    font=('times', 15, 'bold'), 
    width=12, 
    height=1
)
exit_btn.place(relx=0.43, rely=0.91)  # adjust position as needed

# END 
window.configure(menu=menubar)
window.mainloop()










