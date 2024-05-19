from flask import Flask, request, jsonify, send_from_directory, render_template_string
import os
from transformers import pipeline
import docx
from fpdf import FPDF
import zipfile
import boto3
import json

app = Flask(__name__)

# Initialize the summarization pipeline
summarizer = pipeline("summarization")

# Function to retrieve secret from AWS Secrets Manager
def get_secret():
    secret_name = "YOUR_SECRET_NAME"
    region_name = "YOUR_AWS_REGION"

    # Create a Secrets Manager client
    client = boto3.client("secretsmanager", region_name=region_name)

    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
        secret = get_secret_value_response["SecretString"]
        return json.loads(secret)
    except Exception as e:
        print("Error retrieving secret from AWS Secrets Manager: ", e)
        return None

def summarize_text(text):
    summary_list = summarizer(text, max_length=500, min_length=100, do_sample=False)
    summary = summary_list[0]['summary_text']
    return summary

def summarize_text_custom(text):
    # Custom summarization logic here
    return summarize_text(text)  # Placeholder, replace with custom logic

def convert_to_formats(summary):
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    summary_text_path = os.path.join(output_dir, 'summary.txt')
    summary_pdf_path = os.path.join(output_dir, 'summary.pdf')
    summary_word_path = os.path.join(output_dir, 'summary.docx')
    zip_path = os.path.join(output_dir, 'summary.zip')

    # Save summary as text file
    with open(summary_text_path, 'w') as file:
        file.write(summary)

    # Save summary as PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, summary)
    pdf.output(summary_pdf_path)

    # Save summary as Word document
    doc = docx.Document()
    doc.add_paragraph(summary)
    doc.save(summary_word_path)

    # Create ZIP file
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        zipf.write(summary_text_path, os.path.basename(summary_text_path))
        zipf.write(summary_pdf_path, os.path.basename(summary_pdf_path))
        zipf.write(summary_word_path, os.path.basename(summary_word_path))

    return {
        'text': summary_text_path,
        'pdf': summary_pdf_path,
        'word': summary_word_path,
        'zip': zip_path,
    }

@app.route('/')
def index():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>AutoSummarize Pro</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            .container { max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #ccc; border-radius: 10px; }
            .form-group { margin-bottom: 15px; }
            .form-group label { display: block; margin-bottom: 5px; }
            .form-group input, .form-group select, .form-group button { width: 100%; padding: 10px; }
            .form-group button { cursor: pointer; }
            .summary { margin-top: 20px; padding: 10px; border: 1px solid #ccc; border-radius: 10px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>AutoSummarize Pro</h1>
            <form id="upload-form" enctype="multipart/form-data">
                <div class="form-group">
                    <label for="file-input">Upload File:</label>
                    <input type="file" id="file-input" name="file">
                </div>
                <div class="form-group">
                    <label for="method-select">Summary Method:</label>
                    <select id="method-select" name="method">
                        <option value="online">Online AI Tool</option>
                        <option value="custom">Custom Summarizer</option>
                    </select>
                </div>
                <div class="form-group">
                    <button type="submit">Submit Query</button>
                </div>
                <div id="summary" class="summary" style="display:none;">
                    <h2>Summary:</h2>
                    <p id="summary-text"></p>
                </div>
                <div class="form-group" id="download-links" style="display:none;">
                    <button id="download-button">Download</button>
                </div>
            </form>
        </div>
        <script>
            document.getElementById('upload-form').addEventListener('submit', async (e) => {
                e.preventDefault();
                
                const fileInput = document.getElementById('file-input');
                const methodSelect = document.getElementById('method-select');
                const formData = new FormData();
                formData.append('file', fileInput.files[0]);
                formData.append('method', methodSelect.value);

                const response = await fetch('/api/summarize', {
                    method: 'POST',
                    body: formData
                });

                const data = await response.json();
                document.getElementById('summary-text').innerText = data.summary;
                document.getElementById('summary').style.display = 'block';

                const downloadLinks = data.downloadLinks;
                document.getElementById('download-links').innerHTML = `
                    <a href="/download/${downloadLinks.text}" download="summary.txt">Download Text</a><br>
                    <a href="/download/${downloadLinks.pdf}" download="summary.pdf">Download PDF</a><br>
                    <a href="/download/${downloadLinks.word}" download="summary.docx">Download Word</a><br>
                    <a href="/download/${downloadLinks.zip}" download="summary.zip">Download ZIP</a>
                `;
                document.getElementById('download-links').style.display = 'block';
            });
        </script>
    </body>
    </html>
    ''')

@app.route('/api/summarize', methods=['POST'])
def summarize():
    if 'file' not in request.files or 'method' not in request.form:
        return "Missing file or method", 400

    file = request.files['file']
    method = request.form['method']
    if file.filename == '':
        return "No selected file", 400

    text = file.read().decode('utf-8')

    try:
        summary = summarize_text(text) if method == 'online' else summarize_text_custom(text)
        download_links = convert_to_formats(summary)
        return jsonify({'summary': summary, 'downloadLinks': download_links})
    except Exception as e:
        return str(e), 500

@app.route('/download/<path:filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory('output', filename, as_attachment=True)

if __name__ == '__main__':
    if not os.path.exists('output'):
        os.makedirs('output')
    app.run(debug=True)
