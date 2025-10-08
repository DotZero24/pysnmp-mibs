#
# PySNMP MIB module CIE1000-POE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CIE1000-POE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:12:05 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
CIE1000InterfaceIndex, = mibBuilder.importSymbols("CIE1000-TC", "CIE1000InterfaceIndex")
cie1000SwitchMgmt, = mibBuilder.importSymbols("CISCO-IE1000-MIB", "cie1000SwitchMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
cie1000PoeMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 43))
cie1000PoeMib.setRevisions(('2014-08-20 00:00',))
if mibBuilder.loadTexts: cie1000PoeMib.setLastUpdated('201408200000Z')
if mibBuilder.loadTexts: cie1000PoeMib.setOrganization('Cisco Systems, Inc.')
class CIE1000poeMgmtModeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("classReservedPower", 0), ("classConsumption", 1), ("allocatedReservedPower", 2), ("allocatedConsumption", 3), ("lldpReservedPower", 4), ("lldpConsumption", 5))

class CIE1000poeModeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("disable", 0), ("poeDot3af", 1), ("poePlusDot3at", 2))

class CIE1000poePowerPriorityType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("low", 0), ("high", 1), ("critical", 2))

class CIE1000poeStatusType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("notSupported", 0), ("budgetExceeded", 1), ("noPoweredDeviceDetected", 2), ("poweredDeviceOn", 3), ("poweredDeviceOff", 4), ("poweredDeviceOverloaded", 5), ("unknownState", 6), ("disabled", 7))

cie1000PoeMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 43, 1))
cie1000PoeCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 43, 1, 1))
cie1000PoeCapabilitiesInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 43, 1, 1, 1), )
if mibBuilder.loadTexts: cie1000PoeCapabilitiesInterfaceTable.setStatus('current')
cie1000PoeCapabilitiesInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 43, 1, 1, 1, 1), ).setIndexNames((0, "CIE1000-POE-MIB", "cie1000PoeCapabilitiesInterfaceIfIndex"))
if mibBuilder.loadTexts: cie1000PoeCapabilitiesInterfaceEntry.setStatus('current')
cie1000PoeCapabilitiesInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 43, 1, 1, 1, 1, 1), CIE1000InterfaceIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cie1000PoeCapabilitiesInterfaceIfIndex.setStatus('current')
cie1000PoeCapabilitiesInterfacePoE = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 43, 1, 1, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cie1000PoeCapabilitiesInterfacePoE.setStatus('current')
cie1000PoeConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 43, 1, 2))
cie1000PoeConfigGlobals = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 43, 1, 2, 1))
cie1000PoeConfigGlobalsManagementMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 43, 1, 2, 1, 1), CIE1000poeMgmtModeType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cie1000PoeConfigGlobalsManagementMode.setStatus('current')
cie1000PoeConfigSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 43, 1, 2, 2))
cie1000PoeConfigSwitchParamTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 43, 1, 2, 2, 1), )
if mibBuilder.loadTexts: cie1000PoeConfigSwitchParamTable.setStatus('current')
cie1000PoeConfigSwitchParamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 43, 1, 2, 2, 1, 1), ).setIndexNames((0, "CIE1000-POE-MIB", "cie1000PoeConfigSwitchParamSwitchId"))
if mibBuilder.loadTexts: cie1000PoeConfigSwitchParamEntry.setStatus('current')
cie1000PoeConfigSwitchParamSwitchId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 43, 1, 2, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cie1000PoeConfigSwitchParamSwitchId.setStatus('current')
cie1000PoeConfigSwitchParamMaxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 43, 1, 2, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 180))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cie1000PoeConfigSwitchParamMaxPower.setStatus('current')
cie1000PoeConfigSwitchParamCapacitorDetection = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 43, 1, 2, 2, 1, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cie1000PoeConfigSwitchParamCapacitorDetection.setStatus('current')
cie1000PoeConfigInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 43, 1, 2, 3))
cie1000PoeConfigInterfaceParamTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 43, 1, 2, 3, 1), )
if mibBuilder.loadTexts: cie1000PoeConfigInterfaceParamTable.setStatus('current')
cie1000PoeConfigInterfaceParamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 43, 1, 2, 3, 1, 1), ).setIndexNames((0, "CIE1000-POE-MIB", "cie1000PoeConfigInterfaceParamIfIndex"))
if mibBuilder.loadTexts: cie1000PoeConfigInterfaceParamEntry.setStatus('current')
cie1000PoeConfigInterfaceParamIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 43, 1, 2, 3, 1, 1, 1), CIE1000InterfaceIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cie1000PoeConfigInterfaceParamIfIndex.setStatus('current')
cie1000PoeConfigInterfaceParamMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 43, 1, 2, 3, 1, 1, 2), CIE1000poeModeType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cie1000PoeConfigInterfaceParamMode.setStatus('current')
cie1000PoeConfigInterfaceParamPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 43, 1, 2, 3, 1, 1, 3), CIE1000poePowerPriorityType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cie1000PoeConfigInterfaceParamPriority.setStatus('current')
cie1000PoeConfigInterfaceParamMaxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 43, 1, 2, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 300))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cie1000PoeConfigInterfaceParamMaxPower.setStatus('current')
cie1000PoeStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 43, 1, 3))
cie1000PoeStatusInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 43, 1, 3, 1), )
if mibBuilder.loadTexts: cie1000PoeStatusInterfaceTable.setStatus('current')
cie1000PoeStatusInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 43, 1, 3, 1, 1), ).setIndexNames((0, "CIE1000-POE-MIB", "cie1000PoeStatusInterfaceIfIndex"))
if mibBuilder.loadTexts: cie1000PoeStatusInterfaceEntry.setStatus('current')
cie1000PoeStatusInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 43, 1, 3, 1, 1, 1), CIE1000InterfaceIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cie1000PoeStatusInterfaceIfIndex.setStatus('current')
cie1000PoeStatusInterfacePDClass = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 43, 1, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cie1000PoeStatusInterfacePDClass.setStatus('current')
cie1000PoeStatusInterfaceCurrentState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 43, 1, 3, 1, 1, 3), CIE1000poeStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cie1000PoeStatusInterfaceCurrentState.setStatus('current')
cie1000PoeStatusInterfacePowerConsumption = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 43, 1, 3, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cie1000PoeStatusInterfacePowerConsumption.setStatus('current')
cie1000PoeStatusInterfacePowerReserved = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 43, 1, 3, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cie1000PoeStatusInterfacePowerReserved.setStatus('current')
cie1000PoeStatusInterfaceCurrentConsumption = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 43, 1, 3, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cie1000PoeStatusInterfaceCurrentConsumption.setStatus('current')
cie1000PoeMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 43, 2))
cie1000PoeMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 43, 2, 1))
cie1000PoeMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 43, 2, 2))
cie1000PoeCapabilitiesInterfaceInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 43, 2, 2, 1)).setObjects(("CIE1000-POE-MIB", "cie1000PoeCapabilitiesInterfaceIfIndex"), ("CIE1000-POE-MIB", "cie1000PoeCapabilitiesInterfacePoE"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cie1000PoeCapabilitiesInterfaceInfoGroup = cie1000PoeCapabilitiesInterfaceInfoGroup.setStatus('current')
cie1000PoeConfigGlobalsInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 43, 2, 2, 2)).setObjects(("CIE1000-POE-MIB", "cie1000PoeConfigGlobalsManagementMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cie1000PoeConfigGlobalsInfoGroup = cie1000PoeConfigGlobalsInfoGroup.setStatus('current')
cie1000PoeConfigSwitchParamTableInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 43, 2, 2, 3)).setObjects(("CIE1000-POE-MIB", "cie1000PoeConfigSwitchParamSwitchId"), ("CIE1000-POE-MIB", "cie1000PoeConfigSwitchParamMaxPower"), ("CIE1000-POE-MIB", "cie1000PoeConfigSwitchParamCapacitorDetection"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cie1000PoeConfigSwitchParamTableInfoGroup = cie1000PoeConfigSwitchParamTableInfoGroup.setStatus('current')
cie1000PoeConfigInterfaceParamTableInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 43, 2, 2, 4)).setObjects(("CIE1000-POE-MIB", "cie1000PoeConfigInterfaceParamIfIndex"), ("CIE1000-POE-MIB", "cie1000PoeConfigInterfaceParamMode"), ("CIE1000-POE-MIB", "cie1000PoeConfigInterfaceParamPriority"), ("CIE1000-POE-MIB", "cie1000PoeConfigInterfaceParamMaxPower"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cie1000PoeConfigInterfaceParamTableInfoGroup = cie1000PoeConfigInterfaceParamTableInfoGroup.setStatus('current')
cie1000PoeStatusInterfaceTableInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 43, 2, 2, 5)).setObjects(("CIE1000-POE-MIB", "cie1000PoeStatusInterfaceIfIndex"), ("CIE1000-POE-MIB", "cie1000PoeStatusInterfacePDClass"), ("CIE1000-POE-MIB", "cie1000PoeStatusInterfaceCurrentState"), ("CIE1000-POE-MIB", "cie1000PoeStatusInterfacePowerConsumption"), ("CIE1000-POE-MIB", "cie1000PoeStatusInterfacePowerReserved"), ("CIE1000-POE-MIB", "cie1000PoeStatusInterfaceCurrentConsumption"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cie1000PoeStatusInterfaceTableInfoGroup = cie1000PoeStatusInterfaceTableInfoGroup.setStatus('current')
cie1000PoeMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 43, 2, 1, 1)).setObjects(("CIE1000-POE-MIB", "cie1000PoeCapabilitiesInterfaceInfoGroup"), ("CIE1000-POE-MIB", "cie1000PoeConfigGlobalsInfoGroup"), ("CIE1000-POE-MIB", "cie1000PoeConfigSwitchParamTableInfoGroup"), ("CIE1000-POE-MIB", "cie1000PoeConfigInterfaceParamTableInfoGroup"), ("CIE1000-POE-MIB", "cie1000PoeStatusInterfaceTableInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cie1000PoeMibCompliance = cie1000PoeMibCompliance.setStatus('current')
mibBuilder.exportSymbols("CIE1000-POE-MIB", cie1000PoeConfigSwitchParamTableInfoGroup=cie1000PoeConfigSwitchParamTableInfoGroup, PYSNMP_MODULE_ID=cie1000PoeMib, cie1000PoeCapabilitiesInterfacePoE=cie1000PoeCapabilitiesInterfacePoE, cie1000PoeConfigInterfaceParamMaxPower=cie1000PoeConfigInterfaceParamMaxPower, cie1000PoeConfigInterfaceParamPriority=cie1000PoeConfigInterfaceParamPriority, CIE1000poeMgmtModeType=CIE1000poeMgmtModeType, cie1000PoeMibGroups=cie1000PoeMibGroups, cie1000PoeConfigSwitchParamCapacitorDetection=cie1000PoeConfigSwitchParamCapacitorDetection, cie1000PoeStatusInterfaceTable=cie1000PoeStatusInterfaceTable, cie1000PoeCapabilitiesInterfaceEntry=cie1000PoeCapabilitiesInterfaceEntry, cie1000PoeConfigInterfaceParamTable=cie1000PoeConfigInterfaceParamTable, cie1000PoeStatusInterfacePowerConsumption=cie1000PoeStatusInterfacePowerConsumption, cie1000PoeMib=cie1000PoeMib, cie1000PoeStatusInterfacePowerReserved=cie1000PoeStatusInterfacePowerReserved, cie1000PoeCapabilitiesInterfaceTable=cie1000PoeCapabilitiesInterfaceTable, cie1000PoeConfigSwitchParamEntry=cie1000PoeConfigSwitchParamEntry, cie1000PoeConfigInterfaceParamIfIndex=cie1000PoeConfigInterfaceParamIfIndex, cie1000PoeStatusInterfaceEntry=cie1000PoeStatusInterfaceEntry, cie1000PoeStatusInterfaceIfIndex=cie1000PoeStatusInterfaceIfIndex, cie1000PoeConfig=cie1000PoeConfig, cie1000PoeCapabilities=cie1000PoeCapabilities, CIE1000poePowerPriorityType=CIE1000poePowerPriorityType, cie1000PoeConfigGlobalsManagementMode=cie1000PoeConfigGlobalsManagementMode, cie1000PoeStatusInterfaceCurrentConsumption=cie1000PoeStatusInterfaceCurrentConsumption, CIE1000poeStatusType=CIE1000poeStatusType, cie1000PoeConfigGlobals=cie1000PoeConfigGlobals, cie1000PoeStatusInterfaceTableInfoGroup=cie1000PoeStatusInterfaceTableInfoGroup, cie1000PoeStatusInterfacePDClass=cie1000PoeStatusInterfacePDClass, cie1000PoeStatusInterfaceCurrentState=cie1000PoeStatusInterfaceCurrentState, cie1000PoeMibCompliances=cie1000PoeMibCompliances, cie1000PoeMibConformance=cie1000PoeMibConformance, CIE1000poeModeType=CIE1000poeModeType, cie1000PoeConfigInterfaceParamTableInfoGroup=cie1000PoeConfigInterfaceParamTableInfoGroup, cie1000PoeMibCompliance=cie1000PoeMibCompliance, cie1000PoeConfigSwitch=cie1000PoeConfigSwitch, cie1000PoeCapabilitiesInterfaceIfIndex=cie1000PoeCapabilitiesInterfaceIfIndex, cie1000PoeConfigSwitchParamTable=cie1000PoeConfigSwitchParamTable, cie1000PoeStatus=cie1000PoeStatus, cie1000PoeConfigSwitchParamSwitchId=cie1000PoeConfigSwitchParamSwitchId, cie1000PoeConfigInterfaceParamEntry=cie1000PoeConfigInterfaceParamEntry, cie1000PoeConfigGlobalsInfoGroup=cie1000PoeConfigGlobalsInfoGroup, cie1000PoeCapabilitiesInterfaceInfoGroup=cie1000PoeCapabilitiesInterfaceInfoGroup, cie1000PoeConfigInterface=cie1000PoeConfigInterface, cie1000PoeConfigSwitchParamMaxPower=cie1000PoeConfigSwitchParamMaxPower, cie1000PoeMibObjects=cie1000PoeMibObjects, cie1000PoeConfigInterfaceParamMode=cie1000PoeConfigInterfaceParamMode)
