# SNMP MIB module (AT-DOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/allied-old/AT-DOS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:12:09 2025
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

(modules,) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "modules")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Bits,
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dosDefense = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 143)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _DosDefenseStatus_Type(Integer32):
    """Custom type dosDefenseStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_DosDefenseStatus_Type.__name__ = "Integer32"
_DosDefenseStatus_Object = MibScalar
dosDefenseStatus = _DosDefenseStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 143, 1),
    _DosDefenseStatus_Type()
)
dosDefenseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dosDefenseStatus.setStatus("current")


class _DosDefenseDebugMode_Type(Bits):
    """Custom type dosDefenseDebugMode based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("packet", 1),
          ("attack", 2),
          ("packet-attack", 3),
          ("diagnostics", 4),
          ("packet-diagnostics", 5),
          ("attack-diagnostics", 6),
          ("packet-attack-diagnostics", 7))
    )

_DosDefenseDebugMode_Type.__name__ = "Bits"
_DosDefenseDebugMode_Object = MibScalar
dosDefenseDebugMode = _DosDefenseDebugMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 143, 2),
    _DosDefenseDebugMode_Type()
)
dosDefenseDebugMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dosDefenseDebugMode.setStatus("current")


class _DosDefenseNumDebugPackets_Type(Integer32):
    """Custom type dosDefenseNumDebugPackets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("continuous", 0)
    )


_DosDefenseNumDebugPackets_Type.__name__ = "Integer32"
_DosDefenseNumDebugPackets_Object = MibScalar
dosDefenseNumDebugPackets = _DosDefenseNumDebugPackets_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 143, 3),
    _DosDefenseNumDebugPackets_Type()
)
dosDefenseNumDebugPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dosDefenseNumDebugPackets.setStatus("current")
_DosDefenseTable_Object = MibTable
dosDefenseTable = _DosDefenseTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 143, 4)
)
if mibBuilder.loadTexts:
    dosDefenseTable.setStatus("current")
_DosDefenseEntry_Object = MibTableRow
dosDefenseEntry = _DosDefenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 143, 4, 1)
)
dosDefenseEntry.setIndexNames(
    (0, "AT-DOS-MIB", "dosDefensePort"),
    (0, "AT-DOS-MIB", "dosDefenseAttackType"),
)
if mibBuilder.loadTexts:
    dosDefenseEntry.setStatus("current")


class _DosDefensePort_Type(Integer32):
    """Custom type dosDefensePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_DosDefensePort_Type.__name__ = "Integer32"
_DosDefensePort_Object = MibTableColumn
dosDefensePort = _DosDefensePort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 143, 4, 1, 1),
    _DosDefensePort_Type()
)
dosDefensePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dosDefensePort.setStatus("current")


class _DosDefenseAttackType_Type(Integer32):
    """Custom type dosDefenseAttackType based on Integer32"""
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
        *(("synFlood", 1),
          ("pingOfDeath", 2),
          ("smurf", 3),
          ("ipOptions", 4),
          ("land", 5),
          ("teardrop", 6),
          ("none", 7))
    )


_DosDefenseAttackType_Type.__name__ = "Integer32"
_DosDefenseAttackType_Object = MibTableColumn
dosDefenseAttackType = _DosDefenseAttackType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 143, 4, 1, 2),
    _DosDefenseAttackType_Type()
)
dosDefenseAttackType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dosDefenseAttackType.setStatus("current")


class _DosDefenseDefenseStatus_Type(Integer32):
    """Custom type dosDefenseDefenseStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("set", 3))
    )


_DosDefenseDefenseStatus_Type.__name__ = "Integer32"
_DosDefenseDefenseStatus_Object = MibTableColumn
dosDefenseDefenseStatus = _DosDefenseDefenseStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 143, 4, 1, 3),
    _DosDefenseDefenseStatus_Type()
)
dosDefenseDefenseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dosDefenseDefenseStatus.setStatus("current")


class _DosDefenseThreshold_Type(Integer32):
    """Custom type dosDefenseThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_DosDefenseThreshold_Type.__name__ = "Integer32"
_DosDefenseThreshold_Object = MibTableColumn
dosDefenseThreshold = _DosDefenseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 143, 4, 1, 4),
    _DosDefenseThreshold_Type()
)
dosDefenseThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dosDefenseThreshold.setStatus("current")


class _DosDefenseBlockTime_Type(Integer32):
    """Custom type dosDefenseBlockTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DosDefenseBlockTime_Type.__name__ = "Integer32"
_DosDefenseBlockTime_Object = MibTableColumn
dosDefenseBlockTime = _DosDefenseBlockTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 143, 4, 1, 5),
    _DosDefenseBlockTime_Type()
)
dosDefenseBlockTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dosDefenseBlockTime.setStatus("current")
if mibBuilder.loadTexts:
    dosDefenseBlockTime.setUnits("seconds")
_DosDefenseMirroring_Type = TruthValue
_DosDefenseMirroring_Object = MibTableColumn
dosDefenseMirroring = _DosDefenseMirroring_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 143, 4, 1, 6),
    _DosDefenseMirroring_Type()
)
dosDefenseMirroring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dosDefenseMirroring.setStatus("current")


class _DosDefensePortType_Type(Integer32):
    """Custom type dosDefensePortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("client", 1),
          ("gateway", 2))
    )


_DosDefensePortType_Type.__name__ = "Integer32"
_DosDefensePortType_Object = MibTableColumn
dosDefensePortType = _DosDefensePortType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 143, 4, 1, 7),
    _DosDefensePortType_Type()
)
dosDefensePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dosDefensePortType.setStatus("current")
_DosDefenseSubnetAddress_Type = IpAddress
_DosDefenseSubnetAddress_Object = MibTableColumn
dosDefenseSubnetAddress = _DosDefenseSubnetAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 143, 4, 1, 8),
    _DosDefenseSubnetAddress_Type()
)
dosDefenseSubnetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dosDefenseSubnetAddress.setStatus("current")
_DosDefenseSubnetMask_Type = IpAddress
_DosDefenseSubnetMask_Object = MibTableColumn
dosDefenseSubnetMask = _DosDefenseSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 143, 4, 1, 9),
    _DosDefenseSubnetMask_Type()
)
dosDefenseSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dosDefenseSubnetMask.setStatus("current")


class _DosDefenseAttackState_Type(Integer32):
    """Custom type dosDefenseAttackState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("suspected", 1),
          ("inProgress", 2))
    )


_DosDefenseAttackState_Type.__name__ = "Integer32"
_DosDefenseAttackState_Object = MibTableColumn
dosDefenseAttackState = _DosDefenseAttackState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 143, 4, 1, 10),
    _DosDefenseAttackState_Type()
)
dosDefenseAttackState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dosDefenseAttackState.setStatus("current")
_DosDefenseAttackCount_Type = Counter32
_DosDefenseAttackCount_Object = MibTableColumn
dosDefenseAttackCount = _DosDefenseAttackCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 143, 4, 1, 11),
    _DosDefenseAttackCount_Type()
)
dosDefenseAttackCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dosDefenseAttackCount.setStatus("current")


class _DosDefenseRemainingBlockTime_Type(Integer32):
    """Custom type dosDefenseRemainingBlockTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DosDefenseRemainingBlockTime_Type.__name__ = "Integer32"
_DosDefenseRemainingBlockTime_Object = MibTableColumn
dosDefenseRemainingBlockTime = _DosDefenseRemainingBlockTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 143, 4, 1, 12),
    _DosDefenseRemainingBlockTime_Type()
)
dosDefenseRemainingBlockTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dosDefenseRemainingBlockTime.setStatus("current")
if mibBuilder.loadTexts:
    dosDefenseRemainingBlockTime.setUnits("seconds")
_DosDefenseTraps_ObjectIdentity = ObjectIdentity
dosDefenseTraps = _DosDefenseTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 143, 5)
)

# Managed Objects groups


# Notification objects

dosDefenseAttackStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 143, 5, 1)
)
dosDefenseAttackStart.setObjects(
      *(("AT-DOS-MIB", "dosDefensePort"),
        ("AT-DOS-MIB", "dosDefenseAttackType"))
)
if mibBuilder.loadTexts:
    dosDefenseAttackStart.setStatus(
        "current"
    )

dosDefenseAttackEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 143, 5, 2)
)
dosDefenseAttackEnd.setObjects(
      *(("AT-DOS-MIB", "dosDefensePort"),
        ("AT-DOS-MIB", "dosDefenseAttackType"))
)
if mibBuilder.loadTexts:
    dosDefenseAttackEnd.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-DOS-MIB",
    **{"dosDefense": dosDefense,
       "dosDefenseStatus": dosDefenseStatus,
       "dosDefenseDebugMode": dosDefenseDebugMode,
       "dosDefenseNumDebugPackets": dosDefenseNumDebugPackets,
       "dosDefenseTable": dosDefenseTable,
       "dosDefenseEntry": dosDefenseEntry,
       "dosDefensePort": dosDefensePort,
       "dosDefenseAttackType": dosDefenseAttackType,
       "dosDefenseDefenseStatus": dosDefenseDefenseStatus,
       "dosDefenseThreshold": dosDefenseThreshold,
       "dosDefenseBlockTime": dosDefenseBlockTime,
       "dosDefenseMirroring": dosDefenseMirroring,
       "dosDefensePortType": dosDefensePortType,
       "dosDefenseSubnetAddress": dosDefenseSubnetAddress,
       "dosDefenseSubnetMask": dosDefenseSubnetMask,
       "dosDefenseAttackState": dosDefenseAttackState,
       "dosDefenseAttackCount": dosDefenseAttackCount,
       "dosDefenseRemainingBlockTime": dosDefenseRemainingBlockTime,
       "dosDefenseTraps": dosDefenseTraps,
       "dosDefenseAttackStart": dosDefenseAttackStart,
       "dosDefenseAttackEnd": dosDefenseAttackEnd}
)
