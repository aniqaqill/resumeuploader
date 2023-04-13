import requests
import base64

# Replace the URL with the actual URL provided by the company
url = 'https://recruit.servicerocket.io/resumes'

# Replace the file path with the actual file path of your resume
file_path = 'resume.pdf'

# Read the contents of the file
with open(file_path, 'rb') as file:
    file_contents = file.read()

# Encode the file contents using Base64
file_contents_encoded = base64.b64encode(file_contents).decode('utf-8')

# Replace the values with your actual name, email, and about text
data = {
    'name': 'Muhammad Aniq Aqil Bin Azrai Fahmi',
    'email': 'aniqaqil06@gmail.com',
    'about': 'Passionate self-taught software engineer with an impressive track record in hackathons, skilled in software development tools & technologies.',
    'file': file_contents_encoded
}

# Send a POST request to the API endpoint with the data
response = requests.post(url, json=data)

# Check the response status code and content
if response.status_code == 200:
    print('Resume submitted successfully!')
else:
    print('Error submitting resume: ', response.content)