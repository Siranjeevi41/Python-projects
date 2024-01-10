import pandas as pd
import faker
import random
import lorem
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# Instantiate the Faker generator
fake = faker.Faker()

# Create a function to generate fake news articles
def generate_fake_news(num_samples, label):
    fake_news = []
    for _ in range(num_samples):
        title = fake.sentence()
        content = lorem.paragraph()
        fake_news.append((title, content, label))
    return fake_news

# Replace with actual news data
def generate_real_news(num_samples, label):
    # You might want to replace this with actual news data
    real_news = [
        ("Real News Title 1", "Real news content 1.", label),
        ("Real News Title 2", "Real news content 2.", label),
        # Add more real news samples as needed
    ]
    return real_news[:num_samples]

# Generate fake news samples
fake_news_data = generate_fake_news(num_samples=500, label=1)

# Generate real news samples
real_news_data = generate_real_news(num_samples=500, label=0)

# Combine the fake and real news samples
data = fake_news_data + real_news_data

# Shuffle the dataset
random.shuffle(data)

# Create a DataFrame
df = pd.DataFrame(data, columns=['Title', 'Content', 'Label'])

# Split the dataset into training and testing sets
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

# Extract features using TF-IDF
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
X_train = tfidf_vectorizer.fit_transform(train_df['Content'])
X_test = tfidf_vectorizer.transform(test_df['Content'])

# Train a simple SVM classifier
svm_classifier = SVC(kernel='linear')
svm_classifier.fit(X_train, train_df['Label'])

# Predict on the test set
predictions = svm_classifier.predict(X_test)

# Calculate accuracy and display
accuracy = accuracy_score(test_df['Label'], predictions)
print(f'Accuracy: {accuracy * 100:.2f}%')

# Display classification report
print('\nClassification Report:\n', classification_report(test_df['Label'], predictions))
