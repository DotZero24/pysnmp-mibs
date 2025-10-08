#
# PySNMP MIB module CISCO-FC-SDV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-FC-SDV-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:31:56 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
FcNameIdOrZero, FcAddressId, DomainIdOrZero = mibBuilder.importSymbols("CISCO-ST-TC", "FcNameIdOrZero", "FcAddressId", "DomainIdOrZero")
vsanIndex, = mibBuilder.importSymbols("CISCO-VSAN-MIB", "vsanIndex")
FcList, = mibBuilder.importSymbols("CISCO-ZS-MIB", "FcList")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
StorageType, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "StorageType", "RowStatus", "DisplayString", "TextualConvention")
ciscoFcSdvMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 593))
ciscoFcSdvMIB.setRevisions(('2006-09-26 00:00',))
if mibBuilder.loadTexts: ciscoFcSdvMIB.setLastUpdated('200609260000Z')
if mibBuilder.loadTexts: ciscoFcSdvMIB.setOrganization('Cisco Systems, Inc.')
ciscoFcSdvMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 593, 0))
ciscoFcSdvMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 593, 1))
ciscoFcSdvMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 593, 2))
cFcSdvConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1))
class CiscoFcSdvDevIdType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("singleDevPWWN", 1), ("singleDevDevAlias", 2))

class CiscoFcSdvDevId(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class CiscoFcSdvRealDevMapType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("primaryDevMap", 1), ("secondaryDevMap", 2))

cFcSdvVirtDeviceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 1), )
if mibBuilder.loadTexts: cFcSdvVirtDeviceTable.setStatus('current')
cFcSdvVirtDeviceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-VSAN-MIB", "vsanIndex"), (0, "CISCO-FC-SDV-MIB", "cFcSdvVdIndex"))
if mibBuilder.loadTexts: cFcSdvVirtDeviceEntry.setStatus('current')
cFcSdvVdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4096)))
if mibBuilder.loadTexts: cFcSdvVdIndex.setStatus('current')
cFcSdvVdName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cFcSdvVdName.setStatus('current')
cFcSdvVdVirtDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 1, 1, 3), DomainIdOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cFcSdvVdVirtDomain.setStatus('current')
cFcSdvVdFcId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 1, 1, 4), FcAddressId().clone(hexValue="000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cFcSdvVdFcId.setStatus('current')
cFcSdvVdPwwn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 1, 1, 5), FcNameIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cFcSdvVdPwwn.setStatus('current')
cFcSdvVdNwwn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 1, 1, 6), FcNameIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cFcSdvVdNwwn.setStatus('current')
cFcSdvVdAssignedFcId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 1, 1, 7), FcAddressId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cFcSdvVdAssignedFcId.setStatus('current')
cFcSdvVdRealDevMapList = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 1, 1, 8), FcList().subtype(subtypeSpec=ValueSizeConstraint(0, 16)).clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: cFcSdvVdRealDevMapList.setStatus('current')
cFcSdvVdStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 1, 1, 9), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cFcSdvVdStorageType.setStatus('current')
cFcSdvVdRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 1, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cFcSdvVdRowStatus.setStatus('current')
cFcSdvVirtRealDevMapTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 2), )
if mibBuilder.loadTexts: cFcSdvVirtRealDevMapTable.setStatus('current')
cFcSdvVirtRealDevMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-VSAN-MIB", "vsanIndex"), (0, "CISCO-FC-SDV-MIB", "cFcSdvVdIndex"), (0, "CISCO-FC-SDV-MIB", "cFcSdvVirtRealDevMapIndex"))
if mibBuilder.loadTexts: cFcSdvVirtRealDevMapEntry.setStatus('current')
cFcSdvVirtRealDevMapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 128)))
if mibBuilder.loadTexts: cFcSdvVirtRealDevMapIndex.setStatus('current')
cFcSdvVirtRealDeviceIdType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 2, 1, 2), CiscoFcSdvDevIdType().clone('singleDevPWWN')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cFcSdvVirtRealDeviceIdType.setStatus('current')
cFcSdvVirtRealDeviceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 2, 1, 3), CiscoFcSdvDevId().subtype(subtypeSpec=ValueSizeConstraint(1, 64)).clone(hexValue="0000000000000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cFcSdvVirtRealDeviceId.setStatus('current')
cFcSdvVirtRealDevMapType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 2, 1, 4), CiscoFcSdvRealDevMapType().clone('secondaryDevMap')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cFcSdvVirtRealDevMapType.setStatus('current')
cFcSdvVirtRealDevMapStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 2, 1, 5), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cFcSdvVirtRealDevMapStorageType.setStatus('current')
cFcSdvVirtRealDevMapRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 593, 1, 1, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cFcSdvVirtRealDevMapRowStatus.setStatus('current')
ciscoFcSdvMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 593, 2, 1))
ciscoFcSdvMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 593, 2, 2))
ciscoFcSdvMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 593, 2, 1, 1)).setObjects(("CISCO-FC-SDV-MIB", "ciscoFcSdvConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFcSdvMIBCompliance = ciscoFcSdvMIBCompliance.setStatus('current')
ciscoFcSdvConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 593, 2, 2, 1)).setObjects(("CISCO-FC-SDV-MIB", "cFcSdvVdName"), ("CISCO-FC-SDV-MIB", "cFcSdvVdVirtDomain"), ("CISCO-FC-SDV-MIB", "cFcSdvVdFcId"), ("CISCO-FC-SDV-MIB", "cFcSdvVdPwwn"), ("CISCO-FC-SDV-MIB", "cFcSdvVdNwwn"), ("CISCO-FC-SDV-MIB", "cFcSdvVdAssignedFcId"), ("CISCO-FC-SDV-MIB", "cFcSdvVdStorageType"), ("CISCO-FC-SDV-MIB", "cFcSdvVdRealDevMapList"), ("CISCO-FC-SDV-MIB", "cFcSdvVdRowStatus"), ("CISCO-FC-SDV-MIB", "cFcSdvVirtRealDeviceIdType"), ("CISCO-FC-SDV-MIB", "cFcSdvVirtRealDeviceId"), ("CISCO-FC-SDV-MIB", "cFcSdvVirtRealDevMapType"), ("CISCO-FC-SDV-MIB", "cFcSdvVirtRealDevMapStorageType"), ("CISCO-FC-SDV-MIB", "cFcSdvVirtRealDevMapRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFcSdvConfigGroup = ciscoFcSdvConfigGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-FC-SDV-MIB", ciscoFcSdvMIBCompliances=ciscoFcSdvMIBCompliances, cFcSdvVirtRealDeviceId=cFcSdvVirtRealDeviceId, ciscoFcSdvConfigGroup=ciscoFcSdvConfigGroup, CiscoFcSdvDevIdType=CiscoFcSdvDevIdType, cFcSdvVdFcId=cFcSdvVdFcId, ciscoFcSdvMIBObjects=ciscoFcSdvMIBObjects, CiscoFcSdvRealDevMapType=CiscoFcSdvRealDevMapType, ciscoFcSdvMIB=ciscoFcSdvMIB, cFcSdvVirtDeviceEntry=cFcSdvVirtDeviceEntry, cFcSdvVirtRealDeviceIdType=cFcSdvVirtRealDeviceIdType, cFcSdvConfig=cFcSdvConfig, cFcSdvVirtDeviceTable=cFcSdvVirtDeviceTable, PYSNMP_MODULE_ID=ciscoFcSdvMIB, cFcSdvVirtRealDevMapTable=cFcSdvVirtRealDevMapTable, cFcSdvVirtRealDevMapRowStatus=cFcSdvVirtRealDevMapRowStatus, cFcSdvVdAssignedFcId=cFcSdvVdAssignedFcId, cFcSdvVdRealDevMapList=cFcSdvVdRealDevMapList, cFcSdvVdName=cFcSdvVdName, cFcSdvVirtRealDevMapStorageType=cFcSdvVirtRealDevMapStorageType, ciscoFcSdvMIBGroups=ciscoFcSdvMIBGroups, cFcSdvVirtRealDevMapEntry=cFcSdvVirtRealDevMapEntry, ciscoFcSdvMIBCompliance=ciscoFcSdvMIBCompliance, cFcSdvVdIndex=cFcSdvVdIndex, cFcSdvVdNwwn=cFcSdvVdNwwn, ciscoFcSdvMIBConform=ciscoFcSdvMIBConform, ciscoFcSdvMIBNotifs=ciscoFcSdvMIBNotifs, cFcSdvVirtRealDevMapIndex=cFcSdvVirtRealDevMapIndex, cFcSdvVdStorageType=cFcSdvVdStorageType, cFcSdvVirtRealDevMapType=cFcSdvVirtRealDevMapType, cFcSdvVdVirtDomain=cFcSdvVdVirtDomain, cFcSdvVdRowStatus=cFcSdvVdRowStatus, cFcSdvVdPwwn=cFcSdvVdPwwn, CiscoFcSdvDevId=CiscoFcSdvDevId)
