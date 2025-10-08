#
# PySNMP MIB module MX-EMERGENCY-CALL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/media5/MX-EMERGENCY-CALL-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:39:05 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
mediatrixConfig, = mibBuilder.importSymbols("MX-SMI", "mediatrixConfig")
MxEnableState, = mibBuilder.importSymbols("MX-TC", "MxEnableState")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
emergencyCallMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4935, 15, 75))
emergencyCallMIB.setRevisions(('1903-03-03 00:00',))
if mibBuilder.loadTexts: emergencyCallMIB.setLastUpdated('0303030000Z')
if mibBuilder.loadTexts: emergencyCallMIB.setOrganization('Mediatrix Telecom, Inc.')
emergencyCallMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 15, 75, 1))
emergencyCallConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 15, 75, 2))
emergencyCallUrgentGatewayCustomization = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 15, 75, 1, 5))
emergencyCallUrgentGatewayEnable = MibScalar((1, 3, 6, 1, 4, 1, 4935, 15, 75, 1, 5, 5), MxEnableState().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: emergencyCallUrgentGatewayEnable.setStatus('current')
emergencyCallUrgentGatewayDigitMap = MibScalar((1, 3, 6, 1, 4, 1, 4935, 15, 75, 1, 5, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: emergencyCallUrgentGatewayDigitMap.setStatus('current')
emergencyCallUrgentGatewayTargetAddress = MibScalar((1, 3, 6, 1, 4, 1, 4935, 15, 75, 1, 5, 15), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: emergencyCallUrgentGatewayTargetAddress.setStatus('current')
emergencyCallCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 15, 75, 2, 1))
emergencyCallComplVer1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4935, 15, 75, 2, 1, 1)).setObjects(("MX-EMERGENCY-CALL-MIB", "emergencyCallUrgentGatewayVer1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    emergencyCallComplVer1 = emergencyCallComplVer1.setStatus('current')
emergencyCallGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 15, 75, 2, 5))
emergencyCallUrgentGatewayVer1 = ObjectGroup((1, 3, 6, 1, 4, 1, 4935, 15, 75, 2, 5, 5)).setObjects(("MX-EMERGENCY-CALL-MIB", "emergencyCallUrgentGatewayEnable"), ("MX-EMERGENCY-CALL-MIB", "emergencyCallUrgentGatewayDigitMap"), ("MX-EMERGENCY-CALL-MIB", "emergencyCallUrgentGatewayTargetAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    emergencyCallUrgentGatewayVer1 = emergencyCallUrgentGatewayVer1.setStatus('current')
mibBuilder.exportSymbols("MX-EMERGENCY-CALL-MIB", emergencyCallUrgentGatewayCustomization=emergencyCallUrgentGatewayCustomization, emergencyCallMIB=emergencyCallMIB, emergencyCallUrgentGatewayTargetAddress=emergencyCallUrgentGatewayTargetAddress, emergencyCallUrgentGatewayEnable=emergencyCallUrgentGatewayEnable, emergencyCallCompliances=emergencyCallCompliances, emergencyCallUrgentGatewayVer1=emergencyCallUrgentGatewayVer1, emergencyCallComplVer1=emergencyCallComplVer1, PYSNMP_MODULE_ID=emergencyCallMIB, emergencyCallMIBObjects=emergencyCallMIBObjects, emergencyCallGroups=emergencyCallGroups, emergencyCallUrgentGatewayDigitMap=emergencyCallUrgentGatewayDigitMap, emergencyCallConformance=emergencyCallConformance)
