#
# PySNMP MIB module EXTREME-EAPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/extreme/EXTREME-EAPS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:58:56 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
extremeAgent, = mibBuilder.importSymbols("EXTREME-BASE-MIB", "extremeAgent")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
extremeEaps = ModuleIdentity((1, 3, 6, 1, 4, 1, 1916, 1, 18))
if mibBuilder.loadTexts: extremeEaps.setLastUpdated('0502151530Z')
if mibBuilder.loadTexts: extremeEaps.setOrganization('Extreme Networks, Inc.')
class EapsDomainMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("invalid", 0), ("master", 1), ("transit", 2))

class EapsMbrVlanType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unassigned", 0), ("control", 1), ("protected", 2))

class EapsRingPort(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class EapsPortType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("primary", 1), ("secondary", 2))

class EapsDomainState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("idle", 0), ("complete", 1), ("failed", 2), ("linksup", 3), ("linkdown", 4), ("preforwarding", 5), ("init", 6), ("precomplete", 7), ("preinit", 8))

class EapsDomainPortStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("up", 1), ("down", 2), ("blocked", 3))

class EapsFailTimerExpiryAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("sendAlert", 0), ("openSecondaryPort", 1))

class EapsSharedPortState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("idle", 0), ("ready", 1), ("blocking", 2), ("preforwarding", 3))

class EapsSharedPortMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unconfigured", 0), ("controller", 1), ("partner", 2))

class EapsSharedPortSegmentTimerExpiryAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("sendAlert", 0), ("segmentDown", 1))

class EapsSharedPortNeighborStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("neighborDown", 0), ("neighborUp", 1), ("neighborError", 2))

class EapsSharedPortRootBlockerStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("false", 0), ("active", 1), ("inactive", 2))

class EapsSharedPortSegmentStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 0), ("segUp", 1), ("segDown", 2), ("segBlockingUp", 3), ("segBlockingDown", 4))

class EapsSharedPortVlanPortStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 0), ("activeOpen", 1), ("blocked", 2), ("open", 3), ("down", 4))

class EapsDomainPriority(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("normal", 0), ("high", 1))

extremeEapsTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 18, 1), )
if mibBuilder.loadTexts: extremeEapsTable.setStatus('current')
extremeEapsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 18, 1, 1), ).setIndexNames((0, "EXTREME-EAPS-MIB", "extremeEapsName"))
if mibBuilder.loadTexts: extremeEapsEntry.setStatus('current')
extremeEapsName = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeEapsName.setStatus('current')
extremeEapsMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 1, 1, 2), EapsDomainMode()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremeEapsMode.setStatus('current')
extremeEapsState = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 1, 1, 3), EapsDomainState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeEapsState.setStatus('current')
extremeEapsFailedFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeEapsFailedFlag.setStatus('current')
extremeEapsEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 1, 1, 5), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremeEapsEnabled.setStatus('current')
extremeEapsPrimaryPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 1, 1, 6), EapsRingPort()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremeEapsPrimaryPort.setStatus('current')
extremeEapsSecondaryPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 1, 1, 7), EapsRingPort()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremeEapsSecondaryPort.setStatus('current')
extremeEapsHelloTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremeEapsHelloTimer.setStatus('current')
extremeEapsFailedTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 300))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremeEapsFailedTimer.setStatus('current')
extremeEapsFailedTimerExpiryAction = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 1, 1, 10), EapsFailTimerExpiryAction()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremeEapsFailedTimerExpiryAction.setStatus('current')
extremeEapsUnconfigRingPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 1, 1, 11), EapsPortType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extremeEapsUnconfigRingPort.setStatus('current')
extremeEapsPrimaryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 1, 1, 12), EapsDomainPortStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeEapsPrimaryStatus.setStatus('current')
extremeEapsSecondaryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 1, 1, 13), EapsDomainPortStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeEapsSecondaryStatus.setStatus('current')
extremeEapsProtectedVlansCount = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeEapsProtectedVlansCount.setStatus('current')
extremeEapsRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 1, 1, 15), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremeEapsRowStatus.setStatus('current')
extremeEapsHelloTimerMs = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 900))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeEapsHelloTimerMs.setStatus('current')
extremeEapsPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 1, 1, 17), EapsDomainPriority()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremeEapsPriority.setStatus('current')
extremeEapsPrevState = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 18, 2), EapsDomainState()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: extremeEapsPrevState.setStatus('current')
extremeEapsGlobalInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 18, 3))
extremeEapsGlobalEnabled = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 18, 3, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extremeEapsGlobalEnabled.setStatus('current')
extremeEapsGlobalFastConvergence = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 18, 3, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extremeEapsGlobalFastConvergence.setStatus('current')
extremeEapsLastConfigurationChange = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 18, 3, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeEapsLastConfigurationChange.setStatus('current')
extremeEapsLastStatusChange = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 18, 3, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeEapsLastStatusChange.setStatus('current')
extremeEapsStatusTrapCount = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 18, 3, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeEapsStatusTrapCount.setStatus('current')
extremeEapsGlobalMulticastAddRingPorts = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 18, 3, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extremeEapsGlobalMulticastAddRingPorts.setStatus('current')
extremeEapsGlobalMulticastSendIGMPQuery = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 18, 3, 7), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extremeEapsGlobalMulticastSendIGMPQuery.setStatus('current')
extremeEapsGlobalMulticastTempFlooding = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 18, 3, 8), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extremeEapsGlobalMulticastTempFlooding.setStatus('current')
extremeEapsGlobalMulticastTempFloodingDuration = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 18, 3, 9), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extremeEapsGlobalMulticastTempFloodingDuration.setStatus('current')
extremeEapsMbrVlanTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 18, 4), )
if mibBuilder.loadTexts: extremeEapsMbrVlanTable.setStatus('current')
extremeEapsMbrVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 18, 4, 1), ).setIndexNames((0, "EXTREME-EAPS-MIB", "extremeEapsName"), (0, "EXTREME-EAPS-MIB", "extremeEapsMbrVlanName"), (0, "EXTREME-EAPS-MIB", "extremeEapsMbrVlanType"))
if mibBuilder.loadTexts: extremeEapsMbrVlanEntry.setStatus('current')
extremeEapsMbrVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 4, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeEapsMbrVlanName.setStatus('current')
extremeEapsMbrVlanType = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 4, 1, 2), EapsMbrVlanType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeEapsMbrVlanType.setStatus('current')
extremeEapsMbrVlanTag = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeEapsMbrVlanTag.setStatus('current')
extremeEapsMbrVlanRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 4, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremeEapsMbrVlanRowStatus.setStatus('current')
extremeEapsSharedPortTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 18, 5), )
if mibBuilder.loadTexts: extremeEapsSharedPortTable.setStatus('current')
extremeEapsSharedPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 18, 5, 1), ).setIndexNames((0, "EXTREME-EAPS-MIB", "extremeEapsSharedPortIfIndex"))
if mibBuilder.loadTexts: extremeEapsSharedPortEntry.setStatus('current')
extremeEapsSharedPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 5, 1, 1), EapsRingPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeEapsSharedPortIfIndex.setStatus('current')
extremeEapsSharedPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 5, 1, 2), EapsSharedPortMode()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremeEapsSharedPortMode.setStatus('current')
extremeEapsSharedPortLinkId = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 5, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65534))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremeEapsSharedPortLinkId.setStatus('current')
extremeEapsSharedPortSegmentTimerExpiryAction = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 5, 1, 4), EapsSharedPortSegmentTimerExpiryAction()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremeEapsSharedPortSegmentTimerExpiryAction.setStatus('current')
extremeEapsSharedPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 5, 1, 5), EapsSharedPortState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeEapsSharedPortState.setStatus('current')
extremeEapsSharedPortNbrStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 5, 1, 6), EapsSharedPortNeighborStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeEapsSharedPortNbrStatus.setStatus('current')
extremeEapsSharedPortDomainsCount = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 5, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeEapsSharedPortDomainsCount.setStatus('current')
extremeEapsSharedPortProtectedVlansCount = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 5, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeEapsSharedPortProtectedVlansCount.setStatus('current')
extremeEapsSharedPortRootBlockerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 5, 1, 9), EapsSharedPortRootBlockerStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeEapsSharedPortRootBlockerStatus.setStatus('current')
extremeEapsSharedPortRootBlockerId = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 5, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeEapsSharedPortRootBlockerId.setStatus('current')
extremeEapsSharedPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 5, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremeEapsSharedPortRowStatus.setStatus('current')
extremeEapsSharedPortSegmentHealthInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 5, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeEapsSharedPortSegmentHealthInterval.setStatus('current')
extremeEapsSharedPortSegmentTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 5, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeEapsSharedPortSegmentTimeout.setStatus('current')
extremeEapsSharedPortCommonPathFailedFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 5, 1, 14), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeEapsSharedPortCommonPathFailedFlag.setStatus('current')
extremeEapsSharedPortCommonPathHealthInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 5, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeEapsSharedPortCommonPathHealthInterval.setStatus('current')
extremeEapsSharedPortCommonPathTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 5, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeEapsSharedPortCommonPathTimeout.setStatus('current')
extremeEapsSharedPortSegmentTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 18, 6), )
if mibBuilder.loadTexts: extremeEapsSharedPortSegmentTable.setStatus('current')
extremeEapsSharedPortSegmentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 18, 6, 1), ).setIndexNames((0, "EXTREME-EAPS-MIB", "extremeEapsSharedPortIfIndex"), (0, "EXTREME-EAPS-MIB", "extremeEapsSharedPortSegmentPort"), (0, "EXTREME-EAPS-MIB", "extremeEapsName"))
if mibBuilder.loadTexts: extremeEapsSharedPortSegmentEntry.setStatus('current')
extremeEapsSharedPortSegmentPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 6, 1, 1), EapsRingPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeEapsSharedPortSegmentPort.setStatus('current')
extremeEapsSharedPortSegmentStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 6, 1, 2), EapsSharedPortSegmentStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeEapsSharedPortSegmentStatus.setStatus('current')
extremeEapsSharedPortSegmentFailedFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 6, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeEapsSharedPortSegmentFailedFlag.setStatus('current')
extremeEapsSharedPortSegmentVlanPortCount = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 6, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeEapsSharedPortSegmentVlanPortCount.setStatus('current')
extremeEapsSharedPortSegmentAdjId = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 6, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeEapsSharedPortSegmentAdjId.setStatus('current')
extremeEapsSharedPortSegmentRBD = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 6, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeEapsSharedPortSegmentRBD.setStatus('current')
extremeEapsSharedPortVlanTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 18, 7), )
if mibBuilder.loadTexts: extremeEapsSharedPortVlanTable.setStatus('current')
extremeEapsSharedPortVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 18, 7, 1), ).setIndexNames((0, "EXTREME-EAPS-MIB", "extremeEapsSharedPortIfIndex"), (0, "EXTREME-EAPS-MIB", "extremeEapsSharedPortVlanName"))
if mibBuilder.loadTexts: extremeEapsSharedPortVlanEntry.setStatus('current')
extremeEapsSharedPortVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 7, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeEapsSharedPortVlanName.setStatus('current')
extremeEapsSharedPortVlanPortCount = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 7, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeEapsSharedPortVlanPortCount.setStatus('current')
extremeEapsSharedPortVlanActiveOpenPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 7, 1, 3), EapsRingPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeEapsSharedPortVlanActiveOpenPort.setStatus('current')
extremeEapsSharedPortVlanPortTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 18, 8), )
if mibBuilder.loadTexts: extremeEapsSharedPortVlanPortTable.setStatus('current')
extremeEapsSharedPortVlanPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 18, 8, 1), ).setIndexNames((0, "EXTREME-EAPS-MIB", "extremeEapsSharedPortIfIndex"), (0, "EXTREME-EAPS-MIB", "extremeEapsSharedPortVlanName"), (0, "EXTREME-EAPS-MIB", "extremeEapsSharedPortSegmentPort"), (0, "EXTREME-EAPS-MIB", "extremeEapsName"))
if mibBuilder.loadTexts: extremeEapsSharedPortVlanPortEntry.setStatus('current')
extremeEapsSharedPortVlanPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 18, 8, 1, 1), EapsSharedPortVlanPortStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeEapsSharedPortVlanPortStatus.setStatus('current')
mibBuilder.exportSymbols("EXTREME-EAPS-MIB", extremeEapsSharedPortSegmentStatus=extremeEapsSharedPortSegmentStatus, extremeEapsState=extremeEapsState, EapsDomainPriority=EapsDomainPriority, EapsDomainPortStatus=EapsDomainPortStatus, extremeEapsSharedPortCommonPathTimeout=extremeEapsSharedPortCommonPathTimeout, extremeEapsLastStatusChange=extremeEapsLastStatusChange, extremeEapsFailedFlag=extremeEapsFailedFlag, extremeEapsSecondaryPort=extremeEapsSecondaryPort, extremeEapsSharedPortVlanActiveOpenPort=extremeEapsSharedPortVlanActiveOpenPort, extremeEapsMbrVlanEntry=extremeEapsMbrVlanEntry, extremeEapsSharedPortVlanPortEntry=extremeEapsSharedPortVlanPortEntry, extremeEaps=extremeEaps, extremeEapsSharedPortSegmentTimeout=extremeEapsSharedPortSegmentTimeout, extremeEapsRowStatus=extremeEapsRowStatus, PYSNMP_MODULE_ID=extremeEaps, extremeEapsHelloTimer=extremeEapsHelloTimer, extremeEapsMbrVlanType=extremeEapsMbrVlanType, extremeEapsSharedPortRootBlockerId=extremeEapsSharedPortRootBlockerId, extremeEapsSharedPortCommonPathFailedFlag=extremeEapsSharedPortCommonPathFailedFlag, EapsSharedPortState=EapsSharedPortState, extremeEapsSharedPortVlanEntry=extremeEapsSharedPortVlanEntry, extremeEapsGlobalFastConvergence=extremeEapsGlobalFastConvergence, extremeEapsLastConfigurationChange=extremeEapsLastConfigurationChange, extremeEapsGlobalMulticastAddRingPorts=extremeEapsGlobalMulticastAddRingPorts, extremeEapsSharedPortCommonPathHealthInterval=extremeEapsSharedPortCommonPathHealthInterval, extremeEapsSharedPortNbrStatus=extremeEapsSharedPortNbrStatus, EapsRingPort=EapsRingPort, extremeEapsPrimaryStatus=extremeEapsPrimaryStatus, extremeEapsSharedPortSegmentVlanPortCount=extremeEapsSharedPortSegmentVlanPortCount, extremeEapsName=extremeEapsName, EapsSharedPortSegmentStatus=EapsSharedPortSegmentStatus, extremeEapsSharedPortMode=extremeEapsSharedPortMode, extremeEapsSecondaryStatus=extremeEapsSecondaryStatus, extremeEapsSharedPortDomainsCount=extremeEapsSharedPortDomainsCount, extremeEapsMbrVlanRowStatus=extremeEapsMbrVlanRowStatus, EapsSharedPortRootBlockerStatus=EapsSharedPortRootBlockerStatus, extremeEapsMbrVlanName=extremeEapsMbrVlanName, extremeEapsSharedPortVlanPortTable=extremeEapsSharedPortVlanPortTable, extremeEapsSharedPortRowStatus=extremeEapsSharedPortRowStatus, extremeEapsProtectedVlansCount=extremeEapsProtectedVlansCount, extremeEapsSharedPortTable=extremeEapsSharedPortTable, extremeEapsHelloTimerMs=extremeEapsHelloTimerMs, extremeEapsSharedPortSegmentEntry=extremeEapsSharedPortSegmentEntry, extremeEapsSharedPortLinkId=extremeEapsSharedPortLinkId, EapsPortType=EapsPortType, extremeEapsSharedPortRootBlockerStatus=extremeEapsSharedPortRootBlockerStatus, extremeEapsSharedPortSegmentHealthInterval=extremeEapsSharedPortSegmentHealthInterval, extremeEapsEntry=extremeEapsEntry, extremeEapsPriority=extremeEapsPriority, extremeEapsSharedPortState=extremeEapsSharedPortState, extremeEapsSharedPortSegmentFailedFlag=extremeEapsSharedPortSegmentFailedFlag, extremeEapsSharedPortSegmentPort=extremeEapsSharedPortSegmentPort, extremeEapsSharedPortIfIndex=extremeEapsSharedPortIfIndex, extremeEapsMbrVlanTable=extremeEapsMbrVlanTable, extremeEapsEnabled=extremeEapsEnabled, extremeEapsStatusTrapCount=extremeEapsStatusTrapCount, extremeEapsPrimaryPort=extremeEapsPrimaryPort, extremeEapsSharedPortVlanPortStatus=extremeEapsSharedPortVlanPortStatus, extremeEapsFailedTimer=extremeEapsFailedTimer, EapsSharedPortVlanPortStatus=EapsSharedPortVlanPortStatus, EapsSharedPortNeighborStatus=EapsSharedPortNeighborStatus, extremeEapsMbrVlanTag=extremeEapsMbrVlanTag, extremeEapsSharedPortVlanTable=extremeEapsSharedPortVlanTable, extremeEapsPrevState=extremeEapsPrevState, EapsDomainMode=EapsDomainMode, EapsSharedPortSegmentTimerExpiryAction=EapsSharedPortSegmentTimerExpiryAction, EapsMbrVlanType=EapsMbrVlanType, EapsFailTimerExpiryAction=EapsFailTimerExpiryAction, extremeEapsSharedPortSegmentAdjId=extremeEapsSharedPortSegmentAdjId, extremeEapsTable=extremeEapsTable, extremeEapsMode=extremeEapsMode, extremeEapsGlobalInfo=extremeEapsGlobalInfo, extremeEapsSharedPortSegmentTimerExpiryAction=extremeEapsSharedPortSegmentTimerExpiryAction, EapsSharedPortMode=EapsSharedPortMode, extremeEapsSharedPortVlanPortCount=extremeEapsSharedPortVlanPortCount, extremeEapsGlobalEnabled=extremeEapsGlobalEnabled, extremeEapsSharedPortEntry=extremeEapsSharedPortEntry, extremeEapsUnconfigRingPort=extremeEapsUnconfigRingPort, extremeEapsSharedPortVlanName=extremeEapsSharedPortVlanName, extremeEapsSharedPortProtectedVlansCount=extremeEapsSharedPortProtectedVlansCount, extremeEapsFailedTimerExpiryAction=extremeEapsFailedTimerExpiryAction, extremeEapsGlobalMulticastSendIGMPQuery=extremeEapsGlobalMulticastSendIGMPQuery, extremeEapsSharedPortSegmentTable=extremeEapsSharedPortSegmentTable, EapsDomainState=EapsDomainState, extremeEapsGlobalMulticastTempFloodingDuration=extremeEapsGlobalMulticastTempFloodingDuration, extremeEapsSharedPortSegmentRBD=extremeEapsSharedPortSegmentRBD, extremeEapsGlobalMulticastTempFlooding=extremeEapsGlobalMulticastTempFlooding)
