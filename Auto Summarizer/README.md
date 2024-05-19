# AutoSummarize Pro

AutoSummarize Pro is a web application that allows users to upload a text file, generate a summary of the content, and download the summary in various formats (TXT, PDF, DOCX, ZIP). Users can choose between an online AI tool and a custom summarizer.

## Requirements

- Python 3.x
- pip
- AWS account for Secrets Manager (optional)

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/auto-summarizer.git
    cd auto-summarizer
    ```

2. Install the necessary packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Configure AWS Secrets Manager (optional):
    - Store your secret with the necessary API keys (e.g., ChatGPT API key).
    - Update `get_secret()` function in `app.py` with your secret name and AWS region.

4. Run the application:

    ```bash
    python app.py
    ```

5. Open your browser and navigate to `http://127.0.0.1:5000` to access the application.

## Project Structure

- `app.py`: Main application script.
- `requirements.txt`: List of dependencies.
- `output/`: Directory to store output files.
- `README.md`: Project documentation.

## Usage

1. Upload a text file using the provided form.
2. Choose the summary method (Online AI Tool or Custom Summarizer).
3. Click "Submit Query" to generate the summary.
4. The summary will be displayed on the page.
5. Download the summary in TXT, PDF, DOCX, or ZIP format using the provided links.
