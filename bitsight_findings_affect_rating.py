import requests
import time
import json
from datetime import datetime

SEP = ";"
csv = ""

# Current date
now = datetime.now()
today = now.strftime("%Y-%m-%d-%H_%M_%S")

# API DOCUMENTATION: https://help.bitsighttech.com/hc/en-us/articles/360022913734-GET-Finding-Details
api_key = ""
companies = []
base_url = "https://api.bitsighttech.com/ratings/v1/companies/"
url_options = "/findings?limit=1000000000&affects_rating=true"
#url_options = "/findings?limit=1000000000&grade=WARN,BAD"

csv = "company" + SEP + "risk_vector" + SEP + "finding" + SEP + "finding_grade" + SEP + "affects_grade" + SEP + "first_seen" + SEP + "last_seen" + "\n"

def export_to_csv():
    print("\nGenerated CSV: ./security-headers-" + today + "-export.csv\n")
    f = open("bitsight_findings_affect_rating-" + today + "-export.csv", "a")
    f.write(csv)
    f.close()

def load_config():
        global api_key
        global companies
        f = open("config.json", "r")
        config = json.load(f)
        api_key = config["api_token"]
        companies = config["companies"]



def get_bitsight_results():

        global csv

        for company in companies:

                url =  base_url + company['guid'] + url_options
                response = requests.get(url, auth=(api_key, ""))
                # print(response.status_code)
                if response.status_code == 200:

                        json = response.json()
                        f = open(company['name'] + ".json", "wb")
                        f.write(response.text.encode("utf-8"))
                        f.close()
                        
                        time.sleep(2)

                        print("\nCompany name: ", company['name'])

                        for result in json['results']:
                                try:
                                        finding = result['evidence_key']
                                        risk_vector = result['risk_vector_label']
                                        finding_grade = result['details']['grade']
                                        affects_rating = result['affects_rating']
                                        first_seen = result['first_seen']
                                        last_seen = result['last_seen']

                                        csv += company['name'] + SEP + risk_vector + SEP + finding + SEP + finding_grade + SEP + str(affects_rating) + SEP + first_seen + SEP + last_seen + "\n"
                                        print(csv)

                                except KeyError:
                                        pass
                        
                else:
                        raise Exception("HTTP error: " + str(response.status_code))
                
        # write csv
        export_to_csv()


def main():
        load_config()
        get_bitsight_results()        

if __name__ == "__main__":
    try: 
        main() 
    except Exception as err: 
        print("General error : ", err) 
        exit(1)