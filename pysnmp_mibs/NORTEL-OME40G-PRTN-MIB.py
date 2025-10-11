# SNMP MIB module (NORTEL-OME40G-PRTN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nortel/NORTEL-OME40G-PRTN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:17:20 2025
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(nnOme40G,) = mibBuilder.importSymbols(
    "NORTEL-OME40G-MIB",
    "nnOme40G")

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

nnOme40GProtection = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 3)
)
if mibBuilder.loadTexts:
    nnOme40GProtection.setRevisions(
        ("2007-02-02 00:00",
         "2008-02-07 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NnOme40Gotm3Protection_ObjectIdentity = ObjectIdentity
nnOme40Gotm3Protection = _NnOme40Gotm3Protection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 3, 1)
)
_NnOTM3protectionGroupTable_Object = MibTable
nnOTM3protectionGroupTable = _NnOTM3protectionGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    nnOTM3protectionGroupTable.setStatus("current")
_NnOTM3protectionGroupEntry_Object = MibTableRow
nnOTM3protectionGroupEntry = _NnOTM3protectionGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 3, 1, 1, 1)
)
nnOTM3protectionGroupEntry.setIndexNames(
    (0, "NORTEL-OME40G-PRTN-MIB", "workingIfIndex"),
    (0, "NORTEL-OME40G-PRTN-MIB", "protectionIfIndex"),
)
if mibBuilder.loadTexts:
    nnOTM3protectionGroupEntry.setStatus("current")
_WorkingIfIndex_Type = InterfaceIndex
_WorkingIfIndex_Object = MibTableColumn
workingIfIndex = _WorkingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 3, 1, 1, 1, 1),
    _WorkingIfIndex_Type()
)
workingIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    workingIfIndex.setStatus("current")
_ProtectionIfIndex_Type = InterfaceIndex
_ProtectionIfIndex_Object = MibTableColumn
protectionIfIndex = _ProtectionIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 3, 1, 1, 1, 2),
    _ProtectionIfIndex_Type()
)
protectionIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    protectionIfIndex.setStatus("current")
_PtRowStatus_Type = RowStatus
_PtRowStatus_Object = MibTableColumn
ptRowStatus = _PtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 3, 1, 1, 1, 3),
    _PtRowStatus_Type()
)
ptRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptRowStatus.setStatus("current")


class _ProtectionSwitchDir_Type(Integer32):
    """Custom type protectionSwitchDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 1),
          ("unidirectional", 2))
    )


_ProtectionSwitchDir_Type.__name__ = "Integer32"
_ProtectionSwitchDir_Object = MibTableColumn
protectionSwitchDir = _ProtectionSwitchDir_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 3, 1, 1, 1, 4),
    _ProtectionSwitchDir_Type()
)
protectionSwitchDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protectionSwitchDir.setStatus("current")


class _ProtectionScheme_Type(Integer32):
    """Custom type protectionScheme based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("one-plus-one", 1)
    )


_ProtectionScheme_Type.__name__ = "Integer32"
_ProtectionScheme_Object = MibTableColumn
protectionScheme = _ProtectionScheme_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 3, 1, 1, 1, 5),
    _ProtectionScheme_Type()
)
protectionScheme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protectionScheme.setStatus("current")


class _WaitToRestore_Type(Integer32):
    """Custom type waitToRestore based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("one-minute", 1),
          ("two-minutes", 2),
          ("three-minutes", 3),
          ("four-minutes", 4),
          ("five-minutes", 5),
          ("six-minutes", 6),
          ("seven-minutes", 7),
          ("eight-minutes", 8),
          ("nine-minutes", 9),
          ("ten-minutes", 10),
          ("eleven-minutes", 11),
          ("twelve-minutes", 12))
    )


_WaitToRestore_Type.__name__ = "Integer32"
_WaitToRestore_Object = MibTableColumn
waitToRestore = _WaitToRestore_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 3, 1, 1, 1, 6),
    _WaitToRestore_Type()
)
waitToRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    waitToRestore.setStatus("current")


class _Revertive_Type(Integer32):
    """Custom type revertive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_Revertive_Type.__name__ = "Integer32"
_Revertive_Object = MibTableColumn
revertive = _Revertive_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 3, 1, 1, 1, 7),
    _Revertive_Type()
)
revertive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    revertive.setStatus("current")


class _RemoteStandardMode_Type(Integer32):
    """Custom type remoteStandardMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("otn-g-873-1", 1)
    )


_RemoteStandardMode_Type.__name__ = "Integer32"
_RemoteStandardMode_Object = MibTableColumn
remoteStandardMode = _RemoteStandardMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 3, 1, 1, 1, 8),
    _RemoteStandardMode_Type()
)
remoteStandardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteStandardMode.setStatus("current")


class _RouteDiversity_Type(Integer32):
    """Custom type routeDiversity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("off", 0)
    )


_RouteDiversity_Type.__name__ = "Integer32"
_RouteDiversity_Object = MibTableColumn
routeDiversity = _RouteDiversity_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 3, 1, 1, 1, 9),
    _RouteDiversity_Type()
)
routeDiversity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeDiversity.setStatus("current")
_NnOTM3protectionSwitchTable_Object = MibTable
nnOTM3protectionSwitchTable = _NnOTM3protectionSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 3, 1, 2)
)
if mibBuilder.loadTexts:
    nnOTM3protectionSwitchTable.setStatus("current")
_NnOTM3protectionSwitchEntry_Object = MibTableRow
nnOTM3protectionSwitchEntry = _NnOTM3protectionSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 3, 1, 2, 1)
)
nnOTM3protectionSwitchEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    nnOTM3protectionSwitchEntry.setStatus("current")


class _SwitchCommand_Type(Integer32):
    """Custom type switchCommand based on Integer32"""
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
        *(("man", 1),
          ("frcd", 2),
          ("lockout", 3),
          ("release", 4))
    )


_SwitchCommand_Type.__name__ = "Integer32"
_SwitchCommand_Object = MibTableColumn
switchCommand = _SwitchCommand_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 3, 1, 2, 1, 1),
    _SwitchCommand_Type()
)
switchCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchCommand.setStatus("current")


class _SwitchStatus_Type(Integer32):
    """Custom type switchStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("auto", 2),
          ("man", 3),
          ("frcd", 4),
          ("lockout", 5))
    )


_SwitchStatus_Type.__name__ = "Integer32"
_SwitchStatus_Object = MibTableColumn
switchStatus = _SwitchStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 3, 1, 2, 1, 2),
    _SwitchStatus_Type()
)
switchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchStatus.setStatus("current")


class _EndInitiatingSwitch_Type(Integer32):
    """Custom type endInitiatingSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("remote", 1),
          ("local", 2))
    )


_EndInitiatingSwitch_Type.__name__ = "Integer32"
_EndInitiatingSwitch_Object = MibTableColumn
endInitiatingSwitch = _EndInitiatingSwitch_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 3, 1, 2, 1, 3),
    _EndInitiatingSwitch_Type()
)
endInitiatingSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endInitiatingSwitch.setStatus("current")


class _ReasonForAutoSwitch_Type(Integer32):
    """Custom type reasonForAutoSwitch based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("sigok", 1),
          ("sf", 2),
          ("sd", 3),
          ("eber", 4),
          ("eqpfl", 5),
          ("facoos", 6),
          ("eqpoos", 7),
          ("osc", 8),
          ("wr", 9))
    )


_ReasonForAutoSwitch_Type.__name__ = "Integer32"
_ReasonForAutoSwitch_Object = MibTableColumn
reasonForAutoSwitch = _ReasonForAutoSwitch_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 3, 1, 2, 1, 4),
    _ReasonForAutoSwitch_Type()
)
reasonForAutoSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reasonForAutoSwitch.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NORTEL-OME40G-PRTN-MIB",
    **{"nnOme40GProtection": nnOme40GProtection,
       "nnOme40Gotm3Protection": nnOme40Gotm3Protection,
       "nnOTM3protectionGroupTable": nnOTM3protectionGroupTable,
       "nnOTM3protectionGroupEntry": nnOTM3protectionGroupEntry,
       "workingIfIndex": workingIfIndex,
       "protectionIfIndex": protectionIfIndex,
       "ptRowStatus": ptRowStatus,
       "protectionSwitchDir": protectionSwitchDir,
       "protectionScheme": protectionScheme,
       "waitToRestore": waitToRestore,
       "revertive": revertive,
       "remoteStandardMode": remoteStandardMode,
       "routeDiversity": routeDiversity,
       "nnOTM3protectionSwitchTable": nnOTM3protectionSwitchTable,
       "nnOTM3protectionSwitchEntry": nnOTM3protectionSwitchEntry,
       "switchCommand": switchCommand,
       "switchStatus": switchStatus,
       "endInitiatingSwitch": endInitiatingSwitch,
       "reasonForAutoSwitch": reasonForAutoSwitch}
)
