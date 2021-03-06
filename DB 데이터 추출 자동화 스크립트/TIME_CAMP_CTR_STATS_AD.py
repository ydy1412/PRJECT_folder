import pymysql as pms
import pandas as pd
import os
import sys
import time
import pickle as pkl
import datetime

if __name__ == "__main__":
    os_dir = input('base dir [1 : change] : ')
    if os_dir == '1':
        base_dir = input('os_dir : ')
    else:
        base_dir = 'C:/Users/enliple/Desktop/EDA/분석용 데이터셋'
    project_name = base_dir +'/' + input('Project name : ')
    try :
        os.mkdir(project_name)
    except:
        print("folder {0} already exist".format(project_name))
    db_password = input("DB password :")

    B_db = pms.connect(host='192.168.100.108', port=3306, user='dyyang', password=db_password, db='BILLING',
                       charset='utf8')

    sql = """
    SELECT 
        WEEK, STATS_HH, PLTFOM_TP_CODE, SITE_CODE, ADVER_CATE_CODE, TOT_EPRS_CNT, CLICK_CNT
        FROM BILLING.TIME_CAMP_HH_CTR_STATS
        where advrts_tp_code = '01'
        and advrts_prdt_code = '01'
        and itl_tp_code= '01'
        and WEEK = {0};
    """
    dt_index = pd.date_range(start='20200510', end='20200520')
    dt_list = dt_index.strftime("%Y%m%d").tolist()
    advrts_prdt_code_list = ['0{0}'.format(i) for i in range(1, 8)]
    advrts_tp_code_list = [i for i in range(35)]
    advrts_tp_code_list.append(99)
    itl_tp_code_list = [i for i in range(1, 10)]
    itl_tp_code_list.append(99)
    day_of_week_list = [i for i in range(1, 8)]
    print(dt_list[0][4:6])
    data_list = []
    for week in range(1,8):
        try:
            result = pd.read_sql(sql.format(week), B_db)
            data_list.append(result)
            print(week, " successe!")
        except:
            print(week, " : query failed")
    file_name = project_name + '/TIME_CAMP_CTR_STATS.csv'
    pd.concat(data_list).to_csv(file_name, mode='w')