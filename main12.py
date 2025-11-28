class employee:
    def __init__(self):
        print("Employee created")

    #calling destructor
    def __del__(self):
        print("Destructor called")

def create_obj():
    print("Making object.....")
    obj = employee()
    print("function end")
    return obj

print("calling created_Obj function....")
obj = create_obj()
print("program end....")