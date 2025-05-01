# **Automating AWS Security Groups with GitLab CI/CD and ServiceNow**

## **Overview**
This project demonstrates how to automate the management of AWS security groups using a combination of GitLab CI/CD pipelines, ServiceNow integration, and Terraform. The solution streamlines change management processes, reduces manual effort, enforces security compliance, and accelerates deployments.

---

## **Current Status**
### **Completed:**
- Set up Terraform for AWS security group management.
- Created a Python script to append new ports to be opened in existing security groups.
- Configured a GitLab CI/CD pipeline for automated workflows.
- Integrated ServiceNow to trigger the GitLab pipeline when a change ticket status transitions to "Implement."

### **Next Steps:**
- Post the results of the GitLab pipeline, including job details, back to ServiceNow for visibility and traceability.

---

## **Problem Statement**
Manually updating AWS security groups is time-consuming, error-prone, and inconsistent with organizational compliance requirements. This project solves these challenges by introducing an automated workflow that integrates IT Service Management (ServiceNow) with DevOps practices.

---

## **Solution**
This solution integrates ServiceNow and GitLab CI/CD to automate the lifecycle of AWS security groups:
1. **Change Requests in ServiceNow:** A user submits a change request.
2. **Approval and Trigger:** Once approved, ServiceNow triggers a GitLab CI/CD pipeline via its API.
3. **Pipeline Automation:** The pipeline:
   - Validates the request using custom scripts.
   - Applies changes to AWS security groups using Terraform.
   - Sends notifications to stakeholders about the pipeline status.
   - Posts pipeline results back to ServiceNow.
4. **Auditable Logs:** All actions are logged for traceability.

---

## **Key Features**
- **Integration:** Seamless connection between ServiceNow and GitLab CI/CD.
- **Validation:** Ensures security group configurations meet predefined policies.
- **Automation:** Utilizes Terraform for Infrastructure as Code (IaC).
- **Notifications:** Provides real-time updates on pipeline execution.
- **Compliance:** Enforces organizational security standards.
- **Feedback Loop:** Posts pipeline results back to ServiceNow for transparency.

---

## **Getting Started**
### **Prerequisites**
- AWS account with IAM permissions for managing security groups.
- ServiceNow account configured with API access.
- GitLab CI/CD setup with runners.
- Terraform installed on the runner.

### **Setup Instructions**
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/aws-security-groups-ci-cd.git
   cd aws-security-groups-ci-cd
   ```
2. Configure the Terraform backend in `terraform/main.tf`.
3. Update environment variables for GitLab CI/CD:
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`
   - `SERVICENOW_API_TOKEN`
4. Run the pipeline:
   - Triggered automatically by ServiceNow on approval.

---

## **Repository Structure**
```
aws-security-groups-ci-cd/
├── .gitlab-ci.yml       # GitLab pipeline configuration
├── terraform/           # Terraform modules and scripts
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
├── scripts/             # Python and utility scripts
│   ├── append_ports.py  # Script to append new ports
│   └── notify_stakeholders.py
├── README.md            # Project overview and setup guide
```

---

## **Future Enhancements**
- **Integration Improvements:**
  - Add Slack or Microsoft Teams notifications for real-time updates.
  - Generate detailed reports of security group changes.
- **Error Recovery:**
  - Implement a rollback mechanism for failed deployments.
- **Compliance and Monitoring:**
  - Validate security group compliance with organizational policies.
  - Integrate with AWS CloudWatch for monitoring and alerts.
- **Service Expansion:**
  - Automate management for other AWS resources (e.g., ELB, RDS).
- **Testing and Optimization:**
  - Add automated tests for Terraform configurations.
  - Optimize CI/CD pipelines for better performance.
- **Multi-Account Support:**
  - Extend the solution to manage resources across multiple AWS accounts.

---

## **Contact**
For questions or suggestions, feel free to reach out:
- **GitHub:** [darylfragata](https://github.com/darylfragata)
- **LinkedIn:** [fragatadarylj](https://linkedin.com/in/fragatadarylj)
