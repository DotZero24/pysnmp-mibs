#
# PySNMP MIB module RAISECOM-DOT1X-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/raisecom/RAISECOM-DOT1X-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:31:00 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dot1xPaePortEntry, = mibBuilder.importSymbols("IEEE8021-PAE-MIB", "dot1xPaePortEntry")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
iscomSwitch, = mibBuilder.importSymbols("RAISECOM-BASE-MIB", "iscomSwitch")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Integer32, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, TimeTicks, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Integer32", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "TimeTicks", "Bits", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
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
mibBuilder.exportSymbols("RAISECOM-DOT1X-MIB", rcDot1xObjects=rcDot1xObjects, rcdot1xPortAuthControl=rcdot1xPortAuthControl, dot1xPortEntry=dot1xPortEntry, rcdot1xPortAuthMethod=rcdot1xPortAuthMethod, rcDot1xConfig=rcDot1xConfig, rcdot1xPortStatisticClear=rcdot1xPortStatisticClear, dot1xPortTable=dot1xPortTable, rcDot1x=rcDot1x, PYSNMP_MODULE_ID=rcDot1x)
