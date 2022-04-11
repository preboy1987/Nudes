from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException
import time

# Declaration
waitTime = 2
timeTry = 5
current_time = datetime.now().strftime("%D - %H:%M:%S")
prefixFile = "Giang_sendNudes_"
inFile = open(prefixFile + "input.txt", "r")
eachLine = inFile.readlines()
inProfile = open(prefixFile + "profile.txt", "r")
eachProfile = inProfile.readlines()
count = 0

# DEBUG: Declaration
debugMode = True

# DEBUG: Debug trace function
def debugTrace(debugText):
    if debugMode == True:
        print(debugText)

# Find Element until it exists in 5 seconds
def findElementXPath(driver, elementName, elementXPath):
    #Find element elementName until it exists
    tic = time.perf_counter()
    toc = time.perf_counter()
    while (toc - tic) <= timeTry:
        toc = time.perf_counter()
        try:
            debugTrace('Try to find ' + elementName + ' again...')
            time.sleep(waitTime)
            element = driver.find_element(By.XPATH, elementXPath)
            debugTrace('element.text: ' + element.text)
            return element
        except NoSuchElementException:
            debugTrace('!!!!!!!!NoSuchElementException: ' + elementName)
            toc = time.perf_counter()
            continue
    return None

# Choose chrome profile
options = webdriver.ChromeOptions()
options.add_argument("no-sandbox")
options.add_argument("start-maximized")
# options.add_argument("--window-size=800,700")
# chromeOption.add_argument("--disable-dev-shm-usage")
userDataDir = 'C:\\Users\\Giang\\AppData\\Local\\Google\\Chrome\\User Data'
# C:\Users\Giang\AppData\Local\Google\Chrome\User Data
for profile in eachProfile:
    profileID = profile
options.add_argument('--user-data-dir=' + userDataDir)
options.add_argument('--profile-directory=' + profileID)
driver = webdriver.Chrome(options=options)

with open(prefixFile + "output.txt", "a") as outFile:
    outFile.write('\n' + '========== New Test ========== ' + current_time + '\n')
    debugTrace('========== New Test ========== ' + current_time)

    # Open webbrowser with links
    driver.get('chrome-extension://cphhlgmgameodnhkjdmkpanlelnlohao/#/popup/transfer/create')
    time.sleep(waitTime)
    
    # Fill wallet password & Login
    debugTrace('Fill wallet password & Login')
    driver.find_element(By.XPATH, '/html/body/neo-line/div/ng-component/mat-sidenav-container/mat-sidenav-content/div[2]/ng-component/div/form/mat-form-field/div/div[1]/div[2]/input').send_keys('namgiang1987')
    time.sleep(waitTime)
    driver.find_element(By.XPATH, '/html/body/neo-line/div/ng-component/mat-sidenav-container/mat-sidenav-content/div[2]/ng-component/div/button[2]').click()
    time.sleep(waitTime)

    for line in eachLine:
        count += 1
        result = ''

        #Open webbrowser with links
        driver.get('chrome-extension://cphhlgmgameodnhkjdmkpanlelnlohao/#/popup/transfer/create')
        time.sleep(waitTime)

        try:
            # Fill address
            debugTrace('Fill address')
            findElementXPath(driver, 'Address', '/html/body/neo-line/div/ng-component/mat-sidenav-container/mat-sidenav-content/div[2]/ng-component/ng-component/div[2]/div[1]/div').click()
            findElementXPath(driver, 'Address', '/html/body/div[2]/div[2]/div/mat-dialog-container/ng-component/div[2]/div[1]/input').send_keys(line)

            # Choose NUDES
            debugTrace('Choose NUDES')
            findElementXPath(driver, 'NUDES', '/html/body/neo-line/div/ng-component/mat-sidenav-container/mat-sidenav-content/div[2]/ng-component/ng-component/div[2]/div[2]/div').click()
            findElementXPath(driver, 'NUDES', '/html/body/div[2]/div[2]/div/mat-dialog-container/ng-component/div[2]/div[3]/div[2]').click()

            # 100 NUDES
            debugTrace('100 NUDES')
            findElementXPath(driver, '100 NUDES', '/html/body/neo-line/div/ng-component/mat-sidenav-container/mat-sidenav-content/div[2]/ng-component/ng-component/div[2]/div[3]/div/input').send_keys('100')

            # Click Yes
            debugTrace('Click Yes')
            findElementXPath(driver, 'Yes', '/html/body/neo-line/div/ng-component/mat-sidenav-container/mat-sidenav-content/div[2]/ng-component/ng-component/div[2]/div[5]/button[2]').click()
            findElementXPath(driver, 'Yes', '/html/body/div[2]/div/div/mat-dialog-container/ng-component/div/div/div[2]/div/div[4]/button[2]').click()
            time.sleep(waitTime)

            result = 'GOOD JOB'
            
        except:
            debugTrace('Go to EXCEPTION')
            result = 'Go to EXCEPTION'
            continue

        line = line.replace('\n',"")
        debugTrace(line + '\t= ' + result)
        outFile.write(line + '\t = ' + result + '\n')
        outFile.flush()

    # Write count
    outFile.write('count = ' + str(count) + '\n')
    current_time = datetime.now().strftime("%D - %H:%M:%S")
    debugTrace('========== END Test ========== ' + current_time)
    outFile.write('\n' + '========== END Test ========== ' + current_time + '\n')

# Close file
inFile.close()
outFile.close()
driver.close()
driver.quit()

#pyinstaller sample.py --noconsole --onefile
