## 🩺 Medical Report Simplifier

A GenAI-powered app that converts complex medical reports into clear, layman-friendly explanations.


## Features

- Extracts text from **PDFs**, **printed**, and **handwritten images**
- Simplifies complex medical language using **LLaMA 3** locally via **Ollama**
- Uses **OCR.Space API** for reliable OCR on handwritten and scanned text
- Streamlit-based user interface for ease of use
- API keys stored securely using `.env`


##  Tech Stack

| Tool             | Role                                             |
|------------------|--------------------------------------------------|
| Streamlit        | Web frontend                                     |
| OCR.Space API    | Optical Character Recognition for image inputs   |
| Ollama + LLaMA 3 | Local LLM backend for text simplification        |
| Python-dotenv    | API key management                               |
| Pillow (PIL)     | Image file handling                              |






## Sample Inputs

* Lab blood test reports in PDF
* Scanned printed reports (JPEG, PNG)
* Handwritten notes (legible and clear)

## Security Notes

* Your `.env` file is **excluded** from Git tracking.
* Never expose API keys in source files.

## 👤 Author

**Keerti Damani**
GitHub: [@keertidamani](https://github.com/keertidamani)

## License

This project is open-source under the MIT License.



