# SNMP MIB module (LUM-IFOTDR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-IFOTDR-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:50 2025
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

(lumIfOtdrMIB,
 lumModules) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumIfOtdrMIB",
    "lumModules")

(AdminStatusWithNA,
 CommandString,
 DisplayStringWithNA,
 EnabledDisabledWithNA,
 FaultStatusWithNA,
 MgmtNameString,
 OperStatusWithNA,
 PortNumber,
 SlotNumber,
 SubrackNumber,
 Unsigned32WithNA) = mibBuilder.importSymbols(
    "LUM-TC",
    "AdminStatusWithNA",
    "CommandString",
    "DisplayStringWithNA",
    "EnabledDisabledWithNA",
    "FaultStatusWithNA",
    "MgmtNameString",
    "OperStatusWithNA",
    "PortNumber",
    "SlotNumber",
    "SubrackNumber",
    "Unsigned32WithNA")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ifOtdrMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 72)
)
if mibBuilder.loadTexts:
    ifOtdrMIBModule.setRevisions(
        ("2018-06-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LumIfOtdrConfs_ObjectIdentity = ObjectIdentity
lumIfOtdrConfs = _LumIfOtdrConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 72, 1)
)
_LumIfOtdrGroups_ObjectIdentity = ObjectIdentity
lumIfOtdrGroups = _LumIfOtdrGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 72, 1, 1)
)
_LumIfOtdrCompl_ObjectIdentity = ObjectIdentity
lumIfOtdrCompl = _LumIfOtdrCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 72, 1, 2)
)
_LumIfOtdrMIBObjects_ObjectIdentity = ObjectIdentity
lumIfOtdrMIBObjects = _LumIfOtdrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 72, 2)
)
_IfOtdrGeneral_ObjectIdentity = ObjectIdentity
ifOtdrGeneral = _IfOtdrGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 72, 2, 1)
)
_IfOtdrGeneralConfigLastChangeTime_Type = DateAndTime
_IfOtdrGeneralConfigLastChangeTime_Object = MibScalar
ifOtdrGeneralConfigLastChangeTime = _IfOtdrGeneralConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 72, 2, 1, 1),
    _IfOtdrGeneralConfigLastChangeTime_Type()
)
ifOtdrGeneralConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtdrGeneralConfigLastChangeTime.setStatus("current")
_IfOtdrGeneralStateLastChangeTime_Type = DateAndTime
_IfOtdrGeneralStateLastChangeTime_Object = MibScalar
ifOtdrGeneralStateLastChangeTime = _IfOtdrGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 72, 2, 1, 2),
    _IfOtdrGeneralStateLastChangeTime_Type()
)
ifOtdrGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtdrGeneralStateLastChangeTime.setStatus("current")
_IfOtdrGeneralFiberSpanTableSize_Type = Unsigned32
_IfOtdrGeneralFiberSpanTableSize_Object = MibScalar
ifOtdrGeneralFiberSpanTableSize = _IfOtdrGeneralFiberSpanTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 72, 2, 1, 3),
    _IfOtdrGeneralFiberSpanTableSize_Type()
)
ifOtdrGeneralFiberSpanTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtdrGeneralFiberSpanTableSize.setStatus("current")
_IfOtdrFiberSpanList_ObjectIdentity = ObjectIdentity
ifOtdrFiberSpanList = _IfOtdrFiberSpanList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 72, 2, 2)
)
_IfOtdrFiberSpanTable_Object = MibTable
ifOtdrFiberSpanTable = _IfOtdrFiberSpanTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 72, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ifOtdrFiberSpanTable.setStatus("current")
_IfOtdrFiberSpanEntry_Object = MibTableRow
ifOtdrFiberSpanEntry = _IfOtdrFiberSpanEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 72, 2, 2, 1, 1)
)
ifOtdrFiberSpanEntry.setIndexNames(
    (0, "LUM-IFOTDR-MIB", "ifOtdrFiberSpanIndex"),
)
if mibBuilder.loadTexts:
    ifOtdrFiberSpanEntry.setStatus("current")
_IfOtdrFiberSpanIndex_Type = Unsigned32
_IfOtdrFiberSpanIndex_Object = MibTableColumn
ifOtdrFiberSpanIndex = _IfOtdrFiberSpanIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 72, 2, 2, 1, 1, 1),
    _IfOtdrFiberSpanIndex_Type()
)
ifOtdrFiberSpanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtdrFiberSpanIndex.setStatus("current")
_IfOtdrFiberSpanName_Type = MgmtNameString
_IfOtdrFiberSpanName_Object = MibTableColumn
ifOtdrFiberSpanName = _IfOtdrFiberSpanName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 72, 2, 2, 1, 1, 2),
    _IfOtdrFiberSpanName_Type()
)
ifOtdrFiberSpanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtdrFiberSpanName.setStatus("current")


class _IfOtdrFiberSpanFiberId_Type(DisplayString):
    """Custom type ifOtdrFiberSpanFiberId based on DisplayString"""
    defaultValue = OctetString("")


_IfOtdrFiberSpanFiberId_Type.__name__ = "DisplayString"
_IfOtdrFiberSpanFiberId_Object = MibTableColumn
ifOtdrFiberSpanFiberId = _IfOtdrFiberSpanFiberId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 72, 2, 2, 1, 1, 3),
    _IfOtdrFiberSpanFiberId_Type()
)
ifOtdrFiberSpanFiberId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifOtdrFiberSpanFiberId.setStatus("current")


class _IfOtdrFiberSpanSessionType_Type(Integer32):
    """Custom type ifOtdrFiberSpanSessionType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nearField", 1),
          ("farField", 2))
    )


_IfOtdrFiberSpanSessionType_Type.__name__ = "Integer32"
_IfOtdrFiberSpanSessionType_Object = MibTableColumn
ifOtdrFiberSpanSessionType = _IfOtdrFiberSpanSessionType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 72, 2, 2, 1, 1, 4),
    _IfOtdrFiberSpanSessionType_Type()
)
ifOtdrFiberSpanSessionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifOtdrFiberSpanSessionType.setStatus("current")
_IfOtdrFiberSpanStartMeasurementCommand_Type = CommandString
_IfOtdrFiberSpanStartMeasurementCommand_Object = MibTableColumn
ifOtdrFiberSpanStartMeasurementCommand = _IfOtdrFiberSpanStartMeasurementCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 72, 2, 2, 1, 1, 5),
    _IfOtdrFiberSpanStartMeasurementCommand_Type()
)
ifOtdrFiberSpanStartMeasurementCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtdrFiberSpanStartMeasurementCommand.setStatus("current")
_IfOtdrFiberSpanConnIfBasicIfIndex_Type = Unsigned32WithNA
_IfOtdrFiberSpanConnIfBasicIfIndex_Object = MibTableColumn
ifOtdrFiberSpanConnIfBasicIfIndex = _IfOtdrFiberSpanConnIfBasicIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 72, 2, 2, 1, 1, 6),
    _IfOtdrFiberSpanConnIfBasicIfIndex_Type()
)
ifOtdrFiberSpanConnIfBasicIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifOtdrFiberSpanConnIfBasicIfIndex.setStatus("current")
_IfOtdrFiberSpanSubrack_Type = SubrackNumber
_IfOtdrFiberSpanSubrack_Object = MibTableColumn
ifOtdrFiberSpanSubrack = _IfOtdrFiberSpanSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 72, 2, 2, 1, 1, 7),
    _IfOtdrFiberSpanSubrack_Type()
)
ifOtdrFiberSpanSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifOtdrFiberSpanSubrack.setStatus("current")
_IfOtdrFiberSpanSlot_Type = SlotNumber
_IfOtdrFiberSpanSlot_Object = MibTableColumn
ifOtdrFiberSpanSlot = _IfOtdrFiberSpanSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 72, 2, 2, 1, 1, 8),
    _IfOtdrFiberSpanSlot_Type()
)
ifOtdrFiberSpanSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifOtdrFiberSpanSlot.setStatus("current")
_IfOtdrFiberSpanPortNr_Type = PortNumber
_IfOtdrFiberSpanPortNr_Object = MibTableColumn
ifOtdrFiberSpanPortNr = _IfOtdrFiberSpanPortNr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 72, 2, 2, 1, 1, 9),
    _IfOtdrFiberSpanPortNr_Type()
)
ifOtdrFiberSpanPortNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtdrFiberSpanPortNr.setStatus("current")


class _IfOtdrFiberSpanState_Type(Integer32):
    """Custom type ifOtdrFiberSpanState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("measuring", 1))
    )


_IfOtdrFiberSpanState_Type.__name__ = "Integer32"
_IfOtdrFiberSpanState_Object = MibTableColumn
ifOtdrFiberSpanState = _IfOtdrFiberSpanState_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 72, 2, 2, 1, 1, 10),
    _IfOtdrFiberSpanState_Type()
)
ifOtdrFiberSpanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOtdrFiberSpanState.setStatus("current")

# Managed Objects groups

ifOtdrGeneralGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 72, 1, 1, 1)
)
ifOtdrGeneralGroupV1.setObjects(
      *(("LUM-IFOTDR-MIB", "ifOtdrGeneralConfigLastChangeTime"),
        ("LUM-IFOTDR-MIB", "ifOtdrGeneralStateLastChangeTime"))
)
if mibBuilder.loadTexts:
    ifOtdrGeneralGroupV1.setStatus("current")

ifOtdrFiberSpanGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 72, 1, 1, 2)
)
ifOtdrFiberSpanGroupV1.setObjects(
      *(("LUM-IFOTDR-MIB", "ifOtdrFiberSpanIndex"),
        ("LUM-IFOTDR-MIB", "ifOtdrFiberSpanName"),
        ("LUM-IFOTDR-MIB", "ifOtdrFiberSpanFiberId"),
        ("LUM-IFOTDR-MIB", "ifOtdrFiberSpanSessionType"),
        ("LUM-IFOTDR-MIB", "ifOtdrFiberSpanStartMeasurementCommand"),
        ("LUM-IFOTDR-MIB", "ifOtdrFiberSpanConnIfBasicIfIndex"),
        ("LUM-IFOTDR-MIB", "ifOtdrFiberSpanSubrack"),
        ("LUM-IFOTDR-MIB", "ifOtdrFiberSpanSlot"),
        ("LUM-IFOTDR-MIB", "ifOtdrFiberSpanPortNr"),
        ("LUM-IFOTDR-MIB", "ifOtdrFiberSpanState"))
)
if mibBuilder.loadTexts:
    ifOtdrFiberSpanGroupV1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumIfOtdrComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 72, 1, 2, 1)
)
lumIfOtdrComplV1.setObjects(
      *(("LUM-IFOTDR-MIB", "ifOtdrGeneralGroupV1"),
        ("LUM-IFOTDR-MIB", "ifOtdrFiberSpanGroupV1"))
)
if mibBuilder.loadTexts:
    lumIfOtdrComplV1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-IFOTDR-MIB",
    **{"ifOtdrMIBModule": ifOtdrMIBModule,
       "lumIfOtdrConfs": lumIfOtdrConfs,
       "lumIfOtdrGroups": lumIfOtdrGroups,
       "ifOtdrGeneralGroupV1": ifOtdrGeneralGroupV1,
       "ifOtdrFiberSpanGroupV1": ifOtdrFiberSpanGroupV1,
       "lumIfOtdrCompl": lumIfOtdrCompl,
       "lumIfOtdrComplV1": lumIfOtdrComplV1,
       "lumIfOtdrMIBObjects": lumIfOtdrMIBObjects,
       "ifOtdrGeneral": ifOtdrGeneral,
       "ifOtdrGeneralConfigLastChangeTime": ifOtdrGeneralConfigLastChangeTime,
       "ifOtdrGeneralStateLastChangeTime": ifOtdrGeneralStateLastChangeTime,
       "ifOtdrGeneralFiberSpanTableSize": ifOtdrGeneralFiberSpanTableSize,
       "ifOtdrFiberSpanList": ifOtdrFiberSpanList,
       "ifOtdrFiberSpanTable": ifOtdrFiberSpanTable,
       "ifOtdrFiberSpanEntry": ifOtdrFiberSpanEntry,
       "ifOtdrFiberSpanIndex": ifOtdrFiberSpanIndex,
       "ifOtdrFiberSpanName": ifOtdrFiberSpanName,
       "ifOtdrFiberSpanFiberId": ifOtdrFiberSpanFiberId,
       "ifOtdrFiberSpanSessionType": ifOtdrFiberSpanSessionType,
       "ifOtdrFiberSpanStartMeasurementCommand": ifOtdrFiberSpanStartMeasurementCommand,
       "ifOtdrFiberSpanConnIfBasicIfIndex": ifOtdrFiberSpanConnIfBasicIfIndex,
       "ifOtdrFiberSpanSubrack": ifOtdrFiberSpanSubrack,
       "ifOtdrFiberSpanSlot": ifOtdrFiberSpanSlot,
       "ifOtdrFiberSpanPortNr": ifOtdrFiberSpanPortNr,
       "ifOtdrFiberSpanState": ifOtdrFiberSpanState}
)
