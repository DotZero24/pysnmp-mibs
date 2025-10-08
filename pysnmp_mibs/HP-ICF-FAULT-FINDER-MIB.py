#
# PySNMP MIB module HP-ICF-FAULT-FINDER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/HP-ICF-FAULT-FINDER-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:02:48 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
PhysicalClass, PhysicalIndex = mibBuilder.importSymbols("ENTITY-MIB", "PhysicalClass", "PhysicalIndex")
hpicfCommon, hpicfCommonTrapsPrefix, hpicfObjectModules = mibBuilder.importSymbols("HP-ICF-OID", "hpicfCommon", "hpicfCommonTrapsPrefix", "hpicfObjectModules")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
TimeStamp, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "TextualConvention")
hpicfFaultFinderMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12))
hpicfFaultFinderMib.setRevisions(('2017-11-20 14:12', '2015-08-04 14:12', '2013-08-21 00:00', '2010-01-25 20:24', '2009-05-22 00:00', '2009-02-25 13:31', '2007-01-09 14:56', '2005-05-02 19:34', '2005-03-22 11:30', '2003-07-28 07:07', '2000-11-03 07:07', '1998-11-20 23:50', '1997-10-21 02:49',))
if mibBuilder.loadTexts: hpicfFaultFinderMib.setLastUpdated('201711201412Z')
if mibBuilder.loadTexts: hpicfFaultFinderMib.setOrganization('HP Networking')
hpicfFaultFinder = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7))
class HpicfFaultType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42))
    namedValues = NamedValues(("badDriver", 1), ("badXcvr", 2), ("badCable", 3), ("tooLongCable", 4), ("overBandwidth", 5), ("bcastStorm", 6), ("partition", 7), ("misconfiguredSQE", 8), ("polarityReversal", 9), ("networkLoop", 10), ("lossOfLink", 11), ("portSecurityViolation", 12), ("backupLinkTransition", 13), ("meshingFault", 14), ("fanFault", 15), ("rpsFault", 16), ("stuck10MbFault", 17), ("lossOfStackMember", 18), ("hotSwapReboot", 19), ("duplexMismatchHDX", 20), ("duplexMismatchFDX", 21), ("flowcntlJumbosFault", 22), ("portSelftestFailure", 23), ("xcvrUnidentified", 24), ("xcvrUnsupported", 25), ("crfNotify", 26), ("crfThrottled", 27), ("crfBlocked", 28), ("xcvrNotYetSupported", 29), ("xcvrBRevOnly", 30), ("xcvrNotSupportedOnPort", 31), ("phyReadFailure", 32), ("linkFlap", 33), ("intel82566dmportprotect", 34), ("xcvrExceedQty", 35), ("xcvrClone", 36), ("xcvrCloneReminder", 37), ("bcastStormPerPort", 38), ("linkFlapPerPort", 39), ("rxNonStdPreamble", 40), ("mcastStorm", 41), ("mcastStormPerPort", 42))

class HpicfFaultTolerance(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class HpicfFaultAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("none", 1), ("warn", 2), ("warnAndDisable", 3), ("warnAndSpeedReduce", 4), ("warnAndSpeedReduceAndDisable", 5))

class HpicfUrlString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

hpicfFfControlTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 1), )
if mibBuilder.loadTexts: hpicfFfControlTable.setStatus('current')
hpicfFfControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 1, 1), ).setIndexNames((0, "HP-ICF-FAULT-FINDER-MIB", "hpicfFfControlIndex"))
if mibBuilder.loadTexts: hpicfFfControlEntry.setStatus('current')
hpicfFfControlIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 1, 1, 1), HpicfFaultType())
if mibBuilder.loadTexts: hpicfFfControlIndex.setStatus('current')
hpicfFfAction = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 1, 1, 2), HpicfFaultAction()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfFfAction.setStatus('current')
hpicfFfWarnTolerance = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 1, 1, 3), HpicfFaultTolerance()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfFfWarnTolerance.setStatus('current')
hpicfFfDisablePortTolerance = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 1, 1, 4), HpicfFaultTolerance()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfFfDisablePortTolerance.setStatus('current')
hpicfFfSpeedReduceTolerance = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 1, 1, 5), HpicfFaultTolerance()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfFfSpeedReduceTolerance.setStatus('current')
hpicfFfLogTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 2), )
if mibBuilder.loadTexts: hpicfFfLogTable.setStatus('current')
hpicfFfLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 2, 1), ).setIndexNames((0, "HP-ICF-FAULT-FINDER-MIB", "hpicfFfLogIndex"))
if mibBuilder.loadTexts: hpicfFfLogEntry.setStatus('current')
hpicfFfLogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hpicfFfLogIndex.setStatus('current')
hpicfFfLogCreateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 2, 1, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfFfLogCreateTime.setStatus('current')
hpicfFfLogPhysEntity = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 2, 1, 3), PhysicalIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfFfLogPhysEntity.setStatus('current')
hpicfFfLogFaultType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 2, 1, 4), HpicfFaultType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfFfLogFaultType.setStatus('current')
hpicfFfLogAction = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 2, 1, 5), HpicfFaultAction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfFfLogAction.setStatus('current')
hpicfFfLogSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("informational", 1), ("medium", 2), ("critical", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfFfLogSeverity.setStatus('current')
hpicfFfLogStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("new", 1), ("active", 2), ("old", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfFfLogStatus.setStatus('current')
hpicfFfLogPhysClass = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 2, 1, 8), PhysicalClass()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfFfLogPhysClass.setStatus('current')
hpicfFfLogInfoType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ipv4Address", 1), ("displayString", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfFfLogInfoType.setStatus('current')
hpicfFfLogInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 2, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfFfLogInfo.setStatus('current')
hpicfFfFaultInfoURL = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 3), HpicfUrlString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpicfFfFaultInfoURL.setStatus('current')
hpicfFfFaultLightStatus = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("faultLightOff", 1), ("faultLightOn", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfFfFaultLightStatus.setStatus('current')
hpicfFfBcastStormControlPortConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 5))
hpicfFfBcastStormControlPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 5, 1), )
if mibBuilder.loadTexts: hpicfFfBcastStormControlPortConfigTable.setStatus('current')
hpicfFfBcastStormControlPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 5, 1, 1), ).setIndexNames((0, "HP-ICF-FAULT-FINDER-MIB", "hpicfFfBcastStormControlPortIndex"))
if mibBuilder.loadTexts: hpicfFfBcastStormControlPortConfigEntry.setStatus('current')
hpicfFfBcastStormControlPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 5, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hpicfFfBcastStormControlPortIndex.setStatus('current')
hpicfFfBcastStormControlMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("bcastRisingLevelpercent", 2), ("bcastRisingLevelpps", 3))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfFfBcastStormControlMode.setStatus('current')
hpicfFfBcastStormControlRisingpercent = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfFfBcastStormControlRisingpercent.setStatus('current')
hpicfFfBcastStormControlRisingpps = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 5, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfFfBcastStormControlRisingpps.setStatus('current')
hpicfFfBcastStormControlAction = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 5, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("warn", 2), ("warnAndDisable", 3))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfFfBcastStormControlAction.setStatus('current')
hpicfFfBcastStormControlPortDisableTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 5, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 604800))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfFfBcastStormControlPortDisableTimer.setStatus('current')
hpicfFfLinkFlapControlPortConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 6))
hpicfFfLinkFlapControlPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 6, 1), )
if mibBuilder.loadTexts: hpicfFfLinkFlapControlPortConfigTable.setStatus('current')
hpicfFfLinkFlapControlPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 6, 1, 1), ).setIndexNames((0, "HP-ICF-FAULT-FINDER-MIB", "hpicfFfLinkFlapControlPortIndex"))
if mibBuilder.loadTexts: hpicfFfLinkFlapControlPortConfigEntry.setStatus('current')
hpicfFfLinkFlapControlPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 6, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hpicfFfLinkFlapControlPortIndex.setStatus('current')
hpicfFfLinkFlapControlSensitivity = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 6, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 3, 6, 10))).clone(namedValues=NamedValues(("none", 0), ("high", 3), ("medium", 6), ("low", 10))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfFfLinkFlapControlSensitivity.setStatus('current')
hpicfFfLinkFlapControlAction = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 6, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("warn", 2), ("warnAndDisable", 3))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfFfLinkFlapControlAction.setStatus('current')
hpicfFfLinkFlapControlPortDisableTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 6, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 604800))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfFfLinkFlapControlPortDisableTimer.setStatus('current')
hpicfFfMcastStormPortConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 7))
hpicfFfMcastStormPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 7, 1), )
if mibBuilder.loadTexts: hpicfFfMcastStormPortConfigTable.setStatus('current')
hpicfFfMcastStormPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 7, 1, 1), ).setIndexNames((0, "HP-ICF-FAULT-FINDER-MIB", "hpicfFfMcastStormPortIndex"))
if mibBuilder.loadTexts: hpicfFfMcastStormPortConfigEntry.setStatus('current')
hpicfFfMcastStormPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 7, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hpicfFfMcastStormPortIndex.setStatus('current')
hpicfFfMcastStormMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 7, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("mcastRisingLevelpercent", 2), ("mcastRisingLevelpps", 3))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfFfMcastStormMode.setStatus('current')
hpicfFfMcastStormRisingpercent = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 7, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfFfMcastStormRisingpercent.setStatus('current')
hpicfFfMcastStormRisingpps = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 7, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfFfMcastStormRisingpps.setStatus('current')
hpicfFfMcastStormAction = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 7, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("warn", 2), ("warnAndDisable", 3))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfFfMcastStormAction.setStatus('current')
hpicfFfMcastStormPortDisablTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 7, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 604800))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfFfMcastStormPortDisablTimer.setStatus('current')
hpicfFaultFinderTrap = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 12, 1, 0, 5)).setObjects(("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLogFaultType"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLogAction"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLogSeverity"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfFaultInfoURL"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLogPhysEntity"))
if mibBuilder.loadTexts: hpicfFaultFinderTrap.setStatus('current')
hpicfFaultFinderConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1))
hpicfFaultFinderCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 1))
hpicfFaultFinderGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 2))
hpicfFaultFinderCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 1, 1)).setObjects(("HP-ICF-FAULT-FINDER-MIB", "hpicfFaultConfigGroup"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFaultLogGroup"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFaultNotifyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfFaultFinderCompliance = hpicfFaultFinderCompliance.setStatus('current')
hpicfFaultFinder2Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 1, 2)).setObjects(("HP-ICF-FAULT-FINDER-MIB", "hpicfFaultConfig2Group"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFaultLogGroup"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFaultNotifyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfFaultFinder2Compliance = hpicfFaultFinder2Compliance.setStatus('current')
hpicfFaultStatusCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 1, 3)).setObjects(("HP-ICF-FAULT-FINDER-MIB", "hpicfFaultStatusGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfFaultStatusCompliance = hpicfFaultStatusCompliance.setStatus('current')
hpicfFaultFinder3Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 1, 4)).setObjects(("HP-ICF-FAULT-FINDER-MIB", "hpicfFaultConfig3Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfFaultFinder3Compliance = hpicfFaultFinder3Compliance.setStatus('current')
hpicfFaultFinder4Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 1, 5)).setObjects(("HP-ICF-FAULT-FINDER-MIB", "hpicfFaultConfig4Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfFaultFinder4Compliance = hpicfFaultFinder4Compliance.setStatus('current')
hpicfFaultFinder5Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 1, 6)).setObjects(("HP-ICF-FAULT-FINDER-MIB", "hpicfFaultConfig5Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfFaultFinder5Compliance = hpicfFaultFinder5Compliance.setStatus('current')
hpicfFaultConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 2, 1)).setObjects(("HP-ICF-FAULT-FINDER-MIB", "hpicfFfAction"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfWarnTolerance"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfDisablePortTolerance"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfFaultConfigGroup = hpicfFaultConfigGroup.setStatus('current')
hpicfFaultLogGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 2, 2)).setObjects(("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLogCreateTime"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLogPhysEntity"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLogFaultType"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLogAction"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLogSeverity"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLogStatus"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfFaultInfoURL"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLogPhysClass"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLogInfoType"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLogInfo"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfFaultLogGroup = hpicfFaultLogGroup.setStatus('current')
hpicfFaultNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 2, 3)).setObjects(("HP-ICF-FAULT-FINDER-MIB", "hpicfFaultFinderTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfFaultNotifyGroup = hpicfFaultNotifyGroup.setStatus('current')
hpicfFaultConfig2Group = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 2, 4)).setObjects(("HP-ICF-FAULT-FINDER-MIB", "hpicfFfAction"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfWarnTolerance"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfDisablePortTolerance"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfSpeedReduceTolerance"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfFaultConfig2Group = hpicfFaultConfig2Group.setStatus('current')
hpicfFaultStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 2, 5)).setObjects(("HP-ICF-FAULT-FINDER-MIB", "hpicfFfFaultLightStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfFaultStatusGroup = hpicfFaultStatusGroup.setStatus('current')
hpicfFaultConfig3Group = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 2, 6)).setObjects(("HP-ICF-FAULT-FINDER-MIB", "hpicfFfBcastStormControlMode"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfBcastStormControlRisingpercent"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfBcastStormControlRisingpps"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfBcastStormControlAction"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfBcastStormControlPortDisableTimer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfFaultConfig3Group = hpicfFaultConfig3Group.setStatus('current')
hpicfFaultConfig4Group = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 2, 7)).setObjects(("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLinkFlapControlSensitivity"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLinkFlapControlAction"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLinkFlapControlPortDisableTimer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfFaultConfig4Group = hpicfFaultConfig4Group.setStatus('current')
hpicfFaultConfig5Group = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 2, 8)).setObjects(("HP-ICF-FAULT-FINDER-MIB", "hpicfFfMcastStormMode"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfMcastStormRisingpercent"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfMcastStormRisingpps"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfMcastStormAction"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfMcastStormPortDisablTimer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfFaultConfig5Group = hpicfFaultConfig5Group.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-FAULT-FINDER-MIB", hpicfFfMcastStormAction=hpicfFfMcastStormAction, hpicfFaultFinderGroups=hpicfFaultFinderGroups, hpicfFfMcastStormMode=hpicfFfMcastStormMode, hpicfFfBcastStormControlRisingpps=hpicfFfBcastStormControlRisingpps, hpicfFaultFinder5Compliance=hpicfFaultFinder5Compliance, hpicfFaultFinderMib=hpicfFaultFinderMib, hpicfFaultFinder3Compliance=hpicfFaultFinder3Compliance, hpicfFfLinkFlapControlPortConfigTable=hpicfFfLinkFlapControlPortConfigTable, hpicfFfLinkFlapControlPortDisableTimer=hpicfFfLinkFlapControlPortDisableTimer, hpicfFfBcastStormControlRisingpercent=hpicfFfBcastStormControlRisingpercent, hpicfFaultNotifyGroup=hpicfFaultNotifyGroup, hpicfFfControlIndex=hpicfFfControlIndex, hpicfFfAction=hpicfFfAction, hpicfFfLinkFlapControlPortConfigEntry=hpicfFfLinkFlapControlPortConfigEntry, hpicfFaultLogGroup=hpicfFaultLogGroup, hpicfFfLinkFlapControlPortConfig=hpicfFfLinkFlapControlPortConfig, hpicfFaultFinderCompliances=hpicfFaultFinderCompliances, HpicfFaultType=HpicfFaultType, HpicfFaultTolerance=HpicfFaultTolerance, hpicfFfLogPhysClass=hpicfFfLogPhysClass, hpicfFfLogTable=hpicfFfLogTable, hpicfFfLogStatus=hpicfFfLogStatus, hpicfFfBcastStormControlAction=hpicfFfBcastStormControlAction, hpicfFfMcastStormRisingpercent=hpicfFfMcastStormRisingpercent, hpicfFaultConfig3Group=hpicfFaultConfig3Group, hpicfFfLogFaultType=hpicfFfLogFaultType, hpicfFfMcastStormPortConfigEntry=hpicfFfMcastStormPortConfigEntry, HpicfUrlString=HpicfUrlString, PYSNMP_MODULE_ID=hpicfFaultFinderMib, hpicfFfLogInfo=hpicfFfLogInfo, hpicfFfWarnTolerance=hpicfFfWarnTolerance, hpicfFfLogEntry=hpicfFfLogEntry, hpicfFfControlTable=hpicfFfControlTable, hpicfFfFaultInfoURL=hpicfFfFaultInfoURL, hpicfFfBcastStormControlPortConfigEntry=hpicfFfBcastStormControlPortConfigEntry, hpicfFfBcastStormControlPortConfig=hpicfFfBcastStormControlPortConfig, hpicfFaultFinder2Compliance=hpicfFaultFinder2Compliance, hpicfFfLinkFlapControlAction=hpicfFfLinkFlapControlAction, hpicfFaultConfigGroup=hpicfFaultConfigGroup, hpicfFfLogSeverity=hpicfFfLogSeverity, hpicfFaultStatusGroup=hpicfFaultStatusGroup, hpicfFaultConfig2Group=hpicfFaultConfig2Group, hpicfFaultConfig5Group=hpicfFaultConfig5Group, hpicfFfBcastStormControlPortIndex=hpicfFfBcastStormControlPortIndex, HpicfFaultAction=HpicfFaultAction, hpicfFfLogInfoType=hpicfFfLogInfoType, hpicfFfBcastStormControlPortConfigTable=hpicfFfBcastStormControlPortConfigTable, hpicfFfLogPhysEntity=hpicfFfLogPhysEntity, hpicfFaultFinder=hpicfFaultFinder, hpicfFaultFinderCompliance=hpicfFaultFinderCompliance, hpicfFfMcastStormPortDisablTimer=hpicfFfMcastStormPortDisablTimer, hpicfFaultStatusCompliance=hpicfFaultStatusCompliance, hpicfFfDisablePortTolerance=hpicfFfDisablePortTolerance, hpicfFfFaultLightStatus=hpicfFfFaultLightStatus, hpicfFfLogCreateTime=hpicfFfLogCreateTime, hpicfFfLogAction=hpicfFfLogAction, hpicfFaultFinderConformance=hpicfFaultFinderConformance, hpicfFfBcastStormControlPortDisableTimer=hpicfFfBcastStormControlPortDisableTimer, hpicfFfMcastStormPortConfig=hpicfFfMcastStormPortConfig, hpicfFfMcastStormRisingpps=hpicfFfMcastStormRisingpps, hpicfFfLogIndex=hpicfFfLogIndex, hpicfFaultFinderTrap=hpicfFaultFinderTrap, hpicfFfMcastStormPortConfigTable=hpicfFfMcastStormPortConfigTable, hpicfFaultFinder4Compliance=hpicfFaultFinder4Compliance, hpicfFaultConfig4Group=hpicfFaultConfig4Group, hpicfFfLinkFlapControlPortIndex=hpicfFfLinkFlapControlPortIndex, hpicfFfLinkFlapControlSensitivity=hpicfFfLinkFlapControlSensitivity, hpicfFfBcastStormControlMode=hpicfFfBcastStormControlMode, hpicfFfControlEntry=hpicfFfControlEntry, hpicfFfSpeedReduceTolerance=hpicfFfSpeedReduceTolerance, hpicfFfMcastStormPortIndex=hpicfFfMcastStormPortIndex)
