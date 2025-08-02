_AH='unusedHold'
_AG='unusedCoreCardMisMatch'
_AF='redPrimarySlotNum'
_AE='a30minutes'
_AD='a15minutes'
_AC='a0minutes'
_AB='shelfSlotNum'
_AA='rpm-pr'
_A9='pxm1-oc12'
_A8='pxm1-4oc3'
_A7='pxm1-2t3e3'
_A6='vism-8E1'
_A5='vism-8T1'
_A4='cesm-E3'
_A3='cesm-T3'
_A2='frsm-hs2b-12In1'
_A1='frsm-hs2b-hssi'
_A0='frsm-2e3b'
_z='frsm-2t3b'
_y='frsm-hs2'
_x='frsm-2e3'
_w='frsm-2t3'
_v='frsm-2ct3'
_u='frt-8E1'
_t='frt-8T1'
_s='atmt-8E1'
_r='atmt-8T1'
_q='bscsm-4'
_p='bscsm-2'
_o='cesm-8E1'
_n='cesm-8T1'
_m='frasm-8T1'
_l='imatmB-E1'
_k='imatmB-T1'
_j='imatm-E3E1'
_i='imatm-T3T1'
_h='cesm-4E1'
_g='cesm-4T1'
_f='ausmB-8E1'
_e='ausmB-8T1'
_d='ausm-8E1'
_c='ausm-8T1'
_b='ausm-4E1'
_a='ausm-4T1'
_Z='frsm-hs1b'
_Y='frsm-8E1'
_X='frsm-8T1'
_W='frsm-hs1'
_V='frsm-4E1'
_U='frsm-4T1'
_T='other'
_S='cardinit'
_R='notResponding'
_Q='reserved'
_P='blocked'
_O='unknown'
_N='mismatch'
_M='boot'
_L='heldInReset'
_K='selfTest'
_J='failed'
_I='active'
_H='standby'
_G='nocard'
_F='BASIS-SHELF-MIB'
_E='DisplayString'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
axisRedundancy,basisShelf=mibBuilder.importSymbols('BASIS-MIB','axisRedundancy','basisShelf')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
_ShelfTable_Object=MibTable
shelfTable=_ShelfTable_Object((1,3,6,1,4,1,351,110,1,1,1))
if mibBuilder.loadTexts:shelfTable.setStatus(_A)
_ShelfEntry_Object=MibTableRow
shelfEntry=_ShelfEntry_Object((1,3,6,1,4,1,351,110,1,1,1,1))
shelfEntry.setIndexNames((0,_F,'shelfNum'),(0,_F,_AB))
if mibBuilder.loadTexts:shelfEntry.setStatus(_A)
class _ShelfNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_ShelfNum_Type.__name__=_B
_ShelfNum_Object=MibTableColumn
shelfNum=_ShelfNum_Object((1,3,6,1,4,1,351,110,1,1,1,1,1),_ShelfNum_Type())
shelfNum.setMaxAccess(_C)
if mibBuilder.loadTexts:shelfNum.setStatus(_A)
class _ShelfSlotNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,33))
_ShelfSlotNum_Type.__name__=_B
_ShelfSlotNum_Object=MibTableColumn
shelfSlotNum=_ShelfSlotNum_Object((1,3,6,1,4,1,351,110,1,1,1,1,2),_ShelfSlotNum_Type())
shelfSlotNum.setMaxAccess(_C)
if mibBuilder.loadTexts:shelfSlotNum.setStatus(_A)
class _ShelfBkplnSerialNumDeprecated_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_ShelfBkplnSerialNumDeprecated_Type.__name__=_B
_ShelfBkplnSerialNumDeprecated_Object=MibTableColumn
shelfBkplnSerialNumDeprecated=_ShelfBkplnSerialNumDeprecated_Object((1,3,6,1,4,1,351,110,1,1,1,1,3),_ShelfBkplnSerialNumDeprecated_Type())
shelfBkplnSerialNumDeprecated.setMaxAccess(_C)
if mibBuilder.loadTexts:shelfBkplnSerialNumDeprecated.setStatus(_A)
class _ShelfFunctionModuleState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,17)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3),(_J,4),(_K,5),(_L,6),(_M,7),(_N,8),(_O,9),('coreCardMismatch',10),(_P,11),(_Q,12),('hold',13),(_R,14),(_S,17)))
_ShelfFunctionModuleState_Type.__name__=_B
_ShelfFunctionModuleState_Object=MibTableColumn
shelfFunctionModuleState=_ShelfFunctionModuleState_Object((1,3,6,1,4,1,351,110,1,1,1,1,4),_ShelfFunctionModuleState_Type())
shelfFunctionModuleState.setMaxAccess(_C)
if mibBuilder.loadTexts:shelfFunctionModuleState.setStatus(_A)
class _ShelfFunctionModuleType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,10,11,12,20,21,22,23,24,25,30,31,32,33,34,35,36,37,40,41,50,51,52,53,60,61,70,71,72,73,80,90,91,100,101,110,111,120,121,130,131,132,133,134,135,136,137,140,141,150,151,1000,1001,1002,1003,2000,2001)));namedValues=NamedValues(*((_T,1),('asc',2),('bnm-T3',10),('bnm-E3',11),('bnm-155',12),('srm-4T1E1',20),('srm-3T3',21),('srme-1OC3',22),('srme-1STS3',23),('srme-NOBC',24),('srm-3T3-NOBC',25),(_U,30),(_V,31),('frsm-4T1-C',32),('frsm-4E1-C',33),(_W,34),(_X,35),(_Y,36),(_Z,37),(_a,40),(_b,41),(_c,50),(_d,51),(_e,52),(_f,53),(_g,60),(_h,61),(_i,70),(_j,71),(_k,72),(_l,73),(_m,80),(_n,90),(_o,91),(_p,100),(_q,101),(_r,110),(_s,111),(_t,120),(_u,121),(_v,130),(_w,131),(_x,132),(_y,133),(_z,134),(_A0,135),(_A1,136),(_A2,137),(_A3,140),(_A4,141),(_A5,150),(_A6,151),('pxm1',1000),(_A7,1001),(_A8,1002),(_A9,1003),('rpm',2000),(_AA,2001)))
_ShelfFunctionModuleType_Type.__name__=_B
_ShelfFunctionModuleType_Object=MibTableColumn
shelfFunctionModuleType=_ShelfFunctionModuleType_Object((1,3,6,1,4,1,351,110,1,1,1,1,5),_ShelfFunctionModuleType_Type())
shelfFunctionModuleType.setMaxAccess(_C)
if mibBuilder.loadTexts:shelfFunctionModuleType.setStatus(_A)
class _ShelfFunctionModuleHoldReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('doNotHold',1),('holdInReset',2)))
_ShelfFunctionModuleHoldReset_Type.__name__=_B
_ShelfFunctionModuleHoldReset_Object=MibTableColumn
shelfFunctionModuleHoldReset=_ShelfFunctionModuleHoldReset_Object((1,3,6,1,4,1,351,110,1,1,1,1,6),_ShelfFunctionModuleHoldReset_Type())
shelfFunctionModuleHoldReset.setMaxAccess(_D)
if mibBuilder.loadTexts:shelfFunctionModuleHoldReset.setStatus(_A)
class _ShelfNumOfValidEntries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_ShelfNumOfValidEntries_Type.__name__=_B
_ShelfNumOfValidEntries_Object=MibScalar
shelfNumOfValidEntries=_ShelfNumOfValidEntries_Object((1,3,6,1,4,1,351,110,1,1,2),_ShelfNumOfValidEntries_Type())
shelfNumOfValidEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:shelfNumOfValidEntries.setStatus(_A)
class _ShelfNodeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10))
_ShelfNodeName_Type.__name__=_E
_ShelfNodeName_Object=MibScalar
shelfNodeName=_ShelfNodeName_Object((1,3,6,1,4,1,351,110,1,1,3),_ShelfNodeName_Type())
shelfNodeName.setMaxAccess(_D)
if mibBuilder.loadTexts:shelfNodeName.setStatus(_A)
class _ShelfDate_Type(DisplayString):defaultValue=OctetString('01/01/1994');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_ShelfDate_Type.__name__=_E
_ShelfDate_Object=MibScalar
shelfDate=_ShelfDate_Object((1,3,6,1,4,1,351,110,1,1,4),_ShelfDate_Type())
shelfDate.setMaxAccess(_D)
if mibBuilder.loadTexts:shelfDate.setStatus(_A)
class _ShelfTime_Type(DisplayString):defaultValue=OctetString('12:00:00');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ShelfTime_Type.__name__=_E
_ShelfTime_Object=MibScalar
shelfTime=_ShelfTime_Object((1,3,6,1,4,1,351,110,1,1,5),_ShelfTime_Type())
shelfTime.setMaxAccess(_D)
if mibBuilder.loadTexts:shelfTime.setStatus(_A)
class _ShelfTmZn_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('gmt',1),('est',2),('cst',3),('mst',4),('pst',5),('edt',6),('cdt',7),('mdt',8),('pdt',9)))
_ShelfTmZn_Type.__name__=_B
_ShelfTmZn_Object=MibScalar
shelfTmZn=_ShelfTmZn_Object((1,3,6,1,4,1,351,110,1,1,6),_ShelfTmZn_Type())
shelfTmZn.setMaxAccess(_D)
if mibBuilder.loadTexts:shelfTmZn.setStatus(_A)
class _ShelfTmZnGMTOff_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-12,12))
_ShelfTmZnGMTOff_Type.__name__=_B
_ShelfTmZnGMTOff_Object=MibScalar
shelfTmZnGMTOff=_ShelfTmZnGMTOff_Object((1,3,6,1,4,1,351,110,1,1,7),_ShelfTmZnGMTOff_Type())
shelfTmZnGMTOff.setMaxAccess(_D)
if mibBuilder.loadTexts:shelfTmZnGMTOff.setStatus(_A)
class _ShelfBkPlnType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_ShelfBkPlnType_Type.__name__=_B
_ShelfBkPlnType_Object=MibScalar
shelfBkPlnType=_ShelfBkPlnType_Object((1,3,6,1,4,1,351,110,1,1,8),_ShelfBkPlnType_Type())
shelfBkPlnType.setMaxAccess(_C)
if mibBuilder.loadTexts:shelfBkPlnType.setStatus(_A)
class _ShelfBkplnSerialNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,11))
_ShelfBkplnSerialNum_Type.__name__=_E
_ShelfBkplnSerialNum_Object=MibScalar
shelfBkplnSerialNum=_ShelfBkplnSerialNum_Object((1,3,6,1,4,1,351,110,1,1,9),_ShelfBkplnSerialNum_Type())
shelfBkplnSerialNum.setMaxAccess(_C)
if mibBuilder.loadTexts:shelfBkplnSerialNum.setStatus(_A)
_StatsMasterIpAddress_Type=IpAddress
_StatsMasterIpAddress_Object=MibScalar
statsMasterIpAddress=_StatsMasterIpAddress_Object((1,3,6,1,4,1,351,110,1,1,10),_StatsMasterIpAddress_Type())
statsMasterIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:statsMasterIpAddress.setStatus(_A)
class _StatsCollectionInterval_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_StatsCollectionInterval_Type.__name__=_B
_StatsCollectionInterval_Object=MibScalar
statsCollectionInterval=_StatsCollectionInterval_Object((1,3,6,1,4,1,351,110,1,1,11),_StatsCollectionInterval_Type())
statsCollectionInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:statsCollectionInterval.setStatus(_A)
class _StatsBucketInterval_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_StatsBucketInterval_Type.__name__=_B
_StatsBucketInterval_Object=MibScalar
statsBucketInterval=_StatsBucketInterval_Object((1,3,6,1,4,1,351,110,1,1,12),_StatsBucketInterval_Type())
statsBucketInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:statsBucketInterval.setStatus(_A)
class _UserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_UserName_Type.__name__=_E
_UserName_Object=MibScalar
userName=_UserName_Object((1,3,6,1,4,1,351,110,1,1,13),_UserName_Type())
userName.setMaxAccess(_C)
if mibBuilder.loadTexts:userName.setStatus(_A)
class _ShelfIntegratedAlarm_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('clear',1),('minor',2),('major',3),('critical',4)))
_ShelfIntegratedAlarm_Type.__name__=_B
_ShelfIntegratedAlarm_Object=MibScalar
shelfIntegratedAlarm=_ShelfIntegratedAlarm_Object((1,3,6,1,4,1,351,110,1,1,14),_ShelfIntegratedAlarm_Type())
shelfIntegratedAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:shelfIntegratedAlarm.setStatus(_A)
class _ShelfAlarmCardBitMap_Type(Integer32):defaultValue=0
_ShelfAlarmCardBitMap_Type.__name__=_B
_ShelfAlarmCardBitMap_Object=MibScalar
shelfAlarmCardBitMap=_ShelfAlarmCardBitMap_Object((1,3,6,1,4,1,351,110,1,1,15),_ShelfAlarmCardBitMap_Type())
shelfAlarmCardBitMap.setMaxAccess(_C)
if mibBuilder.loadTexts:shelfAlarmCardBitMap.setStatus(_A)
class _AxisFeederTkNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AxisFeederTkNo_Type.__name__=_B
_AxisFeederTkNo_Object=MibScalar
axisFeederTkNo=_AxisFeederTkNo_Object((1,3,6,1,4,1,351,110,1,1,16),_AxisFeederTkNo_Type())
axisFeederTkNo.setMaxAccess(_D)
if mibBuilder.loadTexts:axisFeederTkNo.setStatus(_A)
class _AxisSvcBillingColInterval_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_AC,1),(_AD,2),(_AE,3)))
_AxisSvcBillingColInterval_Type.__name__=_B
_AxisSvcBillingColInterval_Object=MibScalar
axisSvcBillingColInterval=_AxisSvcBillingColInterval_Object((1,3,6,1,4,1,351,110,1,1,17),_AxisSvcBillingColInterval_Type())
axisSvcBillingColInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:axisSvcBillingColInterval.setStatus(_A)
class _AxisSvcBillingBucketInterval_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_AC,1),('a5minutes',2),(_AD,3),(_AE,4)))
_AxisSvcBillingBucketInterval_Type.__name__=_B
_AxisSvcBillingBucketInterval_Object=MibScalar
axisSvcBillingBucketInterval=_AxisSvcBillingBucketInterval_Object((1,3,6,1,4,1,351,110,1,1,18),_AxisSvcBillingBucketInterval_Type())
axisSvcBillingBucketInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:axisSvcBillingBucketInterval.setStatus(_A)
_ApsIpAddress_Type=IpAddress
_ApsIpAddress_Object=MibScalar
apsIpAddress=_ApsIpAddress_Object((1,3,6,1,4,1,351,110,1,1,19),_ApsIpAddress_Type())
apsIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:apsIpAddress.setStatus(_A)
_RedundantApsIpAddress_Type=IpAddress
_RedundantApsIpAddress_Object=MibScalar
redundantApsIpAddress=_RedundantApsIpAddress_Object((1,3,6,1,4,1,351,110,1,1,20),_RedundantApsIpAddress_Type())
redundantApsIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:redundantApsIpAddress.setStatus(_A)
class _AxisSvcBilling_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_AxisSvcBilling_Type.__name__=_B
_AxisSvcBilling_Object=MibScalar
axisSvcBilling=_AxisSvcBilling_Object((1,3,6,1,4,1,351,110,1,1,21),_AxisSvcBilling_Type())
axisSvcBilling.setMaxAccess(_D)
if mibBuilder.loadTexts:axisSvcBilling.setStatus(_A)
_ShelfCBClkRateTable_Object=MibTable
shelfCBClkRateTable=_ShelfCBClkRateTable_Object((1,3,6,1,4,1,351,110,1,1,22))
if mibBuilder.loadTexts:shelfCBClkRateTable.setStatus(_A)
_ShelfCBClkRateEntry_Object=MibTableRow
shelfCBClkRateEntry=_ShelfCBClkRateEntry_Object((1,3,6,1,4,1,351,110,1,1,22,1))
shelfCBClkRateEntry.setIndexNames((0,_F,'cBNum'))
if mibBuilder.loadTexts:shelfCBClkRateEntry.setStatus(_A)
class _CBNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_CBNum_Type.__name__=_B
_CBNum_Object=MibTableColumn
cBNum=_CBNum_Object((1,3,6,1,4,1,351,110,1,1,22,1,1),_CBNum_Type())
cBNum.setMaxAccess(_C)
if mibBuilder.loadTexts:cBNum.setStatus(_A)
class _ClkRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('twentyOne-Mhz',1),('fortyTwo-Mhz',2)))
_ClkRate_Type.__name__=_B
_ClkRate_Object=MibTableColumn
clkRate=_ClkRate_Object((1,3,6,1,4,1,351,110,1,1,22,1,2),_ClkRate_Type())
clkRate.setMaxAccess(_D)
if mibBuilder.loadTexts:clkRate.setStatus(_A)
class _ShelfPowerSupplyVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('two-twenty',1),('one-ten',2)))
_ShelfPowerSupplyVoltage_Type.__name__=_B
_ShelfPowerSupplyVoltage_Object=MibScalar
shelfPowerSupplyVoltage=_ShelfPowerSupplyVoltage_Object((1,3,6,1,4,1,351,110,1,1,23),_ShelfPowerSupplyVoltage_Type())
shelfPowerSupplyVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:shelfPowerSupplyVoltage.setStatus(_A)
_SmRedMapTable_Object=MibTable
smRedMapTable=_SmRedMapTable_Object((1,3,6,1,4,1,351,110,1,3,1))
if mibBuilder.loadTexts:smRedMapTable.setStatus(_A)
_SmRedMapEntry_Object=MibTableRow
smRedMapEntry=_SmRedMapEntry_Object((1,3,6,1,4,1,351,110,1,3,1,1))
smRedMapEntry.setIndexNames((0,_F,_AF))
if mibBuilder.loadTexts:smRedMapEntry.setStatus(_A)
class _RedPrimarySlotNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_RedPrimarySlotNum_Type.__name__=_B
_RedPrimarySlotNum_Object=MibTableColumn
redPrimarySlotNum=_RedPrimarySlotNum_Object((1,3,6,1,4,1,351,110,1,3,1,1,1),_RedPrimarySlotNum_Type())
redPrimarySlotNum.setMaxAccess(_D)
if mibBuilder.loadTexts:redPrimarySlotNum.setStatus(_A)
class _RedRowStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('add',1),('del',2),('mod',3)))
_RedRowStatus_Type.__name__=_B
_RedRowStatus_Object=MibTableColumn
redRowStatus=_RedRowStatus_Object((1,3,6,1,4,1,351,110,1,3,1,1,2),_RedRowStatus_Type())
redRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:redRowStatus.setStatus(_A)
class _RedPrimaryType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,10,20,30,31,34,35,36,37,40,41,50,51,52,53,60,61,70,71,72,73,80,90,91,100,101,110,111,120,121,130,131,132,133,134,135,136,137,140,141,150,151,1000,1001,1002,1003,2000,2001)));namedValues=NamedValues(*((_T,1),('bsc',2),('aum-T3',10),('tim',20),(_U,30),(_V,31),(_W,34),(_X,35),(_Y,36),(_Z,37),(_a,40),(_b,41),(_c,50),(_d,51),(_e,52),(_f,53),(_g,60),(_h,61),(_i,70),(_j,71),(_k,72),(_l,73),(_m,80),(_n,90),(_o,91),(_p,100),(_q,101),(_r,110),(_s,111),(_t,120),(_u,121),(_v,130),(_w,131),(_x,132),(_y,133),(_z,134),(_A0,135),(_A1,136),(_A2,137),(_A3,140),(_A4,141),(_A5,150),(_A6,151),('pxm1',1000),(_A7,1001),(_A8,1002),(_A9,1003),('rpm',2000),(_AA,2001)))
_RedPrimaryType_Type.__name__=_B
_RedPrimaryType_Object=MibTableColumn
redPrimaryType=_RedPrimaryType_Object((1,3,6,1,4,1,351,110,1,3,1,1,3),_RedPrimaryType_Type())
redPrimaryType.setMaxAccess(_C)
if mibBuilder.loadTexts:redPrimaryType.setStatus(_A)
class _RedPrimaryState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,17)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3),(_J,4),(_K,5),(_L,6),(_M,7),(_N,8),(_O,9),(_AG,10),(_P,11),(_Q,12),(_AH,13),(_R,14),(_S,17)))
_RedPrimaryState_Type.__name__=_B
_RedPrimaryState_Object=MibTableColumn
redPrimaryState=_RedPrimaryState_Object((1,3,6,1,4,1,351,110,1,3,1,1,4),_RedPrimaryState_Type())
redPrimaryState.setMaxAccess(_C)
if mibBuilder.loadTexts:redPrimaryState.setStatus(_A)
class _RedSecondarySlotNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_RedSecondarySlotNum_Type.__name__=_B
_RedSecondarySlotNum_Object=MibTableColumn
redSecondarySlotNum=_RedSecondarySlotNum_Object((1,3,6,1,4,1,351,110,1,3,1,1,5),_RedSecondarySlotNum_Type())
redSecondarySlotNum.setMaxAccess(_D)
if mibBuilder.loadTexts:redSecondarySlotNum.setStatus(_A)
class _RedSecondaryType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,10,20,30,31,34,35,36,37,40,41,50,51,52,53,60,61,70,71,72,73,80,90,91,100,101,110,111,120,121,130,131,132,133,134,135,136,137,140,141,150,151,1000,1001,1002,1003,2000,2001)));namedValues=NamedValues(*((_T,1),('bsc',2),('aum-T3',10),('tim',20),(_U,30),(_V,31),(_W,34),(_X,35),(_Y,36),(_Z,37),(_a,40),(_b,41),(_c,50),(_d,51),(_e,52),(_f,53),(_g,60),(_h,61),(_i,70),(_j,71),(_k,72),(_l,73),(_m,80),(_n,90),(_o,91),(_p,100),(_q,101),(_r,110),(_s,111),(_t,120),(_u,121),(_v,130),(_w,131),(_x,132),(_y,133),(_z,134),(_A0,135),(_A1,136),(_A2,137),(_A3,140),(_A4,141),(_A5,150),(_A6,151),('pxm1',1000),(_A7,1001),(_A8,1002),(_A9,1003),('rpm',2000),(_AA,2001)))
_RedSecondaryType_Type.__name__=_B
_RedSecondaryType_Object=MibTableColumn
redSecondaryType=_RedSecondaryType_Object((1,3,6,1,4,1,351,110,1,3,1,1,6),_RedSecondaryType_Type())
redSecondaryType.setMaxAccess(_C)
if mibBuilder.loadTexts:redSecondaryType.setStatus(_A)
class _RedSecondaryState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,17)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3),(_J,4),(_K,5),(_L,6),(_M,7),(_N,8),(_O,9),(_AG,10),(_P,11),(_Q,12),(_AH,13),(_R,14),(_S,17)))
_RedSecondaryState_Type.__name__=_B
_RedSecondaryState_Object=MibTableColumn
redSecondaryState=_RedSecondaryState_Object((1,3,6,1,4,1,351,110,1,3,1,1,7),_RedSecondaryState_Type())
redSecondaryState.setMaxAccess(_C)
if mibBuilder.loadTexts:redSecondaryState.setStatus(_A)
class _RedType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yCable',1),('oneToN',2)))
_RedType_Type.__name__=_B
_RedType_Object=MibTableColumn
redType=_RedType_Object((1,3,6,1,4,1,351,110,1,3,1,1,8),_RedType_Type())
redType.setMaxAccess(_D)
if mibBuilder.loadTexts:redType.setStatus(_A)
class _RedCoveringSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_RedCoveringSlot_Type.__name__=_B
_RedCoveringSlot_Object=MibTableColumn
redCoveringSlot=_RedCoveringSlot_Object((1,3,6,1,4,1,351,110,1,3,1,1,9),_RedCoveringSlot_Type())
redCoveringSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:redCoveringSlot.setStatus(_A)
_RedFeature_Type=Integer32
_RedFeature_Object=MibTableColumn
redFeature=_RedFeature_Object((1,3,6,1,4,1,351,110,1,3,1,1,10),_RedFeature_Type())
redFeature.setMaxAccess(_C)
if mibBuilder.loadTexts:redFeature.setStatus(_A)
class _RedLineModuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32,33,48,49,50,60,61,62,63)));namedValues=NamedValues(*(('lm-DB15-4T1',16),('lm-DB15-4E1',17),('lm-BNC-4E1',18),('lm-DB15-4T1-R',19),('lm-DB15-4E1-R',20),('lm-BNC-4E1-R',21),('lm-RJ48-8T1',22),('lm-RJ48-8E1',23),('lm-SMB-8E1',24),('lm-RJ48-T3T1',25),('lm-RJ48-E3E1',26),('lm-RJ48-T3E1',27),('lm-SMB-E3E1',28),('lm-RJ48-E3T1',29),('lm-SMB-T3E1',30),('lm-T3E3-D',32),('lm-T3E3-B',33),('lm-RJ48-8T1-R',48),('lm-RJ48-8E1-R',49),('lm-SMB-8E1-R',50),('lm-HS1-4X21',60),('lm-HS1-3HSSI',61),('lm-HS1-4V35',62),('lm-12In1-8s',63)))
_RedLineModuleType_Type.__name__=_B
_RedLineModuleType_Object=MibTableColumn
redLineModuleType=_RedLineModuleType_Object((1,3,6,1,4,1,351,110,1,3,1,1,11),_RedLineModuleType_Type())
redLineModuleType.setMaxAccess(_C)
if mibBuilder.loadTexts:redLineModuleType.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'shelfTable':shelfTable,'shelfEntry':shelfEntry,'shelfNum':shelfNum,_AB:shelfSlotNum,'shelfBkplnSerialNumDeprecated':shelfBkplnSerialNumDeprecated,'shelfFunctionModuleState':shelfFunctionModuleState,'shelfFunctionModuleType':shelfFunctionModuleType,'shelfFunctionModuleHoldReset':shelfFunctionModuleHoldReset,'shelfNumOfValidEntries':shelfNumOfValidEntries,'shelfNodeName':shelfNodeName,'shelfDate':shelfDate,'shelfTime':shelfTime,'shelfTmZn':shelfTmZn,'shelfTmZnGMTOff':shelfTmZnGMTOff,'shelfBkPlnType':shelfBkPlnType,'shelfBkplnSerialNum':shelfBkplnSerialNum,'statsMasterIpAddress':statsMasterIpAddress,'statsCollectionInterval':statsCollectionInterval,'statsBucketInterval':statsBucketInterval,'userName':userName,'shelfIntegratedAlarm':shelfIntegratedAlarm,'shelfAlarmCardBitMap':shelfAlarmCardBitMap,'axisFeederTkNo':axisFeederTkNo,'axisSvcBillingColInterval':axisSvcBillingColInterval,'axisSvcBillingBucketInterval':axisSvcBillingBucketInterval,'apsIpAddress':apsIpAddress,'redundantApsIpAddress':redundantApsIpAddress,'axisSvcBilling':axisSvcBilling,'shelfCBClkRateTable':shelfCBClkRateTable,'shelfCBClkRateEntry':shelfCBClkRateEntry,'cBNum':cBNum,'clkRate':clkRate,'shelfPowerSupplyVoltage':shelfPowerSupplyVoltage,'smRedMapTable':smRedMapTable,'smRedMapEntry':smRedMapEntry,_AF:redPrimarySlotNum,'redRowStatus':redRowStatus,'redPrimaryType':redPrimaryType,'redPrimaryState':redPrimaryState,'redSecondarySlotNum':redSecondarySlotNum,'redSecondaryType':redSecondaryType,'redSecondaryState':redSecondaryState,'redType':redType,'redCoveringSlot':redCoveringSlot,'redFeature':redFeature,'redLineModuleType':redLineModuleType})