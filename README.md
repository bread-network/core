# Bread Network

## Setup Instructions

### Flask Setup
1. Install dependencies.
```shell
python -m venv env
source env/bin/activate
pip install requirements.txt
```

#### MongoDB Setup
1. Create new MongoDB database using the Mongo Console or MongoDB Compass with `bread` and keep the initial collection name as `users` and `sticks`
2. Create an admin user
   ```json
    use bread
    db.createUser({
        user: "myUserName",
        pwd:  passwordPrompt(),   
        roles: [ { role: "readWrite", db: "bread" },
                    { role: "read", db: "reporting" } ]
    })
   ```
3. Create a file `keys/mongo_keys.json` and follow the syntax described in `keys/mongo_keys.json.sample`. Write the collection names as the ones declared above. 

### Tweepy Setup
1. Create `keys/keys.json` similar to `keys/keys.json.sample` and write your `app_key`, `app_secret`, `oauth_token`, `oauth_token_secret` in the same format. 
2. You can add multiple keys in `keys.json` by following array declaration rules in JSON.

## Debug Run Instructions
1. After installing dependencies, run the Flask server using the command:
```shell
python main.py
```
The backend engine will be available at http://localhost:5000/ (5000 is the default port, might change according to the system.)
