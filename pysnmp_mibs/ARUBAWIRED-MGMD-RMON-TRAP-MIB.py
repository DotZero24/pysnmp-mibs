_C='eventIndex'
_B='eventDescription'
_A='RMON-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
wndFeatures,=mibBuilder.importSymbols('ARUBAWIRED-NETWORKING-OID','wndFeatures')
eventDescription,eventIndex=mibBuilder.importSymbols(_A,_B,_C)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
arubaWiredMgmdRmonTrapMIB=ModuleIdentity((1,3,6,1,4,1,47196,4,1,1,3,4))
if mibBuilder.loadTexts:arubaWiredMgmdRmonTrapMIB.setRevisions(('2017-11-02 00:00',))
_ArubaWiredMgmdRmonTrapNotifications_ObjectIdentity=ObjectIdentity
arubaWiredMgmdRmonTrapNotifications=_ArubaWiredMgmdRmonTrapNotifications_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,4,1))
arubaWiredMgmdRmonTrapEvent=NotificationType((1,3,6,1,4,1,47196,4,1,1,3,4,1,1))
arubaWiredMgmdRmonTrapEvent.setObjects(*((_A,_C),(_A,_B)))
if mibBuilder.loadTexts:arubaWiredMgmdRmonTrapEvent.setStatus('current')
mibBuilder.exportSymbols('ARUBAWIRED-MGMD-RMON-TRAP-MIB',**{'arubaWiredMgmdRmonTrapMIB':arubaWiredMgmdRmonTrapMIB,'arubaWiredMgmdRmonTrapNotifications':arubaWiredMgmdRmonTrapNotifications,'arubaWiredMgmdRmonTrapEvent':arubaWiredMgmdRmonTrapEvent})