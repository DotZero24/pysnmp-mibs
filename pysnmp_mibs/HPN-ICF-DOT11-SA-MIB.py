_m='hpnicfDot11APTrapDevDctTime'
_l='hpnicfDot11APTrapDevChls'
_k='hpnicfDot11APTrapDevDC'
_j='hpnicfDot11SaTrapDevRSSI'
_i='hpnicfDot11APTrapDevSI'
_h='hpnicfDot11SaChlNum'
_g='hpnicfDot11SaDevID'
_f='hpnicfDot11SaFrequency'
_e='hpnicfDot11SaRtDataGroupID'
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
_R='hpnicfDot11SaCfgRadioType'
_Q='hpnicfDot11SaTrapChlIntfNum'
_P='hpnicfDot11SaTrapChlQlt'
_O='hpnicfDot11SaTrapChlNum'
_N='hpnicfDot11SaTrapIntfDevType'
_M='hpnicfDot11SaTrapDevID'
_L='Bits'
_K='hpnicfDot11SaRadioID'
_J='hpnicfDot11SaAPID'
_I='Integer32'
_H='hpnicfDot11SaTrapRadioID'
_G='hpnicfDot11SaTrapAPID'
_F='not-accessible'
_E='read-write'
_D='accessible-for-notify'
_C='read-only'
_B='HPN-ICF-DOT11-SA-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HpnicfDot11ChannelScopeType,HpnicfDot11ObjectIDType,HpnicfDot11RadioScopeType,HpnicfDot11SaIntfDevType,hpnicfDot11=mibBuilder.importSymbols('HPN-ICF-DOT11-REF-MIB','HpnicfDot11ChannelScopeType','HpnicfDot11ObjectIDType','HpnicfDot11RadioScopeType','HpnicfDot11SaIntfDevType','hpnicfDot11')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_L,'Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention','TruthValue')
hpnicfDot11Sa=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,13))
if mibBuilder.loadTexts:hpnicfDot11Sa.setRevisions(('2011-08-26 20:00',))
_HpnicfDot11SaCfgGroup_ObjectIdentity=ObjectIdentity
hpnicfDot11SaCfgGroup=_HpnicfDot11SaCfgGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,13,1))
_HpnicfDot11SaCfgTable_Object=MibTable
hpnicfDot11SaCfgTable=_HpnicfDot11SaCfgTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,1,1))
if mibBuilder.loadTexts:hpnicfDot11SaCfgTable.setStatus(_A)
_HpnicfDot11SaCfgEntry_Object=MibTableRow
hpnicfDot11SaCfgEntry=_HpnicfDot11SaCfgEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,1,1,1))
hpnicfDot11SaCfgEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:hpnicfDot11SaCfgEntry.setStatus(_A)
class _HpnicfDot11SaCfgRadioType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dot11bg',1),('dot11a',2)))
_HpnicfDot11SaCfgRadioType_Type.__name__=_I
_HpnicfDot11SaCfgRadioType_Object=MibTableColumn
hpnicfDot11SaCfgRadioType=_HpnicfDot11SaCfgRadioType_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,1,1,1,1),_HpnicfDot11SaCfgRadioType_Type())
hpnicfDot11SaCfgRadioType.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11SaCfgRadioType.setStatus(_A)
_HpnicfDot11SaEnable_Type=TruthValue
_HpnicfDot11SaEnable_Object=MibTableColumn
hpnicfDot11SaEnable=_HpnicfDot11SaEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,1,1,1,2),_HpnicfDot11SaEnable_Type())
hpnicfDot11SaEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDot11SaEnable.setStatus(_A)
class _HpnicfDot11SaRptDevType_Type(Bits):namedValues=NamedValues(*((_S,0),(_T,1),(_U,2),(_V,3),(_W,4),(_X,5),(_Y,6),(_Z,7),(_a,8),(_b,9),(_c,10),(_d,11)))
_HpnicfDot11SaRptDevType_Type.__name__=_L
_HpnicfDot11SaRptDevType_Object=MibTableColumn
hpnicfDot11SaRptDevType=_HpnicfDot11SaRptDevType_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,1,1,1,3),_HpnicfDot11SaRptDevType_Type())
hpnicfDot11SaRptDevType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDot11SaRptDevType.setStatus(_A)
_HpnicfDot11SaTrapDevEnable_Type=TruthValue
_HpnicfDot11SaTrapDevEnable_Object=MibTableColumn
hpnicfDot11SaTrapDevEnable=_HpnicfDot11SaTrapDevEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,1,1,1,4),_HpnicfDot11SaTrapDevEnable_Type())
hpnicfDot11SaTrapDevEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDot11SaTrapDevEnable.setStatus(_A)
class _HpnicfDot11SaTrapDevType_Type(Bits):namedValues=NamedValues(*((_S,0),(_T,1),(_U,2),(_V,3),(_W,4),(_X,5),(_Y,6),(_Z,7),(_a,8),(_b,9),(_c,10),(_d,11)))
_HpnicfDot11SaTrapDevType_Type.__name__=_L
_HpnicfDot11SaTrapDevType_Object=MibTableColumn
hpnicfDot11SaTrapDevType=_HpnicfDot11SaTrapDevType_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,1,1,1,5),_HpnicfDot11SaTrapDevType_Type())
hpnicfDot11SaTrapDevType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDot11SaTrapDevType.setStatus(_A)
_HpnicfDot11SaTrapAQEnable_Type=TruthValue
_HpnicfDot11SaTrapAQEnable_Object=MibTableColumn
hpnicfDot11SaTrapAQEnable=_HpnicfDot11SaTrapAQEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,1,1,1,6),_HpnicfDot11SaTrapAQEnable_Type())
hpnicfDot11SaTrapAQEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDot11SaTrapAQEnable.setStatus(_A)
class _HpnicfDot11SaTrapAQThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HpnicfDot11SaTrapAQThreshold_Type.__name__=_I
_HpnicfDot11SaTrapAQThreshold_Object=MibTableColumn
hpnicfDot11SaTrapAQThreshold=_HpnicfDot11SaTrapAQThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,1,1,1,7),_HpnicfDot11SaTrapAQThreshold_Type())
hpnicfDot11SaTrapAQThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDot11SaTrapAQThreshold.setStatus(_A)
_HpnicfDot11SaDrivenRRMEnable_Type=TruthValue
_HpnicfDot11SaDrivenRRMEnable_Object=MibTableColumn
hpnicfDot11SaDrivenRRMEnable=_HpnicfDot11SaDrivenRRMEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,1,1,1,8),_HpnicfDot11SaDrivenRRMEnable_Type())
hpnicfDot11SaDrivenRRMEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDot11SaDrivenRRMEnable.setStatus(_A)
class _HpnicfDot11SaDrivenRRMSnt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('low',1),('medium',2),('high',3)))
_HpnicfDot11SaDrivenRRMSnt_Type.__name__=_I
_HpnicfDot11SaDrivenRRMSnt_Object=MibTableColumn
hpnicfDot11SaDrivenRRMSnt=_HpnicfDot11SaDrivenRRMSnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,1,1,1,9),_HpnicfDot11SaDrivenRRMSnt_Type())
hpnicfDot11SaDrivenRRMSnt.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDot11SaDrivenRRMSnt.setStatus(_A)
_HpnicfDot11SaStatusGroup_ObjectIdentity=ObjectIdentity
hpnicfDot11SaStatusGroup=_HpnicfDot11SaStatusGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,13,2))
_HpnicfDot11SaRtFFTDataTable_Object=MibTable
hpnicfDot11SaRtFFTDataTable=_HpnicfDot11SaRtFFTDataTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,2,1))
if mibBuilder.loadTexts:hpnicfDot11SaRtFFTDataTable.setStatus(_A)
_HpnicfDot11SaRtFFTDataEntry_Object=MibTableRow
hpnicfDot11SaRtFFTDataEntry=_HpnicfDot11SaRtFFTDataEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,2,1,1))
hpnicfDot11SaRtFFTDataEntry.setIndexNames((0,_B,_J),(0,_B,_K),(0,_B,_e),(0,_B,_f))
if mibBuilder.loadTexts:hpnicfDot11SaRtFFTDataEntry.setStatus(_A)
_HpnicfDot11SaAPID_Type=HpnicfDot11ObjectIDType
_HpnicfDot11SaAPID_Object=MibTableColumn
hpnicfDot11SaAPID=_HpnicfDot11SaAPID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,2,1,1,1),_HpnicfDot11SaAPID_Type())
hpnicfDot11SaAPID.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11SaAPID.setStatus(_A)
_HpnicfDot11SaRadioID_Type=HpnicfDot11RadioScopeType
_HpnicfDot11SaRadioID_Object=MibTableColumn
hpnicfDot11SaRadioID=_HpnicfDot11SaRadioID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,2,1,1,2),_HpnicfDot11SaRadioID_Type())
hpnicfDot11SaRadioID.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11SaRadioID.setStatus(_A)
_HpnicfDot11SaRtDataGroupID_Type=Integer32
_HpnicfDot11SaRtDataGroupID_Object=MibTableColumn
hpnicfDot11SaRtDataGroupID=_HpnicfDot11SaRtDataGroupID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,2,1,1,3),_HpnicfDot11SaRtDataGroupID_Type())
hpnicfDot11SaRtDataGroupID.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11SaRtDataGroupID.setStatus(_A)
_HpnicfDot11SaFrequency_Type=Integer32
_HpnicfDot11SaFrequency_Object=MibTableColumn
hpnicfDot11SaFrequency=_HpnicfDot11SaFrequency_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,2,1,1,4),_HpnicfDot11SaFrequency_Type())
hpnicfDot11SaFrequency.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11SaFrequency.setStatus(_A)
_HpnicfDot11SaRtFreqPower_Type=Integer32
_HpnicfDot11SaRtFreqPower_Object=MibTableColumn
hpnicfDot11SaRtFreqPower=_HpnicfDot11SaRtFreqPower_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,2,1,1,5),_HpnicfDot11SaRtFreqPower_Type())
hpnicfDot11SaRtFreqPower.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SaRtFreqPower.setStatus(_A)
_HpnicfDot11SaRtFreqMaxPower_Type=Integer32
_HpnicfDot11SaRtFreqMaxPower_Object=MibTableColumn
hpnicfDot11SaRtFreqMaxPower=_HpnicfDot11SaRtFreqMaxPower_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,2,1,1,6),_HpnicfDot11SaRtFreqMaxPower_Type())
hpnicfDot11SaRtFreqMaxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SaRtFreqMaxPower.setStatus(_A)
_HpnicfDot11SaRtFreqDutyCycle_Type=Integer32
_HpnicfDot11SaRtFreqDutyCycle_Object=MibTableColumn
hpnicfDot11SaRtFreqDutyCycle=_HpnicfDot11SaRtFreqDutyCycle_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,2,1,1,7),_HpnicfDot11SaRtFreqDutyCycle_Type())
hpnicfDot11SaRtFreqDutyCycle.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SaRtFreqDutyCycle.setStatus(_A)
_HpnicfDot11SaRtFreqDataSeqNo_Type=Unsigned32
_HpnicfDot11SaRtFreqDataSeqNo_Object=MibTableColumn
hpnicfDot11SaRtFreqDataSeqNo=_HpnicfDot11SaRtFreqDataSeqNo_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,2,1,1,8),_HpnicfDot11SaRtFreqDataSeqNo_Type())
hpnicfDot11SaRtFreqDataSeqNo.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SaRtFreqDataSeqNo.setStatus(_A)
_HpnicfDot11SaIntfDevTable_Object=MibTable
hpnicfDot11SaIntfDevTable=_HpnicfDot11SaIntfDevTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,2,2))
if mibBuilder.loadTexts:hpnicfDot11SaIntfDevTable.setStatus(_A)
_HpnicfDot11SaIntfDevEntry_Object=MibTableRow
hpnicfDot11SaIntfDevEntry=_HpnicfDot11SaIntfDevEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,2,2,1))
hpnicfDot11SaIntfDevEntry.setIndexNames((0,_B,_J),(0,_B,_K),(0,_B,_g))
if mibBuilder.loadTexts:hpnicfDot11SaIntfDevEntry.setStatus(_A)
_HpnicfDot11SaDevID_Type=Integer32
_HpnicfDot11SaDevID_Object=MibTableColumn
hpnicfDot11SaDevID=_HpnicfDot11SaDevID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,2,2,1,1),_HpnicfDot11SaDevID_Type())
hpnicfDot11SaDevID.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11SaDevID.setStatus(_A)
_HpnicfDot11SaDevType_Type=HpnicfDot11SaIntfDevType
_HpnicfDot11SaDevType_Object=MibTableColumn
hpnicfDot11SaDevType=_HpnicfDot11SaDevType_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,2,2,1,2),_HpnicfDot11SaDevType_Type())
hpnicfDot11SaDevType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SaDevType.setStatus(_A)
_HpnicfDot11SaDevSI_Type=Integer32
_HpnicfDot11SaDevSI_Object=MibTableColumn
hpnicfDot11SaDevSI=_HpnicfDot11SaDevSI_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,2,2,1,3),_HpnicfDot11SaDevSI_Type())
hpnicfDot11SaDevSI.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SaDevSI.setStatus(_A)
_HpnicfDot11SaDevRSSI_Type=Integer32
_HpnicfDot11SaDevRSSI_Object=MibTableColumn
hpnicfDot11SaDevRSSI=_HpnicfDot11SaDevRSSI_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,2,2,1,4),_HpnicfDot11SaDevRSSI_Type())
hpnicfDot11SaDevRSSI.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SaDevRSSI.setStatus(_A)
_HpnicfDot11SaDevDutyCycle_Type=Integer32
_HpnicfDot11SaDevDutyCycle_Object=MibTableColumn
hpnicfDot11SaDevDutyCycle=_HpnicfDot11SaDevDutyCycle_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,2,2,1,5),_HpnicfDot11SaDevDutyCycle_Type())
hpnicfDot11SaDevDutyCycle.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SaDevDutyCycle.setStatus(_A)
_HpnicfDot11SaDevAffectedChls_Type=OctetString
_HpnicfDot11SaDevAffectedChls_Object=MibTableColumn
hpnicfDot11SaDevAffectedChls=_HpnicfDot11SaDevAffectedChls_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,2,2,1,6),_HpnicfDot11SaDevAffectedChls_Type())
hpnicfDot11SaDevAffectedChls.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SaDevAffectedChls.setStatus(_A)
_HpnicfDot11SaDevDetectedTime_Type=DateAndTime
_HpnicfDot11SaDevDetectedTime_Object=MibTableColumn
hpnicfDot11SaDevDetectedTime=_HpnicfDot11SaDevDetectedTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,2,2,1,7),_HpnicfDot11SaDevDetectedTime_Type())
hpnicfDot11SaDevDetectedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SaDevDetectedTime.setStatus(_A)
_HpnicfDot11SaAirQualityTable_Object=MibTable
hpnicfDot11SaAirQualityTable=_HpnicfDot11SaAirQualityTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,2,3))
if mibBuilder.loadTexts:hpnicfDot11SaAirQualityTable.setStatus(_A)
_HpnicfDot11SaAirQualityEntry_Object=MibTableRow
hpnicfDot11SaAirQualityEntry=_HpnicfDot11SaAirQualityEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,2,3,1))
hpnicfDot11SaAirQualityEntry.setIndexNames((0,_B,_J),(0,_B,_K),(0,_B,_h))
if mibBuilder.loadTexts:hpnicfDot11SaAirQualityEntry.setStatus(_A)
_HpnicfDot11SaChlNum_Type=HpnicfDot11ChannelScopeType
_HpnicfDot11SaChlNum_Object=MibTableColumn
hpnicfDot11SaChlNum=_HpnicfDot11SaChlNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,2,3,1,1),_HpnicfDot11SaChlNum_Type())
hpnicfDot11SaChlNum.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11SaChlNum.setStatus(_A)
_HpnicfDot11SaAvgQuality_Type=Integer32
_HpnicfDot11SaAvgQuality_Object=MibTableColumn
hpnicfDot11SaAvgQuality=_HpnicfDot11SaAvgQuality_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,2,3,1,2),_HpnicfDot11SaAvgQuality_Type())
hpnicfDot11SaAvgQuality.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SaAvgQuality.setStatus(_A)
_HpnicfDot11SaMinQuality_Type=Integer32
_HpnicfDot11SaMinQuality_Object=MibTableColumn
hpnicfDot11SaMinQuality=_HpnicfDot11SaMinQuality_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,2,3,1,3),_HpnicfDot11SaMinQuality_Type())
hpnicfDot11SaMinQuality.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SaMinQuality.setStatus(_A)
_HpnicfDot11SaIntfDevNum_Type=Integer32
_HpnicfDot11SaIntfDevNum_Object=MibTableColumn
hpnicfDot11SaIntfDevNum=_HpnicfDot11SaIntfDevNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,2,3,1,4),_HpnicfDot11SaIntfDevNum_Type())
hpnicfDot11SaIntfDevNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SaIntfDevNum.setStatus(_A)
_HpnicfDot11SaWiFiUtil_Type=Integer32
_HpnicfDot11SaWiFiUtil_Object=MibTableColumn
hpnicfDot11SaWiFiUtil=_HpnicfDot11SaWiFiUtil_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,2,3,1,5),_HpnicfDot11SaWiFiUtil_Type())
hpnicfDot11SaWiFiUtil.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SaWiFiUtil.setStatus(_A)
_HpnicfDot11SaNonWiFiUtil_Type=Integer32
_HpnicfDot11SaNonWiFiUtil_Object=MibTableColumn
hpnicfDot11SaNonWiFiUtil=_HpnicfDot11SaNonWiFiUtil_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,2,3,1,6),_HpnicfDot11SaNonWiFiUtil_Type())
hpnicfDot11SaNonWiFiUtil.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SaNonWiFiUtil.setStatus(_A)
_HpnicfDot11SaNoiseFloor_Type=Integer32
_HpnicfDot11SaNoiseFloor_Object=MibTableColumn
hpnicfDot11SaNoiseFloor=_HpnicfDot11SaNoiseFloor_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,2,3,1,7),_HpnicfDot11SaNoiseFloor_Type())
hpnicfDot11SaNoiseFloor.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SaNoiseFloor.setStatus(_A)
_HpnicfDot11SaNotifyGroup_ObjectIdentity=ObjectIdentity
hpnicfDot11SaNotifyGroup=_HpnicfDot11SaNotifyGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,13,3))
_HpnicfDot11SaTraps_ObjectIdentity=ObjectIdentity
hpnicfDot11SaTraps=_HpnicfDot11SaTraps_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,13,3,0))
_HpnicfDot11SaTrapVars_ObjectIdentity=ObjectIdentity
hpnicfDot11SaTrapVars=_HpnicfDot11SaTrapVars_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,13,3,1))
_HpnicfDot11SaTrapAPID_Type=HpnicfDot11ObjectIDType
_HpnicfDot11SaTrapAPID_Object=MibScalar
hpnicfDot11SaTrapAPID=_HpnicfDot11SaTrapAPID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,3,1,1),_HpnicfDot11SaTrapAPID_Type())
hpnicfDot11SaTrapAPID.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11SaTrapAPID.setStatus(_A)
_HpnicfDot11SaTrapRadioID_Type=HpnicfDot11RadioScopeType
_HpnicfDot11SaTrapRadioID_Object=MibScalar
hpnicfDot11SaTrapRadioID=_HpnicfDot11SaTrapRadioID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,3,1,2),_HpnicfDot11SaTrapRadioID_Type())
hpnicfDot11SaTrapRadioID.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11SaTrapRadioID.setStatus(_A)
_HpnicfDot11SaTrapDevID_Type=Integer32
_HpnicfDot11SaTrapDevID_Object=MibScalar
hpnicfDot11SaTrapDevID=_HpnicfDot11SaTrapDevID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,3,1,3),_HpnicfDot11SaTrapDevID_Type())
hpnicfDot11SaTrapDevID.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11SaTrapDevID.setStatus(_A)
_HpnicfDot11SaTrapIntfDevType_Type=HpnicfDot11SaIntfDevType
_HpnicfDot11SaTrapIntfDevType_Object=MibScalar
hpnicfDot11SaTrapIntfDevType=_HpnicfDot11SaTrapIntfDevType_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,3,1,4),_HpnicfDot11SaTrapIntfDevType_Type())
hpnicfDot11SaTrapIntfDevType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11SaTrapIntfDevType.setStatus(_A)
_HpnicfDot11APTrapDevSI_Type=Integer32
_HpnicfDot11APTrapDevSI_Object=MibScalar
hpnicfDot11APTrapDevSI=_HpnicfDot11APTrapDevSI_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,3,1,5),_HpnicfDot11APTrapDevSI_Type())
hpnicfDot11APTrapDevSI.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11APTrapDevSI.setStatus(_A)
_HpnicfDot11SaTrapDevRSSI_Type=Integer32
_HpnicfDot11SaTrapDevRSSI_Object=MibScalar
hpnicfDot11SaTrapDevRSSI=_HpnicfDot11SaTrapDevRSSI_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,3,1,6),_HpnicfDot11SaTrapDevRSSI_Type())
hpnicfDot11SaTrapDevRSSI.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11SaTrapDevRSSI.setStatus(_A)
_HpnicfDot11APTrapDevDC_Type=Integer32
_HpnicfDot11APTrapDevDC_Object=MibScalar
hpnicfDot11APTrapDevDC=_HpnicfDot11APTrapDevDC_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,3,1,7),_HpnicfDot11APTrapDevDC_Type())
hpnicfDot11APTrapDevDC.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11APTrapDevDC.setStatus(_A)
_HpnicfDot11APTrapDevChls_Type=OctetString
_HpnicfDot11APTrapDevChls_Object=MibScalar
hpnicfDot11APTrapDevChls=_HpnicfDot11APTrapDevChls_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,3,1,8),_HpnicfDot11APTrapDevChls_Type())
hpnicfDot11APTrapDevChls.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11APTrapDevChls.setStatus(_A)
_HpnicfDot11APTrapDevDctTime_Type=DateAndTime
_HpnicfDot11APTrapDevDctTime_Object=MibScalar
hpnicfDot11APTrapDevDctTime=_HpnicfDot11APTrapDevDctTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,3,1,9),_HpnicfDot11APTrapDevDctTime_Type())
hpnicfDot11APTrapDevDctTime.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11APTrapDevDctTime.setStatus(_A)
_HpnicfDot11SaTrapChlNum_Type=HpnicfDot11ChannelScopeType
_HpnicfDot11SaTrapChlNum_Object=MibScalar
hpnicfDot11SaTrapChlNum=_HpnicfDot11SaTrapChlNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,3,1,10),_HpnicfDot11SaTrapChlNum_Type())
hpnicfDot11SaTrapChlNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11SaTrapChlNum.setStatus(_A)
_HpnicfDot11SaTrapChlQlt_Type=Integer32
_HpnicfDot11SaTrapChlQlt_Object=MibScalar
hpnicfDot11SaTrapChlQlt=_HpnicfDot11SaTrapChlQlt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,3,1,11),_HpnicfDot11SaTrapChlQlt_Type())
hpnicfDot11SaTrapChlQlt.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11SaTrapChlQlt.setStatus(_A)
_HpnicfDot11SaTrapChlIntfNum_Type=Integer32
_HpnicfDot11SaTrapChlIntfNum_Object=MibScalar
hpnicfDot11SaTrapChlIntfNum=_HpnicfDot11SaTrapChlIntfNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,13,3,1,12),_HpnicfDot11SaTrapChlIntfNum_Type())
hpnicfDot11SaTrapChlIntfNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11SaTrapChlIntfNum.setStatus(_A)
hpnicfDot11SaIntfDevDetected=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,13,3,0,1))
hpnicfDot11SaIntfDevDetected.setObjects(*((_B,_G),(_B,_H),(_B,_M),(_B,_N),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:hpnicfDot11SaIntfDevDetected.setStatus(_A)
hpnicfDot11SaIntfDevDisappear=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,13,3,0,2))
hpnicfDot11SaIntfDevDisappear.setObjects(*((_B,_G),(_B,_H),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:hpnicfDot11SaIntfDevDisappear.setStatus(_A)
hpnicfDot11SaChlQltLow=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,13,3,0,3))
hpnicfDot11SaChlQltLow.setObjects(*((_B,_G),(_B,_H),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:hpnicfDot11SaChlQltLow.setStatus(_A)
hpnicfDot11SaChlQltRecover=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,13,3,0,4))
hpnicfDot11SaChlQltRecover.setObjects(*((_B,_G),(_B,_H),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:hpnicfDot11SaChlQltRecover.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpnicfDot11Sa':hpnicfDot11Sa,'hpnicfDot11SaCfgGroup':hpnicfDot11SaCfgGroup,'hpnicfDot11SaCfgTable':hpnicfDot11SaCfgTable,'hpnicfDot11SaCfgEntry':hpnicfDot11SaCfgEntry,_R:hpnicfDot11SaCfgRadioType,'hpnicfDot11SaEnable':hpnicfDot11SaEnable,'hpnicfDot11SaRptDevType':hpnicfDot11SaRptDevType,'hpnicfDot11SaTrapDevEnable':hpnicfDot11SaTrapDevEnable,'hpnicfDot11SaTrapDevType':hpnicfDot11SaTrapDevType,'hpnicfDot11SaTrapAQEnable':hpnicfDot11SaTrapAQEnable,'hpnicfDot11SaTrapAQThreshold':hpnicfDot11SaTrapAQThreshold,'hpnicfDot11SaDrivenRRMEnable':hpnicfDot11SaDrivenRRMEnable,'hpnicfDot11SaDrivenRRMSnt':hpnicfDot11SaDrivenRRMSnt,'hpnicfDot11SaStatusGroup':hpnicfDot11SaStatusGroup,'hpnicfDot11SaRtFFTDataTable':hpnicfDot11SaRtFFTDataTable,'hpnicfDot11SaRtFFTDataEntry':hpnicfDot11SaRtFFTDataEntry,_J:hpnicfDot11SaAPID,_K:hpnicfDot11SaRadioID,_e:hpnicfDot11SaRtDataGroupID,_f:hpnicfDot11SaFrequency,'hpnicfDot11SaRtFreqPower':hpnicfDot11SaRtFreqPower,'hpnicfDot11SaRtFreqMaxPower':hpnicfDot11SaRtFreqMaxPower,'hpnicfDot11SaRtFreqDutyCycle':hpnicfDot11SaRtFreqDutyCycle,'hpnicfDot11SaRtFreqDataSeqNo':hpnicfDot11SaRtFreqDataSeqNo,'hpnicfDot11SaIntfDevTable':hpnicfDot11SaIntfDevTable,'hpnicfDot11SaIntfDevEntry':hpnicfDot11SaIntfDevEntry,_g:hpnicfDot11SaDevID,'hpnicfDot11SaDevType':hpnicfDot11SaDevType,'hpnicfDot11SaDevSI':hpnicfDot11SaDevSI,'hpnicfDot11SaDevRSSI':hpnicfDot11SaDevRSSI,'hpnicfDot11SaDevDutyCycle':hpnicfDot11SaDevDutyCycle,'hpnicfDot11SaDevAffectedChls':hpnicfDot11SaDevAffectedChls,'hpnicfDot11SaDevDetectedTime':hpnicfDot11SaDevDetectedTime,'hpnicfDot11SaAirQualityTable':hpnicfDot11SaAirQualityTable,'hpnicfDot11SaAirQualityEntry':hpnicfDot11SaAirQualityEntry,_h:hpnicfDot11SaChlNum,'hpnicfDot11SaAvgQuality':hpnicfDot11SaAvgQuality,'hpnicfDot11SaMinQuality':hpnicfDot11SaMinQuality,'hpnicfDot11SaIntfDevNum':hpnicfDot11SaIntfDevNum,'hpnicfDot11SaWiFiUtil':hpnicfDot11SaWiFiUtil,'hpnicfDot11SaNonWiFiUtil':hpnicfDot11SaNonWiFiUtil,'hpnicfDot11SaNoiseFloor':hpnicfDot11SaNoiseFloor,'hpnicfDot11SaNotifyGroup':hpnicfDot11SaNotifyGroup,'hpnicfDot11SaTraps':hpnicfDot11SaTraps,'hpnicfDot11SaIntfDevDetected':hpnicfDot11SaIntfDevDetected,'hpnicfDot11SaIntfDevDisappear':hpnicfDot11SaIntfDevDisappear,'hpnicfDot11SaChlQltLow':hpnicfDot11SaChlQltLow,'hpnicfDot11SaChlQltRecover':hpnicfDot11SaChlQltRecover,'hpnicfDot11SaTrapVars':hpnicfDot11SaTrapVars,_G:hpnicfDot11SaTrapAPID,_H:hpnicfDot11SaTrapRadioID,_M:hpnicfDot11SaTrapDevID,_N:hpnicfDot11SaTrapIntfDevType,_i:hpnicfDot11APTrapDevSI,_j:hpnicfDot11SaTrapDevRSSI,_k:hpnicfDot11APTrapDevDC,_l:hpnicfDot11APTrapDevChls,_m:hpnicfDot11APTrapDevDctTime,_O:hpnicfDot11SaTrapChlNum,_P:hpnicfDot11SaTrapChlQlt,_Q:hpnicfDot11SaTrapChlIntfNum})