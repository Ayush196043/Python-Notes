# for import thr module make the module 
def welcome():
    print("Hey you are welcome from Ayush")

print(__name__)# by use this we find progreme run kaha se kar raha hai.
#output is "__main__"--> yahi se run jho raha hai,and when give the name odf any file then tell the location kaha se run ho raha hai

if __name__=="__main__":# It's tell ki jab ham is function ko yaha run karwaye to run kare lekin import karte time pe waha pe do barr run na kare..
    welcome()  

