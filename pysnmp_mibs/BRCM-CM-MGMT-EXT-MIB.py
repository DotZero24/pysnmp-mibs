#
# PySNMP MIB module BRCM-CM-MGMT-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/broadcom/BRCM-CM-MGMT-EXT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:18:04 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
broadcomCableDataMgmt, = mibBuilder.importSymbols("BRCM-CABLEDATA-MGMT-MIB", "broadcomCableDataMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cmMgmtExt = ModuleIdentity((1, 3, 6, 1, 4, 1, 4413, 2, 2, 99, 4413, 2))
cmMgmtExt.setRevisions(('2007-02-05 00:00', '2005-04-18 00:00',))
if mibBuilder.loadTexts: cmMgmtExt.setLastUpdated('200702050000Z')
if mibBuilder.loadTexts: cmMgmtExt.setOrganization('Broadcom Corporation')
cmMgmtExtBase = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 2, 2, 99, 4413, 2, 1))
cmMgmtExtScan = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 2, 2, 99, 4413, 2, 2))
cmScanPushFrequency = MibScalar((1, 3, 6, 1, 4, 1, 4413, 2, 2, 99, 4413, 2, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmScanPushFrequency.setStatus('current')
cmScanTable = MibTable((1, 3, 6, 1, 4, 1, 4413, 2, 2, 99, 4413, 2, 2, 2), )
if mibBuilder.loadTexts: cmScanTable.setStatus('current')
cmScanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4413, 2, 2, 99, 4413, 2, 2, 2, 1), ).setIndexNames((0, "BRCM-CM-MGMT-EXT-MIB", "cmScanIndex"))
if mibBuilder.loadTexts: cmScanEntry.setStatus('current')
cmScanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 2, 2, 99, 4413, 2, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128)))
if mibBuilder.loadTexts: cmScanIndex.setStatus('current')
cmScanFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 2, 2, 99, 4413, 2, 2, 2, 1, 2), Integer32()).setUnits('hertz').setMaxAccess("readonly")
if mibBuilder.loadTexts: cmScanFrequency.setStatus('current')
cmMgmtExtBaseStandbySwitchStatus = MibScalar((1, 3, 6, 1, 4, 1, 4413, 2, 2, 99, 4413, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmMgmtExtBaseStandbySwitchStatus.setStatus('current')
mibBuilder.exportSymbols("BRCM-CM-MGMT-EXT-MIB", cmScanFrequency=cmScanFrequency, cmScanEntry=cmScanEntry, cmMgmtExtBaseStandbySwitchStatus=cmMgmtExtBaseStandbySwitchStatus, cmMgmtExtBase=cmMgmtExtBase, cmMgmtExtScan=cmMgmtExtScan, cmMgmtExt=cmMgmtExt, cmScanIndex=cmScanIndex, PYSNMP_MODULE_ID=cmMgmtExt, cmScanTable=cmScanTable, cmScanPushFrequency=cmScanPushFrequency)
