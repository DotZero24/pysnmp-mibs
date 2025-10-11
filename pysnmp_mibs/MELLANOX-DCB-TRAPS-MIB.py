# SNMP MIB module (MELLANOX-DCB-TRAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mellanox/MELLANOX-DCB-TRAPS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:10:40 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(mellanoxDCBTraps,) = mibBuilder.importSymbols(
    "MELLANOX-SMI-MIB",
    "mellanoxDCBTraps")

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

mellanoxDCBTrapsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 8, 1)
)
if mibBuilder.loadTexts:
    mellanoxDCBTrapsMib.setRevisions(
        ("2017-07-25 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ProtocolStateType(TextualConvention, Integer32):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_MellanoxDCBTrapsMibNotifications_ObjectIdentity = ObjectIdentity
mellanoxDCBTrapsMibNotifications = _MellanoxDCBTrapsMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 8, 1, 0)
)
_MellanoxDCBTrapsMibObjects_ObjectIdentity = ObjectIdentity
mellanoxDCBTrapsMibObjects = _MellanoxDCBTrapsMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 8, 1, 1)
)
_MellanoxETSProtocolState_Type = ProtocolStateType
_MellanoxETSProtocolState_Object = MibScalar
mellanoxETSProtocolState = _MellanoxETSProtocolState_Object(
    (1, 3, 6, 1, 4, 1, 33049, 8, 1, 1, 1),
    _MellanoxETSProtocolState_Type()
)
mellanoxETSProtocolState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mellanoxETSProtocolState.setStatus("current")
_MellanoxPFCProtocolState_Type = ProtocolStateType
_MellanoxPFCProtocolState_Object = MibScalar
mellanoxPFCProtocolState = _MellanoxPFCProtocolState_Object(
    (1, 3, 6, 1, 4, 1, 33049, 8, 1, 1, 2),
    _MellanoxPFCProtocolState_Type()
)
mellanoxPFCProtocolState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mellanoxPFCProtocolState.setStatus("current")
_MellanoxDCBPortTable_Object = MibTable
mellanoxDCBPortTable = _MellanoxDCBPortTable_Object(
    (1, 3, 6, 1, 4, 1, 33049, 8, 1, 1, 3)
)
if mibBuilder.loadTexts:
    mellanoxDCBPortTable.setStatus("current")
_MellanoxDCBPortStatusEntry_Object = MibTableRow
mellanoxDCBPortStatusEntry = _MellanoxDCBPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 33049, 8, 1, 1, 3, 1)
)
mellanoxDCBPortStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mellanoxDCBPortStatusEntry.setStatus("current")
_MellanoxDCBPortETSAdminState_Type = ProtocolStateType
_MellanoxDCBPortETSAdminState_Object = MibTableColumn
mellanoxDCBPortETSAdminState = _MellanoxDCBPortETSAdminState_Object(
    (1, 3, 6, 1, 4, 1, 33049, 8, 1, 1, 3, 1, 1),
    _MellanoxDCBPortETSAdminState_Type()
)
mellanoxDCBPortETSAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxDCBPortETSAdminState.setStatus("current")
_MellanoxDCBPortETSOperState_Type = ProtocolStateType
_MellanoxDCBPortETSOperState_Object = MibTableColumn
mellanoxDCBPortETSOperState = _MellanoxDCBPortETSOperState_Object(
    (1, 3, 6, 1, 4, 1, 33049, 8, 1, 1, 3, 1, 2),
    _MellanoxDCBPortETSOperState_Type()
)
mellanoxDCBPortETSOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxDCBPortETSOperState.setStatus("current")
_MellanoxDCBPortETSPeerState_Type = ProtocolStateType
_MellanoxDCBPortETSPeerState_Object = MibTableColumn
mellanoxDCBPortETSPeerState = _MellanoxDCBPortETSPeerState_Object(
    (1, 3, 6, 1, 4, 1, 33049, 8, 1, 1, 3, 1, 3),
    _MellanoxDCBPortETSPeerState_Type()
)
mellanoxDCBPortETSPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxDCBPortETSPeerState.setStatus("current")
_MellanoxDCBPortPFCAdminState_Type = ProtocolStateType
_MellanoxDCBPortPFCAdminState_Object = MibTableColumn
mellanoxDCBPortPFCAdminState = _MellanoxDCBPortPFCAdminState_Object(
    (1, 3, 6, 1, 4, 1, 33049, 8, 1, 1, 3, 1, 4),
    _MellanoxDCBPortPFCAdminState_Type()
)
mellanoxDCBPortPFCAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxDCBPortPFCAdminState.setStatus("current")
_MellanoxDCBPortPFCOperState_Type = ProtocolStateType
_MellanoxDCBPortPFCOperState_Object = MibTableColumn
mellanoxDCBPortPFCOperState = _MellanoxDCBPortPFCOperState_Object(
    (1, 3, 6, 1, 4, 1, 33049, 8, 1, 1, 3, 1, 5),
    _MellanoxDCBPortPFCOperState_Type()
)
mellanoxDCBPortPFCOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxDCBPortPFCOperState.setStatus("current")
_MellanoxDCBPortPFCPeerState_Type = ProtocolStateType
_MellanoxDCBPortPFCPeerState_Object = MibTableColumn
mellanoxDCBPortPFCPeerState = _MellanoxDCBPortPFCPeerState_Object(
    (1, 3, 6, 1, 4, 1, 33049, 8, 1, 1, 3, 1, 6),
    _MellanoxDCBPortPFCPeerState_Type()
)
mellanoxDCBPortPFCPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxDCBPortPFCPeerState.setStatus("current")

# Managed Objects groups


# Notification objects

mellanoxETSModuleStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 33049, 8, 1, 0, 1)
)
mellanoxETSModuleStateTrap.setObjects(
    ("MELLANOX-DCB-TRAPS-MIB", "mellanoxETSProtocolState")
)
if mibBuilder.loadTexts:
    mellanoxETSModuleStateTrap.setStatus(
        "current"
    )

mellanoxETSPortAdminStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 33049, 8, 1, 0, 2)
)
mellanoxETSPortAdminStateTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("MELLANOX-DCB-TRAPS-MIB", "mellanoxDCBPortETSAdminState"))
)
if mibBuilder.loadTexts:
    mellanoxETSPortAdminStateTrap.setStatus(
        "current"
    )

mellanoxETSPortOperStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 33049, 8, 1, 0, 3)
)
mellanoxETSPortOperStateTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("MELLANOX-DCB-TRAPS-MIB", "mellanoxDCBPortETSOperState"))
)
if mibBuilder.loadTexts:
    mellanoxETSPortOperStateTrap.setStatus(
        "current"
    )

mellanoxETSPortPeerStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 33049, 8, 1, 0, 4)
)
mellanoxETSPortPeerStateTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("MELLANOX-DCB-TRAPS-MIB", "mellanoxDCBPortETSPeerState"))
)
if mibBuilder.loadTexts:
    mellanoxETSPortPeerStateTrap.setStatus(
        "current"
    )

mellanoxPFCModuleStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 33049, 8, 1, 0, 5)
)
mellanoxPFCModuleStateTrap.setObjects(
    ("MELLANOX-DCB-TRAPS-MIB", "mellanoxPFCProtocolState")
)
if mibBuilder.loadTexts:
    mellanoxPFCModuleStateTrap.setStatus(
        "current"
    )

mellanoxPFCPortAdminStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 33049, 8, 1, 0, 6)
)
mellanoxPFCPortAdminStateTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("MELLANOX-DCB-TRAPS-MIB", "mellanoxDCBPortPFCAdminState"))
)
if mibBuilder.loadTexts:
    mellanoxPFCPortAdminStateTrap.setStatus(
        "current"
    )

mellanoxPFCPortOperStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 33049, 8, 1, 0, 7)
)
mellanoxPFCPortOperStateTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("MELLANOX-DCB-TRAPS-MIB", "mellanoxDCBPortPFCOperState"))
)
if mibBuilder.loadTexts:
    mellanoxPFCPortOperStateTrap.setStatus(
        "current"
    )

mellanoxPFCPortPeerStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 33049, 8, 1, 0, 8)
)
mellanoxPFCPortPeerStateTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("MELLANOX-DCB-TRAPS-MIB", "mellanoxDCBPortPFCPeerState"))
)
if mibBuilder.loadTexts:
    mellanoxPFCPortPeerStateTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MELLANOX-DCB-TRAPS-MIB",
    **{"ProtocolStateType": ProtocolStateType,
       "mellanoxDCBTrapsMib": mellanoxDCBTrapsMib,
       "mellanoxDCBTrapsMibNotifications": mellanoxDCBTrapsMibNotifications,
       "mellanoxETSModuleStateTrap": mellanoxETSModuleStateTrap,
       "mellanoxETSPortAdminStateTrap": mellanoxETSPortAdminStateTrap,
       "mellanoxETSPortOperStateTrap": mellanoxETSPortOperStateTrap,
       "mellanoxETSPortPeerStateTrap": mellanoxETSPortPeerStateTrap,
       "mellanoxPFCModuleStateTrap": mellanoxPFCModuleStateTrap,
       "mellanoxPFCPortAdminStateTrap": mellanoxPFCPortAdminStateTrap,
       "mellanoxPFCPortOperStateTrap": mellanoxPFCPortOperStateTrap,
       "mellanoxPFCPortPeerStateTrap": mellanoxPFCPortPeerStateTrap,
       "mellanoxDCBTrapsMibObjects": mellanoxDCBTrapsMibObjects,
       "mellanoxETSProtocolState": mellanoxETSProtocolState,
       "mellanoxPFCProtocolState": mellanoxPFCProtocolState,
       "mellanoxDCBPortTable": mellanoxDCBPortTable,
       "mellanoxDCBPortStatusEntry": mellanoxDCBPortStatusEntry,
       "mellanoxDCBPortETSAdminState": mellanoxDCBPortETSAdminState,
       "mellanoxDCBPortETSOperState": mellanoxDCBPortETSOperState,
       "mellanoxDCBPortETSPeerState": mellanoxDCBPortETSPeerState,
       "mellanoxDCBPortPFCAdminState": mellanoxDCBPortPFCAdminState,
       "mellanoxDCBPortPFCOperState": mellanoxDCBPortPFCOperState,
       "mellanoxDCBPortPFCPeerState": mellanoxDCBPortPFCPeerState}
)
