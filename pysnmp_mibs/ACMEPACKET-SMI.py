_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
acmepacket=ModuleIdentity((1,3,6,1,4,1,9148))
if mibBuilder.loadTexts:acmepacket.setRevisions(('2012-02-02 18:00','2004-02-26 18:00','2001-09-05 00:00'))
_AcmepacketProducts_ObjectIdentity=ObjectIdentity
acmepacketProducts=_AcmepacketProducts_ObjectIdentity((1,3,6,1,4,1,9148,1))
if mibBuilder.loadTexts:acmepacketProducts.setStatus(_A)
_AcmepacketAgentCapability_ObjectIdentity=ObjectIdentity
acmepacketAgentCapability=_AcmepacketAgentCapability_ObjectIdentity((1,3,6,1,4,1,9148,2))
if mibBuilder.loadTexts:acmepacketAgentCapability.setStatus(_A)
_AcmepacketMgmt_ObjectIdentity=ObjectIdentity
acmepacketMgmt=_AcmepacketMgmt_ObjectIdentity((1,3,6,1,4,1,9148,3))
if mibBuilder.loadTexts:acmepacketMgmt.setStatus(_A)
_AcmepacketConfig_ObjectIdentity=ObjectIdentity
acmepacketConfig=_AcmepacketConfig_ObjectIdentity((1,3,6,1,4,1,9148,4))
if mibBuilder.loadTexts:acmepacketConfig.setStatus(_A)
_AcmepacketExperiment_ObjectIdentity=ObjectIdentity
acmepacketExperiment=_AcmepacketExperiment_ObjectIdentity((1,3,6,1,4,1,9148,5))
if mibBuilder.loadTexts:acmepacketExperiment.setStatus(_A)
_AcmepacketModules_ObjectIdentity=ObjectIdentity
acmepacketModules=_AcmepacketModules_ObjectIdentity((1,3,6,1,4,1,9148,6))
if mibBuilder.loadTexts:acmepacketModules.setStatus(_A)
mibBuilder.exportSymbols('ACMEPACKET-SMI',**{'acmepacket':acmepacket,'acmepacketProducts':acmepacketProducts,'acmepacketAgentCapability':acmepacketAgentCapability,'acmepacketMgmt':acmepacketMgmt,'acmepacketConfig':acmepacketConfig,'acmepacketExperiment':acmepacketExperiment,'acmepacketModules':acmepacketModules})