#
# PySNMP MIB module BRCM-RG-FACTORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/broadcom/BRCM-RG-FACTORY-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:55 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
cableDataFactory, = mibBuilder.importSymbols("BRCM-CABLEDATA-FACTORY-MIB", "cableDataFactory")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("BRCM-RG-FACTORY-MIB", rgInitialMode=rgInitialMode, rgRipAuthEnabled=rgRipAuthEnabled, rgRipAuthKeyValue=rgRipAuthKeyValue, rgRipAuthKeyId=rgRipAuthKeyId, rgRipUnicastDestIpAddress=rgRipUnicastDestIpAddress, rgRipReportingInterval=rgRipReportingInterval, rgRipSubnetMask=rgRipSubnetMask, rgFactoryBase=rgFactoryBase, PYSNMP_MODULE_ID=residentialGatewayFactory, residentialGatewayFactory=residentialGatewayFactory)
