# SNMP MIB module (RAINBOW-NOTIFICATIONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/alvarion/RAINBOW-NOTIFICATIONS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:07:13 2025
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

(rainbow,
 rbChannelId,
 rbLicenseId,
 rbSuMacAddr,
 rbSuSysName,
 rbSuTxPower,
 rbTrapAdditionalInfo,
 rbTrapCategory,
 rbTrapIpAddress,
 rbTrapLedStatus,
 rbTrapSeqNumber,
 rbTrapSetFailureReason,
 rbTrapSeverity,
 rbTrapSource) = mibBuilder.importSymbols(
    "RAINBOW-MIB",
    "rainbow",
    "rbChannelId",
    "rbLicenseId",
    "rbSuMacAddr",
    "rbSuSysName",
    "rbSuTxPower",
    "rbTrapAdditionalInfo",
    "rbTrapCategory",
    "rbTrapIpAddress",
    "rbTrapLedStatus",
    "rbTrapSeqNumber",
    "rbTrapSetFailureReason",
    "rbTrapSeverity",
    "rbTrapSource")

(rbRadiusAcctServerAddress,
 rbRadiusAuthServerAddress) = mibBuilder.importSymbols(
    "RAINBOW-RADIUS-MIB",
    "rbRadiusAcctServerAddress",
    "rbRadiusAuthServerAddress")

(rbServiceIdx,
 rbServiceName,
 rbSubscriberID,
 rbSubscriberIdx) = mibBuilder.importSymbols(
    "RAINBOW-SERVICES-MIB",
    "rbServiceIdx",
    "rbServiceName",
    "rbSubscriberID",
    "rbSubscriberIdx")

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

rbNotifications = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0)
)
if mibBuilder.loadTexts:
    rbNotifications.setRevisions(
        ("2006-06-06 15:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

rbResetOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 1)
)
rbResetOn.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-MIB", "rbTrapAdditionalInfo"))
)
if mibBuilder.loadTexts:
    rbResetOn.setStatus(
        "current"
    )

rbDiagnosticsHwFaultOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 2)
)
rbDiagnosticsHwFaultOn.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-MIB", "rbTrapAdditionalInfo"),
        ("RAINBOW-MIB", "rbTrapLedStatus"))
)
if mibBuilder.loadTexts:
    rbDiagnosticsHwFaultOn.setStatus(
        "current"
    )

rbDiagnosticsHwFaultOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 3)
)
rbDiagnosticsHwFaultOff.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-MIB", "rbTrapAdditionalInfo"),
        ("RAINBOW-MIB", "rbTrapLedStatus"))
)
if mibBuilder.loadTexts:
    rbDiagnosticsHwFaultOff.setStatus(
        "current"
    )

rbMonitorAccessOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 4)
)
rbMonitorAccessOn.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-MIB", "rbTrapAdditionalInfo"),
        ("RAINBOW-MIB", "rbTrapIpAddress"))
)
if mibBuilder.loadTexts:
    rbMonitorAccessOn.setStatus(
        "current"
    )

rbMonitorAccessOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 5)
)
rbMonitorAccessOff.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-MIB", "rbTrapAdditionalInfo"),
        ("RAINBOW-MIB", "rbTrapIpAddress"))
)
if mibBuilder.loadTexts:
    rbMonitorAccessOff.setStatus(
        "current"
    )

rbAuNetworkEntryStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 6)
)
rbAuNetworkEntryStatus.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-MIB", "rbTrapAdditionalInfo"))
)
if mibBuilder.loadTexts:
    rbAuNetworkEntryStatus.setStatus(
        "current"
    )

rbModeConflictOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 7)
)
rbModeConflictOn.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-MIB", "rbTrapAdditionalInfo"))
)
if mibBuilder.loadTexts:
    rbModeConflictOn.setStatus(
        "current"
    )

rbModeConflictOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 8)
)
rbModeConflictOff.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-MIB", "rbTrapAdditionalInfo"))
)
if mibBuilder.loadTexts:
    rbModeConflictOff.setStatus(
        "current"
    )

rbShelfCardExtractionOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 21)
)
rbShelfCardExtractionOn.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"))
)
if mibBuilder.loadTexts:
    rbShelfCardExtractionOn.setStatus(
        "current"
    )

rbShelfCardInsertionOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 22)
)
rbShelfCardInsertionOn.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"))
)
if mibBuilder.loadTexts:
    rbShelfCardInsertionOn.setStatus(
        "current"
    )

rbShelfPeripheralEquipmentFaultOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 23)
)
rbShelfPeripheralEquipmentFaultOn.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-MIB", "rbTrapAdditionalInfo"))
)
if mibBuilder.loadTexts:
    rbShelfPeripheralEquipmentFaultOn.setStatus(
        "current"
    )

rbShelfPeripherallEquipmentFaultOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 24)
)
rbShelfPeripherallEquipmentFaultOff.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-MIB", "rbTrapAdditionalInfo"))
)
if mibBuilder.loadTexts:
    rbShelfPeripherallEquipmentFaultOff.setStatus(
        "current"
    )

rbShelfEnvParamFaultOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 25)
)
rbShelfEnvParamFaultOn.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-MIB", "rbTrapAdditionalInfo"))
)
if mibBuilder.loadTexts:
    rbShelfEnvParamFaultOn.setStatus(
        "current"
    )

rbShelfEnvParamFaultOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 26)
)
rbShelfEnvParamFaultOff.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-MIB", "rbTrapAdditionalInfo"))
)
if mibBuilder.loadTexts:
    rbShelfEnvParamFaultOff.setStatus(
        "current"
    )

rbConfigurationChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 41)
)
rbConfigurationChanged.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-MIB", "rbTrapAdditionalInfo"))
)
if mibBuilder.loadTexts:
    rbConfigurationChanged.setStatus(
        "current"
    )

rbParameterSetFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 42)
)
rbParameterSetFailure.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-MIB", "rbTrapSetFailureReason"))
)
if mibBuilder.loadTexts:
    rbParameterSetFailure.setStatus(
        "current"
    )

rbMbstLicense = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 50)
)
rbMbstLicense.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-MIB", "rbTrapAdditionalInfo"))
)
if mibBuilder.loadTexts:
    rbMbstLicense.setStatus(
        "current"
    )

rbMbstCPEQuantityExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 51)
)
rbMbstCPEQuantityExceed.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-MIB", "rbSuMacAddr"))
)
if mibBuilder.loadTexts:
    rbMbstCPEQuantityExceed.setStatus(
        "current"
    )

rbLicenseFileLoadStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 52)
)
rbLicenseFileLoadStatus.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-MIB", "rbTrapAdditionalInfo"))
)
if mibBuilder.loadTexts:
    rbLicenseFileLoadStatus.setStatus(
        "current"
    )

rbOduCrcErrorOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 61)
)
rbOduCrcErrorOn.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-MIB", "rbChannelId"))
)
if mibBuilder.loadTexts:
    rbOduCrcErrorOn.setStatus(
        "obsolete"
    )

rbOduCrcErrorOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 62)
)
rbOduCrcErrorOff.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-MIB", "rbChannelId"))
)
if mibBuilder.loadTexts:
    rbOduCrcErrorOff.setStatus(
        "obsolete"
    )

rbOduCommErrorOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 63)
)
rbOduCommErrorOn.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-MIB", "rbChannelId"))
)
if mibBuilder.loadTexts:
    rbOduCommErrorOn.setStatus(
        "current"
    )

rbOduCommErrorOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 64)
)
rbOduCommErrorOff.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-MIB", "rbChannelId"))
)
if mibBuilder.loadTexts:
    rbOduCommErrorOff.setStatus(
        "current"
    )

rbOduBandMissmatchOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 65)
)
rbOduBandMissmatchOn.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-MIB", "rbChannelId"))
)
if mibBuilder.loadTexts:
    rbOduBandMissmatchOn.setStatus(
        "current"
    )

rbOduBandMissmatchOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 66)
)
rbOduBandMissmatchOff.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-MIB", "rbChannelId"))
)
if mibBuilder.loadTexts:
    rbOduBandMissmatchOff.setStatus(
        "current"
    )

rbOduPowerMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 67)
)
rbOduPowerMismatch.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-MIB", "rbChannelId"))
)
if mibBuilder.loadTexts:
    rbOduPowerMismatch.setStatus(
        "current"
    )

rbOduFailureOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 68)
)
rbOduFailureOn.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-MIB", "rbChannelId"),
        ("RAINBOW-MIB", "rbTrapAdditionalInfo"))
)
if mibBuilder.loadTexts:
    rbOduFailureOn.setStatus(
        "current"
    )

rbOduFailureOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 69)
)
rbOduFailureOff.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-MIB", "rbChannelId"))
)
if mibBuilder.loadTexts:
    rbOduFailureOff.setStatus(
        "current"
    )

rbSuMaxTxPowerReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 81)
)
rbSuMaxTxPowerReached.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-MIB", "rbSuTxPower"))
)
if mibBuilder.loadTexts:
    rbSuMaxTxPowerReached.setStatus(
        "current"
    )

rbSuMinTxPowerReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 82)
)
rbSuMinTxPowerReached.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-MIB", "rbSuTxPower"))
)
if mibBuilder.loadTexts:
    rbSuMinTxPowerReached.setStatus(
        "current"
    )

rbSuNetworkEntryStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 83)
)
rbSuNetworkEntryStatus.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-MIB", "rbTrapAdditionalInfo"))
)
if mibBuilder.loadTexts:
    rbSuNetworkEntryStatus.setStatus(
        "current"
    )

rbSuLicense = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 84)
)
rbSuLicense.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-MIB", "rbTrapAdditionalInfo"),
        ("RAINBOW-MIB", "rbLicenseId"))
)
if mibBuilder.loadTexts:
    rbSuLicense.setStatus(
        "current"
    )

rbSuDuplicateName = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 85)
)
rbSuDuplicateName.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-MIB", "rbSuMacAddr"),
        ("RAINBOW-MIB", "rbSuSysName"),
        ("RAINBOW-MIB", "rbSuSysName"))
)
if mibBuilder.loadTexts:
    rbSuDuplicateName.setStatus(
        "current"
    )

rbSwDownloadStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 101)
)
rbSwDownloadStart.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"))
)
if mibBuilder.loadTexts:
    rbSwDownloadStart.setStatus(
        "current"
    )

rbSwDownloadEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 102)
)
rbSwDownloadEnd.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"))
)
if mibBuilder.loadTexts:
    rbSwDownloadEnd.setStatus(
        "current"
    )

rbSwDownloadError = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 103)
)
rbSwDownloadError.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-MIB", "rbTrapAdditionalInfo"))
)
if mibBuilder.loadTexts:
    rbSwDownloadError.setStatus(
        "current"
    )

rbSwSwitchFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 104)
)
rbSwSwitchFailed.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-MIB", "rbTrapAdditionalInfo"))
)
if mibBuilder.loadTexts:
    rbSwSwitchFailed.setStatus(
        "current"
    )

rbSwSwitchSucceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 105)
)
rbSwSwitchSucceed.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-MIB", "rbTrapAdditionalInfo"))
)
if mibBuilder.loadTexts:
    rbSwSwitchSucceed.setStatus(
        "current"
    )

rbBERTestFinished = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 106)
)
rbBERTestFinished.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"))
)
if mibBuilder.loadTexts:
    rbBERTestFinished.setStatus(
        "current"
    )

rbBERTestStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 107)
)
rbBERTestStarted.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"))
)
if mibBuilder.loadTexts:
    rbBERTestStarted.setStatus(
        "current"
    )

rbSwFileConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 108)
)
rbSwFileConflict.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"))
)
if mibBuilder.loadTexts:
    rbSwFileConflict.setStatus(
        "current"
    )

rbXMLDownloadResult = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 109)
)
rbXMLDownloadResult.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-MIB", "rbTrapAdditionalInfo"))
)
if mibBuilder.loadTexts:
    rbXMLDownloadResult.setStatus(
        "current"
    )

rbFreqBandDownloadResult = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 110)
)
rbFreqBandDownloadResult.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-MIB", "rbTrapAdditionalInfo"))
)
if mibBuilder.loadTexts:
    rbFreqBandDownloadResult.setStatus(
        "current"
    )

rbServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 111)
)
rbServiceDown.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-SERVICES-MIB", "rbServiceIdx"),
        ("RAINBOW-SERVICES-MIB", "rbSubscriberIdx"),
        ("RAINBOW-SERVICES-MIB", "rbServiceName"),
        ("RAINBOW-SERVICES-MIB", "rbSubscriberID"))
)
if mibBuilder.loadTexts:
    rbServiceDown.setStatus(
        "current"
    )

rbServiceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 112)
)
rbServiceUp.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-SERVICES-MIB", "rbServiceIdx"),
        ("RAINBOW-SERVICES-MIB", "rbSubscriberIdx"),
        ("RAINBOW-SERVICES-MIB", "rbServiceName"),
        ("RAINBOW-SERVICES-MIB", "rbSubscriberID"))
)
if mibBuilder.loadTexts:
    rbServiceUp.setStatus(
        "current"
    )

rbServiceChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 113)
)
rbServiceChanged.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-MIB", "rbTrapAdditionalInfo"),
        ("RAINBOW-SERVICES-MIB", "rbServiceIdx"),
        ("RAINBOW-SERVICES-MIB", "rbSubscriberIdx"),
        ("RAINBOW-SERVICES-MIB", "rbServiceName"),
        ("RAINBOW-SERVICES-MIB", "rbSubscriberID"))
)
if mibBuilder.loadTexts:
    rbServiceChanged.setStatus(
        "current"
    )

rbServiceGeneralError = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 114)
)
rbServiceGeneralError.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-MIB", "rbTrapAdditionalInfo"),
        ("RAINBOW-SERVICES-MIB", "rbServiceIdx"),
        ("RAINBOW-SERVICES-MIB", "rbSubscriberIdx"),
        ("RAINBOW-SERVICES-MIB", "rbServiceName"),
        ("RAINBOW-SERVICES-MIB", "rbSubscriberID"))
)
if mibBuilder.loadTexts:
    rbServiceGeneralError.setStatus(
        "current"
    )

rbNetworkingError = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 115)
)
rbNetworkingError.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-MIB", "rbTrapAdditionalInfo"))
)
if mibBuilder.loadTexts:
    rbNetworkingError.setStatus(
        "current"
    )

rbSwitchedAuthenticationServer = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 117)
)
rbSwitchedAuthenticationServer.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"))
)
if mibBuilder.loadTexts:
    rbSwitchedAuthenticationServer.setStatus(
        "current"
    )

rbSwitchedAccountingServer = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 118)
)
rbSwitchedAccountingServer.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"))
)
if mibBuilder.loadTexts:
    rbSwitchedAccountingServer.setStatus(
        "current"
    )

rbServiceEstablishmentFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 119)
)
rbServiceEstablishmentFailure.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-MIB", "rbTrapAdditionalInfo"),
        ("RAINBOW-SERVICES-MIB", "rbServiceIdx"),
        ("RAINBOW-SERVICES-MIB", "rbServiceName"))
)
if mibBuilder.loadTexts:
    rbServiceEstablishmentFailure.setStatus(
        "current"
    )

rbUserAuthenticationTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 120)
)
rbUserAuthenticationTimeout.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-MIB", "rbTrapAdditionalInfo"),
        ("RAINBOW-MIB", "rbSuMacAddr"))
)
if mibBuilder.loadTexts:
    rbUserAuthenticationTimeout.setStatus(
        "current"
    )

rbUserAuthenticationReject = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 121)
)
rbUserAuthenticationReject.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-MIB", "rbSuMacAddr"))
)
if mibBuilder.loadTexts:
    rbUserAuthenticationReject.setStatus(
        "current"
    )

rbAuthenticationServerKeepAliveTimeoutOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 122)
)
rbAuthenticationServerKeepAliveTimeoutOn.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-RADIUS-MIB", "rbRadiusAuthServerAddress"))
)
if mibBuilder.loadTexts:
    rbAuthenticationServerKeepAliveTimeoutOn.setStatus(
        "current"
    )

rbAuthenticationServerKeepAliveTimeoutOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 123)
)
rbAuthenticationServerKeepAliveTimeoutOff.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-RADIUS-MIB", "rbRadiusAuthServerAddress"))
)
if mibBuilder.loadTexts:
    rbAuthenticationServerKeepAliveTimeoutOff.setStatus(
        "current"
    )

rbAccountingServerKeepAliveTimeoutOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 124)
)
rbAccountingServerKeepAliveTimeoutOn.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-RADIUS-MIB", "rbRadiusAcctServerAddress"))
)
if mibBuilder.loadTexts:
    rbAccountingServerKeepAliveTimeoutOn.setStatus(
        "current"
    )

rbAccountingServerKeepAliveTimeoutOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 125)
)
rbAccountingServerKeepAliveTimeoutOff.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"),
        ("RAINBOW-RADIUS-MIB", "rbRadiusAcctServerAddress"))
)
if mibBuilder.loadTexts:
    rbAccountingServerKeepAliveTimeoutOff.setStatus(
        "current"
    )

rbExternal1PPSFailureOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 134)
)
rbExternal1PPSFailureOn.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"))
)
if mibBuilder.loadTexts:
    rbExternal1PPSFailureOn.setStatus(
        "current"
    )

rbExternal1PPSFailureOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 135)
)
rbExternal1PPSFailureOff.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"))
)
if mibBuilder.loadTexts:
    rbExternal1PPSFailureOff.setStatus(
        "current"
    )

rbInternal1PPSFailureOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 136)
)
rbInternal1PPSFailureOn.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"))
)
if mibBuilder.loadTexts:
    rbInternal1PPSFailureOn.setStatus(
        "current"
    )

rbInternal1PPSFailureOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 137)
)
rbInternal1PPSFailureOff.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"))
)
if mibBuilder.loadTexts:
    rbInternal1PPSFailureOff.setStatus(
        "current"
    )

rbExternal16MHzFailureOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 138)
)
rbExternal16MHzFailureOn.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"))
)
if mibBuilder.loadTexts:
    rbExternal16MHzFailureOn.setStatus(
        "current"
    )

rbExternal16MHzFailureOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 139)
)
rbExternal16MHzFailureOff.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"))
)
if mibBuilder.loadTexts:
    rbExternal16MHzFailureOff.setStatus(
        "current"
    )

rbInternal16MHzFailureOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 140)
)
rbInternal16MHzFailureOn.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"))
)
if mibBuilder.loadTexts:
    rbInternal16MHzFailureOn.setStatus(
        "current"
    )

rbInternal16MHzFailureOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 141)
)
rbInternal16MHzFailureOff.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"))
)
if mibBuilder.loadTexts:
    rbInternal16MHzFailureOff.setStatus(
        "current"
    )

rbGPSComFailureOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 142)
)
rbGPSComFailureOn.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"))
)
if mibBuilder.loadTexts:
    rbGPSComFailureOn.setStatus(
        "current"
    )

rbGPSComFailureOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 143)
)
rbGPSComFailureOff.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"))
)
if mibBuilder.loadTexts:
    rbGPSComFailureOff.setStatus(
        "current"
    )

rbGPSHealthyFailureOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 144)
)
rbGPSHealthyFailureOn.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"))
)
if mibBuilder.loadTexts:
    rbGPSHealthyFailureOn.setStatus(
        "current"
    )

rbGPSHealthyFailureOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 145)
)
rbGPSHealthyFailureOff.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"))
)
if mibBuilder.loadTexts:
    rbGPSHealthyFailureOff.setStatus(
        "current"
    )

rbMin4SatSyncFailureOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 146)
)
rbMin4SatSyncFailureOn.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"))
)
if mibBuilder.loadTexts:
    rbMin4SatSyncFailureOn.setStatus(
        "current"
    )

rbMin4SatSyncFailureOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 147)
)
rbMin4SatSyncFailureOff.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"))
)
if mibBuilder.loadTexts:
    rbMin4SatSyncFailureOff.setStatus(
        "current"
    )

rbAUExternal1PPSFailureOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 148)
)
rbAUExternal1PPSFailureOn.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"))
)
if mibBuilder.loadTexts:
    rbAUExternal1PPSFailureOn.setStatus(
        "current"
    )

rbAUExternal1PPSFailureOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 149)
)
rbAUExternal1PPSFailureOff.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"))
)
if mibBuilder.loadTexts:
    rbAUExternal1PPSFailureOff.setStatus(
        "current"
    )

rbAUHoldOverEnteredOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 150)
)
rbAUHoldOverEnteredOn.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"))
)
if mibBuilder.loadTexts:
    rbAUHoldOverEnteredOn.setStatus(
        "current"
    )

rbAUHoldOverEnteredOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 151)
)
rbAUHoldOverEnteredOff.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"))
)
if mibBuilder.loadTexts:
    rbAUHoldOverEnteredOff.setStatus(
        "current"
    )

rbAUHoldOverTimeoutPassedOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 152)
)
rbAUHoldOverTimeoutPassedOn.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"))
)
if mibBuilder.loadTexts:
    rbAUHoldOverTimeoutPassedOn.setStatus(
        "current"
    )

rbAUHoldOverTimeoutPassedOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 153)
)
rbAUHoldOverTimeoutPassedOff.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"))
)
if mibBuilder.loadTexts:
    rbAUHoldOverTimeoutPassedOff.setStatus(
        "current"
    )

rbAUHoldOverTxStoppedOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 154)
)
rbAUHoldOverTxStoppedOn.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"))
)
if mibBuilder.loadTexts:
    rbAUHoldOverTxStoppedOn.setStatus(
        "current"
    )

rbAUHoldOverTxStoppedOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 0, 155)
)
rbAUHoldOverTxStoppedOff.setObjects(
      *(("RAINBOW-MIB", "rbTrapSeqNumber"),
        ("RAINBOW-MIB", "rbTrapSource"),
        ("RAINBOW-MIB", "rbTrapSeverity"),
        ("RAINBOW-MIB", "rbTrapCategory"))
)
if mibBuilder.loadTexts:
    rbAUHoldOverTxStoppedOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAINBOW-NOTIFICATIONS-MIB",
    **{"rbNotifications": rbNotifications,
       "rbResetOn": rbResetOn,
       "rbDiagnosticsHwFaultOn": rbDiagnosticsHwFaultOn,
       "rbDiagnosticsHwFaultOff": rbDiagnosticsHwFaultOff,
       "rbMonitorAccessOn": rbMonitorAccessOn,
       "rbMonitorAccessOff": rbMonitorAccessOff,
       "rbAuNetworkEntryStatus": rbAuNetworkEntryStatus,
       "rbModeConflictOn": rbModeConflictOn,
       "rbModeConflictOff": rbModeConflictOff,
       "rbShelfCardExtractionOn": rbShelfCardExtractionOn,
       "rbShelfCardInsertionOn": rbShelfCardInsertionOn,
       "rbShelfPeripheralEquipmentFaultOn": rbShelfPeripheralEquipmentFaultOn,
       "rbShelfPeripherallEquipmentFaultOff": rbShelfPeripherallEquipmentFaultOff,
       "rbShelfEnvParamFaultOn": rbShelfEnvParamFaultOn,
       "rbShelfEnvParamFaultOff": rbShelfEnvParamFaultOff,
       "rbConfigurationChanged": rbConfigurationChanged,
       "rbParameterSetFailure": rbParameterSetFailure,
       "rbMbstLicense": rbMbstLicense,
       "rbMbstCPEQuantityExceed": rbMbstCPEQuantityExceed,
       "rbLicenseFileLoadStatus": rbLicenseFileLoadStatus,
       "rbOduCrcErrorOn": rbOduCrcErrorOn,
       "rbOduCrcErrorOff": rbOduCrcErrorOff,
       "rbOduCommErrorOn": rbOduCommErrorOn,
       "rbOduCommErrorOff": rbOduCommErrorOff,
       "rbOduBandMissmatchOn": rbOduBandMissmatchOn,
       "rbOduBandMissmatchOff": rbOduBandMissmatchOff,
       "rbOduPowerMismatch": rbOduPowerMismatch,
       "rbOduFailureOn": rbOduFailureOn,
       "rbOduFailureOff": rbOduFailureOff,
       "rbSuMaxTxPowerReached": rbSuMaxTxPowerReached,
       "rbSuMinTxPowerReached": rbSuMinTxPowerReached,
       "rbSuNetworkEntryStatus": rbSuNetworkEntryStatus,
       "rbSuLicense": rbSuLicense,
       "rbSuDuplicateName": rbSuDuplicateName,
       "rbSwDownloadStart": rbSwDownloadStart,
       "rbSwDownloadEnd": rbSwDownloadEnd,
       "rbSwDownloadError": rbSwDownloadError,
       "rbSwSwitchFailed": rbSwSwitchFailed,
       "rbSwSwitchSucceed": rbSwSwitchSucceed,
       "rbBERTestFinished": rbBERTestFinished,
       "rbBERTestStarted": rbBERTestStarted,
       "rbSwFileConflict": rbSwFileConflict,
       "rbXMLDownloadResult": rbXMLDownloadResult,
       "rbFreqBandDownloadResult": rbFreqBandDownloadResult,
       "rbServiceDown": rbServiceDown,
       "rbServiceUp": rbServiceUp,
       "rbServiceChanged": rbServiceChanged,
       "rbServiceGeneralError": rbServiceGeneralError,
       "rbNetworkingError": rbNetworkingError,
       "rbSwitchedAuthenticationServer": rbSwitchedAuthenticationServer,
       "rbSwitchedAccountingServer": rbSwitchedAccountingServer,
       "rbServiceEstablishmentFailure": rbServiceEstablishmentFailure,
       "rbUserAuthenticationTimeout": rbUserAuthenticationTimeout,
       "rbUserAuthenticationReject": rbUserAuthenticationReject,
       "rbAuthenticationServerKeepAliveTimeoutOn": rbAuthenticationServerKeepAliveTimeoutOn,
       "rbAuthenticationServerKeepAliveTimeoutOff": rbAuthenticationServerKeepAliveTimeoutOff,
       "rbAccountingServerKeepAliveTimeoutOn": rbAccountingServerKeepAliveTimeoutOn,
       "rbAccountingServerKeepAliveTimeoutOff": rbAccountingServerKeepAliveTimeoutOff,
       "rbExternal1PPSFailureOn": rbExternal1PPSFailureOn,
       "rbExternal1PPSFailureOff": rbExternal1PPSFailureOff,
       "rbInternal1PPSFailureOn": rbInternal1PPSFailureOn,
       "rbInternal1PPSFailureOff": rbInternal1PPSFailureOff,
       "rbExternal16MHzFailureOn": rbExternal16MHzFailureOn,
       "rbExternal16MHzFailureOff": rbExternal16MHzFailureOff,
       "rbInternal16MHzFailureOn": rbInternal16MHzFailureOn,
       "rbInternal16MHzFailureOff": rbInternal16MHzFailureOff,
       "rbGPSComFailureOn": rbGPSComFailureOn,
       "rbGPSComFailureOff": rbGPSComFailureOff,
       "rbGPSHealthyFailureOn": rbGPSHealthyFailureOn,
       "rbGPSHealthyFailureOff": rbGPSHealthyFailureOff,
       "rbMin4SatSyncFailureOn": rbMin4SatSyncFailureOn,
       "rbMin4SatSyncFailureOff": rbMin4SatSyncFailureOff,
       "rbAUExternal1PPSFailureOn": rbAUExternal1PPSFailureOn,
       "rbAUExternal1PPSFailureOff": rbAUExternal1PPSFailureOff,
       "rbAUHoldOverEnteredOn": rbAUHoldOverEnteredOn,
       "rbAUHoldOverEnteredOff": rbAUHoldOverEnteredOff,
       "rbAUHoldOverTimeoutPassedOn": rbAUHoldOverTimeoutPassedOn,
       "rbAUHoldOverTimeoutPassedOff": rbAUHoldOverTimeoutPassedOff,
       "rbAUHoldOverTxStoppedOn": rbAUHoldOverTxStoppedOn,
       "rbAUHoldOverTxStoppedOff": rbAUHoldOverTxStoppedOff}
)
