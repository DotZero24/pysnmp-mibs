# SNMP MIB module (LUM-OTN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-OTN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:03 2025
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
 lumOtnMIB) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumModules",
    "lumOtnMIB")

(BoardOrInterfaceAdminStatus,
 BoardOrInterfaceOperStatus,
 CommandString,
 FaultStatus,
 MgmtNameString,
 ObjectProperty,
 OtnMonitorConfig,
 OtnMonitorType,
 OtnTIMDetMode,
 PortNumber,
 SlotNumber,
 SubrackNumber) = mibBuilder.importSymbols(
    "LUM-TC",
    "BoardOrInterfaceAdminStatus",
    "BoardOrInterfaceOperStatus",
    "CommandString",
    "FaultStatus",
    "MgmtNameString",
    "ObjectProperty",
    "OtnMonitorConfig",
    "OtnMonitorType",
    "OtnTIMDetMode",
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
 TextualConvention,
 TestAndIncr) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TestAndIncr")


# MODULE-IDENTITY

lumOtnMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 34)
)
if mibBuilder.loadTexts:
    lumOtnMIBModule.setRevisions(
        ("2017-06-15 00:00",
         "2016-01-11 00:00",
         "2012-03-30 00:00",
         "2009-06-15 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LumOtnConfs_ObjectIdentity = ObjectIdentity
lumOtnConfs = _LumOtnConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 1)
)
_LumOtnGroups_ObjectIdentity = ObjectIdentity
lumOtnGroups = _LumOtnGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 1, 1)
)
_LumOtnCompl_ObjectIdentity = ObjectIdentity
lumOtnCompl = _LumOtnCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 1, 2)
)
_LumOtnMinimalGroups_ObjectIdentity = ObjectIdentity
lumOtnMinimalGroups = _LumOtnMinimalGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 1, 3)
)
_LumOtnMinimalCompl_ObjectIdentity = ObjectIdentity
lumOtnMinimalCompl = _LumOtnMinimalCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 1, 4)
)
_LumOtnMIBObjects_ObjectIdentity = ObjectIdentity
lumOtnMIBObjects = _LumOtnMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 2)
)
_OtnGeneral_ObjectIdentity = ObjectIdentity
otnGeneral = _OtnGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 2, 1)
)
_OtnGeneralTestAndIncr_Type = TestAndIncr
_OtnGeneralTestAndIncr_Object = MibScalar
otnGeneralTestAndIncr = _OtnGeneralTestAndIncr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 2, 1, 1),
    _OtnGeneralTestAndIncr_Type()
)
otnGeneralTestAndIncr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otnGeneralTestAndIncr.setStatus("current")


class _OtnGeneralMibSpecVersion_Type(DisplayString):
    """Custom type otnGeneralMibSpecVersion based on DisplayString"""
    defaultValue = OctetString("")


_OtnGeneralMibSpecVersion_Type.__name__ = "DisplayString"
_OtnGeneralMibSpecVersion_Object = MibScalar
otnGeneralMibSpecVersion = _OtnGeneralMibSpecVersion_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 2, 1, 2),
    _OtnGeneralMibSpecVersion_Type()
)
otnGeneralMibSpecVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otnGeneralMibSpecVersion.setStatus("current")


class _OtnGeneralMibImplVersion_Type(DisplayString):
    """Custom type otnGeneralMibImplVersion based on DisplayString"""
    defaultValue = OctetString("")


_OtnGeneralMibImplVersion_Type.__name__ = "DisplayString"
_OtnGeneralMibImplVersion_Object = MibScalar
otnGeneralMibImplVersion = _OtnGeneralMibImplVersion_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 2, 1, 3),
    _OtnGeneralMibImplVersion_Type()
)
otnGeneralMibImplVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otnGeneralMibImplVersion.setStatus("current")
_OtnGeneralLastChangeTime_Type = DateAndTime
_OtnGeneralLastChangeTime_Object = MibScalar
otnGeneralLastChangeTime = _OtnGeneralLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 2, 1, 4),
    _OtnGeneralLastChangeTime_Type()
)
otnGeneralLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otnGeneralLastChangeTime.setStatus("current")
_OtnGeneralStateLastChangeTime_Type = DateAndTime
_OtnGeneralStateLastChangeTime_Object = MibScalar
otnGeneralStateLastChangeTime = _OtnGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 2, 1, 5),
    _OtnGeneralStateLastChangeTime_Type()
)
otnGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otnGeneralStateLastChangeTime.setStatus("current")
_OtnGeneralSmTcmPmTableSize_Type = Unsigned32
_OtnGeneralSmTcmPmTableSize_Object = MibScalar
otnGeneralSmTcmPmTableSize = _OtnGeneralSmTcmPmTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 2, 1, 6),
    _OtnGeneralSmTcmPmTableSize_Type()
)
otnGeneralSmTcmPmTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otnGeneralSmTcmPmTableSize.setStatus("current")
_OtnSmTcmPmList_ObjectIdentity = ObjectIdentity
otnSmTcmPmList = _OtnSmTcmPmList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 2, 2)
)
_OtnSmTcmPmTable_Object = MibTable
otnSmTcmPmTable = _OtnSmTcmPmTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 2, 2, 1)
)
if mibBuilder.loadTexts:
    otnSmTcmPmTable.setStatus("current")
_OtnSmTcmPmEntry_Object = MibTableRow
otnSmTcmPmEntry = _OtnSmTcmPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 2, 2, 1, 1)
)
otnSmTcmPmEntry.setIndexNames(
    (0, "LUM-OTN-MIB", "otnSmTcmPmIndex"),
)
if mibBuilder.loadTexts:
    otnSmTcmPmEntry.setStatus("current")


class _OtnSmTcmPmIndex_Type(Unsigned32):
    """Custom type otnSmTcmPmIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OtnSmTcmPmIndex_Type.__name__ = "Unsigned32"
_OtnSmTcmPmIndex_Object = MibTableColumn
otnSmTcmPmIndex = _OtnSmTcmPmIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 2, 2, 1, 1, 1),
    _OtnSmTcmPmIndex_Type()
)
otnSmTcmPmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otnSmTcmPmIndex.setStatus("current")


class _OtnSmTcmPmName_Type(MgmtNameString):
    """Custom type otnSmTcmPmName based on MgmtNameString"""
    defaultValue = OctetString("")


_OtnSmTcmPmName_Type.__name__ = "MgmtNameString"
_OtnSmTcmPmName_Object = MibTableColumn
otnSmTcmPmName = _OtnSmTcmPmName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 2, 2, 1, 1, 2),
    _OtnSmTcmPmName_Type()
)
otnSmTcmPmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otnSmTcmPmName.setStatus("current")
_OtnSmTcmPmType_Type = OtnMonitorType
_OtnSmTcmPmType_Object = MibTableColumn
otnSmTcmPmType = _OtnSmTcmPmType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 2, 2, 1, 1, 3),
    _OtnSmTcmPmType_Type()
)
otnSmTcmPmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otnSmTcmPmType.setStatus("current")


class _OtnSmTcmPmMonitorConfig_Type(OtnMonitorConfig):
    """Custom type otnSmTcmPmMonitorConfig based on OtnMonitorConfig"""
    defaultValue = 1


_OtnSmTcmPmMonitorConfig_Type.__name__ = "OtnMonitorConfig"
_OtnSmTcmPmMonitorConfig_Object = MibTableColumn
otnSmTcmPmMonitorConfig = _OtnSmTcmPmMonitorConfig_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 2, 2, 1, 1, 4),
    _OtnSmTcmPmMonitorConfig_Type()
)
otnSmTcmPmMonitorConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otnSmTcmPmMonitorConfig.setStatus("current")


class _OtnSmTcmPmTerminatedTcm_Type(Integer32):
    """Custom type otnSmTcmPmTerminatedTcm based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("tcm1", 1),
          ("tcm2", 2),
          ("tcm3", 3),
          ("tcm4", 4),
          ("tcm5", 5),
          ("tcm6", 6))
    )


_OtnSmTcmPmTerminatedTcm_Type.__name__ = "Integer32"
_OtnSmTcmPmTerminatedTcm_Object = MibTableColumn
otnSmTcmPmTerminatedTcm = _OtnSmTcmPmTerminatedTcm_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 2, 2, 1, 1, 5),
    _OtnSmTcmPmTerminatedTcm_Type()
)
otnSmTcmPmTerminatedTcm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    otnSmTcmPmTerminatedTcm.setStatus("current")


class _OtnSmTcmPmDescr_Type(DisplayString):
    """Custom type otnSmTcmPmDescr based on DisplayString"""
    defaultValue = OctetString("")


_OtnSmTcmPmDescr_Type.__name__ = "DisplayString"
_OtnSmTcmPmDescr_Object = MibTableColumn
otnSmTcmPmDescr = _OtnSmTcmPmDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 2, 2, 1, 1, 6),
    _OtnSmTcmPmDescr_Type()
)
otnSmTcmPmDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otnSmTcmPmDescr.setStatus("current")


class _OtnSmTcmPmSubrack_Type(SubrackNumber):
    """Custom type otnSmTcmPmSubrack based on SubrackNumber"""
    defaultValue = 0


_OtnSmTcmPmSubrack_Type.__name__ = "SubrackNumber"
_OtnSmTcmPmSubrack_Object = MibTableColumn
otnSmTcmPmSubrack = _OtnSmTcmPmSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 2, 2, 1, 1, 7),
    _OtnSmTcmPmSubrack_Type()
)
otnSmTcmPmSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otnSmTcmPmSubrack.setStatus("current")


class _OtnSmTcmPmSlot_Type(SlotNumber):
    """Custom type otnSmTcmPmSlot based on SlotNumber"""
    defaultValue = 0


_OtnSmTcmPmSlot_Type.__name__ = "SlotNumber"
_OtnSmTcmPmSlot_Object = MibTableColumn
otnSmTcmPmSlot = _OtnSmTcmPmSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 2, 2, 1, 1, 8),
    _OtnSmTcmPmSlot_Type()
)
otnSmTcmPmSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otnSmTcmPmSlot.setStatus("current")


class _OtnSmTcmPmTxPort_Type(PortNumber):
    """Custom type otnSmTcmPmTxPort based on PortNumber"""
    defaultValue = 0


_OtnSmTcmPmTxPort_Type.__name__ = "PortNumber"
_OtnSmTcmPmTxPort_Object = MibTableColumn
otnSmTcmPmTxPort = _OtnSmTcmPmTxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 2, 2, 1, 1, 9),
    _OtnSmTcmPmTxPort_Type()
)
otnSmTcmPmTxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otnSmTcmPmTxPort.setStatus("current")


class _OtnSmTcmPmAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type otnSmTcmPmAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 3


_OtnSmTcmPmAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_OtnSmTcmPmAdminStatus_Object = MibTableColumn
otnSmTcmPmAdminStatus = _OtnSmTcmPmAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 2, 2, 1, 1, 10),
    _OtnSmTcmPmAdminStatus_Type()
)
otnSmTcmPmAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otnSmTcmPmAdminStatus.setStatus("current")


class _OtnSmTcmPmOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type otnSmTcmPmOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 1


_OtnSmTcmPmOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_OtnSmTcmPmOperStatus_Object = MibTableColumn
otnSmTcmPmOperStatus = _OtnSmTcmPmOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 2, 2, 1, 1, 11),
    _OtnSmTcmPmOperStatus_Type()
)
otnSmTcmPmOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otnSmTcmPmOperStatus.setStatus("current")


class _OtnSmTcmPmSapiTraceTransmitted_Type(DisplayString):
    """Custom type otnSmTcmPmSapiTraceTransmitted based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_OtnSmTcmPmSapiTraceTransmitted_Type.__name__ = "DisplayString"
_OtnSmTcmPmSapiTraceTransmitted_Object = MibTableColumn
otnSmTcmPmSapiTraceTransmitted = _OtnSmTcmPmSapiTraceTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 2, 2, 1, 1, 12),
    _OtnSmTcmPmSapiTraceTransmitted_Type()
)
otnSmTcmPmSapiTraceTransmitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otnSmTcmPmSapiTraceTransmitted.setStatus("current")


class _OtnSmTcmPmSapiTraceReceivedByte0_Type(Unsigned32):
    """Custom type otnSmTcmPmSapiTraceReceivedByte0 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OtnSmTcmPmSapiTraceReceivedByte0_Type.__name__ = "Unsigned32"
_OtnSmTcmPmSapiTraceReceivedByte0_Object = MibTableColumn
otnSmTcmPmSapiTraceReceivedByte0 = _OtnSmTcmPmSapiTraceReceivedByte0_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 2, 2, 1, 1, 13),
    _OtnSmTcmPmSapiTraceReceivedByte0_Type()
)
otnSmTcmPmSapiTraceReceivedByte0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otnSmTcmPmSapiTraceReceivedByte0.setStatus("current")


class _OtnSmTcmPmSapiTraceReceived_Type(DisplayString):
    """Custom type otnSmTcmPmSapiTraceReceived based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_OtnSmTcmPmSapiTraceReceived_Type.__name__ = "DisplayString"
_OtnSmTcmPmSapiTraceReceived_Object = MibTableColumn
otnSmTcmPmSapiTraceReceived = _OtnSmTcmPmSapiTraceReceived_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 2, 2, 1, 1, 14),
    _OtnSmTcmPmSapiTraceReceived_Type()
)
otnSmTcmPmSapiTraceReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otnSmTcmPmSapiTraceReceived.setStatus("current")


class _OtnSmTcmPmSapiTraceExpected_Type(DisplayString):
    """Custom type otnSmTcmPmSapiTraceExpected based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_OtnSmTcmPmSapiTraceExpected_Type.__name__ = "DisplayString"
_OtnSmTcmPmSapiTraceExpected_Object = MibTableColumn
otnSmTcmPmSapiTraceExpected = _OtnSmTcmPmSapiTraceExpected_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 2, 2, 1, 1, 15),
    _OtnSmTcmPmSapiTraceExpected_Type()
)
otnSmTcmPmSapiTraceExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otnSmTcmPmSapiTraceExpected.setStatus("current")


class _OtnSmTcmPmDapiTraceTransmitted_Type(DisplayString):
    """Custom type otnSmTcmPmDapiTraceTransmitted based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_OtnSmTcmPmDapiTraceTransmitted_Type.__name__ = "DisplayString"
_OtnSmTcmPmDapiTraceTransmitted_Object = MibTableColumn
otnSmTcmPmDapiTraceTransmitted = _OtnSmTcmPmDapiTraceTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 2, 2, 1, 1, 16),
    _OtnSmTcmPmDapiTraceTransmitted_Type()
)
otnSmTcmPmDapiTraceTransmitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otnSmTcmPmDapiTraceTransmitted.setStatus("current")


class _OtnSmTcmPmDapiTraceReceivedByte0_Type(Unsigned32):
    """Custom type otnSmTcmPmDapiTraceReceivedByte0 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OtnSmTcmPmDapiTraceReceivedByte0_Type.__name__ = "Unsigned32"
_OtnSmTcmPmDapiTraceReceivedByte0_Object = MibTableColumn
otnSmTcmPmDapiTraceReceivedByte0 = _OtnSmTcmPmDapiTraceReceivedByte0_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 2, 2, 1, 1, 17),
    _OtnSmTcmPmDapiTraceReceivedByte0_Type()
)
otnSmTcmPmDapiTraceReceivedByte0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otnSmTcmPmDapiTraceReceivedByte0.setStatus("current")


class _OtnSmTcmPmDapiTraceReceived_Type(DisplayString):
    """Custom type otnSmTcmPmDapiTraceReceived based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_OtnSmTcmPmDapiTraceReceived_Type.__name__ = "DisplayString"
_OtnSmTcmPmDapiTraceReceived_Object = MibTableColumn
otnSmTcmPmDapiTraceReceived = _OtnSmTcmPmDapiTraceReceived_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 2, 2, 1, 1, 18),
    _OtnSmTcmPmDapiTraceReceived_Type()
)
otnSmTcmPmDapiTraceReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otnSmTcmPmDapiTraceReceived.setStatus("current")


class _OtnSmTcmPmDapiTraceExpected_Type(DisplayString):
    """Custom type otnSmTcmPmDapiTraceExpected based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_OtnSmTcmPmDapiTraceExpected_Type.__name__ = "DisplayString"
_OtnSmTcmPmDapiTraceExpected_Object = MibTableColumn
otnSmTcmPmDapiTraceExpected = _OtnSmTcmPmDapiTraceExpected_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 2, 2, 1, 1, 19),
    _OtnSmTcmPmDapiTraceExpected_Type()
)
otnSmTcmPmDapiTraceExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otnSmTcmPmDapiTraceExpected.setStatus("current")


class _OtnSmTcmPmOpSpecificTraceTransmitted_Type(DisplayString):
    """Custom type otnSmTcmPmOpSpecificTraceTransmitted based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_OtnSmTcmPmOpSpecificTraceTransmitted_Type.__name__ = "DisplayString"
_OtnSmTcmPmOpSpecificTraceTransmitted_Object = MibTableColumn
otnSmTcmPmOpSpecificTraceTransmitted = _OtnSmTcmPmOpSpecificTraceTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 2, 2, 1, 1, 20),
    _OtnSmTcmPmOpSpecificTraceTransmitted_Type()
)
otnSmTcmPmOpSpecificTraceTransmitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otnSmTcmPmOpSpecificTraceTransmitted.setStatus("current")


class _OtnSmTcmPmOpSpecificTraceReceived_Type(DisplayString):
    """Custom type otnSmTcmPmOpSpecificTraceReceived based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_OtnSmTcmPmOpSpecificTraceReceived_Type.__name__ = "DisplayString"
_OtnSmTcmPmOpSpecificTraceReceived_Object = MibTableColumn
otnSmTcmPmOpSpecificTraceReceived = _OtnSmTcmPmOpSpecificTraceReceived_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 2, 2, 1, 1, 21),
    _OtnSmTcmPmOpSpecificTraceReceived_Type()
)
otnSmTcmPmOpSpecificTraceReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otnSmTcmPmOpSpecificTraceReceived.setStatus("current")


class _OtnSmTcmPmTraceIdMMDetectionMode_Type(OtnTIMDetMode):
    """Custom type otnSmTcmPmTraceIdMMDetectionMode based on OtnTIMDetMode"""
    defaultValue = 0


_OtnSmTcmPmTraceIdMMDetectionMode_Type.__name__ = "OtnTIMDetMode"
_OtnSmTcmPmTraceIdMMDetectionMode_Object = MibTableColumn
otnSmTcmPmTraceIdMMDetectionMode = _OtnSmTcmPmTraceIdMMDetectionMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 2, 2, 1, 1, 22),
    _OtnSmTcmPmTraceIdMMDetectionMode_Type()
)
otnSmTcmPmTraceIdMMDetectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otnSmTcmPmTraceIdMMDetectionMode.setStatus("current")


class _OtnSmTcmPmTraceAlarmMode_Type(Integer32):
    """Custom type otnSmTcmPmTraceAlarmMode based on Integer32"""
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


_OtnSmTcmPmTraceAlarmMode_Type.__name__ = "Integer32"
_OtnSmTcmPmTraceAlarmMode_Object = MibTableColumn
otnSmTcmPmTraceAlarmMode = _OtnSmTcmPmTraceAlarmMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 2, 2, 1, 1, 23),
    _OtnSmTcmPmTraceAlarmMode_Type()
)
otnSmTcmPmTraceAlarmMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otnSmTcmPmTraceAlarmMode.setStatus("current")
_OtnSmTcmPmObjectProperty_Type = ObjectProperty
_OtnSmTcmPmObjectProperty_Object = MibTableColumn
otnSmTcmPmObjectProperty = _OtnSmTcmPmObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 2, 2, 1, 1, 24),
    _OtnSmTcmPmObjectProperty_Type()
)
otnSmTcmPmObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otnSmTcmPmObjectProperty.setStatus("current")
_OtnSmTcmPmTraceMismatch_Type = FaultStatus
_OtnSmTcmPmTraceMismatch_Object = MibTableColumn
otnSmTcmPmTraceMismatch = _OtnSmTcmPmTraceMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 2, 2, 1, 1, 25),
    _OtnSmTcmPmTraceMismatch_Type()
)
otnSmTcmPmTraceMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otnSmTcmPmTraceMismatch.setStatus("current")
_OtnSmTcmPmBackwardDefectIndication_Type = FaultStatus
_OtnSmTcmPmBackwardDefectIndication_Object = MibTableColumn
otnSmTcmPmBackwardDefectIndication = _OtnSmTcmPmBackwardDefectIndication_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 2, 2, 1, 1, 26),
    _OtnSmTcmPmBackwardDefectIndication_Type()
)
otnSmTcmPmBackwardDefectIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otnSmTcmPmBackwardDefectIndication.setStatus("current")
_OtnSmTcmPmAlarmIndicationSignal_Type = FaultStatus
_OtnSmTcmPmAlarmIndicationSignal_Object = MibTableColumn
otnSmTcmPmAlarmIndicationSignal = _OtnSmTcmPmAlarmIndicationSignal_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 2, 2, 1, 1, 27),
    _OtnSmTcmPmAlarmIndicationSignal_Type()
)
otnSmTcmPmAlarmIndicationSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otnSmTcmPmAlarmIndicationSignal.setStatus("current")
_OtnSmTcmPmOpenConnectionIndication_Type = FaultStatus
_OtnSmTcmPmOpenConnectionIndication_Object = MibTableColumn
otnSmTcmPmOpenConnectionIndication = _OtnSmTcmPmOpenConnectionIndication_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 2, 2, 1, 1, 28),
    _OtnSmTcmPmOpenConnectionIndication_Type()
)
otnSmTcmPmOpenConnectionIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otnSmTcmPmOpenConnectionIndication.setStatus("current")
_OtnSmTcmPmClientMaintenanceIndication_Type = FaultStatus
_OtnSmTcmPmClientMaintenanceIndication_Object = MibTableColumn
otnSmTcmPmClientMaintenanceIndication = _OtnSmTcmPmClientMaintenanceIndication_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 2, 2, 1, 1, 29),
    _OtnSmTcmPmClientMaintenanceIndication_Type()
)
otnSmTcmPmClientMaintenanceIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otnSmTcmPmClientMaintenanceIndication.setStatus("deprecated")
_OtnSmTcmPmLockedDefectIndication_Type = FaultStatus
_OtnSmTcmPmLockedDefectIndication_Object = MibTableColumn
otnSmTcmPmLockedDefectIndication = _OtnSmTcmPmLockedDefectIndication_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 2, 2, 1, 1, 30),
    _OtnSmTcmPmLockedDefectIndication_Type()
)
otnSmTcmPmLockedDefectIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otnSmTcmPmLockedDefectIndication.setStatus("current")
_OtnSmTcmPmSetTerminatedTcmCommand_Type = CommandString
_OtnSmTcmPmSetTerminatedTcmCommand_Object = MibTableColumn
otnSmTcmPmSetTerminatedTcmCommand = _OtnSmTcmPmSetTerminatedTcmCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 2, 2, 1, 1, 31),
    _OtnSmTcmPmSetTerminatedTcmCommand_Type()
)
otnSmTcmPmSetTerminatedTcmCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otnSmTcmPmSetTerminatedTcmCommand.setStatus("current")
_OtnSmTcmPmNoRemoteTerminatedTcm_Type = FaultStatus
_OtnSmTcmPmNoRemoteTerminatedTcm_Object = MibTableColumn
otnSmTcmPmNoRemoteTerminatedTcm = _OtnSmTcmPmNoRemoteTerminatedTcm_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 2, 2, 1, 1, 32),
    _OtnSmTcmPmNoRemoteTerminatedTcm_Type()
)
otnSmTcmPmNoRemoteTerminatedTcm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otnSmTcmPmNoRemoteTerminatedTcm.setStatus("current")
_OtnSmTcmPmIncomingAlignmentError_Type = FaultStatus
_OtnSmTcmPmIncomingAlignmentError_Object = MibTableColumn
otnSmTcmPmIncomingAlignmentError = _OtnSmTcmPmIncomingAlignmentError_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 2, 2, 1, 1, 33),
    _OtnSmTcmPmIncomingAlignmentError_Type()
)
otnSmTcmPmIncomingAlignmentError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otnSmTcmPmIncomingAlignmentError.setStatus("current")
_OtnSmTcmPmBackwardIncomingAlignmentError_Type = FaultStatus
_OtnSmTcmPmBackwardIncomingAlignmentError_Object = MibTableColumn
otnSmTcmPmBackwardIncomingAlignmentError = _OtnSmTcmPmBackwardIncomingAlignmentError_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 2, 2, 1, 1, 34),
    _OtnSmTcmPmBackwardIncomingAlignmentError_Type()
)
otnSmTcmPmBackwardIncomingAlignmentError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otnSmTcmPmBackwardIncomingAlignmentError.setStatus("current")

# Managed Objects groups

otnGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 1, 1, 1)
)
otnGeneralGroup.setObjects(
      *(("LUM-OTN-MIB", "otnGeneralTestAndIncr"),
        ("LUM-OTN-MIB", "otnGeneralMibSpecVersion"),
        ("LUM-OTN-MIB", "otnGeneralMibImplVersion"),
        ("LUM-OTN-MIB", "otnGeneralLastChangeTime"))
)
if mibBuilder.loadTexts:
    otnGeneralGroup.setStatus("current")

otnSmTcmPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 1, 1, 2)
)
otnSmTcmPmGroup.setObjects(
      *(("LUM-OTN-MIB", "otnSmTcmPmIndex"),
        ("LUM-OTN-MIB", "otnSmTcmPmName"),
        ("LUM-OTN-MIB", "otnSmTcmPmType"),
        ("LUM-OTN-MIB", "otnSmTcmPmMonitorConfig"),
        ("LUM-OTN-MIB", "otnSmTcmPmTerminatedTcm"),
        ("LUM-OTN-MIB", "otnSmTcmPmDescr"),
        ("LUM-OTN-MIB", "otnSmTcmPmSubrack"),
        ("LUM-OTN-MIB", "otnSmTcmPmSlot"),
        ("LUM-OTN-MIB", "otnSmTcmPmTxPort"),
        ("LUM-OTN-MIB", "otnSmTcmPmAdminStatus"),
        ("LUM-OTN-MIB", "otnSmTcmPmOperStatus"),
        ("LUM-OTN-MIB", "otnSmTcmPmSapiTraceTransmitted"),
        ("LUM-OTN-MIB", "otnSmTcmPmSapiTraceReceivedByte0"),
        ("LUM-OTN-MIB", "otnSmTcmPmSapiTraceReceived"),
        ("LUM-OTN-MIB", "otnSmTcmPmSapiTraceExpected"),
        ("LUM-OTN-MIB", "otnSmTcmPmDapiTraceTransmitted"),
        ("LUM-OTN-MIB", "otnSmTcmPmDapiTraceReceivedByte0"),
        ("LUM-OTN-MIB", "otnSmTcmPmDapiTraceReceived"),
        ("LUM-OTN-MIB", "otnSmTcmPmDapiTraceExpected"),
        ("LUM-OTN-MIB", "otnSmTcmPmOpSpecificTraceTransmitted"),
        ("LUM-OTN-MIB", "otnSmTcmPmOpSpecificTraceReceived"),
        ("LUM-OTN-MIB", "otnSmTcmPmTraceIdMMDetectionMode"),
        ("LUM-OTN-MIB", "otnSmTcmPmTraceAlarmMode"),
        ("LUM-OTN-MIB", "otnSmTcmPmObjectProperty"),
        ("LUM-OTN-MIB", "otnSmTcmPmTraceMismatch"),
        ("LUM-OTN-MIB", "otnSmTcmPmBackwardDefectIndication"),
        ("LUM-OTN-MIB", "otnSmTcmPmAlarmIndicationSignal"),
        ("LUM-OTN-MIB", "otnSmTcmPmOpenConnectionIndication"),
        ("LUM-OTN-MIB", "otnSmTcmPmClientMaintenanceIndication"),
        ("LUM-OTN-MIB", "otnSmTcmPmLockedDefectIndication"))
)
if mibBuilder.loadTexts:
    otnSmTcmPmGroup.setStatus("deprecated")

otnSmTcmPmGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 1, 1, 3)
)
otnSmTcmPmGroupV2.setObjects(
      *(("LUM-OTN-MIB", "otnSmTcmPmIndex"),
        ("LUM-OTN-MIB", "otnSmTcmPmName"),
        ("LUM-OTN-MIB", "otnSmTcmPmType"),
        ("LUM-OTN-MIB", "otnSmTcmPmMonitorConfig"),
        ("LUM-OTN-MIB", "otnSmTcmPmTerminatedTcm"),
        ("LUM-OTN-MIB", "otnSmTcmPmDescr"),
        ("LUM-OTN-MIB", "otnSmTcmPmSubrack"),
        ("LUM-OTN-MIB", "otnSmTcmPmSlot"),
        ("LUM-OTN-MIB", "otnSmTcmPmTxPort"),
        ("LUM-OTN-MIB", "otnSmTcmPmAdminStatus"),
        ("LUM-OTN-MIB", "otnSmTcmPmOperStatus"),
        ("LUM-OTN-MIB", "otnSmTcmPmSapiTraceTransmitted"),
        ("LUM-OTN-MIB", "otnSmTcmPmSapiTraceReceivedByte0"),
        ("LUM-OTN-MIB", "otnSmTcmPmSapiTraceReceived"),
        ("LUM-OTN-MIB", "otnSmTcmPmSapiTraceExpected"),
        ("LUM-OTN-MIB", "otnSmTcmPmDapiTraceTransmitted"),
        ("LUM-OTN-MIB", "otnSmTcmPmDapiTraceReceivedByte0"),
        ("LUM-OTN-MIB", "otnSmTcmPmDapiTraceReceived"),
        ("LUM-OTN-MIB", "otnSmTcmPmDapiTraceExpected"),
        ("LUM-OTN-MIB", "otnSmTcmPmOpSpecificTraceTransmitted"),
        ("LUM-OTN-MIB", "otnSmTcmPmOpSpecificTraceReceived"),
        ("LUM-OTN-MIB", "otnSmTcmPmTraceIdMMDetectionMode"),
        ("LUM-OTN-MIB", "otnSmTcmPmTraceAlarmMode"),
        ("LUM-OTN-MIB", "otnSmTcmPmObjectProperty"),
        ("LUM-OTN-MIB", "otnSmTcmPmTraceMismatch"),
        ("LUM-OTN-MIB", "otnSmTcmPmBackwardDefectIndication"),
        ("LUM-OTN-MIB", "otnSmTcmPmAlarmIndicationSignal"),
        ("LUM-OTN-MIB", "otnSmTcmPmOpenConnectionIndication"),
        ("LUM-OTN-MIB", "otnSmTcmPmLockedDefectIndication"),
        ("LUM-OTN-MIB", "otnSmTcmPmSetTerminatedTcmCommand"),
        ("LUM-OTN-MIB", "otnSmTcmPmNoRemoteTerminatedTcm"))
)
if mibBuilder.loadTexts:
    otnSmTcmPmGroupV2.setStatus("deprecated")

otnSmTcmPmGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 1, 1, 4)
)
otnSmTcmPmGroupV3.setObjects(
      *(("LUM-OTN-MIB", "otnSmTcmPmIndex"),
        ("LUM-OTN-MIB", "otnSmTcmPmName"),
        ("LUM-OTN-MIB", "otnSmTcmPmType"),
        ("LUM-OTN-MIB", "otnSmTcmPmMonitorConfig"),
        ("LUM-OTN-MIB", "otnSmTcmPmTerminatedTcm"),
        ("LUM-OTN-MIB", "otnSmTcmPmDescr"),
        ("LUM-OTN-MIB", "otnSmTcmPmSubrack"),
        ("LUM-OTN-MIB", "otnSmTcmPmSlot"),
        ("LUM-OTN-MIB", "otnSmTcmPmTxPort"),
        ("LUM-OTN-MIB", "otnSmTcmPmAdminStatus"),
        ("LUM-OTN-MIB", "otnSmTcmPmOperStatus"),
        ("LUM-OTN-MIB", "otnSmTcmPmSapiTraceTransmitted"),
        ("LUM-OTN-MIB", "otnSmTcmPmSapiTraceReceivedByte0"),
        ("LUM-OTN-MIB", "otnSmTcmPmSapiTraceReceived"),
        ("LUM-OTN-MIB", "otnSmTcmPmSapiTraceExpected"),
        ("LUM-OTN-MIB", "otnSmTcmPmDapiTraceTransmitted"),
        ("LUM-OTN-MIB", "otnSmTcmPmDapiTraceReceivedByte0"),
        ("LUM-OTN-MIB", "otnSmTcmPmDapiTraceReceived"),
        ("LUM-OTN-MIB", "otnSmTcmPmDapiTraceExpected"),
        ("LUM-OTN-MIB", "otnSmTcmPmOpSpecificTraceTransmitted"),
        ("LUM-OTN-MIB", "otnSmTcmPmOpSpecificTraceReceived"),
        ("LUM-OTN-MIB", "otnSmTcmPmTraceIdMMDetectionMode"),
        ("LUM-OTN-MIB", "otnSmTcmPmTraceAlarmMode"),
        ("LUM-OTN-MIB", "otnSmTcmPmObjectProperty"),
        ("LUM-OTN-MIB", "otnSmTcmPmTraceMismatch"),
        ("LUM-OTN-MIB", "otnSmTcmPmBackwardDefectIndication"),
        ("LUM-OTN-MIB", "otnSmTcmPmAlarmIndicationSignal"),
        ("LUM-OTN-MIB", "otnSmTcmPmOpenConnectionIndication"),
        ("LUM-OTN-MIB", "otnSmTcmPmLockedDefectIndication"),
        ("LUM-OTN-MIB", "otnSmTcmPmSetTerminatedTcmCommand"),
        ("LUM-OTN-MIB", "otnSmTcmPmNoRemoteTerminatedTcm"),
        ("LUM-OTN-MIB", "otnSmTcmPmIncomingAlignmentError"),
        ("LUM-OTN-MIB", "otnSmTcmPmBackwardIncomingAlignmentError"))
)
if mibBuilder.loadTexts:
    otnSmTcmPmGroupV3.setStatus("current")

otnGeneralMinimalGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 1, 3, 1)
)
otnGeneralMinimalGroupV1.setObjects(
      *(("LUM-OTN-MIB", "otnGeneralLastChangeTime"),
        ("LUM-OTN-MIB", "otnGeneralSmTcmPmTableSize"))
)
if mibBuilder.loadTexts:
    otnGeneralMinimalGroupV1.setStatus("current")

otnSmTcmPmMinimalGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 1, 3, 2)
)
otnSmTcmPmMinimalGroupV1.setObjects(
      *(("LUM-OTN-MIB", "otnSmTcmPmIndex"),
        ("LUM-OTN-MIB", "otnSmTcmPmName"),
        ("LUM-OTN-MIB", "otnSmTcmPmType"),
        ("LUM-OTN-MIB", "otnSmTcmPmMonitorConfig"),
        ("LUM-OTN-MIB", "otnSmTcmPmTerminatedTcm"),
        ("LUM-OTN-MIB", "otnSmTcmPmDescr"),
        ("LUM-OTN-MIB", "otnSmTcmPmSubrack"),
        ("LUM-OTN-MIB", "otnSmTcmPmSlot"),
        ("LUM-OTN-MIB", "otnSmTcmPmTxPort"),
        ("LUM-OTN-MIB", "otnSmTcmPmAdminStatus"),
        ("LUM-OTN-MIB", "otnSmTcmPmOperStatus"),
        ("LUM-OTN-MIB", "otnSmTcmPmTraceIdMMDetectionMode"),
        ("LUM-OTN-MIB", "otnSmTcmPmSapiTraceTransmitted"),
        ("LUM-OTN-MIB", "otnSmTcmPmDapiTraceTransmitted"),
        ("LUM-OTN-MIB", "otnSmTcmPmOpSpecificTraceTransmitted"),
        ("LUM-OTN-MIB", "otnSmTcmPmSapiTraceReceivedByte0"),
        ("LUM-OTN-MIB", "otnSmTcmPmSapiTraceReceived"),
        ("LUM-OTN-MIB", "otnSmTcmPmDapiTraceReceivedByte0"),
        ("LUM-OTN-MIB", "otnSmTcmPmDapiTraceReceived"),
        ("LUM-OTN-MIB", "otnSmTcmPmOpSpecificTraceReceived"),
        ("LUM-OTN-MIB", "otnSmTcmPmSapiTraceExpected"),
        ("LUM-OTN-MIB", "otnSmTcmPmDapiTraceExpected"),
        ("LUM-OTN-MIB", "otnSmTcmPmTraceAlarmMode"),
        ("LUM-OTN-MIB", "otnSmTcmPmObjectProperty"),
        ("LUM-OTN-MIB", "otnSmTcmPmTraceMismatch"),
        ("LUM-OTN-MIB", "otnSmTcmPmBackwardDefectIndication"),
        ("LUM-OTN-MIB", "otnSmTcmPmAlarmIndicationSignal"),
        ("LUM-OTN-MIB", "otnSmTcmPmOpenConnectionIndication"),
        ("LUM-OTN-MIB", "otnSmTcmPmClientMaintenanceIndication"),
        ("LUM-OTN-MIB", "otnSmTcmPmLockedDefectIndication"))
)
if mibBuilder.loadTexts:
    otnSmTcmPmMinimalGroupV1.setStatus("deprecated")

otnSmTcmPmMinimalGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 1, 3, 3)
)
otnSmTcmPmMinimalGroupV2.setObjects(
      *(("LUM-OTN-MIB", "otnSmTcmPmIndex"),
        ("LUM-OTN-MIB", "otnSmTcmPmName"),
        ("LUM-OTN-MIB", "otnSmTcmPmType"),
        ("LUM-OTN-MIB", "otnSmTcmPmMonitorConfig"),
        ("LUM-OTN-MIB", "otnSmTcmPmTerminatedTcm"),
        ("LUM-OTN-MIB", "otnSmTcmPmDescr"),
        ("LUM-OTN-MIB", "otnSmTcmPmSubrack"),
        ("LUM-OTN-MIB", "otnSmTcmPmSlot"),
        ("LUM-OTN-MIB", "otnSmTcmPmTxPort"),
        ("LUM-OTN-MIB", "otnSmTcmPmAdminStatus"),
        ("LUM-OTN-MIB", "otnSmTcmPmOperStatus"),
        ("LUM-OTN-MIB", "otnSmTcmPmTraceIdMMDetectionMode"),
        ("LUM-OTN-MIB", "otnSmTcmPmSapiTraceTransmitted"),
        ("LUM-OTN-MIB", "otnSmTcmPmDapiTraceTransmitted"),
        ("LUM-OTN-MIB", "otnSmTcmPmOpSpecificTraceTransmitted"),
        ("LUM-OTN-MIB", "otnSmTcmPmSapiTraceReceivedByte0"),
        ("LUM-OTN-MIB", "otnSmTcmPmSapiTraceReceived"),
        ("LUM-OTN-MIB", "otnSmTcmPmDapiTraceReceivedByte0"),
        ("LUM-OTN-MIB", "otnSmTcmPmDapiTraceReceived"),
        ("LUM-OTN-MIB", "otnSmTcmPmOpSpecificTraceReceived"),
        ("LUM-OTN-MIB", "otnSmTcmPmSapiTraceExpected"),
        ("LUM-OTN-MIB", "otnSmTcmPmDapiTraceExpected"),
        ("LUM-OTN-MIB", "otnSmTcmPmTraceAlarmMode"),
        ("LUM-OTN-MIB", "otnSmTcmPmObjectProperty"),
        ("LUM-OTN-MIB", "otnSmTcmPmTraceMismatch"),
        ("LUM-OTN-MIB", "otnSmTcmPmBackwardDefectIndication"),
        ("LUM-OTN-MIB", "otnSmTcmPmAlarmIndicationSignal"),
        ("LUM-OTN-MIB", "otnSmTcmPmOpenConnectionIndication"),
        ("LUM-OTN-MIB", "otnSmTcmPmLockedDefectIndication"),
        ("LUM-OTN-MIB", "otnSmTcmPmSetTerminatedTcmCommand"))
)
if mibBuilder.loadTexts:
    otnSmTcmPmMinimalGroupV2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumOtnBasicCompl1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 1, 2, 1)
)
lumOtnBasicCompl1.setObjects(
      *(("LUM-OTN-MIB", "otnGeneralGroup"),
        ("LUM-OTN-MIB", "otnSmTcmPmGroup"))
)
if mibBuilder.loadTexts:
    lumOtnBasicCompl1.setStatus(
        "deprecated"
    )

lumOtnBasicCompl2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 1, 2, 2)
)
lumOtnBasicCompl2.setObjects(
      *(("LUM-OTN-MIB", "otnGeneralGroup"),
        ("LUM-OTN-MIB", "otnSmTcmPmGroupV2"))
)
if mibBuilder.loadTexts:
    lumOtnBasicCompl2.setStatus(
        "deprecated"
    )

lumOtnBasicCompl3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 1, 2, 3)
)
lumOtnBasicCompl3.setObjects(
      *(("LUM-OTN-MIB", "otnGeneralGroup"),
        ("LUM-OTN-MIB", "otnSmTcmPmGroupV3"))
)
if mibBuilder.loadTexts:
    lumOtnBasicCompl3.setStatus(
        "current"
    )

lumOtmMinimalComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 1, 4, 1)
)
lumOtmMinimalComplV1.setObjects(
      *(("LUM-OTN-MIB", "otnGeneralMinimalGroupV1"),
        ("LUM-OTN-MIB", "otnSmTcmPmMinimalGroupV1"))
)
if mibBuilder.loadTexts:
    lumOtmMinimalComplV1.setStatus(
        "deprecated"
    )

lumOtmMinimalComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 34, 1, 4, 2)
)
lumOtmMinimalComplV2.setObjects(
      *(("LUM-OTN-MIB", "otnGeneralMinimalGroupV1"),
        ("LUM-OTN-MIB", "otnSmTcmPmMinimalGroupV2"))
)
if mibBuilder.loadTexts:
    lumOtmMinimalComplV2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-OTN-MIB",
    **{"lumOtnMIBModule": lumOtnMIBModule,
       "lumOtnConfs": lumOtnConfs,
       "lumOtnGroups": lumOtnGroups,
       "otnGeneralGroup": otnGeneralGroup,
       "otnSmTcmPmGroup": otnSmTcmPmGroup,
       "otnSmTcmPmGroupV2": otnSmTcmPmGroupV2,
       "otnSmTcmPmGroupV3": otnSmTcmPmGroupV3,
       "lumOtnCompl": lumOtnCompl,
       "lumOtnBasicCompl1": lumOtnBasicCompl1,
       "lumOtnBasicCompl2": lumOtnBasicCompl2,
       "lumOtnBasicCompl3": lumOtnBasicCompl3,
       "lumOtnMinimalGroups": lumOtnMinimalGroups,
       "otnGeneralMinimalGroupV1": otnGeneralMinimalGroupV1,
       "otnSmTcmPmMinimalGroupV1": otnSmTcmPmMinimalGroupV1,
       "otnSmTcmPmMinimalGroupV2": otnSmTcmPmMinimalGroupV2,
       "lumOtnMinimalCompl": lumOtnMinimalCompl,
       "lumOtmMinimalComplV1": lumOtmMinimalComplV1,
       "lumOtmMinimalComplV2": lumOtmMinimalComplV2,
       "lumOtnMIBObjects": lumOtnMIBObjects,
       "otnGeneral": otnGeneral,
       "otnGeneralTestAndIncr": otnGeneralTestAndIncr,
       "otnGeneralMibSpecVersion": otnGeneralMibSpecVersion,
       "otnGeneralMibImplVersion": otnGeneralMibImplVersion,
       "otnGeneralLastChangeTime": otnGeneralLastChangeTime,
       "otnGeneralStateLastChangeTime": otnGeneralStateLastChangeTime,
       "otnGeneralSmTcmPmTableSize": otnGeneralSmTcmPmTableSize,
       "otnSmTcmPmList": otnSmTcmPmList,
       "otnSmTcmPmTable": otnSmTcmPmTable,
       "otnSmTcmPmEntry": otnSmTcmPmEntry,
       "otnSmTcmPmIndex": otnSmTcmPmIndex,
       "otnSmTcmPmName": otnSmTcmPmName,
       "otnSmTcmPmType": otnSmTcmPmType,
       "otnSmTcmPmMonitorConfig": otnSmTcmPmMonitorConfig,
       "otnSmTcmPmTerminatedTcm": otnSmTcmPmTerminatedTcm,
       "otnSmTcmPmDescr": otnSmTcmPmDescr,
       "otnSmTcmPmSubrack": otnSmTcmPmSubrack,
       "otnSmTcmPmSlot": otnSmTcmPmSlot,
       "otnSmTcmPmTxPort": otnSmTcmPmTxPort,
       "otnSmTcmPmAdminStatus": otnSmTcmPmAdminStatus,
       "otnSmTcmPmOperStatus": otnSmTcmPmOperStatus,
       "otnSmTcmPmSapiTraceTransmitted": otnSmTcmPmSapiTraceTransmitted,
       "otnSmTcmPmSapiTraceReceivedByte0": otnSmTcmPmSapiTraceReceivedByte0,
       "otnSmTcmPmSapiTraceReceived": otnSmTcmPmSapiTraceReceived,
       "otnSmTcmPmSapiTraceExpected": otnSmTcmPmSapiTraceExpected,
       "otnSmTcmPmDapiTraceTransmitted": otnSmTcmPmDapiTraceTransmitted,
       "otnSmTcmPmDapiTraceReceivedByte0": otnSmTcmPmDapiTraceReceivedByte0,
       "otnSmTcmPmDapiTraceReceived": otnSmTcmPmDapiTraceReceived,
       "otnSmTcmPmDapiTraceExpected": otnSmTcmPmDapiTraceExpected,
       "otnSmTcmPmOpSpecificTraceTransmitted": otnSmTcmPmOpSpecificTraceTransmitted,
       "otnSmTcmPmOpSpecificTraceReceived": otnSmTcmPmOpSpecificTraceReceived,
       "otnSmTcmPmTraceIdMMDetectionMode": otnSmTcmPmTraceIdMMDetectionMode,
       "otnSmTcmPmTraceAlarmMode": otnSmTcmPmTraceAlarmMode,
       "otnSmTcmPmObjectProperty": otnSmTcmPmObjectProperty,
       "otnSmTcmPmTraceMismatch": otnSmTcmPmTraceMismatch,
       "otnSmTcmPmBackwardDefectIndication": otnSmTcmPmBackwardDefectIndication,
       "otnSmTcmPmAlarmIndicationSignal": otnSmTcmPmAlarmIndicationSignal,
       "otnSmTcmPmOpenConnectionIndication": otnSmTcmPmOpenConnectionIndication,
       "otnSmTcmPmClientMaintenanceIndication": otnSmTcmPmClientMaintenanceIndication,
       "otnSmTcmPmLockedDefectIndication": otnSmTcmPmLockedDefectIndication,
       "otnSmTcmPmSetTerminatedTcmCommand": otnSmTcmPmSetTerminatedTcmCommand,
       "otnSmTcmPmNoRemoteTerminatedTcm": otnSmTcmPmNoRemoteTerminatedTcm,
       "otnSmTcmPmIncomingAlignmentError": otnSmTcmPmIncomingAlignmentError,
       "otnSmTcmPmBackwardIncomingAlignmentError": otnSmTcmPmBackwardIncomingAlignmentError}
)
