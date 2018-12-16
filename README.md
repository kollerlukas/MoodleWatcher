# MoodleWatcher
Simple Python Program that notifies you of new resources on the TUM Moodle page. 
I am planning to have this run maybe once a day on my Raspberry Pi.
## Setup
create a new file `creds.py` like this one:
```python
# app passwd for gmail smtp server
APP_PASSWD = 'your-google-app-passwd'
# my email addrs
FROM_ADDR = 'youremail0@gmail.com'
TO_ADDR = 'youremail1@gmail.com'
# my TUM Moodle login cred
TUM_MOODLE_MAIL = 'your-TUM-Moodle-Login'
TUM_MOODLE_PASSWD = 'your-TUM-Moodle-passwd'
```
run `python moodlewatcher.py`
(might need an inital run with [`mail.sendMail(sbj, msg)`]( https://github.com/kollerlukas/MoodleWatcher/blob/8a688daa932f9ca78cc729909f678d4a21c8646c/moodlewatcher.py#L36) commented out; otherwise you will receive a mail for every resource ever posted in a moodle where you where signed up)
