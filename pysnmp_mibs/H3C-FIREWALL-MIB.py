#
# PySNMP MIB module H3C-FIREWALL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/h3c/H3C-FIREWALL-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:22:20 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("H3C-FIREWALL-MIB", h3cFWConnNumCurr=h3cFWConnNumCurr, h3cFirewallSpecs=h3cFirewallSpecs, h3cFirewallGlobalStats=h3cFirewallGlobalStats, h3cFWMaxConnNum=h3cFWMaxConnNum, h3cFWConnRate=h3cFWConnRate, h3cFirewallobject=h3cFirewallobject, PYSNMP_MODULE_ID=h3cFireWall, h3cFireWall=h3cFireWall)
