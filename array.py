# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 22:46:13 2021

@author: Tzuyoon177
"""

ulg = 'y'
while ulg == 'y' or 'Y':
    ppn = 0.01
    diskon = 0.05
    mindisc = 200000
    
    oli = ['Duration SW20',"Castrol Magnatec","Federal Supreme XX","Yamalube","Shell"]
    harga = [53000,50000,54000,45000,46000]
    
    print("HARGA OLI")
    print("=====================================")
    print("1. DURATION SW20         |   Rp53.000")
    print("2. CASTROL MAGNATEC      |   Rp50.000")
    print("3. FEDERAL SUPREME XX    |   Rp54.000")
    print("4. YAMALUBE              |   Rp45.000")
    print("5. SHELL                 |   Rp46.000")
    print("=====================================")
    
    pilih = int(input("Pilih Oli yang akan dibeli (1-5) : "))
    
    if pilih < 1 or pilih > 5:
        print("Salah Input!")
        continue
    while pilih > 0 and pilih < 6:
        if pilih == 1:
            idx = 0
        if pilih == 2:
            idx = 1
        if pilih == 3:
            idx = 2
        if pilih == 4:
            idx = 3
        if pilih == 5:
            idx = 4
            
        print("Kamu Akan Membeli Oli " + str(oli[idx]) + " Seharga Rp" + format(harga[idx],',.2f'))

        liter = int(input("Ingin Beli Berapa Liter? > "))
        
        potongan = liter * int(harga[idx])
        
        if potongan > mindisc:
            getdisc = potongan * diskon
        else:
            getdisc = 0
            
        total = potongan - getdisc
        pajak = total * ppn
        subtotal = total + pajak
        print()
        print()
        print("./ STRUK PEMBAYARAN \.")
        print("=============================================")
        print(">> Oli yang Kamu Beli    : " + oli[idx])
        print(">> Kamu Membeli Sebanyak : " + str(liter) + " Liter")
        print(">> Harga Normal          : Rp" + format(potongan,',.2f'))
        print(">> Dapat diskon          : Rp" + format(getdisc,',.2f'))
        print(">> Total Tanpa PPN       : Rp" + format(total,',.2f'))
        print(">> PPN                   : 1%")
        print(">> Kena Pajak            : Rp" + format(pajak,',.2f'))
        print(">> Total Biaya           : Rp" + format(subtotal,',.2f'))
        print("=============================================")     
        break
    
    ulang = input(">> Apakah Anda ingin mengulangi? Y/T : ")
    if ulang == 't' or ulang == 'T':
        break