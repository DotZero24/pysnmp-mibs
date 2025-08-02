_m='dchCtpGroup'
_l='dchCtpConnectivityVerification'
_k='dchCtpPmHistStatsEnable'
_j='dchCtpDtsSesDayTceReporting'
_i='dchCtpDtsEsDayTceReporting'
_h='dchCtpDtsCvDayTceReporting'
_g='dchCtpDtsSes15MinutesTceReporting'
_f='dchCtpDtsEs15MinutesTceReporting'
_e='dchCtpDtsCv15MinutesTceReporting'
_d='dchCtpDtsSesDayTce'
_c='dchCtpDtsEsDayTce'
_b='dchCtpDtsCvDayTce'
_a='dchCtpDtsSes15MinutesTce'
_Z='dchCtpDtsEs15MinutesTce'
_Y='dchCtpDtsCv15MinutesTce'
_X='dchCtpPreFecThresholdMantissa'
_W='dchCtpDtsFecSupport'
_V='dchCtpSignalDegradeReportingControl'
_U='dchCtpDataPlaneTransparency'
_T='dchCtpPreFecThresholdOrder'
_S='dchCtpRxDtsTTI'
_R='dchCtpTxDtsTTI'
_Q='dchCtpDtsTTIMismatchReporting'
_P='dchCtpExpectedDtsTTI'
_O='dchCtpConfiguredServiceType'
_N='dchCtpLoopback'
_M='dchCtpSupportingCircuitIdList'
_L='dchCtpTribPrbsMonMode'
_K='dchCtpTribPrbsGenMode'
_J='ifIndex'
_I='IF-MIB'
_H='read-only'
_G='unknown'
_F='enabled'
_E='disabled'
_D='Integer32'
_C='read-write'
_B='INFINERA-TP-DCHCTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_I,_J)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
InfnLoopbackType,InfnServiceType=mibBuilder.importSymbols('INFINERA-TC-MIB','InfnLoopbackType','InfnServiceType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp','TruthValue')
dchCtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,18))
_DchCtpTable_Object=MibTable
dchCtpTable=_DchCtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,18,1))
if mibBuilder.loadTexts:dchCtpTable.setStatus(_A)
_DchCtpEntry_Object=MibTableRow
dchCtpEntry=_DchCtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,18,1,1))
dchCtpEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:dchCtpEntry.setStatus(_A)
class _DchCtpTribPrbsGenMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_DchCtpTribPrbsGenMode_Type.__name__=_D
_DchCtpTribPrbsGenMode_Object=MibTableColumn
dchCtpTribPrbsGenMode=_DchCtpTribPrbsGenMode_Object((1,3,6,1,4,1,21296,2,2,2,2,18,1,1,1),_DchCtpTribPrbsGenMode_Type())
dchCtpTribPrbsGenMode.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpTribPrbsGenMode.setStatus(_A)
class _DchCtpTribPrbsMonMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_DchCtpTribPrbsMonMode_Type.__name__=_D
_DchCtpTribPrbsMonMode_Object=MibTableColumn
dchCtpTribPrbsMonMode=_DchCtpTribPrbsMonMode_Object((1,3,6,1,4,1,21296,2,2,2,2,18,1,1,2),_DchCtpTribPrbsMonMode_Type())
dchCtpTribPrbsMonMode.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpTribPrbsMonMode.setStatus(_A)
_DchCtpSupportingCircuitIdList_Type=DisplayString
_DchCtpSupportingCircuitIdList_Object=MibTableColumn
dchCtpSupportingCircuitIdList=_DchCtpSupportingCircuitIdList_Object((1,3,6,1,4,1,21296,2,2,2,2,18,1,1,3),_DchCtpSupportingCircuitIdList_Type())
dchCtpSupportingCircuitIdList.setMaxAccess(_H)
if mibBuilder.loadTexts:dchCtpSupportingCircuitIdList.setStatus(_A)
_DchCtpLoopback_Type=InfnLoopbackType
_DchCtpLoopback_Object=MibTableColumn
dchCtpLoopback=_DchCtpLoopback_Object((1,3,6,1,4,1,21296,2,2,2,2,18,1,1,4),_DchCtpLoopback_Type())
dchCtpLoopback.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpLoopback.setStatus(_A)
_DchCtpConfiguredServiceType_Type=InfnServiceType
_DchCtpConfiguredServiceType_Object=MibTableColumn
dchCtpConfiguredServiceType=_DchCtpConfiguredServiceType_Object((1,3,6,1,4,1,21296,2,2,2,2,18,1,1,5),_DchCtpConfiguredServiceType_Type())
dchCtpConfiguredServiceType.setMaxAccess(_H)
if mibBuilder.loadTexts:dchCtpConfiguredServiceType.setStatus(_A)
_DchCtpExpectedDtsTTI_Type=DisplayString
_DchCtpExpectedDtsTTI_Object=MibTableColumn
dchCtpExpectedDtsTTI=_DchCtpExpectedDtsTTI_Object((1,3,6,1,4,1,21296,2,2,2,2,18,1,1,6),_DchCtpExpectedDtsTTI_Type())
dchCtpExpectedDtsTTI.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpExpectedDtsTTI.setStatus(_A)
class _DchCtpDtsTTIMismatchReporting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_DchCtpDtsTTIMismatchReporting_Type.__name__=_D
_DchCtpDtsTTIMismatchReporting_Object=MibTableColumn
dchCtpDtsTTIMismatchReporting=_DchCtpDtsTTIMismatchReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,18,1,1,7),_DchCtpDtsTTIMismatchReporting_Type())
dchCtpDtsTTIMismatchReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpDtsTTIMismatchReporting.setStatus(_A)
_DchCtpTxDtsTTI_Type=DisplayString
_DchCtpTxDtsTTI_Object=MibTableColumn
dchCtpTxDtsTTI=_DchCtpTxDtsTTI_Object((1,3,6,1,4,1,21296,2,2,2,2,18,1,1,8),_DchCtpTxDtsTTI_Type())
dchCtpTxDtsTTI.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpTxDtsTTI.setStatus(_A)
_DchCtpRxDtsTTI_Type=DisplayString
_DchCtpRxDtsTTI_Object=MibTableColumn
dchCtpRxDtsTTI=_DchCtpRxDtsTTI_Object((1,3,6,1,4,1,21296,2,2,2,2,18,1,1,9),_DchCtpRxDtsTTI_Type())
dchCtpRxDtsTTI.setMaxAccess(_H)
if mibBuilder.loadTexts:dchCtpRxDtsTTI.setStatus(_A)
_DchCtpPreFecThresholdOrder_Type=Integer32
_DchCtpPreFecThresholdOrder_Object=MibTableColumn
dchCtpPreFecThresholdOrder=_DchCtpPreFecThresholdOrder_Object((1,3,6,1,4,1,21296,2,2,2,2,18,1,1,10),_DchCtpPreFecThresholdOrder_Type())
dchCtpPreFecThresholdOrder.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpPreFecThresholdOrder.setStatus(_A)
class _DchCtpDataPlaneTransparency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_DchCtpDataPlaneTransparency_Type.__name__=_D
_DchCtpDataPlaneTransparency_Object=MibTableColumn
dchCtpDataPlaneTransparency=_DchCtpDataPlaneTransparency_Object((1,3,6,1,4,1,21296,2,2,2,2,18,1,1,11),_DchCtpDataPlaneTransparency_Type())
dchCtpDataPlaneTransparency.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpDataPlaneTransparency.setStatus(_A)
class _DchCtpSignalDegradeReportingControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_DchCtpSignalDegradeReportingControl_Type.__name__=_D
_DchCtpSignalDegradeReportingControl_Object=MibTableColumn
dchCtpSignalDegradeReportingControl=_DchCtpSignalDegradeReportingControl_Object((1,3,6,1,4,1,21296,2,2,2,2,18,1,1,12),_DchCtpSignalDegradeReportingControl_Type())
dchCtpSignalDegradeReportingControl.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpSignalDegradeReportingControl.setStatus(_A)
class _DchCtpDtsFecSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_DchCtpDtsFecSupport_Type.__name__=_D
_DchCtpDtsFecSupport_Object=MibTableColumn
dchCtpDtsFecSupport=_DchCtpDtsFecSupport_Object((1,3,6,1,4,1,21296,2,2,2,2,18,1,1,13),_DchCtpDtsFecSupport_Type())
dchCtpDtsFecSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpDtsFecSupport.setStatus(_A)
_DchCtpPreFecThresholdMantissa_Type=Integer32
_DchCtpPreFecThresholdMantissa_Object=MibTableColumn
dchCtpPreFecThresholdMantissa=_DchCtpPreFecThresholdMantissa_Object((1,3,6,1,4,1,21296,2,2,2,2,18,1,1,14),_DchCtpPreFecThresholdMantissa_Type())
dchCtpPreFecThresholdMantissa.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpPreFecThresholdMantissa.setStatus(_A)
_DchCtpDtsCv15MinutesTce_Type=Counter64
_DchCtpDtsCv15MinutesTce_Object=MibTableColumn
dchCtpDtsCv15MinutesTce=_DchCtpDtsCv15MinutesTce_Object((1,3,6,1,4,1,21296,2,2,2,2,18,1,1,15),_DchCtpDtsCv15MinutesTce_Type())
dchCtpDtsCv15MinutesTce.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpDtsCv15MinutesTce.setStatus(_A)
_DchCtpDtsEs15MinutesTce_Type=Integer32
_DchCtpDtsEs15MinutesTce_Object=MibTableColumn
dchCtpDtsEs15MinutesTce=_DchCtpDtsEs15MinutesTce_Object((1,3,6,1,4,1,21296,2,2,2,2,18,1,1,16),_DchCtpDtsEs15MinutesTce_Type())
dchCtpDtsEs15MinutesTce.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpDtsEs15MinutesTce.setStatus(_A)
_DchCtpDtsSes15MinutesTce_Type=Integer32
_DchCtpDtsSes15MinutesTce_Object=MibTableColumn
dchCtpDtsSes15MinutesTce=_DchCtpDtsSes15MinutesTce_Object((1,3,6,1,4,1,21296,2,2,2,2,18,1,1,17),_DchCtpDtsSes15MinutesTce_Type())
dchCtpDtsSes15MinutesTce.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpDtsSes15MinutesTce.setStatus(_A)
_DchCtpDtsCvDayTce_Type=Counter64
_DchCtpDtsCvDayTce_Object=MibTableColumn
dchCtpDtsCvDayTce=_DchCtpDtsCvDayTce_Object((1,3,6,1,4,1,21296,2,2,2,2,18,1,1,18),_DchCtpDtsCvDayTce_Type())
dchCtpDtsCvDayTce.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpDtsCvDayTce.setStatus(_A)
_DchCtpDtsEsDayTce_Type=Integer32
_DchCtpDtsEsDayTce_Object=MibTableColumn
dchCtpDtsEsDayTce=_DchCtpDtsEsDayTce_Object((1,3,6,1,4,1,21296,2,2,2,2,18,1,1,19),_DchCtpDtsEsDayTce_Type())
dchCtpDtsEsDayTce.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpDtsEsDayTce.setStatus(_A)
_DchCtpDtsSesDayTce_Type=Integer32
_DchCtpDtsSesDayTce_Object=MibTableColumn
dchCtpDtsSesDayTce=_DchCtpDtsSesDayTce_Object((1,3,6,1,4,1,21296,2,2,2,2,18,1,1,20),_DchCtpDtsSesDayTce_Type())
dchCtpDtsSesDayTce.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpDtsSesDayTce.setStatus(_A)
_DchCtpDtsCv15MinutesTceReporting_Type=TruthValue
_DchCtpDtsCv15MinutesTceReporting_Object=MibTableColumn
dchCtpDtsCv15MinutesTceReporting=_DchCtpDtsCv15MinutesTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,18,1,1,21),_DchCtpDtsCv15MinutesTceReporting_Type())
dchCtpDtsCv15MinutesTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpDtsCv15MinutesTceReporting.setStatus(_A)
_DchCtpDtsEs15MinutesTceReporting_Type=TruthValue
_DchCtpDtsEs15MinutesTceReporting_Object=MibTableColumn
dchCtpDtsEs15MinutesTceReporting=_DchCtpDtsEs15MinutesTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,18,1,1,22),_DchCtpDtsEs15MinutesTceReporting_Type())
dchCtpDtsEs15MinutesTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpDtsEs15MinutesTceReporting.setStatus(_A)
_DchCtpDtsSes15MinutesTceReporting_Type=TruthValue
_DchCtpDtsSes15MinutesTceReporting_Object=MibTableColumn
dchCtpDtsSes15MinutesTceReporting=_DchCtpDtsSes15MinutesTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,18,1,1,23),_DchCtpDtsSes15MinutesTceReporting_Type())
dchCtpDtsSes15MinutesTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpDtsSes15MinutesTceReporting.setStatus(_A)
_DchCtpDtsCvDayTceReporting_Type=TruthValue
_DchCtpDtsCvDayTceReporting_Object=MibTableColumn
dchCtpDtsCvDayTceReporting=_DchCtpDtsCvDayTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,18,1,1,24),_DchCtpDtsCvDayTceReporting_Type())
dchCtpDtsCvDayTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpDtsCvDayTceReporting.setStatus(_A)
_DchCtpDtsEsDayTceReporting_Type=TruthValue
_DchCtpDtsEsDayTceReporting_Object=MibTableColumn
dchCtpDtsEsDayTceReporting=_DchCtpDtsEsDayTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,18,1,1,25),_DchCtpDtsEsDayTceReporting_Type())
dchCtpDtsEsDayTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpDtsEsDayTceReporting.setStatus(_A)
_DchCtpDtsSesDayTceReporting_Type=TruthValue
_DchCtpDtsSesDayTceReporting_Object=MibTableColumn
dchCtpDtsSesDayTceReporting=_DchCtpDtsSesDayTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,18,1,1,26),_DchCtpDtsSesDayTceReporting_Type())
dchCtpDtsSesDayTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpDtsSesDayTceReporting.setStatus(_A)
class _DchCtpPmHistStatsEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_DchCtpPmHistStatsEnable_Type.__name__=_D
_DchCtpPmHistStatsEnable_Object=MibTableColumn
dchCtpPmHistStatsEnable=_DchCtpPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,18,1,1,27),_DchCtpPmHistStatsEnable_Type())
dchCtpPmHistStatsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpPmHistStatsEnable.setStatus(_A)
class _DchCtpConnectivityVerification_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_DchCtpConnectivityVerification_Type.__name__=_D
_DchCtpConnectivityVerification_Object=MibTableColumn
dchCtpConnectivityVerification=_DchCtpConnectivityVerification_Object((1,3,6,1,4,1,21296,2,2,2,2,18,1,1,28),_DchCtpConnectivityVerification_Type())
dchCtpConnectivityVerification.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpConnectivityVerification.setStatus(_A)
_DchCtpConformance_ObjectIdentity=ObjectIdentity
dchCtpConformance=_DchCtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,18,3))
_DchCtpCompliances_ObjectIdentity=ObjectIdentity
dchCtpCompliances=_DchCtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,18,3,1))
_DchCtpGroups_ObjectIdentity=ObjectIdentity
dchCtpGroups=_DchCtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,18,3,2))
dchCtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,18,3,2,1))
dchCtpGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:dchCtpGroup.setStatus(_A)
dchCtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,18,3,1,1))
dchCtpCompliance.setObjects((_B,_m))
if mibBuilder.loadTexts:dchCtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dchCtpMIB':dchCtpMIB,'dchCtpTable':dchCtpTable,'dchCtpEntry':dchCtpEntry,_K:dchCtpTribPrbsGenMode,_L:dchCtpTribPrbsMonMode,_M:dchCtpSupportingCircuitIdList,_N:dchCtpLoopback,_O:dchCtpConfiguredServiceType,_P:dchCtpExpectedDtsTTI,_Q:dchCtpDtsTTIMismatchReporting,_R:dchCtpTxDtsTTI,_S:dchCtpRxDtsTTI,_T:dchCtpPreFecThresholdOrder,_U:dchCtpDataPlaneTransparency,_V:dchCtpSignalDegradeReportingControl,_W:dchCtpDtsFecSupport,_X:dchCtpPreFecThresholdMantissa,_Y:dchCtpDtsCv15MinutesTce,_Z:dchCtpDtsEs15MinutesTce,_a:dchCtpDtsSes15MinutesTce,_b:dchCtpDtsCvDayTce,_c:dchCtpDtsEsDayTce,_d:dchCtpDtsSesDayTce,_e:dchCtpDtsCv15MinutesTceReporting,_f:dchCtpDtsEs15MinutesTceReporting,_g:dchCtpDtsSes15MinutesTceReporting,_h:dchCtpDtsCvDayTceReporting,_i:dchCtpDtsEsDayTceReporting,_j:dchCtpDtsSesDayTceReporting,_k:dchCtpPmHistStatsEnable,_l:dchCtpConnectivityVerification,'dchCtpConformance':dchCtpConformance,'dchCtpCompliances':dchCtpCompliances,'dchCtpCompliance':dchCtpCompliance,'dchCtpGroups':dchCtpGroups,_m:dchCtpGroup})