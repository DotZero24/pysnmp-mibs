#
# PySNMP MIB module CISCOSB-ERRDISABLE-RECOVERY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/ciscosb/CISCOSB-ERRDISABLE-RECOVERY-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:55:53 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "DisplayString", "TextualConvention")
rlErrdisableRecovery = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 128))
rlErrdisableRecovery.setRevisions(('2007-11-07 00:00',))
if mibBuilder.loadTexts: rlErrdisableRecovery.setLastUpdated('200711070000Z')
if mibBuilder.loadTexts: rlErrdisableRecovery.setOrganization('Cisco Systems, Inc.')
class RlErrdisableRecoveryCauseType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("loopback-detection", 1), ("port-security", 2), ("dot1x-src-address", 3), ("acl-deny", 4), ("stp-bpdu-guard", 5), ("stp-loopback-guard", 6), ("pcb-overheat", 7), ("udld", 8), ("storm-control", 9), ("link-flapping", 10))

rlErrdisableRecoveryInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 128, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 86400))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlErrdisableRecoveryInterval.setStatus('current')
rlErrdisableRecoveryCauseTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 128, 2), )
if mibBuilder.loadTexts: rlErrdisableRecoveryCauseTable.setStatus('current')
rlErrdisableRecoveryCauseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 128, 2, 1), ).setIndexNames((0, "CISCOSB-ERRDISABLE-RECOVERY-MIB", "rlErrdisableRecoveryCause"))
if mibBuilder.loadTexts: rlErrdisableRecoveryCauseEntry.setStatus('current')
rlErrdisableRecoveryCause = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 128, 2, 1, 1), RlErrdisableRecoveryCauseType())
if mibBuilder.loadTexts: rlErrdisableRecoveryCause.setStatus('current')
rlErrdisableRecoveryEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 128, 2, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlErrdisableRecoveryEnable.setStatus('current')
rlErrdisableRecoveryIfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 128, 3), )
if mibBuilder.loadTexts: rlErrdisableRecoveryIfTable.setStatus('current')
rlErrdisableRecoveryIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 128, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rlErrdisableRecoveryIfEntry.setStatus('current')
rlErrdisableRecoveryIfReason = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 128, 3, 1, 1), RlErrdisableRecoveryCauseType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlErrdisableRecoveryIfReason.setStatus('current')
rlErrdisableRecoveryIfEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 128, 3, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlErrdisableRecoveryIfEnable.setStatus('current')
rlErrdisableRecoveryIfTimeToRecover = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 128, 3, 1, 3), Integer32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rlErrdisableRecoveryIfTimeToRecover.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-ERRDISABLE-RECOVERY-MIB", rlErrdisableRecoveryIfReason=rlErrdisableRecoveryIfReason, rlErrdisableRecoveryIfEntry=rlErrdisableRecoveryIfEntry, rlErrdisableRecoveryInterval=rlErrdisableRecoveryInterval, PYSNMP_MODULE_ID=rlErrdisableRecovery, RlErrdisableRecoveryCauseType=RlErrdisableRecoveryCauseType, rlErrdisableRecoveryCauseEntry=rlErrdisableRecoveryCauseEntry, rlErrdisableRecoveryIfEnable=rlErrdisableRecoveryIfEnable, rlErrdisableRecoveryCauseTable=rlErrdisableRecoveryCauseTable, rlErrdisableRecoveryIfTable=rlErrdisableRecoveryIfTable, rlErrdisableRecoveryIfTimeToRecover=rlErrdisableRecoveryIfTimeToRecover, rlErrdisableRecoveryCause=rlErrdisableRecoveryCause, rlErrdisableRecovery=rlErrdisableRecovery, rlErrdisableRecoveryEnable=rlErrdisableRecoveryEnable)
