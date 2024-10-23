
---

# 🩸 Blood Bank Management System

Welcome to the **Blood Bank Management System**, a comprehensive web application designed to streamline the blood donation process and manage blood stocks efficiently. This application facilitates the interaction between donors, patients, and administrators, ensuring a smooth workflow for blood donations and requests.

![Blood Bank Management System](https://github.com/user-attachments/assets/a7e30e5d-e570-4f16-9349-608562df2065)

---

## 🚀 Key Features

### For Admin
- **Admin Account Management**: Create admin accounts with the command:
  ```bash
  python manage.py createsuperuser
  ```
- **Dashboard Overview**: View critical statistics including:
  - Units of blood available for each blood group
  - Total number of donors
  - Number of blood requests
  - Number of approved requests
  - Total units of blood available
- **Donor Management**: View, update, or delete donor records.
- **Patient Management**: View, update, or delete patient records.
- **Donation Request Handling**: Review and manage donation requests made by donors. Approve or reject requests based on donor health status.
  - Approved requests increase blood stock.
  - Rejected requests do not affect stock.
- **Blood Request Management**: Approve or reject blood requests from donors or patients, affecting blood stock accordingly.
- **History Tracking**: Maintain a history of all blood requests.
- **Stock Management**: Update units of specific blood groups as needed.

### For Donors
- **Account Creation**: Donors can create an account by providing basic details.
- **Donation Management**: Donate blood and view donation history with approval status (Pending, Approved, Rejected).
- **Blood Request**: Request blood from available stock and track request history with statuses.

### For Patients
- **Easy Signup**: Patients can create accounts without admin approval.
- **Request Blood**: Patients can request specific blood groups and units, monitoring their request history.

---

## 💻 How to Run This Project

### Prerequisites
- **Python** (Version: 3.7.6)
  - **Note**: Remember to check "Add to PATH" during installation.

### Installation Steps

1. **Clone or Download the Project**

2. **Navigate to the Project Directory**
   ```bash
   cd blood_bank_system
   ```

3. **Create a Virtual Environment**
   Create a virtual environment to manage project dependencies:
   ```bash
   python -m venv venv
   ```

4. **Activate the Virtual Environment**
   - For **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - For **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

5. **Install Dependencies**
   Install the required Python packages:
   ```bash
   python -m pip install -r requirements.txt
   ```

6. **Run Database Migrations**
   Apply migrations to set up your database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Start the Server**
   Run the application:
   ```bash
   python manage.py runserver
   ```

8. **Access the Application**
   Open your web browser and navigate to:
   [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 📜 Login Credentials
- **Username**: `admin`
- **Password**: `admin12345`

---

## 🛠️ Technologies Used
- **Django**: For building the web application framework.
- **SQLite**: For database management.
- **HTML/CSS**: For front-end development.
- **JavaScript**: For interactive features.

---

## 📷 Screenshots
![2](https://github.com/user-attachments/assets/de8979da-32a9-42c0-a726-a0252a1e3940)
![3](https://github.com/user-attachments/assets/0b1a43fb-16b0-4720-91df-ba30e69007b3)
![4](https://github.com/user-attachments/assets/4e33410b-a348-42c0-91ce-f941718bd4be)
![5](https://github.com/user-attachments/assets/870e3292-e4bb-4515-9847-34b95f2360e5)
![6](https://github.com/user-attachments/assets/d4df00de-9df0-4b38-b824-28c8af3c37f6)

---

### 🌟 **Join Us in Saving Lives!** 🌟

---

Feel free to customize any parts further to suit your project specifics!
