try :
    file = open('YashjiChalJayege.txt', 'r')
    dataOut = file.read()
    print(dataOut)
except FileNotFoundError :
    print("No such file found")
except Exception as ex:
    print(ex)
finally :
    if 'file' in locals() or file.closed():
        file.close()
        print('file closed')
