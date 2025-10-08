#
# PySNMP MIB module LUM-SATELLITE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/LUM-SATELLITE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:20:17 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
lumModules, lumSatelliteMIB = mibBuilder.importSymbols("LUM-REG", "lumModules", "lumSatelliteMIB")
MgmtNameString, = mibBuilder.importSymbols("LUM-TC", "MgmtNameString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("LUM-SATELLITE-MIB", satelliteSatelliteDescr=satelliteSatelliteDescr, satelliteGeneralLastChangeTime=satelliteGeneralLastChangeTime, satelliteSatelliteTable=satelliteSatelliteTable, satelliteGeneralGroup=satelliteGeneralGroup, satelliteSatelliteIndex=satelliteSatelliteIndex, lumSatelliteMIBModule=lumSatelliteMIBModule, PYSNMP_MODULE_ID=lumSatelliteMIBModule, lumSatelliteCompl=lumSatelliteCompl, satelliteSatelliteName=satelliteSatelliteName, lumSatelliteGroups=lumSatelliteGroups, satelliteSatelliteGroup=satelliteSatelliteGroup, satelliteGeneralSatelliteTableSize=satelliteGeneralSatelliteTableSize, lumSatelliteMIBObjects=lumSatelliteMIBObjects, lumSatelliteConfs=lumSatelliteConfs, satelliteSatelliteList=satelliteSatelliteList, satelliteGeneralStateLastChangeTime=satelliteGeneralStateLastChangeTime, satelliteGeneral=satelliteGeneral, satelliteSatelliteEntry=satelliteSatelliteEntry, lumSatelliteBasicCompl1=lumSatelliteBasicCompl1, satelliteSatelliteExpectedBoardType=satelliteSatelliteExpectedBoardType)
