from sqlite_handler.database import SQLiteHandler


class ConfigHandler:
    def __init__(self, db_name='./config_handler/config.db'):
        self.db_handler = SQLiteHandler(db_name)
        self.create_config_table()
        self.default_config = {
            'exchange': 'bybit',
            'api_key': 'YWCeoBdf0Y2LqL59TQ',
            'api_secret': 'R7e2lbwDKXqzlR3bk1wckfmjdCI6vSIfYH2S'
        }
        #self.set_config(self.default_config)
        
    def create_config_table(self):
        self.db_handler.create_table('config', {'key': 'text', 'value': 'text'})

    def set_config(self, configs):
        if configs['api_key'].strip() == '' or configs['api_secret'].strip() == '':
            for key_def, value_def in self.default_config.items():
                    if not self.db_handler.select('config', where=f'key="{key_def}"'):
                        self.db_handler.insert('config', {'key': key_def, 'value': value_def})
        else:
            for key, value in configs.items():
            #if not self.db_handler.select('config', where=f'key="{key}"')
                self.db_handler.insert('config', {'key': key, 'value': value})
            
