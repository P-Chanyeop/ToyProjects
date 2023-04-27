# floation_point(부동 소수점 오차 예시)
import decimal

if(decimal.Decimal('0.1') * 3 == decimal.Decimal('0.3')):
    print("True")
else:
    print("False")
    
if(decimal.Decimal('1.2') - decimal.Decimal('0.1') == decimal.Decimal('1.1')):
    print("True")
else:
    print("False")

if(decimal.Decimal('0.1') * decimal.Decimal('0.1') == decimal.Decimal('0.01')):
    print("True")
else:
    print("False")    



