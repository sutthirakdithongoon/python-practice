# Requirements
# 1. รับชื่อสินค้าจากผู้ใช้
# 2. รับจำนวนสินค้าที่มีในสต็อกเป็นจำนวนเต็ม
# 3. รับจำนวนสินค้าที่ลูกค้าต้องการซื้อเป็นจำนวนเต็ม
# 4. ถ้าจำนวนที่ต้องการซื้อเป็น 0 หรือติดลบ ให้แสดง Invalid quantity
# 5. ถ้าจำนวนที่ต้องการซื้อมากกว่าสต็อก ให้แสดง Not enough stock
# 6. ถ้าสต็อกเพียงพอ ให้แสดง Order accepted และคำนวณจำนวนสินค้าคงเหลือ


product_name = input("Product : ")
stock = int(input("Stock : "))
order_quantity = int(input("Order quantity : "))
print("Product : ", product_name)
print("Stock : ", stock)
print("Order quantity : ", order_quantity)

if order_quantity  <= 0  :
   print ("Invalid quantity")

elif order_quantity > stock :
    print ("Not enough stock") 

else :
   stock = stock - order_quantity
   print ("Order accepted : " )
   print ("Remaining stock :",stock  )