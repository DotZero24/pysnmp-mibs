_H='mellanoxEntStateModuleStateDescr'
_G='mellanoxEntStateModulePreviousState'
_F='mellanoxEntStateModuleCurrentState'
_E='read-only'
_D='entPhysicalIndex'
_C='ENTITY-MIB'
_B='MELLANOX-ENTITY-STATE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_C,_D)
mellanoxEntState,=mibBuilder.importSymbols('MELLANOX-SMI-MIB','mellanoxEntState')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
mellanoxEntStateMib=ModuleIdentity((1,3,6,1,4,1,33049,7,1))
if mibBuilder.loadTexts:mellanoxEntStateMib.setRevisions(('2017-07-25 00:00',))
class ModuleStateType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('ok',1),('disabled',2),('reset',3),('missing',4),('criticalFault',5),('nonCriticalFault',6),('unknown',7)))
_MellanoxEntStateMibNotifications_ObjectIdentity=ObjectIdentity
mellanoxEntStateMibNotifications=_MellanoxEntStateMibNotifications_ObjectIdentity((1,3,6,1,4,1,33049,7,1,0))
_MellanoxEntStateMibObjects_ObjectIdentity=ObjectIdentity
mellanoxEntStateMibObjects=_MellanoxEntStateMibObjects_ObjectIdentity((1,3,6,1,4,1,33049,7,1,1))
_MellanoxEntStateTable_Object=MibTable
mellanoxEntStateTable=_MellanoxEntStateTable_Object((1,3,6,1,4,1,33049,7,1,1,1))
if mibBuilder.loadTexts:mellanoxEntStateTable.setStatus(_A)
_MellanoxEntStateEntry_Object=MibTableRow
mellanoxEntStateEntry=_MellanoxEntStateEntry_Object((1,3,6,1,4,1,33049,7,1,1,1,1))
mellanoxEntStateEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:mellanoxEntStateEntry.setStatus(_A)
_MellanoxEntStateModuleCurrentState_Type=ModuleStateType
_MellanoxEntStateModuleCurrentState_Object=MibTableColumn
mellanoxEntStateModuleCurrentState=_MellanoxEntStateModuleCurrentState_Object((1,3,6,1,4,1,33049,7,1,1,1,1,1),_MellanoxEntStateModuleCurrentState_Type())
mellanoxEntStateModuleCurrentState.setMaxAccess(_E)
if mibBuilder.loadTexts:mellanoxEntStateModuleCurrentState.setStatus(_A)
_MellanoxEntStateModulePreviousState_Type=ModuleStateType
_MellanoxEntStateModulePreviousState_Object=MibTableColumn
mellanoxEntStateModulePreviousState=_MellanoxEntStateModulePreviousState_Object((1,3,6,1,4,1,33049,7,1,1,1,1,2),_MellanoxEntStateModulePreviousState_Type())
mellanoxEntStateModulePreviousState.setMaxAccess(_E)
if mibBuilder.loadTexts:mellanoxEntStateModulePreviousState.setStatus(_A)
_MellanoxEntStateModuleStateDescr_Type=SnmpAdminString
_MellanoxEntStateModuleStateDescr_Object=MibTableColumn
mellanoxEntStateModuleStateDescr=_MellanoxEntStateModuleStateDescr_Object((1,3,6,1,4,1,33049,7,1,1,1,1,3),_MellanoxEntStateModuleStateDescr_Type())
mellanoxEntStateModuleStateDescr.setMaxAccess(_E)
if mibBuilder.loadTexts:mellanoxEntStateModuleStateDescr.setStatus(_A)
mellanoxEntStateChangeAlarm=NotificationType((1,3,6,1,4,1,33049,7,1,0,1))
mellanoxEntStateChangeAlarm.setObjects(*((_C,_D),(_B,'entPhysicalDescr'),(_B,'entPhysicalName'),(_B,_F),(_B,_G),(_B,_H),(_B,'entStateAlarm')))
if mibBuilder.loadTexts:mellanoxEntStateChangeAlarm.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ModuleStateType':ModuleStateType,'mellanoxEntStateMib':mellanoxEntStateMib,'mellanoxEntStateMibNotifications':mellanoxEntStateMibNotifications,'mellanoxEntStateChangeAlarm':mellanoxEntStateChangeAlarm,'mellanoxEntStateMibObjects':mellanoxEntStateMibObjects,'mellanoxEntStateTable':mellanoxEntStateTable,'mellanoxEntStateEntry':mellanoxEntStateEntry,_F:mellanoxEntStateModuleCurrentState,_G:mellanoxEntStateModulePreviousState,_H:mellanoxEntStateModuleStateDescr})