#
# PySNMP MIB module TRAPEZE-NETWORKS-LICENSE-FEATURE-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/trapeze/TRAPEZE-NETWORKS-LICENSE-FEATURE-TC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:05:21 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
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

mibBuilder.exportSymbols("TRAPEZE-NETWORKS-LICENSE-FEATURE-TC-MIB", TrpzLicenseFeature=TrpzLicenseFeature, trpzLicenseFeatureTc=trpzLicenseFeatureTc, PYSNMP_MODULE_ID=trpzLicenseFeatureTc)
