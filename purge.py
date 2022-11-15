import random, time, datetime
from O_0 import api, softblock

followers = api.GetFollowers(count=random(0, 69))
flag = True
while flag:
    nb = len(followers)
    print(f"{nb} followers will be softblocked")
    
    to_block = random.sample(followers, nb)
    time_on_start = datetime.datetime.now()
    
    print("[+] starting")
    for user in to_block:
        print("[+] soft-blocking user " + user.name + "; ID : " + str(user.id))
        softblock(user.id, user.name)
    print("[+] done")

    time_on_end = datetime.datetime.now()

    api.PostUpdate(
        f"[Start: {time_on_start}] \n [End: {time_on_end}] \n Purged {nb} random targets. \n Sleeping."
    )

    time.sleep(86400)  # 24hrs
