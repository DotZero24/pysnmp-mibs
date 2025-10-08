#
# PySNMP MIB module CISCO-VOICE-LMR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-VOICE-LMR-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:29:49 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("CISCO-VOICE-LMR-MIB", cvlGuardToneAmp=cvlGuardToneAmp, cvlMIBObjects=cvlMIBObjects, cvlDigitalFilter=cvlDigitalFilter, LmrToneDuration=LmrToneDuration, cvlSignalToneDur=cvlSignalToneDur, cvlSignalToneIndex=cvlSignalToneIndex, cvlClassTable=cvlClassTable, cvlSignalToneGroupIndex=cvlSignalToneGroupIndex, VoiceAmplitude=VoiceAmplitude, PYSNMP_MODULE_ID=ciscoVoiceLmrMIB, cvlSignalToneEntry=cvlSignalToneEntry, cvlToneSignalGroup=cvlToneSignalGroup, VoiceFrequency=VoiceFrequency, cvlMIBConformance=cvlMIBConformance, cvlClassIndex=cvlClassIndex, cvlMIBCompliances=cvlMIBCompliances, cvlSignalToneAmp=cvlSignalToneAmp, ciscoVoiceLmrMIB=ciscoVoiceLmrMIB, cvlSignalToneFreq=cvlSignalToneFreq, cvlToneClassGroup=cvlToneClassGroup, cvlSignalToneTable=cvlSignalToneTable, cvlMIBGroups=cvlMIBGroups, cvlSignalToneName=cvlSignalToneName, cvlToneObjects=cvlToneObjects, cvlGuardToneFreq=cvlGuardToneFreq, cvlIdleToneFlag=cvlIdleToneFlag, cvlClassName=cvlClassName, cvlMIBCompliance=cvlMIBCompliance, cvlClassEntry=cvlClassEntry)
