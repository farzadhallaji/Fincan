 
#import sqlite3

#class SQLiteHandler:
    #def __init__(self, dbname):
        #self.conn = sqlite3.connect(dbname)
        #self.cursor = self.conn.cursor()

    #def create_table(self, table_name, columns):
        #columns_str = ', '.join(columns)
        #self.cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({columns_str})')
        #self.conn.commit()

    #def insert_data(self, table_name, data):
        #placeholders = ', '.join('?' * len(data))
        #self.cursor.execute(f'INSERT INTO {table_name} VALUES ({placeholders})', data)
        #self.conn.commit()

    #def select_data(self, table_name, columns=None):
        #if columns:
            #columns_str = ', '.join(columns)
        #else:
            #columns_str = '*'
        #self.cursor.execute(f'SELECT {columns_str} FROM {table_name}')
        #return self.cursor.fetchall()
    
    #def select(self, table_name, columns='*', where=None):
        #if where is None:
            #query = f'SELECT {columns} FROM {table_name}'
        #else:
            #query = f'SELECT {columns} FROM {table_name} WHERE {where}'
        #self.cursor.execute(query)
        #rows = self.cursor.fetchall()
        #columns = [col[0] for col in self.cursor.description]
        #return [dict(zip(columns, row)) for row in rows]
    
    #def update_data(self, table_name, set_values, where_clause):
        #set_values_str = ', '.join([f'{key}=?' for key in set_values.keys()])
        #where_clause_str = ' AND '.join([f'{key}=?' for key in where_clause.keys()])
        #values = tuple(set_values.values()) + tuple(where_clause.values())
        #self.cursor.execute(f'UPDATE {table_name} SET {set_values_str} WHERE {where_clause_str}', values)
        #self.conn.commit()

    #def delete_data(self, table_name, where_clause):
        #where_clause_str = ' AND '.join([f'{key}=?' for key in where_clause.keys()])
        #values = tuple(where_clause.values())
        #self.cursor.execute(f'DELETE FROM {table_name} WHERE {where_clause_str}', values)
        #self.conn.commit()

    #def close(self):
        #self.conn.close()
import sqlite3

class SQLiteHandler:
    def __init__(self, db_file):
        self.db_file = db_file
        #self.conn = None
        self.conn = sqlite3.connect(self.db_file)
        #self.cursor = None
        self.cursor = self.conn.cursor()
        print('#####################################3', self.conn, self.cursor)

    #def connect(self):
        
        #self.conn = sqlite3.connect(self.db_file)
        #self.cursor = self.conn.cursor()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def execute(self, query, params=None):
        if not self.conn or not self.cursor:
            self.connect()
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        self.conn.commit()
        return self.cursor.lastrowid

    def fetch_one(self, query, params=None):
        if not self.conn or not self.cursor:
            self.connect()
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchone()

    def fetch_all(self, query, params=None):
        if not self.conn or not self.cursor:
            self.connect()
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()

    def create_table(self, table_name, columns):
        query = f"CREATE TABLE IF NOT EXISTS {table_name}("
        for column, data_type in columns.items():
            query += f"{column} {data_type},"
        query = query[:-1] + ")"
        self.execute(query)

    def insert(self, table_name, data):
        query = f"INSERT INTO {table_name}("
        placeholders = ""
        values = []
        for column, value in data.items():
            query += f"{column},"
            placeholders += "?,"
            values.append(value)
        query = query[:-1] + ") VALUES(" + placeholders[:-1] + ")"
        self.execute(query, values)

    def select(self, table_name, where=None):
        query = f"SELECT * FROM {table_name}"
        if where:
            query += f" WHERE {where}"
        return self.fetch_one(query)

    def update(self, table_name, data, where=None):
        query = f"UPDATE {table_name} SET "
        values = []
        for column, value in data.items():
            query += f"{column}=?,"
            values.append(value)
        query = query[:-1]
        if where:
            query += f" WHERE {where}"
        self.execute(query, values)
