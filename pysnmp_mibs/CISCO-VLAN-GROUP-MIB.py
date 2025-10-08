#
# PySNMP MIB module CISCO-VLAN-GROUP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-VLAN-GROUP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:24:54 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
Cisco2KVlanList, = mibBuilder.importSymbols("CISCO-TC", "Cisco2KVlanList")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
StorageType, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "StorageType", "RowStatus", "TextualConvention", "DisplayString")
ciscoVlanGroupMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 709))
ciscoVlanGroupMIB.setRevisions(('2011-03-22 00:00', '2009-11-20 00:00',))
if mibBuilder.loadTexts: ciscoVlanGroupMIB.setLastUpdated('201103220000Z')
if mibBuilder.loadTexts: ciscoVlanGroupMIB.setOrganization('Cisco Systems, Inc.')
ciscoVlanGroupMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 709, 0))
ciscoVlanGroupMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 709, 1))
ciscoVlanGroupMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 709, 2))
cvgConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 709, 1, 1), )
if mibBuilder.loadTexts: cvgConfigTable.setStatus('current')
cvgConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 709, 1, 1, 1), ).setIndexNames((0, "CISCO-VLAN-GROUP-MIB", "cvgConfigGroupName"))
if mibBuilder.loadTexts: cvgConfigEntry.setStatus('current')
cvgConfigGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 709, 1, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: cvgConfigGroupName.setStatus('current')
cvgConfigVlansFirst2K = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 709, 1, 1, 1, 2), Cisco2KVlanList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvgConfigVlansFirst2K.setStatus('current')
cvgConfigVlansSecond2K = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 709, 1, 1, 1, 3), Cisco2KVlanList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvgConfigVlansSecond2K.setStatus('current')
cvgConfigStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 709, 1, 1, 1, 4), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvgConfigStorageType.setStatus('current')
cvgConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 709, 1, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvgConfigRowStatus.setStatus('current')
cvgConfigTableSize = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 709, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvgConfigTableSize.setStatus('current')
ciscoVlanGroupMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 709, 2, 1))
ciscoVlanGroupMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 709, 2, 2))
ciscoVlanGroupMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 709, 2, 1, 1)).setObjects(("CISCO-VLAN-GROUP-MIB", "ciscoVlanGroupConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanGroupMIBCompliance = ciscoVlanGroupMIBCompliance.setStatus('deprecated')
ciscoVlanGroupMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 709, 2, 1, 2)).setObjects(("CISCO-VLAN-GROUP-MIB", "ciscoVlanGroupConfigGroup"), ("CISCO-VLAN-GROUP-MIB", "cvgConfigTableSizeGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanGroupMIBCompliance2 = ciscoVlanGroupMIBCompliance2.setStatus('current')
ciscoVlanGroupConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 709, 2, 2, 1)).setObjects(("CISCO-VLAN-GROUP-MIB", "cvgConfigVlansFirst2K"), ("CISCO-VLAN-GROUP-MIB", "cvgConfigVlansSecond2K"), ("CISCO-VLAN-GROUP-MIB", "cvgConfigRowStatus"), ("CISCO-VLAN-GROUP-MIB", "cvgConfigStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanGroupConfigGroup = ciscoVlanGroupConfigGroup.setStatus('current')
cvgConfigTableSizeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 709, 2, 2, 2)).setObjects(("CISCO-VLAN-GROUP-MIB", "cvgConfigTableSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvgConfigTableSizeGroup = cvgConfigTableSizeGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VLAN-GROUP-MIB", ciscoVlanGroupMIBNotifs=ciscoVlanGroupMIBNotifs, ciscoVlanGroupMIBCompliance=ciscoVlanGroupMIBCompliance, ciscoVlanGroupMIBGroups=ciscoVlanGroupMIBGroups, cvgConfigRowStatus=cvgConfigRowStatus, cvgConfigStorageType=cvgConfigStorageType, cvgConfigTable=cvgConfigTable, cvgConfigEntry=cvgConfigEntry, cvgConfigTableSize=cvgConfigTableSize, ciscoVlanGroupMIBCompliance2=ciscoVlanGroupMIBCompliance2, cvgConfigGroupName=cvgConfigGroupName, PYSNMP_MODULE_ID=ciscoVlanGroupMIB, ciscoVlanGroupConfigGroup=ciscoVlanGroupConfigGroup, ciscoVlanGroupMIBCompliances=ciscoVlanGroupMIBCompliances, cvgConfigVlansFirst2K=cvgConfigVlansFirst2K, ciscoVlanGroupMIBObjects=ciscoVlanGroupMIBObjects, ciscoVlanGroupMIB=ciscoVlanGroupMIB, cvgConfigTableSizeGroup=cvgConfigTableSizeGroup, cvgConfigVlansSecond2K=cvgConfigVlansSecond2K, ciscoVlanGroupMIBConform=ciscoVlanGroupMIBConform)
