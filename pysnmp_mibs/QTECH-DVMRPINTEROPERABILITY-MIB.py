# SNMP MIB module (QTECH-DVMRPINTEROPERABILITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-DVMRPINTEROPERABILITY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:29 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

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

qtechDvmrpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29)
)
if mibBuilder.loadTexts:
    qtechDvmrpMIB.setRevisions(
        ("2003-01-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechDvmrpMIBObjects_ObjectIdentity = ObjectIdentity
qtechDvmrpMIBObjects = _QtechDvmrpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1)
)
_QtechDvmrpGroup_ObjectIdentity = ObjectIdentity
qtechDvmrpGroup = _QtechDvmrpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1, 1)
)


class _QtechDvmrpRouteLimit_Type(Unsigned32):
    """Custom type qtechDvmrpRouteLimit based on Unsigned32"""
    defaultValue = 7000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_QtechDvmrpRouteLimit_Type.__name__ = "Unsigned32"
_QtechDvmrpRouteLimit_Object = MibScalar
qtechDvmrpRouteLimit = _QtechDvmrpRouteLimit_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1, 1, 1),
    _QtechDvmrpRouteLimit_Type()
)
qtechDvmrpRouteLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDvmrpRouteLimit.setStatus("current")


class _QtechDvmrpRoutehogNotification_Type(Unsigned32):
    """Custom type qtechDvmrpRoutehogNotification based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_QtechDvmrpRoutehogNotification_Type.__name__ = "Unsigned32"
_QtechDvmrpRoutehogNotification_Object = MibScalar
qtechDvmrpRoutehogNotification = _QtechDvmrpRoutehogNotification_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1, 1, 2),
    _QtechDvmrpRoutehogNotification_Type()
)
qtechDvmrpRoutehogNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDvmrpRoutehogNotification.setStatus("current")
_QtechDvmrpInterfaceTable_Object = MibTable
qtechDvmrpInterfaceTable = _QtechDvmrpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1, 2)
)
if mibBuilder.loadTexts:
    qtechDvmrpInterfaceTable.setStatus("current")
_QtechDvmrpInterfaceEntry_Object = MibTableRow
qtechDvmrpInterfaceEntry = _QtechDvmrpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1, 2, 1)
)
qtechDvmrpInterfaceEntry.setIndexNames(
    (0, "QTECH-DVMRPINTEROPERABILITY-MIB", "qtechDvmrpInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    qtechDvmrpInterfaceEntry.setStatus("current")
_QtechDvmrpInterfaceIfIndex_Type = InterfaceIndex
_QtechDvmrpInterfaceIfIndex_Object = MibTableColumn
qtechDvmrpInterfaceIfIndex = _QtechDvmrpInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1, 2, 1, 1),
    _QtechDvmrpInterfaceIfIndex_Type()
)
qtechDvmrpInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechDvmrpInterfaceIfIndex.setStatus("current")


class _QtechDvmrpInterfaceDefaultInformation_Type(Integer32):
    """Custom type qtechDvmrpInterfaceDefaultInformation based on Integer32"""
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


_QtechDvmrpInterfaceDefaultInformation_Type.__name__ = "Integer32"
_QtechDvmrpInterfaceDefaultInformation_Object = MibTableColumn
qtechDvmrpInterfaceDefaultInformation = _QtechDvmrpInterfaceDefaultInformation_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1, 2, 1, 2),
    _QtechDvmrpInterfaceDefaultInformation_Type()
)
qtechDvmrpInterfaceDefaultInformation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDvmrpInterfaceDefaultInformation.setStatus("current")


class _QtechDvmrpInterfaceUnicastRoutingStatus_Type(EnabledStatus):
    """Custom type qtechDvmrpInterfaceUnicastRoutingStatus based on EnabledStatus"""
    defaultValue = 2


_QtechDvmrpInterfaceUnicastRoutingStatus_Type.__name__ = "EnabledStatus"
_QtechDvmrpInterfaceUnicastRoutingStatus_Object = MibTableColumn
qtechDvmrpInterfaceUnicastRoutingStatus = _QtechDvmrpInterfaceUnicastRoutingStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1, 2, 1, 3),
    _QtechDvmrpInterfaceUnicastRoutingStatus_Type()
)
qtechDvmrpInterfaceUnicastRoutingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDvmrpInterfaceUnicastRoutingStatus.setStatus("current")


class _QtechDvmrpInterfaceRejectNonPrunersStatus_Type(EnabledStatus):
    """Custom type qtechDvmrpInterfaceRejectNonPrunersStatus based on EnabledStatus"""
    defaultValue = 2


_QtechDvmrpInterfaceRejectNonPrunersStatus_Type.__name__ = "EnabledStatus"
_QtechDvmrpInterfaceRejectNonPrunersStatus_Object = MibTableColumn
qtechDvmrpInterfaceRejectNonPrunersStatus = _QtechDvmrpInterfaceRejectNonPrunersStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1, 2, 1, 4),
    _QtechDvmrpInterfaceRejectNonPrunersStatus_Type()
)
qtechDvmrpInterfaceRejectNonPrunersStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDvmrpInterfaceRejectNonPrunersStatus.setStatus("current")


class _QtechDvmrpInterfaceAutoSummaryStatus_Type(EnabledStatus):
    """Custom type qtechDvmrpInterfaceAutoSummaryStatus based on EnabledStatus"""
    defaultValue = 1


_QtechDvmrpInterfaceAutoSummaryStatus_Type.__name__ = "EnabledStatus"
_QtechDvmrpInterfaceAutoSummaryStatus_Object = MibTableColumn
qtechDvmrpInterfaceAutoSummaryStatus = _QtechDvmrpInterfaceAutoSummaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1, 2, 1, 5),
    _QtechDvmrpInterfaceAutoSummaryStatus_Type()
)
qtechDvmrpInterfaceAutoSummaryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDvmrpInterfaceAutoSummaryStatus.setStatus("current")
_QtechDvmrpInterfaceRtsRec_Type = Integer32
_QtechDvmrpInterfaceRtsRec_Object = MibTableColumn
qtechDvmrpInterfaceRtsRec = _QtechDvmrpInterfaceRtsRec_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1, 2, 1, 6),
    _QtechDvmrpInterfaceRtsRec_Type()
)
qtechDvmrpInterfaceRtsRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDvmrpInterfaceRtsRec.setStatus("current")
_QtechDvmrpInterfacePoisonReverseRtsRec_Type = Integer32
_QtechDvmrpInterfacePoisonReverseRtsRec_Object = MibTableColumn
qtechDvmrpInterfacePoisonReverseRtsRec = _QtechDvmrpInterfacePoisonReverseRtsRec_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1, 2, 1, 7),
    _QtechDvmrpInterfacePoisonReverseRtsRec_Type()
)
qtechDvmrpInterfacePoisonReverseRtsRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDvmrpInterfacePoisonReverseRtsRec.setStatus("current")
_QtechDvmrpInterfaceUniRtAdvertised_Type = Integer32
_QtechDvmrpInterfaceUniRtAdvertised_Object = MibTableColumn
qtechDvmrpInterfaceUniRtAdvertised = _QtechDvmrpInterfaceUniRtAdvertised_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1, 2, 1, 8),
    _QtechDvmrpInterfaceUniRtAdvertised_Type()
)
qtechDvmrpInterfaceUniRtAdvertised.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDvmrpInterfaceUniRtAdvertised.setStatus("current")
_QtechDvmrpInterfaceDvmrpRtAdvertised_Type = Integer32
_QtechDvmrpInterfaceDvmrpRtAdvertised_Object = MibTableColumn
qtechDvmrpInterfaceDvmrpRtAdvertised = _QtechDvmrpInterfaceDvmrpRtAdvertised_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1, 2, 1, 9),
    _QtechDvmrpInterfaceDvmrpRtAdvertised_Type()
)
qtechDvmrpInterfaceDvmrpRtAdvertised.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDvmrpInterfaceDvmrpRtAdvertised.setStatus("current")
_QtechDvmrpMetricOffsetTable_Object = MibTable
qtechDvmrpMetricOffsetTable = _QtechDvmrpMetricOffsetTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1, 3)
)
if mibBuilder.loadTexts:
    qtechDvmrpMetricOffsetTable.setStatus("current")
_QtechDvmrpMetricOffsetEntry_Object = MibTableRow
qtechDvmrpMetricOffsetEntry = _QtechDvmrpMetricOffsetEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1, 3, 1)
)
qtechDvmrpMetricOffsetEntry.setIndexNames(
    (0, "QTECH-DVMRPINTEROPERABILITY-MIB", "qtechDvmrpMetricOffsetIfIndex"),
    (0, "QTECH-DVMRPINTEROPERABILITY-MIB", "qtechDvmrpMetricOffsetInOrOut"),
)
if mibBuilder.loadTexts:
    qtechDvmrpMetricOffsetEntry.setStatus("current")
_QtechDvmrpMetricOffsetIfIndex_Type = InterfaceIndex
_QtechDvmrpMetricOffsetIfIndex_Object = MibTableColumn
qtechDvmrpMetricOffsetIfIndex = _QtechDvmrpMetricOffsetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1, 3, 1, 1),
    _QtechDvmrpMetricOffsetIfIndex_Type()
)
qtechDvmrpMetricOffsetIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechDvmrpMetricOffsetIfIndex.setStatus("current")


class _QtechDvmrpMetricOffsetInOrOut_Type(Integer32):
    """Custom type qtechDvmrpMetricOffsetInOrOut based on Integer32"""
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


_QtechDvmrpMetricOffsetInOrOut_Type.__name__ = "Integer32"
_QtechDvmrpMetricOffsetInOrOut_Object = MibTableColumn
qtechDvmrpMetricOffsetInOrOut = _QtechDvmrpMetricOffsetInOrOut_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1, 3, 1, 2),
    _QtechDvmrpMetricOffsetInOrOut_Type()
)
qtechDvmrpMetricOffsetInOrOut.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechDvmrpMetricOffsetInOrOut.setStatus("current")


class _QtechDvmrpMetricOffsetIncrement_Type(Integer32):
    """Custom type qtechDvmrpMetricOffsetIncrement based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_QtechDvmrpMetricOffsetIncrement_Type.__name__ = "Integer32"
_QtechDvmrpMetricOffsetIncrement_Object = MibTableColumn
qtechDvmrpMetricOffsetIncrement = _QtechDvmrpMetricOffsetIncrement_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1, 3, 1, 3),
    _QtechDvmrpMetricOffsetIncrement_Type()
)
qtechDvmrpMetricOffsetIncrement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDvmrpMetricOffsetIncrement.setStatus("current")
_QtechDvmrpSummaryTable_Object = MibTable
qtechDvmrpSummaryTable = _QtechDvmrpSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1, 4)
)
if mibBuilder.loadTexts:
    qtechDvmrpSummaryTable.setStatus("current")
_QtechDvmrpSummaryEntry_Object = MibTableRow
qtechDvmrpSummaryEntry = _QtechDvmrpSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1, 4, 1)
)
qtechDvmrpSummaryEntry.setIndexNames(
    (0, "QTECH-DVMRPINTEROPERABILITY-MIB", "qtechDvmrpIfIndex"),
    (0, "QTECH-DVMRPINTEROPERABILITY-MIB", "qtechDvmrpSummaryAddress"),
    (0, "QTECH-DVMRPINTEROPERABILITY-MIB", "qtechDvmrpSummaryMask"),
)
if mibBuilder.loadTexts:
    qtechDvmrpSummaryEntry.setStatus("current")
_QtechDvmrpIfIndex_Type = InterfaceIndex
_QtechDvmrpIfIndex_Object = MibTableColumn
qtechDvmrpIfIndex = _QtechDvmrpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1, 4, 1, 1),
    _QtechDvmrpIfIndex_Type()
)
qtechDvmrpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechDvmrpIfIndex.setStatus("current")
_QtechDvmrpSummaryAddress_Type = IpAddress
_QtechDvmrpSummaryAddress_Object = MibTableColumn
qtechDvmrpSummaryAddress = _QtechDvmrpSummaryAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1, 4, 1, 2),
    _QtechDvmrpSummaryAddress_Type()
)
qtechDvmrpSummaryAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechDvmrpSummaryAddress.setStatus("current")
_QtechDvmrpSummaryMask_Type = IpAddress
_QtechDvmrpSummaryMask_Object = MibTableColumn
qtechDvmrpSummaryMask = _QtechDvmrpSummaryMask_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1, 4, 1, 3),
    _QtechDvmrpSummaryMask_Type()
)
qtechDvmrpSummaryMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechDvmrpSummaryMask.setStatus("current")


class _QtechDvmrpSummaryMetric_Type(Integer32):
    """Custom type qtechDvmrpSummaryMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_QtechDvmrpSummaryMetric_Type.__name__ = "Integer32"
_QtechDvmrpSummaryMetric_Object = MibTableColumn
qtechDvmrpSummaryMetric = _QtechDvmrpSummaryMetric_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1, 4, 1, 4),
    _QtechDvmrpSummaryMetric_Type()
)
qtechDvmrpSummaryMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechDvmrpSummaryMetric.setStatus("current")
_QtechDvmrpSummaryStatus_Type = RowStatus
_QtechDvmrpSummaryStatus_Object = MibTableColumn
qtechDvmrpSummaryStatus = _QtechDvmrpSummaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1, 4, 1, 5),
    _QtechDvmrpSummaryStatus_Type()
)
qtechDvmrpSummaryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechDvmrpSummaryStatus.setStatus("current")
_QtechDvmrpMetricTable_Object = MibTable
qtechDvmrpMetricTable = _QtechDvmrpMetricTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1, 5)
)
if mibBuilder.loadTexts:
    qtechDvmrpMetricTable.setStatus("current")
_QtechDvmrpMetricEntry_Object = MibTableRow
qtechDvmrpMetricEntry = _QtechDvmrpMetricEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1, 5, 1)
)
qtechDvmrpMetricEntry.setIndexNames(
    (0, "QTECH-DVMRPINTEROPERABILITY-MIB", "qtechDvmrpMetricIfIndex"),
    (0, "QTECH-DVMRPINTEROPERABILITY-MIB", "qtechDvmrpMetric"),
    (0, "QTECH-DVMRPINTEROPERABILITY-MIB", "qtechDvmrpMetricProtocolId"),
)
if mibBuilder.loadTexts:
    qtechDvmrpMetricEntry.setStatus("current")
_QtechDvmrpMetricIfIndex_Type = InterfaceIndex
_QtechDvmrpMetricIfIndex_Object = MibTableColumn
qtechDvmrpMetricIfIndex = _QtechDvmrpMetricIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1, 5, 1, 1),
    _QtechDvmrpMetricIfIndex_Type()
)
qtechDvmrpMetricIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechDvmrpMetricIfIndex.setStatus("current")


class _QtechDvmrpMetric_Type(Integer32):
    """Custom type qtechDvmrpMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_QtechDvmrpMetric_Type.__name__ = "Integer32"
_QtechDvmrpMetric_Object = MibTableColumn
qtechDvmrpMetric = _QtechDvmrpMetric_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1, 5, 1, 2),
    _QtechDvmrpMetric_Type()
)
qtechDvmrpMetric.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechDvmrpMetric.setStatus("current")
_QtechDvmrpMetricListAclName_Type = DisplayString
_QtechDvmrpMetricListAclName_Object = MibTableColumn
qtechDvmrpMetricListAclName = _QtechDvmrpMetricListAclName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1, 5, 1, 3),
    _QtechDvmrpMetricListAclName_Type()
)
qtechDvmrpMetricListAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechDvmrpMetricListAclName.setStatus("current")


class _QtechDvmrpMetricProtocolId_Type(Integer32):
    """Custom type qtechDvmrpMetricProtocolId based on Integer32"""
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


_QtechDvmrpMetricProtocolId_Type.__name__ = "Integer32"
_QtechDvmrpMetricProtocolId_Object = MibTableColumn
qtechDvmrpMetricProtocolId = _QtechDvmrpMetricProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1, 5, 1, 4),
    _QtechDvmrpMetricProtocolId_Type()
)
qtechDvmrpMetricProtocolId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechDvmrpMetricProtocolId.setStatus("current")
_QtechDvmrpMetricStatus_Type = RowStatus
_QtechDvmrpMetricStatus_Object = MibTableColumn
qtechDvmrpMetricStatus = _QtechDvmrpMetricStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1, 5, 1, 5),
    _QtechDvmrpMetricStatus_Type()
)
qtechDvmrpMetricStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechDvmrpMetricStatus.setStatus("current")
_QtechDvmrpRouteTable_Object = MibTable
qtechDvmrpRouteTable = _QtechDvmrpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1, 6)
)
if mibBuilder.loadTexts:
    qtechDvmrpRouteTable.setStatus("current")
_QtechDvmrpRouteEntry_Object = MibTableRow
qtechDvmrpRouteEntry = _QtechDvmrpRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1, 6, 1)
)
qtechDvmrpRouteEntry.setIndexNames(
    (0, "QTECH-DVMRPINTEROPERABILITY-MIB", "qtechDvmrpRouteIpAddress"),
    (0, "QTECH-DVMRPINTEROPERABILITY-MIB", "qtechDvmrpRouteInterface"),
)
if mibBuilder.loadTexts:
    qtechDvmrpRouteEntry.setStatus("current")
_QtechDvmrpRouteIpAddress_Type = IpAddress
_QtechDvmrpRouteIpAddress_Object = MibTableColumn
qtechDvmrpRouteIpAddress = _QtechDvmrpRouteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1, 6, 1, 1),
    _QtechDvmrpRouteIpAddress_Type()
)
qtechDvmrpRouteIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechDvmrpRouteIpAddress.setStatus("current")
_QtechDvmrpRouteInterface_Type = InterfaceIndex
_QtechDvmrpRouteInterface_Object = MibTableColumn
qtechDvmrpRouteInterface = _QtechDvmrpRouteInterface_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1, 6, 1, 2),
    _QtechDvmrpRouteInterface_Type()
)
qtechDvmrpRouteInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechDvmrpRouteInterface.setStatus("current")
_QtechDvmrpRouteDistance_Type = Integer32
_QtechDvmrpRouteDistance_Object = MibTableColumn
qtechDvmrpRouteDistance = _QtechDvmrpRouteDistance_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1, 6, 1, 3),
    _QtechDvmrpRouteDistance_Type()
)
qtechDvmrpRouteDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDvmrpRouteDistance.setStatus("current")
_QtechDvmrpRouteMetric_Type = Integer32
_QtechDvmrpRouteMetric_Object = MibTableColumn
qtechDvmrpRouteMetric = _QtechDvmrpRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1, 6, 1, 4),
    _QtechDvmrpRouteMetric_Type()
)
qtechDvmrpRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDvmrpRouteMetric.setStatus("current")
_QtechDvmrpRouteUptime_Type = TimeTicks
_QtechDvmrpRouteUptime_Object = MibTableColumn
qtechDvmrpRouteUptime = _QtechDvmrpRouteUptime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1, 6, 1, 5),
    _QtechDvmrpRouteUptime_Type()
)
qtechDvmrpRouteUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDvmrpRouteUptime.setStatus("current")
_QtechDvmrpRouteExpires_Type = TimeTicks
_QtechDvmrpRouteExpires_Object = MibTableColumn
qtechDvmrpRouteExpires = _QtechDvmrpRouteExpires_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1, 6, 1, 6),
    _QtechDvmrpRouteExpires_Type()
)
qtechDvmrpRouteExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDvmrpRouteExpires.setStatus("current")
_QtechDvmrpRouteNextHopAddress_Type = IpAddress
_QtechDvmrpRouteNextHopAddress_Object = MibTableColumn
qtechDvmrpRouteNextHopAddress = _QtechDvmrpRouteNextHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1, 6, 1, 7),
    _QtechDvmrpRouteNextHopAddress_Type()
)
qtechDvmrpRouteNextHopAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDvmrpRouteNextHopAddress.setStatus("current")
_QtechDvmrpRouteNextHopInterface_Type = InterfaceIndex
_QtechDvmrpRouteNextHopInterface_Object = MibTableColumn
qtechDvmrpRouteNextHopInterface = _QtechDvmrpRouteNextHopInterface_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1, 6, 1, 8),
    _QtechDvmrpRouteNextHopInterface_Type()
)
qtechDvmrpRouteNextHopInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDvmrpRouteNextHopInterface.setStatus("current")
_QtechDvmrpRouteStatus_Type = EnabledStatus
_QtechDvmrpRouteStatus_Object = MibTableColumn
qtechDvmrpRouteStatus = _QtechDvmrpRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1, 6, 1, 9),
    _QtechDvmrpRouteStatus_Type()
)
qtechDvmrpRouteStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDvmrpRouteStatus.setStatus("current")
_QtechDvmrpTraps_ObjectIdentity = ObjectIdentity
qtechDvmrpTraps = _QtechDvmrpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1, 7)
)
_QtechDvmrpMIBConformance_ObjectIdentity = ObjectIdentity
qtechDvmrpMIBConformance = _QtechDvmrpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 2)
)
_QtechDvmrpMIBCompliances_ObjectIdentity = ObjectIdentity
qtechDvmrpMIBCompliances = _QtechDvmrpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 2, 1)
)
_QtechDvmrpMIBGroups_ObjectIdentity = ObjectIdentity
qtechDvmrpMIBGroups = _QtechDvmrpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 2, 2)
)

# Managed Objects groups

qtechDvmrpBaseMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 2, 2, 1)
)
qtechDvmrpBaseMIBGroup.setObjects(
      *(("QTECH-DVMRPINTEROPERABILITY-MIB", "qtechDvmrpRouteLimit"),
        ("QTECH-DVMRPINTEROPERABILITY-MIB", "qtechDvmrpRoutehogNotification"))
)
if mibBuilder.loadTexts:
    qtechDvmrpBaseMIBGroup.setStatus("current")

qtechDvmrpInterfaceMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 2, 2, 2)
)
qtechDvmrpInterfaceMIBGroup.setObjects(
      *(("QTECH-DVMRPINTEROPERABILITY-MIB", "qtechDvmrpInterfaceDefaultInformation"),
        ("QTECH-DVMRPINTEROPERABILITY-MIB", "qtechDvmrpInterfaceUnicastRoutingStatus"),
        ("QTECH-DVMRPINTEROPERABILITY-MIB", "qtechDvmrpInterfaceRejectNonPrunersStatus"),
        ("QTECH-DVMRPINTEROPERABILITY-MIB", "qtechDvmrpInterfaceAutoSummaryStatus"),
        ("QTECH-DVMRPINTEROPERABILITY-MIB", "qtechDvmrpInterfaceRtsRec"),
        ("QTECH-DVMRPINTEROPERABILITY-MIB", "qtechDvmrpInterfacePoisonReverseRtsRec"),
        ("QTECH-DVMRPINTEROPERABILITY-MIB", "qtechDvmrpInterfaceUniRtAdvertised"),
        ("QTECH-DVMRPINTEROPERABILITY-MIB", "qtechDvmrpInterfaceDvmrpRtAdvertised"))
)
if mibBuilder.loadTexts:
    qtechDvmrpInterfaceMIBGroup.setStatus("current")

qtechDvmrpMetricOffsetMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 2, 2, 3)
)
qtechDvmrpMetricOffsetMIBGroup.setObjects(
    ("QTECH-DVMRPINTEROPERABILITY-MIB", "qtechDvmrpMetricOffsetIncrement")
)
if mibBuilder.loadTexts:
    qtechDvmrpMetricOffsetMIBGroup.setStatus("current")

qtechDvmrpSummaryMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 2, 2, 4)
)
qtechDvmrpSummaryMIBGroup.setObjects(
      *(("QTECH-DVMRPINTEROPERABILITY-MIB", "qtechDvmrpSummaryMetric"),
        ("QTECH-DVMRPINTEROPERABILITY-MIB", "qtechDvmrpSummaryStatus"))
)
if mibBuilder.loadTexts:
    qtechDvmrpSummaryMIBGroup.setStatus("current")

qtechDvmrpMetricMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 2, 2, 5)
)
qtechDvmrpMetricMIBGroup.setObjects(
      *(("QTECH-DVMRPINTEROPERABILITY-MIB", "qtechDvmrpMetricListAclName"),
        ("QTECH-DVMRPINTEROPERABILITY-MIB", "qtechDvmrpMetricStatus"))
)
if mibBuilder.loadTexts:
    qtechDvmrpMetricMIBGroup.setStatus("current")

qtechDvmrpRouteMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 2, 2, 6)
)
qtechDvmrpRouteMIBGroup.setObjects(
      *(("QTECH-DVMRPINTEROPERABILITY-MIB", "qtechDvmrpRouteDistance"),
        ("QTECH-DVMRPINTEROPERABILITY-MIB", "qtechDvmrpRouteMetric"),
        ("QTECH-DVMRPINTEROPERABILITY-MIB", "qtechDvmrpRouteUptime"),
        ("QTECH-DVMRPINTEROPERABILITY-MIB", "qtechDvmrpRouteExpires"),
        ("QTECH-DVMRPINTEROPERABILITY-MIB", "qtechDvmrpRouteNextHopAddress"),
        ("QTECH-DVMRPINTEROPERABILITY-MIB", "qtechDvmrpRouteNextHopInterface"),
        ("QTECH-DVMRPINTEROPERABILITY-MIB", "qtechDvmrpRouteStatus"))
)
if mibBuilder.loadTexts:
    qtechDvmrpRouteMIBGroup.setStatus("current")


# Notification objects

qtechDvmrpRouteInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 1, 7, 1)
)
if mibBuilder.loadTexts:
    qtechDvmrpRouteInformation.setStatus(
        "current"
    )


# Notifications groups

qtechDvmrpRouteTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 2, 2, 7)
)
qtechDvmrpRouteTrapGroup.setObjects(
    ("QTECH-DVMRPINTEROPERABILITY-MIB", "qtechDvmrpRouteInformation")
)
if mibBuilder.loadTexts:
    qtechDvmrpRouteTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

qtechDvmrpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 29, 2, 1, 1)
)
qtechDvmrpMIBCompliance.setObjects(
      *(("QTECH-DVMRPINTEROPERABILITY-MIB", "qtechDvmrpBaseMIBGroup"),
        ("QTECH-DVMRPINTEROPERABILITY-MIB", "qtechDvmrpInterfaceMIBGroup"),
        ("QTECH-DVMRPINTEROPERABILITY-MIB", "qtechDvmrpMetricOffsetMIBGroup"),
        ("QTECH-DVMRPINTEROPERABILITY-MIB", "qtechDvmrpSummaryMIBGroup"),
        ("QTECH-DVMRPINTEROPERABILITY-MIB", "qtechDvmrpMetricMIBGroup"),
        ("QTECH-DVMRPINTEROPERABILITY-MIB", "qtechDvmrpRouteMIBGroup"),
        ("QTECH-DVMRPINTEROPERABILITY-MIB", "qtechDvmrpRouteTrapGroup"))
)
if mibBuilder.loadTexts:
    qtechDvmrpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-DVMRPINTEROPERABILITY-MIB",
    **{"qtechDvmrpMIB": qtechDvmrpMIB,
       "qtechDvmrpMIBObjects": qtechDvmrpMIBObjects,
       "qtechDvmrpGroup": qtechDvmrpGroup,
       "qtechDvmrpRouteLimit": qtechDvmrpRouteLimit,
       "qtechDvmrpRoutehogNotification": qtechDvmrpRoutehogNotification,
       "qtechDvmrpInterfaceTable": qtechDvmrpInterfaceTable,
       "qtechDvmrpInterfaceEntry": qtechDvmrpInterfaceEntry,
       "qtechDvmrpInterfaceIfIndex": qtechDvmrpInterfaceIfIndex,
       "qtechDvmrpInterfaceDefaultInformation": qtechDvmrpInterfaceDefaultInformation,
       "qtechDvmrpInterfaceUnicastRoutingStatus": qtechDvmrpInterfaceUnicastRoutingStatus,
       "qtechDvmrpInterfaceRejectNonPrunersStatus": qtechDvmrpInterfaceRejectNonPrunersStatus,
       "qtechDvmrpInterfaceAutoSummaryStatus": qtechDvmrpInterfaceAutoSummaryStatus,
       "qtechDvmrpInterfaceRtsRec": qtechDvmrpInterfaceRtsRec,
       "qtechDvmrpInterfacePoisonReverseRtsRec": qtechDvmrpInterfacePoisonReverseRtsRec,
       "qtechDvmrpInterfaceUniRtAdvertised": qtechDvmrpInterfaceUniRtAdvertised,
       "qtechDvmrpInterfaceDvmrpRtAdvertised": qtechDvmrpInterfaceDvmrpRtAdvertised,
       "qtechDvmrpMetricOffsetTable": qtechDvmrpMetricOffsetTable,
       "qtechDvmrpMetricOffsetEntry": qtechDvmrpMetricOffsetEntry,
       "qtechDvmrpMetricOffsetIfIndex": qtechDvmrpMetricOffsetIfIndex,
       "qtechDvmrpMetricOffsetInOrOut": qtechDvmrpMetricOffsetInOrOut,
       "qtechDvmrpMetricOffsetIncrement": qtechDvmrpMetricOffsetIncrement,
       "qtechDvmrpSummaryTable": qtechDvmrpSummaryTable,
       "qtechDvmrpSummaryEntry": qtechDvmrpSummaryEntry,
       "qtechDvmrpIfIndex": qtechDvmrpIfIndex,
       "qtechDvmrpSummaryAddress": qtechDvmrpSummaryAddress,
       "qtechDvmrpSummaryMask": qtechDvmrpSummaryMask,
       "qtechDvmrpSummaryMetric": qtechDvmrpSummaryMetric,
       "qtechDvmrpSummaryStatus": qtechDvmrpSummaryStatus,
       "qtechDvmrpMetricTable": qtechDvmrpMetricTable,
       "qtechDvmrpMetricEntry": qtechDvmrpMetricEntry,
       "qtechDvmrpMetricIfIndex": qtechDvmrpMetricIfIndex,
       "qtechDvmrpMetric": qtechDvmrpMetric,
       "qtechDvmrpMetricListAclName": qtechDvmrpMetricListAclName,
       "qtechDvmrpMetricProtocolId": qtechDvmrpMetricProtocolId,
       "qtechDvmrpMetricStatus": qtechDvmrpMetricStatus,
       "qtechDvmrpRouteTable": qtechDvmrpRouteTable,
       "qtechDvmrpRouteEntry": qtechDvmrpRouteEntry,
       "qtechDvmrpRouteIpAddress": qtechDvmrpRouteIpAddress,
       "qtechDvmrpRouteInterface": qtechDvmrpRouteInterface,
       "qtechDvmrpRouteDistance": qtechDvmrpRouteDistance,
       "qtechDvmrpRouteMetric": qtechDvmrpRouteMetric,
       "qtechDvmrpRouteUptime": qtechDvmrpRouteUptime,
       "qtechDvmrpRouteExpires": qtechDvmrpRouteExpires,
       "qtechDvmrpRouteNextHopAddress": qtechDvmrpRouteNextHopAddress,
       "qtechDvmrpRouteNextHopInterface": qtechDvmrpRouteNextHopInterface,
       "qtechDvmrpRouteStatus": qtechDvmrpRouteStatus,
       "qtechDvmrpTraps": qtechDvmrpTraps,
       "qtechDvmrpRouteInformation": qtechDvmrpRouteInformation,
       "qtechDvmrpMIBConformance": qtechDvmrpMIBConformance,
       "qtechDvmrpMIBCompliances": qtechDvmrpMIBCompliances,
       "qtechDvmrpMIBCompliance": qtechDvmrpMIBCompliance,
       "qtechDvmrpMIBGroups": qtechDvmrpMIBGroups,
       "qtechDvmrpBaseMIBGroup": qtechDvmrpBaseMIBGroup,
       "qtechDvmrpInterfaceMIBGroup": qtechDvmrpInterfaceMIBGroup,
       "qtechDvmrpMetricOffsetMIBGroup": qtechDvmrpMetricOffsetMIBGroup,
       "qtechDvmrpSummaryMIBGroup": qtechDvmrpSummaryMIBGroup,
       "qtechDvmrpMetricMIBGroup": qtechDvmrpMetricMIBGroup,
       "qtechDvmrpRouteMIBGroup": qtechDvmrpRouteMIBGroup,
       "qtechDvmrpRouteTrapGroup": qtechDvmrpRouteTrapGroup}
)
