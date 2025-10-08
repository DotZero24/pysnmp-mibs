#
# PySNMP MIB module DCP-TOPOLOGY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/smartoptics/DCP-TOPOLOGY-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:02:01 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dcpGeneric, = mibBuilder.importSymbols("DCP-MIB", "dcpGeneric")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dcpTopology = ModuleIdentity((1, 3, 6, 1, 4, 1, 30826, 2, 2, 5))
dcpTopology.setRevisions(('2021-12-30 08:00',))
if mibBuilder.loadTexts: dcpTopology.setLastUpdated('202112300800Z')
if mibBuilder.loadTexts: dcpTopology.setOrganization('Smartoptics.')
dcpTopologyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 30826, 2, 2, 5, 1))
dcpTopologyInternalTable = MibTable((1, 3, 6, 1, 4, 1, 30826, 2, 2, 5, 1, 1), )
if mibBuilder.loadTexts: dcpTopologyInternalTable.setStatus('current')
dcpTopologyInternalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30826, 2, 2, 5, 1, 1, 1), ).setIndexNames((0, "DCP-TOPOLOGY-MIB", "dcpTopologyInternalId"))
if mibBuilder.loadTexts: dcpTopologyInternalEntry.setStatus('current')
dcpTopologyInternalId = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 2, 2, 5, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000000)))
if mibBuilder.loadTexts: dcpTopologyInternalId.setStatus('current')
dcpTopologyInternalSource = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 2, 2, 5, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcpTopologyInternalSource.setStatus('current')
dcpTopologyInternalDestination = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 2, 2, 5, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcpTopologyInternalDestination.setStatus('current')
dcpTopologyMIBCompliance = MibIdentifier((1, 3, 6, 1, 4, 1, 30826, 2, 2, 5, 2))
dcpTopologyMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30826, 2, 2, 5, 2, 1))
dcpTopologyTableGroupV1 = ObjectGroup((1, 3, 6, 1, 4, 1, 30826, 2, 2, 5, 2, 1, 1)).setObjects(("DCP-TOPOLOGY-MIB", "dcpTopologyInternalSource"), ("DCP-TOPOLOGY-MIB", "dcpTopologyInternalDestination"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dcpTopologyTableGroupV1 = dcpTopologyTableGroupV1.setStatus('current')
dcpTopologyMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30826, 2, 2, 5, 2, 2))
dcpTopologyBasicComplV1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 30826, 2, 2, 5, 2, 2, 1)).setObjects(("DCP-TOPOLOGY-MIB", "dcpTopologyTableGroupV1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dcpTopologyBasicComplV1 = dcpTopologyBasicComplV1.setStatus('current')
mibBuilder.exportSymbols("DCP-TOPOLOGY-MIB", dcpTopologyMIBCompliances=dcpTopologyMIBCompliances, dcpTopologyInternalSource=dcpTopologyInternalSource, dcpTopologyInternalId=dcpTopologyInternalId, dcpTopologyMIBGroups=dcpTopologyMIBGroups, dcpTopology=dcpTopology, dcpTopologyInternalDestination=dcpTopologyInternalDestination, PYSNMP_MODULE_ID=dcpTopology, dcpTopologyBasicComplV1=dcpTopologyBasicComplV1, dcpTopologyInternalTable=dcpTopologyInternalTable, dcpTopologyObjects=dcpTopologyObjects, dcpTopologyInternalEntry=dcpTopologyInternalEntry, dcpTopologyTableGroupV1=dcpTopologyTableGroupV1, dcpTopologyMIBCompliance=dcpTopologyMIBCompliance)
