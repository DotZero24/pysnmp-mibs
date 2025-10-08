#
# PySNMP MIB module QLOGIC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/marvell/QLOGIC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:16 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
connUnitId, = mibBuilder.importSymbols("FCMGMT-MIB", "connUnitId")
ancorOidTree, = mibBuilder.importSymbols("QLOGIC-SMI", "ancorOidTree")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, iso, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "iso", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ancorPortModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 1663, 1, 3))
ancorPortModule.setRevisions(('2009-09-29 00:00', '2006-10-11 00:00',))
if mibBuilder.loadTexts: ancorPortModule.setLastUpdated('200909290000Z')
if mibBuilder.loadTexts: ancorPortModule.setOrganization('QLOGIC Corporation')
qlSB2PortControl = MibIdentifier((1, 3, 6, 1, 4, 1, 1663, 1, 3, 10))
qlSB2PortStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 1663, 1, 3, 11))
class FcQlModuleIndex(TextualConvention, Unsigned32):
    status = 'current'

class FcQxPortIndex(TextualConvention, Unsigned32):
    status = 'current'

fcQxPortPhysTable = MibTable((1, 3, 6, 1, 4, 1, 1663, 1, 3, 10, 1), )
if mibBuilder.loadTexts: fcQxPortPhysTable.setStatus('current')
fcQxPortPhysEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1663, 1, 3, 10, 1, 1), ).setIndexNames((0, "QLOGIC-MIB", "fcQxPortPhysModule"), (0, "QLOGIC-MIB", "fcQxPortPhysIndex"))
if mibBuilder.loadTexts: fcQxPortPhysEntry.setStatus('current')
fcQxPortPhysModule = MibTableColumn((1, 3, 6, 1, 4, 1, 1663, 1, 3, 10, 1, 1, 1), FcQlModuleIndex())
if mibBuilder.loadTexts: fcQxPortPhysModule.setStatus('current')
fcQxPortPhysIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1663, 1, 3, 10, 1, 1, 2), FcQxPortIndex())
if mibBuilder.loadTexts: fcQxPortPhysIndex.setStatus('current')
fcQxPortPhysAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1663, 1, 3, 10, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("online", 1), ("offline", 2), ("testing", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fcQxPortPhysAdminStatus.setStatus('current')
fcQxPortPhysOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1663, 1, 3, 10, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("online", 1), ("offline", 2), ("testing", 3), ("linkFailure", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcQxPortPhysOperStatus.setStatus('current')
fcQxQuailPortPhysAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1663, 1, 3, 10, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fcQxQuailPortPhysAdminStatus.setStatus('current')
fcQxQuailPortPhysOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1663, 1, 3, 10, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcQxQuailPortPhysOperStatus.setStatus('current')
fcQxQuailPortPhysReasonCode = MibTableColumn((1, 3, 6, 1, 4, 1, 1663, 1, 3, 10, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("unknown", 1), ("up", 2), ("down", 3), ("notConnected", 4), ("sfpAbsent", 5), ("sfpUnsupported", 6), ("hardwareFailure", 7), ("isolated", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcQxQuailPortPhysReasonCode.setStatus('current')
fcQxPortStatusTable = MibTable((1, 3, 6, 1, 4, 1, 1663, 1, 3, 11, 1), )
if mibBuilder.loadTexts: fcQxPortStatusTable.setStatus('current')
fcQxPortStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1663, 1, 3, 11, 1, 1), ).setIndexNames((0, "QLOGIC-MIB", "fcQxPortStatusModule"), (0, "QLOGIC-MIB", "fcQxPortStatusIndex"))
if mibBuilder.loadTexts: fcQxPortStatusEntry.setStatus('current')
fcQxPortStatusModule = MibTableColumn((1, 3, 6, 1, 4, 1, 1663, 1, 3, 11, 1, 1, 1), FcQlModuleIndex())
if mibBuilder.loadTexts: fcQxPortStatusModule.setStatus('current')
fcQxPortStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1663, 1, 3, 11, 1, 1, 2), FcQxPortIndex())
if mibBuilder.loadTexts: fcQxPortStatusIndex.setStatus('current')
fcQxQuailPortOperMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1663, 1, 3, 11, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 6))).clone(namedValues=NamedValues(("auto", 1), ("fPort", 2), ("flPort", 3), ("ePort", 4), ("fxPort", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcQxQuailPortOperMode.setStatus('current')
fcQxQuailPortAdminMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1663, 1, 3, 11, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 6))).clone(namedValues=NamedValues(("auto", 1), ("fPort", 2), ("flPort", 3), ("ePort", 4), ("fxPort", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fcQxQuailPortAdminMode.setStatus('current')
qlSB2PortLinkDown = NotificationType((1, 3, 6, 1, 4, 1, 1663, 1, 3, 0, 10)).setObjects(("QLOGIC-MIB", "fcQxPortPhysAdminStatus"), ("QLOGIC-MIB", "fcQxPortPhysOperStatus"))
if mibBuilder.loadTexts: qlSB2PortLinkDown.setStatus('current')
qlSB2PortLinkUp = NotificationType((1, 3, 6, 1, 4, 1, 1663, 1, 3, 0, 11)).setObjects(("QLOGIC-MIB", "fcQxPortPhysAdminStatus"), ("QLOGIC-MIB", "fcQxPortPhysOperStatus"))
if mibBuilder.loadTexts: qlSB2PortLinkUp.setStatus('current')
qlconnUnitAddedTrap = NotificationType((1, 3, 6, 1, 4, 1, 1663, 1, 3, 0, 12)).setObjects(("FCMGMT-MIB", "connUnitId"))
if mibBuilder.loadTexts: qlconnUnitAddedTrap.setStatus('current')
mibBuilder.exportSymbols("QLOGIC-MIB", fcQxQuailPortPhysReasonCode=fcQxQuailPortPhysReasonCode, fcQxPortPhysOperStatus=fcQxPortPhysOperStatus, fcQxQuailPortPhysAdminStatus=fcQxQuailPortPhysAdminStatus, ancorPortModule=ancorPortModule, fcQxPortPhysModule=fcQxPortPhysModule, fcQxPortPhysTable=fcQxPortPhysTable, FcQlModuleIndex=FcQlModuleIndex, qlSB2PortStatus=qlSB2PortStatus, fcQxPortStatusIndex=fcQxPortStatusIndex, PYSNMP_MODULE_ID=ancorPortModule, qlSB2PortLinkDown=qlSB2PortLinkDown, qlSB2PortControl=qlSB2PortControl, fcQxQuailPortAdminMode=fcQxQuailPortAdminMode, fcQxQuailPortOperMode=fcQxQuailPortOperMode, FcQxPortIndex=FcQxPortIndex, fcQxQuailPortPhysOperStatus=fcQxQuailPortPhysOperStatus, fcQxPortStatusModule=fcQxPortStatusModule, qlconnUnitAddedTrap=qlconnUnitAddedTrap, fcQxPortPhysEntry=fcQxPortPhysEntry, fcQxPortPhysIndex=fcQxPortPhysIndex, fcQxPortPhysAdminStatus=fcQxPortPhysAdminStatus, fcQxPortStatusEntry=fcQxPortStatusEntry, qlSB2PortLinkUp=qlSB2PortLinkUp, fcQxPortStatusTable=fcQxPortStatusTable)
