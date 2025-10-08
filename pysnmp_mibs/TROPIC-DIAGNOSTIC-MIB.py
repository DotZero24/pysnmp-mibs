#
# PySNMP MIB module TROPIC-DIAGNOSTIC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/nokia/TROPIC-DIAGNOSTIC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:40:13 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
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
mibBuilder.exportSymbols("TROPIC-DIAGNOSTIC-MIB", tnDiagnosticConf=tnDiagnosticConf, tnDiagnosticMibModule=tnDiagnosticMibModule, tnEquipDiagStatusGroup=tnEquipDiagStatusGroup, tnDiagnosticObjs=tnDiagnosticObjs, tnEquipDiagPort=tnEquipDiagPort, tnEquipDiagStatusEntry=tnEquipDiagStatusEntry, tnEquipDiagUnit=tnEquipDiagUnit, tnEquipDiagStatusDescr=tnEquipDiagStatusDescr, tnEquipDiagStatusResult=tnEquipDiagStatusResult, PYSNMP_MODULE_ID=tnDiagnosticMibModule, tnDiagnosticCompliances=tnDiagnosticCompliances, tnEquipDiagId=tnEquipDiagId, tnEquipmentDiagnosticStatusTable=tnEquipmentDiagnosticStatusTable, tnDiagnosticGroups=tnDiagnosticGroups, tnDiagnosticCompliance=tnDiagnosticCompliance, TnEquipDiagDescription=TnEquipDiagDescription)
