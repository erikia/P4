from Controllers import Connection
from Controllers.ApplicationCtrl import ApplicationCtrl


def main():
    application = ApplicationCtrl()
    application.start()


if __name__ == '__main__':
    main()
    Connection().close_db()

    
