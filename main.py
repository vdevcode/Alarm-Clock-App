import tkinter as tk
from playsound import playsound
import datetime
from tkinter import filedialog

def set_alarm():
    alarm_time = entry.get()
    
    # Kiểm tra định dạng thời gian
    try:
        datetime.datetime.strptime(alarm_time, "%H:%M")
    except ValueError:
        notification_label.config(text="Định dạng thời gian không hợp lệ")
        return
    
    # Tạo cửa sổ thông báo
    notification = tk.Toplevel(root)
    notification.title("Thông báo")
    notification.geometry("300x150")
    notification.resizable(False, False)
    
    # Hiển thị thông báo
    notification_label = tk.Label(notification, text="Đã đặt báo thức\nThời gian: " + alarm_time)
    notification_label.pack()
    
    # Tạo nút Dừng báo thức
    stop_button = tk.Button(notification, text="Dừng", command=notification.destroy)
    stop_button.pack()
    
    def check_alarm():
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            playsound('/Users/home/Desktop/notify/music.mp3')  # Đường dẫn tới tệp âm thanh thông báo
            stop_button.destroy()
            reset_button = tk.Button(notification, text="Bạn có muốn đặt lại báo thức", command=root_restart)
            reset_button.pack()
        else:
            notification.after(1000, check_alarm)
    
    check_alarm()

def root_restart():
    entry.delete(0, tk.END)
    root.deiconify()

def change_background():
    filename = filedialog.askopenfilename(title="Chọn ảnh nền", filetypes=(("Image files", "*.jpg *.jpeg *.png"), ("All files", "*.*")))
    if filename:
        root.configure(background="")
        root.background_image = tk.PhotoImage(file=filename)
        background_label.config(image=root.background_image)

root = tk.Tk()
root.title("Đồng hồ báo thức")
root.geometry("400x200")
root.resizable(False, False)

# Chọn màu nền và ảnh nền mặc định
root.configure(background="#f0f0f0")
root.background_image = tk.PhotoImage(file="/Users/home/Desktop/notify/clock.png")

# Hiển thị ảnh nền
background_label = tk.Label(root, image=root.background_image)
background_label.place(relx=0, rely=0, relwidth=1, relheight=1)

label = tk.Label(root, text="Nhập thời gian báo thức (HH:MM): ", bg="black")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Đặt báo thức", command=set_alarm)
button.pack()

change_bg_button = tk.Button(root, text="Thay đổi nền", command=change_background)
change_bg_button.pack()

root.mainloop()
