#
# PySNMP MIB module CISCO-DS0-CROSS-CONNECT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-DS0-CROSS-CONNECT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:24:22 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("CISCO-DS0-CROSS-CONNECT-MIB", cds0Endpt2Ds1=cds0Endpt2Ds1, ciscoDs0CrossConnectMIBConformance=ciscoDs0CrossConnectMIBConformance, ciscoDs0CrossConnectMIB=ciscoDs0CrossConnectMIB, ciscoDs0CrossConnectMIBGroups=ciscoDs0CrossConnectMIBGroups, ciscoDs0CrossConnectMIBCompliance=ciscoDs0CrossConnectMIBCompliance, PYSNMP_MODULE_ID=ciscoDs0CrossConnectMIB, cDs0CrossConnectConfigGroup=cDs0CrossConnectConfigGroup, cds0Endpt1Ds1=cds0Endpt1Ds1, cDs0CrossConnectConfig=cDs0CrossConnectConfig, cds0CrossConnectConfigEntry=cds0CrossConnectConfigEntry, cds0CrossConnectConfigTable=cds0CrossConnectConfigTable, cds0Endpt1Ds0Group=cds0Endpt1Ds0Group, ciscoDs0CrossConnectMIBCompliances=ciscoDs0CrossConnectMIBCompliances, cds0Endpt2Ds0Group=cds0Endpt2Ds0Group, ciscoDs0CrossConnectMIBNotifs=ciscoDs0CrossConnectMIBNotifs, ciscoDs0CrossConnectMIBObjects=ciscoDs0CrossConnectMIBObjects, cds0ConnRowStatus=cds0ConnRowStatus)
