import requests
from bs4 import BeautifulSoup
import time

# 로그인
session = requests.Session()
session.get('https://sports.cfmc.or.kr/member/login')

data = {
    'process_check' : 'login',
    'memid' : 'asd123',
    'mempw' : 'asd321'
}
res = session.post('https://sports.cfmc.or.kr/member/process', data=data)
print(res.status_code)


# 예약 페이지 접속
res = session.get('https://sports.cfmc.or.kr/rent/reservation/index/2023/10/23/1/CHEONAN02/19/19')
print(res.status_code)

# 예약 상세페이지로 접속
# data = {
#     'category_index' : 'reservation',
#     'receipt_date' : '20231023',
#     'year' : '2023',
#     'month' : '10',
#     'rev_day' : '23',
#     'comcd' : 'CHEONAN02',
#     'partcd' : '19',
#     'placecd' : '19',
#     'is_list' : '1',
#     'baseURL' : 'https://sports.cfmc.or.kr',
#     'baseSSL' : 'https://sports.cfmc.or.kr:443',
#     'select_day' : '23',
#     'select_group' : 'Y',
#     'receipt_time[]' : '1908',
#     'receipt_time[]' : '1909',
#     'receipt_time[]' : '1910',
# }

# res = session.post('https://sports.cfmc.or.kr/rent/inputform', data=data)
# print(res.status_code)
time.sleep(5)

data = {
    'receipt_time[]' : '1908',
    'receipt_time[]' : '1909',
    'receipt_time[]' : '1910',
    'item_cd_list[]' : 'I000626',
    'item_cd_list[]' : 'I000626',
    'item_cd_list[]' : 'I000626',
    'item_idx_not_list[]' : 'I000798',
    'item_idx_not_list[]' : 'I000808',
    'item_idx_not_list[]' : 'I000809',
    'item_idx_not_list[]' : 'I000810',
    'item_idx_not_list[]' : 'I000811',
    'item_idx_not_list[]' : 'I000812',
    'item_idx_not_list[]' : 'I000813',
    'facility_count[]' : '0',
    'time_select[]' : '3',
    'facility_amt[]' : '85,810',
    'facility_amt[]': '92,420',
    'facility_amt[]': '99,020',
    'facility_amt[]': '105,630',
    'facility_amt[]': "112,230",
    'facility_amt[]' : '118,840',
    'facility_sale_amt[]': '79210',
    'facility_sale_amt[]': '85810',
    'facility_sale_amt[]': '92420',
    'facility_sale_amt[]': '99020',
    'facility_sale_amt[]': '105630',
    'facility_sale_amt[]': '112230',
    'facility_sale_amt[]': '118840',
    'dc_group[]' : '10',
    'formcheck' : '1001',
    'URL' : 'https://sports.cfmc.or.kr',
    'SSL' : 'https://sports.cfmc.or.kr:443',
    'comcd' : 'CHEONAN02',
    'sale_amt' : '165000',
    'part_cd' : '19',
    'place_cd' : '19',
    'team_seq' : '329',
    'payment_total_amt' : '82,500',
    'receipt_date' : '20231030',
    'select_group' : 'Y',
    'tel': '02-1111-1111',
    'hp' : '010-2262-1273',
    'group_count' : '0',
    'use_time_list' : 'CHEONAN02;1908;20231023;20231023;1400;1500;|CHEONAN02;1909;20231023;20231023;1500;1600;|CHEONAN02;1910;20231023;20231023;1600;1700;'
}

res = session.post('https://sports.cfmc.or.kr/rent/process', data=data)
print(res.text)