#
# PySNMP MIB module MARVELL-SpecialBpdu-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/radlan/MARVELL-SpecialBpdu-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:40:30 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, RowStatus, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "RowStatus", "TruthValue", "TextualConvention")
rlSpecialBpdu = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 144))
rlSpecialBpdu.setRevisions(('2008-05-03 12:34',))
if mibBuilder.loadTexts: rlSpecialBpdu.setLastUpdated('200805031234Z')
if mibBuilder.loadTexts: rlSpecialBpdu.setOrganization('MARVELL Semiconductor, Inc.')
class EncapType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("ethernet-v2", 2), ("llc", 3), ("llc-snap", 4))

class Action(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("bridge", 1), ("discard", 2))

class HwAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("forward", 1), ("drop", 2), ("trap", 3))

rlSpecialBpduTable = MibTable((1, 3, 6, 1, 4, 1, 89, 144, 1), )
if mibBuilder.loadTexts: rlSpecialBpduTable.setStatus('current')
rlSpecialBpduEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 144, 1, 1), ).setIndexNames((0, "MARVELL-SpecialBpdu-MIB", "rlSpecialBpduMacAddr"), (0, "MARVELL-SpecialBpdu-MIB", "rlSpecialBpduEncap"), (0, "MARVELL-SpecialBpdu-MIB", "rlSpecialBpduProtId"))
if mibBuilder.loadTexts: rlSpecialBpduEntry.setStatus('current')
rlSpecialBpduMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 144, 1, 1, 1), MacAddress())
if mibBuilder.loadTexts: rlSpecialBpduMacAddr.setStatus('current')
rlSpecialBpduEncap = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 144, 1, 1, 2), EncapType())
if mibBuilder.loadTexts: rlSpecialBpduEncap.setStatus('current')
rlSpecialBpduProtId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 144, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5))
if mibBuilder.loadTexts: rlSpecialBpduProtId.setStatus('current')
rlSpecialBpduAction = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 144, 1, 1, 4), Action()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpecialBpduAction.setStatus('current')
rlSpecialBpduRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 144, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlSpecialBpduRowStatus.setStatus('current')
rlSpecialBpduHwTable = MibTable((1, 3, 6, 1, 4, 1, 89, 144, 2), )
if mibBuilder.loadTexts: rlSpecialBpduHwTable.setStatus('current')
rlSpecialBpduHwEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 144, 2, 1), ).setIndexNames((0, "MARVELL-SpecialBpdu-MIB", "rlSpecialBpduMacAddr"))
if mibBuilder.loadTexts: rlSpecialBpduHwEntry.setStatus('current')
rlSpecialBpduHwAction = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 144, 2, 1, 2), HwAction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSpecialBpduHwAction.setStatus('current')
mibBuilder.exportSymbols("MARVELL-SpecialBpdu-MIB", PYSNMP_MODULE_ID=rlSpecialBpdu, rlSpecialBpduTable=rlSpecialBpduTable, rlSpecialBpduHwTable=rlSpecialBpduHwTable, Action=Action, HwAction=HwAction, rlSpecialBpduEncap=rlSpecialBpduEncap, rlSpecialBpduProtId=rlSpecialBpduProtId, rlSpecialBpduHwAction=rlSpecialBpduHwAction, rlSpecialBpduHwEntry=rlSpecialBpduHwEntry, rlSpecialBpduMacAddr=rlSpecialBpduMacAddr, rlSpecialBpduEntry=rlSpecialBpduEntry, rlSpecialBpdu=rlSpecialBpdu, EncapType=EncapType, rlSpecialBpduAction=rlSpecialBpduAction, rlSpecialBpduRowStatus=rlSpecialBpduRowStatus)
