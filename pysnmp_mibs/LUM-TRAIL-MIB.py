#
# PySNMP MIB module LUM-TRAIL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/LUM-TRAIL-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:20:31 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
lumTrailMIB, lumModules = mibBuilder.importSymbols("LUM-REG", "lumTrailMIB", "lumModules")
FaultStatus, = mibBuilder.importSymbols("LUM-TC", "FaultStatus")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("LUM-TRAIL-MIB", trailStatusList=trailStatusList, lumTrailCompl=lumTrailCompl, lumTrailGroups=lumTrailGroups, trailStatusIncomplete=trailStatusIncomplete, trailStatusIndex=trailStatusIndex, lumTrailConfs=lumTrailConfs, trailStatusDegraded=trailStatusDegraded, lumTrailBasicComplV1=lumTrailBasicComplV1, trailGeneralConfigLastChangeTime=trailGeneralConfigLastChangeTime, lumTrailMIBObjects=lumTrailMIBObjects, trailStatusGroupV2=trailStatusGroupV2, trailGeneralStateLastChangeTime=trailGeneralStateLastChangeTime, trailStatusTable=trailStatusTable, trailGeneralStatusTableSize=trailGeneralStatusTableSize, trailStatusDown=trailStatusDown, lumTrailMIBModule=lumTrailMIBModule, trailGeneralGroup=trailGeneralGroup, trailStatusEntry=trailStatusEntry, trailGeneral=trailGeneral, lumTrailBasicComplV2=lumTrailBasicComplV2, PYSNMP_MODULE_ID=lumTrailMIBModule, trailStatusGroup=trailStatusGroup)
