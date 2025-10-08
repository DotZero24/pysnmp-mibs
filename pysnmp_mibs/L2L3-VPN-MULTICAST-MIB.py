#
# PySNMP MIB module L2L3-VPN-MULTICAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rfc/L2L3-VPN-MULTICAST-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:27:53 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
L2L3VpnMcastProviderTunnelId, L2L3VpnMcastProviderTunnelType = mibBuilder.importSymbols("L2L3-VPN-MULTICAST-TC-MIB", "L2L3VpnMcastProviderTunnelId", "L2L3VpnMcastProviderTunnelType")
MplsLabel, = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "MplsLabel")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, zeroDotZero, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, TimeTicks, Unsigned32, MibIdentifier, Integer32, Bits, mib_2, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "zeroDotZero", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "TimeTicks", "Unsigned32", "MibIdentifier", "Integer32", "Bits", "mib-2", "IpAddress")
DisplayString, RowPointer, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowPointer", "TextualConvention")
l2L3VpnMcastMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 245))
l2L3VpnMcastMIB.setRevisions(('2018-12-14 00:00',))
if mibBuilder.loadTexts: l2L3VpnMcastMIB.setLastUpdated('201812140000Z')
if mibBuilder.loadTexts: l2L3VpnMcastMIB.setOrganization('IETF BESS Working Group')
l2L3VpnMcastStates = MibIdentifier((1, 3, 6, 1, 2, 1, 245, 1))
l2L3VpnMcastConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 245, 2))
l2L3VpnMcastPmsiTunnelAttributeTable = MibTable((1, 3, 6, 1, 2, 1, 245, 1, 1), )
if mibBuilder.loadTexts: l2L3VpnMcastPmsiTunnelAttributeTable.setStatus('current')
l2L3VpnMcastPmsiTunnelAttributeEntry = MibTableRow((1, 3, 6, 1, 2, 1, 245, 1, 1, 1), ).setIndexNames((0, "L2L3-VPN-MULTICAST-MIB", "l2L3VpnMcastPmsiTunnelAttributeType"), (0, "L2L3-VPN-MULTICAST-MIB", "l2L3VpnMcastPmsiTunnelAttributeId"))
if mibBuilder.loadTexts: l2L3VpnMcastPmsiTunnelAttributeEntry.setStatus('current')
l2L3VpnMcastPmsiTunnelAttributeType = MibTableColumn((1, 3, 6, 1, 2, 1, 245, 1, 1, 1, 1), L2L3VpnMcastProviderTunnelType())
if mibBuilder.loadTexts: l2L3VpnMcastPmsiTunnelAttributeType.setStatus('current')
l2L3VpnMcastPmsiTunnelAttributeId = MibTableColumn((1, 3, 6, 1, 2, 1, 245, 1, 1, 1, 2), L2L3VpnMcastProviderTunnelId())
if mibBuilder.loadTexts: l2L3VpnMcastPmsiTunnelAttributeId.setStatus('current')
l2L3VpnMCastPmsiTunnelLeafInfoRequired = MibTableColumn((1, 3, 6, 1, 2, 1, 245, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("false", 0), ("true", 1), ("notAvailable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: l2L3VpnMCastPmsiTunnelLeafInfoRequired.setStatus('current')
l2L3VpnMcastPmsiTunnelAttributeMplsLabel = MibTableColumn((1, 3, 6, 1, 2, 1, 245, 1, 1, 1, 4), MplsLabel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: l2L3VpnMcastPmsiTunnelAttributeMplsLabel.setStatus('current')
l2L3VpnMcastPmsiTunnelPointer = MibTableColumn((1, 3, 6, 1, 2, 1, 245, 1, 1, 1, 5), RowPointer().clone((0, 0))).setMaxAccess("readonly")
if mibBuilder.loadTexts: l2L3VpnMcastPmsiTunnelPointer.setStatus('current')
l2L3VpnMcastPmsiTunnelIf = MibTableColumn((1, 3, 6, 1, 2, 1, 245, 1, 1, 1, 6), RowPointer().clone((0, 0))).setMaxAccess("readonly")
if mibBuilder.loadTexts: l2L3VpnMcastPmsiTunnelIf.setStatus('current')
l2L3VpnMcastCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 245, 2, 1))
l2L3VpnMcastGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 245, 2, 2))
l2L3VpnMcastCoreCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 245, 2, 1, 1)).setObjects(("L2L3-VPN-MULTICAST-MIB", "l2L3VpnMcastCoreGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    l2L3VpnMcastCoreCompliance = l2L3VpnMcastCoreCompliance.setStatus('current')
l2L3VpnMcastFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 245, 2, 1, 2)).setObjects(("L2L3-VPN-MULTICAST-MIB", "l2L3VpnMcastCoreGroup"), ("L2L3-VPN-MULTICAST-MIB", "l2L3VpnMcastOptionalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    l2L3VpnMcastFullCompliance = l2L3VpnMcastFullCompliance.setStatus('current')
l2L3VpnMcastCoreGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 245, 2, 2, 1)).setObjects(("L2L3-VPN-MULTICAST-MIB", "l2L3VpnMCastPmsiTunnelLeafInfoRequired"), ("L2L3-VPN-MULTICAST-MIB", "l2L3VpnMcastPmsiTunnelAttributeMplsLabel"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    l2L3VpnMcastCoreGroup = l2L3VpnMcastCoreGroup.setStatus('current')
l2L3VpnMcastOptionalGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 245, 2, 2, 2)).setObjects(("L2L3-VPN-MULTICAST-MIB", "l2L3VpnMcastPmsiTunnelPointer"), ("L2L3-VPN-MULTICAST-MIB", "l2L3VpnMcastPmsiTunnelIf"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    l2L3VpnMcastOptionalGroup = l2L3VpnMcastOptionalGroup.setStatus('current')
mibBuilder.exportSymbols("L2L3-VPN-MULTICAST-MIB", l2L3VpnMcastPmsiTunnelAttributeEntry=l2L3VpnMcastPmsiTunnelAttributeEntry, PYSNMP_MODULE_ID=l2L3VpnMcastMIB, l2L3VpnMcastCompliances=l2L3VpnMcastCompliances, l2L3VpnMcastGroups=l2L3VpnMcastGroups, l2L3VpnMcastPmsiTunnelAttributeMplsLabel=l2L3VpnMcastPmsiTunnelAttributeMplsLabel, l2L3VpnMcastConformance=l2L3VpnMcastConformance, l2L3VpnMcastCoreGroup=l2L3VpnMcastCoreGroup, l2L3VpnMcastCoreCompliance=l2L3VpnMcastCoreCompliance, l2L3VpnMcastMIB=l2L3VpnMcastMIB, l2L3VpnMcastPmsiTunnelIf=l2L3VpnMcastPmsiTunnelIf, l2L3VpnMcastPmsiTunnelAttributeTable=l2L3VpnMcastPmsiTunnelAttributeTable, l2L3VpnMCastPmsiTunnelLeafInfoRequired=l2L3VpnMCastPmsiTunnelLeafInfoRequired, l2L3VpnMcastPmsiTunnelPointer=l2L3VpnMcastPmsiTunnelPointer, l2L3VpnMcastOptionalGroup=l2L3VpnMcastOptionalGroup, l2L3VpnMcastFullCompliance=l2L3VpnMcastFullCompliance, l2L3VpnMcastStates=l2L3VpnMcastStates, l2L3VpnMcastPmsiTunnelAttributeId=l2L3VpnMcastPmsiTunnelAttributeId, l2L3VpnMcastPmsiTunnelAttributeType=l2L3VpnMcastPmsiTunnelAttributeType)
