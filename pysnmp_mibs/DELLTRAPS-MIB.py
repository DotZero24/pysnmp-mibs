_E='NotificationType'
_D='connUnitEventType'
_C='connUnitEventId'
_B='connUnitEventDescr'
_A='FCMGMT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
connUnitEventDescr,connUnitEventId,connUnitEventType=mibBuilder.importSymbols(_A,_B,_C,_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier',_E,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_E,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Dell_ObjectIdentity=ObjectIdentity
dell=_Dell_ObjectIdentity((1,3,6,1,4,1,674))
dellEventInfoTrap=NotificationType((1,3,6,1,4,1,674,0,1))
dellEventInfoTrap.setObjects(*((_A,_C),(_A,_D),(_A,_B)))
if mibBuilder.loadTexts:dellEventInfoTrap.setStatus('')
dellEventWarningTrap=NotificationType((1,3,6,1,4,1,674,0,2))
dellEventWarningTrap.setObjects(*((_A,_C),(_A,_D),(_A,_B)))
if mibBuilder.loadTexts:dellEventWarningTrap.setStatus('')
dellEventErrorTrap=NotificationType((1,3,6,1,4,1,674,0,3))
dellEventErrorTrap.setObjects(*((_A,_C),(_A,_D),(_A,_B)))
if mibBuilder.loadTexts:dellEventErrorTrap.setStatus('')
dellEventCriticalTrap=NotificationType((1,3,6,1,4,1,674,0,4))
dellEventCriticalTrap.setObjects(*((_A,_C),(_A,_D),(_A,_B)))
if mibBuilder.loadTexts:dellEventCriticalTrap.setStatus('')
dellEventResolvedTrap=NotificationType((1,3,6,1,4,1,674,0,5))
dellEventResolvedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_B)))
if mibBuilder.loadTexts:dellEventResolvedTrap.setStatus('')
mibBuilder.exportSymbols('DELLTRAPS-MIB',**{'dell':dell,'dellEventInfoTrap':dellEventInfoTrap,'dellEventWarningTrap':dellEventWarningTrap,'dellEventErrorTrap':dellEventErrorTrap,'dellEventCriticalTrap':dellEventCriticalTrap,'dellEventResolvedTrap':dellEventResolvedTrap})