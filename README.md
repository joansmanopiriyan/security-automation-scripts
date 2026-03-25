# Security Automation Scripts

This repository contains beginner-friendly Python automation scripts created during my web security learning journey.

## Script Included

### HTTP Security Headers Checker

This script checks whether important security headers are present on target websites:

- X-Frame-Options
- Content-Security-Policy
- Strict-Transport-Security
- X-Content-Type-Options
- Referrer-Policy

These headers help protect applications from attacks like clickjacking, MIME sniffing, and insecure transport risks.

### Purpose

This project supports my practice in:

- Web security fundamentals
- Reconnaissance automation
- HTTP response analysis
- Python scripting for security workflows

### Directory Exposure Checker

This script scans a target website for commonly exposed directories such as:

- /admin
- /backup
- /uploads
- /logs

Useful during early-stage reconnaissance in web application security testing.

### robots.txt Parser

This script checks whether a target website exposes a robots.txt file and extracts hidden or restricted paths useful during reconnaissance.
