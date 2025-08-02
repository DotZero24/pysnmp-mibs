_H='rlInterfaceQueueStatisticsDP'
_G='rlInterfaceQueueStatisticsQueue'
_F='rlInterfaceQueueStatisticsIfIndex'
_E='Integer32'
_D='not-accessible'
_C='read-only'
_B='CISCOSB-QUEUE-STATISTICS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
switch001,=mibBuilder.importSymbols('CISCOSB-MIB','switch001')
StatisticsDPType,=mibBuilder.importSymbols('CISCOSB-POLICY-MIB','StatisticsDPType')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
rlQueueStatistics=ModuleIdentity((1,3,6,1,4,1,9,6,1,101,233))
if mibBuilder.loadTexts:rlQueueStatistics.setRevisions(('2016-07-07 00:00',))
_RlInterfaceQueueStatisticsClear_Type=InterfaceIndexOrZero
_RlInterfaceQueueStatisticsClear_Object=MibScalar
rlInterfaceQueueStatisticsClear=_RlInterfaceQueueStatisticsClear_Object((1,3,6,1,4,1,9,6,1,101,233,1),_RlInterfaceQueueStatisticsClear_Type())
rlInterfaceQueueStatisticsClear.setMaxAccess('read-write')
if mibBuilder.loadTexts:rlInterfaceQueueStatisticsClear.setStatus(_A)
_RlInterfaceQueueStatisticsTable_Object=MibTable
rlInterfaceQueueStatisticsTable=_RlInterfaceQueueStatisticsTable_Object((1,3,6,1,4,1,9,6,1,101,233,2))
if mibBuilder.loadTexts:rlInterfaceQueueStatisticsTable.setStatus(_A)
_RlInterfaceQueueStatisticsEntry_Object=MibTableRow
rlInterfaceQueueStatisticsEntry=_RlInterfaceQueueStatisticsEntry_Object((1,3,6,1,4,1,9,6,1,101,233,2,1))
rlInterfaceQueueStatisticsEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:rlInterfaceQueueStatisticsEntry.setStatus(_A)
_RlInterfaceQueueStatisticsIfIndex_Type=InterfaceIndex
_RlInterfaceQueueStatisticsIfIndex_Object=MibTableColumn
rlInterfaceQueueStatisticsIfIndex=_RlInterfaceQueueStatisticsIfIndex_Object((1,3,6,1,4,1,9,6,1,101,233,2,1,1),_RlInterfaceQueueStatisticsIfIndex_Type())
rlInterfaceQueueStatisticsIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:rlInterfaceQueueStatisticsIfIndex.setStatus(_A)
class _RlInterfaceQueueStatisticsQueue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_RlInterfaceQueueStatisticsQueue_Type.__name__=_E
_RlInterfaceQueueStatisticsQueue_Object=MibTableColumn
rlInterfaceQueueStatisticsQueue=_RlInterfaceQueueStatisticsQueue_Object((1,3,6,1,4,1,9,6,1,101,233,2,1,2),_RlInterfaceQueueStatisticsQueue_Type())
rlInterfaceQueueStatisticsQueue.setMaxAccess(_D)
if mibBuilder.loadTexts:rlInterfaceQueueStatisticsQueue.setStatus(_A)
_RlInterfaceQueueStatisticsDP_Type=StatisticsDPType
_RlInterfaceQueueStatisticsDP_Object=MibTableColumn
rlInterfaceQueueStatisticsDP=_RlInterfaceQueueStatisticsDP_Object((1,3,6,1,4,1,9,6,1,101,233,2,1,3),_RlInterfaceQueueStatisticsDP_Type())
rlInterfaceQueueStatisticsDP.setMaxAccess(_D)
if mibBuilder.loadTexts:rlInterfaceQueueStatisticsDP.setStatus(_A)
_RlInterfaceQueueStatisticsTxPackets_Type=Counter64
_RlInterfaceQueueStatisticsTxPackets_Object=MibTableColumn
rlInterfaceQueueStatisticsTxPackets=_RlInterfaceQueueStatisticsTxPackets_Object((1,3,6,1,4,1,9,6,1,101,233,2,1,4),_RlInterfaceQueueStatisticsTxPackets_Type())
rlInterfaceQueueStatisticsTxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:rlInterfaceQueueStatisticsTxPackets.setStatus(_A)
_RlInterfaceQueueStatisticsTxBytes_Type=Counter64
_RlInterfaceQueueStatisticsTxBytes_Object=MibTableColumn
rlInterfaceQueueStatisticsTxBytes=_RlInterfaceQueueStatisticsTxBytes_Object((1,3,6,1,4,1,9,6,1,101,233,2,1,5),_RlInterfaceQueueStatisticsTxBytes_Type())
rlInterfaceQueueStatisticsTxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:rlInterfaceQueueStatisticsTxBytes.setStatus(_A)
_RlInterfaceQueueStatisticsDroppedPackets_Type=Counter64
_RlInterfaceQueueStatisticsDroppedPackets_Object=MibTableColumn
rlInterfaceQueueStatisticsDroppedPackets=_RlInterfaceQueueStatisticsDroppedPackets_Object((1,3,6,1,4,1,9,6,1,101,233,2,1,6),_RlInterfaceQueueStatisticsDroppedPackets_Type())
rlInterfaceQueueStatisticsDroppedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:rlInterfaceQueueStatisticsDroppedPackets.setStatus(_A)
_RlInterfaceQueueStatisticsDroppedBytes_Type=Counter64
_RlInterfaceQueueStatisticsDroppedBytes_Object=MibTableColumn
rlInterfaceQueueStatisticsDroppedBytes=_RlInterfaceQueueStatisticsDroppedBytes_Object((1,3,6,1,4,1,9,6,1,101,233,2,1,7),_RlInterfaceQueueStatisticsDroppedBytes_Type())
rlInterfaceQueueStatisticsDroppedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:rlInterfaceQueueStatisticsDroppedBytes.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'rlQueueStatistics':rlQueueStatistics,'rlInterfaceQueueStatisticsClear':rlInterfaceQueueStatisticsClear,'rlInterfaceQueueStatisticsTable':rlInterfaceQueueStatisticsTable,'rlInterfaceQueueStatisticsEntry':rlInterfaceQueueStatisticsEntry,_F:rlInterfaceQueueStatisticsIfIndex,_G:rlInterfaceQueueStatisticsQueue,_H:rlInterfaceQueueStatisticsDP,'rlInterfaceQueueStatisticsTxPackets':rlInterfaceQueueStatisticsTxPackets,'rlInterfaceQueueStatisticsTxBytes':rlInterfaceQueueStatisticsTxBytes,'rlInterfaceQueueStatisticsDroppedPackets':rlInterfaceQueueStatisticsDroppedPackets,'rlInterfaceQueueStatisticsDroppedBytes':rlInterfaceQueueStatisticsDroppedBytes})