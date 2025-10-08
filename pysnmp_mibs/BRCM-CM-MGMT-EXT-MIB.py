#
# PySNMP MIB module BRCM-CM-MGMT-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/broadcom/BRCM-CM-MGMT-EXT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:08:16 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
broadcomCableDataMgmt, = mibBuilder.importSymbols("BRCM-CABLEDATA-MGMT-MIB", "broadcomCableDataMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("BRCM-CM-MGMT-EXT-MIB", PYSNMP_MODULE_ID=cmMgmtExt, cmMgmtExtScan=cmMgmtExtScan, cmScanEntry=cmScanEntry, cmMgmtExtBaseStandbySwitchStatus=cmMgmtExtBaseStandbySwitchStatus, cmScanIndex=cmScanIndex, cmScanPushFrequency=cmScanPushFrequency, cmMgmtExt=cmMgmtExt, cmMgmtExtBase=cmMgmtExtBase, cmScanFrequency=cmScanFrequency, cmScanTable=cmScanTable)
