#
# PySNMP MIB module DES7200-IP-MANAGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/DES7200-IP-MANAGE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:35:24 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
myMgmt, = mibBuilder.importSymbols("DES7200-SMI", "myMgmt")
MemberMap, ConfigStatus = mibBuilder.importSymbols("DES7200-TC", "MemberMap", "ConfigStatus")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, iso, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "iso", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, RowStatus, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "RowStatus", "TruthValue", "TextualConvention")
myIpManageMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 12))
myIpManageMIB.setRevisions(('2002-03-20 00:00',))
if mibBuilder.loadTexts: myIpManageMIB.setLastUpdated('200203200000Z')
if mibBuilder.loadTexts: myIpManageMIB.setOrganization('$Company$')
myDhcpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 12, 1))
myIpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 12, 2))
myDhcpRelayAgentGlobalStatus = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 12, 1, 2), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myDhcpRelayAgentGlobalStatus.setStatus('current')
myDhcpServerIp = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 12, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myDhcpServerIp.setStatus('current')
myIpDefaultGateWay = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 12, 2, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myIpDefaultGateWay.setStatus('current')
myIpManageMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 12, 3))
myIpManageMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 12, 3, 1))
myIpManageMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 12, 3, 2))
myIpManageMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 12, 3, 1, 1)).setObjects(("DES7200-IP-MANAGE-MIB", "myL2L3DhcpManageMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    myIpManageMIBCompliance = myIpManageMIBCompliance.setStatus('current')
myL2L3DhcpManageMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 12, 3, 2, 1)).setObjects(("DES7200-IP-MANAGE-MIB", "myDhcpRelayAgentGlobalStatus"), ("DES7200-IP-MANAGE-MIB", "myDhcpServerIp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    myL2L3DhcpManageMIBGroup = myL2L3DhcpManageMIBGroup.setStatus('current')
mibBuilder.exportSymbols("DES7200-IP-MANAGE-MIB", myIpManageMIBConformance=myIpManageMIBConformance, myL2L3DhcpManageMIBGroup=myL2L3DhcpManageMIBGroup, myDhcpServerIp=myDhcpServerIp, myDhcpMIBObjects=myDhcpMIBObjects, myIpDefaultGateWay=myIpDefaultGateWay, myIpManageMIBCompliance=myIpManageMIBCompliance, myIpMIBObjects=myIpMIBObjects, myDhcpRelayAgentGlobalStatus=myDhcpRelayAgentGlobalStatus, myIpManageMIBGroups=myIpManageMIBGroups, myIpManageMIBCompliances=myIpManageMIBCompliances, myIpManageMIB=myIpManageMIB, PYSNMP_MODULE_ID=myIpManageMIB)
