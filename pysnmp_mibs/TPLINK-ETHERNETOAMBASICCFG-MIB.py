#
# PySNMP MIB module TPLINK-ETHERNETOAMBASICCFG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/tplink/TPLINK-ETHERNETOAMBASICCFG-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:36:31 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("TPLINK-ETHERNETOAMBASICCFG-MIB", ethernetOamBasicCfgTable=ethernetOamBasicCfgTable, ethernetOamBasicCfgEntry=ethernetOamBasicCfgEntry, ethernetOamBasicCfgState=ethernetOamBasicCfgState, ethernetOamBasicCfgLAG=ethernetOamBasicCfgLAG, ethernetOamBasicCfgMode=ethernetOamBasicCfgMode, ethernetOamBasicCfgPort=ethernetOamBasicCfgPort)
