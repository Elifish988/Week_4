from db import get_db_connection
import psycopg2

def normalize_db():
    try:
        source_conn = get_db_connection()

        # יצירת הטבלאות המנורמלות
        create_targets = """
            CREATE TABLE IF NOT EXISTS targets (
                target_id SERIAL PRIMARY KEY,
                target_type VARCHAR(100),
                target_industry VARCHAR(255),
                target_priority VARCHAR(5)
            )
        """
        create_targets_location = """
            CREATE TABLE IF NOT EXISTS targets_location (
                latitude NUMERIC(10, 6),
                longitude NUMERIC(10, 6),
                target_id INTEGER REFERENCES targets(target_id)
            )
        """
        create_targets_address = """
            CREATE TABLE IF NOT EXISTS targets_address (
                country VARCHAR(100),
                city VARCHAR(100),
                target_id INT REFERENCES targets(target_id)
            )
        """

        # ביצוע יצירת הטבלאות
        cur = source_conn.cursor()
        cur.execute(create_targets)
        cur.execute(create_targets_location)
        cur.execute(create_targets_address)
        source_conn.commit()

        # העברת הנתונים מטבלת mission לטבלאות המנורמלות
        s_cur = source_conn.cursor()
        s_cur.execute("""
            SELECT 
                mission_id, target_country, target_city, 
                target_latitude, target_longitude, 
                target_type, target_industry, target_priority 
            FROM mission;
        """)

        for mission_row in s_cur.fetchall():
            # בדיקה אם הטרגט כבר קיים בטבלה
            cur.execute("""
                SELECT target_id FROM targets 
                WHERE target_type = %s AND target_industry = %s AND target_priority = %s
            """, (mission_row[5], mission_row[6], mission_row[7]))

            existing_target = cur.fetchone()

            if existing_target:
                target_id = existing_target[0]
                cur.execute("UPDATE mission SET target_id = %s WHERE mission_id = %s",
                            (target_id, mission_row[0]))
            else:
                # הוספת מטרה חדשה אם לא קיימת
                cur.execute("""
                    INSERT INTO targets (target_type, target_industry, target_priority) 
                    VALUES (%s, %s, %s) RETURNING target_id""",
                            (mission_row[5], mission_row[6], mission_row[7]))
                target_id = cur.fetchone()[0]

                # הוספת מיקום
                cur.execute("INSERT INTO targets_location (latitude, longitude, target_id) "
                            "VALUES (%s, %s, %s)",
                            (mission_row[3], mission_row[4], target_id))

                # הוספת כתובת
                cur.execute("INSERT INTO targets_address (country, city, target_id) "
                            "VALUES (%s, %s, %s)",
                            (mission_row[1], mission_row[2], target_id))

            # עדכון mission עם ה-target_id
            cur.execute("UPDATE mission SET target_id = %s WHERE mission_id = %s",
                        (target_id, mission_row[0]))

        source_conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        source_conn.close()


normalize_db()
