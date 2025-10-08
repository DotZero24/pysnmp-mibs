#
# PySNMP MIB module PDN-IP-MULTICAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/paradyne/PDN-IP-MULTICAST-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:42 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
pdn_common, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdn-common")
SwitchState, = mibBuilder.importSymbols("PDN-TC", "SwitchState")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pdnIpMcastMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48))
pdnIpMcastMIB.setRevisions(('2003-05-01 00:00',))
if mibBuilder.loadTexts: pdnIpMcastMIB.setLastUpdated('200305010000Z')
if mibBuilder.loadTexts: pdnIpMcastMIB.setOrganization('Paradyne Networks MIB Working Group Other information about group editing the MIB.')
pdnIpMcastNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 0))
pdnIpMcastObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 1))
pdnIpMcastAFNs = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 2))
pdnIpMcastConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 3))
pdnIgmpProxy = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 1, 1))
pdnIpMcastStats = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 1, 2))
pdnIgmpProxyEnableDisable = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 1, 1, 1), SwitchState().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnIgmpProxyEnableDisable.setStatus('current')
pdnIgmpProxyReportSummaryEnableDisable = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 1, 1, 2), SwitchState().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnIgmpProxyReportSummaryEnableDisable.setStatus('current')
pdnIpMcastCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 3, 1))
pdnIpMcastGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 3, 2))
pdnIpMcastMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 3, 1, 1)).setObjects(("PDN-IP-MULTICAST-MIB", "pdnIgmpProxyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnIpMcastMIBCompliance = pdnIpMcastMIBCompliance.setStatus('current')
pdnIpMcaseObjGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 3, 2, 1))
pdnIpMcastAfnGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 3, 2, 2))
pdnIpMcaseNtfyGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 3, 2, 3))
pdnIgmpProxyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 3, 2, 1, 1)).setObjects(("PDN-IP-MULTICAST-MIB", "pdnIgmpProxyEnableDisable"), ("PDN-IP-MULTICAST-MIB", "pdnIgmpProxyReportSummaryEnableDisable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnIgmpProxyGroup = pdnIgmpProxyGroup.setStatus('current')
mibBuilder.exportSymbols("PDN-IP-MULTICAST-MIB", pdnIpMcastCompliances=pdnIpMcastCompliances, pdnIpMcaseNtfyGroups=pdnIpMcaseNtfyGroups, pdnIpMcastGroups=pdnIpMcastGroups, pdnIgmpProxyEnableDisable=pdnIgmpProxyEnableDisable, pdnIpMcastNotifications=pdnIpMcastNotifications, pdnIgmpProxy=pdnIgmpProxy, PYSNMP_MODULE_ID=pdnIpMcastMIB, pdnIpMcastStats=pdnIpMcastStats, pdnIpMcastAfnGroups=pdnIpMcastAfnGroups, pdnIpMcastMIB=pdnIpMcastMIB, pdnIpMcastMIBCompliance=pdnIpMcastMIBCompliance, pdnIgmpProxyGroup=pdnIgmpProxyGroup, pdnIpMcaseObjGroups=pdnIpMcaseObjGroups, pdnIgmpProxyReportSummaryEnableDisable=pdnIgmpProxyReportSummaryEnableDisable, pdnIpMcastAFNs=pdnIpMcastAFNs, pdnIpMcastObjects=pdnIpMcastObjects, pdnIpMcastConformance=pdnIpMcastConformance)
