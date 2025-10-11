# SNMP MIB module (ELTEX-FASTPATH-BRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-FASTPATH-BRIDGE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:48:19 2025
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(eltMesFastpath,) = mibBuilder.importSymbols(
    "ELTEX-MES-FASTPATH-MIB",
    "eltMesFastpath")

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

eltFastpathBridgeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 3)
)
if mibBuilder.loadTexts:
    eltFastpathBridgeMIB.setRevisions(
        ("2017-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EfpBridgeStpGroupMacAddressType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dot1d", 1),
          ("dot1ad", 2),
          ("auto", 3))
    )



# MIB Managed Objects in the order of their OIDs

_EfpBridgeObjects_ObjectIdentity = ObjectIdentity
efpBridgeObjects = _EfpBridgeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 3, 1)
)
_EfpBridgeConfigs_ObjectIdentity = ObjectIdentity
efpBridgeConfigs = _EfpBridgeConfigs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 3, 1, 2)
)
_EfpBridgeConfigsStp_ObjectIdentity = ObjectIdentity
efpBridgeConfigsStp = _EfpBridgeConfigsStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 3, 1, 2, 1)
)
_EfpBridgeStpConfigPortTable_Object = MibTable
efpBridgeStpConfigPortTable = _EfpBridgeStpConfigPortTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 3, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    efpBridgeStpConfigPortTable.setStatus("current")
_EfpBridgeStpConfigPortEntry_Object = MibTableRow
efpBridgeStpConfigPortEntry = _EfpBridgeStpConfigPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 3, 1, 2, 1, 1, 1)
)
efpBridgeStpConfigPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    efpBridgeStpConfigPortEntry.setStatus("current")


class _EfpBridgeStpConfigPortGroupMacAddress_Type(EfpBridgeStpGroupMacAddressType):
    """Custom type efpBridgeStpConfigPortGroupMacAddress based on EfpBridgeStpGroupMacAddressType"""
    defaultValue = 1


_EfpBridgeStpConfigPortGroupMacAddress_Type.__name__ = "EfpBridgeStpGroupMacAddressType"
_EfpBridgeStpConfigPortGroupMacAddress_Object = MibTableColumn
efpBridgeStpConfigPortGroupMacAddress = _EfpBridgeStpConfigPortGroupMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 3, 1, 2, 1, 1, 1, 1),
    _EfpBridgeStpConfigPortGroupMacAddress_Type()
)
efpBridgeStpConfigPortGroupMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efpBridgeStpConfigPortGroupMacAddress.setStatus("current")
_EfpBridgeNotifications_ObjectIdentity = ObjectIdentity
efpBridgeNotifications = _EfpBridgeNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 3, 2)
)
_EfpBridgeNotificationsPrefix_ObjectIdentity = ObjectIdentity
efpBridgeNotificationsPrefix = _EfpBridgeNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 3, 2, 0)
)
_EfpBridgeConformance_ObjectIdentity = ObjectIdentity
efpBridgeConformance = _EfpBridgeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 3, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-FASTPATH-BRIDGE-MIB",
    **{"EfpBridgeStpGroupMacAddressType": EfpBridgeStpGroupMacAddressType,
       "eltFastpathBridgeMIB": eltFastpathBridgeMIB,
       "efpBridgeObjects": efpBridgeObjects,
       "efpBridgeConfigs": efpBridgeConfigs,
       "efpBridgeConfigsStp": efpBridgeConfigsStp,
       "efpBridgeStpConfigPortTable": efpBridgeStpConfigPortTable,
       "efpBridgeStpConfigPortEntry": efpBridgeStpConfigPortEntry,
       "efpBridgeStpConfigPortGroupMacAddress": efpBridgeStpConfigPortGroupMacAddress,
       "efpBridgeNotifications": efpBridgeNotifications,
       "efpBridgeNotificationsPrefix": efpBridgeNotificationsPrefix,
       "efpBridgeConformance": efpBridgeConformance}
)
