_S='aristaQueueCounterGroup'
_R='aristaEgressQueueDropPrec'
_Q='aristaEgressQueuePktsDroppedNoBuffer'
_P='aristaEgressQueuePktsDroppedQFull'
_O='aristaEgressQueueBytesDropped'
_N='aristaEgressQueuePktsDropped'
_M='aristaEgressQueueBytes'
_L='aristaEgressQueuePkts'
_K='aristaIngressQueueBytesDropped'
_J='aristaIngressQueuePktsDropped'
_I='aristaEgressPacketType'
_H='aristaEgressQueueIndex'
_G='aristaEgressIfIndex'
_F='aristaIngressQueueIndex'
_E='aristaIngressIfIndex'
_D='not-accessible'
_C='read-only'
_B='ARISTA-QUEUE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
aristaMibs,=mibBuilder.importSymbols('ARISTA-SMI-MIB','aristaMibs')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
aristaQueueMIB=ModuleIdentity((1,3,6,1,4,1,30065,3,6))
if mibBuilder.loadTexts:aristaQueueMIB.setRevisions(('2014-08-15 00:00','2012-08-23 13:00'))
class QueueIndex(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class PacketType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('unicast',0),('multicast',1),('mixedPacketType',2)))
class DropPrecedence(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('dropPrecedence0',0),('dropPrecedence1',1),('dropPrecedence2',2)))
_AristaQueue_ObjectIdentity=ObjectIdentity
aristaQueue=_AristaQueue_ObjectIdentity((1,3,6,1,4,1,30065,3,6,1))
_AristaIngressQueueTable_Object=MibTable
aristaIngressQueueTable=_AristaIngressQueueTable_Object((1,3,6,1,4,1,30065,3,6,1,1))
if mibBuilder.loadTexts:aristaIngressQueueTable.setStatus(_A)
_AristaIngressQueueEntry_Object=MibTableRow
aristaIngressQueueEntry=_AristaIngressQueueEntry_Object((1,3,6,1,4,1,30065,3,6,1,1,1))
aristaIngressQueueEntry.setIndexNames((0,_B,_E),(0,_B,_F))
if mibBuilder.loadTexts:aristaIngressQueueEntry.setStatus(_A)
_AristaIngressIfIndex_Type=InterfaceIndex
_AristaIngressIfIndex_Object=MibTableColumn
aristaIngressIfIndex=_AristaIngressIfIndex_Object((1,3,6,1,4,1,30065,3,6,1,1,1,1),_AristaIngressIfIndex_Type())
aristaIngressIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:aristaIngressIfIndex.setStatus(_A)
_AristaIngressQueueIndex_Type=QueueIndex
_AristaIngressQueueIndex_Object=MibTableColumn
aristaIngressQueueIndex=_AristaIngressQueueIndex_Object((1,3,6,1,4,1,30065,3,6,1,1,1,2),_AristaIngressQueueIndex_Type())
aristaIngressQueueIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:aristaIngressQueueIndex.setStatus(_A)
_AristaIngressQueuePktsDropped_Type=Counter64
_AristaIngressQueuePktsDropped_Object=MibTableColumn
aristaIngressQueuePktsDropped=_AristaIngressQueuePktsDropped_Object((1,3,6,1,4,1,30065,3,6,1,1,1,3),_AristaIngressQueuePktsDropped_Type())
aristaIngressQueuePktsDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaIngressQueuePktsDropped.setStatus(_A)
_AristaIngressQueueBytesDropped_Type=Counter64
_AristaIngressQueueBytesDropped_Object=MibTableColumn
aristaIngressQueueBytesDropped=_AristaIngressQueueBytesDropped_Object((1,3,6,1,4,1,30065,3,6,1,1,1,4),_AristaIngressQueueBytesDropped_Type())
aristaIngressQueueBytesDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaIngressQueueBytesDropped.setStatus(_A)
_AristaEgressQueueTable_Object=MibTable
aristaEgressQueueTable=_AristaEgressQueueTable_Object((1,3,6,1,4,1,30065,3,6,1,2))
if mibBuilder.loadTexts:aristaEgressQueueTable.setStatus(_A)
_AristaEgressQueueEntry_Object=MibTableRow
aristaEgressQueueEntry=_AristaEgressQueueEntry_Object((1,3,6,1,4,1,30065,3,6,1,2,1))
aristaEgressQueueEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:aristaEgressQueueEntry.setStatus(_A)
_AristaEgressIfIndex_Type=InterfaceIndex
_AristaEgressIfIndex_Object=MibTableColumn
aristaEgressIfIndex=_AristaEgressIfIndex_Object((1,3,6,1,4,1,30065,3,6,1,2,1,1),_AristaEgressIfIndex_Type())
aristaEgressIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:aristaEgressIfIndex.setStatus(_A)
_AristaEgressQueueIndex_Type=QueueIndex
_AristaEgressQueueIndex_Object=MibTableColumn
aristaEgressQueueIndex=_AristaEgressQueueIndex_Object((1,3,6,1,4,1,30065,3,6,1,2,1,2),_AristaEgressQueueIndex_Type())
aristaEgressQueueIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:aristaEgressQueueIndex.setStatus(_A)
_AristaEgressPacketType_Type=PacketType
_AristaEgressPacketType_Object=MibTableColumn
aristaEgressPacketType=_AristaEgressPacketType_Object((1,3,6,1,4,1,30065,3,6,1,2,1,3),_AristaEgressPacketType_Type())
aristaEgressPacketType.setMaxAccess(_D)
if mibBuilder.loadTexts:aristaEgressPacketType.setStatus(_A)
_AristaEgressQueuePkts_Type=Counter64
_AristaEgressQueuePkts_Object=MibTableColumn
aristaEgressQueuePkts=_AristaEgressQueuePkts_Object((1,3,6,1,4,1,30065,3,6,1,2,1,4),_AristaEgressQueuePkts_Type())
aristaEgressQueuePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaEgressQueuePkts.setStatus(_A)
_AristaEgressQueueBytes_Type=Counter64
_AristaEgressQueueBytes_Object=MibTableColumn
aristaEgressQueueBytes=_AristaEgressQueueBytes_Object((1,3,6,1,4,1,30065,3,6,1,2,1,5),_AristaEgressQueueBytes_Type())
aristaEgressQueueBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaEgressQueueBytes.setStatus(_A)
_AristaEgressQueuePktsDropped_Type=Counter64
_AristaEgressQueuePktsDropped_Object=MibTableColumn
aristaEgressQueuePktsDropped=_AristaEgressQueuePktsDropped_Object((1,3,6,1,4,1,30065,3,6,1,2,1,6),_AristaEgressQueuePktsDropped_Type())
aristaEgressQueuePktsDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaEgressQueuePktsDropped.setStatus(_A)
_AristaEgressQueueBytesDropped_Type=Counter64
_AristaEgressQueueBytesDropped_Object=MibTableColumn
aristaEgressQueueBytesDropped=_AristaEgressQueueBytesDropped_Object((1,3,6,1,4,1,30065,3,6,1,2,1,7),_AristaEgressQueueBytesDropped_Type())
aristaEgressQueueBytesDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaEgressQueueBytesDropped.setStatus(_A)
_AristaEgressQueuePktsDroppedQFull_Type=Counter64
_AristaEgressQueuePktsDroppedQFull_Object=MibTableColumn
aristaEgressQueuePktsDroppedQFull=_AristaEgressQueuePktsDroppedQFull_Object((1,3,6,1,4,1,30065,3,6,1,2,1,8),_AristaEgressQueuePktsDroppedQFull_Type())
aristaEgressQueuePktsDroppedQFull.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaEgressQueuePktsDroppedQFull.setStatus(_A)
_AristaEgressQueuePktsDroppedNoBuffer_Type=Counter64
_AristaEgressQueuePktsDroppedNoBuffer_Object=MibTableColumn
aristaEgressQueuePktsDroppedNoBuffer=_AristaEgressQueuePktsDroppedNoBuffer_Object((1,3,6,1,4,1,30065,3,6,1,2,1,9),_AristaEgressQueuePktsDroppedNoBuffer_Type())
aristaEgressQueuePktsDroppedNoBuffer.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaEgressQueuePktsDroppedNoBuffer.setStatus(_A)
_AristaEgressQueueDropPrec_Type=DropPrecedence
_AristaEgressQueueDropPrec_Object=MibTableColumn
aristaEgressQueueDropPrec=_AristaEgressQueueDropPrec_Object((1,3,6,1,4,1,30065,3,6,1,2,1,10),_AristaEgressQueueDropPrec_Type())
aristaEgressQueueDropPrec.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaEgressQueueDropPrec.setStatus(_A)
_AristaQueueCounterConformance_ObjectIdentity=ObjectIdentity
aristaQueueCounterConformance=_AristaQueueCounterConformance_ObjectIdentity((1,3,6,1,4,1,30065,3,6,2))
_AristaQueueCounterCompliances_ObjectIdentity=ObjectIdentity
aristaQueueCounterCompliances=_AristaQueueCounterCompliances_ObjectIdentity((1,3,6,1,4,1,30065,3,6,2,1))
_AristaQueueCounterGroups_ObjectIdentity=ObjectIdentity
aristaQueueCounterGroups=_AristaQueueCounterGroups_ObjectIdentity((1,3,6,1,4,1,30065,3,6,2,2))
aristaQueueCounterGroup=ObjectGroup((1,3,6,1,4,1,30065,3,6,2,2,1))
aristaQueueCounterGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:aristaQueueCounterGroup.setStatus(_A)
aristaQueueCounterCompliance=ModuleCompliance((1,3,6,1,4,1,30065,3,6,2,1,1))
aristaQueueCounterCompliance.setObjects((_B,_S))
if mibBuilder.loadTexts:aristaQueueCounterCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'QueueIndex':QueueIndex,'PacketType':PacketType,'DropPrecedence':DropPrecedence,'aristaQueueMIB':aristaQueueMIB,'aristaQueue':aristaQueue,'aristaIngressQueueTable':aristaIngressQueueTable,'aristaIngressQueueEntry':aristaIngressQueueEntry,_E:aristaIngressIfIndex,_F:aristaIngressQueueIndex,_J:aristaIngressQueuePktsDropped,_K:aristaIngressQueueBytesDropped,'aristaEgressQueueTable':aristaEgressQueueTable,'aristaEgressQueueEntry':aristaEgressQueueEntry,_G:aristaEgressIfIndex,_H:aristaEgressQueueIndex,_I:aristaEgressPacketType,_L:aristaEgressQueuePkts,_M:aristaEgressQueueBytes,_N:aristaEgressQueuePktsDropped,_O:aristaEgressQueueBytesDropped,_P:aristaEgressQueuePktsDroppedQFull,_Q:aristaEgressQueuePktsDroppedNoBuffer,_R:aristaEgressQueueDropPrec,'aristaQueueCounterConformance':aristaQueueCounterConformance,'aristaQueueCounterCompliances':aristaQueueCounterCompliances,'aristaQueueCounterCompliance':aristaQueueCounterCompliance,'aristaQueueCounterGroups':aristaQueueCounterGroups,_S:aristaQueueCounterGroup})