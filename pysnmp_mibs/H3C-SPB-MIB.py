# SNMP MIB module (H3C-SPB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-SPB-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:20:03 2025
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

(IEEE8021SpbmSPsourceId,) = mibBuilder.importSymbols(
    "IEEE8021-SPB-MIB",
    "IEEE8021SpbmSPsourceId")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(VlanIdOrNone,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIdOrNone")

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

h3cSpb = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 128)
)
if mibBuilder.loadTexts:
    h3cSpb.setRevisions(
        ("2012-11-22 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cSpbObjects_ObjectIdentity = ObjectIdentity
h3cSpbObjects = _H3cSpbObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 128, 1)
)
_H3cSpbSysObjects_ObjectIdentity = ObjectIdentity
h3cSpbSysObjects = _H3cSpbSysObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 128, 1, 1)
)


class _H3cSpbSysStatus_Type(Integer32):
    """Custom type h3cSpbSysStatus based on Integer32"""
    defaultValue = 2

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


_H3cSpbSysStatus_Type.__name__ = "Integer32"
_H3cSpbSysStatus_Object = MibScalar
h3cSpbSysStatus = _H3cSpbSysStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 128, 1, 1, 1),
    _H3cSpbSysStatus_Type()
)
h3cSpbSysStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSpbSysStatus.setStatus("current")


class _H3cSpbMulticastBVlanStatus_Type(Integer32):
    """Custom type h3cSpbMulticastBVlanStatus based on Integer32"""
    defaultValue = 2

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


_H3cSpbMulticastBVlanStatus_Type.__name__ = "Integer32"
_H3cSpbMulticastBVlanStatus_Object = MibScalar
h3cSpbMulticastBVlanStatus = _H3cSpbMulticastBVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 128, 1, 1, 2),
    _H3cSpbMulticastBVlanStatus_Type()
)
h3cSpbMulticastBVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSpbMulticastBVlanStatus.setStatus("current")
_H3cSpbConfig_ObjectIdentity = ObjectIdentity
h3cSpbConfig = _H3cSpbConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 128, 1, 2)
)
_H3cSpbIfTable_Object = MibTable
h3cSpbIfTable = _H3cSpbIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 128, 1, 2, 1)
)
if mibBuilder.loadTexts:
    h3cSpbIfTable.setStatus("current")
_H3cSpbIfEntry_Object = MibTableRow
h3cSpbIfEntry = _H3cSpbIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 128, 1, 2, 1, 1)
)
h3cSpbIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cSpbIfEntry.setStatus("current")


class _H3cSpbIfStatus_Type(Integer32):
    """Custom type h3cSpbIfStatus based on Integer32"""
    defaultValue = 2

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


_H3cSpbIfStatus_Type.__name__ = "Integer32"
_H3cSpbIfStatus_Object = MibTableColumn
h3cSpbIfStatus = _H3cSpbIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 128, 1, 2, 1, 1, 1),
    _H3cSpbIfStatus_Type()
)
h3cSpbIfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSpbIfStatus.setStatus("current")
_H3cSpbSrvTable_Object = MibTable
h3cSpbSrvTable = _H3cSpbSrvTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 128, 1, 2, 2)
)
if mibBuilder.loadTexts:
    h3cSpbSrvTable.setStatus("current")
_H3cSpbSrvEntry_Object = MibTableRow
h3cSpbSrvEntry = _H3cSpbSrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 128, 1, 2, 2, 1)
)
h3cSpbSrvEntry.setIndexNames(
    (0, "H3C-SPB-MIB", "h3cSpbSrvTableEntryTopIx"),
    (0, "H3C-SPB-MIB", "h3cSpbSrvTableEntryIsid"),
)
if mibBuilder.loadTexts:
    h3cSpbSrvEntry.setStatus("current")
_H3cSpbSrvTableEntryTopIx_Type = Unsigned32
_H3cSpbSrvTableEntryTopIx_Object = MibTableColumn
h3cSpbSrvTableEntryTopIx = _H3cSpbSrvTableEntryTopIx_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 128, 1, 2, 2, 1, 1),
    _H3cSpbSrvTableEntryTopIx_Type()
)
h3cSpbSrvTableEntryTopIx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cSpbSrvTableEntryTopIx.setStatus("current")


class _H3cSpbSrvTableEntryIsid_Type(Unsigned32):
    """Custom type h3cSpbSrvTableEntryIsid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(255, 16777215),
    )


_H3cSpbSrvTableEntryIsid_Type.__name__ = "Unsigned32"
_H3cSpbSrvTableEntryIsid_Object = MibTableColumn
h3cSpbSrvTableEntryIsid = _H3cSpbSrvTableEntryIsid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 128, 1, 2, 2, 1, 2),
    _H3cSpbSrvTableEntryIsid_Type()
)
h3cSpbSrvTableEntryIsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cSpbSrvTableEntryIsid.setStatus("current")
_H3cSpbSrvTableEntryBaseVid_Type = VlanIdOrNone
_H3cSpbSrvTableEntryBaseVid_Object = MibTableColumn
h3cSpbSrvTableEntryBaseVid = _H3cSpbSrvTableEntryBaseVid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 128, 1, 2, 2, 1, 3),
    _H3cSpbSrvTableEntryBaseVid_Type()
)
h3cSpbSrvTableEntryBaseVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSpbSrvTableEntryBaseVid.setStatus("current")


class _H3cSpbSrvTableEntryMode_Type(Integer32):
    """Custom type h3cSpbSrvTableEntryMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("headEnd", 1),
          ("tandem", 2))
    )


_H3cSpbSrvTableEntryMode_Type.__name__ = "Integer32"
_H3cSpbSrvTableEntryMode_Object = MibTableColumn
h3cSpbSrvTableEntryMode = _H3cSpbSrvTableEntryMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 128, 1, 2, 2, 1, 4),
    _H3cSpbSrvTableEntryMode_Type()
)
h3cSpbSrvTableEntryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSpbSrvTableEntryMode.setStatus("current")
_H3cSpbTrap_ObjectIdentity = ObjectIdentity
h3cSpbTrap = _H3cSpbTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 128, 1, 3)
)
_H3cSpbTraps_ObjectIdentity = ObjectIdentity
h3cSpbTraps = _H3cSpbTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 128, 1, 3, 0)
)
_H3cSpbTrapsObjects_ObjectIdentity = ObjectIdentity
h3cSpbTrapsObjects = _H3cSpbTrapsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 128, 1, 3, 1)
)
_H3cSpbConflictSysID_Type = MacAddress
_H3cSpbConflictSysID_Object = MibScalar
h3cSpbConflictSysID = _H3cSpbConflictSysID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 128, 1, 3, 1, 1),
    _H3cSpbConflictSysID_Type()
)
h3cSpbConflictSysID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cSpbConflictSysID.setStatus("current")
_H3cSpbConflictSPSourceID_Type = IEEE8021SpbmSPsourceId
_H3cSpbConflictSPSourceID_Object = MibScalar
h3cSpbConflictSPSourceID = _H3cSpbConflictSPSourceID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 128, 1, 3, 1, 2),
    _H3cSpbConflictSPSourceID_Type()
)
h3cSpbConflictSPSourceID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cSpbConflictSPSourceID.setStatus("current")
_H3cSpbConflictBMac_Type = MacAddress
_H3cSpbConflictBMac_Object = MibScalar
h3cSpbConflictBMac = _H3cSpbConflictBMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 128, 1, 3, 1, 3),
    _H3cSpbConflictBMac_Type()
)
h3cSpbConflictBMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cSpbConflictBMac.setStatus("current")

# Managed Objects groups


# Notification objects

h3cSpbSPSourceConflictTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 128, 1, 3, 0, 1)
)
h3cSpbSPSourceConflictTrap.setObjects(
      *(("H3C-SPB-MIB", "h3cSpbConflictSysID"),
        ("H3C-SPB-MIB", "h3cSpbConflictSPSourceID"))
)
if mibBuilder.loadTexts:
    h3cSpbSPSourceConflictTrap.setStatus(
        "current"
    )

h3cSpbBMacConflictTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 128, 1, 3, 0, 2)
)
h3cSpbBMacConflictTrap.setObjects(
      *(("H3C-SPB-MIB", "h3cSpbConflictSysID"),
        ("H3C-SPB-MIB", "h3cSpbConflictBMac"))
)
if mibBuilder.loadTexts:
    h3cSpbBMacConflictTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-SPB-MIB",
    **{"h3cSpb": h3cSpb,
       "h3cSpbObjects": h3cSpbObjects,
       "h3cSpbSysObjects": h3cSpbSysObjects,
       "h3cSpbSysStatus": h3cSpbSysStatus,
       "h3cSpbMulticastBVlanStatus": h3cSpbMulticastBVlanStatus,
       "h3cSpbConfig": h3cSpbConfig,
       "h3cSpbIfTable": h3cSpbIfTable,
       "h3cSpbIfEntry": h3cSpbIfEntry,
       "h3cSpbIfStatus": h3cSpbIfStatus,
       "h3cSpbSrvTable": h3cSpbSrvTable,
       "h3cSpbSrvEntry": h3cSpbSrvEntry,
       "h3cSpbSrvTableEntryTopIx": h3cSpbSrvTableEntryTopIx,
       "h3cSpbSrvTableEntryIsid": h3cSpbSrvTableEntryIsid,
       "h3cSpbSrvTableEntryBaseVid": h3cSpbSrvTableEntryBaseVid,
       "h3cSpbSrvTableEntryMode": h3cSpbSrvTableEntryMode,
       "h3cSpbTrap": h3cSpbTrap,
       "h3cSpbTraps": h3cSpbTraps,
       "h3cSpbSPSourceConflictTrap": h3cSpbSPSourceConflictTrap,
       "h3cSpbBMacConflictTrap": h3cSpbBMacConflictTrap,
       "h3cSpbTrapsObjects": h3cSpbTrapsObjects,
       "h3cSpbConflictSysID": h3cSpbConflictSysID,
       "h3cSpbConflictSPSourceID": h3cSpbConflictSPSourceID,
       "h3cSpbConflictBMac": h3cSpbConflictBMac}
)
