#
# PySNMP MIB module MX-FXS-METER-PULSE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/media5/MX-FXS-METER-PULSE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:39:01 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
mediatrixExperimental, = mibBuilder.importSymbols("MX-SMI", "mediatrixExperimental")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fxsMeterPulseMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4935, 99, 30))
fxsMeterPulseMIB.setRevisions(('1902-11-04 00:00',))
if mibBuilder.loadTexts: fxsMeterPulseMIB.setLastUpdated('0211040000Z')
if mibBuilder.loadTexts: fxsMeterPulseMIB.setOrganization('Mediatrix Telecom, Inc.')
fxsMeterPulseMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 99, 30, 1))
fxsMeterPulseConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 99, 30, 2))
fxsMeterPulseTable = MibTable((1, 3, 6, 1, 4, 1, 4935, 99, 30, 1, 30), )
if mibBuilder.loadTexts: fxsMeterPulseTable.setStatus('current')
fxsMeterPulseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4935, 99, 30, 1, 30, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: fxsMeterPulseEntry.setStatus('current')
fxsMeterPulseDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 4935, 99, 30, 1, 30, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(120, 220)).clone(160)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fxsMeterPulseDuration.setStatus('current')
fxsMeterPauseDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 4935, 99, 30, 1, 30, 1, 15), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(100, 600)).clone(360)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fxsMeterPauseDuration.setStatus('current')
fxsMeterPulseFreq = MibScalar((1, 3, 6, 1, 4, 1, 4935, 99, 30, 1, 35), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("freq-12-kHz", 1), ("freq-16-kHz", 2))).clone('freq-12-kHz')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fxsMeterPulseFreq.setStatus('current')
fxsMeterPulseCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 99, 30, 2, 1))
fxsMeterPulseBasicComplVer1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4935, 99, 30, 2, 1, 1)).setObjects(("MX-FXS-METER-PULSE-MIB", "fxsMeterPulseGroupVer1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fxsMeterPulseBasicComplVer1 = fxsMeterPulseBasicComplVer1.setStatus('current')
fxsMeterPulseGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 99, 30, 2, 2))
fxsMeterPulseGroupVer1 = ObjectGroup((1, 3, 6, 1, 4, 1, 4935, 99, 30, 2, 2, 1)).setObjects(("MX-FXS-METER-PULSE-MIB", "fxsMeterPulseDuration"), ("MX-FXS-METER-PULSE-MIB", "fxsMeterPauseDuration"), ("MX-FXS-METER-PULSE-MIB", "fxsMeterPulseFreq"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fxsMeterPulseGroupVer1 = fxsMeterPulseGroupVer1.setStatus('current')
mibBuilder.exportSymbols("MX-FXS-METER-PULSE-MIB", fxsMeterPulseConformance=fxsMeterPulseConformance, fxsMeterPulseCompliances=fxsMeterPulseCompliances, fxsMeterPulseMIB=fxsMeterPulseMIB, fxsMeterPulseDuration=fxsMeterPulseDuration, fxsMeterPulseBasicComplVer1=fxsMeterPulseBasicComplVer1, fxsMeterPulseTable=fxsMeterPulseTable, fxsMeterPauseDuration=fxsMeterPauseDuration, fxsMeterPulseFreq=fxsMeterPulseFreq, PYSNMP_MODULE_ID=fxsMeterPulseMIB, fxsMeterPulseMIBObjects=fxsMeterPulseMIBObjects, fxsMeterPulseGroups=fxsMeterPulseGroups, fxsMeterPulseEntry=fxsMeterPulseEntry, fxsMeterPulseGroupVer1=fxsMeterPulseGroupVer1)
