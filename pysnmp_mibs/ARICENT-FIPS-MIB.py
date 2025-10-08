#
# PySNMP MIB module ARICENT-FIPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/aricent/ARICENT-FIPS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:33:06 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
fsFips = ModuleIdentity((1, 3, 6, 1, 4, 1, 29601, 2, 63))
fsFips.setRevisions(('2012-09-05 00:00',))
if mibBuilder.loadTexts: fsFips.setLastUpdated('201209050000Z')
if mibBuilder.loadTexts: fsFips.setOrganization('ARICENT COMMUNICATIONS SOFTWARE')
fsFipsConfigurations = MibIdentifier((1, 3, 6, 1, 4, 1, 29601, 2, 63, 1))
fsFipsOperMode = MibScalar((1, 3, 6, 1, 4, 1, 29601, 2, 63, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fips", 1), ("nonfips", 2))).clone('nonfips')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsFipsOperMode.setStatus('current')
fsFipsTestAlgo = MibScalar((1, 3, 6, 1, 4, 1, 29601, 2, 63, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsFipsTestAlgo.setStatus('current')
fsfipsZeroizeCryptoKeys = MibScalar((1, 3, 6, 1, 4, 1, 29601, 2, 63, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsfipsZeroizeCryptoKeys.setStatus('current')
fsFipsTraceLevel = MibScalar((1, 3, 6, 1, 4, 1, 29601, 2, 63, 1, 4), Integer32().clone(0)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsFipsTraceLevel.setStatus('current')
fsFipsTestExecutionResult = MibScalar((1, 3, 6, 1, 4, 1, 29601, 2, 63, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsFipsTestExecutionResult.setStatus('current')
fsFipsFailedAlgorithm = MibScalar((1, 3, 6, 1, 4, 1, 29601, 2, 63, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsFipsFailedAlgorithm.setStatus('current')
fsFipsBypassCapability = MibScalar((1, 3, 6, 1, 4, 1, 29601, 2, 63, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("bypassCapability", 1), ("noBypassCapability", 2))).clone('noBypassCapability')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsFipsBypassCapability.setStatus('current')
mibBuilder.exportSymbols("ARICENT-FIPS-MIB", fsFipsTestExecutionResult=fsFipsTestExecutionResult, fsFipsOperMode=fsFipsOperMode, fsFipsConfigurations=fsFipsConfigurations, fsfipsZeroizeCryptoKeys=fsfipsZeroizeCryptoKeys, fsFips=fsFips, fsFipsFailedAlgorithm=fsFipsFailedAlgorithm, PYSNMP_MODULE_ID=fsFips, fsFipsTraceLevel=fsFipsTraceLevel, fsFipsTestAlgo=fsFipsTestAlgo, fsFipsBypassCapability=fsFipsBypassCapability)
