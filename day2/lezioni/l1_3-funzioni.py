#le funzioni possono anche richiamare se stesse.
# In questo caso si chiamano funzioni ricorsive

def aSimpleFunction(n):

    if n==1:
        return 1
    else:
        return aSimpleFunction(n-1)+n

#DOMANDA cosa fa questa funzione ? puoi aiutarti con il debugger
#-------------------------------------------------------------------------------------- your code here!!!
