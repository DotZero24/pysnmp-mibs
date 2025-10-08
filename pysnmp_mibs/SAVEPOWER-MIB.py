#
# PySNMP MIB module SAVEPOWER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/SAVEPOWER-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:02:25 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "DateAndTime", "TextualConvention")
hpicfSavepowerMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56))
hpicfSavepowerMIB.setRevisions(('2010-08-12 00:00', '2008-10-17 14:30',))
if mibBuilder.loadTexts: hpicfSavepowerMIB.setLastUpdated('201008120000Z')
if mibBuilder.loadTexts: hpicfSavepowerMIB.setOrganization('HP Networking')
hpicfSavepowerScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 1))
hpicfSavepowerLEDScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 1, 3))
class SavepowerBlockIndex(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'

class SavepowerControl(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("powerOn", 1), ("powerOff", 2))

hpicfSavepowerMaxBlocks = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSavepowerMaxBlocks.setStatus('current')
hpicfSavepowerEnabledPorts = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSavepowerEnabledPorts.setStatus('current')
hpicfSavePowerLEDOffAlarmStartTime = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 1, 3, 1), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfSavePowerLEDOffAlarmStartTime.setStatus('current')
hpicfSavePowerLEDOffAlarmDuration = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 1, 3, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfSavePowerLEDOffAlarmDuration.setStatus('current')
hpicfSavePowerLEDOffAlarmRecur = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 1, 3, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfSavePowerLEDOffAlarmRecur.setStatus('current')
hpicfEntitySavepower = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 2))
hpicfSavepowerTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 2, 1), )
if mibBuilder.loadTexts: hpicfSavepowerTable.setStatus('current')
hpicfSavepowerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 2, 1, 1), ).setIndexNames((0, "SAVEPOWER-MIB", "hpicfSavepowerBlockID"))
if mibBuilder.loadTexts: hpicfSavepowerEntry.setStatus('current')
hpicfSavepowerBlockID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 2, 1, 1, 1), SavepowerBlockIndex())
if mibBuilder.loadTexts: hpicfSavepowerBlockID.setStatus('current')
hpicfSavepowerControl = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 2, 1, 1, 2), SavepowerControl()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfSavepowerControl.setStatus('current')
hpicfSavepowerBlockPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 2, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSavepowerBlockPorts.setStatus('current')
hpicfSavepowerGreenFeaturesTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 2, 2), )
if mibBuilder.loadTexts: hpicfSavepowerGreenFeaturesTable.setStatus('current')
hpicfSavepowerGreenFeaturesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 2, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: hpicfSavepowerGreenFeaturesEntry.setStatus('current')
hpicfSavepowerEntityPowerAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 2, 2, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfSavepowerEntityPowerAdminStatus.setStatus('current')
hpicfSavepowerEntityPowerOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 2, 2, 1, 2), SavepowerControl()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSavepowerEntityPowerOperStatus.setStatus('current')
hpicfSavepowerEntityLEDAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 2, 2, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfSavepowerEntityLEDAdminStatus.setStatus('current')
hpicfSavepowerEntityLEDOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 2, 2, 1, 4), SavepowerControl()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSavepowerEntityLEDOperStatus.setStatus('current')
hpicfSavepowerPHYTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 2, 3), )
if mibBuilder.loadTexts: hpicfSavepowerPHYTable.setStatus('current')
hpicfSavepowerPHYEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 2, 3, 1), ).setIndexNames((0, "SAVEPOWER-MIB", "hpicfSavepowerSlotNum"), (0, "SAVEPOWER-MIB", "hpicfSavepowerPortNum"))
if mibBuilder.loadTexts: hpicfSavepowerPHYEntry.setStatus('current')
hpicfSavepowerSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 2, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hpicfSavepowerSlotNum.setStatus('current')
hpicfSavepowerPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 2, 3, 1, 2), Unsigned32())
if mibBuilder.loadTexts: hpicfSavepowerPortNum.setStatus('current')
hpicfSavepowerPHYAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 2, 3, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfSavepowerPHYAdminStatus.setStatus('current')
hpicfSavepowerPHYOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 2, 3, 1, 4), SavepowerControl()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSavepowerPHYOperStatus.setStatus('current')
hpicfSavepowerEntPHYTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 2, 4), )
if mibBuilder.loadTexts: hpicfSavepowerEntPHYTable.setStatus('current')
hpicfSavepowerEntPHYEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 2, 4, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: hpicfSavepowerEntPHYEntry.setStatus('current')
hpicfSavepowerEntPHYAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 2, 4, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfSavepowerEntPHYAdminStatus.setStatus('current')
hpicfSavepowerEntPHYOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 2, 4, 1, 2), SavepowerControl()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSavepowerEntPHYOperStatus.setStatus('current')
hpicfSavepowerConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 3))
hpicfSavepowerCompliance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 3, 1))
hpicfSavepowerGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 3, 2))
hpicfSavepowerComplianceInfo = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 3, 1, 1)).setObjects(("SAVEPOWER-MIB", "hpicfSavepowerScalarsGroup"), ("SAVEPOWER-MIB", "hpicfSavepowerLEDScalarsGroup"), ("SAVEPOWER-MIB", "hpicfSavepowerGreenFeaturesGroup"), ("SAVEPOWER-MIB", "hpicfSavepowerPHYGroup"), ("SAVEPOWER-MIB", "hpicfSavepowerGroup"), ("SAVEPOWER-MIB", "hpicfSavepowerGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSavepowerComplianceInfo = hpicfSavepowerComplianceInfo.setStatus('current')
hpicfSavepowerScalarsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 3, 2, 1)).setObjects(("SAVEPOWER-MIB", "hpicfSavepowerMaxBlocks"), ("SAVEPOWER-MIB", "hpicfSavepowerEnabledPorts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSavepowerScalarsGroup = hpicfSavepowerScalarsGroup.setStatus('current')
hpicfSavepowerLEDScalarsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 3, 2, 2)).setObjects(("SAVEPOWER-MIB", "hpicfSavePowerLEDOffAlarmStartTime"), ("SAVEPOWER-MIB", "hpicfSavePowerLEDOffAlarmDuration"), ("SAVEPOWER-MIB", "hpicfSavePowerLEDOffAlarmRecur"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSavepowerLEDScalarsGroup = hpicfSavepowerLEDScalarsGroup.setStatus('current')
hpicfSavepowerGreenFeaturesGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 3, 2, 3)).setObjects(("SAVEPOWER-MIB", "hpicfSavepowerEntityPowerAdminStatus"), ("SAVEPOWER-MIB", "hpicfSavepowerEntityPowerOperStatus"), ("SAVEPOWER-MIB", "hpicfSavepowerEntityLEDAdminStatus"), ("SAVEPOWER-MIB", "hpicfSavepowerEntityLEDOperStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSavepowerGreenFeaturesGroup = hpicfSavepowerGreenFeaturesGroup.setStatus('current')
hpicfSavepowerPHYGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 3, 2, 4)).setObjects(("SAVEPOWER-MIB", "hpicfSavepowerPHYAdminStatus"), ("SAVEPOWER-MIB", "hpicfSavepowerPHYOperStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSavepowerPHYGroup = hpicfSavepowerPHYGroup.setStatus('current')
hpicfSavepowerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 3, 2, 5)).setObjects(("SAVEPOWER-MIB", "hpicfSavepowerControl"), ("SAVEPOWER-MIB", "hpicfSavepowerBlockPorts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSavepowerGroup = hpicfSavepowerGroup.setStatus('current')
hpicfPHYConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 4))
hpicfPHYCompliance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 4, 1))
hpicfPHYGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 4, 2))
hpicfPHYComplianceInfo = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 4, 1, 1)).setObjects(("SAVEPOWER-MIB", "hpicfSavepowerEntPHYGroup"), ("SAVEPOWER-MIB", "hpicfPHYGroups"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfPHYComplianceInfo = hpicfPHYComplianceInfo.setStatus('current')
hpicfSavepowerEntPHYGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 4, 2, 1)).setObjects(("SAVEPOWER-MIB", "hpicfSavepowerEntPHYAdminStatus"), ("SAVEPOWER-MIB", "hpicfSavepowerEntPHYOperStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSavepowerEntPHYGroup = hpicfSavepowerEntPHYGroup.setStatus('current')
mibBuilder.exportSymbols("SAVEPOWER-MIB", SavepowerBlockIndex=SavepowerBlockIndex, hpicfPHYConformance=hpicfPHYConformance, hpicfPHYComplianceInfo=hpicfPHYComplianceInfo, hpicfSavepowerBlockPorts=hpicfSavepowerBlockPorts, hpicfSavepowerEntityPowerAdminStatus=hpicfSavepowerEntityPowerAdminStatus, hpicfSavepowerEntPHYGroup=hpicfSavepowerEntPHYGroup, hpicfSavepowerPHYTable=hpicfSavepowerPHYTable, hpicfSavepowerLEDScalars=hpicfSavepowerLEDScalars, hpicfSavepowerEntry=hpicfSavepowerEntry, hpicfSavepowerPortNum=hpicfSavepowerPortNum, hpicfSavepowerLEDScalarsGroup=hpicfSavepowerLEDScalarsGroup, hpicfSavePowerLEDOffAlarmDuration=hpicfSavePowerLEDOffAlarmDuration, hpicfSavepowerPHYGroup=hpicfSavepowerPHYGroup, hpicfSavepowerTable=hpicfSavepowerTable, PYSNMP_MODULE_ID=hpicfSavepowerMIB, hpicfSavepowerGreenFeaturesTable=hpicfSavepowerGreenFeaturesTable, hpicfSavepowerGroup=hpicfSavepowerGroup, hpicfSavepowerSlotNum=hpicfSavepowerSlotNum, hpicfSavepowerEntityLEDOperStatus=hpicfSavepowerEntityLEDOperStatus, hpicfSavepowerCompliance=hpicfSavepowerCompliance, hpicfSavepowerGreenFeaturesGroup=hpicfSavepowerGreenFeaturesGroup, hpicfPHYGroups=hpicfPHYGroups, hpicfSavepowerEntityLEDAdminStatus=hpicfSavepowerEntityLEDAdminStatus, hpicfSavepowerGreenFeaturesEntry=hpicfSavepowerGreenFeaturesEntry, hpicfSavepowerBlockID=hpicfSavepowerBlockID, hpicfSavepowerControl=hpicfSavepowerControl, hpicfSavepowerEntPHYTable=hpicfSavepowerEntPHYTable, hpicfEntitySavepower=hpicfEntitySavepower, hpicfSavePowerLEDOffAlarmStartTime=hpicfSavePowerLEDOffAlarmStartTime, hpicfSavepowerEnabledPorts=hpicfSavepowerEnabledPorts, hpicfSavepowerScalars=hpicfSavepowerScalars, hpicfSavepowerEntPHYEntry=hpicfSavepowerEntPHYEntry, hpicfSavepowerEntPHYAdminStatus=hpicfSavepowerEntPHYAdminStatus, hpicfSavepowerPHYAdminStatus=hpicfSavepowerPHYAdminStatus, SavepowerControl=SavepowerControl, hpicfSavepowerGroups=hpicfSavepowerGroups, hpicfPHYCompliance=hpicfPHYCompliance, hpicfSavepowerMaxBlocks=hpicfSavepowerMaxBlocks, hpicfSavePowerLEDOffAlarmRecur=hpicfSavePowerLEDOffAlarmRecur, hpicfSavepowerPHYOperStatus=hpicfSavepowerPHYOperStatus, hpicfSavepowerEntPHYOperStatus=hpicfSavepowerEntPHYOperStatus, hpicfSavepowerComplianceInfo=hpicfSavepowerComplianceInfo, hpicfSavepowerMIB=hpicfSavepowerMIB, hpicfSavepowerConformance=hpicfSavepowerConformance, hpicfSavepowerScalarsGroup=hpicfSavepowerScalarsGroup, hpicfSavepowerPHYEntry=hpicfSavepowerPHYEntry, hpicfSavepowerEntityPowerOperStatus=hpicfSavepowerEntityPowerOperStatus)
