#
# PySNMP MIB module QTECH-EEE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/qtech/QTECH-EEE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:06:13 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
qtechMgmt, = mibBuilder.importSymbols("QTECH-SMI", "qtechMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
qtechEEEMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 119))
qtechEEEMIB.setRevisions(('2012-10-16 00:00', '2012-10-16 00:00',))
if mibBuilder.loadTexts: qtechEEEMIB.setLastUpdated('201210160000Z')
if mibBuilder.loadTexts: qtechEEEMIB.setOrganization('Qtech Networks Co.,Ltd.')
qtechEEEConfigMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 119, 1))
qtechEEETable = MibTable((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 119, 1, 1), )
if mibBuilder.loadTexts: qtechEEETable.setStatus('current')
qtechEEEEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 119, 1, 1, 1), ).setIndexNames((0, "QTECH-EEE-MIB", "qtechEEEifIndex"))
if mibBuilder.loadTexts: qtechEEEEntry.setStatus('current')
qtechEEEifIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 119, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechEEEifIndex.setStatus('current')
qtechEEEAdminEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 119, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qtechEEEAdminEnable.setStatus('current')
qtechEEEOperEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 119, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechEEEOperEnable.setStatus('current')
mibBuilder.exportSymbols("QTECH-EEE-MIB", PYSNMP_MODULE_ID=qtechEEEMIB, qtechEEEOperEnable=qtechEEEOperEnable, qtechEEEMIB=qtechEEEMIB, qtechEEETable=qtechEEETable, qtechEEEConfigMIBObjects=qtechEEEConfigMIBObjects, qtechEEEifIndex=qtechEEEifIndex, qtechEEEAdminEnable=qtechEEEAdminEnable, qtechEEEEntry=qtechEEEEntry)
