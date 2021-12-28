from app.database.database import DataBase
from app.db_interaction import DBHandler
from app.interface.ui import UI


def main():
    db_h = DBHandler(DataBase())
    UI(db_h)


if __name__ == "__main__":
    main()

