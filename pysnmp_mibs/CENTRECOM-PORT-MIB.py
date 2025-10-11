# SNMP MIB module (CENTRECOM-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/allied-old/CENTRECOM-PORT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:12:17 2025
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

(extSwitchMIB,) = mibBuilder.importSymbols(
    "CENTRECOM-MIB",
    "extSwitchMIB")

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

atiPort = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AtiPortLoadshareTable_Object = MibTable
atiPortLoadshareTable = _AtiPortLoadshareTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 6, 1)
)
if mibBuilder.loadTexts:
    atiPortLoadshareTable.setStatus("mandatory")
_AtiPortLoadshareEntry_Object = MibTableRow
atiPortLoadshareEntry = _AtiPortLoadshareEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 6, 1, 1)
)
atiPortLoadshareEntry.setIndexNames(
    (0, "CENTRECOM-PORT-MIB", "atiPortLoadshareMasterIfIndex"),
    (0, "CENTRECOM-PORT-MIB", "atiPortLoadshareSlaveIfIndex"),
)
if mibBuilder.loadTexts:
    atiPortLoadshareEntry.setStatus("mandatory")
_AtiPortLoadshareMasterIfIndex_Type = Integer32
_AtiPortLoadshareMasterIfIndex_Object = MibTableColumn
atiPortLoadshareMasterIfIndex = _AtiPortLoadshareMasterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 6, 1, 1, 1),
    _AtiPortLoadshareMasterIfIndex_Type()
)
atiPortLoadshareMasterIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiPortLoadshareMasterIfIndex.setStatus("mandatory")
_AtiPortLoadshareSlaveIfIndex_Type = Integer32
_AtiPortLoadshareSlaveIfIndex_Object = MibTableColumn
atiPortLoadshareSlaveIfIndex = _AtiPortLoadshareSlaveIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 6, 1, 1, 2),
    _AtiPortLoadshareSlaveIfIndex_Type()
)
atiPortLoadshareSlaveIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiPortLoadshareSlaveIfIndex.setStatus("mandatory")


class _AtiPortLoadshareGrouping_Type(Integer32):
    """Custom type atiPortLoadshareGrouping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("pair", 2),
          ("quad", 4))
    )


_AtiPortLoadshareGrouping_Type.__name__ = "Integer32"
_AtiPortLoadshareGrouping_Object = MibTableColumn
atiPortLoadshareGrouping = _AtiPortLoadshareGrouping_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 6, 1, 1, 3),
    _AtiPortLoadshareGrouping_Type()
)
atiPortLoadshareGrouping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiPortLoadshareGrouping.setStatus("mandatory")
_AtiPortLoadshareStatus_Type = RowStatus
_AtiPortLoadshareStatus_Object = MibTableColumn
atiPortLoadshareStatus = _AtiPortLoadshareStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 6, 1, 1, 4),
    _AtiPortLoadshareStatus_Type()
)
atiPortLoadshareStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiPortLoadshareStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CENTRECOM-PORT-MIB",
    **{"atiPort": atiPort,
       "atiPortLoadshareTable": atiPortLoadshareTable,
       "atiPortLoadshareEntry": atiPortLoadshareEntry,
       "atiPortLoadshareMasterIfIndex": atiPortLoadshareMasterIfIndex,
       "atiPortLoadshareSlaveIfIndex": atiPortLoadshareSlaveIfIndex,
       "atiPortLoadshareGrouping": atiPortLoadshareGrouping,
       "atiPortLoadshareStatus": atiPortLoadshareStatus}
)
