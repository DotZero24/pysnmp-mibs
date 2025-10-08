#
# PySNMP MIB module LUM-NC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/LUM-NC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:54 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
lumNcMIB, lumModules = mibBuilder.importSymbols("LUM-REG", "lumNcMIB", "lumModules")
FaultStatus, = mibBuilder.importSymbols("LUM-TC", "FaultStatus")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
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
mibBuilder.exportSymbols("LUM-NC-MIB", ncGeneral=ncGeneral, ncStatusTable=ncStatusTable, ncStatusDegraded=ncStatusDegraded, ncStatusGroup=ncStatusGroup, PYSNMP_MODULE_ID=lumNcMIBModule, lumNcMIBModule=lumNcMIBModule, lumNcBasicComplV2=lumNcBasicComplV2, ncStatusEntry=ncStatusEntry, ncStatusList=ncStatusList, lumNcConfs=lumNcConfs, lumNcGroups=lumNcGroups, ncGeneralConfigLastChangeTime=ncGeneralConfigLastChangeTime, ncStatusIncomplete=ncStatusIncomplete, ncStatusGroupV2=ncStatusGroupV2, lumNcBasicComplV1=lumNcBasicComplV1, ncStatusIndex=ncStatusIndex, ncGeneralStatusTableSize=ncGeneralStatusTableSize, ncStatusDown=ncStatusDown, ncGeneralGroup=ncGeneralGroup, ncGeneralStateLastChangeTime=ncGeneralStateLastChangeTime, lumNcMIBObjects=lumNcMIBObjects, lumNcCompl=lumNcCompl)
