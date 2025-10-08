#
# PySNMP MIB module CISCOSB-LBD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/ciscosb/CISCOSB-LBD-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:56:38 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
rlLbd = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 127))
rlLbd.setRevisions(('2007-11-07 00:00',))
if mibBuilder.loadTexts: rlLbd.setLastUpdated('200711070000Z')
if mibBuilder.loadTexts: rlLbd.setOrganization('Cisco Systems, Inc.')
rlLbdEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 127, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLbdEnable.setStatus('current')
rlLbdDetectionInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 127, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 60))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLbdDetectionInterval.setStatus('current')
rlLbdMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 127, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("source-mac-addr", 1), ("base-mac-addr", 2), ("broadcast-mac-addr", 3), ("predefined-multicast-mac-addr", 4), ("user-defined-mac-addr", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLbdMode.setStatus('current')
rlLbdPortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 127, 4), )
if mibBuilder.loadTexts: rlLbdPortTable.setStatus('current')
rlLbdPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 127, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rlLbdPortEntry.setStatus('current')
rlLbdPortAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 127, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLbdPortAdminStatus.setStatus('current')
rlLbdPortOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 127, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("inactive", 1), ("active", 2), ("loopDetected", 3))).clone('inactive')).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlLbdPortOperStatus.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-LBD-MIB", rlLbdPortOperStatus=rlLbdPortOperStatus, rlLbdPortTable=rlLbdPortTable, rlLbdPortEntry=rlLbdPortEntry, rlLbdDetectionInterval=rlLbdDetectionInterval, rlLbd=rlLbd, rlLbdMode=rlLbdMode, rlLbdPortAdminStatus=rlLbdPortAdminStatus, rlLbdEnable=rlLbdEnable, PYSNMP_MODULE_ID=rlLbd)
