# SNMP MIB module (RAINBOW-RADIUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/alvarion/RAINBOW-RADIUS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:07:14 2025
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

(rainbow,) = mibBuilder.importSymbols(
    "RAINBOW-MIB",
    "rainbow")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

rbRadiusClient = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 150)
)
if mibBuilder.loadTexts:
    rbRadiusClient.setRevisions(
        ("2006-06-06 15:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbRadiusClientGeneralParams_ObjectIdentity = ObjectIdentity
rbRadiusClientGeneralParams = _RbRadiusClientGeneralParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 150, 1)
)


class _RbRadiusClientRetryInterval_Type(Integer32):
    """Custom type rbRadiusClientRetryInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_RbRadiusClientRetryInterval_Type.__name__ = "Integer32"
_RbRadiusClientRetryInterval_Object = MibScalar
rbRadiusClientRetryInterval = _RbRadiusClientRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 150, 1, 2),
    _RbRadiusClientRetryInterval_Type()
)
rbRadiusClientRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbRadiusClientRetryInterval.setStatus("current")


class _RbRadiusClientMaxNumOfRetries_Type(Integer32):
    """Custom type rbRadiusClientMaxNumOfRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_RbRadiusClientMaxNumOfRetries_Type.__name__ = "Integer32"
_RbRadiusClientMaxNumOfRetries_Object = MibScalar
rbRadiusClientMaxNumOfRetries = _RbRadiusClientMaxNumOfRetries_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 150, 1, 3),
    _RbRadiusClientMaxNumOfRetries_Type()
)
rbRadiusClientMaxNumOfRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbRadiusClientMaxNumOfRetries.setStatus("current")


class _RbRadiusClientKeepAliveTimeout_Type(Integer32):
    """Custom type rbRadiusClientKeepAliveTimeout based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 180),
    )


_RbRadiusClientKeepAliveTimeout_Type.__name__ = "Integer32"
_RbRadiusClientKeepAliveTimeout_Object = MibScalar
rbRadiusClientKeepAliveTimeout = _RbRadiusClientKeepAliveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 150, 1, 4),
    _RbRadiusClientKeepAliveTimeout_Type()
)
rbRadiusClientKeepAliveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbRadiusClientKeepAliveTimeout.setStatus("current")
_RbRadiusAuthServerTable_Object = MibTable
rbRadiusAuthServerTable = _RbRadiusAuthServerTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 150, 2)
)
if mibBuilder.loadTexts:
    rbRadiusAuthServerTable.setStatus("current")
_RbRadiusAuthServerEntry_Object = MibTableRow
rbRadiusAuthServerEntry = _RbRadiusAuthServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 150, 2, 1)
)
rbRadiusAuthServerEntry.setIndexNames(
    (0, "RAINBOW-RADIUS-MIB", "rbRadiusAuthServerAddress"),
)
if mibBuilder.loadTexts:
    rbRadiusAuthServerEntry.setStatus("current")
_RbRadiusAuthServerAddress_Type = IpAddress
_RbRadiusAuthServerAddress_Object = MibTableColumn
rbRadiusAuthServerAddress = _RbRadiusAuthServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 150, 2, 1, 1),
    _RbRadiusAuthServerAddress_Type()
)
rbRadiusAuthServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbRadiusAuthServerAddress.setStatus("current")
_RbRadiusAuthServerRowStatus_Type = RowStatus
_RbRadiusAuthServerRowStatus_Object = MibTableColumn
rbRadiusAuthServerRowStatus = _RbRadiusAuthServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 150, 2, 1, 2),
    _RbRadiusAuthServerRowStatus_Type()
)
rbRadiusAuthServerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbRadiusAuthServerRowStatus.setStatus("current")


class _RbRadiusAuthServerIndex_Type(Integer32):
    """Custom type rbRadiusAuthServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RbRadiusAuthServerIndex_Type.__name__ = "Integer32"
_RbRadiusAuthServerIndex_Object = MibTableColumn
rbRadiusAuthServerIndex = _RbRadiusAuthServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 150, 2, 1, 3),
    _RbRadiusAuthServerIndex_Type()
)
rbRadiusAuthServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbRadiusAuthServerIndex.setStatus("current")


class _RbRadiusAuthServerPortNumber_Type(Integer32):
    """Custom type rbRadiusAuthServerPortNumber based on Integer32"""
    defaultValue = 1812

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RbRadiusAuthServerPortNumber_Type.__name__ = "Integer32"
_RbRadiusAuthServerPortNumber_Object = MibTableColumn
rbRadiusAuthServerPortNumber = _RbRadiusAuthServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 150, 2, 1, 4),
    _RbRadiusAuthServerPortNumber_Type()
)
rbRadiusAuthServerPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbRadiusAuthServerPortNumber.setStatus("current")


class _RbRadiusAuthServerType_Type(Integer32):
    """Custom type rbRadiusAuthServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_RbRadiusAuthServerType_Type.__name__ = "Integer32"
_RbRadiusAuthServerType_Object = MibTableColumn
rbRadiusAuthServerType = _RbRadiusAuthServerType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 150, 2, 1, 5),
    _RbRadiusAuthServerType_Type()
)
rbRadiusAuthServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbRadiusAuthServerType.setStatus("current")


class _RbRadiusAuthServerStatus_Type(Integer32):
    """Custom type rbRadiusAuthServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2))
    )


_RbRadiusAuthServerStatus_Type.__name__ = "Integer32"
_RbRadiusAuthServerStatus_Object = MibTableColumn
rbRadiusAuthServerStatus = _RbRadiusAuthServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 150, 2, 1, 6),
    _RbRadiusAuthServerStatus_Type()
)
rbRadiusAuthServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbRadiusAuthServerStatus.setStatus("current")


class _RbRadiusAuthServerOperStatus_Type(Integer32):
    """Custom type rbRadiusAuthServerOperStatus based on Integer32"""
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


_RbRadiusAuthServerOperStatus_Type.__name__ = "Integer32"
_RbRadiusAuthServerOperStatus_Object = MibTableColumn
rbRadiusAuthServerOperStatus = _RbRadiusAuthServerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 150, 2, 1, 7),
    _RbRadiusAuthServerOperStatus_Type()
)
rbRadiusAuthServerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbRadiusAuthServerOperStatus.setStatus("current")


class _RbRadiusAuthServerResetCounters_Type(Integer32):
    """Custom type rbRadiusAuthServerResetCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 0),
          ("reset", 1))
    )


_RbRadiusAuthServerResetCounters_Type.__name__ = "Integer32"
_RbRadiusAuthServerResetCounters_Object = MibTableColumn
rbRadiusAuthServerResetCounters = _RbRadiusAuthServerResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 150, 2, 1, 8),
    _RbRadiusAuthServerResetCounters_Type()
)
rbRadiusAuthServerResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbRadiusAuthServerResetCounters.setStatus("current")
_RbRadiusAccountServerTable_Object = MibTable
rbRadiusAccountServerTable = _RbRadiusAccountServerTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 150, 3)
)
if mibBuilder.loadTexts:
    rbRadiusAccountServerTable.setStatus("current")
_RbRadiusAccountServerEntry_Object = MibTableRow
rbRadiusAccountServerEntry = _RbRadiusAccountServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 150, 3, 1)
)
rbRadiusAccountServerEntry.setIndexNames(
    (0, "RAINBOW-RADIUS-MIB", "rbRadiusAcctServerAddress"),
)
if mibBuilder.loadTexts:
    rbRadiusAccountServerEntry.setStatus("current")
_RbRadiusAcctServerAddress_Type = IpAddress
_RbRadiusAcctServerAddress_Object = MibTableColumn
rbRadiusAcctServerAddress = _RbRadiusAcctServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 150, 3, 1, 1),
    _RbRadiusAcctServerAddress_Type()
)
rbRadiusAcctServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbRadiusAcctServerAddress.setStatus("current")
_RbRadiusAcctServerRowStatus_Type = RowStatus
_RbRadiusAcctServerRowStatus_Object = MibTableColumn
rbRadiusAcctServerRowStatus = _RbRadiusAcctServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 150, 3, 1, 2),
    _RbRadiusAcctServerRowStatus_Type()
)
rbRadiusAcctServerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbRadiusAcctServerRowStatus.setStatus("current")


class _RbRadiusAcctServerIndex_Type(Integer32):
    """Custom type rbRadiusAcctServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RbRadiusAcctServerIndex_Type.__name__ = "Integer32"
_RbRadiusAcctServerIndex_Object = MibTableColumn
rbRadiusAcctServerIndex = _RbRadiusAcctServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 150, 3, 1, 3),
    _RbRadiusAcctServerIndex_Type()
)
rbRadiusAcctServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbRadiusAcctServerIndex.setStatus("current")


class _RbRadiusAcctServerPortNumber_Type(Integer32):
    """Custom type rbRadiusAcctServerPortNumber based on Integer32"""
    defaultValue = 1813

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RbRadiusAcctServerPortNumber_Type.__name__ = "Integer32"
_RbRadiusAcctServerPortNumber_Object = MibTableColumn
rbRadiusAcctServerPortNumber = _RbRadiusAcctServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 150, 3, 1, 4),
    _RbRadiusAcctServerPortNumber_Type()
)
rbRadiusAcctServerPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbRadiusAcctServerPortNumber.setStatus("current")


class _RbRadiusAcctServerType_Type(Integer32):
    """Custom type rbRadiusAcctServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_RbRadiusAcctServerType_Type.__name__ = "Integer32"
_RbRadiusAcctServerType_Object = MibTableColumn
rbRadiusAcctServerType = _RbRadiusAcctServerType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 150, 3, 1, 5),
    _RbRadiusAcctServerType_Type()
)
rbRadiusAcctServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbRadiusAcctServerType.setStatus("current")


class _RbRadiusAcctServerStatus_Type(Integer32):
    """Custom type rbRadiusAcctServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2))
    )


_RbRadiusAcctServerStatus_Type.__name__ = "Integer32"
_RbRadiusAcctServerStatus_Object = MibTableColumn
rbRadiusAcctServerStatus = _RbRadiusAcctServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 150, 3, 1, 6),
    _RbRadiusAcctServerStatus_Type()
)
rbRadiusAcctServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbRadiusAcctServerStatus.setStatus("current")


class _RbRadiusAcctServerOperStatus_Type(Integer32):
    """Custom type rbRadiusAcctServerOperStatus based on Integer32"""
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


_RbRadiusAcctServerOperStatus_Type.__name__ = "Integer32"
_RbRadiusAcctServerOperStatus_Object = MibTableColumn
rbRadiusAcctServerOperStatus = _RbRadiusAcctServerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 150, 3, 1, 7),
    _RbRadiusAcctServerOperStatus_Type()
)
rbRadiusAcctServerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbRadiusAcctServerOperStatus.setStatus("current")


class _RbRadiusAcctServerResetCounters_Type(Integer32):
    """Custom type rbRadiusAcctServerResetCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 0),
          ("reset", 1))
    )


_RbRadiusAcctServerResetCounters_Type.__name__ = "Integer32"
_RbRadiusAcctServerResetCounters_Object = MibTableColumn
rbRadiusAcctServerResetCounters = _RbRadiusAcctServerResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 150, 3, 1, 8),
    _RbRadiusAcctServerResetCounters_Type()
)
rbRadiusAcctServerResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbRadiusAcctServerResetCounters.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAINBOW-RADIUS-MIB",
    **{"rbRadiusClient": rbRadiusClient,
       "rbRadiusClientGeneralParams": rbRadiusClientGeneralParams,
       "rbRadiusClientRetryInterval": rbRadiusClientRetryInterval,
       "rbRadiusClientMaxNumOfRetries": rbRadiusClientMaxNumOfRetries,
       "rbRadiusClientKeepAliveTimeout": rbRadiusClientKeepAliveTimeout,
       "rbRadiusAuthServerTable": rbRadiusAuthServerTable,
       "rbRadiusAuthServerEntry": rbRadiusAuthServerEntry,
       "rbRadiusAuthServerAddress": rbRadiusAuthServerAddress,
       "rbRadiusAuthServerRowStatus": rbRadiusAuthServerRowStatus,
       "rbRadiusAuthServerIndex": rbRadiusAuthServerIndex,
       "rbRadiusAuthServerPortNumber": rbRadiusAuthServerPortNumber,
       "rbRadiusAuthServerType": rbRadiusAuthServerType,
       "rbRadiusAuthServerStatus": rbRadiusAuthServerStatus,
       "rbRadiusAuthServerOperStatus": rbRadiusAuthServerOperStatus,
       "rbRadiusAuthServerResetCounters": rbRadiusAuthServerResetCounters,
       "rbRadiusAccountServerTable": rbRadiusAccountServerTable,
       "rbRadiusAccountServerEntry": rbRadiusAccountServerEntry,
       "rbRadiusAcctServerAddress": rbRadiusAcctServerAddress,
       "rbRadiusAcctServerRowStatus": rbRadiusAcctServerRowStatus,
       "rbRadiusAcctServerIndex": rbRadiusAcctServerIndex,
       "rbRadiusAcctServerPortNumber": rbRadiusAcctServerPortNumber,
       "rbRadiusAcctServerType": rbRadiusAcctServerType,
       "rbRadiusAcctServerStatus": rbRadiusAcctServerStatus,
       "rbRadiusAcctServerOperStatus": rbRadiusAcctServerOperStatus,
       "rbRadiusAcctServerResetCounters": rbRadiusAcctServerResetCounters}
)
