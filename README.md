# SMS Spam Detection
A model for SMS spam detection using machine learning is designed to automatically identify and filter out spam messages from legitimate ones in a text messaging system. Detecting spam SMS messages typically involves training a model on a dataset of labeled messages i.e. spam or ham(not spam). For building this model, I conducted data analysis by extracting features from the text which was gathered from a diverse dataset from Kaggle, such as word frequency, length, and presence of specific keywords. I applied Naive Bayes Machine Learning Algorithm for performing predictive analysis on the data, to classify incoming messages as spam or ham.

I performed the following operations for building this model:

Data Analysis- By gathering a dataset from Kaggle, containing a large number of sms messages, including both spam and ham messages. This dataset serves as the foundation for training and evaluating the model.

Feature Extraction- Assigning weights to words based on their importance in distinguishing spam from ham i.e. TF-IDF (Term Frequency-Inverse Document Frequency).

Naive Bayes algorithm- I used naive bayes algorithm for performing predictive analysis on the dataset. Naive Bayes is known for its simplicity, speed, and effectiveness on text data, making it a popular choice for tasks like spam detection, text classification, and sentiment analysis.

Model Training and Evaluation- Split the dataset into training and testing sets to train and evaluate the model's performance, then, train the selected model on the training data, optimizing its parameters to achieve the best results. Assess the model's performance using evaluation metrics such as accuracy, precision on the test dataset.

Streamlit Python Library- For providing user accessibility, I employed streamlit to create an interactive web application. This library helps in providing a user-friendly interface which takes input sms messages from the user for predicting whether the messages is spam or ham.

The model is modified to a web application to operate in real time, providing quick result to the user, enhancing user experience and efficiency.
