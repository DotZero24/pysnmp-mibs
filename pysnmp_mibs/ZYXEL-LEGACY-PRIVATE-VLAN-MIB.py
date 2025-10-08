#
# PySNMP MIB module ZYXEL-LEGACY-PRIVATE-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/zyxel/ZYXEL-LEGACY-PRIVATE-VLAN-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:37:39 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
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
mibBuilder.exportSymbols("ZYXEL-LEGACY-PRIVATE-VLAN-MIB", zyxelLegacyPrivateVlanTable=zyxelLegacyPrivateVlanTable, zyLegacyPrivateVlanName=zyLegacyPrivateVlanName, zyLegacyPrivateVlanMaxNumberOfVlans=zyLegacyPrivateVlanMaxNumberOfVlans, zyxelLegacyPrivateVlan=zyxelLegacyPrivateVlan, PYSNMP_MODULE_ID=zyxelLegacyPrivateVlan, zyLegacyPrivateVlanPromiscuousPorts=zyLegacyPrivateVlanPromiscuousPorts, zyLegacyPrivateVlanVid=zyLegacyPrivateVlanVid, zyxelLegacyPrivateVlanEntry=zyxelLegacyPrivateVlanEntry, zyLegacyPrivateVlanRowStatus=zyLegacyPrivateVlanRowStatus, zyxelLegacyPrivateVlanSetup=zyxelLegacyPrivateVlanSetup)
