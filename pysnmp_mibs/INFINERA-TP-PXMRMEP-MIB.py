# SNMP MIB module (INFINERA-TP-PXMRMEP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-PXMRMEP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:12:43 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(terminationPoint,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "terminationPoint")

(InfnInterfaceStatusTLV,
 InfnIsEnabled,
 InfnPortStatusTLV,
 InfnRMepType,
 InfnRmepState,
 InfnSenderIDTLV) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "InfnInterfaceStatusTLV",
    "InfnIsEnabled",
    "InfnPortStatusTLV",
    "InfnRMepType",
    "InfnRmepState",
    "InfnSenderIDTLV")

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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

rmepMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 77)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RmepTable_Object = MibTable
rmepTable = _RmepTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 77, 1)
)
if mibBuilder.loadTexts:
    rmepTable.setStatus("current")
_RmepEntry_Object = MibTableRow
rmepEntry = _RmepEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 77, 1, 1)
)
rmepEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rmepEntry.setStatus("current")
_RmepLocalMepAid_Type = DisplayString
_RmepLocalMepAid_Object = MibTableColumn
rmepLocalMepAid = _RmepLocalMepAid_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 77, 1, 1, 1),
    _RmepLocalMepAid_Type()
)
rmepLocalMepAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmepLocalMepAid.setStatus("current")
_RmepLocalMepId_Type = Integer32
_RmepLocalMepId_Object = MibTableColumn
rmepLocalMepId = _RmepLocalMepId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 77, 1, 1, 2),
    _RmepLocalMepId_Type()
)
rmepLocalMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmepLocalMepId.setStatus("current")
_RmepRMepId_Type = Integer32
_RmepRMepId_Object = MibTableColumn
rmepRMepId = _RmepRMepId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 77, 1, 1, 3),
    _RmepRMepId_Type()
)
rmepRMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmepRMepId.setStatus("current")
_RmepRMepType_Type = InfnRMepType
_RmepRMepType_Object = MibTableColumn
rmepRMepType = _RmepRMepType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 77, 1, 1, 4),
    _RmepRMepType_Type()
)
rmepRMepType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmepRMepType.setStatus("current")
_RmepMDLevel_Type = Integer32
_RmepMDLevel_Object = MibTableColumn
rmepMDLevel = _RmepMDLevel_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 77, 1, 1, 5),
    _RmepMDLevel_Type()
)
rmepMDLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmepMDLevel.setStatus("current")
_RmepRmepState_Type = InfnRmepState
_RmepRmepState_Object = MibTableColumn
rmepRmepState = _RmepRmepState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 77, 1, 1, 6),
    _RmepRmepState_Type()
)
rmepRmepState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmepRmepState.setStatus("current")
_RmepFailedOkTime_Type = Integer32
_RmepFailedOkTime_Object = MibTableColumn
rmepFailedOkTime = _RmepFailedOkTime_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 77, 1, 1, 7),
    _RmepFailedOkTime_Type()
)
rmepFailedOkTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmepFailedOkTime.setStatus("current")
_RmepMacAddress_Type = DisplayString
_RmepMacAddress_Object = MibTableColumn
rmepMacAddress = _RmepMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 77, 1, 1, 8),
    _RmepMacAddress_Type()
)
rmepMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmepMacAddress.setStatus("current")
_RmepRDI_Type = InfnIsEnabled
_RmepRDI_Object = MibTableColumn
rmepRDI = _RmepRDI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 77, 1, 1, 9),
    _RmepRDI_Type()
)
rmepRDI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmepRDI.setStatus("current")
_RmepPortStatusTLV_Type = InfnPortStatusTLV
_RmepPortStatusTLV_Object = MibTableColumn
rmepPortStatusTLV = _RmepPortStatusTLV_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 77, 1, 1, 10),
    _RmepPortStatusTLV_Type()
)
rmepPortStatusTLV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmepPortStatusTLV.setStatus("current")
_RmepInterfaceStatusTLV_Type = InfnInterfaceStatusTLV
_RmepInterfaceStatusTLV_Object = MibTableColumn
rmepInterfaceStatusTLV = _RmepInterfaceStatusTLV_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 77, 1, 1, 11),
    _RmepInterfaceStatusTLV_Type()
)
rmepInterfaceStatusTLV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmepInterfaceStatusTLV.setStatus("current")
_RmepSenderIDTLV_Type = InfnSenderIDTLV
_RmepSenderIDTLV_Object = MibTableColumn
rmepSenderIDTLV = _RmepSenderIDTLV_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 77, 1, 1, 12),
    _RmepSenderIDTLV_Type()
)
rmepSenderIDTLV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmepSenderIDTLV.setStatus("current")
_RmepConformance_ObjectIdentity = ObjectIdentity
rmepConformance = _RmepConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 77, 3)
)
_RmepCompliances_ObjectIdentity = ObjectIdentity
rmepCompliances = _RmepCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 77, 3, 1)
)
_RmepGroups_ObjectIdentity = ObjectIdentity
rmepGroups = _RmepGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 77, 3, 2)
)

# Managed Objects groups

rmepGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 77, 3, 2, 1)
)
rmepGroup.setObjects(
      *(("INFINERA-TP-PXMRMEP-MIB", "rmepLocalMepAid"),
        ("INFINERA-TP-PXMRMEP-MIB", "rmepLocalMepId"),
        ("INFINERA-TP-PXMRMEP-MIB", "rmepRMepId"),
        ("INFINERA-TP-PXMRMEP-MIB", "rmepRMepType"),
        ("INFINERA-TP-PXMRMEP-MIB", "rmepMDLevel"),
        ("INFINERA-TP-PXMRMEP-MIB", "rmepRmepState"),
        ("INFINERA-TP-PXMRMEP-MIB", "rmepFailedOkTime"),
        ("INFINERA-TP-PXMRMEP-MIB", "rmepMacAddress"),
        ("INFINERA-TP-PXMRMEP-MIB", "rmepRDI"),
        ("INFINERA-TP-PXMRMEP-MIB", "rmepPortStatusTLV"),
        ("INFINERA-TP-PXMRMEP-MIB", "rmepInterfaceStatusTLV"),
        ("INFINERA-TP-PXMRMEP-MIB", "rmepSenderIDTLV"))
)
if mibBuilder.loadTexts:
    rmepGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rmepCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 77, 3, 1, 1)
)
rmepCompliance.setObjects(
    ("INFINERA-TP-PXMRMEP-MIB", "rmepGroup")
)
if mibBuilder.loadTexts:
    rmepCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-PXMRMEP-MIB",
    **{"rmepMIB": rmepMIB,
       "rmepTable": rmepTable,
       "rmepEntry": rmepEntry,
       "rmepLocalMepAid": rmepLocalMepAid,
       "rmepLocalMepId": rmepLocalMepId,
       "rmepRMepId": rmepRMepId,
       "rmepRMepType": rmepRMepType,
       "rmepMDLevel": rmepMDLevel,
       "rmepRmepState": rmepRmepState,
       "rmepFailedOkTime": rmepFailedOkTime,
       "rmepMacAddress": rmepMacAddress,
       "rmepRDI": rmepRDI,
       "rmepPortStatusTLV": rmepPortStatusTLV,
       "rmepInterfaceStatusTLV": rmepInterfaceStatusTLV,
       "rmepSenderIDTLV": rmepSenderIDTLV,
       "rmepConformance": rmepConformance,
       "rmepCompliances": rmepCompliances,
       "rmepCompliance": rmepCompliance,
       "rmepGroups": rmepGroups,
       "rmepGroup": rmepGroup}
)
