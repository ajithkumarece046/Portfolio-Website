import streamlit as st
from PIL import Image
import requests

# Set page configuration
st.set_page_config(
    page_title="Portfolio",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Load images
profile_image = Image.open("D:\Website\Logo\profile.jpg")  # Replace with actual path
developer_image = Image.open("D:\Website\Logo\profile.jpg")  # Replace with actual path

# Sidebar
st.sidebar.title("Portfolio Sections")
sections = ["Introduction", "Skills", "Projects", "Contact"]
selected_section = st.sidebar.radio("Navigate to", sections)

# Introduction Section
if selected_section == "Introduction":
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(profile_image, use_column_width=True, caption="Your Name")
    with col2:
        st.title("Hello, I'm Ajith Kumar!")
        st.write(
            """
            **Data Engineer** | B.E Graduate

            A dynamic and results-oriented Snowflake Data Engineer with expertise in designing, developing, and implementing robust data engineering solutions. Proficient in Python, SQL, and PySpark for complex data workflows, and experienced in managing large-scale datasets in Snowflake for optimized analytical performance.

            """
        )
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
        resume_url = "https://github.com/ajithkumarece046/My_Profile/blob/main/Ajithkumar_DE_Resume.pdf"
        resume_content = fetch_resume(resume_url)
        if resume_content:
            st.sidebar.download_button(
            label="Download Resume",
            data=resume_content,
            file_name="Ajith_Kumar_Resume.pdf",
            mime="application/pdf",
            )
# Skills Section
elif selected_section == "Skills":
    st.title("Skills !!!")
    st.markdown("<hr style='border-top: 3px solid #FF5733;'>", unsafe_allow_html=True)

    # Skills content
    st.subheader("Languages:")
    st.write("Python, C, SQL")

    st.subheader("Databases:")
    st.write("Azure SQL, SQL Server, PostgresSQL")

    st.subheader("Cloud:")
    st.write("Microsoft Azure , AWS ")

    st.subheader("Data Warehouse & Virtualization Tools:")
    st.write("Snowflake, Databricks, Azure Synapse Analytics, Denodo")

    st.subheader("Reporting Tools:")
    st.write("Power BI, Microsoft Fabric, Thoughtspot")

    st.subheader("Frameworks:")
    st.write("Streamlit")

    st.subheader("Soft Skills:")
    st.write(
        """
        Leadership, Creativity, Writing, Public Speaking,  
        Time Management, Problem Solving, Communications
        """
    )
    st.image(developer_image, use_column_width=True)

# Projects Section
elif selected_section == "Projects":
    st.title("Projects !!!")
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

# Contact Section
elif selected_section == "Contact":
    st.title("Get in Touch!")
    st.markdown("<hr style='border-top: 3px solid #FFC300;'>", unsafe_allow_html=True)

    st.write(
        """
        📧 Email: [your-email@example.com](mailto:your-email@example.com)  
        🌐 LinkedIn: [Your LinkedIn](https://linkedin.com/in/your-profile)  
        📞 Phone: +1 (234) 567-890  
        """
    )

# Footer
st.markdown(
    """
    <style>
    footer {
        visibility: hidden;
    }
    footer:after {
        content: 'Created with ❤️ in Streamlit | © 2025 Your Name';
        visibility: visible;
        display: block;
        position: relative;
        color: #000;
        padding: 10px;
        top: 2px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
