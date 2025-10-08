#
# PySNMP MIB module RBN-ATM-PVC-OAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/ericsson/RBN-ATM-PVC-OAM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:25:47 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
RbnPort, RbnSlot = mibBuilder.importSymbols("RBN-TC", "RbnPort", "RbnSlot")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rbnAtmPvcOamMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 2, 19))
rbnAtmPvcOamMib.setRevisions(('2002-11-13 00:00', '2002-02-05 00:00',))
if mibBuilder.loadTexts: rbnAtmPvcOamMib.setLastUpdated('200211130000Z')
if mibBuilder.loadTexts: rbnAtmPvcOamMib.setOrganization('Redback Networks, Inc.')
rbnAtmPvcOamMibNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 19, 0))
rbnAtmPvcOamMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 19, 1))
rbnAtmPvcOamMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 19, 2))
rbnAtmPvcOamStatusTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 19, 1, 1), )
if mibBuilder.loadTexts: rbnAtmPvcOamStatusTable.setStatus('current')
rbnAtmPvcOamStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 19, 1, 1, 1), ).setIndexNames((0, "RBN-ATM-PVC-OAM-MIB", "rbnAtmPvcOamStatusSlot"), (0, "RBN-ATM-PVC-OAM-MIB", "rbnAtmPvcOamStatusPort"), (0, "RBN-ATM-PVC-OAM-MIB", "rbnAtmPvcOamStatusVpi"), (0, "RBN-ATM-PVC-OAM-MIB", "rbnAtmPvcOamStatusVci"))
if mibBuilder.loadTexts: rbnAtmPvcOamStatusEntry.setStatus('current')
rbnAtmPvcOamStatusSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 19, 1, 1, 1, 1), RbnSlot())
if mibBuilder.loadTexts: rbnAtmPvcOamStatusSlot.setStatus('current')
rbnAtmPvcOamStatusPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 19, 1, 1, 1, 2), RbnPort())
if mibBuilder.loadTexts: rbnAtmPvcOamStatusPort.setStatus('current')
rbnAtmPvcOamStatusVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 19, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095)))
if mibBuilder.loadTexts: rbnAtmPvcOamStatusVpi.setStatus('current')
rbnAtmPvcOamStatusVci = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 19, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: rbnAtmPvcOamStatusVci.setStatus('current')
rbnAtmPvcOamStatusState = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 19, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("noOam", 1), ("oamUp", 2), ("oamDownLoopback", 3), ("oamDownAis", 4), ("oamDownRdi", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnAtmPvcOamStatusState.setStatus('current')
rbnAtmPvcOamStatusStateChange = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 19, 0, 1)).setObjects(("RBN-ATM-PVC-OAM-MIB", "rbnAtmPvcOamStatusState"))
if mibBuilder.loadTexts: rbnAtmPvcOamStatusStateChange.setStatus('current')
rbnAtmPvcOamCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 19, 2, 1))
rbnAtmPvcOamGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 19, 2, 2))
rbnAtmPvcOamCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 19, 2, 1, 1)).setObjects(("RBN-ATM-PVC-OAM-MIB", "rbnAtmPvcOamGroup"), ("RBN-ATM-PVC-OAM-MIB", "rbnAtmPvcOamNotifyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnAtmPvcOamCompliance = rbnAtmPvcOamCompliance.setStatus('current')
rbnAtmPvcOamGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 19, 2, 2, 1)).setObjects(("RBN-ATM-PVC-OAM-MIB", "rbnAtmPvcOamStatusState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnAtmPvcOamGroup = rbnAtmPvcOamGroup.setStatus('current')
rbnAtmPvcOamNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2352, 2, 19, 2, 2, 2)).setObjects(("RBN-ATM-PVC-OAM-MIB", "rbnAtmPvcOamStatusStateChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnAtmPvcOamNotifyGroup = rbnAtmPvcOamNotifyGroup.setStatus('current')
mibBuilder.exportSymbols("RBN-ATM-PVC-OAM-MIB", PYSNMP_MODULE_ID=rbnAtmPvcOamMib, rbnAtmPvcOamMibNotifications=rbnAtmPvcOamMibNotifications, rbnAtmPvcOamMib=rbnAtmPvcOamMib, rbnAtmPvcOamStatusSlot=rbnAtmPvcOamStatusSlot, rbnAtmPvcOamCompliances=rbnAtmPvcOamCompliances, rbnAtmPvcOamMibConformance=rbnAtmPvcOamMibConformance, rbnAtmPvcOamStatusPort=rbnAtmPvcOamStatusPort, rbnAtmPvcOamStatusVpi=rbnAtmPvcOamStatusVpi, rbnAtmPvcOamStatusTable=rbnAtmPvcOamStatusTable, rbnAtmPvcOamStatusState=rbnAtmPvcOamStatusState, rbnAtmPvcOamNotifyGroup=rbnAtmPvcOamNotifyGroup, rbnAtmPvcOamStatusEntry=rbnAtmPvcOamStatusEntry, rbnAtmPvcOamStatusStateChange=rbnAtmPvcOamStatusStateChange, rbnAtmPvcOamMibObjects=rbnAtmPvcOamMibObjects, rbnAtmPvcOamGroups=rbnAtmPvcOamGroups, rbnAtmPvcOamStatusVci=rbnAtmPvcOamStatusVci, rbnAtmPvcOamCompliance=rbnAtmPvcOamCompliance, rbnAtmPvcOamGroup=rbnAtmPvcOamGroup)
