from datetime import datetime
from PIL import Image, ImageTk
import tkinter as tk

date_format = "%Y-%m-%d %H:%M:%S"
d_day = datetime.strptime("2023-05-26 00:00:00", date_format)

def update():
    today = datetime.now()
    delta = d_day - today
    d_day_label.config(text=f"D-Day: {delta.days}일 {delta.seconds // 3600}시간 {delta.seconds % 3600 // 60}분 {delta.seconds % 60}초")
    time_label.config(text=today.strftime("%Y-%m-%d %H:%M:%S"))
    d_day_label.after(1000, update)

root = tk.Tk()
root.geometry("400x600")

# 배경 이미지를 설정합니다.
photo = tk.PhotoImage(file="D:\\pythonClass\\bonobono2.png")
label = tk.Label(root, image=photo)
label.place(x=0, y=0, relwidth=1, relheight=1)

# 이미지 파일을 엽니다.
image = Image.open("D:\\pythonClass\\bonobono2.png")

# 이미지 크기를 2배로 확대합니다.
image = image.resize((image.width * 2, image.height * 2))

# PhotoImage 객체를 만듭니다.
photo = ImageTk.PhotoImage(image)

# 레이블에 이미지를 설정합니다.
label = tk.Label(root, image=photo)
label.pack()

# 텍스트를 입력할 수 있는 엔트리 위젯을 생성합니다.
text_entry = tk.Entry(root)
text_entry.pack()

# 텍스트를 입력하고 버튼을 누르면 레이블에 텍스트를 추가합니다.
def add_text():
    text = text_entry.get()
    text_label.config(text=text)

text_button = tk.Button(root, text="일정검색", command=add_text)
text_button.pack()

# 텍스트를 표시할 레이블을 생성합니다.
text_label = tk.Label(root, font=("Times", 20))
text_label.pack()

time_label = tk.Label(root, font=("Times", 20))
time_label.pack()

d_day_label = tk.Label(root, font=("Times", 20))
d_day_label.pack()

update()
root.mainloop()