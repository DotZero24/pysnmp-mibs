#
# PySNMP MIB module FS-VPLS-BGP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/fscom/FS-VPLS-BGP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:01:21 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
fsMgmt, = mibBuilder.importSymbols("FS-SMI", "fsMgmt")
fsvplsConfigIndex, fsvplsPwBindIndex = mibBuilder.importSymbols("FS-VPLS-GENERIC-MIB", "fsvplsConfigIndex", "fsvplsPwBindIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
transmission, MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "transmission", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
StorageType, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "StorageType", "RowStatus", "DisplayString", "TextualConvention")
fsvplsBgpDraft01MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 79))
fsvplsBgpDraft01MIB.setRevisions(('2010-04-28 12:00',))
if mibBuilder.loadTexts: fsvplsBgpDraft01MIB.setLastUpdated('201004281200Z')
if mibBuilder.loadTexts: fsvplsBgpDraft01MIB.setOrganization('FS.COM Inc..')
class FSVplsBgpRouteDistinguisher(TextualConvention, OctetString):
    reference = '[RFC4364]'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class FSVplsBgpRouteTarget(TextualConvention, OctetString):
    reference = '[RFC4364]'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

fsvplsBgpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 79, 1))
fsvplsBgpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 79, 2))
fsvplsBgpVETable = MibTable((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 79, 1, 1), )
if mibBuilder.loadTexts: fsvplsBgpVETable.setStatus('current')
fsvplsBgpVEEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 79, 1, 1, 1), ).setIndexNames((0, "FS-VPLS-GENERIC-MIB", "fsvplsConfigIndex"), (0, "FS-VPLS-BGP-MIB", "fsvplsBgpVEindex"))
if mibBuilder.loadTexts: fsvplsBgpVEEntry.setStatus('current')
fsvplsBgpVEindex = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 79, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: fsvplsBgpVEindex.setStatus('current')
fsvplsBgpVEId = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 79, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 256))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fsvplsBgpVEId.setStatus('current')
fsvplsBgpRangeSize = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 79, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 256)).clone(16)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fsvplsBgpRangeSize.setStatus('current')
fsvplsBgpVEPreference = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 79, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsvplsBgpVEPreference.setStatus('current')
fsvplsBgpVERowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 79, 1, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fsvplsBgpVERowStatus.setStatus('current')
fsvplsBgpPwBindTable = MibTable((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 79, 1, 2), )
if mibBuilder.loadTexts: fsvplsBgpPwBindTable.setStatus('current')
fsvplsBgpPwBindEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 79, 1, 2, 1), ).setIndexNames((0, "FS-VPLS-GENERIC-MIB", "fsvplsConfigIndex"), (0, "FS-VPLS-GENERIC-MIB", "fsvplsPwBindIndex"))
if mibBuilder.loadTexts: fsvplsBgpPwBindEntry.setStatus('current')
fsvplsBgpPwBindLocalVEId = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 79, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsvplsBgpPwBindLocalVEId.setStatus('current')
fsvplsBgpPwBindRemoteVEId = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 79, 1, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsvplsBgpPwBindRemoteVEId.setStatus('current')
fsvplsBgpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 79, 2, 1))
fsvplsBgpModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 79, 2, 1, 1)).setObjects(("FS-VPLS-BGP-MIB", "fsvplsBgpVEGroup"), ("FS-VPLS-BGP-MIB", "fsvplsBgpPwBindGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fsvplsBgpModuleFullCompliance = fsvplsBgpModuleFullCompliance.setStatus('current')
fsvplsBgpModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 79, 2, 1, 2)).setObjects(("FS-VPLS-BGP-MIB", "fsvplsBgpVEGroup"), ("FS-VPLS-BGP-MIB", "fsvplsBgpPwBindGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fsvplsBgpModuleReadOnlyCompliance = fsvplsBgpModuleReadOnlyCompliance.setStatus('current')
fsvplsBgpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 79, 2, 2))
fsvplsBgpVEGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 79, 2, 2, 2)).setObjects(("FS-VPLS-BGP-MIB", "fsvplsBgpVEPreference"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fsvplsBgpVEGroup = fsvplsBgpVEGroup.setStatus('current')
fsvplsBgpPwBindGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 79, 2, 2, 3)).setObjects(("FS-VPLS-BGP-MIB", "fsvplsBgpPwBindLocalVEId"), ("FS-VPLS-BGP-MIB", "fsvplsBgpPwBindRemoteVEId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fsvplsBgpPwBindGroup = fsvplsBgpPwBindGroup.setStatus('current')
mibBuilder.exportSymbols("FS-VPLS-BGP-MIB", FSVplsBgpRouteDistinguisher=FSVplsBgpRouteDistinguisher, fsvplsBgpDraft01MIB=fsvplsBgpDraft01MIB, fsvplsBgpVEGroup=fsvplsBgpVEGroup, FSVplsBgpRouteTarget=FSVplsBgpRouteTarget, fsvplsBgpVEEntry=fsvplsBgpVEEntry, fsvplsBgpVEPreference=fsvplsBgpVEPreference, fsvplsBgpVEindex=fsvplsBgpVEindex, fsvplsBgpVETable=fsvplsBgpVETable, fsvplsBgpConformance=fsvplsBgpConformance, fsvplsBgpVEId=fsvplsBgpVEId, fsvplsBgpPwBindLocalVEId=fsvplsBgpPwBindLocalVEId, fsvplsBgpPwBindTable=fsvplsBgpPwBindTable, PYSNMP_MODULE_ID=fsvplsBgpDraft01MIB, fsvplsBgpPwBindEntry=fsvplsBgpPwBindEntry, fsvplsBgpVERowStatus=fsvplsBgpVERowStatus, fsvplsBgpCompliances=fsvplsBgpCompliances, fsvplsBgpObjects=fsvplsBgpObjects, fsvplsBgpRangeSize=fsvplsBgpRangeSize, fsvplsBgpPwBindGroup=fsvplsBgpPwBindGroup, fsvplsBgpModuleReadOnlyCompliance=fsvplsBgpModuleReadOnlyCompliance, fsvplsBgpModuleFullCompliance=fsvplsBgpModuleFullCompliance, fsvplsBgpGroups=fsvplsBgpGroups, fsvplsBgpPwBindRemoteVEId=fsvplsBgpPwBindRemoteVEId)
