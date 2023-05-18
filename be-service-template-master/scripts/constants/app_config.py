from configparser import  ConfigParser
import sys


try:
    config = ConfigParser(interpolation=None)
    config.read("conf/application.conf")
except Exception as e:
    print(f"Error while loading the config: {e}")
    print("Failed to Load Configuration. Exiting!!!")
    sys.stdout.flush()
    sys.exit()


class DBConf:
    DB_URI = config.get("MONGO_DETAILS", "DB_URI")
    if not DB_URI:
        print("Error, environment variable DB_URI not set")
        sys.exit(1)
        
    DB_DATABASE = config.get("MONGO_DETAILS", "DB_DATABASE")
    if not DB_DATABASE:
        print("Error, environment variable DB_DATABASE not set")
        sys.exit(1)
        
    DB_COLLECTION = config.get("MONGO_DETAILS", "DB_COLLECTION")
    if not DB_COLLECTION:
        print("Error, environment variable DB_COLLECTION not set")
        sys.exit(1)