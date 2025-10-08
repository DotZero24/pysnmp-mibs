#
# PySNMP MIB module BROCADE-CONTEXT-MAPPING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/brocade/BROCADE-CONTEXT-MAPPING-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:00 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
bcsiModules, = mibBuilder.importSymbols("Brocade-REG-MIB", "bcsiModules")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention, RowStatus, StorageType = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus", "StorageType")
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
mibBuilder.exportSymbols("BROCADE-CONTEXT-MAPPING-MIB", PYSNMP_MODULE_ID=brocadeContextMappingMIB, bcmContextMappingTable=bcmContextMappingTable, bContextMapMIBObjects=bContextMapMIBObjects, brocadeContextMapMIBGroups=brocadeContextMapMIBGroups, bcmContextMappingEntry=bcmContextMappingEntry, bcmContextMappingVrfName=bcmContextMappingVrfName, bcmContextMappingRowStatus=bcmContextMappingRowStatus, bcmContextMappingStorageType=bcmContextMappingStorageType, brocadeContextMapConfigGroup=brocadeContextMapConfigGroup, bcmContextMappingVacmContextName=bcmContextMappingVacmContextName, brocadeContextMappingMIB=brocadeContextMappingMIB, brocadeContextMapMIBCompliance=brocadeContextMapMIBCompliance, brocadeContextMapMIBCompliances=brocadeContextMapMIBCompliances, bContextMapMIBConform=bContextMapMIBConform, bcmContexMapConfig=bcmContexMapConfig, bContextMapMIBNotifs=bContextMapMIBNotifs)
