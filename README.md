
# **Predictive Analysis API for Manufacturing Operations**

## Overview
This project is a RESTful API built using **FastAPI** that predicts machine downtime or production defects in manufacturing operations. By using machine learning (ML) models, this API allows users to upload manufacturing data, train a predictive model, and make real-time predictions based on key parameters like machine temperature and run time.

**Key Features:**
- Upload manufacturing data (CSV format).
- Train a machine learning model to predict machine downtime.
- Make predictions on downtime based on input parameters.

## Tech Stack
- **FastAPI** for building the RESTful API
- **scikit-learn** for the machine learning model
- **pandas** for data manipulation and processing
- **Uvicorn** for serving the FastAPI app
- **Python** for the backend

## Installation

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd <project-directory>
```

### Step 2: Install Dependencies
Use `requirements.txt` to install all necessary Python dependencies:
```bash
pip install -r requirements.txt
```

### Step 3: Run the API Server
After installing dependencies, run the FastAPI application with Uvicorn:
```bash
uvicorn main:app --reload
```
The API will be accessible at `http://127.0.0.1:8000`.

## Endpoints

### 1. **Upload Manufacturing Data**
- **URL**: `/upload`
- **Method**: `POST`
- **Description**: Upload a CSV file containing the manufacturing data (e.g., machine temperature, run time).
- **Request**: Form-data with a key `file` (must be a `.csv` file).
- **Example Request**:
  - **File**: `manufacturing_data.csv`
- **Response**:
  ```json
  {
    "message": "File uploaded successfully."
  }
  ```

### 2. **Train the Model**
- **URL**: `/train`
- **Method**: `POST`
- **Description**: Train the model on the uploaded dataset.
- **Response**:
  ```json
  {
    "message": "Model trained successfully.",
    "metrics": {
      "accuracy": 0.87,
      "f1_score": 0.85
    }
  }
  ```

### 3. **Predict Downtime**
- **URL**: `/predict`
- **Method**: `POST`
- **Description**: Make predictions based on input data (temperature, run time).
- **Request**: JSON payload with `Temperature` and `Run_Time` fields.
  - Example Input:
  ```json
  {
    "Temperature": 85,
    "Run_Time": 120
  }
  ```
- **Response**:
  ```json
  {
    "Downtime": "No",
    "Confidence": 0.87
  }
  ```

## Testing the API
You can test the API using **Postman** or **Swagger UI**.

### Swagger UI:
- Visit `http://127.0.0.1:8000/docs` in your browser to interact with the API. FastAPI automatically generates this interactive documentation.

### Postman:
1. Use the `/upload` endpoint to upload the `manufacturing_data.csv` file.
2. Use the `/train` endpoint to train the model.
3. Use the `/predict` endpoint to make predictions on downtime.

## Example Dataset

The dataset should include the following columns:
- `Machine_ID`: Unique identifier for the machine.
- `Temperature`: Operating temperature of the machine.
- `Run_Time`: Time the machine has been running.
- `Downtime_Flag`: Label indicating if downtime occurred (1 for Yes, 0 for No).

Example:
```csv
Machine_ID,Temperature,Run_Time,Downtime_Flag
1,80,120,1
2,70,100,0
3,90,150,1
4,85,110,0
5,75,130,1
```

## Model Explanation
The model uses **Logistic Regression** (by default) to predict machine downtime. Features like **Temperature** and **Run_Time** are used to train the model. You can experiment with other classifiers like **Random Forest** or **SVM** for better results.

## Future Improvements
- Implement **model hyperparameter tuning** for better accuracy.
- Add more **features** like maintenance history, machine age, etc.
- Deploy the API on a cloud platform like AWS or Heroku.

## License
This project is open-source and available under the MIT License.
