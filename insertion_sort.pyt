def insertionSort(dizi):
 
    
    for i in range(1, len(dizi)):
 
        deger = dizi[i]
        
        j = i-1
        while j >=0 and deger< dizi[j] :
                dizi[j+1] = dizi[j]
                j -= 1
        dizi[j+1] = deger

        dizi= [7,3,5,8,2,9,4,15,6]
        insertionSort(dizi)
        for i in range(len(dizi)):
         print ("% d" % dizi[i])
         

