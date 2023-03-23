import sqlite3
from threading import local

class SQLiteHandler:
    def __init__(self, db_file):
        self.db_file = db_file
        self._local = local()
        
    def _get_connection(self):
        if not hasattr(self._local, 'conn'):
            self._local.conn = sqlite3.connect(self.db_file)
        return self._local.conn
    
    def execute(self, query, params=()):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        return cursor
    
    def fetch(self, query, params=()):
        cursor = self.execute(query, params)
        return cursor.fetchall()
    
    def create_table(self, name, columns):
        column_defs = ', '.join([f'{name} {type}' for name, type in columns.items()])
        query = f'CREATE TABLE IF NOT EXISTS {name} ({column_defs})'
        self.execute(query)
    
    def insert(self, table, data):
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['?' for _ in data])
        query = f'INSERT INTO {table} ({columns}) VALUES ({placeholders})'
        self.execute(query, tuple(data.values()))
        
        
    def select(self, table, columns='*', where=None):
        query = f'SELECT {columns} FROM {table}'
        if where:
            query += f' WHERE {where}'
        cursor = self.execute(query)
        return cursor.fetchall()
    
    def update(self, table, data, where):
        columns = ', '.join([f'{col}=?' for col in data.keys()])
        query = f'UPDATE {table} SET {columns} WHERE {where}'
        self.execute(query, tuple(data.values()))