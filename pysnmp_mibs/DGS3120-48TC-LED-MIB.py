# SNMP MIB module (DGS3120-48TC-LED-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DGS3120-48TC-LED-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:51:41 2025
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

(dlink_Dgs3120Proj_DGS_3120_48TC_bx,) = mibBuilder.importSymbols(
    "SWDGS3120PRIMGMT-MIB",
    "dlink-Dgs3120Proj-DGS-3120-48TC-bx")


# MODULE-IDENTITY

swLedMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 5, 1, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwLedMIBObject_ObjectIdentity = ObjectIdentity
swLedMIBObject = _SwLedMIBObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 5, 1, 4, 1)
)
_SwLedInfoTable_Object = MibTable
swLedInfoTable = _SwLedInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 5, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    swLedInfoTable.setStatus("current")
_SwLedInfoEntry_Object = MibTableRow
swLedInfoEntry = _SwLedInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 5, 1, 4, 1, 1, 1)
)
swLedInfoEntry.setIndexNames(
    (0, "DGS3120-48TC-LED-MIB", "swLedInfoUnitId"),
)
if mibBuilder.loadTexts:
    swLedInfoEntry.setStatus("current")


class _SwLedInfoUnitId_Type(Integer32):
    """Custom type swLedInfoUnitId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 13),
    )


_SwLedInfoUnitId_Type.__name__ = "Integer32"
_SwLedInfoUnitId_Object = MibTableColumn
swLedInfoUnitId = _SwLedInfoUnitId_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 5, 1, 4, 1, 1, 1, 1),
    _SwLedInfoUnitId_Type()
)
swLedInfoUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swLedInfoUnitId.setStatus("current")
_SwLedInfoFrontPanelLedStatus_Type = OctetString
_SwLedInfoFrontPanelLedStatus_Object = MibTableColumn
swLedInfoFrontPanelLedStatus = _SwLedInfoFrontPanelLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 5, 1, 4, 1, 1, 1, 2),
    _SwLedInfoFrontPanelLedStatus_Type()
)
swLedInfoFrontPanelLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swLedInfoFrontPanelLedStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DGS3120-48TC-LED-MIB",
    **{"swLedMIB": swLedMIB,
       "swLedMIBObject": swLedMIBObject,
       "swLedInfoTable": swLedInfoTable,
       "swLedInfoEntry": swLedInfoEntry,
       "swLedInfoUnitId": swLedInfoUnitId,
       "swLedInfoFrontPanelLedStatus": swLedInfoFrontPanelLedStatus}
)
