# SNMP MIB module (RUCKUS-SCG-CONFIG-WLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/ruckus/RUCKUS-SCG-CONFIG-WLAN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:13:48 2025
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

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(ruckusSCGWLANModule,) = mibBuilder.importSymbols(
    "RUCKUS-ROOT-MIB",
    "ruckusSCGWLANModule")

(RuckusAdminStatus,
 RuckusRadioMode,
 RuckusRateLimiting,
 RuckusSSID,
 RuckusdB) = mibBuilder.importSymbols(
    "RUCKUS-TC-MIB",
    "RuckusAdminStatus",
    "RuckusRadioMode",
    "RuckusRateLimiting",
    "RuckusSSID",
    "RuckusdB")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruckusSCGConfigWLANMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuckusSCGConfigWLANObjects_ObjectIdentity = ObjectIdentity
ruckusSCGConfigWLANObjects = _RuckusSCGConfigWLANObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 2, 1)
)
_RuckusSCGConfigWLAN_ObjectIdentity = ObjectIdentity
ruckusSCGConfigWLAN = _RuckusSCGConfigWLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 2, 1, 1)
)
_RuckusSCGConfigWLANTable_Object = MibTable
ruckusSCGConfigWLANTable = _RuckusSCGConfigWLANTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ruckusSCGConfigWLANTable.setStatus("current")
_RuckusSCGConfigWLANEntry_Object = MibTableRow
ruckusSCGConfigWLANEntry = _RuckusSCGConfigWLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 2, 1, 1, 1, 1)
)
ruckusSCGConfigWLANEntry.setIndexNames(
    (0, "RUCKUS-SCG-CONFIG-WLAN-MIB", "ruckusSCGConfigWLANID"),
)
if mibBuilder.loadTexts:
    ruckusSCGConfigWLANEntry.setStatus("current")


class _RuckusSCGConfigWLANID_Type(Integer32):
    """Custom type ruckusSCGConfigWLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuckusSCGConfigWLANID_Type.__name__ = "Integer32"
_RuckusSCGConfigWLANID_Object = MibTableColumn
ruckusSCGConfigWLANID = _RuckusSCGConfigWLANID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 2, 1, 1, 1, 1, 1),
    _RuckusSCGConfigWLANID_Type()
)
ruckusSCGConfigWLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGConfigWLANID.setStatus("current")


class _RuckusSCGConfigWLANSSID_Type(OctetString):
    """Custom type ruckusSCGConfigWLANSSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 32),
    )


_RuckusSCGConfigWLANSSID_Type.__name__ = "OctetString"
_RuckusSCGConfigWLANSSID_Object = MibTableColumn
ruckusSCGConfigWLANSSID = _RuckusSCGConfigWLANSSID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 2, 1, 1, 1, 1, 2),
    _RuckusSCGConfigWLANSSID_Type()
)
ruckusSCGConfigWLANSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGConfigWLANSSID.setStatus("current")


class _RuckusSCGConfigWLANDescription_Type(DisplayString):
    """Custom type ruckusSCGConfigWLANDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RuckusSCGConfigWLANDescription_Type.__name__ = "DisplayString"
_RuckusSCGConfigWLANDescription_Object = MibTableColumn
ruckusSCGConfigWLANDescription = _RuckusSCGConfigWLANDescription_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 2, 1, 1, 1, 1, 3),
    _RuckusSCGConfigWLANDescription_Type()
)
ruckusSCGConfigWLANDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusSCGConfigWLANDescription.setStatus("current")


class _RuckusSCGConfigWLANName_Type(OctetString):
    """Custom type ruckusSCGConfigWLANName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 32),
    )


_RuckusSCGConfigWLANName_Type.__name__ = "OctetString"
_RuckusSCGConfigWLANName_Object = MibTableColumn
ruckusSCGConfigWLANName = _RuckusSCGConfigWLANName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 2, 1, 1, 1, 1, 4),
    _RuckusSCGConfigWLANName_Type()
)
ruckusSCGConfigWLANName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGConfigWLANName.setStatus("current")


class _RuckusSCGZoneName_Type(OctetString):
    """Custom type ruckusSCGZoneName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RuckusSCGZoneName_Type.__name__ = "OctetString"
_RuckusSCGZoneName_Object = MibTableColumn
ruckusSCGZoneName = _RuckusSCGZoneName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 2, 1, 1, 1, 1, 5),
    _RuckusSCGZoneName_Type()
)
ruckusSCGZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGZoneName.setStatus("current")


class _RuckusSCGConfigWLANWLANServiceType_Type(Integer32):
    """Custom type ruckusSCGConfigWLANWLANServiceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("standardUsage", 1),
          ("hotspot", 2),
          ("guest", 3),
          ("webauth", 4),
          ("hotspot20", 5),
          ("hotspot20-osen", 6))
    )


_RuckusSCGConfigWLANWLANServiceType_Type.__name__ = "Integer32"
_RuckusSCGConfigWLANWLANServiceType_Object = MibTableColumn
ruckusSCGConfigWLANWLANServiceType = _RuckusSCGConfigWLANWLANServiceType_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 2, 1, 1, 1, 1, 8),
    _RuckusSCGConfigWLANWLANServiceType_Type()
)
ruckusSCGConfigWLANWLANServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGConfigWLANWLANServiceType.setStatus("current")


class _RuckusSCGConfigWLANAuthentication_Type(Integer32):
    """Custom type ruckusSCGConfigWLANAuthentication based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("eap", 2),
          ("mac-address", 3))
    )


_RuckusSCGConfigWLANAuthentication_Type.__name__ = "Integer32"
_RuckusSCGConfigWLANAuthentication_Object = MibTableColumn
ruckusSCGConfigWLANAuthentication = _RuckusSCGConfigWLANAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 2, 1, 1, 1, 1, 10),
    _RuckusSCGConfigWLANAuthentication_Type()
)
ruckusSCGConfigWLANAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGConfigWLANAuthentication.setStatus("current")


class _RuckusSCGConfigWLANEncryption_Type(Integer32):
    """Custom type ruckusSCGConfigWLANEncryption based on Integer32"""
    defaultValue = 5

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
        *(("wpa2", 1),
          ("wpa-Mixed", 2),
          ("wep-64", 3),
          ("wep-128", 4),
          ("none-enc", 5))
    )


_RuckusSCGConfigWLANEncryption_Type.__name__ = "Integer32"
_RuckusSCGConfigWLANEncryption_Object = MibTableColumn
ruckusSCGConfigWLANEncryption = _RuckusSCGConfigWLANEncryption_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 2, 1, 1, 1, 1, 12),
    _RuckusSCGConfigWLANEncryption_Type()
)
ruckusSCGConfigWLANEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusSCGConfigWLANEncryption.setStatus("current")


class _RuckusSCGConfigWLANWEPKeyIndex_Type(Integer32):
    """Custom type ruckusSCGConfigWLANWEPKeyIndex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_RuckusSCGConfigWLANWEPKeyIndex_Type.__name__ = "Integer32"
_RuckusSCGConfigWLANWEPKeyIndex_Object = MibTableColumn
ruckusSCGConfigWLANWEPKeyIndex = _RuckusSCGConfigWLANWEPKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 2, 1, 1, 1, 1, 15),
    _RuckusSCGConfigWLANWEPKeyIndex_Type()
)
ruckusSCGConfigWLANWEPKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusSCGConfigWLANWEPKeyIndex.setStatus("current")


class _RuckusSCGConfigWLANWEPKey_Type(OctetString):
    """Custom type ruckusSCGConfigWLANWEPKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
        ValueSizeConstraint(26, 26),
    )


_RuckusSCGConfigWLANWEPKey_Type.__name__ = "OctetString"
_RuckusSCGConfigWLANWEPKey_Object = MibTableColumn
ruckusSCGConfigWLANWEPKey = _RuckusSCGConfigWLANWEPKey_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 2, 1, 1, 1, 1, 16),
    _RuckusSCGConfigWLANWEPKey_Type()
)
ruckusSCGConfigWLANWEPKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusSCGConfigWLANWEPKey.setStatus("current")


class _RuckusSCGConfigWLANWPACipherType_Type(Integer32):
    """Custom type ruckusSCGConfigWLANWPACipherType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aes", 1),
          ("tkipaes", 2),
          ("null", 3))
    )


_RuckusSCGConfigWLANWPACipherType_Type.__name__ = "Integer32"
_RuckusSCGConfigWLANWPACipherType_Object = MibTableColumn
ruckusSCGConfigWLANWPACipherType = _RuckusSCGConfigWLANWPACipherType_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 2, 1, 1, 1, 1, 20),
    _RuckusSCGConfigWLANWPACipherType_Type()
)
ruckusSCGConfigWLANWPACipherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusSCGConfigWLANWPACipherType.setStatus("current")


class _RuckusSCGConfigWLANWPAKey_Type(OctetString):
    """Custom type ruckusSCGConfigWLANWPAKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 63),
        ValueSizeConstraint(64, 64),
    )


_RuckusSCGConfigWLANWPAKey_Type.__name__ = "OctetString"
_RuckusSCGConfigWLANWPAKey_Object = MibTableColumn
ruckusSCGConfigWLANWPAKey = _RuckusSCGConfigWLANWPAKey_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 2, 1, 1, 1, 1, 21),
    _RuckusSCGConfigWLANWPAKey_Type()
)
ruckusSCGConfigWLANWPAKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusSCGConfigWLANWPAKey.setStatus("current")


class _RuckusSCGConfigWLANWirelessClientIsolation_Type(Integer32):
    """Custom type ruckusSCGConfigWLANWirelessClientIsolation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RuckusSCGConfigWLANWirelessClientIsolation_Type.__name__ = "Integer32"
_RuckusSCGConfigWLANWirelessClientIsolation_Object = MibTableColumn
ruckusSCGConfigWLANWirelessClientIsolation = _RuckusSCGConfigWLANWirelessClientIsolation_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 2, 1, 1, 1, 1, 28),
    _RuckusSCGConfigWLANWirelessClientIsolation_Type()
)
ruckusSCGConfigWLANWirelessClientIsolation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusSCGConfigWLANWirelessClientIsolation.setStatus("current")


class _RuckusSCGConfigWLANZeroITActivation_Type(Integer32):
    """Custom type ruckusSCGConfigWLANZeroITActivation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RuckusSCGConfigWLANZeroITActivation_Type.__name__ = "Integer32"
_RuckusSCGConfigWLANZeroITActivation_Object = MibTableColumn
ruckusSCGConfigWLANZeroITActivation = _RuckusSCGConfigWLANZeroITActivation_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 2, 1, 1, 1, 1, 30),
    _RuckusSCGConfigWLANZeroITActivation_Type()
)
ruckusSCGConfigWLANZeroITActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusSCGConfigWLANZeroITActivation.setStatus("current")


class _RuckusSCGConfigWLANServicePriority_Type(Integer32):
    """Custom type ruckusSCGConfigWLANServicePriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 2))
    )


_RuckusSCGConfigWLANServicePriority_Type.__name__ = "Integer32"
_RuckusSCGConfigWLANServicePriority_Object = MibTableColumn
ruckusSCGConfigWLANServicePriority = _RuckusSCGConfigWLANServicePriority_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 2, 1, 1, 1, 1, 32),
    _RuckusSCGConfigWLANServicePriority_Type()
)
ruckusSCGConfigWLANServicePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusSCGConfigWLANServicePriority.setStatus("current")


class _RuckusSCGConfigWLANAccountingUpdateInterval_Type(Integer32):
    """Custom type ruckusSCGConfigWLANAccountingUpdateInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_RuckusSCGConfigWLANAccountingUpdateInterval_Type.__name__ = "Integer32"
_RuckusSCGConfigWLANAccountingUpdateInterval_Object = MibTableColumn
ruckusSCGConfigWLANAccountingUpdateInterval = _RuckusSCGConfigWLANAccountingUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 2, 1, 1, 1, 1, 36),
    _RuckusSCGConfigWLANAccountingUpdateInterval_Type()
)
ruckusSCGConfigWLANAccountingUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusSCGConfigWLANAccountingUpdateInterval.setStatus("current")


class _RuckusSCGConfigWLANVlanID_Type(Integer32):
    """Custom type ruckusSCGConfigWLANVlanID based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RuckusSCGConfigWLANVlanID_Type.__name__ = "Integer32"
_RuckusSCGConfigWLANVlanID_Object = MibTableColumn
ruckusSCGConfigWLANVlanID = _RuckusSCGConfigWLANVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 2, 1, 1, 1, 1, 45),
    _RuckusSCGConfigWLANVlanID_Type()
)
ruckusSCGConfigWLANVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusSCGConfigWLANVlanID.setStatus("current")


class _RuckusSCGConfigWLANHideSSID_Type(Integer32):
    """Custom type ruckusSCGConfigWLANHideSSID based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RuckusSCGConfigWLANHideSSID_Type.__name__ = "Integer32"
_RuckusSCGConfigWLANHideSSID_Object = MibTableColumn
ruckusSCGConfigWLANHideSSID = _RuckusSCGConfigWLANHideSSID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 2, 1, 1, 1, 1, 50),
    _RuckusSCGConfigWLANHideSSID_Type()
)
ruckusSCGConfigWLANHideSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusSCGConfigWLANHideSSID.setStatus("current")


class _RuckusSCGConfigWLANMaxClientsPerAP_Type(Integer32):
    """Custom type ruckusSCGConfigWLANMaxClientsPerAP based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_RuckusSCGConfigWLANMaxClientsPerAP_Type.__name__ = "Integer32"
_RuckusSCGConfigWLANMaxClientsPerAP_Object = MibTableColumn
ruckusSCGConfigWLANMaxClientsPerAP = _RuckusSCGConfigWLANMaxClientsPerAP_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 2, 1, 1, 1, 1, 55),
    _RuckusSCGConfigWLANMaxClientsPerAP_Type()
)
ruckusSCGConfigWLANMaxClientsPerAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusSCGConfigWLANMaxClientsPerAP.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-SCG-CONFIG-WLAN-MIB",
    **{"ruckusSCGConfigWLANMIB": ruckusSCGConfigWLANMIB,
       "ruckusSCGConfigWLANObjects": ruckusSCGConfigWLANObjects,
       "ruckusSCGConfigWLAN": ruckusSCGConfigWLAN,
       "ruckusSCGConfigWLANTable": ruckusSCGConfigWLANTable,
       "ruckusSCGConfigWLANEntry": ruckusSCGConfigWLANEntry,
       "ruckusSCGConfigWLANID": ruckusSCGConfigWLANID,
       "ruckusSCGConfigWLANSSID": ruckusSCGConfigWLANSSID,
       "ruckusSCGConfigWLANDescription": ruckusSCGConfigWLANDescription,
       "ruckusSCGConfigWLANName": ruckusSCGConfigWLANName,
       "ruckusSCGZoneName": ruckusSCGZoneName,
       "ruckusSCGConfigWLANWLANServiceType": ruckusSCGConfigWLANWLANServiceType,
       "ruckusSCGConfigWLANAuthentication": ruckusSCGConfigWLANAuthentication,
       "ruckusSCGConfigWLANEncryption": ruckusSCGConfigWLANEncryption,
       "ruckusSCGConfigWLANWEPKeyIndex": ruckusSCGConfigWLANWEPKeyIndex,
       "ruckusSCGConfigWLANWEPKey": ruckusSCGConfigWLANWEPKey,
       "ruckusSCGConfigWLANWPACipherType": ruckusSCGConfigWLANWPACipherType,
       "ruckusSCGConfigWLANWPAKey": ruckusSCGConfigWLANWPAKey,
       "ruckusSCGConfigWLANWirelessClientIsolation": ruckusSCGConfigWLANWirelessClientIsolation,
       "ruckusSCGConfigWLANZeroITActivation": ruckusSCGConfigWLANZeroITActivation,
       "ruckusSCGConfigWLANServicePriority": ruckusSCGConfigWLANServicePriority,
       "ruckusSCGConfigWLANAccountingUpdateInterval": ruckusSCGConfigWLANAccountingUpdateInterval,
       "ruckusSCGConfigWLANVlanID": ruckusSCGConfigWLANVlanID,
       "ruckusSCGConfigWLANHideSSID": ruckusSCGConfigWLANHideSSID,
       "ruckusSCGConfigWLANMaxClientsPerAP": ruckusSCGConfigWLANMaxClientsPerAP}
)
