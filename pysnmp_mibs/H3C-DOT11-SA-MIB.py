_m='h3cDot11APTrapDevDctTime'
_l='h3cDot11APTrapDevChls'
_k='h3cDot11APTrapDevDC'
_j='h3cDot11SaTrapDevRSSI'
_i='h3cDot11APTrapDevSI'
_h='h3cDot11SaChlNum'
_g='h3cDot11SaDevID'
_f='h3cDot11SaFrequency'
_e='h3cDot11SaRtDataGroupID'
_d='genericInterferer'
_c='freqHopperXbox'
_b='freqHopperCordlessNetwork'
_a='freqHopperCordlessBase'
_Z='freqHopperOthers'
_Y='fixedFreqAudio'
_X='fixedFreqVideo'
_W='fixedFreqCordlessPhone'
_V='fixedFreqOthers'
_U='bluetooth'
_T='microwaveInverter'
_S='microwave'
_R='h3cDot11SaCfgRadioType'
_Q='h3cDot11SaTrapChlIntfNum'
_P='h3cDot11SaTrapChlQlt'
_O='h3cDot11SaTrapChlNum'
_N='h3cDot11SaTrapIntfDevType'
_M='h3cDot11SaTrapDevID'
_L='Bits'
_K='h3cDot11SaRadioID'
_J='h3cDot11SaAPID'
_I='Integer32'
_H='h3cDot11SaTrapRadioID'
_G='h3cDot11SaTrapAPID'
_F='not-accessible'
_E='read-write'
_D='accessible-for-notify'
_C='read-only'
_B='H3C-DOT11-SA-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
H3cDot11ChannelScopeType,H3cDot11ObjectIDType,H3cDot11RadioScopeType,H3cDot11SaIntfDevType,h3cDot11=mibBuilder.importSymbols('H3C-DOT11-REF-MIB','H3cDot11ChannelScopeType','H3cDot11ObjectIDType','H3cDot11RadioScopeType','H3cDot11SaIntfDevType','h3cDot11')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_L,'Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention','TruthValue')
h3cDot11Sa=ModuleIdentity((1,3,6,1,4,1,2011,10,2,75,13))
if mibBuilder.loadTexts:h3cDot11Sa.setRevisions(('2011-08-26 20:00',))
_H3cDot11SaCfgGroup_ObjectIdentity=ObjectIdentity
h3cDot11SaCfgGroup=_H3cDot11SaCfgGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,75,13,1))
_H3cDot11SaCfgTable_Object=MibTable
h3cDot11SaCfgTable=_H3cDot11SaCfgTable_Object((1,3,6,1,4,1,2011,10,2,75,13,1,1))
if mibBuilder.loadTexts:h3cDot11SaCfgTable.setStatus(_A)
_H3cDot11SaCfgEntry_Object=MibTableRow
h3cDot11SaCfgEntry=_H3cDot11SaCfgEntry_Object((1,3,6,1,4,1,2011,10,2,75,13,1,1,1))
h3cDot11SaCfgEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:h3cDot11SaCfgEntry.setStatus(_A)
class _H3cDot11SaCfgRadioType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dot11bg',1),('dot11a',2)))
_H3cDot11SaCfgRadioType_Type.__name__=_I
_H3cDot11SaCfgRadioType_Object=MibTableColumn
h3cDot11SaCfgRadioType=_H3cDot11SaCfgRadioType_Object((1,3,6,1,4,1,2011,10,2,75,13,1,1,1,1),_H3cDot11SaCfgRadioType_Type())
h3cDot11SaCfgRadioType.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11SaCfgRadioType.setStatus(_A)
_H3cDot11SaEnable_Type=TruthValue
_H3cDot11SaEnable_Object=MibTableColumn
h3cDot11SaEnable=_H3cDot11SaEnable_Object((1,3,6,1,4,1,2011,10,2,75,13,1,1,1,2),_H3cDot11SaEnable_Type())
h3cDot11SaEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDot11SaEnable.setStatus(_A)
class _H3cDot11SaRptDevType_Type(Bits):namedValues=NamedValues(*((_S,0),(_T,1),(_U,2),(_V,3),(_W,4),(_X,5),(_Y,6),(_Z,7),(_a,8),(_b,9),(_c,10),(_d,11)))
_H3cDot11SaRptDevType_Type.__name__=_L
_H3cDot11SaRptDevType_Object=MibTableColumn
h3cDot11SaRptDevType=_H3cDot11SaRptDevType_Object((1,3,6,1,4,1,2011,10,2,75,13,1,1,1,3),_H3cDot11SaRptDevType_Type())
h3cDot11SaRptDevType.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDot11SaRptDevType.setStatus(_A)
_H3cDot11SaTrapDevEnable_Type=TruthValue
_H3cDot11SaTrapDevEnable_Object=MibTableColumn
h3cDot11SaTrapDevEnable=_H3cDot11SaTrapDevEnable_Object((1,3,6,1,4,1,2011,10,2,75,13,1,1,1,4),_H3cDot11SaTrapDevEnable_Type())
h3cDot11SaTrapDevEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDot11SaTrapDevEnable.setStatus(_A)
class _H3cDot11SaTrapDevType_Type(Bits):namedValues=NamedValues(*((_S,0),(_T,1),(_U,2),(_V,3),(_W,4),(_X,5),(_Y,6),(_Z,7),(_a,8),(_b,9),(_c,10),(_d,11)))
_H3cDot11SaTrapDevType_Type.__name__=_L
_H3cDot11SaTrapDevType_Object=MibTableColumn
h3cDot11SaTrapDevType=_H3cDot11SaTrapDevType_Object((1,3,6,1,4,1,2011,10,2,75,13,1,1,1,5),_H3cDot11SaTrapDevType_Type())
h3cDot11SaTrapDevType.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDot11SaTrapDevType.setStatus(_A)
_H3cDot11SaTrapAQEnable_Type=TruthValue
_H3cDot11SaTrapAQEnable_Object=MibTableColumn
h3cDot11SaTrapAQEnable=_H3cDot11SaTrapAQEnable_Object((1,3,6,1,4,1,2011,10,2,75,13,1,1,1,6),_H3cDot11SaTrapAQEnable_Type())
h3cDot11SaTrapAQEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDot11SaTrapAQEnable.setStatus(_A)
class _H3cDot11SaTrapAQThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_H3cDot11SaTrapAQThreshold_Type.__name__=_I
_H3cDot11SaTrapAQThreshold_Object=MibTableColumn
h3cDot11SaTrapAQThreshold=_H3cDot11SaTrapAQThreshold_Object((1,3,6,1,4,1,2011,10,2,75,13,1,1,1,7),_H3cDot11SaTrapAQThreshold_Type())
h3cDot11SaTrapAQThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDot11SaTrapAQThreshold.setStatus(_A)
_H3cDot11SaDrivenRRMEnable_Type=TruthValue
_H3cDot11SaDrivenRRMEnable_Object=MibTableColumn
h3cDot11SaDrivenRRMEnable=_H3cDot11SaDrivenRRMEnable_Object((1,3,6,1,4,1,2011,10,2,75,13,1,1,1,8),_H3cDot11SaDrivenRRMEnable_Type())
h3cDot11SaDrivenRRMEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDot11SaDrivenRRMEnable.setStatus(_A)
class _H3cDot11SaDrivenRRMSnt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('low',1),('medium',2),('high',3)))
_H3cDot11SaDrivenRRMSnt_Type.__name__=_I
_H3cDot11SaDrivenRRMSnt_Object=MibTableColumn
h3cDot11SaDrivenRRMSnt=_H3cDot11SaDrivenRRMSnt_Object((1,3,6,1,4,1,2011,10,2,75,13,1,1,1,9),_H3cDot11SaDrivenRRMSnt_Type())
h3cDot11SaDrivenRRMSnt.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDot11SaDrivenRRMSnt.setStatus(_A)
_H3cDot11SaStatusGroup_ObjectIdentity=ObjectIdentity
h3cDot11SaStatusGroup=_H3cDot11SaStatusGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,75,13,2))
_H3cDot11SaRtFFTDataTable_Object=MibTable
h3cDot11SaRtFFTDataTable=_H3cDot11SaRtFFTDataTable_Object((1,3,6,1,4,1,2011,10,2,75,13,2,1))
if mibBuilder.loadTexts:h3cDot11SaRtFFTDataTable.setStatus(_A)
_H3cDot11SaRtFFTDataEntry_Object=MibTableRow
h3cDot11SaRtFFTDataEntry=_H3cDot11SaRtFFTDataEntry_Object((1,3,6,1,4,1,2011,10,2,75,13,2,1,1))
h3cDot11SaRtFFTDataEntry.setIndexNames((0,_B,_J),(0,_B,_K),(0,_B,_e),(0,_B,_f))
if mibBuilder.loadTexts:h3cDot11SaRtFFTDataEntry.setStatus(_A)
_H3cDot11SaAPID_Type=H3cDot11ObjectIDType
_H3cDot11SaAPID_Object=MibTableColumn
h3cDot11SaAPID=_H3cDot11SaAPID_Object((1,3,6,1,4,1,2011,10,2,75,13,2,1,1,1),_H3cDot11SaAPID_Type())
h3cDot11SaAPID.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11SaAPID.setStatus(_A)
_H3cDot11SaRadioID_Type=H3cDot11RadioScopeType
_H3cDot11SaRadioID_Object=MibTableColumn
h3cDot11SaRadioID=_H3cDot11SaRadioID_Object((1,3,6,1,4,1,2011,10,2,75,13,2,1,1,2),_H3cDot11SaRadioID_Type())
h3cDot11SaRadioID.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11SaRadioID.setStatus(_A)
_H3cDot11SaRtDataGroupID_Type=Integer32
_H3cDot11SaRtDataGroupID_Object=MibTableColumn
h3cDot11SaRtDataGroupID=_H3cDot11SaRtDataGroupID_Object((1,3,6,1,4,1,2011,10,2,75,13,2,1,1,3),_H3cDot11SaRtDataGroupID_Type())
h3cDot11SaRtDataGroupID.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11SaRtDataGroupID.setStatus(_A)
_H3cDot11SaFrequency_Type=Integer32
_H3cDot11SaFrequency_Object=MibTableColumn
h3cDot11SaFrequency=_H3cDot11SaFrequency_Object((1,3,6,1,4,1,2011,10,2,75,13,2,1,1,4),_H3cDot11SaFrequency_Type())
h3cDot11SaFrequency.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11SaFrequency.setStatus(_A)
_H3cDot11SaRtFreqPower_Type=Integer32
_H3cDot11SaRtFreqPower_Object=MibTableColumn
h3cDot11SaRtFreqPower=_H3cDot11SaRtFreqPower_Object((1,3,6,1,4,1,2011,10,2,75,13,2,1,1,5),_H3cDot11SaRtFreqPower_Type())
h3cDot11SaRtFreqPower.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot11SaRtFreqPower.setStatus(_A)
_H3cDot11SaRtFreqMaxPower_Type=Integer32
_H3cDot11SaRtFreqMaxPower_Object=MibTableColumn
h3cDot11SaRtFreqMaxPower=_H3cDot11SaRtFreqMaxPower_Object((1,3,6,1,4,1,2011,10,2,75,13,2,1,1,6),_H3cDot11SaRtFreqMaxPower_Type())
h3cDot11SaRtFreqMaxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot11SaRtFreqMaxPower.setStatus(_A)
_H3cDot11SaRtFreqDutyCycle_Type=Integer32
_H3cDot11SaRtFreqDutyCycle_Object=MibTableColumn
h3cDot11SaRtFreqDutyCycle=_H3cDot11SaRtFreqDutyCycle_Object((1,3,6,1,4,1,2011,10,2,75,13,2,1,1,7),_H3cDot11SaRtFreqDutyCycle_Type())
h3cDot11SaRtFreqDutyCycle.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot11SaRtFreqDutyCycle.setStatus(_A)
_H3cDot11SaRtFreqDataSeqNo_Type=Unsigned32
_H3cDot11SaRtFreqDataSeqNo_Object=MibTableColumn
h3cDot11SaRtFreqDataSeqNo=_H3cDot11SaRtFreqDataSeqNo_Object((1,3,6,1,4,1,2011,10,2,75,13,2,1,1,8),_H3cDot11SaRtFreqDataSeqNo_Type())
h3cDot11SaRtFreqDataSeqNo.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot11SaRtFreqDataSeqNo.setStatus(_A)
_H3cDot11SaIntfDevTable_Object=MibTable
h3cDot11SaIntfDevTable=_H3cDot11SaIntfDevTable_Object((1,3,6,1,4,1,2011,10,2,75,13,2,2))
if mibBuilder.loadTexts:h3cDot11SaIntfDevTable.setStatus(_A)
_H3cDot11SaIntfDevEntry_Object=MibTableRow
h3cDot11SaIntfDevEntry=_H3cDot11SaIntfDevEntry_Object((1,3,6,1,4,1,2011,10,2,75,13,2,2,1))
h3cDot11SaIntfDevEntry.setIndexNames((0,_B,_J),(0,_B,_K),(0,_B,_g))
if mibBuilder.loadTexts:h3cDot11SaIntfDevEntry.setStatus(_A)
_H3cDot11SaDevID_Type=Integer32
_H3cDot11SaDevID_Object=MibTableColumn
h3cDot11SaDevID=_H3cDot11SaDevID_Object((1,3,6,1,4,1,2011,10,2,75,13,2,2,1,1),_H3cDot11SaDevID_Type())
h3cDot11SaDevID.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11SaDevID.setStatus(_A)
_H3cDot11SaDevType_Type=H3cDot11SaIntfDevType
_H3cDot11SaDevType_Object=MibTableColumn
h3cDot11SaDevType=_H3cDot11SaDevType_Object((1,3,6,1,4,1,2011,10,2,75,13,2,2,1,2),_H3cDot11SaDevType_Type())
h3cDot11SaDevType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot11SaDevType.setStatus(_A)
_H3cDot11SaDevSI_Type=Integer32
_H3cDot11SaDevSI_Object=MibTableColumn
h3cDot11SaDevSI=_H3cDot11SaDevSI_Object((1,3,6,1,4,1,2011,10,2,75,13,2,2,1,3),_H3cDot11SaDevSI_Type())
h3cDot11SaDevSI.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot11SaDevSI.setStatus(_A)
_H3cDot11SaDevRSSI_Type=Integer32
_H3cDot11SaDevRSSI_Object=MibTableColumn
h3cDot11SaDevRSSI=_H3cDot11SaDevRSSI_Object((1,3,6,1,4,1,2011,10,2,75,13,2,2,1,4),_H3cDot11SaDevRSSI_Type())
h3cDot11SaDevRSSI.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot11SaDevRSSI.setStatus(_A)
_H3cDot11SaDevDutyCycle_Type=Integer32
_H3cDot11SaDevDutyCycle_Object=MibTableColumn
h3cDot11SaDevDutyCycle=_H3cDot11SaDevDutyCycle_Object((1,3,6,1,4,1,2011,10,2,75,13,2,2,1,5),_H3cDot11SaDevDutyCycle_Type())
h3cDot11SaDevDutyCycle.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot11SaDevDutyCycle.setStatus(_A)
_H3cDot11SaDevAffectedChls_Type=OctetString
_H3cDot11SaDevAffectedChls_Object=MibTableColumn
h3cDot11SaDevAffectedChls=_H3cDot11SaDevAffectedChls_Object((1,3,6,1,4,1,2011,10,2,75,13,2,2,1,6),_H3cDot11SaDevAffectedChls_Type())
h3cDot11SaDevAffectedChls.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot11SaDevAffectedChls.setStatus(_A)
_H3cDot11SaDevDetectedTime_Type=DateAndTime
_H3cDot11SaDevDetectedTime_Object=MibTableColumn
h3cDot11SaDevDetectedTime=_H3cDot11SaDevDetectedTime_Object((1,3,6,1,4,1,2011,10,2,75,13,2,2,1,7),_H3cDot11SaDevDetectedTime_Type())
h3cDot11SaDevDetectedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot11SaDevDetectedTime.setStatus(_A)
_H3cDot11SaAirQualityTable_Object=MibTable
h3cDot11SaAirQualityTable=_H3cDot11SaAirQualityTable_Object((1,3,6,1,4,1,2011,10,2,75,13,2,3))
if mibBuilder.loadTexts:h3cDot11SaAirQualityTable.setStatus(_A)
_H3cDot11SaAirQualityEntry_Object=MibTableRow
h3cDot11SaAirQualityEntry=_H3cDot11SaAirQualityEntry_Object((1,3,6,1,4,1,2011,10,2,75,13,2,3,1))
h3cDot11SaAirQualityEntry.setIndexNames((0,_B,_J),(0,_B,_K),(0,_B,_h))
if mibBuilder.loadTexts:h3cDot11SaAirQualityEntry.setStatus(_A)
_H3cDot11SaChlNum_Type=H3cDot11ChannelScopeType
_H3cDot11SaChlNum_Object=MibTableColumn
h3cDot11SaChlNum=_H3cDot11SaChlNum_Object((1,3,6,1,4,1,2011,10,2,75,13,2,3,1,1),_H3cDot11SaChlNum_Type())
h3cDot11SaChlNum.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11SaChlNum.setStatus(_A)
_H3cDot11SaAvgQuality_Type=Integer32
_H3cDot11SaAvgQuality_Object=MibTableColumn
h3cDot11SaAvgQuality=_H3cDot11SaAvgQuality_Object((1,3,6,1,4,1,2011,10,2,75,13,2,3,1,2),_H3cDot11SaAvgQuality_Type())
h3cDot11SaAvgQuality.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot11SaAvgQuality.setStatus(_A)
_H3cDot11SaMinQuality_Type=Integer32
_H3cDot11SaMinQuality_Object=MibTableColumn
h3cDot11SaMinQuality=_H3cDot11SaMinQuality_Object((1,3,6,1,4,1,2011,10,2,75,13,2,3,1,3),_H3cDot11SaMinQuality_Type())
h3cDot11SaMinQuality.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot11SaMinQuality.setStatus(_A)
_H3cDot11SaIntfDevNum_Type=Integer32
_H3cDot11SaIntfDevNum_Object=MibTableColumn
h3cDot11SaIntfDevNum=_H3cDot11SaIntfDevNum_Object((1,3,6,1,4,1,2011,10,2,75,13,2,3,1,4),_H3cDot11SaIntfDevNum_Type())
h3cDot11SaIntfDevNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot11SaIntfDevNum.setStatus(_A)
_H3cDot11SaWiFiUtil_Type=Integer32
_H3cDot11SaWiFiUtil_Object=MibTableColumn
h3cDot11SaWiFiUtil=_H3cDot11SaWiFiUtil_Object((1,3,6,1,4,1,2011,10,2,75,13,2,3,1,5),_H3cDot11SaWiFiUtil_Type())
h3cDot11SaWiFiUtil.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot11SaWiFiUtil.setStatus(_A)
_H3cDot11SaNonWiFiUtil_Type=Integer32
_H3cDot11SaNonWiFiUtil_Object=MibTableColumn
h3cDot11SaNonWiFiUtil=_H3cDot11SaNonWiFiUtil_Object((1,3,6,1,4,1,2011,10,2,75,13,2,3,1,6),_H3cDot11SaNonWiFiUtil_Type())
h3cDot11SaNonWiFiUtil.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot11SaNonWiFiUtil.setStatus(_A)
_H3cDot11SaNoiseFloor_Type=Integer32
_H3cDot11SaNoiseFloor_Object=MibTableColumn
h3cDot11SaNoiseFloor=_H3cDot11SaNoiseFloor_Object((1,3,6,1,4,1,2011,10,2,75,13,2,3,1,7),_H3cDot11SaNoiseFloor_Type())
h3cDot11SaNoiseFloor.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot11SaNoiseFloor.setStatus(_A)
_H3cDot11SaNotifyGroup_ObjectIdentity=ObjectIdentity
h3cDot11SaNotifyGroup=_H3cDot11SaNotifyGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,75,13,3))
_H3cDot11SaTraps_ObjectIdentity=ObjectIdentity
h3cDot11SaTraps=_H3cDot11SaTraps_ObjectIdentity((1,3,6,1,4,1,2011,10,2,75,13,3,0))
_H3cDot11SaTrapVars_ObjectIdentity=ObjectIdentity
h3cDot11SaTrapVars=_H3cDot11SaTrapVars_ObjectIdentity((1,3,6,1,4,1,2011,10,2,75,13,3,1))
_H3cDot11SaTrapAPID_Type=H3cDot11ObjectIDType
_H3cDot11SaTrapAPID_Object=MibScalar
h3cDot11SaTrapAPID=_H3cDot11SaTrapAPID_Object((1,3,6,1,4,1,2011,10,2,75,13,3,1,1),_H3cDot11SaTrapAPID_Type())
h3cDot11SaTrapAPID.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SaTrapAPID.setStatus(_A)
_H3cDot11SaTrapRadioID_Type=H3cDot11RadioScopeType
_H3cDot11SaTrapRadioID_Object=MibScalar
h3cDot11SaTrapRadioID=_H3cDot11SaTrapRadioID_Object((1,3,6,1,4,1,2011,10,2,75,13,3,1,2),_H3cDot11SaTrapRadioID_Type())
h3cDot11SaTrapRadioID.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SaTrapRadioID.setStatus(_A)
_H3cDot11SaTrapDevID_Type=Integer32
_H3cDot11SaTrapDevID_Object=MibScalar
h3cDot11SaTrapDevID=_H3cDot11SaTrapDevID_Object((1,3,6,1,4,1,2011,10,2,75,13,3,1,3),_H3cDot11SaTrapDevID_Type())
h3cDot11SaTrapDevID.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SaTrapDevID.setStatus(_A)
_H3cDot11SaTrapIntfDevType_Type=H3cDot11SaIntfDevType
_H3cDot11SaTrapIntfDevType_Object=MibScalar
h3cDot11SaTrapIntfDevType=_H3cDot11SaTrapIntfDevType_Object((1,3,6,1,4,1,2011,10,2,75,13,3,1,4),_H3cDot11SaTrapIntfDevType_Type())
h3cDot11SaTrapIntfDevType.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SaTrapIntfDevType.setStatus(_A)
_H3cDot11APTrapDevSI_Type=Integer32
_H3cDot11APTrapDevSI_Object=MibScalar
h3cDot11APTrapDevSI=_H3cDot11APTrapDevSI_Object((1,3,6,1,4,1,2011,10,2,75,13,3,1,5),_H3cDot11APTrapDevSI_Type())
h3cDot11APTrapDevSI.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11APTrapDevSI.setStatus(_A)
_H3cDot11SaTrapDevRSSI_Type=Integer32
_H3cDot11SaTrapDevRSSI_Object=MibScalar
h3cDot11SaTrapDevRSSI=_H3cDot11SaTrapDevRSSI_Object((1,3,6,1,4,1,2011,10,2,75,13,3,1,6),_H3cDot11SaTrapDevRSSI_Type())
h3cDot11SaTrapDevRSSI.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SaTrapDevRSSI.setStatus(_A)
_H3cDot11APTrapDevDC_Type=Integer32
_H3cDot11APTrapDevDC_Object=MibScalar
h3cDot11APTrapDevDC=_H3cDot11APTrapDevDC_Object((1,3,6,1,4,1,2011,10,2,75,13,3,1,7),_H3cDot11APTrapDevDC_Type())
h3cDot11APTrapDevDC.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11APTrapDevDC.setStatus(_A)
_H3cDot11APTrapDevChls_Type=OctetString
_H3cDot11APTrapDevChls_Object=MibScalar
h3cDot11APTrapDevChls=_H3cDot11APTrapDevChls_Object((1,3,6,1,4,1,2011,10,2,75,13,3,1,8),_H3cDot11APTrapDevChls_Type())
h3cDot11APTrapDevChls.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11APTrapDevChls.setStatus(_A)
_H3cDot11APTrapDevDctTime_Type=DateAndTime
_H3cDot11APTrapDevDctTime_Object=MibScalar
h3cDot11APTrapDevDctTime=_H3cDot11APTrapDevDctTime_Object((1,3,6,1,4,1,2011,10,2,75,13,3,1,9),_H3cDot11APTrapDevDctTime_Type())
h3cDot11APTrapDevDctTime.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11APTrapDevDctTime.setStatus(_A)
_H3cDot11SaTrapChlNum_Type=H3cDot11ChannelScopeType
_H3cDot11SaTrapChlNum_Object=MibScalar
h3cDot11SaTrapChlNum=_H3cDot11SaTrapChlNum_Object((1,3,6,1,4,1,2011,10,2,75,13,3,1,10),_H3cDot11SaTrapChlNum_Type())
h3cDot11SaTrapChlNum.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SaTrapChlNum.setStatus(_A)
_H3cDot11SaTrapChlQlt_Type=Integer32
_H3cDot11SaTrapChlQlt_Object=MibScalar
h3cDot11SaTrapChlQlt=_H3cDot11SaTrapChlQlt_Object((1,3,6,1,4,1,2011,10,2,75,13,3,1,11),_H3cDot11SaTrapChlQlt_Type())
h3cDot11SaTrapChlQlt.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SaTrapChlQlt.setStatus(_A)
_H3cDot11SaTrapChlIntfNum_Type=Integer32
_H3cDot11SaTrapChlIntfNum_Object=MibScalar
h3cDot11SaTrapChlIntfNum=_H3cDot11SaTrapChlIntfNum_Object((1,3,6,1,4,1,2011,10,2,75,13,3,1,12),_H3cDot11SaTrapChlIntfNum_Type())
h3cDot11SaTrapChlIntfNum.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SaTrapChlIntfNum.setStatus(_A)
h3cDot11SaIntfDevDetected=NotificationType((1,3,6,1,4,1,2011,10,2,75,13,3,0,1))
h3cDot11SaIntfDevDetected.setObjects(*((_B,_G),(_B,_H),(_B,_M),(_B,_N),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:h3cDot11SaIntfDevDetected.setStatus(_A)
h3cDot11SaIntfDevDisappear=NotificationType((1,3,6,1,4,1,2011,10,2,75,13,3,0,2))
h3cDot11SaIntfDevDisappear.setObjects(*((_B,_G),(_B,_H),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:h3cDot11SaIntfDevDisappear.setStatus(_A)
h3cDot11SaChlQltLow=NotificationType((1,3,6,1,4,1,2011,10,2,75,13,3,0,3))
h3cDot11SaChlQltLow.setObjects(*((_B,_G),(_B,_H),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:h3cDot11SaChlQltLow.setStatus(_A)
h3cDot11SaChlQltRecover=NotificationType((1,3,6,1,4,1,2011,10,2,75,13,3,0,4))
h3cDot11SaChlQltRecover.setObjects(*((_B,_G),(_B,_H),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:h3cDot11SaChlQltRecover.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h3cDot11Sa':h3cDot11Sa,'h3cDot11SaCfgGroup':h3cDot11SaCfgGroup,'h3cDot11SaCfgTable':h3cDot11SaCfgTable,'h3cDot11SaCfgEntry':h3cDot11SaCfgEntry,_R:h3cDot11SaCfgRadioType,'h3cDot11SaEnable':h3cDot11SaEnable,'h3cDot11SaRptDevType':h3cDot11SaRptDevType,'h3cDot11SaTrapDevEnable':h3cDot11SaTrapDevEnable,'h3cDot11SaTrapDevType':h3cDot11SaTrapDevType,'h3cDot11SaTrapAQEnable':h3cDot11SaTrapAQEnable,'h3cDot11SaTrapAQThreshold':h3cDot11SaTrapAQThreshold,'h3cDot11SaDrivenRRMEnable':h3cDot11SaDrivenRRMEnable,'h3cDot11SaDrivenRRMSnt':h3cDot11SaDrivenRRMSnt,'h3cDot11SaStatusGroup':h3cDot11SaStatusGroup,'h3cDot11SaRtFFTDataTable':h3cDot11SaRtFFTDataTable,'h3cDot11SaRtFFTDataEntry':h3cDot11SaRtFFTDataEntry,_J:h3cDot11SaAPID,_K:h3cDot11SaRadioID,_e:h3cDot11SaRtDataGroupID,_f:h3cDot11SaFrequency,'h3cDot11SaRtFreqPower':h3cDot11SaRtFreqPower,'h3cDot11SaRtFreqMaxPower':h3cDot11SaRtFreqMaxPower,'h3cDot11SaRtFreqDutyCycle':h3cDot11SaRtFreqDutyCycle,'h3cDot11SaRtFreqDataSeqNo':h3cDot11SaRtFreqDataSeqNo,'h3cDot11SaIntfDevTable':h3cDot11SaIntfDevTable,'h3cDot11SaIntfDevEntry':h3cDot11SaIntfDevEntry,_g:h3cDot11SaDevID,'h3cDot11SaDevType':h3cDot11SaDevType,'h3cDot11SaDevSI':h3cDot11SaDevSI,'h3cDot11SaDevRSSI':h3cDot11SaDevRSSI,'h3cDot11SaDevDutyCycle':h3cDot11SaDevDutyCycle,'h3cDot11SaDevAffectedChls':h3cDot11SaDevAffectedChls,'h3cDot11SaDevDetectedTime':h3cDot11SaDevDetectedTime,'h3cDot11SaAirQualityTable':h3cDot11SaAirQualityTable,'h3cDot11SaAirQualityEntry':h3cDot11SaAirQualityEntry,_h:h3cDot11SaChlNum,'h3cDot11SaAvgQuality':h3cDot11SaAvgQuality,'h3cDot11SaMinQuality':h3cDot11SaMinQuality,'h3cDot11SaIntfDevNum':h3cDot11SaIntfDevNum,'h3cDot11SaWiFiUtil':h3cDot11SaWiFiUtil,'h3cDot11SaNonWiFiUtil':h3cDot11SaNonWiFiUtil,'h3cDot11SaNoiseFloor':h3cDot11SaNoiseFloor,'h3cDot11SaNotifyGroup':h3cDot11SaNotifyGroup,'h3cDot11SaTraps':h3cDot11SaTraps,'h3cDot11SaIntfDevDetected':h3cDot11SaIntfDevDetected,'h3cDot11SaIntfDevDisappear':h3cDot11SaIntfDevDisappear,'h3cDot11SaChlQltLow':h3cDot11SaChlQltLow,'h3cDot11SaChlQltRecover':h3cDot11SaChlQltRecover,'h3cDot11SaTrapVars':h3cDot11SaTrapVars,_G:h3cDot11SaTrapAPID,_H:h3cDot11SaTrapRadioID,_M:h3cDot11SaTrapDevID,_N:h3cDot11SaTrapIntfDevType,_i:h3cDot11APTrapDevSI,_j:h3cDot11SaTrapDevRSSI,_k:h3cDot11APTrapDevDC,_l:h3cDot11APTrapDevChls,_m:h3cDot11APTrapDevDctTime,_O:h3cDot11SaTrapChlNum,_P:h3cDot11SaTrapChlQlt,_Q:h3cDot11SaTrapChlIntfNum})