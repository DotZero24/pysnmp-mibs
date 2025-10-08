#
# PySNMP MIB module WESTERMO-SW6-PWN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/westermo/WESTERMO-SW6-PWN-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:35:57 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pwn = ModuleIdentity((1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 9))
pwn.setRevisions(('2019-09-06 00:00',))
if mibBuilder.loadTexts: pwn.setLastUpdated('201909060000Z')
if mibBuilder.loadTexts: pwn.setOrganization('Westermo Teleindustri AB')
configuration = MibIdentifier((1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 9, 1))
cfgWireless = MibIdentifier((1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 9, 1, 1))
conformance = MibIdentifier((1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 9, 10000))
groups = MibIdentifier((1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 9, 10000, 1))
groupConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 9, 10000, 1, 1))
compliances = MibIdentifier((1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 9, 10000, 2))
cfgWlanBandsteering = MibIdentifier((1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 9, 1, 1, 1))
cfgWlanBsteerEnabled = MibScalar((1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 9, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfgWlanBsteerEnabled.setStatus('current')
cfgWlanBsteerMatchingSsid = MibScalar((1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 9, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfgWlanBsteerMatchingSsid.setStatus('current')
groupCfgWlanBandsteering = ObjectGroup((1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 9, 10000, 1, 1, 1)).setObjects(("WESTERMO-SW6-PWN-MIB", "cfgWlanBsteerEnabled"), ("WESTERMO-SW6-PWN-MIB", "cfgWlanBsteerMatchingSsid"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    groupCfgWlanBandsteering = groupCfgWlanBandsteering.setStatus('current')
compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 9, 10000, 2, 1)).setObjects(("WESTERMO-SW6-PWN-MIB", "groupCfgWlanBandsteering"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    compliance = compliance.setStatus('current')
mibBuilder.exportSymbols("WESTERMO-SW6-PWN-MIB", compliances=compliances, cfgWlanBandsteering=cfgWlanBandsteering, groupCfgWlanBandsteering=groupCfgWlanBandsteering, cfgWlanBsteerEnabled=cfgWlanBsteerEnabled, cfgWireless=cfgWireless, conformance=conformance, compliance=compliance, pwn=pwn, cfgWlanBsteerMatchingSsid=cfgWlanBsteerMatchingSsid, configuration=configuration, PYSNMP_MODULE_ID=pwn, groups=groups, groupConfiguration=groupConfiguration)
