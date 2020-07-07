# Activity Logger

## Installation
-- *requirements: python3.5+*
##### Follow the below steps to install and run the project

```bash
$ mkdir app_dir && cd app_dir
$ git clone git@github.com:gouravtulsani/activity_logger.git
$ python -m venv .
$ source bin/activate
$ cd activity_logger
$ pip install -r requirements.txt  # install requirements
# make migrations and apply them
$ python manage.py makemigrations
$ python manage.py migrate
# use custom management command to generate dummy data
$ python manage.py add_dummy_data
# start the server
$ python manage.py runserver
```

## APIs:

1. `/activities`
```json
{
    "ok": true,
    "members": [
        {
            "id": 17,
            "real_name": "Test User1",
            "tz": "Asia/Kolkata",
            "activity_periods": [
                {
                    "start_time": "2020-07-05T23:14:35.754Z",
                    "end_time": "2020-07-06T08:44:35.754Z"
                },
                {
                    "start_time": "2020-07-03T21:12:35.754Z",
                    "end_time": "2020-07-04T08:44:35.754Z"
                }
            ]
        }, ...
    ]
}
```
2. `/activity/<user_id>`
```json
{
  "ok": true,
  "activity_periods": [
    {
      "start_time": "2020-07-04T20:52:35.754Z",
      "end_time": "2020-07-05T08:44:35.754Z"
    },
    {
      "start_time": "2020-07-05T23:14:35.754Z",
      "end_time": "2020-07-06T08:44:35.754Z"
    }, ...
  ]
}
```
