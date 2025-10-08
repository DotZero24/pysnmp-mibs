#
# PySNMP MIB module ENTERASYS-DIAGNOSTIC-MESSAGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/enterasys/ENTERASYS-DIAGNOSTIC-MESSAGE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:34:15 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention")
etsysDiagnosticMessageMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13))
etsysDiagnosticMessageMIB.setRevisions(('2003-01-10 21:17', '2002-06-07 14:28', '2001-12-03 19:51', '2001-08-08 00:00',))
if mibBuilder.loadTexts: etsysDiagnosticMessageMIB.setLastUpdated('200304252048Z')
if mibBuilder.loadTexts: etsysDiagnosticMessageMIB.setOrganization('Enterasys Networks')
class LongAdminString(TextualConvention, OctetString):
    reference = 'RFC2571 (An Architecture for Describing SNMP Management Frameworks)'
    status = 'current'
    displayHint = '1024a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

etsysDiagnosticMessage = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 1))
etsysDiagnosticMessageDetails = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 2))
etsysDiagnosticMessageCount = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysDiagnosticMessageCount.setStatus('current')
etsysDiagnosticMessageChanges = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysDiagnosticMessageChanges.setStatus('current')
etsysDiagnosticMessageTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 1, 3), )
if mibBuilder.loadTexts: etsysDiagnosticMessageTable.setStatus('current')
etsysDiagnosticMessageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 1, 3, 1), ).setIndexNames((0, "ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageIndex"))
if mibBuilder.loadTexts: etsysDiagnosticMessageEntry.setStatus('current')
etsysDiagnosticMessageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: etsysDiagnosticMessageIndex.setStatus('current')
etsysDiagnosticMessageTime = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 1, 3, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysDiagnosticMessageTime.setStatus('current')
etsysDiagnosticMessageType = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 1, 3, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysDiagnosticMessageType.setStatus('current')
etsysDiagnosticMessageSummary = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 1, 3, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysDiagnosticMessageSummary.setStatus('current')
etsysDiagnosticMessageFWRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 1, 3, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysDiagnosticMessageFWRevision.setStatus('current')
etsysDiagnosticMessageStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 1, 3, 1, 6), Bits().clone(namedValues=NamedValues(("etsysDiagnosticMessageBadChecksum", 0)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysDiagnosticMessageStatus.setStatus('current')
etsysDiagnosticMessageDetailsTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 2, 1), )
if mibBuilder.loadTexts: etsysDiagnosticMessageDetailsTable.setStatus('current')
etsysDiagnosticMessageDetailsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 2, 1, 1), ).setIndexNames((0, "ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageIndex"), (0, "ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageDetailsIndex"))
if mibBuilder.loadTexts: etsysDiagnosticMessageDetailsEntry.setStatus('current')
etsysDiagnosticMessageDetailsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024)))
if mibBuilder.loadTexts: etsysDiagnosticMessageDetailsIndex.setStatus('current')
etsysDiagnosticMessageDetailsText = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 2, 1, 1, 2), LongAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysDiagnosticMessageDetailsText.setStatus('current')
etsysDiagnosticMessageDetailsStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 2, 1, 1, 3), Bits().clone(namedValues=NamedValues(("etsysDiagnosticMessageLastSegment", 0)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysDiagnosticMessageDetailsStatus.setStatus('current')
etsysDiagnosticMessageConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 3))
etsysDiagnosticMessageGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 3, 1))
etsysDiagnosticMessageCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 3, 2))
etsysDiagnosticMessageGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 3, 1, 1)).setObjects(("ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageCount"), ("ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageChanges"), ("ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageTime"), ("ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageType"), ("ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageSummary"), ("ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageFWRevision"), ("ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageStatus"), ("ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageDetailsText"), ("ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageDetailsStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysDiagnosticMessageGroup = etsysDiagnosticMessageGroup.setStatus('current')
etsysDiagnosticMessageCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 3, 2, 1)).setObjects(("ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysDiagnosticMessageCompliance = etsysDiagnosticMessageCompliance.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", etsysDiagnosticMessage=etsysDiagnosticMessage, etsysDiagnosticMessageDetailsTable=etsysDiagnosticMessageDetailsTable, etsysDiagnosticMessageMIB=etsysDiagnosticMessageMIB, etsysDiagnosticMessageEntry=etsysDiagnosticMessageEntry, etsysDiagnosticMessageGroups=etsysDiagnosticMessageGroups, etsysDiagnosticMessageDetailsEntry=etsysDiagnosticMessageDetailsEntry, etsysDiagnosticMessageDetailsStatus=etsysDiagnosticMessageDetailsStatus, etsysDiagnosticMessageSummary=etsysDiagnosticMessageSummary, etsysDiagnosticMessageChanges=etsysDiagnosticMessageChanges, etsysDiagnosticMessageDetails=etsysDiagnosticMessageDetails, etsysDiagnosticMessageCount=etsysDiagnosticMessageCount, etsysDiagnosticMessageIndex=etsysDiagnosticMessageIndex, etsysDiagnosticMessageTable=etsysDiagnosticMessageTable, etsysDiagnosticMessageCompliance=etsysDiagnosticMessageCompliance, etsysDiagnosticMessageTime=etsysDiagnosticMessageTime, etsysDiagnosticMessageCompliances=etsysDiagnosticMessageCompliances, etsysDiagnosticMessageFWRevision=etsysDiagnosticMessageFWRevision, PYSNMP_MODULE_ID=etsysDiagnosticMessageMIB, etsysDiagnosticMessageDetailsText=etsysDiagnosticMessageDetailsText, etsysDiagnosticMessageType=etsysDiagnosticMessageType, etsysDiagnosticMessageDetailsIndex=etsysDiagnosticMessageDetailsIndex, etsysDiagnosticMessageStatus=etsysDiagnosticMessageStatus, etsysDiagnosticMessageGroup=etsysDiagnosticMessageGroup, LongAdminString=LongAdminString, etsysDiagnosticMessageConformance=etsysDiagnosticMessageConformance)
