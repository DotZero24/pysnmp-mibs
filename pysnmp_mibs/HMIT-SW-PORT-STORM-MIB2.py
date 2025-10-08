#
# PySNMP MIB module HMIT-SW-PORT-STORM-MIB2 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hirschmann/HMIT-SW-PORT-STORM-MIB2
# Produced by pysmi-1.1.12 at Wed Oct  8 09:56:13 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hmITSwPortmgrMIB, hmITSwPortMIB = mibBuilder.importSymbols("HMIT-SW-PORT-MGR-MIB", "hmITSwPortmgrMIB", "hmITSwPortMIB")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
RowStatus, TextualConvention, MacAddress, PhysAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "MacAddress", "PhysAddress", "DisplayString")
hmITStormTable = MibTable((1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 3), )
if mibBuilder.loadTexts: hmITStormTable.setStatus('current')
hmITStormEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 3, 1), ).setIndexNames((0, "HMIT-SW-PORT-STORM-MIB2", "hmITPortId"), (0, "HMIT-SW-PORT-STORM-MIB2", "hmITStormControlPktType"))
if mibBuilder.loadTexts: hmITStormEntry.setStatus('current')
hmITPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmITPortId.setStatus('current')
hmITStormControlPktType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unicast", 1), ("broadcast", 2), ("multicast", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmITStormControlPktType.setStatus('current')
hmITStormControlLmtType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(4, 1, 2, 3))).clone(namedValues=NamedValues(("none", 4), ("kbps", 1), ("pps", 2), ("percent", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmITStormControlLmtType.setStatus('current')
hmITStormControlParam = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmITStormControlParam.setStatus('current')
hmITStormRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 3, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmITStormRowStatus.setStatus('current')
mibBuilder.exportSymbols("HMIT-SW-PORT-STORM-MIB2", hmITStormControlLmtType=hmITStormControlLmtType, hmITStormEntry=hmITStormEntry, hmITStormTable=hmITStormTable, hmITStormRowStatus=hmITStormRowStatus, hmITStormControlParam=hmITStormControlParam, hmITStormControlPktType=hmITStormControlPktType, hmITPortId=hmITPortId)
