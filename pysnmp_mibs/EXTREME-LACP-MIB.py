#
# PySNMP MIB module EXTREME-LACP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/extreme/EXTREME-LACP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:02:04 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
extremeAgent, = mibBuilder.importSymbols("EXTREME-BASE-MIB", "extremeAgent")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "DisplayString", "TextualConvention")
extremeLacp = ModuleIdentity((1, 3, 6, 1, 4, 1, 1916, 1, 19))
if mibBuilder.loadTexts: extremeLacp.setLastUpdated('0502151530Z')
if mibBuilder.loadTexts: extremeLacp.setOrganization('Extreme Networks, Inc.')
class LacpGroupId(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 32)

class LacpMemberPort(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

extremeLacpTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 19, 1), )
if mibBuilder.loadTexts: extremeLacpTable.setStatus('current')
extremeLacpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 19, 1, 1), ).setIndexNames((0, "EXTREME-LACP-MIB", "extremeLacpGroup"), (0, "EXTREME-LACP-MIB", "extremeLacpMemberPort"))
if mibBuilder.loadTexts: extremeLacpEntry.setStatus('current')
extremeLacpGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 19, 1, 1, 1), LacpGroupId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeLacpGroup.setStatus('current')
extremeLacpMemberPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 19, 1, 1, 2), LacpMemberPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeLacpMemberPort.setStatus('current')
extremeLacpAggStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 19, 1, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeLacpAggStatus.setStatus('current')
mibBuilder.exportSymbols("EXTREME-LACP-MIB", LacpGroupId=LacpGroupId, extremeLacpTable=extremeLacpTable, extremeLacpEntry=extremeLacpEntry, PYSNMP_MODULE_ID=extremeLacp, LacpMemberPort=LacpMemberPort, extremeLacpAggStatus=extremeLacpAggStatus, extremeLacpMemberPort=extremeLacpMemberPort, extremeLacp=extremeLacp, extremeLacpGroup=extremeLacpGroup)
