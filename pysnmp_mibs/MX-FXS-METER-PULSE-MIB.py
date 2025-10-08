#
# PySNMP MIB module MX-FXS-METER-PULSE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/media5/MX-FXS-METER-PULSE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:05:26 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
mediatrixExperimental, = mibBuilder.importSymbols("MX-SMI", "mediatrixExperimental")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("MX-FXS-METER-PULSE-MIB", fxsMeterPulseBasicComplVer1=fxsMeterPulseBasicComplVer1, fxsMeterPulseFreq=fxsMeterPulseFreq, fxsMeterPulseGroupVer1=fxsMeterPulseGroupVer1, fxsMeterPulseGroups=fxsMeterPulseGroups, fxsMeterPulseTable=fxsMeterPulseTable, PYSNMP_MODULE_ID=fxsMeterPulseMIB, fxsMeterPulseMIB=fxsMeterPulseMIB, fxsMeterPulseConformance=fxsMeterPulseConformance, fxsMeterPulseMIBObjects=fxsMeterPulseMIBObjects, fxsMeterPulseDuration=fxsMeterPulseDuration, fxsMeterPulseEntry=fxsMeterPulseEntry, fxsMeterPauseDuration=fxsMeterPauseDuration, fxsMeterPulseCompliances=fxsMeterPulseCompliances)
