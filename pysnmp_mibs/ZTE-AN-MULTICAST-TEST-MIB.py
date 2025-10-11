# SNMP MIB module (ZTE-AN-MULTICAST-TEST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-MULTICAST-TEST-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:12 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(zxAn,) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "zxAn")


# MODULE-IDENTITY

zxAnMulticastTestMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 28)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnMulticastTestGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnMulticastTestGlobalObjects = _ZxAnMulticastTestGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 28, 1)
)


class _ZxAnMulticastTestCapabilities_Type(Bits):
    """Custom type zxAnMulticastTestCapabilities based on Bits"""
    namedValues = NamedValues(
        ("supportPriorityAndDuration", 0)
    )

_ZxAnMulticastTestCapabilities_Type.__name__ = "Bits"
_ZxAnMulticastTestCapabilities_Object = MibScalar
zxAnMulticastTestCapabilities = _ZxAnMulticastTestCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 28, 1, 1),
    _ZxAnMulticastTestCapabilities_Type()
)
zxAnMulticastTestCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMulticastTestCapabilities.setStatus("current")
_ZxAnMulticastTestObjects_ObjectIdentity = ObjectIdentity
zxAnMulticastTestObjects = _ZxAnMulticastTestObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 28, 2)
)
_ZxAnMulticastIfTest_ObjectIdentity = ObjectIdentity
zxAnMulticastIfTest = _ZxAnMulticastIfTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 28, 2, 1)
)
_ZxAnMulticastIfTestTable_Object = MibTable
zxAnMulticastIfTestTable = _ZxAnMulticastIfTestTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 28, 2, 1, 2)
)
if mibBuilder.loadTexts:
    zxAnMulticastIfTestTable.setStatus("current")
_ZxAnMulticastIfTestEntry_Object = MibTableRow
zxAnMulticastIfTestEntry = _ZxAnMulticastIfTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 28, 2, 1, 2, 1)
)
zxAnMulticastIfTestEntry.setIndexNames(
    (0, "ZTE-AN-MULTICAST-TEST-MIB", "zxAnMulticastIfTestRack"),
    (0, "ZTE-AN-MULTICAST-TEST-MIB", "zxAnMulticastIfTestShelf"),
    (0, "ZTE-AN-MULTICAST-TEST-MIB", "zxAnMulticastIfTestSlot"),
    (0, "ZTE-AN-MULTICAST-TEST-MIB", "zxAnMulticastIfTestPort"),
    (0, "ZTE-AN-MULTICAST-TEST-MIB", "zxAnMulticastIfTestOnu"),
    (0, "ZTE-AN-MULTICAST-TEST-MIB", "zxAnMulticastIfTestIfType"),
    (0, "ZTE-AN-MULTICAST-TEST-MIB", "zxAnMulticastIfTestLogicalId"),
)
if mibBuilder.loadTexts:
    zxAnMulticastIfTestEntry.setStatus("current")
_ZxAnMulticastIfTestRack_Type = Integer32
_ZxAnMulticastIfTestRack_Object = MibTableColumn
zxAnMulticastIfTestRack = _ZxAnMulticastIfTestRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 28, 2, 1, 2, 1, 1),
    _ZxAnMulticastIfTestRack_Type()
)
zxAnMulticastIfTestRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMulticastIfTestRack.setStatus("current")
_ZxAnMulticastIfTestShelf_Type = Integer32
_ZxAnMulticastIfTestShelf_Object = MibTableColumn
zxAnMulticastIfTestShelf = _ZxAnMulticastIfTestShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 28, 2, 1, 2, 1, 2),
    _ZxAnMulticastIfTestShelf_Type()
)
zxAnMulticastIfTestShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMulticastIfTestShelf.setStatus("current")
_ZxAnMulticastIfTestSlot_Type = Integer32
_ZxAnMulticastIfTestSlot_Object = MibTableColumn
zxAnMulticastIfTestSlot = _ZxAnMulticastIfTestSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 28, 2, 1, 2, 1, 3),
    _ZxAnMulticastIfTestSlot_Type()
)
zxAnMulticastIfTestSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMulticastIfTestSlot.setStatus("current")
_ZxAnMulticastIfTestPort_Type = Integer32
_ZxAnMulticastIfTestPort_Object = MibTableColumn
zxAnMulticastIfTestPort = _ZxAnMulticastIfTestPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 28, 2, 1, 2, 1, 4),
    _ZxAnMulticastIfTestPort_Type()
)
zxAnMulticastIfTestPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMulticastIfTestPort.setStatus("current")
_ZxAnMulticastIfTestOnu_Type = Integer32
_ZxAnMulticastIfTestOnu_Object = MibTableColumn
zxAnMulticastIfTestOnu = _ZxAnMulticastIfTestOnu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 28, 2, 1, 2, 1, 5),
    _ZxAnMulticastIfTestOnu_Type()
)
zxAnMulticastIfTestOnu.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMulticastIfTestOnu.setStatus("current")


class _ZxAnMulticastIfTestIfType_Type(Integer32):
    """Custom type zxAnMulticastIfTestIfType based on Integer32"""
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
        *(("physicalPort", 1),
          ("bridgePort", 2),
          ("ponOnu", 3),
          ("ponVPort", 4),
          ("onuUni", 5))
    )


_ZxAnMulticastIfTestIfType_Type.__name__ = "Integer32"
_ZxAnMulticastIfTestIfType_Object = MibTableColumn
zxAnMulticastIfTestIfType = _ZxAnMulticastIfTestIfType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 28, 2, 1, 2, 1, 6),
    _ZxAnMulticastIfTestIfType_Type()
)
zxAnMulticastIfTestIfType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMulticastIfTestIfType.setStatus("current")
_ZxAnMulticastIfTestLogicalId_Type = ObjectIdentifier
_ZxAnMulticastIfTestLogicalId_Object = MibTableColumn
zxAnMulticastIfTestLogicalId = _ZxAnMulticastIfTestLogicalId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 28, 2, 1, 2, 1, 7),
    _ZxAnMulticastIfTestLogicalId_Type()
)
zxAnMulticastIfTestLogicalId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMulticastIfTestLogicalId.setStatus("current")


class _ZxAnMulticastIfTestMvlanId_Type(Integer32):
    """Custom type zxAnMulticastIfTestMvlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_ZxAnMulticastIfTestMvlanId_Type.__name__ = "Integer32"
_ZxAnMulticastIfTestMvlanId_Object = MibTableColumn
zxAnMulticastIfTestMvlanId = _ZxAnMulticastIfTestMvlanId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 28, 2, 1, 2, 1, 8),
    _ZxAnMulticastIfTestMvlanId_Type()
)
zxAnMulticastIfTestMvlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMulticastIfTestMvlanId.setStatus("current")
_ZxAnMulticastIfTestGroupIpType_Type = InetAddressType
_ZxAnMulticastIfTestGroupIpType_Object = MibTableColumn
zxAnMulticastIfTestGroupIpType = _ZxAnMulticastIfTestGroupIpType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 28, 2, 1, 2, 1, 9),
    _ZxAnMulticastIfTestGroupIpType_Type()
)
zxAnMulticastIfTestGroupIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMulticastIfTestGroupIpType.setStatus("current")
_ZxAnMulticastIfTestGroupIp_Type = InetAddress
_ZxAnMulticastIfTestGroupIp_Object = MibTableColumn
zxAnMulticastIfTestGroupIp = _ZxAnMulticastIfTestGroupIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 28, 2, 1, 2, 1, 10),
    _ZxAnMulticastIfTestGroupIp_Type()
)
zxAnMulticastIfTestGroupIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMulticastIfTestGroupIp.setStatus("current")


class _ZxAnMulticastIfTestPriority_Type(Integer32):
    """Custom type zxAnMulticastIfTestPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnMulticastIfTestPriority_Type.__name__ = "Integer32"
_ZxAnMulticastIfTestPriority_Object = MibTableColumn
zxAnMulticastIfTestPriority = _ZxAnMulticastIfTestPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 28, 2, 1, 2, 1, 11),
    _ZxAnMulticastIfTestPriority_Type()
)
zxAnMulticastIfTestPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMulticastIfTestPriority.setStatus("current")


class _ZxAnMulticastIfTestDuration_Type(Integer32):
    """Custom type zxAnMulticastIfTestDuration based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_ZxAnMulticastIfTestDuration_Type.__name__ = "Integer32"
_ZxAnMulticastIfTestDuration_Object = MibTableColumn
zxAnMulticastIfTestDuration = _ZxAnMulticastIfTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 28, 2, 1, 2, 1, 12),
    _ZxAnMulticastIfTestDuration_Type()
)
zxAnMulticastIfTestDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMulticastIfTestDuration.setStatus("current")
if mibBuilder.loadTexts:
    zxAnMulticastIfTestDuration.setUnits("Seconds")


class _ZxAnMulticastIfTestStatus_Type(Integer32):
    """Custom type zxAnMulticastIfTestStatus based on Integer32"""
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
        *(("notStarted", 1),
          ("inProgress", 2),
          ("success", 3),
          ("failed", 4))
    )


_ZxAnMulticastIfTestStatus_Type.__name__ = "Integer32"
_ZxAnMulticastIfTestStatus_Object = MibTableColumn
zxAnMulticastIfTestStatus = _ZxAnMulticastIfTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 28, 2, 1, 2, 1, 20),
    _ZxAnMulticastIfTestStatus_Type()
)
zxAnMulticastIfTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMulticastIfTestStatus.setStatus("current")


class _ZxAnMulticastIfTestFailedReason_Type(Integer32):
    """Custom type zxAnMulticastIfTestFailedReason based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("pvcNotExist", 2),
          ("mvlanNotExist", 3),
          ("groupNotExist", 4),
          ("groupInvalid", 5),
          ("parameterError", 6),
          ("noTrafficDetected", 7),
          ("joinFailed", 8),
          ("leaveFailed", 9),
          ("setAclFailed", 10),
          ("setLoopbackFailed", 11),
          ("getStatsFailed", 12),
          ("hardwareNotSupport", 13),
          ("unknown", 255))
    )


_ZxAnMulticastIfTestFailedReason_Type.__name__ = "Integer32"
_ZxAnMulticastIfTestFailedReason_Object = MibTableColumn
zxAnMulticastIfTestFailedReason = _ZxAnMulticastIfTestFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 28, 2, 1, 2, 1, 21),
    _ZxAnMulticastIfTestFailedReason_Type()
)
zxAnMulticastIfTestFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMulticastIfTestFailedReason.setStatus("current")
_ZxAnMulticastIfTestBwAfterJoin_Type = Integer32
_ZxAnMulticastIfTestBwAfterJoin_Object = MibTableColumn
zxAnMulticastIfTestBwAfterJoin = _ZxAnMulticastIfTestBwAfterJoin_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 28, 2, 1, 2, 1, 23),
    _ZxAnMulticastIfTestBwAfterJoin_Type()
)
zxAnMulticastIfTestBwAfterJoin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMulticastIfTestBwAfterJoin.setStatus("current")
_ZxAnMulticastIfTestBwAfterLeave_Type = Integer32
_ZxAnMulticastIfTestBwAfterLeave_Object = MibTableColumn
zxAnMulticastIfTestBwAfterLeave = _ZxAnMulticastIfTestBwAfterLeave_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 28, 2, 1, 2, 1, 24),
    _ZxAnMulticastIfTestBwAfterLeave_Type()
)
zxAnMulticastIfTestBwAfterLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMulticastIfTestBwAfterLeave.setStatus("current")


class _ZxAnMulticastIfTestBwUnit_Type(Integer32):
    """Custom type zxAnMulticastIfTestBwUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pps", 1),
          ("kbps", 2))
    )


_ZxAnMulticastIfTestBwUnit_Type.__name__ = "Integer32"
_ZxAnMulticastIfTestBwUnit_Object = MibTableColumn
zxAnMulticastIfTestBwUnit = _ZxAnMulticastIfTestBwUnit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 28, 2, 1, 2, 1, 25),
    _ZxAnMulticastIfTestBwUnit_Type()
)
zxAnMulticastIfTestBwUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMulticastIfTestBwUnit.setStatus("current")
_ZxAnMulticastIfTestMcastPkts_Type = Counter32
_ZxAnMulticastIfTestMcastPkts_Object = MibTableColumn
zxAnMulticastIfTestMcastPkts = _ZxAnMulticastIfTestMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 28, 2, 1, 2, 1, 26),
    _ZxAnMulticastIfTestMcastPkts_Type()
)
zxAnMulticastIfTestMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMulticastIfTestMcastPkts.setStatus("current")


class _ZxAnMulticastIfTestAction_Type(Integer32):
    """Custom type zxAnMulticastIfTestAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2))
    )


_ZxAnMulticastIfTestAction_Type.__name__ = "Integer32"
_ZxAnMulticastIfTestAction_Object = MibTableColumn
zxAnMulticastIfTestAction = _ZxAnMulticastIfTestAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 28, 2, 1, 2, 1, 30),
    _ZxAnMulticastIfTestAction_Type()
)
zxAnMulticastIfTestAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMulticastIfTestAction.setStatus("current")
_ZxAnMulticastIfTestRowStatus_Type = RowStatus
_ZxAnMulticastIfTestRowStatus_Object = MibTableColumn
zxAnMulticastIfTestRowStatus = _ZxAnMulticastIfTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 28, 2, 1, 2, 1, 50),
    _ZxAnMulticastIfTestRowStatus_Type()
)
zxAnMulticastIfTestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMulticastIfTestRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-MULTICAST-TEST-MIB",
    **{"zxAnMulticastTestMib": zxAnMulticastTestMib,
       "zxAnMulticastTestGlobalObjects": zxAnMulticastTestGlobalObjects,
       "zxAnMulticastTestCapabilities": zxAnMulticastTestCapabilities,
       "zxAnMulticastTestObjects": zxAnMulticastTestObjects,
       "zxAnMulticastIfTest": zxAnMulticastIfTest,
       "zxAnMulticastIfTestTable": zxAnMulticastIfTestTable,
       "zxAnMulticastIfTestEntry": zxAnMulticastIfTestEntry,
       "zxAnMulticastIfTestRack": zxAnMulticastIfTestRack,
       "zxAnMulticastIfTestShelf": zxAnMulticastIfTestShelf,
       "zxAnMulticastIfTestSlot": zxAnMulticastIfTestSlot,
       "zxAnMulticastIfTestPort": zxAnMulticastIfTestPort,
       "zxAnMulticastIfTestOnu": zxAnMulticastIfTestOnu,
       "zxAnMulticastIfTestIfType": zxAnMulticastIfTestIfType,
       "zxAnMulticastIfTestLogicalId": zxAnMulticastIfTestLogicalId,
       "zxAnMulticastIfTestMvlanId": zxAnMulticastIfTestMvlanId,
       "zxAnMulticastIfTestGroupIpType": zxAnMulticastIfTestGroupIpType,
       "zxAnMulticastIfTestGroupIp": zxAnMulticastIfTestGroupIp,
       "zxAnMulticastIfTestPriority": zxAnMulticastIfTestPriority,
       "zxAnMulticastIfTestDuration": zxAnMulticastIfTestDuration,
       "zxAnMulticastIfTestStatus": zxAnMulticastIfTestStatus,
       "zxAnMulticastIfTestFailedReason": zxAnMulticastIfTestFailedReason,
       "zxAnMulticastIfTestBwAfterJoin": zxAnMulticastIfTestBwAfterJoin,
       "zxAnMulticastIfTestBwAfterLeave": zxAnMulticastIfTestBwAfterLeave,
       "zxAnMulticastIfTestBwUnit": zxAnMulticastIfTestBwUnit,
       "zxAnMulticastIfTestMcastPkts": zxAnMulticastIfTestMcastPkts,
       "zxAnMulticastIfTestAction": zxAnMulticastIfTestAction,
       "zxAnMulticastIfTestRowStatus": zxAnMulticastIfTestRowStatus}
)
