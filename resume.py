import csv
import json
import yaml
import xml.etree.ElementTree as ET

def create_resume():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    skills = input("Enter your skills (comma-separated): ")
    experience = input("Enter your experience: ")
    education = input("Enter your education: ")

    resume = {
        "name": name,
        "email": email,
        "phone": phone,
        "skills": skills.split(","),
        "experience": experience,
        "education": education
    }

    return resume

def save_as_csv(resume):
    with open("resume.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(resume.keys())
        writer.writerow(resume.values())
    print("Resume saved as CSV.")

def save_as_json(resume):
    with open("resume.json", "w") as f:
        json.dump(resume, f, indent=4)
    print("Resume saved as JSON.")

def save_as_yaml(resume):
    with open("resume.yaml", "w") as f:
        yaml.dump(resume, f, default_flow_style=False)
    print("Resume saved as YAML.")

def save_as_xml(resume):
    root = ET.Element("resume")
    for key, value in resume.items():
        element = ET.SubElement(root, key)
        element.text = str(value)

    tree = ET.ElementTree(root)
    tree.write("resume.xml", encoding="utf-8", xml_declaration=True)
    print("Resume saved as XML.")

# Create the resume
resume = create_resume()

# Save the resume in different formats
print("Select the format to save your resume:")
print("1. CSV")
print("2. JSON")
print("3. YAML")
print("4. XML")

choice = input("Enter your choice (1-4): ")

if choice == "1":
    save_as_csv(resume)
elif choice == "2":
    save_as_json(resume)
elif choice == "3":
    save_as_yaml(resume)
elif choice == "4":
    save_as_xml(resume)
else:
    print("Invalid choice. Resume not saved.")

