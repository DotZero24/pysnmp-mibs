#
# PySNMP MIB module QTECH-EEE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/qtech/QTECH-EEE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:14:09 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
qtechMgmt, = mibBuilder.importSymbols("QTECH-SMI", "qtechMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("QTECH-EEE-MIB", PYSNMP_MODULE_ID=qtechEEEMIB, qtechEEEAdminEnable=qtechEEEAdminEnable, qtechEEEOperEnable=qtechEEEOperEnable, qtechEEETable=qtechEEETable, qtechEEEConfigMIBObjects=qtechEEEConfigMIBObjects, qtechEEEEntry=qtechEEEEntry, qtechEEEMIB=qtechEEEMIB, qtechEEEifIndex=qtechEEEifIndex)
