#
# PySNMP MIB module PDN-IP-MULTICAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/paradyne/PDN-IP-MULTICAST-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:57:22 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
pdn_common, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdn-common")
SwitchState, = mibBuilder.importSymbols("PDN-TC", "SwitchState")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("PDN-IP-MULTICAST-MIB", pdnIpMcastCompliances=pdnIpMcastCompliances, pdnIpMcastStats=pdnIpMcastStats, pdnIpMcastAFNs=pdnIpMcastAFNs, pdnIgmpProxy=pdnIgmpProxy, pdnIpMcastMIB=pdnIpMcastMIB, pdnIgmpProxyEnableDisable=pdnIgmpProxyEnableDisable, pdnIgmpProxyReportSummaryEnableDisable=pdnIgmpProxyReportSummaryEnableDisable, pdnIpMcastMIBCompliance=pdnIpMcastMIBCompliance, pdnIpMcaseObjGroups=pdnIpMcaseObjGroups, pdnIpMcastAfnGroups=pdnIpMcastAfnGroups, pdnIgmpProxyGroup=pdnIgmpProxyGroup, pdnIpMcaseNtfyGroups=pdnIpMcaseNtfyGroups, pdnIpMcastConformance=pdnIpMcastConformance, pdnIpMcastObjects=pdnIpMcastObjects, pdnIpMcastGroups=pdnIpMcastGroups, pdnIpMcastNotifications=pdnIpMcastNotifications, PYSNMP_MODULE_ID=pdnIpMcastMIB)
