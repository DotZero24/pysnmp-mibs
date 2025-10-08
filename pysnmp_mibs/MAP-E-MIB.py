#
# PySNMP MIB module MAP-E-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/rfc/MAP-E-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:49:23 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddressIPv4, InetAddressIPv6, InetAddressPrefixLength = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv4", "InetAddressIPv6", "InetAddressPrefixLength")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Gauge32, MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "mib-2")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mapMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 242))
mapMIB.setRevisions(('2018-11-26 00:00',))
if mibBuilder.loadTexts: mapMIB.setLastUpdated('201811260000Z')
if mibBuilder.loadTexts: mapMIB.setOrganization('IETF Softwire Working Group')
mapMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 242, 1))
mapRule = MibIdentifier((1, 3, 6, 1, 2, 1, 242, 1, 1))
mapSecurityCheck = MibIdentifier((1, 3, 6, 1, 2, 1, 242, 1, 2))
class RulePSID(TextualConvention, OctetString):
    status = 'current'
    displayHint = '0x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 2)
    fixedLength = 2

class RuleType(TextualConvention, Integer32):
    reference = 'bmr, fmr: Section 5 of RFC 7597. bmrAndfmr: Section 5 of RFC 7597, Section 4.1 of RFC 7598.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("bmr", 1), ("fmr", 2), ("bmrAndfmr", 3))

mapRuleTable = MibTable((1, 3, 6, 1, 2, 1, 242, 1, 1, 1), )
if mibBuilder.loadTexts: mapRuleTable.setStatus('current')
mapRuleEntry = MibTableRow((1, 3, 6, 1, 2, 1, 242, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "MAP-E-MIB", "mapRuleID"))
if mibBuilder.loadTexts: mapRuleEntry.setStatus('current')
mapRuleID = MibTableColumn((1, 3, 6, 1, 2, 1, 242, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: mapRuleID.setStatus('current')
mapRuleIPv6Prefix = MibTableColumn((1, 3, 6, 1, 2, 1, 242, 1, 1, 1, 1, 2), InetAddressIPv6()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mapRuleIPv6Prefix.setStatus('current')
mapRuleIPv6PrefixLen = MibTableColumn((1, 3, 6, 1, 2, 1, 242, 1, 1, 1, 1, 3), InetAddressPrefixLength()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mapRuleIPv6PrefixLen.setStatus('current')
mapRuleIPv4Prefix = MibTableColumn((1, 3, 6, 1, 2, 1, 242, 1, 1, 1, 1, 4), InetAddressIPv4()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mapRuleIPv4Prefix.setStatus('current')
mapRuleIPv4PrefixLen = MibTableColumn((1, 3, 6, 1, 2, 1, 242, 1, 1, 1, 1, 5), InetAddressPrefixLength()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mapRuleIPv4PrefixLen.setStatus('current')
mapRuleBRIPv6Address = MibTableColumn((1, 3, 6, 1, 2, 1, 242, 1, 1, 1, 1, 6), InetAddressIPv6()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mapRuleBRIPv6Address.setStatus('current')
mapRulePSID = MibTableColumn((1, 3, 6, 1, 2, 1, 242, 1, 1, 1, 1, 7), RulePSID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mapRulePSID.setStatus('current')
mapRulePSIDLen = MibTableColumn((1, 3, 6, 1, 2, 1, 242, 1, 1, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mapRulePSIDLen.setStatus('current')
mapRuleOffset = MibTableColumn((1, 3, 6, 1, 2, 1, 242, 1, 1, 1, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)).clone(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mapRuleOffset.setStatus('current')
mapRuleEALen = MibTableColumn((1, 3, 6, 1, 2, 1, 242, 1, 1, 1, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 48))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mapRuleEALen.setStatus('current')
mapRuleType = MibTableColumn((1, 3, 6, 1, 2, 1, 242, 1, 1, 1, 1, 11), RuleType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mapRuleType.setStatus('current')
mapSecurityCheckTable = MibTable((1, 3, 6, 1, 2, 1, 242, 1, 2, 1), )
if mibBuilder.loadTexts: mapSecurityCheckTable.setStatus('current')
mapSecurityCheckEntry = MibTableRow((1, 3, 6, 1, 2, 1, 242, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: mapSecurityCheckEntry.setStatus('current')
mapSecurityCheckInvalidv4 = MibTableColumn((1, 3, 6, 1, 2, 1, 242, 1, 2, 1, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mapSecurityCheckInvalidv4.setStatus('current')
mapSecurityCheckInvalidv6 = MibTableColumn((1, 3, 6, 1, 2, 1, 242, 1, 2, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mapSecurityCheckInvalidv6.setStatus('current')
mapMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 242, 2))
mapMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 242, 2, 1))
mapMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 242, 2, 2))
mapMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 242, 2, 1, 1)).setObjects(("MAP-E-MIB", "mapMIBRuleGroup"), ("MAP-E-MIB", "mapMIBSecurityGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mapMIBCompliance = mapMIBCompliance.setStatus('current')
mapMIBRuleGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 242, 2, 2, 1)).setObjects(("MAP-E-MIB", "mapRuleIPv6Prefix"), ("MAP-E-MIB", "mapRuleIPv6PrefixLen"), ("MAP-E-MIB", "mapRuleIPv4Prefix"), ("MAP-E-MIB", "mapRuleIPv4PrefixLen"), ("MAP-E-MIB", "mapRuleBRIPv6Address"), ("MAP-E-MIB", "mapRulePSID"), ("MAP-E-MIB", "mapRulePSIDLen"), ("MAP-E-MIB", "mapRuleOffset"), ("MAP-E-MIB", "mapRuleEALen"), ("MAP-E-MIB", "mapRuleType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mapMIBRuleGroup = mapMIBRuleGroup.setStatus('current')
mapMIBSecurityGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 242, 2, 2, 2)).setObjects(("MAP-E-MIB", "mapSecurityCheckInvalidv4"), ("MAP-E-MIB", "mapSecurityCheckInvalidv6"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mapMIBSecurityGroup = mapMIBSecurityGroup.setStatus('current')
mibBuilder.exportSymbols("MAP-E-MIB", RuleType=RuleType, mapSecurityCheckInvalidv4=mapSecurityCheckInvalidv4, mapMIBConformance=mapMIBConformance, mapRuleIPv6Prefix=mapRuleIPv6Prefix, RulePSID=RulePSID, mapMIBCompliances=mapMIBCompliances, mapMIBGroups=mapMIBGroups, mapRuleEntry=mapRuleEntry, mapSecurityCheckTable=mapSecurityCheckTable, mapMIBCompliance=mapMIBCompliance, mapRuleBRIPv6Address=mapRuleBRIPv6Address, mapSecurityCheckEntry=mapSecurityCheckEntry, mapMIB=mapMIB, mapRulePSID=mapRulePSID, mapMIBObjects=mapMIBObjects, mapRulePSIDLen=mapRulePSIDLen, mapRuleID=mapRuleID, mapSecurityCheckInvalidv6=mapSecurityCheckInvalidv6, mapMIBRuleGroup=mapMIBRuleGroup, mapRuleTable=mapRuleTable, mapRuleEALen=mapRuleEALen, mapRuleIPv6PrefixLen=mapRuleIPv6PrefixLen, mapRule=mapRule, mapRuleOffset=mapRuleOffset, mapSecurityCheck=mapSecurityCheck, mapRuleType=mapRuleType, mapMIBSecurityGroup=mapMIBSecurityGroup, mapRuleIPv4Prefix=mapRuleIPv4Prefix, PYSNMP_MODULE_ID=mapMIB, mapRuleIPv4PrefixLen=mapRuleIPv4PrefixLen)
