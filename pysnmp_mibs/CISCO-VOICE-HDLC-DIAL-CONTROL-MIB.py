#
# PySNMP MIB module CISCO-VOICE-HDLC-DIAL-CONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-VOICE-HDLC-DIAL-CONTROL-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:13:04 2025
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
ciscoVoiceHdlcDialControlMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 37))
if mibBuilder.loadTexts: ciscoVoiceHdlcDialControlMIB.setLastUpdated('9804140000Z')
if mibBuilder.loadTexts: ciscoVoiceHdlcDialControlMIB.setOrganization('Cisco Systems, Inc.')
cvhdlcdcMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 37, 1))
cvHdlcCallHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 37, 1, 1))
cvHdlcCallHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 37, 1, 1, 1), )
if mibBuilder.loadTexts: cvHdlcCallHistoryTable.setStatus('current')
cvHdlcCallHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 37, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-DIAL-CONTROL-MIB", "cCallHistoryIndex"))
if mibBuilder.loadTexts: cvHdlcCallHistoryEntry.setStatus('current')
cvHdlcCallHistoryConnectionId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 37, 1, 1, 1, 1, 1), CvcGUid()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvHdlcCallHistoryConnectionId.setStatus('current')
cvHdlcCallHistoryLowerIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 37, 1, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvHdlcCallHistoryLowerIfName.setStatus('current')
cvHdlcCallHistorySessionTarget = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 37, 1, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvHdlcCallHistorySessionTarget.setStatus('current')
cvhdlcdcMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 37, 3))
cvhdlcdcMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 37, 3, 1))
cvhdlcdcMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 37, 3, 2))
cvhdlcdcMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 37, 3, 1, 1)).setObjects(("CISCO-VOICE-HDLC-DIAL-CONTROL-MIB", "cvHdlcCallHistoryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvhdlcdcMIBCompliance = cvhdlcdcMIBCompliance.setStatus('current')
cvHdlcCallHistoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 37, 3, 2, 1)).setObjects(("CISCO-VOICE-HDLC-DIAL-CONTROL-MIB", "cvHdlcCallHistoryConnectionId"), ("CISCO-VOICE-HDLC-DIAL-CONTROL-MIB", "cvHdlcCallHistoryLowerIfName"), ("CISCO-VOICE-HDLC-DIAL-CONTROL-MIB", "cvHdlcCallHistorySessionTarget"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvHdlcCallHistoryGroup = cvHdlcCallHistoryGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VOICE-HDLC-DIAL-CONTROL-MIB", PYSNMP_MODULE_ID=ciscoVoiceHdlcDialControlMIB, ciscoVoiceHdlcDialControlMIB=ciscoVoiceHdlcDialControlMIB, cvHdlcCallHistoryEntry=cvHdlcCallHistoryEntry, cvHdlcCallHistoryConnectionId=cvHdlcCallHistoryConnectionId, cvHdlcCallHistory=cvHdlcCallHistory, cvHdlcCallHistoryTable=cvHdlcCallHistoryTable, cvhdlcdcMIBObjects=cvhdlcdcMIBObjects, cvHdlcCallHistoryLowerIfName=cvHdlcCallHistoryLowerIfName, cvhdlcdcMIBConformance=cvhdlcdcMIBConformance, cvhdlcdcMIBGroups=cvhdlcdcMIBGroups, cvhdlcdcMIBCompliance=cvhdlcdcMIBCompliance, cvHdlcCallHistoryGroup=cvHdlcCallHistoryGroup, cvHdlcCallHistorySessionTarget=cvHdlcCallHistorySessionTarget, cvhdlcdcMIBCompliances=cvhdlcdcMIBCompliances)
