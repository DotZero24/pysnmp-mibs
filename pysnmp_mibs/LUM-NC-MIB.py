#
# PySNMP MIB module LUM-NC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/LUM-NC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:21:16 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
lumNcMIB, lumModules = mibBuilder.importSymbols("LUM-REG", "lumNcMIB", "lumModules")
FaultStatus, = mibBuilder.importSymbols("LUM-TC", "FaultStatus")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
lumNcMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 8708, 1, 1, 39))
lumNcMIBModule.setRevisions(('2017-06-15 00:00', '2011-04-13 00:00',))
if mibBuilder.loadTexts: lumNcMIBModule.setLastUpdated('201706150000Z')
if mibBuilder.loadTexts: lumNcMIBModule.setOrganization('Infinera Corporation')
lumNcConfs = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 39, 1))
lumNcGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 39, 1, 1))
lumNcCompl = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 39, 1, 2))
lumNcMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 39, 2))
ncGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 39, 2, 1))
ncStatusList = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 39, 2, 2))
ncGeneralConfigLastChangeTime = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 39, 2, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncGeneralConfigLastChangeTime.setStatus('current')
ncGeneralStateLastChangeTime = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 39, 2, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncGeneralStateLastChangeTime.setStatus('current')
ncGeneralStatusTableSize = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 39, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncGeneralStatusTableSize.setStatus('current')
ncStatusTable = MibTable((1, 3, 6, 1, 4, 1, 8708, 2, 39, 2, 2, 1), )
if mibBuilder.loadTexts: ncStatusTable.setStatus('current')
ncStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8708, 2, 39, 2, 2, 1, 1), ).setIndexNames((0, "LUM-NC-MIB", "ncStatusIndex"))
if mibBuilder.loadTexts: ncStatusEntry.setStatus('current')
ncStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 39, 2, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncStatusIndex.setStatus('current')
ncStatusIncomplete = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 39, 2, 2, 1, 1, 2), FaultStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncStatusIncomplete.setStatus('current')
ncStatusDegraded = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 39, 2, 2, 1, 1, 3), FaultStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncStatusDegraded.setStatus('deprecated')
ncStatusDown = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 39, 2, 2, 1, 1, 4), FaultStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncStatusDown.setStatus('deprecated')
ncGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 39, 1, 1, 1)).setObjects(("LUM-NC-MIB", "ncGeneralConfigLastChangeTime"), ("LUM-NC-MIB", "ncGeneralStateLastChangeTime"), ("LUM-NC-MIB", "ncGeneralStatusTableSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ncGeneralGroup = ncGeneralGroup.setStatus('current')
ncStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 39, 1, 1, 2)).setObjects(("LUM-NC-MIB", "ncStatusIndex"), ("LUM-NC-MIB", "ncStatusDegraded"), ("LUM-NC-MIB", "ncStatusDown"), ("LUM-NC-MIB", "ncStatusIncomplete"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ncStatusGroup = ncStatusGroup.setStatus('deprecated')
ncStatusGroupV2 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 39, 1, 1, 3)).setObjects(("LUM-NC-MIB", "ncStatusIndex"), ("LUM-NC-MIB", "ncStatusIncomplete"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ncStatusGroupV2 = ncStatusGroupV2.setStatus('current')
lumNcBasicComplV1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 39, 1, 2, 1)).setObjects(("LUM-NC-MIB", "ncGeneralGroup"), ("LUM-NC-MIB", "ncStatusGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumNcBasicComplV1 = lumNcBasicComplV1.setStatus('deprecated')
lumNcBasicComplV2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 39, 1, 2, 2)).setObjects(("LUM-NC-MIB", "ncGeneralGroup"), ("LUM-NC-MIB", "ncStatusGroupV2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumNcBasicComplV2 = lumNcBasicComplV2.setStatus('current')
mibBuilder.exportSymbols("LUM-NC-MIB", ncStatusEntry=ncStatusEntry, ncStatusTable=ncStatusTable, lumNcCompl=lumNcCompl, lumNcBasicComplV1=lumNcBasicComplV1, PYSNMP_MODULE_ID=lumNcMIBModule, ncGeneralGroup=ncGeneralGroup, lumNcMIBObjects=lumNcMIBObjects, lumNcBasicComplV2=lumNcBasicComplV2, ncGeneralConfigLastChangeTime=ncGeneralConfigLastChangeTime, ncGeneralStatusTableSize=ncGeneralStatusTableSize, ncStatusDown=ncStatusDown, lumNcConfs=lumNcConfs, ncStatusGroup=ncStatusGroup, ncStatusIncomplete=ncStatusIncomplete, ncStatusDegraded=ncStatusDegraded, ncGeneralStateLastChangeTime=ncGeneralStateLastChangeTime, lumNcMIBModule=lumNcMIBModule, ncGeneral=ncGeneral, ncStatusGroupV2=ncStatusGroupV2, ncStatusList=ncStatusList, ncStatusIndex=ncStatusIndex, lumNcGroups=lumNcGroups)
