_P='zxDslPortQueueId'
_O='zxDslMacTableStatSampleIndex'
_N='not-accessible'
_M='dot1dBasePort'
_L='BRIDGE-MIB'
_K='zxDslCardIndex'
_J='second'
_I='read-write'
_H='ifIndex'
_G='IF-MIB'
_F='Integer32'
_E='ZTE-DSL-STATS-MIB'
_D='percent'
_C='BYTES/S'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_L,_M)
ifIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
zxDsl,=mibBuilder.importSymbols('ZTE-DSL-MIB','zxDsl')
zxDslStaticsMib=ModuleIdentity((1,3,6,1,4,1,3902,1004,38))
_ZxDslStatsObjects_ObjectIdentity=ObjectIdentity
zxDslStatsObjects=_ZxDslStatsObjects_ObjectIdentity((1,3,6,1,4,1,3902,1004,38,1))
_ZxDslEtherStatsTable_Object=MibTable
zxDslEtherStatsTable=_ZxDslEtherStatsTable_Object((1,3,6,1,4,1,3902,1004,38,1,1))
if mibBuilder.loadTexts:zxDslEtherStatsTable.setStatus(_A)
_ZxDslEtherStatsEntry_Object=MibTableRow
zxDslEtherStatsEntry=_ZxDslEtherStatsEntry_Object((1,3,6,1,4,1,3902,1004,38,1,1,1))
zxDslEtherStatsEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:zxDslEtherStatsEntry.setStatus(_A)
_ZxDslEtherRxRate_Type=Gauge32
_ZxDslEtherRxRate_Object=MibTableColumn
zxDslEtherRxRate=_ZxDslEtherRxRate_Object((1,3,6,1,4,1,3902,1004,38,1,1,1,1),_ZxDslEtherRxRate_Type())
zxDslEtherRxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslEtherRxRate.setStatus(_A)
if mibBuilder.loadTexts:zxDslEtherRxRate.setUnits(_C)
_ZxDslEtherTxRate_Type=Gauge32
_ZxDslEtherTxRate_Object=MibTableColumn
zxDslEtherTxRate=_ZxDslEtherTxRate_Object((1,3,6,1,4,1,3902,1004,38,1,1,1,2),_ZxDslEtherTxRate_Type())
zxDslEtherTxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslEtherTxRate.setStatus(_A)
if mibBuilder.loadTexts:zxDslEtherTxRate.setUnits(_C)
_ZxDslEtherRxDiscardRatio_Type=Integer32
_ZxDslEtherRxDiscardRatio_Object=MibTableColumn
zxDslEtherRxDiscardRatio=_ZxDslEtherRxDiscardRatio_Object((1,3,6,1,4,1,3902,1004,38,1,1,1,3),_ZxDslEtherRxDiscardRatio_Type())
zxDslEtherRxDiscardRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslEtherRxDiscardRatio.setStatus(_A)
if mibBuilder.loadTexts:zxDslEtherRxDiscardRatio.setUnits(_D)
_ZxDslEtherTxDiscardRatio_Type=Integer32
_ZxDslEtherTxDiscardRatio_Object=MibTableColumn
zxDslEtherTxDiscardRatio=_ZxDslEtherTxDiscardRatio_Object((1,3,6,1,4,1,3902,1004,38,1,1,1,4),_ZxDslEtherTxDiscardRatio_Type())
zxDslEtherTxDiscardRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslEtherTxDiscardRatio.setStatus(_A)
if mibBuilder.loadTexts:zxDslEtherTxDiscardRatio.setUnits(_D)
_ZxDslEtherBroadcastRxRate_Type=Gauge32
_ZxDslEtherBroadcastRxRate_Object=MibTableColumn
zxDslEtherBroadcastRxRate=_ZxDslEtherBroadcastRxRate_Object((1,3,6,1,4,1,3902,1004,38,1,1,1,5),_ZxDslEtherBroadcastRxRate_Type())
zxDslEtherBroadcastRxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslEtherBroadcastRxRate.setStatus(_A)
if mibBuilder.loadTexts:zxDslEtherBroadcastRxRate.setUnits(_C)
_ZxDslEtherBroadcastTxRate_Type=Gauge32
_ZxDslEtherBroadcastTxRate_Object=MibTableColumn
zxDslEtherBroadcastTxRate=_ZxDslEtherBroadcastTxRate_Object((1,3,6,1,4,1,3902,1004,38,1,1,1,6),_ZxDslEtherBroadcastTxRate_Type())
zxDslEtherBroadcastTxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslEtherBroadcastTxRate.setStatus(_A)
if mibBuilder.loadTexts:zxDslEtherBroadcastTxRate.setUnits(_C)
_ZxDslEtherMulticastRxRate_Type=Gauge32
_ZxDslEtherMulticastRxRate_Object=MibTableColumn
zxDslEtherMulticastRxRate=_ZxDslEtherMulticastRxRate_Object((1,3,6,1,4,1,3902,1004,38,1,1,1,7),_ZxDslEtherMulticastRxRate_Type())
zxDslEtherMulticastRxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslEtherMulticastRxRate.setStatus(_A)
if mibBuilder.loadTexts:zxDslEtherMulticastRxRate.setUnits(_C)
_ZxDslEtherMulticastTxRate_Type=Gauge32
_ZxDslEtherMulticastTxRate_Object=MibTableColumn
zxDslEtherMulticastTxRate=_ZxDslEtherMulticastTxRate_Object((1,3,6,1,4,1,3902,1004,38,1,1,1,8),_ZxDslEtherMulticastTxRate_Type())
zxDslEtherMulticastTxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslEtherMulticastTxRate.setStatus(_A)
if mibBuilder.loadTexts:zxDslEtherMulticastTxRate.setUnits(_C)
_ZxDslEtherUnicastRxRate_Type=Gauge32
_ZxDslEtherUnicastRxRate_Object=MibTableColumn
zxDslEtherUnicastRxRate=_ZxDslEtherUnicastRxRate_Object((1,3,6,1,4,1,3902,1004,38,1,1,1,9),_ZxDslEtherUnicastRxRate_Type())
zxDslEtherUnicastRxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslEtherUnicastRxRate.setStatus(_A)
if mibBuilder.loadTexts:zxDslEtherUnicastRxRate.setUnits(_C)
_ZxDslEtherUnicastTxRate_Type=Gauge32
_ZxDslEtherUnicastTxRate_Object=MibTableColumn
zxDslEtherUnicastTxRate=_ZxDslEtherUnicastTxRate_Object((1,3,6,1,4,1,3902,1004,38,1,1,1,10),_ZxDslEtherUnicastTxRate_Type())
zxDslEtherUnicastTxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslEtherUnicastTxRate.setStatus(_A)
if mibBuilder.loadTexts:zxDslEtherUnicastTxRate.setUnits(_C)
_ZxDslBridgePortStatsTable_Object=MibTable
zxDslBridgePortStatsTable=_ZxDslBridgePortStatsTable_Object((1,3,6,1,4,1,3902,1004,38,1,2))
if mibBuilder.loadTexts:zxDslBridgePortStatsTable.setStatus(_A)
_ZxDslBridgePortStatsEntry_Object=MibTableRow
zxDslBridgePortStatsEntry=_ZxDslBridgePortStatsEntry_Object((1,3,6,1,4,1,3902,1004,38,1,2,1))
zxDslBridgePortStatsEntry.setIndexNames((0,_E,_K),(0,_L,_M))
if mibBuilder.loadTexts:zxDslBridgePortStatsEntry.setStatus(_A)
_ZxDslBridgePortRxRate_Type=Gauge32
_ZxDslBridgePortRxRate_Object=MibTableColumn
zxDslBridgePortRxRate=_ZxDslBridgePortRxRate_Object((1,3,6,1,4,1,3902,1004,38,1,2,1,1),_ZxDslBridgePortRxRate_Type())
zxDslBridgePortRxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslBridgePortRxRate.setStatus(_A)
if mibBuilder.loadTexts:zxDslBridgePortRxRate.setUnits(_C)
_ZxDslBridgePortTxRate_Type=Gauge32
_ZxDslBridgePortTxRate_Object=MibTableColumn
zxDslBridgePortTxRate=_ZxDslBridgePortTxRate_Object((1,3,6,1,4,1,3902,1004,38,1,2,1,2),_ZxDslBridgePortTxRate_Type())
zxDslBridgePortTxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslBridgePortTxRate.setStatus(_A)
if mibBuilder.loadTexts:zxDslBridgePortTxRate.setUnits(_C)
_ZxDslBridgePortSelfLoopPkts_Type=Counter32
_ZxDslBridgePortSelfLoopPkts_Object=MibTableColumn
zxDslBridgePortSelfLoopPkts=_ZxDslBridgePortSelfLoopPkts_Object((1,3,6,1,4,1,3902,1004,38,1,2,1,3),_ZxDslBridgePortSelfLoopPkts_Type())
zxDslBridgePortSelfLoopPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslBridgePortSelfLoopPkts.setStatus(_A)
_ZxDslCardResourcesPerfTable_Object=MibTable
zxDslCardResourcesPerfTable=_ZxDslCardResourcesPerfTable_Object((1,3,6,1,4,1,3902,1004,38,1,3))
if mibBuilder.loadTexts:zxDslCardResourcesPerfTable.setStatus(_A)
_ZxDslCardResourcesPerfEntry_Object=MibTableRow
zxDslCardResourcesPerfEntry=_ZxDslCardResourcesPerfEntry_Object((1,3,6,1,4,1,3902,1004,38,1,3,1))
zxDslCardResourcesPerfEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:zxDslCardResourcesPerfEntry.setStatus(_A)
_ZxDslCardIndex_Type=Integer32
_ZxDslCardIndex_Object=MibTableColumn
zxDslCardIndex=_ZxDslCardIndex_Object((1,3,6,1,4,1,3902,1004,38,1,3,1,1),_ZxDslCardIndex_Type())
zxDslCardIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:zxDslCardIndex.setStatus(_A)
_ZxDslCardCPULoad_Type=Integer32
_ZxDslCardCPULoad_Object=MibTableColumn
zxDslCardCPULoad=_ZxDslCardCPULoad_Object((1,3,6,1,4,1,3902,1004,38,1,3,1,2),_ZxDslCardCPULoad_Type())
zxDslCardCPULoad.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslCardCPULoad.setStatus(_A)
if mibBuilder.loadTexts:zxDslCardCPULoad.setUnits(_D)
_ZxDslCardMemUsage_Type=Integer32
_ZxDslCardMemUsage_Object=MibTableColumn
zxDslCardMemUsage=_ZxDslCardMemUsage_Object((1,3,6,1,4,1,3902,1004,38,1,3,1,3),_ZxDslCardMemUsage_Type())
zxDslCardMemUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslCardMemUsage.setStatus(_A)
_ZxDslCardActivedPortNum_Type=Integer32
_ZxDslCardActivedPortNum_Object=MibTableColumn
zxDslCardActivedPortNum=_ZxDslCardActivedPortNum_Object((1,3,6,1,4,1,3902,1004,38,1,3,1,4),_ZxDslCardActivedPortNum_Type())
zxDslCardActivedPortNum.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslCardActivedPortNum.setStatus(_A)
_ZxDslL2ResourcesStat_ObjectIdentity=ObjectIdentity
zxDslL2ResourcesStat=_ZxDslL2ResourcesStat_ObjectIdentity((1,3,6,1,4,1,3902,1004,38,1,4))
class _ZxDslMacTableUsageMornitorPeriod_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(300,86400))
_ZxDslMacTableUsageMornitorPeriod_Type.__name__=_F
_ZxDslMacTableUsageMornitorPeriod_Object=MibScalar
zxDslMacTableUsageMornitorPeriod=_ZxDslMacTableUsageMornitorPeriod_Object((1,3,6,1,4,1,3902,1004,38,1,4,1),_ZxDslMacTableUsageMornitorPeriod_Type())
zxDslMacTableUsageMornitorPeriod.setMaxAccess(_I)
if mibBuilder.loadTexts:zxDslMacTableUsageMornitorPeriod.setStatus(_A)
if mibBuilder.loadTexts:zxDslMacTableUsageMornitorPeriod.setUnits(_J)
class _ZxDslMacTableUsageMornitorTimes_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_ZxDslMacTableUsageMornitorTimes_Type.__name__=_F
_ZxDslMacTableUsageMornitorTimes_Object=MibScalar
zxDslMacTableUsageMornitorTimes=_ZxDslMacTableUsageMornitorTimes_Object((1,3,6,1,4,1,3902,1004,38,1,4,2),_ZxDslMacTableUsageMornitorTimes_Type())
zxDslMacTableUsageMornitorTimes.setMaxAccess(_I)
if mibBuilder.loadTexts:zxDslMacTableUsageMornitorTimes.setStatus(_A)
_ZxDslMacTableUsageMornitorElapsedTime_Type=Integer32
_ZxDslMacTableUsageMornitorElapsedTime_Object=MibScalar
zxDslMacTableUsageMornitorElapsedTime=_ZxDslMacTableUsageMornitorElapsedTime_Object((1,3,6,1,4,1,3902,1004,38,1,4,3),_ZxDslMacTableUsageMornitorElapsedTime_Type())
zxDslMacTableUsageMornitorElapsedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslMacTableUsageMornitorElapsedTime.setStatus(_A)
if mibBuilder.loadTexts:zxDslMacTableUsageMornitorElapsedTime.setUnits(_J)
_ZxDslMacTableMaxSize_Type=Integer32
_ZxDslMacTableMaxSize_Object=MibScalar
zxDslMacTableMaxSize=_ZxDslMacTableMaxSize_Object((1,3,6,1,4,1,3902,1004,38,1,4,4),_ZxDslMacTableMaxSize_Type())
zxDslMacTableMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslMacTableMaxSize.setStatus(_A)
_ZxDslMacTableCurrentUsage_Type=Integer32
_ZxDslMacTableCurrentUsage_Object=MibScalar
zxDslMacTableCurrentUsage=_ZxDslMacTableCurrentUsage_Object((1,3,6,1,4,1,3902,1004,38,1,4,5),_ZxDslMacTableCurrentUsage_Type())
zxDslMacTableCurrentUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslMacTableCurrentUsage.setStatus(_A)
if mibBuilder.loadTexts:zxDslMacTableCurrentUsage.setUnits(_D)
class _ZxDslMacTableUsageThreshold_Type(Integer32):defaultValue=70
_ZxDslMacTableUsageThreshold_Type.__name__=_F
_ZxDslMacTableUsageThreshold_Object=MibScalar
zxDslMacTableUsageThreshold=_ZxDslMacTableUsageThreshold_Object((1,3,6,1,4,1,3902,1004,38,1,4,6),_ZxDslMacTableUsageThreshold_Type())
zxDslMacTableUsageThreshold.setMaxAccess(_I)
if mibBuilder.loadTexts:zxDslMacTableUsageThreshold.setStatus(_A)
if mibBuilder.loadTexts:zxDslMacTableUsageThreshold.setUnits(_D)
_ZxDslMacTableStatTable_Object=MibTable
zxDslMacTableStatTable=_ZxDslMacTableStatTable_Object((1,3,6,1,4,1,3902,1004,38,1,4,7))
if mibBuilder.loadTexts:zxDslMacTableStatTable.setStatus(_A)
_ZxDslMacTableStatEntry_Object=MibTableRow
zxDslMacTableStatEntry=_ZxDslMacTableStatEntry_Object((1,3,6,1,4,1,3902,1004,38,1,4,7,1))
zxDslMacTableStatEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:zxDslMacTableStatEntry.setStatus(_A)
_ZxDslMacTableStatSampleIndex_Type=Integer32
_ZxDslMacTableStatSampleIndex_Object=MibTableColumn
zxDslMacTableStatSampleIndex=_ZxDslMacTableStatSampleIndex_Object((1,3,6,1,4,1,3902,1004,38,1,4,7,1,1),_ZxDslMacTableStatSampleIndex_Type())
zxDslMacTableStatSampleIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:zxDslMacTableStatSampleIndex.setStatus(_A)
_ZxDslMacTableCurrentMaxUsage_Type=Integer32
_ZxDslMacTableCurrentMaxUsage_Object=MibTableColumn
zxDslMacTableCurrentMaxUsage=_ZxDslMacTableCurrentMaxUsage_Object((1,3,6,1,4,1,3902,1004,38,1,4,7,1,2),_ZxDslMacTableCurrentMaxUsage_Type())
zxDslMacTableCurrentMaxUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslMacTableCurrentMaxUsage.setStatus(_A)
if mibBuilder.loadTexts:zxDslMacTableCurrentMaxUsage.setUnits(_D)
_ZxDslPortQueueSampleTable_Object=MibTable
zxDslPortQueueSampleTable=_ZxDslPortQueueSampleTable_Object((1,3,6,1,4,1,3902,1004,38,1,4,8))
if mibBuilder.loadTexts:zxDslPortQueueSampleTable.setStatus(_A)
_ZxDslPortQueueSampleEntry_Object=MibTableRow
zxDslPortQueueSampleEntry=_ZxDslPortQueueSampleEntry_Object((1,3,6,1,4,1,3902,1004,38,1,4,8,1))
zxDslPortQueueSampleEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:zxDslPortQueueSampleEntry.setStatus(_A)
class _ZxDslQueueUsageMornitorPeriod_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(300,86400))
_ZxDslQueueUsageMornitorPeriod_Type.__name__=_F
_ZxDslQueueUsageMornitorPeriod_Object=MibTableColumn
zxDslQueueUsageMornitorPeriod=_ZxDslQueueUsageMornitorPeriod_Object((1,3,6,1,4,1,3902,1004,38,1,4,8,1,1),_ZxDslQueueUsageMornitorPeriod_Type())
zxDslQueueUsageMornitorPeriod.setMaxAccess(_I)
if mibBuilder.loadTexts:zxDslQueueUsageMornitorPeriod.setStatus(_A)
if mibBuilder.loadTexts:zxDslQueueUsageMornitorPeriod.setUnits(_J)
_ZxDslQueueUsageMornitorElapsedTime_Type=Integer32
_ZxDslQueueUsageMornitorElapsedTime_Object=MibTableColumn
zxDslQueueUsageMornitorElapsedTime=_ZxDslQueueUsageMornitorElapsedTime_Object((1,3,6,1,4,1,3902,1004,38,1,4,8,1,2),_ZxDslQueueUsageMornitorElapsedTime_Type())
zxDslQueueUsageMornitorElapsedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslQueueUsageMornitorElapsedTime.setStatus(_A)
if mibBuilder.loadTexts:zxDslQueueUsageMornitorElapsedTime.setUnits(_J)
_ZxDslPortQueueStatTable_Object=MibTable
zxDslPortQueueStatTable=_ZxDslPortQueueStatTable_Object((1,3,6,1,4,1,3902,1004,38,1,4,9))
if mibBuilder.loadTexts:zxDslPortQueueStatTable.setStatus(_A)
_ZxDslPortQueueStatEntry_Object=MibTableRow
zxDslPortQueueStatEntry=_ZxDslPortQueueStatEntry_Object((1,3,6,1,4,1,3902,1004,38,1,4,9,1))
zxDslPortQueueStatEntry.setIndexNames((0,_G,_H),(0,_E,_P))
if mibBuilder.loadTexts:zxDslPortQueueStatEntry.setStatus(_A)
_ZxDslPortQueueId_Type=Integer32
_ZxDslPortQueueId_Object=MibTableColumn
zxDslPortQueueId=_ZxDslPortQueueId_Object((1,3,6,1,4,1,3902,1004,38,1,4,9,1,1),_ZxDslPortQueueId_Type())
zxDslPortQueueId.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslPortQueueId.setStatus(_A)
if mibBuilder.loadTexts:zxDslPortQueueId.setUnits('byte')
_ZxDslPortQueueMaxSize_Type=Integer32
_ZxDslPortQueueMaxSize_Object=MibTableColumn
zxDslPortQueueMaxSize=_ZxDslPortQueueMaxSize_Object((1,3,6,1,4,1,3902,1004,38,1,4,9,1,2),_ZxDslPortQueueMaxSize_Type())
zxDslPortQueueMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslPortQueueMaxSize.setStatus(_A)
if mibBuilder.loadTexts:zxDslPortQueueMaxSize.setUnits('byte')
_ZxDslPortQueueCurrentUsage_Type=Integer32
_ZxDslPortQueueCurrentUsage_Object=MibTableColumn
zxDslPortQueueCurrentUsage=_ZxDslPortQueueCurrentUsage_Object((1,3,6,1,4,1,3902,1004,38,1,4,9,1,3),_ZxDslPortQueueCurrentUsage_Type())
zxDslPortQueueCurrentUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslPortQueueCurrentUsage.setStatus(_A)
if mibBuilder.loadTexts:zxDslPortQueueCurrentUsage.setUnits(_D)
_ZxDslPortQueueStatMinUsage_Type=Integer32
_ZxDslPortQueueStatMinUsage_Object=MibTableColumn
zxDslPortQueueStatMinUsage=_ZxDslPortQueueStatMinUsage_Object((1,3,6,1,4,1,3902,1004,38,1,4,9,1,4),_ZxDslPortQueueStatMinUsage_Type())
zxDslPortQueueStatMinUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslPortQueueStatMinUsage.setStatus(_A)
if mibBuilder.loadTexts:zxDslPortQueueStatMinUsage.setUnits(_D)
_ZxDslPortQueueStatAverageUsage_Type=Integer32
_ZxDslPortQueueStatAverageUsage_Object=MibTableColumn
zxDslPortQueueStatAverageUsage=_ZxDslPortQueueStatAverageUsage_Object((1,3,6,1,4,1,3902,1004,38,1,4,9,1,5),_ZxDslPortQueueStatAverageUsage_Type())
zxDslPortQueueStatAverageUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslPortQueueStatAverageUsage.setStatus(_A)
if mibBuilder.loadTexts:zxDslPortQueueStatAverageUsage.setUnits(_D)
_ZxDslPortQueueStatMaxUsage_Type=Integer32
_ZxDslPortQueueStatMaxUsage_Object=MibTableColumn
zxDslPortQueueStatMaxUsage=_ZxDslPortQueueStatMaxUsage_Object((1,3,6,1,4,1,3902,1004,38,1,4,9,1,6),_ZxDslPortQueueStatMaxUsage_Type())
zxDslPortQueueStatMaxUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslPortQueueStatMaxUsage.setStatus(_A)
if mibBuilder.loadTexts:zxDslPortQueueStatMaxUsage.setUnits(_D)
class _ZxDslMacTablePeakValue_Type(Integer32):defaultValue=70
_ZxDslMacTablePeakValue_Type.__name__=_F
_ZxDslMacTablePeakValue_Object=MibScalar
zxDslMacTablePeakValue=_ZxDslMacTablePeakValue_Object((1,3,6,1,4,1,3902,1004,38,1,4,10),_ZxDslMacTablePeakValue_Type())
zxDslMacTablePeakValue.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslMacTablePeakValue.setStatus(_A)
_ZxDslStatsTrapObjects_ObjectIdentity=ObjectIdentity
zxDslStatsTrapObjects=_ZxDslStatsTrapObjects_ObjectIdentity((1,3,6,1,4,1,3902,1004,38,2))
zxDslMacTableUsageOverThreshTrap=NotificationType((1,3,6,1,4,1,3902,1004,38,2,1))
zxDslMacTableUsageOverThreshTrap.setObjects(*((_E,'zxAnMacTableCurrentUsage'),(_E,'zxAnMacTableUsageThreshold')))
if mibBuilder.loadTexts:zxDslMacTableUsageOverThreshTrap.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'zxDslStaticsMib':zxDslStaticsMib,'zxDslStatsObjects':zxDslStatsObjects,'zxDslEtherStatsTable':zxDslEtherStatsTable,'zxDslEtherStatsEntry':zxDslEtherStatsEntry,'zxDslEtherRxRate':zxDslEtherRxRate,'zxDslEtherTxRate':zxDslEtherTxRate,'zxDslEtherRxDiscardRatio':zxDslEtherRxDiscardRatio,'zxDslEtherTxDiscardRatio':zxDslEtherTxDiscardRatio,'zxDslEtherBroadcastRxRate':zxDslEtherBroadcastRxRate,'zxDslEtherBroadcastTxRate':zxDslEtherBroadcastTxRate,'zxDslEtherMulticastRxRate':zxDslEtherMulticastRxRate,'zxDslEtherMulticastTxRate':zxDslEtherMulticastTxRate,'zxDslEtherUnicastRxRate':zxDslEtherUnicastRxRate,'zxDslEtherUnicastTxRate':zxDslEtherUnicastTxRate,'zxDslBridgePortStatsTable':zxDslBridgePortStatsTable,'zxDslBridgePortStatsEntry':zxDslBridgePortStatsEntry,'zxDslBridgePortRxRate':zxDslBridgePortRxRate,'zxDslBridgePortTxRate':zxDslBridgePortTxRate,'zxDslBridgePortSelfLoopPkts':zxDslBridgePortSelfLoopPkts,'zxDslCardResourcesPerfTable':zxDslCardResourcesPerfTable,'zxDslCardResourcesPerfEntry':zxDslCardResourcesPerfEntry,_K:zxDslCardIndex,'zxDslCardCPULoad':zxDslCardCPULoad,'zxDslCardMemUsage':zxDslCardMemUsage,'zxDslCardActivedPortNum':zxDslCardActivedPortNum,'zxDslL2ResourcesStat':zxDslL2ResourcesStat,'zxDslMacTableUsageMornitorPeriod':zxDslMacTableUsageMornitorPeriod,'zxDslMacTableUsageMornitorTimes':zxDslMacTableUsageMornitorTimes,'zxDslMacTableUsageMornitorElapsedTime':zxDslMacTableUsageMornitorElapsedTime,'zxDslMacTableMaxSize':zxDslMacTableMaxSize,'zxDslMacTableCurrentUsage':zxDslMacTableCurrentUsage,'zxDslMacTableUsageThreshold':zxDslMacTableUsageThreshold,'zxDslMacTableStatTable':zxDslMacTableStatTable,'zxDslMacTableStatEntry':zxDslMacTableStatEntry,_O:zxDslMacTableStatSampleIndex,'zxDslMacTableCurrentMaxUsage':zxDslMacTableCurrentMaxUsage,'zxDslPortQueueSampleTable':zxDslPortQueueSampleTable,'zxDslPortQueueSampleEntry':zxDslPortQueueSampleEntry,'zxDslQueueUsageMornitorPeriod':zxDslQueueUsageMornitorPeriod,'zxDslQueueUsageMornitorElapsedTime':zxDslQueueUsageMornitorElapsedTime,'zxDslPortQueueStatTable':zxDslPortQueueStatTable,'zxDslPortQueueStatEntry':zxDslPortQueueStatEntry,_P:zxDslPortQueueId,'zxDslPortQueueMaxSize':zxDslPortQueueMaxSize,'zxDslPortQueueCurrentUsage':zxDslPortQueueCurrentUsage,'zxDslPortQueueStatMinUsage':zxDslPortQueueStatMinUsage,'zxDslPortQueueStatAverageUsage':zxDslPortQueueStatAverageUsage,'zxDslPortQueueStatMaxUsage':zxDslPortQueueStatMaxUsage,'zxDslMacTablePeakValue':zxDslMacTablePeakValue,'zxDslStatsTrapObjects':zxDslStatsTrapObjects,'zxDslMacTableUsageOverThreshTrap':zxDslMacTableUsageOverThreshTrap})