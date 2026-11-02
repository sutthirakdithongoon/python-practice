# สร้าง Function ชื่อ show_product
# Function ต้องรับ Parameters 3 ตัว ได้แก่ name, price, quantity
# ภายใน Function ให้แสดงชื่อสินค้า ราคา และจำนวนสินค้า
# เรียกใช้ Function จำนวน 3 ครั้ง โดยส่งข้อมูลสินค้าที่ต่างกัน
# ห้ามใช้ input() ในโจทย์นี้ ให้ส่งค่าตรงเข้า Function
# ยังไม่ต้องใช้ return, List หรือ Dictionary



# from os import name


# def show_product(name,price,quantity):
#       print("Name of product : ", name)
#       print("Price : ", price)
#       print("Quantity : ", quantity)
#       print("-----------------------")
# show_product("yuki", 100 , 10)
# show_product("ploy", 50 , 5)
# show_product("kit", 25 , 1)



# สร้าง Function ชื่อ check_grade
# รับ Parameters 2 ตัว คือ name และ score
# ใช้ Conditions ภายใน Function เพื่อกำหนดเกรd
# แสดงชื่อนักเรียน คะแนน และเกรด
# เรียก Function อย่างน้อย 4 ครั้งด้วยข้อมูลที่แตกต่างกัน
# ยังไม่ต้องใช้ return, List หรือ Dictionary



def check_grade(name, score ):
    print("Name : ",name)
    print("Score : ",score)

    if score >= 80:
        grade = "A"
    elif score >=70:
        grade = "B"
    elif score >=60:
        grade = "C"
    elif score >=50:
        grade = "D"
    else: 
        grade = "F"
        
    print("Grade :", grade )
    print("------------------------------")


check_grade("yuki", 85)
check_grade("ploy", 70)
check_grade("soren", 50)
check_grade("ref", 49)