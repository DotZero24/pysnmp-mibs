#
# PySNMP MIB module HPN-ICF-FIREWALL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/HPN-ICF-FIREWALL-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:03:13 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpnicfFireWall = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 88))
if mibBuilder.loadTexts: hpnicfFireWall.setLastUpdated('200801171450Z')
if mibBuilder.loadTexts: hpnicfFireWall.setOrganization('')
hpnicfFirewallobject = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 88, 1))
hpnicfFirewallSpecs = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 88, 1, 1))
hpnicfFWMaxConnNum = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 88, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFWMaxConnNum.setStatus('current')
hpnicfFirewallGlobalStats = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 88, 1, 2))
hpnicfFWConnNumCurr = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 88, 1, 2, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFWConnNumCurr.setStatus('current')
hpnicfFWConnRate = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 88, 1, 2, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFWConnRate.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-FIREWALL-MIB", hpnicfFirewallSpecs=hpnicfFirewallSpecs, hpnicfFirewallGlobalStats=hpnicfFirewallGlobalStats, PYSNMP_MODULE_ID=hpnicfFireWall, hpnicfFirewallobject=hpnicfFirewallobject, hpnicfFWConnRate=hpnicfFWConnRate, hpnicfFireWall=hpnicfFireWall, hpnicfFWConnNumCurr=hpnicfFWConnNumCurr, hpnicfFWMaxConnNum=hpnicfFWMaxConnNum)
