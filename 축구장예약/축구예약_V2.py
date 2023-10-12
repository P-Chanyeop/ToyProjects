# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import tkinter as tk
from threading import Thread
import time


def login():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    
    url = 'https://sports.cfmc.or.kr/member/login'
    driver.get(url=url)
    
    # 아이디
    id_input = driver.find_element(By.ID, 'input_memid')
    id_input.send_keys('qkrcksduq1gh')
    
    # 비밀번호
    pw_input = driver.find_element(By.ID, 'input_mempw')
    pw_input.send_keys('worud3232!')
    pw_input.send_keys(Keys.ENTER)
    
    # 예약페이지 접속
    url = 'https://sports.cfmc.or.kr/rent/application/index/2023/11/01/1/CHEONAN02/19'
    driver.get(url=url)
        
def login_thread():
    t1 = Thread(target=login)
    t1.start()
    

def reserve():
    global driver
    driver.implicitly_wait(10)
    
    # 예약 신청 클릭
    reserve_apply_btn = driver.find_element(By.CSS_SELECTOR, '#contents > div.content_body > ul.reserve_cal_dl > li.reserve_cal_dd > ul > li > ul > li.rent_cal_li > ul > li.reserve_application_li > a')
    reserve_apply_btn.click()
    
    # 시간 선택
    select_index = ['1', '2']    # 리스트로 받아오기
    for i in range(len(select_index)):
        driver.find_element(By.ID, f'select_{select_index[i]}').click()
        
    # 예약 신청 클릭
    time.sleep(2.8)
    
    while True:
        try:
            reserve_btn = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/ul[3]/li[1]/input')
            if reserve_btn:
                reserve_btn.click()
                break
        except:
            continue 
    
    # 전화번호 국번 클릭
    while True:
        try:
            select_element = Select(driver.find_element(By.ID, 'tel1'))
            driver.implicitly_wait(10)
            if select_element:
                select_element.select_by_value('02')
                break
        except:
            continue
    
    driver.find_element(By.ID, 'tel2').send_keys('1111')
    
    driver.find_element(By.ID, 'tel3').send_keys('1111')
    
    driver.find_element(By.ID, 'playname').send_keys('축구')
    
    driver.find_element(By.ID, 'reason').send_keys('축구경기를 위한 목적')
    
    # 동의버튼 클릭
    agree_btn = driver.find_element(By.ID, 'agree_1')
    driver.execute_script("arguments[0].scrollIntoViewIfNeeded();", agree_btn)
    agree_btn.click()
    
    # 예약신청 클릭
    driver.find_element(By.ID, 'btn_reservation').click()
    
    
        
if __name__ == "__main__":
    
    window = tk.Tk()

    btn = tk.Button(window, text='시작', command=login_thread)
    btn.pack()
    
    btn2 = tk.Button(window, text='시작', command=reserve)
    btn2.pack()

    window.mainloop()