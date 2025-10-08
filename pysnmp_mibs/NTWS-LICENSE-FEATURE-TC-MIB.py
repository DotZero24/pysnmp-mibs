#
# PySNMP MIB module NTWS-LICENSE-FEATURE-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/nortel/NTWS-LICENSE-FEATURE-TC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:59:08 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ntwsMibs, = mibBuilder.importSymbols("NTWS-ROOT-MIB", "ntwsMibs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
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
