#
# PySNMP MIB module CISCO-MOBILITY-TAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-MOBILITY-TAP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:31:05 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
cTap2StreamIndex, cTap2MediationContentId = mibBuilder.importSymbols("CISCO-TAP2-MIB", "cTap2StreamIndex", "cTap2MediationContentId")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, StorageType, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "StorageType", "TruthValue", "DisplayString")
ciscoMobilityTapMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 672))
ciscoMobilityTapMIB.setRevisions(('2010-06-16 00:00', '2010-04-15 00:00', '2008-08-05 00:00',))
if mibBuilder.loadTexts: ciscoMobilityTapMIB.setLastUpdated('201006160000Z')
if mibBuilder.loadTexts: ciscoMobilityTapMIB.setOrganization('Cisco Systems, Inc.')
ciscoMobilityTapMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 672, 0))
ciscoMobilityTapMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 672, 1))
ciscoMobilityTapMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 672, 2))
cmtapStreamGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1))
class CmtapLawfulInterceptID(TextualConvention, OctetString):
    status = 'current'
    displayHint = '256a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 256)

class CmtapSubscriberIDType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 1), ("msid", 2), ("imsi", 3), ("nai", 4), ("esn", 5), ("servedMdn", 6))

class CmtapSubscriberID(TextualConvention, OctetString):
    status = 'current'
    displayHint = '256a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 256)

cmtapStreamCapabilities = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 1), Bits().clone(namedValues=NamedValues(("tapEnable", 0), ("interface", 1), ("calledSubscriberID", 2), ("nonvolatileStorage", 3), ("msid", 4), ("imsi", 5), ("nai", 6), ("esn", 7), ("servedMdn", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmtapStreamCapabilities.setStatus('current')
cmtapStreamTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2), )
if mibBuilder.loadTexts: cmtapStreamTable.setStatus('current')
cmtapStreamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-TAP2-MIB", "cTap2MediationContentId"), (0, "CISCO-TAP2-MIB", "cTap2StreamIndex"))
if mibBuilder.loadTexts: cmtapStreamEntry.setStatus('current')
cmtapStreamCalledSubscriberIDType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1, 1), CmtapSubscriberIDType().clone('unknown')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmtapStreamCalledSubscriberIDType.setStatus('current')
cmtapStreamCalledSubscriberID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1, 2), CmtapSubscriberID()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmtapStreamCalledSubscriberID.setStatus('current')
cmtapStreamSubscriberIDType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1, 3), CmtapSubscriberIDType().clone('unknown')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmtapStreamSubscriberIDType.setStatus('current')
cmtapStreamSubscriberID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1, 4), CmtapSubscriberID()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmtapStreamSubscriberID.setStatus('current')
cmtapStreamStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1, 5), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmtapStreamStorageType.setStatus('current')
cmtapStreamStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmtapStreamStatus.setStatus('current')
cmtapStreamLIIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1, 7), CmtapLawfulInterceptID().clone('not set')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmtapStreamLIIdentifier.setStatus('current')
cmtapStreamLocationInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1, 8), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmtapStreamLocationInfo.setStatus('current')
cmtapStreamInterceptType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ccOnly", 1), ("iriOnly", 2), ("both", 3))).clone('both')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmtapStreamInterceptType.setStatus('current')
ciscoMobilityTapMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 672, 2, 1))
ciscoMobilityTapMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 672, 2, 2))
ciscoMobilityTapMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 672, 2, 1, 1)).setObjects(("CISCO-MOBILITY-TAP-MIB", "ciscoMobilityTapCapabilityGroup"), ("CISCO-MOBILITY-TAP-MIB", "ciscoMobilityTapStreamGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMobilityTapMIBCompliance = ciscoMobilityTapMIBCompliance.setStatus('deprecated')
ciscoMobilityTapMIBComplianceRev01 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 672, 2, 1, 2)).setObjects(("CISCO-MOBILITY-TAP-MIB", "ciscoMobilityTapCapabilityGroup"), ("CISCO-MOBILITY-TAP-MIB", "ciscoMobilityTapStreamGroup"), ("CISCO-MOBILITY-TAP-MIB", "ciscoMobilityTapStreamGroupSup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMobilityTapMIBComplianceRev01 = ciscoMobilityTapMIBComplianceRev01.setStatus('current')
ciscoMobilityTapCapabilityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 672, 2, 2, 1)).setObjects(("CISCO-MOBILITY-TAP-MIB", "cmtapStreamCapabilities"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMobilityTapCapabilityGroup = ciscoMobilityTapCapabilityGroup.setStatus('current')
ciscoMobilityTapStreamGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 672, 2, 2, 2)).setObjects(("CISCO-MOBILITY-TAP-MIB", "cmtapStreamCalledSubscriberIDType"), ("CISCO-MOBILITY-TAP-MIB", "cmtapStreamCalledSubscriberID"), ("CISCO-MOBILITY-TAP-MIB", "cmtapStreamSubscriberIDType"), ("CISCO-MOBILITY-TAP-MIB", "cmtapStreamSubscriberID"), ("CISCO-MOBILITY-TAP-MIB", "cmtapStreamStorageType"), ("CISCO-MOBILITY-TAP-MIB", "cmtapStreamStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMobilityTapStreamGroup = ciscoMobilityTapStreamGroup.setStatus('current')
ciscoMobilityTapStreamGroupSup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 672, 2, 2, 3)).setObjects(("CISCO-MOBILITY-TAP-MIB", "cmtapStreamLIIdentifier"), ("CISCO-MOBILITY-TAP-MIB", "cmtapStreamLocationInfo"), ("CISCO-MOBILITY-TAP-MIB", "cmtapStreamInterceptType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMobilityTapStreamGroupSup1 = ciscoMobilityTapStreamGroupSup1.setStatus('current')
mibBuilder.exportSymbols("CISCO-MOBILITY-TAP-MIB", PYSNMP_MODULE_ID=ciscoMobilityTapMIB, CmtapSubscriberIDType=CmtapSubscriberIDType, cmtapStreamSubscriberID=cmtapStreamSubscriberID, cmtapStreamInterceptType=cmtapStreamInterceptType, cmtapStreamCalledSubscriberIDType=cmtapStreamCalledSubscriberIDType, ciscoMobilityTapMIBCompliances=ciscoMobilityTapMIBCompliances, cmtapStreamCapabilities=cmtapStreamCapabilities, ciscoMobilityTapMIBObjects=ciscoMobilityTapMIBObjects, ciscoMobilityTapMIBComplianceRev01=ciscoMobilityTapMIBComplianceRev01, cmtapStreamStorageType=cmtapStreamStorageType, CmtapSubscriberID=CmtapSubscriberID, cmtapStreamLocationInfo=cmtapStreamLocationInfo, cmtapStreamSubscriberIDType=cmtapStreamSubscriberIDType, cmtapStreamGroup=cmtapStreamGroup, CmtapLawfulInterceptID=CmtapLawfulInterceptID, ciscoMobilityTapMIBNotifs=ciscoMobilityTapMIBNotifs, ciscoMobilityTapStreamGroupSup1=ciscoMobilityTapStreamGroupSup1, cmtapStreamLIIdentifier=cmtapStreamLIIdentifier, cmtapStreamTable=cmtapStreamTable, cmtapStreamCalledSubscriberID=cmtapStreamCalledSubscriberID, ciscoMobilityTapCapabilityGroup=ciscoMobilityTapCapabilityGroup, ciscoMobilityTapStreamGroup=ciscoMobilityTapStreamGroup, cmtapStreamStatus=cmtapStreamStatus, ciscoMobilityTapMIB=ciscoMobilityTapMIB, cmtapStreamEntry=cmtapStreamEntry, ciscoMobilityTapMIBCompliance=ciscoMobilityTapMIBCompliance, ciscoMobilityTapMIBConform=ciscoMobilityTapMIBConform, ciscoMobilityTapMIBGroups=ciscoMobilityTapMIBGroups)
