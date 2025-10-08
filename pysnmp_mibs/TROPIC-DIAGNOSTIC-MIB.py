#
# PySNMP MIB module TROPIC-DIAGNOSTIC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/nokia/TROPIC-DIAGNOSTIC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:21:29 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tnSystemModules, tnDiagnosticMIB = mibBuilder.importSymbols("TROPIC-GLOBAL-REG", "tnSystemModules", "tnDiagnosticMIB")
tnShelfIndex, = mibBuilder.importSymbols("TROPIC-SHELF-MIB", "tnShelfIndex")
tnSlotIndex, = mibBuilder.importSymbols("TROPIC-SLOT-MIB", "tnSlotIndex")
tnDiagnosticMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 1, 4))
tnDiagnosticMibModule.setRevisions(('2018-02-23 12:00', '2016-11-16 12:00', '2010-07-15 12:00',))
if mibBuilder.loadTexts: tnDiagnosticMibModule.setLastUpdated('201802231200Z')
if mibBuilder.loadTexts: tnDiagnosticMibModule.setOrganization('Nokia')
tnDiagnosticConf = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 1, 4, 1))
tnDiagnosticGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 1, 4, 1, 1))
tnDiagnosticCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 1, 4, 1, 2))
tnDiagnosticObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 1, 4, 2))
class TnEquipDiagDescription(SnmpAdminString):
    status = 'current'
    subtypeSpec = SnmpAdminString.subtypeSpec + ValueSizeConstraint(0, 60)

tnEquipmentDiagnosticStatusTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 1, 4, 2, 1), )
if mibBuilder.loadTexts: tnEquipmentDiagnosticStatusTable.setStatus('current')
tnEquipDiagStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 1, 4, 2, 1, 1), ).setIndexNames((0, "TROPIC-SHELF-MIB", "tnShelfIndex"), (0, "TROPIC-SLOT-MIB", "tnSlotIndex"), (0, "TROPIC-DIAGNOSTIC-MIB", "tnEquipDiagPort"), (0, "TROPIC-DIAGNOSTIC-MIB", "tnEquipDiagId"), (0, "TROPIC-DIAGNOSTIC-MIB", "tnEquipDiagUnit"))
if mibBuilder.loadTexts: tnEquipDiagStatusEntry.setStatus('current')
tnEquipDiagPort = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 1, 4, 2, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: tnEquipDiagPort.setStatus('current')
tnEquipDiagId = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 1, 4, 2, 1, 1, 2), Unsigned32())
if mibBuilder.loadTexts: tnEquipDiagId.setStatus('current')
tnEquipDiagUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 1, 4, 2, 1, 1, 3), Unsigned32())
if mibBuilder.loadTexts: tnEquipDiagUnit.setStatus('current')
tnEquipDiagStatusDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 1, 4, 2, 1, 1, 4), TnEquipDiagDescription()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnEquipDiagStatusDescr.setStatus('current')
tnEquipDiagStatusResult = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 1, 4, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("failed", 1), ("passed", 2), ("willNotRun", 3), ("notExecuted", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnEquipDiagStatusResult.setStatus('current')
tnEquipDiagStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 1, 4, 1, 1, 1)).setObjects(("TROPIC-DIAGNOSTIC-MIB", "tnEquipDiagStatusDescr"), ("TROPIC-DIAGNOSTIC-MIB", "tnEquipDiagStatusResult"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnEquipDiagStatusGroup = tnEquipDiagStatusGroup.setStatus('current')
tnDiagnosticCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7483, 2, 1, 4, 1, 2, 1)).setObjects(("TROPIC-DIAGNOSTIC-MIB", "tnEquipDiagStatusGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnDiagnosticCompliance = tnDiagnosticCompliance.setStatus('current')
mibBuilder.exportSymbols("TROPIC-DIAGNOSTIC-MIB", PYSNMP_MODULE_ID=tnDiagnosticMibModule, tnEquipDiagPort=tnEquipDiagPort, tnEquipDiagId=tnEquipDiagId, tnEquipDiagUnit=tnEquipDiagUnit, tnEquipDiagStatusResult=tnEquipDiagStatusResult, tnEquipmentDiagnosticStatusTable=tnEquipmentDiagnosticStatusTable, tnDiagnosticCompliances=tnDiagnosticCompliances, tnDiagnosticCompliance=tnDiagnosticCompliance, tnEquipDiagStatusEntry=tnEquipDiagStatusEntry, tnDiagnosticMibModule=tnDiagnosticMibModule, tnDiagnosticGroups=tnDiagnosticGroups, tnDiagnosticObjs=tnDiagnosticObjs, tnDiagnosticConf=tnDiagnosticConf, TnEquipDiagDescription=TnEquipDiagDescription, tnEquipDiagStatusDescr=tnEquipDiagStatusDescr, tnEquipDiagStatusGroup=tnEquipDiagStatusGroup)
