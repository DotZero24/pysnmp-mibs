# SNMP MIB module (ADTRAN-TAESCUAUTOUPGRADE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-TAESCUAUTOUPGRADE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:33:49 2025
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

(adGenSlotInfoIndex,
 adGenSlotProdName,
 adGenSlotProdSwVersion) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex",
    "adGenSlotProdName",
    "adGenSlotProdSwVersion")

(adTrapInformSeqNum,) = mibBuilder.importSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    "adTrapInformSeqNum")

(adTAeSCU,
 adTAeSCUmg,
 adTAeSCUmgNotificationEvents) = mibBuilder.importSymbols(
    "ADTRAN-TAeSCU-MIB",
    "adTAeSCU",
    "adTAeSCUmg",
    "adTAeSCUmgNotificationEvents")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

adTAeSCUAutoUpgradeMgmt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 11)
)
if mibBuilder.loadTexts:
    adTAeSCUAutoUpgradeMgmt.setRevisions(
        ("2010-02-24 13:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _AdTAeScuAutoUpgradeInitiate_Type(Integer32):
    """Custom type adTAeScuAutoUpgradeInitiate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("initiateAutoUpgrade", 1)
    )


_AdTAeScuAutoUpgradeInitiate_Type.__name__ = "Integer32"
_AdTAeScuAutoUpgradeInitiate_Object = MibScalar
adTAeScuAutoUpgradeInitiate = _AdTAeScuAutoUpgradeInitiate_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 11, 1),
    _AdTAeScuAutoUpgradeInitiate_Type()
)
adTAeScuAutoUpgradeInitiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuAutoUpgradeInitiate.setStatus("current")


class _AdTAeScuAutoUpgradeCancel_Type(Integer32):
    """Custom type adTAeScuAutoUpgradeCancel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("cancelAutoUpgrade", 1)
    )


_AdTAeScuAutoUpgradeCancel_Type.__name__ = "Integer32"
_AdTAeScuAutoUpgradeCancel_Object = MibScalar
adTAeScuAutoUpgradeCancel = _AdTAeScuAutoUpgradeCancel_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 11, 2),
    _AdTAeScuAutoUpgradeCancel_Type()
)
adTAeScuAutoUpgradeCancel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuAutoUpgradeCancel.setStatus("current")


class _AdTAeScuAutoUpgradeRetries_Type(Integer32):
    """Custom type adTAeScuAutoUpgradeRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_AdTAeScuAutoUpgradeRetries_Type.__name__ = "Integer32"
_AdTAeScuAutoUpgradeRetries_Object = MibScalar
adTAeScuAutoUpgradeRetries = _AdTAeScuAutoUpgradeRetries_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 11, 3),
    _AdTAeScuAutoUpgradeRetries_Type()
)
adTAeScuAutoUpgradeRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuAutoUpgradeRetries.setStatus("current")


class _AdTAeScuAutoUpgradeRefeshInterval_Type(Integer32):
    """Custom type adTAeScuAutoUpgradeRefeshInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 744),
    )


_AdTAeScuAutoUpgradeRefeshInterval_Type.__name__ = "Integer32"
_AdTAeScuAutoUpgradeRefeshInterval_Object = MibScalar
adTAeScuAutoUpgradeRefeshInterval = _AdTAeScuAutoUpgradeRefeshInterval_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 11, 4),
    _AdTAeScuAutoUpgradeRefeshInterval_Type()
)
adTAeScuAutoUpgradeRefeshInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuAutoUpgradeRefeshInterval.setStatus("current")


class _AdTAeScuAutoUpgradeMode_Type(Integer32):
    """Custom type adTAeScuAutoUpgradeMode based on Integer32"""
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
          ("manual", 2),
          ("disabled", 3))
    )


_AdTAeScuAutoUpgradeMode_Type.__name__ = "Integer32"
_AdTAeScuAutoUpgradeMode_Object = MibScalar
adTAeScuAutoUpgradeMode = _AdTAeScuAutoUpgradeMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 11, 5),
    _AdTAeScuAutoUpgradeMode_Type()
)
adTAeScuAutoUpgradeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuAutoUpgradeMode.setStatus("current")


class _AdTAeScuAutoUpgradeConfigFilename_Type(DisplayString):
    """Custom type adTAeScuAutoUpgradeConfigFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AdTAeScuAutoUpgradeConfigFilename_Type.__name__ = "DisplayString"
_AdTAeScuAutoUpgradeConfigFilename_Object = MibScalar
adTAeScuAutoUpgradeConfigFilename = _AdTAeScuAutoUpgradeConfigFilename_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 11, 6),
    _AdTAeScuAutoUpgradeConfigFilename_Type()
)
adTAeScuAutoUpgradeConfigFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuAutoUpgradeConfigFilename.setStatus("current")


class _AdTAeScuAutoUpgradeBasePath_Type(DisplayString):
    """Custom type adTAeScuAutoUpgradeBasePath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AdTAeScuAutoUpgradeBasePath_Type.__name__ = "DisplayString"
_AdTAeScuAutoUpgradeBasePath_Object = MibScalar
adTAeScuAutoUpgradeBasePath = _AdTAeScuAutoUpgradeBasePath_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 11, 7),
    _AdTAeScuAutoUpgradeBasePath_Type()
)
adTAeScuAutoUpgradeBasePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuAutoUpgradeBasePath.setStatus("current")


class _AdTAeScuAutoUpgradeInvalidate_Type(Integer32):
    """Custom type adTAeScuAutoUpgradeInvalidate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("discardCurrentConfigInfo", 1)
    )


_AdTAeScuAutoUpgradeInvalidate_Type.__name__ = "Integer32"
_AdTAeScuAutoUpgradeInvalidate_Object = MibScalar
adTAeScuAutoUpgradeInvalidate = _AdTAeScuAutoUpgradeInvalidate_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 11, 8),
    _AdTAeScuAutoUpgradeInvalidate_Type()
)
adTAeScuAutoUpgradeInvalidate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuAutoUpgradeInvalidate.setStatus("current")
_AdTAeScuAutoUpgradeSystemRelease_Type = DisplayString
_AdTAeScuAutoUpgradeSystemRelease_Object = MibScalar
adTAeScuAutoUpgradeSystemRelease = _AdTAeScuAutoUpgradeSystemRelease_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 11, 9),
    _AdTAeScuAutoUpgradeSystemRelease_Type()
)
adTAeScuAutoUpgradeSystemRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeScuAutoUpgradeSystemRelease.setStatus("current")
_AdTAeSCUAutoUpgradeStatusTable_Object = MibTable
adTAeSCUAutoUpgradeStatusTable = _AdTAeSCUAutoUpgradeStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 11, 10)
)
if mibBuilder.loadTexts:
    adTAeSCUAutoUpgradeStatusTable.setStatus("current")
_AdTAeSCUAutoUpgradeStatusEntry_Object = MibTableRow
adTAeSCUAutoUpgradeStatusEntry = _AdTAeSCUAutoUpgradeStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 11, 10, 1)
)
adTAeSCUAutoUpgradeStatusEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adTAeSCUAutoUpgradeStatusEntry.setStatus("current")


class _AdTAeScuAutoUpgradeStatus_Type(DisplayString):
    """Custom type adTAeScuAutoUpgradeStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AdTAeScuAutoUpgradeStatus_Type.__name__ = "DisplayString"
_AdTAeScuAutoUpgradeStatus_Object = MibTableColumn
adTAeScuAutoUpgradeStatus = _AdTAeScuAutoUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 11, 10, 1, 1),
    _AdTAeScuAutoUpgradeStatus_Type()
)
adTAeScuAutoUpgradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeScuAutoUpgradeStatus.setStatus("current")


class _AdTAeScuAutoUpgradeSWVerErrLevel_Type(Integer32):
    """Custom type adTAeScuAutoUpgradeSWVerErrLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("alert", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6))
    )


_AdTAeScuAutoUpgradeSWVerErrLevel_Type.__name__ = "Integer32"
_AdTAeScuAutoUpgradeSWVerErrLevel_Object = MibScalar
adTAeScuAutoUpgradeSWVerErrLevel = _AdTAeScuAutoUpgradeSWVerErrLevel_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 11, 11),
    _AdTAeScuAutoUpgradeSWVerErrLevel_Type()
)
adTAeScuAutoUpgradeSWVerErrLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuAutoUpgradeSWVerErrLevel.setStatus("current")

# Managed Objects groups


# Notification objects

adTAeSCUAutoUpgradeConfigChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 241, 0, 24150)
)
adTAeSCUAutoUpgradeConfigChanged.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adTAeSCUAutoUpgradeConfigChanged.setStatus(
        "current"
    )

adTAeSCUAutoUpgradeInvalidConfigFile = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 241, 0, 24152)
)
adTAeSCUAutoUpgradeInvalidConfigFile.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adTAeSCUAutoUpgradeInvalidConfigFile.setStatus(
        "current"
    )

adTAeSCUAutoUpgradeModuleUpgradeStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 241, 0, 24154)
)
adTAeSCUAutoUpgradeModuleUpgradeStarted.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adTAeSCUAutoUpgradeModuleUpgradeStarted.setStatus(
        "current"
    )

adTAeSCUAutoUpgradeModuleUpgradeCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 241, 0, 24156)
)
adTAeSCUAutoUpgradeModuleUpgradeCompleted.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adTAeSCUAutoUpgradeModuleUpgradeCompleted.setStatus(
        "current"
    )

adTAeSCUAutoUpgradeModuleUpgradeFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 241, 0, 24158)
)
adTAeSCUAutoUpgradeModuleUpgradeFailed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-TAESCUAUTOUPGRADE-MIB", "adTAeScuAutoUpgradeStatus"))
)
if mibBuilder.loadTexts:
    adTAeSCUAutoUpgradeModuleUpgradeFailed.setStatus(
        "current"
    )

adTAeSCUAutoUpgradeUnknownModule = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 241, 0, 24160)
)
adTAeSCUAutoUpgradeUnknownModule.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adTAeSCUAutoUpgradeUnknownModule.setStatus(
        "current"
    )

adTAAUSoftwareVerErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 241, 0, 24166)
)
adTAAUSoftwareVerErrorClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotProdName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotProdSwVersion"),
        ("ADTRAN-TAESCUAUTOUPGRADE-MIB", "adTAeScuAutoUpgradeSWVerErrLevel"))
)
if mibBuilder.loadTexts:
    adTAAUSoftwareVerErrorClear.setStatus(
        "current"
    )

adTAAUSoftwareVerErrorActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 241, 0, 24167)
)
adTAAUSoftwareVerErrorActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotProdName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotProdSwVersion"),
        ("ADTRAN-TAESCUAUTOUPGRADE-MIB", "adTAeScuAutoUpgradeSWVerErrLevel"))
)
if mibBuilder.loadTexts:
    adTAAUSoftwareVerErrorActive.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-TAESCUAUTOUPGRADE-MIB",
    **{"adTAeSCUAutoUpgradeConfigChanged": adTAeSCUAutoUpgradeConfigChanged,
       "adTAeSCUAutoUpgradeInvalidConfigFile": adTAeSCUAutoUpgradeInvalidConfigFile,
       "adTAeSCUAutoUpgradeModuleUpgradeStarted": adTAeSCUAutoUpgradeModuleUpgradeStarted,
       "adTAeSCUAutoUpgradeModuleUpgradeCompleted": adTAeSCUAutoUpgradeModuleUpgradeCompleted,
       "adTAeSCUAutoUpgradeModuleUpgradeFailed": adTAeSCUAutoUpgradeModuleUpgradeFailed,
       "adTAeSCUAutoUpgradeUnknownModule": adTAeSCUAutoUpgradeUnknownModule,
       "adTAAUSoftwareVerErrorClear": adTAAUSoftwareVerErrorClear,
       "adTAAUSoftwareVerErrorActive": adTAAUSoftwareVerErrorActive,
       "adTAeSCUAutoUpgradeMgmt": adTAeSCUAutoUpgradeMgmt,
       "adTAeScuAutoUpgradeInitiate": adTAeScuAutoUpgradeInitiate,
       "adTAeScuAutoUpgradeCancel": adTAeScuAutoUpgradeCancel,
       "adTAeScuAutoUpgradeRetries": adTAeScuAutoUpgradeRetries,
       "adTAeScuAutoUpgradeRefeshInterval": adTAeScuAutoUpgradeRefeshInterval,
       "adTAeScuAutoUpgradeMode": adTAeScuAutoUpgradeMode,
       "adTAeScuAutoUpgradeConfigFilename": adTAeScuAutoUpgradeConfigFilename,
       "adTAeScuAutoUpgradeBasePath": adTAeScuAutoUpgradeBasePath,
       "adTAeScuAutoUpgradeInvalidate": adTAeScuAutoUpgradeInvalidate,
       "adTAeScuAutoUpgradeSystemRelease": adTAeScuAutoUpgradeSystemRelease,
       "adTAeSCUAutoUpgradeStatusTable": adTAeSCUAutoUpgradeStatusTable,
       "adTAeSCUAutoUpgradeStatusEntry": adTAeSCUAutoUpgradeStatusEntry,
       "adTAeScuAutoUpgradeStatus": adTAeScuAutoUpgradeStatus,
       "adTAeScuAutoUpgradeSWVerErrLevel": adTAeScuAutoUpgradeSWVerErrLevel}
)
