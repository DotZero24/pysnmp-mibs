# SNMP MIB module (CAMBIUM-NETWORKS-AUTO-ATTACH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/cambium/CAMBIUM-NETWORKS-AUTO-ATTACH-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:07:35 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cnAutoAttachMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1)
)
if mibBuilder.loadTexts:
    cnAutoAttachMib.setRevisions(
        ("2022-09-21 00:00",
         "2021-12-10 00:00",
         "2021-09-29 00:00",
         "2021-02-11 00:00",
         "2021-01-19 00:00",
         "2020-10-12 00:00",
         "2020-06-05 00:00",
         "2019-10-10 00:00",
         "2019-09-10 00:00",
         "2019-06-26 00:00",
         "2019-01-23 00:00",
         "2018-10-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cambium_ObjectIdentity = ObjectIdentity
cambium = _Cambium_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713)
)
_CnMatrix_ObjectIdentity = ObjectIdentity
cnMatrix = _CnMatrix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 24)
)
_CnAutoAttachNotifications_ObjectIdentity = ObjectIdentity
cnAutoAttachNotifications = _CnAutoAttachNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 0)
)
_CnAutoAttachObjects_ObjectIdentity = ObjectIdentity
cnAutoAttachObjects = _CnAutoAttachObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1)
)


class _CnAutoAttachService_Type(Integer32):
    """Custom type cnAutoAttachService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_CnAutoAttachService_Type.__name__ = "Integer32"
_CnAutoAttachService_Object = MibScalar
cnAutoAttachService = _CnAutoAttachService_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 1),
    _CnAutoAttachService_Type()
)
cnAutoAttachService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAutoAttachService.setStatus("current")


class _CnAutoAttachDataDiffAllowed_Type(Integer32):
    """Custom type cnAutoAttachDataDiffAllowed based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_CnAutoAttachDataDiffAllowed_Type.__name__ = "Integer32"
_CnAutoAttachDataDiffAllowed_Object = MibScalar
cnAutoAttachDataDiffAllowed = _CnAutoAttachDataDiffAllowed_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 2),
    _CnAutoAttachDataDiffAllowed_Type()
)
cnAutoAttachDataDiffAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAutoAttachDataDiffAllowed.setStatus("current")


class _CnAutoAttachDeviceDataCompare_Type(Integer32):
    """Custom type cnAutoAttachDeviceDataCompare based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("caseSensitive", 1),
          ("caseInsensitive", 2))
    )


_CnAutoAttachDeviceDataCompare_Type.__name__ = "Integer32"
_CnAutoAttachDeviceDataCompare_Object = MibScalar
cnAutoAttachDeviceDataCompare = _CnAutoAttachDeviceDataCompare_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 3),
    _CnAutoAttachDeviceDataCompare_Type()
)
cnAutoAttachDeviceDataCompare.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAutoAttachDeviceDataCompare.setStatus("current")


class _CnAutoAttachClearPolicyStats_Type(TruthValue):
    """Custom type cnAutoAttachClearPolicyStats based on TruthValue"""
    defaultValue = 2


_CnAutoAttachClearPolicyStats_Type.__name__ = "TruthValue"
_CnAutoAttachClearPolicyStats_Object = MibScalar
cnAutoAttachClearPolicyStats = _CnAutoAttachClearPolicyStats_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 4),
    _CnAutoAttachClearPolicyStats_Type()
)
cnAutoAttachClearPolicyStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAutoAttachClearPolicyStats.setStatus("current")


class _CnAutoAttachClearInterfaceStats_Type(TruthValue):
    """Custom type cnAutoAttachClearInterfaceStats based on TruthValue"""
    defaultValue = 2


_CnAutoAttachClearInterfaceStats_Type.__name__ = "TruthValue"
_CnAutoAttachClearInterfaceStats_Object = MibScalar
cnAutoAttachClearInterfaceStats = _CnAutoAttachClearInterfaceStats_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 5),
    _CnAutoAttachClearInterfaceStats_Type()
)
cnAutoAttachClearInterfaceStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAutoAttachClearInterfaceStats.setStatus("current")


class _CnAutoAttachUpdatePortDesc_Type(Integer32):
    """Custom type cnAutoAttachUpdatePortDesc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("pbaPolicyName", 2),
          ("lldpSystemName", 3),
          ("lldpSystemDescription", 4))
    )


_CnAutoAttachUpdatePortDesc_Type.__name__ = "Integer32"
_CnAutoAttachUpdatePortDesc_Object = MibScalar
cnAutoAttachUpdatePortDesc = _CnAutoAttachUpdatePortDesc_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 6),
    _CnAutoAttachUpdatePortDesc_Type()
)
cnAutoAttachUpdatePortDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAutoAttachUpdatePortDesc.setStatus("current")


class _CnAutoAttachRestrictedMacMatch_Type(Integer32):
    """Custom type cnAutoAttachRestrictedMacMatch based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_CnAutoAttachRestrictedMacMatch_Type.__name__ = "Integer32"
_CnAutoAttachRestrictedMacMatch_Object = MibScalar
cnAutoAttachRestrictedMacMatch = _CnAutoAttachRestrictedMacMatch_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 7),
    _CnAutoAttachRestrictedMacMatch_Type()
)
cnAutoAttachRestrictedMacMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAutoAttachRestrictedMacMatch.setStatus("current")


class _CnAutoAttachActivePolicyReorder_Type(Integer32):
    """Custom type cnAutoAttachActivePolicyReorder based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_CnAutoAttachActivePolicyReorder_Type.__name__ = "Integer32"
_CnAutoAttachActivePolicyReorder_Object = MibScalar
cnAutoAttachActivePolicyReorder = _CnAutoAttachActivePolicyReorder_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 8),
    _CnAutoAttachActivePolicyReorder_Type()
)
cnAutoAttachActivePolicyReorder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAutoAttachActivePolicyReorder.setStatus("current")


class _CnAutoAttachMacPolicyAging_Type(Integer32):
    """Custom type cnAutoAttachMacPolicyAging based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_CnAutoAttachMacPolicyAging_Type.__name__ = "Integer32"
_CnAutoAttachMacPolicyAging_Object = MibScalar
cnAutoAttachMacPolicyAging = _CnAutoAttachMacPolicyAging_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 9),
    _CnAutoAttachMacPolicyAging_Type()
)
cnAutoAttachMacPolicyAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAutoAttachMacPolicyAging.setStatus("current")
_CnAutoAttachPortTable_Object = MibTable
cnAutoAttachPortTable = _CnAutoAttachPortTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 10)
)
if mibBuilder.loadTexts:
    cnAutoAttachPortTable.setStatus("current")
_CnAutoAttachPortEntry_Object = MibTableRow
cnAutoAttachPortEntry = _CnAutoAttachPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 10, 1)
)
cnAutoAttachPortEntry.setIndexNames(
    (0, "CAMBIUM-NETWORKS-AUTO-ATTACH-MIB", "cnAutoAttachPortIfIndex"),
)
if mibBuilder.loadTexts:
    cnAutoAttachPortEntry.setStatus("current")


class _CnAutoAttachPortIfIndex_Type(Integer32):
    """Custom type cnAutoAttachPortIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CnAutoAttachPortIfIndex_Type.__name__ = "Integer32"
_CnAutoAttachPortIfIndex_Object = MibTableColumn
cnAutoAttachPortIfIndex = _CnAutoAttachPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 10, 1, 1),
    _CnAutoAttachPortIfIndex_Type()
)
cnAutoAttachPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnAutoAttachPortIfIndex.setStatus("current")


class _CnAutoAttachPortState_Type(Integer32):
    """Custom type cnAutoAttachPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_CnAutoAttachPortState_Type.__name__ = "Integer32"
_CnAutoAttachPortState_Object = MibTableColumn
cnAutoAttachPortState = _CnAutoAttachPortState_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 10, 1, 2),
    _CnAutoAttachPortState_Type()
)
cnAutoAttachPortState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAutoAttachPortState.setStatus("current")


class _CnAutoAttachPortMsgAuthStatus_Type(Integer32):
    """Custom type cnAutoAttachPortMsgAuthStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_CnAutoAttachPortMsgAuthStatus_Type.__name__ = "Integer32"
_CnAutoAttachPortMsgAuthStatus_Object = MibTableColumn
cnAutoAttachPortMsgAuthStatus = _CnAutoAttachPortMsgAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 10, 1, 3),
    _CnAutoAttachPortMsgAuthStatus_Type()
)
cnAutoAttachPortMsgAuthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAutoAttachPortMsgAuthStatus.setStatus("current")


class _CnAutoAttachPortMsgAuthKey_Type(OctetString):
    """Custom type cnAutoAttachPortMsgAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CnAutoAttachPortMsgAuthKey_Type.__name__ = "OctetString"
_CnAutoAttachPortMsgAuthKey_Object = MibTableColumn
cnAutoAttachPortMsgAuthKey = _CnAutoAttachPortMsgAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 10, 1, 4),
    _CnAutoAttachPortMsgAuthKey_Type()
)
cnAutoAttachPortMsgAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAutoAttachPortMsgAuthKey.setStatus("current")


class _CnAutoAttachPortActivePolicyName_Type(SnmpAdminString):
    """Custom type cnAutoAttachPortActivePolicyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CnAutoAttachPortActivePolicyName_Type.__name__ = "SnmpAdminString"
_CnAutoAttachPortActivePolicyName_Object = MibTableColumn
cnAutoAttachPortActivePolicyName = _CnAutoAttachPortActivePolicyName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 10, 1, 5),
    _CnAutoAttachPortActivePolicyName_Type()
)
cnAutoAttachPortActivePolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAutoAttachPortActivePolicyName.setStatus("current")
_CnAutoAttachPortPolicyApplied_Type = Counter32
_CnAutoAttachPortPolicyApplied_Object = MibTableColumn
cnAutoAttachPortPolicyApplied = _CnAutoAttachPortPolicyApplied_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 10, 1, 6),
    _CnAutoAttachPortPolicyApplied_Type()
)
cnAutoAttachPortPolicyApplied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAutoAttachPortPolicyApplied.setStatus("current")
_CnAutoAttachPortPolicyExpired_Type = Counter32
_CnAutoAttachPortPolicyExpired_Object = MibTableColumn
cnAutoAttachPortPolicyExpired = _CnAutoAttachPortPolicyExpired_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 10, 1, 7),
    _CnAutoAttachPortPolicyExpired_Type()
)
cnAutoAttachPortPolicyExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAutoAttachPortPolicyExpired.setStatus("current")
_CnAutoAttachPortPolicyErrors_Type = Counter32
_CnAutoAttachPortPolicyErrors_Object = MibTableColumn
cnAutoAttachPortPolicyErrors = _CnAutoAttachPortPolicyErrors_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 10, 1, 8),
    _CnAutoAttachPortPolicyErrors_Type()
)
cnAutoAttachPortPolicyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAutoAttachPortPolicyErrors.setStatus("current")
_CnAutoAttachPortRowStatus_Type = RowStatus
_CnAutoAttachPortRowStatus_Object = MibTableColumn
cnAutoAttachPortRowStatus = _CnAutoAttachPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 10, 1, 9),
    _CnAutoAttachPortRowStatus_Type()
)
cnAutoAttachPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAutoAttachPortRowStatus.setStatus("current")


class _CnAutoAttachPortTlvTxEnable_Type(Bits):
    """Custom type cnAutoAttachPortTlvTxEnable based on Bits"""
    namedValues = NamedValues(
        *(("pbaAuthenticationTlv", 0),
          ("pbaDeviceSettingsTlv", 1))
    )

_CnAutoAttachPortTlvTxEnable_Type.__name__ = "Bits"
_CnAutoAttachPortTlvTxEnable_Object = MibTableColumn
cnAutoAttachPortTlvTxEnable = _CnAutoAttachPortTlvTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 10, 1, 10),
    _CnAutoAttachPortTlvTxEnable_Type()
)
cnAutoAttachPortTlvTxEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAutoAttachPortTlvTxEnable.setStatus("current")
_CnAutoAttachPortDevSettingsTlvReceived_Type = Counter32
_CnAutoAttachPortDevSettingsTlvReceived_Object = MibTableColumn
cnAutoAttachPortDevSettingsTlvReceived = _CnAutoAttachPortDevSettingsTlvReceived_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 10, 1, 11),
    _CnAutoAttachPortDevSettingsTlvReceived_Type()
)
cnAutoAttachPortDevSettingsTlvReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAutoAttachPortDevSettingsTlvReceived.setStatus("current")
_CnAutoAttachPortDevSettingsTlvProcessed_Type = Counter32
_CnAutoAttachPortDevSettingsTlvProcessed_Object = MibTableColumn
cnAutoAttachPortDevSettingsTlvProcessed = _CnAutoAttachPortDevSettingsTlvProcessed_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 10, 1, 12),
    _CnAutoAttachPortDevSettingsTlvProcessed_Type()
)
cnAutoAttachPortDevSettingsTlvProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAutoAttachPortDevSettingsTlvProcessed.setStatus("current")
_CnAutoAttachPortDevSettingsTlvAuthFails_Type = Counter32
_CnAutoAttachPortDevSettingsTlvAuthFails_Object = MibTableColumn
cnAutoAttachPortDevSettingsTlvAuthFails = _CnAutoAttachPortDevSettingsTlvAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 10, 1, 13),
    _CnAutoAttachPortDevSettingsTlvAuthFails_Type()
)
cnAutoAttachPortDevSettingsTlvAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAutoAttachPortDevSettingsTlvAuthFails.setStatus("current")


class _CnAutoAttachPortPrevPolicyName_Type(SnmpAdminString):
    """Custom type cnAutoAttachPortPrevPolicyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CnAutoAttachPortPrevPolicyName_Type.__name__ = "SnmpAdminString"
_CnAutoAttachPortPrevPolicyName_Object = MibTableColumn
cnAutoAttachPortPrevPolicyName = _CnAutoAttachPortPrevPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 10, 1, 14),
    _CnAutoAttachPortPrevPolicyName_Type()
)
cnAutoAttachPortPrevPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAutoAttachPortPrevPolicyName.setStatus("current")
_CnAutoAttachRuleTable_Object = MibTable
cnAutoAttachRuleTable = _CnAutoAttachRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 11)
)
if mibBuilder.loadTexts:
    cnAutoAttachRuleTable.setStatus("current")
_CnAutoAttachRuleEntry_Object = MibTableRow
cnAutoAttachRuleEntry = _CnAutoAttachRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 11, 1)
)
cnAutoAttachRuleEntry.setIndexNames(
    (0, "CAMBIUM-NETWORKS-AUTO-ATTACH-MIB", "cnAutoAttachRuleName"),
)
if mibBuilder.loadTexts:
    cnAutoAttachRuleEntry.setStatus("current")


class _CnAutoAttachRuleName_Type(SnmpAdminString):
    """Custom type cnAutoAttachRuleName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CnAutoAttachRuleName_Type.__name__ = "SnmpAdminString"
_CnAutoAttachRuleName_Object = MibTableColumn
cnAutoAttachRuleName = _CnAutoAttachRuleName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 11, 1, 1),
    _CnAutoAttachRuleName_Type()
)
cnAutoAttachRuleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnAutoAttachRuleName.setStatus("current")


class _CnAutoAttachRuleType_Type(Integer32):
    """Custom type cnAutoAttachRuleType based on Integer32"""
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("lldpAny", 2),
          ("lldpCapabilities", 3),
          ("lldpSystemName", 4),
          ("lldpSystemDescription", 5),
          ("lldpChassisId", 6),
          ("lldpPortId", 7),
          ("lldpPortDescription", 8),
          ("macOui", 9),
          ("macFullAddress", 10),
          ("macAddressRange", 11),
          ("lldpIpv4MgmtAddress", 12),
          ("autoVlan", 13),
          ("defaultAnyMac", 14),
          ("ifc8021x", 15),
          ("autoVoip", 16),
          ("macList", 17))
    )


_CnAutoAttachRuleType_Type.__name__ = "Integer32"
_CnAutoAttachRuleType_Object = MibTableColumn
cnAutoAttachRuleType = _CnAutoAttachRuleType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 11, 1, 2),
    _CnAutoAttachRuleType_Type()
)
cnAutoAttachRuleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAutoAttachRuleType.setStatus("current")


class _CnAutoAttachRuleDeviceData_Type(SnmpAdminString):
    """Custom type cnAutoAttachRuleDeviceData based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_CnAutoAttachRuleDeviceData_Type.__name__ = "SnmpAdminString"
_CnAutoAttachRuleDeviceData_Object = MibTableColumn
cnAutoAttachRuleDeviceData = _CnAutoAttachRuleDeviceData_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 11, 1, 3),
    _CnAutoAttachRuleDeviceData_Type()
)
cnAutoAttachRuleDeviceData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAutoAttachRuleDeviceData.setStatus("current")
_CnAutoAttachRuleRowStatus_Type = RowStatus
_CnAutoAttachRuleRowStatus_Object = MibTableColumn
cnAutoAttachRuleRowStatus = _CnAutoAttachRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 11, 1, 4),
    _CnAutoAttachRuleRowStatus_Type()
)
cnAutoAttachRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAutoAttachRuleRowStatus.setStatus("current")


class _CnAutoAttachRuleListName_Type(SnmpAdminString):
    """Custom type cnAutoAttachRuleListName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CnAutoAttachRuleListName_Type.__name__ = "SnmpAdminString"
_CnAutoAttachRuleListName_Object = MibTableColumn
cnAutoAttachRuleListName = _CnAutoAttachRuleListName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 11, 1, 5),
    _CnAutoAttachRuleListName_Type()
)
cnAutoAttachRuleListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAutoAttachRuleListName.setStatus("current")


class _CnAutoAttachRuleDataFileName_Type(SnmpAdminString):
    """Custom type cnAutoAttachRuleDataFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CnAutoAttachRuleDataFileName_Type.__name__ = "SnmpAdminString"
_CnAutoAttachRuleDataFileName_Object = MibTableColumn
cnAutoAttachRuleDataFileName = _CnAutoAttachRuleDataFileName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 11, 1, 6),
    _CnAutoAttachRuleDataFileName_Type()
)
cnAutoAttachRuleDataFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAutoAttachRuleDataFileName.setStatus("current")
_CnAutoAttachActionTable_Object = MibTable
cnAutoAttachActionTable = _CnAutoAttachActionTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 12)
)
if mibBuilder.loadTexts:
    cnAutoAttachActionTable.setStatus("current")
_CnAutoAttachActionEntry_Object = MibTableRow
cnAutoAttachActionEntry = _CnAutoAttachActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 12, 1)
)
cnAutoAttachActionEntry.setIndexNames(
    (0, "CAMBIUM-NETWORKS-AUTO-ATTACH-MIB", "cnAutoAttachActionName"),
)
if mibBuilder.loadTexts:
    cnAutoAttachActionEntry.setStatus("current")


class _CnAutoAttachActionName_Type(SnmpAdminString):
    """Custom type cnAutoAttachActionName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_CnAutoAttachActionName_Type.__name__ = "SnmpAdminString"
_CnAutoAttachActionName_Object = MibTableColumn
cnAutoAttachActionName = _CnAutoAttachActionName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 12, 1, 1),
    _CnAutoAttachActionName_Type()
)
cnAutoAttachActionName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnAutoAttachActionName.setStatus("current")


class _CnAutoAttachActionVlanData_Type(SnmpAdminString):
    """Custom type cnAutoAttachActionVlanData based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CnAutoAttachActionVlanData_Type.__name__ = "SnmpAdminString"
_CnAutoAttachActionVlanData_Object = MibTableColumn
cnAutoAttachActionVlanData = _CnAutoAttachActionVlanData_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 12, 1, 2),
    _CnAutoAttachActionVlanData_Type()
)
cnAutoAttachActionVlanData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAutoAttachActionVlanData.setStatus("current")


class _CnAutoAttachActionPvid_Type(Integer32):
    """Custom type cnAutoAttachActionPvid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_CnAutoAttachActionPvid_Type.__name__ = "Integer32"
_CnAutoAttachActionPvid_Object = MibTableColumn
cnAutoAttachActionPvid = _CnAutoAttachActionPvid_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 12, 1, 3),
    _CnAutoAttachActionPvid_Type()
)
cnAutoAttachActionPvid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAutoAttachActionPvid.setStatus("current")


class _CnAutoAttachActionPortMode_Type(Integer32):
    """Custom type cnAutoAttachActionPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("access", 2),
          ("trunk", 3),
          ("hybrid", 4))
    )


_CnAutoAttachActionPortMode_Type.__name__ = "Integer32"
_CnAutoAttachActionPortMode_Object = MibTableColumn
cnAutoAttachActionPortMode = _CnAutoAttachActionPortMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 12, 1, 4),
    _CnAutoAttachActionPortMode_Type()
)
cnAutoAttachActionPortMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAutoAttachActionPortMode.setStatus("current")
_CnAutoAttachActionRowStatus_Type = RowStatus
_CnAutoAttachActionRowStatus_Object = MibTableColumn
cnAutoAttachActionRowStatus = _CnAutoAttachActionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 12, 1, 5),
    _CnAutoAttachActionRowStatus_Type()
)
cnAutoAttachActionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAutoAttachActionRowStatus.setStatus("current")


class _CnAutoAttachActionUserPriority_Type(Integer32):
    """Custom type cnAutoAttachActionUserPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_CnAutoAttachActionUserPriority_Type.__name__ = "Integer32"
_CnAutoAttachActionUserPriority_Object = MibTableColumn
cnAutoAttachActionUserPriority = _CnAutoAttachActionUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 12, 1, 6),
    _CnAutoAttachActionUserPriority_Type()
)
cnAutoAttachActionUserPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAutoAttachActionUserPriority.setStatus("current")


class _CnAutoAttachActionQosTrust_Type(Integer32):
    """Custom type cnAutoAttachActionQosTrust based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("untrusted", 2),
          ("dot1p", 3),
          ("dscp", 4))
    )


_CnAutoAttachActionQosTrust_Type.__name__ = "Integer32"
_CnAutoAttachActionQosTrust_Object = MibTableColumn
cnAutoAttachActionQosTrust = _CnAutoAttachActionQosTrust_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 12, 1, 7),
    _CnAutoAttachActionQosTrust_Type()
)
cnAutoAttachActionQosTrust.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAutoAttachActionQosTrust.setStatus("current")


class _CnAutoAttachActionUplinkData_Type(SnmpAdminString):
    """Custom type cnAutoAttachActionUplinkData based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CnAutoAttachActionUplinkData_Type.__name__ = "SnmpAdminString"
_CnAutoAttachActionUplinkData_Object = MibTableColumn
cnAutoAttachActionUplinkData = _CnAutoAttachActionUplinkData_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 12, 1, 8),
    _CnAutoAttachActionUplinkData_Type()
)
cnAutoAttachActionUplinkData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAutoAttachActionUplinkData.setStatus("current")


class _CnAutoAttachActionPoePriority_Type(Integer32):
    """Custom type cnAutoAttachActionPoePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("critical", 2),
          ("high", 3),
          ("low", 4))
    )


_CnAutoAttachActionPoePriority_Type.__name__ = "Integer32"
_CnAutoAttachActionPoePriority_Object = MibTableColumn
cnAutoAttachActionPoePriority = _CnAutoAttachActionPoePriority_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 12, 1, 9),
    _CnAutoAttachActionPoePriority_Type()
)
cnAutoAttachActionPoePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAutoAttachActionPoePriority.setStatus("current")


class _CnAutoAttachActionPvidUpdateReset_Type(Integer32):
    """Custom type cnAutoAttachActionPvidUpdateReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_CnAutoAttachActionPvidUpdateReset_Type.__name__ = "Integer32"
_CnAutoAttachActionPvidUpdateReset_Object = MibTableColumn
cnAutoAttachActionPvidUpdateReset = _CnAutoAttachActionPvidUpdateReset_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 12, 1, 10),
    _CnAutoAttachActionPvidUpdateReset_Type()
)
cnAutoAttachActionPvidUpdateReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAutoAttachActionPvidUpdateReset.setStatus("current")


class _CnAutoAttachActionProtectedPort_Type(Integer32):
    """Custom type cnAutoAttachActionProtectedPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("enabled", 2),
          ("disabled", 3))
    )


_CnAutoAttachActionProtectedPort_Type.__name__ = "Integer32"
_CnAutoAttachActionProtectedPort_Object = MibTableColumn
cnAutoAttachActionProtectedPort = _CnAutoAttachActionProtectedPort_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 12, 1, 11),
    _CnAutoAttachActionProtectedPort_Type()
)
cnAutoAttachActionProtectedPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAutoAttachActionProtectedPort.setStatus("current")


class _CnAutoAttachActionCambiumSync_Type(Integer32):
    """Custom type cnAutoAttachActionCambiumSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("enabled", 2),
          ("disabled", 3))
    )


_CnAutoAttachActionCambiumSync_Type.__name__ = "Integer32"
_CnAutoAttachActionCambiumSync_Object = MibTableColumn
cnAutoAttachActionCambiumSync = _CnAutoAttachActionCambiumSync_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 12, 1, 12),
    _CnAutoAttachActionCambiumSync_Type()
)
cnAutoAttachActionCambiumSync.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAutoAttachActionCambiumSync.setStatus("current")


class _CnAutoAttachActionPortSpeed_Type(Integer32):
    """Custom type cnAutoAttachActionPortSpeed based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("negotiated10Mbps", 2),
          ("negotiated100Mbps", 3),
          ("negotiated1Gbps", 4),
          ("negotiated2500Mbps", 5),
          ("forced10Mbps", 6),
          ("forced100Mbps", 7),
          ("forced1Gbps", 8),
          ("forced2500Mbps", 9))
    )


_CnAutoAttachActionPortSpeed_Type.__name__ = "Integer32"
_CnAutoAttachActionPortSpeed_Object = MibTableColumn
cnAutoAttachActionPortSpeed = _CnAutoAttachActionPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 12, 1, 13),
    _CnAutoAttachActionPortSpeed_Type()
)
cnAutoAttachActionPortSpeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAutoAttachActionPortSpeed.setStatus("current")


class _CnAutoAttachActionPortAdr_Type(Integer32):
    """Custom type cnAutoAttachActionPortAdr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("enabled", 2),
          ("disabled", 3))
    )


_CnAutoAttachActionPortAdr_Type.__name__ = "Integer32"
_CnAutoAttachActionPortAdr_Object = MibTableColumn
cnAutoAttachActionPortAdr = _CnAutoAttachActionPortAdr_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 12, 1, 14),
    _CnAutoAttachActionPortAdr_Type()
)
cnAutoAttachActionPortAdr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAutoAttachActionPortAdr.setStatus("current")


class _CnAutoAttachActionAutoVoip_Type(Integer32):
    """Custom type cnAutoAttachActionAutoVoip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_CnAutoAttachActionAutoVoip_Type.__name__ = "Integer32"
_CnAutoAttachActionAutoVoip_Object = MibTableColumn
cnAutoAttachActionAutoVoip = _CnAutoAttachActionAutoVoip_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 12, 1, 15),
    _CnAutoAttachActionAutoVoip_Type()
)
cnAutoAttachActionAutoVoip.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAutoAttachActionAutoVoip.setStatus("current")
_CnAutoAttachPolicyTable_Object = MibTable
cnAutoAttachPolicyTable = _CnAutoAttachPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 13)
)
if mibBuilder.loadTexts:
    cnAutoAttachPolicyTable.setStatus("current")
_CnAutoAttachPolicyEntry_Object = MibTableRow
cnAutoAttachPolicyEntry = _CnAutoAttachPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 13, 1)
)
cnAutoAttachPolicyEntry.setIndexNames(
    (0, "CAMBIUM-NETWORKS-AUTO-ATTACH-MIB", "cnAutoAttachPolicyName"),
)
if mibBuilder.loadTexts:
    cnAutoAttachPolicyEntry.setStatus("current")


class _CnAutoAttachPolicyName_Type(SnmpAdminString):
    """Custom type cnAutoAttachPolicyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CnAutoAttachPolicyName_Type.__name__ = "SnmpAdminString"
_CnAutoAttachPolicyName_Object = MibTableColumn
cnAutoAttachPolicyName = _CnAutoAttachPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 13, 1, 1),
    _CnAutoAttachPolicyName_Type()
)
cnAutoAttachPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnAutoAttachPolicyName.setStatus("current")


class _CnAutoAttachPolicyStatus_Type(Integer32):
    """Custom type cnAutoAttachPolicyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_CnAutoAttachPolicyStatus_Type.__name__ = "Integer32"
_CnAutoAttachPolicyStatus_Object = MibTableColumn
cnAutoAttachPolicyStatus = _CnAutoAttachPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 13, 1, 2),
    _CnAutoAttachPolicyStatus_Type()
)
cnAutoAttachPolicyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAutoAttachPolicyStatus.setStatus("current")


class _CnAutoAttachPolicyPrecedence_Type(Integer32):
    """Custom type cnAutoAttachPolicyPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CnAutoAttachPolicyPrecedence_Type.__name__ = "Integer32"
_CnAutoAttachPolicyPrecedence_Object = MibTableColumn
cnAutoAttachPolicyPrecedence = _CnAutoAttachPolicyPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 13, 1, 3),
    _CnAutoAttachPolicyPrecedence_Type()
)
cnAutoAttachPolicyPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAutoAttachPolicyPrecedence.setStatus("current")


class _CnAutoAttachPolicyRuleName_Type(SnmpAdminString):
    """Custom type cnAutoAttachPolicyRuleName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CnAutoAttachPolicyRuleName_Type.__name__ = "SnmpAdminString"
_CnAutoAttachPolicyRuleName_Object = MibTableColumn
cnAutoAttachPolicyRuleName = _CnAutoAttachPolicyRuleName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 13, 1, 4),
    _CnAutoAttachPolicyRuleName_Type()
)
cnAutoAttachPolicyRuleName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAutoAttachPolicyRuleName.setStatus("current")


class _CnAutoAttachPolicyRuleType_Type(Integer32):
    """Custom type cnAutoAttachPolicyRuleType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("lldpAny", 2),
          ("lldpCapabilities", 3),
          ("lldpSystemName", 4),
          ("lldpSystemDescription", 5),
          ("lldpChassisId", 6),
          ("lldpPortId", 7),
          ("lldpPortDescription", 8),
          ("macOui", 9),
          ("macFullAddress", 10))
    )


_CnAutoAttachPolicyRuleType_Type.__name__ = "Integer32"
_CnAutoAttachPolicyRuleType_Object = MibTableColumn
cnAutoAttachPolicyRuleType = _CnAutoAttachPolicyRuleType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 13, 1, 5),
    _CnAutoAttachPolicyRuleType_Type()
)
cnAutoAttachPolicyRuleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAutoAttachPolicyRuleType.setStatus("current")


class _CnAutoAttachPolicyRuleDeviceData_Type(SnmpAdminString):
    """Custom type cnAutoAttachPolicyRuleDeviceData based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_CnAutoAttachPolicyRuleDeviceData_Type.__name__ = "SnmpAdminString"
_CnAutoAttachPolicyRuleDeviceData_Object = MibTableColumn
cnAutoAttachPolicyRuleDeviceData = _CnAutoAttachPolicyRuleDeviceData_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 13, 1, 6),
    _CnAutoAttachPolicyRuleDeviceData_Type()
)
cnAutoAttachPolicyRuleDeviceData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAutoAttachPolicyRuleDeviceData.setStatus("current")


class _CnAutoAttachPolicyActionName_Type(SnmpAdminString):
    """Custom type cnAutoAttachPolicyActionName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CnAutoAttachPolicyActionName_Type.__name__ = "SnmpAdminString"
_CnAutoAttachPolicyActionName_Object = MibTableColumn
cnAutoAttachPolicyActionName = _CnAutoAttachPolicyActionName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 13, 1, 7),
    _CnAutoAttachPolicyActionName_Type()
)
cnAutoAttachPolicyActionName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAutoAttachPolicyActionName.setStatus("current")


class _CnAutoAttachPolicyActionVlanData_Type(SnmpAdminString):
    """Custom type cnAutoAttachPolicyActionVlanData based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CnAutoAttachPolicyActionVlanData_Type.__name__ = "SnmpAdminString"
_CnAutoAttachPolicyActionVlanData_Object = MibTableColumn
cnAutoAttachPolicyActionVlanData = _CnAutoAttachPolicyActionVlanData_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 13, 1, 8),
    _CnAutoAttachPolicyActionVlanData_Type()
)
cnAutoAttachPolicyActionVlanData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAutoAttachPolicyActionVlanData.setStatus("current")


class _CnAutoAttachPolicyActionPvid_Type(Integer32):
    """Custom type cnAutoAttachPolicyActionPvid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_CnAutoAttachPolicyActionPvid_Type.__name__ = "Integer32"
_CnAutoAttachPolicyActionPvid_Object = MibTableColumn
cnAutoAttachPolicyActionPvid = _CnAutoAttachPolicyActionPvid_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 13, 1, 9),
    _CnAutoAttachPolicyActionPvid_Type()
)
cnAutoAttachPolicyActionPvid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAutoAttachPolicyActionPvid.setStatus("current")


class _CnAutoAttachPolicyActionPortMode_Type(Integer32):
    """Custom type cnAutoAttachPolicyActionPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("access", 2),
          ("trunk", 3),
          ("hybrid", 4))
    )


_CnAutoAttachPolicyActionPortMode_Type.__name__ = "Integer32"
_CnAutoAttachPolicyActionPortMode_Object = MibTableColumn
cnAutoAttachPolicyActionPortMode = _CnAutoAttachPolicyActionPortMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 13, 1, 10),
    _CnAutoAttachPolicyActionPortMode_Type()
)
cnAutoAttachPolicyActionPortMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAutoAttachPolicyActionPortMode.setStatus("current")
_CnAutoAttachPolicyApplied_Type = Counter32
_CnAutoAttachPolicyApplied_Object = MibTableColumn
cnAutoAttachPolicyApplied = _CnAutoAttachPolicyApplied_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 13, 1, 11),
    _CnAutoAttachPolicyApplied_Type()
)
cnAutoAttachPolicyApplied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAutoAttachPolicyApplied.setStatus("current")
_CnAutoAttachPolicyExpired_Type = Counter32
_CnAutoAttachPolicyExpired_Object = MibTableColumn
cnAutoAttachPolicyExpired = _CnAutoAttachPolicyExpired_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 13, 1, 12),
    _CnAutoAttachPolicyExpired_Type()
)
cnAutoAttachPolicyExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAutoAttachPolicyExpired.setStatus("current")
_CnAutoAttachPolicyErrors_Type = Counter32
_CnAutoAttachPolicyErrors_Object = MibTableColumn
cnAutoAttachPolicyErrors = _CnAutoAttachPolicyErrors_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 13, 1, 13),
    _CnAutoAttachPolicyErrors_Type()
)
cnAutoAttachPolicyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAutoAttachPolicyErrors.setStatus("current")
_CnAutoAttachPolicyRowStatus_Type = RowStatus
_CnAutoAttachPolicyRowStatus_Object = MibTableColumn
cnAutoAttachPolicyRowStatus = _CnAutoAttachPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 13, 1, 14),
    _CnAutoAttachPolicyRowStatus_Type()
)
cnAutoAttachPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAutoAttachPolicyRowStatus.setStatus("current")


class _CnAutoAttachPolicyPortList_Type(SnmpAdminString):
    """Custom type cnAutoAttachPolicyPortList based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_CnAutoAttachPolicyPortList_Type.__name__ = "SnmpAdminString"
_CnAutoAttachPolicyPortList_Object = MibTableColumn
cnAutoAttachPolicyPortList = _CnAutoAttachPolicyPortList_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 13, 1, 15),
    _CnAutoAttachPolicyPortList_Type()
)
cnAutoAttachPolicyPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAutoAttachPolicyPortList.setStatus("current")
_CnAutoAttachScriptTable_Object = MibTable
cnAutoAttachScriptTable = _CnAutoAttachScriptTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 14)
)
if mibBuilder.loadTexts:
    cnAutoAttachScriptTable.setStatus("current")
_CnAutoAttachScriptEntry_Object = MibTableRow
cnAutoAttachScriptEntry = _CnAutoAttachScriptEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 14, 1)
)
cnAutoAttachScriptEntry.setIndexNames(
    (0, "CAMBIUM-NETWORKS-AUTO-ATTACH-MIB", "cnAutoAttachScriptName"),
)
if mibBuilder.loadTexts:
    cnAutoAttachScriptEntry.setStatus("current")


class _CnAutoAttachScriptName_Type(SnmpAdminString):
    """Custom type cnAutoAttachScriptName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CnAutoAttachScriptName_Type.__name__ = "SnmpAdminString"
_CnAutoAttachScriptName_Object = MibTableColumn
cnAutoAttachScriptName = _CnAutoAttachScriptName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 14, 1, 1),
    _CnAutoAttachScriptName_Type()
)
cnAutoAttachScriptName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnAutoAttachScriptName.setStatus("current")


class _CnAutoAttachScriptActionVlanData_Type(SnmpAdminString):
    """Custom type cnAutoAttachScriptActionVlanData based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CnAutoAttachScriptActionVlanData_Type.__name__ = "SnmpAdminString"
_CnAutoAttachScriptActionVlanData_Object = MibTableColumn
cnAutoAttachScriptActionVlanData = _CnAutoAttachScriptActionVlanData_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 14, 1, 2),
    _CnAutoAttachScriptActionVlanData_Type()
)
cnAutoAttachScriptActionVlanData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAutoAttachScriptActionVlanData.setStatus("current")


class _CnAutoAttachScriptActionPvid_Type(Integer32):
    """Custom type cnAutoAttachScriptActionPvid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_CnAutoAttachScriptActionPvid_Type.__name__ = "Integer32"
_CnAutoAttachScriptActionPvid_Object = MibTableColumn
cnAutoAttachScriptActionPvid = _CnAutoAttachScriptActionPvid_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 14, 1, 3),
    _CnAutoAttachScriptActionPvid_Type()
)
cnAutoAttachScriptActionPvid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAutoAttachScriptActionPvid.setStatus("current")
_CnAutoAttachScriptRowStatus_Type = RowStatus
_CnAutoAttachScriptRowStatus_Object = MibTableColumn
cnAutoAttachScriptRowStatus = _CnAutoAttachScriptRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 14, 1, 4),
    _CnAutoAttachScriptRowStatus_Type()
)
cnAutoAttachScriptRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAutoAttachScriptRowStatus.setStatus("current")
_CnAutoAttachCondensedNbrTable_Object = MibTable
cnAutoAttachCondensedNbrTable = _CnAutoAttachCondensedNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 15)
)
if mibBuilder.loadTexts:
    cnAutoAttachCondensedNbrTable.setStatus("current")
_CnAutoAttachCondensedNbrEntry_Object = MibTableRow
cnAutoAttachCondensedNbrEntry = _CnAutoAttachCondensedNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 15, 1)
)
cnAutoAttachCondensedNbrEntry.setIndexNames(
    (0, "CAMBIUM-NETWORKS-AUTO-ATTACH-MIB", "cnAutoAttachCondensedNbrIfIndex"),
)
if mibBuilder.loadTexts:
    cnAutoAttachCondensedNbrEntry.setStatus("current")


class _CnAutoAttachCondensedNbrIfIndex_Type(Integer32):
    """Custom type cnAutoAttachCondensedNbrIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CnAutoAttachCondensedNbrIfIndex_Type.__name__ = "Integer32"
_CnAutoAttachCondensedNbrIfIndex_Object = MibTableColumn
cnAutoAttachCondensedNbrIfIndex = _CnAutoAttachCondensedNbrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 15, 1, 1),
    _CnAutoAttachCondensedNbrIfIndex_Type()
)
cnAutoAttachCondensedNbrIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnAutoAttachCondensedNbrIfIndex.setStatus("current")


class _CnAutoAttachCondensedNbrName_Type(SnmpAdminString):
    """Custom type cnAutoAttachCondensedNbrName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CnAutoAttachCondensedNbrName_Type.__name__ = "SnmpAdminString"
_CnAutoAttachCondensedNbrName_Object = MibTableColumn
cnAutoAttachCondensedNbrName = _CnAutoAttachCondensedNbrName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 15, 1, 2),
    _CnAutoAttachCondensedNbrName_Type()
)
cnAutoAttachCondensedNbrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAutoAttachCondensedNbrName.setStatus("current")


class _CnAutoAttachCondensedNbrLldpChassisId_Type(SnmpAdminString):
    """Custom type cnAutoAttachCondensedNbrLldpChassisId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CnAutoAttachCondensedNbrLldpChassisId_Type.__name__ = "SnmpAdminString"
_CnAutoAttachCondensedNbrLldpChassisId_Object = MibTableColumn
cnAutoAttachCondensedNbrLldpChassisId = _CnAutoAttachCondensedNbrLldpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 15, 1, 3),
    _CnAutoAttachCondensedNbrLldpChassisId_Type()
)
cnAutoAttachCondensedNbrLldpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAutoAttachCondensedNbrLldpChassisId.setStatus("current")


class _CnAutoAttachCondensedNbrLldpPortId_Type(SnmpAdminString):
    """Custom type cnAutoAttachCondensedNbrLldpPortId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CnAutoAttachCondensedNbrLldpPortId_Type.__name__ = "SnmpAdminString"
_CnAutoAttachCondensedNbrLldpPortId_Object = MibTableColumn
cnAutoAttachCondensedNbrLldpPortId = _CnAutoAttachCondensedNbrLldpPortId_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 15, 1, 4),
    _CnAutoAttachCondensedNbrLldpPortId_Type()
)
cnAutoAttachCondensedNbrLldpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAutoAttachCondensedNbrLldpPortId.setStatus("current")


class _CnAutoAttachCondensedNbrLldpSystemName_Type(SnmpAdminString):
    """Custom type cnAutoAttachCondensedNbrLldpSystemName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CnAutoAttachCondensedNbrLldpSystemName_Type.__name__ = "SnmpAdminString"
_CnAutoAttachCondensedNbrLldpSystemName_Object = MibTableColumn
cnAutoAttachCondensedNbrLldpSystemName = _CnAutoAttachCondensedNbrLldpSystemName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 15, 1, 5),
    _CnAutoAttachCondensedNbrLldpSystemName_Type()
)
cnAutoAttachCondensedNbrLldpSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAutoAttachCondensedNbrLldpSystemName.setStatus("current")


class _CnAutoAttachCondensedNbrLldpSystemDesc_Type(SnmpAdminString):
    """Custom type cnAutoAttachCondensedNbrLldpSystemDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CnAutoAttachCondensedNbrLldpSystemDesc_Type.__name__ = "SnmpAdminString"
_CnAutoAttachCondensedNbrLldpSystemDesc_Object = MibTableColumn
cnAutoAttachCondensedNbrLldpSystemDesc = _CnAutoAttachCondensedNbrLldpSystemDesc_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 15, 1, 6),
    _CnAutoAttachCondensedNbrLldpSystemDesc_Type()
)
cnAutoAttachCondensedNbrLldpSystemDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAutoAttachCondensedNbrLldpSystemDesc.setStatus("current")


class _CnAutoAttachCondensedNbrLldpMgmtIpv4Addr_Type(SnmpAdminString):
    """Custom type cnAutoAttachCondensedNbrLldpMgmtIpv4Addr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CnAutoAttachCondensedNbrLldpMgmtIpv4Addr_Type.__name__ = "SnmpAdminString"
_CnAutoAttachCondensedNbrLldpMgmtIpv4Addr_Object = MibTableColumn
cnAutoAttachCondensedNbrLldpMgmtIpv4Addr = _CnAutoAttachCondensedNbrLldpMgmtIpv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 15, 1, 7),
    _CnAutoAttachCondensedNbrLldpMgmtIpv4Addr_Type()
)
cnAutoAttachCondensedNbrLldpMgmtIpv4Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAutoAttachCondensedNbrLldpMgmtIpv4Addr.setStatus("current")


class _CnAutoAttachCondensedNbrMacAddress_Type(OctetString):
    """Custom type cnAutoAttachCondensedNbrMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(17, 17),
    )


_CnAutoAttachCondensedNbrMacAddress_Type.__name__ = "OctetString"
_CnAutoAttachCondensedNbrMacAddress_Object = MibTableColumn
cnAutoAttachCondensedNbrMacAddress = _CnAutoAttachCondensedNbrMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 15, 1, 8),
    _CnAutoAttachCondensedNbrMacAddress_Type()
)
cnAutoAttachCondensedNbrMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAutoAttachCondensedNbrMacAddress.setStatus("current")


class _CnAutoAttachCondensedNbrClassification_Type(SnmpAdminString):
    """Custom type cnAutoAttachCondensedNbrClassification based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CnAutoAttachCondensedNbrClassification_Type.__name__ = "SnmpAdminString"
_CnAutoAttachCondensedNbrClassification_Object = MibTableColumn
cnAutoAttachCondensedNbrClassification = _CnAutoAttachCondensedNbrClassification_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 15, 1, 9),
    _CnAutoAttachCondensedNbrClassification_Type()
)
cnAutoAttachCondensedNbrClassification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAutoAttachCondensedNbrClassification.setStatus("current")


class _CnAutoAttachGlobalUplinkData_Type(SnmpAdminString):
    """Custom type cnAutoAttachGlobalUplinkData based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CnAutoAttachGlobalUplinkData_Type.__name__ = "SnmpAdminString"
_CnAutoAttachGlobalUplinkData_Object = MibScalar
cnAutoAttachGlobalUplinkData = _CnAutoAttachGlobalUplinkData_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 16),
    _CnAutoAttachGlobalUplinkData_Type()
)
cnAutoAttachGlobalUplinkData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAutoAttachGlobalUplinkData.setStatus("current")


class _CnAutoAttachAutoVlanStatus_Type(Integer32):
    """Custom type cnAutoAttachAutoVlanStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_CnAutoAttachAutoVlanStatus_Type.__name__ = "Integer32"
_CnAutoAttachAutoVlanStatus_Object = MibScalar
cnAutoAttachAutoVlanStatus = _CnAutoAttachAutoVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 17),
    _CnAutoAttachAutoVlanStatus_Type()
)
cnAutoAttachAutoVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAutoAttachAutoVlanStatus.setStatus("current")
_CnAutoAttachNbrClassTable_Object = MibTable
cnAutoAttachNbrClassTable = _CnAutoAttachNbrClassTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 18)
)
if mibBuilder.loadTexts:
    cnAutoAttachNbrClassTable.setStatus("current")
_CnAutoAttachNbrClassEntry_Object = MibTableRow
cnAutoAttachNbrClassEntry = _CnAutoAttachNbrClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 18, 1)
)
cnAutoAttachNbrClassEntry.setIndexNames(
    (0, "CAMBIUM-NETWORKS-AUTO-ATTACH-MIB", "cnAutoAttachNbrClassType"),
    (0, "CAMBIUM-NETWORKS-AUTO-ATTACH-MIB", "cnAutoAttachNbrClassIdentifier"),
)
if mibBuilder.loadTexts:
    cnAutoAttachNbrClassEntry.setStatus("current")


class _CnAutoAttachNbrClassType_Type(Integer32):
    """Custom type cnAutoAttachNbrClassType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("bridge", 2),
          ("ap", 3),
          ("router", 4),
          ("phone", 5),
          ("radio", 6),
          ("camera", 7),
          ("cambium", 8),
          ("cambiumCnMatrix", 9),
          ("cambiumCnPilot", 10))
    )


_CnAutoAttachNbrClassType_Type.__name__ = "Integer32"
_CnAutoAttachNbrClassType_Object = MibTableColumn
cnAutoAttachNbrClassType = _CnAutoAttachNbrClassType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 18, 1, 1),
    _CnAutoAttachNbrClassType_Type()
)
cnAutoAttachNbrClassType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnAutoAttachNbrClassType.setStatus("current")


class _CnAutoAttachNbrClassIdentifier_Type(SnmpAdminString):
    """Custom type cnAutoAttachNbrClassIdentifier based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CnAutoAttachNbrClassIdentifier_Type.__name__ = "SnmpAdminString"
_CnAutoAttachNbrClassIdentifier_Object = MibTableColumn
cnAutoAttachNbrClassIdentifier = _CnAutoAttachNbrClassIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 18, 1, 2),
    _CnAutoAttachNbrClassIdentifier_Type()
)
cnAutoAttachNbrClassIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnAutoAttachNbrClassIdentifier.setStatus("current")


class _CnAutoAttachNbrClassIdentifierType_Type(Integer32):
    """Custom type cnAutoAttachNbrClassIdentifierType based on Integer32"""
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
        *(("lldp", 1),
          ("macOui", 2),
          ("macAddress", 3))
    )


_CnAutoAttachNbrClassIdentifierType_Type.__name__ = "Integer32"
_CnAutoAttachNbrClassIdentifierType_Object = MibTableColumn
cnAutoAttachNbrClassIdentifierType = _CnAutoAttachNbrClassIdentifierType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 18, 1, 3),
    _CnAutoAttachNbrClassIdentifierType_Type()
)
cnAutoAttachNbrClassIdentifierType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAutoAttachNbrClassIdentifierType.setStatus("current")
_CnAutoAttachNbrClassStorageType_Type = StorageType
_CnAutoAttachNbrClassStorageType_Object = MibTableColumn
cnAutoAttachNbrClassStorageType = _CnAutoAttachNbrClassStorageType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 18, 1, 4),
    _CnAutoAttachNbrClassStorageType_Type()
)
cnAutoAttachNbrClassStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAutoAttachNbrClassStorageType.setStatus("current")
_CnAutoAttachNbrClassRowStatus_Type = RowStatus
_CnAutoAttachNbrClassRowStatus_Object = MibTableColumn
cnAutoAttachNbrClassRowStatus = _CnAutoAttachNbrClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 18, 1, 5),
    _CnAutoAttachNbrClassRowStatus_Type()
)
cnAutoAttachNbrClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAutoAttachNbrClassRowStatus.setStatus("current")


class _CnAutoAttachDeviceLocalization_Type(SnmpAdminString):
    """Custom type cnAutoAttachDeviceLocalization based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CnAutoAttachDeviceLocalization_Type.__name__ = "SnmpAdminString"
_CnAutoAttachDeviceLocalization_Object = MibScalar
cnAutoAttachDeviceLocalization = _CnAutoAttachDeviceLocalization_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 19),
    _CnAutoAttachDeviceLocalization_Type()
)
cnAutoAttachDeviceLocalization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAutoAttachDeviceLocalization.setStatus("current")
_CnAutoAttachMacListFileTable_Object = MibTable
cnAutoAttachMacListFileTable = _CnAutoAttachMacListFileTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 20)
)
if mibBuilder.loadTexts:
    cnAutoAttachMacListFileTable.setStatus("current")
_CnAutoAttachMacListFileEntry_Object = MibTableRow
cnAutoAttachMacListFileEntry = _CnAutoAttachMacListFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 20, 1)
)
cnAutoAttachMacListFileEntry.setIndexNames(
    (0, "CAMBIUM-NETWORKS-AUTO-ATTACH-MIB", "cnAutoAttachMacListFileName"),
)
if mibBuilder.loadTexts:
    cnAutoAttachMacListFileEntry.setStatus("current")


class _CnAutoAttachMacListFileName_Type(SnmpAdminString):
    """Custom type cnAutoAttachMacListFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CnAutoAttachMacListFileName_Type.__name__ = "SnmpAdminString"
_CnAutoAttachMacListFileName_Object = MibTableColumn
cnAutoAttachMacListFileName = _CnAutoAttachMacListFileName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 20, 1, 1),
    _CnAutoAttachMacListFileName_Type()
)
cnAutoAttachMacListFileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnAutoAttachMacListFileName.setStatus("current")


class _CnAutoAttachMacListFileMacCount_Type(Integer32):
    """Custom type cnAutoAttachMacListFileMacCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CnAutoAttachMacListFileMacCount_Type.__name__ = "Integer32"
_CnAutoAttachMacListFileMacCount_Object = MibTableColumn
cnAutoAttachMacListFileMacCount = _CnAutoAttachMacListFileMacCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 20, 1, 2),
    _CnAutoAttachMacListFileMacCount_Type()
)
cnAutoAttachMacListFileMacCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAutoAttachMacListFileMacCount.setStatus("current")


class _CnAutoAttachMacListFileStatus_Type(Integer32):
    """Custom type cnAutoAttachMacListFileStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("pendingDownload", 2),
          ("downloading", 3),
          ("downloaded", 4),
          ("failedDownload", 5))
    )


_CnAutoAttachMacListFileStatus_Type.__name__ = "Integer32"
_CnAutoAttachMacListFileStatus_Object = MibTableColumn
cnAutoAttachMacListFileStatus = _CnAutoAttachMacListFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 20, 1, 3),
    _CnAutoAttachMacListFileStatus_Type()
)
cnAutoAttachMacListFileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAutoAttachMacListFileStatus.setStatus("current")


class _CnAutoAttachMacListFileRefresh_Type(Integer32):
    """Custom type cnAutoAttachMacListFileRefresh based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_CnAutoAttachMacListFileRefresh_Type.__name__ = "Integer32"
_CnAutoAttachMacListFileRefresh_Object = MibTableColumn
cnAutoAttachMacListFileRefresh = _CnAutoAttachMacListFileRefresh_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 20, 1, 4),
    _CnAutoAttachMacListFileRefresh_Type()
)
cnAutoAttachMacListFileRefresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAutoAttachMacListFileRefresh.setStatus("current")
_CnAutoAttachMacListFileRowStatus_Type = RowStatus
_CnAutoAttachMacListFileRowStatus_Object = MibTableColumn
cnAutoAttachMacListFileRowStatus = _CnAutoAttachMacListFileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 20, 1, 5),
    _CnAutoAttachMacListFileRowStatus_Type()
)
cnAutoAttachMacListFileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnAutoAttachMacListFileRowStatus.setStatus("current")


class _CnAutoAttachFileDownloadType_Type(Integer32):
    """Custom type cnAutoAttachFileDownloadType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("macListFile", 1)
    )


_CnAutoAttachFileDownloadType_Type.__name__ = "Integer32"
_CnAutoAttachFileDownloadType_Object = MibScalar
cnAutoAttachFileDownloadType = _CnAutoAttachFileDownloadType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 21),
    _CnAutoAttachFileDownloadType_Type()
)
cnAutoAttachFileDownloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAutoAttachFileDownloadType.setStatus("current")


class _CnAutoAttachFileDownloadPath_Type(SnmpAdminString):
    """Custom type cnAutoAttachFileDownloadPath based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CnAutoAttachFileDownloadPath_Type.__name__ = "SnmpAdminString"
_CnAutoAttachFileDownloadPath_Object = MibScalar
cnAutoAttachFileDownloadPath = _CnAutoAttachFileDownloadPath_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 22),
    _CnAutoAttachFileDownloadPath_Type()
)
cnAutoAttachFileDownloadPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAutoAttachFileDownloadPath.setStatus("current")


class _CnAutoAttachFileDownloadTransferMode_Type(Integer32):
    """Custom type cnAutoAttachFileDownloadTransferMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5)
        )
    )
    namedValues = NamedValues(
        *(("tftp", 1),
          ("sftp", 2),
          ("scp", 5))
    )


_CnAutoAttachFileDownloadTransferMode_Type.__name__ = "Integer32"
_CnAutoAttachFileDownloadTransferMode_Object = MibScalar
cnAutoAttachFileDownloadTransferMode = _CnAutoAttachFileDownloadTransferMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 23),
    _CnAutoAttachFileDownloadTransferMode_Type()
)
cnAutoAttachFileDownloadTransferMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAutoAttachFileDownloadTransferMode.setStatus("current")
_CnAutoAttachFileDownloadFromIpAddrType_Type = InetAddressType
_CnAutoAttachFileDownloadFromIpAddrType_Object = MibScalar
cnAutoAttachFileDownloadFromIpAddrType = _CnAutoAttachFileDownloadFromIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 24),
    _CnAutoAttachFileDownloadFromIpAddrType_Type()
)
cnAutoAttachFileDownloadFromIpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAutoAttachFileDownloadFromIpAddrType.setStatus("current")
_CnAutoAttachFileDownloadFromIpvx_Type = InetAddress
_CnAutoAttachFileDownloadFromIpvx_Object = MibScalar
cnAutoAttachFileDownloadFromIpvx = _CnAutoAttachFileDownloadFromIpvx_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 25),
    _CnAutoAttachFileDownloadFromIpvx_Type()
)
cnAutoAttachFileDownloadFromIpvx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAutoAttachFileDownloadFromIpvx.setStatus("current")


class _CnAutoAttachFileDownloadUsername_Type(SnmpAdminString):
    """Custom type cnAutoAttachFileDownloadUsername based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CnAutoAttachFileDownloadUsername_Type.__name__ = "SnmpAdminString"
_CnAutoAttachFileDownloadUsername_Object = MibScalar
cnAutoAttachFileDownloadUsername = _CnAutoAttachFileDownloadUsername_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 26),
    _CnAutoAttachFileDownloadUsername_Type()
)
cnAutoAttachFileDownloadUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAutoAttachFileDownloadUsername.setStatus("current")


class _CnAutoAttachFileDownloadPassword_Type(SnmpAdminString):
    """Custom type cnAutoAttachFileDownloadPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CnAutoAttachFileDownloadPassword_Type.__name__ = "SnmpAdminString"
_CnAutoAttachFileDownloadPassword_Object = MibScalar
cnAutoAttachFileDownloadPassword = _CnAutoAttachFileDownloadPassword_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 1, 27),
    _CnAutoAttachFileDownloadPassword_Type()
)
cnAutoAttachFileDownloadPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAutoAttachFileDownloadPassword.setStatus("current")
_CnAutoAttachNotifyObjects_ObjectIdentity = ObjectIdentity
cnAutoAttachNotifyObjects = _CnAutoAttachNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 2)
)


class _CnAutoAttachRemoteElemSysDescr_Type(SnmpAdminString):
    """Custom type cnAutoAttachRemoteElemSysDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CnAutoAttachRemoteElemSysDescr_Type.__name__ = "SnmpAdminString"
_CnAutoAttachRemoteElemSysDescr_Object = MibScalar
cnAutoAttachRemoteElemSysDescr = _CnAutoAttachRemoteElemSysDescr_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 2, 1),
    _CnAutoAttachRemoteElemSysDescr_Type()
)
cnAutoAttachRemoteElemSysDescr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnAutoAttachRemoteElemSysDescr.setStatus("current")
_CnAutoAttachRemoteElemMgmtOid_Type = ObjectIdentifier
_CnAutoAttachRemoteElemMgmtOid_Object = MibScalar
cnAutoAttachRemoteElemMgmtOid = _CnAutoAttachRemoteElemMgmtOid_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 2, 2),
    _CnAutoAttachRemoteElemMgmtOid_Type()
)
cnAutoAttachRemoteElemMgmtOid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnAutoAttachRemoteElemMgmtOid.setStatus("current")

# Managed Objects groups


# Notification objects

cnAutoAttachInterfacePolicyApplied = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 0, 1)
)
cnAutoAttachInterfacePolicyApplied.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CAMBIUM-NETWORKS-AUTO-ATTACH-MIB", "cnAutoAttachPortActivePolicyName"),
        ("CAMBIUM-NETWORKS-AUTO-ATTACH-MIB", "cnAutoAttachRemoteElemSysDescr"),
        ("CAMBIUM-NETWORKS-AUTO-ATTACH-MIB", "cnAutoAttachRemoteElemMgmtOid"))
)
if mibBuilder.loadTexts:
    cnAutoAttachInterfacePolicyApplied.setStatus(
        "current"
    )

cnAutoAttachInterfacePolicyExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 24, 1, 0, 2)
)
cnAutoAttachInterfacePolicyExpired.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CAMBIUM-NETWORKS-AUTO-ATTACH-MIB", "cnAutoAttachPortActivePolicyName"))
)
if mibBuilder.loadTexts:
    cnAutoAttachInterfacePolicyExpired.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CAMBIUM-NETWORKS-AUTO-ATTACH-MIB",
    **{"cambium": cambium,
       "cnMatrix": cnMatrix,
       "cnAutoAttachMib": cnAutoAttachMib,
       "cnAutoAttachNotifications": cnAutoAttachNotifications,
       "cnAutoAttachInterfacePolicyApplied": cnAutoAttachInterfacePolicyApplied,
       "cnAutoAttachInterfacePolicyExpired": cnAutoAttachInterfacePolicyExpired,
       "cnAutoAttachObjects": cnAutoAttachObjects,
       "cnAutoAttachService": cnAutoAttachService,
       "cnAutoAttachDataDiffAllowed": cnAutoAttachDataDiffAllowed,
       "cnAutoAttachDeviceDataCompare": cnAutoAttachDeviceDataCompare,
       "cnAutoAttachClearPolicyStats": cnAutoAttachClearPolicyStats,
       "cnAutoAttachClearInterfaceStats": cnAutoAttachClearInterfaceStats,
       "cnAutoAttachUpdatePortDesc": cnAutoAttachUpdatePortDesc,
       "cnAutoAttachRestrictedMacMatch": cnAutoAttachRestrictedMacMatch,
       "cnAutoAttachActivePolicyReorder": cnAutoAttachActivePolicyReorder,
       "cnAutoAttachMacPolicyAging": cnAutoAttachMacPolicyAging,
       "cnAutoAttachPortTable": cnAutoAttachPortTable,
       "cnAutoAttachPortEntry": cnAutoAttachPortEntry,
       "cnAutoAttachPortIfIndex": cnAutoAttachPortIfIndex,
       "cnAutoAttachPortState": cnAutoAttachPortState,
       "cnAutoAttachPortMsgAuthStatus": cnAutoAttachPortMsgAuthStatus,
       "cnAutoAttachPortMsgAuthKey": cnAutoAttachPortMsgAuthKey,
       "cnAutoAttachPortActivePolicyName": cnAutoAttachPortActivePolicyName,
       "cnAutoAttachPortPolicyApplied": cnAutoAttachPortPolicyApplied,
       "cnAutoAttachPortPolicyExpired": cnAutoAttachPortPolicyExpired,
       "cnAutoAttachPortPolicyErrors": cnAutoAttachPortPolicyErrors,
       "cnAutoAttachPortRowStatus": cnAutoAttachPortRowStatus,
       "cnAutoAttachPortTlvTxEnable": cnAutoAttachPortTlvTxEnable,
       "cnAutoAttachPortDevSettingsTlvReceived": cnAutoAttachPortDevSettingsTlvReceived,
       "cnAutoAttachPortDevSettingsTlvProcessed": cnAutoAttachPortDevSettingsTlvProcessed,
       "cnAutoAttachPortDevSettingsTlvAuthFails": cnAutoAttachPortDevSettingsTlvAuthFails,
       "cnAutoAttachPortPrevPolicyName": cnAutoAttachPortPrevPolicyName,
       "cnAutoAttachRuleTable": cnAutoAttachRuleTable,
       "cnAutoAttachRuleEntry": cnAutoAttachRuleEntry,
       "cnAutoAttachRuleName": cnAutoAttachRuleName,
       "cnAutoAttachRuleType": cnAutoAttachRuleType,
       "cnAutoAttachRuleDeviceData": cnAutoAttachRuleDeviceData,
       "cnAutoAttachRuleRowStatus": cnAutoAttachRuleRowStatus,
       "cnAutoAttachRuleListName": cnAutoAttachRuleListName,
       "cnAutoAttachRuleDataFileName": cnAutoAttachRuleDataFileName,
       "cnAutoAttachActionTable": cnAutoAttachActionTable,
       "cnAutoAttachActionEntry": cnAutoAttachActionEntry,
       "cnAutoAttachActionName": cnAutoAttachActionName,
       "cnAutoAttachActionVlanData": cnAutoAttachActionVlanData,
       "cnAutoAttachActionPvid": cnAutoAttachActionPvid,
       "cnAutoAttachActionPortMode": cnAutoAttachActionPortMode,
       "cnAutoAttachActionRowStatus": cnAutoAttachActionRowStatus,
       "cnAutoAttachActionUserPriority": cnAutoAttachActionUserPriority,
       "cnAutoAttachActionQosTrust": cnAutoAttachActionQosTrust,
       "cnAutoAttachActionUplinkData": cnAutoAttachActionUplinkData,
       "cnAutoAttachActionPoePriority": cnAutoAttachActionPoePriority,
       "cnAutoAttachActionPvidUpdateReset": cnAutoAttachActionPvidUpdateReset,
       "cnAutoAttachActionProtectedPort": cnAutoAttachActionProtectedPort,
       "cnAutoAttachActionCambiumSync": cnAutoAttachActionCambiumSync,
       "cnAutoAttachActionPortSpeed": cnAutoAttachActionPortSpeed,
       "cnAutoAttachActionPortAdr": cnAutoAttachActionPortAdr,
       "cnAutoAttachActionAutoVoip": cnAutoAttachActionAutoVoip,
       "cnAutoAttachPolicyTable": cnAutoAttachPolicyTable,
       "cnAutoAttachPolicyEntry": cnAutoAttachPolicyEntry,
       "cnAutoAttachPolicyName": cnAutoAttachPolicyName,
       "cnAutoAttachPolicyStatus": cnAutoAttachPolicyStatus,
       "cnAutoAttachPolicyPrecedence": cnAutoAttachPolicyPrecedence,
       "cnAutoAttachPolicyRuleName": cnAutoAttachPolicyRuleName,
       "cnAutoAttachPolicyRuleType": cnAutoAttachPolicyRuleType,
       "cnAutoAttachPolicyRuleDeviceData": cnAutoAttachPolicyRuleDeviceData,
       "cnAutoAttachPolicyActionName": cnAutoAttachPolicyActionName,
       "cnAutoAttachPolicyActionVlanData": cnAutoAttachPolicyActionVlanData,
       "cnAutoAttachPolicyActionPvid": cnAutoAttachPolicyActionPvid,
       "cnAutoAttachPolicyActionPortMode": cnAutoAttachPolicyActionPortMode,
       "cnAutoAttachPolicyApplied": cnAutoAttachPolicyApplied,
       "cnAutoAttachPolicyExpired": cnAutoAttachPolicyExpired,
       "cnAutoAttachPolicyErrors": cnAutoAttachPolicyErrors,
       "cnAutoAttachPolicyRowStatus": cnAutoAttachPolicyRowStatus,
       "cnAutoAttachPolicyPortList": cnAutoAttachPolicyPortList,
       "cnAutoAttachScriptTable": cnAutoAttachScriptTable,
       "cnAutoAttachScriptEntry": cnAutoAttachScriptEntry,
       "cnAutoAttachScriptName": cnAutoAttachScriptName,
       "cnAutoAttachScriptActionVlanData": cnAutoAttachScriptActionVlanData,
       "cnAutoAttachScriptActionPvid": cnAutoAttachScriptActionPvid,
       "cnAutoAttachScriptRowStatus": cnAutoAttachScriptRowStatus,
       "cnAutoAttachCondensedNbrTable": cnAutoAttachCondensedNbrTable,
       "cnAutoAttachCondensedNbrEntry": cnAutoAttachCondensedNbrEntry,
       "cnAutoAttachCondensedNbrIfIndex": cnAutoAttachCondensedNbrIfIndex,
       "cnAutoAttachCondensedNbrName": cnAutoAttachCondensedNbrName,
       "cnAutoAttachCondensedNbrLldpChassisId": cnAutoAttachCondensedNbrLldpChassisId,
       "cnAutoAttachCondensedNbrLldpPortId": cnAutoAttachCondensedNbrLldpPortId,
       "cnAutoAttachCondensedNbrLldpSystemName": cnAutoAttachCondensedNbrLldpSystemName,
       "cnAutoAttachCondensedNbrLldpSystemDesc": cnAutoAttachCondensedNbrLldpSystemDesc,
       "cnAutoAttachCondensedNbrLldpMgmtIpv4Addr": cnAutoAttachCondensedNbrLldpMgmtIpv4Addr,
       "cnAutoAttachCondensedNbrMacAddress": cnAutoAttachCondensedNbrMacAddress,
       "cnAutoAttachCondensedNbrClassification": cnAutoAttachCondensedNbrClassification,
       "cnAutoAttachGlobalUplinkData": cnAutoAttachGlobalUplinkData,
       "cnAutoAttachAutoVlanStatus": cnAutoAttachAutoVlanStatus,
       "cnAutoAttachNbrClassTable": cnAutoAttachNbrClassTable,
       "cnAutoAttachNbrClassEntry": cnAutoAttachNbrClassEntry,
       "cnAutoAttachNbrClassType": cnAutoAttachNbrClassType,
       "cnAutoAttachNbrClassIdentifier": cnAutoAttachNbrClassIdentifier,
       "cnAutoAttachNbrClassIdentifierType": cnAutoAttachNbrClassIdentifierType,
       "cnAutoAttachNbrClassStorageType": cnAutoAttachNbrClassStorageType,
       "cnAutoAttachNbrClassRowStatus": cnAutoAttachNbrClassRowStatus,
       "cnAutoAttachDeviceLocalization": cnAutoAttachDeviceLocalization,
       "cnAutoAttachMacListFileTable": cnAutoAttachMacListFileTable,
       "cnAutoAttachMacListFileEntry": cnAutoAttachMacListFileEntry,
       "cnAutoAttachMacListFileName": cnAutoAttachMacListFileName,
       "cnAutoAttachMacListFileMacCount": cnAutoAttachMacListFileMacCount,
       "cnAutoAttachMacListFileStatus": cnAutoAttachMacListFileStatus,
       "cnAutoAttachMacListFileRefresh": cnAutoAttachMacListFileRefresh,
       "cnAutoAttachMacListFileRowStatus": cnAutoAttachMacListFileRowStatus,
       "cnAutoAttachFileDownloadType": cnAutoAttachFileDownloadType,
       "cnAutoAttachFileDownloadPath": cnAutoAttachFileDownloadPath,
       "cnAutoAttachFileDownloadTransferMode": cnAutoAttachFileDownloadTransferMode,
       "cnAutoAttachFileDownloadFromIpAddrType": cnAutoAttachFileDownloadFromIpAddrType,
       "cnAutoAttachFileDownloadFromIpvx": cnAutoAttachFileDownloadFromIpvx,
       "cnAutoAttachFileDownloadUsername": cnAutoAttachFileDownloadUsername,
       "cnAutoAttachFileDownloadPassword": cnAutoAttachFileDownloadPassword,
       "cnAutoAttachNotifyObjects": cnAutoAttachNotifyObjects,
       "cnAutoAttachRemoteElemSysDescr": cnAutoAttachRemoteElemSysDescr,
       "cnAutoAttachRemoteElemMgmtOid": cnAutoAttachRemoteElemMgmtOid}
)
