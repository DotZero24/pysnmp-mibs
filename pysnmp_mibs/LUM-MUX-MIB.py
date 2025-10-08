#
# PySNMP MIB module LUM-MUX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/LUM-MUX-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:51 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
lumModules, lumMuxMIB = mibBuilder.importSymbols("LUM-REG", "lumModules", "lumMuxMIB")
SlotNumber, BoardOrInterfaceAdminStatus, BoardOrInterfaceOperStatus, ObjectProperty, LambdaFrequency, MgmtNameString, PortNumber, SubrackNumber, FaultStatus = mibBuilder.importSymbols("LUM-TC", "SlotNumber", "BoardOrInterfaceAdminStatus", "BoardOrInterfaceOperStatus", "ObjectProperty", "LambdaFrequency", "MgmtNameString", "PortNumber", "SubrackNumber", "FaultStatus")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
lumMuxMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 8708, 1, 1, 14))
lumMuxMIBModule.setRevisions(('2017-06-15 00:00', '2016-01-11 00:00', '2011-04-12 00:00', '2007-11-12 00:00', '2003-01-29 00:00', '2002-12-04 00:00', '2002-10-29 00:00', '2002-10-01 00:00', '2002-04-03 00:00', '2002-01-17 00:00', '2001-12-03 00:00', '2001-11-09 00:00', '2001-10-30 00:00',))
if mibBuilder.loadTexts: lumMuxMIBModule.setLastUpdated('201706150000Z')
if mibBuilder.loadTexts: lumMuxMIBModule.setOrganization('Infinera Corporation')
lumMuxConfs = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 13, 1))
lumMuxGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 1))
lumMuxCompl = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 2))
lumMuxMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2))
muxGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 1))
muxIfList = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2))
muxVc4List = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3))
class MuxTxDirection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("toWest", 1), ("toEast", 2))

muxGeneralLastChangeTime = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxGeneralLastChangeTime.setStatus('current')
muxGeneralStateLastChangeTime = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxGeneralStateLastChangeTime.setStatus('current')
muxGeneralMuxIfTableSize = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxGeneralMuxIfTableSize.setStatus('current')
muxGeneralMuxVc4TableSize = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxGeneralMuxVc4TableSize.setStatus('current')
muxIfTable = MibTable((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1), )
if mibBuilder.loadTexts: muxIfTable.setStatus('current')
muxIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1), ).setIndexNames((0, "LUM-MUX-MIB", "muxIfIndex"))
if mibBuilder.loadTexts: muxIfEntry.setStatus('current')
muxIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxIfIndex.setStatus('current')
muxIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 2), MgmtNameString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxIfName.setStatus('current')
muxIfDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: muxIfDescr.setStatus('current')
muxIfSubrack = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 4), SubrackNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxIfSubrack.setStatus('current')
muxIfSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 5), SlotNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxIfSlot.setStatus('current')
muxIfTxPort = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 6), PortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxIfTxPort.setStatus('current')
muxIfRxPort = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 7), PortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxIfRxPort.setStatus('current')
muxIfInvPhysIndexOrZero = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxIfInvPhysIndexOrZero.setStatus('current')
muxIfPowerLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxIfPowerLevel.setStatus('current')
muxIfPowerLevelHighThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-200, -10)).clone(-50)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: muxIfPowerLevelHighThreshold.setStatus('current')
muxIfPowerLevelLowThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-200, -10)).clone(-160)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: muxIfPowerLevelLowThreshold.setStatus('current')
muxIfAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 12), BoardOrInterfaceAdminStatus().clone('up')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: muxIfAdminStatus.setStatus('current')
muxIfOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 13), BoardOrInterfaceOperStatus().clone('notPresent')).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxIfOperStatus.setStatus('current')
muxIfLossOfSignal = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 14), FaultStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxIfLossOfSignal.setStatus('current')
muxIfReceivedPowerHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 15), FaultStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxIfReceivedPowerHigh.setStatus('current')
muxIfReceivedPowerLow = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 16), FaultStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxIfReceivedPowerLow.setStatus('current')
muxIfBitrateMismatch = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 17), FaultStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxIfBitrateMismatch.setStatus('current')
muxIfLaserBias = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 18), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxIfLaserBias.setStatus('current')
muxIfLaserBiasThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 19), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 300)).clone(200)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: muxIfLaserBiasThreshold.setStatus('current')
muxIfJ0PathTrace = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 20), OctetString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(1, 1), ValueSizeConstraint(16, 16), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxIfJ0PathTrace.setStatus('deprecated')
muxIfAlarmIndicationSignal = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 21), FaultStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxIfAlarmIndicationSignal.setStatus('current')
muxIfLossOfFrame = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 22), FaultStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxIfLossOfFrame.setStatus('current')
muxIfLaserStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxIfLaserStatus.setStatus('current')
muxIfTxDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 24), MuxTxDirection()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: muxIfTxDirection.setStatus('current')
muxIfExpectedTxLambda = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 25), LambdaFrequency()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: muxIfExpectedTxLambda.setStatus('current')
muxIfTxLambda = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 26), LambdaFrequency()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxIfTxLambda.setStatus('current')
muxIfTraceIntrusionMode = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxIfTraceIntrusionMode.setStatus('current')
muxIfTraceTransmitted = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 28), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: muxIfTraceTransmitted.setStatus('current')
muxIfTraceReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 29), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxIfTraceReceived.setStatus('current')
muxIfTraceExpected = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 30), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: muxIfTraceExpected.setStatus('current')
muxIfTraceAlarmMode = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 31), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: muxIfTraceAlarmMode.setStatus('current')
muxIfTraceMismatch = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 32), FaultStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxIfTraceMismatch.setStatus('current')
muxIfOHTransparency = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 33), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2))).clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: muxIfOHTransparency.setStatus('current')
muxIfSuppressRemoteAlarms = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 34), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: muxIfSuppressRemoteAlarms.setStatus('current')
muxIfHighSpeedMin = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 35), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxIfHighSpeedMin.setStatus('current')
muxIfHighSpeedMax = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 36), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxIfHighSpeedMax.setStatus('current')
muxIfTrxCodeMismatch = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 37), FaultStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxIfTrxCodeMismatch.setStatus('current')
muxIfTrxBitrateUnavailable = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 38), FaultStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxIfTrxBitrateUnavailable.setStatus('current')
muxIfTrxMissing = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 39), FaultStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxIfTrxMissing.setStatus('current')
muxIfTrxClass = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 40), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxIfTrxClass.setStatus('current')
muxIfTransmitterFailed = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 41), FaultStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxIfTransmitterFailed.setStatus('current')
muxIfUnexpectedFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 42), FaultStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxIfUnexpectedFrequency.setStatus('current')
muxIfIllegalFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 43), FaultStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxIfIllegalFrequency.setStatus('current')
muxIfReceiverSensitivity = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 44), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxIfReceiverSensitivity.setStatus('current')
muxIfPowerLevelLowRelativeThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 45), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-50, 100)).clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: muxIfPowerLevelLowRelativeThreshold.setStatus('current')
muxIfObjectProperty = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 46), ObjectProperty()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxIfObjectProperty.setStatus('current')
muxIfTxPowerLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 47), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxIfTxPowerLevel.setStatus('current')
muxIfLaserTempActual = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 2, 1, 1, 48), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxIfLaserTempActual.setStatus('current')
muxVc4Table = MibTable((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1), )
if mibBuilder.loadTexts: muxVc4Table.setStatus('current')
muxVc4Entry = MibTableRow((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1, 1), ).setIndexNames((0, "LUM-MUX-MIB", "muxVc4Index"))
if mibBuilder.loadTexts: muxVc4Entry.setStatus('current')
muxVc4Index = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxVc4Index.setStatus('current')
muxVc4Name = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1, 1, 2), MgmtNameString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxVc4Name.setStatus('current')
muxVc4Descr = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: muxVc4Descr.setStatus('current')
muxVc4Subrack = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1, 1, 4), SubrackNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxVc4Subrack.setStatus('current')
muxVc4Slot = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1, 1, 5), SlotNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxVc4Slot.setStatus('current')
muxVc4TxPort = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1, 1, 6), PortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxVc4TxPort.setStatus('current')
muxVc4RxPort = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1, 1, 7), PortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxVc4RxPort.setStatus('current')
muxVc4Vc4 = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxVc4Vc4.setStatus('current')
muxVc4Mode = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("addDrop", 1), ("passThrough", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxVc4Mode.setStatus('current')
muxVc4ClientDropPort = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxVc4ClientDropPort.setStatus('current')
muxVc4TxDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1, 1, 11), MuxTxDirection()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxVc4TxDirection.setStatus('current')
muxVc4ClientAddPort = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1, 1, 12), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxVc4ClientAddPort.setStatus('current')
muxVc4ConnectionMode = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unused", 1), ("ringUsed", 2), ("nodeUsed", 3))).clone('unused')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: muxVc4ConnectionMode.setStatus('deprecated')
muxVc4ConnectionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("addDrop", 1), ("passThrough", 2), ("unconnected", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxVc4ConnectionStatus.setStatus('deprecated')
muxVc4ConnectionOverview = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1, 1, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxVc4ConnectionOverview.setStatus('current')
muxVc4ObjectProperty = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1, 1, 16), ObjectProperty()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxVc4ObjectProperty.setStatus('current')
muxVc4AuAlarmIndicationSignalW2C = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ok", 1), ("alarm", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxVc4AuAlarmIndicationSignalW2C.setStatus('current')
muxVc4AuLossOfPointerW2C = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ok", 1), ("alarm", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxVc4AuLossOfPointerW2C.setStatus('current')
muxVc4RxSignalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("down", 1), ("degraded", 2), ("up", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxVc4RxSignalStatus.setStatus('current')
muxVc4ConcatenationStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxVc4ConcatenationStatus.setStatus('current')
muxVc4PayloadStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("equipped", 1), ("unequipped", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxVc4PayloadStatus.setStatus('current')
muxVc4AdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 13, 2, 3, 1, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("down", 1), ("up", 2))).clone('up')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: muxVc4AdminStatus.setStatus('current')
muxGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 1, 1)).setObjects(("LUM-MUX-MIB", "muxGeneralLastChangeTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    muxGeneralGroup = muxGeneralGroup.setStatus('current')
muxIfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 1, 2)).setObjects(("LUM-MUX-MIB", "muxIfIndex"), ("LUM-MUX-MIB", "muxIfName"), ("LUM-MUX-MIB", "muxIfDescr"), ("LUM-MUX-MIB", "muxIfSubrack"), ("LUM-MUX-MIB", "muxIfSlot"), ("LUM-MUX-MIB", "muxIfTxPort"), ("LUM-MUX-MIB", "muxIfRxPort"), ("LUM-MUX-MIB", "muxIfInvPhysIndexOrZero"), ("LUM-MUX-MIB", "muxIfPowerLevel"), ("LUM-MUX-MIB", "muxIfPowerLevelHighThreshold"), ("LUM-MUX-MIB", "muxIfPowerLevelLowThreshold"), ("LUM-MUX-MIB", "muxIfAdminStatus"), ("LUM-MUX-MIB", "muxIfOperStatus"), ("LUM-MUX-MIB", "muxIfLossOfSignal"), ("LUM-MUX-MIB", "muxIfReceivedPowerHigh"), ("LUM-MUX-MIB", "muxIfReceivedPowerLow"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    muxIfGroup = muxIfGroup.setStatus('current')
muxIfGroupV2 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 1, 3)).setObjects(("LUM-MUX-MIB", "muxIfIndex"), ("LUM-MUX-MIB", "muxIfName"), ("LUM-MUX-MIB", "muxIfDescr"), ("LUM-MUX-MIB", "muxIfSubrack"), ("LUM-MUX-MIB", "muxIfSlot"), ("LUM-MUX-MIB", "muxIfTxPort"), ("LUM-MUX-MIB", "muxIfRxPort"), ("LUM-MUX-MIB", "muxIfInvPhysIndexOrZero"), ("LUM-MUX-MIB", "muxIfPowerLevel"), ("LUM-MUX-MIB", "muxIfPowerLevelHighThreshold"), ("LUM-MUX-MIB", "muxIfPowerLevelLowThreshold"), ("LUM-MUX-MIB", "muxIfAdminStatus"), ("LUM-MUX-MIB", "muxIfOperStatus"), ("LUM-MUX-MIB", "muxIfLossOfSignal"), ("LUM-MUX-MIB", "muxIfReceivedPowerHigh"), ("LUM-MUX-MIB", "muxIfReceivedPowerLow"), ("LUM-MUX-MIB", "muxIfBitrateMismatch"), ("LUM-MUX-MIB", "muxIfLaserBias"), ("LUM-MUX-MIB", "muxIfLaserBiasThreshold"), ("LUM-MUX-MIB", "muxIfJ0PathTrace"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    muxIfGroupV2 = muxIfGroupV2.setStatus('deprecated')
muxIfGroupV3 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 1, 4)).setObjects(("LUM-MUX-MIB", "muxIfIndex"), ("LUM-MUX-MIB", "muxIfName"), ("LUM-MUX-MIB", "muxIfDescr"), ("LUM-MUX-MIB", "muxIfSubrack"), ("LUM-MUX-MIB", "muxIfSlot"), ("LUM-MUX-MIB", "muxIfTxPort"), ("LUM-MUX-MIB", "muxIfRxPort"), ("LUM-MUX-MIB", "muxIfInvPhysIndexOrZero"), ("LUM-MUX-MIB", "muxIfPowerLevel"), ("LUM-MUX-MIB", "muxIfPowerLevelHighThreshold"), ("LUM-MUX-MIB", "muxIfPowerLevelLowThreshold"), ("LUM-MUX-MIB", "muxIfAdminStatus"), ("LUM-MUX-MIB", "muxIfOperStatus"), ("LUM-MUX-MIB", "muxIfLossOfSignal"), ("LUM-MUX-MIB", "muxIfReceivedPowerHigh"), ("LUM-MUX-MIB", "muxIfReceivedPowerLow"), ("LUM-MUX-MIB", "muxIfBitrateMismatch"), ("LUM-MUX-MIB", "muxIfLaserBias"), ("LUM-MUX-MIB", "muxIfLaserBiasThreshold"), ("LUM-MUX-MIB", "muxIfJ0PathTrace"), ("LUM-MUX-MIB", "muxIfAlarmIndicationSignal"), ("LUM-MUX-MIB", "muxIfLossOfFrame"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    muxIfGroupV3 = muxIfGroupV3.setStatus('deprecated')
muxIfGroupV4 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 1, 5)).setObjects(("LUM-MUX-MIB", "muxIfIndex"), ("LUM-MUX-MIB", "muxIfName"), ("LUM-MUX-MIB", "muxIfDescr"), ("LUM-MUX-MIB", "muxIfSubrack"), ("LUM-MUX-MIB", "muxIfSlot"), ("LUM-MUX-MIB", "muxIfTxPort"), ("LUM-MUX-MIB", "muxIfRxPort"), ("LUM-MUX-MIB", "muxIfInvPhysIndexOrZero"), ("LUM-MUX-MIB", "muxIfPowerLevel"), ("LUM-MUX-MIB", "muxIfPowerLevelHighThreshold"), ("LUM-MUX-MIB", "muxIfPowerLevelLowThreshold"), ("LUM-MUX-MIB", "muxIfAdminStatus"), ("LUM-MUX-MIB", "muxIfOperStatus"), ("LUM-MUX-MIB", "muxIfLossOfSignal"), ("LUM-MUX-MIB", "muxIfReceivedPowerHigh"), ("LUM-MUX-MIB", "muxIfReceivedPowerLow"), ("LUM-MUX-MIB", "muxIfBitrateMismatch"), ("LUM-MUX-MIB", "muxIfLaserBias"), ("LUM-MUX-MIB", "muxIfLaserBiasThreshold"), ("LUM-MUX-MIB", "muxIfJ0PathTrace"), ("LUM-MUX-MIB", "muxIfAlarmIndicationSignal"), ("LUM-MUX-MIB", "muxIfLossOfFrame"), ("LUM-MUX-MIB", "muxIfLaserStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    muxIfGroupV4 = muxIfGroupV4.setStatus('deprecated')
muxGeneralGroupV2 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 1, 6)).setObjects(("LUM-MUX-MIB", "muxGeneralLastChangeTime"), ("LUM-MUX-MIB", "muxGeneralStateLastChangeTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    muxGeneralGroupV2 = muxGeneralGroupV2.setStatus('deprecated')
muxVc4Group = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 1, 7)).setObjects(("LUM-MUX-MIB", "muxVc4Index"), ("LUM-MUX-MIB", "muxVc4Name"), ("LUM-MUX-MIB", "muxVc4Descr"), ("LUM-MUX-MIB", "muxVc4Subrack"), ("LUM-MUX-MIB", "muxVc4Slot"), ("LUM-MUX-MIB", "muxVc4TxPort"), ("LUM-MUX-MIB", "muxVc4RxPort"), ("LUM-MUX-MIB", "muxVc4Vc4"), ("LUM-MUX-MIB", "muxVc4Mode"), ("LUM-MUX-MIB", "muxVc4ClientDropPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    muxVc4Group = muxVc4Group.setStatus('deprecated')
muxIfGroupV5 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 1, 8)).setObjects(("LUM-MUX-MIB", "muxIfIndex"), ("LUM-MUX-MIB", "muxIfName"), ("LUM-MUX-MIB", "muxIfDescr"), ("LUM-MUX-MIB", "muxIfSubrack"), ("LUM-MUX-MIB", "muxIfSlot"), ("LUM-MUX-MIB", "muxIfTxPort"), ("LUM-MUX-MIB", "muxIfRxPort"), ("LUM-MUX-MIB", "muxIfInvPhysIndexOrZero"), ("LUM-MUX-MIB", "muxIfPowerLevel"), ("LUM-MUX-MIB", "muxIfPowerLevelHighThreshold"), ("LUM-MUX-MIB", "muxIfPowerLevelLowThreshold"), ("LUM-MUX-MIB", "muxIfAdminStatus"), ("LUM-MUX-MIB", "muxIfOperStatus"), ("LUM-MUX-MIB", "muxIfLossOfSignal"), ("LUM-MUX-MIB", "muxIfReceivedPowerHigh"), ("LUM-MUX-MIB", "muxIfReceivedPowerLow"), ("LUM-MUX-MIB", "muxIfBitrateMismatch"), ("LUM-MUX-MIB", "muxIfLaserBias"), ("LUM-MUX-MIB", "muxIfLaserBiasThreshold"), ("LUM-MUX-MIB", "muxIfJ0PathTrace"), ("LUM-MUX-MIB", "muxIfAlarmIndicationSignal"), ("LUM-MUX-MIB", "muxIfLossOfFrame"), ("LUM-MUX-MIB", "muxIfLaserStatus"), ("LUM-MUX-MIB", "muxIfTxDirection"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    muxIfGroupV5 = muxIfGroupV5.setStatus('deprecated')
muxVc4GroupV2 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 1, 9)).setObjects(("LUM-MUX-MIB", "muxVc4Index"), ("LUM-MUX-MIB", "muxVc4Name"), ("LUM-MUX-MIB", "muxVc4Descr"), ("LUM-MUX-MIB", "muxVc4Subrack"), ("LUM-MUX-MIB", "muxVc4Slot"), ("LUM-MUX-MIB", "muxVc4TxPort"), ("LUM-MUX-MIB", "muxVc4RxPort"), ("LUM-MUX-MIB", "muxVc4Vc4"), ("LUM-MUX-MIB", "muxVc4Mode"), ("LUM-MUX-MIB", "muxVc4ClientDropPort"), ("LUM-MUX-MIB", "muxVc4TxDirection"), ("LUM-MUX-MIB", "muxVc4ClientAddPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    muxVc4GroupV2 = muxVc4GroupV2.setStatus('deprecated')
muxIfGroupV6 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 1, 10)).setObjects(("LUM-MUX-MIB", "muxIfIndex"), ("LUM-MUX-MIB", "muxIfName"), ("LUM-MUX-MIB", "muxIfDescr"), ("LUM-MUX-MIB", "muxIfSubrack"), ("LUM-MUX-MIB", "muxIfSlot"), ("LUM-MUX-MIB", "muxIfTxPort"), ("LUM-MUX-MIB", "muxIfRxPort"), ("LUM-MUX-MIB", "muxIfInvPhysIndexOrZero"), ("LUM-MUX-MIB", "muxIfPowerLevel"), ("LUM-MUX-MIB", "muxIfPowerLevelHighThreshold"), ("LUM-MUX-MIB", "muxIfPowerLevelLowThreshold"), ("LUM-MUX-MIB", "muxIfAdminStatus"), ("LUM-MUX-MIB", "muxIfOperStatus"), ("LUM-MUX-MIB", "muxIfLossOfSignal"), ("LUM-MUX-MIB", "muxIfReceivedPowerHigh"), ("LUM-MUX-MIB", "muxIfReceivedPowerLow"), ("LUM-MUX-MIB", "muxIfBitrateMismatch"), ("LUM-MUX-MIB", "muxIfLaserBias"), ("LUM-MUX-MIB", "muxIfLaserBiasThreshold"), ("LUM-MUX-MIB", "muxIfJ0PathTrace"), ("LUM-MUX-MIB", "muxIfAlarmIndicationSignal"), ("LUM-MUX-MIB", "muxIfLossOfFrame"), ("LUM-MUX-MIB", "muxIfLaserStatus"), ("LUM-MUX-MIB", "muxIfTxDirection"), ("LUM-MUX-MIB", "muxIfExpectedTxLambda"), ("LUM-MUX-MIB", "muxIfTxLambda"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    muxIfGroupV6 = muxIfGroupV6.setStatus('deprecated')
muxIfGroupV7 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 1, 11)).setObjects(("LUM-MUX-MIB", "muxIfIndex"), ("LUM-MUX-MIB", "muxIfName"), ("LUM-MUX-MIB", "muxIfDescr"), ("LUM-MUX-MIB", "muxIfSubrack"), ("LUM-MUX-MIB", "muxIfSlot"), ("LUM-MUX-MIB", "muxIfTxPort"), ("LUM-MUX-MIB", "muxIfRxPort"), ("LUM-MUX-MIB", "muxIfInvPhysIndexOrZero"), ("LUM-MUX-MIB", "muxIfPowerLevel"), ("LUM-MUX-MIB", "muxIfPowerLevelHighThreshold"), ("LUM-MUX-MIB", "muxIfPowerLevelLowThreshold"), ("LUM-MUX-MIB", "muxIfAdminStatus"), ("LUM-MUX-MIB", "muxIfOperStatus"), ("LUM-MUX-MIB", "muxIfLossOfSignal"), ("LUM-MUX-MIB", "muxIfReceivedPowerHigh"), ("LUM-MUX-MIB", "muxIfReceivedPowerLow"), ("LUM-MUX-MIB", "muxIfBitrateMismatch"), ("LUM-MUX-MIB", "muxIfLaserBias"), ("LUM-MUX-MIB", "muxIfLaserBiasThreshold"), ("LUM-MUX-MIB", "muxIfJ0PathTrace"), ("LUM-MUX-MIB", "muxIfAlarmIndicationSignal"), ("LUM-MUX-MIB", "muxIfLossOfFrame"), ("LUM-MUX-MIB", "muxIfLaserStatus"), ("LUM-MUX-MIB", "muxIfTxDirection"), ("LUM-MUX-MIB", "muxIfExpectedTxLambda"), ("LUM-MUX-MIB", "muxIfTxLambda"), ("LUM-MUX-MIB", "muxIfTraceIntrusionMode"), ("LUM-MUX-MIB", "muxIfTraceTransmitted"), ("LUM-MUX-MIB", "muxIfTraceReceived"), ("LUM-MUX-MIB", "muxIfTraceExpected"), ("LUM-MUX-MIB", "muxIfTraceAlarmMode"), ("LUM-MUX-MIB", "muxIfTraceMismatch"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    muxIfGroupV7 = muxIfGroupV7.setStatus('deprecated')
muxIfGroupV8 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 1, 12)).setObjects(("LUM-MUX-MIB", "muxIfIndex"), ("LUM-MUX-MIB", "muxIfName"), ("LUM-MUX-MIB", "muxIfDescr"), ("LUM-MUX-MIB", "muxIfSubrack"), ("LUM-MUX-MIB", "muxIfSlot"), ("LUM-MUX-MIB", "muxIfTxPort"), ("LUM-MUX-MIB", "muxIfRxPort"), ("LUM-MUX-MIB", "muxIfInvPhysIndexOrZero"), ("LUM-MUX-MIB", "muxIfPowerLevel"), ("LUM-MUX-MIB", "muxIfPowerLevelHighThreshold"), ("LUM-MUX-MIB", "muxIfPowerLevelLowThreshold"), ("LUM-MUX-MIB", "muxIfAdminStatus"), ("LUM-MUX-MIB", "muxIfOperStatus"), ("LUM-MUX-MIB", "muxIfLossOfSignal"), ("LUM-MUX-MIB", "muxIfReceivedPowerHigh"), ("LUM-MUX-MIB", "muxIfReceivedPowerLow"), ("LUM-MUX-MIB", "muxIfBitrateMismatch"), ("LUM-MUX-MIB", "muxIfLaserBias"), ("LUM-MUX-MIB", "muxIfLaserBiasThreshold"), ("LUM-MUX-MIB", "muxIfJ0PathTrace"), ("LUM-MUX-MIB", "muxIfAlarmIndicationSignal"), ("LUM-MUX-MIB", "muxIfLossOfFrame"), ("LUM-MUX-MIB", "muxIfLaserStatus"), ("LUM-MUX-MIB", "muxIfTxDirection"), ("LUM-MUX-MIB", "muxIfExpectedTxLambda"), ("LUM-MUX-MIB", "muxIfTxLambda"), ("LUM-MUX-MIB", "muxIfTraceIntrusionMode"), ("LUM-MUX-MIB", "muxIfTraceTransmitted"), ("LUM-MUX-MIB", "muxIfTraceReceived"), ("LUM-MUX-MIB", "muxIfTraceExpected"), ("LUM-MUX-MIB", "muxIfTraceAlarmMode"), ("LUM-MUX-MIB", "muxIfTraceMismatch"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    muxIfGroupV8 = muxIfGroupV8.setStatus('deprecated')
muxVc4GroupV3 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 1, 13)).setObjects(("LUM-MUX-MIB", "muxVc4Index"), ("LUM-MUX-MIB", "muxVc4Name"), ("LUM-MUX-MIB", "muxVc4Descr"), ("LUM-MUX-MIB", "muxVc4Subrack"), ("LUM-MUX-MIB", "muxVc4Slot"), ("LUM-MUX-MIB", "muxVc4TxPort"), ("LUM-MUX-MIB", "muxVc4RxPort"), ("LUM-MUX-MIB", "muxVc4Vc4"), ("LUM-MUX-MIB", "muxVc4Mode"), ("LUM-MUX-MIB", "muxVc4ClientDropPort"), ("LUM-MUX-MIB", "muxVc4TxDirection"), ("LUM-MUX-MIB", "muxVc4ClientAddPort"), ("LUM-MUX-MIB", "muxVc4ConnectionMode"), ("LUM-MUX-MIB", "muxVc4ConnectionStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    muxVc4GroupV3 = muxVc4GroupV3.setStatus('deprecated')
muxVc4GroupV4 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 1, 14)).setObjects(("LUM-MUX-MIB", "muxVc4Index"), ("LUM-MUX-MIB", "muxVc4Name"), ("LUM-MUX-MIB", "muxVc4Descr"), ("LUM-MUX-MIB", "muxVc4Subrack"), ("LUM-MUX-MIB", "muxVc4Slot"), ("LUM-MUX-MIB", "muxVc4TxPort"), ("LUM-MUX-MIB", "muxVc4RxPort"), ("LUM-MUX-MIB", "muxVc4Vc4"), ("LUM-MUX-MIB", "muxVc4ClientDropPort"), ("LUM-MUX-MIB", "muxVc4TxDirection"), ("LUM-MUX-MIB", "muxVc4ClientAddPort"), ("LUM-MUX-MIB", "muxVc4ConnectionMode"), ("LUM-MUX-MIB", "muxVc4ConnectionStatus"), ("LUM-MUX-MIB", "muxVc4ConnectionOverview"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    muxVc4GroupV4 = muxVc4GroupV4.setStatus('deprecated')
muxVc4GroupV5 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 1, 15)).setObjects(("LUM-MUX-MIB", "muxVc4Index"), ("LUM-MUX-MIB", "muxVc4Name"), ("LUM-MUX-MIB", "muxVc4Descr"), ("LUM-MUX-MIB", "muxVc4Subrack"), ("LUM-MUX-MIB", "muxVc4Slot"), ("LUM-MUX-MIB", "muxVc4TxPort"), ("LUM-MUX-MIB", "muxVc4RxPort"), ("LUM-MUX-MIB", "muxVc4Vc4"), ("LUM-MUX-MIB", "muxVc4ClientDropPort"), ("LUM-MUX-MIB", "muxVc4TxDirection"), ("LUM-MUX-MIB", "muxVc4ClientAddPort"), ("LUM-MUX-MIB", "muxVc4ConnectionOverview"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    muxVc4GroupV5 = muxVc4GroupV5.setStatus('deprecated')
muxIfGroupV9 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 1, 16)).setObjects(("LUM-MUX-MIB", "muxIfIndex"), ("LUM-MUX-MIB", "muxIfName"), ("LUM-MUX-MIB", "muxIfDescr"), ("LUM-MUX-MIB", "muxIfSubrack"), ("LUM-MUX-MIB", "muxIfSlot"), ("LUM-MUX-MIB", "muxIfTxPort"), ("LUM-MUX-MIB", "muxIfRxPort"), ("LUM-MUX-MIB", "muxIfInvPhysIndexOrZero"), ("LUM-MUX-MIB", "muxIfPowerLevel"), ("LUM-MUX-MIB", "muxIfPowerLevelHighThreshold"), ("LUM-MUX-MIB", "muxIfPowerLevelLowThreshold"), ("LUM-MUX-MIB", "muxIfAdminStatus"), ("LUM-MUX-MIB", "muxIfOperStatus"), ("LUM-MUX-MIB", "muxIfLossOfSignal"), ("LUM-MUX-MIB", "muxIfReceivedPowerHigh"), ("LUM-MUX-MIB", "muxIfReceivedPowerLow"), ("LUM-MUX-MIB", "muxIfBitrateMismatch"), ("LUM-MUX-MIB", "muxIfLaserBias"), ("LUM-MUX-MIB", "muxIfLaserBiasThreshold"), ("LUM-MUX-MIB", "muxIfJ0PathTrace"), ("LUM-MUX-MIB", "muxIfAlarmIndicationSignal"), ("LUM-MUX-MIB", "muxIfLossOfFrame"), ("LUM-MUX-MIB", "muxIfLaserStatus"), ("LUM-MUX-MIB", "muxIfTxDirection"), ("LUM-MUX-MIB", "muxIfExpectedTxLambda"), ("LUM-MUX-MIB", "muxIfTxLambda"), ("LUM-MUX-MIB", "muxIfTraceIntrusionMode"), ("LUM-MUX-MIB", "muxIfTraceTransmitted"), ("LUM-MUX-MIB", "muxIfTraceReceived"), ("LUM-MUX-MIB", "muxIfTraceExpected"), ("LUM-MUX-MIB", "muxIfTraceAlarmMode"), ("LUM-MUX-MIB", "muxIfTraceMismatch"), ("LUM-MUX-MIB", "muxIfSuppressRemoteAlarms"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    muxIfGroupV9 = muxIfGroupV9.setStatus('deprecated')
muxIfGroupV10 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 1, 17)).setObjects(("LUM-MUX-MIB", "muxIfIndex"), ("LUM-MUX-MIB", "muxIfName"), ("LUM-MUX-MIB", "muxIfDescr"), ("LUM-MUX-MIB", "muxIfSubrack"), ("LUM-MUX-MIB", "muxIfSlot"), ("LUM-MUX-MIB", "muxIfTxPort"), ("LUM-MUX-MIB", "muxIfRxPort"), ("LUM-MUX-MIB", "muxIfInvPhysIndexOrZero"), ("LUM-MUX-MIB", "muxIfPowerLevel"), ("LUM-MUX-MIB", "muxIfPowerLevelHighThreshold"), ("LUM-MUX-MIB", "muxIfPowerLevelLowThreshold"), ("LUM-MUX-MIB", "muxIfAdminStatus"), ("LUM-MUX-MIB", "muxIfOperStatus"), ("LUM-MUX-MIB", "muxIfLossOfSignal"), ("LUM-MUX-MIB", "muxIfReceivedPowerHigh"), ("LUM-MUX-MIB", "muxIfReceivedPowerLow"), ("LUM-MUX-MIB", "muxIfBitrateMismatch"), ("LUM-MUX-MIB", "muxIfLaserBias"), ("LUM-MUX-MIB", "muxIfLaserBiasThreshold"), ("LUM-MUX-MIB", "muxIfAlarmIndicationSignal"), ("LUM-MUX-MIB", "muxIfLossOfFrame"), ("LUM-MUX-MIB", "muxIfLaserStatus"), ("LUM-MUX-MIB", "muxIfTxDirection"), ("LUM-MUX-MIB", "muxIfExpectedTxLambda"), ("LUM-MUX-MIB", "muxIfTxLambda"), ("LUM-MUX-MIB", "muxIfTraceIntrusionMode"), ("LUM-MUX-MIB", "muxIfTraceTransmitted"), ("LUM-MUX-MIB", "muxIfTraceReceived"), ("LUM-MUX-MIB", "muxIfTraceExpected"), ("LUM-MUX-MIB", "muxIfTraceAlarmMode"), ("LUM-MUX-MIB", "muxIfTraceMismatch"), ("LUM-MUX-MIB", "muxIfOHTransparency"), ("LUM-MUX-MIB", "muxIfSuppressRemoteAlarms"), ("LUM-MUX-MIB", "muxIfHighSpeedMin"), ("LUM-MUX-MIB", "muxIfHighSpeedMax"), ("LUM-MUX-MIB", "muxIfTrxCodeMismatch"), ("LUM-MUX-MIB", "muxIfTrxBitrateUnavailable"), ("LUM-MUX-MIB", "muxIfTrxMissing"), ("LUM-MUX-MIB", "muxIfTrxClass"), ("LUM-MUX-MIB", "muxIfTransmitterFailed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    muxIfGroupV10 = muxIfGroupV10.setStatus('deprecated')
muxIfGroupV11 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 1, 18)).setObjects(("LUM-MUX-MIB", "muxIfIndex"), ("LUM-MUX-MIB", "muxIfName"), ("LUM-MUX-MIB", "muxIfDescr"), ("LUM-MUX-MIB", "muxIfSubrack"), ("LUM-MUX-MIB", "muxIfSlot"), ("LUM-MUX-MIB", "muxIfTxPort"), ("LUM-MUX-MIB", "muxIfRxPort"), ("LUM-MUX-MIB", "muxIfInvPhysIndexOrZero"), ("LUM-MUX-MIB", "muxIfPowerLevel"), ("LUM-MUX-MIB", "muxIfPowerLevelHighThreshold"), ("LUM-MUX-MIB", "muxIfPowerLevelLowThreshold"), ("LUM-MUX-MIB", "muxIfAdminStatus"), ("LUM-MUX-MIB", "muxIfOperStatus"), ("LUM-MUX-MIB", "muxIfLossOfSignal"), ("LUM-MUX-MIB", "muxIfReceivedPowerHigh"), ("LUM-MUX-MIB", "muxIfReceivedPowerLow"), ("LUM-MUX-MIB", "muxIfBitrateMismatch"), ("LUM-MUX-MIB", "muxIfLaserBias"), ("LUM-MUX-MIB", "muxIfLaserBiasThreshold"), ("LUM-MUX-MIB", "muxIfAlarmIndicationSignal"), ("LUM-MUX-MIB", "muxIfLossOfFrame"), ("LUM-MUX-MIB", "muxIfLaserStatus"), ("LUM-MUX-MIB", "muxIfTxDirection"), ("LUM-MUX-MIB", "muxIfExpectedTxLambda"), ("LUM-MUX-MIB", "muxIfTxLambda"), ("LUM-MUX-MIB", "muxIfTraceIntrusionMode"), ("LUM-MUX-MIB", "muxIfTraceTransmitted"), ("LUM-MUX-MIB", "muxIfTraceReceived"), ("LUM-MUX-MIB", "muxIfTraceExpected"), ("LUM-MUX-MIB", "muxIfTraceAlarmMode"), ("LUM-MUX-MIB", "muxIfTraceMismatch"), ("LUM-MUX-MIB", "muxIfOHTransparency"), ("LUM-MUX-MIB", "muxIfSuppressRemoteAlarms"), ("LUM-MUX-MIB", "muxIfHighSpeedMin"), ("LUM-MUX-MIB", "muxIfHighSpeedMax"), ("LUM-MUX-MIB", "muxIfTrxCodeMismatch"), ("LUM-MUX-MIB", "muxIfTrxBitrateUnavailable"), ("LUM-MUX-MIB", "muxIfTrxMissing"), ("LUM-MUX-MIB", "muxIfTrxClass"), ("LUM-MUX-MIB", "muxIfTransmitterFailed"), ("LUM-MUX-MIB", "muxIfIllegalFrequency"), ("LUM-MUX-MIB", "muxIfReceiverSensitivity"), ("LUM-MUX-MIB", "muxIfPowerLevelLowRelativeThreshold"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    muxIfGroupV11 = muxIfGroupV11.setStatus('deprecated')
muxGeneralGroupV3 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 1, 19)).setObjects(("LUM-MUX-MIB", "muxGeneralLastChangeTime"), ("LUM-MUX-MIB", "muxGeneralStateLastChangeTime"), ("LUM-MUX-MIB", "muxGeneralMuxIfTableSize"), ("LUM-MUX-MIB", "muxGeneralMuxVc4TableSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    muxGeneralGroupV3 = muxGeneralGroupV3.setStatus('current')
muxIfGroupV12 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 1, 20)).setObjects(("LUM-MUX-MIB", "muxIfIndex"), ("LUM-MUX-MIB", "muxIfName"), ("LUM-MUX-MIB", "muxIfDescr"), ("LUM-MUX-MIB", "muxIfSubrack"), ("LUM-MUX-MIB", "muxIfSlot"), ("LUM-MUX-MIB", "muxIfTxPort"), ("LUM-MUX-MIB", "muxIfRxPort"), ("LUM-MUX-MIB", "muxIfInvPhysIndexOrZero"), ("LUM-MUX-MIB", "muxIfPowerLevel"), ("LUM-MUX-MIB", "muxIfPowerLevelHighThreshold"), ("LUM-MUX-MIB", "muxIfPowerLevelLowThreshold"), ("LUM-MUX-MIB", "muxIfAdminStatus"), ("LUM-MUX-MIB", "muxIfOperStatus"), ("LUM-MUX-MIB", "muxIfLossOfSignal"), ("LUM-MUX-MIB", "muxIfReceivedPowerHigh"), ("LUM-MUX-MIB", "muxIfReceivedPowerLow"), ("LUM-MUX-MIB", "muxIfBitrateMismatch"), ("LUM-MUX-MIB", "muxIfLaserBias"), ("LUM-MUX-MIB", "muxIfLaserBiasThreshold"), ("LUM-MUX-MIB", "muxIfAlarmIndicationSignal"), ("LUM-MUX-MIB", "muxIfLossOfFrame"), ("LUM-MUX-MIB", "muxIfLaserStatus"), ("LUM-MUX-MIB", "muxIfTxDirection"), ("LUM-MUX-MIB", "muxIfExpectedTxLambda"), ("LUM-MUX-MIB", "muxIfTxLambda"), ("LUM-MUX-MIB", "muxIfTraceIntrusionMode"), ("LUM-MUX-MIB", "muxIfTraceTransmitted"), ("LUM-MUX-MIB", "muxIfTraceReceived"), ("LUM-MUX-MIB", "muxIfTraceExpected"), ("LUM-MUX-MIB", "muxIfTraceAlarmMode"), ("LUM-MUX-MIB", "muxIfTraceMismatch"), ("LUM-MUX-MIB", "muxIfOHTransparency"), ("LUM-MUX-MIB", "muxIfSuppressRemoteAlarms"), ("LUM-MUX-MIB", "muxIfHighSpeedMin"), ("LUM-MUX-MIB", "muxIfHighSpeedMax"), ("LUM-MUX-MIB", "muxIfTrxCodeMismatch"), ("LUM-MUX-MIB", "muxIfTrxBitrateUnavailable"), ("LUM-MUX-MIB", "muxIfTrxMissing"), ("LUM-MUX-MIB", "muxIfTrxClass"), ("LUM-MUX-MIB", "muxIfTransmitterFailed"), ("LUM-MUX-MIB", "muxIfUnexpectedFrequency"), ("LUM-MUX-MIB", "muxIfIllegalFrequency"), ("LUM-MUX-MIB", "muxIfReceiverSensitivity"), ("LUM-MUX-MIB", "muxIfPowerLevelLowRelativeThreshold"), ("LUM-MUX-MIB", "muxIfObjectProperty"), ("LUM-MUX-MIB", "muxIfTxPowerLevel"), ("LUM-MUX-MIB", "muxIfLaserTempActual"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    muxIfGroupV12 = muxIfGroupV12.setStatus('current')
muxVc4GroupV6 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 1, 21)).setObjects(("LUM-MUX-MIB", "muxVc4Index"), ("LUM-MUX-MIB", "muxVc4Name"), ("LUM-MUX-MIB", "muxVc4Descr"), ("LUM-MUX-MIB", "muxVc4Subrack"), ("LUM-MUX-MIB", "muxVc4Slot"), ("LUM-MUX-MIB", "muxVc4TxPort"), ("LUM-MUX-MIB", "muxVc4RxPort"), ("LUM-MUX-MIB", "muxVc4Vc4"), ("LUM-MUX-MIB", "muxVc4ClientDropPort"), ("LUM-MUX-MIB", "muxVc4TxDirection"), ("LUM-MUX-MIB", "muxVc4ClientAddPort"), ("LUM-MUX-MIB", "muxVc4ConnectionOverview"), ("LUM-MUX-MIB", "muxVc4ObjectProperty"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    muxVc4GroupV6 = muxVc4GroupV6.setStatus('deprecated')
muxVc4GroupV7 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 1, 22)).setObjects(("LUM-MUX-MIB", "muxVc4Index"), ("LUM-MUX-MIB", "muxVc4Name"), ("LUM-MUX-MIB", "muxVc4Descr"), ("LUM-MUX-MIB", "muxVc4Subrack"), ("LUM-MUX-MIB", "muxVc4Slot"), ("LUM-MUX-MIB", "muxVc4TxPort"), ("LUM-MUX-MIB", "muxVc4RxPort"), ("LUM-MUX-MIB", "muxVc4Vc4"), ("LUM-MUX-MIB", "muxVc4ClientDropPort"), ("LUM-MUX-MIB", "muxVc4TxDirection"), ("LUM-MUX-MIB", "muxVc4ClientAddPort"), ("LUM-MUX-MIB", "muxVc4ConnectionOverview"), ("LUM-MUX-MIB", "muxVc4ObjectProperty"), ("LUM-MUX-MIB", "muxVc4AuAlarmIndicationSignalW2C"), ("LUM-MUX-MIB", "muxVc4AuLossOfPointerW2C"), ("LUM-MUX-MIB", "muxVc4RxSignalStatus"), ("LUM-MUX-MIB", "muxVc4ConcatenationStatus"), ("LUM-MUX-MIB", "muxVc4PayloadStatus"), ("LUM-MUX-MIB", "muxVc4AdminStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    muxVc4GroupV7 = muxVc4GroupV7.setStatus('current')
lumMuxBasicComplV1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 2, 1)).setObjects(("LUM-MUX-MIB", "muxGeneralGroup"), ("LUM-MUX-MIB", "muxIfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumMuxBasicComplV1 = lumMuxBasicComplV1.setStatus('current')
lumMuxBasicComplV2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 2, 2)).setObjects(("LUM-MUX-MIB", "muxGeneralGroup"), ("LUM-MUX-MIB", "muxIfGroupV2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumMuxBasicComplV2 = lumMuxBasicComplV2.setStatus('deprecated')
lumMuxBasicComplV3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 2, 3)).setObjects(("LUM-MUX-MIB", "muxGeneralGroup"), ("LUM-MUX-MIB", "muxIfGroupV3"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumMuxBasicComplV3 = lumMuxBasicComplV3.setStatus('deprecated')
lumMuxBasicComplV4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 2, 4)).setObjects(("LUM-MUX-MIB", "muxGeneralGroup"), ("LUM-MUX-MIB", "muxIfGroupV4"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumMuxBasicComplV4 = lumMuxBasicComplV4.setStatus('deprecated')
lumMuxBasicComplV5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 2, 5)).setObjects(("LUM-MUX-MIB", "muxGeneralGroupV2"), ("LUM-MUX-MIB", "muxIfGroupV4"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumMuxBasicComplV5 = lumMuxBasicComplV5.setStatus('deprecated')
lumMuxBasicComplV6 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 2, 6)).setObjects(("LUM-MUX-MIB", "muxGeneralGroupV2"), ("LUM-MUX-MIB", "muxIfGroupV4"), ("LUM-MUX-MIB", "muxVc4Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumMuxBasicComplV6 = lumMuxBasicComplV6.setStatus('deprecated')
lumMuxBasicComplV7 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 2, 7)).setObjects(("LUM-MUX-MIB", "muxGeneralGroupV2"), ("LUM-MUX-MIB", "muxIfGroupV5"), ("LUM-MUX-MIB", "muxVc4Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumMuxBasicComplV7 = lumMuxBasicComplV7.setStatus('deprecated')
lumMuxBasicComplV8 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 2, 8)).setObjects(("LUM-MUX-MIB", "muxGeneralGroupV2"), ("LUM-MUX-MIB", "muxIfGroupV5"), ("LUM-MUX-MIB", "muxVc4GroupV2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumMuxBasicComplV8 = lumMuxBasicComplV8.setStatus('deprecated')
lumMuxBasicComplV9 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 2, 9)).setObjects(("LUM-MUX-MIB", "muxGeneralGroupV2"), ("LUM-MUX-MIB", "muxIfGroupV6"), ("LUM-MUX-MIB", "muxVc4GroupV2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumMuxBasicComplV9 = lumMuxBasicComplV9.setStatus('deprecated')
lumMuxBasicComplV10 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 2, 10)).setObjects(("LUM-MUX-MIB", "muxGeneralGroupV2"), ("LUM-MUX-MIB", "muxIfGroupV7"), ("LUM-MUX-MIB", "muxVc4GroupV2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumMuxBasicComplV10 = lumMuxBasicComplV10.setStatus('deprecated')
lumMuxBasicComplV11 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 2, 11)).setObjects(("LUM-MUX-MIB", "muxGeneralGroupV2"), ("LUM-MUX-MIB", "muxIfGroupV8"), ("LUM-MUX-MIB", "muxVc4GroupV2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumMuxBasicComplV11 = lumMuxBasicComplV11.setStatus('deprecated')
lumMuxBasicComplV12 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 2, 12)).setObjects(("LUM-MUX-MIB", "muxGeneralGroupV2"), ("LUM-MUX-MIB", "muxIfGroupV8"), ("LUM-MUX-MIB", "muxVc4GroupV3"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumMuxBasicComplV12 = lumMuxBasicComplV12.setStatus('deprecated')
lumMuxBasicComplV13 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 2, 13)).setObjects(("LUM-MUX-MIB", "muxGeneralGroupV2"), ("LUM-MUX-MIB", "muxIfGroupV8"), ("LUM-MUX-MIB", "muxVc4GroupV4"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumMuxBasicComplV13 = lumMuxBasicComplV13.setStatus('deprecated')
lumMuxBasicComplV14 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 2, 14)).setObjects(("LUM-MUX-MIB", "muxGeneralGroupV2"), ("LUM-MUX-MIB", "muxIfGroupV8"), ("LUM-MUX-MIB", "muxVc4GroupV5"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumMuxBasicComplV14 = lumMuxBasicComplV14.setStatus('deprecated')
lumMuxBasicComplV15 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 2, 15)).setObjects(("LUM-MUX-MIB", "muxGeneralGroupV2"), ("LUM-MUX-MIB", "muxIfGroupV9"), ("LUM-MUX-MIB", "muxVc4GroupV5"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumMuxBasicComplV15 = lumMuxBasicComplV15.setStatus('deprecated')
lumMuxBasicComplV16 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 2, 16)).setObjects(("LUM-MUX-MIB", "muxGeneralGroupV2"), ("LUM-MUX-MIB", "muxIfGroupV10"), ("LUM-MUX-MIB", "muxVc4GroupV5"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumMuxBasicComplV16 = lumMuxBasicComplV16.setStatus('deprecated')
lumMuxBasicComplV17 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 2, 17)).setObjects(("LUM-MUX-MIB", "muxGeneralGroupV2"), ("LUM-MUX-MIB", "muxIfGroupV11"), ("LUM-MUX-MIB", "muxVc4GroupV5"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumMuxBasicComplV17 = lumMuxBasicComplV17.setStatus('deprecated')
lumMuxBasicComplV18 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 2, 18)).setObjects(("LUM-MUX-MIB", "muxGeneralGroupV3"), ("LUM-MUX-MIB", "muxIfGroupV11"), ("LUM-MUX-MIB", "muxVc4GroupV5"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumMuxBasicComplV18 = lumMuxBasicComplV18.setStatus('deprecated')
lumMuxBasicComplV19 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 2, 19)).setObjects(("LUM-MUX-MIB", "muxGeneralGroupV3"), ("LUM-MUX-MIB", "muxIfGroupV12"), ("LUM-MUX-MIB", "muxVc4GroupV6"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumMuxBasicComplV19 = lumMuxBasicComplV19.setStatus('deprecated')
lumMuxBasicComplV20 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 2, 20)).setObjects(("LUM-MUX-MIB", "muxGeneralGroupV3"), ("LUM-MUX-MIB", "muxIfGroupV12"), ("LUM-MUX-MIB", "muxVc4GroupV7"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumMuxBasicComplV20 = lumMuxBasicComplV20.setStatus('deprecated')
lumMuxBasicComplV21 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 13, 1, 2, 21)).setObjects(("LUM-MUX-MIB", "muxGeneralGroupV3"), ("LUM-MUX-MIB", "muxIfGroupV12"), ("LUM-MUX-MIB", "muxVc4GroupV7"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumMuxBasicComplV21 = lumMuxBasicComplV21.setStatus('current')
mibBuilder.exportSymbols("LUM-MUX-MIB", muxIfIndex=muxIfIndex, lumMuxBasicComplV17=lumMuxBasicComplV17, muxIfIllegalFrequency=muxIfIllegalFrequency, muxIfExpectedTxLambda=muxIfExpectedTxLambda, muxIfGroupV11=muxIfGroupV11, muxVc4ClientDropPort=muxVc4ClientDropPort, muxIfTrxBitrateUnavailable=muxIfTrxBitrateUnavailable, muxVc4Mode=muxVc4Mode, muxGeneralGroup=muxGeneralGroup, muxIfTraceIntrusionMode=muxIfTraceIntrusionMode, muxIfInvPhysIndexOrZero=muxIfInvPhysIndexOrZero, lumMuxBasicComplV1=lumMuxBasicComplV1, lumMuxGroups=lumMuxGroups, lumMuxBasicComplV6=lumMuxBasicComplV6, muxIfGroupV5=muxIfGroupV5, muxGeneralStateLastChangeTime=muxGeneralStateLastChangeTime, muxIfSlot=muxIfSlot, muxIfTraceMismatch=muxIfTraceMismatch, muxIfAlarmIndicationSignal=muxIfAlarmIndicationSignal, muxVc4GroupV6=muxVc4GroupV6, lumMuxBasicComplV18=lumMuxBasicComplV18, muxIfTrxMissing=muxIfTrxMissing, muxIfPowerLevelLowThreshold=muxIfPowerLevelLowThreshold, muxIfHighSpeedMin=muxIfHighSpeedMin, lumMuxBasicComplV9=lumMuxBasicComplV9, muxIfGroupV3=muxIfGroupV3, muxVc4Group=muxVc4Group, muxVc4ConnectionOverview=muxVc4ConnectionOverview, muxGeneralMuxVc4TableSize=muxGeneralMuxVc4TableSize, muxIfOHTransparency=muxIfOHTransparency, muxIfGroupV8=muxIfGroupV8, muxIfTransmitterFailed=muxIfTransmitterFailed, lumMuxBasicComplV14=lumMuxBasicComplV14, muxIfLaserTempActual=muxIfLaserTempActual, muxIfTrxClass=muxIfTrxClass, muxIfReceiverSensitivity=muxIfReceiverSensitivity, muxVc4PayloadStatus=muxVc4PayloadStatus, lumMuxBasicComplV20=lumMuxBasicComplV20, muxIfList=muxIfList, muxIfTxPowerLevel=muxIfTxPowerLevel, lumMuxBasicComplV16=lumMuxBasicComplV16, muxIfUnexpectedFrequency=muxIfUnexpectedFrequency, lumMuxBasicComplV12=lumMuxBasicComplV12, lumMuxBasicComplV15=lumMuxBasicComplV15, muxIfGroupV9=muxIfGroupV9, muxVc4List=muxVc4List, muxVc4AdminStatus=muxVc4AdminStatus, muxIfTraceAlarmMode=muxIfTraceAlarmMode, lumMuxBasicComplV13=lumMuxBasicComplV13, muxIfTxDirection=muxIfTxDirection, muxIfGroupV4=muxIfGroupV4, muxIfGroupV10=muxIfGroupV10, lumMuxBasicComplV11=lumMuxBasicComplV11, muxVc4Index=muxVc4Index, muxVc4RxPort=muxVc4RxPort, muxVc4ObjectProperty=muxVc4ObjectProperty, muxIfName=muxIfName, muxIfEntry=muxIfEntry, muxIfDescr=muxIfDescr, muxVc4RxSignalStatus=muxVc4RxSignalStatus, muxGeneralLastChangeTime=muxGeneralLastChangeTime, muxIfTable=muxIfTable, muxVc4ClientAddPort=muxVc4ClientAddPort, MuxTxDirection=MuxTxDirection, muxIfAdminStatus=muxIfAdminStatus, muxIfOperStatus=muxIfOperStatus, muxVc4ConcatenationStatus=muxVc4ConcatenationStatus, muxVc4Entry=muxVc4Entry, muxIfJ0PathTrace=muxIfJ0PathTrace, muxGeneralGroupV3=muxGeneralGroupV3, muxIfReceivedPowerHigh=muxIfReceivedPowerHigh, muxIfLaserBias=muxIfLaserBias, muxGeneralMuxIfTableSize=muxGeneralMuxIfTableSize, muxIfBitrateMismatch=muxIfBitrateMismatch, muxVc4Descr=muxVc4Descr, muxVc4Vc4=muxVc4Vc4, muxIfGroup=muxIfGroup, lumMuxBasicComplV5=lumMuxBasicComplV5, muxIfTrxCodeMismatch=muxIfTrxCodeMismatch, muxIfPowerLevelLowRelativeThreshold=muxIfPowerLevelLowRelativeThreshold, muxVc4GroupV3=muxVc4GroupV3, lumMuxMIBObjects=lumMuxMIBObjects, muxIfGroupV7=muxIfGroupV7, muxIfGroupV6=muxIfGroupV6, muxIfGroupV12=muxIfGroupV12, muxIfLossOfSignal=muxIfLossOfSignal, muxIfTxLambda=muxIfTxLambda, muxIfTraceExpected=muxIfTraceExpected, muxIfObjectProperty=muxIfObjectProperty, muxIfLaserBiasThreshold=muxIfLaserBiasThreshold, muxGeneral=muxGeneral, muxVc4GroupV5=muxVc4GroupV5, lumMuxCompl=lumMuxCompl, muxVc4GroupV4=muxVc4GroupV4, lumMuxBasicComplV2=lumMuxBasicComplV2, lumMuxBasicComplV3=lumMuxBasicComplV3, muxIfHighSpeedMax=muxIfHighSpeedMax, PYSNMP_MODULE_ID=lumMuxMIBModule, muxVc4TxDirection=muxVc4TxDirection, lumMuxBasicComplV19=lumMuxBasicComplV19, lumMuxConfs=lumMuxConfs, muxIfLossOfFrame=muxIfLossOfFrame, muxVc4AuLossOfPointerW2C=muxVc4AuLossOfPointerW2C, lumMuxBasicComplV7=lumMuxBasicComplV7, muxVc4Subrack=muxVc4Subrack, muxVc4AuAlarmIndicationSignalW2C=muxVc4AuAlarmIndicationSignalW2C, muxIfSubrack=muxIfSubrack, muxIfPowerLevel=muxIfPowerLevel, muxVc4Name=muxVc4Name, lumMuxBasicComplV8=lumMuxBasicComplV8, muxIfPowerLevelHighThreshold=muxIfPowerLevelHighThreshold, lumMuxBasicComplV21=lumMuxBasicComplV21, muxIfTraceTransmitted=muxIfTraceTransmitted, lumMuxBasicComplV4=lumMuxBasicComplV4, muxVc4GroupV7=muxVc4GroupV7, muxVc4TxPort=muxVc4TxPort, muxGeneralGroupV2=muxGeneralGroupV2, muxVc4ConnectionStatus=muxVc4ConnectionStatus, lumMuxMIBModule=lumMuxMIBModule, muxVc4GroupV2=muxVc4GroupV2, muxIfRxPort=muxIfRxPort, muxIfTraceReceived=muxIfTraceReceived, muxIfReceivedPowerLow=muxIfReceivedPowerLow, muxVc4ConnectionMode=muxVc4ConnectionMode, lumMuxBasicComplV10=lumMuxBasicComplV10, muxIfLaserStatus=muxIfLaserStatus, muxIfSuppressRemoteAlarms=muxIfSuppressRemoteAlarms, muxIfTxPort=muxIfTxPort, muxIfGroupV2=muxIfGroupV2, muxVc4Slot=muxVc4Slot, muxVc4Table=muxVc4Table)
