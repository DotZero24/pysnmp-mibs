#
# PySNMP MIB module ZYXEL-DOS-PREVENTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/zyxel/ZYXEL-DOS-PREVENTION-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:38:17 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelDoSPrevention = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 119))
if mibBuilder.loadTexts: zyxelDoSPrevention.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelDoSPrevention.setOrganization('Enterprise Solution ZyXEL')
zyxelDoSPreventionSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 119, 1))
zyDoSPreventionState = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 119, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDoSPreventionState.setStatus('current')
zyxelDoSPreventionPortTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 119, 1, 2), )
if mibBuilder.loadTexts: zyxelDoSPreventionPortTable.setStatus('current')
zyxelDoSPreventionPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 119, 1, 2, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: zyxelDoSPreventionPortEntry.setStatus('current')
zyDoSPreventionPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 119, 1, 2, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDoSPreventionPortState.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-DOS-PREVENTION-MIB", PYSNMP_MODULE_ID=zyxelDoSPrevention, zyDoSPreventionPortState=zyDoSPreventionPortState, zyxelDoSPreventionSetup=zyxelDoSPreventionSetup, zyxelDoSPreventionPortEntry=zyxelDoSPreventionPortEntry, zyxelDoSPrevention=zyxelDoSPrevention, zyDoSPreventionState=zyDoSPreventionState, zyxelDoSPreventionPortTable=zyxelDoSPreventionPortTable)
