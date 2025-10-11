# SNMP MIB module (RAD-Dacs-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rad/RAD-Dacs-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:18:38 2025
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

(PhysicalIndexOrZero,
 entPhysicalAlias,
 entPhysicalDescr,
 entPhysicalEntry,
 entPhysicalHardwareRev,
 entPhysicalSoftwareRev) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndexOrZero",
    "entPhysicalAlias",
    "entPhysicalDescr",
    "entPhysicalEntry",
    "entPhysicalHardwareRev",
    "entPhysicalSoftwareRev")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(agnLed,
 agnThresholdMax,
 agnThresholdMin,
 agnThresholdUom,
 alarmEventLogAlarmOrEventId,
 alarmEventLogDateAndTime,
 alarmEventLogDescription,
 alarmEventLogSeverity,
 alarmEventLogSourceName,
 alarmEventReason,
 systemsEvents) = mibBuilder.importSymbols(
    "RAD-GEN-MIB",
    "agnLed",
    "agnThresholdMax",
    "agnThresholdMin",
    "agnThresholdUom",
    "alarmEventLogAlarmOrEventId",
    "alarmEventLogDateAndTime",
    "alarmEventLogDescription",
    "alarmEventLogSeverity",
    "alarmEventLogSourceName",
    "alarmEventReason",
    "systemsEvents")

(protectGroupLastCmd,
 protectGroupLastSwitchReason) = mibBuilder.importSymbols(
    "RAD-Protection-MIB",
    "protectGroupLastCmd",
    "protectGroupLastSwitchReason")

(radWan,) = mibBuilder.importSymbols(
    "RAD-SMI-MIB",
    "radWan")

(CardType,
 ProtectGroupCmdType,
 ProtectLastSwitchReasonType,
 SlotType) = mibBuilder.importSymbols(
    "RAD-TC",
    "CardType",
    "ProtectGroupCmdType",
    "ProtectLastSwitchReasonType",
    "SlotType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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

dacsMux = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DacsMuxEvents_ObjectIdentity = ObjectIdentity
dacsMuxEvents = _DacsMuxEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 0)
)
if mibBuilder.loadTexts:
    dacsMuxEvents.setStatus("current")
_SystemDacsMux_ObjectIdentity = ObjectIdentity
systemDacsMux = _SystemDacsMux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1)
)
_SysSa_ObjectIdentity = ObjectIdentity
sysSa = _SysSa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 1)
)
_SysSaSwchStatus_Type = Integer32
_SysSaSwchStatus_Object = MibScalar
sysSaSwchStatus = _SysSaSwchStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 1, 1),
    _SysSaSwchStatus_Type()
)
sysSaSwchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSaSwchStatus.setStatus("current")


class _SysSaSwRevision_Type(DisplayString):
    """Custom type sysSaSwRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysSaSwRevision_Type.__name__ = "DisplayString"
_SysSaSwRevision_Object = MibScalar
sysSaSwRevision = _SysSaSwRevision_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 1, 2),
    _SysSaSwRevision_Type()
)
sysSaSwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSaSwRevision.setStatus("current")


class _SysSaHwVersion_Type(DisplayString):
    """Custom type sysSaHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysSaHwVersion_Type.__name__ = "DisplayString"
_SysSaHwVersion_Object = MibScalar
sysSaHwVersion = _SysSaHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 1, 3),
    _SysSaHwVersion_Type()
)
sysSaHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSaHwVersion.setStatus("current")
_SysSaPorts_Type = Integer32
_SysSaPorts_Object = MibScalar
sysSaPorts = _SysSaPorts_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 1, 4),
    _SysSaPorts_Type()
)
sysSaPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSaPorts.setStatus("current")
_SysSaReadSwch_Type = Integer32
_SysSaReadSwch_Object = MibScalar
sysSaReadSwch = _SysSaReadSwch_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 1, 5),
    _SysSaReadSwch_Type()
)
sysSaReadSwch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSaReadSwch.setStatus("current")


class _SysSaBuActivePort_Type(Integer32):
    """Custom type sysSaBuActivePort based on Integer32"""
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
        *(("notApplicable", 1),
          ("e1T1orSerial", 2),
          ("eth", 3),
          ("primary", 4),
          ("secondary", 5),
          ("third", 6),
          ("fourth", 7))
    )


_SysSaBuActivePort_Type.__name__ = "Integer32"
_SysSaBuActivePort_Object = MibScalar
sysSaBuActivePort = _SysSaBuActivePort_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 1, 6),
    _SysSaBuActivePort_Type()
)
sysSaBuActivePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSaBuActivePort.setStatus("current")
_SysHub_ObjectIdentity = ObjectIdentity
sysHub = _SysHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 2)
)
_SysChas_ObjectIdentity = ObjectIdentity
sysChas = _SysChas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 2, 1)
)
_ChassTotalNoOfSlt_Type = Integer32
_ChassTotalNoOfSlt_Object = MibScalar
chassTotalNoOfSlt = _ChassTotalNoOfSlt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 2, 1, 1),
    _ChassTotalNoOfSlt_Type()
)
chassTotalNoOfSlt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassTotalNoOfSlt.setStatus("current")
_ChassTotalNoOfIoSlt_Type = Integer32
_ChassTotalNoOfIoSlt_Object = MibScalar
chassTotalNoOfIoSlt = _ChassTotalNoOfIoSlt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 2, 1, 2),
    _ChassTotalNoOfIoSlt_Type()
)
chassTotalNoOfIoSlt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassTotalNoOfIoSlt.setStatus("current")
_ChassTotalNoOfPsSlt_Type = Integer32
_ChassTotalNoOfPsSlt_Object = MibScalar
chassTotalNoOfPsSlt = _ChassTotalNoOfPsSlt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 2, 1, 3),
    _ChassTotalNoOfPsSlt_Type()
)
chassTotalNoOfPsSlt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassTotalNoOfPsSlt.setStatus("current")
_ChassTotalNoOfClSlt_Type = Integer32
_ChassTotalNoOfClSlt_Object = MibScalar
chassTotalNoOfClSlt = _ChassTotalNoOfClSlt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 2, 1, 4),
    _ChassTotalNoOfClSlt_Type()
)
chassTotalNoOfClSlt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassTotalNoOfClSlt.setStatus("current")
_ChassTotalNoOfMlSlt_Type = Integer32
_ChassTotalNoOfMlSlt_Object = MibScalar
chassTotalNoOfMlSlt = _ChassTotalNoOfMlSlt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 2, 1, 5),
    _ChassTotalNoOfMlSlt_Type()
)
chassTotalNoOfMlSlt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassTotalNoOfMlSlt.setStatus("current")
_SysDcl_ObjectIdentity = ObjectIdentity
sysDcl = _SysDcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 2, 2)
)
_SysDclTable_Object = MibTable
sysDclTable = _SysDclTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    sysDclTable.setStatus("current")
_SysDclEntry_Object = MibTableRow
sysDclEntry = _SysDclEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 2, 2, 1, 1)
)
sysDclEntry.setIndexNames(
    (0, "RAD-Dacs-MIB", "sysDclCnfgIdx"),
)
if mibBuilder.loadTexts:
    sysDclEntry.setStatus("current")


class _SysDclCnfgIdx_Type(Integer32):
    """Custom type sysDclCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SysDclCnfgIdx_Type.__name__ = "Integer32"
_SysDclCnfgIdx_Object = MibTableColumn
sysDclCnfgIdx = _SysDclCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 2, 2, 1, 1, 1),
    _SysDclCnfgIdx_Type()
)
sysDclCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDclCnfgIdx.setStatus("current")


class _SysDclRedundancy_Type(Integer32):
    """Custom type sysDclRedundancy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_SysDclRedundancy_Type.__name__ = "Integer32"
_SysDclRedundancy_Object = MibTableColumn
sysDclRedundancy = _SysDclRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 2, 2, 1, 1, 2),
    _SysDclRedundancy_Type()
)
sysDclRedundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDclRedundancy.setStatus("current")


class _SysDclActiveCl_Type(Integer32):
    """Custom type sysDclActiveCl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("dclA", 2),
          ("dclB", 3))
    )


_SysDclActiveCl_Type.__name__ = "Integer32"
_SysDclActiveCl_Object = MibTableColumn
sysDclActiveCl = _SysDclActiveCl_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 2, 2, 1, 1, 3),
    _SysDclActiveCl_Type()
)
sysDclActiveCl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDclActiveCl.setStatus("current")
_SysDclFlipDelay_Type = Integer32
_SysDclFlipDelay_Object = MibTableColumn
sysDclFlipDelay = _SysDclFlipDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 2, 2, 1, 1, 4),
    _SysDclFlipDelay_Type()
)
sysDclFlipDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDclFlipDelay.setStatus("current")


class _SysDclFlipUponStnClk_Type(Integer32):
    """Custom type sysDclFlipUponStnClk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("no", 2),
          ("yes", 3))
    )


_SysDclFlipUponStnClk_Type.__name__ = "Integer32"
_SysDclFlipUponStnClk_Object = MibTableColumn
sysDclFlipUponStnClk = _SysDclFlipUponStnClk_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 2, 2, 1, 1, 5),
    _SysDclFlipUponStnClk_Type()
)
sysDclFlipUponStnClk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDclFlipUponStnClk.setStatus("current")
_SysDclChFailThreshold_Type = Integer32
_SysDclChFailThreshold_Object = MibTableColumn
sysDclChFailThreshold = _SysDclChFailThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 2, 2, 1, 1, 6),
    _SysDclChFailThreshold_Type()
)
sysDclChFailThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDclChFailThreshold.setStatus("current")
_SysDclChPriority_Type = OctetString
_SysDclChPriority_Object = MibTableColumn
sysDclChPriority = _SysDclChPriority_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 2, 2, 1, 1, 7),
    _SysDclChPriority_Type()
)
sysDclChPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDclChPriority.setStatus("current")


class _SysDclConfigDownloadSrc_Type(Integer32):
    """Custom type sysDclConfigDownloadSrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("dclA", 2),
          ("dclB", 3))
    )


_SysDclConfigDownloadSrc_Type.__name__ = "Integer32"
_SysDclConfigDownloadSrc_Object = MibTableColumn
sysDclConfigDownloadSrc = _SysDclConfigDownloadSrc_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 2, 2, 1, 1, 8),
    _SysDclConfigDownloadSrc_Type()
)
sysDclConfigDownloadSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDclConfigDownloadSrc.setStatus("current")


class _SysDclSwDownloadSrc_Type(Integer32):
    """Custom type sysDclSwDownloadSrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("dclA", 2),
          ("dclB", 3))
    )


_SysDclSwDownloadSrc_Type.__name__ = "Integer32"
_SysDclSwDownloadSrc_Object = MibTableColumn
sysDclSwDownloadSrc = _SysDclSwDownloadSrc_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 2, 2, 1, 1, 9),
    _SysDclSwDownloadSrc_Type()
)
sysDclSwDownloadSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDclSwDownloadSrc.setStatus("current")


class _SysDclRedundancyStatus_Type(Bits):
    """Custom type sysDclRedundancyStatus based on Bits"""
    namedValues = NamedValues(
        *(("cnfgMismatch", 0),
          ("swMismatch", 1),
          ("cardAAbsent", 2),
          ("cardBAbsent", 3),
          ("lossOfCommunication", 4),
          ("hwMismatch", 5),
          ("cnfgUpdate", 6),
          ("swUpdate", 7))
    )

_SysDclRedundancyStatus_Type.__name__ = "Bits"
_SysDclRedundancyStatus_Object = MibTableColumn
sysDclRedundancyStatus = _SysDclRedundancyStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 2, 2, 1, 1, 10),
    _SysDclRedundancyStatus_Type()
)
sysDclRedundancyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDclRedundancyStatus.setStatus("current")


class _SysDclOnline_Type(Integer32):
    """Custom type sysDclOnline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dclA", 1),
          ("dclB", 2))
    )


_SysDclOnline_Type.__name__ = "Integer32"
_SysDclOnline_Object = MibScalar
sysDclOnline = _SysDclOnline_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 2, 2, 2),
    _SysDclOnline_Type()
)
sysDclOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDclOnline.setStatus("current")
_SysDclCopyDbTable_Object = MibTable
sysDclCopyDbTable = _SysDclCopyDbTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    sysDclCopyDbTable.setStatus("current")
_SysDclCopyDbEntry_Object = MibTableRow
sysDclCopyDbEntry = _SysDclCopyDbEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 2, 2, 3, 1)
)
sysDclCopyDbEntry.setIndexNames(
    (0, "RAD-Dacs-MIB", "sysDclCopyDbIdx"),
)
if mibBuilder.loadTexts:
    sysDclCopyDbEntry.setStatus("current")


class _SysDclCopyDbIdx_Type(Integer32):
    """Custom type sysDclCopyDbIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SysDclCopyDbIdx_Type.__name__ = "Integer32"
_SysDclCopyDbIdx_Object = MibTableColumn
sysDclCopyDbIdx = _SysDclCopyDbIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 2, 2, 3, 1, 1),
    _SysDclCopyDbIdx_Type()
)
sysDclCopyDbIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDclCopyDbIdx.setStatus("current")


class _SysDclCopyDbCmd_Type(Integer32):
    """Custom type sysDclCopyDbCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_SysDclCopyDbCmd_Type.__name__ = "Integer32"
_SysDclCopyDbCmd_Object = MibTableColumn
sysDclCopyDbCmd = _SysDclCopyDbCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 2, 2, 3, 1, 2),
    _SysDclCopyDbCmd_Type()
)
sysDclCopyDbCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDclCopyDbCmd.setStatus("current")


class _SysDclFlipCmd_Type(Integer32):
    """Custom type sysDclFlipCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("flip", 3))
    )


_SysDclFlipCmd_Type.__name__ = "Integer32"
_SysDclFlipCmd_Object = MibScalar
sysDclFlipCmd = _SysDclFlipCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 2, 2, 4),
    _SysDclFlipCmd_Type()
)
sysDclFlipCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDclFlipCmd.setStatus("current")
_SysStatus_ObjectIdentity = ObjectIdentity
sysStatus = _SysStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 3)
)


class _SysSDateFormat_Type(Integer32):
    """Custom type sysSDateFormat based on Integer32"""
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
        *(("ddMMYYYY", 1),
          ("mmDDYYYY", 2),
          ("yyyyDDMM", 3),
          ("yyyyMMDD", 4))
    )


_SysSDateFormat_Type.__name__ = "Integer32"
_SysSDateFormat_Object = MibScalar
sysSDateFormat = _SysSDateFormat_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 3, 1),
    _SysSDateFormat_Type()
)
sysSDateFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSDateFormat.setStatus("current")


class _SysSDateCmd_Type(DisplayString):
    """Custom type sysSDateCmd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysSDateCmd_Type.__name__ = "DisplayString"
_SysSDateCmd_Object = MibScalar
sysSDateCmd = _SysSDateCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 3, 2),
    _SysSDateCmd_Type()
)
sysSDateCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSDateCmd.setStatus("current")


class _SysSTimeCmd_Type(DisplayString):
    """Custom type sysSTimeCmd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysSTimeCmd_Type.__name__ = "DisplayString"
_SysSTimeCmd_Object = MibScalar
sysSTimeCmd = _SysSTimeCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 3, 3),
    _SysSTimeCmd_Type()
)
sysSTimeCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSTimeCmd.setStatus("current")
_SysSActiveCnfg_Type = Integer32
_SysSActiveCnfg_Object = MibScalar
sysSActiveCnfg = _SysSActiveCnfg_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 3, 4),
    _SysSActiveCnfg_Type()
)
sysSActiveCnfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSActiveCnfg.setStatus("current")
_SysSEditCnfg_Type = Integer32
_SysSEditCnfg_Object = MibScalar
sysSEditCnfg = _SysSEditCnfg_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 3, 5),
    _SysSEditCnfg_Type()
)
sysSEditCnfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSEditCnfg.setStatus("current")


class _SysSEditBy_Type(Integer32):
    """Custom type sysSEditBy based on Integer32"""
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
        *(("none", 1),
          ("snmp", 2),
          ("terCon1", 3),
          ("terCon2", 4),
          ("terInbandCon1", 5),
          ("terInbandCon2", 6),
          ("lcd", 7))
    )


_SysSEditBy_Type.__name__ = "Integer32"
_SysSEditBy_Object = MibScalar
sysSEditBy = _SysSEditBy_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 3, 6),
    _SysSEditBy_Type()
)
sysSEditBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSEditBy.setStatus("current")


class _SysSClkSrc_Type(Integer32):
    """Custom type sysSClkSrc based on Integer32"""
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
        *(("master", 1),
          ("fallback", 2),
          ("internal", 3),
          ("ml", 4))
    )


_SysSClkSrc_Type.__name__ = "Integer32"
_SysSClkSrc_Object = MibScalar
sysSClkSrc = _SysSClkSrc_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 3, 7),
    _SysSClkSrc_Type()
)
sysSClkSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSClkSrc.setStatus("current")


class _SysSAlrStatus_Type(Integer32):
    """Custom type sysSAlrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("major", 3),
          ("minor", 4),
          ("event", 5),
          ("warning", 6),
          ("critical", 7))
    )


_SysSAlrStatus_Type.__name__ = "Integer32"
_SysSAlrStatus_Object = MibScalar
sysSAlrStatus = _SysSAlrStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 3, 8),
    _SysSAlrStatus_Type()
)
sysSAlrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSAlrStatus.setStatus("current")


class _SysSAlrStatusAll_Type(Integer32):
    """Custom type sysSAlrStatusAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("major", 3),
          ("minor", 4),
          ("event", 5),
          ("warning", 6),
          ("critical", 7))
    )


_SysSAlrStatusAll_Type.__name__ = "Integer32"
_SysSAlrStatusAll_Object = MibScalar
sysSAlrStatusAll = _SysSAlrStatusAll_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 3, 9),
    _SysSAlrStatusAll_Type()
)
sysSAlrStatusAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSAlrStatusAll.setStatus("current")


class _SysSTestStatus_Type(Integer32):
    """Custom type sysSTestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_SysSTestStatus_Type.__name__ = "Integer32"
_SysSTestStatus_Object = MibScalar
sysSTestStatus = _SysSTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 3, 10),
    _SysSTestStatus_Type()
)
sysSTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSTestStatus.setStatus("current")


class _SysSSanityCheckStatus_Type(Integer32):
    """Custom type sysSSanityCheckStatus based on Integer32"""
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
        *(("unknown", 1),
          ("fail", 2),
          ("warning", 3),
          ("ok", 4))
    )


_SysSSanityCheckStatus_Type.__name__ = "Integer32"
_SysSSanityCheckStatus_Object = MibScalar
sysSSanityCheckStatus = _SysSSanityCheckStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 3, 11),
    _SysSSanityCheckStatus_Type()
)
sysSSanityCheckStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSSanityCheckStatus.setStatus("current")
_SysSNoOfSanityCheckErr_Type = Integer32
_SysSNoOfSanityCheckErr_Object = MibScalar
sysSNoOfSanityCheckErr = _SysSNoOfSanityCheckErr_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 3, 12),
    _SysSNoOfSanityCheckErr_Type()
)
sysSNoOfSanityCheckErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSNoOfSanityCheckErr.setStatus("current")
_SysSErrListTable_Object = MibTable
sysSErrListTable = _SysSErrListTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 3, 13)
)
if mibBuilder.loadTexts:
    sysSErrListTable.setStatus("current")
_SysSErrListEntry_Object = MibTableRow
sysSErrListEntry = _SysSErrListEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 3, 13, 1)
)
sysSErrListEntry.setIndexNames(
    (0, "RAD-Dacs-MIB", "sysSErrType"),
    (0, "RAD-Dacs-MIB", "sysSErrIdx"),
)
if mibBuilder.loadTexts:
    sysSErrListEntry.setStatus("current")


class _SysSErrType_Type(Integer32):
    """Custom type sysSErrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("warning", 2))
    )


_SysSErrType_Type.__name__ = "Integer32"
_SysSErrType_Object = MibTableColumn
sysSErrType = _SysSErrType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 3, 13, 1, 1),
    _SysSErrType_Type()
)
sysSErrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSErrType.setStatus("current")
_SysSErrIdx_Type = Integer32
_SysSErrIdx_Object = MibTableColumn
sysSErrIdx = _SysSErrIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 3, 13, 1, 2),
    _SysSErrIdx_Type()
)
sysSErrIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSErrIdx.setStatus("current")


class _SysSErrDescription_Type(DisplayString):
    """Custom type sysSErrDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysSErrDescription_Type.__name__ = "DisplayString"
_SysSErrDescription_Object = MibTableColumn
sysSErrDescription = _SysSErrDescription_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 3, 13, 1, 3),
    _SysSErrDescription_Type()
)
sysSErrDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSErrDescription.setStatus("current")
_SysSMaxNoOfCnfg_Type = Integer32
_SysSMaxNoOfCnfg_Object = MibScalar
sysSMaxNoOfCnfg = _SysSMaxNoOfCnfg_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 3, 14),
    _SysSMaxNoOfCnfg_Type()
)
sysSMaxNoOfCnfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSMaxNoOfCnfg.setStatus("current")
_SysSSelfTestResult_Type = Integer32
_SysSSelfTestResult_Object = MibScalar
sysSSelfTestResult = _SysSSelfTestResult_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 3, 15),
    _SysSSelfTestResult_Type()
)
sysSSelfTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSSelfTestResult.setStatus("current")


class _SysSRelayState_Type(Integer32):
    """Custom type sysSRelayState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("off", 2),
          ("on", 3))
    )


_SysSRelayState_Type.__name__ = "Integer32"
_SysSRelayState_Object = MibScalar
sysSRelayState = _SysSRelayState_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 3, 16),
    _SysSRelayState_Type()
)
sysSRelayState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSRelayState.setStatus("current")


class _SysSInvertedAlr_Type(Integer32):
    """Custom type sysSInvertedAlr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("no", 2),
          ("yes", 3))
    )


_SysSInvertedAlr_Type.__name__ = "Integer32"
_SysSInvertedAlr_Object = MibScalar
sysSInvertedAlr = _SysSInvertedAlr_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 3, 17),
    _SysSInvertedAlr_Type()
)
sysSInvertedAlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSInvertedAlr.setStatus("current")
_SysSRdnFlipTable_Object = MibTable
sysSRdnFlipTable = _SysSRdnFlipTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 3, 18)
)
if mibBuilder.loadTexts:
    sysSRdnFlipTable.setStatus("current")
_SysSRdnFlipEntry_Object = MibTableRow
sysSRdnFlipEntry = _SysSRdnFlipEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 3, 18, 1)
)
sysSRdnFlipEntry.setIndexNames(
    (0, "RAD-Dacs-MIB", "sysSRdnFlipIdx"),
)
if mibBuilder.loadTexts:
    sysSRdnFlipEntry.setStatus("current")
_SysSRdnFlipIdx_Type = Integer32
_SysSRdnFlipIdx_Object = MibTableColumn
sysSRdnFlipIdx = _SysSRdnFlipIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 3, 18, 1, 1),
    _SysSRdnFlipIdx_Type()
)
sysSRdnFlipIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSRdnFlipIdx.setStatus("current")


class _SysSRdnFlipSlot_Type(Integer32):
    """Custom type sysSRdnFlipSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              255)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("io13", 17),
          ("io14", 18),
          ("io15", 19),
          ("notApplicable", 255))
    )


_SysSRdnFlipSlot_Type.__name__ = "Integer32"
_SysSRdnFlipSlot_Object = MibTableColumn
sysSRdnFlipSlot = _SysSRdnFlipSlot_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 3, 18, 1, 2),
    _SysSRdnFlipSlot_Type()
)
sysSRdnFlipSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSRdnFlipSlot.setStatus("current")
_SysSRdnFlipPort_Type = Integer32
_SysSRdnFlipPort_Object = MibTableColumn
sysSRdnFlipPort = _SysSRdnFlipPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 3, 18, 1, 3),
    _SysSRdnFlipPort_Type()
)
sysSRdnFlipPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSRdnFlipPort.setStatus("current")
_SysSRdnFlipCause_Type = DisplayString
_SysSRdnFlipCause_Object = MibTableColumn
sysSRdnFlipCause = _SysSRdnFlipCause_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 3, 18, 1, 4),
    _SysSRdnFlipCause_Type()
)
sysSRdnFlipCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSRdnFlipCause.setStatus("current")
_SysSRdnFlipDate_Type = DisplayString
_SysSRdnFlipDate_Object = MibTableColumn
sysSRdnFlipDate = _SysSRdnFlipDate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 3, 18, 1, 5),
    _SysSRdnFlipDate_Type()
)
sysSRdnFlipDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSRdnFlipDate.setStatus("current")
_SysSRdnFlipTime_Type = DisplayString
_SysSRdnFlipTime_Object = MibTableColumn
sysSRdnFlipTime = _SysSRdnFlipTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 3, 18, 1, 6),
    _SysSRdnFlipTime_Type()
)
sysSRdnFlipTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSRdnFlipTime.setStatus("current")


class _SysSRdnFlipTableClearCmd_Type(Integer32):
    """Custom type sysSRdnFlipTableClearCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_SysSRdnFlipTableClearCmd_Type.__name__ = "Integer32"
_SysSRdnFlipTableClearCmd_Object = MibScalar
sysSRdnFlipTableClearCmd = _SysSRdnFlipTableClearCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 3, 19),
    _SysSRdnFlipTableClearCmd_Type()
)
sysSRdnFlipTableClearCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSRdnFlipTableClearCmd.setStatus("current")
_SysSRdnFlipCmd_Type = ObjectIdentifier
_SysSRdnFlipCmd_Object = MibScalar
sysSRdnFlipCmd = _SysSRdnFlipCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 3, 20),
    _SysSRdnFlipCmd_Type()
)
sysSRdnFlipCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSRdnFlipCmd.setStatus("current")
_SysSBusTable_Object = MibTable
sysSBusTable = _SysSBusTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 3, 21)
)
if mibBuilder.loadTexts:
    sysSBusTable.setStatus("current")
_SysSBusEntry_Object = MibTableRow
sysSBusEntry = _SysSBusEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 3, 21, 1)
)
sysSBusEntry.setIndexNames(
    (0, "RAD-Dacs-MIB", "sysSBusPortIdx"),
)
if mibBuilder.loadTexts:
    sysSBusEntry.setStatus("current")
_SysSBusPortIdx_Type = Integer32
_SysSBusPortIdx_Object = MibTableColumn
sysSBusPortIdx = _SysSBusPortIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 3, 21, 1, 1),
    _SysSBusPortIdx_Type()
)
sysSBusPortIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSBusPortIdx.setStatus("current")


class _SysSBusStatus_Type(Integer32):
    """Custom type sysSBusStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("free", 1),
          ("physical", 2),
          ("virtual", 3))
    )


_SysSBusStatus_Type.__name__ = "Integer32"
_SysSBusStatus_Object = MibTableColumn
sysSBusStatus = _SysSBusStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 3, 21, 1, 2),
    _SysSBusStatus_Type()
)
sysSBusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSBusStatus.setStatus("current")
_SysSBusCapturePort_Type = Integer32
_SysSBusCapturePort_Object = MibTableColumn
sysSBusCapturePort = _SysSBusCapturePort_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 3, 21, 1, 3),
    _SysSBusCapturePort_Type()
)
sysSBusCapturePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSBusCapturePort.setStatus("current")
_SysSBusUtilization_Type = Integer32
_SysSBusUtilization_Object = MibTableColumn
sysSBusUtilization = _SysSBusUtilization_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 3, 21, 1, 4),
    _SysSBusUtilization_Type()
)
sysSBusUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSBusUtilization.setStatus("current")
_SysSRdnCmdTable_Object = MibTable
sysSRdnCmdTable = _SysSRdnCmdTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 3, 22)
)
if mibBuilder.loadTexts:
    sysSRdnCmdTable.setStatus("current")
_SysSRdnCmdEntry_Object = MibTableRow
sysSRdnCmdEntry = _SysSRdnCmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 3, 22, 1)
)
sysSRdnCmdEntry.setIndexNames(
    (0, "RAD-Dacs-MIB", "sysCRdnPrimeSlot"),
    (0, "RAD-Dacs-MIB", "sysCRdnPrimePort"),
)
if mibBuilder.loadTexts:
    sysSRdnCmdEntry.setStatus("current")


class _SysSRdnEnforcedChannel_Type(Integer32):
    """Custom type sysSRdnEnforcedChannel based on Integer32"""
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
        *(("notApplicable", 1),
          ("noEnforcement", 2),
          ("primary", 3),
          ("secondary", 4))
    )


_SysSRdnEnforcedChannel_Type.__name__ = "Integer32"
_SysSRdnEnforcedChannel_Object = MibTableColumn
sysSRdnEnforcedChannel = _SysSRdnEnforcedChannel_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 3, 22, 1, 1),
    _SysSRdnEnforcedChannel_Type()
)
sysSRdnEnforcedChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSRdnEnforcedChannel.setStatus("current")


class _SysSRdnLockFlip_Type(Integer32):
    """Custom type sysSRdnLockFlip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("off", 2),
          ("on", 3))
    )


_SysSRdnLockFlip_Type.__name__ = "Integer32"
_SysSRdnLockFlip_Object = MibTableColumn
sysSRdnLockFlip = _SysSRdnLockFlip_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 3, 22, 1, 2),
    _SysSRdnLockFlip_Type()
)
sysSRdnLockFlip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSRdnLockFlip.setStatus("current")


class _SysSRdnManualFlip_Type(Integer32):
    """Custom type sysSRdnManualFlip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("off", 2),
          ("on", 3))
    )


_SysSRdnManualFlip_Type.__name__ = "Integer32"
_SysSRdnManualFlip_Object = MibTableColumn
sysSRdnManualFlip = _SysSRdnManualFlip_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 3, 22, 1, 3),
    _SysSRdnManualFlip_Type()
)
sysSRdnManualFlip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSRdnManualFlip.setStatus("current")
_SysSAlrAttrIndication_Type = Integer32
_SysSAlrAttrIndication_Object = MibScalar
sysSAlrAttrIndication = _SysSAlrAttrIndication_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 3, 23),
    _SysSAlrAttrIndication_Type()
)
sysSAlrAttrIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSAlrAttrIndication.setStatus("current")
_SysCurrentAlr_ObjectIdentity = ObjectIdentity
sysCurrentAlr = _SysCurrentAlr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 4)
)
_SysSAlrTable_Object = MibTable
sysSAlrTable = _SysSAlrTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    sysSAlrTable.setStatus("current")
_SysSAlrEntry_Object = MibTableRow
sysSAlrEntry = _SysSAlrEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 4, 1, 1)
)
sysSAlrEntry.setIndexNames(
    (0, "RAD-Dacs-MIB", "sysSAlrIdx"),
)
if mibBuilder.loadTexts:
    sysSAlrEntry.setStatus("current")
_SysSAlrIdx_Type = Integer32
_SysSAlrIdx_Object = MibTableColumn
sysSAlrIdx = _SysSAlrIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 4, 1, 1, 1),
    _SysSAlrIdx_Type()
)
sysSAlrIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSAlrIdx.setStatus("current")
_SysSAlrCode_Type = Integer32
_SysSAlrCode_Object = MibTableColumn
sysSAlrCode = _SysSAlrCode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 4, 1, 1, 2),
    _SysSAlrCode_Type()
)
sysSAlrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSAlrCode.setStatus("current")


class _SysSAlrState_Type(Integer32):
    """Custom type sysSAlrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("event", 3),
          ("minor", 4),
          ("major", 5),
          ("warning", 6),
          ("critical", 7))
    )


_SysSAlrState_Type.__name__ = "Integer32"
_SysSAlrState_Object = MibTableColumn
sysSAlrState = _SysSAlrState_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 4, 1, 1, 3),
    _SysSAlrState_Type()
)
sysSAlrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSAlrState.setStatus("current")


class _SysSAlarmMask_Type(Integer32):
    """Custom type sysSAlarmMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_SysSAlarmMask_Type.__name__ = "Integer32"
_SysSAlarmMask_Object = MibTableColumn
sysSAlarmMask = _SysSAlarmMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 4, 1, 1, 4),
    _SysSAlarmMask_Type()
)
sysSAlarmMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSAlarmMask.setStatus("current")


class _SysSAlarmInvert_Type(Integer32):
    """Custom type sysSAlarmInvert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_SysSAlarmInvert_Type.__name__ = "Integer32"
_SysSAlarmInvert_Object = MibTableColumn
sysSAlarmInvert = _SysSAlarmInvert_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 4, 1, 1, 5),
    _SysSAlarmInvert_Type()
)
sysSAlarmInvert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSAlarmInvert.setStatus("current")


class _SysSAlarmOnOff_Type(Integer32):
    """Custom type sysSAlarmOnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_SysSAlarmOnOff_Type.__name__ = "Integer32"
_SysSAlarmOnOff_Object = MibTableColumn
sysSAlarmOnOff = _SysSAlarmOnOff_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 4, 1, 1, 6),
    _SysSAlarmOnOff_Type()
)
sysSAlarmOnOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSAlarmOnOff.setStatus("current")
_SysSAlarmCounter_Type = Integer32
_SysSAlarmCounter_Object = MibTableColumn
sysSAlarmCounter = _SysSAlarmCounter_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 4, 1, 1, 7),
    _SysSAlarmCounter_Type()
)
sysSAlarmCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSAlarmCounter.setStatus("current")


class _SysSAlrClearCmd_Type(Integer32):
    """Custom type sysSAlrClearCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_SysSAlrClearCmd_Type.__name__ = "Integer32"
_SysSAlrClearCmd_Object = MibScalar
sysSAlrClearCmd = _SysSAlrClearCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 4, 2),
    _SysSAlrClearCmd_Type()
)
sysSAlrClearCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSAlrClearCmd.setStatus("current")


class _SysSAlrClearAllCmd_Type(Integer32):
    """Custom type sysSAlrClearAllCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_SysSAlrClearAllCmd_Type.__name__ = "Integer32"
_SysSAlrClearAllCmd_Object = MibScalar
sysSAlrClearAllCmd = _SysSAlrClearAllCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 4, 3),
    _SysSAlrClearAllCmd_Type()
)
sysSAlrClearAllCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSAlrClearAllCmd.setStatus("current")


class _SysSAlrMaskAll_Type(Integer32):
    """Custom type sysSAlrMaskAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_SysSAlrMaskAll_Type.__name__ = "Integer32"
_SysSAlrMaskAll_Object = MibScalar
sysSAlrMaskAll = _SysSAlrMaskAll_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 4, 4),
    _SysSAlrMaskAll_Type()
)
sysSAlrMaskAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSAlrMaskAll.setStatus("current")


class _SysSAlrMask_Type(OctetString):
    """Custom type sysSAlrMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_SysSAlrMask_Type.__name__ = "OctetString"
_SysSAlrMask_Object = MibScalar
sysSAlrMask = _SysSAlrMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 4, 5),
    _SysSAlrMask_Type()
)
sysSAlrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSAlrMask.setStatus("current")


class _SysSAlrDataUpdateCmd_Type(Integer32):
    """Custom type sysSAlrDataUpdateCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_SysSAlrDataUpdateCmd_Type.__name__ = "Integer32"
_SysSAlrDataUpdateCmd_Object = MibScalar
sysSAlrDataUpdateCmd = _SysSAlrDataUpdateCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 4, 6),
    _SysSAlrDataUpdateCmd_Type()
)
sysSAlrDataUpdateCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSAlrDataUpdateCmd.setStatus("current")
_SysBufferAlr_ObjectIdentity = ObjectIdentity
sysBufferAlr = _SysBufferAlr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 5)
)
_SysBufferAlrTable_Object = MibTable
sysBufferAlrTable = _SysBufferAlrTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 5, 1)
)
if mibBuilder.loadTexts:
    sysBufferAlrTable.setStatus("current")
_SysBufferAlrEntry_Object = MibTableRow
sysBufferAlrEntry = _SysBufferAlrEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 5, 1, 1)
)
sysBufferAlrEntry.setIndexNames(
    (0, "RAD-Dacs-MIB", "sysBufferAlrIdx"),
)
if mibBuilder.loadTexts:
    sysBufferAlrEntry.setStatus("current")
_SysBufferAlrIdx_Type = Integer32
_SysBufferAlrIdx_Object = MibTableColumn
sysBufferAlrIdx = _SysBufferAlrIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 5, 1, 1, 1),
    _SysBufferAlrIdx_Type()
)
sysBufferAlrIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBufferAlrIdx.setStatus("current")
_SysBufferAlrCode_Type = Integer32
_SysBufferAlrCode_Object = MibTableColumn
sysBufferAlrCode = _SysBufferAlrCode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 5, 1, 1, 2),
    _SysBufferAlrCode_Type()
)
sysBufferAlrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBufferAlrCode.setStatus("current")


class _SysBufferAlrState_Type(Integer32):
    """Custom type sysBufferAlrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("event", 3),
          ("minor", 4),
          ("major", 5),
          ("warning", 6),
          ("critical", 7))
    )


_SysBufferAlrState_Type.__name__ = "Integer32"
_SysBufferAlrState_Object = MibTableColumn
sysBufferAlrState = _SysBufferAlrState_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 5, 1, 1, 3),
    _SysBufferAlrState_Type()
)
sysBufferAlrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBufferAlrState.setStatus("current")


class _SysBufferAlrSlot_Type(Integer32):
    """Custom type sysBufferAlrSlot based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              120,
              255)
        )
    )
    namedValues = NamedValues(
        *(("psA", 1),
          ("psB", 2),
          ("clA", 3),
          ("clB", 4),
          ("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("io13", 17),
          ("io14", 18),
          ("io15", 19),
          ("local", 20),
          ("psC", 21),
          ("kmxPsA", 101),
          ("kmxPsB", 102),
          ("kmxMlA", 103),
          ("kmxMlB", 104),
          ("kmxCl", 105),
          ("kmxOpt", 106),
          ("kmxIO1", 107),
          ("kmxIO2", 108),
          ("kmxIO3", 109),
          ("kmxIO4", 110),
          ("kmxIO5", 111),
          ("kmxIO6", 112),
          ("kmxIO7", 113),
          ("kmxIO8", 114),
          ("kmxIO9", 115),
          ("kmxIO10", 116),
          ("kmxIO11", 117),
          ("kmxIO12", 118),
          ("remote", 120),
          ("notApplicable", 255))
    )


_SysBufferAlrSlot_Type.__name__ = "Integer32"
_SysBufferAlrSlot_Object = MibTableColumn
sysBufferAlrSlot = _SysBufferAlrSlot_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 5, 1, 1, 4),
    _SysBufferAlrSlot_Type()
)
sysBufferAlrSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBufferAlrSlot.setStatus("current")
_SysBufferAlrPort_Type = Integer32
_SysBufferAlrPort_Object = MibTableColumn
sysBufferAlrPort = _SysBufferAlrPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 5, 1, 1, 5),
    _SysBufferAlrPort_Type()
)
sysBufferAlrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBufferAlrPort.setStatus("current")


class _SysBufferAlrDate_Type(DisplayString):
    """Custom type sysBufferAlrDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysBufferAlrDate_Type.__name__ = "DisplayString"
_SysBufferAlrDate_Object = MibTableColumn
sysBufferAlrDate = _SysBufferAlrDate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 5, 1, 1, 6),
    _SysBufferAlrDate_Type()
)
sysBufferAlrDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBufferAlrDate.setStatus("current")


class _SysBufferAlrTime_Type(DisplayString):
    """Custom type sysBufferAlrTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysBufferAlrTime_Type.__name__ = "DisplayString"
_SysBufferAlrTime_Object = MibTableColumn
sysBufferAlrTime = _SysBufferAlrTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 5, 1, 1, 7),
    _SysBufferAlrTime_Type()
)
sysBufferAlrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBufferAlrTime.setStatus("current")
_SysBufferAlrUpTime_Type = TimeTicks
_SysBufferAlrUpTime_Object = MibTableColumn
sysBufferAlrUpTime = _SysBufferAlrUpTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 5, 1, 1, 8),
    _SysBufferAlrUpTime_Type()
)
sysBufferAlrUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBufferAlrUpTime.setStatus("current")
_SysBufferAlrInfo_Type = SnmpAdminString
_SysBufferAlrInfo_Object = MibTableColumn
sysBufferAlrInfo = _SysBufferAlrInfo_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 5, 1, 1, 9),
    _SysBufferAlrInfo_Type()
)
sysBufferAlrInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBufferAlrInfo.setStatus("current")


class _SysBufferAlrClearCmd_Type(Integer32):
    """Custom type sysBufferAlrClearCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_SysBufferAlrClearCmd_Type.__name__ = "Integer32"
_SysBufferAlrClearCmd_Object = MibScalar
sysBufferAlrClearCmd = _SysBufferAlrClearCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 5, 2),
    _SysBufferAlrClearCmd_Type()
)
sysBufferAlrClearCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysBufferAlrClearCmd.setStatus("current")
_SysConfig_ObjectIdentity = ObjectIdentity
sysConfig = _SysConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6)
)
_SysCClkSrcTable_Object = MibTable
sysCClkSrcTable = _SysCClkSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 1)
)
if mibBuilder.loadTexts:
    sysCClkSrcTable.setStatus("current")
_SysCClkSrcEntry_Object = MibTableRow
sysCClkSrcEntry = _SysCClkSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 1, 1)
)
sysCClkSrcEntry.setIndexNames(
    (0, "RAD-Dacs-MIB", "sysCClkCnfgIdx"),
    (0, "RAD-Dacs-MIB", "sysCClkSrcIdx"),
)
if mibBuilder.loadTexts:
    sysCClkSrcEntry.setStatus("current")


class _SysCClkCnfgIdx_Type(Integer32):
    """Custom type sysCClkCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SysCClkCnfgIdx_Type.__name__ = "Integer32"
_SysCClkCnfgIdx_Object = MibTableColumn
sysCClkCnfgIdx = _SysCClkCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 1, 1, 1),
    _SysCClkCnfgIdx_Type()
)
sysCClkCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCClkCnfgIdx.setStatus("current")


class _SysCClkSrcIdx_Type(Integer32):
    """Custom type sysCClkSrcIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("fallback", 2))
    )


_SysCClkSrcIdx_Type.__name__ = "Integer32"
_SysCClkSrcIdx_Object = MibTableColumn
sysCClkSrcIdx = _SysCClkSrcIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 1, 1, 2),
    _SysCClkSrcIdx_Type()
)
sysCClkSrcIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCClkSrcIdx.setStatus("current")


class _SysCClkSrcMode_Type(Integer32):
    """Custom type sysCClkSrcMode based on Integer32"""
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
              11,
              12,
              255)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("internal", 2),
          ("rxClk", 3),
          ("station", 4),
          ("lbt", 5),
          ("ntr", 6),
          ("adaptive", 7),
          ("stationB", 8),
          ("automatic", 9),
          ("system", 10),
          ("sSubSystem", 11),
          ("recovered", 12),
          ("notApplicable", 255))
    )


_SysCClkSrcMode_Type.__name__ = "Integer32"
_SysCClkSrcMode_Object = MibTableColumn
sysCClkSrcMode = _SysCClkSrcMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 1, 1, 3),
    _SysCClkSrcMode_Type()
)
sysCClkSrcMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCClkSrcMode.setStatus("current")
_SysCClkSrcPrt_Type = Integer32
_SysCClkSrcPrt_Object = MibTableColumn
sysCClkSrcPrt = _SysCClkSrcPrt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 1, 1, 4),
    _SysCClkSrcPrt_Type()
)
sysCClkSrcPrt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCClkSrcPrt.setStatus("current")


class _SysCClkStationFreq_Type(Integer32):
    """Custom type sysCClkStationFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("f1544Khz", 2),
          ("f2048Khz", 3))
    )


_SysCClkStationFreq_Type.__name__ = "Integer32"
_SysCClkStationFreq_Object = MibTableColumn
sysCClkStationFreq = _SysCClkStationFreq_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 1, 1, 5),
    _SysCClkStationFreq_Type()
)
sysCClkStationFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCClkStationFreq.setStatus("current")
_SysCClkRevertiveTimeout_Type = Integer32
_SysCClkRevertiveTimeout_Object = MibTableColumn
sysCClkRevertiveTimeout = _SysCClkRevertiveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 1, 1, 6),
    _SysCClkRevertiveTimeout_Type()
)
sysCClkRevertiveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCClkRevertiveTimeout.setStatus("current")


class _SysCClkStationIf_Type(Integer32):
    """Custom type sysCClkStationIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("g703", 2),
          ("rs422", 3),
          ("g703E1Unbalanced", 4),
          ("g703T1", 5),
          ("rs422T1", 6))
    )


_SysCClkStationIf_Type.__name__ = "Integer32"
_SysCClkStationIf_Object = MibTableColumn
sysCClkStationIf = _SysCClkStationIf_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 1, 1, 7),
    _SysCClkStationIf_Type()
)
sysCClkStationIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCClkStationIf.setStatus("current")


class _SysCClkStationCableMode_Type(Integer32):
    """Custom type sysCClkStationCableMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("normal", 2),
          ("yCable", 3))
    )


_SysCClkStationCableMode_Type.__name__ = "Integer32"
_SysCClkStationCableMode_Object = MibTableColumn
sysCClkStationCableMode = _SysCClkStationCableMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 1, 1, 8),
    _SysCClkStationCableMode_Type()
)
sysCClkStationCableMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCClkStationCableMode.setStatus("current")


class _SysCClkStationOutState_Type(Integer32):
    """Custom type sysCClkStationOutState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_SysCClkStationOutState_Type.__name__ = "Integer32"
_SysCClkStationOutState_Object = MibTableColumn
sysCClkStationOutState = _SysCClkStationOutState_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 1, 1, 9),
    _SysCClkStationOutState_Type()
)
sysCClkStationOutState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCClkStationOutState.setStatus("current")


class _SysCClkSsmBased_Type(Integer32):
    """Custom type sysCClkSsmBased based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("no", 2),
          ("yes", 3))
    )


_SysCClkSsmBased_Type.__name__ = "Integer32"
_SysCClkSsmBased_Object = MibTableColumn
sysCClkSsmBased = _SysCClkSsmBased_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 1, 1, 10),
    _SysCClkSsmBased_Type()
)
sysCClkSsmBased.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCClkSsmBased.setStatus("current")


class _SysCClkSSubsystemSlot_Type(Integer32):
    """Custom type sysCClkSSubsystemSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("clA", 3),
          ("clB", 4))
    )


_SysCClkSSubsystemSlot_Type.__name__ = "Integer32"
_SysCClkSSubsystemSlot_Object = MibTableColumn
sysCClkSSubsystemSlot = _SysCClkSSubsystemSlot_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 1, 1, 11),
    _SysCClkSSubsystemSlot_Type()
)
sysCClkSSubsystemSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCClkSSubsystemSlot.setStatus("current")
_SysCClkRecoveredID_Type = Unsigned32
_SysCClkRecoveredID_Object = MibTableColumn
sysCClkRecoveredID = _SysCClkRecoveredID_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 1, 1, 12),
    _SysCClkRecoveredID_Type()
)
sysCClkRecoveredID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCClkRecoveredID.setStatus("current")
_SysCnfgTable_Object = MibTable
sysCnfgTable = _SysCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 2)
)
if mibBuilder.loadTexts:
    sysCnfgTable.setStatus("current")
_SysCnfgEntry_Object = MibTableRow
sysCnfgEntry = _SysCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 2, 1)
)
sysCnfgEntry.setIndexNames(
    (0, "RAD-Dacs-MIB", "sysCnfgIdx"),
)
if mibBuilder.loadTexts:
    sysCnfgEntry.setStatus("current")
_SysCnfgIdx_Type = Integer32
_SysCnfgIdx_Object = MibTableColumn
sysCnfgIdx = _SysCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 2, 1, 1),
    _SysCnfgIdx_Type()
)
sysCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCnfgIdx.setStatus("current")


class _SysCMatrixMode_Type(Integer32):
    """Custom type sysCMatrixMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("bidirectional", 2),
          ("unidirectional", 3))
    )


_SysCMatrixMode_Type.__name__ = "Integer32"
_SysCMatrixMode_Object = MibTableColumn
sysCMatrixMode = _SysCMatrixMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 2, 1, 2),
    _SysCMatrixMode_Type()
)
sysCMatrixMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCMatrixMode.setStatus("current")


class _SysCIsdnFormat_Type(Integer32):
    """Custom type sysCIsdnFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("te", 2),
          ("nt", 3))
    )


_SysCIsdnFormat_Type.__name__ = "Integer32"
_SysCIsdnFormat_Object = MibTableColumn
sysCIsdnFormat = _SysCIsdnFormat_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 2, 1, 3),
    _SysCIsdnFormat_Type()
)
sysCIsdnFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCIsdnFormat.setStatus("current")


class _SysCRoutingOnEth_Type(Integer32):
    """Custom type sysCRoutingOnEth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("none", 2),
          ("proprietary", 3),
          ("rip2", 4),
          ("rip1", 5),
          ("rip1and2", 6))
    )


_SysCRoutingOnEth_Type.__name__ = "Integer32"
_SysCRoutingOnEth_Object = MibTableColumn
sysCRoutingOnEth = _SysCRoutingOnEth_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 2, 1, 4),
    _SysCRoutingOnEth_Type()
)
sysCRoutingOnEth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCRoutingOnEth.setStatus("current")


class _SysCAutoConfigEnable_Type(Integer32):
    """Custom type sysCAutoConfigEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("disable", 2),
          ("enable", 3))
    )


_SysCAutoConfigEnable_Type.__name__ = "Integer32"
_SysCAutoConfigEnable_Object = MibTableColumn
sysCAutoConfigEnable = _SysCAutoConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 2, 1, 5),
    _SysCAutoConfigEnable_Type()
)
sysCAutoConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCAutoConfigEnable.setStatus("current")


class _SysCIntTsAllocMode_Type(Integer32):
    """Custom type sysCIntTsAllocMode based on Integer32"""
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
        *(("notApplicable", 1),
          ("static", 2),
          ("dynamic", 3),
          ("staticOneToOne", 4))
    )


_SysCIntTsAllocMode_Type.__name__ = "Integer32"
_SysCIntTsAllocMode_Object = MibTableColumn
sysCIntTsAllocMode = _SysCIntTsAllocMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 2, 1, 6),
    _SysCIntTsAllocMode_Type()
)
sysCIntTsAllocMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCIntTsAllocMode.setStatus("current")


class _SysCBuPrimaryPort_Type(Integer32):
    """Custom type sysCBuPrimaryPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noBackup", 2),
          ("e1T1orSerial", 3),
          ("eth", 4))
    )


_SysCBuPrimaryPort_Type.__name__ = "Integer32"
_SysCBuPrimaryPort_Object = MibTableColumn
sysCBuPrimaryPort = _SysCBuPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 2, 1, 7),
    _SysCBuPrimaryPort_Type()
)
sysCBuPrimaryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCBuPrimaryPort.setStatus("current")


class _SysCEnableLanOverTdm_Type(Integer32):
    """Custom type sysCEnableLanOverTdm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("enableAll", 2),
          ("enableVoiceOnly", 3),
          ("enableVoiceAndMng", 4))
    )


_SysCEnableLanOverTdm_Type.__name__ = "Integer32"
_SysCEnableLanOverTdm_Object = MibTableColumn
sysCEnableLanOverTdm = _SysCEnableLanOverTdm_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 2, 1, 8),
    _SysCEnableLanOverTdm_Type()
)
sysCEnableLanOverTdm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCEnableLanOverTdm.setStatus("current")
_SysCSs7FisuSuppression_Type = Integer32
_SysCSs7FisuSuppression_Object = MibTableColumn
sysCSs7FisuSuppression = _SysCSs7FisuSuppression_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 2, 1, 9),
    _SysCSs7FisuSuppression_Type()
)
sysCSs7FisuSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCSs7FisuSuppression.setStatus("current")


class _SysCBuRecMode_Type(Integer32):
    """Custom type sysCBuRecMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("manual", 3))
    )


_SysCBuRecMode_Type.__name__ = "Integer32"
_SysCBuRecMode_Object = MibTableColumn
sysCBuRecMode = _SysCBuRecMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 2, 1, 10),
    _SysCBuRecMode_Type()
)
sysCBuRecMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCBuRecMode.setStatus("current")
_SysCRdnTable_Object = MibTable
sysCRdnTable = _SysCRdnTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 3)
)
if mibBuilder.loadTexts:
    sysCRdnTable.setStatus("current")
_SysCRdnEntry_Object = MibTableRow
sysCRdnEntry = _SysCRdnEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 3, 1)
)
sysCRdnEntry.setIndexNames(
    (0, "RAD-Dacs-MIB", "sysCRdnCnfgIdx"),
    (0, "RAD-Dacs-MIB", "sysCRdnPrimeSlot"),
    (0, "RAD-Dacs-MIB", "sysCRdnPrimePort"),
)
if mibBuilder.loadTexts:
    sysCRdnEntry.setStatus("current")
_SysCRdnCnfgIdx_Type = Integer32
_SysCRdnCnfgIdx_Object = MibTableColumn
sysCRdnCnfgIdx = _SysCRdnCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 3, 1, 1),
    _SysCRdnCnfgIdx_Type()
)
sysCRdnCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCRdnCnfgIdx.setStatus("current")


class _SysCRdnPrimeSlot_Type(Integer32):
    """Custom type sysCRdnPrimeSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              255)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("io13", 17),
          ("io14", 18),
          ("io15", 19),
          ("notApplicable", 255))
    )


_SysCRdnPrimeSlot_Type.__name__ = "Integer32"
_SysCRdnPrimeSlot_Object = MibTableColumn
sysCRdnPrimeSlot = _SysCRdnPrimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 3, 1, 2),
    _SysCRdnPrimeSlot_Type()
)
sysCRdnPrimeSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCRdnPrimeSlot.setStatus("current")
_SysCRdnPrimePort_Type = Integer32
_SysCRdnPrimePort_Object = MibTableColumn
sysCRdnPrimePort = _SysCRdnPrimePort_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 3, 1, 3),
    _SysCRdnPrimePort_Type()
)
sysCRdnPrimePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCRdnPrimePort.setStatus("current")


class _SysCRdnSecSlot_Type(Integer32):
    """Custom type sysCRdnSecSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              255)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("io13", 17),
          ("io14", 18),
          ("io15", 19),
          ("notApplicable", 255))
    )


_SysCRdnSecSlot_Type.__name__ = "Integer32"
_SysCRdnSecSlot_Object = MibTableColumn
sysCRdnSecSlot = _SysCRdnSecSlot_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 3, 1, 4),
    _SysCRdnSecSlot_Type()
)
sysCRdnSecSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysCRdnSecSlot.setStatus("current")
_SysCRdnSecPort_Type = Integer32
_SysCRdnSecPort_Object = MibTableColumn
sysCRdnSecPort = _SysCRdnSecPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 3, 1, 5),
    _SysCRdnSecPort_Type()
)
sysCRdnSecPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysCRdnSecPort.setStatus("current")


class _SysCRdnMode_Type(Integer32):
    """Custom type sysCRdnMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("dualCableAIS", 2),
          ("yCable", 3),
          ("dualCableParallelTx", 4),
          ("backup", 5),
          ("singleSlotProtection", 6),
          ("onePlusOne", 7),
          ("oneToOne", 8),
          ("linkAggregation", 9),
          ("manual", 10),
          ("onePlusOneBid", 11),
          ("onePlusOneOpt", 12),
          ("ds0SncProtection", 13))
    )


_SysCRdnMode_Type.__name__ = "Integer32"
_SysCRdnMode_Object = MibTableColumn
sysCRdnMode = _SysCRdnMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 3, 1, 6),
    _SysCRdnMode_Type()
)
sysCRdnMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysCRdnMode.setStatus("current")


class _SysCRdnRecMode_Type(Integer32):
    """Custom type sysCRdnRecMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("manual", 3),
          ("nonRevertive", 4))
    )


_SysCRdnRecMode_Type.__name__ = "Integer32"
_SysCRdnRecMode_Object = MibTableColumn
sysCRdnRecMode = _SysCRdnRecMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 3, 1, 7),
    _SysCRdnRecMode_Type()
)
sysCRdnRecMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysCRdnRecMode.setStatus("current")
_SysCRdnRecTime_Type = Integer32
_SysCRdnRecTime_Object = MibTableColumn
sysCRdnRecTime = _SysCRdnRecTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 3, 1, 8),
    _SysCRdnRecTime_Type()
)
sysCRdnRecTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysCRdnRecTime.setStatus("current")


class _SysCRdnHwSwFlip_Type(Integer32):
    """Custom type sysCRdnHwSwFlip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("hw", 2),
          ("sw", 3))
    )


_SysCRdnHwSwFlip_Type.__name__ = "Integer32"
_SysCRdnHwSwFlip_Object = MibTableColumn
sysCRdnHwSwFlip = _SysCRdnHwSwFlip_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 3, 1, 9),
    _SysCRdnHwSwFlip_Type()
)
sysCRdnHwSwFlip.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysCRdnHwSwFlip.setStatus("current")
_SysCRdnRowStatus_Type = RowStatus
_SysCRdnRowStatus_Object = MibTableColumn
sysCRdnRowStatus = _SysCRdnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 3, 1, 10),
    _SysCRdnRowStatus_Type()
)
sysCRdnRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysCRdnRowStatus.setStatus("current")


class _SysCRdnOnline_Type(Integer32):
    """Custom type sysCRdnOnline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("primary", 2),
          ("secondary", 3))
    )


_SysCRdnOnline_Type.__name__ = "Integer32"
_SysCRdnOnline_Object = MibTableColumn
sysCRdnOnline = _SysCRdnOnline_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 3, 1, 11),
    _SysCRdnOnline_Type()
)
sysCRdnOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCRdnOnline.setStatus("current")


class _SysCRdnSwitchingMode_Type(Integer32):
    """Custom type sysCRdnSwitchingMode based on Integer32"""
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
        *(("notApplicable", 1),
          ("biDirectional", 2),
          ("uniDirectional", 3),
          ("linkAggregation", 4))
    )


_SysCRdnSwitchingMode_Type.__name__ = "Integer32"
_SysCRdnSwitchingMode_Object = MibTableColumn
sysCRdnSwitchingMode = _SysCRdnSwitchingMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 3, 1, 12),
    _SysCRdnSwitchingMode_Type()
)
sysCRdnSwitchingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysCRdnSwitchingMode.setStatus("current")
_SysCRdnFlipUponEvent_Type = Integer32
_SysCRdnFlipUponEvent_Object = MibTableColumn
sysCRdnFlipUponEvent = _SysCRdnFlipUponEvent_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 3, 1, 13),
    _SysCRdnFlipUponEvent_Type()
)
sysCRdnFlipUponEvent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysCRdnFlipUponEvent.setStatus("current")
_SysCRdnLosOrLofTime_Type = Integer32
_SysCRdnLosOrLofTime_Object = MibTableColumn
sysCRdnLosOrLofTime = _SysCRdnLosOrLofTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 3, 1, 14),
    _SysCRdnLosOrLofTime_Type()
)
sysCRdnLosOrLofTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysCRdnLosOrLofTime.setStatus("current")
_SysCRdnEventsTimeWindow_Type = Integer32
_SysCRdnEventsTimeWindow_Object = MibTableColumn
sysCRdnEventsTimeWindow = _SysCRdnEventsTimeWindow_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 3, 1, 15),
    _SysCRdnEventsTimeWindow_Type()
)
sysCRdnEventsTimeWindow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysCRdnEventsTimeWindow.setStatus("current")
_SysCRdnSequenceNumberThreshold_Type = Integer32
_SysCRdnSequenceNumberThreshold_Object = MibTableColumn
sysCRdnSequenceNumberThreshold = _SysCRdnSequenceNumberThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 3, 1, 16),
    _SysCRdnSequenceNumberThreshold_Type()
)
sysCRdnSequenceNumberThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysCRdnSequenceNumberThreshold.setStatus("current")
_SysCRdnBufferErrorsThreshold_Type = Integer32
_SysCRdnBufferErrorsThreshold_Object = MibTableColumn
sysCRdnBufferErrorsThreshold = _SysCRdnBufferErrorsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 3, 1, 17),
    _SysCRdnBufferErrorsThreshold_Type()
)
sysCRdnBufferErrorsThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysCRdnBufferErrorsThreshold.setStatus("current")
_SysCRdnBuffUnderrunTime_Type = Integer32
_SysCRdnBuffUnderrunTime_Object = MibTableColumn
sysCRdnBuffUnderrunTime = _SysCRdnBuffUnderrunTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 3, 1, 18),
    _SysCRdnBuffUnderrunTime_Type()
)
sysCRdnBuffUnderrunTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysCRdnBuffUnderrunTime.setStatus("current")


class _SysCRdnPrimePriority_Type(Integer32):
    """Custom type sysCRdnPrimePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("low", 2),
          ("high", 3))
    )


_SysCRdnPrimePriority_Type.__name__ = "Integer32"
_SysCRdnPrimePriority_Object = MibTableColumn
sysCRdnPrimePriority = _SysCRdnPrimePriority_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 3, 1, 19),
    _SysCRdnPrimePriority_Type()
)
sysCRdnPrimePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysCRdnPrimePriority.setStatus("current")


class _SysCRdnSecPriority_Type(Integer32):
    """Custom type sysCRdnSecPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("low", 2),
          ("high", 3))
    )


_SysCRdnSecPriority_Type.__name__ = "Integer32"
_SysCRdnSecPriority_Object = MibTableColumn
sysCRdnSecPriority = _SysCRdnSecPriority_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 3, 1, 20),
    _SysCRdnSecPriority_Type()
)
sysCRdnSecPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysCRdnSecPriority.setStatus("current")
_SysCRdnWTR_Type = Unsigned32
_SysCRdnWTR_Object = MibTableColumn
sysCRdnWTR = _SysCRdnWTR_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 3, 1, 21),
    _SysCRdnWTR_Type()
)
sysCRdnWTR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysCRdnWTR.setStatus("current")
_SysCRdnName_Type = SnmpAdminString
_SysCRdnName_Object = MibTableColumn
sysCRdnName = _SysCRdnName_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 3, 1, 22),
    _SysCRdnName_Type()
)
sysCRdnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysCRdnName.setStatus("current")


class _SysCRdnTxDownDurationUponFlip_Type(Unsigned32):
    """Custom type sysCRdnTxDownDurationUponFlip based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_SysCRdnTxDownDurationUponFlip_Type.__name__ = "Unsigned32"
_SysCRdnTxDownDurationUponFlip_Object = MibTableColumn
sysCRdnTxDownDurationUponFlip = _SysCRdnTxDownDurationUponFlip_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 6, 3, 1, 23),
    _SysCRdnTxDownDurationUponFlip_Type()
)
sysCRdnTxDownDurationUponFlip.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysCRdnTxDownDurationUponFlip.setStatus("current")
_SysDbase_ObjectIdentity = ObjectIdentity
sysDbase = _SysDbase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 7)
)


class _SysDbaseSanityCheckCmd_Type(Integer32):
    """Custom type sysDbaseSanityCheckCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_SysDbaseSanityCheckCmd_Type.__name__ = "Integer32"
_SysDbaseSanityCheckCmd_Object = MibScalar
sysDbaseSanityCheckCmd = _SysDbaseSanityCheckCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 7, 1),
    _SysDbaseSanityCheckCmd_Type()
)
sysDbaseSanityCheckCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDbaseSanityCheckCmd.setStatus("current")


class _SysDbaseDownloadCnfgIdxCmd_Type(Integer32):
    """Custom type sysDbaseDownloadCnfgIdxCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SysDbaseDownloadCnfgIdxCmd_Type.__name__ = "Integer32"
_SysDbaseDownloadCnfgIdxCmd_Object = MibScalar
sysDbaseDownloadCnfgIdxCmd = _SysDbaseDownloadCnfgIdxCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 7, 2),
    _SysDbaseDownloadCnfgIdxCmd_Type()
)
sysDbaseDownloadCnfgIdxCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDbaseDownloadCnfgIdxCmd.setStatus("current")


class _SysDbaseUploadCnfgIdxCmd_Type(Integer32):
    """Custom type sysDbaseUploadCnfgIdxCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SysDbaseUploadCnfgIdxCmd_Type.__name__ = "Integer32"
_SysDbaseUploadCnfgIdxCmd_Object = MibScalar
sysDbaseUploadCnfgIdxCmd = _SysDbaseUploadCnfgIdxCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 7, 3),
    _SysDbaseUploadCnfgIdxCmd_Type()
)
sysDbaseUploadCnfgIdxCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDbaseUploadCnfgIdxCmd.setStatus("current")
_SysDbaseFlipTable_Object = MibTable
sysDbaseFlipTable = _SysDbaseFlipTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 7, 4)
)
if mibBuilder.loadTexts:
    sysDbaseFlipTable.setStatus("current")
_SysDbaseFlipEntry_Object = MibTableRow
sysDbaseFlipEntry = _SysDbaseFlipEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 7, 4, 1)
)
sysDbaseFlipEntry.setIndexNames(
    (0, "RAD-Dacs-MIB", "sysDbaseFlipIdx"),
)
if mibBuilder.loadTexts:
    sysDbaseFlipEntry.setStatus("current")


class _SysDbaseFlipIdx_Type(Integer32):
    """Custom type sysDbaseFlipIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SysDbaseFlipIdx_Type.__name__ = "Integer32"
_SysDbaseFlipIdx_Object = MibTableColumn
sysDbaseFlipIdx = _SysDbaseFlipIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 7, 4, 1, 1),
    _SysDbaseFlipIdx_Type()
)
sysDbaseFlipIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDbaseFlipIdx.setStatus("current")


class _SysDbaseFlipTime_Type(DisplayString):
    """Custom type sysDbaseFlipTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysDbaseFlipTime_Type.__name__ = "DisplayString"
_SysDbaseFlipTime_Object = MibTableColumn
sysDbaseFlipTime = _SysDbaseFlipTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 7, 4, 1, 2),
    _SysDbaseFlipTime_Type()
)
sysDbaseFlipTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDbaseFlipTime.setStatus("current")


class _SysDbaseFlipActivation_Type(Integer32):
    """Custom type sysDbaseFlipActivation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_SysDbaseFlipActivation_Type.__name__ = "Integer32"
_SysDbaseFlipActivation_Object = MibTableColumn
sysDbaseFlipActivation = _SysDbaseFlipActivation_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 1, 7, 4, 1, 3),
    _SysDbaseFlipActivation_Type()
)
sysDbaseFlipActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDbaseFlipActivation.setStatus("current")
_MdlDacsMux_ObjectIdentity = ObjectIdentity
mdlDacsMux = _MdlDacsMux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2)
)
_MdlGen_ObjectIdentity = ObjectIdentity
mdlGen = _MdlGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1)
)
_CardEvents_ObjectIdentity = ObjectIdentity
cardEvents = _CardEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 0)
)
_MdlSTable_Object = MibTable
mdlSTable = _MdlSTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    mdlSTable.setStatus("current")
_MdlSEntry_Object = MibTableRow
mdlSEntry = _MdlSEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 1, 1)
)
mdlSEntry.setIndexNames(
    (0, "RAD-Dacs-MIB", "mdlSSltIdx"),
)
if mibBuilder.loadTexts:
    mdlSEntry.setStatus("current")
_MdlSSltIdx_Type = SlotType
_MdlSSltIdx_Object = MibTableColumn
mdlSSltIdx = _MdlSSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 1, 1, 1),
    _MdlSSltIdx_Type()
)
mdlSSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlSSltIdx.setStatus("current")
_MdlSCardType_Type = CardType
_MdlSCardType_Object = MibTableColumn
mdlSCardType = _MdlSCardType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 1, 1, 2),
    _MdlSCardType_Type()
)
mdlSCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlSCardType.setStatus("current")


class _MdlSHwVer_Type(DisplayString):
    """Custom type mdlSHwVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MdlSHwVer_Type.__name__ = "DisplayString"
_MdlSHwVer_Object = MibTableColumn
mdlSHwVer = _MdlSHwVer_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 1, 1, 3),
    _MdlSHwVer_Type()
)
mdlSHwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlSHwVer.setStatus("current")


class _MdlSSwVer_Type(DisplayString):
    """Custom type mdlSSwVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MdlSSwVer_Type.__name__ = "DisplayString"
_MdlSSwVer_Object = MibTableColumn
mdlSSwVer = _MdlSSwVer_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 1, 1, 4),
    _MdlSSwVer_Type()
)
mdlSSwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlSSwVer.setStatus("current")


class _MdlSAlarmStatus_Type(Integer32):
    """Custom type mdlSAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("major", 3),
          ("minor", 4),
          ("event", 5),
          ("warning", 6),
          ("critical", 7))
    )


_MdlSAlarmStatus_Type.__name__ = "Integer32"
_MdlSAlarmStatus_Object = MibTableColumn
mdlSAlarmStatus = _MdlSAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 1, 1, 5),
    _MdlSAlarmStatus_Type()
)
mdlSAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlSAlarmStatus.setStatus("current")


class _MdlSAlarmStatusAll_Type(Integer32):
    """Custom type mdlSAlarmStatusAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("major", 3),
          ("minor", 4),
          ("event", 5),
          ("warning", 6),
          ("critical", 7))
    )


_MdlSAlarmStatusAll_Type.__name__ = "Integer32"
_MdlSAlarmStatusAll_Object = MibTableColumn
mdlSAlarmStatusAll = _MdlSAlarmStatusAll_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 1, 1, 6),
    _MdlSAlarmStatusAll_Type()
)
mdlSAlarmStatusAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlSAlarmStatusAll.setStatus("current")


class _MdlSTestStatus_Type(Integer32):
    """Custom type mdlSTestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_MdlSTestStatus_Type.__name__ = "Integer32"
_MdlSTestStatus_Object = MibTableColumn
mdlSTestStatus = _MdlSTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 1, 1, 7),
    _MdlSTestStatus_Type()
)
mdlSTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlSTestStatus.setStatus("current")


class _MdlSHwStatus_Type(Integer32):
    """Custom type mdlSHwStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("ok", 3))
    )


_MdlSHwStatus_Type.__name__ = "Integer32"
_MdlSHwStatus_Object = MibTableColumn
mdlSHwStatus = _MdlSHwStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 1, 1, 8),
    _MdlSHwStatus_Type()
)
mdlSHwStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlSHwStatus.setStatus("current")


class _MdlSActivity_Type(Integer32):
    """Custom type mdlSActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("offline", 2),
          ("online", 3))
    )


_MdlSActivity_Type.__name__ = "Integer32"
_MdlSActivity_Object = MibTableColumn
mdlSActivity = _MdlSActivity_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 1, 1, 9),
    _MdlSActivity_Type()
)
mdlSActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlSActivity.setStatus("current")


class _MdlSAlrClearCmd_Type(Integer32):
    """Custom type mdlSAlrClearCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_MdlSAlrClearCmd_Type.__name__ = "Integer32"
_MdlSAlrClearCmd_Object = MibTableColumn
mdlSAlrClearCmd = _MdlSAlrClearCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 1, 1, 10),
    _MdlSAlrClearCmd_Type()
)
mdlSAlrClearCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdlSAlrClearCmd.setStatus("current")


class _MdlSAlrClearAllCmd_Type(Integer32):
    """Custom type mdlSAlrClearAllCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_MdlSAlrClearAllCmd_Type.__name__ = "Integer32"
_MdlSAlrClearAllCmd_Object = MibTableColumn
mdlSAlrClearAllCmd = _MdlSAlrClearAllCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 1, 1, 11),
    _MdlSAlrClearAllCmd_Type()
)
mdlSAlrClearAllCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdlSAlrClearAllCmd.setStatus("current")


class _MdlSAlrMaskAll_Type(Integer32):
    """Custom type mdlSAlrMaskAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_MdlSAlrMaskAll_Type.__name__ = "Integer32"
_MdlSAlrMaskAll_Object = MibTableColumn
mdlSAlrMaskAll = _MdlSAlrMaskAll_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 1, 1, 12),
    _MdlSAlrMaskAll_Type()
)
mdlSAlrMaskAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdlSAlrMaskAll.setStatus("current")
_MdlSCmd_Type = Integer32
_MdlSCmd_Object = MibTableColumn
mdlSCmd = _MdlSCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 1, 1, 13),
    _MdlSCmd_Type()
)
mdlSCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdlSCmd.setStatus("current")


class _MdlSReset_Type(Integer32):
    """Custom type mdlSReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_MdlSReset_Type.__name__ = "Integer32"
_MdlSReset_Object = MibTableColumn
mdlSReset = _MdlSReset_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 1, 1, 14),
    _MdlSReset_Type()
)
mdlSReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdlSReset.setStatus("current")


class _MdlSRebuildFrame_Type(Integer32):
    """Custom type mdlSRebuildFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("off", 2),
          ("on", 3))
    )


_MdlSRebuildFrame_Type.__name__ = "Integer32"
_MdlSRebuildFrame_Object = MibTableColumn
mdlSRebuildFrame = _MdlSRebuildFrame_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 1, 1, 15),
    _MdlSRebuildFrame_Type()
)
mdlSRebuildFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdlSRebuildFrame.setStatus("current")


class _MdlSBackupSwVer_Type(DisplayString):
    """Custom type mdlSBackupSwVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MdlSBackupSwVer_Type.__name__ = "DisplayString"
_MdlSBackupSwVer_Object = MibTableColumn
mdlSBackupSwVer = _MdlSBackupSwVer_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 1, 1, 16),
    _MdlSBackupSwVer_Type()
)
mdlSBackupSwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlSBackupSwVer.setStatus("current")


class _MdlSSecondaryBackupSwVer_Type(DisplayString):
    """Custom type mdlSSecondaryBackupSwVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MdlSSecondaryBackupSwVer_Type.__name__ = "DisplayString"
_MdlSSecondaryBackupSwVer_Object = MibTableColumn
mdlSSecondaryBackupSwVer = _MdlSSecondaryBackupSwVer_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 1, 1, 17),
    _MdlSSecondaryBackupSwVer_Type()
)
mdlSSecondaryBackupSwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlSSecondaryBackupSwVer.setStatus("current")


class _MdlSPiggybackVer_Type(SnmpAdminString):
    """Custom type mdlSPiggybackVer based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MdlSPiggybackVer_Type.__name__ = "SnmpAdminString"
_MdlSPiggybackVer_Object = MibTableColumn
mdlSPiggybackVer = _MdlSPiggybackVer_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 1, 1, 18),
    _MdlSPiggybackVer_Type()
)
mdlSPiggybackVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlSPiggybackVer.setStatus("current")
_MdlCTable_Object = MibTable
mdlCTable = _MdlCTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 2)
)
if mibBuilder.loadTexts:
    mdlCTable.setStatus("current")
_MdlCEntry_Object = MibTableRow
mdlCEntry = _MdlCEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 2, 1)
)
mdlCEntry.setIndexNames(
    (0, "RAD-Dacs-MIB", "mdlCConfigIdx"),
    (0, "RAD-Dacs-MIB", "mdlCSlotIdx"),
)
if mibBuilder.loadTexts:
    mdlCEntry.setStatus("current")


class _MdlCConfigIdx_Type(Integer32):
    """Custom type mdlCConfigIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MdlCConfigIdx_Type.__name__ = "Integer32"
_MdlCConfigIdx_Object = MibTableColumn
mdlCConfigIdx = _MdlCConfigIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 2, 1, 1),
    _MdlCConfigIdx_Type()
)
mdlCConfigIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlCConfigIdx.setStatus("current")
_MdlCSlotIdx_Type = SlotType
_MdlCSlotIdx_Object = MibTableColumn
mdlCSlotIdx = _MdlCSlotIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 2, 1, 2),
    _MdlCSlotIdx_Type()
)
mdlCSlotIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlCSlotIdx.setStatus("current")
_MdlCProgCardType_Type = CardType
_MdlCProgCardType_Object = MibTableColumn
mdlCProgCardType = _MdlCProgCardType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 2, 1, 3),
    _MdlCProgCardType_Type()
)
mdlCProgCardType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdlCProgCardType.setStatus("current")
_MdlCNoOfExtPrt_Type = Integer32
_MdlCNoOfExtPrt_Object = MibTableColumn
mdlCNoOfExtPrt = _MdlCNoOfExtPrt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 2, 1, 4),
    _MdlCNoOfExtPrt_Type()
)
mdlCNoOfExtPrt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlCNoOfExtPrt.setStatus("current")
_MdlCNoOfIntPrt_Type = Integer32
_MdlCNoOfIntPrt_Object = MibTableColumn
mdlCNoOfIntPrt = _MdlCNoOfIntPrt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 2, 1, 5),
    _MdlCNoOfIntPrt_Type()
)
mdlCNoOfIntPrt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlCNoOfIntPrt.setStatus("current")
_MdlCParam_Type = Integer32
_MdlCParam_Object = MibTableColumn
mdlCParam = _MdlCParam_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 2, 1, 6),
    _MdlCParam_Type()
)
mdlCParam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdlCParam.setStatus("current")


class _MdlCAdminStatus_Type(Integer32):
    """Custom type mdlCAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_MdlCAdminStatus_Type.__name__ = "Integer32"
_MdlCAdminStatus_Object = MibTableColumn
mdlCAdminStatus = _MdlCAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 2, 1, 7),
    _MdlCAdminStatus_Type()
)
mdlCAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdlCAdminStatus.setStatus("current")
_MdlCActualCardType_Type = CardType
_MdlCActualCardType_Object = MibTableColumn
mdlCActualCardType = _MdlCActualCardType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 2, 1, 8),
    _MdlCActualCardType_Type()
)
mdlCActualCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlCActualCardType.setStatus("current")


class _MdlCOperStatus_Type(Integer32):
    """Custom type mdlCOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("notPresent", 3))
    )


_MdlCOperStatus_Type.__name__ = "Integer32"
_MdlCOperStatus_Object = MibTableColumn
mdlCOperStatus = _MdlCOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 2, 1, 9),
    _MdlCOperStatus_Type()
)
mdlCOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlCOperStatus.setStatus("current")


class _MdlCDetailedStatus_Type(Bits):
    """Custom type mdlCDetailedStatus based on Bits"""
    namedValues = NamedValues(
        *(("initializing", 0),
          ("cardMismatch", 1),
          ("initFailed", 2),
          ("provisionFailed", 3),
          ("selfTestFailed", 4),
          ("commFailure", 5),
          ("bpInterfaceFailure", 6),
          ("configurationMismatch", 7),
          ("noInputPower", 8))
    )

_MdlCDetailedStatus_Type.__name__ = "Bits"
_MdlCDetailedStatus_Object = MibTableColumn
mdlCDetailedStatus = _MdlCDetailedStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 2, 1, 10),
    _MdlCDetailedStatus_Type()
)
mdlCDetailedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlCDetailedStatus.setStatus("current")
_MdlCEntPhysicalIndex_Type = PhysicalIndexOrZero
_MdlCEntPhysicalIndex_Object = MibTableColumn
mdlCEntPhysicalIndex = _MdlCEntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 2, 1, 11),
    _MdlCEntPhysicalIndex_Type()
)
mdlCEntPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlCEntPhysicalIndex.setStatus("current")


class _MdlCReset_Type(Integer32):
    """Custom type mdlCReset based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_MdlCReset_Type.__name__ = "Integer32"
_MdlCReset_Object = MibTableColumn
mdlCReset = _MdlCReset_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 2, 1, 12),
    _MdlCReset_Type()
)
mdlCReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdlCReset.setStatus("current")


class _MdlCConfigMismatchReason_Type(Integer32):
    """Custom type mdlCConfigMismatchReason based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("s128KbpsInSynchronousMode", 1),
          ("s14k4KbpsConfiguration", 2),
          ("s28k8KbpsConfiguration", 3),
          ("s48KbpsConfiguration", 4),
          ("s56KbpsInSynchronousMode", 5),
          ("s7k2KbpsConfiguration", 6),
          ("adpcmConfiguration", 7),
          ("dceOnDteHwInSynchronousMode", 8),
          ("dteOnDceHwInSynchronousMode", 9),
          ("rlbLlbInV110RateAdaptation", 10),
          ("swNotSupportingAdvancedSignaling", 11),
          ("signalingConfiguration", 12),
          ("stratum1WithoutOcxo", 13),
          ("stratum2WithoutOcxo", 14),
          ("useOf4TdmBusesInChassis", 15),
          ("winkStartModeConfiguration", 16),
          ("other", 2147483647))
    )


_MdlCConfigMismatchReason_Type.__name__ = "Integer32"
_MdlCConfigMismatchReason_Object = MibTableColumn
mdlCConfigMismatchReason = _MdlCConfigMismatchReason_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 2, 1, 13),
    _MdlCConfigMismatchReason_Type()
)
mdlCConfigMismatchReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlCConfigMismatchReason.setStatus("current")
_MdlCIpAddressType_Type = InetAddressType
_MdlCIpAddressType_Object = MibTableColumn
mdlCIpAddressType = _MdlCIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 2, 1, 14),
    _MdlCIpAddressType_Type()
)
mdlCIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdlCIpAddressType.setStatus("current")
_MdlCIpAddress_Type = InetAddress
_MdlCIpAddress_Object = MibTableColumn
mdlCIpAddress = _MdlCIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 2, 1, 15),
    _MdlCIpAddress_Type()
)
mdlCIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdlCIpAddress.setStatus("current")


class _MdlCHardwareFailureReason_Type(Integer32):
    """Custom type mdlCHardwareFailureReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("ringerVoltageFailure", 2),
          ("fanFailure", 3))
    )


_MdlCHardwareFailureReason_Type.__name__ = "Integer32"
_MdlCHardwareFailureReason_Object = MibTableColumn
mdlCHardwareFailureReason = _MdlCHardwareFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 2, 1, 16),
    _MdlCHardwareFailureReason_Type()
)
mdlCHardwareFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlCHardwareFailureReason.setStatus("current")


class _MdlCFanControl_Type(Integer32):
    """Custom type mdlCFanControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_MdlCFanControl_Type.__name__ = "Integer32"
_MdlCFanControl_Object = MibTableColumn
mdlCFanControl = _MdlCFanControl_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 2, 1, 22),
    _MdlCFanControl_Type()
)
mdlCFanControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdlCFanControl.setStatus("current")


class _MdlCFanOperStatus_Type(Integer32):
    """Custom type mdlCFanOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("notPresent", 3))
    )


_MdlCFanOperStatus_Type.__name__ = "Integer32"
_MdlCFanOperStatus_Object = MibTableColumn
mdlCFanOperStatus = _MdlCFanOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 2, 1, 23),
    _MdlCFanOperStatus_Type()
)
mdlCFanOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlCFanOperStatus.setStatus("current")
_MdlAlr_ObjectIdentity = ObjectIdentity
mdlAlr = _MdlAlr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 3)
)
_MdlAlrTable_Object = MibTable
mdlAlrTable = _MdlAlrTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    mdlAlrTable.setStatus("current")
_MdlAlrEntry_Object = MibTableRow
mdlAlrEntry = _MdlAlrEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 3, 1, 1)
)
mdlAlrEntry.setIndexNames(
    (0, "RAD-Dacs-MIB", "mdlAlrSltIdx"),
    (0, "RAD-Dacs-MIB", "mdlAlrIdx"),
)
if mibBuilder.loadTexts:
    mdlAlrEntry.setStatus("current")
_MdlAlrIdx_Type = Integer32
_MdlAlrIdx_Object = MibTableColumn
mdlAlrIdx = _MdlAlrIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 3, 1, 1, 1),
    _MdlAlrIdx_Type()
)
mdlAlrIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlAlrIdx.setStatus("current")
_MdlAlrSltIdx_Type = SlotType
_MdlAlrSltIdx_Object = MibTableColumn
mdlAlrSltIdx = _MdlAlrSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 3, 1, 1, 2),
    _MdlAlrSltIdx_Type()
)
mdlAlrSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlAlrSltIdx.setStatus("current")
_MdlAlrCode_Type = Integer32
_MdlAlrCode_Object = MibTableColumn
mdlAlrCode = _MdlAlrCode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 3, 1, 1, 3),
    _MdlAlrCode_Type()
)
mdlAlrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlAlrCode.setStatus("current")


class _MdlAlrState_Type(Integer32):
    """Custom type mdlAlrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("event", 3),
          ("minor", 4),
          ("major", 5),
          ("warning", 6),
          ("critical", 7))
    )


_MdlAlrState_Type.__name__ = "Integer32"
_MdlAlrState_Object = MibTableColumn
mdlAlrState = _MdlAlrState_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 3, 1, 1, 4),
    _MdlAlrState_Type()
)
mdlAlrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlAlrState.setStatus("current")


class _MdlAlarmMask_Type(Integer32):
    """Custom type mdlAlarmMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_MdlAlarmMask_Type.__name__ = "Integer32"
_MdlAlarmMask_Object = MibTableColumn
mdlAlarmMask = _MdlAlarmMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 3, 1, 1, 5),
    _MdlAlarmMask_Type()
)
mdlAlarmMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlAlarmMask.setStatus("current")


class _MdlAlarmInvert_Type(Integer32):
    """Custom type mdlAlarmInvert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_MdlAlarmInvert_Type.__name__ = "Integer32"
_MdlAlarmInvert_Object = MibTableColumn
mdlAlarmInvert = _MdlAlarmInvert_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 3, 1, 1, 6),
    _MdlAlarmInvert_Type()
)
mdlAlarmInvert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlAlarmInvert.setStatus("current")


class _MdlAlarmOnOff_Type(Integer32):
    """Custom type mdlAlarmOnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_MdlAlarmOnOff_Type.__name__ = "Integer32"
_MdlAlarmOnOff_Object = MibTableColumn
mdlAlarmOnOff = _MdlAlarmOnOff_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 3, 1, 1, 7),
    _MdlAlarmOnOff_Type()
)
mdlAlarmOnOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlAlarmOnOff.setStatus("current")
_MdlAlarmCounter_Type = Integer32
_MdlAlarmCounter_Object = MibTableColumn
mdlAlarmCounter = _MdlAlarmCounter_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 3, 1, 1, 8),
    _MdlAlarmCounter_Type()
)
mdlAlarmCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlAlarmCounter.setStatus("current")
_MdlAlrMaskTable_Object = MibTable
mdlAlrMaskTable = _MdlAlrMaskTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    mdlAlrMaskTable.setStatus("current")
_MdlAlrMaskEntry_Object = MibTableRow
mdlAlrMaskEntry = _MdlAlrMaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 3, 2, 1)
)
mdlAlrMaskEntry.setIndexNames(
    (0, "RAD-Dacs-MIB", "mdlAlrMaskSltIdx"),
)
if mibBuilder.loadTexts:
    mdlAlrMaskEntry.setStatus("current")
_MdlAlrMaskSltIdx_Type = SlotType
_MdlAlrMaskSltIdx_Object = MibTableColumn
mdlAlrMaskSltIdx = _MdlAlrMaskSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 3, 2, 1, 1),
    _MdlAlrMaskSltIdx_Type()
)
mdlAlrMaskSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlAlrMaskSltIdx.setStatus("current")


class _MdlAlrMask_Type(OctetString):
    """Custom type mdlAlrMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 10),
    )


_MdlAlrMask_Type.__name__ = "OctetString"
_MdlAlrMask_Object = MibTableColumn
mdlAlrMask = _MdlAlrMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 3, 2, 1, 2),
    _MdlAlrMask_Type()
)
mdlAlrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdlAlrMask.setStatus("current")
_MdlCl_ObjectIdentity = ObjectIdentity
mdlCl = _MdlCl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 2)
)
_MdlClTable_Object = MibTable
mdlClTable = _MdlClTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mdlClTable.setStatus("current")
_MdlClEntry_Object = MibTableRow
mdlClEntry = _MdlClEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 2, 1, 1)
)
mdlClEntry.setIndexNames(
    (0, "RAD-Dacs-MIB", "mdlClIdx"),
)
if mibBuilder.loadTexts:
    mdlClEntry.setStatus("current")


class _MdlClIdx_Type(Integer32):
    """Custom type mdlClIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("clA", 3),
          ("clB", 4))
    )


_MdlClIdx_Type.__name__ = "Integer32"
_MdlClIdx_Object = MibTableColumn
mdlClIdx = _MdlClIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 2, 1, 1, 1),
    _MdlClIdx_Type()
)
mdlClIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlClIdx.setStatus("current")
_MdlClSwchStatus_Type = Integer32
_MdlClSwchStatus_Object = MibTableColumn
mdlClSwchStatus = _MdlClSwchStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 2, 1, 1, 2),
    _MdlClSwchStatus_Type()
)
mdlClSwchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlClSwchStatus.setStatus("current")


class _MdlClLastFlipDate_Type(DisplayString):
    """Custom type mdlClLastFlipDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MdlClLastFlipDate_Type.__name__ = "DisplayString"
_MdlClLastFlipDate_Object = MibTableColumn
mdlClLastFlipDate = _MdlClLastFlipDate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 2, 1, 1, 3),
    _MdlClLastFlipDate_Type()
)
mdlClLastFlipDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlClLastFlipDate.setStatus("current")


class _MdlClLastFlipTime_Type(DisplayString):
    """Custom type mdlClLastFlipTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MdlClLastFlipTime_Type.__name__ = "DisplayString"
_MdlClLastFlipTime_Object = MibTableColumn
mdlClLastFlipTime = _MdlClLastFlipTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 2, 1, 1, 4),
    _MdlClLastFlipTime_Type()
)
mdlClLastFlipTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlClLastFlipTime.setStatus("current")


class _MdlClLastFlipCause_Type(DisplayString):
    """Custom type mdlClLastFlipCause based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MdlClLastFlipCause_Type.__name__ = "DisplayString"
_MdlClLastFlipCause_Object = MibTableColumn
mdlClLastFlipCause = _MdlClLastFlipCause_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 2, 1, 1, 5),
    _MdlClLastFlipCause_Type()
)
mdlClLastFlipCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlClLastFlipCause.setStatus("current")
_MdlPs_ObjectIdentity = ObjectIdentity
mdlPs = _MdlPs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 3)
)
_MdlPsTable_Object = MibTable
mdlPsTable = _MdlPsTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 3, 1)
)
if mibBuilder.loadTexts:
    mdlPsTable.setStatus("current")
_MdlPsEntry_Object = MibTableRow
mdlPsEntry = _MdlPsEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 3, 1, 1)
)
mdlPsEntry.setIndexNames(
    (0, "RAD-Dacs-MIB", "mdlPsIdx"),
)
if mibBuilder.loadTexts:
    mdlPsEntry.setStatus("current")
_MdlPsIdx_Type = SlotType
_MdlPsIdx_Object = MibTableColumn
mdlPsIdx = _MdlPsIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 3, 1, 1, 1),
    _MdlPsIdx_Type()
)
mdlPsIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlPsIdx.setStatus("current")


class _MdlPsStatus_Type(Integer32):
    """Custom type mdlPsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 1),
          ("active", 2))
    )


_MdlPsStatus_Type.__name__ = "Integer32"
_MdlPsStatus_Object = MibTableColumn
mdlPsStatus = _MdlPsStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 3, 1, 1, 2),
    _MdlPsStatus_Type()
)
mdlPsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlPsStatus.setStatus("current")


class _MdlPsTestResult_Type(Integer32):
    """Custom type mdlPsTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("f12V", 2),
          ("f5V", 3),
          ("fMinus5V", 4),
          ("fFanVoltage", 5),
          ("fMainVoltage", 6))
    )


_MdlPsTestResult_Type.__name__ = "Integer32"
_MdlPsTestResult_Object = MibTableColumn
mdlPsTestResult = _MdlPsTestResult_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 3, 1, 1, 3),
    _MdlPsTestResult_Type()
)
mdlPsTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlPsTestResult.setStatus("current")
_MdlPsVoltageCurrent_Type = Integer32
_MdlPsVoltageCurrent_Object = MibTableColumn
mdlPsVoltageCurrent = _MdlPsVoltageCurrent_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 3, 1, 1, 4),
    _MdlPsVoltageCurrent_Type()
)
mdlPsVoltageCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlPsVoltageCurrent.setStatus("current")
_MdlPsVoltageMin_Type = Integer32
_MdlPsVoltageMin_Object = MibTableColumn
mdlPsVoltageMin = _MdlPsVoltageMin_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 3, 1, 1, 5),
    _MdlPsVoltageMin_Type()
)
mdlPsVoltageMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlPsVoltageMin.setStatus("current")
_MdlPsVoltageMax_Type = Integer32
_MdlPsVoltageMax_Object = MibTableColumn
mdlPsVoltageMax = _MdlPsVoltageMax_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 3, 1, 1, 6),
    _MdlPsVoltageMax_Type()
)
mdlPsVoltageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlPsVoltageMax.setStatus("current")
_PrtDacsMux_ObjectIdentity = ObjectIdentity
prtDacsMux = _PrtDacsMux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3)
)
_PrtGen_ObjectIdentity = ObjectIdentity
prtGen = _PrtGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1)
)
_PrtGenParamTable_Object = MibTable
prtGenParamTable = _PrtGenParamTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    prtGenParamTable.setStatus("current")
_PrtGenEntry_Object = MibTableRow
prtGenEntry = _PrtGenEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 1, 1)
)
prtGenEntry.setIndexNames(
    (0, "RAD-Dacs-MIB", "prtGenPrtIdx"),
)
if mibBuilder.loadTexts:
    prtGenEntry.setStatus("current")
_PrtGenPrtIdx_Type = Integer32
_PrtGenPrtIdx_Object = MibTableColumn
prtGenPrtIdx = _PrtGenPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 1, 1, 1),
    _PrtGenPrtIdx_Type()
)
prtGenPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtGenPrtIdx.setStatus("current")


class _PrtGenSlt_Type(Integer32):
    """Custom type prtGenSlt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              255)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("io13", 17),
          ("io14", 18),
          ("io15", 19),
          ("kmxMlA", 103),
          ("kmxMlB", 104),
          ("kmxCl", 105),
          ("kmxOpt", 106),
          ("kmxIO1", 107),
          ("kmxIO2", 108),
          ("kmxIO3", 109),
          ("kmxIO4", 110),
          ("kmxIO5", 111),
          ("kmxIO6", 112),
          ("kmxIO7", 113),
          ("kmxIO8", 114),
          ("kmxIO9", 115),
          ("kmxIO10", 116),
          ("kmxIO11", 117),
          ("kmxIO12", 118),
          ("standAlone", 255))
    )


_PrtGenSlt_Type.__name__ = "Integer32"
_PrtGenSlt_Object = MibTableColumn
prtGenSlt = _PrtGenSlt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 1, 1, 2),
    _PrtGenSlt_Type()
)
prtGenSlt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtGenSlt.setStatus("current")


class _PrtGenExtInt_Type(Integer32):
    """Custom type prtGenExtInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 3))
    )


_PrtGenExtInt_Type.__name__ = "Integer32"
_PrtGenExtInt_Object = MibTableColumn
prtGenExtInt = _PrtGenExtInt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 1, 1, 3),
    _PrtGenExtInt_Type()
)
prtGenExtInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtGenExtInt.setStatus("current")
_PrtGenIfIndex_Type = Integer32
_PrtGenIfIndex_Object = MibTableColumn
prtGenIfIndex = _PrtGenIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 1, 1, 4),
    _PrtGenIfIndex_Type()
)
prtGenIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtGenIfIndex.setStatus("current")


class _PrtGenActiveStatus_Type(Integer32):
    """Custom type prtGenActiveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("notUsed", 2),
          ("offLine", 3),
          ("onLine", 4),
          ("offLineRedundancy", 5),
          ("onLineRedundancy", 6))
    )


_PrtGenActiveStatus_Type.__name__ = "Integer32"
_PrtGenActiveStatus_Object = MibTableColumn
prtGenActiveStatus = _PrtGenActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 1, 1, 5),
    _PrtGenActiveStatus_Type()
)
prtGenActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtGenActiveStatus.setStatus("current")


class _PrtGenAlrStatus_Type(Integer32):
    """Custom type prtGenAlrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("major", 3),
          ("minor", 4),
          ("event", 5),
          ("warning", 6),
          ("critical", 7))
    )


_PrtGenAlrStatus_Type.__name__ = "Integer32"
_PrtGenAlrStatus_Object = MibTableColumn
prtGenAlrStatus = _PrtGenAlrStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 1, 1, 6),
    _PrtGenAlrStatus_Type()
)
prtGenAlrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtGenAlrStatus.setStatus("current")


class _PrtGenTestStatus_Type(Integer32):
    """Custom type prtGenTestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_PrtGenTestStatus_Type.__name__ = "Integer32"
_PrtGenTestStatus_Object = MibTableColumn
prtGenTestStatus = _PrtGenTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 1, 1, 7),
    _PrtGenTestStatus_Type()
)
prtGenTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtGenTestStatus.setStatus("current")
_PrtGenTestMask_Type = Integer32
_PrtGenTestMask_Object = MibTableColumn
prtGenTestMask = _PrtGenTestMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 1, 1, 8),
    _PrtGenTestMask_Type()
)
prtGenTestMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtGenTestMask.setStatus("current")
_PrtGenTestCmd_Type = Integer32
_PrtGenTestCmd_Object = MibTableColumn
prtGenTestCmd = _PrtGenTestCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 1, 1, 9),
    _PrtGenTestCmd_Type()
)
prtGenTestCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtGenTestCmd.setStatus("current")
_PrtGenTestRunning_Type = Integer32
_PrtGenTestRunning_Object = MibTableColumn
prtGenTestRunning = _PrtGenTestRunning_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 1, 1, 10),
    _PrtGenTestRunning_Type()
)
prtGenTestRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtGenTestRunning.setStatus("current")


class _PrtGenType_Type(Integer32):
    """Custom type prtGenType based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              255)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("t1", 2),
          ("e1", 3),
          ("hs", 4),
          ("t1Csu", 5),
          ("t1Dsu", 6),
          ("e1Ltu", 7),
          ("e1Dsu", 8),
          ("hdsl", 9),
          ("sp", 10),
          ("t1F", 11),
          ("e1F", 12),
          ("dim", 13),
          ("isdn", 14),
          ("t3", 15),
          ("e3", 16),
          ("t3f", 17),
          ("e3f", 18),
          ("idsl", 19),
          ("stm1", 20),
          ("vc4", 21),
          ("vc12", 22),
          ("msdsl", 23),
          ("vc11", 24),
          ("vc3", 25),
          ("soh", 26),
          ("eth", 27),
          ("shdsl", 28),
          ("other", 255))
    )


_PrtGenType_Type.__name__ = "Integer32"
_PrtGenType_Object = MibTableColumn
prtGenType = _PrtGenType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 1, 1, 11),
    _PrtGenType_Type()
)
prtGenType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtGenType.setStatus("current")


class _PrtGenInterfaceType_Type(DisplayString):
    """Custom type prtGenInterfaceType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PrtGenInterfaceType_Type.__name__ = "DisplayString"
_PrtGenInterfaceType_Object = MibTableColumn
prtGenInterfaceType = _PrtGenInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 1, 1, 12),
    _PrtGenInterfaceType_Type()
)
prtGenInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtGenInterfaceType.setStatus("current")


class _PrtGenAlrClearCmd_Type(Integer32):
    """Custom type prtGenAlrClearCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 1),
          ("off", 2),
          ("on", 3))
    )


_PrtGenAlrClearCmd_Type.__name__ = "Integer32"
_PrtGenAlrClearCmd_Object = MibTableColumn
prtGenAlrClearCmd = _PrtGenAlrClearCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 1, 1, 13),
    _PrtGenAlrClearCmd_Type()
)
prtGenAlrClearCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtGenAlrClearCmd.setStatus("current")


class _PrtGenAlrMaskAll_Type(Integer32):
    """Custom type prtGenAlrMaskAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 1),
          ("off", 2),
          ("on", 3))
    )


_PrtGenAlrMaskAll_Type.__name__ = "Integer32"
_PrtGenAlrMaskAll_Object = MibTableColumn
prtGenAlrMaskAll = _PrtGenAlrMaskAll_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 1, 1, 14),
    _PrtGenAlrMaskAll_Type()
)
prtGenAlrMaskAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtGenAlrMaskAll.setStatus("current")
_PrtGenParamStatus_Type = OctetString
_PrtGenParamStatus_Object = MibTableColumn
prtGenParamStatus = _PrtGenParamStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 1, 1, 15),
    _PrtGenParamStatus_Type()
)
prtGenParamStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtGenParamStatus.setStatus("current")


class _PrtGenRdnStatus_Type(Integer32):
    """Custom type prtGenRdnStatus based on Integer32"""
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
          ("off", 2),
          ("on", 3))
    )


_PrtGenRdnStatus_Type.__name__ = "Integer32"
_PrtGenRdnStatus_Object = MibTableColumn
prtGenRdnStatus = _PrtGenRdnStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 1, 1, 16),
    _PrtGenRdnStatus_Type()
)
prtGenRdnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtGenRdnStatus.setStatus("current")
_PrtGenTestMaskXP_Type = OctetString
_PrtGenTestMaskXP_Object = MibTableColumn
prtGenTestMaskXP = _PrtGenTestMaskXP_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 1, 1, 17),
    _PrtGenTestMaskXP_Type()
)
prtGenTestMaskXP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtGenTestMaskXP.setStatus("current")
_PrtGenTestCmdXP_Type = OctetString
_PrtGenTestCmdXP_Object = MibTableColumn
prtGenTestCmdXP = _PrtGenTestCmdXP_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 1, 1, 18),
    _PrtGenTestCmdXP_Type()
)
prtGenTestCmdXP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtGenTestCmdXP.setStatus("current")
_PrtGenTestRunningXP_Type = OctetString
_PrtGenTestRunningXP_Object = MibTableColumn
prtGenTestRunningXP = _PrtGenTestRunningXP_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 1, 1, 19),
    _PrtGenTestRunningXP_Type()
)
prtGenTestRunningXP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtGenTestRunningXP.setStatus("current")
_PrtGenTestDurationTable_Object = MibTable
prtGenTestDurationTable = _PrtGenTestDurationTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 2)
)
if mibBuilder.loadTexts:
    prtGenTestDurationTable.setStatus("current")
_PrtGenTestDurationEntry_Object = MibTableRow
prtGenTestDurationEntry = _PrtGenTestDurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 2, 1)
)
prtGenTestDurationEntry.setIndexNames(
    (0, "RAD-Dacs-MIB", "prtGenTestPrtIdx"),
    (0, "RAD-Dacs-MIB", "prtGenTestIdx"),
)
if mibBuilder.loadTexts:
    prtGenTestDurationEntry.setStatus("current")
_PrtGenTestPrtIdx_Type = Integer32
_PrtGenTestPrtIdx_Object = MibTableColumn
prtGenTestPrtIdx = _PrtGenTestPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 2, 1, 1),
    _PrtGenTestPrtIdx_Type()
)
prtGenTestPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtGenTestPrtIdx.setStatus("current")


class _PrtGenTestIdx_Type(Integer32):
    """Custom type prtGenTestIdx based on Integer32"""
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
              11,
              12,
              14,
              15,
              16,
              20,
              21,
              22,
              23,
              26,
              27,
              28,
              30,
              32,
              33,
              34)
        )
    )
    namedValues = NamedValues(
        *(("localLoop", 1),
          ("remoteLoop", 2),
          ("bert", 3),
          ("plb", 4),
          ("rlb", 5),
          ("llb", 6),
          ("toneInjection", 7),
          ("txInband", 8),
          ("rxInband", 9),
          ("remLoopOnRemUnit", 10),
          ("bertOnRemUnit", 11),
          ("llbOnRemUnit", 12),
          ("txPlb", 14),
          ("txLlb", 15),
          ("dteLoop", 16),
          ("hdslTxInband", 20),
          ("hdslRxInband", 21),
          ("monitor", 22),
          ("userLineLoopback", 23),
          ("lbbd", 26),
          ("lb1", 27),
          ("lb2", 28),
          ("tsRemoteLoop", 30),
          ("downstreamAis", 32),
          ("upstreamAis", 33),
          ("sendRdi", 34))
    )


_PrtGenTestIdx_Type.__name__ = "Integer32"
_PrtGenTestIdx_Object = MibTableColumn
prtGenTestIdx = _PrtGenTestIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 2, 1, 2),
    _PrtGenTestIdx_Type()
)
prtGenTestIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtGenTestIdx.setStatus("current")
_PrtGenTestDuration_Type = Integer32
_PrtGenTestDuration_Object = MibTableColumn
prtGenTestDuration = _PrtGenTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 2, 1, 3),
    _PrtGenTestDuration_Type()
)
prtGenTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtGenTestDuration.setStatus("current")
_PrtGenTsTable_Object = MibTable
prtGenTsTable = _PrtGenTsTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 3)
)
if mibBuilder.loadTexts:
    prtGenTsTable.setStatus("current")
_PrtGenTsEntry_Object = MibTableRow
prtGenTsEntry = _PrtGenTsEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 3, 1)
)
prtGenTsEntry.setIndexNames(
    (0, "RAD-Dacs-MIB", "prtGenTsCnfgIdx"),
    (0, "RAD-Dacs-MIB", "prtGenTsPrtIdx"),
    (0, "RAD-Dacs-MIB", "prtGenTsIdx"),
)
if mibBuilder.loadTexts:
    prtGenTsEntry.setStatus("current")


class _PrtGenTsCnfgIdx_Type(Integer32):
    """Custom type prtGenTsCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtGenTsCnfgIdx_Type.__name__ = "Integer32"
_PrtGenTsCnfgIdx_Object = MibTableColumn
prtGenTsCnfgIdx = _PrtGenTsCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 3, 1, 1),
    _PrtGenTsCnfgIdx_Type()
)
prtGenTsCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtGenTsCnfgIdx.setStatus("current")
_PrtGenTsPrtIdx_Type = Integer32
_PrtGenTsPrtIdx_Object = MibTableColumn
prtGenTsPrtIdx = _PrtGenTsPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 3, 1, 2),
    _PrtGenTsPrtIdx_Type()
)
prtGenTsPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtGenTsPrtIdx.setStatus("current")
_PrtGenTsIdx_Type = Integer32
_PrtGenTsIdx_Object = MibTableColumn
prtGenTsIdx = _PrtGenTsIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 3, 1, 3),
    _PrtGenTsIdx_Type()
)
prtGenTsIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtGenTsIdx.setStatus("current")


class _PrtGenTsType_Type(Integer32):
    """Custom type prtGenTsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("voice", 2),
          ("data", 3),
          ("vcMP", 4),
          ("nc", 5),
          ("mng", 6))
    )


_PrtGenTsType_Type.__name__ = "Integer32"
_PrtGenTsType_Object = MibTableColumn
prtGenTsType = _PrtGenTsType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 3, 1, 4),
    _PrtGenTsType_Type()
)
prtGenTsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtGenTsType.setStatus("current")
_PrtGenTsIConPrt_Type = Integer32
_PrtGenTsIConPrt_Object = MibTableColumn
prtGenTsIConPrt = _PrtGenTsIConPrt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 3, 1, 5),
    _PrtGenTsIConPrt_Type()
)
prtGenTsIConPrt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtGenTsIConPrt.setStatus("current")
_PrtGenTsIConTs_Type = Integer32
_PrtGenTsIConTs_Object = MibTableColumn
prtGenTsIConTs = _PrtGenTsIConTs_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 3, 1, 6),
    _PrtGenTsIConTs_Type()
)
prtGenTsIConTs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtGenTsIConTs.setStatus("current")
_PrtAlr_ObjectIdentity = ObjectIdentity
prtAlr = _PrtAlr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 4)
)
_PrtSAlarmTable_Object = MibTable
prtSAlarmTable = _PrtSAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    prtSAlarmTable.setStatus("current")
_PrtSAlarmEntry_Object = MibTableRow
prtSAlarmEntry = _PrtSAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 4, 1, 1)
)
prtSAlarmEntry.setIndexNames(
    (0, "RAD-Dacs-MIB", "prtSAlarmPrtIdx"),
    (0, "RAD-Dacs-MIB", "prtSAlarmIdx"),
)
if mibBuilder.loadTexts:
    prtSAlarmEntry.setStatus("current")
_PrtSAlarmIdx_Type = Integer32
_PrtSAlarmIdx_Object = MibTableColumn
prtSAlarmIdx = _PrtSAlarmIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 4, 1, 1, 1),
    _PrtSAlarmIdx_Type()
)
prtSAlarmIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSAlarmIdx.setStatus("current")
_PrtSAlarmPrtIdx_Type = Integer32
_PrtSAlarmPrtIdx_Object = MibTableColumn
prtSAlarmPrtIdx = _PrtSAlarmPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 4, 1, 1, 2),
    _PrtSAlarmPrtIdx_Type()
)
prtSAlarmPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSAlarmPrtIdx.setStatus("current")
_PrtSAlarmCode_Type = Integer32
_PrtSAlarmCode_Object = MibTableColumn
prtSAlarmCode = _PrtSAlarmCode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 4, 1, 1, 3),
    _PrtSAlarmCode_Type()
)
prtSAlarmCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSAlarmCode.setStatus("current")


class _PrtSAlarmState_Type(Integer32):
    """Custom type prtSAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("event", 3),
          ("minor", 4),
          ("major", 5),
          ("warning", 6),
          ("critical", 7))
    )


_PrtSAlarmState_Type.__name__ = "Integer32"
_PrtSAlarmState_Object = MibTableColumn
prtSAlarmState = _PrtSAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 4, 1, 1, 4),
    _PrtSAlarmState_Type()
)
prtSAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSAlarmState.setStatus("current")


class _PrtSAlarmMask_Type(Integer32):
    """Custom type prtSAlarmMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_PrtSAlarmMask_Type.__name__ = "Integer32"
_PrtSAlarmMask_Object = MibTableColumn
prtSAlarmMask = _PrtSAlarmMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 4, 1, 1, 5),
    _PrtSAlarmMask_Type()
)
prtSAlarmMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSAlarmMask.setStatus("current")


class _PrtSAlarmInvert_Type(Integer32):
    """Custom type prtSAlarmInvert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_PrtSAlarmInvert_Type.__name__ = "Integer32"
_PrtSAlarmInvert_Object = MibTableColumn
prtSAlarmInvert = _PrtSAlarmInvert_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 4, 1, 1, 6),
    _PrtSAlarmInvert_Type()
)
prtSAlarmInvert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSAlarmInvert.setStatus("current")


class _PrtSAlarmOnOff_Type(Integer32):
    """Custom type prtSAlarmOnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_PrtSAlarmOnOff_Type.__name__ = "Integer32"
_PrtSAlarmOnOff_Object = MibTableColumn
prtSAlarmOnOff = _PrtSAlarmOnOff_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 4, 1, 1, 7),
    _PrtSAlarmOnOff_Type()
)
prtSAlarmOnOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSAlarmOnOff.setStatus("current")
_PrtSAlarmCounter_Type = Integer32
_PrtSAlarmCounter_Object = MibTableColumn
prtSAlarmCounter = _PrtSAlarmCounter_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 4, 1, 1, 8),
    _PrtSAlarmCounter_Type()
)
prtSAlarmCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSAlarmCounter.setStatus("current")
_PrtAlrMaskTable_Object = MibTable
prtAlrMaskTable = _PrtAlrMaskTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 4, 2)
)
if mibBuilder.loadTexts:
    prtAlrMaskTable.setStatus("current")
_PrtAlrMaskEntry_Object = MibTableRow
prtAlrMaskEntry = _PrtAlrMaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 4, 2, 1)
)
prtAlrMaskEntry.setIndexNames(
    (0, "RAD-Dacs-MIB", "prtAlrMaskPrtIdx"),
)
if mibBuilder.loadTexts:
    prtAlrMaskEntry.setStatus("current")
_PrtAlrMaskPrtIdx_Type = Integer32
_PrtAlrMaskPrtIdx_Object = MibTableColumn
prtAlrMaskPrtIdx = _PrtAlrMaskPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 4, 2, 1, 1),
    _PrtAlrMaskPrtIdx_Type()
)
prtAlrMaskPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtAlrMaskPrtIdx.setStatus("current")


class _PrtAlrMask_Type(OctetString):
    """Custom type prtAlrMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_PrtAlrMask_Type.__name__ = "OctetString"
_PrtAlrMask_Object = MibTableColumn
prtAlrMask = _PrtAlrMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 4, 2, 1, 2),
    _PrtAlrMask_Type()
)
prtAlrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtAlrMask.setStatus("current")
_PrtBertTable_Object = MibTable
prtBertTable = _PrtBertTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 5)
)
if mibBuilder.loadTexts:
    prtBertTable.setStatus("current")
_PrtBertEntry_Object = MibTableRow
prtBertEntry = _PrtBertEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 5, 1)
)
prtBertEntry.setIndexNames(
    (0, "RAD-Dacs-MIB", "prtBertPrtIdx"),
)
if mibBuilder.loadTexts:
    prtBertEntry.setStatus("current")
_PrtBertPrtIdx_Type = Integer32
_PrtBertPrtIdx_Object = MibTableColumn
prtBertPrtIdx = _PrtBertPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 5, 1, 1),
    _PrtBertPrtIdx_Type()
)
prtBertPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtBertPrtIdx.setStatus("current")


class _PrtBertPattern_Type(Integer32):
    """Custom type prtBertPattern based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              255)
        )
    )
    namedValues = NamedValues(
        *(("p2E3m1", 1),
          ("p2E4m1", 2),
          ("p2E5m1", 3),
          ("p2E6m1", 4),
          ("p2E7m1", 5),
          ("p511", 6),
          ("p2E10m1", 7),
          ("p2047", 8),
          ("p2E15m1", 9),
          ("p2E17m1", 10),
          ("p2E18m1", 11),
          ("p2E20m1", 12),
          ("qrss", 13),
          ("p2E21m1", 14),
          ("p2E22m1", 15),
          ("p2E23m1", 16),
          ("p2E25m1", 17),
          ("p2E28m1", 18),
          ("p2E29m1", 19),
          ("p2E31m1", 20),
          ("p2E32m1", 21),
          ("rj011", 22),
          ("p63", 23),
          ("p1M7S", 24),
          ("p1S7M", 25),
          ("alternate", 26),
          ("mark", 27),
          ("space", 28),
          ("p2E11m1", 29),
          ("notApplicable", 255))
    )


_PrtBertPattern_Type.__name__ = "Integer32"
_PrtBertPattern_Object = MibTableColumn
prtBertPattern = _PrtBertPattern_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 5, 1, 2),
    _PrtBertPattern_Type()
)
prtBertPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtBertPattern.setStatus("current")


class _PrtBertInjectRate_Type(Integer32):
    """Custom type prtBertInjectRate based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("noError", 1),
          ("r10Em1", 2),
          ("r10Em2", 3),
          ("r10Em3", 4),
          ("r10Em4", 5),
          ("r10Em5", 6),
          ("r10Em6", 7),
          ("r10Em7", 8),
          ("single", 9),
          ("notApplicable", 255))
    )


_PrtBertInjectRate_Type.__name__ = "Integer32"
_PrtBertInjectRate_Object = MibTableColumn
prtBertInjectRate = _PrtBertInjectRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 5, 1, 3),
    _PrtBertInjectRate_Type()
)
prtBertInjectRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtBertInjectRate.setStatus("current")


class _PrtBertInjectErrRateCmd_Type(Integer32):
    """Custom type prtBertInjectErrRateCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_PrtBertInjectErrRateCmd_Type.__name__ = "Integer32"
_PrtBertInjectErrRateCmd_Object = MibTableColumn
prtBertInjectErrRateCmd = _PrtBertInjectErrRateCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 5, 1, 4),
    _PrtBertInjectErrRateCmd_Type()
)
prtBertInjectErrRateCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtBertInjectErrRateCmd.setStatus("current")


class _PrtBertInjectSingleErrCmd_Type(Integer32):
    """Custom type prtBertInjectSingleErrCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_PrtBertInjectSingleErrCmd_Type.__name__ = "Integer32"
_PrtBertInjectSingleErrCmd_Object = MibTableColumn
prtBertInjectSingleErrCmd = _PrtBertInjectSingleErrCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 5, 1, 5),
    _PrtBertInjectSingleErrCmd_Type()
)
prtBertInjectSingleErrCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtBertInjectSingleErrCmd.setStatus("current")
_PrtBertRunTime_Type = Integer32
_PrtBertRunTime_Object = MibTableColumn
prtBertRunTime = _PrtBertRunTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 5, 1, 6),
    _PrtBertRunTime_Type()
)
prtBertRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtBertRunTime.setStatus("current")
_PrtBertESs_Type = Integer32
_PrtBertESs_Object = MibTableColumn
prtBertESs = _PrtBertESs_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 5, 1, 7),
    _PrtBertESs_Type()
)
prtBertESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtBertESs.setStatus("current")
_PrtBertSyncLoss_Type = Integer32
_PrtBertSyncLoss_Object = MibTableColumn
prtBertSyncLoss = _PrtBertSyncLoss_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 5, 1, 8),
    _PrtBertSyncLoss_Type()
)
prtBertSyncLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtBertSyncLoss.setStatus("current")
_PrtBertErrorBits_Type = Integer32
_PrtBertErrorBits_Object = MibTableColumn
prtBertErrorBits = _PrtBertErrorBits_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 5, 1, 9),
    _PrtBertErrorBits_Type()
)
prtBertErrorBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtBertErrorBits.setStatus("current")


class _PrtBertClearCounters_Type(Integer32):
    """Custom type prtBertClearCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_PrtBertClearCounters_Type.__name__ = "Integer32"
_PrtBertClearCounters_Object = MibTableColumn
prtBertClearCounters = _PrtBertClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 5, 1, 10),
    _PrtBertClearCounters_Type()
)
prtBertClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtBertClearCounters.setStatus("current")


class _PrtBertSyncStatus_Type(Integer32):
    """Custom type prtBertSyncStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("syncLoss", 2),
          ("sync", 3))
    )


_PrtBertSyncStatus_Type.__name__ = "Integer32"
_PrtBertSyncStatus_Object = MibTableColumn
prtBertSyncStatus = _PrtBertSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 5, 1, 11),
    _PrtBertSyncStatus_Type()
)
prtBertSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtBertSyncStatus.setStatus("current")


class _PrtBertTs_Type(OctetString):
    """Custom type prtBertTs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_PrtBertTs_Type.__name__ = "OctetString"
_PrtBertTs_Object = MibTableColumn
prtBertTs = _PrtBertTs_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 5, 1, 12),
    _PrtBertTs_Type()
)
prtBertTs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtBertTs.setStatus("current")


class _PrtBertResult_Type(DisplayString):
    """Custom type prtBertResult based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PrtBertResult_Type.__name__ = "DisplayString"
_PrtBertResult_Object = MibTableColumn
prtBertResult = _PrtBertResult_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 5, 1, 13),
    _PrtBertResult_Type()
)
prtBertResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtBertResult.setStatus("current")
_PrtBertTxBits_Type = Integer32
_PrtBertTxBits_Object = MibTableColumn
prtBertTxBits = _PrtBertTxBits_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 5, 1, 14),
    _PrtBertTxBits_Type()
)
prtBertTxBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtBertTxBits.setStatus("current")
_PrtBertRxBits_Type = Integer32
_PrtBertRxBits_Object = MibTableColumn
prtBertRxBits = _PrtBertRxBits_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 5, 1, 15),
    _PrtBertRxBits_Type()
)
prtBertRxBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtBertRxBits.setStatus("current")
_PrtBertTxErrorBits_Type = Integer32
_PrtBertTxErrorBits_Object = MibTableColumn
prtBertTxErrorBits = _PrtBertTxErrorBits_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 5, 1, 16),
    _PrtBertTxErrorBits_Type()
)
prtBertTxErrorBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtBertTxErrorBits.setStatus("current")
_PrtMonTable_Object = MibTable
prtMonTable = _PrtMonTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 6)
)
if mibBuilder.loadTexts:
    prtMonTable.setStatus("current")
_PrtMonEntry_Object = MibTableRow
prtMonEntry = _PrtMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 6, 1)
)
prtMonEntry.setIndexNames(
    (0, "RAD-Dacs-MIB", "prtMonCnfgIdx"),
    (0, "RAD-Dacs-MIB", "prtMonitoringIdx"),
)
if mibBuilder.loadTexts:
    prtMonEntry.setStatus("current")


class _PrtMonCnfgIdx_Type(Integer32):
    """Custom type prtMonCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtMonCnfgIdx_Type.__name__ = "Integer32"
_PrtMonCnfgIdx_Object = MibTableColumn
prtMonCnfgIdx = _PrtMonCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 6, 1, 1),
    _PrtMonCnfgIdx_Type()
)
prtMonCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMonCnfgIdx.setStatus("current")
_PrtMonitoringIdx_Type = Integer32
_PrtMonitoringIdx_Object = MibTableColumn
prtMonitoringIdx = _PrtMonitoringIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 6, 1, 2),
    _PrtMonitoringIdx_Type()
)
prtMonitoringIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMonitoringIdx.setStatus("current")


class _PrtMonitoringEnable_Type(Integer32):
    """Custom type prtMonitoringEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_PrtMonitoringEnable_Type.__name__ = "Integer32"
_PrtMonitoringEnable_Object = MibTableColumn
prtMonitoringEnable = _PrtMonitoringEnable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 6, 1, 3),
    _PrtMonitoringEnable_Type()
)
prtMonitoringEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtMonitoringEnable.setStatus("current")


class _PrtMonitoringTSs_Type(OctetString):
    """Custom type prtMonitoringTSs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_PrtMonitoringTSs_Type.__name__ = "OctetString"
_PrtMonitoringTSs_Object = MibTableColumn
prtMonitoringTSs = _PrtMonitoringTSs_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 6, 1, 4),
    _PrtMonitoringTSs_Type()
)
prtMonitoringTSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtMonitoringTSs.setStatus("current")
_PrtMonitoredPort_Type = Integer32
_PrtMonitoredPort_Object = MibTableColumn
prtMonitoredPort = _PrtMonitoredPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 6, 1, 5),
    _PrtMonitoredPort_Type()
)
prtMonitoredPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtMonitoredPort.setStatus("current")


class _PrtMonitoredTSs_Type(OctetString):
    """Custom type prtMonitoredTSs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_PrtMonitoredTSs_Type.__name__ = "OctetString"
_PrtMonitoredTSs_Object = MibTableColumn
prtMonitoredTSs = _PrtMonitoredTSs_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 6, 1, 6),
    _PrtMonitoredTSs_Type()
)
prtMonitoredTSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtMonitoredTSs.setStatus("current")
_PrtCfgParam_ObjectIdentity = ObjectIdentity
prtCfgParam = _PrtCfgParam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 7)
)
_PrtCfgParamTable_Object = MibTable
prtCfgParamTable = _PrtCfgParamTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 7, 1)
)
if mibBuilder.loadTexts:
    prtCfgParamTable.setStatus("current")
_PrtCfgParamEntry_Object = MibTableRow
prtCfgParamEntry = _PrtCfgParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 7, 1, 1)
)
prtCfgParamEntry.setIndexNames(
    (0, "RAD-Dacs-MIB", "prtCfgParamCnfgIdx"),
    (0, "RAD-Dacs-MIB", "prtCfgParamIdx"),
)
if mibBuilder.loadTexts:
    prtCfgParamEntry.setStatus("current")


class _PrtCfgParamCnfgIdx_Type(Integer32):
    """Custom type prtCfgParamCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtCfgParamCnfgIdx_Type.__name__ = "Integer32"
_PrtCfgParamCnfgIdx_Object = MibTableColumn
prtCfgParamCnfgIdx = _PrtCfgParamCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 7, 1, 1, 1),
    _PrtCfgParamCnfgIdx_Type()
)
prtCfgParamCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtCfgParamCnfgIdx.setStatus("current")
_PrtCfgParamIdx_Type = Integer32
_PrtCfgParamIdx_Object = MibTableColumn
prtCfgParamIdx = _PrtCfgParamIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 7, 1, 1, 2),
    _PrtCfgParamIdx_Type()
)
prtCfgParamIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtCfgParamIdx.setStatus("current")


class _PrtCfgParamSlt_Type(Integer32):
    """Custom type prtCfgParamSlt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              255)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("kmxIO1", 107),
          ("kmxIO2", 108),
          ("kmxIO3", 109),
          ("kmxIO4", 110),
          ("kmxIO5", 111),
          ("kmxIO6", 112),
          ("kmxIO7", 113),
          ("kmxIO8", 114),
          ("kmxIO9", 115),
          ("kmxIO10", 116),
          ("kmxIO11", 117),
          ("kmxIO12", 118),
          ("notApplicable", 255))
    )


_PrtCfgParamSlt_Type.__name__ = "Integer32"
_PrtCfgParamSlt_Object = MibTableColumn
prtCfgParamSlt = _PrtCfgParamSlt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 7, 1, 1, 3),
    _PrtCfgParamSlt_Type()
)
prtCfgParamSlt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtCfgParamSlt.setStatus("current")


class _PrtCfgParamOperatedMl_Type(Integer32):
    """Custom type prtCfgParamOperatedMl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              103,
              104)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("kmxMlA", 103),
          ("kmxMlB", 104))
    )


_PrtCfgParamOperatedMl_Type.__name__ = "Integer32"
_PrtCfgParamOperatedMl_Object = MibTableColumn
prtCfgParamOperatedMl = _PrtCfgParamOperatedMl_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 7, 1, 1, 4),
    _PrtCfgParamOperatedMl_Type()
)
prtCfgParamOperatedMl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtCfgParamOperatedMl.setStatus("current")


class _PrtCfgParamMlAtoMlBPrio_Type(Integer32):
    """Custom type prtCfgParamMlAtoMlBPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("low", 2),
          ("high", 3))
    )


_PrtCfgParamMlAtoMlBPrio_Type.__name__ = "Integer32"
_PrtCfgParamMlAtoMlBPrio_Object = MibTableColumn
prtCfgParamMlAtoMlBPrio = _PrtCfgParamMlAtoMlBPrio_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 7, 1, 1, 5),
    _PrtCfgParamMlAtoMlBPrio_Type()
)
prtCfgParamMlAtoMlBPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtCfgParamMlAtoMlBPrio.setStatus("current")


class _PrtCfgParamMlBtoMlAPrio_Type(Integer32):
    """Custom type prtCfgParamMlBtoMlAPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("low", 2),
          ("high", 3))
    )


_PrtCfgParamMlBtoMlAPrio_Type.__name__ = "Integer32"
_PrtCfgParamMlBtoMlAPrio_Object = MibTableColumn
prtCfgParamMlBtoMlAPrio = _PrtCfgParamMlBtoMlAPrio_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 7, 1, 1, 6),
    _PrtCfgParamMlBtoMlAPrio_Type()
)
prtCfgParamMlBtoMlAPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtCfgParamMlBtoMlAPrio.setStatus("current")


class _PrtCfgParamInbandLoopDetection_Type(Integer32):
    """Custom type prtCfgParamInbandLoopDetection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_PrtCfgParamInbandLoopDetection_Type.__name__ = "Integer32"
_PrtCfgParamInbandLoopDetection_Object = MibTableColumn
prtCfgParamInbandLoopDetection = _PrtCfgParamInbandLoopDetection_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 7, 1, 1, 7),
    _PrtCfgParamInbandLoopDetection_Type()
)
prtCfgParamInbandLoopDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtCfgParamInbandLoopDetection.setStatus("current")


class _PrtCfgParamInbandLoopPatternCfg_Type(Integer32):
    """Custom type prtCfgParamInbandLoopPatternCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("rdlLoop", 2),
          ("userConfig", 3))
    )


_PrtCfgParamInbandLoopPatternCfg_Type.__name__ = "Integer32"
_PrtCfgParamInbandLoopPatternCfg_Object = MibTableColumn
prtCfgParamInbandLoopPatternCfg = _PrtCfgParamInbandLoopPatternCfg_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 7, 1, 1, 8),
    _PrtCfgParamInbandLoopPatternCfg_Type()
)
prtCfgParamInbandLoopPatternCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtCfgParamInbandLoopPatternCfg.setStatus("current")
_PrtCfgParamInbandLoopActPattern_Type = DisplayString
_PrtCfgParamInbandLoopActPattern_Object = MibTableColumn
prtCfgParamInbandLoopActPattern = _PrtCfgParamInbandLoopActPattern_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 7, 1, 1, 9),
    _PrtCfgParamInbandLoopActPattern_Type()
)
prtCfgParamInbandLoopActPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtCfgParamInbandLoopActPattern.setStatus("current")
_PrtCfgParamInbandLoopDeactPattern_Type = DisplayString
_PrtCfgParamInbandLoopDeactPattern_Object = MibTableColumn
prtCfgParamInbandLoopDeactPattern = _PrtCfgParamInbandLoopDeactPattern_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 1, 7, 1, 1, 10),
    _PrtCfgParamInbandLoopDeactPattern_Type()
)
prtCfgParamInbandLoopDeactPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtCfgParamInbandLoopDeactPattern.setStatus("current")
_PrtT1E1_ObjectIdentity = ObjectIdentity
prtT1E1 = _PrtT1E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2)
)
_PrtT1E1StatTable_Object = MibTable
prtT1E1StatTable = _PrtT1E1StatTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 1)
)
if mibBuilder.loadTexts:
    prtT1E1StatTable.setStatus("current")
_PrtT1E1StatEntry_Object = MibTableRow
prtT1E1StatEntry = _PrtT1E1StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 1, 1)
)
prtT1E1StatEntry.setIndexNames(
    (0, "RAD-Dacs-MIB", "prtT1E1SPrtIdx"),
)
if mibBuilder.loadTexts:
    prtT1E1StatEntry.setStatus("current")
_PrtT1E1SPrtIdx_Type = Integer32
_PrtT1E1SPrtIdx_Object = MibTableColumn
prtT1E1SPrtIdx = _PrtT1E1SPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 1, 1, 1),
    _PrtT1E1SPrtIdx_Type()
)
prtT1E1SPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtT1E1SPrtIdx.setStatus("current")


class _PrtT1E1SSlt_Type(Integer32):
    """Custom type prtT1E1SSlt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              255)
        )
    )
    namedValues = NamedValues(
        *(("clA", 3),
          ("clB", 4),
          ("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("io13", 17),
          ("io14", 18),
          ("io15", 19),
          ("standAlone", 255))
    )


_PrtT1E1SSlt_Type.__name__ = "Integer32"
_PrtT1E1SSlt_Object = MibTableColumn
prtT1E1SSlt = _PrtT1E1SSlt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 1, 1, 2),
    _PrtT1E1SSlt_Type()
)
prtT1E1SSlt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtT1E1SSlt.setStatus("current")
_PrtT1E1OosCount_Type = Gauge32
_PrtT1E1OosCount_Object = MibTableColumn
prtT1E1OosCount = _PrtT1E1OosCount_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 1, 1, 3),
    _PrtT1E1OosCount_Type()
)
prtT1E1OosCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtT1E1OosCount.setStatus("current")
_PrtT1E1BpvLastMin_Type = Gauge32
_PrtT1E1BpvLastMin_Object = MibTableColumn
prtT1E1BpvLastMin = _PrtT1E1BpvLastMin_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 1, 1, 4),
    _PrtT1E1BpvLastMin_Type()
)
prtT1E1BpvLastMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtT1E1BpvLastMin.setStatus("current")
_PrtT1E1BpvMax_Type = Gauge32
_PrtT1E1BpvMax_Object = MibTableColumn
prtT1E1BpvMax = _PrtT1E1BpvMax_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 1, 1, 5),
    _PrtT1E1BpvMax_Type()
)
prtT1E1BpvMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtT1E1BpvMax.setStatus("current")
_PrtT1E1CnfgTable_Object = MibTable
prtT1E1CnfgTable = _PrtT1E1CnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 2)
)
if mibBuilder.loadTexts:
    prtT1E1CnfgTable.setStatus("current")
_PrtT1E1CnfgEntry_Object = MibTableRow
prtT1E1CnfgEntry = _PrtT1E1CnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 2, 1)
)
prtT1E1CnfgEntry.setIndexNames(
    (0, "RAD-Dacs-MIB", "prtT1E1CnfgIdx"),
    (0, "RAD-Dacs-MIB", "prtT1E1PrtIdx"),
)
if mibBuilder.loadTexts:
    prtT1E1CnfgEntry.setStatus("current")


class _PrtT1E1CnfgIdx_Type(Integer32):
    """Custom type prtT1E1CnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtT1E1CnfgIdx_Type.__name__ = "Integer32"
_PrtT1E1CnfgIdx_Object = MibTableColumn
prtT1E1CnfgIdx = _PrtT1E1CnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 2, 1, 1),
    _PrtT1E1CnfgIdx_Type()
)
prtT1E1CnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtT1E1CnfgIdx.setStatus("current")
_PrtT1E1PrtIdx_Type = Integer32
_PrtT1E1PrtIdx_Object = MibTableColumn
prtT1E1PrtIdx = _PrtT1E1PrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 2, 1, 2),
    _PrtT1E1PrtIdx_Type()
)
prtT1E1PrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtT1E1PrtIdx.setStatus("current")


class _PrtT1E1Slt_Type(Integer32):
    """Custom type prtT1E1Slt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              103,
              104,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              255)
        )
    )
    namedValues = NamedValues(
        *(("clA", 3),
          ("clB", 4),
          ("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("io13", 17),
          ("io14", 18),
          ("io15", 19),
          ("kmxMlA", 103),
          ("kmxMlB", 104),
          ("kmxOpt", 106),
          ("kmxIO1", 107),
          ("kmxIO2", 108),
          ("kmxIO3", 109),
          ("kmxIO4", 110),
          ("kmxIO5", 111),
          ("kmxIO6", 112),
          ("kmxIO7", 113),
          ("kmxIO8", 114),
          ("kmxIO9", 115),
          ("kmxIO10", 116),
          ("kmxIO11", 117),
          ("kmxIO12", 118),
          ("standAlone", 255))
    )


_PrtT1E1Slt_Type.__name__ = "Integer32"
_PrtT1E1Slt_Object = MibTableColumn
prtT1E1Slt = _PrtT1E1Slt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 2, 1, 3),
    _PrtT1E1Slt_Type()
)
prtT1E1Slt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtT1E1Slt.setStatus("current")


class _PrtT1E1LineType_Type(Integer32):
    """Custom type prtT1E1LineType based on Integer32"""
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
        *(("other", 1),
          ("esf", 2),
          ("d4", 3),
          ("e1", 4),
          ("e1Crc", 5),
          ("e1MF", 6),
          ("e1CrcMF", 7),
          ("unframed", 8))
    )


_PrtT1E1LineType_Type.__name__ = "Integer32"
_PrtT1E1LineType_Object = MibTableColumn
prtT1E1LineType = _PrtT1E1LineType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 2, 1, 4),
    _PrtT1E1LineType_Type()
)
prtT1E1LineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtT1E1LineType.setStatus("current")


class _PrtT1E1LineCode_Type(Integer32):
    """Custom type prtT1E1LineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("jbzs", 1),
          ("b8zs", 2),
          ("hdb3", 3),
          ("zbtsi", 4),
          ("ami", 5),
          ("other", 6))
    )


_PrtT1E1LineCode_Type.__name__ = "Integer32"
_PrtT1E1LineCode_Object = MibTableColumn
prtT1E1LineCode = _PrtT1E1LineCode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 2, 1, 5),
    _PrtT1E1LineCode_Type()
)
prtT1E1LineCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtT1E1LineCode.setStatus("current")


class _PrtT1E1SignalMode_Type(Integer32):
    """Custom type prtT1E1SignalMode based on Integer32"""
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
        *(("none", 1),
          ("robbedBit", 2),
          ("bitOriented", 3),
          ("messageOriented", 4))
    )


_PrtT1E1SignalMode_Type.__name__ = "Integer32"
_PrtT1E1SignalMode_Object = MibTableColumn
prtT1E1SignalMode = _PrtT1E1SignalMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 2, 1, 6),
    _PrtT1E1SignalMode_Type()
)
prtT1E1SignalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtT1E1SignalMode.setStatus("current")


class _PrtT1E1Fdl_Type(Integer32):
    """Custom type prtT1E1Fdl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("ansi-T1-403", 2),
          ("att-54016", 4),
          ("fdl-none", 8),
          ("transFdl", 16))
    )


_PrtT1E1Fdl_Type.__name__ = "Integer32"
_PrtT1E1Fdl_Object = MibTableColumn
prtT1E1Fdl = _PrtT1E1Fdl_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 2, 1, 7),
    _PrtT1E1Fdl_Type()
)
prtT1E1Fdl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtT1E1Fdl.setStatus("current")


class _PrtT1E1FdlMode_Type(Integer32):
    """Custom type prtT1E1FdlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("user", 2),
          ("carrier", 3),
          ("notApplicable", 255))
    )


_PrtT1E1FdlMode_Type.__name__ = "Integer32"
_PrtT1E1FdlMode_Object = MibTableColumn
prtT1E1FdlMode = _PrtT1E1FdlMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 2, 1, 8),
    _PrtT1E1FdlMode_Type()
)
prtT1E1FdlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtT1E1FdlMode.setStatus("current")


class _PrtT1E1Sync_Type(Integer32):
    """Custom type prtT1E1Sync based on Integer32"""
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
        *(("other", 1),
          ("tr62411", 2),
          ("ccitt", 3),
          ("fast", 4))
    )


_PrtT1E1Sync_Type.__name__ = "Integer32"
_PrtT1E1Sync_Object = MibTableColumn
prtT1E1Sync = _PrtT1E1Sync_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 2, 1, 9),
    _PrtT1E1Sync_Type()
)
prtT1E1Sync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtT1E1Sync.setStatus("current")


class _PrtT1E1CGA_Type(Integer32):
    """Custom type prtT1E1CGA based on Integer32"""
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
          ("trans", 2),
          ("full", 3))
    )


_PrtT1E1CGA_Type.__name__ = "Integer32"
_PrtT1E1CGA_Object = MibTableColumn
prtT1E1CGA = _PrtT1E1CGA_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 2, 1, 10),
    _PrtT1E1CGA_Type()
)
prtT1E1CGA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtT1E1CGA.setStatus("current")


class _PrtT1E1IdleCode_Type(OctetString):
    """Custom type prtT1E1IdleCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_PrtT1E1IdleCode_Type.__name__ = "OctetString"
_PrtT1E1IdleCode_Object = MibTableColumn
prtT1E1IdleCode = _PrtT1E1IdleCode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 2, 1, 11),
    _PrtT1E1IdleCode_Type()
)
prtT1E1IdleCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtT1E1IdleCode.setStatus("current")


class _PrtT1E1OosSignal_Type(Integer32):
    """Custom type prtT1E1OosSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("notsupported", 2),
          ("forcedIdle", 3),
          ("forcedBusy", 4),
          ("busyIdle", 5),
          ("idleBusy", 6))
    )


_PrtT1E1OosSignal_Type.__name__ = "Integer32"
_PrtT1E1OosSignal_Object = MibTableColumn
prtT1E1OosSignal = _PrtT1E1OosSignal_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 2, 1, 12),
    _PrtT1E1OosSignal_Type()
)
prtT1E1OosSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtT1E1OosSignal.setStatus("current")


class _PrtT1E1VoiceOos_Type(OctetString):
    """Custom type prtT1E1VoiceOos based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_PrtT1E1VoiceOos_Type.__name__ = "OctetString"
_PrtT1E1VoiceOos_Object = MibTableColumn
prtT1E1VoiceOos = _PrtT1E1VoiceOos_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 2, 1, 13),
    _PrtT1E1VoiceOos_Type()
)
prtT1E1VoiceOos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtT1E1VoiceOos.setStatus("current")


class _PrtT1E1DataOos_Type(OctetString):
    """Custom type prtT1E1DataOos based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_PrtT1E1DataOos_Type.__name__ = "OctetString"
_PrtT1E1DataOos_Object = MibTableColumn
prtT1E1DataOos = _PrtT1E1DataOos_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 2, 1, 14),
    _PrtT1E1DataOos_Type()
)
prtT1E1DataOos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtT1E1DataOos.setStatus("current")


class _PrtT1E1LineLengthMask_Type(Integer32):
    """Custom type prtT1E1LineLengthMask based on Integer32"""
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
        *(("unknown", 1),
          ("len0p133ft", 2),
          ("len134p266ft", 3),
          ("len267p399ft", 4),
          ("len400p533ft", 5),
          ("len534p655ft", 6),
          ("fcc68", 7))
    )


_PrtT1E1LineLengthMask_Type.__name__ = "Integer32"
_PrtT1E1LineLengthMask_Object = MibTableColumn
prtT1E1LineLengthMask = _PrtT1E1LineLengthMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 2, 1, 15),
    _PrtT1E1LineLengthMask_Type()
)
prtT1E1LineLengthMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtT1E1LineLengthMask.setStatus("current")


class _PrtT1E1TxGainMask_Type(Integer32):
    """Custom type prtT1E1TxGainMask based on Integer32"""
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
        *(("notApplicable", 1),
          ("txGain0db", 2),
          ("txGain7dot5db", 3),
          ("txGain15db", 4),
          ("txGain22dot5db", 5))
    )


_PrtT1E1TxGainMask_Type.__name__ = "Integer32"
_PrtT1E1TxGainMask_Object = MibTableColumn
prtT1E1TxGainMask = _PrtT1E1TxGainMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 2, 1, 16),
    _PrtT1E1TxGainMask_Type()
)
prtT1E1TxGainMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtT1E1TxGainMask.setStatus("current")


class _PrtT1E1InbandMng_Type(Integer32):
    """Custom type prtT1E1InbandMng based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("fdlOrTs0", 3),
          ("dedicatedTs", 4),
          ("dedicatedPpp", 5),
          ("dedicatedFr", 6),
          ("internal", 7))
    )


_PrtT1E1InbandMng_Type.__name__ = "Integer32"
_PrtT1E1InbandMng_Object = MibTableColumn
prtT1E1InbandMng = _PrtT1E1InbandMng_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 2, 1, 17),
    _PrtT1E1InbandMng_Type()
)
prtT1E1InbandMng.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtT1E1InbandMng.setStatus("current")


class _PrtT1E1InbandMngRate_Type(Integer32):
    """Custom type prtT1E1InbandMngRate based on Integer32"""
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
        *(("notApplicable", 1),
          ("r4k", 2),
          ("r8k", 3),
          ("r12k", 4),
          ("r16k", 5),
          ("r32k", 6),
          ("r64k", 7),
          ("r20k", 8))
    )


_PrtT1E1InbandMngRate_Type.__name__ = "Integer32"
_PrtT1E1InbandMngRate_Object = MibTableColumn
prtT1E1InbandMngRate = _PrtT1E1InbandMngRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 2, 1, 18),
    _PrtT1E1InbandMngRate_Type()
)
prtT1E1InbandMngRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtT1E1InbandMngRate.setStatus("current")
_PrtT1E1DedicatedTs_Type = Integer32
_PrtT1E1DedicatedTs_Object = MibTableColumn
prtT1E1DedicatedTs = _PrtT1E1DedicatedTs_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 2, 1, 19),
    _PrtT1E1DedicatedTs_Type()
)
prtT1E1DedicatedTs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtT1E1DedicatedTs.setStatus("current")


class _PrtT1E1InbandMngRoutProt_Type(Integer32):
    """Custom type prtT1E1InbandMngRoutProt based on Integer32"""
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
        *(("notApplicable", 1),
          ("none", 2),
          ("proprietary", 3),
          ("rip2", 4))
    )


_PrtT1E1InbandMngRoutProt_Type.__name__ = "Integer32"
_PrtT1E1InbandMngRoutProt_Object = MibTableColumn
prtT1E1InbandMngRoutProt = _PrtT1E1InbandMngRoutProt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 2, 1, 20),
    _PrtT1E1InbandMngRoutProt_Type()
)
prtT1E1InbandMngRoutProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtT1E1InbandMngRoutProt.setStatus("current")


class _PrtT1E1LinkMode_Type(Integer32):
    """Custom type prtT1E1LinkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("regular", 2),
          ("transparent", 3))
    )


_PrtT1E1LinkMode_Type.__name__ = "Integer32"
_PrtT1E1LinkMode_Object = MibTableColumn
prtT1E1LinkMode = _PrtT1E1LinkMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 2, 1, 21),
    _PrtT1E1LinkMode_Type()
)
prtT1E1LinkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtT1E1LinkMode.setStatus("current")


class _PrtT1E1Multiplier_Type(Integer32):
    """Custom type prtT1E1Multiplier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("br56", 2),
          ("br64", 3))
    )


_PrtT1E1Multiplier_Type.__name__ = "Integer32"
_PrtT1E1Multiplier_Object = MibTableColumn
prtT1E1Multiplier = _PrtT1E1Multiplier_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 2, 1, 22),
    _PrtT1E1Multiplier_Type()
)
prtT1E1Multiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtT1E1Multiplier.setStatus("current")


class _PrtT1E1RxGain_Type(Integer32):
    """Custom type prtT1E1RxGain based on Integer32"""
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
        *(("notApplicable", 1),
          ("rxGain12dB", 2),
          ("rxGain30dB", 3),
          ("rxGain36dB", 4),
          ("shortHaul", 5),
          ("longHaul", 6),
          ("rxGain20dB", 7))
    )


_PrtT1E1RxGain_Type.__name__ = "Integer32"
_PrtT1E1RxGain_Object = MibTableColumn
prtT1E1RxGain = _PrtT1E1RxGain_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 2, 1, 23),
    _PrtT1E1RxGain_Type()
)
prtT1E1RxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtT1E1RxGain.setStatus("current")


class _PrtT1E1RAI_Type(Integer32):
    """Custom type prtT1E1RAI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("off", 2),
          ("on", 3))
    )


_PrtT1E1RAI_Type.__name__ = "Integer32"
_PrtT1E1RAI_Object = MibTableColumn
prtT1E1RAI = _PrtT1E1RAI_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 2, 1, 24),
    _PrtT1E1RAI_Type()
)
prtT1E1RAI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtT1E1RAI.setStatus("current")


class _PrtT1E1LineMode_Type(Integer32):
    """Custom type prtT1E1LineMode based on Integer32"""
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
        *(("notApplicable", 1),
          ("csu", 2),
          ("dsu", 3),
          ("ltu", 4))
    )


_PrtT1E1LineMode_Type.__name__ = "Integer32"
_PrtT1E1LineMode_Object = MibTableColumn
prtT1E1LineMode = _PrtT1E1LineMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 2, 1, 25),
    _PrtT1E1LineMode_Type()
)
prtT1E1LineMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtT1E1LineMode.setStatus("current")
_PrtT1E1TS0SaBits_Type = OctetString
_PrtT1E1TS0SaBits_Object = MibTableColumn
prtT1E1TS0SaBits = _PrtT1E1TS0SaBits_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 2, 1, 26),
    _PrtT1E1TS0SaBits_Type()
)
prtT1E1TS0SaBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtT1E1TS0SaBits.setStatus("current")


class _PrtT1E1ConnectedTS_Type(Integer32):
    """Custom type prtT1E1ConnectedTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("no", 2),
          ("yes", 3))
    )


_PrtT1E1ConnectedTS_Type.__name__ = "Integer32"
_PrtT1E1ConnectedTS_Object = MibTableColumn
prtT1E1ConnectedTS = _PrtT1E1ConnectedTS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 2, 1, 27),
    _PrtT1E1ConnectedTS_Type()
)
prtT1E1ConnectedTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtT1E1ConnectedTS.setStatus("current")


class _PrtT1E1Ts0SaBit_Type(Integer32):
    """Custom type prtT1E1Ts0SaBit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("noMng", 2),
          ("mng", 3))
    )


_PrtT1E1Ts0SaBit_Type.__name__ = "Integer32"
_PrtT1E1Ts0SaBit_Object = MibTableColumn
prtT1E1Ts0SaBit = _PrtT1E1Ts0SaBit_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 2, 1, 28),
    _PrtT1E1Ts0SaBit_Type()
)
prtT1E1Ts0SaBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtT1E1Ts0SaBit.setStatus("current")


class _PrtT1E1SameFeCnfg_Type(Integer32):
    """Custom type prtT1E1SameFeCnfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("no", 2),
          ("yes", 3))
    )


_PrtT1E1SameFeCnfg_Type.__name__ = "Integer32"
_PrtT1E1SameFeCnfg_Object = MibTableColumn
prtT1E1SameFeCnfg = _PrtT1E1SameFeCnfg_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 2, 1, 29),
    _PrtT1E1SameFeCnfg_Type()
)
prtT1E1SameFeCnfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtT1E1SameFeCnfg.setStatus("current")


class _PrtT1E1RemCrc4_Type(Integer32):
    """Custom type prtT1E1RemCrc4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("no", 2),
          ("yes", 3))
    )


_PrtT1E1RemCrc4_Type.__name__ = "Integer32"
_PrtT1E1RemCrc4_Object = MibTableColumn
prtT1E1RemCrc4 = _PrtT1E1RemCrc4_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 2, 1, 30),
    _PrtT1E1RemCrc4_Type()
)
prtT1E1RemCrc4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtT1E1RemCrc4.setStatus("current")
_PrtT1E1MaxTSs_Type = Integer32
_PrtT1E1MaxTSs_Object = MibTableColumn
prtT1E1MaxTSs = _PrtT1E1MaxTSs_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 2, 1, 31),
    _PrtT1E1MaxTSs_Type()
)
prtT1E1MaxTSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtT1E1MaxTSs.setStatus("current")


class _PrtT1E1EocTsConfig_Type(Integer32):
    """Custom type prtT1E1EocTsConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_PrtT1E1EocTsConfig_Type.__name__ = "Integer32"
_PrtT1E1EocTsConfig_Object = MibTableColumn
prtT1E1EocTsConfig = _PrtT1E1EocTsConfig_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 2, 1, 32),
    _PrtT1E1EocTsConfig_Type()
)
prtT1E1EocTsConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtT1E1EocTsConfig.setStatus("current")


class _PrtT1E1Role_Type(Integer32):
    """Custom type prtT1E1Role based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("sub", 2),
          ("main", 3))
    )


_PrtT1E1Role_Type.__name__ = "Integer32"
_PrtT1E1Role_Object = MibTableColumn
prtT1E1Role = _PrtT1E1Role_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 2, 1, 33),
    _PrtT1E1Role_Type()
)
prtT1E1Role.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtT1E1Role.setStatus("current")


class _PrtT1E1PppEchoFailDetection_Type(Integer32):
    """Custom type prtT1E1PppEchoFailDetection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("disable", 2),
          ("enable", 3))
    )


_PrtT1E1PppEchoFailDetection_Type.__name__ = "Integer32"
_PrtT1E1PppEchoFailDetection_Object = MibTableColumn
prtT1E1PppEchoFailDetection = _PrtT1E1PppEchoFailDetection_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 2, 1, 34),
    _PrtT1E1PppEchoFailDetection_Type()
)
prtT1E1PppEchoFailDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtT1E1PppEchoFailDetection.setStatus("current")


class _PrtT1E1CasOosPattern_Type(Integer32):
    """Custom type prtT1E1CasOosPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("space", 1),
          ("mark", 2),
          ("spaceMark", 3))
    )


_PrtT1E1CasOosPattern_Type.__name__ = "Integer32"
_PrtT1E1CasOosPattern_Object = MibTableColumn
prtT1E1CasOosPattern = _PrtT1E1CasOosPattern_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 2, 1, 36),
    _PrtT1E1CasOosPattern_Type()
)
prtT1E1CasOosPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtT1E1CasOosPattern.setStatus("current")


class _PrtT1E1CasOosSpaceCode_Type(Unsigned32):
    """Custom type prtT1E1CasOosSpaceCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_PrtT1E1CasOosSpaceCode_Type.__name__ = "Unsigned32"
_PrtT1E1CasOosSpaceCode_Object = MibTableColumn
prtT1E1CasOosSpaceCode = _PrtT1E1CasOosSpaceCode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 2, 1, 37),
    _PrtT1E1CasOosSpaceCode_Type()
)
prtT1E1CasOosSpaceCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtT1E1CasOosSpaceCode.setStatus("current")


class _PrtT1E1CasOosMarkCode_Type(Unsigned32):
    """Custom type prtT1E1CasOosMarkCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_PrtT1E1CasOosMarkCode_Type.__name__ = "Unsigned32"
_PrtT1E1CasOosMarkCode_Object = MibTableColumn
prtT1E1CasOosMarkCode = _PrtT1E1CasOosMarkCode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 2, 1, 38),
    _PrtT1E1CasOosMarkCode_Type()
)
prtT1E1CasOosMarkCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtT1E1CasOosMarkCode.setStatus("current")
_PrtT1E1FdlMsgTable_Object = MibTable
prtT1E1FdlMsgTable = _PrtT1E1FdlMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 3)
)
if mibBuilder.loadTexts:
    prtT1E1FdlMsgTable.setStatus("current")
_PrtT1E1FdlMsgEntry_Object = MibTableRow
prtT1E1FdlMsgEntry = _PrtT1E1FdlMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 3, 1)
)
prtT1E1FdlMsgEntry.setIndexNames(
    (0, "RAD-Dacs-MIB", "prtT1E1FdlMsgPrtIdx"),
    (0, "RAD-Dacs-MIB", "prtT1E1FdlMsgFdlType"),
)
if mibBuilder.loadTexts:
    prtT1E1FdlMsgEntry.setStatus("current")
_PrtT1E1FdlMsgPrtIdx_Type = Integer32
_PrtT1E1FdlMsgPrtIdx_Object = MibTableColumn
prtT1E1FdlMsgPrtIdx = _PrtT1E1FdlMsgPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 3, 1, 1),
    _PrtT1E1FdlMsgPrtIdx_Type()
)
prtT1E1FdlMsgPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtT1E1FdlMsgPrtIdx.setStatus("current")


class _PrtT1E1FdlMsgFdlType_Type(Integer32):
    """Custom type prtT1E1FdlMsgFdlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("send", 1),
          ("receive", 2))
    )


_PrtT1E1FdlMsgFdlType_Type.__name__ = "Integer32"
_PrtT1E1FdlMsgFdlType_Object = MibTableColumn
prtT1E1FdlMsgFdlType = _PrtT1E1FdlMsgFdlType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 3, 1, 2),
    _PrtT1E1FdlMsgFdlType_Type()
)
prtT1E1FdlMsgFdlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtT1E1FdlMsgFdlType.setStatus("current")


class _PrtT1E1FdlMsgSlt_Type(Integer32):
    """Custom type prtT1E1FdlMsgSlt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              255)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("io13", 17),
          ("io14", 18),
          ("io15", 19),
          ("standAlone", 255))
    )


_PrtT1E1FdlMsgSlt_Type.__name__ = "Integer32"
_PrtT1E1FdlMsgSlt_Object = MibTableColumn
prtT1E1FdlMsgSlt = _PrtT1E1FdlMsgSlt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 3, 1, 3),
    _PrtT1E1FdlMsgSlt_Type()
)
prtT1E1FdlMsgSlt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtT1E1FdlMsgSlt.setStatus("current")
_PrtT1E1FdlMsg_Type = OctetString
_PrtT1E1FdlMsg_Object = MibTableColumn
prtT1E1FdlMsg = _PrtT1E1FdlMsg_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 2, 3, 1, 4),
    _PrtT1E1FdlMsg_Type()
)
prtT1E1FdlMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtT1E1FdlMsg.setStatus("current")
_PrtHS_ObjectIdentity = ObjectIdentity
prtHS = _PrtHS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 3)
)
_PrtHSParamTable_Object = MibTable
prtHSParamTable = _PrtHSParamTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 3, 1)
)
if mibBuilder.loadTexts:
    prtHSParamTable.setStatus("current")
_PrtHSParamEntry_Object = MibTableRow
prtHSParamEntry = _PrtHSParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 3, 1, 1)
)
prtHSParamEntry.setIndexNames(
    (0, "RAD-Dacs-MIB", "prtHSCnfgIdx"),
    (0, "RAD-Dacs-MIB", "prtHSPrtIdx"),
)
if mibBuilder.loadTexts:
    prtHSParamEntry.setStatus("current")


class _PrtHSCnfgIdx_Type(Integer32):
    """Custom type prtHSCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtHSCnfgIdx_Type.__name__ = "Integer32"
_PrtHSCnfgIdx_Object = MibTableColumn
prtHSCnfgIdx = _PrtHSCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 3, 1, 1, 1),
    _PrtHSCnfgIdx_Type()
)
prtHSCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtHSCnfgIdx.setStatus("current")
_PrtHSPrtIdx_Type = Integer32
_PrtHSPrtIdx_Object = MibTableColumn
prtHSPrtIdx = _PrtHSPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 3, 1, 1, 2),
    _PrtHSPrtIdx_Type()
)
prtHSPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtHSPrtIdx.setStatus("current")


class _PrtHSSlt_Type(Integer32):
    """Custom type prtHSSlt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              255)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("io13", 17),
          ("io14", 18),
          ("io15", 19),
          ("standAlone", 255))
    )


_PrtHSSlt_Type.__name__ = "Integer32"
_PrtHSSlt_Object = MibTableColumn
prtHSSlt = _PrtHSSlt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 3, 1, 1, 3),
    _PrtHSSlt_Type()
)
prtHSSlt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtHSSlt.setStatus("current")


class _PrtHSRate_Type(Integer32):
    """Custom type prtHSRate based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              200)
        )
    )
    namedValues = NamedValues(
        *(("r0x56eq0Kbps", 1),
          ("r1x56eq56Kbps", 2),
          ("r2x56eq112Kbps", 3),
          ("r3x56eq168Kbps", 4),
          ("r4x56eq224Kbps", 5),
          ("r5x56eq280Kbps", 6),
          ("r6x56eq336Kbps", 7),
          ("r7x56eq392Kbps", 8),
          ("r8x56eq448Kbps", 9),
          ("r9x56eq504Kbps", 10),
          ("r10x56eq560Kbps", 11),
          ("r11x56eq616Kbps", 12),
          ("r12x56eq672Kbps", 13),
          ("r13x56eq728Kbps", 14),
          ("r14x56eq784Kbps", 15),
          ("r15x56eq840Kbps", 16),
          ("r16x56eq896Kbps", 17),
          ("r17x56eq952Kbps", 18),
          ("r18x56eq1008Kbps", 19),
          ("r19x56eq1064Kbps", 20),
          ("r20x56eq1120Kbps", 21),
          ("r21x56eq1176Kbps", 22),
          ("r22x56eq1232Kbps", 23),
          ("r23x56eq1288Kbps", 24),
          ("r24x56eq1344Kbps", 25),
          ("r25x56eq1400Kbps", 26),
          ("r26x56eq1456Kbps", 27),
          ("r27x56eq1512Kbps", 28),
          ("r28x56eq1568Kbps", 29),
          ("r29x56eq1624Kbps", 30),
          ("r30x56eq1680Kbps", 31),
          ("r31x56eq1736Kbps", 32),
          ("r0x64eq0Kbps", 33),
          ("r1x64eq64Kbps", 34),
          ("r2x64eq128Kbps", 35),
          ("r3x64eq192Kbps", 36),
          ("r4x64eq256Kbps", 37),
          ("r5x64eq320Kbps", 38),
          ("r6x64eq384Kbps", 39),
          ("r7x64eq448Kbps", 40),
          ("r8x64eq512Kbps", 41),
          ("r9x64eq576Kbps", 42),
          ("r10x64eq640Kbps", 43),
          ("r11x64eq704Kbps", 44),
          ("r12x64eq768Kbps", 45),
          ("r13x64eq832Kbps", 46),
          ("r14x64eq896Kbps", 47),
          ("r15x64eq960Kbps", 48),
          ("r16x64eq1024Kbps", 49),
          ("r17x64eq1088Kbps", 50),
          ("r18x64eq1152Kbps", 51),
          ("r19x64eq1216Kbps", 52),
          ("r20x64eq1280Kbps", 53),
          ("r21x64eq1344Kbps", 54),
          ("r22x64eq1408Kbps", 55),
          ("r23x64eq1472Kbps", 56),
          ("r24x64eq1536Kbps", 57),
          ("r25x64eq1600Kbps", 58),
          ("r26x64eq1664Kbps", 59),
          ("r27x64eq1728Kbps", 60),
          ("r28x64eq1792Kbps", 61),
          ("r29x64eq1856Kbps", 62),
          ("r30x64eq1920Kbps", 63),
          ("r31x64eq1984Kbps", 64),
          ("r32x64eq2048Kbps", 65),
          ("r32x56eq1792Kbps", 66),
          ("r64x64eq4096Kbps", 67),
          ("auto", 200))
    )


_PrtHSRate_Type.__name__ = "Integer32"
_PrtHSRate_Object = MibTableColumn
prtHSRate = _PrtHSRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 3, 1, 1, 4),
    _PrtHSRate_Type()
)
prtHSRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtHSRate.setStatus("current")


class _PrtHSFifoSize_Type(Integer32):
    """Custom type prtHSFifoSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("b32bit", 2),
          ("b60bit", 3),
          ("b104bit", 4),
          ("b144bit", 5),
          ("notApplicable", 255))
    )


_PrtHSFifoSize_Type.__name__ = "Integer32"
_PrtHSFifoSize_Object = MibTableColumn
prtHSFifoSize = _PrtHSFifoSize_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 3, 1, 1, 5),
    _PrtHSFifoSize_Type()
)
prtHSFifoSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtHSFifoSize.setStatus("current")


class _PrtHSClkMode_Type(Integer32):
    """Custom type prtHSClkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("dce", 1),
          ("dte1", 2),
          ("dte2", 3),
          ("notApplicable", 255))
    )


_PrtHSClkMode_Type.__name__ = "Integer32"
_PrtHSClkMode_Object = MibTableColumn
prtHSClkMode = _PrtHSClkMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 3, 1, 1, 6),
    _PrtHSClkMode_Type()
)
prtHSClkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtHSClkMode.setStatus("current")


class _PrtHSCTS_Type(Integer32):
    """Custom type prtHSCTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("rts", 2),
          ("notApplicable", 255))
    )


_PrtHSCTS_Type.__name__ = "Integer32"
_PrtHSCTS_Object = MibTableColumn
prtHSCTS = _PrtHSCTS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 3, 1, 1, 7),
    _PrtHSCTS_Type()
)
prtHSCTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtHSCTS.setStatus("current")


class _PrtHSRtsState_Type(Integer32):
    """Custom type prtHSRtsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3),
          ("notApplicable", 255))
    )


_PrtHSRtsState_Type.__name__ = "Integer32"
_PrtHSRtsState_Object = MibTableColumn
prtHSRtsState = _PrtHSRtsState_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 3, 1, 1, 8),
    _PrtHSRtsState_Type()
)
prtHSRtsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtHSRtsState.setStatus("current")


class _PrtHSInbandLoopback_Type(Integer32):
    """Custom type prtHSInbandLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_PrtHSInbandLoopback_Type.__name__ = "Integer32"
_PrtHSInbandLoopback_Object = MibTableColumn
prtHSInbandLoopback = _PrtHSInbandLoopback_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 3, 1, 1, 9),
    _PrtHSInbandLoopback_Type()
)
prtHSInbandLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtHSInbandLoopback.setStatus("current")


class _PrtHSInbandLoopPatternCfg_Type(Integer32):
    """Custom type prtHSInbandLoopPatternCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("rdlLoop", 2),
          ("userConfig", 3))
    )


_PrtHSInbandLoopPatternCfg_Type.__name__ = "Integer32"
_PrtHSInbandLoopPatternCfg_Object = MibTableColumn
prtHSInbandLoopPatternCfg = _PrtHSInbandLoopPatternCfg_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 3, 1, 1, 10),
    _PrtHSInbandLoopPatternCfg_Type()
)
prtHSInbandLoopPatternCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtHSInbandLoopPatternCfg.setStatus("current")
_PrtHSInbandLoopActPattern_Type = DisplayString
_PrtHSInbandLoopActPattern_Object = MibTableColumn
prtHSInbandLoopActPattern = _PrtHSInbandLoopActPattern_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 3, 1, 1, 11),
    _PrtHSInbandLoopActPattern_Type()
)
prtHSInbandLoopActPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtHSInbandLoopActPattern.setStatus("current")
_PrtHSInbandLoopDeactPattern_Type = DisplayString
_PrtHSInbandLoopDeactPattern_Object = MibTableColumn
prtHSInbandLoopDeactPattern = _PrtHSInbandLoopDeactPattern_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 3, 1, 1, 12),
    _PrtHSInbandLoopDeactPattern_Type()
)
prtHSInbandLoopDeactPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtHSInbandLoopDeactPattern.setStatus("current")


class _PrtHSDCD_Type(Integer32):
    """Custom type prtHSDCD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("linkOK", 2),
          ("on", 3))
    )


_PrtHSDCD_Type.__name__ = "Integer32"
_PrtHSDCD_Object = MibTableColumn
prtHSDCD = _PrtHSDCD_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 3, 1, 1, 13),
    _PrtHSDCD_Type()
)
prtHSDCD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtHSDCD.setStatus("current")


class _PrtHSClkPolarity_Type(Integer32):
    """Custom type prtHSClkPolarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("normal", 2),
          ("invert", 3))
    )


_PrtHSClkPolarity_Type.__name__ = "Integer32"
_PrtHSClkPolarity_Object = MibTableColumn
prtHSClkPolarity = _PrtHSClkPolarity_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 3, 1, 1, 14),
    _PrtHSClkPolarity_Type()
)
prtHSClkPolarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtHSClkPolarity.setStatus("current")


class _PrtHSInterfaceType_Type(Integer32):
    """Custom type prtHSInterfaceType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("rs530", 2),
          ("v35", 3),
          ("rs422", 4),
          ("x21", 5),
          ("v24", 6),
          ("rs530a", 7),
          ("rs232", 8),
          ("rs449", 9))
    )


_PrtHSInterfaceType_Type.__name__ = "Integer32"
_PrtHSInterfaceType_Object = MibTableColumn
prtHSInterfaceType = _PrtHSInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 3, 1, 1, 15),
    _PrtHSInterfaceType_Type()
)
prtHSInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtHSInterfaceType.setStatus("current")


class _PrtHSUnframed_Type(Integer32):
    """Custom type prtHSUnframed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("no", 2),
          ("yes", 3))
    )


_PrtHSUnframed_Type.__name__ = "Integer32"
_PrtHSUnframed_Object = MibTableColumn
prtHSUnframed = _PrtHSUnframed_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 3, 1, 1, 16),
    _PrtHSUnframed_Type()
)
prtHSUnframed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtHSUnframed.setStatus("current")
_PrtHSBertTable_Object = MibTable
prtHSBertTable = _PrtHSBertTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 3, 2)
)
if mibBuilder.loadTexts:
    prtHSBertTable.setStatus("current")
_PrtHSBertEntry_Object = MibTableRow
prtHSBertEntry = _PrtHSBertEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 3, 2, 1)
)
prtHSBertEntry.setIndexNames(
    (0, "RAD-Dacs-MIB", "prtHSBertPrtIdx"),
)
if mibBuilder.loadTexts:
    prtHSBertEntry.setStatus("current")
_PrtHSBertPrtIdx_Type = Integer32
_PrtHSBertPrtIdx_Object = MibTableColumn
prtHSBertPrtIdx = _PrtHSBertPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 3, 2, 1, 1),
    _PrtHSBertPrtIdx_Type()
)
prtHSBertPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtHSBertPrtIdx.setStatus("current")


class _PrtHSBertSlt_Type(Integer32):
    """Custom type prtHSBertSlt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              255)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("io13", 17),
          ("io14", 18),
          ("io15", 19),
          ("standAlone", 255))
    )


_PrtHSBertSlt_Type.__name__ = "Integer32"
_PrtHSBertSlt_Object = MibTableColumn
prtHSBertSlt = _PrtHSBertSlt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 3, 2, 1, 2),
    _PrtHSBertSlt_Type()
)
prtHSBertSlt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtHSBertSlt.setStatus("current")


class _PrtHSBertCountClr_Type(Integer32):
    """Custom type prtHSBertCountClr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_PrtHSBertCountClr_Type.__name__ = "Integer32"
_PrtHSBertCountClr_Object = MibTableColumn
prtHSBertCountClr = _PrtHSBertCountClr_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 3, 2, 1, 3),
    _PrtHSBertCountClr_Type()
)
prtHSBertCountClr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtHSBertCountClr.setStatus("current")
_PrtHSBertTestResult_Type = Integer32
_PrtHSBertTestResult_Object = MibTableColumn
prtHSBertTestResult = _PrtHSBertTestResult_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 3, 2, 1, 4),
    _PrtHSBertTestResult_Type()
)
prtHSBertTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtHSBertTestResult.setStatus("current")
_PrtSP_ObjectIdentity = ObjectIdentity
prtSP = _PrtSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 4)
)
_PrtSpCnfgTable_Object = MibTable
prtSpCnfgTable = _PrtSpCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 4, 1)
)
if mibBuilder.loadTexts:
    prtSpCnfgTable.setStatus("current")
_PrtSpCnfgEntry_Object = MibTableRow
prtSpCnfgEntry = _PrtSpCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 4, 1, 1)
)
prtSpCnfgEntry.setIndexNames(
    (0, "RAD-Dacs-MIB", "prtSpCnfgIdx"),
    (0, "RAD-Dacs-MIB", "prtSpPrtIdx"),
)
if mibBuilder.loadTexts:
    prtSpCnfgEntry.setStatus("current")


class _PrtSpCnfgIdx_Type(Integer32):
    """Custom type prtSpCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtSpCnfgIdx_Type.__name__ = "Integer32"
_PrtSpCnfgIdx_Object = MibTableColumn
prtSpCnfgIdx = _PrtSpCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 4, 1, 1, 1),
    _PrtSpCnfgIdx_Type()
)
prtSpCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSpCnfgIdx.setStatus("current")
_PrtSpPrtIdx_Type = Integer32
_PrtSpPrtIdx_Object = MibTableColumn
prtSpPrtIdx = _PrtSpPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 4, 1, 1, 2),
    _PrtSpPrtIdx_Type()
)
prtSpPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSpPrtIdx.setStatus("current")


class _PrtSpUsage_Type(Integer32):
    """Custom type prtSpUsage based on Integer32"""
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
        *(("unknown", 1),
          ("noUse", 2),
          ("nmsSlip", 3),
          ("nmsPpp", 4),
          ("muxSlip", 5),
          ("muxPpp", 6),
          ("terminal", 7),
          ("dialOut", 8))
    )


_PrtSpUsage_Type.__name__ = "Integer32"
_PrtSpUsage_Object = MibTableColumn
prtSpUsage = _PrtSpUsage_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 4, 1, 1, 3),
    _PrtSpUsage_Type()
)
prtSpUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSpUsage.setStatus("current")


class _PrtSpRate_Type(Integer32):
    """Custom type prtSpRate based on Integer32"""
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
        *(("auto", 1),
          ("s300bps", 2),
          ("s1200bps", 3),
          ("s2400bps", 4),
          ("s4800bps", 5),
          ("s9600bps", 6),
          ("s19200bps", 7),
          ("s38400bps", 8),
          ("s57600bps", 9),
          ("s115200bps", 10))
    )


_PrtSpRate_Type.__name__ = "Integer32"
_PrtSpRate_Object = MibTableColumn
prtSpRate = _PrtSpRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 4, 1, 1, 4),
    _PrtSpRate_Type()
)
prtSpRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSpRate.setStatus("current")


class _PrtSpDataBits_Type(Integer32):
    """Custom type prtSpDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dataBits7", 1),
          ("dataBits8", 2))
    )


_PrtSpDataBits_Type.__name__ = "Integer32"
_PrtSpDataBits_Object = MibTableColumn
prtSpDataBits = _PrtSpDataBits_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 4, 1, 1, 5),
    _PrtSpDataBits_Type()
)
prtSpDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSpDataBits.setStatus("current")


class _PrtSpParity_Type(Integer32):
    """Custom type prtSpParity based on Integer32"""
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
          ("odd", 2),
          ("even", 3))
    )


_PrtSpParity_Type.__name__ = "Integer32"
_PrtSpParity_Object = MibTableColumn
prtSpParity = _PrtSpParity_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 4, 1, 1, 6),
    _PrtSpParity_Type()
)
prtSpParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSpParity.setStatus("current")


class _PrtSpCallOutMode_Type(Integer32):
    """Custom type prtSpCallOutMode based on Integer32"""
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
        *(("notApplicable", 1),
          ("none", 2),
          ("all", 3),
          ("major", 4))
    )


_PrtSpCallOutMode_Type.__name__ = "Integer32"
_PrtSpCallOutMode_Object = MibTableColumn
prtSpCallOutMode = _PrtSpCallOutMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 4, 1, 1, 7),
    _PrtSpCallOutMode_Type()
)
prtSpCallOutMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSpCallOutMode.setStatus("current")


class _PrtSpInterface_Type(Integer32):
    """Custom type prtSpInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dce", 1),
          ("dte", 2))
    )


_PrtSpInterface_Type.__name__ = "Integer32"
_PrtSpInterface_Object = MibTableColumn
prtSpInterface = _PrtSpInterface_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 4, 1, 1, 8),
    _PrtSpInterface_Type()
)
prtSpInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSpInterface.setStatus("current")


class _PrtSpCTS_Type(Integer32):
    """Custom type prtSpCTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("on", 2),
          ("rts", 3))
    )


_PrtSpCTS_Type.__name__ = "Integer32"
_PrtSpCTS_Object = MibTableColumn
prtSpCTS = _PrtSpCTS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 4, 1, 1, 9),
    _PrtSpCTS_Type()
)
prtSpCTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSpCTS.setStatus("current")


class _PrtSpDcdDelay_Type(Integer32):
    """Custom type prtSpDcdDelay based on Integer32"""
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
        *(("notApplicable", 1),
          ("d0", 2),
          ("d10", 3),
          ("d50", 4),
          ("d100", 5),
          ("d200", 6),
          ("d300", 7))
    )


_PrtSpDcdDelay_Type.__name__ = "Integer32"
_PrtSpDcdDelay_Object = MibTableColumn
prtSpDcdDelay = _PrtSpDcdDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 4, 1, 1, 10),
    _PrtSpDcdDelay_Type()
)
prtSpDcdDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSpDcdDelay.setStatus("current")


class _PrtSpDsr_Type(Integer32):
    """Custom type prtSpDsr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("on", 2),
          ("dtr", 3))
    )


_PrtSpDsr_Type.__name__ = "Integer32"
_PrtSpDsr_Object = MibTableColumn
prtSpDsr = _PrtSpDsr_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 4, 1, 1, 11),
    _PrtSpDsr_Type()
)
prtSpDsr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSpDsr.setStatus("current")


class _PrtSpNoOfRetries_Type(Integer32):
    """Custom type prtSpNoOfRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_PrtSpNoOfRetries_Type.__name__ = "Integer32"
_PrtSpNoOfRetries_Object = MibTableColumn
prtSpNoOfRetries = _PrtSpNoOfRetries_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 4, 1, 1, 12),
    _PrtSpNoOfRetries_Type()
)
prtSpNoOfRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSpNoOfRetries.setStatus("current")


class _PrtSpWaitForConnect_Type(Integer32):
    """Custom type prtSpWaitForConnect based on Integer32"""
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
        *(("notApplicable", 1),
          ("t30sec", 2),
          ("t45sec", 3),
          ("t60sec", 4))
    )


_PrtSpWaitForConnect_Type.__name__ = "Integer32"
_PrtSpWaitForConnect_Object = MibTableColumn
prtSpWaitForConnect = _PrtSpWaitForConnect_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 4, 1, 1, 13),
    _PrtSpWaitForConnect_Type()
)
prtSpWaitForConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSpWaitForConnect.setStatus("current")


class _PrtSpDialMode_Type(Integer32):
    """Custom type prtSpDialMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("tone", 2),
          ("pulse", 3))
    )


_PrtSpDialMode_Type.__name__ = "Integer32"
_PrtSpDialMode_Object = MibTableColumn
prtSpDialMode = _PrtSpDialMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 4, 1, 1, 14),
    _PrtSpDialMode_Type()
)
prtSpDialMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSpDialMode.setStatus("current")


class _PrtSpAltNumMode_Type(Integer32):
    """Custom type prtSpAltNumMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_PrtSpAltNumMode_Type.__name__ = "Integer32"
_PrtSpAltNumMode_Object = MibTableColumn
prtSpAltNumMode = _PrtSpAltNumMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 4, 1, 1, 15),
    _PrtSpAltNumMode_Type()
)
prtSpAltNumMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSpAltNumMode.setStatus("current")


class _PrtSpPrimaryNum_Type(DisplayString):
    """Custom type prtSpPrimaryNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_PrtSpPrimaryNum_Type.__name__ = "DisplayString"
_PrtSpPrimaryNum_Object = MibTableColumn
prtSpPrimaryNum = _PrtSpPrimaryNum_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 4, 1, 1, 16),
    _PrtSpPrimaryNum_Type()
)
prtSpPrimaryNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSpPrimaryNum.setStatus("current")


class _PrtSpAltNum_Type(DisplayString):
    """Custom type prtSpAltNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_PrtSpAltNum_Type.__name__ = "DisplayString"
_PrtSpAltNum_Object = MibTableColumn
prtSpAltNum = _PrtSpAltNum_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 4, 1, 1, 17),
    _PrtSpAltNum_Type()
)
prtSpAltNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSpAltNum.setStatus("current")


class _PrtSpRoutProtocol_Type(Integer32):
    """Custom type prtSpRoutProtocol based on Integer32"""
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
        *(("notApplicable", 1),
          ("none", 2),
          ("proprietary", 3),
          ("rip2", 4))
    )


_PrtSpRoutProtocol_Type.__name__ = "Integer32"
_PrtSpRoutProtocol_Object = MibTableColumn
prtSpRoutProtocol = _PrtSpRoutProtocol_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 4, 1, 1, 18),
    _PrtSpRoutProtocol_Type()
)
prtSpRoutProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSpRoutProtocol.setStatus("current")


class _PrtSpCmd_Type(OctetString):
    """Custom type prtSpCmd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_PrtSpCmd_Type.__name__ = "OctetString"
_PrtSpCmd_Object = MibTableColumn
prtSpCmd = _PrtSpCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 4, 1, 1, 19),
    _PrtSpCmd_Type()
)
prtSpCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSpCmd.setStatus("current")


class _PrtSpActCallOut_Type(Integer32):
    """Custom type prtSpActCallOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("always", 2),
          ("linkFail", 3))
    )


_PrtSpActCallOut_Type.__name__ = "Integer32"
_PrtSpActCallOut_Object = MibTableColumn
prtSpActCallOut = _PrtSpActCallOut_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 4, 1, 1, 20),
    _PrtSpActCallOut_Type()
)
prtSpActCallOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSpActCallOut.setStatus("current")


class _PrtSpAlrRelayMode_Type(Integer32):
    """Custom type prtSpAlrRelayMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("normal", 2),
          ("invert", 3))
    )


_PrtSpAlrRelayMode_Type.__name__ = "Integer32"
_PrtSpAlrRelayMode_Object = MibTableColumn
prtSpAlrRelayMode = _PrtSpAlrRelayMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 4, 1, 1, 21),
    _PrtSpAlrRelayMode_Type()
)
prtSpAlrRelayMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSpAlrRelayMode.setStatus("current")


class _PrtSpStopBits_Type(Integer32):
    """Custom type prtSpStopBits based on Integer32"""
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
        *(("notApplicable", 1),
          ("stopBits1", 2),
          ("stopBits1dot5", 3),
          ("stopBits2", 4))
    )


_PrtSpStopBits_Type.__name__ = "Integer32"
_PrtSpStopBits_Object = MibTableColumn
prtSpStopBits = _PrtSpStopBits_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 4, 1, 1, 22),
    _PrtSpStopBits_Type()
)
prtSpStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSpStopBits.setStatus("current")
_PrtDim_ObjectIdentity = ObjectIdentity
prtDim = _PrtDim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 5)
)
_PrtDimCnfgTable_Object = MibTable
prtDimCnfgTable = _PrtDimCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 5, 1)
)
if mibBuilder.loadTexts:
    prtDimCnfgTable.setStatus("current")
_PrtDimCnfgEntry_Object = MibTableRow
prtDimCnfgEntry = _PrtDimCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 5, 1, 1)
)
prtDimCnfgEntry.setIndexNames(
    (0, "RAD-Dacs-MIB", "prtDimCnfgIdx"),
    (0, "RAD-Dacs-MIB", "prtDimIdx"),
)
if mibBuilder.loadTexts:
    prtDimCnfgEntry.setStatus("current")


class _PrtDimCnfgIdx_Type(Integer32):
    """Custom type prtDimCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtDimCnfgIdx_Type.__name__ = "Integer32"
_PrtDimCnfgIdx_Object = MibTableColumn
prtDimCnfgIdx = _PrtDimCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 5, 1, 1, 1),
    _PrtDimCnfgIdx_Type()
)
prtDimCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDimCnfgIdx.setStatus("current")
_PrtDimIdx_Type = Integer32
_PrtDimIdx_Object = MibTableColumn
prtDimIdx = _PrtDimIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 5, 1, 1, 2),
    _PrtDimIdx_Type()
)
prtDimIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDimIdx.setStatus("current")


class _PrtDimTxMode_Type(Integer32):
    """Custom type prtDimTxMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("regularTx", 2),
          ("broadcast", 3))
    )


_PrtDimTxMode_Type.__name__ = "Integer32"
_PrtDimTxMode_Object = MibTableColumn
prtDimTxMode = _PrtDimTxMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 5, 1, 1, 3),
    _PrtDimTxMode_Type()
)
prtDimTxMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtDimTxMode.setStatus("current")


class _PrtDimPolarity_Type(Integer32):
    """Custom type prtDimPolarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normalClk", 2),
          ("inverted", 3))
    )


_PrtDimPolarity_Type.__name__ = "Integer32"
_PrtDimPolarity_Object = MibTableColumn
prtDimPolarity = _PrtDimPolarity_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 5, 1, 1, 4),
    _PrtDimPolarity_Type()
)
prtDimPolarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtDimPolarity.setStatus("current")


class _PrtDimClkMode_Type(Integer32):
    """Custom type prtDimClkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("extDce", 2),
          ("dce", 3),
          ("smooth", 4),
          ("extSmooth", 5))
    )


_PrtDimClkMode_Type.__name__ = "Integer32"
_PrtDimClkMode_Object = MibTableColumn
prtDimClkMode = _PrtDimClkMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 5, 1, 1, 5),
    _PrtDimClkMode_Type()
)
prtDimClkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtDimClkMode.setStatus("current")


class _PrtDimMaxDelay_Type(Integer32):
    """Custom type prtDimMaxDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("t16msec", 2),
          ("t64msec", 3))
    )


_PrtDimMaxDelay_Type.__name__ = "Integer32"
_PrtDimMaxDelay_Object = MibTableColumn
prtDimMaxDelay = _PrtDimMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 5, 1, 1, 6),
    _PrtDimMaxDelay_Type()
)
prtDimMaxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtDimMaxDelay.setStatus("current")


class _PrtDimMng_Type(Integer32):
    """Custom type prtDimMng based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("ts1", 3),
          ("dedicatedFr", 4))
    )


_PrtDimMng_Type.__name__ = "Integer32"
_PrtDimMng_Object = MibTableColumn
prtDimMng = _PrtDimMng_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 5, 1, 1, 7),
    _PrtDimMng_Type()
)
prtDimMng.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtDimMng.setStatus("current")


class _PrtDimMngRoutProt_Type(Integer32):
    """Custom type prtDimMngRoutProt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("none", 2),
          ("proprietary", 3))
    )


_PrtDimMngRoutProt_Type.__name__ = "Integer32"
_PrtDimMngRoutProt_Object = MibTableColumn
prtDimMngRoutProt = _PrtDimMngRoutProt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 5, 1, 1, 8),
    _PrtDimMngRoutProt_Type()
)
prtDimMngRoutProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtDimMngRoutProt.setStatus("current")
_PrtDimDestTable_Object = MibTable
prtDimDestTable = _PrtDimDestTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 5, 2)
)
if mibBuilder.loadTexts:
    prtDimDestTable.setStatus("current")
_PrtDimDestEntry_Object = MibTableRow
prtDimDestEntry = _PrtDimDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 5, 2, 1)
)
prtDimDestEntry.setIndexNames(
    (0, "RAD-Dacs-MIB", "prtDestCnfgIdx"),
    (0, "RAD-Dacs-MIB", "prtDestDimIdx"),
    (0, "RAD-Dacs-MIB", "prtDestIdx"),
)
if mibBuilder.loadTexts:
    prtDimDestEntry.setStatus("current")


class _PrtDestCnfgIdx_Type(Integer32):
    """Custom type prtDestCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtDestCnfgIdx_Type.__name__ = "Integer32"
_PrtDestCnfgIdx_Object = MibTableColumn
prtDestCnfgIdx = _PrtDestCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 5, 2, 1, 1),
    _PrtDestCnfgIdx_Type()
)
prtDestCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDestCnfgIdx.setStatus("current")
_PrtDestDimIdx_Type = Integer32
_PrtDestDimIdx_Object = MibTableColumn
prtDestDimIdx = _PrtDestDimIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 5, 2, 1, 2),
    _PrtDestDimIdx_Type()
)
prtDestDimIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDestDimIdx.setStatus("current")


class _PrtDestIdx_Type(Integer32):
    """Custom type prtDestIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PrtDestIdx_Type.__name__ = "Integer32"
_PrtDestIdx_Object = MibTableColumn
prtDestIdx = _PrtDestIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 5, 2, 1, 3),
    _PrtDestIdx_Type()
)
prtDestIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDestIdx.setStatus("current")
_PrtDest_Type = Integer32
_PrtDest_Object = MibTableColumn
prtDest = _PrtDest_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 5, 2, 1, 4),
    _PrtDest_Type()
)
prtDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtDest.setStatus("current")


class _PrtDestConnect_Type(Integer32):
    """Custom type prtDestConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_PrtDestConnect_Type.__name__ = "Integer32"
_PrtDestConnect_Object = MibTableColumn
prtDestConnect = _PrtDestConnect_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 5, 2, 1, 5),
    _PrtDestConnect_Type()
)
prtDestConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDestConnect.setStatus("current")
_PrtI_ObjectIdentity = ObjectIdentity
prtI = _PrtI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 6)
)
_PrtICnfgTable_Object = MibTable
prtICnfgTable = _PrtICnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 6, 1)
)
if mibBuilder.loadTexts:
    prtICnfgTable.setStatus("current")
_PrtICnfgEntry_Object = MibTableRow
prtICnfgEntry = _PrtICnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 6, 1, 1)
)
prtICnfgEntry.setIndexNames(
    (0, "RAD-Dacs-MIB", "prtICnfgIdx"),
    (0, "RAD-Dacs-MIB", "prtIIdx"),
)
if mibBuilder.loadTexts:
    prtICnfgEntry.setStatus("current")


class _PrtICnfgIdx_Type(Integer32):
    """Custom type prtICnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtICnfgIdx_Type.__name__ = "Integer32"
_PrtICnfgIdx_Object = MibTableColumn
prtICnfgIdx = _PrtICnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 6, 1, 1, 1),
    _PrtICnfgIdx_Type()
)
prtICnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtICnfgIdx.setStatus("current")
_PrtIIdx_Type = Integer32
_PrtIIdx_Object = MibTableColumn
prtIIdx = _PrtIIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 6, 1, 1, 2),
    _PrtIIdx_Type()
)
prtIIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtIIdx.setStatus("current")


class _PrtIRate_Type(Integer32):
    """Custom type prtIRate based on Integer32"""
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
        *(("notApplicable", 1),
          ("nc", 2),
          ("r2bit", 3),
          ("r4bit", 4),
          ("r8bit", 5))
    )


_PrtIRate_Type.__name__ = "Integer32"
_PrtIRate_Object = MibTableColumn
prtIRate = _PrtIRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 6, 1, 1, 3),
    _PrtIRate_Type()
)
prtIRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtIRate.setStatus("current")


class _PrtIConnect_Type(Integer32):
    """Custom type prtIConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("no", 2),
          ("yes", 3))
    )


_PrtIConnect_Type.__name__ = "Integer32"
_PrtIConnect_Object = MibTableColumn
prtIConnect = _PrtIConnect_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 6, 1, 1, 4),
    _PrtIConnect_Type()
)
prtIConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtIConnect.setStatus("current")
_PrtHdsl_ObjectIdentity = ObjectIdentity
prtHdsl = _PrtHdsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 7)
)
_PrtHdslTable_Object = MibTable
prtHdslTable = _PrtHdslTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 7, 1)
)
if mibBuilder.loadTexts:
    prtHdslTable.setStatus("current")
_PrtHdslEntry_Object = MibTableRow
prtHdslEntry = _PrtHdslEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 7, 1, 1)
)
prtHdslEntry.setIndexNames(
    (0, "RAD-Dacs-MIB", "prtHdslIdx"),
)
if mibBuilder.loadTexts:
    prtHdslEntry.setStatus("current")
_PrtHdslIdx_Type = Integer32
_PrtHdslIdx_Object = MibTableColumn
prtHdslIdx = _PrtHdslIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 7, 1, 1, 1),
    _PrtHdslIdx_Type()
)
prtHdslIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtHdslIdx.setStatus("current")


class _PrtHdslMode_Type(Integer32):
    """Custom type prtHdslMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("central", 2),
          ("remote", 3))
    )


_PrtHdslMode_Type.__name__ = "Integer32"
_PrtHdslMode_Object = MibTableColumn
prtHdslMode = _PrtHdslMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 7, 1, 1, 2),
    _PrtHdslMode_Type()
)
prtHdslMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtHdslMode.setStatus("current")


class _PrtHdslRptrType_Type(Integer32):
    """Custom type prtHdslRptrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("none", 2),
          ("hrpt", 3))
    )


_PrtHdslRptrType_Type.__name__ = "Integer32"
_PrtHdslRptrType_Object = MibTableColumn
prtHdslRptrType = _PrtHdslRptrType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 7, 1, 1, 3),
    _PrtHdslRptrType_Type()
)
prtHdslRptrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtHdslRptrType.setStatus("current")


class _PrtHdslMaxRate_Type(Integer32):
    """Custom type prtHdslMaxRate based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("r192", 2),
          ("r256", 3),
          ("r320", 4),
          ("r384", 5),
          ("r448", 6),
          ("r512", 7),
          ("r576", 8),
          ("r640", 9),
          ("r768", 10),
          ("r896", 11),
          ("r1024", 12),
          ("r1152", 13),
          ("r1280", 14),
          ("r1536", 15),
          ("r1920", 16),
          ("r2048", 17))
    )


_PrtHdslMaxRate_Type.__name__ = "Integer32"
_PrtHdslMaxRate_Object = MibTableColumn
prtHdslMaxRate = _PrtHdslMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 7, 1, 1, 4),
    _PrtHdslMaxRate_Type()
)
prtHdslMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtHdslMaxRate.setStatus("current")


class _PrtHdslLinkType_Type(Integer32):
    """Custom type prtHdslLinkType based on Integer32"""
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
        *(("notApplicable", 1),
          ("msdsl2w", 2),
          ("hdsl2w", 3),
          ("hdsl4w", 4),
          ("gDsl", 5))
    )


_PrtHdslLinkType_Type.__name__ = "Integer32"
_PrtHdslLinkType_Object = MibTableColumn
prtHdslLinkType = _PrtHdslLinkType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 7, 1, 1, 5),
    _PrtHdslLinkType_Type()
)
prtHdslLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtHdslLinkType.setStatus("current")


class _PrtHdslCompSwVer_Type(DisplayString):
    """Custom type prtHdslCompSwVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PrtHdslCompSwVer_Type.__name__ = "DisplayString"
_PrtHdslCompSwVer_Object = MibTableColumn
prtHdslCompSwVer = _PrtHdslCompSwVer_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 7, 1, 1, 6),
    _PrtHdslCompSwVer_Type()
)
prtHdslCompSwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtHdslCompSwVer.setStatus("current")


class _PrtHdslCompHwVer_Type(DisplayString):
    """Custom type prtHdslCompHwVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PrtHdslCompHwVer_Type.__name__ = "DisplayString"
_PrtHdslCompHwVer_Object = MibTableColumn
prtHdslCompHwVer = _PrtHdslCompHwVer_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 7, 1, 1, 7),
    _PrtHdslCompHwVer_Type()
)
prtHdslCompHwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtHdslCompHwVer.setStatus("current")
_PrtT3E3_ObjectIdentity = ObjectIdentity
prtT3E3 = _PrtT3E3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 8)
)
_PrtT3E3CnfgTable_Object = MibTable
prtT3E3CnfgTable = _PrtT3E3CnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 8, 1)
)
if mibBuilder.loadTexts:
    prtT3E3CnfgTable.setStatus("current")
_PrtT3E3CnfgEntry_Object = MibTableRow
prtT3E3CnfgEntry = _PrtT3E3CnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 8, 1, 1)
)
prtT3E3CnfgEntry.setIndexNames(
    (0, "RAD-Dacs-MIB", "prtT3E3CnfgIdx"),
    (0, "RAD-Dacs-MIB", "prtT3E3PrtIdx"),
)
if mibBuilder.loadTexts:
    prtT3E3CnfgEntry.setStatus("current")


class _PrtT3E3CnfgIdx_Type(Integer32):
    """Custom type prtT3E3CnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtT3E3CnfgIdx_Type.__name__ = "Integer32"
_PrtT3E3CnfgIdx_Object = MibTableColumn
prtT3E3CnfgIdx = _PrtT3E3CnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 8, 1, 1, 1),
    _PrtT3E3CnfgIdx_Type()
)
prtT3E3CnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtT3E3CnfgIdx.setStatus("current")
_PrtT3E3PrtIdx_Type = Integer32
_PrtT3E3PrtIdx_Object = MibTableColumn
prtT3E3PrtIdx = _PrtT3E3PrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 8, 1, 1, 2),
    _PrtT3E3PrtIdx_Type()
)
prtT3E3PrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtT3E3PrtIdx.setStatus("current")


class _PrtT3E3Slt_Type(Integer32):
    """Custom type prtT3E3Slt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              255)
        )
    )
    namedValues = NamedValues(
        *(("clA", 3),
          ("clB", 4),
          ("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("io13", 17),
          ("io14", 18),
          ("io15", 19),
          ("standAlone", 255))
    )


_PrtT3E3Slt_Type.__name__ = "Integer32"
_PrtT3E3Slt_Object = MibTableColumn
prtT3E3Slt = _PrtT3E3Slt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 8, 1, 1, 3),
    _PrtT3E3Slt_Type()
)
prtT3E3Slt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtT3E3Slt.setStatus("current")


class _PrtT3E3LineLength_Type(Integer32):
    """Custom type prtT3E3LineLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("len0p450ft", 2),
          ("len451p900ft", 3))
    )


_PrtT3E3LineLength_Type.__name__ = "Integer32"
_PrtT3E3LineLength_Object = MibTableColumn
prtT3E3LineLength = _PrtT3E3LineLength_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 8, 1, 1, 4),
    _PrtT3E3LineLength_Type()
)
prtT3E3LineLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtT3E3LineLength.setStatus("current")


class _PrtT3E3InbandMng_Type(Integer32):
    """Custom type prtT3E3InbandMng based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("off", 2),
          ("cBit", 3),
          ("cBitTxRxMng", 4),
          ("cBitTx", 5),
          ("cBitTxMng", 6),
          ("m13", 7),
          ("cdpv", 8),
          ("nationalBit", 9))
    )


_PrtT3E3InbandMng_Type.__name__ = "Integer32"
_PrtT3E3InbandMng_Object = MibTableColumn
prtT3E3InbandMng = _PrtT3E3InbandMng_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 8, 1, 1, 5),
    _PrtT3E3InbandMng_Type()
)
prtT3E3InbandMng.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtT3E3InbandMng.setStatus("current")


class _PrtT3E3AisFrame_Type(Integer32):
    """Custom type prtT3E3AisFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("unframed", 2),
          ("framed", 3))
    )


_PrtT3E3AisFrame_Type.__name__ = "Integer32"
_PrtT3E3AisFrame_Object = MibTableColumn
prtT3E3AisFrame = _PrtT3E3AisFrame_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 8, 1, 1, 6),
    _PrtT3E3AisFrame_Type()
)
prtT3E3AisFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtT3E3AisFrame.setStatus("current")


class _PrtT3E3TxClockSource_Type(Integer32):
    """Custom type prtT3E3TxClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("external", 1),
          ("internal", 2),
          ("notApplicable", 255))
    )


_PrtT3E3TxClockSource_Type.__name__ = "Integer32"
_PrtT3E3TxClockSource_Object = MibTableColumn
prtT3E3TxClockSource = _PrtT3E3TxClockSource_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 8, 1, 1, 7),
    _PrtT3E3TxClockSource_Type()
)
prtT3E3TxClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtT3E3TxClockSource.setStatus("current")


class _PrtT3E3RoutProt_Type(Integer32):
    """Custom type prtT3E3RoutProt based on Integer32"""
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
        *(("notApplicable", 1),
          ("none", 2),
          ("proprietary", 3),
          ("rip2", 4))
    )


_PrtT3E3RoutProt_Type.__name__ = "Integer32"
_PrtT3E3RoutProt_Object = MibTableColumn
prtT3E3RoutProt = _PrtT3E3RoutProt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 8, 1, 1, 8),
    _PrtT3E3RoutProt_Type()
)
prtT3E3RoutProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtT3E3RoutProt.setStatus("current")


class _PrtT3E3AisTransmit_Type(Integer32):
    """Custom type prtT3E3AisTransmit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("disable", 2),
          ("enable", 3))
    )


_PrtT3E3AisTransmit_Type.__name__ = "Integer32"
_PrtT3E3AisTransmit_Object = MibTableColumn
prtT3E3AisTransmit = _PrtT3E3AisTransmit_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 3, 8, 1, 1, 9),
    _PrtT3E3AisTransmit_Type()
)
prtT3E3AisTransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtT3E3AisTransmit.setStatus("current")
_GenDacsMux_ObjectIdentity = ObjectIdentity
genDacsMux = _GenDacsMux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 4)
)
_CmprTable_Object = MibTable
cmprTable = _CmprTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 4, 1)
)
if mibBuilder.loadTexts:
    cmprTable.setStatus("current")
_CmprEntry_Object = MibTableRow
cmprEntry = _CmprEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 4, 1, 1)
)
cmprEntry.setIndexNames(
    (0, "RAD-Dacs-MIB", "cmprTypeIdx"),
    (0, "RAD-Dacs-MIB", "cmprCnfgIdx"),
    (0, "RAD-Dacs-MIB", "cmprVersion"),
    (0, "RAD-Dacs-MIB", "cmprSltIdx"),
    (0, "RAD-Dacs-MIB", "cmprPrtIdx"),
)
if mibBuilder.loadTexts:
    cmprEntry.setStatus("current")
_CmprTypeIdx_Type = Integer32
_CmprTypeIdx_Object = MibTableColumn
cmprTypeIdx = _CmprTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 4, 1, 1, 1),
    _CmprTypeIdx_Type()
)
cmprTypeIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmprTypeIdx.setStatus("current")
_CmprCnfgIdx_Type = Integer32
_CmprCnfgIdx_Object = MibTableColumn
cmprCnfgIdx = _CmprCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 4, 1, 1, 2),
    _CmprCnfgIdx_Type()
)
cmprCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmprCnfgIdx.setStatus("current")
_CmprVersion_Type = Integer32
_CmprVersion_Object = MibTableColumn
cmprVersion = _CmprVersion_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 4, 1, 1, 3),
    _CmprVersion_Type()
)
cmprVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmprVersion.setStatus("current")


class _CmprSltIdx_Type(Integer32):
    """Custom type cmprSltIdx based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              255)
        )
    )
    namedValues = NamedValues(
        *(("psA", 1),
          ("psB", 2),
          ("clA", 3),
          ("clB", 4),
          ("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("io13", 17),
          ("io14", 18),
          ("io15", 19),
          ("notApplicable", 255))
    )


_CmprSltIdx_Type.__name__ = "Integer32"
_CmprSltIdx_Object = MibTableColumn
cmprSltIdx = _CmprSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 4, 1, 1, 4),
    _CmprSltIdx_Type()
)
cmprSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmprSltIdx.setStatus("current")
_CmprPrtIdx_Type = Integer32
_CmprPrtIdx_Object = MibTableColumn
cmprPrtIdx = _CmprPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 4, 1, 1, 5),
    _CmprPrtIdx_Type()
)
cmprPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmprPrtIdx.setStatus("current")
_CmprObj_Type = OctetString
_CmprObj_Object = MibTableColumn
cmprObj = _CmprObj_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 4, 1, 1, 6),
    _CmprObj_Type()
)
cmprObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmprObj.setStatus("current")
_MapLinkTable_Object = MibTable
mapLinkTable = _MapLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 4, 2)
)
if mibBuilder.loadTexts:
    mapLinkTable.setStatus("current")
_MapLinkEntry_Object = MibTableRow
mapLinkEntry = _MapLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 4, 2, 1)
)
mapLinkEntry.setIndexNames(
    (0, "RAD-Dacs-MIB", "mapLinkIdx"),
)
if mibBuilder.loadTexts:
    mapLinkEntry.setStatus("current")
_MapLinkIdx_Type = Integer32
_MapLinkIdx_Object = MibTableColumn
mapLinkIdx = _MapLinkIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 4, 2, 1, 1),
    _MapLinkIdx_Type()
)
mapLinkIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mapLinkIdx.setStatus("current")


class _MapLinkSlotIdx_Type(Integer32):
    """Custom type mapLinkSlotIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              255)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("io13", 17),
          ("io14", 18),
          ("io15", 19),
          ("standAlone", 255))
    )


_MapLinkSlotIdx_Type.__name__ = "Integer32"
_MapLinkSlotIdx_Object = MibTableColumn
mapLinkSlotIdx = _MapLinkSlotIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 4, 2, 1, 2),
    _MapLinkSlotIdx_Type()
)
mapLinkSlotIdx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mapLinkSlotIdx.setStatus("current")
_MapLinkPortIdx_Type = Integer32
_MapLinkPortIdx_Object = MibTableColumn
mapLinkPortIdx = _MapLinkPortIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 4, 2, 1, 3),
    _MapLinkPortIdx_Type()
)
mapLinkPortIdx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mapLinkPortIdx.setStatus("current")


class _MapLinkState_Type(Integer32):
    """Custom type mapLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("down", 2),
          ("up", 3))
    )


_MapLinkState_Type.__name__ = "Integer32"
_MapLinkState_Object = MibTableColumn
mapLinkState = _MapLinkState_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 4, 2, 1, 4),
    _MapLinkState_Type()
)
mapLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mapLinkState.setStatus("current")
_AlrGenTable_Object = MibTable
alrGenTable = _AlrGenTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 4, 3)
)
if mibBuilder.loadTexts:
    alrGenTable.setStatus("current")
_AlrGenEntry_Object = MibTableRow
alrGenEntry = _AlrGenEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 4, 3, 1)
)
alrGenEntry.setIndexNames(
    (0, "RAD-Dacs-MIB", "alrGenCode"),
)
if mibBuilder.loadTexts:
    alrGenEntry.setStatus("current")
_AlrGenCode_Type = Integer32
_AlrGenCode_Object = MibTableColumn
alrGenCode = _AlrGenCode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 4, 3, 1, 1),
    _AlrGenCode_Type()
)
alrGenCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alrGenCode.setStatus("current")


class _AlrGenDescription_Type(DisplayString):
    """Custom type alrGenDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlrGenDescription_Type.__name__ = "DisplayString"
_AlrGenDescription_Object = MibTableColumn
alrGenDescription = _AlrGenDescription_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 4, 3, 1, 2),
    _AlrGenDescription_Type()
)
alrGenDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alrGenDescription.setStatus("current")


class _AlrGenLevel_Type(Integer32):
    """Custom type alrGenLevel based on Integer32"""
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
        *(("notApplicable", 1),
          ("system", 2),
          ("card", 3),
          ("port", 4))
    )


_AlrGenLevel_Type.__name__ = "Integer32"
_AlrGenLevel_Object = MibTableColumn
alrGenLevel = _AlrGenLevel_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 4, 3, 1, 3),
    _AlrGenLevel_Type()
)
alrGenLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alrGenLevel.setStatus("current")


class _AlrGenSlotType_Type(Integer32):
    """Custom type alrGenSlotType based on Integer32"""
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
        *(("notApplicable", 1),
          ("ps", 2),
          ("cl", 3),
          ("io", 4),
          ("clAndIo", 5))
    )


_AlrGenSlotType_Type.__name__ = "Integer32"
_AlrGenSlotType_Object = MibTableColumn
alrGenSlotType = _AlrGenSlotType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 4, 3, 1, 4),
    _AlrGenSlotType_Type()
)
alrGenSlotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alrGenSlotType.setStatus("current")


class _AlrGenSeverity_Type(Integer32):
    """Custom type alrGenSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("event", 3),
          ("minor", 4),
          ("major", 5),
          ("warning", 6),
          ("critical", 7))
    )


_AlrGenSeverity_Type.__name__ = "Integer32"
_AlrGenSeverity_Object = MibTableColumn
alrGenSeverity = _AlrGenSeverity_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 4, 3, 1, 5),
    _AlrGenSeverity_Type()
)
alrGenSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alrGenSeverity.setStatus("current")


class _AlrGenDebounce_Type(Integer32):
    """Custom type alrGenDebounce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlrGenDebounce_Type.__name__ = "Integer32"
_AlrGenDebounce_Object = MibTableColumn
alrGenDebounce = _AlrGenDebounce_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 4, 3, 1, 6),
    _AlrGenDebounce_Type()
)
alrGenDebounce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alrGenDebounce.setStatus("current")


class _AlrGenDefSeverity_Type(Integer32):
    """Custom type alrGenDefSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("event", 3),
          ("minor", 4),
          ("major", 5),
          ("warning", 6),
          ("critical", 7))
    )


_AlrGenDefSeverity_Type.__name__ = "Integer32"
_AlrGenDefSeverity_Object = MibTableColumn
alrGenDefSeverity = _AlrGenDefSeverity_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 4, 3, 1, 7),
    _AlrGenDefSeverity_Type()
)
alrGenDefSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alrGenDefSeverity.setStatus("current")

# Managed Objects groups


# Notification objects

sanityCheckTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 0, 1)
)
sanityCheckTrap.setObjects(
      *(("RAD-Dacs-MIB", "sysSSanityCheckStatus"),
        ("RAD-Dacs-MIB", "sysDbaseDownloadCnfgIdxCmd"))
)
if mibBuilder.loadTexts:
    sanityCheckTrap.setStatus(
        "current"
    )

dacsMuxAlarmsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 0, 2)
)
if mibBuilder.loadTexts:
    dacsMuxAlarmsTrap.setStatus(
        "current"
    )

mdlConnectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 0, 3)
)
mdlConnectTrap.setObjects(
      *(("RAD-Dacs-MIB", "mdlSCardType"),
        ("RAD-Dacs-MIB", "mdlSActivity"))
)
if mibBuilder.loadTexts:
    mdlConnectTrap.setStatus(
        "current"
    )

sysAlrStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 0, 4)
)
sysAlrStatusTrap.setObjects(
      *(("RAD-Dacs-MIB", "sysSAlrStatusAll"),
        ("RAD-Dacs-MIB", "sysSAlrStatus"))
)
if mibBuilder.loadTexts:
    sysAlrStatusTrap.setStatus(
        "current"
    )

sysStatusChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 0, 5)
)
sysStatusChangedTrap.setObjects(
    ("RAD-GEN-MIB", "agnLed")
)
if mibBuilder.loadTexts:
    sysStatusChangedTrap.setStatus(
        "current"
    )

cnfgUpdateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 0, 6)
)
if mibBuilder.loadTexts:
    cnfgUpdateTrap.setStatus(
        "current"
    )

sysRedundancyStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 0, 7)
)
sysRedundancyStatusTrap.setObjects(
    ("RAD-Dacs-MIB", "sysDclRedundancyStatus")
)
if mibBuilder.loadTexts:
    sysRedundancyStatusTrap.setStatus(
        "current"
    )

sysRedundancyActiveCardTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 0, 8)
)
sysRedundancyActiveCardTrap.setObjects(
    ("RAD-Dacs-MIB", "sysDclOnline")
)
if mibBuilder.loadTexts:
    sysRedundancyActiveCardTrap.setStatus(
        "current"
    )

sysRedundancyActivePortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 0, 9)
)
sysRedundancyActivePortTrap.setObjects(
    ("RAD-Dacs-MIB", "sysCRdnOnline")
)
if mibBuilder.loadTexts:
    sysRedundancyActivePortTrap.setStatus(
        "current"
    )

cardHwFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 0, 1)
)
cardHwFailure.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("ENTITY-MIB", "entPhysicalAlias"),
        ("RAD-Dacs-MIB", "mdlCActualCardType"),
        ("RAD-Dacs-MIB", "mdlCHardwareFailureReason"))
)
if mibBuilder.loadTexts:
    cardHwFailure.setStatus(
        "current"
    )

cardMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 0, 2)
)
cardMismatch.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("ENTITY-MIB", "entPhysicalAlias"),
        ("RAD-Dacs-MIB", "mdlCActualCardType"),
        ("RAD-Dacs-MIB", "mdlCProgCardType"))
)
if mibBuilder.loadTexts:
    cardMismatch.setStatus(
        "current"
    )

cardProvisionFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 0, 3)
)
cardProvisionFailure.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("ENTITY-MIB", "entPhysicalAlias"),
        ("RAD-Dacs-MIB", "mdlCActualCardType"))
)
if mibBuilder.loadTexts:
    cardProvisionFailure.setStatus(
        "current"
    )

cardUnsupportedSw = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 0, 4)
)
cardUnsupportedSw.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("ENTITY-MIB", "entPhysicalAlias"),
        ("RAD-Dacs-MIB", "mdlCActualCardType"),
        ("ENTITY-MIB", "entPhysicalSoftwareRev"))
)
if mibBuilder.loadTexts:
    cardUnsupportedSw.setStatus(
        "current"
    )

cardUnsupportedHw = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 0, 5)
)
cardUnsupportedHw.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("ENTITY-MIB", "entPhysicalAlias"),
        ("RAD-Dacs-MIB", "mdlCActualCardType"),
        ("ENTITY-MIB", "entPhysicalHardwareRev"))
)
if mibBuilder.loadTexts:
    cardUnsupportedHw.setStatus(
        "current"
    )

cardImproperRemoval = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 0, 6)
)
cardImproperRemoval.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("ENTITY-MIB", "entPhysicalAlias"),
        ("RAD-Dacs-MIB", "mdlCProgCardType"))
)
if mibBuilder.loadTexts:
    cardImproperRemoval.setStatus(
        "current"
    )

cardNoResponse = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 0, 8)
)
cardNoResponse.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("ENTITY-MIB", "entPhysicalAlias"),
        ("RAD-Dacs-MIB", "mdlCProgCardType"))
)
if mibBuilder.loadTexts:
    cardNoResponse.setStatus(
        "current"
    )

cardInitFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 0, 9)
)
cardInitFailure.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("ENTITY-MIB", "entPhysicalAlias"),
        ("RAD-Dacs-MIB", "mdlCActualCardType"))
)
if mibBuilder.loadTexts:
    cardInitFailure.setStatus(
        "current"
    )

cardReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 0, 10)
)
cardReset.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("ENTITY-MIB", "entPhysicalAlias"),
        ("RAD-Dacs-MIB", "mdlCActualCardType"))
)
if mibBuilder.loadTexts:
    cardReset.setStatus(
        "current"
    )

cardPluggedIn = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 0, 11)
)
cardPluggedIn.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("ENTITY-MIB", "entPhysicalAlias"),
        ("RAD-Dacs-MIB", "mdlCActualCardType"))
)
if mibBuilder.loadTexts:
    cardPluggedIn.setStatus(
        "current"
    )

cardPluggedOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 0, 12)
)
cardPluggedOut.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("ENTITY-MIB", "entPhysicalAlias"),
        ("RAD-Dacs-MIB", "mdlCProgCardType"))
)
if mibBuilder.loadTexts:
    cardPluggedOut.setStatus(
        "current"
    )

cardConfigurationMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 3, 2, 1, 0, 14)
)
cardConfigurationMismatch.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("ENTITY-MIB", "entPhysicalAlias"),
        ("RAD-Dacs-MIB", "mdlCActualCardType"),
        ("RAD-Dacs-MIB", "mdlCConfigMismatchReason"))
)
if mibBuilder.loadTexts:
    cardConfigurationMismatch.setStatus(
        "current"
    )

powerDeliveryFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 0, 73)
)
powerDeliveryFailure.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("ENTITY-MIB", "entPhysicalAlias"),
        ("RAD-Dacs-MIB", "mdlPsTestResult"))
)
if mibBuilder.loadTexts:
    powerDeliveryFailure.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAD-Dacs-MIB",
    **{"dacsMux": dacsMux,
       "dacsMuxEvents": dacsMuxEvents,
       "sanityCheckTrap": sanityCheckTrap,
       "dacsMuxAlarmsTrap": dacsMuxAlarmsTrap,
       "mdlConnectTrap": mdlConnectTrap,
       "sysAlrStatusTrap": sysAlrStatusTrap,
       "sysStatusChangedTrap": sysStatusChangedTrap,
       "cnfgUpdateTrap": cnfgUpdateTrap,
       "sysRedundancyStatusTrap": sysRedundancyStatusTrap,
       "sysRedundancyActiveCardTrap": sysRedundancyActiveCardTrap,
       "sysRedundancyActivePortTrap": sysRedundancyActivePortTrap,
       "systemDacsMux": systemDacsMux,
       "sysSa": sysSa,
       "sysSaSwchStatus": sysSaSwchStatus,
       "sysSaSwRevision": sysSaSwRevision,
       "sysSaHwVersion": sysSaHwVersion,
       "sysSaPorts": sysSaPorts,
       "sysSaReadSwch": sysSaReadSwch,
       "sysSaBuActivePort": sysSaBuActivePort,
       "sysHub": sysHub,
       "sysChas": sysChas,
       "chassTotalNoOfSlt": chassTotalNoOfSlt,
       "chassTotalNoOfIoSlt": chassTotalNoOfIoSlt,
       "chassTotalNoOfPsSlt": chassTotalNoOfPsSlt,
       "chassTotalNoOfClSlt": chassTotalNoOfClSlt,
       "chassTotalNoOfMlSlt": chassTotalNoOfMlSlt,
       "sysDcl": sysDcl,
       "sysDclTable": sysDclTable,
       "sysDclEntry": sysDclEntry,
       "sysDclCnfgIdx": sysDclCnfgIdx,
       "sysDclRedundancy": sysDclRedundancy,
       "sysDclActiveCl": sysDclActiveCl,
       "sysDclFlipDelay": sysDclFlipDelay,
       "sysDclFlipUponStnClk": sysDclFlipUponStnClk,
       "sysDclChFailThreshold": sysDclChFailThreshold,
       "sysDclChPriority": sysDclChPriority,
       "sysDclConfigDownloadSrc": sysDclConfigDownloadSrc,
       "sysDclSwDownloadSrc": sysDclSwDownloadSrc,
       "sysDclRedundancyStatus": sysDclRedundancyStatus,
       "sysDclOnline": sysDclOnline,
       "sysDclCopyDbTable": sysDclCopyDbTable,
       "sysDclCopyDbEntry": sysDclCopyDbEntry,
       "sysDclCopyDbIdx": sysDclCopyDbIdx,
       "sysDclCopyDbCmd": sysDclCopyDbCmd,
       "sysDclFlipCmd": sysDclFlipCmd,
       "sysStatus": sysStatus,
       "sysSDateFormat": sysSDateFormat,
       "sysSDateCmd": sysSDateCmd,
       "sysSTimeCmd": sysSTimeCmd,
       "sysSActiveCnfg": sysSActiveCnfg,
       "sysSEditCnfg": sysSEditCnfg,
       "sysSEditBy": sysSEditBy,
       "sysSClkSrc": sysSClkSrc,
       "sysSAlrStatus": sysSAlrStatus,
       "sysSAlrStatusAll": sysSAlrStatusAll,
       "sysSTestStatus": sysSTestStatus,
       "sysSSanityCheckStatus": sysSSanityCheckStatus,
       "sysSNoOfSanityCheckErr": sysSNoOfSanityCheckErr,
       "sysSErrListTable": sysSErrListTable,
       "sysSErrListEntry": sysSErrListEntry,
       "sysSErrType": sysSErrType,
       "sysSErrIdx": sysSErrIdx,
       "sysSErrDescription": sysSErrDescription,
       "sysSMaxNoOfCnfg": sysSMaxNoOfCnfg,
       "sysSSelfTestResult": sysSSelfTestResult,
       "sysSRelayState": sysSRelayState,
       "sysSInvertedAlr": sysSInvertedAlr,
       "sysSRdnFlipTable": sysSRdnFlipTable,
       "sysSRdnFlipEntry": sysSRdnFlipEntry,
       "sysSRdnFlipIdx": sysSRdnFlipIdx,
       "sysSRdnFlipSlot": sysSRdnFlipSlot,
       "sysSRdnFlipPort": sysSRdnFlipPort,
       "sysSRdnFlipCause": sysSRdnFlipCause,
       "sysSRdnFlipDate": sysSRdnFlipDate,
       "sysSRdnFlipTime": sysSRdnFlipTime,
       "sysSRdnFlipTableClearCmd": sysSRdnFlipTableClearCmd,
       "sysSRdnFlipCmd": sysSRdnFlipCmd,
       "sysSBusTable": sysSBusTable,
       "sysSBusEntry": sysSBusEntry,
       "sysSBusPortIdx": sysSBusPortIdx,
       "sysSBusStatus": sysSBusStatus,
       "sysSBusCapturePort": sysSBusCapturePort,
       "sysSBusUtilization": sysSBusUtilization,
       "sysSRdnCmdTable": sysSRdnCmdTable,
       "sysSRdnCmdEntry": sysSRdnCmdEntry,
       "sysSRdnEnforcedChannel": sysSRdnEnforcedChannel,
       "sysSRdnLockFlip": sysSRdnLockFlip,
       "sysSRdnManualFlip": sysSRdnManualFlip,
       "sysSAlrAttrIndication": sysSAlrAttrIndication,
       "sysCurrentAlr": sysCurrentAlr,
       "sysSAlrTable": sysSAlrTable,
       "sysSAlrEntry": sysSAlrEntry,
       "sysSAlrIdx": sysSAlrIdx,
       "sysSAlrCode": sysSAlrCode,
       "sysSAlrState": sysSAlrState,
       "sysSAlarmMask": sysSAlarmMask,
       "sysSAlarmInvert": sysSAlarmInvert,
       "sysSAlarmOnOff": sysSAlarmOnOff,
       "sysSAlarmCounter": sysSAlarmCounter,
       "sysSAlrClearCmd": sysSAlrClearCmd,
       "sysSAlrClearAllCmd": sysSAlrClearAllCmd,
       "sysSAlrMaskAll": sysSAlrMaskAll,
       "sysSAlrMask": sysSAlrMask,
       "sysSAlrDataUpdateCmd": sysSAlrDataUpdateCmd,
       "sysBufferAlr": sysBufferAlr,
       "sysBufferAlrTable": sysBufferAlrTable,
       "sysBufferAlrEntry": sysBufferAlrEntry,
       "sysBufferAlrIdx": sysBufferAlrIdx,
       "sysBufferAlrCode": sysBufferAlrCode,
       "sysBufferAlrState": sysBufferAlrState,
       "sysBufferAlrSlot": sysBufferAlrSlot,
       "sysBufferAlrPort": sysBufferAlrPort,
       "sysBufferAlrDate": sysBufferAlrDate,
       "sysBufferAlrTime": sysBufferAlrTime,
       "sysBufferAlrUpTime": sysBufferAlrUpTime,
       "sysBufferAlrInfo": sysBufferAlrInfo,
       "sysBufferAlrClearCmd": sysBufferAlrClearCmd,
       "sysConfig": sysConfig,
       "sysCClkSrcTable": sysCClkSrcTable,
       "sysCClkSrcEntry": sysCClkSrcEntry,
       "sysCClkCnfgIdx": sysCClkCnfgIdx,
       "sysCClkSrcIdx": sysCClkSrcIdx,
       "sysCClkSrcMode": sysCClkSrcMode,
       "sysCClkSrcPrt": sysCClkSrcPrt,
       "sysCClkStationFreq": sysCClkStationFreq,
       "sysCClkRevertiveTimeout": sysCClkRevertiveTimeout,
       "sysCClkStationIf": sysCClkStationIf,
       "sysCClkStationCableMode": sysCClkStationCableMode,
       "sysCClkStationOutState": sysCClkStationOutState,
       "sysCClkSsmBased": sysCClkSsmBased,
       "sysCClkSSubsystemSlot": sysCClkSSubsystemSlot,
       "sysCClkRecoveredID": sysCClkRecoveredID,
       "sysCnfgTable": sysCnfgTable,
       "sysCnfgEntry": sysCnfgEntry,
       "sysCnfgIdx": sysCnfgIdx,
       "sysCMatrixMode": sysCMatrixMode,
       "sysCIsdnFormat": sysCIsdnFormat,
       "sysCRoutingOnEth": sysCRoutingOnEth,
       "sysCAutoConfigEnable": sysCAutoConfigEnable,
       "sysCIntTsAllocMode": sysCIntTsAllocMode,
       "sysCBuPrimaryPort": sysCBuPrimaryPort,
       "sysCEnableLanOverTdm": sysCEnableLanOverTdm,
       "sysCSs7FisuSuppression": sysCSs7FisuSuppression,
       "sysCBuRecMode": sysCBuRecMode,
       "sysCRdnTable": sysCRdnTable,
       "sysCRdnEntry": sysCRdnEntry,
       "sysCRdnCnfgIdx": sysCRdnCnfgIdx,
       "sysCRdnPrimeSlot": sysCRdnPrimeSlot,
       "sysCRdnPrimePort": sysCRdnPrimePort,
       "sysCRdnSecSlot": sysCRdnSecSlot,
       "sysCRdnSecPort": sysCRdnSecPort,
       "sysCRdnMode": sysCRdnMode,
       "sysCRdnRecMode": sysCRdnRecMode,
       "sysCRdnRecTime": sysCRdnRecTime,
       "sysCRdnHwSwFlip": sysCRdnHwSwFlip,
       "sysCRdnRowStatus": sysCRdnRowStatus,
       "sysCRdnOnline": sysCRdnOnline,
       "sysCRdnSwitchingMode": sysCRdnSwitchingMode,
       "sysCRdnFlipUponEvent": sysCRdnFlipUponEvent,
       "sysCRdnLosOrLofTime": sysCRdnLosOrLofTime,
       "sysCRdnEventsTimeWindow": sysCRdnEventsTimeWindow,
       "sysCRdnSequenceNumberThreshold": sysCRdnSequenceNumberThreshold,
       "sysCRdnBufferErrorsThreshold": sysCRdnBufferErrorsThreshold,
       "sysCRdnBuffUnderrunTime": sysCRdnBuffUnderrunTime,
       "sysCRdnPrimePriority": sysCRdnPrimePriority,
       "sysCRdnSecPriority": sysCRdnSecPriority,
       "sysCRdnWTR": sysCRdnWTR,
       "sysCRdnName": sysCRdnName,
       "sysCRdnTxDownDurationUponFlip": sysCRdnTxDownDurationUponFlip,
       "sysDbase": sysDbase,
       "sysDbaseSanityCheckCmd": sysDbaseSanityCheckCmd,
       "sysDbaseDownloadCnfgIdxCmd": sysDbaseDownloadCnfgIdxCmd,
       "sysDbaseUploadCnfgIdxCmd": sysDbaseUploadCnfgIdxCmd,
       "sysDbaseFlipTable": sysDbaseFlipTable,
       "sysDbaseFlipEntry": sysDbaseFlipEntry,
       "sysDbaseFlipIdx": sysDbaseFlipIdx,
       "sysDbaseFlipTime": sysDbaseFlipTime,
       "sysDbaseFlipActivation": sysDbaseFlipActivation,
       "mdlDacsMux": mdlDacsMux,
       "mdlGen": mdlGen,
       "cardEvents": cardEvents,
       "cardHwFailure": cardHwFailure,
       "cardMismatch": cardMismatch,
       "cardProvisionFailure": cardProvisionFailure,
       "cardUnsupportedSw": cardUnsupportedSw,
       "cardUnsupportedHw": cardUnsupportedHw,
       "cardImproperRemoval": cardImproperRemoval,
       "cardNoResponse": cardNoResponse,
       "cardInitFailure": cardInitFailure,
       "cardReset": cardReset,
       "cardPluggedIn": cardPluggedIn,
       "cardPluggedOut": cardPluggedOut,
       "cardConfigurationMismatch": cardConfigurationMismatch,
       "mdlSTable": mdlSTable,
       "mdlSEntry": mdlSEntry,
       "mdlSSltIdx": mdlSSltIdx,
       "mdlSCardType": mdlSCardType,
       "mdlSHwVer": mdlSHwVer,
       "mdlSSwVer": mdlSSwVer,
       "mdlSAlarmStatus": mdlSAlarmStatus,
       "mdlSAlarmStatusAll": mdlSAlarmStatusAll,
       "mdlSTestStatus": mdlSTestStatus,
       "mdlSHwStatus": mdlSHwStatus,
       "mdlSActivity": mdlSActivity,
       "mdlSAlrClearCmd": mdlSAlrClearCmd,
       "mdlSAlrClearAllCmd": mdlSAlrClearAllCmd,
       "mdlSAlrMaskAll": mdlSAlrMaskAll,
       "mdlSCmd": mdlSCmd,
       "mdlSReset": mdlSReset,
       "mdlSRebuildFrame": mdlSRebuildFrame,
       "mdlSBackupSwVer": mdlSBackupSwVer,
       "mdlSSecondaryBackupSwVer": mdlSSecondaryBackupSwVer,
       "mdlSPiggybackVer": mdlSPiggybackVer,
       "mdlCTable": mdlCTable,
       "mdlCEntry": mdlCEntry,
       "mdlCConfigIdx": mdlCConfigIdx,
       "mdlCSlotIdx": mdlCSlotIdx,
       "mdlCProgCardType": mdlCProgCardType,
       "mdlCNoOfExtPrt": mdlCNoOfExtPrt,
       "mdlCNoOfIntPrt": mdlCNoOfIntPrt,
       "mdlCParam": mdlCParam,
       "mdlCAdminStatus": mdlCAdminStatus,
       "mdlCActualCardType": mdlCActualCardType,
       "mdlCOperStatus": mdlCOperStatus,
       "mdlCDetailedStatus": mdlCDetailedStatus,
       "mdlCEntPhysicalIndex": mdlCEntPhysicalIndex,
       "mdlCReset": mdlCReset,
       "mdlCConfigMismatchReason": mdlCConfigMismatchReason,
       "mdlCIpAddressType": mdlCIpAddressType,
       "mdlCIpAddress": mdlCIpAddress,
       "mdlCHardwareFailureReason": mdlCHardwareFailureReason,
       "mdlCFanControl": mdlCFanControl,
       "mdlCFanOperStatus": mdlCFanOperStatus,
       "mdlAlr": mdlAlr,
       "mdlAlrTable": mdlAlrTable,
       "mdlAlrEntry": mdlAlrEntry,
       "mdlAlrIdx": mdlAlrIdx,
       "mdlAlrSltIdx": mdlAlrSltIdx,
       "mdlAlrCode": mdlAlrCode,
       "mdlAlrState": mdlAlrState,
       "mdlAlarmMask": mdlAlarmMask,
       "mdlAlarmInvert": mdlAlarmInvert,
       "mdlAlarmOnOff": mdlAlarmOnOff,
       "mdlAlarmCounter": mdlAlarmCounter,
       "mdlAlrMaskTable": mdlAlrMaskTable,
       "mdlAlrMaskEntry": mdlAlrMaskEntry,
       "mdlAlrMaskSltIdx": mdlAlrMaskSltIdx,
       "mdlAlrMask": mdlAlrMask,
       "mdlCl": mdlCl,
       "mdlClTable": mdlClTable,
       "mdlClEntry": mdlClEntry,
       "mdlClIdx": mdlClIdx,
       "mdlClSwchStatus": mdlClSwchStatus,
       "mdlClLastFlipDate": mdlClLastFlipDate,
       "mdlClLastFlipTime": mdlClLastFlipTime,
       "mdlClLastFlipCause": mdlClLastFlipCause,
       "mdlPs": mdlPs,
       "mdlPsTable": mdlPsTable,
       "mdlPsEntry": mdlPsEntry,
       "mdlPsIdx": mdlPsIdx,
       "mdlPsStatus": mdlPsStatus,
       "mdlPsTestResult": mdlPsTestResult,
       "mdlPsVoltageCurrent": mdlPsVoltageCurrent,
       "mdlPsVoltageMin": mdlPsVoltageMin,
       "mdlPsVoltageMax": mdlPsVoltageMax,
       "prtDacsMux": prtDacsMux,
       "prtGen": prtGen,
       "prtGenParamTable": prtGenParamTable,
       "prtGenEntry": prtGenEntry,
       "prtGenPrtIdx": prtGenPrtIdx,
       "prtGenSlt": prtGenSlt,
       "prtGenExtInt": prtGenExtInt,
       "prtGenIfIndex": prtGenIfIndex,
       "prtGenActiveStatus": prtGenActiveStatus,
       "prtGenAlrStatus": prtGenAlrStatus,
       "prtGenTestStatus": prtGenTestStatus,
       "prtGenTestMask": prtGenTestMask,
       "prtGenTestCmd": prtGenTestCmd,
       "prtGenTestRunning": prtGenTestRunning,
       "prtGenType": prtGenType,
       "prtGenInterfaceType": prtGenInterfaceType,
       "prtGenAlrClearCmd": prtGenAlrClearCmd,
       "prtGenAlrMaskAll": prtGenAlrMaskAll,
       "prtGenParamStatus": prtGenParamStatus,
       "prtGenRdnStatus": prtGenRdnStatus,
       "prtGenTestMaskXP": prtGenTestMaskXP,
       "prtGenTestCmdXP": prtGenTestCmdXP,
       "prtGenTestRunningXP": prtGenTestRunningXP,
       "prtGenTestDurationTable": prtGenTestDurationTable,
       "prtGenTestDurationEntry": prtGenTestDurationEntry,
       "prtGenTestPrtIdx": prtGenTestPrtIdx,
       "prtGenTestIdx": prtGenTestIdx,
       "prtGenTestDuration": prtGenTestDuration,
       "prtGenTsTable": prtGenTsTable,
       "prtGenTsEntry": prtGenTsEntry,
       "prtGenTsCnfgIdx": prtGenTsCnfgIdx,
       "prtGenTsPrtIdx": prtGenTsPrtIdx,
       "prtGenTsIdx": prtGenTsIdx,
       "prtGenTsType": prtGenTsType,
       "prtGenTsIConPrt": prtGenTsIConPrt,
       "prtGenTsIConTs": prtGenTsIConTs,
       "prtAlr": prtAlr,
       "prtSAlarmTable": prtSAlarmTable,
       "prtSAlarmEntry": prtSAlarmEntry,
       "prtSAlarmIdx": prtSAlarmIdx,
       "prtSAlarmPrtIdx": prtSAlarmPrtIdx,
       "prtSAlarmCode": prtSAlarmCode,
       "prtSAlarmState": prtSAlarmState,
       "prtSAlarmMask": prtSAlarmMask,
       "prtSAlarmInvert": prtSAlarmInvert,
       "prtSAlarmOnOff": prtSAlarmOnOff,
       "prtSAlarmCounter": prtSAlarmCounter,
       "prtAlrMaskTable": prtAlrMaskTable,
       "prtAlrMaskEntry": prtAlrMaskEntry,
       "prtAlrMaskPrtIdx": prtAlrMaskPrtIdx,
       "prtAlrMask": prtAlrMask,
       "prtBertTable": prtBertTable,
       "prtBertEntry": prtBertEntry,
       "prtBertPrtIdx": prtBertPrtIdx,
       "prtBertPattern": prtBertPattern,
       "prtBertInjectRate": prtBertInjectRate,
       "prtBertInjectErrRateCmd": prtBertInjectErrRateCmd,
       "prtBertInjectSingleErrCmd": prtBertInjectSingleErrCmd,
       "prtBertRunTime": prtBertRunTime,
       "prtBertESs": prtBertESs,
       "prtBertSyncLoss": prtBertSyncLoss,
       "prtBertErrorBits": prtBertErrorBits,
       "prtBertClearCounters": prtBertClearCounters,
       "prtBertSyncStatus": prtBertSyncStatus,
       "prtBertTs": prtBertTs,
       "prtBertResult": prtBertResult,
       "prtBertTxBits": prtBertTxBits,
       "prtBertRxBits": prtBertRxBits,
       "prtBertTxErrorBits": prtBertTxErrorBits,
       "prtMonTable": prtMonTable,
       "prtMonEntry": prtMonEntry,
       "prtMonCnfgIdx": prtMonCnfgIdx,
       "prtMonitoringIdx": prtMonitoringIdx,
       "prtMonitoringEnable": prtMonitoringEnable,
       "prtMonitoringTSs": prtMonitoringTSs,
       "prtMonitoredPort": prtMonitoredPort,
       "prtMonitoredTSs": prtMonitoredTSs,
       "prtCfgParam": prtCfgParam,
       "prtCfgParamTable": prtCfgParamTable,
       "prtCfgParamEntry": prtCfgParamEntry,
       "prtCfgParamCnfgIdx": prtCfgParamCnfgIdx,
       "prtCfgParamIdx": prtCfgParamIdx,
       "prtCfgParamSlt": prtCfgParamSlt,
       "prtCfgParamOperatedMl": prtCfgParamOperatedMl,
       "prtCfgParamMlAtoMlBPrio": prtCfgParamMlAtoMlBPrio,
       "prtCfgParamMlBtoMlAPrio": prtCfgParamMlBtoMlAPrio,
       "prtCfgParamInbandLoopDetection": prtCfgParamInbandLoopDetection,
       "prtCfgParamInbandLoopPatternCfg": prtCfgParamInbandLoopPatternCfg,
       "prtCfgParamInbandLoopActPattern": prtCfgParamInbandLoopActPattern,
       "prtCfgParamInbandLoopDeactPattern": prtCfgParamInbandLoopDeactPattern,
       "prtT1E1": prtT1E1,
       "prtT1E1StatTable": prtT1E1StatTable,
       "prtT1E1StatEntry": prtT1E1StatEntry,
       "prtT1E1SPrtIdx": prtT1E1SPrtIdx,
       "prtT1E1SSlt": prtT1E1SSlt,
       "prtT1E1OosCount": prtT1E1OosCount,
       "prtT1E1BpvLastMin": prtT1E1BpvLastMin,
       "prtT1E1BpvMax": prtT1E1BpvMax,
       "prtT1E1CnfgTable": prtT1E1CnfgTable,
       "prtT1E1CnfgEntry": prtT1E1CnfgEntry,
       "prtT1E1CnfgIdx": prtT1E1CnfgIdx,
       "prtT1E1PrtIdx": prtT1E1PrtIdx,
       "prtT1E1Slt": prtT1E1Slt,
       "prtT1E1LineType": prtT1E1LineType,
       "prtT1E1LineCode": prtT1E1LineCode,
       "prtT1E1SignalMode": prtT1E1SignalMode,
       "prtT1E1Fdl": prtT1E1Fdl,
       "prtT1E1FdlMode": prtT1E1FdlMode,
       "prtT1E1Sync": prtT1E1Sync,
       "prtT1E1CGA": prtT1E1CGA,
       "prtT1E1IdleCode": prtT1E1IdleCode,
       "prtT1E1OosSignal": prtT1E1OosSignal,
       "prtT1E1VoiceOos": prtT1E1VoiceOos,
       "prtT1E1DataOos": prtT1E1DataOos,
       "prtT1E1LineLengthMask": prtT1E1LineLengthMask,
       "prtT1E1TxGainMask": prtT1E1TxGainMask,
       "prtT1E1InbandMng": prtT1E1InbandMng,
       "prtT1E1InbandMngRate": prtT1E1InbandMngRate,
       "prtT1E1DedicatedTs": prtT1E1DedicatedTs,
       "prtT1E1InbandMngRoutProt": prtT1E1InbandMngRoutProt,
       "prtT1E1LinkMode": prtT1E1LinkMode,
       "prtT1E1Multiplier": prtT1E1Multiplier,
       "prtT1E1RxGain": prtT1E1RxGain,
       "prtT1E1RAI": prtT1E1RAI,
       "prtT1E1LineMode": prtT1E1LineMode,
       "prtT1E1TS0SaBits": prtT1E1TS0SaBits,
       "prtT1E1ConnectedTS": prtT1E1ConnectedTS,
       "prtT1E1Ts0SaBit": prtT1E1Ts0SaBit,
       "prtT1E1SameFeCnfg": prtT1E1SameFeCnfg,
       "prtT1E1RemCrc4": prtT1E1RemCrc4,
       "prtT1E1MaxTSs": prtT1E1MaxTSs,
       "prtT1E1EocTsConfig": prtT1E1EocTsConfig,
       "prtT1E1Role": prtT1E1Role,
       "prtT1E1PppEchoFailDetection": prtT1E1PppEchoFailDetection,
       "prtT1E1CasOosPattern": prtT1E1CasOosPattern,
       "prtT1E1CasOosSpaceCode": prtT1E1CasOosSpaceCode,
       "prtT1E1CasOosMarkCode": prtT1E1CasOosMarkCode,
       "prtT1E1FdlMsgTable": prtT1E1FdlMsgTable,
       "prtT1E1FdlMsgEntry": prtT1E1FdlMsgEntry,
       "prtT1E1FdlMsgPrtIdx": prtT1E1FdlMsgPrtIdx,
       "prtT1E1FdlMsgFdlType": prtT1E1FdlMsgFdlType,
       "prtT1E1FdlMsgSlt": prtT1E1FdlMsgSlt,
       "prtT1E1FdlMsg": prtT1E1FdlMsg,
       "prtHS": prtHS,
       "prtHSParamTable": prtHSParamTable,
       "prtHSParamEntry": prtHSParamEntry,
       "prtHSCnfgIdx": prtHSCnfgIdx,
       "prtHSPrtIdx": prtHSPrtIdx,
       "prtHSSlt": prtHSSlt,
       "prtHSRate": prtHSRate,
       "prtHSFifoSize": prtHSFifoSize,
       "prtHSClkMode": prtHSClkMode,
       "prtHSCTS": prtHSCTS,
       "prtHSRtsState": prtHSRtsState,
       "prtHSInbandLoopback": prtHSInbandLoopback,
       "prtHSInbandLoopPatternCfg": prtHSInbandLoopPatternCfg,
       "prtHSInbandLoopActPattern": prtHSInbandLoopActPattern,
       "prtHSInbandLoopDeactPattern": prtHSInbandLoopDeactPattern,
       "prtHSDCD": prtHSDCD,
       "prtHSClkPolarity": prtHSClkPolarity,
       "prtHSInterfaceType": prtHSInterfaceType,
       "prtHSUnframed": prtHSUnframed,
       "prtHSBertTable": prtHSBertTable,
       "prtHSBertEntry": prtHSBertEntry,
       "prtHSBertPrtIdx": prtHSBertPrtIdx,
       "prtHSBertSlt": prtHSBertSlt,
       "prtHSBertCountClr": prtHSBertCountClr,
       "prtHSBertTestResult": prtHSBertTestResult,
       "prtSP": prtSP,
       "prtSpCnfgTable": prtSpCnfgTable,
       "prtSpCnfgEntry": prtSpCnfgEntry,
       "prtSpCnfgIdx": prtSpCnfgIdx,
       "prtSpPrtIdx": prtSpPrtIdx,
       "prtSpUsage": prtSpUsage,
       "prtSpRate": prtSpRate,
       "prtSpDataBits": prtSpDataBits,
       "prtSpParity": prtSpParity,
       "prtSpCallOutMode": prtSpCallOutMode,
       "prtSpInterface": prtSpInterface,
       "prtSpCTS": prtSpCTS,
       "prtSpDcdDelay": prtSpDcdDelay,
       "prtSpDsr": prtSpDsr,
       "prtSpNoOfRetries": prtSpNoOfRetries,
       "prtSpWaitForConnect": prtSpWaitForConnect,
       "prtSpDialMode": prtSpDialMode,
       "prtSpAltNumMode": prtSpAltNumMode,
       "prtSpPrimaryNum": prtSpPrimaryNum,
       "prtSpAltNum": prtSpAltNum,
       "prtSpRoutProtocol": prtSpRoutProtocol,
       "prtSpCmd": prtSpCmd,
       "prtSpActCallOut": prtSpActCallOut,
       "prtSpAlrRelayMode": prtSpAlrRelayMode,
       "prtSpStopBits": prtSpStopBits,
       "prtDim": prtDim,
       "prtDimCnfgTable": prtDimCnfgTable,
       "prtDimCnfgEntry": prtDimCnfgEntry,
       "prtDimCnfgIdx": prtDimCnfgIdx,
       "prtDimIdx": prtDimIdx,
       "prtDimTxMode": prtDimTxMode,
       "prtDimPolarity": prtDimPolarity,
       "prtDimClkMode": prtDimClkMode,
       "prtDimMaxDelay": prtDimMaxDelay,
       "prtDimMng": prtDimMng,
       "prtDimMngRoutProt": prtDimMngRoutProt,
       "prtDimDestTable": prtDimDestTable,
       "prtDimDestEntry": prtDimDestEntry,
       "prtDestCnfgIdx": prtDestCnfgIdx,
       "prtDestDimIdx": prtDestDimIdx,
       "prtDestIdx": prtDestIdx,
       "prtDest": prtDest,
       "prtDestConnect": prtDestConnect,
       "prtI": prtI,
       "prtICnfgTable": prtICnfgTable,
       "prtICnfgEntry": prtICnfgEntry,
       "prtICnfgIdx": prtICnfgIdx,
       "prtIIdx": prtIIdx,
       "prtIRate": prtIRate,
       "prtIConnect": prtIConnect,
       "prtHdsl": prtHdsl,
       "prtHdslTable": prtHdslTable,
       "prtHdslEntry": prtHdslEntry,
       "prtHdslIdx": prtHdslIdx,
       "prtHdslMode": prtHdslMode,
       "prtHdslRptrType": prtHdslRptrType,
       "prtHdslMaxRate": prtHdslMaxRate,
       "prtHdslLinkType": prtHdslLinkType,
       "prtHdslCompSwVer": prtHdslCompSwVer,
       "prtHdslCompHwVer": prtHdslCompHwVer,
       "prtT3E3": prtT3E3,
       "prtT3E3CnfgTable": prtT3E3CnfgTable,
       "prtT3E3CnfgEntry": prtT3E3CnfgEntry,
       "prtT3E3CnfgIdx": prtT3E3CnfgIdx,
       "prtT3E3PrtIdx": prtT3E3PrtIdx,
       "prtT3E3Slt": prtT3E3Slt,
       "prtT3E3LineLength": prtT3E3LineLength,
       "prtT3E3InbandMng": prtT3E3InbandMng,
       "prtT3E3AisFrame": prtT3E3AisFrame,
       "prtT3E3TxClockSource": prtT3E3TxClockSource,
       "prtT3E3RoutProt": prtT3E3RoutProt,
       "prtT3E3AisTransmit": prtT3E3AisTransmit,
       "genDacsMux": genDacsMux,
       "cmprTable": cmprTable,
       "cmprEntry": cmprEntry,
       "cmprTypeIdx": cmprTypeIdx,
       "cmprCnfgIdx": cmprCnfgIdx,
       "cmprVersion": cmprVersion,
       "cmprSltIdx": cmprSltIdx,
       "cmprPrtIdx": cmprPrtIdx,
       "cmprObj": cmprObj,
       "mapLinkTable": mapLinkTable,
       "mapLinkEntry": mapLinkEntry,
       "mapLinkIdx": mapLinkIdx,
       "mapLinkSlotIdx": mapLinkSlotIdx,
       "mapLinkPortIdx": mapLinkPortIdx,
       "mapLinkState": mapLinkState,
       "alrGenTable": alrGenTable,
       "alrGenEntry": alrGenEntry,
       "alrGenCode": alrGenCode,
       "alrGenDescription": alrGenDescription,
       "alrGenLevel": alrGenLevel,
       "alrGenSlotType": alrGenSlotType,
       "alrGenSeverity": alrGenSeverity,
       "alrGenDebounce": alrGenDebounce,
       "alrGenDefSeverity": alrGenDefSeverity,
       "powerDeliveryFailure": powerDeliveryFailure}
)
