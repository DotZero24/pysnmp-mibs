# SNMP MIB module (TPLINK-STATICARP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/tplink/TPLINK-STATICARP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:56:23 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")

(TPRowStatus,) = mibBuilder.importSymbols(
    "TPLINK-TC-MIB",
    "TPRowStatus")


# MODULE-IDENTITY

tplinkStaticARPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 54)
)
if mibBuilder.loadTexts:
    tplinkStaticARPMIB.setRevisions(
        ("2014-11-24 14:42",)
    )


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkStaticARPMIBObjects_ObjectIdentity = ObjectIdentity
tplinkStaticARPMIBObjects = _TplinkStaticARPMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 54, 1)
)
_TpStaticARPConfig_ObjectIdentity = ObjectIdentity
tpStaticARPConfig = _TpStaticARPConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 54, 1, 1)
)
_TpStaticARPConfigTable_Object = MibTable
tpStaticARPConfigTable = _TpStaticARPConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 54, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tpStaticARPConfigTable.setStatus("current")
_TpStaticARPConfigEntry_Object = MibTableRow
tpStaticARPConfigEntry = _TpStaticARPConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 54, 1, 1, 1, 1)
)
tpStaticARPConfigEntry.setIndexNames(
    (0, "TPLINK-STATICARP-MIB", "tpStaticARPItemIp"),
)
if mibBuilder.loadTexts:
    tpStaticARPConfigEntry.setStatus("current")
_TpStaticARPItemIp_Type = IpAddress
_TpStaticARPItemIp_Object = MibTableColumn
tpStaticARPItemIp = _TpStaticARPItemIp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 54, 1, 1, 1, 1, 1),
    _TpStaticARPItemIp_Type()
)
tpStaticARPItemIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpStaticARPItemIp.setStatus("current")


class _TpStaticARPItemMac_Type(OctetString):
    """Custom type tpStaticARPItemMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TpStaticARPItemMac_Type.__name__ = "OctetString"
_TpStaticARPItemMac_Object = MibTableColumn
tpStaticARPItemMac = _TpStaticARPItemMac_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 54, 1, 1, 1, 1, 2),
    _TpStaticARPItemMac_Type()
)
tpStaticARPItemMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpStaticARPItemMac.setStatus("current")


class _TpStaticArpItemInterfaceName_Type(OctetString):
    """Custom type tpStaticArpItemInterfaceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpStaticArpItemInterfaceName_Type.__name__ = "OctetString"
_TpStaticArpItemInterfaceName_Object = MibTableColumn
tpStaticArpItemInterfaceName = _TpStaticArpItemInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 54, 1, 1, 1, 1, 3),
    _TpStaticArpItemInterfaceName_Type()
)
tpStaticArpItemInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpStaticArpItemInterfaceName.setStatus("current")
_TpStaticARPItemStatus_Type = TPRowStatus
_TpStaticARPItemStatus_Object = MibTableColumn
tpStaticARPItemStatus = _TpStaticARPItemStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 54, 1, 1, 1, 1, 4),
    _TpStaticARPItemStatus_Type()
)
tpStaticARPItemStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpStaticARPItemStatus.setStatus("current")
_TplinkStaticARPNotifications_ObjectIdentity = ObjectIdentity
tplinkStaticARPNotifications = _TplinkStaticARPNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 54, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-STATICARP-MIB",
    **{"MacAddress": MacAddress,
       "tplinkStaticARPMIB": tplinkStaticARPMIB,
       "tplinkStaticARPMIBObjects": tplinkStaticARPMIBObjects,
       "tpStaticARPConfig": tpStaticARPConfig,
       "tpStaticARPConfigTable": tpStaticARPConfigTable,
       "tpStaticARPConfigEntry": tpStaticARPConfigEntry,
       "tpStaticARPItemIp": tpStaticARPItemIp,
       "tpStaticARPItemMac": tpStaticARPItemMac,
       "tpStaticArpItemInterfaceName": tpStaticArpItemInterfaceName,
       "tpStaticARPItemStatus": tpStaticARPItemStatus,
       "tplinkStaticARPNotifications": tplinkStaticARPNotifications}
)
