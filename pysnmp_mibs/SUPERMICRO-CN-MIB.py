_N='fsCnCnmQDelta'
_M='fsCnCnmQOffset'
_L='fsCnXPortPriErrorEntry'
_K='fsCnXPortPriEntry'
_J='fsCnXGlobalEntry'
_I='accessible-for-notify'
_H='ieee8021CnCpIdentifier'
_G='IEEE8021-CN-MIB'
_F='TruthValue'
_E='Integer32'
_D='read-write'
_C='SUPERMICRO-CN-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Ieee8021CnDefenseMode,ieee8021CnCpIdentifier,ieee8021CnGlobalEntry,ieee8021CnPortPriEntry=mibBuilder.importSymbols(_G,'Ieee8021CnDefenseMode',_H,'ieee8021CnGlobalEntry','ieee8021CnPortPriEntry')
IEEE8021PriorityValue,=mibBuilder.importSymbols('IEEE8021-TC-MIB','IEEE8021PriorityValue')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp',_F)
fscn=ModuleIdentity((1,3,6,1,4,1,10876,101,2,47))
if mibBuilder.loadTexts:fscn.setRevisions(('2012-09-05 00:00',))
_FsCnMaster_ObjectIdentity=ObjectIdentity
fsCnMaster=_FsCnMaster_ObjectIdentity((1,3,6,1,4,1,10876,101,2,47,1))
class _FsCnSystemControl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('shutdown',2)))
_FsCnSystemControl_Type.__name__=_E
_FsCnSystemControl_Object=MibScalar
fsCnSystemControl=_FsCnSystemControl_Object((1,3,6,1,4,1,10876,101,2,47,1,1),_FsCnSystemControl_Type())
fsCnSystemControl.setMaxAccess(_D)
if mibBuilder.loadTexts:fsCnSystemControl.setStatus(_A)
class _FsCnGlobalEnableTrap_Type(Integer32):defaultValue=3
_FsCnGlobalEnableTrap_Type.__name__=_E
_FsCnGlobalEnableTrap_Object=MibScalar
fsCnGlobalEnableTrap=_FsCnGlobalEnableTrap_Object((1,3,6,1,4,1,10876,101,2,47,1,2),_FsCnGlobalEnableTrap_Type())
fsCnGlobalEnableTrap.setMaxAccess(_D)
if mibBuilder.loadTexts:fsCnGlobalEnableTrap.setStatus(_A)
_FsCnComponent_ObjectIdentity=ObjectIdentity
fsCnComponent=_FsCnComponent_ObjectIdentity((1,3,6,1,4,1,10876,101,2,47,2))
_FsCnXGlobalTable_Object=MibTable
fsCnXGlobalTable=_FsCnXGlobalTable_Object((1,3,6,1,4,1,10876,101,2,47,2,1))
if mibBuilder.loadTexts:fsCnXGlobalTable.setStatus(_A)
_FsCnXGlobalEntry_Object=MibTableRow
fsCnXGlobalEntry=_FsCnXGlobalEntry_Object((1,3,6,1,4,1,10876,101,2,47,2,1,1))
if mibBuilder.loadTexts:fsCnXGlobalEntry.setStatus(_A)
class _FsCnXGlobalTraceLevel_Type(Integer32):defaultValue=32
_FsCnXGlobalTraceLevel_Type.__name__=_E
_FsCnXGlobalTraceLevel_Object=MibTableColumn
fsCnXGlobalTraceLevel=_FsCnXGlobalTraceLevel_Object((1,3,6,1,4,1,10876,101,2,47,2,1,1,1),_FsCnXGlobalTraceLevel_Type())
fsCnXGlobalTraceLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:fsCnXGlobalTraceLevel.setStatus(_A)
class _FsCnXGlobalClearCounters_Type(TruthValue):defaultValue=2
_FsCnXGlobalClearCounters_Type.__name__=_F
_FsCnXGlobalClearCounters_Object=MibTableColumn
fsCnXGlobalClearCounters=_FsCnXGlobalClearCounters_Object((1,3,6,1,4,1,10876,101,2,47,2,1,1,2),_FsCnXGlobalClearCounters_Type())
fsCnXGlobalClearCounters.setMaxAccess(_D)
if mibBuilder.loadTexts:fsCnXGlobalClearCounters.setStatus(_A)
_FsCnXGlobalTLVErrors_Type=Counter32
_FsCnXGlobalTLVErrors_Object=MibTableColumn
fsCnXGlobalTLVErrors=_FsCnXGlobalTLVErrors_Object((1,3,6,1,4,1,10876,101,2,47,2,1,1,3),_FsCnXGlobalTLVErrors_Type())
fsCnXGlobalTLVErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCnXGlobalTLVErrors.setStatus(_A)
_FsCnPortPriority_ObjectIdentity=ObjectIdentity
fsCnPortPriority=_FsCnPortPriority_ObjectIdentity((1,3,6,1,4,1,10876,101,2,47,3))
_FsCnXPortPriTable_Object=MibTable
fsCnXPortPriTable=_FsCnXPortPriTable_Object((1,3,6,1,4,1,10876,101,2,47,3,1))
if mibBuilder.loadTexts:fsCnXPortPriTable.setStatus(_A)
_FsCnXPortPriEntry_Object=MibTableRow
fsCnXPortPriEntry=_FsCnXPortPriEntry_Object((1,3,6,1,4,1,10876,101,2,47,3,1,1))
if mibBuilder.loadTexts:fsCnXPortPriEntry.setStatus(_A)
class _FsCnXPortPriClearCpCounters_Type(TruthValue):defaultValue=2
_FsCnXPortPriClearCpCounters_Type.__name__=_F
_FsCnXPortPriClearCpCounters_Object=MibTableColumn
fsCnXPortPriClearCpCounters=_FsCnXPortPriClearCpCounters_Object((1,3,6,1,4,1,10876,101,2,47,3,1,1,1),_FsCnXPortPriClearCpCounters_Type())
fsCnXPortPriClearCpCounters.setMaxAccess(_D)
if mibBuilder.loadTexts:fsCnXPortPriClearCpCounters.setStatus(_A)
class _FsCnXPortPriErrorEntry_Type(TruthValue):defaultValue=2
_FsCnXPortPriErrorEntry_Type.__name__=_F
_FsCnXPortPriErrorEntry_Object=MibTableColumn
fsCnXPortPriErrorEntry=_FsCnXPortPriErrorEntry_Object((1,3,6,1,4,1,10876,101,2,47,3,1,1,2),_FsCnXPortPriErrorEntry_Type())
fsCnXPortPriErrorEntry.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCnXPortPriErrorEntry.setStatus(_A)
_FsCnXPortPriOperDefMode_Type=Ieee8021CnDefenseMode
_FsCnXPortPriOperDefMode_Object=MibTableColumn
fsCnXPortPriOperDefMode=_FsCnXPortPriOperDefMode_Object((1,3,6,1,4,1,10876,101,2,47,3,1,1,3),_FsCnXPortPriOperDefMode_Type())
fsCnXPortPriOperDefMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCnXPortPriOperDefMode.setStatus(_A)
_FsCnXPortPriOperAltPri_Type=IEEE8021PriorityValue
_FsCnXPortPriOperAltPri_Object=MibTableColumn
fsCnXPortPriOperAltPri=_FsCnXPortPriOperAltPri_Object((1,3,6,1,4,1,10876,101,2,47,3,1,1,4),_FsCnXPortPriOperAltPri_Type())
fsCnXPortPriOperAltPri.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCnXPortPriOperAltPri.setStatus(_A)
_FsCnXPortPriLastRcvdEvent_Type=DisplayString
_FsCnXPortPriLastRcvdEvent_Object=MibTableColumn
fsCnXPortPriLastRcvdEvent=_FsCnXPortPriLastRcvdEvent_Object((1,3,6,1,4,1,10876,101,2,47,3,1,1,5),_FsCnXPortPriLastRcvdEvent_Type())
fsCnXPortPriLastRcvdEvent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCnXPortPriLastRcvdEvent.setStatus(_A)
_FsCnXPortPriLastRcvdEventTime_Type=TimeStamp
_FsCnXPortPriLastRcvdEventTime_Object=MibTableColumn
fsCnXPortPriLastRcvdEventTime=_FsCnXPortPriLastRcvdEventTime_Object((1,3,6,1,4,1,10876,101,2,47,3,1,1,6),_FsCnXPortPriLastRcvdEventTime_Type())
fsCnXPortPriLastRcvdEventTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCnXPortPriLastRcvdEventTime.setStatus(_A)
_FsCnXPortPriLastSentEvent_Type=DisplayString
_FsCnXPortPriLastSentEvent_Object=MibTableColumn
fsCnXPortPriLastSentEvent=_FsCnXPortPriLastSentEvent_Object((1,3,6,1,4,1,10876,101,2,47,3,1,1,7),_FsCnXPortPriLastSentEvent_Type())
fsCnXPortPriLastSentEvent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCnXPortPriLastSentEvent.setStatus(_A)
_FsCnXPortPriLastSentEventTime_Type=TimeStamp
_FsCnXPortPriLastSentEventTime_Object=MibTableColumn
fsCnXPortPriLastSentEventTime=_FsCnXPortPriLastSentEventTime_Object((1,3,6,1,4,1,10876,101,2,47,3,1,1,8),_FsCnXPortPriLastSentEventTime_Type())
fsCnXPortPriLastSentEventTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCnXPortPriLastSentEventTime.setStatus(_A)
_FsCnNotifications_ObjectIdentity=ObjectIdentity
fsCnNotifications=_FsCnNotifications_ObjectIdentity((1,3,6,1,4,1,10876,101,2,47,4))
_FsCnTraps_ObjectIdentity=ObjectIdentity
fsCnTraps=_FsCnTraps_ObjectIdentity((1,3,6,1,4,1,10876,101,2,47,4,0))
_FsCnCnmQOffset_Type=Integer32
_FsCnCnmQOffset_Object=MibScalar
fsCnCnmQOffset=_FsCnCnmQOffset_Object((1,3,6,1,4,1,10876,101,2,47,4,1),_FsCnCnmQOffset_Type())
fsCnCnmQOffset.setMaxAccess(_I)
if mibBuilder.loadTexts:fsCnCnmQOffset.setStatus(_A)
_FsCnCnmQDelta_Type=Integer32
_FsCnCnmQDelta_Object=MibScalar
fsCnCnmQDelta=_FsCnCnmQDelta_Object((1,3,6,1,4,1,10876,101,2,47,4,2),_FsCnCnmQDelta_Type())
fsCnCnmQDelta.setMaxAccess(_I)
if mibBuilder.loadTexts:fsCnCnmQDelta.setStatus(_A)
ieee8021CnGlobalEntry.registerAugmentions((_C,_J))
fsCnXGlobalEntry.setIndexNames(*ieee8021CnGlobalEntry.getIndexNames())
ieee8021CnPortPriEntry.registerAugmentions((_C,_K))
fsCnXPortPriEntry.setIndexNames(*ieee8021CnPortPriEntry.getIndexNames())
fsCnEpEntryTrap=NotificationType((1,3,6,1,4,1,10876,101,2,47,4,0,1))
fsCnEpEntryTrap.setObjects((_C,_L))
if mibBuilder.loadTexts:fsCnEpEntryTrap.setStatus(_A)
fsCnCNMTrap=NotificationType((1,3,6,1,4,1,10876,101,2,47,4,0,2))
fsCnCNMTrap.setObjects(*((_G,_H),(_C,_M),(_C,_N)))
if mibBuilder.loadTexts:fsCnCNMTrap.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'fscn':fscn,'fsCnMaster':fsCnMaster,'fsCnSystemControl':fsCnSystemControl,'fsCnGlobalEnableTrap':fsCnGlobalEnableTrap,'fsCnComponent':fsCnComponent,'fsCnXGlobalTable':fsCnXGlobalTable,_J:fsCnXGlobalEntry,'fsCnXGlobalTraceLevel':fsCnXGlobalTraceLevel,'fsCnXGlobalClearCounters':fsCnXGlobalClearCounters,'fsCnXGlobalTLVErrors':fsCnXGlobalTLVErrors,'fsCnPortPriority':fsCnPortPriority,'fsCnXPortPriTable':fsCnXPortPriTable,_K:fsCnXPortPriEntry,'fsCnXPortPriClearCpCounters':fsCnXPortPriClearCpCounters,_L:fsCnXPortPriErrorEntry,'fsCnXPortPriOperDefMode':fsCnXPortPriOperDefMode,'fsCnXPortPriOperAltPri':fsCnXPortPriOperAltPri,'fsCnXPortPriLastRcvdEvent':fsCnXPortPriLastRcvdEvent,'fsCnXPortPriLastRcvdEventTime':fsCnXPortPriLastRcvdEventTime,'fsCnXPortPriLastSentEvent':fsCnXPortPriLastSentEvent,'fsCnXPortPriLastSentEventTime':fsCnXPortPriLastSentEventTime,'fsCnNotifications':fsCnNotifications,'fsCnTraps':fsCnTraps,'fsCnEpEntryTrap':fsCnEpEntryTrap,'fsCnCNMTrap':fsCnCNMTrap,_M:fsCnCnmQOffset,_N:fsCnCnmQDelta})