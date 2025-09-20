# 💎 Diamond Price Prediction System

An interactive machine learning application built with Streamlit to predict diamond prices based on their characteristics.

## 📌 Overview

This application allows users to input various diamond features such as carat, cut, color, clarity, depth, table, and dimensions (x, y, z) to predict its price. The system uses a pre-trained machine learning model (`diamond_regressor.pkl`) and a `StandardScaler` (`diamond_scaler.pkl`) for preprocessing, both saved as pickle files.

## 🚀 Features

*   **Interactive Inputs**: Users can easily input diamond characteristics using Streamlit widgets.
*   **Real-time Prediction**: Get an instant predicted price for the diamond based on the inputs.
*   **Visual Aids**: Images illustrating GIA cut grading, diamond color priority, and clarity are displayed for user reference.
*   **Automated Preprocessing**: Input data is automatically scaled using a pre-fitted `StandardScaler` before prediction.

## 🛠️ Tech Stack

| Layer        | Tools Used          |
| :----------- | :------------------ |
| Frontend     | Streamlit           |
| Backend      | Python              |
| ML Inference | scikit-learn (pickle) |
| Data Handling| pandas              |
| UI Framework | Streamlit Widgets   |

## 🗂️ Project Structure
MultipleFiles/ ├── app.py ├── diamond_regressor.pkl ├── diamond_scaler.pkl ├── diamond-Clarity.png ├── diamond-color-priority.png ├── GIA-cut-grading.png ├── Diamonds J.ipynb └── diamonds.csv 


## 📋 Input Features

*   **Carat**: Weight of the diamond (float, 0.01 to 5.5)
*   **Cut**: Quality of the cut (categorical: 'Ideal', 'Premium', 'Good', 'Fair', 'Very Good')
*   **Color**: Diamond color grade (categorical: 'D', 'E', 'F', 'G', 'H', 'I', 'J')
*   **Clarity**: Diamond clarity grade (categorical: 'SI1', 'SI2', 'VS1', 'VS2', 'VVS1', 'VVS2', 'IF', 'FL')
*   **Depth**: Total depth percentage (float, 42 to 80)
*   **Table**: Table percentage (float, 42 to 95)
*   **X (mm)**: Length of the diamond in mm (float, 0.00 to 10.74)
*   **Y (mm)**: Width of the diamond in mm (float, 0.00 to 58.90)
*   **Z (mm)**: Depth of the diamond in mm (float, 0.00 to 31.80)

## 🧑‍💻 How to Run Locally

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/monparadharmik9/diamond-price-ml-app.git
    cd MultipleFiles
    ```

2.  **Install Dependencies**
    ```bash
    pip install streamlit pandas scikit-learn numpy
    ```
    *(Note: A `requirements.txt` file is not explicitly provided in the context, but these are the libraries identified from `app.py` and `Diamonds J.ipynb`.)*

3.  **Ensure Model and Scaler Files are Present**
    Make sure `diamond_regressor.pkl` and `diamond_scaler.pkl` are in the `MultipleFiles` directory. These are binary files and should be included in your repository.

4.  **Launch the App**
    ```bash
    streamlit run app.py
    ```
    Visit `http://localhost:8501` in your browser.

## 📈 Model Information

*   **Model Type**: Ridge Regression (as indicated by `rd = Ridge()` in `Diamonds J.ipynb`).
*   **Preprocessing**: `StandardScaler` is used to scale numerical input features. `LabelEncoder` is used for categorical features.
*   **Training Data**: The model is trained on the `diamonds.csv` dataset.
*   **Training and Evaluation**: The `Diamonds J.ipynb` notebook details the data loading, preprocessing (Label Encoding for categorical features, StandardScaler for numerical features), splitting into training/testing sets, and training of various regression models (Logistic Regression, Ridge, Lasso). The Ridge model achieved a score of approximately 0.885 on the test set.

## 🙏 Credits

*   **Developed by**: Dharmik Monpara
*   **Dataset Source**: `diamonds.csv` included in this repository.
