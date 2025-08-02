_O='aristaPfcGroup'
_N='aristaPfcWatchdogTxQueueRecoveredCount'
_M='aristaPfcWatchdogTxQueueStuckCount'
_L='aristaPfcPriorityIndications'
_K='aristaPfcPriorityRequests'
_J='aristaPfcWatchdogTxQueueId'
_I='aristaPfcWatchdogTxQueueType'
_H='aristaPfcWatchdogIfIndex'
_G='aristaPfcPriorityIndex'
_F='aristaPfcIfIndex'
_E='Integer32'
_D='read-only'
_C='not-accessible'
_B='ARISTA-PFC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PacketType,=mibBuilder.importSymbols('ARISTA-QUEUE-MIB','PacketType')
aristaMibs,=mibBuilder.importSymbols('ARISTA-SMI-MIB','aristaMibs')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
aristaPfcMIB=ModuleIdentity((1,3,6,1,4,1,30065,3,11))
if mibBuilder.loadTexts:aristaPfcMIB.setRevisions(('2017-01-17 00:00','2014-08-15 00:00','2013-02-28 00:00'))
class AristaPfcCOSIndex(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AristaPfc_ObjectIdentity=ObjectIdentity
aristaPfc=_AristaPfc_ObjectIdentity((1,3,6,1,4,1,30065,3,11,1))
_AristaPfcPriorityTable_Object=MibTable
aristaPfcPriorityTable=_AristaPfcPriorityTable_Object((1,3,6,1,4,1,30065,3,11,1,1))
if mibBuilder.loadTexts:aristaPfcPriorityTable.setStatus(_A)
_AristaPfcPriorityEntry_Object=MibTableRow
aristaPfcPriorityEntry=_AristaPfcPriorityEntry_Object((1,3,6,1,4,1,30065,3,11,1,1,1))
aristaPfcPriorityEntry.setIndexNames((0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:aristaPfcPriorityEntry.setStatus(_A)
_AristaPfcIfIndex_Type=InterfaceIndex
_AristaPfcIfIndex_Object=MibTableColumn
aristaPfcIfIndex=_AristaPfcIfIndex_Object((1,3,6,1,4,1,30065,3,11,1,1,1,1),_AristaPfcIfIndex_Type())
aristaPfcIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaPfcIfIndex.setStatus(_A)
_AristaPfcPriorityIndex_Type=AristaPfcCOSIndex
_AristaPfcPriorityIndex_Object=MibTableColumn
aristaPfcPriorityIndex=_AristaPfcPriorityIndex_Object((1,3,6,1,4,1,30065,3,11,1,1,1,2),_AristaPfcPriorityIndex_Type())
aristaPfcPriorityIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaPfcPriorityIndex.setStatus(_A)
_AristaPfcPriorityRequests_Type=Counter64
_AristaPfcPriorityRequests_Object=MibTableColumn
aristaPfcPriorityRequests=_AristaPfcPriorityRequests_Object((1,3,6,1,4,1,30065,3,11,1,1,1,3),_AristaPfcPriorityRequests_Type())
aristaPfcPriorityRequests.setMaxAccess(_D)
if mibBuilder.loadTexts:aristaPfcPriorityRequests.setStatus(_A)
if mibBuilder.loadTexts:aristaPfcPriorityRequests.setUnits('Requests')
_AristaPfcPriorityIndications_Type=Counter64
_AristaPfcPriorityIndications_Object=MibTableColumn
aristaPfcPriorityIndications=_AristaPfcPriorityIndications_Object((1,3,6,1,4,1,30065,3,11,1,1,1,4),_AristaPfcPriorityIndications_Type())
aristaPfcPriorityIndications.setMaxAccess(_D)
if mibBuilder.loadTexts:aristaPfcPriorityIndications.setStatus(_A)
if mibBuilder.loadTexts:aristaPfcPriorityIndications.setUnits('Indications')
_AristaPfcWatchdogTxQueueTable_Object=MibTable
aristaPfcWatchdogTxQueueTable=_AristaPfcWatchdogTxQueueTable_Object((1,3,6,1,4,1,30065,3,11,1,2))
if mibBuilder.loadTexts:aristaPfcWatchdogTxQueueTable.setStatus(_A)
_AristaPfcWatchdogTxQueueEntry_Object=MibTableRow
aristaPfcWatchdogTxQueueEntry=_AristaPfcWatchdogTxQueueEntry_Object((1,3,6,1,4,1,30065,3,11,1,2,1))
aristaPfcWatchdogTxQueueEntry.setIndexNames((0,_B,_H),(0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:aristaPfcWatchdogTxQueueEntry.setStatus(_A)
_AristaPfcWatchdogIfIndex_Type=InterfaceIndex
_AristaPfcWatchdogIfIndex_Object=MibTableColumn
aristaPfcWatchdogIfIndex=_AristaPfcWatchdogIfIndex_Object((1,3,6,1,4,1,30065,3,11,1,2,1,1),_AristaPfcWatchdogIfIndex_Type())
aristaPfcWatchdogIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaPfcWatchdogIfIndex.setStatus(_A)
_AristaPfcWatchdogTxQueueType_Type=PacketType
_AristaPfcWatchdogTxQueueType_Object=MibTableColumn
aristaPfcWatchdogTxQueueType=_AristaPfcWatchdogTxQueueType_Object((1,3,6,1,4,1,30065,3,11,1,2,1,2),_AristaPfcWatchdogTxQueueType_Type())
aristaPfcWatchdogTxQueueType.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaPfcWatchdogTxQueueType.setStatus(_A)
class _AristaPfcWatchdogTxQueueId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_AristaPfcWatchdogTxQueueId_Type.__name__=_E
_AristaPfcWatchdogTxQueueId_Object=MibTableColumn
aristaPfcWatchdogTxQueueId=_AristaPfcWatchdogTxQueueId_Object((1,3,6,1,4,1,30065,3,11,1,2,1,3),_AristaPfcWatchdogTxQueueId_Type())
aristaPfcWatchdogTxQueueId.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaPfcWatchdogTxQueueId.setStatus(_A)
_AristaPfcWatchdogTxQueueStuckCount_Type=Integer32
_AristaPfcWatchdogTxQueueStuckCount_Object=MibTableColumn
aristaPfcWatchdogTxQueueStuckCount=_AristaPfcWatchdogTxQueueStuckCount_Object((1,3,6,1,4,1,30065,3,11,1,2,1,4),_AristaPfcWatchdogTxQueueStuckCount_Type())
aristaPfcWatchdogTxQueueStuckCount.setMaxAccess(_D)
if mibBuilder.loadTexts:aristaPfcWatchdogTxQueueStuckCount.setStatus(_A)
_AristaPfcWatchdogTxQueueRecoveredCount_Type=Integer32
_AristaPfcWatchdogTxQueueRecoveredCount_Object=MibTableColumn
aristaPfcWatchdogTxQueueRecoveredCount=_AristaPfcWatchdogTxQueueRecoveredCount_Object((1,3,6,1,4,1,30065,3,11,1,2,1,5),_AristaPfcWatchdogTxQueueRecoveredCount_Type())
aristaPfcWatchdogTxQueueRecoveredCount.setMaxAccess(_D)
if mibBuilder.loadTexts:aristaPfcWatchdogTxQueueRecoveredCount.setStatus(_A)
_AristaPfcConformance_ObjectIdentity=ObjectIdentity
aristaPfcConformance=_AristaPfcConformance_ObjectIdentity((1,3,6,1,4,1,30065,3,11,2))
_AristaPfcCompliances_ObjectIdentity=ObjectIdentity
aristaPfcCompliances=_AristaPfcCompliances_ObjectIdentity((1,3,6,1,4,1,30065,3,11,2,1))
_AristaPfcGroups_ObjectIdentity=ObjectIdentity
aristaPfcGroups=_AristaPfcGroups_ObjectIdentity((1,3,6,1,4,1,30065,3,11,2,2))
aristaPfcGroup=ObjectGroup((1,3,6,1,4,1,30065,3,11,2,2,1))
aristaPfcGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:aristaPfcGroup.setStatus(_A)
aristaPfcCompliance=ModuleCompliance((1,3,6,1,4,1,30065,3,11,2,1,1))
aristaPfcCompliance.setObjects((_B,_O))
if mibBuilder.loadTexts:aristaPfcCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'AristaPfcCOSIndex':AristaPfcCOSIndex,'aristaPfcMIB':aristaPfcMIB,'aristaPfc':aristaPfc,'aristaPfcPriorityTable':aristaPfcPriorityTable,'aristaPfcPriorityEntry':aristaPfcPriorityEntry,_F:aristaPfcIfIndex,_G:aristaPfcPriorityIndex,_K:aristaPfcPriorityRequests,_L:aristaPfcPriorityIndications,'aristaPfcWatchdogTxQueueTable':aristaPfcWatchdogTxQueueTable,'aristaPfcWatchdogTxQueueEntry':aristaPfcWatchdogTxQueueEntry,_H:aristaPfcWatchdogIfIndex,_I:aristaPfcWatchdogTxQueueType,_J:aristaPfcWatchdogTxQueueId,_M:aristaPfcWatchdogTxQueueStuckCount,_N:aristaPfcWatchdogTxQueueRecoveredCount,'aristaPfcConformance':aristaPfcConformance,'aristaPfcCompliances':aristaPfcCompliances,'aristaPfcCompliance':aristaPfcCompliance,'aristaPfcGroups':aristaPfcGroups,_O:aristaPfcGroup})