#
# PySNMP MIB module FS-IP-MANAGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/fscom/FS-IP-MANAGE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:58:38 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
fsMgmt, = mibBuilder.importSymbols("FS-SMI", "fsMgmt")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fsIpManageMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 12))
fsIpManageMIB.setRevisions(('2002-03-20 00:00',))
if mibBuilder.loadTexts: fsIpManageMIB.setLastUpdated('200203200000Z')
if mibBuilder.loadTexts: fsIpManageMIB.setOrganization('FS.COM Inc..')
fsDhcpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 12, 1))
fsIpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 12, 2))
fsDhcpRelayAgentGlobalStatus = MibScalar((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 12, 1, 2), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsDhcpRelayAgentGlobalStatus.setStatus('current')
fsDhcpServerIp = MibScalar((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 12, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsDhcpServerIp.setStatus('current')
fsIpDefaultGateWay = MibScalar((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 12, 2, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsIpDefaultGateWay.setStatus('current')
fsIpManageMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 12, 3))
fsIpManageMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 12, 3, 1))
fsIpManageMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 12, 3, 2))
fsIpManageMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 12, 3, 1, 1)).setObjects(("FS-IP-MANAGE-MIB", "fsL2L3DhcpManageMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fsIpManageMIBCompliance = fsIpManageMIBCompliance.setStatus('current')
fsL2L3DhcpManageMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 12, 3, 2, 1)).setObjects(("FS-IP-MANAGE-MIB", "fsDhcpRelayAgentGlobalStatus"), ("FS-IP-MANAGE-MIB", "fsDhcpServerIp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fsL2L3DhcpManageMIBGroup = fsL2L3DhcpManageMIBGroup.setStatus('current')
mibBuilder.exportSymbols("FS-IP-MANAGE-MIB", fsDhcpMIBObjects=fsDhcpMIBObjects, fsIpDefaultGateWay=fsIpDefaultGateWay, fsIpManageMIBCompliance=fsIpManageMIBCompliance, fsL2L3DhcpManageMIBGroup=fsL2L3DhcpManageMIBGroup, fsIpMIBObjects=fsIpMIBObjects, fsIpManageMIBCompliances=fsIpManageMIBCompliances, fsDhcpRelayAgentGlobalStatus=fsDhcpRelayAgentGlobalStatus, fsIpManageMIBGroups=fsIpManageMIBGroups, fsIpManageMIBConformance=fsIpManageMIBConformance, fsDhcpServerIp=fsDhcpServerIp, fsIpManageMIB=fsIpManageMIB, PYSNMP_MODULE_ID=fsIpManageMIB)
