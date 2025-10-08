#
# PySNMP MIB module QTECH-LICENSE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/qtech/QTECH-LICENSE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:06:31 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
qtechMgmt, = mibBuilder.importSymbols("QTECH-SMI", "qtechMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
qtechLicenseMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 57))
qtechLicenseMIB.setRevisions(('2009-09-18 00:00',))
if mibBuilder.loadTexts: qtechLicenseMIB.setLastUpdated('200909180000Z')
if mibBuilder.loadTexts: qtechLicenseMIB.setOrganization('Qtech Networks Co.,Ltd.')
qtechLicenseMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 57, 1))
qtechShowLicense = MibScalar((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 57, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechShowLicense.setStatus('current')
qtechLicenseTable = MibTable((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 57, 1, 2), )
if mibBuilder.loadTexts: qtechLicenseTable.setStatus('current')
qtechLicenseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 57, 1, 2, 1), ).setIndexNames((0, "QTECH-LICENSE-MIB", "qtechLicenseIndex"))
if mibBuilder.loadTexts: qtechLicenseEntry.setStatus('current')
qtechLicenseIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 57, 1, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: qtechLicenseIndex.setStatus('current')
qtechLicenseString = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 57, 1, 2, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qtechLicenseString.setStatus('current')
qtechLicenseValue = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 57, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechLicenseValue.setStatus('current')
qtechLicenseMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 57, 2))
qtechLicenseMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 57, 2, 1))
qtechLicenseMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 57, 2, 2))
qtechLicenseMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 57, 2, 1, 1)).setObjects(("QTECH-LICENSE-MIB", "qtechLicenseMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qtechLicenseMIBCompliance = qtechLicenseMIBCompliance.setStatus('current')
qtechLicenseMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 57, 2, 2, 1)).setObjects(("QTECH-LICENSE-MIB", "qtechShowLicense"), ("QTECH-LICENSE-MIB", "qtechLicenseString"), ("QTECH-LICENSE-MIB", "qtechLicenseValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qtechLicenseMIBGroup = qtechLicenseMIBGroup.setStatus('current')
mibBuilder.exportSymbols("QTECH-LICENSE-MIB", qtechLicenseValue=qtechLicenseValue, qtechLicenseMIBCompliance=qtechLicenseMIBCompliance, qtechLicenseMIBGroup=qtechLicenseMIBGroup, qtechLicenseMIB=qtechLicenseMIB, qtechLicenseMIBCompliances=qtechLicenseMIBCompliances, PYSNMP_MODULE_ID=qtechLicenseMIB, qtechLicenseEntry=qtechLicenseEntry, qtechLicenseIndex=qtechLicenseIndex, qtechLicenseMIBObjects=qtechLicenseMIBObjects, qtechLicenseMIBGroups=qtechLicenseMIBGroups, qtechLicenseString=qtechLicenseString, qtechShowLicense=qtechShowLicense, qtechLicenseMIBConformance=qtechLicenseMIBConformance, qtechLicenseTable=qtechLicenseTable)
