# یک رمز معتبر است اگر حداقل ۸ کارکتر داشته باشد و دارای حداقل
# یک حرف کوچک، حداقل یک حرف بزرگ، حداقل یک رقم و
# حداقل یک علامت نگارشی باشد. تابع
# is_valid
# یک رشته به عنوان رمز از ورودی می‌گیرد و اگر معتبر باشد
# True
# و در غیر این صورت
# False
# برمی‌گرداند.
# در ادامه برنامه نوشته‌ایم که به طور مداوم از ورودی رمز بخواهد
# و با استفاده از تابع بالا اگر نامعتبر بود پیغام مناسب چاپ کند و
# دوباره رمز بخواهد. در نهایت اگر رمز معتبر وارد شد
# پیغام مناسب چاپ و برنامه متوقف شود

from string import ascii_lowercase, ascii_uppercase, digits, punctuation

def is_valid(password):
    if len(password) < 8:
        return False

    has_lower = has_upper = has_num = has_punc = False

    for char in password:
        if char in ascii_lowercase:
            has_lower = True
        elif char in ascii_uppercase:
            has_upper = True
        elif char in digits:
            has_num = True
        elif char in punctuation:
            has_punc = True

    return has_lower and has_upper and has_num and has_punc

while True:
    password = input("Password: ")
    if not is_valid(password):
        print("Invalid password")
    else:
        print("Valid password")
        break

