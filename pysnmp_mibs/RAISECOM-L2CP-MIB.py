# SNMP MIB module (RAISECOM-L2CP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-L2CP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:36:45 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

(EnableVar,) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar")


# MODULE-IDENTITY

rcL2cp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 71)
)
if mibBuilder.loadTexts:
    rcL2cp.setRevisions(
        ("2012-05-25 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcL2cpGrobal_ObjectIdentity = ObjectIdentity
rcL2cpGrobal = _RcL2cpGrobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 71, 1)
)


class _RcL2cpEnable_Type(EnableVar):
    """Custom type rcL2cpEnable based on EnableVar"""
    defaultValue = 2


_RcL2cpEnable_Type.__name__ = "EnableVar"
_RcL2cpEnable_Object = MibScalar
rcL2cpEnable = _RcL2cpEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 71, 1, 1),
    _RcL2cpEnable_Type()
)
rcL2cpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcL2cpEnable.setStatus("current")
_RcL2cpMacAddress_Type = MacAddress
_RcL2cpMacAddress_Object = MibScalar
rcL2cpMacAddress = _RcL2cpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 71, 1, 2),
    _RcL2cpMacAddress_Type()
)
rcL2cpMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcL2cpMacAddress.setStatus("current")
_RcL2cpProfileTable_Object = MibTable
rcL2cpProfileTable = _RcL2cpProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 71, 2)
)
if mibBuilder.loadTexts:
    rcL2cpProfileTable.setStatus("current")
_RcL2cpProfileEntry_Object = MibTableRow
rcL2cpProfileEntry = _RcL2cpProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 71, 2, 1)
)
rcL2cpProfileEntry.setIndexNames(
    (0, "RAISECOM-L2CP-MIB", "rcL2cpProfileNumber"),
)
if mibBuilder.loadTexts:
    rcL2cpProfileEntry.setStatus("current")


class _RcL2cpProfileNumber_Type(Integer32):
    """Custom type rcL2cpProfileNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_RcL2cpProfileNumber_Type.__name__ = "Integer32"
_RcL2cpProfileNumber_Object = MibTableColumn
rcL2cpProfileNumber = _RcL2cpProfileNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 71, 2, 1, 1),
    _RcL2cpProfileNumber_Type()
)
rcL2cpProfileNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcL2cpProfileNumber.setStatus("current")


class _RcL2cpProfileDescription_Type(OctetString):
    """Custom type rcL2cpProfileDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RcL2cpProfileDescription_Type.__name__ = "OctetString"
_RcL2cpProfileDescription_Object = MibTableColumn
rcL2cpProfileDescription = _RcL2cpProfileDescription_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 71, 2, 1, 2),
    _RcL2cpProfileDescription_Type()
)
rcL2cpProfileDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcL2cpProfileDescription.setStatus("current")
_RcL2cpProfileRef_Type = Gauge32
_RcL2cpProfileRef_Object = MibTableColumn
rcL2cpProfileRef = _RcL2cpProfileRef_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 71, 2, 1, 3),
    _RcL2cpProfileRef_Type()
)
rcL2cpProfileRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcL2cpProfileRef.setStatus("current")
_RcL2cpProfileStatus_Type = RowStatus
_RcL2cpProfileStatus_Object = MibTableColumn
rcL2cpProfileStatus = _RcL2cpProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 71, 2, 1, 4),
    _RcL2cpProfileStatus_Type()
)
rcL2cpProfileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcL2cpProfileStatus.setStatus("current")
_RcL2cpProfileActionTable_Object = MibTable
rcL2cpProfileActionTable = _RcL2cpProfileActionTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 71, 3)
)
if mibBuilder.loadTexts:
    rcL2cpProfileActionTable.setStatus("current")
_RcL2cpProfileActionEntry_Object = MibTableRow
rcL2cpProfileActionEntry = _RcL2cpProfileActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 71, 3, 1)
)
rcL2cpProfileActionEntry.setIndexNames(
    (0, "RAISECOM-L2CP-MIB", "rcL2cpProfileActionProfileIndex"),
    (0, "RAISECOM-L2CP-MIB", "rcL2cpProfileActionProtocolIndex"),
)
if mibBuilder.loadTexts:
    rcL2cpProfileActionEntry.setStatus("current")


class _RcL2cpProfileActionProfileIndex_Type(Integer32):
    """Custom type rcL2cpProfileActionProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_RcL2cpProfileActionProfileIndex_Type.__name__ = "Integer32"
_RcL2cpProfileActionProfileIndex_Object = MibTableColumn
rcL2cpProfileActionProfileIndex = _RcL2cpProfileActionProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 71, 3, 1, 1),
    _RcL2cpProfileActionProfileIndex_Type()
)
rcL2cpProfileActionProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcL2cpProfileActionProfileIndex.setStatus("current")


class _RcL2cpProfileActionProtocolIndex_Type(Integer32):
    """Custom type rcL2cpProfileActionProtocolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("stp", 1),
          ("slow-protocol", 2),
          ("dot1x", 3),
          ("elmi", 4),
          ("lldp", 5),
          ("sisco", 6),
          ("daMac0180-C200-0004", 7),
          ("daMac0180-C200-0005", 8),
          ("daMac0180-C200-0006", 9),
          ("daMac0180-C200-0008", 10),
          ("daMac0180-C200-0009", 11),
          ("daMac0180-C200-000a", 12),
          ("daMac0180-C200-000b", 13),
          ("daMac0180-C200-000c", 14),
          ("daMac0180-C200-000d", 15),
          ("daMac0180-C200-000f", 16),
          ("daMac0180-C200-0020to2f", 17),
          ("lacp", 18),
          ("lamp", 19),
          ("link-oam", 20),
          ("esmc", 21))
    )


_RcL2cpProfileActionProtocolIndex_Type.__name__ = "Integer32"
_RcL2cpProfileActionProtocolIndex_Object = MibTableColumn
rcL2cpProfileActionProtocolIndex = _RcL2cpProfileActionProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 71, 3, 1, 2),
    _RcL2cpProfileActionProtocolIndex_Type()
)
rcL2cpProfileActionProtocolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcL2cpProfileActionProtocolIndex.setStatus("current")


class _RcL2cpProfileActionProtocolAction_Type(Integer32):
    """Custom type rcL2cpProfileActionProtocolAction based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("forward", 0),
          ("peer", 1),
          ("discard", 2),
          ("tunnel", 3),
          ("forward-statistics", 4))
    )


_RcL2cpProfileActionProtocolAction_Type.__name__ = "Integer32"
_RcL2cpProfileActionProtocolAction_Object = MibTableColumn
rcL2cpProfileActionProtocolAction = _RcL2cpProfileActionProtocolAction_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 71, 3, 1, 3),
    _RcL2cpProfileActionProtocolAction_Type()
)
rcL2cpProfileActionProtocolAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcL2cpProfileActionProtocolAction.setStatus("current")


class _RcL2cpProfileActionProtocolCos_Type(Integer32):
    """Custom type rcL2cpProfileActionProtocolCos based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_RcL2cpProfileActionProtocolCos_Type.__name__ = "Integer32"
_RcL2cpProfileActionProtocolCos_Object = MibTableColumn
rcL2cpProfileActionProtocolCos = _RcL2cpProfileActionProtocolCos_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 71, 3, 1, 4),
    _RcL2cpProfileActionProtocolCos_Type()
)
rcL2cpProfileActionProtocolCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcL2cpProfileActionProtocolCos.setStatus("current")
_RcL2cpPortCfgTable_Object = MibTable
rcL2cpPortCfgTable = _RcL2cpPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 71, 4)
)
if mibBuilder.loadTexts:
    rcL2cpPortCfgTable.setStatus("current")
_RcL2cpPortCfgEntry_Object = MibTableRow
rcL2cpPortCfgEntry = _RcL2cpPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 71, 4, 1)
)
rcL2cpPortCfgEntry.setIndexNames(
    (0, "RAISECOM-L2CP-MIB", "rcL2cpPortIndex"),
)
if mibBuilder.loadTexts:
    rcL2cpPortCfgEntry.setStatus("current")
_RcL2cpPortIndex_Type = InterfaceIndex
_RcL2cpPortIndex_Object = MibTableColumn
rcL2cpPortIndex = _RcL2cpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 71, 4, 1, 1),
    _RcL2cpPortIndex_Type()
)
rcL2cpPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcL2cpPortIndex.setStatus("current")


class _RcL2cpPortProfileID_Type(Integer32):
    """Custom type rcL2cpPortProfileID based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_RcL2cpPortProfileID_Type.__name__ = "Integer32"
_RcL2cpPortProfileID_Object = MibTableColumn
rcL2cpPortProfileID = _RcL2cpPortProfileID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 71, 4, 1, 2),
    _RcL2cpPortProfileID_Type()
)
rcL2cpPortProfileID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcL2cpPortProfileID.setStatus("current")


class _RcL2cpPortTerminal_Type(EnableVar):
    """Custom type rcL2cpPortTerminal based on EnableVar"""
    defaultValue = 2


_RcL2cpPortTerminal_Type.__name__ = "EnableVar"
_RcL2cpPortTerminal_Object = MibTableColumn
rcL2cpPortTerminal = _RcL2cpPortTerminal_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 71, 4, 1, 3),
    _RcL2cpPortTerminal_Type()
)
rcL2cpPortTerminal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcL2cpPortTerminal.setStatus("current")


class _RcL2cpPortClearStats_Type(EnableVar):
    """Custom type rcL2cpPortClearStats based on EnableVar"""
    defaultValue = 2


_RcL2cpPortClearStats_Type.__name__ = "EnableVar"
_RcL2cpPortClearStats_Object = MibTableColumn
rcL2cpPortClearStats = _RcL2cpPortClearStats_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 71, 4, 1, 4),
    _RcL2cpPortClearStats_Type()
)
rcL2cpPortClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcL2cpPortClearStats.setStatus("current")
_RcL2cpStatsTable_Object = MibTable
rcL2cpStatsTable = _RcL2cpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 71, 5)
)
if mibBuilder.loadTexts:
    rcL2cpStatsTable.setStatus("current")
_RcL2cpStatsEntry_Object = MibTableRow
rcL2cpStatsEntry = _RcL2cpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 71, 5, 1)
)
rcL2cpStatsEntry.setIndexNames(
    (0, "RAISECOM-L2CP-MIB", "rcL2cpStatsPortIndex"),
    (0, "RAISECOM-L2CP-MIB", "rcL2cpStatsProtocolIndex"),
)
if mibBuilder.loadTexts:
    rcL2cpStatsEntry.setStatus("current")
_RcL2cpStatsPortIndex_Type = InterfaceIndex
_RcL2cpStatsPortIndex_Object = MibTableColumn
rcL2cpStatsPortIndex = _RcL2cpStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 71, 5, 1, 1),
    _RcL2cpStatsPortIndex_Type()
)
rcL2cpStatsPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcL2cpStatsPortIndex.setStatus("current")


class _RcL2cpStatsProtocolIndex_Type(Integer32):
    """Custom type rcL2cpStatsProtocolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("stp", 1),
          ("slow-protocol", 2),
          ("dot1x", 3),
          ("elmi", 4),
          ("lldp", 5),
          ("sisco", 6),
          ("daMac0180-C200-0004", 7),
          ("daMac0180-C200-0005", 8),
          ("daMac0180-C200-0006", 9),
          ("daMac0180-C200-0008", 10),
          ("daMac0180-C200-0009", 11),
          ("daMac0180-C200-000a", 12),
          ("daMac0180-C200-000b", 13),
          ("daMac0180-C200-000c", 14),
          ("daMac0180-C200-000d", 15),
          ("daMac0180-C200-000f", 16),
          ("daMac0180-C200-0020to2f", 17))
    )


_RcL2cpStatsProtocolIndex_Type.__name__ = "Integer32"
_RcL2cpStatsProtocolIndex_Object = MibTableColumn
rcL2cpStatsProtocolIndex = _RcL2cpStatsProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 71, 5, 1, 2),
    _RcL2cpStatsProtocolIndex_Type()
)
rcL2cpStatsProtocolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcL2cpStatsProtocolIndex.setStatus("current")
_RcL2cpStatsProtocolStats_Type = Counter32
_RcL2cpStatsProtocolStats_Object = MibTableColumn
rcL2cpStatsProtocolStats = _RcL2cpStatsProtocolStats_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 71, 5, 1, 3),
    _RcL2cpStatsProtocolStats_Type()
)
rcL2cpStatsProtocolStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcL2cpStatsProtocolStats.setStatus("current")
_RcL2cpPortVlanCfgTable_Object = MibTable
rcL2cpPortVlanCfgTable = _RcL2cpPortVlanCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 71, 6)
)
if mibBuilder.loadTexts:
    rcL2cpPortVlanCfgTable.setStatus("current")
_RcL2cpPortVlanCfgEntry_Object = MibTableRow
rcL2cpPortVlanCfgEntry = _RcL2cpPortVlanCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 71, 6, 1)
)
rcL2cpPortVlanCfgEntry.setIndexNames(
    (0, "RAISECOM-L2CP-MIB", "rcL2cpPortVlanCfgPortIndex"),
    (0, "RAISECOM-L2CP-MIB", "rcL2cpPortVlanCfgVlanIndex"),
)
if mibBuilder.loadTexts:
    rcL2cpPortVlanCfgEntry.setStatus("current")
_RcL2cpPortVlanCfgPortIndex_Type = InterfaceIndex
_RcL2cpPortVlanCfgPortIndex_Object = MibTableColumn
rcL2cpPortVlanCfgPortIndex = _RcL2cpPortVlanCfgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 71, 6, 1, 1),
    _RcL2cpPortVlanCfgPortIndex_Type()
)
rcL2cpPortVlanCfgPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcL2cpPortVlanCfgPortIndex.setStatus("current")


class _RcL2cpPortVlanCfgVlanIndex_Type(Integer32):
    """Custom type rcL2cpPortVlanCfgVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RcL2cpPortVlanCfgVlanIndex_Type.__name__ = "Integer32"
_RcL2cpPortVlanCfgVlanIndex_Object = MibTableColumn
rcL2cpPortVlanCfgVlanIndex = _RcL2cpPortVlanCfgVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 71, 6, 1, 2),
    _RcL2cpPortVlanCfgVlanIndex_Type()
)
rcL2cpPortVlanCfgVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcL2cpPortVlanCfgVlanIndex.setStatus("current")


class _RcL2cpPortVlanCfgL2cpProcess_Type(Integer32):
    """Custom type rcL2cpPortVlanCfgL2cpProcess based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("forward", 0),
          ("peer", 1))
    )


_RcL2cpPortVlanCfgL2cpProcess_Type.__name__ = "Integer32"
_RcL2cpPortVlanCfgL2cpProcess_Object = MibTableColumn
rcL2cpPortVlanCfgL2cpProcess = _RcL2cpPortVlanCfgL2cpProcess_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 71, 6, 1, 3),
    _RcL2cpPortVlanCfgL2cpProcess_Type()
)
rcL2cpPortVlanCfgL2cpProcess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcL2cpPortVlanCfgL2cpProcess.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-L2CP-MIB",
    **{"rcL2cp": rcL2cp,
       "rcL2cpGrobal": rcL2cpGrobal,
       "rcL2cpEnable": rcL2cpEnable,
       "rcL2cpMacAddress": rcL2cpMacAddress,
       "rcL2cpProfileTable": rcL2cpProfileTable,
       "rcL2cpProfileEntry": rcL2cpProfileEntry,
       "rcL2cpProfileNumber": rcL2cpProfileNumber,
       "rcL2cpProfileDescription": rcL2cpProfileDescription,
       "rcL2cpProfileRef": rcL2cpProfileRef,
       "rcL2cpProfileStatus": rcL2cpProfileStatus,
       "rcL2cpProfileActionTable": rcL2cpProfileActionTable,
       "rcL2cpProfileActionEntry": rcL2cpProfileActionEntry,
       "rcL2cpProfileActionProfileIndex": rcL2cpProfileActionProfileIndex,
       "rcL2cpProfileActionProtocolIndex": rcL2cpProfileActionProtocolIndex,
       "rcL2cpProfileActionProtocolAction": rcL2cpProfileActionProtocolAction,
       "rcL2cpProfileActionProtocolCos": rcL2cpProfileActionProtocolCos,
       "rcL2cpPortCfgTable": rcL2cpPortCfgTable,
       "rcL2cpPortCfgEntry": rcL2cpPortCfgEntry,
       "rcL2cpPortIndex": rcL2cpPortIndex,
       "rcL2cpPortProfileID": rcL2cpPortProfileID,
       "rcL2cpPortTerminal": rcL2cpPortTerminal,
       "rcL2cpPortClearStats": rcL2cpPortClearStats,
       "rcL2cpStatsTable": rcL2cpStatsTable,
       "rcL2cpStatsEntry": rcL2cpStatsEntry,
       "rcL2cpStatsPortIndex": rcL2cpStatsPortIndex,
       "rcL2cpStatsProtocolIndex": rcL2cpStatsProtocolIndex,
       "rcL2cpStatsProtocolStats": rcL2cpStatsProtocolStats,
       "rcL2cpPortVlanCfgTable": rcL2cpPortVlanCfgTable,
       "rcL2cpPortVlanCfgEntry": rcL2cpPortVlanCfgEntry,
       "rcL2cpPortVlanCfgPortIndex": rcL2cpPortVlanCfgPortIndex,
       "rcL2cpPortVlanCfgVlanIndex": rcL2cpPortVlanCfgVlanIndex,
       "rcL2cpPortVlanCfgL2cpProcess": rcL2cpPortVlanCfgL2cpProcess}
)
