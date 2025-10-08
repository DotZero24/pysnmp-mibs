#
# PySNMP MIB module TN-CONN-PROF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/nokia/TN-CONN-PROF-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:39:22 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, DisplayString, TimeStamp, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TimeStamp", "TextualConvention")
TmnxEncapVal, TItemDescription = mibBuilder.importSymbols("TN-TC-MIB", "TmnxEncapVal", "TItemDescription")
tnSRObjs, tnSRMIBModules = mibBuilder.importSymbols("TROPIC-GLOBAL-REG", "tnSRObjs", "tnSRMIBModules")
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
mibBuilder.exportSymbols("TN-CONN-PROF-MIB", tnConnProfId=tnConnProfId, TnConnProfVlanRanges=TnConnProfVlanRanges, TnConnProfId=TnConnProfId, PYSNMP_MODULE_ID=tnConnProfMIBModule, tnConnProfDescription=tnConnProfDescription, tnConnProfObjs=tnConnProfObjs, tnConnProfRowStatus=tnConnProfRowStatus, tnConnProfTable=tnConnProfTable, tnConnProfMIBModule=tnConnProfMIBModule, tnConnProfVlanRange=tnConnProfVlanRange, tnConnProfConfigObjs=tnConnProfConfigObjs, tnConnProfLastChanged=tnConnProfLastChanged, tnConnProfEntry=tnConnProfEntry)
