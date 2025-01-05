import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(page_title="My Portfolio", page_icon=":guardsman:", layout="wide")



def add_gif(gif_path):
    st.image(gif_path, use_container_width=True) 
# Sidebar content with custom HTML links
# with st.sidebar:
#     # Display the profile GIF
#     add_gif("Logo/Propic.gif")

#     # Add custom CSS for sidebar styling
#     st.markdown("""
#         <style>
#             /* Sidebar container styling */
#             section[data-testid="stSidebar"] {
#                 border: 3px solid red;  /* Blue border */
#                 border-radius: 10px;        /* Rounded corners */
#                 padding: 10px;             /* Inner spacing */
#                 background-color: #f9f9f9; /* Light background color */
#                 box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Subtle shadow */
#             }

#             /* Navigation links styling */
#             .nav-link {
#                 font-size: 18px;
#                 font-weight: bold;
#                 color: black;
#                 cursor: pointer;
#                 margin-bottom: 10px;
#                 text-decoration: none;
#                 display: block;
#             }
#             .nav-link:hover {
#                 color: #1e90ff; /* Highlight color on hover */
#             }
#         </style>
#         <!-- Sidebar navigation links -->
#         <a class="nav-link" href="#introduction">Introduction</a>
#         <a class="nav-link" href="#experience">Experience</a>
#         <a class="nav-link" href="#projects">Projects</a>
#         <a class="nav-link" href="#skills">Tech Skills</a>
#         <a class="nav-link" href="#Certifications">Certifications</a>
#         <a class="nav-link" href="#Open-Source Contributions">Open-Source Contributions</a>
#         <a class="nav-link" href="#Publications">Publications</a>
#         <a class="nav-link" href="#awards-and-achievements">Awards and Achievements</a>
#         <a class="nav-link" href="#contact">Contact</a>
#     """, unsafe_allow_html=True)

with st.sidebar:
    # Display the profile GIF
    st.image("Logo/Propic.gif", use_container_width=False, width=300)
    st.markdown("""
    <a class="nav-link" href="#introduction">Introduction</a>
    <a class="nav-link" href="#experience">Experience</a>
    <a class="nav-link" href="#projects">Projects</a>
    <a class="nav-link" href="#skills">Tech Skills</a>
    <a class="nav-link" href="#certifications">Certifications</a>
    <a class="nav-link" href="#open-source-contributions">Open-Source Contributions</a>
    <a class="nav-link" href="#publications">Publications</a>
    <a class="nav-link" href="#awards-and-achievements">Awards and Achievements</a>
    <a class="nav-link" href="#contact">Contact</a>
    """, unsafe_allow_html=True)


   
# Main content
st.title("Hello, I'm Ajith Kumar!")
st.write("Data Engineer | B.E Graduate")



# Function to add multi-color line
def add_multicolor_line():
    st.markdown("""
        <div style="height: 5px; background: linear-gradient(to right, #ff7f50, #1e90ff, #32cd32, #ff6347); margin: 20px 0;"></div>
    """, unsafe_allow_html=True)

def add_gif(gif_path):
    st.image(gif_path, use_container_width=True)    

# Section: Intro
st.markdown('<div id="introduction"></div>', unsafe_allow_html=True)
add_multicolor_line()      # Multi-color line
st.markdown("## Summary")  
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("""
    A dynamic and results-oriented Snowflake Data Engineer with expertise in designing, developing, and implementing robust data engineering solutions. Proficient in Python, SQL, and PySpark for complex data workflows, and experienced in managing large-scale datasets in Snowflake for optimized analytical performance.
    """)
with col2:
    add_gif("Logo/summary.gif")
# Section: Experience
st.markdown('<div id="experience"></div>', unsafe_allow_html=True)
add_multicolor_line()  # Multi-color line
st.markdown("## Experience")
col1, col2 = st.columns([2, 1])
with col1:

# List of Experiences
    experiences = [
    {
        "job_title": "**Associate Data Engineer - Blue.Cloud**",
        "company": "Blue.Cloud",
        "dates": "April 2023 - February 2024",
        "description": "Developed and deployed cloud-based data pipelines for the migration of data to Snowflake. Implemented ETL processes using ADF, designed and deployed DBT models, and handled data validation and transformation tasks. Leveraged SQL and Python to automate reporting processes and improve data accuracy.",
        "tech_stack": "Snowflake, Python, SQL, Azure Data Factory (ADF), Databricks, Power BI",
    },
    {
        "job_title": "**Data Engineer - Optisol Business Solutions**",
        "company": "Optisol Business Solutions",
        "dates": " March 2024 -  Present",
        "description": "Worked with cross-functional teams to design and implement scalable data pipelines. Developed and optimized SQL queries for large datasets and built data transformation models in Snowflake using DBT. Assisted in data integration from various sources to enhance business intelligence capabilities.",
        "tech_stack": "Snowflake, SQL, DBT, Power BI, Informatica, Azure Data Factory (ADF), Databricks, Denodo"
    },
    ]

    # Display experiences in expandable format
    for exp in experiences:
        with st.expander(exp["job_title"]):
            st.write(f"**Company**: {exp['company']}")
            st.write(f"**Dates**: {exp['dates']}")
            st.write(f"**Description**: {exp['description']}")
            st.write(f"**Tech Stack**: {exp['tech_stack']}")

with col2:
    add_gif("Logo/experience.gif")            

# Section: Projects
st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
add_multicolor_line()     # Multi-color line
st.markdown("## Projects") 
col1, col2 = st.columns([2, 1])
with col1: 

    projects = [
    {
        "title": "**E-commerce Store Performance Analytics**",
        "description": "Implemented Python scripts to extract and transform data from various online store sources, loading it into SQL Server for further processing. Utilized Azure Data Factory (ADF) to orchestrate the movement of data from SQL Server to Azure container storage, ensuring seamless data transfer and synchronization. Loaded data from Azure container storage to Snowflake using external staging. Developed Power BI dashboards to visualize transformed data, providing stakeholders actionable insights into online store performance.",
        "tech_stack" : "Azure Data Factory, Snowflake, Power BI, Azure Storage Account",
    },
    {
        "title": "**Deesha**",
        "description": "Leveraged PySpark in Databricks for efficient extraction and processing of data from the Data Lake. Implemented Spark transformations for data cleansing, filtering, aggregation, and enrichment. Orchestrated the integration between Databricks and Azure SQL. Developed Power BI dashboards to provide actionable insights.",
        "tech_stack" : "Azure SQL, Azure Data Factory, Azure Databricks, Power BI, Azure Datalake Gen 2",
    },
    {
        "title": "**Snowflake-Powered Market Research Analytics**",
        "description": "Designed an efficient ELT pipeline leveraging AWS S3, Snowflake, and DBT for data processing. Utilized Snowpipe for automated data loading into Snowflake and created DBT models for transformations. Engineered an incremental model for processing data. Developed Power BI visualizations for insights into market trends.",
        "tech_stack" : "AWS S3, Snowflake, DBT, Power BI",
    },
    {
        "title": "**Republic Services (US Ecology Data Migration)**",
        "description": "Developed and deployed Informatica IICS pipelines for incremental and full data loads into Snowflake. Managed deployment of table DDLs via ServiceNow. Designed DBT models incorporating naming conventions, deduplication, and transformation rules. Implemented DBT test cases for validation.",
        "tech_stack" : "SQL Server, Oracle Server, Informatica, Snowflake, DBT, Denodo",
    },
    ]

    for project in projects:
        with st.expander(project["title"]):
            st.write("**Description:**")
            st.write(project["description"])
            st.write("**Tech Stack:**")
            st.write(project["tech_stack"])
with col2:
    add_gif("Logo/projects1.gif")

# Section: Skills
st.markdown('<div id="skills"></div>', unsafe_allow_html=True)
add_multicolor_line()     # Multi-color line
st.markdown("## Tech Skills")
col1, col2 = st.columns([2, 1])
with col1:


    tech_skills = """
    | **Category**             | **Technologies**                                      |
    |--------------------------|-----------------------------------------------------|
    | **Databases**            | MySQL, SQL Server, PostgreSQL                       |
    | **ETL/ELT Tools**        | Azure Databricks, Azure Data Factory, AWS Glue, DBT, Informatica |
    | **Analytics Tools**      | Power BI, ThoughtSpot, Microsoft Fabric                             |
    | **Data Warehousing**     | Snowflake                                           |
    | **Cloud Computing**      | AWS, Microsoft Azure                                |
    | **Programming Languages**| Python, SQL, C                                      |
    | **Source Control**       | GitHub                                              |
    | **CI/CD**                | Azure DevOps                                        |
    | **Virtualization Tools**   | Denodo                                              |
    """

    st.markdown(tech_skills, unsafe_allow_html=True)
with col2:
    add_gif("Logo/ctechskills.gif")    

# Certifications
st.markdown('<div id="Certifications"></div>', unsafe_allow_html=True)
add_multicolor_line()     # Multi-color line
st.markdown("## Certifications")
col1, col2 = st.columns([2, 1])
with col1:
    
    st.markdown("""
    Here are some of the certifications I have earned:
    - **Snowflake Snow Pro Core Certified Professional**
    - **DBT Fundamentals**
    - **Databricks Lakehouse Fundamentals**
    - **SQL Certication by Hacker Rank**
    - **SQL Certification by Skillrack**
    - **Python Certification by Skillrack**
    - **Python Pandas Certificate by Kaggle**
    - **C Programming Certicate by Skillrack**                        
    """)

with col2:
    add_gif("Logo/certificate.gif")


# Open-Source Contributions
st.markdown('<div id="Open-Source Contributions"></div>', unsafe_allow_html=True)
add_multicolor_line()     # Multi-color line
st.header("Open-Source Contributions")
col1, col2 = st.columns([2, 1])
with col1:
  
    st.write("""
    - **Spotify Data Scraper**: Developed a Python script utilizing the Spotipy library to scrape user playlist data and create a CSV file. 
    - **YouTube Data Analysis**: Developed a YouTube data analysis project using Python, extracting video data using the Google Developer API, transforming it, and loading it into Snowflake. Visualized insights using Power BI.
    - **ETL Testing Tool**: Developed a YouTube data analysis project using Python, extracting video data using the Google Developer API, transforming it, and loading it into Snowflake. Visualized insights using Power BI.
    - **Pandas AI Streamlit App**: A user-friendly Streamlit application that integrates Pandas AI, allowing users to interact with CSV files using natural language. Users can upload a CSV file and ask questions like "What are the total sales for 2023?" or "List the top 5 performing categories," receiving accurate and insightful responses. This app simplifies data exploration and makes analytics accessible to everyone.
    """)

with col2:
    add_gif("Logo/open source projects.gif")

# Publications
st.markdown('<div id="Publications"></div>', unsafe_allow_html=True)
add_multicolor_line()     # Multi-color line
st.markdown("## Publications")
col1, col2 = st.columns([2, 1])
with col1:


    # Articles list
    articles = [
        {"name": "Leveraging DBT on Snowflake with Docker for Dynamic Transformation Pipelines", "url": "https://medium.com/optisol-datalabs/unlocking-data-potential-leveraging-dbt-on-snowflake-with-docker-for-dynamic-transformation-de4d05447b01"},
        {"name": "Streamlining Data Processing with AWS, Snowflake, and DBT : A Comprehensive Guide to ELT", "url": "https://medium.com/@ajithkumarece046/streamlining-data-processing-with-aws-snowflake-and-dbt-a-comprehensive-guide-to-elt-657e2b898e60"},
    ]

    st.markdown("""
        <style>
            ul.custom-list {
                padding-left: 10px;
                font-size: 16px;
                line-height: 1.6;
            }
            ul.custom-list li {
                margin-bottom: 10px;
            }
            ul.custom-list a {
                text-decoration: none;
                color: #1e90ff;
            }
            ul.custom-list a:hover {
                text-decoration: underline;
            }
        </style>
        <ul class="custom-list">
    """, unsafe_allow_html=True)

    # Adding articles dynamically
    for article in articles:
        st.markdown(f"""
            <li>
                <span>{article['name']}</span>
                - <a href="{article['url']}" target="_blank">View</a>
            </li>
        """, unsafe_allow_html=True)

    # Closing the unordered list
    st.markdown("</ul>", unsafe_allow_html=True)

with col2:
    add_gif("Logo/cblog.gif")

# Awards & Achievements


# st.header("Awards and Achievements")
# add_multicolor_line()     # Multi-color line
# st.markdown('<a id="awards-and-achievements"></a>', unsafe_allow_html=True)  # Anchor for navigation

# # Display certificate with description
# col1, col2 = st.columns([1, 2])  # Split content into two columns: image and description

# with col1:
#     # Replace with the actual path to your certificate image
#     certificate_image = Image.open("certificates/award_certificate.png")  
#     st.image(certificate_image, caption="Certificate of Excellence", use_container_width=True)

# with col2:
#     st.markdown("""
#         ### Award Title: Certificate of Excellence
#         **Description:** Received the Certificate of Excellence for outstanding contributions to [Project/Domain]. Recognized for exceptional performance in driving innovative solutions and achieving key milestones.  
#         **Year:** 2024  
#     """)    

add_multicolor_line()
st.header("Awards and Achievements")
st.markdown('<a id="awards-and-achievements"></a>', unsafe_allow_html=True)  # Anchor for navigation


col1, col2 = st.columns([2, 1])

with col2:
    st.image("Logo/s_achivements.gif", use_container_width=True)  


with col1:

    # Example Certificate with Expander
    with st.expander("🏆 Certificate of Excellence (2024)", expanded=False):
        col1, col2 = st.columns([1, 2])  # Split content into two columns: image and description
        
        with col1:
            # Replace with the actual path to your certificate image
            certificate_image = Image.open("Logo/spotaward.jpg")  
            st.image(certificate_image, caption="Certificate of Excellence", use_container_width=True)

        with col2:
            st.markdown("""
                ### Award Title: Spot Award
                - **Description:** For your outstanding performance so far in Deesha, we would like to express our deep appreciation. Your dedication, expertise, and consistent efforts have been instrumental in driving the project's progress. We look forward to your continued contributions as we move toward achieving our goals.
                - **Year:** 2024  
            """)

          

    # # Add more certificates by repeating the expander structure
    # with st.expander("🎖 Outstanding Performer Award (2023)", expanded=False):
    #     col1, col2 = st.columns([1, 2])
        
    #     with col1:
    #         certificate_image = Image.open("certificates/outstanding_performer.png")  
    #         st.image(certificate_image, caption="Outstanding Performer Award", use_container_width=True)

    #     with col2:
    #         st.markdown("""
    #             ### Award Title: Outstanding Performer Award
    #             **Description:** Recognized as the Outstanding Performer for exceptional contributions to team success and innovation.  
    #             **Year:** 2023  
    #         """)


# Section: Contact
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
add_multicolor_line()  # Multi-color line
st.markdown("## Contact")

col1, col2 = st.columns([2, 1])
with col1:
    st.write("""
    I would love to connect with you! Feel free to reach out if you have any questions, collaboration opportunities, 
    or simply want to discuss data engineering, cloud technologies, or any of my projects. 

    You can contact me through the following platforms:
    """)

    st.markdown("""
        <div style="display: flex; justify-content: space-around; font-size: 30px; text-align: center;">
            <a href="https://www.linkedin.com/in/ajith-kumar-palanikumar-158226218" target="_blank" style="margin: 0 10px;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/LinkedIn_icon.svg/108px-LinkedIn_icon.svg.png" width="40" style="cursor: pointer;"/>
            </a>
            <a href="mailto:ajithkumarece046@gmail.com" style="margin: 0 10px;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/7/7e/Gmail_icon_%282020%29.svg" width="40" style="cursor: pointer;"/>
            </a>
            <a href="https://github.com/ajithkumarece046" target="_blank" style="margin: 0 10px;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" width="40" style="cursor: pointer;"/>
            </a>
        </div>
    """, unsafe_allow_html=True)

with col2:
    add_gif("Logo/contact.gif")



st.markdown("""
<style>
/* Main Application Container */
div[data-testid="stAppViewContainer"] {
    border: 1px solid transparent;
    border-radius: 15px;
    background-image: linear-gradient(white, white),
                      linear-gradient(to right, #ff7f50, #1e90ff, #32cd32, #ff69b4);
    background-origin: border-box;
    background-clip: content-box, border-box;
    padding: 20px;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
}

/* Sidebar Container */
[data-testid="stSidebar"] {
    width: 300px; /* Fixed width to prevent resizing */
    min-width: 300px; /* Ensure sidebar doesn't shrink */
    max-width: 300px; /* Ensure sidebar doesn't expand */
    padding: 20px; /* Consistent padding */
    border-right: none; /* Prevent duplicate borders */
}

/* Navigation Links */
.nav-link {
    display: block;
    margin: 10px 0;
    text-decoration: none;
    font-size: 16px;
    font-weight: bold;
    color: #333;
    text-align: left;
}

.nav-link:hover {
    color: #1e90ff;
    text-decoration: underline;
}

/* Profile Picture */
img {
    display: block;
    margin: 0 auto;
    border-radius: 50%;
    width: 100px;
    height: auto;
}

/* Section Headers */
h2 {
    color: black;
    font-family: 'Arial', sans-serif;
}

/* General Text */
p {
    font-size: 16px;
    line-height: 1.6;
    color: #333;
}
</style>
""", unsafe_allow_html=True)
