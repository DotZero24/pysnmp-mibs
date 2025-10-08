#
# PySNMP MIB module MAP-E-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rfc/MAP-E-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:27:12 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddressPrefixLength, InetAddressIPv6, InetAddressIPv4 = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressPrefixLength", "InetAddressIPv6", "InetAddressIPv4")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Integer32, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, TimeTicks, MibIdentifier, Counter64, Bits, mib_2, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "TimeTicks", "MibIdentifier", "Counter64", "Bits", "mib-2", "IpAddress")
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
mibBuilder.exportSymbols("MAP-E-MIB", mapRulePSID=mapRulePSID, RuleType=RuleType, mapMIBGroups=mapMIBGroups, mapMIBSecurityGroup=mapMIBSecurityGroup, mapRuleIPv4Prefix=mapRuleIPv4Prefix, mapSecurityCheckInvalidv6=mapSecurityCheckInvalidv6, mapRuleTable=mapRuleTable, mapRule=mapRule, mapRulePSIDLen=mapRulePSIDLen, mapMIBConformance=mapMIBConformance, RulePSID=RulePSID, mapRuleIPv4PrefixLen=mapRuleIPv4PrefixLen, mapMIB=mapMIB, mapSecurityCheckInvalidv4=mapSecurityCheckInvalidv4, mapMIBCompliances=mapMIBCompliances, mapRuleIPv6Prefix=mapRuleIPv6Prefix, mapRuleBRIPv6Address=mapRuleBRIPv6Address, mapRuleType=mapRuleType, mapRuleIPv6PrefixLen=mapRuleIPv6PrefixLen, mapRuleOffset=mapRuleOffset, mapMIBObjects=mapMIBObjects, PYSNMP_MODULE_ID=mapMIB, mapRuleEALen=mapRuleEALen, mapMIBCompliance=mapMIBCompliance, mapRuleEntry=mapRuleEntry, mapMIBRuleGroup=mapMIBRuleGroup, mapSecurityCheckEntry=mapSecurityCheckEntry, mapSecurityCheckTable=mapSecurityCheckTable, mapSecurityCheck=mapSecurityCheck, mapRuleID=mapRuleID)
