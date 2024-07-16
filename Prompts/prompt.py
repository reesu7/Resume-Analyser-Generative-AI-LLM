def input_prompt(text_content, job_description):
    text = f"""
Hey, act like a skilled or highly experienced ATS (Application Tracking System) with a deep understanding of software
engineering, data science, software development, data analysis, big data engineering, high-frequency trading,
and the tech field in general. Your task is to evaluate my resume based on the given
job description and provide me suggestion and shortcomings  for improving the resume.

Resume:
{text_content}

Job Description:
{job_description}
"""
    return text
