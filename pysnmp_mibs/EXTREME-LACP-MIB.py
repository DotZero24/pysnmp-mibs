#
# PySNMP MIB module EXTREME-LACP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/extreme/EXTREME-LACP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:58:56 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
extremeAgent, = mibBuilder.importSymbols("EXTREME-BASE-MIB", "extremeAgent")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
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
mibBuilder.exportSymbols("EXTREME-LACP-MIB", extremeLacpGroup=extremeLacpGroup, PYSNMP_MODULE_ID=extremeLacp, extremeLacp=extremeLacp, extremeLacpMemberPort=extremeLacpMemberPort, extremeLacpAggStatus=extremeLacpAggStatus, LacpGroupId=LacpGroupId, LacpMemberPort=LacpMemberPort, extremeLacpEntry=extremeLacpEntry, extremeLacpTable=extremeLacpTable)
