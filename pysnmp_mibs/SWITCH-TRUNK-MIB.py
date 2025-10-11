# SNMP MIB module (SWITCH-TRUNK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/SWITCH-TRUNK-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:35:45 2025
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

(iscomSwitch,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "iscomSwitch")

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

(EnableVar,
 PortList) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar",
    "PortList")


# MODULE-IDENTITY

rcTrunk = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 6)
)
if mibBuilder.loadTexts:
    rcTrunk.setRevisions(
        ("1991-03-31 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _RcTrunkEnable_Type(EnableVar):
    """Custom type rcTrunkEnable based on EnableVar"""
    defaultValue = 2


_RcTrunkEnable_Type.__name__ = "EnableVar"
_RcTrunkEnable_Object = MibScalar
rcTrunkEnable = _RcTrunkEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 6, 1),
    _RcTrunkEnable_Type()
)
rcTrunkEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcTrunkEnable.setStatus("current")


class _RcTrunkLoadingSharingMode_Type(Integer32):
    """Custom type rcTrunkLoadingSharingMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("srcMAC", 1),
          ("destMAC", 2),
          ("srcXORDestMAC", 3),
          ("srcIP", 4),
          ("destIP", 5),
          ("srcXORDestIP", 6),
          ("SrcXORDestMACXORSrcPort", 7))
    )


_RcTrunkLoadingSharingMode_Type.__name__ = "Integer32"
_RcTrunkLoadingSharingMode_Object = MibScalar
rcTrunkLoadingSharingMode = _RcTrunkLoadingSharingMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 6, 2),
    _RcTrunkLoadingSharingMode_Type()
)
rcTrunkLoadingSharingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcTrunkLoadingSharingMode.setStatus("current")


class _RcTrunkMaxGroup_Type(Integer32):
    """Custom type rcTrunkMaxGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_RcTrunkMaxGroup_Type.__name__ = "Integer32"
_RcTrunkMaxGroup_Object = MibScalar
rcTrunkMaxGroup = _RcTrunkMaxGroup_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 6, 3),
    _RcTrunkMaxGroup_Type()
)
rcTrunkMaxGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcTrunkMaxGroup.setStatus("current")


class _RcTrunkTicketGenerationAlgorithm_Type(Integer32):
    """Custom type rcTrunkTicketGenerationAlgorithm based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("direct-map", 1),
          ("crc", 2))
    )


_RcTrunkTicketGenerationAlgorithm_Type.__name__ = "Integer32"
_RcTrunkTicketGenerationAlgorithm_Object = MibScalar
rcTrunkTicketGenerationAlgorithm = _RcTrunkTicketGenerationAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 6, 4),
    _RcTrunkTicketGenerationAlgorithm_Type()
)
rcTrunkTicketGenerationAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcTrunkTicketGenerationAlgorithm.setStatus("current")
_RcTrunkGroupTable_Object = MibTable
rcTrunkGroupTable = _RcTrunkGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 6, 5)
)
if mibBuilder.loadTexts:
    rcTrunkGroupTable.setStatus("current")
_RcTrunkGroupEntry_Object = MibTableRow
rcTrunkGroupEntry = _RcTrunkGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 6, 5, 1)
)
rcTrunkGroupEntry.setIndexNames(
    (0, "SWITCH-TRUNK-MIB", "rcTrunkGroupID"),
)
if mibBuilder.loadTexts:
    rcTrunkGroupEntry.setStatus("current")


class _RcTrunkGroupID_Type(Integer32):
    """Custom type rcTrunkGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RcTrunkGroupID_Type.__name__ = "Integer32"
_RcTrunkGroupID_Object = MibTableColumn
rcTrunkGroupID = _RcTrunkGroupID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 6, 5, 1, 1),
    _RcTrunkGroupID_Type()
)
rcTrunkGroupID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcTrunkGroupID.setStatus("current")
_RcTrunkGroupSetPorts_Type = PortList
_RcTrunkGroupSetPorts_Object = MibTableColumn
rcTrunkGroupSetPorts = _RcTrunkGroupSetPorts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 6, 5, 1, 2),
    _RcTrunkGroupSetPorts_Type()
)
rcTrunkGroupSetPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcTrunkGroupSetPorts.setStatus("current")
_RcTrunkGroupCurrentPortInOperation_Type = PortList
_RcTrunkGroupCurrentPortInOperation_Object = MibTableColumn
rcTrunkGroupCurrentPortInOperation = _RcTrunkGroupCurrentPortInOperation_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 6, 5, 1, 3),
    _RcTrunkGroupCurrentPortInOperation_Type()
)
rcTrunkGroupCurrentPortInOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcTrunkGroupCurrentPortInOperation.setStatus("current")


class _RcTrunkGroupMode_Type(Integer32):
    """Custom type rcTrunkGroupMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("lacp-static", 2))
    )


_RcTrunkGroupMode_Type.__name__ = "Integer32"
_RcTrunkGroupMode_Object = MibTableColumn
rcTrunkGroupMode = _RcTrunkGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 6, 5, 1, 4),
    _RcTrunkGroupMode_Type()
)
rcTrunkGroupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcTrunkGroupMode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWITCH-TRUNK-MIB",
    **{"rcTrunk": rcTrunk,
       "rcTrunkEnable": rcTrunkEnable,
       "rcTrunkLoadingSharingMode": rcTrunkLoadingSharingMode,
       "rcTrunkMaxGroup": rcTrunkMaxGroup,
       "rcTrunkTicketGenerationAlgorithm": rcTrunkTicketGenerationAlgorithm,
       "rcTrunkGroupTable": rcTrunkGroupTable,
       "rcTrunkGroupEntry": rcTrunkGroupEntry,
       "rcTrunkGroupID": rcTrunkGroupID,
       "rcTrunkGroupSetPorts": rcTrunkGroupSetPorts,
       "rcTrunkGroupCurrentPortInOperation": rcTrunkGroupCurrentPortInOperation,
       "rcTrunkGroupMode": rcTrunkGroupMode}
)
