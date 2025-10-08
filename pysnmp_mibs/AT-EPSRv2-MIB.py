#
# PySNMP MIB module AT-EPSRv2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/allied-old/AT-EPSRv2-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:12:43 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
DisplayStringUnsized, sysinfo, modules = mibBuilder.importSymbols("AT-SMI-MIB", "DisplayStringUnsized", "sysinfo", "modules")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
atEpsrv2 = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536))
atEpsrv2.setRevisions(('2008-12-23 01:30',))
if mibBuilder.loadTexts: atEpsrv2.setLastUpdated('200812230130Z')
if mibBuilder.loadTexts: atEpsrv2.setOrganization('Allied Telesis, Inc')
class AtEpsrv2NodeState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("idle", 0), ("complete", 1), ("failed", 2), ("linksUp", 3), ("linksDown", 4), ("preForward", 5), ("unknown", 6))

class AtEpsrv2InterfaceState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("down", 2), ("blocked", 3), ("forward", 4))

atEpsrv2Events = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 1))
atEpsrv2NodeTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 1, 1)).setObjects(("AT-EPSRv2-MIB", "atEpsrv2NodeType"), ("AT-EPSRv2-MIB", "atEpsrv2DomainName"), ("AT-EPSRv2-MIB", "atEpsrv2DomainID"), ("AT-EPSRv2-MIB", "atEpsrv2FromState"), ("AT-EPSRv2-MIB", "atEpsrv2CurrentState"), ("AT-EPSRv2-MIB", "atEpsrv2ControlVlanId"), ("AT-EPSRv2-MIB", "atEpsrv2PrimaryIfIndex"), ("AT-EPSRv2-MIB", "atEpsrv2PrimaryIfState"), ("AT-EPSRv2-MIB", "atEpsrv2SecondaryIfIndex"), ("AT-EPSRv2-MIB", "atEpsrv2SecondaryIfState"))
if mibBuilder.loadTexts: atEpsrv2NodeTrap.setStatus('current')
atEpsrv2VariablesTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 2), )
if mibBuilder.loadTexts: atEpsrv2VariablesTable.setStatus('current')
atEpsrv2VariablesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 2, 1), ).setIndexNames((0, "AT-EPSRv2-MIB", "atEpsrv2DomainID"))
if mibBuilder.loadTexts: atEpsrv2VariablesEntry.setStatus('current')
atEpsrv2NodeType = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("masterNode", 1), ("transitNode", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atEpsrv2NodeType.setStatus('current')
atEpsrv2DomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 2, 1, 2), DisplayStringUnsized().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atEpsrv2DomainName.setStatus('current')
atEpsrv2DomainID = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atEpsrv2DomainID.setStatus('current')
atEpsrv2FromState = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 2, 1, 4), AtEpsrv2NodeState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atEpsrv2FromState.setStatus('current')
atEpsrv2CurrentState = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 2, 1, 5), AtEpsrv2NodeState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atEpsrv2CurrentState.setStatus('current')
atEpsrv2ControlVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atEpsrv2ControlVlanId.setStatus('current')
atEpsrv2PrimaryIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 2, 1, 7), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atEpsrv2PrimaryIfIndex.setStatus('current')
atEpsrv2PrimaryIfState = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 2, 1, 8), AtEpsrv2InterfaceState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atEpsrv2PrimaryIfState.setStatus('current')
atEpsrv2SecondaryIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 2, 1, 9), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atEpsrv2SecondaryIfIndex.setStatus('current')
atEpsrv2SecondaryIfState = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 536, 2, 1, 10), AtEpsrv2InterfaceState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atEpsrv2SecondaryIfState.setStatus('current')
mibBuilder.exportSymbols("AT-EPSRv2-MIB", atEpsrv2DomainID=atEpsrv2DomainID, atEpsrv2PrimaryIfIndex=atEpsrv2PrimaryIfIndex, atEpsrv2PrimaryIfState=atEpsrv2PrimaryIfState, atEpsrv2Events=atEpsrv2Events, atEpsrv2NodeTrap=atEpsrv2NodeTrap, atEpsrv2VariablesTable=atEpsrv2VariablesTable, AtEpsrv2NodeState=AtEpsrv2NodeState, PYSNMP_MODULE_ID=atEpsrv2, atEpsrv2CurrentState=atEpsrv2CurrentState, atEpsrv2VariablesEntry=atEpsrv2VariablesEntry, atEpsrv2SecondaryIfIndex=atEpsrv2SecondaryIfIndex, atEpsrv2DomainName=atEpsrv2DomainName, AtEpsrv2InterfaceState=AtEpsrv2InterfaceState, atEpsrv2NodeType=atEpsrv2NodeType, atEpsrv2FromState=atEpsrv2FromState, atEpsrv2SecondaryIfState=atEpsrv2SecondaryIfState, atEpsrv2ControlVlanId=atEpsrv2ControlVlanId, atEpsrv2=atEpsrv2)
