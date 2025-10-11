# SNMP MIB module (IEEE8023-MAU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rfc/IEEE8023-MAU-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:20:42 2025
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

(IANAifJackType,
 IANAifMauAutoNegCapBits,
 IANAifMauMediaAvailable,
 IANAifMauTypeListBits) = mibBuilder.importSymbols(
    "IANA-MAU-MIB",
    "IANAifJackType",
    "IANAifMauAutoNegCapBits",
    "IANAifMauMediaAvailable",
    "IANAifMauTypeListBits")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 org) = mibBuilder.importSymbols(
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
    "org")

(AutonomousType,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ieee8023mauMIB = ModuleIdentity(
    (1, 3, 111, 2, 802, 3, 1, 13)
)
if mibBuilder.loadTexts:
    ieee8023mauMIB.setRevisions(
        ("2013-04-11 00:00",
         "2011-02-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ieee8023snmpDot3MauMgt_ObjectIdentity = ObjectIdentity
ieee8023snmpDot3MauMgt = _Ieee8023snmpDot3MauMgt_ObjectIdentity(
    (1, 3, 111, 2, 802, 3, 1, 13, 1)
)
_SnmpDot3MauTraps_ObjectIdentity = ObjectIdentity
snmpDot3MauTraps = _SnmpDot3MauTraps_ObjectIdentity(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 0)
)
_Dot3RpMauBasicGroup_ObjectIdentity = ObjectIdentity
dot3RpMauBasicGroup = _Dot3RpMauBasicGroup_ObjectIdentity(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 1)
)
_RpMauTable_Object = MibTable
rpMauTable = _RpMauTable_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rpMauTable.setStatus("current")
_RpMauEntry_Object = MibTableRow
rpMauEntry = _RpMauEntry_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 1, 1, 1)
)
rpMauEntry.setIndexNames(
    (0, "IEEE8023-MAU-MIB", "rpMauGroupIndex"),
    (0, "IEEE8023-MAU-MIB", "rpMauPortIndex"),
    (0, "IEEE8023-MAU-MIB", "rpMauIndex"),
)
if mibBuilder.loadTexts:
    rpMauEntry.setStatus("current")


class _RpMauGroupIndex_Type(Integer32):
    """Custom type rpMauGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RpMauGroupIndex_Type.__name__ = "Integer32"
_RpMauGroupIndex_Object = MibTableColumn
rpMauGroupIndex = _RpMauGroupIndex_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 1, 1, 1, 1),
    _RpMauGroupIndex_Type()
)
rpMauGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rpMauGroupIndex.setStatus("current")


class _RpMauPortIndex_Type(Integer32):
    """Custom type rpMauPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RpMauPortIndex_Type.__name__ = "Integer32"
_RpMauPortIndex_Object = MibTableColumn
rpMauPortIndex = _RpMauPortIndex_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 1, 1, 1, 2),
    _RpMauPortIndex_Type()
)
rpMauPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rpMauPortIndex.setStatus("current")


class _RpMauIndex_Type(Integer32):
    """Custom type rpMauIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RpMauIndex_Type.__name__ = "Integer32"
_RpMauIndex_Object = MibTableColumn
rpMauIndex = _RpMauIndex_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 1, 1, 1, 3),
    _RpMauIndex_Type()
)
rpMauIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rpMauIndex.setStatus("current")
_RpMauType_Type = AutonomousType
_RpMauType_Object = MibTableColumn
rpMauType = _RpMauType_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 1, 1, 1, 4),
    _RpMauType_Type()
)
rpMauType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpMauType.setStatus("current")


class _RpMauStatus_Type(Integer32):
    """Custom type rpMauStatus based on Integer32"""
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
        *(("other", 1),
          ("unknown", 2),
          ("operational", 3),
          ("standby", 4),
          ("shutdown", 5),
          ("reset", 6))
    )


_RpMauStatus_Type.__name__ = "Integer32"
_RpMauStatus_Object = MibTableColumn
rpMauStatus = _RpMauStatus_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 1, 1, 1, 5),
    _RpMauStatus_Type()
)
rpMauStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpMauStatus.setStatus("current")
_RpMauMediaAvailable_Type = IANAifMauMediaAvailable
_RpMauMediaAvailable_Object = MibTableColumn
rpMauMediaAvailable = _RpMauMediaAvailable_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 1, 1, 1, 6),
    _RpMauMediaAvailable_Type()
)
rpMauMediaAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpMauMediaAvailable.setStatus("current")
_RpMauMediaAvailableStateExits_Type = Counter32
_RpMauMediaAvailableStateExits_Object = MibTableColumn
rpMauMediaAvailableStateExits = _RpMauMediaAvailableStateExits_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 1, 1, 1, 7),
    _RpMauMediaAvailableStateExits_Type()
)
rpMauMediaAvailableStateExits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpMauMediaAvailableStateExits.setStatus("current")


class _RpMauJabberState_Type(Integer32):
    """Custom type rpMauJabberState based on Integer32"""
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
        *(("other", 1),
          ("unknown", 2),
          ("noJabber", 3),
          ("jabbering", 4))
    )


_RpMauJabberState_Type.__name__ = "Integer32"
_RpMauJabberState_Object = MibTableColumn
rpMauJabberState = _RpMauJabberState_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 1, 1, 1, 8),
    _RpMauJabberState_Type()
)
rpMauJabberState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpMauJabberState.setStatus("current")
_RpMauJabberingStateEnters_Type = Counter32
_RpMauJabberingStateEnters_Object = MibTableColumn
rpMauJabberingStateEnters = _RpMauJabberingStateEnters_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 1, 1, 1, 9),
    _RpMauJabberingStateEnters_Type()
)
rpMauJabberingStateEnters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpMauJabberingStateEnters.setStatus("current")
_RpMauFalseCarriers_Type = Counter32
_RpMauFalseCarriers_Object = MibTableColumn
rpMauFalseCarriers = _RpMauFalseCarriers_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 1, 1, 1, 10),
    _RpMauFalseCarriers_Type()
)
rpMauFalseCarriers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpMauFalseCarriers.setStatus("current")
_RpJackTable_Object = MibTable
rpJackTable = _RpJackTable_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 1, 2)
)
if mibBuilder.loadTexts:
    rpJackTable.setStatus("current")
_RpJackEntry_Object = MibTableRow
rpJackEntry = _RpJackEntry_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 1, 2, 1)
)
rpJackEntry.setIndexNames(
    (0, "IEEE8023-MAU-MIB", "rpMauGroupIndex"),
    (0, "IEEE8023-MAU-MIB", "rpMauPortIndex"),
    (0, "IEEE8023-MAU-MIB", "rpMauIndex"),
    (0, "IEEE8023-MAU-MIB", "rpJackIndex"),
)
if mibBuilder.loadTexts:
    rpJackEntry.setStatus("current")


class _RpJackIndex_Type(Integer32):
    """Custom type rpJackIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RpJackIndex_Type.__name__ = "Integer32"
_RpJackIndex_Object = MibTableColumn
rpJackIndex = _RpJackIndex_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 1, 2, 1, 1),
    _RpJackIndex_Type()
)
rpJackIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rpJackIndex.setStatus("current")
_RpJackType_Type = IANAifJackType
_RpJackType_Object = MibTableColumn
rpJackType = _RpJackType_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 1, 2, 1, 2),
    _RpJackType_Type()
)
rpJackType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpJackType.setStatus("current")
_Dot3IfMauBasicGroup_ObjectIdentity = ObjectIdentity
dot3IfMauBasicGroup = _Dot3IfMauBasicGroup_ObjectIdentity(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 2)
)
_IfMauTable_Object = MibTable
ifMauTable = _IfMauTable_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ifMauTable.setStatus("current")
_IfMauEntry_Object = MibTableRow
ifMauEntry = _IfMauEntry_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 2, 1, 1)
)
ifMauEntry.setIndexNames(
    (0, "IEEE8023-MAU-MIB", "ifMauIfIndex"),
    (0, "IEEE8023-MAU-MIB", "ifMauIndex"),
)
if mibBuilder.loadTexts:
    ifMauEntry.setStatus("current")
_IfMauIfIndex_Type = InterfaceIndex
_IfMauIfIndex_Object = MibTableColumn
ifMauIfIndex = _IfMauIfIndex_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 2, 1, 1, 1),
    _IfMauIfIndex_Type()
)
ifMauIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifMauIfIndex.setStatus("current")


class _IfMauIndex_Type(Integer32):
    """Custom type ifMauIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IfMauIndex_Type.__name__ = "Integer32"
_IfMauIndex_Object = MibTableColumn
ifMauIndex = _IfMauIndex_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 2, 1, 1, 2),
    _IfMauIndex_Type()
)
ifMauIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifMauIndex.setStatus("current")
_IfMauType_Type = AutonomousType
_IfMauType_Object = MibTableColumn
ifMauType = _IfMauType_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 2, 1, 1, 3),
    _IfMauType_Type()
)
ifMauType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauType.setStatus("current")


class _IfMauStatus_Type(Integer32):
    """Custom type ifMauStatus based on Integer32"""
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
        *(("other", 1),
          ("unknown", 2),
          ("operational", 3),
          ("standby", 4),
          ("shutdown", 5),
          ("reset", 6))
    )


_IfMauStatus_Type.__name__ = "Integer32"
_IfMauStatus_Object = MibTableColumn
ifMauStatus = _IfMauStatus_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 2, 1, 1, 4),
    _IfMauStatus_Type()
)
ifMauStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifMauStatus.setStatus("current")
_IfMauMediaAvailable_Type = IANAifMauMediaAvailable
_IfMauMediaAvailable_Object = MibTableColumn
ifMauMediaAvailable = _IfMauMediaAvailable_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 2, 1, 1, 5),
    _IfMauMediaAvailable_Type()
)
ifMauMediaAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauMediaAvailable.setStatus("current")
_IfMauMediaAvailableStateExits_Type = Counter32
_IfMauMediaAvailableStateExits_Object = MibTableColumn
ifMauMediaAvailableStateExits = _IfMauMediaAvailableStateExits_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 2, 1, 1, 6),
    _IfMauMediaAvailableStateExits_Type()
)
ifMauMediaAvailableStateExits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauMediaAvailableStateExits.setStatus("current")


class _IfMauJabberState_Type(Integer32):
    """Custom type ifMauJabberState based on Integer32"""
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
        *(("other", 1),
          ("unknown", 2),
          ("noJabber", 3),
          ("jabbering", 4))
    )


_IfMauJabberState_Type.__name__ = "Integer32"
_IfMauJabberState_Object = MibTableColumn
ifMauJabberState = _IfMauJabberState_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 2, 1, 1, 7),
    _IfMauJabberState_Type()
)
ifMauJabberState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauJabberState.setStatus("current")
_IfMauJabberingStateEnters_Type = Counter32
_IfMauJabberingStateEnters_Object = MibTableColumn
ifMauJabberingStateEnters = _IfMauJabberingStateEnters_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 2, 1, 1, 8),
    _IfMauJabberingStateEnters_Type()
)
ifMauJabberingStateEnters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauJabberingStateEnters.setStatus("current")
_IfMauFalseCarriers_Type = Counter32
_IfMauFalseCarriers_Object = MibTableColumn
ifMauFalseCarriers = _IfMauFalseCarriers_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 2, 1, 1, 9),
    _IfMauFalseCarriers_Type()
)
ifMauFalseCarriers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauFalseCarriers.setStatus("current")
_IfMauDefaultType_Type = AutonomousType
_IfMauDefaultType_Object = MibTableColumn
ifMauDefaultType = _IfMauDefaultType_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 2, 1, 1, 10),
    _IfMauDefaultType_Type()
)
ifMauDefaultType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifMauDefaultType.setStatus("current")
_IfMauAutoNegSupported_Type = TruthValue
_IfMauAutoNegSupported_Object = MibTableColumn
ifMauAutoNegSupported = _IfMauAutoNegSupported_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 2, 1, 1, 11),
    _IfMauAutoNegSupported_Type()
)
ifMauAutoNegSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauAutoNegSupported.setStatus("current")
_IfMauTypeListBits_Type = IANAifMauTypeListBits
_IfMauTypeListBits_Object = MibTableColumn
ifMauTypeListBits = _IfMauTypeListBits_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 2, 1, 1, 12),
    _IfMauTypeListBits_Type()
)
ifMauTypeListBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauTypeListBits.setStatus("current")
_IfMauHCFalseCarriers_Type = Counter64
_IfMauHCFalseCarriers_Object = MibTableColumn
ifMauHCFalseCarriers = _IfMauHCFalseCarriers_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 2, 1, 1, 13),
    _IfMauHCFalseCarriers_Type()
)
ifMauHCFalseCarriers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauHCFalseCarriers.setStatus("current")
_IfMauPCSCodingViolations_Type = Counter64
_IfMauPCSCodingViolations_Object = MibTableColumn
ifMauPCSCodingViolations = _IfMauPCSCodingViolations_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 2, 1, 1, 14),
    _IfMauPCSCodingViolations_Type()
)
ifMauPCSCodingViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauPCSCodingViolations.setStatus("current")


class _IfMauFECAbility_Type(Integer32):
    """Custom type ifMauFECAbility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("supported", 2),
          ("notsupported", 3))
    )


_IfMauFECAbility_Type.__name__ = "Integer32"
_IfMauFECAbility_Object = MibTableColumn
ifMauFECAbility = _IfMauFECAbility_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 2, 1, 1, 15),
    _IfMauFECAbility_Type()
)
ifMauFECAbility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauFECAbility.setStatus("current")


class _IfMauFECMode_Type(Integer32):
    """Custom type ifMauFECMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_IfMauFECMode_Type.__name__ = "Integer32"
_IfMauFECMode_Object = MibTableColumn
ifMauFECMode = _IfMauFECMode_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 2, 1, 1, 16),
    _IfMauFECMode_Type()
)
ifMauFECMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifMauFECMode.setStatus("current")
_IfMauFECCorrectedBlocks_Type = Counter64
_IfMauFECCorrectedBlocks_Object = MibTableColumn
ifMauFECCorrectedBlocks = _IfMauFECCorrectedBlocks_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 2, 1, 1, 17),
    _IfMauFECCorrectedBlocks_Type()
)
ifMauFECCorrectedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauFECCorrectedBlocks.setStatus("deprecated")
_IfMauFECUnCorrectableBlocks_Type = Counter64
_IfMauFECUnCorrectableBlocks_Object = MibTableColumn
ifMauFECUnCorrectableBlocks = _IfMauFECUnCorrectableBlocks_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 2, 1, 1, 18),
    _IfMauFECUnCorrectableBlocks_Type()
)
ifMauFECUnCorrectableBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauFECUnCorrectableBlocks.setStatus("deprecated")


class _IfMauSNROpMarginChnlA_Type(Integer32):
    """Custom type ifMauSNROpMarginChnlA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 127),
    )


_IfMauSNROpMarginChnlA_Type.__name__ = "Integer32"
_IfMauSNROpMarginChnlA_Object = MibTableColumn
ifMauSNROpMarginChnlA = _IfMauSNROpMarginChnlA_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 2, 1, 1, 19),
    _IfMauSNROpMarginChnlA_Type()
)
ifMauSNROpMarginChnlA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauSNROpMarginChnlA.setStatus("current")


class _IfMauSNROpMarginChnlB_Type(Integer32):
    """Custom type ifMauSNROpMarginChnlB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 127),
    )


_IfMauSNROpMarginChnlB_Type.__name__ = "Integer32"
_IfMauSNROpMarginChnlB_Object = MibTableColumn
ifMauSNROpMarginChnlB = _IfMauSNROpMarginChnlB_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 2, 1, 1, 20),
    _IfMauSNROpMarginChnlB_Type()
)
ifMauSNROpMarginChnlB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauSNROpMarginChnlB.setStatus("current")


class _IfMauSNROpMarginChnlC_Type(Integer32):
    """Custom type ifMauSNROpMarginChnlC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 127),
    )


_IfMauSNROpMarginChnlC_Type.__name__ = "Integer32"
_IfMauSNROpMarginChnlC_Object = MibTableColumn
ifMauSNROpMarginChnlC = _IfMauSNROpMarginChnlC_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 2, 1, 1, 21),
    _IfMauSNROpMarginChnlC_Type()
)
ifMauSNROpMarginChnlC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauSNROpMarginChnlC.setStatus("current")


class _IfMauSNROpMarginChnlD_Type(Integer32):
    """Custom type ifMauSNROpMarginChnlD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 127),
    )


_IfMauSNROpMarginChnlD_Type.__name__ = "Integer32"
_IfMauSNROpMarginChnlD_Object = MibTableColumn
ifMauSNROpMarginChnlD = _IfMauSNROpMarginChnlD_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 2, 1, 1, 22),
    _IfMauSNROpMarginChnlD_Type()
)
ifMauSNROpMarginChnlD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauSNROpMarginChnlD.setStatus("current")
_IfMauEEESupportList_Type = IANAifMauTypeListBits
_IfMauEEESupportList_Object = MibTableColumn
ifMauEEESupportList = _IfMauEEESupportList_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 2, 1, 1, 23),
    _IfMauEEESupportList_Type()
)
ifMauEEESupportList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauEEESupportList.setStatus("current")
_IfMauEEELDFastRetrainCount_Type = Counter32
_IfMauEEELDFastRetrainCount_Object = MibTableColumn
ifMauEEELDFastRetrainCount = _IfMauEEELDFastRetrainCount_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 2, 1, 1, 24),
    _IfMauEEELDFastRetrainCount_Type()
)
ifMauEEELDFastRetrainCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauEEELDFastRetrainCount.setStatus("current")
_IfMauEEELPFastRetrainCount_Type = Counter32
_IfMauEEELPFastRetrainCount_Object = MibTableColumn
ifMauEEELPFastRetrainCount = _IfMauEEELPFastRetrainCount_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 2, 1, 1, 25),
    _IfMauEEELPFastRetrainCount_Type()
)
ifMauEEELPFastRetrainCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauEEELPFastRetrainCount.setStatus("current")
_IfMauTimeSyncCapabilityTX_Type = TruthValue
_IfMauTimeSyncCapabilityTX_Object = MibTableColumn
ifMauTimeSyncCapabilityTX = _IfMauTimeSyncCapabilityTX_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 2, 1, 1, 26),
    _IfMauTimeSyncCapabilityTX_Type()
)
ifMauTimeSyncCapabilityTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauTimeSyncCapabilityTX.setStatus("current")
_IfMauTimeSyncCapabilityRX_Type = TruthValue
_IfMauTimeSyncCapabilityRX_Object = MibTableColumn
ifMauTimeSyncCapabilityRX = _IfMauTimeSyncCapabilityRX_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 2, 1, 1, 27),
    _IfMauTimeSyncCapabilityRX_Type()
)
ifMauTimeSyncCapabilityRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauTimeSyncCapabilityRX.setStatus("current")
_IfMauTimeSyncDelayTXmax_Type = Integer32
_IfMauTimeSyncDelayTXmax_Object = MibTableColumn
ifMauTimeSyncDelayTXmax = _IfMauTimeSyncDelayTXmax_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 2, 1, 1, 28),
    _IfMauTimeSyncDelayTXmax_Type()
)
ifMauTimeSyncDelayTXmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauTimeSyncDelayTXmax.setStatus("current")
_IfMauTimeSyncDelayTXmin_Type = Integer32
_IfMauTimeSyncDelayTXmin_Object = MibTableColumn
ifMauTimeSyncDelayTXmin = _IfMauTimeSyncDelayTXmin_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 2, 1, 1, 29),
    _IfMauTimeSyncDelayTXmin_Type()
)
ifMauTimeSyncDelayTXmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauTimeSyncDelayTXmin.setStatus("current")
_IfMauTimeSyncDelayRXmax_Type = Integer32
_IfMauTimeSyncDelayRXmax_Object = MibTableColumn
ifMauTimeSyncDelayRXmax = _IfMauTimeSyncDelayRXmax_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 2, 1, 1, 30),
    _IfMauTimeSyncDelayRXmax_Type()
)
ifMauTimeSyncDelayRXmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauTimeSyncDelayRXmax.setStatus("current")
_IfMauTimeSyncDelayRXmin_Type = Integer32
_IfMauTimeSyncDelayRXmin_Object = MibTableColumn
ifMauTimeSyncDelayRXmin = _IfMauTimeSyncDelayRXmin_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 2, 1, 1, 31),
    _IfMauTimeSyncDelayRXmin_Type()
)
ifMauTimeSyncDelayRXmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauTimeSyncDelayRXmin.setStatus("current")
_IfJackTable_Object = MibTable
ifJackTable = _IfJackTable_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ifJackTable.setStatus("current")
_IfJackEntry_Object = MibTableRow
ifJackEntry = _IfJackEntry_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 2, 2, 1)
)
ifJackEntry.setIndexNames(
    (0, "IEEE8023-MAU-MIB", "ifMauIfIndex"),
    (0, "IEEE8023-MAU-MIB", "ifMauIndex"),
    (0, "IEEE8023-MAU-MIB", "ifJackIndex"),
)
if mibBuilder.loadTexts:
    ifJackEntry.setStatus("current")


class _IfJackIndex_Type(Integer32):
    """Custom type ifJackIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IfJackIndex_Type.__name__ = "Integer32"
_IfJackIndex_Object = MibTableColumn
ifJackIndex = _IfJackIndex_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 2, 2, 1, 1),
    _IfJackIndex_Type()
)
ifJackIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifJackIndex.setStatus("current")
_IfJackType_Type = IANAifJackType
_IfJackType_Object = MibTableColumn
ifJackType = _IfJackType_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 2, 2, 1, 2),
    _IfJackType_Type()
)
ifJackType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJackType.setStatus("current")
_IfMauPerPCSLaneStatsTable_Object = MibTable
ifMauPerPCSLaneStatsTable = _IfMauPerPCSLaneStatsTable_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ifMauPerPCSLaneStatsTable.setStatus("current")
_IfMauPerPCSLaneStatsEntry_Object = MibTableRow
ifMauPerPCSLaneStatsEntry = _IfMauPerPCSLaneStatsEntry_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 2, 3, 1)
)
ifMauPerPCSLaneStatsEntry.setIndexNames(
    (0, "IEEE8023-MAU-MIB", "ifMauIfIndex"),
    (0, "IEEE8023-MAU-MIB", "ifMauIndex"),
    (0, "IEEE8023-MAU-MIB", "ifPCSLaneIndex"),
)
if mibBuilder.loadTexts:
    ifMauPerPCSLaneStatsEntry.setStatus("current")


class _IfPCSLaneIndex_Type(Unsigned32):
    """Custom type ifPCSLaneIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IfPCSLaneIndex_Type.__name__ = "Unsigned32"
_IfPCSLaneIndex_Object = MibTableColumn
ifPCSLaneIndex = _IfPCSLaneIndex_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 2, 3, 1, 1),
    _IfPCSLaneIndex_Type()
)
ifPCSLaneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifPCSLaneIndex.setStatus("current")
_IfMauPPLFECCorrectedBlocks_Type = Counter64
_IfMauPPLFECCorrectedBlocks_Object = MibTableColumn
ifMauPPLFECCorrectedBlocks = _IfMauPPLFECCorrectedBlocks_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 2, 3, 1, 2),
    _IfMauPPLFECCorrectedBlocks_Type()
)
ifMauPPLFECCorrectedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauPPLFECCorrectedBlocks.setStatus("current")
_IfMauPPLFECUncorrectableBlocks_Type = Counter64
_IfMauPPLFECUncorrectableBlocks_Object = MibTableColumn
ifMauPPLFECUncorrectableBlocks = _IfMauPPLFECUncorrectableBlocks_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 2, 3, 1, 3),
    _IfMauPPLFECUncorrectableBlocks_Type()
)
ifMauPPLFECUncorrectableBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauPPLFECUncorrectableBlocks.setStatus("current")
_IfMauBIPErrorCount_Type = Counter32
_IfMauBIPErrorCount_Object = MibTableColumn
ifMauBIPErrorCount = _IfMauBIPErrorCount_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 2, 3, 1, 4),
    _IfMauBIPErrorCount_Type()
)
ifMauBIPErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauBIPErrorCount.setStatus("current")
_IfMauPCStoPHYLaneMapping_Type = Unsigned32
_IfMauPCStoPHYLaneMapping_Object = MibTableColumn
ifMauPCStoPHYLaneMapping = _IfMauPCStoPHYLaneMapping_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 2, 3, 1, 5),
    _IfMauPCStoPHYLaneMapping_Type()
)
ifMauPCStoPHYLaneMapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauPCStoPHYLaneMapping.setStatus("current")
_Dot3PlaceholderGroup_ObjectIdentity = ObjectIdentity
dot3PlaceholderGroup = _Dot3PlaceholderGroup_ObjectIdentity(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 3)
)


class _Dot3Placeholder_Type(Integer32):
    """Custom type dot3Placeholder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("placeholder", 1)
    )


_Dot3Placeholder_Type.__name__ = "Integer32"
_Dot3Placeholder_Object = MibScalar
dot3Placeholder = _Dot3Placeholder_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 3, 1),
    _Dot3Placeholder_Type()
)
dot3Placeholder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3Placeholder.setStatus("current")
_Dot3IfMauAutoNegGroup_ObjectIdentity = ObjectIdentity
dot3IfMauAutoNegGroup = _Dot3IfMauAutoNegGroup_ObjectIdentity(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 5)
)
_IfMauAutoNegTable_Object = MibTable
ifMauAutoNegTable = _IfMauAutoNegTable_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ifMauAutoNegTable.setStatus("current")
_IfMauAutoNegEntry_Object = MibTableRow
ifMauAutoNegEntry = _IfMauAutoNegEntry_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 5, 1, 1)
)
ifMauAutoNegEntry.setIndexNames(
    (0, "IEEE8023-MAU-MIB", "ifMauIfIndex"),
    (0, "IEEE8023-MAU-MIB", "ifMauIndex"),
)
if mibBuilder.loadTexts:
    ifMauAutoNegEntry.setStatus("current")


class _IfMauAutoNegAdminStatus_Type(Integer32):
    """Custom type ifMauAutoNegAdminStatus based on Integer32"""
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


_IfMauAutoNegAdminStatus_Type.__name__ = "Integer32"
_IfMauAutoNegAdminStatus_Object = MibTableColumn
ifMauAutoNegAdminStatus = _IfMauAutoNegAdminStatus_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 5, 1, 1, 1),
    _IfMauAutoNegAdminStatus_Type()
)
ifMauAutoNegAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifMauAutoNegAdminStatus.setStatus("current")


class _IfMauAutoNegRemoteSignaling_Type(Integer32):
    """Custom type ifMauAutoNegRemoteSignaling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("detected", 1),
          ("notdetected", 2))
    )


_IfMauAutoNegRemoteSignaling_Type.__name__ = "Integer32"
_IfMauAutoNegRemoteSignaling_Object = MibTableColumn
ifMauAutoNegRemoteSignaling = _IfMauAutoNegRemoteSignaling_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 5, 1, 1, 2),
    _IfMauAutoNegRemoteSignaling_Type()
)
ifMauAutoNegRemoteSignaling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauAutoNegRemoteSignaling.setStatus("current")


class _IfMauAutoNegConfig_Type(Integer32):
    """Custom type ifMauAutoNegConfig based on Integer32"""
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
        *(("other", 1),
          ("configuring", 2),
          ("complete", 3),
          ("disabled", 4),
          ("parallelDetectFail", 5))
    )


_IfMauAutoNegConfig_Type.__name__ = "Integer32"
_IfMauAutoNegConfig_Object = MibTableColumn
ifMauAutoNegConfig = _IfMauAutoNegConfig_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 5, 1, 1, 4),
    _IfMauAutoNegConfig_Type()
)
ifMauAutoNegConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauAutoNegConfig.setStatus("current")


class _IfMauAutoNegRestart_Type(Integer32):
    """Custom type ifMauAutoNegRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("restart", 1),
          ("norestart", 2))
    )


_IfMauAutoNegRestart_Type.__name__ = "Integer32"
_IfMauAutoNegRestart_Object = MibTableColumn
ifMauAutoNegRestart = _IfMauAutoNegRestart_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 5, 1, 1, 5),
    _IfMauAutoNegRestart_Type()
)
ifMauAutoNegRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifMauAutoNegRestart.setStatus("current")
_IfMauAutoNegCapabilityBits_Type = IANAifMauAutoNegCapBits
_IfMauAutoNegCapabilityBits_Object = MibTableColumn
ifMauAutoNegCapabilityBits = _IfMauAutoNegCapabilityBits_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 5, 1, 1, 6),
    _IfMauAutoNegCapabilityBits_Type()
)
ifMauAutoNegCapabilityBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauAutoNegCapabilityBits.setStatus("current")
_IfMauAutoNegCapAdvertisedBits_Type = IANAifMauAutoNegCapBits
_IfMauAutoNegCapAdvertisedBits_Object = MibTableColumn
ifMauAutoNegCapAdvertisedBits = _IfMauAutoNegCapAdvertisedBits_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 5, 1, 1, 7),
    _IfMauAutoNegCapAdvertisedBits_Type()
)
ifMauAutoNegCapAdvertisedBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifMauAutoNegCapAdvertisedBits.setStatus("current")
_IfMauAutoNegCapReceivedBits_Type = IANAifMauAutoNegCapBits
_IfMauAutoNegCapReceivedBits_Object = MibTableColumn
ifMauAutoNegCapReceivedBits = _IfMauAutoNegCapReceivedBits_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 5, 1, 1, 8),
    _IfMauAutoNegCapReceivedBits_Type()
)
ifMauAutoNegCapReceivedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauAutoNegCapReceivedBits.setStatus("current")


class _IfMauAutoNegRemoteFaultAdvertised_Type(Integer32):
    """Custom type ifMauAutoNegRemoteFaultAdvertised based on Integer32"""
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
        *(("noError", 1),
          ("offline", 2),
          ("linkFailure", 3),
          ("autoNegError", 4))
    )


_IfMauAutoNegRemoteFaultAdvertised_Type.__name__ = "Integer32"
_IfMauAutoNegRemoteFaultAdvertised_Object = MibTableColumn
ifMauAutoNegRemoteFaultAdvertised = _IfMauAutoNegRemoteFaultAdvertised_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 5, 1, 1, 9),
    _IfMauAutoNegRemoteFaultAdvertised_Type()
)
ifMauAutoNegRemoteFaultAdvertised.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifMauAutoNegRemoteFaultAdvertised.setStatus("current")


class _IfMauAutoNegRemoteFaultReceived_Type(Integer32):
    """Custom type ifMauAutoNegRemoteFaultReceived based on Integer32"""
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
        *(("noError", 1),
          ("offline", 2),
          ("linkFailure", 3),
          ("autoNegError", 4))
    )


_IfMauAutoNegRemoteFaultReceived_Type.__name__ = "Integer32"
_IfMauAutoNegRemoteFaultReceived_Object = MibTableColumn
ifMauAutoNegRemoteFaultReceived = _IfMauAutoNegRemoteFaultReceived_Object(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 5, 1, 1, 10),
    _IfMauAutoNegRemoteFaultReceived_Type()
)
ifMauAutoNegRemoteFaultReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauAutoNegRemoteFaultReceived.setStatus("current")
_MauModConf_ObjectIdentity = ObjectIdentity
mauModConf = _MauModConf_ObjectIdentity(
    (1, 3, 111, 2, 802, 3, 1, 13, 2)
)
_MauModCompls_ObjectIdentity = ObjectIdentity
mauModCompls = _MauModCompls_ObjectIdentity(
    (1, 3, 111, 2, 802, 3, 1, 13, 2, 1)
)
_MauModObjGrps_ObjectIdentity = ObjectIdentity
mauModObjGrps = _MauModObjGrps_ObjectIdentity(
    (1, 3, 111, 2, 802, 3, 1, 13, 2, 2)
)
_MauModNotGrps_ObjectIdentity = ObjectIdentity
mauModNotGrps = _MauModNotGrps_ObjectIdentity(
    (1, 3, 111, 2, 802, 3, 1, 13, 2, 3)
)

# Managed Objects groups

mauRpGrpBasic = ObjectGroup(
    (1, 3, 111, 2, 802, 3, 1, 13, 2, 2, 1)
)
mauRpGrpBasic.setObjects(
      *(("IEEE8023-MAU-MIB", "rpMauType"),
        ("IEEE8023-MAU-MIB", "rpMauStatus"),
        ("IEEE8023-MAU-MIB", "rpMauMediaAvailable"),
        ("IEEE8023-MAU-MIB", "rpMauMediaAvailableStateExits"),
        ("IEEE8023-MAU-MIB", "rpMauJabberState"),
        ("IEEE8023-MAU-MIB", "rpMauJabberingStateEnters"))
)
if mibBuilder.loadTexts:
    mauRpGrpBasic.setStatus("current")

mauRpGrp100Mbs = ObjectGroup(
    (1, 3, 111, 2, 802, 3, 1, 13, 2, 2, 2)
)
mauRpGrp100Mbs.setObjects(
    ("IEEE8023-MAU-MIB", "rpMauFalseCarriers")
)
if mibBuilder.loadTexts:
    mauRpGrp100Mbs.setStatus("current")

mauRpGrpJack = ObjectGroup(
    (1, 3, 111, 2, 802, 3, 1, 13, 2, 2, 3)
)
mauRpGrpJack.setObjects(
    ("IEEE8023-MAU-MIB", "rpJackType")
)
if mibBuilder.loadTexts:
    mauRpGrpJack.setStatus("current")

mauIfGrpBasic = ObjectGroup(
    (1, 3, 111, 2, 802, 3, 1, 13, 2, 2, 4)
)
mauIfGrpBasic.setObjects(
      *(("IEEE8023-MAU-MIB", "ifMauType"),
        ("IEEE8023-MAU-MIB", "ifMauStatus"),
        ("IEEE8023-MAU-MIB", "ifMauMediaAvailable"),
        ("IEEE8023-MAU-MIB", "ifMauMediaAvailableStateExits"),
        ("IEEE8023-MAU-MIB", "ifMauJabberState"),
        ("IEEE8023-MAU-MIB", "ifMauJabberingStateEnters"),
        ("IEEE8023-MAU-MIB", "dot3Placeholder"))
)
if mibBuilder.loadTexts:
    mauIfGrpBasic.setStatus("current")

mauIfGrpJack = ObjectGroup(
    (1, 3, 111, 2, 802, 3, 1, 13, 2, 2, 5)
)
mauIfGrpJack.setObjects(
    ("IEEE8023-MAU-MIB", "ifJackType")
)
if mibBuilder.loadTexts:
    mauIfGrpJack.setStatus("current")

mauIfGrpHighCapacity = ObjectGroup(
    (1, 3, 111, 2, 802, 3, 1, 13, 2, 2, 6)
)
mauIfGrpHighCapacity.setObjects(
      *(("IEEE8023-MAU-MIB", "ifMauFalseCarriers"),
        ("IEEE8023-MAU-MIB", "ifMauTypeListBits"),
        ("IEEE8023-MAU-MIB", "ifMauDefaultType"),
        ("IEEE8023-MAU-MIB", "ifMauAutoNegSupported"))
)
if mibBuilder.loadTexts:
    mauIfGrpHighCapacity.setStatus("current")

mauIfGrpAutoNeg2 = ObjectGroup(
    (1, 3, 111, 2, 802, 3, 1, 13, 2, 2, 7)
)
mauIfGrpAutoNeg2.setObjects(
      *(("IEEE8023-MAU-MIB", "ifMauAutoNegAdminStatus"),
        ("IEEE8023-MAU-MIB", "ifMauAutoNegRemoteSignaling"),
        ("IEEE8023-MAU-MIB", "ifMauAutoNegConfig"),
        ("IEEE8023-MAU-MIB", "ifMauAutoNegCapabilityBits"),
        ("IEEE8023-MAU-MIB", "ifMauAutoNegCapAdvertisedBits"),
        ("IEEE8023-MAU-MIB", "ifMauAutoNegCapReceivedBits"),
        ("IEEE8023-MAU-MIB", "ifMauAutoNegRestart"))
)
if mibBuilder.loadTexts:
    mauIfGrpAutoNeg2.setStatus("current")

mauIfGrpAutoNeg1000Mbps = ObjectGroup(
    (1, 3, 111, 2, 802, 3, 1, 13, 2, 2, 8)
)
mauIfGrpAutoNeg1000Mbps.setObjects(
      *(("IEEE8023-MAU-MIB", "ifMauAutoNegRemoteFaultAdvertised"),
        ("IEEE8023-MAU-MIB", "ifMauAutoNegRemoteFaultReceived"))
)
if mibBuilder.loadTexts:
    mauIfGrpAutoNeg1000Mbps.setStatus("current")

mauIfGrpHCStats = ObjectGroup(
    (1, 3, 111, 2, 802, 3, 1, 13, 2, 2, 9)
)
mauIfGrpHCStats.setObjects(
      *(("IEEE8023-MAU-MIB", "ifMauHCFalseCarriers"),
        ("IEEE8023-MAU-MIB", "ifMauPCSCodingViolations"))
)
if mibBuilder.loadTexts:
    mauIfGrpHCStats.setStatus("current")

mauIfGrpFEC = ObjectGroup(
    (1, 3, 111, 2, 802, 3, 1, 13, 2, 2, 10)
)
mauIfGrpFEC.setObjects(
      *(("IEEE8023-MAU-MIB", "ifMauFECAbility"),
        ("IEEE8023-MAU-MIB", "ifMauFECMode"),
        ("IEEE8023-MAU-MIB", "ifMauFECCorrectedBlocks"),
        ("IEEE8023-MAU-MIB", "ifMauFECUnCorrectableBlocks"))
)
if mibBuilder.loadTexts:
    mauIfGrpFEC.setStatus("current")

mauIfGrpSNR = ObjectGroup(
    (1, 3, 111, 2, 802, 3, 1, 13, 2, 2, 11)
)
mauIfGrpSNR.setObjects(
      *(("IEEE8023-MAU-MIB", "ifMauSNROpMarginChnlA"),
        ("IEEE8023-MAU-MIB", "ifMauSNROpMarginChnlB"),
        ("IEEE8023-MAU-MIB", "ifMauSNROpMarginChnlC"),
        ("IEEE8023-MAU-MIB", "ifMauSNROpMarginChnlD"))
)
if mibBuilder.loadTexts:
    mauIfGrpSNR.setStatus("current")

mauIfGrpEEE = ObjectGroup(
    (1, 3, 111, 2, 802, 3, 1, 13, 2, 2, 12)
)
mauIfGrpEEE.setObjects(
      *(("IEEE8023-MAU-MIB", "ifMauEEESupportList"),
        ("IEEE8023-MAU-MIB", "ifMauEEELDFastRetrainCount"),
        ("IEEE8023-MAU-MIB", "ifMauEEELPFastRetrainCount"))
)
if mibBuilder.loadTexts:
    mauIfGrpEEE.setStatus("current")

mauIfGrpTimeSync = ObjectGroup(
    (1, 3, 111, 2, 802, 3, 1, 13, 2, 2, 13)
)
mauIfGrpTimeSync.setObjects(
      *(("IEEE8023-MAU-MIB", "ifMauTimeSyncCapabilityTX"),
        ("IEEE8023-MAU-MIB", "ifMauTimeSyncCapabilityRX"),
        ("IEEE8023-MAU-MIB", "ifMauTimeSyncDelayTXmax"),
        ("IEEE8023-MAU-MIB", "ifMauTimeSyncDelayTXmin"),
        ("IEEE8023-MAU-MIB", "ifMauTimeSyncDelayRXmax"),
        ("IEEE8023-MAU-MIB", "ifMauTimeSyncDelayRXmin"))
)
if mibBuilder.loadTexts:
    mauIfGrpTimeSync.setStatus("current")

mauIfGrpPerPCSLaneStats = ObjectGroup(
    (1, 3, 111, 2, 802, 3, 1, 13, 2, 2, 14)
)
mauIfGrpPerPCSLaneStats.setObjects(
      *(("IEEE8023-MAU-MIB", "ifMauPPLFECCorrectedBlocks"),
        ("IEEE8023-MAU-MIB", "ifMauPPLFECUncorrectableBlocks"),
        ("IEEE8023-MAU-MIB", "ifMauBIPErrorCount"),
        ("IEEE8023-MAU-MIB", "ifMauPCStoPHYLaneMapping"))
)
if mibBuilder.loadTexts:
    mauIfGrpPerPCSLaneStats.setStatus("current")


# Notification objects

rpMauJabberTrap = NotificationType(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 0, 1)
)
rpMauJabberTrap.setObjects(
    ("IEEE8023-MAU-MIB", "rpMauJabberState")
)
if mibBuilder.loadTexts:
    rpMauJabberTrap.setStatus(
        "current"
    )

ifMauJabberTrap = NotificationType(
    (1, 3, 111, 2, 802, 3, 1, 13, 1, 0, 2)
)
ifMauJabberTrap.setObjects(
    ("IEEE8023-MAU-MIB", "ifMauJabberState")
)
if mibBuilder.loadTexts:
    ifMauJabberTrap.setStatus(
        "current"
    )


# Notifications groups

rpMauNotifications = NotificationGroup(
    (1, 3, 111, 2, 802, 3, 1, 13, 2, 3, 1)
)
rpMauNotifications.setObjects(
    ("IEEE8023-MAU-MIB", "rpMauJabberTrap")
)
if mibBuilder.loadTexts:
    rpMauNotifications.setStatus(
        "current"
    )

ifMauNotifications = NotificationGroup(
    (1, 3, 111, 2, 802, 3, 1, 13, 2, 3, 2)
)
ifMauNotifications.setObjects(
    ("IEEE8023-MAU-MIB", "ifMauJabberTrap")
)
if mibBuilder.loadTexts:
    ifMauNotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

mauModRpCompl2 = ModuleCompliance(
    (1, 3, 111, 2, 802, 3, 1, 13, 2, 1, 1)
)
mauModRpCompl2.setObjects(
      *(("IEEE8023-MAU-MIB", "mauRpGrpBasic"),
        ("IEEE8023-MAU-MIB", "mauRpGrp100Mbs"),
        ("IEEE8023-MAU-MIB", "mauRpGrpJack"),
        ("IEEE8023-MAU-MIB", "rpMauNotifications"))
)
if mibBuilder.loadTexts:
    mauModRpCompl2.setStatus(
        "current"
    )

mauModIfCompl3 = ModuleCompliance(
    (1, 3, 111, 2, 802, 3, 1, 13, 2, 1, 2)
)
mauModIfCompl3.setObjects(
      *(("IEEE8023-MAU-MIB", "mauIfGrpBasic"),
        ("IEEE8023-MAU-MIB", "mauIfGrpHighCapacity"),
        ("IEEE8023-MAU-MIB", "mauIfGrpHCStats"),
        ("IEEE8023-MAU-MIB", "mauIfGrpJack"),
        ("IEEE8023-MAU-MIB", "mauIfGrpAutoNeg2"),
        ("IEEE8023-MAU-MIB", "mauIfGrpAutoNeg1000Mbps"),
        ("IEEE8023-MAU-MIB", "ifMauNotifications"),
        ("IEEE8023-MAU-MIB", "mauIfGrpFEC"),
        ("IEEE8023-MAU-MIB", "mauIfGrpSNR"),
        ("IEEE8023-MAU-MIB", "mauIfGrpEEE"),
        ("IEEE8023-MAU-MIB", "mauIfGrpTimeSync"),
        ("IEEE8023-MAU-MIB", "mauIfGrpPerPCSLaneStats"))
)
if mibBuilder.loadTexts:
    mauModIfCompl3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE8023-MAU-MIB",
    **{"ieee8023mauMIB": ieee8023mauMIB,
       "ieee8023snmpDot3MauMgt": ieee8023snmpDot3MauMgt,
       "snmpDot3MauTraps": snmpDot3MauTraps,
       "rpMauJabberTrap": rpMauJabberTrap,
       "ifMauJabberTrap": ifMauJabberTrap,
       "dot3RpMauBasicGroup": dot3RpMauBasicGroup,
       "rpMauTable": rpMauTable,
       "rpMauEntry": rpMauEntry,
       "rpMauGroupIndex": rpMauGroupIndex,
       "rpMauPortIndex": rpMauPortIndex,
       "rpMauIndex": rpMauIndex,
       "rpMauType": rpMauType,
       "rpMauStatus": rpMauStatus,
       "rpMauMediaAvailable": rpMauMediaAvailable,
       "rpMauMediaAvailableStateExits": rpMauMediaAvailableStateExits,
       "rpMauJabberState": rpMauJabberState,
       "rpMauJabberingStateEnters": rpMauJabberingStateEnters,
       "rpMauFalseCarriers": rpMauFalseCarriers,
       "rpJackTable": rpJackTable,
       "rpJackEntry": rpJackEntry,
       "rpJackIndex": rpJackIndex,
       "rpJackType": rpJackType,
       "dot3IfMauBasicGroup": dot3IfMauBasicGroup,
       "ifMauTable": ifMauTable,
       "ifMauEntry": ifMauEntry,
       "ifMauIfIndex": ifMauIfIndex,
       "ifMauIndex": ifMauIndex,
       "ifMauType": ifMauType,
       "ifMauStatus": ifMauStatus,
       "ifMauMediaAvailable": ifMauMediaAvailable,
       "ifMauMediaAvailableStateExits": ifMauMediaAvailableStateExits,
       "ifMauJabberState": ifMauJabberState,
       "ifMauJabberingStateEnters": ifMauJabberingStateEnters,
       "ifMauFalseCarriers": ifMauFalseCarriers,
       "ifMauDefaultType": ifMauDefaultType,
       "ifMauAutoNegSupported": ifMauAutoNegSupported,
       "ifMauTypeListBits": ifMauTypeListBits,
       "ifMauHCFalseCarriers": ifMauHCFalseCarriers,
       "ifMauPCSCodingViolations": ifMauPCSCodingViolations,
       "ifMauFECAbility": ifMauFECAbility,
       "ifMauFECMode": ifMauFECMode,
       "ifMauFECCorrectedBlocks": ifMauFECCorrectedBlocks,
       "ifMauFECUnCorrectableBlocks": ifMauFECUnCorrectableBlocks,
       "ifMauSNROpMarginChnlA": ifMauSNROpMarginChnlA,
       "ifMauSNROpMarginChnlB": ifMauSNROpMarginChnlB,
       "ifMauSNROpMarginChnlC": ifMauSNROpMarginChnlC,
       "ifMauSNROpMarginChnlD": ifMauSNROpMarginChnlD,
       "ifMauEEESupportList": ifMauEEESupportList,
       "ifMauEEELDFastRetrainCount": ifMauEEELDFastRetrainCount,
       "ifMauEEELPFastRetrainCount": ifMauEEELPFastRetrainCount,
       "ifMauTimeSyncCapabilityTX": ifMauTimeSyncCapabilityTX,
       "ifMauTimeSyncCapabilityRX": ifMauTimeSyncCapabilityRX,
       "ifMauTimeSyncDelayTXmax": ifMauTimeSyncDelayTXmax,
       "ifMauTimeSyncDelayTXmin": ifMauTimeSyncDelayTXmin,
       "ifMauTimeSyncDelayRXmax": ifMauTimeSyncDelayRXmax,
       "ifMauTimeSyncDelayRXmin": ifMauTimeSyncDelayRXmin,
       "ifJackTable": ifJackTable,
       "ifJackEntry": ifJackEntry,
       "ifJackIndex": ifJackIndex,
       "ifJackType": ifJackType,
       "ifMauPerPCSLaneStatsTable": ifMauPerPCSLaneStatsTable,
       "ifMauPerPCSLaneStatsEntry": ifMauPerPCSLaneStatsEntry,
       "ifPCSLaneIndex": ifPCSLaneIndex,
       "ifMauPPLFECCorrectedBlocks": ifMauPPLFECCorrectedBlocks,
       "ifMauPPLFECUncorrectableBlocks": ifMauPPLFECUncorrectableBlocks,
       "ifMauBIPErrorCount": ifMauBIPErrorCount,
       "ifMauPCStoPHYLaneMapping": ifMauPCStoPHYLaneMapping,
       "dot3PlaceholderGroup": dot3PlaceholderGroup,
       "dot3Placeholder": dot3Placeholder,
       "dot3IfMauAutoNegGroup": dot3IfMauAutoNegGroup,
       "ifMauAutoNegTable": ifMauAutoNegTable,
       "ifMauAutoNegEntry": ifMauAutoNegEntry,
       "ifMauAutoNegAdminStatus": ifMauAutoNegAdminStatus,
       "ifMauAutoNegRemoteSignaling": ifMauAutoNegRemoteSignaling,
       "ifMauAutoNegConfig": ifMauAutoNegConfig,
       "ifMauAutoNegRestart": ifMauAutoNegRestart,
       "ifMauAutoNegCapabilityBits": ifMauAutoNegCapabilityBits,
       "ifMauAutoNegCapAdvertisedBits": ifMauAutoNegCapAdvertisedBits,
       "ifMauAutoNegCapReceivedBits": ifMauAutoNegCapReceivedBits,
       "ifMauAutoNegRemoteFaultAdvertised": ifMauAutoNegRemoteFaultAdvertised,
       "ifMauAutoNegRemoteFaultReceived": ifMauAutoNegRemoteFaultReceived,
       "mauModConf": mauModConf,
       "mauModCompls": mauModCompls,
       "mauModRpCompl2": mauModRpCompl2,
       "mauModIfCompl3": mauModIfCompl3,
       "mauModObjGrps": mauModObjGrps,
       "mauRpGrpBasic": mauRpGrpBasic,
       "mauRpGrp100Mbs": mauRpGrp100Mbs,
       "mauRpGrpJack": mauRpGrpJack,
       "mauIfGrpBasic": mauIfGrpBasic,
       "mauIfGrpJack": mauIfGrpJack,
       "mauIfGrpHighCapacity": mauIfGrpHighCapacity,
       "mauIfGrpAutoNeg2": mauIfGrpAutoNeg2,
       "mauIfGrpAutoNeg1000Mbps": mauIfGrpAutoNeg1000Mbps,
       "mauIfGrpHCStats": mauIfGrpHCStats,
       "mauIfGrpFEC": mauIfGrpFEC,
       "mauIfGrpSNR": mauIfGrpSNR,
       "mauIfGrpEEE": mauIfGrpEEE,
       "mauIfGrpTimeSync": mauIfGrpTimeSync,
       "mauIfGrpPerPCSLaneStats": mauIfGrpPerPCSLaneStats,
       "mauModNotGrps": mauModNotGrps,
       "rpMauNotifications": rpMauNotifications,
       "ifMauNotifications": ifMauNotifications}
)
