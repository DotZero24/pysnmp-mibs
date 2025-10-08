#
# PySNMP MIB module BRCM-RG-FACTORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/broadcom/BRCM-RG-FACTORY-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:08:12 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
cableDataFactory, = mibBuilder.importSymbols("BRCM-CABLEDATA-FACTORY-MIB", "cableDataFactory")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
residentialGatewayFactory = ModuleIdentity((1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 7))
residentialGatewayFactory.setRevisions(('2007-02-05 00:00', '2003-01-30 00:00',))
if mibBuilder.loadTexts: residentialGatewayFactory.setLastUpdated('200702050000Z')
if mibBuilder.loadTexts: residentialGatewayFactory.setOrganization('Broadcom Corporation')
rgFactoryBase = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 7, 1))
rgInitialMode = MibScalar((1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 7, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("disabled", 1), ("residentialGateway", 2), ("cableHome10", 3), ("cableHome11", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rgInitialMode.setStatus('current')
rgRipAuthEnabled = MibScalar((1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 7, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rgRipAuthEnabled.setStatus('current')
rgRipAuthKeyValue = MibScalar((1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 7, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rgRipAuthKeyValue.setStatus('current')
rgRipAuthKeyId = MibScalar((1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 7, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rgRipAuthKeyId.setStatus('current')
rgRipReportingInterval = MibScalar((1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 7, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16535))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rgRipReportingInterval.setStatus('current')
rgRipUnicastDestIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 7, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rgRipUnicastDestIpAddress.setStatus('current')
rgRipSubnetMask = MibScalar((1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 7, 1, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rgRipSubnetMask.setStatus('current')
mibBuilder.exportSymbols("BRCM-RG-FACTORY-MIB", rgRipSubnetMask=rgRipSubnetMask, rgFactoryBase=rgFactoryBase, rgRipAuthKeyValue=rgRipAuthKeyValue, rgRipAuthKeyId=rgRipAuthKeyId, residentialGatewayFactory=residentialGatewayFactory, PYSNMP_MODULE_ID=residentialGatewayFactory, rgRipReportingInterval=rgRipReportingInterval, rgRipAuthEnabled=rgRipAuthEnabled, rgRipUnicastDestIpAddress=rgRipUnicastDestIpAddress, rgInitialMode=rgInitialMode)
