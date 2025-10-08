#
# PySNMP MIB module CISCO-IETF-PPVPN-MPLS-VPN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-IETF-PPVPN-MPLS-VPN-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:15:23 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
mplsVpnVrfPerfCurrNumRoutes, mplsVpnVrfConfHighRouteThreshold = mibBuilder.importSymbols("MPLS-VPN-MIB", "mplsVpnVrfPerfCurrNumRoutes", "mplsVpnVrfConfHighRouteThreshold")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMplsVpnMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 999))
ciscoMplsVpnMIB.setRevisions(('2003-04-17 12:00',))
if mibBuilder.loadTexts: ciscoMplsVpnMIB.setLastUpdated('200304171200Z')
if mibBuilder.loadTexts: ciscoMplsVpnMIB.setOrganization('Cisco Systems, Inc.')
cMplsVpnNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 999, 0))
cMplsVpnObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 999, 1))
cMplsVpnConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 999, 2))
cMplsNumVrfRouteMaxThreshCleared = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 999, 0, 1)).setObjects(("MPLS-VPN-MIB", "mplsVpnVrfPerfCurrNumRoutes"), ("MPLS-VPN-MIB", "mplsVpnVrfConfHighRouteThreshold"))
if mibBuilder.loadTexts: cMplsNumVrfRouteMaxThreshCleared.setStatus('current')
cMplsVpnCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 1))
cMplsVpnGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 2))
cMplsVpnCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 1, 1)).setObjects(("CISCO-IETF-PPVPN-MPLS-VPN-MIB", "cMplsVpnNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cMplsVpnCompliance = cMplsVpnCompliance.setStatus('current')
cMplsVpnNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 2, 1)).setObjects(("CISCO-IETF-PPVPN-MPLS-VPN-MIB", "cMplsNumVrfRouteMaxThreshCleared"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cMplsVpnNotificationGroup = cMplsVpnNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-IETF-PPVPN-MPLS-VPN-MIB", cMplsVpnNotificationGroup=cMplsVpnNotificationGroup, ciscoMplsVpnMIB=ciscoMplsVpnMIB, PYSNMP_MODULE_ID=ciscoMplsVpnMIB, cMplsVpnGroups=cMplsVpnGroups, cMplsVpnCompliance=cMplsVpnCompliance, cMplsVpnNotifs=cMplsVpnNotifs, cMplsVpnConform=cMplsVpnConform, cMplsNumVrfRouteMaxThreshCleared=cMplsNumVrfRouteMaxThreshCleared, cMplsVpnCompliances=cMplsVpnCompliances, cMplsVpnObjects=cMplsVpnObjects)
