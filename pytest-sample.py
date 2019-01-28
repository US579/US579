# coding:utf-8
from pymongo import MongoClient
from pymongo import errors
import re
import json
import requests
from bs4 import BeautifulSoup as bs

class crawl_tjgh(object):
    def __init__(self):
        self.base_url = 'https://www.carelink.cn/'
        self.getProxy()
        self.hospitalID_start = 3097
    def getProxy(self):
        client = MongoClient("mongodb://root:Mongodb789@dds-2ze92ad086cc41a4-pub.mongodb.rds.aliyuncs.com:3717/")
        db = client.medo_mango
        proxy_db = db.proxy
        self.proxies = {'http': i['ip'] for i in proxy_db.find()}
        return None
    def savedata2momgodb(self,doctor_information, hospital_information):
        docinfo_dict = {}
        docinfo_dict.update(doctor_information)
        docinfo_dict.update(hospital_information)
        client = MongoClient("mongodb://root:Mongodb789@dds-2ze92ad086cc41a4-pub.mongodb.rds.aliyuncs.com:3717/")
        db = client.medo_mango
        docinfo_db = db.doctor_info
        try:
            docinfo_db.insert_one(docinfo_dict)
        except errors.DuplicateKeyError:
            return None
        return None
    def clearText(self,text):
        rtext = re.sub(r'[\s\']', '', text)
        return rtext
    def parse_start(self):
        hospitalID = self.hospitalID_start
        while 1:
            url_add = 'hos/index.htm?hi=%d' % hospitalID
            url_hospital = self.base_url + url_add
            r = requests.post(url_hospital,proxies=self.proxies)
            self.parse_hospital(r,hospitalID)
            hospitalID += 1
            if hospitalID > 4812:
                break
    def parse_hospital(self,response,hospitalID):
        hospital_information = {
            "city": u'天津',
            "hospital": None,
            "hospital_tier": None,
            "hospital_address": None,
            "hospital_summary": None,
            "hospital_tel": None,
            "hospital_website": None,
            "source": "tjgh",
        }
        soup = bs(response.text,'html.parser')
        hospital_infor = soup.find('div',attrs={'class':'search-result-hospital-text'})
        if not hospital_infor:
            return None
        iline = 0
        for i in hospital_infor.find_all('p'):
            if iline == 0:
                hospital_information['hospital'] = self.clearText(i.getText().split(u' ')[0])
            if iline == 1:
                hospital_information['hospital_tier'] = self.clearText(i.getText())
            if iline == 2:
                hospital_information['hospital_tel'] = self.clearText(i.getText())
            if iline == 3:
                hospital_information['hospital_address'] = self.clearText(i.getText())
            iline += 1
        if hospital_information['hospital_address'] == None or u'天津' not in hospital_information['hospital_address']:
            if u'天津' not in hospital_information['hospital']:
                return None

        #hospital_information = json.dumps(hospital_information, encoding='utf-8', ensure_ascii=False)
        #print hospital_information
        listpage = 1
        while 1:
            url_add = '/hos/doctorsByDepartmentId.htm?hi=%d&consult_type=1&curr=%d' % (hospitalID,listpage)
            url_doctors = self.base_url+url_add
            r = requests.post(url_doctors,proxies=self.proxies)
            iflag = self.parse_doctors(r,hospitalID,hospital_information)
            if iflag:
                break
            listpage += 1
    def parse_doctors(self,response,hospitalID,hospital_infomation):
        rinfo = json.loads(response.content)
        doctors_info_list = rinfo['data']['doctorPageList']
        if not doctors_info_list:
            return 1
        for i in doctors_info_list:
            doctor_information = {
                "doc_id": None,
                "name": None,
                "department": None,
                "technical_title": None,
                "speciality": None,
                "summary": None,
                "changes": None,
                "source": 'tjgh'
            }
            doctor_information['doc_id'] = 'TJGH_'+str(hospitalID)+'_'+str(i['id'])
            doctor_information['name'] = i['name']
            doctor_information['department'] = i['departmentName']
            doctor_information['technical_title'] = i['doctorTitleName']
            doctor_information['speciality'] = i['skill']
            doctor_information['summary'] = i['skill']
            #doctor_information = json.dumps(doctor_information,ensure_ascii=False,encoding='utf-8')
            #print doctor_information
            self.savedata2momgodb(doctor_information,hospital_infomation)