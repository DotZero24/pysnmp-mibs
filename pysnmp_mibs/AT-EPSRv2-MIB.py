#
# PySNMP MIB module AT-EPSRv2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/allied-old/AT-EPSRv2-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:44:33 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
DisplayStringUnsized, sysinfo, modules = mibBuilder.importSymbols("AT-SMI-MIB", "DisplayStringUnsized", "sysinfo", "modules")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
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
mibBuilder.exportSymbols("AT-EPSRv2-MIB", atEpsrv2FromState=atEpsrv2FromState, atEpsrv2CurrentState=atEpsrv2CurrentState, atEpsrv2SecondaryIfState=atEpsrv2SecondaryIfState, atEpsrv2PrimaryIfIndex=atEpsrv2PrimaryIfIndex, atEpsrv2=atEpsrv2, atEpsrv2VariablesTable=atEpsrv2VariablesTable, atEpsrv2ControlVlanId=atEpsrv2ControlVlanId, PYSNMP_MODULE_ID=atEpsrv2, atEpsrv2NodeType=atEpsrv2NodeType, AtEpsrv2NodeState=AtEpsrv2NodeState, atEpsrv2DomainID=atEpsrv2DomainID, AtEpsrv2InterfaceState=AtEpsrv2InterfaceState, atEpsrv2PrimaryIfState=atEpsrv2PrimaryIfState, atEpsrv2VariablesEntry=atEpsrv2VariablesEntry, atEpsrv2Events=atEpsrv2Events, atEpsrv2DomainName=atEpsrv2DomainName, atEpsrv2NodeTrap=atEpsrv2NodeTrap, atEpsrv2SecondaryIfIndex=atEpsrv2SecondaryIfIndex)
