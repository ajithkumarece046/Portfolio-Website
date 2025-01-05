import streamlit as st
import requests
from PIL import Image
import webbrowser

# Page configuration
st.set_page_config(page_title="Ajith Kumar", page_icon="📊", layout="wide")

# Function to fetch resume from GitHub
@st.cache_data
def fetch_resume(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        st.error("Failed to fetch the resume. Please check the URL.")
        return None

# URL to your resume on GitHub
resume_url = "https://github.com/ajithkumarece046/My_Profile/blob/main/Ajithkumar_DE_Resume.pdf"  # Replace with your raw GitHub URL.

# Load logo
try:
    logo = Image.open("D:\Website\Logo\profile.jpg")  # Replace 'logo.png' with your logo file path.
except FileNotFoundError:
    st.sidebar.error("Logo file not found. Please check the file path.")
    logo = None

st.sidebar.title("Ajith Kumar P")
st.sidebar.markdown("### Snowflake Data Engineer")

# Expander for contact details
with st.sidebar.expander("📬 Contact Us", expanded=False):
    # Load logos
    linkedin_logo = Image.open("D:\Website\Logo\linkedin.png")  # Replace with your LinkedIn logo path
    gmail_logo = Image.open("D:\Website\Logo\gmail.png")        # Replace with your Gmail logo path
    github_logo = Image.open("D:\Website\Logo\github.png")      # Replace with your GitHub logo path

    # Email
    st.image(gmail_logo, width=25)
    st.markdown("[ajithkumarece046@gmail.com](mailto:ajithkumarece046@gmail.com)")

    # LinkedIn
    st.image(linkedin_logo, width=25)
    st.markdown("[Ajith Kumar](https://www.linkedin.com/in/ajith-kumar/)")

    # GitHub
    st.image(github_logo, width=25)
    st.markdown("[GitHub: Ajith's Projects](https://github.com/ajithkumar)")
resume_content = fetch_resume(resume_url)
if resume_content:
    st.sidebar.download_button(
        label="Download Resume",
        data=resume_content,
        file_name="Ajith_Kumar_Resume.pdf",
        mime="application/pdf",
    )

# Main content
st.title("Ajith Kumar")
st.header("Summary")
st.write("""
A dynamic and results-oriented Snowflake Data Engineer with expertise in designing, developing, and implementing robust data engineering solutions. Proficient in Python, SQL, and PySpark for complex data workflows, and experienced in managing large-scale datasets in Snowflake for optimized analytical performance.
""")

st.header("Technical Skills")
tech_skills = """
| **Category**             | **Technologies**                                      |
|--------------------------|-----------------------------------------------------|
| **Databases**            | MySQL, SQL Server, PostgreSQL                       |
| **ETL/ELT Tools**        | Azure Databricks, Azure Data Factory, AWS Glue, DBT, Informatica |
| **Analytics Tools**      | Power BI, ThoughtSpot                               |
| **Data Warehousing**     | Snowflake                                           |
| **Cloud Computing**      | AWS, Microsoft Azure                                |
| **Programming Languages**| Python, SQL, C                                      |
| **Source Control**       | GitHub                                              |
| **CI/CD**                | Azure DevOps                                        |
"""

st.markdown(tech_skills, unsafe_allow_html=True)

st.header("Projects")
projects = [
    {
        "title": "E-commerce Store Performance Analytics",
        "description": "Implemented Python scripts to extract and transform data from various online store sources, loading it into SQL Server for further processing. Utilized Azure Data Factory (ADF) to orchestrate the movement of data from SQL Server to Azure container storage, ensuring seamless data transfer and synchronization. Loaded data from Azure container storage to Snowflake using external staging. Developed Power BI dashboards to visualize transformed data, providing stakeholders actionable insights into online store performance.",
        "tech_stack" : "Azure Data Factory, Snowflake, Power BI, Azure Storage Account",
    },
    {
        "title": "Deesha - Azure ETL Developer & Power BI Developer",
        "description": "Leveraged PySpark in Databricks for efficient extraction and processing of data from the Data Lake. Implemented Spark transformations for data cleansing, filtering, aggregation, and enrichment. Orchestrated the integration between Databricks and Azure SQL. Developed Power BI dashboards to provide actionable insights.",
        "tech_stack" : "Azure SQL, Azure Data Factory, Azure Databricks, Power BI, Azure Datalake Gen 2",
    },
    {
        "title": "Snowflake-Powered Market Research Analytics",
        "description": "Designed an efficient ELT pipeline leveraging AWS S3, Snowflake, and DBT for data processing. Utilized Snowpipe for automated data loading into Snowflake and created DBT models for transformations. Engineered an incremental model for processing data. Developed Power BI visualizations for insights into market trends.",
        "tech_stack" : "AWS S3, Snowflake, DBT, Power BI",
    },
    {
        "title": "Republic Services: US Ecology Data Migration",
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
st.header("Open-Source Contributions")
st.write("""
- **Spotify Data Scraper**: Developed a Python script utilizing the Spotipy library to scrape user playlist data and create a CSV file. 
- **YouTube Data Analysis**: Developed a YouTube data analysis project using Python, extracting video data using the Google Developer API, transforming it, and loading it into Snowflake. Visualized insights using Power BI.
- **ETL Testing Tool**: Developed a YouTube data analysis project using Python, extracting video data using the Google Developer API, transforming it, and loading it into Snowflake. Visualized insights using Power BI.
""")

st.header("Blogs & Publications")
st.write("""
- **[Streamlining Data Processing with AWS, Snowflake, and DBT](https://medium.com)**: Insights into ELT methodologies.
- **[Leveraging DBT on Snowflake with Docker](https://medium.com)**: Proficiency in Docker container deployment for DBT transformations.
""")
