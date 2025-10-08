#
# PySNMP MIB module H3C-FIREWALL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/h3c/H3C-FIREWALL-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:10:32 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
h3cFireWall = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 88))
if mibBuilder.loadTexts: h3cFireWall.setLastUpdated('200801171450Z')
if mibBuilder.loadTexts: h3cFireWall.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
h3cFirewallobject = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 88, 1))
h3cFirewallSpecs = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 88, 1, 1))
h3cFWMaxConnNum = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 88, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFWMaxConnNum.setStatus('current')
h3cFirewallGlobalStats = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 88, 1, 2))
h3cFWConnNumCurr = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 88, 1, 2, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFWConnNumCurr.setStatus('current')
h3cFWConnRate = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 88, 1, 2, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFWConnRate.setStatus('current')
mibBuilder.exportSymbols("H3C-FIREWALL-MIB", h3cFireWall=h3cFireWall, h3cFirewallobject=h3cFirewallobject, h3cFirewallGlobalStats=h3cFirewallGlobalStats, h3cFWConnRate=h3cFWConnRate, h3cFirewallSpecs=h3cFirewallSpecs, PYSNMP_MODULE_ID=h3cFireWall, h3cFWMaxConnNum=h3cFWMaxConnNum, h3cFWConnNumCurr=h3cFWConnNumCurr)
