#
# PySNMP MIB module A3COM-HUAWEI-ARP-RATELIMIT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/a3com/A3COM-HUAWEI-ARP-RATELIMIT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:16:57 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("A3COM-HUAWEI-ARP-RATELIMIT-MIB", h3cARPRatelimitTrapCount=h3cARPRatelimitTrapCount, PYSNMP_MODULE_ID=h3cARPRatelimit, h3cARPRatelimitTrapVer=h3cARPRatelimitTrapVer, h3cARPRatelimitTrapMsg=h3cARPRatelimitTrapMsg, h3cARPRatelimitTrapObjects=h3cARPRatelimitTrapObjects, h3cARPRatelimitTrap=h3cARPRatelimitTrap, h3cARPRatelimitOverspeedTrap=h3cARPRatelimitOverspeedTrap, h3cARPRatelimit=h3cARPRatelimit, h3cARPRatelimitTraps=h3cARPRatelimitTraps, h3cARPRatelimitObjects=h3cARPRatelimitObjects)
