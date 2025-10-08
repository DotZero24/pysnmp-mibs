#
# PySNMP MIB module CISCO-ENTITY-ASSET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-ENTITY-ASSET-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:15:20 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
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
mibBuilder.exportSymbols("CISCO-ENTITY-ASSET-MIB", ceAssetSoftwareID=ceAssetSoftwareID, ceAssetEntityGroup=ceAssetEntityGroup, ceAssetSoftwareRevision=ceAssetSoftwareRevision, ceAssetHardwareRevision=ceAssetHardwareRevision, ciscoEntityAssetMIBComplianceRev1=ciscoEntityAssetMIBComplianceRev1, ciscoEntityAssetMIBGroups=ciscoEntityAssetMIBGroups, ciscoEntityAssetMIB=ciscoEntityAssetMIB, ciscoEntityAssetMIBCompliances=ciscoEntityAssetMIBCompliances, PYSNMP_MODULE_ID=ciscoEntityAssetMIB, ciscoEntityAssetMIBComplianceRev2=ciscoEntityAssetMIBComplianceRev2, ciscoEntityAssetMIBObjects=ciscoEntityAssetMIBObjects, ciscoEntityAssetMIBConformance=ciscoEntityAssetMIBConformance, ceAssetIsFRU=ceAssetIsFRU, ceAssetGroupRev1=ceAssetGroupRev1, ceAssetSerialNumber=ceAssetSerialNumber, ceAssetMfgAssyNumber=ceAssetMfgAssyNumber, ceAssetCLEI=ceAssetCLEI, ceAssetTag=ceAssetTag, ceAssetTable=ceAssetTable, ciscoEntityAssetMIBNotifications=ciscoEntityAssetMIBNotifications, ceAssetFirmwareRevision=ceAssetFirmwareRevision, ciscoEntityAssetMIBNotificationsPrefix=ciscoEntityAssetMIBNotificationsPrefix, ceAssetGroupRev2=ceAssetGroupRev2, ceAssetOEMString=ceAssetOEMString, ceAssetAlias=ceAssetAlias, ceAssetFirmwareID=ceAssetFirmwareID, ceAssetEntry=ceAssetEntry, ceAssetGroup=ceAssetGroup, ceAssetOrderablePartNumber=ceAssetOrderablePartNumber, ceAssetMfgAssyRevision=ceAssetMfgAssyRevision, ciscoEntityAssetMIBCompliance=ciscoEntityAssetMIBCompliance)
