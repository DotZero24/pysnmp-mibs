# SNMP MIB module (HMIT-SYS-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hirschmann/HMIT-SYS-IF-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:54:26 2025
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

(hmITSystem,) = mibBuilder.importSymbols(
    "HMIT-SMI",
    "hmITSystem")

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

hmITSysIfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 1, 11)
)
if mibBuilder.loadTexts:
    hmITSysIfMIB.setRevisions(
        ("2010-01-08 17:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HmITSysIfTable_Object = MibTable
hmITSysIfTable = _HmITSysIfTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 1, 11, 1)
)
if mibBuilder.loadTexts:
    hmITSysIfTable.setStatus("current")
_HmITSysIfEntry_Object = MibTableRow
hmITSysIfEntry = _HmITSysIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 1, 11, 1, 1)
)
hmITSysIfEntry.setIndexNames(
    (0, "HMIT-SYS-IF-MIB", "hmITSysIfIndex"),
)
if mibBuilder.loadTexts:
    hmITSysIfEntry.setStatus("current")


class _HmITSysIfIndex_Type(Integer32):
    """Custom type hmITSysIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HmITSysIfIndex_Type.__name__ = "Integer32"
_HmITSysIfIndex_Object = MibTableColumn
hmITSysIfIndex = _HmITSysIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 1, 11, 1, 1, 1),
    _HmITSysIfIndex_Type()
)
hmITSysIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmITSysIfIndex.setStatus("current")


class _HmITSysIfName_Type(DisplayString):
    """Custom type hmITSysIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 39),
    )


_HmITSysIfName_Type.__name__ = "DisplayString"
_HmITSysIfName_Object = MibTableColumn
hmITSysIfName = _HmITSysIfName_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 1, 11, 1, 1, 2),
    _HmITSysIfName_Type()
)
hmITSysIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmITSysIfName.setStatus("current")


class _HmITSysIfReliability_Type(Integer32):
    """Custom type hmITSysIfReliability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HmITSysIfReliability_Type.__name__ = "Integer32"
_HmITSysIfReliability_Object = MibTableColumn
hmITSysIfReliability = _HmITSysIfReliability_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 1, 11, 1, 1, 3),
    _HmITSysIfReliability_Type()
)
hmITSysIfReliability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmITSysIfReliability.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HMIT-SYS-IF-MIB",
    **{"hmITSysIfMIB": hmITSysIfMIB,
       "hmITSysIfTable": hmITSysIfTable,
       "hmITSysIfEntry": hmITSysIfEntry,
       "hmITSysIfIndex": hmITSysIfIndex,
       "hmITSysIfName": hmITSysIfName,
       "hmITSysIfReliability": hmITSysIfReliability}
)
