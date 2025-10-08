#
# PySNMP MIB module CISCO-FC-DEVICE-ALIAS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-FC-DEVICE-ALIAS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:14:30 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
CdpvmDevType, = mibBuilder.importSymbols("CISCO-DYNAMIC-PORT-VSAN-MIB", "CdpvmDevType")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoFcDeviceAliasMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 430))
ciscoFcDeviceAliasMIB.setRevisions(('2004-09-20 00:00',))
if mibBuilder.loadTexts: ciscoFcDeviceAliasMIB.setLastUpdated('200409200000Z')
if mibBuilder.loadTexts: ciscoFcDeviceAliasMIB.setOrganization('Cisco Systems Inc.')
cfdaMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 430, 0))
cfdaMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 430, 1))
cfdaMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 430, 2))
cfdaConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 430, 1, 1))
cfdaConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 430, 1, 1, 1), )
if mibBuilder.loadTexts: cfdaConfigTable.setStatus('current')
cfdaConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 430, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-FC-DEVICE-ALIAS-MIB", "cfdaConfigDeviceAlias"))
if mibBuilder.loadTexts: cfdaConfigEntry.setStatus('current')
cfdaConfigDeviceAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 430, 1, 1, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 64)))
if mibBuilder.loadTexts: cfdaConfigDeviceAlias.setStatus('current')
cfdaConfigDeviceType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 430, 1, 1, 1, 1, 2), CdpvmDevType().clone('pwwn')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfdaConfigDeviceType.setStatus('current')
cfdaConfigDeviceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 430, 1, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfdaConfigDeviceId.setStatus('current')
cfdaConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 430, 1, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfdaConfigRowStatus.setStatus('current')
ciscoFcDaMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 430, 2, 1))
ciscoFcDaMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 430, 2, 2))
ciscoFcDaMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 430, 2, 1, 1)).setObjects(("CISCO-FC-DEVICE-ALIAS-MIB", "ciscoFcDaConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFcDaMIBCompliance = ciscoFcDaMIBCompliance.setStatus('current')
ciscoFcDaConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 430, 2, 2, 1)).setObjects(("CISCO-FC-DEVICE-ALIAS-MIB", "cfdaConfigDeviceType"), ("CISCO-FC-DEVICE-ALIAS-MIB", "cfdaConfigDeviceId"), ("CISCO-FC-DEVICE-ALIAS-MIB", "cfdaConfigRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFcDaConfigGroup = ciscoFcDaConfigGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-FC-DEVICE-ALIAS-MIB", cfdaConfigTable=cfdaConfigTable, cfdaMIBConform=cfdaMIBConform, cfdaConfigRowStatus=cfdaConfigRowStatus, ciscoFcDaMIBCompliances=ciscoFcDaMIBCompliances, ciscoFcDeviceAliasMIB=ciscoFcDeviceAliasMIB, ciscoFcDaMIBGroups=ciscoFcDaMIBGroups, PYSNMP_MODULE_ID=ciscoFcDeviceAliasMIB, cfdaConfiguration=cfdaConfiguration, cfdaConfigEntry=cfdaConfigEntry, cfdaConfigDeviceType=cfdaConfigDeviceType, cfdaConfigDeviceAlias=cfdaConfigDeviceAlias, cfdaConfigDeviceId=cfdaConfigDeviceId, cfdaMIBObjects=cfdaMIBObjects, ciscoFcDaConfigGroup=ciscoFcDaConfigGroup, cfdaMIBNotifs=cfdaMIBNotifs, ciscoFcDaMIBCompliance=ciscoFcDaMIBCompliance)
