#
# PySNMP MIB module AT-UFO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/allied/AT-UFO-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:12:46 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
modules, = mibBuilder.importSymbols("AT-SMI-MIB", "modules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
atUfo = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 605))
atUfo.setRevisions(('2018-09-20 00:00',))
if mibBuilder.loadTexts: atUfo.setLastUpdated('201809200000Z')
if mibBuilder.loadTexts: atUfo.setOrganization('Allied Telesis, Inc.')
atUfoTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 605, 0))
atUfoTrapVariables = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 605, 1))
atUfoVlanBlackHoleTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 605, 0, 1)).setObjects(("AT-UFO-MIB", "atUfoVlanId"), ("AT-UFO-MIB", "atUfoPreviousState"), ("AT-UFO-MIB", "atUfoCurrentState"))
if mibBuilder.loadTexts: atUfoVlanBlackHoleTrap.setStatus('current')
atUfoBlackHoleAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 605, 0, 2)).setObjects(("AT-UFO-MIB", "atUfoAlarmState"))
if mibBuilder.loadTexts: atUfoBlackHoleAlarmTrap.setStatus('current')
atUfoVlanId = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 605, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atUfoVlanId.setStatus('current')
atUfoPreviousState = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 605, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atUfoPreviousState.setStatus('current')
atUfoCurrentState = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 605, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atUfoCurrentState.setStatus('current')
atUfoAlarmState = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 605, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atUfoAlarmState.setStatus('current')
mibBuilder.exportSymbols("AT-UFO-MIB", atUfoVlanId=atUfoVlanId, atUfoAlarmState=atUfoAlarmState, PYSNMP_MODULE_ID=atUfo, atUfo=atUfo, atUfoTrapVariables=atUfoTrapVariables, atUfoBlackHoleAlarmTrap=atUfoBlackHoleAlarmTrap, atUfoVlanBlackHoleTrap=atUfoVlanBlackHoleTrap, atUfoPreviousState=atUfoPreviousState, atUfoTraps=atUfoTraps, atUfoCurrentState=atUfoCurrentState)
