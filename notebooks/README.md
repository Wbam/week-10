# Brent Oil Prices Analysis and Dashboard

This project aims to analyze Brent oil prices and develop an interactive dashboard to visualize the results of the analysis. It includes three main tasks: defining the data analysis workflow, applying advanced statistical models, and creating a user-friendly dashboard using Flask and React.

## Table of Contents
- [Task 1: Data Analysis Workflow](#task-1-data-analysis-workflow)
- [Task 2: Analysis of Brent Oil Prices](#task-2-analysis-of-brent-oil-prices)
- [Task 3: Developing an Interactive Dashboard](#task-3-developing-an-interactive-dashboard)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [License](#license)

## Task 1: Data Analysis Workflow

### Objectives:
- Define the steps and processes involved in analyzing Brent oil prices data.
- Understand how the data is generated, sampled, and compiled.
- Identify model inputs, parameters, outputs, and any assumptions and limitations.
- Determine communication channels for conveying results to stakeholders.

### Key Steps:
1. **Workflow Definition**:
   - Outline analysis steps to achieve project objectives.
   - Clarify data generation and compilation processes.
   - Understand the model's inputs, parameters, and outputs.

2. **Model and Data Understanding**:
   - Familiarize with time series analysis models (e.g., ARIMA, GARCH).
   - Explain how these models relate to Brent oil prices analysis.
   - Describe expected outputs and limitations of the analysis.

## Task 2: Analysis of Brent Oil Prices

### Objectives:
- Build on the foundational understanding of time series analysis from Task 1.
- Analyze historical Brent oil prices data and explore factors influencing prices.

### Key Steps:
1. **Utilize Advanced Models**:
   - Apply VAR for multivariate analysis.
   - Use Markov-Switching ARIMA for regime-switching models.
   - Implement LSTM networks to capture complex patterns.

2. **Explore Influencing Factors**:
   - Analyze correlations with economic indicators (GDP, inflation, unemployment).
   - Assess impacts of technological changes and advancements in extraction technologies.
   - Investigate political and regulatory factors affecting oil prices.

3. **Model Adaptation**:
   - Extend analysis to different scenarios or related datasets (e.g., natural gas).
   - Integrate additional data sources for enhanced predictive power.
   - Validate model performance through backtesting and cross-validation.

## Task 3: Developing an Interactive Dashboard

### Objectives:
- Build a dashboard application using Flask (backend) and React (frontend) to visualize analysis results.

### Key Components:
1. **Backend (Flask)**:
   - Develop APIs to serve data from analysis results for the React frontend.
   - Handle requests for datasets, model outputs, and performance metrics.

2. **Frontend (React)**:
   - Create an intuitive interface to display analysis results.
   - Design interactive visualizations correlating events with oil price changes.
   - Include filtering, date ranges, and comparison features.

### Key Features:
- Present historical trends and forecasts.
- Visualize how specific events influence Brent oil prices.
- Enable filtering of data and selection of date ranges.
- Display key indicators like volatility and model accuracy metrics (e.g., RMSE, MAE).

## Technologies Used
- **Backend**: Flask, Pandas
- **Frontend**: React, Axios, Recharts/D3.js
- **Databases**: [Include any database if used]
- **Others**: [Include any other tools or libraries used]

## Setup Instructions

### Prerequisites:
- Python 3.x
- Node.js and npm

### Backend Setup:
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd backend
