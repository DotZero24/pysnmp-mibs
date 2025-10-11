# SNMP MIB module (ELTEX-MES-MIB-OBJECTS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-MIB-OBJECTS
# Produced by pysmi-1.6.2 at Fri Oct 10 19:51:00 2025
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

(eltMesIfMIBObjects,) = mibBuilder.importSymbols(
    "ELTEX-MES-IF-MIB",
    "eltMesIfMIBObjects")

(ifEntry,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifEntry")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltIfExtTable_Object = MibTable
eltIfExtTable = _EltIfExtTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 1, 31, 1, 1)
)
if mibBuilder.loadTexts:
    eltIfExtTable.setStatus("current")
_EltIfExtEntry_Object = MibTableRow
eltIfExtEntry = _EltIfExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 1, 31, 1, 1, 1)
)
if mibBuilder.loadTexts:
    eltIfExtEntry.setStatus("current")


class _EltIfLongDescr_Type(DisplayString):
    """Custom type eltIfLongDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_EltIfLongDescr_Type.__name__ = "DisplayString"
_EltIfLongDescr_Object = MibTableColumn
eltIfLongDescr = _EltIfLongDescr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 1, 31, 1, 1, 1, 1),
    _EltIfLongDescr_Type()
)
eltIfLongDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIfLongDescr.setStatus("current")


class _EltIfAdminMtu_Type(Integer32):
    """Custom type eltIfAdminMtu based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(128, 9000),
    )


_EltIfAdminMtu_Type.__name__ = "Integer32"
_EltIfAdminMtu_Object = MibTableColumn
eltIfAdminMtu = _EltIfAdminMtu_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 1, 31, 1, 1, 1, 2),
    _EltIfAdminMtu_Type()
)
eltIfAdminMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIfAdminMtu.setStatus("current")


class _EltIfUpDownTrapEnable_Type(Integer32):
    """Custom type eltIfUpDownTrapEnable based on Integer32"""
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


_EltIfUpDownTrapEnable_Type.__name__ = "Integer32"
_EltIfUpDownTrapEnable_Object = MibScalar
eltIfUpDownTrapEnable = _EltIfUpDownTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 1, 31, 1, 7),
    _EltIfUpDownTrapEnable_Type()
)
eltIfUpDownTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIfUpDownTrapEnable.setStatus("current")
ifEntry.registerAugmentions(
    ("ELTEX-MES-MIB-OBJECTS",
     "eltIfExtEntry")
)
eltIfExtEntry.setIndexNames(*ifEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-MIB-OBJECTS",
    **{"eltIfExtTable": eltIfExtTable,
       "eltIfExtEntry": eltIfExtEntry,
       "eltIfLongDescr": eltIfLongDescr,
       "eltIfAdminMtu": eltIfAdminMtu,
       "eltIfUpDownTrapEnable": eltIfUpDownTrapEnable}
)
