# SNMP MIB module (DC-OAMM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/DC-OAMM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:05:01 2025
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

(AdminStatus,
 BaseOperStatus,
 MjStatus,
 OperStatus) = mibBuilder.importSymbols(
    "DC-MASTER-TC",
    "AdminStatus",
    "BaseOperStatus",
    "MjStatus",
    "OperStatus")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

oammMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 14)
)
if mibBuilder.loadTexts:
    oammMib.setRevisions(
        ("2014-12-21 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class OammMjIfId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(696844288,
              697761792,
              1518338048,
              1904214016,
              1988100096)
        )
    )
    namedValues = NamedValues(
        *(("ifAtgI3", 696844288),
          ("ifAtgFri", 697761792),
          ("ifAtgBfdi", 1518338048),
          ("ifAtgLpi", 1904214016),
          ("ifAtgPmi", 1988100096))
    )



# MIB Managed Objects in the order of their OIDs

_Nbase_ObjectIdentity = ObjectIdentity
nbase = _Nbase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629)
)
_Opx_ObjectIdentity = ObjectIdentity
opx = _Opx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10)
)
_OammObjects_ObjectIdentity = ObjectIdentity
oammObjects = _OammObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 14, 1)
)
_OammEntTable_Object = MibTable
oammEntTable = _OammEntTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 14, 1, 1)
)
if mibBuilder.loadTexts:
    oammEntTable.setStatus("current")
_OammEntEntry_Object = MibTableRow
oammEntEntry = _OammEntEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 14, 1, 1, 1)
)
oammEntEntry.setIndexNames(
    (0, "DC-OAMM-MIB", "oammEntApplIndex"),
)
if mibBuilder.loadTexts:
    oammEntEntry.setStatus("current")
_OammEntApplIndex_Type = Unsigned32
_OammEntApplIndex_Object = MibTableColumn
oammEntApplIndex = _OammEntApplIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 14, 1, 1, 1, 1),
    _OammEntApplIndex_Type()
)
oammEntApplIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oammEntApplIndex.setStatus("current")
_OammEntRowStatus_Type = RowStatus
_OammEntRowStatus_Object = MibTableColumn
oammEntRowStatus = _OammEntRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 14, 1, 1, 1, 2),
    _OammEntRowStatus_Type()
)
oammEntRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oammEntRowStatus.setStatus("current")


class _OammEntAdminStatus_Type(AdminStatus):
    """Custom type oammEntAdminStatus based on AdminStatus"""
    defaultValue = 1


_OammEntAdminStatus_Type.__name__ = "AdminStatus"
_OammEntAdminStatus_Object = MibTableColumn
oammEntAdminStatus = _OammEntAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 14, 1, 1, 1, 3),
    _OammEntAdminStatus_Type()
)
oammEntAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oammEntAdminStatus.setStatus("current")
_OammEntOperStatus_Type = BaseOperStatus
_OammEntOperStatus_Object = MibTableColumn
oammEntOperStatus = _OammEntOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 14, 1, 1, 1, 4),
    _OammEntOperStatus_Type()
)
oammEntOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oammEntOperStatus.setStatus("current")


class _OammEntEnableTrapSupport_Type(TruthValue):
    """Custom type oammEntEnableTrapSupport based on TruthValue"""
    defaultValue = 2


_OammEntEnableTrapSupport_Type.__name__ = "TruthValue"
_OammEntEnableTrapSupport_Object = MibTableColumn
oammEntEnableTrapSupport = _OammEntEnableTrapSupport_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 14, 1, 1, 1, 5),
    _OammEntEnableTrapSupport_Type()
)
oammEntEnableTrapSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oammEntEnableTrapSupport.setStatus("current")


class _OammEntFriBufferPoolSize_Type(Integer32):
    """Custom type oammEntFriBufferPoolSize based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_OammEntFriBufferPoolSize_Type.__name__ = "Integer32"
_OammEntFriBufferPoolSize_Object = MibTableColumn
oammEntFriBufferPoolSize = _OammEntFriBufferPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 14, 1, 1, 1, 6),
    _OammEntFriBufferPoolSize_Type()
)
oammEntFriBufferPoolSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oammEntFriBufferPoolSize.setStatus("current")


class _OammEntRescheduleLimit_Type(Integer32):
    """Custom type oammEntRescheduleLimit based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OammEntRescheduleLimit_Type.__name__ = "Integer32"
_OammEntRescheduleLimit_Object = MibTableColumn
oammEntRescheduleLimit = _OammEntRescheduleLimit_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 14, 1, 1, 1, 7),
    _OammEntRescheduleLimit_Type()
)
oammEntRescheduleLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oammEntRescheduleLimit.setStatus("current")
_OammMjTable_Object = MibTable
oammMjTable = _OammMjTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 14, 1, 2)
)
if mibBuilder.loadTexts:
    oammMjTable.setStatus("current")
_OammMjEntry_Object = MibTableRow
oammMjEntry = _OammMjEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 14, 1, 2, 1)
)
oammMjEntry.setIndexNames(
    (0, "DC-OAMM-MIB", "oammMjApplIndex"),
    (0, "DC-OAMM-MIB", "oammMjInterfaceId"),
    (0, "DC-OAMM-MIB", "oammMjPartnerType"),
    (0, "DC-OAMM-MIB", "oammMjPartnerIndex"),
    (0, "DC-OAMM-MIB", "oammMjSubIndex"),
)
if mibBuilder.loadTexts:
    oammMjEntry.setStatus("current")
_OammMjApplIndex_Type = Unsigned32
_OammMjApplIndex_Object = MibTableColumn
oammMjApplIndex = _OammMjApplIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 14, 1, 2, 1, 1),
    _OammMjApplIndex_Type()
)
oammMjApplIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oammMjApplIndex.setStatus("current")
_OammMjInterfaceId_Type = OammMjIfId
_OammMjInterfaceId_Object = MibTableColumn
oammMjInterfaceId = _OammMjInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 14, 1, 2, 1, 2),
    _OammMjInterfaceId_Type()
)
oammMjInterfaceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oammMjInterfaceId.setStatus("current")
_OammMjPartnerType_Type = Unsigned32
_OammMjPartnerType_Object = MibTableColumn
oammMjPartnerType = _OammMjPartnerType_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 14, 1, 2, 1, 3),
    _OammMjPartnerType_Type()
)
oammMjPartnerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oammMjPartnerType.setStatus("current")
_OammMjPartnerIndex_Type = Unsigned32
_OammMjPartnerIndex_Object = MibTableColumn
oammMjPartnerIndex = _OammMjPartnerIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 14, 1, 2, 1, 4),
    _OammMjPartnerIndex_Type()
)
oammMjPartnerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oammMjPartnerIndex.setStatus("current")
_OammMjSubIndex_Type = Unsigned32
_OammMjSubIndex_Object = MibTableColumn
oammMjSubIndex = _OammMjSubIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 14, 1, 2, 1, 5),
    _OammMjSubIndex_Type()
)
oammMjSubIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oammMjSubIndex.setStatus("current")
_OammMjRowStatus_Type = RowStatus
_OammMjRowStatus_Object = MibTableColumn
oammMjRowStatus = _OammMjRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 14, 1, 2, 1, 6),
    _OammMjRowStatus_Type()
)
oammMjRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oammMjRowStatus.setStatus("current")


class _OammMjAdminStatus_Type(AdminStatus):
    """Custom type oammMjAdminStatus based on AdminStatus"""
    defaultValue = 1


_OammMjAdminStatus_Type.__name__ = "AdminStatus"
_OammMjAdminStatus_Object = MibTableColumn
oammMjAdminStatus = _OammMjAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 14, 1, 2, 1, 7),
    _OammMjAdminStatus_Type()
)
oammMjAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oammMjAdminStatus.setStatus("current")
_OammMjOperStatus_Type = OperStatus
_OammMjOperStatus_Object = MibTableColumn
oammMjOperStatus = _OammMjOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 14, 1, 2, 1, 8),
    _OammMjOperStatus_Type()
)
oammMjOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oammMjOperStatus.setStatus("current")
_OammMjJoinStatus_Type = MjStatus
_OammMjJoinStatus_Object = MibTableColumn
oammMjJoinStatus = _OammMjJoinStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 14, 1, 2, 1, 9),
    _OammMjJoinStatus_Type()
)
oammMjJoinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oammMjJoinStatus.setStatus("current")
_OammConformance_ObjectIdentity = ObjectIdentity
oammConformance = _OammConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 14, 2)
)
_OammGroups_ObjectIdentity = ObjectIdentity
oammGroups = _OammGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 14, 2, 1)
)
_OammCompliances_ObjectIdentity = ObjectIdentity
oammCompliances = _OammCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 14, 2, 2)
)

# Managed Objects groups

oammGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 14, 2, 1, 1)
)
oammGeneralGroup.setObjects(
      *(("DC-OAMM-MIB", "oammEntRowStatus"),
        ("DC-OAMM-MIB", "oammEntAdminStatus"),
        ("DC-OAMM-MIB", "oammEntOperStatus"),
        ("DC-OAMM-MIB", "oammEntEnableTrapSupport"),
        ("DC-OAMM-MIB", "oammEntFriBufferPoolSize"),
        ("DC-OAMM-MIB", "oammEntRescheduleLimit"),
        ("DC-OAMM-MIB", "oammMjRowStatus"),
        ("DC-OAMM-MIB", "oammMjAdminStatus"),
        ("DC-OAMM-MIB", "oammMjOperStatus"),
        ("DC-OAMM-MIB", "oammMjJoinStatus"))
)
if mibBuilder.loadTexts:
    oammGeneralGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

oammModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 629, 10, 14, 2, 2, 1)
)
oammModuleFullCompliance.setObjects(
    ("DC-OAMM-MIB", "oammGeneralGroup")
)
if mibBuilder.loadTexts:
    oammModuleFullCompliance.setStatus(
        "current"
    )

oammModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 629, 10, 14, 2, 2, 2)
)
oammModuleReadOnlyCompliance.setObjects(
    ("DC-OAMM-MIB", "oammGeneralGroup")
)
if mibBuilder.loadTexts:
    oammModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DC-OAMM-MIB",
    **{"OammMjIfId": OammMjIfId,
       "nbase": nbase,
       "opx": opx,
       "oammMib": oammMib,
       "oammObjects": oammObjects,
       "oammEntTable": oammEntTable,
       "oammEntEntry": oammEntEntry,
       "oammEntApplIndex": oammEntApplIndex,
       "oammEntRowStatus": oammEntRowStatus,
       "oammEntAdminStatus": oammEntAdminStatus,
       "oammEntOperStatus": oammEntOperStatus,
       "oammEntEnableTrapSupport": oammEntEnableTrapSupport,
       "oammEntFriBufferPoolSize": oammEntFriBufferPoolSize,
       "oammEntRescheduleLimit": oammEntRescheduleLimit,
       "oammMjTable": oammMjTable,
       "oammMjEntry": oammMjEntry,
       "oammMjApplIndex": oammMjApplIndex,
       "oammMjInterfaceId": oammMjInterfaceId,
       "oammMjPartnerType": oammMjPartnerType,
       "oammMjPartnerIndex": oammMjPartnerIndex,
       "oammMjSubIndex": oammMjSubIndex,
       "oammMjRowStatus": oammMjRowStatus,
       "oammMjAdminStatus": oammMjAdminStatus,
       "oammMjOperStatus": oammMjOperStatus,
       "oammMjJoinStatus": oammMjJoinStatus,
       "oammConformance": oammConformance,
       "oammGroups": oammGroups,
       "oammGeneralGroup": oammGeneralGroup,
       "oammCompliances": oammCompliances,
       "oammModuleFullCompliance": oammModuleFullCompliance,
       "oammModuleReadOnlyCompliance": oammModuleReadOnlyCompliance}
)
