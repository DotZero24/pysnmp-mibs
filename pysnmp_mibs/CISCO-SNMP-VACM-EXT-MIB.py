#
# PySNMP MIB module CISCO-SNMP-VACM-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-SNMP-VACM-EXT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:11:42 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
vacmSecurityModel, vacmSecurityName = mibBuilder.importSymbols("SNMP-VIEW-BASED-ACM-MIB", "vacmSecurityModel", "vacmSecurityName")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention, RowStatus, StorageType = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus", "StorageType")
ciscoSnmpVacmExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 409))
ciscoSnmpVacmExtMIB.setRevisions(('2004-05-19 00:00',))
if mibBuilder.loadTexts: ciscoSnmpVacmExtMIB.setLastUpdated('200405190000Z')
if mibBuilder.loadTexts: ciscoSnmpVacmExtMIB.setOrganization('Cisco Systems, Inc.')
ciscoSnmpVacmExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 409, 1))
ciscoSnmpVacmExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 409, 2))
cvacmSecurityToGroupTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 409, 1, 1), )
if mibBuilder.loadTexts: cvacmSecurityToGroupTable.setStatus('current')
cvacmSecurityToGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 409, 1, 1, 1), ).setIndexNames((0, "SNMP-VIEW-BASED-ACM-MIB", "vacmSecurityModel"), (0, "SNMP-VIEW-BASED-ACM-MIB", "vacmSecurityName"), (0, "CISCO-SNMP-VACM-EXT-MIB", "cvacmSecurityGrpName"))
if mibBuilder.loadTexts: cvacmSecurityToGroupEntry.setStatus('current')
cvacmSecurityGrpName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 409, 1, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: cvacmSecurityGrpName.setStatus('current')
cvacmSecurityGrpStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 409, 1, 1, 1, 2), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvacmSecurityGrpStorageType.setStatus('current')
cvacmSecurityGrpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 409, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvacmSecurityGrpStatus.setStatus('current')
ciscoSnmpVacmExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 409, 2, 1))
ciscoSnmpVacmExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 409, 2, 2))
ciscoSnmpVacmExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 409, 2, 1, 1)).setObjects(("CISCO-SNMP-VACM-EXT-MIB", "ciscoSnmpVacmExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpVacmExtMIBCompliance = ciscoSnmpVacmExtMIBCompliance.setStatus('current')
ciscoSnmpVacmExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 409, 2, 2, 1)).setObjects(("CISCO-SNMP-VACM-EXT-MIB", "cvacmSecurityGrpStorageType"), ("CISCO-SNMP-VACM-EXT-MIB", "cvacmSecurityGrpStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpVacmExtGroup = ciscoSnmpVacmExtGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-SNMP-VACM-EXT-MIB", ciscoSnmpVacmExtMIBObjects=ciscoSnmpVacmExtMIBObjects, cvacmSecurityGrpStorageType=cvacmSecurityGrpStorageType, ciscoSnmpVacmExtMIBCompliances=ciscoSnmpVacmExtMIBCompliances, ciscoSnmpVacmExtMIBGroups=ciscoSnmpVacmExtMIBGroups, cvacmSecurityToGroupEntry=cvacmSecurityToGroupEntry, PYSNMP_MODULE_ID=ciscoSnmpVacmExtMIB, ciscoSnmpVacmExtMIB=ciscoSnmpVacmExtMIB, ciscoSnmpVacmExtMIBConformance=ciscoSnmpVacmExtMIBConformance, cvacmSecurityGrpName=cvacmSecurityGrpName, ciscoSnmpVacmExtGroup=ciscoSnmpVacmExtGroup, cvacmSecurityToGroupTable=cvacmSecurityToGroupTable, cvacmSecurityGrpStatus=cvacmSecurityGrpStatus, ciscoSnmpVacmExtMIBCompliance=ciscoSnmpVacmExtMIBCompliance)
