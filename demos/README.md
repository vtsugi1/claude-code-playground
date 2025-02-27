# Demo Examples

This folder contains three example projects showcasing different capabilities:

## 1. React Todo App
A complete React Todo application with local storage persistence, filtering capabilities, and a clean user interface. Features include:
- Add, toggle, and delete todos
- Filter by status (all, active, completed)
- Clear completed todos
- LocalStorage persistence

### Running the React App:
```bash
# Install dependencies
npm install react react-dom

# Create a new React app and replace App.jsx with 1-react-todo-app.jsx
npx create-react-app todo-app
cp 1-react-todo-app.jsx todo-app/src/App.jsx

# Start the app
cd todo-app
npm start
```

## 2. Python Data Analysis
A data science script demonstrating:
- Pandas for data manipulation
- Matplotlib/Seaborn for visualization
- Scikit-learn for machine learning
- Feature engineering and model evaluation

### Running the Python Script:
```bash
# Install dependencies
pip install pandas matplotlib seaborn scikit-learn

# Run the script
python 2-python-data-analysis.py
```

## 3. Node.js Express API
A RESTful API built with Express.js showcasing:
- JWT authentication
- Role-based authorization
- CRUD operations
- Error handling middleware
- Security best practices with Helmet
- Logging with Morgan

### Running the Node.js API:
```bash
# Install dependencies
npm init -y
npm install express body-parser cors morgan helmet jsonwebtoken

# Run the server
node 3-node-express-api.js

# Test endpoints with curl
curl http://localhost:3000/api/books
curl -X POST -H "Content-Type: application/json" -d '{"username":"admin","password":"admin123"}' http://localhost:3000/api/login
# Copy the token from the response and use it in subsequent requests
curl -H "Authorization: Bearer YOUR_TOKEN" http://localhost:3000/api/books/1
```