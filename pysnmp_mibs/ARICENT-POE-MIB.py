# SNMP MIB module (ARICENT-POE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-POE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:42:16 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fspoe = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 103)
)
if mibBuilder.loadTexts:
    fspoe.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsPoeSystem_ObjectIdentity = ObjectIdentity
fsPoeSystem = _FsPoeSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 103, 1)
)


class _FsPoeGlobalAdminStatus_Type(Integer32):
    """Custom type fsPoeGlobalAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("shutdown", 2))
    )


_FsPoeGlobalAdminStatus_Type.__name__ = "Integer32"
_FsPoeGlobalAdminStatus_Object = MibScalar
fsPoeGlobalAdminStatus = _FsPoeGlobalAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 103, 1, 1),
    _FsPoeGlobalAdminStatus_Type()
)
fsPoeGlobalAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPoeGlobalAdminStatus.setStatus("current")
_FsPoeMacTable_Object = MibTable
fsPoeMacTable = _FsPoeMacTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 103, 1, 2)
)
if mibBuilder.loadTexts:
    fsPoeMacTable.setStatus("current")
_FsPoeMacEntry_Object = MibTableRow
fsPoeMacEntry = _FsPoeMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 103, 1, 2, 1)
)
fsPoeMacEntry.setIndexNames(
    (0, "ARICENT-POE-MIB", "fsPoePdMacAddress"),
)
if mibBuilder.loadTexts:
    fsPoeMacEntry.setStatus("current")
_FsPoePdMacAddress_Type = MacAddress
_FsPoePdMacAddress_Object = MibTableColumn
fsPoePdMacAddress = _FsPoePdMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 103, 1, 2, 1, 1),
    _FsPoePdMacAddress_Type()
)
fsPoePdMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPoePdMacAddress.setStatus("current")
_FsPoePdMacPort_Type = InterfaceIndex
_FsPoePdMacPort_Object = MibTableColumn
fsPoePdMacPort = _FsPoePdMacPort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 103, 1, 2, 1, 2),
    _FsPoePdMacPort_Type()
)
fsPoePdMacPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPoePdMacPort.setStatus("current")
_FsPoePdMacRowStatus_Type = RowStatus
_FsPoePdMacRowStatus_Object = MibTableColumn
fsPoePdMacRowStatus = _FsPoePdMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 103, 1, 2, 1, 3),
    _FsPoePdMacRowStatus_Type()
)
fsPoePdMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPoePdMacRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-POE-MIB",
    **{"fspoe": fspoe,
       "fsPoeSystem": fsPoeSystem,
       "fsPoeGlobalAdminStatus": fsPoeGlobalAdminStatus,
       "fsPoeMacTable": fsPoeMacTable,
       "fsPoeMacEntry": fsPoeMacEntry,
       "fsPoePdMacAddress": fsPoePdMacAddress,
       "fsPoePdMacPort": fsPoePdMacPort,
       "fsPoePdMacRowStatus": fsPoePdMacRowStatus}
)
