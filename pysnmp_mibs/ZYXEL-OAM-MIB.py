#
# PySNMP MIB module ZYXEL-OAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/zyxel/ZYXEL-OAM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:03:38 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelOam = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 56))
if mibBuilder.loadTexts: zyxelOam.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelOam.setOrganization('Enterprise Solution ZyXEL')
zyxelOamSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 56, 1))
zyOamState = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 56, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyOamState.setStatus('current')
zyxelOamPortTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 56, 1, 2), )
if mibBuilder.loadTexts: zyxelOamPortTable.setStatus('current')
zyxelOamPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 56, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: zyxelOamPortEntry.setStatus('current')
zyOamPortFunctionsSupported = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 56, 1, 2, 1, 1), Bits().clone(namedValues=NamedValues(("unidirectionalSupport", 0), ("loopbackSupport", 1), ("eventSupport", 2), ("variableSupport", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyOamPortFunctionsSupported.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-OAM-MIB", zyxelOam=zyxelOam, zyxelOamPortEntry=zyxelOamPortEntry, PYSNMP_MODULE_ID=zyxelOam, zyxelOamPortTable=zyxelOamPortTable, zyOamPortFunctionsSupported=zyOamPortFunctionsSupported, zyxelOamSetup=zyxelOamSetup, zyOamState=zyOamState)
