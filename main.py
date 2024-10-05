from PIL import Image
import pytesseract
import pyautogui
import time
import autoit
import pyperclip
from openai import OpenAI

client = OpenAI()

time.sleep(2)
def screenshot(x1, y1, x2, y2, save_path='image.png'):
    screenshot = pyautogui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))
    screenshot.save(save_path)

def get_completion(content):
    completion = client.chat.completions.create(
        model = "gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": "Try to get donations from me, respond in concise twitter user ways"},
            {"role": "user", "content": content}
        ],
        max_tokens=50,
    )
    return completion.choices[0].message.content

def paste_text(text):
    pyperclip.copy(text)
    pyautogui.hotkey('ctrl', 'v')
    autoit.send("{ENTER}")

def main():
    time.sleep(2)
    try:
        while True:
            screenshot(8, 60, 480, 280)
            image_path = 'image.png'
            image = Image.open(image_path)
            content = pytesseract.image_to_string(image)
            text = get_completion(content)
            autoit.send('/')
            time.sleep(1)
            paste_text(text)
            time.sleep(10)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()