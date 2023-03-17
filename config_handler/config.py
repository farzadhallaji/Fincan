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
        for key, value in configs.items():
            print('|'+value+'|')
            if value != '':
                self.db_handler.insert('config', {'key': key, 'value': value})
            else:
                for key_def, value_def in self.default_config.items():
                    if not self.db_handler.select('config', where=f'key="{key_def}"'):
                        self.db_handler.insert('config', {'key': key_def, 'value': value_def})
                break
            #if value != '':
                #if not self.db_handler.select_data('config', where=f'key="{key}"'):
                    #self.db_handler.insert_data('config', {'key': key, 'value': value})
            #else:
                #self.db_handler.insert_data('config', {'key': key, 'value': self.default_config[key]})
