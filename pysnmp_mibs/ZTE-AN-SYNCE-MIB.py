# SNMP MIB module (ZTE-AN-SYNCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-SYNCE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:43:53 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(ZxAnIfindex,
 zxAn) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "ZxAnIfindex",
    "zxAn")


# MODULE-IDENTITY

zxAnSyncEMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 65)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnSyncEObjects_ObjectIdentity = ObjectIdentity
zxAnSyncEObjects = _ZxAnSyncEObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 65, 1)
)
_ZxAnSyncEGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnSyncEGlobalObjects = _ZxAnSyncEGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 65, 1, 1)
)


class _ZxAnSyncEClockSourceType_Type(Integer32):
    """Custom type zxAnSyncEClockSourceType based on Integer32"""
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
        *(("localClock", 1),
          ("gps1pps", 2),
          ("pon8k", 3),
          ("clockRecovery", 4))
    )


_ZxAnSyncEClockSourceType_Type.__name__ = "Integer32"
_ZxAnSyncEClockSourceType_Object = MibScalar
zxAnSyncEClockSourceType = _ZxAnSyncEClockSourceType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 65, 1, 1, 1),
    _ZxAnSyncEClockSourceType_Type()
)
zxAnSyncEClockSourceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSyncEClockSourceType.setStatus("current")
_ZxAnSyncEClockRecoveryPort_Type = ZxAnIfindex
_ZxAnSyncEClockRecoveryPort_Object = MibScalar
zxAnSyncEClockRecoveryPort = _ZxAnSyncEClockRecoveryPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 65, 1, 1, 2),
    _ZxAnSyncEClockRecoveryPort_Type()
)
zxAnSyncEClockRecoveryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSyncEClockRecoveryPort.setStatus("current")


class _ZxAnSyncEUniPortSyncEnable_Type(Integer32):
    """Custom type zxAnSyncEUniPortSyncEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnSyncEUniPortSyncEnable_Type.__name__ = "Integer32"
_ZxAnSyncEUniPortSyncEnable_Object = MibScalar
zxAnSyncEUniPortSyncEnable = _ZxAnSyncEUniPortSyncEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 65, 1, 1, 3),
    _ZxAnSyncEUniPortSyncEnable_Type()
)
zxAnSyncEUniPortSyncEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSyncEUniPortSyncEnable.setStatus("current")


class _ZxAnSyncEClockSourceStatus_Type(Integer32):
    """Custom type zxAnSyncEClockSourceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_ZxAnSyncEClockSourceStatus_Type.__name__ = "Integer32"
_ZxAnSyncEClockSourceStatus_Object = MibScalar
zxAnSyncEClockSourceStatus = _ZxAnSyncEClockSourceStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 65, 1, 1, 4),
    _ZxAnSyncEClockSourceStatus_Type()
)
zxAnSyncEClockSourceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSyncEClockSourceStatus.setStatus("current")


class _ZxAnSyncEClockOperationStatus_Type(Integer32):
    """Custom type zxAnSyncEClockOperationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6,
              7,
              11,
              14,
              21,
              22,
              255)
        )
    )
    namedValues = NamedValues(
        *(("freerunPhaselockedNormal", 1),
          ("holdover", 2),
          ("locked", 4),
          ("prelocked2LostPhase", 5),
          ("prelocked", 6),
          ("lostPhase", 7),
          ("freerun2PhaselockedAbnormal", 11),
          ("directPass", 14),
          ("destroyFreerunOrHoldover", 21),
          ("acquiring", 22),
          ("unknown", 255))
    )


_ZxAnSyncEClockOperationStatus_Type.__name__ = "Integer32"
_ZxAnSyncEClockOperationStatus_Object = MibScalar
zxAnSyncEClockOperationStatus = _ZxAnSyncEClockOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 65, 1, 1, 5),
    _ZxAnSyncEClockOperationStatus_Type()
)
zxAnSyncEClockOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSyncEClockOperationStatus.setStatus("current")
_ZxAnSyncENniPortTable_Object = MibTable
zxAnSyncENniPortTable = _ZxAnSyncENniPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 65, 1, 2)
)
if mibBuilder.loadTexts:
    zxAnSyncENniPortTable.setStatus("current")
_ZxAnSyncENniPortEntry_Object = MibTableRow
zxAnSyncENniPortEntry = _ZxAnSyncENniPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 65, 1, 2, 1)
)
zxAnSyncENniPortEntry.setIndexNames(
    (0, "ZTE-AN-SYNCE-MIB", "zxAnSyncENniPortIndex"),
)
if mibBuilder.loadTexts:
    zxAnSyncENniPortEntry.setStatus("current")
_ZxAnSyncENniPortIndex_Type = ZxAnIfindex
_ZxAnSyncENniPortIndex_Object = MibTableColumn
zxAnSyncENniPortIndex = _ZxAnSyncENniPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 65, 1, 2, 1, 1),
    _ZxAnSyncENniPortIndex_Type()
)
zxAnSyncENniPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSyncENniPortIndex.setStatus("current")


class _ZxAnSyncENniPortSyncEnable_Type(Integer32):
    """Custom type zxAnSyncENniPortSyncEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnSyncENniPortSyncEnable_Type.__name__ = "Integer32"
_ZxAnSyncENniPortSyncEnable_Object = MibTableColumn
zxAnSyncENniPortSyncEnable = _ZxAnSyncENniPortSyncEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 65, 1, 2, 1, 2),
    _ZxAnSyncENniPortSyncEnable_Type()
)
zxAnSyncENniPortSyncEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSyncENniPortSyncEnable.setStatus("current")


class _ZxAnSyncENniPortClockMode_Type(Integer32):
    """Custom type zxAnSyncENniPortClockMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )


_ZxAnSyncENniPortClockMode_Type.__name__ = "Integer32"
_ZxAnSyncENniPortClockMode_Object = MibTableColumn
zxAnSyncENniPortClockMode = _ZxAnSyncENniPortClockMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 65, 1, 2, 1, 3),
    _ZxAnSyncENniPortClockMode_Type()
)
zxAnSyncENniPortClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSyncENniPortClockMode.setStatus("current")
_ZxAnSyncETrapObjects_ObjectIdentity = ObjectIdentity
zxAnSyncETrapObjects = _ZxAnSyncETrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 65, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-SYNCE-MIB",
    **{"zxAnSyncEMib": zxAnSyncEMib,
       "zxAnSyncEObjects": zxAnSyncEObjects,
       "zxAnSyncEGlobalObjects": zxAnSyncEGlobalObjects,
       "zxAnSyncEClockSourceType": zxAnSyncEClockSourceType,
       "zxAnSyncEClockRecoveryPort": zxAnSyncEClockRecoveryPort,
       "zxAnSyncEUniPortSyncEnable": zxAnSyncEUniPortSyncEnable,
       "zxAnSyncEClockSourceStatus": zxAnSyncEClockSourceStatus,
       "zxAnSyncEClockOperationStatus": zxAnSyncEClockOperationStatus,
       "zxAnSyncENniPortTable": zxAnSyncENniPortTable,
       "zxAnSyncENniPortEntry": zxAnSyncENniPortEntry,
       "zxAnSyncENniPortIndex": zxAnSyncENniPortIndex,
       "zxAnSyncENniPortSyncEnable": zxAnSyncENniPortSyncEnable,
       "zxAnSyncENniPortClockMode": zxAnSyncENniPortClockMode,
       "zxAnSyncETrapObjects": zxAnSyncETrapObjects}
)
