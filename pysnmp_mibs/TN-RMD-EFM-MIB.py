#
# PySNMP MIB module TN-RMD-EFM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/nokia/TN-RMD-EFM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:36:17 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
tnRmdIfIndex, = mibBuilder.importSymbols("TN-RMD-IF-MIB", "tnRmdIfIndex")
tnRmdSystemId, = mibBuilder.importSymbols("TN-RMD-SYSTEM-MIB", "tnRmdSystemId")
tnRmdObjs, tnRmdMIBModules = mibBuilder.importSymbols("TROPIC-GLOBAL-REG", "tnRmdObjs", "tnRmdMIBModules")
tnSysSwitchId, = mibBuilder.importSymbols("TROPIC-SYSTEM-MIB", "tnSysSwitchId")
tnRmdEfmMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 7483, 5, 1, 4, 2))
tnRmdEfmMibModule.setRevisions(('2018-02-23 12:00', '2016-11-16 00:00', '2012-11-28 00:00',))
if mibBuilder.loadTexts: tnRmdEfmMibModule.setLastUpdated('201802231200Z')
if mibBuilder.loadTexts: tnRmdEfmMibModule.setOrganization('Nokia')
tnRmdEfmObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 2))
class TnRmdSystemEfmDefect(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lop", 0))

tnRmdEfmAttributeTotal = MibScalar((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnRmdEfmAttributeTotal.setStatus('current')
tnRmdSystemEfmTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 2, 2), )
if mibBuilder.loadTexts: tnRmdSystemEfmTable.setStatus('current')
tnRmdSystemEfmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 2, 2, 1), ).setIndexNames((0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"), (0, "TN-RMD-SYSTEM-MIB", "tnRmdSystemId"), (0, "TN-RMD-IF-MIB", "tnRmdIfIndex"))
if mibBuilder.loadTexts: tnRmdSystemEfmEntry.setStatus('current')
tnRmdSystemEfmEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 2, 2, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnRmdSystemEfmEnabled.setStatus('current')
tnRmdSystemEfmDefect = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 2, 2, 1, 2), TnRmdSystemEfmDefect()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnRmdSystemEfmDefect.setStatus('current')
tnRmdEfmCountersTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 2, 3), )
if mibBuilder.loadTexts: tnRmdEfmCountersTable.setStatus('current')
tnRmdEfmCountersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 2, 3, 1), ).setIndexNames((0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"), (0, "TN-RMD-SYSTEM-MIB", "tnRmdSystemId"), (0, "TN-RMD-IF-MIB", "tnRmdIfIndex"))
if mibBuilder.loadTexts: tnRmdEfmCountersEntry.setStatus('current')
tnRmdEfmCountersRxNrNearEndErroredSymbols = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 2, 3, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnRmdEfmCountersRxNrNearEndErroredSymbols.setStatus('current')
tnRmdEfmCountersReset = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 2, 3, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnRmdEfmCountersReset.setStatus('current')
mibBuilder.exportSymbols("TN-RMD-EFM-MIB", tnRmdSystemEfmTable=tnRmdSystemEfmTable, tnRmdSystemEfmDefect=tnRmdSystemEfmDefect, PYSNMP_MODULE_ID=tnRmdEfmMibModule, tnRmdEfmCountersTable=tnRmdEfmCountersTable, tnRmdEfmAttributeTotal=tnRmdEfmAttributeTotal, tnRmdEfmCountersEntry=tnRmdEfmCountersEntry, tnRmdEfmCountersRxNrNearEndErroredSymbols=tnRmdEfmCountersRxNrNearEndErroredSymbols, tnRmdEfmCountersReset=tnRmdEfmCountersReset, TnRmdSystemEfmDefect=TnRmdSystemEfmDefect, tnRmdSystemEfmEnabled=tnRmdSystemEfmEnabled, tnRmdEfmMibModule=tnRmdEfmMibModule, tnRmdEfmObjects=tnRmdEfmObjects, tnRmdSystemEfmEntry=tnRmdSystemEfmEntry)
