_M='tnDot3OamLoopbackEntry'
_L='tnDot3OamEntry'
_K='Integer32'
_J='dot3OamPeerMacAddress'
_I='DOT3-OAM-MIB'
_H='TN-DOT3-OAM-MIB'
_G='read-only'
_F='TruthValue'
_E='ifIndex'
_D='IF-MIB'
_C='Unsigned32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot3OamEntry,dot3OamLoopbackEntry,dot3OamPeerMacAddress=mibBuilder.importSymbols(_I,'dot3OamEntry','dot3OamLoopbackEntry',_J)
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_K,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp',_F)
tnSRMIBModules,tnSRNotifyPrefix,tnSRObjs=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnSRMIBModules','tnSRNotifyPrefix','tnSRObjs')
tnDOT3OAMMIBModule=ModuleIdentity((1,3,6,1,4,1,7483,5,1,3,42))
if mibBuilder.loadTexts:tnDOT3OAMMIBModule.setRevisions(('2008-07-01 00:00','2008-01-01 00:00','2006-08-01 00:00'))
_TnDot3OamObjs_ObjectIdentity=ObjectIdentity
tnDot3OamObjs=_TnDot3OamObjs_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,42))
_TnDot3OamEntryObjs_ObjectIdentity=ObjectIdentity
tnDot3OamEntryObjs=_TnDot3OamEntryObjs_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,42,1))
_TnDot3OamTable_Object=MibTable
tnDot3OamTable=_TnDot3OamTable_Object((1,3,6,1,4,1,7483,6,1,2,42,1,1))
if mibBuilder.loadTexts:tnDot3OamTable.setStatus(_A)
_TnDot3OamEntry_Object=MibTableRow
tnDot3OamEntry=_TnDot3OamEntry_Object((1,3,6,1,4,1,7483,6,1,2,42,1,1,1))
if mibBuilder.loadTexts:tnDot3OamEntry.setStatus(_A)
_TnDot3OamLastChanged_Type=TimeStamp
_TnDot3OamLastChanged_Object=MibTableColumn
tnDot3OamLastChanged=_TnDot3OamLastChanged_Object((1,3,6,1,4,1,7483,6,1,2,42,1,1,1,1),_TnDot3OamLastChanged_Type())
tnDot3OamLastChanged.setMaxAccess(_G)
if mibBuilder.loadTexts:tnDot3OamLastChanged.setStatus(_A)
class _TnDot3OamInterval_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_TnDot3OamInterval_Type.__name__=_C
_TnDot3OamInterval_Object=MibTableColumn
tnDot3OamInterval=_TnDot3OamInterval_Object((1,3,6,1,4,1,7483,6,1,2,42,1,1,1,2),_TnDot3OamInterval_Type())
tnDot3OamInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot3OamInterval.setStatus(_A)
if mibBuilder.loadTexts:tnDot3OamInterval.setUnits('100s of milliseconds')
class _TnDot3OamMultiplier_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,5))
_TnDot3OamMultiplier_Type.__name__=_C
_TnDot3OamMultiplier_Object=MibTableColumn
tnDot3OamMultiplier=_TnDot3OamMultiplier_Object((1,3,6,1,4,1,7483,6,1,2,42,1,1,1,3),_TnDot3OamMultiplier_Type())
tnDot3OamMultiplier.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot3OamMultiplier.setStatus(_A)
class _TnDot3OamTunneling_Type(TruthValue):defaultValue=2
_TnDot3OamTunneling_Type.__name__=_F
_TnDot3OamTunneling_Object=MibTableColumn
tnDot3OamTunneling=_TnDot3OamTunneling_Object((1,3,6,1,4,1,7483,6,1,2,42,1,1,1,4),_TnDot3OamTunneling_Type())
tnDot3OamTunneling.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot3OamTunneling.setStatus(_A)
class _TnDot3OamLooped_Type(TruthValue):defaultValue=2
_TnDot3OamLooped_Type.__name__=_F
_TnDot3OamLooped_Object=MibTableColumn
tnDot3OamLooped=_TnDot3OamLooped_Object((1,3,6,1,4,1,7483,6,1,2,42,1,1,1,5),_TnDot3OamLooped_Type())
tnDot3OamLooped.setMaxAccess(_G)
if mibBuilder.loadTexts:tnDot3OamLooped.setStatus(_A)
class _TnDot3OamHoldTime_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,50))
_TnDot3OamHoldTime_Type.__name__=_C
_TnDot3OamHoldTime_Object=MibTableColumn
tnDot3OamHoldTime=_TnDot3OamHoldTime_Object((1,3,6,1,4,1,7483,6,1,2,42,1,1,1,6),_TnDot3OamHoldTime_Type())
tnDot3OamHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot3OamHoldTime.setStatus(_A)
if mibBuilder.loadTexts:tnDot3OamHoldTime.setUnits('seconds')
_TnDot3OamLoopbackObjs_ObjectIdentity=ObjectIdentity
tnDot3OamLoopbackObjs=_TnDot3OamLoopbackObjs_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,42,2))
_TnDot3OamLoopbackTable_Object=MibTable
tnDot3OamLoopbackTable=_TnDot3OamLoopbackTable_Object((1,3,6,1,4,1,7483,6,1,2,42,2,1))
if mibBuilder.loadTexts:tnDot3OamLoopbackTable.setStatus(_A)
_TnDot3OamLoopbackEntry_Object=MibTableRow
tnDot3OamLoopbackEntry=_TnDot3OamLoopbackEntry_Object((1,3,6,1,4,1,7483,6,1,2,42,2,1,1))
if mibBuilder.loadTexts:tnDot3OamLoopbackEntry.setStatus(_A)
_TnDot3OamLoopbackLastChanged_Type=TimeStamp
_TnDot3OamLoopbackLastChanged_Object=MibTableColumn
tnDot3OamLoopbackLastChanged=_TnDot3OamLoopbackLastChanged_Object((1,3,6,1,4,1,7483,6,1,2,42,2,1,1,1),_TnDot3OamLoopbackLastChanged_Type())
tnDot3OamLoopbackLastChanged.setMaxAccess(_G)
if mibBuilder.loadTexts:tnDot3OamLoopbackLastChanged.setStatus(_A)
class _TnDot3OamLoopbackLocalStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noLoopback',1),('localLoopback',2)))
_TnDot3OamLoopbackLocalStatus_Type.__name__=_K
_TnDot3OamLoopbackLocalStatus_Object=MibTableColumn
tnDot3OamLoopbackLocalStatus=_TnDot3OamLoopbackLocalStatus_Object((1,3,6,1,4,1,7483,6,1,2,42,2,1,1,2),_TnDot3OamLoopbackLocalStatus_Type())
tnDot3OamLoopbackLocalStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnDot3OamLoopbackLocalStatus.setStatus(_A)
_TnDot3OamNotifyPrefix_ObjectIdentity=ObjectIdentity
tnDot3OamNotifyPrefix=_TnDot3OamNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,7483,6,1,3,42))
_TnDot3OamNotificationsPrefix_ObjectIdentity=ObjectIdentity
tnDot3OamNotificationsPrefix=_TnDot3OamNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,7483,6,1,3,42,42))
_TnDot3OamNotifications_ObjectIdentity=ObjectIdentity
tnDot3OamNotifications=_TnDot3OamNotifications_ObjectIdentity((1,3,6,1,4,1,7483,6,1,3,42,42,0))
dot3OamEntry.registerAugmentions((_H,_L))
tnDot3OamEntry.setIndexNames(*dot3OamEntry.getIndexNames())
dot3OamLoopbackEntry.registerAugmentions((_H,_M))
tnDot3OamLoopbackEntry.setIndexNames(*dot3OamLoopbackEntry.getIndexNames())
tnDot3OamPeerChanged=NotificationType((1,3,6,1,4,1,7483,6,1,3,42,42,0,1))
tnDot3OamPeerChanged.setObjects((_I,_J))
if mibBuilder.loadTexts:tnDot3OamPeerChanged.setStatus(_A)
tnDot3OamLoopDetected=NotificationType((1,3,6,1,4,1,7483,6,1,3,42,42,0,2))
tnDot3OamLoopDetected.setObjects((_D,_E))
if mibBuilder.loadTexts:tnDot3OamLoopDetected.setStatus(_A)
tnDot3OamLoopCleared=NotificationType((1,3,6,1,4,1,7483,6,1,3,42,42,0,3))
tnDot3OamLoopCleared.setObjects((_D,_E))
if mibBuilder.loadTexts:tnDot3OamLoopCleared.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'tnDOT3OAMMIBModule':tnDOT3OAMMIBModule,'tnDot3OamObjs':tnDot3OamObjs,'tnDot3OamEntryObjs':tnDot3OamEntryObjs,'tnDot3OamTable':tnDot3OamTable,_L:tnDot3OamEntry,'tnDot3OamLastChanged':tnDot3OamLastChanged,'tnDot3OamInterval':tnDot3OamInterval,'tnDot3OamMultiplier':tnDot3OamMultiplier,'tnDot3OamTunneling':tnDot3OamTunneling,'tnDot3OamLooped':tnDot3OamLooped,'tnDot3OamHoldTime':tnDot3OamHoldTime,'tnDot3OamLoopbackObjs':tnDot3OamLoopbackObjs,'tnDot3OamLoopbackTable':tnDot3OamLoopbackTable,_M:tnDot3OamLoopbackEntry,'tnDot3OamLoopbackLastChanged':tnDot3OamLoopbackLastChanged,'tnDot3OamLoopbackLocalStatus':tnDot3OamLoopbackLocalStatus,'tnDot3OamNotifyPrefix':tnDot3OamNotifyPrefix,'tnDot3OamNotificationsPrefix':tnDot3OamNotificationsPrefix,'tnDot3OamNotifications':tnDot3OamNotifications,'tnDot3OamPeerChanged':tnDot3OamPeerChanged,'tnDot3OamLoopDetected':tnDot3OamLoopDetected,'tnDot3OamLoopCleared':tnDot3OamLoopCleared})