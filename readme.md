# database backup/restore process

## setup
change the variables in the two python scripts to conform to the names of the database you are backing up. 

## backup
run `python backup-psql.py`

the database backup file should then be sen't to s3

## restore
if database needs to be restored run 
`python get-backup.py`
then from the command line run 
`psql {database name here} < restore.gz`