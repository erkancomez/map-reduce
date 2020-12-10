# encoding:utf-8
"""
Created in #home

@author: erkan mustafa ali
"""
# def dosyayaz():

#     import requests
#     from bs4 import BeautifulSoup

#     URL  = 'https://www.togg.com.tr/'
#     URL1 = 'https://www.ziraatbank.com.tr/tr'
#     URL2 = 'https://www.turktelekom.com.tr/'
#     URL3 = 'https://www.ziraatbank.com.tr/tr'
#     URL4 = 'https://people.ok.ubc.ca/ylucet/DS/Huffman.html'

#     page  = requests.get(URL)
#     page1 = requests.get(URL1)
#     page2 = requests.get(URL2)
#     page3 = requests.get(URL3)
#     page4 = requests.get(URL4)

#     soup  = BeautifulSoup(page.content, 'html.parser')
#     soup1 = BeautifulSoup(page1.content, 'html.parser')
#     soup2 = BeautifulSoup(page2.content, 'html.parser')
#     soup3 = BeautifulSoup(page3.content, 'html.parser')
#     soup4 = BeautifulSoup(page4.content, 'html.parser')

#     dosya  = open("source1.txt","w")
#     dosya1 = open("source2.txt","w")
#     dosya2 = open("source3.txt","w")
#     dosya3 = open("source4.txt","w")
#     dosya4 = open("source5.txt","w")
    
#     dosya.write(str(soup))
#     dosya1.write(str(soup1))
#     dosya2.write(str(soup2))
#     dosya3.write(str(soup3))
#     dosya4.write(str(soup4))    
    
#     dosya.close()
#     dosya1.close()
#     dosya2.close()
#     dosya3.close()
#     dosya4.close()

# dosyayaz()

#--------------------- 1.Mapper

from functools import reduce   
from collections import Counter

list1 = []  
list2 = []  
list3 = []  
list4 = []  

print("\n----------------------Birinci kısım başlangıç--------------------------\n")

def wordCount():
    
    dosya = open("source1.txt","r")
    inputString = (dosya.read())
    dosya.close()

    strs = inputString
    a = Counter(map(str.lower,strs.split()))
    print(a['<head>']," tane <head> sayıldı")
    print(a['<div']," tane <div sayıldı")
    print(a['</script>']," tane </script> sayıldı")
    print(a['<meta']," tane <meta sayıldı")
    print()
    
    x1= a['<head>']
    list1.append(x1)
    
    y1= a['<div']
    list2.append(y1)
    
    z1= a['</script>']
    list3.append(z1)
    
    w1= a['<meta']
    list4.append(w1)
    
#--------------------- 2.Mapper

def wordCount1():
    
    dosya1 = open("source2.txt","r")
    inputString1 = (dosya1.read())
    dosya1.close()

    strs = inputString1
    b = Counter(map(str.lower,strs.split()))
    print(b['<head>']," tane <head> sayıldı")
    print(b['<div']," tane <div sayıldı")
    print(b['</script>']," tane </script> sayıldı")
    print(b['<meta']," tane <meta sayıldı")
    print()

    x2= b['<head>']
    list1.append(x2)
    
    y2= b['<div']
    list2.append(y2)
    
    z2= b['</script>']
    list3.append(z2)

    w2= b['<meta']
    list4.append(w2)    

#--------------------- 3.Mapper

def wordCount2():
    
    dosya2 = open("source3.txt","r")
    inputString2 = (dosya2.read())
    dosya2.close()

    strs = inputString2
    c = Counter(map(str.lower,strs.split()))
    print(c['<head>']," tane <head> sayıldı")
    print(c['<div']," tane <div sayıldı")
    print(c['</script>']," tane </script> sayıldı")
    print(c['<meta']," tane <meta sayıldı")
    print()

    x3= c['<head>']
    list1.append(x3)
    
    y3= c['<div']
    list2.append(y3)
    
    z3= c['</script>']
    list3.append(z3)
    
    w3= c['<meta']
    list4.append(w3)    

#--------------------- 4.Mapper

def wordCount3():
    
    dosya3 = open("source4.txt","r")
    inputString3 = (dosya3.read())
    dosya3.close()

    strs = inputString3
    d = Counter(map(str.lower,strs.split()))
    print(d['<head>']," tane <head> sayıldı")
    print(d['<div']," tane <div sayıldı")
    print(d['</script>']," tane </script> sayıldı")
    print(d['<meta']," tane <meta sayıldı")
    print()
    
    x4= d['<head>']
    list1.append(x4)

    y4= d['<div']
    list2.append(y4)
    
    z4= d['</script>']
    list3.append(z4)
    
    w4= d['<meta']
    list4.append(w4)

#--------------------- 5.Mapper

def wordCount4():
    
    dosya4 = open("source5.txt","r")
    inputString4 = (dosya4.read())
    dosya4.close()

    strs = inputString4
    e = Counter(map(str.lower,strs.split()))
    print(e['<head>']," tane <head> sayıldı")
    print(e['<div']," tane <div sayıldı")
    print(e['</script>']," tane </script> sayıldı")
    print(e['<meta']," tane <meta sayıldı")
    print()

    x5= e['<head>']
    list1.append(x5)

    y5= e['<div']
    list2.append(y5)
    
    z5= e['</script>']
    list3.append(z5)
    
    w5= e['<meta']
    list4.append(w5)    
    
##-----------------------------------    
 
wordCount()
wordCount1()
wordCount2()
wordCount3()
wordCount4()


print("Liste 1",list1)
print("Liste 2",list2)
print("Liste 3",list3)
print("Liste 4",list4)

toplam = reduce(lambda x,y:x+y , list1)
toplam1 = reduce(lambda x,y:x+y , list2)
toplam2 = reduce(lambda x,y:x+y , list3)
toplam3 = reduce(lambda x,y:x+y , list4)

print()

print("Toplam",toplam,"adet <head> sayıldı")
print("Toplam",toplam1,"adet <div sayıldı")
print("Toplam",toplam2,"adet </script> sayıldı")
print("Toplam",toplam3,"adet <meta sayıldı")


print("\n------------------------Birinci kısım sonu----------------------------\n")
print("\n----------------------İkinci kısım başlangıç--------------------------\n")

def listToString(ref):  
     
    str1 = ""  
    
    for ele in ref:  
        str1 += ele + " "  

    return str1  
 
listsayac1 = []

def wordCount5():
    
    dosya5 = open("source1.txt","r")
    inputString5 = (dosya5.read())
    dosya5.close()
    
    ikliste = inputString5.split()

    sayi1 = ikliste.index("<title>")
    sayi2 = ikliste.index("</title>")

    ik = ikliste[sayi1+1:sayi2]
 
    print("Source1.txt dosyasının 'Title' etiketleri arasında ki metin: ",listToString(ik))  
      
    toplam = len(reduce(lambda x,y:x+y , ik))

    print("Source1.txt dosyasının 'Title' etiketleri arasında ki metin uzunluğu: ",toplam)
    print()    
    
    listsayac1.append(toplam)

    #--------------------- 2. Metin Title ortalaması
 
def wordCount6():
    
    dosya6 = open("source2.txt","r")
    inputString6 = (dosya6.read())
    dosya6.close()
    
    ikliste1 = inputString6.split()

    sayi3 = ikliste1.index("<title>")
    sayi4 = ikliste1.index("</title>")

    ik1 = ikliste1[sayi3+1:sayi4]

    print("Source2.txt dosyasının 'Title' etiketleri arasında ki metin: ",listToString(ik1))  
    
    toplam1 = len(reduce(lambda x,y:x+y , ik1))
    
    print("Source2.txt dosyasının 'Title' etiketleri arasında ki metin uzunluğu: ",toplam1)
    print()
   
    listsayac1.append(toplam1)
 
    #--------------------- 3. Metin Title ortalaması
    
def wordCount7():
    
    dosya7 = open("source3.txt","r")
    inputString7 = (dosya7.read())
    dosya7.close()

    ikliste2 = inputString7.split()

    sayi5 = ikliste2.index("<title>")
    sayi6 = ikliste2.index("</title>")

    ik2 = ikliste2[sayi5+1:sayi6]

    print("Source3.txt dosyasının 'Title' etiketleri arasında ki metin: ",listToString(ik2))  
    
    toplam2 = len(reduce(lambda x,y:x+y , ik2))

    print("Source3.txt dosyasının 'Title' etiketleri arasında ki metin uzunluğu: ",toplam2)
    print()
    
    listsayac1.append(toplam2)
  
    #--------------------- 4. Metin Title ortalaması
  
def wordCount8():
    
    dosya8 = open("source4.txt","r")
    inputString8 = (dosya8.read())
    dosya8.close()

    ikliste3 = inputString8.split()

    sayi7 = ikliste3.index("<title>")
    sayi8 = ikliste3.index("</title>")

    ik3 = ikliste3[sayi7+1:sayi8]

    print("Source4.txt dosyasının 'Title' etiketleri arasında ki metin: ",listToString(ik3))  
    
    toplam3 = len(reduce(lambda x,y:x+y , ik3))

    print("Source4.txt dosyasının 'Title' etiketleri arasında ki metin uzunluğu: ",toplam3)
    print()
    
    listsayac1.append(toplam3)
 
    #--------------------- 5. Metin Title ortalaması
  
def wordCount9():
    
    dosya9 = open("source5.txt","r")
    inputString9 = (dosya9.read())
    dosya9.close()

    ikliste4 = inputString9.split()

    sayi9 = ikliste4.index("<title>")
    sayi10 = ikliste4.index("</title>")

    ik4 = ikliste4[sayi9+1:sayi10]
       
    print("Source5.txt dosyasının 'Title' etiketleri arasında ki metin: ",listToString(ik4))  
    
    toplam4 = len(reduce(lambda x,y:x+y , ik4))

    print("Source5.txt dosyasının 'Title' etiketleri arasında ki metin uzunluğu: ",toplam4)
    print()
    
    listsayac1.append(toplam4)

##-----------------------------------  
    
wordCount5()
wordCount6()
wordCount7()
wordCount8()
wordCount9()
    
ortalamaharf = reduce(lambda x,y:x+y , listsayac1)

print("Ortalama metin uzunluğu", ortalamaharf/5, "harftir.\n")


print("------------------------İkinci kısım sonu----------------------------")
