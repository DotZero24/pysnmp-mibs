#
# PySNMP MIB module TPLINK-COMMANDER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/tplink/TPLINK-COMMANDER-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:36:23 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("TPLINK-COMMANDER-MIB", clusterConfig=clusterConfig, clusterCommit=clusterCommit, clusterName=clusterName, clusterIntervalTime=clusterIntervalTime, commanderConfig=commanderConfig, commanderClusterName=commanderClusterName, clusterIp=clusterIp, clusterIpMask=clusterIpMask, clusterHoldTime=clusterHoldTime)
