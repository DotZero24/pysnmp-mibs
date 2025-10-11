# SNMP MIB module (LUM-PSR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-PSR-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:42 2025
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

(lumModules,
 lumPsrMIB) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumModules",
    "lumPsrMIB")

(FaultStatus,
 MgmtNameString) = mibBuilder.importSymbols(
    "LUM-TC",
    "FaultStatus",
    "MgmtNameString")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

lumPsrMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 43)
)
if mibBuilder.loadTexts:
    lumPsrMIBModule.setRevisions(
        ("2017-06-15 00:00",
         "2012-12-20 00:00",
         "2012-03-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class InputRequest(TextualConvention, Integer32):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("noRequest", 2),
          ("lockOut", 3),
          ("forcedSwitch", 4),
          ("signalFailProtecting", 5),
          ("signalFailWorking", 6),
          ("manualSwitch", 7),
          ("waitToRestore", 8),
          ("doNotRevert", 9),
          ("noConnection", 10))
    )



class PathState(TextualConvention, Integer32):
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
        *(("down", 1),
          ("up", 2),
          ("unknown", 3))
    )



class SupvType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("layer1", 1),
          ("bfd", 2))
    )



# MIB Managed Objects in the order of their OIDs

_LumPsrConfs_ObjectIdentity = ObjectIdentity
lumPsrConfs = _LumPsrConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 43, 1)
)
_LumPsrGroups_ObjectIdentity = ObjectIdentity
lumPsrGroups = _LumPsrGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 43, 1, 1)
)
_LumPsrCompl_ObjectIdentity = ObjectIdentity
lumPsrCompl = _LumPsrCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 43, 1, 2)
)
_LumPsrMIBObjects_ObjectIdentity = ObjectIdentity
lumPsrMIBObjects = _LumPsrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 43, 2)
)
_PsrGeneral_ObjectIdentity = ObjectIdentity
psrGeneral = _PsrGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 43, 2, 1)
)
_PsrGeneralLastChangeTime_Type = DateAndTime
_PsrGeneralLastChangeTime_Object = MibScalar
psrGeneralLastChangeTime = _PsrGeneralLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 43, 2, 1, 1),
    _PsrGeneralLastChangeTime_Type()
)
psrGeneralLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psrGeneralLastChangeTime.setStatus("current")
_PsrGeneralStateLastChangeTime_Type = DateAndTime
_PsrGeneralStateLastChangeTime_Object = MibScalar
psrGeneralStateLastChangeTime = _PsrGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 43, 2, 1, 2),
    _PsrGeneralStateLastChangeTime_Type()
)
psrGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psrGeneralStateLastChangeTime.setStatus("current")
_PsrGeneralPsrMplsLinearProtTableSize_Type = Unsigned32
_PsrGeneralPsrMplsLinearProtTableSize_Object = MibScalar
psrGeneralPsrMplsLinearProtTableSize = _PsrGeneralPsrMplsLinearProtTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 43, 2, 1, 9),
    _PsrGeneralPsrMplsLinearProtTableSize_Type()
)
psrGeneralPsrMplsLinearProtTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psrGeneralPsrMplsLinearProtTableSize.setStatus("current")
_PsrMplsLinearProtList_ObjectIdentity = ObjectIdentity
psrMplsLinearProtList = _PsrMplsLinearProtList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 43, 2, 2)
)
_PsrMplsLinearProtTable_Object = MibTable
psrMplsLinearProtTable = _PsrMplsLinearProtTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 43, 2, 2, 1)
)
if mibBuilder.loadTexts:
    psrMplsLinearProtTable.setStatus("current")
_PsrMplsLinearProtEntry_Object = MibTableRow
psrMplsLinearProtEntry = _PsrMplsLinearProtEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 43, 2, 2, 1, 1)
)
psrMplsLinearProtEntry.setIndexNames(
    (0, "LUM-PSR-MIB", "psrMplsLinearProtIndex"),
)
if mibBuilder.loadTexts:
    psrMplsLinearProtEntry.setStatus("current")


class _PsrMplsLinearProtIndex_Type(Unsigned32):
    """Custom type psrMplsLinearProtIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PsrMplsLinearProtIndex_Type.__name__ = "Unsigned32"
_PsrMplsLinearProtIndex_Object = MibTableColumn
psrMplsLinearProtIndex = _PsrMplsLinearProtIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 43, 2, 2, 1, 1, 1),
    _PsrMplsLinearProtIndex_Type()
)
psrMplsLinearProtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psrMplsLinearProtIndex.setStatus("current")


class _PsrMplsLinearProtInternalReference_Type(Unsigned32):
    """Custom type psrMplsLinearProtInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PsrMplsLinearProtInternalReference_Type.__name__ = "Unsigned32"
_PsrMplsLinearProtInternalReference_Object = MibTableColumn
psrMplsLinearProtInternalReference = _PsrMplsLinearProtInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 43, 2, 2, 1, 1, 2),
    _PsrMplsLinearProtInternalReference_Type()
)
psrMplsLinearProtInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    psrMplsLinearProtInternalReference.setStatus("current")
_PsrMplsLinearProtName_Type = MgmtNameString
_PsrMplsLinearProtName_Object = MibTableColumn
psrMplsLinearProtName = _PsrMplsLinearProtName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 43, 2, 2, 1, 1, 3),
    _PsrMplsLinearProtName_Type()
)
psrMplsLinearProtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psrMplsLinearProtName.setStatus("current")


class _PsrMplsLinearProtTunnelId_Type(DisplayString):
    """Custom type psrMplsLinearProtTunnelId based on DisplayString"""
    defaultValue = OctetString("")


_PsrMplsLinearProtTunnelId_Type.__name__ = "DisplayString"
_PsrMplsLinearProtTunnelId_Object = MibTableColumn
psrMplsLinearProtTunnelId = _PsrMplsLinearProtTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 43, 2, 2, 1, 1, 4),
    _PsrMplsLinearProtTunnelId_Type()
)
psrMplsLinearProtTunnelId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    psrMplsLinearProtTunnelId.setStatus("current")


class _PsrMplsLinearProtAdminStatus_Type(Integer32):
    """Custom type psrMplsLinearProtAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_PsrMplsLinearProtAdminStatus_Type.__name__ = "Integer32"
_PsrMplsLinearProtAdminStatus_Object = MibTableColumn
psrMplsLinearProtAdminStatus = _PsrMplsLinearProtAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 43, 2, 2, 1, 1, 5),
    _PsrMplsLinearProtAdminStatus_Type()
)
psrMplsLinearProtAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psrMplsLinearProtAdminStatus.setStatus("current")


class _PsrMplsLinearProtState_Type(Integer32):
    """Custom type psrMplsLinearProtState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("protectionPathUnavailable", 2),
          ("workingPathFailure", 3),
          ("administrative", 4),
          ("waitToRestore", 5),
          ("doNotRevert", 6),
          ("unknown", 7))
    )


_PsrMplsLinearProtState_Type.__name__ = "Integer32"
_PsrMplsLinearProtState_Object = MibTableColumn
psrMplsLinearProtState = _PsrMplsLinearProtState_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 43, 2, 2, 1, 1, 6),
    _PsrMplsLinearProtState_Type()
)
psrMplsLinearProtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psrMplsLinearProtState.setStatus("current")
_PsrMplsLinearProtLocalEvent_Type = InputRequest
_PsrMplsLinearProtLocalEvent_Object = MibTableColumn
psrMplsLinearProtLocalEvent = _PsrMplsLinearProtLocalEvent_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 43, 2, 2, 1, 1, 7),
    _PsrMplsLinearProtLocalEvent_Type()
)
psrMplsLinearProtLocalEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psrMplsLinearProtLocalEvent.setStatus("current")
_PsrMplsLinearProtRemoteEvent_Type = InputRequest
_PsrMplsLinearProtRemoteEvent_Object = MibTableColumn
psrMplsLinearProtRemoteEvent = _PsrMplsLinearProtRemoteEvent_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 43, 2, 2, 1, 1, 8),
    _PsrMplsLinearProtRemoteEvent_Type()
)
psrMplsLinearProtRemoteEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psrMplsLinearProtRemoteEvent.setStatus("current")


class _PsrMplsLinearProtWorkingPathId_Type(DisplayString):
    """Custom type psrMplsLinearProtWorkingPathId based on DisplayString"""
    defaultValue = OctetString("")


_PsrMplsLinearProtWorkingPathId_Type.__name__ = "DisplayString"
_PsrMplsLinearProtWorkingPathId_Object = MibTableColumn
psrMplsLinearProtWorkingPathId = _PsrMplsLinearProtWorkingPathId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 43, 2, 2, 1, 1, 9),
    _PsrMplsLinearProtWorkingPathId_Type()
)
psrMplsLinearProtWorkingPathId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    psrMplsLinearProtWorkingPathId.setStatus("current")


class _PsrMplsLinearProtWorkingPathIndex_Type(Unsigned32):
    """Custom type psrMplsLinearProtWorkingPathIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PsrMplsLinearProtWorkingPathIndex_Type.__name__ = "Unsigned32"
_PsrMplsLinearProtWorkingPathIndex_Object = MibTableColumn
psrMplsLinearProtWorkingPathIndex = _PsrMplsLinearProtWorkingPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 43, 2, 2, 1, 1, 10),
    _PsrMplsLinearProtWorkingPathIndex_Type()
)
psrMplsLinearProtWorkingPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psrMplsLinearProtWorkingPathIndex.setStatus("current")
_PsrMplsLinearProtWorkingPathState_Type = PathState
_PsrMplsLinearProtWorkingPathState_Object = MibTableColumn
psrMplsLinearProtWorkingPathState = _PsrMplsLinearProtWorkingPathState_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 43, 2, 2, 1, 1, 11),
    _PsrMplsLinearProtWorkingPathState_Type()
)
psrMplsLinearProtWorkingPathState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psrMplsLinearProtWorkingPathState.setStatus("current")
_PsrMplsLinearProtWpathSupvType_Type = SupvType
_PsrMplsLinearProtWpathSupvType_Object = MibTableColumn
psrMplsLinearProtWpathSupvType = _PsrMplsLinearProtWpathSupvType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 43, 2, 2, 1, 1, 12),
    _PsrMplsLinearProtWpathSupvType_Type()
)
psrMplsLinearProtWpathSupvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psrMplsLinearProtWpathSupvType.setStatus("current")


class _PsrMplsLinearProtProtectionPathId_Type(DisplayString):
    """Custom type psrMplsLinearProtProtectionPathId based on DisplayString"""
    defaultValue = OctetString("")


_PsrMplsLinearProtProtectionPathId_Type.__name__ = "DisplayString"
_PsrMplsLinearProtProtectionPathId_Object = MibTableColumn
psrMplsLinearProtProtectionPathId = _PsrMplsLinearProtProtectionPathId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 43, 2, 2, 1, 1, 13),
    _PsrMplsLinearProtProtectionPathId_Type()
)
psrMplsLinearProtProtectionPathId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    psrMplsLinearProtProtectionPathId.setStatus("current")


class _PsrMplsLinearProtProtectionPathIndex_Type(Unsigned32):
    """Custom type psrMplsLinearProtProtectionPathIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PsrMplsLinearProtProtectionPathIndex_Type.__name__ = "Unsigned32"
_PsrMplsLinearProtProtectionPathIndex_Object = MibTableColumn
psrMplsLinearProtProtectionPathIndex = _PsrMplsLinearProtProtectionPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 43, 2, 2, 1, 1, 14),
    _PsrMplsLinearProtProtectionPathIndex_Type()
)
psrMplsLinearProtProtectionPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psrMplsLinearProtProtectionPathIndex.setStatus("current")
_PsrMplsLinearProtProtectionPathState_Type = PathState
_PsrMplsLinearProtProtectionPathState_Object = MibTableColumn
psrMplsLinearProtProtectionPathState = _PsrMplsLinearProtProtectionPathState_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 43, 2, 2, 1, 1, 15),
    _PsrMplsLinearProtProtectionPathState_Type()
)
psrMplsLinearProtProtectionPathState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psrMplsLinearProtProtectionPathState.setStatus("current")
_PsrMplsLinearProtPpathSupvType_Type = SupvType
_PsrMplsLinearProtPpathSupvType_Object = MibTableColumn
psrMplsLinearProtPpathSupvType = _PsrMplsLinearProtPpathSupvType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 43, 2, 2, 1, 1, 16),
    _PsrMplsLinearProtPpathSupvType_Type()
)
psrMplsLinearProtPpathSupvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psrMplsLinearProtPpathSupvType.setStatus("current")


class _PsrMplsLinearProtActivePath_Type(Integer32):
    """Custom type psrMplsLinearProtActivePath based on Integer32"""
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
        *(("workingPath", 1),
          ("protectionPath", 2),
          ("none", 3),
          ("unknown", 4))
    )


_PsrMplsLinearProtActivePath_Type.__name__ = "Integer32"
_PsrMplsLinearProtActivePath_Object = MibTableColumn
psrMplsLinearProtActivePath = _PsrMplsLinearProtActivePath_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 43, 2, 2, 1, 1, 17),
    _PsrMplsLinearProtActivePath_Type()
)
psrMplsLinearProtActivePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psrMplsLinearProtActivePath.setStatus("current")


class _PsrMplsLinearProtOperatorCommand_Type(Integer32):
    """Custom type psrMplsLinearProtOperatorCommand based on Integer32"""
    defaultValue = 1

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
        *(("noRequest", 1),
          ("lockOut", 2),
          ("forced", 3),
          ("manual", 4))
    )


_PsrMplsLinearProtOperatorCommand_Type.__name__ = "Integer32"
_PsrMplsLinearProtOperatorCommand_Object = MibTableColumn
psrMplsLinearProtOperatorCommand = _PsrMplsLinearProtOperatorCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 43, 2, 2, 1, 1, 18),
    _PsrMplsLinearProtOperatorCommand_Type()
)
psrMplsLinearProtOperatorCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psrMplsLinearProtOperatorCommand.setStatus("current")


class _PsrMplsLinearProtHoldoffTimer_Type(Unsigned32):
    """Custom type psrMplsLinearProtHoldoffTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_PsrMplsLinearProtHoldoffTimer_Type.__name__ = "Unsigned32"
_PsrMplsLinearProtHoldoffTimer_Object = MibTableColumn
psrMplsLinearProtHoldoffTimer = _PsrMplsLinearProtHoldoffTimer_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 43, 2, 2, 1, 1, 19),
    _PsrMplsLinearProtHoldoffTimer_Type()
)
psrMplsLinearProtHoldoffTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psrMplsLinearProtHoldoffTimer.setStatus("current")
_PsrMplsLinearProtProtectionFailed_Type = FaultStatus
_PsrMplsLinearProtProtectionFailed_Object = MibTableColumn
psrMplsLinearProtProtectionFailed = _PsrMplsLinearProtProtectionFailed_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 43, 2, 2, 1, 1, 20),
    _PsrMplsLinearProtProtectionFailed_Type()
)
psrMplsLinearProtProtectionFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psrMplsLinearProtProtectionFailed.setStatus("current")
_PsrMplsLinearProtProtectionDegraded_Type = FaultStatus
_PsrMplsLinearProtProtectionDegraded_Object = MibTableColumn
psrMplsLinearProtProtectionDegraded = _PsrMplsLinearProtProtectionDegraded_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 43, 2, 2, 1, 1, 21),
    _PsrMplsLinearProtProtectionDegraded_Type()
)
psrMplsLinearProtProtectionDegraded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psrMplsLinearProtProtectionDegraded.setStatus("current")
_PsrMplsLinearProtCommunicationFailure_Type = FaultStatus
_PsrMplsLinearProtCommunicationFailure_Object = MibTableColumn
psrMplsLinearProtCommunicationFailure = _PsrMplsLinearProtCommunicationFailure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 43, 2, 2, 1, 1, 22),
    _PsrMplsLinearProtCommunicationFailure_Type()
)
psrMplsLinearProtCommunicationFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psrMplsLinearProtCommunicationFailure.setStatus("current")
_PsrMplsLinearProtConfigMismatch_Type = FaultStatus
_PsrMplsLinearProtConfigMismatch_Object = MibTableColumn
psrMplsLinearProtConfigMismatch = _PsrMplsLinearProtConfigMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 43, 2, 2, 1, 1, 23),
    _PsrMplsLinearProtConfigMismatch_Type()
)
psrMplsLinearProtConfigMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psrMplsLinearProtConfigMismatch.setStatus("current")

# Managed Objects groups

psrGeneralGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 43, 1, 1, 1)
)
psrGeneralGroupV1.setObjects(
      *(("LUM-PSR-MIB", "psrGeneralLastChangeTime"),
        ("LUM-PSR-MIB", "psrGeneralStateLastChangeTime"),
        ("LUM-PSR-MIB", "psrGeneralPsrMplsLinearProtTableSize"))
)
if mibBuilder.loadTexts:
    psrGeneralGroupV1.setStatus("current")

psrMplsLinearProtGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 43, 1, 1, 2)
)
psrMplsLinearProtGroupV1.setObjects(
      *(("LUM-PSR-MIB", "psrMplsLinearProtIndex"),
        ("LUM-PSR-MIB", "psrMplsLinearProtInternalReference"),
        ("LUM-PSR-MIB", "psrMplsLinearProtName"),
        ("LUM-PSR-MIB", "psrMplsLinearProtTunnelId"),
        ("LUM-PSR-MIB", "psrMplsLinearProtAdminStatus"),
        ("LUM-PSR-MIB", "psrMplsLinearProtState"),
        ("LUM-PSR-MIB", "psrMplsLinearProtLocalEvent"),
        ("LUM-PSR-MIB", "psrMplsLinearProtRemoteEvent"),
        ("LUM-PSR-MIB", "psrMplsLinearProtWorkingPathId"),
        ("LUM-PSR-MIB", "psrMplsLinearProtWorkingPathIndex"),
        ("LUM-PSR-MIB", "psrMplsLinearProtWorkingPathState"),
        ("LUM-PSR-MIB", "psrMplsLinearProtWpathSupvType"),
        ("LUM-PSR-MIB", "psrMplsLinearProtProtectionPathId"),
        ("LUM-PSR-MIB", "psrMplsLinearProtProtectionPathIndex"),
        ("LUM-PSR-MIB", "psrMplsLinearProtProtectionPathState"),
        ("LUM-PSR-MIB", "psrMplsLinearProtPpathSupvType"),
        ("LUM-PSR-MIB", "psrMplsLinearProtActivePath"),
        ("LUM-PSR-MIB", "psrMplsLinearProtOperatorCommand"),
        ("LUM-PSR-MIB", "psrMplsLinearProtHoldoffTimer"),
        ("LUM-PSR-MIB", "psrMplsLinearProtProtectionFailed"),
        ("LUM-PSR-MIB", "psrMplsLinearProtProtectionDegraded"),
        ("LUM-PSR-MIB", "psrMplsLinearProtCommunicationFailure"),
        ("LUM-PSR-MIB", "psrMplsLinearProtConfigMismatch"))
)
if mibBuilder.loadTexts:
    psrMplsLinearProtGroupV1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumPsrBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 43, 1, 2, 1)
)
lumPsrBasicComplV1.setObjects(
      *(("LUM-PSR-MIB", "psrGeneralGroupV1"),
        ("LUM-PSR-MIB", "psrMplsLinearProtGroupV1"))
)
if mibBuilder.loadTexts:
    lumPsrBasicComplV1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-PSR-MIB",
    **{"InputRequest": InputRequest,
       "PathState": PathState,
       "SupvType": SupvType,
       "lumPsrMIBModule": lumPsrMIBModule,
       "lumPsrConfs": lumPsrConfs,
       "lumPsrGroups": lumPsrGroups,
       "psrGeneralGroupV1": psrGeneralGroupV1,
       "psrMplsLinearProtGroupV1": psrMplsLinearProtGroupV1,
       "lumPsrCompl": lumPsrCompl,
       "lumPsrBasicComplV1": lumPsrBasicComplV1,
       "lumPsrMIBObjects": lumPsrMIBObjects,
       "psrGeneral": psrGeneral,
       "psrGeneralLastChangeTime": psrGeneralLastChangeTime,
       "psrGeneralStateLastChangeTime": psrGeneralStateLastChangeTime,
       "psrGeneralPsrMplsLinearProtTableSize": psrGeneralPsrMplsLinearProtTableSize,
       "psrMplsLinearProtList": psrMplsLinearProtList,
       "psrMplsLinearProtTable": psrMplsLinearProtTable,
       "psrMplsLinearProtEntry": psrMplsLinearProtEntry,
       "psrMplsLinearProtIndex": psrMplsLinearProtIndex,
       "psrMplsLinearProtInternalReference": psrMplsLinearProtInternalReference,
       "psrMplsLinearProtName": psrMplsLinearProtName,
       "psrMplsLinearProtTunnelId": psrMplsLinearProtTunnelId,
       "psrMplsLinearProtAdminStatus": psrMplsLinearProtAdminStatus,
       "psrMplsLinearProtState": psrMplsLinearProtState,
       "psrMplsLinearProtLocalEvent": psrMplsLinearProtLocalEvent,
       "psrMplsLinearProtRemoteEvent": psrMplsLinearProtRemoteEvent,
       "psrMplsLinearProtWorkingPathId": psrMplsLinearProtWorkingPathId,
       "psrMplsLinearProtWorkingPathIndex": psrMplsLinearProtWorkingPathIndex,
       "psrMplsLinearProtWorkingPathState": psrMplsLinearProtWorkingPathState,
       "psrMplsLinearProtWpathSupvType": psrMplsLinearProtWpathSupvType,
       "psrMplsLinearProtProtectionPathId": psrMplsLinearProtProtectionPathId,
       "psrMplsLinearProtProtectionPathIndex": psrMplsLinearProtProtectionPathIndex,
       "psrMplsLinearProtProtectionPathState": psrMplsLinearProtProtectionPathState,
       "psrMplsLinearProtPpathSupvType": psrMplsLinearProtPpathSupvType,
       "psrMplsLinearProtActivePath": psrMplsLinearProtActivePath,
       "psrMplsLinearProtOperatorCommand": psrMplsLinearProtOperatorCommand,
       "psrMplsLinearProtHoldoffTimer": psrMplsLinearProtHoldoffTimer,
       "psrMplsLinearProtProtectionFailed": psrMplsLinearProtProtectionFailed,
       "psrMplsLinearProtProtectionDegraded": psrMplsLinearProtProtectionDegraded,
       "psrMplsLinearProtCommunicationFailure": psrMplsLinearProtCommunicationFailure,
       "psrMplsLinearProtConfigMismatch": psrMplsLinearProtConfigMismatch}
)
