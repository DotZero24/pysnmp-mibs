#
# PySNMP MIB module CISCO-IF-LINK-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-IF-LINK-CONFIG-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:31:51 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
CiscoLocationSpecifier, = mibBuilder.importSymbols("CISCO-TC", "CiscoLocationSpecifier")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
ciscoIfLinkConfigMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 175))
ciscoIfLinkConfigMIB.setRevisions(('2001-10-05 00:00', '2000-09-14 00:00',))
if mibBuilder.loadTexts: ciscoIfLinkConfigMIB.setLastUpdated('200110050000Z')
if mibBuilder.loadTexts: ciscoIfLinkConfigMIB.setOrganization('Cisco Systems, Inc.')
cilConfigMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 175, 1))
cilConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 175, 1, 1))
cilConfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 175, 1, 1, 1), )
if mibBuilder.loadTexts: cilConfTable.setStatus('current')
cilConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 175, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-IF-LINK-CONFIG-MIB", "cilSourceInterface"))
if mibBuilder.loadTexts: cilConfEntry.setStatus('current')
cilSourceInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 175, 1, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: cilSourceInterface.setStatus('current')
cilTargetModuleInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 175, 1, 1, 1, 1, 2), CiscoLocationSpecifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cilTargetModuleInterface.setStatus('current')
cilRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 175, 1, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cilRowStatus.setStatus('current')
cilTargetModuleFramingType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 175, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notApplicable", 1), ("dsx1D4", 2), ("dsx1ESF", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cilTargetModuleFramingType.setStatus('current')
cilConfigMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 175, 3))
cilConfigMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 175, 3, 1))
cilConfigMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 175, 3, 2))
cilConfigMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 175, 3, 1, 1)).setObjects(("CISCO-IF-LINK-CONFIG-MIB", "cilConfMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cilConfigMIBCompliance = cilConfigMIBCompliance.setStatus('deprecated')
cilConfigMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 175, 3, 1, 2)).setObjects(("CISCO-IF-LINK-CONFIG-MIB", "cilConfMIBGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cilConfigMIBComplianceRev1 = cilConfigMIBComplianceRev1.setStatus('current')
cilConfMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 175, 3, 2, 1)).setObjects(("CISCO-IF-LINK-CONFIG-MIB", "cilTargetModuleInterface"), ("CISCO-IF-LINK-CONFIG-MIB", "cilRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cilConfMIBGroup = cilConfMIBGroup.setStatus('deprecated')
cilConfMIBGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 175, 3, 2, 2)).setObjects(("CISCO-IF-LINK-CONFIG-MIB", "cilTargetModuleInterface"), ("CISCO-IF-LINK-CONFIG-MIB", "cilRowStatus"), ("CISCO-IF-LINK-CONFIG-MIB", "cilTargetModuleFramingType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cilConfMIBGroupRev1 = cilConfMIBGroupRev1.setStatus('current')
mibBuilder.exportSymbols("CISCO-IF-LINK-CONFIG-MIB", cilTargetModuleFramingType=cilTargetModuleFramingType, cilConfigMIBObjects=cilConfigMIBObjects, cilRowStatus=cilRowStatus, PYSNMP_MODULE_ID=ciscoIfLinkConfigMIB, cilTargetModuleInterface=cilTargetModuleInterface, cilConfMIBGroupRev1=cilConfMIBGroupRev1, cilConfEntry=cilConfEntry, cilConfig=cilConfig, cilConfigMIBCompliances=cilConfigMIBCompliances, cilConfigMIBComplianceRev1=cilConfigMIBComplianceRev1, cilSourceInterface=cilSourceInterface, cilConfigMIBCompliance=cilConfigMIBCompliance, cilConfigMIBConformance=cilConfigMIBConformance, cilConfMIBGroup=cilConfMIBGroup, ciscoIfLinkConfigMIB=ciscoIfLinkConfigMIB, cilConfigMIBGroups=cilConfigMIBGroups, cilConfTable=cilConfTable)
