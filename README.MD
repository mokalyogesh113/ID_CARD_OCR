# Project Setup Guide

This repository contains a project setup guide for running the server and client applications. Follow the instructions below to set up the environment properly.

## Pre-requisites
Before running the server, ensure that the following software is installed on your system:
- Node.js
- Python
- MySQL

## Server Configuration
1. **Database Connection Setup:**
   - Open the `./server/sql_crud.py` file.
   - Update the database connection parameters:
     ```python
     mydb = mysql.connector.connect(
         host="_____",
         port=____,
         user="____",
         password="____",
         database="____",
         charset='utf8'
     )
     ```

2. **Backend URL Configuration:**
   - If the server is deployed and there is a need to change the backend URL:
     - Navigate to the file: `./CLIENT/src/App.js`.
     - Update the `url` variable:
       ```javascript
       const url = “___________”;
       ```

## Setup Steps for Client & Server

### Server Setup
1. **Navigate to Server Directory:**
   - Open a terminal and navigate to the `/server` directory:
     ```
     cd SERVER
     ```

2. **Install Required Python Libraries:**
   - Execute the following command to install all required Python libraries and packages:
     ```
     pip install easyocr flask flask_cors mysql-connector-python
     ```

3. **Run Server Script:**
   - Execute the following command to run the server:
     ```
     python server.py
     ```
   - Note: For the first time, it may take 5-10 minutes depending on internet speed.

### Client Setup
1. **Navigate to Client Directory:**
   - Open another terminal and navigate to the current project folder:
     ```
     cd CLIENT
     ```

2. **Install Dependencies:**
   - Run the following command to install dependencies:
     ```
     npm i
     ```

3. **Start React Server:**
   - Run the following command to start the React server:
     ```
     npm start
     ```

## Completion
After following the above steps, both the server and client setups should be completed successfully. 