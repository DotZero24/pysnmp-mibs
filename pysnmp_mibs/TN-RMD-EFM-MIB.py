#
# PySNMP MIB module TN-RMD-EFM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/nokia/TN-RMD-EFM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:18:51 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Integer32, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Counter64, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Counter64", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
tnRmdIfIndex, = mibBuilder.importSymbols("TN-RMD-IF-MIB", "tnRmdIfIndex")
tnRmdSystemId, = mibBuilder.importSymbols("TN-RMD-SYSTEM-MIB", "tnRmdSystemId")
tnRmdMIBModules, tnRmdObjs = mibBuilder.importSymbols("TROPIC-GLOBAL-REG", "tnRmdMIBModules", "tnRmdObjs")
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
mibBuilder.exportSymbols("TN-RMD-EFM-MIB", tnRmdEfmCountersReset=tnRmdEfmCountersReset, tnRmdEfmObjects=tnRmdEfmObjects, tnRmdSystemEfmTable=tnRmdSystemEfmTable, TnRmdSystemEfmDefect=TnRmdSystemEfmDefect, tnRmdEfmAttributeTotal=tnRmdEfmAttributeTotal, tnRmdSystemEfmEnabled=tnRmdSystemEfmEnabled, tnRmdEfmCountersEntry=tnRmdEfmCountersEntry, tnRmdSystemEfmDefect=tnRmdSystemEfmDefect, PYSNMP_MODULE_ID=tnRmdEfmMibModule, tnRmdEfmCountersTable=tnRmdEfmCountersTable, tnRmdEfmMibModule=tnRmdEfmMibModule, tnRmdSystemEfmEntry=tnRmdSystemEfmEntry, tnRmdEfmCountersRxNrNearEndErroredSymbols=tnRmdEfmCountersRxNrNearEndErroredSymbols)
