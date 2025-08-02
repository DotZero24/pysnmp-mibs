_J='extremeEnhDosPortStatisticsIfIndex'
_I='extremeEnhDosPortRateLimitThreshold'
_H='read-only'
_G='extremeEnhDosPortIfIndex'
_F='read-write'
_E='EXTREME-ENH-DOS-MIB'
_D='TruthValue'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
extremeAgent,extremeV2Traps=mibBuilder.importSymbols('EXTREME-BASE-MIB','extremeAgent','extremeV2Traps')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_D)
extremeEnhDosMib=ModuleIdentity((1,3,6,1,4,1,1916,1,29))
_ExtremeEnhDosProtect_ObjectIdentity=ObjectIdentity
extremeEnhDosProtect=_ExtremeEnhDosProtect_ObjectIdentity((1,3,6,1,4,1,1916,1,29,1))
class _ExtremeEnhDosEnableRateLimit_Type(TruthValue):defaultValue=2
_ExtremeEnhDosEnableRateLimit_Type.__name__=_D
_ExtremeEnhDosEnableRateLimit_Object=MibScalar
extremeEnhDosEnableRateLimit=_ExtremeEnhDosEnableRateLimit_Object((1,3,6,1,4,1,1916,1,29,1,1),_ExtremeEnhDosEnableRateLimit_Type())
extremeEnhDosEnableRateLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:extremeEnhDosEnableRateLimit.setStatus(_A)
class _ExtremeEnhDosEnableIpFdb_Type(TruthValue):defaultValue=2
_ExtremeEnhDosEnableIpFdb_Type.__name__=_D
_ExtremeEnhDosEnableIpFdb_Object=MibScalar
extremeEnhDosEnableIpFdb=_ExtremeEnhDosEnableIpFdb_Object((1,3,6,1,4,1,1916,1,29,1,2),_ExtremeEnhDosEnableIpFdb_Type())
extremeEnhDosEnableIpFdb.setMaxAccess(_F)
if mibBuilder.loadTexts:extremeEnhDosEnableIpFdb.setStatus(_A)
class _ExtremeEnhDosEnableBenchMark_Type(TruthValue):defaultValue=2
_ExtremeEnhDosEnableBenchMark_Type.__name__=_D
_ExtremeEnhDosEnableBenchMark_Object=MibScalar
extremeEnhDosEnableBenchMark=_ExtremeEnhDosEnableBenchMark_Object((1,3,6,1,4,1,1916,1,29,1,3),_ExtremeEnhDosEnableBenchMark_Type())
extremeEnhDosEnableBenchMark.setMaxAccess(_F)
if mibBuilder.loadTexts:extremeEnhDosEnableBenchMark.setStatus(_A)
class _ExtremeEnhDosCacheSize_Type(Integer32):defaultValue=262144;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,262144))
_ExtremeEnhDosCacheSize_Type.__name__=_C
_ExtremeEnhDosCacheSize_Object=MibScalar
extremeEnhDosCacheSize=_ExtremeEnhDosCacheSize_Object((1,3,6,1,4,1,1916,1,29,1,4),_ExtremeEnhDosCacheSize_Type())
extremeEnhDosCacheSize.setMaxAccess(_F)
if mibBuilder.loadTexts:extremeEnhDosCacheSize.setStatus(_A)
_ExtremeEnhDosPortTable_Object=MibTable
extremeEnhDosPortTable=_ExtremeEnhDosPortTable_Object((1,3,6,1,4,1,1916,1,29,1,5))
if mibBuilder.loadTexts:extremeEnhDosPortTable.setStatus(_A)
_ExtremeEnhDosPortEntry_Object=MibTableRow
extremeEnhDosPortEntry=_ExtremeEnhDosPortEntry_Object((1,3,6,1,4,1,1916,1,29,1,5,1))
extremeEnhDosPortEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:extremeEnhDosPortEntry.setStatus(_A)
_ExtremeEnhDosPortIfIndex_Type=Integer32
_ExtremeEnhDosPortIfIndex_Object=MibTableColumn
extremeEnhDosPortIfIndex=_ExtremeEnhDosPortIfIndex_Object((1,3,6,1,4,1,1916,1,29,1,5,1,1),_ExtremeEnhDosPortIfIndex_Type())
extremeEnhDosPortIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:extremeEnhDosPortIfIndex.setStatus(_A)
class _ExtremeEnhDosPortTrusted_Type(TruthValue):defaultValue=2
_ExtremeEnhDosPortTrusted_Type.__name__=_D
_ExtremeEnhDosPortTrusted_Object=MibTableColumn
extremeEnhDosPortTrusted=_ExtremeEnhDosPortTrusted_Object((1,3,6,1,4,1,1916,1,29,1,5,1,2),_ExtremeEnhDosPortTrusted_Type())
extremeEnhDosPortTrusted.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEnhDosPortTrusted.setStatus(_A)
class _ExtremeEnhDosPortAlarmState_Type(TruthValue):defaultValue=2
_ExtremeEnhDosPortAlarmState_Type.__name__=_D
_ExtremeEnhDosPortAlarmState_Object=MibTableColumn
extremeEnhDosPortAlarmState=_ExtremeEnhDosPortAlarmState_Object((1,3,6,1,4,1,1916,1,29,1,5,1,3),_ExtremeEnhDosPortAlarmState_Type())
extremeEnhDosPortAlarmState.setMaxAccess(_H)
if mibBuilder.loadTexts:extremeEnhDosPortAlarmState.setStatus(_A)
class _ExtremeEnhDosPortLearnLimit_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1953125))
_ExtremeEnhDosPortLearnLimit_Type.__name__=_C
_ExtremeEnhDosPortLearnLimit_Object=MibTableColumn
extremeEnhDosPortLearnLimit=_ExtremeEnhDosPortLearnLimit_Object((1,3,6,1,4,1,1916,1,29,1,5,1,4),_ExtremeEnhDosPortLearnLimit_Type())
extremeEnhDosPortLearnLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEnhDosPortLearnLimit.setStatus(_A)
class _ExtremeEnhDosPortLearnWindow_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_ExtremeEnhDosPortLearnWindow_Type.__name__=_C
_ExtremeEnhDosPortLearnWindow_Object=MibTableColumn
extremeEnhDosPortLearnWindow=_ExtremeEnhDosPortLearnWindow_Object((1,3,6,1,4,1,1916,1,29,1,5,1,5),_ExtremeEnhDosPortLearnWindow_Type())
extremeEnhDosPortLearnWindow.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEnhDosPortLearnWindow.setStatus(_A)
class _ExtremeEnhDosPortAgingTime_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_ExtremeEnhDosPortAgingTime_Type.__name__=_C
_ExtremeEnhDosPortAgingTime_Object=MibTableColumn
extremeEnhDosPortAgingTime=_ExtremeEnhDosPortAgingTime_Object((1,3,6,1,4,1,1916,1,29,1,5,1,6),_ExtremeEnhDosPortAgingTime_Type())
extremeEnhDosPortAgingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEnhDosPortAgingTime.setStatus(_A)
class _ExtremeEnhDosPortRateLimitEnable_Type(TruthValue):defaultValue=2
_ExtremeEnhDosPortRateLimitEnable_Type.__name__=_D
_ExtremeEnhDosPortRateLimitEnable_Object=MibTableColumn
extremeEnhDosPortRateLimitEnable=_ExtremeEnhDosPortRateLimitEnable_Object((1,3,6,1,4,1,1916,1,29,1,5,1,7),_ExtremeEnhDosPortRateLimitEnable_Type())
extremeEnhDosPortRateLimitEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEnhDosPortRateLimitEnable.setStatus(_A)
class _ExtremeEnhDosPortIpFdbEnable_Type(TruthValue):defaultValue=2
_ExtremeEnhDosPortIpFdbEnable_Type.__name__=_D
_ExtremeEnhDosPortIpFdbEnable_Object=MibTableColumn
extremeEnhDosPortIpFdbEnable=_ExtremeEnhDosPortIpFdbEnable_Object((1,3,6,1,4,1,1916,1,29,1,5,1,8),_ExtremeEnhDosPortIpFdbEnable_Type())
extremeEnhDosPortIpFdbEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEnhDosPortIpFdbEnable.setStatus(_A)
class _ExtremeEnhDosPortBenchMarkEnable_Type(TruthValue):defaultValue=2
_ExtremeEnhDosPortBenchMarkEnable_Type.__name__=_D
_ExtremeEnhDosPortBenchMarkEnable_Object=MibTableColumn
extremeEnhDosPortBenchMarkEnable=_ExtremeEnhDosPortBenchMarkEnable_Object((1,3,6,1,4,1,1916,1,29,1,5,1,9),_ExtremeEnhDosPortBenchMarkEnable_Type())
extremeEnhDosPortBenchMarkEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEnhDosPortBenchMarkEnable.setStatus(_A)
class _ExtremeEnhDosPortRateLimitThreshold_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1953125))
_ExtremeEnhDosPortRateLimitThreshold_Type.__name__=_C
_ExtremeEnhDosPortRateLimitThreshold_Object=MibTableColumn
extremeEnhDosPortRateLimitThreshold=_ExtremeEnhDosPortRateLimitThreshold_Object((1,3,6,1,4,1,1916,1,29,1,5,1,10),_ExtremeEnhDosPortRateLimitThreshold_Type())
extremeEnhDosPortRateLimitThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEnhDosPortRateLimitThreshold.setStatus(_A)
class _ExtremeEnhDosPortRateLimitDropProbability_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,100))
_ExtremeEnhDosPortRateLimitDropProbability_Type.__name__=_C
_ExtremeEnhDosPortRateLimitDropProbability_Object=MibTableColumn
extremeEnhDosPortRateLimitDropProbability=_ExtremeEnhDosPortRateLimitDropProbability_Object((1,3,6,1,4,1,1916,1,29,1,5,1,11),_ExtremeEnhDosPortRateLimitDropProbability_Type())
extremeEnhDosPortRateLimitDropProbability.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEnhDosPortRateLimitDropProbability.setStatus(_A)
class _ExtremeEnhDosPortRateLimitLearningWindow_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,300))
_ExtremeEnhDosPortRateLimitLearningWindow_Type.__name__=_C
_ExtremeEnhDosPortRateLimitLearningWindow_Object=MibTableColumn
extremeEnhDosPortRateLimitLearningWindow=_ExtremeEnhDosPortRateLimitLearningWindow_Object((1,3,6,1,4,1,1916,1,29,1,5,1,12),_ExtremeEnhDosPortRateLimitLearningWindow_Type())
extremeEnhDosPortRateLimitLearningWindow.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEnhDosPortRateLimitLearningWindow.setStatus(_A)
class _ExtremeEnhDosPortRateLimitProtocol_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('icmp',1),('all',2)))
_ExtremeEnhDosPortRateLimitProtocol_Type.__name__=_C
_ExtremeEnhDosPortRateLimitProtocol_Object=MibTableColumn
extremeEnhDosPortRateLimitProtocol=_ExtremeEnhDosPortRateLimitProtocol_Object((1,3,6,1,4,1,1916,1,29,1,5,1,13),_ExtremeEnhDosPortRateLimitProtocol_Type())
extremeEnhDosPortRateLimitProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEnhDosPortRateLimitProtocol.setStatus(_A)
_ExtremeEnhDosPortStatisticsTable_Object=MibTable
extremeEnhDosPortStatisticsTable=_ExtremeEnhDosPortStatisticsTable_Object((1,3,6,1,4,1,1916,1,29,1,6))
if mibBuilder.loadTexts:extremeEnhDosPortStatisticsTable.setStatus(_A)
_ExtremeEnhDosPortStatisticsEntry_Object=MibTableRow
extremeEnhDosPortStatisticsEntry=_ExtremeEnhDosPortStatisticsEntry_Object((1,3,6,1,4,1,1916,1,29,1,6,1))
extremeEnhDosPortStatisticsEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:extremeEnhDosPortStatisticsEntry.setStatus(_A)
_ExtremeEnhDosPortStatisticsIfIndex_Type=Integer32
_ExtremeEnhDosPortStatisticsIfIndex_Object=MibTableColumn
extremeEnhDosPortStatisticsIfIndex=_ExtremeEnhDosPortStatisticsIfIndex_Object((1,3,6,1,4,1,1916,1,29,1,6,1,1),_ExtremeEnhDosPortStatisticsIfIndex_Type())
extremeEnhDosPortStatisticsIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:extremeEnhDosPortStatisticsIfIndex.setStatus(_A)
_ExtremeEnhDosPortStatisticsRateLimitFilteredPackets_Type=Integer32
_ExtremeEnhDosPortStatisticsRateLimitFilteredPackets_Object=MibTableColumn
extremeEnhDosPortStatisticsRateLimitFilteredPackets=_ExtremeEnhDosPortStatisticsRateLimitFilteredPackets_Object((1,3,6,1,4,1,1916,1,29,1,6,1,2),_ExtremeEnhDosPortStatisticsRateLimitFilteredPackets_Type())
extremeEnhDosPortStatisticsRateLimitFilteredPackets.setMaxAccess(_H)
if mibBuilder.loadTexts:extremeEnhDosPortStatisticsRateLimitFilteredPackets.setStatus(_A)
_ExtremeEnhDosTraps_ObjectIdentity=ObjectIdentity
extremeEnhDosTraps=_ExtremeEnhDosTraps_ObjectIdentity((1,3,6,1,4,1,1916,4,11))
_ExtremeEnhDosTrapsPrefix_ObjectIdentity=ObjectIdentity
extremeEnhDosTrapsPrefix=_ExtremeEnhDosTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,1916,4,11,0))
extremeEnhDosThresholdReached=NotificationType((1,3,6,1,4,1,1916,4,11,0,1))
extremeEnhDosThresholdReached.setObjects(*((_E,_G),(_E,_I)))
if mibBuilder.loadTexts:extremeEnhDosThresholdReached.setStatus(_A)
extremeEnhDosThresholdCleared=NotificationType((1,3,6,1,4,1,1916,4,11,0,2))
extremeEnhDosThresholdCleared.setObjects(*((_E,_G),(_E,_I)))
if mibBuilder.loadTexts:extremeEnhDosThresholdCleared.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'extremeEnhDosMib':extremeEnhDosMib,'extremeEnhDosProtect':extremeEnhDosProtect,'extremeEnhDosEnableRateLimit':extremeEnhDosEnableRateLimit,'extremeEnhDosEnableIpFdb':extremeEnhDosEnableIpFdb,'extremeEnhDosEnableBenchMark':extremeEnhDosEnableBenchMark,'extremeEnhDosCacheSize':extremeEnhDosCacheSize,'extremeEnhDosPortTable':extremeEnhDosPortTable,'extremeEnhDosPortEntry':extremeEnhDosPortEntry,_G:extremeEnhDosPortIfIndex,'extremeEnhDosPortTrusted':extremeEnhDosPortTrusted,'extremeEnhDosPortAlarmState':extremeEnhDosPortAlarmState,'extremeEnhDosPortLearnLimit':extremeEnhDosPortLearnLimit,'extremeEnhDosPortLearnWindow':extremeEnhDosPortLearnWindow,'extremeEnhDosPortAgingTime':extremeEnhDosPortAgingTime,'extremeEnhDosPortRateLimitEnable':extremeEnhDosPortRateLimitEnable,'extremeEnhDosPortIpFdbEnable':extremeEnhDosPortIpFdbEnable,'extremeEnhDosPortBenchMarkEnable':extremeEnhDosPortBenchMarkEnable,_I:extremeEnhDosPortRateLimitThreshold,'extremeEnhDosPortRateLimitDropProbability':extremeEnhDosPortRateLimitDropProbability,'extremeEnhDosPortRateLimitLearningWindow':extremeEnhDosPortRateLimitLearningWindow,'extremeEnhDosPortRateLimitProtocol':extremeEnhDosPortRateLimitProtocol,'extremeEnhDosPortStatisticsTable':extremeEnhDosPortStatisticsTable,'extremeEnhDosPortStatisticsEntry':extremeEnhDosPortStatisticsEntry,_J:extremeEnhDosPortStatisticsIfIndex,'extremeEnhDosPortStatisticsRateLimitFilteredPackets':extremeEnhDosPortStatisticsRateLimitFilteredPackets,'extremeEnhDosTraps':extremeEnhDosTraps,'extremeEnhDosTrapsPrefix':extremeEnhDosTrapsPrefix,'extremeEnhDosThresholdReached':extremeEnhDosThresholdReached,'extremeEnhDosThresholdCleared':extremeEnhDosThresholdCleared})