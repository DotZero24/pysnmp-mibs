# SNMP MIB module (SUPERMICRO-OSPFMI-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-OSPFMI-TRAP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:02:20 2025
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

(fsMIStdOspfEntry,
 fsMIStdOspfExtLsdbLimit,
 fsMIStdOspfIfState,
 fsMIStdOspfNbrRtrId,
 fsMIStdOspfNbrState,
 fsMIStdOspfRouterId,
 fsMIStdOspfVirtIfState,
 fsMIStdOspfVirtNbrState) = mibBuilder.importSymbols(
    "SUPERMICRO-MISTDOSPF-MIB",
    "fsMIStdOspfEntry",
    "fsMIStdOspfExtLsdbLimit",
    "fsMIStdOspfIfState",
    "fsMIStdOspfNbrRtrId",
    "fsMIStdOspfNbrState",
    "fsMIStdOspfRouterId",
    "fsMIStdOspfVirtIfState",
    "fsMIStdOspfVirtNbrState")


# MODULE-IDENTITY

fsMIStdOspfTrap = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 148)
)
if mibBuilder.loadTexts:
    fsMIStdOspfTrap.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsMIStdOspfTraps_ObjectIdentity = ObjectIdentity
fsMIStdOspfTraps = _FsMIStdOspfTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 148, 0)
)
_FsMIStdOspfTrapControl_ObjectIdentity = ObjectIdentity
fsMIStdOspfTrapControl = _FsMIStdOspfTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 148, 1)
)
_FsMIStdOspfTrapTable_Object = MibTable
fsMIStdOspfTrapTable = _FsMIStdOspfTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 148, 1, 1)
)
if mibBuilder.loadTexts:
    fsMIStdOspfTrapTable.setStatus("current")
_FsMIStdOspfTrapEntry_Object = MibTableRow
fsMIStdOspfTrapEntry = _FsMIStdOspfTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 148, 1, 1, 1)
)
if mibBuilder.loadTexts:
    fsMIStdOspfTrapEntry.setStatus("current")


class _FsMIStdOspfSetTrap_Type(OctetString):
    """Custom type fsMIStdOspfSetTrap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_FsMIStdOspfSetTrap_Type.__name__ = "OctetString"
_FsMIStdOspfSetTrap_Object = MibTableColumn
fsMIStdOspfSetTrap = _FsMIStdOspfSetTrap_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 148, 1, 1, 1, 1),
    _FsMIStdOspfSetTrap_Type()
)
fsMIStdOspfSetTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIStdOspfSetTrap.setStatus("current")


class _FsMIStdOspfConfigErrorType_Type(Integer32):
    """Custom type fsMIStdOspfConfigErrorType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("badVersion", 1),
          ("areaMismatch", 2),
          ("unknownNbmaNbr", 3),
          ("unknownVirtualNbr", 4),
          ("authTypeMismatch", 5),
          ("authFailure", 6),
          ("netMaskMismatch", 7),
          ("helloIntervalMismatch", 8),
          ("deadIntervalMismatch", 9),
          ("optionMismatch", 10))
    )


_FsMIStdOspfConfigErrorType_Type.__name__ = "Integer32"
_FsMIStdOspfConfigErrorType_Object = MibTableColumn
fsMIStdOspfConfigErrorType = _FsMIStdOspfConfigErrorType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 148, 1, 1, 1, 2),
    _FsMIStdOspfConfigErrorType_Type()
)
fsMIStdOspfConfigErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdOspfConfigErrorType.setStatus("current")


class _FsMIStdOspfPacketType_Type(Integer32):
    """Custom type fsMIStdOspfPacketType based on Integer32"""
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
        *(("hello", 1),
          ("dbDescript", 2),
          ("lsReq", 3),
          ("lsUpdate", 4),
          ("lsAck", 5))
    )


_FsMIStdOspfPacketType_Type.__name__ = "Integer32"
_FsMIStdOspfPacketType_Object = MibTableColumn
fsMIStdOspfPacketType = _FsMIStdOspfPacketType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 148, 1, 1, 1, 3),
    _FsMIStdOspfPacketType_Type()
)
fsMIStdOspfPacketType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdOspfPacketType.setStatus("current")
_FsMIStdOspfPacketSrc_Type = IpAddress
_FsMIStdOspfPacketSrc_Object = MibTableColumn
fsMIStdOspfPacketSrc = _FsMIStdOspfPacketSrc_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 148, 1, 1, 1, 4),
    _FsMIStdOspfPacketSrc_Type()
)
fsMIStdOspfPacketSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdOspfPacketSrc.setStatus("current")
fsMIStdOspfEntry.registerAugmentions(
    ("SUPERMICRO-OSPFMI-TRAP-MIB",
     "fsMIStdOspfTrapEntry")
)
fsMIStdOspfTrapEntry.setIndexNames(*fsMIStdOspfEntry.getIndexNames())

# Managed Objects groups


# Notification objects

ospfVirtIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 148, 0, 1)
)
ospfVirtIfStateChange.setObjects(
      *(("SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfRouterId"),
        ("SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfVirtIfState"))
)
if mibBuilder.loadTexts:
    ospfVirtIfStateChange.setStatus(
        "current"
    )

ospfNbrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 148, 0, 2)
)
ospfNbrStateChange.setObjects(
      *(("SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfRouterId"),
        ("SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfNbrRtrId"),
        ("SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfNbrState"))
)
if mibBuilder.loadTexts:
    ospfNbrStateChange.setStatus(
        "current"
    )

ospfVirtNbrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 148, 0, 3)
)
ospfVirtNbrStateChange.setObjects(
      *(("SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfRouterId"),
        ("SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfVirtNbrState"))
)
if mibBuilder.loadTexts:
    ospfVirtNbrStateChange.setStatus(
        "current"
    )

ospfIfConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 148, 0, 4)
)
ospfIfConfigError.setObjects(
      *(("SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfRouterId"),
        ("SUPERMICRO-OSPFMI-TRAP-MIB", "fsMIStdOspfPacketSrc"),
        ("SUPERMICRO-OSPFMI-TRAP-MIB", "fsMIStdOspfConfigErrorType"),
        ("SUPERMICRO-OSPFMI-TRAP-MIB", "fsMIStdOspfPacketType"))
)
if mibBuilder.loadTexts:
    ospfIfConfigError.setStatus(
        "current"
    )

ospfVirtIfConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 148, 0, 5)
)
ospfVirtIfConfigError.setObjects(
      *(("SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfRouterId"),
        ("SUPERMICRO-OSPFMI-TRAP-MIB", "fsMIStdOspfConfigErrorType"),
        ("SUPERMICRO-OSPFMI-TRAP-MIB", "fsMIStdOspfPacketType"))
)
if mibBuilder.loadTexts:
    ospfVirtIfConfigError.setStatus(
        "current"
    )

ospfIfAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 148, 0, 6)
)
ospfIfAuthFailure.setObjects(
      *(("SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfRouterId"),
        ("SUPERMICRO-OSPFMI-TRAP-MIB", "fsMIStdOspfPacketSrc"),
        ("SUPERMICRO-OSPFMI-TRAP-MIB", "fsMIStdOspfConfigErrorType"),
        ("SUPERMICRO-OSPFMI-TRAP-MIB", "fsMIStdOspfPacketType"))
)
if mibBuilder.loadTexts:
    ospfIfAuthFailure.setStatus(
        "current"
    )

ospfVirtIfAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 148, 0, 7)
)
ospfVirtIfAuthFailure.setObjects(
      *(("SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfRouterId"),
        ("SUPERMICRO-OSPFMI-TRAP-MIB", "fsMIStdOspfConfigErrorType"),
        ("SUPERMICRO-OSPFMI-TRAP-MIB", "fsMIStdOspfPacketType"))
)
if mibBuilder.loadTexts:
    ospfVirtIfAuthFailure.setStatus(
        "current"
    )

ospfIfRxBadPacket = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 148, 0, 8)
)
ospfIfRxBadPacket.setObjects(
      *(("SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfRouterId"),
        ("SUPERMICRO-OSPFMI-TRAP-MIB", "fsMIStdOspfPacketSrc"),
        ("SUPERMICRO-OSPFMI-TRAP-MIB", "fsMIStdOspfPacketType"))
)
if mibBuilder.loadTexts:
    ospfIfRxBadPacket.setStatus(
        "current"
    )

ospfVirtIfRxBadPacket = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 148, 0, 9)
)
ospfVirtIfRxBadPacket.setObjects(
      *(("SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfRouterId"),
        ("SUPERMICRO-OSPFMI-TRAP-MIB", "fsMIStdOspfPacketType"))
)
if mibBuilder.loadTexts:
    ospfVirtIfRxBadPacket.setStatus(
        "current"
    )

ospfTxRetransmit = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 148, 0, 10)
)
ospfTxRetransmit.setObjects(
      *(("SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfRouterId"),
        ("SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfNbrRtrId"),
        ("SUPERMICRO-OSPFMI-TRAP-MIB", "fsMIStdOspfPacketType"))
)
if mibBuilder.loadTexts:
    ospfTxRetransmit.setStatus(
        "current"
    )

ospfVirtIfTxRetransmit = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 148, 0, 11)
)
ospfVirtIfTxRetransmit.setObjects(
      *(("SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfRouterId"),
        ("SUPERMICRO-OSPFMI-TRAP-MIB", "fsMIStdOspfPacketType"))
)
if mibBuilder.loadTexts:
    ospfVirtIfTxRetransmit.setStatus(
        "current"
    )

ospfOriginateLsa = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 148, 0, 12)
)
ospfOriginateLsa.setObjects(
    ("SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfRouterId")
)
if mibBuilder.loadTexts:
    ospfOriginateLsa.setStatus(
        "current"
    )

ospfMaxAgeLsa = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 148, 0, 13)
)
ospfMaxAgeLsa.setObjects(
    ("SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfRouterId")
)
if mibBuilder.loadTexts:
    ospfMaxAgeLsa.setStatus(
        "current"
    )

ospfLsdbOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 148, 0, 14)
)
ospfLsdbOverflow.setObjects(
      *(("SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfRouterId"),
        ("SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfExtLsdbLimit"))
)
if mibBuilder.loadTexts:
    ospfLsdbOverflow.setStatus(
        "current"
    )

ospfLsdbApproachingOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 148, 0, 15)
)
ospfLsdbApproachingOverflow.setObjects(
      *(("SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfRouterId"),
        ("SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfExtLsdbLimit"))
)
if mibBuilder.loadTexts:
    ospfLsdbApproachingOverflow.setStatus(
        "current"
    )

ospfIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 148, 0, 16)
)
ospfIfStateChange.setObjects(
      *(("SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfRouterId"),
        ("SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfIfState"))
)
if mibBuilder.loadTexts:
    ospfIfStateChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-OSPFMI-TRAP-MIB",
    **{"fsMIStdOspfTrap": fsMIStdOspfTrap,
       "fsMIStdOspfTraps": fsMIStdOspfTraps,
       "ospfVirtIfStateChange": ospfVirtIfStateChange,
       "ospfNbrStateChange": ospfNbrStateChange,
       "ospfVirtNbrStateChange": ospfVirtNbrStateChange,
       "ospfIfConfigError": ospfIfConfigError,
       "ospfVirtIfConfigError": ospfVirtIfConfigError,
       "ospfIfAuthFailure": ospfIfAuthFailure,
       "ospfVirtIfAuthFailure": ospfVirtIfAuthFailure,
       "ospfIfRxBadPacket": ospfIfRxBadPacket,
       "ospfVirtIfRxBadPacket": ospfVirtIfRxBadPacket,
       "ospfTxRetransmit": ospfTxRetransmit,
       "ospfVirtIfTxRetransmit": ospfVirtIfTxRetransmit,
       "ospfOriginateLsa": ospfOriginateLsa,
       "ospfMaxAgeLsa": ospfMaxAgeLsa,
       "ospfLsdbOverflow": ospfLsdbOverflow,
       "ospfLsdbApproachingOverflow": ospfLsdbApproachingOverflow,
       "ospfIfStateChange": ospfIfStateChange,
       "fsMIStdOspfTrapControl": fsMIStdOspfTrapControl,
       "fsMIStdOspfTrapTable": fsMIStdOspfTrapTable,
       "fsMIStdOspfTrapEntry": fsMIStdOspfTrapEntry,
       "fsMIStdOspfSetTrap": fsMIStdOspfSetTrap,
       "fsMIStdOspfConfigErrorType": fsMIStdOspfConfigErrorType,
       "fsMIStdOspfPacketType": fsMIStdOspfPacketType,
       "fsMIStdOspfPacketSrc": fsMIStdOspfPacketSrc}
)
