#
# PySNMP MIB module RAISECOM-DOT1X-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/raisecom/RAISECOM-DOT1X-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:54:52 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dot1xPaePortEntry, = mibBuilder.importSymbols("IEEE8021-PAE-MIB", "dot1xPaePortEntry")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
iscomSwitch, = mibBuilder.importSymbols("RAISECOM-BASE-MIB", "iscomSwitch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
rcDot1x = ModuleIdentity((1, 3, 6, 1, 4, 1, 8886, 6, 1, 27))
if mibBuilder.loadTexts: rcDot1x.setLastUpdated('200711160000Z')
if mibBuilder.loadTexts: rcDot1x.setOrganization('Raisecom Science & Technology Co., ltd')
rcDot1xObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8886, 6, 1, 27, 1))
rcDot1xConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 8886, 6, 1, 27, 1, 1))
dot1xPortTable = MibTable((1, 3, 6, 1, 4, 1, 8886, 6, 1, 27, 1, 1, 1), )
if mibBuilder.loadTexts: dot1xPortTable.setStatus('current')
dot1xPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8886, 6, 1, 27, 1, 1, 1, 1), )
dot1xPaePortEntry.registerAugmentions(("RAISECOM-DOT1X-MIB", "dot1xPortEntry"))
dot1xPortEntry.setIndexNames(*dot1xPaePortEntry.getIndexNames())
if mibBuilder.loadTexts: dot1xPortEntry.setStatus('current')
rcdot1xPortAuthControl = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 27, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcdot1xPortAuthControl.setStatus('current')
rcdot1xPortStatisticClear = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 27, 1, 1, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcdot1xPortStatisticClear.setStatus('current')
rcdot1xPortAuthMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 27, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("portbased", 1), ("macbased", 2))).clone('portbased')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcdot1xPortAuthMethod.setStatus('current')
mibBuilder.exportSymbols("RAISECOM-DOT1X-MIB", PYSNMP_MODULE_ID=rcDot1x, rcDot1xConfig=rcDot1xConfig, rcdot1xPortAuthControl=rcdot1xPortAuthControl, dot1xPortEntry=dot1xPortEntry, rcdot1xPortStatisticClear=rcdot1xPortStatisticClear, dot1xPortTable=dot1xPortTable, rcDot1x=rcDot1x, rcDot1xObjects=rcDot1xObjects, rcdot1xPortAuthMethod=rcdot1xPortAuthMethod)
