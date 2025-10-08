#
# PySNMP MIB module CISCO-ENTITY-ASSET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-ENTITY-ASSET-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:30:27 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
ciscoEntityAssetMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 92))
ciscoEntityAssetMIB.setRevisions(('2003-09-18 00:00', '2002-07-23 16:00', '1999-06-02 16:00',))
if mibBuilder.loadTexts: ciscoEntityAssetMIB.setLastUpdated('200309180000Z')
if mibBuilder.loadTexts: ciscoEntityAssetMIB.setOrganization('Cisco Systems, Inc.')
ciscoEntityAssetMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 92, 1))
ceAssetTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 92, 1, 1), )
if mibBuilder.loadTexts: ceAssetTable.setStatus('current')
ceAssetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 92, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: ceAssetEntry.setStatus('current')
ceAssetOEMString = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 92, 1, 1, 1, 1), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceAssetOEMString.setStatus('deprecated')
ceAssetSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 92, 1, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceAssetSerialNumber.setStatus('deprecated')
ceAssetOrderablePartNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 92, 1, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceAssetOrderablePartNumber.setStatus('deprecated')
ceAssetHardwareRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 92, 1, 1, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceAssetHardwareRevision.setStatus('deprecated')
ceAssetMfgAssyNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 92, 1, 1, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceAssetMfgAssyNumber.setStatus('current')
ceAssetMfgAssyRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 92, 1, 1, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceAssetMfgAssyRevision.setStatus('current')
ceAssetFirmwareID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 92, 1, 1, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceAssetFirmwareID.setStatus('deprecated')
ceAssetFirmwareRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 92, 1, 1, 1, 8), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceAssetFirmwareRevision.setStatus('deprecated')
ceAssetSoftwareID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 92, 1, 1, 1, 9), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceAssetSoftwareID.setStatus('deprecated')
ceAssetSoftwareRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 92, 1, 1, 1, 10), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceAssetSoftwareRevision.setStatus('deprecated')
ceAssetCLEI = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 92, 1, 1, 1, 11), SnmpAdminString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(10, 10), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceAssetCLEI.setStatus('current')
ceAssetAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 92, 1, 1, 1, 12), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceAssetAlias.setStatus('deprecated')
ceAssetTag = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 92, 1, 1, 1, 13), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceAssetTag.setStatus('deprecated')
ceAssetIsFRU = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 92, 1, 1, 1, 14), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceAssetIsFRU.setStatus('deprecated')
ciscoEntityAssetMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 92, 2))
ciscoEntityAssetMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 92, 2, 0))
ciscoEntityAssetMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 92, 3))
ciscoEntityAssetMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 92, 3, 1))
ciscoEntityAssetMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 92, 3, 2))
ciscoEntityAssetMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 92, 3, 1, 1)).setObjects(("CISCO-ENTITY-ASSET-MIB", "ceAssetGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityAssetMIBCompliance = ciscoEntityAssetMIBCompliance.setStatus('deprecated')
ciscoEntityAssetMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 92, 3, 1, 2)).setObjects(("CISCO-ENTITY-ASSET-MIB", "ceAssetGroupRev1"), ("CISCO-ENTITY-ASSET-MIB", "ceAssetEntityGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityAssetMIBComplianceRev1 = ciscoEntityAssetMIBComplianceRev1.setStatus('deprecated')
ciscoEntityAssetMIBComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 92, 3, 1, 3)).setObjects(("CISCO-ENTITY-ASSET-MIB", "ceAssetGroupRev2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityAssetMIBComplianceRev2 = ciscoEntityAssetMIBComplianceRev2.setStatus('current')
ceAssetGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 92, 3, 2, 1)).setObjects(("CISCO-ENTITY-ASSET-MIB", "ceAssetOEMString"), ("CISCO-ENTITY-ASSET-MIB", "ceAssetSerialNumber"), ("CISCO-ENTITY-ASSET-MIB", "ceAssetOrderablePartNumber"), ("CISCO-ENTITY-ASSET-MIB", "ceAssetHardwareRevision"), ("CISCO-ENTITY-ASSET-MIB", "ceAssetMfgAssyNumber"), ("CISCO-ENTITY-ASSET-MIB", "ceAssetMfgAssyRevision"), ("CISCO-ENTITY-ASSET-MIB", "ceAssetFirmwareID"), ("CISCO-ENTITY-ASSET-MIB", "ceAssetFirmwareRevision"), ("CISCO-ENTITY-ASSET-MIB", "ceAssetSoftwareID"), ("CISCO-ENTITY-ASSET-MIB", "ceAssetSoftwareRevision"), ("CISCO-ENTITY-ASSET-MIB", "ceAssetCLEI"), ("CISCO-ENTITY-ASSET-MIB", "ceAssetAlias"), ("CISCO-ENTITY-ASSET-MIB", "ceAssetTag"), ("CISCO-ENTITY-ASSET-MIB", "ceAssetIsFRU"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceAssetGroup = ceAssetGroup.setStatus('deprecated')
ceAssetGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 92, 3, 2, 2)).setObjects(("CISCO-ENTITY-ASSET-MIB", "ceAssetOEMString"), ("CISCO-ENTITY-ASSET-MIB", "ceAssetMfgAssyNumber"), ("CISCO-ENTITY-ASSET-MIB", "ceAssetMfgAssyRevision"), ("CISCO-ENTITY-ASSET-MIB", "ceAssetFirmwareID"), ("CISCO-ENTITY-ASSET-MIB", "ceAssetSoftwareID"), ("CISCO-ENTITY-ASSET-MIB", "ceAssetCLEI"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceAssetGroupRev1 = ceAssetGroupRev1.setStatus('deprecated')
ceAssetEntityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 92, 3, 2, 3)).setObjects(("CISCO-ENTITY-ASSET-MIB", "ceAssetOrderablePartNumber"), ("CISCO-ENTITY-ASSET-MIB", "ceAssetSerialNumber"), ("CISCO-ENTITY-ASSET-MIB", "ceAssetHardwareRevision"), ("CISCO-ENTITY-ASSET-MIB", "ceAssetFirmwareRevision"), ("CISCO-ENTITY-ASSET-MIB", "ceAssetSoftwareRevision"), ("CISCO-ENTITY-ASSET-MIB", "ceAssetAlias"), ("CISCO-ENTITY-ASSET-MIB", "ceAssetTag"), ("CISCO-ENTITY-ASSET-MIB", "ceAssetIsFRU"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceAssetEntityGroup = ceAssetEntityGroup.setStatus('deprecated')
ceAssetGroupRev2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 92, 3, 2, 4)).setObjects(("CISCO-ENTITY-ASSET-MIB", "ceAssetMfgAssyNumber"), ("CISCO-ENTITY-ASSET-MIB", "ceAssetMfgAssyRevision"), ("CISCO-ENTITY-ASSET-MIB", "ceAssetCLEI"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceAssetGroupRev2 = ceAssetGroupRev2.setStatus('current')
mibBuilder.exportSymbols("CISCO-ENTITY-ASSET-MIB", ciscoEntityAssetMIBObjects=ciscoEntityAssetMIBObjects, ciscoEntityAssetMIBNotifications=ciscoEntityAssetMIBNotifications, ceAssetMfgAssyNumber=ceAssetMfgAssyNumber, ceAssetIsFRU=ceAssetIsFRU, ceAssetEntityGroup=ceAssetEntityGroup, ceAssetMfgAssyRevision=ceAssetMfgAssyRevision, ceAssetOrderablePartNumber=ceAssetOrderablePartNumber, ciscoEntityAssetMIBComplianceRev2=ciscoEntityAssetMIBComplianceRev2, ciscoEntityAssetMIB=ciscoEntityAssetMIB, ceAssetEntry=ceAssetEntry, ceAssetGroup=ceAssetGroup, ceAssetSoftwareRevision=ceAssetSoftwareRevision, ceAssetTag=ceAssetTag, ceAssetSoftwareID=ceAssetSoftwareID, ciscoEntityAssetMIBNotificationsPrefix=ciscoEntityAssetMIBNotificationsPrefix, ceAssetGroupRev2=ceAssetGroupRev2, ceAssetFirmwareRevision=ceAssetFirmwareRevision, ciscoEntityAssetMIBCompliances=ciscoEntityAssetMIBCompliances, ceAssetFirmwareID=ceAssetFirmwareID, PYSNMP_MODULE_ID=ciscoEntityAssetMIB, ciscoEntityAssetMIBGroups=ciscoEntityAssetMIBGroups, ciscoEntityAssetMIBComplianceRev1=ciscoEntityAssetMIBComplianceRev1, ceAssetSerialNumber=ceAssetSerialNumber, ceAssetHardwareRevision=ceAssetHardwareRevision, ceAssetGroupRev1=ceAssetGroupRev1, ciscoEntityAssetMIBCompliance=ciscoEntityAssetMIBCompliance, ceAssetAlias=ceAssetAlias, ceAssetTable=ceAssetTable, ciscoEntityAssetMIBConformance=ciscoEntityAssetMIBConformance, ceAssetCLEI=ceAssetCLEI, ceAssetOEMString=ceAssetOEMString)
