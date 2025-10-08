#
# PySNMP MIB module NTWS-LICENSE-FEATURE-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/nortel/NTWS-LICENSE-FEATURE-TC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:02:29 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ntwsMibs, = mibBuilder.importSymbols("NTWS-ROOT-MIB", "ntwsMibs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ntwsLicenseFeatureTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 19))
ntwsLicenseFeatureTc.setRevisions(('2009-11-16 00:01',))
if mibBuilder.loadTexts: ntwsLicenseFeatureTc.setLastUpdated('200911160001Z')
if mibBuilder.loadTexts: ntwsLicenseFeatureTc.setOrganization('Nortel Networks')
class NtwsLicenseFeature(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 11, 12, 13, 14, 15, 16))
    namedValues = NamedValues(("none", 1), ("maxSupportedAPsOrDAPs", 2), ("fips", 11), ("advancedVoice", 12), ("highAvailability", 13), ("maxSupportedHighSpeedMeshBridgingAPs", 14), ("maxSupportedWapiAPs", 15), ("maxSupportedAdvancedLocalSwitchingAPs", 16))

mibBuilder.exportSymbols("NTWS-LICENSE-FEATURE-TC-MIB", NtwsLicenseFeature=NtwsLicenseFeature, PYSNMP_MODULE_ID=ntwsLicenseFeatureTc, ntwsLicenseFeatureTc=ntwsLicenseFeatureTc)
