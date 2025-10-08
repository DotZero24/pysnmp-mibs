#
# PySNMP MIB module FS-IP-MANAGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/fscom/FS-IP-MANAGE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:01:29 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
fsMgmt, = mibBuilder.importSymbols("FS-SMI", "fsMgmt")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("FS-IP-MANAGE-MIB", fsIpManageMIBConformance=fsIpManageMIBConformance, fsIpManageMIBCompliances=fsIpManageMIBCompliances, fsDhcpServerIp=fsDhcpServerIp, fsIpManageMIB=fsIpManageMIB, fsDhcpMIBObjects=fsDhcpMIBObjects, fsL2L3DhcpManageMIBGroup=fsL2L3DhcpManageMIBGroup, fsIpManageMIBCompliance=fsIpManageMIBCompliance, PYSNMP_MODULE_ID=fsIpManageMIB, fsIpManageMIBGroups=fsIpManageMIBGroups, fsIpMIBObjects=fsIpMIBObjects, fsDhcpRelayAgentGlobalStatus=fsDhcpRelayAgentGlobalStatus, fsIpDefaultGateWay=fsIpDefaultGateWay)
