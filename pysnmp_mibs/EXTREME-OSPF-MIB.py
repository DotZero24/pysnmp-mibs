#
# PySNMP MIB module EXTREME-OSPF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/extreme/EXTREME-OSPF-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:58:50 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
extremeAgent, = mibBuilder.importSymbols("EXTREME-BASE-MIB", "extremeAgent")
extremeVlanIfIndex, = mibBuilder.importSymbols("EXTREME-VLAN-MIB", "extremeVlanIfIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
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
mibBuilder.exportSymbols("EXTREME-OSPF-MIB", extremeOspfInterfaceStatus=extremeOspfInterfaceStatus, extremeOspf=extremeOspf, extremeOspfInterfacePassive=extremeOspfInterfacePassive, PYSNMP_MODULE_ID=extremeOspf, extremeOspfAreaId=extremeOspfAreaId, extremeOspfInterfaceTable=extremeOspfInterfaceTable, extremeOspfInterfaceEntry=extremeOspfInterfaceEntry)
