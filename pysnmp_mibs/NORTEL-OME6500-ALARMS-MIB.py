#
# PySNMP MIB module NORTEL-OME6500-ALARMS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/nortel/NORTEL-OME6500-ALARMS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:02:59 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ome6500, = mibBuilder.importSymbols("NORTEL-OPTICAL-OME6500-MIB", "ome6500")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("NORTEL-OME6500-ALARMS-MIB", major=major, nnOme6500AlarmCounts=nnOme6500AlarmCounts, PYSNMP_MODULE_ID=nnOme6500Alarms, lastAlarmTimeStamp=lastAlarmTimeStamp, warnings=warnings, minor=minor, nnOme6500Alarms=nnOme6500Alarms, critical=critical)
