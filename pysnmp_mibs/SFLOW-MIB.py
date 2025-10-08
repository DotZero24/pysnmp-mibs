#
# PySNMP MIB module SFLOW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rfc/SFLOW-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:43:24 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
OwnerString, = mibBuilder.importSymbols("RMON-MIB", "OwnerString")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
sFlowMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 14706, 1))
sFlowMIB.setRevisions(('2003-10-18 00:00', '2003-09-24 00:00', '2003-04-08 00:00', '2002-09-17 00:00', '2001-07-31 00:00', '2001-05-01 00:00',))
if mibBuilder.loadTexts: sFlowMIB.setLastUpdated('200309240000Z')
if mibBuilder.loadTexts: sFlowMIB.setOrganization('sFlow.org')
sFlowAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 14706, 1, 1))
class SFlowDataSource(TextualConvention, ObjectIdentifier):
    status = 'current'

class SFlowInstance(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 65535)

class SFlowReceiver(TextualConvention, Integer32):
    status = 'current'

sFlowVersion = MibScalar((1, 3, 6, 1, 4, 1, 14706, 1, 1, 1), SnmpAdminString().clone('1.3;;')).setMaxAccess("readonly")
if mibBuilder.loadTexts: sFlowVersion.setStatus('current')
sFlowAgentAddressType = MibScalar((1, 3, 6, 1, 4, 1, 14706, 1, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sFlowAgentAddressType.setStatus('current')
sFlowAgentAddress = MibScalar((1, 3, 6, 1, 4, 1, 14706, 1, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sFlowAgentAddress.setStatus('current')
sFlowRcvrTable = MibTable((1, 3, 6, 1, 4, 1, 14706, 1, 1, 4), )
if mibBuilder.loadTexts: sFlowRcvrTable.setStatus('current')
sFlowRcvrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14706, 1, 1, 4, 1), ).setIndexNames((0, "SFLOW-MIB", "sFlowRcvrIndex"))
if mibBuilder.loadTexts: sFlowRcvrEntry.setStatus('current')
sFlowRcvrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14706, 1, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: sFlowRcvrIndex.setStatus('current')
sFlowRcvrOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 14706, 1, 1, 4, 1, 2), OwnerString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sFlowRcvrOwner.setStatus('current')
sFlowRcvrTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 14706, 1, 1, 4, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sFlowRcvrTimeout.setStatus('current')
sFlowRcvrMaximumDatagramSize = MibTableColumn((1, 3, 6, 1, 4, 1, 14706, 1, 1, 4, 1, 4), Integer32().clone(1400)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sFlowRcvrMaximumDatagramSize.setStatus('current')
sFlowRcvrAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 14706, 1, 1, 4, 1, 5), InetAddressType().clone('ipv4')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sFlowRcvrAddressType.setStatus('current')
sFlowRcvrAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 14706, 1, 1, 4, 1, 6), InetAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sFlowRcvrAddress.setStatus('current')
sFlowRcvrPort = MibTableColumn((1, 3, 6, 1, 4, 1, 14706, 1, 1, 4, 1, 7), Integer32().clone(6343)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sFlowRcvrPort.setStatus('current')
sFlowRcvrDatagramVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 14706, 1, 1, 4, 1, 8), Integer32().clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sFlowRcvrDatagramVersion.setStatus('current')
sFlowFsTable = MibTable((1, 3, 6, 1, 4, 1, 14706, 1, 1, 5), )
if mibBuilder.loadTexts: sFlowFsTable.setStatus('current')
sFlowFsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14706, 1, 1, 5, 1), ).setIndexNames((0, "SFLOW-MIB", "sFlowFsDataSource"), (0, "SFLOW-MIB", "sFlowFsInstance"))
if mibBuilder.loadTexts: sFlowFsEntry.setStatus('current')
sFlowFsDataSource = MibTableColumn((1, 3, 6, 1, 4, 1, 14706, 1, 1, 5, 1, 1), SFlowDataSource())
if mibBuilder.loadTexts: sFlowFsDataSource.setStatus('current')
sFlowFsInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 14706, 1, 1, 5, 1, 2), SFlowInstance())
if mibBuilder.loadTexts: sFlowFsInstance.setStatus('current')
sFlowFsReceiver = MibTableColumn((1, 3, 6, 1, 4, 1, 14706, 1, 1, 5, 1, 3), SFlowReceiver()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sFlowFsReceiver.setStatus('current')
sFlowFsPacketSamplingRate = MibTableColumn((1, 3, 6, 1, 4, 1, 14706, 1, 1, 5, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sFlowFsPacketSamplingRate.setStatus('current')
sFlowFsMaximumHeaderSize = MibTableColumn((1, 3, 6, 1, 4, 1, 14706, 1, 1, 5, 1, 5), Integer32().clone(128)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sFlowFsMaximumHeaderSize.setStatus('current')
sFlowCpTable = MibTable((1, 3, 6, 1, 4, 1, 14706, 1, 1, 6), )
if mibBuilder.loadTexts: sFlowCpTable.setStatus('current')
sFlowCpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14706, 1, 1, 6, 1), ).setIndexNames((0, "SFLOW-MIB", "sFlowCpDataSource"), (0, "SFLOW-MIB", "sFlowCpInstance"))
if mibBuilder.loadTexts: sFlowCpEntry.setStatus('current')
sFlowCpDataSource = MibTableColumn((1, 3, 6, 1, 4, 1, 14706, 1, 1, 6, 1, 1), SFlowDataSource())
if mibBuilder.loadTexts: sFlowCpDataSource.setStatus('current')
sFlowCpInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 14706, 1, 1, 6, 1, 2), SFlowInstance())
if mibBuilder.loadTexts: sFlowCpInstance.setStatus('current')
sFlowCpReceiver = MibTableColumn((1, 3, 6, 1, 4, 1, 14706, 1, 1, 6, 1, 3), SFlowReceiver()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sFlowCpReceiver.setStatus('current')
sFlowCpInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 14706, 1, 1, 6, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sFlowCpInterval.setStatus('current')
sFlowMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 14706, 1, 2))
sFlowMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 14706, 1, 2, 1))
sFlowMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 14706, 1, 2, 2))
sFlowCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 14706, 1, 2, 2, 1)).setObjects(("SFLOW-MIB", "sFlowAgentGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sFlowCompliance = sFlowCompliance.setStatus('current')
sFlowAgentGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 14706, 1, 2, 1, 1)).setObjects(("SFLOW-MIB", "sFlowVersion"), ("SFLOW-MIB", "sFlowAgentAddressType"), ("SFLOW-MIB", "sFlowAgentAddress"), ("SFLOW-MIB", "sFlowRcvrOwner"), ("SFLOW-MIB", "sFlowRcvrTimeout"), ("SFLOW-MIB", "sFlowRcvrMaximumDatagramSize"), ("SFLOW-MIB", "sFlowRcvrAddressType"), ("SFLOW-MIB", "sFlowRcvrAddress"), ("SFLOW-MIB", "sFlowRcvrPort"), ("SFLOW-MIB", "sFlowRcvrDatagramVersion"), ("SFLOW-MIB", "sFlowFsReceiver"), ("SFLOW-MIB", "sFlowFsPacketSamplingRate"), ("SFLOW-MIB", "sFlowFsMaximumHeaderSize"), ("SFLOW-MIB", "sFlowCpReceiver"), ("SFLOW-MIB", "sFlowCpInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sFlowAgentGroup = sFlowAgentGroup.setStatus('current')
mibBuilder.exportSymbols("SFLOW-MIB", sFlowMIBCompliances=sFlowMIBCompliances, PYSNMP_MODULE_ID=sFlowMIB, SFlowInstance=SFlowInstance, sFlowCpEntry=sFlowCpEntry, sFlowRcvrMaximumDatagramSize=sFlowRcvrMaximumDatagramSize, sFlowCpDataSource=sFlowCpDataSource, sFlowFsEntry=sFlowFsEntry, sFlowRcvrIndex=sFlowRcvrIndex, sFlowFsInstance=sFlowFsInstance, sFlowRcvrOwner=sFlowRcvrOwner, SFlowReceiver=SFlowReceiver, sFlowCpInterval=sFlowCpInterval, sFlowAgentAddress=sFlowAgentAddress, sFlowAgent=sFlowAgent, sFlowFsReceiver=sFlowFsReceiver, sFlowRcvrPort=sFlowRcvrPort, sFlowMIBConformance=sFlowMIBConformance, sFlowRcvrAddress=sFlowRcvrAddress, sFlowAgentAddressType=sFlowAgentAddressType, sFlowRcvrTable=sFlowRcvrTable, sFlowFsTable=sFlowFsTable, sFlowMIB=sFlowMIB, sFlowCpTable=sFlowCpTable, sFlowFsDataSource=sFlowFsDataSource, sFlowFsMaximumHeaderSize=sFlowFsMaximumHeaderSize, sFlowRcvrDatagramVersion=sFlowRcvrDatagramVersion, sFlowRcvrAddressType=sFlowRcvrAddressType, sFlowCpInstance=sFlowCpInstance, sFlowCompliance=sFlowCompliance, sFlowRcvrEntry=sFlowRcvrEntry, sFlowMIBGroups=sFlowMIBGroups, sFlowAgentGroup=sFlowAgentGroup, sFlowCpReceiver=sFlowCpReceiver, sFlowRcvrTimeout=sFlowRcvrTimeout, sFlowVersion=sFlowVersion, sFlowFsPacketSamplingRate=sFlowFsPacketSamplingRate, SFlowDataSource=SFlowDataSource)
