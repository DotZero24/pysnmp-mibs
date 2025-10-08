#
# PySNMP MIB module CISCO-CAR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-CAR-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:15:54 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCarMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 113))
ciscoCarMIB.setRevisions(('1997-07-18 00:00', '1900-02-18 00:00',))
if mibBuilder.loadTexts: ciscoCarMIB.setLastUpdated('0002180000Z')
if mibBuilder.loadTexts: ciscoCarMIB.setOrganization('Cisco Systems, Inc.')
ciscoCarMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 113, 1))
ccarConfigs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 1))
ccarStats = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 2))
class PacketSource(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("input", 1), ("output", 2))

class RateLimitType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("all", 1), ("quickAcc", 2), ("standardAcc", 3))

class RateLimitAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("drop", 1), ("xmit", 2), ("continue", 3), ("precedXmit", 4), ("precedCont", 5))

ccarConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 1, 1), )
if mibBuilder.loadTexts: ccarConfigTable.setStatus('current')
ccarConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-CAR-MIB", "ccarConfigDirection"), (0, "CISCO-CAR-MIB", "ccarConfigRowIndex"))
if mibBuilder.loadTexts: ccarConfigEntry.setStatus('current')
ccarConfigDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 1, 1, 1, 1), PacketSource())
if mibBuilder.loadTexts: ccarConfigDirection.setStatus('current')
ccarConfigRowIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ccarConfigRowIndex.setStatus('current')
ccarConfigType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 1, 1, 1, 3), RateLimitType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccarConfigType.setStatus('current')
ccarConfigAccIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccarConfigAccIdx.setStatus('current')
ccarConfigRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 1, 1, 1, 5), Integer32()).setUnits('bits/second').setMaxAccess("readonly")
if mibBuilder.loadTexts: ccarConfigRate.setStatus('current')
ccarConfigLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 1, 1, 1, 6), Integer32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ccarConfigLimit.setStatus('current')
ccarConfigExtLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 1, 1, 1, 7), Integer32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ccarConfigExtLimit.setStatus('current')
ccarConfigConformAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 1, 1, 1, 8), RateLimitAction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccarConfigConformAction.setStatus('current')
ccarConfigExceedAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 1, 1, 1, 9), RateLimitAction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccarConfigExceedAction.setStatus('current')
ccarStatTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 2, 1), )
if mibBuilder.loadTexts: ccarStatTable.setStatus('current')
ccarStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 2, 1, 1), )
ccarConfigEntry.registerAugmentions(("CISCO-CAR-MIB", "ccarStatEntry"))
ccarStatEntry.setIndexNames(*ccarConfigEntry.getIndexNames())
if mibBuilder.loadTexts: ccarStatEntry.setStatus('current')
ccarStatSwitchedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 2, 1, 1, 1), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: ccarStatSwitchedPkts.setStatus('current')
ccarStatSwitchedBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 2, 1, 1, 2), Counter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ccarStatSwitchedBytes.setStatus('current')
ccarStatFilteredPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 2, 1, 1, 3), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: ccarStatFilteredPkts.setStatus('current')
ccarStatFilteredBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 2, 1, 1, 4), Counter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ccarStatFilteredBytes.setStatus('current')
ccarStatCurBurst = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 2, 1, 1, 5), Gauge32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ccarStatCurBurst.setStatus('current')
ccarStatSwitchedPktsOverflow = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 2, 1, 1, 6), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: ccarStatSwitchedPktsOverflow.setStatus('current')
ccarStatSwitchedBytesOverflow = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 2, 1, 1, 7), Counter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ccarStatSwitchedBytesOverflow.setStatus('current')
ccarStatFilteredPktsOverflow = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 2, 1, 1, 8), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: ccarStatFilteredPktsOverflow.setStatus('current')
ccarStatFilteredBytesOverflow = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 2, 1, 1, 9), Counter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ccarStatFilteredBytesOverflow.setStatus('current')
ccarStatHCSwitchedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 2, 1, 1, 10), Counter64()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: ccarStatHCSwitchedPkts.setStatus('current')
ccarStatHCSwitchedBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 2, 1, 1, 11), Counter64()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ccarStatHCSwitchedBytes.setStatus('current')
ccarStatHCFilteredPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 2, 1, 1, 12), Counter64()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: ccarStatHCFilteredPkts.setStatus('current')
ccarStatHCFilteredBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 2, 1, 1, 13), Counter64()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ccarStatHCFilteredBytes.setStatus('current')
ciscoCarMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 113, 3))
ciscoCarMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 113, 3, 1))
ciscoCarMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 113, 3, 2))
ciscoCarMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 113, 3, 1, 1)).setObjects(("CISCO-CAR-MIB", "ciscoCarMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCarMIBCompliance = ciscoCarMIBCompliance.setStatus('current')
ciscoCarMIBComplianceHCCounters = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 113, 3, 1, 2)).setObjects(("CISCO-CAR-MIB", "ciscoCarMIBGroup"), ("CISCO-CAR-MIB", "ciscoCarMIBHCGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCarMIBComplianceHCCounters = ciscoCarMIBComplianceHCCounters.setStatus('current')
ciscoCarMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 113, 3, 2, 1)).setObjects(("CISCO-CAR-MIB", "ccarConfigType"), ("CISCO-CAR-MIB", "ccarConfigAccIdx"), ("CISCO-CAR-MIB", "ccarConfigRate"), ("CISCO-CAR-MIB", "ccarConfigLimit"), ("CISCO-CAR-MIB", "ccarConfigExtLimit"), ("CISCO-CAR-MIB", "ccarConfigConformAction"), ("CISCO-CAR-MIB", "ccarConfigExceedAction"), ("CISCO-CAR-MIB", "ccarStatSwitchedPkts"), ("CISCO-CAR-MIB", "ccarStatSwitchedBytes"), ("CISCO-CAR-MIB", "ccarStatFilteredPkts"), ("CISCO-CAR-MIB", "ccarStatFilteredBytes"), ("CISCO-CAR-MIB", "ccarStatCurBurst"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCarMIBGroup = ciscoCarMIBGroup.setStatus('current')
ciscoCarMIBHCGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 113, 3, 2, 2)).setObjects(("CISCO-CAR-MIB", "ccarStatSwitchedPktsOverflow"), ("CISCO-CAR-MIB", "ccarStatSwitchedBytesOverflow"), ("CISCO-CAR-MIB", "ccarStatFilteredPktsOverflow"), ("CISCO-CAR-MIB", "ccarStatFilteredBytesOverflow"), ("CISCO-CAR-MIB", "ccarStatHCSwitchedPkts"), ("CISCO-CAR-MIB", "ccarStatHCSwitchedBytes"), ("CISCO-CAR-MIB", "ccarStatHCFilteredPkts"), ("CISCO-CAR-MIB", "ccarStatHCFilteredBytes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCarMIBHCGroup = ciscoCarMIBHCGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-CAR-MIB", ciscoCarMIBGroups=ciscoCarMIBGroups, ccarConfigRowIndex=ccarConfigRowIndex, ccarStatSwitchedPktsOverflow=ccarStatSwitchedPktsOverflow, ciscoCarMIBObjects=ciscoCarMIBObjects, ccarConfigExceedAction=ccarConfigExceedAction, ccarStatFilteredPkts=ccarStatFilteredPkts, ciscoCarMIBComplianceHCCounters=ciscoCarMIBComplianceHCCounters, ccarConfigDirection=ccarConfigDirection, ccarConfigRate=ccarConfigRate, ccarStatFilteredBytes=ccarStatFilteredBytes, ccarStatHCFilteredBytes=ccarStatHCFilteredBytes, RateLimitType=RateLimitType, ccarStatSwitchedBytes=ccarStatSwitchedBytes, ccarStatEntry=ccarStatEntry, ccarStatTable=ccarStatTable, ccarConfigs=ccarConfigs, ccarStatHCSwitchedPkts=ccarStatHCSwitchedPkts, ccarConfigTable=ccarConfigTable, ccarConfigLimit=ccarConfigLimit, ccarConfigConformAction=ccarConfigConformAction, ccarStatFilteredPktsOverflow=ccarStatFilteredPktsOverflow, ccarStatHCSwitchedBytes=ccarStatHCSwitchedBytes, ccarConfigExtLimit=ccarConfigExtLimit, ccarStatFilteredBytesOverflow=ccarStatFilteredBytesOverflow, PYSNMP_MODULE_ID=ciscoCarMIB, ccarStatSwitchedBytesOverflow=ccarStatSwitchedBytesOverflow, ciscoCarMIBCompliance=ciscoCarMIBCompliance, ciscoCarMIBConformance=ciscoCarMIBConformance, ccarConfigEntry=ccarConfigEntry, RateLimitAction=RateLimitAction, ciscoCarMIBGroup=ciscoCarMIBGroup, ccarStatCurBurst=ccarStatCurBurst, ciscoCarMIBCompliances=ciscoCarMIBCompliances, ccarStatSwitchedPkts=ccarStatSwitchedPkts, PacketSource=PacketSource, ccarConfigType=ccarConfigType, ciscoCarMIB=ciscoCarMIB, ccarStatHCFilteredPkts=ccarStatHCFilteredPkts, ciscoCarMIBHCGroup=ciscoCarMIBHCGroup, ccarConfigAccIdx=ccarConfigAccIdx, ccarStats=ccarStats)
