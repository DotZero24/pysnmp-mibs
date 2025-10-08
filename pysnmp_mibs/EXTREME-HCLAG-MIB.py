#
# PySNMP MIB module EXTREME-HCLAG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/extreme/EXTREME-HCLAG-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:02:01 2025
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
extremeHclag = ModuleIdentity((1, 3, 6, 1, 4, 1, 1916, 1, 38))
if mibBuilder.loadTexts: extremeHclag.setLastUpdated('1212061000Z')
if mibBuilder.loadTexts: extremeHclag.setOrganization('Extreme Networks, Inc.')
class HclagGroupId(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 32)

class HclagMemberPort(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

extremeHclagTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 38, 1), )
if mibBuilder.loadTexts: extremeHclagTable.setStatus('current')
extremeHclagEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 38, 1, 1), ).setIndexNames((0, "EXTREME-HCLAG-MIB", "extremeHclagGroup"), (0, "EXTREME-HCLAG-MIB", "extremeHclagMemberPort"))
if mibBuilder.loadTexts: extremeHclagEntry.setStatus('current')
extremeHclagGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 38, 1, 1, 1), HclagGroupId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeHclagGroup.setStatus('current')
extremeHclagMemberPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 38, 1, 1, 2), HclagMemberPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeHclagMemberPort.setStatus('current')
extremeHclagAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 38, 1, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeHclagAdminState.setStatus('current')
extremeHclagLinkState = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 38, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeHclagLinkState.setStatus('current')
extremeHclagStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 38, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeHclagStatus.setStatus('current')
mibBuilder.exportSymbols("EXTREME-HCLAG-MIB", extremeHclagMemberPort=extremeHclagMemberPort, extremeHclagLinkState=extremeHclagLinkState, extremeHclagEntry=extremeHclagEntry, extremeHclagTable=extremeHclagTable, HclagGroupId=HclagGroupId, extremeHclag=extremeHclag, PYSNMP_MODULE_ID=extremeHclag, HclagMemberPort=HclagMemberPort, extremeHclagAdminState=extremeHclagAdminState, extremeHclagGroup=extremeHclagGroup, extremeHclagStatus=extremeHclagStatus)
