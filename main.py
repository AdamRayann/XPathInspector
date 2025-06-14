from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://support.mozilla.org/en-US/questions/firefox?show=all"

def highlight_elements(driver, xpath):
    highlight_script = """
        var elements = document.evaluate(arguments[0], document, null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null);
        var htmlList = [];
        for (var i = 0; i < elements.snapshotLength; i++) {
            var el = elements.snapshotItem(i);
            if (el.nodeType === 1) {
                el.setAttribute('data-original-style', el.getAttribute('style') || '');
                el.style.outline = '3px solid red';
                el.style.backgroundColor = 'yellow';
                el.scrollIntoView({ behavior: 'smooth', block: 'center' });
                el.classList.add('highlighted-by-script');
                htmlList.push(el.outerHTML);
            }
        }
        return htmlList;
    """
    highlighted_html = driver.execute_script(highlight_script, xpath)
    for idx, html in enumerate(highlighted_html, 1):
        print(f"\n=== Highlighted Element {idx} ===\n{html}\n")

def clear_all_highlights(driver):
    clear_script = """
        var elements = document.querySelectorAll('.highlighted-by-script');
        elements.forEach(function(el) {
            var originalStyle = el.getAttribute('data-original-style');
            if (originalStyle !== null) {
                el.setAttribute('style', originalStyle);
            } else {
                el.removeAttribute('style');
            }
            el.removeAttribute('data-original-style');
            el.classList.remove('highlighted-by-script');
        });
    """
    driver.execute_script(clear_script)


# Open the browser once
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(URL)

# Initialize last XPATH for unhighlighting
last_xpath = ""

while True:
    clear_all_highlights(driver)

    XPATH = input("Enter the element's XPath or 'all' to load from file (or 'exit'): ")

    if XPATH.lower() == "exit":
        break

    elif XPATH.lower() == "all":
        try:
            with open("xpaths.txt", "r") as file:
                for line in file:
                    xpath = line.strip()
                    if xpath:
                        highlight_elements(driver, xpath)
                        time.sleep(3)
                        clear_all_highlights(driver)
        except FileNotFoundError:
            print("File 'xpaths.txt' not found.")
        continue

    else:
        highlight_elements(driver, XPATH)
        last_xpath = XPATH
