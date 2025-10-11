# SNMP MIB module (ENTERASYS-POLICY-PROFILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/enterasys/ENTERASYS-POLICY-PROFILE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:47:53 2025
# On host Robs-Air.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(StationAddress,
 StationAddressType) = mibBuilder.importSymbols(
    "ENTERASYS-UPN-TC-MIB",
    "StationAddress",
    "StationAddressType")

(ifAlias,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifAlias",
    "ifName")

(InetPortNumber,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetPortNumber")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(PortList,
 VlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 RowPointer,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")

(Uri,) = mibBuilder.importSymbols(
    "URI-TC-MIB",
    "Uri")


# MODULE-IDENTITY

etsysPolicyProfileMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6)
)
if mibBuilder.loadTexts:
    etsysPolicyProfileMIB.setRevisions(
        ("2016-04-18 18:21",
         "2015-01-09 15:57",
         "2014-03-04 12:24",
         "2014-02-27 12:50",
         "2014-01-15 16:24",
         "2013-11-13 15:49",
         "2013-11-07 14:05",
         "2013-03-05 16:51",
         "2013-03-04 15:09",
         "2013-03-01 12:27",
         "2013-02-14 14:12",
         "2013-01-22 16:27",
         "2012-06-13 16:34",
         "2012-02-07 17:01",
         "2010-08-09 15:11",
         "2009-04-10 12:00",
         "2009-04-01 13:36",
         "2008-02-19 14:29",
         "2007-03-21 21:02",
         "2006-06-15 20:40",
         "2005-05-18 20:08",
         "2005-03-28 15:35",
         "2005-03-14 21:34",
         "2004-08-11 15:17",
         "2004-05-18 17:02",
         "2004-04-02 20:35",
         "2004-03-25 18:03",
         "2004-02-03 22:00",
         "2004-02-03 15:33",
         "2004-01-19 21:43",
         "2003-11-04 17:16",
         "2003-02-06 22:59",
         "2002-09-17 14:53",
         "2002-07-19 13:37",
         "2001-06-11 20:00",
         "2001-01-09 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PolicyProfileIDTC(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )



class PortPolicyProfileIndexTypeTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ifIndex", 1),
          ("dot1dBasePort", 2))
    )



class PolicyRFC3580MapRadiusResponseTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("policyProfile", 1),
          ("vlanTunnelAttribute", 2),
          ("vlanTunnelAttributeWithPolicyProfile", 3))
    )



class VlanList(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512



class PolicyClassificationRuleType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("macSource", 1),
          ("macDestination", 2),
          ("ipxSource", 3),
          ("ipxDestination", 4),
          ("ipxSourcePort", 5),
          ("ipxDestinationPort", 6),
          ("ipxCos", 7),
          ("ipxType", 8),
          ("ip6Source", 9),
          ("ip6Destination", 10),
          ("ip6FlowLabel", 11),
          ("ip4Source", 12),
          ("ip4Destination", 13),
          ("ipFragment", 14),
          ("udpSourcePort", 15),
          ("udpDestinationPort", 16),
          ("tcpSourcePort", 17),
          ("tcpDestinationPort", 18),
          ("icmpTypeCode", 19),
          ("ipTtl", 20),
          ("ipTos", 21),
          ("ipType", 22),
          ("icmpTypeCodeV6", 23),
          ("etherType", 25),
          ("llcDsapSsap", 26),
          ("vlanId", 27),
          ("ieee8021dTci", 28),
          ("application", 29),
          ("acl", 30),
          ("bridgePort", 31))
    )



class PolicyRulesSupported(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("macSource", 1),
          ("macDestination", 2),
          ("ipxSource", 3),
          ("ipxDestination", 4),
          ("ipxSourcePort", 5),
          ("ipxDestinationPort", 6),
          ("ipxCos", 7),
          ("ipxType", 8),
          ("ip6Source", 9),
          ("ip6Destination", 10),
          ("ip6FlowLabel", 11),
          ("ip4Source", 12),
          ("ip4Destination", 13),
          ("ipFragment", 14),
          ("udpSourcePort", 15),
          ("udpDestinationPort", 16),
          ("tcpSourcePort", 17),
          ("tcpDestinationPort", 18),
          ("icmpTypeCode", 19),
          ("ipTtl", 20),
          ("ipTos", 21),
          ("ipType", 22),
          ("icmpTypeCodeV6", 23),
          ("etherType", 25),
          ("llcDsapSsap", 26),
          ("vlanId", 27),
          ("ieee8021dTci", 28),
          ("application", 29),
          ("acl", 30),
          ("bridgePort", 31))
    )


class TriStateStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("prohibited", 3))
    )



# MIB Managed Objects in the order of their OIDs

_EtsysPolicyNotifications_ObjectIdentity = ObjectIdentity
etsysPolicyNotifications = _EtsysPolicyNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 0)
)
_EtsysPolicyProfile_ObjectIdentity = ObjectIdentity
etsysPolicyProfile = _EtsysPolicyProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 1)
)


class _EtsysPolicyProfileMaxEntries_Type(Integer32):
    """Custom type etsysPolicyProfileMaxEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysPolicyProfileMaxEntries_Type.__name__ = "Integer32"
_EtsysPolicyProfileMaxEntries_Object = MibScalar
etsysPolicyProfileMaxEntries = _EtsysPolicyProfileMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 1, 1),
    _EtsysPolicyProfileMaxEntries_Type()
)
etsysPolicyProfileMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyProfileMaxEntries.setStatus("current")
_EtsysPolicyProfileNumEntries_Type = Gauge32
_EtsysPolicyProfileNumEntries_Object = MibScalar
etsysPolicyProfileNumEntries = _EtsysPolicyProfileNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 1, 2),
    _EtsysPolicyProfileNumEntries_Type()
)
etsysPolicyProfileNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyProfileNumEntries.setStatus("current")
_EtsysPolicyProfileLastChange_Type = TimeTicks
_EtsysPolicyProfileLastChange_Object = MibScalar
etsysPolicyProfileLastChange = _EtsysPolicyProfileLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 1, 3),
    _EtsysPolicyProfileLastChange_Type()
)
etsysPolicyProfileLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyProfileLastChange.setStatus("current")


class _EtsysPolicyProfileTableNextAvailableIndex_Type(Integer32):
    """Custom type etsysPolicyProfileTableNextAvailableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysPolicyProfileTableNextAvailableIndex_Type.__name__ = "Integer32"
_EtsysPolicyProfileTableNextAvailableIndex_Object = MibScalar
etsysPolicyProfileTableNextAvailableIndex = _EtsysPolicyProfileTableNextAvailableIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 1, 4),
    _EtsysPolicyProfileTableNextAvailableIndex_Type()
)
etsysPolicyProfileTableNextAvailableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyProfileTableNextAvailableIndex.setStatus("current")
_EtsysPolicyProfileTable_Object = MibTable
etsysPolicyProfileTable = _EtsysPolicyProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 1, 5)
)
if mibBuilder.loadTexts:
    etsysPolicyProfileTable.setStatus("current")
_EtsysPolicyProfileEntry_Object = MibTableRow
etsysPolicyProfileEntry = _EtsysPolicyProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 1, 5, 1)
)
etsysPolicyProfileEntry.setIndexNames(
    (0, "ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileIndex"),
)
if mibBuilder.loadTexts:
    etsysPolicyProfileEntry.setStatus("current")


class _EtsysPolicyProfileIndex_Type(Integer32):
    """Custom type etsysPolicyProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysPolicyProfileIndex_Type.__name__ = "Integer32"
_EtsysPolicyProfileIndex_Object = MibTableColumn
etsysPolicyProfileIndex = _EtsysPolicyProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 1, 5, 1, 1),
    _EtsysPolicyProfileIndex_Type()
)
etsysPolicyProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysPolicyProfileIndex.setStatus("current")


class _EtsysPolicyProfileName_Type(SnmpAdminString):
    """Custom type etsysPolicyProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EtsysPolicyProfileName_Type.__name__ = "SnmpAdminString"
_EtsysPolicyProfileName_Object = MibTableColumn
etsysPolicyProfileName = _EtsysPolicyProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 1, 5, 1, 2),
    _EtsysPolicyProfileName_Type()
)
etsysPolicyProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPolicyProfileName.setStatus("current")
_EtsysPolicyProfileRowStatus_Type = RowStatus
_EtsysPolicyProfileRowStatus_Object = MibTableColumn
etsysPolicyProfileRowStatus = _EtsysPolicyProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 1, 5, 1, 3),
    _EtsysPolicyProfileRowStatus_Type()
)
etsysPolicyProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPolicyProfileRowStatus.setStatus("current")


class _EtsysPolicyProfilePortVidStatus_Type(EnabledStatus):
    """Custom type etsysPolicyProfilePortVidStatus based on EnabledStatus"""
    defaultValue = 2


_EtsysPolicyProfilePortVidStatus_Type.__name__ = "EnabledStatus"
_EtsysPolicyProfilePortVidStatus_Object = MibTableColumn
etsysPolicyProfilePortVidStatus = _EtsysPolicyProfilePortVidStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 1, 5, 1, 4),
    _EtsysPolicyProfilePortVidStatus_Type()
)
etsysPolicyProfilePortVidStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPolicyProfilePortVidStatus.setStatus("current")


class _EtsysPolicyProfilePortVid_Type(Unsigned32):
    """Custom type etsysPolicyProfilePortVid based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(4095, 4095),
    )


_EtsysPolicyProfilePortVid_Type.__name__ = "Unsigned32"
_EtsysPolicyProfilePortVid_Object = MibTableColumn
etsysPolicyProfilePortVid = _EtsysPolicyProfilePortVid_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 1, 5, 1, 5),
    _EtsysPolicyProfilePortVid_Type()
)
etsysPolicyProfilePortVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPolicyProfilePortVid.setStatus("current")


class _EtsysPolicyProfilePriorityStatus_Type(EnabledStatus):
    """Custom type etsysPolicyProfilePriorityStatus based on EnabledStatus"""
    defaultValue = 2


_EtsysPolicyProfilePriorityStatus_Type.__name__ = "EnabledStatus"
_EtsysPolicyProfilePriorityStatus_Object = MibTableColumn
etsysPolicyProfilePriorityStatus = _EtsysPolicyProfilePriorityStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 1, 5, 1, 6),
    _EtsysPolicyProfilePriorityStatus_Type()
)
etsysPolicyProfilePriorityStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPolicyProfilePriorityStatus.setStatus("current")


class _EtsysPolicyProfilePriority_Type(Integer32):
    """Custom type etsysPolicyProfilePriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_EtsysPolicyProfilePriority_Type.__name__ = "Integer32"
_EtsysPolicyProfilePriority_Object = MibTableColumn
etsysPolicyProfilePriority = _EtsysPolicyProfilePriority_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 1, 5, 1, 7),
    _EtsysPolicyProfilePriority_Type()
)
etsysPolicyProfilePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPolicyProfilePriority.setStatus("current")
_EtsysPolicyProfileEgressVlans_Type = VlanList
_EtsysPolicyProfileEgressVlans_Object = MibTableColumn
etsysPolicyProfileEgressVlans = _EtsysPolicyProfileEgressVlans_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 1, 5, 1, 8),
    _EtsysPolicyProfileEgressVlans_Type()
)
etsysPolicyProfileEgressVlans.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPolicyProfileEgressVlans.setStatus("current")
_EtsysPolicyProfileForbiddenVlans_Type = VlanList
_EtsysPolicyProfileForbiddenVlans_Object = MibTableColumn
etsysPolicyProfileForbiddenVlans = _EtsysPolicyProfileForbiddenVlans_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 1, 5, 1, 9),
    _EtsysPolicyProfileForbiddenVlans_Type()
)
etsysPolicyProfileForbiddenVlans.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPolicyProfileForbiddenVlans.setStatus("current")
_EtsysPolicyProfileUntaggedVlans_Type = VlanList
_EtsysPolicyProfileUntaggedVlans_Object = MibTableColumn
etsysPolicyProfileUntaggedVlans = _EtsysPolicyProfileUntaggedVlans_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 1, 5, 1, 10),
    _EtsysPolicyProfileUntaggedVlans_Type()
)
etsysPolicyProfileUntaggedVlans.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPolicyProfileUntaggedVlans.setStatus("current")


class _EtsysPolicyProfileOverwriteTCI_Type(EnabledStatus):
    """Custom type etsysPolicyProfileOverwriteTCI based on EnabledStatus"""
    defaultValue = 2


_EtsysPolicyProfileOverwriteTCI_Type.__name__ = "EnabledStatus"
_EtsysPolicyProfileOverwriteTCI_Object = MibTableColumn
etsysPolicyProfileOverwriteTCI = _EtsysPolicyProfileOverwriteTCI_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 1, 5, 1, 11),
    _EtsysPolicyProfileOverwriteTCI_Type()
)
etsysPolicyProfileOverwriteTCI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPolicyProfileOverwriteTCI.setStatus("current")


class _EtsysPolicyProfileRulePrecedence_Type(OctetString):
    """Custom type etsysPolicyProfileRulePrecedence based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EtsysPolicyProfileRulePrecedence_Type.__name__ = "OctetString"
_EtsysPolicyProfileRulePrecedence_Object = MibTableColumn
etsysPolicyProfileRulePrecedence = _EtsysPolicyProfileRulePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 1, 5, 1, 12),
    _EtsysPolicyProfileRulePrecedence_Type()
)
etsysPolicyProfileRulePrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPolicyProfileRulePrecedence.setStatus("current")
_EtsysPolicyProfileVlanRFC3580Mappings_Type = VlanList
_EtsysPolicyProfileVlanRFC3580Mappings_Object = MibTableColumn
etsysPolicyProfileVlanRFC3580Mappings = _EtsysPolicyProfileVlanRFC3580Mappings_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 1, 5, 1, 13),
    _EtsysPolicyProfileVlanRFC3580Mappings_Type()
)
etsysPolicyProfileVlanRFC3580Mappings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyProfileVlanRFC3580Mappings.setStatus("current")


class _EtsysPolicyProfileMirrorIndex_Type(Integer32):
    """Custom type etsysPolicyProfileMirrorIndex based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_EtsysPolicyProfileMirrorIndex_Type.__name__ = "Integer32"
_EtsysPolicyProfileMirrorIndex_Object = MibTableColumn
etsysPolicyProfileMirrorIndex = _EtsysPolicyProfileMirrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 1, 5, 1, 14),
    _EtsysPolicyProfileMirrorIndex_Type()
)
etsysPolicyProfileMirrorIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPolicyProfileMirrorIndex.setStatus("current")


class _EtsysPolicyProfileAuditSyslogEnable_Type(EnabledStatus):
    """Custom type etsysPolicyProfileAuditSyslogEnable based on EnabledStatus"""
    defaultValue = 2


_EtsysPolicyProfileAuditSyslogEnable_Type.__name__ = "EnabledStatus"
_EtsysPolicyProfileAuditSyslogEnable_Object = MibTableColumn
etsysPolicyProfileAuditSyslogEnable = _EtsysPolicyProfileAuditSyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 1, 5, 1, 15),
    _EtsysPolicyProfileAuditSyslogEnable_Type()
)
etsysPolicyProfileAuditSyslogEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPolicyProfileAuditSyslogEnable.setStatus("current")


class _EtsysPolicyProfileAuditTrapEnable_Type(EnabledStatus):
    """Custom type etsysPolicyProfileAuditTrapEnable based on EnabledStatus"""
    defaultValue = 2


_EtsysPolicyProfileAuditTrapEnable_Type.__name__ = "EnabledStatus"
_EtsysPolicyProfileAuditTrapEnable_Object = MibTableColumn
etsysPolicyProfileAuditTrapEnable = _EtsysPolicyProfileAuditTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 1, 5, 1, 16),
    _EtsysPolicyProfileAuditTrapEnable_Type()
)
etsysPolicyProfileAuditTrapEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPolicyProfileAuditTrapEnable.setStatus("current")


class _EtsysPolicyProfileDisablePort_Type(EnabledStatus):
    """Custom type etsysPolicyProfileDisablePort based on EnabledStatus"""
    defaultValue = 2


_EtsysPolicyProfileDisablePort_Type.__name__ = "EnabledStatus"
_EtsysPolicyProfileDisablePort_Object = MibTableColumn
etsysPolicyProfileDisablePort = _EtsysPolicyProfileDisablePort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 1, 5, 1, 17),
    _EtsysPolicyProfileDisablePort_Type()
)
etsysPolicyProfileDisablePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPolicyProfileDisablePort.setStatus("current")
_EtsysPolicyProfileUsageList_Type = PortList
_EtsysPolicyProfileUsageList_Object = MibTableColumn
etsysPolicyProfileUsageList = _EtsysPolicyProfileUsageList_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 1, 5, 1, 18),
    _EtsysPolicyProfileUsageList_Type()
)
etsysPolicyProfileUsageList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPolicyProfileUsageList.setStatus("current")


class _EtsysPolicyProfileFstIndex_Type(Integer32):
    """Custom type etsysPolicyProfileFstIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_EtsysPolicyProfileFstIndex_Type.__name__ = "Integer32"
_EtsysPolicyProfileFstIndex_Object = MibTableColumn
etsysPolicyProfileFstIndex = _EtsysPolicyProfileFstIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 1, 5, 1, 19),
    _EtsysPolicyProfileFstIndex_Type()
)
etsysPolicyProfileFstIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPolicyProfileFstIndex.setStatus("current")


class _EtsysPolicyProfileHttpRedirectIndex_Type(Integer32):
    """Custom type etsysPolicyProfileHttpRedirectIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_EtsysPolicyProfileHttpRedirectIndex_Type.__name__ = "Integer32"
_EtsysPolicyProfileHttpRedirectIndex_Object = MibTableColumn
etsysPolicyProfileHttpRedirectIndex = _EtsysPolicyProfileHttpRedirectIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 1, 5, 1, 20),
    _EtsysPolicyProfileHttpRedirectIndex_Type()
)
etsysPolicyProfileHttpRedirectIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPolicyProfileHttpRedirectIndex.setStatus("current")


class _EtsysPolicyProfilePortAuthOverride_Type(EnabledStatus):
    """Custom type etsysPolicyProfilePortAuthOverride based on EnabledStatus"""
    defaultValue = 2


_EtsysPolicyProfilePortAuthOverride_Type.__name__ = "EnabledStatus"
_EtsysPolicyProfilePortAuthOverride_Object = MibTableColumn
etsysPolicyProfilePortAuthOverride = _EtsysPolicyProfilePortAuthOverride_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 1, 5, 1, 21),
    _EtsysPolicyProfilePortAuthOverride_Type()
)
etsysPolicyProfilePortAuthOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPolicyProfilePortAuthOverride.setStatus("current")
_EtsysPolicyClassification_ObjectIdentity = ObjectIdentity
etsysPolicyClassification = _EtsysPolicyClassification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 2)
)


class _EtsysPolicyClassificationMaxEntries_Type(Integer32):
    """Custom type etsysPolicyClassificationMaxEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysPolicyClassificationMaxEntries_Type.__name__ = "Integer32"
_EtsysPolicyClassificationMaxEntries_Object = MibScalar
etsysPolicyClassificationMaxEntries = _EtsysPolicyClassificationMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 2, 1),
    _EtsysPolicyClassificationMaxEntries_Type()
)
etsysPolicyClassificationMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyClassificationMaxEntries.setStatus("deprecated")
_EtsysPolicyClassificationNumEntries_Type = Gauge32
_EtsysPolicyClassificationNumEntries_Object = MibScalar
etsysPolicyClassificationNumEntries = _EtsysPolicyClassificationNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 2, 2),
    _EtsysPolicyClassificationNumEntries_Type()
)
etsysPolicyClassificationNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyClassificationNumEntries.setStatus("deprecated")
_EtsysPolicyClassificationLastChange_Type = TimeTicks
_EtsysPolicyClassificationLastChange_Object = MibScalar
etsysPolicyClassificationLastChange = _EtsysPolicyClassificationLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 2, 3),
    _EtsysPolicyClassificationLastChange_Type()
)
etsysPolicyClassificationLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyClassificationLastChange.setStatus("deprecated")
_EtsysPolicyClassificationTable_Object = MibTable
etsysPolicyClassificationTable = _EtsysPolicyClassificationTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 2, 4)
)
if mibBuilder.loadTexts:
    etsysPolicyClassificationTable.setStatus("deprecated")
_EtsysPolicyClassificationEntry_Object = MibTableRow
etsysPolicyClassificationEntry = _EtsysPolicyClassificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 2, 4, 1)
)
etsysPolicyClassificationEntry.setIndexNames(
    (0, "ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileIndex"),
    (0, "ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyClassificationIndex"),
)
if mibBuilder.loadTexts:
    etsysPolicyClassificationEntry.setStatus("deprecated")


class _EtsysPolicyClassificationIndex_Type(Integer32):
    """Custom type etsysPolicyClassificationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysPolicyClassificationIndex_Type.__name__ = "Integer32"
_EtsysPolicyClassificationIndex_Object = MibTableColumn
etsysPolicyClassificationIndex = _EtsysPolicyClassificationIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 2, 4, 1, 1),
    _EtsysPolicyClassificationIndex_Type()
)
etsysPolicyClassificationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysPolicyClassificationIndex.setStatus("deprecated")
_EtsysPolicyClassificationOID_Type = RowPointer
_EtsysPolicyClassificationOID_Object = MibTableColumn
etsysPolicyClassificationOID = _EtsysPolicyClassificationOID_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 2, 4, 1, 2),
    _EtsysPolicyClassificationOID_Type()
)
etsysPolicyClassificationOID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPolicyClassificationOID.setStatus("deprecated")
_EtsysPolicyClassificationRowStatus_Type = RowStatus
_EtsysPolicyClassificationRowStatus_Object = MibTableColumn
etsysPolicyClassificationRowStatus = _EtsysPolicyClassificationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 2, 4, 1, 3),
    _EtsysPolicyClassificationRowStatus_Type()
)
etsysPolicyClassificationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPolicyClassificationRowStatus.setStatus("deprecated")
_EtsysPolicyClassificationIngressList_Type = PortList
_EtsysPolicyClassificationIngressList_Object = MibTableColumn
etsysPolicyClassificationIngressList = _EtsysPolicyClassificationIngressList_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 2, 4, 1, 4),
    _EtsysPolicyClassificationIngressList_Type()
)
etsysPolicyClassificationIngressList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyClassificationIngressList.setStatus("deprecated")
_EtsysPortPolicyProfile_ObjectIdentity = ObjectIdentity
etsysPortPolicyProfile = _EtsysPortPolicyProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 3)
)
_EtsysPortPolicyProfileLastChange_Type = TimeTicks
_EtsysPortPolicyProfileLastChange_Object = MibScalar
etsysPortPolicyProfileLastChange = _EtsysPortPolicyProfileLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 3, 1),
    _EtsysPortPolicyProfileLastChange_Type()
)
etsysPortPolicyProfileLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPortPolicyProfileLastChange.setStatus("deprecated")
_EtsysPortPolicyProfileTable_Object = MibTable
etsysPortPolicyProfileTable = _EtsysPortPolicyProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 3, 2)
)
if mibBuilder.loadTexts:
    etsysPortPolicyProfileTable.setStatus("deprecated")
_EtsysPortPolicyProfileEntry_Object = MibTableRow
etsysPortPolicyProfileEntry = _EtsysPortPolicyProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 3, 2, 1)
)
etsysPortPolicyProfileEntry.setIndexNames(
    (0, "ENTERASYS-POLICY-PROFILE-MIB", "etsysPortPolicyProfileIndexType"),
    (0, "ENTERASYS-POLICY-PROFILE-MIB", "etsysPortPolicyProfileIndex"),
)
if mibBuilder.loadTexts:
    etsysPortPolicyProfileEntry.setStatus("deprecated")
_EtsysPortPolicyProfileIndexType_Type = PortPolicyProfileIndexTypeTC
_EtsysPortPolicyProfileIndexType_Object = MibTableColumn
etsysPortPolicyProfileIndexType = _EtsysPortPolicyProfileIndexType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 3, 2, 1, 1),
    _EtsysPortPolicyProfileIndexType_Type()
)
etsysPortPolicyProfileIndexType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysPortPolicyProfileIndexType.setStatus("deprecated")


class _EtsysPortPolicyProfileIndex_Type(Integer32):
    """Custom type etsysPortPolicyProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EtsysPortPolicyProfileIndex_Type.__name__ = "Integer32"
_EtsysPortPolicyProfileIndex_Object = MibTableColumn
etsysPortPolicyProfileIndex = _EtsysPortPolicyProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 3, 2, 1, 2),
    _EtsysPortPolicyProfileIndex_Type()
)
etsysPortPolicyProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysPortPolicyProfileIndex.setStatus("deprecated")


class _EtsysPortPolicyProfileAdminID_Type(PolicyProfileIDTC):
    """Custom type etsysPortPolicyProfileAdminID based on PolicyProfileIDTC"""
    defaultValue = 0


_EtsysPortPolicyProfileAdminID_Type.__name__ = "PolicyProfileIDTC"
_EtsysPortPolicyProfileAdminID_Object = MibTableColumn
etsysPortPolicyProfileAdminID = _EtsysPortPolicyProfileAdminID_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 3, 2, 1, 3),
    _EtsysPortPolicyProfileAdminID_Type()
)
etsysPortPolicyProfileAdminID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPortPolicyProfileAdminID.setStatus("deprecated")
_EtsysPortPolicyProfileOperID_Type = PolicyProfileIDTC
_EtsysPortPolicyProfileOperID_Object = MibTableColumn
etsysPortPolicyProfileOperID = _EtsysPortPolicyProfileOperID_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 3, 2, 1, 4),
    _EtsysPortPolicyProfileOperID_Type()
)
etsysPortPolicyProfileOperID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPortPolicyProfileOperID.setStatus("deprecated")
_EtsysPortPolicyProfileSummaryTable_Object = MibTable
etsysPortPolicyProfileSummaryTable = _EtsysPortPolicyProfileSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 3, 3)
)
if mibBuilder.loadTexts:
    etsysPortPolicyProfileSummaryTable.setStatus("current")
_EtsysPortPolicyProfileSummaryEntry_Object = MibTableRow
etsysPortPolicyProfileSummaryEntry = _EtsysPortPolicyProfileSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 3, 3, 1)
)
etsysPortPolicyProfileSummaryEntry.setIndexNames(
    (0, "ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileIndex"),
    (0, "ENTERASYS-POLICY-PROFILE-MIB", "etsysPortPolicyProfileSummaryIndexType"),
)
if mibBuilder.loadTexts:
    etsysPortPolicyProfileSummaryEntry.setStatus("current")
_EtsysPortPolicyProfileSummaryIndexType_Type = PortPolicyProfileIndexTypeTC
_EtsysPortPolicyProfileSummaryIndexType_Object = MibTableColumn
etsysPortPolicyProfileSummaryIndexType = _EtsysPortPolicyProfileSummaryIndexType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 3, 3, 1, 1),
    _EtsysPortPolicyProfileSummaryIndexType_Type()
)
etsysPortPolicyProfileSummaryIndexType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysPortPolicyProfileSummaryIndexType.setStatus("current")
_EtsysPortPolicyProfileSummaryAdminID_Type = PortList
_EtsysPortPolicyProfileSummaryAdminID_Object = MibTableColumn
etsysPortPolicyProfileSummaryAdminID = _EtsysPortPolicyProfileSummaryAdminID_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 3, 3, 1, 2),
    _EtsysPortPolicyProfileSummaryAdminID_Type()
)
etsysPortPolicyProfileSummaryAdminID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPortPolicyProfileSummaryAdminID.setStatus("current")
_EtsysPortPolicyProfileSummaryOperID_Type = PortList
_EtsysPortPolicyProfileSummaryOperID_Object = MibTableColumn
etsysPortPolicyProfileSummaryOperID = _EtsysPortPolicyProfileSummaryOperID_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 3, 3, 1, 3),
    _EtsysPortPolicyProfileSummaryOperID_Type()
)
etsysPortPolicyProfileSummaryOperID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPortPolicyProfileSummaryOperID.setStatus("current")
_EtsysPortPolicyProfileSummaryDynamicID_Type = PortList
_EtsysPortPolicyProfileSummaryDynamicID_Object = MibTableColumn
etsysPortPolicyProfileSummaryDynamicID = _EtsysPortPolicyProfileSummaryDynamicID_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 3, 3, 1, 4),
    _EtsysPortPolicyProfileSummaryDynamicID_Type()
)
etsysPortPolicyProfileSummaryDynamicID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPortPolicyProfileSummaryDynamicID.setStatus("current")
_EtsysPolicyVlanEgress_ObjectIdentity = ObjectIdentity
etsysPolicyVlanEgress = _EtsysPolicyVlanEgress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 4)
)
_EtsysStationPolicyProfile_ObjectIdentity = ObjectIdentity
etsysStationPolicyProfile = _EtsysStationPolicyProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 5)
)


class _EtsysStationPolicyProfileMaxEntries_Type(Integer32):
    """Custom type etsysStationPolicyProfileMaxEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysStationPolicyProfileMaxEntries_Type.__name__ = "Integer32"
_EtsysStationPolicyProfileMaxEntries_Object = MibScalar
etsysStationPolicyProfileMaxEntries = _EtsysStationPolicyProfileMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 5, 1),
    _EtsysStationPolicyProfileMaxEntries_Type()
)
etsysStationPolicyProfileMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStationPolicyProfileMaxEntries.setStatus("current")
_EtsysStationPolicyProfileNumEntries_Type = Gauge32
_EtsysStationPolicyProfileNumEntries_Object = MibScalar
etsysStationPolicyProfileNumEntries = _EtsysStationPolicyProfileNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 5, 2),
    _EtsysStationPolicyProfileNumEntries_Type()
)
etsysStationPolicyProfileNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStationPolicyProfileNumEntries.setStatus("current")
_EtsysStationPolicyProfileLastChange_Type = TimeTicks
_EtsysStationPolicyProfileLastChange_Object = MibScalar
etsysStationPolicyProfileLastChange = _EtsysStationPolicyProfileLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 5, 3),
    _EtsysStationPolicyProfileLastChange_Type()
)
etsysStationPolicyProfileLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStationPolicyProfileLastChange.setStatus("current")
_EtsysStationPolicyProfileTable_Object = MibTable
etsysStationPolicyProfileTable = _EtsysStationPolicyProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 5, 4)
)
if mibBuilder.loadTexts:
    etsysStationPolicyProfileTable.setStatus("current")
_EtsysStationPolicyProfileEntry_Object = MibTableRow
etsysStationPolicyProfileEntry = _EtsysStationPolicyProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 5, 4, 1)
)
etsysStationPolicyProfileEntry.setIndexNames(
    (0, "ENTERASYS-POLICY-PROFILE-MIB", "etsysStationPolicyProfileIndex"),
)
if mibBuilder.loadTexts:
    etsysStationPolicyProfileEntry.setStatus("current")


class _EtsysStationPolicyProfileIndex_Type(Integer32):
    """Custom type etsysStationPolicyProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EtsysStationPolicyProfileIndex_Type.__name__ = "Integer32"
_EtsysStationPolicyProfileIndex_Object = MibTableColumn
etsysStationPolicyProfileIndex = _EtsysStationPolicyProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 5, 4, 1, 2),
    _EtsysStationPolicyProfileIndex_Type()
)
etsysStationPolicyProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysStationPolicyProfileIndex.setStatus("current")
_EtsysStationIdentifierType_Type = StationAddressType
_EtsysStationIdentifierType_Object = MibTableColumn
etsysStationIdentifierType = _EtsysStationIdentifierType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 5, 4, 1, 3),
    _EtsysStationIdentifierType_Type()
)
etsysStationIdentifierType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStationIdentifierType.setStatus("current")
_EtsysStationIdentifier_Type = StationAddress
_EtsysStationIdentifier_Object = MibTableColumn
etsysStationIdentifier = _EtsysStationIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 5, 4, 1, 4),
    _EtsysStationIdentifier_Type()
)
etsysStationIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStationIdentifier.setStatus("current")
_EtsysStationPolicyProfileOperID_Type = PolicyProfileIDTC
_EtsysStationPolicyProfileOperID_Object = MibTableColumn
etsysStationPolicyProfileOperID = _EtsysStationPolicyProfileOperID_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 5, 4, 1, 5),
    _EtsysStationPolicyProfileOperID_Type()
)
etsysStationPolicyProfileOperID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStationPolicyProfileOperID.setStatus("current")
_EtsysStationPolicyProfilePortType_Type = PortPolicyProfileIndexTypeTC
_EtsysStationPolicyProfilePortType_Object = MibTableColumn
etsysStationPolicyProfilePortType = _EtsysStationPolicyProfilePortType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 5, 4, 1, 6),
    _EtsysStationPolicyProfilePortType_Type()
)
etsysStationPolicyProfilePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStationPolicyProfilePortType.setStatus("current")


class _EtsysStationPolicyProfilePortID_Type(Integer32):
    """Custom type etsysStationPolicyProfilePortID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EtsysStationPolicyProfilePortID_Type.__name__ = "Integer32"
_EtsysStationPolicyProfilePortID_Object = MibTableColumn
etsysStationPolicyProfilePortID = _EtsysStationPolicyProfilePortID_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 5, 4, 1, 7),
    _EtsysStationPolicyProfilePortID_Type()
)
etsysStationPolicyProfilePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStationPolicyProfilePortID.setStatus("current")
_EtsysInvalidPolicyPolicy_ObjectIdentity = ObjectIdentity
etsysInvalidPolicyPolicy = _EtsysInvalidPolicyPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 6)
)


class _EtsysInvalidPolicyAction_Type(Integer32):
    """Custom type etsysInvalidPolicyAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("applyDefaultPolicy", 1),
          ("dropPackets", 2),
          ("forwardPackets", 3))
    )


_EtsysInvalidPolicyAction_Type.__name__ = "Integer32"
_EtsysInvalidPolicyAction_Object = MibScalar
etsysInvalidPolicyAction = _EtsysInvalidPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 6, 1),
    _EtsysInvalidPolicyAction_Type()
)
etsysInvalidPolicyAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysInvalidPolicyAction.setStatus("current")
_EtsysInvalidPolicyCount_Type = Counter32
_EtsysInvalidPolicyCount_Object = MibScalar
etsysInvalidPolicyCount = _EtsysInvalidPolicyCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 6, 2),
    _EtsysInvalidPolicyCount_Type()
)
etsysInvalidPolicyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysInvalidPolicyCount.setStatus("current")
_EtsysPolicyProfileConformance_ObjectIdentity = ObjectIdentity
etsysPolicyProfileConformance = _EtsysPolicyProfileConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 7)
)
_EtsysPolicyProfileGroups_ObjectIdentity = ObjectIdentity
etsysPolicyProfileGroups = _EtsysPolicyProfileGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 7, 1)
)
_EtsysPolicyProfileCompliances_ObjectIdentity = ObjectIdentity
etsysPolicyProfileCompliances = _EtsysPolicyProfileCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 7, 2)
)
_EtsysDevicePolicyProfile_ObjectIdentity = ObjectIdentity
etsysDevicePolicyProfile = _EtsysDevicePolicyProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 8)
)


class _EtsysDevicePolicyProfileDefault_Type(Integer32):
    """Custom type etsysDevicePolicyProfileDefault based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_EtsysDevicePolicyProfileDefault_Type.__name__ = "Integer32"
_EtsysDevicePolicyProfileDefault_Object = MibScalar
etsysDevicePolicyProfileDefault = _EtsysDevicePolicyProfileDefault_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 8, 1),
    _EtsysDevicePolicyProfileDefault_Type()
)
etsysDevicePolicyProfileDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDevicePolicyProfileDefault.setStatus("current")
_EtsysPolicyCapability_ObjectIdentity = ObjectIdentity
etsysPolicyCapability = _EtsysPolicyCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 9)
)


class _EtsysPolicyCapabilities_Type(Bits):
    """Custom type etsysPolicyCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("supportsVLANForwarding", 0),
          ("supportsPriority", 1),
          ("supportsPermit", 2),
          ("supportsDeny", 3),
          ("supportsDeviceLevelPolicy", 4),
          ("supportsPrecedenceReordering", 5),
          ("supportsTciOverwrite", 6),
          ("supportsRulesTable", 7),
          ("supportsRuleUseAccounting", 8),
          ("supportsRuleUseNotification", 9),
          ("supportsCoSTable", 10),
          ("supportsLongestPrefixRules", 11),
          ("supportsPortDisableAction", 12),
          ("supportsRuleUseAutoClearOnLink", 13),
          ("supportsRuleUseAutoClearOnInterval", 14),
          ("supportsRuleUseAutoClearOnProfile", 15),
          ("supportsPolicyRFC3580MapTable", 16),
          ("supportsPolicyEnabledTable", 17),
          ("supportsMirror", 18),
          ("supportsEgressPolicy", 19),
          ("supportsProfileFst", 20),
          ("supportsQuarantine", 21),
          ("supportsProfileHttpRedirect", 22),
          ("supportsCounters", 23),
          ("supportsProfilePortAuthOverride", 24))
    )

_EtsysPolicyCapabilities_Type.__name__ = "Bits"
_EtsysPolicyCapabilities_Object = MibScalar
etsysPolicyCapabilities = _EtsysPolicyCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 9, 1),
    _EtsysPolicyCapabilities_Type()
)
etsysPolicyCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyCapabilities.setStatus("current")
_EtsysPolicyDynaPIDRuleCapabilities_Type = PolicyRulesSupported
_EtsysPolicyDynaPIDRuleCapabilities_Object = MibScalar
etsysPolicyDynaPIDRuleCapabilities = _EtsysPolicyDynaPIDRuleCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 9, 2),
    _EtsysPolicyDynaPIDRuleCapabilities_Type()
)
etsysPolicyDynaPIDRuleCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyDynaPIDRuleCapabilities.setStatus("current")
_EtsysPolicyAdminPIDRuleCapabilities_Type = PolicyRulesSupported
_EtsysPolicyAdminPIDRuleCapabilities_Object = MibScalar
etsysPolicyAdminPIDRuleCapabilities = _EtsysPolicyAdminPIDRuleCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 9, 3),
    _EtsysPolicyAdminPIDRuleCapabilities_Type()
)
etsysPolicyAdminPIDRuleCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyAdminPIDRuleCapabilities.setStatus("current")
_EtsysPolicyVlanRuleCapabilities_Type = PolicyRulesSupported
_EtsysPolicyVlanRuleCapabilities_Object = MibScalar
etsysPolicyVlanRuleCapabilities = _EtsysPolicyVlanRuleCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 9, 4),
    _EtsysPolicyVlanRuleCapabilities_Type()
)
etsysPolicyVlanRuleCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyVlanRuleCapabilities.setStatus("current")
_EtsysPolicyCosRuleCapabilities_Type = PolicyRulesSupported
_EtsysPolicyCosRuleCapabilities_Object = MibScalar
etsysPolicyCosRuleCapabilities = _EtsysPolicyCosRuleCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 9, 5),
    _EtsysPolicyCosRuleCapabilities_Type()
)
etsysPolicyCosRuleCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyCosRuleCapabilities.setStatus("current")
_EtsysPolicyDropRuleCapabilities_Type = PolicyRulesSupported
_EtsysPolicyDropRuleCapabilities_Object = MibScalar
etsysPolicyDropRuleCapabilities = _EtsysPolicyDropRuleCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 9, 6),
    _EtsysPolicyDropRuleCapabilities_Type()
)
etsysPolicyDropRuleCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyDropRuleCapabilities.setStatus("current")
_EtsysPolicyForwardRuleCapabilities_Type = PolicyRulesSupported
_EtsysPolicyForwardRuleCapabilities_Object = MibScalar
etsysPolicyForwardRuleCapabilities = _EtsysPolicyForwardRuleCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 9, 7),
    _EtsysPolicyForwardRuleCapabilities_Type()
)
etsysPolicyForwardRuleCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyForwardRuleCapabilities.setStatus("current")
_EtsysPolicySyslogRuleCapabilities_Type = PolicyRulesSupported
_EtsysPolicySyslogRuleCapabilities_Object = MibScalar
etsysPolicySyslogRuleCapabilities = _EtsysPolicySyslogRuleCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 9, 8),
    _EtsysPolicySyslogRuleCapabilities_Type()
)
etsysPolicySyslogRuleCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicySyslogRuleCapabilities.setStatus("current")
_EtsysPolicyTrapRuleCapabilities_Type = PolicyRulesSupported
_EtsysPolicyTrapRuleCapabilities_Object = MibScalar
etsysPolicyTrapRuleCapabilities = _EtsysPolicyTrapRuleCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 9, 9),
    _EtsysPolicyTrapRuleCapabilities_Type()
)
etsysPolicyTrapRuleCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyTrapRuleCapabilities.setStatus("current")
_EtsysPolicyDisablePortRuleCapabilities_Type = PolicyRulesSupported
_EtsysPolicyDisablePortRuleCapabilities_Object = MibScalar
etsysPolicyDisablePortRuleCapabilities = _EtsysPolicyDisablePortRuleCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 9, 10),
    _EtsysPolicyDisablePortRuleCapabilities_Type()
)
etsysPolicyDisablePortRuleCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyDisablePortRuleCapabilities.setStatus("current")
_EtsysPolicySupportedPortList_Type = PortList
_EtsysPolicySupportedPortList_Object = MibScalar
etsysPolicySupportedPortList = _EtsysPolicySupportedPortList_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 9, 11),
    _EtsysPolicySupportedPortList_Type()
)
etsysPolicySupportedPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicySupportedPortList.setStatus("current")
_EtsysPolicyEnabledTable_Object = MibTable
etsysPolicyEnabledTable = _EtsysPolicyEnabledTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 9, 12)
)
if mibBuilder.loadTexts:
    etsysPolicyEnabledTable.setStatus("current")
_EtsysPolicyEnabledTableEntry_Object = MibTableRow
etsysPolicyEnabledTableEntry = _EtsysPolicyEnabledTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 9, 12, 1)
)
etsysPolicyEnabledTableEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    etsysPolicyEnabledTableEntry.setStatus("current")
_EtsysPolicyEnabledSupportedRuleTypes_Type = PolicyRulesSupported
_EtsysPolicyEnabledSupportedRuleTypes_Object = MibTableColumn
etsysPolicyEnabledSupportedRuleTypes = _EtsysPolicyEnabledSupportedRuleTypes_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 9, 12, 1, 1),
    _EtsysPolicyEnabledSupportedRuleTypes_Type()
)
etsysPolicyEnabledSupportedRuleTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyEnabledSupportedRuleTypes.setStatus("current")
_EtsysPolicyEnabledEnabledRuleTypes_Type = PolicyRulesSupported
_EtsysPolicyEnabledEnabledRuleTypes_Object = MibTableColumn
etsysPolicyEnabledEnabledRuleTypes = _EtsysPolicyEnabledEnabledRuleTypes_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 9, 12, 1, 2),
    _EtsysPolicyEnabledEnabledRuleTypes_Type()
)
etsysPolicyEnabledEnabledRuleTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPolicyEnabledEnabledRuleTypes.setStatus("current")


class _EtsysPolicyEnabledEgressEnabled_Type(EnabledStatus):
    """Custom type etsysPolicyEnabledEgressEnabled based on EnabledStatus"""
    defaultValue = 2


_EtsysPolicyEnabledEgressEnabled_Type.__name__ = "EnabledStatus"
_EtsysPolicyEnabledEgressEnabled_Object = MibTableColumn
etsysPolicyEnabledEgressEnabled = _EtsysPolicyEnabledEgressEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 9, 12, 1, 3),
    _EtsysPolicyEnabledEgressEnabled_Type()
)
etsysPolicyEnabledEgressEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPolicyEnabledEgressEnabled.setStatus("current")
_EtsysPolicyRuleAttributeTable_Object = MibTable
etsysPolicyRuleAttributeTable = _EtsysPolicyRuleAttributeTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 9, 13)
)
if mibBuilder.loadTexts:
    etsysPolicyRuleAttributeTable.setStatus("current")
_EtsysPolicyRuleAttributeTableEntry_Object = MibTableRow
etsysPolicyRuleAttributeTableEntry = _EtsysPolicyRuleAttributeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 9, 13, 1)
)
etsysPolicyRuleAttributeTableEntry.setIndexNames(
    (0, "ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleType"),
)
if mibBuilder.loadTexts:
    etsysPolicyRuleAttributeTableEntry.setStatus("current")
_EtsysPolicyRuleAttributeByteLength_Type = Integer32
_EtsysPolicyRuleAttributeByteLength_Object = MibTableColumn
etsysPolicyRuleAttributeByteLength = _EtsysPolicyRuleAttributeByteLength_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 9, 13, 1, 1),
    _EtsysPolicyRuleAttributeByteLength_Type()
)
etsysPolicyRuleAttributeByteLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyRuleAttributeByteLength.setStatus("current")
_EtsysPolicyRuleAttributeBitLength_Type = Integer32
_EtsysPolicyRuleAttributeBitLength_Object = MibTableColumn
etsysPolicyRuleAttributeBitLength = _EtsysPolicyRuleAttributeBitLength_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 9, 13, 1, 2),
    _EtsysPolicyRuleAttributeBitLength_Type()
)
etsysPolicyRuleAttributeBitLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyRuleAttributeBitLength.setStatus("current")
_EtsysPolicyRuleAttributeMaxCreatable_Type = Integer32
_EtsysPolicyRuleAttributeMaxCreatable_Object = MibTableColumn
etsysPolicyRuleAttributeMaxCreatable = _EtsysPolicyRuleAttributeMaxCreatable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 9, 13, 1, 3),
    _EtsysPolicyRuleAttributeMaxCreatable_Type()
)
etsysPolicyRuleAttributeMaxCreatable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyRuleAttributeMaxCreatable.setStatus("current")
_EtsysPolicyRuleTciOverwriteCapabilities_Type = PolicyRulesSupported
_EtsysPolicyRuleTciOverwriteCapabilities_Object = MibScalar
etsysPolicyRuleTciOverwriteCapabilities = _EtsysPolicyRuleTciOverwriteCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 9, 14),
    _EtsysPolicyRuleTciOverwriteCapabilities_Type()
)
etsysPolicyRuleTciOverwriteCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyRuleTciOverwriteCapabilities.setStatus("current")
_EtsysPolicyRuleMirrorCapabilities_Type = PolicyRulesSupported
_EtsysPolicyRuleMirrorCapabilities_Object = MibScalar
etsysPolicyRuleMirrorCapabilities = _EtsysPolicyRuleMirrorCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 9, 15),
    _EtsysPolicyRuleMirrorCapabilities_Type()
)
etsysPolicyRuleMirrorCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyRuleMirrorCapabilities.setStatus("current")
_EtsysPolicyRuleQuarantineCapabilities_Type = PolicyRulesSupported
_EtsysPolicyRuleQuarantineCapabilities_Object = MibScalar
etsysPolicyRuleQuarantineCapabilities = _EtsysPolicyRuleQuarantineCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 9, 16),
    _EtsysPolicyRuleQuarantineCapabilities_Type()
)
etsysPolicyRuleQuarantineCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyRuleQuarantineCapabilities.setStatus("current")
_EtsysPolicyMap_ObjectIdentity = ObjectIdentity
etsysPolicyMap = _EtsysPolicyMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 10)
)


class _EtsysPolicyMapMaxEntries_Type(Integer32):
    """Custom type etsysPolicyMapMaxEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysPolicyMapMaxEntries_Type.__name__ = "Integer32"
_EtsysPolicyMapMaxEntries_Object = MibScalar
etsysPolicyMapMaxEntries = _EtsysPolicyMapMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 10, 1),
    _EtsysPolicyMapMaxEntries_Type()
)
etsysPolicyMapMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyMapMaxEntries.setStatus("obsolete")
_EtsysPolicyMapNumEntries_Type = Gauge32
_EtsysPolicyMapNumEntries_Object = MibScalar
etsysPolicyMapNumEntries = _EtsysPolicyMapNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 10, 2),
    _EtsysPolicyMapNumEntries_Type()
)
etsysPolicyMapNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyMapNumEntries.setStatus("obsolete")
_EtsysPolicyMapLastChange_Type = TimeTicks
_EtsysPolicyMapLastChange_Object = MibScalar
etsysPolicyMapLastChange = _EtsysPolicyMapLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 10, 3),
    _EtsysPolicyMapLastChange_Type()
)
etsysPolicyMapLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyMapLastChange.setStatus("obsolete")
_EtsysPolicyMapPvidOverRide_Type = TruthValue
_EtsysPolicyMapPvidOverRide_Object = MibScalar
etsysPolicyMapPvidOverRide = _EtsysPolicyMapPvidOverRide_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 10, 4),
    _EtsysPolicyMapPvidOverRide_Type()
)
etsysPolicyMapPvidOverRide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPolicyMapPvidOverRide.setStatus("obsolete")


class _EtsysPolicyMapUnknownPvidPolicy_Type(Integer32):
    """Custom type etsysPolicyMapUnknownPvidPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("denyAccess", 1),
          ("applyDefaultPolicy", 2),
          ("applyPvid", 3))
    )


_EtsysPolicyMapUnknownPvidPolicy_Type.__name__ = "Integer32"
_EtsysPolicyMapUnknownPvidPolicy_Object = MibScalar
etsysPolicyMapUnknownPvidPolicy = _EtsysPolicyMapUnknownPvidPolicy_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 10, 5),
    _EtsysPolicyMapUnknownPvidPolicy_Type()
)
etsysPolicyMapUnknownPvidPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPolicyMapUnknownPvidPolicy.setStatus("obsolete")
_EtsysPolicyMapTable_Object = MibTable
etsysPolicyMapTable = _EtsysPolicyMapTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 10, 6)
)
if mibBuilder.loadTexts:
    etsysPolicyMapTable.setStatus("obsolete")
_EtsysPolicyMapEntry_Object = MibTableRow
etsysPolicyMapEntry = _EtsysPolicyMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 10, 6, 1)
)
etsysPolicyMapEntry.setIndexNames(
    (0, "ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyMapIndex"),
)
if mibBuilder.loadTexts:
    etsysPolicyMapEntry.setStatus("obsolete")


class _EtsysPolicyMapIndex_Type(Integer32):
    """Custom type etsysPolicyMapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysPolicyMapIndex_Type.__name__ = "Integer32"
_EtsysPolicyMapIndex_Object = MibTableColumn
etsysPolicyMapIndex = _EtsysPolicyMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 10, 6, 1, 1),
    _EtsysPolicyMapIndex_Type()
)
etsysPolicyMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysPolicyMapIndex.setStatus("obsolete")
_EtsysPolicyMapRowStatus_Type = RowStatus
_EtsysPolicyMapRowStatus_Object = MibTableColumn
etsysPolicyMapRowStatus = _EtsysPolicyMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 10, 6, 1, 2),
    _EtsysPolicyMapRowStatus_Type()
)
etsysPolicyMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPolicyMapRowStatus.setStatus("obsolete")


class _EtsysPolicyMapStartVid_Type(Unsigned32):
    """Custom type etsysPolicyMapStartVid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EtsysPolicyMapStartVid_Type.__name__ = "Unsigned32"
_EtsysPolicyMapStartVid_Object = MibTableColumn
etsysPolicyMapStartVid = _EtsysPolicyMapStartVid_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 10, 6, 1, 3),
    _EtsysPolicyMapStartVid_Type()
)
etsysPolicyMapStartVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPolicyMapStartVid.setStatus("obsolete")


class _EtsysPolicyMapEndVid_Type(Unsigned32):
    """Custom type etsysPolicyMapEndVid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EtsysPolicyMapEndVid_Type.__name__ = "Unsigned32"
_EtsysPolicyMapEndVid_Object = MibTableColumn
etsysPolicyMapEndVid = _EtsysPolicyMapEndVid_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 10, 6, 1, 4),
    _EtsysPolicyMapEndVid_Type()
)
etsysPolicyMapEndVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPolicyMapEndVid.setStatus("obsolete")


class _EtsysPolicyMapPolicyIndex_Type(Integer32):
    """Custom type etsysPolicyMapPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EtsysPolicyMapPolicyIndex_Type.__name__ = "Integer32"
_EtsysPolicyMapPolicyIndex_Object = MibTableColumn
etsysPolicyMapPolicyIndex = _EtsysPolicyMapPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 10, 6, 1, 5),
    _EtsysPolicyMapPolicyIndex_Type()
)
etsysPolicyMapPolicyIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPolicyMapPolicyIndex.setStatus("obsolete")
_EtsysPolicyRules_ObjectIdentity = ObjectIdentity
etsysPolicyRules = _EtsysPolicyRules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11)
)


class _EtsysPolicyRulesMaxEntries_Type(Integer32):
    """Custom type etsysPolicyRulesMaxEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysPolicyRulesMaxEntries_Type.__name__ = "Integer32"
_EtsysPolicyRulesMaxEntries_Object = MibScalar
etsysPolicyRulesMaxEntries = _EtsysPolicyRulesMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 1),
    _EtsysPolicyRulesMaxEntries_Type()
)
etsysPolicyRulesMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyRulesMaxEntries.setStatus("current")
_EtsysPolicyRulesNumEntries_Type = Gauge32
_EtsysPolicyRulesNumEntries_Object = MibScalar
etsysPolicyRulesNumEntries = _EtsysPolicyRulesNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 2),
    _EtsysPolicyRulesNumEntries_Type()
)
etsysPolicyRulesNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyRulesNumEntries.setStatus("current")
_EtsysPolicyRulesLastChange_Type = TimeTicks
_EtsysPolicyRulesLastChange_Object = MibScalar
etsysPolicyRulesLastChange = _EtsysPolicyRulesLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 3),
    _EtsysPolicyRulesLastChange_Type()
)
etsysPolicyRulesLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyRulesLastChange.setStatus("current")


class _EtsysPolicyRulesAccountingEnable_Type(EnabledStatus):
    """Custom type etsysPolicyRulesAccountingEnable based on EnabledStatus"""
    defaultValue = 2


_EtsysPolicyRulesAccountingEnable_Type.__name__ = "EnabledStatus"
_EtsysPolicyRulesAccountingEnable_Object = MibScalar
etsysPolicyRulesAccountingEnable = _EtsysPolicyRulesAccountingEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 4),
    _EtsysPolicyRulesAccountingEnable_Type()
)
etsysPolicyRulesAccountingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPolicyRulesAccountingEnable.setStatus("current")
_EtsysPolicyRulesPortDisabledList_Type = PortList
_EtsysPolicyRulesPortDisabledList_Object = MibScalar
etsysPolicyRulesPortDisabledList = _EtsysPolicyRulesPortDisabledList_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 5),
    _EtsysPolicyRulesPortDisabledList_Type()
)
etsysPolicyRulesPortDisabledList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPolicyRulesPortDisabledList.setStatus("current")
_EtsysPolicyRuleTable_Object = MibTable
etsysPolicyRuleTable = _EtsysPolicyRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 6)
)
if mibBuilder.loadTexts:
    etsysPolicyRuleTable.setStatus("current")
_EtsysPolicyRuleEntry_Object = MibTableRow
etsysPolicyRuleEntry = _EtsysPolicyRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 6, 1)
)
etsysPolicyRuleEntry.setIndexNames(
    (0, "ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleProfileIndex"),
    (0, "ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleType"),
    (0, "ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleData"),
    (0, "ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulePrefixBits"),
    (0, "ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulePortType"),
    (0, "ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulePort"),
)
if mibBuilder.loadTexts:
    etsysPolicyRuleEntry.setStatus("current")


class _EtsysPolicyRuleProfileIndex_Type(Integer32):
    """Custom type etsysPolicyRuleProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_EtsysPolicyRuleProfileIndex_Type.__name__ = "Integer32"
_EtsysPolicyRuleProfileIndex_Object = MibTableColumn
etsysPolicyRuleProfileIndex = _EtsysPolicyRuleProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 6, 1, 1),
    _EtsysPolicyRuleProfileIndex_Type()
)
etsysPolicyRuleProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysPolicyRuleProfileIndex.setStatus("current")
_EtsysPolicyRuleType_Type = PolicyClassificationRuleType
_EtsysPolicyRuleType_Object = MibTableColumn
etsysPolicyRuleType = _EtsysPolicyRuleType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 6, 1, 2),
    _EtsysPolicyRuleType_Type()
)
etsysPolicyRuleType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysPolicyRuleType.setStatus("current")


class _EtsysPolicyRuleData_Type(OctetString):
    """Custom type etsysPolicyRuleData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EtsysPolicyRuleData_Type.__name__ = "OctetString"
_EtsysPolicyRuleData_Object = MibTableColumn
etsysPolicyRuleData = _EtsysPolicyRuleData_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 6, 1, 3),
    _EtsysPolicyRuleData_Type()
)
etsysPolicyRuleData.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysPolicyRuleData.setStatus("current")


class _EtsysPolicyRulePrefixBits_Type(Integer32):
    """Custom type etsysPolicyRulePrefixBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2048),
    )


_EtsysPolicyRulePrefixBits_Type.__name__ = "Integer32"
_EtsysPolicyRulePrefixBits_Object = MibTableColumn
etsysPolicyRulePrefixBits = _EtsysPolicyRulePrefixBits_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 6, 1, 4),
    _EtsysPolicyRulePrefixBits_Type()
)
etsysPolicyRulePrefixBits.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysPolicyRulePrefixBits.setStatus("current")
_EtsysPolicyRulePortType_Type = PortPolicyProfileIndexTypeTC
_EtsysPolicyRulePortType_Object = MibTableColumn
etsysPolicyRulePortType = _EtsysPolicyRulePortType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 6, 1, 5),
    _EtsysPolicyRulePortType_Type()
)
etsysPolicyRulePortType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysPolicyRulePortType.setStatus("current")


class _EtsysPolicyRulePort_Type(Integer32):
    """Custom type etsysPolicyRulePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_EtsysPolicyRulePort_Type.__name__ = "Integer32"
_EtsysPolicyRulePort_Object = MibTableColumn
etsysPolicyRulePort = _EtsysPolicyRulePort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 6, 1, 6),
    _EtsysPolicyRulePort_Type()
)
etsysPolicyRulePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysPolicyRulePort.setStatus("current")
_EtsysPolicyRuleRowStatus_Type = RowStatus
_EtsysPolicyRuleRowStatus_Object = MibTableColumn
etsysPolicyRuleRowStatus = _EtsysPolicyRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 6, 1, 7),
    _EtsysPolicyRuleRowStatus_Type()
)
etsysPolicyRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPolicyRuleRowStatus.setStatus("current")


class _EtsysPolicyRuleStorageType_Type(StorageType):
    """Custom type etsysPolicyRuleStorageType based on StorageType"""
    defaultValue = 3


_EtsysPolicyRuleStorageType_Type.__name__ = "StorageType"
_EtsysPolicyRuleStorageType_Object = MibTableColumn
etsysPolicyRuleStorageType = _EtsysPolicyRuleStorageType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 6, 1, 8),
    _EtsysPolicyRuleStorageType_Type()
)
etsysPolicyRuleStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPolicyRuleStorageType.setStatus("current")
_EtsysPolicyRuleUsageList_Type = PortList
_EtsysPolicyRuleUsageList_Object = MibTableColumn
etsysPolicyRuleUsageList = _EtsysPolicyRuleUsageList_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 6, 1, 9),
    _EtsysPolicyRuleUsageList_Type()
)
etsysPolicyRuleUsageList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPolicyRuleUsageList.setStatus("current")


class _EtsysPolicyRuleResult1_Type(Integer32):
    """Custom type etsysPolicyRuleResult1 based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(4095, 4095),
    )


_EtsysPolicyRuleResult1_Type.__name__ = "Integer32"
_EtsysPolicyRuleResult1_Object = MibTableColumn
etsysPolicyRuleResult1 = _EtsysPolicyRuleResult1_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 6, 1, 10),
    _EtsysPolicyRuleResult1_Type()
)
etsysPolicyRuleResult1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPolicyRuleResult1.setStatus("current")


class _EtsysPolicyRuleResult2_Type(Integer32):
    """Custom type etsysPolicyRuleResult2 based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 4095),
    )


_EtsysPolicyRuleResult2_Type.__name__ = "Integer32"
_EtsysPolicyRuleResult2_Object = MibTableColumn
etsysPolicyRuleResult2 = _EtsysPolicyRuleResult2_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 6, 1, 11),
    _EtsysPolicyRuleResult2_Type()
)
etsysPolicyRuleResult2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPolicyRuleResult2.setStatus("current")


class _EtsysPolicyRuleAuditSyslogEnable_Type(TriStateStatus):
    """Custom type etsysPolicyRuleAuditSyslogEnable based on TriStateStatus"""
    defaultValue = 2


_EtsysPolicyRuleAuditSyslogEnable_Type.__name__ = "TriStateStatus"
_EtsysPolicyRuleAuditSyslogEnable_Object = MibTableColumn
etsysPolicyRuleAuditSyslogEnable = _EtsysPolicyRuleAuditSyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 6, 1, 12),
    _EtsysPolicyRuleAuditSyslogEnable_Type()
)
etsysPolicyRuleAuditSyslogEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPolicyRuleAuditSyslogEnable.setStatus("current")


class _EtsysPolicyRuleAuditTrapEnable_Type(TriStateStatus):
    """Custom type etsysPolicyRuleAuditTrapEnable based on TriStateStatus"""
    defaultValue = 2


_EtsysPolicyRuleAuditTrapEnable_Type.__name__ = "TriStateStatus"
_EtsysPolicyRuleAuditTrapEnable_Object = MibTableColumn
etsysPolicyRuleAuditTrapEnable = _EtsysPolicyRuleAuditTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 6, 1, 13),
    _EtsysPolicyRuleAuditTrapEnable_Type()
)
etsysPolicyRuleAuditTrapEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPolicyRuleAuditTrapEnable.setStatus("current")


class _EtsysPolicyRuleDisablePort_Type(TriStateStatus):
    """Custom type etsysPolicyRuleDisablePort based on TriStateStatus"""
    defaultValue = 2


_EtsysPolicyRuleDisablePort_Type.__name__ = "TriStateStatus"
_EtsysPolicyRuleDisablePort_Object = MibTableColumn
etsysPolicyRuleDisablePort = _EtsysPolicyRuleDisablePort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 6, 1, 14),
    _EtsysPolicyRuleDisablePort_Type()
)
etsysPolicyRuleDisablePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPolicyRuleDisablePort.setStatus("current")


class _EtsysPolicyRuleOperPid_Type(Integer32):
    """Custom type etsysPolicyRuleOperPid based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 4095),
    )


_EtsysPolicyRuleOperPid_Type.__name__ = "Integer32"
_EtsysPolicyRuleOperPid_Object = MibTableColumn
etsysPolicyRuleOperPid = _EtsysPolicyRuleOperPid_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 6, 1, 15),
    _EtsysPolicyRuleOperPid_Type()
)
etsysPolicyRuleOperPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyRuleOperPid.setStatus("current")


class _EtsysPolicyRuleOverwriteTCI_Type(TriStateStatus):
    """Custom type etsysPolicyRuleOverwriteTCI based on TriStateStatus"""
    defaultValue = 2


_EtsysPolicyRuleOverwriteTCI_Type.__name__ = "TriStateStatus"
_EtsysPolicyRuleOverwriteTCI_Object = MibTableColumn
etsysPolicyRuleOverwriteTCI = _EtsysPolicyRuleOverwriteTCI_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 6, 1, 16),
    _EtsysPolicyRuleOverwriteTCI_Type()
)
etsysPolicyRuleOverwriteTCI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPolicyRuleOverwriteTCI.setStatus("current")


class _EtsysPolicyRuleMirrorIndex_Type(Integer32):
    """Custom type etsysPolicyRuleMirrorIndex based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_EtsysPolicyRuleMirrorIndex_Type.__name__ = "Integer32"
_EtsysPolicyRuleMirrorIndex_Object = MibTableColumn
etsysPolicyRuleMirrorIndex = _EtsysPolicyRuleMirrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 6, 1, 17),
    _EtsysPolicyRuleMirrorIndex_Type()
)
etsysPolicyRuleMirrorIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPolicyRuleMirrorIndex.setStatus("current")


class _EtsysPolicyRuleQuarantineProfileIndex_Type(Integer32):
    """Custom type etsysPolicyRuleQuarantineProfileIndex based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_EtsysPolicyRuleQuarantineProfileIndex_Type.__name__ = "Integer32"
_EtsysPolicyRuleQuarantineProfileIndex_Object = MibTableColumn
etsysPolicyRuleQuarantineProfileIndex = _EtsysPolicyRuleQuarantineProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 6, 1, 18),
    _EtsysPolicyRuleQuarantineProfileIndex_Type()
)
etsysPolicyRuleQuarantineProfileIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPolicyRuleQuarantineProfileIndex.setStatus("current")


class _EtsysPolicyRuleHttpRedirectIndex_Type(Integer32):
    """Custom type etsysPolicyRuleHttpRedirectIndex based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_EtsysPolicyRuleHttpRedirectIndex_Type.__name__ = "Integer32"
_EtsysPolicyRuleHttpRedirectIndex_Object = MibTableColumn
etsysPolicyRuleHttpRedirectIndex = _EtsysPolicyRuleHttpRedirectIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 6, 1, 19),
    _EtsysPolicyRuleHttpRedirectIndex_Type()
)
etsysPolicyRuleHttpRedirectIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPolicyRuleHttpRedirectIndex.setStatus("current")
_EtsysPolicyRulePortTable_Object = MibTable
etsysPolicyRulePortTable = _EtsysPolicyRulePortTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 7)
)
if mibBuilder.loadTexts:
    etsysPolicyRulePortTable.setStatus("current")
_EtsysPolicyRulePortEntry_Object = MibTableRow
etsysPolicyRulePortEntry = _EtsysPolicyRulePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 7, 1)
)
etsysPolicyRulePortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleProfileIndex"),
    (0, "ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleType"),
    (0, "ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleData"),
    (0, "ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulePrefixBits"),
    (0, "ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulePortType"),
    (0, "ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulePort"),
)
if mibBuilder.loadTexts:
    etsysPolicyRulePortEntry.setStatus("current")
_EtsysPolicyRulePortHit_Type = TruthValue
_EtsysPolicyRulePortHit_Object = MibTableColumn
etsysPolicyRulePortHit = _EtsysPolicyRulePortHit_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 7, 1, 1),
    _EtsysPolicyRulePortHit_Type()
)
etsysPolicyRulePortHit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPolicyRulePortHit.setStatus("current")


class _EtsysPolicyRuleDynamicProfileAssignmentOverride_Type(TruthValue):
    """Custom type etsysPolicyRuleDynamicProfileAssignmentOverride based on TruthValue"""
    defaultValue = 2


_EtsysPolicyRuleDynamicProfileAssignmentOverride_Type.__name__ = "TruthValue"
_EtsysPolicyRuleDynamicProfileAssignmentOverride_Object = MibScalar
etsysPolicyRuleDynamicProfileAssignmentOverride = _EtsysPolicyRuleDynamicProfileAssignmentOverride_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 8),
    _EtsysPolicyRuleDynamicProfileAssignmentOverride_Type()
)
etsysPolicyRuleDynamicProfileAssignmentOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPolicyRuleDynamicProfileAssignmentOverride.setStatus("current")


class _EtsysPolicyRuleDefaultDynamicSyslogStatus_Type(TriStateStatus):
    """Custom type etsysPolicyRuleDefaultDynamicSyslogStatus based on TriStateStatus"""
    defaultValue = 2


_EtsysPolicyRuleDefaultDynamicSyslogStatus_Type.__name__ = "TriStateStatus"
_EtsysPolicyRuleDefaultDynamicSyslogStatus_Object = MibScalar
etsysPolicyRuleDefaultDynamicSyslogStatus = _EtsysPolicyRuleDefaultDynamicSyslogStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 9),
    _EtsysPolicyRuleDefaultDynamicSyslogStatus_Type()
)
etsysPolicyRuleDefaultDynamicSyslogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPolicyRuleDefaultDynamicSyslogStatus.setStatus("current")


class _EtsysPolicyRuleDefaultDynamicTrapStatus_Type(TriStateStatus):
    """Custom type etsysPolicyRuleDefaultDynamicTrapStatus based on TriStateStatus"""
    defaultValue = 2


_EtsysPolicyRuleDefaultDynamicTrapStatus_Type.__name__ = "TriStateStatus"
_EtsysPolicyRuleDefaultDynamicTrapStatus_Object = MibScalar
etsysPolicyRuleDefaultDynamicTrapStatus = _EtsysPolicyRuleDefaultDynamicTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 10),
    _EtsysPolicyRuleDefaultDynamicTrapStatus_Type()
)
etsysPolicyRuleDefaultDynamicTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPolicyRuleDefaultDynamicTrapStatus.setStatus("current")


class _EtsysPolicyRuleStatsAutoClearOnLink_Type(EnabledStatus):
    """Custom type etsysPolicyRuleStatsAutoClearOnLink based on EnabledStatus"""
    defaultValue = 2


_EtsysPolicyRuleStatsAutoClearOnLink_Type.__name__ = "EnabledStatus"
_EtsysPolicyRuleStatsAutoClearOnLink_Object = MibScalar
etsysPolicyRuleStatsAutoClearOnLink = _EtsysPolicyRuleStatsAutoClearOnLink_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 11),
    _EtsysPolicyRuleStatsAutoClearOnLink_Type()
)
etsysPolicyRuleStatsAutoClearOnLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPolicyRuleStatsAutoClearOnLink.setStatus("current")


class _EtsysPolicyRuleStatsAutoClearInterval_Type(Integer32):
    """Custom type etsysPolicyRuleStatsAutoClearInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_EtsysPolicyRuleStatsAutoClearInterval_Type.__name__ = "Integer32"
_EtsysPolicyRuleStatsAutoClearInterval_Object = MibScalar
etsysPolicyRuleStatsAutoClearInterval = _EtsysPolicyRuleStatsAutoClearInterval_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 12),
    _EtsysPolicyRuleStatsAutoClearInterval_Type()
)
etsysPolicyRuleStatsAutoClearInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPolicyRuleStatsAutoClearInterval.setStatus("current")
_EtsysPolicyRuleStatsAutoClearPorts_Type = PortList
_EtsysPolicyRuleStatsAutoClearPorts_Object = MibScalar
etsysPolicyRuleStatsAutoClearPorts = _EtsysPolicyRuleStatsAutoClearPorts_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 13),
    _EtsysPolicyRuleStatsAutoClearPorts_Type()
)
etsysPolicyRuleStatsAutoClearPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPolicyRuleStatsAutoClearPorts.setStatus("current")


class _EtsysPolicyRuleStatsAutoClearOnProfile_Type(EnabledStatus):
    """Custom type etsysPolicyRuleStatsAutoClearOnProfile based on EnabledStatus"""
    defaultValue = 2


_EtsysPolicyRuleStatsAutoClearOnProfile_Type.__name__ = "EnabledStatus"
_EtsysPolicyRuleStatsAutoClearOnProfile_Object = MibScalar
etsysPolicyRuleStatsAutoClearOnProfile = _EtsysPolicyRuleStatsAutoClearOnProfile_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 14),
    _EtsysPolicyRuleStatsAutoClearOnProfile_Type()
)
etsysPolicyRuleStatsAutoClearOnProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPolicyRuleStatsAutoClearOnProfile.setStatus("current")
_EtsysPolicyRuleStatsDroppedNotifications_Type = Integer32
_EtsysPolicyRuleStatsDroppedNotifications_Object = MibScalar
etsysPolicyRuleStatsDroppedNotifications = _EtsysPolicyRuleStatsDroppedNotifications_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 15),
    _EtsysPolicyRuleStatsDroppedNotifications_Type()
)
etsysPolicyRuleStatsDroppedNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyRuleStatsDroppedNotifications.setStatus("current")


class _EtsysPolicyRuleSylogMachineReadableFormat_Type(EnabledStatus):
    """Custom type etsysPolicyRuleSylogMachineReadableFormat based on EnabledStatus"""
    defaultValue = 2


_EtsysPolicyRuleSylogMachineReadableFormat_Type.__name__ = "EnabledStatus"
_EtsysPolicyRuleSylogMachineReadableFormat_Object = MibScalar
etsysPolicyRuleSylogMachineReadableFormat = _EtsysPolicyRuleSylogMachineReadableFormat_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 16),
    _EtsysPolicyRuleSylogMachineReadableFormat_Type()
)
etsysPolicyRuleSylogMachineReadableFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPolicyRuleSylogMachineReadableFormat.setStatus("current")


class _EtsysPolicyRuleSylogExtendedFormat_Type(EnabledStatus):
    """Custom type etsysPolicyRuleSylogExtendedFormat based on EnabledStatus"""
    defaultValue = 2


_EtsysPolicyRuleSylogExtendedFormat_Type.__name__ = "EnabledStatus"
_EtsysPolicyRuleSylogExtendedFormat_Object = MibScalar
etsysPolicyRuleSylogExtendedFormat = _EtsysPolicyRuleSylogExtendedFormat_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 17),
    _EtsysPolicyRuleSylogExtendedFormat_Type()
)
etsysPolicyRuleSylogExtendedFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPolicyRuleSylogExtendedFormat.setStatus("current")


class _EtsysPolicyRuleSylogEveryTime_Type(EnabledStatus):
    """Custom type etsysPolicyRuleSylogEveryTime based on EnabledStatus"""
    defaultValue = 2


_EtsysPolicyRuleSylogEveryTime_Type.__name__ = "EnabledStatus"
_EtsysPolicyRuleSylogEveryTime_Object = MibScalar
etsysPolicyRuleSylogEveryTime = _EtsysPolicyRuleSylogEveryTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 18),
    _EtsysPolicyRuleSylogEveryTime_Type()
)
etsysPolicyRuleSylogEveryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPolicyRuleSylogEveryTime.setStatus("current")
_EtsysPolicyNonVolatileRulesLastChange_Type = TimeTicks
_EtsysPolicyNonVolatileRulesLastChange_Object = MibScalar
etsysPolicyNonVolatileRulesLastChange = _EtsysPolicyNonVolatileRulesLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 19),
    _EtsysPolicyNonVolatileRulesLastChange_Type()
)
etsysPolicyNonVolatileRulesLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyNonVolatileRulesLastChange.setStatus("current")
_EtsysPolicyNonVolatileRuleTable_Object = MibTable
etsysPolicyNonVolatileRuleTable = _EtsysPolicyNonVolatileRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 20)
)
if mibBuilder.loadTexts:
    etsysPolicyNonVolatileRuleTable.setStatus("current")
_EtsysPolicyNonVolatileRuleEntry_Object = MibTableRow
etsysPolicyNonVolatileRuleEntry = _EtsysPolicyNonVolatileRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 20, 1)
)
etsysPolicyNonVolatileRuleEntry.setIndexNames(
    (0, "ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleProfileIndex"),
    (0, "ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleType"),
    (0, "ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleData"),
    (0, "ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulePrefixBits"),
    (0, "ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulePortType"),
    (0, "ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulePort"),
)
if mibBuilder.loadTexts:
    etsysPolicyNonVolatileRuleEntry.setStatus("current")
_EtsysPolicyNonVolatileRuleRowStatus_Type = RowStatus
_EtsysPolicyNonVolatileRuleRowStatus_Object = MibTableColumn
etsysPolicyNonVolatileRuleRowStatus = _EtsysPolicyNonVolatileRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 20, 1, 7),
    _EtsysPolicyNonVolatileRuleRowStatus_Type()
)
etsysPolicyNonVolatileRuleRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyNonVolatileRuleRowStatus.setStatus("current")
_EtsysPolicyNonVolatileRuleStorageType_Type = StorageType
_EtsysPolicyNonVolatileRuleStorageType_Object = MibTableColumn
etsysPolicyNonVolatileRuleStorageType = _EtsysPolicyNonVolatileRuleStorageType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 20, 1, 8),
    _EtsysPolicyNonVolatileRuleStorageType_Type()
)
etsysPolicyNonVolatileRuleStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyNonVolatileRuleStorageType.setStatus("current")
_EtsysPolicyNonVolatileRuleUsageList_Type = PortList
_EtsysPolicyNonVolatileRuleUsageList_Object = MibTableColumn
etsysPolicyNonVolatileRuleUsageList = _EtsysPolicyNonVolatileRuleUsageList_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 20, 1, 9),
    _EtsysPolicyNonVolatileRuleUsageList_Type()
)
etsysPolicyNonVolatileRuleUsageList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyNonVolatileRuleUsageList.setStatus("current")


class _EtsysPolicyNonVolatileRuleResult1_Type(Integer32):
    """Custom type etsysPolicyNonVolatileRuleResult1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(4095, 4095),
    )


_EtsysPolicyNonVolatileRuleResult1_Type.__name__ = "Integer32"
_EtsysPolicyNonVolatileRuleResult1_Object = MibTableColumn
etsysPolicyNonVolatileRuleResult1 = _EtsysPolicyNonVolatileRuleResult1_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 20, 1, 10),
    _EtsysPolicyNonVolatileRuleResult1_Type()
)
etsysPolicyNonVolatileRuleResult1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyNonVolatileRuleResult1.setStatus("current")


class _EtsysPolicyNonVolatileRuleResult2_Type(Integer32):
    """Custom type etsysPolicyNonVolatileRuleResult2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 4095),
    )


_EtsysPolicyNonVolatileRuleResult2_Type.__name__ = "Integer32"
_EtsysPolicyNonVolatileRuleResult2_Object = MibTableColumn
etsysPolicyNonVolatileRuleResult2 = _EtsysPolicyNonVolatileRuleResult2_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 20, 1, 11),
    _EtsysPolicyNonVolatileRuleResult2_Type()
)
etsysPolicyNonVolatileRuleResult2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyNonVolatileRuleResult2.setStatus("current")
_EtsysPolicyNonVolatileRuleAuditSyslogEnable_Type = TriStateStatus
_EtsysPolicyNonVolatileRuleAuditSyslogEnable_Object = MibTableColumn
etsysPolicyNonVolatileRuleAuditSyslogEnable = _EtsysPolicyNonVolatileRuleAuditSyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 20, 1, 12),
    _EtsysPolicyNonVolatileRuleAuditSyslogEnable_Type()
)
etsysPolicyNonVolatileRuleAuditSyslogEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyNonVolatileRuleAuditSyslogEnable.setStatus("current")
_EtsysPolicyNonVolatileRuleAuditTrapEnable_Type = TriStateStatus
_EtsysPolicyNonVolatileRuleAuditTrapEnable_Object = MibTableColumn
etsysPolicyNonVolatileRuleAuditTrapEnable = _EtsysPolicyNonVolatileRuleAuditTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 20, 1, 13),
    _EtsysPolicyNonVolatileRuleAuditTrapEnable_Type()
)
etsysPolicyNonVolatileRuleAuditTrapEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyNonVolatileRuleAuditTrapEnable.setStatus("current")
_EtsysPolicyNonVolatileRuleDisablePort_Type = TriStateStatus
_EtsysPolicyNonVolatileRuleDisablePort_Object = MibTableColumn
etsysPolicyNonVolatileRuleDisablePort = _EtsysPolicyNonVolatileRuleDisablePort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 20, 1, 14),
    _EtsysPolicyNonVolatileRuleDisablePort_Type()
)
etsysPolicyNonVolatileRuleDisablePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyNonVolatileRuleDisablePort.setStatus("current")


class _EtsysPolicyNonVolatileRuleOperPid_Type(Integer32):
    """Custom type etsysPolicyNonVolatileRuleOperPid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 4095),
    )


_EtsysPolicyNonVolatileRuleOperPid_Type.__name__ = "Integer32"
_EtsysPolicyNonVolatileRuleOperPid_Object = MibTableColumn
etsysPolicyNonVolatileRuleOperPid = _EtsysPolicyNonVolatileRuleOperPid_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 20, 1, 15),
    _EtsysPolicyNonVolatileRuleOperPid_Type()
)
etsysPolicyNonVolatileRuleOperPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyNonVolatileRuleOperPid.setStatus("current")
_EtsysPolicyNonVolatileRuleOverwriteTCI_Type = TriStateStatus
_EtsysPolicyNonVolatileRuleOverwriteTCI_Object = MibTableColumn
etsysPolicyNonVolatileRuleOverwriteTCI = _EtsysPolicyNonVolatileRuleOverwriteTCI_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 20, 1, 16),
    _EtsysPolicyNonVolatileRuleOverwriteTCI_Type()
)
etsysPolicyNonVolatileRuleOverwriteTCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyNonVolatileRuleOverwriteTCI.setStatus("current")


class _EtsysPolicyNonVolatileRuleMirrorIndex_Type(Integer32):
    """Custom type etsysPolicyNonVolatileRuleMirrorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_EtsysPolicyNonVolatileRuleMirrorIndex_Type.__name__ = "Integer32"
_EtsysPolicyNonVolatileRuleMirrorIndex_Object = MibTableColumn
etsysPolicyNonVolatileRuleMirrorIndex = _EtsysPolicyNonVolatileRuleMirrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 20, 1, 17),
    _EtsysPolicyNonVolatileRuleMirrorIndex_Type()
)
etsysPolicyNonVolatileRuleMirrorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyNonVolatileRuleMirrorIndex.setStatus("current")


class _EtsysPolicyNonVolatileRuleQuarantineProfileIndex_Type(Integer32):
    """Custom type etsysPolicyNonVolatileRuleQuarantineProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_EtsysPolicyNonVolatileRuleQuarantineProfileIndex_Type.__name__ = "Integer32"
_EtsysPolicyNonVolatileRuleQuarantineProfileIndex_Object = MibTableColumn
etsysPolicyNonVolatileRuleQuarantineProfileIndex = _EtsysPolicyNonVolatileRuleQuarantineProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 11, 20, 1, 18),
    _EtsysPolicyNonVolatileRuleQuarantineProfileIndex_Type()
)
etsysPolicyNonVolatileRuleQuarantineProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyNonVolatileRuleQuarantineProfileIndex.setStatus("current")
_EtsysPolicyRFC3580Map_ObjectIdentity = ObjectIdentity
etsysPolicyRFC3580Map = _EtsysPolicyRFC3580Map_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 12)
)


class _EtsysPolicyRFC3580MapResolveReponseConflict_Type(PolicyRFC3580MapRadiusResponseTC):
    """Custom type etsysPolicyRFC3580MapResolveReponseConflict based on PolicyRFC3580MapRadiusResponseTC"""
    defaultValue = 1


_EtsysPolicyRFC3580MapResolveReponseConflict_Type.__name__ = "PolicyRFC3580MapRadiusResponseTC"
_EtsysPolicyRFC3580MapResolveReponseConflict_Object = MibScalar
etsysPolicyRFC3580MapResolveReponseConflict = _EtsysPolicyRFC3580MapResolveReponseConflict_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 12, 1),
    _EtsysPolicyRFC3580MapResolveReponseConflict_Type()
)
etsysPolicyRFC3580MapResolveReponseConflict.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPolicyRFC3580MapResolveReponseConflict.setStatus("current")
_EtsysPolicyRFC3580MapLastChange_Type = TimeTicks
_EtsysPolicyRFC3580MapLastChange_Object = MibScalar
etsysPolicyRFC3580MapLastChange = _EtsysPolicyRFC3580MapLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 12, 2),
    _EtsysPolicyRFC3580MapLastChange_Type()
)
etsysPolicyRFC3580MapLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyRFC3580MapLastChange.setStatus("current")
_EtsysPolicyRFC3580MapTableDefault_Type = TruthValue
_EtsysPolicyRFC3580MapTableDefault_Object = MibScalar
etsysPolicyRFC3580MapTableDefault = _EtsysPolicyRFC3580MapTableDefault_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 12, 3),
    _EtsysPolicyRFC3580MapTableDefault_Type()
)
etsysPolicyRFC3580MapTableDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPolicyRFC3580MapTableDefault.setStatus("current")
_EtsysPolicyRFC3580MapTable_Object = MibTable
etsysPolicyRFC3580MapTable = _EtsysPolicyRFC3580MapTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 12, 4)
)
if mibBuilder.loadTexts:
    etsysPolicyRFC3580MapTable.setStatus("current")
_EtsysPolicyRFC3580MapEntry_Object = MibTableRow
etsysPolicyRFC3580MapEntry = _EtsysPolicyRFC3580MapEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 12, 4, 1)
)
etsysPolicyRFC3580MapEntry.setIndexNames(
    (0, "ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRFC3580MapVlanId"),
)
if mibBuilder.loadTexts:
    etsysPolicyRFC3580MapEntry.setStatus("current")
_EtsysPolicyRFC3580MapVlanId_Type = VlanIndex
_EtsysPolicyRFC3580MapVlanId_Object = MibTableColumn
etsysPolicyRFC3580MapVlanId = _EtsysPolicyRFC3580MapVlanId_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 12, 4, 1, 1),
    _EtsysPolicyRFC3580MapVlanId_Type()
)
etsysPolicyRFC3580MapVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysPolicyRFC3580MapVlanId.setStatus("current")


class _EtsysPolicyRFC3580MapPolicyIndex_Type(PolicyProfileIDTC):
    """Custom type etsysPolicyRFC3580MapPolicyIndex based on PolicyProfileIDTC"""
    defaultValue = 0

    subtypeSpec = PolicyProfileIDTC.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_EtsysPolicyRFC3580MapPolicyIndex_Type.__name__ = "PolicyProfileIDTC"
_EtsysPolicyRFC3580MapPolicyIndex_Object = MibTableColumn
etsysPolicyRFC3580MapPolicyIndex = _EtsysPolicyRFC3580MapPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 12, 4, 1, 2),
    _EtsysPolicyRFC3580MapPolicyIndex_Type()
)
etsysPolicyRFC3580MapPolicyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPolicyRFC3580MapPolicyIndex.setStatus("current")
_EtsysPolicyRFC3580MapInvalidMapping_Type = Counter32
_EtsysPolicyRFC3580MapInvalidMapping_Object = MibScalar
etsysPolicyRFC3580MapInvalidMapping = _EtsysPolicyRFC3580MapInvalidMapping_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 12, 5),
    _EtsysPolicyRFC3580MapInvalidMapping_Type()
)
etsysPolicyRFC3580MapInvalidMapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyRFC3580MapInvalidMapping.setStatus("current")
_EtsysPolicyHttpRedirect_ObjectIdentity = ObjectIdentity
etsysPolicyHttpRedirect = _EtsysPolicyHttpRedirect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 13)
)
_EtsysPolicyHttpRedirectMaxNumSockets_Type = Unsigned32
_EtsysPolicyHttpRedirectMaxNumSockets_Object = MibScalar
etsysPolicyHttpRedirectMaxNumSockets = _EtsysPolicyHttpRedirectMaxNumSockets_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 13, 1),
    _EtsysPolicyHttpRedirectMaxNumSockets_Type()
)
etsysPolicyHttpRedirectMaxNumSockets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyHttpRedirectMaxNumSockets.setStatus("current")
_EtsysPolicyHttpRedirectNumServerGroups_Type = Unsigned32
_EtsysPolicyHttpRedirectNumServerGroups_Object = MibScalar
etsysPolicyHttpRedirectNumServerGroups = _EtsysPolicyHttpRedirectNumServerGroups_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 13, 2),
    _EtsysPolicyHttpRedirectNumServerGroups_Type()
)
etsysPolicyHttpRedirectNumServerGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyHttpRedirectNumServerGroups.setStatus("current")
_EtsysPolicyHttpRedirectMaxNumServer_Type = Unsigned32
_EtsysPolicyHttpRedirectMaxNumServer_Object = MibScalar
etsysPolicyHttpRedirectMaxNumServer = _EtsysPolicyHttpRedirectMaxNumServer_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 13, 3),
    _EtsysPolicyHttpRedirectMaxNumServer_Type()
)
etsysPolicyHttpRedirectMaxNumServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPolicyHttpRedirectMaxNumServer.setStatus("current")
_EtsysPolicyHttpRedirectSocketTable_Object = MibTable
etsysPolicyHttpRedirectSocketTable = _EtsysPolicyHttpRedirectSocketTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 13, 4)
)
if mibBuilder.loadTexts:
    etsysPolicyHttpRedirectSocketTable.setStatus("current")
_EtsysPolicyHttpRedirectSocketEntry_Object = MibTableRow
etsysPolicyHttpRedirectSocketEntry = _EtsysPolicyHttpRedirectSocketEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 13, 4, 1)
)
etsysPolicyHttpRedirectSocketEntry.setIndexNames(
    (0, "ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyHttpRedirectSocketIndex"),
)
if mibBuilder.loadTexts:
    etsysPolicyHttpRedirectSocketEntry.setStatus("current")


class _EtsysPolicyHttpRedirectSocketIndex_Type(Integer32):
    """Custom type etsysPolicyHttpRedirectSocketIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_EtsysPolicyHttpRedirectSocketIndex_Type.__name__ = "Integer32"
_EtsysPolicyHttpRedirectSocketIndex_Object = MibTableColumn
etsysPolicyHttpRedirectSocketIndex = _EtsysPolicyHttpRedirectSocketIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 13, 4, 1, 1),
    _EtsysPolicyHttpRedirectSocketIndex_Type()
)
etsysPolicyHttpRedirectSocketIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysPolicyHttpRedirectSocketIndex.setStatus("current")


class _EtsysPolicyHttpRedirectListenSocket_Type(InetPortNumber):
    """Custom type etsysPolicyHttpRedirectListenSocket based on InetPortNumber"""
    defaultValue = 0


_EtsysPolicyHttpRedirectListenSocket_Type.__name__ = "InetPortNumber"
_EtsysPolicyHttpRedirectListenSocket_Object = MibTableColumn
etsysPolicyHttpRedirectListenSocket = _EtsysPolicyHttpRedirectListenSocket_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 13, 4, 1, 2),
    _EtsysPolicyHttpRedirectListenSocket_Type()
)
etsysPolicyHttpRedirectListenSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPolicyHttpRedirectListenSocket.setStatus("current")
_EtsysPolicyHttpRedirectServerTable_Object = MibTable
etsysPolicyHttpRedirectServerTable = _EtsysPolicyHttpRedirectServerTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 13, 5)
)
if mibBuilder.loadTexts:
    etsysPolicyHttpRedirectServerTable.setStatus("current")
_EtsysPolicyHttpRedirectServerEntry_Object = MibTableRow
etsysPolicyHttpRedirectServerEntry = _EtsysPolicyHttpRedirectServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 13, 5, 1)
)
etsysPolicyHttpRedirectServerEntry.setIndexNames(
    (0, "ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyHttpRedirectGroupIndex"),
    (0, "ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyHttpRedirectServerIndex"),
)
if mibBuilder.loadTexts:
    etsysPolicyHttpRedirectServerEntry.setStatus("current")


class _EtsysPolicyHttpRedirectGroupIndex_Type(Integer32):
    """Custom type etsysPolicyHttpRedirectGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EtsysPolicyHttpRedirectGroupIndex_Type.__name__ = "Integer32"
_EtsysPolicyHttpRedirectGroupIndex_Object = MibTableColumn
etsysPolicyHttpRedirectGroupIndex = _EtsysPolicyHttpRedirectGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 13, 5, 1, 1),
    _EtsysPolicyHttpRedirectGroupIndex_Type()
)
etsysPolicyHttpRedirectGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysPolicyHttpRedirectGroupIndex.setStatus("current")


class _EtsysPolicyHttpRedirectServerIndex_Type(Integer32):
    """Custom type etsysPolicyHttpRedirectServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EtsysPolicyHttpRedirectServerIndex_Type.__name__ = "Integer32"
_EtsysPolicyHttpRedirectServerIndex_Object = MibTableColumn
etsysPolicyHttpRedirectServerIndex = _EtsysPolicyHttpRedirectServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 13, 5, 1, 2),
    _EtsysPolicyHttpRedirectServerIndex_Type()
)
etsysPolicyHttpRedirectServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysPolicyHttpRedirectServerIndex.setStatus("current")


class _EtsysPolicyHttpRedirectServerUri_Type(Uri):
    """Custom type etsysPolicyHttpRedirectServerUri based on Uri"""
    defaultHexValue = ""


_EtsysPolicyHttpRedirectServerUri_Type.__name__ = "Uri"
_EtsysPolicyHttpRedirectServerUri_Object = MibTableColumn
etsysPolicyHttpRedirectServerUri = _EtsysPolicyHttpRedirectServerUri_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 13, 5, 1, 3),
    _EtsysPolicyHttpRedirectServerUri_Type()
)
etsysPolicyHttpRedirectServerUri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPolicyHttpRedirectServerUri.setStatus("current")


class _EtsysPolicyHttpRedirectServerStatus_Type(EnabledStatus):
    """Custom type etsysPolicyHttpRedirectServerStatus based on EnabledStatus"""
    defaultValue = 2


_EtsysPolicyHttpRedirectServerStatus_Type.__name__ = "EnabledStatus"
_EtsysPolicyHttpRedirectServerStatus_Object = MibTableColumn
etsysPolicyHttpRedirectServerStatus = _EtsysPolicyHttpRedirectServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 13, 5, 1, 4),
    _EtsysPolicyHttpRedirectServerStatus_Type()
)
etsysPolicyHttpRedirectServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPolicyHttpRedirectServerStatus.setStatus("current")
_EtsysPolicySystem_ObjectIdentity = ObjectIdentity
etsysPolicySystem = _EtsysPolicySystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 14)
)
_EtsysPolicyEnabledState_Type = EnabledStatus
_EtsysPolicyEnabledState_Object = MibScalar
etsysPolicyEnabledState = _EtsysPolicyEnabledState_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 14, 1),
    _EtsysPolicyEnabledState_Type()
)
etsysPolicyEnabledState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPolicyEnabledState.setStatus("current")

# Managed Objects groups

etsysPolicyProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 7, 1, 1)
)
etsysPolicyProfileGroup.setObjects(
      *(("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileMaxEntries"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileNumEntries"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileLastChange"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileTableNextAvailableIndex"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileName"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileRowStatus"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfilePortVidStatus"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfilePortVid"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfilePriorityStatus"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfilePriority"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileEgressVlans"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileForbiddenVlans"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileUntaggedVlans"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileOverwriteTCI"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileRulePrecedence"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileVlanRFC3580Mappings"))
)
if mibBuilder.loadTexts:
    etsysPolicyProfileGroup.setStatus("deprecated")

etsysPolicyClassificationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 7, 1, 2)
)
etsysPolicyClassificationGroup.setObjects(
      *(("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyClassificationMaxEntries"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyClassificationNumEntries"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyClassificationLastChange"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyClassificationOID"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyClassificationRowStatus"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyClassificationIngressList"))
)
if mibBuilder.loadTexts:
    etsysPolicyClassificationGroup.setStatus("deprecated")

etsysPortPolicyProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 7, 1, 3)
)
etsysPortPolicyProfileGroup.setObjects(
      *(("ENTERASYS-POLICY-PROFILE-MIB", "etsysPortPolicyProfileLastChange"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPortPolicyProfileAdminID"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPortPolicyProfileOperID"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPortPolicyProfileSummaryAdminID"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPortPolicyProfileSummaryOperID"))
)
if mibBuilder.loadTexts:
    etsysPortPolicyProfileGroup.setStatus("deprecated")

etsysStationPolicyProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 7, 1, 5)
)
etsysStationPolicyProfileGroup.setObjects(
      *(("ENTERASYS-POLICY-PROFILE-MIB", "etsysStationPolicyProfileMaxEntries"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysStationPolicyProfileNumEntries"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysStationPolicyProfileLastChange"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysStationIdentifierType"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysStationIdentifier"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysStationPolicyProfileOperID"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysStationPolicyProfilePortType"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysStationPolicyProfilePortID"))
)
if mibBuilder.loadTexts:
    etsysStationPolicyProfileGroup.setStatus("current")

etsysInvalidPolicyPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 7, 1, 6)
)
etsysInvalidPolicyPolicyGroup.setObjects(
      *(("ENTERASYS-POLICY-PROFILE-MIB", "etsysInvalidPolicyAction"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysInvalidPolicyCount"))
)
if mibBuilder.loadTexts:
    etsysInvalidPolicyPolicyGroup.setStatus("current")

etsysDevicePolicyProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 7, 1, 7)
)
etsysDevicePolicyProfileGroup.setObjects(
    ("ENTERASYS-POLICY-PROFILE-MIB", "etsysDevicePolicyProfileDefault")
)
if mibBuilder.loadTexts:
    etsysDevicePolicyProfileGroup.setStatus("current")

etsysPolicyCapabilitiesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 7, 1, 8)
)
etsysPolicyCapabilitiesGroup.setObjects(
      *(("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyVlanRuleCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyCosRuleCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyDropRuleCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyForwardRuleCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyDynaPIDRuleCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyAdminPIDRuleCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicySyslogRuleCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyTrapRuleCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyDisablePortRuleCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicySupportedPortList"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyEnabledSupportedRuleTypes"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyEnabledEnabledRuleTypes"))
)
if mibBuilder.loadTexts:
    etsysPolicyCapabilitiesGroup.setStatus("deprecated")

etsysPolicyMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 7, 1, 9)
)
etsysPolicyMapGroup.setObjects(
      *(("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyMapMaxEntries"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyMapNumEntries"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyMapLastChange"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyMapPvidOverRide"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyMapUnknownPvidPolicy"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyMapRowStatus"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyMapStartVid"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyMapEndVid"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyMapPolicyIndex"))
)
if mibBuilder.loadTexts:
    etsysPolicyMapGroup.setStatus("obsolete")

etsysPolicyRulesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 7, 1, 10)
)
etsysPolicyRulesGroup.setObjects(
      *(("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulesMaxEntries"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulesNumEntries"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulesLastChange"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulesAccountingEnable"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulesPortDisabledList"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleRowStatus"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleStorageType"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleUsageList"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleResult1"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleResult2"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleAuditSyslogEnable"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleAuditTrapEnable"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleDisablePort"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleOperPid"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulePortHit"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleDynamicProfileAssignmentOverride"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleDefaultDynamicSyslogStatus"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleDefaultDynamicTrapStatus"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleStatsAutoClearOnLink"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleStatsAutoClearInterval"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleStatsAutoClearPorts"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleStatsAutoClearOnProfile"))
)
if mibBuilder.loadTexts:
    etsysPolicyRulesGroup.setStatus("deprecated")

etsysPortPolicyProfileGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 7, 1, 11)
)
etsysPortPolicyProfileGroup2.setObjects(
      *(("ENTERASYS-POLICY-PROFILE-MIB", "etsysPortPolicyProfileSummaryAdminID"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPortPolicyProfileSummaryOperID"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPortPolicyProfileSummaryDynamicID"))
)
if mibBuilder.loadTexts:
    etsysPortPolicyProfileGroup2.setStatus("current")

etsysPolicyRFC3580MapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 7, 1, 12)
)
etsysPolicyRFC3580MapGroup.setObjects(
      *(("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRFC3580MapResolveReponseConflict"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRFC3580MapLastChange"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRFC3580MapTableDefault"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRFC3580MapPolicyIndex"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRFC3580MapInvalidMapping"))
)
if mibBuilder.loadTexts:
    etsysPolicyRFC3580MapGroup.setStatus("current")

etsysPolicyCapabilitiesGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 7, 1, 13)
)
etsysPolicyCapabilitiesGroup2.setObjects(
      *(("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyVlanRuleCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyCosRuleCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyDropRuleCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyForwardRuleCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyDynaPIDRuleCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyAdminPIDRuleCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicySyslogRuleCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyTrapRuleCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyDisablePortRuleCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicySupportedPortList"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyEnabledSupportedRuleTypes"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyEnabledEnabledRuleTypes"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleAttributeByteLength"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleAttributeBitLength"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleAttributeMaxCreatable"))
)
if mibBuilder.loadTexts:
    etsysPolicyCapabilitiesGroup2.setStatus("deprecated")

etsysPolicyRulesGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 7, 1, 14)
)
etsysPolicyRulesGroup2.setObjects(
      *(("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulesMaxEntries"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulesNumEntries"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulesLastChange"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulesAccountingEnable"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulesPortDisabledList"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleRowStatus"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleStorageType"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleUsageList"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleResult1"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleResult2"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleAuditSyslogEnable"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleAuditTrapEnable"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleDisablePort"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleOperPid"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulePortHit"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleDynamicProfileAssignmentOverride"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleDefaultDynamicSyslogStatus"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleDefaultDynamicTrapStatus"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleStatsAutoClearOnLink"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleStatsAutoClearInterval"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleStatsAutoClearPorts"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleStatsAutoClearOnProfile"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleStatsDroppedNotifications"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleSylogMachineReadableFormat"))
)
if mibBuilder.loadTexts:
    etsysPolicyRulesGroup2.setStatus("deprecated")

etsysPolicyRulesGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 7, 1, 16)
)
etsysPolicyRulesGroup3.setObjects(
      *(("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulesMaxEntries"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulesNumEntries"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulesLastChange"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulesAccountingEnable"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulesPortDisabledList"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleRowStatus"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleStorageType"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleUsageList"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleResult1"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleResult2"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleAuditSyslogEnable"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleAuditTrapEnable"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleDisablePort"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleOperPid"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulePortHit"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleDynamicProfileAssignmentOverride"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleDefaultDynamicSyslogStatus"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleDefaultDynamicTrapStatus"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleStatsAutoClearOnLink"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleStatsAutoClearInterval"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleStatsAutoClearPorts"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleStatsAutoClearOnProfile"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleStatsDroppedNotifications"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleSylogMachineReadableFormat"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleSylogExtendedFormat"))
)
if mibBuilder.loadTexts:
    etsysPolicyRulesGroup3.setStatus("deprecated")

etsysPolicyRulesGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 7, 1, 17)
)
etsysPolicyRulesGroup4.setObjects(
      *(("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulesMaxEntries"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulesNumEntries"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulesLastChange"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulesAccountingEnable"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulesPortDisabledList"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleRowStatus"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleStorageType"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleUsageList"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleResult1"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleResult2"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleAuditSyslogEnable"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleAuditTrapEnable"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleDisablePort"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleOperPid"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulePortHit"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleDynamicProfileAssignmentOverride"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleDefaultDynamicSyslogStatus"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleDefaultDynamicTrapStatus"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleStatsAutoClearOnLink"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleStatsAutoClearInterval"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleStatsAutoClearPorts"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleStatsAutoClearOnProfile"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleStatsDroppedNotifications"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleSylogMachineReadableFormat"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleSylogExtendedFormat"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleOverwriteTCI"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleMirrorIndex"))
)
if mibBuilder.loadTexts:
    etsysPolicyRulesGroup4.setStatus("deprecated")

etsysPolicyCapabilitiesGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 7, 1, 18)
)
etsysPolicyCapabilitiesGroup3.setObjects(
      *(("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyVlanRuleCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyCosRuleCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyDropRuleCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyForwardRuleCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyDynaPIDRuleCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyAdminPIDRuleCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicySyslogRuleCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyTrapRuleCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyDisablePortRuleCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicySupportedPortList"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyEnabledSupportedRuleTypes"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyEnabledEnabledRuleTypes"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleAttributeByteLength"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleAttributeBitLength"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleAttributeMaxCreatable"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleTciOverwriteCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleMirrorCapabilities"))
)
if mibBuilder.loadTexts:
    etsysPolicyCapabilitiesGroup3.setStatus("deprecated")

etsysPolicyProfileGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 7, 1, 19)
)
etsysPolicyProfileGroup2.setObjects(
      *(("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileMaxEntries"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileNumEntries"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileLastChange"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileTableNextAvailableIndex"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileName"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileRowStatus"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfilePortVidStatus"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfilePortVid"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfilePriorityStatus"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfilePriority"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileEgressVlans"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileForbiddenVlans"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileUntaggedVlans"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileOverwriteTCI"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileRulePrecedence"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileVlanRFC3580Mappings"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileMirrorIndex"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileAuditSyslogEnable"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileAuditTrapEnable"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileDisablePort"))
)
if mibBuilder.loadTexts:
    etsysPolicyProfileGroup2.setStatus("deprecated")

etsysPolicyRulesGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 7, 1, 20)
)
etsysPolicyRulesGroup5.setObjects(
      *(("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulesMaxEntries"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulesNumEntries"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulesLastChange"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulesAccountingEnable"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulesPortDisabledList"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleRowStatus"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleStorageType"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleUsageList"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleResult1"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleResult2"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleAuditSyslogEnable"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleAuditTrapEnable"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleDisablePort"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleOperPid"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulePortHit"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleDynamicProfileAssignmentOverride"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleDefaultDynamicSyslogStatus"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleDefaultDynamicTrapStatus"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleStatsAutoClearOnLink"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleStatsAutoClearInterval"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleStatsAutoClearPorts"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleStatsAutoClearOnProfile"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleStatsDroppedNotifications"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleSylogMachineReadableFormat"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleSylogExtendedFormat"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleSylogEveryTime"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleOverwriteTCI"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleMirrorIndex"))
)
if mibBuilder.loadTexts:
    etsysPolicyRulesGroup5.setStatus("deprecated")

etsysPolicyCapabilitiesGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 7, 1, 21)
)
etsysPolicyCapabilitiesGroup4.setObjects(
      *(("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyVlanRuleCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyCosRuleCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyDropRuleCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyForwardRuleCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyDynaPIDRuleCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyAdminPIDRuleCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicySyslogRuleCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyTrapRuleCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyDisablePortRuleCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicySupportedPortList"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyEnabledSupportedRuleTypes"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyEnabledEnabledRuleTypes"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyEnabledEgressEnabled"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleAttributeByteLength"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleAttributeBitLength"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleAttributeMaxCreatable"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleTciOverwriteCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleMirrorCapabilities"))
)
if mibBuilder.loadTexts:
    etsysPolicyCapabilitiesGroup4.setStatus("deprecated")

etsysPolicyProfileGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 7, 1, 22)
)
etsysPolicyProfileGroup3.setObjects(
      *(("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileMaxEntries"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileNumEntries"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileLastChange"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileTableNextAvailableIndex"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileName"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileRowStatus"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfilePortVidStatus"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfilePortVid"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfilePriorityStatus"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfilePriority"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileEgressVlans"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileForbiddenVlans"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileUntaggedVlans"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileOverwriteTCI"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileRulePrecedence"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileVlanRFC3580Mappings"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileMirrorIndex"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileAuditSyslogEnable"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileAuditTrapEnable"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileDisablePort"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileUsageList"))
)
if mibBuilder.loadTexts:
    etsysPolicyProfileGroup3.setStatus("deprecated")

etsysPolicyProfileGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 7, 1, 23)
)
etsysPolicyProfileGroup4.setObjects(
      *(("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileMaxEntries"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileNumEntries"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileLastChange"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileTableNextAvailableIndex"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileName"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileRowStatus"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfilePortVidStatus"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfilePortVid"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfilePriorityStatus"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfilePriority"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileEgressVlans"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileForbiddenVlans"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileUntaggedVlans"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileOverwriteTCI"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileRulePrecedence"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileVlanRFC3580Mappings"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileMirrorIndex"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileAuditSyslogEnable"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileAuditTrapEnable"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileDisablePort"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileUsageList"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileFstIndex"))
)
if mibBuilder.loadTexts:
    etsysPolicyProfileGroup4.setStatus("deprecated")

etsysPolicyRulesGroup6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 7, 1, 24)
)
etsysPolicyRulesGroup6.setObjects(
      *(("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulesMaxEntries"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulesNumEntries"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulesLastChange"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulesAccountingEnable"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulesPortDisabledList"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleRowStatus"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleStorageType"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleUsageList"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleResult1"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleResult2"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleAuditSyslogEnable"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleAuditTrapEnable"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleDisablePort"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleOperPid"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulePortHit"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleDynamicProfileAssignmentOverride"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleDefaultDynamicSyslogStatus"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleDefaultDynamicTrapStatus"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleStatsAutoClearOnLink"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleStatsAutoClearInterval"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleStatsAutoClearPorts"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleStatsAutoClearOnProfile"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleStatsDroppedNotifications"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleSylogMachineReadableFormat"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleSylogExtendedFormat"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleSylogEveryTime"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleOverwriteTCI"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleMirrorIndex"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleQuarantineProfileIndex"))
)
if mibBuilder.loadTexts:
    etsysPolicyRulesGroup6.setStatus("current")

etsysPolicyCapabilitiesGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 7, 1, 25)
)
etsysPolicyCapabilitiesGroup5.setObjects(
      *(("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyVlanRuleCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyCosRuleCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyDropRuleCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyForwardRuleCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyDynaPIDRuleCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyAdminPIDRuleCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicySyslogRuleCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyTrapRuleCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyDisablePortRuleCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicySupportedPortList"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyEnabledSupportedRuleTypes"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyEnabledEnabledRuleTypes"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyEnabledEgressEnabled"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleAttributeByteLength"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleAttributeBitLength"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleAttributeMaxCreatable"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleTciOverwriteCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleMirrorCapabilities"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleQuarantineCapabilities"))
)
if mibBuilder.loadTexts:
    etsysPolicyCapabilitiesGroup5.setStatus("current")

etsysPolicyNonVolatileRulesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 7, 1, 26)
)
etsysPolicyNonVolatileRulesGroup.setObjects(
      *(("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyNonVolatileRulesLastChange"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyNonVolatileRuleRowStatus"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyNonVolatileRuleStorageType"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyNonVolatileRuleUsageList"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyNonVolatileRuleResult1"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyNonVolatileRuleResult2"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyNonVolatileRuleAuditSyslogEnable"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyNonVolatileRuleAuditTrapEnable"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyNonVolatileRuleDisablePort"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyNonVolatileRuleOperPid"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyNonVolatileRuleOverwriteTCI"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyNonVolatileRuleMirrorIndex"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyNonVolatileRuleQuarantineProfileIndex"))
)
if mibBuilder.loadTexts:
    etsysPolicyNonVolatileRulesGroup.setStatus("current")

etsysPolicyProfileGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 7, 1, 27)
)
etsysPolicyProfileGroup5.setObjects(
      *(("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileMaxEntries"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileNumEntries"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileLastChange"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileTableNextAvailableIndex"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileName"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileRowStatus"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfilePortVidStatus"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfilePortVid"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfilePriorityStatus"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfilePriority"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileEgressVlans"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileForbiddenVlans"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileUntaggedVlans"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileOverwriteTCI"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileRulePrecedence"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileVlanRFC3580Mappings"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileMirrorIndex"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileAuditSyslogEnable"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileAuditTrapEnable"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileDisablePort"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileUsageList"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileFstIndex"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileHttpRedirectIndex"))
)
if mibBuilder.loadTexts:
    etsysPolicyProfileGroup5.setStatus("deprecated")

etsysPolicyHttpRedirectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 7, 1, 28)
)
etsysPolicyHttpRedirectGroup.setObjects(
      *(("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyHttpRedirectMaxNumSockets"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyHttpRedirectNumServerGroups"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyHttpRedirectMaxNumServer"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyHttpRedirectListenSocket"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyHttpRedirectServerUri"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyHttpRedirectServerStatus"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRuleHttpRedirectIndex"))
)
if mibBuilder.loadTexts:
    etsysPolicyHttpRedirectGroup.setStatus("current")

etsysPolicySystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 7, 1, 29)
)
etsysPolicySystemGroup.setObjects(
    ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyEnabledState")
)
if mibBuilder.loadTexts:
    etsysPolicySystemGroup.setStatus("current")

etsysPolicyProfileGroup6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 7, 1, 30)
)
etsysPolicyProfileGroup6.setObjects(
      *(("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileMaxEntries"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileNumEntries"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileLastChange"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileTableNextAvailableIndex"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileName"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileRowStatus"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfilePortVidStatus"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfilePortVid"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfilePriorityStatus"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfilePriority"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileEgressVlans"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileForbiddenVlans"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileUntaggedVlans"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileOverwriteTCI"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileRulePrecedence"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileVlanRFC3580Mappings"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileMirrorIndex"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileAuditSyslogEnable"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileAuditTrapEnable"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileDisablePort"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileUsageList"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileFstIndex"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileHttpRedirectIndex"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfilePortAuthOverride"))
)
if mibBuilder.loadTexts:
    etsysPolicyProfileGroup6.setStatus("current")


# Notification objects

etsysPolicyRulePortHitNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 0, 1)
)
etsysPolicyRulePortHitNotification.setObjects(
      *(("IF-MIB", "ifName"),
        ("IF-MIB", "ifAlias"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulePortHit"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileName"))
)
if mibBuilder.loadTexts:
    etsysPolicyRulePortHitNotification.setStatus(
        "current"
    )


# Notifications groups

etsysPolicyRulePortHitNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 7, 1, 15)
)
etsysPolicyRulePortHitNotificationGroup.setObjects(
    ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulePortHitNotification")
)
if mibBuilder.loadTexts:
    etsysPolicyRulePortHitNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

etsysPolicyProfileCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 7, 2, 1)
)
etsysPolicyProfileCompliance.setObjects(
      *(("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPortPolicyProfileGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyClassificationGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysStationPolicyProfileGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysInvalidPolicyPolicyGroup"))
)
if mibBuilder.loadTexts:
    etsysPolicyProfileCompliance.setStatus(
        "deprecated"
    )

etsysPolicyProfileCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 7, 2, 2)
)
etsysPolicyProfileCompliance2.setObjects(
      *(("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPortPolicyProfileGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyCapabilitiesGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyClassificationGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysStationPolicyProfileGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysInvalidPolicyPolicyGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysDevicePolicyProfileGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRFC3580MapGroup"))
)
if mibBuilder.loadTexts:
    etsysPolicyProfileCompliance2.setStatus(
        "deprecated"
    )

etsysPolicyProfileCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 7, 2, 3)
)
etsysPolicyProfileCompliance3.setObjects(
      *(("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPortPolicyProfileGroup2"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyCapabilitiesGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysStationPolicyProfileGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysInvalidPolicyPolicyGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysDevicePolicyProfileGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRFC3580MapGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulesGroup"))
)
if mibBuilder.loadTexts:
    etsysPolicyProfileCompliance3.setStatus(
        "deprecated"
    )

etsysPolicyProfileCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 7, 2, 4)
)
etsysPolicyProfileCompliance4.setObjects(
      *(("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPortPolicyProfileGroup2"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyCapabilitiesGroup2"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysStationPolicyProfileGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysInvalidPolicyPolicyGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysDevicePolicyProfileGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRFC3580MapGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulesGroup2"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulePortHitNotificationGroup"))
)
if mibBuilder.loadTexts:
    etsysPolicyProfileCompliance4.setStatus(
        "deprecated"
    )

etsysPolicyProfileCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 7, 2, 5)
)
etsysPolicyProfileCompliance5.setObjects(
      *(("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPortPolicyProfileGroup2"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyCapabilitiesGroup2"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysStationPolicyProfileGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysInvalidPolicyPolicyGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysDevicePolicyProfileGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRFC3580MapGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulesGroup3"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulePortHitNotificationGroup"))
)
if mibBuilder.loadTexts:
    etsysPolicyProfileCompliance5.setStatus(
        "deprecated"
    )

etsysPolicyProfileCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 7, 2, 6)
)
etsysPolicyProfileCompliance6.setObjects(
      *(("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPortPolicyProfileGroup2"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyCapabilitiesGroup3"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysStationPolicyProfileGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysInvalidPolicyPolicyGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysDevicePolicyProfileGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRFC3580MapGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulesGroup4"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulePortHitNotificationGroup"))
)
if mibBuilder.loadTexts:
    etsysPolicyProfileCompliance6.setStatus(
        "deprecated"
    )

etsysPolicyProfileCompliance7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 7, 2, 7)
)
etsysPolicyProfileCompliance7.setObjects(
      *(("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileGroup3"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPortPolicyProfileGroup2"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyCapabilitiesGroup4"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysStationPolicyProfileGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysInvalidPolicyPolicyGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysDevicePolicyProfileGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRFC3580MapGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulesGroup5"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulePortHitNotificationGroup"))
)
if mibBuilder.loadTexts:
    etsysPolicyProfileCompliance7.setStatus(
        "deprecated"
    )

etsysPolicyProfileCompliance8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 7, 2, 8)
)
etsysPolicyProfileCompliance8.setObjects(
      *(("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileGroup4"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPortPolicyProfileGroup2"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyCapabilitiesGroup4"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysStationPolicyProfileGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysInvalidPolicyPolicyGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysDevicePolicyProfileGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRFC3580MapGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulesGroup5"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulePortHitNotificationGroup"))
)
if mibBuilder.loadTexts:
    etsysPolicyProfileCompliance8.setStatus(
        "deprecated"
    )

etsysPolicyProfileCompliance9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 7, 2, 9)
)
etsysPolicyProfileCompliance9.setObjects(
      *(("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileGroup4"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPortPolicyProfileGroup2"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyCapabilitiesGroup5"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysStationPolicyProfileGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysInvalidPolicyPolicyGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysDevicePolicyProfileGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRFC3580MapGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulesGroup6"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulePortHitNotificationGroup"))
)
if mibBuilder.loadTexts:
    etsysPolicyProfileCompliance9.setStatus(
        "deprecated"
    )

etsysPolicyNonVolatileRuleCompliances = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 7, 2, 10)
)
etsysPolicyNonVolatileRuleCompliances.setObjects(
      *(("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulesGroup6"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyNonVolatileRulesGroup"))
)
if mibBuilder.loadTexts:
    etsysPolicyNonVolatileRuleCompliances.setStatus(
        "current"
    )

etsysPolicyProfileCompliance10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 7, 2, 11)
)
etsysPolicyProfileCompliance10.setObjects(
      *(("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileGroup5"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPortPolicyProfileGroup2"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyCapabilitiesGroup5"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysStationPolicyProfileGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysInvalidPolicyPolicyGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysDevicePolicyProfileGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRFC3580MapGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulesGroup6"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulePortHitNotificationGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyHttpRedirectGroup"))
)
if mibBuilder.loadTexts:
    etsysPolicyProfileCompliance10.setStatus(
        "deprecated"
    )

etsysPolicyProfileCompliance11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 7, 2, 12)
)
etsysPolicyProfileCompliance11.setObjects(
      *(("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileGroup5"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPortPolicyProfileGroup2"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyCapabilitiesGroup5"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicySystemGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysStationPolicyProfileGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysInvalidPolicyPolicyGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysDevicePolicyProfileGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRFC3580MapGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulesGroup6"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulePortHitNotificationGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyHttpRedirectGroup"))
)
if mibBuilder.loadTexts:
    etsysPolicyProfileCompliance11.setStatus(
        "deprecated"
    )

etsysPolicyProfileCompliance12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 6, 7, 2, 13)
)
etsysPolicyProfileCompliance12.setObjects(
      *(("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyProfileGroup6"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPortPolicyProfileGroup2"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyCapabilitiesGroup5"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicySystemGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysStationPolicyProfileGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysInvalidPolicyPolicyGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysDevicePolicyProfileGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRFC3580MapGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulesGroup6"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyRulePortHitNotificationGroup"),
        ("ENTERASYS-POLICY-PROFILE-MIB", "etsysPolicyHttpRedirectGroup"))
)
if mibBuilder.loadTexts:
    etsysPolicyProfileCompliance12.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-POLICY-PROFILE-MIB",
    **{"PolicyProfileIDTC": PolicyProfileIDTC,
       "PortPolicyProfileIndexTypeTC": PortPolicyProfileIndexTypeTC,
       "PolicyRFC3580MapRadiusResponseTC": PolicyRFC3580MapRadiusResponseTC,
       "VlanList": VlanList,
       "PolicyClassificationRuleType": PolicyClassificationRuleType,
       "PolicyRulesSupported": PolicyRulesSupported,
       "TriStateStatus": TriStateStatus,
       "etsysPolicyProfileMIB": etsysPolicyProfileMIB,
       "etsysPolicyNotifications": etsysPolicyNotifications,
       "etsysPolicyRulePortHitNotification": etsysPolicyRulePortHitNotification,
       "etsysPolicyProfile": etsysPolicyProfile,
       "etsysPolicyProfileMaxEntries": etsysPolicyProfileMaxEntries,
       "etsysPolicyProfileNumEntries": etsysPolicyProfileNumEntries,
       "etsysPolicyProfileLastChange": etsysPolicyProfileLastChange,
       "etsysPolicyProfileTableNextAvailableIndex": etsysPolicyProfileTableNextAvailableIndex,
       "etsysPolicyProfileTable": etsysPolicyProfileTable,
       "etsysPolicyProfileEntry": etsysPolicyProfileEntry,
       "etsysPolicyProfileIndex": etsysPolicyProfileIndex,
       "etsysPolicyProfileName": etsysPolicyProfileName,
       "etsysPolicyProfileRowStatus": etsysPolicyProfileRowStatus,
       "etsysPolicyProfilePortVidStatus": etsysPolicyProfilePortVidStatus,
       "etsysPolicyProfilePortVid": etsysPolicyProfilePortVid,
       "etsysPolicyProfilePriorityStatus": etsysPolicyProfilePriorityStatus,
       "etsysPolicyProfilePriority": etsysPolicyProfilePriority,
       "etsysPolicyProfileEgressVlans": etsysPolicyProfileEgressVlans,
       "etsysPolicyProfileForbiddenVlans": etsysPolicyProfileForbiddenVlans,
       "etsysPolicyProfileUntaggedVlans": etsysPolicyProfileUntaggedVlans,
       "etsysPolicyProfileOverwriteTCI": etsysPolicyProfileOverwriteTCI,
       "etsysPolicyProfileRulePrecedence": etsysPolicyProfileRulePrecedence,
       "etsysPolicyProfileVlanRFC3580Mappings": etsysPolicyProfileVlanRFC3580Mappings,
       "etsysPolicyProfileMirrorIndex": etsysPolicyProfileMirrorIndex,
       "etsysPolicyProfileAuditSyslogEnable": etsysPolicyProfileAuditSyslogEnable,
       "etsysPolicyProfileAuditTrapEnable": etsysPolicyProfileAuditTrapEnable,
       "etsysPolicyProfileDisablePort": etsysPolicyProfileDisablePort,
       "etsysPolicyProfileUsageList": etsysPolicyProfileUsageList,
       "etsysPolicyProfileFstIndex": etsysPolicyProfileFstIndex,
       "etsysPolicyProfileHttpRedirectIndex": etsysPolicyProfileHttpRedirectIndex,
       "etsysPolicyProfilePortAuthOverride": etsysPolicyProfilePortAuthOverride,
       "etsysPolicyClassification": etsysPolicyClassification,
       "etsysPolicyClassificationMaxEntries": etsysPolicyClassificationMaxEntries,
       "etsysPolicyClassificationNumEntries": etsysPolicyClassificationNumEntries,
       "etsysPolicyClassificationLastChange": etsysPolicyClassificationLastChange,
       "etsysPolicyClassificationTable": etsysPolicyClassificationTable,
       "etsysPolicyClassificationEntry": etsysPolicyClassificationEntry,
       "etsysPolicyClassificationIndex": etsysPolicyClassificationIndex,
       "etsysPolicyClassificationOID": etsysPolicyClassificationOID,
       "etsysPolicyClassificationRowStatus": etsysPolicyClassificationRowStatus,
       "etsysPolicyClassificationIngressList": etsysPolicyClassificationIngressList,
       "etsysPortPolicyProfile": etsysPortPolicyProfile,
       "etsysPortPolicyProfileLastChange": etsysPortPolicyProfileLastChange,
       "etsysPortPolicyProfileTable": etsysPortPolicyProfileTable,
       "etsysPortPolicyProfileEntry": etsysPortPolicyProfileEntry,
       "etsysPortPolicyProfileIndexType": etsysPortPolicyProfileIndexType,
       "etsysPortPolicyProfileIndex": etsysPortPolicyProfileIndex,
       "etsysPortPolicyProfileAdminID": etsysPortPolicyProfileAdminID,
       "etsysPortPolicyProfileOperID": etsysPortPolicyProfileOperID,
       "etsysPortPolicyProfileSummaryTable": etsysPortPolicyProfileSummaryTable,
       "etsysPortPolicyProfileSummaryEntry": etsysPortPolicyProfileSummaryEntry,
       "etsysPortPolicyProfileSummaryIndexType": etsysPortPolicyProfileSummaryIndexType,
       "etsysPortPolicyProfileSummaryAdminID": etsysPortPolicyProfileSummaryAdminID,
       "etsysPortPolicyProfileSummaryOperID": etsysPortPolicyProfileSummaryOperID,
       "etsysPortPolicyProfileSummaryDynamicID": etsysPortPolicyProfileSummaryDynamicID,
       "etsysPolicyVlanEgress": etsysPolicyVlanEgress,
       "etsysStationPolicyProfile": etsysStationPolicyProfile,
       "etsysStationPolicyProfileMaxEntries": etsysStationPolicyProfileMaxEntries,
       "etsysStationPolicyProfileNumEntries": etsysStationPolicyProfileNumEntries,
       "etsysStationPolicyProfileLastChange": etsysStationPolicyProfileLastChange,
       "etsysStationPolicyProfileTable": etsysStationPolicyProfileTable,
       "etsysStationPolicyProfileEntry": etsysStationPolicyProfileEntry,
       "etsysStationPolicyProfileIndex": etsysStationPolicyProfileIndex,
       "etsysStationIdentifierType": etsysStationIdentifierType,
       "etsysStationIdentifier": etsysStationIdentifier,
       "etsysStationPolicyProfileOperID": etsysStationPolicyProfileOperID,
       "etsysStationPolicyProfilePortType": etsysStationPolicyProfilePortType,
       "etsysStationPolicyProfilePortID": etsysStationPolicyProfilePortID,
       "etsysInvalidPolicyPolicy": etsysInvalidPolicyPolicy,
       "etsysInvalidPolicyAction": etsysInvalidPolicyAction,
       "etsysInvalidPolicyCount": etsysInvalidPolicyCount,
       "etsysPolicyProfileConformance": etsysPolicyProfileConformance,
       "etsysPolicyProfileGroups": etsysPolicyProfileGroups,
       "etsysPolicyProfileGroup": etsysPolicyProfileGroup,
       "etsysPolicyClassificationGroup": etsysPolicyClassificationGroup,
       "etsysPortPolicyProfileGroup": etsysPortPolicyProfileGroup,
       "etsysStationPolicyProfileGroup": etsysStationPolicyProfileGroup,
       "etsysInvalidPolicyPolicyGroup": etsysInvalidPolicyPolicyGroup,
       "etsysDevicePolicyProfileGroup": etsysDevicePolicyProfileGroup,
       "etsysPolicyCapabilitiesGroup": etsysPolicyCapabilitiesGroup,
       "etsysPolicyMapGroup": etsysPolicyMapGroup,
       "etsysPolicyRulesGroup": etsysPolicyRulesGroup,
       "etsysPortPolicyProfileGroup2": etsysPortPolicyProfileGroup2,
       "etsysPolicyRFC3580MapGroup": etsysPolicyRFC3580MapGroup,
       "etsysPolicyCapabilitiesGroup2": etsysPolicyCapabilitiesGroup2,
       "etsysPolicyRulesGroup2": etsysPolicyRulesGroup2,
       "etsysPolicyRulePortHitNotificationGroup": etsysPolicyRulePortHitNotificationGroup,
       "etsysPolicyRulesGroup3": etsysPolicyRulesGroup3,
       "etsysPolicyRulesGroup4": etsysPolicyRulesGroup4,
       "etsysPolicyCapabilitiesGroup3": etsysPolicyCapabilitiesGroup3,
       "etsysPolicyProfileGroup2": etsysPolicyProfileGroup2,
       "etsysPolicyRulesGroup5": etsysPolicyRulesGroup5,
       "etsysPolicyCapabilitiesGroup4": etsysPolicyCapabilitiesGroup4,
       "etsysPolicyProfileGroup3": etsysPolicyProfileGroup3,
       "etsysPolicyProfileGroup4": etsysPolicyProfileGroup4,
       "etsysPolicyRulesGroup6": etsysPolicyRulesGroup6,
       "etsysPolicyCapabilitiesGroup5": etsysPolicyCapabilitiesGroup5,
       "etsysPolicyNonVolatileRulesGroup": etsysPolicyNonVolatileRulesGroup,
       "etsysPolicyProfileGroup5": etsysPolicyProfileGroup5,
       "etsysPolicyHttpRedirectGroup": etsysPolicyHttpRedirectGroup,
       "etsysPolicySystemGroup": etsysPolicySystemGroup,
       "etsysPolicyProfileGroup6": etsysPolicyProfileGroup6,
       "etsysPolicyProfileCompliances": etsysPolicyProfileCompliances,
       "etsysPolicyProfileCompliance": etsysPolicyProfileCompliance,
       "etsysPolicyProfileCompliance2": etsysPolicyProfileCompliance2,
       "etsysPolicyProfileCompliance3": etsysPolicyProfileCompliance3,
       "etsysPolicyProfileCompliance4": etsysPolicyProfileCompliance4,
       "etsysPolicyProfileCompliance5": etsysPolicyProfileCompliance5,
       "etsysPolicyProfileCompliance6": etsysPolicyProfileCompliance6,
       "etsysPolicyProfileCompliance7": etsysPolicyProfileCompliance7,
       "etsysPolicyProfileCompliance8": etsysPolicyProfileCompliance8,
       "etsysPolicyProfileCompliance9": etsysPolicyProfileCompliance9,
       "etsysPolicyNonVolatileRuleCompliances": etsysPolicyNonVolatileRuleCompliances,
       "etsysPolicyProfileCompliance10": etsysPolicyProfileCompliance10,
       "etsysPolicyProfileCompliance11": etsysPolicyProfileCompliance11,
       "etsysPolicyProfileCompliance12": etsysPolicyProfileCompliance12,
       "etsysDevicePolicyProfile": etsysDevicePolicyProfile,
       "etsysDevicePolicyProfileDefault": etsysDevicePolicyProfileDefault,
       "etsysPolicyCapability": etsysPolicyCapability,
       "etsysPolicyCapabilities": etsysPolicyCapabilities,
       "etsysPolicyDynaPIDRuleCapabilities": etsysPolicyDynaPIDRuleCapabilities,
       "etsysPolicyAdminPIDRuleCapabilities": etsysPolicyAdminPIDRuleCapabilities,
       "etsysPolicyVlanRuleCapabilities": etsysPolicyVlanRuleCapabilities,
       "etsysPolicyCosRuleCapabilities": etsysPolicyCosRuleCapabilities,
       "etsysPolicyDropRuleCapabilities": etsysPolicyDropRuleCapabilities,
       "etsysPolicyForwardRuleCapabilities": etsysPolicyForwardRuleCapabilities,
       "etsysPolicySyslogRuleCapabilities": etsysPolicySyslogRuleCapabilities,
       "etsysPolicyTrapRuleCapabilities": etsysPolicyTrapRuleCapabilities,
       "etsysPolicyDisablePortRuleCapabilities": etsysPolicyDisablePortRuleCapabilities,
       "etsysPolicySupportedPortList": etsysPolicySupportedPortList,
       "etsysPolicyEnabledTable": etsysPolicyEnabledTable,
       "etsysPolicyEnabledTableEntry": etsysPolicyEnabledTableEntry,
       "etsysPolicyEnabledSupportedRuleTypes": etsysPolicyEnabledSupportedRuleTypes,
       "etsysPolicyEnabledEnabledRuleTypes": etsysPolicyEnabledEnabledRuleTypes,
       "etsysPolicyEnabledEgressEnabled": etsysPolicyEnabledEgressEnabled,
       "etsysPolicyRuleAttributeTable": etsysPolicyRuleAttributeTable,
       "etsysPolicyRuleAttributeTableEntry": etsysPolicyRuleAttributeTableEntry,
       "etsysPolicyRuleAttributeByteLength": etsysPolicyRuleAttributeByteLength,
       "etsysPolicyRuleAttributeBitLength": etsysPolicyRuleAttributeBitLength,
       "etsysPolicyRuleAttributeMaxCreatable": etsysPolicyRuleAttributeMaxCreatable,
       "etsysPolicyRuleTciOverwriteCapabilities": etsysPolicyRuleTciOverwriteCapabilities,
       "etsysPolicyRuleMirrorCapabilities": etsysPolicyRuleMirrorCapabilities,
       "etsysPolicyRuleQuarantineCapabilities": etsysPolicyRuleQuarantineCapabilities,
       "etsysPolicyMap": etsysPolicyMap,
       "etsysPolicyMapMaxEntries": etsysPolicyMapMaxEntries,
       "etsysPolicyMapNumEntries": etsysPolicyMapNumEntries,
       "etsysPolicyMapLastChange": etsysPolicyMapLastChange,
       "etsysPolicyMapPvidOverRide": etsysPolicyMapPvidOverRide,
       "etsysPolicyMapUnknownPvidPolicy": etsysPolicyMapUnknownPvidPolicy,
       "etsysPolicyMapTable": etsysPolicyMapTable,
       "etsysPolicyMapEntry": etsysPolicyMapEntry,
       "etsysPolicyMapIndex": etsysPolicyMapIndex,
       "etsysPolicyMapRowStatus": etsysPolicyMapRowStatus,
       "etsysPolicyMapStartVid": etsysPolicyMapStartVid,
       "etsysPolicyMapEndVid": etsysPolicyMapEndVid,
       "etsysPolicyMapPolicyIndex": etsysPolicyMapPolicyIndex,
       "etsysPolicyRules": etsysPolicyRules,
       "etsysPolicyRulesMaxEntries": etsysPolicyRulesMaxEntries,
       "etsysPolicyRulesNumEntries": etsysPolicyRulesNumEntries,
       "etsysPolicyRulesLastChange": etsysPolicyRulesLastChange,
       "etsysPolicyRulesAccountingEnable": etsysPolicyRulesAccountingEnable,
       "etsysPolicyRulesPortDisabledList": etsysPolicyRulesPortDisabledList,
       "etsysPolicyRuleTable": etsysPolicyRuleTable,
       "etsysPolicyRuleEntry": etsysPolicyRuleEntry,
       "etsysPolicyRuleProfileIndex": etsysPolicyRuleProfileIndex,
       "etsysPolicyRuleType": etsysPolicyRuleType,
       "etsysPolicyRuleData": etsysPolicyRuleData,
       "etsysPolicyRulePrefixBits": etsysPolicyRulePrefixBits,
       "etsysPolicyRulePortType": etsysPolicyRulePortType,
       "etsysPolicyRulePort": etsysPolicyRulePort,
       "etsysPolicyRuleRowStatus": etsysPolicyRuleRowStatus,
       "etsysPolicyRuleStorageType": etsysPolicyRuleStorageType,
       "etsysPolicyRuleUsageList": etsysPolicyRuleUsageList,
       "etsysPolicyRuleResult1": etsysPolicyRuleResult1,
       "etsysPolicyRuleResult2": etsysPolicyRuleResult2,
       "etsysPolicyRuleAuditSyslogEnable": etsysPolicyRuleAuditSyslogEnable,
       "etsysPolicyRuleAuditTrapEnable": etsysPolicyRuleAuditTrapEnable,
       "etsysPolicyRuleDisablePort": etsysPolicyRuleDisablePort,
       "etsysPolicyRuleOperPid": etsysPolicyRuleOperPid,
       "etsysPolicyRuleOverwriteTCI": etsysPolicyRuleOverwriteTCI,
       "etsysPolicyRuleMirrorIndex": etsysPolicyRuleMirrorIndex,
       "etsysPolicyRuleQuarantineProfileIndex": etsysPolicyRuleQuarantineProfileIndex,
       "etsysPolicyRuleHttpRedirectIndex": etsysPolicyRuleHttpRedirectIndex,
       "etsysPolicyRulePortTable": etsysPolicyRulePortTable,
       "etsysPolicyRulePortEntry": etsysPolicyRulePortEntry,
       "etsysPolicyRulePortHit": etsysPolicyRulePortHit,
       "etsysPolicyRuleDynamicProfileAssignmentOverride": etsysPolicyRuleDynamicProfileAssignmentOverride,
       "etsysPolicyRuleDefaultDynamicSyslogStatus": etsysPolicyRuleDefaultDynamicSyslogStatus,
       "etsysPolicyRuleDefaultDynamicTrapStatus": etsysPolicyRuleDefaultDynamicTrapStatus,
       "etsysPolicyRuleStatsAutoClearOnLink": etsysPolicyRuleStatsAutoClearOnLink,
       "etsysPolicyRuleStatsAutoClearInterval": etsysPolicyRuleStatsAutoClearInterval,
       "etsysPolicyRuleStatsAutoClearPorts": etsysPolicyRuleStatsAutoClearPorts,
       "etsysPolicyRuleStatsAutoClearOnProfile": etsysPolicyRuleStatsAutoClearOnProfile,
       "etsysPolicyRuleStatsDroppedNotifications": etsysPolicyRuleStatsDroppedNotifications,
       "etsysPolicyRuleSylogMachineReadableFormat": etsysPolicyRuleSylogMachineReadableFormat,
       "etsysPolicyRuleSylogExtendedFormat": etsysPolicyRuleSylogExtendedFormat,
       "etsysPolicyRuleSylogEveryTime": etsysPolicyRuleSylogEveryTime,
       "etsysPolicyNonVolatileRulesLastChange": etsysPolicyNonVolatileRulesLastChange,
       "etsysPolicyNonVolatileRuleTable": etsysPolicyNonVolatileRuleTable,
       "etsysPolicyNonVolatileRuleEntry": etsysPolicyNonVolatileRuleEntry,
       "etsysPolicyNonVolatileRuleRowStatus": etsysPolicyNonVolatileRuleRowStatus,
       "etsysPolicyNonVolatileRuleStorageType": etsysPolicyNonVolatileRuleStorageType,
       "etsysPolicyNonVolatileRuleUsageList": etsysPolicyNonVolatileRuleUsageList,
       "etsysPolicyNonVolatileRuleResult1": etsysPolicyNonVolatileRuleResult1,
       "etsysPolicyNonVolatileRuleResult2": etsysPolicyNonVolatileRuleResult2,
       "etsysPolicyNonVolatileRuleAuditSyslogEnable": etsysPolicyNonVolatileRuleAuditSyslogEnable,
       "etsysPolicyNonVolatileRuleAuditTrapEnable": etsysPolicyNonVolatileRuleAuditTrapEnable,
       "etsysPolicyNonVolatileRuleDisablePort": etsysPolicyNonVolatileRuleDisablePort,
       "etsysPolicyNonVolatileRuleOperPid": etsysPolicyNonVolatileRuleOperPid,
       "etsysPolicyNonVolatileRuleOverwriteTCI": etsysPolicyNonVolatileRuleOverwriteTCI,
       "etsysPolicyNonVolatileRuleMirrorIndex": etsysPolicyNonVolatileRuleMirrorIndex,
       "etsysPolicyNonVolatileRuleQuarantineProfileIndex": etsysPolicyNonVolatileRuleQuarantineProfileIndex,
       "etsysPolicyRFC3580Map": etsysPolicyRFC3580Map,
       "etsysPolicyRFC3580MapResolveReponseConflict": etsysPolicyRFC3580MapResolveReponseConflict,
       "etsysPolicyRFC3580MapLastChange": etsysPolicyRFC3580MapLastChange,
       "etsysPolicyRFC3580MapTableDefault": etsysPolicyRFC3580MapTableDefault,
       "etsysPolicyRFC3580MapTable": etsysPolicyRFC3580MapTable,
       "etsysPolicyRFC3580MapEntry": etsysPolicyRFC3580MapEntry,
       "etsysPolicyRFC3580MapVlanId": etsysPolicyRFC3580MapVlanId,
       "etsysPolicyRFC3580MapPolicyIndex": etsysPolicyRFC3580MapPolicyIndex,
       "etsysPolicyRFC3580MapInvalidMapping": etsysPolicyRFC3580MapInvalidMapping,
       "etsysPolicyHttpRedirect": etsysPolicyHttpRedirect,
       "etsysPolicyHttpRedirectMaxNumSockets": etsysPolicyHttpRedirectMaxNumSockets,
       "etsysPolicyHttpRedirectNumServerGroups": etsysPolicyHttpRedirectNumServerGroups,
       "etsysPolicyHttpRedirectMaxNumServer": etsysPolicyHttpRedirectMaxNumServer,
       "etsysPolicyHttpRedirectSocketTable": etsysPolicyHttpRedirectSocketTable,
       "etsysPolicyHttpRedirectSocketEntry": etsysPolicyHttpRedirectSocketEntry,
       "etsysPolicyHttpRedirectSocketIndex": etsysPolicyHttpRedirectSocketIndex,
       "etsysPolicyHttpRedirectListenSocket": etsysPolicyHttpRedirectListenSocket,
       "etsysPolicyHttpRedirectServerTable": etsysPolicyHttpRedirectServerTable,
       "etsysPolicyHttpRedirectServerEntry": etsysPolicyHttpRedirectServerEntry,
       "etsysPolicyHttpRedirectGroupIndex": etsysPolicyHttpRedirectGroupIndex,
       "etsysPolicyHttpRedirectServerIndex": etsysPolicyHttpRedirectServerIndex,
       "etsysPolicyHttpRedirectServerUri": etsysPolicyHttpRedirectServerUri,
       "etsysPolicyHttpRedirectServerStatus": etsysPolicyHttpRedirectServerStatus,
       "etsysPolicySystem": etsysPolicySystem,
       "etsysPolicyEnabledState": etsysPolicyEnabledState}
)
