ItemInCart = 0
if ItemInCart !=2:
    #raise Exception("Product count not meet")
    pass
assert(ItemInCart==0)

#TRY ,,,, CATCH -EXCEPT
try:
    with open("test.txt","r") as f:
        f.read()

except:
    print("This is except block")
