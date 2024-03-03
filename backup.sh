rds_endpoint="database-2.ch8e2wi8igi6.us-west-2.rds.amazonaws.com"
backupfolder=/home/ubuntu/backup

export TZ=Asia/Kolkata

user=geetanj
password=Geetanj$16

recipient_email=gs7732@srmist.edu.in
sqlfile=$backupfolder/rds-$(date +%d-%m-%Y_%H-%M-%S).sql
zipfile=$backupfolder/rds-$(date +%d-%m-%Y_%H-%M-%S).zip 

sudo mysqldump -h $rds_endpoint -u $user -p$password rds > $zipfile

if [ $? == 0 ]; then
        echo 'SQL dump created'
else
        echo 'mysqldump return non-zero code' | mailx -s 'No backup was created!' $recipient_email
        exit
fi

zip $zipfile $sqlfile 

if [ $? == 0 ]; then
        echo 'The backup was successfully compressed' 
else 
        echo 'Error compressing backup' | mailx -s 'Backup was not created!' $recipient_email 
        exit

fi 

rm $sqlfile 
echo $zipfile | mailx -s 'Backup was successfully created' $recipient_email 
 
find $backupfolder -mtime +$keep_day -delete
find "$backupfolder" -type f -mtime +30 -exec rm {} \;


### after this in crontab -e, modify it -> in the end 
### * * * * *  /bin/bash /home/ubuntu/backup/backup.sh
