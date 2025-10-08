#
# PySNMP MIB module CISCO-VOICE-HDLC-DIAL-CONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-VOICE-HDLC-DIAL-CONTROL-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:25:52 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
cCallHistoryIndex, = mibBuilder.importSymbols("CISCO-DIAL-CONTROL-MIB", "cCallHistoryIndex")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
CvcGUid, = mibBuilder.importSymbols("CISCO-VOICE-DIAL-CONTROL-MIB", "CvcGUid")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("CISCO-VOICE-HDLC-DIAL-CONTROL-MIB", cvhdlcdcMIBCompliance=cvhdlcdcMIBCompliance, PYSNMP_MODULE_ID=ciscoVoiceHdlcDialControlMIB, cvhdlcdcMIBCompliances=cvhdlcdcMIBCompliances, ciscoVoiceHdlcDialControlMIB=ciscoVoiceHdlcDialControlMIB, cvHdlcCallHistoryEntry=cvHdlcCallHistoryEntry, cvHdlcCallHistoryConnectionId=cvHdlcCallHistoryConnectionId, cvHdlcCallHistoryTable=cvHdlcCallHistoryTable, cvHdlcCallHistorySessionTarget=cvHdlcCallHistorySessionTarget, cvHdlcCallHistoryGroup=cvHdlcCallHistoryGroup, cvHdlcCallHistory=cvHdlcCallHistory, cvhdlcdcMIBGroups=cvhdlcdcMIBGroups, cvhdlcdcMIBConformance=cvhdlcdcMIBConformance, cvhdlcdcMIBObjects=cvhdlcdcMIBObjects, cvHdlcCallHistoryLowerIfName=cvHdlcCallHistoryLowerIfName)
