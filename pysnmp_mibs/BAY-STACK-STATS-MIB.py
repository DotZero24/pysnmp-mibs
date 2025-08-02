_I='bayStackStatsCoSQueueQueue'
_H='bayStackStatsCoSQueueIfIndex'
_G='bayStackStatsUnitIndex'
_F='bayStackStatsIfIndex'
_E='not-accessible'
_D='Integer32'
_C='BAY-STACK-STATS-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
bayStackMibs,=mibBuilder.importSymbols('SYNOPTICS-ROOT-MIB','bayStackMibs')
bayStackStatsMib=ModuleIdentity((1,3,6,1,4,1,45,5,12))
if mibBuilder.loadTexts:bayStackStatsMib.setRevisions(('2015-05-11 00:00','2014-12-03 00:00','2014-10-15 00:00','2012-09-12 00:00','2007-03-09 00:00','2005-08-12 00:00'))
_BayStackStatsNotifications_ObjectIdentity=ObjectIdentity
bayStackStatsNotifications=_BayStackStatsNotifications_ObjectIdentity((1,3,6,1,4,1,45,5,12,0))
_BayStackStatsObjects_ObjectIdentity=ObjectIdentity
bayStackStatsObjects=_BayStackStatsObjects_ObjectIdentity((1,3,6,1,4,1,45,5,12,1))
_BayStackStatsIfTable_Object=MibTable
bayStackStatsIfTable=_BayStackStatsIfTable_Object((1,3,6,1,4,1,45,5,12,1,1))
if mibBuilder.loadTexts:bayStackStatsIfTable.setStatus(_A)
_BayStackStatsIfEntry_Object=MibTableRow
bayStackStatsIfEntry=_BayStackStatsIfEntry_Object((1,3,6,1,4,1,45,5,12,1,1,1))
bayStackStatsIfEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:bayStackStatsIfEntry.setStatus(_A)
_BayStackStatsIfIndex_Type=InterfaceIndex
_BayStackStatsIfIndex_Object=MibTableColumn
bayStackStatsIfIndex=_BayStackStatsIfIndex_Object((1,3,6,1,4,1,45,5,12,1,1,1,1),_BayStackStatsIfIndex_Type())
bayStackStatsIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:bayStackStatsIfIndex.setStatus(_A)
_BayStackStatsIfNoResourcesPktsDropped_Type=Counter64
_BayStackStatsIfNoResourcesPktsDropped_Object=MibTableColumn
bayStackStatsIfNoResourcesPktsDropped=_BayStackStatsIfNoResourcesPktsDropped_Object((1,3,6,1,4,1,45,5,12,1,1,1,2),_BayStackStatsIfNoResourcesPktsDropped_Type())
bayStackStatsIfNoResourcesPktsDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:bayStackStatsIfNoResourcesPktsDropped.setStatus(_A)
_BayStackStatsIfInPfcFrames_Type=Counter64
_BayStackStatsIfInPfcFrames_Object=MibTableColumn
bayStackStatsIfInPfcFrames=_BayStackStatsIfInPfcFrames_Object((1,3,6,1,4,1,45,5,12,1,1,1,3),_BayStackStatsIfInPfcFrames_Type())
bayStackStatsIfInPfcFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:bayStackStatsIfInPfcFrames.setStatus(_A)
_BayStackStatsIfOutPfcFrames_Type=Counter64
_BayStackStatsIfOutPfcFrames_Object=MibTableColumn
bayStackStatsIfOutPfcFrames=_BayStackStatsIfOutPfcFrames_Object((1,3,6,1,4,1,45,5,12,1,1,1,4),_BayStackStatsIfOutPfcFrames_Type())
bayStackStatsIfOutPfcFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:bayStackStatsIfOutPfcFrames.setStatus(_A)
_BayStackStatsUnitTable_Object=MibTable
bayStackStatsUnitTable=_BayStackStatsUnitTable_Object((1,3,6,1,4,1,45,5,12,1,2))
if mibBuilder.loadTexts:bayStackStatsUnitTable.setStatus(_A)
_BayStackStatsUnitEntry_Object=MibTableRow
bayStackStatsUnitEntry=_BayStackStatsUnitEntry_Object((1,3,6,1,4,1,45,5,12,1,2,1))
bayStackStatsUnitEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:bayStackStatsUnitEntry.setStatus(_A)
class _BayStackStatsUnitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_BayStackStatsUnitIndex_Type.__name__=_D
_BayStackStatsUnitIndex_Object=MibTableColumn
bayStackStatsUnitIndex=_BayStackStatsUnitIndex_Object((1,3,6,1,4,1,45,5,12,1,2,1,1),_BayStackStatsUnitIndex_Type())
bayStackStatsUnitIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:bayStackStatsUnitIndex.setStatus(_A)
_BayStackStatsUnitNoResourcesPktsDropped_Type=Counter64
_BayStackStatsUnitNoResourcesPktsDropped_Object=MibTableColumn
bayStackStatsUnitNoResourcesPktsDropped=_BayStackStatsUnitNoResourcesPktsDropped_Object((1,3,6,1,4,1,45,5,12,1,2,1,2),_BayStackStatsUnitNoResourcesPktsDropped_Type())
bayStackStatsUnitNoResourcesPktsDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:bayStackStatsUnitNoResourcesPktsDropped.setStatus(_A)
_BayStackStatsCoSQueueTable_Object=MibTable
bayStackStatsCoSQueueTable=_BayStackStatsCoSQueueTable_Object((1,3,6,1,4,1,45,5,12,1,3))
if mibBuilder.loadTexts:bayStackStatsCoSQueueTable.setStatus(_A)
_BayStackStatsCoSQueueEntry_Object=MibTableRow
bayStackStatsCoSQueueEntry=_BayStackStatsCoSQueueEntry_Object((1,3,6,1,4,1,45,5,12,1,3,1))
bayStackStatsCoSQueueEntry.setIndexNames((0,_C,_H),(0,_C,_I))
if mibBuilder.loadTexts:bayStackStatsCoSQueueEntry.setStatus(_A)
_BayStackStatsCoSQueueIfIndex_Type=InterfaceIndex
_BayStackStatsCoSQueueIfIndex_Object=MibTableColumn
bayStackStatsCoSQueueIfIndex=_BayStackStatsCoSQueueIfIndex_Object((1,3,6,1,4,1,45,5,12,1,3,1,1),_BayStackStatsCoSQueueIfIndex_Type())
bayStackStatsCoSQueueIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:bayStackStatsCoSQueueIfIndex.setStatus(_A)
class _BayStackStatsCoSQueueQueue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_BayStackStatsCoSQueueQueue_Type.__name__=_D
_BayStackStatsCoSQueueQueue_Object=MibTableColumn
bayStackStatsCoSQueueQueue=_BayStackStatsCoSQueueQueue_Object((1,3,6,1,4,1,45,5,12,1,3,1,2),_BayStackStatsCoSQueueQueue_Type())
bayStackStatsCoSQueueQueue.setMaxAccess(_E)
if mibBuilder.loadTexts:bayStackStatsCoSQueueQueue.setStatus(_A)
_BayStackStatsCoSQueueOutPackets_Type=Counter64
_BayStackStatsCoSQueueOutPackets_Object=MibTableColumn
bayStackStatsCoSQueueOutPackets=_BayStackStatsCoSQueueOutPackets_Object((1,3,6,1,4,1,45,5,12,1,3,1,3),_BayStackStatsCoSQueueOutPackets_Type())
bayStackStatsCoSQueueOutPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:bayStackStatsCoSQueueOutPackets.setStatus(_A)
_BayStackStatsCoSQueueOutBytes_Type=Counter64
_BayStackStatsCoSQueueOutBytes_Object=MibTableColumn
bayStackStatsCoSQueueOutBytes=_BayStackStatsCoSQueueOutBytes_Object((1,3,6,1,4,1,45,5,12,1,3,1,4),_BayStackStatsCoSQueueOutBytes_Type())
bayStackStatsCoSQueueOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:bayStackStatsCoSQueueOutBytes.setStatus(_A)
_BayStackStatsCoSQueueDropPackets_Type=Counter64
_BayStackStatsCoSQueueDropPackets_Object=MibTableColumn
bayStackStatsCoSQueueDropPackets=_BayStackStatsCoSQueueDropPackets_Object((1,3,6,1,4,1,45,5,12,1,3,1,5),_BayStackStatsCoSQueueDropPackets_Type())
bayStackStatsCoSQueueDropPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:bayStackStatsCoSQueueDropPackets.setStatus(_A)
_BayStackStatsCoSQueueDropBytes_Type=Counter64
_BayStackStatsCoSQueueDropBytes_Object=MibTableColumn
bayStackStatsCoSQueueDropBytes=_BayStackStatsCoSQueueDropBytes_Object((1,3,6,1,4,1,45,5,12,1,3,1,6),_BayStackStatsCoSQueueDropBytes_Type())
bayStackStatsCoSQueueDropBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:bayStackStatsCoSQueueDropBytes.setStatus(_A)
class _BayStackStatsCoSQueueClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('none',1),('clear',2)))
_BayStackStatsCoSQueueClear_Type.__name__=_D
_BayStackStatsCoSQueueClear_Object=MibTableColumn
bayStackStatsCoSQueueClear=_BayStackStatsCoSQueueClear_Object((1,3,6,1,4,1,45,5,12,1,3,1,7),_BayStackStatsCoSQueueClear_Type())
bayStackStatsCoSQueueClear.setMaxAccess('read-write')
if mibBuilder.loadTexts:bayStackStatsCoSQueueClear.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'bayStackStatsMib':bayStackStatsMib,'bayStackStatsNotifications':bayStackStatsNotifications,'bayStackStatsObjects':bayStackStatsObjects,'bayStackStatsIfTable':bayStackStatsIfTable,'bayStackStatsIfEntry':bayStackStatsIfEntry,_F:bayStackStatsIfIndex,'bayStackStatsIfNoResourcesPktsDropped':bayStackStatsIfNoResourcesPktsDropped,'bayStackStatsIfInPfcFrames':bayStackStatsIfInPfcFrames,'bayStackStatsIfOutPfcFrames':bayStackStatsIfOutPfcFrames,'bayStackStatsUnitTable':bayStackStatsUnitTable,'bayStackStatsUnitEntry':bayStackStatsUnitEntry,_G:bayStackStatsUnitIndex,'bayStackStatsUnitNoResourcesPktsDropped':bayStackStatsUnitNoResourcesPktsDropped,'bayStackStatsCoSQueueTable':bayStackStatsCoSQueueTable,'bayStackStatsCoSQueueEntry':bayStackStatsCoSQueueEntry,_H:bayStackStatsCoSQueueIfIndex,_I:bayStackStatsCoSQueueQueue,'bayStackStatsCoSQueueOutPackets':bayStackStatsCoSQueueOutPackets,'bayStackStatsCoSQueueOutBytes':bayStackStatsCoSQueueOutBytes,'bayStackStatsCoSQueueDropPackets':bayStackStatsCoSQueueDropPackets,'bayStackStatsCoSQueueDropBytes':bayStackStatsCoSQueueDropBytes,'bayStackStatsCoSQueueClear':bayStackStatsCoSQueueClear})