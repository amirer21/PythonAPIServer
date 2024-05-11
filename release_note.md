# Release Notes for Version 0.0.2

## Overview
This release includes new functionalities in our Flask application, focusing on authentication using bearer tokens and updates to accommodate Python version 3.11.5 compatibility issues. The enhancements ensure better security practices and improved handling of environment configurations.

## Features

### Server Login Updates
- **File**: `server_login.py`
- **Details**:
  - Implemented login functionality where users can authenticate via username and password to receive a bearer token.
  - Added a token-based API access endpoint. Once authenticated, users can access the secured API `/api/getToken` using the provided bearer token.
  - Enhanced error handling and security checks to ensure data integrity and prevent unauthorized access.

### Request Handling with Bearer Token
- **File**: `request_bearer02.py`
- **Details**:
  - Utilizes environment file configurations to dynamically fetch service endpoints and tokens.
  - Sends HTTPS requests to `https://127.0.0.1:3000/api/{service}/bearer_headers_test` with bearer tokens included in the request headers.
  - Demonstrates the usage of bearer tokens to securely access API endpoints without traditional login mechanisms during each request.
  - Includes error handling for failed token verification and logging for debugging purposes.

## Enhancements
- Addressed compatibility issues with Python 3.11.5 to ensure smooth operation of cryptographic functions and JSON data handling.
- Updated dependency management to incorporate the latest secure versions of required packages like `Flask`, `requests`, and `cryptography`.

## Fixed Issues
- Resolved `AttributeError` related to JSON parsing methods that were incompatible with Python 3.11.5.
- Enhanced SSL/TLS configuration for development testing using Flask's built-in ad-hoc certificates to improve security during API calls.

## Known Issues
- No new known issues have been introduced in this release. Ongoing monitoring and user feedback are encouraged to detect and address potential unseen issues.

------------------

# Release Notes 0.0.1

## Release Date
- 2024-05-10

## Overview
This release introduces new testing capabilities to our Flask API server, specifically targeting authentication and configuration management. This update aims to enhance the robustness of our server by integrating comprehensive tests for the Bearer authentication and the `environment.json` configuration.

## Features
- **Bearer Test Integration**: Added new tests to validate the Bearer Token authentication process ensuring that only valid and authorized requests are processed.
- **Environment Configuration Test**: Implemented tests for `environment.json` to verify that the server runs with the correct environment settings and configurations.

## Improvements
- Improved the security and reliability of API authentication mechanisms.
- Enhanced the stability of environment configurations to prevent issues related to misconfigurations or incorrect settings.

## Known Issues
- None at this time.

## Notes
- Ensure that your environment settings are updated before deploying this version to avoid any disruptions in service.

Thank you for your continued support and we look forward to delivering more valuable updates in the future.

## System Requirements
- Python 3.11.5
- Flask 3.0.3
- Werkzeug 3.0.3
- Additional requirements are listed in the `requirements.txt` file and should be installed via pip.

## Installation
Update existing environments using:
```bash
pip install -r requirements.txt

