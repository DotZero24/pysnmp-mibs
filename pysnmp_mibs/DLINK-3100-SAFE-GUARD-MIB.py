#
# PySNMP MIB module DLINK-3100-SAFE-GUARD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/DLINK-3100-SAFE-GUARD-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:59:50 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("DLINK-3100-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
rlSafeGuard = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 131))
rlSafeGuard.setRevisions(('2007-11-18 00:00',))
if mibBuilder.loadTexts: rlSafeGuard.setLastUpdated('2007111800Z')
if mibBuilder.loadTexts: rlSafeGuard.setOrganization('Dlink, Inc.')
rlSafeGuardEnabled = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 131, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSafeGuardEnabled.setStatus('current')
rlSafeGuardStatus = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 131, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("idle", 0), ("attack", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSafeGuardStatus.setStatus('current')
rlSafeGuardCpuUtilizationUpper = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 131, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(70)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSafeGuardCpuUtilizationUpper.setStatus('current')
rlSafeGuardCpuUtilizationLower = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 131, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSafeGuardCpuUtilizationLower.setStatus('current')
rlSafeGuardBroadcastRateUpper = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 131, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(90, 1000)).clone(350)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSafeGuardBroadcastRateUpper.setStatus('current')
rlSafeGuardBroadcastRateLower = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 131, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(90, 1000)).clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSafeGuardBroadcastRateLower.setStatus('current')
mibBuilder.exportSymbols("DLINK-3100-SAFE-GUARD-MIB", rlSafeGuard=rlSafeGuard, rlSafeGuardCpuUtilizationLower=rlSafeGuardCpuUtilizationLower, rlSafeGuardCpuUtilizationUpper=rlSafeGuardCpuUtilizationUpper, rlSafeGuardEnabled=rlSafeGuardEnabled, rlSafeGuardBroadcastRateUpper=rlSafeGuardBroadcastRateUpper, PYSNMP_MODULE_ID=rlSafeGuard, rlSafeGuardStatus=rlSafeGuardStatus, rlSafeGuardBroadcastRateLower=rlSafeGuardBroadcastRateLower)
