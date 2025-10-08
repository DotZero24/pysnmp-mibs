#
# PySNMP MIB module QTECH-IP-MANAGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/qtech/QTECH-IP-MANAGE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:14:44 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
qtechMgmt, = mibBuilder.importSymbols("QTECH-SMI", "qtechMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
qtechIpManageMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 12))
qtechIpManageMIB.setRevisions(('2002-03-20 00:00',))
if mibBuilder.loadTexts: qtechIpManageMIB.setLastUpdated('200203200000Z')
if mibBuilder.loadTexts: qtechIpManageMIB.setOrganization('Qtech Networks Co.,Ltd.')
qtechDhcpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 12, 1))
qtechIpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 12, 2))
qtechDhcpRelayAgentGlobalStatus = MibScalar((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 12, 1, 2), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qtechDhcpRelayAgentGlobalStatus.setStatus('current')
qtechDhcpServerIp = MibScalar((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 12, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qtechDhcpServerIp.setStatus('current')
qtechIpDefaultGateWay = MibScalar((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 12, 2, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qtechIpDefaultGateWay.setStatus('current')
qtechIpManageMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 12, 3))
qtechIpManageMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 12, 3, 1))
qtechIpManageMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 12, 3, 2))
qtechIpManageMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 12, 3, 1, 1)).setObjects(("QTECH-IP-MANAGE-MIB", "qtechL2L3DhcpManageMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qtechIpManageMIBCompliance = qtechIpManageMIBCompliance.setStatus('current')
qtechL2L3DhcpManageMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 12, 3, 2, 1)).setObjects(("QTECH-IP-MANAGE-MIB", "qtechDhcpRelayAgentGlobalStatus"), ("QTECH-IP-MANAGE-MIB", "qtechDhcpServerIp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qtechL2L3DhcpManageMIBGroup = qtechL2L3DhcpManageMIBGroup.setStatus('current')
mibBuilder.exportSymbols("QTECH-IP-MANAGE-MIB", qtechIpManageMIB=qtechIpManageMIB, qtechIpManageMIBCompliance=qtechIpManageMIBCompliance, qtechIpMIBObjects=qtechIpMIBObjects, PYSNMP_MODULE_ID=qtechIpManageMIB, qtechIpManageMIBCompliances=qtechIpManageMIBCompliances, qtechL2L3DhcpManageMIBGroup=qtechL2L3DhcpManageMIBGroup, qtechIpManageMIBGroups=qtechIpManageMIBGroups, qtechDhcpServerIp=qtechDhcpServerIp, qtechDhcpMIBObjects=qtechDhcpMIBObjects, qtechIpManageMIBConformance=qtechIpManageMIBConformance, qtechDhcpRelayAgentGlobalStatus=qtechDhcpRelayAgentGlobalStatus, qtechIpDefaultGateWay=qtechIpDefaultGateWay)
