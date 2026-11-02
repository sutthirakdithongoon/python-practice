# DEV-005 — Functional Requirements
# - [ ] REQ-01: รับจำนวนรายการสินค้าที่ต้องการบันทึก
# - [ ] REQ-02: ใช้ for หรือ while Loop รับข้อมูลตามจำนวนรายการ
# - [ ] REQ-03: ในแต่ละรอบ รับชื่อสินค้า (name), ราคา (price) และจำนวนในสต็อก (quantity)
# - [ ] REQ-04: จัดเก็บสินค้าแต่ละรายการเป็น Dictionary ที่มี Key ชื่อ name, price, quantity
# - [ ] REQ-05: นำ Dictionary แต่ละรายการเพิ่มเข้า List ด้วย append()
# - [ ] REQ-06: เมื่อรับข้อมูลครบแล้ว ใช้ Loop อีกครั้งเพื่อแสดงชื่อ ราคา และจำนวนสินค้าทุกตัว
# - [ ] REQ-07: แสดงจำนวนประเภทสินค้าทั้งหมดที่บันทึกได้ โดยใช้ len()

products = []

product_number = int(input("Number of products: "))


for i in range(product_number):
    name = input("Product name: ")
    price = float(input("Product price: "))
    quantity = int(input("Product quantity: "))
    product = {"name": name, "price": price, "quantity": quantity}
    products.append(product)

print("Product Information:")
for product in products:
    print(f"Name: {product['name']}, Price: {product['price']}, Quantity: {product['quantity']}")

print(f"\nTotal types of products: {len(products)}")





# REQ-01: รับจำนวนนักเรียนที่ต้องการบันทึก
# REQ-02: ใช้ for หรือ while Loop รับข้อมูลนักเรียนแต่ละคน
# REQ-03: รับชื่อนักเรียน (name) และคะแนน (score) โดยคะแนนเป็น float
# REQ-04: เก็บข้อมูลนักเรียนแต่ละคนเป็น Dictionary ที่มี Key name และ score
# REQ-05: เพิ่ม Dictionary เข้า List ด้วย append()
# REQ-06: หลังรับข้อมูลครบ ใช้ Loop อีกชุดแสดงชื่อนักเรียน คะแนน และสถานะสอบผ่าน
# REQ-07: คะแนนตั้งแต่ 50 ขึ้นไปแสดง Pass ต่ำกว่า 50 แสดง Fail
# REQ-08: ใช้ len() แสดงจำนวนนักเรียนทั้งหมด
# REQ-09: แสดงจำนวนนักเรียนที่สอบผ่านทั้งหมด



students = []
students_number = int(input("Number of students: "))
for i in range(students_number):
    name = input("Student name: ")
    score = float(input("Student score: "))
    student = {"name": name, "score": score}
    students.append(student)
    
print("Student Information:")
for student in students:
    status = "Pass" if student["score"] >= 50 else "Fail"
    print(f"Name: {student['name']}, Score: {student['score']}, Status: {status}")

print(f"\nTotal number of students: {len(students)}")

passing_students = [student for student in students if student["score"] >= 50]
print(f"Number of passing students: {len(passing_students)}") 





# Requirements
# - REQ-01: รับจำนวนรายการรายจ่ายจากผู้ใช้
# - REQ-02: สร้าง List ว่างเพื่อเก็บรายจ่ายทั้งหมด
# - REQ-03: ใช้ Loop รับชื่อรายการ (name) และจำนวนเงิน (amount) ซึ่งเป็น float
# - REQ-04: เก็บรายจ่ายแต่ละรายการเป็น Dictionary ที่มี Key name และ amount
# - REQ-05: เพิ่ม Dictionary แต่ละรายการเข้า List ด้วย append()
# - REQ-06: หลังรับข้อมูลครบ ใช้ Loop อีกชุดแสดงชื่อและจำนวนเงินของแต่ละรายการ
# - REQ-07: คำนวณยอดรายจ่ายรวมทั้งหมด (total_expense)
# - REQ-08: นับจำนวนรายการที่มีรายจ่าย มากกว่า 100 บาท (expensive_count) โดยใช้ Counter, for และ if ไม่ใช้ List Comprehension
# - REQ-09: แสดงจำนวนรายการทั้งหมดด้วย len()
# - REQ-10: ถ้าไม่มีรายการรายจ่าย โปรแกรมต้องแสดงยอดรวมและจำนวนรายการเป็น 0 โดยไม่เกิด Error


expenses = []
number_expense= int(input("Number of expenses: "))
total_expense = 0
expensive_count = 0
for i in range(number_expense):
      name = input("Name: ")
      amount = float(input("Amount: "))
      expense = {"name": name, "amount": amount}
      expenses.append(expense) 
for expense in expenses:
      print(f"Name :   {expense['name']}, Amount :  {expense['amount']} ")
      total_expense = total_expense +  expense["amount"]
      if expense["amount"] > 100:
         expensive_count = expensive_count +1

print ("Total expenses: ", total_expense )
print ("Expensive items: ", expensive_count )
print ("Total items: ", len(expenses) )



# รับจำนวนสินค้าทั้งหมดจากผู้ใช้
# [ ] ใช้ Loop รับชื่อ ราคา และจำนวนคงเหลือของแต่ละสินค้า
# [ ] เก็บสินค้าแต่ละรายการเป็น Dictionary และเพิ่มลง List
# [ ] ใช้ Loop แสดงชื่อ ราคา และจำนวนคงเหลือของสินค้าทั้งหมด
# [ ] แสดงสถานะสินค้าโดยใช้เงื่อนไข Stock Status
# [ ] คำนวณมูลค่าสินค้าคงคลังรวมด้วย Accumulator
# [ ] นับจำนวนสินค้าที่มีสถานะ Low Stock ด้วย Counter
# [ ] นับจำนวนสินค้าที่มีสถานะ Out of Stock ด้วย Counter
# [ ] แสดงจำนวนประเภทสินค้าทั้งหมดด้วย len()
# [ ] รองรับกรณีไม่มีสินค้าเลย (0 รายการ)





stocks = []
total_value = 0
low_stock = 0
out_stock = 0
number_product = int(input("number of product :"))

for i in range(number_product):
    name = input("Name : ")
    price = float(input("Price : "))
    quantity = int(input("Quantity : "))
    stock = {"name": name, "price": price, "quantity": quantity}
    stocks.append(stock)
for stock in stocks:
    print("Name :", stock["name"])
    print("Price :", stock["price"])
    print("quantity :",  stock["quantity"])
    if stock ["quantity"] > 5 :
       print ("Status :  In Stock")
    elif stock ["quantity"] == 0 :
          out_stock = out_stock +1 
          print ("Status : Out of Stock")
    else :
          low_stock = low_stock+1
          print ("Status : Low Stock")
    total_value = total_value +  stock["quantity"]*stock["price"] 

print("Total products :", len(stocks))
print("Total inventory value :", total_value)
print("Low stock items :", low_stock ) 
print("Out of stock items :" ,out_stock )    





orders = []
total_paid = 0
status_paid = 0
status_pending = 0

num_order = int(input("Number of orders:" ))

for i in range(num_order):
       customer = input("Customer: ")
       amount = float(input("Amount : "))
       status = input("Status : ")
       order = {"customer": customer, "amount": amount, "status": status } 
       orders.append(order)
for order in orders:
       print (f"Customer: {order['customer']}, Amount : {order['amount']}, Status : {order['status']}")
       if order["status"] == "Paid":
            status_paid = status_paid +1
            total_paid = total_paid + order["amount"]
       elif order["status"] == "Pending":
            status_pending = status_pending +1
       else :
            print("Status error please check ")

print("Total orders : ", len(orders))
print("Total paid amount : ", total_paid)
print("Paid orders : ", status_paid)
print("Pending orders : ", status_pending)




