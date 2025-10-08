#
# PySNMP MIB module PDN-DHCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/paradyne/PDN-DHCP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:41 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
pdn_common, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdn-common")
SwitchState, = mibBuilder.importSymbols("PDN-TC", "SwitchState")
dot1qVlanStaticEntry, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "dot1qVlanStaticEntry")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pdnDhcpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 57))
pdnDhcpMIB.setRevisions(('2004-09-14 00:00',))
if mibBuilder.loadTexts: pdnDhcpMIB.setLastUpdated('200409130000Z')
if mibBuilder.loadTexts: pdnDhcpMIB.setOrganization('Paradyne Networks MIB Working Group Other information about group editing the MIB')
pdnDhcpNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 57, 0))
pdnDhcpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 57, 1))
pdnDhcpAFNs = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 57, 2))
pdnDhcpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 57, 3))
pdnDhcpVlanConfigTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 57, 1, 1), )
if mibBuilder.loadTexts: pdnDhcpVlanConfigTable.setStatus('current')
pdnDhcpVlanConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 57, 1, 1, 1), )
dot1qVlanStaticEntry.registerAugmentions(("PDN-DHCP-MIB", "pdnDhcpVlanConfigEntry"))
pdnDhcpVlanConfigEntry.setIndexNames(*dot1qVlanStaticEntry.getIndexNames())
if mibBuilder.loadTexts: pdnDhcpVlanConfigEntry.setStatus('current')
pdnDhcpVlanConfigOption82 = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 57, 1, 1, 1, 1), SwitchState().clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pdnDhcpVlanConfigOption82.setStatus('current')
pdnDhcpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 57, 3, 1))
pdnDhcpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 57, 3, 2))
pdnDhcpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 57, 3, 1, 1)).setObjects(("PDN-DHCP-MIB", "pdnDhcpVlanConfigOpt82Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnDhcpCompliance = pdnDhcpCompliance.setStatus('current')
pdnDhcpObjGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 57, 3, 2, 1))
pdnDhcpAfnGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 57, 3, 2, 2))
pdnDhcpNtfyGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 57, 3, 2, 3))
pdnDhcpVlanConfigOpt82Group = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 57, 3, 2, 1, 2)).setObjects(("PDN-DHCP-MIB", "pdnDhcpVlanConfigOption82"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnDhcpVlanConfigOpt82Group = pdnDhcpVlanConfigOpt82Group.setStatus('current')
mibBuilder.exportSymbols("PDN-DHCP-MIB", pdnDhcpGroups=pdnDhcpGroups, pdnDhcpObjGroups=pdnDhcpObjGroups, PYSNMP_MODULE_ID=pdnDhcpMIB, pdnDhcpVlanConfigOption82=pdnDhcpVlanConfigOption82, pdnDhcpMIB=pdnDhcpMIB, pdnDhcpNtfyGroups=pdnDhcpNtfyGroups, pdnDhcpAfnGroups=pdnDhcpAfnGroups, pdnDhcpVlanConfigEntry=pdnDhcpVlanConfigEntry, pdnDhcpVlanConfigTable=pdnDhcpVlanConfigTable, pdnDhcpAFNs=pdnDhcpAFNs, pdnDhcpCompliances=pdnDhcpCompliances, pdnDhcpVlanConfigOpt82Group=pdnDhcpVlanConfigOpt82Group, pdnDhcpObjects=pdnDhcpObjects, pdnDhcpNotifications=pdnDhcpNotifications, pdnDhcpCompliance=pdnDhcpCompliance, pdnDhcpConformance=pdnDhcpConformance)
