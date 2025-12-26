# ProjektX — Bank Database Management System
*AISSCE Class 12 Computer Science Project (2022–23)*

ProjektX is a **Python + MySQL** console-based banking system that lets users manage customer bank accounts using CRUD operations and simple debit/credit transactions.

This project was created as a CBSE Class 12 Computer Science Practical Project (AISSCE – 2022–23).

---

## Features

- Add (Insert) new bank account records
- Display all accounts — sortable by:
  - Account Number
  - Customer Name
  - Account Balance
- Search records by Account Number
- Update customer details
- Delete bank records
- Money Transactions
  - Debit (with minimum balance rule ₹2000)
  - Credit to the account
- Interactive CLI menu interface

---

## Tech Stack

| Component | Technology |
|----------|------------|
| Programming Language | Python 3 |
| Database | MySQL |
| Library Used | `mysql-connector-python` |

---

## Project Structure
```
ProjektX/
├── bnkdb_main.py # Main application - Banking System CLI
└── dbcreate.py # Creates DB, BANK table & sample data
```

---

## Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/ProjektX.git
cd ProjektX
```

### 2️⃣ Install Dependencies
```bash
pip install mysql-connector-python
```

### 3️⃣ Create MySQL Database

Open MySQL and run:
```bash
CREATE DATABASE BANKDB;
```

### 4️⃣ Initialize Table + Demo Records
```bash
python dbcreate.py
```

### 5️⃣ Run the Application
```bash
python bnkdb_main.py
```

## Usage
After launching the script, type:
```bash
>>> menu
```
