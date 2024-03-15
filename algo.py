import nltk
import random

# Download necessary NLTK packages
nltk.download('punkt')
nltk.download('stopwords')

# Define career paths and their corresponding skill sets
career_paths = {

    "Web Dev": ["HTML", "CSS", "JavaScript", "React", "Node.js","Bootstrap","Angular","js","tailwind","XML"],
    "Full Stack Developer":["HTML","CSS","Javascript","React","Angular","Vue.js","jQuery", "Bootstrap","Python","Java","PHP","Node.js","Ruby","Django","Flask","Spring","Laravel","Express","Ruby on Rails","Database","Relational Database","Mysql","PostgreSQL","MongoDB","Data Communication"],
    "Machine Learning Engineer": ["Python", "Statistics", "Machine Learning Algorithms", "Scikit-learn", "TensorFlow"],
    "Software Engineer": ["Programming Fundamentals", "Data Structures", "Algorithms", "System Design", "Java", "C++"],
    "Software Developer": ["Programming Fundamentals", "Object-Oriented Programming", "Software Development Lifecycle",
                           "Version Control", "Python", "Java"],
    "Python Developer": ["Python", "Data Structures", "Algorithms", "Libraries (NumPy, Pandas, Matplotlib)",
                         "Web Development Frameworks (Django, Flask)"]
}

"""
become = {
    "Machine Learning":{
        "Numpy (Python)":["INtro","Basic","Best"],
        "Pandas":["INtro of pandas","Basic of pandas","Best of pandas"],
        "Matplotlib":["INtro of Matplotlib","Basic Matplotlib","Best Matplotlib"]},{
    "Maths ":["INtro Maths","Basic Maths","Best"],"Statics":["INtro of Statics","Basic of Statics","Best of Statics"],"Linear Algebra":["INtro of Algerbra","Basic Algerbra","Best Algerbra"]},{
    "Supervised ":["INtro Supervised","Basic Supervised","Best Supervised"],"UnSupervised":["INtro of UnSupervised","Basic of UnSupervised","Best of UnSupervised"],"Scikit-learn":["INtro of Scikit-learn","Basic Scikit-learn","Best Scikit-learn"]
    },{
    "Deep Learning ":["INtro Deep Learning ","Basic Deep Learning ","Best Deep Learning "],"Backpropagation":["INtro of Backpropagation","Basic of Backpropagation","Best of Backpropagation"],"Activation Function":["INtro of Activation Function","Basic Activation Function","Best Activation Function"],"Architectures":["INtro of Architectures","Basic Architectures","Best Architectures"],"Tensorflow/Kearas":["INtro of Tensorflow","Basic Tensorflow","Best Tensorflow"]
    },

}"""

#by ai gen
become = {
    "Machine Learning": {
        "Numpy (Python)": ["INtro", "Basic", "Best"],
        "Pandas": ["INtro of pandas", "Basic of pandas", "Best of pandas"],
        "Matplotlib": ["INtro of Matplotlib", "Basic Matplotlib", "Best Matplotlib"]  # Colon added here
    },
    "Maths ": ["INtro Maths", "Basic Maths", "Best"],
    "Statics": ["INtro of Statics", "Basic of Statics", "Best of Statics"],
    "Linear Algebra": ["INtro of Algerbra", "Basic Algerbra", "Best Algerbra"],
    "Supervised ": ["INtro Supervised", "Basic Supervised", "Best Supervised"],
    "UnSupervised": ["INtro of UnSupervised", "Basic of Unsupervised", "Best of Unsupervised"],
    "Scikit-learn": ["INtro of Scikit-learn", "Basic Scikit-learn", "Best Scikit-learn"]
}

# Function to preprocess text (remove stopwords and punctuation)
"""def preprocess_text(text):
    text = text.lower()  # Convert text to lowercase
    tokens = nltk.word_tokenize(text)  # Tokenize the text
    stopwords = nltk.corpus.stopwords.words('english')  # Get stopwords from NLTK
    processed_text = [word for word in tokens if
                      word not in stopwords and word.isalpha()]  # Remove stopwords and punctuation
    return processed_text
"""

# Sample user input (replace with actual user input later)
def user_input():
  steam = input("Enter your Current Stream 1) Full Stack Developer , 2) Web Dev,  3) Machine Learning")
  print(steam)
  if steam=="1":
    print("In the user input")
    fullstack()

skill = []
def fullstack():
  q1 = int(input("Enter Skill Rate HTML 1 Hear the Name only 2 Little Bit Known 3 Basic Knowlege Can code 4 Intermediate 5 Expert "))
  skill.append(q1)
  q2 = int(input("Enter Skill Rate CSS 1 Hear the Name only 2 Little Bit Known 3 Basic Knowlege Can code 4 Intermediate 5 Expert "))
  skill.append(q2)
  q3 = int(input("Enter Skill Rate Javascript 1 Hear the Name only 2 Little Bit Known 3 Basic Knowlege Can code 4 Intermediate 5 Expert "))
  skill.append(q3)
  q4 = int(input("Enter Skill Rate React 1 Hear the Name only 2 Little Bit Known 3 Basic Knowlege Can code 4 Intermediate 5 Expert "))
  skill.append(q4)
  q5 = int(input("Enter Skill Rate Angular 1 Hear the Name only 2 Little Bit Known 3 Basic Knowlege Can code 4 Intermediate 5 Expert "))
  skill.append(q5)
  q6 = int(input("Enter Skill Rate Vue.js 1 Hear the Name only 2 Little Bit Known 3 Basic Knowlege Can code 4 Intermediate 5 Expert "))
  skill.append(q6)
  q7 = int(input("Enter Skill Rate jQuery 1 Hear the Name only 2 Little Bit Known 3 Basic Knowlege Can code 4 Intermediate 5 Expert "))
  skill.append(q7)
  q8 = int(input("Enter Skill Rate Bootstrap 1 Hear the Name only 2 Little Bit Known 3 Basic Knowlege Can code 4 Intermediate 5 Expert "))
  skill.append(q8)
  q9 = int(input("Enter Skill Rate Python 1 Hear the Name only 2 Little Bit Known 3 Basic Knowlege Can code 4 Intermediate 5 Expert "))
  skill.append(q9)
  q10 = int(input("Enter Skill Rate Java 1 Hear the Name only 2 Little Bit Known 3 Basic Knowlege Can code 4 Intermediate 5 Expert "))
  skill.append(q10)
  q11 = int(input("Enter Skill Rate PHP 1 Hear the Name only 2 Little Bit Known 3 Basic Knowlege Can code 4 Intermediate 5 Expert "))
  skill.append(q11)
  q12 = int(input("Enter Skill Rate Node.js 1 Hear the Name only 2 Little Bit Known 3 Basic Knowlege Can code 4 Intermediate 5 Expert "))
  skill.append(q12)
  q13 = int(input("Enter Skill Rate Ruby 1 Hear the Name only 2 Little Bit Known 3 Basic Knowlege Can code 4 Intermediate 5 Expert "))
  skill.append(q13)
  q14 = int(input("Enter Skill Rate Django 1 Hear the Name only 2 Little Bit Known 3 Basic Knowlege Can code 4 Intermediate 5 Expert "))
  skill.append(q14)
  q15 = int(input("Enter Skill Rate Flask 1 Hear the Name only 2 Little Bit Known 3 Basic Knowlege Can code 4 Intermediate 5 Expert "))
  skill.append(q15)
  q16 = int(input("Enter Skill Rate Spring 1 Hear the Name only 2 Little Bit Known 3 Basic Knowlege Can code 4 Intermediate 5 Expert "))
  skill.append(q16)
  q17 = int(input("Enter Skill Rate Laravel 1 Hear the Name only 2 Little Bit Known 3 Basic Knowlege Can code 4 Intermediate 5 Expert "))
  skill.append(q17)
  q18 = int(input("Enter Skill Rate Express 1 Hear the Name only 2 Little Bit Known 3 Basic Knowlege Can code 4 Intermediate 5 Expert "))
  skill.append(q18)
  q19 = int(input("Enter Skill Rate Ruby on Rails 1 Hear the Name only 2 Little Bit Known 3 Basic Knowlege Can code 4 Intermediate 5 Expert "))
  skill.append(q19)
  q20 = int(input("Enter Skill Rate Database 1 Hear the Name only 2 Little Bit Known 3 Basic Knowlege Can code 4 Intermediate 5 Expert "))
  skill.append(q20)
  q21 = int(input("Enter Skill Rate Relational Database 1 Hear the Name only 2 Little Bit Known 3 Basic Knowlege Can code 4 Intermediat)e 5 Expert "))
  skill.append(q21)
  q22 = int(input("Enter Skill Rate Mysql 1 Hear the Name only 2 Little Bit Known 3 Basic Knowlege Can code 4 Intermediate 5 Expert "))
  skill.append(q22)
  q23 = int(input("Enter Skill Rate PostgreSQL 1 Hear the Name only 2 Little Bit Known 3 Basic Knowlege Can code 4 Intermediate 5 Expert "))
  skill.append(q23)
  q24 = int(input("Enter Skill Rate MongoDB 1 Hear the Name only 2 Little Bit Known 3 Basic Knowlege Can code 4 Intermediate 5 Expert "))
  skill.append(q24)
  q25 = int(input("Enter Skill Rate Data Communication 1 Hear the Name only 2 Little Bit Known 3 Basic Knowlege Can code 4 Intermediate 5 Expert "))
  skill.append(q25)
  print(skill)
  calculate_points = sum(skill)
  if calculate_points/len(skill)>0.9:
    rate = 5
  elif (calculate_points/len(skill)>0.7) and  (calculate_points/len(skill)<0.9):
    rate = 4
  elif (calculate_points/len(skill)>0.5) and  (calculate_points/len(skill)<0.7):
    rate = 3
  elif (calculate_points/len(skill)>0.3) and  (calculate_points/len(skill)<0.5):
    rate = 2
  elif (calculate_points/len(skill)>0.1) and  (calculate_points/len(skill)<0.3):
    rate = 1
  else:
    rate = 0
  your_intereeted_field = input("Enter your interested field:- 1 Full Stack Developer 2 Machine Learning")
  if your_intereeted_field == "2":
    Provider_ML(skill,rate)


def Provider_ML(skill,rate):
  dict_car = list(career_paths.values())[1]
  dict_bec = list(become.values())[0]
  match_skills_both = any(value in dict_car for value in  dict_bec)
  if not match_skills_both:
    print("N o issue")
  else:
    rate = rate + 0.1


  if rate>=0.9:

  # Get the "Machine Learning" section
    machine_learning_section = become["Machine Learning"]

# Select a random number of keys between 2 and 3 (mostly 3)
    num_keys = random.choices([2, 3], weights=[1, 2])[0:2]  # Weighted random choice

# Randomly select the specified number of keys
    selected_keys = random.sample(list(machine_learning_section.keys()), num_keys)
    selected_data = {key: machine_learning_section[key] for key in selected_keys}

# Print the selected data
    print("Machine Learning:")
    for key, value in selected_data.items():
      print(f"\t- {key}: {', '.join(value)}")
  elif rate>=0.7 and rate<=0.9:

  # Get the "Machine Learning" section
    machine_learning_section = become["Machine Learning"]

# Select a random number of keys between 2 and 3 (mostly 3)
    num_keys = random.choices([1,2], weights=[1, 2])[0]  # Weighted random choice

# Randomly select the specified number of keys
    selected_keys = random.sample(list(machine_learning_section.keys()), num_keys)
    selected_data = {key: machine_learning_section[key] for key in selected_keys}

# Print the selected data
    print("Machine Learning:")
    for key, value in selected_data.items():
      print(f"\t- {key}: {', '.join(value)}")

user_input()




# Preprocess user text
#processed_user_text = preprocess_text(user_text)

"""
# Function to recommend a career path based on skill keywords in user text
def recommend_career_path(processed_text, career_paths):
    # Initialize empty dictionary to store skill counts for each career path
    skill_counts = {path: 0 for path in career_paths}

    # Iterate through user text and compare with skills in each career path
    for word in processed_user_text:
        for path, skills in career_paths.items():
            if word in skills:
                skill_counts[path] += 1  # Increment skill count for matching career path

    # Identify the career path with the highest skill count
    recommended_path = max(skill_counts, key=skill_counts.get)
    return recommended_path"""

# Get recommended career path based on user text
#recommended_career = recommend_career_path(processed_user_text, career_paths)
#print("Based on your experience, we recommend", recommended_career, "as a potential career path.")

