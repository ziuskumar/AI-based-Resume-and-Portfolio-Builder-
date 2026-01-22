def generate_resume(data):
    resume = f"""
    {data['name']}
    Email: {data['email']} | Phone: {data['phone']}

    CAREER OBJECTIVE
    {data['objective']}

    EDUCATION
    {data['education']}

    SKILLS
    {data['skills']}

    PROJECTS
    {data['projects']}

    CERTIFICATIONS
    {data['certifications']}
    """

    cover_letter = f"""
    Dear Hiring Manager,

    I am writing to apply for the position of {data['job_role']}.
    I have strong skills in {data['skills']} and hands-on experience
    through projects such as {data['projects']}.

    I am highly motivated and eager to contribute to your organization.

    Sincerely,
    {data['name']}
    """

    return resume, cover_letter
