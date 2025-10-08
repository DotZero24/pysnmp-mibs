#
# PySNMP MIB module LOOPBACK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/quanta/LOOPBACK-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:41:21 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InetAddressIPv4, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv4")
switch, = mibBuilder.importSymbols("QUANTA-SWITCH-MIB", "switch")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, TimeTicks, MibIdentifier, Integer32, Bits, mib_2, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "TimeTicks", "MibIdentifier", "Integer32", "Bits", "mib-2", "IpAddress")
DisplayString, RowStatus, PhysAddress, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "PhysAddress", "TruthValue", "TextualConvention")
loopback = ModuleIdentity((1, 3, 6, 1, 4, 1, 7244, 2, 22))
if mibBuilder.loadTexts: loopback.setLastUpdated('201108310000Z')
if mibBuilder.loadTexts: loopback.setOrganization('QCI')
agentLoopbackGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 7244, 2, 22, 1))
agentLoopbackTable = MibTable((1, 3, 6, 1, 4, 1, 7244, 2, 22, 1, 1), )
if mibBuilder.loadTexts: agentLoopbackTable.setStatus('current')
agentLoopbackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7244, 2, 22, 1, 1, 1), ).setIndexNames((0, "LOOPBACK-MIB", "agentLoopbackID"))
if mibBuilder.loadTexts: agentLoopbackEntry.setStatus('current')
agentLoopbackID = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 22, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: agentLoopbackID.setStatus('current')
agentLoopbackIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 22, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLoopbackIfIndex.setStatus('current')
agentLoopbackIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 22, 1, 1, 1, 3), InetAddressIPv4()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLoopbackIPAddress.setStatus('current')
agentLoopbackIPSubnet = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 22, 1, 1, 1, 4), InetAddressIPv4()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLoopbackIPSubnet.setStatus('current')
agentLoopbackStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 22, 1, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentLoopbackStatus.setStatus('current')
mibBuilder.exportSymbols("LOOPBACK-MIB", agentLoopbackIfIndex=agentLoopbackIfIndex, loopback=loopback, agentLoopbackStatus=agentLoopbackStatus, agentLoopbackID=agentLoopbackID, agentLoopbackIPSubnet=agentLoopbackIPSubnet, agentLoopbackTable=agentLoopbackTable, agentLoopbackIPAddress=agentLoopbackIPAddress, agentLoopbackEntry=agentLoopbackEntry, agentLoopbackGroup=agentLoopbackGroup, PYSNMP_MODULE_ID=loopback)
