#
# PySNMP MIB module CISCO-FC-DEVICE-ALIAS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-FC-DEVICE-ALIAS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:28:40 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
CdpvmDevType, = mibBuilder.importSymbols("CISCO-DYNAMIC-PORT-VSAN-MIB", "CdpvmDevType")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("CISCO-FC-DEVICE-ALIAS-MIB", PYSNMP_MODULE_ID=ciscoFcDeviceAliasMIB, cfdaConfigTable=cfdaConfigTable, cfdaConfigDeviceAlias=cfdaConfigDeviceAlias, ciscoFcDaMIBGroups=ciscoFcDaMIBGroups, ciscoFcDaMIBCompliance=ciscoFcDaMIBCompliance, cfdaConfigDeviceId=cfdaConfigDeviceId, cfdaMIBNotifs=cfdaMIBNotifs, ciscoFcDaConfigGroup=ciscoFcDaConfigGroup, ciscoFcDaMIBCompliances=ciscoFcDaMIBCompliances, cfdaMIBConform=cfdaMIBConform, cfdaConfigRowStatus=cfdaConfigRowStatus, cfdaConfigDeviceType=cfdaConfigDeviceType, cfdaConfiguration=cfdaConfiguration, cfdaConfigEntry=cfdaConfigEntry, ciscoFcDeviceAliasMIB=ciscoFcDeviceAliasMIB, cfdaMIBObjects=cfdaMIBObjects)
