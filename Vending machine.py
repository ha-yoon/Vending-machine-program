import os    
import time

st = "밀키트 구매를 원하시면 터치해주세요😊"
for i in st:
    print(i, end="")
    time.sleep(0.05)
input()
os.system("cls")

money = 0
cnt = 0

print("안녕하세요🙌~ 해당 자판기는 금액 충전후 사용이 가능합니다.")

while True:    
    print("="*80)
    print("1. 닭볶음탕 / 8500")
    print("2. 제육볶음 / 9500")
    print("3. 쭈꾸미볶음 / 9500")
    print("4. 소불고기 / 9500")
    print("5. 김치찌개 / 8500")
    print("6. 금액 충전(추가 충전을 원하시는 경우 눌러주세요.)")
    print("7. 잔돈반환")
    print("8. 프로그램 종료")
    print("="*80)
    print("현재금액", money)

    user = int(input(" 입력 : "))

    if 1<=user <=8:
        if user == 1:
            if money >= 8500:
                print("닭볶음탕 맛있게 드세요😊")
                money -= 8500
            else:
                print("구매 불가합니다😢")
        elif user == 2:
            if money >= 9500:
                print("제육볶음 맛있게 드세요😊")
                money -= 9500
            else:
                print("구매 불가합니다😢")
        elif user == 3:
            if money >= 9500:
                print("쭈꾸미볶음 맛있게 드세요😊")
                money -= 9500
            else:
                print("구매 불가합니다😢")
        elif user == 4:
            if money >= 9500:
                print("소불고기 맛있게 드세요😊")
                money -= 9500
            else:
                print("구매 불가합니다😢")
        elif user == 5:
            if money >= 8500:
                print("김치찌개 맛있게 드세요😊")
                money -= 8500
            else:
                print("구매 불가합니다😢")
        elif user == 6:
            money += int(input("돈을 넣어주세요 : "))
        elif user == 7:
            print(money, "원이 반환됩니다.")
            money = 0
        elif user == 8:
            if money > 0:
                print(money, "원이 반환됩니다.")
            print("종료~")
            break
        cnt = 0
    else:
        print("입력이상!!")
        cnt += 1

    if cnt == 9:
        print()
        break
    
    time.sleep(0.5)
    os.system("cls")