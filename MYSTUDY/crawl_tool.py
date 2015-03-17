import urllib2
import re
from pymongo import MongoClient
import datetime as dt
import config_hk_stock
import time
import requests
from optparse import OptionParser

OPTION_SLEEP = True
SECS_TO_SLEEP = 2
leak_codes = []

# MONGO_HOST = '192.168.0.222'  # test
MONGO_HOST = '192.168.250.200'  # formal
client = MongoClient(MONGO_HOST, 27017)
db = client.ada
c1 = db.base_stock  # get org id by secu id
c2 = db.base_share_vary  # get details


def handle_stock_code(raw_code):
    code = ''
    if raw_code < 10:
        code = ''.join(['0000', str(raw_code), '_HK_EQ'])
    elif 10 <= raw_code < 100:
        code = ''.join(['000', str(raw_code), '_HK_EQ'])
    elif 100 <= raw_code < 1000:
        code = ''.join(['00', str(raw_code), '_HK_EQ'])
    elif 1000 <= raw_code < 10000:
        code = ''.join(['0', str(raw_code), '_HK_EQ'])
    elif 10000 <= raw_code < 100000:
        code = ''.join([str(raw_code), '_HK_EQ'])
    else:
        print 'Invalid HK stock code captured!'
        exit()
    return code


def get_org_id_from_secu_code(hk_stk_code, collection):
    org_id = -1  #assume it's invalid as a flag; later might be used
    for i in collection.find( { "code": hk_stk_code } ).limit(1):
        org_id = i['org']['id']
    return org_id


# start_raw_stock_code is 0 by default; after a disconnection, change this number to the last number you see in the console/log
USAGE = 'Please specify either nothing or the last integer you saw as a stock code.'
parser = OptionParser(USAGE)
opt, args = parser.parse_args()
if len(args) < 1:
    start_raw_stock_code = 0
elif len(args) == 1:
    try:
        start_raw_stock_code = int(args[0])
    except ValueError:
        print USAGE
        exit()
else:
    print USAGE
    exit()

for raw_stock_code in sorted(config_hk_stock.stock_codes):
    #skip the duplicates after a disconnection
    if raw_stock_code < start_raw_stock_code:
        continue
        
    #whether to sleep to be less aggressive while crawling data
    if OPTION_SLEEP:
        print 'Sleeping for ', SECS_TO_SLEEP, ' seconds now'
        time.sleep(SECS_TO_SLEEP)
        if raw_stock_code %50 == 0:
            print 'Sleeping for 60 * ', SECS_TO_SLEEP, ' seconds now'
            time.sleep(60*SECS_TO_SLEEP)
    
    #get the pre-downloaded local html file data; for testing only
    #html_file = 'd:/crawling_data/hk/o1.html'
    #with open (html_file, "r") as myfile:
        #data = myfile.read().replace('\r\n', '')

    #get the real online html file data
    url = ''.join(['http://www.hkex.com.hk/eng/invest/company/profile_page_e.asp?WidCoID=', str(raw_stock_code), '&WidCoAbbName=&Month=&langcode=e'])
    ############# modify by xutao.ding ################

    data = ''
    for _i in range(4):
        try:
            resp = requests.get(url, timeout=30)
            data = resp.content.replace('\r\n', '')
            if data: break
        except:
            data = ''

    if data is None:
        leak_codes.append(raw_stock_code)

    ############### modify by xutao.ding ###############

    ##resp = urllib2.urlopen(url)  # by sasha
    ##data = resp.read().replace('\r\n', '')  # by sasha

    #get online latest issued shares
    try:
        issued_shares_pattern = r'Issued Shares.*?</tr>'
        con1 = re.compile(issued_shares_pattern, re.MULTILINE)
        issued_shares_data = re.sub('<.*?>', '', con1.search(data).group()).replace('&nbsp;', '').replace('\r', '').replace('\n', '').replace('\t', '').strip()
        raw_issued_shares = str(issued_shares_data.split('  ')[-1])
    except:
        print 'Exceptions in issued shares! (Most likely it doesnt exist in this case.) Now is: ', raw_stock_code, '(secu id). Skip for the next...'
        print
        continue
    issued_shares = re.sub('\(.*\)|,', '', raw_issued_shares)
    
    #get the 'total' value (issued shares) stored in mongodb
    stock_code = handle_stock_code(int(raw_stock_code))
    org_id = get_org_id_from_secu_code(stock_code, c1)
    
    #the stock doesn't exist in base_stock collection
    if org_id < 0:
        print 'org_id doesnt exist in base_stock.'
        continue
        
    for i in c2.find( { "org.id": str(org_id) } ).sort([("vdt", -1)]).limit(1):
        print i['total'], ' | ', issued_shares, ' | ', raw_issued_shares, ' | ', issued_shares_data
        print dt.datetime.now()
        with open("/home/sasha/code/crawling_data/log", "a") as log_file:
            log_file.write(''.join([i['total'], ' | ', issued_shares, ' | ', raw_issued_shares, ' | ', issued_shares_data, "\n"]))
            log_file.write(''.join([str(dt.datetime.now()), "\n"]))
            log_file.write(''.join([str(stock_code), "\n\n"]))
        #check if the issued shares value is the latest in mongodb
        if int(i['total']) == int(issued_shares):
            print stock_code, 'Already the latest!'
            print
            break
        else:
            print stock_code, 'Updating the latest...'
            print
            j = i
            j.pop('_id', None)  #_id is popped
            j.pop('stat', None)
            #keys that may need to modify: vdt, share.amt, total, upt, crt, src
            vdt = dt.datetime.strptime(str(re.sub('[A-Za-z]|\)| ', '', re.search('as at .*\)', raw_issued_shares).group(0))), '%d/%m/%Y')
            upt = dt.datetime.now()
            crt = upt
            src = ''.join(['http://www.hkex.com.hk/eng/invest/company/profile_page_e.asp?WidCoID=', str(raw_stock_code), '&WidCoAbbName=&Month=&langcode=e'])
            j['vdt'], j['share'][0]['amt'], j['total'], j['upt'], j['crt'], j['src'] = vdt, str(issued_shares), str(issued_shares), upt, crt, src
            j['stat'] = 2
            c2.insert(j)
print 'All done'

with open('leak_out.txt', 'w') as fd:
    fd.write(str(leak_codes))