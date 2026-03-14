book1 = "El libro, en el libro, en el libro"
book2 = "White nights"
book3 = "El proceso"
_count = 0
def getLength(bookTitle):
    globals()['_count']=_count+1
    print( f"La longitud del título del libro {_count} es: {len(bookTitle)}")


getLength(book1)
getLength(book2)
getLength(book3)
