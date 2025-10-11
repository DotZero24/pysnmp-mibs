# SNMP MIB module (OCNOS-VR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/ipinfusion/OCNOS-VR-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:34:19 2025
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

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(ipi,) = mibBuilder.importSymbols(
    "OCNOS-IPI-MODULE-MIB",
    "ipi")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(snmpTraps,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "snmpTraps")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

vr = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 36673, 2)
)
if mibBuilder.loadTexts:
    vr.setRevisions(
        ("2018-06-21 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VrVrTable_Object = MibTable
vrVrTable = _VrVrTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 2, 1)
)
if mibBuilder.loadTexts:
    vrVrTable.setStatus("current")
_VrVrEntry_Object = MibTableRow
vrVrEntry = _VrVrEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 2, 1, 1)
)
vrVrEntry.setIndexNames(
    (0, "OCNOS-VR-MIB", "vrVrId"),
)
if mibBuilder.loadTexts:
    vrVrEntry.setStatus("current")


class _VrVrId_Type(Unsigned32):
    """Custom type vrVrId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VrVrId_Type.__name__ = "Unsigned32"
_VrVrId_Object = MibTableColumn
vrVrId = _VrVrId_Object(
    (1, 3, 6, 1, 4, 1, 36673, 2, 1, 1, 1),
    _VrVrId_Type()
)
vrVrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrVrId.setStatus("current")
_VrName_Type = OctetString
_VrName_Object = MibTableColumn
vrName = _VrName_Object(
    (1, 3, 6, 1, 4, 1, 36673, 2, 1, 1, 2),
    _VrName_Type()
)
vrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OCNOS-VR-MIB",
    **{"vr": vr,
       "vrVrTable": vrVrTable,
       "vrVrEntry": vrVrEntry,
       "vrVrId": vrVrId,
       "vrName": vrName}
)
