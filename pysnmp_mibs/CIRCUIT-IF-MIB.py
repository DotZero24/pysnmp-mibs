#
# PySNMP MIB module CIRCUIT-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/rfc/CIRCUIT-IF-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:49:56 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, mib_2, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "mib-2", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, StorageType, RowPointer, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "StorageType", "RowPointer", "TimeStamp", "DisplayString")
circuitIfMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 94))
circuitIfMIB.setRevisions(('2002-01-03 00:00',))
if mibBuilder.loadTexts: circuitIfMIB.setLastUpdated('200201030000Z')
if mibBuilder.loadTexts: circuitIfMIB.setOrganization('IETF Frame Relay Service MIB Working Group')
class CiFlowDirection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("transmit", 1), ("receive", 2), ("both", 3))

ciObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 94, 1))
ciCapabilities = MibIdentifier((1, 3, 6, 1, 2, 1, 94, 2))
ciConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 94, 3))
ciCircuitTable = MibTable((1, 3, 6, 1, 2, 1, 94, 1, 1), )
if mibBuilder.loadTexts: ciCircuitTable.setStatus('current')
ciCircuitEntry = MibTableRow((1, 3, 6, 1, 2, 1, 94, 1, 1, 1), ).setIndexNames((0, "CIRCUIT-IF-MIB", "ciCircuitObject"), (0, "CIRCUIT-IF-MIB", "ciCircuitFlow"))
if mibBuilder.loadTexts: ciCircuitEntry.setStatus('current')
ciCircuitObject = MibTableColumn((1, 3, 6, 1, 2, 1, 94, 1, 1, 1, 1), RowPointer())
if mibBuilder.loadTexts: ciCircuitObject.setStatus('current')
ciCircuitFlow = MibTableColumn((1, 3, 6, 1, 2, 1, 94, 1, 1, 1, 2), CiFlowDirection())
if mibBuilder.loadTexts: ciCircuitFlow.setStatus('current')
ciCircuitStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 94, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciCircuitStatus.setStatus('current')
ciCircuitIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 94, 1, 1, 1, 4), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciCircuitIfIndex.setStatus('current')
ciCircuitCreateTime = MibTableColumn((1, 3, 6, 1, 2, 1, 94, 1, 1, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciCircuitCreateTime.setStatus('current')
ciCircuitStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 94, 1, 1, 1, 6), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciCircuitStorageType.setStatus('current')
ciIfMapTable = MibTable((1, 3, 6, 1, 2, 1, 94, 1, 2), )
if mibBuilder.loadTexts: ciIfMapTable.setStatus('current')
ciIfMapEntry = MibTableRow((1, 3, 6, 1, 2, 1, 94, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ciIfMapEntry.setStatus('current')
ciIfMapObject = MibTableColumn((1, 3, 6, 1, 2, 1, 94, 1, 2, 1, 1), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciIfMapObject.setStatus('current')
ciIfMapFlow = MibTableColumn((1, 3, 6, 1, 2, 1, 94, 1, 2, 1, 2), CiFlowDirection()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciIfMapFlow.setStatus('current')
ciIfLastChange = MibScalar((1, 3, 6, 1, 2, 1, 94, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciIfLastChange.setStatus('current')
ciIfNumActive = MibScalar((1, 3, 6, 1, 2, 1, 94, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciIfNumActive.setStatus('current')
ciMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 94, 3, 1))
ciMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 94, 3, 2))
ciCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 94, 3, 2, 1)).setObjects(("CIRCUIT-IF-MIB", "ciCircuitGroup"), ("CIRCUIT-IF-MIB", "ciIfMapGroup"), ("CIRCUIT-IF-MIB", "ciStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciCompliance = ciCompliance.setStatus('current')
ciCircuitGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 94, 3, 1, 1)).setObjects(("CIRCUIT-IF-MIB", "ciCircuitStatus"), ("CIRCUIT-IF-MIB", "ciCircuitIfIndex"), ("CIRCUIT-IF-MIB", "ciCircuitCreateTime"), ("CIRCUIT-IF-MIB", "ciCircuitStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciCircuitGroup = ciCircuitGroup.setStatus('current')
ciIfMapGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 94, 3, 1, 2)).setObjects(("CIRCUIT-IF-MIB", "ciIfMapObject"), ("CIRCUIT-IF-MIB", "ciIfMapFlow"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciIfMapGroup = ciIfMapGroup.setStatus('current')
ciStatsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 94, 3, 1, 3)).setObjects(("CIRCUIT-IF-MIB", "ciIfLastChange"), ("CIRCUIT-IF-MIB", "ciIfNumActive"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciStatsGroup = ciStatsGroup.setStatus('current')
mibBuilder.exportSymbols("CIRCUIT-IF-MIB", ciObjects=ciObjects, ciCircuitCreateTime=ciCircuitCreateTime, ciConformance=ciConformance, ciCircuitStatus=ciCircuitStatus, ciCompliance=ciCompliance, ciIfMapTable=ciIfMapTable, ciIfLastChange=ciIfLastChange, circuitIfMIB=circuitIfMIB, ciIfMapObject=ciIfMapObject, ciCircuitEntry=ciCircuitEntry, ciIfMapGroup=ciIfMapGroup, ciIfMapEntry=ciIfMapEntry, ciCapabilities=ciCapabilities, ciCircuitFlow=ciCircuitFlow, ciCircuitTable=ciCircuitTable, ciCircuitObject=ciCircuitObject, CiFlowDirection=CiFlowDirection, ciStatsGroup=ciStatsGroup, ciIfNumActive=ciIfNumActive, PYSNMP_MODULE_ID=circuitIfMIB, ciMIBCompliances=ciMIBCompliances, ciCircuitIfIndex=ciCircuitIfIndex, ciCircuitGroup=ciCircuitGroup, ciCircuitStorageType=ciCircuitStorageType, ciIfMapFlow=ciIfMapFlow, ciMIBGroups=ciMIBGroups)
