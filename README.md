# Pls Donate Bot

## Installation

### Tesseract OCR

- **Windows**: Download and install Tesseract from [Tesseract GitHub](https://github.com/UB-Mannheim/tesseract/wiki).
- **Linux**: Use your package manager:
  ```bash
  sudo apt install tesseract-ocr
  ```

### OpenAI API Key Setup

To use GPT-3.5, you will need an OpenAI API key. Set it up as an environment variable:

```bash
export OPENAI_API_KEY='your-api-key-here'
```

Alternatively, replace the `openai.api_key` line in the script with your API key.

## Usage

1. Modify the coordinates in the `screenshot(x1, y1, x2, y2, save_path)` function to capture the region of the screen you want.
2. Update the prompt in the `get_completion(content)` function to generate a desired response from GPT-3.5.
3. Run the script.

### Script Overview

- `screenshot(x1, y1, x2, y2, save_path)`: Captures a screenshot of the specified region.
- `get_completion(content)`: Uses OpenAI's GPT-3.5 to generate a response based on the extracted text.
- `paste_text(text)`: Pastes the generated response into the chat interface.
- `main()`: Continuously captures screenshots, extracts text, generates a response, and pastes it into a chat interface until manually stopped.

## Notes

- This script is designed to automate chat responses, so use it responsibly.
- Modify the OpenAI prompt to better suit your specific needs.
- Tesseract OCR might need configuration adjustments to improve text recognition accuracy.

## License

This project is open-source. Use it at your own discretion and ensure compliance with the terms of use of OpenAI and other software involved.
