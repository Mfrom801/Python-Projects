import os
import sqlite3

# Create a connection to the database
conn = sqlite3.connect('test.db')

# Create a table with some columns
conn.execute('''CREATE TABLE IF NOT EXISTS files_table
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              filename TEXT NOT NULL);''')

fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

txt_files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.txt')]

# Insert the filenames into the table
for file in fileList:
    if file.endswith('.txt'):
        
        conn.execute("INSERT INTO files_table (filename) VALUES (?)", (file,))
        print(file)

# Save the changes and close the connection
conn.commit()
conn.close()


