#
# PySNMP MIB module ZYXEL-MIRROR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/zyxel/ZYXEL-MIRROR-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:38:10 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelMirror = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 65))
if mibBuilder.loadTexts: zyxelMirror.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelMirror.setOrganization('Enterprise Solution ZyXEL')
zyxelMirrorSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 65, 1))
zyMirrorState = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 65, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMirrorState.setStatus('current')
zyMirrorMonitorPort = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 65, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMirrorMonitorPort.setStatus('current')
zyxelMirrorTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 65, 1, 3), )
if mibBuilder.loadTexts: zyxelMirrorTable.setStatus('current')
zyxelMirrorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 65, 1, 3, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: zyxelMirrorEntry.setStatus('current')
zyMirrorMirroredState = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 65, 1, 3, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMirrorMirroredState.setStatus('current')
zyMirrorDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 65, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("ingress", 0), ("egress", 1), ("both", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMirrorDirection.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-MIRROR-MIB", zyMirrorMonitorPort=zyMirrorMonitorPort, zyxelMirror=zyxelMirror, zyxelMirrorSetup=zyxelMirrorSetup, zyxelMirrorEntry=zyxelMirrorEntry, zyxelMirrorTable=zyxelMirrorTable, zyMirrorState=zyMirrorState, zyMirrorDirection=zyMirrorDirection, zyMirrorMirroredState=zyMirrorMirroredState, PYSNMP_MODULE_ID=zyxelMirror)
