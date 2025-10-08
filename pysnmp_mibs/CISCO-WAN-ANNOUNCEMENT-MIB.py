#
# PySNMP MIB module CISCO-WAN-ANNOUNCEMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-WAN-ANNOUNCEMENT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:14:44 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoWanAnnouncementMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 25))
ciscoWanAnnouncementMIB.setRevisions(('2003-12-22 00:00', '2001-12-26 00:00',))
if mibBuilder.loadTexts: ciscoWanAnnouncementMIB.setLastUpdated('200312220000Z')
if mibBuilder.loadTexts: ciscoWanAnnouncementMIB.setOrganization('Cisco Systems, Inc.')
cwAnnounceGrpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 25, 1))
cwAnnounceGeneric = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 25, 1, 1))
cwAnnounceControlGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 25, 1, 1, 1))
cwAnnounceTableGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 25, 1, 1, 2))
class AnnCodecType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 7, 8, 9, 11, 12, 13, 14))
    namedValues = NamedValues(("g711u", 1), ("g711a", 2), ("g726r32000", 3), ("g729a", 4), ("g729ab", 5), ("g726r16000", 7), ("g726r24000", 8), ("g726r40000", 9), ("g723h", 11), ("g723ah", 12), ("g723l", 13), ("g723al", 14))

cwAnnMaximumSize = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 25, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwAnnMaximumSize.setStatus('current')
cwAnnFileServerName = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 25, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)).clone(' ')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwAnnFileServerName.setStatus('current')
cwAnnAgeTime = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 25, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(10080)).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwAnnAgeTime.setStatus('current')
cwAnnPreferenceCodec = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 25, 1, 1, 1, 4), AnnCodecType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwAnnPreferenceCodec.setStatus('current')
cwAnnPrefixPath = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 25, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)).clone(' ')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwAnnPrefixPath.setStatus('current')
cwAnnReqTimeout = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 25, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(5)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwAnnReqTimeout.setStatus('current')
cwAnnounceTable = MibTable((1, 3, 6, 1, 4, 1, 351, 150, 25, 1, 1, 2, 1), )
if mibBuilder.loadTexts: cwAnnounceTable.setStatus('current')
cwAnnounceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 150, 25, 1, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-WAN-ANNOUNCEMENT-MIB", "cwAnnounceNumber"))
if mibBuilder.loadTexts: cwAnnounceEntry.setStatus('current')
cwAnnounceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 25, 1, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: cwAnnounceNumber.setStatus('current')
cwAnnFileStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 25, 1, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("loaded", 1), ("loading", 2), ("invalidFile", 3), ("loadFailed", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwAnnFileStatus.setStatus('current')
cwAnnFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 25, 1, 1, 2, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwAnnFileName.setStatus('current')
cwAnnFileCodec = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 25, 1, 1, 2, 1, 1, 4), AnnCodecType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwAnnFileCodec.setStatus('current')
cwAnnRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 25, 1, 1, 2, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwAnnRowStatus.setStatus('current')
cwAnnounceNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 25, 2))
cwAnnounceNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 25, 2, 0))
cwAnnounceMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 25, 3))
cwAnnounceMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 25, 3, 1))
cwAnnounceMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 25, 3, 2))
announceMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 25, 3, 1, 1)).setObjects(("CISCO-WAN-ANNOUNCEMENT-MIB", "cwAnnounceControlGroup"), ("CISCO-WAN-ANNOUNCEMENT-MIB", "cwAnnounceTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    announceMIBCompliance = announceMIBCompliance.setStatus('current')
cwAnnounceControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 25, 3, 2, 1)).setObjects(("CISCO-WAN-ANNOUNCEMENT-MIB", "cwAnnMaximumSize"), ("CISCO-WAN-ANNOUNCEMENT-MIB", "cwAnnFileServerName"), ("CISCO-WAN-ANNOUNCEMENT-MIB", "cwAnnAgeTime"), ("CISCO-WAN-ANNOUNCEMENT-MIB", "cwAnnPreferenceCodec"), ("CISCO-WAN-ANNOUNCEMENT-MIB", "cwAnnPrefixPath"), ("CISCO-WAN-ANNOUNCEMENT-MIB", "cwAnnReqTimeout"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAnnounceControlGroup = cwAnnounceControlGroup.setStatus('current')
cwAnnounceTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 25, 3, 2, 2)).setObjects(("CISCO-WAN-ANNOUNCEMENT-MIB", "cwAnnFileStatus"), ("CISCO-WAN-ANNOUNCEMENT-MIB", "cwAnnFileName"), ("CISCO-WAN-ANNOUNCEMENT-MIB", "cwAnnFileCodec"), ("CISCO-WAN-ANNOUNCEMENT-MIB", "cwAnnRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAnnounceTableGroup = cwAnnounceTableGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-ANNOUNCEMENT-MIB", cwAnnounceEntry=cwAnnounceEntry, ciscoWanAnnouncementMIB=ciscoWanAnnouncementMIB, cwAnnounceGrpMIBObjects=cwAnnounceGrpMIBObjects, cwAnnPrefixPath=cwAnnPrefixPath, cwAnnFileCodec=cwAnnFileCodec, cwAnnounceMIBConformance=cwAnnounceMIBConformance, cwAnnounceMIBCompliances=cwAnnounceMIBCompliances, cwAnnFileStatus=cwAnnFileStatus, cwAnnounceMIBGroups=cwAnnounceMIBGroups, announceMIBCompliance=announceMIBCompliance, cwAnnounceGeneric=cwAnnounceGeneric, cwAnnounceControlGroup=cwAnnounceControlGroup, cwAnnReqTimeout=cwAnnReqTimeout, AnnCodecType=AnnCodecType, cwAnnMaximumSize=cwAnnMaximumSize, cwAnnounceNumber=cwAnnounceNumber, PYSNMP_MODULE_ID=ciscoWanAnnouncementMIB, cwAnnounceControlGrp=cwAnnounceControlGrp, cwAnnounceTable=cwAnnounceTable, cwAnnRowStatus=cwAnnRowStatus, cwAnnounceNotifications=cwAnnounceNotifications, cwAnnPreferenceCodec=cwAnnPreferenceCodec, cwAnnAgeTime=cwAnnAgeTime, cwAnnounceNotificationPrefix=cwAnnounceNotificationPrefix, cwAnnounceTableGrp=cwAnnounceTableGrp, cwAnnFileServerName=cwAnnFileServerName, cwAnnFileName=cwAnnFileName, cwAnnounceTableGroup=cwAnnounceTableGroup)
