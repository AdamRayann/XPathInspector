# XPath Visualizer

**XPath Visualizer** is a Python-based tool that uses Selenium to dynamically highlight elements on a webpage based on XPath expressions.  
This tool was developed as part of a home task for **CyberInt**.  

---

## 💻 Features

- Highlight HTML elements using XPath
- Automatically scrolls to bring elements into view
- Displays the full HTML (`outerHTML`) of highlighted elements
- Batch XPath execution from a file (`xpaths.txt`)

---
## 🔍 Commands

- **`all`**  
Highlights all elements from the task answers , one at a time.


- **`Specific XPath expression`**  
Example:
```text
    .//input[contains(@id,'search-q')] 
```

- **`exit`**  
Exits the script.
---

## 🚀 Requirements

- Python 3.7+
- Google Chrome
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) (ensure it's in your system PATH)
- `selenium` Python package

Install with:

```bash
pip install selenium
```
---
