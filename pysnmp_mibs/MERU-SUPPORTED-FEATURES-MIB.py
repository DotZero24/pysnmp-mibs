#
# PySNMP MIB module MERU-SUPPORTED-FEATURES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/meru/MERU-SUPPORTED-FEATURES-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:08:31 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
Ipv6Address, = mibBuilder.importSymbols("IPV6-TC", "Ipv6Address")
mwConfiguration, = mibBuilder.importSymbols("MERU-SMI", "mwConfiguration")
MwlIpProxyType, MwlOnOffSwitch = mibBuilder.importSymbols("MERU-TC", "MwlIpProxyType", "MwlOnOffSwitch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
RowStatus, DateAndTime, TextualConvention, TimeInterval, MacAddress, TruthValue, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DateAndTime", "TextualConvention", "TimeInterval", "MacAddress", "TruthValue", "TimeStamp", "DisplayString")
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
mibBuilder.exportSymbols("MERU-SUPPORTED-FEATURES-MIB", mwSupportChannelDomainCheck=mwSupportChannelDomainCheck, mwSupportSipProxy=mwSupportSipProxy, mwSupportedFeatures=mwSupportedFeatures, PYSNMP_MODULE_ID=mwSupportedFeatures, mwSupport=mwSupport, mwSupportLicensingMgmt=mwSupportLicensingMgmt)
