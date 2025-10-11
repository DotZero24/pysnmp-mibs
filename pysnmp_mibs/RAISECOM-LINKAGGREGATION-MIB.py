# SNMP MIB module (RAISECOM-LINKAGGREGATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-LINKAGGREGATION-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:37:33 2025
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

(dot3adAggPortIndex,) = mibBuilder.importSymbols(
    "IEEE8023-LAG-MIB",
    "dot3adAggPortIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(EnableVar,
 PortList) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar",
    "PortList")


# MODULE-IDENTITY

rcLinkAggregation = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 6)
)
if mibBuilder.loadTexts:
    rcLinkAggregation.setRevisions(
        ("1991-03-31 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _RcLinkAggregationStatus_Type(EnableVar):
    """Custom type rcLinkAggregationStatus based on EnableVar"""
    defaultValue = 1


_RcLinkAggregationStatus_Type.__name__ = "EnableVar"
_RcLinkAggregationStatus_Object = MibScalar
rcLinkAggregationStatus = _RcLinkAggregationStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 6, 1),
    _RcLinkAggregationStatus_Type()
)
rcLinkAggregationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcLinkAggregationStatus.setStatus("current")


class _RcLinkAggregationLoadSharingMode_Type(Integer32):
    """Custom type rcLinkAggregationLoadSharingMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("srcMAC", 1),
          ("destMAC", 2),
          ("srcXORDestMAC", 3),
          ("srcIP", 4),
          ("destIP", 5),
          ("srcXORDestIP", 6))
    )


_RcLinkAggregationLoadSharingMode_Type.__name__ = "Integer32"
_RcLinkAggregationLoadSharingMode_Object = MibScalar
rcLinkAggregationLoadSharingMode = _RcLinkAggregationLoadSharingMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 6, 2),
    _RcLinkAggregationLoadSharingMode_Type()
)
rcLinkAggregationLoadSharingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcLinkAggregationLoadSharingMode.setStatus("current")


class _RcLinkAggregationTicketGenerationAlgorithm_Type(Integer32):
    """Custom type rcLinkAggregationTicketGenerationAlgorithm based on Integer32"""
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


_RcLinkAggregationTicketGenerationAlgorithm_Type.__name__ = "Integer32"
_RcLinkAggregationTicketGenerationAlgorithm_Object = MibScalar
rcLinkAggregationTicketGenerationAlgorithm = _RcLinkAggregationTicketGenerationAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 6, 3),
    _RcLinkAggregationTicketGenerationAlgorithm_Type()
)
rcLinkAggregationTicketGenerationAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcLinkAggregationTicketGenerationAlgorithm.setStatus("current")


class _RcLinkAggregationMaxGroup_Type(Integer32):
    """Custom type rcLinkAggregationMaxGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_RcLinkAggregationMaxGroup_Type.__name__ = "Integer32"
_RcLinkAggregationMaxGroup_Object = MibScalar
rcLinkAggregationMaxGroup = _RcLinkAggregationMaxGroup_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 6, 4),
    _RcLinkAggregationMaxGroup_Type()
)
rcLinkAggregationMaxGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcLinkAggregationMaxGroup.setStatus("current")
_RcLinkAggregationGroupTable_Object = MibTable
rcLinkAggregationGroupTable = _RcLinkAggregationGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 6, 5)
)
if mibBuilder.loadTexts:
    rcLinkAggregationGroupTable.setStatus("current")
_RcLinkAggregationGroupEntry_Object = MibTableRow
rcLinkAggregationGroupEntry = _RcLinkAggregationGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 6, 5, 1)
)
rcLinkAggregationGroupEntry.setIndexNames(
    (0, "RAISECOM-LINKAGGREGATION-MIB", "rcLinkAggregationGroupID"),
)
if mibBuilder.loadTexts:
    rcLinkAggregationGroupEntry.setStatus("current")


class _RcLinkAggregationGroupID_Type(Integer32):
    """Custom type rcLinkAggregationGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RcLinkAggregationGroupID_Type.__name__ = "Integer32"
_RcLinkAggregationGroupID_Object = MibTableColumn
rcLinkAggregationGroupID = _RcLinkAggregationGroupID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 6, 5, 1, 1),
    _RcLinkAggregationGroupID_Type()
)
rcLinkAggregationGroupID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcLinkAggregationGroupID.setStatus("current")
_RcLinkAggregationGroupSettingPorts_Type = PortList
_RcLinkAggregationGroupSettingPorts_Object = MibTableColumn
rcLinkAggregationGroupSettingPorts = _RcLinkAggregationGroupSettingPorts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 6, 5, 1, 2),
    _RcLinkAggregationGroupSettingPorts_Type()
)
rcLinkAggregationGroupSettingPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcLinkAggregationGroupSettingPorts.setStatus("current")
_RcLinkAggregationGroupCurrentPorts_Type = PortList
_RcLinkAggregationGroupCurrentPorts_Object = MibTableColumn
rcLinkAggregationGroupCurrentPorts = _RcLinkAggregationGroupCurrentPorts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 6, 5, 1, 3),
    _RcLinkAggregationGroupCurrentPorts_Type()
)
rcLinkAggregationGroupCurrentPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcLinkAggregationGroupCurrentPorts.setStatus("current")


class _RcLinkAggregationGroupMode_Type(Integer32):
    """Custom type rcLinkAggregationGroupMode based on Integer32"""
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


_RcLinkAggregationGroupMode_Type.__name__ = "Integer32"
_RcLinkAggregationGroupMode_Object = MibTableColumn
rcLinkAggregationGroupMode = _RcLinkAggregationGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 6, 5, 1, 4),
    _RcLinkAggregationGroupMode_Type()
)
rcLinkAggregationGroupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcLinkAggregationGroupMode.setStatus("current")


class _RcLinkAggregationGroupMinLinks_Type(Integer32):
    """Custom type rcLinkAggregationGroupMinLinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_RcLinkAggregationGroupMinLinks_Type.__name__ = "Integer32"
_RcLinkAggregationGroupMinLinks_Object = MibTableColumn
rcLinkAggregationGroupMinLinks = _RcLinkAggregationGroupMinLinks_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 6, 5, 1, 5),
    _RcLinkAggregationGroupMinLinks_Type()
)
rcLinkAggregationGroupMinLinks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcLinkAggregationGroupMinLinks.setStatus("current")


class _RcLinkAggregationGroupMaxLinks_Type(Integer32):
    """Custom type rcLinkAggregationGroupMaxLinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_RcLinkAggregationGroupMaxLinks_Type.__name__ = "Integer32"
_RcLinkAggregationGroupMaxLinks_Object = MibTableColumn
rcLinkAggregationGroupMaxLinks = _RcLinkAggregationGroupMaxLinks_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 6, 5, 1, 6),
    _RcLinkAggregationGroupMaxLinks_Type()
)
rcLinkAggregationGroupMaxLinks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcLinkAggregationGroupMaxLinks.setStatus("current")
_RcLinkAggregationPortStatsClearTable_Object = MibTable
rcLinkAggregationPortStatsClearTable = _RcLinkAggregationPortStatsClearTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 6, 6)
)
if mibBuilder.loadTexts:
    rcLinkAggregationPortStatsClearTable.setStatus("current")
_RcLinkAggregationPortStatsClearEntry_Object = MibTableRow
rcLinkAggregationPortStatsClearEntry = _RcLinkAggregationPortStatsClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 6, 6, 1)
)
rcLinkAggregationPortStatsClearEntry.setIndexNames(
    (0, "IEEE8023-LAG-MIB", "dot3adAggPortIndex"),
)
if mibBuilder.loadTexts:
    rcLinkAggregationPortStatsClearEntry.setStatus("current")
_RcLinkAggregationPortStatsClear_Type = TruthValue
_RcLinkAggregationPortStatsClear_Object = MibTableColumn
rcLinkAggregationPortStatsClear = _RcLinkAggregationPortStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 6, 6, 1, 1),
    _RcLinkAggregationPortStatsClear_Type()
)
rcLinkAggregationPortStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcLinkAggregationPortStatsClear.setStatus("current")
_RcLinkAggregationPortLACPTable_Object = MibTable
rcLinkAggregationPortLACPTable = _RcLinkAggregationPortLACPTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 6, 7)
)
if mibBuilder.loadTexts:
    rcLinkAggregationPortLACPTable.setStatus("current")
_RcLinkAggregationPortLACPEntry_Object = MibTableRow
rcLinkAggregationPortLACPEntry = _RcLinkAggregationPortLACPEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 6, 7, 1)
)
rcLinkAggregationPortLACPEntry.setIndexNames(
    (0, "IEEE8023-LAG-MIB", "dot3adAggPortIndex"),
)
if mibBuilder.loadTexts:
    rcLinkAggregationPortLACPEntry.setStatus("current")


class _RcLinkAggregationPortLACPEnable_Type(EnableVar):
    """Custom type rcLinkAggregationPortLACPEnable based on EnableVar"""
    defaultValue = 2


_RcLinkAggregationPortLACPEnable_Type.__name__ = "EnableVar"
_RcLinkAggregationPortLACPEnable_Object = MibTableColumn
rcLinkAggregationPortLACPEnable = _RcLinkAggregationPortLACPEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 6, 7, 1, 1),
    _RcLinkAggregationPortLACPEnable_Type()
)
rcLinkAggregationPortLACPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcLinkAggregationPortLACPEnable.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-LINKAGGREGATION-MIB",
    **{"rcLinkAggregation": rcLinkAggregation,
       "rcLinkAggregationStatus": rcLinkAggregationStatus,
       "rcLinkAggregationLoadSharingMode": rcLinkAggregationLoadSharingMode,
       "rcLinkAggregationTicketGenerationAlgorithm": rcLinkAggregationTicketGenerationAlgorithm,
       "rcLinkAggregationMaxGroup": rcLinkAggregationMaxGroup,
       "rcLinkAggregationGroupTable": rcLinkAggregationGroupTable,
       "rcLinkAggregationGroupEntry": rcLinkAggregationGroupEntry,
       "rcLinkAggregationGroupID": rcLinkAggregationGroupID,
       "rcLinkAggregationGroupSettingPorts": rcLinkAggregationGroupSettingPorts,
       "rcLinkAggregationGroupCurrentPorts": rcLinkAggregationGroupCurrentPorts,
       "rcLinkAggregationGroupMode": rcLinkAggregationGroupMode,
       "rcLinkAggregationGroupMinLinks": rcLinkAggregationGroupMinLinks,
       "rcLinkAggregationGroupMaxLinks": rcLinkAggregationGroupMaxLinks,
       "rcLinkAggregationPortStatsClearTable": rcLinkAggregationPortStatsClearTable,
       "rcLinkAggregationPortStatsClearEntry": rcLinkAggregationPortStatsClearEntry,
       "rcLinkAggregationPortStatsClear": rcLinkAggregationPortStatsClear,
       "rcLinkAggregationPortLACPTable": rcLinkAggregationPortLACPTable,
       "rcLinkAggregationPortLACPEntry": rcLinkAggregationPortLACPEntry,
       "rcLinkAggregationPortLACPEnable": rcLinkAggregationPortLACPEnable}
)
