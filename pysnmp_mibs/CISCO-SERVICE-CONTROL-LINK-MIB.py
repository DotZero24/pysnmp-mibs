#
# PySNMP MIB module CISCO-SERVICE-CONTROL-LINK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-SERVICE-CONTROL-LINK-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:28:11 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
EntPhysicalIndexOrZero, = mibBuilder.importSymbols("CISCO-TC", "EntPhysicalIndexOrZero")
entPhysicalIndex, PhysicalIndex = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex", "PhysicalIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
ciscoServiceControlLinkMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 631))
ciscoServiceControlLinkMIB.setRevisions(('2007-06-26 00:00',))
if mibBuilder.loadTexts: ciscoServiceControlLinkMIB.setLastUpdated('200706260000Z')
if mibBuilder.loadTexts: ciscoServiceControlLinkMIB.setOrganization('Cisco Systems, Inc.')
ciscoSCLinkMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 631, 0))
ciscoSCLinkMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 631, 1))
ciscoSCLinkMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 631, 2))
class CsceLinkModeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("bypass", 2), ("forwarding", 3), ("cutoff", 4), ("sniffing", 5))

cscLinkNotifsEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 631, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cscLinkNotifsEnabled.setStatus('current')
cscLinkStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 631, 1, 2), )
if mibBuilder.loadTexts: cscLinkStatusTable.setStatus('current')
cscLinkStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 631, 1, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cscLinkStatusEntry.setStatus('current')
cscLinkAdminModeOnActive = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 631, 1, 2, 1, 1), CsceLinkModeType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cscLinkAdminModeOnActive.setStatus('current')
cscLinkAdminModeOnFailure = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 631, 1, 2, 1, 2), CsceLinkModeType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cscLinkAdminModeOnFailure.setStatus('current')
cscLinkOperMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 631, 1, 2, 1, 3), CsceLinkModeType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cscLinkOperMode.setStatus('current')
cscLinkAdminReflectionEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 631, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("reflectionEnabled", 1), ("reflectionOnAllPortsEnabled", 2), ("reflectionDisabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cscLinkAdminReflectionEnable.setStatus('current')
cscLinkSubscriberSidePortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 631, 1, 2, 1, 5), EntPhysicalIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cscLinkSubscriberSidePortIndex.setStatus('current')
cscLinkNetworkSidePortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 631, 1, 2, 1, 6), EntPhysicalIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cscLinkNetworkSidePortIndex.setStatus('current')
cscLinkAdminReflectionState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 631, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("noLinkReflection", 1), ("reflectingFailureToNetwork", 2), ("reflectingFailureToSubscriber", 3), ("reflectingFailureToBoth", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cscLinkAdminReflectionState.setStatus('current')
ciscoServiceControlLinkModeChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 631, 0, 1)).setObjects(("CISCO-SERVICE-CONTROL-LINK-MIB", "cscLinkOperMode"))
if mibBuilder.loadTexts: ciscoServiceControlLinkModeChange.setStatus('current')
ciscoSCLinkMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 631, 2, 1))
ciscoSCLinkMIBObjectGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 631, 2, 2))
cServiceLinkMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 631, 2, 1, 1)).setObjects(("CISCO-SERVICE-CONTROL-LINK-MIB", "cSCLinkMIBObjectGroup"), ("CISCO-SERVICE-CONTROL-LINK-MIB", "cSCLinkMIBNotificationGroup"), ("CISCO-SERVICE-CONTROL-LINK-MIB", "cSCLinkNotifControlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cServiceLinkMIBCompliance = cServiceLinkMIBCompliance.setStatus('current')
cSCLinkMIBObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 631, 2, 2, 1)).setObjects(("CISCO-SERVICE-CONTROL-LINK-MIB", "cscLinkAdminModeOnActive"), ("CISCO-SERVICE-CONTROL-LINK-MIB", "cscLinkAdminModeOnFailure"), ("CISCO-SERVICE-CONTROL-LINK-MIB", "cscLinkOperMode"), ("CISCO-SERVICE-CONTROL-LINK-MIB", "cscLinkAdminReflectionEnable"), ("CISCO-SERVICE-CONTROL-LINK-MIB", "cscLinkSubscriberSidePortIndex"), ("CISCO-SERVICE-CONTROL-LINK-MIB", "cscLinkNetworkSidePortIndex"), ("CISCO-SERVICE-CONTROL-LINK-MIB", "cscLinkAdminReflectionState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSCLinkMIBObjectGroup = cSCLinkMIBObjectGroup.setStatus('current')
cSCLinkMIBNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 631, 2, 2, 2)).setObjects(("CISCO-SERVICE-CONTROL-LINK-MIB", "ciscoServiceControlLinkModeChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSCLinkMIBNotificationGroup = cSCLinkMIBNotificationGroup.setStatus('current')
cSCLinkNotifControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 631, 2, 2, 3)).setObjects(("CISCO-SERVICE-CONTROL-LINK-MIB", "cscLinkNotifsEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSCLinkNotifControlGroup = cSCLinkNotifControlGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-SERVICE-CONTROL-LINK-MIB", cscLinkAdminReflectionEnable=cscLinkAdminReflectionEnable, cscLinkOperMode=cscLinkOperMode, ciscoServiceControlLinkMIB=ciscoServiceControlLinkMIB, cscLinkSubscriberSidePortIndex=cscLinkSubscriberSidePortIndex, cscLinkNotifsEnabled=cscLinkNotifsEnabled, cscLinkNetworkSidePortIndex=cscLinkNetworkSidePortIndex, cSCLinkNotifControlGroup=cSCLinkNotifControlGroup, cscLinkAdminModeOnActive=cscLinkAdminModeOnActive, ciscoSCLinkMIBConform=ciscoSCLinkMIBConform, ciscoSCLinkMIBObjects=ciscoSCLinkMIBObjects, ciscoSCLinkMIBCompliances=ciscoSCLinkMIBCompliances, cServiceLinkMIBCompliance=cServiceLinkMIBCompliance, ciscoSCLinkMIBObjectGroups=ciscoSCLinkMIBObjectGroups, ciscoServiceControlLinkModeChange=ciscoServiceControlLinkModeChange, cSCLinkMIBNotificationGroup=cSCLinkMIBNotificationGroup, ciscoSCLinkMIBNotifs=ciscoSCLinkMIBNotifs, cscLinkStatusEntry=cscLinkStatusEntry, CsceLinkModeType=CsceLinkModeType, cscLinkAdminReflectionState=cscLinkAdminReflectionState, PYSNMP_MODULE_ID=ciscoServiceControlLinkMIB, cscLinkStatusTable=cscLinkStatusTable, cscLinkAdminModeOnFailure=cscLinkAdminModeOnFailure, cSCLinkMIBObjectGroup=cSCLinkMIBObjectGroup)
