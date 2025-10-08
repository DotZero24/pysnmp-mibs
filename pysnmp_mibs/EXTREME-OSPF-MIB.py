#
# PySNMP MIB module EXTREME-OSPF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/extreme/EXTREME-OSPF-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:01:52 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
extremeAgent, = mibBuilder.importSymbols("EXTREME-BASE-MIB", "extremeAgent")
extremeVlanIfIndex, = mibBuilder.importSymbols("EXTREME-VLAN-MIB", "extremeVlanIfIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "TextualConvention", "DisplayString")
extremeOspf = ModuleIdentity((1, 3, 6, 1, 4, 1, 1916, 1, 15))
if mibBuilder.loadTexts: extremeOspf.setLastUpdated('200502140000Z')
if mibBuilder.loadTexts: extremeOspf.setOrganization('Extreme Networks, Inc.')
extremeOspfInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 15, 1), )
if mibBuilder.loadTexts: extremeOspfInterfaceTable.setStatus('current')
extremeOspfInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 15, 1, 1), ).setIndexNames((0, "EXTREME-VLAN-MIB", "extremeVlanIfIndex"))
if mibBuilder.loadTexts: extremeOspfInterfaceEntry.setStatus('current')
extremeOspfAreaId = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 15, 1, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extremeOspfAreaId.setStatus('current')
extremeOspfInterfacePassive = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 15, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extremeOspfInterfacePassive.setStatus('current')
extremeOspfInterfaceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 15, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremeOspfInterfaceStatus.setStatus('current')
mibBuilder.exportSymbols("EXTREME-OSPF-MIB", PYSNMP_MODULE_ID=extremeOspf, extremeOspfInterfacePassive=extremeOspfInterfacePassive, extremeOspfInterfaceEntry=extremeOspfInterfaceEntry, extremeOspfInterfaceTable=extremeOspfInterfaceTable, extremeOspfInterfaceStatus=extremeOspfInterfaceStatus, extremeOspfAreaId=extremeOspfAreaId, extremeOspf=extremeOspf)
