_k='oduiktClientCtpGroup'
_j='oduiktClientCtpRxBeiDayTceReporting'
_i='oduiktClientCtpRxBei15MinutesTceReporting'
_h='oduiktClientCtpRxBeiDayTce'
_g='oduiktClientCtpRxBei15MinutesTce'
_f='oduiktClientCtpSDThreshold'
_e='oduiktClientCtpRxDs15MinutesTceReporting'
_d='oduiktClientCtpRxDsDayTceReporting'
_c='oduiktClientCtpRxEb15MinutesTceReporting'
_b='oduiktClientCtpRxEbDayTceReporting'
_a='oduiktClientCtpRxDsDayTce'
_Z='oduiktClientCtpRxDs15MinutesTce'
_Y='oduiktClientCtpRxEbDayTce'
_X='oduiktClientCtpRxEb15MinutesTce'
_W='oduiktClientCtpPmHistStatsEnable'
_V='oduiktClientCtpReceivedTTI'
_U='oduiktClientCtpTimDetMode'
_T='oduiktClientCtpExpectedDAPI'
_S='oduiktClientCtpExpectedSAPI'
_R='oduiktClientCtpTxTTI'
_Q='oduiktClientCtpDSThreshold'
_P='oduiktClientCtpMonitoringMode'
_O='oduiktClientCtpSupportingCircuitIdList'
_N='oduiktClientCtpAlarmReportControl'
_M='oduiktClientCtpConfiguredServiceType'
_L='oduiktClientCtpSide'
_K='InfnArc'
_J='ifIndex'
_I='IF-MIB'
_H='oduiktClientCtpTcmIdentifier'
_G='read-only'
_F='DisplayString'
_E='TruthValue'
_D='Integer32'
_C='read-write'
_B='INFINERA-TP-ODUKTICTP-MIB'
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
oduiktClientCtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,35))
if mibBuilder.loadTexts:oduiktClientCtpMIB.setRevisions(('2011-10-20 00:00',))
_OduiktClientCtpTable_Object=MibTable
oduiktClientCtpTable=_OduiktClientCtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,35,1))
if mibBuilder.loadTexts:oduiktClientCtpTable.setStatus(_A)
_OduiktClientCtpEntry_Object=MibTableRow
oduiktClientCtpEntry=_OduiktClientCtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,35,1,1))
oduiktClientCtpEntry.setIndexNames((0,_I,_J),(0,_B,_H))
if mibBuilder.loadTexts:oduiktClientCtpEntry.setStatus(_A)
class _OduiktClientCtpTcmIdentifier_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_OduiktClientCtpTcmIdentifier_Type.__name__=_D
_OduiktClientCtpTcmIdentifier_Object=MibTableColumn
oduiktClientCtpTcmIdentifier=_OduiktClientCtpTcmIdentifier_Object((1,3,6,1,4,1,21296,2,2,2,2,35,1,1,1),_OduiktClientCtpTcmIdentifier_Type())
oduiktClientCtpTcmIdentifier.setMaxAccess(_G)
if mibBuilder.loadTexts:oduiktClientCtpTcmIdentifier.setStatus(_A)
class _OduiktClientCtpSide_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fac',1),('term',2)))
_OduiktClientCtpSide_Type.__name__=_D
_OduiktClientCtpSide_Object=MibTableColumn
oduiktClientCtpSide=_OduiktClientCtpSide_Object((1,3,6,1,4,1,21296,2,2,2,2,35,1,1,2),_OduiktClientCtpSide_Type())
oduiktClientCtpSide.setMaxAccess(_G)
if mibBuilder.loadTexts:oduiktClientCtpSide.setStatus(_A)
_OduiktClientCtpConfiguredServiceType_Type=InfnServiceType
_OduiktClientCtpConfiguredServiceType_Object=MibTableColumn
oduiktClientCtpConfiguredServiceType=_OduiktClientCtpConfiguredServiceType_Object((1,3,6,1,4,1,21296,2,2,2,2,35,1,1,3),_OduiktClientCtpConfiguredServiceType_Type())
oduiktClientCtpConfiguredServiceType.setMaxAccess(_G)
if mibBuilder.loadTexts:oduiktClientCtpConfiguredServiceType.setStatus(_A)
class _OduiktClientCtpAlarmReportControl_Type(InfnArc):defaultValue=1
_OduiktClientCtpAlarmReportControl_Type.__name__=_K
_OduiktClientCtpAlarmReportControl_Object=MibTableColumn
oduiktClientCtpAlarmReportControl=_OduiktClientCtpAlarmReportControl_Object((1,3,6,1,4,1,21296,2,2,2,2,35,1,1,4),_OduiktClientCtpAlarmReportControl_Type())
oduiktClientCtpAlarmReportControl.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiktClientCtpAlarmReportControl.setStatus(_A)
_OduiktClientCtpSupportingCircuitIdList_Type=DisplayString
_OduiktClientCtpSupportingCircuitIdList_Object=MibTableColumn
oduiktClientCtpSupportingCircuitIdList=_OduiktClientCtpSupportingCircuitIdList_Object((1,3,6,1,4,1,21296,2,2,2,2,35,1,1,5),_OduiktClientCtpSupportingCircuitIdList_Type())
oduiktClientCtpSupportingCircuitIdList.setMaxAccess(_G)
if mibBuilder.loadTexts:oduiktClientCtpSupportingCircuitIdList.setStatus(_A)
_OduiktClientCtpMonitoringMode_Type=InfnMonitoringMode
_OduiktClientCtpMonitoringMode_Object=MibTableColumn
oduiktClientCtpMonitoringMode=_OduiktClientCtpMonitoringMode_Object((1,3,6,1,4,1,21296,2,2,2,2,35,1,1,6),_OduiktClientCtpMonitoringMode_Type())
oduiktClientCtpMonitoringMode.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiktClientCtpMonitoringMode.setStatus(_A)
class _OduiktClientCtpDSThreshold_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_OduiktClientCtpDSThreshold_Type.__name__=_D
_OduiktClientCtpDSThreshold_Object=MibTableColumn
oduiktClientCtpDSThreshold=_OduiktClientCtpDSThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,35,1,1,7),_OduiktClientCtpDSThreshold_Type())
oduiktClientCtpDSThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiktClientCtpDSThreshold.setStatus(_A)
class _OduiktClientCtpTxTTI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_OduiktClientCtpTxTTI_Type.__name__=_F
_OduiktClientCtpTxTTI_Object=MibTableColumn
oduiktClientCtpTxTTI=_OduiktClientCtpTxTTI_Object((1,3,6,1,4,1,21296,2,2,2,2,35,1,1,8),_OduiktClientCtpTxTTI_Type())
oduiktClientCtpTxTTI.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiktClientCtpTxTTI.setStatus(_A)
class _OduiktClientCtpExpectedSAPI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_OduiktClientCtpExpectedSAPI_Type.__name__=_F
_OduiktClientCtpExpectedSAPI_Object=MibTableColumn
oduiktClientCtpExpectedSAPI=_OduiktClientCtpExpectedSAPI_Object((1,3,6,1,4,1,21296,2,2,2,2,35,1,1,9),_OduiktClientCtpExpectedSAPI_Type())
oduiktClientCtpExpectedSAPI.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiktClientCtpExpectedSAPI.setStatus(_A)
class _OduiktClientCtpExpectedDAPI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_OduiktClientCtpExpectedDAPI_Type.__name__=_F
_OduiktClientCtpExpectedDAPI_Object=MibTableColumn
oduiktClientCtpExpectedDAPI=_OduiktClientCtpExpectedDAPI_Object((1,3,6,1,4,1,21296,2,2,2,2,35,1,1,10),_OduiktClientCtpExpectedDAPI_Type())
oduiktClientCtpExpectedDAPI.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiktClientCtpExpectedDAPI.setStatus(_A)
class _OduiktClientCtpTimDetMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('off',1),('sapi',2),('dapi',3),('sapidapi',4)))
_OduiktClientCtpTimDetMode_Type.__name__=_D
_OduiktClientCtpTimDetMode_Object=MibTableColumn
oduiktClientCtpTimDetMode=_OduiktClientCtpTimDetMode_Object((1,3,6,1,4,1,21296,2,2,2,2,35,1,1,11),_OduiktClientCtpTimDetMode_Type())
oduiktClientCtpTimDetMode.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiktClientCtpTimDetMode.setStatus(_A)
class _OduiktClientCtpReceivedTTI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_OduiktClientCtpReceivedTTI_Type.__name__=_F
_OduiktClientCtpReceivedTTI_Object=MibTableColumn
oduiktClientCtpReceivedTTI=_OduiktClientCtpReceivedTTI_Object((1,3,6,1,4,1,21296,2,2,2,2,35,1,1,12),_OduiktClientCtpReceivedTTI_Type())
oduiktClientCtpReceivedTTI.setMaxAccess(_G)
if mibBuilder.loadTexts:oduiktClientCtpReceivedTTI.setStatus(_A)
class _OduiktClientCtpPmHistStatsEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_OduiktClientCtpPmHistStatsEnable_Type.__name__=_D
_OduiktClientCtpPmHistStatsEnable_Object=MibTableColumn
oduiktClientCtpPmHistStatsEnable=_OduiktClientCtpPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,35,1,1,13),_OduiktClientCtpPmHistStatsEnable_Type())
oduiktClientCtpPmHistStatsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiktClientCtpPmHistStatsEnable.setStatus(_A)
class _OduiktClientCtpRxEb15MinutesTce_Type(Integer32):defaultValue=1500
_OduiktClientCtpRxEb15MinutesTce_Type.__name__=_D
_OduiktClientCtpRxEb15MinutesTce_Object=MibTableColumn
oduiktClientCtpRxEb15MinutesTce=_OduiktClientCtpRxEb15MinutesTce_Object((1,3,6,1,4,1,21296,2,2,2,2,35,1,1,14),_OduiktClientCtpRxEb15MinutesTce_Type())
oduiktClientCtpRxEb15MinutesTce.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiktClientCtpRxEb15MinutesTce.setStatus(_A)
class _OduiktClientCtpRxEbDayTce_Type(Integer32):defaultValue=15000
_OduiktClientCtpRxEbDayTce_Type.__name__=_D
_OduiktClientCtpRxEbDayTce_Object=MibTableColumn
oduiktClientCtpRxEbDayTce=_OduiktClientCtpRxEbDayTce_Object((1,3,6,1,4,1,21296,2,2,2,2,35,1,1,15),_OduiktClientCtpRxEbDayTce_Type())
oduiktClientCtpRxEbDayTce.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiktClientCtpRxEbDayTce.setStatus(_A)
class _OduiktClientCtpRxDs15MinutesTce_Type(Integer32):defaultValue=120
_OduiktClientCtpRxDs15MinutesTce_Type.__name__=_D
_OduiktClientCtpRxDs15MinutesTce_Object=MibTableColumn
oduiktClientCtpRxDs15MinutesTce=_OduiktClientCtpRxDs15MinutesTce_Object((1,3,6,1,4,1,21296,2,2,2,2,35,1,1,16),_OduiktClientCtpRxDs15MinutesTce_Type())
oduiktClientCtpRxDs15MinutesTce.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiktClientCtpRxDs15MinutesTce.setStatus(_A)
class _OduiktClientCtpRxDsDayTce_Type(Integer32):defaultValue=1200
_OduiktClientCtpRxDsDayTce_Type.__name__=_D
_OduiktClientCtpRxDsDayTce_Object=MibTableColumn
oduiktClientCtpRxDsDayTce=_OduiktClientCtpRxDsDayTce_Object((1,3,6,1,4,1,21296,2,2,2,2,35,1,1,17),_OduiktClientCtpRxDsDayTce_Type())
oduiktClientCtpRxDsDayTce.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiktClientCtpRxDsDayTce.setStatus(_A)
class _OduiktClientCtpRxEbDayTceReporting_Type(TruthValue):defaultValue=2
_OduiktClientCtpRxEbDayTceReporting_Type.__name__=_E
_OduiktClientCtpRxEbDayTceReporting_Object=MibTableColumn
oduiktClientCtpRxEbDayTceReporting=_OduiktClientCtpRxEbDayTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,35,1,1,18),_OduiktClientCtpRxEbDayTceReporting_Type())
oduiktClientCtpRxEbDayTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiktClientCtpRxEbDayTceReporting.setStatus(_A)
class _OduiktClientCtpRxEb15MinutesTceReporting_Type(TruthValue):defaultValue=2
_OduiktClientCtpRxEb15MinutesTceReporting_Type.__name__=_E
_OduiktClientCtpRxEb15MinutesTceReporting_Object=MibTableColumn
oduiktClientCtpRxEb15MinutesTceReporting=_OduiktClientCtpRxEb15MinutesTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,35,1,1,19),_OduiktClientCtpRxEb15MinutesTceReporting_Type())
oduiktClientCtpRxEb15MinutesTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiktClientCtpRxEb15MinutesTceReporting.setStatus(_A)
class _OduiktClientCtpRxDsDayTceReporting_Type(TruthValue):defaultValue=2
_OduiktClientCtpRxDsDayTceReporting_Type.__name__=_E
_OduiktClientCtpRxDsDayTceReporting_Object=MibTableColumn
oduiktClientCtpRxDsDayTceReporting=_OduiktClientCtpRxDsDayTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,35,1,1,20),_OduiktClientCtpRxDsDayTceReporting_Type())
oduiktClientCtpRxDsDayTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiktClientCtpRxDsDayTceReporting.setStatus(_A)
class _OduiktClientCtpRxDs15MinutesTceReporting_Type(TruthValue):defaultValue=2
_OduiktClientCtpRxDs15MinutesTceReporting_Type.__name__=_E
_OduiktClientCtpRxDs15MinutesTceReporting_Object=MibTableColumn
oduiktClientCtpRxDs15MinutesTceReporting=_OduiktClientCtpRxDs15MinutesTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,35,1,1,21),_OduiktClientCtpRxDs15MinutesTceReporting_Type())
oduiktClientCtpRxDs15MinutesTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiktClientCtpRxDs15MinutesTceReporting.setStatus(_A)
class _OduiktClientCtpSDThreshold_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_OduiktClientCtpSDThreshold_Type.__name__=_D
_OduiktClientCtpSDThreshold_Object=MibTableColumn
oduiktClientCtpSDThreshold=_OduiktClientCtpSDThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,35,1,1,22),_OduiktClientCtpSDThreshold_Type())
oduiktClientCtpSDThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiktClientCtpSDThreshold.setStatus(_A)
_OduiktClientCtpRxBei15MinutesTce_Type=Counter64
_OduiktClientCtpRxBei15MinutesTce_Object=MibTableColumn
oduiktClientCtpRxBei15MinutesTce=_OduiktClientCtpRxBei15MinutesTce_Object((1,3,6,1,4,1,21296,2,2,2,2,35,1,1,23),_OduiktClientCtpRxBei15MinutesTce_Type())
oduiktClientCtpRxBei15MinutesTce.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiktClientCtpRxBei15MinutesTce.setStatus(_A)
_OduiktClientCtpRxBeiDayTce_Type=Counter64
_OduiktClientCtpRxBeiDayTce_Object=MibTableColumn
oduiktClientCtpRxBeiDayTce=_OduiktClientCtpRxBeiDayTce_Object((1,3,6,1,4,1,21296,2,2,2,2,35,1,1,24),_OduiktClientCtpRxBeiDayTce_Type())
oduiktClientCtpRxBeiDayTce.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiktClientCtpRxBeiDayTce.setStatus(_A)
class _OduiktClientCtpRxBei15MinutesTceReporting_Type(TruthValue):defaultValue=2
_OduiktClientCtpRxBei15MinutesTceReporting_Type.__name__=_E
_OduiktClientCtpRxBei15MinutesTceReporting_Object=MibTableColumn
oduiktClientCtpRxBei15MinutesTceReporting=_OduiktClientCtpRxBei15MinutesTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,35,1,1,25),_OduiktClientCtpRxBei15MinutesTceReporting_Type())
oduiktClientCtpRxBei15MinutesTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiktClientCtpRxBei15MinutesTceReporting.setStatus(_A)
class _OduiktClientCtpRxBeiDayTceReporting_Type(TruthValue):defaultValue=2
_OduiktClientCtpRxBeiDayTceReporting_Type.__name__=_E
_OduiktClientCtpRxBeiDayTceReporting_Object=MibTableColumn
oduiktClientCtpRxBeiDayTceReporting=_OduiktClientCtpRxBeiDayTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,35,1,1,26),_OduiktClientCtpRxBeiDayTceReporting_Type())
oduiktClientCtpRxBeiDayTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:oduiktClientCtpRxBeiDayTceReporting.setStatus(_A)
_OduiktClientCtpConformance_ObjectIdentity=ObjectIdentity
oduiktClientCtpConformance=_OduiktClientCtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,35,3))
_OduiktClientCtpCompliances_ObjectIdentity=ObjectIdentity
oduiktClientCtpCompliances=_OduiktClientCtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,35,3,1))
_OduiktClientCtpGroups_ObjectIdentity=ObjectIdentity
oduiktClientCtpGroups=_OduiktClientCtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,35,3,2))
oduiktClientCtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,35,3,2,1))
oduiktClientCtpGroup.setObjects(*((_B,_H),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:oduiktClientCtpGroup.setStatus(_A)
oduiktClientCtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,35,3,1,1))
oduiktClientCtpCompliance.setObjects((_B,_k))
if mibBuilder.loadTexts:oduiktClientCtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'oduiktClientCtpMIB':oduiktClientCtpMIB,'oduiktClientCtpTable':oduiktClientCtpTable,'oduiktClientCtpEntry':oduiktClientCtpEntry,_H:oduiktClientCtpTcmIdentifier,_L:oduiktClientCtpSide,_M:oduiktClientCtpConfiguredServiceType,_N:oduiktClientCtpAlarmReportControl,_O:oduiktClientCtpSupportingCircuitIdList,_P:oduiktClientCtpMonitoringMode,_Q:oduiktClientCtpDSThreshold,_R:oduiktClientCtpTxTTI,_S:oduiktClientCtpExpectedSAPI,_T:oduiktClientCtpExpectedDAPI,_U:oduiktClientCtpTimDetMode,_V:oduiktClientCtpReceivedTTI,_W:oduiktClientCtpPmHistStatsEnable,_X:oduiktClientCtpRxEb15MinutesTce,_Y:oduiktClientCtpRxEbDayTce,_Z:oduiktClientCtpRxDs15MinutesTce,_a:oduiktClientCtpRxDsDayTce,_b:oduiktClientCtpRxEbDayTceReporting,_c:oduiktClientCtpRxEb15MinutesTceReporting,_d:oduiktClientCtpRxDsDayTceReporting,_e:oduiktClientCtpRxDs15MinutesTceReporting,_f:oduiktClientCtpSDThreshold,_g:oduiktClientCtpRxBei15MinutesTce,_h:oduiktClientCtpRxBeiDayTce,_i:oduiktClientCtpRxBei15MinutesTceReporting,_j:oduiktClientCtpRxBeiDayTceReporting,'oduiktClientCtpConformance':oduiktClientCtpConformance,'oduiktClientCtpCompliances':oduiktClientCtpCompliances,'oduiktClientCtpCompliance':oduiktClientCtpCompliance,'oduiktClientCtpGroups':oduiktClientCtpGroups,_k:oduiktClientCtpGroup})