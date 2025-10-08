#
# PySNMP MIB module ELTEX-DOT3-OAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/eltex/ELTEX-DOT3-OAM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:11:45 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
eltexLtd, = mibBuilder.importSymbols("ELTEX-SMI-ACTUAL", "eltexLtd")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
TextualConvention, MacAddress, TruthValue, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "TruthValue", "TimeStamp", "DisplayString")
eltexDot3OamMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 30))
eltexDot3OamMIB.setRevisions(('2013-02-22 00:00',))
if mibBuilder.loadTexts: eltexDot3OamMIB.setLastUpdated('201302220000Z')
if mibBuilder.loadTexts: eltexDot3OamMIB.setOrganization('Eltex Ent')
eltexDot3OamObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 30, 1))
eltexDot3OamClearStatistic = MibScalar((1, 3, 6, 1, 4, 1, 35265, 30, 1, 7), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexDot3OamClearStatistic.setStatus('current')
mibBuilder.exportSymbols("ELTEX-DOT3-OAM-MIB", eltexDot3OamMIB=eltexDot3OamMIB, eltexDot3OamObjects=eltexDot3OamObjects, PYSNMP_MODULE_ID=eltexDot3OamMIB, eltexDot3OamClearStatistic=eltexDot3OamClearStatistic)
