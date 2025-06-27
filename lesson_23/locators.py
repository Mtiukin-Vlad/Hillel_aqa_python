# 1. Лого (svg)
XPATH_LOGO = "//app-header//a[.//svg]"
CSS_LOGO = "app-header a > svg"

# 2. Ссылка Home
XPATH_HOME = "//a[@routerlink='/' and text()='Home']"
CSS_HOME = "a[routerlink='/' i]"

# 3. Кнопка About
XPATH_ABOUT = "//button[@appscrollto='aboutSection' and text()='About']"
CSS_ABOUT = "button[appscrollto='aboutSection']"

# 4. Кнопка Contacts
XPATH_CONTACTS = "//button[@appscrollto='contactsSection' and text()='Contacts']"
CSS_CONTACTS = "button[appscrollto='contactsSection']"

# 5. Кнопка Guest log in
XPATH_GUEST = "//button[contains(@class, '-guest') and text()='Guest log in']"
CSS_GUEST = "button.header-link.-guest"

# 6. Кнопка Sign In
XPATH_SIGN_IN = "//button[contains(@class, 'header_signin') and text()='Sign In']"
CSS_SIGN_IN = "button.header_signin"

# 7. Кнопка "Create an account" в баннере
XPATH_CREATE_BTN = "//app-home//button[text()='Create an account']"
CSS_CREATE_BTN = "app-home button"

# 8. Превью YouTube-плеера (необязательное)
XPATH_YT_PREVIEW = "//*[@id='movie_player']//div[contains(@class, 'ytp-cued-thumbnail-overlay')]"
CSS_YT_PREVIEW = "#movie_player .ytp-cued-thumbnail-overlay"

# 9. Изображение слева в секции About
XPATH_ABOUT_IMG_LEFT = "//*[@id='aboutSection']//div[1]//img"
CSS_ABOUT_IMG_LEFT = "#aboutSection div:first-child img"

# 10. Изображение справа
XPATH_ABOUT_IMG_RIGHT = "//*[@id='aboutSection']//div[contains(@class,'col-lg-6')]//img"
CSS_ABOUT_IMG_RIGHT = "#aboutSection .col-lg-6 img"

# 11. Заголовок About слева
XPATH_ABOUT_TITLE_LEFT = "//*[@id='aboutSection']//div[contains(@class,'col-lg-6')][1]//p[contains(@class,'about-block_title')]"
CSS_ABOUT_TITLE_LEFT = "#aboutSection .col-lg-6:nth-of-type(1) p.about-block_title"

# 12. Текст описания About слева
XPATH_ABOUT_TEXT_LEFT = "//*[@id='aboutSection']//div[contains(@class,'col-lg-6')][1]//p[contains(@class,'about-block_descr')]"
CSS_ABOUT_TEXT_LEFT = "#aboutSection .col-lg-6:nth-of-type(1) p.about-block_descr"

# 13. Заголовок About справа
XPATH_ABOUT_TITLE_RIGHT = "//*[@id='aboutSection']//div[contains(@class,'col-lg-6')][2]//p[contains(@class,'about-block_title')]"
CSS_ABOUT_TITLE_RIGHT = "#aboutSection .col-lg-6:nth-of-type(2) p.about-block_title"

# 14. Текст описания About справа
XPATH_ABOUT_TEXT_RIGHT = "//*[@id='aboutSection']//div[contains(@class,'col-lg-6')][2]//p[contains(@class,'about-block_descr')]"
CSS_ABOUT_TEXT_RIGHT = "#aboutSection .col-lg-6:nth-of-type(2) p.about-block_descr"

# 15. Заголовок секции Contacts
XPATH_CONTACTS_TITLE = "//*[@id='contactsSection']//h2[text()='Contacts']"
CSS_CONTACTS_TITLE = "#contactsSection h2"

# 16. Первая соцсеть (telegram)
XPATH_SOCIAL_1 = "//*[@id='contactsSection']//a[contains(@class,'socials_link')][1]"
CSS_SOCIAL_1 = "#contactsSection a.socials_link:nth-of-type(1)"

# 17. Иконка Telegram
XPATH_TELEGRAM = "//*[@id='contactsSection']//a[contains(@href, 't.me') and contains(@class,'socials_link')]//span[contains(@class, 'icon-telegram')]"
CSS_TELEGRAM = "#contactsSection a[href*='t.me'].socials_link span.icon-telegram"

# 18. Иконка YouTube
XPATH_YOUTUBE = "//*[@id='contactsSection']//a[contains(@href, 'youtube.com') and contains(@class,'socials_link')]//span[contains(@class, 'icon-youtube')]"
CSS_YOUTUBE = "#contactsSection a[href*='youtube.com'].socials_link span.icon-youtube"

# 19. Иконка Instagram
XPATH_INSTAGRAM = "//*[@id='contactsSection']//a[contains(@href, 'instagram.com') and contains(@class,'socials_link')]//span[contains(@class, 'icon-instagram')]"
CSS_INSTAGRAM = "#contactsSection a[href*='instagram.com'].socials_link span.icon-instagram"

# 20. Иконка LinkedIn
XPATH_LINKEDIN = "//*[@id='contactsSection']//a[contains(@href, 'linkedin.com') and contains(@class,'socials_link')]//span[contains(@class, 'icon-linkedin')]"
CSS_LINKEDIN = "#contactsSection a[href*='linkedin.com'].socials_link span.icon-linkedin"

# 21. Сайт ithillel.ua
XPATH_SITE = "//a[text()='ithillel.ua']"
CSS_SITE = "a.contacts_link.display-4"

# 22. Почта
XPATH_EMAIL = "//a[starts-with(@href, 'mailto:')]"
CSS_EMAIL = "a[href^='mailto:']"

# 23. Подвал © 2021
XPATH_COPYRIGHT = "//p[contains(text(),'© 2021')]"
CSS_COPYRIGHT = "footer p:first-of-type"

# 24. Текст подвала
XPATH_FOOTER_TEXT = "//p[contains(text(),'educational purposes')]"
CSS_FOOTER_TEXT = "footer p:last-of-type"

# 25. Логотип в подвале
XPATH_FOOTER_LOGO = "//app-footer//a[.//svg]"
CSS_FOOTER_LOGO = "app-footer a svg"
