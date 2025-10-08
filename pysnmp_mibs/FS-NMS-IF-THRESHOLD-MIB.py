#
# PySNMP MIB module FS-NMS-IF-THRESHOLD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/fscom/FS-NMS-IF-THRESHOLD-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:58:24 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
nmsMgmt, = mibBuilder.importSymbols("FS-NMS-SMI", "nmsMgmt")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TimeStamp, RowStatus, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp", "RowStatus", "TruthValue", "TextualConvention")
nmsIfThresholdMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 52642, 9, 218))
nmsIfThresholdMIB.setRevisions(('2003-10-16 00:00',))
if mibBuilder.loadTexts: nmsIfThresholdMIB.setLastUpdated('200310160000Z')
if mibBuilder.loadTexts: nmsIfThresholdMIB.setOrganization('')
class NMSifthTemplateIndex(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 1000)

class NMSifthTemplateIndexOrZero(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 1000)

class NMSifthThresholdIndex(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 63)

class NMSifthThresholdList(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 8)

class NMSifthThresholdSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("fail", 1), ("degrade", 2), ("info", 3), ("other", 4))

class NMSifthThresholdSeverityOrZero(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4)

nmsIfThresholdMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 9, 218, 1))
nmsifthTemplateGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 9, 218, 1, 1))
nmsifthTemplateIfAssignGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 9, 218, 1, 2))
nmsifthIfThresholdFiredGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 9, 218, 1, 3))
nmsifthTemplateIndexNext = MibScalar((1, 3, 6, 1, 4, 1, 52642, 9, 218, 1, 1, 1), NMSifthTemplateIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsifthTemplateIndexNext.setStatus('current')
nmsifthTemplateLastChange = MibScalar((1, 3, 6, 1, 4, 1, 52642, 9, 218, 1, 1, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsifthTemplateLastChange.setStatus('current')
nmsifthTemplateTable = MibTable((1, 3, 6, 1, 4, 1, 52642, 9, 218, 1, 1, 3), )
if mibBuilder.loadTexts: nmsifthTemplateTable.setStatus('current')
nmsifthTemplateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52642, 9, 218, 1, 1, 3, 1), ).setIndexNames((0, "FS-NMS-IF-THRESHOLD-MIB", "nmsifthTemplateIndex"))
if mibBuilder.loadTexts: nmsifthTemplateEntry.setStatus('current')
nmsifthTemplateIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 9, 218, 1, 1, 3, 1, 1), NMSifthTemplateIndex())
if mibBuilder.loadTexts: nmsifthTemplateIndex.setStatus('current')
nmsifthTemplateName = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 9, 218, 1, 1, 3, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nmsifthTemplateName.setStatus('current')
nmsifthTemplateNotifyHoldDownType = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 9, 218, 1, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("holdDownTimer", 2), ("fireAndClearThresholds", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nmsifthTemplateNotifyHoldDownType.setStatus('current')
nmsifthTemplateNotifyHoldDownTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 9, 218, 1, 1, 3, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 3600)).clone(5)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: nmsifthTemplateNotifyHoldDownTime.setStatus('current')
nmsifthTemplateRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 9, 218, 1, 1, 3, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nmsifthTemplateRowStatus.setStatus('current')
nmsifthThresholdLastChange = MibScalar((1, 3, 6, 1, 4, 1, 52642, 9, 218, 1, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsifthThresholdLastChange.setStatus('current')
nmsifthThresholdTable = MibTable((1, 3, 6, 1, 4, 1, 52642, 9, 218, 1, 1, 5), )
if mibBuilder.loadTexts: nmsifthThresholdTable.setStatus('current')
nmsifthThresholdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52642, 9, 218, 1, 1, 5, 1), ).setIndexNames((0, "FS-NMS-IF-THRESHOLD-MIB", "nmsifthTemplateIndex"), (0, "FS-NMS-IF-THRESHOLD-MIB", "nmsifthThresholdIndex"))
if mibBuilder.loadTexts: nmsifthThresholdEntry.setStatus('current')
nmsifthThresholdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 9, 218, 1, 1, 5, 1, 1), NMSifthThresholdIndex())
if mibBuilder.loadTexts: nmsifthThresholdIndex.setStatus('current')
nmsifthThresholdDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 9, 218, 1, 1, 5, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nmsifthThresholdDescr.setStatus('current')
nmsifthThresholdObject = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 9, 218, 1, 1, 5, 1, 3), ObjectIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nmsifthThresholdObject.setStatus('current')
nmsifthThresholdSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 9, 218, 1, 1, 5, 1, 4), NMSifthThresholdSeverity()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nmsifthThresholdSeverity.setStatus('current')
nmsifthThresholdType = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 9, 218, 1, 1, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("absoluteValue", 1), ("deltaValue", 2), ("rateOfIncreaseExponentXIfSpeed", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nmsifthThresholdType.setStatus('current')
nmsifthThresholdDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 9, 218, 1, 1, 5, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("rising", 1), ("falling", 2))).clone('rising')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nmsifthThresholdDirection.setStatus('current')
nmsifthThresholdFiredValue = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 9, 218, 1, 1, 5, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nmsifthThresholdFiredValue.setStatus('current')
nmsifthThresholdClearedValue = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 9, 218, 1, 1, 5, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nmsifthThresholdClearedValue.setStatus('current')
nmsifthThresholdSampleInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 9, 218, 1, 1, 5, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(5, 900000))).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: nmsifthThresholdSampleInterval.setStatus('current')
nmsifthThresholdApsSwitchover = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 9, 218, 1, 1, 5, 1, 10), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nmsifthThresholdApsSwitchover.setStatus('current')
nmsifthThresholdRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 9, 218, 1, 1, 5, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nmsifthThresholdRowStatus.setStatus('current')
nmsifthTemplateIfLastChange = MibScalar((1, 3, 6, 1, 4, 1, 52642, 9, 218, 1, 2, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsifthTemplateIfLastChange.setStatus('current')
nmsifthTemplateIfAssignTable = MibTable((1, 3, 6, 1, 4, 1, 52642, 9, 218, 1, 2, 2), )
if mibBuilder.loadTexts: nmsifthTemplateIfAssignTable.setStatus('current')
nmsifthTemplateIfAssignEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52642, 9, 218, 1, 2, 2, 1), ).setIndexNames((0, "FS-NMS-IF-THRESHOLD-MIB", "nmsifthTemplateIndex"), (0, "FS-NMS-IF-THRESHOLD-MIB", "nmsifthTemplateIfAssignInterface"))
if mibBuilder.loadTexts: nmsifthTemplateIfAssignEntry.setStatus('current')
nmsifthTemplateIfAssignInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 9, 218, 1, 2, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: nmsifthTemplateIfAssignInterface.setStatus('current')
nmsifthTemplateIfAssignOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 9, 218, 1, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsifthTemplateIfAssignOperStatus.setStatus('current')
nmsifthTemplateIfAssignRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 9, 218, 1, 2, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nmsifthTemplateIfAssignRowStatus.setStatus('current')
nmsifthThresholdFiredNotifyEnable = MibScalar((1, 3, 6, 1, 4, 1, 52642, 9, 218, 1, 3, 1), NMSifthThresholdSeverityOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsifthThresholdFiredNotifyEnable.setStatus('current')
nmsifthThresholdFiredLastChange = MibScalar((1, 3, 6, 1, 4, 1, 52642, 9, 218, 1, 3, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsifthThresholdFiredLastChange.setStatus('current')
nmsifthIfThresholdFiredTable = MibTable((1, 3, 6, 1, 4, 1, 52642, 9, 218, 1, 3, 3), )
if mibBuilder.loadTexts: nmsifthIfThresholdFiredTable.setStatus('current')
nmsifthIfThresholdFiredEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52642, 9, 218, 1, 3, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "FS-NMS-IF-THRESHOLD-MIB", "nmsifthIfThresholdFiredTemplate"))
if mibBuilder.loadTexts: nmsifthIfThresholdFiredEntry.setStatus('current')
nmsifthIfThresholdFiredTemplate = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 9, 218, 1, 3, 3, 1, 1), NMSifthTemplateIndex())
if mibBuilder.loadTexts: nmsifthIfThresholdFiredTemplate.setStatus('current')
nmsifthIfThresholdsFired = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 9, 218, 1, 3, 3, 1, 2), NMSifthThresholdList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsifthIfThresholdsFired.setStatus('current')
nmsifthIfLastThresholdFired = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 9, 218, 1, 3, 3, 1, 3), NMSifthThresholdIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsifthIfLastThresholdFired.setStatus('current')
nmsifthIfThresholdFiredLstChange = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 9, 218, 1, 3, 3, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsifthIfThresholdFiredLstChange.setStatus('current')
nmsifthIfThresholdFiredLstSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 9, 218, 1, 3, 3, 1, 5), NMSifthThresholdSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsifthIfThresholdFiredLstSeverity.setStatus('current')
nmsifthIfThresholdFiredMaxSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 9, 218, 1, 3, 3, 1, 6), NMSifthThresholdSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsifthIfThresholdFiredMaxSeverity.setStatus('current')
nmsIfThresholdMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 9, 218, 2))
nmsifthMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 9, 218, 2, 0))
nmsifthIfThresholdFired = NotificationType((1, 3, 6, 1, 4, 1, 52642, 9, 218, 2, 0, 1)).setObjects(("FS-NMS-IF-THRESHOLD-MIB", "nmsifthIfLastThresholdFired"), ("FS-NMS-IF-THRESHOLD-MIB", "nmsifthIfThresholdFiredLstChange"), ("FS-NMS-IF-THRESHOLD-MIB", "nmsifthIfThresholdFiredLstSeverity"))
if mibBuilder.loadTexts: nmsifthIfThresholdFired.setStatus('current')
nmsifthIfThresholdCleared = NotificationType((1, 3, 6, 1, 4, 1, 52642, 9, 218, 2, 0, 2)).setObjects(("FS-NMS-IF-THRESHOLD-MIB", "nmsifthIfLastThresholdFired"), ("FS-NMS-IF-THRESHOLD-MIB", "nmsifthIfThresholdFiredLstChange"), ("FS-NMS-IF-THRESHOLD-MIB", "nmsifthIfThresholdFiredLstSeverity"))
if mibBuilder.loadTexts: nmsifthIfThresholdCleared.setStatus('current')
nmsifthTemplateIfStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 52642, 9, 218, 2, 0, 3)).setObjects(("FS-NMS-IF-THRESHOLD-MIB", "nmsifthTemplateIfAssignOperStatus"))
if mibBuilder.loadTexts: nmsifthTemplateIfStatusChange.setStatus('current')
nmsIfThresholdMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 9, 218, 3))
nmsIfThresholdMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 9, 218, 3, 1))
nmsIfThresholdMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 9, 218, 3, 2))
nmsIfThresholdMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52642, 9, 218, 3, 1, 1)).setObjects(("FS-NMS-IF-THRESHOLD-MIB", "nmsIfThresholdTemplateGroup"), ("FS-NMS-IF-THRESHOLD-MIB", "nmsIfThresholdFiredGroup"), ("FS-NMS-IF-THRESHOLD-MIB", "nmsIfThresholdNotifsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nmsIfThresholdMIBCompliance = nmsIfThresholdMIBCompliance.setStatus('current')
nmsIfThresholdTemplateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52642, 9, 218, 3, 2, 1)).setObjects(("FS-NMS-IF-THRESHOLD-MIB", "nmsifthTemplateIndexNext"), ("FS-NMS-IF-THRESHOLD-MIB", "nmsifthTemplateLastChange"), ("FS-NMS-IF-THRESHOLD-MIB", "nmsifthTemplateName"), ("FS-NMS-IF-THRESHOLD-MIB", "nmsifthTemplateNotifyHoldDownType"), ("FS-NMS-IF-THRESHOLD-MIB", "nmsifthTemplateRowStatus"), ("FS-NMS-IF-THRESHOLD-MIB", "nmsifthThresholdLastChange"), ("FS-NMS-IF-THRESHOLD-MIB", "nmsifthThresholdDescr"), ("FS-NMS-IF-THRESHOLD-MIB", "nmsifthThresholdObject"), ("FS-NMS-IF-THRESHOLD-MIB", "nmsifthThresholdSeverity"), ("FS-NMS-IF-THRESHOLD-MIB", "nmsifthThresholdType"), ("FS-NMS-IF-THRESHOLD-MIB", "nmsifthThresholdDirection"), ("FS-NMS-IF-THRESHOLD-MIB", "nmsifthThresholdFiredValue"), ("FS-NMS-IF-THRESHOLD-MIB", "nmsifthThresholdSampleInterval"), ("FS-NMS-IF-THRESHOLD-MIB", "nmsifthThresholdRowStatus"), ("FS-NMS-IF-THRESHOLD-MIB", "nmsifthTemplateIfLastChange"), ("FS-NMS-IF-THRESHOLD-MIB", "nmsifthTemplateIfAssignOperStatus"), ("FS-NMS-IF-THRESHOLD-MIB", "nmsifthTemplateIfAssignRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nmsIfThresholdTemplateGroup = nmsIfThresholdTemplateGroup.setStatus('current')
nmsIfThresholdFiredGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52642, 9, 218, 3, 2, 2)).setObjects(("FS-NMS-IF-THRESHOLD-MIB", "nmsifthThresholdFiredNotifyEnable"), ("FS-NMS-IF-THRESHOLD-MIB", "nmsifthThresholdFiredLastChange"), ("FS-NMS-IF-THRESHOLD-MIB", "nmsifthIfThresholdsFired"), ("FS-NMS-IF-THRESHOLD-MIB", "nmsifthIfLastThresholdFired"), ("FS-NMS-IF-THRESHOLD-MIB", "nmsifthIfThresholdFiredLstChange"), ("FS-NMS-IF-THRESHOLD-MIB", "nmsifthIfThresholdFiredLstSeverity"), ("FS-NMS-IF-THRESHOLD-MIB", "nmsifthIfThresholdFiredMaxSeverity"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nmsIfThresholdFiredGroup = nmsIfThresholdFiredGroup.setStatus('current')
nmsifthHoldDownTimerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52642, 9, 218, 3, 2, 3)).setObjects(("FS-NMS-IF-THRESHOLD-MIB", "nmsifthTemplateNotifyHoldDownTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nmsifthHoldDownTimerGroup = nmsifthHoldDownTimerGroup.setStatus('current')
nmsifthHoldDownHysteresisGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52642, 9, 218, 3, 2, 4)).setObjects(("FS-NMS-IF-THRESHOLD-MIB", "nmsifthThresholdClearedValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nmsifthHoldDownHysteresisGroup = nmsifthHoldDownHysteresisGroup.setStatus('current')
nmsifthApsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52642, 9, 218, 3, 2, 5)).setObjects(("FS-NMS-IF-THRESHOLD-MIB", "nmsifthThresholdApsSwitchover"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nmsifthApsGroup = nmsifthApsGroup.setStatus('current')
nmsIfThresholdNotifsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 52642, 9, 218, 3, 2, 6)).setObjects(("FS-NMS-IF-THRESHOLD-MIB", "nmsifthIfThresholdFired"), ("FS-NMS-IF-THRESHOLD-MIB", "nmsifthIfThresholdCleared"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nmsIfThresholdNotifsGroup = nmsIfThresholdNotifsGroup.setStatus('current')
nmsifthTemplateIfNotifsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 52642, 9, 218, 3, 2, 7)).setObjects(("FS-NMS-IF-THRESHOLD-MIB", "nmsifthTemplateIfStatusChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nmsifthTemplateIfNotifsGroup = nmsifthTemplateIfNotifsGroup.setStatus('current')
mibBuilder.exportSymbols("FS-NMS-IF-THRESHOLD-MIB", nmsIfThresholdMIBObjects=nmsIfThresholdMIBObjects, PYSNMP_MODULE_ID=nmsIfThresholdMIB, nmsifthTemplateIndex=nmsifthTemplateIndex, nmsifthThresholdRowStatus=nmsifthThresholdRowStatus, nmsifthTemplateTable=nmsifthTemplateTable, nmsifthTemplateIfNotifsGroup=nmsifthTemplateIfNotifsGroup, nmsifthThresholdApsSwitchover=nmsifthThresholdApsSwitchover, nmsifthThresholdIndex=nmsifthThresholdIndex, nmsifthIfThresholdFiredTemplate=nmsifthIfThresholdFiredTemplate, nmsifthThresholdObject=nmsifthThresholdObject, NMSifthThresholdSeverityOrZero=NMSifthThresholdSeverityOrZero, nmsifthThresholdTable=nmsifthThresholdTable, nmsifthTemplateIfAssignEntry=nmsifthTemplateIfAssignEntry, NMSifthThresholdSeverity=NMSifthThresholdSeverity, nmsifthThresholdClearedValue=nmsifthThresholdClearedValue, nmsIfThresholdMIBConformance=nmsIfThresholdMIBConformance, nmsifthTemplateIfLastChange=nmsifthTemplateIfLastChange, nmsifthThresholdDirection=nmsifthThresholdDirection, nmsifthIfThresholdFired=nmsifthIfThresholdFired, NMSifthTemplateIndexOrZero=NMSifthTemplateIndexOrZero, nmsifthTemplateRowStatus=nmsifthTemplateRowStatus, nmsifthIfThresholdFiredGroup=nmsifthIfThresholdFiredGroup, nmsifthTemplateIfAssignTable=nmsifthTemplateIfAssignTable, NMSifthTemplateIndex=NMSifthTemplateIndex, nmsifthIfThresholdCleared=nmsifthIfThresholdCleared, NMSifthThresholdList=NMSifthThresholdList, nmsifthTemplateGroup=nmsifthTemplateGroup, nmsifthTemplateNotifyHoldDownTime=nmsifthTemplateNotifyHoldDownTime, nmsifthThresholdSampleInterval=nmsifthThresholdSampleInterval, nmsifthThresholdDescr=nmsifthThresholdDescr, nmsifthIfThresholdFiredTable=nmsifthIfThresholdFiredTable, nmsifthIfThresholdFiredMaxSeverity=nmsifthIfThresholdFiredMaxSeverity, nmsIfThresholdMIBNotifications=nmsIfThresholdMIBNotifications, nmsifthMIBNotificationsPrefix=nmsifthMIBNotificationsPrefix, nmsifthTemplateNotifyHoldDownType=nmsifthTemplateNotifyHoldDownType, nmsIfThresholdMIBCompliance=nmsIfThresholdMIBCompliance, nmsifthHoldDownHysteresisGroup=nmsifthHoldDownHysteresisGroup, nmsIfThresholdMIB=nmsIfThresholdMIB, nmsIfThresholdNotifsGroup=nmsIfThresholdNotifsGroup, nmsifthApsGroup=nmsifthApsGroup, nmsifthThresholdLastChange=nmsifthThresholdLastChange, nmsifthTemplateIfAssignGroup=nmsifthTemplateIfAssignGroup, nmsifthTemplateLastChange=nmsifthTemplateLastChange, nmsifthIfThresholdsFired=nmsifthIfThresholdsFired, nmsifthThresholdFiredValue=nmsifthThresholdFiredValue, nmsIfThresholdMIBCompliances=nmsIfThresholdMIBCompliances, nmsifthIfThresholdFiredEntry=nmsifthIfThresholdFiredEntry, nmsifthTemplateIfStatusChange=nmsifthTemplateIfStatusChange, nmsIfThresholdTemplateGroup=nmsIfThresholdTemplateGroup, nmsifthIfThresholdFiredLstSeverity=nmsifthIfThresholdFiredLstSeverity, nmsifthThresholdFiredLastChange=nmsifthThresholdFiredLastChange, nmsifthIfLastThresholdFired=nmsifthIfLastThresholdFired, nmsifthThresholdEntry=nmsifthThresholdEntry, nmsifthHoldDownTimerGroup=nmsifthHoldDownTimerGroup, nmsIfThresholdFiredGroup=nmsIfThresholdFiredGroup, nmsifthTemplateIfAssignInterface=nmsifthTemplateIfAssignInterface, nmsifthTemplateIfAssignOperStatus=nmsifthTemplateIfAssignOperStatus, nmsifthIfThresholdFiredLstChange=nmsifthIfThresholdFiredLstChange, nmsifthTemplateEntry=nmsifthTemplateEntry, nmsIfThresholdMIBGroups=nmsIfThresholdMIBGroups, nmsifthThresholdFiredNotifyEnable=nmsifthThresholdFiredNotifyEnable, nmsifthTemplateName=nmsifthTemplateName, nmsifthTemplateIndexNext=nmsifthTemplateIndexNext, NMSifthThresholdIndex=NMSifthThresholdIndex, nmsifthTemplateIfAssignRowStatus=nmsifthTemplateIfAssignRowStatus, nmsifthThresholdSeverity=nmsifthThresholdSeverity, nmsifthThresholdType=nmsifthThresholdType)
