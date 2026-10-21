# สถานการณ์
# ร้านค้าต้องการโปรแกรมรับข้อมูลสินค้าหลายรายการ แล้วคำนวณยอดรวมทั้งหมดในบิลเดียว
# Requirements
# 1. รับจำนวนรายการสินค้าที่ต้องการกรอก เช่น 3
# 2. ใช้ Loop เพื่อรับข้อมูลตามจำนวนรายการนั้น
# 3. ในแต่ละรอบ รับชื่อสินค้า ราคาต่อชิ้น และจำนวนที่ซื้อ
# 4. คำนวณยอดรวมของสินค้าแต่ละรายการ
# 5. สะสมยอดรวมทุกสินค้าไว้ในตัวแปรเดียว
# 6. เมื่อ Loop จบ ให้แสดงยอดรวมทั้งบิล
# 7. สมมติว่าผู้ใช้กรอกตัวเลขถูกประเภท และจำนวนรายการไม่ติดลบ

# Number of products: 2

# Product: Milk
# Price: 35.5
# Quantity: 2
# Subtotal: 71.0

# Product: Water
# Price: 10
# Quantity: 3
# Subtotal: 30.0

# Grand total: 101.0

product_number = int(input("Number of products: "))
count = 0
while count < product_number:
    count = count + 1
    print("Product", count)
    product = input("Product: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))
    subtotal = price * quantity
    print("Subtotal:", subtotal)
    grand_total = 0
    grand_total = grand_total + subtotal


print("Grand total:", grand_total)

