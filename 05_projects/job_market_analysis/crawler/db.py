import pymysql


def get_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='job_analysis',
        charset="utf8mb4"
    )


def insert_job(job):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO jobs 
    (job_name, company, city, salary, experience, education, skills, keyword)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """

    cursor.execute(sql, (
        job["job_name"],
        job["company"],
        job["city"],
        job["salary"],
        job["experience"],
        job["education"],
        job["skills"],
        job["keyword"]
    ))

    conn.commit()
    cursor.close()
    conn.close()
