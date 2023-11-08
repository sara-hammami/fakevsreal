# fakevsreal

## Context
FakeRealStreamlit App is a Python web application built with Streamlit, designed to detect fake and real images using CNN model.
## Dataset
I use the fakevsreal face image dataset availabel in kaggle .
[Dataset]([URL](https://www.kaggle.com/datasets/ciplab/real-and-fake-face-detection))
## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python**: Version 3.9 or higher installed on your system.
- **Docker**: Installed on your system.
## Installation

1. **Clone the Repository:**
   git clone https://github.com/your-username/fakerealstreamlit-app.git
   cd fakerealstreamlit-app
2. **Build the docker image:**
   docker build -t fakerealstreamlit-app .
3. **Run the docker container:**  
   docker run -p 8501:8501 fakerealstreamlit-app
