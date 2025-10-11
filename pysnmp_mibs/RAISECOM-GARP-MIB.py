# SNMP MIB module (RAISECOM-GARP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-GARP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:36:02 2025
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(raisecomAgent,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "raisecomAgent")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")

(EnableVar,) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar")


# MODULE-IDENTITY

raisecomGarp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 42)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RaisecomGarpNotifications_ObjectIdentity = ObjectIdentity
raisecomGarpNotifications = _RaisecomGarpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 42, 0)
)
_RaisecomGarpCommonObjects_ObjectIdentity = ObjectIdentity
raisecomGarpCommonObjects = _RaisecomGarpCommonObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 42, 1)
)
_RaisecomGarpPortTable_Object = MibTable
raisecomGarpPortTable = _RaisecomGarpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 42, 1, 1)
)
if mibBuilder.loadTexts:
    raisecomGarpPortTable.setStatus("current")
_RaisecomGarpPortEntry_Object = MibTableRow
raisecomGarpPortEntry = _RaisecomGarpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 42, 1, 1, 1)
)
raisecomGarpPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    raisecomGarpPortEntry.setStatus("current")


class _RaisecomGarpPortJoinTime_Type(TimeInterval):
    """Custom type raisecomGarpPortJoinTime based on TimeInterval"""
    defaultValue = 20


_RaisecomGarpPortJoinTime_Type.__name__ = "TimeInterval"
_RaisecomGarpPortJoinTime_Object = MibTableColumn
raisecomGarpPortJoinTime = _RaisecomGarpPortJoinTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 42, 1, 1, 1, 1),
    _RaisecomGarpPortJoinTime_Type()
)
raisecomGarpPortJoinTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomGarpPortJoinTime.setStatus("current")


class _RaisecomGarpPortLeaveTime_Type(TimeInterval):
    """Custom type raisecomGarpPortLeaveTime based on TimeInterval"""
    defaultValue = 60


_RaisecomGarpPortLeaveTime_Type.__name__ = "TimeInterval"
_RaisecomGarpPortLeaveTime_Object = MibTableColumn
raisecomGarpPortLeaveTime = _RaisecomGarpPortLeaveTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 42, 1, 1, 1, 2),
    _RaisecomGarpPortLeaveTime_Type()
)
raisecomGarpPortLeaveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomGarpPortLeaveTime.setStatus("current")


class _RaisecomGarpPortLeaveAllTime_Type(TimeInterval):
    """Custom type raisecomGarpPortLeaveAllTime based on TimeInterval"""
    defaultValue = 1000


_RaisecomGarpPortLeaveAllTime_Type.__name__ = "TimeInterval"
_RaisecomGarpPortLeaveAllTime_Object = MibTableColumn
raisecomGarpPortLeaveAllTime = _RaisecomGarpPortLeaveAllTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 42, 1, 1, 1, 3),
    _RaisecomGarpPortLeaveAllTime_Type()
)
raisecomGarpPortLeaveAllTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomGarpPortLeaveAllTime.setStatus("current")


class _RaisecomGarpPortStatisticClear_Type(EnableVar):
    """Custom type raisecomGarpPortStatisticClear based on EnableVar"""
    defaultValue = 2


_RaisecomGarpPortStatisticClear_Type.__name__ = "EnableVar"
_RaisecomGarpPortStatisticClear_Object = MibTableColumn
raisecomGarpPortStatisticClear = _RaisecomGarpPortStatisticClear_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 42, 1, 1, 1, 4),
    _RaisecomGarpPortStatisticClear_Type()
)
raisecomGarpPortStatisticClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomGarpPortStatisticClear.setStatus("current")


class _RaisecomGvrpPortStatisticClear_Type(EnableVar):
    """Custom type raisecomGvrpPortStatisticClear based on EnableVar"""
    defaultValue = 2


_RaisecomGvrpPortStatisticClear_Type.__name__ = "EnableVar"
_RaisecomGvrpPortStatisticClear_Object = MibTableColumn
raisecomGvrpPortStatisticClear = _RaisecomGvrpPortStatisticClear_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 42, 1, 1, 1, 5),
    _RaisecomGvrpPortStatisticClear_Type()
)
raisecomGvrpPortStatisticClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomGvrpPortStatisticClear.setStatus("current")


class _RaisecomGmrpPortStatisticClear_Type(EnableVar):
    """Custom type raisecomGmrpPortStatisticClear based on EnableVar"""
    defaultValue = 2


_RaisecomGmrpPortStatisticClear_Type.__name__ = "EnableVar"
_RaisecomGmrpPortStatisticClear_Object = MibTableColumn
raisecomGmrpPortStatisticClear = _RaisecomGmrpPortStatisticClear_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 42, 1, 1, 1, 6),
    _RaisecomGmrpPortStatisticClear_Type()
)
raisecomGmrpPortStatisticClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomGmrpPortStatisticClear.setStatus("current")
_RaisecomGarpApplicationObjects_ObjectIdentity = ObjectIdentity
raisecomGarpApplicationObjects = _RaisecomGarpApplicationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 42, 2)
)
_RaisecomGvrpObjects_ObjectIdentity = ObjectIdentity
raisecomGvrpObjects = _RaisecomGvrpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 42, 2, 1)
)


class _RaisecomGvrpStatus_Type(EnabledStatus):
    """Custom type raisecomGvrpStatus based on EnabledStatus"""
    defaultValue = 2


_RaisecomGvrpStatus_Type.__name__ = "EnabledStatus"
_RaisecomGvrpStatus_Object = MibScalar
raisecomGvrpStatus = _RaisecomGvrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 42, 2, 1, 1),
    _RaisecomGvrpStatus_Type()
)
raisecomGvrpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomGvrpStatus.setStatus("current")
_RaisecomGvrpMaxVlan_Type = Integer32
_RaisecomGvrpMaxVlan_Object = MibScalar
raisecomGvrpMaxVlan = _RaisecomGvrpMaxVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 42, 2, 1, 2),
    _RaisecomGvrpMaxVlan_Type()
)
raisecomGvrpMaxVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomGvrpMaxVlan.setStatus("current")
_RaisecomGvrpPortTable_Object = MibTable
raisecomGvrpPortTable = _RaisecomGvrpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 42, 2, 1, 3)
)
if mibBuilder.loadTexts:
    raisecomGvrpPortTable.setStatus("current")
_RaisecomGvrpPortEntry_Object = MibTableRow
raisecomGvrpPortEntry = _RaisecomGvrpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 42, 2, 1, 3, 1)
)
raisecomGvrpPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    raisecomGvrpPortEntry.setStatus("current")


class _RaisecomGvrpPortStatus_Type(EnabledStatus):
    """Custom type raisecomGvrpPortStatus based on EnabledStatus"""
    defaultValue = 2


_RaisecomGvrpPortStatus_Type.__name__ = "EnabledStatus"
_RaisecomGvrpPortStatus_Object = MibTableColumn
raisecomGvrpPortStatus = _RaisecomGvrpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 42, 2, 1, 3, 1, 1),
    _RaisecomGvrpPortStatus_Type()
)
raisecomGvrpPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomGvrpPortStatus.setStatus("current")
_RaisecomGvrpPortLastPduOrigin_Type = MacAddress
_RaisecomGvrpPortLastPduOrigin_Object = MibTableColumn
raisecomGvrpPortLastPduOrigin = _RaisecomGvrpPortLastPduOrigin_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 42, 2, 1, 3, 1, 2),
    _RaisecomGvrpPortLastPduOrigin_Type()
)
raisecomGvrpPortLastPduOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomGvrpPortLastPduOrigin.setStatus("current")
_RaisecomGvrpPortFailedRegistrations_Type = Counter32
_RaisecomGvrpPortFailedRegistrations_Object = MibTableColumn
raisecomGvrpPortFailedRegistrations = _RaisecomGvrpPortFailedRegistrations_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 42, 2, 1, 3, 1, 3),
    _RaisecomGvrpPortFailedRegistrations_Type()
)
raisecomGvrpPortFailedRegistrations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomGvrpPortFailedRegistrations.setStatus("current")


class _RaisecomGvrpPortRestrictedVlanRegistration_Type(TruthValue):
    """Custom type raisecomGvrpPortRestrictedVlanRegistration based on TruthValue"""
    defaultValue = 2


_RaisecomGvrpPortRestrictedVlanRegistration_Type.__name__ = "TruthValue"
_RaisecomGvrpPortRestrictedVlanRegistration_Object = MibTableColumn
raisecomGvrpPortRestrictedVlanRegistration = _RaisecomGvrpPortRestrictedVlanRegistration_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 42, 2, 1, 3, 1, 4),
    _RaisecomGvrpPortRestrictedVlanRegistration_Type()
)
raisecomGvrpPortRestrictedVlanRegistration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomGvrpPortRestrictedVlanRegistration.setStatus("current")


class _RaisecomGvrpPortRegistrationMode_Type(Integer32):
    """Custom type raisecomGvrpPortRegistrationMode based on Integer32"""
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
        *(("normal", 1),
          ("fixed", 2),
          ("forbidden", 3))
    )


_RaisecomGvrpPortRegistrationMode_Type.__name__ = "Integer32"
_RaisecomGvrpPortRegistrationMode_Object = MibTableColumn
raisecomGvrpPortRegistrationMode = _RaisecomGvrpPortRegistrationMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 42, 2, 1, 3, 1, 5),
    _RaisecomGvrpPortRegistrationMode_Type()
)
raisecomGvrpPortRegistrationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomGvrpPortRegistrationMode.setStatus("current")


class _RaisecomGvrpPortRunStatus_Type(EnableVar):
    """Custom type raisecomGvrpPortRunStatus based on EnableVar"""
    defaultValue = 2


_RaisecomGvrpPortRunStatus_Type.__name__ = "EnableVar"
_RaisecomGvrpPortRunStatus_Object = MibTableColumn
raisecomGvrpPortRunStatus = _RaisecomGvrpPortRunStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 42, 2, 1, 3, 1, 6),
    _RaisecomGvrpPortRunStatus_Type()
)
raisecomGvrpPortRunStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomGvrpPortRunStatus.setStatus("current")
_RaisecomGvrpPortStatisticTable_Object = MibTable
raisecomGvrpPortStatisticTable = _RaisecomGvrpPortStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 42, 2, 1, 4)
)
if mibBuilder.loadTexts:
    raisecomGvrpPortStatisticTable.setStatus("current")
_RaisecomGvrpPortStatisticEntry_Object = MibTableRow
raisecomGvrpPortStatisticEntry = _RaisecomGvrpPortStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 42, 2, 1, 4, 1)
)
raisecomGvrpPortStatisticEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    raisecomGvrpPortStatisticEntry.setStatus("current")
_RaisecomGvrpPortFrameRx_Type = Integer32
_RaisecomGvrpPortFrameRx_Object = MibTableColumn
raisecomGvrpPortFrameRx = _RaisecomGvrpPortFrameRx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 42, 2, 1, 4, 1, 1),
    _RaisecomGvrpPortFrameRx_Type()
)
raisecomGvrpPortFrameRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomGvrpPortFrameRx.setStatus("current")
_RaisecomGvrpPortFrameTx_Type = Integer32
_RaisecomGvrpPortFrameTx_Object = MibTableColumn
raisecomGvrpPortFrameTx = _RaisecomGvrpPortFrameTx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 42, 2, 1, 4, 1, 2),
    _RaisecomGvrpPortFrameTx_Type()
)
raisecomGvrpPortFrameTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomGvrpPortFrameTx.setStatus("current")
_RaisecomGvrpPortFrameDiscard_Type = Integer32
_RaisecomGvrpPortFrameDiscard_Object = MibTableColumn
raisecomGvrpPortFrameDiscard = _RaisecomGvrpPortFrameDiscard_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 42, 2, 1, 4, 1, 3),
    _RaisecomGvrpPortFrameDiscard_Type()
)
raisecomGvrpPortFrameDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomGvrpPortFrameDiscard.setStatus("current")
_RaisecomGmrpObjects_ObjectIdentity = ObjectIdentity
raisecomGmrpObjects = _RaisecomGmrpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 42, 2, 2)
)


class _RaisecomGmrpStatus_Type(EnabledStatus):
    """Custom type raisecomGmrpStatus based on EnabledStatus"""
    defaultValue = 2


_RaisecomGmrpStatus_Type.__name__ = "EnabledStatus"
_RaisecomGmrpStatus_Object = MibScalar
raisecomGmrpStatus = _RaisecomGmrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 42, 2, 2, 1),
    _RaisecomGmrpStatus_Type()
)
raisecomGmrpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomGmrpStatus.setStatus("current")
_RaisecomGmrpMaxGroup_Type = Integer32
_RaisecomGmrpMaxGroup_Object = MibScalar
raisecomGmrpMaxGroup = _RaisecomGmrpMaxGroup_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 42, 2, 2, 2),
    _RaisecomGmrpMaxGroup_Type()
)
raisecomGmrpMaxGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomGmrpMaxGroup.setStatus("current")
_RaisecomGmrpPortTable_Object = MibTable
raisecomGmrpPortTable = _RaisecomGmrpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 42, 2, 2, 3)
)
if mibBuilder.loadTexts:
    raisecomGmrpPortTable.setStatus("current")
_RaisecomGmrpPortEntry_Object = MibTableRow
raisecomGmrpPortEntry = _RaisecomGmrpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 42, 2, 2, 3, 1)
)
raisecomGmrpPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    raisecomGmrpPortEntry.setStatus("current")


class _RaisecomGmrpPortStatus_Type(EnabledStatus):
    """Custom type raisecomGmrpPortStatus based on EnabledStatus"""
    defaultValue = 1


_RaisecomGmrpPortStatus_Type.__name__ = "EnabledStatus"
_RaisecomGmrpPortStatus_Object = MibTableColumn
raisecomGmrpPortStatus = _RaisecomGmrpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 42, 2, 2, 3, 1, 1),
    _RaisecomGmrpPortStatus_Type()
)
raisecomGmrpPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomGmrpPortStatus.setStatus("current")
_RaisecomGmrpPortFailedRegistrations_Type = Counter32
_RaisecomGmrpPortFailedRegistrations_Object = MibTableColumn
raisecomGmrpPortFailedRegistrations = _RaisecomGmrpPortFailedRegistrations_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 42, 2, 2, 3, 1, 2),
    _RaisecomGmrpPortFailedRegistrations_Type()
)
raisecomGmrpPortFailedRegistrations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomGmrpPortFailedRegistrations.setStatus("current")
_RaisecomGmrpPortLastPduOrigin_Type = MacAddress
_RaisecomGmrpPortLastPduOrigin_Object = MibTableColumn
raisecomGmrpPortLastPduOrigin = _RaisecomGmrpPortLastPduOrigin_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 42, 2, 2, 3, 1, 3),
    _RaisecomGmrpPortLastPduOrigin_Type()
)
raisecomGmrpPortLastPduOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomGmrpPortLastPduOrigin.setStatus("current")


class _RaisecomGmrpPortRestrictedGroupRegistration_Type(TruthValue):
    """Custom type raisecomGmrpPortRestrictedGroupRegistration based on TruthValue"""
    defaultValue = 2


_RaisecomGmrpPortRestrictedGroupRegistration_Type.__name__ = "TruthValue"
_RaisecomGmrpPortRestrictedGroupRegistration_Object = MibTableColumn
raisecomGmrpPortRestrictedGroupRegistration = _RaisecomGmrpPortRestrictedGroupRegistration_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 42, 2, 2, 3, 1, 4),
    _RaisecomGmrpPortRestrictedGroupRegistration_Type()
)
raisecomGmrpPortRestrictedGroupRegistration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomGmrpPortRestrictedGroupRegistration.setStatus("current")


class _RaisecomGmrpPortRegistrationMode_Type(Integer32):
    """Custom type raisecomGmrpPortRegistrationMode based on Integer32"""
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
        *(("normal", 1),
          ("fixed", 2),
          ("forbidden", 3))
    )


_RaisecomGmrpPortRegistrationMode_Type.__name__ = "Integer32"
_RaisecomGmrpPortRegistrationMode_Object = MibTableColumn
raisecomGmrpPortRegistrationMode = _RaisecomGmrpPortRegistrationMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 42, 2, 2, 3, 1, 5),
    _RaisecomGmrpPortRegistrationMode_Type()
)
raisecomGmrpPortRegistrationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomGmrpPortRegistrationMode.setStatus("current")


class _RaisecomGmrpPortRunStatus_Type(EnableVar):
    """Custom type raisecomGmrpPortRunStatus based on EnableVar"""
    defaultValue = 2


_RaisecomGmrpPortRunStatus_Type.__name__ = "EnableVar"
_RaisecomGmrpPortRunStatus_Object = MibTableColumn
raisecomGmrpPortRunStatus = _RaisecomGmrpPortRunStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 42, 2, 2, 3, 1, 6),
    _RaisecomGmrpPortRunStatus_Type()
)
raisecomGmrpPortRunStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomGmrpPortRunStatus.setStatus("current")
_RaisecomGmrpPortStatisticTable_Object = MibTable
raisecomGmrpPortStatisticTable = _RaisecomGmrpPortStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 42, 2, 2, 4)
)
if mibBuilder.loadTexts:
    raisecomGmrpPortStatisticTable.setStatus("current")
_RaisecomGmrpPortStatisticEntry_Object = MibTableRow
raisecomGmrpPortStatisticEntry = _RaisecomGmrpPortStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 42, 2, 2, 4, 1)
)
raisecomGmrpPortStatisticEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    raisecomGmrpPortStatisticEntry.setStatus("current")
_RaisecomGmrpPortFrameRx_Type = Integer32
_RaisecomGmrpPortFrameRx_Object = MibTableColumn
raisecomGmrpPortFrameRx = _RaisecomGmrpPortFrameRx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 42, 2, 2, 4, 1, 1),
    _RaisecomGmrpPortFrameRx_Type()
)
raisecomGmrpPortFrameRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomGmrpPortFrameRx.setStatus("current")
_RaisecomGmrpPortFrameTx_Type = Integer32
_RaisecomGmrpPortFrameTx_Object = MibTableColumn
raisecomGmrpPortFrameTx = _RaisecomGmrpPortFrameTx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 42, 2, 2, 4, 1, 2),
    _RaisecomGmrpPortFrameTx_Type()
)
raisecomGmrpPortFrameTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomGmrpPortFrameTx.setStatus("current")
_RaisecomGmrpPortFrameDiscard_Type = Integer32
_RaisecomGmrpPortFrameDiscard_Object = MibTableColumn
raisecomGmrpPortFrameDiscard = _RaisecomGmrpPortFrameDiscard_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 42, 2, 2, 4, 1, 3),
    _RaisecomGmrpPortFrameDiscard_Type()
)
raisecomGmrpPortFrameDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomGmrpPortFrameDiscard.setStatus("current")
_RaisecomGarpConformance_ObjectIdentity = ObjectIdentity
raisecomGarpConformance = _RaisecomGarpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 42, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-GARP-MIB",
    **{"raisecomGarp": raisecomGarp,
       "raisecomGarpNotifications": raisecomGarpNotifications,
       "raisecomGarpCommonObjects": raisecomGarpCommonObjects,
       "raisecomGarpPortTable": raisecomGarpPortTable,
       "raisecomGarpPortEntry": raisecomGarpPortEntry,
       "raisecomGarpPortJoinTime": raisecomGarpPortJoinTime,
       "raisecomGarpPortLeaveTime": raisecomGarpPortLeaveTime,
       "raisecomGarpPortLeaveAllTime": raisecomGarpPortLeaveAllTime,
       "raisecomGarpPortStatisticClear": raisecomGarpPortStatisticClear,
       "raisecomGvrpPortStatisticClear": raisecomGvrpPortStatisticClear,
       "raisecomGmrpPortStatisticClear": raisecomGmrpPortStatisticClear,
       "raisecomGarpApplicationObjects": raisecomGarpApplicationObjects,
       "raisecomGvrpObjects": raisecomGvrpObjects,
       "raisecomGvrpStatus": raisecomGvrpStatus,
       "raisecomGvrpMaxVlan": raisecomGvrpMaxVlan,
       "raisecomGvrpPortTable": raisecomGvrpPortTable,
       "raisecomGvrpPortEntry": raisecomGvrpPortEntry,
       "raisecomGvrpPortStatus": raisecomGvrpPortStatus,
       "raisecomGvrpPortLastPduOrigin": raisecomGvrpPortLastPduOrigin,
       "raisecomGvrpPortFailedRegistrations": raisecomGvrpPortFailedRegistrations,
       "raisecomGvrpPortRestrictedVlanRegistration": raisecomGvrpPortRestrictedVlanRegistration,
       "raisecomGvrpPortRegistrationMode": raisecomGvrpPortRegistrationMode,
       "raisecomGvrpPortRunStatus": raisecomGvrpPortRunStatus,
       "raisecomGvrpPortStatisticTable": raisecomGvrpPortStatisticTable,
       "raisecomGvrpPortStatisticEntry": raisecomGvrpPortStatisticEntry,
       "raisecomGvrpPortFrameRx": raisecomGvrpPortFrameRx,
       "raisecomGvrpPortFrameTx": raisecomGvrpPortFrameTx,
       "raisecomGvrpPortFrameDiscard": raisecomGvrpPortFrameDiscard,
       "raisecomGmrpObjects": raisecomGmrpObjects,
       "raisecomGmrpStatus": raisecomGmrpStatus,
       "raisecomGmrpMaxGroup": raisecomGmrpMaxGroup,
       "raisecomGmrpPortTable": raisecomGmrpPortTable,
       "raisecomGmrpPortEntry": raisecomGmrpPortEntry,
       "raisecomGmrpPortStatus": raisecomGmrpPortStatus,
       "raisecomGmrpPortFailedRegistrations": raisecomGmrpPortFailedRegistrations,
       "raisecomGmrpPortLastPduOrigin": raisecomGmrpPortLastPduOrigin,
       "raisecomGmrpPortRestrictedGroupRegistration": raisecomGmrpPortRestrictedGroupRegistration,
       "raisecomGmrpPortRegistrationMode": raisecomGmrpPortRegistrationMode,
       "raisecomGmrpPortRunStatus": raisecomGmrpPortRunStatus,
       "raisecomGmrpPortStatisticTable": raisecomGmrpPortStatisticTable,
       "raisecomGmrpPortStatisticEntry": raisecomGmrpPortStatisticEntry,
       "raisecomGmrpPortFrameRx": raisecomGmrpPortFrameRx,
       "raisecomGmrpPortFrameTx": raisecomGmrpPortFrameTx,
       "raisecomGmrpPortFrameDiscard": raisecomGmrpPortFrameDiscard,
       "raisecomGarpConformance": raisecomGarpConformance}
)
