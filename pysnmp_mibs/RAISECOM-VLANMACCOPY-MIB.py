#
# PySNMP MIB module RAISECOM-VLANMACCOPY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/raisecom/RAISECOM-VLANMACCOPY-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:30:40 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
iscomSwitch, = mibBuilder.importSymbols("RAISECOM-BASE-MIB", "iscomSwitch")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
rcPortIndex, = mibBuilder.importSymbols("SWITCH-SYSTEM-MIB", "rcPortIndex")
Vlanset, = mibBuilder.importSymbols("SWITCH-TC", "Vlanset")
rcMacConfig = ModuleIdentity((1, 3, 6, 1, 4, 1, 8886, 6, 1, 3))
if mibBuilder.loadTexts: rcMacConfig.setLastUpdated('200809230000Z')
if mibBuilder.loadTexts: rcMacConfig.setOrganization('Raisecom, Inc.')
rcVlanMacCopyMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8886, 6, 1, 3, 5))
rcVlanMacCopyTable = MibTable((1, 3, 6, 1, 4, 1, 8886, 6, 1, 3, 5, 1), )
if mibBuilder.loadTexts: rcVlanMacCopyTable.setStatus('current')
rcVlanMacCopyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8886, 6, 1, 3, 5, 1, 1), ).setIndexNames((0, "SWITCH-SYSTEM-MIB", "rcPortIndex"), (0, "RAISECOM-VLANMACCOPY-MIB", "rcMacCopyTableIndex"))
if mibBuilder.loadTexts: rcVlanMacCopyEntry.setStatus('current')
rcMacCopyTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 3, 5, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: rcMacCopyTableIndex.setStatus('current')
rcMacCopyDestVlanList = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 3, 5, 1, 1, 2), Vlanset()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rcMacCopyDestVlanList.setStatus('current')
rcMacCopySourceVlanList = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 3, 5, 1, 1, 3), Vlanset()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rcMacCopySourceVlanList.setStatus('current')
rcMacCopyRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 3, 5, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rcMacCopyRowStatus.setStatus('current')
mibBuilder.exportSymbols("RAISECOM-VLANMACCOPY-MIB", rcVlanMacCopyTable=rcVlanMacCopyTable, rcVlanMacCopyMibObjects=rcVlanMacCopyMibObjects, rcMacConfig=rcMacConfig, rcVlanMacCopyEntry=rcVlanMacCopyEntry, rcMacCopyTableIndex=rcMacCopyTableIndex, PYSNMP_MODULE_ID=rcMacConfig, rcMacCopySourceVlanList=rcMacCopySourceVlanList, rcMacCopyDestVlanList=rcMacCopyDestVlanList, rcMacCopyRowStatus=rcMacCopyRowStatus)
