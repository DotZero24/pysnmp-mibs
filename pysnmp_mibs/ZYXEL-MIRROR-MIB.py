#
# PySNMP MIB module ZYXEL-MIRROR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/zyxel/ZYXEL-MIRROR-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:04:08 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ZYXEL-MIRROR-MIB", PYSNMP_MODULE_ID=zyxelMirror, zyMirrorMonitorPort=zyMirrorMonitorPort, zyxelMirrorSetup=zyxelMirrorSetup, zyMirrorDirection=zyMirrorDirection, zyxelMirrorEntry=zyxelMirrorEntry, zyMirrorState=zyMirrorState, zyxelMirrorTable=zyxelMirrorTable, zyMirrorMirroredState=zyMirrorMirroredState, zyxelMirror=zyxelMirror)
