#
# PySNMP MIB module CISCO-IMAGE-LICENSE-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-IMAGE-LICENSE-MGMT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:32:18 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("CISCO-IMAGE-LICENSE-MGMT-MIB", cilmCurrentLicenseStoreIndex=cilmCurrentLicenseStoreIndex, ciscoImageLicenseMgmtMIBNotifs=ciscoImageLicenseMgmtMIBNotifs, cilmImageLicenseName=cilmImageLicenseName, cilmCurrentImageLevel=cilmCurrentImageLevel, cilmNextBootImageLevel=cilmNextBootImageLevel, ciscoImageLicenseMgmtMIBObjects=ciscoImageLicenseMgmtMIBObjects, cilmNotifCntl=cilmNotifCntl, cilmBootImageLevelTable=cilmBootImageLevelTable, cilmModuleCompliances=cilmModuleCompliances, cilmModuleCompliance=cilmModuleCompliance, cilmOperGroup=cilmOperGroup, cilmNextBootLicenseIndex=cilmNextBootLicenseIndex, PYSNMP_MODULE_ID=ciscoImageLicenseMgmtMIB, cilmImageLicensePriority=cilmImageLicensePriority, cilmImageLevelChangedNotif=cilmImageLevelChangedNotif, cilmConfiguredBootImageLevel=cilmConfiguredBootImageLevel, BootImageLevel=BootImageLevel, cilmImageLicenseMapIndex=cilmImageLicenseMapIndex, cilmBootImageLevelChanged=cilmBootImageLevelChanged, ciscoImageLicenseMgmtMIB=ciscoImageLicenseMgmtMIB, cilmModuleGroups=cilmModuleGroups, cilmImageLevelToLicenseMapTable=cilmImageLevelToLicenseMapTable, cilmModuleName=cilmModuleName, ciscoImageLicenseMgmtMIBConform=ciscoImageLicenseMgmtMIBConform, cilmCurrentLicenseIndex=cilmCurrentLicenseIndex, cilmNextBootLicenseStoreIndex=cilmNextBootLicenseStoreIndex, cilmBootImageLevelEntry=cilmBootImageLevelEntry, cilmImageLevelToLicenseMapEntry=cilmImageLevelToLicenseMapEntry, cilmAdminGroup=cilmAdminGroup, LicenseNameList=LicenseNameList, cilmEULAAccepted=cilmEULAAccepted, cilmImageLicenseImageLevel=cilmImageLicenseImageLevel, cilmNotifGroup=cilmNotifGroup)
