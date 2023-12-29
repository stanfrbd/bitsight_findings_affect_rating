# bitsight_findings_affect_rating

For a better understanding, refer to the official Bitsight API documentation: https://help.bitsighttech.com/hc/en-us/articles/360022913734-GET-Finding-Details

# Dependencies

You might want to create a [`venv`](https://docs.python.org/3/library/venv.html) before installing the dependencies.

- `python3`
- `requests`

```
pip install requests
```

# Quick start

## Edit the config file
```
cp config-sample.json config.json
```

Then edit the config with the good values.

| Variable | Explaination |
|----------|--------------|
|`guid`| the GUID of your company|
|`name`| the display name of your company|
|`api_token`| mandatory|
|`proxy_url`| the proxy, if you need one.|

```
{
    "companies": [{
            "guid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "name": "My company1"
        },
        {
            "guid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "name": "My company2"
        },
        {
            "guid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "name": "My company3"
        }
    ],
    "api_token": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "proxy_url": ""
}
```

## Execute the script

```
PS C:\Users\Me\Test> python bitsight_findings_affect_rating.py
```

or

```
python3 bitsight_findings_affect_rating.py
```

## Output

- A CSV file will be created with `bitsight_findings_affect_rating-` + current date + `-export.csv`.

```
PS C:\Users\Me\Test> python .\bitsight_findings_affect_rating.py
... (output)
Generated CSV: ./bitsight_findings_affect_rating-2022-11-10-15_14_54-export.csv
```

# Errors

If the `config.json` is not properly filled.
```
General error: HTTP error: 401 check your config file and API Token
```
