import psycopg2

class UserRepository:
    def __init__(self, **db_config):
        self.db_config = db_config

    def _get_connection(self):
        return psycopg2.connect(**self.db_config)

    def add_user(self, username, hashed_password):
        with self._get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO users (username, password) VALUES (%s, %s)",
                    (username, hashed_password)
                )
                conn.commit()

    def get_user_by_username(self, username):
        with self._get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT * FROM users WHERE username = %s",
                    (username,)
                )
                row = cur.fetchone()
                if row:
                    return {
                        'id': row[0],
                        'username': row[1],
                        'password': row[2]
                    }
                return None
