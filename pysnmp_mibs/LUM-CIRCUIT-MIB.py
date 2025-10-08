#
# PySNMP MIB module LUM-CIRCUIT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/LUM-CIRCUIT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:21:11 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
lumCircuitMIB, lumModules = mibBuilder.importSymbols("LUM-REG", "lumCircuitMIB", "lumModules")
FaultStatus, MgmtNameString = mibBuilder.importSymbols("LUM-TC", "FaultStatus", "MgmtNameString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
lumCircuitMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 8708, 1, 1, 30))
lumCircuitMIBModule.setRevisions(('2017-06-15 00:00', '2011-03-24 00:00',))
if mibBuilder.loadTexts: lumCircuitMIBModule.setLastUpdated('201706150000Z')
if mibBuilder.loadTexts: lumCircuitMIBModule.setOrganization('Infinera Corporation')
lumCircuitConfs = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 30, 1))
lumCircuitGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 30, 1, 1))
lumCircuitCompl = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 30, 1, 2))
lumCircuitMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 30, 2))
circuitGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 1))
circuitStatusList = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 2))
l2CircuitStatusList = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 3))
circuitGeneralConfigLastChangeTime = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: circuitGeneralConfigLastChangeTime.setStatus('current')
circuitGeneralStateLastChangeTime = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: circuitGeneralStateLastChangeTime.setStatus('current')
circuitGeneralStatusTableSize = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: circuitGeneralStatusTableSize.setStatus('current')
circuitStatusTable = MibTable((1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 2, 1), )
if mibBuilder.loadTexts: circuitStatusTable.setStatus('current')
circuitStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 2, 1, 1), ).setIndexNames((0, "LUM-CIRCUIT-MIB", "circuitStatusIndex"))
if mibBuilder.loadTexts: circuitStatusEntry.setStatus('current')
circuitStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: circuitStatusIndex.setStatus('current')
circuitStatusName = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 2, 1, 1, 2), MgmtNameString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: circuitStatusName.setStatus('current')
circuitStatusDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 2, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: circuitStatusDescription.setStatus('current')
circuitStatusAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("undefined", 0), ("inService", 1), ("maintenance", 2), ("notUsed", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: circuitStatusAdminStatus.setStatus('current')
circuitStatusOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("undefined", 0), ("incomplete", 1), ("down", 2), ("degraded", 3), ("up", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: circuitStatusOperStatus.setStatus('current')
circuitStatusIncomplete = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 2, 1, 1, 6), FaultStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: circuitStatusIncomplete.setStatus('current')
circuitStatusDegraded = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 2, 1, 1, 7), FaultStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: circuitStatusDegraded.setStatus('current')
circuitStatusDown = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 2, 1, 1, 8), FaultStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: circuitStatusDown.setStatus('current')
fdfrStatusTable = MibTable((1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 3, 1), )
if mibBuilder.loadTexts: fdfrStatusTable.setStatus('current')
fdfrStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 3, 1, 1), ).setIndexNames((0, "LUM-CIRCUIT-MIB", "fdfrStatusIndex"))
if mibBuilder.loadTexts: fdfrStatusEntry.setStatus('current')
fdfrStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 3, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdfrStatusIndex.setStatus('current')
fdfrStatusDown = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 3, 1, 1, 2), FaultStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdfrStatusDown.setStatus('current')
fdfrStatusIncomplete = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 3, 1, 1, 3), FaultStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdfrStatusIncomplete.setStatus('current')
fdfrStatusUnexpectedMfdfrType = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 3, 1, 1, 4), FaultStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdfrStatusUnexpectedMfdfrType.setStatus('current')
fdfrStatusDegraded = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 3, 1, 1, 5), FaultStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdfrStatusDegraded.setStatus('current')
fdfrStatusMplsTunnelProtectionFailed = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 3, 1, 1, 6), FaultStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdfrStatusMplsTunnelProtectionFailed.setStatus('current')
fdfrStatusMplsTunnelProtectionDegraded = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 3, 1, 1, 7), FaultStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdfrStatusMplsTunnelProtectionDegraded.setStatus('current')
fdfrStatusUnknown = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 30, 2, 3, 1, 1, 8), FaultStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdfrStatusUnknown.setStatus('current')
circuitGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 30, 1, 1, 1)).setObjects(("LUM-CIRCUIT-MIB", "circuitGeneralConfigLastChangeTime"), ("LUM-CIRCUIT-MIB", "circuitGeneralStateLastChangeTime"), ("LUM-CIRCUIT-MIB", "circuitGeneralStatusTableSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    circuitGeneralGroup = circuitGeneralGroup.setStatus('current')
circuitStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 30, 1, 1, 2)).setObjects(("LUM-CIRCUIT-MIB", "circuitStatusIndex"), ("LUM-CIRCUIT-MIB", "circuitStatusName"), ("LUM-CIRCUIT-MIB", "circuitStatusDescription"), ("LUM-CIRCUIT-MIB", "circuitStatusAdminStatus"), ("LUM-CIRCUIT-MIB", "circuitStatusOperStatus"), ("LUM-CIRCUIT-MIB", "circuitStatusDegraded"), ("LUM-CIRCUIT-MIB", "circuitStatusDown"), ("LUM-CIRCUIT-MIB", "circuitStatusIncomplete"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    circuitStatusGroup = circuitStatusGroup.setStatus('current')
fdfrStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 30, 1, 1, 3)).setObjects(("LUM-CIRCUIT-MIB", "fdfrStatusIndex"), ("LUM-CIRCUIT-MIB", "fdfrStatusDown"), ("LUM-CIRCUIT-MIB", "fdfrStatusIncomplete"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fdfrStatusGroup = fdfrStatusGroup.setStatus('deprecated')
fdfrStatusGroupV2 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 30, 1, 1, 4)).setObjects(("LUM-CIRCUIT-MIB", "fdfrStatusIndex"), ("LUM-CIRCUIT-MIB", "fdfrStatusDown"), ("LUM-CIRCUIT-MIB", "fdfrStatusIncomplete"), ("LUM-CIRCUIT-MIB", "fdfrStatusUnexpectedMfdfrType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fdfrStatusGroupV2 = fdfrStatusGroupV2.setStatus('deprecated')
fdfrStatusGroupV3 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 30, 1, 1, 5)).setObjects(("LUM-CIRCUIT-MIB", "fdfrStatusIndex"), ("LUM-CIRCUIT-MIB", "fdfrStatusDown"), ("LUM-CIRCUIT-MIB", "fdfrStatusIncomplete"), ("LUM-CIRCUIT-MIB", "fdfrStatusUnexpectedMfdfrType"), ("LUM-CIRCUIT-MIB", "fdfrStatusDegraded"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fdfrStatusGroupV3 = fdfrStatusGroupV3.setStatus('deprecated')
fdfrStatusGroupV4 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 30, 1, 1, 6)).setObjects(("LUM-CIRCUIT-MIB", "fdfrStatusIndex"), ("LUM-CIRCUIT-MIB", "fdfrStatusDown"), ("LUM-CIRCUIT-MIB", "fdfrStatusIncomplete"), ("LUM-CIRCUIT-MIB", "fdfrStatusUnexpectedMfdfrType"), ("LUM-CIRCUIT-MIB", "fdfrStatusDegraded"), ("LUM-CIRCUIT-MIB", "fdfrStatusMplsTunnelProtectionFailed"), ("LUM-CIRCUIT-MIB", "fdfrStatusMplsTunnelProtectionDegraded"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fdfrStatusGroupV4 = fdfrStatusGroupV4.setStatus('deprecated')
fdfrStatusGroupV5 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 30, 1, 1, 7)).setObjects(("LUM-CIRCUIT-MIB", "fdfrStatusIndex"), ("LUM-CIRCUIT-MIB", "fdfrStatusDown"), ("LUM-CIRCUIT-MIB", "fdfrStatusIncomplete"), ("LUM-CIRCUIT-MIB", "fdfrStatusUnexpectedMfdfrType"), ("LUM-CIRCUIT-MIB", "fdfrStatusDegraded"), ("LUM-CIRCUIT-MIB", "fdfrStatusMplsTunnelProtectionFailed"), ("LUM-CIRCUIT-MIB", "fdfrStatusMplsTunnelProtectionDegraded"), ("LUM-CIRCUIT-MIB", "fdfrStatusUnknown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fdfrStatusGroupV5 = fdfrStatusGroupV5.setStatus('current')
lumCircuitBasicComplV1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 30, 1, 2, 1)).setObjects(("LUM-CIRCUIT-MIB", "circuitGeneralGroup"), ("LUM-CIRCUIT-MIB", "circuitStatusGroup"), ("LUM-CIRCUIT-MIB", "fdfrStatusGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumCircuitBasicComplV1 = lumCircuitBasicComplV1.setStatus('deprecated')
lumCircuitBasicComplV2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 30, 1, 2, 2)).setObjects(("LUM-CIRCUIT-MIB", "circuitGeneralGroup"), ("LUM-CIRCUIT-MIB", "circuitStatusGroup"), ("LUM-CIRCUIT-MIB", "fdfrStatusGroupV2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumCircuitBasicComplV2 = lumCircuitBasicComplV2.setStatus('deprecated')
lumCircuitBasicComplV3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 30, 1, 2, 3)).setObjects(("LUM-CIRCUIT-MIB", "circuitGeneralGroup"), ("LUM-CIRCUIT-MIB", "circuitStatusGroup"), ("LUM-CIRCUIT-MIB", "fdfrStatusGroupV3"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumCircuitBasicComplV3 = lumCircuitBasicComplV3.setStatus('deprecated')
lumCircuitBasicComplV4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 30, 1, 2, 4)).setObjects(("LUM-CIRCUIT-MIB", "circuitGeneralGroup"), ("LUM-CIRCUIT-MIB", "circuitStatusGroup"), ("LUM-CIRCUIT-MIB", "fdfrStatusGroupV4"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumCircuitBasicComplV4 = lumCircuitBasicComplV4.setStatus('deprecated')
lumCircuitBasicComplV5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 30, 1, 2, 5)).setObjects(("LUM-CIRCUIT-MIB", "circuitGeneralGroup"), ("LUM-CIRCUIT-MIB", "circuitStatusGroup"), ("LUM-CIRCUIT-MIB", "fdfrStatusGroupV5"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumCircuitBasicComplV5 = lumCircuitBasicComplV5.setStatus('current')
mibBuilder.exportSymbols("LUM-CIRCUIT-MIB", circuitStatusDescription=circuitStatusDescription, circuitStatusGroup=circuitStatusGroup, circuitStatusIndex=circuitStatusIndex, fdfrStatusEntry=fdfrStatusEntry, fdfrStatusIndex=fdfrStatusIndex, l2CircuitStatusList=l2CircuitStatusList, lumCircuitMIBModule=lumCircuitMIBModule, fdfrStatusUnexpectedMfdfrType=fdfrStatusUnexpectedMfdfrType, lumCircuitBasicComplV4=lumCircuitBasicComplV4, lumCircuitGroups=lumCircuitGroups, lumCircuitBasicComplV2=lumCircuitBasicComplV2, circuitStatusName=circuitStatusName, fdfrStatusUnknown=fdfrStatusUnknown, circuitStatusAdminStatus=circuitStatusAdminStatus, circuitStatusDegraded=circuitStatusDegraded, fdfrStatusMplsTunnelProtectionFailed=fdfrStatusMplsTunnelProtectionFailed, fdfrStatusGroup=fdfrStatusGroup, PYSNMP_MODULE_ID=lumCircuitMIBModule, circuitGeneral=circuitGeneral, circuitGeneralStateLastChangeTime=circuitGeneralStateLastChangeTime, fdfrStatusDown=fdfrStatusDown, lumCircuitCompl=lumCircuitCompl, circuitStatusOperStatus=circuitStatusOperStatus, circuitStatusList=circuitStatusList, lumCircuitConfs=lumCircuitConfs, fdfrStatusMplsTunnelProtectionDegraded=fdfrStatusMplsTunnelProtectionDegraded, fdfrStatusGroupV5=fdfrStatusGroupV5, circuitGeneralConfigLastChangeTime=circuitGeneralConfigLastChangeTime, fdfrStatusTable=fdfrStatusTable, circuitGeneralGroup=circuitGeneralGroup, circuitGeneralStatusTableSize=circuitGeneralStatusTableSize, fdfrStatusDegraded=fdfrStatusDegraded, fdfrStatusGroupV4=fdfrStatusGroupV4, circuitStatusDown=circuitStatusDown, lumCircuitMIBObjects=lumCircuitMIBObjects, fdfrStatusGroupV3=fdfrStatusGroupV3, fdfrStatusIncomplete=fdfrStatusIncomplete, lumCircuitBasicComplV5=lumCircuitBasicComplV5, lumCircuitBasicComplV3=lumCircuitBasicComplV3, lumCircuitBasicComplV1=lumCircuitBasicComplV1, circuitStatusEntry=circuitStatusEntry, circuitStatusIncomplete=circuitStatusIncomplete, fdfrStatusGroupV2=fdfrStatusGroupV2, circuitStatusTable=circuitStatusTable)
