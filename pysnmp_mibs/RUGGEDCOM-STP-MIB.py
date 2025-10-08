#
# PySNMP MIB module RUGGEDCOM-STP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/siemens/RUGGEDCOM-STP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:57 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ruggedcomTraps, ruggedcomMgmt = mibBuilder.importSymbols("RUGGEDCOM-MIB", "ruggedcomTraps", "ruggedcomMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
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
mibBuilder.exportSymbols("RUGGEDCOM-STP-MIB", rcRstpDot1dStpBrokenPorts=rcRstpDot1dStpBrokenPorts, rcRstpGroups=rcRstpGroups, rcRstpNewTopology=rcRstpNewTopology, PYSNMP_MODULE_ID=rcRstp, ruggedcomRstpTraps=ruggedcomRstpTraps, rcRstpNotifyGroup=rcRstpNotifyGroup, rcRstpDot1dStpTxHoldCount=rcRstpDot1dStpTxHoldCount, rcRstpDot1dStpBlockedPorts=rcRstpDot1dStpBlockedPorts, rcRstpBaseStpTxHoldCountGroup=rcRstpBaseStpTxHoldCountGroup, rcRstpDot1dStpForwardingPorts=rcRstpDot1dStpForwardingPorts, rcRstpBaseGroup=rcRstpBaseGroup, rcRstpConformance=rcRstpConformance, rcRstpDot1dRstpAlternatePorts=rcRstpDot1dRstpAlternatePorts, rcRstpBase=rcRstpBase, rcRstp=rcRstp, rcRstpDot1dRstpBackupPorts=rcRstpDot1dRstpBackupPorts)
