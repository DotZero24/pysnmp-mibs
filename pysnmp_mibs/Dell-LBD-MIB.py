#
# PySNMP MIB module Dell-LBD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/dell/Dell-LBD-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:23:30 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
rnd, = mibBuilder.importSymbols("Dell-MIB", "rnd")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
rlLbd = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 127))
rlLbd.setRevisions(('2007-11-07 00:00',))
if mibBuilder.loadTexts: rlLbd.setLastUpdated('200711070000Z')
if mibBuilder.loadTexts: rlLbd.setOrganization('Dell')
rlLbdEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 127, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLbdEnable.setStatus('current')
rlLbdDetectionInterval = MibScalar((1, 3, 6, 1, 4, 1, 89, 127, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 60))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLbdDetectionInterval.setStatus('current')
rlLbdMode = MibScalar((1, 3, 6, 1, 4, 1, 89, 127, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("source-mac-addr", 1), ("base-mac-addr", 2), ("broadcast-mac-addr", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLbdMode.setStatus('current')
rlLbdPortTable = MibTable((1, 3, 6, 1, 4, 1, 89, 127, 4), )
if mibBuilder.loadTexts: rlLbdPortTable.setStatus('current')
rlLbdPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 127, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rlLbdPortEntry.setStatus('current')
rlLbdPortAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 127, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLbdPortAdminStatus.setStatus('current')
rlLbdPortOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 127, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("inactive", 1), ("active", 2), ("loopDetected", 3))).clone('inactive')).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlLbdPortOperStatus.setStatus('current')
mibBuilder.exportSymbols("Dell-LBD-MIB", rlLbdPortTable=rlLbdPortTable, rlLbdEnable=rlLbdEnable, rlLbd=rlLbd, rlLbdPortEntry=rlLbdPortEntry, rlLbdPortOperStatus=rlLbdPortOperStatus, PYSNMP_MODULE_ID=rlLbd, rlLbdDetectionInterval=rlLbdDetectionInterval, rlLbdMode=rlLbdMode, rlLbdPortAdminStatus=rlLbdPortAdminStatus)
