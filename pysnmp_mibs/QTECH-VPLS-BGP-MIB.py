#
# PySNMP MIB module QTECH-VPLS-BGP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/qtech/QTECH-VPLS-BGP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:06:11 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
qtechMgmt, = mibBuilder.importSymbols("QTECH-SMI", "qtechMgmt")
qtechvplsConfigIndex, qtechvplsPwBindIndex = mibBuilder.importSymbols("QTECH-VPLS-GENERIC-MIB", "qtechvplsConfigIndex", "qtechvplsPwBindIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, transmission, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "transmission", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention, RowStatus, StorageType = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus", "StorageType")
qtechvplsBgpDraft01MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 79))
qtechvplsBgpDraft01MIB.setRevisions(('2010-04-28 12:00',))
if mibBuilder.loadTexts: qtechvplsBgpDraft01MIB.setLastUpdated('201004281200Z')
if mibBuilder.loadTexts: qtechvplsBgpDraft01MIB.setOrganization('Qtech Networks Co.,Ltd.')
class QtechVplsBgpRouteDistinguisher(TextualConvention, OctetString):
    reference = '[RFC4364]'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class QtechVplsBgpRouteTarget(TextualConvention, OctetString):
    reference = '[RFC4364]'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

qtechvplsBgpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 79, 1))
qtechvplsBgpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 79, 2))
qtechvplsBgpVETable = MibTable((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 79, 1, 1), )
if mibBuilder.loadTexts: qtechvplsBgpVETable.setStatus('current')
qtechvplsBgpVEEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 79, 1, 1, 1), ).setIndexNames((0, "QTECH-VPLS-GENERIC-MIB", "qtechvplsConfigIndex"), (0, "QTECH-VPLS-BGP-MIB", "qtechvplsBgpVEindex"))
if mibBuilder.loadTexts: qtechvplsBgpVEEntry.setStatus('current')
qtechvplsBgpVEindex = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 79, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: qtechvplsBgpVEindex.setStatus('current')
qtechvplsBgpVEId = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 79, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 256))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qtechvplsBgpVEId.setStatus('current')
qtechvplsBgpRangeSize = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 79, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 256)).clone(16)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qtechvplsBgpRangeSize.setStatus('current')
qtechvplsBgpVEPreference = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 79, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechvplsBgpVEPreference.setStatus('current')
qtechvplsBgpVERowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 79, 1, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qtechvplsBgpVERowStatus.setStatus('current')
qtechvplsBgpPwBindTable = MibTable((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 79, 1, 2), )
if mibBuilder.loadTexts: qtechvplsBgpPwBindTable.setStatus('current')
qtechvplsBgpPwBindEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 79, 1, 2, 1), ).setIndexNames((0, "QTECH-VPLS-GENERIC-MIB", "qtechvplsConfigIndex"), (0, "QTECH-VPLS-GENERIC-MIB", "qtechvplsPwBindIndex"))
if mibBuilder.loadTexts: qtechvplsBgpPwBindEntry.setStatus('current')
qtechvplsBgpPwBindLocalVEId = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 79, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechvplsBgpPwBindLocalVEId.setStatus('current')
qtechvplsBgpPwBindRemoteVEId = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 79, 1, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechvplsBgpPwBindRemoteVEId.setStatus('current')
qtechvplsBgpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 79, 2, 1))
qtechvplsBgpModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 79, 2, 1, 1)).setObjects(("QTECH-VPLS-BGP-MIB", "qtechvplsBgpConfigGroup"), ("QTECH-VPLS-BGP-MIB", "qtechvplsBgpVEGroup"), ("QTECH-VPLS-BGP-MIB", "qtechvplsBgpPwBindGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qtechvplsBgpModuleFullCompliance = qtechvplsBgpModuleFullCompliance.setStatus('current')
qtechvplsBgpModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 79, 2, 1, 2)).setObjects(("QTECH-VPLS-BGP-MIB", "qtechvplsBgpConfigGroup"), ("QTECH-VPLS-BGP-MIB", "qtechvplsBgpVEGroup"), ("QTECH-VPLS-BGP-MIB", "qtechvplsBgpPwBindGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qtechvplsBgpModuleReadOnlyCompliance = qtechvplsBgpModuleReadOnlyCompliance.setStatus('current')
qtechvplsBgpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 79, 2, 2))
qtechvplsBgpVEGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 79, 2, 2, 2)).setObjects(("QTECH-VPLS-BGP-MIB", "qtechvplsBgpVEPreference"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qtechvplsBgpVEGroup = qtechvplsBgpVEGroup.setStatus('current')
qtechvplsBgpPwBindGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 79, 2, 2, 3)).setObjects(("QTECH-VPLS-BGP-MIB", "qtechvplsBgpPwBindLocalVEId"), ("QTECH-VPLS-BGP-MIB", "qtechvplsBgpPwBindRemoteVEId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qtechvplsBgpPwBindGroup = qtechvplsBgpPwBindGroup.setStatus('current')
mibBuilder.exportSymbols("QTECH-VPLS-BGP-MIB", qtechvplsBgpVEId=qtechvplsBgpVEId, qtechvplsBgpVERowStatus=qtechvplsBgpVERowStatus, qtechvplsBgpPwBindTable=qtechvplsBgpPwBindTable, QtechVplsBgpRouteTarget=QtechVplsBgpRouteTarget, qtechvplsBgpVEEntry=qtechvplsBgpVEEntry, qtechvplsBgpRangeSize=qtechvplsBgpRangeSize, qtechvplsBgpObjects=qtechvplsBgpObjects, qtechvplsBgpVEPreference=qtechvplsBgpVEPreference, qtechvplsBgpPwBindEntry=qtechvplsBgpPwBindEntry, qtechvplsBgpCompliances=qtechvplsBgpCompliances, qtechvplsBgpModuleFullCompliance=qtechvplsBgpModuleFullCompliance, qtechvplsBgpModuleReadOnlyCompliance=qtechvplsBgpModuleReadOnlyCompliance, qtechvplsBgpPwBindRemoteVEId=qtechvplsBgpPwBindRemoteVEId, qtechvplsBgpConformance=qtechvplsBgpConformance, qtechvplsBgpPwBindLocalVEId=qtechvplsBgpPwBindLocalVEId, qtechvplsBgpVEGroup=qtechvplsBgpVEGroup, qtechvplsBgpVEindex=qtechvplsBgpVEindex, qtechvplsBgpVETable=qtechvplsBgpVETable, qtechvplsBgpPwBindGroup=qtechvplsBgpPwBindGroup, PYSNMP_MODULE_ID=qtechvplsBgpDraft01MIB, QtechVplsBgpRouteDistinguisher=QtechVplsBgpRouteDistinguisher, qtechvplsBgpDraft01MIB=qtechvplsBgpDraft01MIB, qtechvplsBgpGroups=qtechvplsBgpGroups)
