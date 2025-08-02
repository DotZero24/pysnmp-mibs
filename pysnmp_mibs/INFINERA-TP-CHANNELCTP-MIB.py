_h='channelCtpGroup'
_g='channelCtpPmHistStatsEnable'
_f='channelCtpTEEnabled'
_e='channelCtpPrbsMonitoringMode'
_d='channelCtpPrbsGenerationMode'
_c='channelCtpDtsSesDayTceReporting'
_b='channelCtpDtsEsDayTceReporting'
_a='channelCtpDtsCvDayTceReporting'
_Z='channelCtpDtsSes15MinutesTceReporting'
_Y='channelCtpDtsEs15MinutesTceReporting'
_X='channelCtpDtsCv15MinutesTceReporting'
_W='channelCtpDtsSesDayTce'
_V='channelCtpDtsEsDayTce'
_U='channelCtpDtsCvDayTce'
_T='channelCtpDtsSes15MinutesTce'
_S='channelCtpDtsEs15MinutesTce'
_R='channelCtpDtsCv15MinutesTce'
_Q='channelCtpRxDtsTti'
_P='channelCtpExpectedDtsTti'
_O='channelCtpTxDtsTti'
_N='channelCtpDtsTtiAlarmReporting'
_M='channelCtpInsertDtsTti'
_L='channelCtpSignalDegradeReporting'
_K='channelCtpPreFecThresholdMantissa'
_J='channelCtpPreFecThresholdOrder'
_I='ifIndex'
_H='IF-MIB'
_G='enabled'
_F='disabled'
_E='TruthValue'
_D='Integer32'
_C='read-write'
_B='INFINERA-TP-CHANNELCTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_H,_I)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_E)
channelCtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,4))
if mibBuilder.loadTexts:channelCtpMIB.setRevisions(('2008-10-20 00:00',))
_ChannelCtpTable_Object=MibTable
channelCtpTable=_ChannelCtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,4,1))
if mibBuilder.loadTexts:channelCtpTable.setStatus(_A)
_ChannelCtpEntry_Object=MibTableRow
channelCtpEntry=_ChannelCtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,4,1,1))
channelCtpEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:channelCtpEntry.setStatus(_A)
class _ChannelCtpPreFecThresholdOrder_Type(Integer32):defaultValue=-4
_ChannelCtpPreFecThresholdOrder_Type.__name__=_D
_ChannelCtpPreFecThresholdOrder_Object=MibTableColumn
channelCtpPreFecThresholdOrder=_ChannelCtpPreFecThresholdOrder_Object((1,3,6,1,4,1,21296,2,2,2,2,4,1,1,1),_ChannelCtpPreFecThresholdOrder_Type())
channelCtpPreFecThresholdOrder.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpPreFecThresholdOrder.setStatus(_A)
class _ChannelCtpPreFecThresholdMantissa_Type(Integer32):defaultValue=1
_ChannelCtpPreFecThresholdMantissa_Type.__name__=_D
_ChannelCtpPreFecThresholdMantissa_Object=MibTableColumn
channelCtpPreFecThresholdMantissa=_ChannelCtpPreFecThresholdMantissa_Object((1,3,6,1,4,1,21296,2,2,2,2,4,1,1,2),_ChannelCtpPreFecThresholdMantissa_Type())
channelCtpPreFecThresholdMantissa.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpPreFecThresholdMantissa.setStatus(_A)
class _ChannelCtpSignalDegradeReporting_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_ChannelCtpSignalDegradeReporting_Type.__name__=_D
_ChannelCtpSignalDegradeReporting_Object=MibTableColumn
channelCtpSignalDegradeReporting=_ChannelCtpSignalDegradeReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,4,1,1,3),_ChannelCtpSignalDegradeReporting_Type())
channelCtpSignalDegradeReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpSignalDegradeReporting.setStatus(_A)
class _ChannelCtpInsertDtsTti_Type(TruthValue):defaultValue=2
_ChannelCtpInsertDtsTti_Type.__name__=_E
_ChannelCtpInsertDtsTti_Object=MibTableColumn
channelCtpInsertDtsTti=_ChannelCtpInsertDtsTti_Object((1,3,6,1,4,1,21296,2,2,2,2,4,1,1,4),_ChannelCtpInsertDtsTti_Type())
channelCtpInsertDtsTti.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpInsertDtsTti.setStatus(_A)
class _ChannelCtpDtsTtiAlarmReporting_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_ChannelCtpDtsTtiAlarmReporting_Type.__name__=_D
_ChannelCtpDtsTtiAlarmReporting_Object=MibTableColumn
channelCtpDtsTtiAlarmReporting=_ChannelCtpDtsTtiAlarmReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,4,1,1,5),_ChannelCtpDtsTtiAlarmReporting_Type())
channelCtpDtsTtiAlarmReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpDtsTtiAlarmReporting.setStatus(_A)
_ChannelCtpTxDtsTti_Type=DisplayString
_ChannelCtpTxDtsTti_Object=MibTableColumn
channelCtpTxDtsTti=_ChannelCtpTxDtsTti_Object((1,3,6,1,4,1,21296,2,2,2,2,4,1,1,6),_ChannelCtpTxDtsTti_Type())
channelCtpTxDtsTti.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpTxDtsTti.setStatus(_A)
_ChannelCtpExpectedDtsTti_Type=DisplayString
_ChannelCtpExpectedDtsTti_Object=MibTableColumn
channelCtpExpectedDtsTti=_ChannelCtpExpectedDtsTti_Object((1,3,6,1,4,1,21296,2,2,2,2,4,1,1,7),_ChannelCtpExpectedDtsTti_Type())
channelCtpExpectedDtsTti.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpExpectedDtsTti.setStatus(_A)
_ChannelCtpRxDtsTti_Type=DisplayString
_ChannelCtpRxDtsTti_Object=MibTableColumn
channelCtpRxDtsTti=_ChannelCtpRxDtsTti_Object((1,3,6,1,4,1,21296,2,2,2,2,4,1,1,8),_ChannelCtpRxDtsTti_Type())
channelCtpRxDtsTti.setMaxAccess('read-only')
if mibBuilder.loadTexts:channelCtpRxDtsTti.setStatus(_A)
class _ChannelCtpDtsCv15MinutesTce_Type(Integer32):defaultValue=1500
_ChannelCtpDtsCv15MinutesTce_Type.__name__=_D
_ChannelCtpDtsCv15MinutesTce_Object=MibTableColumn
channelCtpDtsCv15MinutesTce=_ChannelCtpDtsCv15MinutesTce_Object((1,3,6,1,4,1,21296,2,2,2,2,4,1,1,9),_ChannelCtpDtsCv15MinutesTce_Type())
channelCtpDtsCv15MinutesTce.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpDtsCv15MinutesTce.setStatus(_A)
class _ChannelCtpDtsEs15MinutesTce_Type(Integer32):defaultValue=120
_ChannelCtpDtsEs15MinutesTce_Type.__name__=_D
_ChannelCtpDtsEs15MinutesTce_Object=MibTableColumn
channelCtpDtsEs15MinutesTce=_ChannelCtpDtsEs15MinutesTce_Object((1,3,6,1,4,1,21296,2,2,2,2,4,1,1,10),_ChannelCtpDtsEs15MinutesTce_Type())
channelCtpDtsEs15MinutesTce.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpDtsEs15MinutesTce.setStatus(_A)
class _ChannelCtpDtsSes15MinutesTce_Type(Integer32):defaultValue=3
_ChannelCtpDtsSes15MinutesTce_Type.__name__=_D
_ChannelCtpDtsSes15MinutesTce_Object=MibTableColumn
channelCtpDtsSes15MinutesTce=_ChannelCtpDtsSes15MinutesTce_Object((1,3,6,1,4,1,21296,2,2,2,2,4,1,1,11),_ChannelCtpDtsSes15MinutesTce_Type())
channelCtpDtsSes15MinutesTce.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpDtsSes15MinutesTce.setStatus(_A)
class _ChannelCtpDtsCvDayTce_Type(Integer32):defaultValue=15000
_ChannelCtpDtsCvDayTce_Type.__name__=_D
_ChannelCtpDtsCvDayTce_Object=MibTableColumn
channelCtpDtsCvDayTce=_ChannelCtpDtsCvDayTce_Object((1,3,6,1,4,1,21296,2,2,2,2,4,1,1,12),_ChannelCtpDtsCvDayTce_Type())
channelCtpDtsCvDayTce.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpDtsCvDayTce.setStatus(_A)
class _ChannelCtpDtsEsDayTce_Type(Integer32):defaultValue=1200
_ChannelCtpDtsEsDayTce_Type.__name__=_D
_ChannelCtpDtsEsDayTce_Object=MibTableColumn
channelCtpDtsEsDayTce=_ChannelCtpDtsEsDayTce_Object((1,3,6,1,4,1,21296,2,2,2,2,4,1,1,13),_ChannelCtpDtsEsDayTce_Type())
channelCtpDtsEsDayTce.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpDtsEsDayTce.setStatus(_A)
class _ChannelCtpDtsSesDayTce_Type(Integer32):defaultValue=7
_ChannelCtpDtsSesDayTce_Type.__name__=_D
_ChannelCtpDtsSesDayTce_Object=MibTableColumn
channelCtpDtsSesDayTce=_ChannelCtpDtsSesDayTce_Object((1,3,6,1,4,1,21296,2,2,2,2,4,1,1,14),_ChannelCtpDtsSesDayTce_Type())
channelCtpDtsSesDayTce.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpDtsSesDayTce.setStatus(_A)
class _ChannelCtpDtsCv15MinutesTceReporting_Type(TruthValue):defaultValue=2
_ChannelCtpDtsCv15MinutesTceReporting_Type.__name__=_E
_ChannelCtpDtsCv15MinutesTceReporting_Object=MibTableColumn
channelCtpDtsCv15MinutesTceReporting=_ChannelCtpDtsCv15MinutesTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,4,1,1,15),_ChannelCtpDtsCv15MinutesTceReporting_Type())
channelCtpDtsCv15MinutesTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpDtsCv15MinutesTceReporting.setStatus(_A)
class _ChannelCtpDtsEs15MinutesTceReporting_Type(TruthValue):defaultValue=2
_ChannelCtpDtsEs15MinutesTceReporting_Type.__name__=_E
_ChannelCtpDtsEs15MinutesTceReporting_Object=MibTableColumn
channelCtpDtsEs15MinutesTceReporting=_ChannelCtpDtsEs15MinutesTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,4,1,1,16),_ChannelCtpDtsEs15MinutesTceReporting_Type())
channelCtpDtsEs15MinutesTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpDtsEs15MinutesTceReporting.setStatus(_A)
class _ChannelCtpDtsSes15MinutesTceReporting_Type(TruthValue):defaultValue=2
_ChannelCtpDtsSes15MinutesTceReporting_Type.__name__=_E
_ChannelCtpDtsSes15MinutesTceReporting_Object=MibTableColumn
channelCtpDtsSes15MinutesTceReporting=_ChannelCtpDtsSes15MinutesTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,4,1,1,17),_ChannelCtpDtsSes15MinutesTceReporting_Type())
channelCtpDtsSes15MinutesTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpDtsSes15MinutesTceReporting.setStatus(_A)
class _ChannelCtpDtsCvDayTceReporting_Type(TruthValue):defaultValue=2
_ChannelCtpDtsCvDayTceReporting_Type.__name__=_E
_ChannelCtpDtsCvDayTceReporting_Object=MibTableColumn
channelCtpDtsCvDayTceReporting=_ChannelCtpDtsCvDayTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,4,1,1,18),_ChannelCtpDtsCvDayTceReporting_Type())
channelCtpDtsCvDayTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpDtsCvDayTceReporting.setStatus(_A)
class _ChannelCtpDtsEsDayTceReporting_Type(TruthValue):defaultValue=2
_ChannelCtpDtsEsDayTceReporting_Type.__name__=_E
_ChannelCtpDtsEsDayTceReporting_Object=MibTableColumn
channelCtpDtsEsDayTceReporting=_ChannelCtpDtsEsDayTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,4,1,1,19),_ChannelCtpDtsEsDayTceReporting_Type())
channelCtpDtsEsDayTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpDtsEsDayTceReporting.setStatus(_A)
class _ChannelCtpDtsSesDayTceReporting_Type(TruthValue):defaultValue=2
_ChannelCtpDtsSesDayTceReporting_Type.__name__=_E
_ChannelCtpDtsSesDayTceReporting_Object=MibTableColumn
channelCtpDtsSesDayTceReporting=_ChannelCtpDtsSesDayTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,4,1,1,20),_ChannelCtpDtsSesDayTceReporting_Type())
channelCtpDtsSesDayTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpDtsSesDayTceReporting.setStatus(_A)
class _ChannelCtpPrbsGenerationMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_ChannelCtpPrbsGenerationMode_Type.__name__=_D
_ChannelCtpPrbsGenerationMode_Object=MibTableColumn
channelCtpPrbsGenerationMode=_ChannelCtpPrbsGenerationMode_Object((1,3,6,1,4,1,21296,2,2,2,2,4,1,1,21),_ChannelCtpPrbsGenerationMode_Type())
channelCtpPrbsGenerationMode.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpPrbsGenerationMode.setStatus(_A)
class _ChannelCtpPrbsMonitoringMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_ChannelCtpPrbsMonitoringMode_Type.__name__=_D
_ChannelCtpPrbsMonitoringMode_Object=MibTableColumn
channelCtpPrbsMonitoringMode=_ChannelCtpPrbsMonitoringMode_Object((1,3,6,1,4,1,21296,2,2,2,2,4,1,1,22),_ChannelCtpPrbsMonitoringMode_Type())
channelCtpPrbsMonitoringMode.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpPrbsMonitoringMode.setStatus(_A)
class _ChannelCtpTEEnabled_Type(TruthValue):defaultValue=1
_ChannelCtpTEEnabled_Type.__name__=_E
_ChannelCtpTEEnabled_Object=MibTableColumn
channelCtpTEEnabled=_ChannelCtpTEEnabled_Object((1,3,6,1,4,1,21296,2,2,2,2,4,1,1,23),_ChannelCtpTEEnabled_Type())
channelCtpTEEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpTEEnabled.setStatus(_A)
class _ChannelCtpPmHistStatsEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_ChannelCtpPmHistStatsEnable_Type.__name__=_D
_ChannelCtpPmHistStatsEnable_Object=MibTableColumn
channelCtpPmHistStatsEnable=_ChannelCtpPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,4,1,1,24),_ChannelCtpPmHistStatsEnable_Type())
channelCtpPmHistStatsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpPmHistStatsEnable.setStatus(_A)
_ChannelCtpConformance_ObjectIdentity=ObjectIdentity
channelCtpConformance=_ChannelCtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,4,3))
_ChannelCtpCompliances_ObjectIdentity=ObjectIdentity
channelCtpCompliances=_ChannelCtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,4,3,1))
_ChannelCtpGroups_ObjectIdentity=ObjectIdentity
channelCtpGroups=_ChannelCtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,4,3,2))
channelCtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,4,3,2,1))
channelCtpGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:channelCtpGroup.setStatus(_A)
channelCtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,4,3,1,1))
channelCtpCompliance.setObjects((_B,_h))
if mibBuilder.loadTexts:channelCtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'channelCtpMIB':channelCtpMIB,'channelCtpTable':channelCtpTable,'channelCtpEntry':channelCtpEntry,_J:channelCtpPreFecThresholdOrder,_K:channelCtpPreFecThresholdMantissa,_L:channelCtpSignalDegradeReporting,_M:channelCtpInsertDtsTti,_N:channelCtpDtsTtiAlarmReporting,_O:channelCtpTxDtsTti,_P:channelCtpExpectedDtsTti,_Q:channelCtpRxDtsTti,_R:channelCtpDtsCv15MinutesTce,_S:channelCtpDtsEs15MinutesTce,_T:channelCtpDtsSes15MinutesTce,_U:channelCtpDtsCvDayTce,_V:channelCtpDtsEsDayTce,_W:channelCtpDtsSesDayTce,_X:channelCtpDtsCv15MinutesTceReporting,_Y:channelCtpDtsEs15MinutesTceReporting,_Z:channelCtpDtsSes15MinutesTceReporting,_a:channelCtpDtsCvDayTceReporting,_b:channelCtpDtsEsDayTceReporting,_c:channelCtpDtsSesDayTceReporting,_d:channelCtpPrbsGenerationMode,_e:channelCtpPrbsMonitoringMode,_f:channelCtpTEEnabled,_g:channelCtpPmHistStatsEnable,'channelCtpConformance':channelCtpConformance,'channelCtpCompliances':channelCtpCompliances,'channelCtpCompliance':channelCtpCompliance,'channelCtpGroups':channelCtpGroups,_h:channelCtpGroup})