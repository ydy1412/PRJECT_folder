select MCHS.STATS_DTTM, 
	MCHS.STATS_HH, 
	MCHS.PLTFOM_TP_CODE, 
	MCHS.ADVRTS_PRDT_CODE, 
	MCHS.ADVRTS_TP_CODE, 
	MCHS.SITE_CODE, 
	MCHS.TOT_EPRS_CNT, 
	MCHS.CLICK_CNT, 
case when TCES.stop_time is null then 60 else TCES.stop_time end as "stop_time"
from
(SELECT STATS_DTTM, STATS_HH, PLTFOM_TP_CODE, ADVRTS_PRDT_CODE,ADVRTS_TP_CODE, SITE_CODE, TOT_EPRS_CNT, CLICK_CNT 
FROM BILLING.MOB_CAMP_HH_STATS where STATS_DTTM = '20200107' and ITL_TP_CODE = '01') as MCHS
left outer join
(SELECT STATS_DTTM,PLTFOM_TP_CODE,ADVRTS_PRDT_CODE,SITE_CODE,HH_NO as STATS_HH, MINUTE(REG_DTTM) as stop_time FROM BILLING.TIME_CAMP_EXHS_STATS
where ITL_TP_CODE ='01' and STATS_DTTM = '20200107') as TCES
on (MCHS.STATS_DTTM = TCES.STATS_DTTM)  and (MCHS.STATS_HH = TCES.STATS_HH) and (MCHS.ADVRTS_PRDT_CODE =TCES.ADVRTS_PRDT_CODE)  and  (MCHS.PLTFOM_TP_CODE = TCES.PLTFOM_TP_CODE)
and MCHS.SITE_CODE = TCES.SITE_CODE;