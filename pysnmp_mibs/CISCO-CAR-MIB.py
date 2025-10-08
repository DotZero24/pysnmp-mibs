#
# PySNMP MIB module CISCO-CAR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-CAR-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:31:31 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
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
mibBuilder.exportSymbols("CISCO-CAR-MIB", ciscoCarMIBConformance=ciscoCarMIBConformance, PacketSource=PacketSource, ccarStatHCFilteredPkts=ccarStatHCFilteredPkts, ccarConfigLimit=ccarConfigLimit, ccarStatFilteredBytesOverflow=ccarStatFilteredBytesOverflow, ciscoCarMIBGroup=ciscoCarMIBGroup, ccarConfigAccIdx=ccarConfigAccIdx, ccarConfigExtLimit=ccarConfigExtLimit, ccarConfigs=ccarConfigs, ccarStatTable=ccarStatTable, PYSNMP_MODULE_ID=ciscoCarMIB, ciscoCarMIBComplianceHCCounters=ciscoCarMIBComplianceHCCounters, ccarConfigRowIndex=ccarConfigRowIndex, ccarConfigRate=ccarConfigRate, ccarStatSwitchedPkts=ccarStatSwitchedPkts, ccarStatCurBurst=ccarStatCurBurst, RateLimitType=RateLimitType, ciscoCarMIBGroups=ciscoCarMIBGroups, ccarStatHCSwitchedPkts=ccarStatHCSwitchedPkts, ccarConfigDirection=ccarConfigDirection, ccarConfigTable=ccarConfigTable, ccarConfigConformAction=ccarConfigConformAction, ccarStatFilteredBytes=ccarStatFilteredBytes, ccarStatSwitchedBytesOverflow=ccarStatSwitchedBytesOverflow, ciscoCarMIBObjects=ciscoCarMIBObjects, ciscoCarMIB=ciscoCarMIB, ciscoCarMIBCompliance=ciscoCarMIBCompliance, ccarStatSwitchedBytes=ccarStatSwitchedBytes, ccarConfigEntry=ccarConfigEntry, ciscoCarMIBHCGroup=ciscoCarMIBHCGroup, ccarStatSwitchedPktsOverflow=ccarStatSwitchedPktsOverflow, ccarStatEntry=ccarStatEntry, ccarStatHCFilteredBytes=ccarStatHCFilteredBytes, ccarConfigType=ccarConfigType, ccarStatFilteredPkts=ccarStatFilteredPkts, ciscoCarMIBCompliances=ciscoCarMIBCompliances, ccarConfigExceedAction=ccarConfigExceedAction, ccarStats=ccarStats, RateLimitAction=RateLimitAction, ccarStatFilteredPktsOverflow=ccarStatFilteredPktsOverflow, ccarStatHCSwitchedBytes=ccarStatHCSwitchedBytes)
