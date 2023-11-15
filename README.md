# Vegetable and Fruit Classifier with Nutrition Analysis

### Depolyed Model

![ezgif-3-4d61281ecf](https://github.com/AjayK47/Fruits-vegetables-Classification-and-Nutrition-analysisusing-Inception-V3/assets/88961945/404615ce-6b7f-45f1-b0d5-64b0e68b42b7)


## Overview

This project is a web application built using Flask and TensorFlow for classifying images of vegetables and fruits. It utilizes a fine-tuned InceptionV3 model to predict the type of vegetable or fruit from an uploaded image. Additionally, the application provides nutrition information for the predicted item based on a pre-loaded dataset.

The project also incorporates the Google Generative AI API (Palm) to generate interesting facts about the identified vegetable or fruit, making it an informative tool for nutrition specialists or anyone interested in learning more about different produce.

## Features

- **Image Classification:** Utilizes a pre-trained InceptionV3 model to classify vegetables and fruits.
- **Nutrition Analysis:** Retrieves nutrition information from a CSV dataset for the predicted item.
- **Fun Facts Generation:** Uses the Google Generative AI API to generate interesting facts about the identified item.
- **Web Interface:** Provides a simple web interface for users to upload images and receive predictions and nutrition information.

## Prerequisites

- Python 3.10
- Flask
- TensorFlow
- pandas
- google.generativeai

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/AjayK47/Fruits-vegetables-Classification-and-Nutrition-analysisusing-Inception-V3.git
    ```

2. Download the Food Dataset from Kaggle:
   - [Kaggle Food Image Dataset](https://www.kaggle.com/datasets/kritikseth/fruit-and-vegetable-image-recognition)
    ```

3. Run the Flask application:

    ```bash
    python app.py
    ```

4. Access the application at `http://localhost:5000` in your web browser.

## Usage

1. Upload an image of a vegetable or fruit.
2. Receive predictions about the item's type.
3. Explore nutrition information and fun facts.

## Future Enhancements

- [ ] Improve model accuracy through further training.
- [ ] Expand the dataset for more diverse predictions.
- [ ] Enhance the user interface for better user experience.
- [ ] Implement user authentication for personalized experiences.

## Contributions

Contributions are welcome! If you have ideas for improvements, open an issue or create a pull request.






