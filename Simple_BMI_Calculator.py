print ("\nKALKULATOR SEDERHANA\n")
while True:
    print('Satuan Panjang :\n 1. Cm (Centi Meter)\n 2. M (Meter)\n')
    Satuan_Panjang = int(input('Pilih Satuan Panjang : '))
    if Satuan_Panjang == 1:
      Tinggi_Badan = float(input('Masukkan tinggi badan anda (Cm) : '))
      Berat_Badan = float(input('Masukkan berat badan anda (Kg) : '))
      Tinggi_M = (Tinggi_Badan / 100)
      BMI = (Berat_Badan) / (Tinggi_M ** 2)
  
      print('Hasil perhitungan BMI anda adalah', BMI)
      if BMI <= 18.5:
        print('Berat badan kurang (underweight)')
      elif BMI <= 24.9:
        print('Berat badan normal')
      elif BMI <= 29.9:
        print('Kelebihan berat badan (overweight)')
      else :
        print('Obesitas')
    
    elif Satuan_Panjang == 2:
      while True:
        Tinggi_M = float(input('Masukkan tinggi badan anda (M) : '))
        Berat_Badan = float(input('Masukkan berat badan anda (Kg) : '))
        BMI = (Berat_Badan) / (Tinggi_M ** 2)
  
        print('Hasil perhitungan BMI anda adalah', BMI)
        if BMI <= 18.5:
          print('Berat badan kurang (underweight)')
        elif BMI <= 24.9:
          print('Berat badan normal')
        elif BMI <= 29.9:
          print('Kelebihan berat badan (overweight)')
        else :
          print('Obesitas')
    
    else:
      print('\nHarap hanya input opsi 1 atau 2 !!! \n')