#
# PySNMP MIB module TPLINK-NTDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/tplink/TPLINK-NTDP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:01:50 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("TPLINK-NTDP-MIB", ntdpCollectTopo=ntdpCollectTopo, ntdpStatus=ntdpStatus, ntdpGlobalConfig=ntdpGlobalConfig, ntdpPortTable=ntdpPortTable, ntdpIntervalTime=ntdpIntervalTime, ntdpHopDelay=ntdpHopDelay, ntdpPortEntry=ntdpPortEntry, ntdpPortStatus=ntdpPortStatus, ntpdPortDelay=ntpdPortDelay, ntdpHop=ntdpHop)
