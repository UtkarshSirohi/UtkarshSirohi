#integer slicing module
def sliceint(num,decimals):
    strnum=str(num)
    findnum=strnum.find(".")
    findnum1=findnum+(decimals+1)
    printnum=strnum[:findnum1]
    return float(printnum)
