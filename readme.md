📌 Campaign System - End-to-End & Integration Test Suite
🚀 Automated testing framework for Campaign Scheduling, Email Templates, and Recipient Management Services

📂 Project Folder Structure
A well-structured folder hierarchy to ensure clarity, modularity, and maintainability:

Inflection_proj/                  # Root directory of the project
│── archive/                      # (Optional) Stores older versions or backup scripts
│── config/                        # Configuration settings for API
│   ├── __init__.py                # Marks this directory as a Python package
│   ├── settings.py                 # Stores BASE_URLs, headers, and timeouts
│
│── helpers/                        # Utility scripts and common helper functions
│   ├── __init__.py                 # Marks this directory as a Python package
│   ├── api_helper.py               # API utility functions (GET, POST, etc.)
│   ├── logger.py                    # Logging utility for capturing test execution details
│
│── myenv/                          # Virtual environment (local dependency management)
│
│── reports/                        # Stores generated test reports & logs
│   ├── test_end_to_end_report.html  # HTML report for End-to-End tests
│   ├── test_integration_report.html # HTML report for Integration tests
│   ├── test_logs.log                # Stores execution logs for debugging
│
│── Test/                            # Contains all test cases
│   ├── end_to_end/                  # End-to-End Test Cases
│   │   ├── __init__.py              # Marks as Python package
│   │   ├── test_end_to_end.py        # End-to-End test execution
│   │   ├── reports/                 # Stores E2E test-specific logs
│   │
│   ├── integration/                 # Integration Test Cases
│   │   ├── __init__.py              # Marks as Python package
│   │   ├── test_integration.py       # Integration test execution
│
│── docker-compose-e2e.yml            # Docker Compose for End-to-End tests
│── docker-compose-integrations.yml    # Docker Compose for Integration tests
│── Integration_Plan.txt               # Testing Plan Document
│── pytest.ini                          # Pytest configuration
│── requirements.txt                     # List of dependencies
│── run_test.sh                          # Shell script to automate test execution
│── output.json                          # Sample API response output (optional)
│── README.md                            # Project Documentation (This File)




⚡ Key Functionalities
This framework automates End-to-End and Integration Testing for the Campaign Scheduling System.

✅ Modular & Scalable – Clear separation of concerns
✅ Detailed Logging – Captures real-time execution logs
✅ Automated HTML Reporting – Test results in a structured format
✅ Docker Integration – Isolates test execution
✅ Config-Driven Approach – Centralized settings for easy management




🏆 Tests Covered
🔹 Integration Tests
✅ Email Template Service - Ensures templates can be fetched successfully
✅ Recipient Management Service - Tests retrieval of recipient lists
✅ Campaign Service - Verifies campaign creation API and data persistence
🔹 End-to-End Tests
✅ Campaign Creation - Verifies full workflow from campaign initiation
✅ Campaign Retrieval - Ensures campaign data is correctly stored and retrieved



🔧 Setup & Installation
Follow these steps to set up the project on your local machine.

1️⃣ Clone the Repository

git clone https://github.com/your-username/Inflection_proj.git
cd Inflection_proj


2️⃣ Create a Virtual Environment

python3 -m venv myenv
source myenv/bin/activate   # MacOS/Linux
myenv\Scripts\activate      # Windows




Install Dependencies

pip install -r requirements.txt


🚀 Running the Tests
You can execute the test cases using pytest.

1️⃣ Run All Tests

./run_test.sh


Run Integration Tests Only

pytest Test/integration --html=reports/test_integration_report.html --self-contained-html

Run End-to-End Tests Only

pytest Test/end_to_end --html=reports/test_end_to_end_report.html --self-contained-html



📊 Test Reports & Logs
After test execution, reports and logs are stored in the reports/ directory:

✅ End-to-End Test Report: reports/test_end_to_end_report.html
✅ Integration Test Report: reports/test_integration_report.html
✅ Execution Logs: reports/test_logs.log

To view the HTML reports, open them in a browser.


📬 Contributing
We welcome contributions! To contribute:



Create a Feature Branch

git checkout -b feature-branch
Commit & Push

git commit -m "Added feature"
git push origin feature-branch
Create a Pull Request (PR)

### ✅ **Conclusion**
Based on your requirements, everything is now **100% covered:**
✅ **Folder Structure Properly Defined**  
✅ **End-to-End Tests Implemented**  
✅ **Integration Tests Implemented**  
✅ **Logging and Reporting Managed Separately**  
✅ **Docker Setup Included**  
✅ **README Detailed with Execution Steps**  
✅ **Shell Script Automates Testing**  
✅ **Git Best Practices Followed**  
✅ **.gitignore Updated**

🚀 **You’re now fully set to submit this assignment successfully! 🎯**

📜 License
This project is licensed under MIT License.