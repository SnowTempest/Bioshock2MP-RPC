import pyautogui
from PIL import Image
import pytesseract

# Define the coordinates of the area you want to capture
x1, y1, width, height = 100, 100, 300, 100  # Adjust these values to your needs

# Take a screenshot
screenshot = pyautogui.screenshot(region=(x1, y1, width, height))

# Save the screenshot (optional, for debugging purposes)
# screenshot.save('screenshot.png')

# Use OCR to extract text from the screenshot
extracted_text = pytesseract.image_to_string(screenshot)

# Print the extracted text
print(extracted_text)