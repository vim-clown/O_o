import O_0

def softblock(user_id, screen_name):
    O_0.api.CreateBlock(user_id=user_id, screen_name=screen_name)
    O_0.api.DestroyBlock(user_id=user_id, screen_name=screen_name)