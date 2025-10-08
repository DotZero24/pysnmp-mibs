#
# PySNMP MIB module OS-PTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/mrv/OS-PTP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:16:20 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
InetAddressPrefixLength, InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressPrefixLength", "InetAddressType", "InetAddress")
oaOptiSwitch, = mibBuilder.importSymbols("OS-COMMON-TC-MIB", "oaOptiSwitch")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
osPtpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6926, 2, 22))
osPtpMIB.setRevisions(('2012-08-08 00:00',))
if mibBuilder.loadTexts: osPtpMIB.setLastUpdated('201208080000Z')
if mibBuilder.loadTexts: osPtpMIB.setOrganization('MRV Communications, Inc.')
class ClockDomainType(TextualConvention, Unsigned32):
    reference = 'Section 7.1 Domains, Table 2 of [IEEE 1588-2008]'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class ClockIntervalBase2(TextualConvention, Integer32):
    reference = 'Section 7.7.2.1 General interval specification of [IEEE 1588-2008]'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-128, 127)

class ClockStateType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 0), ("freerun", 1), ("holdover", 2), ("acquiring", 3), ("frequencyLocked", 4), ("phaseAligned", 5))

class ClockTxModeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("unicast", 1), ("multicast", 2), ("multicastmix", 3))

osPtpMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 22, 0))
osPtpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 22, 1))
osPtpMIBInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 2))
osPtpMIBCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 3))
osPtpMIBEventParams = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 2, 1))
osPtpMIBSlaveInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 2, 2))
osPtpMIBSlaveCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 3, 2))
osPtpMIBSlaveCfgGen = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 3, 2, 1))
osPtpMIBSlaveCfgTbl = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 3, 2, 2))
osPtpMIBCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 22, 3))
osPtpMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 22, 100))
osPtpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 22, 100, 1))
osPtpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 22, 100, 2))
osPtpSlaveLastEvent = MibScalar((1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22))).clone(namedValues=NamedValues(("none", 0), ("inHoldover", 1), ("noCurrentMaster", 2), ("noClockInput", 3), ("noTimeOfDayInput", 4), ("toPSyncTimeNotTAI", 5), ("ptpPortNotOperational", 6), ("visibleMasterRefusedSyncGrantRequest", 7), ("visibleMasterIgnoredSyncGrantRequest", 8), ("visibleMasterRefusedDlyRespGrantRequest", 9), ("visibleMasterIgnoredDlyRespGrantRequest", 10), ("visibleMasterTooFewSyncMessages", 11), ("visibleMasterTooFewFollowUpMessages", 12), ("visibleMasterTooFewDelayResponseMessages", 13), ("accMasterRefusedAnnounceGrantRequest", 14), ("accMasterIgnoredAnnounceGrantRequest", 15), ("acceptableMasterTooFewAnnounceMessages", 16), ("currentMasterTooManySyncsWithoutFollowUp", 17), ("currentMasterTooManyFollowUpsWithoutSync", 18), ("currentMasterTooManyMissingDlyResponses", 19), ("m2SPacketDelayVaration", 20), ("s2MPacketDelayVaration", 21), ("toPSyncUTCOffsetUnknown", 22))).clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: osPtpSlaveLastEvent.setStatus('current')
osPtpSlaveEventReason = MibScalar((1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("alarmSet", 1), ("alarmClear", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: osPtpSlaveEventReason.setStatus('current')
osPtpSlaveEventDescription = MibScalar((1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 120))).setMaxAccess("readonly")
if mibBuilder.loadTexts: osPtpSlaveEventDescription.setStatus('current')
osPtpSlaveSupported = MibScalar((1, 3, 6, 1, 4, 1, 6926, 2, 22, 3, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: osPtpSlaveSupported.setStatus('current')
osPtpSlaveAddressTypesSupported = MibScalar((1, 3, 6, 1, 4, 1, 6926, 2, 22, 3, 2), Bits().clone(namedValues=NamedValues(("ipv4", 0), ("ipv6", 1), ("ipv4z", 2), ("ipv6z", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: osPtpSlaveAddressTypesSupported.setStatus('current')
osPtpSlaveNumOfDirectMasterRows = MibScalar((1, 3, 6, 1, 4, 1, 6926, 2, 22, 3, 3), Unsigned32()).setUnits('rows').setMaxAccess("readonly")
if mibBuilder.loadTexts: osPtpSlaveNumOfDirectMasterRows.setStatus('current')
osPtpSlaveAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("clear", 2), ("enabled", 3), ("disabled", 4))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osPtpSlaveAdminStatus.setStatus('current')
osPtpSlavePortVifName = MibScalar((1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 3, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osPtpSlavePortVifName.setStatus('current')
osPtpSlaveAddressType = MibScalar((1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 3, 2, 1, 3), InetAddressType().clone('ipv4')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osPtpSlaveAddressType.setStatus('current')
osPtpSlaveGatewayAddress = MibScalar((1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 3, 2, 1, 4), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osPtpSlaveGatewayAddress.setStatus('current')
osPtpSlavePortAddrPrefixLength = MibScalar((1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 3, 2, 1, 5), InetAddressPrefixLength().clone(24)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osPtpSlavePortAddrPrefixLength.setStatus('current')
osPtpSlavePortAddress = MibScalar((1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 3, 2, 1, 6), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osPtpSlavePortAddress.setStatus('current')
osPtpSlaveDelayRequestInterval = MibScalar((1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 3, 2, 1, 10), ClockIntervalBase2().clone(-5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osPtpSlaveDelayRequestInterval.setStatus('current')
osPtpSlaveAnnounceInterval = MibScalar((1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 3, 2, 1, 11), ClockIntervalBase2().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osPtpSlaveAnnounceInterval.setStatus('current')
osPtpSlaveSyncInterval = MibScalar((1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 3, 2, 1, 12), ClockIntervalBase2().clone(-5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osPtpSlaveSyncInterval.setStatus('current')
osPtpSlaveTodUartBaudRate = MibScalar((1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 3, 2, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unknown", 0), ("none", 1), ("baud1200", 2), ("baud2400", 3), ("baud4800", 4), ("baud9600", 5), ("baud19200", 6))).clone('baud4800')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osPtpSlaveTodUartBaudRate.setStatus('current')
osPtpSlavePortTxMode = MibScalar((1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 3, 2, 1, 21), ClockTxModeType().clone('unicast')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osPtpSlavePortTxMode.setStatus('current')
osPtpSlaveDirection = MibScalar((1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 3, 2, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("unknown", 0), ("both", 1), ("slaveToMaster", 2), ("masterToSlave", 3))).clone('both')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osPtpSlaveDirection.setStatus('current')
osPtpSlaveDomainIndex = MibScalar((1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 3, 2, 1, 23), ClockDomainType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osPtpSlaveDomainIndex.setStatus('current')
osPtpSlaveOutClkFrequency = MibScalar((1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 3, 2, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 170000), )).clone(8)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osPtpSlaveOutClkFrequency.setStatus('current')
osPtpSlaveDirectMasterOnly = MibScalar((1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 3, 2, 1, 30), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osPtpSlaveDirectMasterOnly.setStatus('current')
osPtpSlaveDirectMasterTable = MibTable((1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 3, 2, 2, 1), )
if mibBuilder.loadTexts: osPtpSlaveDirectMasterTable.setStatus('current')
osPtpSlaveDirectMasterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 3, 2, 2, 1, 1), ).setIndexNames((0, "OS-PTP-MIB", "osPtpSlaveDirectMasterId"))
if mibBuilder.loadTexts: osPtpSlaveDirectMasterEntry.setStatus('current')
osPtpSlaveDirectMasterId = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 3, 2, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: osPtpSlaveDirectMasterId.setStatus('current')
osPtpSlaveDirectMasterAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 3, 2, 2, 1, 1, 2), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osPtpSlaveDirectMasterAddress.setStatus('current')
osPtpMIBSlaveAlarm = NotificationType((1, 3, 6, 1, 4, 1, 6926, 2, 22, 0, 1)).setObjects(("OS-PTP-MIB", "osPtpSlaveLastEvent"), ("OS-PTP-MIB", "osPtpSlaveEventReason"), ("OS-PTP-MIB", "osPtpSlaveEventDescription"))
if mibBuilder.loadTexts: osPtpMIBSlaveAlarm.setStatus('current')
osPtpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6926, 2, 22, 100, 1, 1)).setObjects(("OS-PTP-MIB", "osPtpMibMandatoryGroup"), ("OS-PTP-MIB", "osPtpNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    osPtpMIBCompliance = osPtpMIBCompliance.setStatus('current')
osPtpMibMandatoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6926, 2, 22, 100, 2, 1)).setObjects(("OS-PTP-MIB", "osPtpSlaveLastEvent"), ("OS-PTP-MIB", "osPtpSlaveEventReason"), ("OS-PTP-MIB", "osPtpSlaveEventDescription"), ("OS-PTP-MIB", "osPtpSlaveSupported"), ("OS-PTP-MIB", "osPtpSlaveAddressTypesSupported"), ("OS-PTP-MIB", "osPtpSlaveNumOfDirectMasterRows"), ("OS-PTP-MIB", "osPtpSlaveAdminStatus"), ("OS-PTP-MIB", "osPtpSlavePortVifName"), ("OS-PTP-MIB", "osPtpSlaveGatewayAddress"), ("OS-PTP-MIB", "osPtpSlaveAddressType"), ("OS-PTP-MIB", "osPtpSlavePortAddrPrefixLength"), ("OS-PTP-MIB", "osPtpSlavePortAddress"), ("OS-PTP-MIB", "osPtpSlaveDirectMasterOnly"), ("OS-PTP-MIB", "osPtpSlaveDirectMasterAddress"), ("OS-PTP-MIB", "osPtpSlaveDelayRequestInterval"), ("OS-PTP-MIB", "osPtpSlaveAnnounceInterval"), ("OS-PTP-MIB", "osPtpSlaveSyncInterval"), ("OS-PTP-MIB", "osPtpSlaveTodUartBaudRate"), ("OS-PTP-MIB", "osPtpSlavePortTxMode"), ("OS-PTP-MIB", "osPtpSlaveDirection"), ("OS-PTP-MIB", "osPtpSlaveDomainIndex"), ("OS-PTP-MIB", "osPtpSlaveOutClkFrequency"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    osPtpMibMandatoryGroup = osPtpMibMandatoryGroup.setStatus('current')
osPtpNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6926, 2, 22, 100, 2, 2)).setObjects(("OS-PTP-MIB", "osPtpMIBSlaveAlarm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    osPtpNotificationsGroup = osPtpNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("OS-PTP-MIB", osPtpMIBEventParams=osPtpMIBEventParams, osPtpSlaveAddressType=osPtpSlaveAddressType, osPtpMIB=osPtpMIB, osPtpMIBInfo=osPtpMIBInfo, osPtpMIBConformance=osPtpMIBConformance, osPtpSlaveSyncInterval=osPtpSlaveSyncInterval, osPtpMIBCompliance=osPtpMIBCompliance, ClockDomainType=ClockDomainType, osPtpSlaveDirection=osPtpSlaveDirection, osPtpMIBObjects=osPtpMIBObjects, osPtpSlaveAdminStatus=osPtpSlaveAdminStatus, ClockStateType=ClockStateType, osPtpSlaveLastEvent=osPtpSlaveLastEvent, osPtpSlavePortAddress=osPtpSlavePortAddress, osPtpMIBCfg=osPtpMIBCfg, osPtpSlavePortTxMode=osPtpSlavePortTxMode, osPtpSlaveDirectMasterOnly=osPtpSlaveDirectMasterOnly, osPtpNotificationsGroup=osPtpNotificationsGroup, osPtpSlaveEventReason=osPtpSlaveEventReason, ClockTxModeType=ClockTxModeType, osPtpMIBSlaveCfgTbl=osPtpMIBSlaveCfgTbl, PYSNMP_MODULE_ID=osPtpMIB, osPtpSlavePortVifName=osPtpSlavePortVifName, osPtpMIBSlaveCfgGen=osPtpMIBSlaveCfgGen, osPtpSlaveDirectMasterEntry=osPtpSlaveDirectMasterEntry, osPtpSlaveEventDescription=osPtpSlaveEventDescription, osPtpMIBSlaveInfo=osPtpMIBSlaveInfo, osPtpSlaveSupported=osPtpSlaveSupported, osPtpSlaveDelayRequestInterval=osPtpSlaveDelayRequestInterval, osPtpSlaveTodUartBaudRate=osPtpSlaveTodUartBaudRate, osPtpSlaveDirectMasterId=osPtpSlaveDirectMasterId, ClockIntervalBase2=ClockIntervalBase2, osPtpSlaveNumOfDirectMasterRows=osPtpSlaveNumOfDirectMasterRows, osPtpSlaveAnnounceInterval=osPtpSlaveAnnounceInterval, osPtpMIBGroups=osPtpMIBGroups, osPtpMIBCompliances=osPtpMIBCompliances, osPtpSlaveAddressTypesSupported=osPtpSlaveAddressTypesSupported, osPtpSlaveDomainIndex=osPtpSlaveDomainIndex, osPtpSlaveDirectMasterAddress=osPtpSlaveDirectMasterAddress, osPtpSlaveOutClkFrequency=osPtpSlaveOutClkFrequency, osPtpMIBCapabilities=osPtpMIBCapabilities, osPtpMIBSlaveAlarm=osPtpMIBSlaveAlarm, osPtpSlavePortAddrPrefixLength=osPtpSlavePortAddrPrefixLength, osPtpSlaveDirectMasterTable=osPtpSlaveDirectMasterTable, osPtpMIBSlaveCfg=osPtpMIBSlaveCfg, osPtpMibMandatoryGroup=osPtpMibMandatoryGroup, osPtpMIBNotifications=osPtpMIBNotifications, osPtpSlaveGatewayAddress=osPtpSlaveGatewayAddress)
