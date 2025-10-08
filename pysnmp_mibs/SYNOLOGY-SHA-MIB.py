#
# PySNMP MIB module SYNOLOGY-SHA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/synology/SYNOLOGY-SHA-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:56:53 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
synologyHA = ModuleIdentity((1, 3, 6, 1, 4, 1, 6574, 106))
synologyHA.setRevisions(('2018-07-25 00:00',))
if mibBuilder.loadTexts: synologyHA.setLastUpdated('201807250000Z')
if mibBuilder.loadTexts: synologyHA.setOrganization('www.synology.com')
synology = MibIdentifier((1, 3, 6, 1, 4, 1, 6574))
class HostName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class ClusterStatusType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("normal", 0), ("warning", 1), ("critical", 2), ("upgrading", 3), ("processing", 4))

class HeartbeatStatusType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("normal", 0), ("abnormal", 1), ("disconnected", 2), ("empty", 3))

activeNodeName = MibScalar((1, 3, 6, 1, 4, 1, 6574, 106, 1), HostName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: activeNodeName.setStatus('current')
passiveNodeName = MibScalar((1, 3, 6, 1, 4, 1, 6574, 106, 2), HostName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: passiveNodeName.setStatus('current')
clusterAutoFailover = MibScalar((1, 3, 6, 1, 4, 1, 6574, 106, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterAutoFailover.setStatus('current')
clusterName = MibScalar((1, 3, 6, 1, 4, 1, 6574, 106, 4), HostName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterName.setStatus('current')
clusterStatus = MibScalar((1, 3, 6, 1, 4, 1, 6574, 106, 5), ClusterStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterStatus.setStatus('current')
heartbeatStatus = MibScalar((1, 3, 6, 1, 4, 1, 6574, 106, 6), HeartbeatStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: heartbeatStatus.setStatus('current')
heartbeatTxRate = MibScalar((1, 3, 6, 1, 4, 1, 6574, 106, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: heartbeatTxRate.setStatus('current')
heartbeatLatency = MibScalar((1, 3, 6, 1, 4, 1, 6574, 106, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: heartbeatLatency.setStatus('current')
synologyHAConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 106, 9))
synologyHACompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 106, 9, 1))
synologyHAGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 106, 9, 2))
synologyHACompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6574, 106, 9, 1, 1)).setObjects(("SYNOLOGY-SHA-MIB", "synologyHAGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    synologyHACompliance = synologyHACompliance.setStatus('current')
synologyHAGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6574, 106, 9, 2, 1)).setObjects(("SYNOLOGY-SHA-MIB", "activeNodeName"), ("SYNOLOGY-SHA-MIB", "passiveNodeName"), ("SYNOLOGY-SHA-MIB", "clusterAutoFailover"), ("SYNOLOGY-SHA-MIB", "clusterName"), ("SYNOLOGY-SHA-MIB", "clusterStatus"), ("SYNOLOGY-SHA-MIB", "heartbeatStatus"), ("SYNOLOGY-SHA-MIB", "heartbeatTxRate"), ("SYNOLOGY-SHA-MIB", "heartbeatLatency"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    synologyHAGroup = synologyHAGroup.setStatus('current')
mibBuilder.exportSymbols("SYNOLOGY-SHA-MIB", passiveNodeName=passiveNodeName, ClusterStatusType=ClusterStatusType, clusterName=clusterName, activeNodeName=activeNodeName, heartbeatStatus=heartbeatStatus, clusterAutoFailover=clusterAutoFailover, synology=synology, synologyHA=synologyHA, synologyHACompliances=synologyHACompliances, PYSNMP_MODULE_ID=synologyHA, heartbeatLatency=heartbeatLatency, synologyHAGroup=synologyHAGroup, HostName=HostName, synologyHACompliance=synologyHACompliance, clusterStatus=clusterStatus, heartbeatTxRate=heartbeatTxRate, synologyHAConformance=synologyHAConformance, HeartbeatStatusType=HeartbeatStatusType, synologyHAGroups=synologyHAGroups)
