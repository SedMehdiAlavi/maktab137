# جاهای خالی را طوری پر کنید
# تا این تابع IndexError را مدیریت کند.

def print_list_element(thelist, index):
    try:
        print(thelist[index])

    except IndexError:
        print("Invalid Index")

