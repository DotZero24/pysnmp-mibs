# SNMP MIB module (LUM-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-CLIENT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:07 2025
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

(lumClientMIB,
 lumModules) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumClientMIB",
    "lumModules")

(BerLevelMTOSI,
 BoardOrInterfaceAdminStatus,
 BoardOrInterfaceOperStatus,
 CommandString,
 EnableDisable,
 FaultStatus,
 InterfaceType,
 LambdaFrequency,
 LaneFrequency,
 MgmtNameString,
 ObjectProperty,
 OnOff,
 OpticalLayerMappingType,
 PhysicalLayerMappingType,
 PortNumber,
 SignalDirection,
 SignalFormat,
 SignalStatusWithNA,
 SlotNumber,
 SubrackNumber,
 TrxMedia,
 TrxRxState,
 TrxTxState) = mibBuilder.importSymbols(
    "LUM-TC",
    "BerLevelMTOSI",
    "BoardOrInterfaceAdminStatus",
    "BoardOrInterfaceOperStatus",
    "CommandString",
    "EnableDisable",
    "FaultStatus",
    "InterfaceType",
    "LambdaFrequency",
    "LaneFrequency",
    "MgmtNameString",
    "ObjectProperty",
    "OnOff",
    "OpticalLayerMappingType",
    "PhysicalLayerMappingType",
    "PortNumber",
    "SignalDirection",
    "SignalFormat",
    "SignalStatusWithNA",
    "SlotNumber",
    "SubrackNumber",
    "TrxMedia",
    "TrxRxState",
    "TrxTxState")

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

lumClientMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 27)
)
if mibBuilder.loadTexts:
    lumClientMIBModule.setRevisions(
        ("2018-08-23 00:00",
         "2018-04-13 00:00",
         "2017-12-15 00:00",
         "2017-06-15 00:00",
         "2016-11-30 00:00",
         "2016-07-15 00:00",
         "2016-05-24 00:00",
         "2015-12-15 00:00",
         "2015-01-14 00:00",
         "2014-08-15 00:00",
         "2014-05-16 00:00",
         "2013-09-30 00:00",
         "2013-05-01 00:00",
         "2012-12-20 00:00",
         "2012-03-30 00:00",
         "2011-12-20 00:00",
         "2011-04-12 00:00",
         "2006-01-27 00:00",
         "2005-09-14 00:00",
         "2004-04-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LumClientConfs_ObjectIdentity = ObjectIdentity
lumClientConfs = _LumClientConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1)
)
_LumClientGroups_ObjectIdentity = ObjectIdentity
lumClientGroups = _LumClientGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 1)
)
_LumClientCompl_ObjectIdentity = ObjectIdentity
lumClientCompl = _LumClientCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 2)
)
_LumClientMinimalGroups_ObjectIdentity = ObjectIdentity
lumClientMinimalGroups = _LumClientMinimalGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 3)
)
_LumClientMinimalCompl_ObjectIdentity = ObjectIdentity
lumClientMinimalCompl = _LumClientMinimalCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 4)
)
_LumClientMIBObjects_ObjectIdentity = ObjectIdentity
lumClientMIBObjects = _LumClientMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2)
)
_ClientGeneral_ObjectIdentity = ObjectIdentity
clientGeneral = _ClientGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 1)
)
_ClientGeneralLastChangeTime_Type = DateAndTime
_ClientGeneralLastChangeTime_Object = MibScalar
clientGeneralLastChangeTime = _ClientGeneralLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 1, 1),
    _ClientGeneralLastChangeTime_Type()
)
clientGeneralLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientGeneralLastChangeTime.setStatus("current")
_ClientGeneralStateLastChangeTime_Type = DateAndTime
_ClientGeneralStateLastChangeTime_Object = MibScalar
clientGeneralStateLastChangeTime = _ClientGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 1, 2),
    _ClientGeneralStateLastChangeTime_Type()
)
clientGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientGeneralStateLastChangeTime.setStatus("current")
_ClientGeneralClientIfTableSize_Type = Unsigned32
_ClientGeneralClientIfTableSize_Object = MibScalar
clientGeneralClientIfTableSize = _ClientGeneralClientIfTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 1, 3),
    _ClientGeneralClientIfTableSize_Type()
)
clientGeneralClientIfTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientGeneralClientIfTableSize.setStatus("current")
_ClientGeneralVc4TableSize_Type = Unsigned32
_ClientGeneralVc4TableSize_Object = MibScalar
clientGeneralVc4TableSize = _ClientGeneralVc4TableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 1, 4),
    _ClientGeneralVc4TableSize_Type()
)
clientGeneralVc4TableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientGeneralVc4TableSize.setStatus("current")
_ClientGeneralLanesTableSize_Type = Unsigned32
_ClientGeneralLanesTableSize_Object = MibScalar
clientGeneralLanesTableSize = _ClientGeneralLanesTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 1, 5),
    _ClientGeneralLanesTableSize_Type()
)
clientGeneralLanesTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientGeneralLanesTableSize.setStatus("current")
_ClientGeneralMpoLanesTableSize_Type = Unsigned32
_ClientGeneralMpoLanesTableSize_Object = MibScalar
clientGeneralMpoLanesTableSize = _ClientGeneralMpoLanesTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 1, 6),
    _ClientGeneralMpoLanesTableSize_Type()
)
clientGeneralMpoLanesTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientGeneralMpoLanesTableSize.setStatus("current")
_ClientIfList_ObjectIdentity = ObjectIdentity
clientIfList = _ClientIfList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2)
)
_ClientIfTable_Object = MibTable
clientIfTable = _ClientIfTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1)
)
if mibBuilder.loadTexts:
    clientIfTable.setStatus("current")
_ClientIfEntry_Object = MibTableRow
clientIfEntry = _ClientIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1)
)
clientIfEntry.setIndexNames(
    (0, "LUM-CLIENT-MIB", "clientIfIndex"),
)
if mibBuilder.loadTexts:
    clientIfEntry.setStatus("current")


class _ClientIfIndex_Type(Unsigned32):
    """Custom type clientIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClientIfIndex_Type.__name__ = "Unsigned32"
_ClientIfIndex_Object = MibTableColumn
clientIfIndex = _ClientIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 1),
    _ClientIfIndex_Type()
)
clientIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clientIfIndex.setStatus("current")


class _ClientIfName_Type(MgmtNameString):
    """Custom type clientIfName based on MgmtNameString"""
    defaultValue = OctetString("")


_ClientIfName_Type.__name__ = "MgmtNameString"
_ClientIfName_Object = MibTableColumn
clientIfName = _ClientIfName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 2),
    _ClientIfName_Type()
)
clientIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clientIfName.setStatus("current")


class _ClientIfDescr_Type(DisplayString):
    """Custom type clientIfDescr based on DisplayString"""
    defaultValue = OctetString("")


_ClientIfDescr_Type.__name__ = "DisplayString"
_ClientIfDescr_Object = MibTableColumn
clientIfDescr = _ClientIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 3),
    _ClientIfDescr_Type()
)
clientIfDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientIfDescr.setStatus("current")


class _ClientIfSubrack_Type(SubrackNumber):
    """Custom type clientIfSubrack based on SubrackNumber"""
    defaultValue = 0


_ClientIfSubrack_Type.__name__ = "SubrackNumber"
_ClientIfSubrack_Object = MibTableColumn
clientIfSubrack = _ClientIfSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 4),
    _ClientIfSubrack_Type()
)
clientIfSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clientIfSubrack.setStatus("current")


class _ClientIfSlot_Type(SlotNumber):
    """Custom type clientIfSlot based on SlotNumber"""
    defaultValue = 0


_ClientIfSlot_Type.__name__ = "SlotNumber"
_ClientIfSlot_Object = MibTableColumn
clientIfSlot = _ClientIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 5),
    _ClientIfSlot_Type()
)
clientIfSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clientIfSlot.setStatus("current")


class _ClientIfTxPort_Type(PortNumber):
    """Custom type clientIfTxPort based on PortNumber"""
    defaultValue = 0


_ClientIfTxPort_Type.__name__ = "PortNumber"
_ClientIfTxPort_Object = MibTableColumn
clientIfTxPort = _ClientIfTxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 6),
    _ClientIfTxPort_Type()
)
clientIfTxPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clientIfTxPort.setStatus("current")


class _ClientIfRxPort_Type(PortNumber):
    """Custom type clientIfRxPort based on PortNumber"""
    defaultValue = 0


_ClientIfRxPort_Type.__name__ = "PortNumber"
_ClientIfRxPort_Object = MibTableColumn
clientIfRxPort = _ClientIfRxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 7),
    _ClientIfRxPort_Type()
)
clientIfRxPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clientIfRxPort.setStatus("current")


class _ClientIfInvPhysIndexOrZero_Type(Unsigned32):
    """Custom type clientIfInvPhysIndexOrZero based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ClientIfInvPhysIndexOrZero_Type.__name__ = "Unsigned32"
_ClientIfInvPhysIndexOrZero_Object = MibTableColumn
clientIfInvPhysIndexOrZero = _ClientIfInvPhysIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 8),
    _ClientIfInvPhysIndexOrZero_Type()
)
clientIfInvPhysIndexOrZero.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clientIfInvPhysIndexOrZero.setStatus("current")


class _ClientIfEntityId_Type(Unsigned32):
    """Custom type clientIfEntityId based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClientIfEntityId_Type.__name__ = "Unsigned32"
_ClientIfEntityId_Object = MibTableColumn
clientIfEntityId = _ClientIfEntityId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 9),
    _ClientIfEntityId_Type()
)
clientIfEntityId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clientIfEntityId.setStatus("current")


class _ClientIfAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type clientIfAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 3


_ClientIfAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_ClientIfAdminStatus_Object = MibTableColumn
clientIfAdminStatus = _ClientIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 10),
    _ClientIfAdminStatus_Type()
)
clientIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientIfAdminStatus.setStatus("current")


class _ClientIfOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type clientIfOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 1


_ClientIfOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_ClientIfOperStatus_Object = MibTableColumn
clientIfOperStatus = _ClientIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 11),
    _ClientIfOperStatus_Type()
)
clientIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfOperStatus.setStatus("current")


class _ClientIfLaserStatus_Type(Integer32):
    """Custom type clientIfLaserStatus based on Integer32"""
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


_ClientIfLaserStatus_Type.__name__ = "Integer32"
_ClientIfLaserStatus_Object = MibTableColumn
clientIfLaserStatus = _ClientIfLaserStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 12),
    _ClientIfLaserStatus_Type()
)
clientIfLaserStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfLaserStatus.setStatus("current")


class _ClientIfTxSignalStatus_Type(SignalStatusWithNA):
    """Custom type clientIfTxSignalStatus based on SignalStatusWithNA"""
    defaultValue = 1


_ClientIfTxSignalStatus_Type.__name__ = "SignalStatusWithNA"
_ClientIfTxSignalStatus_Object = MibTableColumn
clientIfTxSignalStatus = _ClientIfTxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 13),
    _ClientIfTxSignalStatus_Type()
)
clientIfTxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfTxSignalStatus.setStatus("current")


class _ClientIfForwardAls_Type(Integer32):
    """Custom type clientIfForwardAls based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ClientIfForwardAls_Type.__name__ = "Integer32"
_ClientIfForwardAls_Object = MibTableColumn
clientIfForwardAls = _ClientIfForwardAls_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 14),
    _ClientIfForwardAls_Type()
)
clientIfForwardAls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientIfForwardAls.setStatus("current")


class _ClientIfSuppressRemoteAlarms_Type(Integer32):
    """Custom type clientIfSuppressRemoteAlarms based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ClientIfSuppressRemoteAlarms_Type.__name__ = "Integer32"
_ClientIfSuppressRemoteAlarms_Object = MibTableColumn
clientIfSuppressRemoteAlarms = _ClientIfSuppressRemoteAlarms_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 15),
    _ClientIfSuppressRemoteAlarms_Type()
)
clientIfSuppressRemoteAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientIfSuppressRemoteAlarms.setStatus("current")


class _ClientIfFarEndLoopback_Type(Integer32):
    """Custom type clientIfFarEndLoopback based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ClientIfFarEndLoopback_Type.__name__ = "Integer32"
_ClientIfFarEndLoopback_Object = MibTableColumn
clientIfFarEndLoopback = _ClientIfFarEndLoopback_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 16),
    _ClientIfFarEndLoopback_Type()
)
clientIfFarEndLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientIfFarEndLoopback.setStatus("current")


class _ClientIfFormat_Type(SignalFormat):
    """Custom type clientIfFormat based on SignalFormat"""
    defaultValue = 10


_ClientIfFormat_Type.__name__ = "SignalFormat"
_ClientIfFormat_Object = MibTableColumn
clientIfFormat = _ClientIfFormat_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 17),
    _ClientIfFormat_Type()
)
clientIfFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clientIfFormat.setStatus("current")


class _ClientIfGfpMode_Type(Integer32):
    """Custom type clientIfGfpMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("transparent", 1),
          ("framed", 2))
    )


_ClientIfGfpMode_Type.__name__ = "Integer32"
_ClientIfGfpMode_Object = MibTableColumn
clientIfGfpMode = _ClientIfGfpMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 18),
    _ClientIfGfpMode_Type()
)
clientIfGfpMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clientIfGfpMode.setStatus("current")


class _ClientIfBandWidth_Type(Integer32):
    """Custom type clientIfBandWidth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_ClientIfBandWidth_Type.__name__ = "Integer32"
_ClientIfBandWidth_Object = MibTableColumn
clientIfBandWidth = _ClientIfBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 19),
    _ClientIfBandWidth_Type()
)
clientIfBandWidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clientIfBandWidth.setStatus("current")


class _ClientIfRateLimit_Type(Integer32):
    """Custom type clientIfRateLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_ClientIfRateLimit_Type.__name__ = "Integer32"
_ClientIfRateLimit_Object = MibTableColumn
clientIfRateLimit = _ClientIfRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 20),
    _ClientIfRateLimit_Type()
)
clientIfRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientIfRateLimit.setStatus("current")


class _ClientIfAutoNegotiationMode_Type(Integer32):
    """Custom type clientIfAutoNegotiationMode based on Integer32"""
    defaultValue = 2

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


_ClientIfAutoNegotiationMode_Type.__name__ = "Integer32"
_ClientIfAutoNegotiationMode_Object = MibTableColumn
clientIfAutoNegotiationMode = _ClientIfAutoNegotiationMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 21),
    _ClientIfAutoNegotiationMode_Type()
)
clientIfAutoNegotiationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientIfAutoNegotiationMode.setStatus("current")


class _ClientIfAutoNegotiationStatus_Type(Integer32):
    """Custom type clientIfAutoNegotiationStatus based on Integer32"""
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
        *(("incomplete", 1),
          ("half", 2),
          ("full", 3))
    )


_ClientIfAutoNegotiationStatus_Type.__name__ = "Integer32"
_ClientIfAutoNegotiationStatus_Object = MibTableColumn
clientIfAutoNegotiationStatus = _ClientIfAutoNegotiationStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 22),
    _ClientIfAutoNegotiationStatus_Type()
)
clientIfAutoNegotiationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfAutoNegotiationStatus.setStatus("current")


class _ClientIfDuplexCapability_Type(Integer32):
    """Custom type clientIfDuplexCapability based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("half", 1),
          ("full", 2))
    )


_ClientIfDuplexCapability_Type.__name__ = "Integer32"
_ClientIfDuplexCapability_Object = MibTableColumn
clientIfDuplexCapability = _ClientIfDuplexCapability_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 23),
    _ClientIfDuplexCapability_Type()
)
clientIfDuplexCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfDuplexCapability.setStatus("current")


class _ClientIfFlowControlMode_Type(Integer32):
    """Custom type clientIfFlowControlMode based on Integer32"""
    defaultValue = 2

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
        *(("noPause", 1),
          ("rxPause", 2),
          ("txPause", 3),
          ("bothPause", 4))
    )


_ClientIfFlowControlMode_Type.__name__ = "Integer32"
_ClientIfFlowControlMode_Object = MibTableColumn
clientIfFlowControlMode = _ClientIfFlowControlMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 24),
    _ClientIfFlowControlMode_Type()
)
clientIfFlowControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientIfFlowControlMode.setStatus("current")


class _ClientIfInterPacketGap_Type(Gauge32):
    """Custom type clientIfInterPacketGap based on Gauge32"""
    defaultValue = 96

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 456),
    )


_ClientIfInterPacketGap_Type.__name__ = "Gauge32"
_ClientIfInterPacketGap_Object = MibTableColumn
clientIfInterPacketGap = _ClientIfInterPacketGap_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 25),
    _ClientIfInterPacketGap_Type()
)
clientIfInterPacketGap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientIfInterPacketGap.setStatus("current")


class _ClientIfFrameSize_Type(Gauge32):
    """Custom type clientIfFrameSize based on Gauge32"""
    defaultValue = 9600

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1518, 9600),
    )


_ClientIfFrameSize_Type.__name__ = "Gauge32"
_ClientIfFrameSize_Object = MibTableColumn
clientIfFrameSize = _ClientIfFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 26),
    _ClientIfFrameSize_Type()
)
clientIfFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientIfFrameSize.setStatus("current")


class _ClientIfTrxClass_Type(DisplayString):
    """Custom type clientIfTrxClass based on DisplayString"""
    defaultValue = OctetString("")


_ClientIfTrxClass_Type.__name__ = "DisplayString"
_ClientIfTrxClass_Object = MibTableColumn
clientIfTrxClass = _ClientIfTrxClass_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 27),
    _ClientIfTrxClass_Type()
)
clientIfTrxClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfTrxClass.setStatus("current")
_ClientIfLaserBias_Type = Unsigned32
_ClientIfLaserBias_Object = MibTableColumn
clientIfLaserBias = _ClientIfLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 28),
    _ClientIfLaserBias_Type()
)
clientIfLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfLaserBias.setStatus("current")
_ClientIfPowerLevel_Type = Integer32
_ClientIfPowerLevel_Object = MibTableColumn
clientIfPowerLevel = _ClientIfPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 29),
    _ClientIfPowerLevel_Type()
)
clientIfPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfPowerLevel.setStatus("current")
_ClientIfReceiverSensitivity_Type = Integer32
_ClientIfReceiverSensitivity_Object = MibTableColumn
clientIfReceiverSensitivity = _ClientIfReceiverSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 30),
    _ClientIfReceiverSensitivity_Type()
)
clientIfReceiverSensitivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfReceiverSensitivity.setStatus("current")


class _ClientIfPowerLevelLowRelativeThreshold_Type(Integer32):
    """Custom type clientIfPowerLevelLowRelativeThreshold based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_ClientIfPowerLevelLowRelativeThreshold_Type.__name__ = "Integer32"
_ClientIfPowerLevelLowRelativeThreshold_Object = MibTableColumn
clientIfPowerLevelLowRelativeThreshold = _ClientIfPowerLevelLowRelativeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 31),
    _ClientIfPowerLevelLowRelativeThreshold_Type()
)
clientIfPowerLevelLowRelativeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientIfPowerLevelLowRelativeThreshold.setStatus("current")
_ClientIfLossOfSignal_Type = FaultStatus
_ClientIfLossOfSignal_Object = MibTableColumn
clientIfLossOfSignal = _ClientIfLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 32),
    _ClientIfLossOfSignal_Type()
)
clientIfLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfLossOfSignal.setStatus("current")
_ClientIfLossOfFrame_Type = FaultStatus
_ClientIfLossOfFrame_Object = MibTableColumn
clientIfLossOfFrame = _ClientIfLossOfFrame_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 33),
    _ClientIfLossOfFrame_Type()
)
clientIfLossOfFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfLossOfFrame.setStatus("current")
_ClientIfBitrateMismatch_Type = FaultStatus
_ClientIfBitrateMismatch_Object = MibTableColumn
clientIfBitrateMismatch = _ClientIfBitrateMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 34),
    _ClientIfBitrateMismatch_Type()
)
clientIfBitrateMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfBitrateMismatch.setStatus("current")
_ClientIfAuAlarmIndicationSignalW2C_Type = FaultStatus
_ClientIfAuAlarmIndicationSignalW2C_Object = MibTableColumn
clientIfAuAlarmIndicationSignalW2C = _ClientIfAuAlarmIndicationSignalW2C_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 35),
    _ClientIfAuAlarmIndicationSignalW2C_Type()
)
clientIfAuAlarmIndicationSignalW2C.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfAuAlarmIndicationSignalW2C.setStatus("current")
_ClientIfTransmitterFailed_Type = FaultStatus
_ClientIfTransmitterFailed_Object = MibTableColumn
clientIfTransmitterFailed = _ClientIfTransmitterFailed_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 36),
    _ClientIfTransmitterFailed_Type()
)
clientIfTransmitterFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfTransmitterFailed.setStatus("current")
_ClientIfTrxCodeMismatch_Type = FaultStatus
_ClientIfTrxCodeMismatch_Object = MibTableColumn
clientIfTrxCodeMismatch = _ClientIfTrxCodeMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 37),
    _ClientIfTrxCodeMismatch_Type()
)
clientIfTrxCodeMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfTrxCodeMismatch.setStatus("current")
_ClientIfTrxBitrateUnavailable_Type = FaultStatus
_ClientIfTrxBitrateUnavailable_Object = MibTableColumn
clientIfTrxBitrateUnavailable = _ClientIfTrxBitrateUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 38),
    _ClientIfTrxBitrateUnavailable_Type()
)
clientIfTrxBitrateUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfTrxBitrateUnavailable.setStatus("current")
_ClientIfTrxMissing_Type = FaultStatus
_ClientIfTrxMissing_Object = MibTableColumn
clientIfTrxMissing = _ClientIfTrxMissing_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 39),
    _ClientIfTrxMissing_Type()
)
clientIfTrxMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfTrxMissing.setStatus("current")
_ClientIfReceivedPowerHigh_Type = FaultStatus
_ClientIfReceivedPowerHigh_Object = MibTableColumn
clientIfReceivedPowerHigh = _ClientIfReceivedPowerHigh_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 40),
    _ClientIfReceivedPowerHigh_Type()
)
clientIfReceivedPowerHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfReceivedPowerHigh.setStatus("current")
_ClientIfReceivedPowerLow_Type = FaultStatus
_ClientIfReceivedPowerLow_Object = MibTableColumn
clientIfReceivedPowerLow = _ClientIfReceivedPowerLow_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 41),
    _ClientIfReceivedPowerLow_Type()
)
clientIfReceivedPowerLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfReceivedPowerLow.setStatus("current")
_ClientIfLinkDown_Type = FaultStatus
_ClientIfLinkDown_Object = MibTableColumn
clientIfLinkDown = _ClientIfLinkDown_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 42),
    _ClientIfLinkDown_Type()
)
clientIfLinkDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfLinkDown.setStatus("current")
_ClientIfConfigurationCommand_Type = CommandString
_ClientIfConfigurationCommand_Object = MibTableColumn
clientIfConfigurationCommand = _ClientIfConfigurationCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 43),
    _ClientIfConfigurationCommand_Type()
)
clientIfConfigurationCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfConfigurationCommand.setStatus("current")


class _ClientIfGbeUtilization_Type(Unsigned32):
    """Custom type clientIfGbeUtilization based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
        ValueRangeConstraint(2147483646, 2147483646),
    )


_ClientIfGbeUtilization_Type.__name__ = "Unsigned32"
_ClientIfGbeUtilization_Object = MibTableColumn
clientIfGbeUtilization = _ClientIfGbeUtilization_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 44),
    _ClientIfGbeUtilization_Type()
)
clientIfGbeUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfGbeUtilization.setStatus("current")
_ClientIfLossOfSync_Type = FaultStatus
_ClientIfLossOfSync_Object = MibTableColumn
clientIfLossOfSync = _ClientIfLossOfSync_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 45),
    _ClientIfLossOfSync_Type()
)
clientIfLossOfSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfLossOfSync.setStatus("current")
_ClientIfConfigureTrxModeCommand_Type = CommandString
_ClientIfConfigureTrxModeCommand_Object = MibTableColumn
clientIfConfigureTrxModeCommand = _ClientIfConfigureTrxModeCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 46),
    _ClientIfConfigureTrxModeCommand_Type()
)
clientIfConfigureTrxModeCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfConfigureTrxModeCommand.setStatus("current")


class _ClientIfTrxMode_Type(Integer32):
    """Custom type clientIfTrxMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("client", 1),
          ("line", 2))
    )


_ClientIfTrxMode_Type.__name__ = "Integer32"
_ClientIfTrxMode_Object = MibTableColumn
clientIfTrxMode = _ClientIfTrxMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 47),
    _ClientIfTrxMode_Type()
)
clientIfTrxMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clientIfTrxMode.setStatus("current")


class _ClientIfExpectedTxFrequency_Type(LambdaFrequency):
    """Custom type clientIfExpectedTxFrequency based on LambdaFrequency"""
    defaultValue = 0


_ClientIfExpectedTxFrequency_Type.__name__ = "LambdaFrequency"
_ClientIfExpectedTxFrequency_Object = MibTableColumn
clientIfExpectedTxFrequency = _ClientIfExpectedTxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 48),
    _ClientIfExpectedTxFrequency_Type()
)
clientIfExpectedTxFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientIfExpectedTxFrequency.setStatus("current")
_ClientIfTxFrequency_Type = LambdaFrequency
_ClientIfTxFrequency_Object = MibTableColumn
clientIfTxFrequency = _ClientIfTxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 49),
    _ClientIfTxFrequency_Type()
)
clientIfTxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfTxFrequency.setStatus("current")
_ClientIfUnexpectedTxFrequency_Type = FaultStatus
_ClientIfUnexpectedTxFrequency_Object = MibTableColumn
clientIfUnexpectedTxFrequency = _ClientIfUnexpectedTxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 50),
    _ClientIfUnexpectedTxFrequency_Type()
)
clientIfUnexpectedTxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfUnexpectedTxFrequency.setStatus("current")
_ClientIfIllegalFrequency_Type = FaultStatus
_ClientIfIllegalFrequency_Object = MibTableColumn
clientIfIllegalFrequency = _ClientIfIllegalFrequency_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 51),
    _ClientIfIllegalFrequency_Type()
)
clientIfIllegalFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfIllegalFrequency.setStatus("current")


class _ClientIfLaserForcedOn_Type(Integer32):
    """Custom type clientIfLaserForcedOn based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ClientIfLaserForcedOn_Type.__name__ = "Integer32"
_ClientIfLaserForcedOn_Object = MibTableColumn
clientIfLaserForcedOn = _ClientIfLaserForcedOn_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 52),
    _ClientIfLaserForcedOn_Type()
)
clientIfLaserForcedOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientIfLaserForcedOn.setStatus("current")


class _ClientIfTrxMedia_Type(TrxMedia):
    """Custom type clientIfTrxMedia based on TrxMedia"""
    defaultValue = 1


_ClientIfTrxMedia_Type.__name__ = "TrxMedia"
_ClientIfTrxMedia_Object = MibTableColumn
clientIfTrxMedia = _ClientIfTrxMedia_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 53),
    _ClientIfTrxMedia_Type()
)
clientIfTrxMedia.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clientIfTrxMedia.setStatus("current")
_ClientIfTrxMediaMismatch_Type = FaultStatus
_ClientIfTrxMediaMismatch_Object = MibTableColumn
clientIfTrxMediaMismatch = _ClientIfTrxMediaMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 54),
    _ClientIfTrxMediaMismatch_Type()
)
clientIfTrxMediaMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfTrxMediaMismatch.setStatus("current")


class _ClientIfTruncAutoNegotiationMode_Type(Integer32):
    """Custom type clientIfTruncAutoNegotiationMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ClientIfTruncAutoNegotiationMode_Type.__name__ = "Integer32"
_ClientIfTruncAutoNegotiationMode_Object = MibTableColumn
clientIfTruncAutoNegotiationMode = _ClientIfTruncAutoNegotiationMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 55),
    _ClientIfTruncAutoNegotiationMode_Type()
)
clientIfTruncAutoNegotiationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientIfTruncAutoNegotiationMode.setStatus("current")
_ClientIfObjectProperty_Type = ObjectProperty
_ClientIfObjectProperty_Object = MibTableColumn
clientIfObjectProperty = _ClientIfObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 56),
    _ClientIfObjectProperty_Type()
)
clientIfObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfObjectProperty.setStatus("current")
_ClientIfTxPowerLevel_Type = Integer32
_ClientIfTxPowerLevel_Object = MibTableColumn
clientIfTxPowerLevel = _ClientIfTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 57),
    _ClientIfTxPowerLevel_Type()
)
clientIfTxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfTxPowerLevel.setStatus("current")
_ClientIfLaserTempActual_Type = Integer32
_ClientIfLaserTempActual_Object = MibTableColumn
clientIfLaserTempActual = _ClientIfLaserTempActual_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 58),
    _ClientIfLaserTempActual_Type()
)
clientIfLaserTempActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfLaserTempActual.setStatus("current")


class _ClientIfTraceIntrusionMode_Type(Integer32):
    """Custom type clientIfTraceIntrusionMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ClientIfTraceIntrusionMode_Type.__name__ = "Integer32"
_ClientIfTraceIntrusionMode_Object = MibTableColumn
clientIfTraceIntrusionMode = _ClientIfTraceIntrusionMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 59),
    _ClientIfTraceIntrusionMode_Type()
)
clientIfTraceIntrusionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientIfTraceIntrusionMode.setStatus("current")


class _ClientIfTraceTransmitted_Type(DisplayString):
    """Custom type clientIfTraceTransmitted based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 62),
    )


_ClientIfTraceTransmitted_Type.__name__ = "DisplayString"
_ClientIfTraceTransmitted_Object = MibTableColumn
clientIfTraceTransmitted = _ClientIfTraceTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 60),
    _ClientIfTraceTransmitted_Type()
)
clientIfTraceTransmitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientIfTraceTransmitted.setStatus("current")


class _ClientIfTraceReceived_Type(DisplayString):
    """Custom type clientIfTraceReceived based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 62),
    )


_ClientIfTraceReceived_Type.__name__ = "DisplayString"
_ClientIfTraceReceived_Object = MibTableColumn
clientIfTraceReceived = _ClientIfTraceReceived_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 61),
    _ClientIfTraceReceived_Type()
)
clientIfTraceReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfTraceReceived.setStatus("current")


class _ClientIfTraceExpected_Type(DisplayString):
    """Custom type clientIfTraceExpected based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 62),
    )


_ClientIfTraceExpected_Type.__name__ = "DisplayString"
_ClientIfTraceExpected_Object = MibTableColumn
clientIfTraceExpected = _ClientIfTraceExpected_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 62),
    _ClientIfTraceExpected_Type()
)
clientIfTraceExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientIfTraceExpected.setStatus("current")


class _ClientIfTraceAlarmMode_Type(Integer32):
    """Custom type clientIfTraceAlarmMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ClientIfTraceAlarmMode_Type.__name__ = "Integer32"
_ClientIfTraceAlarmMode_Object = MibTableColumn
clientIfTraceAlarmMode = _ClientIfTraceAlarmMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 63),
    _ClientIfTraceAlarmMode_Type()
)
clientIfTraceAlarmMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientIfTraceAlarmMode.setStatus("current")
_ClientIfTraceMismatch_Type = FaultStatus
_ClientIfTraceMismatch_Object = MibTableColumn
clientIfTraceMismatch = _ClientIfTraceMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 64),
    _ClientIfTraceMismatch_Type()
)
clientIfTraceMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfTraceMismatch.setStatus("current")


class _ClientIfNearEndLoopback_Type(Integer32):
    """Custom type clientIfNearEndLoopback based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ClientIfNearEndLoopback_Type.__name__ = "Integer32"
_ClientIfNearEndLoopback_Object = MibTableColumn
clientIfNearEndLoopback = _ClientIfNearEndLoopback_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 65),
    _ClientIfNearEndLoopback_Type()
)
clientIfNearEndLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientIfNearEndLoopback.setStatus("current")


class _ClientIfRxSignalStatus_Type(SignalStatusWithNA):
    """Custom type clientIfRxSignalStatus based on SignalStatusWithNA"""
    defaultValue = 1


_ClientIfRxSignalStatus_Type.__name__ = "SignalStatusWithNA"
_ClientIfRxSignalStatus_Object = MibTableColumn
clientIfRxSignalStatus = _ClientIfRxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 66),
    _ClientIfRxSignalStatus_Type()
)
clientIfRxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfRxSignalStatus.setStatus("current")
_ClientIfMsAlarmIndicationSignalC2W_Type = FaultStatus
_ClientIfMsAlarmIndicationSignalC2W_Object = MibTableColumn
clientIfMsAlarmIndicationSignalC2W = _ClientIfMsAlarmIndicationSignalC2W_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 67),
    _ClientIfMsAlarmIndicationSignalC2W_Type()
)
clientIfMsAlarmIndicationSignalC2W.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfMsAlarmIndicationSignalC2W.setStatus("current")
_ClientIfMsAlarmIndicationSignalW2C_Type = FaultStatus
_ClientIfMsAlarmIndicationSignalW2C_Object = MibTableColumn
clientIfMsAlarmIndicationSignalW2C = _ClientIfMsAlarmIndicationSignalW2C_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 68),
    _ClientIfMsAlarmIndicationSignalW2C_Type()
)
clientIfMsAlarmIndicationSignalW2C.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfMsAlarmIndicationSignalW2C.setStatus("current")
_ClientIfRemoteDefectIndication_Type = FaultStatus
_ClientIfRemoteDefectIndication_Object = MibTableColumn
clientIfRemoteDefectIndication = _ClientIfRemoteDefectIndication_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 69),
    _ClientIfRemoteDefectIndication_Type()
)
clientIfRemoteDefectIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfRemoteDefectIndication.setStatus("current")


class _ClientIfJ1TxTrailTrace_Type(DisplayString):
    """Custom type clientIfJ1TxTrailTrace based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ClientIfJ1TxTrailTrace_Type.__name__ = "DisplayString"
_ClientIfJ1TxTrailTrace_Object = MibTableColumn
clientIfJ1TxTrailTrace = _ClientIfJ1TxTrailTrace_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 70),
    _ClientIfJ1TxTrailTrace_Type()
)
clientIfJ1TxTrailTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientIfJ1TxTrailTrace.setStatus("current")


class _ClientIfJ1TxTrailTraceInsertionMode_Type(Integer32):
    """Custom type clientIfJ1TxTrailTraceInsertionMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vcGroupLevel", 1),
          ("individualVcLevel", 2))
    )


_ClientIfJ1TxTrailTraceInsertionMode_Type.__name__ = "Integer32"
_ClientIfJ1TxTrailTraceInsertionMode_Object = MibTableColumn
clientIfJ1TxTrailTraceInsertionMode = _ClientIfJ1TxTrailTraceInsertionMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 71),
    _ClientIfJ1TxTrailTraceInsertionMode_Type()
)
clientIfJ1TxTrailTraceInsertionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientIfJ1TxTrailTraceInsertionMode.setStatus("current")
_ClientIfTrxFailed_Type = FaultStatus
_ClientIfTrxFailed_Object = MibTableColumn
clientIfTrxFailed = _ClientIfTrxFailed_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 72),
    _ClientIfTrxFailed_Type()
)
clientIfTrxFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfTrxFailed.setStatus("current")
_ClientIfDisabled_Type = FaultStatus
_ClientIfDisabled_Object = MibTableColumn
clientIfDisabled = _ClientIfDisabled_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 73),
    _ClientIfDisabled_Type()
)
clientIfDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfDisabled.setStatus("current")
_ClientIfLoopback_Type = FaultStatus
_ClientIfLoopback_Object = MibTableColumn
clientIfLoopback = _ClientIfLoopback_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 74),
    _ClientIfLoopback_Type()
)
clientIfLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfLoopback.setStatus("current")
_ClientIfVcGroupFailedW2C_Type = FaultStatus
_ClientIfVcGroupFailedW2C_Object = MibTableColumn
clientIfVcGroupFailedW2C = _ClientIfVcGroupFailedW2C_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 75),
    _ClientIfVcGroupFailedW2C_Type()
)
clientIfVcGroupFailedW2C.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfVcGroupFailedW2C.setStatus("current")
_ClientIfReadJ1_Type = CommandString
_ClientIfReadJ1_Object = MibTableColumn
clientIfReadJ1 = _ClientIfReadJ1_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 76),
    _ClientIfReadJ1_Type()
)
clientIfReadJ1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfReadJ1.setStatus("current")
_ClientIfClientSignalFailed_Type = FaultStatus
_ClientIfClientSignalFailed_Object = MibTableColumn
clientIfClientSignalFailed = _ClientIfClientSignalFailed_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 77),
    _ClientIfClientSignalFailed_Type()
)
clientIfClientSignalFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfClientSignalFailed.setStatus("current")
_ClientIfAuLossOfPointer_Type = FaultStatus
_ClientIfAuLossOfPointer_Object = MibTableColumn
clientIfAuLossOfPointer = _ClientIfAuLossOfPointer_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 78),
    _ClientIfAuLossOfPointer_Type()
)
clientIfAuLossOfPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfAuLossOfPointer.setStatus("current")
_ClientIfGfpLossOfFrame_Type = FaultStatus
_ClientIfGfpLossOfFrame_Object = MibTableColumn
clientIfGfpLossOfFrame = _ClientIfGfpLossOfFrame_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 79),
    _ClientIfGfpLossOfFrame_Type()
)
clientIfGfpLossOfFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfGfpLossOfFrame.setStatus("current")


class _ClientIfHighSpeed_Type(Gauge32):
    """Custom type clientIfHighSpeed based on Gauge32"""
    defaultValue = 125000

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(12500, 491520),
    )


_ClientIfHighSpeed_Type.__name__ = "Gauge32"
_ClientIfHighSpeed_Object = MibTableColumn
clientIfHighSpeed = _ClientIfHighSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 80),
    _ClientIfHighSpeed_Type()
)
clientIfHighSpeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clientIfHighSpeed.setStatus("current")


class _ClientIfActualFormat_Type(SignalFormat):
    """Custom type clientIfActualFormat based on SignalFormat"""
    defaultValue = 10


_ClientIfActualFormat_Type.__name__ = "SignalFormat"
_ClientIfActualFormat_Object = MibTableColumn
clientIfActualFormat = _ClientIfActualFormat_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 81),
    _ClientIfActualFormat_Type()
)
clientIfActualFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfActualFormat.setStatus("current")


class _ClientIfRdiIntrusionMode_Type(Integer32):
    """Custom type clientIfRdiIntrusionMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ClientIfRdiIntrusionMode_Type.__name__ = "Integer32"
_ClientIfRdiIntrusionMode_Object = MibTableColumn
clientIfRdiIntrusionMode = _ClientIfRdiIntrusionMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 82),
    _ClientIfRdiIntrusionMode_Type()
)
clientIfRdiIntrusionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfRdiIntrusionMode.setStatus("current")


class _ClientIfMuxQuadVc4_Type(Unsigned32):
    """Custom type clientIfMuxQuadVc4 based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ClientIfMuxQuadVc4_Type.__name__ = "Unsigned32"
_ClientIfMuxQuadVc4_Object = MibTableColumn
clientIfMuxQuadVc4 = _ClientIfMuxQuadVc4_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 83),
    _ClientIfMuxQuadVc4_Type()
)
clientIfMuxQuadVc4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clientIfMuxQuadVc4.setStatus("current")


class _ClientIfDemuxQuadVc4_Type(Unsigned32):
    """Custom type clientIfDemuxQuadVc4 based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ClientIfDemuxQuadVc4_Type.__name__ = "Unsigned32"
_ClientIfDemuxQuadVc4_Object = MibTableColumn
clientIfDemuxQuadVc4 = _ClientIfDemuxQuadVc4_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 84),
    _ClientIfDemuxQuadVc4_Type()
)
clientIfDemuxQuadVc4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clientIfDemuxQuadVc4.setStatus("current")


class _ClientIfCcConnectionMode_Type(Integer32):
    """Custom type clientIfCcConnectionMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("disconnected", 2))
    )


_ClientIfCcConnectionMode_Type.__name__ = "Integer32"
_ClientIfCcConnectionMode_Object = MibTableColumn
clientIfCcConnectionMode = _ClientIfCcConnectionMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 85),
    _ClientIfCcConnectionMode_Type()
)
clientIfCcConnectionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clientIfCcConnectionMode.setStatus("current")
_ClientIfCcConfigurationCommand_Type = CommandString
_ClientIfCcConfigurationCommand_Object = MibTableColumn
clientIfCcConfigurationCommand = _ClientIfCcConfigurationCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 86),
    _ClientIfCcConfigurationCommand_Type()
)
clientIfCcConfigurationCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfCcConfigurationCommand.setStatus("current")
_ClientIfIllegalSignalFormat_Type = FaultStatus
_ClientIfIllegalSignalFormat_Object = MibTableColumn
clientIfIllegalSignalFormat = _ClientIfIllegalSignalFormat_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 87),
    _ClientIfIllegalSignalFormat_Type()
)
clientIfIllegalSignalFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfIllegalSignalFormat.setStatus("current")


class _ClientIfSynchProtPortId_Type(Integer32):
    """Custom type clientIfSynchProtPortId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("portA", 1),
          ("portB", 2))
    )


_ClientIfSynchProtPortId_Type.__name__ = "Integer32"
_ClientIfSynchProtPortId_Object = MibTableColumn
clientIfSynchProtPortId = _ClientIfSynchProtPortId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 88),
    _ClientIfSynchProtPortId_Type()
)
clientIfSynchProtPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfSynchProtPortId.setStatus("current")


class _ClientIfSynchProtGroupMemberPort_Type(PortNumber):
    """Custom type clientIfSynchProtGroupMemberPort based on PortNumber"""
    defaultValue = 0


_ClientIfSynchProtGroupMemberPort_Type.__name__ = "PortNumber"
_ClientIfSynchProtGroupMemberPort_Object = MibTableColumn
clientIfSynchProtGroupMemberPort = _ClientIfSynchProtGroupMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 89),
    _ClientIfSynchProtGroupMemberPort_Type()
)
clientIfSynchProtGroupMemberPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfSynchProtGroupMemberPort.setStatus("current")


class _ClientIfSynchProtGroupStatus_Type(Integer32):
    """Custom type clientIfSynchProtGroupStatus based on Integer32"""
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
        *(("bothDown", 1),
          ("bothUp", 2),
          ("portADownBUp", 3),
          ("portAUpBDown", 4))
    )


_ClientIfSynchProtGroupStatus_Type.__name__ = "Integer32"
_ClientIfSynchProtGroupStatus_Object = MibTableColumn
clientIfSynchProtGroupStatus = _ClientIfSynchProtGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 90),
    _ClientIfSynchProtGroupStatus_Type()
)
clientIfSynchProtGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfSynchProtGroupStatus.setStatus("current")


class _ClientIfSynchProtActivePort_Type(Integer32):
    """Custom type clientIfSynchProtActivePort based on Integer32"""
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
        *(("none", 1),
          ("portA", 2),
          ("portB", 3))
    )


_ClientIfSynchProtActivePort_Type.__name__ = "Integer32"
_ClientIfSynchProtActivePort_Object = MibTableColumn
clientIfSynchProtActivePort = _ClientIfSynchProtActivePort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 91),
    _ClientIfSynchProtActivePort_Type()
)
clientIfSynchProtActivePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfSynchProtActivePort.setStatus("current")


class _ClientIfSynchProtPortStatus_Type(Integer32):
    """Custom type clientIfSynchProtPortStatus based on Integer32"""
    defaultValue = 1

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


_ClientIfSynchProtPortStatus_Type.__name__ = "Integer32"
_ClientIfSynchProtPortStatus_Object = MibTableColumn
clientIfSynchProtPortStatus = _ClientIfSynchProtPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 92),
    _ClientIfSynchProtPortStatus_Type()
)
clientIfSynchProtPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfSynchProtPortStatus.setStatus("current")
_ClientIfSynchProtToggleActivePort_Type = CommandString
_ClientIfSynchProtToggleActivePort_Object = MibTableColumn
clientIfSynchProtToggleActivePort = _ClientIfSynchProtToggleActivePort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 93),
    _ClientIfSynchProtToggleActivePort_Type()
)
clientIfSynchProtToggleActivePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfSynchProtToggleActivePort.setStatus("current")


class _ClientIfNearEndLoopbackTimeout_Type(Integer32):
    """Custom type clientIfNearEndLoopbackTimeout based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1200),
    )


_ClientIfNearEndLoopbackTimeout_Type.__name__ = "Integer32"
_ClientIfNearEndLoopbackTimeout_Object = MibTableColumn
clientIfNearEndLoopbackTimeout = _ClientIfNearEndLoopbackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 94),
    _ClientIfNearEndLoopbackTimeout_Type()
)
clientIfNearEndLoopbackTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clientIfNearEndLoopbackTimeout.setStatus("current")
_ClientIfNearEndLoopbackEnabled_Type = FaultStatus
_ClientIfNearEndLoopbackEnabled_Object = MibTableColumn
clientIfNearEndLoopbackEnabled = _ClientIfNearEndLoopbackEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 95),
    _ClientIfNearEndLoopbackEnabled_Type()
)
clientIfNearEndLoopbackEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfNearEndLoopbackEnabled.setStatus("current")
_ClientIfChangeNearEndLoopbackCommand_Type = CommandString
_ClientIfChangeNearEndLoopbackCommand_Object = MibTableColumn
clientIfChangeNearEndLoopbackCommand = _ClientIfChangeNearEndLoopbackCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 96),
    _ClientIfChangeNearEndLoopbackCommand_Type()
)
clientIfChangeNearEndLoopbackCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfChangeNearEndLoopbackCommand.setStatus("current")
_ClientIfFarEndLoopbackEnabled_Type = FaultStatus
_ClientIfFarEndLoopbackEnabled_Object = MibTableColumn
clientIfFarEndLoopbackEnabled = _ClientIfFarEndLoopbackEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 97),
    _ClientIfFarEndLoopbackEnabled_Type()
)
clientIfFarEndLoopbackEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfFarEndLoopbackEnabled.setStatus("current")


class _ClientIfFarEndLoopbackTimeout_Type(Integer32):
    """Custom type clientIfFarEndLoopbackTimeout based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1200),
    )


_ClientIfFarEndLoopbackTimeout_Type.__name__ = "Integer32"
_ClientIfFarEndLoopbackTimeout_Object = MibTableColumn
clientIfFarEndLoopbackTimeout = _ClientIfFarEndLoopbackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 98),
    _ClientIfFarEndLoopbackTimeout_Type()
)
clientIfFarEndLoopbackTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clientIfFarEndLoopbackTimeout.setStatus("current")
_ClientIfChangeFarEndLoopbackCommand_Type = CommandString
_ClientIfChangeFarEndLoopbackCommand_Object = MibTableColumn
clientIfChangeFarEndLoopbackCommand = _ClientIfChangeFarEndLoopbackCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 99),
    _ClientIfChangeFarEndLoopbackCommand_Type()
)
clientIfChangeFarEndLoopbackCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfChangeFarEndLoopbackCommand.setStatus("current")
_ClientIfFormatNotSupportedByHw_Type = FaultStatus
_ClientIfFormatNotSupportedByHw_Object = MibTableColumn
clientIfFormatNotSupportedByHw = _ClientIfFormatNotSupportedByHw_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 100),
    _ClientIfFormatNotSupportedByHw_Type()
)
clientIfFormatNotSupportedByHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfFormatNotSupportedByHw.setStatus("current")


class _ClientIfLaserMode_Type(Integer32):
    """Custom type clientIfLaserMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("als", 2))
    )


_ClientIfLaserMode_Type.__name__ = "Integer32"
_ClientIfLaserMode_Object = MibTableColumn
clientIfLaserMode = _ClientIfLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 101),
    _ClientIfLaserMode_Type()
)
clientIfLaserMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientIfLaserMode.setStatus("current")
_ClientIfAlarmIndicationSignalLineC2W_Type = FaultStatus
_ClientIfAlarmIndicationSignalLineC2W_Object = MibTableColumn
clientIfAlarmIndicationSignalLineC2W = _ClientIfAlarmIndicationSignalLineC2W_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 102),
    _ClientIfAlarmIndicationSignalLineC2W_Type()
)
clientIfAlarmIndicationSignalLineC2W.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfAlarmIndicationSignalLineC2W.setStatus("current")
_ClientIfFarEndClientFailure_Type = FaultStatus
_ClientIfFarEndClientFailure_Object = MibTableColumn
clientIfFarEndClientFailure = _ClientIfFarEndClientFailure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 103),
    _ClientIfFarEndClientFailure_Type()
)
clientIfFarEndClientFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfFarEndClientFailure.setStatus("current")


class _ClientIfOHTransparency_Type(Integer32):
    """Custom type clientIfOHTransparency based on Integer32"""
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


_ClientIfOHTransparency_Type.__name__ = "Integer32"
_ClientIfOHTransparency_Object = MibTableColumn
clientIfOHTransparency = _ClientIfOHTransparency_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 104),
    _ClientIfOHTransparency_Type()
)
clientIfOHTransparency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientIfOHTransparency.setStatus("current")


class _ClientIfConnectedLine_Type(Unsigned32):
    """Custom type clientIfConnectedLine based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ClientIfConnectedLine_Type.__name__ = "Unsigned32"
_ClientIfConnectedLine_Object = MibTableColumn
clientIfConnectedLine = _ClientIfConnectedLine_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 105),
    _ClientIfConnectedLine_Type()
)
clientIfConnectedLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfConnectedLine.setStatus("current")


class _ClientIfForwardingErrorCorrectionMode_Type(Integer32):
    """Custom type clientIfForwardingErrorCorrectionMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("auto", 3))
    )


_ClientIfForwardingErrorCorrectionMode_Type.__name__ = "Integer32"
_ClientIfForwardingErrorCorrectionMode_Object = MibTableColumn
clientIfForwardingErrorCorrectionMode = _ClientIfForwardingErrorCorrectionMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 106),
    _ClientIfForwardingErrorCorrectionMode_Type()
)
clientIfForwardingErrorCorrectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientIfForwardingErrorCorrectionMode.setStatus("current")
_ClientIfNoFrequencySet_Type = FaultStatus
_ClientIfNoFrequencySet_Object = MibTableColumn
clientIfNoFrequencySet = _ClientIfNoFrequencySet_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 107),
    _ClientIfNoFrequencySet_Type()
)
clientIfNoFrequencySet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfNoFrequencySet.setStatus("current")


class _ClientIfJitterAttenuatorBW_Type(Integer32):
    """Custom type clientIfJitterAttenuatorBW based on Integer32"""
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
        *(("option1", 0),
          ("option2", 1),
          ("notUsed", 2))
    )


_ClientIfJitterAttenuatorBW_Type.__name__ = "Integer32"
_ClientIfJitterAttenuatorBW_Object = MibTableColumn
clientIfJitterAttenuatorBW = _ClientIfJitterAttenuatorBW_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 108),
    _ClientIfJitterAttenuatorBW_Type()
)
clientIfJitterAttenuatorBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientIfJitterAttenuatorBW.setStatus("current")


class _ClientIfConnectionStatus_Type(DisplayString):
    """Custom type clientIfConnectionStatus based on DisplayString"""
    defaultValue = OctetString("Not connected")


_ClientIfConnectionStatus_Type.__name__ = "DisplayString"
_ClientIfConnectionStatus_Object = MibTableColumn
clientIfConnectionStatus = _ClientIfConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 109),
    _ClientIfConnectionStatus_Type()
)
clientIfConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfConnectionStatus.setStatus("current")
_ClientIfLoopFilterUnlocked_Type = FaultStatus
_ClientIfLoopFilterUnlocked_Object = MibTableColumn
clientIfLoopFilterUnlocked = _ClientIfLoopFilterUnlocked_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 110),
    _ClientIfLoopFilterUnlocked_Type()
)
clientIfLoopFilterUnlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfLoopFilterUnlocked.setStatus("current")


class _ClientIfCableLength_Type(Integer32):
    """Custom type clientIfCableLength based on Integer32"""
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
        *(("feet133", 0),
          ("feet266", 1),
          ("feet399", 2),
          ("feet533", 3),
          ("feet655", 4))
    )


_ClientIfCableLength_Type.__name__ = "Integer32"
_ClientIfCableLength_Object = MibTableColumn
clientIfCableLength = _ClientIfCableLength_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 111),
    _ClientIfCableLength_Type()
)
clientIfCableLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientIfCableLength.setStatus("current")


class _ClientIfConnectedForeignIndex_Type(Unsigned32):
    """Custom type clientIfConnectedForeignIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ClientIfConnectedForeignIndex_Type.__name__ = "Unsigned32"
_ClientIfConnectedForeignIndex_Object = MibTableColumn
clientIfConnectedForeignIndex = _ClientIfConnectedForeignIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 112),
    _ClientIfConnectedForeignIndex_Type()
)
clientIfConnectedForeignIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientIfConnectedForeignIndex.setStatus("current")
_ClientIfDisconnect_Type = CommandString
_ClientIfDisconnect_Object = MibTableColumn
clientIfDisconnect = _ClientIfDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 113),
    _ClientIfDisconnect_Type()
)
clientIfDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfDisconnect.setStatus("current")


class _ClientIfOHTransparencyBitMask_Type(Unsigned32):
    """Custom type clientIfOHTransparencyBitMask based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ClientIfOHTransparencyBitMask_Type.__name__ = "Unsigned32"
_ClientIfOHTransparencyBitMask_Object = MibTableColumn
clientIfOHTransparencyBitMask = _ClientIfOHTransparencyBitMask_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 114),
    _ClientIfOHTransparencyBitMask_Type()
)
clientIfOHTransparencyBitMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clientIfOHTransparencyBitMask.setStatus("current")


class _ClientIfOHTransparencyString_Type(DisplayString):
    """Custom type clientIfOHTransparencyString based on DisplayString"""
    defaultValue = OctetString("")


_ClientIfOHTransparencyString_Type.__name__ = "DisplayString"
_ClientIfOHTransparencyString_Object = MibTableColumn
clientIfOHTransparencyString = _ClientIfOHTransparencyString_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 115),
    _ClientIfOHTransparencyString_Type()
)
clientIfOHTransparencyString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfOHTransparencyString.setStatus("current")
_ClientIfOHTransparencySet_Type = CommandString
_ClientIfOHTransparencySet_Object = MibTableColumn
clientIfOHTransparencySet = _ClientIfOHTransparencySet_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 116),
    _ClientIfOHTransparencySet_Type()
)
clientIfOHTransparencySet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfOHTransparencySet.setStatus("current")
_ClientIfAuAlarmIndicationSignalC2W_Type = FaultStatus
_ClientIfAuAlarmIndicationSignalC2W_Object = MibTableColumn
clientIfAuAlarmIndicationSignalC2W = _ClientIfAuAlarmIndicationSignalC2W_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 117),
    _ClientIfAuAlarmIndicationSignalC2W_Type()
)
clientIfAuAlarmIndicationSignalC2W.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfAuAlarmIndicationSignalC2W.setStatus("current")
_ClientIfAuLossOfPointerC2W_Type = FaultStatus
_ClientIfAuLossOfPointerC2W_Object = MibTableColumn
clientIfAuLossOfPointerC2W = _ClientIfAuLossOfPointerC2W_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 118),
    _ClientIfAuLossOfPointerC2W_Type()
)
clientIfAuLossOfPointerC2W.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfAuLossOfPointerC2W.setStatus("current")
_ClientIfAuLossOfPointerW2C_Type = FaultStatus
_ClientIfAuLossOfPointerW2C_Object = MibTableColumn
clientIfAuLossOfPointerW2C = _ClientIfAuLossOfPointerW2C_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 119),
    _ClientIfAuLossOfPointerW2C_Type()
)
clientIfAuLossOfPointerW2C.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfAuLossOfPointerW2C.setStatus("current")


class _ClientIfEthStandbyIndicator_Type(Integer32):
    """Custom type clientIfEthStandbyIndicator based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ClientIfEthStandbyIndicator_Type.__name__ = "Integer32"
_ClientIfEthStandbyIndicator_Object = MibTableColumn
clientIfEthStandbyIndicator = _ClientIfEthStandbyIndicator_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 120),
    _ClientIfEthStandbyIndicator_Type()
)
clientIfEthStandbyIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfEthStandbyIndicator.setStatus("current")
_ClientIfAuAlarmIndicationSignalW2CSonet_Type = FaultStatus
_ClientIfAuAlarmIndicationSignalW2CSonet_Object = MibTableColumn
clientIfAuAlarmIndicationSignalW2CSonet = _ClientIfAuAlarmIndicationSignalW2CSonet_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 121),
    _ClientIfAuAlarmIndicationSignalW2CSonet_Type()
)
clientIfAuAlarmIndicationSignalW2CSonet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfAuAlarmIndicationSignalW2CSonet.setStatus("current")
_ClientIfAuAlarmIndicationSignalC2WSonet_Type = FaultStatus
_ClientIfAuAlarmIndicationSignalC2WSonet_Object = MibTableColumn
clientIfAuAlarmIndicationSignalC2WSonet = _ClientIfAuAlarmIndicationSignalC2WSonet_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 122),
    _ClientIfAuAlarmIndicationSignalC2WSonet_Type()
)
clientIfAuAlarmIndicationSignalC2WSonet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfAuAlarmIndicationSignalC2WSonet.setStatus("current")
_ClientIfAuLossOfPointerC2WSonet_Type = FaultStatus
_ClientIfAuLossOfPointerC2WSonet_Object = MibTableColumn
clientIfAuLossOfPointerC2WSonet = _ClientIfAuLossOfPointerC2WSonet_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 123),
    _ClientIfAuLossOfPointerC2WSonet_Type()
)
clientIfAuLossOfPointerC2WSonet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfAuLossOfPointerC2WSonet.setStatus("current")
_ClientIfAuLossOfPointerW2CSonet_Type = FaultStatus
_ClientIfAuLossOfPointerW2CSonet_Object = MibTableColumn
clientIfAuLossOfPointerW2CSonet = _ClientIfAuLossOfPointerW2CSonet_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 124),
    _ClientIfAuLossOfPointerW2CSonet_Type()
)
clientIfAuLossOfPointerW2CSonet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfAuLossOfPointerW2CSonet.setStatus("current")
_ClientIfTransceiverNoLoopback_Type = FaultStatus
_ClientIfTransceiverNoLoopback_Object = MibTableColumn
clientIfTransceiverNoLoopback = _ClientIfTransceiverNoLoopback_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 125),
    _ClientIfTransceiverNoLoopback_Type()
)
clientIfTransceiverNoLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfTransceiverNoLoopback.setStatus("current")
_ClientIfFecFailure_Type = FaultStatus
_ClientIfFecFailure_Object = MibTableColumn
clientIfFecFailure = _ClientIfFecFailure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 126),
    _ClientIfFecFailure_Type()
)
clientIfFecFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfFecFailure.setStatus("current")
_ClientIfLaneAlignmentError_Type = FaultStatus
_ClientIfLaneAlignmentError_Object = MibTableColumn
clientIfLaneAlignmentError = _ClientIfLaneAlignmentError_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 127),
    _ClientIfLaneAlignmentError_Type()
)
clientIfLaneAlignmentError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfLaneAlignmentError.setStatus("current")
_ClientIfFecCorrectedZeros_Type = Unsigned32
_ClientIfFecCorrectedZeros_Object = MibTableColumn
clientIfFecCorrectedZeros = _ClientIfFecCorrectedZeros_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 128),
    _ClientIfFecCorrectedZeros_Type()
)
clientIfFecCorrectedZeros.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfFecCorrectedZeros.setStatus("current")
_ClientIfFecCorrectedOnes_Type = Unsigned32
_ClientIfFecCorrectedOnes_Object = MibTableColumn
clientIfFecCorrectedOnes = _ClientIfFecCorrectedOnes_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 129),
    _ClientIfFecCorrectedOnes_Type()
)
clientIfFecCorrectedOnes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfFecCorrectedOnes.setStatus("current")
_ClientIfSignalDegraded_Type = FaultStatus
_ClientIfSignalDegraded_Object = MibTableColumn
clientIfSignalDegraded = _ClientIfSignalDegraded_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 130),
    _ClientIfSignalDegraded_Type()
)
clientIfSignalDegraded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfSignalDegraded.setStatus("current")


class _ClientIfFecType_Type(Integer32):
    """Custom type clientIfFecType based on Integer32"""
    defaultValue = 1

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
        *(("disabled", 1),
          ("gFec", 2),
          ("superFecI4", 3),
          ("superFecI7", 4),
          ("sdFec", 5))
    )


_ClientIfFecType_Type.__name__ = "Integer32"
_ClientIfFecType_Object = MibTableColumn
clientIfFecType = _ClientIfFecType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 131),
    _ClientIfFecType_Type()
)
clientIfFecType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientIfFecType.setStatus("current")


class _ClientIfSignalDegradeThreshold_Type(BerLevelMTOSI):
    """Custom type clientIfSignalDegradeThreshold based on BerLevelMTOSI"""
    defaultValue = 13


_ClientIfSignalDegradeThreshold_Type.__name__ = "BerLevelMTOSI"
_ClientIfSignalDegradeThreshold_Object = MibTableColumn
clientIfSignalDegradeThreshold = _ClientIfSignalDegradeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 132),
    _ClientIfSignalDegradeThreshold_Type()
)
clientIfSignalDegradeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientIfSignalDegradeThreshold.setStatus("current")


class _ClientIfExpectedOpticalLayerMapping_Type(OpticalLayerMappingType):
    """Custom type clientIfExpectedOpticalLayerMapping based on OpticalLayerMappingType"""
    defaultValue = 3


_ClientIfExpectedOpticalLayerMapping_Type.__name__ = "OpticalLayerMappingType"
_ClientIfExpectedOpticalLayerMapping_Object = MibTableColumn
clientIfExpectedOpticalLayerMapping = _ClientIfExpectedOpticalLayerMapping_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 133),
    _ClientIfExpectedOpticalLayerMapping_Type()
)
clientIfExpectedOpticalLayerMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientIfExpectedOpticalLayerMapping.setStatus("current")
_ClientIfActualOpticalLayerMapping_Type = OpticalLayerMappingType
_ClientIfActualOpticalLayerMapping_Object = MibTableColumn
clientIfActualOpticalLayerMapping = _ClientIfActualOpticalLayerMapping_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 134),
    _ClientIfActualOpticalLayerMapping_Type()
)
clientIfActualOpticalLayerMapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfActualOpticalLayerMapping.setStatus("current")
_ClientIfConfigurationMismatch_Type = FaultStatus
_ClientIfConfigurationMismatch_Object = MibTableColumn
clientIfConfigurationMismatch = _ClientIfConfigurationMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 135),
    _ClientIfConfigurationMismatch_Type()
)
clientIfConfigurationMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfConfigurationMismatch.setStatus("current")
_ClientIfChromaticDispersion_Type = Integer32
_ClientIfChromaticDispersion_Object = MibTableColumn
clientIfChromaticDispersion = _ClientIfChromaticDispersion_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 136),
    _ClientIfChromaticDispersion_Type()
)
clientIfChromaticDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfChromaticDispersion.setStatus("current")
_ClientIfDifferentialGroupDelay_Type = Unsigned32
_ClientIfDifferentialGroupDelay_Object = MibTableColumn
clientIfDifferentialGroupDelay = _ClientIfDifferentialGroupDelay_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 137),
    _ClientIfDifferentialGroupDelay_Type()
)
clientIfDifferentialGroupDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfDifferentialGroupDelay.setStatus("current")
_ClientIfTxState_Type = TrxTxState
_ClientIfTxState_Object = MibTableColumn
clientIfTxState = _ClientIfTxState_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 138),
    _ClientIfTxState_Type()
)
clientIfTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfTxState.setStatus("current")
_ClientIfRxState_Type = TrxRxState
_ClientIfRxState_Object = MibTableColumn
clientIfRxState = _ClientIfRxState_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 139),
    _ClientIfRxState_Type()
)
clientIfRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfRxState.setStatus("current")


class _ClientIfIdx_Type(Integer32):
    """Custom type clientIfIdx based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_ClientIfIdx_Type.__name__ = "Integer32"
_ClientIfIdx_Object = MibTableColumn
clientIfIdx = _ClientIfIdx_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 140),
    _ClientIfIdx_Type()
)
clientIfIdx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clientIfIdx.setStatus("current")


class _ClientIfIfNo_Type(PortNumber):
    """Custom type clientIfIfNo based on PortNumber"""
    defaultValue = 1


_ClientIfIfNo_Type.__name__ = "PortNumber"
_ClientIfIfNo_Object = MibTableColumn
clientIfIfNo = _ClientIfIfNo_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 141),
    _ClientIfIfNo_Type()
)
clientIfIfNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clientIfIfNo.setStatus("current")


class _ClientIfIdxIf_Type(Integer32):
    """Custom type clientIfIdxIf based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_ClientIfIdxIf_Type.__name__ = "Integer32"
_ClientIfIdxIf_Object = MibTableColumn
clientIfIdxIf = _ClientIfIdxIf_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 142),
    _ClientIfIdxIf_Type()
)
clientIfIdxIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clientIfIdxIf.setStatus("current")


class _ClientIfUpPortId_Type(Integer32):
    """Custom type clientIfUpPortId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_ClientIfUpPortId_Type.__name__ = "Integer32"
_ClientIfUpPortId_Object = MibTableColumn
clientIfUpPortId = _ClientIfUpPortId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 143),
    _ClientIfUpPortId_Type()
)
clientIfUpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfUpPortId.setStatus("current")


class _ClientIfNoOfLanes_Type(Integer32):
    """Custom type clientIfNoOfLanes based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_ClientIfNoOfLanes_Type.__name__ = "Integer32"
_ClientIfNoOfLanes_Object = MibTableColumn
clientIfNoOfLanes = _ClientIfNoOfLanes_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 144),
    _ClientIfNoOfLanes_Type()
)
clientIfNoOfLanes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clientIfNoOfLanes.setStatus("current")
_ClientIfFecCorrectedBits_Type = Unsigned32
_ClientIfFecCorrectedBits_Object = MibTableColumn
clientIfFecCorrectedBits = _ClientIfFecCorrectedBits_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 145),
    _ClientIfFecCorrectedBits_Type()
)
clientIfFecCorrectedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfFecCorrectedBits.setStatus("current")
_ClientIfOSNRMargin_Type = Integer32
_ClientIfOSNRMargin_Object = MibTableColumn
clientIfOSNRMargin = _ClientIfOSNRMargin_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 146),
    _ClientIfOSNRMargin_Type()
)
clientIfOSNRMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfOSNRMargin.setStatus("current")


class _ClientIfExpectedPhysicalLayerMapping_Type(PhysicalLayerMappingType):
    """Custom type clientIfExpectedPhysicalLayerMapping based on PhysicalLayerMappingType"""
    defaultValue = 1


_ClientIfExpectedPhysicalLayerMapping_Type.__name__ = "PhysicalLayerMappingType"
_ClientIfExpectedPhysicalLayerMapping_Object = MibTableColumn
clientIfExpectedPhysicalLayerMapping = _ClientIfExpectedPhysicalLayerMapping_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 147),
    _ClientIfExpectedPhysicalLayerMapping_Type()
)
clientIfExpectedPhysicalLayerMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientIfExpectedPhysicalLayerMapping.setStatus("current")


class _ClientIfSignalDirection_Type(SignalDirection):
    """Custom type clientIfSignalDirection based on SignalDirection"""
    defaultValue = 2147483646


_ClientIfSignalDirection_Type.__name__ = "SignalDirection"
_ClientIfSignalDirection_Object = MibTableColumn
clientIfSignalDirection = _ClientIfSignalDirection_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 148),
    _ClientIfSignalDirection_Type()
)
clientIfSignalDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfSignalDirection.setStatus("current")
_ClientIfAid_Type = DisplayString
_ClientIfAid_Object = MibTableColumn
clientIfAid = _ClientIfAid_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 149),
    _ClientIfAid_Type()
)
clientIfAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfAid.setStatus("current")
_ClientIfPhysicalLocation_Type = DisplayString
_ClientIfPhysicalLocation_Object = MibTableColumn
clientIfPhysicalLocation = _ClientIfPhysicalLocation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 150),
    _ClientIfPhysicalLocation_Type()
)
clientIfPhysicalLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfPhysicalLocation.setStatus("current")
_ClientIfTrxCommunicationFailure_Type = FaultStatus
_ClientIfTrxCommunicationFailure_Object = MibTableColumn
clientIfTrxCommunicationFailure = _ClientIfTrxCommunicationFailure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 151),
    _ClientIfTrxCommunicationFailure_Type()
)
clientIfTrxCommunicationFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfTrxCommunicationFailure.setStatus("current")


class _ClientIfTribPortId_Type(Unsigned32):
    """Custom type clientIfTribPortId based on Unsigned32"""
    defaultValue = 0


_ClientIfTribPortId_Type.__name__ = "Unsigned32"
_ClientIfTribPortId_Object = MibTableColumn
clientIfTribPortId = _ClientIfTribPortId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 152),
    _ClientIfTribPortId_Type()
)
clientIfTribPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfTribPortId.setStatus("current")


class _ClientIfIfType_Type(InterfaceType):
    """Custom type clientIfIfType based on InterfaceType"""
    defaultValue = 1


_ClientIfIfType_Type.__name__ = "InterfaceType"
_ClientIfIfType_Object = MibTableColumn
clientIfIfType = _ClientIfIfType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 153),
    _ClientIfIfType_Type()
)
clientIfIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientIfIfType.setStatus("current")
_ClientIfConfigurationCommandSNMP_Type = CommandString
_ClientIfConfigurationCommandSNMP_Object = MibTableColumn
clientIfConfigurationCommandSNMP = _ClientIfConfigurationCommandSNMP_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 154),
    _ClientIfConfigurationCommandSNMP_Type()
)
clientIfConfigurationCommandSNMP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfConfigurationCommandSNMP.setStatus("current")
_ClientIfTrxPowerOutOfRange_Type = FaultStatus
_ClientIfTrxPowerOutOfRange_Object = MibTableColumn
clientIfTrxPowerOutOfRange = _ClientIfTrxPowerOutOfRange_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 2, 1, 1, 155),
    _ClientIfTrxPowerOutOfRange_Type()
)
clientIfTrxPowerOutOfRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIfTrxPowerOutOfRange.setStatus("current")
_ClientVc4List_ObjectIdentity = ObjectIdentity
clientVc4List = _ClientVc4List_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 3)
)
_ClientVc4Table_Object = MibTable
clientVc4Table = _ClientVc4Table_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 3, 1)
)
if mibBuilder.loadTexts:
    clientVc4Table.setStatus("current")
_ClientVc4Entry_Object = MibTableRow
clientVc4Entry = _ClientVc4Entry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 3, 1, 1)
)
clientVc4Entry.setIndexNames(
    (0, "LUM-CLIENT-MIB", "clientVc4Index"),
)
if mibBuilder.loadTexts:
    clientVc4Entry.setStatus("current")


class _ClientVc4Index_Type(Unsigned32):
    """Custom type clientVc4Index based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClientVc4Index_Type.__name__ = "Unsigned32"
_ClientVc4Index_Object = MibTableColumn
clientVc4Index = _ClientVc4Index_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 3, 1, 1, 1),
    _ClientVc4Index_Type()
)
clientVc4Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientVc4Index.setStatus("current")
_ClientVc4Name_Type = MgmtNameString
_ClientVc4Name_Object = MibTableColumn
clientVc4Name = _ClientVc4Name_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 3, 1, 1, 2),
    _ClientVc4Name_Type()
)
clientVc4Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientVc4Name.setStatus("current")


class _ClientVc4Descr_Type(DisplayString):
    """Custom type clientVc4Descr based on DisplayString"""
    defaultValue = OctetString("")


_ClientVc4Descr_Type.__name__ = "DisplayString"
_ClientVc4Descr_Object = MibTableColumn
clientVc4Descr = _ClientVc4Descr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 3, 1, 1, 3),
    _ClientVc4Descr_Type()
)
clientVc4Descr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientVc4Descr.setStatus("current")
_ClientVc4Subrack_Type = SubrackNumber
_ClientVc4Subrack_Object = MibTableColumn
clientVc4Subrack = _ClientVc4Subrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 3, 1, 1, 4),
    _ClientVc4Subrack_Type()
)
clientVc4Subrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientVc4Subrack.setStatus("current")
_ClientVc4Slot_Type = SlotNumber
_ClientVc4Slot_Object = MibTableColumn
clientVc4Slot = _ClientVc4Slot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 3, 1, 1, 5),
    _ClientVc4Slot_Type()
)
clientVc4Slot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientVc4Slot.setStatus("current")
_ClientVc4TxPort_Type = PortNumber
_ClientVc4TxPort_Object = MibTableColumn
clientVc4TxPort = _ClientVc4TxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 3, 1, 1, 6),
    _ClientVc4TxPort_Type()
)
clientVc4TxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientVc4TxPort.setStatus("current")
_ClientVc4RxPort_Type = PortNumber
_ClientVc4RxPort_Object = MibTableColumn
clientVc4RxPort = _ClientVc4RxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 3, 1, 1, 7),
    _ClientVc4RxPort_Type()
)
clientVc4RxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientVc4RxPort.setStatus("current")


class _ClientVc4Vc4_Type(Unsigned32):
    """Custom type clientVc4Vc4 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ClientVc4Vc4_Type.__name__ = "Unsigned32"
_ClientVc4Vc4_Object = MibTableColumn
clientVc4Vc4 = _ClientVc4Vc4_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 3, 1, 1, 8),
    _ClientVc4Vc4_Type()
)
clientVc4Vc4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientVc4Vc4.setStatus("current")
_ClientVc4ObjectProperty_Type = ObjectProperty
_ClientVc4ObjectProperty_Object = MibTableColumn
clientVc4ObjectProperty = _ClientVc4ObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 3, 1, 1, 9),
    _ClientVc4ObjectProperty_Type()
)
clientVc4ObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientVc4ObjectProperty.setStatus("current")


class _ClientVc4AuAlarmIndicationSignal_Type(Integer32):
    """Custom type clientVc4AuAlarmIndicationSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("alarm", 2))
    )


_ClientVc4AuAlarmIndicationSignal_Type.__name__ = "Integer32"
_ClientVc4AuAlarmIndicationSignal_Object = MibTableColumn
clientVc4AuAlarmIndicationSignal = _ClientVc4AuAlarmIndicationSignal_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 3, 1, 1, 10),
    _ClientVc4AuAlarmIndicationSignal_Type()
)
clientVc4AuAlarmIndicationSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientVc4AuAlarmIndicationSignal.setStatus("current")


class _ClientVc4AuLossOfPointer_Type(Integer32):
    """Custom type clientVc4AuLossOfPointer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("alarm", 2))
    )


_ClientVc4AuLossOfPointer_Type.__name__ = "Integer32"
_ClientVc4AuLossOfPointer_Object = MibTableColumn
clientVc4AuLossOfPointer = _ClientVc4AuLossOfPointer_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 3, 1, 1, 11),
    _ClientVc4AuLossOfPointer_Type()
)
clientVc4AuLossOfPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientVc4AuLossOfPointer.setStatus("current")


class _ClientVc4RxSignalStatus_Type(Integer32):
    """Custom type clientVc4RxSignalStatus based on Integer32"""
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
          ("degraded", 2),
          ("up", 3))
    )


_ClientVc4RxSignalStatus_Type.__name__ = "Integer32"
_ClientVc4RxSignalStatus_Object = MibTableColumn
clientVc4RxSignalStatus = _ClientVc4RxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 3, 1, 1, 12),
    _ClientVc4RxSignalStatus_Type()
)
clientVc4RxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientVc4RxSignalStatus.setStatus("current")


class _ClientVc4ConcatenationStatus_Type(Integer32):
    """Custom type clientVc4ConcatenationStatus based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("vc3", 3),
          ("vc4", 4),
          ("vc4x4c", 5),
          ("vc4x16c", 6),
          ("vc4x64c", 7),
          ("sts1", 8),
          ("sts3c", 9),
          ("sts12c", 10),
          ("unknown", 11))
    )


_ClientVc4ConcatenationStatus_Type.__name__ = "Integer32"
_ClientVc4ConcatenationStatus_Object = MibTableColumn
clientVc4ConcatenationStatus = _ClientVc4ConcatenationStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 3, 1, 1, 13),
    _ClientVc4ConcatenationStatus_Type()
)
clientVc4ConcatenationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientVc4ConcatenationStatus.setStatus("current")


class _ClientVc4PayloadStatus_Type(Integer32):
    """Custom type clientVc4PayloadStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("equipped", 1),
          ("unequipped", 2))
    )


_ClientVc4PayloadStatus_Type.__name__ = "Integer32"
_ClientVc4PayloadStatus_Object = MibTableColumn
clientVc4PayloadStatus = _ClientVc4PayloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 3, 1, 1, 14),
    _ClientVc4PayloadStatus_Type()
)
clientVc4PayloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientVc4PayloadStatus.setStatus("current")


class _ClientVc4ConnectionStatus_Type(DisplayString):
    """Custom type clientVc4ConnectionStatus based on DisplayString"""
    defaultValue = OctetString("Not connected")


_ClientVc4ConnectionStatus_Type.__name__ = "DisplayString"
_ClientVc4ConnectionStatus_Object = MibTableColumn
clientVc4ConnectionStatus = _ClientVc4ConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 3, 1, 1, 15),
    _ClientVc4ConnectionStatus_Type()
)
clientVc4ConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientVc4ConnectionStatus.setStatus("current")
_LumentisClientNotifications_ObjectIdentity = ObjectIdentity
lumentisClientNotifications = _LumentisClientNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 4)
)
_ClientNotifyPrefix_ObjectIdentity = ObjectIdentity
clientNotifyPrefix = _ClientNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 4, 0)
)
_ClientLanesList_ObjectIdentity = ObjectIdentity
clientLanesList = _ClientLanesList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 5)
)
_ClientLanesTable_Object = MibTable
clientLanesTable = _ClientLanesTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 5, 1)
)
if mibBuilder.loadTexts:
    clientLanesTable.setStatus("current")
_ClientLanesEntry_Object = MibTableRow
clientLanesEntry = _ClientLanesEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 5, 1, 1)
)
clientLanesEntry.setIndexNames(
    (0, "LUM-CLIENT-MIB", "clientLanesIndex"),
)
if mibBuilder.loadTexts:
    clientLanesEntry.setStatus("current")


class _ClientLanesIndex_Type(Unsigned32):
    """Custom type clientLanesIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClientLanesIndex_Type.__name__ = "Unsigned32"
_ClientLanesIndex_Object = MibTableColumn
clientLanesIndex = _ClientLanesIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 5, 1, 1, 1),
    _ClientLanesIndex_Type()
)
clientLanesIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clientLanesIndex.setStatus("current")
_ClientLanesName_Type = MgmtNameString
_ClientLanesName_Object = MibTableColumn
clientLanesName = _ClientLanesName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 5, 1, 1, 2),
    _ClientLanesName_Type()
)
clientLanesName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clientLanesName.setStatus("current")
_ClientLanesSubrack_Type = SubrackNumber
_ClientLanesSubrack_Object = MibTableColumn
clientLanesSubrack = _ClientLanesSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 5, 1, 1, 3),
    _ClientLanesSubrack_Type()
)
clientLanesSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clientLanesSubrack.setStatus("current")
_ClientLanesSlot_Type = SlotNumber
_ClientLanesSlot_Object = MibTableColumn
clientLanesSlot = _ClientLanesSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 5, 1, 1, 4),
    _ClientLanesSlot_Type()
)
clientLanesSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clientLanesSlot.setStatus("current")
_ClientLanesTxPort_Type = PortNumber
_ClientLanesTxPort_Object = MibTableColumn
clientLanesTxPort = _ClientLanesTxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 5, 1, 1, 5),
    _ClientLanesTxPort_Type()
)
clientLanesTxPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clientLanesTxPort.setStatus("current")
_ClientLanesRxPort_Type = PortNumber
_ClientLanesRxPort_Object = MibTableColumn
clientLanesRxPort = _ClientLanesRxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 5, 1, 1, 6),
    _ClientLanesRxPort_Type()
)
clientLanesRxPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clientLanesRxPort.setStatus("current")


class _ClientLanesLaneId_Type(Unsigned32):
    """Custom type clientLanesLaneId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ClientLanesLaneId_Type.__name__ = "Unsigned32"
_ClientLanesLaneId_Object = MibTableColumn
clientLanesLaneId = _ClientLanesLaneId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 5, 1, 1, 7),
    _ClientLanesLaneId_Type()
)
clientLanesLaneId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clientLanesLaneId.setStatus("current")
_ClientLanesRxPowerLevel_Type = Integer32
_ClientLanesRxPowerLevel_Object = MibTableColumn
clientLanesRxPowerLevel = _ClientLanesRxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 5, 1, 1, 8),
    _ClientLanesRxPowerLevel_Type()
)
clientLanesRxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientLanesRxPowerLevel.setStatus("current")
_ClientLanesWaveLength_Type = LaneFrequency
_ClientLanesWaveLength_Object = MibTableColumn
clientLanesWaveLength = _ClientLanesWaveLength_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 5, 1, 1, 9),
    _ClientLanesWaveLength_Type()
)
clientLanesWaveLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientLanesWaveLength.setStatus("current")
_ClientLanesBE_Type = Gauge32
_ClientLanesBE_Object = MibTableColumn
clientLanesBE = _ClientLanesBE_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 5, 1, 1, 10),
    _ClientLanesBE_Type()
)
clientLanesBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientLanesBE.setStatus("current")


class _ClientLanesResetBE_Type(Integer32):
    """Custom type clientLanesResetBE based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_ClientLanesResetBE_Type.__name__ = "Integer32"
_ClientLanesResetBE_Object = MibTableColumn
clientLanesResetBE = _ClientLanesResetBE_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 5, 1, 1, 11),
    _ClientLanesResetBE_Type()
)
clientLanesResetBE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientLanesResetBE.setStatus("current")
_ClientLanesLossOfSignal_Type = FaultStatus
_ClientLanesLossOfSignal_Object = MibTableColumn
clientLanesLossOfSignal = _ClientLanesLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 5, 1, 1, 12),
    _ClientLanesLossOfSignal_Type()
)
clientLanesLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientLanesLossOfSignal.setStatus("current")
_ClientLanesObjectProperty_Type = ObjectProperty
_ClientLanesObjectProperty_Object = MibTableColumn
clientLanesObjectProperty = _ClientLanesObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 5, 1, 1, 13),
    _ClientLanesObjectProperty_Type()
)
clientLanesObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientLanesObjectProperty.setStatus("current")
_ClientLanesLossOfSync_Type = FaultStatus
_ClientLanesLossOfSync_Object = MibTableColumn
clientLanesLossOfSync = _ClientLanesLossOfSync_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 5, 1, 1, 14),
    _ClientLanesLossOfSync_Type()
)
clientLanesLossOfSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientLanesLossOfSync.setStatus("current")
_ClientLanesLocalLinkFault_Type = FaultStatus
_ClientLanesLocalLinkFault_Object = MibTableColumn
clientLanesLocalLinkFault = _ClientLanesLocalLinkFault_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 5, 1, 1, 15),
    _ClientLanesLocalLinkFault_Type()
)
clientLanesLocalLinkFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientLanesLocalLinkFault.setStatus("current")
_ClientLanesRemoteLinkFault_Type = FaultStatus
_ClientLanesRemoteLinkFault_Object = MibTableColumn
clientLanesRemoteLinkFault = _ClientLanesRemoteLinkFault_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 5, 1, 1, 16),
    _ClientLanesRemoteLinkFault_Type()
)
clientLanesRemoteLinkFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientLanesRemoteLinkFault.setStatus("current")
_ClientLanesHighBitErrorRate_Type = FaultStatus
_ClientLanesHighBitErrorRate_Object = MibTableColumn
clientLanesHighBitErrorRate = _ClientLanesHighBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 5, 1, 1, 17),
    _ClientLanesHighBitErrorRate_Type()
)
clientLanesHighBitErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientLanesHighBitErrorRate.setStatus("current")
_ClientLanesReceiverSensitivity_Type = Integer32
_ClientLanesReceiverSensitivity_Object = MibTableColumn
clientLanesReceiverSensitivity = _ClientLanesReceiverSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 5, 1, 1, 18),
    _ClientLanesReceiverSensitivity_Type()
)
clientLanesReceiverSensitivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientLanesReceiverSensitivity.setStatus("current")
_ClientLanesReceivedPowerLow_Type = FaultStatus
_ClientLanesReceivedPowerLow_Object = MibTableColumn
clientLanesReceivedPowerLow = _ClientLanesReceivedPowerLow_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 5, 1, 1, 19),
    _ClientLanesReceivedPowerLow_Type()
)
clientLanesReceivedPowerLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientLanesReceivedPowerLow.setStatus("current")


class _ClientLanesIfNo_Type(PortNumber):
    """Custom type clientLanesIfNo based on PortNumber"""
    defaultValue = 0


_ClientLanesIfNo_Type.__name__ = "PortNumber"
_ClientLanesIfNo_Object = MibTableColumn
clientLanesIfNo = _ClientLanesIfNo_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 5, 1, 1, 20),
    _ClientLanesIfNo_Type()
)
clientLanesIfNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clientLanesIfNo.setStatus("current")


class _ClientLanesIdx_Type(Integer32):
    """Custom type clientLanesIdx based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_ClientLanesIdx_Type.__name__ = "Integer32"
_ClientLanesIdx_Object = MibTableColumn
clientLanesIdx = _ClientLanesIdx_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 5, 1, 1, 21),
    _ClientLanesIdx_Type()
)
clientLanesIdx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clientLanesIdx.setStatus("current")


class _ClientLanesClientIfIdx_Type(Integer32):
    """Custom type clientLanesClientIfIdx based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_ClientLanesClientIfIdx_Type.__name__ = "Integer32"
_ClientLanesClientIfIdx_Object = MibTableColumn
clientLanesClientIfIdx = _ClientLanesClientIfIdx_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 5, 1, 1, 22),
    _ClientLanesClientIfIdx_Type()
)
clientLanesClientIfIdx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clientLanesClientIfIdx.setStatus("current")


class _ClientLanesAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type clientLanesAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 3


_ClientLanesAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_ClientLanesAdminStatus_Object = MibTableColumn
clientLanesAdminStatus = _ClientLanesAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 5, 1, 1, 23),
    _ClientLanesAdminStatus_Type()
)
clientLanesAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientLanesAdminStatus.setStatus("current")


class _ClientLanesOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type clientLanesOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 1


_ClientLanesOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_ClientLanesOperStatus_Object = MibTableColumn
clientLanesOperStatus = _ClientLanesOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 5, 1, 1, 24),
    _ClientLanesOperStatus_Type()
)
clientLanesOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientLanesOperStatus.setStatus("current")


class _ClientLanesUpPortId_Type(Integer32):
    """Custom type clientLanesUpPortId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_ClientLanesUpPortId_Type.__name__ = "Integer32"
_ClientLanesUpPortId_Object = MibTableColumn
clientLanesUpPortId = _ClientLanesUpPortId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 5, 1, 1, 25),
    _ClientLanesUpPortId_Type()
)
clientLanesUpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientLanesUpPortId.setStatus("current")
_ClientMpoLanesList_ObjectIdentity = ObjectIdentity
clientMpoLanesList = _ClientMpoLanesList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 6)
)
_ClientMpoLanesTable_Object = MibTable
clientMpoLanesTable = _ClientMpoLanesTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 6, 1)
)
if mibBuilder.loadTexts:
    clientMpoLanesTable.setStatus("current")
_ClientMpoLanesEntry_Object = MibTableRow
clientMpoLanesEntry = _ClientMpoLanesEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 6, 1, 1)
)
clientMpoLanesEntry.setIndexNames(
    (0, "LUM-CLIENT-MIB", "clientMpoLanesIndex"),
)
if mibBuilder.loadTexts:
    clientMpoLanesEntry.setStatus("current")


class _ClientMpoLanesIndex_Type(Unsigned32):
    """Custom type clientMpoLanesIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClientMpoLanesIndex_Type.__name__ = "Unsigned32"
_ClientMpoLanesIndex_Object = MibTableColumn
clientMpoLanesIndex = _ClientMpoLanesIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 6, 1, 1, 1),
    _ClientMpoLanesIndex_Type()
)
clientMpoLanesIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clientMpoLanesIndex.setStatus("current")
_ClientMpoLanesName_Type = MgmtNameString
_ClientMpoLanesName_Object = MibTableColumn
clientMpoLanesName = _ClientMpoLanesName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 6, 1, 1, 2),
    _ClientMpoLanesName_Type()
)
clientMpoLanesName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clientMpoLanesName.setStatus("current")
_ClientMpoLanesSubrack_Type = SubrackNumber
_ClientMpoLanesSubrack_Object = MibTableColumn
clientMpoLanesSubrack = _ClientMpoLanesSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 6, 1, 1, 3),
    _ClientMpoLanesSubrack_Type()
)
clientMpoLanesSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clientMpoLanesSubrack.setStatus("current")
_ClientMpoLanesSlot_Type = SlotNumber
_ClientMpoLanesSlot_Object = MibTableColumn
clientMpoLanesSlot = _ClientMpoLanesSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 6, 1, 1, 4),
    _ClientMpoLanesSlot_Type()
)
clientMpoLanesSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clientMpoLanesSlot.setStatus("current")


class _ClientMpoLanesIfNo_Type(PortNumber):
    """Custom type clientMpoLanesIfNo based on PortNumber"""
    defaultValue = 0


_ClientMpoLanesIfNo_Type.__name__ = "PortNumber"
_ClientMpoLanesIfNo_Object = MibTableColumn
clientMpoLanesIfNo = _ClientMpoLanesIfNo_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 6, 1, 1, 5),
    _ClientMpoLanesIfNo_Type()
)
clientMpoLanesIfNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clientMpoLanesIfNo.setStatus("current")


class _ClientMpoLanesLaneId_Type(Unsigned32):
    """Custom type clientMpoLanesLaneId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ClientMpoLanesLaneId_Type.__name__ = "Unsigned32"
_ClientMpoLanesLaneId_Object = MibTableColumn
clientMpoLanesLaneId = _ClientMpoLanesLaneId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 6, 1, 1, 6),
    _ClientMpoLanesLaneId_Type()
)
clientMpoLanesLaneId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clientMpoLanesLaneId.setStatus("current")


class _ClientMpoLanesAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type clientMpoLanesAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 3


_ClientMpoLanesAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_ClientMpoLanesAdminStatus_Object = MibTableColumn
clientMpoLanesAdminStatus = _ClientMpoLanesAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 6, 1, 1, 7),
    _ClientMpoLanesAdminStatus_Type()
)
clientMpoLanesAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientMpoLanesAdminStatus.setStatus("current")


class _ClientMpoLanesOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type clientMpoLanesOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 1


_ClientMpoLanesOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_ClientMpoLanesOperStatus_Object = MibTableColumn
clientMpoLanesOperStatus = _ClientMpoLanesOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 6, 1, 1, 8),
    _ClientMpoLanesOperStatus_Type()
)
clientMpoLanesOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientMpoLanesOperStatus.setStatus("current")


class _ClientMpoLanesLaserStatus_Type(OnOff):
    """Custom type clientMpoLanesLaserStatus based on OnOff"""
    defaultValue = 1


_ClientMpoLanesLaserStatus_Type.__name__ = "OnOff"
_ClientMpoLanesLaserStatus_Object = MibTableColumn
clientMpoLanesLaserStatus = _ClientMpoLanesLaserStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 6, 1, 1, 9),
    _ClientMpoLanesLaserStatus_Type()
)
clientMpoLanesLaserStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientMpoLanesLaserStatus.setStatus("current")
_ClientMpoLanesRxSensitivity_Type = Integer32
_ClientMpoLanesRxSensitivity_Object = MibTableColumn
clientMpoLanesRxSensitivity = _ClientMpoLanesRxSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 6, 1, 1, 10),
    _ClientMpoLanesRxSensitivity_Type()
)
clientMpoLanesRxSensitivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientMpoLanesRxSensitivity.setStatus("current")
_ClientMpoLanesRxPowerLevel_Type = Integer32
_ClientMpoLanesRxPowerLevel_Object = MibTableColumn
clientMpoLanesRxPowerLevel = _ClientMpoLanesRxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 6, 1, 1, 11),
    _ClientMpoLanesRxPowerLevel_Type()
)
clientMpoLanesRxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientMpoLanesRxPowerLevel.setStatus("current")


class _ClientMpoLanesPowerLevelLowRelativeThreshold_Type(Integer32):
    """Custom type clientMpoLanesPowerLevelLowRelativeThreshold based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_ClientMpoLanesPowerLevelLowRelativeThreshold_Type.__name__ = "Integer32"
_ClientMpoLanesPowerLevelLowRelativeThreshold_Object = MibTableColumn
clientMpoLanesPowerLevelLowRelativeThreshold = _ClientMpoLanesPowerLevelLowRelativeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 6, 1, 1, 12),
    _ClientMpoLanesPowerLevelLowRelativeThreshold_Type()
)
clientMpoLanesPowerLevelLowRelativeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientMpoLanesPowerLevelLowRelativeThreshold.setStatus("current")
_ClientMpoLanesWaveLength_Type = LaneFrequency
_ClientMpoLanesWaveLength_Object = MibTableColumn
clientMpoLanesWaveLength = _ClientMpoLanesWaveLength_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 6, 1, 1, 13),
    _ClientMpoLanesWaveLength_Type()
)
clientMpoLanesWaveLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientMpoLanesWaveLength.setStatus("current")
_ClientMpoLanesObjectProperty_Type = ObjectProperty
_ClientMpoLanesObjectProperty_Object = MibTableColumn
clientMpoLanesObjectProperty = _ClientMpoLanesObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 6, 1, 1, 14),
    _ClientMpoLanesObjectProperty_Type()
)
clientMpoLanesObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientMpoLanesObjectProperty.setStatus("current")


class _ClientMpoLanesForwardAls_Type(EnableDisable):
    """Custom type clientMpoLanesForwardAls based on EnableDisable"""
    defaultValue = 1


_ClientMpoLanesForwardAls_Type.__name__ = "EnableDisable"
_ClientMpoLanesForwardAls_Object = MibTableColumn
clientMpoLanesForwardAls = _ClientMpoLanesForwardAls_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 6, 1, 1, 15),
    _ClientMpoLanesForwardAls_Type()
)
clientMpoLanesForwardAls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientMpoLanesForwardAls.setStatus("current")
_ClientMpoLanesLossOfSignal_Type = FaultStatus
_ClientMpoLanesLossOfSignal_Object = MibTableColumn
clientMpoLanesLossOfSignal = _ClientMpoLanesLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 6, 1, 1, 16),
    _ClientMpoLanesLossOfSignal_Type()
)
clientMpoLanesLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientMpoLanesLossOfSignal.setStatus("current")
_ClientMpoLanesRxPowerLow_Type = FaultStatus
_ClientMpoLanesRxPowerLow_Object = MibTableColumn
clientMpoLanesRxPowerLow = _ClientMpoLanesRxPowerLow_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 6, 1, 1, 17),
    _ClientMpoLanesRxPowerLow_Type()
)
clientMpoLanesRxPowerLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientMpoLanesRxPowerLow.setStatus("current")

# Managed Objects groups

clientGeneralGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 1, 1)
)
clientGeneralGroupV1.setObjects(
      *(("LUM-CLIENT-MIB", "clientGeneralLastChangeTime"),
        ("LUM-CLIENT-MIB", "clientGeneralStateLastChangeTime"))
)
if mibBuilder.loadTexts:
    clientGeneralGroupV1.setStatus("deprecated")

clientIfGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 1, 3)
)
clientIfGroupV1.setObjects(
      *(("LUM-CLIENT-MIB", "clientIfIndex"),
        ("LUM-CLIENT-MIB", "clientIfName"),
        ("LUM-CLIENT-MIB", "clientIfSubrack"),
        ("LUM-CLIENT-MIB", "clientIfSlot"),
        ("LUM-CLIENT-MIB", "clientIfTxPort"),
        ("LUM-CLIENT-MIB", "clientIfRxPort"),
        ("LUM-CLIENT-MIB", "clientIfEntityId"),
        ("LUM-CLIENT-MIB", "clientIfAdminStatus"),
        ("LUM-CLIENT-MIB", "clientIfOperStatus"),
        ("LUM-CLIENT-MIB", "clientIfLaserStatus"),
        ("LUM-CLIENT-MIB", "clientIfTxSignalStatus"),
        ("LUM-CLIENT-MIB", "clientIfForwardAls"),
        ("LUM-CLIENT-MIB", "clientIfSuppressRemoteAlarms"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfFormat"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationStatus"),
        ("LUM-CLIENT-MIB", "clientIfDuplexCapability"),
        ("LUM-CLIENT-MIB", "clientIfFlowControlMode"),
        ("LUM-CLIENT-MIB", "clientIfInterPacketGap"),
        ("LUM-CLIENT-MIB", "clientIfFrameSize"),
        ("LUM-CLIENT-MIB", "clientIfGfpMode"),
        ("LUM-CLIENT-MIB", "clientIfBandWidth"),
        ("LUM-CLIENT-MIB", "clientIfRateLimit"),
        ("LUM-CLIENT-MIB", "clientIfTrxClass"),
        ("LUM-CLIENT-MIB", "clientIfLaserBias"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfReceiverSensitivity"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevelLowRelativeThreshold"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSignal"),
        ("LUM-CLIENT-MIB", "clientIfLossOfFrame"),
        ("LUM-CLIENT-MIB", "clientIfBitrateMismatch"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfTransmitterFailed"),
        ("LUM-CLIENT-MIB", "clientIfTrxCodeMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTrxBitrateUnavailable"),
        ("LUM-CLIENT-MIB", "clientIfTrxMissing"),
        ("LUM-CLIENT-MIB", "clientIfTrxFailed"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerHigh"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerLow"),
        ("LUM-CLIENT-MIB", "clientIfLinkDown"),
        ("LUM-CLIENT-MIB", "clientIfConfigurationCommand"),
        ("LUM-CLIENT-MIB", "clientIfGbeUtilization"))
)
if mibBuilder.loadTexts:
    clientIfGroupV1.setStatus("deprecated")

clientIfGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 1, 4)
)
clientIfGroupV2.setObjects(
      *(("LUM-CLIENT-MIB", "clientIfIndex"),
        ("LUM-CLIENT-MIB", "clientIfName"),
        ("LUM-CLIENT-MIB", "clientIfSubrack"),
        ("LUM-CLIENT-MIB", "clientIfSlot"),
        ("LUM-CLIENT-MIB", "clientIfTxPort"),
        ("LUM-CLIENT-MIB", "clientIfRxPort"),
        ("LUM-CLIENT-MIB", "clientIfEntityId"),
        ("LUM-CLIENT-MIB", "clientIfAdminStatus"),
        ("LUM-CLIENT-MIB", "clientIfOperStatus"),
        ("LUM-CLIENT-MIB", "clientIfLaserStatus"),
        ("LUM-CLIENT-MIB", "clientIfTxSignalStatus"),
        ("LUM-CLIENT-MIB", "clientIfForwardAls"),
        ("LUM-CLIENT-MIB", "clientIfSuppressRemoteAlarms"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfFormat"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationStatus"),
        ("LUM-CLIENT-MIB", "clientIfDuplexCapability"),
        ("LUM-CLIENT-MIB", "clientIfFlowControlMode"),
        ("LUM-CLIENT-MIB", "clientIfInterPacketGap"),
        ("LUM-CLIENT-MIB", "clientIfFrameSize"),
        ("LUM-CLIENT-MIB", "clientIfGfpMode"),
        ("LUM-CLIENT-MIB", "clientIfBandWidth"),
        ("LUM-CLIENT-MIB", "clientIfRateLimit"),
        ("LUM-CLIENT-MIB", "clientIfTrxClass"),
        ("LUM-CLIENT-MIB", "clientIfLaserBias"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfReceiverSensitivity"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevelLowRelativeThreshold"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSignal"),
        ("LUM-CLIENT-MIB", "clientIfLossOfFrame"),
        ("LUM-CLIENT-MIB", "clientIfBitrateMismatch"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfTransmitterFailed"),
        ("LUM-CLIENT-MIB", "clientIfTrxCodeMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTrxBitrateUnavailable"),
        ("LUM-CLIENT-MIB", "clientIfTrxMissing"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerHigh"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerLow"),
        ("LUM-CLIENT-MIB", "clientIfLinkDown"),
        ("LUM-CLIENT-MIB", "clientIfConfigurationCommand"),
        ("LUM-CLIENT-MIB", "clientIfGbeUtilization"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSync"),
        ("LUM-CLIENT-MIB", "clientIfConfigureTrxModeCommand"),
        ("LUM-CLIENT-MIB", "clientIfTrxMode"),
        ("LUM-CLIENT-MIB", "clientIfExpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfUnexpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfIllegalFrequency"),
        ("LUM-CLIENT-MIB", "clientIfLaserForcedOn"),
        ("LUM-CLIENT-MIB", "clientIfRxSignalStatus"))
)
if mibBuilder.loadTexts:
    clientIfGroupV2.setStatus("deprecated")

clientGeneralGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 1, 5)
)
clientGeneralGroupV2.setObjects(
      *(("LUM-CLIENT-MIB", "clientGeneralLastChangeTime"),
        ("LUM-CLIENT-MIB", "clientGeneralStateLastChangeTime"),
        ("LUM-CLIENT-MIB", "clientGeneralClientIfTableSize"))
)
if mibBuilder.loadTexts:
    clientGeneralGroupV2.setStatus("current")

clientIfGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 1, 6)
)
clientIfGroupV3.setObjects(
      *(("LUM-CLIENT-MIB", "clientIfIndex"),
        ("LUM-CLIENT-MIB", "clientIfName"),
        ("LUM-CLIENT-MIB", "clientIfSubrack"),
        ("LUM-CLIENT-MIB", "clientIfSlot"),
        ("LUM-CLIENT-MIB", "clientIfTxPort"),
        ("LUM-CLIENT-MIB", "clientIfRxPort"),
        ("LUM-CLIENT-MIB", "clientIfEntityId"),
        ("LUM-CLIENT-MIB", "clientIfAdminStatus"),
        ("LUM-CLIENT-MIB", "clientIfOperStatus"),
        ("LUM-CLIENT-MIB", "clientIfLaserStatus"),
        ("LUM-CLIENT-MIB", "clientIfTxSignalStatus"),
        ("LUM-CLIENT-MIB", "clientIfForwardAls"),
        ("LUM-CLIENT-MIB", "clientIfSuppressRemoteAlarms"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfFormat"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationStatus"),
        ("LUM-CLIENT-MIB", "clientIfDuplexCapability"),
        ("LUM-CLIENT-MIB", "clientIfFlowControlMode"),
        ("LUM-CLIENT-MIB", "clientIfInterPacketGap"),
        ("LUM-CLIENT-MIB", "clientIfFrameSize"),
        ("LUM-CLIENT-MIB", "clientIfGfpMode"),
        ("LUM-CLIENT-MIB", "clientIfBandWidth"),
        ("LUM-CLIENT-MIB", "clientIfRateLimit"),
        ("LUM-CLIENT-MIB", "clientIfTrxClass"),
        ("LUM-CLIENT-MIB", "clientIfLaserBias"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfReceiverSensitivity"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevelLowRelativeThreshold"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSignal"),
        ("LUM-CLIENT-MIB", "clientIfLossOfFrame"),
        ("LUM-CLIENT-MIB", "clientIfBitrateMismatch"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfTransmitterFailed"),
        ("LUM-CLIENT-MIB", "clientIfTrxCodeMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTrxBitrateUnavailable"),
        ("LUM-CLIENT-MIB", "clientIfTrxMissing"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerHigh"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerLow"),
        ("LUM-CLIENT-MIB", "clientIfLinkDown"),
        ("LUM-CLIENT-MIB", "clientIfConfigurationCommand"),
        ("LUM-CLIENT-MIB", "clientIfGbeUtilization"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSync"),
        ("LUM-CLIENT-MIB", "clientIfConfigureTrxModeCommand"),
        ("LUM-CLIENT-MIB", "clientIfTrxMode"),
        ("LUM-CLIENT-MIB", "clientIfExpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfUnexpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfIllegalFrequency"),
        ("LUM-CLIENT-MIB", "clientIfLaserForcedOn"),
        ("LUM-CLIENT-MIB", "clientIfTrxMedia"),
        ("LUM-CLIENT-MIB", "clientIfTrxMediaMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTruncAutoNegotiationMode"))
)
if mibBuilder.loadTexts:
    clientIfGroupV3.setStatus("deprecated")

clientIfGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 1, 7)
)
clientIfGroupV4.setObjects(
      *(("LUM-CLIENT-MIB", "clientIfIndex"),
        ("LUM-CLIENT-MIB", "clientIfName"),
        ("LUM-CLIENT-MIB", "clientIfSubrack"),
        ("LUM-CLIENT-MIB", "clientIfSlot"),
        ("LUM-CLIENT-MIB", "clientIfTxPort"),
        ("LUM-CLIENT-MIB", "clientIfRxPort"),
        ("LUM-CLIENT-MIB", "clientIfEntityId"),
        ("LUM-CLIENT-MIB", "clientIfAdminStatus"),
        ("LUM-CLIENT-MIB", "clientIfOperStatus"),
        ("LUM-CLIENT-MIB", "clientIfLaserStatus"),
        ("LUM-CLIENT-MIB", "clientIfTxSignalStatus"),
        ("LUM-CLIENT-MIB", "clientIfForwardAls"),
        ("LUM-CLIENT-MIB", "clientIfSuppressRemoteAlarms"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfFormat"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationStatus"),
        ("LUM-CLIENT-MIB", "clientIfDuplexCapability"),
        ("LUM-CLIENT-MIB", "clientIfFlowControlMode"),
        ("LUM-CLIENT-MIB", "clientIfInterPacketGap"),
        ("LUM-CLIENT-MIB", "clientIfFrameSize"),
        ("LUM-CLIENT-MIB", "clientIfGfpMode"),
        ("LUM-CLIENT-MIB", "clientIfBandWidth"),
        ("LUM-CLIENT-MIB", "clientIfRateLimit"),
        ("LUM-CLIENT-MIB", "clientIfTrxClass"),
        ("LUM-CLIENT-MIB", "clientIfLaserBias"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfReceiverSensitivity"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevelLowRelativeThreshold"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSignal"),
        ("LUM-CLIENT-MIB", "clientIfLossOfFrame"),
        ("LUM-CLIENT-MIB", "clientIfBitrateMismatch"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfTransmitterFailed"),
        ("LUM-CLIENT-MIB", "clientIfTrxCodeMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTrxBitrateUnavailable"),
        ("LUM-CLIENT-MIB", "clientIfTrxMissing"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerHigh"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerLow"),
        ("LUM-CLIENT-MIB", "clientIfLinkDown"),
        ("LUM-CLIENT-MIB", "clientIfConfigurationCommand"),
        ("LUM-CLIENT-MIB", "clientIfGbeUtilization"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSync"),
        ("LUM-CLIENT-MIB", "clientIfConfigureTrxModeCommand"),
        ("LUM-CLIENT-MIB", "clientIfTrxMode"),
        ("LUM-CLIENT-MIB", "clientIfExpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfUnexpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfIllegalFrequency"),
        ("LUM-CLIENT-MIB", "clientIfLaserForcedOn"),
        ("LUM-CLIENT-MIB", "clientIfTrxMedia"),
        ("LUM-CLIENT-MIB", "clientIfTrxMediaMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTruncAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfObjectProperty"),
        ("LUM-CLIENT-MIB", "clientIfTxPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfLaserTempActual"),
        ("LUM-CLIENT-MIB", "clientIfTraceIntrusionMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceTransmitted"),
        ("LUM-CLIENT-MIB", "clientIfTraceReceived"),
        ("LUM-CLIENT-MIB", "clientIfTraceExpected"),
        ("LUM-CLIENT-MIB", "clientIfTraceAlarmMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceMismatch"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopback"))
)
if mibBuilder.loadTexts:
    clientIfGroupV4.setStatus("deprecated")

clientIfGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 1, 8)
)
clientIfGroupV5.setObjects(
      *(("LUM-CLIENT-MIB", "clientIfIndex"),
        ("LUM-CLIENT-MIB", "clientIfName"),
        ("LUM-CLIENT-MIB", "clientIfSubrack"),
        ("LUM-CLIENT-MIB", "clientIfSlot"),
        ("LUM-CLIENT-MIB", "clientIfTxPort"),
        ("LUM-CLIENT-MIB", "clientIfRxPort"),
        ("LUM-CLIENT-MIB", "clientIfEntityId"),
        ("LUM-CLIENT-MIB", "clientIfAdminStatus"),
        ("LUM-CLIENT-MIB", "clientIfOperStatus"),
        ("LUM-CLIENT-MIB", "clientIfLaserStatus"),
        ("LUM-CLIENT-MIB", "clientIfTxSignalStatus"),
        ("LUM-CLIENT-MIB", "clientIfForwardAls"),
        ("LUM-CLIENT-MIB", "clientIfSuppressRemoteAlarms"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfFormat"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationStatus"),
        ("LUM-CLIENT-MIB", "clientIfDuplexCapability"),
        ("LUM-CLIENT-MIB", "clientIfFlowControlMode"),
        ("LUM-CLIENT-MIB", "clientIfInterPacketGap"),
        ("LUM-CLIENT-MIB", "clientIfFrameSize"),
        ("LUM-CLIENT-MIB", "clientIfGfpMode"),
        ("LUM-CLIENT-MIB", "clientIfBandWidth"),
        ("LUM-CLIENT-MIB", "clientIfRateLimit"),
        ("LUM-CLIENT-MIB", "clientIfTrxClass"),
        ("LUM-CLIENT-MIB", "clientIfLaserBias"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfReceiverSensitivity"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevelLowRelativeThreshold"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSignal"),
        ("LUM-CLIENT-MIB", "clientIfLossOfFrame"),
        ("LUM-CLIENT-MIB", "clientIfBitrateMismatch"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfTransmitterFailed"),
        ("LUM-CLIENT-MIB", "clientIfTrxCodeMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTrxBitrateUnavailable"),
        ("LUM-CLIENT-MIB", "clientIfTrxMissing"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerHigh"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerLow"),
        ("LUM-CLIENT-MIB", "clientIfLinkDown"),
        ("LUM-CLIENT-MIB", "clientIfConfigurationCommand"),
        ("LUM-CLIENT-MIB", "clientIfGbeUtilization"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSync"),
        ("LUM-CLIENT-MIB", "clientIfConfigureTrxModeCommand"),
        ("LUM-CLIENT-MIB", "clientIfTrxMode"),
        ("LUM-CLIENT-MIB", "clientIfExpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfUnexpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfIllegalFrequency"),
        ("LUM-CLIENT-MIB", "clientIfLaserForcedOn"),
        ("LUM-CLIENT-MIB", "clientIfTrxMedia"),
        ("LUM-CLIENT-MIB", "clientIfTrxMediaMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTruncAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfObjectProperty"),
        ("LUM-CLIENT-MIB", "clientIfTxPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfLaserTempActual"),
        ("LUM-CLIENT-MIB", "clientIfTraceIntrusionMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceTransmitted"),
        ("LUM-CLIENT-MIB", "clientIfTraceReceived"),
        ("LUM-CLIENT-MIB", "clientIfTraceExpected"),
        ("LUM-CLIENT-MIB", "clientIfTraceAlarmMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceMismatch"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfMsAlarmIndicationSignalC2W"),
        ("LUM-CLIENT-MIB", "clientIfMsAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfRemoteDefectIndication"))
)
if mibBuilder.loadTexts:
    clientIfGroupV5.setStatus("deprecated")

clientIfGroupV6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 1, 9)
)
clientIfGroupV6.setObjects(
      *(("LUM-CLIENT-MIB", "clientIfIndex"),
        ("LUM-CLIENT-MIB", "clientIfName"),
        ("LUM-CLIENT-MIB", "clientIfSubrack"),
        ("LUM-CLIENT-MIB", "clientIfSlot"),
        ("LUM-CLIENT-MIB", "clientIfTxPort"),
        ("LUM-CLIENT-MIB", "clientIfRxPort"),
        ("LUM-CLIENT-MIB", "clientIfEntityId"),
        ("LUM-CLIENT-MIB", "clientIfAdminStatus"),
        ("LUM-CLIENT-MIB", "clientIfOperStatus"),
        ("LUM-CLIENT-MIB", "clientIfLaserStatus"),
        ("LUM-CLIENT-MIB", "clientIfTxSignalStatus"),
        ("LUM-CLIENT-MIB", "clientIfForwardAls"),
        ("LUM-CLIENT-MIB", "clientIfSuppressRemoteAlarms"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfFormat"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationStatus"),
        ("LUM-CLIENT-MIB", "clientIfDuplexCapability"),
        ("LUM-CLIENT-MIB", "clientIfFlowControlMode"),
        ("LUM-CLIENT-MIB", "clientIfInterPacketGap"),
        ("LUM-CLIENT-MIB", "clientIfFrameSize"),
        ("LUM-CLIENT-MIB", "clientIfGfpMode"),
        ("LUM-CLIENT-MIB", "clientIfBandWidth"),
        ("LUM-CLIENT-MIB", "clientIfRateLimit"),
        ("LUM-CLIENT-MIB", "clientIfTrxClass"),
        ("LUM-CLIENT-MIB", "clientIfLaserBias"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfReceiverSensitivity"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevelLowRelativeThreshold"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSignal"),
        ("LUM-CLIENT-MIB", "clientIfLossOfFrame"),
        ("LUM-CLIENT-MIB", "clientIfBitrateMismatch"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfTransmitterFailed"),
        ("LUM-CLIENT-MIB", "clientIfTrxCodeMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTrxBitrateUnavailable"),
        ("LUM-CLIENT-MIB", "clientIfTrxMissing"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerHigh"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerLow"),
        ("LUM-CLIENT-MIB", "clientIfLinkDown"),
        ("LUM-CLIENT-MIB", "clientIfConfigurationCommand"),
        ("LUM-CLIENT-MIB", "clientIfGbeUtilization"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSync"),
        ("LUM-CLIENT-MIB", "clientIfConfigureTrxModeCommand"),
        ("LUM-CLIENT-MIB", "clientIfTrxMode"),
        ("LUM-CLIENT-MIB", "clientIfExpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfUnexpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfIllegalFrequency"),
        ("LUM-CLIENT-MIB", "clientIfLaserForcedOn"),
        ("LUM-CLIENT-MIB", "clientIfTrxMedia"),
        ("LUM-CLIENT-MIB", "clientIfTrxMediaMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTruncAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfObjectProperty"),
        ("LUM-CLIENT-MIB", "clientIfTxPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfLaserTempActual"),
        ("LUM-CLIENT-MIB", "clientIfTraceIntrusionMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceTransmitted"),
        ("LUM-CLIENT-MIB", "clientIfTraceReceived"),
        ("LUM-CLIENT-MIB", "clientIfTraceExpected"),
        ("LUM-CLIENT-MIB", "clientIfTraceAlarmMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceMismatch"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfMsAlarmIndicationSignalC2W"),
        ("LUM-CLIENT-MIB", "clientIfMsAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfRemoteDefectIndication"),
        ("LUM-CLIENT-MIB", "clientIfJ1TxTrailTrace"),
        ("LUM-CLIENT-MIB", "clientIfJ1TxTrailTraceInsertionMode"),
        ("LUM-CLIENT-MIB", "clientIfVcGroupFailedW2C"),
        ("LUM-CLIENT-MIB", "clientIfReadJ1"))
)
if mibBuilder.loadTexts:
    clientIfGroupV6.setStatus("deprecated")

clientIfGroupV7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 1, 10)
)
clientIfGroupV7.setObjects(
      *(("LUM-CLIENT-MIB", "clientIfIndex"),
        ("LUM-CLIENT-MIB", "clientIfName"),
        ("LUM-CLIENT-MIB", "clientIfSubrack"),
        ("LUM-CLIENT-MIB", "clientIfSlot"),
        ("LUM-CLIENT-MIB", "clientIfTxPort"),
        ("LUM-CLIENT-MIB", "clientIfRxPort"),
        ("LUM-CLIENT-MIB", "clientIfEntityId"),
        ("LUM-CLIENT-MIB", "clientIfAdminStatus"),
        ("LUM-CLIENT-MIB", "clientIfOperStatus"),
        ("LUM-CLIENT-MIB", "clientIfLaserStatus"),
        ("LUM-CLIENT-MIB", "clientIfTxSignalStatus"),
        ("LUM-CLIENT-MIB", "clientIfForwardAls"),
        ("LUM-CLIENT-MIB", "clientIfSuppressRemoteAlarms"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfFormat"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationStatus"),
        ("LUM-CLIENT-MIB", "clientIfDuplexCapability"),
        ("LUM-CLIENT-MIB", "clientIfFlowControlMode"),
        ("LUM-CLIENT-MIB", "clientIfInterPacketGap"),
        ("LUM-CLIENT-MIB", "clientIfFrameSize"),
        ("LUM-CLIENT-MIB", "clientIfGfpMode"),
        ("LUM-CLIENT-MIB", "clientIfBandWidth"),
        ("LUM-CLIENT-MIB", "clientIfRateLimit"),
        ("LUM-CLIENT-MIB", "clientIfTrxClass"),
        ("LUM-CLIENT-MIB", "clientIfLaserBias"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfReceiverSensitivity"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevelLowRelativeThreshold"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSignal"),
        ("LUM-CLIENT-MIB", "clientIfLossOfFrame"),
        ("LUM-CLIENT-MIB", "clientIfBitrateMismatch"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfTransmitterFailed"),
        ("LUM-CLIENT-MIB", "clientIfTrxCodeMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTrxBitrateUnavailable"),
        ("LUM-CLIENT-MIB", "clientIfTrxMissing"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerHigh"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerLow"),
        ("LUM-CLIENT-MIB", "clientIfLinkDown"),
        ("LUM-CLIENT-MIB", "clientIfConfigurationCommand"),
        ("LUM-CLIENT-MIB", "clientIfGbeUtilization"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSync"),
        ("LUM-CLIENT-MIB", "clientIfConfigureTrxModeCommand"),
        ("LUM-CLIENT-MIB", "clientIfTrxMode"),
        ("LUM-CLIENT-MIB", "clientIfExpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfUnexpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfIllegalFrequency"),
        ("LUM-CLIENT-MIB", "clientIfLaserForcedOn"),
        ("LUM-CLIENT-MIB", "clientIfTrxMedia"),
        ("LUM-CLIENT-MIB", "clientIfTrxMediaMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTruncAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfObjectProperty"),
        ("LUM-CLIENT-MIB", "clientIfTxPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfLaserTempActual"),
        ("LUM-CLIENT-MIB", "clientIfTraceIntrusionMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceTransmitted"),
        ("LUM-CLIENT-MIB", "clientIfTraceReceived"),
        ("LUM-CLIENT-MIB", "clientIfTraceExpected"),
        ("LUM-CLIENT-MIB", "clientIfTraceAlarmMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceMismatch"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfMsAlarmIndicationSignalC2W"),
        ("LUM-CLIENT-MIB", "clientIfMsAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfRemoteDefectIndication"),
        ("LUM-CLIENT-MIB", "clientIfJ1TxTrailTrace"),
        ("LUM-CLIENT-MIB", "clientIfJ1TxTrailTraceInsertionMode"),
        ("LUM-CLIENT-MIB", "clientIfVcGroupFailedW2C"),
        ("LUM-CLIENT-MIB", "clientIfReadJ1"),
        ("LUM-CLIENT-MIB", "clientIfHighSpeed"),
        ("LUM-CLIENT-MIB", "clientIfActualFormat"))
)
if mibBuilder.loadTexts:
    clientIfGroupV7.setStatus("deprecated")

clientIfGroupV8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 1, 11)
)
clientIfGroupV8.setObjects(
      *(("LUM-CLIENT-MIB", "clientIfIndex"),
        ("LUM-CLIENT-MIB", "clientIfName"),
        ("LUM-CLIENT-MIB", "clientIfSubrack"),
        ("LUM-CLIENT-MIB", "clientIfSlot"),
        ("LUM-CLIENT-MIB", "clientIfTxPort"),
        ("LUM-CLIENT-MIB", "clientIfRxPort"),
        ("LUM-CLIENT-MIB", "clientIfEntityId"),
        ("LUM-CLIENT-MIB", "clientIfAdminStatus"),
        ("LUM-CLIENT-MIB", "clientIfOperStatus"),
        ("LUM-CLIENT-MIB", "clientIfLaserStatus"),
        ("LUM-CLIENT-MIB", "clientIfTxSignalStatus"),
        ("LUM-CLIENT-MIB", "clientIfForwardAls"),
        ("LUM-CLIENT-MIB", "clientIfSuppressRemoteAlarms"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfFormat"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationStatus"),
        ("LUM-CLIENT-MIB", "clientIfDuplexCapability"),
        ("LUM-CLIENT-MIB", "clientIfFlowControlMode"),
        ("LUM-CLIENT-MIB", "clientIfInterPacketGap"),
        ("LUM-CLIENT-MIB", "clientIfFrameSize"),
        ("LUM-CLIENT-MIB", "clientIfGfpMode"),
        ("LUM-CLIENT-MIB", "clientIfBandWidth"),
        ("LUM-CLIENT-MIB", "clientIfRateLimit"),
        ("LUM-CLIENT-MIB", "clientIfTrxClass"),
        ("LUM-CLIENT-MIB", "clientIfLaserBias"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfReceiverSensitivity"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevelLowRelativeThreshold"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSignal"),
        ("LUM-CLIENT-MIB", "clientIfLossOfFrame"),
        ("LUM-CLIENT-MIB", "clientIfBitrateMismatch"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfTransmitterFailed"),
        ("LUM-CLIENT-MIB", "clientIfTrxCodeMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTrxBitrateUnavailable"),
        ("LUM-CLIENT-MIB", "clientIfTrxMissing"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerHigh"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerLow"),
        ("LUM-CLIENT-MIB", "clientIfLinkDown"),
        ("LUM-CLIENT-MIB", "clientIfConfigurationCommand"),
        ("LUM-CLIENT-MIB", "clientIfGbeUtilization"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSync"),
        ("LUM-CLIENT-MIB", "clientIfConfigureTrxModeCommand"),
        ("LUM-CLIENT-MIB", "clientIfTrxMode"),
        ("LUM-CLIENT-MIB", "clientIfExpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfUnexpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfIllegalFrequency"),
        ("LUM-CLIENT-MIB", "clientIfLaserForcedOn"),
        ("LUM-CLIENT-MIB", "clientIfTrxMedia"),
        ("LUM-CLIENT-MIB", "clientIfTrxMediaMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTruncAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfObjectProperty"),
        ("LUM-CLIENT-MIB", "clientIfTxPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfLaserTempActual"),
        ("LUM-CLIENT-MIB", "clientIfTraceIntrusionMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceTransmitted"),
        ("LUM-CLIENT-MIB", "clientIfTraceReceived"),
        ("LUM-CLIENT-MIB", "clientIfTraceExpected"),
        ("LUM-CLIENT-MIB", "clientIfTraceAlarmMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceMismatch"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfMsAlarmIndicationSignalC2W"),
        ("LUM-CLIENT-MIB", "clientIfMsAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfRemoteDefectIndication"),
        ("LUM-CLIENT-MIB", "clientIfJ1TxTrailTrace"),
        ("LUM-CLIENT-MIB", "clientIfJ1TxTrailTraceInsertionMode"),
        ("LUM-CLIENT-MIB", "clientIfVcGroupFailedW2C"),
        ("LUM-CLIENT-MIB", "clientIfReadJ1"),
        ("LUM-CLIENT-MIB", "clientIfHighSpeed"),
        ("LUM-CLIENT-MIB", "clientIfActualFormat"),
        ("LUM-CLIENT-MIB", "clientIfRdiIntrusionMode"))
)
if mibBuilder.loadTexts:
    clientIfGroupV8.setStatus("deprecated")

clientVc4Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 1, 12)
)
clientVc4Group.setObjects(
      *(("LUM-CLIENT-MIB", "clientVc4Index"),
        ("LUM-CLIENT-MIB", "clientVc4Name"),
        ("LUM-CLIENT-MIB", "clientVc4Descr"),
        ("LUM-CLIENT-MIB", "clientVc4Subrack"),
        ("LUM-CLIENT-MIB", "clientVc4Slot"),
        ("LUM-CLIENT-MIB", "clientVc4TxPort"),
        ("LUM-CLIENT-MIB", "clientVc4RxPort"),
        ("LUM-CLIENT-MIB", "clientVc4Vc4"),
        ("LUM-CLIENT-MIB", "clientVc4ObjectProperty"),
        ("LUM-CLIENT-MIB", "clientVc4AuAlarmIndicationSignal"),
        ("LUM-CLIENT-MIB", "clientVc4AuLossOfPointer"),
        ("LUM-CLIENT-MIB", "clientVc4RxSignalStatus"),
        ("LUM-CLIENT-MIB", "clientVc4ConcatenationStatus"),
        ("LUM-CLIENT-MIB", "clientVc4PayloadStatus"))
)
if mibBuilder.loadTexts:
    clientVc4Group.setStatus("deprecated")

clientGeneralGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 1, 13)
)
clientGeneralGroupV3.setObjects(
      *(("LUM-CLIENT-MIB", "clientGeneralLastChangeTime"),
        ("LUM-CLIENT-MIB", "clientGeneralStateLastChangeTime"),
        ("LUM-CLIENT-MIB", "clientGeneralClientIfTableSize"),
        ("LUM-CLIENT-MIB", "clientGeneralVc4TableSize"))
)
if mibBuilder.loadTexts:
    clientGeneralGroupV3.setStatus("current")

clientIfGroupV9 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 1, 14)
)
clientIfGroupV9.setObjects(
      *(("LUM-CLIENT-MIB", "clientIfIndex"),
        ("LUM-CLIENT-MIB", "clientIfName"),
        ("LUM-CLIENT-MIB", "clientIfSubrack"),
        ("LUM-CLIENT-MIB", "clientIfSlot"),
        ("LUM-CLIENT-MIB", "clientIfTxPort"),
        ("LUM-CLIENT-MIB", "clientIfRxPort"),
        ("LUM-CLIENT-MIB", "clientIfEntityId"),
        ("LUM-CLIENT-MIB", "clientIfAdminStatus"),
        ("LUM-CLIENT-MIB", "clientIfOperStatus"),
        ("LUM-CLIENT-MIB", "clientIfLaserStatus"),
        ("LUM-CLIENT-MIB", "clientIfTxSignalStatus"),
        ("LUM-CLIENT-MIB", "clientIfForwardAls"),
        ("LUM-CLIENT-MIB", "clientIfSuppressRemoteAlarms"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfFormat"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationStatus"),
        ("LUM-CLIENT-MIB", "clientIfDuplexCapability"),
        ("LUM-CLIENT-MIB", "clientIfFlowControlMode"),
        ("LUM-CLIENT-MIB", "clientIfInterPacketGap"),
        ("LUM-CLIENT-MIB", "clientIfFrameSize"),
        ("LUM-CLIENT-MIB", "clientIfGfpMode"),
        ("LUM-CLIENT-MIB", "clientIfBandWidth"),
        ("LUM-CLIENT-MIB", "clientIfRateLimit"),
        ("LUM-CLIENT-MIB", "clientIfTrxClass"),
        ("LUM-CLIENT-MIB", "clientIfLaserBias"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfReceiverSensitivity"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevelLowRelativeThreshold"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSignal"),
        ("LUM-CLIENT-MIB", "clientIfLossOfFrame"),
        ("LUM-CLIENT-MIB", "clientIfBitrateMismatch"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfTransmitterFailed"),
        ("LUM-CLIENT-MIB", "clientIfTrxCodeMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTrxBitrateUnavailable"),
        ("LUM-CLIENT-MIB", "clientIfTrxMissing"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerHigh"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerLow"),
        ("LUM-CLIENT-MIB", "clientIfLinkDown"),
        ("LUM-CLIENT-MIB", "clientIfConfigurationCommand"),
        ("LUM-CLIENT-MIB", "clientIfGbeUtilization"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSync"),
        ("LUM-CLIENT-MIB", "clientIfConfigureTrxModeCommand"),
        ("LUM-CLIENT-MIB", "clientIfTrxMode"),
        ("LUM-CLIENT-MIB", "clientIfExpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfUnexpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfIllegalFrequency"),
        ("LUM-CLIENT-MIB", "clientIfLaserForcedOn"),
        ("LUM-CLIENT-MIB", "clientIfTrxMedia"),
        ("LUM-CLIENT-MIB", "clientIfTrxMediaMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTruncAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfObjectProperty"),
        ("LUM-CLIENT-MIB", "clientIfTxPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfLaserTempActual"),
        ("LUM-CLIENT-MIB", "clientIfTraceIntrusionMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceTransmitted"),
        ("LUM-CLIENT-MIB", "clientIfTraceReceived"),
        ("LUM-CLIENT-MIB", "clientIfTraceExpected"),
        ("LUM-CLIENT-MIB", "clientIfTraceAlarmMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceMismatch"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfMsAlarmIndicationSignalC2W"),
        ("LUM-CLIENT-MIB", "clientIfMsAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfRemoteDefectIndication"),
        ("LUM-CLIENT-MIB", "clientIfJ1TxTrailTrace"),
        ("LUM-CLIENT-MIB", "clientIfJ1TxTrailTraceInsertionMode"),
        ("LUM-CLIENT-MIB", "clientIfVcGroupFailedW2C"),
        ("LUM-CLIENT-MIB", "clientIfReadJ1"),
        ("LUM-CLIENT-MIB", "clientIfHighSpeed"),
        ("LUM-CLIENT-MIB", "clientIfActualFormat"),
        ("LUM-CLIENT-MIB", "clientIfRdiIntrusionMode"),
        ("LUM-CLIENT-MIB", "clientIfMuxQuadVc4"),
        ("LUM-CLIENT-MIB", "clientIfDemuxQuadVc4"),
        ("LUM-CLIENT-MIB", "clientIfCcConnectionMode"),
        ("LUM-CLIENT-MIB", "clientIfCcConfigurationCommand"))
)
if mibBuilder.loadTexts:
    clientIfGroupV9.setStatus("deprecated")

clientIfGroupV10 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 1, 15)
)
clientIfGroupV10.setObjects(
      *(("LUM-CLIENT-MIB", "clientIfIndex"),
        ("LUM-CLIENT-MIB", "clientIfName"),
        ("LUM-CLIENT-MIB", "clientIfSubrack"),
        ("LUM-CLIENT-MIB", "clientIfSlot"),
        ("LUM-CLIENT-MIB", "clientIfTxPort"),
        ("LUM-CLIENT-MIB", "clientIfRxPort"),
        ("LUM-CLIENT-MIB", "clientIfEntityId"),
        ("LUM-CLIENT-MIB", "clientIfAdminStatus"),
        ("LUM-CLIENT-MIB", "clientIfOperStatus"),
        ("LUM-CLIENT-MIB", "clientIfLaserStatus"),
        ("LUM-CLIENT-MIB", "clientIfTxSignalStatus"),
        ("LUM-CLIENT-MIB", "clientIfForwardAls"),
        ("LUM-CLIENT-MIB", "clientIfSuppressRemoteAlarms"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfFormat"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationStatus"),
        ("LUM-CLIENT-MIB", "clientIfDuplexCapability"),
        ("LUM-CLIENT-MIB", "clientIfFlowControlMode"),
        ("LUM-CLIENT-MIB", "clientIfInterPacketGap"),
        ("LUM-CLIENT-MIB", "clientIfFrameSize"),
        ("LUM-CLIENT-MIB", "clientIfGfpMode"),
        ("LUM-CLIENT-MIB", "clientIfBandWidth"),
        ("LUM-CLIENT-MIB", "clientIfRateLimit"),
        ("LUM-CLIENT-MIB", "clientIfTrxClass"),
        ("LUM-CLIENT-MIB", "clientIfLaserBias"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfReceiverSensitivity"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevelLowRelativeThreshold"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSignal"),
        ("LUM-CLIENT-MIB", "clientIfLossOfFrame"),
        ("LUM-CLIENT-MIB", "clientIfBitrateMismatch"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfTransmitterFailed"),
        ("LUM-CLIENT-MIB", "clientIfTrxCodeMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTrxBitrateUnavailable"),
        ("LUM-CLIENT-MIB", "clientIfTrxMissing"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerHigh"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerLow"),
        ("LUM-CLIENT-MIB", "clientIfLinkDown"),
        ("LUM-CLIENT-MIB", "clientIfConfigurationCommand"),
        ("LUM-CLIENT-MIB", "clientIfGbeUtilization"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSync"),
        ("LUM-CLIENT-MIB", "clientIfConfigureTrxModeCommand"),
        ("LUM-CLIENT-MIB", "clientIfTrxMode"),
        ("LUM-CLIENT-MIB", "clientIfExpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfUnexpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfIllegalFrequency"),
        ("LUM-CLIENT-MIB", "clientIfLaserForcedOn"),
        ("LUM-CLIENT-MIB", "clientIfTrxMedia"),
        ("LUM-CLIENT-MIB", "clientIfTrxMediaMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTruncAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfObjectProperty"),
        ("LUM-CLIENT-MIB", "clientIfTxPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfLaserTempActual"),
        ("LUM-CLIENT-MIB", "clientIfTraceIntrusionMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceTransmitted"),
        ("LUM-CLIENT-MIB", "clientIfTraceReceived"),
        ("LUM-CLIENT-MIB", "clientIfTraceExpected"),
        ("LUM-CLIENT-MIB", "clientIfTraceAlarmMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceMismatch"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfMsAlarmIndicationSignalC2W"),
        ("LUM-CLIENT-MIB", "clientIfMsAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfRemoteDefectIndication"),
        ("LUM-CLIENT-MIB", "clientIfJ1TxTrailTrace"),
        ("LUM-CLIENT-MIB", "clientIfJ1TxTrailTraceInsertionMode"),
        ("LUM-CLIENT-MIB", "clientIfVcGroupFailedW2C"),
        ("LUM-CLIENT-MIB", "clientIfReadJ1"),
        ("LUM-CLIENT-MIB", "clientIfHighSpeed"),
        ("LUM-CLIENT-MIB", "clientIfActualFormat"),
        ("LUM-CLIENT-MIB", "clientIfRdiIntrusionMode"),
        ("LUM-CLIENT-MIB", "clientIfMuxQuadVc4"),
        ("LUM-CLIENT-MIB", "clientIfDemuxQuadVc4"),
        ("LUM-CLIENT-MIB", "clientIfCcConnectionMode"),
        ("LUM-CLIENT-MIB", "clientIfCcConfigurationCommand"),
        ("LUM-CLIENT-MIB", "clientIfIllegalSignalFormat"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtPortId"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtGroupMemberPort"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtGroupStatus"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtActivePort"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtPortStatus"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtToggleActivePort"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopbackTimeout"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopbackEnabled"),
        ("LUM-CLIENT-MIB", "clientIfChangeNearEndLoopbackCommand"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopbackEnabled"))
)
if mibBuilder.loadTexts:
    clientIfGroupV10.setStatus("deprecated")

clientIfGroupV11 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 1, 16)
)
clientIfGroupV11.setObjects(
      *(("LUM-CLIENT-MIB", "clientIfIndex"),
        ("LUM-CLIENT-MIB", "clientIfName"),
        ("LUM-CLIENT-MIB", "clientIfSubrack"),
        ("LUM-CLIENT-MIB", "clientIfSlot"),
        ("LUM-CLIENT-MIB", "clientIfTxPort"),
        ("LUM-CLIENT-MIB", "clientIfRxPort"),
        ("LUM-CLIENT-MIB", "clientIfEntityId"),
        ("LUM-CLIENT-MIB", "clientIfAdminStatus"),
        ("LUM-CLIENT-MIB", "clientIfOperStatus"),
        ("LUM-CLIENT-MIB", "clientIfLaserStatus"),
        ("LUM-CLIENT-MIB", "clientIfTxSignalStatus"),
        ("LUM-CLIENT-MIB", "clientIfForwardAls"),
        ("LUM-CLIENT-MIB", "clientIfSuppressRemoteAlarms"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfFormat"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationStatus"),
        ("LUM-CLIENT-MIB", "clientIfDuplexCapability"),
        ("LUM-CLIENT-MIB", "clientIfFlowControlMode"),
        ("LUM-CLIENT-MIB", "clientIfInterPacketGap"),
        ("LUM-CLIENT-MIB", "clientIfFrameSize"),
        ("LUM-CLIENT-MIB", "clientIfGfpMode"),
        ("LUM-CLIENT-MIB", "clientIfBandWidth"),
        ("LUM-CLIENT-MIB", "clientIfRateLimit"),
        ("LUM-CLIENT-MIB", "clientIfTrxClass"),
        ("LUM-CLIENT-MIB", "clientIfLaserBias"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfReceiverSensitivity"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevelLowRelativeThreshold"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSignal"),
        ("LUM-CLIENT-MIB", "clientIfLossOfFrame"),
        ("LUM-CLIENT-MIB", "clientIfBitrateMismatch"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfTransmitterFailed"),
        ("LUM-CLIENT-MIB", "clientIfTrxCodeMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTrxBitrateUnavailable"),
        ("LUM-CLIENT-MIB", "clientIfTrxMissing"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerHigh"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerLow"),
        ("LUM-CLIENT-MIB", "clientIfLinkDown"),
        ("LUM-CLIENT-MIB", "clientIfConfigurationCommand"),
        ("LUM-CLIENT-MIB", "clientIfGbeUtilization"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSync"),
        ("LUM-CLIENT-MIB", "clientIfConfigureTrxModeCommand"),
        ("LUM-CLIENT-MIB", "clientIfTrxMode"),
        ("LUM-CLIENT-MIB", "clientIfExpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfUnexpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfIllegalFrequency"),
        ("LUM-CLIENT-MIB", "clientIfLaserForcedOn"),
        ("LUM-CLIENT-MIB", "clientIfTrxMedia"),
        ("LUM-CLIENT-MIB", "clientIfTrxMediaMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTruncAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfObjectProperty"),
        ("LUM-CLIENT-MIB", "clientIfTxPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfLaserTempActual"),
        ("LUM-CLIENT-MIB", "clientIfTraceIntrusionMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceTransmitted"),
        ("LUM-CLIENT-MIB", "clientIfTraceReceived"),
        ("LUM-CLIENT-MIB", "clientIfTraceExpected"),
        ("LUM-CLIENT-MIB", "clientIfTraceAlarmMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceMismatch"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfMsAlarmIndicationSignalC2W"),
        ("LUM-CLIENT-MIB", "clientIfMsAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfRemoteDefectIndication"),
        ("LUM-CLIENT-MIB", "clientIfJ1TxTrailTrace"),
        ("LUM-CLIENT-MIB", "clientIfJ1TxTrailTraceInsertionMode"),
        ("LUM-CLIENT-MIB", "clientIfVcGroupFailedW2C"),
        ("LUM-CLIENT-MIB", "clientIfReadJ1"),
        ("LUM-CLIENT-MIB", "clientIfHighSpeed"),
        ("LUM-CLIENT-MIB", "clientIfActualFormat"),
        ("LUM-CLIENT-MIB", "clientIfRdiIntrusionMode"),
        ("LUM-CLIENT-MIB", "clientIfMuxQuadVc4"),
        ("LUM-CLIENT-MIB", "clientIfDemuxQuadVc4"),
        ("LUM-CLIENT-MIB", "clientIfCcConnectionMode"),
        ("LUM-CLIENT-MIB", "clientIfCcConfigurationCommand"),
        ("LUM-CLIENT-MIB", "clientIfIllegalSignalFormat"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtPortId"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtGroupMemberPort"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtGroupStatus"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtActivePort"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtPortStatus"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtToggleActivePort"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopbackTimeout"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopbackEnabled"),
        ("LUM-CLIENT-MIB", "clientIfChangeNearEndLoopbackCommand"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopbackEnabled"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopbackTimeout"),
        ("LUM-CLIENT-MIB", "clientIfChangeFarEndLoopbackCommand"),
        ("LUM-CLIENT-MIB", "clientIfFormatNotSupportedByHw"),
        ("LUM-CLIENT-MIB", "clientIfLaserMode"),
        ("LUM-CLIENT-MIB", "clientIfAlarmIndicationSignalLineC2W"),
        ("LUM-CLIENT-MIB", "clientIfFarEndClientFailure"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparency"),
        ("LUM-CLIENT-MIB", "clientIfConnectedLine"))
)
if mibBuilder.loadTexts:
    clientIfGroupV11.setStatus("deprecated")

clientIfGroupV12 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 1, 17)
)
clientIfGroupV12.setObjects(
      *(("LUM-CLIENT-MIB", "clientIfIndex"),
        ("LUM-CLIENT-MIB", "clientIfName"),
        ("LUM-CLIENT-MIB", "clientIfSubrack"),
        ("LUM-CLIENT-MIB", "clientIfSlot"),
        ("LUM-CLIENT-MIB", "clientIfTxPort"),
        ("LUM-CLIENT-MIB", "clientIfRxPort"),
        ("LUM-CLIENT-MIB", "clientIfEntityId"),
        ("LUM-CLIENT-MIB", "clientIfAdminStatus"),
        ("LUM-CLIENT-MIB", "clientIfOperStatus"),
        ("LUM-CLIENT-MIB", "clientIfLaserStatus"),
        ("LUM-CLIENT-MIB", "clientIfTxSignalStatus"),
        ("LUM-CLIENT-MIB", "clientIfForwardAls"),
        ("LUM-CLIENT-MIB", "clientIfSuppressRemoteAlarms"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfFormat"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationStatus"),
        ("LUM-CLIENT-MIB", "clientIfDuplexCapability"),
        ("LUM-CLIENT-MIB", "clientIfFlowControlMode"),
        ("LUM-CLIENT-MIB", "clientIfInterPacketGap"),
        ("LUM-CLIENT-MIB", "clientIfFrameSize"),
        ("LUM-CLIENT-MIB", "clientIfGfpMode"),
        ("LUM-CLIENT-MIB", "clientIfBandWidth"),
        ("LUM-CLIENT-MIB", "clientIfRateLimit"),
        ("LUM-CLIENT-MIB", "clientIfTrxClass"),
        ("LUM-CLIENT-MIB", "clientIfLaserBias"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfReceiverSensitivity"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevelLowRelativeThreshold"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSignal"),
        ("LUM-CLIENT-MIB", "clientIfLossOfFrame"),
        ("LUM-CLIENT-MIB", "clientIfBitrateMismatch"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfTransmitterFailed"),
        ("LUM-CLIENT-MIB", "clientIfTrxCodeMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTrxBitrateUnavailable"),
        ("LUM-CLIENT-MIB", "clientIfTrxMissing"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerHigh"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerLow"),
        ("LUM-CLIENT-MIB", "clientIfLinkDown"),
        ("LUM-CLIENT-MIB", "clientIfConfigurationCommand"),
        ("LUM-CLIENT-MIB", "clientIfGbeUtilization"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSync"),
        ("LUM-CLIENT-MIB", "clientIfConfigureTrxModeCommand"),
        ("LUM-CLIENT-MIB", "clientIfTrxMode"),
        ("LUM-CLIENT-MIB", "clientIfExpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfUnexpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfIllegalFrequency"),
        ("LUM-CLIENT-MIB", "clientIfLaserForcedOn"),
        ("LUM-CLIENT-MIB", "clientIfTrxMedia"),
        ("LUM-CLIENT-MIB", "clientIfTrxMediaMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTruncAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfObjectProperty"),
        ("LUM-CLIENT-MIB", "clientIfTxPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfLaserTempActual"),
        ("LUM-CLIENT-MIB", "clientIfTraceIntrusionMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceTransmitted"),
        ("LUM-CLIENT-MIB", "clientIfTraceReceived"),
        ("LUM-CLIENT-MIB", "clientIfTraceExpected"),
        ("LUM-CLIENT-MIB", "clientIfTraceAlarmMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceMismatch"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfMsAlarmIndicationSignalC2W"),
        ("LUM-CLIENT-MIB", "clientIfMsAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfRemoteDefectIndication"),
        ("LUM-CLIENT-MIB", "clientIfJ1TxTrailTrace"),
        ("LUM-CLIENT-MIB", "clientIfJ1TxTrailTraceInsertionMode"),
        ("LUM-CLIENT-MIB", "clientIfVcGroupFailedW2C"),
        ("LUM-CLIENT-MIB", "clientIfReadJ1"),
        ("LUM-CLIENT-MIB", "clientIfHighSpeed"),
        ("LUM-CLIENT-MIB", "clientIfActualFormat"),
        ("LUM-CLIENT-MIB", "clientIfRdiIntrusionMode"),
        ("LUM-CLIENT-MIB", "clientIfMuxQuadVc4"),
        ("LUM-CLIENT-MIB", "clientIfDemuxQuadVc4"),
        ("LUM-CLIENT-MIB", "clientIfCcConnectionMode"),
        ("LUM-CLIENT-MIB", "clientIfCcConfigurationCommand"),
        ("LUM-CLIENT-MIB", "clientIfIllegalSignalFormat"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtPortId"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtGroupMemberPort"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtGroupStatus"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtActivePort"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtPortStatus"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtToggleActivePort"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopbackTimeout"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopbackEnabled"),
        ("LUM-CLIENT-MIB", "clientIfChangeNearEndLoopbackCommand"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopbackEnabled"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopbackTimeout"),
        ("LUM-CLIENT-MIB", "clientIfChangeFarEndLoopbackCommand"),
        ("LUM-CLIENT-MIB", "clientIfFormatNotSupportedByHw"),
        ("LUM-CLIENT-MIB", "clientIfLaserMode"),
        ("LUM-CLIENT-MIB", "clientIfAlarmIndicationSignalLineC2W"),
        ("LUM-CLIENT-MIB", "clientIfFarEndClientFailure"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparency"),
        ("LUM-CLIENT-MIB", "clientIfConnectedLine"),
        ("LUM-CLIENT-MIB", "clientIfForwardingErrorCorrectionMode"),
        ("LUM-CLIENT-MIB", "clientIfNoFrequencySet"),
        ("LUM-CLIENT-MIB", "clientIfJitterAttenuatorBW"),
        ("LUM-CLIENT-MIB", "clientIfConnectionStatus"),
        ("LUM-CLIENT-MIB", "clientIfLoopFilterUnlocked"),
        ("LUM-CLIENT-MIB", "clientIfCableLength"),
        ("LUM-CLIENT-MIB", "clientIfConnectedForeignIndex"),
        ("LUM-CLIENT-MIB", "clientIfDisconnect"))
)
if mibBuilder.loadTexts:
    clientIfGroupV12.setStatus("deprecated")

clientIfGroupV13 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 1, 18)
)
clientIfGroupV13.setObjects(
      *(("LUM-CLIENT-MIB", "clientIfIndex"),
        ("LUM-CLIENT-MIB", "clientIfName"),
        ("LUM-CLIENT-MIB", "clientIfSubrack"),
        ("LUM-CLIENT-MIB", "clientIfSlot"),
        ("LUM-CLIENT-MIB", "clientIfTxPort"),
        ("LUM-CLIENT-MIB", "clientIfRxPort"),
        ("LUM-CLIENT-MIB", "clientIfEntityId"),
        ("LUM-CLIENT-MIB", "clientIfAdminStatus"),
        ("LUM-CLIENT-MIB", "clientIfOperStatus"),
        ("LUM-CLIENT-MIB", "clientIfLaserStatus"),
        ("LUM-CLIENT-MIB", "clientIfTxSignalStatus"),
        ("LUM-CLIENT-MIB", "clientIfForwardAls"),
        ("LUM-CLIENT-MIB", "clientIfSuppressRemoteAlarms"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfFormat"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationStatus"),
        ("LUM-CLIENT-MIB", "clientIfDuplexCapability"),
        ("LUM-CLIENT-MIB", "clientIfFlowControlMode"),
        ("LUM-CLIENT-MIB", "clientIfInterPacketGap"),
        ("LUM-CLIENT-MIB", "clientIfFrameSize"),
        ("LUM-CLIENT-MIB", "clientIfGfpMode"),
        ("LUM-CLIENT-MIB", "clientIfBandWidth"),
        ("LUM-CLIENT-MIB", "clientIfRateLimit"),
        ("LUM-CLIENT-MIB", "clientIfTrxClass"),
        ("LUM-CLIENT-MIB", "clientIfLaserBias"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfReceiverSensitivity"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevelLowRelativeThreshold"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSignal"),
        ("LUM-CLIENT-MIB", "clientIfLossOfFrame"),
        ("LUM-CLIENT-MIB", "clientIfBitrateMismatch"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfTransmitterFailed"),
        ("LUM-CLIENT-MIB", "clientIfTrxCodeMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTrxBitrateUnavailable"),
        ("LUM-CLIENT-MIB", "clientIfTrxMissing"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerHigh"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerLow"),
        ("LUM-CLIENT-MIB", "clientIfLinkDown"),
        ("LUM-CLIENT-MIB", "clientIfConfigurationCommand"),
        ("LUM-CLIENT-MIB", "clientIfGbeUtilization"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSync"),
        ("LUM-CLIENT-MIB", "clientIfConfigureTrxModeCommand"),
        ("LUM-CLIENT-MIB", "clientIfTrxMode"),
        ("LUM-CLIENT-MIB", "clientIfExpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfUnexpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfIllegalFrequency"),
        ("LUM-CLIENT-MIB", "clientIfLaserForcedOn"),
        ("LUM-CLIENT-MIB", "clientIfTrxMedia"),
        ("LUM-CLIENT-MIB", "clientIfTrxMediaMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTruncAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfObjectProperty"),
        ("LUM-CLIENT-MIB", "clientIfTxPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfLaserTempActual"),
        ("LUM-CLIENT-MIB", "clientIfTraceIntrusionMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceTransmitted"),
        ("LUM-CLIENT-MIB", "clientIfTraceReceived"),
        ("LUM-CLIENT-MIB", "clientIfTraceExpected"),
        ("LUM-CLIENT-MIB", "clientIfTraceAlarmMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceMismatch"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfMsAlarmIndicationSignalC2W"),
        ("LUM-CLIENT-MIB", "clientIfMsAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfRemoteDefectIndication"),
        ("LUM-CLIENT-MIB", "clientIfJ1TxTrailTrace"),
        ("LUM-CLIENT-MIB", "clientIfJ1TxTrailTraceInsertionMode"),
        ("LUM-CLIENT-MIB", "clientIfVcGroupFailedW2C"),
        ("LUM-CLIENT-MIB", "clientIfReadJ1"),
        ("LUM-CLIENT-MIB", "clientIfHighSpeed"),
        ("LUM-CLIENT-MIB", "clientIfActualFormat"),
        ("LUM-CLIENT-MIB", "clientIfRdiIntrusionMode"),
        ("LUM-CLIENT-MIB", "clientIfMuxQuadVc4"),
        ("LUM-CLIENT-MIB", "clientIfDemuxQuadVc4"),
        ("LUM-CLIENT-MIB", "clientIfCcConnectionMode"),
        ("LUM-CLIENT-MIB", "clientIfCcConfigurationCommand"),
        ("LUM-CLIENT-MIB", "clientIfIllegalSignalFormat"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtPortId"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtGroupMemberPort"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtGroupStatus"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtActivePort"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtPortStatus"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtToggleActivePort"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopbackTimeout"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopbackEnabled"),
        ("LUM-CLIENT-MIB", "clientIfChangeNearEndLoopbackCommand"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopbackEnabled"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopbackTimeout"),
        ("LUM-CLIENT-MIB", "clientIfChangeFarEndLoopbackCommand"),
        ("LUM-CLIENT-MIB", "clientIfFormatNotSupportedByHw"),
        ("LUM-CLIENT-MIB", "clientIfLaserMode"),
        ("LUM-CLIENT-MIB", "clientIfAlarmIndicationSignalLineC2W"),
        ("LUM-CLIENT-MIB", "clientIfFarEndClientFailure"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparency"),
        ("LUM-CLIENT-MIB", "clientIfConnectedLine"),
        ("LUM-CLIENT-MIB", "clientIfForwardingErrorCorrectionMode"),
        ("LUM-CLIENT-MIB", "clientIfNoFrequencySet"),
        ("LUM-CLIENT-MIB", "clientIfJitterAttenuatorBW"),
        ("LUM-CLIENT-MIB", "clientIfConnectionStatus"),
        ("LUM-CLIENT-MIB", "clientIfLoopFilterUnlocked"),
        ("LUM-CLIENT-MIB", "clientIfCableLength"),
        ("LUM-CLIENT-MIB", "clientIfConnectedForeignIndex"),
        ("LUM-CLIENT-MIB", "clientIfDisconnect"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparencyBitMask"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparencyString"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparencySet"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalC2W"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerC2W"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerW2C"))
)
if mibBuilder.loadTexts:
    clientIfGroupV13.setStatus("deprecated")

clientVc4GroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 1, 19)
)
clientVc4GroupV2.setObjects(
      *(("LUM-CLIENT-MIB", "clientVc4Index"),
        ("LUM-CLIENT-MIB", "clientVc4Name"),
        ("LUM-CLIENT-MIB", "clientVc4Descr"),
        ("LUM-CLIENT-MIB", "clientVc4Subrack"),
        ("LUM-CLIENT-MIB", "clientVc4Slot"),
        ("LUM-CLIENT-MIB", "clientVc4TxPort"),
        ("LUM-CLIENT-MIB", "clientVc4RxPort"),
        ("LUM-CLIENT-MIB", "clientVc4Vc4"),
        ("LUM-CLIENT-MIB", "clientVc4ObjectProperty"),
        ("LUM-CLIENT-MIB", "clientVc4AuAlarmIndicationSignal"),
        ("LUM-CLIENT-MIB", "clientVc4AuLossOfPointer"),
        ("LUM-CLIENT-MIB", "clientVc4RxSignalStatus"),
        ("LUM-CLIENT-MIB", "clientVc4ConcatenationStatus"),
        ("LUM-CLIENT-MIB", "clientVc4PayloadStatus"),
        ("LUM-CLIENT-MIB", "clientVc4ConnectionStatus"))
)
if mibBuilder.loadTexts:
    clientVc4GroupV2.setStatus("current")

clientIfGroupV14 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 1, 20)
)
clientIfGroupV14.setObjects(
      *(("LUM-CLIENT-MIB", "clientIfIndex"),
        ("LUM-CLIENT-MIB", "clientIfName"),
        ("LUM-CLIENT-MIB", "clientIfSubrack"),
        ("LUM-CLIENT-MIB", "clientIfSlot"),
        ("LUM-CLIENT-MIB", "clientIfTxPort"),
        ("LUM-CLIENT-MIB", "clientIfRxPort"),
        ("LUM-CLIENT-MIB", "clientIfEntityId"),
        ("LUM-CLIENT-MIB", "clientIfAdminStatus"),
        ("LUM-CLIENT-MIB", "clientIfOperStatus"),
        ("LUM-CLIENT-MIB", "clientIfLaserStatus"),
        ("LUM-CLIENT-MIB", "clientIfTxSignalStatus"),
        ("LUM-CLIENT-MIB", "clientIfForwardAls"),
        ("LUM-CLIENT-MIB", "clientIfSuppressRemoteAlarms"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfFormat"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationStatus"),
        ("LUM-CLIENT-MIB", "clientIfDuplexCapability"),
        ("LUM-CLIENT-MIB", "clientIfFlowControlMode"),
        ("LUM-CLIENT-MIB", "clientIfInterPacketGap"),
        ("LUM-CLIENT-MIB", "clientIfFrameSize"),
        ("LUM-CLIENT-MIB", "clientIfGfpMode"),
        ("LUM-CLIENT-MIB", "clientIfBandWidth"),
        ("LUM-CLIENT-MIB", "clientIfRateLimit"),
        ("LUM-CLIENT-MIB", "clientIfTrxClass"),
        ("LUM-CLIENT-MIB", "clientIfLaserBias"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfReceiverSensitivity"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevelLowRelativeThreshold"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSignal"),
        ("LUM-CLIENT-MIB", "clientIfLossOfFrame"),
        ("LUM-CLIENT-MIB", "clientIfBitrateMismatch"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfTransmitterFailed"),
        ("LUM-CLIENT-MIB", "clientIfTrxCodeMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTrxBitrateUnavailable"),
        ("LUM-CLIENT-MIB", "clientIfTrxMissing"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerHigh"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerLow"),
        ("LUM-CLIENT-MIB", "clientIfLinkDown"),
        ("LUM-CLIENT-MIB", "clientIfConfigurationCommand"),
        ("LUM-CLIENT-MIB", "clientIfGbeUtilization"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSync"),
        ("LUM-CLIENT-MIB", "clientIfConfigureTrxModeCommand"),
        ("LUM-CLIENT-MIB", "clientIfTrxMode"),
        ("LUM-CLIENT-MIB", "clientIfExpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfUnexpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfIllegalFrequency"),
        ("LUM-CLIENT-MIB", "clientIfLaserForcedOn"),
        ("LUM-CLIENT-MIB", "clientIfTrxMedia"),
        ("LUM-CLIENT-MIB", "clientIfTrxMediaMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTruncAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfObjectProperty"),
        ("LUM-CLIENT-MIB", "clientIfTxPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfLaserTempActual"),
        ("LUM-CLIENT-MIB", "clientIfTraceIntrusionMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceTransmitted"),
        ("LUM-CLIENT-MIB", "clientIfTraceReceived"),
        ("LUM-CLIENT-MIB", "clientIfTraceExpected"),
        ("LUM-CLIENT-MIB", "clientIfTraceAlarmMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceMismatch"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfMsAlarmIndicationSignalC2W"),
        ("LUM-CLIENT-MIB", "clientIfMsAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfRemoteDefectIndication"),
        ("LUM-CLIENT-MIB", "clientIfJ1TxTrailTrace"),
        ("LUM-CLIENT-MIB", "clientIfJ1TxTrailTraceInsertionMode"),
        ("LUM-CLIENT-MIB", "clientIfVcGroupFailedW2C"),
        ("LUM-CLIENT-MIB", "clientIfReadJ1"),
        ("LUM-CLIENT-MIB", "clientIfHighSpeed"),
        ("LUM-CLIENT-MIB", "clientIfActualFormat"),
        ("LUM-CLIENT-MIB", "clientIfRdiIntrusionMode"),
        ("LUM-CLIENT-MIB", "clientIfMuxQuadVc4"),
        ("LUM-CLIENT-MIB", "clientIfDemuxQuadVc4"),
        ("LUM-CLIENT-MIB", "clientIfCcConnectionMode"),
        ("LUM-CLIENT-MIB", "clientIfCcConfigurationCommand"),
        ("LUM-CLIENT-MIB", "clientIfIllegalSignalFormat"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtPortId"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtGroupMemberPort"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtGroupStatus"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtActivePort"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtPortStatus"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtToggleActivePort"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopbackTimeout"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopbackEnabled"),
        ("LUM-CLIENT-MIB", "clientIfChangeNearEndLoopbackCommand"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopbackEnabled"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopbackTimeout"),
        ("LUM-CLIENT-MIB", "clientIfChangeFarEndLoopbackCommand"),
        ("LUM-CLIENT-MIB", "clientIfFormatNotSupportedByHw"),
        ("LUM-CLIENT-MIB", "clientIfLaserMode"),
        ("LUM-CLIENT-MIB", "clientIfAlarmIndicationSignalLineC2W"),
        ("LUM-CLIENT-MIB", "clientIfFarEndClientFailure"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparency"),
        ("LUM-CLIENT-MIB", "clientIfConnectedLine"),
        ("LUM-CLIENT-MIB", "clientIfForwardingErrorCorrectionMode"),
        ("LUM-CLIENT-MIB", "clientIfNoFrequencySet"),
        ("LUM-CLIENT-MIB", "clientIfJitterAttenuatorBW"),
        ("LUM-CLIENT-MIB", "clientIfConnectionStatus"),
        ("LUM-CLIENT-MIB", "clientIfLoopFilterUnlocked"),
        ("LUM-CLIENT-MIB", "clientIfCableLength"),
        ("LUM-CLIENT-MIB", "clientIfConnectedForeignIndex"),
        ("LUM-CLIENT-MIB", "clientIfDisconnect"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparencyBitMask"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparencyString"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparencySet"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalC2W"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerC2W"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerW2C"),
        ("LUM-CLIENT-MIB", "clientIfEthStandbyIndicator"))
)
if mibBuilder.loadTexts:
    clientIfGroupV14.setStatus("deprecated")

clientIfGroupV15 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 1, 21)
)
clientIfGroupV15.setObjects(
      *(("LUM-CLIENT-MIB", "clientIfIndex"),
        ("LUM-CLIENT-MIB", "clientIfName"),
        ("LUM-CLIENT-MIB", "clientIfSubrack"),
        ("LUM-CLIENT-MIB", "clientIfSlot"),
        ("LUM-CLIENT-MIB", "clientIfTxPort"),
        ("LUM-CLIENT-MIB", "clientIfRxPort"),
        ("LUM-CLIENT-MIB", "clientIfEntityId"),
        ("LUM-CLIENT-MIB", "clientIfAdminStatus"),
        ("LUM-CLIENT-MIB", "clientIfOperStatus"),
        ("LUM-CLIENT-MIB", "clientIfLaserStatus"),
        ("LUM-CLIENT-MIB", "clientIfTxSignalStatus"),
        ("LUM-CLIENT-MIB", "clientIfForwardAls"),
        ("LUM-CLIENT-MIB", "clientIfSuppressRemoteAlarms"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfFormat"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationStatus"),
        ("LUM-CLIENT-MIB", "clientIfDuplexCapability"),
        ("LUM-CLIENT-MIB", "clientIfFlowControlMode"),
        ("LUM-CLIENT-MIB", "clientIfInterPacketGap"),
        ("LUM-CLIENT-MIB", "clientIfFrameSize"),
        ("LUM-CLIENT-MIB", "clientIfGfpMode"),
        ("LUM-CLIENT-MIB", "clientIfBandWidth"),
        ("LUM-CLIENT-MIB", "clientIfRateLimit"),
        ("LUM-CLIENT-MIB", "clientIfTrxClass"),
        ("LUM-CLIENT-MIB", "clientIfLaserBias"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfReceiverSensitivity"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevelLowRelativeThreshold"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSignal"),
        ("LUM-CLIENT-MIB", "clientIfLossOfFrame"),
        ("LUM-CLIENT-MIB", "clientIfBitrateMismatch"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfTransmitterFailed"),
        ("LUM-CLIENT-MIB", "clientIfTrxCodeMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTrxBitrateUnavailable"),
        ("LUM-CLIENT-MIB", "clientIfTrxMissing"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerHigh"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerLow"),
        ("LUM-CLIENT-MIB", "clientIfLinkDown"),
        ("LUM-CLIENT-MIB", "clientIfConfigurationCommand"),
        ("LUM-CLIENT-MIB", "clientIfGbeUtilization"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSync"),
        ("LUM-CLIENT-MIB", "clientIfConfigureTrxModeCommand"),
        ("LUM-CLIENT-MIB", "clientIfTrxMode"),
        ("LUM-CLIENT-MIB", "clientIfExpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfUnexpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfIllegalFrequency"),
        ("LUM-CLIENT-MIB", "clientIfLaserForcedOn"),
        ("LUM-CLIENT-MIB", "clientIfTrxMedia"),
        ("LUM-CLIENT-MIB", "clientIfTrxMediaMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTruncAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfObjectProperty"),
        ("LUM-CLIENT-MIB", "clientIfTxPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfLaserTempActual"),
        ("LUM-CLIENT-MIB", "clientIfTraceIntrusionMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceTransmitted"),
        ("LUM-CLIENT-MIB", "clientIfTraceReceived"),
        ("LUM-CLIENT-MIB", "clientIfTraceExpected"),
        ("LUM-CLIENT-MIB", "clientIfTraceAlarmMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceMismatch"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfMsAlarmIndicationSignalC2W"),
        ("LUM-CLIENT-MIB", "clientIfMsAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfRemoteDefectIndication"),
        ("LUM-CLIENT-MIB", "clientIfJ1TxTrailTrace"),
        ("LUM-CLIENT-MIB", "clientIfJ1TxTrailTraceInsertionMode"),
        ("LUM-CLIENT-MIB", "clientIfVcGroupFailedW2C"),
        ("LUM-CLIENT-MIB", "clientIfReadJ1"),
        ("LUM-CLIENT-MIB", "clientIfHighSpeed"),
        ("LUM-CLIENT-MIB", "clientIfActualFormat"),
        ("LUM-CLIENT-MIB", "clientIfRdiIntrusionMode"),
        ("LUM-CLIENT-MIB", "clientIfMuxQuadVc4"),
        ("LUM-CLIENT-MIB", "clientIfDemuxQuadVc4"),
        ("LUM-CLIENT-MIB", "clientIfCcConnectionMode"),
        ("LUM-CLIENT-MIB", "clientIfCcConfigurationCommand"),
        ("LUM-CLIENT-MIB", "clientIfIllegalSignalFormat"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtPortId"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtGroupMemberPort"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtGroupStatus"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtActivePort"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtPortStatus"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtToggleActivePort"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopbackTimeout"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopbackEnabled"),
        ("LUM-CLIENT-MIB", "clientIfChangeNearEndLoopbackCommand"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopbackEnabled"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopbackTimeout"),
        ("LUM-CLIENT-MIB", "clientIfChangeFarEndLoopbackCommand"),
        ("LUM-CLIENT-MIB", "clientIfFormatNotSupportedByHw"),
        ("LUM-CLIENT-MIB", "clientIfLaserMode"),
        ("LUM-CLIENT-MIB", "clientIfAlarmIndicationSignalLineC2W"),
        ("LUM-CLIENT-MIB", "clientIfFarEndClientFailure"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparency"),
        ("LUM-CLIENT-MIB", "clientIfConnectedLine"),
        ("LUM-CLIENT-MIB", "clientIfForwardingErrorCorrectionMode"),
        ("LUM-CLIENT-MIB", "clientIfNoFrequencySet"),
        ("LUM-CLIENT-MIB", "clientIfJitterAttenuatorBW"),
        ("LUM-CLIENT-MIB", "clientIfConnectionStatus"),
        ("LUM-CLIENT-MIB", "clientIfLoopFilterUnlocked"),
        ("LUM-CLIENT-MIB", "clientIfCableLength"),
        ("LUM-CLIENT-MIB", "clientIfConnectedForeignIndex"),
        ("LUM-CLIENT-MIB", "clientIfDisconnect"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparencyBitMask"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparencyString"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparencySet"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalC2W"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerC2W"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerW2C"),
        ("LUM-CLIENT-MIB", "clientIfEthStandbyIndicator"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalW2CSonet"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalC2WSonet"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerC2WSonet"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerW2CSonet"))
)
if mibBuilder.loadTexts:
    clientIfGroupV15.setStatus("deprecated")

clientIfGroupV16 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 1, 22)
)
clientIfGroupV16.setObjects(
      *(("LUM-CLIENT-MIB", "clientIfIndex"),
        ("LUM-CLIENT-MIB", "clientIfName"),
        ("LUM-CLIENT-MIB", "clientIfSubrack"),
        ("LUM-CLIENT-MIB", "clientIfSlot"),
        ("LUM-CLIENT-MIB", "clientIfTxPort"),
        ("LUM-CLIENT-MIB", "clientIfRxPort"),
        ("LUM-CLIENT-MIB", "clientIfEntityId"),
        ("LUM-CLIENT-MIB", "clientIfAdminStatus"),
        ("LUM-CLIENT-MIB", "clientIfOperStatus"),
        ("LUM-CLIENT-MIB", "clientIfLaserStatus"),
        ("LUM-CLIENT-MIB", "clientIfTxSignalStatus"),
        ("LUM-CLIENT-MIB", "clientIfForwardAls"),
        ("LUM-CLIENT-MIB", "clientIfSuppressRemoteAlarms"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfFormat"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationStatus"),
        ("LUM-CLIENT-MIB", "clientIfDuplexCapability"),
        ("LUM-CLIENT-MIB", "clientIfFlowControlMode"),
        ("LUM-CLIENT-MIB", "clientIfInterPacketGap"),
        ("LUM-CLIENT-MIB", "clientIfFrameSize"),
        ("LUM-CLIENT-MIB", "clientIfGfpMode"),
        ("LUM-CLIENT-MIB", "clientIfBandWidth"),
        ("LUM-CLIENT-MIB", "clientIfRateLimit"),
        ("LUM-CLIENT-MIB", "clientIfTrxClass"),
        ("LUM-CLIENT-MIB", "clientIfLaserBias"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfReceiverSensitivity"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevelLowRelativeThreshold"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSignal"),
        ("LUM-CLIENT-MIB", "clientIfLossOfFrame"),
        ("LUM-CLIENT-MIB", "clientIfBitrateMismatch"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfTransmitterFailed"),
        ("LUM-CLIENT-MIB", "clientIfTrxCodeMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTrxBitrateUnavailable"),
        ("LUM-CLIENT-MIB", "clientIfTrxMissing"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerHigh"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerLow"),
        ("LUM-CLIENT-MIB", "clientIfLinkDown"),
        ("LUM-CLIENT-MIB", "clientIfConfigurationCommand"),
        ("LUM-CLIENT-MIB", "clientIfGbeUtilization"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSync"),
        ("LUM-CLIENT-MIB", "clientIfConfigureTrxModeCommand"),
        ("LUM-CLIENT-MIB", "clientIfTrxMode"),
        ("LUM-CLIENT-MIB", "clientIfExpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfUnexpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfIllegalFrequency"),
        ("LUM-CLIENT-MIB", "clientIfLaserForcedOn"),
        ("LUM-CLIENT-MIB", "clientIfTrxMedia"),
        ("LUM-CLIENT-MIB", "clientIfTrxMediaMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTruncAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfObjectProperty"),
        ("LUM-CLIENT-MIB", "clientIfTxPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfLaserTempActual"),
        ("LUM-CLIENT-MIB", "clientIfTraceIntrusionMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceTransmitted"),
        ("LUM-CLIENT-MIB", "clientIfTraceReceived"),
        ("LUM-CLIENT-MIB", "clientIfTraceExpected"),
        ("LUM-CLIENT-MIB", "clientIfTraceAlarmMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceMismatch"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfMsAlarmIndicationSignalC2W"),
        ("LUM-CLIENT-MIB", "clientIfMsAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfRemoteDefectIndication"),
        ("LUM-CLIENT-MIB", "clientIfJ1TxTrailTrace"),
        ("LUM-CLIENT-MIB", "clientIfJ1TxTrailTraceInsertionMode"),
        ("LUM-CLIENT-MIB", "clientIfVcGroupFailedW2C"),
        ("LUM-CLIENT-MIB", "clientIfReadJ1"),
        ("LUM-CLIENT-MIB", "clientIfHighSpeed"),
        ("LUM-CLIENT-MIB", "clientIfActualFormat"),
        ("LUM-CLIENT-MIB", "clientIfRdiIntrusionMode"),
        ("LUM-CLIENT-MIB", "clientIfMuxQuadVc4"),
        ("LUM-CLIENT-MIB", "clientIfDemuxQuadVc4"),
        ("LUM-CLIENT-MIB", "clientIfCcConnectionMode"),
        ("LUM-CLIENT-MIB", "clientIfCcConfigurationCommand"),
        ("LUM-CLIENT-MIB", "clientIfIllegalSignalFormat"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtPortId"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtGroupMemberPort"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtGroupStatus"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtActivePort"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtPortStatus"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtToggleActivePort"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopbackTimeout"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopbackEnabled"),
        ("LUM-CLIENT-MIB", "clientIfChangeNearEndLoopbackCommand"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopbackEnabled"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopbackTimeout"),
        ("LUM-CLIENT-MIB", "clientIfChangeFarEndLoopbackCommand"),
        ("LUM-CLIENT-MIB", "clientIfFormatNotSupportedByHw"),
        ("LUM-CLIENT-MIB", "clientIfLaserMode"),
        ("LUM-CLIENT-MIB", "clientIfAlarmIndicationSignalLineC2W"),
        ("LUM-CLIENT-MIB", "clientIfFarEndClientFailure"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparency"),
        ("LUM-CLIENT-MIB", "clientIfConnectedLine"),
        ("LUM-CLIENT-MIB", "clientIfForwardingErrorCorrectionMode"),
        ("LUM-CLIENT-MIB", "clientIfNoFrequencySet"),
        ("LUM-CLIENT-MIB", "clientIfJitterAttenuatorBW"),
        ("LUM-CLIENT-MIB", "clientIfConnectionStatus"),
        ("LUM-CLIENT-MIB", "clientIfLoopFilterUnlocked"),
        ("LUM-CLIENT-MIB", "clientIfCableLength"),
        ("LUM-CLIENT-MIB", "clientIfConnectedForeignIndex"),
        ("LUM-CLIENT-MIB", "clientIfDisconnect"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparencyBitMask"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparencyString"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparencySet"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalC2W"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerC2W"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerW2C"),
        ("LUM-CLIENT-MIB", "clientIfEthStandbyIndicator"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalW2CSonet"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalC2WSonet"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerC2WSonet"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerW2CSonet"),
        ("LUM-CLIENT-MIB", "clientIfTransceiverNoLoopback"),
        ("LUM-CLIENT-MIB", "clientIfFecFailure"))
)
if mibBuilder.loadTexts:
    clientIfGroupV16.setStatus("deprecated")

clientIfGroupV17 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 1, 23)
)
clientIfGroupV17.setObjects(
      *(("LUM-CLIENT-MIB", "clientIfIndex"),
        ("LUM-CLIENT-MIB", "clientIfName"),
        ("LUM-CLIENT-MIB", "clientIfSubrack"),
        ("LUM-CLIENT-MIB", "clientIfSlot"),
        ("LUM-CLIENT-MIB", "clientIfTxPort"),
        ("LUM-CLIENT-MIB", "clientIfRxPort"),
        ("LUM-CLIENT-MIB", "clientIfEntityId"),
        ("LUM-CLIENT-MIB", "clientIfAdminStatus"),
        ("LUM-CLIENT-MIB", "clientIfOperStatus"),
        ("LUM-CLIENT-MIB", "clientIfLaserStatus"),
        ("LUM-CLIENT-MIB", "clientIfTxSignalStatus"),
        ("LUM-CLIENT-MIB", "clientIfForwardAls"),
        ("LUM-CLIENT-MIB", "clientIfSuppressRemoteAlarms"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfFormat"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationStatus"),
        ("LUM-CLIENT-MIB", "clientIfDuplexCapability"),
        ("LUM-CLIENT-MIB", "clientIfFlowControlMode"),
        ("LUM-CLIENT-MIB", "clientIfInterPacketGap"),
        ("LUM-CLIENT-MIB", "clientIfFrameSize"),
        ("LUM-CLIENT-MIB", "clientIfGfpMode"),
        ("LUM-CLIENT-MIB", "clientIfBandWidth"),
        ("LUM-CLIENT-MIB", "clientIfRateLimit"),
        ("LUM-CLIENT-MIB", "clientIfTrxClass"),
        ("LUM-CLIENT-MIB", "clientIfLaserBias"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfReceiverSensitivity"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevelLowRelativeThreshold"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSignal"),
        ("LUM-CLIENT-MIB", "clientIfLossOfFrame"),
        ("LUM-CLIENT-MIB", "clientIfBitrateMismatch"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfTransmitterFailed"),
        ("LUM-CLIENT-MIB", "clientIfTrxCodeMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTrxBitrateUnavailable"),
        ("LUM-CLIENT-MIB", "clientIfTrxMissing"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerHigh"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerLow"),
        ("LUM-CLIENT-MIB", "clientIfLinkDown"),
        ("LUM-CLIENT-MIB", "clientIfConfigurationCommand"),
        ("LUM-CLIENT-MIB", "clientIfGbeUtilization"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSync"),
        ("LUM-CLIENT-MIB", "clientIfConfigureTrxModeCommand"),
        ("LUM-CLIENT-MIB", "clientIfTrxMode"),
        ("LUM-CLIENT-MIB", "clientIfExpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfUnexpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfIllegalFrequency"),
        ("LUM-CLIENT-MIB", "clientIfLaserForcedOn"),
        ("LUM-CLIENT-MIB", "clientIfTrxMedia"),
        ("LUM-CLIENT-MIB", "clientIfTrxMediaMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTruncAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfObjectProperty"),
        ("LUM-CLIENT-MIB", "clientIfTxPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfLaserTempActual"),
        ("LUM-CLIENT-MIB", "clientIfTraceIntrusionMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceTransmitted"),
        ("LUM-CLIENT-MIB", "clientIfTraceReceived"),
        ("LUM-CLIENT-MIB", "clientIfTraceExpected"),
        ("LUM-CLIENT-MIB", "clientIfTraceAlarmMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceMismatch"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfMsAlarmIndicationSignalC2W"),
        ("LUM-CLIENT-MIB", "clientIfMsAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfRemoteDefectIndication"),
        ("LUM-CLIENT-MIB", "clientIfJ1TxTrailTrace"),
        ("LUM-CLIENT-MIB", "clientIfJ1TxTrailTraceInsertionMode"),
        ("LUM-CLIENT-MIB", "clientIfVcGroupFailedW2C"),
        ("LUM-CLIENT-MIB", "clientIfReadJ1"),
        ("LUM-CLIENT-MIB", "clientIfHighSpeed"),
        ("LUM-CLIENT-MIB", "clientIfActualFormat"),
        ("LUM-CLIENT-MIB", "clientIfRdiIntrusionMode"),
        ("LUM-CLIENT-MIB", "clientIfMuxQuadVc4"),
        ("LUM-CLIENT-MIB", "clientIfDemuxQuadVc4"),
        ("LUM-CLIENT-MIB", "clientIfCcConnectionMode"),
        ("LUM-CLIENT-MIB", "clientIfCcConfigurationCommand"),
        ("LUM-CLIENT-MIB", "clientIfIllegalSignalFormat"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtPortId"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtGroupMemberPort"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtGroupStatus"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtActivePort"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtPortStatus"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtToggleActivePort"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopbackTimeout"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopbackEnabled"),
        ("LUM-CLIENT-MIB", "clientIfChangeNearEndLoopbackCommand"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopbackEnabled"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopbackTimeout"),
        ("LUM-CLIENT-MIB", "clientIfChangeFarEndLoopbackCommand"),
        ("LUM-CLIENT-MIB", "clientIfFormatNotSupportedByHw"),
        ("LUM-CLIENT-MIB", "clientIfLaserMode"),
        ("LUM-CLIENT-MIB", "clientIfAlarmIndicationSignalLineC2W"),
        ("LUM-CLIENT-MIB", "clientIfFarEndClientFailure"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparency"),
        ("LUM-CLIENT-MIB", "clientIfConnectedLine"),
        ("LUM-CLIENT-MIB", "clientIfForwardingErrorCorrectionMode"),
        ("LUM-CLIENT-MIB", "clientIfNoFrequencySet"),
        ("LUM-CLIENT-MIB", "clientIfJitterAttenuatorBW"),
        ("LUM-CLIENT-MIB", "clientIfConnectionStatus"),
        ("LUM-CLIENT-MIB", "clientIfLoopFilterUnlocked"),
        ("LUM-CLIENT-MIB", "clientIfCableLength"),
        ("LUM-CLIENT-MIB", "clientIfConnectedForeignIndex"),
        ("LUM-CLIENT-MIB", "clientIfDisconnect"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparencyBitMask"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparencyString"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparencySet"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalC2W"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerC2W"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerW2C"),
        ("LUM-CLIENT-MIB", "clientIfEthStandbyIndicator"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalW2CSonet"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalC2WSonet"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerC2WSonet"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerW2CSonet"),
        ("LUM-CLIENT-MIB", "clientIfTransceiverNoLoopback"),
        ("LUM-CLIENT-MIB", "clientIfFecFailure"),
        ("LUM-CLIENT-MIB", "clientIfLaneAlignmentError"))
)
if mibBuilder.loadTexts:
    clientIfGroupV17.setStatus("deprecated")

clientLanesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 1, 24)
)
clientLanesGroup.setObjects(
      *(("LUM-CLIENT-MIB", "clientLanesIndex"),
        ("LUM-CLIENT-MIB", "clientLanesName"),
        ("LUM-CLIENT-MIB", "clientLanesSubrack"),
        ("LUM-CLIENT-MIB", "clientLanesSlot"),
        ("LUM-CLIENT-MIB", "clientLanesTxPort"),
        ("LUM-CLIENT-MIB", "clientLanesRxPort"),
        ("LUM-CLIENT-MIB", "clientLanesLaneId"),
        ("LUM-CLIENT-MIB", "clientLanesRxPowerLevel"),
        ("LUM-CLIENT-MIB", "clientLanesWaveLength"),
        ("LUM-CLIENT-MIB", "clientLanesBE"),
        ("LUM-CLIENT-MIB", "clientLanesResetBE"),
        ("LUM-CLIENT-MIB", "clientLanesLossOfSignal"),
        ("LUM-CLIENT-MIB", "clientLanesObjectProperty"),
        ("LUM-CLIENT-MIB", "clientLanesLossOfSync"),
        ("LUM-CLIENT-MIB", "clientLanesLocalLinkFault"),
        ("LUM-CLIENT-MIB", "clientLanesRemoteLinkFault"),
        ("LUM-CLIENT-MIB", "clientLanesHighBitErrorRate"))
)
if mibBuilder.loadTexts:
    clientLanesGroup.setStatus("deprecated")

clientIfGroupV18 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 1, 25)
)
clientIfGroupV18.setObjects(
      *(("LUM-CLIENT-MIB", "clientIfIndex"),
        ("LUM-CLIENT-MIB", "clientIfName"),
        ("LUM-CLIENT-MIB", "clientIfSubrack"),
        ("LUM-CLIENT-MIB", "clientIfSlot"),
        ("LUM-CLIENT-MIB", "clientIfTxPort"),
        ("LUM-CLIENT-MIB", "clientIfRxPort"),
        ("LUM-CLIENT-MIB", "clientIfEntityId"),
        ("LUM-CLIENT-MIB", "clientIfAdminStatus"),
        ("LUM-CLIENT-MIB", "clientIfOperStatus"),
        ("LUM-CLIENT-MIB", "clientIfLaserStatus"),
        ("LUM-CLIENT-MIB", "clientIfTxSignalStatus"),
        ("LUM-CLIENT-MIB", "clientIfForwardAls"),
        ("LUM-CLIENT-MIB", "clientIfSuppressRemoteAlarms"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfFormat"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationStatus"),
        ("LUM-CLIENT-MIB", "clientIfDuplexCapability"),
        ("LUM-CLIENT-MIB", "clientIfFlowControlMode"),
        ("LUM-CLIENT-MIB", "clientIfInterPacketGap"),
        ("LUM-CLIENT-MIB", "clientIfFrameSize"),
        ("LUM-CLIENT-MIB", "clientIfGfpMode"),
        ("LUM-CLIENT-MIB", "clientIfBandWidth"),
        ("LUM-CLIENT-MIB", "clientIfRateLimit"),
        ("LUM-CLIENT-MIB", "clientIfTrxClass"),
        ("LUM-CLIENT-MIB", "clientIfLaserBias"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfReceiverSensitivity"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevelLowRelativeThreshold"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSignal"),
        ("LUM-CLIENT-MIB", "clientIfLossOfFrame"),
        ("LUM-CLIENT-MIB", "clientIfBitrateMismatch"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfTransmitterFailed"),
        ("LUM-CLIENT-MIB", "clientIfTrxCodeMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTrxBitrateUnavailable"),
        ("LUM-CLIENT-MIB", "clientIfTrxMissing"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerHigh"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerLow"),
        ("LUM-CLIENT-MIB", "clientIfLinkDown"),
        ("LUM-CLIENT-MIB", "clientIfConfigurationCommand"),
        ("LUM-CLIENT-MIB", "clientIfGbeUtilization"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSync"),
        ("LUM-CLIENT-MIB", "clientIfConfigureTrxModeCommand"),
        ("LUM-CLIENT-MIB", "clientIfTrxMode"),
        ("LUM-CLIENT-MIB", "clientIfExpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfUnexpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfIllegalFrequency"),
        ("LUM-CLIENT-MIB", "clientIfLaserForcedOn"),
        ("LUM-CLIENT-MIB", "clientIfTrxMedia"),
        ("LUM-CLIENT-MIB", "clientIfTrxMediaMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTruncAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfObjectProperty"),
        ("LUM-CLIENT-MIB", "clientIfTxPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfLaserTempActual"),
        ("LUM-CLIENT-MIB", "clientIfTraceIntrusionMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceTransmitted"),
        ("LUM-CLIENT-MIB", "clientIfTraceReceived"),
        ("LUM-CLIENT-MIB", "clientIfTraceExpected"),
        ("LUM-CLIENT-MIB", "clientIfTraceAlarmMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceMismatch"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfMsAlarmIndicationSignalC2W"),
        ("LUM-CLIENT-MIB", "clientIfMsAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfRemoteDefectIndication"),
        ("LUM-CLIENT-MIB", "clientIfJ1TxTrailTrace"),
        ("LUM-CLIENT-MIB", "clientIfJ1TxTrailTraceInsertionMode"),
        ("LUM-CLIENT-MIB", "clientIfVcGroupFailedW2C"),
        ("LUM-CLIENT-MIB", "clientIfReadJ1"),
        ("LUM-CLIENT-MIB", "clientIfHighSpeed"),
        ("LUM-CLIENT-MIB", "clientIfActualFormat"),
        ("LUM-CLIENT-MIB", "clientIfRdiIntrusionMode"),
        ("LUM-CLIENT-MIB", "clientIfMuxQuadVc4"),
        ("LUM-CLIENT-MIB", "clientIfDemuxQuadVc4"),
        ("LUM-CLIENT-MIB", "clientIfCcConnectionMode"),
        ("LUM-CLIENT-MIB", "clientIfCcConfigurationCommand"),
        ("LUM-CLIENT-MIB", "clientIfIllegalSignalFormat"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtPortId"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtGroupMemberPort"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtGroupStatus"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtActivePort"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtPortStatus"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtToggleActivePort"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopbackTimeout"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopbackEnabled"),
        ("LUM-CLIENT-MIB", "clientIfChangeNearEndLoopbackCommand"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopbackEnabled"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopbackTimeout"),
        ("LUM-CLIENT-MIB", "clientIfChangeFarEndLoopbackCommand"),
        ("LUM-CLIENT-MIB", "clientIfFormatNotSupportedByHw"),
        ("LUM-CLIENT-MIB", "clientIfLaserMode"),
        ("LUM-CLIENT-MIB", "clientIfAlarmIndicationSignalLineC2W"),
        ("LUM-CLIENT-MIB", "clientIfFarEndClientFailure"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparency"),
        ("LUM-CLIENT-MIB", "clientIfConnectedLine"),
        ("LUM-CLIENT-MIB", "clientIfForwardingErrorCorrectionMode"),
        ("LUM-CLIENT-MIB", "clientIfNoFrequencySet"),
        ("LUM-CLIENT-MIB", "clientIfJitterAttenuatorBW"),
        ("LUM-CLIENT-MIB", "clientIfConnectionStatus"),
        ("LUM-CLIENT-MIB", "clientIfLoopFilterUnlocked"),
        ("LUM-CLIENT-MIB", "clientIfCableLength"),
        ("LUM-CLIENT-MIB", "clientIfConnectedForeignIndex"),
        ("LUM-CLIENT-MIB", "clientIfDisconnect"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparencyBitMask"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparencyString"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparencySet"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalC2W"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerC2W"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerW2C"),
        ("LUM-CLIENT-MIB", "clientIfEthStandbyIndicator"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalW2CSonet"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalC2WSonet"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerC2WSonet"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerW2CSonet"),
        ("LUM-CLIENT-MIB", "clientIfTransceiverNoLoopback"),
        ("LUM-CLIENT-MIB", "clientIfFecFailure"),
        ("LUM-CLIENT-MIB", "clientIfLaneAlignmentError"),
        ("LUM-CLIENT-MIB", "clientIfFecCorrectedZeros"),
        ("LUM-CLIENT-MIB", "clientIfFecCorrectedOnes"),
        ("LUM-CLIENT-MIB", "clientIfSignalDegraded"))
)
if mibBuilder.loadTexts:
    clientIfGroupV18.setStatus("deprecated")

clientIfGroupV19 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 1, 26)
)
clientIfGroupV19.setObjects(
      *(("LUM-CLIENT-MIB", "clientIfIndex"),
        ("LUM-CLIENT-MIB", "clientIfName"),
        ("LUM-CLIENT-MIB", "clientIfSubrack"),
        ("LUM-CLIENT-MIB", "clientIfSlot"),
        ("LUM-CLIENT-MIB", "clientIfTxPort"),
        ("LUM-CLIENT-MIB", "clientIfRxPort"),
        ("LUM-CLIENT-MIB", "clientIfEntityId"),
        ("LUM-CLIENT-MIB", "clientIfAdminStatus"),
        ("LUM-CLIENT-MIB", "clientIfOperStatus"),
        ("LUM-CLIENT-MIB", "clientIfLaserStatus"),
        ("LUM-CLIENT-MIB", "clientIfTxSignalStatus"),
        ("LUM-CLIENT-MIB", "clientIfForwardAls"),
        ("LUM-CLIENT-MIB", "clientIfSuppressRemoteAlarms"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfFormat"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationStatus"),
        ("LUM-CLIENT-MIB", "clientIfDuplexCapability"),
        ("LUM-CLIENT-MIB", "clientIfFlowControlMode"),
        ("LUM-CLIENT-MIB", "clientIfInterPacketGap"),
        ("LUM-CLIENT-MIB", "clientIfFrameSize"),
        ("LUM-CLIENT-MIB", "clientIfGfpMode"),
        ("LUM-CLIENT-MIB", "clientIfBandWidth"),
        ("LUM-CLIENT-MIB", "clientIfRateLimit"),
        ("LUM-CLIENT-MIB", "clientIfTrxClass"),
        ("LUM-CLIENT-MIB", "clientIfLaserBias"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfReceiverSensitivity"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevelLowRelativeThreshold"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSignal"),
        ("LUM-CLIENT-MIB", "clientIfLossOfFrame"),
        ("LUM-CLIENT-MIB", "clientIfBitrateMismatch"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfTransmitterFailed"),
        ("LUM-CLIENT-MIB", "clientIfTrxCodeMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTrxBitrateUnavailable"),
        ("LUM-CLIENT-MIB", "clientIfTrxMissing"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerHigh"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerLow"),
        ("LUM-CLIENT-MIB", "clientIfLinkDown"),
        ("LUM-CLIENT-MIB", "clientIfConfigurationCommand"),
        ("LUM-CLIENT-MIB", "clientIfGbeUtilization"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSync"),
        ("LUM-CLIENT-MIB", "clientIfConfigureTrxModeCommand"),
        ("LUM-CLIENT-MIB", "clientIfTrxMode"),
        ("LUM-CLIENT-MIB", "clientIfExpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfUnexpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfIllegalFrequency"),
        ("LUM-CLIENT-MIB", "clientIfLaserForcedOn"),
        ("LUM-CLIENT-MIB", "clientIfTrxMedia"),
        ("LUM-CLIENT-MIB", "clientIfTrxMediaMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTruncAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfObjectProperty"),
        ("LUM-CLIENT-MIB", "clientIfTxPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfLaserTempActual"),
        ("LUM-CLIENT-MIB", "clientIfTraceIntrusionMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceTransmitted"),
        ("LUM-CLIENT-MIB", "clientIfTraceReceived"),
        ("LUM-CLIENT-MIB", "clientIfTraceExpected"),
        ("LUM-CLIENT-MIB", "clientIfTraceAlarmMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceMismatch"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfMsAlarmIndicationSignalC2W"),
        ("LUM-CLIENT-MIB", "clientIfMsAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfRemoteDefectIndication"),
        ("LUM-CLIENT-MIB", "clientIfJ1TxTrailTrace"),
        ("LUM-CLIENT-MIB", "clientIfJ1TxTrailTraceInsertionMode"),
        ("LUM-CLIENT-MIB", "clientIfVcGroupFailedW2C"),
        ("LUM-CLIENT-MIB", "clientIfReadJ1"),
        ("LUM-CLIENT-MIB", "clientIfHighSpeed"),
        ("LUM-CLIENT-MIB", "clientIfActualFormat"),
        ("LUM-CLIENT-MIB", "clientIfRdiIntrusionMode"),
        ("LUM-CLIENT-MIB", "clientIfMuxQuadVc4"),
        ("LUM-CLIENT-MIB", "clientIfDemuxQuadVc4"),
        ("LUM-CLIENT-MIB", "clientIfCcConnectionMode"),
        ("LUM-CLIENT-MIB", "clientIfCcConfigurationCommand"),
        ("LUM-CLIENT-MIB", "clientIfIllegalSignalFormat"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtPortId"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtGroupMemberPort"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtGroupStatus"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtActivePort"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtPortStatus"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtToggleActivePort"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopbackTimeout"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopbackEnabled"),
        ("LUM-CLIENT-MIB", "clientIfChangeNearEndLoopbackCommand"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopbackEnabled"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopbackTimeout"),
        ("LUM-CLIENT-MIB", "clientIfChangeFarEndLoopbackCommand"),
        ("LUM-CLIENT-MIB", "clientIfFormatNotSupportedByHw"),
        ("LUM-CLIENT-MIB", "clientIfLaserMode"),
        ("LUM-CLIENT-MIB", "clientIfAlarmIndicationSignalLineC2W"),
        ("LUM-CLIENT-MIB", "clientIfFarEndClientFailure"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparency"),
        ("LUM-CLIENT-MIB", "clientIfConnectedLine"),
        ("LUM-CLIENT-MIB", "clientIfForwardingErrorCorrectionMode"),
        ("LUM-CLIENT-MIB", "clientIfNoFrequencySet"),
        ("LUM-CLIENT-MIB", "clientIfJitterAttenuatorBW"),
        ("LUM-CLIENT-MIB", "clientIfConnectionStatus"),
        ("LUM-CLIENT-MIB", "clientIfLoopFilterUnlocked"),
        ("LUM-CLIENT-MIB", "clientIfCableLength"),
        ("LUM-CLIENT-MIB", "clientIfConnectedForeignIndex"),
        ("LUM-CLIENT-MIB", "clientIfDisconnect"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparencyBitMask"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparencyString"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparencySet"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalC2W"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerC2W"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerW2C"),
        ("LUM-CLIENT-MIB", "clientIfEthStandbyIndicator"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalW2CSonet"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalC2WSonet"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerC2WSonet"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerW2CSonet"),
        ("LUM-CLIENT-MIB", "clientIfTransceiverNoLoopback"),
        ("LUM-CLIENT-MIB", "clientIfFecFailure"),
        ("LUM-CLIENT-MIB", "clientIfLaneAlignmentError"),
        ("LUM-CLIENT-MIB", "clientIfFecCorrectedZeros"),
        ("LUM-CLIENT-MIB", "clientIfFecCorrectedOnes"),
        ("LUM-CLIENT-MIB", "clientIfSignalDegraded"),
        ("LUM-CLIENT-MIB", "clientIfFecType"),
        ("LUM-CLIENT-MIB", "clientIfSignalDegradeThreshold"))
)
if mibBuilder.loadTexts:
    clientIfGroupV19.setStatus("deprecated")

clientIfGroupV20 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 1, 27)
)
clientIfGroupV20.setObjects(
      *(("LUM-CLIENT-MIB", "clientIfIndex"),
        ("LUM-CLIENT-MIB", "clientIfName"),
        ("LUM-CLIENT-MIB", "clientIfSubrack"),
        ("LUM-CLIENT-MIB", "clientIfSlot"),
        ("LUM-CLIENT-MIB", "clientIfTxPort"),
        ("LUM-CLIENT-MIB", "clientIfRxPort"),
        ("LUM-CLIENT-MIB", "clientIfEntityId"),
        ("LUM-CLIENT-MIB", "clientIfAdminStatus"),
        ("LUM-CLIENT-MIB", "clientIfOperStatus"),
        ("LUM-CLIENT-MIB", "clientIfLaserStatus"),
        ("LUM-CLIENT-MIB", "clientIfTxSignalStatus"),
        ("LUM-CLIENT-MIB", "clientIfForwardAls"),
        ("LUM-CLIENT-MIB", "clientIfSuppressRemoteAlarms"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfFormat"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationStatus"),
        ("LUM-CLIENT-MIB", "clientIfDuplexCapability"),
        ("LUM-CLIENT-MIB", "clientIfFlowControlMode"),
        ("LUM-CLIENT-MIB", "clientIfInterPacketGap"),
        ("LUM-CLIENT-MIB", "clientIfFrameSize"),
        ("LUM-CLIENT-MIB", "clientIfGfpMode"),
        ("LUM-CLIENT-MIB", "clientIfBandWidth"),
        ("LUM-CLIENT-MIB", "clientIfRateLimit"),
        ("LUM-CLIENT-MIB", "clientIfTrxClass"),
        ("LUM-CLIENT-MIB", "clientIfLaserBias"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfReceiverSensitivity"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevelLowRelativeThreshold"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSignal"),
        ("LUM-CLIENT-MIB", "clientIfLossOfFrame"),
        ("LUM-CLIENT-MIB", "clientIfBitrateMismatch"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfTransmitterFailed"),
        ("LUM-CLIENT-MIB", "clientIfTrxCodeMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTrxBitrateUnavailable"),
        ("LUM-CLIENT-MIB", "clientIfTrxMissing"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerHigh"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerLow"),
        ("LUM-CLIENT-MIB", "clientIfLinkDown"),
        ("LUM-CLIENT-MIB", "clientIfConfigurationCommand"),
        ("LUM-CLIENT-MIB", "clientIfGbeUtilization"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSync"),
        ("LUM-CLIENT-MIB", "clientIfConfigureTrxModeCommand"),
        ("LUM-CLIENT-MIB", "clientIfTrxMode"),
        ("LUM-CLIENT-MIB", "clientIfExpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfUnexpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfIllegalFrequency"),
        ("LUM-CLIENT-MIB", "clientIfLaserForcedOn"),
        ("LUM-CLIENT-MIB", "clientIfTrxMedia"),
        ("LUM-CLIENT-MIB", "clientIfTrxMediaMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTruncAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfObjectProperty"),
        ("LUM-CLIENT-MIB", "clientIfTxPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfLaserTempActual"),
        ("LUM-CLIENT-MIB", "clientIfTraceIntrusionMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceTransmitted"),
        ("LUM-CLIENT-MIB", "clientIfTraceReceived"),
        ("LUM-CLIENT-MIB", "clientIfTraceExpected"),
        ("LUM-CLIENT-MIB", "clientIfTraceAlarmMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceMismatch"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfMsAlarmIndicationSignalC2W"),
        ("LUM-CLIENT-MIB", "clientIfMsAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfRemoteDefectIndication"),
        ("LUM-CLIENT-MIB", "clientIfJ1TxTrailTrace"),
        ("LUM-CLIENT-MIB", "clientIfJ1TxTrailTraceInsertionMode"),
        ("LUM-CLIENT-MIB", "clientIfVcGroupFailedW2C"),
        ("LUM-CLIENT-MIB", "clientIfReadJ1"),
        ("LUM-CLIENT-MIB", "clientIfHighSpeed"),
        ("LUM-CLIENT-MIB", "clientIfActualFormat"),
        ("LUM-CLIENT-MIB", "clientIfRdiIntrusionMode"),
        ("LUM-CLIENT-MIB", "clientIfMuxQuadVc4"),
        ("LUM-CLIENT-MIB", "clientIfDemuxQuadVc4"),
        ("LUM-CLIENT-MIB", "clientIfCcConnectionMode"),
        ("LUM-CLIENT-MIB", "clientIfCcConfigurationCommand"),
        ("LUM-CLIENT-MIB", "clientIfIllegalSignalFormat"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtPortId"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtGroupMemberPort"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtGroupStatus"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtActivePort"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtPortStatus"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtToggleActivePort"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopbackTimeout"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopbackEnabled"),
        ("LUM-CLIENT-MIB", "clientIfChangeNearEndLoopbackCommand"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopbackEnabled"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopbackTimeout"),
        ("LUM-CLIENT-MIB", "clientIfChangeFarEndLoopbackCommand"),
        ("LUM-CLIENT-MIB", "clientIfFormatNotSupportedByHw"),
        ("LUM-CLIENT-MIB", "clientIfLaserMode"),
        ("LUM-CLIENT-MIB", "clientIfAlarmIndicationSignalLineC2W"),
        ("LUM-CLIENT-MIB", "clientIfFarEndClientFailure"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparency"),
        ("LUM-CLIENT-MIB", "clientIfConnectedLine"),
        ("LUM-CLIENT-MIB", "clientIfForwardingErrorCorrectionMode"),
        ("LUM-CLIENT-MIB", "clientIfNoFrequencySet"),
        ("LUM-CLIENT-MIB", "clientIfJitterAttenuatorBW"),
        ("LUM-CLIENT-MIB", "clientIfConnectionStatus"),
        ("LUM-CLIENT-MIB", "clientIfLoopFilterUnlocked"),
        ("LUM-CLIENT-MIB", "clientIfCableLength"),
        ("LUM-CLIENT-MIB", "clientIfConnectedForeignIndex"),
        ("LUM-CLIENT-MIB", "clientIfDisconnect"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparencyBitMask"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparencyString"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparencySet"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalC2W"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerC2W"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerW2C"),
        ("LUM-CLIENT-MIB", "clientIfEthStandbyIndicator"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalW2CSonet"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalC2WSonet"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerC2WSonet"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerW2CSonet"),
        ("LUM-CLIENT-MIB", "clientIfTransceiverNoLoopback"),
        ("LUM-CLIENT-MIB", "clientIfFecFailure"),
        ("LUM-CLIENT-MIB", "clientIfLaneAlignmentError"),
        ("LUM-CLIENT-MIB", "clientIfFecCorrectedZeros"),
        ("LUM-CLIENT-MIB", "clientIfFecCorrectedOnes"),
        ("LUM-CLIENT-MIB", "clientIfSignalDegraded"),
        ("LUM-CLIENT-MIB", "clientIfFecType"),
        ("LUM-CLIENT-MIB", "clientIfSignalDegradeThreshold"),
        ("LUM-CLIENT-MIB", "clientIfExpectedOpticalLayerMapping"),
        ("LUM-CLIENT-MIB", "clientIfActualOpticalLayerMapping"),
        ("LUM-CLIENT-MIB", "clientIfConfigurationMismatch"))
)
if mibBuilder.loadTexts:
    clientIfGroupV20.setStatus("deprecated")

clientLanesGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 1, 28)
)
clientLanesGroupV2.setObjects(
      *(("LUM-CLIENT-MIB", "clientLanesIndex"),
        ("LUM-CLIENT-MIB", "clientLanesName"),
        ("LUM-CLIENT-MIB", "clientLanesSubrack"),
        ("LUM-CLIENT-MIB", "clientLanesSlot"),
        ("LUM-CLIENT-MIB", "clientLanesTxPort"),
        ("LUM-CLIENT-MIB", "clientLanesRxPort"),
        ("LUM-CLIENT-MIB", "clientLanesLaneId"),
        ("LUM-CLIENT-MIB", "clientLanesRxPowerLevel"),
        ("LUM-CLIENT-MIB", "clientLanesWaveLength"),
        ("LUM-CLIENT-MIB", "clientLanesBE"),
        ("LUM-CLIENT-MIB", "clientLanesResetBE"),
        ("LUM-CLIENT-MIB", "clientLanesLossOfSignal"),
        ("LUM-CLIENT-MIB", "clientLanesObjectProperty"),
        ("LUM-CLIENT-MIB", "clientLanesLossOfSync"),
        ("LUM-CLIENT-MIB", "clientLanesLocalLinkFault"),
        ("LUM-CLIENT-MIB", "clientLanesRemoteLinkFault"),
        ("LUM-CLIENT-MIB", "clientLanesHighBitErrorRate"),
        ("LUM-CLIENT-MIB", "clientLanesReceiverSensitivity"),
        ("LUM-CLIENT-MIB", "clientLanesReceivedPowerLow"))
)
if mibBuilder.loadTexts:
    clientLanesGroupV2.setStatus("deprecated")

clientIfGroupV21 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 1, 29)
)
clientIfGroupV21.setObjects(
      *(("LUM-CLIENT-MIB", "clientIfIndex"),
        ("LUM-CLIENT-MIB", "clientIfName"),
        ("LUM-CLIENT-MIB", "clientIfSubrack"),
        ("LUM-CLIENT-MIB", "clientIfSlot"),
        ("LUM-CLIENT-MIB", "clientIfTxPort"),
        ("LUM-CLIENT-MIB", "clientIfRxPort"),
        ("LUM-CLIENT-MIB", "clientIfEntityId"),
        ("LUM-CLIENT-MIB", "clientIfAdminStatus"),
        ("LUM-CLIENT-MIB", "clientIfOperStatus"),
        ("LUM-CLIENT-MIB", "clientIfLaserStatus"),
        ("LUM-CLIENT-MIB", "clientIfTxSignalStatus"),
        ("LUM-CLIENT-MIB", "clientIfForwardAls"),
        ("LUM-CLIENT-MIB", "clientIfSuppressRemoteAlarms"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfFormat"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationStatus"),
        ("LUM-CLIENT-MIB", "clientIfDuplexCapability"),
        ("LUM-CLIENT-MIB", "clientIfFlowControlMode"),
        ("LUM-CLIENT-MIB", "clientIfInterPacketGap"),
        ("LUM-CLIENT-MIB", "clientIfFrameSize"),
        ("LUM-CLIENT-MIB", "clientIfGfpMode"),
        ("LUM-CLIENT-MIB", "clientIfBandWidth"),
        ("LUM-CLIENT-MIB", "clientIfRateLimit"),
        ("LUM-CLIENT-MIB", "clientIfTrxClass"),
        ("LUM-CLIENT-MIB", "clientIfLaserBias"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfReceiverSensitivity"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevelLowRelativeThreshold"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSignal"),
        ("LUM-CLIENT-MIB", "clientIfLossOfFrame"),
        ("LUM-CLIENT-MIB", "clientIfBitrateMismatch"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfTransmitterFailed"),
        ("LUM-CLIENT-MIB", "clientIfTrxCodeMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTrxBitrateUnavailable"),
        ("LUM-CLIENT-MIB", "clientIfTrxMissing"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerHigh"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerLow"),
        ("LUM-CLIENT-MIB", "clientIfLinkDown"),
        ("LUM-CLIENT-MIB", "clientIfConfigurationCommand"),
        ("LUM-CLIENT-MIB", "clientIfGbeUtilization"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSync"),
        ("LUM-CLIENT-MIB", "clientIfConfigureTrxModeCommand"),
        ("LUM-CLIENT-MIB", "clientIfTrxMode"),
        ("LUM-CLIENT-MIB", "clientIfExpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfUnexpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfIllegalFrequency"),
        ("LUM-CLIENT-MIB", "clientIfLaserForcedOn"),
        ("LUM-CLIENT-MIB", "clientIfTrxMedia"),
        ("LUM-CLIENT-MIB", "clientIfTrxMediaMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTruncAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfObjectProperty"),
        ("LUM-CLIENT-MIB", "clientIfTxPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfLaserTempActual"),
        ("LUM-CLIENT-MIB", "clientIfTraceIntrusionMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceTransmitted"),
        ("LUM-CLIENT-MIB", "clientIfTraceReceived"),
        ("LUM-CLIENT-MIB", "clientIfTraceExpected"),
        ("LUM-CLIENT-MIB", "clientIfTraceAlarmMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceMismatch"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfMsAlarmIndicationSignalC2W"),
        ("LUM-CLIENT-MIB", "clientIfMsAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfRemoteDefectIndication"),
        ("LUM-CLIENT-MIB", "clientIfJ1TxTrailTrace"),
        ("LUM-CLIENT-MIB", "clientIfJ1TxTrailTraceInsertionMode"),
        ("LUM-CLIENT-MIB", "clientIfVcGroupFailedW2C"),
        ("LUM-CLIENT-MIB", "clientIfReadJ1"),
        ("LUM-CLIENT-MIB", "clientIfHighSpeed"),
        ("LUM-CLIENT-MIB", "clientIfActualFormat"),
        ("LUM-CLIENT-MIB", "clientIfRdiIntrusionMode"),
        ("LUM-CLIENT-MIB", "clientIfMuxQuadVc4"),
        ("LUM-CLIENT-MIB", "clientIfDemuxQuadVc4"),
        ("LUM-CLIENT-MIB", "clientIfCcConnectionMode"),
        ("LUM-CLIENT-MIB", "clientIfCcConfigurationCommand"),
        ("LUM-CLIENT-MIB", "clientIfIllegalSignalFormat"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtPortId"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtGroupMemberPort"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtGroupStatus"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtActivePort"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtPortStatus"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtToggleActivePort"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopbackTimeout"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopbackEnabled"),
        ("LUM-CLIENT-MIB", "clientIfChangeNearEndLoopbackCommand"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopbackEnabled"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopbackTimeout"),
        ("LUM-CLIENT-MIB", "clientIfChangeFarEndLoopbackCommand"),
        ("LUM-CLIENT-MIB", "clientIfFormatNotSupportedByHw"),
        ("LUM-CLIENT-MIB", "clientIfLaserMode"),
        ("LUM-CLIENT-MIB", "clientIfAlarmIndicationSignalLineC2W"),
        ("LUM-CLIENT-MIB", "clientIfFarEndClientFailure"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparency"),
        ("LUM-CLIENT-MIB", "clientIfConnectedLine"),
        ("LUM-CLIENT-MIB", "clientIfForwardingErrorCorrectionMode"),
        ("LUM-CLIENT-MIB", "clientIfNoFrequencySet"),
        ("LUM-CLIENT-MIB", "clientIfJitterAttenuatorBW"),
        ("LUM-CLIENT-MIB", "clientIfConnectionStatus"),
        ("LUM-CLIENT-MIB", "clientIfLoopFilterUnlocked"),
        ("LUM-CLIENT-MIB", "clientIfCableLength"),
        ("LUM-CLIENT-MIB", "clientIfConnectedForeignIndex"),
        ("LUM-CLIENT-MIB", "clientIfDisconnect"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparencyBitMask"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparencyString"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparencySet"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalC2W"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerC2W"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerW2C"),
        ("LUM-CLIENT-MIB", "clientIfEthStandbyIndicator"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalW2CSonet"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalC2WSonet"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerC2WSonet"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerW2CSonet"),
        ("LUM-CLIENT-MIB", "clientIfTransceiverNoLoopback"),
        ("LUM-CLIENT-MIB", "clientIfFecFailure"),
        ("LUM-CLIENT-MIB", "clientIfLaneAlignmentError"),
        ("LUM-CLIENT-MIB", "clientIfFecCorrectedZeros"),
        ("LUM-CLIENT-MIB", "clientIfFecCorrectedOnes"),
        ("LUM-CLIENT-MIB", "clientIfSignalDegraded"),
        ("LUM-CLIENT-MIB", "clientIfFecType"),
        ("LUM-CLIENT-MIB", "clientIfSignalDegradeThreshold"),
        ("LUM-CLIENT-MIB", "clientIfExpectedOpticalLayerMapping"),
        ("LUM-CLIENT-MIB", "clientIfActualOpticalLayerMapping"),
        ("LUM-CLIENT-MIB", "clientIfConfigurationMismatch"),
        ("LUM-CLIENT-MIB", "clientIfChromaticDispersion"),
        ("LUM-CLIENT-MIB", "clientIfDifferentialGroupDelay"),
        ("LUM-CLIENT-MIB", "clientIfTxState"),
        ("LUM-CLIENT-MIB", "clientIfRxState"))
)
if mibBuilder.loadTexts:
    clientIfGroupV21.setStatus("deprecated")

clientIfGroupV22 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 1, 30)
)
clientIfGroupV22.setObjects(
      *(("LUM-CLIENT-MIB", "clientIfIndex"),
        ("LUM-CLIENT-MIB", "clientIfName"),
        ("LUM-CLIENT-MIB", "clientIfDescr"),
        ("LUM-CLIENT-MIB", "clientIfSubrack"),
        ("LUM-CLIENT-MIB", "clientIfSlot"),
        ("LUM-CLIENT-MIB", "clientIfTxPort"),
        ("LUM-CLIENT-MIB", "clientIfRxPort"),
        ("LUM-CLIENT-MIB", "clientIfInvPhysIndexOrZero"),
        ("LUM-CLIENT-MIB", "clientIfEntityId"),
        ("LUM-CLIENT-MIB", "clientIfAdminStatus"),
        ("LUM-CLIENT-MIB", "clientIfOperStatus"),
        ("LUM-CLIENT-MIB", "clientIfLaserStatus"),
        ("LUM-CLIENT-MIB", "clientIfTxSignalStatus"),
        ("LUM-CLIENT-MIB", "clientIfForwardAls"),
        ("LUM-CLIENT-MIB", "clientIfSuppressRemoteAlarms"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfFormat"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationStatus"),
        ("LUM-CLIENT-MIB", "clientIfDuplexCapability"),
        ("LUM-CLIENT-MIB", "clientIfFlowControlMode"),
        ("LUM-CLIENT-MIB", "clientIfInterPacketGap"),
        ("LUM-CLIENT-MIB", "clientIfFrameSize"),
        ("LUM-CLIENT-MIB", "clientIfGfpMode"),
        ("LUM-CLIENT-MIB", "clientIfBandWidth"),
        ("LUM-CLIENT-MIB", "clientIfRateLimit"),
        ("LUM-CLIENT-MIB", "clientIfTrxClass"),
        ("LUM-CLIENT-MIB", "clientIfLaserBias"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfReceiverSensitivity"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevelLowRelativeThreshold"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSignal"),
        ("LUM-CLIENT-MIB", "clientIfLossOfFrame"),
        ("LUM-CLIENT-MIB", "clientIfBitrateMismatch"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfTransmitterFailed"),
        ("LUM-CLIENT-MIB", "clientIfTrxCodeMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTrxBitrateUnavailable"),
        ("LUM-CLIENT-MIB", "clientIfTrxMissing"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerHigh"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerLow"),
        ("LUM-CLIENT-MIB", "clientIfLinkDown"),
        ("LUM-CLIENT-MIB", "clientIfConfigurationCommand"),
        ("LUM-CLIENT-MIB", "clientIfGbeUtilization"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSync"),
        ("LUM-CLIENT-MIB", "clientIfRxSignalStatus"),
        ("LUM-CLIENT-MIB", "clientIfTrxFailed"),
        ("LUM-CLIENT-MIB", "clientIfDisabled"),
        ("LUM-CLIENT-MIB", "clientIfLoopback"),
        ("LUM-CLIENT-MIB", "clientIfClientSignalFailed"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointer"),
        ("LUM-CLIENT-MIB", "clientIfGfpLossOfFrame"),
        ("LUM-CLIENT-MIB", "clientIfConfigureTrxModeCommand"),
        ("LUM-CLIENT-MIB", "clientIfTrxMode"),
        ("LUM-CLIENT-MIB", "clientIfExpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfUnexpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfIllegalFrequency"),
        ("LUM-CLIENT-MIB", "clientIfLaserForcedOn"),
        ("LUM-CLIENT-MIB", "clientIfTrxMedia"),
        ("LUM-CLIENT-MIB", "clientIfTrxMediaMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTruncAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfObjectProperty"),
        ("LUM-CLIENT-MIB", "clientIfTxPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfLaserTempActual"),
        ("LUM-CLIENT-MIB", "clientIfTraceIntrusionMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceTransmitted"),
        ("LUM-CLIENT-MIB", "clientIfTraceReceived"),
        ("LUM-CLIENT-MIB", "clientIfTraceExpected"),
        ("LUM-CLIENT-MIB", "clientIfTraceAlarmMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceMismatch"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfMsAlarmIndicationSignalC2W"),
        ("LUM-CLIENT-MIB", "clientIfMsAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfRemoteDefectIndication"),
        ("LUM-CLIENT-MIB", "clientIfJ1TxTrailTrace"),
        ("LUM-CLIENT-MIB", "clientIfJ1TxTrailTraceInsertionMode"),
        ("LUM-CLIENT-MIB", "clientIfVcGroupFailedW2C"),
        ("LUM-CLIENT-MIB", "clientIfReadJ1"),
        ("LUM-CLIENT-MIB", "clientIfHighSpeed"),
        ("LUM-CLIENT-MIB", "clientIfActualFormat"),
        ("LUM-CLIENT-MIB", "clientIfRdiIntrusionMode"),
        ("LUM-CLIENT-MIB", "clientIfMuxQuadVc4"),
        ("LUM-CLIENT-MIB", "clientIfDemuxQuadVc4"),
        ("LUM-CLIENT-MIB", "clientIfCcConnectionMode"),
        ("LUM-CLIENT-MIB", "clientIfCcConfigurationCommand"),
        ("LUM-CLIENT-MIB", "clientIfIllegalSignalFormat"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtPortId"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtGroupMemberPort"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtGroupStatus"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtActivePort"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtPortStatus"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtToggleActivePort"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopbackTimeout"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopbackEnabled"),
        ("LUM-CLIENT-MIB", "clientIfChangeNearEndLoopbackCommand"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopbackEnabled"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopbackTimeout"),
        ("LUM-CLIENT-MIB", "clientIfChangeFarEndLoopbackCommand"),
        ("LUM-CLIENT-MIB", "clientIfFormatNotSupportedByHw"),
        ("LUM-CLIENT-MIB", "clientIfLaserMode"),
        ("LUM-CLIENT-MIB", "clientIfAlarmIndicationSignalLineC2W"),
        ("LUM-CLIENT-MIB", "clientIfFarEndClientFailure"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparency"),
        ("LUM-CLIENT-MIB", "clientIfConnectedLine"),
        ("LUM-CLIENT-MIB", "clientIfForwardingErrorCorrectionMode"),
        ("LUM-CLIENT-MIB", "clientIfNoFrequencySet"),
        ("LUM-CLIENT-MIB", "clientIfJitterAttenuatorBW"),
        ("LUM-CLIENT-MIB", "clientIfConnectionStatus"),
        ("LUM-CLIENT-MIB", "clientIfLoopFilterUnlocked"),
        ("LUM-CLIENT-MIB", "clientIfCableLength"),
        ("LUM-CLIENT-MIB", "clientIfConnectedForeignIndex"),
        ("LUM-CLIENT-MIB", "clientIfDisconnect"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparencyBitMask"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparencyString"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparencySet"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalC2W"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerC2W"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerW2C"),
        ("LUM-CLIENT-MIB", "clientIfEthStandbyIndicator"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalW2CSonet"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalC2WSonet"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerC2WSonet"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerW2CSonet"),
        ("LUM-CLIENT-MIB", "clientIfTransceiverNoLoopback"),
        ("LUM-CLIENT-MIB", "clientIfFecFailure"),
        ("LUM-CLIENT-MIB", "clientIfLaneAlignmentError"),
        ("LUM-CLIENT-MIB", "clientIfFecCorrectedZeros"),
        ("LUM-CLIENT-MIB", "clientIfFecCorrectedOnes"),
        ("LUM-CLIENT-MIB", "clientIfSignalDegraded"),
        ("LUM-CLIENT-MIB", "clientIfFecType"),
        ("LUM-CLIENT-MIB", "clientIfSignalDegradeThreshold"),
        ("LUM-CLIENT-MIB", "clientIfExpectedOpticalLayerMapping"),
        ("LUM-CLIENT-MIB", "clientIfActualOpticalLayerMapping"),
        ("LUM-CLIENT-MIB", "clientIfConfigurationMismatch"),
        ("LUM-CLIENT-MIB", "clientIfChromaticDispersion"),
        ("LUM-CLIENT-MIB", "clientIfDifferentialGroupDelay"),
        ("LUM-CLIENT-MIB", "clientIfTxState"),
        ("LUM-CLIENT-MIB", "clientIfRxState"),
        ("LUM-CLIENT-MIB", "clientIfIdx"),
        ("LUM-CLIENT-MIB", "clientIfIfNo"),
        ("LUM-CLIENT-MIB", "clientIfIdxIf"),
        ("LUM-CLIENT-MIB", "clientIfUpPortId"),
        ("LUM-CLIENT-MIB", "clientIfNoOfLanes"),
        ("LUM-CLIENT-MIB", "clientIfFecCorrectedBits"),
        ("LUM-CLIENT-MIB", "clientIfOSNRMargin"),
        ("LUM-CLIENT-MIB", "clientIfExpectedPhysicalLayerMapping"),
        ("LUM-CLIENT-MIB", "clientIfSignalDirection"))
)
if mibBuilder.loadTexts:
    clientIfGroupV22.setStatus("deprecated")

clientLanesGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 1, 31)
)
clientLanesGroupV3.setObjects(
      *(("LUM-CLIENT-MIB", "clientLanesIndex"),
        ("LUM-CLIENT-MIB", "clientLanesName"),
        ("LUM-CLIENT-MIB", "clientLanesSubrack"),
        ("LUM-CLIENT-MIB", "clientLanesSlot"),
        ("LUM-CLIENT-MIB", "clientLanesTxPort"),
        ("LUM-CLIENT-MIB", "clientLanesRxPort"),
        ("LUM-CLIENT-MIB", "clientLanesLaneId"),
        ("LUM-CLIENT-MIB", "clientLanesRxPowerLevel"),
        ("LUM-CLIENT-MIB", "clientLanesWaveLength"),
        ("LUM-CLIENT-MIB", "clientLanesBE"),
        ("LUM-CLIENT-MIB", "clientLanesResetBE"),
        ("LUM-CLIENT-MIB", "clientLanesLossOfSignal"),
        ("LUM-CLIENT-MIB", "clientLanesObjectProperty"),
        ("LUM-CLIENT-MIB", "clientLanesLossOfSync"),
        ("LUM-CLIENT-MIB", "clientLanesLocalLinkFault"),
        ("LUM-CLIENT-MIB", "clientLanesRemoteLinkFault"),
        ("LUM-CLIENT-MIB", "clientLanesHighBitErrorRate"),
        ("LUM-CLIENT-MIB", "clientLanesReceiverSensitivity"),
        ("LUM-CLIENT-MIB", "clientLanesReceivedPowerLow"),
        ("LUM-CLIENT-MIB", "clientLanesIfNo"),
        ("LUM-CLIENT-MIB", "clientLanesIdx"),
        ("LUM-CLIENT-MIB", "clientLanesClientIfIdx"))
)
if mibBuilder.loadTexts:
    clientLanesGroupV3.setStatus("deprecated")

clientLanesGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 1, 32)
)
clientLanesGroupV4.setObjects(
      *(("LUM-CLIENT-MIB", "clientLanesIndex"),
        ("LUM-CLIENT-MIB", "clientLanesName"),
        ("LUM-CLIENT-MIB", "clientLanesSubrack"),
        ("LUM-CLIENT-MIB", "clientLanesSlot"),
        ("LUM-CLIENT-MIB", "clientLanesTxPort"),
        ("LUM-CLIENT-MIB", "clientLanesRxPort"),
        ("LUM-CLIENT-MIB", "clientLanesLaneId"),
        ("LUM-CLIENT-MIB", "clientLanesRxPowerLevel"),
        ("LUM-CLIENT-MIB", "clientLanesWaveLength"),
        ("LUM-CLIENT-MIB", "clientLanesBE"),
        ("LUM-CLIENT-MIB", "clientLanesResetBE"),
        ("LUM-CLIENT-MIB", "clientLanesLossOfSignal"),
        ("LUM-CLIENT-MIB", "clientLanesObjectProperty"),
        ("LUM-CLIENT-MIB", "clientLanesLossOfSync"),
        ("LUM-CLIENT-MIB", "clientLanesLocalLinkFault"),
        ("LUM-CLIENT-MIB", "clientLanesRemoteLinkFault"),
        ("LUM-CLIENT-MIB", "clientLanesHighBitErrorRate"),
        ("LUM-CLIENT-MIB", "clientLanesReceiverSensitivity"),
        ("LUM-CLIENT-MIB", "clientLanesReceivedPowerLow"),
        ("LUM-CLIENT-MIB", "clientLanesIfNo"),
        ("LUM-CLIENT-MIB", "clientLanesIdx"),
        ("LUM-CLIENT-MIB", "clientLanesClientIfIdx"),
        ("LUM-CLIENT-MIB", "clientLanesAdminStatus"),
        ("LUM-CLIENT-MIB", "clientLanesOperStatus"))
)
if mibBuilder.loadTexts:
    clientLanesGroupV4.setStatus("deprecated")

clientMpoLanesGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 1, 33)
)
clientMpoLanesGroupV1.setObjects(
      *(("LUM-CLIENT-MIB", "clientMpoLanesIndex"),
        ("LUM-CLIENT-MIB", "clientMpoLanesName"),
        ("LUM-CLIENT-MIB", "clientMpoLanesSubrack"),
        ("LUM-CLIENT-MIB", "clientMpoLanesSlot"),
        ("LUM-CLIENT-MIB", "clientMpoLanesLaneId"),
        ("LUM-CLIENT-MIB", "clientMpoLanesRxPowerLevel"),
        ("LUM-CLIENT-MIB", "clientMpoLanesRxSensitivity"),
        ("LUM-CLIENT-MIB", "clientMpoLanesWaveLength"),
        ("LUM-CLIENT-MIB", "clientMpoLanesLossOfSignal"),
        ("LUM-CLIENT-MIB", "clientMpoLanesObjectProperty"),
        ("LUM-CLIENT-MIB", "clientMpoLanesRxPowerLow"),
        ("LUM-CLIENT-MIB", "clientMpoLanesIfNo"),
        ("LUM-CLIENT-MIB", "clientMpoLanesAdminStatus"),
        ("LUM-CLIENT-MIB", "clientMpoLanesOperStatus"),
        ("LUM-CLIENT-MIB", "clientMpoLanesForwardAls"),
        ("LUM-CLIENT-MIB", "clientMpoLanesPowerLevelLowRelativeThreshold"),
        ("LUM-CLIENT-MIB", "clientMpoLanesLaserStatus"))
)
if mibBuilder.loadTexts:
    clientMpoLanesGroupV1.setStatus("current")

clientLanesGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 1, 34)
)
clientLanesGroupV5.setObjects(
      *(("LUM-CLIENT-MIB", "clientLanesIndex"),
        ("LUM-CLIENT-MIB", "clientLanesName"),
        ("LUM-CLIENT-MIB", "clientLanesSubrack"),
        ("LUM-CLIENT-MIB", "clientLanesSlot"),
        ("LUM-CLIENT-MIB", "clientLanesTxPort"),
        ("LUM-CLIENT-MIB", "clientLanesRxPort"),
        ("LUM-CLIENT-MIB", "clientLanesLaneId"),
        ("LUM-CLIENT-MIB", "clientLanesRxPowerLevel"),
        ("LUM-CLIENT-MIB", "clientLanesWaveLength"),
        ("LUM-CLIENT-MIB", "clientLanesBE"),
        ("LUM-CLIENT-MIB", "clientLanesResetBE"),
        ("LUM-CLIENT-MIB", "clientLanesLossOfSignal"),
        ("LUM-CLIENT-MIB", "clientLanesObjectProperty"),
        ("LUM-CLIENT-MIB", "clientLanesLossOfSync"),
        ("LUM-CLIENT-MIB", "clientLanesLocalLinkFault"),
        ("LUM-CLIENT-MIB", "clientLanesRemoteLinkFault"),
        ("LUM-CLIENT-MIB", "clientLanesHighBitErrorRate"),
        ("LUM-CLIENT-MIB", "clientLanesReceiverSensitivity"),
        ("LUM-CLIENT-MIB", "clientLanesReceivedPowerLow"),
        ("LUM-CLIENT-MIB", "clientLanesIfNo"),
        ("LUM-CLIENT-MIB", "clientLanesIdx"),
        ("LUM-CLIENT-MIB", "clientLanesClientIfIdx"),
        ("LUM-CLIENT-MIB", "clientLanesAdminStatus"),
        ("LUM-CLIENT-MIB", "clientLanesOperStatus"),
        ("LUM-CLIENT-MIB", "clientLanesUpPortId"))
)
if mibBuilder.loadTexts:
    clientLanesGroupV5.setStatus("current")

clientIfGroupV23 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 1, 35)
)
clientIfGroupV23.setObjects(
      *(("LUM-CLIENT-MIB", "clientIfIndex"),
        ("LUM-CLIENT-MIB", "clientIfName"),
        ("LUM-CLIENT-MIB", "clientIfDescr"),
        ("LUM-CLIENT-MIB", "clientIfSubrack"),
        ("LUM-CLIENT-MIB", "clientIfSlot"),
        ("LUM-CLIENT-MIB", "clientIfTxPort"),
        ("LUM-CLIENT-MIB", "clientIfRxPort"),
        ("LUM-CLIENT-MIB", "clientIfInvPhysIndexOrZero"),
        ("LUM-CLIENT-MIB", "clientIfEntityId"),
        ("LUM-CLIENT-MIB", "clientIfAdminStatus"),
        ("LUM-CLIENT-MIB", "clientIfOperStatus"),
        ("LUM-CLIENT-MIB", "clientIfLaserStatus"),
        ("LUM-CLIENT-MIB", "clientIfTxSignalStatus"),
        ("LUM-CLIENT-MIB", "clientIfForwardAls"),
        ("LUM-CLIENT-MIB", "clientIfSuppressRemoteAlarms"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfFormat"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationStatus"),
        ("LUM-CLIENT-MIB", "clientIfDuplexCapability"),
        ("LUM-CLIENT-MIB", "clientIfFlowControlMode"),
        ("LUM-CLIENT-MIB", "clientIfInterPacketGap"),
        ("LUM-CLIENT-MIB", "clientIfFrameSize"),
        ("LUM-CLIENT-MIB", "clientIfGfpMode"),
        ("LUM-CLIENT-MIB", "clientIfBandWidth"),
        ("LUM-CLIENT-MIB", "clientIfRateLimit"),
        ("LUM-CLIENT-MIB", "clientIfTrxClass"),
        ("LUM-CLIENT-MIB", "clientIfLaserBias"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfReceiverSensitivity"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevelLowRelativeThreshold"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSignal"),
        ("LUM-CLIENT-MIB", "clientIfLossOfFrame"),
        ("LUM-CLIENT-MIB", "clientIfBitrateMismatch"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfTransmitterFailed"),
        ("LUM-CLIENT-MIB", "clientIfTrxCodeMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTrxBitrateUnavailable"),
        ("LUM-CLIENT-MIB", "clientIfTrxMissing"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerHigh"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerLow"),
        ("LUM-CLIENT-MIB", "clientIfLinkDown"),
        ("LUM-CLIENT-MIB", "clientIfConfigurationCommand"),
        ("LUM-CLIENT-MIB", "clientIfGbeUtilization"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSync"),
        ("LUM-CLIENT-MIB", "clientIfRxSignalStatus"),
        ("LUM-CLIENT-MIB", "clientIfTrxFailed"),
        ("LUM-CLIENT-MIB", "clientIfDisabled"),
        ("LUM-CLIENT-MIB", "clientIfLoopback"),
        ("LUM-CLIENT-MIB", "clientIfClientSignalFailed"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointer"),
        ("LUM-CLIENT-MIB", "clientIfGfpLossOfFrame"),
        ("LUM-CLIENT-MIB", "clientIfConfigureTrxModeCommand"),
        ("LUM-CLIENT-MIB", "clientIfTrxMode"),
        ("LUM-CLIENT-MIB", "clientIfExpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfUnexpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfIllegalFrequency"),
        ("LUM-CLIENT-MIB", "clientIfLaserForcedOn"),
        ("LUM-CLIENT-MIB", "clientIfTrxMedia"),
        ("LUM-CLIENT-MIB", "clientIfTrxMediaMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTruncAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfObjectProperty"),
        ("LUM-CLIENT-MIB", "clientIfTxPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfLaserTempActual"),
        ("LUM-CLIENT-MIB", "clientIfTraceIntrusionMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceTransmitted"),
        ("LUM-CLIENT-MIB", "clientIfTraceReceived"),
        ("LUM-CLIENT-MIB", "clientIfTraceExpected"),
        ("LUM-CLIENT-MIB", "clientIfTraceAlarmMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceMismatch"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfMsAlarmIndicationSignalC2W"),
        ("LUM-CLIENT-MIB", "clientIfMsAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfRemoteDefectIndication"),
        ("LUM-CLIENT-MIB", "clientIfJ1TxTrailTrace"),
        ("LUM-CLIENT-MIB", "clientIfJ1TxTrailTraceInsertionMode"),
        ("LUM-CLIENT-MIB", "clientIfVcGroupFailedW2C"),
        ("LUM-CLIENT-MIB", "clientIfReadJ1"),
        ("LUM-CLIENT-MIB", "clientIfHighSpeed"),
        ("LUM-CLIENT-MIB", "clientIfActualFormat"),
        ("LUM-CLIENT-MIB", "clientIfRdiIntrusionMode"),
        ("LUM-CLIENT-MIB", "clientIfMuxQuadVc4"),
        ("LUM-CLIENT-MIB", "clientIfDemuxQuadVc4"),
        ("LUM-CLIENT-MIB", "clientIfCcConnectionMode"),
        ("LUM-CLIENT-MIB", "clientIfCcConfigurationCommand"),
        ("LUM-CLIENT-MIB", "clientIfIllegalSignalFormat"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtPortId"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtGroupMemberPort"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtGroupStatus"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtActivePort"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtPortStatus"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtToggleActivePort"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopbackTimeout"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopbackEnabled"),
        ("LUM-CLIENT-MIB", "clientIfChangeNearEndLoopbackCommand"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopbackEnabled"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopbackTimeout"),
        ("LUM-CLIENT-MIB", "clientIfChangeFarEndLoopbackCommand"),
        ("LUM-CLIENT-MIB", "clientIfFormatNotSupportedByHw"),
        ("LUM-CLIENT-MIB", "clientIfLaserMode"),
        ("LUM-CLIENT-MIB", "clientIfAlarmIndicationSignalLineC2W"),
        ("LUM-CLIENT-MIB", "clientIfFarEndClientFailure"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparency"),
        ("LUM-CLIENT-MIB", "clientIfConnectedLine"),
        ("LUM-CLIENT-MIB", "clientIfForwardingErrorCorrectionMode"),
        ("LUM-CLIENT-MIB", "clientIfNoFrequencySet"),
        ("LUM-CLIENT-MIB", "clientIfJitterAttenuatorBW"),
        ("LUM-CLIENT-MIB", "clientIfConnectionStatus"),
        ("LUM-CLIENT-MIB", "clientIfLoopFilterUnlocked"),
        ("LUM-CLIENT-MIB", "clientIfCableLength"),
        ("LUM-CLIENT-MIB", "clientIfConnectedForeignIndex"),
        ("LUM-CLIENT-MIB", "clientIfDisconnect"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparencyBitMask"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparencyString"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparencySet"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalC2W"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerC2W"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerW2C"),
        ("LUM-CLIENT-MIB", "clientIfEthStandbyIndicator"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalW2CSonet"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalC2WSonet"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerC2WSonet"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerW2CSonet"),
        ("LUM-CLIENT-MIB", "clientIfTransceiverNoLoopback"),
        ("LUM-CLIENT-MIB", "clientIfFecFailure"),
        ("LUM-CLIENT-MIB", "clientIfLaneAlignmentError"),
        ("LUM-CLIENT-MIB", "clientIfFecCorrectedZeros"),
        ("LUM-CLIENT-MIB", "clientIfFecCorrectedOnes"),
        ("LUM-CLIENT-MIB", "clientIfSignalDegraded"),
        ("LUM-CLIENT-MIB", "clientIfFecType"),
        ("LUM-CLIENT-MIB", "clientIfSignalDegradeThreshold"),
        ("LUM-CLIENT-MIB", "clientIfExpectedOpticalLayerMapping"),
        ("LUM-CLIENT-MIB", "clientIfActualOpticalLayerMapping"),
        ("LUM-CLIENT-MIB", "clientIfConfigurationMismatch"),
        ("LUM-CLIENT-MIB", "clientIfChromaticDispersion"),
        ("LUM-CLIENT-MIB", "clientIfDifferentialGroupDelay"),
        ("LUM-CLIENT-MIB", "clientIfTxState"),
        ("LUM-CLIENT-MIB", "clientIfRxState"),
        ("LUM-CLIENT-MIB", "clientIfIdx"),
        ("LUM-CLIENT-MIB", "clientIfIfNo"),
        ("LUM-CLIENT-MIB", "clientIfIdxIf"),
        ("LUM-CLIENT-MIB", "clientIfUpPortId"),
        ("LUM-CLIENT-MIB", "clientIfNoOfLanes"),
        ("LUM-CLIENT-MIB", "clientIfFecCorrectedBits"),
        ("LUM-CLIENT-MIB", "clientIfOSNRMargin"),
        ("LUM-CLIENT-MIB", "clientIfExpectedPhysicalLayerMapping"),
        ("LUM-CLIENT-MIB", "clientIfSignalDirection"),
        ("LUM-CLIENT-MIB", "clientIfAid"),
        ("LUM-CLIENT-MIB", "clientIfPhysicalLocation"))
)
if mibBuilder.loadTexts:
    clientIfGroupV23.setStatus("deprecated")

clientIfGroupV24 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 1, 36)
)
clientIfGroupV24.setObjects(
      *(("LUM-CLIENT-MIB", "clientIfIndex"),
        ("LUM-CLIENT-MIB", "clientIfName"),
        ("LUM-CLIENT-MIB", "clientIfDescr"),
        ("LUM-CLIENT-MIB", "clientIfSubrack"),
        ("LUM-CLIENT-MIB", "clientIfSlot"),
        ("LUM-CLIENT-MIB", "clientIfTxPort"),
        ("LUM-CLIENT-MIB", "clientIfRxPort"),
        ("LUM-CLIENT-MIB", "clientIfInvPhysIndexOrZero"),
        ("LUM-CLIENT-MIB", "clientIfEntityId"),
        ("LUM-CLIENT-MIB", "clientIfAdminStatus"),
        ("LUM-CLIENT-MIB", "clientIfOperStatus"),
        ("LUM-CLIENT-MIB", "clientIfLaserStatus"),
        ("LUM-CLIENT-MIB", "clientIfTxSignalStatus"),
        ("LUM-CLIENT-MIB", "clientIfForwardAls"),
        ("LUM-CLIENT-MIB", "clientIfSuppressRemoteAlarms"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfFormat"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationStatus"),
        ("LUM-CLIENT-MIB", "clientIfDuplexCapability"),
        ("LUM-CLIENT-MIB", "clientIfFlowControlMode"),
        ("LUM-CLIENT-MIB", "clientIfInterPacketGap"),
        ("LUM-CLIENT-MIB", "clientIfFrameSize"),
        ("LUM-CLIENT-MIB", "clientIfGfpMode"),
        ("LUM-CLIENT-MIB", "clientIfBandWidth"),
        ("LUM-CLIENT-MIB", "clientIfRateLimit"),
        ("LUM-CLIENT-MIB", "clientIfTrxClass"),
        ("LUM-CLIENT-MIB", "clientIfLaserBias"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfReceiverSensitivity"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevelLowRelativeThreshold"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSignal"),
        ("LUM-CLIENT-MIB", "clientIfLossOfFrame"),
        ("LUM-CLIENT-MIB", "clientIfBitrateMismatch"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfTransmitterFailed"),
        ("LUM-CLIENT-MIB", "clientIfTrxCodeMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTrxBitrateUnavailable"),
        ("LUM-CLIENT-MIB", "clientIfTrxMissing"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerHigh"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerLow"),
        ("LUM-CLIENT-MIB", "clientIfLinkDown"),
        ("LUM-CLIENT-MIB", "clientIfConfigurationCommand"),
        ("LUM-CLIENT-MIB", "clientIfGbeUtilization"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSync"),
        ("LUM-CLIENT-MIB", "clientIfRxSignalStatus"),
        ("LUM-CLIENT-MIB", "clientIfTrxFailed"),
        ("LUM-CLIENT-MIB", "clientIfDisabled"),
        ("LUM-CLIENT-MIB", "clientIfLoopback"),
        ("LUM-CLIENT-MIB", "clientIfClientSignalFailed"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointer"),
        ("LUM-CLIENT-MIB", "clientIfGfpLossOfFrame"),
        ("LUM-CLIENT-MIB", "clientIfConfigureTrxModeCommand"),
        ("LUM-CLIENT-MIB", "clientIfTrxMode"),
        ("LUM-CLIENT-MIB", "clientIfExpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfUnexpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfIllegalFrequency"),
        ("LUM-CLIENT-MIB", "clientIfLaserForcedOn"),
        ("LUM-CLIENT-MIB", "clientIfTrxMedia"),
        ("LUM-CLIENT-MIB", "clientIfTrxMediaMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTruncAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfObjectProperty"),
        ("LUM-CLIENT-MIB", "clientIfTxPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfLaserTempActual"),
        ("LUM-CLIENT-MIB", "clientIfTraceIntrusionMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceTransmitted"),
        ("LUM-CLIENT-MIB", "clientIfTraceReceived"),
        ("LUM-CLIENT-MIB", "clientIfTraceExpected"),
        ("LUM-CLIENT-MIB", "clientIfTraceAlarmMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceMismatch"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfMsAlarmIndicationSignalC2W"),
        ("LUM-CLIENT-MIB", "clientIfMsAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfRemoteDefectIndication"),
        ("LUM-CLIENT-MIB", "clientIfJ1TxTrailTrace"),
        ("LUM-CLIENT-MIB", "clientIfJ1TxTrailTraceInsertionMode"),
        ("LUM-CLIENT-MIB", "clientIfVcGroupFailedW2C"),
        ("LUM-CLIENT-MIB", "clientIfReadJ1"),
        ("LUM-CLIENT-MIB", "clientIfHighSpeed"),
        ("LUM-CLIENT-MIB", "clientIfActualFormat"),
        ("LUM-CLIENT-MIB", "clientIfRdiIntrusionMode"),
        ("LUM-CLIENT-MIB", "clientIfMuxQuadVc4"),
        ("LUM-CLIENT-MIB", "clientIfDemuxQuadVc4"),
        ("LUM-CLIENT-MIB", "clientIfCcConnectionMode"),
        ("LUM-CLIENT-MIB", "clientIfCcConfigurationCommand"),
        ("LUM-CLIENT-MIB", "clientIfIllegalSignalFormat"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtPortId"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtGroupMemberPort"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtGroupStatus"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtActivePort"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtPortStatus"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtToggleActivePort"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopbackTimeout"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopbackEnabled"),
        ("LUM-CLIENT-MIB", "clientIfChangeNearEndLoopbackCommand"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopbackEnabled"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopbackTimeout"),
        ("LUM-CLIENT-MIB", "clientIfChangeFarEndLoopbackCommand"),
        ("LUM-CLIENT-MIB", "clientIfFormatNotSupportedByHw"),
        ("LUM-CLIENT-MIB", "clientIfLaserMode"),
        ("LUM-CLIENT-MIB", "clientIfAlarmIndicationSignalLineC2W"),
        ("LUM-CLIENT-MIB", "clientIfFarEndClientFailure"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparency"),
        ("LUM-CLIENT-MIB", "clientIfConnectedLine"),
        ("LUM-CLIENT-MIB", "clientIfForwardingErrorCorrectionMode"),
        ("LUM-CLIENT-MIB", "clientIfNoFrequencySet"),
        ("LUM-CLIENT-MIB", "clientIfJitterAttenuatorBW"),
        ("LUM-CLIENT-MIB", "clientIfConnectionStatus"),
        ("LUM-CLIENT-MIB", "clientIfLoopFilterUnlocked"),
        ("LUM-CLIENT-MIB", "clientIfCableLength"),
        ("LUM-CLIENT-MIB", "clientIfConnectedForeignIndex"),
        ("LUM-CLIENT-MIB", "clientIfDisconnect"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparencyBitMask"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparencyString"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparencySet"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalC2W"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerC2W"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerW2C"),
        ("LUM-CLIENT-MIB", "clientIfEthStandbyIndicator"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalW2CSonet"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalC2WSonet"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerC2WSonet"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerW2CSonet"),
        ("LUM-CLIENT-MIB", "clientIfTransceiverNoLoopback"),
        ("LUM-CLIENT-MIB", "clientIfFecFailure"),
        ("LUM-CLIENT-MIB", "clientIfLaneAlignmentError"),
        ("LUM-CLIENT-MIB", "clientIfFecCorrectedZeros"),
        ("LUM-CLIENT-MIB", "clientIfFecCorrectedOnes"),
        ("LUM-CLIENT-MIB", "clientIfSignalDegraded"),
        ("LUM-CLIENT-MIB", "clientIfFecType"),
        ("LUM-CLIENT-MIB", "clientIfSignalDegradeThreshold"),
        ("LUM-CLIENT-MIB", "clientIfExpectedOpticalLayerMapping"),
        ("LUM-CLIENT-MIB", "clientIfActualOpticalLayerMapping"),
        ("LUM-CLIENT-MIB", "clientIfConfigurationMismatch"),
        ("LUM-CLIENT-MIB", "clientIfChromaticDispersion"),
        ("LUM-CLIENT-MIB", "clientIfDifferentialGroupDelay"),
        ("LUM-CLIENT-MIB", "clientIfTxState"),
        ("LUM-CLIENT-MIB", "clientIfRxState"),
        ("LUM-CLIENT-MIB", "clientIfIdx"),
        ("LUM-CLIENT-MIB", "clientIfIfNo"),
        ("LUM-CLIENT-MIB", "clientIfIdxIf"),
        ("LUM-CLIENT-MIB", "clientIfUpPortId"),
        ("LUM-CLIENT-MIB", "clientIfNoOfLanes"),
        ("LUM-CLIENT-MIB", "clientIfFecCorrectedBits"),
        ("LUM-CLIENT-MIB", "clientIfOSNRMargin"),
        ("LUM-CLIENT-MIB", "clientIfExpectedPhysicalLayerMapping"),
        ("LUM-CLIENT-MIB", "clientIfSignalDirection"),
        ("LUM-CLIENT-MIB", "clientIfAid"),
        ("LUM-CLIENT-MIB", "clientIfPhysicalLocation"),
        ("LUM-CLIENT-MIB", "clientIfTrxCommunicationFailure"))
)
if mibBuilder.loadTexts:
    clientIfGroupV24.setStatus("deprecated")

clientIfGroupV25 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 1, 37)
)
clientIfGroupV25.setObjects(
      *(("LUM-CLIENT-MIB", "clientIfIndex"),
        ("LUM-CLIENT-MIB", "clientIfName"),
        ("LUM-CLIENT-MIB", "clientIfDescr"),
        ("LUM-CLIENT-MIB", "clientIfSubrack"),
        ("LUM-CLIENT-MIB", "clientIfSlot"),
        ("LUM-CLIENT-MIB", "clientIfTxPort"),
        ("LUM-CLIENT-MIB", "clientIfRxPort"),
        ("LUM-CLIENT-MIB", "clientIfInvPhysIndexOrZero"),
        ("LUM-CLIENT-MIB", "clientIfEntityId"),
        ("LUM-CLIENT-MIB", "clientIfAdminStatus"),
        ("LUM-CLIENT-MIB", "clientIfOperStatus"),
        ("LUM-CLIENT-MIB", "clientIfLaserStatus"),
        ("LUM-CLIENT-MIB", "clientIfTxSignalStatus"),
        ("LUM-CLIENT-MIB", "clientIfForwardAls"),
        ("LUM-CLIENT-MIB", "clientIfSuppressRemoteAlarms"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfFormat"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationStatus"),
        ("LUM-CLIENT-MIB", "clientIfDuplexCapability"),
        ("LUM-CLIENT-MIB", "clientIfFlowControlMode"),
        ("LUM-CLIENT-MIB", "clientIfInterPacketGap"),
        ("LUM-CLIENT-MIB", "clientIfFrameSize"),
        ("LUM-CLIENT-MIB", "clientIfGfpMode"),
        ("LUM-CLIENT-MIB", "clientIfBandWidth"),
        ("LUM-CLIENT-MIB", "clientIfRateLimit"),
        ("LUM-CLIENT-MIB", "clientIfTrxClass"),
        ("LUM-CLIENT-MIB", "clientIfLaserBias"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfReceiverSensitivity"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevelLowRelativeThreshold"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSignal"),
        ("LUM-CLIENT-MIB", "clientIfLossOfFrame"),
        ("LUM-CLIENT-MIB", "clientIfBitrateMismatch"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfTransmitterFailed"),
        ("LUM-CLIENT-MIB", "clientIfTrxCodeMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTrxBitrateUnavailable"),
        ("LUM-CLIENT-MIB", "clientIfTrxMissing"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerHigh"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerLow"),
        ("LUM-CLIENT-MIB", "clientIfLinkDown"),
        ("LUM-CLIENT-MIB", "clientIfConfigurationCommand"),
        ("LUM-CLIENT-MIB", "clientIfGbeUtilization"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSync"),
        ("LUM-CLIENT-MIB", "clientIfRxSignalStatus"),
        ("LUM-CLIENT-MIB", "clientIfTrxFailed"),
        ("LUM-CLIENT-MIB", "clientIfDisabled"),
        ("LUM-CLIENT-MIB", "clientIfLoopback"),
        ("LUM-CLIENT-MIB", "clientIfClientSignalFailed"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointer"),
        ("LUM-CLIENT-MIB", "clientIfGfpLossOfFrame"),
        ("LUM-CLIENT-MIB", "clientIfConfigureTrxModeCommand"),
        ("LUM-CLIENT-MIB", "clientIfTrxMode"),
        ("LUM-CLIENT-MIB", "clientIfExpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfUnexpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfIllegalFrequency"),
        ("LUM-CLIENT-MIB", "clientIfLaserForcedOn"),
        ("LUM-CLIENT-MIB", "clientIfTrxMedia"),
        ("LUM-CLIENT-MIB", "clientIfTrxMediaMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTruncAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfObjectProperty"),
        ("LUM-CLIENT-MIB", "clientIfTxPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfLaserTempActual"),
        ("LUM-CLIENT-MIB", "clientIfTraceIntrusionMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceTransmitted"),
        ("LUM-CLIENT-MIB", "clientIfTraceReceived"),
        ("LUM-CLIENT-MIB", "clientIfTraceExpected"),
        ("LUM-CLIENT-MIB", "clientIfTraceAlarmMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceMismatch"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfMsAlarmIndicationSignalC2W"),
        ("LUM-CLIENT-MIB", "clientIfMsAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfRemoteDefectIndication"),
        ("LUM-CLIENT-MIB", "clientIfJ1TxTrailTrace"),
        ("LUM-CLIENT-MIB", "clientIfJ1TxTrailTraceInsertionMode"),
        ("LUM-CLIENT-MIB", "clientIfVcGroupFailedW2C"),
        ("LUM-CLIENT-MIB", "clientIfReadJ1"),
        ("LUM-CLIENT-MIB", "clientIfHighSpeed"),
        ("LUM-CLIENT-MIB", "clientIfActualFormat"),
        ("LUM-CLIENT-MIB", "clientIfRdiIntrusionMode"),
        ("LUM-CLIENT-MIB", "clientIfMuxQuadVc4"),
        ("LUM-CLIENT-MIB", "clientIfDemuxQuadVc4"),
        ("LUM-CLIENT-MIB", "clientIfCcConnectionMode"),
        ("LUM-CLIENT-MIB", "clientIfCcConfigurationCommand"),
        ("LUM-CLIENT-MIB", "clientIfIllegalSignalFormat"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtPortId"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtGroupMemberPort"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtGroupStatus"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtActivePort"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtPortStatus"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtToggleActivePort"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopbackTimeout"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopbackEnabled"),
        ("LUM-CLIENT-MIB", "clientIfChangeNearEndLoopbackCommand"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopbackEnabled"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopbackTimeout"),
        ("LUM-CLIENT-MIB", "clientIfChangeFarEndLoopbackCommand"),
        ("LUM-CLIENT-MIB", "clientIfFormatNotSupportedByHw"),
        ("LUM-CLIENT-MIB", "clientIfLaserMode"),
        ("LUM-CLIENT-MIB", "clientIfAlarmIndicationSignalLineC2W"),
        ("LUM-CLIENT-MIB", "clientIfFarEndClientFailure"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparency"),
        ("LUM-CLIENT-MIB", "clientIfConnectedLine"),
        ("LUM-CLIENT-MIB", "clientIfForwardingErrorCorrectionMode"),
        ("LUM-CLIENT-MIB", "clientIfNoFrequencySet"),
        ("LUM-CLIENT-MIB", "clientIfJitterAttenuatorBW"),
        ("LUM-CLIENT-MIB", "clientIfConnectionStatus"),
        ("LUM-CLIENT-MIB", "clientIfLoopFilterUnlocked"),
        ("LUM-CLIENT-MIB", "clientIfCableLength"),
        ("LUM-CLIENT-MIB", "clientIfConnectedForeignIndex"),
        ("LUM-CLIENT-MIB", "clientIfDisconnect"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparencyBitMask"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparencyString"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparencySet"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalC2W"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerC2W"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerW2C"),
        ("LUM-CLIENT-MIB", "clientIfEthStandbyIndicator"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalW2CSonet"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalC2WSonet"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerC2WSonet"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerW2CSonet"),
        ("LUM-CLIENT-MIB", "clientIfTransceiverNoLoopback"),
        ("LUM-CLIENT-MIB", "clientIfFecFailure"),
        ("LUM-CLIENT-MIB", "clientIfLaneAlignmentError"),
        ("LUM-CLIENT-MIB", "clientIfFecCorrectedZeros"),
        ("LUM-CLIENT-MIB", "clientIfFecCorrectedOnes"),
        ("LUM-CLIENT-MIB", "clientIfSignalDegraded"),
        ("LUM-CLIENT-MIB", "clientIfFecType"),
        ("LUM-CLIENT-MIB", "clientIfSignalDegradeThreshold"),
        ("LUM-CLIENT-MIB", "clientIfExpectedOpticalLayerMapping"),
        ("LUM-CLIENT-MIB", "clientIfActualOpticalLayerMapping"),
        ("LUM-CLIENT-MIB", "clientIfConfigurationMismatch"),
        ("LUM-CLIENT-MIB", "clientIfChromaticDispersion"),
        ("LUM-CLIENT-MIB", "clientIfDifferentialGroupDelay"),
        ("LUM-CLIENT-MIB", "clientIfTxState"),
        ("LUM-CLIENT-MIB", "clientIfRxState"),
        ("LUM-CLIENT-MIB", "clientIfIdx"),
        ("LUM-CLIENT-MIB", "clientIfIfNo"),
        ("LUM-CLIENT-MIB", "clientIfIdxIf"),
        ("LUM-CLIENT-MIB", "clientIfUpPortId"),
        ("LUM-CLIENT-MIB", "clientIfNoOfLanes"),
        ("LUM-CLIENT-MIB", "clientIfFecCorrectedBits"),
        ("LUM-CLIENT-MIB", "clientIfOSNRMargin"),
        ("LUM-CLIENT-MIB", "clientIfExpectedPhysicalLayerMapping"),
        ("LUM-CLIENT-MIB", "clientIfSignalDirection"),
        ("LUM-CLIENT-MIB", "clientIfAid"),
        ("LUM-CLIENT-MIB", "clientIfPhysicalLocation"),
        ("LUM-CLIENT-MIB", "clientIfTrxCommunicationFailure"),
        ("LUM-CLIENT-MIB", "clientIfTribPortId"),
        ("LUM-CLIENT-MIB", "clientIfIfType"))
)
if mibBuilder.loadTexts:
    clientIfGroupV25.setStatus("deprecated")

clientIfGroupV26 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 1, 38)
)
clientIfGroupV26.setObjects(
      *(("LUM-CLIENT-MIB", "clientIfIndex"),
        ("LUM-CLIENT-MIB", "clientIfName"),
        ("LUM-CLIENT-MIB", "clientIfDescr"),
        ("LUM-CLIENT-MIB", "clientIfSubrack"),
        ("LUM-CLIENT-MIB", "clientIfSlot"),
        ("LUM-CLIENT-MIB", "clientIfTxPort"),
        ("LUM-CLIENT-MIB", "clientIfRxPort"),
        ("LUM-CLIENT-MIB", "clientIfInvPhysIndexOrZero"),
        ("LUM-CLIENT-MIB", "clientIfEntityId"),
        ("LUM-CLIENT-MIB", "clientIfAdminStatus"),
        ("LUM-CLIENT-MIB", "clientIfOperStatus"),
        ("LUM-CLIENT-MIB", "clientIfLaserStatus"),
        ("LUM-CLIENT-MIB", "clientIfTxSignalStatus"),
        ("LUM-CLIENT-MIB", "clientIfForwardAls"),
        ("LUM-CLIENT-MIB", "clientIfSuppressRemoteAlarms"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfFormat"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationStatus"),
        ("LUM-CLIENT-MIB", "clientIfDuplexCapability"),
        ("LUM-CLIENT-MIB", "clientIfFlowControlMode"),
        ("LUM-CLIENT-MIB", "clientIfInterPacketGap"),
        ("LUM-CLIENT-MIB", "clientIfFrameSize"),
        ("LUM-CLIENT-MIB", "clientIfGfpMode"),
        ("LUM-CLIENT-MIB", "clientIfBandWidth"),
        ("LUM-CLIENT-MIB", "clientIfRateLimit"),
        ("LUM-CLIENT-MIB", "clientIfTrxClass"),
        ("LUM-CLIENT-MIB", "clientIfLaserBias"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfReceiverSensitivity"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevelLowRelativeThreshold"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSignal"),
        ("LUM-CLIENT-MIB", "clientIfLossOfFrame"),
        ("LUM-CLIENT-MIB", "clientIfBitrateMismatch"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfTransmitterFailed"),
        ("LUM-CLIENT-MIB", "clientIfTrxCodeMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTrxBitrateUnavailable"),
        ("LUM-CLIENT-MIB", "clientIfTrxMissing"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerHigh"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerLow"),
        ("LUM-CLIENT-MIB", "clientIfLinkDown"),
        ("LUM-CLIENT-MIB", "clientIfConfigurationCommand"),
        ("LUM-CLIENT-MIB", "clientIfGbeUtilization"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSync"),
        ("LUM-CLIENT-MIB", "clientIfRxSignalStatus"),
        ("LUM-CLIENT-MIB", "clientIfTrxFailed"),
        ("LUM-CLIENT-MIB", "clientIfDisabled"),
        ("LUM-CLIENT-MIB", "clientIfLoopback"),
        ("LUM-CLIENT-MIB", "clientIfClientSignalFailed"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointer"),
        ("LUM-CLIENT-MIB", "clientIfGfpLossOfFrame"),
        ("LUM-CLIENT-MIB", "clientIfConfigureTrxModeCommand"),
        ("LUM-CLIENT-MIB", "clientIfTrxMode"),
        ("LUM-CLIENT-MIB", "clientIfExpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfUnexpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfIllegalFrequency"),
        ("LUM-CLIENT-MIB", "clientIfLaserForcedOn"),
        ("LUM-CLIENT-MIB", "clientIfTrxMedia"),
        ("LUM-CLIENT-MIB", "clientIfTrxMediaMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTruncAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfObjectProperty"),
        ("LUM-CLIENT-MIB", "clientIfTxPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfLaserTempActual"),
        ("LUM-CLIENT-MIB", "clientIfTraceIntrusionMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceTransmitted"),
        ("LUM-CLIENT-MIB", "clientIfTraceReceived"),
        ("LUM-CLIENT-MIB", "clientIfTraceExpected"),
        ("LUM-CLIENT-MIB", "clientIfTraceAlarmMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceMismatch"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfMsAlarmIndicationSignalC2W"),
        ("LUM-CLIENT-MIB", "clientIfMsAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfRemoteDefectIndication"),
        ("LUM-CLIENT-MIB", "clientIfJ1TxTrailTrace"),
        ("LUM-CLIENT-MIB", "clientIfJ1TxTrailTraceInsertionMode"),
        ("LUM-CLIENT-MIB", "clientIfVcGroupFailedW2C"),
        ("LUM-CLIENT-MIB", "clientIfReadJ1"),
        ("LUM-CLIENT-MIB", "clientIfHighSpeed"),
        ("LUM-CLIENT-MIB", "clientIfActualFormat"),
        ("LUM-CLIENT-MIB", "clientIfRdiIntrusionMode"),
        ("LUM-CLIENT-MIB", "clientIfMuxQuadVc4"),
        ("LUM-CLIENT-MIB", "clientIfDemuxQuadVc4"),
        ("LUM-CLIENT-MIB", "clientIfCcConnectionMode"),
        ("LUM-CLIENT-MIB", "clientIfCcConfigurationCommand"),
        ("LUM-CLIENT-MIB", "clientIfIllegalSignalFormat"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtPortId"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtGroupMemberPort"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtGroupStatus"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtActivePort"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtPortStatus"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtToggleActivePort"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopbackTimeout"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopbackEnabled"),
        ("LUM-CLIENT-MIB", "clientIfChangeNearEndLoopbackCommand"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopbackEnabled"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopbackTimeout"),
        ("LUM-CLIENT-MIB", "clientIfChangeFarEndLoopbackCommand"),
        ("LUM-CLIENT-MIB", "clientIfFormatNotSupportedByHw"),
        ("LUM-CLIENT-MIB", "clientIfLaserMode"),
        ("LUM-CLIENT-MIB", "clientIfAlarmIndicationSignalLineC2W"),
        ("LUM-CLIENT-MIB", "clientIfFarEndClientFailure"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparency"),
        ("LUM-CLIENT-MIB", "clientIfConnectedLine"),
        ("LUM-CLIENT-MIB", "clientIfForwardingErrorCorrectionMode"),
        ("LUM-CLIENT-MIB", "clientIfNoFrequencySet"),
        ("LUM-CLIENT-MIB", "clientIfJitterAttenuatorBW"),
        ("LUM-CLIENT-MIB", "clientIfConnectionStatus"),
        ("LUM-CLIENT-MIB", "clientIfLoopFilterUnlocked"),
        ("LUM-CLIENT-MIB", "clientIfCableLength"),
        ("LUM-CLIENT-MIB", "clientIfConnectedForeignIndex"),
        ("LUM-CLIENT-MIB", "clientIfDisconnect"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparencyBitMask"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparencyString"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparencySet"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalC2W"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerC2W"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerW2C"),
        ("LUM-CLIENT-MIB", "clientIfEthStandbyIndicator"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalW2CSonet"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalC2WSonet"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerC2WSonet"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerW2CSonet"),
        ("LUM-CLIENT-MIB", "clientIfTransceiverNoLoopback"),
        ("LUM-CLIENT-MIB", "clientIfFecFailure"),
        ("LUM-CLIENT-MIB", "clientIfLaneAlignmentError"),
        ("LUM-CLIENT-MIB", "clientIfFecCorrectedZeros"),
        ("LUM-CLIENT-MIB", "clientIfFecCorrectedOnes"),
        ("LUM-CLIENT-MIB", "clientIfSignalDegraded"),
        ("LUM-CLIENT-MIB", "clientIfFecType"),
        ("LUM-CLIENT-MIB", "clientIfSignalDegradeThreshold"),
        ("LUM-CLIENT-MIB", "clientIfExpectedOpticalLayerMapping"),
        ("LUM-CLIENT-MIB", "clientIfActualOpticalLayerMapping"),
        ("LUM-CLIENT-MIB", "clientIfConfigurationMismatch"),
        ("LUM-CLIENT-MIB", "clientIfChromaticDispersion"),
        ("LUM-CLIENT-MIB", "clientIfDifferentialGroupDelay"),
        ("LUM-CLIENT-MIB", "clientIfTxState"),
        ("LUM-CLIENT-MIB", "clientIfRxState"),
        ("LUM-CLIENT-MIB", "clientIfIdx"),
        ("LUM-CLIENT-MIB", "clientIfIfNo"),
        ("LUM-CLIENT-MIB", "clientIfIdxIf"),
        ("LUM-CLIENT-MIB", "clientIfUpPortId"),
        ("LUM-CLIENT-MIB", "clientIfNoOfLanes"),
        ("LUM-CLIENT-MIB", "clientIfFecCorrectedBits"),
        ("LUM-CLIENT-MIB", "clientIfOSNRMargin"),
        ("LUM-CLIENT-MIB", "clientIfExpectedPhysicalLayerMapping"),
        ("LUM-CLIENT-MIB", "clientIfSignalDirection"),
        ("LUM-CLIENT-MIB", "clientIfAid"),
        ("LUM-CLIENT-MIB", "clientIfPhysicalLocation"),
        ("LUM-CLIENT-MIB", "clientIfTrxCommunicationFailure"),
        ("LUM-CLIENT-MIB", "clientIfTribPortId"),
        ("LUM-CLIENT-MIB", "clientIfIfType"),
        ("LUM-CLIENT-MIB", "clientIfConfigurationCommandSNMP"))
)
if mibBuilder.loadTexts:
    clientIfGroupV26.setStatus("deprecated")

clientIfGroupV27 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 1, 39)
)
clientIfGroupV27.setObjects(
      *(("LUM-CLIENT-MIB", "clientIfIndex"),
        ("LUM-CLIENT-MIB", "clientIfName"),
        ("LUM-CLIENT-MIB", "clientIfDescr"),
        ("LUM-CLIENT-MIB", "clientIfSubrack"),
        ("LUM-CLIENT-MIB", "clientIfSlot"),
        ("LUM-CLIENT-MIB", "clientIfTxPort"),
        ("LUM-CLIENT-MIB", "clientIfRxPort"),
        ("LUM-CLIENT-MIB", "clientIfInvPhysIndexOrZero"),
        ("LUM-CLIENT-MIB", "clientIfEntityId"),
        ("LUM-CLIENT-MIB", "clientIfAdminStatus"),
        ("LUM-CLIENT-MIB", "clientIfOperStatus"),
        ("LUM-CLIENT-MIB", "clientIfLaserStatus"),
        ("LUM-CLIENT-MIB", "clientIfTxSignalStatus"),
        ("LUM-CLIENT-MIB", "clientIfForwardAls"),
        ("LUM-CLIENT-MIB", "clientIfSuppressRemoteAlarms"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfFormat"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfAutoNegotiationStatus"),
        ("LUM-CLIENT-MIB", "clientIfDuplexCapability"),
        ("LUM-CLIENT-MIB", "clientIfFlowControlMode"),
        ("LUM-CLIENT-MIB", "clientIfInterPacketGap"),
        ("LUM-CLIENT-MIB", "clientIfFrameSize"),
        ("LUM-CLIENT-MIB", "clientIfGfpMode"),
        ("LUM-CLIENT-MIB", "clientIfBandWidth"),
        ("LUM-CLIENT-MIB", "clientIfRateLimit"),
        ("LUM-CLIENT-MIB", "clientIfTrxClass"),
        ("LUM-CLIENT-MIB", "clientIfLaserBias"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfReceiverSensitivity"),
        ("LUM-CLIENT-MIB", "clientIfPowerLevelLowRelativeThreshold"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSignal"),
        ("LUM-CLIENT-MIB", "clientIfLossOfFrame"),
        ("LUM-CLIENT-MIB", "clientIfBitrateMismatch"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfTransmitterFailed"),
        ("LUM-CLIENT-MIB", "clientIfTrxCodeMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTrxBitrateUnavailable"),
        ("LUM-CLIENT-MIB", "clientIfTrxMissing"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerHigh"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerLow"),
        ("LUM-CLIENT-MIB", "clientIfLinkDown"),
        ("LUM-CLIENT-MIB", "clientIfConfigurationCommand"),
        ("LUM-CLIENT-MIB", "clientIfGbeUtilization"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSync"),
        ("LUM-CLIENT-MIB", "clientIfRxSignalStatus"),
        ("LUM-CLIENT-MIB", "clientIfTrxFailed"),
        ("LUM-CLIENT-MIB", "clientIfDisabled"),
        ("LUM-CLIENT-MIB", "clientIfLoopback"),
        ("LUM-CLIENT-MIB", "clientIfClientSignalFailed"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointer"),
        ("LUM-CLIENT-MIB", "clientIfGfpLossOfFrame"),
        ("LUM-CLIENT-MIB", "clientIfConfigureTrxModeCommand"),
        ("LUM-CLIENT-MIB", "clientIfTrxMode"),
        ("LUM-CLIENT-MIB", "clientIfExpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfUnexpectedTxFrequency"),
        ("LUM-CLIENT-MIB", "clientIfIllegalFrequency"),
        ("LUM-CLIENT-MIB", "clientIfLaserForcedOn"),
        ("LUM-CLIENT-MIB", "clientIfTrxMedia"),
        ("LUM-CLIENT-MIB", "clientIfTrxMediaMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTruncAutoNegotiationMode"),
        ("LUM-CLIENT-MIB", "clientIfObjectProperty"),
        ("LUM-CLIENT-MIB", "clientIfTxPowerLevel"),
        ("LUM-CLIENT-MIB", "clientIfLaserTempActual"),
        ("LUM-CLIENT-MIB", "clientIfTraceIntrusionMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceTransmitted"),
        ("LUM-CLIENT-MIB", "clientIfTraceReceived"),
        ("LUM-CLIENT-MIB", "clientIfTraceExpected"),
        ("LUM-CLIENT-MIB", "clientIfTraceAlarmMode"),
        ("LUM-CLIENT-MIB", "clientIfTraceMismatch"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopback"),
        ("LUM-CLIENT-MIB", "clientIfMsAlarmIndicationSignalC2W"),
        ("LUM-CLIENT-MIB", "clientIfMsAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfRemoteDefectIndication"),
        ("LUM-CLIENT-MIB", "clientIfJ1TxTrailTrace"),
        ("LUM-CLIENT-MIB", "clientIfJ1TxTrailTraceInsertionMode"),
        ("LUM-CLIENT-MIB", "clientIfVcGroupFailedW2C"),
        ("LUM-CLIENT-MIB", "clientIfReadJ1"),
        ("LUM-CLIENT-MIB", "clientIfHighSpeed"),
        ("LUM-CLIENT-MIB", "clientIfActualFormat"),
        ("LUM-CLIENT-MIB", "clientIfRdiIntrusionMode"),
        ("LUM-CLIENT-MIB", "clientIfMuxQuadVc4"),
        ("LUM-CLIENT-MIB", "clientIfDemuxQuadVc4"),
        ("LUM-CLIENT-MIB", "clientIfCcConnectionMode"),
        ("LUM-CLIENT-MIB", "clientIfCcConfigurationCommand"),
        ("LUM-CLIENT-MIB", "clientIfIllegalSignalFormat"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtPortId"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtGroupMemberPort"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtGroupStatus"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtActivePort"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtPortStatus"),
        ("LUM-CLIENT-MIB", "clientIfSynchProtToggleActivePort"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopbackTimeout"),
        ("LUM-CLIENT-MIB", "clientIfNearEndLoopbackEnabled"),
        ("LUM-CLIENT-MIB", "clientIfChangeNearEndLoopbackCommand"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopbackEnabled"),
        ("LUM-CLIENT-MIB", "clientIfFarEndLoopbackTimeout"),
        ("LUM-CLIENT-MIB", "clientIfChangeFarEndLoopbackCommand"),
        ("LUM-CLIENT-MIB", "clientIfFormatNotSupportedByHw"),
        ("LUM-CLIENT-MIB", "clientIfLaserMode"),
        ("LUM-CLIENT-MIB", "clientIfAlarmIndicationSignalLineC2W"),
        ("LUM-CLIENT-MIB", "clientIfFarEndClientFailure"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparency"),
        ("LUM-CLIENT-MIB", "clientIfConnectedLine"),
        ("LUM-CLIENT-MIB", "clientIfForwardingErrorCorrectionMode"),
        ("LUM-CLIENT-MIB", "clientIfNoFrequencySet"),
        ("LUM-CLIENT-MIB", "clientIfJitterAttenuatorBW"),
        ("LUM-CLIENT-MIB", "clientIfConnectionStatus"),
        ("LUM-CLIENT-MIB", "clientIfLoopFilterUnlocked"),
        ("LUM-CLIENT-MIB", "clientIfCableLength"),
        ("LUM-CLIENT-MIB", "clientIfConnectedForeignIndex"),
        ("LUM-CLIENT-MIB", "clientIfDisconnect"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparencyBitMask"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparencyString"),
        ("LUM-CLIENT-MIB", "clientIfOHTransparencySet"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalC2W"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerC2W"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerW2C"),
        ("LUM-CLIENT-MIB", "clientIfEthStandbyIndicator"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalW2CSonet"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalC2WSonet"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerC2WSonet"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointerW2CSonet"),
        ("LUM-CLIENT-MIB", "clientIfTransceiverNoLoopback"),
        ("LUM-CLIENT-MIB", "clientIfFecFailure"),
        ("LUM-CLIENT-MIB", "clientIfLaneAlignmentError"),
        ("LUM-CLIENT-MIB", "clientIfFecCorrectedZeros"),
        ("LUM-CLIENT-MIB", "clientIfFecCorrectedOnes"),
        ("LUM-CLIENT-MIB", "clientIfSignalDegraded"),
        ("LUM-CLIENT-MIB", "clientIfFecType"),
        ("LUM-CLIENT-MIB", "clientIfSignalDegradeThreshold"),
        ("LUM-CLIENT-MIB", "clientIfExpectedOpticalLayerMapping"),
        ("LUM-CLIENT-MIB", "clientIfActualOpticalLayerMapping"),
        ("LUM-CLIENT-MIB", "clientIfConfigurationMismatch"),
        ("LUM-CLIENT-MIB", "clientIfChromaticDispersion"),
        ("LUM-CLIENT-MIB", "clientIfDifferentialGroupDelay"),
        ("LUM-CLIENT-MIB", "clientIfTxState"),
        ("LUM-CLIENT-MIB", "clientIfRxState"),
        ("LUM-CLIENT-MIB", "clientIfIdx"),
        ("LUM-CLIENT-MIB", "clientIfIfNo"),
        ("LUM-CLIENT-MIB", "clientIfIdxIf"),
        ("LUM-CLIENT-MIB", "clientIfUpPortId"),
        ("LUM-CLIENT-MIB", "clientIfNoOfLanes"),
        ("LUM-CLIENT-MIB", "clientIfFecCorrectedBits"),
        ("LUM-CLIENT-MIB", "clientIfOSNRMargin"),
        ("LUM-CLIENT-MIB", "clientIfExpectedPhysicalLayerMapping"),
        ("LUM-CLIENT-MIB", "clientIfSignalDirection"),
        ("LUM-CLIENT-MIB", "clientIfAid"),
        ("LUM-CLIENT-MIB", "clientIfPhysicalLocation"),
        ("LUM-CLIENT-MIB", "clientIfTrxCommunicationFailure"),
        ("LUM-CLIENT-MIB", "clientIfTribPortId"),
        ("LUM-CLIENT-MIB", "clientIfIfType"),
        ("LUM-CLIENT-MIB", "clientIfConfigurationCommandSNMP"),
        ("LUM-CLIENT-MIB", "clientIfTrxPowerOutOfRange"))
)
if mibBuilder.loadTexts:
    clientIfGroupV27.setStatus("current")

clientIfMinimalGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 3, 1)
)
clientIfMinimalGroupV1.setObjects(
      *(("LUM-CLIENT-MIB", "clientIfIndex"),
        ("LUM-CLIENT-MIB", "clientIfName"),
        ("LUM-CLIENT-MIB", "clientIfDescr"),
        ("LUM-CLIENT-MIB", "clientIfSubrack"),
        ("LUM-CLIENT-MIB", "clientIfSlot"),
        ("LUM-CLIENT-MIB", "clientIfTxPort"),
        ("LUM-CLIENT-MIB", "clientIfRxPort"),
        ("LUM-CLIENT-MIB", "clientIfInvPhysIndexOrZero"),
        ("LUM-CLIENT-MIB", "clientIfEntityId"),
        ("LUM-CLIENT-MIB", "clientIfAdminStatus"),
        ("LUM-CLIENT-MIB", "clientIfOperStatus"),
        ("LUM-CLIENT-MIB", "clientIfTxSignalStatus"),
        ("LUM-CLIENT-MIB", "clientIfFormat"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSignal"),
        ("LUM-CLIENT-MIB", "clientIfLossOfFrame"),
        ("LUM-CLIENT-MIB", "clientIfBitrateMismatch"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfTransmitterFailed"),
        ("LUM-CLIENT-MIB", "clientIfTrxCodeMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTrxBitrateUnavailable"),
        ("LUM-CLIENT-MIB", "clientIfTrxMissing"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerHigh"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerLow"),
        ("LUM-CLIENT-MIB", "clientIfLinkDown"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSync"),
        ("LUM-CLIENT-MIB", "clientIfRxSignalStatus"))
)
if mibBuilder.loadTexts:
    clientIfMinimalGroupV1.setStatus("deprecated")

clientIfMinimalGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 3, 2)
)
clientIfMinimalGroupV2.setObjects(
      *(("LUM-CLIENT-MIB", "clientIfIndex"),
        ("LUM-CLIENT-MIB", "clientIfName"),
        ("LUM-CLIENT-MIB", "clientIfDescr"),
        ("LUM-CLIENT-MIB", "clientIfSubrack"),
        ("LUM-CLIENT-MIB", "clientIfSlot"),
        ("LUM-CLIENT-MIB", "clientIfTxPort"),
        ("LUM-CLIENT-MIB", "clientIfRxPort"),
        ("LUM-CLIENT-MIB", "clientIfInvPhysIndexOrZero"),
        ("LUM-CLIENT-MIB", "clientIfEntityId"),
        ("LUM-CLIENT-MIB", "clientIfAdminStatus"),
        ("LUM-CLIENT-MIB", "clientIfOperStatus"),
        ("LUM-CLIENT-MIB", "clientIfTxSignalStatus"),
        ("LUM-CLIENT-MIB", "clientIfFormat"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSignal"),
        ("LUM-CLIENT-MIB", "clientIfLossOfFrame"),
        ("LUM-CLIENT-MIB", "clientIfBitrateMismatch"),
        ("LUM-CLIENT-MIB", "clientIfAuAlarmIndicationSignalW2C"),
        ("LUM-CLIENT-MIB", "clientIfTransmitterFailed"),
        ("LUM-CLIENT-MIB", "clientIfTrxCodeMismatch"),
        ("LUM-CLIENT-MIB", "clientIfTrxBitrateUnavailable"),
        ("LUM-CLIENT-MIB", "clientIfTrxMissing"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerHigh"),
        ("LUM-CLIENT-MIB", "clientIfReceivedPowerLow"),
        ("LUM-CLIENT-MIB", "clientIfLinkDown"),
        ("LUM-CLIENT-MIB", "clientIfLossOfSync"),
        ("LUM-CLIENT-MIB", "clientIfRxSignalStatus"),
        ("LUM-CLIENT-MIB", "clientIfTrxFailed"),
        ("LUM-CLIENT-MIB", "clientIfDisabled"),
        ("LUM-CLIENT-MIB", "clientIfLoopback"),
        ("LUM-CLIENT-MIB", "clientIfClientSignalFailed"),
        ("LUM-CLIENT-MIB", "clientIfAuLossOfPointer"),
        ("LUM-CLIENT-MIB", "clientIfGfpLossOfFrame"))
)
if mibBuilder.loadTexts:
    clientIfMinimalGroupV2.setStatus("current")


# Notification objects

clientIfTxSignalStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 4, 0, 1)
)
clientIfTxSignalStatusDown.setObjects(
      *(("LUM-CLIENT-MIB", "clientIfIndex"),
        ("LUM-CLIENT-MIB", "clientIfName"),
        ("LUM-CLIENT-MIB", "clientIfSubrack"),
        ("LUM-CLIENT-MIB", "clientIfSlot"),
        ("LUM-CLIENT-MIB", "clientIfTxPort"),
        ("LUM-CLIENT-MIB", "clientIfRxPort"),
        ("LUM-CLIENT-MIB", "clientIfEntityId"),
        ("LUM-CLIENT-MIB", "clientIfTxSignalStatus"))
)
if mibBuilder.loadTexts:
    clientIfTxSignalStatusDown.setStatus(
        "current"
    )

clientIfTxSignalStatusUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 4, 0, 2)
)
clientIfTxSignalStatusUp.setObjects(
      *(("LUM-CLIENT-MIB", "clientIfIndex"),
        ("LUM-CLIENT-MIB", "clientIfName"),
        ("LUM-CLIENT-MIB", "clientIfSubrack"),
        ("LUM-CLIENT-MIB", "clientIfSlot"),
        ("LUM-CLIENT-MIB", "clientIfTxPort"),
        ("LUM-CLIENT-MIB", "clientIfRxPort"),
        ("LUM-CLIENT-MIB", "clientIfEntityId"),
        ("LUM-CLIENT-MIB", "clientIfTxSignalStatus"))
)
if mibBuilder.loadTexts:
    clientIfTxSignalStatusUp.setStatus(
        "current"
    )

clientIfTxSignalStatusDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 2, 4, 0, 3)
)
clientIfTxSignalStatusDegraded.setObjects(
      *(("LUM-CLIENT-MIB", "clientIfIndex"),
        ("LUM-CLIENT-MIB", "clientIfName"),
        ("LUM-CLIENT-MIB", "clientIfSubrack"),
        ("LUM-CLIENT-MIB", "clientIfSlot"),
        ("LUM-CLIENT-MIB", "clientIfTxPort"),
        ("LUM-CLIENT-MIB", "clientIfRxPort"),
        ("LUM-CLIENT-MIB", "clientIfEntityId"),
        ("LUM-CLIENT-MIB", "clientIfTxSignalStatus"))
)
if mibBuilder.loadTexts:
    clientIfTxSignalStatusDegraded.setStatus(
        "current"
    )


# Notifications groups

clientNotificationGroupV1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 1, 2)
)
clientNotificationGroupV1.setObjects(
      *(("LUM-CLIENT-MIB", "clientIfTxSignalStatusDown"),
        ("LUM-CLIENT-MIB", "clientIfTxSignalStatusUp"),
        ("LUM-CLIENT-MIB", "clientIfTxSignalStatusDegraded"))
)
if mibBuilder.loadTexts:
    clientNotificationGroupV1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

lumClientBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 2, 1)
)
lumClientBasicComplV1.setObjects(
      *(("LUM-CLIENT-MIB", "clientGeneralGroupV1"),
        ("LUM-CLIENT-MIB", "clientIfGroupV1"))
)
if mibBuilder.loadTexts:
    lumClientBasicComplV1.setStatus(
        "deprecated"
    )

lumClientBasicComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 2, 2)
)
lumClientBasicComplV2.setObjects(
      *(("LUM-CLIENT-MIB", "clientGeneralGroupV2"),
        ("LUM-CLIENT-MIB", "clientIfGroupV2"))
)
if mibBuilder.loadTexts:
    lumClientBasicComplV2.setStatus(
        "deprecated"
    )

lumClientBasicComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 2, 3)
)
lumClientBasicComplV3.setObjects(
      *(("LUM-CLIENT-MIB", "clientGeneralGroupV2"),
        ("LUM-CLIENT-MIB", "clientIfGroupV3"))
)
if mibBuilder.loadTexts:
    lumClientBasicComplV3.setStatus(
        "deprecated"
    )

lumClientBasicComplV4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 2, 4)
)
lumClientBasicComplV4.setObjects(
      *(("LUM-CLIENT-MIB", "clientGeneralGroupV2"),
        ("LUM-CLIENT-MIB", "clientIfGroupV4"))
)
if mibBuilder.loadTexts:
    lumClientBasicComplV4.setStatus(
        "deprecated"
    )

lumClientBasicComplV5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 2, 5)
)
lumClientBasicComplV5.setObjects(
      *(("LUM-CLIENT-MIB", "clientGeneralGroupV2"),
        ("LUM-CLIENT-MIB", "clientIfGroupV5"))
)
if mibBuilder.loadTexts:
    lumClientBasicComplV5.setStatus(
        "deprecated"
    )

lumClientBasicComplV6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 2, 6)
)
lumClientBasicComplV6.setObjects(
      *(("LUM-CLIENT-MIB", "clientGeneralGroupV2"),
        ("LUM-CLIENT-MIB", "clientIfGroupV6"))
)
if mibBuilder.loadTexts:
    lumClientBasicComplV6.setStatus(
        "deprecated"
    )

lumClientBasicComplV7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 2, 7)
)
lumClientBasicComplV7.setObjects(
      *(("LUM-CLIENT-MIB", "clientGeneralGroupV2"),
        ("LUM-CLIENT-MIB", "clientIfGroupV7"))
)
if mibBuilder.loadTexts:
    lumClientBasicComplV7.setStatus(
        "deprecated"
    )

lumClientBasicComplV8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 2, 8)
)
lumClientBasicComplV8.setObjects(
      *(("LUM-CLIENT-MIB", "clientGeneralGroupV2"),
        ("LUM-CLIENT-MIB", "clientIfGroupV8"))
)
if mibBuilder.loadTexts:
    lumClientBasicComplV8.setStatus(
        "deprecated"
    )

lumClientBasicComplV9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 2, 9)
)
lumClientBasicComplV9.setObjects(
      *(("LUM-CLIENT-MIB", "clientGeneralGroupV3"),
        ("LUM-CLIENT-MIB", "clientIfGroupV8"),
        ("LUM-CLIENT-MIB", "clientVc4Group"))
)
if mibBuilder.loadTexts:
    lumClientBasicComplV9.setStatus(
        "deprecated"
    )

lumClientBasicComplV10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 2, 10)
)
lumClientBasicComplV10.setObjects(
      *(("LUM-CLIENT-MIB", "clientGeneralGroupV3"),
        ("LUM-CLIENT-MIB", "clientIfGroupV9"),
        ("LUM-CLIENT-MIB", "clientVc4Group"))
)
if mibBuilder.loadTexts:
    lumClientBasicComplV10.setStatus(
        "deprecated"
    )

lumClientBasicComplV11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 2, 11)
)
lumClientBasicComplV11.setObjects(
      *(("LUM-CLIENT-MIB", "clientGeneralGroupV3"),
        ("LUM-CLIENT-MIB", "clientIfGroupV10"),
        ("LUM-CLIENT-MIB", "clientVc4Group"))
)
if mibBuilder.loadTexts:
    lumClientBasicComplV11.setStatus(
        "deprecated"
    )

lumClientBasicComplV12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 2, 12)
)
lumClientBasicComplV12.setObjects(
      *(("LUM-CLIENT-MIB", "clientGeneralGroupV3"),
        ("LUM-CLIENT-MIB", "clientIfGroupV11"),
        ("LUM-CLIENT-MIB", "clientVc4Group"))
)
if mibBuilder.loadTexts:
    lumClientBasicComplV12.setStatus(
        "deprecated"
    )

lumClientBasicComplV13 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 2, 13)
)
lumClientBasicComplV13.setObjects(
      *(("LUM-CLIENT-MIB", "clientGeneralGroupV3"),
        ("LUM-CLIENT-MIB", "clientIfGroupV12"),
        ("LUM-CLIENT-MIB", "clientVc4Group"))
)
if mibBuilder.loadTexts:
    lumClientBasicComplV13.setStatus(
        "deprecated"
    )

lumClientBasicComplV14 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 2, 14)
)
lumClientBasicComplV14.setObjects(
      *(("LUM-CLIENT-MIB", "clientGeneralGroupV3"),
        ("LUM-CLIENT-MIB", "clientIfGroupV13"),
        ("LUM-CLIENT-MIB", "clientVc4GroupV2"))
)
if mibBuilder.loadTexts:
    lumClientBasicComplV14.setStatus(
        "deprecated"
    )

lumClientBasicComplV15 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 2, 15)
)
lumClientBasicComplV15.setObjects(
      *(("LUM-CLIENT-MIB", "clientGeneralGroupV3"),
        ("LUM-CLIENT-MIB", "clientIfGroupV14"),
        ("LUM-CLIENT-MIB", "clientVc4GroupV2"))
)
if mibBuilder.loadTexts:
    lumClientBasicComplV15.setStatus(
        "deprecated"
    )

lumClientBasicComplV16 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 2, 16)
)
lumClientBasicComplV16.setObjects(
      *(("LUM-CLIENT-MIB", "clientGeneralGroupV3"),
        ("LUM-CLIENT-MIB", "clientIfGroupV15"),
        ("LUM-CLIENT-MIB", "clientVc4GroupV2"))
)
if mibBuilder.loadTexts:
    lumClientBasicComplV16.setStatus(
        "deprecated"
    )

lumClientBasicComplV17 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 2, 17)
)
lumClientBasicComplV17.setObjects(
      *(("LUM-CLIENT-MIB", "clientGeneralGroupV3"),
        ("LUM-CLIENT-MIB", "clientIfGroupV16"),
        ("LUM-CLIENT-MIB", "clientVc4GroupV2"))
)
if mibBuilder.loadTexts:
    lumClientBasicComplV17.setStatus(
        "deprecated"
    )

lumClientBasicComplV18 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 2, 18)
)
lumClientBasicComplV18.setObjects(
      *(("LUM-CLIENT-MIB", "clientGeneralGroupV3"),
        ("LUM-CLIENT-MIB", "clientIfGroupV17"),
        ("LUM-CLIENT-MIB", "clientVc4GroupV2"),
        ("LUM-CLIENT-MIB", "clientLanesGroup"))
)
if mibBuilder.loadTexts:
    lumClientBasicComplV18.setStatus(
        "deprecated"
    )

lumClientBasicComplV19 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 2, 19)
)
lumClientBasicComplV19.setObjects(
      *(("LUM-CLIENT-MIB", "clientGeneralGroupV3"),
        ("LUM-CLIENT-MIB", "clientIfGroupV18"),
        ("LUM-CLIENT-MIB", "clientVc4GroupV2"),
        ("LUM-CLIENT-MIB", "clientLanesGroup"))
)
if mibBuilder.loadTexts:
    lumClientBasicComplV19.setStatus(
        "deprecated"
    )

lumClientBasicComplV20 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 2, 20)
)
lumClientBasicComplV20.setObjects(
      *(("LUM-CLIENT-MIB", "clientGeneralGroupV3"),
        ("LUM-CLIENT-MIB", "clientIfGroupV19"),
        ("LUM-CLIENT-MIB", "clientVc4GroupV2"),
        ("LUM-CLIENT-MIB", "clientLanesGroup"))
)
if mibBuilder.loadTexts:
    lumClientBasicComplV20.setStatus(
        "deprecated"
    )

lumClientBasicComplV21 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 2, 21)
)
lumClientBasicComplV21.setObjects(
      *(("LUM-CLIENT-MIB", "clientGeneralGroupV3"),
        ("LUM-CLIENT-MIB", "clientIfGroupV20"),
        ("LUM-CLIENT-MIB", "clientVc4GroupV2"),
        ("LUM-CLIENT-MIB", "clientLanesGroupV2"))
)
if mibBuilder.loadTexts:
    lumClientBasicComplV21.setStatus(
        "deprecated"
    )

lumClientBasicComplV22 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 2, 22)
)
lumClientBasicComplV22.setObjects(
      *(("LUM-CLIENT-MIB", "clientGeneralGroupV3"),
        ("LUM-CLIENT-MIB", "clientIfGroupV21"),
        ("LUM-CLIENT-MIB", "clientVc4GroupV2"),
        ("LUM-CLIENT-MIB", "clientLanesGroupV2"))
)
if mibBuilder.loadTexts:
    lumClientBasicComplV22.setStatus(
        "deprecated"
    )

lumClientBasicComplV23 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 2, 23)
)
lumClientBasicComplV23.setObjects(
      *(("LUM-CLIENT-MIB", "clientGeneralGroupV3"),
        ("LUM-CLIENT-MIB", "clientIfGroupV22"),
        ("LUM-CLIENT-MIB", "clientVc4GroupV2"),
        ("LUM-CLIENT-MIB", "clientLanesGroupV3"))
)
if mibBuilder.loadTexts:
    lumClientBasicComplV23.setStatus(
        "deprecated"
    )

lumClientBasicComplV24 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 2, 24)
)
lumClientBasicComplV24.setObjects(
      *(("LUM-CLIENT-MIB", "clientGeneralGroupV3"),
        ("LUM-CLIENT-MIB", "clientIfGroupV22"),
        ("LUM-CLIENT-MIB", "clientVc4GroupV2"),
        ("LUM-CLIENT-MIB", "clientLanesGroupV4"),
        ("LUM-CLIENT-MIB", "clientMpoLanesGroupV1"))
)
if mibBuilder.loadTexts:
    lumClientBasicComplV24.setStatus(
        "deprecated"
    )

lumClientBasicComplV25 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 2, 25)
)
lumClientBasicComplV25.setObjects(
      *(("LUM-CLIENT-MIB", "clientGeneralGroupV3"),
        ("LUM-CLIENT-MIB", "clientIfGroupV22"),
        ("LUM-CLIENT-MIB", "clientVc4GroupV2"),
        ("LUM-CLIENT-MIB", "clientLanesGroupV5"),
        ("LUM-CLIENT-MIB", "clientMpoLanesGroupV1"))
)
if mibBuilder.loadTexts:
    lumClientBasicComplV25.setStatus(
        "deprecated"
    )

lumClientBasicComplV26 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 2, 26)
)
lumClientBasicComplV26.setObjects(
      *(("LUM-CLIENT-MIB", "clientGeneralGroupV3"),
        ("LUM-CLIENT-MIB", "clientIfGroupV23"),
        ("LUM-CLIENT-MIB", "clientVc4GroupV2"),
        ("LUM-CLIENT-MIB", "clientLanesGroupV5"),
        ("LUM-CLIENT-MIB", "clientMpoLanesGroupV1"))
)
if mibBuilder.loadTexts:
    lumClientBasicComplV26.setStatus(
        "deprecated"
    )

lumClientBasicComplV27 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 2, 27)
)
lumClientBasicComplV27.setObjects(
      *(("LUM-CLIENT-MIB", "clientGeneralGroupV3"),
        ("LUM-CLIENT-MIB", "clientIfGroupV24"),
        ("LUM-CLIENT-MIB", "clientVc4GroupV2"),
        ("LUM-CLIENT-MIB", "clientLanesGroupV5"),
        ("LUM-CLIENT-MIB", "clientMpoLanesGroupV1"))
)
if mibBuilder.loadTexts:
    lumClientBasicComplV27.setStatus(
        "deprecated"
    )

lumClientBasicComplV28 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 2, 28)
)
lumClientBasicComplV28.setObjects(
      *(("LUM-CLIENT-MIB", "clientGeneralGroupV3"),
        ("LUM-CLIENT-MIB", "clientIfGroupV25"),
        ("LUM-CLIENT-MIB", "clientVc4GroupV2"),
        ("LUM-CLIENT-MIB", "clientLanesGroupV5"),
        ("LUM-CLIENT-MIB", "clientMpoLanesGroupV1"))
)
if mibBuilder.loadTexts:
    lumClientBasicComplV28.setStatus(
        "deprecated"
    )

lumClientBasicComplV29 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 2, 29)
)
lumClientBasicComplV29.setObjects(
      *(("LUM-CLIENT-MIB", "clientGeneralGroupV3"),
        ("LUM-CLIENT-MIB", "clientIfGroupV26"),
        ("LUM-CLIENT-MIB", "clientVc4GroupV2"),
        ("LUM-CLIENT-MIB", "clientLanesGroupV5"),
        ("LUM-CLIENT-MIB", "clientMpoLanesGroupV1"))
)
if mibBuilder.loadTexts:
    lumClientBasicComplV29.setStatus(
        "deprecated"
    )

lumClientBasicComplV30 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 2, 30)
)
lumClientBasicComplV30.setObjects(
      *(("LUM-CLIENT-MIB", "clientGeneralGroupV3"),
        ("LUM-CLIENT-MIB", "clientIfGroupV27"),
        ("LUM-CLIENT-MIB", "clientVc4GroupV2"),
        ("LUM-CLIENT-MIB", "clientLanesGroupV5"),
        ("LUM-CLIENT-MIB", "clientMpoLanesGroupV1"))
)
if mibBuilder.loadTexts:
    lumClientBasicComplV30.setStatus(
        "current"
    )

lumClientMinimalComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 4, 1)
)
lumClientMinimalComplV1.setObjects(
      *(("LUM-CLIENT-MIB", "clientGeneralGroupV2"),
        ("LUM-CLIENT-MIB", "clientIfMinimalGroupV1"))
)
if mibBuilder.loadTexts:
    lumClientMinimalComplV1.setStatus(
        "deprecated"
    )

lumClientMinimalComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 27, 1, 4, 2)
)
lumClientMinimalComplV2.setObjects(
      *(("LUM-CLIENT-MIB", "clientGeneralGroupV2"),
        ("LUM-CLIENT-MIB", "clientIfMinimalGroupV2"))
)
if mibBuilder.loadTexts:
    lumClientMinimalComplV2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-CLIENT-MIB",
    **{"lumClientMIBModule": lumClientMIBModule,
       "lumClientConfs": lumClientConfs,
       "lumClientGroups": lumClientGroups,
       "clientGeneralGroupV1": clientGeneralGroupV1,
       "clientNotificationGroupV1": clientNotificationGroupV1,
       "clientIfGroupV1": clientIfGroupV1,
       "clientIfGroupV2": clientIfGroupV2,
       "clientGeneralGroupV2": clientGeneralGroupV2,
       "clientIfGroupV3": clientIfGroupV3,
       "clientIfGroupV4": clientIfGroupV4,
       "clientIfGroupV5": clientIfGroupV5,
       "clientIfGroupV6": clientIfGroupV6,
       "clientIfGroupV7": clientIfGroupV7,
       "clientIfGroupV8": clientIfGroupV8,
       "clientVc4Group": clientVc4Group,
       "clientGeneralGroupV3": clientGeneralGroupV3,
       "clientIfGroupV9": clientIfGroupV9,
       "clientIfGroupV10": clientIfGroupV10,
       "clientIfGroupV11": clientIfGroupV11,
       "clientIfGroupV12": clientIfGroupV12,
       "clientIfGroupV13": clientIfGroupV13,
       "clientVc4GroupV2": clientVc4GroupV2,
       "clientIfGroupV14": clientIfGroupV14,
       "clientIfGroupV15": clientIfGroupV15,
       "clientIfGroupV16": clientIfGroupV16,
       "clientIfGroupV17": clientIfGroupV17,
       "clientLanesGroup": clientLanesGroup,
       "clientIfGroupV18": clientIfGroupV18,
       "clientIfGroupV19": clientIfGroupV19,
       "clientIfGroupV20": clientIfGroupV20,
       "clientLanesGroupV2": clientLanesGroupV2,
       "clientIfGroupV21": clientIfGroupV21,
       "clientIfGroupV22": clientIfGroupV22,
       "clientLanesGroupV3": clientLanesGroupV3,
       "clientLanesGroupV4": clientLanesGroupV4,
       "clientMpoLanesGroupV1": clientMpoLanesGroupV1,
       "clientLanesGroupV5": clientLanesGroupV5,
       "clientIfGroupV23": clientIfGroupV23,
       "clientIfGroupV24": clientIfGroupV24,
       "clientIfGroupV25": clientIfGroupV25,
       "clientIfGroupV26": clientIfGroupV26,
       "clientIfGroupV27": clientIfGroupV27,
       "lumClientCompl": lumClientCompl,
       "lumClientBasicComplV1": lumClientBasicComplV1,
       "lumClientBasicComplV2": lumClientBasicComplV2,
       "lumClientBasicComplV3": lumClientBasicComplV3,
       "lumClientBasicComplV4": lumClientBasicComplV4,
       "lumClientBasicComplV5": lumClientBasicComplV5,
       "lumClientBasicComplV6": lumClientBasicComplV6,
       "lumClientBasicComplV7": lumClientBasicComplV7,
       "lumClientBasicComplV8": lumClientBasicComplV8,
       "lumClientBasicComplV9": lumClientBasicComplV9,
       "lumClientBasicComplV10": lumClientBasicComplV10,
       "lumClientBasicComplV11": lumClientBasicComplV11,
       "lumClientBasicComplV12": lumClientBasicComplV12,
       "lumClientBasicComplV13": lumClientBasicComplV13,
       "lumClientBasicComplV14": lumClientBasicComplV14,
       "lumClientBasicComplV15": lumClientBasicComplV15,
       "lumClientBasicComplV16": lumClientBasicComplV16,
       "lumClientBasicComplV17": lumClientBasicComplV17,
       "lumClientBasicComplV18": lumClientBasicComplV18,
       "lumClientBasicComplV19": lumClientBasicComplV19,
       "lumClientBasicComplV20": lumClientBasicComplV20,
       "lumClientBasicComplV21": lumClientBasicComplV21,
       "lumClientBasicComplV22": lumClientBasicComplV22,
       "lumClientBasicComplV23": lumClientBasicComplV23,
       "lumClientBasicComplV24": lumClientBasicComplV24,
       "lumClientBasicComplV25": lumClientBasicComplV25,
       "lumClientBasicComplV26": lumClientBasicComplV26,
       "lumClientBasicComplV27": lumClientBasicComplV27,
       "lumClientBasicComplV28": lumClientBasicComplV28,
       "lumClientBasicComplV29": lumClientBasicComplV29,
       "lumClientBasicComplV30": lumClientBasicComplV30,
       "lumClientMinimalGroups": lumClientMinimalGroups,
       "clientIfMinimalGroupV1": clientIfMinimalGroupV1,
       "clientIfMinimalGroupV2": clientIfMinimalGroupV2,
       "lumClientMinimalCompl": lumClientMinimalCompl,
       "lumClientMinimalComplV1": lumClientMinimalComplV1,
       "lumClientMinimalComplV2": lumClientMinimalComplV2,
       "lumClientMIBObjects": lumClientMIBObjects,
       "clientGeneral": clientGeneral,
       "clientGeneralLastChangeTime": clientGeneralLastChangeTime,
       "clientGeneralStateLastChangeTime": clientGeneralStateLastChangeTime,
       "clientGeneralClientIfTableSize": clientGeneralClientIfTableSize,
       "clientGeneralVc4TableSize": clientGeneralVc4TableSize,
       "clientGeneralLanesTableSize": clientGeneralLanesTableSize,
       "clientGeneralMpoLanesTableSize": clientGeneralMpoLanesTableSize,
       "clientIfList": clientIfList,
       "clientIfTable": clientIfTable,
       "clientIfEntry": clientIfEntry,
       "clientIfIndex": clientIfIndex,
       "clientIfName": clientIfName,
       "clientIfDescr": clientIfDescr,
       "clientIfSubrack": clientIfSubrack,
       "clientIfSlot": clientIfSlot,
       "clientIfTxPort": clientIfTxPort,
       "clientIfRxPort": clientIfRxPort,
       "clientIfInvPhysIndexOrZero": clientIfInvPhysIndexOrZero,
       "clientIfEntityId": clientIfEntityId,
       "clientIfAdminStatus": clientIfAdminStatus,
       "clientIfOperStatus": clientIfOperStatus,
       "clientIfLaserStatus": clientIfLaserStatus,
       "clientIfTxSignalStatus": clientIfTxSignalStatus,
       "clientIfForwardAls": clientIfForwardAls,
       "clientIfSuppressRemoteAlarms": clientIfSuppressRemoteAlarms,
       "clientIfFarEndLoopback": clientIfFarEndLoopback,
       "clientIfFormat": clientIfFormat,
       "clientIfGfpMode": clientIfGfpMode,
       "clientIfBandWidth": clientIfBandWidth,
       "clientIfRateLimit": clientIfRateLimit,
       "clientIfAutoNegotiationMode": clientIfAutoNegotiationMode,
       "clientIfAutoNegotiationStatus": clientIfAutoNegotiationStatus,
       "clientIfDuplexCapability": clientIfDuplexCapability,
       "clientIfFlowControlMode": clientIfFlowControlMode,
       "clientIfInterPacketGap": clientIfInterPacketGap,
       "clientIfFrameSize": clientIfFrameSize,
       "clientIfTrxClass": clientIfTrxClass,
       "clientIfLaserBias": clientIfLaserBias,
       "clientIfPowerLevel": clientIfPowerLevel,
       "clientIfReceiverSensitivity": clientIfReceiverSensitivity,
       "clientIfPowerLevelLowRelativeThreshold": clientIfPowerLevelLowRelativeThreshold,
       "clientIfLossOfSignal": clientIfLossOfSignal,
       "clientIfLossOfFrame": clientIfLossOfFrame,
       "clientIfBitrateMismatch": clientIfBitrateMismatch,
       "clientIfAuAlarmIndicationSignalW2C": clientIfAuAlarmIndicationSignalW2C,
       "clientIfTransmitterFailed": clientIfTransmitterFailed,
       "clientIfTrxCodeMismatch": clientIfTrxCodeMismatch,
       "clientIfTrxBitrateUnavailable": clientIfTrxBitrateUnavailable,
       "clientIfTrxMissing": clientIfTrxMissing,
       "clientIfReceivedPowerHigh": clientIfReceivedPowerHigh,
       "clientIfReceivedPowerLow": clientIfReceivedPowerLow,
       "clientIfLinkDown": clientIfLinkDown,
       "clientIfConfigurationCommand": clientIfConfigurationCommand,
       "clientIfGbeUtilization": clientIfGbeUtilization,
       "clientIfLossOfSync": clientIfLossOfSync,
       "clientIfConfigureTrxModeCommand": clientIfConfigureTrxModeCommand,
       "clientIfTrxMode": clientIfTrxMode,
       "clientIfExpectedTxFrequency": clientIfExpectedTxFrequency,
       "clientIfTxFrequency": clientIfTxFrequency,
       "clientIfUnexpectedTxFrequency": clientIfUnexpectedTxFrequency,
       "clientIfIllegalFrequency": clientIfIllegalFrequency,
       "clientIfLaserForcedOn": clientIfLaserForcedOn,
       "clientIfTrxMedia": clientIfTrxMedia,
       "clientIfTrxMediaMismatch": clientIfTrxMediaMismatch,
       "clientIfTruncAutoNegotiationMode": clientIfTruncAutoNegotiationMode,
       "clientIfObjectProperty": clientIfObjectProperty,
       "clientIfTxPowerLevel": clientIfTxPowerLevel,
       "clientIfLaserTempActual": clientIfLaserTempActual,
       "clientIfTraceIntrusionMode": clientIfTraceIntrusionMode,
       "clientIfTraceTransmitted": clientIfTraceTransmitted,
       "clientIfTraceReceived": clientIfTraceReceived,
       "clientIfTraceExpected": clientIfTraceExpected,
       "clientIfTraceAlarmMode": clientIfTraceAlarmMode,
       "clientIfTraceMismatch": clientIfTraceMismatch,
       "clientIfNearEndLoopback": clientIfNearEndLoopback,
       "clientIfRxSignalStatus": clientIfRxSignalStatus,
       "clientIfMsAlarmIndicationSignalC2W": clientIfMsAlarmIndicationSignalC2W,
       "clientIfMsAlarmIndicationSignalW2C": clientIfMsAlarmIndicationSignalW2C,
       "clientIfRemoteDefectIndication": clientIfRemoteDefectIndication,
       "clientIfJ1TxTrailTrace": clientIfJ1TxTrailTrace,
       "clientIfJ1TxTrailTraceInsertionMode": clientIfJ1TxTrailTraceInsertionMode,
       "clientIfTrxFailed": clientIfTrxFailed,
       "clientIfDisabled": clientIfDisabled,
       "clientIfLoopback": clientIfLoopback,
       "clientIfVcGroupFailedW2C": clientIfVcGroupFailedW2C,
       "clientIfReadJ1": clientIfReadJ1,
       "clientIfClientSignalFailed": clientIfClientSignalFailed,
       "clientIfAuLossOfPointer": clientIfAuLossOfPointer,
       "clientIfGfpLossOfFrame": clientIfGfpLossOfFrame,
       "clientIfHighSpeed": clientIfHighSpeed,
       "clientIfActualFormat": clientIfActualFormat,
       "clientIfRdiIntrusionMode": clientIfRdiIntrusionMode,
       "clientIfMuxQuadVc4": clientIfMuxQuadVc4,
       "clientIfDemuxQuadVc4": clientIfDemuxQuadVc4,
       "clientIfCcConnectionMode": clientIfCcConnectionMode,
       "clientIfCcConfigurationCommand": clientIfCcConfigurationCommand,
       "clientIfIllegalSignalFormat": clientIfIllegalSignalFormat,
       "clientIfSynchProtPortId": clientIfSynchProtPortId,
       "clientIfSynchProtGroupMemberPort": clientIfSynchProtGroupMemberPort,
       "clientIfSynchProtGroupStatus": clientIfSynchProtGroupStatus,
       "clientIfSynchProtActivePort": clientIfSynchProtActivePort,
       "clientIfSynchProtPortStatus": clientIfSynchProtPortStatus,
       "clientIfSynchProtToggleActivePort": clientIfSynchProtToggleActivePort,
       "clientIfNearEndLoopbackTimeout": clientIfNearEndLoopbackTimeout,
       "clientIfNearEndLoopbackEnabled": clientIfNearEndLoopbackEnabled,
       "clientIfChangeNearEndLoopbackCommand": clientIfChangeNearEndLoopbackCommand,
       "clientIfFarEndLoopbackEnabled": clientIfFarEndLoopbackEnabled,
       "clientIfFarEndLoopbackTimeout": clientIfFarEndLoopbackTimeout,
       "clientIfChangeFarEndLoopbackCommand": clientIfChangeFarEndLoopbackCommand,
       "clientIfFormatNotSupportedByHw": clientIfFormatNotSupportedByHw,
       "clientIfLaserMode": clientIfLaserMode,
       "clientIfAlarmIndicationSignalLineC2W": clientIfAlarmIndicationSignalLineC2W,
       "clientIfFarEndClientFailure": clientIfFarEndClientFailure,
       "clientIfOHTransparency": clientIfOHTransparency,
       "clientIfConnectedLine": clientIfConnectedLine,
       "clientIfForwardingErrorCorrectionMode": clientIfForwardingErrorCorrectionMode,
       "clientIfNoFrequencySet": clientIfNoFrequencySet,
       "clientIfJitterAttenuatorBW": clientIfJitterAttenuatorBW,
       "clientIfConnectionStatus": clientIfConnectionStatus,
       "clientIfLoopFilterUnlocked": clientIfLoopFilterUnlocked,
       "clientIfCableLength": clientIfCableLength,
       "clientIfConnectedForeignIndex": clientIfConnectedForeignIndex,
       "clientIfDisconnect": clientIfDisconnect,
       "clientIfOHTransparencyBitMask": clientIfOHTransparencyBitMask,
       "clientIfOHTransparencyString": clientIfOHTransparencyString,
       "clientIfOHTransparencySet": clientIfOHTransparencySet,
       "clientIfAuAlarmIndicationSignalC2W": clientIfAuAlarmIndicationSignalC2W,
       "clientIfAuLossOfPointerC2W": clientIfAuLossOfPointerC2W,
       "clientIfAuLossOfPointerW2C": clientIfAuLossOfPointerW2C,
       "clientIfEthStandbyIndicator": clientIfEthStandbyIndicator,
       "clientIfAuAlarmIndicationSignalW2CSonet": clientIfAuAlarmIndicationSignalW2CSonet,
       "clientIfAuAlarmIndicationSignalC2WSonet": clientIfAuAlarmIndicationSignalC2WSonet,
       "clientIfAuLossOfPointerC2WSonet": clientIfAuLossOfPointerC2WSonet,
       "clientIfAuLossOfPointerW2CSonet": clientIfAuLossOfPointerW2CSonet,
       "clientIfTransceiverNoLoopback": clientIfTransceiverNoLoopback,
       "clientIfFecFailure": clientIfFecFailure,
       "clientIfLaneAlignmentError": clientIfLaneAlignmentError,
       "clientIfFecCorrectedZeros": clientIfFecCorrectedZeros,
       "clientIfFecCorrectedOnes": clientIfFecCorrectedOnes,
       "clientIfSignalDegraded": clientIfSignalDegraded,
       "clientIfFecType": clientIfFecType,
       "clientIfSignalDegradeThreshold": clientIfSignalDegradeThreshold,
       "clientIfExpectedOpticalLayerMapping": clientIfExpectedOpticalLayerMapping,
       "clientIfActualOpticalLayerMapping": clientIfActualOpticalLayerMapping,
       "clientIfConfigurationMismatch": clientIfConfigurationMismatch,
       "clientIfChromaticDispersion": clientIfChromaticDispersion,
       "clientIfDifferentialGroupDelay": clientIfDifferentialGroupDelay,
       "clientIfTxState": clientIfTxState,
       "clientIfRxState": clientIfRxState,
       "clientIfIdx": clientIfIdx,
       "clientIfIfNo": clientIfIfNo,
       "clientIfIdxIf": clientIfIdxIf,
       "clientIfUpPortId": clientIfUpPortId,
       "clientIfNoOfLanes": clientIfNoOfLanes,
       "clientIfFecCorrectedBits": clientIfFecCorrectedBits,
       "clientIfOSNRMargin": clientIfOSNRMargin,
       "clientIfExpectedPhysicalLayerMapping": clientIfExpectedPhysicalLayerMapping,
       "clientIfSignalDirection": clientIfSignalDirection,
       "clientIfAid": clientIfAid,
       "clientIfPhysicalLocation": clientIfPhysicalLocation,
       "clientIfTrxCommunicationFailure": clientIfTrxCommunicationFailure,
       "clientIfTribPortId": clientIfTribPortId,
       "clientIfIfType": clientIfIfType,
       "clientIfConfigurationCommandSNMP": clientIfConfigurationCommandSNMP,
       "clientIfTrxPowerOutOfRange": clientIfTrxPowerOutOfRange,
       "clientVc4List": clientVc4List,
       "clientVc4Table": clientVc4Table,
       "clientVc4Entry": clientVc4Entry,
       "clientVc4Index": clientVc4Index,
       "clientVc4Name": clientVc4Name,
       "clientVc4Descr": clientVc4Descr,
       "clientVc4Subrack": clientVc4Subrack,
       "clientVc4Slot": clientVc4Slot,
       "clientVc4TxPort": clientVc4TxPort,
       "clientVc4RxPort": clientVc4RxPort,
       "clientVc4Vc4": clientVc4Vc4,
       "clientVc4ObjectProperty": clientVc4ObjectProperty,
       "clientVc4AuAlarmIndicationSignal": clientVc4AuAlarmIndicationSignal,
       "clientVc4AuLossOfPointer": clientVc4AuLossOfPointer,
       "clientVc4RxSignalStatus": clientVc4RxSignalStatus,
       "clientVc4ConcatenationStatus": clientVc4ConcatenationStatus,
       "clientVc4PayloadStatus": clientVc4PayloadStatus,
       "clientVc4ConnectionStatus": clientVc4ConnectionStatus,
       "lumentisClientNotifications": lumentisClientNotifications,
       "clientNotifyPrefix": clientNotifyPrefix,
       "clientIfTxSignalStatusDown": clientIfTxSignalStatusDown,
       "clientIfTxSignalStatusUp": clientIfTxSignalStatusUp,
       "clientIfTxSignalStatusDegraded": clientIfTxSignalStatusDegraded,
       "clientLanesList": clientLanesList,
       "clientLanesTable": clientLanesTable,
       "clientLanesEntry": clientLanesEntry,
       "clientLanesIndex": clientLanesIndex,
       "clientLanesName": clientLanesName,
       "clientLanesSubrack": clientLanesSubrack,
       "clientLanesSlot": clientLanesSlot,
       "clientLanesTxPort": clientLanesTxPort,
       "clientLanesRxPort": clientLanesRxPort,
       "clientLanesLaneId": clientLanesLaneId,
       "clientLanesRxPowerLevel": clientLanesRxPowerLevel,
       "clientLanesWaveLength": clientLanesWaveLength,
       "clientLanesBE": clientLanesBE,
       "clientLanesResetBE": clientLanesResetBE,
       "clientLanesLossOfSignal": clientLanesLossOfSignal,
       "clientLanesObjectProperty": clientLanesObjectProperty,
       "clientLanesLossOfSync": clientLanesLossOfSync,
       "clientLanesLocalLinkFault": clientLanesLocalLinkFault,
       "clientLanesRemoteLinkFault": clientLanesRemoteLinkFault,
       "clientLanesHighBitErrorRate": clientLanesHighBitErrorRate,
       "clientLanesReceiverSensitivity": clientLanesReceiverSensitivity,
       "clientLanesReceivedPowerLow": clientLanesReceivedPowerLow,
       "clientLanesIfNo": clientLanesIfNo,
       "clientLanesIdx": clientLanesIdx,
       "clientLanesClientIfIdx": clientLanesClientIfIdx,
       "clientLanesAdminStatus": clientLanesAdminStatus,
       "clientLanesOperStatus": clientLanesOperStatus,
       "clientLanesUpPortId": clientLanesUpPortId,
       "clientMpoLanesList": clientMpoLanesList,
       "clientMpoLanesTable": clientMpoLanesTable,
       "clientMpoLanesEntry": clientMpoLanesEntry,
       "clientMpoLanesIndex": clientMpoLanesIndex,
       "clientMpoLanesName": clientMpoLanesName,
       "clientMpoLanesSubrack": clientMpoLanesSubrack,
       "clientMpoLanesSlot": clientMpoLanesSlot,
       "clientMpoLanesIfNo": clientMpoLanesIfNo,
       "clientMpoLanesLaneId": clientMpoLanesLaneId,
       "clientMpoLanesAdminStatus": clientMpoLanesAdminStatus,
       "clientMpoLanesOperStatus": clientMpoLanesOperStatus,
       "clientMpoLanesLaserStatus": clientMpoLanesLaserStatus,
       "clientMpoLanesRxSensitivity": clientMpoLanesRxSensitivity,
       "clientMpoLanesRxPowerLevel": clientMpoLanesRxPowerLevel,
       "clientMpoLanesPowerLevelLowRelativeThreshold": clientMpoLanesPowerLevelLowRelativeThreshold,
       "clientMpoLanesWaveLength": clientMpoLanesWaveLength,
       "clientMpoLanesObjectProperty": clientMpoLanesObjectProperty,
       "clientMpoLanesForwardAls": clientMpoLanesForwardAls,
       "clientMpoLanesLossOfSignal": clientMpoLanesLossOfSignal,
       "clientMpoLanesRxPowerLow": clientMpoLanesRxPowerLow}
)
