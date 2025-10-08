#
# PySNMP MIB module SLE-RED-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/dasan/SLE-RED-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:58:10 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
sleMgmt, = mibBuilder.importSymbols("DASAN-SMI", "sleMgmt")
SleControlStatusType, SleControlRequestResultType = mibBuilder.importSymbols("SLE-TC-MIB", "SleControlStatusType", "SleControlRequestResultType")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Integer32, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, TimeTicks, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Integer32", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "TimeTicks", "Bits", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
sleRed = ModuleIdentity((1, 3, 6, 1, 4, 1, 6296, 101, 22))
if mibBuilder.loadTexts: sleRed.setLastUpdated('200710192200Z')
if mibBuilder.loadTexts: sleRed.setOrganization('DASAN Networks.')
class SleRedBoardIdType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("sfuA", 1), ("sfuB", 2))

class SleRedModeType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("redundant", 1), ("standalone", 2))

class SleRedFaultActionType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("switchover", 1), ("log", 2), ("disable", 3))

class SleRedReloadOSType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("os1", 1), ("os2", 2), ("default", 3))

sleRedBase = MibIdentifier((1, 3, 6, 1, 4, 1, 6296, 101, 22, 1))
sleRedInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 6296, 101, 22, 1, 1))
sleRedActiveBoard = MibScalar((1, 3, 6, 1, 4, 1, 6296, 101, 22, 1, 1, 1), SleRedBoardIdType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sleRedActiveBoard.setStatus('current')
sleRedMode = MibScalar((1, 3, 6, 1, 4, 1, 6296, 101, 22, 1, 1, 2), SleRedModeType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sleRedMode.setStatus('current')
sleRedFaultCrashAction = MibScalar((1, 3, 6, 1, 4, 1, 6296, 101, 22, 1, 1, 3), SleRedFaultActionType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sleRedFaultCrashAction.setStatus('current')
sleRedFaultTimeoutAction = MibScalar((1, 3, 6, 1, 4, 1, 6296, 101, 22, 1, 1, 4), SleRedFaultActionType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sleRedFaultTimeoutAction.setStatus('current')
sleRedFaultTimeout = MibScalar((1, 3, 6, 1, 4, 1, 6296, 101, 22, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 720000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sleRedFaultTimeout.setStatus('current')
sleRedActivePrevState = MibScalar((1, 3, 6, 1, 4, 1, 6296, 101, 22, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19))).clone(namedValues=NamedValues(("activeInit", 0), ("singleActiveReady", 1), ("versionReport", 2), ("softwareXfer", 3), ("softwareXferDone", 4), ("configXfer", 5), ("configXferDone", 6), ("stateXfer", 7), ("activeReady", 8), ("disconnectStandby", 9), ("standbyWait", 10), ("versionCheck", 11), ("updateMac", 12), ("softwareSync", 13), ("softwareSyncDone", 14), ("configSync", 15), ("configSyncDone", 16), ("startupSync", 17), ("standbyReady", 18), ("standbyReset", 19)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sleRedActivePrevState.setStatus('current')
sleRedActiveCurrState = MibScalar((1, 3, 6, 1, 4, 1, 6296, 101, 22, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19))).clone(namedValues=NamedValues(("activeInit", 0), ("singleActiveReady", 1), ("versionReport", 2), ("softwareXfer", 3), ("softwareXferDone", 4), ("configXfer", 5), ("configXferDone", 6), ("stateXfer", 7), ("activeReady", 8), ("disconnectStandby", 9), ("standbyWait", 10), ("versionCheck", 11), ("updateMac", 12), ("softwareSync", 13), ("softwareSyncDone", 14), ("configSync", 15), ("configSyncDone", 16), ("startupSync", 17), ("standbyReady", 18), ("standbyReset", 19)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sleRedActiveCurrState.setStatus('current')
sleRedControl = MibIdentifier((1, 3, 6, 1, 4, 1, 6296, 101, 22, 1, 2))
sleRedControlRequest = MibScalar((1, 3, 6, 1, 4, 1, 6296, 101, 22, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("reloadStandby", 1), ("switchover", 2), ("setFaultMonitor", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sleRedControlRequest.setStatus('current')
sleRedControlStatus = MibScalar((1, 3, 6, 1, 4, 1, 6296, 101, 22, 1, 2, 2), SleControlStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sleRedControlStatus.setStatus('current')
sleRedControlTimer = MibScalar((1, 3, 6, 1, 4, 1, 6296, 101, 22, 1, 2, 3), Gauge32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sleRedControlTimer.setStatus('current')
sleRedControlTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 6296, 101, 22, 1, 2, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sleRedControlTimeStamp.setStatus('current')
sleRedControlReqResult = MibScalar((1, 3, 6, 1, 4, 1, 6296, 101, 22, 1, 2, 5), SleControlRequestResultType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sleRedControlReqResult.setStatus('current')
sleRedControlReloadOS = MibScalar((1, 3, 6, 1, 4, 1, 6296, 101, 22, 1, 2, 6), SleRedReloadOSType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sleRedControlReloadOS.setStatus('current')
sleRedControlFaultCrashAction = MibScalar((1, 3, 6, 1, 4, 1, 6296, 101, 22, 1, 2, 7), SleRedFaultActionType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sleRedControlFaultCrashAction.setStatus('current')
sleRedControlFaultTimeoutAction = MibScalar((1, 3, 6, 1, 4, 1, 6296, 101, 22, 1, 2, 8), SleRedFaultActionType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sleRedControlFaultTimeoutAction.setStatus('current')
sleRedControlFaultTimeout = MibScalar((1, 3, 6, 1, 4, 1, 6296, 101, 22, 1, 2, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 720000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sleRedControlFaultTimeout.setStatus('current')
sleRedNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 6296, 101, 22, 1, 3))
sleRedMateReloadRequested = NotificationType((1, 3, 6, 1, 4, 1, 6296, 101, 22, 1, 3, 1)).setObjects(("SLE-RED-MIB", "sleRedControlRequest"), ("SLE-RED-MIB", "sleRedControlTimeStamp"), ("SLE-RED-MIB", "sleRedControlReqResult"), ("SLE-RED-MIB", "sleRedActiveBoard"))
if mibBuilder.loadTexts: sleRedMateReloadRequested.setStatus('current')
sleRedSwitchoverRequested = NotificationType((1, 3, 6, 1, 4, 1, 6296, 101, 22, 1, 3, 2)).setObjects(("SLE-RED-MIB", "sleRedControlRequest"), ("SLE-RED-MIB", "sleRedControlTimeStamp"), ("SLE-RED-MIB", "sleRedControlReqResult"))
if mibBuilder.loadTexts: sleRedSwitchoverRequested.setStatus('current')
sleRedFaultMonitorChanged = NotificationType((1, 3, 6, 1, 4, 1, 6296, 101, 22, 1, 3, 3)).setObjects(("SLE-RED-MIB", "sleRedControlRequest"), ("SLE-RED-MIB", "sleRedControlTimeStamp"), ("SLE-RED-MIB", "sleRedControlReqResult"), ("SLE-RED-MIB", "sleRedControlFaultCrashAction"), ("SLE-RED-MIB", "sleRedControlFaultTimeoutAction"), ("SLE-RED-MIB", "sleRedControlFaultTimeout"))
if mibBuilder.loadTexts: sleRedFaultMonitorChanged.setStatus('current')
sleRedGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6296, 101, 22, 2)).setObjects(("SLE-RED-MIB", "sleRedActiveBoard"), ("SLE-RED-MIB", "sleRedMode"), ("SLE-RED-MIB", "sleRedFaultCrashAction"), ("SLE-RED-MIB", "sleRedFaultTimeoutAction"), ("SLE-RED-MIB", "sleRedFaultTimeout"), ("SLE-RED-MIB", "sleRedControlStatus"), ("SLE-RED-MIB", "sleRedControlTimer"), ("SLE-RED-MIB", "sleRedControlTimeStamp"), ("SLE-RED-MIB", "sleRedControlReqResult"), ("SLE-RED-MIB", "sleRedControlReloadOS"), ("SLE-RED-MIB", "sleRedControlFaultCrashAction"), ("SLE-RED-MIB", "sleRedControlFaultTimeoutAction"), ("SLE-RED-MIB", "sleRedActivePrevState"), ("SLE-RED-MIB", "sleRedActiveCurrState"), ("SLE-RED-MIB", "sleRedControlFaultTimeout"), ("SLE-RED-MIB", "sleRedControlRequest"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sleRedGroup = sleRedGroup.setStatus('current')
sleRedNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6296, 101, 22, 3)).setObjects(("SLE-RED-MIB", "sleRedMateReloadRequested"), ("SLE-RED-MIB", "sleRedSwitchoverRequested"), ("SLE-RED-MIB", "sleRedFaultMonitorChanged"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sleRedNotificationGroup = sleRedNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("SLE-RED-MIB", sleRedFaultMonitorChanged=sleRedFaultMonitorChanged, SleRedModeType=SleRedModeType, sleRedBase=sleRedBase, sleRedActivePrevState=sleRedActivePrevState, sleRedMateReloadRequested=sleRedMateReloadRequested, sleRedActiveCurrState=sleRedActiveCurrState, sleRedNotification=sleRedNotification, sleRedFaultTimeoutAction=sleRedFaultTimeoutAction, sleRedControlRequest=sleRedControlRequest, SleRedReloadOSType=SleRedReloadOSType, sleRedControlTimeStamp=sleRedControlTimeStamp, sleRedNotificationGroup=sleRedNotificationGroup, sleRedControlReqResult=sleRedControlReqResult, sleRedControlFaultTimeoutAction=sleRedControlFaultTimeoutAction, sleRedFaultTimeout=sleRedFaultTimeout, PYSNMP_MODULE_ID=sleRed, sleRedControlReloadOS=sleRedControlReloadOS, sleRedMode=sleRedMode, SleRedBoardIdType=SleRedBoardIdType, SleRedFaultActionType=SleRedFaultActionType, sleRedControlTimer=sleRedControlTimer, sleRedFaultCrashAction=sleRedFaultCrashAction, sleRedGroup=sleRedGroup, sleRedActiveBoard=sleRedActiveBoard, sleRed=sleRed, sleRedControlStatus=sleRedControlStatus, sleRedSwitchoverRequested=sleRedSwitchoverRequested, sleRedInfo=sleRedInfo, sleRedControlFaultTimeout=sleRedControlFaultTimeout, sleRedControlFaultCrashAction=sleRedControlFaultCrashAction, sleRedControl=sleRedControl)
