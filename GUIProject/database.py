import sqlite3

def create_databases():
    con = sqlite3.connect("Users.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTs Users(username TEXT NOT NULL,password TEXT NOT NULL,favs TEXT, favsMovies TEXT);")
    cur.execute("SELECT * FROM Users")
    # print(cur.fetchall())
    con.commit()
    con.close()

    con = sqlite3.connect("Movies.db")
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTs Movies(
            mid   INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            category TEXT,
            subject TEXT,
            release INTEGER,
            imdb_rate TEXT
        );
        """)
    con.commit()
    con.close()

    con = sqlite3.connect("Movies.db")
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTs MoviesTr(
            mid   INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            category TEXT,
            subject TEXT,
            release INTEGER,
            imdb_rate TEXT
        );
        """)
    con.commit()
    con.close()

    con = sqlite3.connect("Series.db")
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTs Series(
        mid   INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        category TEXT,
        subject TEXT,
        release INTEGER,
        imdb_rate TEXT
    );
    """)
    con.commit()
    con.close()

    con = sqlite3.connect("Series.db")
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTs SeriesTr(
        mid   INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        category TEXT,
        subject TEXT,
        release INTEGER,
        imdb_rate TEXT
    );
    """)
    con.commit()
    con.close()

def fill_databases():
    # Movies

    con = sqlite3.connect("Movies.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Movies")

    result = cur.fetchall()

    if not result:

        movieData = [('Joker',
                      'Crime',
                      """In Gotham City, mentally troubled comedian Arthur Fleck is disregarded and mistreated by society. He then embarks on a downward spiral of revolution and bloody crime. This path brings him face-to-face with his alter-ego: the Joker.""",
                      2019,
                      "8.5"),
                     ('Toy Story 3',
                      'Animation',
                      """The toys are mistakenly delivered to a day-care center instead of the attic right before Andy leaves for college, and it's up to Woody to convince the other toys that they weren't abandoned and to return home.""",
                      2010,
                      "8.3"),
                     ('Avengers: Endgame',
                      'Action',
                      """After the devastating events of Avengers: Infinity War (2018), the universe is in ruins. With the help of remaining allies, the Avengers assemble once more in order to reverse Thanos' actions and restore balance to the universe.""",
                      2019,
                      "8.4"),
                     ('Venom',
                      'Action',
                      """A failed reporter is bonded to an alien entity, one of many symbiotes who have invaded Earth. But the being takes a liking to Earth and decides to protect it.""",
                      2018,
                      "6.7"),
                     ('The Giver',
                      'Drama',
                      """In a seemingly perfect community, without war, pain, suffering, differences or choice, a young boy is chosen to learn from an elderly man about the true pain and pleasure of the "real" world.""",
                      2014,
                      "6.5"),
                     ('The Invisible Guest',
                      'Mystery ',
                      """A successful entrepreneur accused of murder and a witness preparation expert have less than three hours to come up with an impregnable defense.""",
                      2016,
                      "8.1"),
                     ('Up',
                      'Animation',
                      """78-year-old Carl Fredricksen travels to Paradise Falls in his house equipped with balloons, inadvertently taking a young stowaway.""",
                      2009,
                      "8.2"),
                     ('Interstellar',
                      'Sci-Fi',
                      """A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.""",
                      2014,
                      "8.6")
                     ]

        for x in movieData:
            cur.execute("INSERT INTO Movies(name, category, subject, release, imdb_rate) VALUES (?, ?, ?, ?, ?)", [x[0], x[1], x[2], x[3], x[4]])

    con.commit()
    con.close()


    # Series


    con = sqlite3.connect("Series.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Series")

    result = cur.fetchall()

    if not result:

        seriesData = [('Brooklyn Nine-Nine ',
                      'Comedy',
                      """'Brooklyn Nine-Nine' follows the exploits of hilarious Det. Jake Peralta and his diverse, lovable colleagues as they police the NYPD's 99th Precinct.""",
                      2013,
                      "8.4"),
                     ('Stranger Things ',
                      'Drama',
                      """When a young boy disappears, his mother, a police chief and his friends must confront terrifying supernatural forces in order to get him back.""",
                      2016,
                      "8.7"),
                     ('Mr. Robot ',
                      'Crime',
                      """Elliot, a brilliant but highly unstable young cyber-security engineer and vigilante hacker, becomes a key figure in a complex game of global dominance when he and his shadowy allies try to take down the corrupt corporation he works for.""",
                      2015,
                      "8.6"),
                     ('The Walking Dead',
                      'Horror',
                      """Sheriff Deputy Rick Grimes wakes up from a coma to learn the world is in ruins and must lead a group of survivors to stay alive.""",
                      2010,
                      "8.2"),
                     ('Wayward Pines',
                      'Mystery',
                      """A Secret Service agent goes to Wayward Pines, Idaho, in search of two federal agents who have gone missing in the bucolic town. He soon learns that he may never get out of Wayward Pines alive.""",
                      2015,
                      "7.4"),
                     ('Flashforward',
                      'Sci-Fi',
                      """A special task force in the FBI investigates after every person on Earth simultaneously blacks out and awakens with a short vision of their future.""",
                      2009,
                      "7.6"),
                     ('How I Met Your Mother',
                      'Comedy',
                      """A father recounts to his children - through a series of flashbacks - the journey he and his four best friends took leading up to him meeting their mother.""",
                      2005,
                      "8.3"),
                     ('Prison Break',
                      'Crime',
                      """Due to a political conspiracy, an innocent man is sent to death row and his only hope is his brother, who makes it his mission to deliberately get himself sent to the same prison in order to break the both of them out, from the inside.""",
                      2005,
                      "8.3")
                     ]

        for x in seriesData:
            cur.execute("INSERT INTO Series(name, category, subject, release, imdb_rate) VALUES (?, ?, ?, ?, ?)",
                        [x[0], x[1], x[2], x[3], x[4]])

    con.commit()
    con.close()


def fill_databasesTr():
    # Movies

    con = sqlite3.connect("Movies.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM MoviesTr")

    result = cur.fetchall()

    if not result:

        movieData = [('Joker',
                      'Polisiye',
                      """Joker, ba??ar??s??z bir komedyen olan Arthur Fleck'in hayat??na odaklan??yor. Toplum taraf??ndan d????lanan bir adam olan Arthur zamanla kendi kimli??inden uzakla????p Joker karakterine b??r??n??r.""",
                      2019,
                      "8.5"),
                     ('Oyuncak Hikayesi 3',
                      'Animasyon',
                      """Woody ve Buzz, sahipleri Andy'nin g??n??n birinde b??y??yece??ini kabullenmi?? durumdad??r. Peki o g??n gelip ??att??????nda ne yapacaklard??r? Serinin ??????nc?? b??l??m??nde Andy, ??niversiteye gitmeye haz??rlanmakta, sad??k oyuncaklar?? ise belirsiz gelecekleri y??z??nden endi??e i??indedir.""",
                      2010,
                      "8.3"),
                     ('Avengers: Endgame',
                      'Aksiyon',
                      """Thanos'un Sonsuzluk Eldiveni'ni ele ge??irmesi ve kendi D??nya dengesini kurmas?? nedeniyle s??perkahramanlar dahil d??nyan??n yar??s?? k??le d??n????m????t??. Geriye kalan ve yas tutan Yenilmezler'in as kadrosu kuantum b??lgesinden gelerek aralar??na kat??lan Ant-Man umut ?????????? olacak.""",
                      2019,
                      "8.4"),
                     ('Venom',
                      'Aksiyon',
                      """H??rsl?? bir muhabir olan Eddie Brock'un hikayesini konu alan Venom filmi, Gazeteci Brock'un sevgilisinin ??al????t?????? ara??t??rma ??irketinin patronunun pe??ine d????mesiyle ba??l??yor. ... Bunun ??zerine ara??t??rmalar??n?? daha da derile??tiren Eddie, ??irketin bu uzayl?? varl?????? insan deneklerle birle??tirmeye ??al????t??????n?? ke??feder.""",
                      2018,
                      "6.7"),
                     ('Se??ilmi?? ki??i',
                      'Drama',
                      """D??nyan??n d??zeni ya??anan bir koas sonras?? tamamen de??i??mi??tir. Uygarl??k tarihi ile tamamen ba??lar?? kopart??lm???? yeni nesiller yeti??tirmek i??in, "Ya??l??lar" ad?? verilen bir grup yery??z??ndeki renk, din, d??????nce gibi farkl??l?????? tan??mlayacak t??m s??fatlar?? ortadan kald??r??rlar. Art??k d??nya sadece siyah ve beyazd??r; d??md??z, denizler, da??lar, engeller yoktur. Sadece g??ne??in a??t?????? tek tip iklim vard??r. ??nsanlar??n aile bireyleri d??????nda birbirlerine dokunmalar??, yalan s??ylemeleri, dili yanl???? kullanmalar?? ve s??n??rlar d??????na ????kmalar?? yasakt??r. Dahas?? hi?? kimsenin duygular??, hissiyatlar?? ve an??lar?? yoktur. B??yle bir d??zen i??erisinde ergenli??ini tamamlay??p, ya????tlar?? gibi hayatta kendisine verilecek g??revi bekleyen Jonas, ummad?????? bir s??rprizle kar????la??acakt??r... """,
                      2014,
                      "6.5"),
                     ('G??r??nmeyen Misafir',
                      'Gizem ',
                      """Bir da?? oteli odas??nda yan??nda foto??raf???? sevgilisi Laura Vidal'??n cesedi dururken polis taraf??ndan tutuklan??r. ... Adrian, Virginia'yla cinayet ve sevgilisi Laura ile ili??kisi hakk??nda konu??ur. Her ikisi de Daniel Garrido ad??nda bir adam??n ??ld?????? araba kazas??nda yer alm????t??r.""",
                      2016,
                      "8.1"),
                     ('Yukar?? Bak',
                      'Animasyon',
                      """Hayat?? boyunca ya??amak istedi??i macera hayalini ger??ekle??tirmek i??in evine binlerce balon ba??lay??p G??ney Amerika'n??n vah??i do??as??na do??ru yolculu??a ????kan 78 ya????ndaki baloncu Carl Fredricksen'??n hikayesinin anlat??ld?????? yeni bir komedi.""",
                      2009,
                      "8.2"),
                     ('Y??ld??zlararas??',
                      'Bilim-kurgu',
                      """Bir grup ka??if, bu solucan deli??inden ge??ip boyut de??i??tirerek insanl??k taraf??ndan daha ??nce ula????lamam???? noktalara ula??mak ve insanl??k i??in yeni ya??am alanlar?? ara??t??rmak niyetindedir.""",
                      2014,
                      "8.6")
                     ]

        for x in movieData:
            cur.execute("INSERT INTO MoviesTr(name, category, subject, release, imdb_rate) VALUES (?, ?, ?, ?, ?)", [x[0], x[1], x[2], x[3], x[4]])

    con.commit()
    con.close()


    # Series


    con = sqlite3.connect("Series.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM SeriesTr")

    result = cur.fetchall()

    if not result:

        seriesData = [('Brooklyn Nine-Nine ',
                      'komedi',
                      """Dizi, Brooklyn'in 99 numaral?? polis b??lgesinde yer alan bir karakolda g??rev alan bir grup dedektifin ve karakol ??al????anlar??n??n ya??ad?????? komik ve e??lenceli olaylar??, b??l??ml??k konular e??li??inde anlat??yor.""",
                      2013,
                      "8.4"),
                     ('Stranger Things ',
                      'Drama',
                      """Stranger Things, kaybolan arkada??lar??n?? aramaya ba??layan 3 ??ocu??un ve onlara yard??m eden insanlar??n hikayesini konu alan bir amerikan bilim kurgu hikayesidir. Konusu kadar ba??ar??l?? oyuncu kadrosuyla da dikkat ??eken dizide, macera ve do??a??st?? olaylar??n s??reklili??i, izleyiciyi etkisi alt??na al??yor.""",
                      2016,
                      "8.7"),
                     ('Mr. Robot ',
                      'polisiye',
                      """ Dizide Elliot, g??nd??zleri gen?? bir siber g??venlik m??hendisi ve geceleri hackerl??k yapan bir siber korsand??r. Elliot, yer alt?? hacker grubunun (fsociety) onunla irtibata ge??mek i??in ??irketininin sistemine zarar vermesi ??zerine b??y??k bir karma????kl??????n i??ine kendisini atm????t??r.""",
                      2015,
                      "8.6"),
                     ('The Walking Dead',
                      'korku',
                      """The Walking Dead, ayn?? adl?? ??izgi roman serisine dayanmaktad??r. Roman, d??nya ??ap??nda beklenmedik bir bi??imde ortaya ????kan esrarengiz bir bula????c?? beyinsel hastal??k sonucu, modern medeniyetin sonunu getiren bir zombi salg??n??n?? konu eder.""",
                      2010,
                      "8.2"),
                     ('Wayward Pines',
                      'Gizem',
                      """Dizi, Blake Crouch'??n Pines, Wayward ve The Last Town adlar??n?? ta????yan ???? kitaptan olu??an Wayward Pines serisinden uyarlanm????. ... Ard??ndan g??zlerini Wayward Pines'ta bir hastanede a????yor. Dizimiz, bunu, sonras??nda ya??anacak gizemli olaylar?? ve Ethan'??n kasabadan ka??ma ??abalar??n?? anlat??yor.""",
                      2015,
                      "7.4"),
                     ('Flashforward',
                      'Bilim-kurgu',
                      """Gizemli bir olay d??nya ??zerindeki herkesin 137 saniye boyunca bilincini kaybetmesine sebep olmu??, bu s??re??te herkes 6 ay sonras??n?? g??rm????t??r - bir k??resel "??ng??r??". Gibbons" ve 1991'de baz?? bilin?? kay??plar??n??n oldu??u Somali'yi ara??t??rmaya ba??lar.""",
                      2009,
                      "7.6"),
                     ('How I Met Your Mother',
                      'komedi',
                      """How i met your mother dizisi 2030 y??l??nda, Ted Mosby adl?? ba??rol karakterin ??ocuklar??na anneleri ile nas??l tan????t??????n?? anlatmas?? ile ba??lamaktad??r. Dizide genellikle Ted Mosby'nin ge??mi??inde arkada??lar?? ile ya??ad?????? hayat?? anlat??lmaktad??r.""",
                      2005,
                      "8.3"),
                     ('Prison Break',
                      'polisiye',
                      """Dizi genel olarak i??lemedi??i bir su??tan dolay?? idam cezas?? alm???? Lincoln Burrows (Dominic Purcell) 'u ve Lincoln'??n karde??i Michael Scofield (Wentworth Miller)'??n karde??ini kurtarmak i??in t??m yasal yollar??n t??kendi??ini fark edip onu hapishaneden ????karmak i??in bir ka?????? plan?? yapmas?? ve sonras??nda geli??en olaylar?? konu al??r.""",
                      2005,
                      "8.3")
                     ]

        for x in seriesData:
            cur.execute("INSERT INTO SeriesTr(name, category, subject, release, imdb_rate) VALUES (?, ?, ?, ?, ?)",
                        [x[0], x[1], x[2], x[3], x[4]])

    con.commit()
    con.close()
