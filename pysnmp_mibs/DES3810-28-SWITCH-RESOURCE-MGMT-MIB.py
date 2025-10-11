# SNMP MIB module (DES3810-28-SWITCH-RESOURCE-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DES3810-28-SWITCH-RESOURCE-MGMT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:49:38 2025
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(des3810_28,) = mibBuilder.importSymbols(
    "SW3810PRIMGMT-MIB",
    "des3810-28")


# MODULE-IDENTITY

swSwitchResourceMgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 1, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwSwitchResourceMgmtMIBObjects_ObjectIdentity = ObjectIdentity
swSwitchResourceMgmtMIBObjects = _SwSwitchResourceMgmtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 1, 4, 1)
)


class _SwSwitchResourceMgmtSRMMode_Type(Integer32):
    """Custom type swSwitchResourceMgmtSRMMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("routing", 1),
          ("vpws", 2))
    )


_SwSwitchResourceMgmtSRMMode_Type.__name__ = "Integer32"
_SwSwitchResourceMgmtSRMMode_Object = MibScalar
swSwitchResourceMgmtSRMMode = _SwSwitchResourceMgmtSRMMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 1, 4, 1, 2),
    _SwSwitchResourceMgmtSRMMode_Type()
)
swSwitchResourceMgmtSRMMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSwitchResourceMgmtSRMMode.setStatus("current")


class _SwSwitchResourceMgmtSRMCurrentMode_Type(Integer32):
    """Custom type swSwitchResourceMgmtSRMCurrentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("routing", 1),
          ("vpws", 2))
    )


_SwSwitchResourceMgmtSRMCurrentMode_Type.__name__ = "Integer32"
_SwSwitchResourceMgmtSRMCurrentMode_Object = MibScalar
swSwitchResourceMgmtSRMCurrentMode = _SwSwitchResourceMgmtSRMCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 1, 4, 1, 3),
    _SwSwitchResourceMgmtSRMCurrentMode_Type()
)
swSwitchResourceMgmtSRMCurrentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSwitchResourceMgmtSRMCurrentMode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DES3810-28-SWITCH-RESOURCE-MGMT-MIB",
    **{"swSwitchResourceMgmtMIB": swSwitchResourceMgmtMIB,
       "swSwitchResourceMgmtMIBObjects": swSwitchResourceMgmtMIBObjects,
       "swSwitchResourceMgmtSRMMode": swSwitchResourceMgmtSRMMode,
       "swSwitchResourceMgmtSRMCurrentMode": swSwitchResourceMgmtSRMCurrentMode}
)
