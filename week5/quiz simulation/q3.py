# برنامه‌ای بنویسید که هر بار عددی را دریافت کند
# . در صورتی که ورودی از جنس صحیح یا اعشاری بود
# این کار را ادامه دهد تا جایی که
#
# Ctrl + C
#
# یا همان
#
# Keyboard Interrupt
#
# صدا زده شود. در این صورت جمع اعداد را اعلام کند و برنامه تمام شود.
#
# در صورتی که ورودی از جنس عددی نبود (صحیح یا اعشاری) دقیقا
# باید پیغام مناسب چاپ شود و دوباره ورودی بگیرد.
#
# جاهای خالی را با کد مناسب پر کنید.
#

num_sum = 0

while True:
    try:
        num = input("Enter a number: ")
    except KeyboardInterrupt:
            print('sum = ', num_sum)
            break

    try:
        num = int(num)
        num_sum += num
    except ValueError:
            try:
                num = float(num)
                num_sum += num
            except ValueError:
                print('Enter an integer or float')
                continue