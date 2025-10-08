#
# PySNMP MIB module QTECH-VPLS-LDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/qtech/QTECH-VPLS-LDP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:06:08 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
IANAPwTypeTC, IANAPwPsnTypeTC, IANAPwCapabilities = mibBuilder.importSymbols("IANA-PWE3-MIB", "IANAPwTypeTC", "IANAPwPsnTypeTC", "IANAPwCapabilities")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
qtechMgmt, = mibBuilder.importSymbols("QTECH-SMI", "qtechMgmt")
qtechvplsConfigIndex, qtechvplsPwBindIndex = mibBuilder.importSymbols("QTECH-VPLS-GENERIC-MIB", "qtechvplsConfigIndex", "qtechvplsPwBindIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, transmission, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "transmission", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
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
mibBuilder.exportSymbols("QTECH-VPLS-LDP-MIB", qtechvplsLdpModuleFullCompliance=qtechvplsLdpModuleFullCompliance, qtechvplsLdpNotifications=qtechvplsLdpNotifications, qtechvplsLdpConfigEntry=qtechvplsLdpConfigEntry, qtechvplsLdpPeerAddr=qtechvplsLdpPeerAddr, qtechvplsPwEncapType=qtechvplsPwEncapType, qtechvplsLdpGroups=qtechvplsLdpGroups, qtechvplsLdpObjects=qtechvplsLdpObjects, qtechvplsLdpCompliances=qtechvplsLdpCompliances, qtechvplsLdpModuleReadOnlyCompliance=qtechvplsLdpModuleReadOnlyCompliance, qtechvplsLdpNeighborRowStatus=qtechvplsLdpNeighborRowStatus, qtechvplsLdpPwId=qtechvplsLdpPwId, qtechvplsLdpConformance=qtechvplsLdpConformance, qtechvplsLdpConfigTable=qtechvplsLdpConfigTable, qtechvplsLdpPwIndex=qtechvplsLdpPwIndex, qtechvplsLdpDraft01MIB=qtechvplsLdpDraft01MIB, qtechvplsPwType=qtechvplsPwType, PYSNMP_MODULE_ID=qtechvplsLdpDraft01MIB)
