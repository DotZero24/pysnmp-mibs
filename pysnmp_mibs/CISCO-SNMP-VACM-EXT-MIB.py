#
# PySNMP MIB module CISCO-SNMP-VACM-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-SNMP-VACM-EXT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:23:52 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
vacmSecurityModel, vacmSecurityName = mibBuilder.importSymbols("SNMP-VIEW-BASED-ACM-MIB", "vacmSecurityModel", "vacmSecurityName")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
StorageType, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "StorageType", "RowStatus", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("CISCO-SNMP-VACM-EXT-MIB", cvacmSecurityToGroupEntry=cvacmSecurityToGroupEntry, cvacmSecurityGrpStorageType=cvacmSecurityGrpStorageType, ciscoSnmpVacmExtMIBObjects=ciscoSnmpVacmExtMIBObjects, cvacmSecurityGrpName=cvacmSecurityGrpName, ciscoSnmpVacmExtMIBCompliances=ciscoSnmpVacmExtMIBCompliances, ciscoSnmpVacmExtMIBGroups=ciscoSnmpVacmExtMIBGroups, ciscoSnmpVacmExtMIB=ciscoSnmpVacmExtMIB, ciscoSnmpVacmExtMIBCompliance=ciscoSnmpVacmExtMIBCompliance, ciscoSnmpVacmExtMIBConformance=ciscoSnmpVacmExtMIBConformance, PYSNMP_MODULE_ID=ciscoSnmpVacmExtMIB, cvacmSecurityToGroupTable=cvacmSecurityToGroupTable, ciscoSnmpVacmExtGroup=ciscoSnmpVacmExtGroup, cvacmSecurityGrpStatus=cvacmSecurityGrpStatus)
