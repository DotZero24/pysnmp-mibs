#
# PySNMP MIB module AT-UFO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/allied/AT-UFO-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:44:35 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
modules, = mibBuilder.importSymbols("AT-SMI-MIB", "modules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
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
mibBuilder.exportSymbols("AT-UFO-MIB", PYSNMP_MODULE_ID=atUfo, atUfoTraps=atUfoTraps, atUfoTrapVariables=atUfoTrapVariables, atUfoPreviousState=atUfoPreviousState, atUfoAlarmState=atUfoAlarmState, atUfoVlanBlackHoleTrap=atUfoVlanBlackHoleTrap, atUfoCurrentState=atUfoCurrentState, atUfo=atUfo, atUfoBlackHoleAlarmTrap=atUfoBlackHoleAlarmTrap, atUfoVlanId=atUfoVlanId)
