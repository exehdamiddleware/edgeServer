import sqlite3

class Table():
    def __init__(self, cursor):
        self.cursor = cursor
        
        self.create_table_manufacturer()
        self.create_table_gateway()
        self.create_table_device()
        self.create_table_context_server()
        self.create_table_persistance()
        self.create_table_scheduler()
        self.create_table_action_rule()
        self.create_table_rule()

    def create_table_manufacturer(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS manufacturer (
                id INTEGER NOT NULL PRIMARY KEY,
                name TEXT NOT NULL,
                address TEXT,
                phone TEXT,
                url TEXT,
                city TEXT,
                state TEXT,
                country TEXT
            ); 
        """)

    def create_table_gateway(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS gateway (
                uuid TEXT NOT NULL PRIMARY KEY,
                name TEXT NOT NULL,
                status INTEGER NOT NULL,
                manufacturer_id INTEGER,
                FOREIGN KEY (manufacturer_id) REFERENCES manufacturer (id)
            ); 
        """)
    
    def create_table_device(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS device (
                uuid TEXT NOT NULL PRIMARY KEY,
                name TEXT,
                description TEXT,
                model TEXT,
                precision TEXT,
                unit TEXT,
                pin INTEGER NOT NULL,
                driver TEXT NOT NULL,
                manufacturer TEXT,
                gateway_id TEXT NOT NULL,
                -- FOREIGN KEY (manufacturer_id) REFERENCES manufacturer (id),
                FOREIGN KEY (gateway_id) REFERENCES gateway (uuid)
            ); 
        """)
    
    def create_table_context_server(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS context_server (
                uuid TEXT NOT NULL PRIMARY KEY,
                name TEXT,
                ip TEXT NOT NULL,
                port INTEGER NOT NULL,
                user TEXT NOT NULL,
                password TEXT NOT NULL
            ); 
        """)

    def create_table_persistance(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS persistance (
                id INTEGER NOT NULL PRIMARY KEY,
                value INTEGER NOT NULL,
                collect_date TEXT NOT NULL, 
                publisher INTEGER NOT NULL,
                device_uuid TEXT NOT NULL,
                FOREIGN KEY (device_uuid) REFERENCES device (uuid)
            ); 
        """)

    def create_table_scheduler(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS scheduler (
                id INTEGER NOT NULL PRIMARY KEY,
                event TEXT NOT NULL,
                second TEXT NOT NULL,
                minute TEXT NOT NULL,
                hour TEXT NOT NULL,
                day TEXT NOT NULL,
                month TEXT NOT NULL,
                year TEXT NOT NULL,
                device_uuid TEXT NOT NULL,
                FOREIGN KEY (device_uuid) REFERENCES device (uuid)
            ); 
        """)

    def create_table_action_rule(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS action_rule (
                id INTEGER NOT NULL PRIMARY KEY,
                command TEXT NOT NULL
            ); 
        """)

    def create_table_rule(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS rule (
                id INTEGER NOT NULL PRIMARY KEY,
                name TEXT,
                rule TEXT,
                action_rule_id INTEGER,
                device_uuid TEXT NOT NULL,
                FOREIGN KEY (action_rule_id) REFERENCES action_rule (id),
                FOREIGN KEY (device_uuid) REFERENCES device (uuid)
            ); 
        """)

    # def create_table_sensor_rule(self):
    #     self.cursor.execute("""
    #         CREATE TABLE IF NOT EXISTS sensor_rule (
    #             rule_id INTEGER NOT NULL,
    #             sensor_id INTEGER NOT NULL,
    #             FOREIGN KEY (rule_id) REFERENCES rule (id),
    #             FOREIGN KEY (sensor_id) REFERENCES sensor (uuid)
    #         ); 
    #     """)

    