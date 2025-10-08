#
# PySNMP MIB module NETGEAR-RADLAN-openflow-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/netgear/NETGEAR-RADLAN-openflow-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:28:35 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
rnd, = mibBuilder.importSymbols("NETGEAR-RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Integer32, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, TimeTicks, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Integer32", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "TimeTicks", "Bits", "IpAddress")
DisplayString, TimeStamp, RowStatus, DateAndTime, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp", "RowStatus", "DateAndTime", "TruthValue", "TextualConvention")
rlOpenFlow = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 17, 319))
rlOpenFlowSupported = MibScalar((1, 3, 6, 1, 4, 1, 4526, 17, 319, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlOpenFlowSupported.setStatus('current')
rlOpenFlowTcpPort = MibScalar((1, 3, 6, 1, 4, 1, 4526, 17, 319, 2), Integer32().clone(6633)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlOpenFlowTcpPort.setStatus('current')
rlOpenFlowServerIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 4526, 17, 319, 3), IpAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlOpenFlowServerIpAddr.setStatus('current')
rlOpenFlowProtocolType = MibScalar((1, 3, 6, 1, 4, 1, 4526, 17, 319, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("tcp", 0), ("tls", 1))).clone('tcp')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlOpenFlowProtocolType.setStatus('current')
rlOpenFlowDefaultForwardAction = MibScalar((1, 3, 6, 1, 4, 1, 4526, 17, 319, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("forward", 0), ("drop", 1), ("toController", 2))).clone('forward')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlOpenFlowDefaultForwardAction.setStatus('current')
rlOpenFlowEnable = MibScalar((1, 3, 6, 1, 4, 1, 4526, 17, 319, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOpenFlowEnable.setStatus('current')
rlOpenFlowEnableAfterReset = MibScalar((1, 3, 6, 1, 4, 1, 4526, 17, 319, 7), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlOpenFlowEnableAfterReset.setStatus('current')
mibBuilder.exportSymbols("NETGEAR-RADLAN-openflow-MIB", rlOpenFlowSupported=rlOpenFlowSupported, rlOpenFlow=rlOpenFlow, rlOpenFlowDefaultForwardAction=rlOpenFlowDefaultForwardAction, rlOpenFlowEnableAfterReset=rlOpenFlowEnableAfterReset, rlOpenFlowServerIpAddr=rlOpenFlowServerIpAddr, rlOpenFlowProtocolType=rlOpenFlowProtocolType, rlOpenFlowTcpPort=rlOpenFlowTcpPort, rlOpenFlowEnable=rlOpenFlowEnable)
