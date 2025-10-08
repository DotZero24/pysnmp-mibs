#
# PySNMP MIB module BASIS-RAS-DISK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/BASIS-RAS-DISK-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:14:10 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
axisDiagnostics, = mibBuilder.importSymbols("BASIS-MIB", "axisDiagnostics")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rasDsk = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 6, 2))
rasDskStatus = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rasDskStatus.setStatus('mandatory')
dskHealth = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("pass", 1), ("fail", 2), ("unknown", 3), ("testInProgress", 4))).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dskHealth.setStatus('mandatory')
standbyDskHealth = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("pass", 1), ("fail", 2), ("unknown", 3), ("testInProgress", 4))).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: standbyDskHealth.setStatus('mandatory')
wakeupInterval = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(12, 168)).clone(12)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wakeupInterval.setStatus('mandatory')
lastTime = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 2, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(20, 20)).setFixedLength(20)).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastTime.setStatus('mandatory')
numBadSectors = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 2, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numBadSectors.setStatus('mandatory')
crptdPRIfiles = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 2, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crptdPRIfiles.setStatus('mandatory')
crptdFWfiles = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 2, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crptdFWfiles.setStatus('mandatory')
mibBuilder.exportSymbols("BASIS-RAS-DISK-MIB", crptdFWfiles=crptdFWfiles, rasDskStatus=rasDskStatus, numBadSectors=numBadSectors, wakeupInterval=wakeupInterval, standbyDskHealth=standbyDskHealth, lastTime=lastTime, crptdPRIfiles=crptdPRIfiles, rasDsk=rasDsk, dskHealth=dskHealth)
