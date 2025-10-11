# SNMP MIB module (FS-EEE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-EEE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:15:39 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

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

fsEEEMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 119)
)
if mibBuilder.loadTexts:
    fsEEEMIB.setRevisions(
        ("2012-10-16 00:00",
         "2012-10-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsEEEConfigMIBObjects_ObjectIdentity = ObjectIdentity
fsEEEConfigMIBObjects = _FsEEEConfigMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 119, 1)
)
_FsEEETable_Object = MibTable
fsEEETable = _FsEEETable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 119, 1, 1)
)
if mibBuilder.loadTexts:
    fsEEETable.setStatus("current")
_FsEEEEntry_Object = MibTableRow
fsEEEEntry = _FsEEEEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 119, 1, 1, 1)
)
fsEEEEntry.setIndexNames(
    (0, "FS-EEE-MIB", "fsEEEifIndex"),
)
if mibBuilder.loadTexts:
    fsEEEEntry.setStatus("current")


class _FsEEEifIndex_Type(Integer32):
    """Custom type fsEEEifIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsEEEifIndex_Type.__name__ = "Integer32"
_FsEEEifIndex_Object = MibTableColumn
fsEEEifIndex = _FsEEEifIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 119, 1, 1, 1, 1),
    _FsEEEifIndex_Type()
)
fsEEEifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEEEifIndex.setStatus("current")


class _FsEEEAdminEnable_Type(Integer32):
    """Custom type fsEEEAdminEnable based on Integer32"""
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


_FsEEEAdminEnable_Type.__name__ = "Integer32"
_FsEEEAdminEnable_Object = MibTableColumn
fsEEEAdminEnable = _FsEEEAdminEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 119, 1, 1, 1, 2),
    _FsEEEAdminEnable_Type()
)
fsEEEAdminEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEEEAdminEnable.setStatus("current")


class _FsEEEOperEnable_Type(Integer32):
    """Custom type fsEEEOperEnable based on Integer32"""
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


_FsEEEOperEnable_Type.__name__ = "Integer32"
_FsEEEOperEnable_Object = MibTableColumn
fsEEEOperEnable = _FsEEEOperEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 119, 1, 1, 1, 3),
    _FsEEEOperEnable_Type()
)
fsEEEOperEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEEEOperEnable.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-EEE-MIB",
    **{"fsEEEMIB": fsEEEMIB,
       "fsEEEConfigMIBObjects": fsEEEConfigMIBObjects,
       "fsEEETable": fsEEETable,
       "fsEEEEntry": fsEEEEntry,
       "fsEEEifIndex": fsEEEifIndex,
       "fsEEEAdminEnable": fsEEEAdminEnable,
       "fsEEEOperEnable": fsEEEOperEnable}
)
