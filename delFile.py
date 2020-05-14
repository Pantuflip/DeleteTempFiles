# -*- coding: utf-8 -*-

"""
###############################################################################
Be ca

###############################################################################


Autor: Rafael Zapata Grau
e-mail: razazapata@rzgcontrol.com

programa para borrar arhivos
._.DS_Store
.DS_Store
._*
Recorriendo todas las subcarpetas seleccionadas.

Program to delete filesList
._.DS_Store
.DS_Store
._*
looking inside every subfolder

"""
import os
from send2trash import send2trash # I really don't use, because don't work really good.



def deleteFile(pathFile):
    if os.path.exists(pathFile):
        #retorno = send2trash(pathFile) # Libreria que enviar los archivos o carpetas borrados a la papelera de reciclaje.
        retorno = os.remove(pathFile) # Este comando borra y despues de borrado no se pueden recuperar los archivos
        print(retorno)

    else:
        print("Archivos no se pudieron eliminar.")


def listSubFolders(MainFolder):
    mi_List = [ ]

    for d in os.listdir(MainFolder):
        if os.path.isdir(os.path.join(MainFolder, d)):
            mi_List.append(MainFolder +"/"+d)

    if len(mi_List) < 1:
        return mi_List
        print("Fin")
    else:
        for subfolder in mi_List:
            mi_List.extend(listSubFolders(subfolder))
        return mi_List


def listFiles(MainFolder):
    return [MainFolder+"/"+f for f in os.listdir(MainFolder) if os.path.isfile(os.path.join(MainFolder, f))]


def printList(lista):
    for data in lista:
        print(data)


def listFileFilter(lista):
    newList = []
    for filepath in lista:
        filename = filepath.split("/")[-1]
        if filename[0]=="." and filename[1]=="_":
            newList.append(filepath)
        elif filename == ".DS_Store":
            newList.append(filepath)
    return newList


### -----------  MAIN PROGRAM -----------------------------------
def run():
    filesListT = []
    # Test D:\CursoPlatzi
    # findPath = "C:\CursoPlatzi"
    findPath = input("Digita path de busqueda: por ejemplo (D:\\)   \n?? ")
    while os.path.exists(findPath) is False:  # validation
            findPath = input("Digita path de busqueda: por ejemplo (D:\\)   \n?? ")
    folders = listSubFolders(findPath)
    folders.insert(0, findPath)

    #print(type(folders))
    #printList(folders)

    ##
    ##print("\n Todos los archivos")
    for folder in folders:
        filesListT.extend(listFiles(folder))
    ##printList(filesListT)

    print("\n Filtrados:")
    filesListToDelete = listFileFilter(filesListT)
    printList(filesListToDelete)
    respuesta_Usuario = input("\n\nDigita (s) para borrar los arhivos. \nDigita cualquier tecla para cancelar el borrado. \n?? ")

    if respuesta_Usuario.lower() == "s":
        for pathFile in filesListToDelete:
            deleteFile(pathFile)
    else:
        quit()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Main ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':
    run()
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
