from registration_site import cron

def backup_database():
  print "Backing up database to dropbox account at usimc2017tech@gmail.com"
  cron.backup_database()