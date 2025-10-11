# SNMP MIB module (HM2-PLATFORM-DOT1X-ADVANCED-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hirschmann/HM2-PLATFORM-DOT1X-ADVANCED-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:54:00 2025
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

(HmEnabledStatus,
 HmTimeSeconds1970,
 hm2PlatformMibs) = mibBuilder.importSymbols(
    "HM2-TC-MIB",
    "HmEnabledStatus",
    "HmTimeSeconds1970",
    "hm2PlatformMibs")

(dot1xPaePortNumber,) = mibBuilder.importSymbols(
    "IEEE8021-PAE-MIB",
    "dot1xPaePortNumber")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

hm2PlatformDot1xAdvanced = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 36)
)
if mibBuilder.loadTexts:
    hm2PlatformDot1xAdvanced.setRevisions(
        ("2011-10-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Dot1xPortControlMode(TextualConvention, Integer32):
    status = "current"
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
        *(("forceUnauthorized", 1),
          ("auto", 2),
          ("forceAuthorized", 3),
          ("multiClient", 4))
    )



class Dot1xSessionTerminationAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("reauthenticate", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Hm2AgentDot1xEnhancementConfigGroup_ObjectIdentity = ObjectIdentity
hm2AgentDot1xEnhancementConfigGroup = _Hm2AgentDot1xEnhancementConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 1)
)


class _Hm2AgentDot1xRadiusVlanAssignment_Type(HmEnabledStatus):
    """Custom type hm2AgentDot1xRadiusVlanAssignment based on HmEnabledStatus"""
    defaultValue = 2


_Hm2AgentDot1xRadiusVlanAssignment_Type.__name__ = "HmEnabledStatus"
_Hm2AgentDot1xRadiusVlanAssignment_Object = MibScalar
hm2AgentDot1xRadiusVlanAssignment = _Hm2AgentDot1xRadiusVlanAssignment_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 1, 1),
    _Hm2AgentDot1xRadiusVlanAssignment_Type()
)
hm2AgentDot1xRadiusVlanAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDot1xRadiusVlanAssignment.setStatus("current")


class _Hm2AgentDot1xDynamicVlanCreationMode_Type(HmEnabledStatus):
    """Custom type hm2AgentDot1xDynamicVlanCreationMode based on HmEnabledStatus"""
    defaultValue = 2


_Hm2AgentDot1xDynamicVlanCreationMode_Type.__name__ = "HmEnabledStatus"
_Hm2AgentDot1xDynamicVlanCreationMode_Object = MibScalar
hm2AgentDot1xDynamicVlanCreationMode = _Hm2AgentDot1xDynamicVlanCreationMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 1, 2),
    _Hm2AgentDot1xDynamicVlanCreationMode_Type()
)
hm2AgentDot1xDynamicVlanCreationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDot1xDynamicVlanCreationMode.setStatus("current")


class _Hm2AgentDot1xStatisticsClear_Type(HmEnabledStatus):
    """Custom type hm2AgentDot1xStatisticsClear based on HmEnabledStatus"""
    defaultValue = 2


_Hm2AgentDot1xStatisticsClear_Type.__name__ = "HmEnabledStatus"
_Hm2AgentDot1xStatisticsClear_Object = MibScalar
hm2AgentDot1xStatisticsClear = _Hm2AgentDot1xStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 1, 248),
    _Hm2AgentDot1xStatisticsClear_Type()
)
hm2AgentDot1xStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDot1xStatisticsClear.setStatus("current")
_Hm2AgentDot1xPortStatsClearTable_Object = MibTable
hm2AgentDot1xPortStatsClearTable = _Hm2AgentDot1xPortStatsClearTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 1, 249)
)
if mibBuilder.loadTexts:
    hm2AgentDot1xPortStatsClearTable.setStatus("current")
_Hm2AgentDot1xPortStatsClearEntry_Object = MibTableRow
hm2AgentDot1xPortStatsClearEntry = _Hm2AgentDot1xPortStatsClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 1, 249, 1)
)
hm2AgentDot1xPortStatsClearEntry.setIndexNames(
    (0, "HM2-PLATFORM-DOT1X-ADVANCED-MIB", "hm2AgentDot1xStatsIfIndex"),
)
if mibBuilder.loadTexts:
    hm2AgentDot1xPortStatsClearEntry.setStatus("current")
_Hm2AgentDot1xStatsIfIndex_Type = Unsigned32
_Hm2AgentDot1xStatsIfIndex_Object = MibTableColumn
hm2AgentDot1xStatsIfIndex = _Hm2AgentDot1xStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 1, 249, 1, 1),
    _Hm2AgentDot1xStatsIfIndex_Type()
)
hm2AgentDot1xStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1xStatsIfIndex.setStatus("current")


class _Hm2AgentDot1xPortStatsClear_Type(HmEnabledStatus):
    """Custom type hm2AgentDot1xPortStatsClear based on HmEnabledStatus"""
    defaultValue = 2


_Hm2AgentDot1xPortStatsClear_Type.__name__ = "HmEnabledStatus"
_Hm2AgentDot1xPortStatsClear_Object = MibTableColumn
hm2AgentDot1xPortStatsClear = _Hm2AgentDot1xPortStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 1, 249, 1, 2),
    _Hm2AgentDot1xPortStatsClear_Type()
)
hm2AgentDot1xPortStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDot1xPortStatsClear.setStatus("current")


class _Hm2AgentDot1xMABFormatGroupSize_Type(Integer32):
    """Custom type hm2AgentDot1xMABFormatGroupSize based on Integer32"""
    defaultValue = 12

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              12)
        )
    )
    namedValues = NamedValues(
        *(("group-size-1", 1),
          ("group-size-2", 2),
          ("group-size-4", 4),
          ("group-size-12", 12))
    )


_Hm2AgentDot1xMABFormatGroupSize_Type.__name__ = "Integer32"
_Hm2AgentDot1xMABFormatGroupSize_Object = MibScalar
hm2AgentDot1xMABFormatGroupSize = _Hm2AgentDot1xMABFormatGroupSize_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 1, 250),
    _Hm2AgentDot1xMABFormatGroupSize_Type()
)
hm2AgentDot1xMABFormatGroupSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDot1xMABFormatGroupSize.setStatus("current")


class _Hm2AgentDot1xMABFormatGroupSeparator_Type(Integer32):
    """Custom type hm2AgentDot1xMABFormatGroupSeparator based on Integer32"""
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
        *(("hyphen", 1),
          ("colon", 2),
          ("dot", 3))
    )


_Hm2AgentDot1xMABFormatGroupSeparator_Type.__name__ = "Integer32"
_Hm2AgentDot1xMABFormatGroupSeparator_Object = MibScalar
hm2AgentDot1xMABFormatGroupSeparator = _Hm2AgentDot1xMABFormatGroupSeparator_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 1, 251),
    _Hm2AgentDot1xMABFormatGroupSeparator_Type()
)
hm2AgentDot1xMABFormatGroupSeparator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDot1xMABFormatGroupSeparator.setStatus("current")


class _Hm2AgentDot1xMABFormatLetterCase_Type(Integer32):
    """Custom type hm2AgentDot1xMABFormatLetterCase based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lower-case", 1),
          ("upper-case", 2))
    )


_Hm2AgentDot1xMABFormatLetterCase_Type.__name__ = "Integer32"
_Hm2AgentDot1xMABFormatLetterCase_Object = MibScalar
hm2AgentDot1xMABFormatLetterCase = _Hm2AgentDot1xMABFormatLetterCase_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 1, 252),
    _Hm2AgentDot1xMABFormatLetterCase_Type()
)
hm2AgentDot1xMABFormatLetterCase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDot1xMABFormatLetterCase.setStatus("current")


class _Hm2AgentDot1xMABPassword_Type(SnmpAdminString):
    """Custom type hm2AgentDot1xMABPassword based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hm2AgentDot1xMABPassword_Type.__name__ = "SnmpAdminString"
_Hm2AgentDot1xMABPassword_Object = MibScalar
hm2AgentDot1xMABPassword = _Hm2AgentDot1xMABPassword_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 1, 253),
    _Hm2AgentDot1xMABPassword_Type()
)
hm2AgentDot1xMABPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDot1xMABPassword.setStatus("current")
_Hm2AgentDot1xPortConfigGroup_ObjectIdentity = ObjectIdentity
hm2AgentDot1xPortConfigGroup = _Hm2AgentDot1xPortConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 2)
)
_Hm2AgentDot1xPortConfigTable_Object = MibTable
hm2AgentDot1xPortConfigTable = _Hm2AgentDot1xPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 2, 1)
)
if mibBuilder.loadTexts:
    hm2AgentDot1xPortConfigTable.setStatus("current")
_Hm2AgentDot1xPortConfigEntry_Object = MibTableRow
hm2AgentDot1xPortConfigEntry = _Hm2AgentDot1xPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 2, 1, 1)
)
hm2AgentDot1xPortConfigEntry.setIndexNames(
    (0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"),
)
if mibBuilder.loadTexts:
    hm2AgentDot1xPortConfigEntry.setStatus("current")


class _Hm2AgentDot1xPortControlMode_Type(Dot1xPortControlMode):
    """Custom type hm2AgentDot1xPortControlMode based on Dot1xPortControlMode"""
    defaultValue = 3


_Hm2AgentDot1xPortControlMode_Type.__name__ = "Dot1xPortControlMode"
_Hm2AgentDot1xPortControlMode_Object = MibTableColumn
hm2AgentDot1xPortControlMode = _Hm2AgentDot1xPortControlMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 2, 1, 1, 1),
    _Hm2AgentDot1xPortControlMode_Type()
)
hm2AgentDot1xPortControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDot1xPortControlMode.setStatus("current")


class _Hm2AgentDot1xGuestVlanId_Type(Unsigned32):
    """Custom type hm2AgentDot1xGuestVlanId based on Unsigned32"""
    defaultValue = 0


_Hm2AgentDot1xGuestVlanId_Type.__name__ = "Unsigned32"
_Hm2AgentDot1xGuestVlanId_Object = MibTableColumn
hm2AgentDot1xGuestVlanId = _Hm2AgentDot1xGuestVlanId_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 2, 1, 1, 2),
    _Hm2AgentDot1xGuestVlanId_Type()
)
hm2AgentDot1xGuestVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDot1xGuestVlanId.setStatus("current")


class _Hm2AgentDot1xGuestVlanPeriod_Type(Unsigned32):
    """Custom type hm2AgentDot1xGuestVlanPeriod based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_Hm2AgentDot1xGuestVlanPeriod_Type.__name__ = "Unsigned32"
_Hm2AgentDot1xGuestVlanPeriod_Object = MibTableColumn
hm2AgentDot1xGuestVlanPeriod = _Hm2AgentDot1xGuestVlanPeriod_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 2, 1, 1, 3),
    _Hm2AgentDot1xGuestVlanPeriod_Type()
)
hm2AgentDot1xGuestVlanPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1xGuestVlanPeriod.setStatus("current")


class _Hm2AgentDot1xUnauthenticatedVlan_Type(Unsigned32):
    """Custom type hm2AgentDot1xUnauthenticatedVlan based on Unsigned32"""
    defaultValue = 0


_Hm2AgentDot1xUnauthenticatedVlan_Type.__name__ = "Unsigned32"
_Hm2AgentDot1xUnauthenticatedVlan_Object = MibTableColumn
hm2AgentDot1xUnauthenticatedVlan = _Hm2AgentDot1xUnauthenticatedVlan_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 2, 1, 1, 4),
    _Hm2AgentDot1xUnauthenticatedVlan_Type()
)
hm2AgentDot1xUnauthenticatedVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDot1xUnauthenticatedVlan.setStatus("current")


class _Hm2AgentDot1xMaxUsers_Type(Unsigned32):
    """Custom type hm2AgentDot1xMaxUsers based on Unsigned32"""
    defaultValue = 16


_Hm2AgentDot1xMaxUsers_Type.__name__ = "Unsigned32"
_Hm2AgentDot1xMaxUsers_Object = MibTableColumn
hm2AgentDot1xMaxUsers = _Hm2AgentDot1xMaxUsers_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 2, 1, 1, 5),
    _Hm2AgentDot1xMaxUsers_Type()
)
hm2AgentDot1xMaxUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDot1xMaxUsers.setStatus("current")


class _Hm2AgentDot1xPortVlanAssigned_Type(Unsigned32):
    """Custom type hm2AgentDot1xPortVlanAssigned based on Unsigned32"""
    defaultValue = 0


_Hm2AgentDot1xPortVlanAssigned_Type.__name__ = "Unsigned32"
_Hm2AgentDot1xPortVlanAssigned_Object = MibTableColumn
hm2AgentDot1xPortVlanAssigned = _Hm2AgentDot1xPortVlanAssigned_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 2, 1, 1, 6),
    _Hm2AgentDot1xPortVlanAssigned_Type()
)
hm2AgentDot1xPortVlanAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1xPortVlanAssigned.setStatus("current")


class _Hm2AgentDot1xPortVlanAssignedReason_Type(Integer32):
    """Custom type hm2AgentDot1xPortVlanAssignedReason based on Integer32"""
    defaultValue = 7

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
        *(("default", 1),
          ("radius", 2),
          ("unauthenticatedVlan", 3),
          ("guestVlan", 4),
          ("voiceVlan", 5),
          ("monitorVlan", 6),
          ("notAssigned", 7))
    )


_Hm2AgentDot1xPortVlanAssignedReason_Type.__name__ = "Integer32"
_Hm2AgentDot1xPortVlanAssignedReason_Object = MibTableColumn
hm2AgentDot1xPortVlanAssignedReason = _Hm2AgentDot1xPortVlanAssignedReason_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 2, 1, 1, 7),
    _Hm2AgentDot1xPortVlanAssignedReason_Type()
)
hm2AgentDot1xPortVlanAssignedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1xPortVlanAssignedReason.setStatus("current")
_Hm2AgentDot1xPortSessionTimeout_Type = Unsigned32
_Hm2AgentDot1xPortSessionTimeout_Object = MibTableColumn
hm2AgentDot1xPortSessionTimeout = _Hm2AgentDot1xPortSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 2, 1, 1, 8),
    _Hm2AgentDot1xPortSessionTimeout_Type()
)
hm2AgentDot1xPortSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1xPortSessionTimeout.setStatus("current")


class _Hm2AgentDot1xPortTerminationAction_Type(Dot1xSessionTerminationAction):
    """Custom type hm2AgentDot1xPortTerminationAction based on Dot1xSessionTerminationAction"""
    defaultValue = 1


_Hm2AgentDot1xPortTerminationAction_Type.__name__ = "Dot1xSessionTerminationAction"
_Hm2AgentDot1xPortTerminationAction_Object = MibTableColumn
hm2AgentDot1xPortTerminationAction = _Hm2AgentDot1xPortTerminationAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 2, 1, 1, 9),
    _Hm2AgentDot1xPortTerminationAction_Type()
)
hm2AgentDot1xPortTerminationAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1xPortTerminationAction.setStatus("current")


class _Hm2AgentDot1xPortMABenabled_Type(HmEnabledStatus):
    """Custom type hm2AgentDot1xPortMABenabled based on HmEnabledStatus"""
    defaultValue = 2


_Hm2AgentDot1xPortMABenabled_Type.__name__ = "HmEnabledStatus"
_Hm2AgentDot1xPortMABenabled_Object = MibTableColumn
hm2AgentDot1xPortMABenabled = _Hm2AgentDot1xPortMABenabled_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 2, 1, 1, 10),
    _Hm2AgentDot1xPortMABenabled_Type()
)
hm2AgentDot1xPortMABenabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDot1xPortMABenabled.setStatus("current")


class _Hm2AgentDot1xPortMABenabledOperational_Type(HmEnabledStatus):
    """Custom type hm2AgentDot1xPortMABenabledOperational based on HmEnabledStatus"""
    defaultValue = 2


_Hm2AgentDot1xPortMABenabledOperational_Type.__name__ = "HmEnabledStatus"
_Hm2AgentDot1xPortMABenabledOperational_Object = MibTableColumn
hm2AgentDot1xPortMABenabledOperational = _Hm2AgentDot1xPortMABenabledOperational_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 2, 1, 1, 11),
    _Hm2AgentDot1xPortMABenabledOperational_Type()
)
hm2AgentDot1xPortMABenabledOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1xPortMABenabledOperational.setStatus("current")
_Hm2AgentDot1xClientConfigGroup_ObjectIdentity = ObjectIdentity
hm2AgentDot1xClientConfigGroup = _Hm2AgentDot1xClientConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 3)
)
_Hm2AgentDot1xClientConfigTable_Object = MibTable
hm2AgentDot1xClientConfigTable = _Hm2AgentDot1xClientConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 3, 1)
)
if mibBuilder.loadTexts:
    hm2AgentDot1xClientConfigTable.setStatus("current")
_Hm2AgentDot1xClientConfigEntry_Object = MibTableRow
hm2AgentDot1xClientConfigEntry = _Hm2AgentDot1xClientConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 3, 1, 1)
)
hm2AgentDot1xClientConfigEntry.setIndexNames(
    (0, "HM2-PLATFORM-DOT1X-ADVANCED-MIB", "hm2AgentDot1xClientMacAddress"),
)
if mibBuilder.loadTexts:
    hm2AgentDot1xClientConfigEntry.setStatus("current")
_Hm2AgentDot1xClientMacAddress_Type = MacAddress
_Hm2AgentDot1xClientMacAddress_Object = MibTableColumn
hm2AgentDot1xClientMacAddress = _Hm2AgentDot1xClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 3, 1, 1, 1),
    _Hm2AgentDot1xClientMacAddress_Type()
)
hm2AgentDot1xClientMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1xClientMacAddress.setStatus("current")
_Hm2AgentDot1xLogicalPort_Type = Unsigned32
_Hm2AgentDot1xLogicalPort_Object = MibTableColumn
hm2AgentDot1xLogicalPort = _Hm2AgentDot1xLogicalPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 3, 1, 1, 2),
    _Hm2AgentDot1xLogicalPort_Type()
)
hm2AgentDot1xLogicalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1xLogicalPort.setStatus("current")
_Hm2AgentDot1xInterface_Type = Unsigned32
_Hm2AgentDot1xInterface_Object = MibTableColumn
hm2AgentDot1xInterface = _Hm2AgentDot1xInterface_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 3, 1, 1, 3),
    _Hm2AgentDot1xInterface_Type()
)
hm2AgentDot1xInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1xInterface.setStatus("current")


class _Hm2AgentDot1xClientAuthPAEstate_Type(Integer32):
    """Custom type hm2AgentDot1xClientAuthPAEstate based on Integer32"""
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
        *(("initialize", 1),
          ("disconnected", 2),
          ("connecting", 3),
          ("authenticating", 4),
          ("authenticated", 5),
          ("aborting", 6),
          ("held", 7),
          ("forceAuth", 8),
          ("forceUnauth", 9))
    )


_Hm2AgentDot1xClientAuthPAEstate_Type.__name__ = "Integer32"
_Hm2AgentDot1xClientAuthPAEstate_Object = MibTableColumn
hm2AgentDot1xClientAuthPAEstate = _Hm2AgentDot1xClientAuthPAEstate_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 3, 1, 1, 4),
    _Hm2AgentDot1xClientAuthPAEstate_Type()
)
hm2AgentDot1xClientAuthPAEstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1xClientAuthPAEstate.setStatus("current")


class _Hm2AgentDot1xClientBackendState_Type(Integer32):
    """Custom type hm2AgentDot1xClientBackendState based on Integer32"""
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
        *(("request", 1),
          ("response", 2),
          ("success", 3),
          ("fail", 4),
          ("timeout", 5),
          ("idle", 6),
          ("initialize", 7))
    )


_Hm2AgentDot1xClientBackendState_Type.__name__ = "Integer32"
_Hm2AgentDot1xClientBackendState_Object = MibTableColumn
hm2AgentDot1xClientBackendState = _Hm2AgentDot1xClientBackendState_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 3, 1, 1, 5),
    _Hm2AgentDot1xClientBackendState_Type()
)
hm2AgentDot1xClientBackendState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1xClientBackendState.setStatus("current")
_Hm2AgentDot1xClientUserName_Type = DisplayString
_Hm2AgentDot1xClientUserName_Object = MibTableColumn
hm2AgentDot1xClientUserName = _Hm2AgentDot1xClientUserName_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 3, 1, 1, 6),
    _Hm2AgentDot1xClientUserName_Type()
)
hm2AgentDot1xClientUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1xClientUserName.setStatus("current")
_Hm2AgentDot1xClientSessionTime_Type = Unsigned32
_Hm2AgentDot1xClientSessionTime_Object = MibTableColumn
hm2AgentDot1xClientSessionTime = _Hm2AgentDot1xClientSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 3, 1, 1, 7),
    _Hm2AgentDot1xClientSessionTime_Type()
)
hm2AgentDot1xClientSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1xClientSessionTime.setStatus("current")
_Hm2AgentDot1xClientFilterID_Type = DisplayString
_Hm2AgentDot1xClientFilterID_Object = MibTableColumn
hm2AgentDot1xClientFilterID = _Hm2AgentDot1xClientFilterID_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 3, 1, 1, 8),
    _Hm2AgentDot1xClientFilterID_Type()
)
hm2AgentDot1xClientFilterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1xClientFilterID.setStatus("current")
_Hm2AgentDot1xClientVlanAssigned_Type = Unsigned32
_Hm2AgentDot1xClientVlanAssigned_Object = MibTableColumn
hm2AgentDot1xClientVlanAssigned = _Hm2AgentDot1xClientVlanAssigned_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 3, 1, 1, 9),
    _Hm2AgentDot1xClientVlanAssigned_Type()
)
hm2AgentDot1xClientVlanAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1xClientVlanAssigned.setStatus("current")


class _Hm2AgentDot1xClientVlanAssignedReason_Type(Integer32):
    """Custom type hm2AgentDot1xClientVlanAssignedReason based on Integer32"""
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
        *(("default", 1),
          ("radius", 2),
          ("unauthenticatedVlan", 3),
          ("guestVlan", 4),
          ("voiceVlan", 5),
          ("monitorVlan", 6),
          ("invalid", 7))
    )


_Hm2AgentDot1xClientVlanAssignedReason_Type.__name__ = "Integer32"
_Hm2AgentDot1xClientVlanAssignedReason_Object = MibTableColumn
hm2AgentDot1xClientVlanAssignedReason = _Hm2AgentDot1xClientVlanAssignedReason_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 3, 1, 1, 10),
    _Hm2AgentDot1xClientVlanAssignedReason_Type()
)
hm2AgentDot1xClientVlanAssignedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1xClientVlanAssignedReason.setStatus("current")
_Hm2AgentDot1xClientSessionTimeout_Type = Unsigned32
_Hm2AgentDot1xClientSessionTimeout_Object = MibTableColumn
hm2AgentDot1xClientSessionTimeout = _Hm2AgentDot1xClientSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 3, 1, 1, 11),
    _Hm2AgentDot1xClientSessionTimeout_Type()
)
hm2AgentDot1xClientSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1xClientSessionTimeout.setStatus("current")
_Hm2AgentDot1xClientTerminationAction_Type = Dot1xSessionTerminationAction
_Hm2AgentDot1xClientTerminationAction_Object = MibTableColumn
hm2AgentDot1xClientTerminationAction = _Hm2AgentDot1xClientTerminationAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 3, 1, 1, 12),
    _Hm2AgentDot1xClientTerminationAction_Type()
)
hm2AgentDot1xClientTerminationAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1xClientTerminationAction.setStatus("current")
_Hm2AgentDot1xMonitorModeConfigGroup_ObjectIdentity = ObjectIdentity
hm2AgentDot1xMonitorModeConfigGroup = _Hm2AgentDot1xMonitorModeConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 4)
)


class _Hm2AgentDot1xMonitorModeEnabled_Type(HmEnabledStatus):
    """Custom type hm2AgentDot1xMonitorModeEnabled based on HmEnabledStatus"""
    defaultValue = 2


_Hm2AgentDot1xMonitorModeEnabled_Type.__name__ = "HmEnabledStatus"
_Hm2AgentDot1xMonitorModeEnabled_Object = MibScalar
hm2AgentDot1xMonitorModeEnabled = _Hm2AgentDot1xMonitorModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 4, 1),
    _Hm2AgentDot1xMonitorModeEnabled_Type()
)
hm2AgentDot1xMonitorModeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDot1xMonitorModeEnabled.setStatus("current")
_Hm2AgentDot1xMonitorModeClients_Type = Unsigned32
_Hm2AgentDot1xMonitorModeClients_Object = MibScalar
hm2AgentDot1xMonitorModeClients = _Hm2AgentDot1xMonitorModeClients_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 4, 2),
    _Hm2AgentDot1xMonitorModeClients_Type()
)
hm2AgentDot1xMonitorModeClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1xMonitorModeClients.setStatus("current")
_Hm2AgentDot1xNonMonitorModeClients_Type = Unsigned32
_Hm2AgentDot1xNonMonitorModeClients_Object = MibScalar
hm2AgentDot1xNonMonitorModeClients = _Hm2AgentDot1xNonMonitorModeClients_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 4, 3),
    _Hm2AgentDot1xNonMonitorModeClients_Type()
)
hm2AgentDot1xNonMonitorModeClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1xNonMonitorModeClients.setStatus("current")
_Hm2AgentDot1xAuthHistoryResultsGroup_ObjectIdentity = ObjectIdentity
hm2AgentDot1xAuthHistoryResultsGroup = _Hm2AgentDot1xAuthHistoryResultsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 5)
)
_Hm2AgentDot1xPortAuthHistoryResultTable_Object = MibTable
hm2AgentDot1xPortAuthHistoryResultTable = _Hm2AgentDot1xPortAuthHistoryResultTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 5, 1)
)
if mibBuilder.loadTexts:
    hm2AgentDot1xPortAuthHistoryResultTable.setStatus("current")
_Hm2AgentDot1xPortAuthHistoryResultEntry_Object = MibTableRow
hm2AgentDot1xPortAuthHistoryResultEntry = _Hm2AgentDot1xPortAuthHistoryResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 5, 1, 1)
)
hm2AgentDot1xPortAuthHistoryResultEntry.setIndexNames(
    (0, "HM2-PLATFORM-DOT1X-ADVANCED-MIB", "hm2AgentDot1xAuthHistoryResultIfaceIndex"),
    (0, "HM2-PLATFORM-DOT1X-ADVANCED-MIB", "hm2AgentDot1xAuthHistoryResultIndex"),
)
if mibBuilder.loadTexts:
    hm2AgentDot1xPortAuthHistoryResultEntry.setStatus("current")
_Hm2AgentDot1xAuthHistoryResultIfaceIndex_Type = Unsigned32
_Hm2AgentDot1xAuthHistoryResultIfaceIndex_Object = MibTableColumn
hm2AgentDot1xAuthHistoryResultIfaceIndex = _Hm2AgentDot1xAuthHistoryResultIfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 5, 1, 1, 1),
    _Hm2AgentDot1xAuthHistoryResultIfaceIndex_Type()
)
hm2AgentDot1xAuthHistoryResultIfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1xAuthHistoryResultIfaceIndex.setStatus("current")
_Hm2AgentDot1xAuthHistoryResultIndex_Type = Unsigned32
_Hm2AgentDot1xAuthHistoryResultIndex_Object = MibTableColumn
hm2AgentDot1xAuthHistoryResultIndex = _Hm2AgentDot1xAuthHistoryResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 5, 1, 1, 2),
    _Hm2AgentDot1xAuthHistoryResultIndex_Type()
)
hm2AgentDot1xAuthHistoryResultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1xAuthHistoryResultIndex.setStatus("current")
_Hm2AgentDot1xAuthHistoryResultTimeStamp_Type = HmTimeSeconds1970
_Hm2AgentDot1xAuthHistoryResultTimeStamp_Object = MibTableColumn
hm2AgentDot1xAuthHistoryResultTimeStamp = _Hm2AgentDot1xAuthHistoryResultTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 5, 1, 1, 3),
    _Hm2AgentDot1xAuthHistoryResultTimeStamp_Type()
)
hm2AgentDot1xAuthHistoryResultTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1xAuthHistoryResultTimeStamp.setStatus("current")
_Hm2AgentDot1xAuthHistoryResultAge_Type = TimeTicks
_Hm2AgentDot1xAuthHistoryResultAge_Object = MibTableColumn
hm2AgentDot1xAuthHistoryResultAge = _Hm2AgentDot1xAuthHistoryResultAge_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 5, 1, 1, 4),
    _Hm2AgentDot1xAuthHistoryResultAge_Type()
)
hm2AgentDot1xAuthHistoryResultAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1xAuthHistoryResultAge.setStatus("current")
_Hm2AgentDot1xAuthHistoryResultMacAddress_Type = MacAddress
_Hm2AgentDot1xAuthHistoryResultMacAddress_Object = MibTableColumn
hm2AgentDot1xAuthHistoryResultMacAddress = _Hm2AgentDot1xAuthHistoryResultMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 5, 1, 1, 5),
    _Hm2AgentDot1xAuthHistoryResultMacAddress_Type()
)
hm2AgentDot1xAuthHistoryResultMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1xAuthHistoryResultMacAddress.setStatus("current")
_Hm2AgentDot1xAuthHistoryResultVlanId_Type = Unsigned32
_Hm2AgentDot1xAuthHistoryResultVlanId_Object = MibTableColumn
hm2AgentDot1xAuthHistoryResultVlanId = _Hm2AgentDot1xAuthHistoryResultVlanId_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 5, 1, 1, 6),
    _Hm2AgentDot1xAuthHistoryResultVlanId_Type()
)
hm2AgentDot1xAuthHistoryResultVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1xAuthHistoryResultVlanId.setStatus("current")


class _Hm2AgentDot1xAuthHistoryResultAuthStatus_Type(Integer32):
    """Custom type hm2AgentDot1xAuthHistoryResultAuthStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("failure", 2))
    )


_Hm2AgentDot1xAuthHistoryResultAuthStatus_Type.__name__ = "Integer32"
_Hm2AgentDot1xAuthHistoryResultAuthStatus_Object = MibTableColumn
hm2AgentDot1xAuthHistoryResultAuthStatus = _Hm2AgentDot1xAuthHistoryResultAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 5, 1, 1, 7),
    _Hm2AgentDot1xAuthHistoryResultAuthStatus_Type()
)
hm2AgentDot1xAuthHistoryResultAuthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1xAuthHistoryResultAuthStatus.setStatus("current")


class _Hm2AgentDot1xAuthHistoryResultAccessStatus_Type(Integer32):
    """Custom type hm2AgentDot1xAuthHistoryResultAccessStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("granted", 1),
          ("denied", 2))
    )


_Hm2AgentDot1xAuthHistoryResultAccessStatus_Type.__name__ = "Integer32"
_Hm2AgentDot1xAuthHistoryResultAccessStatus_Object = MibTableColumn
hm2AgentDot1xAuthHistoryResultAccessStatus = _Hm2AgentDot1xAuthHistoryResultAccessStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 5, 1, 1, 8),
    _Hm2AgentDot1xAuthHistoryResultAccessStatus_Type()
)
hm2AgentDot1xAuthHistoryResultAccessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1xAuthHistoryResultAccessStatus.setStatus("current")
_Hm2AgentDot1xAuthHistoryResultFilterID_Type = DisplayString
_Hm2AgentDot1xAuthHistoryResultFilterID_Object = MibTableColumn
hm2AgentDot1xAuthHistoryResultFilterID = _Hm2AgentDot1xAuthHistoryResultFilterID_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 5, 1, 1, 9),
    _Hm2AgentDot1xAuthHistoryResultFilterID_Type()
)
hm2AgentDot1xAuthHistoryResultFilterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1xAuthHistoryResultFilterID.setStatus("current")
_Hm2AgentDot1xAuthHistoryResultVlanAssigned_Type = Unsigned32
_Hm2AgentDot1xAuthHistoryResultVlanAssigned_Object = MibTableColumn
hm2AgentDot1xAuthHistoryResultVlanAssigned = _Hm2AgentDot1xAuthHistoryResultVlanAssigned_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 5, 1, 1, 10),
    _Hm2AgentDot1xAuthHistoryResultVlanAssigned_Type()
)
hm2AgentDot1xAuthHistoryResultVlanAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1xAuthHistoryResultVlanAssigned.setStatus("current")


class _Hm2AgentDot1xAuthHistoryResultVlanAssignedType_Type(Integer32):
    """Custom type hm2AgentDot1xAuthHistoryResultVlanAssignedType based on Integer32"""
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
        *(("default", 1),
          ("radius", 2),
          ("unauthenticatedVlan", 3),
          ("guestVlan", 4),
          ("voiceVlan", 5),
          ("monitorVlan", 6),
          ("notAssigned", 7))
    )


_Hm2AgentDot1xAuthHistoryResultVlanAssignedType_Type.__name__ = "Integer32"
_Hm2AgentDot1xAuthHistoryResultVlanAssignedType_Object = MibTableColumn
hm2AgentDot1xAuthHistoryResultVlanAssignedType = _Hm2AgentDot1xAuthHistoryResultVlanAssignedType_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 5, 1, 1, 11),
    _Hm2AgentDot1xAuthHistoryResultVlanAssignedType_Type()
)
hm2AgentDot1xAuthHistoryResultVlanAssignedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1xAuthHistoryResultVlanAssignedType.setStatus("current")


class _Hm2AgentDot1xAuthHistoryResultReasonCode_Type(Integer32):
    """Custom type hm2AgentDot1xAuthHistoryResultReasonCode based on Integer32"""
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
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30)
        )
    )
    namedValues = NamedValues(
        *(("supplicant-timeout", 1),
          ("eapol-timeout", 2),
          ("radius-request-timeout", 3),
          ("radius-auth-failure", 4),
          ("radius-auth-comm-failure", 5),
          ("radius-challenge-process-invalid-nas-port", 6),
          ("radius-challenge-process-wrong-eap-msg", 7),
          ("radius-request-send-msg-error", 8),
          ("radius-accept-process-invalid-nas-port", 9),
          ("radius-accept-process-wrong-eap-msg", 10),
          ("radius-accept-filter-assignment-failure", 11),
          ("radius-accept-diffserv-not-present", 12),
          ("radius-accept-vlan-assignment-failure", 13),
          ("vlan-assignment-feature-not-enabled", 14),
          ("radius-success", 15),
          ("local-auth-user-not-found", 16),
          ("local-auth-user-no-access", 17),
          ("local-auth-md5-validation-failure", 18),
          ("local-auth-invalid-eap-type", 19),
          ("local-failure", 20),
          ("local-success", 21),
          ("radius-invalid-radius-status", 22),
          ("guest-vlan-timer-expiry", 23),
          ("undefined-auth-method", 24),
          ("reject-auth-method", 25),
          ("invalid-auth-method", 26),
          ("auth-method-not-configured", 27),
          ("unauth-vlan-not-created", 28),
          ("guest-vlan-not-created", 29),
          ("radius-accept-invalid-vlan-failure", 30))
    )


_Hm2AgentDot1xAuthHistoryResultReasonCode_Type.__name__ = "Integer32"
_Hm2AgentDot1xAuthHistoryResultReasonCode_Object = MibTableColumn
hm2AgentDot1xAuthHistoryResultReasonCode = _Hm2AgentDot1xAuthHistoryResultReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 5, 1, 1, 12),
    _Hm2AgentDot1xAuthHistoryResultReasonCode_Type()
)
hm2AgentDot1xAuthHistoryResultReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1xAuthHistoryResultReasonCode.setStatus("current")


class _Hm2AgentDot1xAuthHistoryResultsClear_Type(HmEnabledStatus):
    """Custom type hm2AgentDot1xAuthHistoryResultsClear based on HmEnabledStatus"""
    defaultValue = 2


_Hm2AgentDot1xAuthHistoryResultsClear_Type.__name__ = "HmEnabledStatus"
_Hm2AgentDot1xAuthHistoryResultsClear_Object = MibScalar
hm2AgentDot1xAuthHistoryResultsClear = _Hm2AgentDot1xAuthHistoryResultsClear_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 5, 2),
    _Hm2AgentDot1xAuthHistoryResultsClear_Type()
)
hm2AgentDot1xAuthHistoryResultsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDot1xAuthHistoryResultsClear.setStatus("current")
_Hm2AgentDot1xPortAuthHistoryResultClearTable_Object = MibTable
hm2AgentDot1xPortAuthHistoryResultClearTable = _Hm2AgentDot1xPortAuthHistoryResultClearTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 5, 3)
)
if mibBuilder.loadTexts:
    hm2AgentDot1xPortAuthHistoryResultClearTable.setStatus("current")
_Hm2AgentDot1xPortAuthHistoryResultClearEntry_Object = MibTableRow
hm2AgentDot1xPortAuthHistoryResultClearEntry = _Hm2AgentDot1xPortAuthHistoryResultClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 5, 3, 1)
)
hm2AgentDot1xPortAuthHistoryResultClearEntry.setIndexNames(
    (0, "HM2-PLATFORM-DOT1X-ADVANCED-MIB", "hm2AgentDot1xAuthHistoryResultIfIndex"),
)
if mibBuilder.loadTexts:
    hm2AgentDot1xPortAuthHistoryResultClearEntry.setStatus("current")
_Hm2AgentDot1xAuthHistoryResultIfIndex_Type = Unsigned32
_Hm2AgentDot1xAuthHistoryResultIfIndex_Object = MibTableColumn
hm2AgentDot1xAuthHistoryResultIfIndex = _Hm2AgentDot1xAuthHistoryResultIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 5, 3, 1, 1),
    _Hm2AgentDot1xAuthHistoryResultIfIndex_Type()
)
hm2AgentDot1xAuthHistoryResultIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1xAuthHistoryResultIfIndex.setStatus("current")


class _Hm2AgentDot1xPortAuthHistoryResultsClear_Type(HmEnabledStatus):
    """Custom type hm2AgentDot1xPortAuthHistoryResultsClear based on HmEnabledStatus"""
    defaultValue = 2


_Hm2AgentDot1xPortAuthHistoryResultsClear_Type.__name__ = "HmEnabledStatus"
_Hm2AgentDot1xPortAuthHistoryResultsClear_Object = MibTableColumn
hm2AgentDot1xPortAuthHistoryResultsClear = _Hm2AgentDot1xPortAuthHistoryResultsClear_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 36, 5, 3, 1, 2),
    _Hm2AgentDot1xPortAuthHistoryResultsClear_Type()
)
hm2AgentDot1xPortAuthHistoryResultsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDot1xPortAuthHistoryResultsClear.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-PLATFORM-DOT1X-ADVANCED-MIB",
    **{"Dot1xPortControlMode": Dot1xPortControlMode,
       "Dot1xSessionTerminationAction": Dot1xSessionTerminationAction,
       "hm2PlatformDot1xAdvanced": hm2PlatformDot1xAdvanced,
       "hm2AgentDot1xEnhancementConfigGroup": hm2AgentDot1xEnhancementConfigGroup,
       "hm2AgentDot1xRadiusVlanAssignment": hm2AgentDot1xRadiusVlanAssignment,
       "hm2AgentDot1xDynamicVlanCreationMode": hm2AgentDot1xDynamicVlanCreationMode,
       "hm2AgentDot1xStatisticsClear": hm2AgentDot1xStatisticsClear,
       "hm2AgentDot1xPortStatsClearTable": hm2AgentDot1xPortStatsClearTable,
       "hm2AgentDot1xPortStatsClearEntry": hm2AgentDot1xPortStatsClearEntry,
       "hm2AgentDot1xStatsIfIndex": hm2AgentDot1xStatsIfIndex,
       "hm2AgentDot1xPortStatsClear": hm2AgentDot1xPortStatsClear,
       "hm2AgentDot1xMABFormatGroupSize": hm2AgentDot1xMABFormatGroupSize,
       "hm2AgentDot1xMABFormatGroupSeparator": hm2AgentDot1xMABFormatGroupSeparator,
       "hm2AgentDot1xMABFormatLetterCase": hm2AgentDot1xMABFormatLetterCase,
       "hm2AgentDot1xMABPassword": hm2AgentDot1xMABPassword,
       "hm2AgentDot1xPortConfigGroup": hm2AgentDot1xPortConfigGroup,
       "hm2AgentDot1xPortConfigTable": hm2AgentDot1xPortConfigTable,
       "hm2AgentDot1xPortConfigEntry": hm2AgentDot1xPortConfigEntry,
       "hm2AgentDot1xPortControlMode": hm2AgentDot1xPortControlMode,
       "hm2AgentDot1xGuestVlanId": hm2AgentDot1xGuestVlanId,
       "hm2AgentDot1xGuestVlanPeriod": hm2AgentDot1xGuestVlanPeriod,
       "hm2AgentDot1xUnauthenticatedVlan": hm2AgentDot1xUnauthenticatedVlan,
       "hm2AgentDot1xMaxUsers": hm2AgentDot1xMaxUsers,
       "hm2AgentDot1xPortVlanAssigned": hm2AgentDot1xPortVlanAssigned,
       "hm2AgentDot1xPortVlanAssignedReason": hm2AgentDot1xPortVlanAssignedReason,
       "hm2AgentDot1xPortSessionTimeout": hm2AgentDot1xPortSessionTimeout,
       "hm2AgentDot1xPortTerminationAction": hm2AgentDot1xPortTerminationAction,
       "hm2AgentDot1xPortMABenabled": hm2AgentDot1xPortMABenabled,
       "hm2AgentDot1xPortMABenabledOperational": hm2AgentDot1xPortMABenabledOperational,
       "hm2AgentDot1xClientConfigGroup": hm2AgentDot1xClientConfigGroup,
       "hm2AgentDot1xClientConfigTable": hm2AgentDot1xClientConfigTable,
       "hm2AgentDot1xClientConfigEntry": hm2AgentDot1xClientConfigEntry,
       "hm2AgentDot1xClientMacAddress": hm2AgentDot1xClientMacAddress,
       "hm2AgentDot1xLogicalPort": hm2AgentDot1xLogicalPort,
       "hm2AgentDot1xInterface": hm2AgentDot1xInterface,
       "hm2AgentDot1xClientAuthPAEstate": hm2AgentDot1xClientAuthPAEstate,
       "hm2AgentDot1xClientBackendState": hm2AgentDot1xClientBackendState,
       "hm2AgentDot1xClientUserName": hm2AgentDot1xClientUserName,
       "hm2AgentDot1xClientSessionTime": hm2AgentDot1xClientSessionTime,
       "hm2AgentDot1xClientFilterID": hm2AgentDot1xClientFilterID,
       "hm2AgentDot1xClientVlanAssigned": hm2AgentDot1xClientVlanAssigned,
       "hm2AgentDot1xClientVlanAssignedReason": hm2AgentDot1xClientVlanAssignedReason,
       "hm2AgentDot1xClientSessionTimeout": hm2AgentDot1xClientSessionTimeout,
       "hm2AgentDot1xClientTerminationAction": hm2AgentDot1xClientTerminationAction,
       "hm2AgentDot1xMonitorModeConfigGroup": hm2AgentDot1xMonitorModeConfigGroup,
       "hm2AgentDot1xMonitorModeEnabled": hm2AgentDot1xMonitorModeEnabled,
       "hm2AgentDot1xMonitorModeClients": hm2AgentDot1xMonitorModeClients,
       "hm2AgentDot1xNonMonitorModeClients": hm2AgentDot1xNonMonitorModeClients,
       "hm2AgentDot1xAuthHistoryResultsGroup": hm2AgentDot1xAuthHistoryResultsGroup,
       "hm2AgentDot1xPortAuthHistoryResultTable": hm2AgentDot1xPortAuthHistoryResultTable,
       "hm2AgentDot1xPortAuthHistoryResultEntry": hm2AgentDot1xPortAuthHistoryResultEntry,
       "hm2AgentDot1xAuthHistoryResultIfaceIndex": hm2AgentDot1xAuthHistoryResultIfaceIndex,
       "hm2AgentDot1xAuthHistoryResultIndex": hm2AgentDot1xAuthHistoryResultIndex,
       "hm2AgentDot1xAuthHistoryResultTimeStamp": hm2AgentDot1xAuthHistoryResultTimeStamp,
       "hm2AgentDot1xAuthHistoryResultAge": hm2AgentDot1xAuthHistoryResultAge,
       "hm2AgentDot1xAuthHistoryResultMacAddress": hm2AgentDot1xAuthHistoryResultMacAddress,
       "hm2AgentDot1xAuthHistoryResultVlanId": hm2AgentDot1xAuthHistoryResultVlanId,
       "hm2AgentDot1xAuthHistoryResultAuthStatus": hm2AgentDot1xAuthHistoryResultAuthStatus,
       "hm2AgentDot1xAuthHistoryResultAccessStatus": hm2AgentDot1xAuthHistoryResultAccessStatus,
       "hm2AgentDot1xAuthHistoryResultFilterID": hm2AgentDot1xAuthHistoryResultFilterID,
       "hm2AgentDot1xAuthHistoryResultVlanAssigned": hm2AgentDot1xAuthHistoryResultVlanAssigned,
       "hm2AgentDot1xAuthHistoryResultVlanAssignedType": hm2AgentDot1xAuthHistoryResultVlanAssignedType,
       "hm2AgentDot1xAuthHistoryResultReasonCode": hm2AgentDot1xAuthHistoryResultReasonCode,
       "hm2AgentDot1xAuthHistoryResultsClear": hm2AgentDot1xAuthHistoryResultsClear,
       "hm2AgentDot1xPortAuthHistoryResultClearTable": hm2AgentDot1xPortAuthHistoryResultClearTable,
       "hm2AgentDot1xPortAuthHistoryResultClearEntry": hm2AgentDot1xPortAuthHistoryResultClearEntry,
       "hm2AgentDot1xAuthHistoryResultIfIndex": hm2AgentDot1xAuthHistoryResultIfIndex,
       "hm2AgentDot1xPortAuthHistoryResultsClear": hm2AgentDot1xPortAuthHistoryResultsClear}
)
