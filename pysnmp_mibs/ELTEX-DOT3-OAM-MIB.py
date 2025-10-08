#
# PySNMP MIB module ELTEX-DOT3-OAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/eltex/ELTEX-DOT3-OAM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:32 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
eltexLtd, = mibBuilder.importSymbols("ELTEX-SMI-ACTUAL", "eltexLtd")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, iso, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "iso", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, TimeStamp, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TimeStamp", "TruthValue", "TextualConvention")
eltexDot3OamMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 30))
eltexDot3OamMIB.setRevisions(('2013-02-22 00:00',))
if mibBuilder.loadTexts: eltexDot3OamMIB.setLastUpdated('201302220000Z')
if mibBuilder.loadTexts: eltexDot3OamMIB.setOrganization('Eltex Ent')
eltexDot3OamObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 30, 1))
eltexDot3OamClearStatistic = MibScalar((1, 3, 6, 1, 4, 1, 35265, 30, 1, 7), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexDot3OamClearStatistic.setStatus('current')
mibBuilder.exportSymbols("ELTEX-DOT3-OAM-MIB", eltexDot3OamObjects=eltexDot3OamObjects, PYSNMP_MODULE_ID=eltexDot3OamMIB, eltexDot3OamClearStatistic=eltexDot3OamClearStatistic, eltexDot3OamMIB=eltexDot3OamMIB)
