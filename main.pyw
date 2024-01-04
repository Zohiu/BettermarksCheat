version = 0.5

import pip

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])


install("selenium")
install("hjson")
install("webdriver_manager")

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, WebDriverException

from webdriver_manager.chrome import ChromeDriverManager

from time import sleep, time
from hjson import loads
from datetime import datetime

with open("config.hjson", "r") as f:
    config = loads(f.read())

if config["version"] != version:
    with open(f"error_log-{datetime.now()}.txt", "w") as f:
        f.write("Die Version der Config stimmt nicht mit dem Script überein.")
        exit(-1)


url = config["url"]

username = config["username"]
password = config["password"]

coins_buffersize = config["coins_buffersize"]
rounding_amount = config["rounding_amount"]

chrome_options = webdriver.ChromeOptions()
if config["sound_muted"]:
    chrome_options.add_argument("--mute-audio")

def wait_for_anim():
    print("Waiting for animation to complete...")
    while True:
        try:
            if driver.find_element("xpath", '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div[2]/div/div').is_displayed():
                pass
            else:
                print("Animation completed!")
                break
            pass
        except NoSuchElementException:
            break
            

def submit_answer():
    print("Submitting answer...")
    while True:
        try:
            driver.find_element("xpath", '//*[@id="submit-btn"]').click()
            break
        except NoSuchElementException:
            pass

    print("Moving to next question...")
    while True:
        try:
            driver.find_element("xpath", '//*[@id="next-exercise-btn"]').click()
            break
        except NoSuchElementException:
            pass

def finish():
    print("Submitting answer...")
    while True:
        try:
            driver.find_element("xpath", '//*[@id="submit-btn"]').click()
            break
        except NoSuchElementException:
            pass
    
    print("Showing results...")
    while True:
        try:
            driver.find_element("xpath", '//*[@id="results-btn"]').click()
            break
        except NoSuchElementException:
            pass
    
    print("Closing endscreen...")
    while True:
        try:
            driver.find_element("xpath", '//*[@id="close-endscreen-btn"]').click()
            break
        except NoSuchElementException:
            pass

def main():
    coins_buffer = []
    runs_counter = 0
    
    best_time = 100
    worst_time = 0
    
    runtime_start = time()
    
    while True:
        try:
            # Go to your page url
            driver.get(url)
            
            driver.find_element("name", "username").send_keys(username)
            driver.find_element("name", "password").send_keys(password)
            
            driver.find_element("xpath", '//*[@data-cy="ucm-login-confirm"]').click()
            
            while True:
                try:
                    button = driver.find_element("link text", 'Abgelaufene To-dos')
                    sleep(0.2)
                    button.click()
                    break
                except NoSuchElementException:
                    pass
            
            while True:
                start = time()
                print("Switching to default content")
                driver.switch_to.default_content()
                while True:
                    try:
                        button = driver.find_element("xpath", '/html/body/div[2]/div[3]/div/ng/div/div[2]/div/ul/li[36]/div/div[5]/div/div/a/span')
                        sleep(0.2)
                        button.click()
                        print("Task opened.")
                        break
                    except NoSuchElementException:
                        pass
                
                print("Switching to iframe.")
                while True:
                    try:
                        iframe = driver.find_element("xpath", '//*[@id="seriesplayer"]')
                        break
                    except NoSuchElementException:
                        pass
                        
                print("iframe found.")
                driver.switch_to.frame(iframe)
            
                # Question 1
                print("Starting Question 1...")
                while True:
                    try:
                        driver.find_element("xpath", '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div[3]/div/span/div/div/div[3]/div').click()
                        break
                    except NoSuchElementException:
                        pass
                submit_answer()

                wait_for_anim()
            
                # Question 2
                print("Question 2.")
                while True:
                    try:
                        driver.find_element("xpath", '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div[3]/div/span/div/div/div[1]/div').click()
                        break
                    except NoSuchElementException:
                        pass
                submit_answer()

                wait_for_anim()
            
                # Question 3
                print("Question 3.")
                while True:
                    try:
                        driver.find_element("xpath", "//span[text()='Nein, weil es nur einmal die 0 aber 18-mal eine rote Zahl auf der Drehscheibe gibt.']").click()
                        break
                    except NoSuchElementException:
                        pass
                submit_answer()

                wait_for_anim()
            
                # Question 4
                print("Question 4.")
                while True:
                    try:
                        driver.find_element("xpath", "//span[text()='Ja, weil eine faire Münze symmetrisch ist und eine gleichmäßig verteilte Masse besitzt.']").click()
                        break
                    except NoSuchElementException:
                        pass
                    try:
                        driver.find_element("xpath", "//span[text()='Ja, weil ein fairer Würfel symmetrisch ist und eine gleichmäßig verteilte Masse besitzt.']").click()
                        break
                    except NoSuchElementException:
                        pass
                submit_answer()

                wait_for_anim()
            
                # Question 5
                print("Question 5.")
                while True:
                    try:
                        driver.find_element("xpath", '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div[3]/div/span/div/div/div[3]/div').click()
                        break
                    except NoSuchElementException:
                        pass
                submit_answer()

                wait_for_anim()
            
                # Question 6
                print("Question 6.")
                while True:
                    try:
                        driver.find_element("xpath", '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div[3]/div/span/div/div/div[7]/div').click()
                        break
                    except NoSuchElementException:
                        pass
                    
                finish()
                print("Question 6 done! Task completed! Restarting from the beginning!")
                end = time()
                runs_counter += 1
                
                if runs_counter > 1:
                    final_time = round(end - start, rounding_amount)
                    
                    if best_time > final_time:
                        best_time = final_time
    
                    if worst_time < final_time:
                        worst_time = final_time
                    
                    coins_buffer.append(final_time)
                
                    average_time = 0
                    for i in coins_buffer:
                        average_time += i
                    average_time /= len(coins_buffer)
                
                    current_cpm = round((60 / average_time) * 3, rounding_amount)
                    current_cph = round(current_cpm * 60, rounding_amount)
                    
                    runtime = round(end - runtime_start, rounding_amount)
                    actual_cpm = round(runs_counter * 3 / (runtime / 60), rounding_amount)
                    actual_cph = round(runs_counter * 3 / ((runtime / 60) / 60), rounding_amount)
                    
                    print(f"\nThis run: {final_time}s\nBest: {best_time}s\nAverage: {round(average_time, rounding_amount)}s\nWorst: {worst_time}\nExpected earnings (coins): {current_cpm} per minute | {current_cph} per hour\nTotal runs: {runs_counter}\nBuffer: last {len(coins_buffer)}\nRuntime: {runtime}\nEarnings this session: {runs_counter * 3}\nActual earnings (coins): {actual_cpm} per minute | {actual_cph} per hour\n")
                    
                    if len(coins_buffer) >= coins_buffersize:
                        coins_buffer = coins_buffer[1:]
                
        except ElementClickInterceptedException:
            pass
            sleep(10)
            
        except WebDriverException:
            pass
            sleep(10)


if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path = ChromeDriverManager().install(), chrome_options = chrome_options)
    driver.maximize_window()
    main()