#
# PySNMP MIB module ZYXEL-PRIVATE-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/zyxel/ZYXEL-PRIVATE-VLAN-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:37:39 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelPrivateVlan = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 68))
if mibBuilder.loadTexts: zyxelPrivateVlan.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelPrivateVlan.setOrganization('Enterprise Solution ZyXEL')
zyxelPrivateVlanSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 68, 1))
zyxelPrivateVlanTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 68, 1, 1), )
if mibBuilder.loadTexts: zyxelPrivateVlanTable.setStatus('current')
zyxelPrivateVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 68, 1, 1, 1), ).setIndexNames((0, "ZYXEL-PRIVATE-VLAN-MIB", "zyPrivateVlanType"))
if mibBuilder.loadTexts: zyxelPrivateVlanEntry.setStatus('current')
zyPrivateVlanType = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 68, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("normal", 0), ("primary", 1), ("isolated", 2), ("community", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyPrivateVlanType.setStatus('current')
zyPrivateVlanAssociatedVlanMap1k = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 68, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyPrivateVlanAssociatedVlanMap1k.setStatus('current')
zyPrivateVlanAssociatedVlanMap2k = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 68, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyPrivateVlanAssociatedVlanMap2k.setStatus('current')
zyPrivateVlanAssociatedVlanMap3k = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 68, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyPrivateVlanAssociatedVlanMap3k.setStatus('current')
zyPrivateVlanAssociatedVlanMap4k = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 68, 1, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyPrivateVlanAssociatedVlanMap4k.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-PRIVATE-VLAN-MIB", zyPrivateVlanAssociatedVlanMap2k=zyPrivateVlanAssociatedVlanMap2k, zyPrivateVlanAssociatedVlanMap1k=zyPrivateVlanAssociatedVlanMap1k, zyxelPrivateVlanEntry=zyxelPrivateVlanEntry, zyPrivateVlanType=zyPrivateVlanType, zyPrivateVlanAssociatedVlanMap4k=zyPrivateVlanAssociatedVlanMap4k, zyPrivateVlanAssociatedVlanMap3k=zyPrivateVlanAssociatedVlanMap3k, zyxelPrivateVlanSetup=zyxelPrivateVlanSetup, zyxelPrivateVlan=zyxelPrivateVlan, PYSNMP_MODULE_ID=zyxelPrivateVlan, zyxelPrivateVlanTable=zyxelPrivateVlanTable)
