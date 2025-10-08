#
# PySNMP MIB module FS-EEE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/fscom/FS-EEE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:58:45 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
fsMgmt, = mibBuilder.importSymbols("FS-SMI", "fsMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fsEEEMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 119))
fsEEEMIB.setRevisions(('2012-10-16 00:00', '2012-10-16 00:00',))
if mibBuilder.loadTexts: fsEEEMIB.setLastUpdated('201210160000Z')
if mibBuilder.loadTexts: fsEEEMIB.setOrganization('FS.COM Inc..')
fsEEEConfigMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 119, 1))
fsEEETable = MibTable((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 119, 1, 1), )
if mibBuilder.loadTexts: fsEEETable.setStatus('current')
fsEEEEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 119, 1, 1, 1), ).setIndexNames((0, "FS-EEE-MIB", "fsEEEifIndex"))
if mibBuilder.loadTexts: fsEEEEntry.setStatus('current')
fsEEEifIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 119, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsEEEifIndex.setStatus('current')
fsEEEAdminEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 119, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsEEEAdminEnable.setStatus('current')
fsEEEOperEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 119, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsEEEOperEnable.setStatus('current')
mibBuilder.exportSymbols("FS-EEE-MIB", fsEEEConfigMIBObjects=fsEEEConfigMIBObjects, fsEEEAdminEnable=fsEEEAdminEnable, fsEEEEntry=fsEEEEntry, fsEEEOperEnable=fsEEEOperEnable, PYSNMP_MODULE_ID=fsEEEMIB, fsEEEifIndex=fsEEEifIndex, fsEEETable=fsEEETable, fsEEEMIB=fsEEEMIB)
