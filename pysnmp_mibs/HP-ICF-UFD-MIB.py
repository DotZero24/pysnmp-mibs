#
# PySNMP MIB module HP-ICF-UFD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/HP-ICF-UFD-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:02:48 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
hpicfUfdMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74))
hpicfUfdMIB.setRevisions(('2018-05-23 00:00', '2012-04-30 00:00', '2011-05-12 00:00', '2010-02-06 15:39',))
if mibBuilder.loadTexts: hpicfUfdMIB.setLastUpdated('201805230000Z')
if mibBuilder.loadTexts: hpicfUfdMIB.setOrganization('HP Networking')
hpicfUfdNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 0))
hpicfUfdConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1))
hpicfUfdConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 3))
class HpUfdTrackEntityType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("ufd", 1))

class HpUfdTrackLinksSubtype(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("portMap", 1), ("lacpKey", 2))

hpicfUfdScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 1))
hpicfUfdAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfUfdAdminStatus.setStatus('current')
hpicfUfdNotifyTrackId = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4096))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpicfUfdNotifyTrackId.setStatus('current')
hpicfUfdTrackEntities = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2))
hpicfUfdTrackTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 1), )
if mibBuilder.loadTexts: hpicfUfdTrackTable.setStatus('current')
hpicfUfdTrackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 1, 1), ).setIndexNames((0, "HP-ICF-UFD-MIB", "hpicfUfdTrackId"))
if mibBuilder.loadTexts: hpicfUfdTrackEntry.setStatus('current')
hpicfUfdTrackId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4096)))
if mibBuilder.loadTexts: hpicfUfdTrackId.setStatus('current')
hpicfUfdTrackEntityType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 1, 1, 2), HpUfdTrackEntityType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfUfdTrackEntityType.setStatus('current')
hpicfUfdLinksToMonitor = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfUfdLinksToMonitor.setStatus('current')
hpicfUfdLinksToTransition = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfUfdLinksToTransition.setStatus('current')
hpicfUfdLinksToMonitorState = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfUfdLinksToMonitorState.setStatus('current')
hpicfUfdLinksToTransitionState = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("autoDisabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfUfdLinksToTransitionState.setStatus('current')
hpicfUfdTrackEntityState = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("ok", 1), ("failed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfUfdTrackEntityState.setStatus('current')
hpicfUfdTrackEntityRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 1, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfUfdTrackEntityRowStatus.setStatus('current')
hpicfUfdLinksToMonitorType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 1, 1, 9), HpUfdTrackLinksSubtype()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfUfdLinksToMonitorType.setStatus('current')
hpicfUfdLinksToTransitionType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 1, 1, 10), HpUfdTrackLinksSubtype()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfUfdLinksToTransitionType.setStatus('current')
hpicfUfdLinksTransitionDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 300))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfUfdLinksTransitionDelay.setStatus('current')
hpicfUfdTrackedLinkTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 2), )
if mibBuilder.loadTexts: hpicfUfdTrackedLinkTable.setStatus('current')
hpicfUfdTrackedLinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 2, 1), ).setIndexNames((0, "HP-ICF-UFD-MIB", "hpicfUfdTrackId"), (0, "HP-ICF-UFD-MIB", "hpicfUfdIfIndex"))
if mibBuilder.loadTexts: hpicfUfdTrackedLinkEntry.setStatus('current')
hpicfUfdIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hpicfUfdIfIndex.setStatus('current')
hpicfUfdLinkRole = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("uplink", 1), ("downlink", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfUfdLinkRole.setStatus('current')
hpicfUfdNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 0, 0))
hpicfUfdLtDAutoDisabled = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 0, 0, 3)).setObjects(("HP-ICF-UFD-MIB", "hpicfUfdNotifyTrackId"), ("HP-ICF-UFD-MIB", "hpicfUfdLinksToTransition"))
if mibBuilder.loadTexts: hpicfUfdLtDAutoDisabled.setStatus('current')
hpicfUfdLtDAutoEnabled = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 0, 0, 4)).setObjects(("HP-ICF-UFD-MIB", "hpicfUfdNotifyTrackId"), ("HP-ICF-UFD-MIB", "hpicfUfdLinksToTransition"))
if mibBuilder.loadTexts: hpicfUfdLtDAutoEnabled.setStatus('current')
hpicfUfdCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 3, 1))
hpicfUfdGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 3, 2))
hpicfUfdCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 3, 1, 1)).setObjects(("HP-ICF-UFD-MIB", "hpicfUfdBaseGroup"), ("HP-ICF-UFD-MIB", "hpicfUfdConfigGroup"), ("HP-ICF-UFD-MIB", "hpicfUfdNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfUfdCompliance = hpicfUfdCompliance.setStatus('deprecated')
hpicfUfdCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 3, 1, 2)).setObjects(("HP-ICF-UFD-MIB", "hpicfUfdBaseGroup"), ("HP-ICF-UFD-MIB", "hpicfUfdConfigGroup"), ("HP-ICF-UFD-MIB", "hpicfUfdNotificationGroup"), ("HP-ICF-UFD-MIB", "hpicfUfdConfigGroup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfUfdCompliance1 = hpicfUfdCompliance1.setStatus('deprecated')
hpicfUfdCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 3, 1, 3)).setObjects(("HP-ICF-UFD-MIB", "hpicfUfdBaseGroup"), ("HP-ICF-UFD-MIB", "hpicfUfdConfigGroup2"), ("HP-ICF-UFD-MIB", "hpicfUfdNotificationGroup"), ("HP-ICF-UFD-MIB", "hpicfUfdConfigGroup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfUfdCompliance2 = hpicfUfdCompliance2.setStatus('current')
hpicfUfdBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 3, 2, 1)).setObjects(("HP-ICF-UFD-MIB", "hpicfUfdAdminStatus"), ("HP-ICF-UFD-MIB", "hpicfUfdNotifyTrackId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfUfdBaseGroup = hpicfUfdBaseGroup.setStatus('current')
hpicfUfdConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 3, 2, 2)).setObjects(("HP-ICF-UFD-MIB", "hpicfUfdTrackEntityType"), ("HP-ICF-UFD-MIB", "hpicfUfdLinksToMonitor"), ("HP-ICF-UFD-MIB", "hpicfUfdLinksToTransition"), ("HP-ICF-UFD-MIB", "hpicfUfdLinksToMonitorState"), ("HP-ICF-UFD-MIB", "hpicfUfdLinksToTransitionState"), ("HP-ICF-UFD-MIB", "hpicfUfdTrackEntityState"), ("HP-ICF-UFD-MIB", "hpicfUfdTrackEntityRowStatus"), ("HP-ICF-UFD-MIB", "hpicfUfdLinksToMonitorType"), ("HP-ICF-UFD-MIB", "hpicfUfdLinksToTransitionType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfUfdConfigGroup = hpicfUfdConfigGroup.setStatus('deprecated')
hpicfUfdNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 3, 2, 3)).setObjects(("HP-ICF-UFD-MIB", "hpicfUfdLtDAutoDisabled"), ("HP-ICF-UFD-MIB", "hpicfUfdLtDAutoEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfUfdNotificationGroup = hpicfUfdNotificationGroup.setStatus('current')
hpicfUfdConfigGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 3, 2, 4)).setObjects(("HP-ICF-UFD-MIB", "hpicfUfdLinkRole"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfUfdConfigGroup1 = hpicfUfdConfigGroup1.setStatus('current')
hpicfUfdConfigGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 3, 2, 5)).setObjects(("HP-ICF-UFD-MIB", "hpicfUfdTrackEntityType"), ("HP-ICF-UFD-MIB", "hpicfUfdLinksToMonitor"), ("HP-ICF-UFD-MIB", "hpicfUfdLinksToTransition"), ("HP-ICF-UFD-MIB", "hpicfUfdLinksToMonitorState"), ("HP-ICF-UFD-MIB", "hpicfUfdLinksToTransitionState"), ("HP-ICF-UFD-MIB", "hpicfUfdTrackEntityState"), ("HP-ICF-UFD-MIB", "hpicfUfdTrackEntityRowStatus"), ("HP-ICF-UFD-MIB", "hpicfUfdLinksToMonitorType"), ("HP-ICF-UFD-MIB", "hpicfUfdLinksToTransitionType"), ("HP-ICF-UFD-MIB", "hpicfUfdLinksTransitionDelay"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfUfdConfigGroup2 = hpicfUfdConfigGroup2.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-UFD-MIB", hpicfUfdCompliance=hpicfUfdCompliance, hpicfUfdLinksToMonitor=hpicfUfdLinksToMonitor, hpicfUfdTrackEntityType=hpicfUfdTrackEntityType, hpicfUfdScalars=hpicfUfdScalars, hpicfUfdCompliances=hpicfUfdCompliances, hpicfUfdNotificationGroup=hpicfUfdNotificationGroup, hpicfUfdTrackedLinkEntry=hpicfUfdTrackedLinkEntry, hpicfUfdLinksTransitionDelay=hpicfUfdLinksTransitionDelay, hpicfUfdConfigGroup=hpicfUfdConfigGroup, hpicfUfdLtDAutoDisabled=hpicfUfdLtDAutoDisabled, hpicfUfdGroups=hpicfUfdGroups, hpicfUfdNotifyTrackId=hpicfUfdNotifyTrackId, hpicfUfdTrackEntityRowStatus=hpicfUfdTrackEntityRowStatus, hpicfUfdLinksToMonitorType=hpicfUfdLinksToMonitorType, hpicfUfdAdminStatus=hpicfUfdAdminStatus, HpUfdTrackEntityType=HpUfdTrackEntityType, hpicfUfdConformance=hpicfUfdConformance, hpicfUfdLinksToTransitionType=hpicfUfdLinksToTransitionType, hpicfUfdCompliance2=hpicfUfdCompliance2, hpicfUfdLinksToMonitorState=hpicfUfdLinksToMonitorState, hpicfUfdConfigGroup1=hpicfUfdConfigGroup1, hpicfUfdConfigGroup2=hpicfUfdConfigGroup2, PYSNMP_MODULE_ID=hpicfUfdMIB, hpicfUfdLinksToTransition=hpicfUfdLinksToTransition, hpicfUfdIfIndex=hpicfUfdIfIndex, hpicfUfdTrackEntities=hpicfUfdTrackEntities, hpicfUfdTrackId=hpicfUfdTrackId, hpicfUfdTrackTable=hpicfUfdTrackTable, hpicfUfdNotificationPrefix=hpicfUfdNotificationPrefix, hpicfUfdMIB=hpicfUfdMIB, HpUfdTrackLinksSubtype=HpUfdTrackLinksSubtype, hpicfUfdTrackEntityState=hpicfUfdTrackEntityState, hpicfUfdTrackedLinkTable=hpicfUfdTrackedLinkTable, hpicfUfdLtDAutoEnabled=hpicfUfdLtDAutoEnabled, hpicfUfdCompliance1=hpicfUfdCompliance1, hpicfUfdLinksToTransitionState=hpicfUfdLinksToTransitionState, hpicfUfdNotifications=hpicfUfdNotifications, hpicfUfdBaseGroup=hpicfUfdBaseGroup, hpicfUfdLinkRole=hpicfUfdLinkRole, hpicfUfdTrackEntry=hpicfUfdTrackEntry, hpicfUfdConfigObjects=hpicfUfdConfigObjects)
