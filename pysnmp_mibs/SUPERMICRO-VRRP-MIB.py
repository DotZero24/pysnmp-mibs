# SNMP MIB module (SUPERMICRO-VRRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-VRRP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:01:55 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(vrrpOperEntry,) = mibBuilder.importSymbols(
    "VRRP-MIB",
    "vrrpOperEntry")


# MODULE-IDENTITY

fsvrrp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 153)
)
if mibBuilder.loadTexts:
    fsvrrp.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsVrrpSystem_ObjectIdentity = ObjectIdentity
fsVrrpSystem = _FsVrrpSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 153, 1)
)


class _FsVrrpStatus_Type(Integer32):
    """Custom type fsVrrpStatus based on Integer32"""
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


_FsVrrpStatus_Type.__name__ = "Integer32"
_FsVrrpStatus_Object = MibScalar
fsVrrpStatus = _FsVrrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 153, 1, 1),
    _FsVrrpStatus_Type()
)
fsVrrpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVrrpStatus.setStatus("current")
_FsVrrpMaxOperEntries_Type = Integer32
_FsVrrpMaxOperEntries_Object = MibScalar
fsVrrpMaxOperEntries = _FsVrrpMaxOperEntries_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 153, 1, 2),
    _FsVrrpMaxOperEntries_Type()
)
fsVrrpMaxOperEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVrrpMaxOperEntries.setStatus("current")
_FsVrrpOperTable_Object = MibTable
fsVrrpOperTable = _FsVrrpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 153, 1, 3)
)
if mibBuilder.loadTexts:
    fsVrrpOperTable.setStatus("current")
_FsVrrpOperEntry_Object = MibTableRow
fsVrrpOperEntry = _FsVrrpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 153, 1, 3, 1)
)
if mibBuilder.loadTexts:
    fsVrrpOperEntry.setStatus("current")


class _FsVrrpAdminPriority_Type(Integer32):
    """Custom type fsVrrpAdminPriority based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_FsVrrpAdminPriority_Type.__name__ = "Integer32"
_FsVrrpAdminPriority_Object = MibTableColumn
fsVrrpAdminPriority = _FsVrrpAdminPriority_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 153, 1, 3, 1, 1),
    _FsVrrpAdminPriority_Type()
)
fsVrrpAdminPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVrrpAdminPriority.setStatus("current")


class _FsVrrpOperAdvertisementIntervalInMsec_Type(Integer32):
    """Custom type fsVrrpOperAdvertisementIntervalInMsec based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 255000),
    )


_FsVrrpOperAdvertisementIntervalInMsec_Type.__name__ = "Integer32"
_FsVrrpOperAdvertisementIntervalInMsec_Object = MibTableColumn
fsVrrpOperAdvertisementIntervalInMsec = _FsVrrpOperAdvertisementIntervalInMsec_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 153, 1, 3, 1, 2),
    _FsVrrpOperAdvertisementIntervalInMsec_Type()
)
fsVrrpOperAdvertisementIntervalInMsec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsVrrpOperAdvertisementIntervalInMsec.setStatus("current")
if mibBuilder.loadTexts:
    fsVrrpOperAdvertisementIntervalInMsec.setUnits("milli seconds")


class _FsvrrpOperPingEnable_Type(Integer32):
    """Custom type fsvrrpOperPingEnable based on Integer32"""
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


_FsvrrpOperPingEnable_Type.__name__ = "Integer32"
_FsvrrpOperPingEnable_Object = MibTableColumn
fsvrrpOperPingEnable = _FsvrrpOperPingEnable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 153, 1, 3, 1, 3),
    _FsvrrpOperPingEnable_Type()
)
fsvrrpOperPingEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsvrrpOperPingEnable.setStatus("current")


class _FsVrrpAuthDeprecate_Type(Integer32):
    """Custom type fsVrrpAuthDeprecate based on Integer32"""
    defaultValue = 1

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


_FsVrrpAuthDeprecate_Type.__name__ = "Integer32"
_FsVrrpAuthDeprecate_Object = MibScalar
fsVrrpAuthDeprecate = _FsVrrpAuthDeprecate_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 153, 1, 4),
    _FsVrrpAuthDeprecate_Type()
)
fsVrrpAuthDeprecate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVrrpAuthDeprecate.setStatus("current")


class _FsVrrpTraceOption_Type(Integer32):
    """Custom type fsVrrpTraceOption based on Integer32"""
    defaultValue = 0


_FsVrrpTraceOption_Type.__name__ = "Integer32"
_FsVrrpTraceOption_Object = MibScalar
fsVrrpTraceOption = _FsVrrpTraceOption_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 153, 1, 5),
    _FsVrrpTraceOption_Type()
)
fsVrrpTraceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVrrpTraceOption.setStatus("current")
vrrpOperEntry.registerAugmentions(
    ("SUPERMICRO-VRRP-MIB",
     "fsVrrpOperEntry")
)
fsVrrpOperEntry.setIndexNames(*vrrpOperEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-VRRP-MIB",
    **{"fsvrrp": fsvrrp,
       "fsVrrpSystem": fsVrrpSystem,
       "fsVrrpStatus": fsVrrpStatus,
       "fsVrrpMaxOperEntries": fsVrrpMaxOperEntries,
       "fsVrrpOperTable": fsVrrpOperTable,
       "fsVrrpOperEntry": fsVrrpOperEntry,
       "fsVrrpAdminPriority": fsVrrpAdminPriority,
       "fsVrrpOperAdvertisementIntervalInMsec": fsVrrpOperAdvertisementIntervalInMsec,
       "fsvrrpOperPingEnable": fsvrrpOperPingEnable,
       "fsVrrpAuthDeprecate": fsVrrpAuthDeprecate,
       "fsVrrpTraceOption": fsVrrpTraceOption}
)
