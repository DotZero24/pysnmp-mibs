# SNMP MIB module (ADTRAN-ARP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-ARP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:32:39 2025
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

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adGenArp,
 adGenArpID) = mibBuilder.importSymbols(
    "ADTRAN-GENTA5K-MIB",
    "adGenArp",
    "adGenArpID")

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

adTa5kArpModuleIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 67, 1, 30, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenArpTable_Object = MibTable
adGenArpTable = _AdGenArpTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 30, 1)
)
if mibBuilder.loadTexts:
    adGenArpTable.setStatus("current")
_AdGenArpEntry_Object = MibTableRow
adGenArpEntry = _AdGenArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 30, 1, 1)
)
adGenArpEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-ARP-MIB", "adGenArpIpAddress"),
    (0, "ADTRAN-ARP-MIB", "adGenArpOuterVlan"),
    (0, "ADTRAN-ARP-MIB", "adGenArpInnerVlan"),
)
if mibBuilder.loadTexts:
    adGenArpEntry.setStatus("current")
_AdGenArpIpAddress_Type = IpAddress
_AdGenArpIpAddress_Object = MibTableColumn
adGenArpIpAddress = _AdGenArpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 30, 1, 1, 1),
    _AdGenArpIpAddress_Type()
)
adGenArpIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenArpIpAddress.setStatus("current")
_AdGenArpOuterVlan_Type = Integer32
_AdGenArpOuterVlan_Object = MibTableColumn
adGenArpOuterVlan = _AdGenArpOuterVlan_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 30, 1, 1, 2),
    _AdGenArpOuterVlan_Type()
)
adGenArpOuterVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenArpOuterVlan.setStatus("current")
_AdGenArpInnerVlan_Type = Integer32
_AdGenArpInnerVlan_Object = MibTableColumn
adGenArpInnerVlan = _AdGenArpInnerVlan_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 30, 1, 1, 3),
    _AdGenArpInnerVlan_Type()
)
adGenArpInnerVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenArpInnerVlan.setStatus("current")


class _AdGenArpMacAddress_Type(OctetString):
    """Custom type adGenArpMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_AdGenArpMacAddress_Type.__name__ = "OctetString"
_AdGenArpMacAddress_Object = MibTableColumn
adGenArpMacAddress = _AdGenArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 30, 1, 1, 4),
    _AdGenArpMacAddress_Type()
)
adGenArpMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenArpMacAddress.setStatus("current")
_AdGenArpTTLMin_Type = Integer32
_AdGenArpTTLMin_Object = MibTableColumn
adGenArpTTLMin = _AdGenArpTTLMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 30, 1, 1, 5),
    _AdGenArpTTLMin_Type()
)
adGenArpTTLMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenArpTTLMin.setStatus("current")
_AdGenArpInterface_Type = DisplayString
_AdGenArpInterface_Object = MibTableColumn
adGenArpInterface = _AdGenArpInterface_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 30, 1, 1, 6),
    _AdGenArpInterface_Type()
)
adGenArpInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenArpInterface.setStatus("current")


class _AdGenArpType_Type(Integer32):
    """Custom type adGenArpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("invalid", 2),
          ("dynamic", 3),
          ("static", 4),
          ("proxy", 5),
          ("reachable", 6),
          ("stale", 7),
          ("incomplete", 8))
    )


_AdGenArpType_Type.__name__ = "Integer32"
_AdGenArpType_Object = MibTableColumn
adGenArpType = _AdGenArpType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 30, 1, 1, 7),
    _AdGenArpType_Type()
)
adGenArpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenArpType.setStatus("current")
_AdGenArpSettingsTable_Object = MibTable
adGenArpSettingsTable = _AdGenArpSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 30, 2)
)
if mibBuilder.loadTexts:
    adGenArpSettingsTable.setStatus("current")
_AdGenArpSettingsEntry_Object = MibTableRow
adGenArpSettingsEntry = _AdGenArpSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 30, 2, 1)
)
adGenArpSettingsEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenArpSettingsEntry.setStatus("current")
_AdGenArpTimeout_Type = Integer32
_AdGenArpTimeout_Object = MibTableColumn
adGenArpTimeout = _AdGenArpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 30, 2, 1, 1),
    _AdGenArpTimeout_Type()
)
adGenArpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenArpTimeout.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-ARP-MIB",
    **{"adGenArpTable": adGenArpTable,
       "adGenArpEntry": adGenArpEntry,
       "adGenArpIpAddress": adGenArpIpAddress,
       "adGenArpOuterVlan": adGenArpOuterVlan,
       "adGenArpInnerVlan": adGenArpInnerVlan,
       "adGenArpMacAddress": adGenArpMacAddress,
       "adGenArpTTLMin": adGenArpTTLMin,
       "adGenArpInterface": adGenArpInterface,
       "adGenArpType": adGenArpType,
       "adGenArpSettingsTable": adGenArpSettingsTable,
       "adGenArpSettingsEntry": adGenArpSettingsEntry,
       "adGenArpTimeout": adGenArpTimeout,
       "adTa5kArpModuleIdentity": adTa5kArpModuleIdentity}
)
