import uuid


def get_random_code():
    code = str(uuid.uuid4())[:11].replace("-", "")
    #bir sürü karakter ve tire oldu,  biz tireyi kaldırıp 10 karakter bulmalıyız
    return code

print('random str:',get_random_code())
