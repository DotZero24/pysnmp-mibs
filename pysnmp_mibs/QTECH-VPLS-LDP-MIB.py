#
# PySNMP MIB module QTECH-VPLS-LDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/qtech/QTECH-VPLS-LDP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:14:02 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
IANAPwCapabilities, IANAPwPsnTypeTC, IANAPwTypeTC = mibBuilder.importSymbols("IANA-PWE3-MIB", "IANAPwCapabilities", "IANAPwPsnTypeTC", "IANAPwTypeTC")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
qtechMgmt, = mibBuilder.importSymbols("QTECH-SMI", "qtechMgmt")
qtechvplsConfigIndex, qtechvplsPwBindIndex = mibBuilder.importSymbols("QTECH-VPLS-GENERIC-MIB", "qtechvplsConfigIndex", "qtechvplsPwBindIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
transmission, MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "transmission", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "TextualConvention", "DisplayString")
qtechvplsLdpDraft01MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 78))
qtechvplsLdpDraft01MIB.setRevisions(('2010-04-28 12:00',))
if mibBuilder.loadTexts: qtechvplsLdpDraft01MIB.setLastUpdated('201004281200Z')
if mibBuilder.loadTexts: qtechvplsLdpDraft01MIB.setOrganization('Qtech Networks Co.,Ltd.')
qtechvplsLdpNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 78, 0))
qtechvplsLdpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 78, 1))
qtechvplsLdpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 78, 2))
qtechvplsLdpConfigTable = MibTable((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 78, 1, 1), )
if mibBuilder.loadTexts: qtechvplsLdpConfigTable.setStatus('current')
qtechvplsLdpConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 78, 1, 1, 1), ).setIndexNames((0, "QTECH-VPLS-GENERIC-MIB", "qtechvplsConfigIndex"), (0, "QTECH-VPLS-LDP-MIB", "qtechvplsLdpPwIndex"))
if mibBuilder.loadTexts: qtechvplsLdpConfigEntry.setStatus('current')
qtechvplsLdpPwIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 78, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: qtechvplsLdpPwIndex.setStatus('current')
qtechvplsLdpPeerAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 78, 1, 1, 1, 2), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qtechvplsLdpPeerAddr.setStatus('current')
qtechvplsLdpPwId = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 78, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qtechvplsLdpPwId.setStatus('current')
qtechvplsPwType = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 78, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mesh", 1), ("spoke", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qtechvplsPwType.setStatus('current')
qtechvplsPwEncapType = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 78, 1, 1, 1, 5), IANAPwTypeTC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qtechvplsPwEncapType.setStatus('current')
qtechvplsLdpNeighborRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 78, 1, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qtechvplsLdpNeighborRowStatus.setStatus('current')
qtechvplsLdpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 78, 2, 1))
qtechvplsLdpModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 78, 2, 1, 1)).setObjects(("QTECH-VPLS-LDP-MIB", "qtechvplsLdpGroup"), ("QTECH-VPLS-LDP-MIB", "qtechvplsLdpNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qtechvplsLdpModuleFullCompliance = qtechvplsLdpModuleFullCompliance.setStatus('current')
qtechvplsLdpModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 78, 2, 1, 2)).setObjects(("QTECH-VPLS-LDP-MIB", "qtechvplsLdpGroup"), ("QTECH-VPLS-LDP-MIB", "qtechvplsLdpNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qtechvplsLdpModuleReadOnlyCompliance = qtechvplsLdpModuleReadOnlyCompliance.setStatus('current')
qtechvplsLdpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 78, 2, 2))
mibBuilder.exportSymbols("QTECH-VPLS-LDP-MIB", qtechvplsLdpObjects=qtechvplsLdpObjects, qtechvplsLdpNeighborRowStatus=qtechvplsLdpNeighborRowStatus, qtechvplsPwEncapType=qtechvplsPwEncapType, qtechvplsLdpConformance=qtechvplsLdpConformance, qtechvplsLdpNotifications=qtechvplsLdpNotifications, qtechvplsLdpPwId=qtechvplsLdpPwId, qtechvplsLdpConfigEntry=qtechvplsLdpConfigEntry, qtechvplsLdpDraft01MIB=qtechvplsLdpDraft01MIB, qtechvplsLdpModuleReadOnlyCompliance=qtechvplsLdpModuleReadOnlyCompliance, qtechvplsPwType=qtechvplsPwType, qtechvplsLdpPwIndex=qtechvplsLdpPwIndex, qtechvplsLdpCompliances=qtechvplsLdpCompliances, qtechvplsLdpGroups=qtechvplsLdpGroups, qtechvplsLdpConfigTable=qtechvplsLdpConfigTable, qtechvplsLdpPeerAddr=qtechvplsLdpPeerAddr, qtechvplsLdpModuleFullCompliance=qtechvplsLdpModuleFullCompliance, PYSNMP_MODULE_ID=qtechvplsLdpDraft01MIB)
