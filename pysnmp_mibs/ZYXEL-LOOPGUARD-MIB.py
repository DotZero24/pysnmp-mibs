_F='read-write'
_E='ifIndex'
_D='IF-MIB'
_C='dot1dBasePort'
_B='BRIDGE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_B,_C)
ifIndex,=mibBuilder.importSymbols(_D,_E)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelLoopGuard=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,45))
_ZyxelLoopGuardSetup_ObjectIdentity=ObjectIdentity
zyxelLoopGuardSetup=_ZyxelLoopGuardSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,45,1))
_ZyLoopGuardState_Type=EnabledStatus
_ZyLoopGuardState_Object=MibScalar
zyLoopGuardState=_ZyLoopGuardState_Object((1,3,6,1,4,1,890,1,15,3,45,1,1),_ZyLoopGuardState_Type())
zyLoopGuardState.setMaxAccess(_F)
if mibBuilder.loadTexts:zyLoopGuardState.setStatus(_A)
_ZyxelLoopGuardPortTable_Object=MibTable
zyxelLoopGuardPortTable=_ZyxelLoopGuardPortTable_Object((1,3,6,1,4,1,890,1,15,3,45,1,2))
if mibBuilder.loadTexts:zyxelLoopGuardPortTable.setStatus(_A)
_ZyxelLoopGuardPortEntry_Object=MibTableRow
zyxelLoopGuardPortEntry=_ZyxelLoopGuardPortEntry_Object((1,3,6,1,4,1,890,1,15,3,45,1,2,1))
zyxelLoopGuardPortEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:zyxelLoopGuardPortEntry.setStatus(_A)
_ZyLoopGuardPortState_Type=EnabledStatus
_ZyLoopGuardPortState_Object=MibTableColumn
zyLoopGuardPortState=_ZyLoopGuardPortState_Object((1,3,6,1,4,1,890,1,15,3,45,1,2,1,1),_ZyLoopGuardPortState_Type())
zyLoopGuardPortState.setMaxAccess(_F)
if mibBuilder.loadTexts:zyLoopGuardPortState.setStatus(_A)
_ZyxelLoopGuardNotifications_ObjectIdentity=ObjectIdentity
zyxelLoopGuardNotifications=_ZyxelLoopGuardNotifications_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,45,2))
zyLoopGuardLoopDetect=NotificationType((1,3,6,1,4,1,890,1,15,3,45,2,1))
zyLoopGuardLoopDetect.setObjects((_D,_E))
if mibBuilder.loadTexts:zyLoopGuardLoopDetect.setStatus(_A)
mibBuilder.exportSymbols('ZYXEL-LOOPGUARD-MIB',**{'zyxelLoopGuard':zyxelLoopGuard,'zyxelLoopGuardSetup':zyxelLoopGuardSetup,'zyLoopGuardState':zyLoopGuardState,'zyxelLoopGuardPortTable':zyxelLoopGuardPortTable,'zyxelLoopGuardPortEntry':zyxelLoopGuardPortEntry,'zyLoopGuardPortState':zyLoopGuardPortState,'zyxelLoopGuardNotifications':zyxelLoopGuardNotifications,'zyLoopGuardLoopDetect':zyLoopGuardLoopDetect})