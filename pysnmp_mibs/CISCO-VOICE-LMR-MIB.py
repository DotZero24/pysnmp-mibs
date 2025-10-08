#
# PySNMP MIB module CISCO-VOICE-LMR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-VOICE-LMR-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:15:02 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ciscoVoiceLmrMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 510))
ciscoVoiceLmrMIB.setRevisions(('2004-10-14 00:00',))
if mibBuilder.loadTexts: ciscoVoiceLmrMIB.setLastUpdated('200410140000Z')
if mibBuilder.loadTexts: ciscoVoiceLmrMIB.setOrganization('Cisco Systems, Inc.')
cvlMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 510, 1))
cvlMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 510, 2))
cvlToneObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1))
class VoiceFrequency(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4000)

class VoiceAmplitude(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-30, 3)

class LmrToneDuration(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 500)

cvlClassTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 1), )
if mibBuilder.loadTexts: cvlClassTable.setStatus('current')
cvlClassEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-VOICE-LMR-MIB", "cvlClassIndex"))
if mibBuilder.loadTexts: cvlClassEntry.setStatus('current')
cvlClassIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000)))
if mibBuilder.loadTexts: cvlClassIndex.setStatus('current')
cvlClassName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 19))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvlClassName.setStatus('current')
cvlDigitalFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("digitalFilterNone", 0), ("digitalFilter1950HZ", 1), ("digitalFilter2175HZ", 2))).clone('digitalFilterNone')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvlDigitalFilter.setStatus('current')
cvlGuardToneFreq = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 1, 1, 4), VoiceFrequency()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvlGuardToneFreq.setStatus('current')
cvlGuardToneAmp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 1, 1, 5), VoiceAmplitude()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvlGuardToneAmp.setStatus('current')
cvlIdleToneFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 1, 1, 6), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvlIdleToneFlag.setStatus('current')
cvlSignalToneTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 2), )
if mibBuilder.loadTexts: cvlSignalToneTable.setStatus('current')
cvlSignalToneEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-VOICE-LMR-MIB", "cvlSignalToneGroupIndex"), (0, "CISCO-VOICE-LMR-MIB", "cvlSignalToneIndex"))
if mibBuilder.loadTexts: cvlSignalToneEntry.setStatus('current')
cvlSignalToneGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000)))
if mibBuilder.loadTexts: cvlSignalToneGroupIndex.setStatus('current')
cvlSignalToneIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)))
if mibBuilder.loadTexts: cvlSignalToneIndex.setStatus('current')
cvlSignalToneName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 2, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 19))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvlSignalToneName.setStatus('current')
cvlSignalToneFreq = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 2, 1, 4), VoiceFrequency()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvlSignalToneFreq.setStatus('current')
cvlSignalToneAmp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 2, 1, 5), VoiceAmplitude()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvlSignalToneAmp.setStatus('current')
cvlSignalToneDur = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 2, 1, 6), LmrToneDuration()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvlSignalToneDur.setStatus('current')
cvlMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 510, 2, 1))
cvlMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 510, 2, 2))
cvlMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 510, 2, 1, 1)).setObjects(("CISCO-VOICE-LMR-MIB", "cvlToneClassGroup"), ("CISCO-VOICE-LMR-MIB", "cvlToneSignalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvlMIBCompliance = cvlMIBCompliance.setStatus('current')
cvlToneClassGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 510, 2, 2, 1)).setObjects(("CISCO-VOICE-LMR-MIB", "cvlClassName"), ("CISCO-VOICE-LMR-MIB", "cvlDigitalFilter"), ("CISCO-VOICE-LMR-MIB", "cvlGuardToneFreq"), ("CISCO-VOICE-LMR-MIB", "cvlGuardToneAmp"), ("CISCO-VOICE-LMR-MIB", "cvlIdleToneFlag"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvlToneClassGroup = cvlToneClassGroup.setStatus('current')
cvlToneSignalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 510, 2, 2, 2)).setObjects(("CISCO-VOICE-LMR-MIB", "cvlSignalToneName"), ("CISCO-VOICE-LMR-MIB", "cvlSignalToneFreq"), ("CISCO-VOICE-LMR-MIB", "cvlSignalToneAmp"), ("CISCO-VOICE-LMR-MIB", "cvlSignalToneDur"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvlToneSignalGroup = cvlToneSignalGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VOICE-LMR-MIB", cvlClassEntry=cvlClassEntry, cvlClassName=cvlClassName, cvlSignalToneDur=cvlSignalToneDur, cvlSignalToneGroupIndex=cvlSignalToneGroupIndex, cvlGuardToneAmp=cvlGuardToneAmp, cvlToneSignalGroup=cvlToneSignalGroup, cvlSignalToneFreq=cvlSignalToneFreq, VoiceAmplitude=VoiceAmplitude, cvlToneObjects=cvlToneObjects, cvlToneClassGroup=cvlToneClassGroup, cvlMIBConformance=cvlMIBConformance, cvlMIBGroups=cvlMIBGroups, cvlSignalToneName=cvlSignalToneName, cvlSignalToneEntry=cvlSignalToneEntry, cvlSignalToneIndex=cvlSignalToneIndex, cvlClassIndex=cvlClassIndex, cvlSignalToneAmp=cvlSignalToneAmp, cvlMIBCompliance=cvlMIBCompliance, cvlGuardToneFreq=cvlGuardToneFreq, cvlClassTable=cvlClassTable, cvlSignalToneTable=cvlSignalToneTable, cvlMIBCompliances=cvlMIBCompliances, ciscoVoiceLmrMIB=ciscoVoiceLmrMIB, cvlDigitalFilter=cvlDigitalFilter, cvlIdleToneFlag=cvlIdleToneFlag, LmrToneDuration=LmrToneDuration, cvlMIBObjects=cvlMIBObjects, PYSNMP_MODULE_ID=ciscoVoiceLmrMIB, VoiceFrequency=VoiceFrequency)
