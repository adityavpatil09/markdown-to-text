from flask import Flask, render_template, request
import re

app = Flask(__name__)

def markdown_to_plain(md_text):
    """Convert Markdown to plain text while preserving natural bullet formatting."""

    # Remove bold (**bold** → bold)
    md_text = re.sub(r'\*\*(.*?)\*\*', r'\1', md_text)  

    # Remove italic (*italic* → italic)
    md_text = re.sub(r'\*(.*?)\*', r'\1', md_text)  

    # Remove inline code (`code` → code)
    md_text = re.sub(r'`(.+?)`', r'\1', md_text)  

    # Remove headings (# Heading → Heading)
    md_text = re.sub(r'#+\s*(.*)', r'\1', md_text)  

    # Remove Markdown links [text](url) → text
    md_text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', md_text)  

    # Normalize multiple newlines
    md_text = re.sub(r'\n{2,}', '\n', md_text)  

    # Handle unordered lists (convert `- ` or `* ` into `• ` for a more natural feel)
    md_text = re.sub(r'^\s*[-*]\s+', '• ', md_text, flags=re.MULTILINE)

    # Handle ordered lists (keep numbers but ensure spacing)
    md_text = re.sub(r'^\s*(\d+)\.\s+', r'\1. ', md_text, flags=re.MULTILINE)

    # Handle tables: Convert table rows into readable text
    md_text = re.sub(r'\|(.+?)\|', r'\1', md_text)  # Remove pipe delimiters
    md_text = re.sub(r'\n\s*\|\s*(.+?)\s*\|\s*\n', '\n\1\n', md_text)  # Simplify table rows
    md_text = re.sub(r'\n\s*\|', '', md_text)  # Remove the trailing pipe at the start of a table row

    return md_text.strip()

@app.route("/", methods=["GET", "POST"])
def index():
    converted_text = ""
    if request.method == "POST":
        markdown_text = request.form["markdown_text"]
        converted_text = markdown_to_plain(markdown_text)
    return render_template("index.html", converted_text=converted_text)

if __name__ == "__main__":
    app.run(debug=True)
