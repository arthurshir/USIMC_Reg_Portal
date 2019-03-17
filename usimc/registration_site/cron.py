from django.core.management import call_command

def backup_database():
  print "Backing up database to dropbox account at usimc2017tech@gmail.com"
  call_command('dbbackup')