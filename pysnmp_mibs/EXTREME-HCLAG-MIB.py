#
# PySNMP MIB module EXTREME-HCLAG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/extreme/EXTREME-HCLAG-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:58:54 2025
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
mibBuilder.exportSymbols("EXTREME-HCLAG-MIB", extremeHclagAdminState=extremeHclagAdminState, extremeHclagGroup=extremeHclagGroup, extremeHclag=extremeHclag, HclagMemberPort=HclagMemberPort, HclagGroupId=HclagGroupId, extremeHclagLinkState=extremeHclagLinkState, extremeHclagMemberPort=extremeHclagMemberPort, extremeHclagTable=extremeHclagTable, extremeHclagEntry=extremeHclagEntry, extremeHclagStatus=extremeHclagStatus, PYSNMP_MODULE_ID=extremeHclag)
