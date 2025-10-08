#
# PySNMP MIB module DCP-TOPOLOGY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/smartoptics/DCP-TOPOLOGY-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:07:35 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dcpGeneric, = mibBuilder.importSymbols("DCP-MIB", "dcpGeneric")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("DCP-TOPOLOGY-MIB", PYSNMP_MODULE_ID=dcpTopology, dcpTopologyInternalTable=dcpTopologyInternalTable, dcpTopologyBasicComplV1=dcpTopologyBasicComplV1, dcpTopologyInternalDestination=dcpTopologyInternalDestination, dcpTopologyInternalSource=dcpTopologyInternalSource, dcpTopologyMIBGroups=dcpTopologyMIBGroups, dcpTopologyMIBCompliances=dcpTopologyMIBCompliances, dcpTopologyTableGroupV1=dcpTopologyTableGroupV1, dcpTopologyInternalEntry=dcpTopologyInternalEntry, dcpTopologyInternalId=dcpTopologyInternalId, dcpTopology=dcpTopology, dcpTopologyMIBCompliance=dcpTopologyMIBCompliance, dcpTopologyObjects=dcpTopologyObjects)
