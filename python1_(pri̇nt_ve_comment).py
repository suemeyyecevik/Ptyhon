# -*- coding: utf-8 -*-
"""Python1 (PRİNT VE COMMENT).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1h2-zlygJ72eyDtkNDp93hlvk3dy3oQbh
"""

!python3 --version  # ile hangi sürümü kullandığınızı görebilirsiniz.

!python3  -V   # ile de hangi sürümü kullandığınızı görebilirsiniz.

print ('Hello')
                 # print yazma komutudur. Tırnak içinde (çift veya tek tırnak kullanılabilir) yazmamız gerekir.
                 # hangi tırnak ile başladıysa öyle bitmeli tek ise tek tırnak ile çift tırnak ile
                 # ise çift tırnak işareti ile bitmelidir.

"""**TIRNAK MESELESİ**

Python da bir sabit mesaj ekrana basılacaksa print deyimi yanında tek tırnak ya da çift tırnak, 3 çift veya 3 tek tırnak da kullanılabilir.
"""

print (''' Hello''')  # 3 tane tek tırnak kullandık arasına mesajımızı yazdık yine aynı çıktıyı verir.
                      # Tırnak arasına konulan her şey doğrudan ekrana yazılır.

print ('Merhaba Dünya')

print("SELAM")

print ('''"<ipython-input-14-fe8e9c90c0b2>", line 1
    print("SELAM"
                 ^
SyntaxError: incomplete input''')
                # Tek veya çift tırnaklar tek satırlı mesajlar için kullanılır.
                # 3 tek tırnak veya 3 çift tırnaklarla çok satılı mesajlar için kullanılır.

print('3.14') # Tırnak içerisine yazılan mesaj ve text string dir.
              # String

print(3.14) # Tırnak içerisinde değilse float tır yani sayidir.

type (3.14) # Type deyimi veri tipini gösterir.

type ('hello') # Type deyimi str sözel veridir.

print (3+10) # Type deyimi float tır sayısal veri tipidir.

print('ilk satır')
print()               # Boş bir satır bırakır.
print('ikinci satır')

print ('1.satır')
print ()            # 2. boş satır bırakır.
print ('')
print('4.satır')

"""# PEP 8 NEDİR?
Pyton geliştirici önerileri demektir.
Bu önerilere uyarsanız kodunuzu güzelleştirecektir.
Bir proje içerisinde kullanmanız çok daha önemli.
Bir programcının vaktinin çoğu yazmakla değil okumakla geçer bu yüzden kodların okunabilirliğini arttıran şey PEP8 kurallarıdır.



PYTHON RESMİ SİTESİ
https://peps.python.org/pep-0008/#a-foolish-consistency-is-the-hobgoblin-of-little-minds

buradan da rahatça öğrenebilirsiniz.

**YORUM SATIRLARI** COMMENT  

-Yorum satırları programcı için yazılır.
- hash karakteri kullanılır, bu karakterden sonra derleyicisi yorumlamaz.
"""

print ('MERHABA')  # Print ('MERHABA') anlamında. Basit şeyler için yorumlar kullanılmaz.
                   # Karmaşık kodlarda açıklamak için kullanılır.
                   # Çok satırlı yorumlar için hash karakteri alt alta kullanılabilir.

