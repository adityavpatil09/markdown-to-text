# 📝 Markdown to Plain Text Converter

## 🚀 Overview  
Markdown is widely used for formatting text, but sometimes we need a **clean, plain text version**. This **Flask-based web application** allows users to:  
✅ Convert **Markdown-formatted text** into **Plain Text**  
✅ Preserve **bullet points** and **ordered lists**  
✅ Convert **tables into readable text**  
✅ Provide a **modern and user-friendly UI** with **Light/Dark Mode**  

This tool is **ideal for writers, students, and developers** who frequently work with Markdown and need a quick **conversion to plain text**.

---

## 🎯 **Features & Functionality**  

### ✅ **Markdown to Plain Text Conversion**  
- Removes **bold (`**bold**`)**, **italics (`*italic*`)**, and **inline code (`code`)**  
- Strips **Markdown headings (`# Heading`)**  
- Converts **bullet points (`- item` / `* item`)** into **• item**  
- Converts **ordered lists (`1. Item`)** into **1. Item**  
- Converts **tables (`| Col1 | Col2 |`)** into simple text format  
- Removes **Markdown links (`[Text](URL)`)**, keeping only the text  

### 🎨 **User-Friendly Interface**  
- **Minimalist & elegant design**  
- **Light/Dark mode toggle** 🌞🌙  
- **Mobile responsive** – works on **phones, tablets, and desktops**  

### ⚡ **Performance & Deployment**  
- **Built with Flask** – lightweight and fast  
- **Deployed using Gunicorn** – for production readiness  

---

## 🛠️ **Installation & Setup**  

### 🔹 **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/yourusername/markdown-to-text.git
cd markdown-to-text
