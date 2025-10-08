#
# PySNMP MIB module AT-EPSR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/allied-old/AT-EPSR-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:08:20 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
DisplayStringUnsized, modules = mibBuilder.importSymbols("AT-SMI-MIB", "DisplayStringUnsized", "modules")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
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
mibBuilder.exportSymbols("AT-EPSR-MIB", epsrNodeTrap=epsrNodeTrap, epsrFromState=epsrFromState, epsrDomainName=epsrDomainName, PYSNMP_MODULE_ID=epsr, epsrSecondaryIfIndex=epsrSecondaryIfIndex, EpsrNodeState=EpsrNodeState, epsrToState=epsrToState, epsrNodeTrapType=epsrNodeTrapType, epsrEventVariablesEntry=epsrEventVariablesEntry, epsrControlVlanId=epsrControlVlanId, epsrPrimaryIfIndex=epsrPrimaryIfIndex, epsrSecondaryIfState=epsrSecondaryIfState, epsrPrimaryIfState=epsrPrimaryIfState, EpsrInterfaceState=EpsrInterfaceState, epsr=epsr, epsrEventVariablesTable=epsrEventVariablesTable, epsrEvents=epsrEvents)
