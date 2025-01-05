import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(page_title="My Portfolio", page_icon=":guardsman:", layout="wide")

# Sidebar content with custom HTML links
with st.sidebar:
    # Make sure this path is accessible or replace with an online URL for the image
    st.image("D:/Website/Logo/profile.jpg", width=200)  # Add your profile picture
    st.markdown("""
        <style>
            .nav-link {
                font-size: 18px;
                font-weight: bold;
                color: #555;
                cursor: pointer;
                margin-bottom: 10px;
                text-decoration: none;
                display: block;  /* Ensures each link appears on a new line */
            }
            .nav-link:hover {
                color: #1e90ff;
            }
        </style>
        <a class="nav-link" href="#introduction">Introduction</a>
        <a class="nav-link" href="#projects">Projects</a>
        <a class="nav-link" href="#skills">Skills</a>
        <a class="nav-link" href="#Certifications">Certifications</a>
        <a class="nav-link" href="#Open-Source Contributions">Open-Source Contributions</a>
        <a class="nav-link" href="#Publications">Publications</a>
        <a class="nav-link" href="#contact">Contact</a>
    """, unsafe_allow_html=True)

# Main content
st.title("Hello, I'm Ajith Kumar!")
st.write("Data Engineer | B.E Graduate")

# Section: Intro
st.markdown('<div id="introduction"></div>', unsafe_allow_html=True)
st.markdown("## Summary")
st.markdown("""
    A dynamic and results-oriented Snowflake Data Engineer with expertise in designing, developing, and implementing robust data engineering solutions. Proficient in Python, SQL, and PySpark for complex data workflows, and experienced in managing large-scale datasets in Snowflake for optimized analytical performance.
""")

# Section: Projects
st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
st.markdown("## Projects")
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

# Section: Skills
st.markdown('<div id="skills"></div>', unsafe_allow_html=True)
st.markdown("## Tech Skills")
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

# Certifications
st.markdown('<div id="Certifications"></div>', unsafe_allow_html=True)
st.markdown("## Certifications")
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

# Open-Source Contributions
st.markdown('<div id="Open-Source Contributions"></div>', unsafe_allow_html=True)
st.header("Open-Source Contributions")
st.write("""
- **Spotify Data Scraper**: Developed a Python script utilizing the Spotipy library to scrape user playlist data and create a CSV file. 
- **YouTube Data Analysis**: Developed a YouTube data analysis project using Python, extracting video data using the Google Developer API, transforming it, and loading it into Snowflake. Visualized insights using Power BI.
- **ETL Testing Tool**: Developed a YouTube data analysis project using Python, extracting video data using the Google Developer API, transforming it, and loading it into Snowflake. Visualized insights using Power BI.
- **Pandas AI Streamlit App**: A user-friendly Streamlit application that integrates Pandas AI, allowing users to interact with CSV files using natural language. Users can upload a CSV file and ask questions like "What are the total sales for 2023?" or "List the top 5 performing categories," receiving accurate and insightful responses. This app simplifies data exploration and makes analytics accessible to everyone.
""")

# Publications
st.markdown('<div id="Publications"></div>', unsafe_allow_html=True)
st.markdown("## Publications")

# Articles list
articles = [
    {"name": "Leveraging DBT on Snowflake with Docker for Dynamic Transformation Pipelines", "url": "https://medium.com/optisol-datalabs/unlocking-data-potential-leveraging-dbt-on-snowflake-with-docker-for-dynamic-transformation-de4d05447b01"},
    {"name": "Streamlining Data Processing with AWS, Snowflake, and DBT : A Comprehensive Guide to ELT", "url": "https://medium.com/@ajithkumarece046/streamlining-data-processing-with-aws-snowflake-and-dbt-a-comprehensive-guide-to-elt-657e2b898e60"},
]

st.markdown("""
    <style>
        ul.custom-list {
            padding-left: 10px; /* Adjust this value to move bullet points left or right */
            font-size: 16px; /* Optional: Adjust font size */
            line-height: 1.6; /* Optional: Adjust line spacing */
        }
        ul.custom-list li {
            margin-bottom: 10px; /* Add space between items */
        }
        ul.custom-list a {
            text-decoration: none; /* Remove underline from links */
            color: #1e90ff; /* Optional: Change link color */
        }
        ul.custom-list a:hover {
            text-decoration: underline; /* Optional: Add underline on hover */
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


# Section: Contact
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.markdown("## Contact")
# st.markdown("""
#     Feel free to reach out to me via email at [ajithkumarece046@gmail.com](mailto:ajithkumarece046@gmail.com).
# """)

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