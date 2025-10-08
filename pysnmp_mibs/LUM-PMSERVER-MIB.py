#
# PySNMP MIB module LUM-PMSERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/LUM-PMSERVER-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:21:51 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
lumModules, lumPmServerMIB = mibBuilder.importSymbols("LUM-REG", "lumModules", "lumPmServerMIB")
FaultStatus, = mibBuilder.importSymbols("LUM-TC", "FaultStatus")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("LUM-PMSERVER-MIB", PYSNMP_MODULE_ID=lumPmServerMIBModule, lumPmServerMIBModule=lumPmServerMIBModule, lumPmServerCompl=lumPmServerCompl, pmServerStatusTable=pmServerStatusTable, pmServerStatusList=pmServerStatusList, pmServerStatusEntry=pmServerStatusEntry, pmServerStatusFaultyEduReportFilesExist=pmServerStatusFaultyEduReportFilesExist, pmServerGeneralGroup=pmServerGeneralGroup, pmServerGeneralConfigLastChangeTime=pmServerGeneralConfigLastChangeTime, pmServerStatusGroup=pmServerStatusGroup, pmServerStatusIndex=pmServerStatusIndex, lumPmServerConfs=lumPmServerConfs, lumPmServerGroups=lumPmServerGroups, pmServerGeneralStateLastChangeTime=pmServerGeneralStateLastChangeTime, pmServerGeneralStatusTableSize=pmServerGeneralStatusTableSize, lumPmServerBasicComplV1=lumPmServerBasicComplV1, lumPmServerMIBObjects=lumPmServerMIBObjects, pmServerGeneral=pmServerGeneral)
