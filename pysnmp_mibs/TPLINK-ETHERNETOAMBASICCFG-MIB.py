#
# PySNMP MIB module TPLINK-ETHERNETOAMBASICCFG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/tplink/TPLINK-ETHERNETOAMBASICCFG-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:01:56 2025
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
ethernetOamBasicConfig, = mibBuilder.importSymbols("TPLINK-ETHERNETOAM-MIB", "ethernetOamBasicConfig")
ethernetOamBasicCfgTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 1, 1), )
if mibBuilder.loadTexts: ethernetOamBasicCfgTable.setStatus('current')
ethernetOamBasicCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ethernetOamBasicCfgEntry.setStatus('current')
ethernetOamBasicCfgPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamBasicCfgPort.setStatus('current')
ethernetOamBasicCfgMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("passive", 0), ("active", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethernetOamBasicCfgMode.setStatus('current')
ethernetOamBasicCfgState = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethernetOamBasicCfgState.setStatus('current')
ethernetOamBasicCfgLAG = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamBasicCfgLAG.setStatus('current')
mibBuilder.exportSymbols("TPLINK-ETHERNETOAMBASICCFG-MIB", ethernetOamBasicCfgTable=ethernetOamBasicCfgTable, ethernetOamBasicCfgMode=ethernetOamBasicCfgMode, ethernetOamBasicCfgPort=ethernetOamBasicCfgPort, ethernetOamBasicCfgState=ethernetOamBasicCfgState, ethernetOamBasicCfgEntry=ethernetOamBasicCfgEntry, ethernetOamBasicCfgLAG=ethernetOamBasicCfgLAG)
