#
# PySNMP MIB module RUCKUS-NDI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/brocade/RUCKUS-NDI-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:06:57 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
snSwitch, = mibBuilder.importSymbols("FOUNDRY-SN-SWITCH-GROUP-MIB", "snSwitch")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
Ipv6Address, = mibBuilder.importSymbols("IPV6-TC", "Ipv6Address")
VlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, RowStatus, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "RowStatus", "TruthValue", "TextualConvention")
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
mibBuilder.exportSymbols("RUCKUS-NDI-MIB", ruckusNdiStaticNDInspectMacAddr=ruckusNdiStaticNDInspectMacAddr, ruckusNdiNotify=ruckusNdiNotify, ruckusNdiVlan=ruckusNdiVlan, ruckusNdiVlanConfigEntry=ruckusNdiVlanConfigEntry, NDState=NDState, ruckusNdiVlanConfigVlanId=ruckusNdiVlanConfigVlanId, ruckusNdiNDInspect=ruckusNdiNDInspect, ruckusNdiConformance=ruckusNdiConformance, ruckusNdiVlanConfigTable=ruckusNdiVlanConfigTable, ruckusNdiIfConfigEntry=ruckusNdiIfConfigEntry, ruckusNdiIfTrustValue=ruckusNdiIfTrustValue, ruckusNdiStaticNDInspectType=ruckusNdiStaticNDInspectType, ruckusNdiStaticNDInspectState=ruckusNdiStaticNDInspectState, ruckusNdiStaticNDInspectRowStatus=ruckusNdiStaticNDInspectRowStatus, ruckusNdiStaticNDInspectPort=ruckusNdiStaticNDInspectPort, ruckusNdiObjects=ruckusNdiObjects, ruckusNdiVlanDynNDInspectionEnable=ruckusNdiVlanDynNDInspectionEnable, ruckusNdiMIB=ruckusNdiMIB, ruckusNdiCompliances=ruckusNdiCompliances, ruckusNdiStaticNDInspectAge=ruckusNdiStaticNDInspectAge, ruckusNdiStaticNDInspectEntry=ruckusNdiStaticNDInspectEntry, ruckusNdiInterface=ruckusNdiInterface, ruckusNdiCompliance=ruckusNdiCompliance, NDType=NDType, ruckusNdInspectIfConfigTable=ruckusNdInspectIfConfigTable, PYSNMP_MODULE_ID=ruckusNdiMIB, ruckusNdiStaticNDInspectTable=ruckusNdiStaticNDInspectTable, ruckusNdiStaticNDInspectIpv6Addr=ruckusNdiStaticNDInspectIpv6Addr)
