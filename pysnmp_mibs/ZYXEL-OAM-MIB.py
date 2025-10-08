#
# PySNMP MIB module ZYXEL-OAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/zyxel/ZYXEL-OAM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:37:52 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("ZYXEL-OAM-MIB", zyxelOamPortTable=zyxelOamPortTable, zyxelOamSetup=zyxelOamSetup, PYSNMP_MODULE_ID=zyxelOam, zyOamPortFunctionsSupported=zyOamPortFunctionsSupported, zyOamState=zyOamState, zyxelOam=zyxelOam, zyxelOamPortEntry=zyxelOamPortEntry)
