#
# PySNMP MIB module RUCKUS-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/ruckus/RUCKUS-TC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:41:37 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ruckusCommonTCModule, = mibBuilder.importSymbols("RUCKUS-ROOT-MIB", "ruckusCommonTCModule")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Integer32, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, TimeTicks, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Integer32", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "TimeTicks", "Bits", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ruckusTCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 25053, 1, 1, 1, 1))
if mibBuilder.loadTexts: ruckusTCMIB.setLastUpdated('201405191100Z')
if mibBuilder.loadTexts: ruckusTCMIB.setOrganization('Ruckus Wireless, Inc.')
class RuckusRadioMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("ieee802dot11b", 1), ("ieee802dot11g", 2), ("ieee802dot11Mixed", 3), ("ieee802dot11a", 4), ("ieee802dot11ng", 5), ("ieee802dot11na", 6), ("ieee802dot11ac", 7), ("ieee802dot11ax", 8))

class RuckusWEPKey(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(5, 5), ValueSizeConstraint(13, 13), ValueSizeConstraint(10, 10), ValueSizeConstraint(26, 26), )
class RuckusAdminStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enable", 1), ("disable", 2))

class RuckusCountryCode(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 2)
    fixedLength = 2

class RuckusFequency(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(2412, 5805)

class RuckusWPAPassPhrase(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(8, 63), ValueSizeConstraint(64, 64), )
class RuckusSSID(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 32)

class RuckusRate(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 126)

class RuckusdB(TextualConvention, Integer32):
    status = 'current'

class RuckusRateLimiting(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("disable", 0), ("rate100Kbps", 1), ("rate250Kbps", 2), ("rate500Kbps", 3), ("rate1Mbps", 4), ("rate2Mbps", 5), ("rate5Mbps", 6), ("rate10Mbps", 7), ("rate20Mbps", 8), ("rate50Mbps", 9))

class RuckusWLANServiceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("standardUsage", 1), ("guestAccess", 2), ("hotSpotService", 3))

class RuckusAuthenticationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("open", 1), ("shared", 2), ("eap", 3), ("mac-address", 4), ("eap-mac-mix", 5))

class RuckusEncryptionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("wpa", 1), ("wpa2", 2), ("wpa-Mixed", 3), ("wep-64", 4), ("wep-128", 5), ("none-enc", 6))

class RuckusWPACipherType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("tkip", 1), ("aes", 2), ("auto", 3), ("none", 4))

class RuckusWLANServicePriority(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("high", 1), ("low", 2))

class RuckusSysLogLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("more", 1), ("warning-and-critical", 2), ("critical-only", 3))

class RuckusSNMPv3AuthenticationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("md5", 1), ("sha", 2))

class RuckusSNMPv3EncryptionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("des", 1), ("aes", 2))

class RuckusSNMPVersionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("v2", 1), ("v3", 2))

class RuckusNameString(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 128)

class RuckusPassPhrase(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 64)

class RuckusAAAServiceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("active-directory", 1), ("ldap-directory", 2), ("aaa-authentication", 3), ("aaa-accounting", 4))

class RuckusAPIpAddressSettingMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("admin-by-zd", 1), ("admin-by-dhcp", 2), ("admin-by-ap", 3))

class RuckusAPRadioType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("ieee80211bg", 1), ("ieee80211na", 2), ("ieee80211a", 3), ("ieee80211n", 4))

class RuckusAPRadioType24(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("ieee80211b", 1), ("ieee80211g", 2), ("ieee80211bg", 3), ("ieee80211ng", 4))

class RuckusAPRadioType5(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ieee80211a", 1), ("ieee80211n", 2), ("ieee80211nag", 3))

class RuckusAPRadioTxPowerLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("auto", 1), ("full", 2), ("half-full", 3), ("quarter-full", 4), ("one-eighth-full", 5), ("one-tenth-full", 6))

class RuckusAPWirelessChannel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 11)

class RuckusAPMeshConfigurationMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("auto", 1), ("root-ap", 2), ("mesh-ap", 3), ("disabled", 4))

class RuckusAPUplinkSelectionMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("smart", 1), ("manual", 2))

class RuckusAPApproveMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("approved", 1), ("not-approved", 2))

class RuckusZDAPManagementAdminControl(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("delete", 1), ("associated", 2))

class RuckusSystemNodeStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 8))
    namedValues = NamedValues(("out-of-service", 0), ("in-service", 8))

class RuckusSystemClusterStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4))
    namedValues = NamedValues(("in-service", 0), ("out-of-service", 1), ("maintenance", 2), ("network-partition-suspected", 4))

class RuckusUUID(TextualConvention, OctetString):
    status = 'current'
    displayHint = '4x-2x-2x-2x-6x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

class RuckusMeshRoles(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("disable", 0), ("rap", 1), ("map", 2), ("emap", 3), ("mesh-is-down", 4), ("mesh-role-is-undefined", 5))

class RuckusUUIDType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("domain", 1), ("zone", 2), ("apgroup", 3))

class RuckusWLANAuthMethodType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("open", 1), ("wep-shared", 2), ("auto", 3), ("wpa-eap-802-1x", 4))

class RuckusWLANEncryptionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("open", 1), ("wep", 2), ("wpa", 3))

class RuckusChannelWidthType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(10, 20, 2040, 40, 80, 160))
    namedValues = NamedValues(("cw10", 10), ("cw20", 20), ("cw2040", 2040), ("cw40", 40), ("cw80", 80), ("cw160", 160))

class RuckusAuthStatusType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("unauthorized", 1), ("authorized", 2))

ruckusTCObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 1, 1, 1))
ruckusTCEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 1, 1, 2))
ruckusTCConf = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 1, 1, 3))
ruckusTCGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 1, 1, 3, 1))
ruckusTCCompls = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 1, 1, 3, 2))
mibBuilder.exportSymbols("RUCKUS-TC-MIB", RuckusRate=RuckusRate, RuckusPassPhrase=RuckusPassPhrase, RuckusAPRadioType24=RuckusAPRadioType24, RuckusAuthStatusType=RuckusAuthStatusType, RuckusAPIpAddressSettingMode=RuckusAPIpAddressSettingMode, ruckusTCConf=ruckusTCConf, ruckusTCGroups=ruckusTCGroups, RuckusAPWirelessChannel=RuckusAPWirelessChannel, RuckusNameString=RuckusNameString, RuckusAPApproveMode=RuckusAPApproveMode, RuckusSystemClusterStatus=RuckusSystemClusterStatus, RuckusAPRadioType=RuckusAPRadioType, ruckusTCMIB=ruckusTCMIB, RuckusWEPKey=RuckusWEPKey, RuckusCountryCode=RuckusCountryCode, RuckusSysLogLevel=RuckusSysLogLevel, RuckusAdminStatus=RuckusAdminStatus, RuckusFequency=RuckusFequency, RuckusWLANAuthMethodType=RuckusWLANAuthMethodType, RuckusdB=RuckusdB, RuckusWPAPassPhrase=RuckusWPAPassPhrase, RuckusWLANServiceType=RuckusWLANServiceType, RuckusAAAServiceType=RuckusAAAServiceType, RuckusWLANServicePriority=RuckusWLANServicePriority, RuckusAPUplinkSelectionMode=RuckusAPUplinkSelectionMode, RuckusAPMeshConfigurationMode=RuckusAPMeshConfigurationMode, RuckusSystemNodeStatus=RuckusSystemNodeStatus, RuckusUUIDType=RuckusUUIDType, RuckusAPRadioTxPowerLevel=RuckusAPRadioTxPowerLevel, RuckusWPACipherType=RuckusWPACipherType, RuckusUUID=RuckusUUID, RuckusZDAPManagementAdminControl=RuckusZDAPManagementAdminControl, RuckusMeshRoles=RuckusMeshRoles, RuckusAPRadioType5=RuckusAPRadioType5, RuckusSNMPv3EncryptionType=RuckusSNMPv3EncryptionType, PYSNMP_MODULE_ID=ruckusTCMIB, ruckusTCEvents=ruckusTCEvents, ruckusTCObjects=ruckusTCObjects, RuckusSSID=RuckusSSID, RuckusSNMPv3AuthenticationType=RuckusSNMPv3AuthenticationType, RuckusAuthenticationType=RuckusAuthenticationType, ruckusTCCompls=ruckusTCCompls, RuckusSNMPVersionType=RuckusSNMPVersionType, RuckusEncryptionType=RuckusEncryptionType, RuckusWLANEncryptionType=RuckusWLANEncryptionType, RuckusRadioMode=RuckusRadioMode, RuckusRateLimiting=RuckusRateLimiting, RuckusChannelWidthType=RuckusChannelWidthType)
