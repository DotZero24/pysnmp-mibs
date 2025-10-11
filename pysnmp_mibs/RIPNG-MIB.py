# SNMP MIB module (RIPNG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/RIPNG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:50:07 2025
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

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

swRIPngMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 83)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _SwRIPngGlobalState_Type(Integer32):
    """Custom type swRIPngGlobalState based on Integer32"""
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


_SwRIPngGlobalState_Type.__name__ = "Integer32"
_SwRIPngGlobalState_Object = MibScalar
swRIPngGlobalState = _SwRIPngGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 83, 1),
    _SwRIPngGlobalState_Type()
)
swRIPngGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRIPngGlobalState.setStatus("current")


class _SwRIPngMethod_Type(Integer32):
    """Custom type swRIPngMethod based on Integer32"""
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
        *(("no-horizon", 1),
          ("split-horizon", 2),
          ("poison-reverse", 3))
    )


_SwRIPngMethod_Type.__name__ = "Integer32"
_SwRIPngMethod_Object = MibScalar
swRIPngMethod = _SwRIPngMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 83, 2),
    _SwRIPngMethod_Type()
)
swRIPngMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRIPngMethod.setStatus("current")


class _SwRIPngUpdateTime_Type(Integer32):
    """Custom type swRIPngUpdateTime based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 65535),
    )


_SwRIPngUpdateTime_Type.__name__ = "Integer32"
_SwRIPngUpdateTime_Object = MibScalar
swRIPngUpdateTime = _SwRIPngUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 83, 3),
    _SwRIPngUpdateTime_Type()
)
swRIPngUpdateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRIPngUpdateTime.setStatus("current")


class _SwRIPngExpireTime_Type(Integer32):
    """Custom type swRIPngExpireTime based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwRIPngExpireTime_Type.__name__ = "Integer32"
_SwRIPngExpireTime_Object = MibScalar
swRIPngExpireTime = _SwRIPngExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 83, 4),
    _SwRIPngExpireTime_Type()
)
swRIPngExpireTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRIPngExpireTime.setStatus("current")


class _SwRIPngGarbageCollectionTime_Type(Integer32):
    """Custom type swRIPngGarbageCollectionTime based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwRIPngGarbageCollectionTime_Type.__name__ = "Integer32"
_SwRIPngGarbageCollectionTime_Object = MibScalar
swRIPngGarbageCollectionTime = _SwRIPngGarbageCollectionTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 83, 5),
    _SwRIPngGarbageCollectionTime_Type()
)
swRIPngGarbageCollectionTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRIPngGarbageCollectionTime.setStatus("current")
_SwRIPngIfTable_Object = MibTable
swRIPngIfTable = _SwRIPngIfTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 83, 6)
)
if mibBuilder.loadTexts:
    swRIPngIfTable.setStatus("current")
_SwRIPngIfEntry_Object = MibTableRow
swRIPngIfEntry = _SwRIPngIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 83, 6, 1)
)
swRIPngIfEntry.setIndexNames(
    (0, "RIPNG-MIB", "swRIPngIfName"),
)
if mibBuilder.loadTexts:
    swRIPngIfEntry.setStatus("current")
_SwRIPngIfName_Type = DisplayString
_SwRIPngIfName_Object = MibTableColumn
swRIPngIfName = _SwRIPngIfName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 83, 6, 1, 1),
    _SwRIPngIfName_Type()
)
swRIPngIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swRIPngIfName.setStatus("current")


class _SwRIPngIfState_Type(Integer32):
    """Custom type swRIPngIfState based on Integer32"""
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


_SwRIPngIfState_Type.__name__ = "Integer32"
_SwRIPngIfState_Object = MibTableColumn
swRIPngIfState = _SwRIPngIfState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 83, 6, 1, 2),
    _SwRIPngIfState_Type()
)
swRIPngIfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRIPngIfState.setStatus("current")


class _SwRIPngIfMetric_Type(Integer32):
    """Custom type swRIPngIfMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_SwRIPngIfMetric_Type.__name__ = "Integer32"
_SwRIPngIfMetric_Object = MibTableColumn
swRIPngIfMetric = _SwRIPngIfMetric_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 83, 6, 1, 3),
    _SwRIPngIfMetric_Type()
)
swRIPngIfMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRIPngIfMetric.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RIPNG-MIB",
    **{"swRIPngMIB": swRIPngMIB,
       "swRIPngGlobalState": swRIPngGlobalState,
       "swRIPngMethod": swRIPngMethod,
       "swRIPngUpdateTime": swRIPngUpdateTime,
       "swRIPngExpireTime": swRIPngExpireTime,
       "swRIPngGarbageCollectionTime": swRIPngGarbageCollectionTime,
       "swRIPngIfTable": swRIPngIfTable,
       "swRIPngIfEntry": swRIPngIfEntry,
       "swRIPngIfName": swRIPngIfName,
       "swRIPngIfState": swRIPngIfState,
       "swRIPngIfMetric": swRIPngIfMetric}
)
