class Path(object):
    main_website = "http://www.seleniumframework.com/Practiceform/"

    # Contact fields
    imie = "//input[@placeholder='Name *']"
    email = "//input[@placeholder='E-mail *']"
    telephone = "//input[@placeholder='Telephone *']"
    country = "//input[@placeholder='Country']"
    company = "//input[@placeholder='Company']"
    message = "//textarea[@placeholder='Message']"
    submit_button = "//a[@class='dt-btn dt-btn-m dt-btn-submit']"
    clear_button = "//a[@class='clear-form']"


    # Used in TEST4
    Selenium_Python_Basic_Tutorial = "//body[1]/div[2]/header[1]/div[1]/div[2]/div[1]/nav[1]/ul[1]/li[2]/ul[1]/li[4]/ul[1]/li[1]/a[1]"
    Selenium_Python_Intermediate = "//body[1]/div[1]/header[1]/div[1]/div[2]/div[1]/nav[1]/ul[1]/li[2]/ul[1]/li[4]/ul[1]/li[2]/a[1]"
    Selenium_Python_Frameworks = "//body[1]/div[1]/header[1]/div[1]/div[2]/div[1]/nav[1]/ul[1]/li[2]/ul[1]/li[4]/ul[1]/li[3]/a[1]"


    # 1 Browser Windows
    new_browser_window = "//button[@id='button1']"
    new_message_window = "//button[@onclick='newMsgWin()']"
    new_browser_tab_button = "//button[@onclick='newBrwTab()']"

    # 2 JavaScript alert
    alertbox = "//button[@id='alert']"