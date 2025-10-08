#
# PySNMP MIB module TPLINK-NTDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/tplink/TPLINK-NTDP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:36:26 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ntdpManage, = mibBuilder.importSymbols("TPLINK-CLUSTER-MIB", "ntdpManage")
ntdpGlobalConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 2, 1))
ntdpStatus = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntdpStatus.setStatus('current')
ntdpIntervalTime = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntdpIntervalTime.setStatus('current')
ntdpHop = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntdpHop.setStatus('current')
ntdpHopDelay = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntdpHopDelay.setStatus('current')
ntpdPortDelay = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntpdPortDelay.setStatus('current')
ntdpPortTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 2, 2), )
if mibBuilder.loadTexts: ntdpPortTable.setStatus('current')
ntdpPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 2, 2, 1), ).setIndexNames((0, "TPLINK-NTDP-MIB", "ifIndex"))
if mibBuilder.loadTexts: ntdpPortEntry.setStatus('current')
ntdpPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntdpPortStatus.setStatus('current')
ntdpCollectTopo = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("commit", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntdpCollectTopo.setStatus('current')
mibBuilder.exportSymbols("TPLINK-NTDP-MIB", ntdpStatus=ntdpStatus, ntdpPortStatus=ntdpPortStatus, ntdpPortTable=ntdpPortTable, ntdpIntervalTime=ntdpIntervalTime, ntdpPortEntry=ntdpPortEntry, ntdpHopDelay=ntdpHopDelay, ntdpCollectTopo=ntdpCollectTopo, ntdpHop=ntdpHop, ntdpGlobalConfig=ntdpGlobalConfig, ntpdPortDelay=ntpdPortDelay)
