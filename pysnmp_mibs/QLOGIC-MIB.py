# SNMP MIB module (QLOGIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/marvell/QLOGIC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:47:52 2025
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

(connUnitId,) = mibBuilder.importSymbols(
    "FCMGMT-MIB",
    "connUnitId")

(ancorOidTree,) = mibBuilder.importSymbols(
    "QLOGIC-SMI",
    "ancorOidTree")

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

ancorPortModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1663, 1, 3)
)
if mibBuilder.loadTexts:
    ancorPortModule.setRevisions(
        ("2009-09-29 00:00",
         "2006-10-11 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FcQlModuleIndex(TextualConvention, Unsigned32):
    status = "current"


class FcQxPortIndex(TextualConvention, Unsigned32):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_QlSB2PortControl_ObjectIdentity = ObjectIdentity
qlSB2PortControl = _QlSB2PortControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1663, 1, 3, 10)
)
_FcQxPortPhysTable_Object = MibTable
fcQxPortPhysTable = _FcQxPortPhysTable_Object(
    (1, 3, 6, 1, 4, 1, 1663, 1, 3, 10, 1)
)
if mibBuilder.loadTexts:
    fcQxPortPhysTable.setStatus("current")
_FcQxPortPhysEntry_Object = MibTableRow
fcQxPortPhysEntry = _FcQxPortPhysEntry_Object(
    (1, 3, 6, 1, 4, 1, 1663, 1, 3, 10, 1, 1)
)
fcQxPortPhysEntry.setIndexNames(
    (0, "QLOGIC-MIB", "fcQxPortPhysModule"),
    (0, "QLOGIC-MIB", "fcQxPortPhysIndex"),
)
if mibBuilder.loadTexts:
    fcQxPortPhysEntry.setStatus("current")
_FcQxPortPhysModule_Type = FcQlModuleIndex
_FcQxPortPhysModule_Object = MibTableColumn
fcQxPortPhysModule = _FcQxPortPhysModule_Object(
    (1, 3, 6, 1, 4, 1, 1663, 1, 3, 10, 1, 1, 1),
    _FcQxPortPhysModule_Type()
)
fcQxPortPhysModule.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcQxPortPhysModule.setStatus("current")
_FcQxPortPhysIndex_Type = FcQxPortIndex
_FcQxPortPhysIndex_Object = MibTableColumn
fcQxPortPhysIndex = _FcQxPortPhysIndex_Object(
    (1, 3, 6, 1, 4, 1, 1663, 1, 3, 10, 1, 1, 2),
    _FcQxPortPhysIndex_Type()
)
fcQxPortPhysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcQxPortPhysIndex.setStatus("current")


class _FcQxPortPhysAdminStatus_Type(Integer32):
    """Custom type fcQxPortPhysAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("online", 1),
          ("offline", 2),
          ("testing", 3))
    )


_FcQxPortPhysAdminStatus_Type.__name__ = "Integer32"
_FcQxPortPhysAdminStatus_Object = MibTableColumn
fcQxPortPhysAdminStatus = _FcQxPortPhysAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1663, 1, 3, 10, 1, 1, 3),
    _FcQxPortPhysAdminStatus_Type()
)
fcQxPortPhysAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcQxPortPhysAdminStatus.setStatus("current")


class _FcQxPortPhysOperStatus_Type(Integer32):
    """Custom type fcQxPortPhysOperStatus based on Integer32"""
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
        *(("online", 1),
          ("offline", 2),
          ("testing", 3),
          ("linkFailure", 4))
    )


_FcQxPortPhysOperStatus_Type.__name__ = "Integer32"
_FcQxPortPhysOperStatus_Object = MibTableColumn
fcQxPortPhysOperStatus = _FcQxPortPhysOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1663, 1, 3, 10, 1, 1, 4),
    _FcQxPortPhysOperStatus_Type()
)
fcQxPortPhysOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcQxPortPhysOperStatus.setStatus("current")


class _FcQxQuailPortPhysAdminStatus_Type(Integer32):
    """Custom type fcQxQuailPortPhysAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_FcQxQuailPortPhysAdminStatus_Type.__name__ = "Integer32"
_FcQxQuailPortPhysAdminStatus_Object = MibTableColumn
fcQxQuailPortPhysAdminStatus = _FcQxQuailPortPhysAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1663, 1, 3, 10, 1, 1, 5),
    _FcQxQuailPortPhysAdminStatus_Type()
)
fcQxQuailPortPhysAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcQxQuailPortPhysAdminStatus.setStatus("current")


class _FcQxQuailPortPhysOperStatus_Type(Integer32):
    """Custom type fcQxQuailPortPhysOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_FcQxQuailPortPhysOperStatus_Type.__name__ = "Integer32"
_FcQxQuailPortPhysOperStatus_Object = MibTableColumn
fcQxQuailPortPhysOperStatus = _FcQxQuailPortPhysOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1663, 1, 3, 10, 1, 1, 6),
    _FcQxQuailPortPhysOperStatus_Type()
)
fcQxQuailPortPhysOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcQxQuailPortPhysOperStatus.setStatus("current")


class _FcQxQuailPortPhysReasonCode_Type(Integer32):
    """Custom type fcQxQuailPortPhysReasonCode based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("up", 2),
          ("down", 3),
          ("notConnected", 4),
          ("sfpAbsent", 5),
          ("sfpUnsupported", 6),
          ("hardwareFailure", 7),
          ("isolated", 8))
    )


_FcQxQuailPortPhysReasonCode_Type.__name__ = "Integer32"
_FcQxQuailPortPhysReasonCode_Object = MibTableColumn
fcQxQuailPortPhysReasonCode = _FcQxQuailPortPhysReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 1663, 1, 3, 10, 1, 1, 7),
    _FcQxQuailPortPhysReasonCode_Type()
)
fcQxQuailPortPhysReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcQxQuailPortPhysReasonCode.setStatus("current")
_QlSB2PortStatus_ObjectIdentity = ObjectIdentity
qlSB2PortStatus = _QlSB2PortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1663, 1, 3, 11)
)
_FcQxPortStatusTable_Object = MibTable
fcQxPortStatusTable = _FcQxPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1663, 1, 3, 11, 1)
)
if mibBuilder.loadTexts:
    fcQxPortStatusTable.setStatus("current")
_FcQxPortStatusEntry_Object = MibTableRow
fcQxPortStatusEntry = _FcQxPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1663, 1, 3, 11, 1, 1)
)
fcQxPortStatusEntry.setIndexNames(
    (0, "QLOGIC-MIB", "fcQxPortStatusModule"),
    (0, "QLOGIC-MIB", "fcQxPortStatusIndex"),
)
if mibBuilder.loadTexts:
    fcQxPortStatusEntry.setStatus("current")
_FcQxPortStatusModule_Type = FcQlModuleIndex
_FcQxPortStatusModule_Object = MibTableColumn
fcQxPortStatusModule = _FcQxPortStatusModule_Object(
    (1, 3, 6, 1, 4, 1, 1663, 1, 3, 11, 1, 1, 1),
    _FcQxPortStatusModule_Type()
)
fcQxPortStatusModule.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcQxPortStatusModule.setStatus("current")
_FcQxPortStatusIndex_Type = FcQxPortIndex
_FcQxPortStatusIndex_Object = MibTableColumn
fcQxPortStatusIndex = _FcQxPortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 1663, 1, 3, 11, 1, 1, 2),
    _FcQxPortStatusIndex_Type()
)
fcQxPortStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcQxPortStatusIndex.setStatus("current")


class _FcQxQuailPortOperMode_Type(Integer32):
    """Custom type fcQxQuailPortOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("fPort", 2),
          ("flPort", 3),
          ("ePort", 4),
          ("fxPort", 6))
    )


_FcQxQuailPortOperMode_Type.__name__ = "Integer32"
_FcQxQuailPortOperMode_Object = MibTableColumn
fcQxQuailPortOperMode = _FcQxQuailPortOperMode_Object(
    (1, 3, 6, 1, 4, 1, 1663, 1, 3, 11, 1, 1, 3),
    _FcQxQuailPortOperMode_Type()
)
fcQxQuailPortOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcQxQuailPortOperMode.setStatus("current")


class _FcQxQuailPortAdminMode_Type(Integer32):
    """Custom type fcQxQuailPortAdminMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("fPort", 2),
          ("flPort", 3),
          ("ePort", 4),
          ("fxPort", 6))
    )


_FcQxQuailPortAdminMode_Type.__name__ = "Integer32"
_FcQxQuailPortAdminMode_Object = MibTableColumn
fcQxQuailPortAdminMode = _FcQxQuailPortAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 1663, 1, 3, 11, 1, 1, 4),
    _FcQxQuailPortAdminMode_Type()
)
fcQxQuailPortAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcQxQuailPortAdminMode.setStatus("current")

# Managed Objects groups


# Notification objects

qlSB2PortLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1663, 1, 3, 0, 10)
)
qlSB2PortLinkDown.setObjects(
      *(("QLOGIC-MIB", "fcQxPortPhysAdminStatus"),
        ("QLOGIC-MIB", "fcQxPortPhysOperStatus"))
)
if mibBuilder.loadTexts:
    qlSB2PortLinkDown.setStatus(
        "current"
    )

qlSB2PortLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1663, 1, 3, 0, 11)
)
qlSB2PortLinkUp.setObjects(
      *(("QLOGIC-MIB", "fcQxPortPhysAdminStatus"),
        ("QLOGIC-MIB", "fcQxPortPhysOperStatus"))
)
if mibBuilder.loadTexts:
    qlSB2PortLinkUp.setStatus(
        "current"
    )

qlconnUnitAddedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1663, 1, 3, 0, 12)
)
qlconnUnitAddedTrap.setObjects(
    ("FCMGMT-MIB", "connUnitId")
)
if mibBuilder.loadTexts:
    qlconnUnitAddedTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QLOGIC-MIB",
    **{"FcQlModuleIndex": FcQlModuleIndex,
       "FcQxPortIndex": FcQxPortIndex,
       "ancorPortModule": ancorPortModule,
       "qlSB2PortLinkDown": qlSB2PortLinkDown,
       "qlSB2PortLinkUp": qlSB2PortLinkUp,
       "qlconnUnitAddedTrap": qlconnUnitAddedTrap,
       "qlSB2PortControl": qlSB2PortControl,
       "fcQxPortPhysTable": fcQxPortPhysTable,
       "fcQxPortPhysEntry": fcQxPortPhysEntry,
       "fcQxPortPhysModule": fcQxPortPhysModule,
       "fcQxPortPhysIndex": fcQxPortPhysIndex,
       "fcQxPortPhysAdminStatus": fcQxPortPhysAdminStatus,
       "fcQxPortPhysOperStatus": fcQxPortPhysOperStatus,
       "fcQxQuailPortPhysAdminStatus": fcQxQuailPortPhysAdminStatus,
       "fcQxQuailPortPhysOperStatus": fcQxQuailPortPhysOperStatus,
       "fcQxQuailPortPhysReasonCode": fcQxQuailPortPhysReasonCode,
       "qlSB2PortStatus": qlSB2PortStatus,
       "fcQxPortStatusTable": fcQxPortStatusTable,
       "fcQxPortStatusEntry": fcQxPortStatusEntry,
       "fcQxPortStatusModule": fcQxPortStatusModule,
       "fcQxPortStatusIndex": fcQxPortStatusIndex,
       "fcQxQuailPortOperMode": fcQxQuailPortOperMode,
       "fcQxQuailPortAdminMode": fcQxQuailPortAdminMode}
)
