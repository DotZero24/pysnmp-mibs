#
# PySNMP MIB module L2L3-VPN-MULTICAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/rfc/L2L3-VPN-MULTICAST-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:50:25 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
L2L3VpnMcastProviderTunnelType, L2L3VpnMcastProviderTunnelId = mibBuilder.importSymbols("L2L3-VPN-MULTICAST-TC-MIB", "L2L3VpnMcastProviderTunnelType", "L2L3VpnMcastProviderTunnelId")
MplsLabel, = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "MplsLabel")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Gauge32, zeroDotZero, MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "zeroDotZero", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "mib-2")
TextualConvention, RowPointer, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowPointer", "DisplayString")
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
mibBuilder.exportSymbols("L2L3-VPN-MULTICAST-MIB", l2L3VpnMcastMIB=l2L3VpnMcastMIB, l2L3VpnMcastGroups=l2L3VpnMcastGroups, l2L3VpnMcastPmsiTunnelAttributeType=l2L3VpnMcastPmsiTunnelAttributeType, l2L3VpnMcastPmsiTunnelAttributeId=l2L3VpnMcastPmsiTunnelAttributeId, l2L3VpnMcastPmsiTunnelAttributeTable=l2L3VpnMcastPmsiTunnelAttributeTable, l2L3VpnMcastPmsiTunnelPointer=l2L3VpnMcastPmsiTunnelPointer, PYSNMP_MODULE_ID=l2L3VpnMcastMIB, l2L3VpnMcastPmsiTunnelIf=l2L3VpnMcastPmsiTunnelIf, l2L3VpnMCastPmsiTunnelLeafInfoRequired=l2L3VpnMCastPmsiTunnelLeafInfoRequired, l2L3VpnMcastFullCompliance=l2L3VpnMcastFullCompliance, l2L3VpnMcastCoreGroup=l2L3VpnMcastCoreGroup, l2L3VpnMcastPmsiTunnelAttributeEntry=l2L3VpnMcastPmsiTunnelAttributeEntry, l2L3VpnMcastPmsiTunnelAttributeMplsLabel=l2L3VpnMcastPmsiTunnelAttributeMplsLabel, l2L3VpnMcastOptionalGroup=l2L3VpnMcastOptionalGroup, l2L3VpnMcastConformance=l2L3VpnMcastConformance, l2L3VpnMcastCompliances=l2L3VpnMcastCompliances, l2L3VpnMcastStates=l2L3VpnMcastStates, l2L3VpnMcastCoreCompliance=l2L3VpnMcastCoreCompliance)
