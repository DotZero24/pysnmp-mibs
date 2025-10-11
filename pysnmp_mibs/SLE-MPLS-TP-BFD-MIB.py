# SNMP MIB module (SLE-MPLS-TP-BFD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/dasan/SLE-MPLS-TP-BFD-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:11:08 2025
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

(sleMgmt,) = mibBuilder.importSymbols(
    "DASAN-SMI",
    "sleMgmt")

(IANAbfdDiagTC,) = mibBuilder.importSymbols(
    "IANA-BFD-TC-STD-MIB",
    "IANAbfdDiagTC")

(SleControlRequestResultType,
 SleControlStatusType) = mibBuilder.importSymbols(
    "SLE-TC-MIB",
    "SleControlRequestResultType",
    "SleControlStatusType")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

sleMplsTpBfd = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 19)
)
if mibBuilder.loadTexts:
    sleMplsTpBfd.setRevisions(
        ("2004-06-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SleMpls_ObjectIdentity = ObjectIdentity
sleMpls = _SleMpls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16)
)
if mibBuilder.loadTexts:
    sleMpls.setStatus("current")
_SleMplsTpBfdCfg_ObjectIdentity = ObjectIdentity
sleMplsTpBfdCfg = _SleMplsTpBfdCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 19, 1)
)
_SleMplsTpBfdCfgInfoTable_Object = MibTable
sleMplsTpBfdCfgInfoTable = _SleMplsTpBfdCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 19, 1, 1)
)
if mibBuilder.loadTexts:
    sleMplsTpBfdCfgInfoTable.setStatus("current")
_SleMplsTpBfdCfgInfoEntry_Object = MibTableRow
sleMplsTpBfdCfgInfoEntry = _SleMplsTpBfdCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 19, 1, 1, 1)
)
sleMplsTpBfdCfgInfoEntry.setIndexNames(
    (0, "SLE-MPLS-TP-BFD-MIB", "sleMplsTpBfdCfgInfoMegIndex"),
    (0, "SLE-MPLS-TP-BFD-MIB", "sleMplsTpBfdCfgInfoMeIndex"),
)
if mibBuilder.loadTexts:
    sleMplsTpBfdCfgInfoEntry.setStatus("current")


class _SleMplsTpBfdCfgInfoMegIndex_Type(Unsigned32):
    """Custom type sleMplsTpBfdCfgInfoMegIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleMplsTpBfdCfgInfoMegIndex_Type.__name__ = "Unsigned32"
_SleMplsTpBfdCfgInfoMegIndex_Object = MibTableColumn
sleMplsTpBfdCfgInfoMegIndex = _SleMplsTpBfdCfgInfoMegIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 19, 1, 1, 1, 1),
    _SleMplsTpBfdCfgInfoMegIndex_Type()
)
sleMplsTpBfdCfgInfoMegIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sleMplsTpBfdCfgInfoMegIndex.setStatus("current")


class _SleMplsTpBfdCfgInfoMeIndex_Type(Unsigned32):
    """Custom type sleMplsTpBfdCfgInfoMeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleMplsTpBfdCfgInfoMeIndex_Type.__name__ = "Unsigned32"
_SleMplsTpBfdCfgInfoMeIndex_Object = MibTableColumn
sleMplsTpBfdCfgInfoMeIndex = _SleMplsTpBfdCfgInfoMeIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 19, 1, 1, 1, 2),
    _SleMplsTpBfdCfgInfoMeIndex_Type()
)
sleMplsTpBfdCfgInfoMeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sleMplsTpBfdCfgInfoMeIndex.setStatus("current")
_SleMplsTpBfdCfgInfoMegName_Type = OctetString
_SleMplsTpBfdCfgInfoMegName_Object = MibTableColumn
sleMplsTpBfdCfgInfoMegName = _SleMplsTpBfdCfgInfoMegName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 19, 1, 1, 1, 3),
    _SleMplsTpBfdCfgInfoMegName_Type()
)
sleMplsTpBfdCfgInfoMegName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpBfdCfgInfoMegName.setStatus("current")
_SleMplsTpBfdCfgInfoMeName_Type = OctetString
_SleMplsTpBfdCfgInfoMeName_Object = MibTableColumn
sleMplsTpBfdCfgInfoMeName = _SleMplsTpBfdCfgInfoMeName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 19, 1, 1, 1, 4),
    _SleMplsTpBfdCfgInfoMeName_Type()
)
sleMplsTpBfdCfgInfoMeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpBfdCfgInfoMeName.setStatus("current")
_SleMplsTpBfdCfgInfoTxInterval_Type = OctetString
_SleMplsTpBfdCfgInfoTxInterval_Object = MibTableColumn
sleMplsTpBfdCfgInfoTxInterval = _SleMplsTpBfdCfgInfoTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 19, 1, 1, 1, 5),
    _SleMplsTpBfdCfgInfoTxInterval_Type()
)
sleMplsTpBfdCfgInfoTxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpBfdCfgInfoTxInterval.setStatus("current")
_SleMplsTpBfdCfgInfoRXInterval_Type = OctetString
_SleMplsTpBfdCfgInfoRXInterval_Object = MibTableColumn
sleMplsTpBfdCfgInfoRXInterval = _SleMplsTpBfdCfgInfoRXInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 19, 1, 1, 1, 6),
    _SleMplsTpBfdCfgInfoRXInterval_Type()
)
sleMplsTpBfdCfgInfoRXInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpBfdCfgInfoRXInterval.setStatus("current")
_SleMplsTpBfdCfgControl_ObjectIdentity = ObjectIdentity
sleMplsTpBfdCfgControl = _SleMplsTpBfdCfgControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 19, 1, 2)
)


class _SleMplsTpBfdCfgControlRequest_Type(Integer32):
    """Custom type sleMplsTpBfdCfgControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createBfdcfgEntry", 1),
          ("deleteBfdCfgEntry", 2),
          ("setIntervals", 3))
    )


_SleMplsTpBfdCfgControlRequest_Type.__name__ = "Integer32"
_SleMplsTpBfdCfgControlRequest_Object = MibScalar
sleMplsTpBfdCfgControlRequest = _SleMplsTpBfdCfgControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 19, 1, 2, 1),
    _SleMplsTpBfdCfgControlRequest_Type()
)
sleMplsTpBfdCfgControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpBfdCfgControlRequest.setStatus("current")
_SleMplsTpBfdCfgControlStatus_Type = SleControlStatusType
_SleMplsTpBfdCfgControlStatus_Object = MibScalar
sleMplsTpBfdCfgControlStatus = _SleMplsTpBfdCfgControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 19, 1, 2, 2),
    _SleMplsTpBfdCfgControlStatus_Type()
)
sleMplsTpBfdCfgControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpBfdCfgControlStatus.setStatus("current")
_SleMplsTpBfdCfgControlTimer_Type = Gauge32
_SleMplsTpBfdCfgControlTimer_Object = MibScalar
sleMplsTpBfdCfgControlTimer = _SleMplsTpBfdCfgControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 19, 1, 2, 3),
    _SleMplsTpBfdCfgControlTimer_Type()
)
sleMplsTpBfdCfgControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpBfdCfgControlTimer.setStatus("current")
_SleMplsTpBfdCfgControlTimestamp_Type = TimeTicks
_SleMplsTpBfdCfgControlTimestamp_Object = MibScalar
sleMplsTpBfdCfgControlTimestamp = _SleMplsTpBfdCfgControlTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 19, 1, 2, 4),
    _SleMplsTpBfdCfgControlTimestamp_Type()
)
sleMplsTpBfdCfgControlTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpBfdCfgControlTimestamp.setStatus("current")
_SleMplsTpBfdCfgControlReqResult_Type = SleControlRequestResultType
_SleMplsTpBfdCfgControlReqResult_Object = MibScalar
sleMplsTpBfdCfgControlReqResult = _SleMplsTpBfdCfgControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 19, 1, 2, 5),
    _SleMplsTpBfdCfgControlReqResult_Type()
)
sleMplsTpBfdCfgControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpBfdCfgControlReqResult.setStatus("current")
_SleMplsTpBfdCfgControlMegName_Type = OctetString
_SleMplsTpBfdCfgControlMegName_Object = MibScalar
sleMplsTpBfdCfgControlMegName = _SleMplsTpBfdCfgControlMegName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 19, 1, 2, 6),
    _SleMplsTpBfdCfgControlMegName_Type()
)
sleMplsTpBfdCfgControlMegName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sleMplsTpBfdCfgControlMegName.setStatus("current")
_SleMplsTpBfdCfgControlMeName_Type = OctetString
_SleMplsTpBfdCfgControlMeName_Object = MibScalar
sleMplsTpBfdCfgControlMeName = _SleMplsTpBfdCfgControlMeName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 19, 1, 2, 7),
    _SleMplsTpBfdCfgControlMeName_Type()
)
sleMplsTpBfdCfgControlMeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpBfdCfgControlMeName.setStatus("current")
_SleMplsTpBfdCfgControlTxInterval_Type = OctetString
_SleMplsTpBfdCfgControlTxInterval_Object = MibScalar
sleMplsTpBfdCfgControlTxInterval = _SleMplsTpBfdCfgControlTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 19, 1, 2, 8),
    _SleMplsTpBfdCfgControlTxInterval_Type()
)
sleMplsTpBfdCfgControlTxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpBfdCfgControlTxInterval.setStatus("current")
_SleMplsTpBfdCfgControlRXInterval_Type = OctetString
_SleMplsTpBfdCfgControlRXInterval_Object = MibScalar
sleMplsTpBfdCfgControlRXInterval = _SleMplsTpBfdCfgControlRXInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 19, 1, 2, 9),
    _SleMplsTpBfdCfgControlRXInterval_Type()
)
sleMplsTpBfdCfgControlRXInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpBfdCfgControlRXInterval.setStatus("current")
_SleMplsTpBfdSession_ObjectIdentity = ObjectIdentity
sleMplsTpBfdSession = _SleMplsTpBfdSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 19, 2)
)
_SleMplsTpBfdSessionInfoTable_Object = MibTable
sleMplsTpBfdSessionInfoTable = _SleMplsTpBfdSessionInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 19, 2, 1)
)
if mibBuilder.loadTexts:
    sleMplsTpBfdSessionInfoTable.setStatus("current")
_SleMplsTpBfdSessionInfoEntry_Object = MibTableRow
sleMplsTpBfdSessionInfoEntry = _SleMplsTpBfdSessionInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 19, 2, 1, 1)
)
sleMplsTpBfdSessionInfoEntry.setIndexNames(
    (0, "SLE-MPLS-TP-BFD-MIB", "sleMplsTpBfdSessionInfoSessIndex"),
)
if mibBuilder.loadTexts:
    sleMplsTpBfdSessionInfoEntry.setStatus("current")


class _SleMplsTpBfdSessionInfoSessIndex_Type(Unsigned32):
    """Custom type sleMplsTpBfdSessionInfoSessIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleMplsTpBfdSessionInfoSessIndex_Type.__name__ = "Unsigned32"
_SleMplsTpBfdSessionInfoSessIndex_Object = MibTableColumn
sleMplsTpBfdSessionInfoSessIndex = _SleMplsTpBfdSessionInfoSessIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 19, 2, 1, 1, 1),
    _SleMplsTpBfdSessionInfoSessIndex_Type()
)
sleMplsTpBfdSessionInfoSessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sleMplsTpBfdSessionInfoSessIndex.setStatus("current")
_SleMplsTpBfdSessionInfoMegName_Type = OctetString
_SleMplsTpBfdSessionInfoMegName_Object = MibTableColumn
sleMplsTpBfdSessionInfoMegName = _SleMplsTpBfdSessionInfoMegName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 19, 2, 1, 1, 2),
    _SleMplsTpBfdSessionInfoMegName_Type()
)
sleMplsTpBfdSessionInfoMegName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpBfdSessionInfoMegName.setStatus("current")
_SleMplsTpBfdSessionInfoMeName_Type = OctetString
_SleMplsTpBfdSessionInfoMeName_Object = MibTableColumn
sleMplsTpBfdSessionInfoMeName = _SleMplsTpBfdSessionInfoMeName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 19, 2, 1, 1, 3),
    _SleMplsTpBfdSessionInfoMeName_Type()
)
sleMplsTpBfdSessionInfoMeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpBfdSessionInfoMeName.setStatus("current")


class _SleMplsTpBfdSessionInfoVersionNumber_Type(Unsigned32):
    """Custom type sleMplsTpBfdSessionInfoVersionNumber based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SleMplsTpBfdSessionInfoVersionNumber_Type.__name__ = "Unsigned32"
_SleMplsTpBfdSessionInfoVersionNumber_Object = MibTableColumn
sleMplsTpBfdSessionInfoVersionNumber = _SleMplsTpBfdSessionInfoVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 19, 2, 1, 1, 4),
    _SleMplsTpBfdSessionInfoVersionNumber_Type()
)
sleMplsTpBfdSessionInfoVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpBfdSessionInfoVersionNumber.setStatus("current")


class _SleMplsTpBfdSessionInfoDiscriminator_Type(Unsigned32):
    """Custom type sleMplsTpBfdSessionInfoDiscriminator based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SleMplsTpBfdSessionInfoDiscriminator_Type.__name__ = "Unsigned32"
_SleMplsTpBfdSessionInfoDiscriminator_Object = MibTableColumn
sleMplsTpBfdSessionInfoDiscriminator = _SleMplsTpBfdSessionInfoDiscriminator_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 19, 2, 1, 1, 5),
    _SleMplsTpBfdSessionInfoDiscriminator_Type()
)
sleMplsTpBfdSessionInfoDiscriminator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpBfdSessionInfoDiscriminator.setStatus("current")


class _SleMplsTpBfdSessionInfoRemoteDiscriminator_Type(Unsigned32):
    """Custom type sleMplsTpBfdSessionInfoRemoteDiscriminator based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_SleMplsTpBfdSessionInfoRemoteDiscriminator_Type.__name__ = "Unsigned32"
_SleMplsTpBfdSessionInfoRemoteDiscriminator_Object = MibTableColumn
sleMplsTpBfdSessionInfoRemoteDiscriminator = _SleMplsTpBfdSessionInfoRemoteDiscriminator_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 19, 2, 1, 1, 6),
    _SleMplsTpBfdSessionInfoRemoteDiscriminator_Type()
)
sleMplsTpBfdSessionInfoRemoteDiscriminator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpBfdSessionInfoRemoteDiscriminator.setStatus("current")


class _SleMplsTpBfdSessionInfoState_Type(Integer32):
    """Custom type sleMplsTpBfdSessionInfoState based on Integer32"""
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
        *(("adminDown", 0),
          ("stateDown", 1),
          ("stateInit", 2),
          ("stateUp", 3),
          ("unknown", 4))
    )


_SleMplsTpBfdSessionInfoState_Type.__name__ = "Integer32"
_SleMplsTpBfdSessionInfoState_Object = MibTableColumn
sleMplsTpBfdSessionInfoState = _SleMplsTpBfdSessionInfoState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 19, 2, 1, 1, 7),
    _SleMplsTpBfdSessionInfoState_Type()
)
sleMplsTpBfdSessionInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpBfdSessionInfoState.setStatus("current")
_SleMplsTpBfdSessionInfoDiag_Type = IANAbfdDiagTC
_SleMplsTpBfdSessionInfoDiag_Object = MibTableColumn
sleMplsTpBfdSessionInfoDiag = _SleMplsTpBfdSessionInfoDiag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 19, 2, 1, 1, 8),
    _SleMplsTpBfdSessionInfoDiag_Type()
)
sleMplsTpBfdSessionInfoDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpBfdSessionInfoDiag.setStatus("current")
_SleMplsTpBfdSessionInfoDesiredMinTxInterval_Type = OctetString
_SleMplsTpBfdSessionInfoDesiredMinTxInterval_Object = MibTableColumn
sleMplsTpBfdSessionInfoDesiredMinTxInterval = _SleMplsTpBfdSessionInfoDesiredMinTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 19, 2, 1, 1, 9),
    _SleMplsTpBfdSessionInfoDesiredMinTxInterval_Type()
)
sleMplsTpBfdSessionInfoDesiredMinTxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpBfdSessionInfoDesiredMinTxInterval.setStatus("current")
_SleMplsTpBfdSessionInfoReqMinRxInterval_Type = OctetString
_SleMplsTpBfdSessionInfoReqMinRxInterval_Object = MibTableColumn
sleMplsTpBfdSessionInfoReqMinRxInterval = _SleMplsTpBfdSessionInfoReqMinRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 19, 2, 1, 1, 10),
    _SleMplsTpBfdSessionInfoReqMinRxInterval_Type()
)
sleMplsTpBfdSessionInfoReqMinRxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpBfdSessionInfoReqMinRxInterval.setStatus("current")
_SleMplsTpBfdSessionInfoDetectMult_Type = Unsigned32
_SleMplsTpBfdSessionInfoDetectMult_Object = MibTableColumn
sleMplsTpBfdSessionInfoDetectMult = _SleMplsTpBfdSessionInfoDetectMult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 19, 2, 1, 1, 11),
    _SleMplsTpBfdSessionInfoDetectMult_Type()
)
sleMplsTpBfdSessionInfoDetectMult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpBfdSessionInfoDetectMult.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLE-MPLS-TP-BFD-MIB",
    **{"sleMpls": sleMpls,
       "sleMplsTpBfd": sleMplsTpBfd,
       "sleMplsTpBfdCfg": sleMplsTpBfdCfg,
       "sleMplsTpBfdCfgInfoTable": sleMplsTpBfdCfgInfoTable,
       "sleMplsTpBfdCfgInfoEntry": sleMplsTpBfdCfgInfoEntry,
       "sleMplsTpBfdCfgInfoMegIndex": sleMplsTpBfdCfgInfoMegIndex,
       "sleMplsTpBfdCfgInfoMeIndex": sleMplsTpBfdCfgInfoMeIndex,
       "sleMplsTpBfdCfgInfoMegName": sleMplsTpBfdCfgInfoMegName,
       "sleMplsTpBfdCfgInfoMeName": sleMplsTpBfdCfgInfoMeName,
       "sleMplsTpBfdCfgInfoTxInterval": sleMplsTpBfdCfgInfoTxInterval,
       "sleMplsTpBfdCfgInfoRXInterval": sleMplsTpBfdCfgInfoRXInterval,
       "sleMplsTpBfdCfgControl": sleMplsTpBfdCfgControl,
       "sleMplsTpBfdCfgControlRequest": sleMplsTpBfdCfgControlRequest,
       "sleMplsTpBfdCfgControlStatus": sleMplsTpBfdCfgControlStatus,
       "sleMplsTpBfdCfgControlTimer": sleMplsTpBfdCfgControlTimer,
       "sleMplsTpBfdCfgControlTimestamp": sleMplsTpBfdCfgControlTimestamp,
       "sleMplsTpBfdCfgControlReqResult": sleMplsTpBfdCfgControlReqResult,
       "sleMplsTpBfdCfgControlMegName": sleMplsTpBfdCfgControlMegName,
       "sleMplsTpBfdCfgControlMeName": sleMplsTpBfdCfgControlMeName,
       "sleMplsTpBfdCfgControlTxInterval": sleMplsTpBfdCfgControlTxInterval,
       "sleMplsTpBfdCfgControlRXInterval": sleMplsTpBfdCfgControlRXInterval,
       "sleMplsTpBfdSession": sleMplsTpBfdSession,
       "sleMplsTpBfdSessionInfoTable": sleMplsTpBfdSessionInfoTable,
       "sleMplsTpBfdSessionInfoEntry": sleMplsTpBfdSessionInfoEntry,
       "sleMplsTpBfdSessionInfoSessIndex": sleMplsTpBfdSessionInfoSessIndex,
       "sleMplsTpBfdSessionInfoMegName": sleMplsTpBfdSessionInfoMegName,
       "sleMplsTpBfdSessionInfoMeName": sleMplsTpBfdSessionInfoMeName,
       "sleMplsTpBfdSessionInfoVersionNumber": sleMplsTpBfdSessionInfoVersionNumber,
       "sleMplsTpBfdSessionInfoDiscriminator": sleMplsTpBfdSessionInfoDiscriminator,
       "sleMplsTpBfdSessionInfoRemoteDiscriminator": sleMplsTpBfdSessionInfoRemoteDiscriminator,
       "sleMplsTpBfdSessionInfoState": sleMplsTpBfdSessionInfoState,
       "sleMplsTpBfdSessionInfoDiag": sleMplsTpBfdSessionInfoDiag,
       "sleMplsTpBfdSessionInfoDesiredMinTxInterval": sleMplsTpBfdSessionInfoDesiredMinTxInterval,
       "sleMplsTpBfdSessionInfoReqMinRxInterval": sleMplsTpBfdSessionInfoReqMinRxInterval,
       "sleMplsTpBfdSessionInfoDetectMult": sleMplsTpBfdSessionInfoDetectMult}
)
