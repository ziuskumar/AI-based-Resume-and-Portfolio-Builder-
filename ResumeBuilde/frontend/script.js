function generateResume() {
    const data = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        phone: document.getElementById("phone").value,
        job_role: document.getElementById("job_role").value,
        objective: document.getElementById("objective").value,
        education: document.getElementById("education").value,
        skills: document.getElementById("skills").value,
        projects: document.getElementById("projects").value,
        certifications: document.getElementById("certifications").value
    };

    fetch("http://127.0.0.1:5000/generate", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(result => {
        document.getElementById("resume").textContent = result.resume;
        document.getElementById("cover").textContent = result.cover_letter;
    });
}
