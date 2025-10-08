#
# PySNMP MIB module RUGGEDCOM-STP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/siemens/RUGGEDCOM-STP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:23 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ruggedcomMgmt, ruggedcomTraps = mibBuilder.importSymbols("RUGGEDCOM-MIB", "ruggedcomMgmt", "ruggedcomTraps")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rcRstp = ModuleIdentity((1, 3, 6, 1, 4, 1, 15004, 4, 5))
rcRstp.setRevisions(('2012-06-01 17:00', '2012-06-01 17:00', '2010-10-10 10:00',))
if mibBuilder.loadTexts: rcRstp.setLastUpdated('201208030700Z')
if mibBuilder.loadTexts: rcRstp.setOrganization('RuggedCom')
rcRstpBase = MibIdentifier((1, 3, 6, 1, 4, 1, 15004, 4, 5, 1))
rcRstpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 15004, 4, 5, 3))
rcRstpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 15004, 4, 5, 3, 2))
ruggedcomRstpTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 15004, 5, 11))
rcRstpDot1dStpTxHoldCount = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(3, 100), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcRstpDot1dStpTxHoldCount.setStatus('current')
rcRstpDot1dStpForwardingPorts = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 5, 1, 2), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcRstpDot1dStpForwardingPorts.setStatus('current')
rcRstpDot1dStpBlockedPorts = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 5, 1, 3), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcRstpDot1dStpBlockedPorts.setStatus('current')
rcRstpDot1dStpBrokenPorts = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 5, 1, 4), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcRstpDot1dStpBrokenPorts.setStatus('current')
rcRstpDot1dRstpAlternatePorts = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 5, 1, 5), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcRstpDot1dRstpAlternatePorts.setStatus('current')
rcRstpDot1dRstpBackupPorts = MibScalar((1, 3, 6, 1, 4, 1, 15004, 4, 5, 1, 6), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcRstpDot1dRstpBackupPorts.setStatus('current')
rcRstpNewTopology = NotificationType((1, 3, 6, 1, 4, 1, 15004, 5, 11, 1)).setObjects(("RUGGEDCOM-STP-MIB", "rcRstpDot1dStpForwardingPorts"), ("RUGGEDCOM-STP-MIB", "rcRstpDot1dStpBlockedPorts"), ("RUGGEDCOM-STP-MIB", "rcRstpDot1dStpBrokenPorts"), ("RUGGEDCOM-STP-MIB", "rcRstpDot1dRstpAlternatePorts"), ("RUGGEDCOM-STP-MIB", "rcRstpDot1dRstpBackupPorts"), ("RUGGEDCOM-STP-MIB", "dot1dStpRootPort"), ("RUGGEDCOM-STP-MIB", "dot1dStpDesignatedRoot"))
if mibBuilder.loadTexts: rcRstpNewTopology.setStatus('current')
rcRstpBaseStpTxHoldCountGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 15004, 4, 5, 3, 2, 1)).setObjects(("RUGGEDCOM-STP-MIB", "rcRstpDot1dStpTxHoldCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rcRstpBaseStpTxHoldCountGroup = rcRstpBaseStpTxHoldCountGroup.setStatus('current')
rcRstpBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 15004, 4, 5, 3, 2, 2)).setObjects(("RUGGEDCOM-STP-MIB", "rcRstpDot1dStpForwardingPorts"), ("RUGGEDCOM-STP-MIB", "rcRstpDot1dStpBlockedPorts"), ("RUGGEDCOM-STP-MIB", "rcRstpDot1dStpBrokenPorts"), ("RUGGEDCOM-STP-MIB", "rcRstpDot1dRstpAlternatePorts"), ("RUGGEDCOM-STP-MIB", "rcRstpDot1dRstpBackupPorts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rcRstpBaseGroup = rcRstpBaseGroup.setStatus('current')
rcRstpNotifyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 15004, 4, 5, 3, 2, 3)).setObjects(("RUGGEDCOM-STP-MIB", "rcRstpNewTopology"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rcRstpNotifyGroup = rcRstpNotifyGroup.setStatus('current')
mibBuilder.exportSymbols("RUGGEDCOM-STP-MIB", rcRstpGroups=rcRstpGroups, PYSNMP_MODULE_ID=rcRstp, rcRstpDot1dStpTxHoldCount=rcRstpDot1dStpTxHoldCount, ruggedcomRstpTraps=ruggedcomRstpTraps, rcRstpDot1dRstpAlternatePorts=rcRstpDot1dRstpAlternatePorts, rcRstp=rcRstp, rcRstpDot1dStpBlockedPorts=rcRstpDot1dStpBlockedPorts, rcRstpDot1dStpBrokenPorts=rcRstpDot1dStpBrokenPorts, rcRstpDot1dRstpBackupPorts=rcRstpDot1dRstpBackupPorts, rcRstpBaseGroup=rcRstpBaseGroup, rcRstpNotifyGroup=rcRstpNotifyGroup, rcRstpConformance=rcRstpConformance, rcRstpNewTopology=rcRstpNewTopology, rcRstpDot1dStpForwardingPorts=rcRstpDot1dStpForwardingPorts, rcRstpBaseStpTxHoldCountGroup=rcRstpBaseStpTxHoldCountGroup, rcRstpBase=rcRstpBase)
