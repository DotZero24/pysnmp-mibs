#
# PySNMP MIB module ENTERASYS-DIAGNOSTIC-MESSAGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/enterasys/ENTERASYS-DIAGNOSTIC-MESSAGE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:17:33 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
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
mibBuilder.exportSymbols("ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", etsysDiagnosticMessageCount=etsysDiagnosticMessageCount, etsysDiagnosticMessageIndex=etsysDiagnosticMessageIndex, PYSNMP_MODULE_ID=etsysDiagnosticMessageMIB, LongAdminString=LongAdminString, etsysDiagnosticMessageEntry=etsysDiagnosticMessageEntry, etsysDiagnosticMessageSummary=etsysDiagnosticMessageSummary, etsysDiagnosticMessageConformance=etsysDiagnosticMessageConformance, etsysDiagnosticMessageDetailsStatus=etsysDiagnosticMessageDetailsStatus, etsysDiagnosticMessageDetailsEntry=etsysDiagnosticMessageDetailsEntry, etsysDiagnosticMessageType=etsysDiagnosticMessageType, etsysDiagnosticMessageGroups=etsysDiagnosticMessageGroups, etsysDiagnosticMessageTime=etsysDiagnosticMessageTime, etsysDiagnosticMessageDetailsTable=etsysDiagnosticMessageDetailsTable, etsysDiagnosticMessageStatus=etsysDiagnosticMessageStatus, etsysDiagnosticMessageChanges=etsysDiagnosticMessageChanges, etsysDiagnosticMessageCompliance=etsysDiagnosticMessageCompliance, etsysDiagnosticMessageDetails=etsysDiagnosticMessageDetails, etsysDiagnosticMessageDetailsText=etsysDiagnosticMessageDetailsText, etsysDiagnosticMessageFWRevision=etsysDiagnosticMessageFWRevision, etsysDiagnosticMessageTable=etsysDiagnosticMessageTable, etsysDiagnosticMessage=etsysDiagnosticMessage, etsysDiagnosticMessageDetailsIndex=etsysDiagnosticMessageDetailsIndex, etsysDiagnosticMessageCompliances=etsysDiagnosticMessageCompliances, etsysDiagnosticMessageMIB=etsysDiagnosticMessageMIB, etsysDiagnosticMessageGroup=etsysDiagnosticMessageGroup)
