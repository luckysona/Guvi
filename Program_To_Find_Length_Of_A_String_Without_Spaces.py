''' PROGRAM TO PRINT LENGTH OF THE STRING WITHOUT SPACES '''
def space(strg): 
    return "".join(strg.split())
a=input()
b=space(a)
print(len(b))
