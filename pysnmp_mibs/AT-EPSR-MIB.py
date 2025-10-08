#
# PySNMP MIB module AT-EPSR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/allied-old/AT-EPSR-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:41:17 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
DisplayStringUnsized, modules = mibBuilder.importSymbols("AT-SMI-MIB", "DisplayStringUnsized", "modules")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
epsr = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136))
epsr.setRevisions(('2006-11-22 12:12', '2006-02-16 16:19',))
if mibBuilder.loadTexts: epsr.setLastUpdated('200611221212Z')
if mibBuilder.loadTexts: epsr.setOrganization('Allied Telesis, Inc')
class EpsrNodeState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("idle", 0), ("complete", 1), ("failed", 2), ("linksUp", 3), ("linksDown", 4), ("preForward", 5), ("unknown", 6))

class EpsrInterfaceState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("blocked", 1), ("forward", 2))

epsrEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 1))
epsrNodeTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 1, 1)).setObjects(("AT-EPSR-MIB", "epsrNodeTrapType"), ("AT-EPSR-MIB", "epsrDomainName"), ("AT-EPSR-MIB", "epsrFromState"), ("AT-EPSR-MIB", "epsrToState"), ("AT-EPSR-MIB", "epsrControlVlanId"), ("AT-EPSR-MIB", "epsrPrimaryIfIndex"), ("AT-EPSR-MIB", "epsrPrimaryIfState"), ("AT-EPSR-MIB", "epsrSecondaryIfIndex"), ("AT-EPSR-MIB", "epsrSecondaryIfState"))
if mibBuilder.loadTexts: epsrNodeTrap.setStatus('current')
epsrEventVariablesTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 2), )
if mibBuilder.loadTexts: epsrEventVariablesTable.setStatus('current')
epsrEventVariablesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 2, 1), ).setIndexNames((0, "AT-EPSR-MIB", "epsrDomainName"))
if mibBuilder.loadTexts: epsrEventVariablesEntry.setStatus('current')
epsrNodeTrapType = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("unknown", 0), ("masterNodeTrap", 1), ("transitNodeTrap", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: epsrNodeTrapType.setStatus('current')
epsrDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 2, 1, 2), DisplayStringUnsized().subtype(subtypeSpec=ValueSizeConstraint(1, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: epsrDomainName.setStatus('current')
epsrFromState = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 2, 1, 3), EpsrNodeState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: epsrFromState.setStatus('current')
epsrToState = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 2, 1, 4), EpsrNodeState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: epsrToState.setStatus('current')
epsrControlVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: epsrControlVlanId.setStatus('current')
epsrPrimaryIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 2, 1, 6), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: epsrPrimaryIfIndex.setStatus('current')
epsrPrimaryIfState = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 2, 1, 7), EpsrInterfaceState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: epsrPrimaryIfState.setStatus('current')
epsrSecondaryIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 2, 1, 8), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: epsrSecondaryIfIndex.setStatus('current')
epsrSecondaryIfState = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 2, 1, 9), EpsrInterfaceState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: epsrSecondaryIfState.setStatus('current')
mibBuilder.exportSymbols("AT-EPSR-MIB", epsrEvents=epsrEvents, epsrSecondaryIfIndex=epsrSecondaryIfIndex, epsrEventVariablesTable=epsrEventVariablesTable, EpsrNodeState=EpsrNodeState, EpsrInterfaceState=EpsrInterfaceState, epsrControlVlanId=epsrControlVlanId, epsrPrimaryIfState=epsrPrimaryIfState, epsrDomainName=epsrDomainName, epsrNodeTrap=epsrNodeTrap, epsrFromState=epsrFromState, epsrSecondaryIfState=epsrSecondaryIfState, epsrPrimaryIfIndex=epsrPrimaryIfIndex, PYSNMP_MODULE_ID=epsr, epsrEventVariablesEntry=epsrEventVariablesEntry, epsrNodeTrapType=epsrNodeTrapType, epsr=epsr, epsrToState=epsrToState)
