#
# PySNMP MIB module SAVEPOWER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/SAVEPOWER-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:08:12 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DateAndTime", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("SAVEPOWER-MIB", SavepowerBlockIndex=SavepowerBlockIndex, hpicfSavepowerEntityLEDOperStatus=hpicfSavepowerEntityLEDOperStatus, hpicfSavepowerEnabledPorts=hpicfSavepowerEnabledPorts, hpicfSavepowerGreenFeaturesEntry=hpicfSavepowerGreenFeaturesEntry, hpicfSavepowerScalars=hpicfSavepowerScalars, hpicfSavepowerLEDScalars=hpicfSavepowerLEDScalars, hpicfPHYGroups=hpicfPHYGroups, hpicfSavepowerPHYTable=hpicfSavepowerPHYTable, hpicfPHYComplianceInfo=hpicfPHYComplianceInfo, hpicfSavepowerPHYOperStatus=hpicfSavepowerPHYOperStatus, hpicfSavepowerConformance=hpicfSavepowerConformance, hpicfSavepowerCompliance=hpicfSavepowerCompliance, hpicfSavepowerScalarsGroup=hpicfSavepowerScalarsGroup, hpicfSavePowerLEDOffAlarmStartTime=hpicfSavePowerLEDOffAlarmStartTime, hpicfPHYCompliance=hpicfPHYCompliance, hpicfSavepowerPHYAdminStatus=hpicfSavepowerPHYAdminStatus, hpicfSavepowerComplianceInfo=hpicfSavepowerComplianceInfo, hpicfSavepowerBlockID=hpicfSavepowerBlockID, hpicfSavepowerPHYEntry=hpicfSavepowerPHYEntry, hpicfSavepowerGroup=hpicfSavepowerGroup, hpicfSavePowerLEDOffAlarmRecur=hpicfSavePowerLEDOffAlarmRecur, PYSNMP_MODULE_ID=hpicfSavepowerMIB, hpicfSavepowerEntPHYAdminStatus=hpicfSavepowerEntPHYAdminStatus, hpicfSavepowerLEDScalarsGroup=hpicfSavepowerLEDScalarsGroup, hpicfSavepowerBlockPorts=hpicfSavepowerBlockPorts, hpicfEntitySavepower=hpicfEntitySavepower, hpicfSavepowerEntityPowerOperStatus=hpicfSavepowerEntityPowerOperStatus, hpicfPHYConformance=hpicfPHYConformance, hpicfSavepowerEntry=hpicfSavepowerEntry, hpicfSavepowerGreenFeaturesTable=hpicfSavepowerGreenFeaturesTable, hpicfSavepowerEntityLEDAdminStatus=hpicfSavepowerEntityLEDAdminStatus, hpicfSavePowerLEDOffAlarmDuration=hpicfSavePowerLEDOffAlarmDuration, hpicfSavepowerGreenFeaturesGroup=hpicfSavepowerGreenFeaturesGroup, hpicfSavepowerControl=hpicfSavepowerControl, hpicfSavepowerEntPHYEntry=hpicfSavepowerEntPHYEntry, hpicfSavepowerEntPHYOperStatus=hpicfSavepowerEntPHYOperStatus, hpicfSavepowerPHYGroup=hpicfSavepowerPHYGroup, hpicfSavepowerEntPHYTable=hpicfSavepowerEntPHYTable, hpicfSavepowerTable=hpicfSavepowerTable, hpicfSavepowerEntityPowerAdminStatus=hpicfSavepowerEntityPowerAdminStatus, hpicfSavepowerMIB=hpicfSavepowerMIB, hpicfSavepowerGroups=hpicfSavepowerGroups, hpicfSavepowerEntPHYGroup=hpicfSavepowerEntPHYGroup, SavepowerControl=SavepowerControl, hpicfSavepowerMaxBlocks=hpicfSavepowerMaxBlocks, hpicfSavepowerPortNum=hpicfSavepowerPortNum, hpicfSavepowerSlotNum=hpicfSavepowerSlotNum)
