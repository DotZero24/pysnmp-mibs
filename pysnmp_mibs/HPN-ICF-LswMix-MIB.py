# SNMP MIB module (HPN-ICF-LswMix-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/HPN-ICF-LswMix-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:35:07 2025
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

(hpnicfLswFrameIndex,
 hpnicfLswSlotIndex) = mibBuilder.importSymbols(
    "HPN-ICF-LSW-DEV-ADM-MIB",
    "hpnicfLswFrameIndex",
    "hpnicfLswSlotIndex")

(hpnicflswCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicflswCommon")

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


# MODULE-IDENTITY

hpnicfLswMix = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 17)
)
if mibBuilder.loadTexts:
    hpnicfLswMix.setRevisions(
        ("2001-06-29 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfLswLastSwitchDate_Type = Integer32
_HpnicfLswLastSwitchDate_Object = MibScalar
hpnicfLswLastSwitchDate = _HpnicfLswLastSwitchDate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 17, 1),
    _HpnicfLswLastSwitchDate_Type()
)
hpnicfLswLastSwitchDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLswLastSwitchDate.setStatus("current")
_HpnicfLswLastSwitchTime_Type = Integer32
_HpnicfLswLastSwitchTime_Object = MibScalar
hpnicfLswLastSwitchTime = _HpnicfLswLastSwitchTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 17, 2),
    _HpnicfLswLastSwitchTime_Type()
)
hpnicfLswLastSwitchTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLswLastSwitchTime.setStatus("current")
_HpnicfLswMpuSwitchsNum_Type = Integer32
_HpnicfLswMpuSwitchsNum_Object = MibScalar
hpnicfLswMpuSwitchsNum = _HpnicfLswMpuSwitchsNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 17, 3),
    _HpnicfLswMpuSwitchsNum_Type()
)
hpnicfLswMpuSwitchsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLswMpuSwitchsNum.setStatus("current")


class _HpnicfLswMpuSwitch_Type(Integer32):
    """Custom type hpnicfLswMpuSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("switch", 1)
    )


_HpnicfLswMpuSwitch_Type.__name__ = "Integer32"
_HpnicfLswMpuSwitch_Object = MibScalar
hpnicfLswMpuSwitch = _HpnicfLswMpuSwitch_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 17, 4),
    _HpnicfLswMpuSwitch_Type()
)
hpnicfLswMpuSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfLswMpuSwitch.setStatus("current")
_HpnicfLswXSlotTable_Object = MibTable
hpnicfLswXSlotTable = _HpnicfLswXSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 17, 5)
)
if mibBuilder.loadTexts:
    hpnicfLswXSlotTable.setStatus("current")
_HpnicfLswXSlotEntry_Object = MibTableRow
hpnicfLswXSlotEntry = _HpnicfLswXSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 17, 5, 1)
)
hpnicfLswXSlotEntry.setIndexNames(
    (0, "HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"),
    (0, "HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex"),
)
if mibBuilder.loadTexts:
    hpnicfLswXSlotEntry.setStatus("current")


class _HpnicfLswMainCardBoardStatus_Type(Integer32):
    """Custom type hpnicfLswMainCardBoardStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("standby", 2),
          ("process", 3))
    )


_HpnicfLswMainCardBoardStatus_Type.__name__ = "Integer32"
_HpnicfLswMainCardBoardStatus_Object = MibTableColumn
hpnicfLswMainCardBoardStatus = _HpnicfLswMainCardBoardStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 17, 5, 1, 1),
    _HpnicfLswMainCardBoardStatus_Type()
)
hpnicfLswMainCardBoardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLswMainCardBoardStatus.setStatus("current")


class _HpnicfLswCrossBarStatus_Type(Integer32):
    """Custom type hpnicfLswCrossBarStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("standby", 2))
    )


_HpnicfLswCrossBarStatus_Type.__name__ = "Integer32"
_HpnicfLswCrossBarStatus_Object = MibTableColumn
hpnicfLswCrossBarStatus = _HpnicfLswCrossBarStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 17, 5, 1, 2),
    _HpnicfLswCrossBarStatus_Type()
)
hpnicfLswCrossBarStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLswCrossBarStatus.setStatus("current")
_HpnicfsMixTrapMib_ObjectIdentity = ObjectIdentity
hpnicfsMixTrapMib = _HpnicfsMixTrapMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 17, 10)
)

# Managed Objects groups


# Notification objects

hpnicfSlaveSwitchOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 17, 10, 1)
)
if mibBuilder.loadTexts:
    hpnicfSlaveSwitchOver.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-LswMix-MIB",
    **{"hpnicfLswMix": hpnicfLswMix,
       "hpnicfLswLastSwitchDate": hpnicfLswLastSwitchDate,
       "hpnicfLswLastSwitchTime": hpnicfLswLastSwitchTime,
       "hpnicfLswMpuSwitchsNum": hpnicfLswMpuSwitchsNum,
       "hpnicfLswMpuSwitch": hpnicfLswMpuSwitch,
       "hpnicfLswXSlotTable": hpnicfLswXSlotTable,
       "hpnicfLswXSlotEntry": hpnicfLswXSlotEntry,
       "hpnicfLswMainCardBoardStatus": hpnicfLswMainCardBoardStatus,
       "hpnicfLswCrossBarStatus": hpnicfLswCrossBarStatus,
       "hpnicfsMixTrapMib": hpnicfsMixTrapMib,
       "hpnicfSlaveSwitchOver": hpnicfSlaveSwitchOver}
)
