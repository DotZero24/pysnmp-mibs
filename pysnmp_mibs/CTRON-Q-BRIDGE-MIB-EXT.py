#
# PySNMP MIB module CTRON-Q-BRIDGE-MIB-EXT (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cabletron/CTRON-Q-BRIDGE-MIB-EXT
# Produced by pysmi-1.1.12 at Thu Sep 11 10:05:57 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dot1dBasePortEntry, dot1dBasePort = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePortEntry", "dot1dBasePort")
ctVlanExt, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctVlanExt")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
dot1qVlanIndex, dot1qFdbId, dot1qTpFdbAddress, VlanIndex, PortList, dot1qVlanCurrentEntry = mibBuilder.importSymbols("Q-BRIDGE-MIB", "dot1qVlanIndex", "dot1qFdbId", "dot1qTpFdbAddress", "VlanIndex", "PortList", "dot1qVlanCurrentEntry")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ctQBridgeMibExt = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7))
ctQBridgeMibExt.setRevisions(('2012-02-14 14:42', '2012-01-09 13:49', '2010-06-30 18:25', '2007-02-16 17:44', '2005-01-21 17:17', '2004-06-04 12:41', '2003-12-15 20:53', '2002-07-26 20:45', '2002-07-19 14:12', '2001-04-16 18:16', '2001-01-10 13:29', '1999-10-06 08:12',))
if mibBuilder.loadTexts: ctQBridgeMibExt.setLastUpdated('201202141442Z')
if mibBuilder.loadTexts: ctQBridgeMibExt.setOrganization('Enterasys Networks, Inc.')
ctQBridgeMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1))
ctDot1qPortVlanExtTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 1), )
if mibBuilder.loadTexts: ctDot1qPortVlanExtTable.setStatus('current')
ctDot1qPortVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 1, 1), )
dot1dBasePortEntry.registerAugmentions(("CTRON-Q-BRIDGE-MIB-EXT", "ctDot1qPortVlanEntry"))
ctDot1qPortVlanEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())
if mibBuilder.loadTexts: ctDot1qPortVlanEntry.setStatus('current')
ctDot1qPortDefaultForwardMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("forwardNoFrames", 1), ("forwardAllFramesAsTagged", 2), ("forwardAllFramesAsUntagged", 3))).clone('forwardNoFrames')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDot1qPortDefaultForwardMode.setStatus('current')
ctDot1qPortDiscardTagged = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 1, 1, 2), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDot1qPortDiscardTagged.setStatus('current')
ctDot1qPortReplaceTCI = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 1, 1, 3), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDot1qPortReplaceTCI.setStatus('current')
ctDot1qVlanDynamicEgressTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 2), )
if mibBuilder.loadTexts: ctDot1qVlanDynamicEgressTable.setStatus('current')
ctDot1qVlanDynamicEgressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 2, 1), ).setIndexNames((0, "CTRON-Q-BRIDGE-MIB-EXT", "ctDot1qVlanDynamicEgressIndex"))
if mibBuilder.loadTexts: ctDot1qVlanDynamicEgressEntry.setStatus('current')
ctDot1qVlanDynamicEgressIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 2, 1, 1), VlanIndex())
if mibBuilder.loadTexts: ctDot1qVlanDynamicEgressIndex.setStatus('current')
ctDot1qVlanDynamicEgressStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 2, 1, 2), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDot1qVlanDynamicEgressStatus.setStatus('current')
ctDot1qVlanCurrentExtTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 3), )
if mibBuilder.loadTexts: ctDot1qVlanCurrentExtTable.setStatus('current')
ctDot1qVlanCurrentEntryExt = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 3, 1), )
dot1qVlanCurrentEntry.registerAugmentions(("CTRON-Q-BRIDGE-MIB-EXT", "ctDot1qVlanCurrentEntryExt"))
ctDot1qVlanCurrentEntryExt.setIndexNames(*dot1qVlanCurrentEntry.getIndexNames())
if mibBuilder.loadTexts: ctDot1qVlanCurrentEntryExt.setStatus('current')
ctDot1qVlanForbidEgressPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 3, 1, 1), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDot1qVlanForbidEgressPorts.setStatus('current')
ctDot1qPortVlanEgressTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 4), )
if mibBuilder.loadTexts: ctDot1qPortVlanEgressTable.setStatus('current')
ctDot1qPortVlanEgressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 4, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"), (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"))
if mibBuilder.loadTexts: ctDot1qPortVlanEgressEntry.setStatus('current')
ctDot1qPortVlanEgressStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("other", 1), ("static", 2), ("gvrp", 3), ("ctDynamicEgress", 4), ("etsysPolicyProfile", 5), ("ctPortDefFwdMode", 6), ("rfc3580VlanTunnelAttribute", 7), ("mvrp", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDot1qPortVlanEgressStatus.setStatus('current')
ctDot1qPortVlanEgressType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("tagged", 1), ("untagged", 2), ("forbidden", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDot1qPortVlanEgressType.setStatus('current')
ctDot1qTpFdbExtTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 5), )
if mibBuilder.loadTexts: ctDot1qTpFdbExtTable.setStatus('current')
ctDot1qTpFdbExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 5, 1), ).setIndexNames((0, "Q-BRIDGE-MIB", "dot1qFdbId"), (0, "Q-BRIDGE-MIB", "dot1qTpFdbAddress"))
if mibBuilder.loadTexts: ctDot1qTpFdbExtEntry.setStatus('current')
ctDot1qTpFdbRemoveAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 5, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDot1qTpFdbRemoveAddress.setStatus('current')
ctDot1qVlanGvrpRestrictedTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 6), )
if mibBuilder.loadTexts: ctDot1qVlanGvrpRestrictedTable.setStatus('current')
ctDot1qVlanGvrpRestrictedEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 6, 1), ).setIndexNames((0, "CTRON-Q-BRIDGE-MIB-EXT", "ctDot1qVlanGvrpRestrictedIndex"))
if mibBuilder.loadTexts: ctDot1qVlanGvrpRestrictedEntry.setStatus('current')
ctDot1qVlanGvrpRestrictedIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 6, 1, 1), VlanIndex())
if mibBuilder.loadTexts: ctDot1qVlanGvrpRestrictedIndex.setStatus('current')
ctDot1qVlanGvrpRestrictedStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 6, 1, 2), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDot1qVlanGvrpRestrictedStatus.setStatus('current')
ctDot1qPortVlanStaticEgressTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 7), )
if mibBuilder.loadTexts: ctDot1qPortVlanStaticEgressTable.setStatus('current')
ctDot1qPortVlanStaticEgressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 7, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"), (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"))
if mibBuilder.loadTexts: ctDot1qPortVlanStaticEgressEntry.setStatus('current')
ctDot1qPortVlanStaticEgressType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("tagged", 1), ("untagged", 2), ("forbidden", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDot1qPortVlanStaticEgressType.setStatus('current')
ctQBridgeConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2))
ctQBridgeGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2, 1))
ctQBridgeCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2, 2))
ctQBridgePortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2, 1, 1)).setObjects(("CTRON-Q-BRIDGE-MIB-EXT", "ctDot1qPortDefaultForwardMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctQBridgePortGroup = ctQBridgePortGroup.setStatus('deprecated')
ctQBridgeVlanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2, 1, 2)).setObjects(("CTRON-Q-BRIDGE-MIB-EXT", "ctDot1qVlanDynamicEgressStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctQBridgeVlanGroup = ctQBridgeVlanGroup.setStatus('current')
ctQBridgePortGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2, 1, 3)).setObjects(("CTRON-Q-BRIDGE-MIB-EXT", "ctDot1qPortDefaultForwardMode"), ("CTRON-Q-BRIDGE-MIB-EXT", "ctDot1qPortDiscardTagged"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctQBridgePortGroup2 = ctQBridgePortGroup2.setStatus('current')
ctQBridgeVlanCurrentForbidGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2, 1, 4)).setObjects(("CTRON-Q-BRIDGE-MIB-EXT", "ctDot1qVlanForbidEgressPorts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctQBridgeVlanCurrentForbidGroup = ctQBridgeVlanCurrentForbidGroup.setStatus('current')
ctQBridgePortReplaceTCIGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2, 1, 5)).setObjects(("CTRON-Q-BRIDGE-MIB-EXT", "ctDot1qPortReplaceTCI"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctQBridgePortReplaceTCIGroup = ctQBridgePortReplaceTCIGroup.setStatus('current')
ctQBridgePortVlanEgressGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2, 1, 6)).setObjects(("CTRON-Q-BRIDGE-MIB-EXT", "ctDot1qPortVlanEgressStatus"), ("CTRON-Q-BRIDGE-MIB-EXT", "ctDot1qPortVlanEgressType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctQBridgePortVlanEgressGroup = ctQBridgePortVlanEgressGroup.setStatus('deprecated')
ctQBridgeTpFdbTableExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2, 1, 7)).setObjects(("CTRON-Q-BRIDGE-MIB-EXT", "ctDot1qTpFdbRemoveAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctQBridgeTpFdbTableExtGroup = ctQBridgeTpFdbTableExtGroup.setStatus('current')
ctQBridgeVlanGvrpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2, 1, 8)).setObjects(("CTRON-Q-BRIDGE-MIB-EXT", "ctDot1qVlanGvrpRestrictedStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctQBridgeVlanGvrpGroup = ctQBridgeVlanGvrpGroup.setStatus('current')
ctQBridgePortVlanEgressGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2, 1, 9)).setObjects(("CTRON-Q-BRIDGE-MIB-EXT", "ctDot1qPortVlanEgressStatus"), ("CTRON-Q-BRIDGE-MIB-EXT", "ctDot1qPortVlanEgressType"), ("CTRON-Q-BRIDGE-MIB-EXT", "ctDot1qPortVlanStaticEgressType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctQBridgePortVlanEgressGroup2 = ctQBridgePortVlanEgressGroup2.setStatus('current')
ctDot1qVlan = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2, 2, 1)).setObjects(("CTRON-Q-BRIDGE-MIB-EXT", "ctQBridgePortGroup"), ("CTRON-Q-BRIDGE-MIB-EXT", "ctQBridgeVlanGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctDot1qVlan = ctDot1qVlan.setStatus('deprecated')
ctDot1qVlan2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2, 2, 2)).setObjects(("CTRON-Q-BRIDGE-MIB-EXT", "ctQBridgeVlanGroup"), ("CTRON-Q-BRIDGE-MIB-EXT", "ctQBridgePortGroup2"), ("CTRON-Q-BRIDGE-MIB-EXT", "ctQBridgePortReplaceTCIGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctDot1qVlan2 = ctDot1qVlan2.setStatus('deprecated')
ctDot1qVlanCurentCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2, 2, 3)).setObjects(("CTRON-Q-BRIDGE-MIB-EXT", "ctQBridgeVlanCurrentForbidGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctDot1qVlanCurentCompliance = ctDot1qVlanCurentCompliance.setStatus('current')
ctDot1qPortVlanEgressCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2, 2, 4)).setObjects(("CTRON-Q-BRIDGE-MIB-EXT", "ctQBridgePortVlanEgressGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctDot1qPortVlanEgressCompliance = ctDot1qPortVlanEgressCompliance.setStatus('deprecated')
ctDot1qTpFdbTableExtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2, 2, 5)).setObjects(("CTRON-Q-BRIDGE-MIB-EXT", "ctQBridgeTpFdbTableExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctDot1qTpFdbTableExtCompliance = ctDot1qTpFdbTableExtCompliance.setStatus('current')
ctDot1qVlan3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2, 2, 6)).setObjects(("CTRON-Q-BRIDGE-MIB-EXT", "ctQBridgeVlanGroup"), ("CTRON-Q-BRIDGE-MIB-EXT", "ctQBridgePortGroup2"), ("CTRON-Q-BRIDGE-MIB-EXT", "ctQBridgePortReplaceTCIGroup"), ("CTRON-Q-BRIDGE-MIB-EXT", "ctQBridgeVlanGvrpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctDot1qVlan3 = ctDot1qVlan3.setStatus('current')
ctDot1qPortVlanEgressCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2, 2, 7)).setObjects(("CTRON-Q-BRIDGE-MIB-EXT", "ctQBridgePortVlanEgressGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctDot1qPortVlanEgressCompliance2 = ctDot1qPortVlanEgressCompliance2.setStatus('current')
mibBuilder.exportSymbols("CTRON-Q-BRIDGE-MIB-EXT", ctDot1qVlanDynamicEgressTable=ctDot1qVlanDynamicEgressTable, ctQBridgeVlanCurrentForbidGroup=ctQBridgeVlanCurrentForbidGroup, ctQBridgeVlanGvrpGroup=ctQBridgeVlanGvrpGroup, ctDot1qPortVlanEgressEntry=ctDot1qPortVlanEgressEntry, ctDot1qPortVlanStaticEgressTable=ctDot1qPortVlanStaticEgressTable, ctDot1qPortVlanStaticEgressEntry=ctDot1qPortVlanStaticEgressEntry, ctQBridgeCompliances=ctQBridgeCompliances, ctDot1qVlanGvrpRestrictedTable=ctDot1qVlanGvrpRestrictedTable, ctDot1qPortVlanEgressTable=ctDot1qPortVlanEgressTable, ctDot1qVlanGvrpRestrictedIndex=ctDot1qVlanGvrpRestrictedIndex, ctDot1qPortVlanExtTable=ctDot1qPortVlanExtTable, ctDot1qTpFdbTableExtCompliance=ctDot1qTpFdbTableExtCompliance, ctDot1qVlan3=ctDot1qVlan3, ctDot1qVlanCurrentExtTable=ctDot1qVlanCurrentExtTable, ctDot1qPortVlanEntry=ctDot1qPortVlanEntry, ctQBridgeGroups=ctQBridgeGroups, ctQBridgeMIBObjects=ctQBridgeMIBObjects, ctDot1qVlan2=ctDot1qVlan2, ctQBridgePortVlanEgressGroup2=ctQBridgePortVlanEgressGroup2, PYSNMP_MODULE_ID=ctQBridgeMibExt, ctDot1qVlan=ctDot1qVlan, ctDot1qPortReplaceTCI=ctDot1qPortReplaceTCI, ctQBridgeMibExt=ctQBridgeMibExt, ctDot1qVlanCurrentEntryExt=ctDot1qVlanCurrentEntryExt, ctQBridgeVlanGroup=ctQBridgeVlanGroup, ctQBridgePortReplaceTCIGroup=ctQBridgePortReplaceTCIGroup, ctDot1qPortDiscardTagged=ctDot1qPortDiscardTagged, ctDot1qVlanDynamicEgressEntry=ctDot1qVlanDynamicEgressEntry, ctDot1qVlanGvrpRestrictedEntry=ctDot1qVlanGvrpRestrictedEntry, ctDot1qVlanCurentCompliance=ctDot1qVlanCurentCompliance, ctDot1qPortVlanEgressStatus=ctDot1qPortVlanEgressStatus, ctDot1qPortVlanEgressCompliance=ctDot1qPortVlanEgressCompliance, ctDot1qPortDefaultForwardMode=ctDot1qPortDefaultForwardMode, ctDot1qVlanDynamicEgressIndex=ctDot1qVlanDynamicEgressIndex, ctQBridgeConformance=ctQBridgeConformance, ctDot1qVlanForbidEgressPorts=ctDot1qVlanForbidEgressPorts, ctDot1qTpFdbExtEntry=ctDot1qTpFdbExtEntry, ctDot1qTpFdbRemoveAddress=ctDot1qTpFdbRemoveAddress, ctDot1qVlanGvrpRestrictedStatus=ctDot1qVlanGvrpRestrictedStatus, ctDot1qPortVlanStaticEgressType=ctDot1qPortVlanStaticEgressType, ctDot1qVlanDynamicEgressStatus=ctDot1qVlanDynamicEgressStatus, ctQBridgePortGroup2=ctQBridgePortGroup2, ctDot1qPortVlanEgressCompliance2=ctDot1qPortVlanEgressCompliance2, ctQBridgePortGroup=ctQBridgePortGroup, ctQBridgePortVlanEgressGroup=ctQBridgePortVlanEgressGroup, ctQBridgeTpFdbTableExtGroup=ctQBridgeTpFdbTableExtGroup, ctDot1qPortVlanEgressType=ctDot1qPortVlanEgressType, ctDot1qTpFdbExtTable=ctDot1qTpFdbExtTable)
