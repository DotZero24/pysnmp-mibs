#
# PySNMP MIB module TRAPEZE-NETWORKS-LICENSE-FEATURE-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/trapeze/TRAPEZE-NETWORKS-LICENSE-FEATURE-TC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:38:56 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
trpzMibs, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-ROOT-MIB", "trpzMibs")
trpzLicenseFeatureTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 14525, 4, 19))
trpzLicenseFeatureTc.setRevisions(('2011-01-27 01:00', '2009-11-17 00:20', '2009-11-16 00:01',))
if mibBuilder.loadTexts: trpzLicenseFeatureTc.setLastUpdated('201101270100Z')
if mibBuilder.loadTexts: trpzLicenseFeatureTc.setOrganization('Trapeze Networks')
class TrpzLicenseFeature(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 11, 12, 13, 14, 16, 17, 18))
    namedValues = NamedValues(("none", 1), ("maxSupportedAPsOrDAPs", 2), ("maxSupportedSessions", 3), ("fips", 11), ("advancedVoice", 12), ("highAvailability", 13), ("maxSupportedHighSpeedMeshBridgingAPs", 14), ("maxSupportedAdvancedLocalSwitchingAPs", 16), ("maxSupportedRemoteOfficeAPs", 17), ("maxSupportedSpectrumAnalysisAPs", 18))

mibBuilder.exportSymbols("TRAPEZE-NETWORKS-LICENSE-FEATURE-TC-MIB", PYSNMP_MODULE_ID=trpzLicenseFeatureTc, TrpzLicenseFeature=TrpzLicenseFeature, trpzLicenseFeatureTc=trpzLicenseFeatureTc)
