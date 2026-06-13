from app.db.db_connection import get_cur


def create_credential_user_token_repo(email, hashed_password, token, expires_at):
    with get_cur() as cur:
        cur.execute(
            """
            INSERT INTO auth_credentials(email, hashed_password)
            VALUES(%s, %s) 
            RETURNING credential_id
            """, (email, hashed_password)
        )
        credential_id = cur.fetchone()
        cur.execute("INSERT INTO users(credential_id) VALUES(%s)",(credential_id,))
        cur.execute(    
            """INSERT INTO verify_email_token
            (token, credential_id, expires_at)
            VALUES(%s, %s, %s)""",
            (token,credential_id, expires_at))
    return credential_id

        
def get_verify_email_token_repo(credential_id:str):
    with get_cur() as cur:
        cur.execute(
            """
            SELECT ac.is_verified, vem.token, vem.expires_at, vem.is_used
            FROM auth_credentials ac
            JOIN verify_email_token vem
            ON ac.credential_id = vem.credential_id
            WHERE vem.credential_id = %s AND vem.is_used = False
            """,(credential_id,)
        )
        row = cur.fetchone()
    return row

def update_verify_email_token_repo(credential_id, is_used:bool, is_verified: bool| None = None):
    with get_cur() as cur:
        cur.execute("""UPDATE auth_credentials
                    SET is_verified = COALESCE(%s, is_verified) 
                    WHERE credential_id = %s
                    """,
                    (is_verified,credential_id) 
        )
        cur.execute("""UPDATE verify_email_token
                    SET is_used = %s
                    WHERE credential_id = %s
                    """
                    , (is_used, credential_id)
        )