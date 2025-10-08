#
# PySNMP MIB module TPLINK-ETHERNETOAMRMTLBCFG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/tplink/TPLINK-ETHERNETOAMRMTLBCFG-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:01:36 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ethernetOamRmtLbConfig, = mibBuilder.importSymbols("TPLINK-ETHERNETOAM-MIB", "ethernetOamRmtLbConfig")
ethernetOamRmtLbCfgTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 4, 1), )
if mibBuilder.loadTexts: ethernetOamRmtLbCfgTable.setStatus('current')
ethernetOamRmtLbCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 4, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ethernetOamRmtLbCfgEntry.setStatus('current')
ethernetOamRmtLbCfgPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 4, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamRmtLbCfgPort.setStatus('current')
ethernetOamRmtLbCfgReceivedRemoteLoopback = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("ignore", 0), ("process", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethernetOamRmtLbCfgReceivedRemoteLoopback.setStatus('current')
ethernetOamRmtLbCfgRemoteLoopback = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("stop", 0), ("start", 1), ("unchanged", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethernetOamRmtLbCfgRemoteLoopback.setStatus('current')
ethernetOamRmtLbCfgLAG = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 4, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamRmtLbCfgLAG.setStatus('current')
mibBuilder.exportSymbols("TPLINK-ETHERNETOAMRMTLBCFG-MIB", ethernetOamRmtLbCfgPort=ethernetOamRmtLbCfgPort, ethernetOamRmtLbCfgRemoteLoopback=ethernetOamRmtLbCfgRemoteLoopback, ethernetOamRmtLbCfgEntry=ethernetOamRmtLbCfgEntry, ethernetOamRmtLbCfgReceivedRemoteLoopback=ethernetOamRmtLbCfgReceivedRemoteLoopback, ethernetOamRmtLbCfgTable=ethernetOamRmtLbCfgTable, ethernetOamRmtLbCfgLAG=ethernetOamRmtLbCfgLAG)
