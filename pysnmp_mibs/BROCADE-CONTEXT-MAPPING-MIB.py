#
# PySNMP MIB module BROCADE-CONTEXT-MAPPING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/brocade/BROCADE-CONTEXT-MAPPING-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:15:32 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
bcsiModules, = mibBuilder.importSymbols("Brocade-REG-MIB", "bcsiModules")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
StorageType, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "StorageType", "RowStatus", "TextualConvention", "DisplayString")
brocadeContextMappingMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1588, 3, 1, 7))
brocadeContextMappingMIB.setRevisions(('2015-06-18 00:00',))
if mibBuilder.loadTexts: brocadeContextMappingMIB.setLastUpdated('201506180000Z')
if mibBuilder.loadTexts: brocadeContextMappingMIB.setOrganization(' Brocade Communications Systems, Inc.')
bContextMapMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 1, 7, 0))
bContextMapMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 1, 7, 1))
bContextMapMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 1, 7, 2))
bcmContexMapConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 1, 7, 1, 1))
bcmContextMappingTable = MibTable((1, 3, 6, 1, 4, 1, 1588, 3, 1, 7, 1, 1, 1), )
if mibBuilder.loadTexts: bcmContextMappingTable.setStatus('current')
bcmContextMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1588, 3, 1, 7, 1, 1, 1, 1), ).setIndexNames((0, "BROCADE-CONTEXT-MAPPING-MIB", "bcmContextMappingVacmContextName"))
if mibBuilder.loadTexts: bcmContextMappingEntry.setStatus('current')
bcmContextMappingVacmContextName = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 3, 1, 7, 1, 1, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)))
if mibBuilder.loadTexts: bcmContextMappingVacmContextName.setStatus('current')
bcmContextMappingVrfName = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 3, 1, 7, 1, 1, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcmContextMappingVrfName.setStatus('current')
bcmContextMappingStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 3, 1, 7, 1, 1, 1, 1, 3), StorageType().clone('nonVolatile')).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcmContextMappingStorageType.setStatus('current')
bcmContextMappingRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 3, 1, 7, 1, 1, 1, 1, 4), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcmContextMappingRowStatus.setStatus('current')
brocadeContextMapMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 1, 7, 2, 1))
brocadeContextMapMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 1, 7, 2, 2))
brocadeContextMapMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1588, 3, 1, 7, 2, 1, 1)).setObjects(("BROCADE-CONTEXT-MAPPING-MIB", "brocadeContextMapConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    brocadeContextMapMIBCompliance = brocadeContextMapMIBCompliance.setStatus('current')
brocadeContextMapConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1588, 3, 1, 7, 2, 2, 1)).setObjects(("BROCADE-CONTEXT-MAPPING-MIB", "bcmContextMappingVrfName"), ("BROCADE-CONTEXT-MAPPING-MIB", "bcmContextMappingStorageType"), ("BROCADE-CONTEXT-MAPPING-MIB", "bcmContextMappingRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    brocadeContextMapConfigGroup = brocadeContextMapConfigGroup.setStatus('current')
mibBuilder.exportSymbols("BROCADE-CONTEXT-MAPPING-MIB", PYSNMP_MODULE_ID=brocadeContextMappingMIB, brocadeContextMapMIBCompliance=brocadeContextMapMIBCompliance, bcmContextMappingVacmContextName=bcmContextMappingVacmContextName, bContextMapMIBConform=bContextMapMIBConform, bcmContextMappingStorageType=bcmContextMappingStorageType, bContextMapMIBNotifs=bContextMapMIBNotifs, bcmContextMappingVrfName=bcmContextMappingVrfName, brocadeContextMapMIBGroups=brocadeContextMapMIBGroups, bcmContextMappingEntry=bcmContextMappingEntry, bcmContextMappingTable=bcmContextMappingTable, brocadeContextMapMIBCompliances=brocadeContextMapMIBCompliances, brocadeContextMapConfigGroup=brocadeContextMapConfigGroup, brocadeContextMappingMIB=brocadeContextMappingMIB, bcmContextMappingRowStatus=bcmContextMappingRowStatus, bcmContexMapConfig=bcmContexMapConfig, bContextMapMIBObjects=bContextMapMIBObjects)
