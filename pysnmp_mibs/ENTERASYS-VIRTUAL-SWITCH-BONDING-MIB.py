#
# PySNMP MIB module ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/enterasys/ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:17:18 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, TimeStamp, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TimeStamp", "TruthValue", "TextualConvention")
etsysVirtualSwitchBondingMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 83))
etsysVirtualSwitchBondingMIB.setRevisions(('2012-03-13 19:14', '2012-02-07 15:53', '2011-12-13 20:31',))
if mibBuilder.loadTexts: etsysVirtualSwitchBondingMIB.setLastUpdated('201203131914Z')
if mibBuilder.loadTexts: etsysVirtualSwitchBondingMIB.setOrganization('Enterasys Networks, Inc')
etsysVsbObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1))
etsysVsbSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 1))
etsysVsbChassis = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 2))
etsysVsbPort = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 3))
class VsbId(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(8, 8), )
class VsbChassisStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("up", 1), ("down", 2), ("incomplete", 3), ("inactive", 4))

class VsbSlotList(TextualConvention, OctetString):
    status = 'current'

etsysVsbSystemEnable = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysVsbSystemEnable.setStatus('current')
etsysVsbSystemMaxChassis = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysVsbSystemMaxChassis.setStatus('current')
etsysVsbSystemMaxSlotNumber = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysVsbSystemMaxSlotNumber.setStatus('current')
etsysVsbAdministrativeMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 1, 4), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysVsbAdministrativeMacAddress.setStatus('current')
etsysVsbOperationalMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 1, 5), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysVsbOperationalMacAddress.setStatus('current')
etsysVsbSystemLinkFailureResponse = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysVsbSystemLinkFailureResponse.setStatus('current')
etsysVsbChassisTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 2, 1), )
if mibBuilder.loadTexts: etsysVsbChassisTable.setStatus('current')
etsysVsbChassisEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 2, 1, 1), ).setIndexNames((0, "ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbChassisIndex"))
if mibBuilder.loadTexts: etsysVsbChassisEntry.setStatus('current')
etsysVsbChassisIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 2, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: etsysVsbChassisIndex.setStatus('current')
etsysVsbChassisSystemId = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 2, 1, 1, 2), VsbId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysVsbChassisSystemId.setStatus('current')
etsysVsbChassisSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 2, 1, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysVsbChassisSerialNum.setStatus('current')
etsysVsbChassisFirstSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 2, 1, 1, 4), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysVsbChassisFirstSlotNumber.setStatus('current')
etsysVsbChassisLocalSlotList = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 2, 1, 1, 5), VsbSlotList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysVsbChassisLocalSlotList.setStatus('current')
etsysVsbChassisSystemSlotList = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 2, 1, 1, 6), VsbSlotList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysVsbChassisSystemSlotList.setStatus('current')
etsysVsbChassisStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 2, 1, 1, 7), VsbChassisStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysVsbChassisStatus.setStatus('current')
etsysVsbChassisLastBondTime = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 2, 1, 1, 8), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysVsbChassisLastBondTime.setStatus('current')
etsysVsbChassisSharedSecret = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 2, 1, 1, 9), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysVsbChassisSharedSecret.setStatus('current')
etsysVsbChassisSecretEntered = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 2, 1, 1, 10), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysVsbChassisSecretEntered.setStatus('current')
etsysVsbChassisLfrOperPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 2, 1, 1, 11), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysVsbChassisLfrOperPriority.setStatus('current')
etsysVsbPortTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 3, 1), )
if mibBuilder.loadTexts: etsysVsbPortTable.setStatus('current')
etsysVsbPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: etsysVsbPortEntry.setStatus('current')
etsysVsbPortAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2))).clone('down')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysVsbPortAdminStatus.setStatus('current')
etsysVsbPortOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("highLatency", 3), ("probeLoop", 4), ("probeTimeout", 5), ("portInstability", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysVsbPortOperStatus.setStatus('current')
etsysVsbConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 2))
etsysVsbGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 2, 1))
etsysVsbCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 2, 2))
etsysVsbSystemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 2, 1, 1)).setObjects(("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbSystemEnable"), ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbSystemMaxChassis"), ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbSystemMaxSlotNumber"), ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbAdministrativeMacAddress"), ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbOperationalMacAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysVsbSystemGroup = etsysVsbSystemGroup.setStatus('deprecated')
etsysVsbChassisGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 2, 1, 2)).setObjects(("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbChassisSystemId"), ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbChassisSerialNum"), ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbChassisFirstSlotNumber"), ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbChassisLocalSlotList"), ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbChassisSystemSlotList"), ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbChassisStatus"), ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbChassisLastBondTime"), ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbChassisSharedSecret"), ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbChassisSecretEntered"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysVsbChassisGroup = etsysVsbChassisGroup.setStatus('deprecated')
etsysVsbPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 2, 1, 3)).setObjects(("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbPortAdminStatus"), ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbPortOperStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysVsbPortGroup = etsysVsbPortGroup.setStatus('current')
etsysVsbSystemGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 2, 1, 4)).setObjects(("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbSystemEnable"), ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbSystemMaxChassis"), ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbSystemMaxSlotNumber"), ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbAdministrativeMacAddress"), ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbOperationalMacAddress"), ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbSystemLinkFailureResponse"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysVsbSystemGroup2 = etsysVsbSystemGroup2.setStatus('current')
etsysVsbChassisGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 2, 1, 5)).setObjects(("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbChassisSystemId"), ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbChassisSerialNum"), ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbChassisFirstSlotNumber"), ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbChassisLocalSlotList"), ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbChassisSystemSlotList"), ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbChassisStatus"), ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbChassisLastBondTime"), ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbChassisSharedSecret"), ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbChassisSecretEntered"), ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbChassisLfrOperPriority"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysVsbChassisGroup2 = etsysVsbChassisGroup2.setStatus('current')
etsysVsbCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 2, 2, 1)).setObjects(("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbSystemGroup"), ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbChassisGroup"), ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbPortGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysVsbCompliance = etsysVsbCompliance.setStatus('deprecated')
etsysVsbCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 83, 2, 2, 2)).setObjects(("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbSystemGroup2"), ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbChassisGroup2"), ("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", "etsysVsbPortGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysVsbCompliance2 = etsysVsbCompliance2.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB", etsysVsbSystemMaxSlotNumber=etsysVsbSystemMaxSlotNumber, etsysVirtualSwitchBondingMIB=etsysVirtualSwitchBondingMIB, etsysVsbSystemMaxChassis=etsysVsbSystemMaxChassis, etsysVsbSystemLinkFailureResponse=etsysVsbSystemLinkFailureResponse, etsysVsbPortOperStatus=etsysVsbPortOperStatus, etsysVsbChassis=etsysVsbChassis, etsysVsbChassisTable=etsysVsbChassisTable, etsysVsbSystemGroup2=etsysVsbSystemGroup2, etsysVsbPortTable=etsysVsbPortTable, etsysVsbCompliance2=etsysVsbCompliance2, etsysVsbChassisLastBondTime=etsysVsbChassisLastBondTime, etsysVsbPortEntry=etsysVsbPortEntry, etsysVsbOperationalMacAddress=etsysVsbOperationalMacAddress, etsysVsbPortGroup=etsysVsbPortGroup, etsysVsbObjects=etsysVsbObjects, etsysVsbChassisGroup=etsysVsbChassisGroup, VsbChassisStatus=VsbChassisStatus, VsbSlotList=VsbSlotList, etsysVsbChassisStatus=etsysVsbChassisStatus, etsysVsbChassisLfrOperPriority=etsysVsbChassisLfrOperPriority, etsysVsbAdministrativeMacAddress=etsysVsbAdministrativeMacAddress, etsysVsbSystemGroup=etsysVsbSystemGroup, PYSNMP_MODULE_ID=etsysVirtualSwitchBondingMIB, etsysVsbChassisSharedSecret=etsysVsbChassisSharedSecret, etsysVsbChassisSystemSlotList=etsysVsbChassisSystemSlotList, etsysVsbChassisSecretEntered=etsysVsbChassisSecretEntered, etsysVsbChassisIndex=etsysVsbChassisIndex, etsysVsbChassisLocalSlotList=etsysVsbChassisLocalSlotList, etsysVsbSystem=etsysVsbSystem, VsbId=VsbId, etsysVsbChassisEntry=etsysVsbChassisEntry, etsysVsbChassisFirstSlotNumber=etsysVsbChassisFirstSlotNumber, etsysVsbChassisSerialNum=etsysVsbChassisSerialNum, etsysVsbPort=etsysVsbPort, etsysVsbConformance=etsysVsbConformance, etsysVsbSystemEnable=etsysVsbSystemEnable, etsysVsbGroups=etsysVsbGroups, etsysVsbCompliances=etsysVsbCompliances, etsysVsbChassisGroup2=etsysVsbChassisGroup2, etsysVsbChassisSystemId=etsysVsbChassisSystemId, etsysVsbCompliance=etsysVsbCompliance, etsysVsbPortAdminStatus=etsysVsbPortAdminStatus)
