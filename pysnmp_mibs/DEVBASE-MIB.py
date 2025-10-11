# SNMP MIB module (DEVBASE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aperto/DEVBASE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:06:20 2025
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

(device,) = mibBuilder.importSymbols(
    "ANIROOT-MIB",
    "device")

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


# MODULE-IDENTITY

aniDevBase = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _AniDevProductName_Type(DisplayString):
    """Custom type aniDevProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AniDevProductName_Type.__name__ = "DisplayString"
_AniDevProductName_Object = MibScalar
aniDevProductName = _AniDevProductName_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 1, 1),
    _AniDevProductName_Type()
)
aniDevProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniDevProductName.setStatus("current")
_AniDevLanIpAddr_Type = IpAddress
_AniDevLanIpAddr_Object = MibScalar
aniDevLanIpAddr = _AniDevLanIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 1, 2),
    _AniDevLanIpAddr_Type()
)
aniDevLanIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniDevLanIpAddr.setStatus("current")
_AniDevLanSubnetMask_Type = IpAddress
_AniDevLanSubnetMask_Object = MibScalar
aniDevLanSubnetMask = _AniDevLanSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 1, 3),
    _AniDevLanSubnetMask_Type()
)
aniDevLanSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniDevLanSubnetMask.setStatus("current")
_AniDevDefaultGateway_Type = IpAddress
_AniDevDefaultGateway_Object = MibScalar
aniDevDefaultGateway = _AniDevDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 1, 4),
    _AniDevDefaultGateway_Type()
)
aniDevDefaultGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniDevDefaultGateway.setStatus("current")
_AniDevMacAddr_Type = MacAddress
_AniDevMacAddr_Object = MibScalar
aniDevMacAddr = _AniDevMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 1, 5),
    _AniDevMacAddr_Type()
)
aniDevMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniDevMacAddr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DEVBASE-MIB",
    **{"aniDevBase": aniDevBase,
       "aniDevProductName": aniDevProductName,
       "aniDevLanIpAddr": aniDevLanIpAddr,
       "aniDevLanSubnetMask": aniDevLanSubnetMask,
       "aniDevDefaultGateway": aniDevDefaultGateway,
       "aniDevMacAddr": aniDevMacAddr}
)
