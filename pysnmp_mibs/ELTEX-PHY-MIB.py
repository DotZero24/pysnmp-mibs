#
# PySNMP MIB module ELTEX-PHY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/eltex/ELTEX-PHY-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:11:46 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
eltexLtd, = mibBuilder.importSymbols("ELTEX-SMI-ACTUAL", "eltexLtd")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
eltexPhyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 52))
eltexPhyMIB.setRevisions(('2020-10-15 00:00', '2018-10-30 00:00',))
if mibBuilder.loadTexts: eltexPhyMIB.setLastUpdated('202010150000Z')
if mibBuilder.loadTexts: eltexPhyMIB.setOrganization('Eltex Enterprise Co, Ltd.')
class EltexPhyTransConnectorType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 32, 33, 34, 35, 127, 255))
    namedValues = NamedValues(("unknown", 0), ("sc", 1), ("fibre-ch-st1", 2), ("fibre-ch-st2", 3), ("bnc-tnc", 4), ("fibre-ch-coaxial-headers", 5), ("fibrejack", 6), ("lc", 7), ("mt-rj", 8), ("mu", 9), ("sg", 10), ("optical-pigtail", 11), ("mpo-parallel-optic", 12), ("hssdc-ii", 32), ("copper-pigtail", 33), ("rj45", 34), ("no-separable-connector", 35), ("unallocated", 127), ("vendorspec", 255))

class EltexPhyTransType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 127, 255))
    namedValues = NamedValues(("unknown", 0), ("gbic", 1), ("sff", 2), ("sfp-sfpplus", 3), ("xbi-300-pin", 4), ("xenpak", 5), ("xfp", 6), ("xff", 7), ("xfp-e", 8), ("xpak", 9), ("x2", 10), ("dwdm-sfp", 11), ("qsfp", 12), ("qsfpplus", 13), ("reserved", 127), ("vendorspec", 255))

class EltexPhyTransFiberDiameter(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 65535))
    namedValues = NamedValues(("fiber9", 1), ("fiber50", 2), ("fiber625", 3), ("copper", 4), ("unknown", 65535))

class EltexPhyTransDiagnosticType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("temperature", 1), ("supplyVoltage", 2), ("txBiasCurrent", 3), ("txOpticalPower", 4), ("rxOpticalPower", 5), ("lossOfSignal", 6))

class EltexPhyTestSetType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("cableStatus", 1))

class EltexPhyTestGetStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("none", 1), ("success", 2), ("inProgress", 3), ("notSupported", 4), ("unableToRun", 5), ("aborted", 6), ("failed", 7))

class EltexPhyTestGetUnits(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("integer", 1), ("boolean", 2), ("meter", 3))

class EltexPhyTestGetType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))
    namedValues = NamedValues(("channelAShort", 1), ("channelBShort", 2), ("channelCShort", 3), ("channelDShort", 4), ("channelAOpen", 5), ("channelBOpen", 6), ("channelCOpen", 7), ("channelDOpen", 8), ("channelAMismatch", 9), ("channelBMismatch", 10), ("channelCMismatch", 11), ("channelDMismatch", 12), ("channelALineDriver", 13), ("channelBLineDriver", 14), ("channelCLineDriver", 15), ("channelDLineDriver", 16), ("channelALength", 17), ("channelBLength", 18), ("channelCLength", 19), ("channelDLength", 20), ("channelACross", 21), ("channelBCross", 22), ("channelCCross", 23), ("channelDCross", 24))

eltexPhyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 52, 1))
eltexPhyTransceiverObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 52, 1, 1))
eltexPhyTestObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 52, 1, 2))
eltexPhyTransceiverGlobals = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 1))
eltexPhyTransceiverConfigs = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 2))
eltexPhyTransceiverStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3))
eltexPhyTestGlobals = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 52, 1, 2, 1))
eltexPhyTransceiverInfoTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3, 1), )
if mibBuilder.loadTexts: eltexPhyTransceiverInfoTable.setStatus('current')
eltexPhyTransceiverInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: eltexPhyTransceiverInfoEntry.setStatus('current')
eltexPhyTransceiverInfoConnectorType = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3, 1, 1, 1), EltexPhyTransConnectorType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexPhyTransceiverInfoConnectorType.setStatus('current')
eltexPhyTransceiverInfoType = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3, 1, 1, 2), EltexPhyTransType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexPhyTransceiverInfoType.setStatus('current')
eltexPhyTransceiverInfoComplianceCode = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexPhyTransceiverInfoComplianceCode.setStatus('current')
eltexPhyTransceiverInfoWaveLength = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexPhyTransceiverInfoWaveLength.setStatus('current')
eltexPhyTransceiverInfoVendorName = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3, 1, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexPhyTransceiverInfoVendorName.setStatus('current')
eltexPhyTransceiverInfoSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3, 1, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexPhyTransceiverInfoSerialNumber.setStatus('current')
eltexPhyTransceiverInfoFiberDiameter = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3, 1, 1, 7), EltexPhyTransFiberDiameter()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexPhyTransceiverInfoFiberDiameter.setStatus('current')
eltexPhyTransceiverInfoTransferDistance = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexPhyTransceiverInfoTransferDistance.setStatus('current')
eltexPhyTransceiverInfoDiagnosticSupported = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3, 1, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexPhyTransceiverInfoDiagnosticSupported.setStatus('current')
eltexPhyTransceiverInfoPartNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3, 1, 1, 10), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexPhyTransceiverInfoPartNumber.setStatus('current')
eltexPhyTransceiverInfoVendorRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3, 1, 1, 11), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexPhyTransceiverInfoVendorRevision.setStatus('current')
eltexPhyTransceiverDiagnosticTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3, 2), )
if mibBuilder.loadTexts: eltexPhyTransceiverDiagnosticTable.setStatus('current')
eltexPhyTransceiverDiagnosticEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ELTEX-PHY-MIB", "eltexPhyTransceiverDiagnosticType"), (0, "ELTEX-PHY-MIB", "eltexPhyTransceiverDiagnosticChannel"))
if mibBuilder.loadTexts: eltexPhyTransceiverDiagnosticEntry.setStatus('current')
eltexPhyTransceiverDiagnosticType = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3, 2, 1, 1), EltexPhyTransDiagnosticType())
if mibBuilder.loadTexts: eltexPhyTransceiverDiagnosticType.setStatus('current')
eltexPhyTransceiverDiagnosticChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4)))
if mibBuilder.loadTexts: eltexPhyTransceiverDiagnosticChannel.setStatus('current')
eltexPhyTransceiverDiagnosticUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexPhyTransceiverDiagnosticUnits.setStatus('current')
eltexPhyTransceiverDiagnosticHighAlarmThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexPhyTransceiverDiagnosticHighAlarmThreshold.setStatus('current')
eltexPhyTransceiverDiagnosticHighWarningThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexPhyTransceiverDiagnosticHighWarningThreshold.setStatus('current')
eltexPhyTransceiverDiagnosticLowWarningThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexPhyTransceiverDiagnosticLowWarningThreshold.setStatus('current')
eltexPhyTransceiverDiagnosticLowAlarmThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexPhyTransceiverDiagnosticLowAlarmThreshold.setStatus('current')
eltexPhyTransceiverDiagnosticCurrentValue = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 52, 1, 1, 3, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexPhyTransceiverDiagnosticCurrentValue.setStatus('current')
eltexPhyTestSetTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 52, 1, 2, 1, 1), )
if mibBuilder.loadTexts: eltexPhyTestSetTable.setStatus('current')
eltexPhyTestSetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 52, 1, 2, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: eltexPhyTestSetEntry.setStatus('current')
eltexPhyTestSetType = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 52, 1, 2, 1, 1, 1, 1), EltexPhyTestSetType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexPhyTestSetType.setStatus('current')
eltexPhyTestGetTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 52, 1, 2, 1, 2), )
if mibBuilder.loadTexts: eltexPhyTestGetTable.setStatus('current')
eltexPhyTestGetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 52, 1, 2, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ELTEX-PHY-MIB", "eltexPhyTestGetType"))
if mibBuilder.loadTexts: eltexPhyTestGetEntry.setStatus('current')
eltexPhyTestGetType = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 52, 1, 2, 1, 2, 1, 1), EltexPhyTestGetType())
if mibBuilder.loadTexts: eltexPhyTestGetType.setStatus('current')
eltexPhyTestGetStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 52, 1, 2, 1, 2, 1, 2), EltexPhyTestGetStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexPhyTestGetStatus.setStatus('current')
eltexPhyTestGetResult = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 52, 1, 2, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexPhyTestGetResult.setStatus('current')
eltexPhyTestGetUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 52, 1, 2, 1, 2, 1, 4), EltexPhyTestGetUnits()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexPhyTestGetUnits.setStatus('current')
eltexPhyTestGetTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 52, 1, 2, 1, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexPhyTestGetTimeStamp.setStatus('current')
mibBuilder.exportSymbols("ELTEX-PHY-MIB", eltexPhyTestObjects=eltexPhyTestObjects, eltexPhyTransceiverInfoWaveLength=eltexPhyTransceiverInfoWaveLength, eltexPhyTransceiverDiagnosticEntry=eltexPhyTransceiverDiagnosticEntry, eltexPhyTestGetUnits=eltexPhyTestGetUnits, eltexPhyTestGetTable=eltexPhyTestGetTable, EltexPhyTestGetStatus=EltexPhyTestGetStatus, eltexPhyTransceiverInfoEntry=eltexPhyTransceiverInfoEntry, eltexPhyTransceiverInfoDiagnosticSupported=eltexPhyTransceiverInfoDiagnosticSupported, eltexPhyTransceiverDiagnosticUnits=eltexPhyTransceiverDiagnosticUnits, eltexPhyObjects=eltexPhyObjects, eltexPhyTransceiverInfoType=eltexPhyTransceiverInfoType, eltexPhyTransceiverDiagnosticCurrentValue=eltexPhyTransceiverDiagnosticCurrentValue, eltexPhyTransceiverObjects=eltexPhyTransceiverObjects, eltexPhyTestGetTimeStamp=eltexPhyTestGetTimeStamp, eltexPhyTransceiverInfoVendorRevision=eltexPhyTransceiverInfoVendorRevision, EltexPhyTransType=EltexPhyTransType, eltexPhyTransceiverDiagnosticLowAlarmThreshold=eltexPhyTransceiverDiagnosticLowAlarmThreshold, eltexPhyTransceiverInfoVendorName=eltexPhyTransceiverInfoVendorName, eltexPhyTransceiverDiagnosticLowWarningThreshold=eltexPhyTransceiverDiagnosticLowWarningThreshold, eltexPhyTransceiverDiagnosticChannel=eltexPhyTransceiverDiagnosticChannel, eltexPhyTestGetType=eltexPhyTestGetType, eltexPhyTestGetResult=eltexPhyTestGetResult, EltexPhyTransFiberDiameter=EltexPhyTransFiberDiameter, eltexPhyTransceiverDiagnosticTable=eltexPhyTransceiverDiagnosticTable, EltexPhyTestGetType=EltexPhyTestGetType, eltexPhyTestGlobals=eltexPhyTestGlobals, eltexPhyTestSetType=eltexPhyTestSetType, EltexPhyTransConnectorType=EltexPhyTransConnectorType, eltexPhyTransceiverStatistics=eltexPhyTransceiverStatistics, eltexPhyTransceiverInfoTable=eltexPhyTransceiverInfoTable, eltexPhyTestGetEntry=eltexPhyTestGetEntry, eltexPhyTransceiverInfoSerialNumber=eltexPhyTransceiverInfoSerialNumber, eltexPhyTransceiverInfoPartNumber=eltexPhyTransceiverInfoPartNumber, eltexPhyTestSetTable=eltexPhyTestSetTable, eltexPhyMIB=eltexPhyMIB, eltexPhyTestGetStatus=eltexPhyTestGetStatus, eltexPhyTestSetEntry=eltexPhyTestSetEntry, eltexPhyTransceiverInfoFiberDiameter=eltexPhyTransceiverInfoFiberDiameter, EltexPhyTransDiagnosticType=EltexPhyTransDiagnosticType, eltexPhyTransceiverInfoConnectorType=eltexPhyTransceiverInfoConnectorType, EltexPhyTestGetUnits=EltexPhyTestGetUnits, eltexPhyTransceiverConfigs=eltexPhyTransceiverConfigs, eltexPhyTransceiverInfoTransferDistance=eltexPhyTransceiverInfoTransferDistance, eltexPhyTransceiverDiagnosticHighWarningThreshold=eltexPhyTransceiverDiagnosticHighWarningThreshold, eltexPhyTransceiverDiagnosticHighAlarmThreshold=eltexPhyTransceiverDiagnosticHighAlarmThreshold, EltexPhyTestSetType=EltexPhyTestSetType, eltexPhyTransceiverGlobals=eltexPhyTransceiverGlobals, PYSNMP_MODULE_ID=eltexPhyMIB, eltexPhyTransceiverDiagnosticType=eltexPhyTransceiverDiagnosticType, eltexPhyTransceiverInfoComplianceCode=eltexPhyTransceiverInfoComplianceCode)
