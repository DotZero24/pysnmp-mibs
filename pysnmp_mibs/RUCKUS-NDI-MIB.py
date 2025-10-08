#
# PySNMP MIB module RUCKUS-NDI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/brocade/RUCKUS-NDI-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:15:25 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
snSwitch, = mibBuilder.importSymbols("FOUNDRY-SN-SWITCH-GROUP-MIB", "snSwitch")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
Ipv6Address, = mibBuilder.importSymbols("IPV6-TC", "Ipv6Address")
VlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, MacAddress, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "MacAddress", "TruthValue", "DisplayString")
ruckusNdiMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47))
if mibBuilder.loadTexts: ruckusNdiMIB.setLastUpdated('202006110000Z')
if mibBuilder.loadTexts: ruckusNdiMIB.setOrganization('Ruckus Wireless, Inc.')
class NDType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("other", 1), ("static", 2), ("dynamic", 3), ("inspect", 4), ("dhcpv6", 5), ("dynamicDhcpv6", 6), ("staticDhcpv6", 7), ("host", 8))

class NDState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("other", 1), ("valid", 2), ("pend", 3))

ruckusNdiNotify = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 0))
ruckusNdiObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 1))
ruckusNdiConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 2))
ruckusNdiVlan = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 1, 1))
ruckusNdiInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 1, 2))
ruckusNdiNDInspect = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 1, 3))
ruckusNdiVlanConfigTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 1, 1, 1), )
if mibBuilder.loadTexts: ruckusNdiVlanConfigTable.setStatus('current')
ruckusNdiVlanConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 1, 1, 1, 1), ).setIndexNames((0, "RUCKUS-NDI-MIB", "ruckusNdiVlanConfigVlanId"))
if mibBuilder.loadTexts: ruckusNdiVlanConfigEntry.setStatus('current')
ruckusNdiVlanConfigVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 1, 1, 1, 1, 1), VlanIndex())
if mibBuilder.loadTexts: ruckusNdiVlanConfigVlanId.setStatus('current')
ruckusNdiVlanDynNDInspectionEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 1, 1, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusNdiVlanDynNDInspectionEnable.setStatus('current')
ruckusNdInspectIfConfigTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 1, 2, 1), )
if mibBuilder.loadTexts: ruckusNdInspectIfConfigTable.setStatus('current')
ruckusNdiIfConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ruckusNdiIfConfigEntry.setStatus('current')
ruckusNdiIfTrustValue = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 1, 2, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusNdiIfTrustValue.setStatus('current')
ruckusNdiStaticNDInspectTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 1, 3, 1), )
if mibBuilder.loadTexts: ruckusNdiStaticNDInspectTable.setStatus('current')
ruckusNdiStaticNDInspectEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 1, 3, 1, 1), ).setIndexNames((0, "RUCKUS-NDI-MIB", "ruckusNdiStaticNDInspectIpv6Addr"))
if mibBuilder.loadTexts: ruckusNdiStaticNDInspectEntry.setStatus('current')
ruckusNdiStaticNDInspectIpv6Addr = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 1, 3, 1, 1, 1), Ipv6Address())
if mibBuilder.loadTexts: ruckusNdiStaticNDInspectIpv6Addr.setStatus('current')
ruckusNdiStaticNDInspectMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 1, 3, 1, 1, 2), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ruckusNdiStaticNDInspectMacAddr.setStatus('current')
ruckusNdiStaticNDInspectType = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 1, 3, 1, 1, 3), NDType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusNdiStaticNDInspectType.setStatus('current')
ruckusNdiStaticNDInspectState = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 1, 3, 1, 1, 4), NDState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusNdiStaticNDInspectState.setStatus('current')
ruckusNdiStaticNDInspectAge = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 1, 3, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusNdiStaticNDInspectAge.setStatus('current')
ruckusNdiStaticNDInspectPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 1, 3, 1, 1, 6), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusNdiStaticNDInspectPort.setStatus('current')
ruckusNdiStaticNDInspectRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 1, 3, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ruckusNdiStaticNDInspectRowStatus.setStatus('current')
ruckusNdiCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 2, 1))
ruckusNdiCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 2, 1, 1)).setObjects()

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruckusNdiCompliance = ruckusNdiCompliance.setStatus('current')
mibBuilder.exportSymbols("RUCKUS-NDI-MIB", ruckusNdiStaticNDInspectType=ruckusNdiStaticNDInspectType, ruckusNdiNDInspect=ruckusNdiNDInspect, ruckusNdiStaticNDInspectTable=ruckusNdiStaticNDInspectTable, ruckusNdiVlan=ruckusNdiVlan, ruckusNdiStaticNDInspectState=ruckusNdiStaticNDInspectState, ruckusNdiCompliances=ruckusNdiCompliances, ruckusNdiVlanConfigTable=ruckusNdiVlanConfigTable, ruckusNdiMIB=ruckusNdiMIB, ruckusNdiInterface=ruckusNdiInterface, ruckusNdiIfConfigEntry=ruckusNdiIfConfigEntry, PYSNMP_MODULE_ID=ruckusNdiMIB, ruckusNdiObjects=ruckusNdiObjects, ruckusNdiConformance=ruckusNdiConformance, ruckusNdiStaticNDInspectAge=ruckusNdiStaticNDInspectAge, ruckusNdiStaticNDInspectIpv6Addr=ruckusNdiStaticNDInspectIpv6Addr, ruckusNdiStaticNDInspectRowStatus=ruckusNdiStaticNDInspectRowStatus, ruckusNdiVlanDynNDInspectionEnable=ruckusNdiVlanDynNDInspectionEnable, ruckusNdInspectIfConfigTable=ruckusNdInspectIfConfigTable, ruckusNdiStaticNDInspectMacAddr=ruckusNdiStaticNDInspectMacAddr, NDState=NDState, NDType=NDType, ruckusNdiStaticNDInspectPort=ruckusNdiStaticNDInspectPort, ruckusNdiVlanConfigVlanId=ruckusNdiVlanConfigVlanId, ruckusNdiIfTrustValue=ruckusNdiIfTrustValue, ruckusNdiVlanConfigEntry=ruckusNdiVlanConfigEntry, ruckusNdiStaticNDInspectEntry=ruckusNdiStaticNDInspectEntry, ruckusNdiNotify=ruckusNdiNotify, ruckusNdiCompliance=ruckusNdiCompliance)
