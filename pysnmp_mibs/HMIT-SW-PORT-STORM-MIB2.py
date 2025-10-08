#
# PySNMP MIB module HMIT-SW-PORT-STORM-MIB2 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hirschmann/HMIT-SW-PORT-STORM-MIB2
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:12 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hmITSwPortmgrMIB, hmITSwPortMIB = mibBuilder.importSymbols("HMIT-SW-PORT-MGR-MIB", "hmITSwPortmgrMIB", "hmITSwPortMIB")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, RowStatus, PhysAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "RowStatus", "PhysAddress", "TextualConvention")
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
mibBuilder.exportSymbols("HMIT-SW-PORT-STORM-MIB2", hmITStormControlParam=hmITStormControlParam, hmITPortId=hmITPortId, hmITStormControlPktType=hmITStormControlPktType, hmITStormEntry=hmITStormEntry, hmITStormRowStatus=hmITStormRowStatus, hmITStormControlLmtType=hmITStormControlLmtType, hmITStormTable=hmITStormTable)
