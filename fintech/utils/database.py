from sqlmodel import SQLModel, create_engine
from servicios.loggingConfig import log
sqliteFileName = "users.db"
sqliteUrl = f"sqlite:///{sqliteFileName}"

engine = create_engine(sqliteUrl, echo=True)

def createAll():
    SQLModel.metadata.create_all(engine) 
    log("DEBUG","Se cargaron correctamente los modelos y se conecto a la base de datos.")