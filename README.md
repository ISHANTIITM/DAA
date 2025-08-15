TDS Data Analyst Agent

The TDS Data Analyst Agent is an advanced, AI-driven data analysis platform that integrates Google’s Generative AI with robust data processing capabilities. It enables users to upload datasets and analytical questions, providing detailed insights, visualizations, and automated workflows through a web-based interface.

Overview

This application revolutionizes the way users interact with data by offering intelligent analysis, statistical summaries, and dynamic visualizations. Users can upload multiple file formats, perform batch processing, and receive comprehensive reports and AI-generated recommendations.

Key Features

Intelligent Data Analysis: Leverages Google Generative AI for advanced insights.

Interactive Visualizations: Generates dynamic charts and graphs using Matplotlib and Seaborn.

Web Scraping: Extracts structured data from URLs and web pages.

Multi-Format Support: Supports CSV, Excel, JSON, Parquet, and plain text files.

Batch Processing: Allows the analysis of multiple questions simultaneously.

Modern User Interface: Provides a responsive and user-friendly design.

Real-Time Processing: Ensures fast data analysis with progress tracking.

Quick Start
Prerequisites

Python 3.8 or higher

Google Generative AI API key

Modern web browser

Installation

Clone the repository:

git clone <repository-url>
cd Project_2


Install dependencies:

pip install -r requirements.txt


Set up environment variables by creating a .env file in the project root:

GOOGLE_API_KEY=your_google_generative_ai_api_key_here
LLM_TIMEOUT_SECONDS=150


Run the application:

python app.py


Access the application in your browser at:

http://localhost:8000

Usage Guide
Step 1: Prepare Questions

Create a .txt file containing your analysis questions, with each question on a separate line:

What are the key trends in the sales data?
Which products have the highest profit margins?
Show a correlation analysis between variables A and B.

Step 2: Upload Data

Questions File: Required (must be in .txt format).

Dataset: Optional (supported formats include CSV, Excel, JSON, Parquet, TXT).

Step 3: Receive Results

The agent will process your questions and data to:

Generate comprehensive analysis

Produce interactive visualizations

Provide AI-powered insights and recommendations

Technical Architecture
Backend

FastAPI for high-performance server-side processing

LangChain for LLM orchestration

Google Generative AI for advanced natural language and analytical capabilities

Pandas & NumPy for data manipulation

Matplotlib & Seaborn for visualizations

Frontend

HTML5/CSS3 for responsive design

JavaScript for interactivity

Bootstrap-inspired styling for professional appearance

Data Processing

Supports multiple file formats (CSV, Excel, JSON, Parquet, TXT)

Includes automated web scraping for HTML tables, CSV/Excel links, and APIs

Performs data cleaning and preprocessing

Offers statistical and inferential analysis

API Endpoints
GET /

Serves the main web interface.

POST /analyze

Processes questions and datasets.
Parameters:

questions_file: Required text file containing questions

data_file: Optional dataset file

POST /scrape

Extracts structured data from a given URL.
Parameters:

url: Target web address

Tool Functions

scrape_url_to_dataframe(url): Extracts data from web pages in formats such as HTML tables, CSV, Excel, JSON, and plain text.

analyze_dataframe_with_llm(data, questions): Performs AI-powered analysis, including statistical summaries, trend identification, correlation studies, anomaly detection, and predictive insights.

Supported Data Formats
Format	Extension	Description
CSV	.csv	Comma-separated values
Excel	.xlsx, .xls	Microsoft Excel spreadsheets
JSON	.json	JavaScript Object Notation
Parquet	.parquet	Columnar storage format
Text	.txt	Plain text files
Example Use Cases

Business Intelligence

Sales performance monitoring

Customer behavior insights

Market trend identification

Financial reporting

Research & Analytics

Academic research

Hypothesis testing

Data exploration

Statistical modeling

Data Science

Exploratory Data Analysis (EDA)

Feature engineering guidance

Model evaluation

Data quality assessment

Security and Privacy

Local Processing: Data is processed locally on your server.

No Data Storage: Files are processed in memory and not stored persistently.

API Key Protection: Environment variable usage for security.

CORS Configuration: Adjustable for deployment requirements.

Deployment

Local Development

python app.py


Production Deployment

Set up a production server (AWS, GCP, Azure, etc.)

Install dependencies:

pip install -r requirements.txt


Configure environment variables

Use Gunicorn with Uvicorn workers:

gunicorn app:app -w 4 -k uvicorn.workers.UvicornWorker


Docker Deployment

FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "app.py"]

Configuration

Environment Variables

Variable	Description	Default
GOOGLE_API_KEY	Google Generative AI API key	Required
LLM_TIMEOUT_SECONDS	Timeout for LLM operations	150
Contribution Guidelines

Fork the repository

Create a feature branch:

git checkout -b feature-name


Make your changes and add tests

Commit your changes:

git commit -am "Add feature"


Push to your branch:

git push origin feature-name


Submit a pull request

Development Setup

pip install -r requirements.txt
python -m pytest
black app.py

License

This project is licensed under the MIT License. See the LICENSE file for details.

Support and Troubleshooting

API Key Error

Verify the key is set correctly in .env

Ensure the key has appropriate permissions

File Upload Issues

Confirm the file is in a supported format

Ensure file size is within acceptable limits

Use UTF-8 encoding where possible

Analysis Timeout

Increase LLM_TIMEOUT_SECONDS in .env

Split large datasets into smaller files

Roadmap

Planned Features

Real-time collaboration

Advanced statistical modeling

Custom visualization templates

API rate limiting and caching

Multi-language support

Mobile application

Version History

v1.0.0 – Initial release with core analysis capabilities

v1.1.0 – Added web scraping functionality

v1.2.0 – Enhanced visualization options

Developed using FastAPI, LangChain, and Google Generative AI
