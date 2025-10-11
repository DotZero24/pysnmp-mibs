# SNMP MIB module (LUM-MCLAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-MCLAG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:45 2025
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

(lumMclagMIB,
 lumModules) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumMclagMIB",
    "lumModules")

(FaultStatus,
 MgmtNameString) = mibBuilder.importSymbols(
    "LUM-TC",
    "FaultStatus",
    "MgmtNameString")

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

lumMclagMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 62)
)
if mibBuilder.loadTexts:
    lumMclagMIBModule.setRevisions(
        ("2017-06-15 00:00",
         "2015-01-14 00:00",
         "2014-11-05 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class MclagLabel(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )



class MclagIdentifier(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_LumMclagConfs_ObjectIdentity = ObjectIdentity
lumMclagConfs = _LumMclagConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 62, 1)
)
_LumMclagGroups_ObjectIdentity = ObjectIdentity
lumMclagGroups = _LumMclagGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 62, 1, 1)
)
_LumMclagCompl_ObjectIdentity = ObjectIdentity
lumMclagCompl = _LumMclagCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 62, 1, 2)
)
_LumMclagMIBObjects_ObjectIdentity = ObjectIdentity
lumMclagMIBObjects = _LumMclagMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 62, 2)
)
_MclagGeneral_ObjectIdentity = ObjectIdentity
mclagGeneral = _MclagGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 62, 2, 1)
)
_MclagGeneralLastChangeTime_Type = DateAndTime
_MclagGeneralLastChangeTime_Object = MibScalar
mclagGeneralLastChangeTime = _MclagGeneralLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 62, 2, 1, 1),
    _MclagGeneralLastChangeTime_Type()
)
mclagGeneralLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mclagGeneralLastChangeTime.setStatus("current")
_MclagGeneralStateLastChangeTime_Type = DateAndTime
_MclagGeneralStateLastChangeTime_Object = MibScalar
mclagGeneralStateLastChangeTime = _MclagGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 62, 2, 1, 2),
    _MclagGeneralStateLastChangeTime_Type()
)
mclagGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mclagGeneralStateLastChangeTime.setStatus("current")
_MclagGeneralMclagTableSize_Type = Unsigned32
_MclagGeneralMclagTableSize_Object = MibScalar
mclagGeneralMclagTableSize = _MclagGeneralMclagTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 62, 2, 1, 3),
    _MclagGeneralMclagTableSize_Type()
)
mclagGeneralMclagTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mclagGeneralMclagTableSize.setStatus("current")
_MclagList_ObjectIdentity = ObjectIdentity
mclagList = _MclagList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 62, 2, 2)
)
_MclagTable_Object = MibTable
mclagTable = _MclagTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 62, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mclagTable.setStatus("current")
_MclagEntry_Object = MibTableRow
mclagEntry = _MclagEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 62, 2, 2, 1, 1)
)
mclagEntry.setIndexNames(
    (0, "LUM-MCLAG-MIB", "mclagIndex"),
)
if mibBuilder.loadTexts:
    mclagEntry.setStatus("current")


class _MclagIndex_Type(Unsigned32):
    """Custom type mclagIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MclagIndex_Type.__name__ = "Unsigned32"
_MclagIndex_Object = MibTableColumn
mclagIndex = _MclagIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 62, 2, 2, 1, 1, 1),
    _MclagIndex_Type()
)
mclagIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mclagIndex.setStatus("current")
_MclagName_Type = MgmtNameString
_MclagName_Object = MibTableColumn
mclagName = _MclagName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 62, 2, 2, 1, 1, 2),
    _MclagName_Type()
)
mclagName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mclagName.setStatus("current")


class _MclagDescr_Type(DisplayString):
    """Custom type mclagDescr based on DisplayString"""
    defaultValue = OctetString("")


_MclagDescr_Type.__name__ = "DisplayString"
_MclagDescr_Object = MibTableColumn
mclagDescr = _MclagDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 62, 2, 2, 1, 1, 3),
    _MclagDescr_Type()
)
mclagDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mclagDescr.setStatus("current")


class _MclagNodeId_Type(Unsigned32):
    """Custom type mclagNodeId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MclagNodeId_Type.__name__ = "Unsigned32"
_MclagNodeId_Object = MibTableColumn
mclagNodeId = _MclagNodeId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 62, 2, 2, 1, 1, 4),
    _MclagNodeId_Type()
)
mclagNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mclagNodeId.setStatus("current")


class _MclagRgId_Type(Unsigned32):
    """Custom type mclagRgId based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_MclagRgId_Type.__name__ = "Unsigned32"
_MclagRgId_Object = MibTableColumn
mclagRgId = _MclagRgId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 62, 2, 2, 1, 1, 5),
    _MclagRgId_Type()
)
mclagRgId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mclagRgId.setStatus("current")


class _MclagSynchronizationStatus_Type(Integer32):
    """Custom type mclagSynchronizationStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unSynchronized", 1),
          ("synchronized", 2),
          ("undefined", 3))
    )


_MclagSynchronizationStatus_Type.__name__ = "Integer32"
_MclagSynchronizationStatus_Object = MibTableColumn
mclagSynchronizationStatus = _MclagSynchronizationStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 62, 2, 2, 1, 1, 6),
    _MclagSynchronizationStatus_Type()
)
mclagSynchronizationStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mclagSynchronizationStatus.setStatus("current")


class _MclagControlledLag_Type(DisplayString):
    """Custom type mclagControlledLag based on DisplayString"""
    defaultValue = OctetString("")


_MclagControlledLag_Type.__name__ = "DisplayString"
_MclagControlledLag_Object = MibTableColumn
mclagControlledLag = _MclagControlledLag_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 62, 2, 2, 1, 1, 7),
    _MclagControlledLag_Type()
)
mclagControlledLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mclagControlledLag.setStatus("current")


class _MclagLagAdminSystemPrio_Type(Unsigned32):
    """Custom type mclagLagAdminSystemPrio based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MclagLagAdminSystemPrio_Type.__name__ = "Unsigned32"
_MclagLagAdminSystemPrio_Object = MibTableColumn
mclagLagAdminSystemPrio = _MclagLagAdminSystemPrio_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 62, 2, 2, 1, 1, 8),
    _MclagLagAdminSystemPrio_Type()
)
mclagLagAdminSystemPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mclagLagAdminSystemPrio.setStatus("current")


class _MclagLagOperSystemPrio_Type(Unsigned32):
    """Custom type mclagLagOperSystemPrio based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MclagLagOperSystemPrio_Type.__name__ = "Unsigned32"
_MclagLagOperSystemPrio_Object = MibTableColumn
mclagLagOperSystemPrio = _MclagLagOperSystemPrio_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 62, 2, 2, 1, 1, 9),
    _MclagLagOperSystemPrio_Type()
)
mclagLagOperSystemPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mclagLagOperSystemPrio.setStatus("current")


class _MclagLagAdminPortPrio_Type(Unsigned32):
    """Custom type mclagLagAdminPortPrio based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MclagLagAdminPortPrio_Type.__name__ = "Unsigned32"
_MclagLagAdminPortPrio_Object = MibTableColumn
mclagLagAdminPortPrio = _MclagLagAdminPortPrio_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 62, 2, 2, 1, 1, 10),
    _MclagLagAdminPortPrio_Type()
)
mclagLagAdminPortPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mclagLagAdminPortPrio.setStatus("current")


class _MclagLagOperPortPrio_Type(Unsigned32):
    """Custom type mclagLagOperPortPrio based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MclagLagOperPortPrio_Type.__name__ = "Unsigned32"
_MclagLagOperPortPrio_Object = MibTableColumn
mclagLagOperPortPrio = _MclagLagOperPortPrio_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 62, 2, 2, 1, 1, 11),
    _MclagLagOperPortPrio_Type()
)
mclagLagOperPortPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mclagLagOperPortPrio.setStatus("current")


class _MclagLagStatus_Type(Integer32):
    """Custom type mclagLagStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("standby", 1),
          ("active", 2))
    )


_MclagLagStatus_Type.__name__ = "Integer32"
_MclagLagStatus_Object = MibTableColumn
mclagLagStatus = _MclagLagStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 62, 2, 2, 1, 1, 12),
    _MclagLagStatus_Type()
)
mclagLagStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mclagLagStatus.setStatus("current")
_MclagProtectionStateFailure_Type = FaultStatus
_MclagProtectionStateFailure_Object = MibTableColumn
mclagProtectionStateFailure = _MclagProtectionStateFailure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 62, 2, 2, 1, 1, 13),
    _MclagProtectionStateFailure_Type()
)
mclagProtectionStateFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mclagProtectionStateFailure.setStatus("current")
_MclagProtectionStateDegraded_Type = FaultStatus
_MclagProtectionStateDegraded_Object = MibTableColumn
mclagProtectionStateDegraded = _MclagProtectionStateDegraded_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 62, 2, 2, 1, 1, 14),
    _MclagProtectionStateDegraded_Type()
)
mclagProtectionStateDegraded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mclagProtectionStateDegraded.setStatus("current")


class _MclagInternalReference_Type(Unsigned32):
    """Custom type mclagInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MclagInternalReference_Type.__name__ = "Unsigned32"
_MclagInternalReference_Object = MibTableColumn
mclagInternalReference = _MclagInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 62, 2, 2, 1, 1, 15),
    _MclagInternalReference_Type()
)
mclagInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mclagInternalReference.setStatus("current")

# Managed Objects groups

mclagGeneralGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 62, 1, 1, 1)
)
mclagGeneralGroupV1.setObjects(
      *(("LUM-MCLAG-MIB", "mclagGeneralLastChangeTime"),
        ("LUM-MCLAG-MIB", "mclagGeneralStateLastChangeTime"),
        ("LUM-MCLAG-MIB", "mclagGeneralMclagTableSize"))
)
if mibBuilder.loadTexts:
    mclagGeneralGroupV1.setStatus("current")

mclagGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 62, 1, 1, 2)
)
mclagGroupV1.setObjects(
      *(("LUM-MCLAG-MIB", "mclagIndex"),
        ("LUM-MCLAG-MIB", "mclagName"),
        ("LUM-MCLAG-MIB", "mclagDescr"),
        ("LUM-MCLAG-MIB", "mclagNodeId"),
        ("LUM-MCLAG-MIB", "mclagRgId"),
        ("LUM-MCLAG-MIB", "mclagSynchronizationStatus"),
        ("LUM-MCLAG-MIB", "mclagControlledLag"),
        ("LUM-MCLAG-MIB", "mclagLagAdminSystemPrio"),
        ("LUM-MCLAG-MIB", "mclagLagOperSystemPrio"),
        ("LUM-MCLAG-MIB", "mclagLagAdminPortPrio"),
        ("LUM-MCLAG-MIB", "mclagLagOperPortPrio"),
        ("LUM-MCLAG-MIB", "mclagLagStatus"),
        ("LUM-MCLAG-MIB", "mclagProtectionStateFailure"),
        ("LUM-MCLAG-MIB", "mclagProtectionStateDegraded"),
        ("LUM-MCLAG-MIB", "mclagInternalReference"))
)
if mibBuilder.loadTexts:
    mclagGroupV1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumMclagBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 62, 1, 2, 1)
)
lumMclagBasicComplV1.setObjects(
    ("LUM-MCLAG-MIB", "mclagGroupV1")
)
if mibBuilder.loadTexts:
    lumMclagBasicComplV1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-MCLAG-MIB",
    **{"MclagLabel": MclagLabel,
       "MclagIdentifier": MclagIdentifier,
       "lumMclagMIBModule": lumMclagMIBModule,
       "lumMclagConfs": lumMclagConfs,
       "lumMclagGroups": lumMclagGroups,
       "mclagGeneralGroupV1": mclagGeneralGroupV1,
       "mclagGroupV1": mclagGroupV1,
       "lumMclagCompl": lumMclagCompl,
       "lumMclagBasicComplV1": lumMclagBasicComplV1,
       "lumMclagMIBObjects": lumMclagMIBObjects,
       "mclagGeneral": mclagGeneral,
       "mclagGeneralLastChangeTime": mclagGeneralLastChangeTime,
       "mclagGeneralStateLastChangeTime": mclagGeneralStateLastChangeTime,
       "mclagGeneralMclagTableSize": mclagGeneralMclagTableSize,
       "mclagList": mclagList,
       "mclagTable": mclagTable,
       "mclagEntry": mclagEntry,
       "mclagIndex": mclagIndex,
       "mclagName": mclagName,
       "mclagDescr": mclagDescr,
       "mclagNodeId": mclagNodeId,
       "mclagRgId": mclagRgId,
       "mclagSynchronizationStatus": mclagSynchronizationStatus,
       "mclagControlledLag": mclagControlledLag,
       "mclagLagAdminSystemPrio": mclagLagAdminSystemPrio,
       "mclagLagOperSystemPrio": mclagLagOperSystemPrio,
       "mclagLagAdminPortPrio": mclagLagAdminPortPrio,
       "mclagLagOperPortPrio": mclagLagOperPortPrio,
       "mclagLagStatus": mclagLagStatus,
       "mclagProtectionStateFailure": mclagProtectionStateFailure,
       "mclagProtectionStateDegraded": mclagProtectionStateDegraded,
       "mclagInternalReference": mclagInternalReference}
)
