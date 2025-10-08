#
# PySNMP MIB module HPN-ICF-FIREWALL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HPN-ICF-FIREWALL-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:09:28 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("HPN-ICF-FIREWALL-MIB", PYSNMP_MODULE_ID=hpnicfFireWall, hpnicfFWMaxConnNum=hpnicfFWMaxConnNum, hpnicfFirewallGlobalStats=hpnicfFirewallGlobalStats, hpnicfFWConnRate=hpnicfFWConnRate, hpnicfFirewallSpecs=hpnicfFirewallSpecs, hpnicfFirewallobject=hpnicfFirewallobject, hpnicfFWConnNumCurr=hpnicfFWConnNumCurr, hpnicfFireWall=hpnicfFireWall)
