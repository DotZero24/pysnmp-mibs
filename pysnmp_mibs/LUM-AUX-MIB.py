# SNMP MIB module (LUM-AUX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-AUX-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:32 2025
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

(lumAuxMIB,
 lumModules) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumAuxMIB",
    "lumModules")

(AdminStatusWithNA,
 BoardOrInterfaceAdminStatus,
 BoardOrInterfaceOperStatus,
 CommandString,
 FaultStatus,
 MgmtNameString,
 ObjectProperty,
 PortNumber,
 Signed32WithNA,
 SlotNumber,
 SubrackNumber) = mibBuilder.importSymbols(
    "LUM-TC",
    "AdminStatusWithNA",
    "BoardOrInterfaceAdminStatus",
    "BoardOrInterfaceOperStatus",
    "CommandString",
    "FaultStatus",
    "MgmtNameString",
    "ObjectProperty",
    "PortNumber",
    "Signed32WithNA",
    "SlotNumber",
    "SubrackNumber")

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
 TextualConvention,
 TestAndIncr) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TestAndIncr")


# MODULE-IDENTITY

lumAuxMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 29)
)
if mibBuilder.loadTexts:
    lumAuxMIBModule.setRevisions(
        ("2017-06-15 00:00",
         "2017-04-17 00:00",
         "2016-04-25 00:00",
         "2016-01-11 00:00",
         "2014-11-03 00:00",
         "2012-12-20 00:00",
         "2011-10-12 00:00",
         "2009-08-19 00:00",
         "2004-10-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LumAuxConfs_ObjectIdentity = ObjectIdentity
lumAuxConfs = _LumAuxConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 1)
)
_LumAuxGroups_ObjectIdentity = ObjectIdentity
lumAuxGroups = _LumAuxGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 1, 1)
)
_LumAuxCompl_ObjectIdentity = ObjectIdentity
lumAuxCompl = _LumAuxCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 1, 2)
)
_LumAuxMIBObjects_ObjectIdentity = ObjectIdentity
lumAuxMIBObjects = _LumAuxMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2)
)
_AuxGeneral_ObjectIdentity = ObjectIdentity
auxGeneral = _AuxGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 1)
)
_AuxGeneralTestAndIncr_Type = TestAndIncr
_AuxGeneralTestAndIncr_Object = MibScalar
auxGeneralTestAndIncr = _AuxGeneralTestAndIncr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 1, 1),
    _AuxGeneralTestAndIncr_Type()
)
auxGeneralTestAndIncr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxGeneralTestAndIncr.setStatus("current")
_AuxGeneralStateLastChangeTime_Type = DateAndTime
_AuxGeneralStateLastChangeTime_Object = MibScalar
auxGeneralStateLastChangeTime = _AuxGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 1, 2),
    _AuxGeneralStateLastChangeTime_Type()
)
auxGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxGeneralStateLastChangeTime.setStatus("current")
_AuxGeneralConfigLastChangeTime_Type = DateAndTime
_AuxGeneralConfigLastChangeTime_Object = MibScalar
auxGeneralConfigLastChangeTime = _AuxGeneralConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 1, 3),
    _AuxGeneralConfigLastChangeTime_Type()
)
auxGeneralConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxGeneralConfigLastChangeTime.setStatus("current")
_AuxGeneralSnmpTableSize_Type = Unsigned32
_AuxGeneralSnmpTableSize_Object = MibScalar
auxGeneralSnmpTableSize = _AuxGeneralSnmpTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 1, 4),
    _AuxGeneralSnmpTableSize_Type()
)
auxGeneralSnmpTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxGeneralSnmpTableSize.setStatus("current")
_AuxGeneralFxIfTableSize_Type = Unsigned32
_AuxGeneralFxIfTableSize_Object = MibScalar
auxGeneralFxIfTableSize = _AuxGeneralFxIfTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 1, 5),
    _AuxGeneralFxIfTableSize_Type()
)
auxGeneralFxIfTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxGeneralFxIfTableSize.setStatus("current")
_AuxGeneralAuxEquipmentTableSize_Type = Unsigned32
_AuxGeneralAuxEquipmentTableSize_Object = MibScalar
auxGeneralAuxEquipmentTableSize = _AuxGeneralAuxEquipmentTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 1, 6),
    _AuxGeneralAuxEquipmentTableSize_Type()
)
auxGeneralAuxEquipmentTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxGeneralAuxEquipmentTableSize.setStatus("current")
_AuxGeneralRamanIfTableSize_Type = Unsigned32
_AuxGeneralRamanIfTableSize_Object = MibScalar
auxGeneralRamanIfTableSize = _AuxGeneralRamanIfTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 1, 7),
    _AuxGeneralRamanIfTableSize_Type()
)
auxGeneralRamanIfTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxGeneralRamanIfTableSize.setStatus("current")
_AuxGeneralRamanSafetyTableSize_Type = Unsigned32
_AuxGeneralRamanSafetyTableSize_Object = MibScalar
auxGeneralRamanSafetyTableSize = _AuxGeneralRamanSafetyTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 1, 8),
    _AuxGeneralRamanSafetyTableSize_Type()
)
auxGeneralRamanSafetyTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxGeneralRamanSafetyTableSize.setStatus("current")
_AuxGeneralPEIfTableSize_Type = Unsigned32
_AuxGeneralPEIfTableSize_Object = MibScalar
auxGeneralPEIfTableSize = _AuxGeneralPEIfTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 1, 9),
    _AuxGeneralPEIfTableSize_Type()
)
auxGeneralPEIfTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxGeneralPEIfTableSize.setStatus("current")
_AuxGeneralNodeTableSize_Type = Unsigned32
_AuxGeneralNodeTableSize_Object = MibScalar
auxGeneralNodeTableSize = _AuxGeneralNodeTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 1, 10),
    _AuxGeneralNodeTableSize_Type()
)
auxGeneralNodeTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxGeneralNodeTableSize.setStatus("current")
_AuxGeneralCabinetTableSize_Type = Unsigned32
_AuxGeneralCabinetTableSize_Object = MibScalar
auxGeneralCabinetTableSize = _AuxGeneralCabinetTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 1, 11),
    _AuxGeneralCabinetTableSize_Type()
)
auxGeneralCabinetTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxGeneralCabinetTableSize.setStatus("current")
_AuxGeneralFanTableSize_Type = Unsigned32
_AuxGeneralFanTableSize_Object = MibScalar
auxGeneralFanTableSize = _AuxGeneralFanTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 1, 12),
    _AuxGeneralFanTableSize_Type()
)
auxGeneralFanTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxGeneralFanTableSize.setStatus("current")
_AuxGeneralFanGroupTableSize_Type = Unsigned32
_AuxGeneralFanGroupTableSize_Object = MibScalar
auxGeneralFanGroupTableSize = _AuxGeneralFanGroupTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 1, 13),
    _AuxGeneralFanGroupTableSize_Type()
)
auxGeneralFanGroupTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxGeneralFanGroupTableSize.setStatus("current")
_AuxSnmpList_ObjectIdentity = ObjectIdentity
auxSnmpList = _AuxSnmpList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 2)
)
_AuxSnmpTable_Object = MibTable
auxSnmpTable = _AuxSnmpTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 2, 1)
)
if mibBuilder.loadTexts:
    auxSnmpTable.setStatus("current")
_AuxSnmpEntry_Object = MibTableRow
auxSnmpEntry = _AuxSnmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 2, 1, 1)
)
auxSnmpEntry.setIndexNames(
    (0, "LUM-AUX-MIB", "auxSnmpIndex"),
)
if mibBuilder.loadTexts:
    auxSnmpEntry.setStatus("current")


class _AuxSnmpIndex_Type(Unsigned32):
    """Custom type auxSnmpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AuxSnmpIndex_Type.__name__ = "Unsigned32"
_AuxSnmpIndex_Object = MibTableColumn
auxSnmpIndex = _AuxSnmpIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 2, 1, 1, 1),
    _AuxSnmpIndex_Type()
)
auxSnmpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxSnmpIndex.setStatus("current")
_AuxSnmpName_Type = MgmtNameString
_AuxSnmpName_Object = MibTableColumn
auxSnmpName = _AuxSnmpName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 2, 1, 1, 2),
    _AuxSnmpName_Type()
)
auxSnmpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxSnmpName.setStatus("current")
_AuxSnmpDescr_Type = DisplayString
_AuxSnmpDescr_Object = MibTableColumn
auxSnmpDescr = _AuxSnmpDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 2, 1, 1, 3),
    _AuxSnmpDescr_Type()
)
auxSnmpDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxSnmpDescr.setStatus("current")
_AuxSnmpAddress_Type = IpAddress
_AuxSnmpAddress_Object = MibTableColumn
auxSnmpAddress = _AuxSnmpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 2, 1, 1, 4),
    _AuxSnmpAddress_Type()
)
auxSnmpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxSnmpAddress.setStatus("current")


class _AuxSnmpVersion_Type(Integer32):
    """Custom type auxSnmpVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2c", 2))
    )


_AuxSnmpVersion_Type.__name__ = "Integer32"
_AuxSnmpVersion_Object = MibTableColumn
auxSnmpVersion = _AuxSnmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 2, 1, 1, 5),
    _AuxSnmpVersion_Type()
)
auxSnmpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxSnmpVersion.setStatus("current")


class _AuxSnmpPort_Type(Unsigned32):
    """Custom type auxSnmpPort based on Unsigned32"""
    defaultValue = 161

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AuxSnmpPort_Type.__name__ = "Unsigned32"
_AuxSnmpPort_Object = MibTableColumn
auxSnmpPort = _AuxSnmpPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 2, 1, 1, 6),
    _AuxSnmpPort_Type()
)
auxSnmpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxSnmpPort.setStatus("current")


class _AuxSnmpReadCommunity_Type(DisplayString):
    """Custom type auxSnmpReadCommunity based on DisplayString"""
    defaultValue = OctetString("public")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AuxSnmpReadCommunity_Type.__name__ = "DisplayString"
_AuxSnmpReadCommunity_Object = MibTableColumn
auxSnmpReadCommunity = _AuxSnmpReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 2, 1, 1, 7),
    _AuxSnmpReadCommunity_Type()
)
auxSnmpReadCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxSnmpReadCommunity.setStatus("current")


class _AuxSnmpWriteCommunity_Type(DisplayString):
    """Custom type auxSnmpWriteCommunity based on DisplayString"""
    defaultValue = OctetString("private")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AuxSnmpWriteCommunity_Type.__name__ = "DisplayString"
_AuxSnmpWriteCommunity_Object = MibTableColumn
auxSnmpWriteCommunity = _AuxSnmpWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 2, 1, 1, 8),
    _AuxSnmpWriteCommunity_Type()
)
auxSnmpWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxSnmpWriteCommunity.setStatus("current")


class _AuxSnmpAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type auxSnmpAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 3


_AuxSnmpAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_AuxSnmpAdminStatus_Object = MibTableColumn
auxSnmpAdminStatus = _AuxSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 2, 1, 1, 9),
    _AuxSnmpAdminStatus_Type()
)
auxSnmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxSnmpAdminStatus.setStatus("current")


class _AuxSnmpOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type auxSnmpOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 1


_AuxSnmpOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_AuxSnmpOperStatus_Object = MibTableColumn
auxSnmpOperStatus = _AuxSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 2, 1, 1, 10),
    _AuxSnmpOperStatus_Type()
)
auxSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxSnmpOperStatus.setStatus("current")


class _AuxSnmpInvPhysIndexOrZero_Type(Unsigned32):
    """Custom type auxSnmpInvPhysIndexOrZero based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AuxSnmpInvPhysIndexOrZero_Type.__name__ = "Unsigned32"
_AuxSnmpInvPhysIndexOrZero_Object = MibTableColumn
auxSnmpInvPhysIndexOrZero = _AuxSnmpInvPhysIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 2, 1, 1, 11),
    _AuxSnmpInvPhysIndexOrZero_Type()
)
auxSnmpInvPhysIndexOrZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxSnmpInvPhysIndexOrZero.setStatus("current")
_AuxSnmpHostUnreachable_Type = FaultStatus
_AuxSnmpHostUnreachable_Object = MibTableColumn
auxSnmpHostUnreachable = _AuxSnmpHostUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 2, 1, 1, 12),
    _AuxSnmpHostUnreachable_Type()
)
auxSnmpHostUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxSnmpHostUnreachable.setStatus("current")
_AuxSnmpSnmpError_Type = FaultStatus
_AuxSnmpSnmpError_Object = MibTableColumn
auxSnmpSnmpError = _AuxSnmpSnmpError_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 2, 1, 1, 13),
    _AuxSnmpSnmpError_Type()
)
auxSnmpSnmpError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxSnmpSnmpError.setStatus("current")
_AuxSnmpUnexpectedEquipmentType_Type = FaultStatus
_AuxSnmpUnexpectedEquipmentType_Object = MibTableColumn
auxSnmpUnexpectedEquipmentType = _AuxSnmpUnexpectedEquipmentType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 2, 1, 1, 14),
    _AuxSnmpUnexpectedEquipmentType_Type()
)
auxSnmpUnexpectedEquipmentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxSnmpUnexpectedEquipmentType.setStatus("current")
_AuxSnmpInconsistentConfiguration_Type = FaultStatus
_AuxSnmpInconsistentConfiguration_Object = MibTableColumn
auxSnmpInconsistentConfiguration = _AuxSnmpInconsistentConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 2, 1, 1, 15),
    _AuxSnmpInconsistentConfiguration_Type()
)
auxSnmpInconsistentConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxSnmpInconsistentConfiguration.setStatus("current")
_AuxSnmpConfigurationProblem_Type = FaultStatus
_AuxSnmpConfigurationProblem_Object = MibTableColumn
auxSnmpConfigurationProblem = _AuxSnmpConfigurationProblem_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 2, 1, 1, 16),
    _AuxSnmpConfigurationProblem_Type()
)
auxSnmpConfigurationProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxSnmpConfigurationProblem.setStatus("current")
_AuxFxIfList_ObjectIdentity = ObjectIdentity
auxFxIfList = _AuxFxIfList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 3)
)
_AuxFxIfTable_Object = MibTable
auxFxIfTable = _AuxFxIfTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 3, 1)
)
if mibBuilder.loadTexts:
    auxFxIfTable.setStatus("current")
_AuxFxIfEntry_Object = MibTableRow
auxFxIfEntry = _AuxFxIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 3, 1, 1)
)
auxFxIfEntry.setIndexNames(
    (0, "LUM-AUX-MIB", "auxFxIfIndex"),
)
if mibBuilder.loadTexts:
    auxFxIfEntry.setStatus("current")


class _AuxFxIfIndex_Type(Unsigned32):
    """Custom type auxFxIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AuxFxIfIndex_Type.__name__ = "Unsigned32"
_AuxFxIfIndex_Object = MibTableColumn
auxFxIfIndex = _AuxFxIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 3, 1, 1, 1),
    _AuxFxIfIndex_Type()
)
auxFxIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxFxIfIndex.setStatus("current")
_AuxFxIfName_Type = MgmtNameString
_AuxFxIfName_Object = MibTableColumn
auxFxIfName = _AuxFxIfName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 3, 1, 1, 2),
    _AuxFxIfName_Type()
)
auxFxIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxFxIfName.setStatus("current")


class _AuxFxIfDescr_Type(DisplayString):
    """Custom type auxFxIfDescr based on DisplayString"""
    defaultValue = OctetString("")


_AuxFxIfDescr_Type.__name__ = "DisplayString"
_AuxFxIfDescr_Object = MibTableColumn
auxFxIfDescr = _AuxFxIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 3, 1, 1, 3),
    _AuxFxIfDescr_Type()
)
auxFxIfDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxFxIfDescr.setStatus("current")
_AuxFxIfSubrack_Type = SubrackNumber
_AuxFxIfSubrack_Object = MibTableColumn
auxFxIfSubrack = _AuxFxIfSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 3, 1, 1, 4),
    _AuxFxIfSubrack_Type()
)
auxFxIfSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxFxIfSubrack.setStatus("current")
_AuxFxIfSlot_Type = SlotNumber
_AuxFxIfSlot_Object = MibTableColumn
auxFxIfSlot = _AuxFxIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 3, 1, 1, 5),
    _AuxFxIfSlot_Type()
)
auxFxIfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxFxIfSlot.setStatus("current")
_AuxFxIfTxPort_Type = PortNumber
_AuxFxIfTxPort_Object = MibTableColumn
auxFxIfTxPort = _AuxFxIfTxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 3, 1, 1, 6),
    _AuxFxIfTxPort_Type()
)
auxFxIfTxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxFxIfTxPort.setStatus("current")
_AuxFxIfRxPort_Type = PortNumber
_AuxFxIfRxPort_Object = MibTableColumn
auxFxIfRxPort = _AuxFxIfRxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 3, 1, 1, 7),
    _AuxFxIfRxPort_Type()
)
auxFxIfRxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxFxIfRxPort.setStatus("current")


class _AuxFxIfInvPhysIndexOrZero_Type(Unsigned32):
    """Custom type auxFxIfInvPhysIndexOrZero based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AuxFxIfInvPhysIndexOrZero_Type.__name__ = "Unsigned32"
_AuxFxIfInvPhysIndexOrZero_Object = MibTableColumn
auxFxIfInvPhysIndexOrZero = _AuxFxIfInvPhysIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 3, 1, 1, 8),
    _AuxFxIfInvPhysIndexOrZero_Type()
)
auxFxIfInvPhysIndexOrZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxFxIfInvPhysIndexOrZero.setStatus("current")


class _AuxFxIfAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type auxFxIfAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 3


_AuxFxIfAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_AuxFxIfAdminStatus_Object = MibTableColumn
auxFxIfAdminStatus = _AuxFxIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 3, 1, 1, 9),
    _AuxFxIfAdminStatus_Type()
)
auxFxIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxFxIfAdminStatus.setStatus("current")


class _AuxFxIfOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type auxFxIfOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 1


_AuxFxIfOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_AuxFxIfOperStatus_Object = MibTableColumn
auxFxIfOperStatus = _AuxFxIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 3, 1, 1, 10),
    _AuxFxIfOperStatus_Type()
)
auxFxIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxFxIfOperStatus.setStatus("current")
_AuxFxIfRxPowerLevel_Type = Integer32
_AuxFxIfRxPowerLevel_Object = MibTableColumn
auxFxIfRxPowerLevel = _AuxFxIfRxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 3, 1, 1, 11),
    _AuxFxIfRxPowerLevel_Type()
)
auxFxIfRxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxFxIfRxPowerLevel.setStatus("current")


class _AuxFxIfLossOfSignalThreshold_Type(Integer32):
    """Custom type auxFxIfLossOfSignalThreshold based on Integer32"""
    defaultValue = -350

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-350, -60),
    )


_AuxFxIfLossOfSignalThreshold_Type.__name__ = "Integer32"
_AuxFxIfLossOfSignalThreshold_Object = MibTableColumn
auxFxIfLossOfSignalThreshold = _AuxFxIfLossOfSignalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 3, 1, 1, 12),
    _AuxFxIfLossOfSignalThreshold_Type()
)
auxFxIfLossOfSignalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxFxIfLossOfSignalThreshold.setStatus("current")
_AuxFxIfLossOfSignal_Type = FaultStatus
_AuxFxIfLossOfSignal_Object = MibTableColumn
auxFxIfLossOfSignal = _AuxFxIfLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 3, 1, 1, 13),
    _AuxFxIfLossOfSignal_Type()
)
auxFxIfLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxFxIfLossOfSignal.setStatus("current")
_AuxFxIfObjectProperty_Type = ObjectProperty
_AuxFxIfObjectProperty_Object = MibTableColumn
auxFxIfObjectProperty = _AuxFxIfObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 3, 1, 1, 14),
    _AuxFxIfObjectProperty_Type()
)
auxFxIfObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxFxIfObjectProperty.setStatus("current")
_AuxEquipmentList_ObjectIdentity = ObjectIdentity
auxEquipmentList = _AuxEquipmentList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 4)
)
_AuxEquipmentTable_Object = MibTable
auxEquipmentTable = _AuxEquipmentTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 4, 1)
)
if mibBuilder.loadTexts:
    auxEquipmentTable.setStatus("current")
_AuxEquipmentEntry_Object = MibTableRow
auxEquipmentEntry = _AuxEquipmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 4, 1, 1)
)
auxEquipmentEntry.setIndexNames(
    (0, "LUM-AUX-MIB", "auxEquipmentIndex"),
)
if mibBuilder.loadTexts:
    auxEquipmentEntry.setStatus("current")


class _AuxEquipmentIndex_Type(Unsigned32):
    """Custom type auxEquipmentIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AuxEquipmentIndex_Type.__name__ = "Unsigned32"
_AuxEquipmentIndex_Object = MibTableColumn
auxEquipmentIndex = _AuxEquipmentIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 4, 1, 1, 1),
    _AuxEquipmentIndex_Type()
)
auxEquipmentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxEquipmentIndex.setStatus("current")
_AuxEquipmentName_Type = MgmtNameString
_AuxEquipmentName_Object = MibTableColumn
auxEquipmentName = _AuxEquipmentName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 4, 1, 1, 2),
    _AuxEquipmentName_Type()
)
auxEquipmentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxEquipmentName.setStatus("current")


class _AuxEquipmentDescr_Type(DisplayString):
    """Custom type auxEquipmentDescr based on DisplayString"""
    defaultValue = OctetString("")


_AuxEquipmentDescr_Type.__name__ = "DisplayString"
_AuxEquipmentDescr_Object = MibTableColumn
auxEquipmentDescr = _AuxEquipmentDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 4, 1, 1, 3),
    _AuxEquipmentDescr_Type()
)
auxEquipmentDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxEquipmentDescr.setStatus("current")
_AuxEquipmentSubrack_Type = SubrackNumber
_AuxEquipmentSubrack_Object = MibTableColumn
auxEquipmentSubrack = _AuxEquipmentSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 4, 1, 1, 4),
    _AuxEquipmentSubrack_Type()
)
auxEquipmentSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxEquipmentSubrack.setStatus("current")
_AuxEquipmentSlot_Type = SlotNumber
_AuxEquipmentSlot_Object = MibTableColumn
auxEquipmentSlot = _AuxEquipmentSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 4, 1, 1, 5),
    _AuxEquipmentSlot_Type()
)
auxEquipmentSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxEquipmentSlot.setStatus("current")


class _AuxEquipmentAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type auxEquipmentAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 3


_AuxEquipmentAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_AuxEquipmentAdminStatus_Object = MibTableColumn
auxEquipmentAdminStatus = _AuxEquipmentAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 4, 1, 1, 6),
    _AuxEquipmentAdminStatus_Type()
)
auxEquipmentAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxEquipmentAdminStatus.setStatus("current")


class _AuxEquipmentOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type auxEquipmentOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 1


_AuxEquipmentOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_AuxEquipmentOperStatus_Object = MibTableColumn
auxEquipmentOperStatus = _AuxEquipmentOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 4, 1, 1, 7),
    _AuxEquipmentOperStatus_Type()
)
auxEquipmentOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxEquipmentOperStatus.setStatus("current")
_AuxEquipmentPowerFailure_Type = FaultStatus
_AuxEquipmentPowerFailure_Object = MibTableColumn
auxEquipmentPowerFailure = _AuxEquipmentPowerFailure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 4, 1, 1, 8),
    _AuxEquipmentPowerFailure_Type()
)
auxEquipmentPowerFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxEquipmentPowerFailure.setStatus("current")
_AuxEquipmentFanProblem_Type = FaultStatus
_AuxEquipmentFanProblem_Object = MibTableColumn
auxEquipmentFanProblem = _AuxEquipmentFanProblem_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 4, 1, 1, 9),
    _AuxEquipmentFanProblem_Type()
)
auxEquipmentFanProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxEquipmentFanProblem.setStatus("current")
_AuxEquipmentObjectProperty_Type = ObjectProperty
_AuxEquipmentObjectProperty_Object = MibTableColumn
auxEquipmentObjectProperty = _AuxEquipmentObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 4, 1, 1, 10),
    _AuxEquipmentObjectProperty_Type()
)
auxEquipmentObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxEquipmentObjectProperty.setStatus("current")
_AuxEquipmentPumpsEol_Type = FaultStatus
_AuxEquipmentPumpsEol_Object = MibTableColumn
auxEquipmentPumpsEol = _AuxEquipmentPumpsEol_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 4, 1, 1, 11),
    _AuxEquipmentPumpsEol_Type()
)
auxEquipmentPumpsEol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxEquipmentPumpsEol.setStatus("current")
_AuxEquipmentSelfTestFailure_Type = FaultStatus
_AuxEquipmentSelfTestFailure_Object = MibTableColumn
auxEquipmentSelfTestFailure = _AuxEquipmentSelfTestFailure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 4, 1, 1, 12),
    _AuxEquipmentSelfTestFailure_Type()
)
auxEquipmentSelfTestFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxEquipmentSelfTestFailure.setStatus("current")
_AuxEquipmentAmbientTemp_Type = Integer32
_AuxEquipmentAmbientTemp_Object = MibTableColumn
auxEquipmentAmbientTemp = _AuxEquipmentAmbientTemp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 4, 1, 1, 13),
    _AuxEquipmentAmbientTemp_Type()
)
auxEquipmentAmbientTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxEquipmentAmbientTemp.setStatus("current")
_AuxEquipmentRebootEquipment_Type = CommandString
_AuxEquipmentRebootEquipment_Object = MibTableColumn
auxEquipmentRebootEquipment = _AuxEquipmentRebootEquipment_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 4, 1, 1, 14),
    _AuxEquipmentRebootEquipment_Type()
)
auxEquipmentRebootEquipment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxEquipmentRebootEquipment.setStatus("current")
_AuxEquipmentPowerAMissing_Type = FaultStatus
_AuxEquipmentPowerAMissing_Object = MibTableColumn
auxEquipmentPowerAMissing = _AuxEquipmentPowerAMissing_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 4, 1, 1, 15),
    _AuxEquipmentPowerAMissing_Type()
)
auxEquipmentPowerAMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxEquipmentPowerAMissing.setStatus("current")
_AuxEquipmentPowerBMissing_Type = FaultStatus
_AuxEquipmentPowerBMissing_Object = MibTableColumn
auxEquipmentPowerBMissing = _AuxEquipmentPowerBMissing_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 4, 1, 1, 16),
    _AuxEquipmentPowerBMissing_Type()
)
auxEquipmentPowerBMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxEquipmentPowerBMissing.setStatus("current")
_AuxEquipmentConfigurationMismatch_Type = FaultStatus
_AuxEquipmentConfigurationMismatch_Object = MibTableColumn
auxEquipmentConfigurationMismatch = _AuxEquipmentConfigurationMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 4, 1, 1, 17),
    _AuxEquipmentConfigurationMismatch_Type()
)
auxEquipmentConfigurationMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxEquipmentConfigurationMismatch.setStatus("current")
_AuxRamanIfList_ObjectIdentity = ObjectIdentity
auxRamanIfList = _AuxRamanIfList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5)
)
_AuxRamanIfTable_Object = MibTable
auxRamanIfTable = _AuxRamanIfTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1)
)
if mibBuilder.loadTexts:
    auxRamanIfTable.setStatus("current")
_AuxRamanIfEntry_Object = MibTableRow
auxRamanIfEntry = _AuxRamanIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1)
)
auxRamanIfEntry.setIndexNames(
    (0, "LUM-AUX-MIB", "auxRamanIfIndex"),
)
if mibBuilder.loadTexts:
    auxRamanIfEntry.setStatus("current")


class _AuxRamanIfIndex_Type(Unsigned32):
    """Custom type auxRamanIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AuxRamanIfIndex_Type.__name__ = "Unsigned32"
_AuxRamanIfIndex_Object = MibTableColumn
auxRamanIfIndex = _AuxRamanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 1),
    _AuxRamanIfIndex_Type()
)
auxRamanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanIfIndex.setStatus("current")
_AuxRamanIfName_Type = MgmtNameString
_AuxRamanIfName_Object = MibTableColumn
auxRamanIfName = _AuxRamanIfName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 2),
    _AuxRamanIfName_Type()
)
auxRamanIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanIfName.setStatus("current")


class _AuxRamanIfDescr_Type(DisplayString):
    """Custom type auxRamanIfDescr based on DisplayString"""
    defaultValue = OctetString("")


_AuxRamanIfDescr_Type.__name__ = "DisplayString"
_AuxRamanIfDescr_Object = MibTableColumn
auxRamanIfDescr = _AuxRamanIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 3),
    _AuxRamanIfDescr_Type()
)
auxRamanIfDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxRamanIfDescr.setStatus("current")
_AuxRamanIfSubrack_Type = SubrackNumber
_AuxRamanIfSubrack_Object = MibTableColumn
auxRamanIfSubrack = _AuxRamanIfSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 4),
    _AuxRamanIfSubrack_Type()
)
auxRamanIfSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanIfSubrack.setStatus("current")
_AuxRamanIfSlot_Type = SlotNumber
_AuxRamanIfSlot_Object = MibTableColumn
auxRamanIfSlot = _AuxRamanIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 5),
    _AuxRamanIfSlot_Type()
)
auxRamanIfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanIfSlot.setStatus("current")
_AuxRamanIfTxPort_Type = PortNumber
_AuxRamanIfTxPort_Object = MibTableColumn
auxRamanIfTxPort = _AuxRamanIfTxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 6),
    _AuxRamanIfTxPort_Type()
)
auxRamanIfTxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanIfTxPort.setStatus("current")
_AuxRamanIfRxPort_Type = PortNumber
_AuxRamanIfRxPort_Object = MibTableColumn
auxRamanIfRxPort = _AuxRamanIfRxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 7),
    _AuxRamanIfRxPort_Type()
)
auxRamanIfRxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanIfRxPort.setStatus("current")


class _AuxRamanIfInvPhysIndexOrZero_Type(Unsigned32):
    """Custom type auxRamanIfInvPhysIndexOrZero based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AuxRamanIfInvPhysIndexOrZero_Type.__name__ = "Unsigned32"
_AuxRamanIfInvPhysIndexOrZero_Object = MibTableColumn
auxRamanIfInvPhysIndexOrZero = _AuxRamanIfInvPhysIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 8),
    _AuxRamanIfInvPhysIndexOrZero_Type()
)
auxRamanIfInvPhysIndexOrZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanIfInvPhysIndexOrZero.setStatus("current")


class _AuxRamanIfAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type auxRamanIfAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 3


_AuxRamanIfAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_AuxRamanIfAdminStatus_Object = MibTableColumn
auxRamanIfAdminStatus = _AuxRamanIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 9),
    _AuxRamanIfAdminStatus_Type()
)
auxRamanIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxRamanIfAdminStatus.setStatus("current")


class _AuxRamanIfOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type auxRamanIfOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 1


_AuxRamanIfOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_AuxRamanIfOperStatus_Object = MibTableColumn
auxRamanIfOperStatus = _AuxRamanIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 10),
    _AuxRamanIfOperStatus_Type()
)
auxRamanIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanIfOperStatus.setStatus("current")
_AuxRamanIfObjectProperty_Type = ObjectProperty
_AuxRamanIfObjectProperty_Object = MibTableColumn
auxRamanIfObjectProperty = _AuxRamanIfObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 11),
    _AuxRamanIfObjectProperty_Type()
)
auxRamanIfObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanIfObjectProperty.setStatus("current")


class _AuxRamanIfModuleOperationMode_Type(Integer32):
    """Custom type auxRamanIfModuleOperationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("coPropagating", 1),
          ("counterPropagating", 2))
    )


_AuxRamanIfModuleOperationMode_Type.__name__ = "Integer32"
_AuxRamanIfModuleOperationMode_Object = MibTableColumn
auxRamanIfModuleOperationMode = _AuxRamanIfModuleOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 12),
    _AuxRamanIfModuleOperationMode_Type()
)
auxRamanIfModuleOperationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanIfModuleOperationMode.setStatus("current")


class _AuxRamanIfPumpsOperationMode_Type(Integer32):
    """Custom type auxRamanIfPumpsOperationMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("maxPumpsPower", 1),
          ("manualPumpsPower", 2),
          ("automaticalGainControl", 3))
    )


_AuxRamanIfPumpsOperationMode_Type.__name__ = "Integer32"
_AuxRamanIfPumpsOperationMode_Object = MibTableColumn
auxRamanIfPumpsOperationMode = _AuxRamanIfPumpsOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 13),
    _AuxRamanIfPumpsOperationMode_Type()
)
auxRamanIfPumpsOperationMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    auxRamanIfPumpsOperationMode.setStatus("current")
_AuxRamanIfPumpsOperationModeConfig_Type = CommandString
_AuxRamanIfPumpsOperationModeConfig_Object = MibTableColumn
auxRamanIfPumpsOperationModeConfig = _AuxRamanIfPumpsOperationModeConfig_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 14),
    _AuxRamanIfPumpsOperationModeConfig_Type()
)
auxRamanIfPumpsOperationModeConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanIfPumpsOperationModeConfig.setStatus("current")


class _AuxRamanIfLineFiberType_Type(Integer32):
    """Custom type auxRamanIfLineFiberType based on Integer32"""
    defaultValue = 1

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
        *(("ftSMF", 1),
          ("ftLeaf", 2),
          ("ftTrueWave", 3),
          ("ftG654", 4),
          ("ftTeralight", 5),
          ("ftG653", 6))
    )


_AuxRamanIfLineFiberType_Type.__name__ = "Integer32"
_AuxRamanIfLineFiberType_Object = MibTableColumn
auxRamanIfLineFiberType = _AuxRamanIfLineFiberType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 15),
    _AuxRamanIfLineFiberType_Type()
)
auxRamanIfLineFiberType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxRamanIfLineFiberType.setStatus("current")


class _AuxRamanIfAutoRestartProcTime_Type(Unsigned32):
    """Custom type auxRamanIfAutoRestartProcTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AuxRamanIfAutoRestartProcTime_Type.__name__ = "Unsigned32"
_AuxRamanIfAutoRestartProcTime_Object = MibTableColumn
auxRamanIfAutoRestartProcTime = _AuxRamanIfAutoRestartProcTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 16),
    _AuxRamanIfAutoRestartProcTime_Type()
)
auxRamanIfAutoRestartProcTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxRamanIfAutoRestartProcTime.setStatus("current")


class _AuxRamanIfArpPauseStatus_Type(Integer32):
    """Custom type auxRamanIfArpPauseStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("pause", 2))
    )


_AuxRamanIfArpPauseStatus_Type.__name__ = "Integer32"
_AuxRamanIfArpPauseStatus_Object = MibTableColumn
auxRamanIfArpPauseStatus = _AuxRamanIfArpPauseStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 17),
    _AuxRamanIfArpPauseStatus_Type()
)
auxRamanIfArpPauseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanIfArpPauseStatus.setStatus("current")


class _AuxRamanIfPumpsStatus_Type(Integer32):
    """Custom type auxRamanIfPumpsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("shutdown", 1),
          ("active", 2))
    )


_AuxRamanIfPumpsStatus_Type.__name__ = "Integer32"
_AuxRamanIfPumpsStatus_Object = MibTableColumn
auxRamanIfPumpsStatus = _AuxRamanIfPumpsStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 18),
    _AuxRamanIfPumpsStatus_Type()
)
auxRamanIfPumpsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanIfPumpsStatus.setStatus("current")
_AuxRamanIfTotalPumpsPower_Type = Integer32
_AuxRamanIfTotalPumpsPower_Object = MibTableColumn
auxRamanIfTotalPumpsPower = _AuxRamanIfTotalPumpsPower_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 19),
    _AuxRamanIfTotalPumpsPower_Type()
)
auxRamanIfTotalPumpsPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanIfTotalPumpsPower.setStatus("current")


class _AuxRamanIfPump1WantedPower_Type(Unsigned32):
    """Custom type auxRamanIfPump1WantedPower based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 4000),
    )


_AuxRamanIfPump1WantedPower_Type.__name__ = "Unsigned32"
_AuxRamanIfPump1WantedPower_Object = MibTableColumn
auxRamanIfPump1WantedPower = _AuxRamanIfPump1WantedPower_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 20),
    _AuxRamanIfPump1WantedPower_Type()
)
auxRamanIfPump1WantedPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxRamanIfPump1WantedPower.setStatus("current")
_AuxRamanIfPump1ActualPower_Type = Integer32
_AuxRamanIfPump1ActualPower_Object = MibTableColumn
auxRamanIfPump1ActualPower = _AuxRamanIfPump1ActualPower_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 21),
    _AuxRamanIfPump1ActualPower_Type()
)
auxRamanIfPump1ActualPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanIfPump1ActualPower.setStatus("current")
_AuxRamanIfPump1Current_Type = Unsigned32
_AuxRamanIfPump1Current_Object = MibTableColumn
auxRamanIfPump1Current = _AuxRamanIfPump1Current_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 22),
    _AuxRamanIfPump1Current_Type()
)
auxRamanIfPump1Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanIfPump1Current.setStatus("current")
_AuxRamanIfPump1Temperature_Type = Integer32
_AuxRamanIfPump1Temperature_Object = MibTableColumn
auxRamanIfPump1Temperature = _AuxRamanIfPump1Temperature_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 23),
    _AuxRamanIfPump1Temperature_Type()
)
auxRamanIfPump1Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanIfPump1Temperature.setStatus("current")


class _AuxRamanIfPump2WantedPower_Type(Unsigned32):
    """Custom type auxRamanIfPump2WantedPower based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 4000),
    )


_AuxRamanIfPump2WantedPower_Type.__name__ = "Unsigned32"
_AuxRamanIfPump2WantedPower_Object = MibTableColumn
auxRamanIfPump2WantedPower = _AuxRamanIfPump2WantedPower_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 24),
    _AuxRamanIfPump2WantedPower_Type()
)
auxRamanIfPump2WantedPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxRamanIfPump2WantedPower.setStatus("current")
_AuxRamanIfPump2ActualPower_Type = Integer32
_AuxRamanIfPump2ActualPower_Object = MibTableColumn
auxRamanIfPump2ActualPower = _AuxRamanIfPump2ActualPower_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 25),
    _AuxRamanIfPump2ActualPower_Type()
)
auxRamanIfPump2ActualPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanIfPump2ActualPower.setStatus("current")
_AuxRamanIfPump2Current_Type = Unsigned32
_AuxRamanIfPump2Current_Object = MibTableColumn
auxRamanIfPump2Current = _AuxRamanIfPump2Current_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 26),
    _AuxRamanIfPump2Current_Type()
)
auxRamanIfPump2Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanIfPump2Current.setStatus("current")
_AuxRamanIfPump2Temperature_Type = Integer32
_AuxRamanIfPump2Temperature_Object = MibTableColumn
auxRamanIfPump2Temperature = _AuxRamanIfPump2Temperature_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 27),
    _AuxRamanIfPump2Temperature_Type()
)
auxRamanIfPump2Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanIfPump2Temperature.setStatus("current")


class _AuxRamanIfWantedGain_Type(Unsigned32):
    """Custom type auxRamanIfWantedGain based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 200),
    )


_AuxRamanIfWantedGain_Type.__name__ = "Unsigned32"
_AuxRamanIfWantedGain_Object = MibTableColumn
auxRamanIfWantedGain = _AuxRamanIfWantedGain_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 28),
    _AuxRamanIfWantedGain_Type()
)
auxRamanIfWantedGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxRamanIfWantedGain.setStatus("current")
_AuxRamanIfActualGain_Type = Unsigned32
_AuxRamanIfActualGain_Object = MibTableColumn
auxRamanIfActualGain = _AuxRamanIfActualGain_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 29),
    _AuxRamanIfActualGain_Type()
)
auxRamanIfActualGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanIfActualGain.setStatus("current")
_AuxRamanIfReceivedPowerLevel_Type = Integer32
_AuxRamanIfReceivedPowerLevel_Object = MibTableColumn
auxRamanIfReceivedPowerLevel = _AuxRamanIfReceivedPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 30),
    _AuxRamanIfReceivedPowerLevel_Type()
)
auxRamanIfReceivedPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanIfReceivedPowerLevel.setStatus("current")
_AuxRamanIfReflectionPowerLevel_Type = Integer32
_AuxRamanIfReflectionPowerLevel_Object = MibTableColumn
auxRamanIfReflectionPowerLevel = _AuxRamanIfReflectionPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 31),
    _AuxRamanIfReflectionPowerLevel_Type()
)
auxRamanIfReflectionPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanIfReflectionPowerLevel.setStatus("current")
_AuxRamanIfReflectionPowerRatio_Type = Integer32
_AuxRamanIfReflectionPowerRatio_Object = MibTableColumn
auxRamanIfReflectionPowerRatio = _AuxRamanIfReflectionPowerRatio_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 32),
    _AuxRamanIfReflectionPowerRatio_Type()
)
auxRamanIfReflectionPowerRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanIfReflectionPowerRatio.setStatus("current")
_AuxRamanIf1510BandReceivedPowerLevel_Type = Integer32
_AuxRamanIf1510BandReceivedPowerLevel_Object = MibTableColumn
auxRamanIf1510BandReceivedPowerLevel = _AuxRamanIf1510BandReceivedPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 33),
    _AuxRamanIf1510BandReceivedPowerLevel_Type()
)
auxRamanIf1510BandReceivedPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanIf1510BandReceivedPowerLevel.setStatus("current")
_AuxRamanIfOscReceivedPowerLevel_Type = Integer32
_AuxRamanIfOscReceivedPowerLevel_Object = MibTableColumn
auxRamanIfOscReceivedPowerLevel = _AuxRamanIfOscReceivedPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 34),
    _AuxRamanIfOscReceivedPowerLevel_Type()
)
auxRamanIfOscReceivedPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanIfOscReceivedPowerLevel.setStatus("current")


class _AuxRamanIfAPRState_Type(Integer32):
    """Custom type auxRamanIfAPRState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("shutdown", 2))
    )


_AuxRamanIfAPRState_Type.__name__ = "Integer32"
_AuxRamanIfAPRState_Object = MibTableColumn
auxRamanIfAPRState = _AuxRamanIfAPRState_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 35),
    _AuxRamanIfAPRState_Type()
)
auxRamanIfAPRState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanIfAPRState.setStatus("current")


class _AuxRamanIfOscDitherState_Type(Integer32):
    """Custom type auxRamanIfOscDitherState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("lost", 2))
    )


_AuxRamanIfOscDitherState_Type.__name__ = "Integer32"
_AuxRamanIfOscDitherState_Object = MibTableColumn
auxRamanIfOscDitherState = _AuxRamanIfOscDitherState_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 36),
    _AuxRamanIfOscDitherState_Type()
)
auxRamanIfOscDitherState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanIfOscDitherState.setStatus("current")
_AuxRamanIfLineLossOfSignal_Type = FaultStatus
_AuxRamanIfLineLossOfSignal_Object = MibTableColumn
auxRamanIfLineLossOfSignal = _AuxRamanIfLineLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 37),
    _AuxRamanIfLineLossOfSignal_Type()
)
auxRamanIfLineLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanIfLineLossOfSignal.setStatus("current")
_AuxRamanIfOscDitherLos_Type = FaultStatus
_AuxRamanIfOscDitherLos_Object = MibTableColumn
auxRamanIfOscDitherLos = _AuxRamanIfOscDitherLos_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 38),
    _AuxRamanIfOscDitherLos_Type()
)
auxRamanIfOscDitherLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanIfOscDitherLos.setStatus("current")
_AuxRamanIfHighBackReflection_Type = FaultStatus
_AuxRamanIfHighBackReflection_Object = MibTableColumn
auxRamanIfHighBackReflection = _AuxRamanIfHighBackReflection_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 39),
    _AuxRamanIfHighBackReflection_Type()
)
auxRamanIfHighBackReflection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanIfHighBackReflection.setStatus("current")
_AuxRamanIfHighLineOutputPower_Type = FaultStatus
_AuxRamanIfHighLineOutputPower_Object = MibTableColumn
auxRamanIfHighLineOutputPower = _AuxRamanIfHighLineOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 40),
    _AuxRamanIfHighLineOutputPower_Type()
)
auxRamanIfHighLineOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanIfHighLineOutputPower.setStatus("current")
_AuxRamanIfLowLineOutputPower_Type = FaultStatus
_AuxRamanIfLowLineOutputPower_Object = MibTableColumn
auxRamanIfLowLineOutputPower = _AuxRamanIfLowLineOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 41),
    _AuxRamanIfLowLineOutputPower_Type()
)
auxRamanIfLowLineOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanIfLowLineOutputPower.setStatus("current")
_AuxRamanIfModuleTempTooHigh_Type = FaultStatus
_AuxRamanIfModuleTempTooHigh_Object = MibTableColumn
auxRamanIfModuleTempTooHigh = _AuxRamanIfModuleTempTooHigh_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 42),
    _AuxRamanIfModuleTempTooHigh_Type()
)
auxRamanIfModuleTempTooHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanIfModuleTempTooHigh.setStatus("current")
_AuxRamanIfModuleTempHigh_Type = FaultStatus
_AuxRamanIfModuleTempHigh_Object = MibTableColumn
auxRamanIfModuleTempHigh = _AuxRamanIfModuleTempHigh_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 43),
    _AuxRamanIfModuleTempHigh_Type()
)
auxRamanIfModuleTempHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanIfModuleTempHigh.setStatus("current")
_AuxRamanIfPumpsTempTooHigh_Type = FaultStatus
_AuxRamanIfPumpsTempTooHigh_Object = MibTableColumn
auxRamanIfPumpsTempTooHigh = _AuxRamanIfPumpsTempTooHigh_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 44),
    _AuxRamanIfPumpsTempTooHigh_Type()
)
auxRamanIfPumpsTempTooHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanIfPumpsTempTooHigh.setStatus("current")
_AuxRamanIfPumpsTempHigh_Type = FaultStatus
_AuxRamanIfPumpsTempHigh_Object = MibTableColumn
auxRamanIfPumpsTempHigh = _AuxRamanIfPumpsTempHigh_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 45),
    _AuxRamanIfPumpsTempHigh_Type()
)
auxRamanIfPumpsTempHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanIfPumpsTempHigh.setStatus("current")
_AuxRamanIfAprShutdown_Type = FaultStatus
_AuxRamanIfAprShutdown_Object = MibTableColumn
auxRamanIfAprShutdown = _AuxRamanIfAprShutdown_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 46),
    _AuxRamanIfAprShutdown_Type()
)
auxRamanIfAprShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanIfAprShutdown.setStatus("current")
_AuxRamanIfLineFiberDeteriorated_Type = FaultStatus
_AuxRamanIfLineFiberDeteriorated_Object = MibTableColumn
auxRamanIfLineFiberDeteriorated = _AuxRamanIfLineFiberDeteriorated_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 47),
    _AuxRamanIfLineFiberDeteriorated_Type()
)
auxRamanIfLineFiberDeteriorated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanIfLineFiberDeteriorated.setStatus("current")
_AuxRamanIf1510BandPowerLos_Type = FaultStatus
_AuxRamanIf1510BandPowerLos_Object = MibTableColumn
auxRamanIf1510BandPowerLos = _AuxRamanIf1510BandPowerLos_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 48),
    _AuxRamanIf1510BandPowerLos_Type()
)
auxRamanIf1510BandPowerLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanIf1510BandPowerLos.setStatus("current")
_AuxRamanIfManualRestartTrial_Type = CommandString
_AuxRamanIfManualRestartTrial_Object = MibTableColumn
auxRamanIfManualRestartTrial = _AuxRamanIfManualRestartTrial_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 49),
    _AuxRamanIfManualRestartTrial_Type()
)
auxRamanIfManualRestartTrial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanIfManualRestartTrial.setStatus("current")
_AuxRamanIfModuleTemp_Type = Integer32
_AuxRamanIfModuleTemp_Object = MibTableColumn
auxRamanIfModuleTemp = _AuxRamanIfModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 50),
    _AuxRamanIfModuleTemp_Type()
)
auxRamanIfModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanIfModuleTemp.setStatus("current")


class _AuxRamanIfTxSignalStatus_Type(Integer32):
    """Custom type auxRamanIfTxSignalStatus based on Integer32"""
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
        *(("down", 1),
          ("degraded", 2),
          ("up", 3))
    )


_AuxRamanIfTxSignalStatus_Type.__name__ = "Integer32"
_AuxRamanIfTxSignalStatus_Object = MibTableColumn
auxRamanIfTxSignalStatus = _AuxRamanIfTxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 51),
    _AuxRamanIfTxSignalStatus_Type()
)
auxRamanIfTxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanIfTxSignalStatus.setStatus("current")


class _AuxRamanIfRxSignalStatus_Type(Integer32):
    """Custom type auxRamanIfRxSignalStatus based on Integer32"""
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
        *(("down", 1),
          ("degraded", 2),
          ("up", 3))
    )


_AuxRamanIfRxSignalStatus_Type.__name__ = "Integer32"
_AuxRamanIfRxSignalStatus_Object = MibTableColumn
auxRamanIfRxSignalStatus = _AuxRamanIfRxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 5, 1, 1, 52),
    _AuxRamanIfRxSignalStatus_Type()
)
auxRamanIfRxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanIfRxSignalStatus.setStatus("current")
_AuxRamanSafetyList_ObjectIdentity = ObjectIdentity
auxRamanSafetyList = _AuxRamanSafetyList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 6)
)
_AuxRamanSafetyTable_Object = MibTable
auxRamanSafetyTable = _AuxRamanSafetyTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 6, 1)
)
if mibBuilder.loadTexts:
    auxRamanSafetyTable.setStatus("current")
_AuxRamanSafetyEntry_Object = MibTableRow
auxRamanSafetyEntry = _AuxRamanSafetyEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 6, 1, 1)
)
auxRamanSafetyEntry.setIndexNames(
    (0, "LUM-AUX-MIB", "auxRamanSafetyIndex"),
)
if mibBuilder.loadTexts:
    auxRamanSafetyEntry.setStatus("current")


class _AuxRamanSafetyIndex_Type(Unsigned32):
    """Custom type auxRamanSafetyIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AuxRamanSafetyIndex_Type.__name__ = "Unsigned32"
_AuxRamanSafetyIndex_Object = MibTableColumn
auxRamanSafetyIndex = _AuxRamanSafetyIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 6, 1, 1, 1),
    _AuxRamanSafetyIndex_Type()
)
auxRamanSafetyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanSafetyIndex.setStatus("current")
_AuxRamanSafetyName_Type = MgmtNameString
_AuxRamanSafetyName_Object = MibTableColumn
auxRamanSafetyName = _AuxRamanSafetyName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 6, 1, 1, 2),
    _AuxRamanSafetyName_Type()
)
auxRamanSafetyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanSafetyName.setStatus("current")


class _AuxRamanSafetyDescr_Type(DisplayString):
    """Custom type auxRamanSafetyDescr based on DisplayString"""
    defaultValue = OctetString("")


_AuxRamanSafetyDescr_Type.__name__ = "DisplayString"
_AuxRamanSafetyDescr_Object = MibTableColumn
auxRamanSafetyDescr = _AuxRamanSafetyDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 6, 1, 1, 3),
    _AuxRamanSafetyDescr_Type()
)
auxRamanSafetyDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxRamanSafetyDescr.setStatus("current")
_AuxRamanSafetySubrack_Type = SubrackNumber
_AuxRamanSafetySubrack_Object = MibTableColumn
auxRamanSafetySubrack = _AuxRamanSafetySubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 6, 1, 1, 4),
    _AuxRamanSafetySubrack_Type()
)
auxRamanSafetySubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanSafetySubrack.setStatus("current")
_AuxRamanSafetySlot_Type = SlotNumber
_AuxRamanSafetySlot_Object = MibTableColumn
auxRamanSafetySlot = _AuxRamanSafetySlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 6, 1, 1, 5),
    _AuxRamanSafetySlot_Type()
)
auxRamanSafetySlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanSafetySlot.setStatus("current")
_AuxRamanSafetyTxPort_Type = PortNumber
_AuxRamanSafetyTxPort_Object = MibTableColumn
auxRamanSafetyTxPort = _AuxRamanSafetyTxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 6, 1, 1, 6),
    _AuxRamanSafetyTxPort_Type()
)
auxRamanSafetyTxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanSafetyTxPort.setStatus("current")
_AuxRamanSafetyRxPort_Type = PortNumber
_AuxRamanSafetyRxPort_Object = MibTableColumn
auxRamanSafetyRxPort = _AuxRamanSafetyRxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 6, 1, 1, 7),
    _AuxRamanSafetyRxPort_Type()
)
auxRamanSafetyRxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanSafetyRxPort.setStatus("current")


class _AuxRamanSafetyInvPhysIndexOrZero_Type(Unsigned32):
    """Custom type auxRamanSafetyInvPhysIndexOrZero based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AuxRamanSafetyInvPhysIndexOrZero_Type.__name__ = "Unsigned32"
_AuxRamanSafetyInvPhysIndexOrZero_Object = MibTableColumn
auxRamanSafetyInvPhysIndexOrZero = _AuxRamanSafetyInvPhysIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 6, 1, 1, 8),
    _AuxRamanSafetyInvPhysIndexOrZero_Type()
)
auxRamanSafetyInvPhysIndexOrZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanSafetyInvPhysIndexOrZero.setStatus("current")
_AuxRamanSafetyObjectProperty_Type = ObjectProperty
_AuxRamanSafetyObjectProperty_Object = MibTableColumn
auxRamanSafetyObjectProperty = _AuxRamanSafetyObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 6, 1, 1, 9),
    _AuxRamanSafetyObjectProperty_Type()
)
auxRamanSafetyObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanSafetyObjectProperty.setStatus("current")


class _AuxRamanSafetyShutDownAtInputLoss_Type(Integer32):
    """Custom type auxRamanSafetyShutDownAtInputLoss based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AuxRamanSafetyShutDownAtInputLoss_Type.__name__ = "Integer32"
_AuxRamanSafetyShutDownAtInputLoss_Object = MibTableColumn
auxRamanSafetyShutDownAtInputLoss = _AuxRamanSafetyShutDownAtInputLoss_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 6, 1, 1, 10),
    _AuxRamanSafetyShutDownAtInputLoss_Type()
)
auxRamanSafetyShutDownAtInputLoss.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    auxRamanSafetyShutDownAtInputLoss.setStatus("current")


class _AuxRamanSafetyShutDownAtHighTemp_Type(Integer32):
    """Custom type auxRamanSafetyShutDownAtHighTemp based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AuxRamanSafetyShutDownAtHighTemp_Type.__name__ = "Integer32"
_AuxRamanSafetyShutDownAtHighTemp_Object = MibTableColumn
auxRamanSafetyShutDownAtHighTemp = _AuxRamanSafetyShutDownAtHighTemp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 6, 1, 1, 11),
    _AuxRamanSafetyShutDownAtHighTemp_Type()
)
auxRamanSafetyShutDownAtHighTemp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    auxRamanSafetyShutDownAtHighTemp.setStatus("current")


class _AuxRamanSafetyShutDownAtHighBackReflection_Type(Integer32):
    """Custom type auxRamanSafetyShutDownAtHighBackReflection based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AuxRamanSafetyShutDownAtHighBackReflection_Type.__name__ = "Integer32"
_AuxRamanSafetyShutDownAtHighBackReflection_Object = MibTableColumn
auxRamanSafetyShutDownAtHighBackReflection = _AuxRamanSafetyShutDownAtHighBackReflection_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 6, 1, 1, 12),
    _AuxRamanSafetyShutDownAtHighBackReflection_Type()
)
auxRamanSafetyShutDownAtHighBackReflection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    auxRamanSafetyShutDownAtHighBackReflection.setStatus("current")


class _AuxRamanSafetyHighBackReflectionThreshold_Type(Integer32):
    """Custom type auxRamanSafetyHighBackReflectionThreshold based on Integer32"""
    defaultValue = -22

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-28, -19),
    )


_AuxRamanSafetyHighBackReflectionThreshold_Type.__name__ = "Integer32"
_AuxRamanSafetyHighBackReflectionThreshold_Object = MibTableColumn
auxRamanSafetyHighBackReflectionThreshold = _AuxRamanSafetyHighBackReflectionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 6, 1, 1, 13),
    _AuxRamanSafetyHighBackReflectionThreshold_Type()
)
auxRamanSafetyHighBackReflectionThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxRamanSafetyHighBackReflectionThreshold.setStatus("current")


class _AuxRamanSafetyShutDownAtOscLoss_Type(Integer32):
    """Custom type auxRamanSafetyShutDownAtOscLoss based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AuxRamanSafetyShutDownAtOscLoss_Type.__name__ = "Integer32"
_AuxRamanSafetyShutDownAtOscLoss_Object = MibTableColumn
auxRamanSafetyShutDownAtOscLoss = _AuxRamanSafetyShutDownAtOscLoss_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 6, 1, 1, 14),
    _AuxRamanSafetyShutDownAtOscLoss_Type()
)
auxRamanSafetyShutDownAtOscLoss.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    auxRamanSafetyShutDownAtOscLoss.setStatus("current")


class _AuxRamanSafetyShutDownAt1510BandDrop_Type(Integer32):
    """Custom type auxRamanSafetyShutDownAt1510BandDrop based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AuxRamanSafetyShutDownAt1510BandDrop_Type.__name__ = "Integer32"
_AuxRamanSafetyShutDownAt1510BandDrop_Object = MibTableColumn
auxRamanSafetyShutDownAt1510BandDrop = _AuxRamanSafetyShutDownAt1510BandDrop_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 6, 1, 1, 15),
    _AuxRamanSafetyShutDownAt1510BandDrop_Type()
)
auxRamanSafetyShutDownAt1510BandDrop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    auxRamanSafetyShutDownAt1510BandDrop.setStatus("current")
_AuxRamanSafetyShutDownAtInputLossConfig_Type = CommandString
_AuxRamanSafetyShutDownAtInputLossConfig_Object = MibTableColumn
auxRamanSafetyShutDownAtInputLossConfig = _AuxRamanSafetyShutDownAtInputLossConfig_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 6, 1, 1, 16),
    _AuxRamanSafetyShutDownAtInputLossConfig_Type()
)
auxRamanSafetyShutDownAtInputLossConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanSafetyShutDownAtInputLossConfig.setStatus("current")
_AuxRamanSafetyShutDownAtHighTempConfig_Type = CommandString
_AuxRamanSafetyShutDownAtHighTempConfig_Object = MibTableColumn
auxRamanSafetyShutDownAtHighTempConfig = _AuxRamanSafetyShutDownAtHighTempConfig_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 6, 1, 1, 17),
    _AuxRamanSafetyShutDownAtHighTempConfig_Type()
)
auxRamanSafetyShutDownAtHighTempConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanSafetyShutDownAtHighTempConfig.setStatus("current")
_AuxRamanSafetyShutDownAtHighBackReflectionConfig_Type = CommandString
_AuxRamanSafetyShutDownAtHighBackReflectionConfig_Object = MibTableColumn
auxRamanSafetyShutDownAtHighBackReflectionConfig = _AuxRamanSafetyShutDownAtHighBackReflectionConfig_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 6, 1, 1, 18),
    _AuxRamanSafetyShutDownAtHighBackReflectionConfig_Type()
)
auxRamanSafetyShutDownAtHighBackReflectionConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanSafetyShutDownAtHighBackReflectionConfig.setStatus("current")
_AuxRamanSafetyShutDownAtOscLossConfig_Type = CommandString
_AuxRamanSafetyShutDownAtOscLossConfig_Object = MibTableColumn
auxRamanSafetyShutDownAtOscLossConfig = _AuxRamanSafetyShutDownAtOscLossConfig_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 6, 1, 1, 19),
    _AuxRamanSafetyShutDownAtOscLossConfig_Type()
)
auxRamanSafetyShutDownAtOscLossConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanSafetyShutDownAtOscLossConfig.setStatus("current")
_AuxRamanSafetyShutDownAt1510BandDropConfig_Type = CommandString
_AuxRamanSafetyShutDownAt1510BandDropConfig_Object = MibTableColumn
auxRamanSafetyShutDownAt1510BandDropConfig = _AuxRamanSafetyShutDownAt1510BandDropConfig_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 6, 1, 1, 20),
    _AuxRamanSafetyShutDownAt1510BandDropConfig_Type()
)
auxRamanSafetyShutDownAt1510BandDropConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanSafetyShutDownAt1510BandDropConfig.setStatus("current")


class _AuxRamanSafetyPasswd_Type(DisplayString):
    """Custom type auxRamanSafetyPasswd based on DisplayString"""
    defaultValue = OctetString("-")


_AuxRamanSafetyPasswd_Type.__name__ = "DisplayString"
_AuxRamanSafetyPasswd_Object = MibTableColumn
auxRamanSafetyPasswd = _AuxRamanSafetyPasswd_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 6, 1, 1, 21),
    _AuxRamanSafetyPasswd_Type()
)
auxRamanSafetyPasswd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    auxRamanSafetyPasswd.setStatus("current")
_AuxRamanSafetyPasswdConfig_Type = CommandString
_AuxRamanSafetyPasswdConfig_Object = MibTableColumn
auxRamanSafetyPasswdConfig = _AuxRamanSafetyPasswdConfig_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 6, 1, 1, 22),
    _AuxRamanSafetyPasswdConfig_Type()
)
auxRamanSafetyPasswdConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanSafetyPasswdConfig.setStatus("current")


class _AuxRamanSafety1510BandDropThreshold_Type(Integer32):
    """Custom type auxRamanSafety1510BandDropThreshold based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_AuxRamanSafety1510BandDropThreshold_Type.__name__ = "Integer32"
_AuxRamanSafety1510BandDropThreshold_Object = MibTableColumn
auxRamanSafety1510BandDropThreshold = _AuxRamanSafety1510BandDropThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 6, 1, 1, 23),
    _AuxRamanSafety1510BandDropThreshold_Type()
)
auxRamanSafety1510BandDropThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxRamanSafety1510BandDropThreshold.setStatus("current")


class _AuxRamanSafetyInhibitStartAtOscLoss_Type(Integer32):
    """Custom type auxRamanSafetyInhibitStartAtOscLoss based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AuxRamanSafetyInhibitStartAtOscLoss_Type.__name__ = "Integer32"
_AuxRamanSafetyInhibitStartAtOscLoss_Object = MibTableColumn
auxRamanSafetyInhibitStartAtOscLoss = _AuxRamanSafetyInhibitStartAtOscLoss_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 6, 1, 1, 24),
    _AuxRamanSafetyInhibitStartAtOscLoss_Type()
)
auxRamanSafetyInhibitStartAtOscLoss.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    auxRamanSafetyInhibitStartAtOscLoss.setStatus("current")
_AuxRamanSafetyInhibitStartAtOscLossConfig_Type = CommandString
_AuxRamanSafetyInhibitStartAtOscLossConfig_Object = MibTableColumn
auxRamanSafetyInhibitStartAtOscLossConfig = _AuxRamanSafetyInhibitStartAtOscLossConfig_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 6, 1, 1, 25),
    _AuxRamanSafetyInhibitStartAtOscLossConfig_Type()
)
auxRamanSafetyInhibitStartAtOscLossConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanSafetyInhibitStartAtOscLossConfig.setStatus("current")


class _AuxRamanSafetyShutDownAtLowBandDrop_Type(Integer32):
    """Custom type auxRamanSafetyShutDownAtLowBandDrop based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AuxRamanSafetyShutDownAtLowBandDrop_Type.__name__ = "Integer32"
_AuxRamanSafetyShutDownAtLowBandDrop_Object = MibTableColumn
auxRamanSafetyShutDownAtLowBandDrop = _AuxRamanSafetyShutDownAtLowBandDrop_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 6, 1, 1, 26),
    _AuxRamanSafetyShutDownAtLowBandDrop_Type()
)
auxRamanSafetyShutDownAtLowBandDrop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    auxRamanSafetyShutDownAtLowBandDrop.setStatus("current")


class _AuxRamanSafetyLowBandScatteringThreshold_Type(Integer32):
    """Custom type auxRamanSafetyLowBandScatteringThreshold based on Integer32"""
    defaultValue = -370

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-450, -250),
    )


_AuxRamanSafetyLowBandScatteringThreshold_Type.__name__ = "Integer32"
_AuxRamanSafetyLowBandScatteringThreshold_Object = MibTableColumn
auxRamanSafetyLowBandScatteringThreshold = _AuxRamanSafetyLowBandScatteringThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 6, 1, 1, 27),
    _AuxRamanSafetyLowBandScatteringThreshold_Type()
)
auxRamanSafetyLowBandScatteringThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxRamanSafetyLowBandScatteringThreshold.setStatus("current")
_AuxRamanSafetyShutDownAtLowBandDropConfig_Type = CommandString
_AuxRamanSafetyShutDownAtLowBandDropConfig_Object = MibTableColumn
auxRamanSafetyShutDownAtLowBandDropConfig = _AuxRamanSafetyShutDownAtLowBandDropConfig_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 6, 1, 1, 28),
    _AuxRamanSafetyShutDownAtLowBandDropConfig_Type()
)
auxRamanSafetyShutDownAtLowBandDropConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanSafetyShutDownAtLowBandDropConfig.setStatus("current")


class _AuxRamanSafetyAmplifierSwitch_Type(Integer32):
    """Custom type auxRamanSafetyAmplifierSwitch based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AuxRamanSafetyAmplifierSwitch_Type.__name__ = "Integer32"
_AuxRamanSafetyAmplifierSwitch_Object = MibTableColumn
auxRamanSafetyAmplifierSwitch = _AuxRamanSafetyAmplifierSwitch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 6, 1, 1, 29),
    _AuxRamanSafetyAmplifierSwitch_Type()
)
auxRamanSafetyAmplifierSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    auxRamanSafetyAmplifierSwitch.setStatus("current")
_AuxRamanSafetyAmplifierSwitchConfig_Type = CommandString
_AuxRamanSafetyAmplifierSwitchConfig_Object = MibTableColumn
auxRamanSafetyAmplifierSwitchConfig = _AuxRamanSafetyAmplifierSwitchConfig_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 6, 1, 1, 30),
    _AuxRamanSafetyAmplifierSwitchConfig_Type()
)
auxRamanSafetyAmplifierSwitchConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxRamanSafetyAmplifierSwitchConfig.setStatus("current")


class _AuxRamanSafetyLowBandScatteringTolerance_Type(Integer32):
    """Custom type auxRamanSafetyLowBandScatteringTolerance based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 20),
    )


_AuxRamanSafetyLowBandScatteringTolerance_Type.__name__ = "Integer32"
_AuxRamanSafetyLowBandScatteringTolerance_Object = MibTableColumn
auxRamanSafetyLowBandScatteringTolerance = _AuxRamanSafetyLowBandScatteringTolerance_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 6, 1, 1, 31),
    _AuxRamanSafetyLowBandScatteringTolerance_Type()
)
auxRamanSafetyLowBandScatteringTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxRamanSafetyLowBandScatteringTolerance.setStatus("current")
_AuxPEIfList_ObjectIdentity = ObjectIdentity
auxPEIfList = _AuxPEIfList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 7)
)
_AuxPEIfTable_Object = MibTable
auxPEIfTable = _AuxPEIfTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 7, 1)
)
if mibBuilder.loadTexts:
    auxPEIfTable.setStatus("current")
_AuxPEIfEntry_Object = MibTableRow
auxPEIfEntry = _AuxPEIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 7, 1, 1)
)
auxPEIfEntry.setIndexNames(
    (0, "LUM-AUX-MIB", "auxPEIfIndex"),
)
if mibBuilder.loadTexts:
    auxPEIfEntry.setStatus("current")


class _AuxPEIfIndex_Type(Unsigned32):
    """Custom type auxPEIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AuxPEIfIndex_Type.__name__ = "Unsigned32"
_AuxPEIfIndex_Object = MibTableColumn
auxPEIfIndex = _AuxPEIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 7, 1, 1, 1),
    _AuxPEIfIndex_Type()
)
auxPEIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPEIfIndex.setStatus("current")
_AuxPEIfName_Type = MgmtNameString
_AuxPEIfName_Object = MibTableColumn
auxPEIfName = _AuxPEIfName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 7, 1, 1, 2),
    _AuxPEIfName_Type()
)
auxPEIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPEIfName.setStatus("current")


class _AuxPEIfDescr_Type(DisplayString):
    """Custom type auxPEIfDescr based on DisplayString"""
    defaultValue = OctetString("")


_AuxPEIfDescr_Type.__name__ = "DisplayString"
_AuxPEIfDescr_Object = MibTableColumn
auxPEIfDescr = _AuxPEIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 7, 1, 1, 3),
    _AuxPEIfDescr_Type()
)
auxPEIfDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxPEIfDescr.setStatus("current")
_AuxPEIfSubrack_Type = SubrackNumber
_AuxPEIfSubrack_Object = MibTableColumn
auxPEIfSubrack = _AuxPEIfSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 7, 1, 1, 4),
    _AuxPEIfSubrack_Type()
)
auxPEIfSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPEIfSubrack.setStatus("current")
_AuxPEIfSlot_Type = SlotNumber
_AuxPEIfSlot_Object = MibTableColumn
auxPEIfSlot = _AuxPEIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 7, 1, 1, 5),
    _AuxPEIfSlot_Type()
)
auxPEIfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPEIfSlot.setStatus("current")
_AuxPEIfTxPort_Type = PortNumber
_AuxPEIfTxPort_Object = MibTableColumn
auxPEIfTxPort = _AuxPEIfTxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 7, 1, 1, 6),
    _AuxPEIfTxPort_Type()
)
auxPEIfTxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPEIfTxPort.setStatus("current")
_AuxPEIfRxPort_Type = PortNumber
_AuxPEIfRxPort_Object = MibTableColumn
auxPEIfRxPort = _AuxPEIfRxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 7, 1, 1, 7),
    _AuxPEIfRxPort_Type()
)
auxPEIfRxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPEIfRxPort.setStatus("current")


class _AuxPEIfInvPhysIndexOrZero_Type(Unsigned32):
    """Custom type auxPEIfInvPhysIndexOrZero based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AuxPEIfInvPhysIndexOrZero_Type.__name__ = "Unsigned32"
_AuxPEIfInvPhysIndexOrZero_Object = MibTableColumn
auxPEIfInvPhysIndexOrZero = _AuxPEIfInvPhysIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 7, 1, 1, 8),
    _AuxPEIfInvPhysIndexOrZero_Type()
)
auxPEIfInvPhysIndexOrZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPEIfInvPhysIndexOrZero.setStatus("current")


class _AuxPEIfAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type auxPEIfAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 3


_AuxPEIfAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_AuxPEIfAdminStatus_Object = MibTableColumn
auxPEIfAdminStatus = _AuxPEIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 7, 1, 1, 9),
    _AuxPEIfAdminStatus_Type()
)
auxPEIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxPEIfAdminStatus.setStatus("current")


class _AuxPEIfOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type auxPEIfOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 1


_AuxPEIfOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_AuxPEIfOperStatus_Object = MibTableColumn
auxPEIfOperStatus = _AuxPEIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 7, 1, 1, 10),
    _AuxPEIfOperStatus_Type()
)
auxPEIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPEIfOperStatus.setStatus("current")
_AuxPEIfObjectProperty_Type = ObjectProperty
_AuxPEIfObjectProperty_Object = MibTableColumn
auxPEIfObjectProperty = _AuxPEIfObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 7, 1, 1, 11),
    _AuxPEIfObjectProperty_Type()
)
auxPEIfObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPEIfObjectProperty.setStatus("current")


class _AuxPEIfPumpsOperationMode_Type(Integer32):
    """Custom type auxPEIfPumpsOperationMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("constantPower", 1),
          ("constantGain", 2))
    )


_AuxPEIfPumpsOperationMode_Type.__name__ = "Integer32"
_AuxPEIfPumpsOperationMode_Object = MibTableColumn
auxPEIfPumpsOperationMode = _AuxPEIfPumpsOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 7, 1, 1, 12),
    _AuxPEIfPumpsOperationMode_Type()
)
auxPEIfPumpsOperationMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    auxPEIfPumpsOperationMode.setStatus("current")
_AuxPEIfPumpsOperationModeConfig_Type = CommandString
_AuxPEIfPumpsOperationModeConfig_Object = MibTableColumn
auxPEIfPumpsOperationModeConfig = _AuxPEIfPumpsOperationModeConfig_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 7, 1, 1, 13),
    _AuxPEIfPumpsOperationModeConfig_Type()
)
auxPEIfPumpsOperationModeConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPEIfPumpsOperationModeConfig.setStatus("current")


class _AuxPEIfAutoRestartProcTime_Type(Unsigned32):
    """Custom type auxPEIfAutoRestartProcTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AuxPEIfAutoRestartProcTime_Type.__name__ = "Unsigned32"
_AuxPEIfAutoRestartProcTime_Object = MibTableColumn
auxPEIfAutoRestartProcTime = _AuxPEIfAutoRestartProcTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 7, 1, 1, 14),
    _AuxPEIfAutoRestartProcTime_Type()
)
auxPEIfAutoRestartProcTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxPEIfAutoRestartProcTime.setStatus("current")


class _AuxPEIfPumpsStatus_Type(Integer32):
    """Custom type auxPEIfPumpsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("shutdown", 1),
          ("active", 2))
    )


_AuxPEIfPumpsStatus_Type.__name__ = "Integer32"
_AuxPEIfPumpsStatus_Object = MibTableColumn
auxPEIfPumpsStatus = _AuxPEIfPumpsStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 7, 1, 1, 15),
    _AuxPEIfPumpsStatus_Type()
)
auxPEIfPumpsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPEIfPumpsStatus.setStatus("current")


class _AuxPEIfWantedPower_Type(Integer32):
    """Custom type auxPEIfWantedPower based on Integer32"""
    defaultValue = 170

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 261),
    )


_AuxPEIfWantedPower_Type.__name__ = "Integer32"
_AuxPEIfWantedPower_Object = MibTableColumn
auxPEIfWantedPower = _AuxPEIfWantedPower_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 7, 1, 1, 16),
    _AuxPEIfWantedPower_Type()
)
auxPEIfWantedPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxPEIfWantedPower.setStatus("current")


class _AuxPEIfWantedGain_Type(Unsigned32):
    """Custom type auxPEIfWantedGain based on Unsigned32"""
    defaultValue = 62

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 90),
    )


_AuxPEIfWantedGain_Type.__name__ = "Unsigned32"
_AuxPEIfWantedGain_Object = MibTableColumn
auxPEIfWantedGain = _AuxPEIfWantedGain_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 7, 1, 1, 17),
    _AuxPEIfWantedGain_Type()
)
auxPEIfWantedGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxPEIfWantedGain.setStatus("current")
_AuxPEIfPumpsTotalCurrent_Type = Unsigned32
_AuxPEIfPumpsTotalCurrent_Object = MibTableColumn
auxPEIfPumpsTotalCurrent = _AuxPEIfPumpsTotalCurrent_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 7, 1, 1, 18),
    _AuxPEIfPumpsTotalCurrent_Type()
)
auxPEIfPumpsTotalCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPEIfPumpsTotalCurrent.setStatus("current")
_AuxPEIfPump1Temperature_Type = Integer32
_AuxPEIfPump1Temperature_Object = MibTableColumn
auxPEIfPump1Temperature = _AuxPEIfPump1Temperature_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 7, 1, 1, 19),
    _AuxPEIfPump1Temperature_Type()
)
auxPEIfPump1Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPEIfPump1Temperature.setStatus("current")
_AuxPEIfActualGain_Type = Integer32
_AuxPEIfActualGain_Object = MibTableColumn
auxPEIfActualGain = _AuxPEIfActualGain_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 7, 1, 1, 20),
    _AuxPEIfActualGain_Type()
)
auxPEIfActualGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPEIfActualGain.setStatus("current")
_AuxPEIfReceivedPowerLevel_Type = Integer32
_AuxPEIfReceivedPowerLevel_Object = MibTableColumn
auxPEIfReceivedPowerLevel = _AuxPEIfReceivedPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 7, 1, 1, 21),
    _AuxPEIfReceivedPowerLevel_Type()
)
auxPEIfReceivedPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPEIfReceivedPowerLevel.setStatus("current")
_AuxPEIfCombinedOutPwrLevel_Type = Integer32
_AuxPEIfCombinedOutPwrLevel_Object = MibTableColumn
auxPEIfCombinedOutPwrLevel = _AuxPEIfCombinedOutPwrLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 7, 1, 1, 22),
    _AuxPEIfCombinedOutPwrLevel_Type()
)
auxPEIfCombinedOutPwrLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPEIfCombinedOutPwrLevel.setStatus("current")
_AuxPEIfReflectionPowerLevel_Type = Integer32
_AuxPEIfReflectionPowerLevel_Object = MibTableColumn
auxPEIfReflectionPowerLevel = _AuxPEIfReflectionPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 7, 1, 1, 23),
    _AuxPEIfReflectionPowerLevel_Type()
)
auxPEIfReflectionPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPEIfReflectionPowerLevel.setStatus("current")
_AuxPEIfReflectionPowerRatio_Type = Integer32
_AuxPEIfReflectionPowerRatio_Object = MibTableColumn
auxPEIfReflectionPowerRatio = _AuxPEIfReflectionPowerRatio_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 7, 1, 1, 24),
    _AuxPEIfReflectionPowerRatio_Type()
)
auxPEIfReflectionPowerRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPEIfReflectionPowerRatio.setStatus("current")
_AuxPEIfLowBandScatteredPowerLevel_Type = Integer32
_AuxPEIfLowBandScatteredPowerLevel_Object = MibTableColumn
auxPEIfLowBandScatteredPowerLevel = _AuxPEIfLowBandScatteredPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 7, 1, 1, 25),
    _AuxPEIfLowBandScatteredPowerLevel_Type()
)
auxPEIfLowBandScatteredPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPEIfLowBandScatteredPowerLevel.setStatus("current")
_AuxPEIfLineLossOfSignal_Type = FaultStatus
_AuxPEIfLineLossOfSignal_Object = MibTableColumn
auxPEIfLineLossOfSignal = _AuxPEIfLineLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 7, 1, 1, 26),
    _AuxPEIfLineLossOfSignal_Type()
)
auxPEIfLineLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPEIfLineLossOfSignal.setStatus("current")
_AuxPEIfHighBackReflection_Type = FaultStatus
_AuxPEIfHighBackReflection_Object = MibTableColumn
auxPEIfHighBackReflection = _AuxPEIfHighBackReflection_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 7, 1, 1, 27),
    _AuxPEIfHighBackReflection_Type()
)
auxPEIfHighBackReflection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPEIfHighBackReflection.setStatus("current")
_AuxPEIfAutoPowerReduction_Type = FaultStatus
_AuxPEIfAutoPowerReduction_Object = MibTableColumn
auxPEIfAutoPowerReduction = _AuxPEIfAutoPowerReduction_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 7, 1, 1, 28),
    _AuxPEIfAutoPowerReduction_Type()
)
auxPEIfAutoPowerReduction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPEIfAutoPowerReduction.setStatus("current")
_AuxPEIfLowLineOutputPower_Type = FaultStatus
_AuxPEIfLowLineOutputPower_Object = MibTableColumn
auxPEIfLowLineOutputPower = _AuxPEIfLowLineOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 7, 1, 1, 29),
    _AuxPEIfLowLineOutputPower_Type()
)
auxPEIfLowLineOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPEIfLowLineOutputPower.setStatus("current")
_AuxPEIfModuleTempTooHigh_Type = FaultStatus
_AuxPEIfModuleTempTooHigh_Object = MibTableColumn
auxPEIfModuleTempTooHigh = _AuxPEIfModuleTempTooHigh_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 7, 1, 1, 30),
    _AuxPEIfModuleTempTooHigh_Type()
)
auxPEIfModuleTempTooHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPEIfModuleTempTooHigh.setStatus("current")
_AuxPEIfModuleTempHigh_Type = FaultStatus
_AuxPEIfModuleTempHigh_Object = MibTableColumn
auxPEIfModuleTempHigh = _AuxPEIfModuleTempHigh_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 7, 1, 1, 31),
    _AuxPEIfModuleTempHigh_Type()
)
auxPEIfModuleTempHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPEIfModuleTempHigh.setStatus("current")
_AuxPEIfPumpsTempTooHigh_Type = FaultStatus
_AuxPEIfPumpsTempTooHigh_Object = MibTableColumn
auxPEIfPumpsTempTooHigh = _AuxPEIfPumpsTempTooHigh_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 7, 1, 1, 32),
    _AuxPEIfPumpsTempTooHigh_Type()
)
auxPEIfPumpsTempTooHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPEIfPumpsTempTooHigh.setStatus("current")
_AuxPEIfPumpsTempHigh_Type = FaultStatus
_AuxPEIfPumpsTempHigh_Object = MibTableColumn
auxPEIfPumpsTempHigh = _AuxPEIfPumpsTempHigh_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 7, 1, 1, 33),
    _AuxPEIfPumpsTempHigh_Type()
)
auxPEIfPumpsTempHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPEIfPumpsTempHigh.setStatus("current")
_AuxPEIfModuleTemp_Type = Integer32
_AuxPEIfModuleTemp_Object = MibTableColumn
auxPEIfModuleTemp = _AuxPEIfModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 7, 1, 1, 34),
    _AuxPEIfModuleTemp_Type()
)
auxPEIfModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPEIfModuleTemp.setStatus("current")
_AuxPEIfPump2Temperature_Type = Integer32
_AuxPEIfPump2Temperature_Object = MibTableColumn
auxPEIfPump2Temperature = _AuxPEIfPump2Temperature_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 7, 1, 1, 35),
    _AuxPEIfPump2Temperature_Type()
)
auxPEIfPump2Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPEIfPump2Temperature.setStatus("current")
_AuxNodeList_ObjectIdentity = ObjectIdentity
auxNodeList = _AuxNodeList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 8)
)
_AuxNodeTable_Object = MibTable
auxNodeTable = _AuxNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 8, 1)
)
if mibBuilder.loadTexts:
    auxNodeTable.setStatus("current")
_AuxNodeEntry_Object = MibTableRow
auxNodeEntry = _AuxNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 8, 1, 1)
)
auxNodeEntry.setIndexNames(
    (0, "LUM-AUX-MIB", "auxNodeIndex"),
)
if mibBuilder.loadTexts:
    auxNodeEntry.setStatus("current")


class _AuxNodeIndex_Type(Unsigned32):
    """Custom type auxNodeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AuxNodeIndex_Type.__name__ = "Unsigned32"
_AuxNodeIndex_Object = MibTableColumn
auxNodeIndex = _AuxNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 8, 1, 1, 1),
    _AuxNodeIndex_Type()
)
auxNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxNodeIndex.setStatus("current")
_AuxNodeName_Type = MgmtNameString
_AuxNodeName_Object = MibTableColumn
auxNodeName = _AuxNodeName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 8, 1, 1, 2),
    _AuxNodeName_Type()
)
auxNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxNodeName.setStatus("current")


class _AuxNodeDescr_Type(DisplayString):
    """Custom type auxNodeDescr based on DisplayString"""
    defaultValue = OctetString("")


_AuxNodeDescr_Type.__name__ = "DisplayString"
_AuxNodeDescr_Object = MibTableColumn
auxNodeDescr = _AuxNodeDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 8, 1, 1, 3),
    _AuxNodeDescr_Type()
)
auxNodeDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxNodeDescr.setStatus("current")
_AuxNodeIpAddress_Type = IpAddress
_AuxNodeIpAddress_Object = MibTableColumn
auxNodeIpAddress = _AuxNodeIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 8, 1, 1, 4),
    _AuxNodeIpAddress_Type()
)
auxNodeIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxNodeIpAddress.setStatus("current")


class _AuxNodePort_Type(Unsigned32):
    """Custom type auxNodePort based on Unsigned32"""
    defaultValue = 49177

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_AuxNodePort_Type.__name__ = "Unsigned32"
_AuxNodePort_Object = MibTableColumn
auxNodePort = _AuxNodePort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 8, 1, 1, 5),
    _AuxNodePort_Type()
)
auxNodePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxNodePort.setStatus("current")


class _AuxNodeEventPort_Type(Unsigned32):
    """Custom type auxNodeEventPort based on Unsigned32"""
    defaultValue = 50177

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_AuxNodeEventPort_Type.__name__ = "Unsigned32"
_AuxNodeEventPort_Object = MibTableColumn
auxNodeEventPort = _AuxNodeEventPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 8, 1, 1, 6),
    _AuxNodeEventPort_Type()
)
auxNodeEventPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxNodeEventPort.setStatus("current")
_AuxNodeTime_Type = DateAndTime
_AuxNodeTime_Object = MibTableColumn
auxNodeTime = _AuxNodeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 8, 1, 1, 7),
    _AuxNodeTime_Type()
)
auxNodeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxNodeTime.setStatus("current")
_AuxNodeNtpPrimary_Type = IpAddress
_AuxNodeNtpPrimary_Object = MibTableColumn
auxNodeNtpPrimary = _AuxNodeNtpPrimary_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 8, 1, 1, 8),
    _AuxNodeNtpPrimary_Type()
)
auxNodeNtpPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxNodeNtpPrimary.setStatus("current")
_AuxNodeNtpSecondary_Type = IpAddress
_AuxNodeNtpSecondary_Object = MibTableColumn
auxNodeNtpSecondary = _AuxNodeNtpSecondary_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 8, 1, 1, 9),
    _AuxNodeNtpSecondary_Type()
)
auxNodeNtpSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxNodeNtpSecondary.setStatus("current")
_AuxNodeChangeLocalTime_Type = CommandString
_AuxNodeChangeLocalTime_Object = MibTableColumn
auxNodeChangeLocalTime = _AuxNodeChangeLocalTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 8, 1, 1, 10),
    _AuxNodeChangeLocalTime_Type()
)
auxNodeChangeLocalTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxNodeChangeLocalTime.setStatus("current")
_AuxNodeHostUnreachable_Type = FaultStatus
_AuxNodeHostUnreachable_Object = MibTableColumn
auxNodeHostUnreachable = _AuxNodeHostUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 8, 1, 1, 11),
    _AuxNodeHostUnreachable_Type()
)
auxNodeHostUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxNodeHostUnreachable.setStatus("current")
_AuxCabinetList_ObjectIdentity = ObjectIdentity
auxCabinetList = _AuxCabinetList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 9)
)
_AuxCabinetTable_Object = MibTable
auxCabinetTable = _AuxCabinetTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 9, 1)
)
if mibBuilder.loadTexts:
    auxCabinetTable.setStatus("current")
_AuxCabinetEntry_Object = MibTableRow
auxCabinetEntry = _AuxCabinetEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 9, 1, 1)
)
auxCabinetEntry.setIndexNames(
    (0, "LUM-AUX-MIB", "auxCabinetIndex"),
)
if mibBuilder.loadTexts:
    auxCabinetEntry.setStatus("current")


class _AuxCabinetIndex_Type(Unsigned32):
    """Custom type auxCabinetIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AuxCabinetIndex_Type.__name__ = "Unsigned32"
_AuxCabinetIndex_Object = MibTableColumn
auxCabinetIndex = _AuxCabinetIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 9, 1, 1, 1),
    _AuxCabinetIndex_Type()
)
auxCabinetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxCabinetIndex.setStatus("current")
_AuxCabinetName_Type = MgmtNameString
_AuxCabinetName_Object = MibTableColumn
auxCabinetName = _AuxCabinetName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 9, 1, 1, 2),
    _AuxCabinetName_Type()
)
auxCabinetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxCabinetName.setStatus("current")


class _AuxCabinetDescr_Type(DisplayString):
    """Custom type auxCabinetDescr based on DisplayString"""
    defaultValue = OctetString("")


_AuxCabinetDescr_Type.__name__ = "DisplayString"
_AuxCabinetDescr_Object = MibTableColumn
auxCabinetDescr = _AuxCabinetDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 9, 1, 1, 3),
    _AuxCabinetDescr_Type()
)
auxCabinetDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxCabinetDescr.setStatus("current")


class _AuxCabinetAdminStatus_Type(AdminStatusWithNA):
    """Custom type auxCabinetAdminStatus based on AdminStatusWithNA"""
    defaultValue = 3


_AuxCabinetAdminStatus_Type.__name__ = "AdminStatusWithNA"
_AuxCabinetAdminStatus_Object = MibTableColumn
auxCabinetAdminStatus = _AuxCabinetAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 9, 1, 1, 4),
    _AuxCabinetAdminStatus_Type()
)
auxCabinetAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxCabinetAdminStatus.setStatus("current")


class _AuxCabinetOperStatus_Type(Integer32):
    """Custom type auxCabinetOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 1),
          ("down", 2),
          ("up", 3))
    )


_AuxCabinetOperStatus_Type.__name__ = "Integer32"
_AuxCabinetOperStatus_Object = MibTableColumn
auxCabinetOperStatus = _AuxCabinetOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 9, 1, 1, 5),
    _AuxCabinetOperStatus_Type()
)
auxCabinetOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxCabinetOperStatus.setStatus("current")


class _AuxCabinetUpId_Type(Unsigned32):
    """Custom type auxCabinetUpId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AuxCabinetUpId_Type.__name__ = "Unsigned32"
_AuxCabinetUpId_Object = MibTableColumn
auxCabinetUpId = _AuxCabinetUpId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 9, 1, 1, 6),
    _AuxCabinetUpId_Type()
)
auxCabinetUpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxCabinetUpId.setStatus("current")
_AuxCabinetIndoorTemp_Type = Signed32WithNA
_AuxCabinetIndoorTemp_Object = MibTableColumn
auxCabinetIndoorTemp = _AuxCabinetIndoorTemp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 9, 1, 1, 7),
    _AuxCabinetIndoorTemp_Type()
)
auxCabinetIndoorTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxCabinetIndoorTemp.setStatus("current")
_AuxCabinetOutdoorTemp_Type = Signed32WithNA
_AuxCabinetOutdoorTemp_Object = MibTableColumn
auxCabinetOutdoorTemp = _AuxCabinetOutdoorTemp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 9, 1, 1, 8),
    _AuxCabinetOutdoorTemp_Type()
)
auxCabinetOutdoorTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxCabinetOutdoorTemp.setStatus("current")


class _AuxCabinetOperMode_Type(Integer32):
    """Custom type auxCabinetOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("cooling", 1),
          ("heating", 2),
          ("nightmode", 3),
          ("tsf", 4),
          ("selftest", 5),
          ("manual", 6))
    )


_AuxCabinetOperMode_Type.__name__ = "Integer32"
_AuxCabinetOperMode_Object = MibTableColumn
auxCabinetOperMode = _AuxCabinetOperMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 9, 1, 1, 9),
    _AuxCabinetOperMode_Type()
)
auxCabinetOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxCabinetOperMode.setStatus("current")
_AuxCabinetDoorAlarm_Type = FaultStatus
_AuxCabinetDoorAlarm_Object = MibTableColumn
auxCabinetDoorAlarm = _AuxCabinetDoorAlarm_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 9, 1, 1, 10),
    _AuxCabinetDoorAlarm_Type()
)
auxCabinetDoorAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxCabinetDoorAlarm.setStatus("current")
_AuxCabinetSPDAlarm_Type = FaultStatus
_AuxCabinetSPDAlarm_Object = MibTableColumn
auxCabinetSPDAlarm = _AuxCabinetSPDAlarm_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 9, 1, 1, 11),
    _AuxCabinetSPDAlarm_Type()
)
auxCabinetSPDAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxCabinetSPDAlarm.setStatus("current")
_AuxCabinetHighTempAlarm_Type = FaultStatus
_AuxCabinetHighTempAlarm_Object = MibTableColumn
auxCabinetHighTempAlarm = _AuxCabinetHighTempAlarm_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 9, 1, 1, 12),
    _AuxCabinetHighTempAlarm_Type()
)
auxCabinetHighTempAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxCabinetHighTempAlarm.setStatus("current")
_AuxCabinetCtrlFailAlarm_Type = FaultStatus
_AuxCabinetCtrlFailAlarm_Object = MibTableColumn
auxCabinetCtrlFailAlarm = _AuxCabinetCtrlFailAlarm_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 9, 1, 1, 13),
    _AuxCabinetCtrlFailAlarm_Type()
)
auxCabinetCtrlFailAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxCabinetCtrlFailAlarm.setStatus("current")
_AuxCabinetHeatFailAlarm_Type = FaultStatus
_AuxCabinetHeatFailAlarm_Object = MibTableColumn
auxCabinetHeatFailAlarm = _AuxCabinetHeatFailAlarm_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 9, 1, 1, 14),
    _AuxCabinetHeatFailAlarm_Type()
)
auxCabinetHeatFailAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxCabinetHeatFailAlarm.setStatus("current")
_AuxCabinetExtTempFailAlarm_Type = FaultStatus
_AuxCabinetExtTempFailAlarm_Object = MibTableColumn
auxCabinetExtTempFailAlarm = _AuxCabinetExtTempFailAlarm_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 9, 1, 1, 15),
    _AuxCabinetExtTempFailAlarm_Type()
)
auxCabinetExtTempFailAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxCabinetExtTempFailAlarm.setStatus("current")
_AuxCabinetIntTempFailAlarm_Type = FaultStatus
_AuxCabinetIntTempFailAlarm_Object = MibTableColumn
auxCabinetIntTempFailAlarm = _AuxCabinetIntTempFailAlarm_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 9, 1, 1, 16),
    _AuxCabinetIntTempFailAlarm_Type()
)
auxCabinetIntTempFailAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxCabinetIntTempFailAlarm.setStatus("current")
_AuxFanList_ObjectIdentity = ObjectIdentity
auxFanList = _AuxFanList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 10)
)
_AuxFanTable_Object = MibTable
auxFanTable = _AuxFanTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 10, 1)
)
if mibBuilder.loadTexts:
    auxFanTable.setStatus("current")
_AuxFanEntry_Object = MibTableRow
auxFanEntry = _AuxFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 10, 1, 1)
)
auxFanEntry.setIndexNames(
    (0, "LUM-AUX-MIB", "auxFanIndex"),
)
if mibBuilder.loadTexts:
    auxFanEntry.setStatus("current")


class _AuxFanIndex_Type(Unsigned32):
    """Custom type auxFanIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AuxFanIndex_Type.__name__ = "Unsigned32"
_AuxFanIndex_Object = MibTableColumn
auxFanIndex = _AuxFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 10, 1, 1, 1),
    _AuxFanIndex_Type()
)
auxFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxFanIndex.setStatus("current")
_AuxFanName_Type = MgmtNameString
_AuxFanName_Object = MibTableColumn
auxFanName = _AuxFanName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 10, 1, 1, 2),
    _AuxFanName_Type()
)
auxFanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxFanName.setStatus("current")


class _AuxFanDescr_Type(DisplayString):
    """Custom type auxFanDescr based on DisplayString"""
    defaultValue = OctetString("")


_AuxFanDescr_Type.__name__ = "DisplayString"
_AuxFanDescr_Object = MibTableColumn
auxFanDescr = _AuxFanDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 10, 1, 1, 3),
    _AuxFanDescr_Type()
)
auxFanDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxFanDescr.setStatus("current")


class _AuxFanAdminStatus_Type(AdminStatusWithNA):
    """Custom type auxFanAdminStatus based on AdminStatusWithNA"""
    defaultValue = 3


_AuxFanAdminStatus_Type.__name__ = "AdminStatusWithNA"
_AuxFanAdminStatus_Object = MibTableColumn
auxFanAdminStatus = _AuxFanAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 10, 1, 1, 4),
    _AuxFanAdminStatus_Type()
)
auxFanAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxFanAdminStatus.setStatus("current")


class _AuxFanOperStatus_Type(Integer32):
    """Custom type auxFanOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 1),
          ("down", 2),
          ("up", 3))
    )


_AuxFanOperStatus_Type.__name__ = "Integer32"
_AuxFanOperStatus_Object = MibTableColumn
auxFanOperStatus = _AuxFanOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 10, 1, 1, 5),
    _AuxFanOperStatus_Type()
)
auxFanOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxFanOperStatus.setStatus("current")


class _AuxFanUpId_Type(Unsigned32):
    """Custom type auxFanUpId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AuxFanUpId_Type.__name__ = "Unsigned32"
_AuxFanUpId_Object = MibTableColumn
auxFanUpId = _AuxFanUpId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 10, 1, 1, 6),
    _AuxFanUpId_Type()
)
auxFanUpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxFanUpId.setStatus("current")
_AuxFanFailure_Type = FaultStatus
_AuxFanFailure_Object = MibTableColumn
auxFanFailure = _AuxFanFailure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 10, 1, 1, 7),
    _AuxFanFailure_Type()
)
auxFanFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxFanFailure.setStatus("current")
_AuxFanRPM_Type = Signed32WithNA
_AuxFanRPM_Object = MibTableColumn
auxFanRPM = _AuxFanRPM_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 10, 1, 1, 8),
    _AuxFanRPM_Type()
)
auxFanRPM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxFanRPM.setStatus("current")
_AuxFanGroupList_ObjectIdentity = ObjectIdentity
auxFanGroupList = _AuxFanGroupList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 11)
)
_AuxFanGroupTable_Object = MibTable
auxFanGroupTable = _AuxFanGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 11, 1)
)
if mibBuilder.loadTexts:
    auxFanGroupTable.setStatus("current")
_AuxFanGroupEntry_Object = MibTableRow
auxFanGroupEntry = _AuxFanGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 11, 1, 1)
)
auxFanGroupEntry.setIndexNames(
    (0, "LUM-AUX-MIB", "auxFanGroupIndex"),
)
if mibBuilder.loadTexts:
    auxFanGroupEntry.setStatus("current")


class _AuxFanGroupIndex_Type(Unsigned32):
    """Custom type auxFanGroupIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AuxFanGroupIndex_Type.__name__ = "Unsigned32"
_AuxFanGroupIndex_Object = MibTableColumn
auxFanGroupIndex = _AuxFanGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 11, 1, 1, 1),
    _AuxFanGroupIndex_Type()
)
auxFanGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxFanGroupIndex.setStatus("current")
_AuxFanGroupName_Type = MgmtNameString
_AuxFanGroupName_Object = MibTableColumn
auxFanGroupName = _AuxFanGroupName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 11, 1, 1, 2),
    _AuxFanGroupName_Type()
)
auxFanGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxFanGroupName.setStatus("current")


class _AuxFanGroupDescr_Type(DisplayString):
    """Custom type auxFanGroupDescr based on DisplayString"""
    defaultValue = OctetString("")


_AuxFanGroupDescr_Type.__name__ = "DisplayString"
_AuxFanGroupDescr_Object = MibTableColumn
auxFanGroupDescr = _AuxFanGroupDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 11, 1, 1, 3),
    _AuxFanGroupDescr_Type()
)
auxFanGroupDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxFanGroupDescr.setStatus("current")


class _AuxFanGroupAdminStatus_Type(AdminStatusWithNA):
    """Custom type auxFanGroupAdminStatus based on AdminStatusWithNA"""
    defaultValue = 3


_AuxFanGroupAdminStatus_Type.__name__ = "AdminStatusWithNA"
_AuxFanGroupAdminStatus_Object = MibTableColumn
auxFanGroupAdminStatus = _AuxFanGroupAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 11, 1, 1, 4),
    _AuxFanGroupAdminStatus_Type()
)
auxFanGroupAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxFanGroupAdminStatus.setStatus("current")


class _AuxFanGroupOperStatus_Type(Integer32):
    """Custom type auxFanGroupOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 1),
          ("down", 2),
          ("up", 3))
    )


_AuxFanGroupOperStatus_Type.__name__ = "Integer32"
_AuxFanGroupOperStatus_Object = MibTableColumn
auxFanGroupOperStatus = _AuxFanGroupOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 11, 1, 1, 5),
    _AuxFanGroupOperStatus_Type()
)
auxFanGroupOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxFanGroupOperStatus.setStatus("current")


class _AuxFanGroupUpId_Type(Unsigned32):
    """Custom type auxFanGroupUpId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AuxFanGroupUpId_Type.__name__ = "Unsigned32"
_AuxFanGroupUpId_Object = MibTableColumn
auxFanGroupUpId = _AuxFanGroupUpId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 11, 1, 1, 6),
    _AuxFanGroupUpId_Type()
)
auxFanGroupUpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxFanGroupUpId.setStatus("current")
_AuxFanGroupFailure_Type = FaultStatus
_AuxFanGroupFailure_Object = MibTableColumn
auxFanGroupFailure = _AuxFanGroupFailure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 2, 11, 1, 1, 7),
    _AuxFanGroupFailure_Type()
)
auxFanGroupFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxFanGroupFailure.setStatus("current")

# Managed Objects groups

auxGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 1, 1, 1)
)
auxGeneralGroup.setObjects(
      *(("LUM-AUX-MIB", "auxGeneralTestAndIncr"),
        ("LUM-AUX-MIB", "auxGeneralStateLastChangeTime"),
        ("LUM-AUX-MIB", "auxGeneralConfigLastChangeTime"),
        ("LUM-AUX-MIB", "auxGeneralSnmpTableSize"),
        ("LUM-AUX-MIB", "auxGeneralFxIfTableSize"),
        ("LUM-AUX-MIB", "auxGeneralAuxEquipmentTableSize"))
)
if mibBuilder.loadTexts:
    auxGeneralGroup.setStatus("deprecated")

auxSnmpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 1, 1, 2)
)
auxSnmpGroup.setObjects(
      *(("LUM-AUX-MIB", "auxSnmpIndex"),
        ("LUM-AUX-MIB", "auxSnmpName"),
        ("LUM-AUX-MIB", "auxSnmpDescr"),
        ("LUM-AUX-MIB", "auxSnmpAddress"),
        ("LUM-AUX-MIB", "auxSnmpPort"),
        ("LUM-AUX-MIB", "auxSnmpVersion"),
        ("LUM-AUX-MIB", "auxSnmpReadCommunity"),
        ("LUM-AUX-MIB", "auxSnmpWriteCommunity"),
        ("LUM-AUX-MIB", "auxSnmpAdminStatus"),
        ("LUM-AUX-MIB", "auxSnmpOperStatus"),
        ("LUM-AUX-MIB", "auxSnmpInvPhysIndexOrZero"),
        ("LUM-AUX-MIB", "auxSnmpHostUnreachable"),
        ("LUM-AUX-MIB", "auxSnmpSnmpError"),
        ("LUM-AUX-MIB", "auxSnmpUnexpectedEquipmentType"),
        ("LUM-AUX-MIB", "auxSnmpInconsistentConfiguration"))
)
if mibBuilder.loadTexts:
    auxSnmpGroup.setStatus("deprecated")

auxFxIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 1, 1, 3)
)
auxFxIfGroup.setObjects(
      *(("LUM-AUX-MIB", "auxFxIfIndex"),
        ("LUM-AUX-MIB", "auxFxIfName"),
        ("LUM-AUX-MIB", "auxFxIfDescr"),
        ("LUM-AUX-MIB", "auxFxIfSubrack"),
        ("LUM-AUX-MIB", "auxFxIfSlot"),
        ("LUM-AUX-MIB", "auxFxIfRxPort"),
        ("LUM-AUX-MIB", "auxFxIfTxPort"),
        ("LUM-AUX-MIB", "auxFxIfInvPhysIndexOrZero"),
        ("LUM-AUX-MIB", "auxFxIfAdminStatus"),
        ("LUM-AUX-MIB", "auxFxIfOperStatus"),
        ("LUM-AUX-MIB", "auxFxIfRxPowerLevel"),
        ("LUM-AUX-MIB", "auxFxIfLossOfSignalThreshold"),
        ("LUM-AUX-MIB", "auxFxIfLossOfSignal"))
)
if mibBuilder.loadTexts:
    auxFxIfGroup.setStatus("deprecated")

auxEquipmentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 1, 1, 4)
)
auxEquipmentGroup.setObjects(
      *(("LUM-AUX-MIB", "auxEquipmentIndex"),
        ("LUM-AUX-MIB", "auxEquipmentName"),
        ("LUM-AUX-MIB", "auxEquipmentDescr"),
        ("LUM-AUX-MIB", "auxEquipmentSubrack"),
        ("LUM-AUX-MIB", "auxEquipmentSlot"),
        ("LUM-AUX-MIB", "auxEquipmentAdminStatus"),
        ("LUM-AUX-MIB", "auxEquipmentOperStatus"),
        ("LUM-AUX-MIB", "auxEquipmentPowerFailure"),
        ("LUM-AUX-MIB", "auxEquipmentFanProblem"))
)
if mibBuilder.loadTexts:
    auxEquipmentGroup.setStatus("deprecated")

auxFxIfGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 1, 1, 5)
)
auxFxIfGroupV2.setObjects(
      *(("LUM-AUX-MIB", "auxFxIfIndex"),
        ("LUM-AUX-MIB", "auxFxIfName"),
        ("LUM-AUX-MIB", "auxFxIfDescr"),
        ("LUM-AUX-MIB", "auxFxIfSubrack"),
        ("LUM-AUX-MIB", "auxFxIfSlot"),
        ("LUM-AUX-MIB", "auxFxIfRxPort"),
        ("LUM-AUX-MIB", "auxFxIfTxPort"),
        ("LUM-AUX-MIB", "auxFxIfInvPhysIndexOrZero"),
        ("LUM-AUX-MIB", "auxFxIfAdminStatus"),
        ("LUM-AUX-MIB", "auxFxIfOperStatus"),
        ("LUM-AUX-MIB", "auxFxIfRxPowerLevel"),
        ("LUM-AUX-MIB", "auxFxIfLossOfSignalThreshold"),
        ("LUM-AUX-MIB", "auxFxIfLossOfSignal"),
        ("LUM-AUX-MIB", "auxFxIfObjectProperty"))
)
if mibBuilder.loadTexts:
    auxFxIfGroupV2.setStatus("current")

auxEquipmentGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 1, 1, 6)
)
auxEquipmentGroupV2.setObjects(
      *(("LUM-AUX-MIB", "auxEquipmentIndex"),
        ("LUM-AUX-MIB", "auxEquipmentName"),
        ("LUM-AUX-MIB", "auxEquipmentDescr"),
        ("LUM-AUX-MIB", "auxEquipmentSubrack"),
        ("LUM-AUX-MIB", "auxEquipmentSlot"),
        ("LUM-AUX-MIB", "auxEquipmentAdminStatus"),
        ("LUM-AUX-MIB", "auxEquipmentOperStatus"),
        ("LUM-AUX-MIB", "auxEquipmentPowerFailure"),
        ("LUM-AUX-MIB", "auxEquipmentFanProblem"),
        ("LUM-AUX-MIB", "auxEquipmentObjectProperty"))
)
if mibBuilder.loadTexts:
    auxEquipmentGroupV2.setStatus("deprecated")

auxRamanIfGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 1, 1, 7)
)
auxRamanIfGroupV1.setObjects(
      *(("LUM-AUX-MIB", "auxRamanIfIndex"),
        ("LUM-AUX-MIB", "auxRamanIfName"),
        ("LUM-AUX-MIB", "auxRamanIfDescr"),
        ("LUM-AUX-MIB", "auxRamanIfSubrack"),
        ("LUM-AUX-MIB", "auxRamanIfSlot"),
        ("LUM-AUX-MIB", "auxRamanIfRxPort"),
        ("LUM-AUX-MIB", "auxRamanIfTxPort"),
        ("LUM-AUX-MIB", "auxRamanIfInvPhysIndexOrZero"),
        ("LUM-AUX-MIB", "auxRamanIfAdminStatus"),
        ("LUM-AUX-MIB", "auxRamanIfOperStatus"),
        ("LUM-AUX-MIB", "auxRamanIfObjectProperty"),
        ("LUM-AUX-MIB", "auxRamanIfPumpsOperationMode"),
        ("LUM-AUX-MIB", "auxRamanIfModuleOperationMode"),
        ("LUM-AUX-MIB", "auxRamanIfPumpsOperationModeConfig"),
        ("LUM-AUX-MIB", "auxRamanIfLineFiberType"),
        ("LUM-AUX-MIB", "auxRamanIfAutoRestartProcTime"),
        ("LUM-AUX-MIB", "auxRamanIfArpPauseStatus"),
        ("LUM-AUX-MIB", "auxRamanIfPumpsStatus"),
        ("LUM-AUX-MIB", "auxRamanIfTotalPumpsPower"),
        ("LUM-AUX-MIB", "auxRamanIfPump1WantedPower"),
        ("LUM-AUX-MIB", "auxRamanIfPump1ActualPower"),
        ("LUM-AUX-MIB", "auxRamanIfPump1Current"),
        ("LUM-AUX-MIB", "auxRamanIfPump1Temperature"),
        ("LUM-AUX-MIB", "auxRamanIfPump2WantedPower"),
        ("LUM-AUX-MIB", "auxRamanIfPump2ActualPower"),
        ("LUM-AUX-MIB", "auxRamanIfPump2Current"),
        ("LUM-AUX-MIB", "auxRamanIfPump2Temperature"),
        ("LUM-AUX-MIB", "auxRamanIfWantedGain"),
        ("LUM-AUX-MIB", "auxRamanIfActualGain"),
        ("LUM-AUX-MIB", "auxRamanIfReceivedPowerLevel"),
        ("LUM-AUX-MIB", "auxRamanIfReflectionPowerLevel"),
        ("LUM-AUX-MIB", "auxRamanIfReflectionPowerRatio"),
        ("LUM-AUX-MIB", "auxRamanIf1510BandReceivedPowerLevel"),
        ("LUM-AUX-MIB", "auxRamanIfOscReceivedPowerLevel"),
        ("LUM-AUX-MIB", "auxRamanIfManualRestartTrial"),
        ("LUM-AUX-MIB", "auxRamanIfModuleTemp"))
)
if mibBuilder.loadTexts:
    auxRamanIfGroupV1.setStatus("deprecated")

auxRamanSafetyGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 1, 1, 8)
)
auxRamanSafetyGroupV1.setObjects(
      *(("LUM-AUX-MIB", "auxRamanSafetyIndex"),
        ("LUM-AUX-MIB", "auxRamanSafetyName"),
        ("LUM-AUX-MIB", "auxRamanSafetyDescr"),
        ("LUM-AUX-MIB", "auxRamanSafetySubrack"),
        ("LUM-AUX-MIB", "auxRamanSafetySlot"),
        ("LUM-AUX-MIB", "auxRamanSafetyRxPort"),
        ("LUM-AUX-MIB", "auxRamanSafetyTxPort"),
        ("LUM-AUX-MIB", "auxRamanSafetyInvPhysIndexOrZero"),
        ("LUM-AUX-MIB", "auxRamanSafetyObjectProperty"),
        ("LUM-AUX-MIB", "auxRamanSafetyShutDownAtInputLoss"),
        ("LUM-AUX-MIB", "auxRamanSafetyShutDownAtHighTemp"),
        ("LUM-AUX-MIB", "auxRamanSafetyShutDownAtHighBackReflection"),
        ("LUM-AUX-MIB", "auxRamanSafetyHighBackReflectionThreshold"),
        ("LUM-AUX-MIB", "auxRamanSafetyShutDownAtOscLoss"),
        ("LUM-AUX-MIB", "auxRamanSafetyShutDownAt1510BandDrop"),
        ("LUM-AUX-MIB", "auxRamanSafetyShutDownAtInputLossConfig"),
        ("LUM-AUX-MIB", "auxRamanSafetyShutDownAtHighTempConfig"),
        ("LUM-AUX-MIB", "auxRamanSafetyShutDownAtHighBackReflectionConfig"),
        ("LUM-AUX-MIB", "auxRamanSafetyShutDownAtOscLossConfig"),
        ("LUM-AUX-MIB", "auxRamanSafetyShutDownAt1510BandDropConfig"),
        ("LUM-AUX-MIB", "auxRamanSafetyPasswd"),
        ("LUM-AUX-MIB", "auxRamanSafetyPasswdConfig"),
        ("LUM-AUX-MIB", "auxRamanSafety1510BandDropThreshold"),
        ("LUM-AUX-MIB", "auxRamanSafetyInhibitStartAtOscLoss"),
        ("LUM-AUX-MIB", "auxRamanSafetyInhibitStartAtOscLossConfig"))
)
if mibBuilder.loadTexts:
    auxRamanSafetyGroupV1.setStatus("deprecated")

auxEquipmentGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 1, 1, 9)
)
auxEquipmentGroupV3.setObjects(
      *(("LUM-AUX-MIB", "auxEquipmentIndex"),
        ("LUM-AUX-MIB", "auxEquipmentName"),
        ("LUM-AUX-MIB", "auxEquipmentDescr"),
        ("LUM-AUX-MIB", "auxEquipmentSubrack"),
        ("LUM-AUX-MIB", "auxEquipmentSlot"),
        ("LUM-AUX-MIB", "auxEquipmentAdminStatus"),
        ("LUM-AUX-MIB", "auxEquipmentOperStatus"),
        ("LUM-AUX-MIB", "auxEquipmentPowerFailure"),
        ("LUM-AUX-MIB", "auxEquipmentFanProblem"),
        ("LUM-AUX-MIB", "auxEquipmentObjectProperty"),
        ("LUM-AUX-MIB", "auxEquipmentPumpsEol"),
        ("LUM-AUX-MIB", "auxEquipmentSelfTestFailure"),
        ("LUM-AUX-MIB", "auxEquipmentAmbientTemp"),
        ("LUM-AUX-MIB", "auxEquipmentRebootEquipment"))
)
if mibBuilder.loadTexts:
    auxEquipmentGroupV3.setStatus("deprecated")

auxSnmpGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 1, 1, 10)
)
auxSnmpGroupV2.setObjects(
      *(("LUM-AUX-MIB", "auxSnmpIndex"),
        ("LUM-AUX-MIB", "auxSnmpName"),
        ("LUM-AUX-MIB", "auxSnmpDescr"),
        ("LUM-AUX-MIB", "auxSnmpAddress"),
        ("LUM-AUX-MIB", "auxSnmpPort"),
        ("LUM-AUX-MIB", "auxSnmpVersion"),
        ("LUM-AUX-MIB", "auxSnmpReadCommunity"),
        ("LUM-AUX-MIB", "auxSnmpWriteCommunity"),
        ("LUM-AUX-MIB", "auxSnmpAdminStatus"),
        ("LUM-AUX-MIB", "auxSnmpOperStatus"),
        ("LUM-AUX-MIB", "auxSnmpInvPhysIndexOrZero"),
        ("LUM-AUX-MIB", "auxSnmpHostUnreachable"),
        ("LUM-AUX-MIB", "auxSnmpSnmpError"),
        ("LUM-AUX-MIB", "auxSnmpUnexpectedEquipmentType"),
        ("LUM-AUX-MIB", "auxSnmpInconsistentConfiguration"),
        ("LUM-AUX-MIB", "auxSnmpConfigurationProblem"))
)
if mibBuilder.loadTexts:
    auxSnmpGroupV2.setStatus("current")

auxRamanSafetyGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 1, 1, 11)
)
auxRamanSafetyGroupV2.setObjects(
      *(("LUM-AUX-MIB", "auxRamanSafetyIndex"),
        ("LUM-AUX-MIB", "auxRamanSafetyName"),
        ("LUM-AUX-MIB", "auxRamanSafetyDescr"),
        ("LUM-AUX-MIB", "auxRamanSafetySubrack"),
        ("LUM-AUX-MIB", "auxRamanSafetySlot"),
        ("LUM-AUX-MIB", "auxRamanSafetyRxPort"),
        ("LUM-AUX-MIB", "auxRamanSafetyTxPort"),
        ("LUM-AUX-MIB", "auxRamanSafetyInvPhysIndexOrZero"),
        ("LUM-AUX-MIB", "auxRamanSafetyObjectProperty"),
        ("LUM-AUX-MIB", "auxRamanSafetyShutDownAtInputLoss"),
        ("LUM-AUX-MIB", "auxRamanSafetyShutDownAtHighTemp"),
        ("LUM-AUX-MIB", "auxRamanSafetyShutDownAtHighBackReflection"),
        ("LUM-AUX-MIB", "auxRamanSafetyHighBackReflectionThreshold"),
        ("LUM-AUX-MIB", "auxRamanSafetyShutDownAtOscLoss"),
        ("LUM-AUX-MIB", "auxRamanSafetyShutDownAt1510BandDrop"),
        ("LUM-AUX-MIB", "auxRamanSafetyShutDownAtInputLossConfig"),
        ("LUM-AUX-MIB", "auxRamanSafetyShutDownAtHighTempConfig"),
        ("LUM-AUX-MIB", "auxRamanSafetyShutDownAtHighBackReflectionConfig"),
        ("LUM-AUX-MIB", "auxRamanSafetyShutDownAtOscLossConfig"),
        ("LUM-AUX-MIB", "auxRamanSafetyShutDownAt1510BandDropConfig"),
        ("LUM-AUX-MIB", "auxRamanSafetyPasswd"),
        ("LUM-AUX-MIB", "auxRamanSafetyPasswdConfig"),
        ("LUM-AUX-MIB", "auxRamanSafety1510BandDropThreshold"),
        ("LUM-AUX-MIB", "auxRamanSafetyInhibitStartAtOscLoss"),
        ("LUM-AUX-MIB", "auxRamanSafetyInhibitStartAtOscLossConfig"),
        ("LUM-AUX-MIB", "auxRamanSafetyShutDownAtLowBandDrop"),
        ("LUM-AUX-MIB", "auxRamanSafetyLowBandScatteringThreshold"),
        ("LUM-AUX-MIB", "auxRamanSafetyShutDownAtLowBandDropConfig"),
        ("LUM-AUX-MIB", "auxRamanSafetyAmplifierSwitch"),
        ("LUM-AUX-MIB", "auxRamanSafetyAmplifierSwitchConfig"),
        ("LUM-AUX-MIB", "auxRamanSafetyLowBandScatteringTolerance"))
)
if mibBuilder.loadTexts:
    auxRamanSafetyGroupV2.setStatus("current")

auxPEIfGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 1, 1, 12)
)
auxPEIfGroupV1.setObjects(
      *(("LUM-AUX-MIB", "auxPEIfIndex"),
        ("LUM-AUX-MIB", "auxPEIfName"),
        ("LUM-AUX-MIB", "auxPEIfDescr"),
        ("LUM-AUX-MIB", "auxPEIfSubrack"),
        ("LUM-AUX-MIB", "auxPEIfSlot"),
        ("LUM-AUX-MIB", "auxPEIfRxPort"),
        ("LUM-AUX-MIB", "auxPEIfTxPort"),
        ("LUM-AUX-MIB", "auxPEIfInvPhysIndexOrZero"),
        ("LUM-AUX-MIB", "auxPEIfAdminStatus"),
        ("LUM-AUX-MIB", "auxPEIfOperStatus"),
        ("LUM-AUX-MIB", "auxPEIfObjectProperty"),
        ("LUM-AUX-MIB", "auxPEIfPumpsOperationMode"),
        ("LUM-AUX-MIB", "auxPEIfPumpsOperationModeConfig"),
        ("LUM-AUX-MIB", "auxPEIfAutoRestartProcTime"),
        ("LUM-AUX-MIB", "auxPEIfPumpsStatus"),
        ("LUM-AUX-MIB", "auxPEIfWantedPower"),
        ("LUM-AUX-MIB", "auxPEIfWantedGain"),
        ("LUM-AUX-MIB", "auxPEIfPumpsTotalCurrent"),
        ("LUM-AUX-MIB", "auxPEIfPump1Temperature"),
        ("LUM-AUX-MIB", "auxPEIfActualGain"),
        ("LUM-AUX-MIB", "auxPEIfReceivedPowerLevel"),
        ("LUM-AUX-MIB", "auxPEIfReflectionPowerLevel"),
        ("LUM-AUX-MIB", "auxPEIfReflectionPowerRatio"),
        ("LUM-AUX-MIB", "auxPEIfLowBandScatteredPowerLevel"),
        ("LUM-AUX-MIB", "auxPEIfLineLossOfSignal"),
        ("LUM-AUX-MIB", "auxPEIfHighBackReflection"),
        ("LUM-AUX-MIB", "auxPEIfAutoPowerReduction"),
        ("LUM-AUX-MIB", "auxPEIfLowLineOutputPower"),
        ("LUM-AUX-MIB", "auxPEIfModuleTempTooHigh"),
        ("LUM-AUX-MIB", "auxPEIfModuleTempHigh"),
        ("LUM-AUX-MIB", "auxPEIfPumpsTempTooHigh"),
        ("LUM-AUX-MIB", "auxPEIfPumpsTempHigh"),
        ("LUM-AUX-MIB", "auxPEIfModuleTemp"),
        ("LUM-AUX-MIB", "auxPEIfPump2Temperature"))
)
if mibBuilder.loadTexts:
    auxPEIfGroupV1.setStatus("current")

auxEquipmentGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 1, 1, 13)
)
auxEquipmentGroupV4.setObjects(
      *(("LUM-AUX-MIB", "auxEquipmentIndex"),
        ("LUM-AUX-MIB", "auxEquipmentName"),
        ("LUM-AUX-MIB", "auxEquipmentDescr"),
        ("LUM-AUX-MIB", "auxEquipmentSubrack"),
        ("LUM-AUX-MIB", "auxEquipmentSlot"),
        ("LUM-AUX-MIB", "auxEquipmentAdminStatus"),
        ("LUM-AUX-MIB", "auxEquipmentOperStatus"),
        ("LUM-AUX-MIB", "auxEquipmentPowerFailure"),
        ("LUM-AUX-MIB", "auxEquipmentFanProblem"),
        ("LUM-AUX-MIB", "auxEquipmentObjectProperty"),
        ("LUM-AUX-MIB", "auxEquipmentPumpsEol"),
        ("LUM-AUX-MIB", "auxEquipmentSelfTestFailure"),
        ("LUM-AUX-MIB", "auxEquipmentAmbientTemp"),
        ("LUM-AUX-MIB", "auxEquipmentRebootEquipment"),
        ("LUM-AUX-MIB", "auxEquipmentPowerAMissing"),
        ("LUM-AUX-MIB", "auxEquipmentPowerBMissing"))
)
if mibBuilder.loadTexts:
    auxEquipmentGroupV4.setStatus("deprecated")

auxEquipmentGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 1, 1, 14)
)
auxEquipmentGroupV5.setObjects(
      *(("LUM-AUX-MIB", "auxEquipmentIndex"),
        ("LUM-AUX-MIB", "auxEquipmentName"),
        ("LUM-AUX-MIB", "auxEquipmentDescr"),
        ("LUM-AUX-MIB", "auxEquipmentSubrack"),
        ("LUM-AUX-MIB", "auxEquipmentSlot"),
        ("LUM-AUX-MIB", "auxEquipmentAdminStatus"),
        ("LUM-AUX-MIB", "auxEquipmentOperStatus"),
        ("LUM-AUX-MIB", "auxEquipmentPowerFailure"),
        ("LUM-AUX-MIB", "auxEquipmentFanProblem"),
        ("LUM-AUX-MIB", "auxEquipmentObjectProperty"),
        ("LUM-AUX-MIB", "auxEquipmentPumpsEol"),
        ("LUM-AUX-MIB", "auxEquipmentSelfTestFailure"),
        ("LUM-AUX-MIB", "auxEquipmentAmbientTemp"),
        ("LUM-AUX-MIB", "auxEquipmentRebootEquipment"),
        ("LUM-AUX-MIB", "auxEquipmentPowerAMissing"),
        ("LUM-AUX-MIB", "auxEquipmentPowerBMissing"),
        ("LUM-AUX-MIB", "auxEquipmentConfigurationMismatch"))
)
if mibBuilder.loadTexts:
    auxEquipmentGroupV5.setStatus("current")

auxNodeGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 1, 1, 15)
)
auxNodeGroupV1.setObjects(
      *(("LUM-AUX-MIB", "auxNodeIndex"),
        ("LUM-AUX-MIB", "auxNodeName"),
        ("LUM-AUX-MIB", "auxNodeDescr"),
        ("LUM-AUX-MIB", "auxNodeIpAddress"),
        ("LUM-AUX-MIB", "auxNodePort"),
        ("LUM-AUX-MIB", "auxNodeEventPort"),
        ("LUM-AUX-MIB", "auxNodeTime"),
        ("LUM-AUX-MIB", "auxNodeNtpPrimary"),
        ("LUM-AUX-MIB", "auxNodeNtpSecondary"),
        ("LUM-AUX-MIB", "auxNodeChangeLocalTime"),
        ("LUM-AUX-MIB", "auxNodeHostUnreachable"))
)
if mibBuilder.loadTexts:
    auxNodeGroupV1.setStatus("current")

auxRamanIfGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 1, 1, 16)
)
auxRamanIfGroupV2.setObjects(
      *(("LUM-AUX-MIB", "auxRamanIfIndex"),
        ("LUM-AUX-MIB", "auxRamanIfName"),
        ("LUM-AUX-MIB", "auxRamanIfDescr"),
        ("LUM-AUX-MIB", "auxRamanIfSubrack"),
        ("LUM-AUX-MIB", "auxRamanIfSlot"),
        ("LUM-AUX-MIB", "auxRamanIfRxPort"),
        ("LUM-AUX-MIB", "auxRamanIfTxPort"),
        ("LUM-AUX-MIB", "auxRamanIfInvPhysIndexOrZero"),
        ("LUM-AUX-MIB", "auxRamanIfAdminStatus"),
        ("LUM-AUX-MIB", "auxRamanIfOperStatus"),
        ("LUM-AUX-MIB", "auxRamanIfObjectProperty"),
        ("LUM-AUX-MIB", "auxRamanIfPumpsOperationMode"),
        ("LUM-AUX-MIB", "auxRamanIfModuleOperationMode"),
        ("LUM-AUX-MIB", "auxRamanIfPumpsOperationModeConfig"),
        ("LUM-AUX-MIB", "auxRamanIfLineFiberType"),
        ("LUM-AUX-MIB", "auxRamanIfAutoRestartProcTime"),
        ("LUM-AUX-MIB", "auxRamanIfArpPauseStatus"),
        ("LUM-AUX-MIB", "auxRamanIfPumpsStatus"),
        ("LUM-AUX-MIB", "auxRamanIfTotalPumpsPower"),
        ("LUM-AUX-MIB", "auxRamanIfPump1WantedPower"),
        ("LUM-AUX-MIB", "auxRamanIfPump1ActualPower"),
        ("LUM-AUX-MIB", "auxRamanIfPump1Current"),
        ("LUM-AUX-MIB", "auxRamanIfPump1Temperature"),
        ("LUM-AUX-MIB", "auxRamanIfPump2WantedPower"),
        ("LUM-AUX-MIB", "auxRamanIfPump2ActualPower"),
        ("LUM-AUX-MIB", "auxRamanIfPump2Current"),
        ("LUM-AUX-MIB", "auxRamanIfPump2Temperature"),
        ("LUM-AUX-MIB", "auxRamanIfWantedGain"),
        ("LUM-AUX-MIB", "auxRamanIfActualGain"),
        ("LUM-AUX-MIB", "auxRamanIfReceivedPowerLevel"),
        ("LUM-AUX-MIB", "auxRamanIfReflectionPowerLevel"),
        ("LUM-AUX-MIB", "auxRamanIfReflectionPowerRatio"),
        ("LUM-AUX-MIB", "auxRamanIf1510BandReceivedPowerLevel"),
        ("LUM-AUX-MIB", "auxRamanIfOscReceivedPowerLevel"),
        ("LUM-AUX-MIB", "auxRamanIfManualRestartTrial"),
        ("LUM-AUX-MIB", "auxRamanIfModuleTemp"),
        ("LUM-AUX-MIB", "auxRamanIfTxSignalStatus"),
        ("LUM-AUX-MIB", "auxRamanIfRxSignalStatus"))
)
if mibBuilder.loadTexts:
    auxRamanIfGroupV2.setStatus("current")

auxGeneralGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 1, 1, 17)
)
auxGeneralGroupV2.setObjects(
      *(("LUM-AUX-MIB", "auxGeneralTestAndIncr"),
        ("LUM-AUX-MIB", "auxGeneralStateLastChangeTime"),
        ("LUM-AUX-MIB", "auxGeneralConfigLastChangeTime"),
        ("LUM-AUX-MIB", "auxGeneralSnmpTableSize"),
        ("LUM-AUX-MIB", "auxGeneralFxIfTableSize"),
        ("LUM-AUX-MIB", "auxGeneralAuxEquipmentTableSize"),
        ("LUM-AUX-MIB", "auxGeneralRamanIfTableSize"),
        ("LUM-AUX-MIB", "auxGeneralRamanSafetyTableSize"),
        ("LUM-AUX-MIB", "auxGeneralPEIfTableSize"),
        ("LUM-AUX-MIB", "auxGeneralNodeTableSize"),
        ("LUM-AUX-MIB", "auxGeneralCabinetTableSize"),
        ("LUM-AUX-MIB", "auxGeneralFanTableSize"),
        ("LUM-AUX-MIB", "auxGeneralFanGroupTableSize"))
)
if mibBuilder.loadTexts:
    auxGeneralGroupV2.setStatus("current")

auxCabinetGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 1, 1, 18)
)
auxCabinetGroupV1.setObjects(
      *(("LUM-AUX-MIB", "auxCabinetIndex"),
        ("LUM-AUX-MIB", "auxCabinetName"),
        ("LUM-AUX-MIB", "auxCabinetDescr"),
        ("LUM-AUX-MIB", "auxCabinetAdminStatus"),
        ("LUM-AUX-MIB", "auxCabinetOperStatus"),
        ("LUM-AUX-MIB", "auxCabinetUpId"),
        ("LUM-AUX-MIB", "auxCabinetIndoorTemp"),
        ("LUM-AUX-MIB", "auxCabinetOutdoorTemp"),
        ("LUM-AUX-MIB", "auxCabinetOperMode"),
        ("LUM-AUX-MIB", "auxCabinetDoorAlarm"),
        ("LUM-AUX-MIB", "auxCabinetSPDAlarm"),
        ("LUM-AUX-MIB", "auxCabinetHighTempAlarm"),
        ("LUM-AUX-MIB", "auxCabinetCtrlFailAlarm"),
        ("LUM-AUX-MIB", "auxCabinetHeatFailAlarm"),
        ("LUM-AUX-MIB", "auxCabinetExtTempFailAlarm"),
        ("LUM-AUX-MIB", "auxCabinetIntTempFailAlarm"))
)
if mibBuilder.loadTexts:
    auxCabinetGroupV1.setStatus("current")

auxFanGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 1, 1, 19)
)
auxFanGroupV1.setObjects(
      *(("LUM-AUX-MIB", "auxFanIndex"),
        ("LUM-AUX-MIB", "auxFanName"),
        ("LUM-AUX-MIB", "auxFanDescr"),
        ("LUM-AUX-MIB", "auxFanAdminStatus"),
        ("LUM-AUX-MIB", "auxFanOperStatus"),
        ("LUM-AUX-MIB", "auxFanUpId"),
        ("LUM-AUX-MIB", "auxFanFailure"),
        ("LUM-AUX-MIB", "auxFanRPM"))
)
if mibBuilder.loadTexts:
    auxFanGroupV1.setStatus("current")

auxFanGroupGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 1, 1, 20)
)
auxFanGroupGroupV1.setObjects(
      *(("LUM-AUX-MIB", "auxFanGroupIndex"),
        ("LUM-AUX-MIB", "auxFanGroupName"),
        ("LUM-AUX-MIB", "auxFanGroupDescr"),
        ("LUM-AUX-MIB", "auxFanGroupAdminStatus"),
        ("LUM-AUX-MIB", "auxFanGroupOperStatus"),
        ("LUM-AUX-MIB", "auxFanGroupUpId"),
        ("LUM-AUX-MIB", "auxFanGroupFailure"))
)
if mibBuilder.loadTexts:
    auxFanGroupGroupV1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumAuxBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 1, 2, 1)
)
lumAuxBasicComplV1.setObjects(
      *(("LUM-AUX-MIB", "auxGeneralGroup"),
        ("LUM-AUX-MIB", "auxSnmpGroup"),
        ("LUM-AUX-MIB", "auxFxIfGroup"),
        ("LUM-AUX-MIB", "auxEquipmentGroup"))
)
if mibBuilder.loadTexts:
    lumAuxBasicComplV1.setStatus(
        "deprecated"
    )

lumAuxBasicComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 1, 2, 2)
)
lumAuxBasicComplV2.setObjects(
      *(("LUM-AUX-MIB", "auxGeneralGroup"),
        ("LUM-AUX-MIB", "auxSnmpGroup"),
        ("LUM-AUX-MIB", "auxFxIfGroupV2"),
        ("LUM-AUX-MIB", "auxEquipmentGroupV2"))
)
if mibBuilder.loadTexts:
    lumAuxBasicComplV2.setStatus(
        "deprecated"
    )

lumAuxBasicComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 1, 2, 3)
)
lumAuxBasicComplV3.setObjects(
      *(("LUM-AUX-MIB", "auxGeneralGroup"),
        ("LUM-AUX-MIB", "auxSnmpGroupV2"),
        ("LUM-AUX-MIB", "auxFxIfGroupV2"),
        ("LUM-AUX-MIB", "auxEquipmentGroupV3"),
        ("LUM-AUX-MIB", "auxRamanIfGroupV1"),
        ("LUM-AUX-MIB", "auxRamanSafetyGroupV1"))
)
if mibBuilder.loadTexts:
    lumAuxBasicComplV3.setStatus(
        "deprecated"
    )

lumAuxBasicComplV4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 1, 2, 4)
)
lumAuxBasicComplV4.setObjects(
      *(("LUM-AUX-MIB", "auxGeneralGroup"),
        ("LUM-AUX-MIB", "auxSnmpGroupV2"),
        ("LUM-AUX-MIB", "auxFxIfGroupV2"),
        ("LUM-AUX-MIB", "auxEquipmentGroupV4"),
        ("LUM-AUX-MIB", "auxRamanIfGroupV1"),
        ("LUM-AUX-MIB", "auxRamanSafetyGroupV2"),
        ("LUM-AUX-MIB", "auxPEIfGroupV1"))
)
if mibBuilder.loadTexts:
    lumAuxBasicComplV4.setStatus(
        "deprecated"
    )

lumAuxBasicComplV5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 1, 2, 5)
)
lumAuxBasicComplV5.setObjects(
      *(("LUM-AUX-MIB", "auxGeneralGroup"),
        ("LUM-AUX-MIB", "auxSnmpGroupV2"),
        ("LUM-AUX-MIB", "auxFxIfGroupV2"),
        ("LUM-AUX-MIB", "auxEquipmentGroupV5"),
        ("LUM-AUX-MIB", "auxRamanIfGroupV1"),
        ("LUM-AUX-MIB", "auxRamanSafetyGroupV2"),
        ("LUM-AUX-MIB", "auxPEIfGroupV1"),
        ("LUM-AUX-MIB", "auxNodeGroupV1"))
)
if mibBuilder.loadTexts:
    lumAuxBasicComplV5.setStatus(
        "deprecated"
    )

lumAuxBasicComplV6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 1, 2, 6)
)
lumAuxBasicComplV6.setObjects(
      *(("LUM-AUX-MIB", "auxGeneralGroup"),
        ("LUM-AUX-MIB", "auxSnmpGroupV2"),
        ("LUM-AUX-MIB", "auxFxIfGroupV2"),
        ("LUM-AUX-MIB", "auxEquipmentGroupV5"),
        ("LUM-AUX-MIB", "auxRamanIfGroupV2"),
        ("LUM-AUX-MIB", "auxRamanSafetyGroupV2"),
        ("LUM-AUX-MIB", "auxPEIfGroupV1"),
        ("LUM-AUX-MIB", "auxNodeGroupV1"))
)
if mibBuilder.loadTexts:
    lumAuxBasicComplV6.setStatus(
        "deprecated"
    )

lumAuxBasicComplV7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 1, 2, 7)
)
lumAuxBasicComplV7.setObjects(
      *(("LUM-AUX-MIB", "auxGeneralGroupV2"),
        ("LUM-AUX-MIB", "auxSnmpGroupV2"),
        ("LUM-AUX-MIB", "auxFxIfGroupV2"),
        ("LUM-AUX-MIB", "auxEquipmentGroupV5"),
        ("LUM-AUX-MIB", "auxRamanIfGroupV2"),
        ("LUM-AUX-MIB", "auxRamanSafetyGroupV2"),
        ("LUM-AUX-MIB", "auxPEIfGroupV1"),
        ("LUM-AUX-MIB", "auxNodeGroupV1"),
        ("LUM-AUX-MIB", "auxCabinetGroupV1"),
        ("LUM-AUX-MIB", "auxFanGroupV1"),
        ("LUM-AUX-MIB", "auxFanGroupGroupV1"))
)
if mibBuilder.loadTexts:
    lumAuxBasicComplV7.setStatus(
        "deprecated"
    )

lumAuxBasicComplV8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 29, 1, 2, 8)
)
lumAuxBasicComplV8.setObjects(
      *(("LUM-AUX-MIB", "auxGeneralGroupV2"),
        ("LUM-AUX-MIB", "auxSnmpGroupV2"),
        ("LUM-AUX-MIB", "auxFxIfGroupV2"),
        ("LUM-AUX-MIB", "auxEquipmentGroupV5"),
        ("LUM-AUX-MIB", "auxRamanIfGroupV2"),
        ("LUM-AUX-MIB", "auxRamanSafetyGroupV2"),
        ("LUM-AUX-MIB", "auxPEIfGroupV1"),
        ("LUM-AUX-MIB", "auxNodeGroupV1"),
        ("LUM-AUX-MIB", "auxCabinetGroupV1"),
        ("LUM-AUX-MIB", "auxFanGroupV1"),
        ("LUM-AUX-MIB", "auxFanGroupGroupV1"))
)
if mibBuilder.loadTexts:
    lumAuxBasicComplV8.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-AUX-MIB",
    **{"lumAuxMIBModule": lumAuxMIBModule,
       "lumAuxConfs": lumAuxConfs,
       "lumAuxGroups": lumAuxGroups,
       "auxGeneralGroup": auxGeneralGroup,
       "auxSnmpGroup": auxSnmpGroup,
       "auxFxIfGroup": auxFxIfGroup,
       "auxEquipmentGroup": auxEquipmentGroup,
       "auxFxIfGroupV2": auxFxIfGroupV2,
       "auxEquipmentGroupV2": auxEquipmentGroupV2,
       "auxRamanIfGroupV1": auxRamanIfGroupV1,
       "auxRamanSafetyGroupV1": auxRamanSafetyGroupV1,
       "auxEquipmentGroupV3": auxEquipmentGroupV3,
       "auxSnmpGroupV2": auxSnmpGroupV2,
       "auxRamanSafetyGroupV2": auxRamanSafetyGroupV2,
       "auxPEIfGroupV1": auxPEIfGroupV1,
       "auxEquipmentGroupV4": auxEquipmentGroupV4,
       "auxEquipmentGroupV5": auxEquipmentGroupV5,
       "auxNodeGroupV1": auxNodeGroupV1,
       "auxRamanIfGroupV2": auxRamanIfGroupV2,
       "auxGeneralGroupV2": auxGeneralGroupV2,
       "auxCabinetGroupV1": auxCabinetGroupV1,
       "auxFanGroupV1": auxFanGroupV1,
       "auxFanGroupGroupV1": auxFanGroupGroupV1,
       "lumAuxCompl": lumAuxCompl,
       "lumAuxBasicComplV1": lumAuxBasicComplV1,
       "lumAuxBasicComplV2": lumAuxBasicComplV2,
       "lumAuxBasicComplV3": lumAuxBasicComplV3,
       "lumAuxBasicComplV4": lumAuxBasicComplV4,
       "lumAuxBasicComplV5": lumAuxBasicComplV5,
       "lumAuxBasicComplV6": lumAuxBasicComplV6,
       "lumAuxBasicComplV7": lumAuxBasicComplV7,
       "lumAuxBasicComplV8": lumAuxBasicComplV8,
       "lumAuxMIBObjects": lumAuxMIBObjects,
       "auxGeneral": auxGeneral,
       "auxGeneralTestAndIncr": auxGeneralTestAndIncr,
       "auxGeneralStateLastChangeTime": auxGeneralStateLastChangeTime,
       "auxGeneralConfigLastChangeTime": auxGeneralConfigLastChangeTime,
       "auxGeneralSnmpTableSize": auxGeneralSnmpTableSize,
       "auxGeneralFxIfTableSize": auxGeneralFxIfTableSize,
       "auxGeneralAuxEquipmentTableSize": auxGeneralAuxEquipmentTableSize,
       "auxGeneralRamanIfTableSize": auxGeneralRamanIfTableSize,
       "auxGeneralRamanSafetyTableSize": auxGeneralRamanSafetyTableSize,
       "auxGeneralPEIfTableSize": auxGeneralPEIfTableSize,
       "auxGeneralNodeTableSize": auxGeneralNodeTableSize,
       "auxGeneralCabinetTableSize": auxGeneralCabinetTableSize,
       "auxGeneralFanTableSize": auxGeneralFanTableSize,
       "auxGeneralFanGroupTableSize": auxGeneralFanGroupTableSize,
       "auxSnmpList": auxSnmpList,
       "auxSnmpTable": auxSnmpTable,
       "auxSnmpEntry": auxSnmpEntry,
       "auxSnmpIndex": auxSnmpIndex,
       "auxSnmpName": auxSnmpName,
       "auxSnmpDescr": auxSnmpDescr,
       "auxSnmpAddress": auxSnmpAddress,
       "auxSnmpVersion": auxSnmpVersion,
       "auxSnmpPort": auxSnmpPort,
       "auxSnmpReadCommunity": auxSnmpReadCommunity,
       "auxSnmpWriteCommunity": auxSnmpWriteCommunity,
       "auxSnmpAdminStatus": auxSnmpAdminStatus,
       "auxSnmpOperStatus": auxSnmpOperStatus,
       "auxSnmpInvPhysIndexOrZero": auxSnmpInvPhysIndexOrZero,
       "auxSnmpHostUnreachable": auxSnmpHostUnreachable,
       "auxSnmpSnmpError": auxSnmpSnmpError,
       "auxSnmpUnexpectedEquipmentType": auxSnmpUnexpectedEquipmentType,
       "auxSnmpInconsistentConfiguration": auxSnmpInconsistentConfiguration,
       "auxSnmpConfigurationProblem": auxSnmpConfigurationProblem,
       "auxFxIfList": auxFxIfList,
       "auxFxIfTable": auxFxIfTable,
       "auxFxIfEntry": auxFxIfEntry,
       "auxFxIfIndex": auxFxIfIndex,
       "auxFxIfName": auxFxIfName,
       "auxFxIfDescr": auxFxIfDescr,
       "auxFxIfSubrack": auxFxIfSubrack,
       "auxFxIfSlot": auxFxIfSlot,
       "auxFxIfTxPort": auxFxIfTxPort,
       "auxFxIfRxPort": auxFxIfRxPort,
       "auxFxIfInvPhysIndexOrZero": auxFxIfInvPhysIndexOrZero,
       "auxFxIfAdminStatus": auxFxIfAdminStatus,
       "auxFxIfOperStatus": auxFxIfOperStatus,
       "auxFxIfRxPowerLevel": auxFxIfRxPowerLevel,
       "auxFxIfLossOfSignalThreshold": auxFxIfLossOfSignalThreshold,
       "auxFxIfLossOfSignal": auxFxIfLossOfSignal,
       "auxFxIfObjectProperty": auxFxIfObjectProperty,
       "auxEquipmentList": auxEquipmentList,
       "auxEquipmentTable": auxEquipmentTable,
       "auxEquipmentEntry": auxEquipmentEntry,
       "auxEquipmentIndex": auxEquipmentIndex,
       "auxEquipmentName": auxEquipmentName,
       "auxEquipmentDescr": auxEquipmentDescr,
       "auxEquipmentSubrack": auxEquipmentSubrack,
       "auxEquipmentSlot": auxEquipmentSlot,
       "auxEquipmentAdminStatus": auxEquipmentAdminStatus,
       "auxEquipmentOperStatus": auxEquipmentOperStatus,
       "auxEquipmentPowerFailure": auxEquipmentPowerFailure,
       "auxEquipmentFanProblem": auxEquipmentFanProblem,
       "auxEquipmentObjectProperty": auxEquipmentObjectProperty,
       "auxEquipmentPumpsEol": auxEquipmentPumpsEol,
       "auxEquipmentSelfTestFailure": auxEquipmentSelfTestFailure,
       "auxEquipmentAmbientTemp": auxEquipmentAmbientTemp,
       "auxEquipmentRebootEquipment": auxEquipmentRebootEquipment,
       "auxEquipmentPowerAMissing": auxEquipmentPowerAMissing,
       "auxEquipmentPowerBMissing": auxEquipmentPowerBMissing,
       "auxEquipmentConfigurationMismatch": auxEquipmentConfigurationMismatch,
       "auxRamanIfList": auxRamanIfList,
       "auxRamanIfTable": auxRamanIfTable,
       "auxRamanIfEntry": auxRamanIfEntry,
       "auxRamanIfIndex": auxRamanIfIndex,
       "auxRamanIfName": auxRamanIfName,
       "auxRamanIfDescr": auxRamanIfDescr,
       "auxRamanIfSubrack": auxRamanIfSubrack,
       "auxRamanIfSlot": auxRamanIfSlot,
       "auxRamanIfTxPort": auxRamanIfTxPort,
       "auxRamanIfRxPort": auxRamanIfRxPort,
       "auxRamanIfInvPhysIndexOrZero": auxRamanIfInvPhysIndexOrZero,
       "auxRamanIfAdminStatus": auxRamanIfAdminStatus,
       "auxRamanIfOperStatus": auxRamanIfOperStatus,
       "auxRamanIfObjectProperty": auxRamanIfObjectProperty,
       "auxRamanIfModuleOperationMode": auxRamanIfModuleOperationMode,
       "auxRamanIfPumpsOperationMode": auxRamanIfPumpsOperationMode,
       "auxRamanIfPumpsOperationModeConfig": auxRamanIfPumpsOperationModeConfig,
       "auxRamanIfLineFiberType": auxRamanIfLineFiberType,
       "auxRamanIfAutoRestartProcTime": auxRamanIfAutoRestartProcTime,
       "auxRamanIfArpPauseStatus": auxRamanIfArpPauseStatus,
       "auxRamanIfPumpsStatus": auxRamanIfPumpsStatus,
       "auxRamanIfTotalPumpsPower": auxRamanIfTotalPumpsPower,
       "auxRamanIfPump1WantedPower": auxRamanIfPump1WantedPower,
       "auxRamanIfPump1ActualPower": auxRamanIfPump1ActualPower,
       "auxRamanIfPump1Current": auxRamanIfPump1Current,
       "auxRamanIfPump1Temperature": auxRamanIfPump1Temperature,
       "auxRamanIfPump2WantedPower": auxRamanIfPump2WantedPower,
       "auxRamanIfPump2ActualPower": auxRamanIfPump2ActualPower,
       "auxRamanIfPump2Current": auxRamanIfPump2Current,
       "auxRamanIfPump2Temperature": auxRamanIfPump2Temperature,
       "auxRamanIfWantedGain": auxRamanIfWantedGain,
       "auxRamanIfActualGain": auxRamanIfActualGain,
       "auxRamanIfReceivedPowerLevel": auxRamanIfReceivedPowerLevel,
       "auxRamanIfReflectionPowerLevel": auxRamanIfReflectionPowerLevel,
       "auxRamanIfReflectionPowerRatio": auxRamanIfReflectionPowerRatio,
       "auxRamanIf1510BandReceivedPowerLevel": auxRamanIf1510BandReceivedPowerLevel,
       "auxRamanIfOscReceivedPowerLevel": auxRamanIfOscReceivedPowerLevel,
       "auxRamanIfAPRState": auxRamanIfAPRState,
       "auxRamanIfOscDitherState": auxRamanIfOscDitherState,
       "auxRamanIfLineLossOfSignal": auxRamanIfLineLossOfSignal,
       "auxRamanIfOscDitherLos": auxRamanIfOscDitherLos,
       "auxRamanIfHighBackReflection": auxRamanIfHighBackReflection,
       "auxRamanIfHighLineOutputPower": auxRamanIfHighLineOutputPower,
       "auxRamanIfLowLineOutputPower": auxRamanIfLowLineOutputPower,
       "auxRamanIfModuleTempTooHigh": auxRamanIfModuleTempTooHigh,
       "auxRamanIfModuleTempHigh": auxRamanIfModuleTempHigh,
       "auxRamanIfPumpsTempTooHigh": auxRamanIfPumpsTempTooHigh,
       "auxRamanIfPumpsTempHigh": auxRamanIfPumpsTempHigh,
       "auxRamanIfAprShutdown": auxRamanIfAprShutdown,
       "auxRamanIfLineFiberDeteriorated": auxRamanIfLineFiberDeteriorated,
       "auxRamanIf1510BandPowerLos": auxRamanIf1510BandPowerLos,
       "auxRamanIfManualRestartTrial": auxRamanIfManualRestartTrial,
       "auxRamanIfModuleTemp": auxRamanIfModuleTemp,
       "auxRamanIfTxSignalStatus": auxRamanIfTxSignalStatus,
       "auxRamanIfRxSignalStatus": auxRamanIfRxSignalStatus,
       "auxRamanSafetyList": auxRamanSafetyList,
       "auxRamanSafetyTable": auxRamanSafetyTable,
       "auxRamanSafetyEntry": auxRamanSafetyEntry,
       "auxRamanSafetyIndex": auxRamanSafetyIndex,
       "auxRamanSafetyName": auxRamanSafetyName,
       "auxRamanSafetyDescr": auxRamanSafetyDescr,
       "auxRamanSafetySubrack": auxRamanSafetySubrack,
       "auxRamanSafetySlot": auxRamanSafetySlot,
       "auxRamanSafetyTxPort": auxRamanSafetyTxPort,
       "auxRamanSafetyRxPort": auxRamanSafetyRxPort,
       "auxRamanSafetyInvPhysIndexOrZero": auxRamanSafetyInvPhysIndexOrZero,
       "auxRamanSafetyObjectProperty": auxRamanSafetyObjectProperty,
       "auxRamanSafetyShutDownAtInputLoss": auxRamanSafetyShutDownAtInputLoss,
       "auxRamanSafetyShutDownAtHighTemp": auxRamanSafetyShutDownAtHighTemp,
       "auxRamanSafetyShutDownAtHighBackReflection": auxRamanSafetyShutDownAtHighBackReflection,
       "auxRamanSafetyHighBackReflectionThreshold": auxRamanSafetyHighBackReflectionThreshold,
       "auxRamanSafetyShutDownAtOscLoss": auxRamanSafetyShutDownAtOscLoss,
       "auxRamanSafetyShutDownAt1510BandDrop": auxRamanSafetyShutDownAt1510BandDrop,
       "auxRamanSafetyShutDownAtInputLossConfig": auxRamanSafetyShutDownAtInputLossConfig,
       "auxRamanSafetyShutDownAtHighTempConfig": auxRamanSafetyShutDownAtHighTempConfig,
       "auxRamanSafetyShutDownAtHighBackReflectionConfig": auxRamanSafetyShutDownAtHighBackReflectionConfig,
       "auxRamanSafetyShutDownAtOscLossConfig": auxRamanSafetyShutDownAtOscLossConfig,
       "auxRamanSafetyShutDownAt1510BandDropConfig": auxRamanSafetyShutDownAt1510BandDropConfig,
       "auxRamanSafetyPasswd": auxRamanSafetyPasswd,
       "auxRamanSafetyPasswdConfig": auxRamanSafetyPasswdConfig,
       "auxRamanSafety1510BandDropThreshold": auxRamanSafety1510BandDropThreshold,
       "auxRamanSafetyInhibitStartAtOscLoss": auxRamanSafetyInhibitStartAtOscLoss,
       "auxRamanSafetyInhibitStartAtOscLossConfig": auxRamanSafetyInhibitStartAtOscLossConfig,
       "auxRamanSafetyShutDownAtLowBandDrop": auxRamanSafetyShutDownAtLowBandDrop,
       "auxRamanSafetyLowBandScatteringThreshold": auxRamanSafetyLowBandScatteringThreshold,
       "auxRamanSafetyShutDownAtLowBandDropConfig": auxRamanSafetyShutDownAtLowBandDropConfig,
       "auxRamanSafetyAmplifierSwitch": auxRamanSafetyAmplifierSwitch,
       "auxRamanSafetyAmplifierSwitchConfig": auxRamanSafetyAmplifierSwitchConfig,
       "auxRamanSafetyLowBandScatteringTolerance": auxRamanSafetyLowBandScatteringTolerance,
       "auxPEIfList": auxPEIfList,
       "auxPEIfTable": auxPEIfTable,
       "auxPEIfEntry": auxPEIfEntry,
       "auxPEIfIndex": auxPEIfIndex,
       "auxPEIfName": auxPEIfName,
       "auxPEIfDescr": auxPEIfDescr,
       "auxPEIfSubrack": auxPEIfSubrack,
       "auxPEIfSlot": auxPEIfSlot,
       "auxPEIfTxPort": auxPEIfTxPort,
       "auxPEIfRxPort": auxPEIfRxPort,
       "auxPEIfInvPhysIndexOrZero": auxPEIfInvPhysIndexOrZero,
       "auxPEIfAdminStatus": auxPEIfAdminStatus,
       "auxPEIfOperStatus": auxPEIfOperStatus,
       "auxPEIfObjectProperty": auxPEIfObjectProperty,
       "auxPEIfPumpsOperationMode": auxPEIfPumpsOperationMode,
       "auxPEIfPumpsOperationModeConfig": auxPEIfPumpsOperationModeConfig,
       "auxPEIfAutoRestartProcTime": auxPEIfAutoRestartProcTime,
       "auxPEIfPumpsStatus": auxPEIfPumpsStatus,
       "auxPEIfWantedPower": auxPEIfWantedPower,
       "auxPEIfWantedGain": auxPEIfWantedGain,
       "auxPEIfPumpsTotalCurrent": auxPEIfPumpsTotalCurrent,
       "auxPEIfPump1Temperature": auxPEIfPump1Temperature,
       "auxPEIfActualGain": auxPEIfActualGain,
       "auxPEIfReceivedPowerLevel": auxPEIfReceivedPowerLevel,
       "auxPEIfCombinedOutPwrLevel": auxPEIfCombinedOutPwrLevel,
       "auxPEIfReflectionPowerLevel": auxPEIfReflectionPowerLevel,
       "auxPEIfReflectionPowerRatio": auxPEIfReflectionPowerRatio,
       "auxPEIfLowBandScatteredPowerLevel": auxPEIfLowBandScatteredPowerLevel,
       "auxPEIfLineLossOfSignal": auxPEIfLineLossOfSignal,
       "auxPEIfHighBackReflection": auxPEIfHighBackReflection,
       "auxPEIfAutoPowerReduction": auxPEIfAutoPowerReduction,
       "auxPEIfLowLineOutputPower": auxPEIfLowLineOutputPower,
       "auxPEIfModuleTempTooHigh": auxPEIfModuleTempTooHigh,
       "auxPEIfModuleTempHigh": auxPEIfModuleTempHigh,
       "auxPEIfPumpsTempTooHigh": auxPEIfPumpsTempTooHigh,
       "auxPEIfPumpsTempHigh": auxPEIfPumpsTempHigh,
       "auxPEIfModuleTemp": auxPEIfModuleTemp,
       "auxPEIfPump2Temperature": auxPEIfPump2Temperature,
       "auxNodeList": auxNodeList,
       "auxNodeTable": auxNodeTable,
       "auxNodeEntry": auxNodeEntry,
       "auxNodeIndex": auxNodeIndex,
       "auxNodeName": auxNodeName,
       "auxNodeDescr": auxNodeDescr,
       "auxNodeIpAddress": auxNodeIpAddress,
       "auxNodePort": auxNodePort,
       "auxNodeEventPort": auxNodeEventPort,
       "auxNodeTime": auxNodeTime,
       "auxNodeNtpPrimary": auxNodeNtpPrimary,
       "auxNodeNtpSecondary": auxNodeNtpSecondary,
       "auxNodeChangeLocalTime": auxNodeChangeLocalTime,
       "auxNodeHostUnreachable": auxNodeHostUnreachable,
       "auxCabinetList": auxCabinetList,
       "auxCabinetTable": auxCabinetTable,
       "auxCabinetEntry": auxCabinetEntry,
       "auxCabinetIndex": auxCabinetIndex,
       "auxCabinetName": auxCabinetName,
       "auxCabinetDescr": auxCabinetDescr,
       "auxCabinetAdminStatus": auxCabinetAdminStatus,
       "auxCabinetOperStatus": auxCabinetOperStatus,
       "auxCabinetUpId": auxCabinetUpId,
       "auxCabinetIndoorTemp": auxCabinetIndoorTemp,
       "auxCabinetOutdoorTemp": auxCabinetOutdoorTemp,
       "auxCabinetOperMode": auxCabinetOperMode,
       "auxCabinetDoorAlarm": auxCabinetDoorAlarm,
       "auxCabinetSPDAlarm": auxCabinetSPDAlarm,
       "auxCabinetHighTempAlarm": auxCabinetHighTempAlarm,
       "auxCabinetCtrlFailAlarm": auxCabinetCtrlFailAlarm,
       "auxCabinetHeatFailAlarm": auxCabinetHeatFailAlarm,
       "auxCabinetExtTempFailAlarm": auxCabinetExtTempFailAlarm,
       "auxCabinetIntTempFailAlarm": auxCabinetIntTempFailAlarm,
       "auxFanList": auxFanList,
       "auxFanTable": auxFanTable,
       "auxFanEntry": auxFanEntry,
       "auxFanIndex": auxFanIndex,
       "auxFanName": auxFanName,
       "auxFanDescr": auxFanDescr,
       "auxFanAdminStatus": auxFanAdminStatus,
       "auxFanOperStatus": auxFanOperStatus,
       "auxFanUpId": auxFanUpId,
       "auxFanFailure": auxFanFailure,
       "auxFanRPM": auxFanRPM,
       "auxFanGroupList": auxFanGroupList,
       "auxFanGroupTable": auxFanGroupTable,
       "auxFanGroupEntry": auxFanGroupEntry,
       "auxFanGroupIndex": auxFanGroupIndex,
       "auxFanGroupName": auxFanGroupName,
       "auxFanGroupDescr": auxFanGroupDescr,
       "auxFanGroupAdminStatus": auxFanGroupAdminStatus,
       "auxFanGroupOperStatus": auxFanGroupOperStatus,
       "auxFanGroupUpId": auxFanGroupUpId,
       "auxFanGroupFailure": auxFanGroupFailure}
)
