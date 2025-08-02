_k='oduktClientCtpGroup'
_j='oduktClientCtpRxBeiDayTceReporting'
_i='oduktClientCtpRxBei15MinutesTceReporting'
_h='oduktClientCtpRxBeiDayTce'
_g='oduktClientCtpRxBei15MinutesTce'
_f='oduktClientCtpSDThreshold'
_e='oduktClientCtpRxDs15MinutesTceReporting'
_d='oduktClientCtpRxDsDayTceReporting'
_c='oduktClientCtpRxEb15MinutesTceReporting'
_b='oduktClientCtpRxEbDayTceReporting'
_a='oduktClientCtpRxDsDayTce'
_Z='oduktClientCtpRxDs15MinutesTce'
_Y='oduktClientCtpRxEbDayTce'
_X='oduktClientCtpRxEb15MinutesTce'
_W='oduktClientCtpPmHistStatsEnable'
_V='oduktClientCtpReceivedTTI'
_U='oduktClientCtpTimDetMode'
_T='oduktClientCtpExpectedDAPI'
_S='oduktClientCtpExpectedSAPI'
_R='oduktClientCtpTxTTI'
_Q='oduktClientCtpDSThreshold'
_P='oduktClientCtpMonitoringMode'
_O='oduktClientCtpSupportingCircuitIdList'
_N='oduktClientCtpAlarmReportControl'
_M='oduktClientCtpConfiguredServiceType'
_L='oduktClientCtpSide'
_K='InfnArc'
_J='ifIndex'
_I='IF-MIB'
_H='oduktClientCtpTcmIdentifier'
_G='read-only'
_F='DisplayString'
_E='TruthValue'
_D='Integer32'
_C='read-write'
_B='INFINERA-TP-ODUKTCLIENTCTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_I,_J)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
InfnArc,InfnEnableDisable,InfnMonitoringMode,InfnServiceType=mibBuilder.importSymbols('INFINERA-TC-MIB',_K,'InfnEnableDisable','InfnMonitoringMode','InfnServiceType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention',_E)
oduktClientCtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,24))
if mibBuilder.loadTexts:oduktClientCtpMIB.setRevisions(('2009-04-20 00:00',))
_OduktClientCtpTable_Object=MibTable
oduktClientCtpTable=_OduktClientCtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,24,1))
if mibBuilder.loadTexts:oduktClientCtpTable.setStatus(_A)
_OduktClientCtpEntry_Object=MibTableRow
oduktClientCtpEntry=_OduktClientCtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,24,1,1))
oduktClientCtpEntry.setIndexNames((0,_I,_J),(0,_B,_H))
if mibBuilder.loadTexts:oduktClientCtpEntry.setStatus(_A)
class _OduktClientCtpTcmIdentifier_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_OduktClientCtpTcmIdentifier_Type.__name__=_D
_OduktClientCtpTcmIdentifier_Object=MibTableColumn
oduktClientCtpTcmIdentifier=_OduktClientCtpTcmIdentifier_Object((1,3,6,1,4,1,21296,2,2,2,2,24,1,1,1),_OduktClientCtpTcmIdentifier_Type())
oduktClientCtpTcmIdentifier.setMaxAccess(_G)
if mibBuilder.loadTexts:oduktClientCtpTcmIdentifier.setStatus(_A)
class _OduktClientCtpSide_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fac',1),('term',2)))
_OduktClientCtpSide_Type.__name__=_D
_OduktClientCtpSide_Object=MibTableColumn
oduktClientCtpSide=_OduktClientCtpSide_Object((1,3,6,1,4,1,21296,2,2,2,2,24,1,1,2),_OduktClientCtpSide_Type())
oduktClientCtpSide.setMaxAccess(_G)
if mibBuilder.loadTexts:oduktClientCtpSide.setStatus(_A)
_OduktClientCtpConfiguredServiceType_Type=InfnServiceType
_OduktClientCtpConfiguredServiceType_Object=MibTableColumn
oduktClientCtpConfiguredServiceType=_OduktClientCtpConfiguredServiceType_Object((1,3,6,1,4,1,21296,2,2,2,2,24,1,1,3),_OduktClientCtpConfiguredServiceType_Type())
oduktClientCtpConfiguredServiceType.setMaxAccess(_G)
if mibBuilder.loadTexts:oduktClientCtpConfiguredServiceType.setStatus(_A)
class _OduktClientCtpAlarmReportControl_Type(InfnArc):defaultValue=1
_OduktClientCtpAlarmReportControl_Type.__name__=_K
_OduktClientCtpAlarmReportControl_Object=MibTableColumn
oduktClientCtpAlarmReportControl=_OduktClientCtpAlarmReportControl_Object((1,3,6,1,4,1,21296,2,2,2,2,24,1,1,4),_OduktClientCtpAlarmReportControl_Type())
oduktClientCtpAlarmReportControl.setMaxAccess(_C)
if mibBuilder.loadTexts:oduktClientCtpAlarmReportControl.setStatus(_A)
_OduktClientCtpSupportingCircuitIdList_Type=DisplayString
_OduktClientCtpSupportingCircuitIdList_Object=MibTableColumn
oduktClientCtpSupportingCircuitIdList=_OduktClientCtpSupportingCircuitIdList_Object((1,3,6,1,4,1,21296,2,2,2,2,24,1,1,5),_OduktClientCtpSupportingCircuitIdList_Type())
oduktClientCtpSupportingCircuitIdList.setMaxAccess(_G)
if mibBuilder.loadTexts:oduktClientCtpSupportingCircuitIdList.setStatus(_A)
_OduktClientCtpMonitoringMode_Type=InfnMonitoringMode
_OduktClientCtpMonitoringMode_Object=MibTableColumn
oduktClientCtpMonitoringMode=_OduktClientCtpMonitoringMode_Object((1,3,6,1,4,1,21296,2,2,2,2,24,1,1,6),_OduktClientCtpMonitoringMode_Type())
oduktClientCtpMonitoringMode.setMaxAccess(_C)
if mibBuilder.loadTexts:oduktClientCtpMonitoringMode.setStatus(_A)
class _OduktClientCtpDSThreshold_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_OduktClientCtpDSThreshold_Type.__name__=_D
_OduktClientCtpDSThreshold_Object=MibTableColumn
oduktClientCtpDSThreshold=_OduktClientCtpDSThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,24,1,1,7),_OduktClientCtpDSThreshold_Type())
oduktClientCtpDSThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:oduktClientCtpDSThreshold.setStatus(_A)
class _OduktClientCtpTxTTI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_OduktClientCtpTxTTI_Type.__name__=_F
_OduktClientCtpTxTTI_Object=MibTableColumn
oduktClientCtpTxTTI=_OduktClientCtpTxTTI_Object((1,3,6,1,4,1,21296,2,2,2,2,24,1,1,8),_OduktClientCtpTxTTI_Type())
oduktClientCtpTxTTI.setMaxAccess(_C)
if mibBuilder.loadTexts:oduktClientCtpTxTTI.setStatus(_A)
class _OduktClientCtpExpectedSAPI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_OduktClientCtpExpectedSAPI_Type.__name__=_F
_OduktClientCtpExpectedSAPI_Object=MibTableColumn
oduktClientCtpExpectedSAPI=_OduktClientCtpExpectedSAPI_Object((1,3,6,1,4,1,21296,2,2,2,2,24,1,1,9),_OduktClientCtpExpectedSAPI_Type())
oduktClientCtpExpectedSAPI.setMaxAccess(_C)
if mibBuilder.loadTexts:oduktClientCtpExpectedSAPI.setStatus(_A)
class _OduktClientCtpExpectedDAPI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_OduktClientCtpExpectedDAPI_Type.__name__=_F
_OduktClientCtpExpectedDAPI_Object=MibTableColumn
oduktClientCtpExpectedDAPI=_OduktClientCtpExpectedDAPI_Object((1,3,6,1,4,1,21296,2,2,2,2,24,1,1,10),_OduktClientCtpExpectedDAPI_Type())
oduktClientCtpExpectedDAPI.setMaxAccess(_C)
if mibBuilder.loadTexts:oduktClientCtpExpectedDAPI.setStatus(_A)
class _OduktClientCtpTimDetMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('off',1),('sapi',2),('dapi',3),('sapidapi',4)))
_OduktClientCtpTimDetMode_Type.__name__=_D
_OduktClientCtpTimDetMode_Object=MibTableColumn
oduktClientCtpTimDetMode=_OduktClientCtpTimDetMode_Object((1,3,6,1,4,1,21296,2,2,2,2,24,1,1,11),_OduktClientCtpTimDetMode_Type())
oduktClientCtpTimDetMode.setMaxAccess(_C)
if mibBuilder.loadTexts:oduktClientCtpTimDetMode.setStatus(_A)
class _OduktClientCtpReceivedTTI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_OduktClientCtpReceivedTTI_Type.__name__=_F
_OduktClientCtpReceivedTTI_Object=MibTableColumn
oduktClientCtpReceivedTTI=_OduktClientCtpReceivedTTI_Object((1,3,6,1,4,1,21296,2,2,2,2,24,1,1,12),_OduktClientCtpReceivedTTI_Type())
oduktClientCtpReceivedTTI.setMaxAccess(_G)
if mibBuilder.loadTexts:oduktClientCtpReceivedTTI.setStatus(_A)
class _OduktClientCtpPmHistStatsEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_OduktClientCtpPmHistStatsEnable_Type.__name__=_D
_OduktClientCtpPmHistStatsEnable_Object=MibTableColumn
oduktClientCtpPmHistStatsEnable=_OduktClientCtpPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,24,1,1,13),_OduktClientCtpPmHistStatsEnable_Type())
oduktClientCtpPmHistStatsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:oduktClientCtpPmHistStatsEnable.setStatus(_A)
class _OduktClientCtpRxEb15MinutesTce_Type(Integer32):defaultValue=1500
_OduktClientCtpRxEb15MinutesTce_Type.__name__=_D
_OduktClientCtpRxEb15MinutesTce_Object=MibTableColumn
oduktClientCtpRxEb15MinutesTce=_OduktClientCtpRxEb15MinutesTce_Object((1,3,6,1,4,1,21296,2,2,2,2,24,1,1,14),_OduktClientCtpRxEb15MinutesTce_Type())
oduktClientCtpRxEb15MinutesTce.setMaxAccess(_C)
if mibBuilder.loadTexts:oduktClientCtpRxEb15MinutesTce.setStatus(_A)
class _OduktClientCtpRxEbDayTce_Type(Integer32):defaultValue=15000
_OduktClientCtpRxEbDayTce_Type.__name__=_D
_OduktClientCtpRxEbDayTce_Object=MibTableColumn
oduktClientCtpRxEbDayTce=_OduktClientCtpRxEbDayTce_Object((1,3,6,1,4,1,21296,2,2,2,2,24,1,1,15),_OduktClientCtpRxEbDayTce_Type())
oduktClientCtpRxEbDayTce.setMaxAccess(_C)
if mibBuilder.loadTexts:oduktClientCtpRxEbDayTce.setStatus(_A)
class _OduktClientCtpRxDs15MinutesTce_Type(Integer32):defaultValue=120
_OduktClientCtpRxDs15MinutesTce_Type.__name__=_D
_OduktClientCtpRxDs15MinutesTce_Object=MibTableColumn
oduktClientCtpRxDs15MinutesTce=_OduktClientCtpRxDs15MinutesTce_Object((1,3,6,1,4,1,21296,2,2,2,2,24,1,1,16),_OduktClientCtpRxDs15MinutesTce_Type())
oduktClientCtpRxDs15MinutesTce.setMaxAccess(_C)
if mibBuilder.loadTexts:oduktClientCtpRxDs15MinutesTce.setStatus(_A)
class _OduktClientCtpRxDsDayTce_Type(Integer32):defaultValue=1200
_OduktClientCtpRxDsDayTce_Type.__name__=_D
_OduktClientCtpRxDsDayTce_Object=MibTableColumn
oduktClientCtpRxDsDayTce=_OduktClientCtpRxDsDayTce_Object((1,3,6,1,4,1,21296,2,2,2,2,24,1,1,17),_OduktClientCtpRxDsDayTce_Type())
oduktClientCtpRxDsDayTce.setMaxAccess(_C)
if mibBuilder.loadTexts:oduktClientCtpRxDsDayTce.setStatus(_A)
class _OduktClientCtpRxEbDayTceReporting_Type(TruthValue):defaultValue=2
_OduktClientCtpRxEbDayTceReporting_Type.__name__=_E
_OduktClientCtpRxEbDayTceReporting_Object=MibTableColumn
oduktClientCtpRxEbDayTceReporting=_OduktClientCtpRxEbDayTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,24,1,1,18),_OduktClientCtpRxEbDayTceReporting_Type())
oduktClientCtpRxEbDayTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:oduktClientCtpRxEbDayTceReporting.setStatus(_A)
class _OduktClientCtpRxEb15MinutesTceReporting_Type(TruthValue):defaultValue=2
_OduktClientCtpRxEb15MinutesTceReporting_Type.__name__=_E
_OduktClientCtpRxEb15MinutesTceReporting_Object=MibTableColumn
oduktClientCtpRxEb15MinutesTceReporting=_OduktClientCtpRxEb15MinutesTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,24,1,1,19),_OduktClientCtpRxEb15MinutesTceReporting_Type())
oduktClientCtpRxEb15MinutesTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:oduktClientCtpRxEb15MinutesTceReporting.setStatus(_A)
class _OduktClientCtpRxDsDayTceReporting_Type(TruthValue):defaultValue=2
_OduktClientCtpRxDsDayTceReporting_Type.__name__=_E
_OduktClientCtpRxDsDayTceReporting_Object=MibTableColumn
oduktClientCtpRxDsDayTceReporting=_OduktClientCtpRxDsDayTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,24,1,1,20),_OduktClientCtpRxDsDayTceReporting_Type())
oduktClientCtpRxDsDayTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:oduktClientCtpRxDsDayTceReporting.setStatus(_A)
class _OduktClientCtpRxDs15MinutesTceReporting_Type(TruthValue):defaultValue=2
_OduktClientCtpRxDs15MinutesTceReporting_Type.__name__=_E
_OduktClientCtpRxDs15MinutesTceReporting_Object=MibTableColumn
oduktClientCtpRxDs15MinutesTceReporting=_OduktClientCtpRxDs15MinutesTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,24,1,1,21),_OduktClientCtpRxDs15MinutesTceReporting_Type())
oduktClientCtpRxDs15MinutesTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:oduktClientCtpRxDs15MinutesTceReporting.setStatus(_A)
class _OduktClientCtpSDThreshold_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_OduktClientCtpSDThreshold_Type.__name__=_D
_OduktClientCtpSDThreshold_Object=MibTableColumn
oduktClientCtpSDThreshold=_OduktClientCtpSDThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,24,1,1,22),_OduktClientCtpSDThreshold_Type())
oduktClientCtpSDThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:oduktClientCtpSDThreshold.setStatus(_A)
_OduktClientCtpRxBei15MinutesTce_Type=Counter64
_OduktClientCtpRxBei15MinutesTce_Object=MibTableColumn
oduktClientCtpRxBei15MinutesTce=_OduktClientCtpRxBei15MinutesTce_Object((1,3,6,1,4,1,21296,2,2,2,2,24,1,1,23),_OduktClientCtpRxBei15MinutesTce_Type())
oduktClientCtpRxBei15MinutesTce.setMaxAccess(_C)
if mibBuilder.loadTexts:oduktClientCtpRxBei15MinutesTce.setStatus(_A)
_OduktClientCtpRxBeiDayTce_Type=Counter64
_OduktClientCtpRxBeiDayTce_Object=MibTableColumn
oduktClientCtpRxBeiDayTce=_OduktClientCtpRxBeiDayTce_Object((1,3,6,1,4,1,21296,2,2,2,2,24,1,1,24),_OduktClientCtpRxBeiDayTce_Type())
oduktClientCtpRxBeiDayTce.setMaxAccess(_C)
if mibBuilder.loadTexts:oduktClientCtpRxBeiDayTce.setStatus(_A)
class _OduktClientCtpRxBei15MinutesTceReporting_Type(TruthValue):defaultValue=2
_OduktClientCtpRxBei15MinutesTceReporting_Type.__name__=_E
_OduktClientCtpRxBei15MinutesTceReporting_Object=MibTableColumn
oduktClientCtpRxBei15MinutesTceReporting=_OduktClientCtpRxBei15MinutesTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,24,1,1,25),_OduktClientCtpRxBei15MinutesTceReporting_Type())
oduktClientCtpRxBei15MinutesTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:oduktClientCtpRxBei15MinutesTceReporting.setStatus(_A)
class _OduktClientCtpRxBeiDayTceReporting_Type(TruthValue):defaultValue=2
_OduktClientCtpRxBeiDayTceReporting_Type.__name__=_E
_OduktClientCtpRxBeiDayTceReporting_Object=MibTableColumn
oduktClientCtpRxBeiDayTceReporting=_OduktClientCtpRxBeiDayTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,24,1,1,26),_OduktClientCtpRxBeiDayTceReporting_Type())
oduktClientCtpRxBeiDayTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:oduktClientCtpRxBeiDayTceReporting.setStatus(_A)
_OduktClientCtpConformance_ObjectIdentity=ObjectIdentity
oduktClientCtpConformance=_OduktClientCtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,24,3))
_OduktClientCtpCompliances_ObjectIdentity=ObjectIdentity
oduktClientCtpCompliances=_OduktClientCtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,24,3,1))
_OduktClientCtpGroups_ObjectIdentity=ObjectIdentity
oduktClientCtpGroups=_OduktClientCtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,24,3,2))
oduktClientCtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,24,3,2,1))
oduktClientCtpGroup.setObjects(*((_B,_H),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:oduktClientCtpGroup.setStatus(_A)
oduktClientCtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,24,3,1,1))
oduktClientCtpCompliance.setObjects((_B,_k))
if mibBuilder.loadTexts:oduktClientCtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'oduktClientCtpMIB':oduktClientCtpMIB,'oduktClientCtpTable':oduktClientCtpTable,'oduktClientCtpEntry':oduktClientCtpEntry,_H:oduktClientCtpTcmIdentifier,_L:oduktClientCtpSide,_M:oduktClientCtpConfiguredServiceType,_N:oduktClientCtpAlarmReportControl,_O:oduktClientCtpSupportingCircuitIdList,_P:oduktClientCtpMonitoringMode,_Q:oduktClientCtpDSThreshold,_R:oduktClientCtpTxTTI,_S:oduktClientCtpExpectedSAPI,_T:oduktClientCtpExpectedDAPI,_U:oduktClientCtpTimDetMode,_V:oduktClientCtpReceivedTTI,_W:oduktClientCtpPmHistStatsEnable,_X:oduktClientCtpRxEb15MinutesTce,_Y:oduktClientCtpRxEbDayTce,_Z:oduktClientCtpRxDs15MinutesTce,_a:oduktClientCtpRxDsDayTce,_b:oduktClientCtpRxEbDayTceReporting,_c:oduktClientCtpRxEb15MinutesTceReporting,_d:oduktClientCtpRxDsDayTceReporting,_e:oduktClientCtpRxDs15MinutesTceReporting,_f:oduktClientCtpSDThreshold,_g:oduktClientCtpRxBei15MinutesTce,_h:oduktClientCtpRxBeiDayTce,_i:oduktClientCtpRxBei15MinutesTceReporting,_j:oduktClientCtpRxBeiDayTceReporting,'oduktClientCtpConformance':oduktClientCtpConformance,'oduktClientCtpCompliances':oduktClientCtpCompliances,'oduktClientCtpCompliance':oduktClientCtpCompliance,'oduktClientCtpGroups':oduktClientCtpGroups,_k:oduktClientCtpGroup})