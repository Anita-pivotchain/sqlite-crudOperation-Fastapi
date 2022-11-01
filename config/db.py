from sqlalchemy import create_engine,MetaData

engine = create_engine("sqlite:///sqldb.db",connect_args={'check_same_thread': False})

meta = MetaData(bind=engine)

conn = engine.connect()
