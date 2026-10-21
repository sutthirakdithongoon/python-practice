# Requirements
# 1. รับชื่อสินค้าจากผู้ใช้
# 2. รับราคาสินค้าต่อชิ้นเป็นเลขทศนิยม
# 3. รับจำนวนสินค้าเป็นจำนวนเต็ม
# 4. คำนวณยอดรวมจากราคา × จำนวน
# 5. แสดงผลชื่อสินค้า ราคา จำนวน และยอดรวม พร้อมข้อความกำกับ

product_name = input("ชื่อสินค้า : ")
price = float(input("ราคาสินค้า : "))
quantity = int(input("จำนวนสินค้า : "))
total_value = price * quantity 

print("ชื่อสินค้า", product_name )
print("ราคาสินค้า", price )
print("จำนวนสินค้า", quantity)
print("มูลค่าสินค้า", total_value)