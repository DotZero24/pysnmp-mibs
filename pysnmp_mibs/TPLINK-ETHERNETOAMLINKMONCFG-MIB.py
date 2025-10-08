#
# PySNMP MIB module TPLINK-ETHERNETOAMLINKMONCFG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/tplink/TPLINK-ETHERNETOAMLINKMONCFG-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:01:30 2025
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
ethernetOamLinkMonConfig, = mibBuilder.importSymbols("TPLINK-ETHERNETOAM-MIB", "ethernetOamLinkMonConfig")
ethernetOamLinkMonCfgTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 2, 1), )
if mibBuilder.loadTexts: ethernetOamLinkMonCfgTable.setStatus('current')
ethernetOamLinkMonCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "TPLINK-ETHERNETOAMLINKMONCFG-MIB", "ethernetOamLinkMonCfgEvent"))
if mibBuilder.loadTexts: ethernetOamLinkMonCfgEntry.setStatus('current')
ethernetOamLinkMonCfgPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 2, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamLinkMonCfgPort.setStatus('current')
ethernetOamLinkMonCfgEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("symbol-period", 1), ("frame", 2), ("frame-period", 3), ("frame-seconds", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamLinkMonCfgEvent.setStatus('current')
ethernetOamLinkMonCfgThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 2, 1, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethernetOamLinkMonCfgThreshold.setStatus('current')
ethernetOamLinkMonCfgWindow = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 2, 1, 1, 4), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethernetOamLinkMonCfgWindow.setStatus('current')
ethernetOamLinkMonCfgNotify = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethernetOamLinkMonCfgNotify.setStatus('current')
ethernetOamLinkMonCfgLAG = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 2, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamLinkMonCfgLAG.setStatus('current')
mibBuilder.exportSymbols("TPLINK-ETHERNETOAMLINKMONCFG-MIB", ethernetOamLinkMonCfgNotify=ethernetOamLinkMonCfgNotify, ethernetOamLinkMonCfgPort=ethernetOamLinkMonCfgPort, ethernetOamLinkMonCfgThreshold=ethernetOamLinkMonCfgThreshold, ethernetOamLinkMonCfgWindow=ethernetOamLinkMonCfgWindow, ethernetOamLinkMonCfgEntry=ethernetOamLinkMonCfgEntry, ethernetOamLinkMonCfgTable=ethernetOamLinkMonCfgTable, ethernetOamLinkMonCfgLAG=ethernetOamLinkMonCfgLAG, ethernetOamLinkMonCfgEvent=ethernetOamLinkMonCfgEvent)
