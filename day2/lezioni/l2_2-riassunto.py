import os

#la funzione  listdir genera una lista contenente tutti i file contenuti in una cartella
#modificate questa stringa con il un path a piacere sul vostro pc
folder='C:\\Users\\FL5585\\git\\corso-python\\day1\\'


files = os.listdir()
print('stampa i file contenuti in folder')
print(files)

# è possibile utilizzare anche os.walk() per fare una ricerca ricorsiva nelle sotto cartelle
print('\n\nstampa ricorsivamente i file contenuti in tutte le sub-folder')
files = os.walk(folder)
for root, dirs, files in os.walk(folder,topdown=False):
    print('folder:  '+str(root)+'\t\t\t\t\tfiles: '+str(files))


#Esercizio Stampare tutti i file del corso che trattano le iterazioni