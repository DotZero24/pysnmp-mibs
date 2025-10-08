#
# PySNMP MIB module TPLINK-COMMANDER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/tplink/TPLINK-COMMANDER-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:01:46 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
clusterManage, = mibBuilder.importSymbols("TPLINK-CLUSTER-MIB", "clusterManage")
clusterConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 3, 2))
commanderConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 3, 2, 4))
clusterName = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 3, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterName.setStatus('current')
clusterHoldTime = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 3, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clusterHoldTime.setStatus('current')
clusterIntervalTime = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 3, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clusterIntervalTime.setStatus('current')
commanderClusterName = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 3, 2, 4, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commanderClusterName.setStatus('current')
clusterIp = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 3, 2, 4, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clusterIp.setStatus('current')
clusterIpMask = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 3, 2, 4, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clusterIpMask.setStatus('current')
clusterCommit = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 3, 2, 4, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("commit", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clusterCommit.setStatus('current')
mibBuilder.exportSymbols("TPLINK-COMMANDER-MIB", clusterConfig=clusterConfig, clusterCommit=clusterCommit, commanderClusterName=commanderClusterName, commanderConfig=commanderConfig, clusterHoldTime=clusterHoldTime, clusterIp=clusterIp, clusterIntervalTime=clusterIntervalTime, clusterIpMask=clusterIpMask, clusterName=clusterName)
