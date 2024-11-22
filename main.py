import tkinter as tk
import flag
import random
from tkinter import simpledialog
import turtle

buttons = [] #버튼 변수들을 담을 리스트 선언

def draw_flag(name):
    disable_buttons()
    turtle.reset() # 화면 초기화
    for info in flag.flag_info: # flag.py에 있는 국기 정보를 가져옴
        if info["name"] == name: # 선택한 국기와 이름이 동일한 국기를 찾아서 그림
            info["draw"]()
            break
    enable_buttons()        

def quiz():
    disable_buttons()
    name = random.choice(flag.flag_info)["name"] # 랜덤으로 국기 선택
    draw_flag(name) # 해당 국기를 그림
    user_answer = simpledialog.askstring("퀴즈", "이 국기의 국가 이름은 무엇인가요?") # 사용자에게 국가 이름을 입력받음
    if user_answer == name:
        tk.messagebox.showinfo("결과", "정답!") # 정답인 경우
    else:
        tk.messagebox.showinfo("결과", "오답! 정답은 " + name + "입니다.") # 오답인 경우
    enable_buttons()

def disable_buttons():
    for button in buttons: # 모든 버튼에 반복
        button.config(state = tk.DISABLED) # 버튼 상태 비활성화

def enable_buttons():
    for button in buttons: #모든 버튼에 반복
        button.config(state = tk.NORMAL) # 버튼 상태 활성화

# GUI 초기화
root = tk.Tk()
root.title("국기 그리기 프로그램️")

# 프레임 설정
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=tk.YES)

# 국가 버튼 추가
for info in flag.flag_info:
    button = tk.Button(frame, 
                       text=info["name"], 
                       command=lambda name=info["name"]: draw_flag(name), # 해당 국기를 그리는 함수 호출
                       height=2)
    button.pack(fill=tk.X)
    buttons.append(button)

# 모든 국기를 그리는 버튼
button = tk.Button(frame, 
                   text="모두 그리기", 
                   command=lambda: [draw_flag(info["name"]) for info in flag.flag_info], # 국기를 그리는 함수를 모두 호출
                   height=2)
button.pack(fill=tk.X)
buttons.append(button)

# 퀴즈 버튼
button = tk.Button(frame, 
                        text="퀴즈",
                        command=quiz,
                        height=2)
button.pack(fill=tk.X)
buttons.append(button)

root.geometry("300x600") # 창 크기 설정
root.mainloop()
