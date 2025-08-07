# database/db_logging.py

from datetime import datetime

from database.db_Connection import get_connection


class RequestDAO:
    def __init__(self):
        self.conn = get_connection()

    def save_request(self, operation: str, input_data: str, result: str):
        cursor = self.conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO math_requests (operation, input_data, result, created_at)
                VALUES (:op, :inp, :res, :ts)
            """, {
                "op": operation,
                "inp": input_data,
                "res": result,
                "ts": datetime.utcnow()
            })
            self.conn.commit()
        finally:
            cursor.close()

    def close(self):
        self.conn.close()
