#
# PySNMP MIB module FOUNDRY-IP-SOURCE-GUARD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/brocade/FOUNDRY-IP-SOURCE-GUARD-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:15:40 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
snSwitch, = mibBuilder.importSymbols("FOUNDRY-SN-SWITCH-GROUP-MIB", "snSwitch")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
VlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "DisplayString", "TextualConvention")
fdryIpSrcGuardMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37))
fdryIpSrcGuardMIB.setRevisions(('2010-07-26 00:00', '2010-02-22 00:00',))
if mibBuilder.loadTexts: fdryIpSrcGuardMIB.setLastUpdated('201007260000Z')
if mibBuilder.loadTexts: fdryIpSrcGuardMIB.setOrganization('Brocade Communications Systems, Inc.')
class BindMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("other", 1), ("active", 2), ("inactive", 3))

class BindType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("other", 1), ("ip", 2))

fdryIpSrcGuardInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 1))
fdryIpSrcGuardPortVlan = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 2))
fdryIpSrcGuardBind = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 3))
fdryIpSrcGuardIfConfigTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 1, 1), )
if mibBuilder.loadTexts: fdryIpSrcGuardIfConfigTable.setStatus('current')
fdryIpSrcGuardIfConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: fdryIpSrcGuardIfConfigEntry.setStatus('current')
fdryIpSrcGuardIfEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 1, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fdryIpSrcGuardIfEnable.setStatus('current')
fdryIpSrcGuardPortVlanConfigTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 2, 1), )
if mibBuilder.loadTexts: fdryIpSrcGuardPortVlanConfigTable.setStatus('current')
fdryIpSrcGuardPortVlanConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 2, 1, 1), ).setIndexNames((0, "FOUNDRY-IP-SOURCE-GUARD-MIB", "fdryIpSrcGuardPortVlanPortId"), (0, "FOUNDRY-IP-SOURCE-GUARD-MIB", "fdryIpSrcGuardPortVlanVlanId"))
if mibBuilder.loadTexts: fdryIpSrcGuardPortVlanConfigEntry.setStatus('current')
fdryIpSrcGuardPortVlanPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 2, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: fdryIpSrcGuardPortVlanPortId.setStatus('current')
fdryIpSrcGuardPortVlanVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 2, 1, 1, 2), VlanIndex())
if mibBuilder.loadTexts: fdryIpSrcGuardPortVlanVlanId.setStatus('current')
fdryIpSrcGuardPortVlanEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 2, 1, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fdryIpSrcGuardPortVlanEnable.setStatus('current')
fdryIpSrcGuardBindTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 3, 1), )
if mibBuilder.loadTexts: fdryIpSrcGuardBindTable.setStatus('current')
fdryIpSrcGuardBindEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "FOUNDRY-IP-SOURCE-GUARD-MIB", "fdryIpSrcGuardBindIpAddr"))
if mibBuilder.loadTexts: fdryIpSrcGuardBindEntry.setStatus('current')
fdryIpSrcGuardBindIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 3, 1, 1, 1), IpAddress())
if mibBuilder.loadTexts: fdryIpSrcGuardBindIpAddr.setStatus('current')
fdryIpSrcGuardBindVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 3, 1, 1, 2), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryIpSrcGuardBindVlanId.setStatus('current')
fdryIpSrcGuardBindRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 3, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryIpSrcGuardBindRowStatus.setStatus('current')
fdryIpSrcGuardBindMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 3, 1, 1, 4), BindMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdryIpSrcGuardBindMode.setStatus('current')
fdryIpSrcGuardBindType = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 3, 1, 1, 5), BindType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdryIpSrcGuardBindType.setStatus('current')
mibBuilder.exportSymbols("FOUNDRY-IP-SOURCE-GUARD-MIB", fdryIpSrcGuardPortVlan=fdryIpSrcGuardPortVlan, fdryIpSrcGuardMIB=fdryIpSrcGuardMIB, fdryIpSrcGuardInterface=fdryIpSrcGuardInterface, fdryIpSrcGuardBindType=fdryIpSrcGuardBindType, fdryIpSrcGuardBind=fdryIpSrcGuardBind, fdryIpSrcGuardBindMode=fdryIpSrcGuardBindMode, PYSNMP_MODULE_ID=fdryIpSrcGuardMIB, fdryIpSrcGuardBindVlanId=fdryIpSrcGuardBindVlanId, fdryIpSrcGuardBindTable=fdryIpSrcGuardBindTable, BindType=BindType, fdryIpSrcGuardBindRowStatus=fdryIpSrcGuardBindRowStatus, fdryIpSrcGuardPortVlanConfigTable=fdryIpSrcGuardPortVlanConfigTable, fdryIpSrcGuardPortVlanVlanId=fdryIpSrcGuardPortVlanVlanId, fdryIpSrcGuardIfEnable=fdryIpSrcGuardIfEnable, fdryIpSrcGuardPortVlanEnable=fdryIpSrcGuardPortVlanEnable, fdryIpSrcGuardIfConfigEntry=fdryIpSrcGuardIfConfigEntry, fdryIpSrcGuardPortVlanPortId=fdryIpSrcGuardPortVlanPortId, fdryIpSrcGuardIfConfigTable=fdryIpSrcGuardIfConfigTable, fdryIpSrcGuardBindEntry=fdryIpSrcGuardBindEntry, fdryIpSrcGuardPortVlanConfigEntry=fdryIpSrcGuardPortVlanConfigEntry, BindMode=BindMode, fdryIpSrcGuardBindIpAddr=fdryIpSrcGuardBindIpAddr)
