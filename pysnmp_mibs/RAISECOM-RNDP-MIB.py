# SNMP MIB module (RAISECOM-RNDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-RNDP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:37:19 2025
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

(raisecomCluster,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "raisecomCluster")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")

(EnableVar,) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar")


# MODULE-IDENTITY

raisecomTopoDiscovery = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _RaisecomRndpProtocolEnable_Type(EnableVar):
    """Custom type raisecomRndpProtocolEnable based on EnableVar"""
    defaultValue = 2


_RaisecomRndpProtocolEnable_Type.__name__ = "EnableVar"
_RaisecomRndpProtocolEnable_Object = MibScalar
raisecomRndpProtocolEnable = _RaisecomRndpProtocolEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 2, 1),
    _RaisecomRndpProtocolEnable_Type()
)
raisecomRndpProtocolEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRndpProtocolEnable.setStatus("mandatory")
_RaisecomRndpDiscoveryTable_Object = MibTable
raisecomRndpDiscoveryTable = _RaisecomRndpDiscoveryTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 2, 2)
)
if mibBuilder.loadTexts:
    raisecomRndpDiscoveryTable.setStatus("current")
_RaisecomRndpDiscoveryEntry_Object = MibTableRow
raisecomRndpDiscoveryEntry = _RaisecomRndpDiscoveryEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 2, 2, 1)
)
raisecomRndpDiscoveryEntry.setIndexNames(
    (0, "RAISECOM-RNDP-MIB", "raisecomRndpDiscoveryInterfaceId"),
    (0, "RAISECOM-RNDP-MIB", "raisecomRndpDiscoveryDeviceId"),
)
if mibBuilder.loadTexts:
    raisecomRndpDiscoveryEntry.setStatus("current")
_RaisecomRndpDiscoveryInterfaceId_Type = Integer32
_RaisecomRndpDiscoveryInterfaceId_Object = MibTableColumn
raisecomRndpDiscoveryInterfaceId = _RaisecomRndpDiscoveryInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 2, 2, 1, 1),
    _RaisecomRndpDiscoveryInterfaceId_Type()
)
raisecomRndpDiscoveryInterfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRndpDiscoveryInterfaceId.setStatus("current")
_RaisecomRndpDiscoveryDeviceId_Type = MacAddress
_RaisecomRndpDiscoveryDeviceId_Object = MibTableColumn
raisecomRndpDiscoveryDeviceId = _RaisecomRndpDiscoveryDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 2, 2, 1, 2),
    _RaisecomRndpDiscoveryDeviceId_Type()
)
raisecomRndpDiscoveryDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRndpDiscoveryDeviceId.setStatus("current")
_RaisecomRndpDiscoveryPortId_Type = Integer32
_RaisecomRndpDiscoveryPortId_Object = MibTableColumn
raisecomRndpDiscoveryPortId = _RaisecomRndpDiscoveryPortId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 2, 2, 1, 3),
    _RaisecomRndpDiscoveryPortId_Type()
)
raisecomRndpDiscoveryPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRndpDiscoveryPortId.setStatus("current")
_RaisecomRndpDiscoveryHostName_Type = OctetString
_RaisecomRndpDiscoveryHostName_Object = MibTableColumn
raisecomRndpDiscoveryHostName = _RaisecomRndpDiscoveryHostName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 2, 2, 1, 4),
    _RaisecomRndpDiscoveryHostName_Type()
)
raisecomRndpDiscoveryHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRndpDiscoveryHostName.setStatus("current")
_RaisecomRndpDiscoveryPlatformOid_Type = ObjectIdentifier
_RaisecomRndpDiscoveryPlatformOid_Object = MibTableColumn
raisecomRndpDiscoveryPlatformOid = _RaisecomRndpDiscoveryPlatformOid_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 2, 2, 1, 5),
    _RaisecomRndpDiscoveryPlatformOid_Type()
)
raisecomRndpDiscoveryPlatformOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRndpDiscoveryPlatformOid.setStatus("current")
_RaisecomRndpDiscoveryVersion_Type = OctetString
_RaisecomRndpDiscoveryVersion_Object = MibTableColumn
raisecomRndpDiscoveryVersion = _RaisecomRndpDiscoveryVersion_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 2, 2, 1, 6),
    _RaisecomRndpDiscoveryVersion_Type()
)
raisecomRndpDiscoveryVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRndpDiscoveryVersion.setStatus("current")


class _RaisecomRndpDiscoveryCapabilities_Type(Integer32):
    """Custom type raisecomRndpDiscoveryCapabilities based on Integer32"""
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
        *(("switch", 1),
          ("router", 2),
          ("eoa", 3),
          ("eos", 4),
          ("others", 5))
    )


_RaisecomRndpDiscoveryCapabilities_Type.__name__ = "Integer32"
_RaisecomRndpDiscoveryCapabilities_Object = MibTableColumn
raisecomRndpDiscoveryCapabilities = _RaisecomRndpDiscoveryCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 2, 2, 1, 7),
    _RaisecomRndpDiscoveryCapabilities_Type()
)
raisecomRndpDiscoveryCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRndpDiscoveryCapabilities.setStatus("current")
_RaisecomRndpInterfaceTable_Object = MibTable
raisecomRndpInterfaceTable = _RaisecomRndpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 2, 3)
)
if mibBuilder.loadTexts:
    raisecomRndpInterfaceTable.setStatus("mandatory")
_RaisecomRndpInterfaceEntry_Object = MibTableRow
raisecomRndpInterfaceEntry = _RaisecomRndpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 2, 3, 1)
)
raisecomRndpInterfaceEntry.setIndexNames(
    (0, "RAISECOM-RNDP-MIB", "raisecomRndpInterfaceId"),
)
if mibBuilder.loadTexts:
    raisecomRndpInterfaceEntry.setStatus("mandatory")
_RaisecomRndpInterfaceId_Type = Integer32
_RaisecomRndpInterfaceId_Object = MibTableColumn
raisecomRndpInterfaceId = _RaisecomRndpInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 2, 3, 1, 1),
    _RaisecomRndpInterfaceId_Type()
)
raisecomRndpInterfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRndpInterfaceId.setStatus("mandatory")
_RaisecomRndpInterfaceEnable_Type = EnableVar
_RaisecomRndpInterfaceEnable_Object = MibTableColumn
raisecomRndpInterfaceEnable = _RaisecomRndpInterfaceEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 2, 3, 1, 2),
    _RaisecomRndpInterfaceEnable_Type()
)
raisecomRndpInterfaceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRndpInterfaceEnable.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-RNDP-MIB",
    **{"raisecomTopoDiscovery": raisecomTopoDiscovery,
       "raisecomRndpProtocolEnable": raisecomRndpProtocolEnable,
       "raisecomRndpDiscoveryTable": raisecomRndpDiscoveryTable,
       "raisecomRndpDiscoveryEntry": raisecomRndpDiscoveryEntry,
       "raisecomRndpDiscoveryInterfaceId": raisecomRndpDiscoveryInterfaceId,
       "raisecomRndpDiscoveryDeviceId": raisecomRndpDiscoveryDeviceId,
       "raisecomRndpDiscoveryPortId": raisecomRndpDiscoveryPortId,
       "raisecomRndpDiscoveryHostName": raisecomRndpDiscoveryHostName,
       "raisecomRndpDiscoveryPlatformOid": raisecomRndpDiscoveryPlatformOid,
       "raisecomRndpDiscoveryVersion": raisecomRndpDiscoveryVersion,
       "raisecomRndpDiscoveryCapabilities": raisecomRndpDiscoveryCapabilities,
       "raisecomRndpInterfaceTable": raisecomRndpInterfaceTable,
       "raisecomRndpInterfaceEntry": raisecomRndpInterfaceEntry,
       "raisecomRndpInterfaceId": raisecomRndpInterfaceId,
       "raisecomRndpInterfaceEnable": raisecomRndpInterfaceEnable}
)
