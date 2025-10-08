#
# PySNMP MIB module EDGECORE-RLPFC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/edgecore/EDGECORE-RLPFC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:05:25 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
rnd, = mibBuilder.importSymbols("EDGECORE-MIB", "rnd")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
rlPfcMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 148))
rlPfcMib.setRevisions(('2010-04-18 00:00',))
if mibBuilder.loadTexts: rlPfcMib.setLastUpdated('201004180000Z')
if mibBuilder.loadTexts: rlPfcMib.setOrganization('Radlan Computer Communications Ltd.')
class RlPfcPriority(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 7)

rlPfcGlobalEnable = MibScalar((1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 148, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPfcGlobalEnable.setStatus('current')
rlPfcPortTable = MibTable((1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 148, 2), )
if mibBuilder.loadTexts: rlPfcPortTable.setStatus('current')
rlPfcPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 148, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rlPfcPortEntry.setStatus('current')
rlPfcPortEnableAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 148, 2, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPfcPortEnableAdmin.setStatus('current')
rlPfcPortEnableOper = MibTableColumn((1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 148, 2, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPfcPortEnableOper.setStatus('current')
rlPfcPriorityTable = MibTable((1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 148, 3), )
if mibBuilder.loadTexts: rlPfcPriorityTable.setStatus('current')
rlPfcPriorityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 148, 3, 1), ).setIndexNames((0, "EDGECORE-RLPFC-MIB", "rlPfcPriority"))
if mibBuilder.loadTexts: rlPfcPriorityEntry.setStatus('current')
rlPfcPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 148, 3, 1, 1), RlPfcPriority())
if mibBuilder.loadTexts: rlPfcPriority.setStatus('current')
rlPfcPriorityEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 148, 3, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPfcPriorityEnable.setStatus('current')
rlPfcPriorityEnableOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 148, 3, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPfcPriorityEnableOperStatus.setStatus('current')
rlPfcPriorityEnableOperStatusReason = MibTableColumn((1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 148, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("ok", 1), ("pfcGlobalDis", 2), ("pfcPriorityAdminDis", 3), ("queue0", 4), ("sharedQueue", 5), ("notSameQueue", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPfcPriorityEnableOperStatusReason.setStatus('current')
mibBuilder.exportSymbols("EDGECORE-RLPFC-MIB", rlPfcPortEnableOper=rlPfcPortEnableOper, rlPfcMib=rlPfcMib, rlPfcGlobalEnable=rlPfcGlobalEnable, RlPfcPriority=RlPfcPriority, rlPfcPortEnableAdmin=rlPfcPortEnableAdmin, rlPfcPriorityEntry=rlPfcPriorityEntry, rlPfcPriority=rlPfcPriority, rlPfcPriorityEnable=rlPfcPriorityEnable, rlPfcPriorityEnableOperStatus=rlPfcPriorityEnableOperStatus, rlPfcPriorityEnableOperStatusReason=rlPfcPriorityEnableOperStatusReason, rlPfcPriorityTable=rlPfcPriorityTable, rlPfcPortTable=rlPfcPortTable, rlPfcPortEntry=rlPfcPortEntry, PYSNMP_MODULE_ID=rlPfcMib)
