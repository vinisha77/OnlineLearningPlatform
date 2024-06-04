# Online Learning Platform

## Project Description
The objective of this project is to develop an innovative online learning platform that offers a wide range of courses across different domains, catering to the diverse learning needs of users. Inspired by popular platforms like Udemy and Pluralsight, the platform provides users with access to comprehensive course content, interactive learning materials, and engaging instructor-led sessions. Utilizing agile methodologies such as Scrum, the project will be executed in iterative sprints, focusing on collaboration, adaptability, and continuous improvement.

## Key Features
- **Comprehensive course catalog:** The platform features a diverse catalog of courses covering topics ranging from technology and business to arts and humanities, ensuring something for everyone.
- **Interactive learning experience:** Users have access to interactive course content, including video lectures, quizzes, assignments, and discussions, to enhance their learning experience.
- **Expert instructors:** Courses are taught by experienced instructors and industry experts, providing valuable insights and practical knowledge to learners.
- **Personalized learning paths:** Users have the flexibility to create personalized learning paths based on their interests, goals, and skill levels, enabling them to progress at their own pace.
- **Responsive design:** The website is optimized for various devices, including desktops, tablets, and smartphones, to accommodate users with different preferences and screen sizes.

## Agile (Scrum) Approach
- **Sprints:** The project is divided into short, manageable units of work called sprints, typically lasting 1-2 weeks.
- **Sprint planning:** At the beginning of each sprint, the team collaborates to define sprint goals and identify the tasks needed to achieve them.
- **Daily stand-up meetings:** Brief daily meetings are held to discuss progress, address challenges, and ensure alignment among team members.
- **Sprint review:** At the end of each sprint, the team demonstrates the completed work to stakeholders and gathers feedback for future improvements.
- **Sprint retrospective:** The team reflects on the sprint process, identifying what went well and what can be improved in future sprints.

## Technologies
- **Backend:** Django framework version 4+
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite or MongoDB (optional)
- **Version Control:** Git and GitHub
- **Project Management:** Trello or a similar tool

- ## Screenshots
<div style="display: flex; flex-wrap: wrap;">
    <img src="https://github.com/Olcaytp/OnlineLearningPlatform/blob/main/assets/homepage.png" alt="" width="300"/>
    <img src="https://github.com/Olcaytp/OnlineLearningPlatform/blob/main/assets/dashboard.png" alt="" width="300"/>
    <img src="https://github.com/Olcaytp/OnlineLearningPlatform/blob/main/assets/path.png" alt="" width="300"/>
</div>

## Installation
1. **Clone the repository:**
   git clone https://github.com/yourusername/online-learning-platform.git
   cd online-learning-platform

2. **Create a virtual environment and activate it:**
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install the required packages:**
pip install -r requirements.txt

4. **Apply migrations:**
python manage.py migrate

5. **Run the development server:**
python manage.py runserver

6. **Access the application:**
Open your web browser and go to http://127.0.0.1:8000.

## Usage
1. **Admin panel:**
 You can access the Django admin panel at http://127.0.0.1:8000/admin to manage courses, users, and other aspects of the platform.

 2. **User registration and login:**
 Users can register and log in to access personalized course recommendations and track their learning progress.
