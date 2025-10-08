#
# PySNMP MIB module APPN-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/rfc/APPN-TRAP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:48:29 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
dlurDlusSessnStatus, = mibBuilder.importSymbols("APPN-DLUR-MIB", "dlurDlusSessnStatus")
appnIsInS2PNonFmdPius, appnLocalTgCpCpSession, appnLocalTgOperational, appnIsInS2PFmdBytes, appnPortOperState, appnGroups, appnObjects, appnIsInSessUpTime, appnCompliances, appnIsInS2PNonFmdBytes, appnMIB, appnIsInS2PFmdPius, appnIsInP2SNonFmdBytes, appnLsOperState, appnIsInP2SNonFmdPius, appnIsInP2SFmdPius, appnIsInP2SFmdBytes = mibBuilder.importSymbols("APPN-MIB", "appnIsInS2PNonFmdPius", "appnLocalTgCpCpSession", "appnLocalTgOperational", "appnIsInS2PFmdBytes", "appnPortOperState", "appnGroups", "appnObjects", "appnIsInSessUpTime", "appnCompliances", "appnIsInS2PNonFmdBytes", "appnMIB", "appnIsInS2PFmdPius", "appnIsInP2SNonFmdBytes", "appnLsOperState", "appnIsInP2SNonFmdPius", "appnIsInP2SFmdPius", "appnIsInP2SFmdBytes")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("APPN-TRAP-MIB", appnTrapControl=appnTrapControl, appnTrapMibDlurConfGroup=appnTrapMibDlurConfGroup, PYSNMP_MODULE_ID=appnTrapMIB, appnTrapMibCompliance=appnTrapMibCompliance, appnLsOperStateChangeTrap=appnLsOperStateChangeTrap, appnTrapMIB=appnTrapMIB, appnLocalTgCpCpChangeTrap=appnLocalTgCpCpChangeTrap, appnLocalTgOperStateChangeTrap=appnLocalTgOperStateChangeTrap, appnPortOperStateChangeTrap=appnPortOperStateChangeTrap, dlurDlusStateChangeTrap=dlurDlusStateChangeTrap, appnTrapMibIsrNotifGroup=appnTrapMibIsrNotifGroup, appnIsrAccountingDataTrap=appnIsrAccountingDataTrap, appnTrapObjects=appnTrapObjects, appnTrapMibTopoConfGroup=appnTrapMibTopoConfGroup, appnLocalTgTableChanges=appnLocalTgTableChanges, appnTrapMibTopoNotifGroup=appnTrapMibTopoNotifGroup, appnTrapMibDlurNotifGroup=appnTrapMibDlurNotifGroup, appnPortTableChanges=appnPortTableChanges, appnLsTableChanges=appnLsTableChanges, dlurDlusTableChanges=dlurDlusTableChanges)
