#
# PySNMP MIB module APPN-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rfc/APPN-TRAP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:26:38 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
dlurDlusSessnStatus, = mibBuilder.importSymbols("APPN-DLUR-MIB", "dlurDlusSessnStatus")
appnCompliances, appnIsInP2SFmdBytes, appnObjects, appnLocalTgOperational, appnPortOperState, appnIsInS2PFmdPius, appnIsInSessUpTime, appnGroups, appnIsInP2SNonFmdPius, appnIsInS2PFmdBytes, appnLsOperState, appnMIB, appnLocalTgCpCpSession, appnIsInP2SFmdPius, appnIsInS2PNonFmdPius, appnIsInS2PNonFmdBytes, appnIsInP2SNonFmdBytes = mibBuilder.importSymbols("APPN-MIB", "appnCompliances", "appnIsInP2SFmdBytes", "appnObjects", "appnLocalTgOperational", "appnPortOperState", "appnIsInS2PFmdPius", "appnIsInSessUpTime", "appnGroups", "appnIsInP2SNonFmdPius", "appnIsInS2PFmdBytes", "appnLsOperState", "appnMIB", "appnLocalTgCpCpSession", "appnIsInP2SFmdPius", "appnIsInS2PNonFmdPius", "appnIsInS2PNonFmdBytes", "appnIsInP2SNonFmdBytes")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, iso, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "iso", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
appnTrapMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 34, 4, 0))
if mibBuilder.loadTexts: appnTrapMIB.setLastUpdated('9808310000Z')
if mibBuilder.loadTexts: appnTrapMIB.setOrganization('IETF SNA NAU MIB WG / AIW APPN MIBs SIG')
appnIsrAccountingDataTrap = NotificationType((1, 3, 6, 1, 2, 1, 34, 4, 0, 1)).setObjects(("APPN-MIB", "appnIsInP2SFmdPius"), ("APPN-MIB", "appnIsInS2PFmdPius"), ("APPN-MIB", "appnIsInP2SNonFmdPius"), ("APPN-MIB", "appnIsInS2PNonFmdPius"), ("APPN-MIB", "appnIsInP2SFmdBytes"), ("APPN-MIB", "appnIsInS2PFmdBytes"), ("APPN-MIB", "appnIsInP2SNonFmdBytes"), ("APPN-MIB", "appnIsInS2PNonFmdBytes"), ("APPN-MIB", "appnIsInSessUpTime"))
if mibBuilder.loadTexts: appnIsrAccountingDataTrap.setStatus('current')
appnLocalTgOperStateChangeTrap = NotificationType((1, 3, 6, 1, 2, 1, 34, 4, 0, 2)).setObjects(("APPN-TRAP-MIB", "appnLocalTgTableChanges"), ("APPN-MIB", "appnLocalTgOperational"))
if mibBuilder.loadTexts: appnLocalTgOperStateChangeTrap.setStatus('current')
appnLocalTgCpCpChangeTrap = NotificationType((1, 3, 6, 1, 2, 1, 34, 4, 0, 3)).setObjects(("APPN-TRAP-MIB", "appnLocalTgTableChanges"), ("APPN-MIB", "appnLocalTgCpCpSession"))
if mibBuilder.loadTexts: appnLocalTgCpCpChangeTrap.setStatus('current')
appnPortOperStateChangeTrap = NotificationType((1, 3, 6, 1, 2, 1, 34, 4, 0, 4)).setObjects(("APPN-TRAP-MIB", "appnPortTableChanges"), ("APPN-MIB", "appnPortOperState"))
if mibBuilder.loadTexts: appnPortOperStateChangeTrap.setStatus('current')
appnLsOperStateChangeTrap = NotificationType((1, 3, 6, 1, 2, 1, 34, 4, 0, 5)).setObjects(("APPN-TRAP-MIB", "appnLsTableChanges"), ("APPN-MIB", "appnLsOperState"))
if mibBuilder.loadTexts: appnLsOperStateChangeTrap.setStatus('current')
dlurDlusStateChangeTrap = NotificationType((1, 3, 6, 1, 2, 1, 34, 4, 0, 6)).setObjects(("APPN-TRAP-MIB", "dlurDlusTableChanges"), ("APPN-DLUR-MIB", "dlurDlusSessnStatus"))
if mibBuilder.loadTexts: dlurDlusStateChangeTrap.setStatus('current')
appnTrapObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 4, 1, 7))
appnTrapControl = MibScalar((1, 3, 6, 1, 2, 1, 34, 4, 1, 7, 1), Bits().clone(namedValues=NamedValues(("appnLocalTgOperStateChangeTrap", 0), ("appnLocalTgCpCpChangeTrap", 1), ("appnPortOperStateChangeTrap", 2), ("appnLsOperStateChangeTrap", 3), ("dlurDlusStateChangeTrap", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: appnTrapControl.setStatus('current')
appnLocalTgTableChanges = MibScalar((1, 3, 6, 1, 2, 1, 34, 4, 1, 7, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appnLocalTgTableChanges.setStatus('current')
appnPortTableChanges = MibScalar((1, 3, 6, 1, 2, 1, 34, 4, 1, 7, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appnPortTableChanges.setStatus('current')
appnLsTableChanges = MibScalar((1, 3, 6, 1, 2, 1, 34, 4, 1, 7, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appnLsTableChanges.setStatus('current')
dlurDlusTableChanges = MibScalar((1, 3, 6, 1, 2, 1, 34, 4, 1, 7, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlurDlusTableChanges.setStatus('current')
appnTrapMibCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 34, 4, 3, 1, 2)).setObjects(("APPN-TRAP-MIB", "appnTrapMibIsrNotifGroup"), ("APPN-TRAP-MIB", "appnTrapMibTopoConfGroup"), ("APPN-TRAP-MIB", "appnTrapMibTopoNotifGroup"), ("APPN-TRAP-MIB", "appnTrapMibDlurConfGroup"), ("APPN-TRAP-MIB", "appnTrapMibDlurNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    appnTrapMibCompliance = appnTrapMibCompliance.setStatus('current')
appnTrapMibIsrNotifGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 21)).setObjects(("APPN-TRAP-MIB", "appnIsrAccountingDataTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    appnTrapMibIsrNotifGroup = appnTrapMibIsrNotifGroup.setStatus('current')
appnTrapMibTopoConfGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 22)).setObjects(("APPN-TRAP-MIB", "appnTrapControl"), ("APPN-TRAP-MIB", "appnLocalTgTableChanges"), ("APPN-TRAP-MIB", "appnPortTableChanges"), ("APPN-TRAP-MIB", "appnLsTableChanges"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    appnTrapMibTopoConfGroup = appnTrapMibTopoConfGroup.setStatus('current')
appnTrapMibTopoNotifGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 23)).setObjects(("APPN-TRAP-MIB", "appnLocalTgOperStateChangeTrap"), ("APPN-TRAP-MIB", "appnLocalTgCpCpChangeTrap"), ("APPN-TRAP-MIB", "appnPortOperStateChangeTrap"), ("APPN-TRAP-MIB", "appnLsOperStateChangeTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    appnTrapMibTopoNotifGroup = appnTrapMibTopoNotifGroup.setStatus('current')
appnTrapMibDlurConfGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 24)).setObjects(("APPN-TRAP-MIB", "appnTrapControl"), ("APPN-TRAP-MIB", "dlurDlusTableChanges"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    appnTrapMibDlurConfGroup = appnTrapMibDlurConfGroup.setStatus('current')
appnTrapMibDlurNotifGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 25)).setObjects(("APPN-TRAP-MIB", "dlurDlusStateChangeTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    appnTrapMibDlurNotifGroup = appnTrapMibDlurNotifGroup.setStatus('current')
mibBuilder.exportSymbols("APPN-TRAP-MIB", appnTrapMibDlurNotifGroup=appnTrapMibDlurNotifGroup, appnLsOperStateChangeTrap=appnLsOperStateChangeTrap, appnTrapMibTopoConfGroup=appnTrapMibTopoConfGroup, appnPortOperStateChangeTrap=appnPortOperStateChangeTrap, appnTrapMibCompliance=appnTrapMibCompliance, dlurDlusStateChangeTrap=dlurDlusStateChangeTrap, appnLsTableChanges=appnLsTableChanges, appnTrapMIB=appnTrapMIB, appnTrapMibIsrNotifGroup=appnTrapMibIsrNotifGroup, appnTrapMibTopoNotifGroup=appnTrapMibTopoNotifGroup, appnTrapObjects=appnTrapObjects, appnTrapMibDlurConfGroup=appnTrapMibDlurConfGroup, appnLocalTgOperStateChangeTrap=appnLocalTgOperStateChangeTrap, dlurDlusTableChanges=dlurDlusTableChanges, appnLocalTgCpCpChangeTrap=appnLocalTgCpCpChangeTrap, PYSNMP_MODULE_ID=appnTrapMIB, appnTrapControl=appnTrapControl, appnPortTableChanges=appnPortTableChanges, appnIsrAccountingDataTrap=appnIsrAccountingDataTrap, appnLocalTgTableChanges=appnLocalTgTableChanges)
