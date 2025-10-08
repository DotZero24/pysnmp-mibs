#
# PySNMP MIB module OS-DEVICE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/mrv/OS-DEVICE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:16:21 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
oaOptiSwitch, = mibBuilder.importSymbols("OS-COMMON-TC-MIB", "oaOptiSwitch")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
osDevice = ModuleIdentity((1, 3, 6, 1, 4, 1, 6926, 2, 40))
osDevice.setRevisions(('2019-04-04 00:00', '2016-09-14 00:00',))
if mibBuilder.loadTexts: osDevice.setLastUpdated('201904040000Z')
if mibBuilder.loadTexts: osDevice.setOrganization('MRV Communications, Inc.')
osDevNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 40, 0))
osDevModule = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 40, 1))
osDevParams = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 40, 2))
osDevSerial = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 40, 2, 1))
osDevConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 40, 101))
osDevMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 40, 101, 1))
osDevMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 40, 101, 2))
class DevModuleType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("none", 1), ("lte0", 2), ("vdsl0", 3))

class SerialBaudRate(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(9600, 9600), ValueRangeConstraint(115200, 115200), )
osDevModuleType = MibScalar((1, 3, 6, 1, 4, 1, 6926, 2, 40, 1, 1), DevModuleType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: osDevModuleType.setStatus('current')
osDevModuleSlotNumber = MibScalar((1, 3, 6, 1, 4, 1, 6926, 2, 40, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: osDevModuleSlotNumber.setStatus('current')
osDevSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 6926, 2, 40, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: osDevSerialNumber.setStatus('current')
osDevSerialTable = MibTable((1, 3, 6, 1, 4, 1, 6926, 2, 40, 2, 1, 2), )
if mibBuilder.loadTexts: osDevSerialTable.setStatus('current')
osDevSerialEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6926, 2, 40, 2, 1, 2, 1), ).setIndexNames((0, "OS-DEVICE-MIB", "osDevSerialIndex"))
if mibBuilder.loadTexts: osDevSerialEntry.setStatus('current')
osDevSerialIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 40, 2, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: osDevSerialIndex.setStatus('current')
osDevSerialOperBaudrate = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 40, 2, 1, 2, 1, 2), SerialBaudRate()).setMaxAccess("readonly")
if mibBuilder.loadTexts: osDevSerialOperBaudrate.setStatus('current')
osDevSerialAdminBaudrate = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 40, 2, 1, 2, 1, 3), SerialBaudRate()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osDevSerialAdminBaudrate.setStatus('current')
osDevModuleInserted = NotificationType((1, 3, 6, 1, 4, 1, 6926, 2, 40, 0, 1)).setObjects(("OS-DEVICE-MIB", "osDevModuleSlotNumber"), ("OS-DEVICE-MIB", "osDevModuleType"))
if mibBuilder.loadTexts: osDevModuleInserted.setStatus('current')
osDevModuleRemoved = NotificationType((1, 3, 6, 1, 4, 1, 6926, 2, 40, 0, 2)).setObjects(("OS-DEVICE-MIB", "osDevModuleSlotNumber"), ("OS-DEVICE-MIB", "osDevModuleType"))
if mibBuilder.loadTexts: osDevModuleRemoved.setStatus('current')
osDevModuleLedPowerOn = NotificationType((1, 3, 6, 1, 4, 1, 6926, 2, 40, 0, 3)).setObjects(("OS-DEVICE-MIB", "osDevModuleSlotNumber"), ("OS-DEVICE-MIB", "osDevModuleType"))
if mibBuilder.loadTexts: osDevModuleLedPowerOn.setStatus('current')
osDevModuleLedPowerOff = NotificationType((1, 3, 6, 1, 4, 1, 6926, 2, 40, 0, 4)).setObjects(("OS-DEVICE-MIB", "osDevModuleSlotNumber"), ("OS-DEVICE-MIB", "osDevModuleType"))
if mibBuilder.loadTexts: osDevModuleLedPowerOff.setStatus('current')
osDevModuleLedWanOn = NotificationType((1, 3, 6, 1, 4, 1, 6926, 2, 40, 0, 5)).setObjects(("OS-DEVICE-MIB", "osDevModuleSlotNumber"), ("OS-DEVICE-MIB", "osDevModuleType"))
if mibBuilder.loadTexts: osDevModuleLedWanOn.setStatus('current')
osDevModuleLedWanOff = NotificationType((1, 3, 6, 1, 4, 1, 6926, 2, 40, 0, 6)).setObjects(("OS-DEVICE-MIB", "osDevModuleSlotNumber"), ("OS-DEVICE-MIB", "osDevModuleType"))
if mibBuilder.loadTexts: osDevModuleLedWanOff.setStatus('current')
osDevModuleLedConnOn = NotificationType((1, 3, 6, 1, 4, 1, 6926, 2, 40, 0, 7)).setObjects(("OS-DEVICE-MIB", "osDevModuleSlotNumber"), ("OS-DEVICE-MIB", "osDevModuleType"))
if mibBuilder.loadTexts: osDevModuleLedConnOn.setStatus('current')
osDevModuleLedConnOff = NotificationType((1, 3, 6, 1, 4, 1, 6926, 2, 40, 0, 8)).setObjects(("OS-DEVICE-MIB", "osDevModuleSlotNumber"), ("OS-DEVICE-MIB", "osDevModuleType"))
if mibBuilder.loadTexts: osDevModuleLedConnOff.setStatus('current')
osDevMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6926, 2, 40, 101, 1, 1)).setObjects(("OS-DEVICE-MIB", "osDevMandatoryGroup"), ("OS-DEVICE-MIB", "osDevNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    osDevMIBCompliance = osDevMIBCompliance.setStatus('current')
osDevMandatoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6926, 2, 40, 101, 2, 1)).setObjects(("OS-DEVICE-MIB", "osDevModuleSlotNumber"), ("OS-DEVICE-MIB", "osDevModuleType"), ("OS-DEVICE-MIB", "osDevSerialNumber"), ("OS-DEVICE-MIB", "osDevSerialOperBaudrate"), ("OS-DEVICE-MIB", "osDevSerialAdminBaudrate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    osDevMandatoryGroup = osDevMandatoryGroup.setStatus('current')
osDevNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6926, 2, 40, 101, 2, 2)).setObjects(("OS-DEVICE-MIB", "osDevModuleInserted"), ("OS-DEVICE-MIB", "osDevModuleRemoved"), ("OS-DEVICE-MIB", "osDevModuleLedPowerOn"), ("OS-DEVICE-MIB", "osDevModuleLedPowerOff"), ("OS-DEVICE-MIB", "osDevModuleLedWanOn"), ("OS-DEVICE-MIB", "osDevModuleLedWanOff"), ("OS-DEVICE-MIB", "osDevModuleLedConnOn"), ("OS-DEVICE-MIB", "osDevModuleLedConnOff"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    osDevNotificationsGroup = osDevNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("OS-DEVICE-MIB", DevModuleType=DevModuleType, osDevModuleType=osDevModuleType, osDevModuleLedPowerOn=osDevModuleLedPowerOn, osDevice=osDevice, osDevModuleSlotNumber=osDevModuleSlotNumber, osDevMandatoryGroup=osDevMandatoryGroup, osDevModuleLedWanOff=osDevModuleLedWanOff, osDevMIBCompliance=osDevMIBCompliance, osDevModule=osDevModule, osDevParams=osDevParams, osDevConformance=osDevConformance, osDevModuleLedWanOn=osDevModuleLedWanOn, osDevMIBGroups=osDevMIBGroups, osDevSerialOperBaudrate=osDevSerialOperBaudrate, osDevModuleLedConnOn=osDevModuleLedConnOn, osDevNotificationsGroup=osDevNotificationsGroup, PYSNMP_MODULE_ID=osDevice, osDevSerialIndex=osDevSerialIndex, osDevSerialEntry=osDevSerialEntry, SerialBaudRate=SerialBaudRate, osDevSerialTable=osDevSerialTable, osDevModuleRemoved=osDevModuleRemoved, osDevSerialNumber=osDevSerialNumber, osDevNotifications=osDevNotifications, osDevModuleInserted=osDevModuleInserted, osDevSerial=osDevSerial, osDevSerialAdminBaudrate=osDevSerialAdminBaudrate, osDevModuleLedConnOff=osDevModuleLedConnOff, osDevMIBCompliances=osDevMIBCompliances, osDevModuleLedPowerOff=osDevModuleLedPowerOff)
