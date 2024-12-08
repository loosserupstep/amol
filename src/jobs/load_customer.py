import snowflake.connector


# Connect to Snowflake
conn = snowflake.connector.connect(
    user='your_username',
    password='your_password',
    account='your_account'
)

# Create a cursor
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM your_table")

# Fetch results
for row in cur:
    print(row)

# Close the connection
cur.close()
conn.close()