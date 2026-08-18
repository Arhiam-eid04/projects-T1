                          # *** Project Page ***

#1 خزّن المبيعات بـ Dictionary رئيسي

print("نظام تتبّع المبيعات (المنتجات واسعارها)")

sales_data = {
    "iPhone 17 Pro Max": [7000, 7500, 8000],
    "iPhone 16 Pro Max": [5000, 5500, 6000],
    "iPhone 15 Pro Max": [4000, 4500, 5000]
}
#________________________________________________________________________________

#2 اعمل قائمة تفاعلية (Menu) تُعرض بحلقة while True وفيها الخيارات:
#3قسّم كل عملية إلى دالة منفصلة، ولا تضع كل الكود في دالة واحدة.
#4عالج الأخطاء برسائل واضحة بدل ما يتوقف البرنامج، مثل المنتج غير الموجود أو عدم وجود مبيعات.

#_____________
#1. إضافة منتج جديد إلى النظام
def add_product():
    product_name = input("أدخل اسم المنتج: ")

    if product_name in sales_data:
        print("المنتج موجود مسبقًا.")
        return

    sales_data[product_name] = []
    print("تمت إضافة المنتج بنجاح.")

#_____________
#2. تسجيل مبيعات شهر جديد لمنتج موجود
def add_monthly_sale():
    product_name = input("أدخل اسم المنتج: ")

    if product_name not in sales_data:
        print("المنتج غير موجود.")
        return

    sale = float(input("أدخل مبيعات الشهر: "))
    sales_data[product_name].append(sale)

    print("تم تسجيل المبيعات بنجاح.")

#_____________
#3. عرض جميع المنتجات ومبيعاتها الشهرية
def display_sales():
    for product, sales in sales_data.items():
        print(product, ":", sales)

#_____________
#4. حساب إجمالي مبيعات منتج معين
def calculate_total_sales():
    product_name = input("أدخل اسم المنتج: ")

    if product_name not in sales_data:
        print("المنتج غير موجود.")
        return

    if len(sales_data[product_name]) == 0:
        print("لا توجد مبيعات مسجلة لهذا المنتج.")
        return

    total = sum(sales_data[product_name])
    print("إجمالي المبيعات:", total)

#_____________
#5. حساب متوسط المبيعات الشهرية لمنتج معين
def calculate_average_sales():
    product_name = input("أدخل اسم المنتج: ")

    if product_name not in sales_data:
        print("المنتج غير موجود.")
        return

    if len(sales_data[product_name]) == 0:
        print("لا توجد مبيعات مسجلة لهذا المنتج.")
        return

    average = sum(sales_data[product_name]) / len(sales_data[product_name])
    print("متوسط المبيعات الشهرية:", average)

#_____________
#6. البحث عن المنتج الأعلى مبيعًا
def find_top_product():
    if not sales_data:
        print("لا توجد منتجات مسجلة.")
        return

    top_product = max(
        sales_data,
        key=lambda product: sum(sales_data[product])
    )

    print("المنتج الأعلى مبيعًا:", top_product)
    print("إجمالي مبيعاته:", sum(sales_data[top_product]))

#_____________
#7. القائمة التفاعلية Menu
while True:
    print("\n--- Menu ---")
    print("1. إضافة منتج جديد")
    print("2. تسجيل مبيعات شهر جديد")
    print("3. عرض جميع المنتجات ومبيعاتها")
    print("4. حساب إجمالي مبيعات منتج")
    print("5. حساب متوسط المبيعات الشهرية")
    print("6. البحث عن المنتج الأعلى مبيعًا")
    print("7. خروج")

    choice = input("اختر رقمًا: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        add_monthly_sale()

    elif choice == "3":
        display_sales()

    elif choice == "4":
        calculate_total_sales()

    elif choice == "5":
        calculate_average_sales()

    elif choice == "6":
        find_top_product()

    elif choice == "7":
        print("تم إنهاء البرنامج.")
        break

    else:
        print("اختيار غير صحيح.")
#________________________________________________________________________________
## استخدام Set لتخزين فئات المنتجات بدون تكرار
categories = {"Phones", "Tablets", "Chargers"}

print("فئات المنتجات:", categories)