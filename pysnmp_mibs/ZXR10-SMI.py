# SNMP MIB module (ZXR10-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZXR10-SMI
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:46 2025
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


# MODULE-IDENTITY

zte = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902)
)
if mibBuilder.loadTexts:
    zte.setRevisions(
        ("2005-04-12 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zxr10_ObjectIdentity = ObjectIdentity
zxr10 = _Zxr10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3)
)
if mibBuilder.loadTexts:
    zxr10.setStatus("current")
_Zxr10Products_ObjectIdentity = ObjectIdentity
zxr10Products = _Zxr10Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101)
)
if mibBuilder.loadTexts:
    zxr10Products.setStatus("current")
_Zxr10switch_ObjectIdentity = ObjectIdentity
zxr10switch = _Zxr10switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102)
)
if mibBuilder.loadTexts:
    zxr10switch.setStatus("current")
_Zxr10interfaces_ObjectIdentity = ObjectIdentity
zxr10interfaces = _Zxr10interfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103)
)
if mibBuilder.loadTexts:
    zxr10interfaces.setStatus("current")
_Zxr10L2vpn_ObjectIdentity = ObjectIdentity
zxr10L2vpn = _Zxr10L2vpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104)
)
if mibBuilder.loadTexts:
    zxr10L2vpn.setStatus("current")
_Zxr10L3vpn_ObjectIdentity = ObjectIdentity
zxr10L3vpn = _Zxr10L3vpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 105)
)
if mibBuilder.loadTexts:
    zxr10L3vpn.setStatus("current")
_Voip_ObjectIdentity = ObjectIdentity
voip = _Voip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 200)
)
if mibBuilder.loadTexts:
    voip.setStatus("current")
_Isdn_ObjectIdentity = ObjectIdentity
isdn = _Isdn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 201)
)
if mibBuilder.loadTexts:
    isdn.setStatus("current")
_Mgmt_ObjectIdentity = ObjectIdentity
mgmt = _Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 202)
)
if mibBuilder.loadTexts:
    mgmt.setStatus("current")
_Mstp_ObjectIdentity = ObjectIdentity
mstp = _Mstp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 300)
)
if mibBuilder.loadTexts:
    mstp.setStatus("current")
_Lacp_ObjectIdentity = ObjectIdentity
lacp = _Lacp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 301)
)
if mibBuilder.loadTexts:
    lacp.setStatus("current")
_Zxr10Modules_ObjectIdentity = ObjectIdentity
zxr10Modules = _Zxr10Modules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 500)
)
if mibBuilder.loadTexts:
    zxr10Modules.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXR10-SMI",
    **{"zte": zte,
       "zxr10": zxr10,
       "zxr10Products": zxr10Products,
       "zxr10switch": zxr10switch,
       "zxr10interfaces": zxr10interfaces,
       "zxr10L2vpn": zxr10L2vpn,
       "zxr10L3vpn": zxr10L3vpn,
       "voip": voip,
       "isdn": isdn,
       "mgmt": mgmt,
       "mstp": mstp,
       "lacp": lacp,
       "zxr10Modules": zxr10Modules}
)
