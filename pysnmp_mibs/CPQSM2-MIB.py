# SNMP MIB module (CPQSM2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/CPQSM2-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:38:18 2025
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

(compaq,
 cpqHoGUIDCanonical,
 cpqHoTrapFlags) = mibBuilder.importSymbols(
    "CPQHOST-MIB",
    "compaq",
    "cpqHoGUIDCanonical",
    "cpqHoTrapFlags")

(cpqSiAssetTag,
 cpqSiProductName,
 cpqSiSysProductId,
 cpqSiSysSerialNum) = mibBuilder.importSymbols(
    "CPQSINFO-MIB",
    "cpqSiAssetTag",
    "cpqSiProductName",
    "cpqSiSysProductId",
    "cpqSiSysSerialNum")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CpqSm2_ObjectIdentity = ObjectIdentity
cpqSm2 = _CpqSm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 9)
)
_CpqSm2MibRev_ObjectIdentity = ObjectIdentity
cpqSm2MibRev = _CpqSm2MibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 9, 1)
)


class _CpqSm2MibRevMajor_Type(Integer32):
    """Custom type cpqSm2MibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpqSm2MibRevMajor_Type.__name__ = "Integer32"
_CpqSm2MibRevMajor_Object = MibScalar
cpqSm2MibRevMajor = _CpqSm2MibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 1, 1),
    _CpqSm2MibRevMajor_Type()
)
cpqSm2MibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2MibRevMajor.setStatus("mandatory")


class _CpqSm2MibRevMinor_Type(Integer32):
    """Custom type cpqSm2MibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSm2MibRevMinor_Type.__name__ = "Integer32"
_CpqSm2MibRevMinor_Object = MibScalar
cpqSm2MibRevMinor = _CpqSm2MibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 1, 2),
    _CpqSm2MibRevMinor_Type()
)
cpqSm2MibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2MibRevMinor.setStatus("mandatory")


class _CpqSm2MibCondition_Type(Integer32):
    """Custom type cpqSm2MibCondition based on Integer32"""
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
          ("ok", 2),
          ("degraded", 3),
          ("failed", 4))
    )


_CpqSm2MibCondition_Type.__name__ = "Integer32"
_CpqSm2MibCondition_Object = MibScalar
cpqSm2MibCondition = _CpqSm2MibCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 1, 3),
    _CpqSm2MibCondition_Type()
)
cpqSm2MibCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2MibCondition.setStatus("mandatory")
_CpqSm2Component_ObjectIdentity = ObjectIdentity
cpqSm2Component = _CpqSm2Component_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 9, 2)
)
_CpqSm2Interface_ObjectIdentity = ObjectIdentity
cpqSm2Interface = _CpqSm2Interface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 1)
)
_CpqSm2OsCommon_ObjectIdentity = ObjectIdentity
cpqSm2OsCommon = _CpqSm2OsCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 1, 4)
)


class _CpqSm2OsCommonPollFreq_Type(Integer32):
    """Custom type cpqSm2OsCommonPollFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSm2OsCommonPollFreq_Type.__name__ = "Integer32"
_CpqSm2OsCommonPollFreq_Object = MibScalar
cpqSm2OsCommonPollFreq = _CpqSm2OsCommonPollFreq_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 1, 4, 1),
    _CpqSm2OsCommonPollFreq_Type()
)
cpqSm2OsCommonPollFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqSm2OsCommonPollFreq.setStatus("mandatory")
_CpqSm2OsCommonModuleTable_Object = MibTable
cpqSm2OsCommonModuleTable = _CpqSm2OsCommonModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cpqSm2OsCommonModuleTable.setStatus("deprecated")
_CpqSm2OsCommonModuleEntry_Object = MibTableRow
cpqSm2OsCommonModuleEntry = _CpqSm2OsCommonModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 1, 4, 2, 1)
)
cpqSm2OsCommonModuleEntry.setIndexNames(
    (0, "CPQSM2-MIB", "cpqSm2OsCommonModuleIndex"),
)
if mibBuilder.loadTexts:
    cpqSm2OsCommonModuleEntry.setStatus("deprecated")


class _CpqSm2OsCommonModuleIndex_Type(Integer32):
    """Custom type cpqSm2OsCommonModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSm2OsCommonModuleIndex_Type.__name__ = "Integer32"
_CpqSm2OsCommonModuleIndex_Object = MibTableColumn
cpqSm2OsCommonModuleIndex = _CpqSm2OsCommonModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 1, 4, 2, 1, 1),
    _CpqSm2OsCommonModuleIndex_Type()
)
cpqSm2OsCommonModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2OsCommonModuleIndex.setStatus("deprecated")


class _CpqSm2OsCommonModuleName_Type(DisplayString):
    """Custom type cpqSm2OsCommonModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSm2OsCommonModuleName_Type.__name__ = "DisplayString"
_CpqSm2OsCommonModuleName_Object = MibTableColumn
cpqSm2OsCommonModuleName = _CpqSm2OsCommonModuleName_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 1, 4, 2, 1, 2),
    _CpqSm2OsCommonModuleName_Type()
)
cpqSm2OsCommonModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2OsCommonModuleName.setStatus("deprecated")


class _CpqSm2OsCommonModuleVersion_Type(DisplayString):
    """Custom type cpqSm2OsCommonModuleVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_CpqSm2OsCommonModuleVersion_Type.__name__ = "DisplayString"
_CpqSm2OsCommonModuleVersion_Object = MibTableColumn
cpqSm2OsCommonModuleVersion = _CpqSm2OsCommonModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 1, 4, 2, 1, 3),
    _CpqSm2OsCommonModuleVersion_Type()
)
cpqSm2OsCommonModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2OsCommonModuleVersion.setStatus("deprecated")


class _CpqSm2OsCommonModuleDate_Type(OctetString):
    """Custom type cpqSm2OsCommonModuleDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )
    fixed_length = 7


_CpqSm2OsCommonModuleDate_Type.__name__ = "OctetString"
_CpqSm2OsCommonModuleDate_Object = MibTableColumn
cpqSm2OsCommonModuleDate = _CpqSm2OsCommonModuleDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 1, 4, 2, 1, 4),
    _CpqSm2OsCommonModuleDate_Type()
)
cpqSm2OsCommonModuleDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2OsCommonModuleDate.setStatus("deprecated")


class _CpqSm2OsCommonModulePurpose_Type(DisplayString):
    """Custom type cpqSm2OsCommonModulePurpose based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSm2OsCommonModulePurpose_Type.__name__ = "DisplayString"
_CpqSm2OsCommonModulePurpose_Object = MibTableColumn
cpqSm2OsCommonModulePurpose = _CpqSm2OsCommonModulePurpose_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 1, 4, 2, 1, 5),
    _CpqSm2OsCommonModulePurpose_Type()
)
cpqSm2OsCommonModulePurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2OsCommonModulePurpose.setStatus("deprecated")
_CpqSm2Cntlr_ObjectIdentity = ObjectIdentity
cpqSm2Cntlr = _CpqSm2Cntlr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 2)
)


class _CpqSm2CntlrRomDate_Type(DisplayString):
    """Custom type cpqSm2CntlrRomDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CpqSm2CntlrRomDate_Type.__name__ = "DisplayString"
_CpqSm2CntlrRomDate_Object = MibScalar
cpqSm2CntlrRomDate = _CpqSm2CntlrRomDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 2, 1),
    _CpqSm2CntlrRomDate_Type()
)
cpqSm2CntlrRomDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CntlrRomDate.setStatus("mandatory")


class _CpqSm2CntlrRomRevision_Type(DisplayString):
    """Custom type cpqSm2CntlrRomRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_CpqSm2CntlrRomRevision_Type.__name__ = "DisplayString"
_CpqSm2CntlrRomRevision_Object = MibScalar
cpqSm2CntlrRomRevision = _CpqSm2CntlrRomRevision_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 2, 2),
    _CpqSm2CntlrRomRevision_Type()
)
cpqSm2CntlrRomRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CntlrRomRevision.setStatus("mandatory")


class _CpqSm2CntlrVideoStatus_Type(Integer32):
    """Custom type cpqSm2CntlrVideoStatus based on Integer32"""
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
          ("enabled", 2),
          ("disabled", 3))
    )


_CpqSm2CntlrVideoStatus_Type.__name__ = "Integer32"
_CpqSm2CntlrVideoStatus_Object = MibScalar
cpqSm2CntlrVideoStatus = _CpqSm2CntlrVideoStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 2, 3),
    _CpqSm2CntlrVideoStatus_Type()
)
cpqSm2CntlrVideoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CntlrVideoStatus.setStatus("mandatory")


class _CpqSm2CntlrBatteryEnabled_Type(Integer32):
    """Custom type cpqSm2CntlrBatteryEnabled based on Integer32"""
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
          ("enabled", 2),
          ("disabled", 3),
          ("noBattery", 4))
    )


_CpqSm2CntlrBatteryEnabled_Type.__name__ = "Integer32"
_CpqSm2CntlrBatteryEnabled_Object = MibScalar
cpqSm2CntlrBatteryEnabled = _CpqSm2CntlrBatteryEnabled_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 2, 4),
    _CpqSm2CntlrBatteryEnabled_Type()
)
cpqSm2CntlrBatteryEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqSm2CntlrBatteryEnabled.setStatus("mandatory")


class _CpqSm2CntlrBatteryStatus_Type(Integer32):
    """Custom type cpqSm2CntlrBatteryStatus based on Integer32"""
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
          ("batteryOk", 2),
          ("batteryFailed", 3),
          ("batteryDisconnected", 4))
    )


_CpqSm2CntlrBatteryStatus_Type.__name__ = "Integer32"
_CpqSm2CntlrBatteryStatus_Object = MibScalar
cpqSm2CntlrBatteryStatus = _CpqSm2CntlrBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 2, 5),
    _CpqSm2CntlrBatteryStatus_Type()
)
cpqSm2CntlrBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CntlrBatteryStatus.setStatus("mandatory")


class _CpqSm2CntlrBatteryPercentCharged_Type(Integer32):
    """Custom type cpqSm2CntlrBatteryPercentCharged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpqSm2CntlrBatteryPercentCharged_Type.__name__ = "Integer32"
_CpqSm2CntlrBatteryPercentCharged_Object = MibScalar
cpqSm2CntlrBatteryPercentCharged = _CpqSm2CntlrBatteryPercentCharged_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 2, 6),
    _CpqSm2CntlrBatteryPercentCharged_Type()
)
cpqSm2CntlrBatteryPercentCharged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CntlrBatteryPercentCharged.setStatus("mandatory")


class _CpqSm2CntlrAlertStatus_Type(Integer32):
    """Custom type cpqSm2CntlrAlertStatus based on Integer32"""
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
          ("enabled", 2),
          ("disabled", 3))
    )


_CpqSm2CntlrAlertStatus_Type.__name__ = "Integer32"
_CpqSm2CntlrAlertStatus_Object = MibScalar
cpqSm2CntlrAlertStatus = _CpqSm2CntlrAlertStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 2, 7),
    _CpqSm2CntlrAlertStatus_Type()
)
cpqSm2CntlrAlertStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqSm2CntlrAlertStatus.setStatus("mandatory")


class _CpqSm2CntlrPendingAlerts_Type(Integer32):
    """Custom type cpqSm2CntlrPendingAlerts based on Integer32"""
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
          ("noAlertsPending", 2),
          ("alertsPending", 3),
          ("clearPendingAlerts", 4))
    )


_CpqSm2CntlrPendingAlerts_Type.__name__ = "Integer32"
_CpqSm2CntlrPendingAlerts_Object = MibScalar
cpqSm2CntlrPendingAlerts = _CpqSm2CntlrPendingAlerts_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 2, 8),
    _CpqSm2CntlrPendingAlerts_Type()
)
cpqSm2CntlrPendingAlerts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqSm2CntlrPendingAlerts.setStatus("mandatory")
_CpqSm2CntlrSelfTestErrors_Type = Integer32
_CpqSm2CntlrSelfTestErrors_Object = MibScalar
cpqSm2CntlrSelfTestErrors = _CpqSm2CntlrSelfTestErrors_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 2, 9),
    _CpqSm2CntlrSelfTestErrors_Type()
)
cpqSm2CntlrSelfTestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CntlrSelfTestErrors.setStatus("mandatory")


class _CpqSm2CntlrAgentLocation_Type(Integer32):
    """Custom type cpqSm2CntlrAgentLocation based on Integer32"""
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
        *(("hostOsAgent", 1),
          ("firmwareAgent", 2),
          ("remoteInsightPciFirmwareAgent", 3),
          ("enclosureFirmwareAgent", 4))
    )


_CpqSm2CntlrAgentLocation_Type.__name__ = "Integer32"
_CpqSm2CntlrAgentLocation_Object = MibScalar
cpqSm2CntlrAgentLocation = _CpqSm2CntlrAgentLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 2, 10),
    _CpqSm2CntlrAgentLocation_Type()
)
cpqSm2CntlrAgentLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CntlrAgentLocation.setStatus("mandatory")


class _CpqSm2CntlrLastDataUpdate_Type(OctetString):
    """Custom type cpqSm2CntlrLastDataUpdate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )
    fixed_length = 7


_CpqSm2CntlrLastDataUpdate_Type.__name__ = "OctetString"
_CpqSm2CntlrLastDataUpdate_Object = MibScalar
cpqSm2CntlrLastDataUpdate = _CpqSm2CntlrLastDataUpdate_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 2, 11),
    _CpqSm2CntlrLastDataUpdate_Type()
)
cpqSm2CntlrLastDataUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CntlrLastDataUpdate.setStatus("deprecated")


class _CpqSm2CntlrDataStatus_Type(Integer32):
    """Custom type cpqSm2CntlrDataStatus based on Integer32"""
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
          ("noData", 2),
          ("onlineData", 3),
          ("offlineData", 4))
    )


_CpqSm2CntlrDataStatus_Type.__name__ = "Integer32"
_CpqSm2CntlrDataStatus_Object = MibScalar
cpqSm2CntlrDataStatus = _CpqSm2CntlrDataStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 2, 12),
    _CpqSm2CntlrDataStatus_Type()
)
cpqSm2CntlrDataStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CntlrDataStatus.setStatus("mandatory")


class _CpqSm2CntlrColdReboot_Type(Integer32):
    """Custom type cpqSm2CntlrColdReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 1),
          ("available", 2),
          ("doColdReboot", 3))
    )


_CpqSm2CntlrColdReboot_Type.__name__ = "Integer32"
_CpqSm2CntlrColdReboot_Object = MibScalar
cpqSm2CntlrColdReboot = _CpqSm2CntlrColdReboot_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 2, 13),
    _CpqSm2CntlrColdReboot_Type()
)
cpqSm2CntlrColdReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqSm2CntlrColdReboot.setStatus("mandatory")
_CpqSm2CntlrBadLoginAttemptsThresh_Type = Integer32
_CpqSm2CntlrBadLoginAttemptsThresh_Object = MibScalar
cpqSm2CntlrBadLoginAttemptsThresh = _CpqSm2CntlrBadLoginAttemptsThresh_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 2, 14),
    _CpqSm2CntlrBadLoginAttemptsThresh_Type()
)
cpqSm2CntlrBadLoginAttemptsThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CntlrBadLoginAttemptsThresh.setStatus("mandatory")


class _CpqSm2CntlrBoardSerialNumber_Type(DisplayString):
    """Custom type cpqSm2CntlrBoardSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CpqSm2CntlrBoardSerialNumber_Type.__name__ = "DisplayString"
_CpqSm2CntlrBoardSerialNumber_Object = MibScalar
cpqSm2CntlrBoardSerialNumber = _CpqSm2CntlrBoardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 2, 15),
    _CpqSm2CntlrBoardSerialNumber_Type()
)
cpqSm2CntlrBoardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CntlrBoardSerialNumber.setStatus("mandatory")


class _CpqSm2CntlrRemoteSessionStatus_Type(Integer32):
    """Custom type cpqSm2CntlrRemoteSessionStatus based on Integer32"""
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
          ("active", 2),
          ("inactive", 3))
    )


_CpqSm2CntlrRemoteSessionStatus_Type.__name__ = "Integer32"
_CpqSm2CntlrRemoteSessionStatus_Object = MibScalar
cpqSm2CntlrRemoteSessionStatus = _CpqSm2CntlrRemoteSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 2, 16),
    _CpqSm2CntlrRemoteSessionStatus_Type()
)
cpqSm2CntlrRemoteSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CntlrRemoteSessionStatus.setStatus("mandatory")


class _CpqSm2CntlrInterfaceStatus_Type(Integer32):
    """Custom type cpqSm2CntlrInterfaceStatus based on Integer32"""
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
          ("ok", 2),
          ("notResponding", 3))
    )


_CpqSm2CntlrInterfaceStatus_Type.__name__ = "Integer32"
_CpqSm2CntlrInterfaceStatus_Object = MibScalar
cpqSm2CntlrInterfaceStatus = _CpqSm2CntlrInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 2, 17),
    _CpqSm2CntlrInterfaceStatus_Type()
)
cpqSm2CntlrInterfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CntlrInterfaceStatus.setStatus("mandatory")


class _CpqSm2CntlrSystemId_Type(DisplayString):
    """Custom type cpqSm2CntlrSystemId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_CpqSm2CntlrSystemId_Type.__name__ = "DisplayString"
_CpqSm2CntlrSystemId_Object = MibScalar
cpqSm2CntlrSystemId = _CpqSm2CntlrSystemId_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 2, 18),
    _CpqSm2CntlrSystemId_Type()
)
cpqSm2CntlrSystemId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqSm2CntlrSystemId.setStatus("mandatory")


class _CpqSm2CntlrKeyboardCableStatus_Type(Integer32):
    """Custom type cpqSm2CntlrKeyboardCableStatus based on Integer32"""
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
          ("connected", 2),
          ("disconnected", 3))
    )


_CpqSm2CntlrKeyboardCableStatus_Type.__name__ = "Integer32"
_CpqSm2CntlrKeyboardCableStatus_Object = MibScalar
cpqSm2CntlrKeyboardCableStatus = _CpqSm2CntlrKeyboardCableStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 2, 19),
    _CpqSm2CntlrKeyboardCableStatus_Type()
)
cpqSm2CntlrKeyboardCableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CntlrKeyboardCableStatus.setStatus("mandatory")
_CpqSm2ServerIpAddress_Type = IpAddress
_CpqSm2ServerIpAddress_Object = MibScalar
cpqSm2ServerIpAddress = _CpqSm2ServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 2, 20),
    _CpqSm2ServerIpAddress_Type()
)
cpqSm2ServerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2ServerIpAddress.setStatus("mandatory")


class _CpqSm2CntlrModel_Type(Integer32):
    """Custom type cpqSm2CntlrModel based on Integer32"""
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
        *(("other", 1),
          ("eisaRemoteInsightBoard", 2),
          ("pciRemoteInsightBoard", 3),
          ("pciLightsOutRemoteInsightBoard", 4),
          ("pciIntegratedLightsOutRemoteInsight", 5),
          ("pciLightsOutRemoteInsightBoardII", 6),
          ("pciIntegratedLightsOutRemoteInsight2", 7),
          ("pciLightsOut100series", 8),
          ("pciIntegratedLightsOutRemoteInsight3", 9),
          ("pciIntegratedLightsOutRemoteInsight4", 10),
          ("pciIntegratedLightsOutRemoteInsight5", 11))
    )


_CpqSm2CntlrModel_Type.__name__ = "Integer32"
_CpqSm2CntlrModel_Object = MibScalar
cpqSm2CntlrModel = _CpqSm2CntlrModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 2, 21),
    _CpqSm2CntlrModel_Type()
)
cpqSm2CntlrModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CntlrModel.setStatus("mandatory")
_CpqSm2CntlrSelfTestErrorMask_Type = Integer32
_CpqSm2CntlrSelfTestErrorMask_Object = MibScalar
cpqSm2CntlrSelfTestErrorMask = _CpqSm2CntlrSelfTestErrorMask_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 2, 22),
    _CpqSm2CntlrSelfTestErrorMask_Type()
)
cpqSm2CntlrSelfTestErrorMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CntlrSelfTestErrorMask.setStatus("mandatory")


class _CpqSm2CntlrMouseCableStatus_Type(Integer32):
    """Custom type cpqSm2CntlrMouseCableStatus based on Integer32"""
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
          ("connected", 2),
          ("disconnected", 3))
    )


_CpqSm2CntlrMouseCableStatus_Type.__name__ = "Integer32"
_CpqSm2CntlrMouseCableStatus_Object = MibScalar
cpqSm2CntlrMouseCableStatus = _CpqSm2CntlrMouseCableStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 2, 23),
    _CpqSm2CntlrMouseCableStatus_Type()
)
cpqSm2CntlrMouseCableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CntlrMouseCableStatus.setStatus("mandatory")


class _CpqSm2CntlrVirtualPowerCableStatus_Type(Integer32):
    """Custom type cpqSm2CntlrVirtualPowerCableStatus based on Integer32"""
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
          ("connected", 2),
          ("disconnected", 3),
          ("notApplicable", 4))
    )


_CpqSm2CntlrVirtualPowerCableStatus_Type.__name__ = "Integer32"
_CpqSm2CntlrVirtualPowerCableStatus_Object = MibScalar
cpqSm2CntlrVirtualPowerCableStatus = _CpqSm2CntlrVirtualPowerCableStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 2, 24),
    _CpqSm2CntlrVirtualPowerCableStatus_Type()
)
cpqSm2CntlrVirtualPowerCableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CntlrVirtualPowerCableStatus.setStatus("mandatory")


class _CpqSm2CntlrExternalPowerCableStatus_Type(Integer32):
    """Custom type cpqSm2CntlrExternalPowerCableStatus based on Integer32"""
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
        *(("other", 1),
          ("externallyConnected", 2),
          ("disconnected", 3),
          ("internallyConnected", 4),
          ("externallyAndInternallyConnected", 5),
          ("notApplicable", 6))
    )


_CpqSm2CntlrExternalPowerCableStatus_Type.__name__ = "Integer32"
_CpqSm2CntlrExternalPowerCableStatus_Object = MibScalar
cpqSm2CntlrExternalPowerCableStatus = _CpqSm2CntlrExternalPowerCableStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 2, 25),
    _CpqSm2CntlrExternalPowerCableStatus_Type()
)
cpqSm2CntlrExternalPowerCableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CntlrExternalPowerCableStatus.setStatus("mandatory")


class _CpqSm2CntlrHostGUID_Type(OctetString):
    """Custom type cpqSm2CntlrHostGUID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_CpqSm2CntlrHostGUID_Type.__name__ = "OctetString"
_CpqSm2CntlrHostGUID_Object = MibScalar
cpqSm2CntlrHostGUID = _CpqSm2CntlrHostGUID_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 2, 26),
    _CpqSm2CntlrHostGUID_Type()
)
cpqSm2CntlrHostGUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CntlrHostGUID.setStatus("mandatory")


class _CpqSm2CntlriLOSecurityOverrideSwitchState_Type(Integer32):
    """Custom type cpqSm2CntlriLOSecurityOverrideSwitchState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("set", 2),
          ("notSet", 3))
    )


_CpqSm2CntlriLOSecurityOverrideSwitchState_Type.__name__ = "Integer32"
_CpqSm2CntlriLOSecurityOverrideSwitchState_Object = MibScalar
cpqSm2CntlriLOSecurityOverrideSwitchState = _CpqSm2CntlriLOSecurityOverrideSwitchState_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 2, 27),
    _CpqSm2CntlriLOSecurityOverrideSwitchState_Type()
)
cpqSm2CntlriLOSecurityOverrideSwitchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CntlriLOSecurityOverrideSwitchState.setStatus("mandatory")
_CpqSm2CntlrHardwareVer_Type = Integer32
_CpqSm2CntlrHardwareVer_Object = MibScalar
cpqSm2CntlrHardwareVer = _CpqSm2CntlrHardwareVer_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 2, 28),
    _CpqSm2CntlrHardwareVer_Type()
)
cpqSm2CntlrHardwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CntlrHardwareVer.setStatus("mandatory")
_CpqSm2CntlrAction_Type = Integer32
_CpqSm2CntlrAction_Object = MibScalar
cpqSm2CntlrAction = _CpqSm2CntlrAction_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 2, 29),
    _CpqSm2CntlrAction_Type()
)
cpqSm2CntlrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqSm2CntlrAction.setStatus("mandatory")


class _CpqSm2CntlrLicenseActive_Type(Integer32):
    """Custom type cpqSm2CntlrLicenseActive based on Integer32"""
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
        *(("none", 1),
          ("iloAdvanced", 2),
          ("iloLight", 3),
          ("iloAdvancedBlade", 4),
          ("iloStandard", 5),
          ("iloEssentials", 6),
          ("iloScaleOut", 7),
          ("iloAdvancedPremiumSecurity", 8))
    )


_CpqSm2CntlrLicenseActive_Type.__name__ = "Integer32"
_CpqSm2CntlrLicenseActive_Object = MibScalar
cpqSm2CntlrLicenseActive = _CpqSm2CntlrLicenseActive_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 2, 30),
    _CpqSm2CntlrLicenseActive_Type()
)
cpqSm2CntlrLicenseActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CntlrLicenseActive.setStatus("mandatory")


class _CpqSm2CntlrLicenseKey_Type(DisplayString):
    """Custom type cpqSm2CntlrLicenseKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_CpqSm2CntlrLicenseKey_Type.__name__ = "DisplayString"
_CpqSm2CntlrLicenseKey_Object = MibScalar
cpqSm2CntlrLicenseKey = _CpqSm2CntlrLicenseKey_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 2, 31),
    _CpqSm2CntlrLicenseKey_Type()
)
cpqSm2CntlrLicenseKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CntlrLicenseKey.setStatus("mandatory")


class _CpqSm2CntlrServerPowerState_Type(Integer32):
    """Custom type cpqSm2CntlrServerPowerState based on Integer32"""
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
          ("poweredOff", 2),
          ("poweredOn", 3),
          ("insufficientPowerOrPowerOnDenied", 4))
    )


_CpqSm2CntlrServerPowerState_Type.__name__ = "Integer32"
_CpqSm2CntlrServerPowerState_Object = MibScalar
cpqSm2CntlrServerPowerState = _CpqSm2CntlrServerPowerState_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 2, 32),
    _CpqSm2CntlrServerPowerState_Type()
)
cpqSm2CntlrServerPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CntlrServerPowerState.setStatus("mandatory")


class _CpqSm2CntlrSysAutoShutdownCause_Type(Integer32):
    """Custom type cpqSm2CntlrSysAutoShutdownCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              129,
              130,
              131,
              132,
              133,
              134,
              135)
        )
    )
    namedValues = NamedValues(
        *(("fanFailure", 1),
          ("overheatCondition", 2),
          ("vrmFailure", 3),
          ("powerSupplyFailure", 4),
          ("systemRunningOnBatteryBackupUnit", 5),
          ("aborted", 129),
          ("fanFailureAborted", 130),
          ("overheatAborted", 131),
          ("vrmFailureAborted", 132),
          ("softPowerDown", 133),
          ("softwareAutomaticServerRecovery", 134),
          ("powerSupplyFailureAborted", 135))
    )


_CpqSm2CntlrSysAutoShutdownCause_Type.__name__ = "Integer32"
_CpqSm2CntlrSysAutoShutdownCause_Object = MibScalar
cpqSm2CntlrSysAutoShutdownCause = _CpqSm2CntlrSysAutoShutdownCause_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 2, 33),
    _CpqSm2CntlrSysAutoShutdownCause_Type()
)
cpqSm2CntlrSysAutoShutdownCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CntlrSysAutoShutdownCause.setStatus("mandatory")


class _CpqSm2CntlrSecurityState_Type(Integer32):
    """Custom type cpqSm2CntlrSecurityState based on Integer32"""
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
        *(("factory", 1),
          ("wipe", 2),
          ("production", 3),
          ("highSecurity", 4),
          ("fips", 5),
          ("cnsa", 6))
    )


_CpqSm2CntlrSecurityState_Type.__name__ = "Integer32"
_CpqSm2CntlrSecurityState_Object = MibScalar
cpqSm2CntlrSecurityState = _CpqSm2CntlrSecurityState_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 2, 34),
    _CpqSm2CntlrSecurityState_Type()
)
cpqSm2CntlrSecurityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CntlrSecurityState.setStatus("mandatory")


class _CpqSm2WDTimerType_Type(Integer32):
    """Custom type cpqSm2WDTimerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("ipmi", 2))
    )


_CpqSm2WDTimerType_Type.__name__ = "Integer32"
_CpqSm2WDTimerType_Object = MibScalar
cpqSm2WDTimerType = _CpqSm2WDTimerType_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 2, 35),
    _CpqSm2WDTimerType_Type()
)
cpqSm2WDTimerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2WDTimerType.setStatus("mandatory")


class _CpqSm2WDTimerTimeoutDetails_Type(DisplayString):
    """Custom type cpqSm2WDTimerTimeoutDetails based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_CpqSm2WDTimerTimeoutDetails_Type.__name__ = "DisplayString"
_CpqSm2WDTimerTimeoutDetails_Object = MibScalar
cpqSm2WDTimerTimeoutDetails = _CpqSm2WDTimerTimeoutDetails_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 2, 36),
    _CpqSm2WDTimerTimeoutDetails_Type()
)
cpqSm2WDTimerTimeoutDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2WDTimerTimeoutDetails.setStatus("mandatory")


class _CpqSm2CntlrOverallSecStatus_Type(Integer32):
    """Custom type cpqSm2CntlrOverallSecStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("Ok", 1),
          ("Risk", 2),
          ("Ignored", 3))
    )


_CpqSm2CntlrOverallSecStatus_Type.__name__ = "Integer32"
_CpqSm2CntlrOverallSecStatus_Object = MibScalar
cpqSm2CntlrOverallSecStatus = _CpqSm2CntlrOverallSecStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 2, 37),
    _CpqSm2CntlrOverallSecStatus_Type()
)
cpqSm2CntlrOverallSecStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CntlrOverallSecStatus.setStatus("mandatory")
_CpqSm2EventLog_ObjectIdentity = ObjectIdentity
cpqSm2EventLog = _CpqSm2EventLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 3)
)
_CpqSm2EventTotalEntries_Type = Integer32
_CpqSm2EventTotalEntries_Object = MibScalar
cpqSm2EventTotalEntries = _CpqSm2EventTotalEntries_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 3, 1),
    _CpqSm2EventTotalEntries_Type()
)
cpqSm2EventTotalEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqSm2EventTotalEntries.setStatus("mandatory")
_CpqSm2EventLogTable_Object = MibTable
cpqSm2EventLogTable = _CpqSm2EventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 3, 2)
)
if mibBuilder.loadTexts:
    cpqSm2EventLogTable.setStatus("mandatory")
_CpqSm2EventLogEntry_Object = MibTableRow
cpqSm2EventLogEntry = _CpqSm2EventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 3, 2, 1)
)
cpqSm2EventLogEntry.setIndexNames(
    (0, "CPQSM2-MIB", "cpqSm2EventLogIndex"),
)
if mibBuilder.loadTexts:
    cpqSm2EventLogEntry.setStatus("mandatory")
_CpqSm2EventLogIndex_Type = Integer32
_CpqSm2EventLogIndex_Object = MibTableColumn
cpqSm2EventLogIndex = _CpqSm2EventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 3, 2, 1, 1),
    _CpqSm2EventLogIndex_Type()
)
cpqSm2EventLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2EventLogIndex.setStatus("mandatory")
_CpqSm2EventLogNumber_Type = Integer32
_CpqSm2EventLogNumber_Object = MibTableColumn
cpqSm2EventLogNumber = _CpqSm2EventLogNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 3, 2, 1, 2),
    _CpqSm2EventLogNumber_Type()
)
cpqSm2EventLogNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2EventLogNumber.setStatus("mandatory")


class _CpqSm2EventLogDate_Type(OctetString):
    """Custom type cpqSm2EventLogDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )
    fixed_length = 7


_CpqSm2EventLogDate_Type.__name__ = "OctetString"
_CpqSm2EventLogDate_Object = MibTableColumn
cpqSm2EventLogDate = _CpqSm2EventLogDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 3, 2, 1, 3),
    _CpqSm2EventLogDate_Type()
)
cpqSm2EventLogDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2EventLogDate.setStatus("mandatory")


class _CpqSm2EventLogMessage_Type(DisplayString):
    """Custom type cpqSm2EventLogMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CpqSm2EventLogMessage_Type.__name__ = "DisplayString"
_CpqSm2EventLogMessage_Object = MibTableColumn
cpqSm2EventLogMessage = _CpqSm2EventLogMessage_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 3, 2, 1, 4),
    _CpqSm2EventLogMessage_Type()
)
cpqSm2EventLogMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2EventLogMessage.setStatus("mandatory")
_CpqSm2AsyncComm_ObjectIdentity = ObjectIdentity
cpqSm2AsyncComm = _CpqSm2AsyncComm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 4)
)
_CpqSm2CommSettingsTable_Object = MibTable
cpqSm2CommSettingsTable = _CpqSm2CommSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 4, 1)
)
if mibBuilder.loadTexts:
    cpqSm2CommSettingsTable.setStatus("mandatory")
_CpqSm2CommSettingsEntry_Object = MibTableRow
cpqSm2CommSettingsEntry = _CpqSm2CommSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 4, 1, 1)
)
cpqSm2CommSettingsEntry.setIndexNames(
    (0, "CPQSM2-MIB", "cpqSm2CommPort"),
)
if mibBuilder.loadTexts:
    cpqSm2CommSettingsEntry.setStatus("mandatory")


class _CpqSm2CommPort_Type(Integer32):
    """Custom type cpqSm2CommPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("auxiliary", 2))
    )


_CpqSm2CommPort_Type.__name__ = "Integer32"
_CpqSm2CommPort_Object = MibTableColumn
cpqSm2CommPort = _CpqSm2CommPort_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 4, 1, 1, 1),
    _CpqSm2CommPort_Type()
)
cpqSm2CommPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CommPort.setStatus("mandatory")


class _CpqSm2CommType_Type(Integer32):
    """Custom type cpqSm2CommType based on Integer32"""
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
        *(("other", 1),
          ("none", 2),
          ("modem", 3),
          ("nulModemCable", 4),
          ("xonXoff", 5))
    )


_CpqSm2CommType_Type.__name__ = "Integer32"
_CpqSm2CommType_Object = MibTableColumn
cpqSm2CommType = _CpqSm2CommType_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 4, 1, 1, 2),
    _CpqSm2CommType_Type()
)
cpqSm2CommType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CommType.setStatus("mandatory")
_CpqSm2CommBaudRate_Type = Integer32
_CpqSm2CommBaudRate_Object = MibTableColumn
cpqSm2CommBaudRate = _CpqSm2CommBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 4, 1, 1, 3),
    _CpqSm2CommBaudRate_Type()
)
cpqSm2CommBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CommBaudRate.setStatus("mandatory")


class _CpqSm2CommParity_Type(Integer32):
    """Custom type cpqSm2CommParity based on Integer32"""
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
          ("none", 2),
          ("odd", 3),
          ("even", 4))
    )


_CpqSm2CommParity_Type.__name__ = "Integer32"
_CpqSm2CommParity_Object = MibTableColumn
cpqSm2CommParity = _CpqSm2CommParity_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 4, 1, 1, 4),
    _CpqSm2CommParity_Type()
)
cpqSm2CommParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CommParity.setStatus("mandatory")


class _CpqSm2CommDataBits_Type(Integer32):
    """Custom type cpqSm2CommDataBits based on Integer32"""
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
          ("sevenBits", 2),
          ("eightBits", 3))
    )


_CpqSm2CommDataBits_Type.__name__ = "Integer32"
_CpqSm2CommDataBits_Object = MibTableColumn
cpqSm2CommDataBits = _CpqSm2CommDataBits_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 4, 1, 1, 5),
    _CpqSm2CommDataBits_Type()
)
cpqSm2CommDataBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CommDataBits.setStatus("mandatory")


class _CpqSm2CommStopBits_Type(Integer32):
    """Custom type cpqSm2CommStopBits based on Integer32"""
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
          ("oneBit", 2),
          ("twoBits", 3))
    )


_CpqSm2CommStopBits_Type.__name__ = "Integer32"
_CpqSm2CommStopBits_Object = MibTableColumn
cpqSm2CommStopBits = _CpqSm2CommStopBits_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 4, 1, 1, 6),
    _CpqSm2CommStopBits_Type()
)
cpqSm2CommStopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CommStopBits.setStatus("mandatory")


class _CpqSm2CommModemReset_Type(DisplayString):
    """Custom type cpqSm2CommModemReset based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 42),
    )


_CpqSm2CommModemReset_Type.__name__ = "DisplayString"
_CpqSm2CommModemReset_Object = MibTableColumn
cpqSm2CommModemReset = _CpqSm2CommModemReset_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 4, 1, 1, 7),
    _CpqSm2CommModemReset_Type()
)
cpqSm2CommModemReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CommModemReset.setStatus("mandatory")


class _CpqSm2CommModemInit_Type(DisplayString):
    """Custom type cpqSm2CommModemInit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 42),
    )


_CpqSm2CommModemInit_Type.__name__ = "DisplayString"
_CpqSm2CommModemInit_Object = MibTableColumn
cpqSm2CommModemInit = _CpqSm2CommModemInit_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 4, 1, 1, 8),
    _CpqSm2CommModemInit_Type()
)
cpqSm2CommModemInit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CommModemInit.setStatus("mandatory")


class _CpqSm2CommModemDialPrefix_Type(DisplayString):
    """Custom type cpqSm2CommModemDialPrefix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 42),
    )


_CpqSm2CommModemDialPrefix_Type.__name__ = "DisplayString"
_CpqSm2CommModemDialPrefix_Object = MibTableColumn
cpqSm2CommModemDialPrefix = _CpqSm2CommModemDialPrefix_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 4, 1, 1, 9),
    _CpqSm2CommModemDialPrefix_Type()
)
cpqSm2CommModemDialPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CommModemDialPrefix.setStatus("mandatory")


class _CpqSm2CommPortInit_Type(DisplayString):
    """Custom type cpqSm2CommPortInit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 42),
    )


_CpqSm2CommPortInit_Type.__name__ = "DisplayString"
_CpqSm2CommPortInit_Object = MibTableColumn
cpqSm2CommPortInit = _CpqSm2CommPortInit_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 4, 1, 1, 10),
    _CpqSm2CommPortInit_Type()
)
cpqSm2CommPortInit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CommPortInit.setStatus("mandatory")


class _CpqSm2CommDialin_Type(Integer32):
    """Custom type cpqSm2CommDialin based on Integer32"""
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
          ("enabled", 2),
          ("disabled", 3))
    )


_CpqSm2CommDialin_Type.__name__ = "Integer32"
_CpqSm2CommDialin_Object = MibTableColumn
cpqSm2CommDialin = _CpqSm2CommDialin_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 4, 1, 1, 11),
    _CpqSm2CommDialin_Type()
)
cpqSm2CommDialin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CommDialin.setStatus("mandatory")


class _CpqSm2CommDialbackRequired_Type(Integer32):
    """Custom type cpqSm2CommDialbackRequired based on Integer32"""
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
          ("required", 2),
          ("notRequired", 3))
    )


_CpqSm2CommDialbackRequired_Type.__name__ = "Integer32"
_CpqSm2CommDialbackRequired_Object = MibTableColumn
cpqSm2CommDialbackRequired = _CpqSm2CommDialbackRequired_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 4, 1, 1, 12),
    _CpqSm2CommDialbackRequired_Type()
)
cpqSm2CommDialbackRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CommDialbackRequired.setStatus("mandatory")


class _CpqSm2CommNonPppConnections_Type(Integer32):
    """Custom type cpqSm2CommNonPppConnections based on Integer32"""
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
          ("enabled", 2),
          ("disabled", 3))
    )


_CpqSm2CommNonPppConnections_Type.__name__ = "Integer32"
_CpqSm2CommNonPppConnections_Object = MibTableColumn
cpqSm2CommNonPppConnections = _CpqSm2CommNonPppConnections_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 4, 1, 1, 13),
    _CpqSm2CommNonPppConnections_Type()
)
cpqSm2CommNonPppConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CommNonPppConnections.setStatus("mandatory")


class _CpqSm2CommSnmpTrapDelivery_Type(Integer32):
    """Custom type cpqSm2CommSnmpTrapDelivery based on Integer32"""
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
          ("enabled", 2),
          ("disabled", 3))
    )


_CpqSm2CommSnmpTrapDelivery_Type.__name__ = "Integer32"
_CpqSm2CommSnmpTrapDelivery_Object = MibTableColumn
cpqSm2CommSnmpTrapDelivery = _CpqSm2CommSnmpTrapDelivery_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 4, 1, 1, 14),
    _CpqSm2CommSnmpTrapDelivery_Type()
)
cpqSm2CommSnmpTrapDelivery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CommSnmpTrapDelivery.setStatus("mandatory")


class _CpqSm2CommPageDelivery_Type(Integer32):
    """Custom type cpqSm2CommPageDelivery based on Integer32"""
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
          ("enabled", 2),
          ("disabled", 3))
    )


_CpqSm2CommPageDelivery_Type.__name__ = "Integer32"
_CpqSm2CommPageDelivery_Object = MibTableColumn
cpqSm2CommPageDelivery = _CpqSm2CommPageDelivery_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 4, 1, 1, 15),
    _CpqSm2CommPageDelivery_Type()
)
cpqSm2CommPageDelivery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CommPageDelivery.setStatus("mandatory")
_CpqSm2CommPagerBaudRate_Type = Integer32
_CpqSm2CommPagerBaudRate_Object = MibTableColumn
cpqSm2CommPagerBaudRate = _CpqSm2CommPagerBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 4, 1, 1, 16),
    _CpqSm2CommPagerBaudRate_Type()
)
cpqSm2CommPagerBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CommPagerBaudRate.setStatus("mandatory")


class _CpqSm2CommPagerParity_Type(Integer32):
    """Custom type cpqSm2CommPagerParity based on Integer32"""
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
          ("none", 2),
          ("odd", 3),
          ("even", 4))
    )


_CpqSm2CommPagerParity_Type.__name__ = "Integer32"
_CpqSm2CommPagerParity_Object = MibTableColumn
cpqSm2CommPagerParity = _CpqSm2CommPagerParity_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 4, 1, 1, 17),
    _CpqSm2CommPagerParity_Type()
)
cpqSm2CommPagerParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CommPagerParity.setStatus("mandatory")


class _CpqSm2CommPagerDataBits_Type(Integer32):
    """Custom type cpqSm2CommPagerDataBits based on Integer32"""
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
          ("sevenBits", 2),
          ("eightBits", 3))
    )


_CpqSm2CommPagerDataBits_Type.__name__ = "Integer32"
_CpqSm2CommPagerDataBits_Object = MibTableColumn
cpqSm2CommPagerDataBits = _CpqSm2CommPagerDataBits_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 4, 1, 1, 18),
    _CpqSm2CommPagerDataBits_Type()
)
cpqSm2CommPagerDataBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CommPagerDataBits.setStatus("mandatory")


class _CpqSm2CommPagerStopBits_Type(Integer32):
    """Custom type cpqSm2CommPagerStopBits based on Integer32"""
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
          ("oneBit", 2),
          ("twoBits", 3))
    )


_CpqSm2CommPagerStopBits_Type.__name__ = "Integer32"
_CpqSm2CommPagerStopBits_Object = MibTableColumn
cpqSm2CommPagerStopBits = _CpqSm2CommPagerStopBits_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 4, 1, 1, 19),
    _CpqSm2CommPagerStopBits_Type()
)
cpqSm2CommPagerStopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CommPagerStopBits.setStatus("mandatory")


class _CpqSm2CommPcmciaModel_Type(DisplayString):
    """Custom type cpqSm2CommPcmciaModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CpqSm2CommPcmciaModel_Type.__name__ = "DisplayString"
_CpqSm2CommPcmciaModel_Object = MibTableColumn
cpqSm2CommPcmciaModel = _CpqSm2CommPcmciaModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 4, 1, 1, 20),
    _CpqSm2CommPcmciaModel_Type()
)
cpqSm2CommPcmciaModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2CommPcmciaModel.setStatus("mandatory")
_CpqSm2Nic_ObjectIdentity = ObjectIdentity
cpqSm2Nic = _CpqSm2Nic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5)
)
_CpqSm2NicConfigTable_Object = MibTable
cpqSm2NicConfigTable = _CpqSm2NicConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 1)
)
if mibBuilder.loadTexts:
    cpqSm2NicConfigTable.setStatus("mandatory")
_CpqSm2NicConfigEntry_Object = MibTableRow
cpqSm2NicConfigEntry = _CpqSm2NicConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 1, 1)
)
cpqSm2NicConfigEntry.setIndexNames(
    (0, "CPQSM2-MIB", "cpqSm2NicLocation"),
)
if mibBuilder.loadTexts:
    cpqSm2NicConfigEntry.setStatus("mandatory")


class _CpqSm2NicLocation_Type(Integer32):
    """Custom type cpqSm2NicLocation based on Integer32"""
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
          ("embedded", 2),
          ("pcmcia", 3))
    )


_CpqSm2NicLocation_Type.__name__ = "Integer32"
_CpqSm2NicLocation_Object = MibTableColumn
cpqSm2NicLocation = _CpqSm2NicLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 1, 1, 1),
    _CpqSm2NicLocation_Type()
)
cpqSm2NicLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2NicLocation.setStatus("mandatory")


class _CpqSm2NicModel_Type(DisplayString):
    """Custom type cpqSm2NicModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CpqSm2NicModel_Type.__name__ = "DisplayString"
_CpqSm2NicModel_Object = MibTableColumn
cpqSm2NicModel = _CpqSm2NicModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 1, 1, 2),
    _CpqSm2NicModel_Type()
)
cpqSm2NicModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2NicModel.setStatus("mandatory")


class _CpqSm2NicType_Type(Integer32):
    """Custom type cpqSm2NicType based on Integer32"""
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
          ("ethernet", 2),
          ("tokenRing", 3))
    )


_CpqSm2NicType_Type.__name__ = "Integer32"
_CpqSm2NicType_Object = MibTableColumn
cpqSm2NicType = _CpqSm2NicType_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 1, 1, 3),
    _CpqSm2NicType_Type()
)
cpqSm2NicType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2NicType.setStatus("mandatory")


class _CpqSm2NicMacAddress_Type(OctetString):
    """Custom type cpqSm2NicMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_CpqSm2NicMacAddress_Type.__name__ = "OctetString"
_CpqSm2NicMacAddress_Object = MibTableColumn
cpqSm2NicMacAddress = _CpqSm2NicMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 1, 1, 4),
    _CpqSm2NicMacAddress_Type()
)
cpqSm2NicMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2NicMacAddress.setStatus("mandatory")
_CpqSm2NicIpAddress_Type = IpAddress
_CpqSm2NicIpAddress_Object = MibTableColumn
cpqSm2NicIpAddress = _CpqSm2NicIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 1, 1, 5),
    _CpqSm2NicIpAddress_Type()
)
cpqSm2NicIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2NicIpAddress.setStatus("mandatory")
_CpqSm2NicIpSubnetMask_Type = IpAddress
_CpqSm2NicIpSubnetMask_Object = MibTableColumn
cpqSm2NicIpSubnetMask = _CpqSm2NicIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 1, 1, 6),
    _CpqSm2NicIpSubnetMask_Type()
)
cpqSm2NicIpSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2NicIpSubnetMask.setStatus("mandatory")


class _CpqSm2NicEnabledStatus_Type(Integer32):
    """Custom type cpqSm2NicEnabledStatus based on Integer32"""
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
          ("enabled", 2),
          ("disabled", 3))
    )


_CpqSm2NicEnabledStatus_Type.__name__ = "Integer32"
_CpqSm2NicEnabledStatus_Object = MibTableColumn
cpqSm2NicEnabledStatus = _CpqSm2NicEnabledStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 1, 1, 7),
    _CpqSm2NicEnabledStatus_Type()
)
cpqSm2NicEnabledStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2NicEnabledStatus.setStatus("mandatory")


class _CpqSm2NicDuplexState_Type(Integer32):
    """Custom type cpqSm2NicDuplexState based on Integer32"""
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
          ("halfDuplex", 2),
          ("fullDuplex", 3),
          ("notSupported", 4))
    )


_CpqSm2NicDuplexState_Type.__name__ = "Integer32"
_CpqSm2NicDuplexState_Object = MibTableColumn
cpqSm2NicDuplexState = _CpqSm2NicDuplexState_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 1, 1, 8),
    _CpqSm2NicDuplexState_Type()
)
cpqSm2NicDuplexState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2NicDuplexState.setStatus("mandatory")
_CpqSm2NicSpeed_Type = Integer32
_CpqSm2NicSpeed_Object = MibTableColumn
cpqSm2NicSpeed = _CpqSm2NicSpeed_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 1, 1, 9),
    _CpqSm2NicSpeed_Type()
)
cpqSm2NicSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2NicSpeed.setStatus("mandatory")


class _CpqSm2NicDhcpUse_Type(Integer32):
    """Custom type cpqSm2NicDhcpUse based on Integer32"""
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
          ("enabled", 2),
          ("disabled", 3))
    )


_CpqSm2NicDhcpUse_Type.__name__ = "Integer32"
_CpqSm2NicDhcpUse_Object = MibTableColumn
cpqSm2NicDhcpUse = _CpqSm2NicDhcpUse_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 1, 1, 10),
    _CpqSm2NicDhcpUse_Type()
)
cpqSm2NicDhcpUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2NicDhcpUse.setStatus("mandatory")


class _CpqSm2NicCondition_Type(Integer32):
    """Custom type cpqSm2NicCondition based on Integer32"""
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
          ("ok", 2),
          ("degraded", 3),
          ("failed", 4))
    )


_CpqSm2NicCondition_Type.__name__ = "Integer32"
_CpqSm2NicCondition_Object = MibTableColumn
cpqSm2NicCondition = _CpqSm2NicCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 1, 1, 11),
    _CpqSm2NicCondition_Type()
)
cpqSm2NicCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2NicCondition.setStatus("mandatory")
_CpqSm2NicMtu_Type = Integer32
_CpqSm2NicMtu_Object = MibTableColumn
cpqSm2NicMtu = _CpqSm2NicMtu_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 1, 1, 12),
    _CpqSm2NicMtu_Type()
)
cpqSm2NicMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2NicMtu.setStatus("mandatory")
_CpqSm2NicGatewayIpAddress_Type = IpAddress
_CpqSm2NicGatewayIpAddress_Object = MibTableColumn
cpqSm2NicGatewayIpAddress = _CpqSm2NicGatewayIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 1, 1, 13),
    _CpqSm2NicGatewayIpAddress_Type()
)
cpqSm2NicGatewayIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2NicGatewayIpAddress.setStatus("mandatory")


class _CpqSm2NicRibFullQualDnsName_Type(DisplayString):
    """Custom type cpqSm2NicRibFullQualDnsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 180),
    )


_CpqSm2NicRibFullQualDnsName_Type.__name__ = "DisplayString"
_CpqSm2NicRibFullQualDnsName_Object = MibTableColumn
cpqSm2NicRibFullQualDnsName = _CpqSm2NicRibFullQualDnsName_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 1, 1, 14),
    _CpqSm2NicRibFullQualDnsName_Type()
)
cpqSm2NicRibFullQualDnsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2NicRibFullQualDnsName.setStatus("mandatory")
_CpqSm2NicStatsTable_Object = MibTable
cpqSm2NicStatsTable = _CpqSm2NicStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 2)
)
if mibBuilder.loadTexts:
    cpqSm2NicStatsTable.setStatus("mandatory")
_CpqSm2NicStatsEntry_Object = MibTableRow
cpqSm2NicStatsEntry = _CpqSm2NicStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 2, 1)
)
cpqSm2NicStatsEntry.setIndexNames(
    (0, "CPQSM2-MIB", "cpqSm2NicStatsLocation"),
)
if mibBuilder.loadTexts:
    cpqSm2NicStatsEntry.setStatus("mandatory")


class _CpqSm2NicStatsLocation_Type(Integer32):
    """Custom type cpqSm2NicStatsLocation based on Integer32"""
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
          ("embedded", 2),
          ("pcmcia", 3))
    )


_CpqSm2NicStatsLocation_Type.__name__ = "Integer32"
_CpqSm2NicStatsLocation_Object = MibTableColumn
cpqSm2NicStatsLocation = _CpqSm2NicStatsLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 2, 1, 1),
    _CpqSm2NicStatsLocation_Type()
)
cpqSm2NicStatsLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2NicStatsLocation.setStatus("mandatory")
_CpqSm2NicXmitBytes_Type = Counter32
_CpqSm2NicXmitBytes_Object = MibTableColumn
cpqSm2NicXmitBytes = _CpqSm2NicXmitBytes_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 2, 1, 2),
    _CpqSm2NicXmitBytes_Type()
)
cpqSm2NicXmitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2NicXmitBytes.setStatus("mandatory")
_CpqSm2NicXmitTotalPackets_Type = Counter32
_CpqSm2NicXmitTotalPackets_Object = MibTableColumn
cpqSm2NicXmitTotalPackets = _CpqSm2NicXmitTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 2, 1, 3),
    _CpqSm2NicXmitTotalPackets_Type()
)
cpqSm2NicXmitTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2NicXmitTotalPackets.setStatus("mandatory")
_CpqSm2NicXmitUnicastPackets_Type = Counter32
_CpqSm2NicXmitUnicastPackets_Object = MibTableColumn
cpqSm2NicXmitUnicastPackets = _CpqSm2NicXmitUnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 2, 1, 4),
    _CpqSm2NicXmitUnicastPackets_Type()
)
cpqSm2NicXmitUnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2NicXmitUnicastPackets.setStatus("mandatory")
_CpqSm2NicXmitNonUniPackets_Type = Counter32
_CpqSm2NicXmitNonUniPackets_Object = MibTableColumn
cpqSm2NicXmitNonUniPackets = _CpqSm2NicXmitNonUniPackets_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 2, 1, 5),
    _CpqSm2NicXmitNonUniPackets_Type()
)
cpqSm2NicXmitNonUniPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2NicXmitNonUniPackets.setStatus("mandatory")
_CpqSm2NicXmitDiscardPackets_Type = Counter32
_CpqSm2NicXmitDiscardPackets_Object = MibTableColumn
cpqSm2NicXmitDiscardPackets = _CpqSm2NicXmitDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 2, 1, 6),
    _CpqSm2NicXmitDiscardPackets_Type()
)
cpqSm2NicXmitDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2NicXmitDiscardPackets.setStatus("mandatory")
_CpqSm2NicXmitErrorPackets_Type = Counter32
_CpqSm2NicXmitErrorPackets_Object = MibTableColumn
cpqSm2NicXmitErrorPackets = _CpqSm2NicXmitErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 2, 1, 7),
    _CpqSm2NicXmitErrorPackets_Type()
)
cpqSm2NicXmitErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2NicXmitErrorPackets.setStatus("mandatory")
_CpqSm2NicXmitQueueLength_Type = Counter32
_CpqSm2NicXmitQueueLength_Object = MibTableColumn
cpqSm2NicXmitQueueLength = _CpqSm2NicXmitQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 2, 1, 8),
    _CpqSm2NicXmitQueueLength_Type()
)
cpqSm2NicXmitQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2NicXmitQueueLength.setStatus("mandatory")
_CpqSm2NicRecvBytes_Type = Counter32
_CpqSm2NicRecvBytes_Object = MibTableColumn
cpqSm2NicRecvBytes = _CpqSm2NicRecvBytes_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 2, 1, 9),
    _CpqSm2NicRecvBytes_Type()
)
cpqSm2NicRecvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2NicRecvBytes.setStatus("mandatory")
_CpqSm2NicRecvTotalPackets_Type = Counter32
_CpqSm2NicRecvTotalPackets_Object = MibTableColumn
cpqSm2NicRecvTotalPackets = _CpqSm2NicRecvTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 2, 1, 10),
    _CpqSm2NicRecvTotalPackets_Type()
)
cpqSm2NicRecvTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2NicRecvTotalPackets.setStatus("mandatory")
_CpqSm2NicRecvUnicastPackets_Type = Counter32
_CpqSm2NicRecvUnicastPackets_Object = MibTableColumn
cpqSm2NicRecvUnicastPackets = _CpqSm2NicRecvUnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 2, 1, 11),
    _CpqSm2NicRecvUnicastPackets_Type()
)
cpqSm2NicRecvUnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2NicRecvUnicastPackets.setStatus("mandatory")
_CpqSm2NicRecvNonUniPackets_Type = Counter32
_CpqSm2NicRecvNonUniPackets_Object = MibTableColumn
cpqSm2NicRecvNonUniPackets = _CpqSm2NicRecvNonUniPackets_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 2, 1, 12),
    _CpqSm2NicRecvNonUniPackets_Type()
)
cpqSm2NicRecvNonUniPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2NicRecvNonUniPackets.setStatus("mandatory")
_CpqSm2NicRecvDiscardPackets_Type = Counter32
_CpqSm2NicRecvDiscardPackets_Object = MibTableColumn
cpqSm2NicRecvDiscardPackets = _CpqSm2NicRecvDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 2, 1, 13),
    _CpqSm2NicRecvDiscardPackets_Type()
)
cpqSm2NicRecvDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2NicRecvDiscardPackets.setStatus("mandatory")
_CpqSm2NicRecvErrorPackets_Type = Counter32
_CpqSm2NicRecvErrorPackets_Object = MibTableColumn
cpqSm2NicRecvErrorPackets = _CpqSm2NicRecvErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 2, 1, 14),
    _CpqSm2NicRecvErrorPackets_Type()
)
cpqSm2NicRecvErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2NicRecvErrorPackets.setStatus("mandatory")
_CpqSm2NicRecvUnknownPackets_Type = Counter32
_CpqSm2NicRecvUnknownPackets_Object = MibTableColumn
cpqSm2NicRecvUnknownPackets = _CpqSm2NicRecvUnknownPackets_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 2, 1, 15),
    _CpqSm2NicRecvUnknownPackets_Type()
)
cpqSm2NicRecvUnknownPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2NicRecvUnknownPackets.setStatus("mandatory")
_CpqSm2NicIpv6_ObjectIdentity = ObjectIdentity
cpqSm2NicIpv6 = _CpqSm2NicIpv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 3)
)
_CpqSm2NicIpv6Gateway_Type = DisplayString
_CpqSm2NicIpv6Gateway_Object = MibScalar
cpqSm2NicIpv6Gateway = _CpqSm2NicIpv6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 3, 1),
    _CpqSm2NicIpv6Gateway_Type()
)
cpqSm2NicIpv6Gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2NicIpv6Gateway.setStatus("mandatory")
_CpqSm2NicIpv6AddressTable_Object = MibTable
cpqSm2NicIpv6AddressTable = _CpqSm2NicIpv6AddressTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 3, 2)
)
if mibBuilder.loadTexts:
    cpqSm2NicIpv6AddressTable.setStatus("mandatory")
_CpqSm2NicIpv6AddressEntry_Object = MibTableRow
cpqSm2NicIpv6AddressEntry = _CpqSm2NicIpv6AddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 3, 2, 1)
)
cpqSm2NicIpv6AddressEntry.setIndexNames(
    (0, "CPQSM2-MIB", "cpqSm2NicIpv6Index"),
)
if mibBuilder.loadTexts:
    cpqSm2NicIpv6AddressEntry.setStatus("mandatory")
_CpqSm2NicIpv6Index_Type = Integer32
_CpqSm2NicIpv6Index_Object = MibTableColumn
cpqSm2NicIpv6Index = _CpqSm2NicIpv6Index_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 3, 2, 1, 1),
    _CpqSm2NicIpv6Index_Type()
)
cpqSm2NicIpv6Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2NicIpv6Index.setStatus("mandatory")
_CpqSm2NicIpv6Address_Type = DisplayString
_CpqSm2NicIpv6Address_Object = MibTableColumn
cpqSm2NicIpv6Address = _CpqSm2NicIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 3, 2, 1, 2),
    _CpqSm2NicIpv6Address_Type()
)
cpqSm2NicIpv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2NicIpv6Address.setStatus("mandatory")
_CpqSm2NicIpv6Status_Type = DisplayString
_CpqSm2NicIpv6Status_Object = MibTableColumn
cpqSm2NicIpv6Status = _CpqSm2NicIpv6Status_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 3, 2, 1, 3),
    _CpqSm2NicIpv6Status_Type()
)
cpqSm2NicIpv6Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2NicIpv6Status.setStatus("mandatory")
_CpqSm2NicIpv6PrefixLen_Type = Integer32
_CpqSm2NicIpv6PrefixLen_Object = MibTableColumn
cpqSm2NicIpv6PrefixLen = _CpqSm2NicIpv6PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 3, 2, 1, 4),
    _CpqSm2NicIpv6PrefixLen_Type()
)
cpqSm2NicIpv6PrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2NicIpv6PrefixLen.setStatus("mandatory")
_CpqSm2NicIpv6DhcpTable_Object = MibTable
cpqSm2NicIpv6DhcpTable = _CpqSm2NicIpv6DhcpTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 3, 3)
)
if mibBuilder.loadTexts:
    cpqSm2NicIpv6DhcpTable.setStatus("mandatory")
_CpqSm2NicIpv6DhcpEntry_Object = MibTableRow
cpqSm2NicIpv6DhcpEntry = _CpqSm2NicIpv6DhcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 3, 3, 1)
)
cpqSm2NicIpv6DhcpEntry.setIndexNames(
    (0, "CPQSM2-MIB", "cpqSm2NicIpv6Index"),
)
if mibBuilder.loadTexts:
    cpqSm2NicIpv6DhcpEntry.setStatus("mandatory")
_CpqSm2NicIpv6DhcpIndex_Type = Integer32
_CpqSm2NicIpv6DhcpIndex_Object = MibTableColumn
cpqSm2NicIpv6DhcpIndex = _CpqSm2NicIpv6DhcpIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 3, 3, 1, 1),
    _CpqSm2NicIpv6DhcpIndex_Type()
)
cpqSm2NicIpv6DhcpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2NicIpv6DhcpIndex.setStatus("mandatory")
_CpqSm2NicIpv6Dhcp_Type = DisplayString
_CpqSm2NicIpv6Dhcp_Object = MibTableColumn
cpqSm2NicIpv6Dhcp = _CpqSm2NicIpv6Dhcp_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 3, 3, 1, 2),
    _CpqSm2NicIpv6Dhcp_Type()
)
cpqSm2NicIpv6Dhcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2NicIpv6Dhcp.setStatus("mandatory")
_CpqSm2NicIpv6DhcpStatus_Type = DisplayString
_CpqSm2NicIpv6DhcpStatus_Object = MibTableColumn
cpqSm2NicIpv6DhcpStatus = _CpqSm2NicIpv6DhcpStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 3, 3, 1, 3),
    _CpqSm2NicIpv6DhcpStatus_Type()
)
cpqSm2NicIpv6DhcpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2NicIpv6DhcpStatus.setStatus("mandatory")
_CpqSm2NicIpv6DhcpPrefixLen_Type = Integer32
_CpqSm2NicIpv6DhcpPrefixLen_Object = MibTableColumn
cpqSm2NicIpv6DhcpPrefixLen = _CpqSm2NicIpv6DhcpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 3, 3, 1, 4),
    _CpqSm2NicIpv6DhcpPrefixLen_Type()
)
cpqSm2NicIpv6DhcpPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2NicIpv6DhcpPrefixLen.setStatus("mandatory")
_CpqSm2NicIpv6SlaacTable_Object = MibTable
cpqSm2NicIpv6SlaacTable = _CpqSm2NicIpv6SlaacTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 3, 4)
)
if mibBuilder.loadTexts:
    cpqSm2NicIpv6SlaacTable.setStatus("mandatory")
_CpqSm2NicIpv6SlaacEntry_Object = MibTableRow
cpqSm2NicIpv6SlaacEntry = _CpqSm2NicIpv6SlaacEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 3, 4, 1)
)
cpqSm2NicIpv6SlaacEntry.setIndexNames(
    (0, "CPQSM2-MIB", "cpqSm2NicIpv6SlaacIndex"),
)
if mibBuilder.loadTexts:
    cpqSm2NicIpv6SlaacEntry.setStatus("mandatory")
_CpqSm2NicIpv6SlaacIndex_Type = Integer32
_CpqSm2NicIpv6SlaacIndex_Object = MibTableColumn
cpqSm2NicIpv6SlaacIndex = _CpqSm2NicIpv6SlaacIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 3, 4, 1, 1),
    _CpqSm2NicIpv6SlaacIndex_Type()
)
cpqSm2NicIpv6SlaacIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2NicIpv6SlaacIndex.setStatus("mandatory")
_CpqSm2NicIpv6Slaac_Type = DisplayString
_CpqSm2NicIpv6Slaac_Object = MibTableColumn
cpqSm2NicIpv6Slaac = _CpqSm2NicIpv6Slaac_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 3, 4, 1, 2),
    _CpqSm2NicIpv6Slaac_Type()
)
cpqSm2NicIpv6Slaac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2NicIpv6Slaac.setStatus("mandatory")
_Cpqsm2NicIpv6SlaacStatus_Type = DisplayString
_Cpqsm2NicIpv6SlaacStatus_Object = MibTableColumn
cpqsm2NicIpv6SlaacStatus = _Cpqsm2NicIpv6SlaacStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 3, 4, 1, 3),
    _Cpqsm2NicIpv6SlaacStatus_Type()
)
cpqsm2NicIpv6SlaacStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqsm2NicIpv6SlaacStatus.setStatus("mandatory")
_CpqSm2NicIpv6SlaacPrefixLen_Type = Integer32
_CpqSm2NicIpv6SlaacPrefixLen_Object = MibTableColumn
cpqSm2NicIpv6SlaacPrefixLen = _CpqSm2NicIpv6SlaacPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 3, 4, 1, 4),
    _CpqSm2NicIpv6SlaacPrefixLen_Type()
)
cpqSm2NicIpv6SlaacPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2NicIpv6SlaacPrefixLen.setStatus("mandatory")
_CpqSm2NicIpv6RouteTable_Object = MibTable
cpqSm2NicIpv6RouteTable = _CpqSm2NicIpv6RouteTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 3, 5)
)
if mibBuilder.loadTexts:
    cpqSm2NicIpv6RouteTable.setStatus("mandatory")
_CpqSm2NicIpv6RouteEntry_Object = MibTableRow
cpqSm2NicIpv6RouteEntry = _CpqSm2NicIpv6RouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 3, 5, 1)
)
cpqSm2NicIpv6RouteEntry.setIndexNames(
    (0, "CPQSM2-MIB", "cpqSm2NicIpv6RouteIndex"),
)
if mibBuilder.loadTexts:
    cpqSm2NicIpv6RouteEntry.setStatus("mandatory")
_CpqSm2NicIpv6RouteIndex_Type = Integer32
_CpqSm2NicIpv6RouteIndex_Object = MibTableColumn
cpqSm2NicIpv6RouteIndex = _CpqSm2NicIpv6RouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 3, 5, 1, 1),
    _CpqSm2NicIpv6RouteIndex_Type()
)
cpqSm2NicIpv6RouteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2NicIpv6RouteIndex.setStatus("mandatory")
_CpqSm2NicIpv6RouteDest_Type = DisplayString
_CpqSm2NicIpv6RouteDest_Object = MibTableColumn
cpqSm2NicIpv6RouteDest = _CpqSm2NicIpv6RouteDest_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 3, 5, 1, 2),
    _CpqSm2NicIpv6RouteDest_Type()
)
cpqSm2NicIpv6RouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2NicIpv6RouteDest.setStatus("mandatory")
_Cpqsm2NicIpv6RouteDestStatus_Type = DisplayString
_Cpqsm2NicIpv6RouteDestStatus_Object = MibTableColumn
cpqsm2NicIpv6RouteDestStatus = _Cpqsm2NicIpv6RouteDestStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 3, 5, 1, 3),
    _Cpqsm2NicIpv6RouteDestStatus_Type()
)
cpqsm2NicIpv6RouteDestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqsm2NicIpv6RouteDestStatus.setStatus("mandatory")
_CpqSm2NicIpv6RouteDestPrefixLen_Type = Integer32
_CpqSm2NicIpv6RouteDestPrefixLen_Object = MibTableColumn
cpqSm2NicIpv6RouteDestPrefixLen = _CpqSm2NicIpv6RouteDestPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 3, 5, 1, 4),
    _CpqSm2NicIpv6RouteDestPrefixLen_Type()
)
cpqSm2NicIpv6RouteDestPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2NicIpv6RouteDestPrefixLen.setStatus("mandatory")
_CpqSM2NicIpv6RouteGate_Type = DisplayString
_CpqSM2NicIpv6RouteGate_Object = MibTableColumn
cpqSM2NicIpv6RouteGate = _CpqSM2NicIpv6RouteGate_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 3, 5, 1, 5),
    _CpqSM2NicIpv6RouteGate_Type()
)
cpqSM2NicIpv6RouteGate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSM2NicIpv6RouteGate.setStatus("mandatory")
_Cpqsm2NicIpv6RouteGateStatus_Type = DisplayString
_Cpqsm2NicIpv6RouteGateStatus_Object = MibTableColumn
cpqsm2NicIpv6RouteGateStatus = _Cpqsm2NicIpv6RouteGateStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 5, 3, 5, 1, 6),
    _Cpqsm2NicIpv6RouteGateStatus_Type()
)
cpqsm2NicIpv6RouteGateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqsm2NicIpv6RouteGateStatus.setStatus("mandatory")
_CpqSm2Ers_ObjectIdentity = ObjectIdentity
cpqSm2Ers = _CpqSm2Ers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 6)
)


class _CpqSm2ErsTransactionType_Type(Integer32):
    """Custom type cpqSm2ErsTransactionType based on Integer32"""
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
        *(("registration", 1),
          ("serviceEvent", 2),
          ("l2DataCollection", 3),
          ("unregistration", 4),
          ("ahsDataCollection", 5))
    )


_CpqSm2ErsTransactionType_Type.__name__ = "Integer32"
_CpqSm2ErsTransactionType_Object = MibScalar
cpqSm2ErsTransactionType = _CpqSm2ErsTransactionType_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 6, 1),
    _CpqSm2ErsTransactionType_Type()
)
cpqSm2ErsTransactionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2ErsTransactionType.setStatus("mandatory")


class _CpqSm2ErsConnectionModel_Type(Integer32):
    """Custom type cpqSm2ErsConnectionModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("insightOnline", 1),
          ("insightRemoteSupport", 2))
    )


_CpqSm2ErsConnectionModel_Type.__name__ = "Integer32"
_CpqSm2ErsConnectionModel_Object = MibScalar
cpqSm2ErsConnectionModel = _CpqSm2ErsConnectionModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 6, 2),
    _CpqSm2ErsConnectionModel_Type()
)
cpqSm2ErsConnectionModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2ErsConnectionModel.setStatus("mandatory")


class _CpqSm2ErsFailureCode_Type(Integer32):
    """Custom type cpqSm2ErsFailureCode based on Integer32"""
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
        *(("genericTransmitError", 1),
          ("clientTransmitTimeout", 2),
          ("clientReceiveTimeout", 3),
          ("proxyConnectError", 4),
          ("remoteHostConnectError", 5),
          ("remoteServiceError", 6))
    )


_CpqSm2ErsFailureCode_Type.__name__ = "Integer32"
_CpqSm2ErsFailureCode_Object = MibScalar
cpqSm2ErsFailureCode = _CpqSm2ErsFailureCode_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 6, 3),
    _CpqSm2ErsFailureCode_Type()
)
cpqSm2ErsFailureCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2ErsFailureCode.setStatus("mandatory")


class _CpqSm2ErsRemoteHost_Type(DisplayString):
    """Custom type cpqSm2ErsRemoteHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 135),
    )


_CpqSm2ErsRemoteHost_Type.__name__ = "DisplayString"
_CpqSm2ErsRemoteHost_Object = MibScalar
cpqSm2ErsRemoteHost = _CpqSm2ErsRemoteHost_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 6, 4),
    _CpqSm2ErsRemoteHost_Type()
)
cpqSm2ErsRemoteHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2ErsRemoteHost.setStatus("mandatory")
_CpqSm2FW_ObjectIdentity = ObjectIdentity
cpqSm2FW = _CpqSm2FW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 7)
)


class _CpqSm2FirmwareType_Type(Integer32):
    """Custom type cpqSm2FirmwareType based on Integer32"""
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
          ("ilo", 2),
          ("bios", 3),
          ("cpld", 4),
          ("ie", 5),
          ("sps", 6))
    )


_CpqSm2FirmwareType_Type.__name__ = "Integer32"
_CpqSm2FirmwareType_Object = MibScalar
cpqSm2FirmwareType = _CpqSm2FirmwareType_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 7, 1),
    _CpqSm2FirmwareType_Type()
)
cpqSm2FirmwareType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2FirmwareType.setStatus("mandatory")


class _CpqSm2FwFailureCode_Type(DisplayString):
    """Custom type cpqSm2FwFailureCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 135),
    )


_CpqSm2FwFailureCode_Type.__name__ = "DisplayString"
_CpqSm2FwFailureCode_Object = MibScalar
cpqSm2FwFailureCode = _CpqSm2FwFailureCode_Object(
    (1, 3, 6, 1, 4, 1, 232, 9, 2, 7, 2),
    _CpqSm2FwFailureCode_Type()
)
cpqSm2FwFailureCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSm2FwFailureCode.setStatus("mandatory")
_CpqSm2Trap_ObjectIdentity = ObjectIdentity
cpqSm2Trap = _CpqSm2Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 9, 3)
)
_CpqSm2Products_ObjectIdentity = ObjectIdentity
cpqSm2Products = _CpqSm2Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 9, 4)
)
_CpaSm2ProdEisaRemote_ObjectIdentity = ObjectIdentity
cpaSm2ProdEisaRemote = _CpaSm2ProdEisaRemote_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 9, 4, 2)
)
_CpqSm2ProdPCIRemote_ObjectIdentity = ObjectIdentity
cpqSm2ProdPCIRemote = _CpqSm2ProdPCIRemote_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 9, 4, 3)
)
_CpqSm2ProdRILOE_ObjectIdentity = ObjectIdentity
cpqSm2ProdRILOE = _CpqSm2ProdRILOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 9, 4, 4)
)
_CpqSm2ProdiLo_ObjectIdentity = ObjectIdentity
cpqSm2ProdiLo = _CpqSm2ProdiLo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 9, 4, 5)
)
_CpqSm2ProdRILOEII_ObjectIdentity = ObjectIdentity
cpqSm2ProdRILOEII = _CpqSm2ProdRILOEII_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 9, 4, 6)
)
_CpqSm2ProdRILO2_ObjectIdentity = ObjectIdentity
cpqSm2ProdRILO2 = _CpqSm2ProdRILO2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 9, 4, 7)
)
_CpqSm2ProdRLO100_ObjectIdentity = ObjectIdentity
cpqSm2ProdRLO100 = _CpqSm2ProdRLO100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 9, 4, 8)
)
_CpqSm2ProdRILO3_ObjectIdentity = ObjectIdentity
cpqSm2ProdRILO3 = _CpqSm2ProdRILO3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 9, 4, 9)
)
_CpqSm2ProdRILO4_ObjectIdentity = ObjectIdentity
cpqSm2ProdRILO4 = _CpqSm2ProdRILO4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 9, 4, 10)
)
_CpqSm2ProdRILO5_ObjectIdentity = ObjectIdentity
cpqSm2ProdRILO5 = _CpqSm2ProdRILO5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 9, 4, 11)
)

# Managed Objects groups


# Notification objects

cpqSm2ServerReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 9001)
)
cpqSm2ServerReset.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"))
)
if mibBuilder.loadTexts:
    cpqSm2ServerReset.setStatus(
        ""
    )

cpqSm2ServerPowerOutage = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 9002)
)
cpqSm2ServerPowerOutage.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"))
)
if mibBuilder.loadTexts:
    cpqSm2ServerPowerOutage.setStatus(
        ""
    )

cpqSm2UnauthorizedLoginAttempts = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 9003)
)
cpqSm2UnauthorizedLoginAttempts.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSM2-MIB", "cpqSm2CntlrBadLoginAttemptsThresh"))
)
if mibBuilder.loadTexts:
    cpqSm2UnauthorizedLoginAttempts.setStatus(
        ""
    )

cpqSm2BatteryFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 9004)
)
cpqSm2BatteryFailed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"))
)
if mibBuilder.loadTexts:
    cpqSm2BatteryFailed.setStatus(
        ""
    )

cpqSm2SelfTestError = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 9005)
)
cpqSm2SelfTestError.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSM2-MIB", "cpqSm2CntlrSelfTestErrors"))
)
if mibBuilder.loadTexts:
    cpqSm2SelfTestError.setStatus(
        ""
    )

cpqSm2InterfaceError = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 9006)
)
cpqSm2InterfaceError.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"))
)
if mibBuilder.loadTexts:
    cpqSm2InterfaceError.setStatus(
        ""
    )

cpqSm2BatteryDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 9007)
)
cpqSm2BatteryDisconnected.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"))
)
if mibBuilder.loadTexts:
    cpqSm2BatteryDisconnected.setStatus(
        ""
    )

cpqSm2KeyboardCableDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 9008)
)
cpqSm2KeyboardCableDisconnected.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"))
)
if mibBuilder.loadTexts:
    cpqSm2KeyboardCableDisconnected.setStatus(
        ""
    )

cpqSm2MouseCableDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 9009)
)
cpqSm2MouseCableDisconnected.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"))
)
if mibBuilder.loadTexts:
    cpqSm2MouseCableDisconnected.setStatus(
        ""
    )

cpqSm2ExternalPowerCableDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 9010)
)
cpqSm2ExternalPowerCableDisconnected.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"))
)
if mibBuilder.loadTexts:
    cpqSm2ExternalPowerCableDisconnected.setStatus(
        ""
    )

cpqSm2LogsFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 9011)
)
cpqSm2LogsFull.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"))
)
if mibBuilder.loadTexts:
    cpqSm2LogsFull.setStatus(
        ""
    )

cpqSm2SecurityOverrideEngaged = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 9012)
)
cpqSm2SecurityOverrideEngaged.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"))
)
if mibBuilder.loadTexts:
    cpqSm2SecurityOverrideEngaged.setStatus(
        ""
    )

cpqSm2SecurityOverrideDisengaged = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 9013)
)
cpqSm2SecurityOverrideDisengaged.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"))
)
if mibBuilder.loadTexts:
    cpqSm2SecurityOverrideDisengaged.setStatus(
        ""
    )

cpqSm2ServerFatalError = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 9014)
)
cpqSm2ServerFatalError.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    cpqSm2ServerFatalError.setStatus(
        ""
    )

cpqSm2NicLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 9015)
)
cpqSm2NicLinkDown.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    cpqSm2NicLinkDown.setStatus(
        ""
    )

cpqSm2NicLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 9016)
)
cpqSm2NicLinkUp.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    cpqSm2NicLinkUp.setStatus(
        ""
    )

cpqSm2ServerPowerOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 9017)
)
cpqSm2ServerPowerOn.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHOST-MIB", "cpqHoGUIDCanonical"))
)
if mibBuilder.loadTexts:
    cpqSm2ServerPowerOn.setStatus(
        ""
    )

cpqSm2ServerPowerOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 9018)
)
cpqSm2ServerPowerOff.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHOST-MIB", "cpqHoGUIDCanonical"))
)
if mibBuilder.loadTexts:
    cpqSm2ServerPowerOff.setStatus(
        ""
    )

cpqSm2ServerPowerOnFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 9019)
)
cpqSm2ServerPowerOnFailure.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHOST-MIB", "cpqHoGUIDCanonical"))
)
if mibBuilder.loadTexts:
    cpqSm2ServerPowerOnFailure.setStatus(
        ""
    )

cpqSm2IrsCommFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 9020)
)
cpqSm2IrsCommFailure.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHOST-MIB", "cpqHoGUIDCanonical"),
        ("CPQSINFO-MIB", "cpqSiProductName"),
        ("CPQSINFO-MIB", "cpqSiSysProductId"),
        ("CPQSINFO-MIB", "cpqSiSysSerialNum"),
        ("CPQSINFO-MIB", "cpqSiAssetTag"),
        ("CPQSM2-MIB", "cpqSm2ErsTransactionType"),
        ("CPQSM2-MIB", "cpqSm2ErsConnectionModel"),
        ("CPQSM2-MIB", "cpqSm2ErsFailureCode"),
        ("CPQSM2-MIB", "cpqSm2ErsRemoteHost"))
)
if mibBuilder.loadTexts:
    cpqSm2IrsCommFailure.setStatus(
        ""
    )

cpqSm2FirmwareValidationScanFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 9021)
)
cpqSm2FirmwareValidationScanFailed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSM2-MIB", "cpqSm2FirmwareType"))
)
if mibBuilder.loadTexts:
    cpqSm2FirmwareValidationScanFailed.setStatus(
        ""
    )

cpqSm2FirmwareValidationScanErrorRepaired = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 9022)
)
cpqSm2FirmwareValidationScanErrorRepaired.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSM2-MIB", "cpqSm2FirmwareType"))
)
if mibBuilder.loadTexts:
    cpqSm2FirmwareValidationScanErrorRepaired.setStatus(
        ""
    )

cpqSm2FirmwareValidationAutoRepairFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 9023)
)
cpqSm2FirmwareValidationAutoRepairFailed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSM2-MIB", "cpqSm2FirmwareType"))
)
if mibBuilder.loadTexts:
    cpqSm2FirmwareValidationAutoRepairFailed.setStatus(
        ""
    )

cpqSm2AutoShutdownInitiated = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 9024)
)
cpqSm2AutoShutdownInitiated.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSM2-MIB", "cpqSm2CntlrSysAutoShutdownCause"))
)
if mibBuilder.loadTexts:
    cpqSm2AutoShutdownInitiated.setStatus(
        ""
    )

cpqSm2AutoShutdownCancelled = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 9025)
)
cpqSm2AutoShutdownCancelled.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSM2-MIB", "cpqSm2CntlrSysAutoShutdownCause"))
)
if mibBuilder.loadTexts:
    cpqSm2AutoShutdownCancelled.setStatus(
        ""
    )

cpqSm2FwUpdateUploadFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 9026)
)
cpqSm2FwUpdateUploadFailed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSM2-MIB", "cpqSm2FwFailureCode"))
)
if mibBuilder.loadTexts:
    cpqSm2FwUpdateUploadFailed.setStatus(
        ""
    )

cpqSm2SecurityStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 9027)
)
cpqSm2SecurityStateChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSM2-MIB", "cpqSm2CntlrSecurityState"))
)
if mibBuilder.loadTexts:
    cpqSm2SecurityStateChange.setStatus(
        ""
    )

cpqSm2WDTimerReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 9028)
)
cpqSm2WDTimerReset.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSM2-MIB", "cpqSm2WDTimerType"),
        ("CPQSM2-MIB", "cpqSm2WDTimerTimeoutDetails"))
)
if mibBuilder.loadTexts:
    cpqSm2WDTimerReset.setStatus(
        ""
    )

cpqSm2OverallSecStateAtRisk = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 9029)
)
cpqSm2OverallSecStateAtRisk.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"))
)
if mibBuilder.loadTexts:
    cpqSm2OverallSecStateAtRisk.setStatus(
        ""
    )

cpqSm2OverallSecStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 9030)
)
cpqSm2OverallSecStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSM2-MIB", "cpqSm2CntlrOverallSecStatus"))
)
if mibBuilder.loadTexts:
    cpqSm2OverallSecStatusChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQSM2-MIB",
    **{"cpqSm2ServerReset": cpqSm2ServerReset,
       "cpqSm2ServerPowerOutage": cpqSm2ServerPowerOutage,
       "cpqSm2UnauthorizedLoginAttempts": cpqSm2UnauthorizedLoginAttempts,
       "cpqSm2BatteryFailed": cpqSm2BatteryFailed,
       "cpqSm2SelfTestError": cpqSm2SelfTestError,
       "cpqSm2InterfaceError": cpqSm2InterfaceError,
       "cpqSm2BatteryDisconnected": cpqSm2BatteryDisconnected,
       "cpqSm2KeyboardCableDisconnected": cpqSm2KeyboardCableDisconnected,
       "cpqSm2MouseCableDisconnected": cpqSm2MouseCableDisconnected,
       "cpqSm2ExternalPowerCableDisconnected": cpqSm2ExternalPowerCableDisconnected,
       "cpqSm2LogsFull": cpqSm2LogsFull,
       "cpqSm2SecurityOverrideEngaged": cpqSm2SecurityOverrideEngaged,
       "cpqSm2SecurityOverrideDisengaged": cpqSm2SecurityOverrideDisengaged,
       "cpqSm2ServerFatalError": cpqSm2ServerFatalError,
       "cpqSm2NicLinkDown": cpqSm2NicLinkDown,
       "cpqSm2NicLinkUp": cpqSm2NicLinkUp,
       "cpqSm2ServerPowerOn": cpqSm2ServerPowerOn,
       "cpqSm2ServerPowerOff": cpqSm2ServerPowerOff,
       "cpqSm2ServerPowerOnFailure": cpqSm2ServerPowerOnFailure,
       "cpqSm2IrsCommFailure": cpqSm2IrsCommFailure,
       "cpqSm2FirmwareValidationScanFailed": cpqSm2FirmwareValidationScanFailed,
       "cpqSm2FirmwareValidationScanErrorRepaired": cpqSm2FirmwareValidationScanErrorRepaired,
       "cpqSm2FirmwareValidationAutoRepairFailed": cpqSm2FirmwareValidationAutoRepairFailed,
       "cpqSm2AutoShutdownInitiated": cpqSm2AutoShutdownInitiated,
       "cpqSm2AutoShutdownCancelled": cpqSm2AutoShutdownCancelled,
       "cpqSm2FwUpdateUploadFailed": cpqSm2FwUpdateUploadFailed,
       "cpqSm2SecurityStateChange": cpqSm2SecurityStateChange,
       "cpqSm2WDTimerReset": cpqSm2WDTimerReset,
       "cpqSm2OverallSecStateAtRisk": cpqSm2OverallSecStateAtRisk,
       "cpqSm2OverallSecStatusChange": cpqSm2OverallSecStatusChange,
       "cpqSm2": cpqSm2,
       "cpqSm2MibRev": cpqSm2MibRev,
       "cpqSm2MibRevMajor": cpqSm2MibRevMajor,
       "cpqSm2MibRevMinor": cpqSm2MibRevMinor,
       "cpqSm2MibCondition": cpqSm2MibCondition,
       "cpqSm2Component": cpqSm2Component,
       "cpqSm2Interface": cpqSm2Interface,
       "cpqSm2OsCommon": cpqSm2OsCommon,
       "cpqSm2OsCommonPollFreq": cpqSm2OsCommonPollFreq,
       "cpqSm2OsCommonModuleTable": cpqSm2OsCommonModuleTable,
       "cpqSm2OsCommonModuleEntry": cpqSm2OsCommonModuleEntry,
       "cpqSm2OsCommonModuleIndex": cpqSm2OsCommonModuleIndex,
       "cpqSm2OsCommonModuleName": cpqSm2OsCommonModuleName,
       "cpqSm2OsCommonModuleVersion": cpqSm2OsCommonModuleVersion,
       "cpqSm2OsCommonModuleDate": cpqSm2OsCommonModuleDate,
       "cpqSm2OsCommonModulePurpose": cpqSm2OsCommonModulePurpose,
       "cpqSm2Cntlr": cpqSm2Cntlr,
       "cpqSm2CntlrRomDate": cpqSm2CntlrRomDate,
       "cpqSm2CntlrRomRevision": cpqSm2CntlrRomRevision,
       "cpqSm2CntlrVideoStatus": cpqSm2CntlrVideoStatus,
       "cpqSm2CntlrBatteryEnabled": cpqSm2CntlrBatteryEnabled,
       "cpqSm2CntlrBatteryStatus": cpqSm2CntlrBatteryStatus,
       "cpqSm2CntlrBatteryPercentCharged": cpqSm2CntlrBatteryPercentCharged,
       "cpqSm2CntlrAlertStatus": cpqSm2CntlrAlertStatus,
       "cpqSm2CntlrPendingAlerts": cpqSm2CntlrPendingAlerts,
       "cpqSm2CntlrSelfTestErrors": cpqSm2CntlrSelfTestErrors,
       "cpqSm2CntlrAgentLocation": cpqSm2CntlrAgentLocation,
       "cpqSm2CntlrLastDataUpdate": cpqSm2CntlrLastDataUpdate,
       "cpqSm2CntlrDataStatus": cpqSm2CntlrDataStatus,
       "cpqSm2CntlrColdReboot": cpqSm2CntlrColdReboot,
       "cpqSm2CntlrBadLoginAttemptsThresh": cpqSm2CntlrBadLoginAttemptsThresh,
       "cpqSm2CntlrBoardSerialNumber": cpqSm2CntlrBoardSerialNumber,
       "cpqSm2CntlrRemoteSessionStatus": cpqSm2CntlrRemoteSessionStatus,
       "cpqSm2CntlrInterfaceStatus": cpqSm2CntlrInterfaceStatus,
       "cpqSm2CntlrSystemId": cpqSm2CntlrSystemId,
       "cpqSm2CntlrKeyboardCableStatus": cpqSm2CntlrKeyboardCableStatus,
       "cpqSm2ServerIpAddress": cpqSm2ServerIpAddress,
       "cpqSm2CntlrModel": cpqSm2CntlrModel,
       "cpqSm2CntlrSelfTestErrorMask": cpqSm2CntlrSelfTestErrorMask,
       "cpqSm2CntlrMouseCableStatus": cpqSm2CntlrMouseCableStatus,
       "cpqSm2CntlrVirtualPowerCableStatus": cpqSm2CntlrVirtualPowerCableStatus,
       "cpqSm2CntlrExternalPowerCableStatus": cpqSm2CntlrExternalPowerCableStatus,
       "cpqSm2CntlrHostGUID": cpqSm2CntlrHostGUID,
       "cpqSm2CntlriLOSecurityOverrideSwitchState": cpqSm2CntlriLOSecurityOverrideSwitchState,
       "cpqSm2CntlrHardwareVer": cpqSm2CntlrHardwareVer,
       "cpqSm2CntlrAction": cpqSm2CntlrAction,
       "cpqSm2CntlrLicenseActive": cpqSm2CntlrLicenseActive,
       "cpqSm2CntlrLicenseKey": cpqSm2CntlrLicenseKey,
       "cpqSm2CntlrServerPowerState": cpqSm2CntlrServerPowerState,
       "cpqSm2CntlrSysAutoShutdownCause": cpqSm2CntlrSysAutoShutdownCause,
       "cpqSm2CntlrSecurityState": cpqSm2CntlrSecurityState,
       "cpqSm2WDTimerType": cpqSm2WDTimerType,
       "cpqSm2WDTimerTimeoutDetails": cpqSm2WDTimerTimeoutDetails,
       "cpqSm2CntlrOverallSecStatus": cpqSm2CntlrOverallSecStatus,
       "cpqSm2EventLog": cpqSm2EventLog,
       "cpqSm2EventTotalEntries": cpqSm2EventTotalEntries,
       "cpqSm2EventLogTable": cpqSm2EventLogTable,
       "cpqSm2EventLogEntry": cpqSm2EventLogEntry,
       "cpqSm2EventLogIndex": cpqSm2EventLogIndex,
       "cpqSm2EventLogNumber": cpqSm2EventLogNumber,
       "cpqSm2EventLogDate": cpqSm2EventLogDate,
       "cpqSm2EventLogMessage": cpqSm2EventLogMessage,
       "cpqSm2AsyncComm": cpqSm2AsyncComm,
       "cpqSm2CommSettingsTable": cpqSm2CommSettingsTable,
       "cpqSm2CommSettingsEntry": cpqSm2CommSettingsEntry,
       "cpqSm2CommPort": cpqSm2CommPort,
       "cpqSm2CommType": cpqSm2CommType,
       "cpqSm2CommBaudRate": cpqSm2CommBaudRate,
       "cpqSm2CommParity": cpqSm2CommParity,
       "cpqSm2CommDataBits": cpqSm2CommDataBits,
       "cpqSm2CommStopBits": cpqSm2CommStopBits,
       "cpqSm2CommModemReset": cpqSm2CommModemReset,
       "cpqSm2CommModemInit": cpqSm2CommModemInit,
       "cpqSm2CommModemDialPrefix": cpqSm2CommModemDialPrefix,
       "cpqSm2CommPortInit": cpqSm2CommPortInit,
       "cpqSm2CommDialin": cpqSm2CommDialin,
       "cpqSm2CommDialbackRequired": cpqSm2CommDialbackRequired,
       "cpqSm2CommNonPppConnections": cpqSm2CommNonPppConnections,
       "cpqSm2CommSnmpTrapDelivery": cpqSm2CommSnmpTrapDelivery,
       "cpqSm2CommPageDelivery": cpqSm2CommPageDelivery,
       "cpqSm2CommPagerBaudRate": cpqSm2CommPagerBaudRate,
       "cpqSm2CommPagerParity": cpqSm2CommPagerParity,
       "cpqSm2CommPagerDataBits": cpqSm2CommPagerDataBits,
       "cpqSm2CommPagerStopBits": cpqSm2CommPagerStopBits,
       "cpqSm2CommPcmciaModel": cpqSm2CommPcmciaModel,
       "cpqSm2Nic": cpqSm2Nic,
       "cpqSm2NicConfigTable": cpqSm2NicConfigTable,
       "cpqSm2NicConfigEntry": cpqSm2NicConfigEntry,
       "cpqSm2NicLocation": cpqSm2NicLocation,
       "cpqSm2NicModel": cpqSm2NicModel,
       "cpqSm2NicType": cpqSm2NicType,
       "cpqSm2NicMacAddress": cpqSm2NicMacAddress,
       "cpqSm2NicIpAddress": cpqSm2NicIpAddress,
       "cpqSm2NicIpSubnetMask": cpqSm2NicIpSubnetMask,
       "cpqSm2NicEnabledStatus": cpqSm2NicEnabledStatus,
       "cpqSm2NicDuplexState": cpqSm2NicDuplexState,
       "cpqSm2NicSpeed": cpqSm2NicSpeed,
       "cpqSm2NicDhcpUse": cpqSm2NicDhcpUse,
       "cpqSm2NicCondition": cpqSm2NicCondition,
       "cpqSm2NicMtu": cpqSm2NicMtu,
       "cpqSm2NicGatewayIpAddress": cpqSm2NicGatewayIpAddress,
       "cpqSm2NicRibFullQualDnsName": cpqSm2NicRibFullQualDnsName,
       "cpqSm2NicStatsTable": cpqSm2NicStatsTable,
       "cpqSm2NicStatsEntry": cpqSm2NicStatsEntry,
       "cpqSm2NicStatsLocation": cpqSm2NicStatsLocation,
       "cpqSm2NicXmitBytes": cpqSm2NicXmitBytes,
       "cpqSm2NicXmitTotalPackets": cpqSm2NicXmitTotalPackets,
       "cpqSm2NicXmitUnicastPackets": cpqSm2NicXmitUnicastPackets,
       "cpqSm2NicXmitNonUniPackets": cpqSm2NicXmitNonUniPackets,
       "cpqSm2NicXmitDiscardPackets": cpqSm2NicXmitDiscardPackets,
       "cpqSm2NicXmitErrorPackets": cpqSm2NicXmitErrorPackets,
       "cpqSm2NicXmitQueueLength": cpqSm2NicXmitQueueLength,
       "cpqSm2NicRecvBytes": cpqSm2NicRecvBytes,
       "cpqSm2NicRecvTotalPackets": cpqSm2NicRecvTotalPackets,
       "cpqSm2NicRecvUnicastPackets": cpqSm2NicRecvUnicastPackets,
       "cpqSm2NicRecvNonUniPackets": cpqSm2NicRecvNonUniPackets,
       "cpqSm2NicRecvDiscardPackets": cpqSm2NicRecvDiscardPackets,
       "cpqSm2NicRecvErrorPackets": cpqSm2NicRecvErrorPackets,
       "cpqSm2NicRecvUnknownPackets": cpqSm2NicRecvUnknownPackets,
       "cpqSm2NicIpv6": cpqSm2NicIpv6,
       "cpqSm2NicIpv6Gateway": cpqSm2NicIpv6Gateway,
       "cpqSm2NicIpv6AddressTable": cpqSm2NicIpv6AddressTable,
       "cpqSm2NicIpv6AddressEntry": cpqSm2NicIpv6AddressEntry,
       "cpqSm2NicIpv6Index": cpqSm2NicIpv6Index,
       "cpqSm2NicIpv6Address": cpqSm2NicIpv6Address,
       "cpqSm2NicIpv6Status": cpqSm2NicIpv6Status,
       "cpqSm2NicIpv6PrefixLen": cpqSm2NicIpv6PrefixLen,
       "cpqSm2NicIpv6DhcpTable": cpqSm2NicIpv6DhcpTable,
       "cpqSm2NicIpv6DhcpEntry": cpqSm2NicIpv6DhcpEntry,
       "cpqSm2NicIpv6DhcpIndex": cpqSm2NicIpv6DhcpIndex,
       "cpqSm2NicIpv6Dhcp": cpqSm2NicIpv6Dhcp,
       "cpqSm2NicIpv6DhcpStatus": cpqSm2NicIpv6DhcpStatus,
       "cpqSm2NicIpv6DhcpPrefixLen": cpqSm2NicIpv6DhcpPrefixLen,
       "cpqSm2NicIpv6SlaacTable": cpqSm2NicIpv6SlaacTable,
       "cpqSm2NicIpv6SlaacEntry": cpqSm2NicIpv6SlaacEntry,
       "cpqSm2NicIpv6SlaacIndex": cpqSm2NicIpv6SlaacIndex,
       "cpqSm2NicIpv6Slaac": cpqSm2NicIpv6Slaac,
       "cpqsm2NicIpv6SlaacStatus": cpqsm2NicIpv6SlaacStatus,
       "cpqSm2NicIpv6SlaacPrefixLen": cpqSm2NicIpv6SlaacPrefixLen,
       "cpqSm2NicIpv6RouteTable": cpqSm2NicIpv6RouteTable,
       "cpqSm2NicIpv6RouteEntry": cpqSm2NicIpv6RouteEntry,
       "cpqSm2NicIpv6RouteIndex": cpqSm2NicIpv6RouteIndex,
       "cpqSm2NicIpv6RouteDest": cpqSm2NicIpv6RouteDest,
       "cpqsm2NicIpv6RouteDestStatus": cpqsm2NicIpv6RouteDestStatus,
       "cpqSm2NicIpv6RouteDestPrefixLen": cpqSm2NicIpv6RouteDestPrefixLen,
       "cpqSM2NicIpv6RouteGate": cpqSM2NicIpv6RouteGate,
       "cpqsm2NicIpv6RouteGateStatus": cpqsm2NicIpv6RouteGateStatus,
       "cpqSm2Ers": cpqSm2Ers,
       "cpqSm2ErsTransactionType": cpqSm2ErsTransactionType,
       "cpqSm2ErsConnectionModel": cpqSm2ErsConnectionModel,
       "cpqSm2ErsFailureCode": cpqSm2ErsFailureCode,
       "cpqSm2ErsRemoteHost": cpqSm2ErsRemoteHost,
       "cpqSm2FW": cpqSm2FW,
       "cpqSm2FirmwareType": cpqSm2FirmwareType,
       "cpqSm2FwFailureCode": cpqSm2FwFailureCode,
       "cpqSm2Trap": cpqSm2Trap,
       "cpqSm2Products": cpqSm2Products,
       "cpaSm2ProdEisaRemote": cpaSm2ProdEisaRemote,
       "cpqSm2ProdPCIRemote": cpqSm2ProdPCIRemote,
       "cpqSm2ProdRILOE": cpqSm2ProdRILOE,
       "cpqSm2ProdiLo": cpqSm2ProdiLo,
       "cpqSm2ProdRILOEII": cpqSm2ProdRILOEII,
       "cpqSm2ProdRILO2": cpqSm2ProdRILO2,
       "cpqSm2ProdRLO100": cpqSm2ProdRLO100,
       "cpqSm2ProdRILO3": cpqSm2ProdRILO3,
       "cpqSm2ProdRILO4": cpqSm2ProdRILO4,
       "cpqSm2ProdRILO5": cpqSm2ProdRILO5}
)
