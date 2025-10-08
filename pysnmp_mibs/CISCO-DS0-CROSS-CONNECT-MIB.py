#
# PySNMP MIB module CISCO-DS0-CROSS-CONNECT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-DS0-CROSS-CONNECT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:12:04 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoDs0CrossConnectMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 9999))
ciscoDs0CrossConnectMIB.setRevisions(('2003-03-05 00:00',))
if mibBuilder.loadTexts: ciscoDs0CrossConnectMIB.setLastUpdated('200303050000Z')
if mibBuilder.loadTexts: ciscoDs0CrossConnectMIB.setOrganization('Cisco Systems, Inc.')
ciscoDs0CrossConnectMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 0))
ciscoDs0CrossConnectMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1))
ciscoDs0CrossConnectMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2))
cDs0CrossConnectConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1))
cds0CrossConnectConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1), )
if mibBuilder.loadTexts: cds0CrossConnectConfigTable.setStatus('current')
cds0CrossConnectConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-DS0-CROSS-CONNECT-MIB", "cds0Endpt1Ds1"), (0, "CISCO-DS0-CROSS-CONNECT-MIB", "cds0Endpt1Ds0Group"))
if mibBuilder.loadTexts: cds0CrossConnectConfigEntry.setStatus('current')
cds0Endpt1Ds1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: cds0Endpt1Ds1.setStatus('current')
cds0Endpt1Ds0Group = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 31)))
if mibBuilder.loadTexts: cds0Endpt1Ds0Group.setStatus('current')
cds0Endpt2Ds1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 3), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cds0Endpt2Ds1.setStatus('current')
cds0Endpt2Ds0Group = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cds0Endpt2Ds0Group.setStatus('current')
cds0ConnRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cds0ConnRowStatus.setStatus('current')
ciscoDs0CrossConnectMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 1))
ciscoDs0CrossConnectMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2))
ciscoDs0CrossConnectMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 1, 1)).setObjects(("CISCO-DS0-CROSS-CONNECT-MIB", "cDs0CrossConnectConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs0CrossConnectMIBCompliance = ciscoDs0CrossConnectMIBCompliance.setStatus('current')
cDs0CrossConnectConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 1)).setObjects(("CISCO-DS0-CROSS-CONNECT-MIB", "cds0Endpt2Ds1"), ("CISCO-DS0-CROSS-CONNECT-MIB", "cds0Endpt2Ds0Group"), ("CISCO-DS0-CROSS-CONNECT-MIB", "cds0ConnRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDs0CrossConnectConfigGroup = cDs0CrossConnectConfigGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-DS0-CROSS-CONNECT-MIB", cds0Endpt2Ds1=cds0Endpt2Ds1, cds0Endpt1Ds1=cds0Endpt1Ds1, cds0CrossConnectConfigEntry=cds0CrossConnectConfigEntry, cDs0CrossConnectConfig=cDs0CrossConnectConfig, cds0CrossConnectConfigTable=cds0CrossConnectConfigTable, cds0Endpt1Ds0Group=cds0Endpt1Ds0Group, ciscoDs0CrossConnectMIBCompliance=ciscoDs0CrossConnectMIBCompliance, ciscoDs0CrossConnectMIBNotifs=ciscoDs0CrossConnectMIBNotifs, ciscoDs0CrossConnectMIBGroups=ciscoDs0CrossConnectMIBGroups, ciscoDs0CrossConnectMIBObjects=ciscoDs0CrossConnectMIBObjects, cDs0CrossConnectConfigGroup=cDs0CrossConnectConfigGroup, cds0Endpt2Ds0Group=cds0Endpt2Ds0Group, ciscoDs0CrossConnectMIBConformance=ciscoDs0CrossConnectMIBConformance, ciscoDs0CrossConnectMIBCompliances=ciscoDs0CrossConnectMIBCompliances, cds0ConnRowStatus=cds0ConnRowStatus, ciscoDs0CrossConnectMIB=ciscoDs0CrossConnectMIB, PYSNMP_MODULE_ID=ciscoDs0CrossConnectMIB)
