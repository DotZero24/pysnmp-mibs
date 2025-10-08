#
# PySNMP MIB module TN-RMD-CFM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/nokia/TN-RMD-CFM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:35:14 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
Dot1agCfmMepId, Dot1agCfmCcmInterval, Dot1agCfmMaintAssocNameType, Dot1agCfmMaintDomainName, Dot1agCfmMaintAssocName, Dot1agCfmMaintDomainNameType, Dot1agCfmMDLevel, VlanIdOrNone, Dot1agCfmMpDirection = mibBuilder.importSymbols("IEEE8021-CFM-MIB", "Dot1agCfmMepId", "Dot1agCfmCcmInterval", "Dot1agCfmMaintAssocNameType", "Dot1agCfmMaintDomainName", "Dot1agCfmMaintAssocName", "Dot1agCfmMaintDomainNameType", "Dot1agCfmMDLevel", "VlanIdOrNone", "Dot1agCfmMpDirection")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, MacAddress, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "MacAddress", "TruthValue", "DisplayString")
tnRmdSystemId, = mibBuilder.importSymbols("TN-RMD-SYSTEM-MIB", "tnRmdSystemId")
tnRmdObjs, tnRmdMIBModules = mibBuilder.importSymbols("TROPIC-GLOBAL-REG", "tnRmdObjs", "tnRmdMIBModules")
tnSysSwitchId, = mibBuilder.importSymbols("TROPIC-SYSTEM-MIB", "tnSysSwitchId")
tnRmdCfmMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 7483, 5, 1, 4, 1))
tnRmdCfmMibModule.setRevisions(('2020-11-13 12:00', '2020-11-06 12:00', '2020-10-09 12:00', '2018-02-23 12:00', '2016-11-16 00:00', '2012-11-28 00:00',))
if mibBuilder.loadTexts: tnRmdCfmMibModule.setLastUpdated('202011131200Z')
if mibBuilder.loadTexts: tnRmdCfmMibModule.setOrganization('Nokia')
tnRmdCfmObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1))
class TnRmdCfmDmInitiatorSessionMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("cfmDmInitiatorSessionModeNormal", 0), ("cfmDmInitiatorSessionModeTest", 1))

class TnRmdCfmDmTestMeasurementInterval(TextualConvention, Unsigned32):
    status = 'current'

class TnRmdCfmInitiatorSessionState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("cfmInitiatorSessionRunning", 0), ("cfmInitiatorSessionStopped", 1))

class TnRmdCfmInitiatorSessionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("cfmInitiatorSessionTypeOnDemand", 0), ("cfmInitiatorSessionTypeProActive", 1))

class TnRmdCfmMegId(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(48, 48)
    fixedLength = 48

class TnRmdCfmMepDefect(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("unl", 0), ("mmg", 1), ("unm", 2), ("loc", 3), ("rdi", 4), ("unp", 5), ("unpr", 6))

class TnRmdCfmMepNumber(TextualConvention, Unsigned32):
    status = 'current'

class TnRmdCfmMeasurementInterval(TextualConvention, Unsigned32):
    reference = '[MEF SOAM-PM] R56.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(3, 3600000)

class IEEE8021PriorityValue(TextualConvention, Unsigned32):
    reference = '12.13.3.3'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 7)

tnRmdCfmAttributeTotal = MibScalar((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnRmdCfmAttributeTotal.setStatus('current')
tnRmdSystemCfmTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 2), )
if mibBuilder.loadTexts: tnRmdSystemCfmTable.setStatus('current')
tnRmdSystemCfmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 2, 1), ).setIndexNames((0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"), (0, "TN-RMD-SYSTEM-MIB", "tnRmdSystemId"))
if mibBuilder.loadTexts: tnRmdSystemCfmEntry.setStatus('current')
tnRmdSystemCfmMaxNrMeps = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 2, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnRmdSystemCfmMaxNrMeps.setStatus('current')
tnRmdSystemCfmLmMaxNrPriorityLevels = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnRmdSystemCfmLmMaxNrPriorityLevels.setStatus('current')
tnRmdSystemCfmDmUpdateLocalTime = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 2, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnRmdSystemCfmDmUpdateLocalTime.setStatus('current')
tnRmdCfmMepTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3), )
if mibBuilder.loadTexts: tnRmdCfmMepTable.setStatus('current')
tnRmdCfmMepEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1), ).setIndexNames((0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"), (0, "TN-RMD-SYSTEM-MIB", "tnRmdSystemId"), (0, "TN-RMD-CFM-MIB", "tnRmdCfmMepNumber"))
if mibBuilder.loadTexts: tnRmdCfmMepEntry.setStatus('current')
tnRmdCfmMepNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 1), TnRmdCfmMepNumber())
if mibBuilder.loadTexts: tnRmdCfmMepNumber.setStatus('current')
tnRmdCfmMepMdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 2), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnRmdCfmMepMdIndex.setStatus('current')
tnRmdCfmMepMdFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 3), Dot1agCfmMaintDomainNameType().clone('charString')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnRmdCfmMepMdFormat.setStatus('current')
tnRmdCfmMepMdName = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 4), Dot1agCfmMaintDomainName().clone('DEFAULT')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnRmdCfmMepMdName.setStatus('current')
tnRmdCfmMepMaIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 5), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnRmdCfmMepMaIndex.setStatus('current')
tnRmdCfmMepMaNetFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 6), Dot1agCfmMaintAssocNameType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnRmdCfmMepMaNetFormat.setStatus('current')
tnRmdCfmMepMaNetName = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 7), Dot1agCfmMaintAssocName()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnRmdCfmMepMaNetName.setStatus('current')
tnRmdCfmMepMdLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 8), Dot1agCfmMDLevel()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnRmdCfmMepMdLevel.setStatus('current')
tnRmdCfmMepMegId = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 9), TnRmdCfmMegId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnRmdCfmMepMegId.setStatus('current')
tnRmdCfmMepDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 10), Dot1agCfmMpDirection()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnRmdCfmMepDirection.setStatus('current')
tnRmdCfmMepLocalId = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 11), Dot1agCfmMepId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnRmdCfmMepLocalId.setStatus('current')
tnRmdCfmMepEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 12), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnRmdCfmMepEnabled.setStatus('current')
tnRmdCfmMepCcmEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 13), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnRmdCfmMepCcmEnabled.setStatus('current')
tnRmdCfmMepLbrEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 14), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnRmdCfmMepLbrEnabled.setStatus('current')
tnRmdCfmMepCcmInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 15), Dot1agCfmCcmInterval()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnRmdCfmMepCcmInterval.setStatus('current')
tnRmdCfmMepIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 16), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnRmdCfmMepIfIndex.setStatus('current')
tnRmdCfmMepVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 17), VlanIdOrNone()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnRmdCfmMepVlanId.setStatus('current')
tnRmdCfmMepDefect = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 18), TnRmdCfmMepDefect()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnRmdCfmMepDefect.setStatus('current')
tnRmdCfmMepRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 19), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnRmdCfmMepRowStatus.setStatus('current')
tnRmdCfmMepEvcLoopbackEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 20), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnRmdCfmMepEvcLoopbackEnabled.setStatus('current')
tnRmdCfmRemoteMepTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 4), )
if mibBuilder.loadTexts: tnRmdCfmRemoteMepTable.setStatus('current')
tnRmdCfmRemoteMepEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 4, 1), ).setIndexNames((0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"), (0, "TN-RMD-SYSTEM-MIB", "tnRmdSystemId"), (0, "TN-RMD-CFM-MIB", "tnRmdCfmMepNumber"), (0, "TN-RMD-CFM-MIB", "tnRmdCfmRemoteMepId"))
if mibBuilder.loadTexts: tnRmdCfmRemoteMepEntry.setStatus('current')
tnRmdCfmRemoteMepId = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 4, 1, 1), Dot1agCfmMepId())
if mibBuilder.loadTexts: tnRmdCfmRemoteMepId.setStatus('current')
tnRmdCfmRemoteMepRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 4, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnRmdCfmRemoteMepRowStatus.setStatus('current')
tnRmdCfmMepDmTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 5), )
if mibBuilder.loadTexts: tnRmdCfmMepDmTable.setStatus('current')
tnRmdCfmMepDmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 5, 1), ).setIndexNames((0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"), (0, "TN-RMD-SYSTEM-MIB", "tnRmdSystemId"), (0, "TN-RMD-CFM-MIB", "tnRmdCfmMepNumber"))
if mibBuilder.loadTexts: tnRmdCfmMepDmEntry.setStatus('current')
tnRmdCfmMepDmResponder = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 5, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnRmdCfmMepDmResponder.setStatus('current')
tnRmdCfmMepDmInitiatorSessionTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 6), )
if mibBuilder.loadTexts: tnRmdCfmMepDmInitiatorSessionTable.setStatus('current')
tnRmdCfmMepDmInitiatorSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 6, 1), ).setIndexNames((0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"), (0, "TN-RMD-SYSTEM-MIB", "tnRmdSystemId"), (0, "TN-RMD-CFM-MIB", "tnRmdCfmMepNumber"), (0, "TN-RMD-CFM-MIB", "tnRmdCfmMepDmInitiatorSessionNumber"))
if mibBuilder.loadTexts: tnRmdCfmMepDmInitiatorSessionEntry.setStatus('current')
tnRmdCfmMepDmInitiatorSessionNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 6, 1, 1), Unsigned32())
if mibBuilder.loadTexts: tnRmdCfmMepDmInitiatorSessionNumber.setStatus('current')
tnRmdCfmMepDmInitiatorSessionType = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 6, 1, 2), TnRmdCfmInitiatorSessionType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnRmdCfmMepDmInitiatorSessionType.setStatus('current')
tnRmdCfmMepDmInitiatorSessionMode = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 6, 1, 3), TnRmdCfmDmInitiatorSessionMode()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnRmdCfmMepDmInitiatorSessionMode.setStatus('current')
tnRmdCfmMepDmInitiatorSessionInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 6, 1, 4), TnRmdCfmMeasurementInterval()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnRmdCfmMepDmInitiatorSessionInterval.setStatus('current')
tnRmdCfmMepDmInitiatorSessionTestInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 6, 1, 5), TnRmdCfmDmTestMeasurementInterval()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnRmdCfmMepDmInitiatorSessionTestInterval.setStatus('current')
tnRmdCfmMepDmInitiatorSessionPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 6, 1, 6), IEEE8021PriorityValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnRmdCfmMepDmInitiatorSessionPriority.setStatus('current')
tnRmdCfmMepDmInitiatorSessionDropEligible = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 6, 1, 7), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnRmdCfmMepDmInitiatorSessionDropEligible.setStatus('current')
tnRmdCfmMepDmInitiatorSessionDestMac = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 6, 1, 8), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnRmdCfmMepDmInitiatorSessionDestMac.setStatus('current')
tnRmdCfmMepDmInitiatorSessionInsertTestIdTlv = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 6, 1, 9), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnRmdCfmMepDmInitiatorSessionInsertTestIdTlv.setStatus('current')
tnRmdCfmMepDmInitiatorSessionTestId = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 6, 1, 10), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnRmdCfmMepDmInitiatorSessionTestId.setStatus('current')
tnRmdCfmMepDmInitiatorSessionFrameLength = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 6, 1, 11), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnRmdCfmMepDmInitiatorSessionFrameLength.setStatus('current')
tnRmdCfmMepDmInitiatorSessionState = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 6, 1, 12), TnRmdCfmInitiatorSessionState()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnRmdCfmMepDmInitiatorSessionState.setStatus('current')
tnRmdCfmMepDmInitiatorSessionRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 6, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnRmdCfmMepDmInitiatorSessionRowStatus.setStatus('current')
tnRmdCfmMepSlmTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 11), )
if mibBuilder.loadTexts: tnRmdCfmMepSlmTable.setStatus('current')
tnRmdCfmMepSlmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 11, 1), ).setIndexNames((0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"), (0, "TN-RMD-SYSTEM-MIB", "tnRmdSystemId"), (0, "TN-RMD-CFM-MIB", "tnRmdCfmMepNumber"))
if mibBuilder.loadTexts: tnRmdCfmMepSlmEntry.setStatus('current')
tnRmdCfmMepSlmResponder = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 11, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnRmdCfmMepSlmResponder.setStatus('current')
mibBuilder.exportSymbols("TN-RMD-CFM-MIB", tnRmdCfmMepDmInitiatorSessionRowStatus=tnRmdCfmMepDmInitiatorSessionRowStatus, tnRmdCfmMepMdName=tnRmdCfmMepMdName, tnRmdCfmMepMdLevel=tnRmdCfmMepMdLevel, tnRmdCfmObjects=tnRmdCfmObjects, TnRmdCfmMepNumber=TnRmdCfmMepNumber, tnRmdCfmMepDmInitiatorSessionNumber=tnRmdCfmMepDmInitiatorSessionNumber, tnRmdSystemCfmDmUpdateLocalTime=tnRmdSystemCfmDmUpdateLocalTime, tnRmdCfmMepDefect=tnRmdCfmMepDefect, tnRmdCfmRemoteMepTable=tnRmdCfmRemoteMepTable, tnRmdCfmMepCcmInterval=tnRmdCfmMepCcmInterval, tnRmdCfmMepDmInitiatorSessionEntry=tnRmdCfmMepDmInitiatorSessionEntry, tnRmdCfmMepDmInitiatorSessionFrameLength=tnRmdCfmMepDmInitiatorSessionFrameLength, tnRmdCfmMepDmInitiatorSessionTable=tnRmdCfmMepDmInitiatorSessionTable, TnRmdCfmMeasurementInterval=TnRmdCfmMeasurementInterval, tnRmdSystemCfmLmMaxNrPriorityLevels=tnRmdSystemCfmLmMaxNrPriorityLevels, tnRmdCfmMepLbrEnabled=tnRmdCfmMepLbrEnabled, tnRmdCfmMepDmInitiatorSessionType=tnRmdCfmMepDmInitiatorSessionType, tnRmdCfmMepDirection=tnRmdCfmMepDirection, tnRmdCfmAttributeTotal=tnRmdCfmAttributeTotal, IEEE8021PriorityValue=IEEE8021PriorityValue, tnRmdCfmMepMdFormat=tnRmdCfmMepMdFormat, tnRmdCfmMepMaIndex=tnRmdCfmMepMaIndex, tnRmdCfmMepVlanId=tnRmdCfmMepVlanId, tnRmdCfmMepDmInitiatorSessionDestMac=tnRmdCfmMepDmInitiatorSessionDestMac, tnRmdSystemCfmEntry=tnRmdSystemCfmEntry, TnRmdCfmMepDefect=TnRmdCfmMepDefect, TnRmdCfmInitiatorSessionState=TnRmdCfmInitiatorSessionState, tnRmdCfmMepDmInitiatorSessionMode=tnRmdCfmMepDmInitiatorSessionMode, tnRmdCfmMepDmInitiatorSessionPriority=tnRmdCfmMepDmInitiatorSessionPriority, tnRmdCfmMepSlmResponder=tnRmdCfmMepSlmResponder, TnRmdCfmInitiatorSessionType=TnRmdCfmInitiatorSessionType, TnRmdCfmDmTestMeasurementInterval=TnRmdCfmDmTestMeasurementInterval, tnRmdCfmMepDmInitiatorSessionTestId=tnRmdCfmMepDmInitiatorSessionTestId, tnRmdCfmMepLocalId=tnRmdCfmMepLocalId, tnRmdCfmRemoteMepRowStatus=tnRmdCfmRemoteMepRowStatus, tnRmdCfmMepIfIndex=tnRmdCfmMepIfIndex, tnRmdCfmMepDmEntry=tnRmdCfmMepDmEntry, tnRmdCfmMibModule=tnRmdCfmMibModule, tnRmdSystemCfmMaxNrMeps=tnRmdSystemCfmMaxNrMeps, tnRmdCfmMepMdIndex=tnRmdCfmMepMdIndex, tnRmdCfmMepTable=tnRmdCfmMepTable, tnRmdCfmMepCcmEnabled=tnRmdCfmMepCcmEnabled, tnRmdCfmMepEvcLoopbackEnabled=tnRmdCfmMepEvcLoopbackEnabled, tnRmdCfmMepDmTable=tnRmdCfmMepDmTable, tnRmdCfmMepDmInitiatorSessionDropEligible=tnRmdCfmMepDmInitiatorSessionDropEligible, PYSNMP_MODULE_ID=tnRmdCfmMibModule, tnRmdCfmMepSlmEntry=tnRmdCfmMepSlmEntry, TnRmdCfmDmInitiatorSessionMode=TnRmdCfmDmInitiatorSessionMode, tnRmdCfmMepEnabled=tnRmdCfmMepEnabled, tnRmdCfmMepNumber=tnRmdCfmMepNumber, tnRmdCfmMepRowStatus=tnRmdCfmMepRowStatus, tnRmdCfmRemoteMepId=tnRmdCfmRemoteMepId, tnRmdSystemCfmTable=tnRmdSystemCfmTable, tnRmdCfmMepSlmTable=tnRmdCfmMepSlmTable, tnRmdCfmRemoteMepEntry=tnRmdCfmRemoteMepEntry, tnRmdCfmMepDmInitiatorSessionState=tnRmdCfmMepDmInitiatorSessionState, tnRmdCfmMepMaNetFormat=tnRmdCfmMepMaNetFormat, TnRmdCfmMegId=TnRmdCfmMegId, tnRmdCfmMepDmInitiatorSessionTestInterval=tnRmdCfmMepDmInitiatorSessionTestInterval, tnRmdCfmMepMegId=tnRmdCfmMepMegId, tnRmdCfmMepDmInitiatorSessionInterval=tnRmdCfmMepDmInitiatorSessionInterval, tnRmdCfmMepEntry=tnRmdCfmMepEntry, tnRmdCfmMepMaNetName=tnRmdCfmMepMaNetName, tnRmdCfmMepDmInitiatorSessionInsertTestIdTlv=tnRmdCfmMepDmInitiatorSessionInsertTestIdTlv, tnRmdCfmMepDmResponder=tnRmdCfmMepDmResponder)
