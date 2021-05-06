class I18N:
    def __init__(self, language):
        if language == "en":
            self.load_text_in_english()
        elif language == "tr":
            self.load_text_in_turkish()
        else:
            raise NotImplementedError("Unsupported language.")

    def load_text_in_turkish(self):
        # Login Page
        self.login_page_head = "Pyflix'e Hoşgeldin"
        self.login_page_head2 = "Hesap Oluştur"
        self.login_page_title = "Giriş Sayfası"

        self.lang_frame_label = "Dil"
        self.lang_frame_head = "Dil seçiniz"
        self.lang_frame_rd1 = "İngilizce"
        self.lang_frame_rd2 = "Türkçe"

        self.login_frame_label = "Bilgilerinizi giriniz"
        self.login_frame_username_label = "Kullanıcı adı"
        self.login_frame_password_label = "Şifre"
        self.login_frame_login_button = "Giriş"
        self.login_frame_create_button = "Hesap Oluştur"

        self.create_frame_login = "Girişe geri dön"
        self.create_frame_create = "Hesabı Oluştur"
        self.create_empty_error = "Boşlukları doldurmalısınız."

        # Main Page
        self.main_page_title = "Ana Sayfa"
        self.main_page_movies_button = "Filmleri Göster"
        self.main_page_series_button = "Dizileri Göster"
        self.main_page_movies_fav = "Favori Filmleriniz"
        self.main_page_series_fav = "Favori Dizileriniz"
        self.main_page_logoff_button = "Çıkış Yap"

        # Movie Page and Tv Page
        self.series_page_title = "Dizi Sayfası"
        self.movie_page_title = "Film Sayfası"

        self.movie_page_tv_name = "İsim"
        self.movie_page_tv_category = "Kategori"
        self.movie_page_tv_release = "Çıkış Tarihi"
        self.movie_page_tv_imdb = "Imdb Puanı"
        self.movie_page_goMain = "Ana Sayfaya Dön"

        # Detailed Pages

        self.detail_addToFav = "Favorilere Ekle"
        self.detail_removeFromFav = "Favorilerden Çıkar"

    def load_text_in_english(self):
        # Login Page
        self.login_page_head = "Welcome to Pyflix"
        self.login_page_head2 = "Create account"
        self.login_page_title = "Login Page"

        self.lang_frame_label = "Language"
        self.lang_frame_head = "Choose a language"
        self.lang_frame_rd1 = "English"
        self.lang_frame_rd2 = "Turkish"

        self.login_frame_label = "Enter your informations"
        self.login_frame_username_label = "Username"
        self.login_frame_password_label = "Password"
        self.login_frame_login_button = "Login"
        self.login_frame_create_button = "Create"

        self.create_frame_login = "Go back to Login"
        self.create_frame_create = "Create Account"
        self.create_empty_error = "You need to fill blanks."

        # Main Page
        self.main_page_title = "Main Page"
        self.main_page_movies_button = "Show Movies"
        self.main_page_series_button = "Show TV Series"
        self.main_page_movies_fav = "Favorite Movies"
        self.main_page_series_fav = "Favorite TV Shows"
        self.main_page_logoff_button = "Log Off"

        # Movie Page and Tv Page
        self.series_page_title = "TV Series Page"
        self.movie_page_title = "Movie Page"

        self.movie_page_tv_name = "Name"
        self.movie_page_tv_category = "Category"
        self.movie_page_tv_release = "Release Date"
        self.movie_page_tv_imdb = "Imdb Rate"
        self.movie_page_goMain = "Go Back to Main Page"

        # Detailed Pages

        self.detail_addToFav = "Add to Favorites"
        self.detail_removeFromFav = "Remove From Favorites"