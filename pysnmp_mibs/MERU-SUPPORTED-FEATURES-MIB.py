#
# PySNMP MIB module MERU-SUPPORTED-FEATURES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/meru/MERU-SUPPORTED-FEATURES-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:41:27 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
Ipv6Address, = mibBuilder.importSymbols("IPV6-TC", "Ipv6Address")
mwConfiguration, = mibBuilder.importSymbols("MERU-SMI", "mwConfiguration")
MwlIpProxyType, MwlOnOffSwitch = mibBuilder.importSymbols("MERU-TC", "MwlIpProxyType", "MwlOnOffSwitch")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Integer32, enterprises, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, iso, MibIdentifier, Counter64, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "enterprises", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "iso", "MibIdentifier", "Counter64", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, TimeInterval, TimeStamp, RowStatus, DateAndTime, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TimeInterval", "TimeStamp", "RowStatus", "DateAndTime", "TruthValue", "TextualConvention")
mwSupportedFeatures = ModuleIdentity((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 14))
if mibBuilder.loadTexts: mwSupportedFeatures.setLastUpdated('200506050000Z')
if mibBuilder.loadTexts: mwSupportedFeatures.setOrganization('Meru Networks')
mwSupport = MibIdentifier((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 14, 1))
mwSupportChannelDomainCheck = MibScalar((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 14, 1, 1), MwlOnOffSwitch()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwSupportChannelDomainCheck.setStatus('current')
mwSupportLicensingMgmt = MibScalar((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 14, 1, 2), MwlOnOffSwitch()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwSupportLicensingMgmt.setStatus('current')
mwSupportSipProxy = MibScalar((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 14, 1, 3), MwlIpProxyType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwSupportSipProxy.setStatus('current')
mibBuilder.exportSymbols("MERU-SUPPORTED-FEATURES-MIB", mwSupportedFeatures=mwSupportedFeatures, PYSNMP_MODULE_ID=mwSupportedFeatures, mwSupportLicensingMgmt=mwSupportLicensingMgmt, mwSupportChannelDomainCheck=mwSupportChannelDomainCheck, mwSupport=mwSupport, mwSupportSipProxy=mwSupportSipProxy)
