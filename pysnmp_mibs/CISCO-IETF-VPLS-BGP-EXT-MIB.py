#
# PySNMP MIB module CISCO-IETF-VPLS-BGP-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-IETF-VPLS-BGP-EXT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:15:09 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
cvplsConfigIndex, cvplsPwBindIndex = mibBuilder.importSymbols("CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigIndex", "cvplsPwBindIndex")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention, RowStatus, StorageType = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus", "StorageType")
ciscoIetfVplsBgpExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 140))
ciscoIetfVplsBgpExtMIB.setRevisions(('2008-10-24 00:00',))
if mibBuilder.loadTexts: ciscoIetfVplsBgpExtMIB.setLastUpdated('200810240000Z')
if mibBuilder.loadTexts: ciscoIetfVplsBgpExtMIB.setOrganization('Cisco Systems, Inc.')
class CiVplsBgpExtRouteDistinguisher(TextualConvention, OctetString):
    reference = '[RFC4364]'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class CiVplsBgpExtRouteTarget(TextualConvention, OctetString):
    reference = '[RFC4364]'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class CiVplsBgpExtRouteTargetType(TextualConvention, Integer32):
    reference = '[RFC 4364]'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("import", 1), ("export", 2), ("both", 3))

class CiVplsBgpExtVEID(TextualConvention, Unsigned32):
    status = 'current'

ciscoIetfVplsBgpExtMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 140, 0))
ciscoIetfVplsBgpExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 140, 1))
ciscoIetfVplsBgpExtMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 140, 2))
ciVplsBgpExtConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 1), )
if mibBuilder.loadTexts: ciVplsBgpExtConfigTable.setStatus('current')
ciVplsBgpExtConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 1, 1), ).setIndexNames((0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigIndex"))
if mibBuilder.loadTexts: ciVplsBgpExtConfigEntry.setStatus('current')
ciVplsBgpExtConfigRouteDistinguisher = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 1, 1, 1), CiVplsBgpExtRouteDistinguisher()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciVplsBgpExtConfigRouteDistinguisher.setStatus('current')
ciVplsBgpExtConfigVERangeSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciVplsBgpExtConfigVERangeSize.setStatus('current')
civplsBgpExtRTTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 2), )
if mibBuilder.loadTexts: civplsBgpExtRTTable.setStatus('current')
civplsBgpExtRTEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 2, 1), ).setIndexNames((0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigIndex"), (0, "CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtRTType"), (0, "CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtRT"))
if mibBuilder.loadTexts: civplsBgpExtRTEntry.setStatus('current')
ciVplsBgpExtRTType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 2, 1, 1), CiVplsBgpExtRouteTargetType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciVplsBgpExtRTType.setStatus('current')
ciVplsBgpExtRT = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 2, 1, 2), CiVplsBgpExtRouteTarget().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciVplsBgpExtRT.setStatus('current')
ciVplsBgpExtRTStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 2, 1, 3), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciVplsBgpExtRTStorageType.setStatus('current')
ciVplsBgpExtRTRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciVplsBgpExtRTRowStatus.setStatus('current')
ciVplsBgpExtVETable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 3), )
if mibBuilder.loadTexts: ciVplsBgpExtVETable.setStatus('current')
ciVplsBgpExtVEEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 3, 1), ).setIndexNames((0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigIndex"), (0, "CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtVEId"))
if mibBuilder.loadTexts: ciVplsBgpExtVEEntry.setStatus('current')
ciVplsBgpExtVEId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 3, 1, 1), CiVplsBgpExtVEID())
if mibBuilder.loadTexts: ciVplsBgpExtVEId.setStatus('current')
ciVplsBgpExtVEName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 3, 1, 2), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciVplsBgpExtVEName.setStatus('current')
ciVplsBgpExtVEPreference = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 3, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciVplsBgpExtVEPreference.setStatus('current')
ciVplsBgpExtVEStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 3, 1, 5), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciVplsBgpExtVEStorageType.setStatus('current')
ciVplsBgpExtVERowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 3, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciVplsBgpExtVERowStatus.setStatus('current')
ciVplsBgpExtPwBindTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 4), )
if mibBuilder.loadTexts: ciVplsBgpExtPwBindTable.setStatus('current')
ciVplsBgpExtPwBindEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 4, 1), ).setIndexNames((0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigIndex"), (0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsPwBindIndex"))
if mibBuilder.loadTexts: ciVplsBgpExtPwBindEntry.setStatus('current')
ciVplsBgpExtPwBindLocalVEId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 4, 1, 1), CiVplsBgpExtVEID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciVplsBgpExtPwBindLocalVEId.setStatus('current')
ciVplsBgpExtPwBindRemoteVEId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 4, 1, 2), CiVplsBgpExtVEID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciVplsBgpExtPwBindRemoteVEId.setStatus('current')
ciscoIetfVplsBgpExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 140, 2, 1))
ciscoIetfVplsBgpExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 140, 2, 2))
ciscoIetfVplsBgpExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 140, 2, 1, 1)).setObjects(("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtConfigGroup"), ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtRTGroup"), ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtVEGroup"), ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtPwBindGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfVplsBgpExtMIBCompliance = ciscoIetfVplsBgpExtMIBCompliance.setStatus('current')
ciVplsBgpExtConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 140, 2, 2, 1)).setObjects(("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtConfigRouteDistinguisher"), ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtConfigVERangeSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciVplsBgpExtConfigGroup = ciVplsBgpExtConfigGroup.setStatus('current')
ciVplsBgpExtRTGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 140, 2, 2, 2)).setObjects(("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtRTType"), ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtRT"), ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtRTStorageType"), ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtRTRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciVplsBgpExtRTGroup = ciVplsBgpExtRTGroup.setStatus('current')
ciVplsBgpExtVEGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 140, 2, 2, 3)).setObjects(("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtVEName"), ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtVEPreference"), ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtVERowStatus"), ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtVEStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciVplsBgpExtVEGroup = ciVplsBgpExtVEGroup.setStatus('current')
ciVplsBgpExtPwBindGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 140, 2, 2, 4)).setObjects(("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtPwBindLocalVEId"), ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtPwBindRemoteVEId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciVplsBgpExtPwBindGroup = ciVplsBgpExtPwBindGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-IETF-VPLS-BGP-EXT-MIB", ciVplsBgpExtConfigRouteDistinguisher=ciVplsBgpExtConfigRouteDistinguisher, ciVplsBgpExtRTGroup=ciVplsBgpExtRTGroup, ciVplsBgpExtRTType=ciVplsBgpExtRTType, ciVplsBgpExtConfigGroup=ciVplsBgpExtConfigGroup, ciVplsBgpExtPwBindEntry=ciVplsBgpExtPwBindEntry, ciVplsBgpExtConfigTable=ciVplsBgpExtConfigTable, ciscoIetfVplsBgpExtMIBObjects=ciscoIetfVplsBgpExtMIBObjects, CiVplsBgpExtRouteTarget=CiVplsBgpExtRouteTarget, ciVplsBgpExtVETable=ciVplsBgpExtVETable, ciVplsBgpExtVERowStatus=ciVplsBgpExtVERowStatus, CiVplsBgpExtRouteTargetType=CiVplsBgpExtRouteTargetType, ciscoIetfVplsBgpExtMIBCompliance=ciscoIetfVplsBgpExtMIBCompliance, ciVplsBgpExtRTRowStatus=ciVplsBgpExtRTRowStatus, ciVplsBgpExtPwBindLocalVEId=ciVplsBgpExtPwBindLocalVEId, ciVplsBgpExtPwBindGroup=ciVplsBgpExtPwBindGroup, CiVplsBgpExtVEID=CiVplsBgpExtVEID, ciVplsBgpExtVEGroup=ciVplsBgpExtVEGroup, ciscoIetfVplsBgpExtMIB=ciscoIetfVplsBgpExtMIB, civplsBgpExtRTTable=civplsBgpExtRTTable, ciVplsBgpExtVEStorageType=ciVplsBgpExtVEStorageType, ciVplsBgpExtVEId=ciVplsBgpExtVEId, ciVplsBgpExtVEPreference=ciVplsBgpExtVEPreference, ciscoIetfVplsBgpExtMIBCompliances=ciscoIetfVplsBgpExtMIBCompliances, ciscoIetfVplsBgpExtMIBNotifs=ciscoIetfVplsBgpExtMIBNotifs, ciscoIetfVplsBgpExtMIBGroups=ciscoIetfVplsBgpExtMIBGroups, CiVplsBgpExtRouteDistinguisher=CiVplsBgpExtRouteDistinguisher, ciVplsBgpExtConfigVERangeSize=ciVplsBgpExtConfigVERangeSize, ciVplsBgpExtVEEntry=ciVplsBgpExtVEEntry, ciVplsBgpExtConfigEntry=ciVplsBgpExtConfigEntry, ciscoIetfVplsBgpExtMIBConform=ciscoIetfVplsBgpExtMIBConform, ciVplsBgpExtVEName=ciVplsBgpExtVEName, civplsBgpExtRTEntry=civplsBgpExtRTEntry, ciVplsBgpExtPwBindRemoteVEId=ciVplsBgpExtPwBindRemoteVEId, PYSNMP_MODULE_ID=ciscoIetfVplsBgpExtMIB, ciVplsBgpExtPwBindTable=ciVplsBgpExtPwBindTable, ciVplsBgpExtRTStorageType=ciVplsBgpExtRTStorageType, ciVplsBgpExtRT=ciVplsBgpExtRT)
