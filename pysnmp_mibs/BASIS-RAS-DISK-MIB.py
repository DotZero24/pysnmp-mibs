#
# PySNMP MIB module BASIS-RAS-DISK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/BASIS-RAS-DISK-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:27:49 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
axisDiagnostics, = mibBuilder.importSymbols("BASIS-MIB", "axisDiagnostics")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("BASIS-RAS-DISK-MIB", standbyDskHealth=standbyDskHealth, crptdFWfiles=crptdFWfiles, dskHealth=dskHealth, rasDsk=rasDsk, crptdPRIfiles=crptdPRIfiles, wakeupInterval=wakeupInterval, lastTime=lastTime, numBadSectors=numBadSectors, rasDskStatus=rasDskStatus)
