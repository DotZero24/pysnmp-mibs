#
# PySNMP MIB module OS-ETH-SERV-PROTECTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/mrv/OS-ETH-SERV-PROTECTION-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:26 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
oaOptiSwitch, OsCfmMepIdOrZero = mibBuilder.importSymbols("OS-COMMON-TC-MIB", "oaOptiSwitch", "OsCfmMepIdOrZero")
osEthServId, = mibBuilder.importSymbols("OS-ETH-SERV-MIB", "osEthServId")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, iso, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "iso", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention")
osEthServProtection = ModuleIdentity((1, 3, 6, 1, 4, 1, 6926, 2, 33))
osEthServProtection.setRevisions(('2013-01-21 00:00',))
if mibBuilder.loadTexts: osEthServProtection.setLastUpdated('201301210000Z')
if mibBuilder.loadTexts: osEthServProtection.setOrganization('MRV Communications, Inc.')
osEthServProtNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 33, 0))
osEthProtConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 33, 100))
osEthProtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 33, 100, 1))
osEthProtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 33, 100, 2))
class CcmTrackState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("disabled", 1), ("up", 2), ("down", 3))

class TrailSignalState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("normal", 2), ("fail", 3), ("degrade", 4))

class ElpCommand(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("unknown", 1), ("nothing", 2), ("clear", 3), ("lockout", 4), ("forcedSwitch", 5), ("manualSwitchWorking", 6), ("manualSwitchProtection", 7), ("exercise", 8), ("freeze", 9), ("clearFreeze", 10))

osEthServElpTable = MibTable((1, 3, 6, 1, 4, 1, 6926, 2, 33, 1), )
if mibBuilder.loadTexts: osEthServElpTable.setStatus('current')
osEthServElpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6926, 2, 33, 1, 1), ).setIndexNames((0, "OS-ETH-SERV-MIB", "osEthServId"))
if mibBuilder.loadTexts: osEthServElpEntry.setStatus('current')
osEthElpApsMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 33, 1, 1, 1), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osEthElpApsMacAddress.setStatus('current')
osEthElpTrackCcm = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 33, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("all", 2), ("onlyWorking", 3), ("onlyProtection", 4))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osEthElpTrackCcm.setStatus('current')
osEthElpRemoteMepIdWorking = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 33, 1, 1, 3), OsCfmMepIdOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osEthElpRemoteMepIdWorking.setStatus('current')
osEthElpRemoteMepIdProtection = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 33, 1, 1, 4), OsCfmMepIdOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osEthElpRemoteMepIdProtection.setStatus('current')
osEthElpHoldOffDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 33, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(100, 60000), ))).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: osEthElpHoldOffDelay.setStatus('current')
osEthElpRevertDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 33, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 0), ValueRangeConstraint(10, 86400000), )).clone(-1)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: osEthElpRevertDelay.setStatus('current')
osEthElpCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 33, 1, 1, 7), ElpCommand().clone('nothing')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osEthElpCommand.setStatus('current')
osEthElpActiveTrail = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 33, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("working", 1), ("protection", 2))).clone('working')).setMaxAccess("readonly")
if mibBuilder.loadTexts: osEthElpActiveTrail.setStatus('current')
osEthElpPendingCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 33, 1, 1, 21), ElpCommand().clone('nothing')).setMaxAccess("readonly")
if mibBuilder.loadTexts: osEthElpPendingCommand.setStatus('current')
osEthElpApsRxCount = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 33, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: osEthElpApsRxCount.setStatus('current')
osEthElpApsTxCount = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 33, 1, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: osEthElpApsTxCount.setStatus('current')
osEthElpFsmStateName = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 33, 1, 1, 24), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: osEthElpFsmStateName.setStatus('current')
osEthElpFarEndFsmStateName = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 33, 1, 1, 25), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: osEthElpFarEndFsmStateName.setStatus('current')
osEthElpTrackCcmStateWorking = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 33, 1, 1, 26), CcmTrackState().clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: osEthElpTrackCcmStateWorking.setStatus('current')
osEthElpTrackCcmStateProtection = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 33, 1, 1, 27), CcmTrackState().clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: osEthElpTrackCcmStateProtection.setStatus('current')
osEthElpTimeToRevert = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 33, 1, 1, 28), Integer32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: osEthElpTimeToRevert.setStatus('current')
osEthElpWorkingSignalState = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 33, 1, 1, 29), TrailSignalState().clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: osEthElpWorkingSignalState.setStatus('current')
osEthElpProtectionSignalState = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 33, 1, 1, 30), TrailSignalState().clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: osEthElpProtectionSignalState.setStatus('current')
osEthElpProtectionIndexName = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 33, 1, 1, 40), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: osEthElpProtectionIndexName.setStatus('current')
osEthElpAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 33, 1, 1, 98), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unknown", 1), ("nothing", 2), ("delete", 3), ("create", 4), ("enable", 5), ("disable", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osEthElpAdminStatus.setStatus('current')
osEthElpTrailSwitch = NotificationType((1, 3, 6, 1, 4, 1, 6926, 2, 33, 0, 1)).setObjects(("OS-ETH-SERV-PROTECTION-MIB", "osEthElpActiveTrail"), ("OS-ETH-SERV-PROTECTION-MIB", "osEthElpWorkingSignalState"), ("OS-ETH-SERV-PROTECTION-MIB", "osEthElpProtectionSignalState"))
if mibBuilder.loadTexts: osEthElpTrailSwitch.setStatus('current')
osEthProtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6926, 2, 33, 100, 1, 1)).setObjects(("OS-ETH-SERV-PROTECTION-MIB", "osEthProtectionMandatoryGroup"), ("OS-ETH-SERV-PROTECTION-MIB", "osEthProtectionNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    osEthProtMIBCompliance = osEthProtMIBCompliance.setStatus('current')
osEthProtectionMandatoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6926, 2, 33, 100, 2, 1)).setObjects(("OS-ETH-SERV-PROTECTION-MIB", "osEthElpAdminStatus"), ("OS-ETH-SERV-PROTECTION-MIB", "osEthElpApsMacAddress"), ("OS-ETH-SERV-PROTECTION-MIB", "osEthElpTrackCcm"), ("OS-ETH-SERV-PROTECTION-MIB", "osEthElpRemoteMepIdWorking"), ("OS-ETH-SERV-PROTECTION-MIB", "osEthElpRemoteMepIdProtection"), ("OS-ETH-SERV-PROTECTION-MIB", "osEthElpHoldOffDelay"), ("OS-ETH-SERV-PROTECTION-MIB", "osEthElpRevertDelay"), ("OS-ETH-SERV-PROTECTION-MIB", "osEthElpCommand"), ("OS-ETH-SERV-PROTECTION-MIB", "osEthElpActiveTrail"), ("OS-ETH-SERV-PROTECTION-MIB", "osEthElpPendingCommand"), ("OS-ETH-SERV-PROTECTION-MIB", "osEthElpApsRxCount"), ("OS-ETH-SERV-PROTECTION-MIB", "osEthElpApsTxCount"), ("OS-ETH-SERV-PROTECTION-MIB", "osEthElpFsmStateName"), ("OS-ETH-SERV-PROTECTION-MIB", "osEthElpFarEndFsmStateName"), ("OS-ETH-SERV-PROTECTION-MIB", "osEthElpTrackCcmStateWorking"), ("OS-ETH-SERV-PROTECTION-MIB", "osEthElpTrackCcmStateProtection"), ("OS-ETH-SERV-PROTECTION-MIB", "osEthElpTimeToRevert"), ("OS-ETH-SERV-PROTECTION-MIB", "osEthElpWorkingSignalState"), ("OS-ETH-SERV-PROTECTION-MIB", "osEthElpProtectionSignalState"), ("OS-ETH-SERV-PROTECTION-MIB", "osEthElpProtectionIndexName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    osEthProtectionMandatoryGroup = osEthProtectionMandatoryGroup.setStatus('current')
osEthProtectionNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6926, 2, 33, 100, 2, 2)).setObjects(("OS-ETH-SERV-PROTECTION-MIB", "osEthElpTrailSwitch"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    osEthProtectionNotificationsGroup = osEthProtectionNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("OS-ETH-SERV-PROTECTION-MIB", CcmTrackState=CcmTrackState, osEthProtMIBGroups=osEthProtMIBGroups, osEthElpFarEndFsmStateName=osEthElpFarEndFsmStateName, PYSNMP_MODULE_ID=osEthServProtection, osEthElpRevertDelay=osEthElpRevertDelay, osEthServElpEntry=osEthServElpEntry, osEthProtMIBCompliance=osEthProtMIBCompliance, osEthElpProtectionSignalState=osEthElpProtectionSignalState, TrailSignalState=TrailSignalState, osEthProtConformance=osEthProtConformance, osEthElpTrackCcmStateWorking=osEthElpTrackCcmStateWorking, osEthElpHoldOffDelay=osEthElpHoldOffDelay, osEthProtMIBCompliances=osEthProtMIBCompliances, osEthProtectionMandatoryGroup=osEthProtectionMandatoryGroup, osEthElpApsTxCount=osEthElpApsTxCount, osEthServElpTable=osEthServElpTable, osEthElpProtectionIndexName=osEthElpProtectionIndexName, osEthElpFsmStateName=osEthElpFsmStateName, osEthElpRemoteMepIdWorking=osEthElpRemoteMepIdWorking, osEthElpTrackCcmStateProtection=osEthElpTrackCcmStateProtection, osEthElpTrailSwitch=osEthElpTrailSwitch, osEthElpActiveTrail=osEthElpActiveTrail, osEthServProtection=osEthServProtection, ElpCommand=ElpCommand, osEthElpTimeToRevert=osEthElpTimeToRevert, osEthElpAdminStatus=osEthElpAdminStatus, osEthElpRemoteMepIdProtection=osEthElpRemoteMepIdProtection, osEthElpTrackCcm=osEthElpTrackCcm, osEthServProtNotifications=osEthServProtNotifications, osEthElpApsRxCount=osEthElpApsRxCount, osEthElpWorkingSignalState=osEthElpWorkingSignalState, osEthElpCommand=osEthElpCommand, osEthProtectionNotificationsGroup=osEthProtectionNotificationsGroup, osEthElpPendingCommand=osEthElpPendingCommand, osEthElpApsMacAddress=osEthElpApsMacAddress)
