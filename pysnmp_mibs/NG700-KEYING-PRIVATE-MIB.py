#
# PySNMP MIB module NG700-KEYING-PRIVATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/netgear/NG700-KEYING-PRIVATE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:50:47 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ng700smartswitch, = mibBuilder.importSymbols("NG700-REF-MIB", "ng700smartswitch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, DisplayString, RowPointer, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "RowPointer", "TextualConvention")
fastPathKeyingPrivate = ModuleIdentity((1, 3, 6, 1, 4, 1, 4526, 11, 24))
fastPathKeyingPrivate.setRevisions(('2011-01-26 00:00', '2007-05-23 00:00',))
if mibBuilder.loadTexts: fastPathKeyingPrivate.setLastUpdated('201101260000Z')
if mibBuilder.loadTexts: fastPathKeyingPrivate.setOrganization('Netgear Inc')
agentFeatureKeyingGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 11, 24, 1))
agentFeatureKeyingEnableKey = MibScalar((1, 3, 6, 1, 4, 1, 4526, 11, 24, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentFeatureKeyingEnableKey.setStatus('current')
agentFeatureKeyingDisableKey = MibScalar((1, 3, 6, 1, 4, 1, 4526, 11, 24, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentFeatureKeyingDisableKey.setStatus('current')
agentFeatureKeyingTable = MibTable((1, 3, 6, 1, 4, 1, 4526, 11, 24, 1, 3), )
if mibBuilder.loadTexts: agentFeatureKeyingTable.setStatus('current')
agentFeatureKeyingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4526, 11, 24, 1, 3, 1), ).setIndexNames((0, "NG700-KEYING-PRIVATE-MIB", "agentFeatureKeyingIndex"))
if mibBuilder.loadTexts: agentFeatureKeyingEntry.setStatus('current')
agentFeatureKeyingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 11, 24, 1, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: agentFeatureKeyingIndex.setStatus('current')
agentFeatureKeyingName = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 11, 24, 1, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentFeatureKeyingName.setStatus('current')
agentFeatureKeyingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 11, 24, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentFeatureKeyingStatus.setStatus('current')
mibBuilder.exportSymbols("NG700-KEYING-PRIVATE-MIB", agentFeatureKeyingEnableKey=agentFeatureKeyingEnableKey, fastPathKeyingPrivate=fastPathKeyingPrivate, agentFeatureKeyingName=agentFeatureKeyingName, agentFeatureKeyingStatus=agentFeatureKeyingStatus, agentFeatureKeyingDisableKey=agentFeatureKeyingDisableKey, agentFeatureKeyingGroup=agentFeatureKeyingGroup, agentFeatureKeyingTable=agentFeatureKeyingTable, agentFeatureKeyingEntry=agentFeatureKeyingEntry, agentFeatureKeyingIndex=agentFeatureKeyingIndex, PYSNMP_MODULE_ID=fastPathKeyingPrivate)
