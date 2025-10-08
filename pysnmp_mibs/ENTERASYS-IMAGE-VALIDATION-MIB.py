#
# PySNMP MIB module ENTERASYS-IMAGE-VALIDATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/enterasys/ENTERASYS-IMAGE-VALIDATION-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:33:55 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ENTERASYS-IMAGE-VALIDATION-MIB", etsysImageValidationConfigGroup=etsysImageValidationConfigGroup, etsysImageValidationOperations=etsysImageValidationOperations, etsysImageValidationGroups=etsysImageValidationGroups, etsysImageValidationMIB=etsysImageValidationMIB, etsysImageValidationCompliance=etsysImageValidationCompliance, etsysImageValidationConfig=etsysImageValidationConfig, etsysImageValidationPeriod=etsysImageValidationPeriod, etsysImageValidationEnable=etsysImageValidationEnable, etsysImageValidationObjects=etsysImageValidationObjects, etsysImageValidationConformance=etsysImageValidationConformance, etsysImageValidationSnmpAddress=etsysImageValidationSnmpAddress, etsysImageValidationCompliances=etsysImageValidationCompliances, etsysImageValidationIcmpAddressType=etsysImageValidationIcmpAddressType, PYSNMP_MODULE_ID=etsysImageValidationMIB, etsysImageValidationIcmpAddress=etsysImageValidationIcmpAddress, etsysImageValidationSnmpAddressType=etsysImageValidationSnmpAddressType)
