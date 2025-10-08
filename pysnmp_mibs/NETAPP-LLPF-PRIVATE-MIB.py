#
# PySNMP MIB module NETAPP-LLPF-PRIVATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/netapp/NETAPP-LLPF-PRIVATE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:57:33 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
fastPath, = mibBuilder.importSymbols("NETAPP-REF-MIB", "fastPath")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "RowStatus", "TextualConvention")
fastPathLlpf = ModuleIdentity((1, 3, 6, 1, 4, 1, 789, 4413, 1, 1, 48))
fastPathLlpf.setRevisions(('2011-01-26 00:00', '2009-10-26 00:00',))
if mibBuilder.loadTexts: fastPathLlpf.setLastUpdated('201101260000Z')
if mibBuilder.loadTexts: fastPathLlpf.setOrganization('Broadcom Corporation')
agentSwitchLlpfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 789, 4413, 1, 1, 48, 1))
agentSwitchLlpfPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 789, 4413, 1, 1, 48, 1, 1), )
if mibBuilder.loadTexts: agentSwitchLlpfPortConfigTable.setStatus('current')
agentSwitchLlpfPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 789, 4413, 1, 1, 48, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "NETAPP-LLPF-PRIVATE-MIB", "agentSwitchLlpfProtocolType"))
if mibBuilder.loadTexts: agentSwitchLlpfPortConfigEntry.setStatus('current')
agentSwitchLlpfProtocolType = MibTableColumn((1, 3, 6, 1, 4, 1, 789, 4413, 1, 1, 48, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 6)))
if mibBuilder.loadTexts: agentSwitchLlpfProtocolType.setStatus('current')
agentSwitchLlpfPortBlockMode = MibTableColumn((1, 3, 6, 1, 4, 1, 789, 4413, 1, 1, 48, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSwitchLlpfPortBlockMode.setStatus('current')
mibBuilder.exportSymbols("NETAPP-LLPF-PRIVATE-MIB", fastPathLlpf=fastPathLlpf, agentSwitchLlpfPortConfigTable=agentSwitchLlpfPortConfigTable, agentSwitchLlpfPortConfigEntry=agentSwitchLlpfPortConfigEntry, agentSwitchLlpfGroup=agentSwitchLlpfGroup, PYSNMP_MODULE_ID=fastPathLlpf, agentSwitchLlpfProtocolType=agentSwitchLlpfProtocolType, agentSwitchLlpfPortBlockMode=agentSwitchLlpfPortBlockMode)
