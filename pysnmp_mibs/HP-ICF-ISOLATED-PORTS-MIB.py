#
# PySNMP MIB module HP-ICF-ISOLATED-PORTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HP-ICF-ISOLATED-PORTS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:07:59 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
PortList, dot1qVlanStaticEntry = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList", "dot1qVlanStaticEntry")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hpicfDot1qIsolatedPorts = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 109))
hpicfDot1qIsolatedPorts.setRevisions(('2014-04-14 00:00',))
if mibBuilder.loadTexts: hpicfDot1qIsolatedPorts.setLastUpdated('201404140000Z')
if mibBuilder.loadTexts: hpicfDot1qIsolatedPorts.setOrganization('HP Networking')
hpicfDot1qIsolatedPortConfigurationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 109, 1))
hpicfDot1qIsolatedPortConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 109, 2))
hpicfDot1qIsolatedPortsTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 109, 1, 1), )
if mibBuilder.loadTexts: hpicfDot1qIsolatedPortsTable.setStatus('current')
hpicfDot1qIsolatedPortsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 109, 1, 1, 1), )
dot1qVlanStaticEntry.registerAugmentions(("HP-ICF-ISOLATED-PORTS-MIB", "hpicfDot1qIsolatedPortsEntry"))
hpicfDot1qIsolatedPortsEntry.setIndexNames(*dot1qVlanStaticEntry.getIndexNames())
if mibBuilder.loadTexts: hpicfDot1qIsolatedPortsEntry.setStatus('current')
hpicfDot1qVlanStaticIsolatedPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 109, 1, 1, 1, 1), PortList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfDot1qVlanStaticIsolatedPorts.setStatus('current')
hpicfDot1qIsolatedPortCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 109, 2, 1))
hpicfDot1qIsolatedPortGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 109, 2, 2))
hpicfDot1qIsolatedPortCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 109, 2, 1, 1)).setObjects(("HP-ICF-ISOLATED-PORTS-MIB", "hpicfDot1qIsolatedPortGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDot1qIsolatedPortCompliance = hpicfDot1qIsolatedPortCompliance.setStatus('current')
hpicfDot1qIsolatedPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 109, 2, 2, 1)).setObjects(("HP-ICF-ISOLATED-PORTS-MIB", "hpicfDot1qVlanStaticIsolatedPorts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDot1qIsolatedPortGroup = hpicfDot1qIsolatedPortGroup.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-ISOLATED-PORTS-MIB", hpicfDot1qIsolatedPortConformance=hpicfDot1qIsolatedPortConformance, hpicfDot1qIsolatedPortCompliances=hpicfDot1qIsolatedPortCompliances, PYSNMP_MODULE_ID=hpicfDot1qIsolatedPorts, hpicfDot1qIsolatedPortCompliance=hpicfDot1qIsolatedPortCompliance, hpicfDot1qIsolatedPortsTable=hpicfDot1qIsolatedPortsTable, hpicfDot1qIsolatedPorts=hpicfDot1qIsolatedPorts, hpicfDot1qVlanStaticIsolatedPorts=hpicfDot1qVlanStaticIsolatedPorts, hpicfDot1qIsolatedPortConfigurationObjects=hpicfDot1qIsolatedPortConfigurationObjects, hpicfDot1qIsolatedPortsEntry=hpicfDot1qIsolatedPortsEntry, hpicfDot1qIsolatedPortGroup=hpicfDot1qIsolatedPortGroup, hpicfDot1qIsolatedPortGroups=hpicfDot1qIsolatedPortGroups)
