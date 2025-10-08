#
# PySNMP MIB module CISCO-TEMPERATURE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-TEMPERATURE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:11:49 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoTempMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 870))
ciscoTempMIB.setRevisions(('2020-05-28 00:00',))
if mibBuilder.loadTexts: ciscoTempMIB.setLastUpdated('202005280000Z')
if mibBuilder.loadTexts: ciscoTempMIB.setOrganization('Cisco Systems, Inc.')
ciscoTempMIBInformation = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 870, 1))
ciscoTempTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 870, 1, 1), )
if mibBuilder.loadTexts: ciscoTempTable.setStatus('current')
ciscoTempEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 870, 1, 1, 1), ).setIndexNames((0, "CISCO-TEMPERATURE-MIB", "ciscoTempIndex"))
if mibBuilder.loadTexts: ciscoTempEntry.setStatus('current')
ciscoTempIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 870, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: ciscoTempIndex.setStatus('current')
ciscoTempValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 870, 1, 1, 1, 2), Unsigned32()).setUnits('degrees Celsius').setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoTempValue.setStatus('current')
ciscoTempHyst = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 870, 1, 1, 1, 3), Unsigned32()).setUnits('degrees Celsius').setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoTempHyst.setStatus('current')
ciscoTempOs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 870, 1, 1, 1, 4), Unsigned32()).setUnits('degrees Celsius').setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoTempOs.setStatus('current')
ciscoTempMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 870, 2))
ciscoTempMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 870, 2, 1))
ciscoTempMIBConformGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 870, 2, 2))
ciscoTempMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 870, 2, 1, 1)).setObjects(("CISCO-TEMPERATURE-MIB", "ciscoTempMIBGlobalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTempMIBCompliance = ciscoTempMIBCompliance.setStatus('current')
ciscoTempMIBGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 870, 2, 2, 1)).setObjects(("CISCO-TEMPERATURE-MIB", "ciscoTempValue"), ("CISCO-TEMPERATURE-MIB", "ciscoTempHyst"), ("CISCO-TEMPERATURE-MIB", "ciscoTempOs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTempMIBGlobalGroup = ciscoTempMIBGlobalGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-TEMPERATURE-MIB", ciscoTempValue=ciscoTempValue, ciscoTempMIBInformation=ciscoTempMIBInformation, ciscoTempEntry=ciscoTempEntry, ciscoTempIndex=ciscoTempIndex, ciscoTempMIBCompliances=ciscoTempMIBCompliances, ciscoTempMIBCompliance=ciscoTempMIBCompliance, ciscoTempMIBConformGroups=ciscoTempMIBConformGroups, ciscoTempMIB=ciscoTempMIB, ciscoTempMIBGlobalGroup=ciscoTempMIBGlobalGroup, ciscoTempTable=ciscoTempTable, ciscoTempHyst=ciscoTempHyst, ciscoTempMIBConform=ciscoTempMIBConform, PYSNMP_MODULE_ID=ciscoTempMIB, ciscoTempOs=ciscoTempOs)
