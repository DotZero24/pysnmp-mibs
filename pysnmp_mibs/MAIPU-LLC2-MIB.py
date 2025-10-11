# SNMP MIB module (MAIPU-LLC2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/maipu/MAIPU-LLC2-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:11:13 2025
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

(mpMgmt,) = mibBuilder.importSymbols(
    "MAIPU-SMI",
    "mpMgmt")

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

mpLlc2Mib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 23)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Llc2ConfTable_Object = MibTable
llc2ConfTable = _Llc2ConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 23, 1)
)
if mibBuilder.loadTexts:
    llc2ConfTable.setStatus("current")
_Llc2ConfEntry_Object = MibTableRow
llc2ConfEntry = _Llc2ConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 23, 1, 1)
)
llc2ConfEntry.setIndexNames(
    (0, "MAIPU-LLC2-MIB", "llc2IfIndex"),
)
if mibBuilder.loadTexts:
    llc2ConfEntry.setStatus("current")
_Llc2IfIndex_Type = Integer32
_Llc2IfIndex_Object = MibTableColumn
llc2IfIndex = _Llc2IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 23, 1, 1, 1),
    _Llc2IfIndex_Type()
)
llc2IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llc2IfIndex.setStatus("current")


class _Llc2Group_Type(Integer32):
    """Custom type llc2Group based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Llc2Group_Type.__name__ = "Integer32"
_Llc2Group_Object = MibTableColumn
llc2Group = _Llc2Group_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 23, 1, 1, 2),
    _Llc2Group_Type()
)
llc2Group.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    llc2Group.setStatus("current")
_Llc2Status_Type = RowStatus
_Llc2Status_Object = MibTableColumn
llc2Status = _Llc2Status_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 23, 1, 1, 3),
    _Llc2Status_Type()
)
llc2Status.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    llc2Status.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MAIPU-LLC2-MIB",
    **{"mpLlc2Mib": mpLlc2Mib,
       "llc2ConfTable": llc2ConfTable,
       "llc2ConfEntry": llc2ConfEntry,
       "llc2IfIndex": llc2IfIndex,
       "llc2Group": llc2Group,
       "llc2Status": llc2Status}
)
