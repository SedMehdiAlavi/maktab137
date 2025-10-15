# یک generator به نام read_file پیاده‌سازی کنید، به‌طوری‌که نام فایل
# را به عنوان ورودی و محتوا فایل را به صورت
# خط‌ به خط به عنوان خروجی برگرداند.
#
# حالا باتوجه به تصویر جاهای خالی را پر کنید.

def read_file(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line


for line in read_file('somefile.txt'):
    print(line)