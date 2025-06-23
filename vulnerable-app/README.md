# Vulnerable App

This repository contains an intentionally vulnerable web application and infrastructure code, designed to serve as a benchmark for testing Application Security (AppSec) tools.

## Purpose

The goal of this project is to provide a multi-faceted, easily detectable set of vulnerabilities for evaluating the detection capabilities of open-source security tools such as KICS (for IaC), Semgrep (for SAST), and various SCA and secret scanners.

## Included Vulnerabilities

- **Infrastructure as Code (IaC):**
  - Publicly readable S3 bucket (Terraform)
  - Overly permissive IAM role with AdministratorAccess (Terraform)
  - Dockerfile runs as root
- **Static Application Security Testing (SAST):**
  - Flask debug mode enabled
  - Command injection via unsanitized subprocess usage
  - Unsafe yaml.load() usage
  - Hardcoded secrets and credentials
- **Software Composition Analysis (SCA):**
  - Outdated and vulnerable dependencies (requests, PyYAML)
- **Secrets Detection:**
  - Hardcoded secret key and database connection string

## Usage

1. Clone this repository.
2. Run your AppSec tool (e.g., KICS, Semgrep, Trivy, Gitleaks) against this repository.
3. Review the findings and use them to benchmark or test your tool's detection capabilities.

**Warning:** This project is intentionally insecure. Do not deploy in production or expose to the internet. 