#
# PySNMP MIB module QTECH-VPLS-BGP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/qtech/QTECH-VPLS-BGP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:14:06 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
qtechMgmt, = mibBuilder.importSymbols("QTECH-SMI", "qtechMgmt")
qtechvplsConfigIndex, qtechvplsPwBindIndex = mibBuilder.importSymbols("QTECH-VPLS-GENERIC-MIB", "qtechvplsConfigIndex", "qtechvplsPwBindIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
transmission, MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "transmission", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
StorageType, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "StorageType", "RowStatus", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("QTECH-VPLS-BGP-MIB", qtechvplsBgpVEId=qtechvplsBgpVEId, qtechvplsBgpModuleFullCompliance=qtechvplsBgpModuleFullCompliance, qtechvplsBgpPwBindLocalVEId=qtechvplsBgpPwBindLocalVEId, qtechvplsBgpCompliances=qtechvplsBgpCompliances, QtechVplsBgpRouteDistinguisher=QtechVplsBgpRouteDistinguisher, qtechvplsBgpDraft01MIB=qtechvplsBgpDraft01MIB, qtechvplsBgpVERowStatus=qtechvplsBgpVERowStatus, qtechvplsBgpVETable=qtechvplsBgpVETable, qtechvplsBgpPwBindTable=qtechvplsBgpPwBindTable, qtechvplsBgpVEEntry=qtechvplsBgpVEEntry, qtechvplsBgpVEGroup=qtechvplsBgpVEGroup, qtechvplsBgpRangeSize=qtechvplsBgpRangeSize, qtechvplsBgpPwBindRemoteVEId=qtechvplsBgpPwBindRemoteVEId, QtechVplsBgpRouteTarget=QtechVplsBgpRouteTarget, qtechvplsBgpPwBindEntry=qtechvplsBgpPwBindEntry, qtechvplsBgpVEPreference=qtechvplsBgpVEPreference, PYSNMP_MODULE_ID=qtechvplsBgpDraft01MIB, qtechvplsBgpModuleReadOnlyCompliance=qtechvplsBgpModuleReadOnlyCompliance, qtechvplsBgpVEindex=qtechvplsBgpVEindex, qtechvplsBgpPwBindGroup=qtechvplsBgpPwBindGroup, qtechvplsBgpObjects=qtechvplsBgpObjects, qtechvplsBgpConformance=qtechvplsBgpConformance, qtechvplsBgpGroups=qtechvplsBgpGroups)
