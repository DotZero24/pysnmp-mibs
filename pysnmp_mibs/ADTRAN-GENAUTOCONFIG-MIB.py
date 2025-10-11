# SNMP MIB module (ADTRAN-GENAUTOCONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENAUTOCONFIG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:31:28 2025
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

(adGenSlotProdPartNumber,
 adGenSlotProdSwVersion) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotProdPartNumber",
    "adGenSlotProdSwVersion")

(adTrapInformSeqNum,) = mibBuilder.importSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    "adTrapInformSeqNum")

(adGenAutoConfig,
 adGenAutoConfigID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenAutoConfig",
    "adGenAutoConfigID")

(InetAddressIPv4,
 InetAddressIPv6) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6")

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
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

adGenAutoConfigMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 59, 1)
)
if mibBuilder.loadTexts:
    adGenAutoConfigMIB.setRevisions(
        ("2014-10-13 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenAutoConfigEvents_ObjectIdentity = ObjectIdentity
adGenAutoConfigEvents = _AdGenAutoConfigEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 59, 0)
)
_AdGenAutoConfigStatus_ObjectIdentity = ObjectIdentity
adGenAutoConfigStatus = _AdGenAutoConfigStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 59, 1)
)
_AdGenAutoConfigEnabled_Type = TruthValue
_AdGenAutoConfigEnabled_Object = MibScalar
adGenAutoConfigEnabled = _AdGenAutoConfigEnabled_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 59, 1, 1),
    _AdGenAutoConfigEnabled_Type()
)
adGenAutoConfigEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAutoConfigEnabled.setStatus("current")
_AdGenAutoConfigHostIPv4_Type = InetAddressIPv4
_AdGenAutoConfigHostIPv4_Object = MibScalar
adGenAutoConfigHostIPv4 = _AdGenAutoConfigHostIPv4_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 59, 1, 2),
    _AdGenAutoConfigHostIPv4_Type()
)
adGenAutoConfigHostIPv4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAutoConfigHostIPv4.setStatus("current")
_AdGenAutoConfigHostIPv6_Type = InetAddressIPv6
_AdGenAutoConfigHostIPv6_Object = MibScalar
adGenAutoConfigHostIPv6 = _AdGenAutoConfigHostIPv6_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 59, 1, 3),
    _AdGenAutoConfigHostIPv6_Type()
)
adGenAutoConfigHostIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAutoConfigHostIPv6.setStatus("current")
_AdGenAutoConfigFilename_Type = DisplayString
_AdGenAutoConfigFilename_Object = MibScalar
adGenAutoConfigFilename = _AdGenAutoConfigFilename_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 59, 1, 4),
    _AdGenAutoConfigFilename_Type()
)
adGenAutoConfigFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAutoConfigFilename.setStatus("current")
_AdGenAutoConfigGroupName_Type = DisplayString
_AdGenAutoConfigGroupName_Object = MibScalar
adGenAutoConfigGroupName = _AdGenAutoConfigGroupName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 59, 1, 5),
    _AdGenAutoConfigGroupName_Type()
)
adGenAutoConfigGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAutoConfigGroupName.setStatus("current")
_AdGenAutoConfigTempConfigFilename_Type = DisplayString
_AdGenAutoConfigTempConfigFilename_Object = MibScalar
adGenAutoConfigTempConfigFilename = _AdGenAutoConfigTempConfigFilename_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 59, 1, 6),
    _AdGenAutoConfigTempConfigFilename_Type()
)
adGenAutoConfigTempConfigFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAutoConfigTempConfigFilename.setStatus("current")
_AdGenAutoConfigUnitConfigFilename_Type = DisplayString
_AdGenAutoConfigUnitConfigFilename_Object = MibScalar
adGenAutoConfigUnitConfigFilename = _AdGenAutoConfigUnitConfigFilename_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 59, 1, 7),
    _AdGenAutoConfigUnitConfigFilename_Type()
)
adGenAutoConfigUnitConfigFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAutoConfigUnitConfigFilename.setStatus("current")
_AdGenAutoConfigBaseConfigFilename_Type = DisplayString
_AdGenAutoConfigBaseConfigFilename_Object = MibScalar
adGenAutoConfigBaseConfigFilename = _AdGenAutoConfigBaseConfigFilename_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 59, 1, 8),
    _AdGenAutoConfigBaseConfigFilename_Type()
)
adGenAutoConfigBaseConfigFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAutoConfigBaseConfigFilename.setStatus("current")
_AdGenAutoConfigFirmwareDefinitionFilename_Type = DisplayString
_AdGenAutoConfigFirmwareDefinitionFilename_Object = MibScalar
adGenAutoConfigFirmwareDefinitionFilename = _AdGenAutoConfigFirmwareDefinitionFilename_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 59, 1, 9),
    _AdGenAutoConfigFirmwareDefinitionFilename_Type()
)
adGenAutoConfigFirmwareDefinitionFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAutoConfigFirmwareDefinitionFilename.setStatus("current")


class _AdGenAutoConfigRetryCount_Type(Unsigned32):
    """Custom type adGenAutoConfigRetryCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_AdGenAutoConfigRetryCount_Type.__name__ = "Unsigned32"
_AdGenAutoConfigRetryCount_Object = MibScalar
adGenAutoConfigRetryCount = _AdGenAutoConfigRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 59, 1, 10),
    _AdGenAutoConfigRetryCount_Type()
)
adGenAutoConfigRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAutoConfigRetryCount.setStatus("current")


class _AdGenAutoConfigPollingInterval_Type(Unsigned32):
    """Custom type adGenAutoConfigPollingInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2592000),
    )


_AdGenAutoConfigPollingInterval_Type.__name__ = "Unsigned32"
_AdGenAutoConfigPollingInterval_Object = MibScalar
adGenAutoConfigPollingInterval = _AdGenAutoConfigPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 59, 1, 11),
    _AdGenAutoConfigPollingInterval_Type()
)
adGenAutoConfigPollingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAutoConfigPollingInterval.setStatus("current")


class _AdGenAutoConfigProtocol_Type(Integer32):
    """Custom type adGenAutoConfigProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tftp", 1),
          ("ftp", 2),
          ("sftp", 3))
    )


_AdGenAutoConfigProtocol_Type.__name__ = "Integer32"
_AdGenAutoConfigProtocol_Object = MibScalar
adGenAutoConfigProtocol = _AdGenAutoConfigProtocol_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 59, 1, 12),
    _AdGenAutoConfigProtocol_Type()
)
adGenAutoConfigProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAutoConfigProtocol.setStatus("current")


class _AdGenAutoConfigProtocolPortSFTP_Type(Unsigned32):
    """Custom type adGenAutoConfigProtocolPortSFTP based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AdGenAutoConfigProtocolPortSFTP_Type.__name__ = "Unsigned32"
_AdGenAutoConfigProtocolPortSFTP_Object = MibScalar
adGenAutoConfigProtocolPortSFTP = _AdGenAutoConfigProtocolPortSFTP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 59, 1, 13),
    _AdGenAutoConfigProtocolPortSFTP_Type()
)
adGenAutoConfigProtocolPortSFTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAutoConfigProtocolPortSFTP.setStatus("current")
_AdGenAutoConfigLastFailureFilename_Type = DisplayString
_AdGenAutoConfigLastFailureFilename_Object = MibScalar
adGenAutoConfigLastFailureFilename = _AdGenAutoConfigLastFailureFilename_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 59, 1, 14),
    _AdGenAutoConfigLastFailureFilename_Type()
)
adGenAutoConfigLastFailureFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAutoConfigLastFailureFilename.setStatus("current")
_AdGenAutoConfigLastFailureReason_Type = DisplayString
_AdGenAutoConfigLastFailureReason_Object = MibScalar
adGenAutoConfigLastFailureReason = _AdGenAutoConfigLastFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 59, 1, 15),
    _AdGenAutoConfigLastFailureReason_Type()
)
adGenAutoConfigLastFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAutoConfigLastFailureReason.setStatus("current")
_AdGenAutoConfigCurrentStatus_Type = DisplayString
_AdGenAutoConfigCurrentStatus_Object = MibScalar
adGenAutoConfigCurrentStatus = _AdGenAutoConfigCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 59, 1, 16),
    _AdGenAutoConfigCurrentStatus_Type()
)
adGenAutoConfigCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAutoConfigCurrentStatus.setStatus("current")


class _AdGenAutoConfigFailureAlmSeverity_Type(Integer32):
    """Custom type adGenAutoConfigFailureAlmSeverity based on Integer32"""
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
        *(("disabled", 1),
          ("info", 2),
          ("alert", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6))
    )


_AdGenAutoConfigFailureAlmSeverity_Type.__name__ = "Integer32"
_AdGenAutoConfigFailureAlmSeverity_Object = MibScalar
adGenAutoConfigFailureAlmSeverity = _AdGenAutoConfigFailureAlmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 59, 1, 17),
    _AdGenAutoConfigFailureAlmSeverity_Type()
)
adGenAutoConfigFailureAlmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAutoConfigFailureAlmSeverity.setStatus("current")


class _AdGenAutoConfigTimeoutAlmSeverity_Type(Integer32):
    """Custom type adGenAutoConfigTimeoutAlmSeverity based on Integer32"""
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
        *(("disabled", 1),
          ("info", 2),
          ("alert", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6))
    )


_AdGenAutoConfigTimeoutAlmSeverity_Type.__name__ = "Integer32"
_AdGenAutoConfigTimeoutAlmSeverity_Object = MibScalar
adGenAutoConfigTimeoutAlmSeverity = _AdGenAutoConfigTimeoutAlmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 59, 1, 18),
    _AdGenAutoConfigTimeoutAlmSeverity_Type()
)
adGenAutoConfigTimeoutAlmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAutoConfigTimeoutAlmSeverity.setStatus("current")
_AdGenAutoConfigProvisioning_ObjectIdentity = ObjectIdentity
adGenAutoConfigProvisioning = _AdGenAutoConfigProvisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 59, 2)
)


class _AdGenAutoConfigRestart_Type(Integer32):
    """Custom type adGenAutoConfigRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("restart", 1)
    )


_AdGenAutoConfigRestart_Type.__name__ = "Integer32"
_AdGenAutoConfigRestart_Object = MibScalar
adGenAutoConfigRestart = _AdGenAutoConfigRestart_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 59, 2, 1),
    _AdGenAutoConfigRestart_Type()
)
adGenAutoConfigRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAutoConfigRestart.setStatus("current")

# Managed Objects groups


# Notification objects

adGenAutoConfigFailureAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 59, 0, 1)
)
adGenAutoConfigFailureAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENAUTOCONFIG-MIB", "adGenAutoConfigFailureAlmSeverity"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotProdPartNumber"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotProdSwVersion"),
        ("ADTRAN-GENAUTOCONFIG-MIB", "adGenAutoConfigHostIPv4"),
        ("ADTRAN-GENAUTOCONFIG-MIB", "adGenAutoConfigHostIPv6"),
        ("ADTRAN-GENAUTOCONFIG-MIB", "adGenAutoConfigFilename"),
        ("ADTRAN-GENAUTOCONFIG-MIB", "adGenAutoConfigGroupName"),
        ("ADTRAN-GENAUTOCONFIG-MIB", "adGenAutoConfigTempConfigFilename"),
        ("ADTRAN-GENAUTOCONFIG-MIB", "adGenAutoConfigUnitConfigFilename"),
        ("ADTRAN-GENAUTOCONFIG-MIB", "adGenAutoConfigBaseConfigFilename"),
        ("ADTRAN-GENAUTOCONFIG-MIB", "adGenAutoConfigFirmwareDefinitionFilename"),
        ("ADTRAN-GENAUTOCONFIG-MIB", "adGenAutoConfigLastFailureFilename"),
        ("ADTRAN-GENAUTOCONFIG-MIB", "adGenAutoConfigLastFailureReason"))
)
if mibBuilder.loadTexts:
    adGenAutoConfigFailureAlm.setStatus(
        "current"
    )

adGenAutoConfigTimeoutAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 59, 0, 2)
)
adGenAutoConfigTimeoutAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENAUTOCONFIG-MIB", "adGenAutoConfigTimeoutAlmSeverity"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotProdPartNumber"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotProdSwVersion"),
        ("ADTRAN-GENAUTOCONFIG-MIB", "adGenAutoConfigHostIPv4"),
        ("ADTRAN-GENAUTOCONFIG-MIB", "adGenAutoConfigHostIPv6"),
        ("ADTRAN-GENAUTOCONFIG-MIB", "adGenAutoConfigLastFailureFilename"))
)
if mibBuilder.loadTexts:
    adGenAutoConfigTimeoutAlm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENAUTOCONFIG-MIB",
    **{"adGenAutoConfigEvents": adGenAutoConfigEvents,
       "adGenAutoConfigFailureAlm": adGenAutoConfigFailureAlm,
       "adGenAutoConfigTimeoutAlm": adGenAutoConfigTimeoutAlm,
       "adGenAutoConfigStatus": adGenAutoConfigStatus,
       "adGenAutoConfigEnabled": adGenAutoConfigEnabled,
       "adGenAutoConfigHostIPv4": adGenAutoConfigHostIPv4,
       "adGenAutoConfigHostIPv6": adGenAutoConfigHostIPv6,
       "adGenAutoConfigFilename": adGenAutoConfigFilename,
       "adGenAutoConfigGroupName": adGenAutoConfigGroupName,
       "adGenAutoConfigTempConfigFilename": adGenAutoConfigTempConfigFilename,
       "adGenAutoConfigUnitConfigFilename": adGenAutoConfigUnitConfigFilename,
       "adGenAutoConfigBaseConfigFilename": adGenAutoConfigBaseConfigFilename,
       "adGenAutoConfigFirmwareDefinitionFilename": adGenAutoConfigFirmwareDefinitionFilename,
       "adGenAutoConfigRetryCount": adGenAutoConfigRetryCount,
       "adGenAutoConfigPollingInterval": adGenAutoConfigPollingInterval,
       "adGenAutoConfigProtocol": adGenAutoConfigProtocol,
       "adGenAutoConfigProtocolPortSFTP": adGenAutoConfigProtocolPortSFTP,
       "adGenAutoConfigLastFailureFilename": adGenAutoConfigLastFailureFilename,
       "adGenAutoConfigLastFailureReason": adGenAutoConfigLastFailureReason,
       "adGenAutoConfigCurrentStatus": adGenAutoConfigCurrentStatus,
       "adGenAutoConfigFailureAlmSeverity": adGenAutoConfigFailureAlmSeverity,
       "adGenAutoConfigTimeoutAlmSeverity": adGenAutoConfigTimeoutAlmSeverity,
       "adGenAutoConfigProvisioning": adGenAutoConfigProvisioning,
       "adGenAutoConfigRestart": adGenAutoConfigRestart,
       "adGenAutoConfigMIB": adGenAutoConfigMIB}
)
