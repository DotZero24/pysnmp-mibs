#
# PySNMP MIB module A3COM-HUAWEI-ARP-RATELIMIT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/a3com/A3COM-HUAWEI-ARP-RATELIMIT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:33:18 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
h3cARPRatelimit = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 110))
h3cARPRatelimit.setRevisions(('2009-12-08 19:12',))
if mibBuilder.loadTexts: h3cARPRatelimit.setLastUpdated('200912081912Z')
if mibBuilder.loadTexts: h3cARPRatelimit.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
h3cARPRatelimitObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 110, 1))
h3cARPRatelimitTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 110, 1, 1))
h3cARPRatelimitTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 110, 1, 1, 0))
h3cARPRatelimitOverspeedTrap = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 110, 1, 1, 0, 1)).setObjects(("A3COM-HUAWEI-ARP-RATELIMIT-MIB", "h3cARPRatelimitTrapVer"), ("A3COM-HUAWEI-ARP-RATELIMIT-MIB", "h3cARPRatelimitTrapCount"), ("A3COM-HUAWEI-ARP-RATELIMIT-MIB", "h3cARPRatelimitTrapMsg"))
if mibBuilder.loadTexts: h3cARPRatelimitOverspeedTrap.setStatus('current')
h3cARPRatelimitTrapObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 110, 1, 1, 1))
h3cARPRatelimitTrapVer = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 110, 1, 1, 1, 1), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cARPRatelimitTrapVer.setStatus('current')
h3cARPRatelimitTrapCount = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 110, 1, 1, 1, 2), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cARPRatelimitTrapCount.setStatus('current')
h3cARPRatelimitTrapMsg = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 110, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 254))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cARPRatelimitTrapMsg.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-ARP-RATELIMIT-MIB", h3cARPRatelimitTraps=h3cARPRatelimitTraps, h3cARPRatelimitTrapVer=h3cARPRatelimitTrapVer, h3cARPRatelimit=h3cARPRatelimit, h3cARPRatelimitOverspeedTrap=h3cARPRatelimitOverspeedTrap, h3cARPRatelimitTrap=h3cARPRatelimitTrap, PYSNMP_MODULE_ID=h3cARPRatelimit, h3cARPRatelimitTrapMsg=h3cARPRatelimitTrapMsg, h3cARPRatelimitTrapObjects=h3cARPRatelimitTrapObjects, h3cARPRatelimitObjects=h3cARPRatelimitObjects, h3cARPRatelimitTrapCount=h3cARPRatelimitTrapCount)
