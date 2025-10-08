#
# PySNMP MIB module AOS-CORE-ALARM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/adva/AOS-CORE-ALARM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:02:59 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
aosCommon, = mibBuilder.importSymbols("ADVA-MIB", "aosCommon")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, RowPointer, TruthValue, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowPointer", "TruthValue", "TimeStamp", "DisplayString")
aosCoreAlarmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1))
aosCoreAlarmMIB.setRevisions(('2015-10-23 00:00',))
if mibBuilder.loadTexts: aosCoreAlarmMIB.setLastUpdated('201510230000Z')
if mibBuilder.loadTexts: aosCoreAlarmMIB.setOrganization('ADVA Optical Networking')
alarmObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 1))
alarmNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 2))
alarmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 3))
alarmNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 2, 0))
class ServiceEffect(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("nonServiceAffecting", 1), ("serviceAffecting", 2))

class NotificationCode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("critical", 1), ("major", 2), ("minor", 3), ("warning", 4), ("notAlarmed", 5), ("notReported", 6), ("clear", 7))

class Direction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("noDirection", 1), ("transmit", 2), ("receive", 3), ("biDirectional", 4))

class Location(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("nearEnd", 1), ("farEnd", 2), ("noLocation", 3))

class ConditionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 300, 301, 302, 303, 304, 305, 306, 307, 308, 400, 401, 410, 411, 412, 413, 414, 550, 551, 552, 553, 554, 555, 570, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 616, 617, 618, 619, 620, 621, 622), SingleValueConstraint(623, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 670, 680, 690, 1000, 1020, 1021, 1022, 1500, 1501, 1502, 1503))
    namedValues = NamedValues(("voltAnr", 1), ("removed", 2), ("fault", 3), ("mea", 4), ("incompatibleHardware", 5), ("meaApprove", 6), ("meaAccept", 7), ("meaCapability", 8), ("fwPackageMismatch", 9), ("fwReboot", 10), ("backplaneCommFail", 11), ("meaPhys", 12), ("meaDiffer", 13), ("psuRedundancyMismatch", 14), ("insufficientPower", 15), ("backplaneEepromCommFail", 16), ("powerFeedUndervoltage", 17), ("powerFeedAFail", 18), ("powerFeedBFail", 19), ("outPowerFail", 20), ("tcaOutCurrentHigh", 21), ("tcaPowerConsumptionHigh", 22), ("tcaTempHigh", 23), ("tcaTempLow", 24), ("lossOfSignal", 25), ("laserFail", 26), ("forceLaserOn", 27), ("forceTransmitShutdown", 28), ("lossOfClock", 29), ("lossOfOverhead", 30), ("lossOfPrbsPattern", 31), ("laserOnDelay", 32), ("autoPowerReduction", 33), ("supportingEqptFailure", 35), ("payloadMissingIndication", 36), ("lossOfSignalPayload", 37), ("tcaOptRcvPowerHigh", 38), ("tcaOptTrmtPowerHigh", 39), ("tcaOptLaserBiasCurrHigh", 40), ("laserTempHigh", 41), ("tcaOptRcvPowerLow", 42), ("tcaOptTrmtPowerLow", 43), ("laserTempLow", 44), ("alarmIndicatorSigDefect", 45), ("backwardDefectIndicator", 46), ("backwardDefectIndicatorPayload", 47), ("backwardDefectIndicatorOverhead", 48), ("clientSigFail", 49), ("degradedSig", 50), ("forwardDefectIndicatorPayload", 51), ("forwardDefectIndicatorOverhead", 52), ("incomingAlignError", 53), ("backwardIncomingAlignError", 54), ("lossOfFrame", 55), ("lossOfMultiframe", 56), ("lossOfFrameAndMultiframe", 57), ("lockedCondition", 58), ("lossOfTandemConn", 59), ("multiplexStructIdentifierMismatch", 60), ("openConnIndication", 61), ("payloadMismatch", 62), ("serverSigFail", 63), ("serverSigFailPayload", 64), ("serverSigFailOverhead", 65), ("trailSigFail", 66), ("trailSigFailPayload", 67), ("trailSigFailOverhead", 68), ("trailTraceIdentifierMismatch", 69), ("lossOfSignalOverhead", 70), ("pumpEndOfLife", 71), ("midstageLossHigh", 72), ("ampControlAbnormal", 73), ("autoPowerShutdown", 74), ("voaControlFail", 75), ("gainControlFail", 76), ("tiltControlFail", 77), ("optLimitHt", 78), ("optLimitHtEx", 79), ("oscLaserFail", 80), ("oscPower", 81), ("lossOfSigMidstage", 82), ("lossOfOpuMultiframeId", 83), ("tcaUnavailableSecondsHigh", 84), ("tcaErroredSecondHigh", 85), ("tcaSeverlyErroredSecondHigh", 86), ("tcaBackgroundBlockErrorsHigh", 87), ("tcaOscOptLaserBiasCurrHigh", 88), ("tcaOscLaserTempHigh", 89), ("tcaOscOptRcvPowerHigh", 90), ("tcaOscOptTrmtPowerHigh", 91), ("tcaSesPayloadHigh", 92), ("tcaSesOverheadHigh", 93), ("tcaUasPayloadHigh", 94), ("tcaUasOverheadHigh", 95), ("tcaOscLaserTempLow", 96), ("tcaOscOptRcvPowerLow", 97), ("tcaOscOptTrmtPowerLow", 98), ("lossOfModemSync", 99), ("lossOfCouplingAlignment", 100), ("autoCdcFail", 101), ("tcaDiffGroupDelayHigh", 102), ("tcaCdcHigh", 103), ("tcaCarrierFreqOffsetHigh", 104), ("tcaSnrLow", 105), ("tcaCdcLow", 106), ("tcaCarrierFreqOffsetLow", 107), ("lnkFail", 108), ("lnkCblFault", 109), ("lnkCblRmv", 110), ("lnkAutonegFail", 111), ("lnkNoRootCause", 112), ("fendDupModeUnknown", 113), ("jabThldExceed", 114), ("lossOfSync", 115), ("rxLocalFault", 116), ("txLocalFault", 117), ("lossOfBlockLock", 118), ("hiBer", 119), ("autoCdcInProgress", 120), ("lossOfBlockLockLane", 121), ("lossOfLaneAlgnMarkLane", 122), ("lnkDownDeact", 123), ("negBwExceed", 124), ("rxSsf", 125), ("txSsf", 126), ("outputOvercurrent", 127), ("tcaOutputPowerHigh", 128), ("lossOfAlignment", 129), ("ntpServerUnavailable", 130), ("tunedFrequencyMismatch", 131), ("temperatureHigh", 133), ("temperatureLow", 134), ("manifestMismatch", 135), ("manifestIncomplete", 136), ("laserBiasCurrentAbnormal", 137), ("lossOfTrafficAfterFirmwareActivation", 138), ("softwareVersionMismatch", 139), ("fanFault", 140), ("portConfigMismatch", 141), ("licenseServerDisconnect", 142), ("hwResourceUnavailableRecoverable", 143), ("licenseInvalid", 144), ("ssdWearoutLevelWarning", 145), ("licenseExpire", 146), ("databaseMismatch", 147), ("licenseMissing", 148), ("licenseOverdraft", 149), ("cryptoPasswordMissing", 150), ("vmResumeFailed", 151), ("keyExchangeAuthMissing", 152), ("keyLifetimeExpired", 153), ("tamperDetected", 154), ("selfTestFailed", 155), ("cryptoTemporaryLockout", 156), ("batteryLow", 157), ("selfTestInProgress", 158), ("vmCrashed", 159), ("keyExchangeDegrade", 160), ("internalEncryptionFailed", 161), ("keyExchangeInProgress", 162), ("keyExchangeChannelFail", 163), ("terminalLoopbackInProgress", 164), ("localOscBiarCurAbnormal", 165), ("licenseFileMissing", 166), ("licenseServerConfigMissing", 167), ("hardwareBusy", 168), ("fanFilterReplace", 169), ("rebootInProgress", 170), ("prbsDetectionInProgress", 171), ("tcaOutOfFrameSecondHigh", 172), ("msLineAis", 173), ("localOscTemperatureLow", 174), ("localOscTemperatureHigh", 175), ("facilityLoopbackInProgress", 176), ("prbsGenerationInProgress", 177), ("transmitSignalFail", 178), ("loopbackActive", 179), ("meaPhyChanged", 180), ("licenseBackupServerDisconnect", 181), ("callHomeServerUnreachable", 182), ("timinglicensemissing", 183), ("eomplslicensemissing", 184), ("fullcapacitylicensemissing", 185), ("elephantflowlicensemissing", 186), ("snmpdyinggasp", 187), ("snmpdyinggasphostresourcesbusy", 188), ("snmpdyinggasphostunreachable", 189), ("controlplanelicensemissing", 190), ("l3licensemissing", 191), ("coldrebootrequired", 192), ("efmRemoteDyingGasp", 227), ("efmFail", 228), ("efmRemoteCriticalEvent", 229), ("efmRemoteLinkDown", 230), ("efmRemoteLoopbackFail", 231), ("efmRemoteLoopbackRequest", 232), ("tcaQFactorLow", 233), ("tcaPolarizationDependentLHigh", 234), ("tcaStateOfPolarizationChangeRateHigh", 235), ("tcaOpticalSnrLow", 236), ("srvDiscarded", 300), ("bwExceedPortSpeed", 301), ("meaPortalAddress", 302), ("meaPortalPri", 303), ("meaThreePortal", 304), ("meaPortalSysNumber", 305), ("meaActorAdminKey", 306), ("meaPortDigest", 307), ("meaGatewayDigest", 308), ("ztpInProgress", 400), ("ztpFailed", 401), ("cryptoConfigMismatch", 410), ("keyExchangeConfigMismatch", 411), ("fingerprintAuthMissing", 412), ("cryptoConfigError", 413), ("keyExchangeAuthMismatch", 414), ("crossConnectCCM", 550), ("errorCCM", 551), ("someRemoteMEPCCM", 552), ("someMACstatus", 553), ("someRDI", 554), ("ethAIS", 555), ("remoteInitSAT", 570), ("erpFoPPM", 580), ("erpFoPTO", 581), ("erpBlockPort0RPL", 582), ("erpBlockPort0SF", 583), ("erpBlockPort0MS", 584), ("erpBlockPort0FS", 585), ("erpBlockPort0WTR", 586), ("erpBlockPort1RPL", 587), ("erpBlockPort1SF", 588), ("erpBlockPort1MS", 589), ("erpBlockPort1FS", 590), ("erpBlockPort1WTR", 591), ("avgHoldoverNotReady", 600), ("freerun", 601), ("fastAccquisition", 602), ("holdover", 603), ("lossOfLock", 604), ("allSyncRefFail", 605), ("syncRefLockOut", 606), ("syncRefFS", 607), ("syncRefMS", 608), ("syncRefWTR", 609), ("syncRefSW", 610), ("syncRefFail", 611), ("syncRefFreqOffset", 612), ("ais", 616), ("bitsLossOfFrame", 617), ("qlMismatch", 618), ("qlInvalid", 619), ("esmcFail", 620), ("linkdownMasterSlaveCfg", 621), ("autoNegoMasterSlaveCfg", 622)) + NamedValues(("squelched", 623), ("ptpFreerun", 650), ("ptpTimeFreeRun", 651), ("ptpFreqHoldover", 652), ("ptpTimeHoldover", 653), ("ptpFreqNotTraceable", 654), ("ptpTimeNotTraceable", 655), ("ptpAnnounceTimeout", 656), ("ptpSyncTimeout", 657), ("ptpDelayrespTimeout", 658), ("ptpMultiplePeers", 659), ("ptpWrongDomain", 660), ("ptpNoTrafficFP", 661), ("bgpNbrLinkDown", 670), ("paAuthFail", 680), ("noMGroupRes", 690), ("eomplsDstUnresovled", 1000), ("trafficArpTableFull", 1020), ("noRouteResources", 1021), ("ipAddressConflict", 1022), ("ntpLossOfServer", 1500), ("remoteServerUnreachable", 1501), ("sysLogServerUnreachable", 1502), ("targetAddressUnreachable", 1503))

class ConditionDescr(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 64)

class ConditionEntityTranslation(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

aosCoreAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 1, 1), )
if mibBuilder.loadTexts: aosCoreAlarmTable.setStatus('current')
aosCoreAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 1, 1, 1), ).setIndexNames((0, "AOS-CORE-ALARM-MIB", "aosCoreAlarmIndex"))
if mibBuilder.loadTexts: aosCoreAlarmEntry.setStatus('current')
aosCoreAlarmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 1, 1, 1, 1), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: aosCoreAlarmIndex.setStatus('current')
aosCoreAlarmConditionType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 1, 1, 1, 2), ConditionType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aosCoreAlarmConditionType.setStatus('current')
aosCoreAlarmEntityTranslation = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 1, 1, 1, 3), ConditionEntityTranslation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aosCoreAlarmEntityTranslation.setStatus('current')
aosCoreAlarmEntity = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 1, 1, 1, 4), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aosCoreAlarmEntity.setStatus('current')
aosCoreAlarmCondDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 1, 1, 1, 5), ConditionDescr()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aosCoreAlarmCondDescr.setStatus('current')
aosCoreAlarmTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 1, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aosCoreAlarmTimestamp.setStatus('current')
aosCoreAlarmDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 1, 1, 1, 7), Direction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aosCoreAlarmDirection.setStatus('current')
aosCoreAlarmLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 1, 1, 1, 8), Location()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aosCoreAlarmLocation.setStatus('current')
aosCoreAlarmSrvEff = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 1, 1, 1, 9), ServiceEffect()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aosCoreAlarmSrvEff.setStatus('current')
aosCoreAlarmNotifCode = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 1, 1, 1, 10), NotificationCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aosCoreAlarmNotifCode.setStatus('current')
aosCoreAlarmNotifTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 1, 1, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aosCoreAlarmNotifTimestamp.setStatus('current')
aosCoreAlarmAdditionalInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 1, 1, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aosCoreAlarmAdditionalInfo.setStatus('current')
aosCoreAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 2, 0, 1)).setObjects(("AOS-CORE-ALARM-MIB", "aosCoreAlarmIndex"), ("AOS-CORE-ALARM-MIB", "aosCoreAlarmConditionType"), ("AOS-CORE-ALARM-MIB", "aosCoreAlarmEntityTranslation"), ("AOS-CORE-ALARM-MIB", "aosCoreAlarmEntity"), ("AOS-CORE-ALARM-MIB", "aosCoreAlarmCondDescr"), ("AOS-CORE-ALARM-MIB", "aosCoreAlarmTimestamp"), ("AOS-CORE-ALARM-MIB", "aosCoreAlarmDirection"), ("AOS-CORE-ALARM-MIB", "aosCoreAlarmLocation"), ("AOS-CORE-ALARM-MIB", "aosCoreAlarmSrvEff"), ("AOS-CORE-ALARM-MIB", "aosCoreAlarmNotifCode"), ("AOS-CORE-ALARM-MIB", "aosCoreAlarmNotifTimestamp"), ("AOS-CORE-ALARM-MIB", "aosCoreAlarmAdditionalInfo"))
if mibBuilder.loadTexts: aosCoreAlarmTrap.setStatus('current')
aosCoreAlarmCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 3, 1))
aosCoreAlarmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 3, 2))
aosCoreAlarmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 3, 1, 1)).setObjects(("AOS-CORE-ALARM-MIB", "aosCoreAlarmObjectGroup"), ("AOS-CORE-ALARM-MIB", "aosCoreAlarmNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aosCoreAlarmCompliance = aosCoreAlarmCompliance.setStatus('current')
aosCoreAlarmObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 3, 2, 1)).setObjects(("AOS-CORE-ALARM-MIB", "aosCoreAlarmIndex"), ("AOS-CORE-ALARM-MIB", "aosCoreAlarmConditionType"), ("AOS-CORE-ALARM-MIB", "aosCoreAlarmEntityTranslation"), ("AOS-CORE-ALARM-MIB", "aosCoreAlarmEntity"), ("AOS-CORE-ALARM-MIB", "aosCoreAlarmCondDescr"), ("AOS-CORE-ALARM-MIB", "aosCoreAlarmTimestamp"), ("AOS-CORE-ALARM-MIB", "aosCoreAlarmDirection"), ("AOS-CORE-ALARM-MIB", "aosCoreAlarmLocation"), ("AOS-CORE-ALARM-MIB", "aosCoreAlarmSrvEff"), ("AOS-CORE-ALARM-MIB", "aosCoreAlarmNotifCode"), ("AOS-CORE-ALARM-MIB", "aosCoreAlarmNotifTimestamp"), ("AOS-CORE-ALARM-MIB", "aosCoreAlarmAdditionalInfo"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aosCoreAlarmObjectGroup = aosCoreAlarmObjectGroup.setStatus('current')
aosCoreAlarmNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 3, 2, 2)).setObjects(("AOS-CORE-ALARM-MIB", "aosCoreAlarmTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aosCoreAlarmNotifGroup = aosCoreAlarmNotifGroup.setStatus('current')
mibBuilder.exportSymbols("AOS-CORE-ALARM-MIB", ServiceEffect=ServiceEffect, aosCoreAlarmCompliance=aosCoreAlarmCompliance, aosCoreAlarmEntry=aosCoreAlarmEntry, aosCoreAlarmTimestamp=aosCoreAlarmTimestamp, PYSNMP_MODULE_ID=aosCoreAlarmMIB, aosCoreAlarmObjectGroup=aosCoreAlarmObjectGroup, aosCoreAlarmConditionType=aosCoreAlarmConditionType, aosCoreAlarmCompliances=aosCoreAlarmCompliances, NotificationCode=NotificationCode, alarmNotifications=alarmNotifications, aosCoreAlarmEntity=aosCoreAlarmEntity, aosCoreAlarmTrap=aosCoreAlarmTrap, aosCoreAlarmDirection=aosCoreAlarmDirection, aosCoreAlarmNotifCode=aosCoreAlarmNotifCode, Direction=Direction, aosCoreAlarmGroups=aosCoreAlarmGroups, alarmConformance=alarmConformance, aosCoreAlarmNotifGroup=aosCoreAlarmNotifGroup, alarmObjects=alarmObjects, ConditionType=ConditionType, aosCoreAlarmIndex=aosCoreAlarmIndex, aosCoreAlarmSrvEff=aosCoreAlarmSrvEff, alarmNotificationsPrefix=alarmNotificationsPrefix, aosCoreAlarmAdditionalInfo=aosCoreAlarmAdditionalInfo, aosCoreAlarmMIB=aosCoreAlarmMIB, aosCoreAlarmEntityTranslation=aosCoreAlarmEntityTranslation, ConditionDescr=ConditionDescr, aosCoreAlarmLocation=aosCoreAlarmLocation, aosCoreAlarmNotifTimestamp=aosCoreAlarmNotifTimestamp, ConditionEntityTranslation=ConditionEntityTranslation, aosCoreAlarmTable=aosCoreAlarmTable, Location=Location, aosCoreAlarmCondDescr=aosCoreAlarmCondDescr)
