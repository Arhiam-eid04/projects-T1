#استخدمت py العادي لانه اسهل ومتعود عليه اكثر وشائع في الاستخدام بايثون 

print ("** الجزء الأول **")
#1_________
product="iphone 17 pro max "
price=5000
quantity=25
print(product,price,quantity)
#2_________
price = float(input("Enter product price: "))
quantity = int(input("Enter quantity sold: "))
revenue = price * quantity
print(f"الإيراد الكلي: {revenue:.2f}")
#3_________
x ="1800200"
print(type(x))
x =int(x)
print(type(x))
print (x)
#__________________________________________________
print ("** الجزء الثاني **")
#1_________
sales =float(input("أدخل قيمة المبيعات الشهرية: "))

if sales < 1000:
    print("ضعيف")
elif sales <= 5000:
    print("متوسط")
else:
    print("ممتاز")
#2_________
quantity = int(input("أدخل كمية المخزون: "))

if quantity == 0:
    print("نفذ المخزون")
elif quantity < 10:
    print("كمية منخفضة")
else:
    print("متوفر")
#3_________
# **AI-powered solution**
month1 = float(input("أدخل مبيعات الشهر الأول: "))
month2 = float(input("أدخل مبيعات الشهر الثاني: "))
month3 = float(input("أدخل مبيعات الشهر الثالث: "))

if month1 >= month2 and month1 >= month3:
    print("أعلى مبيعات: الشهر الأول")
elif month2 >= month1 and month2 >= month3:
    print("أعلى مبيعات: الشهر الثاني")
else:
    print("أعلى مبيعات: الشهر الثالث")
#__________________________________________________
print ("** الجزء الثالث **")
#1_________
#اعملنا اضافة 250 على 5000 في كل مرة حسب ترتيب الاشهر 
sales = []
for i in range(12):
    sales.append(5000 + (i * 250))

months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]
for i in range(12):
    print(f"Month {i + 1}: {months[i]} - Sales: {sales[i]}")
#2_________
#("** مجموع المبيعات الأعلى من 5000 **")
sales = [4000, 4250, 4500, 4750, 5000, 5250, 5500, 5750, 6000, 6250, 6500, 6750]
total = 0
for sale in sales:
    if sale > 5000:
        total += sale
print("مجموع المبيعات الأعلى من 5000:", total)
#3_________
#("** حل مسألة FizzBuzz الشهيرة **")
print("Fizz:", end=" ")
for i in range(1, 51):
    if i % 3 == 0 and i % 5 != 0:
        print(i, end=" ")

print("\nBuzz:", end=" ")
for i in range(1, 51):
    if i % 5 == 0 and i % 3 != 0:
        print(i, end=" ")

print("\nFizzBuzz:", end=" ")
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=" ")
#4_________
print("** Number Guessing Game **")

target = 7000
guess = 0

while guess != target:
    guess = int(input("خمن هدف المبيعات: "))

    if guess > target:
        print("أعلى من الهدف")
    elif guess < target:
        print("أقل من الهدف")
    else:
        print("مبروك! خمنت الهدف بشكل صحيح")
#__________________________________________________
print ("** الجزء الرابع **")
#1_________
def calculate_revenue(price, quantity):
    return price * quantity
#2_________
def apply_discount(price, discount_percent=10):
    return price - (price * discount_percent / 100)
#3_________
def classify_performance(sales_value):
    if sales_value < 1000:
        return "ضعيف"
    elif sales_value <= 5000:
        return "متوسط"
    else:
        return "ممتاز"
#4_________
def average(numbers_list):
    return sum(numbers_list) / len(numbers_list)
#__________________________________________________
print ("** الجزء الخامس **")
#1_________
sales = [5500, 4000, 6750, 5000, 6250, 4500, 6000, 4250, 6500, 4750, 5250, 5750]

months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

highest = max(sales)
lowest = min(sales)

print("أعلى شهر مبيعات:", months[sales.index(highest)])
print("أقل شهر مبيعات:", months[sales.index(lowest)])

sales.sort()
print("المبيعات بعد الترتيب:", sales)
#2_________
sales = {
    "iPhone 17 Pro Max": 7000,
    "iPhone 16 Pro Max": 5000,
    "iPhone 15 Pro Max": 4500
}
TOP = max(sales, key=sales.get)

print("أعلى منتج مبيعًا:", TOP)
#3_________
cities = ["Ramallah", "Jerusalem", "Nablus", "Jericho", "Hebron",
          "Ramallah", "Nablus", "Hebron", "Jerusalem"]

unique_cities = set(cities)

print("المدن الفريدة:", unique_cities)
#4_________
#بستخدم Tuple لما تكون البيانات ثابتة وما بقدر أغير عليها
#اما List  بستخدمها اذا بدي اعدل على البيانات حذف أو اضافة 
#مثال 
# هان البيانات ثابتة وما بقدر اعدل عليها (Tuple)
date = (2026, 8)
print(date)

# هان بقدر اعدل احذف اضيف بيانات [List]
date = [2026, 8]
date.remove(2026)
date.append(2025)
print(date)
#__________________________________________________
print ("** الجزء السادس **")
# ***Project Page***
