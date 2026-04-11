# **AWS Multi‑Account Foundation (Control Tower + CDK + GitHub Actions)**

This repository provides an automated, production‑ready foundation for managing a secure, scalable AWS multi‑account environment. It uses **AWS Control Tower** as the governance layer and extends it with **AWS CDK (Python)** to provision Organizational Units (OUs), IAM Identity Center permission sets, and future enterprise‑level configurations. Deployment is fully automated using **GitHub Actions**.

---

## **Overview**

This project implements a modern AWS enterprise landing zone architecture with:

- **AWS Control Tower** as the governance and compliance engine  
- **AWS Organizations** for multi‑account structure  
- **PROD** and **NonPROD** Organizational Units  
- **IAM Identity Center (built‑in directory)** for centralized authentication and authorization  
- **CDK (Python)** for infrastructure-as-code  
- **GitHub Actions** for CI/CD automation  
- **Secure, scalable, repeatable deployments** across your AWS environment  

This foundation is designed for long‑term growth, enabling you to add new accounts, guardrails, SCPs, networking, and workload infrastructure as your organization expands.

---

## **Architecture**

### **Core Components**

- **Management Account**  
  Hosts Control Tower, Organizations, and Identity Center.

- **Log Archive Account**  
  Centralized CloudTrail and Config logs.

- **Audit/Security Account**  
  Read‑only access to all accounts for security operations.

- **Organizational Units**
  - **PROD OU** – Production workloads  
  - **NonPROD OU** – Development, testing, staging  

- **IAM Identity Center**
  - Built‑in directory  
  - Permission sets for PROD and NonPROD environments  

- **CI/CD Pipeline**
  - GitHub Actions deploys CDK stacks automatically  
  - Uses OIDC to assume a secure deployment role in AWS  

---

### **Key Modules**

- **ou_stack.py**  
  Creates PROD and NonPROD Organizational Units.

- **identity_center_stack.py**  
  Creates IAM Identity Center permission sets for each environment.

- **deploy.yml**  
  GitHub Actions workflow for automated deployments.

---

## **Prerequisites**

Before deploying this foundation, ensure the following are completed:

### **AWS Requirements**
- AWS Control Tower is enabled in your management account  
- AWS Organizations is active  
- IAM Identity Center is configured using the **built‑in directory**  
- You have:
  - **Parent OU ID** (Root or another OU)
  - **IAM Identity Center Instance ARN**
  - **Deployment IAM Role** for GitHub OIDC  

### **Local Requirements**
- Python 3.11+
- Node.js (for CDK CLI)
- AWS CLI configured (optional for local testing)

---

## **Deployment Workflow**

### **1. Configure GitHub Secrets**

Add the following secrets to your GitHub repository:

| Secret Name | Description |
|------------|-------------|
| `AWS_DEPLOY_ROLE_ARN` | IAM role GitHub Actions will assume |
| `AWS_REGION` | Deployment region (e.g., `us-east-1`) |
| `ORG_PARENT_OU_ID` | Root or parent OU ID |
| `SSO_INSTANCE_ARN` | IAM Identity Center instance ARN |

---

### **2. Push to `main` Branch**

Every push to `main` triggers the GitHub Actions workflow:

- Installs dependencies  
- Synthesizes CDK  
- Deploys all stacks to AWS  
- Creates OUs and permission sets  

No manual approval is required.

---

## **How It Works**

### **Organizational Units**

The CDK stack provisions:

- **PROD OU**  
- **NonPROD OU**

These OUs become the foundation for account placement, guardrails, and SCPs.

---

### **IAM Identity Center Permission Sets**

Two permission sets are created:

- **Prod‑Admin**  
  Full administrative access for production accounts.

- **NonProd‑PowerUser**  
  PowerUser access for development and testing accounts.

Assignments can be added later to map:

- Groups → Accounts → Permission Sets

---

### **GitHub Actions CI/CD**

The pipeline uses:

- GitHub OIDC for secure authentication  
- A deployment role in AWS  
- CDK to deploy infrastructure changes automatically  

This ensures:

- No long‑lived AWS credentials  
- Fully automated deployments  
- Production‑grade security posture  

---

## **Extending the Foundation**

This repository is intentionally modular and ready for expansion. You can add:

- Service Control Policies (SCPs)  
- Additional OUs (e.g., Sandbox, Shared Services, Networking)  
- Account Factory customizations  
- Baseline networking (VPCs, Transit Gateway, DNS)  
- Security services (Security Hub, GuardDuty, IAM Access Analyzer)  
- Workload infrastructure (ECS, EKS, RDS, Lambda)  

The CDK structure supports multi‑stack, multi‑account deployments as your environment grows.

---

## **Troubleshooting**

### **Common Issues**

- **Missing environment variables**  
  Ensure GitHub secrets are correctly configured.

- **Access denied during deployment**  
  Verify the deployment role has:
  - `organizations:`
  - `sso:`
  - `iam:`
  - `cloudformation:`

- **Identity Center ARN mismatch**  
  Confirm the ARN matches the region where Identity Center is enabled.

---

## **Support**

If you are experimenting with this architecture and encounter issues, you can reach out for help using the following email ID:

📧 **mogeshailu381@gmail.com**

