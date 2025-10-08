#
# PySNMP MIB module ENTERASYS-IMAGE-VALIDATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/enterasys/ENTERASYS-IMAGE-VALIDATION-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:17:22 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
etsysImageValidationMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 47))
etsysImageValidationMIB.setRevisions(('2004-04-02 21:34',))
if mibBuilder.loadTexts: etsysImageValidationMIB.setLastUpdated('200404022134Z')
if mibBuilder.loadTexts: etsysImageValidationMIB.setOrganization('Enterasys Networks')
etsysImageValidationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 47, 1))
etsysImageValidationConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 47, 1, 1))
etsysImageValidationEnable = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 47, 1, 1, 1), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysImageValidationEnable.setStatus('current')
etsysImageValidationPeriod = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 47, 1, 1, 2), Unsigned32().clone(600)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysImageValidationPeriod.setStatus('current')
etsysImageValidationOperations = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 47, 1, 1, 3), Bits().clone(namedValues=NamedValues(("etsysImageValidationConfig", 0), ("etsysImageValidationIcmp", 1), ("etsysImageValidationSnmp", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysImageValidationOperations.setStatus('current')
etsysImageValidationIcmpAddressType = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 47, 1, 1, 4), InetAddressType().clone('ipv4')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysImageValidationIcmpAddressType.setStatus('current')
etsysImageValidationIcmpAddress = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 47, 1, 1, 5), InetAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysImageValidationIcmpAddress.setStatus('current')
etsysImageValidationSnmpAddressType = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 47, 1, 1, 6), InetAddressType().clone('ipv4')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysImageValidationSnmpAddressType.setStatus('current')
etsysImageValidationSnmpAddress = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 47, 1, 1, 7), InetAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysImageValidationSnmpAddress.setStatus('current')
etsysImageValidationConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 47, 2))
etsysImageValidationGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 47, 2, 1))
etsysImageValidationCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 47, 2, 2))
etsysImageValidationConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 47, 2, 1, 1)).setObjects(("ENTERASYS-IMAGE-VALIDATION-MIB", "etsysImageValidationEnable"), ("ENTERASYS-IMAGE-VALIDATION-MIB", "etsysImageValidationPeriod"), ("ENTERASYS-IMAGE-VALIDATION-MIB", "etsysImageValidationOperations"), ("ENTERASYS-IMAGE-VALIDATION-MIB", "etsysImageValidationIcmpAddressType"), ("ENTERASYS-IMAGE-VALIDATION-MIB", "etsysImageValidationIcmpAddress"), ("ENTERASYS-IMAGE-VALIDATION-MIB", "etsysImageValidationSnmpAddressType"), ("ENTERASYS-IMAGE-VALIDATION-MIB", "etsysImageValidationSnmpAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysImageValidationConfigGroup = etsysImageValidationConfigGroup.setStatus('current')
etsysImageValidationCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 47, 2, 2, 1)).setObjects(("ENTERASYS-IMAGE-VALIDATION-MIB", "etsysImageValidationConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysImageValidationCompliance = etsysImageValidationCompliance.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-IMAGE-VALIDATION-MIB", etsysImageValidationIcmpAddress=etsysImageValidationIcmpAddress, etsysImageValidationMIB=etsysImageValidationMIB, PYSNMP_MODULE_ID=etsysImageValidationMIB, etsysImageValidationOperations=etsysImageValidationOperations, etsysImageValidationEnable=etsysImageValidationEnable, etsysImageValidationConformance=etsysImageValidationConformance, etsysImageValidationCompliances=etsysImageValidationCompliances, etsysImageValidationSnmpAddressType=etsysImageValidationSnmpAddressType, etsysImageValidationObjects=etsysImageValidationObjects, etsysImageValidationPeriod=etsysImageValidationPeriod, etsysImageValidationConfig=etsysImageValidationConfig, etsysImageValidationSnmpAddress=etsysImageValidationSnmpAddress, etsysImageValidationConfigGroup=etsysImageValidationConfigGroup, etsysImageValidationIcmpAddressType=etsysImageValidationIcmpAddressType, etsysImageValidationGroups=etsysImageValidationGroups, etsysImageValidationCompliance=etsysImageValidationCompliance)
