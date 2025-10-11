# SNMP MIB module (CDE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/radware/CDE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:15:33 2025
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

(TruthValue,
 rdwrConfigurationSync) = mibBuilder.importSymbols(
    "RADWARE-MIB",
    "TruthValue",
    "rdwrConfigurationSync")

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

_RdwrConfigurationSyncMonitor_ObjectIdentity = ObjectIdentity
rdwrConfigurationSyncMonitor = _RdwrConfigurationSyncMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 161, 1)
)


class _RdwrConfSyncState_Type(Integer32):
    """Custom type rdwrConfSyncState based on Integer32"""
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
        *(("syncOff", 1),
          ("disconnected", 2),
          ("synchronizing", 3),
          ("inSync", 4),
          ("incompatible", 5),
          ("cannotSync", 6),
          ("pendingVRRPSwitch", 7),
          ("noMaster", 8),
          ("masterConnected", 9),
          ("outOfSync", 10))
    )


_RdwrConfSyncState_Type.__name__ = "Integer32"
_RdwrConfSyncState_Object = MibScalar
rdwrConfSyncState = _RdwrConfSyncState_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 161, 1, 1),
    _RdwrConfSyncState_Type()
)
rdwrConfSyncState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrConfSyncState.setStatus("mandatory")
_RdwrConfSyncIP_Type = IpAddress
_RdwrConfSyncIP_Object = MibScalar
rdwrConfSyncIP = _RdwrConfSyncIP_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 161, 1, 2),
    _RdwrConfSyncIP_Type()
)
rdwrConfSyncIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrConfSyncIP.setStatus("mandatory")
_RdwrConfSyncPeerIP_Type = IpAddress
_RdwrConfSyncPeerIP_Object = MibScalar
rdwrConfSyncPeerIP = _RdwrConfSyncPeerIP_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 161, 1, 3),
    _RdwrConfSyncPeerIP_Type()
)
rdwrConfSyncPeerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrConfSyncPeerIP.setStatus("mandatory")
_RdwrConfSyncPeerBaseMac_Type = PhysAddress
_RdwrConfSyncPeerBaseMac_Object = MibScalar
rdwrConfSyncPeerBaseMac = _RdwrConfSyncPeerBaseMac_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 161, 1, 4),
    _RdwrConfSyncPeerBaseMac_Type()
)
rdwrConfSyncPeerBaseMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrConfSyncPeerBaseMac.setStatus("mandatory")


class _RdwrConfSyncIncompatibilityReason_Type(Integer32):
    """Custom type rdwrConfSyncIncompatibilityReason based on Integer32"""
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
        *(("compatible", 1),
          ("incompatibleHardware", 2),
          ("incompatibleInstalledMemorySize", 3),
          ("incompatibleLicense", 4),
          ("incompatibleSoftwareVersion", 5),
          ("incompatibleSlaveConfiguration", 6),
          ("unknown", 7),
          ("incompatibleAttackDb", 8))
    )


_RdwrConfSyncIncompatibilityReason_Type.__name__ = "Integer32"
_RdwrConfSyncIncompatibilityReason_Object = MibScalar
rdwrConfSyncIncompatibilityReason = _RdwrConfSyncIncompatibilityReason_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 161, 1, 5),
    _RdwrConfSyncIncompatibilityReason_Type()
)
rdwrConfSyncIncompatibilityReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrConfSyncIncompatibilityReason.setStatus("mandatory")
_RdwrConfSyncLastConfSyncTime_Type = Unsigned32
_RdwrConfSyncLastConfSyncTime_Object = MibScalar
rdwrConfSyncLastConfSyncTime = _RdwrConfSyncLastConfSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 161, 1, 6),
    _RdwrConfSyncLastConfSyncTime_Type()
)
rdwrConfSyncLastConfSyncTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrConfSyncLastConfSyncTime.setStatus("mandatory")
_RdwrConfSyncLastConfFullSyncTime_Type = Unsigned32
_RdwrConfSyncLastConfFullSyncTime_Object = MibScalar
rdwrConfSyncLastConfFullSyncTime = _RdwrConfSyncLastConfFullSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 161, 1, 7),
    _RdwrConfSyncLastConfFullSyncTime_Type()
)
rdwrConfSyncLastConfFullSyncTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrConfSyncLastConfFullSyncTime.setStatus("mandatory")
_RdwrConfSyncNumOfFullSyncOperations_Type = Integer32
_RdwrConfSyncNumOfFullSyncOperations_Object = MibScalar
rdwrConfSyncNumOfFullSyncOperations = _RdwrConfSyncNumOfFullSyncOperations_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 161, 1, 8),
    _RdwrConfSyncNumOfFullSyncOperations_Type()
)
rdwrConfSyncNumOfFullSyncOperations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrConfSyncNumOfFullSyncOperations.setStatus("mandatory")
_RdwrConfSyncNumOfSyncOperations_Type = Integer32
_RdwrConfSyncNumOfSyncOperations_Object = MibScalar
rdwrConfSyncNumOfSyncOperations = _RdwrConfSyncNumOfSyncOperations_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 161, 1, 9),
    _RdwrConfSyncNumOfSyncOperations_Type()
)
rdwrConfSyncNumOfSyncOperations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrConfSyncNumOfSyncOperations.setStatus("mandatory")
_RdwrConfSyncNumOfFailedSyncAttempts_Type = Integer32
_RdwrConfSyncNumOfFailedSyncAttempts_Object = MibScalar
rdwrConfSyncNumOfFailedSyncAttempts = _RdwrConfSyncNumOfFailedSyncAttempts_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 161, 1, 10),
    _RdwrConfSyncNumOfFailedSyncAttempts_Type()
)
rdwrConfSyncNumOfFailedSyncAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrConfSyncNumOfFailedSyncAttempts.setStatus("mandatory")
_RdwrConfSyncPeerConfigVersion_Type = Integer32
_RdwrConfSyncPeerConfigVersion_Object = MibScalar
rdwrConfSyncPeerConfigVersion = _RdwrConfSyncPeerConfigVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 161, 1, 11),
    _RdwrConfSyncPeerConfigVersion_Type()
)
rdwrConfSyncPeerConfigVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrConfSyncPeerConfigVersion.setStatus("mandatory")
_RdwrConfSyncConfigTimestamp_Type = Unsigned32
_RdwrConfSyncConfigTimestamp_Object = MibScalar
rdwrConfSyncConfigTimestamp = _RdwrConfSyncConfigTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 161, 1, 12),
    _RdwrConfSyncConfigTimestamp_Type()
)
rdwrConfSyncConfigTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrConfSyncConfigTimestamp.setStatus("mandatory")


class _RdwrConfSyncResetStatistics_Type(Integer32):
    """Custom type rdwrConfSyncResetStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_RdwrConfSyncResetStatistics_Type.__name__ = "Integer32"
_RdwrConfSyncResetStatistics_Object = MibScalar
rdwrConfSyncResetStatistics = _RdwrConfSyncResetStatistics_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 161, 1, 13),
    _RdwrConfSyncResetStatistics_Type()
)
rdwrConfSyncResetStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrConfSyncResetStatistics.setStatus("mandatory")
_RdwrConfSyncShouldReboot_Type = TruthValue
_RdwrConfSyncShouldReboot_Object = MibScalar
rdwrConfSyncShouldReboot = _RdwrConfSyncShouldReboot_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 161, 1, 14),
    _RdwrConfSyncShouldReboot_Type()
)
rdwrConfSyncShouldReboot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrConfSyncShouldReboot.setStatus("mandatory")
_RdwrConfSyncNumOfConnects_Type = Integer32
_RdwrConfSyncNumOfConnects_Object = MibScalar
rdwrConfSyncNumOfConnects = _RdwrConfSyncNumOfConnects_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 161, 1, 15),
    _RdwrConfSyncNumOfConnects_Type()
)
rdwrConfSyncNumOfConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrConfSyncNumOfConnects.setStatus("mandatory")
_RdwrConfSyncNumOfDisconnects_Type = Integer32
_RdwrConfSyncNumOfDisconnects_Object = MibScalar
rdwrConfSyncNumOfDisconnects = _RdwrConfSyncNumOfDisconnects_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 161, 1, 16),
    _RdwrConfSyncNumOfDisconnects_Type()
)
rdwrConfSyncNumOfDisconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrConfSyncNumOfDisconnects.setStatus("mandatory")
_RdwrConfSyncIPString_Type = OctetString
_RdwrConfSyncIPString_Object = MibScalar
rdwrConfSyncIPString = _RdwrConfSyncIPString_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 161, 1, 18),
    _RdwrConfSyncIPString_Type()
)
rdwrConfSyncIPString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrConfSyncIPString.setStatus("mandatory")
_RdwrConfSyncPeerIPString_Type = OctetString
_RdwrConfSyncPeerIPString_Object = MibScalar
rdwrConfSyncPeerIPString = _RdwrConfSyncPeerIPString_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 161, 1, 19),
    _RdwrConfSyncPeerIPString_Type()
)
rdwrConfSyncPeerIPString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrConfSyncPeerIPString.setStatus("mandatory")
_RdwrConfigurationSyncConf_ObjectIdentity = ObjectIdentity
rdwrConfigurationSyncConf = _RdwrConfigurationSyncConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 161, 2)
)


class _RdwrConfSyncMode_Type(Integer32):
    """Custom type rdwrConfSyncMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2),
          ("disabled", 3))
    )


_RdwrConfSyncMode_Type.__name__ = "Integer32"
_RdwrConfSyncMode_Object = MibScalar
rdwrConfSyncMode = _RdwrConfSyncMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 161, 2, 1),
    _RdwrConfSyncMode_Type()
)
rdwrConfSyncMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrConfSyncMode.setStatus("mandatory")


class _RdwrConfSyncRetryTimeout_Type(Integer32):
    """Custom type rdwrConfSyncRetryTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_RdwrConfSyncRetryTimeout_Type.__name__ = "Integer32"
_RdwrConfSyncRetryTimeout_Object = MibScalar
rdwrConfSyncRetryTimeout = _RdwrConfSyncRetryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 161, 2, 2),
    _RdwrConfSyncRetryTimeout_Type()
)
rdwrConfSyncRetryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrConfSyncRetryTimeout.setStatus("mandatory")


class _RdwrConfSyncKeepAlivePeriod_Type(Integer32):
    """Custom type rdwrConfSyncKeepAlivePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 600),
    )


_RdwrConfSyncKeepAlivePeriod_Type.__name__ = "Integer32"
_RdwrConfSyncKeepAlivePeriod_Object = MibScalar
rdwrConfSyncKeepAlivePeriod = _RdwrConfSyncKeepAlivePeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 161, 2, 3),
    _RdwrConfSyncKeepAlivePeriod_Type()
)
rdwrConfSyncKeepAlivePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrConfSyncKeepAlivePeriod.setStatus("mandatory")


class _RdwrConfSyncRebootTimeout_Type(Integer32):
    """Custom type rdwrConfSyncRebootTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_RdwrConfSyncRebootTimeout_Type.__name__ = "Integer32"
_RdwrConfSyncRebootTimeout_Object = MibScalar
rdwrConfSyncRebootTimeout = _RdwrConfSyncRebootTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 161, 2, 4),
    _RdwrConfSyncRebootTimeout_Type()
)
rdwrConfSyncRebootTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrConfSyncRebootTimeout.setStatus("mandatory")


class _RdwrConfSyncPeerDiscTrapDelay_Type(Integer32):
    """Custom type rdwrConfSyncPeerDiscTrapDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_RdwrConfSyncPeerDiscTrapDelay_Type.__name__ = "Integer32"
_RdwrConfSyncPeerDiscTrapDelay_Object = MibScalar
rdwrConfSyncPeerDiscTrapDelay = _RdwrConfSyncPeerDiscTrapDelay_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 161, 2, 5),
    _RdwrConfSyncPeerDiscTrapDelay_Type()
)
rdwrConfSyncPeerDiscTrapDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrConfSyncPeerDiscTrapDelay.setStatus("mandatory")


class _RdwrConfSyncPeerResponseTimeout_Type(Integer32):
    """Custom type rdwrConfSyncPeerResponseTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_RdwrConfSyncPeerResponseTimeout_Type.__name__ = "Integer32"
_RdwrConfSyncPeerResponseTimeout_Object = MibScalar
rdwrConfSyncPeerResponseTimeout = _RdwrConfSyncPeerResponseTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 161, 2, 6),
    _RdwrConfSyncPeerResponseTimeout_Type()
)
rdwrConfSyncPeerResponseTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrConfSyncPeerResponseTimeout.setStatus("mandatory")


class _RdwrConfSyncMasterActivityTimeout_Type(Integer32):
    """Custom type rdwrConfSyncMasterActivityTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 600),
    )


_RdwrConfSyncMasterActivityTimeout_Type.__name__ = "Integer32"
_RdwrConfSyncMasterActivityTimeout_Object = MibScalar
rdwrConfSyncMasterActivityTimeout = _RdwrConfSyncMasterActivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 161, 2, 7),
    _RdwrConfSyncMasterActivityTimeout_Type()
)
rdwrConfSyncMasterActivityTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrConfSyncMasterActivityTimeout.setStatus("mandatory")
_RdwrConfSyncAllowRebootActiveDevice_Type = TruthValue
_RdwrConfSyncAllowRebootActiveDevice_Object = MibScalar
rdwrConfSyncAllowRebootActiveDevice = _RdwrConfSyncAllowRebootActiveDevice_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 161, 2, 8),
    _RdwrConfSyncAllowRebootActiveDevice_Type()
)
rdwrConfSyncAllowRebootActiveDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrConfSyncAllowRebootActiveDevice.setStatus("mandatory")


class _RdwrConfSyncRebootSlave_Type(Integer32):
    """Custom type rdwrConfSyncRebootSlave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reboot", 1)
    )


_RdwrConfSyncRebootSlave_Type.__name__ = "Integer32"
_RdwrConfSyncRebootSlave_Object = MibScalar
rdwrConfSyncRebootSlave = _RdwrConfSyncRebootSlave_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 161, 2, 9),
    _RdwrConfSyncRebootSlave_Type()
)
rdwrConfSyncRebootSlave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrConfSyncRebootSlave.setStatus("mandatory")
_RdwrConfSyncExcludeMgmtIP_Type = TruthValue
_RdwrConfSyncExcludeMgmtIP_Object = MibScalar
rdwrConfSyncExcludeMgmtIP = _RdwrConfSyncExcludeMgmtIP_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 161, 2, 10),
    _RdwrConfSyncExcludeMgmtIP_Type()
)
rdwrConfSyncExcludeMgmtIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrConfSyncExcludeMgmtIP.setStatus("mandatory")
_RdwrConfSyncExcludeMgmtCert_Type = TruthValue
_RdwrConfSyncExcludeMgmtCert_Object = MibScalar
rdwrConfSyncExcludeMgmtCert = _RdwrConfSyncExcludeMgmtCert_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 161, 2, 11),
    _RdwrConfSyncExcludeMgmtCert_Type()
)
rdwrConfSyncExcludeMgmtCert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrConfSyncExcludeMgmtCert.setStatus("mandatory")
_RdwrConfSyncDiscoverMngIPOnly_Type = TruthValue
_RdwrConfSyncDiscoverMngIPOnly_Object = MibScalar
rdwrConfSyncDiscoverMngIPOnly = _RdwrConfSyncDiscoverMngIPOnly_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 161, 2, 12),
    _RdwrConfSyncDiscoverMngIPOnly_Type()
)
rdwrConfSyncDiscoverMngIPOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrConfSyncDiscoverMngIPOnly.setStatus("obsolete")


class _RdwrConfSyncFullSyncDelay_Type(Integer32):
    """Custom type rdwrConfSyncFullSyncDelay based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_RdwrConfSyncFullSyncDelay_Type.__name__ = "Integer32"
_RdwrConfSyncFullSyncDelay_Object = MibScalar
rdwrConfSyncFullSyncDelay = _RdwrConfSyncFullSyncDelay_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 161, 2, 13),
    _RdwrConfSyncFullSyncDelay_Type()
)
rdwrConfSyncFullSyncDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrConfSyncFullSyncDelay.setStatus("mandatory")


class _RdwrConfSyncFullSyncMaxDelay_Type(Integer32):
    """Custom type rdwrConfSyncFullSyncMaxDelay based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_RdwrConfSyncFullSyncMaxDelay_Type.__name__ = "Integer32"
_RdwrConfSyncFullSyncMaxDelay_Object = MibScalar
rdwrConfSyncFullSyncMaxDelay = _RdwrConfSyncFullSyncMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 161, 2, 14),
    _RdwrConfSyncFullSyncMaxDelay_Type()
)
rdwrConfSyncFullSyncMaxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrConfSyncFullSyncMaxDelay.setStatus("mandatory")
_RdwrConfSyncCommunicationPassword_Type = OctetString
_RdwrConfSyncCommunicationPassword_Object = MibScalar
rdwrConfSyncCommunicationPassword = _RdwrConfSyncCommunicationPassword_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 161, 2, 15),
    _RdwrConfSyncCommunicationPassword_Type()
)
rdwrConfSyncCommunicationPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrConfSyncCommunicationPassword.setStatus("mandatory")
_RdwrConfSyncConnectionPreference_Type = OctetString
_RdwrConfSyncConnectionPreference_Object = MibScalar
rdwrConfSyncConnectionPreference = _RdwrConfSyncConnectionPreference_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 161, 2, 16),
    _RdwrConfSyncConnectionPreference_Type()
)
rdwrConfSyncConnectionPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrConfSyncConnectionPreference.setStatus("mandatory")
_RdwrConfSyncAlternateConnectionPreference_Type = OctetString
_RdwrConfSyncAlternateConnectionPreference_Object = MibScalar
rdwrConfSyncAlternateConnectionPreference = _RdwrConfSyncAlternateConnectionPreference_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 161, 2, 17),
    _RdwrConfSyncAlternateConnectionPreference_Type()
)
rdwrConfSyncAlternateConnectionPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrConfSyncAlternateConnectionPreference.setStatus("mandatory")


class _RdwrConfSyncReconnect_Type(Integer32):
    """Custom type rdwrConfSyncReconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reconnect", 1),
          ("doNothing", 2))
    )


_RdwrConfSyncReconnect_Type.__name__ = "Integer32"
_RdwrConfSyncReconnect_Object = MibScalar
rdwrConfSyncReconnect = _RdwrConfSyncReconnect_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 161, 2, 18),
    _RdwrConfSyncReconnect_Type()
)
rdwrConfSyncReconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdwrConfSyncReconnect.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CDE-MIB",
    **{"rdwrConfigurationSyncMonitor": rdwrConfigurationSyncMonitor,
       "rdwrConfSyncState": rdwrConfSyncState,
       "rdwrConfSyncIP": rdwrConfSyncIP,
       "rdwrConfSyncPeerIP": rdwrConfSyncPeerIP,
       "rdwrConfSyncPeerBaseMac": rdwrConfSyncPeerBaseMac,
       "rdwrConfSyncIncompatibilityReason": rdwrConfSyncIncompatibilityReason,
       "rdwrConfSyncLastConfSyncTime": rdwrConfSyncLastConfSyncTime,
       "rdwrConfSyncLastConfFullSyncTime": rdwrConfSyncLastConfFullSyncTime,
       "rdwrConfSyncNumOfFullSyncOperations": rdwrConfSyncNumOfFullSyncOperations,
       "rdwrConfSyncNumOfSyncOperations": rdwrConfSyncNumOfSyncOperations,
       "rdwrConfSyncNumOfFailedSyncAttempts": rdwrConfSyncNumOfFailedSyncAttempts,
       "rdwrConfSyncPeerConfigVersion": rdwrConfSyncPeerConfigVersion,
       "rdwrConfSyncConfigTimestamp": rdwrConfSyncConfigTimestamp,
       "rdwrConfSyncResetStatistics": rdwrConfSyncResetStatistics,
       "rdwrConfSyncShouldReboot": rdwrConfSyncShouldReboot,
       "rdwrConfSyncNumOfConnects": rdwrConfSyncNumOfConnects,
       "rdwrConfSyncNumOfDisconnects": rdwrConfSyncNumOfDisconnects,
       "rdwrConfSyncIPString": rdwrConfSyncIPString,
       "rdwrConfSyncPeerIPString": rdwrConfSyncPeerIPString,
       "rdwrConfigurationSyncConf": rdwrConfigurationSyncConf,
       "rdwrConfSyncMode": rdwrConfSyncMode,
       "rdwrConfSyncRetryTimeout": rdwrConfSyncRetryTimeout,
       "rdwrConfSyncKeepAlivePeriod": rdwrConfSyncKeepAlivePeriod,
       "rdwrConfSyncRebootTimeout": rdwrConfSyncRebootTimeout,
       "rdwrConfSyncPeerDiscTrapDelay": rdwrConfSyncPeerDiscTrapDelay,
       "rdwrConfSyncPeerResponseTimeout": rdwrConfSyncPeerResponseTimeout,
       "rdwrConfSyncMasterActivityTimeout": rdwrConfSyncMasterActivityTimeout,
       "rdwrConfSyncAllowRebootActiveDevice": rdwrConfSyncAllowRebootActiveDevice,
       "rdwrConfSyncRebootSlave": rdwrConfSyncRebootSlave,
       "rdwrConfSyncExcludeMgmtIP": rdwrConfSyncExcludeMgmtIP,
       "rdwrConfSyncExcludeMgmtCert": rdwrConfSyncExcludeMgmtCert,
       "rdwrConfSyncDiscoverMngIPOnly": rdwrConfSyncDiscoverMngIPOnly,
       "rdwrConfSyncFullSyncDelay": rdwrConfSyncFullSyncDelay,
       "rdwrConfSyncFullSyncMaxDelay": rdwrConfSyncFullSyncMaxDelay,
       "rdwrConfSyncCommunicationPassword": rdwrConfSyncCommunicationPassword,
       "rdwrConfSyncConnectionPreference": rdwrConfSyncConnectionPreference,
       "rdwrConfSyncAlternateConnectionPreference": rdwrConfSyncAlternateConnectionPreference,
       "rdwrConfSyncReconnect": rdwrConfSyncReconnect}
)
