#
# PySNMP MIB module SUPERMICRO-FIPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/supermicro/SUPERMICRO-FIPS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:57:59 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
fsFips = ModuleIdentity((1, 3, 6, 1, 4, 1, 10876, 101, 2, 63))
fsFips.setRevisions(('2012-09-05 00:00',))
if mibBuilder.loadTexts: fsFips.setLastUpdated('201209050000Z')
if mibBuilder.loadTexts: fsFips.setOrganization('Super Micro Computer Inc.')
fsFipsConfigurations = MibIdentifier((1, 3, 6, 1, 4, 1, 10876, 101, 2, 63, 1))
fsFipsOperMode = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 2, 63, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fips", 1), ("nonfips", 2))).clone('nonfips')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsFipsOperMode.setStatus('current')
fsFipsTestAlgo = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 2, 63, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsFipsTestAlgo.setStatus('current')
fsfipsZeroizeCryptoKeys = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 2, 63, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsfipsZeroizeCryptoKeys.setStatus('current')
fsFipsTraceLevel = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 2, 63, 1, 4), Integer32().clone(0)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsFipsTraceLevel.setStatus('current')
fsFipsTestExecutionResult = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 2, 63, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsFipsTestExecutionResult.setStatus('current')
fsFipsFailedAlgorithm = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 2, 63, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsFipsFailedAlgorithm.setStatus('current')
fsFipsBypassCapability = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 2, 63, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("bypassCapability", 1), ("noBypassCapability", 2))).clone('noBypassCapability')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsFipsBypassCapability.setStatus('current')
mibBuilder.exportSymbols("SUPERMICRO-FIPS-MIB", PYSNMP_MODULE_ID=fsFips, fsFipsTestExecutionResult=fsFipsTestExecutionResult, fsFips=fsFips, fsFipsConfigurations=fsFipsConfigurations, fsfipsZeroizeCryptoKeys=fsfipsZeroizeCryptoKeys, fsFipsBypassCapability=fsFipsBypassCapability, fsFipsFailedAlgorithm=fsFipsFailedAlgorithm, fsFipsOperMode=fsFipsOperMode, fsFipsTraceLevel=fsFipsTraceLevel, fsFipsTestAlgo=fsFipsTestAlgo)
