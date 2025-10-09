cw7:
import random
import time
import os
def memory_game(length=6, show_second=3):
    seq = [random.randint(1, 99) for _ in range(length)]
    print("list: ", seq)
    time.sleep(show_second)
    clear_cmd ='cls' if os.name == "nt" else "clear"
    os.system(clear_cmd)
    ans = input(" plz inter ur number with distance!:")
    ans_list = [int(x) for x in ans.split() if x.isdigit()]
    score = 0
    for i in range(min(len(seq), len(ans_list))):
        if seq[i] == ans_list[i]:
            score = score + 1
        else:
            score = score - 1
    name = input("inter ur name for saving ur scores: ")
    try:
        with open("memory_scores.txt", "a", encoding="utf-8") as f:
            f.write(f"{name}: {score}\n")
        print(f"ur score: {score} -- is saved! ")
    except Exception as error:
        print("error in saving ur score: ", error)
memory_game()
---------------------------------------------------
