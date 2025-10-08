#
# PySNMP MIB module CISCO-IMAGE-LICENSE-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-IMAGE-LICENSE-MGMT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:16:20 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ciscoImageLicenseMgmtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 640))
ciscoImageLicenseMgmtMIB.setRevisions(('2007-10-16 00:00',))
if mibBuilder.loadTexts: ciscoImageLicenseMgmtMIB.setLastUpdated('200710160000Z')
if mibBuilder.loadTexts: ciscoImageLicenseMgmtMIB.setOrganization('Cisco Systems Inc.')
ciscoImageLicenseMgmtMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 640, 0))
ciscoImageLicenseMgmtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 640, 1))
ciscoImageLicenseMgmtMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 640, 2))
class BootImageLevel(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class LicenseNameList(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

cilmBootImageLevelTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 1), )
if mibBuilder.loadTexts: cilmBootImageLevelTable.setStatus('current')
cilmBootImageLevelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmModuleName"))
if mibBuilder.loadTexts: cilmBootImageLevelEntry.setStatus('current')
cilmModuleName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 1, 1, 1), SnmpAdminString())
if mibBuilder.loadTexts: cilmModuleName.setStatus('current')
cilmCurrentImageLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 1, 1, 2), BootImageLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cilmCurrentImageLevel.setStatus('current')
cilmConfiguredBootImageLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 1, 1, 3), BootImageLevel()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cilmConfiguredBootImageLevel.setStatus('current')
cilmNextBootImageLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 1, 1, 4), BootImageLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cilmNextBootImageLevel.setStatus('current')
cilmCurrentLicenseStoreIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cilmCurrentLicenseStoreIndex.setStatus('current')
cilmCurrentLicenseIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cilmCurrentLicenseIndex.setStatus('current')
cilmNextBootLicenseStoreIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cilmNextBootLicenseStoreIndex.setStatus('current')
cilmNextBootLicenseIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cilmNextBootLicenseIndex.setStatus('current')
cilmImageLevelToLicenseMapTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 2), )
if mibBuilder.loadTexts: cilmImageLevelToLicenseMapTable.setStatus('current')
cilmImageLevelToLicenseMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmModuleName"), (0, "CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmImageLicenseMapIndex"))
if mibBuilder.loadTexts: cilmImageLevelToLicenseMapEntry.setStatus('current')
cilmImageLicenseMapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cilmImageLicenseMapIndex.setStatus('current')
cilmImageLicenseImageLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 2, 1, 2), BootImageLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cilmImageLicenseImageLevel.setStatus('current')
cilmImageLicenseName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 2, 1, 3), LicenseNameList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cilmImageLicenseName.setStatus('current')
cilmImageLicensePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 2, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cilmImageLicensePriority.setStatus('current')
cilmEULAAccepted = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cilmEULAAccepted.setStatus('current')
cilmNotifCntl = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 4))
cilmImageLevelChangedNotif = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 4, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cilmImageLevelChangedNotif.setStatus('current')
cilmBootImageLevelChanged = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 640, 0, 1)).setObjects(("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmCurrentImageLevel"), ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmConfiguredBootImageLevel"))
if mibBuilder.loadTexts: cilmBootImageLevelChanged.setStatus('current')
cilmModuleCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 640, 2, 1))
cilmModuleGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 640, 2, 2))
cilmModuleCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 640, 2, 1, 1)).setObjects(("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmAdminGroup"), ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmNotifGroup"), ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmOperGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cilmModuleCompliance = cilmModuleCompliance.setStatus('current')
cilmAdminGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 640, 2, 2, 1)).setObjects(("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmCurrentImageLevel"), ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmConfiguredBootImageLevel"), ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmNextBootImageLevel"), ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmCurrentLicenseStoreIndex"), ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmCurrentLicenseIndex"), ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmNextBootLicenseStoreIndex"), ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmNextBootLicenseIndex"), ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmEULAAccepted"), ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmImageLevelChangedNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cilmAdminGroup = cilmAdminGroup.setStatus('current')
cilmOperGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 640, 2, 2, 2)).setObjects(("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmImageLicenseImageLevel"), ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmImageLicenseName"), ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmImageLicensePriority"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cilmOperGroup = cilmOperGroup.setStatus('current')
cilmNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 640, 2, 2, 3)).setObjects(("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmBootImageLevelChanged"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cilmNotifGroup = cilmNotifGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-IMAGE-LICENSE-MGMT-MIB", ciscoImageLicenseMgmtMIBNotifs=ciscoImageLicenseMgmtMIBNotifs, cilmModuleCompliance=cilmModuleCompliance, BootImageLevel=BootImageLevel, cilmNextBootLicenseIndex=cilmNextBootLicenseIndex, cilmImageLicenseImageLevel=cilmImageLicenseImageLevel, cilmBootImageLevelChanged=cilmBootImageLevelChanged, cilmEULAAccepted=cilmEULAAccepted, cilmImageLicenseMapIndex=cilmImageLicenseMapIndex, cilmNotifGroup=cilmNotifGroup, cilmNextBootImageLevel=cilmNextBootImageLevel, cilmBootImageLevelTable=cilmBootImageLevelTable, cilmNotifCntl=cilmNotifCntl, cilmBootImageLevelEntry=cilmBootImageLevelEntry, cilmCurrentLicenseStoreIndex=cilmCurrentLicenseStoreIndex, cilmImageLicenseName=cilmImageLicenseName, cilmAdminGroup=cilmAdminGroup, cilmOperGroup=cilmOperGroup, cilmCurrentImageLevel=cilmCurrentImageLevel, cilmImageLevelChangedNotif=cilmImageLevelChangedNotif, cilmImageLevelToLicenseMapEntry=cilmImageLevelToLicenseMapEntry, cilmModuleGroups=cilmModuleGroups, ciscoImageLicenseMgmtMIBConform=ciscoImageLicenseMgmtMIBConform, PYSNMP_MODULE_ID=ciscoImageLicenseMgmtMIB, cilmModuleName=cilmModuleName, LicenseNameList=LicenseNameList, cilmImageLevelToLicenseMapTable=cilmImageLevelToLicenseMapTable, cilmConfiguredBootImageLevel=cilmConfiguredBootImageLevel, cilmNextBootLicenseStoreIndex=cilmNextBootLicenseStoreIndex, ciscoImageLicenseMgmtMIB=ciscoImageLicenseMgmtMIB, cilmCurrentLicenseIndex=cilmCurrentLicenseIndex, cilmImageLicensePriority=cilmImageLicensePriority, ciscoImageLicenseMgmtMIBObjects=ciscoImageLicenseMgmtMIBObjects, cilmModuleCompliances=cilmModuleCompliances)
