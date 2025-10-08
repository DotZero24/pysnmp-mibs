#
# PySNMP MIB module CISCO-FABRIC-MCAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-FABRIC-MCAST-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:28:59 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entLogicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entLogicalIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoFabricMcastMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 255))
ciscoFabricMcastMIB.setRevisions(('2002-08-20 00:00',))
if mibBuilder.loadTexts: ciscoFabricMcastMIB.setLastUpdated('200208200000Z')
if mibBuilder.loadTexts: ciscoFabricMcastMIB.setOrganization('Cisco Systems, Inc.')
ciscoFabricMcastMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 255, 0))
ciscoFabricMcastMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 255, 1))
ciscoFabricMcastMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 255, 2))
cfmGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 1))
cfmPool = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 2))
cfmLr = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 3))
class CfmPoolIndex(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

cfmGenInfoTotalFgids = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 1, 1), Gauge32()).setUnits('fgid').setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmGenInfoTotalFgids.setStatus('current')
cfmGenInfoInuseFgids = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 1, 2), Gauge32()).setUnits('fgid').setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmGenInfoInuseFgids.setStatus('current')
cfmGenInfoHighWaterInuseFgids = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 1, 3), Gauge32()).setUnits('fgid').setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmGenInfoHighWaterInuseFgids.setStatus('current')
cfmPoolTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 2, 1), )
if mibBuilder.loadTexts: cfmPoolTable.setStatus('current')
cfmPoolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-FABRIC-MCAST-MIB", "cfmPoolId"))
if mibBuilder.loadTexts: cfmPoolEntry.setStatus('current')
cfmPoolId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 2, 1, 1, 1), CfmPoolIndex())
if mibBuilder.loadTexts: cfmPoolId.setStatus('current')
cfmPoolName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 2, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmPoolName.setStatus('current')
cfmPoolType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("shared", 1), ("dedicated", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmPoolType.setStatus('current')
cfmPoolTotalFgids = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 2, 1, 1, 4), Gauge32()).setUnits('fgid').setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmPoolTotalFgids.setStatus('current')
cfmPoolInuseFgids = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 2, 1, 1, 5), Gauge32()).setUnits('fgid').setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmPoolInuseFgids.setStatus('current')
cfmPoolHighWaterInuseFgids = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 2, 1, 1, 6), Gauge32()).setUnits('fgid').setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmPoolHighWaterInuseFgids.setStatus('current')
cfmLrTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 3, 1), )
if mibBuilder.loadTexts: cfmLrTable.setStatus('current')
cfmLrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 3, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entLogicalIndex"))
if mibBuilder.loadTexts: cfmLrEntry.setStatus('current')
cfmLrInuseFgids = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 3, 1, 1, 1), Gauge32()).setUnits('fgid').setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmLrInuseFgids.setStatus('current')
cfmLrHighWaterInuseFgids = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 255, 1, 3, 1, 1, 2), Gauge32()).setUnits('fgid').setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmLrHighWaterInuseFgids.setStatus('current')
cfmMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 255, 2, 1))
cfmMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 255, 2, 2))
cfmMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 255, 2, 1, 1)).setObjects(("CISCO-FABRIC-MCAST-MIB", "cfmGenInfoGroup"), ("CISCO-FABRIC-MCAST-MIB", "cfmPoolGroup"), ("CISCO-FABRIC-MCAST-MIB", "cfmLrGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmMIBCompliance = cfmMIBCompliance.setStatus('current')
cfmGenInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 255, 2, 2, 1)).setObjects(("CISCO-FABRIC-MCAST-MIB", "cfmGenInfoTotalFgids"), ("CISCO-FABRIC-MCAST-MIB", "cfmGenInfoInuseFgids"), ("CISCO-FABRIC-MCAST-MIB", "cfmGenInfoHighWaterInuseFgids"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmGenInfoGroup = cfmGenInfoGroup.setStatus('current')
cfmPoolGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 255, 2, 2, 2)).setObjects(("CISCO-FABRIC-MCAST-MIB", "cfmPoolName"), ("CISCO-FABRIC-MCAST-MIB", "cfmPoolType"), ("CISCO-FABRIC-MCAST-MIB", "cfmPoolTotalFgids"), ("CISCO-FABRIC-MCAST-MIB", "cfmPoolInuseFgids"), ("CISCO-FABRIC-MCAST-MIB", "cfmPoolHighWaterInuseFgids"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmPoolGroup = cfmPoolGroup.setStatus('current')
cfmLrGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 255, 2, 2, 3)).setObjects(("CISCO-FABRIC-MCAST-MIB", "cfmLrInuseFgids"), ("CISCO-FABRIC-MCAST-MIB", "cfmLrHighWaterInuseFgids"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmLrGroup = cfmLrGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-FABRIC-MCAST-MIB", cfmGeneral=cfmGeneral, cfmLr=cfmLr, cfmGenInfoTotalFgids=cfmGenInfoTotalFgids, cfmPoolHighWaterInuseFgids=cfmPoolHighWaterInuseFgids, cfmLrEntry=cfmLrEntry, ciscoFabricMcastMIBConform=ciscoFabricMcastMIBConform, cfmMIBCompliances=cfmMIBCompliances, cfmMIBCompliance=cfmMIBCompliance, cfmPoolTable=cfmPoolTable, cfmLrInuseFgids=cfmLrInuseFgids, cfmLrGroup=cfmLrGroup, cfmGenInfoInuseFgids=cfmGenInfoInuseFgids, cfmPool=cfmPool, ciscoFabricMcastMIBNotifs=ciscoFabricMcastMIBNotifs, cfmLrHighWaterInuseFgids=cfmLrHighWaterInuseFgids, ciscoFabricMcastMIB=ciscoFabricMcastMIB, PYSNMP_MODULE_ID=ciscoFabricMcastMIB, cfmLrTable=cfmLrTable, cfmPoolInuseFgids=cfmPoolInuseFgids, cfmPoolId=cfmPoolId, ciscoFabricMcastMIBObjects=ciscoFabricMcastMIBObjects, cfmMIBGroups=cfmMIBGroups, cfmGenInfoGroup=cfmGenInfoGroup, cfmPoolType=cfmPoolType, cfmPoolTotalFgids=cfmPoolTotalFgids, cfmPoolName=cfmPoolName, cfmGenInfoHighWaterInuseFgids=cfmGenInfoHighWaterInuseFgids, cfmPoolGroup=cfmPoolGroup, cfmPoolEntry=cfmPoolEntry, CfmPoolIndex=CfmPoolIndex)
