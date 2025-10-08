#
# PySNMP MIB module ALU-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/nokia/ALU-SYSTEM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:20:47 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
aluHwObjs, = mibBuilder.importSymbols("ALU-CHASSIS-MIB", "aluHwObjs")
aluSARMIBModules, aluSARConfs, aluSARNotifyPrefix, aluSARObjs = mibBuilder.importSymbols("ALU-SAR-GLOBAL-MIB", "aluSARMIBModules", "aluSARConfs", "aluSARNotifyPrefix", "aluSARObjs")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TimeStamp, RowStatus, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp", "RowStatus", "TruthValue", "TextualConvention")
TmnxAdminState, TPortSchedulerPIR = mibBuilder.importSymbols("TIMETRA-TC-MIB", "TmnxAdminState", "TPortSchedulerPIR")
aluSystemMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 1, 3, 13))
aluSystemMIBModule.setRevisions(('1911-06-14 00:00', '1914-02-10 00:00',))
if mibBuilder.loadTexts: aluSystemMIBModule.setLastUpdated('1402100000Z')
if mibBuilder.loadTexts: aluSystemMIBModule.setOrganization('Nokia')
aluSystemObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13))
aluSystemMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 13))
aluSystemNotifyPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 9))
aluSystemNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 9, 0))
aluSystemNotificationObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 8))
class AluTod1PpsMessageType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("none", 0), ("cm", 1), ("ct", 2), ("irig-b000-b120", 3), ("irig-b001-b121", 4), ("irig-b002-b122", 5), ("irig-b003-b123", 6), ("irig-b004-b124", 7), ("irig-b005-b125", 8), ("irig-b006-b126", 9), ("irig-b007-b127", 10))

class AluSysTimePriorityType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))
    namedValues = NamedValues(("none", 0), ("priority1", 1), ("priority2", 2), ("priority3", 3), ("priority4", 4), ("priority5", 5), ("priority6", 6), ("priority7", 7), ("priority8", 8), ("priority9", 9), ("priority10", 10), ("priority11", 11), ("priority12", 12), ("priority13", 13), ("priority14", 14), ("priority15", 15), ("priority16", 16), ("priority17", 17), ("holdover", 18))

class AluSysTimeRefLeapSecSchedType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("notScheduled", 0), ("forwardScheduled", 1), ("backwardScheduled", 2))

class AluSysTimeReferenceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("notApplic", 0), ("gnss", 1), ("ptp", 2), ("ntp", 3), ("sntp", 4), ("holdover", 5))

class AluSysTimeReferenceId(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

aluTod1PpsInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 1))
aluTod1PpsMessageType = MibScalar((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 1, 1), AluTod1PpsMessageType().clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aluTod1PpsMessageType.setStatus('current')
aluTod1PpsOutput = MibScalar((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 1, 2), TmnxAdminState().clone('outOfService')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aluTod1PpsOutput.setStatus('current')
aluTod1PpsInput = MibScalar((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 1, 3), TmnxAdminState().clone('outOfService')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aluTod1PpsInput.setStatus('current')
aluNtpSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 2))
aluNtpMdaTimestamp = MibScalar((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 2, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aluNtpMdaTimestamp.setStatus('current')
aluSysTimeSelector = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 3))
aluActiveTimeSourceType = MibScalar((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 3, 1), AluSysTimeReferenceType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aluActiveTimeSourceType.setStatus('current')
aluActiveTimeSourceId = MibScalar((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 3, 2), AluSysTimeReferenceId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aluActiveTimeSourceId.setStatus('current')
aluActiveTimeSourceChange = MibScalar((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 3, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aluActiveTimeSourceChange.setStatus('current')
aluTimeSelectorTable = MibTable((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 3, 4), )
if mibBuilder.loadTexts: aluTimeSelectorTable.setStatus('current')
aluTimeReferenceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 3, 4, 1), ).setIndexNames((0, "ALU-SYSTEM-MIB", "timeRefType"), (0, "ALU-SYSTEM-MIB", "timeRefId"))
if mibBuilder.loadTexts: aluTimeReferenceEntry.setStatus('current')
timeRefType = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 3, 4, 1, 1), AluSysTimeReferenceType())
if mibBuilder.loadTexts: timeRefType.setStatus('current')
timeRefId = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 3, 4, 1, 2), AluSysTimeReferenceId())
if mibBuilder.loadTexts: timeRefId.setStatus('current')
timeRefPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 3, 4, 1, 3), AluSysTimePriorityType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRefPriority.setStatus('current')
timeRefRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 3, 4, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRefRowStatus.setStatus('current')
timeRefQualified = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 3, 4, 1, 5), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: timeRefQualified.setStatus('current')
timeRefQualifiedChange = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 3, 4, 1, 6), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timeRefQualifiedChange.setStatus('current')
timeRefPropertiesUpdate = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 3, 4, 1, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timeRefPropertiesUpdate.setStatus('current')
timeRefDeltaSec = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 3, 4, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timeRefDeltaSec.setStatus('current')
timeRefDeltaNs = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 3, 4, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timeRefDeltaNs.setStatus('current')
timeRefLeapSecSched = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 3, 4, 1, 10), AluSysTimeRefLeapSecSchedType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timeRefLeapSecSched.setStatus('current')
timeRefLeapSecValid = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 3, 4, 1, 11), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: timeRefLeapSecValid.setStatus('obsolete')
timeRefLeapSec = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 3, 4, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timeRefLeapSec.setStatus('obsolete')
timeRefLeapSecUpdTime = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 3, 4, 1, 13), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timeRefLeapSecUpdTime.setStatus('current')
aluSystemSptConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 4))
aluSystemSptSecAggRate = MibScalar((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 13, 4, 1), TPortSchedulerPIR().clone(50000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aluSystemSptSecAggRate.setStatus('current')
aluSystemNotifyTimeRefType = MibScalar((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 8, 1), AluSysTimeReferenceType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: aluSystemNotifyTimeRefType.setStatus('current')
aluSystemNotifyTimeRefId = MibScalar((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 8, 2), AluSysTimeReferenceId()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: aluSystemNotifyTimeRefId.setStatus('current')
aluTimeRefCreated = NotificationType((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 9, 0, 1)).setObjects(("ALU-SYSTEM-MIB", "aluSystemNotifyTimeRefType"), ("ALU-SYSTEM-MIB", "aluSystemNotifyTimeRefId"), ("ALU-SYSTEM-MIB", "timeRefPriority"))
if mibBuilder.loadTexts: aluTimeRefCreated.setStatus('current')
aluTimeRefDeleted = NotificationType((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 9, 0, 2)).setObjects(("ALU-SYSTEM-MIB", "aluSystemNotifyTimeRefType"), ("ALU-SYSTEM-MIB", "aluSystemNotifyTimeRefId"))
if mibBuilder.loadTexts: aluTimeRefDeleted.setStatus('current')
aluTimeRefQualified = NotificationType((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 9, 0, 3)).setObjects(("ALU-SYSTEM-MIB", "aluSystemNotifyTimeRefType"), ("ALU-SYSTEM-MIB", "aluSystemNotifyTimeRefId"))
if mibBuilder.loadTexts: aluTimeRefQualified.setStatus('current')
aluTimeRefDisqualified = NotificationType((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 9, 0, 4)).setObjects(("ALU-SYSTEM-MIB", "aluSystemNotifyTimeRefType"), ("ALU-SYSTEM-MIB", "aluSystemNotifyTimeRefId"))
if mibBuilder.loadTexts: aluTimeRefDisqualified.setStatus('current')
aluTimeRefSelect = NotificationType((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 9, 0, 5)).setObjects(("ALU-SYSTEM-MIB", "aluSystemNotifyTimeRefType"), ("ALU-SYSTEM-MIB", "aluSystemNotifyTimeRefId"))
if mibBuilder.loadTexts: aluTimeRefSelect.setStatus('current')
aluSystemMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 13, 1))
aluSystemMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 13, 2))
aluSystemMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 13, 1, 1)).setObjects(("ALU-SYSTEM-MIB", "aluTod1PpsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aluSystemMIBCompliance = aluSystemMIBCompliance.setStatus('obsolete')
aluSystemV6v1MIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 13, 1, 2)).setObjects(("ALU-SYSTEM-MIB", "aluTod1PpsGroup"), ("ALU-SYSTEM-MIB", "aluNtpMdaTimestamp"), ("ALU-SYSTEM-MIB", "aluSysTimeReferenceGroup"), ("ALU-SYSTEM-MIB", "aluSysTimeNotificationV6v1Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aluSystemV6v1MIBCompliance = aluSystemV6v1MIBCompliance.setStatus('obsolete')
aluSystemV7v0MIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 13, 1, 3)).setObjects(("ALU-SYSTEM-MIB", "aluTod1PpsGroup"), ("ALU-SYSTEM-MIB", "aluNtpMdaTimestamp"), ("ALU-SYSTEM-MIB", "aluSysTimeReferenceGroup"), ("ALU-SYSTEM-MIB", "aluSysTimeNotificationV6v1Group"), ("ALU-SYSTEM-MIB", "aluSystemSptGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aluSystemV7v0MIBCompliance = aluSystemV7v0MIBCompliance.setStatus('current')
aluTod1PpsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 13, 2, 1)).setObjects(("ALU-SYSTEM-MIB", "aluTod1PpsMessageType"), ("ALU-SYSTEM-MIB", "aluTod1PpsOutput"), ("ALU-SYSTEM-MIB", "aluTod1PpsInput"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aluTod1PpsGroup = aluTod1PpsGroup.setStatus('current')
aluNtpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 13, 2, 2)).setObjects(("ALU-SYSTEM-MIB", "aluNtpMdaTimestamp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aluNtpGroup = aluNtpGroup.setStatus('current')
aluSysTimeReferenceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 13, 2, 3)).setObjects(("ALU-SYSTEM-MIB", "aluActiveTimeSourceType"), ("ALU-SYSTEM-MIB", "aluActiveTimeSourceId"), ("ALU-SYSTEM-MIB", "aluActiveTimeSourceChange"), ("ALU-SYSTEM-MIB", "timeRefPriority"), ("ALU-SYSTEM-MIB", "timeRefRowStatus"), ("ALU-SYSTEM-MIB", "timeRefQualified"), ("ALU-SYSTEM-MIB", "timeRefQualifiedChange"), ("ALU-SYSTEM-MIB", "timeRefPropertiesUpdate"), ("ALU-SYSTEM-MIB", "timeRefDeltaSec"), ("ALU-SYSTEM-MIB", "timeRefDeltaNs"), ("ALU-SYSTEM-MIB", "timeRefLeapSecSched"), ("ALU-SYSTEM-MIB", "timeRefLeapSecValid"), ("ALU-SYSTEM-MIB", "timeRefLeapSec"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aluSysTimeReferenceGroup = aluSysTimeReferenceGroup.setStatus('current')
aluSysTimeNotifyObjsV6v1Group = ObjectGroup((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 13, 2, 4)).setObjects(("ALU-SYSTEM-MIB", "aluSystemNotifyTimeRefId"), ("ALU-SYSTEM-MIB", "aluSystemNotifyTimeRefType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aluSysTimeNotifyObjsV6v1Group = aluSysTimeNotifyObjsV6v1Group.setStatus('current')
aluSysTimeNotificationV6v1Group = NotificationGroup((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 13, 2, 5)).setObjects(("ALU-SYSTEM-MIB", "aluTimeRefCreated"), ("ALU-SYSTEM-MIB", "aluTimeRefDeleted"), ("ALU-SYSTEM-MIB", "aluTimeRefQualified"), ("ALU-SYSTEM-MIB", "aluTimeRefDisqualified"), ("ALU-SYSTEM-MIB", "aluTimeRefSelect"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aluSysTimeNotificationV6v1Group = aluSysTimeNotificationV6v1Group.setStatus('current')
aluSysTimeReferenceV6v1Group = ObjectGroup((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 13, 2, 6)).setObjects(("ALU-SYSTEM-MIB", "aluActiveTimeSourceType"), ("ALU-SYSTEM-MIB", "aluActiveTimeSourceId"), ("ALU-SYSTEM-MIB", "aluActiveTimeSourceChange"), ("ALU-SYSTEM-MIB", "timeRefPriority"), ("ALU-SYSTEM-MIB", "timeRefRowStatus"), ("ALU-SYSTEM-MIB", "timeRefQualified"), ("ALU-SYSTEM-MIB", "timeRefQualifiedChange"), ("ALU-SYSTEM-MIB", "timeRefPropertiesUpdate"), ("ALU-SYSTEM-MIB", "timeRefDeltaSec"), ("ALU-SYSTEM-MIB", "timeRefDeltaNs"), ("ALU-SYSTEM-MIB", "timeRefLeapSecSched"), ("ALU-SYSTEM-MIB", "timeRefLeapSecUpdTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aluSysTimeReferenceV6v1Group = aluSysTimeReferenceV6v1Group.setStatus('current')
aluSysTimeReferenceObsoleteGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 13, 2, 7)).setObjects(("ALU-SYSTEM-MIB", "timeRefLeapSecValid"), ("ALU-SYSTEM-MIB", "timeRefLeapSec"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aluSysTimeReferenceObsoleteGroup = aluSysTimeReferenceObsoleteGroup.setStatus('current')
aluSystemSptGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 13, 2, 8)).setObjects(("ALU-SYSTEM-MIB", "aluSystemSptSecAggRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aluSystemSptGroup = aluSystemSptGroup.setStatus('current')
mibBuilder.exportSymbols("ALU-SYSTEM-MIB", aluActiveTimeSourceType=aluActiveTimeSourceType, aluSystemMIBCompliances=aluSystemMIBCompliances, timeRefPropertiesUpdate=timeRefPropertiesUpdate, aluSysTimeReferenceV6v1Group=aluSysTimeReferenceV6v1Group, aluSysTimeReferenceGroup=aluSysTimeReferenceGroup, aluSysTimeNotificationV6v1Group=aluSysTimeNotificationV6v1Group, aluActiveTimeSourceId=aluActiveTimeSourceId, timeRefDeltaSec=timeRefDeltaSec, aluNtpMdaTimestamp=aluNtpMdaTimestamp, aluNtpSystem=aluNtpSystem, aluSysTimeSelector=aluSysTimeSelector, aluSysTimeNotifyObjsV6v1Group=aluSysTimeNotifyObjsV6v1Group, timeRefLeapSecUpdTime=timeRefLeapSecUpdTime, timeRefQualifiedChange=timeRefQualifiedChange, aluTimeRefDeleted=aluTimeRefDeleted, aluTimeReferenceEntry=aluTimeReferenceEntry, aluSystemMIBGroups=aluSystemMIBGroups, aluTimeRefQualified=aluTimeRefQualified, aluSystemV6v1MIBCompliance=aluSystemV6v1MIBCompliance, PYSNMP_MODULE_ID=aluSystemMIBModule, aluSystemNotification=aluSystemNotification, aluTimeSelectorTable=aluTimeSelectorTable, aluTod1PpsOutput=aluTod1PpsOutput, aluSystemSptSecAggRate=aluSystemSptSecAggRate, timeRefLeapSec=timeRefLeapSec, aluSystemSptConfig=aluSystemSptConfig, aluActiveTimeSourceChange=aluActiveTimeSourceChange, timeRefRowStatus=timeRefRowStatus, aluSystemNotifyTimeRefType=aluSystemNotifyTimeRefType, AluSysTimePriorityType=AluSysTimePriorityType, aluTimeRefDisqualified=aluTimeRefDisqualified, aluSystemV7v0MIBCompliance=aluSystemV7v0MIBCompliance, AluSysTimeReferenceType=AluSysTimeReferenceType, timeRefType=timeRefType, timeRefDeltaNs=timeRefDeltaNs, aluTod1PpsInfo=aluTod1PpsInfo, timeRefLeapSecSched=timeRefLeapSecSched, aluTod1PpsMessageType=aluTod1PpsMessageType, aluTod1PpsGroup=aluTod1PpsGroup, aluSystemMIBConformance=aluSystemMIBConformance, aluSysTimeReferenceObsoleteGroup=aluSysTimeReferenceObsoleteGroup, timeRefPriority=timeRefPriority, AluSysTimeReferenceId=AluSysTimeReferenceId, timeRefQualified=timeRefQualified, timeRefLeapSecValid=timeRefLeapSecValid, aluSystemNotifyTimeRefId=aluSystemNotifyTimeRefId, aluNtpGroup=aluNtpGroup, AluTod1PpsMessageType=AluTod1PpsMessageType, aluTimeRefSelect=aluTimeRefSelect, aluSystemMIBCompliance=aluSystemMIBCompliance, aluSystemNotificationObjs=aluSystemNotificationObjs, aluSystemSptGroup=aluSystemSptGroup, aluTimeRefCreated=aluTimeRefCreated, AluSysTimeRefLeapSecSchedType=AluSysTimeRefLeapSecSchedType, aluSystemObjs=aluSystemObjs, aluSystemMIBModule=aluSystemMIBModule, timeRefId=timeRefId, aluSystemNotifyPrefix=aluSystemNotifyPrefix, aluTod1PpsInput=aluTod1PpsInput)
