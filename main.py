from Controllers import Connection
from Controllers.Connection import close_db
from Controllers.ApplicationCtrl import ApplicationCtrl



def main():
    application = ApplicationCtrl()
    application.start()


if __name__ == '__main__':
    main()
    close_db()

    
