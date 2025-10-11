# SNMP MIB module (Q-IN-Q-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/Q-IN-Q-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:45:56 2025
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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

swQinQMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 57)
)


# Types definitions



class VlanId(Integer32):
    """Custom type VlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwQinQCtrl_ObjectIdentity = ObjectIdentity
swQinQCtrl = _SwQinQCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 1)
)


class _SwQinQState_Type(Integer32):
    """Custom type swQinQState based on Integer32"""
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


_SwQinQState_Type.__name__ = "Integer32"
_SwQinQState_Object = MibScalar
swQinQState = _SwQinQState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 1, 1),
    _SwQinQState_Type()
)
swQinQState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swQinQState.setStatus("current")


class _SwQinQInnerTpid_Type(OctetString):
    """Custom type swQinQInnerTpid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_SwQinQInnerTpid_Type.__name__ = "OctetString"
_SwQinQInnerTpid_Object = MibScalar
swQinQInnerTpid = _SwQinQInnerTpid_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 1, 2),
    _SwQinQInnerTpid_Type()
)
swQinQInnerTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swQinQInnerTpid.setStatus("current")
_SwQinQInfo_ObjectIdentity = ObjectIdentity
swQinQInfo = _SwQinQInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 2)
)
_SwQinQPortMgmt_ObjectIdentity = ObjectIdentity
swQinQPortMgmt = _SwQinQPortMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 3)
)
_SwQinQPortTable_Object = MibTable
swQinQPortTable = _SwQinQPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 3, 1)
)
if mibBuilder.loadTexts:
    swQinQPortTable.setStatus("current")
_SwQinQPortEntry_Object = MibTableRow
swQinQPortEntry = _SwQinQPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 3, 1, 1)
)
swQinQPortEntry.setIndexNames(
    (0, "Q-IN-Q-MIB", "swQinQPortIndex"),
)
if mibBuilder.loadTexts:
    swQinQPortEntry.setStatus("current")


class _SwQinQPortIndex_Type(Integer32):
    """Custom type swQinQPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwQinQPortIndex_Type.__name__ = "Integer32"
_SwQinQPortIndex_Object = MibTableColumn
swQinQPortIndex = _SwQinQPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 3, 1, 1, 1),
    _SwQinQPortIndex_Type()
)
swQinQPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swQinQPortIndex.setStatus("current")


class _SwQinQPortRole_Type(Integer32):
    """Custom type swQinQPortRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nni", 1),
          ("uni", 2))
    )


_SwQinQPortRole_Type.__name__ = "Integer32"
_SwQinQPortRole_Object = MibTableColumn
swQinQPortRole = _SwQinQPortRole_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 3, 1, 1, 2),
    _SwQinQPortRole_Type()
)
swQinQPortRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swQinQPortRole.setStatus("current")


class _SwQinQPortMissDrop_Type(Integer32):
    """Custom type swQinQPortMissDrop based on Integer32"""
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


_SwQinQPortMissDrop_Type.__name__ = "Integer32"
_SwQinQPortMissDrop_Object = MibTableColumn
swQinQPortMissDrop = _SwQinQPortMissDrop_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 3, 1, 1, 3),
    _SwQinQPortMissDrop_Type()
)
swQinQPortMissDrop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swQinQPortMissDrop.setStatus("current")


class _SwQinQPortTpid_Type(OctetString):
    """Custom type swQinQPortTpid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_SwQinQPortTpid_Type.__name__ = "OctetString"
_SwQinQPortTpid_Object = MibTableColumn
swQinQPortTpid = _SwQinQPortTpid_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 3, 1, 1, 4),
    _SwQinQPortTpid_Type()
)
swQinQPortTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swQinQPortTpid.setStatus("current")


class _SwQinQPortUseInnerPriority_Type(Integer32):
    """Custom type swQinQPortUseInnerPriority based on Integer32"""
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


_SwQinQPortUseInnerPriority_Type.__name__ = "Integer32"
_SwQinQPortUseInnerPriority_Object = MibTableColumn
swQinQPortUseInnerPriority = _SwQinQPortUseInnerPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 3, 1, 1, 5),
    _SwQinQPortUseInnerPriority_Type()
)
swQinQPortUseInnerPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swQinQPortUseInnerPriority.setStatus("current")


class _SwQinQPortInnerTagState_Type(Integer32):
    """Custom type swQinQPortInnerTagState based on Integer32"""
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


_SwQinQPortInnerTagState_Type.__name__ = "Integer32"
_SwQinQPortInnerTagState_Object = MibTableColumn
swQinQPortInnerTagState = _SwQinQPortInnerTagState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 3, 1, 1, 6),
    _SwQinQPortInnerTagState_Type()
)
swQinQPortInnerTagState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swQinQPortInnerTagState.setStatus("current")


class _SwQinQPortInnerTag_Type(OctetString):
    """Custom type swQinQPortInnerTag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_SwQinQPortInnerTag_Type.__name__ = "OctetString"
_SwQinQPortInnerTag_Object = MibTableColumn
swQinQPortInnerTag = _SwQinQPortInnerTag_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 3, 1, 1, 7),
    _SwQinQPortInnerTag_Type()
)
swQinQPortInnerTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swQinQPortInnerTag.setStatus("current")


class _SwQinQPortTrustCVID_Type(Integer32):
    """Custom type swQinQPortTrustCVID based on Integer32"""
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


_SwQinQPortTrustCVID_Type.__name__ = "Integer32"
_SwQinQPortTrustCVID_Object = MibTableColumn
swQinQPortTrustCVID = _SwQinQPortTrustCVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 3, 1, 1, 8),
    _SwQinQPortTrustCVID_Type()
)
swQinQPortTrustCVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swQinQPortTrustCVID.setStatus("current")


class _SwQinQPortVlanTranslation_Type(Integer32):
    """Custom type swQinQPortVlanTranslation based on Integer32"""
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


_SwQinQPortVlanTranslation_Type.__name__ = "Integer32"
_SwQinQPortVlanTranslation_Object = MibTableColumn
swQinQPortVlanTranslation = _SwQinQPortVlanTranslation_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 3, 1, 1, 9),
    _SwQinQPortVlanTranslation_Type()
)
swQinQPortVlanTranslation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swQinQPortVlanTranslation.setStatus("current")


class _SwQinQPortInnerTpid_Type(OctetString):
    """Custom type swQinQPortInnerTpid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_SwQinQPortInnerTpid_Type.__name__ = "OctetString"
_SwQinQPortInnerTpid_Object = MibTableColumn
swQinQPortInnerTpid = _SwQinQPortInnerTpid_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 3, 1, 1, 10),
    _SwQinQPortInnerTpid_Type()
)
swQinQPortInnerTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swQinQPortInnerTpid.setStatus("current")
_SwQinQPortRuleTable_Object = MibTable
swQinQPortRuleTable = _SwQinQPortRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 3, 2)
)
if mibBuilder.loadTexts:
    swQinQPortRuleTable.setStatus("current")
_SwQinQPortRuleEntry_Object = MibTableRow
swQinQPortRuleEntry = _SwQinQPortRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 3, 2, 1)
)
swQinQPortRuleEntry.setIndexNames(
    (0, "Q-IN-Q-MIB", "swQinQPortRuleIndex"),
    (0, "Q-IN-Q-MIB", "swQinQProfileId"),
)
if mibBuilder.loadTexts:
    swQinQPortRuleEntry.setStatus("current")


class _SwQinQPortRuleIndex_Type(Integer32):
    """Custom type swQinQPortRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwQinQPortRuleIndex_Type.__name__ = "Integer32"
_SwQinQPortRuleIndex_Object = MibTableColumn
swQinQPortRuleIndex = _SwQinQPortRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 3, 2, 1, 1),
    _SwQinQPortRuleIndex_Type()
)
swQinQPortRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swQinQPortRuleIndex.setStatus("current")


class _SwQinQProfileId_Type(Integer32):
    """Custom type swQinQProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwQinQProfileId_Type.__name__ = "Integer32"
_SwQinQProfileId_Object = MibTableColumn
swQinQProfileId = _SwQinQProfileId_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 3, 2, 1, 2),
    _SwQinQProfileId_Type()
)
swQinQProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swQinQProfileId.setStatus("current")
_SwQinQPortRuleRowStatus_Type = RowStatus
_SwQinQPortRuleRowStatus_Object = MibTableColumn
swQinQPortRuleRowStatus = _SwQinQPortRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 3, 2, 1, 3),
    _SwQinQPortRuleRowStatus_Type()
)
swQinQPortRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swQinQPortRuleRowStatus.setStatus("current")
_SwVlanTranslateTable_Object = MibTable
swVlanTranslateTable = _SwVlanTranslateTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 3, 3)
)
if mibBuilder.loadTexts:
    swVlanTranslateTable.setStatus("current")
_SwVlanTranslateEntry_Object = MibTableRow
swVlanTranslateEntry = _SwVlanTranslateEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 3, 3, 1)
)
swVlanTranslateEntry.setIndexNames(
    (0, "Q-IN-Q-MIB", "swVlanTranslatePortIndex"),
    (0, "Q-IN-Q-MIB", "swVlanTranslateCVID"),
)
if mibBuilder.loadTexts:
    swVlanTranslateEntry.setStatus("current")
_SwVlanTranslatePortIndex_Type = Integer32
_SwVlanTranslatePortIndex_Object = MibTableColumn
swVlanTranslatePortIndex = _SwVlanTranslatePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 3, 3, 1, 1),
    _SwVlanTranslatePortIndex_Type()
)
swVlanTranslatePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVlanTranslatePortIndex.setStatus("current")
_SwVlanTranslateCVID_Type = VlanId
_SwVlanTranslateCVID_Object = MibTableColumn
swVlanTranslateCVID = _SwVlanTranslateCVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 3, 3, 1, 2),
    _SwVlanTranslateCVID_Type()
)
swVlanTranslateCVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVlanTranslateCVID.setStatus("current")
_SwVlanTranslateSVID_Type = VlanId
_SwVlanTranslateSVID_Object = MibTableColumn
swVlanTranslateSVID = _SwVlanTranslateSVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 3, 3, 1, 3),
    _SwVlanTranslateSVID_Type()
)
swVlanTranslateSVID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swVlanTranslateSVID.setStatus("current")


class _SwVlanTranslateSVIDOperation_Type(Integer32):
    """Custom type swVlanTranslateSVIDOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("replace", 2))
    )


_SwVlanTranslateSVIDOperation_Type.__name__ = "Integer32"
_SwVlanTranslateSVIDOperation_Object = MibTableColumn
swVlanTranslateSVIDOperation = _SwVlanTranslateSVIDOperation_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 3, 3, 1, 4),
    _SwVlanTranslateSVIDOperation_Type()
)
swVlanTranslateSVIDOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swVlanTranslateSVIDOperation.setStatus("current")


class _SwVlanTranslatePriority_Type(Integer32):
    """Custom type swVlanTranslatePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )


_SwVlanTranslatePriority_Type.__name__ = "Integer32"
_SwVlanTranslatePriority_Object = MibTableColumn
swVlanTranslatePriority = _SwVlanTranslatePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 3, 3, 1, 5),
    _SwVlanTranslatePriority_Type()
)
swVlanTranslatePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swVlanTranslatePriority.setStatus("current")
_SwVlanTranslateRowStatus_Type = RowStatus
_SwVlanTranslateRowStatus_Object = MibTableColumn
swVlanTranslateRowStatus = _SwVlanTranslateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 3, 3, 1, 6),
    _SwVlanTranslateRowStatus_Type()
)
swVlanTranslateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swVlanTranslateRowStatus.setStatus("current")
_SwDoubleVlanTranslateTable_Object = MibTable
swDoubleVlanTranslateTable = _SwDoubleVlanTranslateTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 3, 4)
)
if mibBuilder.loadTexts:
    swDoubleVlanTranslateTable.setStatus("current")
_SwDoubleVlanTranslateEntry_Object = MibTableRow
swDoubleVlanTranslateEntry = _SwDoubleVlanTranslateEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 3, 4, 1)
)
swDoubleVlanTranslateEntry.setIndexNames(
    (0, "Q-IN-Q-MIB", "swDoubleVlanTranslatePortIndex"),
    (0, "Q-IN-Q-MIB", "swDoubleVlanTranslateSVID"),
    (0, "Q-IN-Q-MIB", "swDoubleVlanTranslateCVID"),
)
if mibBuilder.loadTexts:
    swDoubleVlanTranslateEntry.setStatus("current")
_SwDoubleVlanTranslatePortIndex_Type = Integer32
_SwDoubleVlanTranslatePortIndex_Object = MibTableColumn
swDoubleVlanTranslatePortIndex = _SwDoubleVlanTranslatePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 3, 4, 1, 1),
    _SwDoubleVlanTranslatePortIndex_Type()
)
swDoubleVlanTranslatePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swDoubleVlanTranslatePortIndex.setStatus("current")
_SwDoubleVlanTranslateSVID_Type = VlanId
_SwDoubleVlanTranslateSVID_Object = MibTableColumn
swDoubleVlanTranslateSVID = _SwDoubleVlanTranslateSVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 3, 4, 1, 2),
    _SwDoubleVlanTranslateSVID_Type()
)
swDoubleVlanTranslateSVID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swDoubleVlanTranslateSVID.setStatus("current")
_SwDoubleVlanTranslateCVID_Type = VlanId
_SwDoubleVlanTranslateCVID_Object = MibTableColumn
swDoubleVlanTranslateCVID = _SwDoubleVlanTranslateCVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 3, 4, 1, 3),
    _SwDoubleVlanTranslateCVID_Type()
)
swDoubleVlanTranslateCVID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swDoubleVlanTranslateCVID.setStatus("current")


class _SwDoubleVlanTranslateOperation_Type(Integer32):
    """Custom type swDoubleVlanTranslateOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("replace", 2)
    )


_SwDoubleVlanTranslateOperation_Type.__name__ = "Integer32"
_SwDoubleVlanTranslateOperation_Object = MibTableColumn
swDoubleVlanTranslateOperation = _SwDoubleVlanTranslateOperation_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 3, 4, 1, 4),
    _SwDoubleVlanTranslateOperation_Type()
)
swDoubleVlanTranslateOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swDoubleVlanTranslateOperation.setStatus("current")
_SwDoubleVlanTranslateNewSVID_Type = VlanId
_SwDoubleVlanTranslateNewSVID_Object = MibTableColumn
swDoubleVlanTranslateNewSVID = _SwDoubleVlanTranslateNewSVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 3, 4, 1, 5),
    _SwDoubleVlanTranslateNewSVID_Type()
)
swDoubleVlanTranslateNewSVID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swDoubleVlanTranslateNewSVID.setStatus("current")


class _SwDoubleVlanTranslatePriority_Type(Integer32):
    """Custom type swDoubleVlanTranslatePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )


_SwDoubleVlanTranslatePriority_Type.__name__ = "Integer32"
_SwDoubleVlanTranslatePriority_Object = MibTableColumn
swDoubleVlanTranslatePriority = _SwDoubleVlanTranslatePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 3, 4, 1, 6),
    _SwDoubleVlanTranslatePriority_Type()
)
swDoubleVlanTranslatePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swDoubleVlanTranslatePriority.setStatus("current")
_SwDoubleVlanTranslateRowStatus_Type = RowStatus
_SwDoubleVlanTranslateRowStatus_Object = MibTableColumn
swDoubleVlanTranslateRowStatus = _SwDoubleVlanTranslateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 3, 4, 1, 7),
    _SwDoubleVlanTranslateRowStatus_Type()
)
swDoubleVlanTranslateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swDoubleVlanTranslateRowStatus.setStatus("current")
_SwQinQMgmt_ObjectIdentity = ObjectIdentity
swQinQMgmt = _SwQinQMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 4)
)
_SwQinQProfileTable_Object = MibTable
swQinQProfileTable = _SwQinQProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 4, 1)
)
if mibBuilder.loadTexts:
    swQinQProfileTable.setStatus("current")
_SwQinQProfileEntry_Object = MibTableRow
swQinQProfileEntry = _SwQinQProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 4, 1, 1)
)
swQinQProfileEntry.setIndexNames(
    (0, "Q-IN-Q-MIB", "swQinQProfileID"),
)
if mibBuilder.loadTexts:
    swQinQProfileEntry.setStatus("current")


class _SwQinQProfileID_Type(Integer32):
    """Custom type swQinQProfileID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwQinQProfileID_Type.__name__ = "Integer32"
_SwQinQProfileID_Object = MibTableColumn
swQinQProfileID = _SwQinQProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 4, 1, 1, 1),
    _SwQinQProfileID_Type()
)
swQinQProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swQinQProfileID.setStatus("current")
_SwQinQProfileRowStatus_Type = RowStatus
_SwQinQProfileRowStatus_Object = MibTableColumn
swQinQProfileRowStatus = _SwQinQProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 4, 1, 1, 2),
    _SwQinQProfileRowStatus_Type()
)
swQinQProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swQinQProfileRowStatus.setStatus("current")
_SwQinQRuleTable_Object = MibTable
swQinQRuleTable = _SwQinQRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 4, 2)
)
if mibBuilder.loadTexts:
    swQinQRuleTable.setStatus("current")
_SwQinQRuleEntry_Object = MibTableRow
swQinQRuleEntry = _SwQinQRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 4, 2, 1)
)
swQinQRuleEntry.setIndexNames(
    (0, "Q-IN-Q-MIB", "swQinQRuleProfileID"),
    (0, "Q-IN-Q-MIB", "swQinQRuleAccessID"),
)
if mibBuilder.loadTexts:
    swQinQRuleEntry.setStatus("current")


class _SwQinQRuleProfileID_Type(Integer32):
    """Custom type swQinQRuleProfileID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwQinQRuleProfileID_Type.__name__ = "Integer32"
_SwQinQRuleProfileID_Object = MibTableColumn
swQinQRuleProfileID = _SwQinQRuleProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 4, 2, 1, 1),
    _SwQinQRuleProfileID_Type()
)
swQinQRuleProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swQinQRuleProfileID.setStatus("current")


class _SwQinQRuleAccessID_Type(Integer32):
    """Custom type swQinQRuleAccessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwQinQRuleAccessID_Type.__name__ = "Integer32"
_SwQinQRuleAccessID_Object = MibTableColumn
swQinQRuleAccessID = _SwQinQRuleAccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 4, 2, 1, 2),
    _SwQinQRuleAccessID_Type()
)
swQinQRuleAccessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swQinQRuleAccessID.setStatus("current")
_SwQinQRuleClassifySrcMacAddr_Type = MacAddress
_SwQinQRuleClassifySrcMacAddr_Object = MibTableColumn
swQinQRuleClassifySrcMacAddr = _SwQinQRuleClassifySrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 4, 2, 1, 3),
    _SwQinQRuleClassifySrcMacAddr_Type()
)
swQinQRuleClassifySrcMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swQinQRuleClassifySrcMacAddr.setStatus("current")
_SwQinQRuleClassifySrcMacAddrMask_Type = MacAddress
_SwQinQRuleClassifySrcMacAddrMask_Object = MibTableColumn
swQinQRuleClassifySrcMacAddrMask = _SwQinQRuleClassifySrcMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 4, 2, 1, 4),
    _SwQinQRuleClassifySrcMacAddrMask_Type()
)
swQinQRuleClassifySrcMacAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swQinQRuleClassifySrcMacAddrMask.setStatus("current")
_SwQinQRuleClassifyDstMacAddr_Type = MacAddress
_SwQinQRuleClassifyDstMacAddr_Object = MibTableColumn
swQinQRuleClassifyDstMacAddr = _SwQinQRuleClassifyDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 4, 2, 1, 5),
    _SwQinQRuleClassifyDstMacAddr_Type()
)
swQinQRuleClassifyDstMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swQinQRuleClassifyDstMacAddr.setStatus("current")
_SwQinQRuleClassifyDstMacAddrMask_Type = MacAddress
_SwQinQRuleClassifyDstMacAddrMask_Object = MibTableColumn
swQinQRuleClassifyDstMacAddrMask = _SwQinQRuleClassifyDstMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 4, 2, 1, 6),
    _SwQinQRuleClassifyDstMacAddrMask_Type()
)
swQinQRuleClassifyDstMacAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swQinQRuleClassifyDstMacAddrMask.setStatus("current")
_SwQinQRuleSrcIPv4Address_Type = IpAddress
_SwQinQRuleSrcIPv4Address_Object = MibTableColumn
swQinQRuleSrcIPv4Address = _SwQinQRuleSrcIPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 4, 2, 1, 7),
    _SwQinQRuleSrcIPv4Address_Type()
)
swQinQRuleSrcIPv4Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swQinQRuleSrcIPv4Address.setStatus("current")
_SwQinQRuleSrcIPv4AddrMask_Type = IpAddress
_SwQinQRuleSrcIPv4AddrMask_Object = MibTableColumn
swQinQRuleSrcIPv4AddrMask = _SwQinQRuleSrcIPv4AddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 4, 2, 1, 8),
    _SwQinQRuleSrcIPv4AddrMask_Type()
)
swQinQRuleSrcIPv4AddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swQinQRuleSrcIPv4AddrMask.setStatus("current")
_SwQinQRuleDstIPv4Address_Type = IpAddress
_SwQinQRuleDstIPv4Address_Object = MibTableColumn
swQinQRuleDstIPv4Address = _SwQinQRuleDstIPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 4, 2, 1, 9),
    _SwQinQRuleDstIPv4Address_Type()
)
swQinQRuleDstIPv4Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swQinQRuleDstIPv4Address.setStatus("current")
_SwQinQRuleDstIPv4AddrMask_Type = IpAddress
_SwQinQRuleDstIPv4AddrMask_Object = MibTableColumn
swQinQRuleDstIPv4AddrMask = _SwQinQRuleDstIPv4AddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 4, 2, 1, 10),
    _SwQinQRuleDstIPv4AddrMask_Type()
)
swQinQRuleDstIPv4AddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swQinQRuleDstIPv4AddrMask.setStatus("current")
_SwQinQRuleInnerVid_Type = DisplayString
_SwQinQRuleInnerVid_Object = MibTableColumn
swQinQRuleInnerVid = _SwQinQRuleInnerVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 4, 2, 1, 11),
    _SwQinQRuleInnerVid_Type()
)
swQinQRuleInnerVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swQinQRuleInnerVid.setStatus("current")
_SwQinQRuleOuterVid_Type = DisplayString
_SwQinQRuleOuterVid_Object = MibTableColumn
swQinQRuleOuterVid = _SwQinQRuleOuterVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 4, 2, 1, 12),
    _SwQinQRuleOuterVid_Type()
)
swQinQRuleOuterVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swQinQRuleOuterVid.setStatus("current")


class _SwQinQRule8021p_Type(Integer32):
    """Custom type swQinQRule8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )


_SwQinQRule8021p_Type.__name__ = "Integer32"
_SwQinQRule8021p_Object = MibTableColumn
swQinQRule8021p = _SwQinQRule8021p_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 4, 2, 1, 13),
    _SwQinQRule8021p_Type()
)
swQinQRule8021p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swQinQRule8021p.setStatus("current")
_SwQinQRuleIpProtocol_Type = Integer32
_SwQinQRuleIpProtocol_Object = MibTableColumn
swQinQRuleIpProtocol = _SwQinQRuleIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 4, 2, 1, 14),
    _SwQinQRuleIpProtocol_Type()
)
swQinQRuleIpProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swQinQRuleIpProtocol.setStatus("current")
_SwQinQRuleSourcePort_Type = Integer32
_SwQinQRuleSourcePort_Object = MibTableColumn
swQinQRuleSourcePort = _SwQinQRuleSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 4, 2, 1, 15),
    _SwQinQRuleSourcePort_Type()
)
swQinQRuleSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swQinQRuleSourcePort.setStatus("current")
_SwQinQRuleDestinationPort_Type = Integer32
_SwQinQRuleDestinationPort_Object = MibTableColumn
swQinQRuleDestinationPort = _SwQinQRuleDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 4, 2, 1, 16),
    _SwQinQRuleDestinationPort_Type()
)
swQinQRuleDestinationPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swQinQRuleDestinationPort.setStatus("current")


class _SwQinQRuleSpvidOperation_Type(Integer32):
    """Custom type swQinQRuleSpvidOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("replace", 2))
    )


_SwQinQRuleSpvidOperation_Type.__name__ = "Integer32"
_SwQinQRuleSpvidOperation_Object = MibTableColumn
swQinQRuleSpvidOperation = _SwQinQRuleSpvidOperation_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 4, 2, 1, 17),
    _SwQinQRuleSpvidOperation_Type()
)
swQinQRuleSpvidOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swQinQRuleSpvidOperation.setStatus("current")


class _SwQinQRuleSpvid_Type(Integer32):
    """Custom type swQinQRuleSpvid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SwQinQRuleSpvid_Type.__name__ = "Integer32"
_SwQinQRuleSpvid_Object = MibTableColumn
swQinQRuleSpvid = _SwQinQRuleSpvid_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 4, 2, 1, 18),
    _SwQinQRuleSpvid_Type()
)
swQinQRuleSpvid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swQinQRuleSpvid.setStatus("current")


class _SwQinQPriority_Type(Integer32):
    """Custom type swQinQPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )


_SwQinQPriority_Type.__name__ = "Integer32"
_SwQinQPriority_Object = MibTableColumn
swQinQPriority = _SwQinQPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 4, 2, 1, 19),
    _SwQinQPriority_Type()
)
swQinQPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swQinQPriority.setStatus("current")
_SwQinQRuleRowStatus_Type = RowStatus
_SwQinQRuleRowStatus_Object = MibTableColumn
swQinQRuleRowStatus = _SwQinQRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 4, 2, 1, 20),
    _SwQinQRuleRowStatus_Type()
)
swQinQRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swQinQRuleRowStatus.setStatus("current")
_SwQinQRuleActivePort_Type = PortList
_SwQinQRuleActivePort_Object = MibTableColumn
swQinQRuleActivePort = _SwQinQRuleActivePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 4, 2, 1, 21),
    _SwQinQRuleActivePort_Type()
)
swQinQRuleActivePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swQinQRuleActivePort.setStatus("current")
_SwVlanTranslationCVIDTable_Object = MibTable
swVlanTranslationCVIDTable = _SwVlanTranslationCVIDTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 4, 3)
)
if mibBuilder.loadTexts:
    swVlanTranslationCVIDTable.setStatus("current")
_SwVlanTranslationCVIDEntry_Object = MibTableRow
swVlanTranslationCVIDEntry = _SwVlanTranslationCVIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 4, 3, 1)
)
swVlanTranslationCVIDEntry.setIndexNames(
    (0, "Q-IN-Q-MIB", "swVlanTranslationCVID"),
)
if mibBuilder.loadTexts:
    swVlanTranslationCVIDEntry.setStatus("current")
_SwVlanTranslationCVID_Type = VlanId
_SwVlanTranslationCVID_Object = MibTableColumn
swVlanTranslationCVID = _SwVlanTranslationCVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 4, 3, 1, 1),
    _SwVlanTranslationCVID_Type()
)
swVlanTranslationCVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVlanTranslationCVID.setStatus("current")
_SwVlanTranslationSVID_Type = VlanId
_SwVlanTranslationSVID_Object = MibTableColumn
swVlanTranslationSVID = _SwVlanTranslationSVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 4, 3, 1, 2),
    _SwVlanTranslationSVID_Type()
)
swVlanTranslationSVID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swVlanTranslationSVID.setStatus("current")


class _SwVlanTranslationSVIDOperation_Type(Integer32):
    """Custom type swVlanTranslationSVIDOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("replace", 2))
    )


_SwVlanTranslationSVIDOperation_Type.__name__ = "Integer32"
_SwVlanTranslationSVIDOperation_Object = MibTableColumn
swVlanTranslationSVIDOperation = _SwVlanTranslationSVIDOperation_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 4, 3, 1, 3),
    _SwVlanTranslationSVIDOperation_Type()
)
swVlanTranslationSVIDOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swVlanTranslationSVIDOperation.setStatus("current")
_SwVlanTranslationCVIDRowStatus_Type = RowStatus
_SwVlanTranslationCVIDRowStatus_Object = MibTableColumn
swVlanTranslationCVIDRowStatus = _SwVlanTranslationCVIDRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 4, 3, 1, 4),
    _SwVlanTranslationCVIDRowStatus_Type()
)
swVlanTranslationCVIDRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swVlanTranslationCVIDRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Q-IN-Q-MIB",
    **{"VlanId": VlanId,
       "swQinQMIB": swQinQMIB,
       "swQinQCtrl": swQinQCtrl,
       "swQinQState": swQinQState,
       "swQinQInnerTpid": swQinQInnerTpid,
       "swQinQInfo": swQinQInfo,
       "swQinQPortMgmt": swQinQPortMgmt,
       "swQinQPortTable": swQinQPortTable,
       "swQinQPortEntry": swQinQPortEntry,
       "swQinQPortIndex": swQinQPortIndex,
       "swQinQPortRole": swQinQPortRole,
       "swQinQPortMissDrop": swQinQPortMissDrop,
       "swQinQPortTpid": swQinQPortTpid,
       "swQinQPortUseInnerPriority": swQinQPortUseInnerPriority,
       "swQinQPortInnerTagState": swQinQPortInnerTagState,
       "swQinQPortInnerTag": swQinQPortInnerTag,
       "swQinQPortTrustCVID": swQinQPortTrustCVID,
       "swQinQPortVlanTranslation": swQinQPortVlanTranslation,
       "swQinQPortInnerTpid": swQinQPortInnerTpid,
       "swQinQPortRuleTable": swQinQPortRuleTable,
       "swQinQPortRuleEntry": swQinQPortRuleEntry,
       "swQinQPortRuleIndex": swQinQPortRuleIndex,
       "swQinQProfileId": swQinQProfileId,
       "swQinQPortRuleRowStatus": swQinQPortRuleRowStatus,
       "swVlanTranslateTable": swVlanTranslateTable,
       "swVlanTranslateEntry": swVlanTranslateEntry,
       "swVlanTranslatePortIndex": swVlanTranslatePortIndex,
       "swVlanTranslateCVID": swVlanTranslateCVID,
       "swVlanTranslateSVID": swVlanTranslateSVID,
       "swVlanTranslateSVIDOperation": swVlanTranslateSVIDOperation,
       "swVlanTranslatePriority": swVlanTranslatePriority,
       "swVlanTranslateRowStatus": swVlanTranslateRowStatus,
       "swDoubleVlanTranslateTable": swDoubleVlanTranslateTable,
       "swDoubleVlanTranslateEntry": swDoubleVlanTranslateEntry,
       "swDoubleVlanTranslatePortIndex": swDoubleVlanTranslatePortIndex,
       "swDoubleVlanTranslateSVID": swDoubleVlanTranslateSVID,
       "swDoubleVlanTranslateCVID": swDoubleVlanTranslateCVID,
       "swDoubleVlanTranslateOperation": swDoubleVlanTranslateOperation,
       "swDoubleVlanTranslateNewSVID": swDoubleVlanTranslateNewSVID,
       "swDoubleVlanTranslatePriority": swDoubleVlanTranslatePriority,
       "swDoubleVlanTranslateRowStatus": swDoubleVlanTranslateRowStatus,
       "swQinQMgmt": swQinQMgmt,
       "swQinQProfileTable": swQinQProfileTable,
       "swQinQProfileEntry": swQinQProfileEntry,
       "swQinQProfileID": swQinQProfileID,
       "swQinQProfileRowStatus": swQinQProfileRowStatus,
       "swQinQRuleTable": swQinQRuleTable,
       "swQinQRuleEntry": swQinQRuleEntry,
       "swQinQRuleProfileID": swQinQRuleProfileID,
       "swQinQRuleAccessID": swQinQRuleAccessID,
       "swQinQRuleClassifySrcMacAddr": swQinQRuleClassifySrcMacAddr,
       "swQinQRuleClassifySrcMacAddrMask": swQinQRuleClassifySrcMacAddrMask,
       "swQinQRuleClassifyDstMacAddr": swQinQRuleClassifyDstMacAddr,
       "swQinQRuleClassifyDstMacAddrMask": swQinQRuleClassifyDstMacAddrMask,
       "swQinQRuleSrcIPv4Address": swQinQRuleSrcIPv4Address,
       "swQinQRuleSrcIPv4AddrMask": swQinQRuleSrcIPv4AddrMask,
       "swQinQRuleDstIPv4Address": swQinQRuleDstIPv4Address,
       "swQinQRuleDstIPv4AddrMask": swQinQRuleDstIPv4AddrMask,
       "swQinQRuleInnerVid": swQinQRuleInnerVid,
       "swQinQRuleOuterVid": swQinQRuleOuterVid,
       "swQinQRule8021p": swQinQRule8021p,
       "swQinQRuleIpProtocol": swQinQRuleIpProtocol,
       "swQinQRuleSourcePort": swQinQRuleSourcePort,
       "swQinQRuleDestinationPort": swQinQRuleDestinationPort,
       "swQinQRuleSpvidOperation": swQinQRuleSpvidOperation,
       "swQinQRuleSpvid": swQinQRuleSpvid,
       "swQinQPriority": swQinQPriority,
       "swQinQRuleRowStatus": swQinQRuleRowStatus,
       "swQinQRuleActivePort": swQinQRuleActivePort,
       "swVlanTranslationCVIDTable": swVlanTranslationCVIDTable,
       "swVlanTranslationCVIDEntry": swVlanTranslationCVIDEntry,
       "swVlanTranslationCVID": swVlanTranslationCVID,
       "swVlanTranslationSVID": swVlanTranslationSVID,
       "swVlanTranslationSVIDOperation": swVlanTranslationSVIDOperation,
       "swVlanTranslationCVIDRowStatus": swVlanTranslationCVIDRowStatus}
)
