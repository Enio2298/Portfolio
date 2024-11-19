# Personal Portfolio Website

This is a **Streamlit-based portfolio** designed to showcase my skills, projects, and allow visitors to contact you. The project includes multiple pages that highlight my data projects and Python development work.

## Features

### 1. Home Page
- **Introduction**: A brief bio about Enio Rodríguez and his interests in programming, learning new technologies, and working on data-driven projects.
- **Contact Form**: A form where users can send messages via email using the `send_email` function.
- **Profile Image**: Displays a personal photo on the homepage.

### 2. Data Projects Page
- **Showcases Data-Driven Projects**: Displays a curated list of data-related projects.
- **Details**:
  - Title, image, description, and links to source code for each project.
  - Projects are displayed in two columns for better layout and readability.

### 3. Python Developer Projects Page
- **Python-Focused Portfolio**: Highlights Python development projects.
- **Details**:
  - Title, image, description, and source code link for each project.
  - Two-column layout to display projects.

## Installation

Follow these steps to set up and run the project:

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_folder>

    Install Dependencies: Ensure you have Python installed, then install the required Python libraries:

pip install streamlit pandas

Run the Application: Launch the Streamlit application using the terminal:

    streamlit run Home.py

Project Structure

Project/
├── Home.py                   # Homepage script
├── Data_Projects.py          # Script for the Data Projects page
├── Python_Developer_Projects.py  # Script for Python Developer Projects page
├── data.csv                  # CSV file containing Python developer projects
├── data1.csv                 # CSV file containing data projects
├── images/                   # Folder containing images for Python projects
├── images1/                  # Folder containing images for Data projects
├── Email.py                  # Script handling email functionality
├── requirements.txt          # List of required Python packages
└── README.md                 # Project documentation

Configuration
CSV Files

    data.csv: Contains the details for Python development projects.
    data1.csv: Contains the details for Data projects.
    Both files should follow this structure:

    title;image;description;url

Images

    Store project images in the images/ and images1/ directories as required.

Email Functionality

    SMTP Setup: Ensure your Email.py script is configured with valid SMTP credentials for sending emails.

Example CSV Format

Here’s an example of how the CSV files should be structured:

title;image;description;url
Project 1;project1.png;This is a description of Project 1.;https://github.com/username/project1
Project 2;project2.png;This is a description of Project 2.;https://github.com/username/project2

Usage

    Launch the application.
    Navigate between the pages using the Streamlit sidebar.
    View your data projects, Python development work, or contact you via the form on the homepage.

License

This project is open-source and available under the MIT License.
Contact

For inquiries or suggestions, feel free to reach out via the contact form on the homepage or email directly.


This `README.md` should make it clear how your project is structured and how others can use or contribute to it. Let me know if you need further adjustments!

