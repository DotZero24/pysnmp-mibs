#
# PySNMP MIB module CISCO-GPRS-ISGSN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-GPRS-ISGSN-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:12:46 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoGprsIsgsnMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 9992))
if mibBuilder.loadTexts: ciscoGprsIsgsnMIB.setLastUpdated('9810150000Z')
if mibBuilder.loadTexts: ciscoGprsIsgsnMIB.setOrganization('Cisco Systems, Inc.')
ciscoGprsIsgsnMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9992, 1))
ciscoGprsIsgsnStats = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9992, 1, 1))
cgprsIsgsnRxPacketCountFromTnode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9992, 1, 1, 1), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgprsIsgsnRxPacketCountFromTnode.setStatus('current')
cgprsIsgsnTxPacketCountToTnode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9992, 1, 1, 2), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgprsIsgsnTxPacketCountToTnode.setStatus('current')
cgprsIsgsnRxOctetCountFromTnode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9992, 1, 1, 3), Counter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgprsIsgsnRxOctetCountFromTnode.setStatus('current')
cgprsIsgsnTxOctetCountToTnode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9992, 1, 1, 4), Counter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgprsIsgsnTxOctetCountToTnode.setStatus('current')
cgprsIsgsnErrorCountRxFromTnode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9992, 1, 1, 5), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgprsIsgsnErrorCountRxFromTnode.setStatus('current')
cgprsIsgsnErrorCountRxToTnode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9992, 1, 1, 6), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgprsIsgsnErrorCountRxToTnode.setStatus('current')
ciscoGprsIsgsnConformances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9992, 3))
cgprsIsgsnGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9992, 3, 1))
cgprsIsgsnCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9992, 3, 2))
cgprsIsgsnCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 9992, 3, 2, 1)).setObjects(("CISCO-GPRS-ISGSN-MIB", "cgprsIsgsnStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cgprsIsgsnCompliance1 = cgprsIsgsnCompliance1.setStatus('current')
cgprsIsgsnStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 9992, 3, 1, 1)).setObjects(("CISCO-GPRS-ISGSN-MIB", "cgprsIsgsnRxPacketCountFromTnode"), ("CISCO-GPRS-ISGSN-MIB", "cgprsIsgsnTxPacketCountToTnode"), ("CISCO-GPRS-ISGSN-MIB", "cgprsIsgsnRxOctetCountFromTnode"), ("CISCO-GPRS-ISGSN-MIB", "cgprsIsgsnTxOctetCountToTnode"), ("CISCO-GPRS-ISGSN-MIB", "cgprsIsgsnErrorCountRxFromTnode"), ("CISCO-GPRS-ISGSN-MIB", "cgprsIsgsnErrorCountRxToTnode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cgprsIsgsnStatsGroup = cgprsIsgsnStatsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-GPRS-ISGSN-MIB", cgprsIsgsnTxOctetCountToTnode=cgprsIsgsnTxOctetCountToTnode, cgprsIsgsnCompliance1=cgprsIsgsnCompliance1, cgprsIsgsnCompliances=cgprsIsgsnCompliances, cgprsIsgsnStatsGroup=cgprsIsgsnStatsGroup, cgprsIsgsnRxOctetCountFromTnode=cgprsIsgsnRxOctetCountFromTnode, cgprsIsgsnErrorCountRxToTnode=cgprsIsgsnErrorCountRxToTnode, cgprsIsgsnErrorCountRxFromTnode=cgprsIsgsnErrorCountRxFromTnode, ciscoGprsIsgsnConformances=ciscoGprsIsgsnConformances, PYSNMP_MODULE_ID=ciscoGprsIsgsnMIB, ciscoGprsIsgsnStats=ciscoGprsIsgsnStats, ciscoGprsIsgsnMIB=ciscoGprsIsgsnMIB, cgprsIsgsnRxPacketCountFromTnode=cgprsIsgsnRxPacketCountFromTnode, cgprsIsgsnTxPacketCountToTnode=cgprsIsgsnTxPacketCountToTnode, ciscoGprsIsgsnMIBObjects=ciscoGprsIsgsnMIBObjects, cgprsIsgsnGroups=cgprsIsgsnGroups)
