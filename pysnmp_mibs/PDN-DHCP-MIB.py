#
# PySNMP MIB module PDN-DHCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/paradyne/PDN-DHCP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:57:21 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
pdn_common, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdn-common")
SwitchState, = mibBuilder.importSymbols("PDN-TC", "SwitchState")
dot1qVlanStaticEntry, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "dot1qVlanStaticEntry")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("PDN-DHCP-MIB", pdnDhcpVlanConfigTable=pdnDhcpVlanConfigTable, pdnDhcpCompliances=pdnDhcpCompliances, pdnDhcpConformance=pdnDhcpConformance, pdnDhcpObjects=pdnDhcpObjects, pdnDhcpAFNs=pdnDhcpAFNs, pdnDhcpVlanConfigEntry=pdnDhcpVlanConfigEntry, pdnDhcpCompliance=pdnDhcpCompliance, pdnDhcpAfnGroups=pdnDhcpAfnGroups, pdnDhcpNtfyGroups=pdnDhcpNtfyGroups, pdnDhcpNotifications=pdnDhcpNotifications, PYSNMP_MODULE_ID=pdnDhcpMIB, pdnDhcpObjGroups=pdnDhcpObjGroups, pdnDhcpMIB=pdnDhcpMIB, pdnDhcpVlanConfigOption82=pdnDhcpVlanConfigOption82, pdnDhcpVlanConfigOpt82Group=pdnDhcpVlanConfigOpt82Group, pdnDhcpGroups=pdnDhcpGroups)
