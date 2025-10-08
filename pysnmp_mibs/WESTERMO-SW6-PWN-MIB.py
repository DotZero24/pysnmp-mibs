#
# PySNMP MIB module WESTERMO-SW6-PWN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/westermo/WESTERMO-SW6-PWN-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:01:14 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("WESTERMO-SW6-PWN-MIB", PYSNMP_MODULE_ID=pwn, groupConfiguration=groupConfiguration, groups=groups, pwn=pwn, compliance=compliance, conformance=conformance, cfgWireless=cfgWireless, configuration=configuration, cfgWlanBandsteering=cfgWlanBandsteering, cfgWlanBsteerEnabled=cfgWlanBsteerEnabled, cfgWlanBsteerMatchingSsid=cfgWlanBsteerMatchingSsid, groupCfgWlanBandsteering=groupCfgWlanBandsteering, compliances=compliances)
