from fastapi import FastAPI
import mysql.connector

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Docker application running"}

@app.get("/insert")
def insert_data():

    connection = mysql.connector.connect(
        host="mysql",
        user="root",
        password="root123",
        database="ml_database"
    )

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INT AUTO_INCREMENT PRIMARY KEY,
            prediction FLOAT
        )
    """)

    cursor.execute(
        "INSERT INTO predictions (prediction) VALUES (%s)",
        (250.5,)
    )

    connection.commit()

    cursor.close()
    connection.close()

    return {"message": "Data inserted into MySQL"}