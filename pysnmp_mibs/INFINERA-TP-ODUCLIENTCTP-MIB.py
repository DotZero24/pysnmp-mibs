_Ag='oduClientCtpGroup'
_Af='oduClientCtpDetectedTPNList'
_Ae='oduClientCtpTermDMPSLatLowThreshold'
_Ad='oduClientCtpTermDMPSLatHighThreshold'
_Ac='oduClientCtpFacDMPSLatLowThreshold'
_Ab='oduClientCtpFacDMPSLatHighThreshold'
_Aa='oduClientCtpTermDMPELatLowThreshold'
_AZ='oduClientCtpTermDMPELatHighThreshold'
_AY='oduClientCtpFacDMPELatLowThreshold'
_AX='oduClientCtpFacDMPELatHighThreshold'
_AW='oduClientCtpTermDMPSLatencyMode'
_AV='oduClientCtpTermDMPELatencyMode'
_AU='oduClientCtpFacDMPSLatencyMode'
_AT='oduClientCtpFacDMPELatencyMode'
_AS='oduClientCtpDetectedPayloadType'
_AR='oduClientCtpTermPrbsMonMode'
_AQ='oduClientCtpTermPrbsGenMode'
_AP='oduClientCtpFacPrbsMonMode'
_AO='oduClientCtpFacPrbsGenMode'
_AN='oduClientCtpFacSDThreshold'
_AM='oduClientCtpLoopBack'
_AL='oduClientCtpExpectedPayload'
_AK='oduClientCtpTsg'
_AJ='oduClientCtpSupportingTP'
_AI='oduClientCtpCrossConnectType'
_AH='oduClientCtpdatarate'
_AG='oduClientCtpavailableOPUTributarySlots'
_AF='oduClientCtpsupportingOPUTributarySlots'
_AE='oduClientCtpuserConfigured'
_AD='oduClientCtpDetectedTPNs'
_AC='oduClientCtpExpectedTPNs'
_AB='oduClientCtpTributaryPortNumber'
_AA='oduClientCtprate'
_A9='oduClientCtpTSCount'
_A8='oduClientCtpTermMonitoringMode'
_A7='oduClientCtpTxBei15MinutesTceReporting'
_A6='oduClientCtpTxBeiDayTceReporting'
_A5='oduClientCtpRxBei15MinutesTceReporting'
_A4='oduClientCtpRxBeiDayTceReporting'
_A3='oduClientCtpTxBeiDayTce'
_A2='oduClientCtpRxBeiDayTce'
_A1='oduClientCtpTxBei15MinutesTce'
_A0='oduClientCtpRxBei15MinutesTce'
_z='oduClientCtpTermDSThreshold'
_y='oduClientCtpFacDSThreshold'
_x='oduClientCtpSupportingCircuitIdList'
_w='oduClientCtpAlarmReportControl'
_v='oduClientCtpTermPmHistStatsEnable'
_u='oduClientCtpFacPmHistStatsEnable'
_t='oduClientCtpTamType'
_s='oduClientCtpConfiguredServiceType'
_r='oduClientCtpTcmList'
_q='oduClientCtpTermTimDetMode'
_p='oduClientCtpFacTimDetMode'
_o='oduClientCtpTxDs15MinutesTceReporting'
_n='oduClientCtpTxDsDayTceReporting'
_m='oduClientCtpRxDs15MinutesTceReporting'
_l='oduClientCtpRxDsDayTceReporting'
_k='oduClientCtpTxEb15MinutesTceReporting'
_j='oduClientCtpTxEbDayTceReporting'
_i='oduClientCtpRxEb15MinutesTceReporting'
_h='oduClientCtpRxEbDayTceReporting'
_g='oduClientCtpTxDsDayTce'
_f='oduClientCtpRxDsDayTce'
_e='oduClientCtpTxDs15MinutesTce'
_d='oduClientCtpRxDs15MinutesTce'
_c='oduClientCtpTxEbDayTce'
_b='oduClientCtpRxEbDayTce'
_a='oduClientCtpTxEb15MinutesTce'
_Z='oduClientCtpRxEb15MinutesTce'
_Y='oduClientCtpTermReceivedTTI'
_X='oduClientCtpFacReceivedTTI'
_W='oduClientCtpTermExpectedDAPI'
_V='oduClientCtpTermExpectedSAPI'
_U='oduClientCtpTermTxTTI'
_T='oduClientCtpFacExpectedDAPI'
_S='oduClientCtpFacExpectedSAPI'
_R='oduClientCtpFacTxTTI'
_Q='oduClientCtpFacMonitoringMode'
_P='oduClientCtpServiceMode'
_O='obsolete'
_N='sapidapi'
_M='InfnServiceMode'
_L='InfnSMQ'
_K='InfnArc'
_J='ifIndex'
_I='IF-MIB'
_H='InfnEnableDisable'
_G='DisplayString'
_F='TruthValue'
_E='read-only'
_D='Integer32'
_C='read-write'
_B='INFINERA-TP-ODUCLIENTCTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_I,_J)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
FloatTenths,InfnArc,InfnEnableDisable,InfnEqptType,InfnMonitoringMode,InfnNwLatencyMeasurementMode,InfnRate,InfnSMQ,InfnServiceMode,InfnServiceType,InfnTcmList,InfnTsgType,InfnXconType=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatTenths',_K,_H,'InfnEqptType','InfnMonitoringMode','InfnNwLatencyMeasurementMode','InfnRate',_L,_M,'InfnServiceType','InfnTcmList','InfnTsgType','InfnXconType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention',_F)
oduClientCtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,23))
if mibBuilder.loadTexts:oduClientCtpMIB.setRevisions(('2009-07-20 00:00',))
_OduClientCtpTable_Object=MibTable
oduClientCtpTable=_OduClientCtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1))
if mibBuilder.loadTexts:oduClientCtpTable.setStatus(_A)
_OduClientCtpEntry_Object=MibTableRow
oduClientCtpEntry=_OduClientCtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1))
oduClientCtpEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:oduClientCtpEntry.setStatus(_A)
class _OduClientCtpServiceMode_Type(InfnServiceMode):defaultValue=1
_OduClientCtpServiceMode_Type.__name__=_M
_OduClientCtpServiceMode_Object=MibTableColumn
oduClientCtpServiceMode=_OduClientCtpServiceMode_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,1),_OduClientCtpServiceMode_Type())
oduClientCtpServiceMode.setMaxAccess(_E)
if mibBuilder.loadTexts:oduClientCtpServiceMode.setStatus(_A)
class _OduClientCtpServiceModeQualifier_Type(InfnSMQ):defaultValue=1
_OduClientCtpServiceModeQualifier_Type.__name__=_L
_OduClientCtpServiceModeQualifier_Object=MibTableColumn
oduClientCtpServiceModeQualifier=_OduClientCtpServiceModeQualifier_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,2),_OduClientCtpServiceModeQualifier_Type())
oduClientCtpServiceModeQualifier.setMaxAccess(_E)
if mibBuilder.loadTexts:oduClientCtpServiceModeQualifier.setStatus(_A)
_OduClientCtpFacMonitoringMode_Type=InfnMonitoringMode
_OduClientCtpFacMonitoringMode_Object=MibTableColumn
oduClientCtpFacMonitoringMode=_OduClientCtpFacMonitoringMode_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,3),_OduClientCtpFacMonitoringMode_Type())
oduClientCtpFacMonitoringMode.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpFacMonitoringMode.setStatus(_A)
class _OduClientCtpFacTxTTI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_OduClientCtpFacTxTTI_Type.__name__=_G
_OduClientCtpFacTxTTI_Object=MibTableColumn
oduClientCtpFacTxTTI=_OduClientCtpFacTxTTI_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,4),_OduClientCtpFacTxTTI_Type())
oduClientCtpFacTxTTI.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpFacTxTTI.setStatus(_A)
class _OduClientCtpFacExpectedSAPI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_OduClientCtpFacExpectedSAPI_Type.__name__=_G
_OduClientCtpFacExpectedSAPI_Object=MibTableColumn
oduClientCtpFacExpectedSAPI=_OduClientCtpFacExpectedSAPI_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,5),_OduClientCtpFacExpectedSAPI_Type())
oduClientCtpFacExpectedSAPI.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpFacExpectedSAPI.setStatus(_A)
class _OduClientCtpFacExpectedDAPI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_OduClientCtpFacExpectedDAPI_Type.__name__=_G
_OduClientCtpFacExpectedDAPI_Object=MibTableColumn
oduClientCtpFacExpectedDAPI=_OduClientCtpFacExpectedDAPI_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,6),_OduClientCtpFacExpectedDAPI_Type())
oduClientCtpFacExpectedDAPI.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpFacExpectedDAPI.setStatus(_A)
class _OduClientCtpTermTxTTI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_OduClientCtpTermTxTTI_Type.__name__=_G
_OduClientCtpTermTxTTI_Object=MibTableColumn
oduClientCtpTermTxTTI=_OduClientCtpTermTxTTI_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,7),_OduClientCtpTermTxTTI_Type())
oduClientCtpTermTxTTI.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpTermTxTTI.setStatus(_A)
class _OduClientCtpTermExpectedSAPI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_OduClientCtpTermExpectedSAPI_Type.__name__=_G
_OduClientCtpTermExpectedSAPI_Object=MibTableColumn
oduClientCtpTermExpectedSAPI=_OduClientCtpTermExpectedSAPI_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,8),_OduClientCtpTermExpectedSAPI_Type())
oduClientCtpTermExpectedSAPI.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpTermExpectedSAPI.setStatus(_A)
class _OduClientCtpTermExpectedDAPI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_OduClientCtpTermExpectedDAPI_Type.__name__=_G
_OduClientCtpTermExpectedDAPI_Object=MibTableColumn
oduClientCtpTermExpectedDAPI=_OduClientCtpTermExpectedDAPI_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,9),_OduClientCtpTermExpectedDAPI_Type())
oduClientCtpTermExpectedDAPI.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpTermExpectedDAPI.setStatus(_A)
class _OduClientCtpFacReceivedTTI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_OduClientCtpFacReceivedTTI_Type.__name__=_G
_OduClientCtpFacReceivedTTI_Object=MibTableColumn
oduClientCtpFacReceivedTTI=_OduClientCtpFacReceivedTTI_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,10),_OduClientCtpFacReceivedTTI_Type())
oduClientCtpFacReceivedTTI.setMaxAccess(_E)
if mibBuilder.loadTexts:oduClientCtpFacReceivedTTI.setStatus(_A)
class _OduClientCtpTermReceivedTTI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_OduClientCtpTermReceivedTTI_Type.__name__=_G
_OduClientCtpTermReceivedTTI_Object=MibTableColumn
oduClientCtpTermReceivedTTI=_OduClientCtpTermReceivedTTI_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,11),_OduClientCtpTermReceivedTTI_Type())
oduClientCtpTermReceivedTTI.setMaxAccess(_E)
if mibBuilder.loadTexts:oduClientCtpTermReceivedTTI.setStatus(_A)
class _OduClientCtpRxEb15MinutesTce_Type(Integer32):defaultValue=1500
_OduClientCtpRxEb15MinutesTce_Type.__name__=_D
_OduClientCtpRxEb15MinutesTce_Object=MibTableColumn
oduClientCtpRxEb15MinutesTce=_OduClientCtpRxEb15MinutesTce_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,12),_OduClientCtpRxEb15MinutesTce_Type())
oduClientCtpRxEb15MinutesTce.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpRxEb15MinutesTce.setStatus(_A)
class _OduClientCtpTxEb15MinutesTce_Type(Integer32):defaultValue=1500
_OduClientCtpTxEb15MinutesTce_Type.__name__=_D
_OduClientCtpTxEb15MinutesTce_Object=MibTableColumn
oduClientCtpTxEb15MinutesTce=_OduClientCtpTxEb15MinutesTce_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,13),_OduClientCtpTxEb15MinutesTce_Type())
oduClientCtpTxEb15MinutesTce.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpTxEb15MinutesTce.setStatus(_A)
class _OduClientCtpRxEbDayTce_Type(Integer32):defaultValue=15000
_OduClientCtpRxEbDayTce_Type.__name__=_D
_OduClientCtpRxEbDayTce_Object=MibTableColumn
oduClientCtpRxEbDayTce=_OduClientCtpRxEbDayTce_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,14),_OduClientCtpRxEbDayTce_Type())
oduClientCtpRxEbDayTce.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpRxEbDayTce.setStatus(_A)
class _OduClientCtpTxEbDayTce_Type(Integer32):defaultValue=15000
_OduClientCtpTxEbDayTce_Type.__name__=_D
_OduClientCtpTxEbDayTce_Object=MibTableColumn
oduClientCtpTxEbDayTce=_OduClientCtpTxEbDayTce_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,15),_OduClientCtpTxEbDayTce_Type())
oduClientCtpTxEbDayTce.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpTxEbDayTce.setStatus(_A)
class _OduClientCtpRxDs15MinutesTce_Type(Integer32):defaultValue=120
_OduClientCtpRxDs15MinutesTce_Type.__name__=_D
_OduClientCtpRxDs15MinutesTce_Object=MibTableColumn
oduClientCtpRxDs15MinutesTce=_OduClientCtpRxDs15MinutesTce_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,16),_OduClientCtpRxDs15MinutesTce_Type())
oduClientCtpRxDs15MinutesTce.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpRxDs15MinutesTce.setStatus(_A)
class _OduClientCtpTxDs15MinutesTce_Type(Integer32):defaultValue=120
_OduClientCtpTxDs15MinutesTce_Type.__name__=_D
_OduClientCtpTxDs15MinutesTce_Object=MibTableColumn
oduClientCtpTxDs15MinutesTce=_OduClientCtpTxDs15MinutesTce_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,17),_OduClientCtpTxDs15MinutesTce_Type())
oduClientCtpTxDs15MinutesTce.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpTxDs15MinutesTce.setStatus(_A)
class _OduClientCtpRxDsDayTce_Type(Integer32):defaultValue=1200
_OduClientCtpRxDsDayTce_Type.__name__=_D
_OduClientCtpRxDsDayTce_Object=MibTableColumn
oduClientCtpRxDsDayTce=_OduClientCtpRxDsDayTce_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,18),_OduClientCtpRxDsDayTce_Type())
oduClientCtpRxDsDayTce.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpRxDsDayTce.setStatus(_A)
class _OduClientCtpTxDsDayTce_Type(Integer32):defaultValue=1200
_OduClientCtpTxDsDayTce_Type.__name__=_D
_OduClientCtpTxDsDayTce_Object=MibTableColumn
oduClientCtpTxDsDayTce=_OduClientCtpTxDsDayTce_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,19),_OduClientCtpTxDsDayTce_Type())
oduClientCtpTxDsDayTce.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpTxDsDayTce.setStatus(_A)
class _OduClientCtpRxEbDayTceReporting_Type(TruthValue):defaultValue=2
_OduClientCtpRxEbDayTceReporting_Type.__name__=_F
_OduClientCtpRxEbDayTceReporting_Object=MibTableColumn
oduClientCtpRxEbDayTceReporting=_OduClientCtpRxEbDayTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,20),_OduClientCtpRxEbDayTceReporting_Type())
oduClientCtpRxEbDayTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpRxEbDayTceReporting.setStatus(_A)
class _OduClientCtpRxEb15MinutesTceReporting_Type(TruthValue):defaultValue=2
_OduClientCtpRxEb15MinutesTceReporting_Type.__name__=_F
_OduClientCtpRxEb15MinutesTceReporting_Object=MibTableColumn
oduClientCtpRxEb15MinutesTceReporting=_OduClientCtpRxEb15MinutesTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,21),_OduClientCtpRxEb15MinutesTceReporting_Type())
oduClientCtpRxEb15MinutesTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpRxEb15MinutesTceReporting.setStatus(_A)
class _OduClientCtpTxEbDayTceReporting_Type(TruthValue):defaultValue=2
_OduClientCtpTxEbDayTceReporting_Type.__name__=_F
_OduClientCtpTxEbDayTceReporting_Object=MibTableColumn
oduClientCtpTxEbDayTceReporting=_OduClientCtpTxEbDayTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,22),_OduClientCtpTxEbDayTceReporting_Type())
oduClientCtpTxEbDayTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpTxEbDayTceReporting.setStatus(_A)
class _OduClientCtpTxEb15MinutesTceReporting_Type(TruthValue):defaultValue=2
_OduClientCtpTxEb15MinutesTceReporting_Type.__name__=_F
_OduClientCtpTxEb15MinutesTceReporting_Object=MibTableColumn
oduClientCtpTxEb15MinutesTceReporting=_OduClientCtpTxEb15MinutesTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,23),_OduClientCtpTxEb15MinutesTceReporting_Type())
oduClientCtpTxEb15MinutesTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpTxEb15MinutesTceReporting.setStatus(_A)
class _OduClientCtpRxDsDayTceReporting_Type(TruthValue):defaultValue=2
_OduClientCtpRxDsDayTceReporting_Type.__name__=_F
_OduClientCtpRxDsDayTceReporting_Object=MibTableColumn
oduClientCtpRxDsDayTceReporting=_OduClientCtpRxDsDayTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,24),_OduClientCtpRxDsDayTceReporting_Type())
oduClientCtpRxDsDayTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpRxDsDayTceReporting.setStatus(_A)
class _OduClientCtpRxDs15MinutesTceReporting_Type(TruthValue):defaultValue=2
_OduClientCtpRxDs15MinutesTceReporting_Type.__name__=_F
_OduClientCtpRxDs15MinutesTceReporting_Object=MibTableColumn
oduClientCtpRxDs15MinutesTceReporting=_OduClientCtpRxDs15MinutesTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,25),_OduClientCtpRxDs15MinutesTceReporting_Type())
oduClientCtpRxDs15MinutesTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpRxDs15MinutesTceReporting.setStatus(_A)
class _OduClientCtpTxDsDayTceReporting_Type(TruthValue):defaultValue=2
_OduClientCtpTxDsDayTceReporting_Type.__name__=_F
_OduClientCtpTxDsDayTceReporting_Object=MibTableColumn
oduClientCtpTxDsDayTceReporting=_OduClientCtpTxDsDayTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,26),_OduClientCtpTxDsDayTceReporting_Type())
oduClientCtpTxDsDayTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpTxDsDayTceReporting.setStatus(_A)
class _OduClientCtpTxDs15MinutesTceReporting_Type(TruthValue):defaultValue=2
_OduClientCtpTxDs15MinutesTceReporting_Type.__name__=_F
_OduClientCtpTxDs15MinutesTceReporting_Object=MibTableColumn
oduClientCtpTxDs15MinutesTceReporting=_OduClientCtpTxDs15MinutesTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,27),_OduClientCtpTxDs15MinutesTceReporting_Type())
oduClientCtpTxDs15MinutesTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpTxDs15MinutesTceReporting.setStatus(_A)
class _OduClientCtpFacTimDetMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('off',1),('sapi',2),('dapi',3),(_N,4)))
_OduClientCtpFacTimDetMode_Type.__name__=_D
_OduClientCtpFacTimDetMode_Object=MibTableColumn
oduClientCtpFacTimDetMode=_OduClientCtpFacTimDetMode_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,28),_OduClientCtpFacTimDetMode_Type())
oduClientCtpFacTimDetMode.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpFacTimDetMode.setStatus(_A)
class _OduClientCtpTermTimDetMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('off',1),('sapi',2),('dapi',3),(_N,4)))
_OduClientCtpTermTimDetMode_Type.__name__=_D
_OduClientCtpTermTimDetMode_Object=MibTableColumn
oduClientCtpTermTimDetMode=_OduClientCtpTermTimDetMode_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,29),_OduClientCtpTermTimDetMode_Type())
oduClientCtpTermTimDetMode.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpTermTimDetMode.setStatus(_A)
_OduClientCtpTcmList_Type=InfnTcmList
_OduClientCtpTcmList_Object=MibTableColumn
oduClientCtpTcmList=_OduClientCtpTcmList_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,30),_OduClientCtpTcmList_Type())
oduClientCtpTcmList.setMaxAccess(_E)
if mibBuilder.loadTexts:oduClientCtpTcmList.setStatus(_A)
_OduClientCtpConfiguredServiceType_Type=InfnServiceType
_OduClientCtpConfiguredServiceType_Object=MibTableColumn
oduClientCtpConfiguredServiceType=_OduClientCtpConfiguredServiceType_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,31),_OduClientCtpConfiguredServiceType_Type())
oduClientCtpConfiguredServiceType.setMaxAccess(_E)
if mibBuilder.loadTexts:oduClientCtpConfiguredServiceType.setStatus(_A)
_OduClientCtpTamType_Type=InfnEqptType
_OduClientCtpTamType_Object=MibTableColumn
oduClientCtpTamType=_OduClientCtpTamType_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,32),_OduClientCtpTamType_Type())
oduClientCtpTamType.setMaxAccess(_E)
if mibBuilder.loadTexts:oduClientCtpTamType.setStatus(_O)
class _OduClientCtpFacPmHistStatsEnable_Type(InfnEnableDisable):defaultValue=2
_OduClientCtpFacPmHistStatsEnable_Type.__name__=_H
_OduClientCtpFacPmHistStatsEnable_Object=MibTableColumn
oduClientCtpFacPmHistStatsEnable=_OduClientCtpFacPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,33),_OduClientCtpFacPmHistStatsEnable_Type())
oduClientCtpFacPmHistStatsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpFacPmHistStatsEnable.setStatus(_A)
class _OduClientCtpTermPmHistStatsEnable_Type(InfnEnableDisable):defaultValue=2
_OduClientCtpTermPmHistStatsEnable_Type.__name__=_H
_OduClientCtpTermPmHistStatsEnable_Object=MibTableColumn
oduClientCtpTermPmHistStatsEnable=_OduClientCtpTermPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,34),_OduClientCtpTermPmHistStatsEnable_Type())
oduClientCtpTermPmHistStatsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpTermPmHistStatsEnable.setStatus(_A)
class _OduClientCtpAlarmReportControl_Type(InfnArc):defaultValue=1
_OduClientCtpAlarmReportControl_Type.__name__=_K
_OduClientCtpAlarmReportControl_Object=MibTableColumn
oduClientCtpAlarmReportControl=_OduClientCtpAlarmReportControl_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,35),_OduClientCtpAlarmReportControl_Type())
oduClientCtpAlarmReportControl.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpAlarmReportControl.setStatus(_A)
_OduClientCtpSupportingCircuitIdList_Type=DisplayString
_OduClientCtpSupportingCircuitIdList_Object=MibTableColumn
oduClientCtpSupportingCircuitIdList=_OduClientCtpSupportingCircuitIdList_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,36),_OduClientCtpSupportingCircuitIdList_Type())
oduClientCtpSupportingCircuitIdList.setMaxAccess(_E)
if mibBuilder.loadTexts:oduClientCtpSupportingCircuitIdList.setStatus(_A)
class _OduClientCtpFacDSThreshold_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_OduClientCtpFacDSThreshold_Type.__name__=_D
_OduClientCtpFacDSThreshold_Object=MibTableColumn
oduClientCtpFacDSThreshold=_OduClientCtpFacDSThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,37),_OduClientCtpFacDSThreshold_Type())
oduClientCtpFacDSThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpFacDSThreshold.setStatus(_A)
class _OduClientCtpTermDSThreshold_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_OduClientCtpTermDSThreshold_Type.__name__=_D
_OduClientCtpTermDSThreshold_Object=MibTableColumn
oduClientCtpTermDSThreshold=_OduClientCtpTermDSThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,38),_OduClientCtpTermDSThreshold_Type())
oduClientCtpTermDSThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpTermDSThreshold.setStatus(_A)
_OduClientCtpTermMonitoringMode_Type=InfnMonitoringMode
_OduClientCtpTermMonitoringMode_Object=MibTableColumn
oduClientCtpTermMonitoringMode=_OduClientCtpTermMonitoringMode_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,39),_OduClientCtpTermMonitoringMode_Type())
oduClientCtpTermMonitoringMode.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpTermMonitoringMode.setStatus(_A)
class _OduClientCtpRxBei15MinutesTce_Type(Integer32):defaultValue=1500
_OduClientCtpRxBei15MinutesTce_Type.__name__=_D
_OduClientCtpRxBei15MinutesTce_Object=MibTableColumn
oduClientCtpRxBei15MinutesTce=_OduClientCtpRxBei15MinutesTce_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,40),_OduClientCtpRxBei15MinutesTce_Type())
oduClientCtpRxBei15MinutesTce.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpRxBei15MinutesTce.setStatus(_A)
class _OduClientCtpTxBei15MinutesTce_Type(Integer32):defaultValue=1500
_OduClientCtpTxBei15MinutesTce_Type.__name__=_D
_OduClientCtpTxBei15MinutesTce_Object=MibTableColumn
oduClientCtpTxBei15MinutesTce=_OduClientCtpTxBei15MinutesTce_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,41),_OduClientCtpTxBei15MinutesTce_Type())
oduClientCtpTxBei15MinutesTce.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpTxBei15MinutesTce.setStatus(_A)
class _OduClientCtpRxBeiDayTce_Type(Integer32):defaultValue=15000
_OduClientCtpRxBeiDayTce_Type.__name__=_D
_OduClientCtpRxBeiDayTce_Object=MibTableColumn
oduClientCtpRxBeiDayTce=_OduClientCtpRxBeiDayTce_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,42),_OduClientCtpRxBeiDayTce_Type())
oduClientCtpRxBeiDayTce.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpRxBeiDayTce.setStatus(_A)
class _OduClientCtpTxBeiDayTce_Type(Integer32):defaultValue=15000
_OduClientCtpTxBeiDayTce_Type.__name__=_D
_OduClientCtpTxBeiDayTce_Object=MibTableColumn
oduClientCtpTxBeiDayTce=_OduClientCtpTxBeiDayTce_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,43),_OduClientCtpTxBeiDayTce_Type())
oduClientCtpTxBeiDayTce.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpTxBeiDayTce.setStatus(_A)
class _OduClientCtpRxBeiDayTceReporting_Type(TruthValue):defaultValue=2
_OduClientCtpRxBeiDayTceReporting_Type.__name__=_F
_OduClientCtpRxBeiDayTceReporting_Object=MibTableColumn
oduClientCtpRxBeiDayTceReporting=_OduClientCtpRxBeiDayTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,44),_OduClientCtpRxBeiDayTceReporting_Type())
oduClientCtpRxBeiDayTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpRxBeiDayTceReporting.setStatus(_A)
class _OduClientCtpRxBei15MinutesTceReporting_Type(TruthValue):defaultValue=2
_OduClientCtpRxBei15MinutesTceReporting_Type.__name__=_F
_OduClientCtpRxBei15MinutesTceReporting_Object=MibTableColumn
oduClientCtpRxBei15MinutesTceReporting=_OduClientCtpRxBei15MinutesTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,45),_OduClientCtpRxBei15MinutesTceReporting_Type())
oduClientCtpRxBei15MinutesTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpRxBei15MinutesTceReporting.setStatus(_A)
class _OduClientCtpTxBeiDayTceReporting_Type(TruthValue):defaultValue=2
_OduClientCtpTxBeiDayTceReporting_Type.__name__=_F
_OduClientCtpTxBeiDayTceReporting_Object=MibTableColumn
oduClientCtpTxBeiDayTceReporting=_OduClientCtpTxBeiDayTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,46),_OduClientCtpTxBeiDayTceReporting_Type())
oduClientCtpTxBeiDayTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpTxBeiDayTceReporting.setStatus(_A)
class _OduClientCtpTxBei15MinutesTceReporting_Type(TruthValue):defaultValue=2
_OduClientCtpTxBei15MinutesTceReporting_Type.__name__=_F
_OduClientCtpTxBei15MinutesTceReporting_Object=MibTableColumn
oduClientCtpTxBei15MinutesTceReporting=_OduClientCtpTxBei15MinutesTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,47),_OduClientCtpTxBei15MinutesTceReporting_Type())
oduClientCtpTxBei15MinutesTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpTxBei15MinutesTceReporting.setStatus(_A)
_OduClientCtpTSCount_Type=Integer32
_OduClientCtpTSCount_Object=MibTableColumn
oduClientCtpTSCount=_OduClientCtpTSCount_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,48),_OduClientCtpTSCount_Type())
oduClientCtpTSCount.setMaxAccess(_E)
if mibBuilder.loadTexts:oduClientCtpTSCount.setStatus(_A)
_OduClientCtprate_Type=DisplayString
_OduClientCtprate_Object=MibTableColumn
oduClientCtprate=_OduClientCtprate_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,49),_OduClientCtprate_Type())
oduClientCtprate.setMaxAccess(_E)
if mibBuilder.loadTexts:oduClientCtprate.setStatus(_A)
_OduClientCtpTributaryPortNumber_Type=Integer32
_OduClientCtpTributaryPortNumber_Object=MibTableColumn
oduClientCtpTributaryPortNumber=_OduClientCtpTributaryPortNumber_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,50),_OduClientCtpTributaryPortNumber_Type())
oduClientCtpTributaryPortNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:oduClientCtpTributaryPortNumber.setStatus(_A)
_OduClientCtpExpectedTPNs_Type=Integer32
_OduClientCtpExpectedTPNs_Object=MibTableColumn
oduClientCtpExpectedTPNs=_OduClientCtpExpectedTPNs_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,51),_OduClientCtpExpectedTPNs_Type())
oduClientCtpExpectedTPNs.setMaxAccess(_E)
if mibBuilder.loadTexts:oduClientCtpExpectedTPNs.setStatus(_A)
_OduClientCtpDetectedTPNs_Type=Integer32
_OduClientCtpDetectedTPNs_Object=MibTableColumn
oduClientCtpDetectedTPNs=_OduClientCtpDetectedTPNs_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,52),_OduClientCtpDetectedTPNs_Type())
oduClientCtpDetectedTPNs.setMaxAccess(_E)
if mibBuilder.loadTexts:oduClientCtpDetectedTPNs.setStatus(_A)
_OduClientCtpuserConfigured_Type=TruthValue
_OduClientCtpuserConfigured_Object=MibTableColumn
oduClientCtpuserConfigured=_OduClientCtpuserConfigured_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,53),_OduClientCtpuserConfigured_Type())
oduClientCtpuserConfigured.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpuserConfigured.setStatus(_O)
_OduClientCtpsupportingOPUTributarySlots_Type=DisplayString
_OduClientCtpsupportingOPUTributarySlots_Object=MibTableColumn
oduClientCtpsupportingOPUTributarySlots=_OduClientCtpsupportingOPUTributarySlots_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,54),_OduClientCtpsupportingOPUTributarySlots_Type())
oduClientCtpsupportingOPUTributarySlots.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpsupportingOPUTributarySlots.setStatus(_A)
_OduClientCtpavailableOPUTributarySlots_Type=DisplayString
_OduClientCtpavailableOPUTributarySlots_Object=MibTableColumn
oduClientCtpavailableOPUTributarySlots=_OduClientCtpavailableOPUTributarySlots_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,55),_OduClientCtpavailableOPUTributarySlots_Type())
oduClientCtpavailableOPUTributarySlots.setMaxAccess(_E)
if mibBuilder.loadTexts:oduClientCtpavailableOPUTributarySlots.setStatus(_A)
_OduClientCtpdatarate_Type=InfnRate
_OduClientCtpdatarate_Object=MibTableColumn
oduClientCtpdatarate=_OduClientCtpdatarate_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,56),_OduClientCtpdatarate_Type())
oduClientCtpdatarate.setMaxAccess(_E)
if mibBuilder.loadTexts:oduClientCtpdatarate.setStatus(_A)
_OduClientCtpCrossConnectType_Type=InfnXconType
_OduClientCtpCrossConnectType_Object=MibTableColumn
oduClientCtpCrossConnectType=_OduClientCtpCrossConnectType_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,57),_OduClientCtpCrossConnectType_Type())
oduClientCtpCrossConnectType.setMaxAccess(_E)
if mibBuilder.loadTexts:oduClientCtpCrossConnectType.setStatus(_A)
_OduClientCtpSupportingTP_Type=DisplayString
_OduClientCtpSupportingTP_Object=MibTableColumn
oduClientCtpSupportingTP=_OduClientCtpSupportingTP_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,58),_OduClientCtpSupportingTP_Type())
oduClientCtpSupportingTP.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpSupportingTP.setStatus(_A)
_OduClientCtpTsg_Type=InfnTsgType
_OduClientCtpTsg_Object=MibTableColumn
oduClientCtpTsg=_OduClientCtpTsg_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,59),_OduClientCtpTsg_Type())
oduClientCtpTsg.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpTsg.setStatus(_A)
_OduClientCtpExpectedPayload_Type=InfnServiceType
_OduClientCtpExpectedPayload_Object=MibTableColumn
oduClientCtpExpectedPayload=_OduClientCtpExpectedPayload_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,60),_OduClientCtpExpectedPayload_Type())
oduClientCtpExpectedPayload.setMaxAccess(_E)
if mibBuilder.loadTexts:oduClientCtpExpectedPayload.setStatus(_A)
class _OduClientCtpLoopBack_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('terminal',2),('facility',3)))
_OduClientCtpLoopBack_Type.__name__=_D
_OduClientCtpLoopBack_Object=MibTableColumn
oduClientCtpLoopBack=_OduClientCtpLoopBack_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,61),_OduClientCtpLoopBack_Type())
oduClientCtpLoopBack.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpLoopBack.setStatus(_A)
class _OduClientCtpFacSDThreshold_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_OduClientCtpFacSDThreshold_Type.__name__=_D
_OduClientCtpFacSDThreshold_Object=MibTableColumn
oduClientCtpFacSDThreshold=_OduClientCtpFacSDThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,62),_OduClientCtpFacSDThreshold_Type())
oduClientCtpFacSDThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpFacSDThreshold.setStatus(_A)
_OduClientCtpFacPrbsGenMode_Type=InfnEnableDisable
_OduClientCtpFacPrbsGenMode_Object=MibTableColumn
oduClientCtpFacPrbsGenMode=_OduClientCtpFacPrbsGenMode_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,63),_OduClientCtpFacPrbsGenMode_Type())
oduClientCtpFacPrbsGenMode.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpFacPrbsGenMode.setStatus(_A)
_OduClientCtpFacPrbsMonMode_Type=InfnEnableDisable
_OduClientCtpFacPrbsMonMode_Object=MibTableColumn
oduClientCtpFacPrbsMonMode=_OduClientCtpFacPrbsMonMode_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,64),_OduClientCtpFacPrbsMonMode_Type())
oduClientCtpFacPrbsMonMode.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpFacPrbsMonMode.setStatus(_A)
_OduClientCtpTermPrbsGenMode_Type=InfnEnableDisable
_OduClientCtpTermPrbsGenMode_Object=MibTableColumn
oduClientCtpTermPrbsGenMode=_OduClientCtpTermPrbsGenMode_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,65),_OduClientCtpTermPrbsGenMode_Type())
oduClientCtpTermPrbsGenMode.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpTermPrbsGenMode.setStatus(_A)
_OduClientCtpTermPrbsMonMode_Type=InfnEnableDisable
_OduClientCtpTermPrbsMonMode_Object=MibTableColumn
oduClientCtpTermPrbsMonMode=_OduClientCtpTermPrbsMonMode_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,66),_OduClientCtpTermPrbsMonMode_Type())
oduClientCtpTermPrbsMonMode.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpTermPrbsMonMode.setStatus(_A)
_OduClientCtpDetectedPayloadType_Type=InfnServiceType
_OduClientCtpDetectedPayloadType_Object=MibTableColumn
oduClientCtpDetectedPayloadType=_OduClientCtpDetectedPayloadType_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,67),_OduClientCtpDetectedPayloadType_Type())
oduClientCtpDetectedPayloadType.setMaxAccess(_E)
if mibBuilder.loadTexts:oduClientCtpDetectedPayloadType.setStatus(_A)
_OduClientCtpFacDMPELatencyMode_Type=InfnNwLatencyMeasurementMode
_OduClientCtpFacDMPELatencyMode_Object=MibTableColumn
oduClientCtpFacDMPELatencyMode=_OduClientCtpFacDMPELatencyMode_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,68),_OduClientCtpFacDMPELatencyMode_Type())
oduClientCtpFacDMPELatencyMode.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpFacDMPELatencyMode.setStatus(_A)
_OduClientCtpFacDMPSLatencyMode_Type=InfnNwLatencyMeasurementMode
_OduClientCtpFacDMPSLatencyMode_Object=MibTableColumn
oduClientCtpFacDMPSLatencyMode=_OduClientCtpFacDMPSLatencyMode_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,69),_OduClientCtpFacDMPSLatencyMode_Type())
oduClientCtpFacDMPSLatencyMode.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpFacDMPSLatencyMode.setStatus(_A)
_OduClientCtpTermDMPELatencyMode_Type=InfnNwLatencyMeasurementMode
_OduClientCtpTermDMPELatencyMode_Object=MibTableColumn
oduClientCtpTermDMPELatencyMode=_OduClientCtpTermDMPELatencyMode_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,70),_OduClientCtpTermDMPELatencyMode_Type())
oduClientCtpTermDMPELatencyMode.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpTermDMPELatencyMode.setStatus(_A)
_OduClientCtpTermDMPSLatencyMode_Type=InfnNwLatencyMeasurementMode
_OduClientCtpTermDMPSLatencyMode_Object=MibTableColumn
oduClientCtpTermDMPSLatencyMode=_OduClientCtpTermDMPSLatencyMode_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,71),_OduClientCtpTermDMPSLatencyMode_Type())
oduClientCtpTermDMPSLatencyMode.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpTermDMPSLatencyMode.setStatus(_A)
_OduClientCtpFacDMPELatHighThreshold_Type=FloatTenths
_OduClientCtpFacDMPELatHighThreshold_Object=MibTableColumn
oduClientCtpFacDMPELatHighThreshold=_OduClientCtpFacDMPELatHighThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,72),_OduClientCtpFacDMPELatHighThreshold_Type())
oduClientCtpFacDMPELatHighThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpFacDMPELatHighThreshold.setStatus(_A)
_OduClientCtpFacDMPELatLowThreshold_Type=FloatTenths
_OduClientCtpFacDMPELatLowThreshold_Object=MibTableColumn
oduClientCtpFacDMPELatLowThreshold=_OduClientCtpFacDMPELatLowThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,73),_OduClientCtpFacDMPELatLowThreshold_Type())
oduClientCtpFacDMPELatLowThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpFacDMPELatLowThreshold.setStatus(_A)
_OduClientCtpTermDMPELatHighThreshold_Type=FloatTenths
_OduClientCtpTermDMPELatHighThreshold_Object=MibTableColumn
oduClientCtpTermDMPELatHighThreshold=_OduClientCtpTermDMPELatHighThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,74),_OduClientCtpTermDMPELatHighThreshold_Type())
oduClientCtpTermDMPELatHighThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpTermDMPELatHighThreshold.setStatus(_A)
_OduClientCtpTermDMPELatLowThreshold_Type=FloatTenths
_OduClientCtpTermDMPELatLowThreshold_Object=MibTableColumn
oduClientCtpTermDMPELatLowThreshold=_OduClientCtpTermDMPELatLowThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,75),_OduClientCtpTermDMPELatLowThreshold_Type())
oduClientCtpTermDMPELatLowThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpTermDMPELatLowThreshold.setStatus(_A)
_OduClientCtpFacDMPSLatHighThreshold_Type=FloatTenths
_OduClientCtpFacDMPSLatHighThreshold_Object=MibTableColumn
oduClientCtpFacDMPSLatHighThreshold=_OduClientCtpFacDMPSLatHighThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,76),_OduClientCtpFacDMPSLatHighThreshold_Type())
oduClientCtpFacDMPSLatHighThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpFacDMPSLatHighThreshold.setStatus(_A)
_OduClientCtpFacDMPSLatLowThreshold_Type=FloatTenths
_OduClientCtpFacDMPSLatLowThreshold_Object=MibTableColumn
oduClientCtpFacDMPSLatLowThreshold=_OduClientCtpFacDMPSLatLowThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,77),_OduClientCtpFacDMPSLatLowThreshold_Type())
oduClientCtpFacDMPSLatLowThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpFacDMPSLatLowThreshold.setStatus(_A)
_OduClientCtpTermDMPSLatHighThreshold_Type=FloatTenths
_OduClientCtpTermDMPSLatHighThreshold_Object=MibTableColumn
oduClientCtpTermDMPSLatHighThreshold=_OduClientCtpTermDMPSLatHighThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,78),_OduClientCtpTermDMPSLatHighThreshold_Type())
oduClientCtpTermDMPSLatHighThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpTermDMPSLatHighThreshold.setStatus(_A)
_OduClientCtpTermDMPSLatLowThreshold_Type=FloatTenths
_OduClientCtpTermDMPSLatLowThreshold_Object=MibTableColumn
oduClientCtpTermDMPSLatLowThreshold=_OduClientCtpTermDMPSLatLowThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,79),_OduClientCtpTermDMPSLatLowThreshold_Type())
oduClientCtpTermDMPSLatLowThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpTermDMPSLatLowThreshold.setStatus(_A)
_OduClientCtpDetectedTPNList_Type=DisplayString
_OduClientCtpDetectedTPNList_Object=MibTableColumn
oduClientCtpDetectedTPNList=_OduClientCtpDetectedTPNList_Object((1,3,6,1,4,1,21296,2,2,2,2,23,1,1,80),_OduClientCtpDetectedTPNList_Type())
oduClientCtpDetectedTPNList.setMaxAccess(_C)
if mibBuilder.loadTexts:oduClientCtpDetectedTPNList.setStatus(_A)
_OduClientCtpConformance_ObjectIdentity=ObjectIdentity
oduClientCtpConformance=_OduClientCtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,23,3))
_OduClientCtpCompliances_ObjectIdentity=ObjectIdentity
oduClientCtpCompliances=_OduClientCtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,23,3,1))
_OduClientCtpGroups_ObjectIdentity=ObjectIdentity
oduClientCtpGroups=_OduClientCtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,23,3,2))
oduClientCtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,23,3,2,1))
oduClientCtpGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af)))
if mibBuilder.loadTexts:oduClientCtpGroup.setStatus(_A)
oduClientCtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,23,3,1,1))
oduClientCtpCompliance.setObjects((_B,_Ag))
if mibBuilder.loadTexts:oduClientCtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'oduClientCtpMIB':oduClientCtpMIB,'oduClientCtpTable':oduClientCtpTable,'oduClientCtpEntry':oduClientCtpEntry,_P:oduClientCtpServiceMode,'oduClientCtpServiceModeQualifier':oduClientCtpServiceModeQualifier,_Q:oduClientCtpFacMonitoringMode,_R:oduClientCtpFacTxTTI,_S:oduClientCtpFacExpectedSAPI,_T:oduClientCtpFacExpectedDAPI,_U:oduClientCtpTermTxTTI,_V:oduClientCtpTermExpectedSAPI,_W:oduClientCtpTermExpectedDAPI,_X:oduClientCtpFacReceivedTTI,_Y:oduClientCtpTermReceivedTTI,_Z:oduClientCtpRxEb15MinutesTce,_a:oduClientCtpTxEb15MinutesTce,_b:oduClientCtpRxEbDayTce,_c:oduClientCtpTxEbDayTce,_d:oduClientCtpRxDs15MinutesTce,_e:oduClientCtpTxDs15MinutesTce,_f:oduClientCtpRxDsDayTce,_g:oduClientCtpTxDsDayTce,_h:oduClientCtpRxEbDayTceReporting,_i:oduClientCtpRxEb15MinutesTceReporting,_j:oduClientCtpTxEbDayTceReporting,_k:oduClientCtpTxEb15MinutesTceReporting,_l:oduClientCtpRxDsDayTceReporting,_m:oduClientCtpRxDs15MinutesTceReporting,_n:oduClientCtpTxDsDayTceReporting,_o:oduClientCtpTxDs15MinutesTceReporting,_p:oduClientCtpFacTimDetMode,_q:oduClientCtpTermTimDetMode,_r:oduClientCtpTcmList,_s:oduClientCtpConfiguredServiceType,_t:oduClientCtpTamType,_u:oduClientCtpFacPmHistStatsEnable,_v:oduClientCtpTermPmHistStatsEnable,_w:oduClientCtpAlarmReportControl,_x:oduClientCtpSupportingCircuitIdList,_y:oduClientCtpFacDSThreshold,_z:oduClientCtpTermDSThreshold,_A8:oduClientCtpTermMonitoringMode,_A0:oduClientCtpRxBei15MinutesTce,_A1:oduClientCtpTxBei15MinutesTce,_A2:oduClientCtpRxBeiDayTce,_A3:oduClientCtpTxBeiDayTce,_A4:oduClientCtpRxBeiDayTceReporting,_A5:oduClientCtpRxBei15MinutesTceReporting,_A6:oduClientCtpTxBeiDayTceReporting,_A7:oduClientCtpTxBei15MinutesTceReporting,_A9:oduClientCtpTSCount,_AA:oduClientCtprate,_AB:oduClientCtpTributaryPortNumber,_AC:oduClientCtpExpectedTPNs,_AD:oduClientCtpDetectedTPNs,_AE:oduClientCtpuserConfigured,_AF:oduClientCtpsupportingOPUTributarySlots,_AG:oduClientCtpavailableOPUTributarySlots,_AH:oduClientCtpdatarate,_AI:oduClientCtpCrossConnectType,_AJ:oduClientCtpSupportingTP,_AK:oduClientCtpTsg,_AL:oduClientCtpExpectedPayload,_AM:oduClientCtpLoopBack,_AN:oduClientCtpFacSDThreshold,_AO:oduClientCtpFacPrbsGenMode,_AP:oduClientCtpFacPrbsMonMode,_AQ:oduClientCtpTermPrbsGenMode,_AR:oduClientCtpTermPrbsMonMode,_AS:oduClientCtpDetectedPayloadType,_AT:oduClientCtpFacDMPELatencyMode,_AU:oduClientCtpFacDMPSLatencyMode,_AV:oduClientCtpTermDMPELatencyMode,_AW:oduClientCtpTermDMPSLatencyMode,_AX:oduClientCtpFacDMPELatHighThreshold,_AY:oduClientCtpFacDMPELatLowThreshold,_AZ:oduClientCtpTermDMPELatHighThreshold,_Aa:oduClientCtpTermDMPELatLowThreshold,_Ab:oduClientCtpFacDMPSLatHighThreshold,_Ac:oduClientCtpFacDMPSLatLowThreshold,_Ad:oduClientCtpTermDMPSLatHighThreshold,_Ae:oduClientCtpTermDMPSLatLowThreshold,_Af:oduClientCtpDetectedTPNList,'oduClientCtpConformance':oduClientCtpConformance,'oduClientCtpCompliances':oduClientCtpCompliances,'oduClientCtpCompliance':oduClientCtpCompliance,'oduClientCtpGroups':oduClientCtpGroups,_Ag:oduClientCtpGroup})