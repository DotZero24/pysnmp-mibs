#
# PySNMP MIB module RAISECOM-VLANMACCOPY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/raisecom/RAISECOM-VLANMACCOPY-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:54:25 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
iscomSwitch, = mibBuilder.importSymbols("RAISECOM-BASE-MIB", "iscomSwitch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("RAISECOM-VLANMACCOPY-MIB", rcVlanMacCopyEntry=rcVlanMacCopyEntry, rcMacConfig=rcMacConfig, PYSNMP_MODULE_ID=rcMacConfig, rcMacCopySourceVlanList=rcMacCopySourceVlanList, rcMacCopyTableIndex=rcMacCopyTableIndex, rcMacCopyRowStatus=rcMacCopyRowStatus, rcVlanMacCopyTable=rcVlanMacCopyTable, rcMacCopyDestVlanList=rcMacCopyDestVlanList, rcVlanMacCopyMibObjects=rcVlanMacCopyMibObjects)
