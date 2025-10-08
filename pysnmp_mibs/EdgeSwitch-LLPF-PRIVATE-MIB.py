#
# PySNMP MIB module EdgeSwitch-LLPF-PRIVATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/ubiquiti/EdgeSwitch-LLPF-PRIVATE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:57:02 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
fastPath, = mibBuilder.importSymbols("EdgeSwitch-REF-MIB", "fastPath")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
MacAddress, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "RowStatus", "DisplayString", "TextualConvention")
fastPathLlpf = ModuleIdentity((1, 3, 6, 1, 4, 1, 4413, 1, 1, 48))
fastPathLlpf.setRevisions(('2011-01-26 00:00', '2009-10-26 00:00',))
if mibBuilder.loadTexts: fastPathLlpf.setLastUpdated('201101260000Z')
if mibBuilder.loadTexts: fastPathLlpf.setOrganization('Broadcom Inc')
agentSwitchLlpfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 48, 1))
agentSwitchLlpfPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4413, 1, 1, 48, 1, 1), )
if mibBuilder.loadTexts: agentSwitchLlpfPortConfigTable.setStatus('current')
agentSwitchLlpfPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4413, 1, 1, 48, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "EdgeSwitch-LLPF-PRIVATE-MIB", "agentSwitchLlpfProtocolType"))
if mibBuilder.loadTexts: agentSwitchLlpfPortConfigEntry.setStatus('current')
agentSwitchLlpfProtocolType = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 48, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 6)))
if mibBuilder.loadTexts: agentSwitchLlpfProtocolType.setStatus('current')
agentSwitchLlpfPortBlockMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 48, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSwitchLlpfPortBlockMode.setStatus('current')
mibBuilder.exportSymbols("EdgeSwitch-LLPF-PRIVATE-MIB", agentSwitchLlpfGroup=agentSwitchLlpfGroup, fastPathLlpf=fastPathLlpf, PYSNMP_MODULE_ID=fastPathLlpf, agentSwitchLlpfPortConfigTable=agentSwitchLlpfPortConfigTable, agentSwitchLlpfPortBlockMode=agentSwitchLlpfPortBlockMode, agentSwitchLlpfPortConfigEntry=agentSwitchLlpfPortConfigEntry, agentSwitchLlpfProtocolType=agentSwitchLlpfProtocolType)
