from multiprocessing import Process
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import pandas as pd
from config import BASE_URL
from time import sleep
import cloudscraper
from bs4 import BeautifulSoup
import cloudscraper
from dotenv import load_dotenv
import os
from google.cloud import bigquery
from config import BASE_URL, PROJECT_ID, DATASET_ID, TABLE_ID, SCHEMA
load_dotenv()


def startScraping(contract, client):
    data=[
        {
            "contract":contract,
            "domain_name":"",
            "reverse_resolved_address":"",
            "reverse_expiration_date":"",
            "reverse_registrant":"",
            "reverse_parent":"",
            "reverse_controller":"",
            "reverse_token_id":"",
            "reverse_other_addresses":"",
            "reverse_content":"",
            "reverse_text_records":[],
            "reverse_owner":"",
            "reverse_single_chain_records":[],
            "reverse_multi_chain_records":[],
            "reverse_other_records":[],
            "domain_resolved_address":"",
            "domain_expiration_date":"",
            "domain_registrant":"",
            "domain_parent":"",
            "domain_controller":"",
            "domain_token_id":"",
            "domain_other_addresses":"",
            "domain_content":"",
            "domain_text_records":[],
            "domain_owner":"",
            "domain_single_chain_records":[],
            "domain_multi_chain_records":[],
            "domain_other_records":[],
        }     
    ]
    contract=contract
    domain_name=""
    reverse_resolved_address=""
    reverse_expiration_date=""
    reverse_registrant=""
    reverse_parent=""
    reverse_controller=""
    reverse_token_id=""
    reverse_other_addresses=""
    reverse_content=""
    reverse_text_records=[""]
    reverse_owner=""
    reverse_single_chain_records=[""]
    reverse_multi_chain_records=[""]
    reverse_other_records=[""]
    domain_resolved_address=""
    domain_expiration_date=""
    domain_registrant=""
    domain_parent=""
    domain_controller=""
    domain_token_id=""
    domain_other_addresses=""
    domain_content=""
    domain_text_records=[""]
    domain_owner=""
    domain_single_chain_records=[""]
    domain_multi_chain_records=[""]
    domain_other_records=[""]
    count=0
    # table=client.get_table("token-filters.etherescan_ens.ens_detail_records")
    table=client.get_table("token-filters.etherescan_ens.ens_details")
    try:
        service = Service(executable_path="C:\chrome\chromedriver.exe")
        options = Options()
        # options.add_argument("--no-sandbox")
        # options.add_argument("--disable-dev-shm-usage")
        # options.add_argument("--force-dark-mode")
        # options.add_argument("--start-maximized")
        options.add_experimental_option("debuggerAddress", f"127.0.0.1:9900/json")
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.217 Safari/537.36")
        driver = webdriver.Chrome(service=service, options=options)
        actions=ActionChains(driver)
        # scraper=cloudscraper.create_scraper()
        driver.get(f"{BASE_URL}{contract}")
        sleep(1)
        try:
            reverse_record=driver.find_element(By.CSS_SELECTOR,"div.col-md-9.mb-n1").text
            if reverse_record == "":
                raise Exception("No reverse record found")
            total_number=int(driver.find_element(By.ID,"ownedDomainNamesTable_info").find_element(By.TAG_NAME,"strong").text)
            page_number=int(total_number/10)
            if total_number%10==0:
                page_number-=1
            overview_link=driver.find_element(By.CSS_SELECTOR,"div.col-md-9.mb-n1").find_element(By.TAG_NAME,"a").get_attribute("href")
            driver.get(f"{overview_link}")
            sleep(0.5)
            # try:
            #     # more_button=driver.find_element(By.CSS_SELECTOR,"span.link-collapse-default")
            #     # actions.move_to_element(more_button).click().perform()
            #     driver.find_element(By.CSS_SELECTOR,"span.link-collapse-default").click()
            #     sleep(0.5)
            # except Exception as e:
            #     pass
            print("Reverse record------------------------------------------------------------------------------->")
            # soup=BeautifulSoup(overview,"html.parser")
            try:
                reverse_resolved_address=driver.find_element(By.ID,"txtEthereumAddress").get_attribute("innerHTML")
                if reverse_resolved_address != "":
                    print("reverse_resolved_address------------>", reverse_resolved_address)
            except Exception as e:
                pass
            try:
                reverse_expiration_date=driver.find_element(By.ID,"ContentPlaceHolder1_divENSExpiration").find_element(By.CSS_SELECTOR,"div.col-md-9.mb-n1").text
                if reverse_expiration_date != "":
                    print("reverse_expiration_date------------->", reverse_expiration_date)
            except Exception as e:
                pass
            try:
                reverse_registrant=driver.find_element(By.ID,"ContentPlaceHolder1_divRegistrant").find_element(By.CSS_SELECTOR,"div.col-md-9.mb-n1").find_element(By.TAG_NAME,"a").get_attribute("innerHTML")
                if reverse_registrant != "":
                    print("reverse_registrant------------------>", reverse_registrant)
            except Exception as e:
                pass
            try:
                reverse_parent=driver.find_element(By.ID,"ContentPlaceHolder1_divENSParentOfSubDomain").find_element(By.CSS_SELECTOR,"div.col-md-9.mb-n1").find_element(By.TAG_NAME,"a").get_attribute("innerHTML")
                if reverse_parent != "":
                    print("reverse_parent---------------------->", reverse_parent)
            except Exception as e:
                pass
            try:
                reverse_controller=resolved_address
                print("reverse_controller------------------>", reverse_controller)
            except Exception as e:
                pass
            try:
                reverse_token_id=driver.find_element(By.ID,"collapseDetail").find_element(By.CSS_SELECTOR,"div.col-md-9.mb-n1.text-truncate").get_attribute("innerHTML")
                if reverse_token_id != "":
                    print("reverse_token_id-------------------->", reverse_token_id)
            except Exception as e:
                pass
            try:
                coin_type=driver.find_element(By.CSS_SELECTOR,"div.col-4.col-md-2.text-muted.divCoinType").get_attribute("innerHTML")
                coin_address=driver.find_element(By.ID,"ContentPlaceHolder1_divOtherAddresses").find_element(By.CSS_SELECTOR,"div.col-8.col-md-10").find_element(By.TAG_NAME,"a").get_attribute("innerHTML")
                if coin_address != "" and coin_type != "":
                    print("reverse_other addresses------------->", coin_type, coin_address)
                    reverse_other_addresses=f"{coin_type}   {coin_address}"
            except Exception as e:
                pass
            try:
                reverse_content=driver.find_element(By.ID,"divContentHashData").find_element(By.TAG_NAME,"a").get_attribute("innerHTML")
                if reverse_content != "":
                    print("reverse_ContentHash----------------->", reverse_content)
            except Exception as e:
                pass
            try:
                text_records=driver.find_element(By.ID,"divTextRecordsContent").find_elements(By.TAG_NAME,"li")
                if text_records != []:
                    print("reverse_Text records---------------->\n")
                    for text_record in text_records:
                        reverse_text_records.append(text_record.find_elements(By.TAG_NAME,"div")[0].get_attribute("innerHTML")+":"+text_record.find_elements(By.TAG_NAME,"div")[1].find_element(By.TAG_NAME,"a").get_attribute("innerHTML"))
                        print(text_record.find_elements(By.TAG_NAME,"div")[0].get_attribute("innerHTML"),":",text_record.find_elements(By.TAG_NAME,"div")[1].find_element(By.TAG_NAME,"a").get_attribute("innerHTML"))
                    del reverse_text_records[0]
            except Exception as e:
                pass
            
            #######################################################################
            try:
                reverse_owner=driver.find_element(By.ID,"spanOwnerAddress").get_attribute("innerHTML")
                if reverse_owner!= "":
                    print("reverse_owner-------------------->", reverse_owner)
            except Exception as e:
                pass
            try:
                single_chain_records=driver.find_element(By.ID,"ContentPlaceHolder1_divSingleChainRecords").find_elements(By.TAG_NAME,"li")
                if single_chain_records != []:
                    print("reverse_single_chain_records-------------------->")
                    for single_chain_record in single_chain_records:
                        reverse_single_chain_records.append(single_chain_record.find_elements(By.TAG_NAME,"div")[0].get_attribute("innerHTML")+":"+single_chain_record.find_elements(By.TAG_NAME,"div")[1].get_attribute("innerHTML"))
                        print(single_chain_record.find_elements(By.TAG_NAME,"div")[0].get_attribute("innerHTML"),":",single_chain_record.find_elements(By.TAG_NAME,"div")[1].get_attribute("innerHTML"))
                    del reverse_single_chain_records[0]
            except Exception as e:
                pass
            try:
                multi_chain_records=driver.find_element(By.ID,"ContentPlaceHolder1_divMultiChainRecords").find_elements(By.TAG_NAME,"li")
                if multi_chain_records != []:
                    print("---------------->reverse_multi chain records")
                    for multi_chain_record in multi_chain_records:
                        reverse_multi_chain_records.append(multi_chain_record.find_elements(By.TAG_NAME,"div")[0].get_attribute("innerHTML")+":"+multi_chain_record.find_elements(By.TAG_NAME,"div")[1].get_attribute("innerHTML"))
                        print(multi_chain_record.find_elements(By.TAG_NAME,"div")[0].get_attribute("innerHTML"),":",multi_chain_record.find_elements(By.TAG_NAME,"div")[1].get_attribute("innerHTML"))
                    del reverse_multi_chain_records[0]
            except Exception as e:
                pass
            try:
                other_records=driver.find_element(By.ID,"ContentPlaceHolder1_divOtherRecords").find_elements(By.TAG_NAME,"li")
                if other_records != []:
                    print("---------------->reverse_other records")
                    for other_record in other_records:
                        reverse_other_records.append(other_record.find_elements(By.TAG_NAME,"div")[0].get_attribute("innerHTML")+":"+other_record.find_elements(By.TAG_NAME,"div")[1].get_attribute("innerHTML"))
                        print(other_record.find_elements(By.TAG_NAME,"div")[0].get_attribute("innerHTML"),":",other_record.find_elements(By.TAG_NAME,"div")[1].get_attribute("innerHTML"))
                    del reverse_other_records[0]
            except Exception as e:
                pass
            driver.back()
            sleep(0.5)
            while True:
                try:
                    domain_elements=driver.find_element(By.TAG_NAME,'tbody').find_elements(By.TAG_NAME,'tr')
                except Exception as e:
                    pass
                for element in domain_elements:
                    domain_name=element.text
                    print("domain-------------------------------------------------------------------------------------->", domain_name)
                    link=element.find_element(By.TAG_NAME,"a").get_attribute("href")
                    driver.get(link)
                    sleep(1)
                    # try:
                    #     # more_button=driver.find_element(By.CSS_SELECTOR,"span.link-collapse-default")
                    #     # actions.move_to_element(more_button).click().perform()
                    #     driver.find_element(By.CSS_SELECTOR,"span.link-collapse-default").click()
                    #     sleep(0.5)
                    # except Exception as e:
                    #     pass
                    
                    # soup=BeautifulSoup(overview,"html.parser")
                    try:
                        domain_resolved_address=driver.find_element(By.ID,"txtEthereumAddress").get_attribute("innerHTML")
                        if domain_resolved_address != "":
                            print("domain_resolved_address------------>", domain_resolved_address)
                    except Exception as e:
                        pass
                    try:
                        domain_expiration_date=driver.find_element(By.ID,"ContentPlaceHolder1_divENSExpiration").find_element(By.CSS_SELECTOR,"div.col-md-9.mb-n1").text
                        if domain_expiration_date != "":
                            print("domain_expiration_date------------->", domain_expiration_date)
                    except Exception as e:
                        pass
                    try:
                        domain_registrant=driver.find_element(By.ID,"ContentPlaceHolder1_divRegistrant").find_element(By.CSS_SELECTOR,"div.col-md-9.mb-n1").find_element(By.TAG_NAME,"a").get_attribute("innerHTML")
                        if domain_registrant != "":
                            print("domain_registrant------------------>", domain_registrant)
                    except Exception as e:
                        pass
                    try:
                        domain_parent=driver.find_element(By.ID,"ContentPlaceHolder1_divENSParentOfSubDomain").find_element(By.CSS_SELECTOR,"div.col-md-9.mb-n1").find_element(By.TAG_NAME,"a").get_attribute("innerHTML")
                        if domain_parent != "":
                            print("domain_parent---------------------->", domain_parent)
                    except Exception as e:
                        pass
                    try:
                        domain_controller=resolved_address
                        print("domain_controller------------------>", domain_controller)
                    except Exception as e:
                        pass
                    try:
                        domain_token_id=driver.find_element(By.ID,"collapseDetail").find_element(By.CSS_SELECTOR,"div.col-md-9.mb-n1.text-truncate").get_attribute("innerHTML")
                        if domain_token_id != "":
                            print("domain_token_id-------------------->", domain_token_id)
                    except Exception as e:
                        pass
                    try:
                        coin_type=driver.find_element(By.CSS_SELECTOR,"div.col-4.col-md-2.text-muted.divCoinType").get_attribute("innerHTML")
                        coin_address=driver.find_element(By.ID,"ContentPlaceHolder1_divOtherAddresses").find_element(By.CSS_SELECTOR,"div.col-8.col-md-10").find_element(By.TAG_NAME,"a").get_attribute("innerHTML")
                        if coin_address != "" and coin_type != "":
                            print("domain_other addresses------------->", coin_type, coin_address)
                            domain_other_addresses=f"{coin_type}   {coin_address}"
                    except Exception as e:
                        pass
                    try:
                        domain_content=driver.find_element(By.ID,"divContentHashData").find_element(By.TAG_NAME,"a").get_attribute("innerHTML")
                        if domain_content != "":
                            print("domain_ContentHash----------------->", domain_content)
                    except Exception as e:
                        pass
                    try:
                        text_records=driver.find_element(By.ID,"divTextRecordsContent").find_elements(By.TAG_NAME,"li")
                        if text_records != []:
                            print("domain_Text records---------------->\n")
                            for text_record in text_records:
                                domain_text_records.append(text_record.find_elements(By.TAG_NAME,"div")[0].get_attribute("innerHTML")+":"+text_record.find_elements(By.TAG_NAME,"div")[1].find_element(By.TAG_NAME,"a").get_attribute("innerHTML"))
                                print(text_record.find_elements(By.TAG_NAME,"div")[0].get_attribute("innerHTML"),":",text_record.find_elements(By.TAG_NAME,"div")[1].find_element(By.TAG_NAME,"a").get_attribute("innerHTML"))
                            del domain_text_records[0]
                    except Exception as e:
                        pass
                    
                    try:
                        domain_owner=driver.find_element(By.ID,"spanOwnerAddress").get_attribute("innerHTML")
                        if domain_owner!= "":
                            print("domain_owner-------------------->", domain_owner)
                    except Exception as e:
                        pass
                    try:
                        single_chain_records=driver.find_element(By.ID,"ContentPlaceHolder1_divSingleChainRecords").find_elements(By.TAG_NAME,"li")
                        if single_chain_records != []:
                            print("domain_single_chain_records-------------------->")
                            for single_chain_record in single_chain_records:
                                domain_single_chain_records.append(single_chain_record.find_elements(By.TAG_NAME,"div")[0].get_attribute("innerHTML")+":"+single_chain_record.find_elements(By.TAG_NAME,"div")[1].get_attribute("innerHTML"))
                                print(single_chain_record.find_elements(By.TAG_NAME,"div")[0].get_attribute("innerHTML"),":",single_chain_record.find_elements(By.TAG_NAME,"div")[1].get_attribute("innerHTML"))
                            del domain_single_chain_records[0]
                    except Exception as e:
                        pass
                    try:
                        multi_chain_records=driver.find_element(By.ID,"ContentPlaceHolder1_divMultiChainRecords").find_elements(By.TAG_NAME,"li")
                        if multi_chain_records != []:
                            print("---------------->domain_multi chain records")
                            for multi_chain_record in multi_chain_records:
                                domain_multi_chain_records.append(multi_chain_record.find_elements(By.TAG_NAME,"div")[0].get_attribute("innerHTML")+":"+multi_chain_record.find_elements(By.TAG_NAME,"div")[1].get_attribute("innerHTML"))
                                print(multi_chain_record.find_elements(By.TAG_NAME,"div")[0].get_attribute("innerHTML"),":",multi_chain_record.find_elements(By.TAG_NAME,"div")[1].get_attribute("innerHTML"))
                            del domain_parent_multi_chain_records[0]
                    except Exception as e:
                        pass
                    try:
                        other_records=driver.find_element(By.ID,"ContentPlaceHolder1_divOtherRecords").find_elements(By.TAG_NAME,"li")
                        if other_records != []:
                            print("---------------->domain_other records")
                            for other_record in other_records:
                                domain_other_records.append(other_record.find_elements(By.TAG_NAME,"div")[0].get_attribute("innerHTML")+":"+other_record.find_elements(By.TAG_NAME,"div")[1].get_attribute("innerHTML"))
                                print(other_record.find_elements(By.TAG_NAME,"div")[0].get_attribute("innerHTML"),":",other_record.find_elements(By.TAG_NAME,"div")[1].get_attribute("innerHTML"))
                            del domain_other_records[0]
                    except Exception as e:
                        pass
                    try:
                        new_data={
                            "contract":contract,
                            "domain_name":domain_name,
                            "reverse_resolved_address":reverse_resolved_address,
                            "reverse_expiration_date":reverse_expiration_date,
                            "reverse_registrant":reverse_registrant,
                            "reverse_parent":reverse_parent,
                            "reverse_controller":reverse_controller,
                            "reverse_token_id":reverse_token_id,
                            "reverse_other_addresses":reverse_other_addresses,
                            "reverse_content":reverse_content,
                            "reverse_text_records":reverse_text_records,
                            "reverse_owner":reverse_owner,
                            "reverse_single_chain_records":reverse_single_chain_records,
                            "reverse_multi_chain_records":reverse_multi_chain_records,
                            "reverse_other_records":reverse_other_records,
                            "domain_resolved_address":domain_resolved_address,
                            "domain_expiration_date":domain_expiration_date,
                            "domain_registrant":domain_registrant,
                            "domain_parent":domain_parent,
                            "domain_controller":domain_controller,
                            "domain_token_id":domain_token_id,
                            "domain_other_addresses":domain_other_addresses,
                            "domain_content":domain_content,
                            "domain_text_records":domain_text_records,
                            "domain_owner":domain_owner,
                            "domain_single_chain_records":domain_single_chain_records,
                            "domain_multi_chain_records":domain_multi_chain_records,
                            "domain_other_records":domain_other_records
                        }     
                        data.append(new_data)
                    except Exception as e:
                        print(e)
                    domain_name=""
                    domain_resolved_address=""
                    domain_expiration_date=""
                    domain_registrant=""
                    domain_parent=""
                    domain_controller=""
                    domain_token_id=""
                    domain_other_addresses=""
                    domain_content=""
                    domain_text_records=[""]
                    domain_owner=""
                    domain_single_chain_records=[""]
                    domain_multi_chain_records=[""]
                    domain_other_records=[""]
                    
                    # count+=1
                    driver.back()
                if page_number>0:
                    try:
                        # next_element=driver.find_element(By.ID, "ownedDomainNamesTable_paginate").find_elements(By.TAG_NAME,'li')[3]
                        # actions.move_to_element(next_element).click().perform()
                        # driver.find_element(By.ID, "ownedDomainNamesTable_next").click()
                        driver.execute_script('document.querySelector("li[id=\'ownedDomainNamesTable_next\']").click()')
                        sleep(1)
                        page_number-=1
                    except Exception as e:
                        print("There is no next button")
                else:
                    break
            # overview=scraper.get(f"{BASE_URL}{reverse_record}").text
            # actions.move_to_element(reverse_record).click().perform()
            
            del data[0]
            error=client.insert_rows_json(table, data)
            if error:
                print("Encountered errors while inserting rows")
                print(error)
            else:
                print("Data was inserted successfully")
            print("********************************************")
        except Exception as e:
            error=client.insert_rows_json(table, data)
            if error:
                print("Encountered errors while inserting rows")
                print(error)
            else:
                print("Data was inserted successfully")
            print(e)
            print("********************************************")
    except Exception as e:
        print("Something went wrong, please try again later")
        print(e)
        

if __name__=="__main__":
    try:
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="./adc.json"
        os.environ["GCLOUD_PROJECT"] = "token-filters"
        client=bigquery.Client()
        print("Connected to bigquery")
        query = f"SELECT wallet_address from {PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"
        print("Getting data from bigquery...")
        wallet_query=client.query(query)
        CONTRACT_LIST=wallet_query.result()
        print("Data has been loaded from bigquery")
    except Exception as e:
        print("Failed to connect to bigquery")
        print(e)
    for CONTRACT in CONTRACT_LIST:
        print("---------------------->contract\n",CONTRACT.wallet_address)
        # process=Process(target=startScraping, args=(f"{9017+i}",CONTRACT_LIST[i]))
        # process.start()
        # print("process started")
        startScraping(CONTRACT.wallet_address, client)