import os
from datetime import datetime
from selenium import webdriver


IMPLICIT_WAIT = 3


class WindowSize:
    # maximized
    MAXIMIZED = 'MAXIMIZED'

    # desktop
    PC_width  = 1200
    PC_height = 800
    PC = '%sx%s' % (PC_width, PC_height)
    PC_dict = dict(width=PC_width, height=PC_height)

    # mobile
    MB_width  = 360
    MB_height = 640
    MB = '%sx%s' % (MB_width, MB_height)
    MB_dict = dict(width=MB_width, height=MB_height)


def loadWebDriver_localCHROME(windowSize=WindowSize.PC, implicitWait=IMPLICIT_WAIT):
    #region webdriver option
    # create options that be passed to the WebDriver initializer
    options = webdriver.ChromeOptions()

    #TODO load chrome binary path auto instead of hardcoded as below
    # tell selenium to use the beta/dev channel version of chrome
    options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'  # for MacOS
    # options.binary_location = '/usr/bin/google-chrome' #for linux - get by `which google-chrome`

    # set headless mode for chrome
    options.add_argument('headless')

    # set the window size
    if windowSize == WindowSize.MAXIMIZED:
        # set Chrome window maximize ref. https://stackoverflow.com/a/12213723/248616 #TODO Why size 800x600 not full?
        options.add_argument("--start-maximized")
    else:
        options.add_argument('window-size=%s' % windowSize)

    # more options go here ref. https://sites.google.com/a/chromium.org/chromedriver/capabilities

    #endregion webdriver option

    # initialize the driver
    driver = webdriver.Chrome(chrome_options=options)  # If nothing happens then everything worked! Normally, a new browser window would pop open at this point with a warning about being controlled by automated test software. It not appearing is exactly what we want to happen in headless mode and it means that we could be running our code on a server that doesn't even have a graphical environment. Everything from here on out is just standard Selenium so if you were only trying to figure out how to get it working with Chrome in headless mode then that's it!
    # config the implicit wait aka. default waiting time for any action ref. http://www.seleniumhq.org/docs/04_webdriver_advanced.jsp#implicit-waits
    driver.implicitly_wait(implicitWait)  # in seconds
    return driver

def loadWebDriver_localFIREFOX():
    #region webdriver option
    # create options that be passed to the WebDriver initializers
    os.environ['MOZ_HEADLESS'] = '1'
    # options = Options()
    # options.headless = True
    # options = webdriver.FirefoxOptions()

    driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')  # If nothing happens then everything worked! Normally, a new browser window would pop open at this point with a warning about being controlled by automated test software. It not appearing is exactly what we want to happen in headless mode and it means that we could be running our code on a server that doesn't even have a graphical environment. Everything from here on out is just standard Selenium so if you were only trying to figure out how to get it working with Chrome in headless mode then that's it!
    # config the implicit wait aka. default waiting time for any action ref. http://www.seleniumhq.org/docs/04_webdriver_advanced.jsp#implicit-waits
    # driver.implicitly_wait(implicitWait)  # in seconds
    return driver


APP_HOME         = os.path.abspath(os.path.dirname(__file__)+'../../../')
SNAPSHOT_VAULT   = f'{APP_HOME}/_snapshot_/vault'
timestamp        = datetime.now().strftime("%Y%m%d-%H%M%S-%f")[:-3]
SNAPSHOT_FOLDER  = f'{SNAPSHOT_VAULT}/{timestamp}'
SNAPSHOT_COUNTER = 0

os.makedirs(SNAPSHOT_FOLDER, exist_ok=True) # create folder path recursively ref. https://stackoverflow.com/a/41146954/248616


def take_snapshot(driver, prefix=None, suffix=None):

    # prepare filename
    global SNAPSHOT_COUNTER
    filename = '{SNAPSHOT_FOLDER}/{prefix}s{SNAPSHOT_COUNTER:02d}{suffix}.png'.format( # format number ref. https://stackoverflow.com/a/135157/248616
        SNAPSHOT_FOLDER  = SNAPSHOT_FOLDER,
        prefix           = '%s-' % prefix if prefix else '',
        suffix           = '-%s' % suffix if suffix else '',
        SNAPSHOT_COUNTER = SNAPSHOT_COUNTER,
    )

    # do take snapshot
    driver.get_screenshot_as_file(filename); SNAPSHOT_COUNTER += 1

    # printing
    print(f'Snapshot taken at {filename}')

    return filename

