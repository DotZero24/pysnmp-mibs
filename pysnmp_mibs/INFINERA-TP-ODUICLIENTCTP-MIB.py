_AA='oduiClientCtpGroup'
_A9='oduiClientCtpBitRateK'
_A8='oduiClientCtpRxBeiDayTceReporting'
_A7='oduiClientCtpRxBeiDayTce'
_A6='oduiClientCtpRxBei15MinutesTceReporting'
_A5='oduiClientCtpRxBei15MinutesTce'
_A4='oduiClientCtpRxDsFDayTceReporting'
_A3='oduiClientCtpRxDsFDayTce'
_A2='oduiClientCtpRxDsF15MinutesTceReporting'
_A1='oduiClientCtpRxDsF15MinutesTce'
_A0='oduiClientCtpFacSDThreshold'
_z='oduiClientCtpLoopBack'
_y='oduiClientCtpExpectedPayload'
_x='oduiClientCtpTsg'
_w='oduiClientCtpSupportingTP'
_v='oduiClientCtpCrossConnectType'
_u='oduiClientCtpdatarate'
_t='oduiClientCtpavailableOPUTributarySlots'
_s='oduiClientCtpsupportingOPUTributarySlots'
_r='oduiClientCtpDetectedTPNs'
_q='oduiClientCtpExpectedTPNs'
_p='oduiClientCtpTributaryPortNumber'
_o='oduiClientCtprate'
_n='oduiClientCtpTSCount'
_m='oduiClientCtpTermMonitoringMode'
_l='oduiClientCtpTermDSThreshold'
_k='oduiClientCtpFacDSThreshold'
_j='oduiClientCtpSupportingCircuitIdList'
_i='oduiClientCtpAlarmReportControl'
_h='oduiClientCtpTermPmHistStatsEnable'
_g='oduiClientCtpFacPmHistStatsEnable'
_f='oduiClientCtpConfiguredServiceType'
_e='oduiClientCtpTcmList'
_d='oduiClientCtpTermTimDetMode'
_c='oduiClientCtpFacTimDetMode'
_b='oduiClientCtpRxDs15MinutesTceReporting'
_a='oduiClientCtpRxDsDayTceReporting'
_Z='oduiClientCtpRxDsDayTce'
_Y='oduiClientCtpRxDs15MinutesTce'
_X='oduiClientCtpTermReceivedTTI'
_W='oduiClientCtpFacReceivedTTI'
_V='oduiClientCtpTermExpectedDAPI'
_U='oduiClientCtpTermExpectedSAPI'
_T='oduiClientCtpTermTxTTI'
_S='oduiClientCtpFacExpectedDAPI'
_R='oduiClientCtpFacExpectedSAPI'
_Q='oduiClientCtpFacTxTTI'
_P='oduiClientCtpFacMonitoringMode'
_O='oduiClientCtpServiceMode'
_N='sapidapi'
_M='InfnServiceMode'
_L='InfnSMQ'
_K='InfnArc'
_J='ifIndex'
_I='IF-MIB'
_H='TruthValue'
_G='InfnEnableDisable'
_F='DisplayString'
_E='Integer32'
_D='read-only'
_C='read-write'
_B='INFINERA-TP-ODUICLIENTCTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_I,_J)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
InfnArc,InfnEnableDisable,InfnEqptType,InfnMonitoringMode,InfnOtuBitRateK,InfnRate,InfnSMQ,InfnServiceMode,InfnServiceType,InfnTcmList,InfnTsgType,InfnXconType=mibBuilder.importSymbols('INFINERA-TC-MIB',_K,_G,'InfnEqptType','InfnMonitoringMode','InfnOtuBitRateK','InfnRate',_L,_M,'InfnServiceType','InfnTcmList','InfnTsgType','InfnXconType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention',_H)
oduiClientCtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,30))
if mibBuilder.loadTexts:oduiClientCtpMIB.setRevisions(('2009-07-20 00:00',))
_OduiClientCtpTable_Object=MibTable
oduiClientCtpTable=_OduiClientCtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1))
if mibBuilder.loadTexts:oduiClientCtpTable.setStatus(_A)
_OduiClientCtpEntry_Object=MibTableRow
oduiClientCtpEntry=_OduiClientCtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1))
oduiClientCtpEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:oduiClientCtpEntry.setStatus(_A)
class _OduiClientCtpServiceMode_Type(InfnServiceMode):defaultValue=1
_OduiClientCtpServiceMode_Type.__name__=_M
_OduiClientCtpServiceMode_Object=MibTableColumn
oduiClientCtpServiceMode=_OduiClientCtpServiceMode_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,1),_OduiClientCtpServiceMode_Type())
oduiClientCtpServiceMode.setMaxAccess(_D)
if mibBuilder.loadTexts:oduiClientCtpServiceMode.setStatus(_A)
class _OduiClientCtpServiceModeQualifier_Type(InfnSMQ):defaultValue=1
_OduiClientCtpServiceModeQualifier_Type.__name__=_L
_OduiClientCtpServiceModeQualifier_Object=MibTableColumn
oduiClientCtpServiceModeQualifier=_OduiClientCtpServiceModeQualifier_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,2),_OduiClientCtpServiceModeQualifier_Type())
oduiClientCtpServiceModeQualifier.setMaxAccess(_D)
if mibBuilder.loadTexts:oduiClientCtpServiceModeQualifier.setStatus(_A)
_OduiClientCtpFacMonitoringMode_Type=InfnMonitoringMode
_OduiClientCtpFacMonitoringMode_Object=MibTableColumn
oduiClientCtpFacMonitoringMode=_OduiClientCtpFacMonitoringMode_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,3),_OduiClientCtpFacMonitoringMode_Type())
oduiClientCtpFacMonitoringMode.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiClientCtpFacMonitoringMode.setStatus(_A)
class _OduiClientCtpFacTxTTI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_OduiClientCtpFacTxTTI_Type.__name__=_F
_OduiClientCtpFacTxTTI_Object=MibTableColumn
oduiClientCtpFacTxTTI=_OduiClientCtpFacTxTTI_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,4),_OduiClientCtpFacTxTTI_Type())
oduiClientCtpFacTxTTI.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiClientCtpFacTxTTI.setStatus(_A)
class _OduiClientCtpFacExpectedSAPI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_OduiClientCtpFacExpectedSAPI_Type.__name__=_F
_OduiClientCtpFacExpectedSAPI_Object=MibTableColumn
oduiClientCtpFacExpectedSAPI=_OduiClientCtpFacExpectedSAPI_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,5),_OduiClientCtpFacExpectedSAPI_Type())
oduiClientCtpFacExpectedSAPI.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiClientCtpFacExpectedSAPI.setStatus(_A)
class _OduiClientCtpFacExpectedDAPI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_OduiClientCtpFacExpectedDAPI_Type.__name__=_F
_OduiClientCtpFacExpectedDAPI_Object=MibTableColumn
oduiClientCtpFacExpectedDAPI=_OduiClientCtpFacExpectedDAPI_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,6),_OduiClientCtpFacExpectedDAPI_Type())
oduiClientCtpFacExpectedDAPI.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiClientCtpFacExpectedDAPI.setStatus(_A)
class _OduiClientCtpTermTxTTI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_OduiClientCtpTermTxTTI_Type.__name__=_F
_OduiClientCtpTermTxTTI_Object=MibTableColumn
oduiClientCtpTermTxTTI=_OduiClientCtpTermTxTTI_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,7),_OduiClientCtpTermTxTTI_Type())
oduiClientCtpTermTxTTI.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiClientCtpTermTxTTI.setStatus(_A)
class _OduiClientCtpTermExpectedSAPI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_OduiClientCtpTermExpectedSAPI_Type.__name__=_F
_OduiClientCtpTermExpectedSAPI_Object=MibTableColumn
oduiClientCtpTermExpectedSAPI=_OduiClientCtpTermExpectedSAPI_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,8),_OduiClientCtpTermExpectedSAPI_Type())
oduiClientCtpTermExpectedSAPI.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiClientCtpTermExpectedSAPI.setStatus(_A)
class _OduiClientCtpTermExpectedDAPI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_OduiClientCtpTermExpectedDAPI_Type.__name__=_F
_OduiClientCtpTermExpectedDAPI_Object=MibTableColumn
oduiClientCtpTermExpectedDAPI=_OduiClientCtpTermExpectedDAPI_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,9),_OduiClientCtpTermExpectedDAPI_Type())
oduiClientCtpTermExpectedDAPI.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiClientCtpTermExpectedDAPI.setStatus(_A)
class _OduiClientCtpFacReceivedTTI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_OduiClientCtpFacReceivedTTI_Type.__name__=_F
_OduiClientCtpFacReceivedTTI_Object=MibTableColumn
oduiClientCtpFacReceivedTTI=_OduiClientCtpFacReceivedTTI_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,10),_OduiClientCtpFacReceivedTTI_Type())
oduiClientCtpFacReceivedTTI.setMaxAccess(_D)
if mibBuilder.loadTexts:oduiClientCtpFacReceivedTTI.setStatus(_A)
class _OduiClientCtpTermReceivedTTI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_OduiClientCtpTermReceivedTTI_Type.__name__=_F
_OduiClientCtpTermReceivedTTI_Object=MibTableColumn
oduiClientCtpTermReceivedTTI=_OduiClientCtpTermReceivedTTI_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,11),_OduiClientCtpTermReceivedTTI_Type())
oduiClientCtpTermReceivedTTI.setMaxAccess(_D)
if mibBuilder.loadTexts:oduiClientCtpTermReceivedTTI.setStatus(_A)
class _OduiClientCtpRxDs15MinutesTce_Type(Integer32):defaultValue=120
_OduiClientCtpRxDs15MinutesTce_Type.__name__=_E
_OduiClientCtpRxDs15MinutesTce_Object=MibTableColumn
oduiClientCtpRxDs15MinutesTce=_OduiClientCtpRxDs15MinutesTce_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,12),_OduiClientCtpRxDs15MinutesTce_Type())
oduiClientCtpRxDs15MinutesTce.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiClientCtpRxDs15MinutesTce.setStatus(_A)
class _OduiClientCtpRxDsDayTce_Type(Integer32):defaultValue=1200
_OduiClientCtpRxDsDayTce_Type.__name__=_E
_OduiClientCtpRxDsDayTce_Object=MibTableColumn
oduiClientCtpRxDsDayTce=_OduiClientCtpRxDsDayTce_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,13),_OduiClientCtpRxDsDayTce_Type())
oduiClientCtpRxDsDayTce.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiClientCtpRxDsDayTce.setStatus(_A)
class _OduiClientCtpRxDsDayTceReporting_Type(TruthValue):defaultValue=2
_OduiClientCtpRxDsDayTceReporting_Type.__name__=_H
_OduiClientCtpRxDsDayTceReporting_Object=MibTableColumn
oduiClientCtpRxDsDayTceReporting=_OduiClientCtpRxDsDayTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,14),_OduiClientCtpRxDsDayTceReporting_Type())
oduiClientCtpRxDsDayTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiClientCtpRxDsDayTceReporting.setStatus(_A)
class _OduiClientCtpRxDs15MinutesTceReporting_Type(TruthValue):defaultValue=2
_OduiClientCtpRxDs15MinutesTceReporting_Type.__name__=_H
_OduiClientCtpRxDs15MinutesTceReporting_Object=MibTableColumn
oduiClientCtpRxDs15MinutesTceReporting=_OduiClientCtpRxDs15MinutesTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,15),_OduiClientCtpRxDs15MinutesTceReporting_Type())
oduiClientCtpRxDs15MinutesTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiClientCtpRxDs15MinutesTceReporting.setStatus(_A)
class _OduiClientCtpFacTimDetMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('off',1),('sapi',2),('dapi',3),(_N,4)))
_OduiClientCtpFacTimDetMode_Type.__name__=_E
_OduiClientCtpFacTimDetMode_Object=MibTableColumn
oduiClientCtpFacTimDetMode=_OduiClientCtpFacTimDetMode_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,16),_OduiClientCtpFacTimDetMode_Type())
oduiClientCtpFacTimDetMode.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiClientCtpFacTimDetMode.setStatus(_A)
class _OduiClientCtpTermTimDetMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('off',1),('sapi',2),('dapi',3),(_N,4)))
_OduiClientCtpTermTimDetMode_Type.__name__=_E
_OduiClientCtpTermTimDetMode_Object=MibTableColumn
oduiClientCtpTermTimDetMode=_OduiClientCtpTermTimDetMode_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,17),_OduiClientCtpTermTimDetMode_Type())
oduiClientCtpTermTimDetMode.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiClientCtpTermTimDetMode.setStatus(_A)
_OduiClientCtpTcmList_Type=InfnTcmList
_OduiClientCtpTcmList_Object=MibTableColumn
oduiClientCtpTcmList=_OduiClientCtpTcmList_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,18),_OduiClientCtpTcmList_Type())
oduiClientCtpTcmList.setMaxAccess(_D)
if mibBuilder.loadTexts:oduiClientCtpTcmList.setStatus(_A)
_OduiClientCtpConfiguredServiceType_Type=InfnServiceType
_OduiClientCtpConfiguredServiceType_Object=MibTableColumn
oduiClientCtpConfiguredServiceType=_OduiClientCtpConfiguredServiceType_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,19),_OduiClientCtpConfiguredServiceType_Type())
oduiClientCtpConfiguredServiceType.setMaxAccess(_D)
if mibBuilder.loadTexts:oduiClientCtpConfiguredServiceType.setStatus(_A)
class _OduiClientCtpFacPmHistStatsEnable_Type(InfnEnableDisable):defaultValue=2
_OduiClientCtpFacPmHistStatsEnable_Type.__name__=_G
_OduiClientCtpFacPmHistStatsEnable_Object=MibTableColumn
oduiClientCtpFacPmHistStatsEnable=_OduiClientCtpFacPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,20),_OduiClientCtpFacPmHistStatsEnable_Type())
oduiClientCtpFacPmHistStatsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiClientCtpFacPmHistStatsEnable.setStatus(_A)
class _OduiClientCtpTermPmHistStatsEnable_Type(InfnEnableDisable):defaultValue=2
_OduiClientCtpTermPmHistStatsEnable_Type.__name__=_G
_OduiClientCtpTermPmHistStatsEnable_Object=MibTableColumn
oduiClientCtpTermPmHistStatsEnable=_OduiClientCtpTermPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,21),_OduiClientCtpTermPmHistStatsEnable_Type())
oduiClientCtpTermPmHistStatsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiClientCtpTermPmHistStatsEnable.setStatus(_A)
class _OduiClientCtpAlarmReportControl_Type(InfnArc):defaultValue=1
_OduiClientCtpAlarmReportControl_Type.__name__=_K
_OduiClientCtpAlarmReportControl_Object=MibTableColumn
oduiClientCtpAlarmReportControl=_OduiClientCtpAlarmReportControl_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,22),_OduiClientCtpAlarmReportControl_Type())
oduiClientCtpAlarmReportControl.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiClientCtpAlarmReportControl.setStatus(_A)
_OduiClientCtpSupportingCircuitIdList_Type=DisplayString
_OduiClientCtpSupportingCircuitIdList_Object=MibTableColumn
oduiClientCtpSupportingCircuitIdList=_OduiClientCtpSupportingCircuitIdList_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,23),_OduiClientCtpSupportingCircuitIdList_Type())
oduiClientCtpSupportingCircuitIdList.setMaxAccess(_D)
if mibBuilder.loadTexts:oduiClientCtpSupportingCircuitIdList.setStatus(_A)
class _OduiClientCtpFacDSThreshold_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_OduiClientCtpFacDSThreshold_Type.__name__=_E
_OduiClientCtpFacDSThreshold_Object=MibTableColumn
oduiClientCtpFacDSThreshold=_OduiClientCtpFacDSThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,24),_OduiClientCtpFacDSThreshold_Type())
oduiClientCtpFacDSThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiClientCtpFacDSThreshold.setStatus(_A)
class _OduiClientCtpTermDSThreshold_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_OduiClientCtpTermDSThreshold_Type.__name__=_E
_OduiClientCtpTermDSThreshold_Object=MibTableColumn
oduiClientCtpTermDSThreshold=_OduiClientCtpTermDSThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,25),_OduiClientCtpTermDSThreshold_Type())
oduiClientCtpTermDSThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiClientCtpTermDSThreshold.setStatus(_A)
_OduiClientCtpTermMonitoringMode_Type=InfnMonitoringMode
_OduiClientCtpTermMonitoringMode_Object=MibTableColumn
oduiClientCtpTermMonitoringMode=_OduiClientCtpTermMonitoringMode_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,26),_OduiClientCtpTermMonitoringMode_Type())
oduiClientCtpTermMonitoringMode.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiClientCtpTermMonitoringMode.setStatus(_A)
_OduiClientCtpTSCount_Type=Integer32
_OduiClientCtpTSCount_Object=MibTableColumn
oduiClientCtpTSCount=_OduiClientCtpTSCount_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,28),_OduiClientCtpTSCount_Type())
oduiClientCtpTSCount.setMaxAccess(_D)
if mibBuilder.loadTexts:oduiClientCtpTSCount.setStatus(_A)
_OduiClientCtprate_Type=DisplayString
_OduiClientCtprate_Object=MibTableColumn
oduiClientCtprate=_OduiClientCtprate_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,29),_OduiClientCtprate_Type())
oduiClientCtprate.setMaxAccess(_D)
if mibBuilder.loadTexts:oduiClientCtprate.setStatus(_A)
_OduiClientCtpTributaryPortNumber_Type=Integer32
_OduiClientCtpTributaryPortNumber_Object=MibTableColumn
oduiClientCtpTributaryPortNumber=_OduiClientCtpTributaryPortNumber_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,30),_OduiClientCtpTributaryPortNumber_Type())
oduiClientCtpTributaryPortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:oduiClientCtpTributaryPortNumber.setStatus(_A)
_OduiClientCtpExpectedTPNs_Type=Integer32
_OduiClientCtpExpectedTPNs_Object=MibTableColumn
oduiClientCtpExpectedTPNs=_OduiClientCtpExpectedTPNs_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,31),_OduiClientCtpExpectedTPNs_Type())
oduiClientCtpExpectedTPNs.setMaxAccess(_D)
if mibBuilder.loadTexts:oduiClientCtpExpectedTPNs.setStatus(_A)
_OduiClientCtpDetectedTPNs_Type=Integer32
_OduiClientCtpDetectedTPNs_Object=MibTableColumn
oduiClientCtpDetectedTPNs=_OduiClientCtpDetectedTPNs_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,32),_OduiClientCtpDetectedTPNs_Type())
oduiClientCtpDetectedTPNs.setMaxAccess(_D)
if mibBuilder.loadTexts:oduiClientCtpDetectedTPNs.setStatus(_A)
_OduiClientCtpsupportingOPUTributarySlots_Type=DisplayString
_OduiClientCtpsupportingOPUTributarySlots_Object=MibTableColumn
oduiClientCtpsupportingOPUTributarySlots=_OduiClientCtpsupportingOPUTributarySlots_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,33),_OduiClientCtpsupportingOPUTributarySlots_Type())
oduiClientCtpsupportingOPUTributarySlots.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiClientCtpsupportingOPUTributarySlots.setStatus(_A)
_OduiClientCtpavailableOPUTributarySlots_Type=DisplayString
_OduiClientCtpavailableOPUTributarySlots_Object=MibTableColumn
oduiClientCtpavailableOPUTributarySlots=_OduiClientCtpavailableOPUTributarySlots_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,34),_OduiClientCtpavailableOPUTributarySlots_Type())
oduiClientCtpavailableOPUTributarySlots.setMaxAccess(_D)
if mibBuilder.loadTexts:oduiClientCtpavailableOPUTributarySlots.setStatus(_A)
_OduiClientCtpdatarate_Type=InfnRate
_OduiClientCtpdatarate_Object=MibTableColumn
oduiClientCtpdatarate=_OduiClientCtpdatarate_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,35),_OduiClientCtpdatarate_Type())
oduiClientCtpdatarate.setMaxAccess(_D)
if mibBuilder.loadTexts:oduiClientCtpdatarate.setStatus(_A)
_OduiClientCtpCrossConnectType_Type=InfnXconType
_OduiClientCtpCrossConnectType_Object=MibTableColumn
oduiClientCtpCrossConnectType=_OduiClientCtpCrossConnectType_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,36),_OduiClientCtpCrossConnectType_Type())
oduiClientCtpCrossConnectType.setMaxAccess(_D)
if mibBuilder.loadTexts:oduiClientCtpCrossConnectType.setStatus(_A)
_OduiClientCtpSupportingTP_Type=DisplayString
_OduiClientCtpSupportingTP_Object=MibTableColumn
oduiClientCtpSupportingTP=_OduiClientCtpSupportingTP_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,37),_OduiClientCtpSupportingTP_Type())
oduiClientCtpSupportingTP.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiClientCtpSupportingTP.setStatus(_A)
_OduiClientCtpTsg_Type=InfnTsgType
_OduiClientCtpTsg_Object=MibTableColumn
oduiClientCtpTsg=_OduiClientCtpTsg_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,38),_OduiClientCtpTsg_Type())
oduiClientCtpTsg.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiClientCtpTsg.setStatus(_A)
_OduiClientCtpExpectedPayload_Type=InfnServiceType
_OduiClientCtpExpectedPayload_Object=MibTableColumn
oduiClientCtpExpectedPayload=_OduiClientCtpExpectedPayload_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,39),_OduiClientCtpExpectedPayload_Type())
oduiClientCtpExpectedPayload.setMaxAccess(_D)
if mibBuilder.loadTexts:oduiClientCtpExpectedPayload.setStatus(_A)
class _OduiClientCtpLoopBack_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('terminal',2),('facility',3)))
_OduiClientCtpLoopBack_Type.__name__=_E
_OduiClientCtpLoopBack_Object=MibTableColumn
oduiClientCtpLoopBack=_OduiClientCtpLoopBack_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,40),_OduiClientCtpLoopBack_Type())
oduiClientCtpLoopBack.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiClientCtpLoopBack.setStatus(_A)
class _OduiClientCtpFacSDThreshold_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_OduiClientCtpFacSDThreshold_Type.__name__=_E
_OduiClientCtpFacSDThreshold_Object=MibTableColumn
oduiClientCtpFacSDThreshold=_OduiClientCtpFacSDThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,41),_OduiClientCtpFacSDThreshold_Type())
oduiClientCtpFacSDThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiClientCtpFacSDThreshold.setStatus(_A)
_OduiClientCtpRxDsF15MinutesTce_Type=Integer32
_OduiClientCtpRxDsF15MinutesTce_Object=MibTableColumn
oduiClientCtpRxDsF15MinutesTce=_OduiClientCtpRxDsF15MinutesTce_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,42),_OduiClientCtpRxDsF15MinutesTce_Type())
oduiClientCtpRxDsF15MinutesTce.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiClientCtpRxDsF15MinutesTce.setStatus(_A)
_OduiClientCtpRxDsF15MinutesTceReporting_Type=TruthValue
_OduiClientCtpRxDsF15MinutesTceReporting_Object=MibTableColumn
oduiClientCtpRxDsF15MinutesTceReporting=_OduiClientCtpRxDsF15MinutesTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,43),_OduiClientCtpRxDsF15MinutesTceReporting_Type())
oduiClientCtpRxDsF15MinutesTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiClientCtpRxDsF15MinutesTceReporting.setStatus(_A)
_OduiClientCtpRxDsFDayTce_Type=Integer32
_OduiClientCtpRxDsFDayTce_Object=MibTableColumn
oduiClientCtpRxDsFDayTce=_OduiClientCtpRxDsFDayTce_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,44),_OduiClientCtpRxDsFDayTce_Type())
oduiClientCtpRxDsFDayTce.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiClientCtpRxDsFDayTce.setStatus(_A)
_OduiClientCtpRxDsFDayTceReporting_Type=TruthValue
_OduiClientCtpRxDsFDayTceReporting_Object=MibTableColumn
oduiClientCtpRxDsFDayTceReporting=_OduiClientCtpRxDsFDayTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,45),_OduiClientCtpRxDsFDayTceReporting_Type())
oduiClientCtpRxDsFDayTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiClientCtpRxDsFDayTceReporting.setStatus(_A)
_OduiClientCtpRxBei15MinutesTce_Type=Integer32
_OduiClientCtpRxBei15MinutesTce_Object=MibTableColumn
oduiClientCtpRxBei15MinutesTce=_OduiClientCtpRxBei15MinutesTce_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,46),_OduiClientCtpRxBei15MinutesTce_Type())
oduiClientCtpRxBei15MinutesTce.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiClientCtpRxBei15MinutesTce.setStatus(_A)
_OduiClientCtpRxBei15MinutesTceReporting_Type=TruthValue
_OduiClientCtpRxBei15MinutesTceReporting_Object=MibTableColumn
oduiClientCtpRxBei15MinutesTceReporting=_OduiClientCtpRxBei15MinutesTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,47),_OduiClientCtpRxBei15MinutesTceReporting_Type())
oduiClientCtpRxBei15MinutesTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiClientCtpRxBei15MinutesTceReporting.setStatus(_A)
_OduiClientCtpRxBeiDayTce_Type=Integer32
_OduiClientCtpRxBeiDayTce_Object=MibTableColumn
oduiClientCtpRxBeiDayTce=_OduiClientCtpRxBeiDayTce_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,48),_OduiClientCtpRxBeiDayTce_Type())
oduiClientCtpRxBeiDayTce.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiClientCtpRxBeiDayTce.setStatus(_A)
_OduiClientCtpRxBeiDayTceReporting_Type=TruthValue
_OduiClientCtpRxBeiDayTceReporting_Object=MibTableColumn
oduiClientCtpRxBeiDayTceReporting=_OduiClientCtpRxBeiDayTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,49),_OduiClientCtpRxBeiDayTceReporting_Type())
oduiClientCtpRxBeiDayTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiClientCtpRxBeiDayTceReporting.setStatus(_A)
_OduiClientCtpBitRateK_Type=InfnOtuBitRateK
_OduiClientCtpBitRateK_Object=MibTableColumn
oduiClientCtpBitRateK=_OduiClientCtpBitRateK_Object((1,3,6,1,4,1,21296,2,2,2,2,30,1,1,50),_OduiClientCtpBitRateK_Type())
oduiClientCtpBitRateK.setMaxAccess(_D)
if mibBuilder.loadTexts:oduiClientCtpBitRateK.setStatus(_A)
_OduiClientCtpConformance_ObjectIdentity=ObjectIdentity
oduiClientCtpConformance=_OduiClientCtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,30,3))
_OduiClientCtpCompliances_ObjectIdentity=ObjectIdentity
oduiClientCtpCompliances=_OduiClientCtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,30,3,1))
_OduiClientCtpGroups_ObjectIdentity=ObjectIdentity
oduiClientCtpGroups=_OduiClientCtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,30,3,2))
oduiClientCtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,30,3,2,1))
oduiClientCtpGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9)))
if mibBuilder.loadTexts:oduiClientCtpGroup.setStatus(_A)
oduiClientCtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,30,3,1,1))
oduiClientCtpCompliance.setObjects((_B,_AA))
if mibBuilder.loadTexts:oduiClientCtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'oduiClientCtpMIB':oduiClientCtpMIB,'oduiClientCtpTable':oduiClientCtpTable,'oduiClientCtpEntry':oduiClientCtpEntry,_O:oduiClientCtpServiceMode,'oduiClientCtpServiceModeQualifier':oduiClientCtpServiceModeQualifier,_P:oduiClientCtpFacMonitoringMode,_Q:oduiClientCtpFacTxTTI,_R:oduiClientCtpFacExpectedSAPI,_S:oduiClientCtpFacExpectedDAPI,_T:oduiClientCtpTermTxTTI,_U:oduiClientCtpTermExpectedSAPI,_V:oduiClientCtpTermExpectedDAPI,_W:oduiClientCtpFacReceivedTTI,_X:oduiClientCtpTermReceivedTTI,_Y:oduiClientCtpRxDs15MinutesTce,_Z:oduiClientCtpRxDsDayTce,_a:oduiClientCtpRxDsDayTceReporting,_b:oduiClientCtpRxDs15MinutesTceReporting,_c:oduiClientCtpFacTimDetMode,_d:oduiClientCtpTermTimDetMode,_e:oduiClientCtpTcmList,_f:oduiClientCtpConfiguredServiceType,_g:oduiClientCtpFacPmHistStatsEnable,_h:oduiClientCtpTermPmHistStatsEnable,_i:oduiClientCtpAlarmReportControl,_j:oduiClientCtpSupportingCircuitIdList,_k:oduiClientCtpFacDSThreshold,_l:oduiClientCtpTermDSThreshold,_m:oduiClientCtpTermMonitoringMode,_n:oduiClientCtpTSCount,_o:oduiClientCtprate,_p:oduiClientCtpTributaryPortNumber,_q:oduiClientCtpExpectedTPNs,_r:oduiClientCtpDetectedTPNs,_s:oduiClientCtpsupportingOPUTributarySlots,_t:oduiClientCtpavailableOPUTributarySlots,_u:oduiClientCtpdatarate,_v:oduiClientCtpCrossConnectType,_w:oduiClientCtpSupportingTP,_x:oduiClientCtpTsg,_y:oduiClientCtpExpectedPayload,_z:oduiClientCtpLoopBack,_A0:oduiClientCtpFacSDThreshold,_A1:oduiClientCtpRxDsF15MinutesTce,_A2:oduiClientCtpRxDsF15MinutesTceReporting,_A3:oduiClientCtpRxDsFDayTce,_A4:oduiClientCtpRxDsFDayTceReporting,_A5:oduiClientCtpRxBei15MinutesTce,_A6:oduiClientCtpRxBei15MinutesTceReporting,_A7:oduiClientCtpRxBeiDayTce,_A8:oduiClientCtpRxBeiDayTceReporting,_A9:oduiClientCtpBitRateK,'oduiClientCtpConformance':oduiClientCtpConformance,'oduiClientCtpCompliances':oduiClientCtpCompliances,'oduiClientCtpCompliance':oduiClientCtpCompliance,'oduiClientCtpGroups':oduiClientCtpGroups,_AA:oduiClientCtpGroup})