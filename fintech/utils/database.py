from sqlmodel import SQLModel, create_engine

sqliteFileName = "users.db"
sqliteUrl = f"sqlite:///{sqliteFileName}"

engine = create_engine(sqliteUrl, echo=True)

def createAll():
    SQLModel.metadata.create_all(engine) 