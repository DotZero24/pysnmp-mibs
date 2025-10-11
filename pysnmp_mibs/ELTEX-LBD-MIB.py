# SNMP MIB module (ELTEX-LBD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-LBD-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:50:06 2025
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

(eltMes,) = mibBuilder.importSymbols(
    "ELTEX-MES",
    "eltMes")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

(VlanList1,
 VlanList2,
 VlanList3,
 VlanList4) = mibBuilder.importSymbols(
    "RADLAN-BRIDGEMIBOBJECTS-MIB",
    "VlanList1",
    "VlanList2",
    "VlanList3",
    "VlanList4")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltMesLbd_ObjectIdentity = ObjectIdentity
eltMesLbd = _EltMesLbd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 127)
)
_EltMesLbdNotif_ObjectIdentity = ObjectIdentity
eltMesLbdNotif = _EltMesLbdNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 127, 0)
)
_EltMesLbdVlanBased_Type = TruthValue
_EltMesLbdVlanBased_Object = MibScalar
eltMesLbdVlanBased = _EltMesLbdVlanBased_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 127, 1),
    _EltMesLbdVlanBased_Type()
)
eltMesLbdVlanBased.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesLbdVlanBased.setStatus("current")


class _EltMesLbdVlanBasedRecoveryTime_Type(Integer32):
    """Custom type eltMesLbdVlanBasedRecoveryTime based on Integer32"""
    defaultValue = 0


_EltMesLbdVlanBasedRecoveryTime_Type.__name__ = "Integer32"
_EltMesLbdVlanBasedRecoveryTime_Object = MibScalar
eltMesLbdVlanBasedRecoveryTime = _EltMesLbdVlanBasedRecoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 127, 2),
    _EltMesLbdVlanBasedRecoveryTime_Type()
)
eltMesLbdVlanBasedRecoveryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesLbdVlanBasedRecoveryTime.setStatus("current")
if mibBuilder.loadTexts:
    eltMesLbdVlanBasedRecoveryTime.setUnits("seconds")
_EltMesLbdVlanBasedPortTable_Object = MibTable
eltMesLbdVlanBasedPortTable = _EltMesLbdVlanBasedPortTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 127, 3)
)
if mibBuilder.loadTexts:
    eltMesLbdVlanBasedPortTable.setStatus("current")
_EltMesLbdVlanBasedPortEntry_Object = MibTableRow
eltMesLbdVlanBasedPortEntry = _EltMesLbdVlanBasedPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 127, 3, 1)
)
eltMesLbdVlanBasedPortEntry.setIndexNames(
    (0, "ELTEX-LBD-MIB", "eltMesLbdVlanBasedPort"),
)
if mibBuilder.loadTexts:
    eltMesLbdVlanBasedPortEntry.setStatus("current")
_EltMesLbdVlanBasedPort_Type = InterfaceIndex
_EltMesLbdVlanBasedPort_Object = MibTableColumn
eltMesLbdVlanBasedPort = _EltMesLbdVlanBasedPort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 127, 3, 1, 1),
    _EltMesLbdVlanBasedPort_Type()
)
eltMesLbdVlanBasedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesLbdVlanBasedPort.setStatus("current")


class _EltMesLbdVlanBasedVlanId1To1024_Type(OctetString):
    """Custom type eltMesLbdVlanBasedVlanId1To1024 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EltMesLbdVlanBasedVlanId1To1024_Type.__name__ = "OctetString"
_EltMesLbdVlanBasedVlanId1To1024_Object = MibTableColumn
eltMesLbdVlanBasedVlanId1To1024 = _EltMesLbdVlanBasedVlanId1To1024_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 127, 3, 1, 2),
    _EltMesLbdVlanBasedVlanId1To1024_Type()
)
eltMesLbdVlanBasedVlanId1To1024.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesLbdVlanBasedVlanId1To1024.setStatus("current")


class _EltMesLbdVlanBasedVlanId1025To2048_Type(OctetString):
    """Custom type eltMesLbdVlanBasedVlanId1025To2048 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EltMesLbdVlanBasedVlanId1025To2048_Type.__name__ = "OctetString"
_EltMesLbdVlanBasedVlanId1025To2048_Object = MibTableColumn
eltMesLbdVlanBasedVlanId1025To2048 = _EltMesLbdVlanBasedVlanId1025To2048_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 127, 3, 1, 3),
    _EltMesLbdVlanBasedVlanId1025To2048_Type()
)
eltMesLbdVlanBasedVlanId1025To2048.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesLbdVlanBasedVlanId1025To2048.setStatus("current")


class _EltMesLbdVlanBasedVlanId2049To3072_Type(OctetString):
    """Custom type eltMesLbdVlanBasedVlanId2049To3072 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EltMesLbdVlanBasedVlanId2049To3072_Type.__name__ = "OctetString"
_EltMesLbdVlanBasedVlanId2049To3072_Object = MibTableColumn
eltMesLbdVlanBasedVlanId2049To3072 = _EltMesLbdVlanBasedVlanId2049To3072_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 127, 3, 1, 4),
    _EltMesLbdVlanBasedVlanId2049To3072_Type()
)
eltMesLbdVlanBasedVlanId2049To3072.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesLbdVlanBasedVlanId2049To3072.setStatus("current")


class _EltMesLbdVlanBasedVlanId3073To4094_Type(OctetString):
    """Custom type eltMesLbdVlanBasedVlanId3073To4094 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EltMesLbdVlanBasedVlanId3073To4094_Type.__name__ = "OctetString"
_EltMesLbdVlanBasedVlanId3073To4094_Object = MibTableColumn
eltMesLbdVlanBasedVlanId3073To4094 = _EltMesLbdVlanBasedVlanId3073To4094_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 127, 3, 1, 5),
    _EltMesLbdVlanBasedVlanId3073To4094_Type()
)
eltMesLbdVlanBasedVlanId3073To4094.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesLbdVlanBasedVlanId3073To4094.setStatus("current")
_EltMesLbdVlanBasedVlanStateTable_Object = MibTable
eltMesLbdVlanBasedVlanStateTable = _EltMesLbdVlanBasedVlanStateTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 127, 4)
)
if mibBuilder.loadTexts:
    eltMesLbdVlanBasedVlanStateTable.setStatus("current")
_EltMesLbdVlanBasedVlanStateEntry_Object = MibTableRow
eltMesLbdVlanBasedVlanStateEntry = _EltMesLbdVlanBasedVlanStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 127, 4, 1)
)
eltMesLbdVlanBasedVlanStateEntry.setIndexNames(
    (0, "ELTEX-LBD-MIB", "eltMesLbdVlanBasedVlanStatePort"),
    (0, "ELTEX-LBD-MIB", "eltMesLbdVlanBasedVlanStateVlan"),
)
if mibBuilder.loadTexts:
    eltMesLbdVlanBasedVlanStateEntry.setStatus("current")
_EltMesLbdVlanBasedVlanStatePort_Type = InterfaceIndex
_EltMesLbdVlanBasedVlanStatePort_Object = MibTableColumn
eltMesLbdVlanBasedVlanStatePort = _EltMesLbdVlanBasedVlanStatePort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 127, 4, 1, 1),
    _EltMesLbdVlanBasedVlanStatePort_Type()
)
eltMesLbdVlanBasedVlanStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesLbdVlanBasedVlanStatePort.setStatus("current")
_EltMesLbdVlanBasedVlanStateVlan_Type = VlanIndex
_EltMesLbdVlanBasedVlanStateVlan_Object = MibTableColumn
eltMesLbdVlanBasedVlanStateVlan = _EltMesLbdVlanBasedVlanStateVlan_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 127, 4, 1, 2),
    _EltMesLbdVlanBasedVlanStateVlan_Type()
)
eltMesLbdVlanBasedVlanStateVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesLbdVlanBasedVlanStateVlan.setStatus("current")


class _EltMesLbdVlanBasedVlanState_Type(Integer32):
    """Custom type eltMesLbdVlanBasedVlanState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("blocked", 2))
    )


_EltMesLbdVlanBasedVlanState_Type.__name__ = "Integer32"
_EltMesLbdVlanBasedVlanState_Object = MibTableColumn
eltMesLbdVlanBasedVlanState = _EltMesLbdVlanBasedVlanState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 127, 4, 1, 3),
    _EltMesLbdVlanBasedVlanState_Type()
)
eltMesLbdVlanBasedVlanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesLbdVlanBasedVlanState.setStatus("current")
_EltMesLbdVlanBasedGlobals_ObjectIdentity = ObjectIdentity
eltMesLbdVlanBasedGlobals = _EltMesLbdVlanBasedGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 127, 5)
)
_EltMesLbdVlanBasedGlobalsId1To1024_Type = VlanList1
_EltMesLbdVlanBasedGlobalsId1To1024_Object = MibScalar
eltMesLbdVlanBasedGlobalsId1To1024 = _EltMesLbdVlanBasedGlobalsId1To1024_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 127, 5, 1),
    _EltMesLbdVlanBasedGlobalsId1To1024_Type()
)
eltMesLbdVlanBasedGlobalsId1To1024.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesLbdVlanBasedGlobalsId1To1024.setStatus("current")
_EltMesLbdVlanBasedGlobalsId1025To2048_Type = VlanList2
_EltMesLbdVlanBasedGlobalsId1025To2048_Object = MibScalar
eltMesLbdVlanBasedGlobalsId1025To2048 = _EltMesLbdVlanBasedGlobalsId1025To2048_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 127, 5, 2),
    _EltMesLbdVlanBasedGlobalsId1025To2048_Type()
)
eltMesLbdVlanBasedGlobalsId1025To2048.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesLbdVlanBasedGlobalsId1025To2048.setStatus("current")
_EltMesLbdVlanBasedGlobalsId2049To3072_Type = VlanList3
_EltMesLbdVlanBasedGlobalsId2049To3072_Object = MibScalar
eltMesLbdVlanBasedGlobalsId2049To3072 = _EltMesLbdVlanBasedGlobalsId2049To3072_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 127, 5, 3),
    _EltMesLbdVlanBasedGlobalsId2049To3072_Type()
)
eltMesLbdVlanBasedGlobalsId2049To3072.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesLbdVlanBasedGlobalsId2049To3072.setStatus("current")
_EltMesLbdVlanBasedGlobalsId3073To4094_Type = VlanList4
_EltMesLbdVlanBasedGlobalsId3073To4094_Object = MibScalar
eltMesLbdVlanBasedGlobalsId3073To4094 = _EltMesLbdVlanBasedGlobalsId3073To4094_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 127, 5, 4),
    _EltMesLbdVlanBasedGlobalsId3073To4094_Type()
)
eltMesLbdVlanBasedGlobalsId3073To4094.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesLbdVlanBasedGlobalsId3073To4094.setStatus("current")

# Managed Objects groups


# Notification objects

eltMesLbdVlanBasedVlanNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 127, 0, 1)
)
eltMesLbdVlanBasedVlanNotif.setObjects(
    ("ELTEX-LBD-MIB", "eltMesLbdVlanBasedVlanState")
)
if mibBuilder.loadTexts:
    eltMesLbdVlanBasedVlanNotif.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-LBD-MIB",
    **{"eltMesLbd": eltMesLbd,
       "eltMesLbdNotif": eltMesLbdNotif,
       "eltMesLbdVlanBasedVlanNotif": eltMesLbdVlanBasedVlanNotif,
       "eltMesLbdVlanBased": eltMesLbdVlanBased,
       "eltMesLbdVlanBasedRecoveryTime": eltMesLbdVlanBasedRecoveryTime,
       "eltMesLbdVlanBasedPortTable": eltMesLbdVlanBasedPortTable,
       "eltMesLbdVlanBasedPortEntry": eltMesLbdVlanBasedPortEntry,
       "eltMesLbdVlanBasedPort": eltMesLbdVlanBasedPort,
       "eltMesLbdVlanBasedVlanId1To1024": eltMesLbdVlanBasedVlanId1To1024,
       "eltMesLbdVlanBasedVlanId1025To2048": eltMesLbdVlanBasedVlanId1025To2048,
       "eltMesLbdVlanBasedVlanId2049To3072": eltMesLbdVlanBasedVlanId2049To3072,
       "eltMesLbdVlanBasedVlanId3073To4094": eltMesLbdVlanBasedVlanId3073To4094,
       "eltMesLbdVlanBasedVlanStateTable": eltMesLbdVlanBasedVlanStateTable,
       "eltMesLbdVlanBasedVlanStateEntry": eltMesLbdVlanBasedVlanStateEntry,
       "eltMesLbdVlanBasedVlanStatePort": eltMesLbdVlanBasedVlanStatePort,
       "eltMesLbdVlanBasedVlanStateVlan": eltMesLbdVlanBasedVlanStateVlan,
       "eltMesLbdVlanBasedVlanState": eltMesLbdVlanBasedVlanState,
       "eltMesLbdVlanBasedGlobals": eltMesLbdVlanBasedGlobals,
       "eltMesLbdVlanBasedGlobalsId1To1024": eltMesLbdVlanBasedGlobalsId1To1024,
       "eltMesLbdVlanBasedGlobalsId1025To2048": eltMesLbdVlanBasedGlobalsId1025To2048,
       "eltMesLbdVlanBasedGlobalsId2049To3072": eltMesLbdVlanBasedGlobalsId2049To3072,
       "eltMesLbdVlanBasedGlobalsId3073To4094": eltMesLbdVlanBasedGlobalsId3073To4094}
)
