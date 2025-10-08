#
# PySNMP MIB module KEYING-PRIVATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/quanta/KEYING-PRIVATE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:41:22 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
switch, = mibBuilder.importSymbols("QUANTA-SWITCH-MIB", "switch")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowPointer, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowPointer", "RowStatus", "TextualConvention")
keyingPrivate = ModuleIdentity((1, 3, 6, 1, 4, 1, 7244, 2, 24))
if mibBuilder.loadTexts: keyingPrivate.setLastUpdated('201108310000Z')
if mibBuilder.loadTexts: keyingPrivate.setOrganization('QCI')
agentFeatureKeyingGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 7244, 2, 24, 1))
agentFeatureKeyingEnableKey = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 24, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentFeatureKeyingEnableKey.setStatus('current')
agentFeatureKeyingDisableKey = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 24, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentFeatureKeyingDisableKey.setStatus('current')
agentFeatureKeyingTable = MibTable((1, 3, 6, 1, 4, 1, 7244, 2, 24, 1, 3), )
if mibBuilder.loadTexts: agentFeatureKeyingTable.setStatus('current')
agentFeatureKeyingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7244, 2, 24, 1, 3, 1), ).setIndexNames((0, "KEYING-PRIVATE-MIB", "agentFeatureKeyingIndex"))
if mibBuilder.loadTexts: agentFeatureKeyingEntry.setStatus('current')
agentFeatureKeyingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 24, 1, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: agentFeatureKeyingIndex.setStatus('current')
agentFeatureKeyingName = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 24, 1, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentFeatureKeyingName.setStatus('current')
agentFeatureKeyingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 24, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentFeatureKeyingStatus.setStatus('current')
mibBuilder.exportSymbols("KEYING-PRIVATE-MIB", agentFeatureKeyingEnableKey=agentFeatureKeyingEnableKey, agentFeatureKeyingStatus=agentFeatureKeyingStatus, agentFeatureKeyingGroup=agentFeatureKeyingGroup, keyingPrivate=keyingPrivate, agentFeatureKeyingIndex=agentFeatureKeyingIndex, agentFeatureKeyingName=agentFeatureKeyingName, PYSNMP_MODULE_ID=keyingPrivate, agentFeatureKeyingEntry=agentFeatureKeyingEntry, agentFeatureKeyingTable=agentFeatureKeyingTable, agentFeatureKeyingDisableKey=agentFeatureKeyingDisableKey)
