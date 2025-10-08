#
# PySNMP MIB module ACD-TID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/accedian/ACD-TID-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:11:43 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
acdMibs, = mibBuilder.importSymbols("ACCEDIAN-SMI", "acdMibs")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
acdTid = ModuleIdentity((1, 3, 6, 1, 4, 1, 22420, 2, 14))
acdTid.setRevisions(('2012-11-05 22:00', '2011-11-11 01:00',))
if mibBuilder.loadTexts: acdTid.setLastUpdated('201211052200Z')
if mibBuilder.loadTexts: acdTid.setOrganization('Accedian Networks, Inc.')
acdTidNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 14, 0))
acdTidMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1))
acdTidConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 14, 2))
acdTidGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 1))
acdTidInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 2))
acdTidGlobalCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 3))
class AcdTidType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("configuration", 1), ("status", 2))

acdTidCfgLastChangeTid = MibScalar((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdTidCfgLastChangeTid.setStatus('current')
acdTidStatusLastChangeTid = MibScalar((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdTidStatusLastChangeTid.setStatus('current')
acdTidInfoTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 2, 1), )
if mibBuilder.loadTexts: acdTidInfoTable.setStatus('current')
acdTidInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 2, 1, 1), ).setIndexNames((0, "ACD-TID-MIB", "acdTidInfoIndex"))
if mibBuilder.loadTexts: acdTidInfoEntry.setStatus('current')
acdTidInfoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 2, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: acdTidInfoIndex.setStatus('current')
acdTidInfoOID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 2, 1, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdTidInfoOID.setStatus('current')
acdTidInfoType = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 2, 1, 1, 3), AcdTidType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdTidInfoType.setStatus('current')
acdTidInfoDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 2, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdTidInfoDescr.setStatus('current')
acdTidInfoLastChangeTid = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 2, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdTidInfoLastChangeTid.setStatus('current')
acdTidglobalCfgChangeCount = MibScalar((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 3, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdTidglobalCfgChangeCount.setStatus('current')
acdTidNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 14, 0, 0))
acdTidGlobalCfgChange = NotificationType((1, 3, 6, 1, 4, 1, 22420, 2, 14, 0, 0, 1)).setObjects(("ACD-TID-MIB", "acdTidglobalCfgChangeCount"))
if mibBuilder.loadTexts: acdTidGlobalCfgChange.setStatus('current')
acdTidCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 14, 2, 1))
acdTidGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 14, 2, 2))
acdTidGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 14, 2, 2, 1)).setObjects(("ACD-TID-MIB", "acdTidCfgLastChangeTid"), ("ACD-TID-MIB", "acdTidStatusLastChangeTid"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdTidGeneralGroup = acdTidGeneralGroup.setStatus('current')
acdTidTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 14, 2, 2, 2)).setObjects(("ACD-TID-MIB", "acdTidInfoOID"), ("ACD-TID-MIB", "acdTidInfoType"), ("ACD-TID-MIB", "acdTidInfoDescr"), ("ACD-TID-MIB", "acdTidInfoLastChangeTid"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdTidTableGroup = acdTidTableGroup.setStatus('current')
acdTidGlobalCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 14, 2, 2, 3)).setObjects(("ACD-TID-MIB", "acdTidglobalCfgChangeCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdTidGlobalCfgGroup = acdTidGlobalCfgGroup.setStatus('current')
acdTidNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 22420, 2, 14, 2, 2, 4)).setObjects(("ACD-TID-MIB", "acdTidGlobalCfgChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdTidNotificationsGroup = acdTidNotificationsGroup.setStatus('current')
acdTidCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 22420, 2, 14, 2, 1, 1)).setObjects(("ACD-TID-MIB", "acdTidGeneralGroup"), ("ACD-TID-MIB", "acdTidTableGroup"), ("ACD-TID-MIB", "acdTidGlobalCfgGroup"), ("ACD-TID-MIB", "acdTidNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdTidCompliance = acdTidCompliance.setStatus('current')
mibBuilder.exportSymbols("ACD-TID-MIB", acdTidConformance=acdTidConformance, AcdTidType=AcdTidType, acdTidGlobalCfg=acdTidGlobalCfg, acdTidCompliance=acdTidCompliance, acdTidGlobalCfgGroup=acdTidGlobalCfgGroup, acdTidInfoEntry=acdTidInfoEntry, acdTidGroups=acdTidGroups, acdTidInfoLastChangeTid=acdTidInfoLastChangeTid, acdTidInfoDescr=acdTidInfoDescr, acdTidNotificationPrefix=acdTidNotificationPrefix, acdTidMIBObjects=acdTidMIBObjects, acdTidGeneral=acdTidGeneral, acdTidGlobalCfgChange=acdTidGlobalCfgChange, acdTidInfoType=acdTidInfoType, acdTidglobalCfgChangeCount=acdTidglobalCfgChangeCount, acdTidInfo=acdTidInfo, acdTidInfoIndex=acdTidInfoIndex, acdTid=acdTid, acdTidCfgLastChangeTid=acdTidCfgLastChangeTid, PYSNMP_MODULE_ID=acdTid, acdTidNotificationsGroup=acdTidNotificationsGroup, acdTidCompliances=acdTidCompliances, acdTidNotifications=acdTidNotifications, acdTidStatusLastChangeTid=acdTidStatusLastChangeTid, acdTidTableGroup=acdTidTableGroup, acdTidInfoTable=acdTidInfoTable, acdTidGeneralGroup=acdTidGeneralGroup, acdTidInfoOID=acdTidInfoOID)
