import tkinter as tk
import tkinter.filedialog
import pymysql
from os import path

filename = ''
rowList = []
posX = 50
posY = 100

# DB 연결ㄱ
con = pymysql.connect(host='localhost', user='root', password='7579',
                       db='notepad', charset='utf8') # 한글처리 (charset = 'utf8')

# Connection 으로부터 Cursor 생성
cur = con.cursor()

# # 파일 저장 함수
# def save_file():
#     # 파일 대화 상자 열기
#     filename = tk.filedialog.asksaveasfilename(initialdir= path.dirname(__file__), defaultextension=".txt")
#     # 파일이 선택되면 file을 저장하고 filename과 content를 Database에 저장한다.
#     # 사용자가 파일을 선택하지 않고 취소를 누르면 insertDB함수를 실행하지 않는다.
#     if filename:
#         # 텍스트 입력 창의 내용을 파일에 씁니다.
#         with open(filename, "w") as f:
#             f.write(text_widget.get("1.0", "end-1c"))
#         filename = filename[filename.rfind("/")+1:len(filename)-4]
#         insertDB(filename)
#     return filename
    
      
# # DB 저장함수 
# def insertDB(filename):
#     subject = filename
#     content = text_widget.get(1.0, "end")
#     sql = f'INSERT INTO notepad(subject, content) VALUES ("{subject}", "{content}")'
#     cur.execute(sql)
    
# DB 조회함수
def selectDB():
    sql = "SELECT subject FROM notepad"
    cur.execute(sql)
    rows = cur.fetchall()
    
    
    return rows

# 새 글 작성 함수
def createBtnClick():
    print("새 글 작성 버튼 클릭됨!!")
    

# 글 버튼 클릭시 상세 페이지 보여주기 함수
def question_detail(button):
    print(f'{button.text}번째 게시글 클릭됨.')
    

# 메모장 창 만들기
root = tk.Tk()

# 창 제목, 사이즈 설정
root.geometry("1280x960")
root.title("게시판")

# 게시글 리스트 출력 창 만들기
board_name = tk.Label(root, text="컴퓨터공학과 SNS 컴브리타임")
board_name.pack(padx=10,pady=10)    
idx = 0

# 데이터 리스트 출력 
for i in selectDB():
    question_list = tk.Button(root, text=i)
    question_list.place(x = posX, y = posY + idx * 50)
    question_list.configure(command=question_detail(question_list))
    print(i)
    idx += 1
    if idx != 0 and idx % 11 == 0:
        posY = 100
        idx = 0
        posX += 200

# 게시글 생성 버튼 만들기
create_question = tk.Button(root, text="새 글 작성")
create_question.configure(command=createBtnClick)
create_question.pack(side="bottom", padx=0, pady=10)

# 게시글 생성 버튼에 이벤트 리스너 달기

# 텍스트 입력 창 만들기
# text_widget = tk.Text()

# 텍스트 입력 창을 중앙에 배치
# text_widget.pack(padx=10, pady=10)

# 저장 버튼 만들기
# save_button = tk.Button(root, text="저장", command=lambda: save_file())

# 저장 버튼을 중앙에 배치
# save_button.pack(side="bottom", padx=10, pady=10)

# # 조회 버튼 만들기
# select_button = tk.Button(root, text="DB조회", command=lambda: selectDB())

# # 저장 버튼을 중앙에 배치
# select_button.pack(side="bottom", padx=10, pady=10)

# 메모장 창 표시
root.mainloop()

# DB 연결 종료
con.close()