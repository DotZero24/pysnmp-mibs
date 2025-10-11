# SNMP MIB module (BROADCOM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/radlan/BROADCOM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:11:04 2025
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

(rlBroadcom,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rlBroadcom")

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
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class RlPolicySimpleBcmMibProfileType(TextualConvention, Integer32):
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
        *(("bandwidthGuarantee", 1),
          ("minDelay", 2),
          ("bestEffort", 3))
    )



class RlBcmQoSRateLimitType(TextualConvention, Integer32):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("aggregate", 1),
          ("flowAggregate", 2),
          ("perFlow", 3),
          ("multiField", 4),
          ("inPort", 5),
          ("outPort", 6),
          ("qosIP", 7),
          ("qosIPAcl", 8))
    )



# MIB Managed Objects in the order of their OIDs

_RlBcmMibVersion_Type = Integer32
_RlBcmMibVersion_Object = MibScalar
rlBcmMibVersion = _RlBcmMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 1),
    _RlBcmMibVersion_Type()
)
rlBcmMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBcmMibVersion.setStatus("mandatory")
_RlPolicySimpleBcmMib_ObjectIdentity = ObjectIdentity
rlPolicySimpleBcmMib = _RlPolicySimpleBcmMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 68, 2)
)
_RlPolicySimpleBcmMibVersion_Type = Integer32
_RlPolicySimpleBcmMibVersion_Object = MibScalar
rlPolicySimpleBcmMibVersion = _RlPolicySimpleBcmMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 2, 1),
    _RlPolicySimpleBcmMibVersion_Type()
)
rlPolicySimpleBcmMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicySimpleBcmMibVersion.setStatus("mandatory")


class _RlPolicySimpleBcmMibReservedBW_Type(Integer32):
    """Custom type rlPolicySimpleBcmMibReservedBW based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RlPolicySimpleBcmMibReservedBW_Type.__name__ = "Integer32"
_RlPolicySimpleBcmMibReservedBW_Object = MibScalar
rlPolicySimpleBcmMibReservedBW = _RlPolicySimpleBcmMibReservedBW_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 2, 2),
    _RlPolicySimpleBcmMibReservedBW_Type()
)
rlPolicySimpleBcmMibReservedBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleBcmMibReservedBW.setStatus("mandatory")


class _RlPolicySimpleBcmMibPolicyEnable_Type(Integer32):
    """Custom type rlPolicySimpleBcmMibPolicyEnable based on Integer32"""
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


_RlPolicySimpleBcmMibPolicyEnable_Type.__name__ = "Integer32"
_RlPolicySimpleBcmMibPolicyEnable_Object = MibScalar
rlPolicySimpleBcmMibPolicyEnable = _RlPolicySimpleBcmMibPolicyEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 2, 3),
    _RlPolicySimpleBcmMibPolicyEnable_Type()
)
rlPolicySimpleBcmMibPolicyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleBcmMibPolicyEnable.setStatus("mandatory")
_RlPolicySimpleBcmMibProfileTable_Object = MibTable
rlPolicySimpleBcmMibProfileTable = _RlPolicySimpleBcmMibProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 2, 4)
)
if mibBuilder.loadTexts:
    rlPolicySimpleBcmMibProfileTable.setStatus("mandatory")
_RlPolicySimpleBcmMibProfileEntry_Object = MibTableRow
rlPolicySimpleBcmMibProfileEntry = _RlPolicySimpleBcmMibProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 2, 4, 1)
)
rlPolicySimpleBcmMibProfileEntry.setIndexNames(
    (0, "BROADCOM-MIB", "rlPolicySimpleBcmMibIndex"),
)
if mibBuilder.loadTexts:
    rlPolicySimpleBcmMibProfileEntry.setStatus("mandatory")


class _RlPolicySimpleBcmMibIndex_Type(Integer32):
    """Custom type rlPolicySimpleBcmMibIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1048576),
    )


_RlPolicySimpleBcmMibIndex_Type.__name__ = "Integer32"
_RlPolicySimpleBcmMibIndex_Object = MibTableColumn
rlPolicySimpleBcmMibIndex = _RlPolicySimpleBcmMibIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 2, 4, 1, 1),
    _RlPolicySimpleBcmMibIndex_Type()
)
rlPolicySimpleBcmMibIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicySimpleBcmMibIndex.setStatus("mandatory")


class _RlPolicySimpleBcmMibDescription_Type(DisplayString):
    """Custom type rlPolicySimpleBcmMibDescription based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RlPolicySimpleBcmMibDescription_Type.__name__ = "DisplayString"
_RlPolicySimpleBcmMibDescription_Object = MibTableColumn
rlPolicySimpleBcmMibDescription = _RlPolicySimpleBcmMibDescription_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 2, 4, 1, 2),
    _RlPolicySimpleBcmMibDescription_Type()
)
rlPolicySimpleBcmMibDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleBcmMibDescription.setStatus("mandatory")
_RlPolicySimpleBcmMibProfileType_Type = RlPolicySimpleBcmMibProfileType
_RlPolicySimpleBcmMibProfileType_Object = MibTableColumn
rlPolicySimpleBcmMibProfileType = _RlPolicySimpleBcmMibProfileType_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 2, 4, 1, 3),
    _RlPolicySimpleBcmMibProfileType_Type()
)
rlPolicySimpleBcmMibProfileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleBcmMibProfileType.setStatus("mandatory")


class _RlPolicySimpleBcmMibRate_Type(Integer32):
    """Custom type rlPolicySimpleBcmMibRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RlPolicySimpleBcmMibRate_Type.__name__ = "Integer32"
_RlPolicySimpleBcmMibRate_Object = MibTableColumn
rlPolicySimpleBcmMibRate = _RlPolicySimpleBcmMibRate_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 2, 4, 1, 4),
    _RlPolicySimpleBcmMibRate_Type()
)
rlPolicySimpleBcmMibRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleBcmMibRate.setStatus("mandatory")


class _RlPolicySimpleBcmMibBurstSize_Type(Integer32):
    """Custom type rlPolicySimpleBcmMibBurstSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RlPolicySimpleBcmMibBurstSize_Type.__name__ = "Integer32"
_RlPolicySimpleBcmMibBurstSize_Object = MibTableColumn
rlPolicySimpleBcmMibBurstSize = _RlPolicySimpleBcmMibBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 2, 4, 1, 5),
    _RlPolicySimpleBcmMibBurstSize_Type()
)
rlPolicySimpleBcmMibBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleBcmMibBurstSize.setStatus("mandatory")


class _RlPolicySimpleBcmMibChangeTosOrDscp_Type(TruthValue):
    """Custom type rlPolicySimpleBcmMibChangeTosOrDscp based on TruthValue"""
    defaultValue = 2


_RlPolicySimpleBcmMibChangeTosOrDscp_Type.__name__ = "TruthValue"
_RlPolicySimpleBcmMibChangeTosOrDscp_Object = MibTableColumn
rlPolicySimpleBcmMibChangeTosOrDscp = _RlPolicySimpleBcmMibChangeTosOrDscp_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 2, 4, 1, 6),
    _RlPolicySimpleBcmMibChangeTosOrDscp_Type()
)
rlPolicySimpleBcmMibChangeTosOrDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleBcmMibChangeTosOrDscp.setStatus("mandatory")


class _RlPolicySimpleBcmMibNewTosOrDscp_Type(Integer32):
    """Custom type rlPolicySimpleBcmMibNewTosOrDscp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RlPolicySimpleBcmMibNewTosOrDscp_Type.__name__ = "Integer32"
_RlPolicySimpleBcmMibNewTosOrDscp_Object = MibTableColumn
rlPolicySimpleBcmMibNewTosOrDscp = _RlPolicySimpleBcmMibNewTosOrDscp_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 2, 4, 1, 7),
    _RlPolicySimpleBcmMibNewTosOrDscp_Type()
)
rlPolicySimpleBcmMibNewTosOrDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleBcmMibNewTosOrDscp.setStatus("mandatory")
_RlPolicySimpleBcmMibStatus_Type = RowStatus
_RlPolicySimpleBcmMibStatus_Object = MibTableColumn
rlPolicySimpleBcmMibStatus = _RlPolicySimpleBcmMibStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 2, 4, 1, 8),
    _RlPolicySimpleBcmMibStatus_Type()
)
rlPolicySimpleBcmMibStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleBcmMibStatus.setStatus("mandatory")
_RlPolicySimpleBcmMibRulesTable_Object = MibTable
rlPolicySimpleBcmMibRulesTable = _RlPolicySimpleBcmMibRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 2, 5)
)
if mibBuilder.loadTexts:
    rlPolicySimpleBcmMibRulesTable.setStatus("mandatory")
_RlPolicySimpleBcmMibRulesEntry_Object = MibTableRow
rlPolicySimpleBcmMibRulesEntry = _RlPolicySimpleBcmMibRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 2, 5, 1)
)
rlPolicySimpleBcmMibRulesEntry.setIndexNames(
    (0, "BROADCOM-MIB", "rlPolicySimpleBcmMibRulesIndex"),
)
if mibBuilder.loadTexts:
    rlPolicySimpleBcmMibRulesEntry.setStatus("mandatory")


class _RlPolicySimpleBcmMibRulesIndex_Type(Integer32):
    """Custom type rlPolicySimpleBcmMibRulesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1048576),
    )


_RlPolicySimpleBcmMibRulesIndex_Type.__name__ = "Integer32"
_RlPolicySimpleBcmMibRulesIndex_Object = MibTableColumn
rlPolicySimpleBcmMibRulesIndex = _RlPolicySimpleBcmMibRulesIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 2, 5, 1, 1),
    _RlPolicySimpleBcmMibRulesIndex_Type()
)
rlPolicySimpleBcmMibRulesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicySimpleBcmMibRulesIndex.setStatus("mandatory")


class _RlPolicySimpleBcmMibRulesDescription_Type(DisplayString):
    """Custom type rlPolicySimpleBcmMibRulesDescription based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RlPolicySimpleBcmMibRulesDescription_Type.__name__ = "DisplayString"
_RlPolicySimpleBcmMibRulesDescription_Object = MibTableColumn
rlPolicySimpleBcmMibRulesDescription = _RlPolicySimpleBcmMibRulesDescription_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 2, 5, 1, 2),
    _RlPolicySimpleBcmMibRulesDescription_Type()
)
rlPolicySimpleBcmMibRulesDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleBcmMibRulesDescription.setStatus("mandatory")


class _RlPolicySimpleBcmMibRulesDstMac_Type(OctetString):
    """Custom type rlPolicySimpleBcmMibRulesDstMac based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_RlPolicySimpleBcmMibRulesDstMac_Type.__name__ = "OctetString"
_RlPolicySimpleBcmMibRulesDstMac_Object = MibTableColumn
rlPolicySimpleBcmMibRulesDstMac = _RlPolicySimpleBcmMibRulesDstMac_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 2, 5, 1, 3),
    _RlPolicySimpleBcmMibRulesDstMac_Type()
)
rlPolicySimpleBcmMibRulesDstMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleBcmMibRulesDstMac.setStatus("mandatory")


class _RlPolicySimpleBcmMibRulesSrcMac_Type(OctetString):
    """Custom type rlPolicySimpleBcmMibRulesSrcMac based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_RlPolicySimpleBcmMibRulesSrcMac_Type.__name__ = "OctetString"
_RlPolicySimpleBcmMibRulesSrcMac_Object = MibTableColumn
rlPolicySimpleBcmMibRulesSrcMac = _RlPolicySimpleBcmMibRulesSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 2, 5, 1, 4),
    _RlPolicySimpleBcmMibRulesSrcMac_Type()
)
rlPolicySimpleBcmMibRulesSrcMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleBcmMibRulesSrcMac.setStatus("mandatory")


class _RlPolicySimpleBcmMibRulesVpt_Type(Integer32):
    """Custom type rlPolicySimpleBcmMibRulesVpt based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RlPolicySimpleBcmMibRulesVpt_Type.__name__ = "Integer32"
_RlPolicySimpleBcmMibRulesVpt_Object = MibTableColumn
rlPolicySimpleBcmMibRulesVpt = _RlPolicySimpleBcmMibRulesVpt_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 2, 5, 1, 5),
    _RlPolicySimpleBcmMibRulesVpt_Type()
)
rlPolicySimpleBcmMibRulesVpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleBcmMibRulesVpt.setStatus("mandatory")


class _RlPolicySimpleBcmMibRulesVid_Type(Integer32):
    """Custom type rlPolicySimpleBcmMibRulesVid based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_RlPolicySimpleBcmMibRulesVid_Type.__name__ = "Integer32"
_RlPolicySimpleBcmMibRulesVid_Object = MibTableColumn
rlPolicySimpleBcmMibRulesVid = _RlPolicySimpleBcmMibRulesVid_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 2, 5, 1, 6),
    _RlPolicySimpleBcmMibRulesVid_Type()
)
rlPolicySimpleBcmMibRulesVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleBcmMibRulesVid.setStatus("mandatory")


class _RlPolicySimpleBcmMibRulesEthType_Type(Integer32):
    """Custom type rlPolicySimpleBcmMibRulesEthType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlPolicySimpleBcmMibRulesEthType_Type.__name__ = "Integer32"
_RlPolicySimpleBcmMibRulesEthType_Object = MibTableColumn
rlPolicySimpleBcmMibRulesEthType = _RlPolicySimpleBcmMibRulesEthType_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 2, 5, 1, 7),
    _RlPolicySimpleBcmMibRulesEthType_Type()
)
rlPolicySimpleBcmMibRulesEthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleBcmMibRulesEthType.setStatus("mandatory")


class _RlPolicySimpleBcmMibRulesTosOrDscp_Type(Integer32):
    """Custom type rlPolicySimpleBcmMibRulesTosOrDscp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RlPolicySimpleBcmMibRulesTosOrDscp_Type.__name__ = "Integer32"
_RlPolicySimpleBcmMibRulesTosOrDscp_Object = MibTableColumn
rlPolicySimpleBcmMibRulesTosOrDscp = _RlPolicySimpleBcmMibRulesTosOrDscp_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 2, 5, 1, 8),
    _RlPolicySimpleBcmMibRulesTosOrDscp_Type()
)
rlPolicySimpleBcmMibRulesTosOrDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleBcmMibRulesTosOrDscp.setStatus("mandatory")


class _RlPolicySimpleBcmMibRulesProtocol_Type(Integer32):
    """Custom type rlPolicySimpleBcmMibRulesProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RlPolicySimpleBcmMibRulesProtocol_Type.__name__ = "Integer32"
_RlPolicySimpleBcmMibRulesProtocol_Object = MibTableColumn
rlPolicySimpleBcmMibRulesProtocol = _RlPolicySimpleBcmMibRulesProtocol_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 2, 5, 1, 9),
    _RlPolicySimpleBcmMibRulesProtocol_Type()
)
rlPolicySimpleBcmMibRulesProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleBcmMibRulesProtocol.setStatus("mandatory")


class _RlPolicySimpleBcmMibRulesSrcIp_Type(IpAddress):
    """Custom type rlPolicySimpleBcmMibRulesSrcIp based on IpAddress"""
    defaultHexValue = "00000000"


_RlPolicySimpleBcmMibRulesSrcIp_Type.__name__ = "IpAddress"
_RlPolicySimpleBcmMibRulesSrcIp_Object = MibTableColumn
rlPolicySimpleBcmMibRulesSrcIp = _RlPolicySimpleBcmMibRulesSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 2, 5, 1, 10),
    _RlPolicySimpleBcmMibRulesSrcIp_Type()
)
rlPolicySimpleBcmMibRulesSrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleBcmMibRulesSrcIp.setStatus("mandatory")


class _RlPolicySimpleBcmMibRulesSrcIpMask_Type(Integer32):
    """Custom type rlPolicySimpleBcmMibRulesSrcIpMask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_RlPolicySimpleBcmMibRulesSrcIpMask_Type.__name__ = "Integer32"
_RlPolicySimpleBcmMibRulesSrcIpMask_Object = MibTableColumn
rlPolicySimpleBcmMibRulesSrcIpMask = _RlPolicySimpleBcmMibRulesSrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 2, 5, 1, 11),
    _RlPolicySimpleBcmMibRulesSrcIpMask_Type()
)
rlPolicySimpleBcmMibRulesSrcIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleBcmMibRulesSrcIpMask.setStatus("mandatory")


class _RlPolicySimpleBcmMibRulesDstIp_Type(IpAddress):
    """Custom type rlPolicySimpleBcmMibRulesDstIp based on IpAddress"""
    defaultHexValue = "00000000"


_RlPolicySimpleBcmMibRulesDstIp_Type.__name__ = "IpAddress"
_RlPolicySimpleBcmMibRulesDstIp_Object = MibTableColumn
rlPolicySimpleBcmMibRulesDstIp = _RlPolicySimpleBcmMibRulesDstIp_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 2, 5, 1, 12),
    _RlPolicySimpleBcmMibRulesDstIp_Type()
)
rlPolicySimpleBcmMibRulesDstIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleBcmMibRulesDstIp.setStatus("mandatory")


class _RlPolicySimpleBcmMibRulesDstIpMask_Type(Integer32):
    """Custom type rlPolicySimpleBcmMibRulesDstIpMask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_RlPolicySimpleBcmMibRulesDstIpMask_Type.__name__ = "Integer32"
_RlPolicySimpleBcmMibRulesDstIpMask_Object = MibTableColumn
rlPolicySimpleBcmMibRulesDstIpMask = _RlPolicySimpleBcmMibRulesDstIpMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 2, 5, 1, 13),
    _RlPolicySimpleBcmMibRulesDstIpMask_Type()
)
rlPolicySimpleBcmMibRulesDstIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleBcmMibRulesDstIpMask.setStatus("mandatory")


class _RlPolicySimpleBcmMibRulesSrcPort_Type(Integer32):
    """Custom type rlPolicySimpleBcmMibRulesSrcPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlPolicySimpleBcmMibRulesSrcPort_Type.__name__ = "Integer32"
_RlPolicySimpleBcmMibRulesSrcPort_Object = MibTableColumn
rlPolicySimpleBcmMibRulesSrcPort = _RlPolicySimpleBcmMibRulesSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 2, 5, 1, 14),
    _RlPolicySimpleBcmMibRulesSrcPort_Type()
)
rlPolicySimpleBcmMibRulesSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleBcmMibRulesSrcPort.setStatus("mandatory")


class _RlPolicySimpleBcmMibRulesDstPort_Type(Integer32):
    """Custom type rlPolicySimpleBcmMibRulesDstPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlPolicySimpleBcmMibRulesDstPort_Type.__name__ = "Integer32"
_RlPolicySimpleBcmMibRulesDstPort_Object = MibTableColumn
rlPolicySimpleBcmMibRulesDstPort = _RlPolicySimpleBcmMibRulesDstPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 2, 5, 1, 15),
    _RlPolicySimpleBcmMibRulesDstPort_Type()
)
rlPolicySimpleBcmMibRulesDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleBcmMibRulesDstPort.setStatus("mandatory")
_RlPolicySimpleBcmMibRulesInIfIndexList_Type = PortList
_RlPolicySimpleBcmMibRulesInIfIndexList_Object = MibTableColumn
rlPolicySimpleBcmMibRulesInIfIndexList = _RlPolicySimpleBcmMibRulesInIfIndexList_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 2, 5, 1, 16),
    _RlPolicySimpleBcmMibRulesInIfIndexList_Type()
)
rlPolicySimpleBcmMibRulesInIfIndexList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleBcmMibRulesInIfIndexList.setStatus("mandatory")
_RlPolicySimpleBcmMibRulesOutIfIndexList_Type = PortList
_RlPolicySimpleBcmMibRulesOutIfIndexList_Object = MibTableColumn
rlPolicySimpleBcmMibRulesOutIfIndexList = _RlPolicySimpleBcmMibRulesOutIfIndexList_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 2, 5, 1, 17),
    _RlPolicySimpleBcmMibRulesOutIfIndexList_Type()
)
rlPolicySimpleBcmMibRulesOutIfIndexList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleBcmMibRulesOutIfIndexList.setStatus("mandatory")


class _RlPolicySimpleBcmMibRulesAction_Type(Integer32):
    """Custom type rlPolicySimpleBcmMibRulesAction based on Integer32"""
    defaultValue = 4

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
        *(("block", 1),
          ("blockAndTrap", 2),
          ("permitAndTrap", 3),
          ("permit", 4))
    )


_RlPolicySimpleBcmMibRulesAction_Type.__name__ = "Integer32"
_RlPolicySimpleBcmMibRulesAction_Object = MibTableColumn
rlPolicySimpleBcmMibRulesAction = _RlPolicySimpleBcmMibRulesAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 2, 5, 1, 18),
    _RlPolicySimpleBcmMibRulesAction_Type()
)
rlPolicySimpleBcmMibRulesAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleBcmMibRulesAction.setStatus("mandatory")


class _RlPolicySimpleBcmMibRulesProfilePointer_Type(Integer32):
    """Custom type rlPolicySimpleBcmMibRulesProfilePointer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RlPolicySimpleBcmMibRulesProfilePointer_Type.__name__ = "Integer32"
_RlPolicySimpleBcmMibRulesProfilePointer_Object = MibTableColumn
rlPolicySimpleBcmMibRulesProfilePointer = _RlPolicySimpleBcmMibRulesProfilePointer_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 2, 5, 1, 19),
    _RlPolicySimpleBcmMibRulesProfilePointer_Type()
)
rlPolicySimpleBcmMibRulesProfilePointer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleBcmMibRulesProfilePointer.setStatus("mandatory")


class _RlPolicySimpleBcmMibRulesBitsUsed_Type(OctetString):
    """Custom type rlPolicySimpleBcmMibRulesBitsUsed based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_RlPolicySimpleBcmMibRulesBitsUsed_Type.__name__ = "OctetString"
_RlPolicySimpleBcmMibRulesBitsUsed_Object = MibTableColumn
rlPolicySimpleBcmMibRulesBitsUsed = _RlPolicySimpleBcmMibRulesBitsUsed_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 2, 5, 1, 20),
    _RlPolicySimpleBcmMibRulesBitsUsed_Type()
)
rlPolicySimpleBcmMibRulesBitsUsed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleBcmMibRulesBitsUsed.setStatus("mandatory")
_RlPolicySimpleBcmMibRulesStatus_Type = RowStatus
_RlPolicySimpleBcmMibRulesStatus_Object = MibTableColumn
rlPolicySimpleBcmMibRulesStatus = _RlPolicySimpleBcmMibRulesStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 2, 5, 1, 21),
    _RlPolicySimpleBcmMibRulesStatus_Type()
)
rlPolicySimpleBcmMibRulesStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleBcmMibRulesStatus.setStatus("mandatory")
_RlBcmRateLimit_ObjectIdentity = ObjectIdentity
rlBcmRateLimit = _RlBcmRateLimit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 68, 3)
)
_RlBcmPacketRateLimitBroadcstMulticastUnicastUnknown_Type = Integer32
_RlBcmPacketRateLimitBroadcstMulticastUnicastUnknown_Object = MibScalar
rlBcmPacketRateLimitBroadcstMulticastUnicastUnknown = _RlBcmPacketRateLimitBroadcstMulticastUnicastUnknown_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 3, 1),
    _RlBcmPacketRateLimitBroadcstMulticastUnicastUnknown_Type()
)
rlBcmPacketRateLimitBroadcstMulticastUnicastUnknown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmPacketRateLimitBroadcstMulticastUnicastUnknown.setStatus("mandatory")


class _RlBcmPacketRateLimitMulticastEnable_Type(Integer32):
    """Custom type rlBcmPacketRateLimitMulticastEnable based on Integer32"""
    defaultValue = 2

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


_RlBcmPacketRateLimitMulticastEnable_Type.__name__ = "Integer32"
_RlBcmPacketRateLimitMulticastEnable_Object = MibScalar
rlBcmPacketRateLimitMulticastEnable = _RlBcmPacketRateLimitMulticastEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 3, 2),
    _RlBcmPacketRateLimitMulticastEnable_Type()
)
rlBcmPacketRateLimitMulticastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmPacketRateLimitMulticastEnable.setStatus("mandatory")


class _RlBcmPacketRateLimitBroadcstEnable_Type(Integer32):
    """Custom type rlBcmPacketRateLimitBroadcstEnable based on Integer32"""
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


_RlBcmPacketRateLimitBroadcstEnable_Type.__name__ = "Integer32"
_RlBcmPacketRateLimitBroadcstEnable_Object = MibScalar
rlBcmPacketRateLimitBroadcstEnable = _RlBcmPacketRateLimitBroadcstEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 3, 3),
    _RlBcmPacketRateLimitBroadcstEnable_Type()
)
rlBcmPacketRateLimitBroadcstEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmPacketRateLimitBroadcstEnable.setStatus("mandatory")


class _RlBcmPacketRateLimitUnicastUnknownEnable_Type(Integer32):
    """Custom type rlBcmPacketRateLimitUnicastUnknownEnable based on Integer32"""
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


_RlBcmPacketRateLimitUnicastUnknownEnable_Type.__name__ = "Integer32"
_RlBcmPacketRateLimitUnicastUnknownEnable_Object = MibScalar
rlBcmPacketRateLimitUnicastUnknownEnable = _RlBcmPacketRateLimitUnicastUnknownEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 3, 4),
    _RlBcmPacketRateLimitUnicastUnknownEnable_Type()
)
rlBcmPacketRateLimitUnicastUnknownEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmPacketRateLimitUnicastUnknownEnable.setStatus("mandatory")
_RlBcmQoSRateLimit_ObjectIdentity = ObjectIdentity
rlBcmQoSRateLimit = _RlBcmQoSRateLimit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 68, 4)
)
_RlBcmQoSRateLimitIndexCounter_Type = Integer32
_RlBcmQoSRateLimitIndexCounter_Object = MibScalar
rlBcmQoSRateLimitIndexCounter = _RlBcmQoSRateLimitIndexCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 4, 1),
    _RlBcmQoSRateLimitIndexCounter_Type()
)
rlBcmQoSRateLimitIndexCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBcmQoSRateLimitIndexCounter.setStatus("mandatory")
_RlBcmQoSRateLimitTable_Object = MibTable
rlBcmQoSRateLimitTable = _RlBcmQoSRateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 4, 2)
)
if mibBuilder.loadTexts:
    rlBcmQoSRateLimitTable.setStatus("mandatory")
_RlBcmQoSRateLimitEntry_Object = MibTableRow
rlBcmQoSRateLimitEntry = _RlBcmQoSRateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 4, 2, 1)
)
rlBcmQoSRateLimitEntry.setIndexNames(
    (0, "BROADCOM-MIB", "rlBcmQoSRateLimitType"),
    (0, "BROADCOM-MIB", "rlBcmQoSRateLimitName"),
    (0, "BROADCOM-MIB", "rlBcmQoSRateLimitIndex"),
)
if mibBuilder.loadTexts:
    rlBcmQoSRateLimitEntry.setStatus("mandatory")
_RlBcmQoSRateLimitType_Type = RlBcmQoSRateLimitType
_RlBcmQoSRateLimitType_Object = MibTableColumn
rlBcmQoSRateLimitType = _RlBcmQoSRateLimitType_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 4, 2, 1, 1),
    _RlBcmQoSRateLimitType_Type()
)
rlBcmQoSRateLimitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmQoSRateLimitType.setStatus("mandatory")


class _RlBcmQoSRateLimitName_Type(DisplayString):
    """Custom type rlBcmQoSRateLimitName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RlBcmQoSRateLimitName_Type.__name__ = "DisplayString"
_RlBcmQoSRateLimitName_Object = MibTableColumn
rlBcmQoSRateLimitName = _RlBcmQoSRateLimitName_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 4, 2, 1, 2),
    _RlBcmQoSRateLimitName_Type()
)
rlBcmQoSRateLimitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmQoSRateLimitName.setStatus("mandatory")
_RlBcmQoSRateLimitIndex_Type = Integer32
_RlBcmQoSRateLimitIndex_Object = MibTableColumn
rlBcmQoSRateLimitIndex = _RlBcmQoSRateLimitIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 4, 2, 1, 3),
    _RlBcmQoSRateLimitIndex_Type()
)
rlBcmQoSRateLimitIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmQoSRateLimitIndex.setStatus("mandatory")


class _RlBcmQoSRateLimitAclsNameOrFlow_Type(OctetString):
    """Custom type rlBcmQoSRateLimitAclsNameOrFlow based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_RlBcmQoSRateLimitAclsNameOrFlow_Type.__name__ = "OctetString"
_RlBcmQoSRateLimitAclsNameOrFlow_Object = MibTableColumn
rlBcmQoSRateLimitAclsNameOrFlow = _RlBcmQoSRateLimitAclsNameOrFlow_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 4, 2, 1, 4),
    _RlBcmQoSRateLimitAclsNameOrFlow_Type()
)
rlBcmQoSRateLimitAclsNameOrFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmQoSRateLimitAclsNameOrFlow.setStatus("mandatory")


class _RlBcmQoSRateLimitPortsOrInterfaces_Type(DisplayString):
    """Custom type rlBcmQoSRateLimitPortsOrInterfaces based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_RlBcmQoSRateLimitPortsOrInterfaces_Type.__name__ = "DisplayString"
_RlBcmQoSRateLimitPortsOrInterfaces_Object = MibTableColumn
rlBcmQoSRateLimitPortsOrInterfaces = _RlBcmQoSRateLimitPortsOrInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 4, 2, 1, 5),
    _RlBcmQoSRateLimitPortsOrInterfaces_Type()
)
rlBcmQoSRateLimitPortsOrInterfaces.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmQoSRateLimitPortsOrInterfaces.setStatus("mandatory")


class _RlBcmQoSRateLimitRatePriority_Type(Integer32):
    """Custom type rlBcmQoSRateLimitRatePriority based on Integer32"""
    defaultValue = 0


_RlBcmQoSRateLimitRatePriority_Type.__name__ = "Integer32"
_RlBcmQoSRateLimitRatePriority_Object = MibTableColumn
rlBcmQoSRateLimitRatePriority = _RlBcmQoSRateLimitRatePriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 4, 2, 1, 6),
    _RlBcmQoSRateLimitRatePriority_Type()
)
rlBcmQoSRateLimitRatePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmQoSRateLimitRatePriority.setStatus("mandatory")


class _RlBcmQoSRateLimitBurstSizeTosMask_Type(Integer32):
    """Custom type rlBcmQoSRateLimitBurstSizeTosMask based on Integer32"""
    defaultValue = 0


_RlBcmQoSRateLimitBurstSizeTosMask_Type.__name__ = "Integer32"
_RlBcmQoSRateLimitBurstSizeTosMask_Object = MibTableColumn
rlBcmQoSRateLimitBurstSizeTosMask = _RlBcmQoSRateLimitBurstSizeTosMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 4, 2, 1, 7),
    _RlBcmQoSRateLimitBurstSizeTosMask_Type()
)
rlBcmQoSRateLimitBurstSizeTosMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmQoSRateLimitBurstSizeTosMask.setStatus("mandatory")


class _RlBcmQoSRateLimitDropOutProfile_Type(TruthValue):
    """Custom type rlBcmQoSRateLimitDropOutProfile based on TruthValue"""
    defaultValue = 2


_RlBcmQoSRateLimitDropOutProfile_Type.__name__ = "TruthValue"
_RlBcmQoSRateLimitDropOutProfile_Object = MibTableColumn
rlBcmQoSRateLimitDropOutProfile = _RlBcmQoSRateLimitDropOutProfile_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 4, 2, 1, 8),
    _RlBcmQoSRateLimitDropOutProfile_Type()
)
rlBcmQoSRateLimitDropOutProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmQoSRateLimitDropOutProfile.setStatus("mandatory")


class _RlBcmQoSRateLimitNewTos_Type(Integer32):
    """Custom type rlBcmQoSRateLimitNewTos based on Integer32"""
    defaultValue = 64


_RlBcmQoSRateLimitNewTos_Type.__name__ = "Integer32"
_RlBcmQoSRateLimitNewTos_Object = MibTableColumn
rlBcmQoSRateLimitNewTos = _RlBcmQoSRateLimitNewTos_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 4, 2, 1, 9),
    _RlBcmQoSRateLimitNewTos_Type()
)
rlBcmQoSRateLimitNewTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmQoSRateLimitNewTos.setStatus("mandatory")


class _RlBcmQoSRateLimitNewTosPrecedence_Type(Integer32):
    """Custom type rlBcmQoSRateLimitNewTosPrecedence based on Integer32"""
    defaultValue = 16


_RlBcmQoSRateLimitNewTosPrecedence_Type.__name__ = "Integer32"
_RlBcmQoSRateLimitNewTosPrecedence_Object = MibTableColumn
rlBcmQoSRateLimitNewTosPrecedence = _RlBcmQoSRateLimitNewTosPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 4, 2, 1, 10),
    _RlBcmQoSRateLimitNewTosPrecedence_Type()
)
rlBcmQoSRateLimitNewTosPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmQoSRateLimitNewTosPrecedence.setStatus("mandatory")
_RlBcmQoSRateLimitStatus_Type = RowStatus
_RlBcmQoSRateLimitStatus_Object = MibTableColumn
rlBcmQoSRateLimitStatus = _RlBcmQoSRateLimitStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 4, 2, 1, 11),
    _RlBcmQoSRateLimitStatus_Type()
)
rlBcmQoSRateLimitStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmQoSRateLimitStatus.setStatus("mandatory")
_RlBcmQoSRateLimitAclApplliedTable_Object = MibTable
rlBcmQoSRateLimitAclApplliedTable = _RlBcmQoSRateLimitAclApplliedTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 4, 3)
)
if mibBuilder.loadTexts:
    rlBcmQoSRateLimitAclApplliedTable.setStatus("mandatory")
_RlBcmQoSRateLimitAclApplliedEntry_Object = MibTableRow
rlBcmQoSRateLimitAclApplliedEntry = _RlBcmQoSRateLimitAclApplliedEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 4, 3, 1)
)
rlBcmQoSRateLimitAclApplliedEntry.setIndexNames(
    (0, "BROADCOM-MIB", "rlBcmQoSRateLimitAclName"),
    (0, "BROADCOM-MIB", "rlBcmQoSRateLimitAclApplliedIfIndex"),
)
if mibBuilder.loadTexts:
    rlBcmQoSRateLimitAclApplliedEntry.setStatus("mandatory")


class _RlBcmQoSRateLimitAclName_Type(DisplayString):
    """Custom type rlBcmQoSRateLimitAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RlBcmQoSRateLimitAclName_Type.__name__ = "DisplayString"
_RlBcmQoSRateLimitAclName_Object = MibTableColumn
rlBcmQoSRateLimitAclName = _RlBcmQoSRateLimitAclName_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 4, 3, 1, 1),
    _RlBcmQoSRateLimitAclName_Type()
)
rlBcmQoSRateLimitAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmQoSRateLimitAclName.setStatus("mandatory")
_RlBcmQoSRateLimitAclApplliedIfIndex_Type = Integer32
_RlBcmQoSRateLimitAclApplliedIfIndex_Object = MibTableColumn
rlBcmQoSRateLimitAclApplliedIfIndex = _RlBcmQoSRateLimitAclApplliedIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 4, 3, 1, 2),
    _RlBcmQoSRateLimitAclApplliedIfIndex_Type()
)
rlBcmQoSRateLimitAclApplliedIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmQoSRateLimitAclApplliedIfIndex.setStatus("mandatory")
_RlBcmQoSRateLimitAclApplliedType_Type = Integer32
_RlBcmQoSRateLimitAclApplliedType_Object = MibTableColumn
rlBcmQoSRateLimitAclApplliedType = _RlBcmQoSRateLimitAclApplliedType_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 4, 3, 1, 3),
    _RlBcmQoSRateLimitAclApplliedType_Type()
)
rlBcmQoSRateLimitAclApplliedType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmQoSRateLimitAclApplliedType.setStatus("mandatory")
_RlBcmQoSRateLimitAclApplliedStatus_Type = RowStatus
_RlBcmQoSRateLimitAclApplliedStatus_Object = MibTableColumn
rlBcmQoSRateLimitAclApplliedStatus = _RlBcmQoSRateLimitAclApplliedStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 4, 3, 1, 4),
    _RlBcmQoSRateLimitAclApplliedStatus_Type()
)
rlBcmQoSRateLimitAclApplliedStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmQoSRateLimitAclApplliedStatus.setStatus("mandatory")
_RlBcmQoSRateLimitIPflowTable_Object = MibTable
rlBcmQoSRateLimitIPflowTable = _RlBcmQoSRateLimitIPflowTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 4, 4)
)
if mibBuilder.loadTexts:
    rlBcmQoSRateLimitIPflowTable.setStatus("mandatory")
_RlBcmQoSRateLimitIPflowEntry_Object = MibTableRow
rlBcmQoSRateLimitIPflowEntry = _RlBcmQoSRateLimitIPflowEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 4, 4, 1)
)
rlBcmQoSRateLimitIPflowEntry.setIndexNames(
    (0, "BROADCOM-MIB", "rlBcmQoSRateLimitIPflowTos"),
    (0, "BROADCOM-MIB", "rlBcmQoSRateLimitIPflowTosMask"),
    (0, "BROADCOM-MIB", "rlBcmQoSRateLimitIPflowProtocol"),
    (0, "BROADCOM-MIB", "rlBcmQoSRateLimitIPflowSrcIp"),
    (0, "BROADCOM-MIB", "rlBcmQoSRateLimitIPflowSrcIpMask"),
    (0, "BROADCOM-MIB", "rlBcmQoSRateLimitIPflowDstIp"),
    (0, "BROADCOM-MIB", "rlBcmQoSRateLimitIPflowDstIpMask"),
    (0, "BROADCOM-MIB", "rlBcmQoSRateLimitIPflowSrcPort"),
    (0, "BROADCOM-MIB", "rlBcmQoSRateLimitIPflowDstPort"),
    (0, "BROADCOM-MIB", "rlBcmQoSRateLimitInIfindex"),
    (0, "BROADCOM-MIB", "rlBcmQoSRateLimitOutIfindex"),
)
if mibBuilder.loadTexts:
    rlBcmQoSRateLimitIPflowEntry.setStatus("mandatory")
_RlBcmQoSRateLimitIPflowTos_Type = Integer32
_RlBcmQoSRateLimitIPflowTos_Object = MibTableColumn
rlBcmQoSRateLimitIPflowTos = _RlBcmQoSRateLimitIPflowTos_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 4, 4, 1, 1),
    _RlBcmQoSRateLimitIPflowTos_Type()
)
rlBcmQoSRateLimitIPflowTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmQoSRateLimitIPflowTos.setStatus("mandatory")
_RlBcmQoSRateLimitIPflowTosMask_Type = Integer32
_RlBcmQoSRateLimitIPflowTosMask_Object = MibTableColumn
rlBcmQoSRateLimitIPflowTosMask = _RlBcmQoSRateLimitIPflowTosMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 4, 4, 1, 2),
    _RlBcmQoSRateLimitIPflowTosMask_Type()
)
rlBcmQoSRateLimitIPflowTosMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmQoSRateLimitIPflowTosMask.setStatus("mandatory")
_RlBcmQoSRateLimitIPflowProtocol_Type = Integer32
_RlBcmQoSRateLimitIPflowProtocol_Object = MibTableColumn
rlBcmQoSRateLimitIPflowProtocol = _RlBcmQoSRateLimitIPflowProtocol_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 4, 4, 1, 3),
    _RlBcmQoSRateLimitIPflowProtocol_Type()
)
rlBcmQoSRateLimitIPflowProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmQoSRateLimitIPflowProtocol.setStatus("mandatory")
_RlBcmQoSRateLimitIPflowSrcIp_Type = IpAddress
_RlBcmQoSRateLimitIPflowSrcIp_Object = MibTableColumn
rlBcmQoSRateLimitIPflowSrcIp = _RlBcmQoSRateLimitIPflowSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 4, 4, 1, 4),
    _RlBcmQoSRateLimitIPflowSrcIp_Type()
)
rlBcmQoSRateLimitIPflowSrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmQoSRateLimitIPflowSrcIp.setStatus("mandatory")
_RlBcmQoSRateLimitIPflowSrcIpMask_Type = IpAddress
_RlBcmQoSRateLimitIPflowSrcIpMask_Object = MibTableColumn
rlBcmQoSRateLimitIPflowSrcIpMask = _RlBcmQoSRateLimitIPflowSrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 4, 4, 1, 5),
    _RlBcmQoSRateLimitIPflowSrcIpMask_Type()
)
rlBcmQoSRateLimitIPflowSrcIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmQoSRateLimitIPflowSrcIpMask.setStatus("mandatory")
_RlBcmQoSRateLimitIPflowDstIp_Type = IpAddress
_RlBcmQoSRateLimitIPflowDstIp_Object = MibTableColumn
rlBcmQoSRateLimitIPflowDstIp = _RlBcmQoSRateLimitIPflowDstIp_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 4, 4, 1, 6),
    _RlBcmQoSRateLimitIPflowDstIp_Type()
)
rlBcmQoSRateLimitIPflowDstIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmQoSRateLimitIPflowDstIp.setStatus("mandatory")
_RlBcmQoSRateLimitIPflowDstIpMask_Type = IpAddress
_RlBcmQoSRateLimitIPflowDstIpMask_Object = MibTableColumn
rlBcmQoSRateLimitIPflowDstIpMask = _RlBcmQoSRateLimitIPflowDstIpMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 4, 4, 1, 7),
    _RlBcmQoSRateLimitIPflowDstIpMask_Type()
)
rlBcmQoSRateLimitIPflowDstIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmQoSRateLimitIPflowDstIpMask.setStatus("mandatory")
_RlBcmQoSRateLimitIPflowSrcPort_Type = Integer32
_RlBcmQoSRateLimitIPflowSrcPort_Object = MibTableColumn
rlBcmQoSRateLimitIPflowSrcPort = _RlBcmQoSRateLimitIPflowSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 4, 4, 1, 8),
    _RlBcmQoSRateLimitIPflowSrcPort_Type()
)
rlBcmQoSRateLimitIPflowSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmQoSRateLimitIPflowSrcPort.setStatus("mandatory")
_RlBcmQoSRateLimitIPflowDstPort_Type = Integer32
_RlBcmQoSRateLimitIPflowDstPort_Object = MibTableColumn
rlBcmQoSRateLimitIPflowDstPort = _RlBcmQoSRateLimitIPflowDstPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 4, 4, 1, 9),
    _RlBcmQoSRateLimitIPflowDstPort_Type()
)
rlBcmQoSRateLimitIPflowDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmQoSRateLimitIPflowDstPort.setStatus("mandatory")
_RlBcmQoSRateLimitInIfindex_Type = Integer32
_RlBcmQoSRateLimitInIfindex_Object = MibTableColumn
rlBcmQoSRateLimitInIfindex = _RlBcmQoSRateLimitInIfindex_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 4, 4, 1, 10),
    _RlBcmQoSRateLimitInIfindex_Type()
)
rlBcmQoSRateLimitInIfindex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmQoSRateLimitInIfindex.setStatus("mandatory")
_RlBcmQoSRateLimitOutIfindex_Type = Integer32
_RlBcmQoSRateLimitOutIfindex_Object = MibTableColumn
rlBcmQoSRateLimitOutIfindex = _RlBcmQoSRateLimitOutIfindex_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 4, 4, 1, 11),
    _RlBcmQoSRateLimitOutIfindex_Type()
)
rlBcmQoSRateLimitOutIfindex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmQoSRateLimitOutIfindex.setStatus("mandatory")


class _RlBcmQoSRateLimitIPFlowType_Type(Integer32):
    """Custom type rlBcmQoSRateLimitIPFlowType based on Integer32"""
    defaultValue = 0


_RlBcmQoSRateLimitIPFlowType_Type.__name__ = "Integer32"
_RlBcmQoSRateLimitIPFlowType_Object = MibTableColumn
rlBcmQoSRateLimitIPFlowType = _RlBcmQoSRateLimitIPFlowType_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 4, 4, 1, 12),
    _RlBcmQoSRateLimitIPFlowType_Type()
)
rlBcmQoSRateLimitIPFlowType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmQoSRateLimitIPFlowType.setStatus("mandatory")


class _RlBcmQoSRateLimitIPFlowRule_Type(Integer32):
    """Custom type rlBcmQoSRateLimitIPFlowRule based on Integer32"""
    defaultValue = 0


_RlBcmQoSRateLimitIPFlowRule_Type.__name__ = "Integer32"
_RlBcmQoSRateLimitIPFlowRule_Object = MibTableColumn
rlBcmQoSRateLimitIPFlowRule = _RlBcmQoSRateLimitIPFlowRule_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 4, 4, 1, 13),
    _RlBcmQoSRateLimitIPFlowRule_Type()
)
rlBcmQoSRateLimitIPFlowRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmQoSRateLimitIPFlowRule.setStatus("mandatory")
_RlBcmQoSRateLimitIPflowStatus_Type = RowStatus
_RlBcmQoSRateLimitIPflowStatus_Object = MibTableColumn
rlBcmQoSRateLimitIPflowStatus = _RlBcmQoSRateLimitIPflowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 4, 4, 1, 14),
    _RlBcmQoSRateLimitIPflowStatus_Type()
)
rlBcmQoSRateLimitIPflowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmQoSRateLimitIPflowStatus.setStatus("mandatory")


class _RlBcmQoSRateLimitQoSprecedenceMap_Type(OctetString):
    """Custom type rlBcmQoSRateLimitQoSprecedenceMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )
    fixed_length = 7


_RlBcmQoSRateLimitQoSprecedenceMap_Type.__name__ = "OctetString"
_RlBcmQoSRateLimitQoSprecedenceMap_Object = MibScalar
rlBcmQoSRateLimitQoSprecedenceMap = _RlBcmQoSRateLimitQoSprecedenceMap_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 4, 5),
    _RlBcmQoSRateLimitQoSprecedenceMap_Type()
)
rlBcmQoSRateLimitQoSprecedenceMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmQoSRateLimitQoSprecedenceMap.setStatus("mandatory")
_RlTosOverwriteMapMib_ObjectIdentity = ObjectIdentity
rlTosOverwriteMapMib = _RlTosOverwriteMapMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 68, 5)
)
_RlTosOverwriteMapTable_Object = MibTable
rlTosOverwriteMapTable = _RlTosOverwriteMapTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 5, 1)
)
if mibBuilder.loadTexts:
    rlTosOverwriteMapTable.setStatus("mandatory")
_RlTosOverwriteMapEntry_Object = MibTableRow
rlTosOverwriteMapEntry = _RlTosOverwriteMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 5, 1, 1)
)
rlTosOverwriteMapEntry.setIndexNames(
    (0, "BROADCOM-MIB", "rlTosOverwriteMapName"),
    (0, "BROADCOM-MIB", "rlTosOverwriteMapRange"),
)
if mibBuilder.loadTexts:
    rlTosOverwriteMapEntry.setStatus("mandatory")


class _RlTosOverwriteMapName_Type(DisplayString):
    """Custom type rlTosOverwriteMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_RlTosOverwriteMapName_Type.__name__ = "DisplayString"
_RlTosOverwriteMapName_Object = MibTableColumn
rlTosOverwriteMapName = _RlTosOverwriteMapName_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 5, 1, 1, 1),
    _RlTosOverwriteMapName_Type()
)
rlTosOverwriteMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlTosOverwriteMapName.setStatus("mandatory")


class _RlTosOverwriteMapRange_Type(Integer32):
    """Custom type rlTosOverwriteMapRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              63,
              255)
        )
    )
    namedValues = NamedValues(
        *(("bits", 7),
          ("tos", 63),
          ("byte", 255))
    )


_RlTosOverwriteMapRange_Type.__name__ = "Integer32"
_RlTosOverwriteMapRange_Object = MibTableColumn
rlTosOverwriteMapRange = _RlTosOverwriteMapRange_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 5, 1, 1, 2),
    _RlTosOverwriteMapRange_Type()
)
rlTosOverwriteMapRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTosOverwriteMapRange.setStatus("mandatory")


class _RlTosOverwriteMapMapping_Type(OctetString):
    """Custom type rlTosOverwriteMapMapping based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_RlTosOverwriteMapMapping_Type.__name__ = "OctetString"
_RlTosOverwriteMapMapping_Object = MibTableColumn
rlTosOverwriteMapMapping = _RlTosOverwriteMapMapping_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 5, 1, 1, 3),
    _RlTosOverwriteMapMapping_Type()
)
rlTosOverwriteMapMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTosOverwriteMapMapping.setStatus("mandatory")
_RlTosOverwriteMapPortList_Type = PortList
_RlTosOverwriteMapPortList_Object = MibTableColumn
rlTosOverwriteMapPortList = _RlTosOverwriteMapPortList_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 5, 1, 1, 4),
    _RlTosOverwriteMapPortList_Type()
)
rlTosOverwriteMapPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTosOverwriteMapPortList.setStatus("mandatory")
_RlTosOverwriteMapStatus_Type = RowStatus
_RlTosOverwriteMapStatus_Object = MibTableColumn
rlTosOverwriteMapStatus = _RlTosOverwriteMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 5, 1, 1, 5),
    _RlTosOverwriteMapStatus_Type()
)
rlTosOverwriteMapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTosOverwriteMapStatus.setStatus("mandatory")
_RlBcmACLMib_ObjectIdentity = ObjectIdentity
rlBcmACLMib = _RlBcmACLMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 68, 6)
)
_RlBcmACLMibVersion_Type = Integer32
_RlBcmACLMibVersion_Object = MibScalar
rlBcmACLMibVersion = _RlBcmACLMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 6, 1),
    _RlBcmACLMibVersion_Type()
)
rlBcmACLMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBcmACLMibVersion.setStatus("mandatory")
_RlBcmACLMaxNumberOfEntries_Type = Integer32
_RlBcmACLMaxNumberOfEntries_Object = MibScalar
rlBcmACLMaxNumberOfEntries = _RlBcmACLMaxNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 6, 2),
    _RlBcmACLMaxNumberOfEntries_Type()
)
rlBcmACLMaxNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBcmACLMaxNumberOfEntries.setStatus("mandatory")
_RlBcmACLNamesTable_Object = MibTable
rlBcmACLNamesTable = _RlBcmACLNamesTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 6, 3)
)
if mibBuilder.loadTexts:
    rlBcmACLNamesTable.setStatus("mandatory")
_RlBcmACLNamesEntry_Object = MibTableRow
rlBcmACLNamesEntry = _RlBcmACLNamesEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 6, 3, 1)
)
rlBcmACLNamesEntry.setIndexNames(
    (0, "BROADCOM-MIB", "rlBcmACLNamesName"),
)
if mibBuilder.loadTexts:
    rlBcmACLNamesEntry.setStatus("mandatory")


class _RlBcmACLNamesName_Type(DisplayString):
    """Custom type rlBcmACLNamesName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_RlBcmACLNamesName_Type.__name__ = "DisplayString"
_RlBcmACLNamesName_Object = MibTableColumn
rlBcmACLNamesName = _RlBcmACLNamesName_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 6, 3, 1, 1),
    _RlBcmACLNamesName_Type()
)
rlBcmACLNamesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBcmACLNamesName.setStatus("mandatory")
_RlBcmACLNamesID_Type = Integer32
_RlBcmACLNamesID_Object = MibTableColumn
rlBcmACLNamesID = _RlBcmACLNamesID_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 6, 3, 1, 2),
    _RlBcmACLNamesID_Type()
)
rlBcmACLNamesID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmACLNamesID.setStatus("mandatory")
_RlBcmACLNamesStatus_Type = RowStatus
_RlBcmACLNamesStatus_Object = MibTableColumn
rlBcmACLNamesStatus = _RlBcmACLNamesStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 6, 3, 1, 3),
    _RlBcmACLNamesStatus_Type()
)
rlBcmACLNamesStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmACLNamesStatus.setStatus("mandatory")
_RlBcmACLTable_Object = MibTable
rlBcmACLTable = _RlBcmACLTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 6, 4)
)
if mibBuilder.loadTexts:
    rlBcmACLTable.setStatus("mandatory")
_RlBcmACLEntry_Object = MibTableRow
rlBcmACLEntry = _RlBcmACLEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 6, 4, 1)
)
rlBcmACLEntry.setIndexNames(
    (0, "BROADCOM-MIB", "rlBcmAclID"),
    (0, "BROADCOM-MIB", "rlBcmAclRowIndex"),
)
if mibBuilder.loadTexts:
    rlBcmACLEntry.setStatus("mandatory")
_RlBcmAclID_Type = Integer32
_RlBcmAclID_Object = MibTableColumn
rlBcmAclID = _RlBcmAclID_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 6, 4, 1, 1),
    _RlBcmAclID_Type()
)
rlBcmAclID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmAclID.setStatus("mandatory")
_RlBcmAclRowIndex_Type = Integer32
_RlBcmAclRowIndex_Object = MibTableColumn
rlBcmAclRowIndex = _RlBcmAclRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 6, 4, 1, 2),
    _RlBcmAclRowIndex_Type()
)
rlBcmAclRowIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmAclRowIndex.setStatus("mandatory")


class _RlBcmAclAction_Type(Integer32):
    """Custom type rlBcmAclAction based on Integer32"""
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
        *(("permit", 1),
          ("permitAndLog", 2),
          ("deny", 3),
          ("denyAndLog", 4),
          ("logAndContinue", 5))
    )


_RlBcmAclAction_Type.__name__ = "Integer32"
_RlBcmAclAction_Object = MibTableColumn
rlBcmAclAction = _RlBcmAclAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 6, 4, 1, 3),
    _RlBcmAclAction_Type()
)
rlBcmAclAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmAclAction.setStatus("mandatory")


class _RlBcmAclIPflags_Type(Integer32):
    """Custom type rlBcmAclIPflags based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RlBcmAclIPflags_Type.__name__ = "Integer32"
_RlBcmAclIPflags_Object = MibTableColumn
rlBcmAclIPflags = _RlBcmAclIPflags_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 6, 4, 1, 4),
    _RlBcmAclIPflags_Type()
)
rlBcmAclIPflags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmAclIPflags.setStatus("mandatory")


class _RlBcmAclIPflagsMask_Type(Integer32):
    """Custom type rlBcmAclIPflagsMask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RlBcmAclIPflagsMask_Type.__name__ = "Integer32"
_RlBcmAclIPflagsMask_Object = MibTableColumn
rlBcmAclIPflagsMask = _RlBcmAclIPflagsMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 6, 4, 1, 5),
    _RlBcmAclIPflagsMask_Type()
)
rlBcmAclIPflagsMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmAclIPflagsMask.setStatus("mandatory")


class _RlBcmAclIPfragOffset_Type(Integer32):
    """Custom type rlBcmAclIPfragOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_RlBcmAclIPfragOffset_Type.__name__ = "Integer32"
_RlBcmAclIPfragOffset_Object = MibTableColumn
rlBcmAclIPfragOffset = _RlBcmAclIPfragOffset_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 6, 4, 1, 6),
    _RlBcmAclIPfragOffset_Type()
)
rlBcmAclIPfragOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmAclIPfragOffset.setStatus("mandatory")


class _RlBcmAclIPfragOffsetMask_Type(Integer32):
    """Custom type rlBcmAclIPfragOffsetMask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_RlBcmAclIPfragOffsetMask_Type.__name__ = "Integer32"
_RlBcmAclIPfragOffsetMask_Object = MibTableColumn
rlBcmAclIPfragOffsetMask = _RlBcmAclIPfragOffsetMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 6, 4, 1, 7),
    _RlBcmAclIPfragOffsetMask_Type()
)
rlBcmAclIPfragOffsetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmAclIPfragOffsetMask.setStatus("mandatory")


class _RlBcmAclIPprotocol_Type(Integer32):
    """Custom type rlBcmAclIPprotocol based on Integer32"""
    defaultValue = 256

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_RlBcmAclIPprotocol_Type.__name__ = "Integer32"
_RlBcmAclIPprotocol_Object = MibTableColumn
rlBcmAclIPprotocol = _RlBcmAclIPprotocol_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 6, 4, 1, 8),
    _RlBcmAclIPprotocol_Type()
)
rlBcmAclIPprotocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmAclIPprotocol.setStatus("mandatory")


class _RlBcmAclSrcIp_Type(IpAddress):
    """Custom type rlBcmAclSrcIp based on IpAddress"""
    defaultHexValue = "00000000"


_RlBcmAclSrcIp_Type.__name__ = "IpAddress"
_RlBcmAclSrcIp_Object = MibTableColumn
rlBcmAclSrcIp = _RlBcmAclSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 6, 4, 1, 9),
    _RlBcmAclSrcIp_Type()
)
rlBcmAclSrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmAclSrcIp.setStatus("mandatory")


class _RlBcmAclSrcIpMask_Type(IpAddress):
    """Custom type rlBcmAclSrcIpMask based on IpAddress"""
    defaultHexValue = "00000000"


_RlBcmAclSrcIpMask_Type.__name__ = "IpAddress"
_RlBcmAclSrcIpMask_Object = MibTableColumn
rlBcmAclSrcIpMask = _RlBcmAclSrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 6, 4, 1, 10),
    _RlBcmAclSrcIpMask_Type()
)
rlBcmAclSrcIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmAclSrcIpMask.setStatus("mandatory")


class _RlBcmAclDstIp_Type(IpAddress):
    """Custom type rlBcmAclDstIp based on IpAddress"""
    defaultHexValue = "00000000"


_RlBcmAclDstIp_Type.__name__ = "IpAddress"
_RlBcmAclDstIp_Object = MibTableColumn
rlBcmAclDstIp = _RlBcmAclDstIp_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 6, 4, 1, 11),
    _RlBcmAclDstIp_Type()
)
rlBcmAclDstIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmAclDstIp.setStatus("mandatory")


class _RlBcmAclDstIpMask_Type(IpAddress):
    """Custom type rlBcmAclDstIpMask based on IpAddress"""
    defaultHexValue = "00000000"


_RlBcmAclDstIpMask_Type.__name__ = "IpAddress"
_RlBcmAclDstIpMask_Object = MibTableColumn
rlBcmAclDstIpMask = _RlBcmAclDstIpMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 6, 4, 1, 12),
    _RlBcmAclDstIpMask_Type()
)
rlBcmAclDstIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmAclDstIpMask.setStatus("mandatory")


class _RlBcmAclSrcL4Port_Type(Integer32):
    """Custom type rlBcmAclSrcL4Port based on Integer32"""
    defaultValue = 65536

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_RlBcmAclSrcL4Port_Type.__name__ = "Integer32"
_RlBcmAclSrcL4Port_Object = MibTableColumn
rlBcmAclSrcL4Port = _RlBcmAclSrcL4Port_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 6, 4, 1, 13),
    _RlBcmAclSrcL4Port_Type()
)
rlBcmAclSrcL4Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmAclSrcL4Port.setStatus("mandatory")


class _RlBcmAclDstL4Port_Type(Integer32):
    """Custom type rlBcmAclDstL4Port based on Integer32"""
    defaultValue = 65536

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_RlBcmAclDstL4Port_Type.__name__ = "Integer32"
_RlBcmAclDstL4Port_Object = MibTableColumn
rlBcmAclDstL4Port = _RlBcmAclDstL4Port_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 6, 4, 1, 14),
    _RlBcmAclDstL4Port_Type()
)
rlBcmAclDstL4Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmAclDstL4Port.setStatus("mandatory")


class _RlBcmAclTCPbits_Type(Integer32):
    """Custom type rlBcmAclTCPbits based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RlBcmAclTCPbits_Type.__name__ = "Integer32"
_RlBcmAclTCPbits_Object = MibTableColumn
rlBcmAclTCPbits = _RlBcmAclTCPbits_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 6, 4, 1, 15),
    _RlBcmAclTCPbits_Type()
)
rlBcmAclTCPbits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmAclTCPbits.setStatus("mandatory")


class _RlBcmAclTCPbitsMask_Type(Integer32):
    """Custom type rlBcmAclTCPbitsMask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RlBcmAclTCPbitsMask_Type.__name__ = "Integer32"
_RlBcmAclTCPbitsMask_Object = MibTableColumn
rlBcmAclTCPbitsMask = _RlBcmAclTCPbitsMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 6, 4, 1, 16),
    _RlBcmAclTCPbitsMask_Type()
)
rlBcmAclTCPbitsMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmAclTCPbitsMask.setStatus("mandatory")
_RlBcmAclStatus_Type = RowStatus
_RlBcmAclStatus_Object = MibTableColumn
rlBcmAclStatus = _RlBcmAclStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 6, 4, 1, 17),
    _RlBcmAclStatus_Type()
)
rlBcmAclStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmAclStatus.setStatus("mandatory")
_RlBcmACLPortsTable_Object = MibTable
rlBcmACLPortsTable = _RlBcmACLPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 6, 5)
)
if mibBuilder.loadTexts:
    rlBcmACLPortsTable.setStatus("mandatory")
_RlBcmACLPortsEntry_Object = MibTableRow
rlBcmACLPortsEntry = _RlBcmACLPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 6, 5, 1)
)
rlBcmACLPortsEntry.setIndexNames(
    (0, "BROADCOM-MIB", "rlBcmAclPortsIfIndex"),
    (0, "BROADCOM-MIB", "rlBcmAclPortsDirection"),
)
if mibBuilder.loadTexts:
    rlBcmACLPortsEntry.setStatus("mandatory")
_RlBcmAclPortsIfIndex_Type = Integer32
_RlBcmAclPortsIfIndex_Object = MibTableColumn
rlBcmAclPortsIfIndex = _RlBcmAclPortsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 6, 5, 1, 1),
    _RlBcmAclPortsIfIndex_Type()
)
rlBcmAclPortsIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmAclPortsIfIndex.setStatus("mandatory")


class _RlBcmAclPortsDirection_Type(Integer32):
    """Custom type rlBcmAclPortsDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ingress", 1),
          ("egress", 2),
          ("both", 3))
    )


_RlBcmAclPortsDirection_Type.__name__ = "Integer32"
_RlBcmAclPortsDirection_Object = MibTableColumn
rlBcmAclPortsDirection = _RlBcmAclPortsDirection_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 6, 5, 1, 2),
    _RlBcmAclPortsDirection_Type()
)
rlBcmAclPortsDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmAclPortsDirection.setStatus("mandatory")
_RlBcmAclPortsAclID_Type = Integer32
_RlBcmAclPortsAclID_Object = MibTableColumn
rlBcmAclPortsAclID = _RlBcmAclPortsAclID_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 6, 5, 1, 3),
    _RlBcmAclPortsAclID_Type()
)
rlBcmAclPortsAclID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmAclPortsAclID.setStatus("mandatory")
_RlBcmAclPortsStatus_Type = RowStatus
_RlBcmAclPortsStatus_Object = MibTableColumn
rlBcmAclPortsStatus = _RlBcmAclPortsStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 68, 6, 5, 1, 4),
    _RlBcmAclPortsStatus_Type()
)
rlBcmAclPortsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBcmAclPortsStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BROADCOM-MIB",
    **{"RlPolicySimpleBcmMibProfileType": RlPolicySimpleBcmMibProfileType,
       "RlBcmQoSRateLimitType": RlBcmQoSRateLimitType,
       "rlBcmMibVersion": rlBcmMibVersion,
       "rlPolicySimpleBcmMib": rlPolicySimpleBcmMib,
       "rlPolicySimpleBcmMibVersion": rlPolicySimpleBcmMibVersion,
       "rlPolicySimpleBcmMibReservedBW": rlPolicySimpleBcmMibReservedBW,
       "rlPolicySimpleBcmMibPolicyEnable": rlPolicySimpleBcmMibPolicyEnable,
       "rlPolicySimpleBcmMibProfileTable": rlPolicySimpleBcmMibProfileTable,
       "rlPolicySimpleBcmMibProfileEntry": rlPolicySimpleBcmMibProfileEntry,
       "rlPolicySimpleBcmMibIndex": rlPolicySimpleBcmMibIndex,
       "rlPolicySimpleBcmMibDescription": rlPolicySimpleBcmMibDescription,
       "rlPolicySimpleBcmMibProfileType": rlPolicySimpleBcmMibProfileType,
       "rlPolicySimpleBcmMibRate": rlPolicySimpleBcmMibRate,
       "rlPolicySimpleBcmMibBurstSize": rlPolicySimpleBcmMibBurstSize,
       "rlPolicySimpleBcmMibChangeTosOrDscp": rlPolicySimpleBcmMibChangeTosOrDscp,
       "rlPolicySimpleBcmMibNewTosOrDscp": rlPolicySimpleBcmMibNewTosOrDscp,
       "rlPolicySimpleBcmMibStatus": rlPolicySimpleBcmMibStatus,
       "rlPolicySimpleBcmMibRulesTable": rlPolicySimpleBcmMibRulesTable,
       "rlPolicySimpleBcmMibRulesEntry": rlPolicySimpleBcmMibRulesEntry,
       "rlPolicySimpleBcmMibRulesIndex": rlPolicySimpleBcmMibRulesIndex,
       "rlPolicySimpleBcmMibRulesDescription": rlPolicySimpleBcmMibRulesDescription,
       "rlPolicySimpleBcmMibRulesDstMac": rlPolicySimpleBcmMibRulesDstMac,
       "rlPolicySimpleBcmMibRulesSrcMac": rlPolicySimpleBcmMibRulesSrcMac,
       "rlPolicySimpleBcmMibRulesVpt": rlPolicySimpleBcmMibRulesVpt,
       "rlPolicySimpleBcmMibRulesVid": rlPolicySimpleBcmMibRulesVid,
       "rlPolicySimpleBcmMibRulesEthType": rlPolicySimpleBcmMibRulesEthType,
       "rlPolicySimpleBcmMibRulesTosOrDscp": rlPolicySimpleBcmMibRulesTosOrDscp,
       "rlPolicySimpleBcmMibRulesProtocol": rlPolicySimpleBcmMibRulesProtocol,
       "rlPolicySimpleBcmMibRulesSrcIp": rlPolicySimpleBcmMibRulesSrcIp,
       "rlPolicySimpleBcmMibRulesSrcIpMask": rlPolicySimpleBcmMibRulesSrcIpMask,
       "rlPolicySimpleBcmMibRulesDstIp": rlPolicySimpleBcmMibRulesDstIp,
       "rlPolicySimpleBcmMibRulesDstIpMask": rlPolicySimpleBcmMibRulesDstIpMask,
       "rlPolicySimpleBcmMibRulesSrcPort": rlPolicySimpleBcmMibRulesSrcPort,
       "rlPolicySimpleBcmMibRulesDstPort": rlPolicySimpleBcmMibRulesDstPort,
       "rlPolicySimpleBcmMibRulesInIfIndexList": rlPolicySimpleBcmMibRulesInIfIndexList,
       "rlPolicySimpleBcmMibRulesOutIfIndexList": rlPolicySimpleBcmMibRulesOutIfIndexList,
       "rlPolicySimpleBcmMibRulesAction": rlPolicySimpleBcmMibRulesAction,
       "rlPolicySimpleBcmMibRulesProfilePointer": rlPolicySimpleBcmMibRulesProfilePointer,
       "rlPolicySimpleBcmMibRulesBitsUsed": rlPolicySimpleBcmMibRulesBitsUsed,
       "rlPolicySimpleBcmMibRulesStatus": rlPolicySimpleBcmMibRulesStatus,
       "rlBcmRateLimit": rlBcmRateLimit,
       "rlBcmPacketRateLimitBroadcstMulticastUnicastUnknown": rlBcmPacketRateLimitBroadcstMulticastUnicastUnknown,
       "rlBcmPacketRateLimitMulticastEnable": rlBcmPacketRateLimitMulticastEnable,
       "rlBcmPacketRateLimitBroadcstEnable": rlBcmPacketRateLimitBroadcstEnable,
       "rlBcmPacketRateLimitUnicastUnknownEnable": rlBcmPacketRateLimitUnicastUnknownEnable,
       "rlBcmQoSRateLimit": rlBcmQoSRateLimit,
       "rlBcmQoSRateLimitIndexCounter": rlBcmQoSRateLimitIndexCounter,
       "rlBcmQoSRateLimitTable": rlBcmQoSRateLimitTable,
       "rlBcmQoSRateLimitEntry": rlBcmQoSRateLimitEntry,
       "rlBcmQoSRateLimitType": rlBcmQoSRateLimitType,
       "rlBcmQoSRateLimitName": rlBcmQoSRateLimitName,
       "rlBcmQoSRateLimitIndex": rlBcmQoSRateLimitIndex,
       "rlBcmQoSRateLimitAclsNameOrFlow": rlBcmQoSRateLimitAclsNameOrFlow,
       "rlBcmQoSRateLimitPortsOrInterfaces": rlBcmQoSRateLimitPortsOrInterfaces,
       "rlBcmQoSRateLimitRatePriority": rlBcmQoSRateLimitRatePriority,
       "rlBcmQoSRateLimitBurstSizeTosMask": rlBcmQoSRateLimitBurstSizeTosMask,
       "rlBcmQoSRateLimitDropOutProfile": rlBcmQoSRateLimitDropOutProfile,
       "rlBcmQoSRateLimitNewTos": rlBcmQoSRateLimitNewTos,
       "rlBcmQoSRateLimitNewTosPrecedence": rlBcmQoSRateLimitNewTosPrecedence,
       "rlBcmQoSRateLimitStatus": rlBcmQoSRateLimitStatus,
       "rlBcmQoSRateLimitAclApplliedTable": rlBcmQoSRateLimitAclApplliedTable,
       "rlBcmQoSRateLimitAclApplliedEntry": rlBcmQoSRateLimitAclApplliedEntry,
       "rlBcmQoSRateLimitAclName": rlBcmQoSRateLimitAclName,
       "rlBcmQoSRateLimitAclApplliedIfIndex": rlBcmQoSRateLimitAclApplliedIfIndex,
       "rlBcmQoSRateLimitAclApplliedType": rlBcmQoSRateLimitAclApplliedType,
       "rlBcmQoSRateLimitAclApplliedStatus": rlBcmQoSRateLimitAclApplliedStatus,
       "rlBcmQoSRateLimitIPflowTable": rlBcmQoSRateLimitIPflowTable,
       "rlBcmQoSRateLimitIPflowEntry": rlBcmQoSRateLimitIPflowEntry,
       "rlBcmQoSRateLimitIPflowTos": rlBcmQoSRateLimitIPflowTos,
       "rlBcmQoSRateLimitIPflowTosMask": rlBcmQoSRateLimitIPflowTosMask,
       "rlBcmQoSRateLimitIPflowProtocol": rlBcmQoSRateLimitIPflowProtocol,
       "rlBcmQoSRateLimitIPflowSrcIp": rlBcmQoSRateLimitIPflowSrcIp,
       "rlBcmQoSRateLimitIPflowSrcIpMask": rlBcmQoSRateLimitIPflowSrcIpMask,
       "rlBcmQoSRateLimitIPflowDstIp": rlBcmQoSRateLimitIPflowDstIp,
       "rlBcmQoSRateLimitIPflowDstIpMask": rlBcmQoSRateLimitIPflowDstIpMask,
       "rlBcmQoSRateLimitIPflowSrcPort": rlBcmQoSRateLimitIPflowSrcPort,
       "rlBcmQoSRateLimitIPflowDstPort": rlBcmQoSRateLimitIPflowDstPort,
       "rlBcmQoSRateLimitInIfindex": rlBcmQoSRateLimitInIfindex,
       "rlBcmQoSRateLimitOutIfindex": rlBcmQoSRateLimitOutIfindex,
       "rlBcmQoSRateLimitIPFlowType": rlBcmQoSRateLimitIPFlowType,
       "rlBcmQoSRateLimitIPFlowRule": rlBcmQoSRateLimitIPFlowRule,
       "rlBcmQoSRateLimitIPflowStatus": rlBcmQoSRateLimitIPflowStatus,
       "rlBcmQoSRateLimitQoSprecedenceMap": rlBcmQoSRateLimitQoSprecedenceMap,
       "rlTosOverwriteMapMib": rlTosOverwriteMapMib,
       "rlTosOverwriteMapTable": rlTosOverwriteMapTable,
       "rlTosOverwriteMapEntry": rlTosOverwriteMapEntry,
       "rlTosOverwriteMapName": rlTosOverwriteMapName,
       "rlTosOverwriteMapRange": rlTosOverwriteMapRange,
       "rlTosOverwriteMapMapping": rlTosOverwriteMapMapping,
       "rlTosOverwriteMapPortList": rlTosOverwriteMapPortList,
       "rlTosOverwriteMapStatus": rlTosOverwriteMapStatus,
       "rlBcmACLMib": rlBcmACLMib,
       "rlBcmACLMibVersion": rlBcmACLMibVersion,
       "rlBcmACLMaxNumberOfEntries": rlBcmACLMaxNumberOfEntries,
       "rlBcmACLNamesTable": rlBcmACLNamesTable,
       "rlBcmACLNamesEntry": rlBcmACLNamesEntry,
       "rlBcmACLNamesName": rlBcmACLNamesName,
       "rlBcmACLNamesID": rlBcmACLNamesID,
       "rlBcmACLNamesStatus": rlBcmACLNamesStatus,
       "rlBcmACLTable": rlBcmACLTable,
       "rlBcmACLEntry": rlBcmACLEntry,
       "rlBcmAclID": rlBcmAclID,
       "rlBcmAclRowIndex": rlBcmAclRowIndex,
       "rlBcmAclAction": rlBcmAclAction,
       "rlBcmAclIPflags": rlBcmAclIPflags,
       "rlBcmAclIPflagsMask": rlBcmAclIPflagsMask,
       "rlBcmAclIPfragOffset": rlBcmAclIPfragOffset,
       "rlBcmAclIPfragOffsetMask": rlBcmAclIPfragOffsetMask,
       "rlBcmAclIPprotocol": rlBcmAclIPprotocol,
       "rlBcmAclSrcIp": rlBcmAclSrcIp,
       "rlBcmAclSrcIpMask": rlBcmAclSrcIpMask,
       "rlBcmAclDstIp": rlBcmAclDstIp,
       "rlBcmAclDstIpMask": rlBcmAclDstIpMask,
       "rlBcmAclSrcL4Port": rlBcmAclSrcL4Port,
       "rlBcmAclDstL4Port": rlBcmAclDstL4Port,
       "rlBcmAclTCPbits": rlBcmAclTCPbits,
       "rlBcmAclTCPbitsMask": rlBcmAclTCPbitsMask,
       "rlBcmAclStatus": rlBcmAclStatus,
       "rlBcmACLPortsTable": rlBcmACLPortsTable,
       "rlBcmACLPortsEntry": rlBcmACLPortsEntry,
       "rlBcmAclPortsIfIndex": rlBcmAclPortsIfIndex,
       "rlBcmAclPortsDirection": rlBcmAclPortsDirection,
       "rlBcmAclPortsAclID": rlBcmAclPortsAclID,
       "rlBcmAclPortsStatus": rlBcmAclPortsStatus}
)
