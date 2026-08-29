from pydantic import BaseModel

class Experience(BaseModel):
    companyName: str
    jobTitle: str
    startTime: str
    endTime: str
    location: str
    bullets: list[str]

experiences = [
    Experience(
        companyName="AUSTRALIAN NATIONAL UNIVERSITY",
        jobTitle="Course Tutor (COMP1110/COMP6710/COMP7710)",
        startTime="July 2025",
        endTime="Present",
        location="Canberra, ACT",
        bullets=[
            "Helped design coding tasks, evaluation criteria, rubrics, and marking workflows for programming assignments and final projects.",
            "Adapted communication and evaluation approaches for students with varying English proficiency and programming backgrounds, simplifying phrasing and using alternative comprehension checks while maintaining fairness and consistent assessment standards.",
            "Supported students in building programming confidence and problem-solving skills by delivering detailed assignment feedback and guiding them on how to improve future work.",
            "Collaborated closely with fellow tutors, demonstrating teamwork and clear communication in a high-interaction academic environment."
        ]
    ),
    Experience(
        companyName="EPAM SYSTEMS INC.",
        jobTitle="Software Engineer",
        startTime="September 2019",
        endTime="June 2024",
        location="Shenzhen, China",
        bullets=[
            "Delivered 30+ front-end and back-end projects for UBS wealth management applications, including 2 projects independently owned end-to-end from requirements through production deployment.",
            "Modernized legacy JSP-based UI (table-based layout) into React components, improving maintainability and user experience.",
            "Worked directly with international stakeholders and client technical teams across the UK, Luxembourg, Monaco, Spain and other regions to clarify business requirements, validate implementation details, support testing, and resolve issues during release and production deployment.",
            "Wrote and maintained SQL queries to enforce data integrity across multiple database tables, identifying and resolving cross-table inconsistencies as part of backend data remediation workflows.",
            "Reduced manual credential handling and improved deployment repeatability by migrating configuration credentials to a secure secrets vault and automating secure retrieval, encryption, and injection of secrets into application configuration files." ,
            "Wrote Python scripts to automate password rotation across deployed application config files on the server, encrypting existing plaintext credentials as part of the secrets vault migration.",
            "Migrated an enterprise-level Java application from IBM WebSphere to Apache and Tomcat, managing 20+ tickets concurrently to coordinate database migration and server setup, and handling configuration file and proxy adjustments on new servers.",
            "Produced clear user and technical guides adopted by teams in Singapore and Switzerland, improving knowledge transfer, support efficiency, and consistency across distributed teams."
        ]
    ),
]