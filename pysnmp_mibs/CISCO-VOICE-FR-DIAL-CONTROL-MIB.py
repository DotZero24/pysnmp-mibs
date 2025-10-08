#
# PySNMP MIB module CISCO-VOICE-FR-DIAL-CONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-VOICE-FR-DIAL-CONTROL-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:14:37 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
cCallHistoryIndex, = mibBuilder.importSymbols("CISCO-DIAL-CONTROL-MIB", "cCallHistoryIndex")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
CvcGUid, = mibBuilder.importSymbols("CISCO-VOICE-DIAL-CONTROL-MIB", "CvcGUid")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVoiceFrDialControlMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 36))
if mibBuilder.loadTexts: ciscoVoiceFrDialControlMIB.setLastUpdated('9804140000Z')
if mibBuilder.loadTexts: ciscoVoiceFrDialControlMIB.setOrganization('Cisco Systems, Inc.')
cvfrdcMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 36, 1))
cvFrCallHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 36, 1, 1))
cvFrCallHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 36, 1, 1, 1), )
if mibBuilder.loadTexts: cvFrCallHistoryTable.setStatus('current')
cvFrCallHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 36, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-DIAL-CONTROL-MIB", "cCallHistoryIndex"))
if mibBuilder.loadTexts: cvFrCallHistoryEntry.setStatus('current')
cvFrCallHistoryConnectionId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 36, 1, 1, 1, 1, 1), CvcGUid()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvFrCallHistoryConnectionId.setStatus('current')
cvFrCallHistoryDlci = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 36, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvFrCallHistoryDlci.setStatus('current')
cvFrCallHistoryLowerIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 36, 1, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvFrCallHistoryLowerIfName.setStatus('current')
cvFrCallHistorySessionTarget = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 36, 1, 1, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvFrCallHistorySessionTarget.setStatus('current')
cvfrdcMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 36, 3))
cvfrdcMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 36, 3, 1))
cvfrdcMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 36, 3, 2))
cvfrdcMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 36, 3, 1, 1)).setObjects(("CISCO-VOICE-FR-DIAL-CONTROL-MIB", "cvFrCallHistoryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvfrdcMIBCompliance = cvfrdcMIBCompliance.setStatus('current')
cvFrCallHistoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 36, 3, 2, 1)).setObjects(("CISCO-VOICE-FR-DIAL-CONTROL-MIB", "cvFrCallHistoryConnectionId"), ("CISCO-VOICE-FR-DIAL-CONTROL-MIB", "cvFrCallHistoryDlci"), ("CISCO-VOICE-FR-DIAL-CONTROL-MIB", "cvFrCallHistoryLowerIfName"), ("CISCO-VOICE-FR-DIAL-CONTROL-MIB", "cvFrCallHistorySessionTarget"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvFrCallHistoryGroup = cvFrCallHistoryGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VOICE-FR-DIAL-CONTROL-MIB", cvfrdcMIBCompliance=cvfrdcMIBCompliance, cvFrCallHistoryConnectionId=cvFrCallHistoryConnectionId, cvfrdcMIBCompliances=cvfrdcMIBCompliances, cvFrCallHistoryTable=cvFrCallHistoryTable, PYSNMP_MODULE_ID=ciscoVoiceFrDialControlMIB, cvfrdcMIBConformance=cvfrdcMIBConformance, cvfrdcMIBGroups=cvfrdcMIBGroups, cvFrCallHistory=cvFrCallHistory, cvfrdcMIBObjects=cvfrdcMIBObjects, ciscoVoiceFrDialControlMIB=ciscoVoiceFrDialControlMIB, cvFrCallHistoryDlci=cvFrCallHistoryDlci, cvFrCallHistorySessionTarget=cvFrCallHistorySessionTarget, cvFrCallHistoryLowerIfName=cvFrCallHistoryLowerIfName, cvFrCallHistoryEntry=cvFrCallHistoryEntry, cvFrCallHistoryGroup=cvFrCallHistoryGroup)
