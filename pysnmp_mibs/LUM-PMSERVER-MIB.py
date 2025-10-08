#
# PySNMP MIB module LUM-PMSERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/LUM-PMSERVER-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:10:13 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
lumPmServerMIB, lumModules = mibBuilder.importSymbols("LUM-REG", "lumPmServerMIB", "lumModules")
FaultStatus, = mibBuilder.importSymbols("LUM-TC", "FaultStatus")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
lumPmServerMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 8708, 1, 1, 49))
lumPmServerMIBModule.setRevisions(('2017-06-15 00:00', '2012-07-18 00:00',))
if mibBuilder.loadTexts: lumPmServerMIBModule.setLastUpdated('201706150000Z')
if mibBuilder.loadTexts: lumPmServerMIBModule.setOrganization('Infinera Corporation')
lumPmServerConfs = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 49, 1))
lumPmServerGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 49, 1, 1))
lumPmServerCompl = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 49, 1, 2))
lumPmServerMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 49, 2))
pmServerGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 49, 2, 1))
pmServerStatusList = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 49, 2, 2))
pmServerGeneralConfigLastChangeTime = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 49, 2, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmServerGeneralConfigLastChangeTime.setStatus('current')
pmServerGeneralStateLastChangeTime = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 49, 2, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmServerGeneralStateLastChangeTime.setStatus('current')
pmServerGeneralStatusTableSize = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 49, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmServerGeneralStatusTableSize.setStatus('current')
pmServerStatusTable = MibTable((1, 3, 6, 1, 4, 1, 8708, 2, 49, 2, 2, 1), )
if mibBuilder.loadTexts: pmServerStatusTable.setStatus('current')
pmServerStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8708, 2, 49, 2, 2, 1, 1), ).setIndexNames((0, "LUM-PMSERVER-MIB", "pmServerStatusIndex"))
if mibBuilder.loadTexts: pmServerStatusEntry.setStatus('current')
pmServerStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 49, 2, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmServerStatusIndex.setStatus('current')
pmServerStatusFaultyEduReportFilesExist = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 49, 2, 2, 1, 1, 2), FaultStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmServerStatusFaultyEduReportFilesExist.setStatus('current')
pmServerGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 49, 1, 1, 1)).setObjects(("LUM-PMSERVER-MIB", "pmServerGeneralConfigLastChangeTime"), ("LUM-PMSERVER-MIB", "pmServerGeneralStateLastChangeTime"), ("LUM-PMSERVER-MIB", "pmServerGeneralStatusTableSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pmServerGeneralGroup = pmServerGeneralGroup.setStatus('current')
pmServerStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 49, 1, 1, 2)).setObjects(("LUM-PMSERVER-MIB", "pmServerStatusIndex"), ("LUM-PMSERVER-MIB", "pmServerStatusFaultyEduReportFilesExist"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pmServerStatusGroup = pmServerStatusGroup.setStatus('current')
lumPmServerBasicComplV1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 49, 1, 2, 1)).setObjects(("LUM-PMSERVER-MIB", "pmServerGeneralGroup"), ("LUM-PMSERVER-MIB", "pmServerStatusGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumPmServerBasicComplV1 = lumPmServerBasicComplV1.setStatus('current')
mibBuilder.exportSymbols("LUM-PMSERVER-MIB", lumPmServerMIBModule=lumPmServerMIBModule, pmServerGeneralStateLastChangeTime=pmServerGeneralStateLastChangeTime, pmServerStatusIndex=pmServerStatusIndex, pmServerStatusFaultyEduReportFilesExist=pmServerStatusFaultyEduReportFilesExist, lumPmServerCompl=lumPmServerCompl, pmServerGeneralStatusTableSize=pmServerGeneralStatusTableSize, PYSNMP_MODULE_ID=lumPmServerMIBModule, pmServerStatusList=pmServerStatusList, pmServerStatusGroup=pmServerStatusGroup, lumPmServerConfs=lumPmServerConfs, pmServerGeneralConfigLastChangeTime=pmServerGeneralConfigLastChangeTime, pmServerStatusTable=pmServerStatusTable, pmServerGeneralGroup=pmServerGeneralGroup, lumPmServerGroups=lumPmServerGroups, pmServerGeneral=pmServerGeneral, lumPmServerMIBObjects=lumPmServerMIBObjects, lumPmServerBasicComplV1=lumPmServerBasicComplV1, pmServerStatusEntry=pmServerStatusEntry)
