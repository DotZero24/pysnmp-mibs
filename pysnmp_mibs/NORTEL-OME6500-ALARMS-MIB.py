#
# PySNMP MIB module NORTEL-OME6500-ALARMS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/nortel/NORTEL-OME6500-ALARMS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:59:21 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ome6500, = mibBuilder.importSymbols("NORTEL-OPTICAL-OME6500-MIB", "ome6500")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
nnOme6500Alarms = ModuleIdentity((1, 3, 6, 1, 4, 1, 562, 68, 11, 4))
nnOme6500Alarms.setRevisions(('2007-02-02 00:00', '2008-02-07 00:00', '2009-06-15 00:00',))
if mibBuilder.loadTexts: nnOme6500Alarms.setLastUpdated('200906150000Z')
if mibBuilder.loadTexts: nnOme6500Alarms.setOrganization('Nortel')
nnOme6500AlarmCounts = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 68, 11, 4, 1))
critical = MibScalar((1, 3, 6, 1, 4, 1, 562, 68, 11, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: critical.setStatus('current')
major = MibScalar((1, 3, 6, 1, 4, 1, 562, 68, 11, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: major.setStatus('current')
minor = MibScalar((1, 3, 6, 1, 4, 1, 562, 68, 11, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: minor.setStatus('current')
warnings = MibScalar((1, 3, 6, 1, 4, 1, 562, 68, 11, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: warnings.setStatus('current')
lastAlarmTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 562, 68, 11, 4, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastAlarmTimeStamp.setStatus('current')
mibBuilder.exportSymbols("NORTEL-OME6500-ALARMS-MIB", minor=minor, PYSNMP_MODULE_ID=nnOme6500Alarms, critical=critical, nnOme6500AlarmCounts=nnOme6500AlarmCounts, major=major, lastAlarmTimeStamp=lastAlarmTimeStamp, nnOme6500Alarms=nnOme6500Alarms, warnings=warnings)
