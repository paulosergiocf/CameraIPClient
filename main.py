from src.config.db_sessions import create_tables

from dotenv import load_dotenv

load_dotenv()

if __name__=='__main__':
    create_tables()