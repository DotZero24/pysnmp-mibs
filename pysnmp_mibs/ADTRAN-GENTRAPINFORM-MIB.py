# SNMP MIB module (ADTRAN-GENTRAPINFORM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENTRAPINFORM-MIB
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

(adIdentityShared,
 adShared) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentityShared",
    "adShared")

(EntryStatus,) = mibBuilder.importSymbols(
    "ADTRAN-TC",
    "EntryStatus")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

adTrapInformID = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 101601)
)
if mibBuilder.loadTexts:
    adTrapInformID.setRevisions(
        ("2015-11-04 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdTrapInform_ObjectIdentity = ObjectIdentity
adTrapInform = _AdTrapInform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 16)
)
_AdTrapInformScalars_ObjectIdentity = ObjectIdentity
adTrapInformScalars = _AdTrapInformScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 16, 1)
)


class _AdTrapEnable_Type(Integer32):
    """Custom type adTrapEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enableTraps", 1),
          ("disableTraps", 2))
    )


_AdTrapEnable_Type.__name__ = "Integer32"
_AdTrapEnable_Object = MibScalar
adTrapEnable = _AdTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 16, 1, 1),
    _AdTrapEnable_Type()
)
adTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTrapEnable.setStatus("current")
_AdTrapInformSeqNum_Type = Integer32
_AdTrapInformSeqNum_Object = MibScalar
adTrapInformSeqNum = _AdTrapInformSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 16, 1, 2),
    _AdTrapInformSeqNum_Type()
)
adTrapInformSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTrapInformSeqNum.setStatus("current")
_AdTrapHostEntriesUsed_Type = Integer32
_AdTrapHostEntriesUsed_Object = MibScalar
adTrapHostEntriesUsed = _AdTrapHostEntriesUsed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 16, 1, 3),
    _AdTrapHostEntriesUsed_Type()
)
adTrapHostEntriesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTrapHostEntriesUsed.setStatus("current")
_AdTrapHostEntryCapacity_Type = Integer32
_AdTrapHostEntryCapacity_Object = MibScalar
adTrapHostEntryCapacity = _AdTrapHostEntryCapacity_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 16, 1, 4),
    _AdTrapHostEntryCapacity_Type()
)
adTrapHostEntryCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTrapHostEntryCapacity.setStatus("current")
_AdTrapInformTables_ObjectIdentity = ObjectIdentity
adTrapInformTables = _AdTrapInformTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 16, 2)
)
_AdTrapInformHostTable_Object = MibTable
adTrapInformHostTable = _AdTrapInformHostTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 16, 2, 1)
)
if mibBuilder.loadTexts:
    adTrapInformHostTable.setStatus("current")
_AdTrapInformHostEntry_Object = MibTableRow
adTrapInformHostEntry = _AdTrapInformHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 16, 2, 1, 1)
)
adTrapInformHostEntry.setIndexNames(
    (0, "ADTRAN-GENTRAPINFORM-MIB", "adTrapInformHostIP"),
)
if mibBuilder.loadTexts:
    adTrapInformHostEntry.setStatus("current")
_AdTrapInformHostIP_Type = IpAddress
_AdTrapInformHostIP_Object = MibTableColumn
adTrapInformHostIP = _AdTrapInformHostIP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 16, 2, 1, 1, 1),
    _AdTrapInformHostIP_Type()
)
adTrapInformHostIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTrapInformHostIP.setStatus("current")


class _AdTrapInformConfirmation_Type(Integer32):
    """Custom type adTrapInformConfirmation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_AdTrapInformConfirmation_Type.__name__ = "Integer32"
_AdTrapInformConfirmation_Object = MibTableColumn
adTrapInformConfirmation = _AdTrapInformConfirmation_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 16, 2, 1, 1, 2),
    _AdTrapInformConfirmation_Type()
)
adTrapInformConfirmation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTrapInformConfirmation.setStatus("deprecated")


class _AdTrapInformSeqNumConfirmed_Type(Integer32):
    """Custom type adTrapInformSeqNumConfirmed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_AdTrapInformSeqNumConfirmed_Type.__name__ = "Integer32"
_AdTrapInformSeqNumConfirmed_Object = MibTableColumn
adTrapInformSeqNumConfirmed = _AdTrapInformSeqNumConfirmed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 16, 2, 1, 1, 3),
    _AdTrapInformSeqNumConfirmed_Type()
)
adTrapInformSeqNumConfirmed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTrapInformSeqNumConfirmed.setStatus("current")
_AdTrapInformSeqNumRequested_Type = Integer32
_AdTrapInformSeqNumRequested_Object = MibTableColumn
adTrapInformSeqNumRequested = _AdTrapInformSeqNumRequested_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 16, 2, 1, 1, 4),
    _AdTrapInformSeqNumRequested_Type()
)
adTrapInformSeqNumRequested.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTrapInformSeqNumRequested.setStatus("current")


class _AdTrapInformRetryLimit_Type(Integer32):
    """Custom type adTrapInformRetryLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_AdTrapInformRetryLimit_Type.__name__ = "Integer32"
_AdTrapInformRetryLimit_Object = MibTableColumn
adTrapInformRetryLimit = _AdTrapInformRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 16, 2, 1, 1, 5),
    _AdTrapInformRetryLimit_Type()
)
adTrapInformRetryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTrapInformRetryLimit.setStatus("current")


class _AdTrapInformInitialTimeout_Type(Integer32):
    """Custom type adTrapInformInitialTimeout based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AdTrapInformInitialTimeout_Type.__name__ = "Integer32"
_AdTrapInformInitialTimeout_Object = MibTableColumn
adTrapInformInitialTimeout = _AdTrapInformInitialTimeout_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 16, 2, 1, 1, 6),
    _AdTrapInformInitialTimeout_Type()
)
adTrapInformInitialTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTrapInformInitialTimeout.setStatus("current")
_AdTrapInformCache_Type = Integer32
_AdTrapInformCache_Object = MibTableColumn
adTrapInformCache = _AdTrapInformCache_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 16, 2, 1, 1, 7),
    _AdTrapInformCache_Type()
)
adTrapInformCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTrapInformCache.setStatus("current")
_AdTrapInformHostStatus_Type = EntryStatus
_AdTrapInformHostStatus_Object = MibTableColumn
adTrapInformHostStatus = _AdTrapInformHostStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 16, 2, 1, 1, 8),
    _AdTrapInformHostStatus_Type()
)
adTrapInformHostStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTrapInformHostStatus.setStatus("current")


class _AdTrapInformVersion_Type(Integer32):
    """Custom type adTrapInformVersion based on Integer32"""
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
        *(("snmpV1", 1),
          ("snmpV2", 2),
          ("snmpV3", 3))
    )


_AdTrapInformVersion_Type.__name__ = "Integer32"
_AdTrapInformVersion_Object = MibTableColumn
adTrapInformVersion = _AdTrapInformVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 16, 2, 1, 1, 9),
    _AdTrapInformVersion_Type()
)
adTrapInformVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTrapInformVersion.setStatus("current")
_AdTrapHostTable_Object = MibTable
adTrapHostTable = _AdTrapHostTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 16, 2, 2)
)
if mibBuilder.loadTexts:
    adTrapHostTable.setStatus("current")
_AdTrapHostEntry_Object = MibTableRow
adTrapHostEntry = _AdTrapHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 16, 2, 2, 1)
)
adTrapHostEntry.setIndexNames(
    (0, "ADTRAN-GENTRAPINFORM-MIB", "adTrapHostAddressType"),
    (0, "ADTRAN-GENTRAPINFORM-MIB", "adTrapHostAddressSize"),
    (0, "ADTRAN-GENTRAPINFORM-MIB", "adTrapHostAddress"),
)
if mibBuilder.loadTexts:
    adTrapHostEntry.setStatus("current")
_AdTrapHostAddressType_Type = InetAddressType
_AdTrapHostAddressType_Object = MibTableColumn
adTrapHostAddressType = _AdTrapHostAddressType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 16, 2, 2, 1, 1),
    _AdTrapHostAddressType_Type()
)
adTrapHostAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adTrapHostAddressType.setStatus("current")


class _AdTrapHostAddressSize_Type(Integer32):
    """Custom type adTrapHostAddressSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AdTrapHostAddressSize_Type.__name__ = "Integer32"
_AdTrapHostAddressSize_Object = MibTableColumn
adTrapHostAddressSize = _AdTrapHostAddressSize_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 16, 2, 2, 1, 2),
    _AdTrapHostAddressSize_Type()
)
adTrapHostAddressSize.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adTrapHostAddressSize.setStatus("current")
_AdTrapHostAddress_Type = InetAddress
_AdTrapHostAddress_Object = MibTableColumn
adTrapHostAddress = _AdTrapHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 16, 2, 2, 1, 3),
    _AdTrapHostAddress_Type()
)
adTrapHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adTrapHostAddress.setStatus("current")


class _AdTrapHostConfirmation_Type(Integer32):
    """Custom type adTrapHostConfirmation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_AdTrapHostConfirmation_Type.__name__ = "Integer32"
_AdTrapHostConfirmation_Object = MibTableColumn
adTrapHostConfirmation = _AdTrapHostConfirmation_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 16, 2, 2, 1, 4),
    _AdTrapHostConfirmation_Type()
)
adTrapHostConfirmation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adTrapHostConfirmation.setStatus("current")


class _AdTrapHostSeqNumConfirmed_Type(Integer32):
    """Custom type adTrapHostSeqNumConfirmed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_AdTrapHostSeqNumConfirmed_Type.__name__ = "Integer32"
_AdTrapHostSeqNumConfirmed_Object = MibTableColumn
adTrapHostSeqNumConfirmed = _AdTrapHostSeqNumConfirmed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 16, 2, 2, 1, 5),
    _AdTrapHostSeqNumConfirmed_Type()
)
adTrapHostSeqNumConfirmed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adTrapHostSeqNumConfirmed.setStatus("current")
_AdTrapHostSeqNumRequested_Type = Integer32
_AdTrapHostSeqNumRequested_Object = MibTableColumn
adTrapHostSeqNumRequested = _AdTrapHostSeqNumRequested_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 16, 2, 2, 1, 6),
    _AdTrapHostSeqNumRequested_Type()
)
adTrapHostSeqNumRequested.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adTrapHostSeqNumRequested.setStatus("current")


class _AdTrapHostRetryLimit_Type(Integer32):
    """Custom type adTrapHostRetryLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_AdTrapHostRetryLimit_Type.__name__ = "Integer32"
_AdTrapHostRetryLimit_Object = MibTableColumn
adTrapHostRetryLimit = _AdTrapHostRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 16, 2, 2, 1, 7),
    _AdTrapHostRetryLimit_Type()
)
adTrapHostRetryLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adTrapHostRetryLimit.setStatus("current")


class _AdTrapHostInitialTimeout_Type(Integer32):
    """Custom type adTrapHostInitialTimeout based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AdTrapHostInitialTimeout_Type.__name__ = "Integer32"
_AdTrapHostInitialTimeout_Object = MibTableColumn
adTrapHostInitialTimeout = _AdTrapHostInitialTimeout_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 16, 2, 2, 1, 8),
    _AdTrapHostInitialTimeout_Type()
)
adTrapHostInitialTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adTrapHostInitialTimeout.setStatus("current")
_AdTrapHostCache_Type = Integer32
_AdTrapHostCache_Object = MibTableColumn
adTrapHostCache = _AdTrapHostCache_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 16, 2, 2, 1, 9),
    _AdTrapHostCache_Type()
)
adTrapHostCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTrapHostCache.setStatus("current")


class _AdTrapHostVersion_Type(Integer32):
    """Custom type adTrapHostVersion based on Integer32"""
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
        *(("snmpV1", 1),
          ("snmpV2", 2),
          ("snmpV3", 3))
    )


_AdTrapHostVersion_Type.__name__ = "Integer32"
_AdTrapHostVersion_Object = MibTableColumn
adTrapHostVersion = _AdTrapHostVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 16, 2, 2, 1, 10),
    _AdTrapHostVersion_Type()
)
adTrapHostVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adTrapHostVersion.setStatus("current")
_AdTrapHostRowStatus_Type = RowStatus
_AdTrapHostRowStatus_Object = MibTableColumn
adTrapHostRowStatus = _AdTrapHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 16, 2, 2, 1, 11),
    _AdTrapHostRowStatus_Type()
)
adTrapHostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adTrapHostRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    **{"adTrapInform": adTrapInform,
       "adTrapInformScalars": adTrapInformScalars,
       "adTrapEnable": adTrapEnable,
       "adTrapInformSeqNum": adTrapInformSeqNum,
       "adTrapHostEntriesUsed": adTrapHostEntriesUsed,
       "adTrapHostEntryCapacity": adTrapHostEntryCapacity,
       "adTrapInformTables": adTrapInformTables,
       "adTrapInformHostTable": adTrapInformHostTable,
       "adTrapInformHostEntry": adTrapInformHostEntry,
       "adTrapInformHostIP": adTrapInformHostIP,
       "adTrapInformConfirmation": adTrapInformConfirmation,
       "adTrapInformSeqNumConfirmed": adTrapInformSeqNumConfirmed,
       "adTrapInformSeqNumRequested": adTrapInformSeqNumRequested,
       "adTrapInformRetryLimit": adTrapInformRetryLimit,
       "adTrapInformInitialTimeout": adTrapInformInitialTimeout,
       "adTrapInformCache": adTrapInformCache,
       "adTrapInformHostStatus": adTrapInformHostStatus,
       "adTrapInformVersion": adTrapInformVersion,
       "adTrapHostTable": adTrapHostTable,
       "adTrapHostEntry": adTrapHostEntry,
       "adTrapHostAddressType": adTrapHostAddressType,
       "adTrapHostAddressSize": adTrapHostAddressSize,
       "adTrapHostAddress": adTrapHostAddress,
       "adTrapHostConfirmation": adTrapHostConfirmation,
       "adTrapHostSeqNumConfirmed": adTrapHostSeqNumConfirmed,
       "adTrapHostSeqNumRequested": adTrapHostSeqNumRequested,
       "adTrapHostRetryLimit": adTrapHostRetryLimit,
       "adTrapHostInitialTimeout": adTrapHostInitialTimeout,
       "adTrapHostCache": adTrapHostCache,
       "adTrapHostVersion": adTrapHostVersion,
       "adTrapHostRowStatus": adTrapHostRowStatus,
       "adTrapInformID": adTrapInformID}
)
