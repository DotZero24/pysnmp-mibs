#
# PySNMP MIB module ZYXEL-LEGACY-PRIVATE-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/zyxel/ZYXEL-LEGACY-PRIVATE-VLAN-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:03:19 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelLegacyPrivateVlan = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 41))
if mibBuilder.loadTexts: zyxelLegacyPrivateVlan.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelLegacyPrivateVlan.setOrganization('Enterprise Solution ZyXEL')
zyxelLegacyPrivateVlanSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 41, 1))
zyLegacyPrivateVlanMaxNumberOfVlans = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 41, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyLegacyPrivateVlanMaxNumberOfVlans.setStatus('current')
zyxelLegacyPrivateVlanTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 41, 1, 2), )
if mibBuilder.loadTexts: zyxelLegacyPrivateVlanTable.setStatus('current')
zyxelLegacyPrivateVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 41, 1, 2, 1), ).setIndexNames((0, "ZYXEL-LEGACY-PRIVATE-VLAN-MIB", "zyLegacyPrivateVlanVid"))
if mibBuilder.loadTexts: zyxelLegacyPrivateVlanEntry.setStatus('current')
zyLegacyPrivateVlanVid = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 41, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)))
if mibBuilder.loadTexts: zyLegacyPrivateVlanVid.setStatus('current')
zyLegacyPrivateVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 41, 1, 2, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLegacyPrivateVlanName.setStatus('current')
zyLegacyPrivateVlanPromiscuousPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 41, 1, 2, 1, 3), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLegacyPrivateVlanPromiscuousPorts.setStatus('current')
zyLegacyPrivateVlanRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 41, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zyLegacyPrivateVlanRowStatus.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-LEGACY-PRIVATE-VLAN-MIB", zyLegacyPrivateVlanName=zyLegacyPrivateVlanName, zyLegacyPrivateVlanRowStatus=zyLegacyPrivateVlanRowStatus, zyLegacyPrivateVlanPromiscuousPorts=zyLegacyPrivateVlanPromiscuousPorts, zyLegacyPrivateVlanMaxNumberOfVlans=zyLegacyPrivateVlanMaxNumberOfVlans, PYSNMP_MODULE_ID=zyxelLegacyPrivateVlan, zyxelLegacyPrivateVlanTable=zyxelLegacyPrivateVlanTable, zyLegacyPrivateVlanVid=zyLegacyPrivateVlanVid, zyxelLegacyPrivateVlanSetup=zyxelLegacyPrivateVlanSetup, zyxelLegacyPrivateVlan=zyxelLegacyPrivateVlan, zyxelLegacyPrivateVlanEntry=zyxelLegacyPrivateVlanEntry)
