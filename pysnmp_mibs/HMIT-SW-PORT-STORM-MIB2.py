# SNMP MIB module (HMIT-SW-PORT-STORM-MIB2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hirschmann/HMIT-SW-PORT-STORM-MIB2
# Produced by pysmi-1.6.2 at Fri Oct 10 18:54:01 2025
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

(hmITSwPortMIB,
 hmITSwPortmgrMIB) = mibBuilder.importSymbols(
    "HMIT-SW-PORT-MGR-MIB",
    "hmITSwPortMIB",
    "hmITSwPortmgrMIB")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HmITStormTable_Object = MibTable
hmITStormTable = _HmITStormTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 3)
)
if mibBuilder.loadTexts:
    hmITStormTable.setStatus("current")
_HmITStormEntry_Object = MibTableRow
hmITStormEntry = _HmITStormEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 3, 1)
)
hmITStormEntry.setIndexNames(
    (0, "HMIT-SW-PORT-STORM-MIB2", "hmITPortId"),
    (0, "HMIT-SW-PORT-STORM-MIB2", "hmITStormControlPktType"),
)
if mibBuilder.loadTexts:
    hmITStormEntry.setStatus("current")


class _HmITPortId_Type(Integer32):
    """Custom type hmITPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HmITPortId_Type.__name__ = "Integer32"
_HmITPortId_Object = MibTableColumn
hmITPortId = _HmITPortId_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 3, 1, 1),
    _HmITPortId_Type()
)
hmITPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmITPortId.setStatus("current")


class _HmITStormControlPktType_Type(Integer32):
    """Custom type hmITStormControlPktType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("broadcast", 2),
          ("multicast", 3))
    )


_HmITStormControlPktType_Type.__name__ = "Integer32"
_HmITStormControlPktType_Object = MibTableColumn
hmITStormControlPktType = _HmITStormControlPktType_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 3, 1, 2),
    _HmITStormControlPktType_Type()
)
hmITStormControlPktType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmITStormControlPktType.setStatus("current")


class _HmITStormControlLmtType_Type(Integer32):
    """Custom type hmITStormControlLmtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("kbps", 1),
          ("pps", 2),
          ("percent", 3),
          ("none", 4))
    )


_HmITStormControlLmtType_Type.__name__ = "Integer32"
_HmITStormControlLmtType_Object = MibTableColumn
hmITStormControlLmtType = _HmITStormControlLmtType_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 3, 1, 3),
    _HmITStormControlLmtType_Type()
)
hmITStormControlLmtType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmITStormControlLmtType.setStatus("current")


class _HmITStormControlParam_Type(Integer32):
    """Custom type hmITStormControlParam based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HmITStormControlParam_Type.__name__ = "Integer32"
_HmITStormControlParam_Object = MibTableColumn
hmITStormControlParam = _HmITStormControlParam_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 3, 1, 4),
    _HmITStormControlParam_Type()
)
hmITStormControlParam.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmITStormControlParam.setStatus("current")
_HmITStormRowStatus_Type = RowStatus
_HmITStormRowStatus_Object = MibTableColumn
hmITStormRowStatus = _HmITStormRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 3, 1, 10),
    _HmITStormRowStatus_Type()
)
hmITStormRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmITStormRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HMIT-SW-PORT-STORM-MIB2",
    **{"hmITStormTable": hmITStormTable,
       "hmITStormEntry": hmITStormEntry,
       "hmITPortId": hmITPortId,
       "hmITStormControlPktType": hmITStormControlPktType,
       "hmITStormControlLmtType": hmITStormControlLmtType,
       "hmITStormControlParam": hmITStormControlParam,
       "hmITStormRowStatus": hmITStormRowStatus}
)
