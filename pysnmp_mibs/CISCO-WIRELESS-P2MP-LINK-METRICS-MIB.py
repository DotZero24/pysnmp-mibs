_B2='p2mpComplianceNotifGroup'
_B1='p2mpComplianceHeMetricsGroup'
_B0='p2mpComplianceSuMetricsGroup'
_A_='p2mpComplianceLinkMetricsGroup'
_Az='p2mpSuDegradedSecAlarmTrap'
_Ay='p2mpSuConsecSevErrSecAlarmTrap'
_Ax='p2mpSuSevErrSecAlarmTrap'
_Aw='p2mpSuErrSecAlarmTrap'
_Av='p2mpHeMacPctErrCWThreshTrap'
_Au='p2mpHeChPctErrCWThreshTrap'
_At='p2mpHe1HrErroredCodewords'
_As='p2mpHe1HrTotalCodewords'
_Ar='p2mpHe1HrUpdateTime'
_Aq='p2mpHe1MinErroredCodewords'
_Ap='p2mpHe1MinTotalCodewords'
_Ao='p2mpHe1MinUpdateTime'
_An='p2mpHe1SecErroredCodewords'
_Am='p2mpHe1SecTotalCodewords'
_Al='p2mpHe1SecUpdateTime'
_Ak='p2mpErroredCodewords'
_Aj='p2mpTotalCodewords'
_Ai='p2mpHeCWErrorUpdateTime'
_Ah='p2mpBadSuUpdateTime'
_Ag='p2mpHe1HrMinTotalCWThresh'
_Af='p2mpSuPercentEfficiency'
_Ae='p2mpSuEffectiveDataRate'
_Ad='p2mpSuLastSyncFailTime'
_Ac='p2mpSuSyncFailureCount'
_Ab='p2mpSuSyncHighEffort'
_Aa='p2mpSuSyncMedEffort'
_AZ='p2mpSuLastSyncSuccessTime'
_AY='p2mpSuSyncSuccessCount'
_AX='p2mpSuInitialSyncSeconds'
_AW='p2mpSuPctDegradedSeconds'
_AV='p2mpSuPctSevErroredSeconds'
_AU='p2mpSuPctErroredSeconds'
_AT='p2mpSuPctErrorFreeSeconds'
_AS='p2mpSuSyncLossSeconds'
_AR='p2mpSuPctAvailSeconds'
_AQ='p2mpSuUnAvailableSeconds'
_AP='p2mpSuAvailableSeconds'
_AO='p2mpSu1HrDivAntRxPowerAvg'
_AN='p2mpSu1HrDivAntRxPowerMin'
_AM='p2mpSu1HrDivAntRxPowerMax'
_AL='p2mpSu1HrMainAntRxPowerAvg'
_AK='p2mpSu1HrMainAntRxPowerMin'
_AJ='p2mpSu1HrMainAntRxPowerMax'
_AI='p2mpSu1HrTxPowerAvg'
_AH='p2mpSu1HrTxPowerMin'
_AG='p2mpSu1HrTxPowerMax'
_AF='p2mpSu1HrDegradedSeconds'
_AE='p2mpSu1HrSyncLossSeconds'
_AD='p2mpSu1HrConsecSvErrSeconds'
_AC='p2mpSu1HrSevErroredSeconds'
_AB='p2mpSu1HrErroredSeconds'
_AA='p2mpSu1HrErrorFreeSeconds'
_A9='p2mpSu1HrValidDataPkt'
_A8='p2mpSu1HrTotalErrCodewords'
_A7='p2mpSu1HrTotalCodewords'
_A6='p2mpSu1HrUpdateTime'
_A5='p2mpSu1MinDivAntRxPowerAvg'
_A4='p2mpSu1MinDivAntRxPowerMin'
_A3='p2mpSu1MinDivAntRxPowerMax'
_A2='p2mpSu1MinMainAntRxPowerAvg'
_A1='p2mpSu1MinMainAntRxPowerMin'
_A0='p2mpSu1MinMainAntRxPowerMax'
_z='p2mpSu1MinTxPowerAvg'
_y='p2mpSu1MinTxPowerMin'
_x='p2mpSu1MinTxPowerMax'
_w='p2mpSu1MinDegradedSeconds'
_v='p2mpSu1MinSyncLossSeconds'
_u='p2mpSu1MinConsecSevErrSeconds'
_t='p2mpSu1MinSevErroredSeconds'
_s='p2mpSu1MinErroredSeconds'
_r='p2mpSu1MinErrorFreeSeconds'
_q='p2mpSu1MinValidDataPkt'
_p='p2mpSu1MinTotalErrCodewords'
_o='p2mpSu1MinTotalCodewords'
_n='p2mpSu1MinUpdateTime'
_m='p2mpSu1SecValidDataPkt'
_l='p2mpSu1SecTotalErrCodewords'
_k='p2mpSu1SecTotalCodewords'
_j='p2mpSu1SecType'
_i='p2mpSu1SecUpdateTime'
_h='p2mpSuLinkCSESThresh'
_g='p2mpSuLinkSESThresh'
_f='p2mpSuLinkDSThresh'
_e='p2mpSuLinkESThresh'
_d='p2mpLinkMetricsPrecision'
_c='p2mpLinkMetricsScale'
_b='p2mpHe1HrIndex'
_a='p2mpHe1MinIndex'
_Z='p2mpHe1SecIndex'
_Y='p2mpHeCWErrorIndex'
_X='p2mpSuMacAddress'
_W='p2mpBadSuIndex'
_V='p2mpSu1HrIndex'
_U='p2mpSu1MinIndex'
_T='p2mpSu1SecIndex'
_S='p2mpPctErroredCodewords'
_R='p2mpTotalErroredCodewords'
_Q='p2mpBadSuMacAddress'
_P='p2mpHe1HrPctErrCWThresh'
_O='p2mpSuLink1HrDCSAlarmThresh'
_N='p2mpSuLink1HrCSESAlarmThresh'
_M='p2mpSuLink1HrSESAlarmThresh'
_L='p2mpSuLink1HrESAlarmThresh'
_K='seconds'
_J='not-accessible'
_I='0.00001 percent'
_H='read-write'
_G='Integer32'
_F='ifIndex'
_E='IF-MIB'
_D='dBm - decibel milliwatts'
_C='read-only'
_B='CISCO-WIRELESS-P2MP-LINK-METRICS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CwrCwConsecutiveSevErrSecond,CwrCwDegradedSecond,CwrCwErrorFreeSecond,CwrCwErroredSecond,CwrCwSeverelyErroredSecond,CwrFixedPointPrecision,CwrFixedPointScale,CwrFixedPointValue,CwrPercentageValue,CwrUpdateTime,WirelessGauge64=mibBuilder.importSymbols('CISCO-WIRELESS-TC-MIB','CwrCwConsecutiveSevErrSecond','CwrCwDegradedSecond','CwrCwErrorFreeSecond','CwrCwErroredSecond','CwrCwSeverelyErroredSecond','CwrFixedPointPrecision','CwrFixedPointScale','CwrFixedPointValue','CwrPercentageValue','CwrUpdateTime','WirelessGauge64')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TimeInterval=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TimeInterval')
ciscoWirelessLinkMetricsMIB=ModuleIdentity((1,3,6,1,4,1,9,9,181))
if mibBuilder.loadTexts:ciscoWirelessLinkMetricsMIB.setRevisions(('2006-01-04 10:03','2000-02-14 19:10'))
_P2mpLinkMetricsGroup_ObjectIdentity=ObjectIdentity
p2mpLinkMetricsGroup=_P2mpLinkMetricsGroup_ObjectIdentity((1,3,6,1,4,1,9,9,181,1))
_P2mpMetricsPrecisionTable_Object=MibTable
p2mpMetricsPrecisionTable=_P2mpMetricsPrecisionTable_Object((1,3,6,1,4,1,9,9,181,1,1))
if mibBuilder.loadTexts:p2mpMetricsPrecisionTable.setStatus(_A)
_P2mpMetricsPrecisionEntry_Object=MibTableRow
p2mpMetricsPrecisionEntry=_P2mpMetricsPrecisionEntry_Object((1,3,6,1,4,1,9,9,181,1,1,1))
p2mpMetricsPrecisionEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:p2mpMetricsPrecisionEntry.setStatus(_A)
_P2mpLinkMetricsScale_Type=CwrFixedPointScale
_P2mpLinkMetricsScale_Object=MibTableColumn
p2mpLinkMetricsScale=_P2mpLinkMetricsScale_Object((1,3,6,1,4,1,9,9,181,1,1,1,1),_P2mpLinkMetricsScale_Type())
p2mpLinkMetricsScale.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpLinkMetricsScale.setStatus(_A)
_P2mpLinkMetricsPrecision_Type=CwrFixedPointPrecision
_P2mpLinkMetricsPrecision_Object=MibTableColumn
p2mpLinkMetricsPrecision=_P2mpLinkMetricsPrecision_Object((1,3,6,1,4,1,9,9,181,1,1,1,2),_P2mpLinkMetricsPrecision_Type())
p2mpLinkMetricsPrecision.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpLinkMetricsPrecision.setStatus(_A)
_P2mpMetricsMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
p2mpMetricsMIBNotificationPrefix=_P2mpMetricsMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,181,1,2))
_P2mpMetricsMIBNotification_ObjectIdentity=ObjectIdentity
p2mpMetricsMIBNotification=_P2mpMetricsMIBNotification_ObjectIdentity((1,3,6,1,4,1,9,9,181,1,2,0))
_P2mpSuLinkMetricsGroup_ObjectIdentity=ObjectIdentity
p2mpSuLinkMetricsGroup=_P2mpSuLinkMetricsGroup_ObjectIdentity((1,3,6,1,4,1,9,9,181,2))
_P2mpSuLinkMetricsThreshTable_Object=MibTable
p2mpSuLinkMetricsThreshTable=_P2mpSuLinkMetricsThreshTable_Object((1,3,6,1,4,1,9,9,181,2,1))
if mibBuilder.loadTexts:p2mpSuLinkMetricsThreshTable.setStatus(_A)
_P2mpSuLinkMetricsThreshEntry_Object=MibTableRow
p2mpSuLinkMetricsThreshEntry=_P2mpSuLinkMetricsThreshEntry_Object((1,3,6,1,4,1,9,9,181,2,1,1))
p2mpSuLinkMetricsThreshEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:p2mpSuLinkMetricsThreshEntry.setStatus(_A)
_P2mpSuLinkESThresh_Type=Unsigned32
_P2mpSuLinkESThresh_Object=MibTableColumn
p2mpSuLinkESThresh=_P2mpSuLinkESThresh_Object((1,3,6,1,4,1,9,9,181,2,1,1,1),_P2mpSuLinkESThresh_Type())
p2mpSuLinkESThresh.setMaxAccess(_H)
if mibBuilder.loadTexts:p2mpSuLinkESThresh.setStatus(_A)
_P2mpSuLinkDSThresh_Type=CwrPercentageValue
_P2mpSuLinkDSThresh_Object=MibTableColumn
p2mpSuLinkDSThresh=_P2mpSuLinkDSThresh_Object((1,3,6,1,4,1,9,9,181,2,1,1,2),_P2mpSuLinkDSThresh_Type())
p2mpSuLinkDSThresh.setMaxAccess(_H)
if mibBuilder.loadTexts:p2mpSuLinkDSThresh.setStatus(_A)
if mibBuilder.loadTexts:p2mpSuLinkDSThresh.setUnits(_I)
_P2mpSuLinkSESThresh_Type=CwrPercentageValue
_P2mpSuLinkSESThresh_Object=MibTableColumn
p2mpSuLinkSESThresh=_P2mpSuLinkSESThresh_Object((1,3,6,1,4,1,9,9,181,2,1,1,3),_P2mpSuLinkSESThresh_Type())
p2mpSuLinkSESThresh.setMaxAccess(_H)
if mibBuilder.loadTexts:p2mpSuLinkSESThresh.setStatus(_A)
if mibBuilder.loadTexts:p2mpSuLinkSESThresh.setUnits(_I)
_P2mpSuLinkCSESThresh_Type=Unsigned32
_P2mpSuLinkCSESThresh_Object=MibTableColumn
p2mpSuLinkCSESThresh=_P2mpSuLinkCSESThresh_Object((1,3,6,1,4,1,9,9,181,2,1,1,4),_P2mpSuLinkCSESThresh_Type())
p2mpSuLinkCSESThresh.setMaxAccess(_H)
if mibBuilder.loadTexts:p2mpSuLinkCSESThresh.setStatus(_A)
_P2mpSuLink1HrESAlarmThresh_Type=Unsigned32
_P2mpSuLink1HrESAlarmThresh_Object=MibTableColumn
p2mpSuLink1HrESAlarmThresh=_P2mpSuLink1HrESAlarmThresh_Object((1,3,6,1,4,1,9,9,181,2,1,1,5),_P2mpSuLink1HrESAlarmThresh_Type())
p2mpSuLink1HrESAlarmThresh.setMaxAccess(_H)
if mibBuilder.loadTexts:p2mpSuLink1HrESAlarmThresh.setStatus(_A)
_P2mpSuLink1HrSESAlarmThresh_Type=Unsigned32
_P2mpSuLink1HrSESAlarmThresh_Object=MibTableColumn
p2mpSuLink1HrSESAlarmThresh=_P2mpSuLink1HrSESAlarmThresh_Object((1,3,6,1,4,1,9,9,181,2,1,1,6),_P2mpSuLink1HrSESAlarmThresh_Type())
p2mpSuLink1HrSESAlarmThresh.setMaxAccess(_H)
if mibBuilder.loadTexts:p2mpSuLink1HrSESAlarmThresh.setStatus(_A)
_P2mpSuLink1HrCSESAlarmThresh_Type=Unsigned32
_P2mpSuLink1HrCSESAlarmThresh_Object=MibTableColumn
p2mpSuLink1HrCSESAlarmThresh=_P2mpSuLink1HrCSESAlarmThresh_Object((1,3,6,1,4,1,9,9,181,2,1,1,7),_P2mpSuLink1HrCSESAlarmThresh_Type())
p2mpSuLink1HrCSESAlarmThresh.setMaxAccess(_H)
if mibBuilder.loadTexts:p2mpSuLink1HrCSESAlarmThresh.setStatus(_A)
_P2mpSuLink1HrDCSAlarmThresh_Type=Unsigned32
_P2mpSuLink1HrDCSAlarmThresh_Object=MibTableColumn
p2mpSuLink1HrDCSAlarmThresh=_P2mpSuLink1HrDCSAlarmThresh_Object((1,3,6,1,4,1,9,9,181,2,1,1,8),_P2mpSuLink1HrDCSAlarmThresh_Type())
p2mpSuLink1HrDCSAlarmThresh.setMaxAccess(_H)
if mibBuilder.loadTexts:p2mpSuLink1HrDCSAlarmThresh.setStatus(_A)
_P2mpSu1SecMetricsTable_Object=MibTable
p2mpSu1SecMetricsTable=_P2mpSu1SecMetricsTable_Object((1,3,6,1,4,1,9,9,181,2,2))
if mibBuilder.loadTexts:p2mpSu1SecMetricsTable.setStatus(_A)
_P2mpSu1SecMetricsEntry_Object=MibTableRow
p2mpSu1SecMetricsEntry=_P2mpSu1SecMetricsEntry_Object((1,3,6,1,4,1,9,9,181,2,2,1))
p2mpSu1SecMetricsEntry.setIndexNames((0,_E,_F),(0,_B,_T))
if mibBuilder.loadTexts:p2mpSu1SecMetricsEntry.setStatus(_A)
class _P2mpSu1SecIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_P2mpSu1SecIndex_Type.__name__=_G
_P2mpSu1SecIndex_Object=MibTableColumn
p2mpSu1SecIndex=_P2mpSu1SecIndex_Object((1,3,6,1,4,1,9,9,181,2,2,1,1),_P2mpSu1SecIndex_Type())
p2mpSu1SecIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:p2mpSu1SecIndex.setStatus(_A)
_P2mpSu1SecUpdateTime_Type=CwrUpdateTime
_P2mpSu1SecUpdateTime_Object=MibTableColumn
p2mpSu1SecUpdateTime=_P2mpSu1SecUpdateTime_Object((1,3,6,1,4,1,9,9,181,2,2,1,2),_P2mpSu1SecUpdateTime_Type())
p2mpSu1SecUpdateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSu1SecUpdateTime.setStatus(_A)
if mibBuilder.loadTexts:p2mpSu1SecUpdateTime.setUnits(_K)
class _P2mpSu1SecType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('unknown',0),('errorFree',1),('errored',2),('degraded',3),('sevErrored',4),('syncLoss',5)))
_P2mpSu1SecType_Type.__name__=_G
_P2mpSu1SecType_Object=MibTableColumn
p2mpSu1SecType=_P2mpSu1SecType_Object((1,3,6,1,4,1,9,9,181,2,2,1,3),_P2mpSu1SecType_Type())
p2mpSu1SecType.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSu1SecType.setStatus(_A)
_P2mpSu1SecTotalCodewords_Type=WirelessGauge64
_P2mpSu1SecTotalCodewords_Object=MibTableColumn
p2mpSu1SecTotalCodewords=_P2mpSu1SecTotalCodewords_Object((1,3,6,1,4,1,9,9,181,2,2,1,4),_P2mpSu1SecTotalCodewords_Type())
p2mpSu1SecTotalCodewords.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSu1SecTotalCodewords.setStatus(_A)
_P2mpSu1SecTotalErrCodewords_Type=WirelessGauge64
_P2mpSu1SecTotalErrCodewords_Object=MibTableColumn
p2mpSu1SecTotalErrCodewords=_P2mpSu1SecTotalErrCodewords_Object((1,3,6,1,4,1,9,9,181,2,2,1,5),_P2mpSu1SecTotalErrCodewords_Type())
p2mpSu1SecTotalErrCodewords.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSu1SecTotalErrCodewords.setStatus(_A)
_P2mpSu1SecValidDataPkt_Type=Counter32
_P2mpSu1SecValidDataPkt_Object=MibTableColumn
p2mpSu1SecValidDataPkt=_P2mpSu1SecValidDataPkt_Object((1,3,6,1,4,1,9,9,181,2,2,1,6),_P2mpSu1SecValidDataPkt_Type())
p2mpSu1SecValidDataPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSu1SecValidDataPkt.setStatus(_A)
_P2mpSu1MinMetricsTable_Object=MibTable
p2mpSu1MinMetricsTable=_P2mpSu1MinMetricsTable_Object((1,3,6,1,4,1,9,9,181,2,3))
if mibBuilder.loadTexts:p2mpSu1MinMetricsTable.setStatus(_A)
_P2mpSu1MinMetricsEntry_Object=MibTableRow
p2mpSu1MinMetricsEntry=_P2mpSu1MinMetricsEntry_Object((1,3,6,1,4,1,9,9,181,2,3,1))
p2mpSu1MinMetricsEntry.setIndexNames((0,_E,_F),(0,_B,_U))
if mibBuilder.loadTexts:p2mpSu1MinMetricsEntry.setStatus(_A)
class _P2mpSu1MinIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_P2mpSu1MinIndex_Type.__name__=_G
_P2mpSu1MinIndex_Object=MibTableColumn
p2mpSu1MinIndex=_P2mpSu1MinIndex_Object((1,3,6,1,4,1,9,9,181,2,3,1,1),_P2mpSu1MinIndex_Type())
p2mpSu1MinIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:p2mpSu1MinIndex.setStatus(_A)
_P2mpSu1MinUpdateTime_Type=CwrUpdateTime
_P2mpSu1MinUpdateTime_Object=MibTableColumn
p2mpSu1MinUpdateTime=_P2mpSu1MinUpdateTime_Object((1,3,6,1,4,1,9,9,181,2,3,1,2),_P2mpSu1MinUpdateTime_Type())
p2mpSu1MinUpdateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSu1MinUpdateTime.setStatus(_A)
if mibBuilder.loadTexts:p2mpSu1MinUpdateTime.setUnits(_K)
_P2mpSu1MinTotalCodewords_Type=WirelessGauge64
_P2mpSu1MinTotalCodewords_Object=MibTableColumn
p2mpSu1MinTotalCodewords=_P2mpSu1MinTotalCodewords_Object((1,3,6,1,4,1,9,9,181,2,3,1,3),_P2mpSu1MinTotalCodewords_Type())
p2mpSu1MinTotalCodewords.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSu1MinTotalCodewords.setStatus(_A)
_P2mpSu1MinTotalErrCodewords_Type=WirelessGauge64
_P2mpSu1MinTotalErrCodewords_Object=MibTableColumn
p2mpSu1MinTotalErrCodewords=_P2mpSu1MinTotalErrCodewords_Object((1,3,6,1,4,1,9,9,181,2,3,1,4),_P2mpSu1MinTotalErrCodewords_Type())
p2mpSu1MinTotalErrCodewords.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSu1MinTotalErrCodewords.setStatus(_A)
_P2mpSu1MinValidDataPkt_Type=Counter32
_P2mpSu1MinValidDataPkt_Object=MibTableColumn
p2mpSu1MinValidDataPkt=_P2mpSu1MinValidDataPkt_Object((1,3,6,1,4,1,9,9,181,2,3,1,5),_P2mpSu1MinValidDataPkt_Type())
p2mpSu1MinValidDataPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSu1MinValidDataPkt.setStatus(_A)
_P2mpSu1MinErrorFreeSeconds_Type=CwrCwErrorFreeSecond
_P2mpSu1MinErrorFreeSeconds_Object=MibTableColumn
p2mpSu1MinErrorFreeSeconds=_P2mpSu1MinErrorFreeSeconds_Object((1,3,6,1,4,1,9,9,181,2,3,1,6),_P2mpSu1MinErrorFreeSeconds_Type())
p2mpSu1MinErrorFreeSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSu1MinErrorFreeSeconds.setStatus(_A)
_P2mpSu1MinErroredSeconds_Type=CwrCwErroredSecond
_P2mpSu1MinErroredSeconds_Object=MibTableColumn
p2mpSu1MinErroredSeconds=_P2mpSu1MinErroredSeconds_Object((1,3,6,1,4,1,9,9,181,2,3,1,7),_P2mpSu1MinErroredSeconds_Type())
p2mpSu1MinErroredSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSu1MinErroredSeconds.setStatus(_A)
_P2mpSu1MinDegradedSeconds_Type=CwrCwDegradedSecond
_P2mpSu1MinDegradedSeconds_Object=MibTableColumn
p2mpSu1MinDegradedSeconds=_P2mpSu1MinDegradedSeconds_Object((1,3,6,1,4,1,9,9,181,2,3,1,8),_P2mpSu1MinDegradedSeconds_Type())
p2mpSu1MinDegradedSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSu1MinDegradedSeconds.setStatus(_A)
_P2mpSu1MinSevErroredSeconds_Type=CwrCwSeverelyErroredSecond
_P2mpSu1MinSevErroredSeconds_Object=MibTableColumn
p2mpSu1MinSevErroredSeconds=_P2mpSu1MinSevErroredSeconds_Object((1,3,6,1,4,1,9,9,181,2,3,1,9),_P2mpSu1MinSevErroredSeconds_Type())
p2mpSu1MinSevErroredSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSu1MinSevErroredSeconds.setStatus(_A)
_P2mpSu1MinConsecSevErrSeconds_Type=CwrCwConsecutiveSevErrSecond
_P2mpSu1MinConsecSevErrSeconds_Object=MibTableColumn
p2mpSu1MinConsecSevErrSeconds=_P2mpSu1MinConsecSevErrSeconds_Object((1,3,6,1,4,1,9,9,181,2,3,1,10),_P2mpSu1MinConsecSevErrSeconds_Type())
p2mpSu1MinConsecSevErrSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSu1MinConsecSevErrSeconds.setStatus(_A)
_P2mpSu1MinSyncLossSeconds_Type=Counter32
_P2mpSu1MinSyncLossSeconds_Object=MibTableColumn
p2mpSu1MinSyncLossSeconds=_P2mpSu1MinSyncLossSeconds_Object((1,3,6,1,4,1,9,9,181,2,3,1,11),_P2mpSu1MinSyncLossSeconds_Type())
p2mpSu1MinSyncLossSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSu1MinSyncLossSeconds.setStatus(_A)
_P2mpSu1MinTxPowerMax_Type=CwrFixedPointValue
_P2mpSu1MinTxPowerMax_Object=MibTableColumn
p2mpSu1MinTxPowerMax=_P2mpSu1MinTxPowerMax_Object((1,3,6,1,4,1,9,9,181,2,3,1,12),_P2mpSu1MinTxPowerMax_Type())
p2mpSu1MinTxPowerMax.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSu1MinTxPowerMax.setStatus(_A)
if mibBuilder.loadTexts:p2mpSu1MinTxPowerMax.setUnits(_D)
_P2mpSu1MinTxPowerMin_Type=CwrFixedPointValue
_P2mpSu1MinTxPowerMin_Object=MibTableColumn
p2mpSu1MinTxPowerMin=_P2mpSu1MinTxPowerMin_Object((1,3,6,1,4,1,9,9,181,2,3,1,13),_P2mpSu1MinTxPowerMin_Type())
p2mpSu1MinTxPowerMin.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSu1MinTxPowerMin.setStatus(_A)
if mibBuilder.loadTexts:p2mpSu1MinTxPowerMin.setUnits(_D)
_P2mpSu1MinTxPowerAvg_Type=CwrFixedPointValue
_P2mpSu1MinTxPowerAvg_Object=MibTableColumn
p2mpSu1MinTxPowerAvg=_P2mpSu1MinTxPowerAvg_Object((1,3,6,1,4,1,9,9,181,2,3,1,14),_P2mpSu1MinTxPowerAvg_Type())
p2mpSu1MinTxPowerAvg.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSu1MinTxPowerAvg.setStatus(_A)
if mibBuilder.loadTexts:p2mpSu1MinTxPowerAvg.setUnits(_D)
_P2mpSu1MinMainAntRxPowerMax_Type=CwrFixedPointValue
_P2mpSu1MinMainAntRxPowerMax_Object=MibTableColumn
p2mpSu1MinMainAntRxPowerMax=_P2mpSu1MinMainAntRxPowerMax_Object((1,3,6,1,4,1,9,9,181,2,3,1,15),_P2mpSu1MinMainAntRxPowerMax_Type())
p2mpSu1MinMainAntRxPowerMax.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSu1MinMainAntRxPowerMax.setStatus(_A)
if mibBuilder.loadTexts:p2mpSu1MinMainAntRxPowerMax.setUnits(_D)
_P2mpSu1MinMainAntRxPowerMin_Type=CwrFixedPointValue
_P2mpSu1MinMainAntRxPowerMin_Object=MibTableColumn
p2mpSu1MinMainAntRxPowerMin=_P2mpSu1MinMainAntRxPowerMin_Object((1,3,6,1,4,1,9,9,181,2,3,1,16),_P2mpSu1MinMainAntRxPowerMin_Type())
p2mpSu1MinMainAntRxPowerMin.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSu1MinMainAntRxPowerMin.setStatus(_A)
if mibBuilder.loadTexts:p2mpSu1MinMainAntRxPowerMin.setUnits(_D)
_P2mpSu1MinMainAntRxPowerAvg_Type=CwrFixedPointValue
_P2mpSu1MinMainAntRxPowerAvg_Object=MibTableColumn
p2mpSu1MinMainAntRxPowerAvg=_P2mpSu1MinMainAntRxPowerAvg_Object((1,3,6,1,4,1,9,9,181,2,3,1,17),_P2mpSu1MinMainAntRxPowerAvg_Type())
p2mpSu1MinMainAntRxPowerAvg.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSu1MinMainAntRxPowerAvg.setStatus(_A)
if mibBuilder.loadTexts:p2mpSu1MinMainAntRxPowerAvg.setUnits(_D)
_P2mpSu1MinDivAntRxPowerMax_Type=CwrFixedPointValue
_P2mpSu1MinDivAntRxPowerMax_Object=MibTableColumn
p2mpSu1MinDivAntRxPowerMax=_P2mpSu1MinDivAntRxPowerMax_Object((1,3,6,1,4,1,9,9,181,2,3,1,18),_P2mpSu1MinDivAntRxPowerMax_Type())
p2mpSu1MinDivAntRxPowerMax.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSu1MinDivAntRxPowerMax.setStatus(_A)
if mibBuilder.loadTexts:p2mpSu1MinDivAntRxPowerMax.setUnits(_D)
_P2mpSu1MinDivAntRxPowerMin_Type=CwrFixedPointValue
_P2mpSu1MinDivAntRxPowerMin_Object=MibTableColumn
p2mpSu1MinDivAntRxPowerMin=_P2mpSu1MinDivAntRxPowerMin_Object((1,3,6,1,4,1,9,9,181,2,3,1,19),_P2mpSu1MinDivAntRxPowerMin_Type())
p2mpSu1MinDivAntRxPowerMin.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSu1MinDivAntRxPowerMin.setStatus(_A)
if mibBuilder.loadTexts:p2mpSu1MinDivAntRxPowerMin.setUnits(_D)
_P2mpSu1MinDivAntRxPowerAvg_Type=CwrFixedPointValue
_P2mpSu1MinDivAntRxPowerAvg_Object=MibTableColumn
p2mpSu1MinDivAntRxPowerAvg=_P2mpSu1MinDivAntRxPowerAvg_Object((1,3,6,1,4,1,9,9,181,2,3,1,20),_P2mpSu1MinDivAntRxPowerAvg_Type())
p2mpSu1MinDivAntRxPowerAvg.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSu1MinDivAntRxPowerAvg.setStatus(_A)
if mibBuilder.loadTexts:p2mpSu1MinDivAntRxPowerAvg.setUnits(_D)
_P2mpSu1HrMetricsTable_Object=MibTable
p2mpSu1HrMetricsTable=_P2mpSu1HrMetricsTable_Object((1,3,6,1,4,1,9,9,181,2,4))
if mibBuilder.loadTexts:p2mpSu1HrMetricsTable.setStatus(_A)
_P2mpSu1HrMetricsEntry_Object=MibTableRow
p2mpSu1HrMetricsEntry=_P2mpSu1HrMetricsEntry_Object((1,3,6,1,4,1,9,9,181,2,4,1))
p2mpSu1HrMetricsEntry.setIndexNames((0,_E,_F),(0,_B,_V))
if mibBuilder.loadTexts:p2mpSu1HrMetricsEntry.setStatus(_A)
class _P2mpSu1HrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_P2mpSu1HrIndex_Type.__name__=_G
_P2mpSu1HrIndex_Object=MibTableColumn
p2mpSu1HrIndex=_P2mpSu1HrIndex_Object((1,3,6,1,4,1,9,9,181,2,4,1,1),_P2mpSu1HrIndex_Type())
p2mpSu1HrIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:p2mpSu1HrIndex.setStatus(_A)
_P2mpSu1HrUpdateTime_Type=CwrUpdateTime
_P2mpSu1HrUpdateTime_Object=MibTableColumn
p2mpSu1HrUpdateTime=_P2mpSu1HrUpdateTime_Object((1,3,6,1,4,1,9,9,181,2,4,1,2),_P2mpSu1HrUpdateTime_Type())
p2mpSu1HrUpdateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSu1HrUpdateTime.setStatus(_A)
if mibBuilder.loadTexts:p2mpSu1HrUpdateTime.setUnits(_K)
_P2mpSu1HrTotalCodewords_Type=WirelessGauge64
_P2mpSu1HrTotalCodewords_Object=MibTableColumn
p2mpSu1HrTotalCodewords=_P2mpSu1HrTotalCodewords_Object((1,3,6,1,4,1,9,9,181,2,4,1,3),_P2mpSu1HrTotalCodewords_Type())
p2mpSu1HrTotalCodewords.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSu1HrTotalCodewords.setStatus(_A)
_P2mpSu1HrTotalErrCodewords_Type=WirelessGauge64
_P2mpSu1HrTotalErrCodewords_Object=MibTableColumn
p2mpSu1HrTotalErrCodewords=_P2mpSu1HrTotalErrCodewords_Object((1,3,6,1,4,1,9,9,181,2,4,1,4),_P2mpSu1HrTotalErrCodewords_Type())
p2mpSu1HrTotalErrCodewords.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSu1HrTotalErrCodewords.setStatus(_A)
_P2mpSu1HrValidDataPkt_Type=Counter32
_P2mpSu1HrValidDataPkt_Object=MibTableColumn
p2mpSu1HrValidDataPkt=_P2mpSu1HrValidDataPkt_Object((1,3,6,1,4,1,9,9,181,2,4,1,5),_P2mpSu1HrValidDataPkt_Type())
p2mpSu1HrValidDataPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSu1HrValidDataPkt.setStatus(_A)
_P2mpSu1HrErrorFreeSeconds_Type=CwrCwErrorFreeSecond
_P2mpSu1HrErrorFreeSeconds_Object=MibTableColumn
p2mpSu1HrErrorFreeSeconds=_P2mpSu1HrErrorFreeSeconds_Object((1,3,6,1,4,1,9,9,181,2,4,1,6),_P2mpSu1HrErrorFreeSeconds_Type())
p2mpSu1HrErrorFreeSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSu1HrErrorFreeSeconds.setStatus(_A)
_P2mpSu1HrErroredSeconds_Type=CwrCwErroredSecond
_P2mpSu1HrErroredSeconds_Object=MibTableColumn
p2mpSu1HrErroredSeconds=_P2mpSu1HrErroredSeconds_Object((1,3,6,1,4,1,9,9,181,2,4,1,7),_P2mpSu1HrErroredSeconds_Type())
p2mpSu1HrErroredSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSu1HrErroredSeconds.setStatus(_A)
_P2mpSu1HrSevErroredSeconds_Type=CwrCwSeverelyErroredSecond
_P2mpSu1HrSevErroredSeconds_Object=MibTableColumn
p2mpSu1HrSevErroredSeconds=_P2mpSu1HrSevErroredSeconds_Object((1,3,6,1,4,1,9,9,181,2,4,1,8),_P2mpSu1HrSevErroredSeconds_Type())
p2mpSu1HrSevErroredSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSu1HrSevErroredSeconds.setStatus(_A)
_P2mpSu1HrConsecSvErrSeconds_Type=CwrCwConsecutiveSevErrSecond
_P2mpSu1HrConsecSvErrSeconds_Object=MibTableColumn
p2mpSu1HrConsecSvErrSeconds=_P2mpSu1HrConsecSvErrSeconds_Object((1,3,6,1,4,1,9,9,181,2,4,1,9),_P2mpSu1HrConsecSvErrSeconds_Type())
p2mpSu1HrConsecSvErrSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSu1HrConsecSvErrSeconds.setStatus(_A)
_P2mpSu1HrSyncLossSeconds_Type=Counter32
_P2mpSu1HrSyncLossSeconds_Object=MibTableColumn
p2mpSu1HrSyncLossSeconds=_P2mpSu1HrSyncLossSeconds_Object((1,3,6,1,4,1,9,9,181,2,4,1,10),_P2mpSu1HrSyncLossSeconds_Type())
p2mpSu1HrSyncLossSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSu1HrSyncLossSeconds.setStatus(_A)
_P2mpSu1HrDegradedSeconds_Type=CwrCwDegradedSecond
_P2mpSu1HrDegradedSeconds_Object=MibTableColumn
p2mpSu1HrDegradedSeconds=_P2mpSu1HrDegradedSeconds_Object((1,3,6,1,4,1,9,9,181,2,4,1,11),_P2mpSu1HrDegradedSeconds_Type())
p2mpSu1HrDegradedSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSu1HrDegradedSeconds.setStatus(_A)
_P2mpSu1HrTxPowerMax_Type=CwrFixedPointValue
_P2mpSu1HrTxPowerMax_Object=MibTableColumn
p2mpSu1HrTxPowerMax=_P2mpSu1HrTxPowerMax_Object((1,3,6,1,4,1,9,9,181,2,4,1,12),_P2mpSu1HrTxPowerMax_Type())
p2mpSu1HrTxPowerMax.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSu1HrTxPowerMax.setStatus(_A)
if mibBuilder.loadTexts:p2mpSu1HrTxPowerMax.setUnits(_D)
_P2mpSu1HrTxPowerMin_Type=CwrFixedPointValue
_P2mpSu1HrTxPowerMin_Object=MibTableColumn
p2mpSu1HrTxPowerMin=_P2mpSu1HrTxPowerMin_Object((1,3,6,1,4,1,9,9,181,2,4,1,13),_P2mpSu1HrTxPowerMin_Type())
p2mpSu1HrTxPowerMin.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSu1HrTxPowerMin.setStatus(_A)
if mibBuilder.loadTexts:p2mpSu1HrTxPowerMin.setUnits(_D)
_P2mpSu1HrTxPowerAvg_Type=CwrFixedPointValue
_P2mpSu1HrTxPowerAvg_Object=MibTableColumn
p2mpSu1HrTxPowerAvg=_P2mpSu1HrTxPowerAvg_Object((1,3,6,1,4,1,9,9,181,2,4,1,14),_P2mpSu1HrTxPowerAvg_Type())
p2mpSu1HrTxPowerAvg.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSu1HrTxPowerAvg.setStatus(_A)
if mibBuilder.loadTexts:p2mpSu1HrTxPowerAvg.setUnits(_D)
_P2mpSu1HrMainAntRxPowerMax_Type=CwrFixedPointValue
_P2mpSu1HrMainAntRxPowerMax_Object=MibTableColumn
p2mpSu1HrMainAntRxPowerMax=_P2mpSu1HrMainAntRxPowerMax_Object((1,3,6,1,4,1,9,9,181,2,4,1,15),_P2mpSu1HrMainAntRxPowerMax_Type())
p2mpSu1HrMainAntRxPowerMax.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSu1HrMainAntRxPowerMax.setStatus(_A)
if mibBuilder.loadTexts:p2mpSu1HrMainAntRxPowerMax.setUnits(_D)
_P2mpSu1HrMainAntRxPowerMin_Type=CwrFixedPointValue
_P2mpSu1HrMainAntRxPowerMin_Object=MibTableColumn
p2mpSu1HrMainAntRxPowerMin=_P2mpSu1HrMainAntRxPowerMin_Object((1,3,6,1,4,1,9,9,181,2,4,1,16),_P2mpSu1HrMainAntRxPowerMin_Type())
p2mpSu1HrMainAntRxPowerMin.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSu1HrMainAntRxPowerMin.setStatus(_A)
if mibBuilder.loadTexts:p2mpSu1HrMainAntRxPowerMin.setUnits(_D)
_P2mpSu1HrMainAntRxPowerAvg_Type=CwrFixedPointValue
_P2mpSu1HrMainAntRxPowerAvg_Object=MibTableColumn
p2mpSu1HrMainAntRxPowerAvg=_P2mpSu1HrMainAntRxPowerAvg_Object((1,3,6,1,4,1,9,9,181,2,4,1,17),_P2mpSu1HrMainAntRxPowerAvg_Type())
p2mpSu1HrMainAntRxPowerAvg.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSu1HrMainAntRxPowerAvg.setStatus(_A)
if mibBuilder.loadTexts:p2mpSu1HrMainAntRxPowerAvg.setUnits(_D)
_P2mpSu1HrDivAntRxPowerMax_Type=CwrFixedPointValue
_P2mpSu1HrDivAntRxPowerMax_Object=MibTableColumn
p2mpSu1HrDivAntRxPowerMax=_P2mpSu1HrDivAntRxPowerMax_Object((1,3,6,1,4,1,9,9,181,2,4,1,18),_P2mpSu1HrDivAntRxPowerMax_Type())
p2mpSu1HrDivAntRxPowerMax.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSu1HrDivAntRxPowerMax.setStatus(_A)
if mibBuilder.loadTexts:p2mpSu1HrDivAntRxPowerMax.setUnits(_D)
_P2mpSu1HrDivAntRxPowerMin_Type=CwrFixedPointValue
_P2mpSu1HrDivAntRxPowerMin_Object=MibTableColumn
p2mpSu1HrDivAntRxPowerMin=_P2mpSu1HrDivAntRxPowerMin_Object((1,3,6,1,4,1,9,9,181,2,4,1,19),_P2mpSu1HrDivAntRxPowerMin_Type())
p2mpSu1HrDivAntRxPowerMin.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSu1HrDivAntRxPowerMin.setStatus(_A)
if mibBuilder.loadTexts:p2mpSu1HrDivAntRxPowerMin.setUnits(_D)
_P2mpSu1HrDivAntRxPowerAvg_Type=CwrFixedPointValue
_P2mpSu1HrDivAntRxPowerAvg_Object=MibTableColumn
p2mpSu1HrDivAntRxPowerAvg=_P2mpSu1HrDivAntRxPowerAvg_Object((1,3,6,1,4,1,9,9,181,2,4,1,20),_P2mpSu1HrDivAntRxPowerAvg_Type())
p2mpSu1HrDivAntRxPowerAvg.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSu1HrDivAntRxPowerAvg.setStatus(_A)
if mibBuilder.loadTexts:p2mpSu1HrDivAntRxPowerAvg.setUnits(_D)
_P2mpSuCumulativeLinkMetricsTable_Object=MibTable
p2mpSuCumulativeLinkMetricsTable=_P2mpSuCumulativeLinkMetricsTable_Object((1,3,6,1,4,1,9,9,181,2,6))
if mibBuilder.loadTexts:p2mpSuCumulativeLinkMetricsTable.setStatus(_A)
_P2mpSuCumulativeLinkMetricsEntry_Object=MibTableRow
p2mpSuCumulativeLinkMetricsEntry=_P2mpSuCumulativeLinkMetricsEntry_Object((1,3,6,1,4,1,9,9,181,2,6,1))
p2mpSuCumulativeLinkMetricsEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:p2mpSuCumulativeLinkMetricsEntry.setStatus(_A)
_P2mpSuAvailableSeconds_Type=Counter32
_P2mpSuAvailableSeconds_Object=MibTableColumn
p2mpSuAvailableSeconds=_P2mpSuAvailableSeconds_Object((1,3,6,1,4,1,9,9,181,2,6,1,1),_P2mpSuAvailableSeconds_Type())
p2mpSuAvailableSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSuAvailableSeconds.setStatus(_A)
_P2mpSuUnAvailableSeconds_Type=Counter32
_P2mpSuUnAvailableSeconds_Object=MibTableColumn
p2mpSuUnAvailableSeconds=_P2mpSuUnAvailableSeconds_Object((1,3,6,1,4,1,9,9,181,2,6,1,2),_P2mpSuUnAvailableSeconds_Type())
p2mpSuUnAvailableSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSuUnAvailableSeconds.setStatus(_A)
_P2mpSuPctAvailSeconds_Type=CwrPercentageValue
_P2mpSuPctAvailSeconds_Object=MibTableColumn
p2mpSuPctAvailSeconds=_P2mpSuPctAvailSeconds_Object((1,3,6,1,4,1,9,9,181,2,6,1,3),_P2mpSuPctAvailSeconds_Type())
p2mpSuPctAvailSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSuPctAvailSeconds.setStatus(_A)
if mibBuilder.loadTexts:p2mpSuPctAvailSeconds.setUnits(_I)
_P2mpSuSyncLossSeconds_Type=Counter32
_P2mpSuSyncLossSeconds_Object=MibTableColumn
p2mpSuSyncLossSeconds=_P2mpSuSyncLossSeconds_Object((1,3,6,1,4,1,9,9,181,2,6,1,4),_P2mpSuSyncLossSeconds_Type())
p2mpSuSyncLossSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSuSyncLossSeconds.setStatus(_A)
_P2mpSuPctErrorFreeSeconds_Type=CwrPercentageValue
_P2mpSuPctErrorFreeSeconds_Object=MibTableColumn
p2mpSuPctErrorFreeSeconds=_P2mpSuPctErrorFreeSeconds_Object((1,3,6,1,4,1,9,9,181,2,6,1,5),_P2mpSuPctErrorFreeSeconds_Type())
p2mpSuPctErrorFreeSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSuPctErrorFreeSeconds.setStatus(_A)
if mibBuilder.loadTexts:p2mpSuPctErrorFreeSeconds.setUnits(_I)
_P2mpSuPctErroredSeconds_Type=CwrPercentageValue
_P2mpSuPctErroredSeconds_Object=MibTableColumn
p2mpSuPctErroredSeconds=_P2mpSuPctErroredSeconds_Object((1,3,6,1,4,1,9,9,181,2,6,1,6),_P2mpSuPctErroredSeconds_Type())
p2mpSuPctErroredSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSuPctErroredSeconds.setStatus(_A)
if mibBuilder.loadTexts:p2mpSuPctErroredSeconds.setUnits(_I)
_P2mpSuPctSevErroredSeconds_Type=CwrPercentageValue
_P2mpSuPctSevErroredSeconds_Object=MibTableColumn
p2mpSuPctSevErroredSeconds=_P2mpSuPctSevErroredSeconds_Object((1,3,6,1,4,1,9,9,181,2,6,1,7),_P2mpSuPctSevErroredSeconds_Type())
p2mpSuPctSevErroredSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSuPctSevErroredSeconds.setStatus(_A)
if mibBuilder.loadTexts:p2mpSuPctSevErroredSeconds.setUnits(_I)
_P2mpSuPctDegradedSeconds_Type=CwrPercentageValue
_P2mpSuPctDegradedSeconds_Object=MibTableColumn
p2mpSuPctDegradedSeconds=_P2mpSuPctDegradedSeconds_Object((1,3,6,1,4,1,9,9,181,2,6,1,8),_P2mpSuPctDegradedSeconds_Type())
p2mpSuPctDegradedSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSuPctDegradedSeconds.setStatus(_A)
if mibBuilder.loadTexts:p2mpSuPctDegradedSeconds.setUnits(_I)
_P2mpSuInitialSyncSeconds_Type=Counter32
_P2mpSuInitialSyncSeconds_Object=MibTableColumn
p2mpSuInitialSyncSeconds=_P2mpSuInitialSyncSeconds_Object((1,3,6,1,4,1,9,9,181,2,6,1,9),_P2mpSuInitialSyncSeconds_Type())
p2mpSuInitialSyncSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSuInitialSyncSeconds.setStatus(_A)
_P2mpSuSyncSuccessCount_Type=Counter32
_P2mpSuSyncSuccessCount_Object=MibTableColumn
p2mpSuSyncSuccessCount=_P2mpSuSyncSuccessCount_Object((1,3,6,1,4,1,9,9,181,2,6,1,10),_P2mpSuSyncSuccessCount_Type())
p2mpSuSyncSuccessCount.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSuSyncSuccessCount.setStatus(_A)
_P2mpSuLastSyncSuccessTime_Type=TimeInterval
_P2mpSuLastSyncSuccessTime_Object=MibTableColumn
p2mpSuLastSyncSuccessTime=_P2mpSuLastSyncSuccessTime_Object((1,3,6,1,4,1,9,9,181,2,6,1,11),_P2mpSuLastSyncSuccessTime_Type())
p2mpSuLastSyncSuccessTime.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSuLastSyncSuccessTime.setStatus(_A)
_P2mpSuSyncFailureCount_Type=Counter32
_P2mpSuSyncFailureCount_Object=MibTableColumn
p2mpSuSyncFailureCount=_P2mpSuSyncFailureCount_Object((1,3,6,1,4,1,9,9,181,2,6,1,12),_P2mpSuSyncFailureCount_Type())
p2mpSuSyncFailureCount.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSuSyncFailureCount.setStatus(_A)
_P2mpSuLastSyncFailTime_Type=TimeInterval
_P2mpSuLastSyncFailTime_Object=MibTableColumn
p2mpSuLastSyncFailTime=_P2mpSuLastSyncFailTime_Object((1,3,6,1,4,1,9,9,181,2,6,1,13),_P2mpSuLastSyncFailTime_Type())
p2mpSuLastSyncFailTime.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSuLastSyncFailTime.setStatus(_A)
_P2mpSuSyncMedEffort_Type=Counter32
_P2mpSuSyncMedEffort_Object=MibTableColumn
p2mpSuSyncMedEffort=_P2mpSuSyncMedEffort_Object((1,3,6,1,4,1,9,9,181,2,6,1,14),_P2mpSuSyncMedEffort_Type())
p2mpSuSyncMedEffort.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSuSyncMedEffort.setStatus(_A)
_P2mpSuSyncHighEffort_Type=Counter32
_P2mpSuSyncHighEffort_Object=MibTableColumn
p2mpSuSyncHighEffort=_P2mpSuSyncHighEffort_Object((1,3,6,1,4,1,9,9,181,2,6,1,15),_P2mpSuSyncHighEffort_Type())
p2mpSuSyncHighEffort.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSuSyncHighEffort.setStatus(_A)
_P2mpSuEffectiveDataRate_Type=Gauge32
_P2mpSuEffectiveDataRate_Object=MibTableColumn
p2mpSuEffectiveDataRate=_P2mpSuEffectiveDataRate_Object((1,3,6,1,4,1,9,9,181,2,6,1,16),_P2mpSuEffectiveDataRate_Type())
p2mpSuEffectiveDataRate.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSuEffectiveDataRate.setStatus(_A)
_P2mpSuPercentEfficiency_Type=CwrPercentageValue
_P2mpSuPercentEfficiency_Object=MibTableColumn
p2mpSuPercentEfficiency=_P2mpSuPercentEfficiency_Object((1,3,6,1,4,1,9,9,181,2,6,1,17),_P2mpSuPercentEfficiency_Type())
p2mpSuPercentEfficiency.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSuPercentEfficiency.setStatus(_A)
if mibBuilder.loadTexts:p2mpSuPercentEfficiency.setUnits(_I)
_P2mpHeLinkMetricsGroup_ObjectIdentity=ObjectIdentity
p2mpHeLinkMetricsGroup=_P2mpHeLinkMetricsGroup_ObjectIdentity((1,3,6,1,4,1,9,9,181,3))
_P2mpHeLinkMetricsThreshTable_Object=MibTable
p2mpHeLinkMetricsThreshTable=_P2mpHeLinkMetricsThreshTable_Object((1,3,6,1,4,1,9,9,181,3,1))
if mibBuilder.loadTexts:p2mpHeLinkMetricsThreshTable.setStatus(_A)
_P2mpHeLinkMetricsThreshEntry_Object=MibTableRow
p2mpHeLinkMetricsThreshEntry=_P2mpHeLinkMetricsThreshEntry_Object((1,3,6,1,4,1,9,9,181,3,1,1))
p2mpHeLinkMetricsThreshEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:p2mpHeLinkMetricsThreshEntry.setStatus(_A)
_P2mpHe1HrMinTotalCWThresh_Type=Unsigned32
_P2mpHe1HrMinTotalCWThresh_Object=MibTableColumn
p2mpHe1HrMinTotalCWThresh=_P2mpHe1HrMinTotalCWThresh_Object((1,3,6,1,4,1,9,9,181,3,1,1,1),_P2mpHe1HrMinTotalCWThresh_Type())
p2mpHe1HrMinTotalCWThresh.setMaxAccess(_H)
if mibBuilder.loadTexts:p2mpHe1HrMinTotalCWThresh.setStatus(_A)
_P2mpHe1HrPctErrCWThresh_Type=CwrPercentageValue
_P2mpHe1HrPctErrCWThresh_Object=MibTableColumn
p2mpHe1HrPctErrCWThresh=_P2mpHe1HrPctErrCWThresh_Object((1,3,6,1,4,1,9,9,181,3,1,1,2),_P2mpHe1HrPctErrCWThresh_Type())
p2mpHe1HrPctErrCWThresh.setMaxAccess(_H)
if mibBuilder.loadTexts:p2mpHe1HrPctErrCWThresh.setStatus(_A)
if mibBuilder.loadTexts:p2mpHe1HrPctErrCWThresh.setUnits(_I)
_P2mpHeBadSuTable_Object=MibTable
p2mpHeBadSuTable=_P2mpHeBadSuTable_Object((1,3,6,1,4,1,9,9,181,3,2))
if mibBuilder.loadTexts:p2mpHeBadSuTable.setStatus(_A)
_P2mpHeBadSuEntry_Object=MibTableRow
p2mpHeBadSuEntry=_P2mpHeBadSuEntry_Object((1,3,6,1,4,1,9,9,181,3,2,1))
p2mpHeBadSuEntry.setIndexNames((0,_E,_F),(0,_B,_W))
if mibBuilder.loadTexts:p2mpHeBadSuEntry.setStatus(_A)
class _P2mpBadSuIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_P2mpBadSuIndex_Type.__name__=_G
_P2mpBadSuIndex_Object=MibTableColumn
p2mpBadSuIndex=_P2mpBadSuIndex_Object((1,3,6,1,4,1,9,9,181,3,2,1,1),_P2mpBadSuIndex_Type())
p2mpBadSuIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:p2mpBadSuIndex.setStatus(_A)
_P2mpBadSuUpdateTime_Type=CwrUpdateTime
_P2mpBadSuUpdateTime_Object=MibTableColumn
p2mpBadSuUpdateTime=_P2mpBadSuUpdateTime_Object((1,3,6,1,4,1,9,9,181,3,2,1,2),_P2mpBadSuUpdateTime_Type())
p2mpBadSuUpdateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpBadSuUpdateTime.setStatus(_A)
if mibBuilder.loadTexts:p2mpBadSuUpdateTime.setUnits(_K)
_P2mpBadSuMacAddress_Type=MacAddress
_P2mpBadSuMacAddress_Object=MibTableColumn
p2mpBadSuMacAddress=_P2mpBadSuMacAddress_Object((1,3,6,1,4,1,9,9,181,3,2,1,3),_P2mpBadSuMacAddress_Type())
p2mpBadSuMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpBadSuMacAddress.setStatus(_A)
_P2mpTotalErroredCodewords_Type=Unsigned32
_P2mpTotalErroredCodewords_Object=MibTableColumn
p2mpTotalErroredCodewords=_P2mpTotalErroredCodewords_Object((1,3,6,1,4,1,9,9,181,3,2,1,4),_P2mpTotalErroredCodewords_Type())
p2mpTotalErroredCodewords.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpTotalErroredCodewords.setStatus(_A)
_P2mpPctErroredCodewords_Type=Unsigned32
_P2mpPctErroredCodewords_Object=MibTableColumn
p2mpPctErroredCodewords=_P2mpPctErroredCodewords_Object((1,3,6,1,4,1,9,9,181,3,2,1,5),_P2mpPctErroredCodewords_Type())
p2mpPctErroredCodewords.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpPctErroredCodewords.setStatus(_A)
_P2mpHeCodewordErrorTable_Object=MibTable
p2mpHeCodewordErrorTable=_P2mpHeCodewordErrorTable_Object((1,3,6,1,4,1,9,9,181,3,3))
if mibBuilder.loadTexts:p2mpHeCodewordErrorTable.setStatus(_A)
_P2mpHeCodewordErrorEntry_Object=MibTableRow
p2mpHeCodewordErrorEntry=_P2mpHeCodewordErrorEntry_Object((1,3,6,1,4,1,9,9,181,3,3,1))
p2mpHeCodewordErrorEntry.setIndexNames((0,_E,_F),(0,_B,_X),(0,_B,_Y))
if mibBuilder.loadTexts:p2mpHeCodewordErrorEntry.setStatus(_A)
_P2mpSuMacAddress_Type=MacAddress
_P2mpSuMacAddress_Object=MibTableColumn
p2mpSuMacAddress=_P2mpSuMacAddress_Object((1,3,6,1,4,1,9,9,181,3,3,1,1),_P2mpSuMacAddress_Type())
p2mpSuMacAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:p2mpSuMacAddress.setStatus(_A)
class _P2mpHeCWErrorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_P2mpHeCWErrorIndex_Type.__name__=_G
_P2mpHeCWErrorIndex_Object=MibTableColumn
p2mpHeCWErrorIndex=_P2mpHeCWErrorIndex_Object((1,3,6,1,4,1,9,9,181,3,3,1,2),_P2mpHeCWErrorIndex_Type())
p2mpHeCWErrorIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:p2mpHeCWErrorIndex.setStatus(_A)
_P2mpHeCWErrorUpdateTime_Type=CwrUpdateTime
_P2mpHeCWErrorUpdateTime_Object=MibTableColumn
p2mpHeCWErrorUpdateTime=_P2mpHeCWErrorUpdateTime_Object((1,3,6,1,4,1,9,9,181,3,3,1,3),_P2mpHeCWErrorUpdateTime_Type())
p2mpHeCWErrorUpdateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpHeCWErrorUpdateTime.setStatus(_A)
if mibBuilder.loadTexts:p2mpHeCWErrorUpdateTime.setUnits(_K)
_P2mpTotalCodewords_Type=WirelessGauge64
_P2mpTotalCodewords_Object=MibTableColumn
p2mpTotalCodewords=_P2mpTotalCodewords_Object((1,3,6,1,4,1,9,9,181,3,3,1,4),_P2mpTotalCodewords_Type())
p2mpTotalCodewords.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpTotalCodewords.setStatus(_A)
_P2mpErroredCodewords_Type=WirelessGauge64
_P2mpErroredCodewords_Object=MibTableColumn
p2mpErroredCodewords=_P2mpErroredCodewords_Object((1,3,6,1,4,1,9,9,181,3,3,1,5),_P2mpErroredCodewords_Type())
p2mpErroredCodewords.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpErroredCodewords.setStatus(_A)
_P2mpSINR_Type=CwrFixedPointValue
_P2mpSINR_Object=MibTableColumn
p2mpSINR=_P2mpSINR_Object((1,3,6,1,4,1,9,9,181,3,3,1,6),_P2mpSINR_Type())
p2mpSINR.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSINR.setStatus(_A)
_P2mpHe1SecMetricsTable_Object=MibTable
p2mpHe1SecMetricsTable=_P2mpHe1SecMetricsTable_Object((1,3,6,1,4,1,9,9,181,3,4))
if mibBuilder.loadTexts:p2mpHe1SecMetricsTable.setStatus(_A)
_P2mpHe1SecMetricsEntry_Object=MibTableRow
p2mpHe1SecMetricsEntry=_P2mpHe1SecMetricsEntry_Object((1,3,6,1,4,1,9,9,181,3,4,1))
p2mpHe1SecMetricsEntry.setIndexNames((0,_E,_F),(0,_B,_Z))
if mibBuilder.loadTexts:p2mpHe1SecMetricsEntry.setStatus(_A)
class _P2mpHe1SecIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_P2mpHe1SecIndex_Type.__name__=_G
_P2mpHe1SecIndex_Object=MibTableColumn
p2mpHe1SecIndex=_P2mpHe1SecIndex_Object((1,3,6,1,4,1,9,9,181,3,4,1,1),_P2mpHe1SecIndex_Type())
p2mpHe1SecIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:p2mpHe1SecIndex.setStatus(_A)
_P2mpHe1SecUpdateTime_Type=CwrUpdateTime
_P2mpHe1SecUpdateTime_Object=MibTableColumn
p2mpHe1SecUpdateTime=_P2mpHe1SecUpdateTime_Object((1,3,6,1,4,1,9,9,181,3,4,1,2),_P2mpHe1SecUpdateTime_Type())
p2mpHe1SecUpdateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpHe1SecUpdateTime.setStatus(_A)
if mibBuilder.loadTexts:p2mpHe1SecUpdateTime.setUnits(_K)
_P2mpHe1SecTotalCodewords_Type=WirelessGauge64
_P2mpHe1SecTotalCodewords_Object=MibTableColumn
p2mpHe1SecTotalCodewords=_P2mpHe1SecTotalCodewords_Object((1,3,6,1,4,1,9,9,181,3,4,1,3),_P2mpHe1SecTotalCodewords_Type())
p2mpHe1SecTotalCodewords.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpHe1SecTotalCodewords.setStatus(_A)
_P2mpHe1SecErroredCodewords_Type=WirelessGauge64
_P2mpHe1SecErroredCodewords_Object=MibTableColumn
p2mpHe1SecErroredCodewords=_P2mpHe1SecErroredCodewords_Object((1,3,6,1,4,1,9,9,181,3,4,1,4),_P2mpHe1SecErroredCodewords_Type())
p2mpHe1SecErroredCodewords.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpHe1SecErroredCodewords.setStatus(_A)
_P2mpHe1MinMetricsTable_Object=MibTable
p2mpHe1MinMetricsTable=_P2mpHe1MinMetricsTable_Object((1,3,6,1,4,1,9,9,181,3,5))
if mibBuilder.loadTexts:p2mpHe1MinMetricsTable.setStatus(_A)
_P2mpHe1MinMetricsEntry_Object=MibTableRow
p2mpHe1MinMetricsEntry=_P2mpHe1MinMetricsEntry_Object((1,3,6,1,4,1,9,9,181,3,5,1))
p2mpHe1MinMetricsEntry.setIndexNames((0,_E,_F),(0,_B,_a))
if mibBuilder.loadTexts:p2mpHe1MinMetricsEntry.setStatus(_A)
class _P2mpHe1MinIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_P2mpHe1MinIndex_Type.__name__=_G
_P2mpHe1MinIndex_Object=MibTableColumn
p2mpHe1MinIndex=_P2mpHe1MinIndex_Object((1,3,6,1,4,1,9,9,181,3,5,1,1),_P2mpHe1MinIndex_Type())
p2mpHe1MinIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:p2mpHe1MinIndex.setStatus(_A)
_P2mpHe1MinUpdateTime_Type=CwrUpdateTime
_P2mpHe1MinUpdateTime_Object=MibTableColumn
p2mpHe1MinUpdateTime=_P2mpHe1MinUpdateTime_Object((1,3,6,1,4,1,9,9,181,3,5,1,2),_P2mpHe1MinUpdateTime_Type())
p2mpHe1MinUpdateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpHe1MinUpdateTime.setStatus(_A)
if mibBuilder.loadTexts:p2mpHe1MinUpdateTime.setUnits(_K)
_P2mpHe1MinTotalCodewords_Type=WirelessGauge64
_P2mpHe1MinTotalCodewords_Object=MibTableColumn
p2mpHe1MinTotalCodewords=_P2mpHe1MinTotalCodewords_Object((1,3,6,1,4,1,9,9,181,3,5,1,3),_P2mpHe1MinTotalCodewords_Type())
p2mpHe1MinTotalCodewords.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpHe1MinTotalCodewords.setStatus(_A)
_P2mpHe1MinErroredCodewords_Type=WirelessGauge64
_P2mpHe1MinErroredCodewords_Object=MibTableColumn
p2mpHe1MinErroredCodewords=_P2mpHe1MinErroredCodewords_Object((1,3,6,1,4,1,9,9,181,3,5,1,4),_P2mpHe1MinErroredCodewords_Type())
p2mpHe1MinErroredCodewords.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpHe1MinErroredCodewords.setStatus(_A)
_P2mpHe1HrMetricsTable_Object=MibTable
p2mpHe1HrMetricsTable=_P2mpHe1HrMetricsTable_Object((1,3,6,1,4,1,9,9,181,3,6))
if mibBuilder.loadTexts:p2mpHe1HrMetricsTable.setStatus(_A)
_P2mpHe1HrMetricsEntry_Object=MibTableRow
p2mpHe1HrMetricsEntry=_P2mpHe1HrMetricsEntry_Object((1,3,6,1,4,1,9,9,181,3,6,1))
p2mpHe1HrMetricsEntry.setIndexNames((0,_E,_F),(0,_B,_b))
if mibBuilder.loadTexts:p2mpHe1HrMetricsEntry.setStatus(_A)
class _P2mpHe1HrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_P2mpHe1HrIndex_Type.__name__=_G
_P2mpHe1HrIndex_Object=MibTableColumn
p2mpHe1HrIndex=_P2mpHe1HrIndex_Object((1,3,6,1,4,1,9,9,181,3,6,1,1),_P2mpHe1HrIndex_Type())
p2mpHe1HrIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:p2mpHe1HrIndex.setStatus(_A)
_P2mpHe1HrUpdateTime_Type=CwrUpdateTime
_P2mpHe1HrUpdateTime_Object=MibTableColumn
p2mpHe1HrUpdateTime=_P2mpHe1HrUpdateTime_Object((1,3,6,1,4,1,9,9,181,3,6,1,2),_P2mpHe1HrUpdateTime_Type())
p2mpHe1HrUpdateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpHe1HrUpdateTime.setStatus(_A)
if mibBuilder.loadTexts:p2mpHe1HrUpdateTime.setUnits(_K)
_P2mpHe1HrTotalCodewords_Type=WirelessGauge64
_P2mpHe1HrTotalCodewords_Object=MibTableColumn
p2mpHe1HrTotalCodewords=_P2mpHe1HrTotalCodewords_Object((1,3,6,1,4,1,9,9,181,3,6,1,3),_P2mpHe1HrTotalCodewords_Type())
p2mpHe1HrTotalCodewords.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpHe1HrTotalCodewords.setStatus(_A)
_P2mpHe1HrErroredCodewords_Type=WirelessGauge64
_P2mpHe1HrErroredCodewords_Object=MibTableColumn
p2mpHe1HrErroredCodewords=_P2mpHe1HrErroredCodewords_Object((1,3,6,1,4,1,9,9,181,3,6,1,4),_P2mpHe1HrErroredCodewords_Type())
p2mpHe1HrErroredCodewords.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpHe1HrErroredCodewords.setStatus(_A)
_P2mpRadioLinkConformance_ObjectIdentity=ObjectIdentity
p2mpRadioLinkConformance=_P2mpRadioLinkConformance_ObjectIdentity((1,3,6,1,4,1,9,9,181,4))
_P2mpRadioLinkCompliances_ObjectIdentity=ObjectIdentity
p2mpRadioLinkCompliances=_P2mpRadioLinkCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,181,4,1))
_P2mpRadioLinkGroups_ObjectIdentity=ObjectIdentity
p2mpRadioLinkGroups=_P2mpRadioLinkGroups_ObjectIdentity((1,3,6,1,4,1,9,9,181,4,2))
p2mpComplianceLinkMetricsGroup=ObjectGroup((1,3,6,1,4,1,9,9,181,4,2,1))
p2mpComplianceLinkMetricsGroup.setObjects(*((_B,_c),(_B,_d)))
if mibBuilder.loadTexts:p2mpComplianceLinkMetricsGroup.setStatus(_A)
p2mpComplianceSuMetricsGroup=ObjectGroup((1,3,6,1,4,1,9,9,181,4,2,2))
p2mpComplianceSuMetricsGroup.setObjects(*((_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af)))
if mibBuilder.loadTexts:p2mpComplianceSuMetricsGroup.setStatus(_A)
p2mpComplianceHeMetricsGroup=ObjectGroup((1,3,6,1,4,1,9,9,181,4,2,3))
p2mpComplianceHeMetricsGroup.setObjects(*((_B,_Ag),(_B,_P),(_B,_Ah),(_B,_Q),(_B,_R),(_B,_S),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,'p2mpSINR'),(_B,_Al),(_B,_Am),(_B,_An),(_B,_Ao),(_B,_Ap),(_B,_Aq),(_B,_Ar),(_B,_As),(_B,_At)))
if mibBuilder.loadTexts:p2mpComplianceHeMetricsGroup.setStatus(_A)
p2mpHeChPctErrCWThreshTrap=NotificationType((1,3,6,1,4,1,9,9,181,1,2,0,1))
p2mpHeChPctErrCWThreshTrap.setObjects((_B,_P))
if mibBuilder.loadTexts:p2mpHeChPctErrCWThreshTrap.setStatus(_A)
p2mpHeMacPctErrCWThreshTrap=NotificationType((1,3,6,1,4,1,9,9,181,1,2,0,2))
p2mpHeMacPctErrCWThreshTrap.setObjects(*((_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:p2mpHeMacPctErrCWThreshTrap.setStatus(_A)
p2mpSuErrSecAlarmTrap=NotificationType((1,3,6,1,4,1,9,9,181,1,2,0,3))
p2mpSuErrSecAlarmTrap.setObjects((_B,_L))
if mibBuilder.loadTexts:p2mpSuErrSecAlarmTrap.setStatus(_A)
p2mpSuSevErrSecAlarmTrap=NotificationType((1,3,6,1,4,1,9,9,181,1,2,0,4))
p2mpSuSevErrSecAlarmTrap.setObjects((_B,_M))
if mibBuilder.loadTexts:p2mpSuSevErrSecAlarmTrap.setStatus(_A)
p2mpSuConsecSevErrSecAlarmTrap=NotificationType((1,3,6,1,4,1,9,9,181,1,2,0,5))
p2mpSuConsecSevErrSecAlarmTrap.setObjects((_B,_N))
if mibBuilder.loadTexts:p2mpSuConsecSevErrSecAlarmTrap.setStatus(_A)
p2mpSuDegradedSecAlarmTrap=NotificationType((1,3,6,1,4,1,9,9,181,1,2,0,6))
p2mpSuDegradedSecAlarmTrap.setObjects((_B,_O))
if mibBuilder.loadTexts:p2mpSuDegradedSecAlarmTrap.setStatus(_A)
p2mpComplianceNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,181,4,2,4))
p2mpComplianceNotifGroup.setObjects(*((_B,_Au),(_B,_Av),(_B,_Aw),(_B,_Ax),(_B,_Ay),(_B,_Az)))
if mibBuilder.loadTexts:p2mpComplianceNotifGroup.setStatus(_A)
p2mpRadioLinkCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,181,4,1,1))
p2mpRadioLinkCompliance.setObjects(*((_B,_A_),(_B,_B0),(_B,_B1),(_B,_B2)))
if mibBuilder.loadTexts:p2mpRadioLinkCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoWirelessLinkMetricsMIB':ciscoWirelessLinkMetricsMIB,'p2mpLinkMetricsGroup':p2mpLinkMetricsGroup,'p2mpMetricsPrecisionTable':p2mpMetricsPrecisionTable,'p2mpMetricsPrecisionEntry':p2mpMetricsPrecisionEntry,_c:p2mpLinkMetricsScale,_d:p2mpLinkMetricsPrecision,'p2mpMetricsMIBNotificationPrefix':p2mpMetricsMIBNotificationPrefix,'p2mpMetricsMIBNotification':p2mpMetricsMIBNotification,_Au:p2mpHeChPctErrCWThreshTrap,_Av:p2mpHeMacPctErrCWThreshTrap,_Aw:p2mpSuErrSecAlarmTrap,_Ax:p2mpSuSevErrSecAlarmTrap,_Ay:p2mpSuConsecSevErrSecAlarmTrap,_Az:p2mpSuDegradedSecAlarmTrap,'p2mpSuLinkMetricsGroup':p2mpSuLinkMetricsGroup,'p2mpSuLinkMetricsThreshTable':p2mpSuLinkMetricsThreshTable,'p2mpSuLinkMetricsThreshEntry':p2mpSuLinkMetricsThreshEntry,_e:p2mpSuLinkESThresh,_f:p2mpSuLinkDSThresh,_g:p2mpSuLinkSESThresh,_h:p2mpSuLinkCSESThresh,_L:p2mpSuLink1HrESAlarmThresh,_M:p2mpSuLink1HrSESAlarmThresh,_N:p2mpSuLink1HrCSESAlarmThresh,_O:p2mpSuLink1HrDCSAlarmThresh,'p2mpSu1SecMetricsTable':p2mpSu1SecMetricsTable,'p2mpSu1SecMetricsEntry':p2mpSu1SecMetricsEntry,_T:p2mpSu1SecIndex,_i:p2mpSu1SecUpdateTime,_j:p2mpSu1SecType,_k:p2mpSu1SecTotalCodewords,_l:p2mpSu1SecTotalErrCodewords,_m:p2mpSu1SecValidDataPkt,'p2mpSu1MinMetricsTable':p2mpSu1MinMetricsTable,'p2mpSu1MinMetricsEntry':p2mpSu1MinMetricsEntry,_U:p2mpSu1MinIndex,_n:p2mpSu1MinUpdateTime,_o:p2mpSu1MinTotalCodewords,_p:p2mpSu1MinTotalErrCodewords,_q:p2mpSu1MinValidDataPkt,_r:p2mpSu1MinErrorFreeSeconds,_s:p2mpSu1MinErroredSeconds,_w:p2mpSu1MinDegradedSeconds,_t:p2mpSu1MinSevErroredSeconds,_u:p2mpSu1MinConsecSevErrSeconds,_v:p2mpSu1MinSyncLossSeconds,_x:p2mpSu1MinTxPowerMax,_y:p2mpSu1MinTxPowerMin,_z:p2mpSu1MinTxPowerAvg,_A0:p2mpSu1MinMainAntRxPowerMax,_A1:p2mpSu1MinMainAntRxPowerMin,_A2:p2mpSu1MinMainAntRxPowerAvg,_A3:p2mpSu1MinDivAntRxPowerMax,_A4:p2mpSu1MinDivAntRxPowerMin,_A5:p2mpSu1MinDivAntRxPowerAvg,'p2mpSu1HrMetricsTable':p2mpSu1HrMetricsTable,'p2mpSu1HrMetricsEntry':p2mpSu1HrMetricsEntry,_V:p2mpSu1HrIndex,_A6:p2mpSu1HrUpdateTime,_A7:p2mpSu1HrTotalCodewords,_A8:p2mpSu1HrTotalErrCodewords,_A9:p2mpSu1HrValidDataPkt,_AA:p2mpSu1HrErrorFreeSeconds,_AB:p2mpSu1HrErroredSeconds,_AC:p2mpSu1HrSevErroredSeconds,_AD:p2mpSu1HrConsecSvErrSeconds,_AE:p2mpSu1HrSyncLossSeconds,_AF:p2mpSu1HrDegradedSeconds,_AG:p2mpSu1HrTxPowerMax,_AH:p2mpSu1HrTxPowerMin,_AI:p2mpSu1HrTxPowerAvg,_AJ:p2mpSu1HrMainAntRxPowerMax,_AK:p2mpSu1HrMainAntRxPowerMin,_AL:p2mpSu1HrMainAntRxPowerAvg,_AM:p2mpSu1HrDivAntRxPowerMax,_AN:p2mpSu1HrDivAntRxPowerMin,_AO:p2mpSu1HrDivAntRxPowerAvg,'p2mpSuCumulativeLinkMetricsTable':p2mpSuCumulativeLinkMetricsTable,'p2mpSuCumulativeLinkMetricsEntry':p2mpSuCumulativeLinkMetricsEntry,_AP:p2mpSuAvailableSeconds,_AQ:p2mpSuUnAvailableSeconds,_AR:p2mpSuPctAvailSeconds,_AS:p2mpSuSyncLossSeconds,_AT:p2mpSuPctErrorFreeSeconds,_AU:p2mpSuPctErroredSeconds,_AV:p2mpSuPctSevErroredSeconds,_AW:p2mpSuPctDegradedSeconds,_AX:p2mpSuInitialSyncSeconds,_AY:p2mpSuSyncSuccessCount,_AZ:p2mpSuLastSyncSuccessTime,_Ac:p2mpSuSyncFailureCount,_Ad:p2mpSuLastSyncFailTime,_Aa:p2mpSuSyncMedEffort,_Ab:p2mpSuSyncHighEffort,_Ae:p2mpSuEffectiveDataRate,_Af:p2mpSuPercentEfficiency,'p2mpHeLinkMetricsGroup':p2mpHeLinkMetricsGroup,'p2mpHeLinkMetricsThreshTable':p2mpHeLinkMetricsThreshTable,'p2mpHeLinkMetricsThreshEntry':p2mpHeLinkMetricsThreshEntry,_Ag:p2mpHe1HrMinTotalCWThresh,_P:p2mpHe1HrPctErrCWThresh,'p2mpHeBadSuTable':p2mpHeBadSuTable,'p2mpHeBadSuEntry':p2mpHeBadSuEntry,_W:p2mpBadSuIndex,_Ah:p2mpBadSuUpdateTime,_Q:p2mpBadSuMacAddress,_R:p2mpTotalErroredCodewords,_S:p2mpPctErroredCodewords,'p2mpHeCodewordErrorTable':p2mpHeCodewordErrorTable,'p2mpHeCodewordErrorEntry':p2mpHeCodewordErrorEntry,_X:p2mpSuMacAddress,_Y:p2mpHeCWErrorIndex,_Ai:p2mpHeCWErrorUpdateTime,_Aj:p2mpTotalCodewords,_Ak:p2mpErroredCodewords,'p2mpSINR':p2mpSINR,'p2mpHe1SecMetricsTable':p2mpHe1SecMetricsTable,'p2mpHe1SecMetricsEntry':p2mpHe1SecMetricsEntry,_Z:p2mpHe1SecIndex,_Al:p2mpHe1SecUpdateTime,_Am:p2mpHe1SecTotalCodewords,_An:p2mpHe1SecErroredCodewords,'p2mpHe1MinMetricsTable':p2mpHe1MinMetricsTable,'p2mpHe1MinMetricsEntry':p2mpHe1MinMetricsEntry,_a:p2mpHe1MinIndex,_Ao:p2mpHe1MinUpdateTime,_Ap:p2mpHe1MinTotalCodewords,_Aq:p2mpHe1MinErroredCodewords,'p2mpHe1HrMetricsTable':p2mpHe1HrMetricsTable,'p2mpHe1HrMetricsEntry':p2mpHe1HrMetricsEntry,_b:p2mpHe1HrIndex,_Ar:p2mpHe1HrUpdateTime,_As:p2mpHe1HrTotalCodewords,_At:p2mpHe1HrErroredCodewords,'p2mpRadioLinkConformance':p2mpRadioLinkConformance,'p2mpRadioLinkCompliances':p2mpRadioLinkCompliances,'p2mpRadioLinkCompliance':p2mpRadioLinkCompliance,'p2mpRadioLinkGroups':p2mpRadioLinkGroups,_A_:p2mpComplianceLinkMetricsGroup,_B0:p2mpComplianceSuMetricsGroup,_B1:p2mpComplianceHeMetricsGroup,_B2:p2mpComplianceNotifGroup})