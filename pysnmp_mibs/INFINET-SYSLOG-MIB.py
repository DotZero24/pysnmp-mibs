#
# PySNMP MIB module INFINET-SYSLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinet/INFINET-SYSLOG-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:53 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
sysSerialNumber, sysTrapSequence = mibBuilder.importSymbols("AQUASYSTEM-MIB", "sysSerialNumber", "sysTrapSequence")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
wanflex, = mibBuilder.importSymbols("INFINET-MIB", "wanflex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, iso, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "iso", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
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
mibBuilder.exportSymbols("INFINET-SYSLOG-MIB", InfinetSyslogFacility=InfinetSyslogFacility, infinetSyslogMessageFacility=infinetSyslogMessageFacility, InfinetSyslogSeverity=InfinetSyslogSeverity, infinetSyslogGroups=infinetSyslogGroups, infinetSyslogObjects=infinetSyslogObjects, infinetSyslogMessageGenerated=infinetSyslogMessageGenerated, infinetSyslogMIB=infinetSyslogMIB, infinetSyslogMessageText=infinetSyslogMessageText, PYSNMP_MODULE_ID=infinetSyslogMIB, infinetSyslogEventsPrefix=infinetSyslogEventsPrefix, infinetSyslogMessageTimestamp=infinetSyslogMessageTimestamp, infinetSyslogMessageSeverity=infinetSyslogMessageSeverity, infinetSyslogMessageIdentity=infinetSyslogMessageIdentity, infinetSyslogEvents=infinetSyslogEvents, infinetSyslogBasicGroup=infinetSyslogBasicGroup, infinetSyslogBasicEvents=infinetSyslogBasicEvents, infinetSyslogServerAddress=infinetSyslogServerAddress, infinetSyslogCompls=infinetSyslogCompls, infinetSyslogMessagesTable=infinetSyslogMessagesTable, infinetSyslogConf=infinetSyslogConf, infinetSyslogMessageIndex=infinetSyslogMessageIndex, infinetSyslogMessageEntry=infinetSyslogMessageEntry)
