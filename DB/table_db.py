import sqlite3

class Table():
    def __init__(self, cursor):
        self.cursor = cursor
        
        self.create_table_manufacturer()
        self.create_table_gateway()
        self.create_table_actuator()
        self.create_table_sensor()
        self.create_table_context_server()
        self.create_table_persistance()
        self.create_table_scheduler()

    def create_table_manufacturer(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS manufacturer (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                web_site TEXT
            ); 
        """)

    def create_table_gateway(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS gateway (
                uuid INTEGER PRIMARY KEY,
                name TEXT,
                ip TEXT NOT NULL,
                port INTEGER NOT NULL,
                user TEXT NOT NULL,
                password TEXT NOT NULLam,
                manufacturer_id INTEGER NOT NULL,
                FOREIGN KEY (manufacturer_id) REFERENCES manufacturer (id)
            ); 
        """)

    def create_table_actuator(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS actuator (
                uuid INTEGER PRIMARY KEY,
                name TEXT,
                manufacturer_id INTEGER NOT NULL,
                gateway_id INTEGER NOT NULL,
                FOREIGN KEY (manufacturer_id) REFERENCES manufacturer (id),
                FOREIGN KEY (gateway_id) REFERENCES gateway (uuid)
            ); 
        """)
    
    def create_table_sensor(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS sensor (
                uuid INTEGER PRIMARY KEY,
                name TEXT,
                unit TEXT,
                manufacturer_id INTEGER NOT NULL,
                gateway_id INTEGER NOT NULL,
                FOREIGN KEY (manufacturer_id) REFERENCES manufacturer (id),
                FOREIGN KEY (gateway_id) REFERENCES gateway (uuid),
            ); 
        """)
    
    def create_table_context_server(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS context_server (
                uuid INTEGER PRIMARY KEY,
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
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                value INTEGER,
                collect_date TEXT, 
                publisher BLOB,
                sensor_id INTEGER NOT NULL,
                context_server_id INTEGER NOT NULL,
                FOREIGN KEY (sensor_id) REFERENCES sensor (uuid),
                FOREIGN KEY (context_server_id) REFERENCES context_server (uuid)
            ); 
        """)

    def create_table_scheduler(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS scheduler (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                event TEXT NOT NULL,
                second TEXT NOT NULL,
                minute TEXT NOT NULL,
                hour TEXT NOT NULL,
                day TEXT NOT NULL,
                month TEXT NOT NULL,
                year TEXT NOT NULL,
                sensor_id INTEGER NOT NULL,
                FOREIGN KEY (sensor_id) REFERENCES sensor (uuid)
            ); 
        """)

    def create_table_action_rule(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS action_rule (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                command TEXT NOT NULL
            ); 
        """)

    def create_table_rule(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS rule (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                rule TEXT,
                action_rule_id INTEGER NOT NULL,
                sensor_rule_id INTEGER NOT NULL,
                sensor_id INTEGER NOT NULL,
                FOREIGN KEY (action_rule_id) REFERENCES action_rule (id),
                FOREIGN KEY (sensor_rule_id) REFERENCES sensor_rule (id),
                FOREIGN KEY (sensor_id) REFERENCES sensor (uuid),
            ); 
        """)

    def create_table_sensor_rule(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS sensor_rule (
                rule_id INTEGER NOT NULL,
                sensor_id INTEGER NOT NULL,
                FOREIGN KEY (rule_id) REFERENCES rule (id),
                FOREIGN KEY (sensor_id) REFERENCES sensor (uuid)
            ); 
        """)

    