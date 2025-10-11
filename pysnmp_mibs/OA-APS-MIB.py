# SNMP MIB module (OA-APS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/OA-APS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:05:20 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

oaApsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 20)
)
if mibBuilder.loadTexts:
    oaApsMIB.setRevisions(
        ("2012-07-30 00:00",
         "2012-02-07 00:00",
         "2011-09-15 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ApsSwitchCommand(TextualConvention, Integer32):
    status = "current"
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
        *(("noCmd", 1),
          ("clear", 2),
          ("lockoutOfProtection", 3),
          ("forcedSwitchWorkToProtect", 4),
          ("forcedSwitchProtectToWork", 5),
          ("manualSwitchWorkToProtect", 6),
          ("manualSwitchProtectToWork", 7))
    )



# MIB Managed Objects in the order of their OIDs

_Oaccess_ObjectIdentity = ObjectIdentity
oaccess = _Oaccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926)
)
_OaManagement_ObjectIdentity = ObjectIdentity
oaManagement = _OaManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1)
)
_OaLambdaDriver_ObjectIdentity = ObjectIdentity
oaLambdaDriver = _OaLambdaDriver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41)
)
_OaApsConfig_ObjectIdentity = ObjectIdentity
oaApsConfig = _OaApsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 20, 1)
)
_OaApsModeConfigTable_Object = MibTable
oaApsModeConfigTable = _OaApsModeConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 20, 1, 1)
)
if mibBuilder.loadTexts:
    oaApsModeConfigTable.setStatus("current")
_OaApsModeConfigEntry_Object = MibTableRow
oaApsModeConfigEntry = _OaApsModeConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 20, 1, 1, 1)
)
oaApsModeConfigEntry.setIndexNames(
    (0, "OA-APS-MIB", "oaApsModeConfigSlotIndex"),
)
if mibBuilder.loadTexts:
    oaApsModeConfigEntry.setStatus("current")


class _OaApsModeConfigSlotIndex_Type(Integer32):
    """Custom type oaApsModeConfigSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OaApsModeConfigSlotIndex_Type.__name__ = "Integer32"
_OaApsModeConfigSlotIndex_Object = MibTableColumn
oaApsModeConfigSlotIndex = _OaApsModeConfigSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 20, 1, 1, 1, 1),
    _OaApsModeConfigSlotIndex_Type()
)
oaApsModeConfigSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaApsModeConfigSlotIndex.setStatus("current")


class _OaApsModeConfigMode_Type(Integer32):
    """Custom type oaApsModeConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAps", 1),
          ("apsProtect", 2))
    )


_OaApsModeConfigMode_Type.__name__ = "Integer32"
_OaApsModeConfigMode_Object = MibTableColumn
oaApsModeConfigMode = _OaApsModeConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 20, 1, 1, 1, 2),
    _OaApsModeConfigMode_Type()
)
oaApsModeConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaApsModeConfigMode.setStatus("current")


class _OaApsModeConfigRevert_Type(Integer32):
    """Custom type oaApsModeConfigRevert based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonRevertive", 1),
          ("revertive", 2))
    )


_OaApsModeConfigRevert_Type.__name__ = "Integer32"
_OaApsModeConfigRevert_Object = MibTableColumn
oaApsModeConfigRevert = _OaApsModeConfigRevert_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 20, 1, 1, 1, 3),
    _OaApsModeConfigRevert_Type()
)
oaApsModeConfigRevert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaApsModeConfigRevert.setStatus("current")


class _OaApsModeConfigWaitToRestore_Type(Integer32):
    """Custom type oaApsModeConfigWaitToRestore based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 720),
    )


_OaApsModeConfigWaitToRestore_Type.__name__ = "Integer32"
_OaApsModeConfigWaitToRestore_Object = MibTableColumn
oaApsModeConfigWaitToRestore = _OaApsModeConfigWaitToRestore_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 20, 1, 1, 1, 4),
    _OaApsModeConfigWaitToRestore_Type()
)
oaApsModeConfigWaitToRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaApsModeConfigWaitToRestore.setStatus("current")
if mibBuilder.loadTexts:
    oaApsModeConfigWaitToRestore.setUnits("seconds")
_OaApsModeConfigGroups_Type = Gauge32
_OaApsModeConfigGroups_Object = MibTableColumn
oaApsModeConfigGroups = _OaApsModeConfigGroups_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 20, 1, 1, 1, 5),
    _OaApsModeConfigGroups_Type()
)
oaApsModeConfigGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaApsModeConfigGroups.setStatus("current")
_OaApsModeVersion_Type = Integer32
_OaApsModeVersion_Object = MibTableColumn
oaApsModeVersion = _OaApsModeVersion_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 20, 1, 1, 1, 6),
    _OaApsModeVersion_Type()
)
oaApsModeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaApsModeVersion.setStatus("current")
_OaApsConfigGroupTable_Object = MibTable
oaApsConfigGroupTable = _OaApsConfigGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 20, 1, 5)
)
if mibBuilder.loadTexts:
    oaApsConfigGroupTable.setStatus("current")
_OaApsConfigGroupEntry_Object = MibTableRow
oaApsConfigGroupEntry = _OaApsConfigGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 20, 1, 5, 1)
)
oaApsConfigGroupEntry.setIndexNames(
    (0, "OA-APS-MIB", "oaApsConfigGroupSlotIndex"),
    (0, "OA-APS-MIB", "oaApsConfigGroupId"),
)
if mibBuilder.loadTexts:
    oaApsConfigGroupEntry.setStatus("current")


class _OaApsConfigGroupSlotIndex_Type(Integer32):
    """Custom type oaApsConfigGroupSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OaApsConfigGroupSlotIndex_Type.__name__ = "Integer32"
_OaApsConfigGroupSlotIndex_Object = MibTableColumn
oaApsConfigGroupSlotIndex = _OaApsConfigGroupSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 20, 1, 5, 1, 1),
    _OaApsConfigGroupSlotIndex_Type()
)
oaApsConfigGroupSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaApsConfigGroupSlotIndex.setStatus("current")


class _OaApsConfigGroupId_Type(Integer32):
    """Custom type oaApsConfigGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OaApsConfigGroupId_Type.__name__ = "Integer32"
_OaApsConfigGroupId_Object = MibTableColumn
oaApsConfigGroupId = _OaApsConfigGroupId_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 20, 1, 5, 1, 2),
    _OaApsConfigGroupId_Type()
)
oaApsConfigGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaApsConfigGroupId.setStatus("current")


class _OaApsConfigGroupName_Type(DisplayString):
    """Custom type oaApsConfigGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_OaApsConfigGroupName_Type.__name__ = "DisplayString"
_OaApsConfigGroupName_Object = MibTableColumn
oaApsConfigGroupName = _OaApsConfigGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 20, 1, 5, 1, 3),
    _OaApsConfigGroupName_Type()
)
oaApsConfigGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaApsConfigGroupName.setStatus("current")


class _OaApsConfigGroupPortMembers_Type(OctetString):
    """Custom type oaApsConfigGroupPortMembers based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_OaApsConfigGroupPortMembers_Type.__name__ = "OctetString"
_OaApsConfigGroupPortMembers_Object = MibTableColumn
oaApsConfigGroupPortMembers = _OaApsConfigGroupPortMembers_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 20, 1, 5, 1, 4),
    _OaApsConfigGroupPortMembers_Type()
)
oaApsConfigGroupPortMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaApsConfigGroupPortMembers.setStatus("current")


class _OaApsConfigGroupWorkingLinePort_Type(Integer32):
    """Custom type oaApsConfigGroupWorkingLinePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OaApsConfigGroupWorkingLinePort_Type.__name__ = "Integer32"
_OaApsConfigGroupWorkingLinePort_Object = MibTableColumn
oaApsConfigGroupWorkingLinePort = _OaApsConfigGroupWorkingLinePort_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 20, 1, 5, 1, 5),
    _OaApsConfigGroupWorkingLinePort_Type()
)
oaApsConfigGroupWorkingLinePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaApsConfigGroupWorkingLinePort.setStatus("current")


class _OaApsConfigGroupProtectLinePort_Type(Integer32):
    """Custom type oaApsConfigGroupProtectLinePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OaApsConfigGroupProtectLinePort_Type.__name__ = "Integer32"
_OaApsConfigGroupProtectLinePort_Object = MibTableColumn
oaApsConfigGroupProtectLinePort = _OaApsConfigGroupProtectLinePort_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 20, 1, 5, 1, 6),
    _OaApsConfigGroupProtectLinePort_Type()
)
oaApsConfigGroupProtectLinePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaApsConfigGroupProtectLinePort.setStatus("current")


class _OaApsConfigGroupWorkingStatus_Type(Integer32):
    """Custom type oaApsConfigGroupWorkingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inActive", 1),
          ("active", 2),
          ("standBy", 3))
    )


_OaApsConfigGroupWorkingStatus_Type.__name__ = "Integer32"
_OaApsConfigGroupWorkingStatus_Object = MibTableColumn
oaApsConfigGroupWorkingStatus = _OaApsConfigGroupWorkingStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 20, 1, 5, 1, 7),
    _OaApsConfigGroupWorkingStatus_Type()
)
oaApsConfigGroupWorkingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaApsConfigGroupWorkingStatus.setStatus("current")


class _OaApsConfigGroupProtectStatus_Type(Integer32):
    """Custom type oaApsConfigGroupProtectStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inActive", 1),
          ("active", 2),
          ("standBy", 3))
    )


_OaApsConfigGroupProtectStatus_Type.__name__ = "Integer32"
_OaApsConfigGroupProtectStatus_Object = MibTableColumn
oaApsConfigGroupProtectStatus = _OaApsConfigGroupProtectStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 20, 1, 5, 1, 8),
    _OaApsConfigGroupProtectStatus_Type()
)
oaApsConfigGroupProtectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaApsConfigGroupProtectStatus.setStatus("current")
_OaApsConfigGroupCmdSwitchTrans_Type = ApsSwitchCommand
_OaApsConfigGroupCmdSwitchTrans_Object = MibTableColumn
oaApsConfigGroupCmdSwitchTrans = _OaApsConfigGroupCmdSwitchTrans_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 20, 1, 5, 1, 9),
    _OaApsConfigGroupCmdSwitchTrans_Type()
)
oaApsConfigGroupCmdSwitchTrans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaApsConfigGroupCmdSwitchTrans.setStatus("current")
_OaApsConfigGroupCmdSwitchRec_Type = ApsSwitchCommand
_OaApsConfigGroupCmdSwitchRec_Object = MibTableColumn
oaApsConfigGroupCmdSwitchRec = _OaApsConfigGroupCmdSwitchRec_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 20, 1, 5, 1, 10),
    _OaApsConfigGroupCmdSwitchRec_Type()
)
oaApsConfigGroupCmdSwitchRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaApsConfigGroupCmdSwitchRec.setStatus("current")
_OaApsConfigGroupCmdSwitchStatus_Type = ApsSwitchCommand
_OaApsConfigGroupCmdSwitchStatus_Object = MibTableColumn
oaApsConfigGroupCmdSwitchStatus = _OaApsConfigGroupCmdSwitchStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 20, 1, 5, 1, 11),
    _OaApsConfigGroupCmdSwitchStatus_Type()
)
oaApsConfigGroupCmdSwitchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaApsConfigGroupCmdSwitchStatus.setStatus("current")


class _OaApsConfigGroupWorkingLineDefect_Type(Bits):
    """Custom type oaApsConfigGroupWorkingLineDefect based on Bits"""
    namedValues = NamedValues(
        *(("noDefect", 0),
          ("odu1AIS", 1),
          ("otu2LOS", 2),
          ("otu2BDI", 3))
    )

_OaApsConfigGroupWorkingLineDefect_Type.__name__ = "Bits"
_OaApsConfigGroupWorkingLineDefect_Object = MibTableColumn
oaApsConfigGroupWorkingLineDefect = _OaApsConfigGroupWorkingLineDefect_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 20, 1, 5, 1, 12),
    _OaApsConfigGroupWorkingLineDefect_Type()
)
oaApsConfigGroupWorkingLineDefect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaApsConfigGroupWorkingLineDefect.setStatus("current")


class _OaApsConfigGroupProtectLineDefect_Type(Bits):
    """Custom type oaApsConfigGroupProtectLineDefect based on Bits"""
    namedValues = NamedValues(
        *(("noDefect", 0),
          ("odu1AIS", 1),
          ("otu2LOS", 2),
          ("otu2BDI", 3))
    )

_OaApsConfigGroupProtectLineDefect_Type.__name__ = "Bits"
_OaApsConfigGroupProtectLineDefect_Object = MibTableColumn
oaApsConfigGroupProtectLineDefect = _OaApsConfigGroupProtectLineDefect_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 20, 1, 5, 1, 13),
    _OaApsConfigGroupProtectLineDefect_Type()
)
oaApsConfigGroupProtectLineDefect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaApsConfigGroupProtectLineDefect.setStatus("current")
_OaApsMIBNotifications_ObjectIdentity = ObjectIdentity
oaApsMIBNotifications = _OaApsMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 20, 2)
)
_OaApsMIBConformance_ObjectIdentity = ObjectIdentity
oaApsMIBConformance = _OaApsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 20, 3)
)
_OaApsMIBCompliances_ObjectIdentity = ObjectIdentity
oaApsMIBCompliances = _OaApsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 20, 3, 1)
)
_OaApsMIBGroups_ObjectIdentity = ObjectIdentity
oaApsMIBGroups = _OaApsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 20, 3, 2)
)

# Managed Objects groups

oaApsMibMandatoryConfigMode = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 20, 3, 2, 1)
)
oaApsMibMandatoryConfigMode.setObjects(
      *(("OA-APS-MIB", "oaApsModeConfigMode"),
        ("OA-APS-MIB", "oaApsModeConfigRevert"),
        ("OA-APS-MIB", "oaApsModeConfigWaitToRestore"),
        ("OA-APS-MIB", "oaApsModeConfigGroups"),
        ("OA-APS-MIB", "oaApsModeVersion"))
)
if mibBuilder.loadTexts:
    oaApsMibMandatoryConfigMode.setStatus("current")

oaApsMibMandatoryConfigGroupMode = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 20, 3, 2, 2)
)
oaApsMibMandatoryConfigGroupMode.setObjects(
      *(("OA-APS-MIB", "oaApsConfigGroupName"),
        ("OA-APS-MIB", "oaApsConfigGroupPortMembers"),
        ("OA-APS-MIB", "oaApsConfigGroupWorkingLinePort"),
        ("OA-APS-MIB", "oaApsConfigGroupProtectLinePort"),
        ("OA-APS-MIB", "oaApsConfigGroupWorkingStatus"),
        ("OA-APS-MIB", "oaApsConfigGroupProtectStatus"),
        ("OA-APS-MIB", "oaApsConfigGroupCmdSwitchTrans"),
        ("OA-APS-MIB", "oaApsConfigGroupCmdSwitchRec"),
        ("OA-APS-MIB", "oaApsConfigGroupCmdSwitchStatus"),
        ("OA-APS-MIB", "oaApsConfigGroupWorkingLineDefect"),
        ("OA-APS-MIB", "oaApsConfigGroupProtectLineDefect"))
)
if mibBuilder.loadTexts:
    oaApsMibMandatoryConfigGroupMode.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

oaApsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 20, 3, 1, 1)
)
oaApsMIBCompliance.setObjects(
      *(("OA-APS-MIB", "oaApsMibMandatoryConfigMode"),
        ("OA-APS-MIB", "oaApsMibMandatoryConfigGroupMode"))
)
if mibBuilder.loadTexts:
    oaApsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OA-APS-MIB",
    **{"ApsSwitchCommand": ApsSwitchCommand,
       "oaccess": oaccess,
       "oaManagement": oaManagement,
       "oaLambdaDriver": oaLambdaDriver,
       "oaApsMIB": oaApsMIB,
       "oaApsConfig": oaApsConfig,
       "oaApsModeConfigTable": oaApsModeConfigTable,
       "oaApsModeConfigEntry": oaApsModeConfigEntry,
       "oaApsModeConfigSlotIndex": oaApsModeConfigSlotIndex,
       "oaApsModeConfigMode": oaApsModeConfigMode,
       "oaApsModeConfigRevert": oaApsModeConfigRevert,
       "oaApsModeConfigWaitToRestore": oaApsModeConfigWaitToRestore,
       "oaApsModeConfigGroups": oaApsModeConfigGroups,
       "oaApsModeVersion": oaApsModeVersion,
       "oaApsConfigGroupTable": oaApsConfigGroupTable,
       "oaApsConfigGroupEntry": oaApsConfigGroupEntry,
       "oaApsConfigGroupSlotIndex": oaApsConfigGroupSlotIndex,
       "oaApsConfigGroupId": oaApsConfigGroupId,
       "oaApsConfigGroupName": oaApsConfigGroupName,
       "oaApsConfigGroupPortMembers": oaApsConfigGroupPortMembers,
       "oaApsConfigGroupWorkingLinePort": oaApsConfigGroupWorkingLinePort,
       "oaApsConfigGroupProtectLinePort": oaApsConfigGroupProtectLinePort,
       "oaApsConfigGroupWorkingStatus": oaApsConfigGroupWorkingStatus,
       "oaApsConfigGroupProtectStatus": oaApsConfigGroupProtectStatus,
       "oaApsConfigGroupCmdSwitchTrans": oaApsConfigGroupCmdSwitchTrans,
       "oaApsConfigGroupCmdSwitchRec": oaApsConfigGroupCmdSwitchRec,
       "oaApsConfigGroupCmdSwitchStatus": oaApsConfigGroupCmdSwitchStatus,
       "oaApsConfigGroupWorkingLineDefect": oaApsConfigGroupWorkingLineDefect,
       "oaApsConfigGroupProtectLineDefect": oaApsConfigGroupProtectLineDefect,
       "oaApsMIBNotifications": oaApsMIBNotifications,
       "oaApsMIBConformance": oaApsMIBConformance,
       "oaApsMIBCompliances": oaApsMIBCompliances,
       "oaApsMIBCompliance": oaApsMIBCompliance,
       "oaApsMIBGroups": oaApsMIBGroups,
       "oaApsMibMandatoryConfigMode": oaApsMibMandatoryConfigMode,
       "oaApsMibMandatoryConfigGroupMode": oaApsMibMandatoryConfigGroupMode}
)
