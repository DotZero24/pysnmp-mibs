#
# PySNMP MIB module A3COM-HUAWEI-FIREWALL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/a3com/A3COM-HUAWEI-FIREWALL-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:33:09 2025
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
h3cFireWall = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 88))
if mibBuilder.loadTexts: h3cFireWall.setLastUpdated('200801171450Z')
if mibBuilder.loadTexts: h3cFireWall.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
h3cFirewallobject = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 88, 1))
h3cFirewallSpecs = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 88, 1, 1))
h3cFWMaxConnNum = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 88, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFWMaxConnNum.setStatus('current')
h3cFirewallGlobalStats = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 88, 1, 2))
h3cFWConnNumCurr = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 88, 1, 2, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFWConnNumCurr.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-FIREWALL-MIB", h3cFWConnNumCurr=h3cFWConnNumCurr, h3cFirewallSpecs=h3cFirewallSpecs, h3cFirewallGlobalStats=h3cFirewallGlobalStats, h3cFWMaxConnNum=h3cFWMaxConnNum, h3cFirewallobject=h3cFirewallobject, PYSNMP_MODULE_ID=h3cFireWall, h3cFireWall=h3cFireWall)
