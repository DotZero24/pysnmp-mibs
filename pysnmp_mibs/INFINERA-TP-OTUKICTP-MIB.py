_o='otukiCtpGroup'
_n='otukiCtpConfiguredServiceType'
_m='otukiCtpAlarmReportControl'
_l='otukiCtpRxDs15MinutesTceReporting'
_k='otukiCtpRxDsDayTceReporting'
_j='otukiCtpRxEb15MinutesTceReporting'
_i='otukiCtpRxEbDayTceReporting'
_h='otukiCtpRxDsDayTce'
_g='otukiCtpRxDs15MinutesTce'
_f='otukiCtpRxEbDayTce'
_e='otukiCtpRxEb15MinutesTce'
_d='otukiCtpSupportingOchList'
_c='otukiCtpFacTimDetMode'
_b='otukiCtpFacSDThreshold'
_a='otukiCtpFacDSThreshold'
_Z='otukiCtpFacMonitoringMode'
_Y='otukiCtpFacPmHistStatsEnable'
_X='otukiCtpFacRxTTI'
_W='otukiCtpFacExpectedDAPI'
_V='otukiCtpFacExpectedSAPI'
_U='otukiCtpFacTxTTI'
_T='otukiBitRateK'
_S='otukpropagationDelay'
_R='otukiFecDecoderIterationCount'
_Q='otukiCtpFecEnabled'
_P='otukiCtpFecCorrection'
_O='otukiCtpServiceModeQualifier'
_N='otukiCtpServiceMode'
_M='InfnServiceMode'
_L='InfnSMQ'
_K='InfnArc'
_J='ifIndex'
_I='IF-MIB'
_H='InfnEnableDisable'
_G='TruthValue'
_F='DisplayString'
_E='read-only'
_D='Integer32'
_C='read-write'
_B='INFINERA-TP-OTUKICTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_I,_J)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
FloatTenths,InfnArc,InfnEnableDisable,InfnEqptType,InfnMonitoringMode,InfnOtuBitRateK,InfnSMQ,InfnServiceMode,InfnServiceType=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatTenths',_K,_H,'InfnEqptType','InfnMonitoringMode','InfnOtuBitRateK',_L,_M,'InfnServiceType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention',_G)
otukiCtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,31))
if mibBuilder.loadTexts:otukiCtpMIB.setRevisions(('2009-04-20 00:00',))
_OtukiCtpTable_Object=MibTable
otukiCtpTable=_OtukiCtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,31,1))
if mibBuilder.loadTexts:otukiCtpTable.setStatus(_A)
_OtukiCtpEntry_Object=MibTableRow
otukiCtpEntry=_OtukiCtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,31,1,1))
otukiCtpEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:otukiCtpEntry.setStatus(_A)
class _OtukiCtpServiceMode_Type(InfnServiceMode):defaultValue=1
_OtukiCtpServiceMode_Type.__name__=_M
_OtukiCtpServiceMode_Object=MibTableColumn
otukiCtpServiceMode=_OtukiCtpServiceMode_Object((1,3,6,1,4,1,21296,2,2,2,2,31,1,1,1),_OtukiCtpServiceMode_Type())
otukiCtpServiceMode.setMaxAccess(_E)
if mibBuilder.loadTexts:otukiCtpServiceMode.setStatus(_A)
class _OtukiCtpServiceModeQualifier_Type(InfnSMQ):defaultValue=1
_OtukiCtpServiceModeQualifier_Type.__name__=_L
_OtukiCtpServiceModeQualifier_Object=MibTableColumn
otukiCtpServiceModeQualifier=_OtukiCtpServiceModeQualifier_Object((1,3,6,1,4,1,21296,2,2,2,2,31,1,1,2),_OtukiCtpServiceModeQualifier_Type())
otukiCtpServiceModeQualifier.setMaxAccess(_E)
if mibBuilder.loadTexts:otukiCtpServiceModeQualifier.setStatus(_A)
class _OtukiCtpFecCorrection_Type(InfnEnableDisable):defaultValue=2
_OtukiCtpFecCorrection_Type.__name__=_H
_OtukiCtpFecCorrection_Object=MibTableColumn
otukiCtpFecCorrection=_OtukiCtpFecCorrection_Object((1,3,6,1,4,1,21296,2,2,2,2,31,1,1,3),_OtukiCtpFecCorrection_Type())
otukiCtpFecCorrection.setMaxAccess(_C)
if mibBuilder.loadTexts:otukiCtpFecCorrection.setStatus(_A)
class _OtukiCtpFecEnabled_Type(InfnEnableDisable):defaultValue=2
_OtukiCtpFecEnabled_Type.__name__=_H
_OtukiCtpFecEnabled_Object=MibTableColumn
otukiCtpFecEnabled=_OtukiCtpFecEnabled_Object((1,3,6,1,4,1,21296,2,2,2,2,31,1,1,4),_OtukiCtpFecEnabled_Type())
otukiCtpFecEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:otukiCtpFecEnabled.setStatus(_A)
class _OtukiFecDecoderIterationCount_Type(Integer32):defaultValue=3
_OtukiFecDecoderIterationCount_Type.__name__=_D
_OtukiFecDecoderIterationCount_Object=MibTableColumn
otukiFecDecoderIterationCount=_OtukiFecDecoderIterationCount_Object((1,3,6,1,4,1,21296,2,2,2,2,31,1,1,5),_OtukiFecDecoderIterationCount_Type())
otukiFecDecoderIterationCount.setMaxAccess(_C)
if mibBuilder.loadTexts:otukiFecDecoderIterationCount.setStatus(_A)
_OtukpropagationDelay_Type=FloatTenths
_OtukpropagationDelay_Object=MibTableColumn
otukpropagationDelay=_OtukpropagationDelay_Object((1,3,6,1,4,1,21296,2,2,2,2,31,1,1,6),_OtukpropagationDelay_Type())
otukpropagationDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:otukpropagationDelay.setStatus(_A)
_OtukiBitRateK_Type=InfnOtuBitRateK
_OtukiBitRateK_Object=MibTableColumn
otukiBitRateK=_OtukiBitRateK_Object((1,3,6,1,4,1,21296,2,2,2,2,31,1,1,7),_OtukiBitRateK_Type())
otukiBitRateK.setMaxAccess(_E)
if mibBuilder.loadTexts:otukiBitRateK.setStatus(_A)
class _OtukiCtpFacTxTTI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_OtukiCtpFacTxTTI_Type.__name__=_F
_OtukiCtpFacTxTTI_Object=MibTableColumn
otukiCtpFacTxTTI=_OtukiCtpFacTxTTI_Object((1,3,6,1,4,1,21296,2,2,2,2,31,1,1,8),_OtukiCtpFacTxTTI_Type())
otukiCtpFacTxTTI.setMaxAccess(_C)
if mibBuilder.loadTexts:otukiCtpFacTxTTI.setStatus(_A)
class _OtukiCtpFacExpectedSAPI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_OtukiCtpFacExpectedSAPI_Type.__name__=_F
_OtukiCtpFacExpectedSAPI_Object=MibTableColumn
otukiCtpFacExpectedSAPI=_OtukiCtpFacExpectedSAPI_Object((1,3,6,1,4,1,21296,2,2,2,2,31,1,1,9),_OtukiCtpFacExpectedSAPI_Type())
otukiCtpFacExpectedSAPI.setMaxAccess(_C)
if mibBuilder.loadTexts:otukiCtpFacExpectedSAPI.setStatus(_A)
class _OtukiCtpFacExpectedDAPI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_OtukiCtpFacExpectedDAPI_Type.__name__=_F
_OtukiCtpFacExpectedDAPI_Object=MibTableColumn
otukiCtpFacExpectedDAPI=_OtukiCtpFacExpectedDAPI_Object((1,3,6,1,4,1,21296,2,2,2,2,31,1,1,10),_OtukiCtpFacExpectedDAPI_Type())
otukiCtpFacExpectedDAPI.setMaxAccess(_C)
if mibBuilder.loadTexts:otukiCtpFacExpectedDAPI.setStatus(_A)
class _OtukiCtpFacRxTTI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_OtukiCtpFacRxTTI_Type.__name__=_F
_OtukiCtpFacRxTTI_Object=MibTableColumn
otukiCtpFacRxTTI=_OtukiCtpFacRxTTI_Object((1,3,6,1,4,1,21296,2,2,2,2,31,1,1,11),_OtukiCtpFacRxTTI_Type())
otukiCtpFacRxTTI.setMaxAccess(_E)
if mibBuilder.loadTexts:otukiCtpFacRxTTI.setStatus(_A)
class _OtukiCtpFacPmHistStatsEnable_Type(InfnEnableDisable):defaultValue=2
_OtukiCtpFacPmHistStatsEnable_Type.__name__=_H
_OtukiCtpFacPmHistStatsEnable_Object=MibTableColumn
otukiCtpFacPmHistStatsEnable=_OtukiCtpFacPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,31,1,1,12),_OtukiCtpFacPmHistStatsEnable_Type())
otukiCtpFacPmHistStatsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:otukiCtpFacPmHistStatsEnable.setStatus(_A)
_OtukiCtpFacMonitoringMode_Type=InfnMonitoringMode
_OtukiCtpFacMonitoringMode_Object=MibTableColumn
otukiCtpFacMonitoringMode=_OtukiCtpFacMonitoringMode_Object((1,3,6,1,4,1,21296,2,2,2,2,31,1,1,13),_OtukiCtpFacMonitoringMode_Type())
otukiCtpFacMonitoringMode.setMaxAccess(_E)
if mibBuilder.loadTexts:otukiCtpFacMonitoringMode.setStatus(_A)
class _OtukiCtpFacDSThreshold_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_OtukiCtpFacDSThreshold_Type.__name__=_D
_OtukiCtpFacDSThreshold_Object=MibTableColumn
otukiCtpFacDSThreshold=_OtukiCtpFacDSThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,31,1,1,14),_OtukiCtpFacDSThreshold_Type())
otukiCtpFacDSThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:otukiCtpFacDSThreshold.setStatus(_A)
class _OtukiCtpFacSDThreshold_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_OtukiCtpFacSDThreshold_Type.__name__=_D
_OtukiCtpFacSDThreshold_Object=MibTableColumn
otukiCtpFacSDThreshold=_OtukiCtpFacSDThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,31,1,1,15),_OtukiCtpFacSDThreshold_Type())
otukiCtpFacSDThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:otukiCtpFacSDThreshold.setStatus(_A)
class _OtukiCtpFacTimDetMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('off',1),('sapi',2),('dapi',3),('sapidapi',4)))
_OtukiCtpFacTimDetMode_Type.__name__=_D
_OtukiCtpFacTimDetMode_Object=MibTableColumn
otukiCtpFacTimDetMode=_OtukiCtpFacTimDetMode_Object((1,3,6,1,4,1,21296,2,2,2,2,31,1,1,16),_OtukiCtpFacTimDetMode_Type())
otukiCtpFacTimDetMode.setMaxAccess(_C)
if mibBuilder.loadTexts:otukiCtpFacTimDetMode.setStatus(_A)
_OtukiCtpSupportingOchList_Type=DisplayString
_OtukiCtpSupportingOchList_Object=MibTableColumn
otukiCtpSupportingOchList=_OtukiCtpSupportingOchList_Object((1,3,6,1,4,1,21296,2,2,2,2,31,1,1,17),_OtukiCtpSupportingOchList_Type())
otukiCtpSupportingOchList.setMaxAccess(_E)
if mibBuilder.loadTexts:otukiCtpSupportingOchList.setStatus(_A)
class _OtukiCtpRxEb15MinutesTce_Type(Integer32):defaultValue=1500
_OtukiCtpRxEb15MinutesTce_Type.__name__=_D
_OtukiCtpRxEb15MinutesTce_Object=MibTableColumn
otukiCtpRxEb15MinutesTce=_OtukiCtpRxEb15MinutesTce_Object((1,3,6,1,4,1,21296,2,2,2,2,31,1,1,18),_OtukiCtpRxEb15MinutesTce_Type())
otukiCtpRxEb15MinutesTce.setMaxAccess(_C)
if mibBuilder.loadTexts:otukiCtpRxEb15MinutesTce.setStatus(_A)
class _OtukiCtpRxEbDayTce_Type(Integer32):defaultValue=15000
_OtukiCtpRxEbDayTce_Type.__name__=_D
_OtukiCtpRxEbDayTce_Object=MibTableColumn
otukiCtpRxEbDayTce=_OtukiCtpRxEbDayTce_Object((1,3,6,1,4,1,21296,2,2,2,2,31,1,1,19),_OtukiCtpRxEbDayTce_Type())
otukiCtpRxEbDayTce.setMaxAccess(_C)
if mibBuilder.loadTexts:otukiCtpRxEbDayTce.setStatus(_A)
class _OtukiCtpRxDs15MinutesTce_Type(Integer32):defaultValue=120
_OtukiCtpRxDs15MinutesTce_Type.__name__=_D
_OtukiCtpRxDs15MinutesTce_Object=MibTableColumn
otukiCtpRxDs15MinutesTce=_OtukiCtpRxDs15MinutesTce_Object((1,3,6,1,4,1,21296,2,2,2,2,31,1,1,20),_OtukiCtpRxDs15MinutesTce_Type())
otukiCtpRxDs15MinutesTce.setMaxAccess(_C)
if mibBuilder.loadTexts:otukiCtpRxDs15MinutesTce.setStatus(_A)
class _OtukiCtpRxDsDayTce_Type(Integer32):defaultValue=1200
_OtukiCtpRxDsDayTce_Type.__name__=_D
_OtukiCtpRxDsDayTce_Object=MibTableColumn
otukiCtpRxDsDayTce=_OtukiCtpRxDsDayTce_Object((1,3,6,1,4,1,21296,2,2,2,2,31,1,1,21),_OtukiCtpRxDsDayTce_Type())
otukiCtpRxDsDayTce.setMaxAccess(_C)
if mibBuilder.loadTexts:otukiCtpRxDsDayTce.setStatus(_A)
class _OtukiCtpRxEbDayTceReporting_Type(TruthValue):defaultValue=2
_OtukiCtpRxEbDayTceReporting_Type.__name__=_G
_OtukiCtpRxEbDayTceReporting_Object=MibTableColumn
otukiCtpRxEbDayTceReporting=_OtukiCtpRxEbDayTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,31,1,1,22),_OtukiCtpRxEbDayTceReporting_Type())
otukiCtpRxEbDayTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:otukiCtpRxEbDayTceReporting.setStatus(_A)
class _OtukiCtpRxEb15MinutesTceReporting_Type(TruthValue):defaultValue=2
_OtukiCtpRxEb15MinutesTceReporting_Type.__name__=_G
_OtukiCtpRxEb15MinutesTceReporting_Object=MibTableColumn
otukiCtpRxEb15MinutesTceReporting=_OtukiCtpRxEb15MinutesTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,31,1,1,23),_OtukiCtpRxEb15MinutesTceReporting_Type())
otukiCtpRxEb15MinutesTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:otukiCtpRxEb15MinutesTceReporting.setStatus(_A)
class _OtukiCtpRxDsDayTceReporting_Type(TruthValue):defaultValue=2
_OtukiCtpRxDsDayTceReporting_Type.__name__=_G
_OtukiCtpRxDsDayTceReporting_Object=MibTableColumn
otukiCtpRxDsDayTceReporting=_OtukiCtpRxDsDayTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,31,1,1,24),_OtukiCtpRxDsDayTceReporting_Type())
otukiCtpRxDsDayTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:otukiCtpRxDsDayTceReporting.setStatus(_A)
class _OtukiCtpRxDs15MinutesTceReporting_Type(TruthValue):defaultValue=2
_OtukiCtpRxDs15MinutesTceReporting_Type.__name__=_G
_OtukiCtpRxDs15MinutesTceReporting_Object=MibTableColumn
otukiCtpRxDs15MinutesTceReporting=_OtukiCtpRxDs15MinutesTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,31,1,1,25),_OtukiCtpRxDs15MinutesTceReporting_Type())
otukiCtpRxDs15MinutesTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:otukiCtpRxDs15MinutesTceReporting.setStatus(_A)
class _OtukiCtpAlarmReportControl_Type(InfnArc):defaultValue=1
_OtukiCtpAlarmReportControl_Type.__name__=_K
_OtukiCtpAlarmReportControl_Object=MibTableColumn
otukiCtpAlarmReportControl=_OtukiCtpAlarmReportControl_Object((1,3,6,1,4,1,21296,2,2,2,2,31,1,1,26),_OtukiCtpAlarmReportControl_Type())
otukiCtpAlarmReportControl.setMaxAccess(_C)
if mibBuilder.loadTexts:otukiCtpAlarmReportControl.setStatus(_A)
_OtukiCtpConfiguredServiceType_Type=InfnServiceType
_OtukiCtpConfiguredServiceType_Object=MibTableColumn
otukiCtpConfiguredServiceType=_OtukiCtpConfiguredServiceType_Object((1,3,6,1,4,1,21296,2,2,2,2,31,1,1,27),_OtukiCtpConfiguredServiceType_Type())
otukiCtpConfiguredServiceType.setMaxAccess(_E)
if mibBuilder.loadTexts:otukiCtpConfiguredServiceType.setStatus(_A)
_OtukiCtpConformance_ObjectIdentity=ObjectIdentity
otukiCtpConformance=_OtukiCtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,31,3))
_OtukiCtpCompliances_ObjectIdentity=ObjectIdentity
otukiCtpCompliances=_OtukiCtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,31,3,1))
_OtukiCtpGroups_ObjectIdentity=ObjectIdentity
otukiCtpGroups=_OtukiCtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,31,3,2))
otukiCtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,31,3,2,1))
otukiCtpGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:otukiCtpGroup.setStatus(_A)
otukiCtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,31,3,1,1))
otukiCtpCompliance.setObjects((_B,_o))
if mibBuilder.loadTexts:otukiCtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'otukiCtpMIB':otukiCtpMIB,'otukiCtpTable':otukiCtpTable,'otukiCtpEntry':otukiCtpEntry,_N:otukiCtpServiceMode,_O:otukiCtpServiceModeQualifier,_P:otukiCtpFecCorrection,_Q:otukiCtpFecEnabled,_R:otukiFecDecoderIterationCount,_S:otukpropagationDelay,_T:otukiBitRateK,_U:otukiCtpFacTxTTI,_V:otukiCtpFacExpectedSAPI,_W:otukiCtpFacExpectedDAPI,_X:otukiCtpFacRxTTI,_Y:otukiCtpFacPmHistStatsEnable,_Z:otukiCtpFacMonitoringMode,_a:otukiCtpFacDSThreshold,_b:otukiCtpFacSDThreshold,_c:otukiCtpFacTimDetMode,_d:otukiCtpSupportingOchList,_e:otukiCtpRxEb15MinutesTce,_f:otukiCtpRxEbDayTce,_g:otukiCtpRxDs15MinutesTce,_h:otukiCtpRxDsDayTce,_i:otukiCtpRxEbDayTceReporting,_j:otukiCtpRxEb15MinutesTceReporting,_k:otukiCtpRxDsDayTceReporting,_l:otukiCtpRxDs15MinutesTceReporting,_m:otukiCtpAlarmReportControl,_n:otukiCtpConfiguredServiceType,'otukiCtpConformance':otukiCtpConformance,'otukiCtpCompliances':otukiCtpCompliances,'otukiCtpCompliance':otukiCtpCompliance,'otukiCtpGroups':otukiCtpGroups,_o:otukiCtpGroup})