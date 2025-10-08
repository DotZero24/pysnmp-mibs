#
# PySNMP MIB module NEWTEC-REFERENCECLOCK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/newtec/NEWTEC-REFERENCECLOCK-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:38:25 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ntcFunction, = mibBuilder.importSymbols("NEWTEC-MAIN-MIB", "ntcFunction")
NtcAlarmState, = mibBuilder.importSymbols("NEWTEC-TC-MIB", "NtcAlarmState")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ntcReferenceClock = ModuleIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 300))
ntcReferenceClock.setRevisions(('2013-09-20 08:00', '2012-06-28 12:00',))
if mibBuilder.loadTexts: ntcReferenceClock.setLastUpdated('201309200800Z')
if mibBuilder.loadTexts: ntcReferenceClock.setOrganization('Newtec Cy')
ntcRefClkObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 300, 1))
if mibBuilder.loadTexts: ntcRefClkObjects.setStatus('current')
ntcRefClkConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 300, 2))
if mibBuilder.loadTexts: ntcRefClkConformance.setStatus('current')
ntcRefClkAlarm = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 300, 1, 3))
if mibBuilder.loadTexts: ntcRefClkAlarm.setStatus('current')
ntcRefClkConfCompliance = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 300, 2, 1))
if mibBuilder.loadTexts: ntcRefClkConfCompliance.setStatus('current')
ntcRefClkConfGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 300, 2, 2))
if mibBuilder.loadTexts: ntcRefClkConfGroup.setStatus('current')
ntcRefClkRefSelection = MibScalar((1, 3, 6, 1, 4, 1, 5835, 5, 2, 300, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("internal", 0), ("external", 1))).clone('internal')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntcRefClkRefSelection.setStatus('current')
ntcRefClkExtRefFrequency = MibScalar((1, 3, 6, 1, 4, 1, 5835, 5, 2, 300, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 3, 4, 5))).clone(namedValues=NamedValues(("e1Mhz", 0), ("e2Mhz", 1), ("e5Mhz", 3), ("e10Mhz", 4), ("e20Mhz", 5))).clone('e10Mhz')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntcRefClkExtRefFrequency.setStatus('current')
ntcRefClkAlmRefClockNoSignal = MibScalar((1, 3, 6, 1, 4, 1, 5835, 5, 2, 300, 1, 3, 1), NtcAlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntcRefClkAlmRefClockNoSignal.setStatus('current')
ntcRefClkAlmRefClockNoLock = MibScalar((1, 3, 6, 1, 4, 1, 5835, 5, 2, 300, 1, 3, 2), NtcAlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntcRefClkAlmRefClockNoLock.setStatus('current')
ntcRefClkActiveRef = MibScalar((1, 3, 6, 1, 4, 1, 5835, 5, 2, 300, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("internal", 0), ("external", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntcRefClkActiveRef.setStatus('current')
ntcRefClkConfGrpV1Standard = ObjectGroup((1, 3, 6, 1, 4, 1, 5835, 5, 2, 300, 2, 2, 1)).setObjects(("NEWTEC-REFERENCECLOCK-MIB", "ntcRefClkRefSelection"), ("NEWTEC-REFERENCECLOCK-MIB", "ntcRefClkExtRefFrequency"), ("NEWTEC-REFERENCECLOCK-MIB", "ntcRefClkAlmRefClockNoSignal"), ("NEWTEC-REFERENCECLOCK-MIB", "ntcRefClkAlmRefClockNoLock"), ("NEWTEC-REFERENCECLOCK-MIB", "ntcRefClkActiveRef"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntcRefClkConfGrpV1Standard = ntcRefClkConfGrpV1Standard.setStatus('current')
ntcRefClkConfCompV1Standard = ModuleCompliance((1, 3, 6, 1, 4, 1, 5835, 5, 2, 300, 2, 1, 1)).setObjects(("NEWTEC-REFERENCECLOCK-MIB", "ntcRefClkConfGrpV1Standard"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntcRefClkConfCompV1Standard = ntcRefClkConfCompV1Standard.setStatus('current')
mibBuilder.exportSymbols("NEWTEC-REFERENCECLOCK-MIB", ntcRefClkAlmRefClockNoSignal=ntcRefClkAlmRefClockNoSignal, ntcRefClkObjects=ntcRefClkObjects, PYSNMP_MODULE_ID=ntcReferenceClock, ntcRefClkConfCompliance=ntcRefClkConfCompliance, ntcRefClkAlmRefClockNoLock=ntcRefClkAlmRefClockNoLock, ntcRefClkExtRefFrequency=ntcRefClkExtRefFrequency, ntcRefClkRefSelection=ntcRefClkRefSelection, ntcReferenceClock=ntcReferenceClock, ntcRefClkConformance=ntcRefClkConformance, ntcRefClkConfGroup=ntcRefClkConfGroup, ntcRefClkConfGrpV1Standard=ntcRefClkConfGrpV1Standard, ntcRefClkActiveRef=ntcRefClkActiveRef, ntcRefClkAlarm=ntcRefClkAlarm, ntcRefClkConfCompV1Standard=ntcRefClkConfCompV1Standard)
