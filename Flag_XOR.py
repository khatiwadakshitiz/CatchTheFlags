KEY1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
S1 = bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e") #KEY2 ^ KEY1
S2 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1") #KEY2 ^ KEY3 
S3 = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf") #FLAG ^ KEY1 ^ KEY3 ^ KEY2

#defining fucntion : 
def XOR_gate(first,second):
    result = bytes(f ^ s for f,s in zip(first,second))
    return result
#Finding KEY2, XOR KEY1 on S1 gives KEY2
KEY2 = XOR_gate(S1,KEY1)
print(KEY2.hex())
#for KEY3, KEY2 ^ S2 will give KEY3

KEY3 = XOR_gate(KEY2,S2)
print(KEY3.hex())

#for flag, we have to repear similar, first S3 xor KEY2, then result xor key3 , then result xor key 1 gives flag 

FLAG = XOR_gate(XOR_gate(XOR_gate(S3,KEY2),KEY3),KEY1)
print(FLAG)