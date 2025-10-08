#
# PySNMP MIB module MX-NCS-COMPATIBILITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/media5/MX-NCS-COMPATIBILITY-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:05:24 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
mediatrixExperimental, = mibBuilder.importSymbols("MX-SMI", "mediatrixExperimental")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ncsCompatibilityMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4935, 99, 15))
ncsCompatibilityMIB.setRevisions(('2008-12-03 00:00', '1902-08-28 00:00',))
if mibBuilder.loadTexts: ncsCompatibilityMIB.setLastUpdated('200812030000Z')
if mibBuilder.loadTexts: ncsCompatibilityMIB.setOrganization('Mediatrix Telecom, Inc.')
ncsCompatibilityMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 99, 15, 1))
ncsCompatibilityConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 99, 15, 2))
ncsCompatibilityRtpPayloadType18EncodingName = MibScalar((1, 3, 6, 1, 4, 1, 4935, 99, 15, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("g729", 0), ("g729A", 1))).clone('g729')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncsCompatibilityRtpPayloadType18EncodingName.setStatus('current')
ncsCompatibilityVersion = MibScalar((1, 3, 6, 1, 4, 1, 4935, 99, 15, 1, 100), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("mgcp01Ncs10", 0), ("fakeMgcp10Ncs10", 1))).clone('mgcp01Ncs10')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncsCompatibilityVersion.setStatus('current')
ncsCompatibilityCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 99, 15, 2, 1))
ncsCompatibilityComplVer1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4935, 99, 15, 2, 1, 10)).setObjects(("MX-NCS-COMPATIBILITY-MIB", "ncsCompatibilityBasicGroupVer1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ncsCompatibilityComplVer1 = ncsCompatibilityComplVer1.setStatus('current')
ncsCompatibilityGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 99, 15, 2, 2))
ncsCompatibilityBasicGroupVer1 = ObjectGroup((1, 3, 6, 1, 4, 1, 4935, 99, 15, 2, 2, 10)).setObjects(("MX-NCS-COMPATIBILITY-MIB", "ncsCompatibilityRtpPayloadType18EncodingName"), ("MX-NCS-COMPATIBILITY-MIB", "ncsCompatibilityVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ncsCompatibilityBasicGroupVer1 = ncsCompatibilityBasicGroupVer1.setStatus('current')
mibBuilder.exportSymbols("MX-NCS-COMPATIBILITY-MIB", ncsCompatibilityRtpPayloadType18EncodingName=ncsCompatibilityRtpPayloadType18EncodingName, ncsCompatibilityConformance=ncsCompatibilityConformance, ncsCompatibilityVersion=ncsCompatibilityVersion, PYSNMP_MODULE_ID=ncsCompatibilityMIB, ncsCompatibilityBasicGroupVer1=ncsCompatibilityBasicGroupVer1, ncsCompatibilityCompliances=ncsCompatibilityCompliances, ncsCompatibilityGroups=ncsCompatibilityGroups, ncsCompatibilityMIBObjects=ncsCompatibilityMIBObjects, ncsCompatibilityComplVer1=ncsCompatibilityComplVer1, ncsCompatibilityMIB=ncsCompatibilityMIB)
