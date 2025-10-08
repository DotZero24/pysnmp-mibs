#
# PySNMP MIB module LUM-CIRCUIT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/LUM-CIRCUIT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:52 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
lumModules, lumCircuitMIB = mibBuilder.importSymbols("LUM-REG", "lumModules", "lumCircuitMIB")
MgmtNameString, FaultStatus = mibBuilder.importSymbols("LUM-TC", "MgmtNameString", "FaultStatus")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
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
mibBuilder.exportSymbols("LUM-CIRCUIT-MIB", lumCircuitBasicComplV1=lumCircuitBasicComplV1, lumCircuitMIBModule=lumCircuitMIBModule, fdfrStatusIncomplete=fdfrStatusIncomplete, fdfrStatusGroup=fdfrStatusGroup, fdfrStatusGroupV2=fdfrStatusGroupV2, circuitStatusEntry=circuitStatusEntry, circuitGeneralStateLastChangeTime=circuitGeneralStateLastChangeTime, circuitGeneralConfigLastChangeTime=circuitGeneralConfigLastChangeTime, lumCircuitCompl=lumCircuitCompl, PYSNMP_MODULE_ID=lumCircuitMIBModule, circuitStatusOperStatus=circuitStatusOperStatus, circuitStatusDescription=circuitStatusDescription, lumCircuitBasicComplV2=lumCircuitBasicComplV2, fdfrStatusGroupV5=fdfrStatusGroupV5, fdfrStatusMplsTunnelProtectionFailed=fdfrStatusMplsTunnelProtectionFailed, circuitGeneralGroup=circuitGeneralGroup, lumCircuitBasicComplV3=lumCircuitBasicComplV3, lumCircuitGroups=lumCircuitGroups, lumCircuitMIBObjects=lumCircuitMIBObjects, circuitStatusIndex=circuitStatusIndex, lumCircuitBasicComplV4=lumCircuitBasicComplV4, circuitStatusIncomplete=circuitStatusIncomplete, fdfrStatusUnexpectedMfdfrType=fdfrStatusUnexpectedMfdfrType, fdfrStatusDegraded=fdfrStatusDegraded, circuitStatusGroup=circuitStatusGroup, fdfrStatusGroupV4=fdfrStatusGroupV4, fdfrStatusEntry=fdfrStatusEntry, circuitGeneralStatusTableSize=circuitGeneralStatusTableSize, circuitStatusDegraded=circuitStatusDegraded, fdfrStatusDown=fdfrStatusDown, l2CircuitStatusList=l2CircuitStatusList, circuitStatusName=circuitStatusName, fdfrStatusMplsTunnelProtectionDegraded=fdfrStatusMplsTunnelProtectionDegraded, circuitStatusTable=circuitStatusTable, lumCircuitBasicComplV5=lumCircuitBasicComplV5, lumCircuitConfs=lumCircuitConfs, circuitStatusAdminStatus=circuitStatusAdminStatus, fdfrStatusIndex=fdfrStatusIndex, fdfrStatusGroupV3=fdfrStatusGroupV3, fdfrStatusTable=fdfrStatusTable, circuitStatusList=circuitStatusList, fdfrStatusUnknown=fdfrStatusUnknown, circuitStatusDown=circuitStatusDown, circuitGeneral=circuitGeneral)
