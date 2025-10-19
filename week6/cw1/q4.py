class SmartPhone :
    def __init__(self , brand : str ,  model : str , storage : int ,
        battery : int , camera_mp : int):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery
        self.camera_mp = camera_mp

    def make_call(self ,number : int):
        print(f"{number} miss calls")

    def take_photo(self ,photo):
        print(f"{photo} photo is taken")

    def install_app(self , app_name):
        print(f"{app_name} app is installed")

    def check_battery(self , battery ):
        print(f"the battery percentage is {battery}  ")

phone = SmartPhone("apple" , "17 pro max" , 125 ,
        800 , 300)
phone.make_call(126472)
phone.check_battery(400)
