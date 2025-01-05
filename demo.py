import streamlit as st
from PIL import Image

# Page configuration
st.set_page_config(page_title="Ajith Kumar Portfolio", page_icon="📊", layout="wide")

# Load logo
logo = Image.open("D:\Website\Logo\profile.jpg")  # Replace 'logo.png' with your logo file path.

# Sidebar
st.sidebar.image(logo, use_column_width=True)
st.sidebar.title("Ajith Kumar")
st.sidebar.markdown("### Snowflake Data Engineer")
st.sidebar.markdown("**Email:** [ajithkumarece046@gmail.com](mailto:ajithkumarece046@gmail.com)")
st.sidebar.markdown("**LinkedIn:** [Ajith Kumar](https://www.linkedin.com/in/ajith-kumar/)")
st.sidebar.markdown("**GitHub:** [Ajith's Projects](https://github.com/ajithkumar)")
st.sidebar.markdown("**Certifications:** SnowPro, DBT Learn Fundamentals")
st.sidebar.download_button(
    label="Download Resume",
    data=open("Ajith_Kumar_Resume.pdf", "rb"),  # Replace with your resume file path.
    file_name="Ajith_Kumar_Resume.pdf",
    mime="application/pdf",
)

# Main content
st.title("Ajith Kumar Portfolio")
st.header("Summary")
st.write("""
A dynamic and results-oriented Snowflake Data Engineer with expertise in designing, developing, and implementing robust data engineering solutions. Proficient in Python, SQL, and PySpark for complex data workflows, and experienced in managing large-scale datasets in Snowflake for optimized analytical performance.
""")

st.header("Technical Skills")
st.write("""
- **Databases:** MySQL, SQL Server, PostgreSQL
- **ETL/ELT Tools:** Azure Databricks, Azure Data Factory, AWS Glue, DBT, Informatica
- **Analytics Tools:** Power BI, ThoughtSpot
- **Data Warehousing:** Snowflake
- **Cloud Computing:** AWS, Microsoft Azure
- **Programming Languages:** Python, SQL, C
- **Source Control:** GitHub
- **CI/CD:** Azure DevOps
""")

st.header("Projects")
projects = [
    {
        "title": "E-commerce Store Performance Analytics",
        "description": "Implemented Python scripts to extract and transform data from various online store sources, loading it into SQL Server for further processing. Utilized Azure Data Factory (ADF) to orchestrate the movement of data from SQL Server to Azure container storage, ensuring seamless data transfer and synchronization. Loaded data from Azure container storage to Snowflake using external staging. Developed Power BI dashboards to visualize transformed data, providing stakeholders actionable insights into online store performance.",
    },
    {
        "title": "Deesha - Azure ETL Developer & Power BI Developer",
        "description": "Leveraged PySpark in Databricks for efficient extraction and processing of data from the Data Lake. Implemented Spark transformations for data cleansing, filtering, aggregation, and enrichment. Orchestrated the integration between Databricks and Azure SQL. Developed Power BI dashboards to provide actionable insights.",
    },
    {
        "title": "Snowflake-Powered Market Research Analytics",
        "description": "Designed an efficient ELT pipeline leveraging AWS S3, Snowflake, and DBT for data processing. Utilized Snowpipe for automated data loading into Snowflake and created DBT models for transformations. Engineered an incremental model for processing data. Developed Power BI visualizations for insights into market trends.",
    },
    {
        "title": "Republic Services: US Ecology Data Migration",
        "description": "Developed and deployed Informatica IICS pipelines for incremental and full data loads into Snowflake. Managed deployment of table DDLs via ServiceNow. Designed DBT models incorporating naming conventions, deduplication, and transformation rules. Implemented DBT test cases for validation.",
    },
]

for idx, project in enumerate(projects):
    if st.button(f"Project: {project['title']}"):
        st.write(f"**Description:** {project['description']}")

st.header("Open-Source Contributions")
st.write("""
- **Python Script for Spotify Data Scraping**: Developed a Python script to scrape user playlist data.
- **YouTube Data Analysis**: Extracted video data using Google Developer API, loaded it into Snowflake, and visualized insights with Power BI.
- **ETL Testing Tool**: Created a Streamlit-based tool to validate data counts, columns, data types, and constraints.
""")

st.header("Blogs & Publications")
st.write("""
- **[Streamlining Data Processing with AWS, Snowflake, and DBT](https://medium.com)**: Insights into ELT methodologies.
- **[Leveraging DBT on Snowflake with Docker](https://medium.com)**: Proficiency in Docker container deployment for DBT transformations.
""")
