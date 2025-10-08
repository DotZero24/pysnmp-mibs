#
# PySNMP MIB module QTECH-LICENSE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/qtech/QTECH-LICENSE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:14:37 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
qtechMgmt, = mibBuilder.importSymbols("QTECH-SMI", "qtechMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("QTECH-LICENSE-MIB", qtechLicenseString=qtechLicenseString, qtechLicenseMIBGroups=qtechLicenseMIBGroups, qtechLicenseMIBConformance=qtechLicenseMIBConformance, qtechShowLicense=qtechShowLicense, qtechLicenseTable=qtechLicenseTable, qtechLicenseValue=qtechLicenseValue, qtechLicenseMIB=qtechLicenseMIB, qtechLicenseMIBCompliances=qtechLicenseMIBCompliances, qtechLicenseIndex=qtechLicenseIndex, qtechLicenseMIBCompliance=qtechLicenseMIBCompliance, qtechLicenseEntry=qtechLicenseEntry, PYSNMP_MODULE_ID=qtechLicenseMIB, qtechLicenseMIBGroup=qtechLicenseMIBGroup, qtechLicenseMIBObjects=qtechLicenseMIBObjects)
