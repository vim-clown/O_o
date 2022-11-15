import O_o

def softblock(user_id, screen_name):
    O_o.api.CreateBlock(user_id=user_id, screen_name=screen_name)
    O_o.api.DestroyBlock(user_id=user_id, screen_name=screen_name)