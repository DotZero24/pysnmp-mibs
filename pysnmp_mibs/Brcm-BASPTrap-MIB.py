# SNMP MIB module (Brcm-BASPTrap-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/broadcom/Brcm-BASPTrap-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:08:53 2025
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
 NotificationType,
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
    "NotificationType",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Broadcom_ObjectIdentity = ObjectIdentity
broadcom = _Broadcom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413)
)
_Enet_ObjectIdentity = ObjectIdentity
enet = _Enet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1)
)
_Basp_ObjectIdentity = ObjectIdentity
basp = _Basp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2)
)
_BaspConfig_ObjectIdentity = ObjectIdentity
baspConfig = _BaspConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 1)
)
_BaspStat_ObjectIdentity = ObjectIdentity
baspStat = _BaspStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 2)
)
_BaspTrap_ObjectIdentity = ObjectIdentity
baspTrap = _BaspTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 3)
)
_TrapAdapterName_Type = DisplayString
_TrapAdapterName_Object = MibScalar
trapAdapterName = _TrapAdapterName_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 3, 1),
    _TrapAdapterName_Type()
)
trapAdapterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapAdapterName.setStatus("mandatory")
_TrapTeamName_Type = DisplayString
_TrapTeamName_Object = MibScalar
trapTeamName = _TrapTeamName_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 3, 2),
    _TrapTeamName_Type()
)
trapTeamName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapTeamName.setStatus("mandatory")


class _TrapCauseDirection_Type(Integer32):
    """Custom type trapCauseDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adapterActive", 1),
          ("adapterInactive", 2))
    )


_TrapCauseDirection_Type.__name__ = "Integer32"
_TrapCauseDirection_Object = MibScalar
trapCauseDirection = _TrapCauseDirection_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 3, 3),
    _TrapCauseDirection_Type()
)
trapCauseDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapCauseDirection.setStatus("mandatory")


class _TrapAdapterActivityCause_Type(Integer32):
    """Custom type trapAdapterActivityCause based on Integer32"""
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
        *(("none", 1),
          ("linkChange", 2),
          ("adapterEnabledOrDisabled", 3),
          ("adapterAddedOrRemoved", 4))
    )


_TrapAdapterActivityCause_Type.__name__ = "Integer32"
_TrapAdapterActivityCause_Object = MibScalar
trapAdapterActivityCause = _TrapAdapterActivityCause_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 3, 4),
    _TrapAdapterActivityCause_Type()
)
trapAdapterActivityCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapAdapterActivityCause.setStatus("mandatory")

# Managed Objects groups


# Notification objects

failoverEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4413, 1, 2, 3, 0, 1)
)
failoverEvent.setObjects(
      *(("Brcm-BASPTrap-MIB", "trapAdapterName"),
        ("Brcm-BASPTrap-MIB", "trapTeamName"),
        ("Brcm-BASPTrap-MIB", "trapCauseDirection"),
        ("Brcm-BASPTrap-MIB", "trapAdapterActivityCause"))
)
if mibBuilder.loadTexts:
    failoverEvent.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Brcm-BASPTrap-MIB",
    **{"broadcom": broadcom,
       "enet": enet,
       "basp": basp,
       "baspConfig": baspConfig,
       "baspStat": baspStat,
       "baspTrap": baspTrap,
       "failoverEvent": failoverEvent,
       "trapAdapterName": trapAdapterName,
       "trapTeamName": trapTeamName,
       "trapCauseDirection": trapCauseDirection,
       "trapAdapterActivityCause": trapAdapterActivityCause}
)
