#
# PySNMP MIB module SUPERMICRO-CLKIWF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/supermicro/SUPERMICRO-CLKIWF-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:58:12 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
fsClkIwfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 10876, 101, 2, 46))
fsClkIwfMIB.setRevisions(('2012-09-05 00:00',))
if mibBuilder.loadTexts: fsClkIwfMIB.setLastUpdated('201209050000Z')
if mibBuilder.loadTexts: fsClkIwfMIB.setOrganization('Super Micro Computer Inc.')
fsClkIwfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 10876, 101, 2, 46, 1))
fsClkIwfNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 10876, 101, 2, 46, 2))
fsClkIwfGeneralGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 10876, 101, 2, 46, 1, 1))
class FsClkIwfTimeInterval(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

fsClkIwfClockVariance = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 2, 46, 1, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsClkIwfClockVariance.setStatus('current')
fsClkIwfClockClass = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 2, 46, 1, 1, 2), Integer32().clone(248)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsClkIwfClockClass.setStatus('current')
fsClkIwfClockAccuracy = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 2, 46, 1, 1, 3), Integer32().clone(254)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsClkIwfClockAccuracy.setStatus('current')
fsClkIwfClockTimeSource = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 2, 46, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(16, 32, 64, 80, 144, 160))).clone(namedValues=NamedValues(("atomicClock", 16), ("gps", 32), ("ptp", 64), ("ntp", 80), ("cmm", 144), ("internalOscillator", 160))).clone('cmm')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsClkIwfClockTimeSource.setStatus('current')
fsClkIwfCurrentUtcOffset = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 2, 46, 1, 1, 5), FsClkIwfTimeInterval()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsClkIwfCurrentUtcOffset.setStatus('deprecated')
fsClkIwfARBTime = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 2, 46, 1, 1, 6), FsClkIwfTimeInterval()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsClkIwfARBTime.setStatus('current')
fsClkIwfHoldoverSpecification = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 2, 46, 1, 1, 7), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsClkIwfHoldoverSpecification.setStatus('current')
fsClkIwfLostSync = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 2, 46, 1, 1, 8), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsClkIwfLostSync.setStatus('current')
fsClkIwfUtcOffset = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 2, 46, 1, 1, 9), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsClkIwfUtcOffset.setStatus('current')
fsClkIwfTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 10876, 101, 2, 46, 2, 0))
fsClkIwfGlobalErrTrapType = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 2, 46, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("none", 0), ("memfail", 1), ("bufffail", 2), ("timesourcechange", 3), ("clockclasschange", 4), ("clockaccuracychange", 5), ("clockvariancechange", 6), ("holdovermodechange", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsClkIwfGlobalErrTrapType.setStatus('current')
fsClkIwfNotification = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 2, 46, 2, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsClkIwfNotification.setStatus('current')
fsClkIwfGlobalErrorTrap = NotificationType((1, 3, 6, 1, 4, 1, 10876, 101, 2, 46, 2, 0, 1)).setObjects(("SUPERMICRO-CLKIWF-MIB", "fsClkIwfGlobalErrTrapType"))
if mibBuilder.loadTexts: fsClkIwfGlobalErrorTrap.setStatus('current')
mibBuilder.exportSymbols("SUPERMICRO-CLKIWF-MIB", fsClkIwfLostSync=fsClkIwfLostSync, fsClkIwfClockVariance=fsClkIwfClockVariance, fsClkIwfObjects=fsClkIwfObjects, fsClkIwfUtcOffset=fsClkIwfUtcOffset, fsClkIwfMIB=fsClkIwfMIB, fsClkIwfCurrentUtcOffset=fsClkIwfCurrentUtcOffset, PYSNMP_MODULE_ID=fsClkIwfMIB, fsClkIwfHoldoverSpecification=fsClkIwfHoldoverSpecification, fsClkIwfNotifications=fsClkIwfNotifications, fsClkIwfClockAccuracy=fsClkIwfClockAccuracy, fsClkIwfGlobalErrTrapType=fsClkIwfGlobalErrTrapType, fsClkIwfNotification=fsClkIwfNotification, fsClkIwfTrap=fsClkIwfTrap, fsClkIwfGeneralGroup=fsClkIwfGeneralGroup, FsClkIwfTimeInterval=FsClkIwfTimeInterval, fsClkIwfClockClass=fsClkIwfClockClass, fsClkIwfARBTime=fsClkIwfARBTime, fsClkIwfClockTimeSource=fsClkIwfClockTimeSource, fsClkIwfGlobalErrorTrap=fsClkIwfGlobalErrorTrap)
