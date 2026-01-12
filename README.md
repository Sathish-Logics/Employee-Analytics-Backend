# Employee Management & Analytics System (Backend)

## 📌 Project Overview
This project is a high-performance backend system built to manage and validate corporate employee data. It utilizes a **3-Tier Architecture** to ensure the separation of business logic from database operations, following industry best practices for Data Engineering.

## 🏗️ System Architecture
The project is structured into three distinct layers to ensure scalability and clean code:

* **Service Layer (`service/`):** Handles business logic and data validation (e.g., salary floors, name length constraints).
* **Data Access Layer / Repository (`repository/`):** Manages all SQL transactions and raw database interactions.
* **Database Layer (`database/`):** Configures secure connections to the PostgreSQL database.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Database:** PostgreSQL
* **Libraries:** Psycopg2 (Database Driver)

## 🔍 Key Data Governance Features
* **Validation:** Enforces a minimum salary of 15,000 and name length limits to maintain data quality.
* **Error Handling:** Implements custom exceptions for missing IDs or invalid inputs.
* **CRUD Functionality:** Full support for Create, Read, Update, and Delete operations for employee records.
