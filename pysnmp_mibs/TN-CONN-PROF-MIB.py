#
# PySNMP MIB module TN-CONN-PROF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/nokia/TN-CONN-PROF-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:20:54 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
TimeStamp, DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "RowStatus", "TextualConvention")
TItemDescription, TmnxEncapVal = mibBuilder.importSymbols("TN-TC-MIB", "TItemDescription", "TmnxEncapVal")
tnSRMIBModules, tnSRObjs = mibBuilder.importSymbols("TROPIC-GLOBAL-REG", "tnSRMIBModules", "tnSRObjs")
tnSysSwitchId, = mibBuilder.importSymbols("TROPIC-SYSTEM-MIB", "tnSysSwitchId")
tnConnProfMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 7483, 5, 1, 3, 75))
tnConnProfMIBModule.setRevisions(('2019-10-18 00:00', '2015-04-06 00:00', '2011-02-01 00:00',))
if mibBuilder.loadTexts: tnConnProfMIBModule.setLastUpdated('201910180000Z')
if mibBuilder.loadTexts: tnConnProfMIBModule.setOrganization('Nokia')
tnConnProfObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 75))
tnConnProfConfigObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 75, 2))
class TnConnProfId(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 1000), )
class TnConnProfVlanRanges(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 512)

tnConnProfTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 75, 2, 1), )
if mibBuilder.loadTexts: tnConnProfTable.setStatus('current')
tnConnProfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 75, 2, 1, 1), ).setIndexNames((0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"), (0, "TN-CONN-PROF-MIB", "tnConnProfId"))
if mibBuilder.loadTexts: tnConnProfEntry.setStatus('current')
tnConnProfId = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 75, 2, 1, 1, 1), TnConnProfId())
if mibBuilder.loadTexts: tnConnProfId.setStatus('current')
tnConnProfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 75, 2, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnConnProfRowStatus.setStatus('current')
tnConnProfLastChanged = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 75, 2, 1, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnConnProfLastChanged.setStatus('current')
tnConnProfDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 75, 2, 1, 1, 4), TItemDescription()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnConnProfDescription.setStatus('current')
tnConnProfVlanRange = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 75, 2, 1, 1, 5), TnConnProfVlanRanges()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnConnProfVlanRange.setStatus('current')
mibBuilder.exportSymbols("TN-CONN-PROF-MIB", tnConnProfTable=tnConnProfTable, tnConnProfLastChanged=tnConnProfLastChanged, tnConnProfDescription=tnConnProfDescription, TnConnProfId=TnConnProfId, tnConnProfRowStatus=tnConnProfRowStatus, tnConnProfVlanRange=tnConnProfVlanRange, tnConnProfConfigObjs=tnConnProfConfigObjs, tnConnProfId=tnConnProfId, PYSNMP_MODULE_ID=tnConnProfMIBModule, tnConnProfEntry=tnConnProfEntry, tnConnProfObjs=tnConnProfObjs, tnConnProfMIBModule=tnConnProfMIBModule, TnConnProfVlanRanges=TnConnProfVlanRanges)
