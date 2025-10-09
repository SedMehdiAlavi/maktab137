
vip_users = {"ali", "reza", "sara", "hadi"}
normal_users = {"nima", "sara", "hadi", "mahdi"}

eshterak = vip_users & normal_users

ejtema = vip_users | normal_users

users = ejtema - eshterak

print(users)
