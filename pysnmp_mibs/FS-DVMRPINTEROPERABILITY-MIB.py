# SNMP MIB module (FS-DVMRPINTEROPERABILITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-DVMRPINTEROPERABILITY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:14:49 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fsDvmrpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29)
)
if mibBuilder.loadTexts:
    fsDvmrpMIB.setRevisions(
        ("2003-01-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsDvmrpMIBObjects_ObjectIdentity = ObjectIdentity
fsDvmrpMIBObjects = _FsDvmrpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1)
)
_FsDvmrpGroup_ObjectIdentity = ObjectIdentity
fsDvmrpGroup = _FsDvmrpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1, 1)
)


class _FsDvmrpRouteLimit_Type(Unsigned32):
    """Custom type fsDvmrpRouteLimit based on Unsigned32"""
    defaultValue = 7000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsDvmrpRouteLimit_Type.__name__ = "Unsigned32"
_FsDvmrpRouteLimit_Object = MibScalar
fsDvmrpRouteLimit = _FsDvmrpRouteLimit_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1, 1, 1),
    _FsDvmrpRouteLimit_Type()
)
fsDvmrpRouteLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDvmrpRouteLimit.setStatus("current")


class _FsDvmrpRoutehogNotification_Type(Unsigned32):
    """Custom type fsDvmrpRoutehogNotification based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsDvmrpRoutehogNotification_Type.__name__ = "Unsigned32"
_FsDvmrpRoutehogNotification_Object = MibScalar
fsDvmrpRoutehogNotification = _FsDvmrpRoutehogNotification_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1, 1, 2),
    _FsDvmrpRoutehogNotification_Type()
)
fsDvmrpRoutehogNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDvmrpRoutehogNotification.setStatus("current")
_FsDvmrpInterfaceTable_Object = MibTable
fsDvmrpInterfaceTable = _FsDvmrpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1, 2)
)
if mibBuilder.loadTexts:
    fsDvmrpInterfaceTable.setStatus("current")
_FsDvmrpInterfaceEntry_Object = MibTableRow
fsDvmrpInterfaceEntry = _FsDvmrpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1, 2, 1)
)
fsDvmrpInterfaceEntry.setIndexNames(
    (0, "FS-DVMRPINTEROPERABILITY-MIB", "fsDvmrpInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    fsDvmrpInterfaceEntry.setStatus("current")
_FsDvmrpInterfaceIfIndex_Type = InterfaceIndex
_FsDvmrpInterfaceIfIndex_Object = MibTableColumn
fsDvmrpInterfaceIfIndex = _FsDvmrpInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1, 2, 1, 1),
    _FsDvmrpInterfaceIfIndex_Type()
)
fsDvmrpInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDvmrpInterfaceIfIndex.setStatus("current")


class _FsDvmrpInterfaceDefaultInformation_Type(Integer32):
    """Custom type fsDvmrpInterfaceDefaultInformation based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("originate", 1),
          ("only", 2))
    )


_FsDvmrpInterfaceDefaultInformation_Type.__name__ = "Integer32"
_FsDvmrpInterfaceDefaultInformation_Object = MibTableColumn
fsDvmrpInterfaceDefaultInformation = _FsDvmrpInterfaceDefaultInformation_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1, 2, 1, 2),
    _FsDvmrpInterfaceDefaultInformation_Type()
)
fsDvmrpInterfaceDefaultInformation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDvmrpInterfaceDefaultInformation.setStatus("current")


class _FsDvmrpInterfaceUnicastRoutingStatus_Type(EnabledStatus):
    """Custom type fsDvmrpInterfaceUnicastRoutingStatus based on EnabledStatus"""
    defaultValue = 2


_FsDvmrpInterfaceUnicastRoutingStatus_Type.__name__ = "EnabledStatus"
_FsDvmrpInterfaceUnicastRoutingStatus_Object = MibTableColumn
fsDvmrpInterfaceUnicastRoutingStatus = _FsDvmrpInterfaceUnicastRoutingStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1, 2, 1, 3),
    _FsDvmrpInterfaceUnicastRoutingStatus_Type()
)
fsDvmrpInterfaceUnicastRoutingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDvmrpInterfaceUnicastRoutingStatus.setStatus("current")


class _FsDvmrpInterfaceRejectNonPrunersStatus_Type(EnabledStatus):
    """Custom type fsDvmrpInterfaceRejectNonPrunersStatus based on EnabledStatus"""
    defaultValue = 2


_FsDvmrpInterfaceRejectNonPrunersStatus_Type.__name__ = "EnabledStatus"
_FsDvmrpInterfaceRejectNonPrunersStatus_Object = MibTableColumn
fsDvmrpInterfaceRejectNonPrunersStatus = _FsDvmrpInterfaceRejectNonPrunersStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1, 2, 1, 4),
    _FsDvmrpInterfaceRejectNonPrunersStatus_Type()
)
fsDvmrpInterfaceRejectNonPrunersStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDvmrpInterfaceRejectNonPrunersStatus.setStatus("current")


class _FsDvmrpInterfaceAutoSummaryStatus_Type(EnabledStatus):
    """Custom type fsDvmrpInterfaceAutoSummaryStatus based on EnabledStatus"""
    defaultValue = 1


_FsDvmrpInterfaceAutoSummaryStatus_Type.__name__ = "EnabledStatus"
_FsDvmrpInterfaceAutoSummaryStatus_Object = MibTableColumn
fsDvmrpInterfaceAutoSummaryStatus = _FsDvmrpInterfaceAutoSummaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1, 2, 1, 5),
    _FsDvmrpInterfaceAutoSummaryStatus_Type()
)
fsDvmrpInterfaceAutoSummaryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDvmrpInterfaceAutoSummaryStatus.setStatus("current")
_FsDvmrpInterfaceRtsRec_Type = Integer32
_FsDvmrpInterfaceRtsRec_Object = MibTableColumn
fsDvmrpInterfaceRtsRec = _FsDvmrpInterfaceRtsRec_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1, 2, 1, 6),
    _FsDvmrpInterfaceRtsRec_Type()
)
fsDvmrpInterfaceRtsRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDvmrpInterfaceRtsRec.setStatus("current")
_FsDvmrpInterfacePoisonReverseRtsRec_Type = Integer32
_FsDvmrpInterfacePoisonReverseRtsRec_Object = MibTableColumn
fsDvmrpInterfacePoisonReverseRtsRec = _FsDvmrpInterfacePoisonReverseRtsRec_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1, 2, 1, 7),
    _FsDvmrpInterfacePoisonReverseRtsRec_Type()
)
fsDvmrpInterfacePoisonReverseRtsRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDvmrpInterfacePoisonReverseRtsRec.setStatus("current")
_FsDvmrpInterfaceUniRtAdvertised_Type = Integer32
_FsDvmrpInterfaceUniRtAdvertised_Object = MibTableColumn
fsDvmrpInterfaceUniRtAdvertised = _FsDvmrpInterfaceUniRtAdvertised_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1, 2, 1, 8),
    _FsDvmrpInterfaceUniRtAdvertised_Type()
)
fsDvmrpInterfaceUniRtAdvertised.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDvmrpInterfaceUniRtAdvertised.setStatus("current")
_FsDvmrpInterfaceDvmrpRtAdvertised_Type = Integer32
_FsDvmrpInterfaceDvmrpRtAdvertised_Object = MibTableColumn
fsDvmrpInterfaceDvmrpRtAdvertised = _FsDvmrpInterfaceDvmrpRtAdvertised_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1, 2, 1, 9),
    _FsDvmrpInterfaceDvmrpRtAdvertised_Type()
)
fsDvmrpInterfaceDvmrpRtAdvertised.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDvmrpInterfaceDvmrpRtAdvertised.setStatus("current")
_FsDvmrpMetricOffsetTable_Object = MibTable
fsDvmrpMetricOffsetTable = _FsDvmrpMetricOffsetTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1, 3)
)
if mibBuilder.loadTexts:
    fsDvmrpMetricOffsetTable.setStatus("current")
_FsDvmrpMetricOffsetEntry_Object = MibTableRow
fsDvmrpMetricOffsetEntry = _FsDvmrpMetricOffsetEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1, 3, 1)
)
fsDvmrpMetricOffsetEntry.setIndexNames(
    (0, "FS-DVMRPINTEROPERABILITY-MIB", "fsDvmrpMetricOffsetIfIndex"),
    (0, "FS-DVMRPINTEROPERABILITY-MIB", "fsDvmrpMetricOffsetInOrOut"),
)
if mibBuilder.loadTexts:
    fsDvmrpMetricOffsetEntry.setStatus("current")
_FsDvmrpMetricOffsetIfIndex_Type = InterfaceIndex
_FsDvmrpMetricOffsetIfIndex_Object = MibTableColumn
fsDvmrpMetricOffsetIfIndex = _FsDvmrpMetricOffsetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1, 3, 1, 1),
    _FsDvmrpMetricOffsetIfIndex_Type()
)
fsDvmrpMetricOffsetIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDvmrpMetricOffsetIfIndex.setStatus("current")


class _FsDvmrpMetricOffsetInOrOut_Type(Integer32):
    """Custom type fsDvmrpMetricOffsetInOrOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_FsDvmrpMetricOffsetInOrOut_Type.__name__ = "Integer32"
_FsDvmrpMetricOffsetInOrOut_Object = MibTableColumn
fsDvmrpMetricOffsetInOrOut = _FsDvmrpMetricOffsetInOrOut_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1, 3, 1, 2),
    _FsDvmrpMetricOffsetInOrOut_Type()
)
fsDvmrpMetricOffsetInOrOut.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDvmrpMetricOffsetInOrOut.setStatus("current")


class _FsDvmrpMetricOffsetIncrement_Type(Integer32):
    """Custom type fsDvmrpMetricOffsetIncrement based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_FsDvmrpMetricOffsetIncrement_Type.__name__ = "Integer32"
_FsDvmrpMetricOffsetIncrement_Object = MibTableColumn
fsDvmrpMetricOffsetIncrement = _FsDvmrpMetricOffsetIncrement_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1, 3, 1, 3),
    _FsDvmrpMetricOffsetIncrement_Type()
)
fsDvmrpMetricOffsetIncrement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDvmrpMetricOffsetIncrement.setStatus("current")
_FsDvmrpSummaryTable_Object = MibTable
fsDvmrpSummaryTable = _FsDvmrpSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1, 4)
)
if mibBuilder.loadTexts:
    fsDvmrpSummaryTable.setStatus("current")
_FsDvmrpSummaryEntry_Object = MibTableRow
fsDvmrpSummaryEntry = _FsDvmrpSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1, 4, 1)
)
fsDvmrpSummaryEntry.setIndexNames(
    (0, "FS-DVMRPINTEROPERABILITY-MIB", "fsDvmrpIfIndex"),
    (0, "FS-DVMRPINTEROPERABILITY-MIB", "fsDvmrpSummaryAddress"),
    (0, "FS-DVMRPINTEROPERABILITY-MIB", "fsDvmrpSummaryMask"),
)
if mibBuilder.loadTexts:
    fsDvmrpSummaryEntry.setStatus("current")
_FsDvmrpIfIndex_Type = InterfaceIndex
_FsDvmrpIfIndex_Object = MibTableColumn
fsDvmrpIfIndex = _FsDvmrpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1, 4, 1, 1),
    _FsDvmrpIfIndex_Type()
)
fsDvmrpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDvmrpIfIndex.setStatus("current")
_FsDvmrpSummaryAddress_Type = IpAddress
_FsDvmrpSummaryAddress_Object = MibTableColumn
fsDvmrpSummaryAddress = _FsDvmrpSummaryAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1, 4, 1, 2),
    _FsDvmrpSummaryAddress_Type()
)
fsDvmrpSummaryAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDvmrpSummaryAddress.setStatus("current")
_FsDvmrpSummaryMask_Type = IpAddress
_FsDvmrpSummaryMask_Object = MibTableColumn
fsDvmrpSummaryMask = _FsDvmrpSummaryMask_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1, 4, 1, 3),
    _FsDvmrpSummaryMask_Type()
)
fsDvmrpSummaryMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDvmrpSummaryMask.setStatus("current")


class _FsDvmrpSummaryMetric_Type(Integer32):
    """Custom type fsDvmrpSummaryMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_FsDvmrpSummaryMetric_Type.__name__ = "Integer32"
_FsDvmrpSummaryMetric_Object = MibTableColumn
fsDvmrpSummaryMetric = _FsDvmrpSummaryMetric_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1, 4, 1, 4),
    _FsDvmrpSummaryMetric_Type()
)
fsDvmrpSummaryMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDvmrpSummaryMetric.setStatus("current")
_FsDvmrpSummaryStatus_Type = RowStatus
_FsDvmrpSummaryStatus_Object = MibTableColumn
fsDvmrpSummaryStatus = _FsDvmrpSummaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1, 4, 1, 5),
    _FsDvmrpSummaryStatus_Type()
)
fsDvmrpSummaryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDvmrpSummaryStatus.setStatus("current")
_FsDvmrpMetricTable_Object = MibTable
fsDvmrpMetricTable = _FsDvmrpMetricTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1, 5)
)
if mibBuilder.loadTexts:
    fsDvmrpMetricTable.setStatus("current")
_FsDvmrpMetricEntry_Object = MibTableRow
fsDvmrpMetricEntry = _FsDvmrpMetricEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1, 5, 1)
)
fsDvmrpMetricEntry.setIndexNames(
    (0, "FS-DVMRPINTEROPERABILITY-MIB", "fsDvmrpMetricIfIndex"),
    (0, "FS-DVMRPINTEROPERABILITY-MIB", "fsDvmrpMetric"),
    (0, "FS-DVMRPINTEROPERABILITY-MIB", "fsDvmrpMetricProtocolId"),
)
if mibBuilder.loadTexts:
    fsDvmrpMetricEntry.setStatus("current")
_FsDvmrpMetricIfIndex_Type = InterfaceIndex
_FsDvmrpMetricIfIndex_Object = MibTableColumn
fsDvmrpMetricIfIndex = _FsDvmrpMetricIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1, 5, 1, 1),
    _FsDvmrpMetricIfIndex_Type()
)
fsDvmrpMetricIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDvmrpMetricIfIndex.setStatus("current")


class _FsDvmrpMetric_Type(Integer32):
    """Custom type fsDvmrpMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_FsDvmrpMetric_Type.__name__ = "Integer32"
_FsDvmrpMetric_Object = MibTableColumn
fsDvmrpMetric = _FsDvmrpMetric_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1, 5, 1, 2),
    _FsDvmrpMetric_Type()
)
fsDvmrpMetric.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDvmrpMetric.setStatus("current")
_FsDvmrpMetricListAclName_Type = DisplayString
_FsDvmrpMetricListAclName_Object = MibTableColumn
fsDvmrpMetricListAclName = _FsDvmrpMetricListAclName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1, 5, 1, 3),
    _FsDvmrpMetricListAclName_Type()
)
fsDvmrpMetricListAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDvmrpMetricListAclName.setStatus("current")


class _FsDvmrpMetricProtocolId_Type(Integer32):
    """Custom type fsDvmrpMetricProtocolId based on Integer32"""
    defaultValue = 0

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
        *(("default", 0),
          ("ospf", 1),
          ("rip", 2),
          ("static", 3),
          ("dvmrp", 4))
    )


_FsDvmrpMetricProtocolId_Type.__name__ = "Integer32"
_FsDvmrpMetricProtocolId_Object = MibTableColumn
fsDvmrpMetricProtocolId = _FsDvmrpMetricProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1, 5, 1, 4),
    _FsDvmrpMetricProtocolId_Type()
)
fsDvmrpMetricProtocolId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDvmrpMetricProtocolId.setStatus("current")
_FsDvmrpMetricStatus_Type = RowStatus
_FsDvmrpMetricStatus_Object = MibTableColumn
fsDvmrpMetricStatus = _FsDvmrpMetricStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1, 5, 1, 5),
    _FsDvmrpMetricStatus_Type()
)
fsDvmrpMetricStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDvmrpMetricStatus.setStatus("current")
_FsDvmrpRouteTable_Object = MibTable
fsDvmrpRouteTable = _FsDvmrpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1, 6)
)
if mibBuilder.loadTexts:
    fsDvmrpRouteTable.setStatus("current")
_FsDvmrpRouteEntry_Object = MibTableRow
fsDvmrpRouteEntry = _FsDvmrpRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1, 6, 1)
)
fsDvmrpRouteEntry.setIndexNames(
    (0, "FS-DVMRPINTEROPERABILITY-MIB", "fsDvmrpRouteIpAddress"),
    (0, "FS-DVMRPINTEROPERABILITY-MIB", "fsDvmrpRouteInterface"),
)
if mibBuilder.loadTexts:
    fsDvmrpRouteEntry.setStatus("current")
_FsDvmrpRouteIpAddress_Type = IpAddress
_FsDvmrpRouteIpAddress_Object = MibTableColumn
fsDvmrpRouteIpAddress = _FsDvmrpRouteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1, 6, 1, 1),
    _FsDvmrpRouteIpAddress_Type()
)
fsDvmrpRouteIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDvmrpRouteIpAddress.setStatus("current")
_FsDvmrpRouteInterface_Type = InterfaceIndex
_FsDvmrpRouteInterface_Object = MibTableColumn
fsDvmrpRouteInterface = _FsDvmrpRouteInterface_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1, 6, 1, 2),
    _FsDvmrpRouteInterface_Type()
)
fsDvmrpRouteInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDvmrpRouteInterface.setStatus("current")
_FsDvmrpRouteDistance_Type = Integer32
_FsDvmrpRouteDistance_Object = MibTableColumn
fsDvmrpRouteDistance = _FsDvmrpRouteDistance_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1, 6, 1, 3),
    _FsDvmrpRouteDistance_Type()
)
fsDvmrpRouteDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDvmrpRouteDistance.setStatus("current")
_FsDvmrpRouteMetric_Type = Integer32
_FsDvmrpRouteMetric_Object = MibTableColumn
fsDvmrpRouteMetric = _FsDvmrpRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1, 6, 1, 4),
    _FsDvmrpRouteMetric_Type()
)
fsDvmrpRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDvmrpRouteMetric.setStatus("current")
_FsDvmrpRouteUptime_Type = TimeTicks
_FsDvmrpRouteUptime_Object = MibTableColumn
fsDvmrpRouteUptime = _FsDvmrpRouteUptime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1, 6, 1, 5),
    _FsDvmrpRouteUptime_Type()
)
fsDvmrpRouteUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDvmrpRouteUptime.setStatus("current")
_FsDvmrpRouteExpires_Type = TimeTicks
_FsDvmrpRouteExpires_Object = MibTableColumn
fsDvmrpRouteExpires = _FsDvmrpRouteExpires_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1, 6, 1, 6),
    _FsDvmrpRouteExpires_Type()
)
fsDvmrpRouteExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDvmrpRouteExpires.setStatus("current")
_FsDvmrpRouteNextHopAddress_Type = IpAddress
_FsDvmrpRouteNextHopAddress_Object = MibTableColumn
fsDvmrpRouteNextHopAddress = _FsDvmrpRouteNextHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1, 6, 1, 7),
    _FsDvmrpRouteNextHopAddress_Type()
)
fsDvmrpRouteNextHopAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDvmrpRouteNextHopAddress.setStatus("current")
_FsDvmrpRouteNextHopInterface_Type = InterfaceIndex
_FsDvmrpRouteNextHopInterface_Object = MibTableColumn
fsDvmrpRouteNextHopInterface = _FsDvmrpRouteNextHopInterface_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1, 6, 1, 8),
    _FsDvmrpRouteNextHopInterface_Type()
)
fsDvmrpRouteNextHopInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDvmrpRouteNextHopInterface.setStatus("current")
_FsDvmrpRouteStatus_Type = EnabledStatus
_FsDvmrpRouteStatus_Object = MibTableColumn
fsDvmrpRouteStatus = _FsDvmrpRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1, 6, 1, 9),
    _FsDvmrpRouteStatus_Type()
)
fsDvmrpRouteStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDvmrpRouteStatus.setStatus("current")
_FsDvmrpTraps_ObjectIdentity = ObjectIdentity
fsDvmrpTraps = _FsDvmrpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1, 7)
)
_FsDvmrpMIBConformance_ObjectIdentity = ObjectIdentity
fsDvmrpMIBConformance = _FsDvmrpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 2)
)
_FsDvmrpMIBCompliances_ObjectIdentity = ObjectIdentity
fsDvmrpMIBCompliances = _FsDvmrpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 2, 1)
)
_FsDvmrpMIBGroups_ObjectIdentity = ObjectIdentity
fsDvmrpMIBGroups = _FsDvmrpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 2, 2)
)

# Managed Objects groups

fsDvmrpBaseMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 2, 2, 1)
)
fsDvmrpBaseMIBGroup.setObjects(
      *(("FS-DVMRPINTEROPERABILITY-MIB", "fsDvmrpRouteLimit"),
        ("FS-DVMRPINTEROPERABILITY-MIB", "fsDvmrpRoutehogNotification"))
)
if mibBuilder.loadTexts:
    fsDvmrpBaseMIBGroup.setStatus("current")

fsDvmrpInterfaceMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 2, 2, 2)
)
fsDvmrpInterfaceMIBGroup.setObjects(
      *(("FS-DVMRPINTEROPERABILITY-MIB", "fsDvmrpInterfaceDefaultInformation"),
        ("FS-DVMRPINTEROPERABILITY-MIB", "fsDvmrpInterfaceUnicastRoutingStatus"),
        ("FS-DVMRPINTEROPERABILITY-MIB", "fsDvmrpInterfaceRejectNonPrunersStatus"),
        ("FS-DVMRPINTEROPERABILITY-MIB", "fsDvmrpInterfaceAutoSummaryStatus"),
        ("FS-DVMRPINTEROPERABILITY-MIB", "fsDvmrpInterfaceRtsRec"),
        ("FS-DVMRPINTEROPERABILITY-MIB", "fsDvmrpInterfacePoisonReverseRtsRec"),
        ("FS-DVMRPINTEROPERABILITY-MIB", "fsDvmrpInterfaceUniRtAdvertised"),
        ("FS-DVMRPINTEROPERABILITY-MIB", "fsDvmrpInterfaceDvmrpRtAdvertised"))
)
if mibBuilder.loadTexts:
    fsDvmrpInterfaceMIBGroup.setStatus("current")

fsDvmrpMetricOffsetMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 2, 2, 3)
)
fsDvmrpMetricOffsetMIBGroup.setObjects(
    ("FS-DVMRPINTEROPERABILITY-MIB", "fsDvmrpMetricOffsetIncrement")
)
if mibBuilder.loadTexts:
    fsDvmrpMetricOffsetMIBGroup.setStatus("current")

fsDvmrpSummaryMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 2, 2, 4)
)
fsDvmrpSummaryMIBGroup.setObjects(
      *(("FS-DVMRPINTEROPERABILITY-MIB", "fsDvmrpSummaryMetric"),
        ("FS-DVMRPINTEROPERABILITY-MIB", "fsDvmrpSummaryStatus"))
)
if mibBuilder.loadTexts:
    fsDvmrpSummaryMIBGroup.setStatus("current")

fsDvmrpMetricMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 2, 2, 5)
)
fsDvmrpMetricMIBGroup.setObjects(
      *(("FS-DVMRPINTEROPERABILITY-MIB", "fsDvmrpMetricListAclName"),
        ("FS-DVMRPINTEROPERABILITY-MIB", "fsDvmrpMetricStatus"))
)
if mibBuilder.loadTexts:
    fsDvmrpMetricMIBGroup.setStatus("current")

fsDvmrpRouteMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 2, 2, 6)
)
fsDvmrpRouteMIBGroup.setObjects(
      *(("FS-DVMRPINTEROPERABILITY-MIB", "fsDvmrpRouteDistance"),
        ("FS-DVMRPINTEROPERABILITY-MIB", "fsDvmrpRouteMetric"),
        ("FS-DVMRPINTEROPERABILITY-MIB", "fsDvmrpRouteUptime"),
        ("FS-DVMRPINTEROPERABILITY-MIB", "fsDvmrpRouteExpires"),
        ("FS-DVMRPINTEROPERABILITY-MIB", "fsDvmrpRouteNextHopAddress"),
        ("FS-DVMRPINTEROPERABILITY-MIB", "fsDvmrpRouteNextHopInterface"),
        ("FS-DVMRPINTEROPERABILITY-MIB", "fsDvmrpRouteStatus"))
)
if mibBuilder.loadTexts:
    fsDvmrpRouteMIBGroup.setStatus("current")


# Notification objects

fsDvmrpRouteInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 1, 7, 1)
)
if mibBuilder.loadTexts:
    fsDvmrpRouteInformation.setStatus(
        "current"
    )


# Notifications groups

fsDvmrpRouteTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 2, 2, 7)
)
fsDvmrpRouteTrapGroup.setObjects(
    ("FS-DVMRPINTEROPERABILITY-MIB", "fsDvmrpRouteInformation")
)
if mibBuilder.loadTexts:
    fsDvmrpRouteTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

fsDvmrpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 29, 2, 1, 1)
)
fsDvmrpMIBCompliance.setObjects(
      *(("FS-DVMRPINTEROPERABILITY-MIB", "fsDvmrpBaseMIBGroup"),
        ("FS-DVMRPINTEROPERABILITY-MIB", "fsDvmrpInterfaceMIBGroup"),
        ("FS-DVMRPINTEROPERABILITY-MIB", "fsDvmrpMetricOffsetMIBGroup"),
        ("FS-DVMRPINTEROPERABILITY-MIB", "fsDvmrpSummaryMIBGroup"),
        ("FS-DVMRPINTEROPERABILITY-MIB", "fsDvmrpMetricMIBGroup"),
        ("FS-DVMRPINTEROPERABILITY-MIB", "fsDvmrpRouteMIBGroup"),
        ("FS-DVMRPINTEROPERABILITY-MIB", "fsDvmrpRouteTrapGroup"))
)
if mibBuilder.loadTexts:
    fsDvmrpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-DVMRPINTEROPERABILITY-MIB",
    **{"fsDvmrpMIB": fsDvmrpMIB,
       "fsDvmrpMIBObjects": fsDvmrpMIBObjects,
       "fsDvmrpGroup": fsDvmrpGroup,
       "fsDvmrpRouteLimit": fsDvmrpRouteLimit,
       "fsDvmrpRoutehogNotification": fsDvmrpRoutehogNotification,
       "fsDvmrpInterfaceTable": fsDvmrpInterfaceTable,
       "fsDvmrpInterfaceEntry": fsDvmrpInterfaceEntry,
       "fsDvmrpInterfaceIfIndex": fsDvmrpInterfaceIfIndex,
       "fsDvmrpInterfaceDefaultInformation": fsDvmrpInterfaceDefaultInformation,
       "fsDvmrpInterfaceUnicastRoutingStatus": fsDvmrpInterfaceUnicastRoutingStatus,
       "fsDvmrpInterfaceRejectNonPrunersStatus": fsDvmrpInterfaceRejectNonPrunersStatus,
       "fsDvmrpInterfaceAutoSummaryStatus": fsDvmrpInterfaceAutoSummaryStatus,
       "fsDvmrpInterfaceRtsRec": fsDvmrpInterfaceRtsRec,
       "fsDvmrpInterfacePoisonReverseRtsRec": fsDvmrpInterfacePoisonReverseRtsRec,
       "fsDvmrpInterfaceUniRtAdvertised": fsDvmrpInterfaceUniRtAdvertised,
       "fsDvmrpInterfaceDvmrpRtAdvertised": fsDvmrpInterfaceDvmrpRtAdvertised,
       "fsDvmrpMetricOffsetTable": fsDvmrpMetricOffsetTable,
       "fsDvmrpMetricOffsetEntry": fsDvmrpMetricOffsetEntry,
       "fsDvmrpMetricOffsetIfIndex": fsDvmrpMetricOffsetIfIndex,
       "fsDvmrpMetricOffsetInOrOut": fsDvmrpMetricOffsetInOrOut,
       "fsDvmrpMetricOffsetIncrement": fsDvmrpMetricOffsetIncrement,
       "fsDvmrpSummaryTable": fsDvmrpSummaryTable,
       "fsDvmrpSummaryEntry": fsDvmrpSummaryEntry,
       "fsDvmrpIfIndex": fsDvmrpIfIndex,
       "fsDvmrpSummaryAddress": fsDvmrpSummaryAddress,
       "fsDvmrpSummaryMask": fsDvmrpSummaryMask,
       "fsDvmrpSummaryMetric": fsDvmrpSummaryMetric,
       "fsDvmrpSummaryStatus": fsDvmrpSummaryStatus,
       "fsDvmrpMetricTable": fsDvmrpMetricTable,
       "fsDvmrpMetricEntry": fsDvmrpMetricEntry,
       "fsDvmrpMetricIfIndex": fsDvmrpMetricIfIndex,
       "fsDvmrpMetric": fsDvmrpMetric,
       "fsDvmrpMetricListAclName": fsDvmrpMetricListAclName,
       "fsDvmrpMetricProtocolId": fsDvmrpMetricProtocolId,
       "fsDvmrpMetricStatus": fsDvmrpMetricStatus,
       "fsDvmrpRouteTable": fsDvmrpRouteTable,
       "fsDvmrpRouteEntry": fsDvmrpRouteEntry,
       "fsDvmrpRouteIpAddress": fsDvmrpRouteIpAddress,
       "fsDvmrpRouteInterface": fsDvmrpRouteInterface,
       "fsDvmrpRouteDistance": fsDvmrpRouteDistance,
       "fsDvmrpRouteMetric": fsDvmrpRouteMetric,
       "fsDvmrpRouteUptime": fsDvmrpRouteUptime,
       "fsDvmrpRouteExpires": fsDvmrpRouteExpires,
       "fsDvmrpRouteNextHopAddress": fsDvmrpRouteNextHopAddress,
       "fsDvmrpRouteNextHopInterface": fsDvmrpRouteNextHopInterface,
       "fsDvmrpRouteStatus": fsDvmrpRouteStatus,
       "fsDvmrpTraps": fsDvmrpTraps,
       "fsDvmrpRouteInformation": fsDvmrpRouteInformation,
       "fsDvmrpMIBConformance": fsDvmrpMIBConformance,
       "fsDvmrpMIBCompliances": fsDvmrpMIBCompliances,
       "fsDvmrpMIBCompliance": fsDvmrpMIBCompliance,
       "fsDvmrpMIBGroups": fsDvmrpMIBGroups,
       "fsDvmrpBaseMIBGroup": fsDvmrpBaseMIBGroup,
       "fsDvmrpInterfaceMIBGroup": fsDvmrpInterfaceMIBGroup,
       "fsDvmrpMetricOffsetMIBGroup": fsDvmrpMetricOffsetMIBGroup,
       "fsDvmrpSummaryMIBGroup": fsDvmrpSummaryMIBGroup,
       "fsDvmrpMetricMIBGroup": fsDvmrpMetricMIBGroup,
       "fsDvmrpRouteMIBGroup": fsDvmrpRouteMIBGroup,
       "fsDvmrpRouteTrapGroup": fsDvmrpRouteTrapGroup}
)
