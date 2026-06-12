from app.db.db_connection import get_cur
tables = ("""
        CREATE TABLE IF NOT EXISTS expense_categorization (
        expense_cat_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        category VARCHAR(80) NOT NULL UNIQUE
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS income_categorization (
        income_cat_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        category VARCHAR(80) NOT NULL UNIQUE
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS auth_credentials (
        credential_id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
        email VARCHAR(100) NOT NULL UNIQUE,
        hashed_password TEXT NOT NULL,
        is_verified BOOLEAN DEFAULT false,
        access_revoked BOOLEAN DEFAULT false
        );
        """,

        "CREATE TYPE roles_type AS ENUM ('user', 'admin', 'super admin');",

        """
        CREATE TABLE IF NOT EXISTS users (
        user_id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
        first_name VARCHAR(80),
        middle_name VARCHAR(80),
        last_name VARCHAR(80),
        location VARCHAR(100),
        role roles_type NOT NULL DEFAULT 'user',
        credential_id UUID UNIQUE,
        FOREIGN KEY (credential_id) REFERENCES auth_credentials(credential_id)
        );
        """,

        """
        CREATE TABLE IF NOT EXISTS time_metadata (
        time_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        datetime TIMESTAMP NOT NULL,
        day VARCHAR(15) NOT NULL,
        month VARCHAR(15) NOT NULL,
        year INT NOT NULL,
        day_of_week INT NOT NULL,
        week_of_year INT NOT NULL,
        day_of_year INT NOT NULL

        );
        """,

        """
        CREATE TABLE IF NOT EXISTS expenses (
        expense_id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
        amount NUMERIC(12,2) NOT NULL,
        expense_cat_id INTEGER NOT NULL,
        user_id UUID NOT NULL,
        time_id INT NOT NULL,
        FOREIGN KEY (expense_cat_id) REFERENCES expense_categorization(expense_cat_id),
        FOREIGN KEY (user_id) REFERENCES users(user_id),
        FOREIGN KEY (time_id) REFERENCES time_metadata(time_id)
        );
        """,

        """
        CREATE TABLE IF NOT EXISTS incomes (
        income_id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
        amount NUMERIC(12,2) NOT NULL,
        income_cat_id INTEGER NOT NULL,
        user_id UUID NOT NULL,
        time_id INT NOT NULL,
        FOREIGN KEY (income_cat_id) REFERENCES income_categorization(income_cat_id),
        FOREIGN KEY (user_id) REFERENCES users(user_id),
        FOREIGN KEY (time_id) REFERENCES time_metadata(time_id)
        );
        """,

        """
        CREATE TABLE IF NOT EXISTS reset_password_token (
        reset_pwd_token UUID DEFAULT gen_random_uuid() PRIMARY KEY,
        token TEXT NOT NULL UNIQUE,
        credential_id UUID NOT NULL,
        expire_at TIMESTAMP NOT NULL,
        is_used BOOLEAN DEFAULT false,
        created_at TIMESTAMP DEFAULT NOW(),
        FOREIGN KEY (credential_id) REFERENCES auth_credentials(credential_id)
        );
        """,

        """
        CREATE TABLE IF NOT EXISTS verify_email_token (
        verify_email_token UUID DEFAULT gen_random_uuid() PRIMARY KEY,
        token TEXT NOT NULL UNIQUE,
        credential_id UUID NOT NULL,
        expires_at TIMESTAMP NOT NULL,
        is_used BOOLEAN DEFAULT false,
        created_at TIMESTAMPTZ DEFAULT NOW(),
        FOREIGN KEY (credential_id) REFERENCES auth_credentials(credential_id)
        );
        """
        )

if  __name__ == "__main__":
        with get_cur() as cur:
                count = 0
                for table in tables:
                        cur.execute(table)
                        count +=1
                print(count)
