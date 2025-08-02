_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
juniperMIB=ModuleIdentity((1,3,6,1,4,1,2636))
if mibBuilder.loadTexts:juniperMIB.setRevisions(('2003-04-17 01:00',))
_JnxProducts_ObjectIdentity=ObjectIdentity
jnxProducts=_JnxProducts_ObjectIdentity((1,3,6,1,4,1,2636,1))
if mibBuilder.loadTexts:jnxProducts.setStatus(_A)
_JnxServices_ObjectIdentity=ObjectIdentity
jnxServices=_JnxServices_ObjectIdentity((1,3,6,1,4,1,2636,2))
if mibBuilder.loadTexts:jnxServices.setStatus(_A)
_JnxMibs_ObjectIdentity=ObjectIdentity
jnxMibs=_JnxMibs_ObjectIdentity((1,3,6,1,4,1,2636,3))
if mibBuilder.loadTexts:jnxMibs.setStatus(_A)
_JnxTraps_ObjectIdentity=ObjectIdentity
jnxTraps=_JnxTraps_ObjectIdentity((1,3,6,1,4,1,2636,4))
if mibBuilder.loadTexts:jnxTraps.setStatus(_A)
_JnxChassisTraps_ObjectIdentity=ObjectIdentity
jnxChassisTraps=_JnxChassisTraps_ObjectIdentity((1,3,6,1,4,1,2636,4,1))
_JnxChassisOKTraps_ObjectIdentity=ObjectIdentity
jnxChassisOKTraps=_JnxChassisOKTraps_ObjectIdentity((1,3,6,1,4,1,2636,4,2))
_JnxRmonTraps_ObjectIdentity=ObjectIdentity
jnxRmonTraps=_JnxRmonTraps_ObjectIdentity((1,3,6,1,4,1,2636,4,3))
_JnxLdpTraps_ObjectIdentity=ObjectIdentity
jnxLdpTraps=_JnxLdpTraps_ObjectIdentity((1,3,6,1,4,1,2636,4,4))
_JnxCmNotifications_ObjectIdentity=ObjectIdentity
jnxCmNotifications=_JnxCmNotifications_ObjectIdentity((1,3,6,1,4,1,2636,4,5))
_JnxSonetNotifications_ObjectIdentity=ObjectIdentity
jnxSonetNotifications=_JnxSonetNotifications_ObjectIdentity((1,3,6,1,4,1,2636,4,6))
_JnxPMonNotifications_ObjectIdentity=ObjectIdentity
jnxPMonNotifications=_JnxPMonNotifications_ObjectIdentity((1,3,6,1,4,1,2636,4,7))
_JnxExperiment_ObjectIdentity=ObjectIdentity
jnxExperiment=_JnxExperiment_ObjectIdentity((1,3,6,1,4,1,2636,5))
mibBuilder.exportSymbols('JUNIPER-SMI',**{'juniperMIB':juniperMIB,'jnxProducts':jnxProducts,'jnxServices':jnxServices,'jnxMibs':jnxMibs,'jnxTraps':jnxTraps,'jnxChassisTraps':jnxChassisTraps,'jnxChassisOKTraps':jnxChassisOKTraps,'jnxRmonTraps':jnxRmonTraps,'jnxLdpTraps':jnxLdpTraps,'jnxCmNotifications':jnxCmNotifications,'jnxSonetNotifications':jnxSonetNotifications,'jnxPMonNotifications':jnxPMonNotifications,'jnxExperiment':jnxExperiment})