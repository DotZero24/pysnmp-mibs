#
# PySNMP MIB module DLINK-3100-SAFE-GUARD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/DLINK-3100-SAFE-GUARD-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:34:53 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
rnd, = mibBuilder.importSymbols("DLINK-3100-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
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
mibBuilder.exportSymbols("DLINK-3100-SAFE-GUARD-MIB", rlSafeGuardBroadcastRateLower=rlSafeGuardBroadcastRateLower, rlSafeGuardBroadcastRateUpper=rlSafeGuardBroadcastRateUpper, PYSNMP_MODULE_ID=rlSafeGuard, rlSafeGuardEnabled=rlSafeGuardEnabled, rlSafeGuard=rlSafeGuard, rlSafeGuardCpuUtilizationUpper=rlSafeGuardCpuUtilizationUpper, rlSafeGuardCpuUtilizationLower=rlSafeGuardCpuUtilizationLower, rlSafeGuardStatus=rlSafeGuardStatus)
