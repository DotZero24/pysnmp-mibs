#
# PySNMP MIB module MX-EMERGENCY-CALL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/media5/MX-EMERGENCY-CALL-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:05:31 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
mediatrixConfig, = mibBuilder.importSymbols("MX-SMI", "mediatrixConfig")
MxEnableState, = mibBuilder.importSymbols("MX-TC", "MxEnableState")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("MX-EMERGENCY-CALL-MIB", emergencyCallUrgentGatewayTargetAddress=emergencyCallUrgentGatewayTargetAddress, emergencyCallCompliances=emergencyCallCompliances, emergencyCallUrgentGatewayDigitMap=emergencyCallUrgentGatewayDigitMap, emergencyCallUrgentGatewayVer1=emergencyCallUrgentGatewayVer1, emergencyCallConformance=emergencyCallConformance, PYSNMP_MODULE_ID=emergencyCallMIB, emergencyCallUrgentGatewayCustomization=emergencyCallUrgentGatewayCustomization, emergencyCallGroups=emergencyCallGroups, emergencyCallUrgentGatewayEnable=emergencyCallUrgentGatewayEnable, emergencyCallMIB=emergencyCallMIB, emergencyCallComplVer1=emergencyCallComplVer1, emergencyCallMIBObjects=emergencyCallMIBObjects)
