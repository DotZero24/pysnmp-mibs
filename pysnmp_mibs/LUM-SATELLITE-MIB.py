#
# PySNMP MIB module LUM-SATELLITE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/LUM-SATELLITE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:22 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
lumSatelliteMIB, lumModules = mibBuilder.importSymbols("LUM-REG", "lumSatelliteMIB", "lumModules")
MgmtNameString, = mibBuilder.importSymbols("LUM-TC", "MgmtNameString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
lumSatelliteMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 8708, 1, 1, 36))
lumSatelliteMIBModule.setRevisions(('2017-06-15 00:00', '2009-06-15 00:00',))
if mibBuilder.loadTexts: lumSatelliteMIBModule.setLastUpdated('201706150000Z')
if mibBuilder.loadTexts: lumSatelliteMIBModule.setOrganization('Infinera Corporation')
lumSatelliteConfs = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 36, 1))
lumSatelliteGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 36, 1, 1))
lumSatelliteCompl = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 36, 1, 2))
lumSatelliteMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 36, 2))
satelliteGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 36, 2, 1))
satelliteSatelliteList = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 36, 2, 2))
satelliteGeneralLastChangeTime = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 36, 2, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteGeneralLastChangeTime.setStatus('current')
satelliteGeneralStateLastChangeTime = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 36, 2, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteGeneralStateLastChangeTime.setStatus('current')
satelliteGeneralSatelliteTableSize = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 36, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteGeneralSatelliteTableSize.setStatus('current')
satelliteSatelliteTable = MibTable((1, 3, 6, 1, 4, 1, 8708, 2, 36, 2, 2, 1), )
if mibBuilder.loadTexts: satelliteSatelliteTable.setStatus('current')
satelliteSatelliteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8708, 2, 36, 2, 2, 1, 1), ).setIndexNames((0, "LUM-SATELLITE-MIB", "satelliteSatelliteIndex"))
if mibBuilder.loadTexts: satelliteSatelliteEntry.setStatus('current')
satelliteSatelliteIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 36, 2, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteSatelliteIndex.setStatus('current')
satelliteSatelliteName = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 36, 2, 2, 1, 1, 2), MgmtNameString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteSatelliteName.setStatus('current')
satelliteSatelliteDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 36, 2, 2, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: satelliteSatelliteDescr.setStatus('current')
satelliteSatelliteExpectedBoardType = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 36, 2, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mba1", 1), ("mba2", 2))).clone('mba2')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: satelliteSatelliteExpectedBoardType.setStatus('current')
satelliteGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 36, 1, 1, 1)).setObjects(("LUM-SATELLITE-MIB", "satelliteGeneralLastChangeTime"), ("LUM-SATELLITE-MIB", "satelliteGeneralStateLastChangeTime"), ("LUM-SATELLITE-MIB", "satelliteGeneralSatelliteTableSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    satelliteGeneralGroup = satelliteGeneralGroup.setStatus('current')
satelliteSatelliteGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 36, 1, 1, 2)).setObjects(("LUM-SATELLITE-MIB", "satelliteSatelliteIndex"), ("LUM-SATELLITE-MIB", "satelliteSatelliteName"), ("LUM-SATELLITE-MIB", "satelliteSatelliteDescr"), ("LUM-SATELLITE-MIB", "satelliteSatelliteExpectedBoardType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    satelliteSatelliteGroup = satelliteSatelliteGroup.setStatus('current')
lumSatelliteBasicCompl1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 36, 1, 2, 1)).setObjects(("LUM-SATELLITE-MIB", "satelliteGeneralGroup"), ("LUM-SATELLITE-MIB", "satelliteSatelliteGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumSatelliteBasicCompl1 = lumSatelliteBasicCompl1.setStatus('current')
mibBuilder.exportSymbols("LUM-SATELLITE-MIB", satelliteSatelliteGroup=satelliteSatelliteGroup, satelliteSatelliteList=satelliteSatelliteList, PYSNMP_MODULE_ID=lumSatelliteMIBModule, satelliteSatelliteDescr=satelliteSatelliteDescr, lumSatelliteMIBObjects=lumSatelliteMIBObjects, lumSatelliteConfs=lumSatelliteConfs, satelliteGeneralGroup=satelliteGeneralGroup, satelliteSatelliteTable=satelliteSatelliteTable, satelliteSatelliteIndex=satelliteSatelliteIndex, lumSatelliteBasicCompl1=lumSatelliteBasicCompl1, lumSatelliteCompl=lumSatelliteCompl, lumSatelliteMIBModule=lumSatelliteMIBModule, lumSatelliteGroups=lumSatelliteGroups, satelliteGeneralLastChangeTime=satelliteGeneralLastChangeTime, satelliteSatelliteEntry=satelliteSatelliteEntry, satelliteGeneral=satelliteGeneral, satelliteGeneralStateLastChangeTime=satelliteGeneralStateLastChangeTime, satelliteSatelliteExpectedBoardType=satelliteSatelliteExpectedBoardType, satelliteSatelliteName=satelliteSatelliteName, satelliteGeneralSatelliteTableSize=satelliteGeneralSatelliteTableSize)
