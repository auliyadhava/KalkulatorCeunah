import streamlit as st 
from PIL import Image
import pandas as pd 

#aplikasi stoikiometri  
st.image("images/gambarlogo.png")    
with st.sidebar.container():
    st.image("images/gambar1.png", width=250)
    
page_names = ("APLIKASI PERHITUNGAN STOIKIOMETRI", ['HOME','ABOUT US','CONTACT US'])
page = st.sidebar.selectbox ('APLIKASI PERHITUNGAN STOIKIOMETRI',['HOME','PERHITUNGAN STOIKIOMETRI','HUBUNGAN PERSEN B/B DAN B/V','PENGENCERAN DALAM TITRIMETRI','ABOUT US','CONTACT US'])

if (page =='HOME'):
    st.title (':green[aplikasi perhitungan stoikiometri]')
    st.markdown ('selamat datang di web kami:wave:')
    st.markdown ('aplikasi ini dapat memudahkan user dalam perhitungan kimia dasar stoikiometri dan pengenceran dalam titrimetri')
    st.write("---")
    tombol = st.button ('APLIKASI INI DIBUAT OLEH KELOMPOK 10')
    
    if tombol:
        st.write ('Dinda Salsabila Azzahra')
        st.write ('Naiya Ramadhani')
        st.write ('Pani Permatasari')
        st.write ('Syifa Nurfadilah')
        
if (page =='ABOUT US'):
    st.title(':green[aplikasi stoikiometri??]')
    st.subheader("Hello, to all user :wave:")
    st.write ('''aplikasi stoikiometri merupakan aplikasi yang akan memudahkan user untuk
              menghitung stoikiometri dan membantu untuk perhitungan pada titrasi''')
    
    st.write("---")
    st.header("Apa yang aplikasi stoikometri lakukan")
    st.write("##")
    st.write(
            """
            Di Web Aplikasi perhitungan stoikiometri ini, kita akan menyediakan untuk orang-orang yang:
            - membutuhkan kalkulator untuk memudahkan perhitungan stoikiometri  
            - mengetahui mengenai titrasi
            - ingin belajar standardisasi dalam titrasi 
         
            Share web ini jika menarik dan bermanfaat bagi Anda 👍
            """)
        
    st.write("---")
    st.header("Our crew")
    image3 = Image.open ('images/gambar3.png')
    st.image(image3)
    
if (page =='CONTACT US'):
    st.header(":mailbox: Get In Touch With Us!")
    
    contact_form =""""
     <form action="https://formsubmit.co/permatasaripani@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder= "your name" required>
     <input type="email" name="email" placeholder= "email" required>
     <textarea name="message" placeholder="your massage here"></textarea>
     <button type="submit">Send</button>
    </form>
    """
    
    st.markdown(contact_form, unsafe_allow_html=True )
    
    def local_css(file_name):
        with open (file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html= True)
            
    local_css ("style/style.css.txt")
        
if (page =='PERHITUNGAN STOIKIOMETRI'):
    st.title ('perhitungan stoikiometri')
    
    page = st.selectbox ('pilih perhitungan stoikiometri yang diinginkan',['PERHITUNGAN MOL','PERHITUNGAN Vstp','PERHITUNGAN Vrtp','PERHITUNGAN MOLARITAS','PERHITUNGAN NORMALITAS'])
    st.write("---")
    
    if (page == 'PERHITUNGAN MOL'):
        st.subheader (':blue[perhitungan mol]')
        massa = st.number_input ("masukan nilai massa")
        bm = st.number_input ("masukan nilai bm")
        hitung = st.button ("hitung mol")
        
        if hitung:
            mol = massa / bm
            st.write ("nilai mol adalah = ", (mol))

    if (page =='PERHITUNGAN Vstp'):
        st.subheader (':blue[perhitungan Vstp]')
        n = st.number_input ("masukan nilai n")
        atm = st.number_input ("masukan nilai atm(diasuksikan bahwa atm=22,4)")
        hitung = st.button ("hitung Vstp")
    
        if hitung:
            Vstp = n * atm
            st.write ("nilai Vstp adalah =", (Vstp))
                          
    if (page =='PERHITUNGAN Vrtp'):
        st.subheader (':blue[perhitungan Vrtp]')
        n = st.number_input ("masukan nilai n")
        atm = st.number_input ("masukan nilai atm(diasuksikan bahwa atm=22)")
        hitung = st.button ("hitung Vstp")
    
        if hitung:
            Vstp = n * atm
            st.write ("nilai Vstp adalah =", (Vstp))
        
    if (page =='PERHITUNGAN MOLARITAS'):
        st.subheader (':blue[perhitungan molaritas]')
        st.write ('jika berbeda satuan, user bisa mengkonversi satuan terlebih dahulu, jika satuan dalam l silahkan konversi dengan mengkalikan nilai volume sebanyak 1000, jika massa dalam g silahkan konversi dengan mengkalikan nilai massa dengan 1000')
        massa = st.number_input ("masukan nilai massa dalam mg")
        BM = st.number_input ("masukan nilai BM dalam mg/mmol")
        volume = st.number_input ("masukan nilai volume dalam ml")
        hitung =st.button ("hitung molaritas")
    
        if hitung:
            molaritas = massa / (BM * volume)
            st.write ("nilai molaritas adalah =",(molaritas))
        
    if (page =='PERHITUNGAN NORMALITAS'):
        st.subheader (':blue[perhitungan normalitas]')
        st.write ('jika berbeda satuan, user bisa mengkonversi satuan terlebih dahulu, jika satuan dalam l silahkan konversi dengan mengkalikan nilai volume sebanyak 1000, jika massa dalam g silahkan konversi dengan mengkalikan nilai massa dengan 1000')
        massa = st.number_input ("masukan nilai massa dalam mg")
        BE = st.number_input ("masukan nilai BE dalam mg/mgrek (BE didapatkan dari BM dibagi dengan n)")
        volume = st.number_input ("masukan nilai volume dalam ml")
        hitung = st.button ("hitung normalitas")
    
        if hitung:
            normalitas = massa / (BE * volume)
            st.write ("nilai normalitas adalah =",(normalitas))

if (page =='HUBUNGAN PERSEN B/B DAN B/V'):
    tab1,tab2 = st.tabs (['B/B DAN B/V','HUBUNGAN PERSEN DENGAN PPM'])
    
    with tab1:
        st.title ('hubungan persen b/b dan b/v')
        bobot = st.number_input ("masukan nilai bobot")
        bobot2 = st.number_input ("masukan nilai bobot (bobot 2 adalah 100 gram)")
        bj = st.number_input ("masukan nilai bj")
        hitung = st.button ("hitung b/v")
        
        if hitung:
            berat_per_volume = (bobot * bj * 100) / bobot2
            st.write ("nilai berat_per_berat adalah=", (berat_per_volume))  
        
    with tab2:
        st.title ('hubungan persen dengan ppm')
        persen = st.number_input ("masukan nilai b/v atau b/b", 0)
        hitung = st.button ("hitung ppm")
        
        if hitung:
            nilai_ppm = persen * 10000
            st.write ("nilai ppm adalah =", (nilai_ppm))
            
if (page =='PENGENCERAN DALAM TITRIMETRI'):
    tab1,tab2 = st.tabs (['perhitungan pengenceran pada titrimetri','about titrasi'])
    
    with tab1:
        st.title ('cara pengenceran pada titrimetri')
        
        selected = st.selectbox ('pilih perhitungan titrimetri yang diinginkan',['perhitungan pengenceran','perhitungan normalitas dalam titrimetri','perhitungan molaritas dalam titrimetri'])
        st.write("---")
        
        if (selected =='perhitungan pengenceran'):
            st.subheader (':blue[perhitungan pengenceran]')
            volume1 = st.number_input ('masukan nilai volume1')
            konsentrasi1 = st.number_input ('masukan nilai konsentrasi1')
            st.write ('nilai konsentrasi dapat di ganti dengan normalitas dan molaritas')
            konsentrasi2 = st.number_input ('masukan nilai konsentrasi')
            st.write ('nilai konsentrasi dapat di ganti dengan nilai volume')
            hitung = st.button ('hitung pengenceran')
            
            if hitung:
                pengenceran = (volume1 * konsentrasi1)/konsentrasi2 
                st.write ('nilai pengenceran adalah =',(pengenceran))
                
        if (selected =='perhitungan normalitas dalam titrimetri'):
            st.subheader (':blue[perhitungan normalitas]')
            st.write ('jika berbeda satuan, user bisa mengkonversi satuan terlebih dahulu, jika satuan dalam l silahkan konversi dengan mengkalikan nilai volume sebanyak 1000, jika massa dalam g silahkan konversi dengan mengkalikan nilai massa dengan 1000')
            massa = st.number_input ("masukan nilai massa dalam mg")
            BE = st.number_input ("masukan nilai BE dalam mg/mgrek (BE didapatkan dari BM dibagi dengan n)")
            volume = st.number_input ("masukan nilai volume dalam ml")
            FP = st.number_input ("masukan nilai FP", 0)
            hitung = st.button ("hitung normalitas")
            
            if hitung:
                normalitas = massa / (BE * volume * FP)
                st.write ("nilai normalitas adalah =",(normalitas))
                
        if (selected =='perhitungan molaritas dalam titrimetri'):
            st.subheader (':blue[perhitungan molaritas]')
            st.write ('jika berbeda satuan, user bisa mengkonversi satuan terlebih dahulu, jika satuan dalam l silahkan konversi dengan mengkalikan nilai volume sebanyak 1000, jika massa dalam g silahkan konversi dengan mengkalikan nilai massa dengan 1000')
            massa = st.number_input ("masukan nilai massa dalam mg")
            BM = st.number_input ("masukan nilai BM dalam mg/mmol")
            volume = st.number_input ("masukan nilai volume dalam ml")
            FP = st.number_input ("masukan nilai FP", 0)
            hitung = st.button ("hitung normalitas")
            
            if hitung:
                normalitas = massa / (BM * volume * FP)
                st.write ("nilai normalitas adalah =",(normalitas))
        st.write("---")
            
        page = st.radio ('silahkan pilih titrasi yang ingin dilakukan',['standardisasi HCL','standardisasi NaOH','standardisasi KMnO4','standardisasi TioSulfat','standardisasi EDTA'])
        
        if (page =='standardisasi HCL'):
            st.subheader (':blue[cara standardisasi HCL]')
            
            st.write ('''
                  1. setelah menghitung berapa volume pengenceran yang dibuat, lakukan lah pengenceran dengan HCL pekat 
                  2. masukan volume yang di dapat dari hasil pengenceran kedalam gelas piala atau labu takar
                  3. masukan sedikit aquadest terlebih dahulu sebelum memasukan HCL pekat kedalam gelas piala atau labu takar
                  4. setelah itu encerkan HCL pekat menggunakan aquadest sampai ke batas volume1
                  5. kemudian aduk dengan batang pengaduk
                  6. setelah pengenceran dilakukan, masukan HCL yang sudah diencerkan kedalam buret
                  
                  untuk melakukan standardisasi HCL 
                  
                  1. timbang boraks sebanyak 1500 mg menggunakan kaca arloji
                  2. larutkan menggunakan aquadest kedalam labu takar 100 mL
                  3. pipet larutan boraks sebanyak 25 mL menggunakan pipet volumetri 
                  4. masukan kedalam erlenmeyer
                  5. tambahkan indikator MM sebanyak 2 tetes kedalam erlenmeyer
                  6. titrasi menggunakan larutan HCL
                  7. perubahan warna yang akan terjadi adalah dari warna kuning menjadi merah jingga
                  ''')
        
        if (page =='standardisasi NaOH'):
            st.subheader (':blue[cara standardisasi NaOH]')
            st.write ('''
                  1. setelah menghitung berapa volume pengenceran yang dibuat, lakukan lah pengenceran dengan NaOH pekat 
                  2. masukan volume yang di dapat dari hasil pengenceran kedalam gelas piala atau labu takar
                  3. masukan sedikit aquadest terlebih dahulu sebelum memasukan NaOH pekat kedalam gelas piala atau labu takar
                  4. setelah itu encerkan NaOH pekat menggunakan aquadest sampai ke batas volume1
                  5. aduk dengan batang pengaduk
                  6. setelah pengenceran dilakukan, masukan NaOH yang sudah diencerkan kedalam buret
                  
                  untuk melakukan standardisasi NaOH 
                  
                  1. timbang asam oksalat sebanyak 630 mg menggunakan kaca arloji
                  2. larutkan menggunakan aquadest kedalam labu takar 100 mL
                  3. pipet larutan asam oksalat sebanyak 25 mL menggunakan pipet volumetri 
                  4. masukan kedalam erlenmeyer
                  5. tambahkan indikator PP sebanyak 1 tetes kedalam erlenmeyer
                  6. titrasi menggunakan larutan NaOH
                  7. perubahan warna yang akan terjadi adalah dari tidak berwarna menjadi merah muda
                  ''')
        
        if (page =='standardisasi KMnO4'):
            st.subheader (':blue[cara standardisasi KMnO4]')
            st.write ('''
                  1. setelah menghitung berapa volume pengenceran yang dibuat, lakukan lah pengenceran dengan KMnO4 pekat 
                  2. masukan volume yang di dapat dari hasil pengenceran kedalam gelas piala atau labu takar
                  3. setelah itu encerkan KMnO4 pekat menggunakan aquadest sampai ke batas volume1
                  4. aduk menggunakan batang pengaduk agar homogen
                  5. setelah pengenceran dilakukan, masukan KMnO4 yang sudah diencerkan kedalam buret
                  
                  untuk melakukan standardisasi KMnO4
                  
                  1. timbang asam oksalat sebanyak 630 mg menggunakan kaca arloji
                  2. larutkan menggunakan aquadest kedalam labu takar 100 mL
                  3. pipet larutan asam oksalat sebanyak 25 mL menggunakan pipet volumetri 
                  4. masukan kedalam erlenmeyer
                  5. tambahkan 25 mL asam sulfat (H₂SO₄) 4N kedalam erlenmeyer
                  6. panaskan erlenmeyer sampai tidak bisa dipegang dengan tangan langsung (70°C)
                  7. titrasi menggunakan larutan KMnO4
                  8. titrasi dilakukan dengan memegang leher erlenmeryer menggunakan lap atau serbet
                  9. perubahan warna yang akan terjadi adalah dari tidak berwarna menjadi merah muda 
                  ''')
      
        if (page =='standardisasi TioSulfat'):
            st.subheader (':blue[cara standardisasi TioSulfat]')
            st.write ('''
                  1. setelah menghitung berapa volume pengenceran yang dibuat, lakukan lah pengenceran dengan TioSulfat pekat 
                  2. masukan volume yang di dapat dari hasil pengenceran kedalam gelas piala atau labu takar
                  3. setelah itu encerkan TioSulfat pekat menggunakan aquadest sampai ke batas volume1
                  4. aduk menggunakan batang pengaduk agar homogen
                  5. setelah pengenceran dilakukan, masukan TioSulfat yang sudah diencerkan kedalam buret
                  
                  untuk melakukan standardisasi TioSulfat
                  
                  1. timbang K₂Cr₂O₇ sebanyak 500 mg menggunakan kaca arloji
                  2. larutkan menggunakan aquadest kedalam labu takar 100 mL
                  3. pipet larutan kalium dikromat (K₂Cr₂O₇) sebanyak 25 mL menggunakan pipet volumetri 
                  4. masukan kedalam erlenmeyer
                  5. tambahkan 7,5/10 mL KI 20% dan HCL 4N 25 mL kedalam erlenmeyer
                  6. setelah mendekati titik akhir titrasi (warna kuning kehijauan) tambahkan 1 drop kanji 
                  7. titrasi kembali menggunakan larutan TioSulfat
                  8. perubahan warna yang akan terjadi adalah dari warna biru tua menjadi hijau muda 
                  ''')
        
        if (page =='standardisasi EDTA'):
            st.subheader (':blue[cara standardisasi EDTA]')
            st.write ('''
                  1. setelah menghitung berapa volume pengenceran yang dibuat, lakukan lah pengenceran dengan EDTA pekat 
                  2. masukan volume yang di dapat dari hasil pengenceran kedalam gelas piala atau labu takar
                  3. setelah itu encerkan EDTA pekat menggunakan aquadest sampai ke batas volume1
                  4. aduk menggunakan batang pengaduk agar homogen
                  5. setelah pengenceran dilakukan, masukan EDTA yang sudah diencerkan kedalam buret
                  
                  untuk melakukan standardisasi EDTA 
                  
                  1. timbang CaCO₃ sebanyak 100 mg menggunakan gelas piala kecil
                  2. larutkan menggunakan HCL 4N 
                  3. masukan kedalam labu takar 100 mL
                  4. larutkan dengan aqudest 
                  5. pipet larutan kalsium karbonat (CaCO₃) sebanyak 25 mL menggunakan pipet volumetri 
                  6. masukan kedalam erlenmeyer
                  7. tambahkan 10 mL larutan buffer pH 10, 1 mL Mg-EDTA kedalam erlenmeyer
                  8. tutup erlenmeyer dengan kaca arloji
                  9. masukan indikator erio-T 
                  10. titrasi menggunakan larutan EDTA
                  11. perubahan warna yang akan terjadi adalah dari warna merah anggur menjadi biru.
                  ''')
        
    with tab2:
        st.title (':blue[about titrasi]')
        
        st.write ('''
                  analisis titrimetri adalah analisis berdasarkan pengukuran volume larutan yang sudah diketahui konsentrasinya, 
                  untuk menentukan zat atau larutan yang belum diketahui konsentrasinya. 
                  titrasi adalah proses pengukuran volume suatu larutan yang dibutuhkan untuk bereaksi sempurna dengan suatu pereaksi lain.
                  larutan standar baku adalah larutan yang sudah diketahui konsentrasinya (titran).
                  sedangkan larutan yang tidak diketahui konsentrasinya disebut dengan titrat. 
                  
                  titrimetri secara kuantitatif dibagi menjadi 4, yaitu;
                  1. titrasi asidimetri-alkalimetri
                  2. titrasi redoks
                  3. titrasi argentometri
                  4. titrasi kompleksometri 
                  ''')
        
        image5 = Image.open ('images/gambar5.png')
        st.image (image5)
        
        st.write ('''1. titrasi asidimetri dan alkalimetri
                  titrasi asidimetri-alkalimetri ini disebut juga sebagai titrasi asam-basa
                  asidimetri merupakan titrasi terhadap larutan basa bebas atau larutan garam 
                  terhidrolisis (yang berasal dari asam lemah) dengan larutan standar asam kuat, atau dapat 
                  diartikan sebagai proses penentuan konsentrasi basa dengan menggunakan larutan asam sebagai standar.
                  alkalimetri merupakan titrasi terhadap larutan asam bebas atau larutan garam 
                  terhidrolisi (yang berasal dari basa lemah) dengan larutan standar basa kuat, atau 
                  penentuan konsentrasi larutan asam dengan menggunakan larutan basa.
                  konsep yang digunakan dalam titrasi ini merupakan reaksi asam-basa arrhenius, 
                  dimana suatu zat disebut asam bila zat itu menghasilkan ion H+ dalam air  
                  dan suatu zat disebut basa bila dilarutkan dengan air menghasilkan ion OH-.
                  asidimetri merupakan titrasi dengan titran (yang berada di buret) 
                  yaitu asam kuat ataupun asam lemah terhadap suatu basa
                  alkalimetri merupakan titrasi dengan titran (yang berada di buret) 
                  yaitu basa kuat atau basa lemah terhadap suatu asam.''')
                  
        st.write ('''
                  dalam titrasi asam-basa diperlukan suatu indikator yaitu;
                  1. Metil jingga atau sindur metil adalah indikator pH yang sering digunakan pada titrasi
                  karena perubahan warna nya yang kontras, hal ini karena ia akan berubah dengan adanya kelebihan sedikti asam,
                  maka dapat digunakan dalam titrasi asam, Tidak seperti indikator universal, metil jingga tidak memiliki spektrum
                  perubahan warna yang lengkap, tetapi memiliki titik akhir yang lebih tajam. Dalam larutan yang basa, 
                  metil jingga berubah dari merah menjadi jingga dan akhirnya menjadi kuning, dan sebaliknya jika keasaman larutan bertambah perubahan
                  warna akan berubah dari kuning ke jingga dan berakhir ke warna merah.
                  metil jingga dalam kondisi asam berwarna merah, dan dalam kondisi basa berwarna kuning. 
                  Metil jingga memiliki pHa 3,47 dalam air pada 25 °C (77 °F).
                  2.  indikator MM 
                  Metil merah (2-(N,N-dimethyl-4-aminophenyl) azobenzenecarboxylic acid), 
                  disebut juga C.I. Acid Red 2 adalah indikator warna yang berubah menjadi merah dalam larutan asam,
                  Ini merupakan zat warna azo, dan berbentuk bubuk kristal berwarna merah gelap. 
                  Metil merah adalah indikator pH; berwarna merah pada pH di bawah 4,4; kuning pada pH 6,2; 
                  dan jingga pada pH di antaranya. Memiliki pKa 5,1.[2]
                  3.  indikator BTB 
                  Bromotimol biru (juga dikenal sebagai Bromotimol sulfonftalein dan BTB) 
                  adalah suatu indikator pH, Senyawa ini banyak digunakan dalam aplikasi yang memerlukan pengukuran
                  zat yang memiliki pH relatif netral (dekat 7). 
                  Senyawa ini umum digunakan untuk mengukur kehadiran asam karbonat dalam cairan. 
                  Senyawa ini biasanya dijual dalam bentuk padatan seperti garam natrium pada indikator asam.
                  4.  indikator PP
                  Fenolftalein adalah pewarna yang berperan sebagai indikator pH. Fenolftalein adalah senyawa kimia 
                  dengan rumus molekul C20H14O4 dan sering ditulis sebagai "HIn" atau "pp" dalam notasi singkat. 
                  Fenolftalein sering digunakan sebagai indikator dalam titrasi asam-basa. 
                  Untuk aplikasi ini, ia berubah warna dari tak berwarna dalam larutan asam menjadi merah muda dalam larutan basa
                  Fenolftalein biasanya digunakan sebagai indikator keadaan suatu zat yang bersifat lebih asam atau lebih basa.
                  Prinsip perubahan warna ini digunakan dalam metode titrasi. Fenolftalein cocok untuk digunakan sebagai indikator untuk proses titrasi HCl dan NaOH. 
                  Fenolftalein tidak akan berwarna (bening) dalam keadaan zat yang asam atau netral, 
                  namun akan berwarna kemerahan dalam keadaan zat yang basa. Tepatnya pada titik pH di bawah 8,3 fenolftalein tidak berwarna, 
                  namun jika mulai melewati 8,3 maka warna merah muda yang semakin kemerahan akan muncul. 
                  Semakin basa maka warna yang ditimbulkan akan semakin merah.Fenolftalein juga merupakan salah satu komponen indikator universal, 
                  bersama dengan metil merah, bromotimol biru, dan timol biru.
                  ''')
        st.write("---")
        st.write ('''2. titrasi redoks
                Titrasi redoks merupakan metode analisa reaksi reduksi dan oksidasi yang terjadi antara titran (zat yang konsentrasinya sudah diketahui) 
                dan titrat (zat yang konsentrasinya akan diungkap melalui titrasi). Titrasi redoks merupakan kependekan dari titrasi reduksi dan oksidasi. 
                Reduksi adalah proses pengambilan elektron dalam sebuah atom, ion, maupun molekul. Sebaliknya, oksidasi adalah proses pembebasan elektron dari sebuah atom, ion, atau molekul. 
                Faktanya, oksidasi selalu dilanjutkan dengan reduksi, sehingga terjadilah reaksi redoks. 
                Dalam reaksi redoks, jumlah elektron yang dibebaskan selalu sama dengan jumlah elektron yang diambil. Bila dibandingkan dengan reaksi asam basa, 
                konsepnya cukup mirip di mana jumlah proton yang dibebaskan oleh asam selalu sama dengan jumlah proton yang diambil oleh basa. 
                Titrasi redoks terjadi saat ada perpindahan elektron di antara titran dan titrat. Karena reaksi redoks umumnya terjadi di dalam air, 
                maka diperlukan penyetaraan koefisien terhadap reaksi air menggunakan H+ atau OH-.
                  ''')
        
        st.write ('''
                  titrasi redoks juga dibagi dalam beberapa jenis berdasarkan sifat larutan bakunya, yaitu:
                  1. Permanganometri
                  Sesuai namanya, jenis titrasi redoks ini menggunakan kalium permanganat (KMnO4) sebagai titran dan oksidator. 
                  Untuk permanganometri, Anda bisa menggunakan asam seperti H2SO4 yang encer atau HClO4 namun Cl- berpotensi teroksidasi dan kestabilannya pun terbatas. 
                  Bila menggunakan larutan tidak berwarna, titrasi permanganometri tidak membutuhkan indikator karena setetes 0,1 N permanganat menunjukkan warna pink keunguan dalam 100 ml larutan.
                  2. Dikromatometri
                  Dikromatometri menggunakan dikromat (Cr₂O₇) yang merupakan oksidator yang kuat, namun masih berada di bawah permanganat. 
                  Dalam prosesnya, ion dikromat kemudian tereduksi menjadi Cr3+ yang memiliki warna hijau. Dikromat dipilih karena kestabilan yang baik dan bentuknya yang murni. 
                  Sayangnya, dikromat memiliki reaksi yang cukup lambat.
                  3. Iodometri dan iodimetri
                  Titrasi Iodometri dan iodimetri merupakan titrasi redoks yang menggunakan iodium. 
                  Iodometri adalah titrasi tidak langsung yang menggunakan iodium sebagai reduktor, di mana iodium yang dilepas akan dititrasi menggunakan larutan tiosulfat. 
                  Sementara itu, iodimetri adalah titrasi langsung yang dilakukan dalam kondisi pH netral atau sedikit asam, di mana iodium digunakan sebagai oksidator.
                  4. Bromatometri
                  Bromatometri menggunakan potasium bromat (KBrO3) sebagai reduktor dan titran. Untuk mempercepat terjadinya reaksi, biasanya bromatometri dilakukan dalam suhu yang panas dan kondisi pH asam. 
                  Kelebihan KBr akan memunculkan reaksi pada ion bromat yang kemudian menghasilkan warna kuning pucat yang sulit untuk ditetapkan sebagai titik akhir.
                    ''')
        st.write("---")
        
        st.write ('''3. titrasi argentometri 
                  Titrasi Argentometri merupakan titrasi pengendapan. Titrasi pengendapan merupakan reaksi titran dengan titrat membentuk endapan yang sukar larut 
                  seperti misalnya ion klorida dititrasi dengan larutan perak nitrat (AgNO3) membentuk endapan perak klorida (AgCl) berwarna putih.
                  metode titrasi yang satu ini berpatokan pada pembentukan endapan. Dengan kata lain, kadar zat analit (zat yang diuji kadar atau konsentrasinya) 
                  ditentukan oleh pembentukan endapan dari titran (larutan yang dipakai sebagai tolok ukur pengukuran dengan titrasi) larutan titer perak nitrat.
                  ''')
        
        st.write ('''
                  Dalam titrasi argentometri, ada tiga jenis metode yang digunakan;
                  1. metode fayans
                  Metode titrasi argentometri yang satu ini pertama kali dikenalkan oleh Kazimierz Fajans. 
                  Dalam metode ini, dichlorofluorescein akan digunakan sebagai indikator. 
                  Indikator ini akan berubah warna untuk memberitahu Anda informasi kadar. 
                  Jika proses sudah mencapai titik akhir, suspensi yang awalnya berwarna hijau akan berubah warna menjadi merah muda.
                  Biasanya, sebelum proses titrasi selesai, ion klorida masih berlebih jumlahnya. 
                  Kemudian, hal yang terjadi adalah ion klorida ini akan diabsorpsi ke permukaan perak klorit. 
                  Proses adsorpsi ion inilah yang akan mempengaruhi warna di indikator nanti.
                  2. metode mohr 
                  Metode berikutnya adalah metode Mohr. Metode titrasi yang satu ini dikenalkan dan dinamai dari nama Karl Friedrich Mohr. 
                  Dalam proses metode titrasi Mohr ini, indikator yang digunakan sudah pasti berbeda dengan Metode Fajans tadi. 
                  Di sini, kalium kromat digunakan sebagai indikator. Jika semua ion klorida bereaksi, nantinya akan dihasilkan kromat perak merah.
                  Sebaiknya tidak menguji atau memeriksa kadar zat karbonat dan fosfat menggunakan metode ini karena keduanya akan mengendap dengan perak. 
                  Hasilnya juga nanti tidak begitu akurat. Metode ini terutama dapat dipakai untuk memeriksa kandungan klorin. Anda bisa melakukannya dengan menggunakan sampel lain seperti kalsium dan besi asetat.
                  3. metode volhard 
                  Jacob Volhard adalah orang dibalik metode titrasi yang satu ini. Dalam metodenya, Volhard juga menambahkan kelebihan dari perak nitrat ini ke analit. 
                  Lalu, perak klorida akan disaring sehingga perak nitrat yang tersisa bisa dititrasi terhadap larutan yang hendak diperiksa kadar zatnya.
                  Untuk indikatornya, metode Volhard menggunakan besi amonium sulfat. Di hasil akhir proses titrasi, indikator ini akan berubah warna menjadi warna merah darah. 
                  Selain itu, indikator seperti larutan garam ferri (Fe3+) juga bisa Anda gunakan sebagai indikator alternatif saat melakukan metode ini.
                  ''')
        st.write("---")
        
        st.write ('''4. titrasi kompleksometri 
                  Titrasi kompleksometri yaitu titrasi berdasarkan pembentukan persenyawaan kompleks (ion kompleks atau garam yang sukar mengion). 
                  Kompleksometri merupakan jenis titrasi dimana titran dan titrat saling mengkompleks, membentuk hasil berupa kompleks. 
                  reaksi–reaksi pembentukan kompleks atau yang menyangkut kompleks banyak sekali dan penerapannya juga banyak, tidak hanya dalam titrasi.
                  Titrasi kompleksometri juga dikenal sebagai reaksi pembentukan molekul netral yang terdisosiasi dalam larutan. Persyaratan mendasar terbentuknya kompleks demikian adalah tingkat kelarutan tinggi. 
                  Selain titrasi kompleks biasa seperti di atas, dikenal pula kompleksometri yang dikenal sebagai titrasi kelatometri, seperti yang menyangkut penggunaan EDTA. Gugus-yang terikat pada ion pusat, disebut ligan.          
                  Kompleksometri merupakan metoda titrasi yang pada reaksinya terjadi pembentukan larutan atau senyawa kompleks dengan kata lain membentuk hash berupa kompleks. Untuk dapat dipakai sebagai dasar suatu titrasi, reaksi pembentukan kompleks disamping harus memenuhi persyaratan umum amok titrasi, maka kompleks yang terjadi harus stabil. 
                  Titrasi ini biasanya digunakan untuk penetapan kadar logam polivalen .
                  Selektivitas kompleks dapat diatur dengan pengendalian pH, missal Mg, Ca, Cr, dan Ba dapat dititrasi pada pH = 11 EDTA. Sebagian besar titrasi kompleksometri mempergunakan indikator yang juga bertindak sebagai pengompleks dan tentu saja kompleks logamnya mempunyai warna yang berbeda dengan pengompleksnya sendiri. 
                  Indikator demikian disebut indikator metalokromat, contohnya : Eriochrome black T dan Asam salisilat.
                  Penentuan Ca dan Mg dapat dilakukan dengan titrasi EDTA, pH untuk titrasi adalah 10 dengan indikator Eriochrome black T. pada pH tinggi, 12, Mg(OH)2 akan mengendap, sehingga EDTA dapat dikonsumsi hanya oleh Ca2+ dengan indicator murexide 
                  ''')
        st.write("---")
        