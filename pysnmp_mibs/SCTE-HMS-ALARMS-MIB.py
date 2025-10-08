#
# PySNMP MIB module SCTE-HMS-ALARMS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/scte/SCTE-HMS-ALARMS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:00:55 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
commonLogicalID, commonPhysAddress = mibBuilder.importSymbols("SCTE-HMS-COMMON-MIB", "commonLogicalID", "commonPhysAddress")
alarmsIdent, = mibBuilder.importSymbols("SCTE-HMS-ROOTS", "alarmsIdent")
scteHmsTree, = mibBuilder.importSymbols("SCTE-ROOT", "scteHmsTree")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
alarmLogNumberOfEntries = MibScalar((1, 3, 6, 1, 4, 1, 5591, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogNumberOfEntries.setStatus('mandatory')
alarmLogLastIndex = MibScalar((1, 3, 6, 1, 4, 1, 5591, 1, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogLastIndex.setStatus('mandatory')
alarmLogTable = MibTable((1, 3, 6, 1, 4, 1, 5591, 1, 2, 3), )
if mibBuilder.loadTexts: alarmLogTable.setStatus('mandatory')
alarmLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5591, 1, 2, 3, 1), ).setIndexNames((0, "SCTE-HMS-ALARMS-MIB", "alarmLogIndex"))
if mibBuilder.loadTexts: alarmLogEntry.setStatus('mandatory')
alarmLogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogIndex.setStatus('mandatory')
alarmLogInformation = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 2, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(17, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogInformation.setStatus('mandatory')
alarmText = MibScalar((1, 3, 6, 1, 4, 1, 5591, 1, 2, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmText.setStatus('optional')
hmsAlarmEvent = NotificationType((1, 3, 6, 1, 4, 1, 5591, 1) + (0,1)).setObjects(("SCTE-HMS-COMMON-MIB", "commonPhysAddress"), ("SCTE-HMS-COMMON-MIB", "commonLogicalID"), ("SCTE-HMS-ALARMS-MIB", "alarmLogInformation"))
mibBuilder.exportSymbols("SCTE-HMS-ALARMS-MIB", hmsAlarmEvent=hmsAlarmEvent, alarmLogTable=alarmLogTable, alarmLogInformation=alarmLogInformation, alarmText=alarmText, alarmLogEntry=alarmLogEntry, alarmLogLastIndex=alarmLogLastIndex, alarmLogNumberOfEntries=alarmLogNumberOfEntries, alarmLogIndex=alarmLogIndex)
