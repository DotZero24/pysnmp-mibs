#
# PySNMP MIB module QTECH-IP-MANAGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/qtech/QTECH-IP-MANAGE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:06:35 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
qtechMgmt, = mibBuilder.importSymbols("QTECH-SMI", "qtechMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("QTECH-IP-MANAGE-MIB", qtechIpManageMIBConformance=qtechIpManageMIBConformance, qtechIpMIBObjects=qtechIpMIBObjects, qtechIpManageMIBGroups=qtechIpManageMIBGroups, qtechDhcpServerIp=qtechDhcpServerIp, qtechDhcpRelayAgentGlobalStatus=qtechDhcpRelayAgentGlobalStatus, PYSNMP_MODULE_ID=qtechIpManageMIB, qtechIpManageMIBCompliance=qtechIpManageMIBCompliance, qtechIpDefaultGateWay=qtechIpDefaultGateWay, qtechIpManageMIB=qtechIpManageMIB, qtechL2L3DhcpManageMIBGroup=qtechL2L3DhcpManageMIBGroup, qtechDhcpMIBObjects=qtechDhcpMIBObjects, qtechIpManageMIBCompliances=qtechIpManageMIBCompliances)
