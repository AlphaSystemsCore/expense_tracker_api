tables = ("""
        CREATE TABLE expense_categorization IF NOT EXISTS( 
        expense_cat_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY, 
        category VARCHAR(80) NOT NULL UNIQUE
        );
        """,
        """
        CREATE TABLE income_categorization IF NOT EXISTS(
        income_cat_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        category VARCHAR(80) UNIQUE NOT NULL
        );
        """,
        """
        CREATE TABLE auth_credentials(
        credential_id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
        email VARCHAR(100) UNIQUE NOT NULL,
        hashed_password TEXT NOT NULL
        )
        """,
        "CREATE TYPE roles_type AS ENUM('user', 'admin')",
        """
        CREATE TABLE users(
        user_id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
        first_name VARCHAR(80) NOT NULL,
        middle_name VARCHAR(80),
        last_name VARCHAR(80),
        location VARCHAR(100),
        role roles_type NOT NULL DEFAULT 'user',
        credential_id UUID,
        FOREIGN KEY credential_id  REFERENCES auth_credentials(credential_id),

        )
        """,
        """
        CREATE TABLE time_metadata(
        time_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        datetime datetime NOT NULL,
        day varchar(15) NOT NULL,
        month MONTH NOT NULL,
        year YEAR NOT NULL,
        day_of_the_week int NOT NULL,
        week_of_the_year int NOT NULL,
        day_of_the_year int NOT NULL
        )
        """,
        """
        CREATE TABLE expenses(
        expense_id UUID DEFAULT gen_radom_uuid() PRIMARY KEY,
        amount numeric NOT NULL ,
        expense_cat_id INTEGER NOT NULL,
        user_id UUID NOT NULL,
        time_id INT NOT NULL, 
        FOREIGN KEY expense_cat_id REFERENCES expense_categorization(expense_cat_id),
        FOREIGN KEY user_id REFERENCES users(user_id),
        FOREIGN KEY time_id REFERENCES time_metadata(time_id)
        )
        """,
        """
        CREATE TABLE incomes(
        income_id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
        amount NUMERIC NOT NULL,
        income_cat_id INTEGER NOT NULL,
        user_id UUID NOT NULL,
        time_id INTEGER NOT NULL,
        FOREIGN KEY income_cat_id REFERENCES income_categorization(income_cat_id),
        FOREIGN KEY user_id REFERENCES users(user_id),
        FOREIGN KEY time_id REFERENCES time_metadate(time_id)
        )
        """,
    
        )