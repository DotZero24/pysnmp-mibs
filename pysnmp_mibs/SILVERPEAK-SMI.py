_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
silverpeakNW=ModuleIdentity((1,3,6,1,4,1,23867))
_SilverpeakProducts_ObjectIdentity=ObjectIdentity
silverpeakProducts=_SilverpeakProducts_ObjectIdentity((1,3,6,1,4,1,23867,1))
if mibBuilder.loadTexts:silverpeakProducts.setStatus(_A)
_SilverpeakModules_ObjectIdentity=ObjectIdentity
silverpeakModules=_SilverpeakModules_ObjectIdentity((1,3,6,1,4,1,23867,2))
if mibBuilder.loadTexts:silverpeakModules.setStatus(_A)
_SilverpeakMgmt_ObjectIdentity=ObjectIdentity
silverpeakMgmt=_SilverpeakMgmt_ObjectIdentity((1,3,6,1,4,1,23867,3))
if mibBuilder.loadTexts:silverpeakMgmt.setStatus(_A)
_SilverpeakNotifications_ObjectIdentity=ObjectIdentity
silverpeakNotifications=_SilverpeakNotifications_ObjectIdentity((1,3,6,1,4,1,23867,4))
if mibBuilder.loadTexts:silverpeakNotifications.setStatus(_A)
_SilverpeakAgentCapability_ObjectIdentity=ObjectIdentity
silverpeakAgentCapability=_SilverpeakAgentCapability_ObjectIdentity((1,3,6,1,4,1,23867,5))
if mibBuilder.loadTexts:silverpeakAgentCapability.setStatus(_A)
mibBuilder.exportSymbols('SILVERPEAK-SMI',**{'silverpeakNW':silverpeakNW,'silverpeakProducts':silverpeakProducts,'silverpeakModules':silverpeakModules,'silverpeakMgmt':silverpeakMgmt,'silverpeakNotifications':silverpeakNotifications,'silverpeakAgentCapability':silverpeakAgentCapability})