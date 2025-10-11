# SNMP MIB module (MPFW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/maipu/MPFW-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:11:00 2025
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
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 ObjectName,
 ObjectSyntax,
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
    "ObjectName",
    "ObjectSyntax",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

mpFwMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 35)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MpFwIfTable_Object = MibTable
mpFwIfTable = _MpFwIfTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 35, 10)
)
if mibBuilder.loadTexts:
    mpFwIfTable.setStatus("current")
_MpFwIfEntry_Object = MibTableRow
mpFwIfEntry = _MpFwIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 35, 10, 1)
)
mpFwIfEntry.setIndexNames(
    (0, "MPFW-MIB", "fwIfName"),
    (0, "MPFW-MIB", "fwIfDirection"),
)
if mibBuilder.loadTexts:
    mpFwIfEntry.setStatus("current")


class _FwIfName_Type(DisplayString):
    """Custom type fwIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 39),
    )


_FwIfName_Type.__name__ = "DisplayString"
_FwIfName_Object = MibTableColumn
fwIfName = _FwIfName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 35, 10, 1, 1),
    _FwIfName_Type()
)
fwIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fwIfName.setStatus("current")


class _FwIfDirection_Type(Integer32):
    """Custom type fwIfDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_FwIfDirection_Type.__name__ = "Integer32"
_FwIfDirection_Object = MibTableColumn
fwIfDirection = _FwIfDirection_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 35, 10, 1, 2),
    _FwIfDirection_Type()
)
fwIfDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fwIfDirection.setStatus("current")


class _FwIfGrpName_Type(DisplayString):
    """Custom type fwIfGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_FwIfGrpName_Type.__name__ = "DisplayString"
_FwIfGrpName_Object = MibTableColumn
fwIfGrpName = _FwIfGrpName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 35, 10, 1, 3),
    _FwIfGrpName_Type()
)
fwIfGrpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwIfGrpName.setStatus("current")
_FwIfRowStatus_Type = RowStatus
_FwIfRowStatus_Object = MibTableColumn
fwIfRowStatus = _FwIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 35, 10, 1, 4),
    _FwIfRowStatus_Type()
)
fwIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fwIfRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPFW-MIB",
    **{"mpFwMib": mpFwMib,
       "mpFwIfTable": mpFwIfTable,
       "mpFwIfEntry": mpFwIfEntry,
       "fwIfName": fwIfName,
       "fwIfDirection": fwIfDirection,
       "fwIfGrpName": fwIfGrpName,
       "fwIfRowStatus": fwIfRowStatus}
)
