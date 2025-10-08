#
# PySNMP MIB module DES7200-IP-MANAGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/DES7200-IP-MANAGE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:00:31 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
myMgmt, = mibBuilder.importSymbols("DES7200-SMI", "myMgmt")
MemberMap, ConfigStatus = mibBuilder.importSymbols("DES7200-TC", "MemberMap", "ConfigStatus")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, MacAddress, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "MacAddress", "TruthValue", "DisplayString")
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
mibBuilder.exportSymbols("DES7200-IP-MANAGE-MIB", myIpManageMIBGroups=myIpManageMIBGroups, myDhcpMIBObjects=myDhcpMIBObjects, myIpManageMIBConformance=myIpManageMIBConformance, myIpManageMIBCompliances=myIpManageMIBCompliances, myIpDefaultGateWay=myIpDefaultGateWay, myDhcpServerIp=myDhcpServerIp, myIpMIBObjects=myIpMIBObjects, PYSNMP_MODULE_ID=myIpManageMIB, myIpManageMIBCompliance=myIpManageMIBCompliance, myL2L3DhcpManageMIBGroup=myL2L3DhcpManageMIBGroup, myIpManageMIB=myIpManageMIB, myDhcpRelayAgentGlobalStatus=myDhcpRelayAgentGlobalStatus)
