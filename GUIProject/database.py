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
                      """Joker, başarısız bir komedyen olan Arthur Fleck'in hayatına odaklanıyor. Toplum tarafından dışlanan bir adam olan Arthur zamanla kendi kimliğinden uzaklaşıp Joker karakterine bürünür.""",
                      2019,
                      "8.5"),
                     ('Oyuncak Hikayesi 3',
                      'Animasyon',
                      """Woody ve Buzz, sahipleri Andy'nin günün birinde büyüyeceğini kabullenmiş durumdadır. Peki o gün gelip çattığında ne yapacaklardır? Serinin üçüncü bölümünde Andy, üniversiteye gitmeye hazırlanmakta, sadık oyuncakları ise belirsiz gelecekleri yüzünden endişe içindedir.""",
                      2010,
                      "8.3"),
                     ('Avengers: Endgame',
                      'Aksiyon',
                      """Thanos'un Sonsuzluk Eldiveni'ni ele geçirmesi ve kendi Dünya dengesini kurması nedeniyle süperkahramanlar dahil dünyanın yarısı küle dönüşmüştü. Geriye kalan ve yas tutan Yenilmezler'in as kadrosu kuantum bölgesinden gelerek aralarına katılan Ant-Man umut ışığı olacak.""",
                      2019,
                      "8.4"),
                     ('Venom',
                      'Aksiyon',
                      """Hırslı bir muhabir olan Eddie Brock'un hikayesini konu alan Venom filmi, Gazeteci Brock'un sevgilisinin çalıştığı araştırma şirketinin patronunun peşine düşmesiyle başlıyor. ... Bunun üzerine araştırmalarını daha da derileştiren Eddie, şirketin bu uzaylı varlığı insan deneklerle birleştirmeye çalıştığını keşfeder.""",
                      2018,
                      "6.7"),
                     ('Seçilmiş kişi',
                      'Drama',
                      """Dünyanın düzeni yaşanan bir koas sonrası tamamen değişmiştir. Uygarlık tarihi ile tamamen bağları kopartılmış yeni nesiller yetiştirmek için, "Yaşlılar" adı verilen bir grup yeryüzündeki renk, din, düşünce gibi farklılığı tanımlayacak tüm sıfatları ortadan kaldırırlar. Artık dünya sadece siyah ve beyazdır; dümdüz, denizler, dağlar, engeller yoktur. Sadece güneşin açtığı tek tip iklim vardır. İnsanların aile bireyleri dışında birbirlerine dokunmaları, yalan söylemeleri, dili yanlış kullanmaları ve sınırlar dışına çıkmaları yasaktır. Dahası hiç kimsenin duyguları, hissiyatları ve anıları yoktur. Böyle bir düzen içerisinde ergenliğini tamamlayıp, yaşıtları gibi hayatta kendisine verilecek görevi bekleyen Jonas, ummadığı bir sürprizle karşılaşacaktır... """,
                      2014,
                      "6.5"),
                     ('Görünmeyen Misafir',
                      'Gizem ',
                      """Bir dağ oteli odasında yanında fotoğrafçı sevgilisi Laura Vidal'ın cesedi dururken polis tarafından tutuklanır. ... Adrian, Virginia'yla cinayet ve sevgilisi Laura ile ilişkisi hakkında konuşur. Her ikisi de Daniel Garrido adında bir adamın öldüğü araba kazasında yer almıştır.""",
                      2016,
                      "8.1"),
                     ('Yukarı Bak',
                      'Animasyon',
                      """Hayatı boyunca yaşamak istediği macera hayalini gerçekleştirmek için evine binlerce balon bağlayıp Güney Amerika'nın vahşi doğasına doğru yolculuğa çıkan 78 yaşındaki baloncu Carl Fredricksen'ın hikayesinin anlatıldığı yeni bir komedi.""",
                      2009,
                      "8.2"),
                     ('Yıldızlararası',
                      'Bilim-kurgu',
                      """Bir grup kaşif, bu solucan deliğinden geçip boyut değiştirerek insanlık tarafından daha önce ulaşılamamış noktalara ulaşmak ve insanlık için yeni yaşam alanları araştırmak niyetindedir.""",
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
                      """Dizi, Brooklyn'in 99 numaralı polis bölgesinde yer alan bir karakolda görev alan bir grup dedektifin ve karakol çalışanlarının yaşadığı komik ve eğlenceli olayları, bölümlük konular eşliğinde anlatıyor.""",
                      2013,
                      "8.4"),
                     ('Stranger Things ',
                      'Drama',
                      """Stranger Things, kaybolan arkadaşlarını aramaya başlayan 3 çocuğun ve onlara yardım eden insanların hikayesini konu alan bir amerikan bilim kurgu hikayesidir. Konusu kadar başarılı oyuncu kadrosuyla da dikkat çeken dizide, macera ve doğaüstü olayların sürekliliği, izleyiciyi etkisi altına alıyor.""",
                      2016,
                      "8.7"),
                     ('Mr. Robot ',
                      'polisiye',
                      """ Dizide Elliot, gündüzleri genç bir siber güvenlik mühendisi ve geceleri hackerlık yapan bir siber korsandır. Elliot, yer altı hacker grubunun (fsociety) onunla irtibata geçmek için şirketininin sistemine zarar vermesi üzerine büyük bir karmaşıklığın içine kendisini atmıştır.""",
                      2015,
                      "8.6"),
                     ('The Walking Dead',
                      'korku',
                      """The Walking Dead, aynı adlı çizgi roman serisine dayanmaktadır. Roman, dünya çapında beklenmedik bir biçimde ortaya çıkan esrarengiz bir bulaşıcı beyinsel hastalık sonucu, modern medeniyetin sonunu getiren bir zombi salgınını konu eder.""",
                      2010,
                      "8.2"),
                     ('Wayward Pines',
                      'Gizem',
                      """Dizi, Blake Crouch'ın Pines, Wayward ve The Last Town adlarını taşıyan üç kitaptan oluşan Wayward Pines serisinden uyarlanmış. ... Ardından gözlerini Wayward Pines'ta bir hastanede açıyor. Dizimiz, bunu, sonrasında yaşanacak gizemli olayları ve Ethan'ın kasabadan kaçma çabalarını anlatıyor.""",
                      2015,
                      "7.4"),
                     ('Flashforward',
                      'Bilim-kurgu',
                      """Gizemli bir olay dünya üzerindeki herkesin 137 saniye boyunca bilincini kaybetmesine sebep olmuş, bu süreçte herkes 6 ay sonrasını görmüştür - bir küresel "öngörü". Gibbons" ve 1991'de bazı bilinç kayıplarının olduğu Somali'yi araştırmaya başlar.""",
                      2009,
                      "7.6"),
                     ('How I Met Your Mother',
                      'komedi',
                      """How i met your mother dizisi 2030 yılında, Ted Mosby adlı başrol karakterin çocuklarına anneleri ile nasıl tanıştığını anlatması ile başlamaktadır. Dizide genellikle Ted Mosby'nin geçmişinde arkadaşları ile yaşadığı hayatı anlatılmaktadır.""",
                      2005,
                      "8.3"),
                     ('Prison Break',
                      'polisiye',
                      """Dizi genel olarak işlemediği bir suçtan dolayı idam cezası almış Lincoln Burrows (Dominic Purcell) 'u ve Lincoln'ün kardeşi Michael Scofield (Wentworth Miller)'ın kardeşini kurtarmak için tüm yasal yolların tükendiğini fark edip onu hapishaneden çıkarmak için bir kaçış planı yapması ve sonrasında gelişen olayları konu alır.""",
                      2005,
                      "8.3")
                     ]

        for x in seriesData:
            cur.execute("INSERT INTO SeriesTr(name, category, subject, release, imdb_rate) VALUES (?, ?, ?, ?, ?)",
                        [x[0], x[1], x[2], x[3], x[4]])

    con.commit()
    con.close()
