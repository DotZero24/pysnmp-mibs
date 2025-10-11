# SNMP MIB module (SUPERMICRO-DOT1AD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-DOT1AD-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:03:44 2025
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dot1adMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 130)
)
if mibBuilder.loadTexts:
    dot1adMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PriorityCodePoint(TextualConvention, Integer32):
    status = "current"
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
        *(("codePoint8p0d", 1),
          ("codePoint7p1d", 2),
          ("codePoint6p2d", 3),
          ("codePoint5p3d", 4))
    )



class VlanId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



# MIB Managed Objects in the order of their OIDs

_Dot1adProviderBridge_ObjectIdentity = ObjectIdentity
dot1adProviderBridge = _Dot1adProviderBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 130, 1)
)
_Dot1adPortTable_Object = MibTable
dot1adPortTable = _Dot1adPortTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 130, 1, 1)
)
if mibBuilder.loadTexts:
    dot1adPortTable.setStatus("current")
_Dot1adPortEntry_Object = MibTableRow
dot1adPortEntry = _Dot1adPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 130, 1, 1, 1)
)
dot1adPortEntry.setIndexNames(
    (0, "SUPERMICRO-DOT1AD-MIB", "dot1adPortNum"),
)
if mibBuilder.loadTexts:
    dot1adPortEntry.setStatus("current")


class _Dot1adPortNum_Type(Integer32):
    """Custom type dot1adPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot1adPortNum_Type.__name__ = "Integer32"
_Dot1adPortNum_Object = MibTableColumn
dot1adPortNum = _Dot1adPortNum_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 130, 1, 1, 1, 1),
    _Dot1adPortNum_Type()
)
dot1adPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1adPortNum.setStatus("current")


class _Dot1adPortPcpSelectionRow_Type(PriorityCodePoint):
    """Custom type dot1adPortPcpSelectionRow based on PriorityCodePoint"""
    defaultValue = 1


_Dot1adPortPcpSelectionRow_Type.__name__ = "PriorityCodePoint"
_Dot1adPortPcpSelectionRow_Object = MibTableColumn
dot1adPortPcpSelectionRow = _Dot1adPortPcpSelectionRow_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 130, 1, 1, 1, 2),
    _Dot1adPortPcpSelectionRow_Type()
)
dot1adPortPcpSelectionRow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1adPortPcpSelectionRow.setStatus("current")


class _Dot1adPortUseDei_Type(TruthValue):
    """Custom type dot1adPortUseDei based on TruthValue"""
    defaultValue = 2


_Dot1adPortUseDei_Type.__name__ = "TruthValue"
_Dot1adPortUseDei_Object = MibTableColumn
dot1adPortUseDei = _Dot1adPortUseDei_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 130, 1, 1, 1, 3),
    _Dot1adPortUseDei_Type()
)
dot1adPortUseDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1adPortUseDei.setStatus("current")


class _Dot1adPortReqDropEncoding_Type(TruthValue):
    """Custom type dot1adPortReqDropEncoding based on TruthValue"""
    defaultValue = 2


_Dot1adPortReqDropEncoding_Type.__name__ = "TruthValue"
_Dot1adPortReqDropEncoding_Object = MibTableColumn
dot1adPortReqDropEncoding = _Dot1adPortReqDropEncoding_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 130, 1, 1, 1, 4),
    _Dot1adPortReqDropEncoding_Type()
)
dot1adPortReqDropEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1adPortReqDropEncoding.setStatus("current")
_Dot1adVidTranslationTable_Object = MibTable
dot1adVidTranslationTable = _Dot1adVidTranslationTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 130, 1, 2)
)
if mibBuilder.loadTexts:
    dot1adVidTranslationTable.setStatus("current")
_Dot1adVidTranslationEntry_Object = MibTableRow
dot1adVidTranslationEntry = _Dot1adVidTranslationEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 130, 1, 2, 1)
)
dot1adVidTranslationEntry.setIndexNames(
    (0, "SUPERMICRO-DOT1AD-MIB", "dot1adPortNum"),
    (0, "SUPERMICRO-DOT1AD-MIB", "dot1adVidTranslationLocalVid"),
)
if mibBuilder.loadTexts:
    dot1adVidTranslationEntry.setStatus("current")
_Dot1adVidTranslationLocalVid_Type = VlanId
_Dot1adVidTranslationLocalVid_Object = MibTableColumn
dot1adVidTranslationLocalVid = _Dot1adVidTranslationLocalVid_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 130, 1, 2, 1, 1),
    _Dot1adVidTranslationLocalVid_Type()
)
dot1adVidTranslationLocalVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1adVidTranslationLocalVid.setStatus("current")
_Dot1adVidTranslationRelayVid_Type = VlanId
_Dot1adVidTranslationRelayVid_Object = MibTableColumn
dot1adVidTranslationRelayVid = _Dot1adVidTranslationRelayVid_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 130, 1, 2, 1, 2),
    _Dot1adVidTranslationRelayVid_Type()
)
dot1adVidTranslationRelayVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1adVidTranslationRelayVid.setStatus("current")
_Dot1adVidTranslationRowStatus_Type = RowStatus
_Dot1adVidTranslationRowStatus_Object = MibTableColumn
dot1adVidTranslationRowStatus = _Dot1adVidTranslationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 130, 1, 2, 1, 3),
    _Dot1adVidTranslationRowStatus_Type()
)
dot1adVidTranslationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1adVidTranslationRowStatus.setStatus("current")
_Dot1adCVidRegistrationTable_Object = MibTable
dot1adCVidRegistrationTable = _Dot1adCVidRegistrationTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 130, 1, 3)
)
if mibBuilder.loadTexts:
    dot1adCVidRegistrationTable.setStatus("current")
_Dot1adCVidRegistrationEntry_Object = MibTableRow
dot1adCVidRegistrationEntry = _Dot1adCVidRegistrationEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 130, 1, 3, 1)
)
dot1adCVidRegistrationEntry.setIndexNames(
    (0, "SUPERMICRO-DOT1AD-MIB", "dot1adPortNum"),
    (0, "SUPERMICRO-DOT1AD-MIB", "dot1adCVidRegistrationCVid"),
)
if mibBuilder.loadTexts:
    dot1adCVidRegistrationEntry.setStatus("current")
_Dot1adCVidRegistrationCVid_Type = VlanId
_Dot1adCVidRegistrationCVid_Object = MibTableColumn
dot1adCVidRegistrationCVid = _Dot1adCVidRegistrationCVid_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 130, 1, 3, 1, 1),
    _Dot1adCVidRegistrationCVid_Type()
)
dot1adCVidRegistrationCVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1adCVidRegistrationCVid.setStatus("current")
_Dot1adCVidRegistrationSVid_Type = VlanId
_Dot1adCVidRegistrationSVid_Object = MibTableColumn
dot1adCVidRegistrationSVid = _Dot1adCVidRegistrationSVid_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 130, 1, 3, 1, 2),
    _Dot1adCVidRegistrationSVid_Type()
)
dot1adCVidRegistrationSVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1adCVidRegistrationSVid.setStatus("current")


class _Dot1adCVidRegistrationUntaggedPep_Type(TruthValue):
    """Custom type dot1adCVidRegistrationUntaggedPep based on TruthValue"""
    defaultValue = 2


_Dot1adCVidRegistrationUntaggedPep_Type.__name__ = "TruthValue"
_Dot1adCVidRegistrationUntaggedPep_Object = MibTableColumn
dot1adCVidRegistrationUntaggedPep = _Dot1adCVidRegistrationUntaggedPep_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 130, 1, 3, 1, 3),
    _Dot1adCVidRegistrationUntaggedPep_Type()
)
dot1adCVidRegistrationUntaggedPep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1adCVidRegistrationUntaggedPep.setStatus("current")


class _Dot1adCVidRegistrationUntaggedCep_Type(TruthValue):
    """Custom type dot1adCVidRegistrationUntaggedCep based on TruthValue"""
    defaultValue = 2


_Dot1adCVidRegistrationUntaggedCep_Type.__name__ = "TruthValue"
_Dot1adCVidRegistrationUntaggedCep_Object = MibTableColumn
dot1adCVidRegistrationUntaggedCep = _Dot1adCVidRegistrationUntaggedCep_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 130, 1, 3, 1, 4),
    _Dot1adCVidRegistrationUntaggedCep_Type()
)
dot1adCVidRegistrationUntaggedCep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1adCVidRegistrationUntaggedCep.setStatus("current")
_Dot1adCVidRegistrationRowStatus_Type = RowStatus
_Dot1adCVidRegistrationRowStatus_Object = MibTableColumn
dot1adCVidRegistrationRowStatus = _Dot1adCVidRegistrationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 130, 1, 3, 1, 5),
    _Dot1adCVidRegistrationRowStatus_Type()
)
dot1adCVidRegistrationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1adCVidRegistrationRowStatus.setStatus("current")
_Dot1adPepTable_Object = MibTable
dot1adPepTable = _Dot1adPepTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 130, 1, 4)
)
if mibBuilder.loadTexts:
    dot1adPepTable.setStatus("current")
_Dot1adPepEntry_Object = MibTableRow
dot1adPepEntry = _Dot1adPepEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 130, 1, 4, 1)
)
dot1adPepEntry.setIndexNames(
    (0, "SUPERMICRO-DOT1AD-MIB", "dot1adPortNum"),
    (0, "SUPERMICRO-DOT1AD-MIB", "dot1adCVidRegistrationSVid"),
)
if mibBuilder.loadTexts:
    dot1adPepEntry.setStatus("current")
_Dot1adPepPvid_Type = VlanId
_Dot1adPepPvid_Object = MibTableColumn
dot1adPepPvid = _Dot1adPepPvid_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 130, 1, 4, 1, 1),
    _Dot1adPepPvid_Type()
)
dot1adPepPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1adPepPvid.setStatus("current")


class _Dot1adPepDefaultUserPriority_Type(Integer32):
    """Custom type dot1adPepDefaultUserPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dot1adPepDefaultUserPriority_Type.__name__ = "Integer32"
_Dot1adPepDefaultUserPriority_Object = MibTableColumn
dot1adPepDefaultUserPriority = _Dot1adPepDefaultUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 130, 1, 4, 1, 2),
    _Dot1adPepDefaultUserPriority_Type()
)
dot1adPepDefaultUserPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1adPepDefaultUserPriority.setStatus("current")


class _Dot1adPepAccptableFrameTypes_Type(Integer32):
    """Custom type dot1adPepAccptableFrameTypes based on Integer32"""
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
        *(("admitAll", 1),
          ("admitOnlyVlanTagged", 2),
          ("admitOnlyUntaggedAndPriorityTagged", 3))
    )


_Dot1adPepAccptableFrameTypes_Type.__name__ = "Integer32"
_Dot1adPepAccptableFrameTypes_Object = MibTableColumn
dot1adPepAccptableFrameTypes = _Dot1adPepAccptableFrameTypes_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 130, 1, 4, 1, 3),
    _Dot1adPepAccptableFrameTypes_Type()
)
dot1adPepAccptableFrameTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1adPepAccptableFrameTypes.setStatus("current")


class _Dot1adPepIngressFiltering_Type(TruthValue):
    """Custom type dot1adPepIngressFiltering based on TruthValue"""
    defaultValue = 2


_Dot1adPepIngressFiltering_Type.__name__ = "TruthValue"
_Dot1adPepIngressFiltering_Object = MibTableColumn
dot1adPepIngressFiltering = _Dot1adPepIngressFiltering_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 130, 1, 4, 1, 4),
    _Dot1adPepIngressFiltering_Type()
)
dot1adPepIngressFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1adPepIngressFiltering.setStatus("current")
_Dot1adServicePriorityRegenerationTable_Object = MibTable
dot1adServicePriorityRegenerationTable = _Dot1adServicePriorityRegenerationTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 130, 1, 5)
)
if mibBuilder.loadTexts:
    dot1adServicePriorityRegenerationTable.setStatus("current")
_Dot1adServicePriorityRegenerationEntry_Object = MibTableRow
dot1adServicePriorityRegenerationEntry = _Dot1adServicePriorityRegenerationEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 130, 1, 5, 1)
)
dot1adServicePriorityRegenerationEntry.setIndexNames(
    (0, "SUPERMICRO-DOT1AD-MIB", "dot1adPortNum"),
    (0, "SUPERMICRO-DOT1AD-MIB", "dot1adCVidRegistrationSVid"),
    (0, "SUPERMICRO-DOT1AD-MIB", "dot1adServicePriorityRegenReceivedPriority"),
)
if mibBuilder.loadTexts:
    dot1adServicePriorityRegenerationEntry.setStatus("current")


class _Dot1adServicePriorityRegenReceivedPriority_Type(Integer32):
    """Custom type dot1adServicePriorityRegenReceivedPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dot1adServicePriorityRegenReceivedPriority_Type.__name__ = "Integer32"
_Dot1adServicePriorityRegenReceivedPriority_Object = MibTableColumn
dot1adServicePriorityRegenReceivedPriority = _Dot1adServicePriorityRegenReceivedPriority_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 130, 1, 5, 1, 1),
    _Dot1adServicePriorityRegenReceivedPriority_Type()
)
dot1adServicePriorityRegenReceivedPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1adServicePriorityRegenReceivedPriority.setStatus("current")


class _Dot1adServicePriorityRegenRegeneratedPriority_Type(Integer32):
    """Custom type dot1adServicePriorityRegenRegeneratedPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dot1adServicePriorityRegenRegeneratedPriority_Type.__name__ = "Integer32"
_Dot1adServicePriorityRegenRegeneratedPriority_Object = MibTableColumn
dot1adServicePriorityRegenRegeneratedPriority = _Dot1adServicePriorityRegenRegeneratedPriority_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 130, 1, 5, 1, 2),
    _Dot1adServicePriorityRegenRegeneratedPriority_Type()
)
dot1adServicePriorityRegenRegeneratedPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1adServicePriorityRegenRegeneratedPriority.setStatus("current")
_Dot1adPcpDecodingTable_Object = MibTable
dot1adPcpDecodingTable = _Dot1adPcpDecodingTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 130, 1, 6)
)
if mibBuilder.loadTexts:
    dot1adPcpDecodingTable.setStatus("current")
_Dot1adPcpDecodingEntry_Object = MibTableRow
dot1adPcpDecodingEntry = _Dot1adPcpDecodingEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 130, 1, 6, 1)
)
dot1adPcpDecodingEntry.setIndexNames(
    (0, "SUPERMICRO-DOT1AD-MIB", "dot1adPortNum"),
    (0, "SUPERMICRO-DOT1AD-MIB", "dot1adPcpDecodingPcpSelRow"),
    (0, "SUPERMICRO-DOT1AD-MIB", "dot1adPcpDecodingPcpValue"),
)
if mibBuilder.loadTexts:
    dot1adPcpDecodingEntry.setStatus("current")
_Dot1adPcpDecodingPcpSelRow_Type = PriorityCodePoint
_Dot1adPcpDecodingPcpSelRow_Object = MibTableColumn
dot1adPcpDecodingPcpSelRow = _Dot1adPcpDecodingPcpSelRow_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 130, 1, 6, 1, 1),
    _Dot1adPcpDecodingPcpSelRow_Type()
)
dot1adPcpDecodingPcpSelRow.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1adPcpDecodingPcpSelRow.setStatus("current")


class _Dot1adPcpDecodingPcpValue_Type(Integer32):
    """Custom type dot1adPcpDecodingPcpValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dot1adPcpDecodingPcpValue_Type.__name__ = "Integer32"
_Dot1adPcpDecodingPcpValue_Object = MibTableColumn
dot1adPcpDecodingPcpValue = _Dot1adPcpDecodingPcpValue_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 130, 1, 6, 1, 2),
    _Dot1adPcpDecodingPcpValue_Type()
)
dot1adPcpDecodingPcpValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1adPcpDecodingPcpValue.setStatus("current")


class _Dot1adPcpDecodingPriority_Type(Integer32):
    """Custom type dot1adPcpDecodingPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dot1adPcpDecodingPriority_Type.__name__ = "Integer32"
_Dot1adPcpDecodingPriority_Object = MibTableColumn
dot1adPcpDecodingPriority = _Dot1adPcpDecodingPriority_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 130, 1, 6, 1, 3),
    _Dot1adPcpDecodingPriority_Type()
)
dot1adPcpDecodingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1adPcpDecodingPriority.setStatus("current")
_Dot1adPcpDecodingDropEligible_Type = TruthValue
_Dot1adPcpDecodingDropEligible_Object = MibTableColumn
dot1adPcpDecodingDropEligible = _Dot1adPcpDecodingDropEligible_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 130, 1, 6, 1, 4),
    _Dot1adPcpDecodingDropEligible_Type()
)
dot1adPcpDecodingDropEligible.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1adPcpDecodingDropEligible.setStatus("current")
_Dot1adPcpEncodingTable_Object = MibTable
dot1adPcpEncodingTable = _Dot1adPcpEncodingTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 130, 1, 7)
)
if mibBuilder.loadTexts:
    dot1adPcpEncodingTable.setStatus("current")
_Dot1adPcpEncodingEntry_Object = MibTableRow
dot1adPcpEncodingEntry = _Dot1adPcpEncodingEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 130, 1, 7, 1)
)
dot1adPcpEncodingEntry.setIndexNames(
    (0, "SUPERMICRO-DOT1AD-MIB", "dot1adPortNum"),
    (0, "SUPERMICRO-DOT1AD-MIB", "dot1adPcpEncodingPcpSelRow"),
    (0, "SUPERMICRO-DOT1AD-MIB", "dot1adPcpEncodingPriority"),
    (0, "SUPERMICRO-DOT1AD-MIB", "dot1adPcpEncodingDropEligible"),
)
if mibBuilder.loadTexts:
    dot1adPcpEncodingEntry.setStatus("current")
_Dot1adPcpEncodingPcpSelRow_Type = PriorityCodePoint
_Dot1adPcpEncodingPcpSelRow_Object = MibTableColumn
dot1adPcpEncodingPcpSelRow = _Dot1adPcpEncodingPcpSelRow_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 130, 1, 7, 1, 1),
    _Dot1adPcpEncodingPcpSelRow_Type()
)
dot1adPcpEncodingPcpSelRow.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1adPcpEncodingPcpSelRow.setStatus("current")


class _Dot1adPcpEncodingPriority_Type(Integer32):
    """Custom type dot1adPcpEncodingPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dot1adPcpEncodingPriority_Type.__name__ = "Integer32"
_Dot1adPcpEncodingPriority_Object = MibTableColumn
dot1adPcpEncodingPriority = _Dot1adPcpEncodingPriority_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 130, 1, 7, 1, 2),
    _Dot1adPcpEncodingPriority_Type()
)
dot1adPcpEncodingPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1adPcpEncodingPriority.setStatus("current")
_Dot1adPcpEncodingDropEligible_Type = TruthValue
_Dot1adPcpEncodingDropEligible_Object = MibTableColumn
dot1adPcpEncodingDropEligible = _Dot1adPcpEncodingDropEligible_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 130, 1, 7, 1, 3),
    _Dot1adPcpEncodingDropEligible_Type()
)
dot1adPcpEncodingDropEligible.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1adPcpEncodingDropEligible.setStatus("current")


class _Dot1adPcpEncodingPcpValue_Type(Integer32):
    """Custom type dot1adPcpEncodingPcpValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dot1adPcpEncodingPcpValue_Type.__name__ = "Integer32"
_Dot1adPcpEncodingPcpValue_Object = MibTableColumn
dot1adPcpEncodingPcpValue = _Dot1adPcpEncodingPcpValue_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 130, 1, 7, 1, 4),
    _Dot1adPcpEncodingPcpValue_Type()
)
dot1adPcpEncodingPcpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1adPcpEncodingPcpValue.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-DOT1AD-MIB",
    **{"PriorityCodePoint": PriorityCodePoint,
       "VlanId": VlanId,
       "dot1adMIB": dot1adMIB,
       "dot1adProviderBridge": dot1adProviderBridge,
       "dot1adPortTable": dot1adPortTable,
       "dot1adPortEntry": dot1adPortEntry,
       "dot1adPortNum": dot1adPortNum,
       "dot1adPortPcpSelectionRow": dot1adPortPcpSelectionRow,
       "dot1adPortUseDei": dot1adPortUseDei,
       "dot1adPortReqDropEncoding": dot1adPortReqDropEncoding,
       "dot1adVidTranslationTable": dot1adVidTranslationTable,
       "dot1adVidTranslationEntry": dot1adVidTranslationEntry,
       "dot1adVidTranslationLocalVid": dot1adVidTranslationLocalVid,
       "dot1adVidTranslationRelayVid": dot1adVidTranslationRelayVid,
       "dot1adVidTranslationRowStatus": dot1adVidTranslationRowStatus,
       "dot1adCVidRegistrationTable": dot1adCVidRegistrationTable,
       "dot1adCVidRegistrationEntry": dot1adCVidRegistrationEntry,
       "dot1adCVidRegistrationCVid": dot1adCVidRegistrationCVid,
       "dot1adCVidRegistrationSVid": dot1adCVidRegistrationSVid,
       "dot1adCVidRegistrationUntaggedPep": dot1adCVidRegistrationUntaggedPep,
       "dot1adCVidRegistrationUntaggedCep": dot1adCVidRegistrationUntaggedCep,
       "dot1adCVidRegistrationRowStatus": dot1adCVidRegistrationRowStatus,
       "dot1adPepTable": dot1adPepTable,
       "dot1adPepEntry": dot1adPepEntry,
       "dot1adPepPvid": dot1adPepPvid,
       "dot1adPepDefaultUserPriority": dot1adPepDefaultUserPriority,
       "dot1adPepAccptableFrameTypes": dot1adPepAccptableFrameTypes,
       "dot1adPepIngressFiltering": dot1adPepIngressFiltering,
       "dot1adServicePriorityRegenerationTable": dot1adServicePriorityRegenerationTable,
       "dot1adServicePriorityRegenerationEntry": dot1adServicePriorityRegenerationEntry,
       "dot1adServicePriorityRegenReceivedPriority": dot1adServicePriorityRegenReceivedPriority,
       "dot1adServicePriorityRegenRegeneratedPriority": dot1adServicePriorityRegenRegeneratedPriority,
       "dot1adPcpDecodingTable": dot1adPcpDecodingTable,
       "dot1adPcpDecodingEntry": dot1adPcpDecodingEntry,
       "dot1adPcpDecodingPcpSelRow": dot1adPcpDecodingPcpSelRow,
       "dot1adPcpDecodingPcpValue": dot1adPcpDecodingPcpValue,
       "dot1adPcpDecodingPriority": dot1adPcpDecodingPriority,
       "dot1adPcpDecodingDropEligible": dot1adPcpDecodingDropEligible,
       "dot1adPcpEncodingTable": dot1adPcpEncodingTable,
       "dot1adPcpEncodingEntry": dot1adPcpEncodingEntry,
       "dot1adPcpEncodingPcpSelRow": dot1adPcpEncodingPcpSelRow,
       "dot1adPcpEncodingPriority": dot1adPcpEncodingPriority,
       "dot1adPcpEncodingDropEligible": dot1adPcpEncodingDropEligible,
       "dot1adPcpEncodingPcpValue": dot1adPcpEncodingPcpValue}
)
