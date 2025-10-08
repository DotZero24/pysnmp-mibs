#
# PySNMP MIB module CISCOSB-openflow-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/ciscosb/CISCOSB-openflow-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:55:56 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, DateAndTime, TextualConvention, TruthValue, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DateAndTime", "TextualConvention", "TruthValue", "TimeStamp", "DisplayString")
rlOpenFlow = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 319))
rlOpenFlowSupported = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 319, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlOpenFlowSupported.setStatus('current')
rlOpenFlowTcpPort = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 319, 2), Integer32().clone(6633)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlOpenFlowTcpPort.setStatus('current')
rlOpenFlowServerIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 319, 3), IpAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlOpenFlowServerIpAddr.setStatus('current')
rlOpenFlowProtocolType = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 319, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("tcp", 0), ("tls", 1))).clone('tcp')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlOpenFlowProtocolType.setStatus('current')
rlOpenFlowDefaultForwardAction = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 319, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("forward", 0), ("drop", 1), ("toController", 2))).clone('forward')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlOpenFlowDefaultForwardAction.setStatus('current')
rlOpenFlowEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 319, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOpenFlowEnable.setStatus('current')
rlOpenFlowEnableAfterReset = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 319, 7), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlOpenFlowEnableAfterReset.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-openflow-MIB", rlOpenFlow=rlOpenFlow, rlOpenFlowServerIpAddr=rlOpenFlowServerIpAddr, rlOpenFlowTcpPort=rlOpenFlowTcpPort, rlOpenFlowProtocolType=rlOpenFlowProtocolType, rlOpenFlowSupported=rlOpenFlowSupported, rlOpenFlowEnable=rlOpenFlowEnable, rlOpenFlowDefaultForwardAction=rlOpenFlowDefaultForwardAction, rlOpenFlowEnableAfterReset=rlOpenFlowEnableAfterReset)
