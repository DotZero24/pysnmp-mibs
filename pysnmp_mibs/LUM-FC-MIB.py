# SNMP MIB module (LUM-FC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-FC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:24 2025
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

(lumFcMIB,
 lumModules) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumFcMIB",
    "lumModules")

(BoardOrInterfaceAdminStatus,
 BoardOrInterfaceOperStatus,
 FaultStatus,
 MgmtNameString,
 ObjectProperty,
 PortNumber,
 SlotNumber,
 SubrackNumber) = mibBuilder.importSymbols(
    "LUM-TC",
    "BoardOrInterfaceAdminStatus",
    "BoardOrInterfaceOperStatus",
    "FaultStatus",
    "MgmtNameString",
    "ObjectProperty",
    "PortNumber",
    "SlotNumber",
    "SubrackNumber")

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

lumFcMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 23)
)
if mibBuilder.loadTexts:
    lumFcMIBModule.setRevisions(
        ("2017-06-15 00:00",
         "2016-01-11 00:00",
         "2002-12-06 00:00",
         "2002-11-19 00:00",
         "2002-11-13 00:00",
         "2002-06-25 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FcSignalFormat(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("fc1Gb", 1))
    )



# MIB Managed Objects in the order of their OIDs

_LumFcConfs_ObjectIdentity = ObjectIdentity
lumFcConfs = _LumFcConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22, 1)
)
_LumFcGroups_ObjectIdentity = ObjectIdentity
lumFcGroups = _LumFcGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22, 1, 1)
)
_LumFcCompl_ObjectIdentity = ObjectIdentity
lumFcCompl = _LumFcCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22, 1, 2)
)
_LumFcMIBObjects_ObjectIdentity = ObjectIdentity
lumFcMIBObjects = _LumFcMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22, 2)
)
_FcGeneral_ObjectIdentity = ObjectIdentity
fcGeneral = _FcGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22, 2, 1)
)
_FcGeneralLastChangeTime_Type = DateAndTime
_FcGeneralLastChangeTime_Object = MibScalar
fcGeneralLastChangeTime = _FcGeneralLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22, 2, 1, 1),
    _FcGeneralLastChangeTime_Type()
)
fcGeneralLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcGeneralLastChangeTime.setStatus("current")
_FcGeneralStateLastChangeTime_Type = DateAndTime
_FcGeneralStateLastChangeTime_Object = MibScalar
fcGeneralStateLastChangeTime = _FcGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22, 2, 1, 2),
    _FcGeneralStateLastChangeTime_Type()
)
fcGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcGeneralStateLastChangeTime.setStatus("current")
_FcGeneralFcIfTableSize_Type = Unsigned32
_FcGeneralFcIfTableSize_Object = MibScalar
fcGeneralFcIfTableSize = _FcGeneralFcIfTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22, 2, 1, 3),
    _FcGeneralFcIfTableSize_Type()
)
fcGeneralFcIfTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcGeneralFcIfTableSize.setStatus("current")
_FcIfList_ObjectIdentity = ObjectIdentity
fcIfList = _FcIfList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22, 2, 2)
)
_FcIfTable_Object = MibTable
fcIfTable = _FcIfTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22, 2, 2, 1)
)
if mibBuilder.loadTexts:
    fcIfTable.setStatus("current")
_FcIfEntry_Object = MibTableRow
fcIfEntry = _FcIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22, 2, 2, 1, 1)
)
fcIfEntry.setIndexNames(
    (0, "LUM-FC-MIB", "fcIfIndex"),
)
if mibBuilder.loadTexts:
    fcIfEntry.setStatus("current")


class _FcIfIndex_Type(Unsigned32):
    """Custom type fcIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FcIfIndex_Type.__name__ = "Unsigned32"
_FcIfIndex_Object = MibTableColumn
fcIfIndex = _FcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22, 2, 2, 1, 1, 1),
    _FcIfIndex_Type()
)
fcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfIndex.setStatus("current")
_FcIfName_Type = MgmtNameString
_FcIfName_Object = MibTableColumn
fcIfName = _FcIfName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22, 2, 2, 1, 1, 2),
    _FcIfName_Type()
)
fcIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfName.setStatus("current")


class _FcIfDescr_Type(DisplayString):
    """Custom type fcIfDescr based on DisplayString"""
    defaultValue = OctetString("")


_FcIfDescr_Type.__name__ = "DisplayString"
_FcIfDescr_Object = MibTableColumn
fcIfDescr = _FcIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22, 2, 2, 1, 1, 3),
    _FcIfDescr_Type()
)
fcIfDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcIfDescr.setStatus("current")
_FcIfSubrack_Type = SubrackNumber
_FcIfSubrack_Object = MibTableColumn
fcIfSubrack = _FcIfSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22, 2, 2, 1, 1, 4),
    _FcIfSubrack_Type()
)
fcIfSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfSubrack.setStatus("current")
_FcIfSlot_Type = SlotNumber
_FcIfSlot_Object = MibTableColumn
fcIfSlot = _FcIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22, 2, 2, 1, 1, 5),
    _FcIfSlot_Type()
)
fcIfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfSlot.setStatus("current")
_FcIfTxPort_Type = PortNumber
_FcIfTxPort_Object = MibTableColumn
fcIfTxPort = _FcIfTxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22, 2, 2, 1, 1, 6),
    _FcIfTxPort_Type()
)
fcIfTxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfTxPort.setStatus("current")
_FcIfRxPort_Type = PortNumber
_FcIfRxPort_Object = MibTableColumn
fcIfRxPort = _FcIfRxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22, 2, 2, 1, 1, 7),
    _FcIfRxPort_Type()
)
fcIfRxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfRxPort.setStatus("current")


class _FcIfInvPhysIndexOrZero_Type(Unsigned32):
    """Custom type fcIfInvPhysIndexOrZero based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FcIfInvPhysIndexOrZero_Type.__name__ = "Unsigned32"
_FcIfInvPhysIndexOrZero_Object = MibTableColumn
fcIfInvPhysIndexOrZero = _FcIfInvPhysIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22, 2, 2, 1, 1, 8),
    _FcIfInvPhysIndexOrZero_Type()
)
fcIfInvPhysIndexOrZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfInvPhysIndexOrZero.setStatus("current")


class _FcIfFormat_Type(FcSignalFormat):
    """Custom type fcIfFormat based on FcSignalFormat"""
    defaultValue = 1


_FcIfFormat_Type.__name__ = "FcSignalFormat"
_FcIfFormat_Object = MibTableColumn
fcIfFormat = _FcIfFormat_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22, 2, 2, 1, 1, 9),
    _FcIfFormat_Type()
)
fcIfFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfFormat.setStatus("current")


class _FcIfHighSpeed_Type(Gauge32):
    """Custom type fcIfHighSpeed based on Gauge32"""
    defaultValue = 1000

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 2000),
    )


_FcIfHighSpeed_Type.__name__ = "Gauge32"
_FcIfHighSpeed_Object = MibTableColumn
fcIfHighSpeed = _FcIfHighSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22, 2, 2, 1, 1, 10),
    _FcIfHighSpeed_Type()
)
fcIfHighSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfHighSpeed.setStatus("current")


class _FcIfAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type fcIfAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 3


_FcIfAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_FcIfAdminStatus_Object = MibTableColumn
fcIfAdminStatus = _FcIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22, 2, 2, 1, 1, 11),
    _FcIfAdminStatus_Type()
)
fcIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcIfAdminStatus.setStatus("current")


class _FcIfOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type fcIfOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 1


_FcIfOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_FcIfOperStatus_Object = MibTableColumn
fcIfOperStatus = _FcIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22, 2, 2, 1, 1, 12),
    _FcIfOperStatus_Type()
)
fcIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfOperStatus.setStatus("current")


class _FcIfLaserStatus_Type(Integer32):
    """Custom type fcIfLaserStatus based on Integer32"""
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


_FcIfLaserStatus_Type.__name__ = "Integer32"
_FcIfLaserStatus_Object = MibTableColumn
fcIfLaserStatus = _FcIfLaserStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22, 2, 2, 1, 1, 13),
    _FcIfLaserStatus_Type()
)
fcIfLaserStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfLaserStatus.setStatus("current")


class _FcIfTxSignalStatus_Type(Integer32):
    """Custom type fcIfTxSignalStatus based on Integer32"""
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


_FcIfTxSignalStatus_Type.__name__ = "Integer32"
_FcIfTxSignalStatus_Object = MibTableColumn
fcIfTxSignalStatus = _FcIfTxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22, 2, 2, 1, 1, 14),
    _FcIfTxSignalStatus_Type()
)
fcIfTxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfTxSignalStatus.setStatus("current")
_FcIfLossOfSignal_Type = FaultStatus
_FcIfLossOfSignal_Object = MibTableColumn
fcIfLossOfSignal = _FcIfLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22, 2, 2, 1, 1, 15),
    _FcIfLossOfSignal_Type()
)
fcIfLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfLossOfSignal.setStatus("current")
_FcIfLossOfSync_Type = FaultStatus
_FcIfLossOfSync_Object = MibTableColumn
fcIfLossOfSync = _FcIfLossOfSync_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22, 2, 2, 1, 1, 16),
    _FcIfLossOfSync_Type()
)
fcIfLossOfSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfLossOfSync.setStatus("current")
_FcIfAuAlarmIndicationSignalW2C_Type = FaultStatus
_FcIfAuAlarmIndicationSignalW2C_Object = MibTableColumn
fcIfAuAlarmIndicationSignalW2C = _FcIfAuAlarmIndicationSignalW2C_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22, 2, 2, 1, 1, 17),
    _FcIfAuAlarmIndicationSignalW2C_Type()
)
fcIfAuAlarmIndicationSignalW2C.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfAuAlarmIndicationSignalW2C.setStatus("current")


class _FcIfForwardAls_Type(Integer32):
    """Custom type fcIfForwardAls based on Integer32"""
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


_FcIfForwardAls_Type.__name__ = "Integer32"
_FcIfForwardAls_Object = MibTableColumn
fcIfForwardAls = _FcIfForwardAls_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22, 2, 2, 1, 1, 18),
    _FcIfForwardAls_Type()
)
fcIfForwardAls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcIfForwardAls.setStatus("current")


class _FcIfSuppressRemoteAlarms_Type(Integer32):
    """Custom type fcIfSuppressRemoteAlarms based on Integer32"""
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


_FcIfSuppressRemoteAlarms_Type.__name__ = "Integer32"
_FcIfSuppressRemoteAlarms_Object = MibTableColumn
fcIfSuppressRemoteAlarms = _FcIfSuppressRemoteAlarms_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22, 2, 2, 1, 1, 19),
    _FcIfSuppressRemoteAlarms_Type()
)
fcIfSuppressRemoteAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcIfSuppressRemoteAlarms.setStatus("current")


class _FcIfFarEndLoopback_Type(Integer32):
    """Custom type fcIfFarEndLoopback based on Integer32"""
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


_FcIfFarEndLoopback_Type.__name__ = "Integer32"
_FcIfFarEndLoopback_Object = MibTableColumn
fcIfFarEndLoopback = _FcIfFarEndLoopback_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22, 2, 2, 1, 1, 20),
    _FcIfFarEndLoopback_Type()
)
fcIfFarEndLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcIfFarEndLoopback.setStatus("current")


class _FcIfEntityId_Type(Unsigned32):
    """Custom type fcIfEntityId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FcIfEntityId_Type.__name__ = "Unsigned32"
_FcIfEntityId_Object = MibTableColumn
fcIfEntityId = _FcIfEntityId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22, 2, 2, 1, 1, 21),
    _FcIfEntityId_Type()
)
fcIfEntityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfEntityId.setStatus("current")
_FcIfObjectProperty_Type = ObjectProperty
_FcIfObjectProperty_Object = MibTableColumn
fcIfObjectProperty = _FcIfObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22, 2, 2, 1, 1, 22),
    _FcIfObjectProperty_Type()
)
fcIfObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcIfObjectProperty.setStatus("current")
_LumentisFcNotifications_ObjectIdentity = ObjectIdentity
lumentisFcNotifications = _LumentisFcNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22, 2, 3)
)
_FcNotifyPrefix_ObjectIdentity = ObjectIdentity
fcNotifyPrefix = _FcNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22, 2, 3, 0)
)

# Managed Objects groups

fcGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22, 1, 1, 1)
)
fcGeneralGroup.setObjects(
      *(("LUM-FC-MIB", "fcGeneralLastChangeTime"),
        ("LUM-FC-MIB", "fcGeneralStateLastChangeTime"))
)
if mibBuilder.loadTexts:
    fcGeneralGroup.setStatus("deprecated")

fcIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22, 1, 1, 2)
)
fcIfGroup.setObjects(
      *(("LUM-FC-MIB", "fcIfIndex"),
        ("LUM-FC-MIB", "fcIfName"),
        ("LUM-FC-MIB", "fcIfDescr"),
        ("LUM-FC-MIB", "fcIfSubrack"),
        ("LUM-FC-MIB", "fcIfSlot"),
        ("LUM-FC-MIB", "fcIfTxPort"),
        ("LUM-FC-MIB", "fcIfRxPort"),
        ("LUM-FC-MIB", "fcIfInvPhysIndexOrZero"),
        ("LUM-FC-MIB", "fcIfFormat"),
        ("LUM-FC-MIB", "fcIfHighSpeed"),
        ("LUM-FC-MIB", "fcIfLaserStatus"),
        ("LUM-FC-MIB", "fcIfAdminStatus"),
        ("LUM-FC-MIB", "fcIfOperStatus"),
        ("LUM-FC-MIB", "fcIfTxSignalStatus"),
        ("LUM-FC-MIB", "fcIfLossOfSignal"),
        ("LUM-FC-MIB", "fcIfLossOfSync"),
        ("LUM-FC-MIB", "fcIfAuAlarmIndicationSignalW2C"),
        ("LUM-FC-MIB", "fcIfForwardAls"),
        ("LUM-FC-MIB", "fcIfSuppressRemoteAlarms"),
        ("LUM-FC-MIB", "fcIfFarEndLoopback"))
)
if mibBuilder.loadTexts:
    fcIfGroup.setStatus("deprecated")

fcGeneralGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22, 1, 1, 4)
)
fcGeneralGroupV2.setObjects(
      *(("LUM-FC-MIB", "fcGeneralLastChangeTime"),
        ("LUM-FC-MIB", "fcGeneralStateLastChangeTime"),
        ("LUM-FC-MIB", "fcGeneralFcIfTableSize"))
)
if mibBuilder.loadTexts:
    fcGeneralGroupV2.setStatus("current")

fcIfGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22, 1, 1, 5)
)
fcIfGroupV2.setObjects(
      *(("LUM-FC-MIB", "fcIfIndex"),
        ("LUM-FC-MIB", "fcIfName"),
        ("LUM-FC-MIB", "fcIfDescr"),
        ("LUM-FC-MIB", "fcIfSubrack"),
        ("LUM-FC-MIB", "fcIfSlot"),
        ("LUM-FC-MIB", "fcIfTxPort"),
        ("LUM-FC-MIB", "fcIfRxPort"),
        ("LUM-FC-MIB", "fcIfInvPhysIndexOrZero"),
        ("LUM-FC-MIB", "fcIfFormat"),
        ("LUM-FC-MIB", "fcIfHighSpeed"),
        ("LUM-FC-MIB", "fcIfLaserStatus"),
        ("LUM-FC-MIB", "fcIfAdminStatus"),
        ("LUM-FC-MIB", "fcIfOperStatus"),
        ("LUM-FC-MIB", "fcIfTxSignalStatus"),
        ("LUM-FC-MIB", "fcIfLossOfSignal"),
        ("LUM-FC-MIB", "fcIfLossOfSync"),
        ("LUM-FC-MIB", "fcIfAuAlarmIndicationSignalW2C"),
        ("LUM-FC-MIB", "fcIfForwardAls"),
        ("LUM-FC-MIB", "fcIfSuppressRemoteAlarms"),
        ("LUM-FC-MIB", "fcIfFarEndLoopback"),
        ("LUM-FC-MIB", "fcIfEntityId"),
        ("LUM-FC-MIB", "fcIfObjectProperty"))
)
if mibBuilder.loadTexts:
    fcIfGroupV2.setStatus("current")


# Notification objects

fcIfTxSignalStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22, 2, 3, 0, 1)
)
fcIfTxSignalStatusDown.setObjects(
      *(("LUM-FC-MIB", "fcIfIndex"),
        ("LUM-FC-MIB", "fcIfName"),
        ("LUM-FC-MIB", "fcIfSubrack"),
        ("LUM-FC-MIB", "fcIfSlot"),
        ("LUM-FC-MIB", "fcIfTxPort"),
        ("LUM-FC-MIB", "fcIfRxPort"),
        ("LUM-FC-MIB", "fcIfEntityId"),
        ("LUM-FC-MIB", "fcIfTxSignalStatus"))
)
if mibBuilder.loadTexts:
    fcIfTxSignalStatusDown.setStatus(
        "current"
    )

fcIfTxSignalStatusUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22, 2, 3, 0, 2)
)
fcIfTxSignalStatusUp.setObjects(
      *(("LUM-FC-MIB", "fcIfIndex"),
        ("LUM-FC-MIB", "fcIfName"),
        ("LUM-FC-MIB", "fcIfSubrack"),
        ("LUM-FC-MIB", "fcIfSlot"),
        ("LUM-FC-MIB", "fcIfTxPort"),
        ("LUM-FC-MIB", "fcIfRxPort"),
        ("LUM-FC-MIB", "fcIfEntityId"),
        ("LUM-FC-MIB", "fcIfTxSignalStatus"))
)
if mibBuilder.loadTexts:
    fcIfTxSignalStatusUp.setStatus(
        "current"
    )

fcIfTxSignalStatusDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22, 2, 3, 0, 3)
)
fcIfTxSignalStatusDegraded.setObjects(
      *(("LUM-FC-MIB", "fcIfIndex"),
        ("LUM-FC-MIB", "fcIfName"),
        ("LUM-FC-MIB", "fcIfSubrack"),
        ("LUM-FC-MIB", "fcIfSlot"),
        ("LUM-FC-MIB", "fcIfTxPort"),
        ("LUM-FC-MIB", "fcIfRxPort"),
        ("LUM-FC-MIB", "fcIfEntityId"),
        ("LUM-FC-MIB", "fcIfTxSignalStatus"))
)
if mibBuilder.loadTexts:
    fcIfTxSignalStatusDegraded.setStatus(
        "current"
    )


# Notifications groups

fcNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22, 1, 1, 3)
)
fcNotificationGroup.setObjects(
      *(("LUM-FC-MIB", "fcIfTxSignalStatusDown"),
        ("LUM-FC-MIB", "fcIfTxSignalStatusUp"),
        ("LUM-FC-MIB", "fcIfTxSignalStatusDegraded"))
)
if mibBuilder.loadTexts:
    fcNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

lumFcBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22, 1, 2, 1)
)
lumFcBasicComplV1.setObjects(
      *(("LUM-FC-MIB", "fcGeneralGroup"),
        ("LUM-FC-MIB", "fcIfGroup"),
        ("LUM-FC-MIB", "fcNotificationGroup"))
)
if mibBuilder.loadTexts:
    lumFcBasicComplV1.setStatus(
        "deprecated"
    )

lumFcBasicComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22, 1, 2, 2)
)
lumFcBasicComplV2.setObjects(
      *(("LUM-FC-MIB", "fcGeneralGroupV2"),
        ("LUM-FC-MIB", "fcIfGroup"),
        ("LUM-FC-MIB", "fcNotificationGroup"))
)
if mibBuilder.loadTexts:
    lumFcBasicComplV2.setStatus(
        "deprecated"
    )

lumFcBasicComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 22, 1, 2, 3)
)
lumFcBasicComplV3.setObjects(
      *(("LUM-FC-MIB", "fcGeneralGroupV2"),
        ("LUM-FC-MIB", "fcIfGroupV2"),
        ("LUM-FC-MIB", "fcNotificationGroup"))
)
if mibBuilder.loadTexts:
    lumFcBasicComplV3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-FC-MIB",
    **{"FcSignalFormat": FcSignalFormat,
       "lumFcMIBModule": lumFcMIBModule,
       "lumFcConfs": lumFcConfs,
       "lumFcGroups": lumFcGroups,
       "fcGeneralGroup": fcGeneralGroup,
       "fcIfGroup": fcIfGroup,
       "fcNotificationGroup": fcNotificationGroup,
       "fcGeneralGroupV2": fcGeneralGroupV2,
       "fcIfGroupV2": fcIfGroupV2,
       "lumFcCompl": lumFcCompl,
       "lumFcBasicComplV1": lumFcBasicComplV1,
       "lumFcBasicComplV2": lumFcBasicComplV2,
       "lumFcBasicComplV3": lumFcBasicComplV3,
       "lumFcMIBObjects": lumFcMIBObjects,
       "fcGeneral": fcGeneral,
       "fcGeneralLastChangeTime": fcGeneralLastChangeTime,
       "fcGeneralStateLastChangeTime": fcGeneralStateLastChangeTime,
       "fcGeneralFcIfTableSize": fcGeneralFcIfTableSize,
       "fcIfList": fcIfList,
       "fcIfTable": fcIfTable,
       "fcIfEntry": fcIfEntry,
       "fcIfIndex": fcIfIndex,
       "fcIfName": fcIfName,
       "fcIfDescr": fcIfDescr,
       "fcIfSubrack": fcIfSubrack,
       "fcIfSlot": fcIfSlot,
       "fcIfTxPort": fcIfTxPort,
       "fcIfRxPort": fcIfRxPort,
       "fcIfInvPhysIndexOrZero": fcIfInvPhysIndexOrZero,
       "fcIfFormat": fcIfFormat,
       "fcIfHighSpeed": fcIfHighSpeed,
       "fcIfAdminStatus": fcIfAdminStatus,
       "fcIfOperStatus": fcIfOperStatus,
       "fcIfLaserStatus": fcIfLaserStatus,
       "fcIfTxSignalStatus": fcIfTxSignalStatus,
       "fcIfLossOfSignal": fcIfLossOfSignal,
       "fcIfLossOfSync": fcIfLossOfSync,
       "fcIfAuAlarmIndicationSignalW2C": fcIfAuAlarmIndicationSignalW2C,
       "fcIfForwardAls": fcIfForwardAls,
       "fcIfSuppressRemoteAlarms": fcIfSuppressRemoteAlarms,
       "fcIfFarEndLoopback": fcIfFarEndLoopback,
       "fcIfEntityId": fcIfEntityId,
       "fcIfObjectProperty": fcIfObjectProperty,
       "lumentisFcNotifications": lumentisFcNotifications,
       "fcNotifyPrefix": fcNotifyPrefix,
       "fcIfTxSignalStatusDown": fcIfTxSignalStatusDown,
       "fcIfTxSignalStatusUp": fcIfTxSignalStatusUp,
       "fcIfTxSignalStatusDegraded": fcIfTxSignalStatusDegraded}
)
