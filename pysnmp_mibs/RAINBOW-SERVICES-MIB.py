# SNMP MIB module (RAINBOW-SERVICES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/alvarion/RAINBOW-SERVICES-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:07:13 2025
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

(rainbow,) = mibBuilder.importSymbols(
    "RAINBOW-MIB",
    "rainbow")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

rainbowServices = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100)
)
if mibBuilder.loadTexts:
    rainbowServices.setRevisions(
        ("2006-06-06 15:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RainbowServiceType(TextualConvention, Integer32):
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
        *(("rbLayerII", 1),
          ("rbPPPoE", 2),
          ("rbVoIP", 3))
    )



# MIB Managed Objects in the order of their OIDs

_RbServiceGeneralConfig_ObjectIdentity = ObjectIdentity
rbServiceGeneralConfig = _RbServiceGeneralConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 1)
)
_RbGetNewPolicyRuleID_Type = Unsigned32
_RbGetNewPolicyRuleID_Object = MibScalar
rbGetNewPolicyRuleID = _RbGetNewPolicyRuleID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 1, 1),
    _RbGetNewPolicyRuleID_Type()
)
rbGetNewPolicyRuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbGetNewPolicyRuleID.setStatus("current")
_RbGetNewServiceID_Type = Unsigned32
_RbGetNewServiceID_Object = MibScalar
rbGetNewServiceID = _RbGetNewServiceID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 1, 2),
    _RbGetNewServiceID_Type()
)
rbGetNewServiceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbGetNewServiceID.setStatus("current")
_RbGetNewServiceTemplateID_Type = Unsigned32
_RbGetNewServiceTemplateID_Object = MibScalar
rbGetNewServiceTemplateID = _RbGetNewServiceTemplateID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 1, 3),
    _RbGetNewServiceTemplateID_Type()
)
rbGetNewServiceTemplateID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbGetNewServiceTemplateID.setStatus("current")
_RbGetNewSubscriberID_Type = Unsigned32
_RbGetNewSubscriberID_Object = MibScalar
rbGetNewSubscriberID = _RbGetNewSubscriberID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 1, 4),
    _RbGetNewSubscriberID_Type()
)
rbGetNewSubscriberID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbGetNewSubscriberID.setStatus("current")
_RbGetNewQoSProfileID_Type = Unsigned32
_RbGetNewQoSProfileID_Object = MibScalar
rbGetNewQoSProfileID = _RbGetNewQoSProfileID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 1, 5),
    _RbGetNewQoSProfileID_Type()
)
rbGetNewQoSProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbGetNewQoSProfileID.setStatus("current")
_RbGetNewForwardingRuleID_Type = Unsigned32
_RbGetNewForwardingRuleID_Object = MibScalar
rbGetNewForwardingRuleID = _RbGetNewForwardingRuleID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 1, 6),
    _RbGetNewForwardingRuleID_Type()
)
rbGetNewForwardingRuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbGetNewForwardingRuleID.setStatus("current")


class _RbServiceWorkingMode_Type(Integer32):
    """Custom type rbServiceWorkingMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("professionalMode", 1),
          ("lightMode", 2))
    )


_RbServiceWorkingMode_Type.__name__ = "Integer32"
_RbServiceWorkingMode_Object = MibScalar
rbServiceWorkingMode = _RbServiceWorkingMode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 1, 7),
    _RbServiceWorkingMode_Type()
)
rbServiceWorkingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbServiceWorkingMode.setStatus("current")
_RbDfltServiceTemplateTable_Object = MibTable
rbDfltServiceTemplateTable = _RbDfltServiceTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 1, 8)
)
if mibBuilder.loadTexts:
    rbDfltServiceTemplateTable.setStatus("current")
_RbDfltServiceTemplateEntry_Object = MibTableRow
rbDfltServiceTemplateEntry = _RbDfltServiceTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 1, 8, 1)
)
rbDfltServiceTemplateEntry.setIndexNames(
    (0, "RAINBOW-SERVICES-MIB", "rbDfltServiceTemplateType"),
)
if mibBuilder.loadTexts:
    rbDfltServiceTemplateEntry.setStatus("current")
_RbDfltServiceTemplateType_Type = RainbowServiceType
_RbDfltServiceTemplateType_Object = MibTableColumn
rbDfltServiceTemplateType = _RbDfltServiceTemplateType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 1, 8, 1, 1),
    _RbDfltServiceTemplateType_Type()
)
rbDfltServiceTemplateType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbDfltServiceTemplateType.setStatus("current")
_RbDfltServiceTemplateIdx_Type = Unsigned32
_RbDfltServiceTemplateIdx_Object = MibTableColumn
rbDfltServiceTemplateIdx = _RbDfltServiceTemplateIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 1, 8, 1, 2),
    _RbDfltServiceTemplateIdx_Type()
)
rbDfltServiceTemplateIdx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbDfltServiceTemplateIdx.setStatus("current")
_RbServiceTemplate_ObjectIdentity = ObjectIdentity
rbServiceTemplate = _RbServiceTemplate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 2)
)
_RbServiceTemplateConfigTable_Object = MibTable
rbServiceTemplateConfigTable = _RbServiceTemplateConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 2, 1)
)
if mibBuilder.loadTexts:
    rbServiceTemplateConfigTable.setStatus("current")
_RbServiceTemplateConfigEntry_Object = MibTableRow
rbServiceTemplateConfigEntry = _RbServiceTemplateConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 2, 1, 1)
)
rbServiceTemplateConfigEntry.setIndexNames(
    (0, "RAINBOW-SERVICES-MIB", "rbServiceTemplateType"),
    (0, "RAINBOW-SERVICES-MIB", "rbServiceTemplateIdx"),
)
if mibBuilder.loadTexts:
    rbServiceTemplateConfigEntry.setStatus("current")
_RbServiceTemplateType_Type = RainbowServiceType
_RbServiceTemplateType_Object = MibTableColumn
rbServiceTemplateType = _RbServiceTemplateType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 2, 1, 1, 1),
    _RbServiceTemplateType_Type()
)
rbServiceTemplateType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbServiceTemplateType.setStatus("current")
_RbServiceTemplateIdx_Type = Unsigned32
_RbServiceTemplateIdx_Object = MibTableColumn
rbServiceTemplateIdx = _RbServiceTemplateIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 2, 1, 1, 2),
    _RbServiceTemplateIdx_Type()
)
rbServiceTemplateIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbServiceTemplateIdx.setStatus("current")


class _RbServiceTemplateName_Type(DisplayString):
    """Custom type rbServiceTemplateName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RbServiceTemplateName_Type.__name__ = "DisplayString"
_RbServiceTemplateName_Object = MibTableColumn
rbServiceTemplateName = _RbServiceTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 2, 1, 1, 3),
    _RbServiceTemplateName_Type()
)
rbServiceTemplateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbServiceTemplateName.setStatus("current")
_RbServiceTemplateID_Type = Unsigned32
_RbServiceTemplateID_Object = MibTableColumn
rbServiceTemplateID = _RbServiceTemplateID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 2, 1, 1, 4),
    _RbServiceTemplateID_Type()
)
rbServiceTemplateID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbServiceTemplateID.setStatus("current")
_RbServiceTemplateBaseVLAN_Type = Integer32
_RbServiceTemplateBaseVLAN_Object = MibTableColumn
rbServiceTemplateBaseVLAN = _RbServiceTemplateBaseVLAN_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 2, 1, 1, 5),
    _RbServiceTemplateBaseVLAN_Type()
)
rbServiceTemplateBaseVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbServiceTemplateBaseVLAN.setStatus("current")
_RbServiceTemplateBaseSignallingVLAN_Type = Integer32
_RbServiceTemplateBaseSignallingVLAN_Object = MibTableColumn
rbServiceTemplateBaseSignallingVLAN = _RbServiceTemplateBaseSignallingVLAN_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 2, 1, 1, 6),
    _RbServiceTemplateBaseSignallingVLAN_Type()
)
rbServiceTemplateBaseSignallingVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbServiceTemplateBaseSignallingVLAN.setStatus("current")
_RbServiceTemplateBaseDhcpVLAN_Type = Integer32
_RbServiceTemplateBaseDhcpVLAN_Object = MibTableColumn
rbServiceTemplateBaseDhcpVLAN = _RbServiceTemplateBaseDhcpVLAN_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 2, 1, 1, 7),
    _RbServiceTemplateBaseDhcpVLAN_Type()
)
rbServiceTemplateBaseDhcpVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbServiceTemplateBaseDhcpVLAN.setStatus("current")


class _RbServiceTemplateForwardDhcpRequest_Type(Integer32):
    """Custom type rbServiceTemplateForwardDhcpRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RbServiceTemplateForwardDhcpRequest_Type.__name__ = "Integer32"
_RbServiceTemplateForwardDhcpRequest_Object = MibTableColumn
rbServiceTemplateForwardDhcpRequest = _RbServiceTemplateForwardDhcpRequest_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 2, 1, 1, 8),
    _RbServiceTemplateForwardDhcpRequest_Type()
)
rbServiceTemplateForwardDhcpRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbServiceTemplateForwardDhcpRequest.setStatus("current")


class _RbServiceTemplateNumberOfSimultaneousCalls_Type(Integer32):
    """Custom type rbServiceTemplateNumberOfSimultaneousCalls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_RbServiceTemplateNumberOfSimultaneousCalls_Type.__name__ = "Integer32"
_RbServiceTemplateNumberOfSimultaneousCalls_Object = MibTableColumn
rbServiceTemplateNumberOfSimultaneousCalls = _RbServiceTemplateNumberOfSimultaneousCalls_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 2, 1, 1, 9),
    _RbServiceTemplateNumberOfSimultaneousCalls_Type()
)
rbServiceTemplateNumberOfSimultaneousCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbServiceTemplateNumberOfSimultaneousCalls.setStatus("current")
_RbServiceTemplatePolicyRuleIdx_Type = Unsigned32
_RbServiceTemplatePolicyRuleIdx_Object = MibTableColumn
rbServiceTemplatePolicyRuleIdx = _RbServiceTemplatePolicyRuleIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 2, 1, 1, 10),
    _RbServiceTemplatePolicyRuleIdx_Type()
)
rbServiceTemplatePolicyRuleIdx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbServiceTemplatePolicyRuleIdx.setStatus("current")


class _RbServiceTemplatePolicyRuleName_Type(DisplayString):
    """Custom type rbServiceTemplatePolicyRuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RbServiceTemplatePolicyRuleName_Type.__name__ = "DisplayString"
_RbServiceTemplatePolicyRuleName_Object = MibTableColumn
rbServiceTemplatePolicyRuleName = _RbServiceTemplatePolicyRuleName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 2, 1, 1, 11),
    _RbServiceTemplatePolicyRuleName_Type()
)
rbServiceTemplatePolicyRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbServiceTemplatePolicyRuleName.setStatus("current")
_RbServiceTemplateForwardingRuleIdx_Type = Unsigned32
_RbServiceTemplateForwardingRuleIdx_Object = MibTableColumn
rbServiceTemplateForwardingRuleIdx = _RbServiceTemplateForwardingRuleIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 2, 1, 1, 12),
    _RbServiceTemplateForwardingRuleIdx_Type()
)
rbServiceTemplateForwardingRuleIdx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbServiceTemplateForwardingRuleIdx.setStatus("current")


class _RbServiceTemplateForwardingRuleName_Type(DisplayString):
    """Custom type rbServiceTemplateForwardingRuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RbServiceTemplateForwardingRuleName_Type.__name__ = "DisplayString"
_RbServiceTemplateForwardingRuleName_Object = MibTableColumn
rbServiceTemplateForwardingRuleName = _RbServiceTemplateForwardingRuleName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 2, 1, 1, 13),
    _RbServiceTemplateForwardingRuleName_Type()
)
rbServiceTemplateForwardingRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbServiceTemplateForwardingRuleName.setStatus("current")
_RbAServiceTemplateRowStatus_Type = RowStatus
_RbAServiceTemplateRowStatus_Object = MibTableColumn
rbAServiceTemplateRowStatus = _RbAServiceTemplateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 2, 1, 1, 14),
    _RbAServiceTemplateRowStatus_Type()
)
rbAServiceTemplateRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAServiceTemplateRowStatus.setStatus("current")


class _RbServiceTemplateQoSMarkingMode_Type(Integer32):
    """Custom type rbServiceTemplateQoSMarkingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("transparent", 1),
          ("rb8021p", 2),
          ("rbDSCP", 3))
    )


_RbServiceTemplateQoSMarkingMode_Type.__name__ = "Integer32"
_RbServiceTemplateQoSMarkingMode_Object = MibTableColumn
rbServiceTemplateQoSMarkingMode = _RbServiceTemplateQoSMarkingMode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 2, 1, 1, 15),
    _RbServiceTemplateQoSMarkingMode_Type()
)
rbServiceTemplateQoSMarkingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbServiceTemplateQoSMarkingMode.setStatus("current")
_RbServiceTemplateQoSMarkingValue_Type = Integer32
_RbServiceTemplateQoSMarkingValue_Object = MibTableColumn
rbServiceTemplateQoSMarkingValue = _RbServiceTemplateQoSMarkingValue_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 2, 1, 1, 16),
    _RbServiceTemplateQoSMarkingValue_Type()
)
rbServiceTemplateQoSMarkingValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbServiceTemplateQoSMarkingValue.setStatus("current")


class _RbServiceTemplateVLANTransparencyMode_Type(Integer32):
    """Custom type rbServiceTemplateVLANTransparencyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RbServiceTemplateVLANTransparencyMode_Type.__name__ = "Integer32"
_RbServiceTemplateVLANTransparencyMode_Object = MibTableColumn
rbServiceTemplateVLANTransparencyMode = _RbServiceTemplateVLANTransparencyMode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 2, 1, 1, 17),
    _RbServiceTemplateVLANTransparencyMode_Type()
)
rbServiceTemplateVLANTransparencyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbServiceTemplateVLANTransparencyMode.setStatus("current")


class _RbServiceTemplateClass_Type(Integer32):
    """Custom type rbServiceTemplateClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("global", 2))
    )


_RbServiceTemplateClass_Type.__name__ = "Integer32"
_RbServiceTemplateClass_Object = MibTableColumn
rbServiceTemplateClass = _RbServiceTemplateClass_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 2, 1, 1, 18),
    _RbServiceTemplateClass_Type()
)
rbServiceTemplateClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbServiceTemplateClass.setStatus("deprecated")
_RbServices_ObjectIdentity = ObjectIdentity
rbServices = _RbServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 3)
)
_RbServiceConfigTable_Object = MibTable
rbServiceConfigTable = _RbServiceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 3, 1)
)
if mibBuilder.loadTexts:
    rbServiceConfigTable.setStatus("deprecated")
_RbServiceConfigEntry_Object = MibTableRow
rbServiceConfigEntry = _RbServiceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 3, 1, 1)
)
rbServiceConfigEntry.setIndexNames(
    (0, "RAINBOW-SERVICES-MIB", "rbSubscriberIdx"),
    (0, "RAINBOW-SERVICES-MIB", "rbServiceIdx"),
)
if mibBuilder.loadTexts:
    rbServiceConfigEntry.setStatus("deprecated")
_RbServiceIdx_Type = Unsigned32
_RbServiceIdx_Object = MibTableColumn
rbServiceIdx = _RbServiceIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 3, 1, 1, 1),
    _RbServiceIdx_Type()
)
rbServiceIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbServiceIdx.setStatus("deprecated")
_RbServiceType_Type = RainbowServiceType
_RbServiceType_Object = MibTableColumn
rbServiceType = _RbServiceType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 3, 1, 1, 2),
    _RbServiceType_Type()
)
rbServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbServiceType.setStatus("deprecated")


class _RbServiceName_Type(DisplayString):
    """Custom type rbServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RbServiceName_Type.__name__ = "DisplayString"
_RbServiceName_Object = MibTableColumn
rbServiceName = _RbServiceName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 3, 1, 1, 3),
    _RbServiceName_Type()
)
rbServiceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbServiceName.setStatus("deprecated")
_RbServiceID_Type = Unsigned32
_RbServiceID_Object = MibTableColumn
rbServiceID = _RbServiceID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 3, 1, 1, 4),
    _RbServiceID_Type()
)
rbServiceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbServiceID.setStatus("deprecated")
_RbServiceServiceTemplateIdx_Type = Unsigned32
_RbServiceServiceTemplateIdx_Object = MibTableColumn
rbServiceServiceTemplateIdx = _RbServiceServiceTemplateIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 3, 1, 1, 5),
    _RbServiceServiceTemplateIdx_Type()
)
rbServiceServiceTemplateIdx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbServiceServiceTemplateIdx.setStatus("deprecated")


class _RbServiceServiceTemplateName_Type(DisplayString):
    """Custom type rbServiceServiceTemplateName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RbServiceServiceTemplateName_Type.__name__ = "DisplayString"
_RbServiceServiceTemplateName_Object = MibTableColumn
rbServiceServiceTemplateName = _RbServiceServiceTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 3, 1, 1, 6),
    _RbServiceServiceTemplateName_Type()
)
rbServiceServiceTemplateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbServiceServiceTemplateName.setStatus("deprecated")
_RbServiceServiceTemplateID_Type = Unsigned32
_RbServiceServiceTemplateID_Object = MibTableColumn
rbServiceServiceTemplateID = _RbServiceServiceTemplateID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 3, 1, 1, 7),
    _RbServiceServiceTemplateID_Type()
)
rbServiceServiceTemplateID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbServiceServiceTemplateID.setStatus("deprecated")
_RbServiceSwitchingGroupIdx_Type = Unsigned32
_RbServiceSwitchingGroupIdx_Object = MibTableColumn
rbServiceSwitchingGroupIdx = _RbServiceSwitchingGroupIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 3, 1, 1, 8),
    _RbServiceSwitchingGroupIdx_Type()
)
rbServiceSwitchingGroupIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbServiceSwitchingGroupIdx.setStatus("deprecated")


class _RbServiceAdminStatus_Type(Integer32):
    """Custom type rbServiceAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RbServiceAdminStatus_Type.__name__ = "Integer32"
_RbServiceAdminStatus_Object = MibTableColumn
rbServiceAdminStatus = _RbServiceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 3, 1, 1, 9),
    _RbServiceAdminStatus_Type()
)
rbServiceAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbServiceAdminStatus.setStatus("deprecated")


class _RbServiceOperStatus_Type(Integer32):
    """Custom type rbServiceOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("unknown", 3))
    )


_RbServiceOperStatus_Type.__name__ = "Integer32"
_RbServiceOperStatus_Object = MibTableColumn
rbServiceOperStatus = _RbServiceOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 3, 1, 1, 10),
    _RbServiceOperStatus_Type()
)
rbServiceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbServiceOperStatus.setStatus("deprecated")
_RbAServiceRowStatus_Type = RowStatus
_RbAServiceRowStatus_Object = MibTableColumn
rbAServiceRowStatus = _RbAServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 3, 1, 1, 11),
    _RbAServiceRowStatus_Type()
)
rbAServiceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAServiceRowStatus.setStatus("deprecated")


class _RbServiceClientSiteVLANList_Type(OctetString):
    """Custom type rbServiceClientSiteVLANList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_RbServiceClientSiteVLANList_Type.__name__ = "OctetString"
_RbServiceClientSiteVLANList_Object = MibTableColumn
rbServiceClientSiteVLANList = _RbServiceClientSiteVLANList_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 3, 1, 1, 12),
    _RbServiceClientSiteVLANList_Type()
)
rbServiceClientSiteVLANList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbServiceClientSiteVLANList.setStatus("deprecated")
_RbServiceClientSiteVLANListCount_Type = Integer32
_RbServiceClientSiteVLANListCount_Object = MibTableColumn
rbServiceClientSiteVLANListCount = _RbServiceClientSiteVLANListCount_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 3, 1, 1, 13),
    _RbServiceClientSiteVLANListCount_Type()
)
rbServiceClientSiteVLANListCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbServiceClientSiteVLANListCount.setStatus("deprecated")
_RbServiceSuMacAddress_Type = MacAddress
_RbServiceSuMacAddress_Object = MibTableColumn
rbServiceSuMacAddress = _RbServiceSuMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 3, 1, 1, 14),
    _RbServiceSuMacAddress_Type()
)
rbServiceSuMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbServiceSuMacAddress.setStatus("deprecated")
_RbServiceAUSlotNumber_Type = Integer32
_RbServiceAUSlotNumber_Object = MibTableColumn
rbServiceAUSlotNumber = _RbServiceAUSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 3, 1, 1, 15),
    _RbServiceAUSlotNumber_Type()
)
rbServiceAUSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbServiceAUSlotNumber.setStatus("deprecated")


class _RbServiceVLANHybridMode_Type(Integer32):
    """Custom type rbServiceVLANHybridMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RbServiceVLANHybridMode_Type.__name__ = "Integer32"
_RbServiceVLANHybridMode_Object = MibTableColumn
rbServiceVLANHybridMode = _RbServiceVLANHybridMode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 3, 1, 1, 16),
    _RbServiceVLANHybridMode_Type()
)
rbServiceVLANHybridMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbServiceVLANHybridMode.setStatus("deprecated")


class _RbServiceVLANClassificationMode_Type(Integer32):
    """Custom type rbServiceVLANClassificationMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_RbServiceVLANClassificationMode_Type.__name__ = "Integer32"
_RbServiceVLANClassificationMode_Object = MibTableColumn
rbServiceVLANClassificationMode = _RbServiceVLANClassificationMode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 3, 1, 1, 17),
    _RbServiceVLANClassificationMode_Type()
)
rbServiceVLANClassificationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbServiceVLANClassificationMode.setStatus("deprecated")


class _RbServiceAccessVLAN_Type(Integer32):
    """Custom type rbServiceAccessVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_RbServiceAccessVLAN_Type.__name__ = "Integer32"
_RbServiceAccessVLAN_Object = MibTableColumn
rbServiceAccessVLAN = _RbServiceAccessVLAN_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 3, 1, 1, 18),
    _RbServiceAccessVLAN_Type()
)
rbServiceAccessVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbServiceAccessVLAN.setStatus("deprecated")
_RbSuServiceConfigTable_Object = MibTable
rbSuServiceConfigTable = _RbSuServiceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 3, 2)
)
if mibBuilder.loadTexts:
    rbSuServiceConfigTable.setStatus("current")
_RbSuServiceConfigEntry_Object = MibTableRow
rbSuServiceConfigEntry = _RbSuServiceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 3, 2, 1)
)
rbSuServiceConfigEntry.setIndexNames(
    (0, "RAINBOW-SERVICES-MIB", "rbSuServiceMacAddress"),
    (0, "RAINBOW-SERVICES-MIB", "rbSuServiceIdx"),
)
if mibBuilder.loadTexts:
    rbSuServiceConfigEntry.setStatus("current")
_RbSuServiceMacAddress_Type = MacAddress
_RbSuServiceMacAddress_Object = MibTableColumn
rbSuServiceMacAddress = _RbSuServiceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 3, 2, 1, 1),
    _RbSuServiceMacAddress_Type()
)
rbSuServiceMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuServiceMacAddress.setStatus("current")
_RbSuServiceIdx_Type = Unsigned32
_RbSuServiceIdx_Object = MibTableColumn
rbSuServiceIdx = _RbSuServiceIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 3, 2, 1, 2),
    _RbSuServiceIdx_Type()
)
rbSuServiceIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuServiceIdx.setStatus("current")
_RbSuServiceRbType_Type = RainbowServiceType
_RbSuServiceRbType_Object = MibTableColumn
rbSuServiceRbType = _RbSuServiceRbType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 3, 2, 1, 3),
    _RbSuServiceRbType_Type()
)
rbSuServiceRbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuServiceRbType.setStatus("current")


class _RbSuServiceName_Type(DisplayString):
    """Custom type rbSuServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RbSuServiceName_Type.__name__ = "DisplayString"
_RbSuServiceName_Object = MibTableColumn
rbSuServiceName = _RbSuServiceName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 3, 2, 1, 4),
    _RbSuServiceName_Type()
)
rbSuServiceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSuServiceName.setStatus("current")
_RbSuServiceID_Type = Unsigned32
_RbSuServiceID_Object = MibTableColumn
rbSuServiceID = _RbSuServiceID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 3, 2, 1, 5),
    _RbSuServiceID_Type()
)
rbSuServiceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuServiceID.setStatus("current")
_RbSuSubscriberIdx_Type = Unsigned32
_RbSuSubscriberIdx_Object = MibTableColumn
rbSuSubscriberIdx = _RbSuSubscriberIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 3, 2, 1, 6),
    _RbSuSubscriberIdx_Type()
)
rbSuSubscriberIdx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSuSubscriberIdx.setStatus("current")
_RbSuServiceTemplateIdx_Type = Unsigned32
_RbSuServiceTemplateIdx_Object = MibTableColumn
rbSuServiceTemplateIdx = _RbSuServiceTemplateIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 3, 2, 1, 7),
    _RbSuServiceTemplateIdx_Type()
)
rbSuServiceTemplateIdx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSuServiceTemplateIdx.setStatus("current")


class _RbSuServiceTemplateName_Type(DisplayString):
    """Custom type rbSuServiceTemplateName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RbSuServiceTemplateName_Type.__name__ = "DisplayString"
_RbSuServiceTemplateName_Object = MibTableColumn
rbSuServiceTemplateName = _RbSuServiceTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 3, 2, 1, 8),
    _RbSuServiceTemplateName_Type()
)
rbSuServiceTemplateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuServiceTemplateName.setStatus("current")
_RbSuServiceTemplateID_Type = Unsigned32
_RbSuServiceTemplateID_Object = MibTableColumn
rbSuServiceTemplateID = _RbSuServiceTemplateID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 3, 2, 1, 9),
    _RbSuServiceTemplateID_Type()
)
rbSuServiceTemplateID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuServiceTemplateID.setStatus("current")
_RbSuServiceSwitchingGroupIdx_Type = Unsigned32
_RbSuServiceSwitchingGroupIdx_Object = MibTableColumn
rbSuServiceSwitchingGroupIdx = _RbSuServiceSwitchingGroupIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 3, 2, 1, 10),
    _RbSuServiceSwitchingGroupIdx_Type()
)
rbSuServiceSwitchingGroupIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuServiceSwitchingGroupIdx.setStatus("current")


class _RbSuServiceAdminStatus_Type(Integer32):
    """Custom type rbSuServiceAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RbSuServiceAdminStatus_Type.__name__ = "Integer32"
_RbSuServiceAdminStatus_Object = MibTableColumn
rbSuServiceAdminStatus = _RbSuServiceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 3, 2, 1, 11),
    _RbSuServiceAdminStatus_Type()
)
rbSuServiceAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSuServiceAdminStatus.setStatus("current")


class _RbSuServiceOperStatus_Type(Integer32):
    """Custom type rbSuServiceOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("unknown", 3))
    )


_RbSuServiceOperStatus_Type.__name__ = "Integer32"
_RbSuServiceOperStatus_Object = MibTableColumn
rbSuServiceOperStatus = _RbSuServiceOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 3, 2, 1, 12),
    _RbSuServiceOperStatus_Type()
)
rbSuServiceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuServiceOperStatus.setStatus("current")


class _RbSuServiceClientSiteVLANList_Type(OctetString):
    """Custom type rbSuServiceClientSiteVLANList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_RbSuServiceClientSiteVLANList_Type.__name__ = "OctetString"
_RbSuServiceClientSiteVLANList_Object = MibTableColumn
rbSuServiceClientSiteVLANList = _RbSuServiceClientSiteVLANList_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 3, 2, 1, 13),
    _RbSuServiceClientSiteVLANList_Type()
)
rbSuServiceClientSiteVLANList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSuServiceClientSiteVLANList.setStatus("current")
_RbSuServiceClientSiteVLANListCount_Type = Integer32
_RbSuServiceClientSiteVLANListCount_Object = MibTableColumn
rbSuServiceClientSiteVLANListCount = _RbSuServiceClientSiteVLANListCount_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 3, 2, 1, 14),
    _RbSuServiceClientSiteVLANListCount_Type()
)
rbSuServiceClientSiteVLANListCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSuServiceClientSiteVLANListCount.setStatus("current")
_RbSuServiceAUSlotNumber_Type = Integer32
_RbSuServiceAUSlotNumber_Object = MibTableColumn
rbSuServiceAUSlotNumber = _RbSuServiceAUSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 3, 2, 1, 15),
    _RbSuServiceAUSlotNumber_Type()
)
rbSuServiceAUSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuServiceAUSlotNumber.setStatus("current")


class _RbSuServiceVLANHybridMode_Type(Integer32):
    """Custom type rbSuServiceVLANHybridMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RbSuServiceVLANHybridMode_Type.__name__ = "Integer32"
_RbSuServiceVLANHybridMode_Object = MibTableColumn
rbSuServiceVLANHybridMode = _RbSuServiceVLANHybridMode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 3, 2, 1, 16),
    _RbSuServiceVLANHybridMode_Type()
)
rbSuServiceVLANHybridMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSuServiceVLANHybridMode.setStatus("current")


class _RbSuServiceVLANClassificationMode_Type(Integer32):
    """Custom type rbSuServiceVLANClassificationMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_RbSuServiceVLANClassificationMode_Type.__name__ = "Integer32"
_RbSuServiceVLANClassificationMode_Object = MibTableColumn
rbSuServiceVLANClassificationMode = _RbSuServiceVLANClassificationMode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 3, 2, 1, 17),
    _RbSuServiceVLANClassificationMode_Type()
)
rbSuServiceVLANClassificationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSuServiceVLANClassificationMode.setStatus("current")


class _RbSuServiceAccessVLAN_Type(Integer32):
    """Custom type rbSuServiceAccessVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_RbSuServiceAccessVLAN_Type.__name__ = "Integer32"
_RbSuServiceAccessVLAN_Object = MibTableColumn
rbSuServiceAccessVLAN = _RbSuServiceAccessVLAN_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 3, 2, 1, 18),
    _RbSuServiceAccessVLAN_Type()
)
rbSuServiceAccessVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSuServiceAccessVLAN.setStatus("current")
_RbSuServiceRowStatus_Type = RowStatus
_RbSuServiceRowStatus_Object = MibTableColumn
rbSuServiceRowStatus = _RbSuServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 3, 2, 1, 19),
    _RbSuServiceRowStatus_Type()
)
rbSuServiceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSuServiceRowStatus.setStatus("current")
_RbSuMappingTable_Object = MibTable
rbSuMappingTable = _RbSuMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 3, 3)
)
if mibBuilder.loadTexts:
    rbSuMappingTable.setStatus("current")
_RbSuMappingEntry_Object = MibTableRow
rbSuMappingEntry = _RbSuMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 3, 3, 1)
)
rbSuMappingEntry.setIndexNames(
    (0, "RAINBOW-SERVICES-MIB", "rbSuMappingSysName"),
)
if mibBuilder.loadTexts:
    rbSuMappingEntry.setStatus("current")


class _RbSuMappingSysName_Type(DisplayString):
    """Custom type rbSuMappingSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RbSuMappingSysName_Type.__name__ = "DisplayString"
_RbSuMappingSysName_Object = MibTableColumn
rbSuMappingSysName = _RbSuMappingSysName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 3, 3, 1, 1),
    _RbSuMappingSysName_Type()
)
rbSuMappingSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuMappingSysName.setStatus("current")
_RbSuMappingMacAddress_Type = MacAddress
_RbSuMappingMacAddress_Object = MibTableColumn
rbSuMappingMacAddress = _RbSuMappingMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 3, 3, 1, 2),
    _RbSuMappingMacAddress_Type()
)
rbSuMappingMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuMappingMacAddress.setStatus("current")
_RbQoSProfiles_ObjectIdentity = ObjectIdentity
rbQoSProfiles = _RbQoSProfiles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 4)
)
_RbQoSProfileConfigTable_Object = MibTable
rbQoSProfileConfigTable = _RbQoSProfileConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 4, 1)
)
if mibBuilder.loadTexts:
    rbQoSProfileConfigTable.setStatus("current")
_RbQoSProfileConfigEntry_Object = MibTableRow
rbQoSProfileConfigEntry = _RbQoSProfileConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 4, 1, 1)
)
rbQoSProfileConfigEntry.setIndexNames(
    (0, "RAINBOW-SERVICES-MIB", "rbQoSProfileIdx"),
)
if mibBuilder.loadTexts:
    rbQoSProfileConfigEntry.setStatus("current")
_RbQoSProfileIdx_Type = Unsigned32
_RbQoSProfileIdx_Object = MibTableColumn
rbQoSProfileIdx = _RbQoSProfileIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 4, 1, 1, 1),
    _RbQoSProfileIdx_Type()
)
rbQoSProfileIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbQoSProfileIdx.setStatus("current")


class _RbQoSProfileName_Type(DisplayString):
    """Custom type rbQoSProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RbQoSProfileName_Type.__name__ = "DisplayString"
_RbQoSProfileName_Object = MibTableColumn
rbQoSProfileName = _RbQoSProfileName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 4, 1, 1, 2),
    _RbQoSProfileName_Type()
)
rbQoSProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbQoSProfileName.setStatus("current")
_RbQoSProfileID_Type = Unsigned32
_RbQoSProfileID_Object = MibTableColumn
rbQoSProfileID = _RbQoSProfileID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 4, 1, 1, 3),
    _RbQoSProfileID_Type()
)
rbQoSProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbQoSProfileID.setStatus("current")


class _RbQoSProfileType_Type(Integer32):
    """Custom type rbQoSProfileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rbCG", 0),
          ("rbRT", 1),
          ("rbNRT", 2),
          ("rbBE", 3))
    )


_RbQoSProfileType_Type.__name__ = "Integer32"
_RbQoSProfileType_Object = MibTableColumn
rbQoSProfileType = _RbQoSProfileType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 4, 1, 1, 4),
    _RbQoSProfileType_Type()
)
rbQoSProfileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbQoSProfileType.setStatus("current")
_RbQoSProfileParam1_Type = Unsigned32
_RbQoSProfileParam1_Object = MibTableColumn
rbQoSProfileParam1 = _RbQoSProfileParam1_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 4, 1, 1, 5),
    _RbQoSProfileParam1_Type()
)
rbQoSProfileParam1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbQoSProfileParam1.setStatus("current")
_RbQoSProfileParam2_Type = Unsigned32
_RbQoSProfileParam2_Object = MibTableColumn
rbQoSProfileParam2 = _RbQoSProfileParam2_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 4, 1, 1, 6),
    _RbQoSProfileParam2_Type()
)
rbQoSProfileParam2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbQoSProfileParam2.setStatus("current")


class _RbQoSProfileParamTime_Type(Integer32):
    """Custom type rbQoSProfileParamTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("short", 1),
          ("medium", 2),
          ("long", 3))
    )


_RbQoSProfileParamTime_Type.__name__ = "Integer32"
_RbQoSProfileParamTime_Object = MibTableColumn
rbQoSProfileParamTime = _RbQoSProfileParamTime_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 4, 1, 1, 7),
    _RbQoSProfileParamTime_Type()
)
rbQoSProfileParamTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbQoSProfileParamTime.setStatus("current")
_RbAQoSProfileRowStatus_Type = RowStatus
_RbAQoSProfileRowStatus_Object = MibTableColumn
rbAQoSProfileRowStatus = _RbAQoSProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 4, 1, 1, 8),
    _RbAQoSProfileRowStatus_Type()
)
rbAQoSProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAQoSProfileRowStatus.setStatus("current")


class _RbQoSProfileClass_Type(Integer32):
    """Custom type rbQoSProfileClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("global", 2))
    )


_RbQoSProfileClass_Type.__name__ = "Integer32"
_RbQoSProfileClass_Object = MibTableColumn
rbQoSProfileClass = _RbQoSProfileClass_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 4, 1, 1, 9),
    _RbQoSProfileClass_Type()
)
rbQoSProfileClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbQoSProfileClass.setStatus("current")
_RbPolicyRules_ObjectIdentity = ObjectIdentity
rbPolicyRules = _RbPolicyRules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 5)
)
_RbPolicyRuleConfigTable_Object = MibTable
rbPolicyRuleConfigTable = _RbPolicyRuleConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 5, 1)
)
if mibBuilder.loadTexts:
    rbPolicyRuleConfigTable.setStatus("current")
_RbPolicyRuleConfigEntry_Object = MibTableRow
rbPolicyRuleConfigEntry = _RbPolicyRuleConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 5, 1, 1)
)
rbPolicyRuleConfigEntry.setIndexNames(
    (0, "RAINBOW-SERVICES-MIB", "rbPolicyRuleIdx"),
)
if mibBuilder.loadTexts:
    rbPolicyRuleConfigEntry.setStatus("current")
_RbPolicyRuleIdx_Type = Unsigned32
_RbPolicyRuleIdx_Object = MibTableColumn
rbPolicyRuleIdx = _RbPolicyRuleIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 5, 1, 1, 1),
    _RbPolicyRuleIdx_Type()
)
rbPolicyRuleIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPolicyRuleIdx.setStatus("current")


class _RbPolicyRuleName_Type(DisplayString):
    """Custom type rbPolicyRuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RbPolicyRuleName_Type.__name__ = "DisplayString"
_RbPolicyRuleName_Object = MibTableColumn
rbPolicyRuleName = _RbPolicyRuleName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 5, 1, 1, 2),
    _RbPolicyRuleName_Type()
)
rbPolicyRuleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbPolicyRuleName.setStatus("current")
_RbPolicyRuleID_Type = Unsigned32
_RbPolicyRuleID_Object = MibTableColumn
rbPolicyRuleID = _RbPolicyRuleID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 5, 1, 1, 3),
    _RbPolicyRuleID_Type()
)
rbPolicyRuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPolicyRuleID.setStatus("current")


class _RbPolicyRulePriorityType_Type(Integer32):
    """Custom type rbPolicyRulePriorityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rbDSCP", 1),
          ("rb8021p", 2))
    )


_RbPolicyRulePriorityType_Type.__name__ = "Integer32"
_RbPolicyRulePriorityType_Object = MibTableColumn
rbPolicyRulePriorityType = _RbPolicyRulePriorityType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 5, 1, 1, 4),
    _RbPolicyRulePriorityType_Type()
)
rbPolicyRulePriorityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbPolicyRulePriorityType.setStatus("current")
_RbPolicyRuleUpQoSProfileIdx1_Type = Unsigned32
_RbPolicyRuleUpQoSProfileIdx1_Object = MibTableColumn
rbPolicyRuleUpQoSProfileIdx1 = _RbPolicyRuleUpQoSProfileIdx1_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 5, 1, 1, 6),
    _RbPolicyRuleUpQoSProfileIdx1_Type()
)
rbPolicyRuleUpQoSProfileIdx1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbPolicyRuleUpQoSProfileIdx1.setStatus("current")
_RbPolicyRuleUpQoSUpperLimit1_Type = Unsigned32
_RbPolicyRuleUpQoSUpperLimit1_Object = MibTableColumn
rbPolicyRuleUpQoSUpperLimit1 = _RbPolicyRuleUpQoSUpperLimit1_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 5, 1, 1, 7),
    _RbPolicyRuleUpQoSUpperLimit1_Type()
)
rbPolicyRuleUpQoSUpperLimit1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbPolicyRuleUpQoSUpperLimit1.setStatus("current")
_RbPolicyRuleUpQoSProfileIdx2_Type = Unsigned32
_RbPolicyRuleUpQoSProfileIdx2_Object = MibTableColumn
rbPolicyRuleUpQoSProfileIdx2 = _RbPolicyRuleUpQoSProfileIdx2_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 5, 1, 1, 9),
    _RbPolicyRuleUpQoSProfileIdx2_Type()
)
rbPolicyRuleUpQoSProfileIdx2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbPolicyRuleUpQoSProfileIdx2.setStatus("current")
_RbPolicyRuleUpQoSUpperLimit2_Type = Unsigned32
_RbPolicyRuleUpQoSUpperLimit2_Object = MibTableColumn
rbPolicyRuleUpQoSUpperLimit2 = _RbPolicyRuleUpQoSUpperLimit2_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 5, 1, 1, 10),
    _RbPolicyRuleUpQoSUpperLimit2_Type()
)
rbPolicyRuleUpQoSUpperLimit2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbPolicyRuleUpQoSUpperLimit2.setStatus("current")
_RbPolicyRuleUpQoSProfileIdx3_Type = Unsigned32
_RbPolicyRuleUpQoSProfileIdx3_Object = MibTableColumn
rbPolicyRuleUpQoSProfileIdx3 = _RbPolicyRuleUpQoSProfileIdx3_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 5, 1, 1, 12),
    _RbPolicyRuleUpQoSProfileIdx3_Type()
)
rbPolicyRuleUpQoSProfileIdx3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbPolicyRuleUpQoSProfileIdx3.setStatus("current")
_RbPolicyRuleUpQoSUpperLimit3_Type = Unsigned32
_RbPolicyRuleUpQoSUpperLimit3_Object = MibTableColumn
rbPolicyRuleUpQoSUpperLimit3 = _RbPolicyRuleUpQoSUpperLimit3_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 5, 1, 1, 13),
    _RbPolicyRuleUpQoSUpperLimit3_Type()
)
rbPolicyRuleUpQoSUpperLimit3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbPolicyRuleUpQoSUpperLimit3.setStatus("current")
_RbPolicyRuleUpQoSProfileIdx4_Type = Unsigned32
_RbPolicyRuleUpQoSProfileIdx4_Object = MibTableColumn
rbPolicyRuleUpQoSProfileIdx4 = _RbPolicyRuleUpQoSProfileIdx4_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 5, 1, 1, 15),
    _RbPolicyRuleUpQoSProfileIdx4_Type()
)
rbPolicyRuleUpQoSProfileIdx4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbPolicyRuleUpQoSProfileIdx4.setStatus("current")
_RbPolicyRuleUpQoSUpperLimit4_Type = Unsigned32
_RbPolicyRuleUpQoSUpperLimit4_Object = MibTableColumn
rbPolicyRuleUpQoSUpperLimit4 = _RbPolicyRuleUpQoSUpperLimit4_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 5, 1, 1, 16),
    _RbPolicyRuleUpQoSUpperLimit4_Type()
)
rbPolicyRuleUpQoSUpperLimit4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbPolicyRuleUpQoSUpperLimit4.setStatus("current")
_RbPolicyRuleDownQoSProfileIdx1_Type = Unsigned32
_RbPolicyRuleDownQoSProfileIdx1_Object = MibTableColumn
rbPolicyRuleDownQoSProfileIdx1 = _RbPolicyRuleDownQoSProfileIdx1_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 5, 1, 1, 18),
    _RbPolicyRuleDownQoSProfileIdx1_Type()
)
rbPolicyRuleDownQoSProfileIdx1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbPolicyRuleDownQoSProfileIdx1.setStatus("current")
_RbPolicyRuleDownQoSUpperLimit1_Type = Unsigned32
_RbPolicyRuleDownQoSUpperLimit1_Object = MibTableColumn
rbPolicyRuleDownQoSUpperLimit1 = _RbPolicyRuleDownQoSUpperLimit1_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 5, 1, 1, 19),
    _RbPolicyRuleDownQoSUpperLimit1_Type()
)
rbPolicyRuleDownQoSUpperLimit1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbPolicyRuleDownQoSUpperLimit1.setStatus("current")
_RbPolicyRuleDownQoSProfileIdx2_Type = Unsigned32
_RbPolicyRuleDownQoSProfileIdx2_Object = MibTableColumn
rbPolicyRuleDownQoSProfileIdx2 = _RbPolicyRuleDownQoSProfileIdx2_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 5, 1, 1, 21),
    _RbPolicyRuleDownQoSProfileIdx2_Type()
)
rbPolicyRuleDownQoSProfileIdx2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbPolicyRuleDownQoSProfileIdx2.setStatus("current")
_RbPolicyRuleDownQoSUpperLimit2_Type = Unsigned32
_RbPolicyRuleDownQoSUpperLimit2_Object = MibTableColumn
rbPolicyRuleDownQoSUpperLimit2 = _RbPolicyRuleDownQoSUpperLimit2_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 5, 1, 1, 22),
    _RbPolicyRuleDownQoSUpperLimit2_Type()
)
rbPolicyRuleDownQoSUpperLimit2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbPolicyRuleDownQoSUpperLimit2.setStatus("current")
_RbPolicyRuleDownQoSProfileIdx3_Type = Unsigned32
_RbPolicyRuleDownQoSProfileIdx3_Object = MibTableColumn
rbPolicyRuleDownQoSProfileIdx3 = _RbPolicyRuleDownQoSProfileIdx3_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 5, 1, 1, 24),
    _RbPolicyRuleDownQoSProfileIdx3_Type()
)
rbPolicyRuleDownQoSProfileIdx3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbPolicyRuleDownQoSProfileIdx3.setStatus("current")
_RbPolicyRuleDownQoSUpperLimit3_Type = Unsigned32
_RbPolicyRuleDownQoSUpperLimit3_Object = MibTableColumn
rbPolicyRuleDownQoSUpperLimit3 = _RbPolicyRuleDownQoSUpperLimit3_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 5, 1, 1, 25),
    _RbPolicyRuleDownQoSUpperLimit3_Type()
)
rbPolicyRuleDownQoSUpperLimit3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbPolicyRuleDownQoSUpperLimit3.setStatus("current")
_RbPolicyRuleDownQoSProfileIdx4_Type = Unsigned32
_RbPolicyRuleDownQoSProfileIdx4_Object = MibTableColumn
rbPolicyRuleDownQoSProfileIdx4 = _RbPolicyRuleDownQoSProfileIdx4_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 5, 1, 1, 27),
    _RbPolicyRuleDownQoSProfileIdx4_Type()
)
rbPolicyRuleDownQoSProfileIdx4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbPolicyRuleDownQoSProfileIdx4.setStatus("current")
_RbPolicyRuleDownQoSUpperLimit4_Type = Unsigned32
_RbPolicyRuleDownQoSUpperLimit4_Object = MibTableColumn
rbPolicyRuleDownQoSUpperLimit4 = _RbPolicyRuleDownQoSUpperLimit4_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 5, 1, 1, 28),
    _RbPolicyRuleDownQoSUpperLimit4_Type()
)
rbPolicyRuleDownQoSUpperLimit4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbPolicyRuleDownQoSUpperLimit4.setStatus("current")
_RbAPolicyRuleRowStatus_Type = RowStatus
_RbAPolicyRuleRowStatus_Object = MibTableColumn
rbAPolicyRuleRowStatus = _RbAPolicyRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 5, 1, 1, 29),
    _RbAPolicyRuleRowStatus_Type()
)
rbAPolicyRuleRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAPolicyRuleRowStatus.setStatus("current")


class _RbPolicyRuleClass_Type(Integer32):
    """Custom type rbPolicyRuleClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("global", 2))
    )


_RbPolicyRuleClass_Type.__name__ = "Integer32"
_RbPolicyRuleClass_Object = MibTableColumn
rbPolicyRuleClass = _RbPolicyRuleClass_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 5, 1, 1, 30),
    _RbPolicyRuleClass_Type()
)
rbPolicyRuleClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPolicyRuleClass.setStatus("current")
_RbForwardingRules_ObjectIdentity = ObjectIdentity
rbForwardingRules = _RbForwardingRules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 6)
)
_RbForwardingRuleConfigTable_Object = MibTable
rbForwardingRuleConfigTable = _RbForwardingRuleConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 6, 2)
)
if mibBuilder.loadTexts:
    rbForwardingRuleConfigTable.setStatus("current")
_RbForwardingRuleConfigEntry_Object = MibTableRow
rbForwardingRuleConfigEntry = _RbForwardingRuleConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 6, 2, 1)
)
rbForwardingRuleConfigEntry.setIndexNames(
    (0, "RAINBOW-SERVICES-MIB", "rbForwardingRuleType"),
    (0, "RAINBOW-SERVICES-MIB", "rbForwardingRuleIdx"),
)
if mibBuilder.loadTexts:
    rbForwardingRuleConfigEntry.setStatus("current")
_RbForwardingRuleType_Type = RainbowServiceType
_RbForwardingRuleType_Object = MibTableColumn
rbForwardingRuleType = _RbForwardingRuleType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 6, 2, 1, 1),
    _RbForwardingRuleType_Type()
)
rbForwardingRuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbForwardingRuleType.setStatus("current")
_RbForwardingRuleIdx_Type = Unsigned32
_RbForwardingRuleIdx_Object = MibTableColumn
rbForwardingRuleIdx = _RbForwardingRuleIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 6, 2, 1, 2),
    _RbForwardingRuleIdx_Type()
)
rbForwardingRuleIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbForwardingRuleIdx.setStatus("current")


class _RbForwardingRuleName_Type(DisplayString):
    """Custom type rbForwardingRuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RbForwardingRuleName_Type.__name__ = "DisplayString"
_RbForwardingRuleName_Object = MibTableColumn
rbForwardingRuleName = _RbForwardingRuleName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 6, 2, 1, 3),
    _RbForwardingRuleName_Type()
)
rbForwardingRuleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbForwardingRuleName.setStatus("current")
_RbForwardingRuleID_Type = Unsigned32
_RbForwardingRuleID_Object = MibTableColumn
rbForwardingRuleID = _RbForwardingRuleID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 6, 2, 1, 4),
    _RbForwardingRuleID_Type()
)
rbForwardingRuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbForwardingRuleID.setStatus("current")


class _RbForwardingRuleUnicastRelaying_Type(Integer32):
    """Custom type rbForwardingRuleUnicastRelaying based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RbForwardingRuleUnicastRelaying_Type.__name__ = "Integer32"
_RbForwardingRuleUnicastRelaying_Object = MibTableColumn
rbForwardingRuleUnicastRelaying = _RbForwardingRuleUnicastRelaying_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 6, 2, 1, 6),
    _RbForwardingRuleUnicastRelaying_Type()
)
rbForwardingRuleUnicastRelaying.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbForwardingRuleUnicastRelaying.setStatus("current")


class _RbForwardingRuleMulticastRelaying_Type(Integer32):
    """Custom type rbForwardingRuleMulticastRelaying based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RbForwardingRuleMulticastRelaying_Type.__name__ = "Integer32"
_RbForwardingRuleMulticastRelaying_Object = MibTableColumn
rbForwardingRuleMulticastRelaying = _RbForwardingRuleMulticastRelaying_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 6, 2, 1, 7),
    _RbForwardingRuleMulticastRelaying_Type()
)
rbForwardingRuleMulticastRelaying.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbForwardingRuleMulticastRelaying.setStatus("current")


class _RbForwardingUnknownAddrPolicy_Type(Integer32):
    """Custom type rbForwardingUnknownAddrPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reject", 1),
          ("forward", 2))
    )


_RbForwardingUnknownAddrPolicy_Type.__name__ = "Integer32"
_RbForwardingUnknownAddrPolicy_Object = MibTableColumn
rbForwardingUnknownAddrPolicy = _RbForwardingUnknownAddrPolicy_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 6, 2, 1, 8),
    _RbForwardingUnknownAddrPolicy_Type()
)
rbForwardingUnknownAddrPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbForwardingUnknownAddrPolicy.setStatus("current")


class _RbForwardingRuleMulticastVLAN_Type(Integer32):
    """Custom type rbForwardingRuleMulticastVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_RbForwardingRuleMulticastVLAN_Type.__name__ = "Integer32"
_RbForwardingRuleMulticastVLAN_Object = MibTableColumn
rbForwardingRuleMulticastVLAN = _RbForwardingRuleMulticastVLAN_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 6, 2, 1, 9),
    _RbForwardingRuleMulticastVLAN_Type()
)
rbForwardingRuleMulticastVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbForwardingRuleMulticastVLAN.setStatus("current")
_RbForwardingRuleMulticastQoSIdx_Type = Unsigned32
_RbForwardingRuleMulticastQoSIdx_Object = MibTableColumn
rbForwardingRuleMulticastQoSIdx = _RbForwardingRuleMulticastQoSIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 6, 2, 1, 10),
    _RbForwardingRuleMulticastQoSIdx_Type()
)
rbForwardingRuleMulticastQoSIdx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbForwardingRuleMulticastQoSIdx.setStatus("current")
_RbAForwardingRuleRowStatus_Type = RowStatus
_RbAForwardingRuleRowStatus_Object = MibTableColumn
rbAForwardingRuleRowStatus = _RbAForwardingRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 6, 2, 1, 11),
    _RbAForwardingRuleRowStatus_Type()
)
rbAForwardingRuleRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAForwardingRuleRowStatus.setStatus("current")


class _RbForwardingRuleClass_Type(Integer32):
    """Custom type rbForwardingRuleClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("global", 2))
    )


_RbForwardingRuleClass_Type.__name__ = "Integer32"
_RbForwardingRuleClass_Object = MibTableColumn
rbForwardingRuleClass = _RbForwardingRuleClass_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 6, 2, 1, 12),
    _RbForwardingRuleClass_Type()
)
rbForwardingRuleClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbForwardingRuleClass.setStatus("current")
_RbSubscribersInfo_ObjectIdentity = ObjectIdentity
rbSubscribersInfo = _RbSubscribersInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 7)
)
_RbSubscriberTable_Object = MibTable
rbSubscriberTable = _RbSubscriberTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 7, 1)
)
if mibBuilder.loadTexts:
    rbSubscriberTable.setStatus("current")
_RbSubscriberEntry_Object = MibTableRow
rbSubscriberEntry = _RbSubscriberEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 7, 1, 1)
)
rbSubscriberEntry.setIndexNames(
    (0, "RAINBOW-SERVICES-MIB", "rbSubscriberIdx"),
)
if mibBuilder.loadTexts:
    rbSubscriberEntry.setStatus("current")
_RbSubscriberIdx_Type = Unsigned32
_RbSubscriberIdx_Object = MibTableColumn
rbSubscriberIdx = _RbSubscriberIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 7, 1, 1, 1),
    _RbSubscriberIdx_Type()
)
rbSubscriberIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSubscriberIdx.setStatus("current")


class _RbSubscriberID_Type(DisplayString):
    """Custom type rbSubscriberID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RbSubscriberID_Type.__name__ = "DisplayString"
_RbSubscriberID_Object = MibTableColumn
rbSubscriberID = _RbSubscriberID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 7, 1, 1, 2),
    _RbSubscriberID_Type()
)
rbSubscriberID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSubscriberID.setStatus("current")


class _RbSubscriberFirstName_Type(DisplayString):
    """Custom type rbSubscriberFirstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_RbSubscriberFirstName_Type.__name__ = "DisplayString"
_RbSubscriberFirstName_Object = MibTableColumn
rbSubscriberFirstName = _RbSubscriberFirstName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 7, 1, 1, 3),
    _RbSubscriberFirstName_Type()
)
rbSubscriberFirstName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSubscriberFirstName.setStatus("current")


class _RbSubscriberLastName_Type(DisplayString):
    """Custom type rbSubscriberLastName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_RbSubscriberLastName_Type.__name__ = "DisplayString"
_RbSubscriberLastName_Object = MibTableColumn
rbSubscriberLastName = _RbSubscriberLastName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 7, 1, 1, 4),
    _RbSubscriberLastName_Type()
)
rbSubscriberLastName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSubscriberLastName.setStatus("current")


class _RbSubscriberAdminStatus_Type(Integer32):
    """Custom type rbSubscriberAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RbSubscriberAdminStatus_Type.__name__ = "Integer32"
_RbSubscriberAdminStatus_Object = MibTableColumn
rbSubscriberAdminStatus = _RbSubscriberAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 7, 1, 1, 5),
    _RbSubscriberAdminStatus_Type()
)
rbSubscriberAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSubscriberAdminStatus.setStatus("current")


class _RbSubscriberInfo_Type(DisplayString):
    """Custom type rbSubscriberInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_RbSubscriberInfo_Type.__name__ = "DisplayString"
_RbSubscriberInfo_Object = MibTableColumn
rbSubscriberInfo = _RbSubscriberInfo_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 7, 1, 1, 6),
    _RbSubscriberInfo_Type()
)
rbSubscriberInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSubscriberInfo.setStatus("current")
_RbASubscriberRowStatus_Type = RowStatus
_RbASubscriberRowStatus_Object = MibTableColumn
rbASubscriberRowStatus = _RbASubscriberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 7, 1, 1, 7),
    _RbASubscriberRowStatus_Type()
)
rbASubscriberRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbASubscriberRowStatus.setStatus("current")
_RbFilteringSystem_ObjectIdentity = ObjectIdentity
rbFilteringSystem = _RbFilteringSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8)
)
_RbL2FilteringRules_ObjectIdentity = ObjectIdentity
rbL2FilteringRules = _RbL2FilteringRules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 1)
)
_RbL2FilteringRuleTable_Object = MibTable
rbL2FilteringRuleTable = _RbL2FilteringRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 1, 1)
)
if mibBuilder.loadTexts:
    rbL2FilteringRuleTable.setStatus("current")
_RbL2FilteringRuleEntry_Object = MibTableRow
rbL2FilteringRuleEntry = _RbL2FilteringRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 1, 1, 1)
)
rbL2FilteringRuleEntry.setIndexNames(
    (0, "RAINBOW-SERVICES-MIB", "rbL2FilteringRuleIdx"),
)
if mibBuilder.loadTexts:
    rbL2FilteringRuleEntry.setStatus("current")
_RbL2FilteringRuleIdx_Type = Unsigned32
_RbL2FilteringRuleIdx_Object = MibTableColumn
rbL2FilteringRuleIdx = _RbL2FilteringRuleIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 1, 1, 1, 1),
    _RbL2FilteringRuleIdx_Type()
)
rbL2FilteringRuleIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbL2FilteringRuleIdx.setStatus("current")
_RbL2FilteringRuleRowStatus_Type = RowStatus
_RbL2FilteringRuleRowStatus_Object = MibTableColumn
rbL2FilteringRuleRowStatus = _RbL2FilteringRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 1, 1, 1, 2),
    _RbL2FilteringRuleRowStatus_Type()
)
rbL2FilteringRuleRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbL2FilteringRuleRowStatus.setStatus("current")


class _RbL2FilteringRuleName_Type(DisplayString):
    """Custom type rbL2FilteringRuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RbL2FilteringRuleName_Type.__name__ = "DisplayString"
_RbL2FilteringRuleName_Object = MibTableColumn
rbL2FilteringRuleName = _RbL2FilteringRuleName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 1, 1, 1, 3),
    _RbL2FilteringRuleName_Type()
)
rbL2FilteringRuleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbL2FilteringRuleName.setStatus("current")
_RbL2FilteringRuleSrcMacAddress_Type = MacAddress
_RbL2FilteringRuleSrcMacAddress_Object = MibTableColumn
rbL2FilteringRuleSrcMacAddress = _RbL2FilteringRuleSrcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 1, 1, 1, 4),
    _RbL2FilteringRuleSrcMacAddress_Type()
)
rbL2FilteringRuleSrcMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbL2FilteringRuleSrcMacAddress.setStatus("current")
_RbL2FilteringRuleSrcMask_Type = MacAddress
_RbL2FilteringRuleSrcMask_Object = MibTableColumn
rbL2FilteringRuleSrcMask = _RbL2FilteringRuleSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 1, 1, 1, 5),
    _RbL2FilteringRuleSrcMask_Type()
)
rbL2FilteringRuleSrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbL2FilteringRuleSrcMask.setStatus("current")
_RbL2FilteringRuleDestMacAddress_Type = MacAddress
_RbL2FilteringRuleDestMacAddress_Object = MibTableColumn
rbL2FilteringRuleDestMacAddress = _RbL2FilteringRuleDestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 1, 1, 1, 6),
    _RbL2FilteringRuleDestMacAddress_Type()
)
rbL2FilteringRuleDestMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbL2FilteringRuleDestMacAddress.setStatus("current")
_RbL2FilteringRuleDestMask_Type = MacAddress
_RbL2FilteringRuleDestMask_Object = MibTableColumn
rbL2FilteringRuleDestMask = _RbL2FilteringRuleDestMask_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 1, 1, 1, 7),
    _RbL2FilteringRuleDestMask_Type()
)
rbL2FilteringRuleDestMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbL2FilteringRuleDestMask.setStatus("current")


class _RbL2FilteringRuleEthType_Type(Integer32):
    """Custom type rbL2FilteringRuleEthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RbL2FilteringRuleEthType_Type.__name__ = "Integer32"
_RbL2FilteringRuleEthType_Object = MibTableColumn
rbL2FilteringRuleEthType = _RbL2FilteringRuleEthType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 1, 1, 1, 8),
    _RbL2FilteringRuleEthType_Type()
)
rbL2FilteringRuleEthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbL2FilteringRuleEthType.setStatus("current")
_RbL34FilteringRules_ObjectIdentity = ObjectIdentity
rbL34FilteringRules = _RbL34FilteringRules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 2)
)
_RbL34FilteringRuleTable_Object = MibTable
rbL34FilteringRuleTable = _RbL34FilteringRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 2, 1)
)
if mibBuilder.loadTexts:
    rbL34FilteringRuleTable.setStatus("current")
_RbL34FilteringRuleEntry_Object = MibTableRow
rbL34FilteringRuleEntry = _RbL34FilteringRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 2, 1, 1)
)
rbL34FilteringRuleEntry.setIndexNames(
    (0, "RAINBOW-SERVICES-MIB", "rbL34FilteringRuleIdx"),
)
if mibBuilder.loadTexts:
    rbL34FilteringRuleEntry.setStatus("current")
_RbL34FilteringRuleIdx_Type = Unsigned32
_RbL34FilteringRuleIdx_Object = MibTableColumn
rbL34FilteringRuleIdx = _RbL34FilteringRuleIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 2, 1, 1, 1),
    _RbL34FilteringRuleIdx_Type()
)
rbL34FilteringRuleIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbL34FilteringRuleIdx.setStatus("current")
_RbL34FilteringRuleRowStatus_Type = RowStatus
_RbL34FilteringRuleRowStatus_Object = MibTableColumn
rbL34FilteringRuleRowStatus = _RbL34FilteringRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 2, 1, 1, 2),
    _RbL34FilteringRuleRowStatus_Type()
)
rbL34FilteringRuleRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbL34FilteringRuleRowStatus.setStatus("current")


class _RbL34FilteringRuleName_Type(DisplayString):
    """Custom type rbL34FilteringRuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RbL34FilteringRuleName_Type.__name__ = "DisplayString"
_RbL34FilteringRuleName_Object = MibTableColumn
rbL34FilteringRuleName = _RbL34FilteringRuleName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 2, 1, 1, 3),
    _RbL34FilteringRuleName_Type()
)
rbL34FilteringRuleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbL34FilteringRuleName.setStatus("current")
_RbL34FilteringRuleSrcIpAddress_Type = IpAddress
_RbL34FilteringRuleSrcIpAddress_Object = MibTableColumn
rbL34FilteringRuleSrcIpAddress = _RbL34FilteringRuleSrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 2, 1, 1, 4),
    _RbL34FilteringRuleSrcIpAddress_Type()
)
rbL34FilteringRuleSrcIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbL34FilteringRuleSrcIpAddress.setStatus("current")
_RbL34FilteringRuleSrcMask_Type = IpAddress
_RbL34FilteringRuleSrcMask_Object = MibTableColumn
rbL34FilteringRuleSrcMask = _RbL34FilteringRuleSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 2, 1, 1, 5),
    _RbL34FilteringRuleSrcMask_Type()
)
rbL34FilteringRuleSrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbL34FilteringRuleSrcMask.setStatus("current")
_RbL34FilteringRuleDestIpAddress_Type = IpAddress
_RbL34FilteringRuleDestIpAddress_Object = MibTableColumn
rbL34FilteringRuleDestIpAddress = _RbL34FilteringRuleDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 2, 1, 1, 6),
    _RbL34FilteringRuleDestIpAddress_Type()
)
rbL34FilteringRuleDestIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbL34FilteringRuleDestIpAddress.setStatus("current")
_RbL34FilteringRuleDestMask_Type = IpAddress
_RbL34FilteringRuleDestMask_Object = MibTableColumn
rbL34FilteringRuleDestMask = _RbL34FilteringRuleDestMask_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 2, 1, 1, 7),
    _RbL34FilteringRuleDestMask_Type()
)
rbL34FilteringRuleDestMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbL34FilteringRuleDestMask.setStatus("current")


class _RbL34FilteringRuleIpProtocol_Type(Integer32):
    """Custom type rbL34FilteringRuleIpProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RbL34FilteringRuleIpProtocol_Type.__name__ = "Integer32"
_RbL34FilteringRuleIpProtocol_Object = MibTableColumn
rbL34FilteringRuleIpProtocol = _RbL34FilteringRuleIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 2, 1, 1, 8),
    _RbL34FilteringRuleIpProtocol_Type()
)
rbL34FilteringRuleIpProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbL34FilteringRuleIpProtocol.setStatus("current")


class _RbL34FilteringRuleSrcUdpTcpPort_Type(Integer32):
    """Custom type rbL34FilteringRuleSrcUdpTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RbL34FilteringRuleSrcUdpTcpPort_Type.__name__ = "Integer32"
_RbL34FilteringRuleSrcUdpTcpPort_Object = MibTableColumn
rbL34FilteringRuleSrcUdpTcpPort = _RbL34FilteringRuleSrcUdpTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 2, 1, 1, 9),
    _RbL34FilteringRuleSrcUdpTcpPort_Type()
)
rbL34FilteringRuleSrcUdpTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbL34FilteringRuleSrcUdpTcpPort.setStatus("current")


class _RbL34FilteringRuleDestUdpTcpPort_Type(Integer32):
    """Custom type rbL34FilteringRuleDestUdpTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RbL34FilteringRuleDestUdpTcpPort_Type.__name__ = "Integer32"
_RbL34FilteringRuleDestUdpTcpPort_Object = MibTableColumn
rbL34FilteringRuleDestUdpTcpPort = _RbL34FilteringRuleDestUdpTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 2, 1, 1, 10),
    _RbL34FilteringRuleDestUdpTcpPort_Type()
)
rbL34FilteringRuleDestUdpTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbL34FilteringRuleDestUdpTcpPort.setStatus("current")
_RbInterfaceFiltering_ObjectIdentity = ObjectIdentity
rbInterfaceFiltering = _RbInterfaceFiltering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 3)
)
_RbInterfaceFilteringTable_Object = MibTable
rbInterfaceFilteringTable = _RbInterfaceFilteringTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 3, 1)
)
if mibBuilder.loadTexts:
    rbInterfaceFilteringTable.setStatus("current")
_RbInterfaceFilteringEntry_Object = MibTableRow
rbInterfaceFilteringEntry = _RbInterfaceFilteringEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 3, 1, 1)
)
rbInterfaceFilteringEntry.setIndexNames(
    (0, "RAINBOW-SERVICES-MIB", "rbInterfaceFilteringType"),
    (0, "RAINBOW-SERVICES-MIB", "rbInterfaceFilteringIdx"),
)
if mibBuilder.loadTexts:
    rbInterfaceFilteringEntry.setStatus("current")


class _RbInterfaceFilteringType_Type(Integer32):
    """Custom type rbInterfaceFilteringType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fromWireless", 1),
          ("fromNetwork", 2))
    )


_RbInterfaceFilteringType_Type.__name__ = "Integer32"
_RbInterfaceFilteringType_Object = MibTableColumn
rbInterfaceFilteringType = _RbInterfaceFilteringType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 3, 1, 1, 1),
    _RbInterfaceFilteringType_Type()
)
rbInterfaceFilteringType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbInterfaceFilteringType.setStatus("current")
_RbInterfaceFilteringIdx_Type = Unsigned32
_RbInterfaceFilteringIdx_Object = MibTableColumn
rbInterfaceFilteringIdx = _RbInterfaceFilteringIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 3, 1, 1, 2),
    _RbInterfaceFilteringIdx_Type()
)
rbInterfaceFilteringIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbInterfaceFilteringIdx.setStatus("current")


class _RbInterfaceFilteringName_Type(DisplayString):
    """Custom type rbInterfaceFilteringName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RbInterfaceFilteringName_Type.__name__ = "DisplayString"
_RbInterfaceFilteringName_Object = MibTableColumn
rbInterfaceFilteringName = _RbInterfaceFilteringName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 3, 1, 1, 3),
    _RbInterfaceFilteringName_Type()
)
rbInterfaceFilteringName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbInterfaceFilteringName.setStatus("current")


class _RbInterfaceFilteringAdminStatus_Type(Integer32):
    """Custom type rbInterfaceFilteringAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RbInterfaceFilteringAdminStatus_Type.__name__ = "Integer32"
_RbInterfaceFilteringAdminStatus_Object = MibTableColumn
rbInterfaceFilteringAdminStatus = _RbInterfaceFilteringAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 3, 1, 1, 4),
    _RbInterfaceFilteringAdminStatus_Type()
)
rbInterfaceFilteringAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbInterfaceFilteringAdminStatus.setStatus("current")


class _RbInterfaceFilteringActiveFilterType_Type(Integer32):
    """Custom type rbInterfaceFilteringActiveFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filterL2", 1),
          ("filterL34", 2))
    )


_RbInterfaceFilteringActiveFilterType_Type.__name__ = "Integer32"
_RbInterfaceFilteringActiveFilterType_Object = MibTableColumn
rbInterfaceFilteringActiveFilterType = _RbInterfaceFilteringActiveFilterType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 3, 1, 1, 5),
    _RbInterfaceFilteringActiveFilterType_Type()
)
rbInterfaceFilteringActiveFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbInterfaceFilteringActiveFilterType.setStatus("current")


class _RbInterfaceFilteringAction_Type(Integer32):
    """Custom type rbInterfaceFilteringAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("allow", 2))
    )


_RbInterfaceFilteringAction_Type.__name__ = "Integer32"
_RbInterfaceFilteringAction_Object = MibTableColumn
rbInterfaceFilteringAction = _RbInterfaceFilteringAction_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 3, 1, 1, 6),
    _RbInterfaceFilteringAction_Type()
)
rbInterfaceFilteringAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbInterfaceFilteringAction.setStatus("current")


class _RbInterfaceFilteringDeleteAllFilteringRules_Type(Integer32):
    """Custom type rbInterfaceFilteringDeleteAllFilteringRules based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("doNothing", 0),
          ("deleteAllRules", 1))
    )


_RbInterfaceFilteringDeleteAllFilteringRules_Type.__name__ = "Integer32"
_RbInterfaceFilteringDeleteAllFilteringRules_Object = MibTableColumn
rbInterfaceFilteringDeleteAllFilteringRules = _RbInterfaceFilteringDeleteAllFilteringRules_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 3, 1, 1, 7),
    _RbInterfaceFilteringDeleteAllFilteringRules_Type()
)
rbInterfaceFilteringDeleteAllFilteringRules.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbInterfaceFilteringDeleteAllFilteringRules.setStatus("current")


class _RbInterfaceFilteringResetAllFilteringCounters_Type(Integer32):
    """Custom type rbInterfaceFilteringResetAllFilteringCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("doNothing", 0),
          ("resetCounters", 1))
    )


_RbInterfaceFilteringResetAllFilteringCounters_Type.__name__ = "Integer32"
_RbInterfaceFilteringResetAllFilteringCounters_Object = MibTableColumn
rbInterfaceFilteringResetAllFilteringCounters = _RbInterfaceFilteringResetAllFilteringCounters_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 3, 1, 1, 8),
    _RbInterfaceFilteringResetAllFilteringCounters_Type()
)
rbInterfaceFilteringResetAllFilteringCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbInterfaceFilteringResetAllFilteringCounters.setStatus("current")
_RbInterfaceFilteringNonMatchingPacketsCounter_Type = Counter32
_RbInterfaceFilteringNonMatchingPacketsCounter_Object = MibTableColumn
rbInterfaceFilteringNonMatchingPacketsCounter = _RbInterfaceFilteringNonMatchingPacketsCounter_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 3, 1, 1, 9),
    _RbInterfaceFilteringNonMatchingPacketsCounter_Type()
)
rbInterfaceFilteringNonMatchingPacketsCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbInterfaceFilteringNonMatchingPacketsCounter.setStatus("current")
_RbFilters_ObjectIdentity = ObjectIdentity
rbFilters = _RbFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 4)
)
_RbFilterTable_Object = MibTable
rbFilterTable = _RbFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 4, 1)
)
if mibBuilder.loadTexts:
    rbFilterTable.setStatus("current")
_RbFilterEntry_Object = MibTableRow
rbFilterEntry = _RbFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 4, 1, 1)
)
rbFilterEntry.setIndexNames(
    (0, "RAINBOW-SERVICES-MIB", "rbInterfaceFilteringIdx"),
    (0, "RAINBOW-SERVICES-MIB", "rbFilterRuleType"),
    (0, "RAINBOW-SERVICES-MIB", "rbFilterRuleIndex"),
)
if mibBuilder.loadTexts:
    rbFilterEntry.setStatus("current")


class _RbFilterRuleType_Type(Integer32):
    """Custom type rbFilterRuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filterL2", 1),
          ("filterL34", 2))
    )


_RbFilterRuleType_Type.__name__ = "Integer32"
_RbFilterRuleType_Object = MibTableColumn
rbFilterRuleType = _RbFilterRuleType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 4, 1, 1, 1),
    _RbFilterRuleType_Type()
)
rbFilterRuleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbFilterRuleType.setStatus("current")
_RbFilterRuleIndex_Type = Unsigned32
_RbFilterRuleIndex_Object = MibTableColumn
rbFilterRuleIndex = _RbFilterRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 4, 1, 1, 2),
    _RbFilterRuleIndex_Type()
)
rbFilterRuleIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbFilterRuleIndex.setStatus("current")
_RbFilterRowStatus_Type = RowStatus
_RbFilterRowStatus_Object = MibTableColumn
rbFilterRowStatus = _RbFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 4, 1, 1, 3),
    _RbFilterRowStatus_Type()
)
rbFilterRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbFilterRowStatus.setStatus("current")
_RbFilterCounters_ObjectIdentity = ObjectIdentity
rbFilterCounters = _RbFilterCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 5)
)
_RbFilteringCounterTable_Object = MibTable
rbFilteringCounterTable = _RbFilteringCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 5, 1)
)
if mibBuilder.loadTexts:
    rbFilteringCounterTable.setStatus("current")
_RbFilteringCounterEntry_Object = MibTableRow
rbFilteringCounterEntry = _RbFilteringCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 5, 1, 1)
)
rbFilteringCounterEntry.setIndexNames(
    (0, "RAINBOW-SERVICES-MIB", "rbInterfaceFilteringIdx"),
    (0, "RAINBOW-SERVICES-MIB", "rbInterfaceFilteringActiveFilterType"),
    (0, "RAINBOW-SERVICES-MIB", "rbCountRuleIdx"),
)
if mibBuilder.loadTexts:
    rbFilteringCounterEntry.setStatus("current")
_RbCountRuleIdx_Type = Unsigned32
_RbCountRuleIdx_Object = MibTableColumn
rbCountRuleIdx = _RbCountRuleIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 5, 1, 1, 1),
    _RbCountRuleIdx_Type()
)
rbCountRuleIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbCountRuleIdx.setStatus("current")


class _RbResetCounter_Type(Integer32):
    """Custom type rbResetCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("doNothing", 0),
          ("resetCounter", 1))
    )


_RbResetCounter_Type.__name__ = "Integer32"
_RbResetCounter_Object = MibTableColumn
rbResetCounter = _RbResetCounter_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 5, 1, 1, 2),
    _RbResetCounter_Type()
)
rbResetCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbResetCounter.setStatus("current")
_RbRuleMatchCount_Type = Counter32
_RbRuleMatchCount_Object = MibTableColumn
rbRuleMatchCount = _RbRuleMatchCount_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 5, 1, 1, 3),
    _RbRuleMatchCount_Type()
)
rbRuleMatchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbRuleMatchCount.setStatus("current")
_RbMACAddressDenyList_ObjectIdentity = ObjectIdentity
rbMACAddressDenyList = _RbMACAddressDenyList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 6)
)
_RbMACAddressDenyListCounters_ObjectIdentity = ObjectIdentity
rbMACAddressDenyListCounters = _RbMACAddressDenyListCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 6, 1)
)


class _RbDenyListCounterReset_Type(Integer32):
    """Custom type rbDenyListCounterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("doNothing", 0),
          ("resetCounter", 1))
    )


_RbDenyListCounterReset_Type.__name__ = "Integer32"
_RbDenyListCounterReset_Object = MibScalar
rbDenyListCounterReset = _RbDenyListCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 6, 1, 1),
    _RbDenyListCounterReset_Type()
)
rbDenyListCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbDenyListCounterReset.setStatus("current")
_RbDenyListWirelessPacketCounter_Type = Counter32
_RbDenyListWirelessPacketCounter_Object = MibScalar
rbDenyListWirelessPacketCounter = _RbDenyListWirelessPacketCounter_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 6, 1, 2),
    _RbDenyListWirelessPacketCounter_Type()
)
rbDenyListWirelessPacketCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbDenyListWirelessPacketCounter.setStatus("current")
_RbDenyListNetworkPacketCounter_Type = Counter32
_RbDenyListNetworkPacketCounter_Object = MibScalar
rbDenyListNetworkPacketCounter = _RbDenyListNetworkPacketCounter_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 6, 1, 3),
    _RbDenyListNetworkPacketCounter_Type()
)
rbDenyListNetworkPacketCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbDenyListNetworkPacketCounter.setStatus("current")
_RbMACAddressDenyListTable_Object = MibTable
rbMACAddressDenyListTable = _RbMACAddressDenyListTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 6, 2)
)
if mibBuilder.loadTexts:
    rbMACAddressDenyListTable.setStatus("current")
_RbMACAddressDenyListEntry_Object = MibTableRow
rbMACAddressDenyListEntry = _RbMACAddressDenyListEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 6, 2, 1)
)
rbMACAddressDenyListEntry.setIndexNames(
    (0, "RAINBOW-SERVICES-MIB", "rbMACAddressDenyMacAddress"),
)
if mibBuilder.loadTexts:
    rbMACAddressDenyListEntry.setStatus("current")
_RbMACAddressDenyMacAddress_Type = MacAddress
_RbMACAddressDenyMacAddress_Object = MibTableColumn
rbMACAddressDenyMacAddress = _RbMACAddressDenyMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 6, 2, 1, 1),
    _RbMACAddressDenyMacAddress_Type()
)
rbMACAddressDenyMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbMACAddressDenyMacAddress.setStatus("current")
_RbMACAddressDenyListRowStatus_Type = RowStatus
_RbMACAddressDenyListRowStatus_Object = MibTableColumn
rbMACAddressDenyListRowStatus = _RbMACAddressDenyListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 6, 2, 1, 2),
    _RbMACAddressDenyListRowStatus_Type()
)
rbMACAddressDenyListRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbMACAddressDenyListRowStatus.setStatus("current")
_RbFilterGeneralConfig_ObjectIdentity = ObjectIdentity
rbFilterGeneralConfig = _RbFilterGeneralConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 7)
)
_RbGetNewL2FilterRuleID_Type = Unsigned32
_RbGetNewL2FilterRuleID_Object = MibScalar
rbGetNewL2FilterRuleID = _RbGetNewL2FilterRuleID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 7, 1),
    _RbGetNewL2FilterRuleID_Type()
)
rbGetNewL2FilterRuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbGetNewL2FilterRuleID.setStatus("current")
_RbGetNewL34FilterRuleID_Type = Unsigned32
_RbGetNewL34FilterRuleID_Object = MibScalar
rbGetNewL34FilterRuleID = _RbGetNewL34FilterRuleID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 8, 7, 2),
    _RbGetNewL34FilterRuleID_Type()
)
rbGetNewL34FilterRuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbGetNewL34FilterRuleID.setStatus("current")
_RbXmlErrorReport_ObjectIdentity = ObjectIdentity
rbXmlErrorReport = _RbXmlErrorReport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 10)
)
_RbXmlErrorReportTable_Object = MibTable
rbXmlErrorReportTable = _RbXmlErrorReportTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 10, 1)
)
if mibBuilder.loadTexts:
    rbXmlErrorReportTable.setStatus("current")
_RbXmlErrorReportEntry_Object = MibTableRow
rbXmlErrorReportEntry = _RbXmlErrorReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 10, 1, 1)
)
rbXmlErrorReportEntry.setIndexNames(
    (0, "RAINBOW-SERVICES-MIB", "rbXmlErrorIdx"),
)
if mibBuilder.loadTexts:
    rbXmlErrorReportEntry.setStatus("current")
_RbXmlErrorIdx_Type = Integer32
_RbXmlErrorIdx_Object = MibTableColumn
rbXmlErrorIdx = _RbXmlErrorIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 10, 1, 1, 1),
    _RbXmlErrorIdx_Type()
)
rbXmlErrorIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbXmlErrorIdx.setStatus("current")


class _RbXmlFolderType_Type(Integer32):
    """Custom type rbXmlFolderType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("serviceProfiles", 1))
    )


_RbXmlFolderType_Type.__name__ = "Integer32"
_RbXmlFolderType_Object = MibTableColumn
rbXmlFolderType = _RbXmlFolderType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 10, 1, 1, 2),
    _RbXmlFolderType_Type()
)
rbXmlFolderType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbXmlFolderType.setStatus("current")


class _RbXmlElementType_Type(Integer32):
    """Custom type rbXmlElementType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("qosProfile", 1),
          ("forwardingRule", 2),
          ("priorityClassifier", 3),
          ("serviceProfile", 4))
    )


_RbXmlElementType_Type.__name__ = "Integer32"
_RbXmlElementType_Object = MibTableColumn
rbXmlElementType = _RbXmlElementType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 10, 1, 1, 3),
    _RbXmlElementType_Type()
)
rbXmlElementType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbXmlElementType.setStatus("current")


class _RbXmlErrorType_Type(Integer32):
    """Custom type rbXmlErrorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              1000,
              1001,
              1002,
              1003)
        )
    )
    namedValues = NamedValues(
        *(("noError", 0),
          ("illegalTableId", 1),
          ("deleteSuFailure", 2),
          ("oneL2fwrulePerVpl", 3),
          ("sameServiceTypeOnVlan", 4),
          ("dbAddFailure", 5),
          ("dbUpdateFailure", 6),
          ("dbDeleteFailure", 7),
          ("keyMissing", 8),
          ("addedRecordAlreadyExists", 9),
          ("addSmRecNeeded", 10),
          ("addSuRecNeeded", 11),
          ("addPipeRecNeeded", 12),
          ("addPriorityClassRecNeeded", 13),
          ("addFwRulesRecNeeded", 14),
          ("addIpAddrsRulesRecNeeded", 15),
          ("addProfileRecNeeded", 16),
          ("addSubscriberRecNeeded", 17),
          ("addVlanListNeeded", 18),
          ("addQosRecNeeded", 19),
          ("updatedRecordNotExists", 20),
          ("deletedRecordNotExists", 21),
          ("deletePipeRecNeeded", 22),
          ("deleteProfileRecNeeded", 23),
          ("deleteFwRulesRecNeeded", 24),
          ("deletePriorityRecNeeded", 25),
          ("deleteDefaultProfileNeeded", 26),
          ("deletePriorityDefDscpRecNeeded", 27),
          ("wrongPriorityType", 28),
          ("wrongUpPriorityRanges", 29),
          ("wrongDnPriorityRanges", 30),
          ("addTooManyConnections", 31),
          ("serviceHandling", 32),
          ("illeagalTranstype", 33),
          ("illeagalSustatus", 34),
          ("addedKeyAlreadyExists", 35),
          ("fileDoesNotExist", 36),
          ("tableIsFull", 37),
          ("deleteSuServicesNeeded", 38),
          ("differentServiceType", 39),
          ("differentForwardingType", 40),
          ("differentForwardSrvcType", 41),
          ("tooManyVlans", 42),
          ("updateSuStatus", 43),
          ("changeSu", 44),
          ("vlanMismatch", 45),
          ("wrongVlanId", 46),
          ("wrongCgQosValues", 47),
          ("maxVlanPerSuExcedded", 48),
          ("duplicateRecordName", 49),
          ("deleteTransparentFwRule", 50),
          ("transparentVlanVplMismatch", 51),
          ("transparentFwProfileMismatch", 52),
          ("missingTransparentFwRule", 53),
          ("globalProfile", 54),
          ("wrongCirValue", 55),
          ("wrongMirValue", 56),
          ("invalidMaxCallsValue", 57),
          ("invalidSampleRate", 58),
          ("invalidPacketSize", 59),
          ("invalidFwRuleParameter", 60),
          ("nullProfileName", 61),
          ("invalidQosType", 62),
          ("invalidPriorityClassifierType", 63),
          ("invalidCT", 64),
          ("invalidTransparencyMode", 65),
          ("oneVlanPermittedForVlanClassMode", 66),
          ("accessVlanMismatch", 67),
          ("accessVlanDuplicate", 68),
          ("oneAccessVlanPerSU", 69),
          ("changTransparentFWRuleName", 70),
          ("unknownError", 1000),
          ("xmlParseFormatErr", 1001),
          ("xmlParseSyntaxErr", 1002),
          ("xmlParseUnresolvedProfileErr", 1003))
    )


_RbXmlErrorType_Type.__name__ = "Integer32"
_RbXmlErrorType_Object = MibTableColumn
rbXmlErrorType = _RbXmlErrorType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 10, 1, 1, 4),
    _RbXmlErrorType_Type()
)
rbXmlErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbXmlErrorType.setStatus("current")
_RbXmlFileLineNumber_Type = Integer32
_RbXmlFileLineNumber_Object = MibTableColumn
rbXmlFileLineNumber = _RbXmlFileLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 100, 10, 1, 1, 5),
    _RbXmlFileLineNumber_Type()
)
rbXmlFileLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbXmlFileLineNumber.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAINBOW-SERVICES-MIB",
    **{"RainbowServiceType": RainbowServiceType,
       "rainbowServices": rainbowServices,
       "rbServiceGeneralConfig": rbServiceGeneralConfig,
       "rbGetNewPolicyRuleID": rbGetNewPolicyRuleID,
       "rbGetNewServiceID": rbGetNewServiceID,
       "rbGetNewServiceTemplateID": rbGetNewServiceTemplateID,
       "rbGetNewSubscriberID": rbGetNewSubscriberID,
       "rbGetNewQoSProfileID": rbGetNewQoSProfileID,
       "rbGetNewForwardingRuleID": rbGetNewForwardingRuleID,
       "rbServiceWorkingMode": rbServiceWorkingMode,
       "rbDfltServiceTemplateTable": rbDfltServiceTemplateTable,
       "rbDfltServiceTemplateEntry": rbDfltServiceTemplateEntry,
       "rbDfltServiceTemplateType": rbDfltServiceTemplateType,
       "rbDfltServiceTemplateIdx": rbDfltServiceTemplateIdx,
       "rbServiceTemplate": rbServiceTemplate,
       "rbServiceTemplateConfigTable": rbServiceTemplateConfigTable,
       "rbServiceTemplateConfigEntry": rbServiceTemplateConfigEntry,
       "rbServiceTemplateType": rbServiceTemplateType,
       "rbServiceTemplateIdx": rbServiceTemplateIdx,
       "rbServiceTemplateName": rbServiceTemplateName,
       "rbServiceTemplateID": rbServiceTemplateID,
       "rbServiceTemplateBaseVLAN": rbServiceTemplateBaseVLAN,
       "rbServiceTemplateBaseSignallingVLAN": rbServiceTemplateBaseSignallingVLAN,
       "rbServiceTemplateBaseDhcpVLAN": rbServiceTemplateBaseDhcpVLAN,
       "rbServiceTemplateForwardDhcpRequest": rbServiceTemplateForwardDhcpRequest,
       "rbServiceTemplateNumberOfSimultaneousCalls": rbServiceTemplateNumberOfSimultaneousCalls,
       "rbServiceTemplatePolicyRuleIdx": rbServiceTemplatePolicyRuleIdx,
       "rbServiceTemplatePolicyRuleName": rbServiceTemplatePolicyRuleName,
       "rbServiceTemplateForwardingRuleIdx": rbServiceTemplateForwardingRuleIdx,
       "rbServiceTemplateForwardingRuleName": rbServiceTemplateForwardingRuleName,
       "rbAServiceTemplateRowStatus": rbAServiceTemplateRowStatus,
       "rbServiceTemplateQoSMarkingMode": rbServiceTemplateQoSMarkingMode,
       "rbServiceTemplateQoSMarkingValue": rbServiceTemplateQoSMarkingValue,
       "rbServiceTemplateVLANTransparencyMode": rbServiceTemplateVLANTransparencyMode,
       "rbServiceTemplateClass": rbServiceTemplateClass,
       "rbServices": rbServices,
       "rbServiceConfigTable": rbServiceConfigTable,
       "rbServiceConfigEntry": rbServiceConfigEntry,
       "rbServiceIdx": rbServiceIdx,
       "rbServiceType": rbServiceType,
       "rbServiceName": rbServiceName,
       "rbServiceID": rbServiceID,
       "rbServiceServiceTemplateIdx": rbServiceServiceTemplateIdx,
       "rbServiceServiceTemplateName": rbServiceServiceTemplateName,
       "rbServiceServiceTemplateID": rbServiceServiceTemplateID,
       "rbServiceSwitchingGroupIdx": rbServiceSwitchingGroupIdx,
       "rbServiceAdminStatus": rbServiceAdminStatus,
       "rbServiceOperStatus": rbServiceOperStatus,
       "rbAServiceRowStatus": rbAServiceRowStatus,
       "rbServiceClientSiteVLANList": rbServiceClientSiteVLANList,
       "rbServiceClientSiteVLANListCount": rbServiceClientSiteVLANListCount,
       "rbServiceSuMacAddress": rbServiceSuMacAddress,
       "rbServiceAUSlotNumber": rbServiceAUSlotNumber,
       "rbServiceVLANHybridMode": rbServiceVLANHybridMode,
       "rbServiceVLANClassificationMode": rbServiceVLANClassificationMode,
       "rbServiceAccessVLAN": rbServiceAccessVLAN,
       "rbSuServiceConfigTable": rbSuServiceConfigTable,
       "rbSuServiceConfigEntry": rbSuServiceConfigEntry,
       "rbSuServiceMacAddress": rbSuServiceMacAddress,
       "rbSuServiceIdx": rbSuServiceIdx,
       "rbSuServiceRbType": rbSuServiceRbType,
       "rbSuServiceName": rbSuServiceName,
       "rbSuServiceID": rbSuServiceID,
       "rbSuSubscriberIdx": rbSuSubscriberIdx,
       "rbSuServiceTemplateIdx": rbSuServiceTemplateIdx,
       "rbSuServiceTemplateName": rbSuServiceTemplateName,
       "rbSuServiceTemplateID": rbSuServiceTemplateID,
       "rbSuServiceSwitchingGroupIdx": rbSuServiceSwitchingGroupIdx,
       "rbSuServiceAdminStatus": rbSuServiceAdminStatus,
       "rbSuServiceOperStatus": rbSuServiceOperStatus,
       "rbSuServiceClientSiteVLANList": rbSuServiceClientSiteVLANList,
       "rbSuServiceClientSiteVLANListCount": rbSuServiceClientSiteVLANListCount,
       "rbSuServiceAUSlotNumber": rbSuServiceAUSlotNumber,
       "rbSuServiceVLANHybridMode": rbSuServiceVLANHybridMode,
       "rbSuServiceVLANClassificationMode": rbSuServiceVLANClassificationMode,
       "rbSuServiceAccessVLAN": rbSuServiceAccessVLAN,
       "rbSuServiceRowStatus": rbSuServiceRowStatus,
       "rbSuMappingTable": rbSuMappingTable,
       "rbSuMappingEntry": rbSuMappingEntry,
       "rbSuMappingSysName": rbSuMappingSysName,
       "rbSuMappingMacAddress": rbSuMappingMacAddress,
       "rbQoSProfiles": rbQoSProfiles,
       "rbQoSProfileConfigTable": rbQoSProfileConfigTable,
       "rbQoSProfileConfigEntry": rbQoSProfileConfigEntry,
       "rbQoSProfileIdx": rbQoSProfileIdx,
       "rbQoSProfileName": rbQoSProfileName,
       "rbQoSProfileID": rbQoSProfileID,
       "rbQoSProfileType": rbQoSProfileType,
       "rbQoSProfileParam1": rbQoSProfileParam1,
       "rbQoSProfileParam2": rbQoSProfileParam2,
       "rbQoSProfileParamTime": rbQoSProfileParamTime,
       "rbAQoSProfileRowStatus": rbAQoSProfileRowStatus,
       "rbQoSProfileClass": rbQoSProfileClass,
       "rbPolicyRules": rbPolicyRules,
       "rbPolicyRuleConfigTable": rbPolicyRuleConfigTable,
       "rbPolicyRuleConfigEntry": rbPolicyRuleConfigEntry,
       "rbPolicyRuleIdx": rbPolicyRuleIdx,
       "rbPolicyRuleName": rbPolicyRuleName,
       "rbPolicyRuleID": rbPolicyRuleID,
       "rbPolicyRulePriorityType": rbPolicyRulePriorityType,
       "rbPolicyRuleUpQoSProfileIdx1": rbPolicyRuleUpQoSProfileIdx1,
       "rbPolicyRuleUpQoSUpperLimit1": rbPolicyRuleUpQoSUpperLimit1,
       "rbPolicyRuleUpQoSProfileIdx2": rbPolicyRuleUpQoSProfileIdx2,
       "rbPolicyRuleUpQoSUpperLimit2": rbPolicyRuleUpQoSUpperLimit2,
       "rbPolicyRuleUpQoSProfileIdx3": rbPolicyRuleUpQoSProfileIdx3,
       "rbPolicyRuleUpQoSUpperLimit3": rbPolicyRuleUpQoSUpperLimit3,
       "rbPolicyRuleUpQoSProfileIdx4": rbPolicyRuleUpQoSProfileIdx4,
       "rbPolicyRuleUpQoSUpperLimit4": rbPolicyRuleUpQoSUpperLimit4,
       "rbPolicyRuleDownQoSProfileIdx1": rbPolicyRuleDownQoSProfileIdx1,
       "rbPolicyRuleDownQoSUpperLimit1": rbPolicyRuleDownQoSUpperLimit1,
       "rbPolicyRuleDownQoSProfileIdx2": rbPolicyRuleDownQoSProfileIdx2,
       "rbPolicyRuleDownQoSUpperLimit2": rbPolicyRuleDownQoSUpperLimit2,
       "rbPolicyRuleDownQoSProfileIdx3": rbPolicyRuleDownQoSProfileIdx3,
       "rbPolicyRuleDownQoSUpperLimit3": rbPolicyRuleDownQoSUpperLimit3,
       "rbPolicyRuleDownQoSProfileIdx4": rbPolicyRuleDownQoSProfileIdx4,
       "rbPolicyRuleDownQoSUpperLimit4": rbPolicyRuleDownQoSUpperLimit4,
       "rbAPolicyRuleRowStatus": rbAPolicyRuleRowStatus,
       "rbPolicyRuleClass": rbPolicyRuleClass,
       "rbForwardingRules": rbForwardingRules,
       "rbForwardingRuleConfigTable": rbForwardingRuleConfigTable,
       "rbForwardingRuleConfigEntry": rbForwardingRuleConfigEntry,
       "rbForwardingRuleType": rbForwardingRuleType,
       "rbForwardingRuleIdx": rbForwardingRuleIdx,
       "rbForwardingRuleName": rbForwardingRuleName,
       "rbForwardingRuleID": rbForwardingRuleID,
       "rbForwardingRuleUnicastRelaying": rbForwardingRuleUnicastRelaying,
       "rbForwardingRuleMulticastRelaying": rbForwardingRuleMulticastRelaying,
       "rbForwardingUnknownAddrPolicy": rbForwardingUnknownAddrPolicy,
       "rbForwardingRuleMulticastVLAN": rbForwardingRuleMulticastVLAN,
       "rbForwardingRuleMulticastQoSIdx": rbForwardingRuleMulticastQoSIdx,
       "rbAForwardingRuleRowStatus": rbAForwardingRuleRowStatus,
       "rbForwardingRuleClass": rbForwardingRuleClass,
       "rbSubscribersInfo": rbSubscribersInfo,
       "rbSubscriberTable": rbSubscriberTable,
       "rbSubscriberEntry": rbSubscriberEntry,
       "rbSubscriberIdx": rbSubscriberIdx,
       "rbSubscriberID": rbSubscriberID,
       "rbSubscriberFirstName": rbSubscriberFirstName,
       "rbSubscriberLastName": rbSubscriberLastName,
       "rbSubscriberAdminStatus": rbSubscriberAdminStatus,
       "rbSubscriberInfo": rbSubscriberInfo,
       "rbASubscriberRowStatus": rbASubscriberRowStatus,
       "rbFilteringSystem": rbFilteringSystem,
       "rbL2FilteringRules": rbL2FilteringRules,
       "rbL2FilteringRuleTable": rbL2FilteringRuleTable,
       "rbL2FilteringRuleEntry": rbL2FilteringRuleEntry,
       "rbL2FilteringRuleIdx": rbL2FilteringRuleIdx,
       "rbL2FilteringRuleRowStatus": rbL2FilteringRuleRowStatus,
       "rbL2FilteringRuleName": rbL2FilteringRuleName,
       "rbL2FilteringRuleSrcMacAddress": rbL2FilteringRuleSrcMacAddress,
       "rbL2FilteringRuleSrcMask": rbL2FilteringRuleSrcMask,
       "rbL2FilteringRuleDestMacAddress": rbL2FilteringRuleDestMacAddress,
       "rbL2FilteringRuleDestMask": rbL2FilteringRuleDestMask,
       "rbL2FilteringRuleEthType": rbL2FilteringRuleEthType,
       "rbL34FilteringRules": rbL34FilteringRules,
       "rbL34FilteringRuleTable": rbL34FilteringRuleTable,
       "rbL34FilteringRuleEntry": rbL34FilteringRuleEntry,
       "rbL34FilteringRuleIdx": rbL34FilteringRuleIdx,
       "rbL34FilteringRuleRowStatus": rbL34FilteringRuleRowStatus,
       "rbL34FilteringRuleName": rbL34FilteringRuleName,
       "rbL34FilteringRuleSrcIpAddress": rbL34FilteringRuleSrcIpAddress,
       "rbL34FilteringRuleSrcMask": rbL34FilteringRuleSrcMask,
       "rbL34FilteringRuleDestIpAddress": rbL34FilteringRuleDestIpAddress,
       "rbL34FilteringRuleDestMask": rbL34FilteringRuleDestMask,
       "rbL34FilteringRuleIpProtocol": rbL34FilteringRuleIpProtocol,
       "rbL34FilteringRuleSrcUdpTcpPort": rbL34FilteringRuleSrcUdpTcpPort,
       "rbL34FilteringRuleDestUdpTcpPort": rbL34FilteringRuleDestUdpTcpPort,
       "rbInterfaceFiltering": rbInterfaceFiltering,
       "rbInterfaceFilteringTable": rbInterfaceFilteringTable,
       "rbInterfaceFilteringEntry": rbInterfaceFilteringEntry,
       "rbInterfaceFilteringType": rbInterfaceFilteringType,
       "rbInterfaceFilteringIdx": rbInterfaceFilteringIdx,
       "rbInterfaceFilteringName": rbInterfaceFilteringName,
       "rbInterfaceFilteringAdminStatus": rbInterfaceFilteringAdminStatus,
       "rbInterfaceFilteringActiveFilterType": rbInterfaceFilteringActiveFilterType,
       "rbInterfaceFilteringAction": rbInterfaceFilteringAction,
       "rbInterfaceFilteringDeleteAllFilteringRules": rbInterfaceFilteringDeleteAllFilteringRules,
       "rbInterfaceFilteringResetAllFilteringCounters": rbInterfaceFilteringResetAllFilteringCounters,
       "rbInterfaceFilteringNonMatchingPacketsCounter": rbInterfaceFilteringNonMatchingPacketsCounter,
       "rbFilters": rbFilters,
       "rbFilterTable": rbFilterTable,
       "rbFilterEntry": rbFilterEntry,
       "rbFilterRuleType": rbFilterRuleType,
       "rbFilterRuleIndex": rbFilterRuleIndex,
       "rbFilterRowStatus": rbFilterRowStatus,
       "rbFilterCounters": rbFilterCounters,
       "rbFilteringCounterTable": rbFilteringCounterTable,
       "rbFilteringCounterEntry": rbFilteringCounterEntry,
       "rbCountRuleIdx": rbCountRuleIdx,
       "rbResetCounter": rbResetCounter,
       "rbRuleMatchCount": rbRuleMatchCount,
       "rbMACAddressDenyList": rbMACAddressDenyList,
       "rbMACAddressDenyListCounters": rbMACAddressDenyListCounters,
       "rbDenyListCounterReset": rbDenyListCounterReset,
       "rbDenyListWirelessPacketCounter": rbDenyListWirelessPacketCounter,
       "rbDenyListNetworkPacketCounter": rbDenyListNetworkPacketCounter,
       "rbMACAddressDenyListTable": rbMACAddressDenyListTable,
       "rbMACAddressDenyListEntry": rbMACAddressDenyListEntry,
       "rbMACAddressDenyMacAddress": rbMACAddressDenyMacAddress,
       "rbMACAddressDenyListRowStatus": rbMACAddressDenyListRowStatus,
       "rbFilterGeneralConfig": rbFilterGeneralConfig,
       "rbGetNewL2FilterRuleID": rbGetNewL2FilterRuleID,
       "rbGetNewL34FilterRuleID": rbGetNewL34FilterRuleID,
       "rbXmlErrorReport": rbXmlErrorReport,
       "rbXmlErrorReportTable": rbXmlErrorReportTable,
       "rbXmlErrorReportEntry": rbXmlErrorReportEntry,
       "rbXmlErrorIdx": rbXmlErrorIdx,
       "rbXmlFolderType": rbXmlFolderType,
       "rbXmlElementType": rbXmlElementType,
       "rbXmlErrorType": rbXmlErrorType,
       "rbXmlFileLineNumber": rbXmlFileLineNumber}
)
