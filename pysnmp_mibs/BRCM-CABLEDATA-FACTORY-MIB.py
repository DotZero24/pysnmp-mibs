# SNMP MIB module (BRCM-CABLEDATA-FACTORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/broadcom/BRCM-CABLEDATA-FACTORY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:08:52 2025
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

(cableDataPrivateMIBObjects,) = mibBuilder.importSymbols(
    "BRCM-CABLEDATA-PRIVATE-MIB",
    "cableDataPrivateMIBObjects")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cableDataFactory = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cableDataFactory.setRevisions(
        ("2011-05-12 00:00",
         "2007-02-05 00:00",
         "2002-06-19 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CableDataFactoryBase_ObjectIdentity = ObjectIdentity
cableDataFactoryBase = _CableDataFactoryBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 1)
)
_CdFactCommitSettings_Type = TruthValue
_CdFactCommitSettings_Object = MibScalar
cdFactCommitSettings = _CdFactCommitSettings_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 1, 1),
    _CdFactCommitSettings_Type()
)
cdFactCommitSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdFactCommitSettings.setStatus("current")
_CdFactScratchPad_Type = Unsigned32
_CdFactScratchPad_Object = MibScalar
cdFactScratchPad = _CdFactScratchPad_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 1, 2),
    _CdFactScratchPad_Type()
)
cdFactScratchPad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdFactScratchPad.setStatus("current")
_CdFactSerialNumberTable_Object = MibTable
cdFactSerialNumberTable = _CdFactSerialNumberTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    cdFactSerialNumberTable.setStatus("current")
_CdFactSerialNumberEntry_Object = MibTableRow
cdFactSerialNumberEntry = _CdFactSerialNumberEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 1, 3, 1)
)
cdFactSerialNumberEntry.setIndexNames(
    (0, "BRCM-CABLEDATA-FACTORY-MIB", "cdSerialNumIndex"),
)
if mibBuilder.loadTexts:
    cdFactSerialNumberEntry.setStatus("current")


class _CdSerialNumIndex_Type(Integer32):
    """Custom type cdSerialNumIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CdSerialNumIndex_Type.__name__ = "Integer32"
_CdSerialNumIndex_Object = MibTableColumn
cdSerialNumIndex = _CdSerialNumIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 1, 3, 1, 1),
    _CdSerialNumIndex_Type()
)
cdSerialNumIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdSerialNumIndex.setStatus("current")
_CdSerialNumber_Type = OctetString
_CdSerialNumber_Object = MibTableColumn
cdSerialNumber = _CdSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 1, 3, 1, 2),
    _CdSerialNumber_Type()
)
cdSerialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdSerialNumber.setStatus("current")
_CdSerialNumDescr_Type = DisplayString
_CdSerialNumDescr_Object = MibTableColumn
cdSerialNumDescr = _CdSerialNumDescr_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 1, 3, 1, 3),
    _CdSerialNumDescr_Type()
)
cdSerialNumDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdSerialNumDescr.setStatus("current")
_CdFactMacAddressTable_Object = MibTable
cdFactMacAddressTable = _CdFactMacAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 1, 4)
)
if mibBuilder.loadTexts:
    cdFactMacAddressTable.setStatus("current")
_CdFactMacAddressEntry_Object = MibTableRow
cdFactMacAddressEntry = _CdFactMacAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 1, 4, 1)
)
cdFactMacAddressEntry.setIndexNames(
    (0, "BRCM-CABLEDATA-FACTORY-MIB", "cdMacAddrIndex"),
)
if mibBuilder.loadTexts:
    cdFactMacAddressEntry.setStatus("current")


class _CdMacAddrIndex_Type(Integer32):
    """Custom type cdMacAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CdMacAddrIndex_Type.__name__ = "Integer32"
_CdMacAddrIndex_Object = MibTableColumn
cdMacAddrIndex = _CdMacAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 1, 4, 1, 1),
    _CdMacAddrIndex_Type()
)
cdMacAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdMacAddrIndex.setStatus("current")
_CdMacAddress_Type = MacAddress
_CdMacAddress_Object = MibTableColumn
cdMacAddress = _CdMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 1, 4, 1, 2),
    _CdMacAddress_Type()
)
cdMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdMacAddress.setStatus("current")


class _CdMacAddrType_Type(Integer32):
    """Custom type cdMacAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("external", 2))
    )


_CdMacAddrType_Type.__name__ = "Integer32"
_CdMacAddrType_Object = MibTableColumn
cdMacAddrType = _CdMacAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 1, 4, 1, 3),
    _CdMacAddrType_Type()
)
cdMacAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdMacAddrType.setStatus("current")
_CdMacAddrDescr_Type = DisplayString
_CdMacAddrDescr_Object = MibTableColumn
cdMacAddrDescr = _CdMacAddrDescr_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 1, 4, 1, 4),
    _CdMacAddrDescr_Type()
)
cdMacAddrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdMacAddrDescr.setStatus("current")
_CdFactIpSettingsTable_Object = MibTable
cdFactIpSettingsTable = _CdFactIpSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 1, 5)
)
if mibBuilder.loadTexts:
    cdFactIpSettingsTable.setStatus("current")
_CdFactIpSettingsEntry_Object = MibTableRow
cdFactIpSettingsEntry = _CdFactIpSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 1, 5, 1)
)
cdFactIpSettingsEntry.setIndexNames(
    (0, "BRCM-CABLEDATA-FACTORY-MIB", "cdMacAddrIndex"),
)
if mibBuilder.loadTexts:
    cdFactIpSettingsEntry.setStatus("current")
_CdIpDescr_Type = DisplayString
_CdIpDescr_Object = MibTableColumn
cdIpDescr = _CdIpDescr_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 1, 5, 1, 1),
    _CdIpDescr_Type()
)
cdIpDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdIpDescr.setStatus("current")


class _CdIpProvMethod_Type(Integer32):
    """Custom type cdIpProvMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("static", 0),
          ("dynamic", 1))
    )


_CdIpProvMethod_Type.__name__ = "Integer32"
_CdIpProvMethod_Object = MibTableColumn
cdIpProvMethod = _CdIpProvMethod_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 1, 5, 1, 2),
    _CdIpProvMethod_Type()
)
cdIpProvMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdIpProvMethod.setStatus("current")
_CdIpStaticAddress_Type = IpAddress
_CdIpStaticAddress_Object = MibTableColumn
cdIpStaticAddress = _CdIpStaticAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 1, 5, 1, 3),
    _CdIpStaticAddress_Type()
)
cdIpStaticAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdIpStaticAddress.setStatus("current")
_CdIpStaticSubnet_Type = IpAddress
_CdIpStaticSubnet_Object = MibTableColumn
cdIpStaticSubnet = _CdIpStaticSubnet_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 1, 5, 1, 4),
    _CdIpStaticSubnet_Type()
)
cdIpStaticSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdIpStaticSubnet.setStatus("current")
_CdIpStaticGateway_Type = IpAddress
_CdIpStaticGateway_Object = MibTableColumn
cdIpStaticGateway = _CdIpStaticGateway_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 1, 5, 1, 5),
    _CdIpStaticGateway_Type()
)
cdIpStaticGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdIpStaticGateway.setStatus("current")


class _CdFactNonVolOperStatus_Type(Integer32):
    """Custom type cdFactNonVolOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("readPending", 1),
          ("reading", 2),
          ("writePending", 3),
          ("writing", 4))
    )


_CdFactNonVolOperStatus_Type.__name__ = "Integer32"
_CdFactNonVolOperStatus_Object = MibScalar
cdFactNonVolOperStatus = _CdFactNonVolOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 1, 6),
    _CdFactNonVolOperStatus_Type()
)
cdFactNonVolOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdFactNonVolOperStatus.setStatus("current")
_CableDataFactoryVendor_ObjectIdentity = ObjectIdentity
cableDataFactoryVendor = _CableDataFactoryVendor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 99)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BRCM-CABLEDATA-FACTORY-MIB",
    **{"cableDataFactory": cableDataFactory,
       "cableDataFactoryBase": cableDataFactoryBase,
       "cdFactCommitSettings": cdFactCommitSettings,
       "cdFactScratchPad": cdFactScratchPad,
       "cdFactSerialNumberTable": cdFactSerialNumberTable,
       "cdFactSerialNumberEntry": cdFactSerialNumberEntry,
       "cdSerialNumIndex": cdSerialNumIndex,
       "cdSerialNumber": cdSerialNumber,
       "cdSerialNumDescr": cdSerialNumDescr,
       "cdFactMacAddressTable": cdFactMacAddressTable,
       "cdFactMacAddressEntry": cdFactMacAddressEntry,
       "cdMacAddrIndex": cdMacAddrIndex,
       "cdMacAddress": cdMacAddress,
       "cdMacAddrType": cdMacAddrType,
       "cdMacAddrDescr": cdMacAddrDescr,
       "cdFactIpSettingsTable": cdFactIpSettingsTable,
       "cdFactIpSettingsEntry": cdFactIpSettingsEntry,
       "cdIpDescr": cdIpDescr,
       "cdIpProvMethod": cdIpProvMethod,
       "cdIpStaticAddress": cdIpStaticAddress,
       "cdIpStaticSubnet": cdIpStaticSubnet,
       "cdIpStaticGateway": cdIpStaticGateway,
       "cdFactNonVolOperStatus": cdFactNonVolOperStatus,
       "cableDataFactoryVendor": cableDataFactoryVendor}
)
