# SNMP MIB module (ELTEX-VLAN-TRANSLATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-VLAN-TRANSLATION-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:49:10 2025
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

(eltexLtd,) = mibBuilder.importSymbols(
    "ELTEX-SMI-ACTUAL",
    "eltexLtd")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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


# MODULE-IDENTITY

eltexVlanTranslationMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 54)
)
if mibBuilder.loadTexts:
    eltexVlanTranslationMIB.setRevisions(
        ("2019-11-07 00:00",
         "2019-02-04 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EltexSqinqDirection(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ingress", 1),
          ("egress", 2))
    )



class EltexSqinqAction(TextualConvention, Integer32):
    status = "current"
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
        *(("overrideVlan", 1),
          ("addVlan", 2),
          ("permit", 3),
          ("deny", 4))
    )



# MIB Managed Objects in the order of their OIDs

_EltexVlanTranslationObjects_ObjectIdentity = ObjectIdentity
eltexVlanTranslationObjects = _EltexVlanTranslationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 54, 1)
)
_EltexSqinqObjects_ObjectIdentity = ObjectIdentity
eltexSqinqObjects = _EltexSqinqObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 54, 1, 1)
)
_EltexSqinqGlobals_ObjectIdentity = ObjectIdentity
eltexSqinqGlobals = _EltexSqinqGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 54, 1, 1, 1)
)
_EltexSqinqConfigs_ObjectIdentity = ObjectIdentity
eltexSqinqConfigs = _EltexSqinqConfigs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 54, 1, 1, 2)
)
_EltexSqinqPortTable_Object = MibTable
eltexSqinqPortTable = _EltexSqinqPortTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 54, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    eltexSqinqPortTable.setStatus("current")
_EltexSqinqPortEntry_Object = MibTableRow
eltexSqinqPortEntry = _EltexSqinqPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 54, 1, 1, 2, 1, 1)
)
eltexSqinqPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ELTEX-VLAN-TRANSLATION-MIB", "eltexSqinqDirection"),
    (0, "ELTEX-VLAN-TRANSLATION-MIB", "eltexSqinqClassifierVlan"),
)
if mibBuilder.loadTexts:
    eltexSqinqPortEntry.setStatus("current")
_EltexSqinqDirection_Type = EltexSqinqDirection
_EltexSqinqDirection_Object = MibTableColumn
eltexSqinqDirection = _EltexSqinqDirection_Object(
    (1, 3, 6, 1, 4, 1, 35265, 54, 1, 1, 2, 1, 1, 1),
    _EltexSqinqDirection_Type()
)
eltexSqinqDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexSqinqDirection.setStatus("current")
_EltexSqinqClassifierVlan_Type = VlanId
_EltexSqinqClassifierVlan_Object = MibTableColumn
eltexSqinqClassifierVlan = _EltexSqinqClassifierVlan_Object(
    (1, 3, 6, 1, 4, 1, 35265, 54, 1, 1, 2, 1, 1, 2),
    _EltexSqinqClassifierVlan_Type()
)
eltexSqinqClassifierVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexSqinqClassifierVlan.setStatus("current")
_EltexSqinqAction_Type = EltexSqinqAction
_EltexSqinqAction_Object = MibTableColumn
eltexSqinqAction = _EltexSqinqAction_Object(
    (1, 3, 6, 1, 4, 1, 35265, 54, 1, 1, 2, 1, 1, 3),
    _EltexSqinqAction_Type()
)
eltexSqinqAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexSqinqAction.setStatus("current")
_EltexSqinqActionVlan_Type = VlanId
_EltexSqinqActionVlan_Object = MibTableColumn
eltexSqinqActionVlan = _EltexSqinqActionVlan_Object(
    (1, 3, 6, 1, 4, 1, 35265, 54, 1, 1, 2, 1, 1, 4),
    _EltexSqinqActionVlan_Type()
)
eltexSqinqActionVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexSqinqActionVlan.setStatus("current")
_EltexSqinqRowStatus_Type = RowStatus
_EltexSqinqRowStatus_Object = MibTableColumn
eltexSqinqRowStatus = _EltexSqinqRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 54, 1, 1, 2, 1, 1, 5),
    _EltexSqinqRowStatus_Type()
)
eltexSqinqRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexSqinqRowStatus.setStatus("current")
_EltexSqinqStatistics_ObjectIdentity = ObjectIdentity
eltexSqinqStatistics = _EltexSqinqStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 54, 1, 1, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-VLAN-TRANSLATION-MIB",
    **{"EltexSqinqDirection": EltexSqinqDirection,
       "EltexSqinqAction": EltexSqinqAction,
       "eltexVlanTranslationMIB": eltexVlanTranslationMIB,
       "eltexVlanTranslationObjects": eltexVlanTranslationObjects,
       "eltexSqinqObjects": eltexSqinqObjects,
       "eltexSqinqGlobals": eltexSqinqGlobals,
       "eltexSqinqConfigs": eltexSqinqConfigs,
       "eltexSqinqPortTable": eltexSqinqPortTable,
       "eltexSqinqPortEntry": eltexSqinqPortEntry,
       "eltexSqinqDirection": eltexSqinqDirection,
       "eltexSqinqClassifierVlan": eltexSqinqClassifierVlan,
       "eltexSqinqAction": eltexSqinqAction,
       "eltexSqinqActionVlan": eltexSqinqActionVlan,
       "eltexSqinqRowStatus": eltexSqinqRowStatus,
       "eltexSqinqStatistics": eltexSqinqStatistics}
)
