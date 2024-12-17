# 🍽 ChefMate: Restaurant Clustering & Cooking Guide Application
ChefMate is a smart application that clusters and recommends restaurants according to user preferences, such as specific dishes or cuisines. It also includes a chef-like chatbot that helps users with recipes, making their cooking experience more enjoyable. The project utilizes machine learning and cloud computing technologies to provide tailored recommendations and culinary assistance.
## 🌟 Features of app
- *Personalized Recommendations:* Receive customized restaurant suggestions based on your preferred cuisines and dishes.  
- *Interactive Maps:* Discover restaurant locations through dynamic maps and ratings to enrich your experience.  
- *Cooking Assistance:* Interact with our chatbot for detailed, step-by-step cooking guidance and tips.  
- *Future Integrations:* Plans to integrate with food delivery platforms for effortless ordering.
## 🚀 Technologies Used
- *Streamlit:* Used to develop an intuitive and user-friendly web application.  
- *AWS Services:* Leveraging S3 for data storage, RDS for database management, and EC2 for deployment.  
- *Machine Learning:* Applying clustering algorithms to deliver accurate restaurant recommendations.  
- *Python:* The core programming language for development.  
- *Chatbot Integration:* Improving user engagement through conversational AI.
## 🗝 Key Features of the project
- *Data Storage:* AWS S3 was used to store project files and raw datasets.  
- *Data Preprocessing:* Applied data cleaning and preprocessing methods to prepare the data for training models.  
- *Database Management:* Integrated AWS RDS to store the cleaned data for efficient querying.  
- *Model Training:* Developed and trained various clustering models, including:  
- KMeans  
- DBSCAN  
- Agglomerative Clustering  
- Gaussian Mixture  

The models were evaluated using the silhouette score to identify the best performer.  
- *Application Development:* Built the ChefMate application with Streamlit to fulfill project requirements.  
- *Chatbot Integration:* Incorporated a Gemini generative AI role-based chatbot via API key for interactive assistance.  
- *Deployment:* Deployed the application on AWS to enable real-time user interaction.
# Project Structure
The project follows the directory structure outlined below:

### *Description of Each Component:*

- *ChefMate.py:*  
  The main entry point of the application. It initializes the Streamlit web app, processes user inputs, and displays restaurant recommendations along with chatbot interactions.  

- *requirements.txt:*  
  Contains a list of all the Python packages and dependencies needed to run the application. Dependencies can be installed using pip.  

- *ChefMate/:*  
  This directory holds datasets used in the project. The Zomato_cluster_data.csv file contains detailed restaurant information, including names, locations, cuisines, ratings, and other relevant details.  

- *models/:*  
  A directory for storing machine learning models. The kmeans_model.pkl file contains the trained clustering model used for grouping restaurants based on user preferences.  

- *ChefMate/:*  
  Includes scripts for data preprocessing and other utility functions.  

- *data_preprocessing.ipynb:*  
  A notebook for cleaning raw restaurant data, handling missing values, and converting JSON data into a structured format for analysis.  

- *data_cleaning.ipynb:*  
  Contains reusable utility functions for data manipulation and visualization tasks within the application.  

- *README.md:*  
  Provides detailed project documentation, including an overview, key features, installation steps, usage instructions, and contribution guidelines.
