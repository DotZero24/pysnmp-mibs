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
_SeagateSystems_ObjectIdentity=ObjectIdentity
seagateSystems=_SeagateSystems_ObjectIdentity((1,3,6,1,4,1,347))
seagateEventInfoTrap=NotificationType((1,3,6,1,4,1,347,0,1))
seagateEventInfoTrap.setObjects(*((_A,_C),(_A,_D),(_A,_B)))
if mibBuilder.loadTexts:seagateEventInfoTrap.setStatus('')
seagateEventWarningTrap=NotificationType((1,3,6,1,4,1,347,0,2))
seagateEventWarningTrap.setObjects(*((_A,_C),(_A,_D),(_A,_B)))
if mibBuilder.loadTexts:seagateEventWarningTrap.setStatus('')
seagateEventErrorTrap=NotificationType((1,3,6,1,4,1,347,0,3))
seagateEventErrorTrap.setObjects(*((_A,_C),(_A,_D),(_A,_B)))
if mibBuilder.loadTexts:seagateEventErrorTrap.setStatus('')
seagateEventCriticalTrap=NotificationType((1,3,6,1,4,1,347,0,4))
seagateEventCriticalTrap.setObjects(*((_A,_C),(_A,_D),(_A,_B)))
if mibBuilder.loadTexts:seagateEventCriticalTrap.setStatus('')
seagateEventResolvedTrap=NotificationType((1,3,6,1,4,1,347,0,5))
seagateEventResolvedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_B)))
if mibBuilder.loadTexts:seagateEventResolvedTrap.setStatus('')
mibBuilder.exportSymbols('SEAGATESYSTEMTRAP-MIB',**{'seagateSystems':seagateSystems,'seagateEventInfoTrap':seagateEventInfoTrap,'seagateEventWarningTrap':seagateEventWarningTrap,'seagateEventErrorTrap':seagateEventErrorTrap,'seagateEventCriticalTrap':seagateEventCriticalTrap,'seagateEventResolvedTrap':seagateEventResolvedTrap})