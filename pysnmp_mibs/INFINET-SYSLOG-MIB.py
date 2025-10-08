#
# PySNMP MIB module INFINET-SYSLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinet/INFINET-SYSLOG-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:15 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
sysTrapSequence, sysSerialNumber = mibBuilder.importSymbols("AQUASYSTEM-MIB", "sysTrapSequence", "sysSerialNumber")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
wanflex, = mibBuilder.importSymbols("INFINET-MIB", "wanflex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
infinetSyslogMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3942, 1, 1, 6))
infinetSyslogMIB.setRevisions(('2008-02-07 11:36',))
if mibBuilder.loadTexts: infinetSyslogMIB.setLastUpdated('200802071136Z')
if mibBuilder.loadTexts: infinetSyslogMIB.setOrganization('Infinet Wireless Ltd.')
class InfinetSyslogFacility(TextualConvention, Integer32):
    reference = 'RFC 3164, Section 4.1 - syslog Message Parts'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23))
    namedValues = NamedValues(("kernel", 0), ("user", 1), ("mail", 2), ("daemon", 3), ("authentication", 4), ("syslog", 5), ("lpr", 6), ("news", 7), ("uucp", 8), ("cron", 9), ("authpriv", 10), ("ftp", 11), ("ntp", 12), ("security", 13), ("console", 14), ("local0", 16), ("local1", 17), ("local2", 18), ("local3", 19), ("local4", 20), ("local5", 21), ("local6", 22), ("local7", 23))

class InfinetSyslogSeverity(TextualConvention, Integer32):
    reference = 'RFC 3164, Section 4.1 - syslog Message Parts'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("emergency", 0), ("alert", 1), ("critical", 2), ("error", 3), ("warning", 4), ("notice", 5), ("info", 6), ("debug", 7))

infinetSyslogObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3942, 1, 1, 6, 1))
infinetSyslogServerAddress = MibScalar((1, 3, 6, 1, 4, 1, 3942, 1, 1, 6, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: infinetSyslogServerAddress.setStatus('current')
infinetSyslogMessagesTable = MibTable((1, 3, 6, 1, 4, 1, 3942, 1, 1, 6, 1, 2), )
if mibBuilder.loadTexts: infinetSyslogMessagesTable.setStatus('current')
infinetSyslogMessageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3942, 1, 1, 6, 1, 2, 1), ).setIndexNames((0, "INFINET-SYSLOG-MIB", "infinetSyslogMessageIndex"))
if mibBuilder.loadTexts: infinetSyslogMessageEntry.setStatus('current')
infinetSyslogMessageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3942, 1, 1, 6, 1, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: infinetSyslogMessageIndex.setStatus('current')
infinetSyslogMessageSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 3942, 1, 1, 6, 1, 2, 1, 2), InfinetSyslogSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: infinetSyslogMessageSeverity.setStatus('current')
infinetSyslogMessageFacility = MibTableColumn((1, 3, 6, 1, 4, 1, 3942, 1, 1, 6, 1, 2, 1, 3), InfinetSyslogFacility()).setMaxAccess("readonly")
if mibBuilder.loadTexts: infinetSyslogMessageFacility.setStatus('current')
infinetSyslogMessageTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 3942, 1, 1, 6, 1, 2, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: infinetSyslogMessageTimestamp.setStatus('current')
infinetSyslogMessageIdentity = MibTableColumn((1, 3, 6, 1, 4, 1, 3942, 1, 1, 6, 1, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: infinetSyslogMessageIdentity.setStatus('current')
infinetSyslogMessageText = MibTableColumn((1, 3, 6, 1, 4, 1, 3942, 1, 1, 6, 1, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: infinetSyslogMessageText.setStatus('current')
infinetSyslogEventsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 3942, 1, 1, 6, 2))
infinetSyslogEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 3942, 1, 1, 6, 2, 0))
infinetSyslogConf = MibIdentifier((1, 3, 6, 1, 4, 1, 3942, 1, 1, 6, 3))
infinetSyslogGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 3942, 1, 1, 6, 3, 1))
infinetSyslogCompls = MibIdentifier((1, 3, 6, 1, 4, 1, 3942, 1, 1, 6, 3, 2))
infinetSyslogMessageGenerated = NotificationType((1, 3, 6, 1, 4, 1, 3942, 1, 1, 6, 2, 0, 1)).setObjects(("AQUASYSTEM-MIB", "sysSerialNumber"), ("AQUASYSTEM-MIB", "sysTrapSequence"), ("INFINET-SYSLOG-MIB", "infinetSyslogMessageIndex"), ("INFINET-SYSLOG-MIB", "infinetSyslogMessageSeverity"), ("INFINET-SYSLOG-MIB", "infinetSyslogMessageFacility"), ("INFINET-SYSLOG-MIB", "infinetSyslogMessageTimestamp"), ("INFINET-SYSLOG-MIB", "infinetSyslogMessageIdentity"), ("INFINET-SYSLOG-MIB", "infinetSyslogMessageText"))
if mibBuilder.loadTexts: infinetSyslogMessageGenerated.setStatus('current')
infinetSyslogBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3942, 1, 1, 6, 3, 1, 1)).setObjects(("INFINET-SYSLOG-MIB", "infinetSyslogServerAddress"), ("INFINET-SYSLOG-MIB", "infinetSyslogMessageIndex"), ("INFINET-SYSLOG-MIB", "infinetSyslogMessageSeverity"), ("INFINET-SYSLOG-MIB", "infinetSyslogMessageText"), ("INFINET-SYSLOG-MIB", "infinetSyslogMessageFacility"), ("INFINET-SYSLOG-MIB", "infinetSyslogMessageTimestamp"), ("INFINET-SYSLOG-MIB", "infinetSyslogMessageIdentity"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    infinetSyslogBasicGroup = infinetSyslogBasicGroup.setStatus('current')
infinetSyslogBasicEvents = NotificationGroup((1, 3, 6, 1, 4, 1, 3942, 1, 1, 6, 3, 1, 2)).setObjects(("INFINET-SYSLOG-MIB", "infinetSyslogMessageGenerated"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    infinetSyslogBasicEvents = infinetSyslogBasicEvents.setStatus('current')
mibBuilder.exportSymbols("INFINET-SYSLOG-MIB", infinetSyslogEvents=infinetSyslogEvents, infinetSyslogServerAddress=infinetSyslogServerAddress, infinetSyslogMessageGenerated=infinetSyslogMessageGenerated, infinetSyslogBasicEvents=infinetSyslogBasicEvents, infinetSyslogMessageTimestamp=infinetSyslogMessageTimestamp, infinetSyslogEventsPrefix=infinetSyslogEventsPrefix, infinetSyslogMessageIndex=infinetSyslogMessageIndex, infinetSyslogMessageIdentity=infinetSyslogMessageIdentity, infinetSyslogMIB=infinetSyslogMIB, infinetSyslogMessageText=infinetSyslogMessageText, infinetSyslogConf=infinetSyslogConf, infinetSyslogCompls=infinetSyslogCompls, infinetSyslogMessagesTable=infinetSyslogMessagesTable, infinetSyslogBasicGroup=infinetSyslogBasicGroup, InfinetSyslogFacility=InfinetSyslogFacility, infinetSyslogObjects=infinetSyslogObjects, infinetSyslogMessageFacility=infinetSyslogMessageFacility, infinetSyslogMessageEntry=infinetSyslogMessageEntry, InfinetSyslogSeverity=InfinetSyslogSeverity, infinetSyslogGroups=infinetSyslogGroups, infinetSyslogMessageSeverity=infinetSyslogMessageSeverity, PYSNMP_MODULE_ID=infinetSyslogMIB)
