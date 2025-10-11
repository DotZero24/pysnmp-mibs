# SNMP MIB module (MELLANOX-IF-VPI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mellanox/MELLANOX-IF-VPI-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:10:43 2025
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

(mellanoxIfVPI,) = mibBuilder.importSymbols(
    "MELLANOX-SMI-MIB",
    "mellanoxIfVPI")

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

mellanoxIfVPIMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 3, 1)
)
if mibBuilder.loadTexts:
    mellanoxIfVPIMib.setRevisions(
        ("2017-07-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MellanoxIfVPITable_Object = MibTable
mellanoxIfVPITable = _MellanoxIfVPITable_Object(
    (1, 3, 6, 1, 4, 1, 33049, 3, 1, 1)
)
if mibBuilder.loadTexts:
    mellanoxIfVPITable.setStatus("current")
_MellanoxIfVPIEntry_Object = MibTableRow
mellanoxIfVPIEntry = _MellanoxIfVPIEntry_Object(
    (1, 3, 6, 1, 4, 1, 33049, 3, 1, 1, 1)
)
mellanoxIfVPIEntry.setIndexNames(
    (0, "MELLANOX-IF-VPI-MIB", "mellanoxIfVPIIndex"),
)
if mibBuilder.loadTexts:
    mellanoxIfVPIEntry.setStatus("current")
_MellanoxIfVPIIndex_Type = Integer32
_MellanoxIfVPIIndex_Object = MibTableColumn
mellanoxIfVPIIndex = _MellanoxIfVPIIndex_Object(
    (1, 3, 6, 1, 4, 1, 33049, 3, 1, 1, 1, 1),
    _MellanoxIfVPIIndex_Type()
)
mellanoxIfVPIIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxIfVPIIndex.setStatus("current")


class _MellanoxIfVPIIbPortPhysicalState_Type(Integer32):
    """Custom type mellanoxIfVPIIbPortPhysicalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              100)
        )
    )
    namedValues = NamedValues(
        *(("noStateChange", 0),
          ("sleep", 1),
          ("polling", 2),
          ("disabled", 3),
          ("portConfigurationTraining", 4),
          ("linkUp", 5),
          ("linkErrorRecovery", 6),
          ("phyTest", 7),
          ("notAvailable", 100))
    )


_MellanoxIfVPIIbPortPhysicalState_Type.__name__ = "Integer32"
_MellanoxIfVPIIbPortPhysicalState_Object = MibTableColumn
mellanoxIfVPIIbPortPhysicalState = _MellanoxIfVPIIbPortPhysicalState_Object(
    (1, 3, 6, 1, 4, 1, 33049, 3, 1, 1, 1, 2),
    _MellanoxIfVPIIbPortPhysicalState_Type()
)
mellanoxIfVPIIbPortPhysicalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxIfVPIIbPortPhysicalState.setStatus("current")


class _MellanoxIfVPIIbPortLogicalState_Type(Integer32):
    """Custom type mellanoxIfVPIIbPortLogicalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              100)
        )
    )
    namedValues = NamedValues(
        *(("noState", 0),
          ("down", 1),
          ("initialize", 2),
          ("armed", 3),
          ("active", 4),
          ("notAvailable", 100))
    )


_MellanoxIfVPIIbPortLogicalState_Type.__name__ = "Integer32"
_MellanoxIfVPIIbPortLogicalState_Object = MibTableColumn
mellanoxIfVPIIbPortLogicalState = _MellanoxIfVPIIbPortLogicalState_Object(
    (1, 3, 6, 1, 4, 1, 33049, 3, 1, 1, 1, 3),
    _MellanoxIfVPIIbPortLogicalState_Type()
)
mellanoxIfVPIIbPortLogicalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxIfVPIIbPortLogicalState.setStatus("current")
_MellanoxIfVPIIbPortGuid_Type = DisplayString
_MellanoxIfVPIIbPortGuid_Object = MibTableColumn
mellanoxIfVPIIbPortGuid = _MellanoxIfVPIIbPortGuid_Object(
    (1, 3, 6, 1, 4, 1, 33049, 3, 1, 1, 1, 4),
    _MellanoxIfVPIIbPortGuid_Type()
)
mellanoxIfVPIIbPortGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxIfVPIIbPortGuid.setStatus("current")
_MellanoxIfVPIPortXmitWait_Type = Counter64
_MellanoxIfVPIPortXmitWait_Object = MibTableColumn
mellanoxIfVPIPortXmitWait = _MellanoxIfVPIPortXmitWait_Object(
    (1, 3, 6, 1, 4, 1, 33049, 3, 1, 1, 1, 5),
    _MellanoxIfVPIPortXmitWait_Type()
)
mellanoxIfVPIPortXmitWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxIfVPIPortXmitWait.setStatus("current")
_MellanoxIfVPISymbolErrorCounter_Type = Counter64
_MellanoxIfVPISymbolErrorCounter_Object = MibTableColumn
mellanoxIfVPISymbolErrorCounter = _MellanoxIfVPISymbolErrorCounter_Object(
    (1, 3, 6, 1, 4, 1, 33049, 3, 1, 1, 1, 6),
    _MellanoxIfVPISymbolErrorCounter_Type()
)
mellanoxIfVPISymbolErrorCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxIfVPISymbolErrorCounter.setStatus("current")
_MellanoxIfVPIPortAdminSpeed_Type = Gauge32
_MellanoxIfVPIPortAdminSpeed_Object = MibTableColumn
mellanoxIfVPIPortAdminSpeed = _MellanoxIfVPIPortAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 33049, 3, 1, 1, 1, 7),
    _MellanoxIfVPIPortAdminSpeed_Type()
)
mellanoxIfVPIPortAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxIfVPIPortAdminSpeed.setStatus("current")
_MellanoxIfVPISubnetName_Type = DisplayString
_MellanoxIfVPISubnetName_Object = MibTableColumn
mellanoxIfVPISubnetName = _MellanoxIfVPISubnetName_Object(
    (1, 3, 6, 1, 4, 1, 33049, 3, 1, 1, 1, 8),
    _MellanoxIfVPISubnetName_Type()
)
mellanoxIfVPISubnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxIfVPISubnetName.setStatus("current")
_MellanoxIfVPISubnetPrefix_Type = DisplayString
_MellanoxIfVPISubnetPrefix_Object = MibTableColumn
mellanoxIfVPISubnetPrefix = _MellanoxIfVPISubnetPrefix_Object(
    (1, 3, 6, 1, 4, 1, 33049, 3, 1, 1, 1, 9),
    _MellanoxIfVPISubnetPrefix_Type()
)
mellanoxIfVPISubnetPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxIfVPISubnetPrefix.setStatus("current")
_MellanoxIfVPIIbLocalIdentifier_Type = Integer32
_MellanoxIfVPIIbLocalIdentifier_Object = MibTableColumn
mellanoxIfVPIIbLocalIdentifier = _MellanoxIfVPIIbLocalIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 33049, 3, 1, 1, 1, 10),
    _MellanoxIfVPIIbLocalIdentifier_Type()
)
mellanoxIfVPIIbLocalIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxIfVPIIbLocalIdentifier.setStatus("current")
_MellanoxIfVPI64bytePkts_Type = Counter64
_MellanoxIfVPI64bytePkts_Object = MibTableColumn
mellanoxIfVPI64bytePkts = _MellanoxIfVPI64bytePkts_Object(
    (1, 3, 6, 1, 4, 1, 33049, 3, 1, 1, 1, 11),
    _MellanoxIfVPI64bytePkts_Type()
)
mellanoxIfVPI64bytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxIfVPI64bytePkts.setStatus("current")
_MellanoxIfVPI65to127bytePkts_Type = Counter64
_MellanoxIfVPI65to127bytePkts_Object = MibTableColumn
mellanoxIfVPI65to127bytePkts = _MellanoxIfVPI65to127bytePkts_Object(
    (1, 3, 6, 1, 4, 1, 33049, 3, 1, 1, 1, 12),
    _MellanoxIfVPI65to127bytePkts_Type()
)
mellanoxIfVPI65to127bytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxIfVPI65to127bytePkts.setStatus("current")
_MellanoxIfVPI128to255bytePkts_Type = Counter64
_MellanoxIfVPI128to255bytePkts_Object = MibTableColumn
mellanoxIfVPI128to255bytePkts = _MellanoxIfVPI128to255bytePkts_Object(
    (1, 3, 6, 1, 4, 1, 33049, 3, 1, 1, 1, 13),
    _MellanoxIfVPI128to255bytePkts_Type()
)
mellanoxIfVPI128to255bytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxIfVPI128to255bytePkts.setStatus("current")
_MellanoxIfVPI256to511bytePkts_Type = Counter64
_MellanoxIfVPI256to511bytePkts_Object = MibTableColumn
mellanoxIfVPI256to511bytePkts = _MellanoxIfVPI256to511bytePkts_Object(
    (1, 3, 6, 1, 4, 1, 33049, 3, 1, 1, 1, 14),
    _MellanoxIfVPI256to511bytePkts_Type()
)
mellanoxIfVPI256to511bytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxIfVPI256to511bytePkts.setStatus("current")
_MellanoxIfVPI512to1023bytePkts_Type = Counter64
_MellanoxIfVPI512to1023bytePkts_Object = MibTableColumn
mellanoxIfVPI512to1023bytePkts = _MellanoxIfVPI512to1023bytePkts_Object(
    (1, 3, 6, 1, 4, 1, 33049, 3, 1, 1, 1, 15),
    _MellanoxIfVPI512to1023bytePkts_Type()
)
mellanoxIfVPI512to1023bytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxIfVPI512to1023bytePkts.setStatus("current")
_MellanoxIfVPI1024to1518bytePkts_Type = Counter64
_MellanoxIfVPI1024to1518bytePkts_Object = MibTableColumn
mellanoxIfVPI1024to1518bytePkts = _MellanoxIfVPI1024to1518bytePkts_Object(
    (1, 3, 6, 1, 4, 1, 33049, 3, 1, 1, 1, 16),
    _MellanoxIfVPI1024to1518bytePkts_Type()
)
mellanoxIfVPI1024to1518bytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxIfVPI1024to1518bytePkts.setStatus("current")
_MellanoxIfVPIJumboPkts_Type = Counter64
_MellanoxIfVPIJumboPkts_Object = MibTableColumn
mellanoxIfVPIJumboPkts = _MellanoxIfVPIJumboPkts_Object(
    (1, 3, 6, 1, 4, 1, 33049, 3, 1, 1, 1, 17),
    _MellanoxIfVPIJumboPkts_Type()
)
mellanoxIfVPIJumboPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxIfVPIJumboPkts.setStatus("current")
_MellanoxIfVPIUndersizedPkts_Type = Counter64
_MellanoxIfVPIUndersizedPkts_Object = MibTableColumn
mellanoxIfVPIUndersizedPkts = _MellanoxIfVPIUndersizedPkts_Object(
    (1, 3, 6, 1, 4, 1, 33049, 3, 1, 1, 1, 18),
    _MellanoxIfVPIUndersizedPkts_Type()
)
mellanoxIfVPIUndersizedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxIfVPIUndersizedPkts.setStatus("current")
_MellanoxIfVPIOversizedPkts_Type = Counter64
_MellanoxIfVPIOversizedPkts_Object = MibTableColumn
mellanoxIfVPIOversizedPkts = _MellanoxIfVPIOversizedPkts_Object(
    (1, 3, 6, 1, 4, 1, 33049, 3, 1, 1, 1, 19),
    _MellanoxIfVPIOversizedPkts_Type()
)
mellanoxIfVPIOversizedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxIfVPIOversizedPkts.setStatus("current")
_MellanoxIfVPIUnknownControlOpcode_Type = Counter64
_MellanoxIfVPIUnknownControlOpcode_Object = MibTableColumn
mellanoxIfVPIUnknownControlOpcode = _MellanoxIfVPIUnknownControlOpcode_Object(
    (1, 3, 6, 1, 4, 1, 33049, 3, 1, 1, 1, 20),
    _MellanoxIfVPIUnknownControlOpcode_Type()
)
mellanoxIfVPIUnknownControlOpcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxIfVPIUnknownControlOpcode.setStatus("current")
_MellanoxIfVPIFCSErrors_Type = Counter64
_MellanoxIfVPIFCSErrors_Object = MibTableColumn
mellanoxIfVPIFCSErrors = _MellanoxIfVPIFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 33049, 3, 1, 1, 1, 21),
    _MellanoxIfVPIFCSErrors_Type()
)
mellanoxIfVPIFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxIfVPIFCSErrors.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MELLANOX-IF-VPI-MIB",
    **{"mellanoxIfVPIMib": mellanoxIfVPIMib,
       "mellanoxIfVPITable": mellanoxIfVPITable,
       "mellanoxIfVPIEntry": mellanoxIfVPIEntry,
       "mellanoxIfVPIIndex": mellanoxIfVPIIndex,
       "mellanoxIfVPIIbPortPhysicalState": mellanoxIfVPIIbPortPhysicalState,
       "mellanoxIfVPIIbPortLogicalState": mellanoxIfVPIIbPortLogicalState,
       "mellanoxIfVPIIbPortGuid": mellanoxIfVPIIbPortGuid,
       "mellanoxIfVPIPortXmitWait": mellanoxIfVPIPortXmitWait,
       "mellanoxIfVPISymbolErrorCounter": mellanoxIfVPISymbolErrorCounter,
       "mellanoxIfVPIPortAdminSpeed": mellanoxIfVPIPortAdminSpeed,
       "mellanoxIfVPISubnetName": mellanoxIfVPISubnetName,
       "mellanoxIfVPISubnetPrefix": mellanoxIfVPISubnetPrefix,
       "mellanoxIfVPIIbLocalIdentifier": mellanoxIfVPIIbLocalIdentifier,
       "mellanoxIfVPI64bytePkts": mellanoxIfVPI64bytePkts,
       "mellanoxIfVPI65to127bytePkts": mellanoxIfVPI65to127bytePkts,
       "mellanoxIfVPI128to255bytePkts": mellanoxIfVPI128to255bytePkts,
       "mellanoxIfVPI256to511bytePkts": mellanoxIfVPI256to511bytePkts,
       "mellanoxIfVPI512to1023bytePkts": mellanoxIfVPI512to1023bytePkts,
       "mellanoxIfVPI1024to1518bytePkts": mellanoxIfVPI1024to1518bytePkts,
       "mellanoxIfVPIJumboPkts": mellanoxIfVPIJumboPkts,
       "mellanoxIfVPIUndersizedPkts": mellanoxIfVPIUndersizedPkts,
       "mellanoxIfVPIOversizedPkts": mellanoxIfVPIOversizedPkts,
       "mellanoxIfVPIUnknownControlOpcode": mellanoxIfVPIUnknownControlOpcode,
       "mellanoxIfVPIFCSErrors": mellanoxIfVPIFCSErrors}
)
