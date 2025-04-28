# AWS Security Groups Automation  

This repository contains the initial codebase for automating AWS Security Groups with integrations to GitLab CI/CD and ServiceNow.  

## Project Overview  

This project is designed to automate the management of AWS Security Groups through a robust CI/CD pipeline and ServiceNow integration. It helps streamline workflows, improve operational efficiency, and ensure consistent security group configurations in AWS.  

### Key Features  

- **AWS Security Group Automation**: Automates the creation, updating, and deletion of AWS Security Groups.  
- **GitLab CI/CD Integration**: Currently configured for GitLab pipelines to facilitate automation workflows.  
- **ServiceNow Integration**: Connects with ServiceNow to enable change management processes.  

## Repository Migration  

This project was originally hosted on GitLab. While the source code has been migrated to GitHub, the CI/CD pipeline remains configured for GitLab.  

### What's Next?  

This is the initial file for the GitHub repository. I will be updating the project to integrate GitHub CI/CD workflows (e.g., GitHub Actions) and enhance compatibility with this platform soon. Stay tuned for updates!  

If you'd like to contribute or help with the migration to GitHub CI/CD, feel free to fork the repository and submit a pull request.  

## Getting Started  

### Prerequisites  

- **AWS Credentials**: Ensure you have access to an AWS account with the necessary permissions.  
- **ServiceNow Access**: A ServiceNow instance with integration capabilities.  
- **Pipeline Trigger Token**: Set up a trigger token in GitLab's **Pipeline Trigger Tokens** section to allow automated CI/CD executions.  
- **Project Access Token**: Create a project access token in GitLab for authentication during API calls.  

### Installation  

1. Clone the repository:  
   ```bash
   git clone https://github.com/<your-github-username>/<your-repo-name>.git
   cd <your-repo-name>
