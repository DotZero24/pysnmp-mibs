#
# PySNMP MIB module CISCO-ENTITY-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-ENTITY-EXT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:13:01 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
Unsigned64, = mibBuilder.importSymbols("CISCO-TC", "Unsigned64")
entPhysicalDescr, entPhysicalContainedIn, entPhysicalIndex, entPhysicalName, entPhysicalEntry = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalDescr", "entPhysicalContainedIn", "entPhysicalIndex", "entPhysicalName", "entPhysicalEntry")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ciscoEntityExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 195))
ciscoEntityExtMIB.setRevisions(('2018-04-04 00:00', '2015-04-17 00:00', '2014-09-12 00:00', '2014-03-27 00:00', '2013-08-06 00:00', '2013-08-05 00:00', '2008-11-24 00:00', '2004-07-06 00:00', '2004-03-03 00:00', '2004-01-26 00:00', '2003-08-24 00:00', '2001-05-17 00:00', '2001-04-05 00:00',))
if mibBuilder.loadTexts: ciscoEntityExtMIB.setLastUpdated('201804040000Z')
if mibBuilder.loadTexts: ciscoEntityExtMIB.setOrganization('Cisco Systems, Inc.')
ciscoEntityExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 195, 1))
class ConfigRegisterValue(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 2)
    fixedLength = 2

class BootImageList(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

ceExtPhysicalProcessorTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 1), )
if mibBuilder.loadTexts: ceExtPhysicalProcessorTable.setStatus('current')
ceExtPhysicalProcessorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: ceExtPhysicalProcessorEntry.setStatus('current')
ceExtProcessorRam = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 1, 1, 1), Unsigned32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceExtProcessorRam.setStatus('current')
ceExtNVRAMSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 1, 1, 2), Unsigned32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceExtNVRAMSize.setStatus('current')
ceExtNVRAMUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 1, 1, 3), Unsigned32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceExtNVRAMUsed.setStatus('current')
ceExtProcessorRamOverflow = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 1, 1, 4), Unsigned32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceExtProcessorRamOverflow.setStatus('current')
ceExtHCProcessorRam = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 1, 1, 5), Unsigned64()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceExtHCProcessorRam.setStatus('current')
ceExtNVRAMSizeOverflow = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 1, 1, 6), Unsigned32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceExtNVRAMSizeOverflow.setStatus('current')
ceExtHCNVRAMSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 1, 1, 7), Unsigned64()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceExtHCNVRAMSize.setStatus('current')
ceExtNVRAMUsedOverflow = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 1, 1, 8), Unsigned32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceExtNVRAMUsedOverflow.setStatus('current')
ceExtHCNVRAMUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 1, 1, 9), Unsigned64()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceExtHCNVRAMUsed.setStatus('current')
ceExtConfigRegTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 2), )
if mibBuilder.loadTexts: ceExtConfigRegTable.setStatus('current')
ceExtConfigRegEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: ceExtConfigRegEntry.setStatus('current')
ceExtConfigRegister = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 2, 1, 1), ConfigRegisterValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceExtConfigRegister.setStatus('current')
ceExtConfigRegNext = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 2, 1, 2), ConfigRegisterValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceExtConfigRegNext.setStatus('current')
ceExtSysBootImageList = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 2, 1, 3), BootImageList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceExtSysBootImageList.setStatus('current')
ceExtKickstartImageList = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 2, 1, 4), BootImageList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceExtKickstartImageList.setStatus('current')
ceExtEntityLEDTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 3), )
if mibBuilder.loadTexts: ceExtEntityLEDTable.setStatus('current')
ceExtEntityLEDEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 3, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-ENTITY-EXT-MIB", "ceExtEntityLEDType"))
if mibBuilder.loadTexts: ceExtEntityLEDEntry.setStatus('current')
ceExtEntityLEDType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("status", 1), ("system", 2), ("active", 3), ("power", 4), ("battery", 5))))
if mibBuilder.loadTexts: ceExtEntityLEDType.setStatus('current')
ceExtEntityLEDColor = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("off", 1), ("green", 2), ("amber", 3), ("red", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceExtEntityLEDColor.setStatus('current')
ceExtEntPhysicalTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 4), )
if mibBuilder.loadTexts: ceExtEntPhysicalTable.setStatus('current')
ceExtEntPhysicalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 4, 1), )
entPhysicalEntry.registerAugmentions(("CISCO-ENTITY-EXT-MIB", "ceExtEntPhysicalEntry"))
ceExtEntPhysicalEntry.setIndexNames(*entPhysicalEntry.getIndexNames())
if mibBuilder.loadTexts: ceExtEntPhysicalEntry.setStatus('current')
ceEntPhysicalSecondSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 4, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceEntPhysicalSecondSerialNum.setStatus('current')
ceExtNotificationControlObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 5))
ceExtEntDoorNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 5, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceExtEntDoorNotifEnable.setStatus('current')
ceExtEntBreakOutPortNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 5, 2), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceExtEntBreakOutPortNotifEnable.setStatus('current')
ceExtEntUsbModemNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 5, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceExtEntUsbModemNotifEnable.setStatus('current')
ceExtUSBModemTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 6), )
if mibBuilder.loadTexts: ceExtUSBModemTable.setStatus('current')
ceExtUSBModemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 6, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: ceExtUSBModemEntry.setStatus('current')
ceExtUSBModemIMEI = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 6, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceExtUSBModemIMEI.setStatus('current')
ceExtUSBModemIMSI = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 6, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceExtUSBModemIMSI.setStatus('current')
ceExtUSBModemServiceProvider = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 6, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceExtUSBModemServiceProvider.setStatus('current')
ceExtUSBModemSignalStrength = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 6, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceExtUSBModemSignalStrength.setStatus('current')
ceExtMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 195, 2))
ciscoEntityExtMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 195, 2, 0))
ceExtEntDoorCloseNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 195, 2, 0, 1)).setObjects(("ENTITY-MIB", "entPhysicalDescr"), ("ENTITY-MIB", "entPhysicalName"))
if mibBuilder.loadTexts: ceExtEntDoorCloseNotif.setStatus('current')
ceExtEntDoorOpenNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 195, 2, 0, 2)).setObjects(("ENTITY-MIB", "entPhysicalDescr"), ("ENTITY-MIB", "entPhysicalName"))
if mibBuilder.loadTexts: ceExtEntDoorOpenNotif.setStatus('current')
ceExtBreakOutPortInserted = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 195, 2, 0, 3)).setObjects(("ENTITY-MIB", "entPhysicalContainedIn"), ("ENTITY-MIB", "entPhysicalName"))
if mibBuilder.loadTexts: ceExtBreakOutPortInserted.setStatus('current')
ceExtBreakOutPortRemoved = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 195, 2, 0, 4)).setObjects(("ENTITY-MIB", "entPhysicalContainedIn"), ("ENTITY-MIB", "entPhysicalName"))
if mibBuilder.loadTexts: ceExtBreakOutPortRemoved.setStatus('current')
ceExtUSBModemPlugInNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 195, 2, 0, 5)).setObjects(("ENTITY-MIB", "entPhysicalContainedIn"), ("ENTITY-MIB", "entPhysicalDescr"))
if mibBuilder.loadTexts: ceExtUSBModemPlugInNotif.setStatus('current')
ceExtUSBModemPlugOutNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 195, 2, 0, 6)).setObjects(("ENTITY-MIB", "entPhysicalContainedIn"), ("ENTITY-MIB", "entPhysicalDescr"))
if mibBuilder.loadTexts: ceExtUSBModemPlugOutNotif.setStatus('current')
ciscoEntityExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 195, 3))
ciscoEntityExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 1))
ciscoEntityExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2))
ciscoEntityExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 1, 1)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceExtPhysicalProcessorGroup"), ("CISCO-ENTITY-EXT-MIB", "ciscoEntityExtConfigRegGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtSysBootImageListGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityExtMIBCompliance = ciscoEntityExtMIBCompliance.setStatus('deprecated')
ciscoEntityExtMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 1, 2)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceExtPhysicalProcessorGroup"), ("CISCO-ENTITY-EXT-MIB", "ciscoEntityExtConfigRegGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtSysBootImageListGroup"), ("CISCO-ENTITY-EXT-MIB", "ciscoEntityExtLEDGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtSysBootImageListGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityExtMIBComplianceRev1 = ciscoEntityExtMIBComplianceRev1.setStatus('deprecated')
ciscoEntityExtMIBComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 1, 3)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceExtPhysicalProcessorGroup"), ("CISCO-ENTITY-EXT-MIB", "ciscoEntityExtConfigRegGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtSysBootImageListGroup"), ("CISCO-ENTITY-EXT-MIB", "ciscoEntityExtLEDGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtSysBootImageListGroupRev1"), ("CISCO-ENTITY-EXT-MIB", "ciscoExtEntityPhysicalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityExtMIBComplianceRev2 = ciscoEntityExtMIBComplianceRev2.setStatus('deprecated')
ciscoEntityExtMIBComplianceRev3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 1, 4)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceExtPhysicalProcessorGroup"), ("CISCO-ENTITY-EXT-MIB", "ciscoEntityExtConfigRegGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtSysBootImageListGroup"), ("CISCO-ENTITY-EXT-MIB", "ciscoEntityExtLEDGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtSysBootImageListGroupRev1"), ("CISCO-ENTITY-EXT-MIB", "ciscoExtEntityPhysicalGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtPhyProcessorOverflowGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtPhyProcessorHCGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityExtMIBComplianceRev3 = ciscoEntityExtMIBComplianceRev3.setStatus('deprecated')
ciscoEntityExtMIBComplianceRev4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 1, 5)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceExtPhysicalProcessorGroup"), ("CISCO-ENTITY-EXT-MIB", "ciscoEntityExtConfigRegGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtSysBootImageListGroup"), ("CISCO-ENTITY-EXT-MIB", "ciscoEntityExtLEDGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtSysBootImageListGroupRev1"), ("CISCO-ENTITY-EXT-MIB", "ciscoExtEntityPhysicalGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtPhyProcessorOverflowGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtPhyProcessorHCGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtEntDoorNotifGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtEntDoorNotifControlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityExtMIBComplianceRev4 = ciscoEntityExtMIBComplianceRev4.setStatus('deprecated')
ciscoEntityExtMIBComplianceRev5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 1, 6)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceExtPhysicalProcessorGroup"), ("CISCO-ENTITY-EXT-MIB", "ciscoEntityExtConfigRegGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtSysBootImageListGroup"), ("CISCO-ENTITY-EXT-MIB", "ciscoEntityExtLEDGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtSysBootImageListGroupRev1"), ("CISCO-ENTITY-EXT-MIB", "ciscoExtEntityPhysicalGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtPhyProcessorOverflowGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtPhyProcessorHCGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtEntDoorNotifGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtEntDoorNotifControlGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtBreakOutPortNotifGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtBreakOutPortNotifControlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityExtMIBComplianceRev5 = ciscoEntityExtMIBComplianceRev5.setStatus('deprecated')
ciscoEntityExtMIBComplianceRev6 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 1, 7)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceExtPhysicalProcessorGroup"), ("CISCO-ENTITY-EXT-MIB", "ciscoEntityExtConfigRegGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtSysBootImageListGroup"), ("CISCO-ENTITY-EXT-MIB", "ciscoEntityExtLEDGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtSysBootImageListGroupRev1"), ("CISCO-ENTITY-EXT-MIB", "ciscoExtEntityPhysicalGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtPhyProcessorOverflowGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtPhyProcessorHCGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtEntDoorNotifGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtEntDoorNotifControlGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtBreakOutPortNotifGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtBreakOutPortNotifControlGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtUSBModemGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtUsbModemNotificationsGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtUsbModemNotifControlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityExtMIBComplianceRev6 = ciscoEntityExtMIBComplianceRev6.setStatus('current')
ceExtPhysicalProcessorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 1)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceExtProcessorRam"), ("CISCO-ENTITY-EXT-MIB", "ceExtNVRAMSize"), ("CISCO-ENTITY-EXT-MIB", "ceExtNVRAMUsed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceExtPhysicalProcessorGroup = ceExtPhysicalProcessorGroup.setStatus('current')
ciscoEntityExtConfigRegGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 2)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceExtConfigRegister"), ("CISCO-ENTITY-EXT-MIB", "ceExtConfigRegNext"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityExtConfigRegGroup = ciscoEntityExtConfigRegGroup.setStatus('current')
ceExtSysBootImageListGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 3)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceExtSysBootImageList"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceExtSysBootImageListGroup = ceExtSysBootImageListGroup.setStatus('current')
ciscoEntityExtLEDGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 4)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceExtEntityLEDColor"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityExtLEDGroup = ciscoEntityExtLEDGroup.setStatus('current')
ceExtSysBootImageListGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 5)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceExtKickstartImageList"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceExtSysBootImageListGroupRev1 = ceExtSysBootImageListGroupRev1.setStatus('current')
ciscoExtEntityPhysicalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 6)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceEntPhysicalSecondSerialNum"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoExtEntityPhysicalGroup = ciscoExtEntityPhysicalGroup.setStatus('current')
ceExtPhyProcessorOverflowGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 7)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceExtProcessorRamOverflow"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceExtPhyProcessorOverflowGroup = ceExtPhyProcessorOverflowGroup.setStatus('current')
ceExtPhyProcessorHCGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 8)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceExtHCProcessorRam"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceExtPhyProcessorHCGroup = ceExtPhyProcessorHCGroup.setStatus('current')
ceExtEntDoorNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 9)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceExtEntDoorCloseNotif"), ("CISCO-ENTITY-EXT-MIB", "ceExtEntDoorOpenNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceExtEntDoorNotifGroup = ceExtEntDoorNotifGroup.setStatus('current')
ceExtEntDoorNotifControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 10)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceExtEntDoorNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceExtEntDoorNotifControlGroup = ceExtEntDoorNotifControlGroup.setStatus('current')
ceExtBreakOutPortNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 11)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceExtBreakOutPortInserted"), ("CISCO-ENTITY-EXT-MIB", "ceExtBreakOutPortRemoved"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceExtBreakOutPortNotifGroup = ceExtBreakOutPortNotifGroup.setStatus('current')
ceExtBreakOutPortNotifControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 12)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceExtEntBreakOutPortNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceExtBreakOutPortNotifControlGroup = ceExtBreakOutPortNotifControlGroup.setStatus('current')
ceExtUSBModemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 13)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceExtUSBModemIMEI"), ("CISCO-ENTITY-EXT-MIB", "ceExtUSBModemIMSI"), ("CISCO-ENTITY-EXT-MIB", "ceExtUSBModemServiceProvider"), ("CISCO-ENTITY-EXT-MIB", "ceExtUSBModemSignalStrength"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceExtUSBModemGroup = ceExtUSBModemGroup.setStatus('current')
ceExtUsbModemNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 14)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceExtUSBModemPlugInNotif"), ("CISCO-ENTITY-EXT-MIB", "ceExtUSBModemPlugOutNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceExtUsbModemNotificationsGroup = ceExtUsbModemNotificationsGroup.setStatus('current')
ceExtUsbModemNotifControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 15)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceExtEntUsbModemNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceExtUsbModemNotifControlGroup = ceExtUsbModemNotifControlGroup.setStatus('current')
ceExtNVRAMOverflowGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 16)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceExtNVRAMSizeOverflow"), ("CISCO-ENTITY-EXT-MIB", "ceExtNVRAMUsedOverflow"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceExtNVRAMOverflowGroup = ceExtNVRAMOverflowGroup.setStatus('current')
ceExtHCNVRAMGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 17)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceExtHCNVRAMSize"), ("CISCO-ENTITY-EXT-MIB", "ceExtHCNVRAMUsed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceExtHCNVRAMGroup = ceExtHCNVRAMGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ENTITY-EXT-MIB", ceExtEntBreakOutPortNotifEnable=ceExtEntBreakOutPortNotifEnable, ceExtEntUsbModemNotifEnable=ceExtEntUsbModemNotifEnable, ceExtEntDoorNotifControlGroup=ceExtEntDoorNotifControlGroup, ceExtSysBootImageListGroup=ceExtSysBootImageListGroup, ciscoEntityExtMIBCompliances=ciscoEntityExtMIBCompliances, ceExtSysBootImageList=ceExtSysBootImageList, ciscoEntityExtMIBComplianceRev4=ciscoEntityExtMIBComplianceRev4, ceExtUSBModemIMSI=ceExtUSBModemIMSI, ceExtNVRAMUsed=ceExtNVRAMUsed, ceExtConfigRegTable=ceExtConfigRegTable, ciscoEntityExtMIBNotifications=ciscoEntityExtMIBNotifications, ceExtUSBModemPlugOutNotif=ceExtUSBModemPlugOutNotif, ciscoEntityExtMIBComplianceRev5=ciscoEntityExtMIBComplianceRev5, BootImageList=BootImageList, ceExtProcessorRam=ceExtProcessorRam, ceExtHCNVRAMUsed=ceExtHCNVRAMUsed, ceExtNotificationControlObjects=ceExtNotificationControlObjects, ceExtHCProcessorRam=ceExtHCProcessorRam, ceExtBreakOutPortInserted=ceExtBreakOutPortInserted, ceExtSysBootImageListGroupRev1=ceExtSysBootImageListGroupRev1, ceExtConfigRegister=ceExtConfigRegister, ceExtNVRAMOverflowGroup=ceExtNVRAMOverflowGroup, ceExtEntityLEDType=ceExtEntityLEDType, ceExtUSBModemEntry=ceExtUSBModemEntry, ciscoEntityExtMIBConformance=ciscoEntityExtMIBConformance, ciscoEntityExtLEDGroup=ciscoEntityExtLEDGroup, ceEntPhysicalSecondSerialNum=ceEntPhysicalSecondSerialNum, ciscoEntityExtMIB=ciscoEntityExtMIB, ConfigRegisterValue=ConfigRegisterValue, ceExtPhyProcessorOverflowGroup=ceExtPhyProcessorOverflowGroup, ceExtEntityLEDTable=ceExtEntityLEDTable, ceExtUSBModemServiceProvider=ceExtUSBModemServiceProvider, ceExtUsbModemNotificationsGroup=ceExtUsbModemNotificationsGroup, ceExtEntPhysicalEntry=ceExtEntPhysicalEntry, ceExtHCNVRAMSize=ceExtHCNVRAMSize, ceExtNVRAMSizeOverflow=ceExtNVRAMSizeOverflow, ceExtUSBModemTable=ceExtUSBModemTable, ciscoExtEntityPhysicalGroup=ciscoExtEntityPhysicalGroup, ceExtUsbModemNotifControlGroup=ceExtUsbModemNotifControlGroup, ceExtMIBNotificationPrefix=ceExtMIBNotificationPrefix, ceExtEntityLEDColor=ceExtEntityLEDColor, ceExtBreakOutPortNotifControlGroup=ceExtBreakOutPortNotifControlGroup, ceExtBreakOutPortRemoved=ceExtBreakOutPortRemoved, ceExtProcessorRamOverflow=ceExtProcessorRamOverflow, ceExtEntDoorNotifEnable=ceExtEntDoorNotifEnable, ceExtEntPhysicalTable=ceExtEntPhysicalTable, ciscoEntityExtMIBComplianceRev3=ciscoEntityExtMIBComplianceRev3, ciscoEntityExtMIBComplianceRev6=ciscoEntityExtMIBComplianceRev6, ciscoEntityExtMIBGroups=ciscoEntityExtMIBGroups, ceExtConfigRegEntry=ceExtConfigRegEntry, ceExtKickstartImageList=ceExtKickstartImageList, ciscoEntityExtConfigRegGroup=ciscoEntityExtConfigRegGroup, ceExtBreakOutPortNotifGroup=ceExtBreakOutPortNotifGroup, ceExtEntDoorCloseNotif=ceExtEntDoorCloseNotif, ceExtPhysicalProcessorGroup=ceExtPhysicalProcessorGroup, ceExtUSBModemGroup=ceExtUSBModemGroup, ceExtConfigRegNext=ceExtConfigRegNext, ciscoEntityExtMIBComplianceRev2=ciscoEntityExtMIBComplianceRev2, PYSNMP_MODULE_ID=ciscoEntityExtMIB, ceExtEntDoorNotifGroup=ceExtEntDoorNotifGroup, ceExtUSBModemPlugInNotif=ceExtUSBModemPlugInNotif, ceExtHCNVRAMGroup=ceExtHCNVRAMGroup, ceExtPhysicalProcessorTable=ceExtPhysicalProcessorTable, ceExtNVRAMSize=ceExtNVRAMSize, ceExtEntDoorOpenNotif=ceExtEntDoorOpenNotif, ceExtUSBModemSignalStrength=ceExtUSBModemSignalStrength, ciscoEntityExtMIBObjects=ciscoEntityExtMIBObjects, ceExtEntityLEDEntry=ceExtEntityLEDEntry, ceExtUSBModemIMEI=ceExtUSBModemIMEI, ciscoEntityExtMIBComplianceRev1=ciscoEntityExtMIBComplianceRev1, ciscoEntityExtMIBCompliance=ciscoEntityExtMIBCompliance, ceExtNVRAMUsedOverflow=ceExtNVRAMUsedOverflow, ceExtPhysicalProcessorEntry=ceExtPhysicalProcessorEntry, ceExtPhyProcessorHCGroup=ceExtPhyProcessorHCGroup)
