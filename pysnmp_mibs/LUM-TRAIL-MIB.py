#
# PySNMP MIB module LUM-TRAIL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/LUM-TRAIL-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:28 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
lumTrailMIB, lumModules = mibBuilder.importSymbols("LUM-REG", "lumTrailMIB", "lumModules")
FaultStatus, = mibBuilder.importSymbols("LUM-TC", "FaultStatus")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
lumTrailMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 8708, 1, 1, 38))
lumTrailMIBModule.setRevisions(('2017-06-15 00:00', '2011-04-13 00:00',))
if mibBuilder.loadTexts: lumTrailMIBModule.setLastUpdated('201706150000Z')
if mibBuilder.loadTexts: lumTrailMIBModule.setOrganization('Infinera Corporation')
lumTrailConfs = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 38, 1))
lumTrailGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 38, 1, 1))
lumTrailCompl = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 38, 1, 2))
lumTrailMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 38, 2))
trailGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 38, 2, 1))
trailStatusList = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 38, 2, 2))
trailGeneralConfigLastChangeTime = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 38, 2, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trailGeneralConfigLastChangeTime.setStatus('current')
trailGeneralStateLastChangeTime = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 38, 2, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trailGeneralStateLastChangeTime.setStatus('current')
trailGeneralStatusTableSize = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 38, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trailGeneralStatusTableSize.setStatus('current')
trailStatusTable = MibTable((1, 3, 6, 1, 4, 1, 8708, 2, 38, 2, 2, 1), )
if mibBuilder.loadTexts: trailStatusTable.setStatus('current')
trailStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8708, 2, 38, 2, 2, 1, 1), ).setIndexNames((0, "LUM-TRAIL-MIB", "trailStatusIndex"))
if mibBuilder.loadTexts: trailStatusEntry.setStatus('current')
trailStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 38, 2, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trailStatusIndex.setStatus('current')
trailStatusIncomplete = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 38, 2, 2, 1, 1, 2), FaultStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trailStatusIncomplete.setStatus('current')
trailStatusDegraded = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 38, 2, 2, 1, 1, 3), FaultStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trailStatusDegraded.setStatus('deprecated')
trailStatusDown = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 38, 2, 2, 1, 1, 4), FaultStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trailStatusDown.setStatus('deprecated')
trailGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 38, 1, 1, 1)).setObjects(("LUM-TRAIL-MIB", "trailGeneralConfigLastChangeTime"), ("LUM-TRAIL-MIB", "trailGeneralStateLastChangeTime"), ("LUM-TRAIL-MIB", "trailGeneralStatusTableSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trailGeneralGroup = trailGeneralGroup.setStatus('current')
trailStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 38, 1, 1, 2)).setObjects(("LUM-TRAIL-MIB", "trailStatusIndex"), ("LUM-TRAIL-MIB", "trailStatusDegraded"), ("LUM-TRAIL-MIB", "trailStatusDown"), ("LUM-TRAIL-MIB", "trailStatusIncomplete"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trailStatusGroup = trailStatusGroup.setStatus('deprecated')
trailStatusGroupV2 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 38, 1, 1, 3)).setObjects(("LUM-TRAIL-MIB", "trailStatusIndex"), ("LUM-TRAIL-MIB", "trailStatusIncomplete"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trailStatusGroupV2 = trailStatusGroupV2.setStatus('current')
lumTrailBasicComplV1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 38, 1, 2, 1)).setObjects(("LUM-TRAIL-MIB", "trailGeneralGroup"), ("LUM-TRAIL-MIB", "trailStatusGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumTrailBasicComplV1 = lumTrailBasicComplV1.setStatus('deprecated')
lumTrailBasicComplV2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 38, 1, 2, 2)).setObjects(("LUM-TRAIL-MIB", "trailGeneralGroup"), ("LUM-TRAIL-MIB", "trailStatusGroupV2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumTrailBasicComplV2 = lumTrailBasicComplV2.setStatus('current')
mibBuilder.exportSymbols("LUM-TRAIL-MIB", trailStatusDown=trailStatusDown, trailStatusGroup=trailStatusGroup, trailStatusDegraded=trailStatusDegraded, trailGeneralConfigLastChangeTime=trailGeneralConfigLastChangeTime, trailStatusIncomplete=trailStatusIncomplete, trailStatusTable=trailStatusTable, trailGeneralStateLastChangeTime=trailGeneralStateLastChangeTime, lumTrailCompl=lumTrailCompl, lumTrailBasicComplV2=lumTrailBasicComplV2, trailStatusList=trailStatusList, trailGeneralGroup=trailGeneralGroup, lumTrailMIBObjects=lumTrailMIBObjects, trailStatusGroupV2=trailStatusGroupV2, lumTrailMIBModule=lumTrailMIBModule, lumTrailConfs=lumTrailConfs, lumTrailBasicComplV1=lumTrailBasicComplV1, trailStatusIndex=trailStatusIndex, trailGeneral=trailGeneral, PYSNMP_MODULE_ID=lumTrailMIBModule, trailStatusEntry=trailStatusEntry, lumTrailGroups=lumTrailGroups, trailGeneralStatusTableSize=trailGeneralStatusTableSize)
