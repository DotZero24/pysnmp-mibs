# SNMP MIB module (NEWTEC-ETHERNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-ETHERNET-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:04:00 2025
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

(ntcFunction,) = mibBuilder.importSymbols(
    "NEWTEC-MAIN-MIB",
    "ntcFunction")

(NtcAlarmState,
 NtcEnable) = mibBuilder.importSymbols(
    "NEWTEC-TC-MIB",
    "NtcAlarmState",
    "NtcEnable")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ntcEthernet = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500)
)
if mibBuilder.loadTexts:
    ntcEthernet.setRevisions(
        ("2018-02-02 09:00",
         "2017-07-10 12:00",
         "2014-11-24 12:00",
         "2013-05-22 06:00",
         "2013-03-27 10:00",
         "2013-01-08 12:00",
         "2012-06-28 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcEtherObjects_ObjectIdentity = ObjectIdentity
ntcEtherObjects = _NtcEtherObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1)
)
if mibBuilder.loadTexts:
    ntcEtherObjects.setStatus("current")
_NtcEtherLinkMgmtTable_Object = MibTable
ntcEtherLinkMgmtTable = _NtcEtherLinkMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 1)
)
if mibBuilder.loadTexts:
    ntcEtherLinkMgmtTable.setStatus("current")
_NtcEtherLinkMgmtEntry_Object = MibTableRow
ntcEtherLinkMgmtEntry = _NtcEtherLinkMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 1, 1)
)
ntcEtherLinkMgmtEntry.setIndexNames(
    (0, "NEWTEC-ETHERNET-MIB", "ntcEtherLinkMgmtInterface"),
)
if mibBuilder.loadTexts:
    ntcEtherLinkMgmtEntry.setStatus("current")


class _NtcEtherLinkMgmtInterface_Type(Integer32):
    """Custom type ntcEtherLinkMgmtInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mgmt1", 0),
          ("mgmt2", 1),
          ("mgmtfp", 2))
    )


_NtcEtherLinkMgmtInterface_Type.__name__ = "Integer32"
_NtcEtherLinkMgmtInterface_Object = MibTableColumn
ntcEtherLinkMgmtInterface = _NtcEtherLinkMgmtInterface_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 1, 1, 1),
    _NtcEtherLinkMgmtInterface_Type()
)
ntcEtherLinkMgmtInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcEtherLinkMgmtInterface.setStatus("current")


class _NtcEtherLinkMgmtEnable_Type(NtcEnable):
    """Custom type ntcEtherLinkMgmtEnable based on NtcEnable"""
    defaultValue = 0


_NtcEtherLinkMgmtEnable_Type.__name__ = "NtcEnable"
_NtcEtherLinkMgmtEnable_Object = MibTableColumn
ntcEtherLinkMgmtEnable = _NtcEtherLinkMgmtEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 1, 1, 2),
    _NtcEtherLinkMgmtEnable_Type()
)
ntcEtherLinkMgmtEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcEtherLinkMgmtEnable.setStatus("current")
_NtcEtherLinkMgmtMacAddress_Type = MacAddress
_NtcEtherLinkMgmtMacAddress_Object = MibTableColumn
ntcEtherLinkMgmtMacAddress = _NtcEtherLinkMgmtMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 1, 1, 3),
    _NtcEtherLinkMgmtMacAddress_Type()
)
ntcEtherLinkMgmtMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcEtherLinkMgmtMacAddress.setStatus("current")


class _NtcEtherLinkMgmtAutoNegotiation_Type(NtcEnable):
    """Custom type ntcEtherLinkMgmtAutoNegotiation based on NtcEnable"""
    defaultValue = 1


_NtcEtherLinkMgmtAutoNegotiation_Type.__name__ = "NtcEnable"
_NtcEtherLinkMgmtAutoNegotiation_Object = MibTableColumn
ntcEtherLinkMgmtAutoNegotiation = _NtcEtherLinkMgmtAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 1, 1, 4),
    _NtcEtherLinkMgmtAutoNegotiation_Type()
)
ntcEtherLinkMgmtAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcEtherLinkMgmtAutoNegotiation.setStatus("current")


class _NtcEtherLinkMgmtAdvertisedSpeeds_Type(Integer32):
    """Custom type ntcEtherLinkMgmtAdvertisedSpeeds based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("all", 0),
          ("e10BTHalfDuplex", 1),
          ("e10BTFullDuplex", 2),
          ("e100BTHalfDuplex", 3),
          ("e100BTFullDuplex", 4),
          ("e1000BTFullDuplex", 5))
    )


_NtcEtherLinkMgmtAdvertisedSpeeds_Type.__name__ = "Integer32"
_NtcEtherLinkMgmtAdvertisedSpeeds_Object = MibTableColumn
ntcEtherLinkMgmtAdvertisedSpeeds = _NtcEtherLinkMgmtAdvertisedSpeeds_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 1, 1, 5),
    _NtcEtherLinkMgmtAdvertisedSpeeds_Type()
)
ntcEtherLinkMgmtAdvertisedSpeeds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcEtherLinkMgmtAdvertisedSpeeds.setStatus("current")


class _NtcEtherLinkMgmtForcedSpeed_Type(Integer32):
    """Custom type ntcEtherLinkMgmtForcedSpeed based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("e10BTHalfDuplex", 1),
          ("e10BTFullDuplex", 2),
          ("e100BTHalfDuplex", 3),
          ("e100BTFullDuplex", 4))
    )


_NtcEtherLinkMgmtForcedSpeed_Type.__name__ = "Integer32"
_NtcEtherLinkMgmtForcedSpeed_Object = MibTableColumn
ntcEtherLinkMgmtForcedSpeed = _NtcEtherLinkMgmtForcedSpeed_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 1, 1, 6),
    _NtcEtherLinkMgmtForcedSpeed_Type()
)
ntcEtherLinkMgmtForcedSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcEtherLinkMgmtForcedSpeed.setStatus("current")


class _NtcEtherLinkMgmtLinkState_Type(Integer32):
    """Custom type ntcEtherLinkMgmtLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 0),
          ("e10BTHalfDuplex", 1),
          ("e10BTFullDuplex", 2),
          ("e100BTHalfDuplex", 3),
          ("e100BTFullDuplex", 4),
          ("e1000BTFullDuplex", 5),
          ("e10GSFPplus", 6))
    )


_NtcEtherLinkMgmtLinkState_Type.__name__ = "Integer32"
_NtcEtherLinkMgmtLinkState_Object = MibTableColumn
ntcEtherLinkMgmtLinkState = _NtcEtherLinkMgmtLinkState_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 1, 1, 7),
    _NtcEtherLinkMgmtLinkState_Type()
)
ntcEtherLinkMgmtLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcEtherLinkMgmtLinkState.setStatus("current")


class _NtcEtherLinkMgmtMtu_Type(Unsigned32):
    """Custom type ntcEtherLinkMgmtMtu based on Unsigned32"""
    defaultValue = 1500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(68, 9216),
    )


_NtcEtherLinkMgmtMtu_Type.__name__ = "Unsigned32"
_NtcEtherLinkMgmtMtu_Object = MibTableColumn
ntcEtherLinkMgmtMtu = _NtcEtherLinkMgmtMtu_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 1, 1, 8),
    _NtcEtherLinkMgmtMtu_Type()
)
ntcEtherLinkMgmtMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcEtherLinkMgmtMtu.setStatus("current")
_NtcEtherLinkDataTable_Object = MibTable
ntcEtherLinkDataTable = _NtcEtherLinkDataTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 2)
)
if mibBuilder.loadTexts:
    ntcEtherLinkDataTable.setStatus("current")
_NtcEtherLinkDataEntry_Object = MibTableRow
ntcEtherLinkDataEntry = _NtcEtherLinkDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 2, 1)
)
ntcEtherLinkDataEntry.setIndexNames(
    (0, "NEWTEC-ETHERNET-MIB", "ntcEtherLinkDataInterface"),
)
if mibBuilder.loadTexts:
    ntcEtherLinkDataEntry.setStatus("current")


class _NtcEtherLinkDataInterface_Type(Integer32):
    """Custom type ntcEtherLinkDataInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("data1", 0),
          ("data2", 1),
          ("sat1", 2),
          ("sat2", 3))
    )


_NtcEtherLinkDataInterface_Type.__name__ = "Integer32"
_NtcEtherLinkDataInterface_Object = MibTableColumn
ntcEtherLinkDataInterface = _NtcEtherLinkDataInterface_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 2, 1, 1),
    _NtcEtherLinkDataInterface_Type()
)
ntcEtherLinkDataInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcEtherLinkDataInterface.setStatus("current")


class _NtcEtherLinkDataEnable_Type(NtcEnable):
    """Custom type ntcEtherLinkDataEnable based on NtcEnable"""
    defaultValue = 0


_NtcEtherLinkDataEnable_Type.__name__ = "NtcEnable"
_NtcEtherLinkDataEnable_Object = MibTableColumn
ntcEtherLinkDataEnable = _NtcEtherLinkDataEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 2, 1, 2),
    _NtcEtherLinkDataEnable_Type()
)
ntcEtherLinkDataEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcEtherLinkDataEnable.setStatus("current")
_NtcEtherLinkDataMacAddress_Type = MacAddress
_NtcEtherLinkDataMacAddress_Object = MibTableColumn
ntcEtherLinkDataMacAddress = _NtcEtherLinkDataMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 2, 1, 3),
    _NtcEtherLinkDataMacAddress_Type()
)
ntcEtherLinkDataMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcEtherLinkDataMacAddress.setStatus("current")


class _NtcEtherLinkDataAutoNegotiation_Type(NtcEnable):
    """Custom type ntcEtherLinkDataAutoNegotiation based on NtcEnable"""
    defaultValue = 1


_NtcEtherLinkDataAutoNegotiation_Type.__name__ = "NtcEnable"
_NtcEtherLinkDataAutoNegotiation_Object = MibTableColumn
ntcEtherLinkDataAutoNegotiation = _NtcEtherLinkDataAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 2, 1, 4),
    _NtcEtherLinkDataAutoNegotiation_Type()
)
ntcEtherLinkDataAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcEtherLinkDataAutoNegotiation.setStatus("current")


class _NtcEtherLinkDataAdvertisedSpeeds_Type(Integer32):
    """Custom type ntcEtherLinkDataAdvertisedSpeeds based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("all", 0),
          ("e10BTHalfDuplex", 1),
          ("e10BTFullDuplex", 2),
          ("e100BTHalfDuplex", 3),
          ("e100BTFullDuplex", 4),
          ("e1000BTFullDuplex", 5))
    )


_NtcEtherLinkDataAdvertisedSpeeds_Type.__name__ = "Integer32"
_NtcEtherLinkDataAdvertisedSpeeds_Object = MibTableColumn
ntcEtherLinkDataAdvertisedSpeeds = _NtcEtherLinkDataAdvertisedSpeeds_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 2, 1, 5),
    _NtcEtherLinkDataAdvertisedSpeeds_Type()
)
ntcEtherLinkDataAdvertisedSpeeds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcEtherLinkDataAdvertisedSpeeds.setStatus("current")


class _NtcEtherLinkDataForcedSpeed_Type(Integer32):
    """Custom type ntcEtherLinkDataForcedSpeed based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("e10BTHalfDuplex", 1),
          ("e10BTFullDuplex", 2),
          ("e100BTHalfDuplex", 3),
          ("e100BTFullDuplex", 4))
    )


_NtcEtherLinkDataForcedSpeed_Type.__name__ = "Integer32"
_NtcEtherLinkDataForcedSpeed_Object = MibTableColumn
ntcEtherLinkDataForcedSpeed = _NtcEtherLinkDataForcedSpeed_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 2, 1, 6),
    _NtcEtherLinkDataForcedSpeed_Type()
)
ntcEtherLinkDataForcedSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcEtherLinkDataForcedSpeed.setStatus("current")


class _NtcEtherLinkDataLinkState_Type(Integer32):
    """Custom type ntcEtherLinkDataLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 0),
          ("e10BTHalfDuplex", 1),
          ("e10BTFullDuplex", 2),
          ("e100BTHalfDuplex", 3),
          ("e100BTFullDuplex", 4),
          ("e1000BTFullDuplex", 5),
          ("e10GSFPplus", 6))
    )


_NtcEtherLinkDataLinkState_Type.__name__ = "Integer32"
_NtcEtherLinkDataLinkState_Object = MibTableColumn
ntcEtherLinkDataLinkState = _NtcEtherLinkDataLinkState_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 2, 1, 7),
    _NtcEtherLinkDataLinkState_Type()
)
ntcEtherLinkDataLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcEtherLinkDataLinkState.setStatus("current")


class _NtcEtherLinkDataMtu_Type(Unsigned32):
    """Custom type ntcEtherLinkDataMtu based on Unsigned32"""
    defaultValue = 1500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(68, 9216),
    )


_NtcEtherLinkDataMtu_Type.__name__ = "Unsigned32"
_NtcEtherLinkDataMtu_Object = MibTableColumn
ntcEtherLinkDataMtu = _NtcEtherLinkDataMtu_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 2, 1, 8),
    _NtcEtherLinkDataMtu_Type()
)
ntcEtherLinkDataMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcEtherLinkDataMtu.setStatus("current")
_NtcEtherStatMgmtTable_Object = MibTable
ntcEtherStatMgmtTable = _NtcEtherStatMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 3)
)
if mibBuilder.loadTexts:
    ntcEtherStatMgmtTable.setStatus("current")
_NtcEtherStatMgmtEntry_Object = MibTableRow
ntcEtherStatMgmtEntry = _NtcEtherStatMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 3, 1)
)
ntcEtherStatMgmtEntry.setIndexNames(
    (0, "NEWTEC-ETHERNET-MIB", "ntcEtherStatMgmtInterface"),
)
if mibBuilder.loadTexts:
    ntcEtherStatMgmtEntry.setStatus("current")


class _NtcEtherStatMgmtInterface_Type(Integer32):
    """Custom type ntcEtherStatMgmtInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mgmt1", 0),
          ("mgmt2", 1),
          ("mgmtfp", 2),
          ("mgmtbond", 3))
    )


_NtcEtherStatMgmtInterface_Type.__name__ = "Integer32"
_NtcEtherStatMgmtInterface_Object = MibTableColumn
ntcEtherStatMgmtInterface = _NtcEtherStatMgmtInterface_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 3, 1, 1),
    _NtcEtherStatMgmtInterface_Type()
)
ntcEtherStatMgmtInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcEtherStatMgmtInterface.setStatus("current")
_NtcEtherStatMgmtInputBytes_Type = Counter32
_NtcEtherStatMgmtInputBytes_Object = MibTableColumn
ntcEtherStatMgmtInputBytes = _NtcEtherStatMgmtInputBytes_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 3, 1, 2),
    _NtcEtherStatMgmtInputBytes_Type()
)
ntcEtherStatMgmtInputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcEtherStatMgmtInputBytes.setStatus("current")
if mibBuilder.loadTexts:
    ntcEtherStatMgmtInputBytes.setUnits("bytes")
_NtcEtherStatMgmtInputPackets_Type = Counter32
_NtcEtherStatMgmtInputPackets_Object = MibTableColumn
ntcEtherStatMgmtInputPackets = _NtcEtherStatMgmtInputPackets_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 3, 1, 3),
    _NtcEtherStatMgmtInputPackets_Type()
)
ntcEtherStatMgmtInputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcEtherStatMgmtInputPackets.setStatus("current")
if mibBuilder.loadTexts:
    ntcEtherStatMgmtInputPackets.setUnits("packets")
_NtcEtherStatMgmtInputDropped_Type = Counter32
_NtcEtherStatMgmtInputDropped_Object = MibTableColumn
ntcEtherStatMgmtInputDropped = _NtcEtherStatMgmtInputDropped_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 3, 1, 4),
    _NtcEtherStatMgmtInputDropped_Type()
)
ntcEtherStatMgmtInputDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcEtherStatMgmtInputDropped.setStatus("current")
if mibBuilder.loadTexts:
    ntcEtherStatMgmtInputDropped.setUnits("packets")
_NtcEtherStatMgmtOutputBytes_Type = Counter32
_NtcEtherStatMgmtOutputBytes_Object = MibTableColumn
ntcEtherStatMgmtOutputBytes = _NtcEtherStatMgmtOutputBytes_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 3, 1, 5),
    _NtcEtherStatMgmtOutputBytes_Type()
)
ntcEtherStatMgmtOutputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcEtherStatMgmtOutputBytes.setStatus("current")
if mibBuilder.loadTexts:
    ntcEtherStatMgmtOutputBytes.setUnits("bytes")
_NtcEtherStatMgmtOutputPackets_Type = Counter32
_NtcEtherStatMgmtOutputPackets_Object = MibTableColumn
ntcEtherStatMgmtOutputPackets = _NtcEtherStatMgmtOutputPackets_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 3, 1, 6),
    _NtcEtherStatMgmtOutputPackets_Type()
)
ntcEtherStatMgmtOutputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcEtherStatMgmtOutputPackets.setStatus("current")
if mibBuilder.loadTexts:
    ntcEtherStatMgmtOutputPackets.setUnits("packets")
_NtcEtherStatMgmtOutputDropped_Type = Counter32
_NtcEtherStatMgmtOutputDropped_Object = MibTableColumn
ntcEtherStatMgmtOutputDropped = _NtcEtherStatMgmtOutputDropped_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 3, 1, 7),
    _NtcEtherStatMgmtOutputDropped_Type()
)
ntcEtherStatMgmtOutputDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcEtherStatMgmtOutputDropped.setStatus("current")
if mibBuilder.loadTexts:
    ntcEtherStatMgmtOutputDropped.setUnits("packets")
_NtcEtherStatMgmtInputErrors_Type = Counter64
_NtcEtherStatMgmtInputErrors_Object = MibTableColumn
ntcEtherStatMgmtInputErrors = _NtcEtherStatMgmtInputErrors_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 3, 1, 8),
    _NtcEtherStatMgmtInputErrors_Type()
)
ntcEtherStatMgmtInputErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcEtherStatMgmtInputErrors.setStatus("current")
if mibBuilder.loadTexts:
    ntcEtherStatMgmtInputErrors.setUnits("packets")
_NtcEtherStatMgmtOutputerrors_Type = Counter64
_NtcEtherStatMgmtOutputerrors_Object = MibTableColumn
ntcEtherStatMgmtOutputerrors = _NtcEtherStatMgmtOutputerrors_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 3, 1, 9),
    _NtcEtherStatMgmtOutputerrors_Type()
)
ntcEtherStatMgmtOutputerrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcEtherStatMgmtOutputerrors.setStatus("current")
if mibBuilder.loadTexts:
    ntcEtherStatMgmtOutputerrors.setUnits("packets")
_NtcEtherStatDataTable_Object = MibTable
ntcEtherStatDataTable = _NtcEtherStatDataTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 4)
)
if mibBuilder.loadTexts:
    ntcEtherStatDataTable.setStatus("current")
_NtcEtherStatDataEntry_Object = MibTableRow
ntcEtherStatDataEntry = _NtcEtherStatDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 4, 1)
)
ntcEtherStatDataEntry.setIndexNames(
    (0, "NEWTEC-ETHERNET-MIB", "ntcEtherStatDataInterface"),
)
if mibBuilder.loadTexts:
    ntcEtherStatDataEntry.setStatus("current")


class _NtcEtherStatDataInterface_Type(Integer32):
    """Custom type ntcEtherStatDataInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("data1", 0),
          ("data2", 1),
          ("databond", 2),
          ("sat1", 3),
          ("sat2", 4),
          ("satbond", 5))
    )


_NtcEtherStatDataInterface_Type.__name__ = "Integer32"
_NtcEtherStatDataInterface_Object = MibTableColumn
ntcEtherStatDataInterface = _NtcEtherStatDataInterface_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 4, 1, 1),
    _NtcEtherStatDataInterface_Type()
)
ntcEtherStatDataInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcEtherStatDataInterface.setStatus("current")
_NtcEtherStatDataInputBytes_Type = Counter32
_NtcEtherStatDataInputBytes_Object = MibTableColumn
ntcEtherStatDataInputBytes = _NtcEtherStatDataInputBytes_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 4, 1, 2),
    _NtcEtherStatDataInputBytes_Type()
)
ntcEtherStatDataInputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcEtherStatDataInputBytes.setStatus("current")
if mibBuilder.loadTexts:
    ntcEtherStatDataInputBytes.setUnits("bytes")
_NtcEtherStatDataInputPackets_Type = Counter32
_NtcEtherStatDataInputPackets_Object = MibTableColumn
ntcEtherStatDataInputPackets = _NtcEtherStatDataInputPackets_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 4, 1, 3),
    _NtcEtherStatDataInputPackets_Type()
)
ntcEtherStatDataInputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcEtherStatDataInputPackets.setStatus("current")
if mibBuilder.loadTexts:
    ntcEtherStatDataInputPackets.setUnits("packets")
_NtcEtherStatDataInputDropped_Type = Counter32
_NtcEtherStatDataInputDropped_Object = MibTableColumn
ntcEtherStatDataInputDropped = _NtcEtherStatDataInputDropped_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 4, 1, 4),
    _NtcEtherStatDataInputDropped_Type()
)
ntcEtherStatDataInputDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcEtherStatDataInputDropped.setStatus("current")
if mibBuilder.loadTexts:
    ntcEtherStatDataInputDropped.setUnits("packets")
_NtcEtherStatDataOutputBytes_Type = Counter32
_NtcEtherStatDataOutputBytes_Object = MibTableColumn
ntcEtherStatDataOutputBytes = _NtcEtherStatDataOutputBytes_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 4, 1, 5),
    _NtcEtherStatDataOutputBytes_Type()
)
ntcEtherStatDataOutputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcEtherStatDataOutputBytes.setStatus("current")
if mibBuilder.loadTexts:
    ntcEtherStatDataOutputBytes.setUnits("bytes")
_NtcEtherStatDataOutputPackets_Type = Counter32
_NtcEtherStatDataOutputPackets_Object = MibTableColumn
ntcEtherStatDataOutputPackets = _NtcEtherStatDataOutputPackets_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 4, 1, 6),
    _NtcEtherStatDataOutputPackets_Type()
)
ntcEtherStatDataOutputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcEtherStatDataOutputPackets.setStatus("current")
if mibBuilder.loadTexts:
    ntcEtherStatDataOutputPackets.setUnits("packets")
_NtcEtherStatDataOutputDropped_Type = Counter32
_NtcEtherStatDataOutputDropped_Object = MibTableColumn
ntcEtherStatDataOutputDropped = _NtcEtherStatDataOutputDropped_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 4, 1, 7),
    _NtcEtherStatDataOutputDropped_Type()
)
ntcEtherStatDataOutputDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcEtherStatDataOutputDropped.setStatus("current")
if mibBuilder.loadTexts:
    ntcEtherStatDataOutputDropped.setUnits("packets")
_NtcEtherStatDataInputErrors_Type = Counter64
_NtcEtherStatDataInputErrors_Object = MibTableColumn
ntcEtherStatDataInputErrors = _NtcEtherStatDataInputErrors_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 4, 1, 8),
    _NtcEtherStatDataInputErrors_Type()
)
ntcEtherStatDataInputErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcEtherStatDataInputErrors.setStatus("current")
if mibBuilder.loadTexts:
    ntcEtherStatDataInputErrors.setUnits("packets")
_NtcEtherStatDataOutputerrors_Type = Counter64
_NtcEtherStatDataOutputerrors_Object = MibTableColumn
ntcEtherStatDataOutputerrors = _NtcEtherStatDataOutputerrors_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 4, 1, 9),
    _NtcEtherStatDataOutputerrors_Type()
)
ntcEtherStatDataOutputerrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcEtherStatDataOutputerrors.setStatus("current")
if mibBuilder.loadTexts:
    ntcEtherStatDataOutputerrors.setUnits("packets")
_NtcEtherInterfaceRedundancy_ObjectIdentity = ObjectIdentity
ntcEtherInterfaceRedundancy = _NtcEtherInterfaceRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 5)
)
if mibBuilder.loadTexts:
    ntcEtherInterfaceRedundancy.setStatus("current")
_NtcEtherIfRedMgmt_ObjectIdentity = ObjectIdentity
ntcEtherIfRedMgmt = _NtcEtherIfRedMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ntcEtherIfRedMgmt.setStatus("current")


class _NtcEtherIfRedMgmtSwitchOrder_Type(Integer32):
    """Custom type ntcEtherIfRedMgmtSwitchOrder based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("mgmt1or2", 1),
          ("mgmt1before2", 2),
          ("mgmt2before1", 3))
    )


_NtcEtherIfRedMgmtSwitchOrder_Type.__name__ = "Integer32"
_NtcEtherIfRedMgmtSwitchOrder_Object = MibScalar
ntcEtherIfRedMgmtSwitchOrder = _NtcEtherIfRedMgmtSwitchOrder_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 5, 1, 1),
    _NtcEtherIfRedMgmtSwitchOrder_Type()
)
ntcEtherIfRedMgmtSwitchOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcEtherIfRedMgmtSwitchOrder.setStatus("current")
_NtcEtherIfRedMgmtSwitchCount_Type = Counter32
_NtcEtherIfRedMgmtSwitchCount_Object = MibScalar
ntcEtherIfRedMgmtSwitchCount = _NtcEtherIfRedMgmtSwitchCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 5, 1, 2),
    _NtcEtherIfRedMgmtSwitchCount_Type()
)
ntcEtherIfRedMgmtSwitchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcEtherIfRedMgmtSwitchCount.setStatus("current")


class _NtcEtherIfRedMgmtActiveInterface_Type(Integer32):
    """Custom type ntcEtherIfRedMgmtActiveInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("mgmt1", 1),
          ("mgmt2", 2),
          ("na", 3))
    )


_NtcEtherIfRedMgmtActiveInterface_Type.__name__ = "Integer32"
_NtcEtherIfRedMgmtActiveInterface_Object = MibScalar
ntcEtherIfRedMgmtActiveInterface = _NtcEtherIfRedMgmtActiveInterface_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 5, 1, 3),
    _NtcEtherIfRedMgmtActiveInterface_Type()
)
ntcEtherIfRedMgmtActiveInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcEtherIfRedMgmtActiveInterface.setStatus("current")
_NtcEtherIfRedData_ObjectIdentity = ObjectIdentity
ntcEtherIfRedData = _NtcEtherIfRedData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 5, 2)
)
if mibBuilder.loadTexts:
    ntcEtherIfRedData.setStatus("current")


class _NtcEtherIfRedDataSwitchOrder_Type(Integer32):
    """Custom type ntcEtherIfRedDataSwitchOrder based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("data1or2", 1),
          ("data1before2", 2),
          ("data2before1", 3),
          ("data1", 4),
          ("data2", 5))
    )


_NtcEtherIfRedDataSwitchOrder_Type.__name__ = "Integer32"
_NtcEtherIfRedDataSwitchOrder_Object = MibScalar
ntcEtherIfRedDataSwitchOrder = _NtcEtherIfRedDataSwitchOrder_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 5, 2, 1),
    _NtcEtherIfRedDataSwitchOrder_Type()
)
ntcEtherIfRedDataSwitchOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcEtherIfRedDataSwitchOrder.setStatus("current")
_NtcEtherIfRedDataSwitchCount_Type = Counter32
_NtcEtherIfRedDataSwitchCount_Object = MibScalar
ntcEtherIfRedDataSwitchCount = _NtcEtherIfRedDataSwitchCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 5, 2, 2),
    _NtcEtherIfRedDataSwitchCount_Type()
)
ntcEtherIfRedDataSwitchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcEtherIfRedDataSwitchCount.setStatus("current")


class _NtcEtherIfRedDataActiveInterface_Type(Integer32):
    """Custom type ntcEtherIfRedDataActiveInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("data1", 1),
          ("data2", 2),
          ("na", 3))
    )


_NtcEtherIfRedDataActiveInterface_Type.__name__ = "Integer32"
_NtcEtherIfRedDataActiveInterface_Object = MibScalar
ntcEtherIfRedDataActiveInterface = _NtcEtherIfRedDataActiveInterface_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 5, 2, 3),
    _NtcEtherIfRedDataActiveInterface_Type()
)
ntcEtherIfRedDataActiveInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcEtherIfRedDataActiveInterface.setStatus("current")


class _NtcEtherIfRedDataGwUnreachImpact_Type(Integer32):
    """Custom type ntcEtherIfRedDataGwUnreachImpact based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noImpact", 0),
          ("linkRedundancyTrigger", 1))
    )


_NtcEtherIfRedDataGwUnreachImpact_Type.__name__ = "Integer32"
_NtcEtherIfRedDataGwUnreachImpact_Object = MibScalar
ntcEtherIfRedDataGwUnreachImpact = _NtcEtherIfRedDataGwUnreachImpact_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 5, 2, 4),
    _NtcEtherIfRedDataGwUnreachImpact_Type()
)
ntcEtherIfRedDataGwUnreachImpact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcEtherIfRedDataGwUnreachImpact.setStatus("current")
_NtcEtherIfRedSat_ObjectIdentity = ObjectIdentity
ntcEtherIfRedSat = _NtcEtherIfRedSat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 5, 3)
)
if mibBuilder.loadTexts:
    ntcEtherIfRedSat.setStatus("current")


class _NtcEtherIfRedSatSwitchOrder_Type(Integer32):
    """Custom type ntcEtherIfRedSatSwitchOrder based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("sat1or2", 1),
          ("sat1before2", 2),
          ("sat2before1", 3),
          ("sat1", 4),
          ("sat2", 5))
    )


_NtcEtherIfRedSatSwitchOrder_Type.__name__ = "Integer32"
_NtcEtherIfRedSatSwitchOrder_Object = MibScalar
ntcEtherIfRedSatSwitchOrder = _NtcEtherIfRedSatSwitchOrder_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 5, 3, 1),
    _NtcEtherIfRedSatSwitchOrder_Type()
)
ntcEtherIfRedSatSwitchOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcEtherIfRedSatSwitchOrder.setStatus("current")
_NtcEtherIfRedSatSwitchCount_Type = Counter32
_NtcEtherIfRedSatSwitchCount_Object = MibScalar
ntcEtherIfRedSatSwitchCount = _NtcEtherIfRedSatSwitchCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 5, 3, 2),
    _NtcEtherIfRedSatSwitchCount_Type()
)
ntcEtherIfRedSatSwitchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcEtherIfRedSatSwitchCount.setStatus("current")


class _NtcEtherIfRedSatActiveInterface_Type(Integer32):
    """Custom type ntcEtherIfRedSatActiveInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("sat1", 1),
          ("sat2", 2),
          ("na", 3))
    )


_NtcEtherIfRedSatActiveInterface_Type.__name__ = "Integer32"
_NtcEtherIfRedSatActiveInterface_Object = MibScalar
ntcEtherIfRedSatActiveInterface = _NtcEtherIfRedSatActiveInterface_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 5, 3, 3),
    _NtcEtherIfRedSatActiveInterface_Type()
)
ntcEtherIfRedSatActiveInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcEtherIfRedSatActiveInterface.setStatus("current")
_NtcEtherAlarm_ObjectIdentity = ObjectIdentity
ntcEtherAlarm = _NtcEtherAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 6)
)
if mibBuilder.loadTexts:
    ntcEtherAlarm.setStatus("current")
_NtcEtherAlmMgmt1EthLinkFail_Type = NtcAlarmState
_NtcEtherAlmMgmt1EthLinkFail_Object = MibScalar
ntcEtherAlmMgmt1EthLinkFail = _NtcEtherAlmMgmt1EthLinkFail_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 6, 1),
    _NtcEtherAlmMgmt1EthLinkFail_Type()
)
ntcEtherAlmMgmt1EthLinkFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcEtherAlmMgmt1EthLinkFail.setStatus("current")
_NtcEtherAlmMgmt1EthHalfDuplex_Type = NtcAlarmState
_NtcEtherAlmMgmt1EthHalfDuplex_Object = MibScalar
ntcEtherAlmMgmt1EthHalfDuplex = _NtcEtherAlmMgmt1EthHalfDuplex_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 6, 2),
    _NtcEtherAlmMgmt1EthHalfDuplex_Type()
)
ntcEtherAlmMgmt1EthHalfDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcEtherAlmMgmt1EthHalfDuplex.setStatus("current")
_NtcEtherAlmMgmt2EthLinkFail_Type = NtcAlarmState
_NtcEtherAlmMgmt2EthLinkFail_Object = MibScalar
ntcEtherAlmMgmt2EthLinkFail = _NtcEtherAlmMgmt2EthLinkFail_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 6, 3),
    _NtcEtherAlmMgmt2EthLinkFail_Type()
)
ntcEtherAlmMgmt2EthLinkFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcEtherAlmMgmt2EthLinkFail.setStatus("current")
_NtcEtherAlmMgmt2EthHalfDuplex_Type = NtcAlarmState
_NtcEtherAlmMgmt2EthHalfDuplex_Object = MibScalar
ntcEtherAlmMgmt2EthHalfDuplex = _NtcEtherAlmMgmt2EthHalfDuplex_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 6, 4),
    _NtcEtherAlmMgmt2EthHalfDuplex_Type()
)
ntcEtherAlmMgmt2EthHalfDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcEtherAlmMgmt2EthHalfDuplex.setStatus("current")
_NtcEtherAlmData1EthLinkFail_Type = NtcAlarmState
_NtcEtherAlmData1EthLinkFail_Object = MibScalar
ntcEtherAlmData1EthLinkFail = _NtcEtherAlmData1EthLinkFail_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 6, 5),
    _NtcEtherAlmData1EthLinkFail_Type()
)
ntcEtherAlmData1EthLinkFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcEtherAlmData1EthLinkFail.setStatus("current")
_NtcEtherAlmData1EthHalfDuplex_Type = NtcAlarmState
_NtcEtherAlmData1EthHalfDuplex_Object = MibScalar
ntcEtherAlmData1EthHalfDuplex = _NtcEtherAlmData1EthHalfDuplex_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 6, 6),
    _NtcEtherAlmData1EthHalfDuplex_Type()
)
ntcEtherAlmData1EthHalfDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcEtherAlmData1EthHalfDuplex.setStatus("current")
_NtcEtherAlmData2EthLinkFail_Type = NtcAlarmState
_NtcEtherAlmData2EthLinkFail_Object = MibScalar
ntcEtherAlmData2EthLinkFail = _NtcEtherAlmData2EthLinkFail_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 6, 7),
    _NtcEtherAlmData2EthLinkFail_Type()
)
ntcEtherAlmData2EthLinkFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcEtherAlmData2EthLinkFail.setStatus("current")
_NtcEtherAlmData2EthHalfDuplex_Type = NtcAlarmState
_NtcEtherAlmData2EthHalfDuplex_Object = MibScalar
ntcEtherAlmData2EthHalfDuplex = _NtcEtherAlmData2EthHalfDuplex_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 6, 8),
    _NtcEtherAlmData2EthHalfDuplex_Type()
)
ntcEtherAlmData2EthHalfDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcEtherAlmData2EthHalfDuplex.setStatus("current")
_NtcEtherAlmMgmtFpEthLinkFail_Type = NtcAlarmState
_NtcEtherAlmMgmtFpEthLinkFail_Object = MibScalar
ntcEtherAlmMgmtFpEthLinkFail = _NtcEtherAlmMgmtFpEthLinkFail_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 6, 9),
    _NtcEtherAlmMgmtFpEthLinkFail_Type()
)
ntcEtherAlmMgmtFpEthLinkFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcEtherAlmMgmtFpEthLinkFail.setStatus("current")
_NtcEtherAlmMgmtFpEthHalfDuplex_Type = NtcAlarmState
_NtcEtherAlmMgmtFpEthHalfDuplex_Object = MibScalar
ntcEtherAlmMgmtFpEthHalfDuplex = _NtcEtherAlmMgmtFpEthHalfDuplex_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 6, 10),
    _NtcEtherAlmMgmtFpEthHalfDuplex_Type()
)
ntcEtherAlmMgmtFpEthHalfDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcEtherAlmMgmtFpEthHalfDuplex.setStatus("current")
_NtcEtherAlmMgmtEthInterfaceFail_Type = NtcAlarmState
_NtcEtherAlmMgmtEthInterfaceFail_Object = MibScalar
ntcEtherAlmMgmtEthInterfaceFail = _NtcEtherAlmMgmtEthInterfaceFail_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 6, 11),
    _NtcEtherAlmMgmtEthInterfaceFail_Type()
)
ntcEtherAlmMgmtEthInterfaceFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcEtherAlmMgmtEthInterfaceFail.setStatus("current")
_NtcEtherAlmDataEthInterfaceFail_Type = NtcAlarmState
_NtcEtherAlmDataEthInterfaceFail_Object = MibScalar
ntcEtherAlmDataEthInterfaceFail = _NtcEtherAlmDataEthInterfaceFail_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 6, 12),
    _NtcEtherAlmDataEthInterfaceFail_Type()
)
ntcEtherAlmDataEthInterfaceFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcEtherAlmDataEthInterfaceFail.setStatus("current")
_NtcEtherAlmSat1EthLinkFail_Type = NtcAlarmState
_NtcEtherAlmSat1EthLinkFail_Object = MibScalar
ntcEtherAlmSat1EthLinkFail = _NtcEtherAlmSat1EthLinkFail_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 6, 13),
    _NtcEtherAlmSat1EthLinkFail_Type()
)
ntcEtherAlmSat1EthLinkFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcEtherAlmSat1EthLinkFail.setStatus("current")
_NtcEtherAlmSat1EthHalfDuplex_Type = NtcAlarmState
_NtcEtherAlmSat1EthHalfDuplex_Object = MibScalar
ntcEtherAlmSat1EthHalfDuplex = _NtcEtherAlmSat1EthHalfDuplex_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 6, 14),
    _NtcEtherAlmSat1EthHalfDuplex_Type()
)
ntcEtherAlmSat1EthHalfDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcEtherAlmSat1EthHalfDuplex.setStatus("current")
_NtcEtherAlmSat2EthLinkFail_Type = NtcAlarmState
_NtcEtherAlmSat2EthLinkFail_Object = MibScalar
ntcEtherAlmSat2EthLinkFail = _NtcEtherAlmSat2EthLinkFail_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 6, 15),
    _NtcEtherAlmSat2EthLinkFail_Type()
)
ntcEtherAlmSat2EthLinkFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcEtherAlmSat2EthLinkFail.setStatus("current")
_NtcEtherAlmSat2EthHalfDuplex_Type = NtcAlarmState
_NtcEtherAlmSat2EthHalfDuplex_Object = MibScalar
ntcEtherAlmSat2EthHalfDuplex = _NtcEtherAlmSat2EthHalfDuplex_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 6, 16),
    _NtcEtherAlmSat2EthHalfDuplex_Type()
)
ntcEtherAlmSat2EthHalfDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcEtherAlmSat2EthHalfDuplex.setStatus("current")
_NtcEtherAlmSatEthInterfaceFail_Type = NtcAlarmState
_NtcEtherAlmSatEthInterfaceFail_Object = MibScalar
ntcEtherAlmSatEthInterfaceFail = _NtcEtherAlmSatEthInterfaceFail_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 6, 17),
    _NtcEtherAlmSatEthInterfaceFail_Type()
)
ntcEtherAlmSatEthInterfaceFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcEtherAlmSatEthInterfaceFail.setStatus("current")
_NtcEtherAlmMgmtEthGenIfFail_Type = NtcAlarmState
_NtcEtherAlmMgmtEthGenIfFail_Object = MibScalar
ntcEtherAlmMgmtEthGenIfFail = _NtcEtherAlmMgmtEthGenIfFail_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 6, 18),
    _NtcEtherAlmMgmtEthGenIfFail_Type()
)
ntcEtherAlmMgmtEthGenIfFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcEtherAlmMgmtEthGenIfFail.setStatus("current")
_NtcEtherAlmDataEthGenIfFail_Type = NtcAlarmState
_NtcEtherAlmDataEthGenIfFail_Object = MibScalar
ntcEtherAlmDataEthGenIfFail = _NtcEtherAlmDataEthGenIfFail_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 6, 19),
    _NtcEtherAlmDataEthGenIfFail_Type()
)
ntcEtherAlmDataEthGenIfFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcEtherAlmDataEthGenIfFail.setStatus("current")
_NtcEtherAlmSatEthGenIfFail_Type = NtcAlarmState
_NtcEtherAlmSatEthGenIfFail_Object = MibScalar
ntcEtherAlmSatEthGenIfFail = _NtcEtherAlmSatEthGenIfFail_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 6, 20),
    _NtcEtherAlmSatEthGenIfFail_Type()
)
ntcEtherAlmSatEthGenIfFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcEtherAlmSatEthGenIfFail.setStatus("current")


class _NtcEtherDataIgmpVersion_Type(Integer32):
    """Custom type ntcEtherDataIgmpVersion based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("v2", 0),
          ("v3", 1))
    )


_NtcEtherDataIgmpVersion_Type.__name__ = "Integer32"
_NtcEtherDataIgmpVersion_Object = MibScalar
ntcEtherDataIgmpVersion = _NtcEtherDataIgmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 1, 7),
    _NtcEtherDataIgmpVersion_Type()
)
ntcEtherDataIgmpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcEtherDataIgmpVersion.setStatus("current")
_NtcEtherConformance_ObjectIdentity = ObjectIdentity
ntcEtherConformance = _NtcEtherConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 2)
)
if mibBuilder.loadTexts:
    ntcEtherConformance.setStatus("current")
_NtcEtherConfCompliance_ObjectIdentity = ObjectIdentity
ntcEtherConfCompliance = _NtcEtherConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 2, 1)
)
if mibBuilder.loadTexts:
    ntcEtherConfCompliance.setStatus("current")
_NtcEtherConfGroup_ObjectIdentity = ObjectIdentity
ntcEtherConfGroup = _NtcEtherConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 2, 2)
)
if mibBuilder.loadTexts:
    ntcEtherConfGroup.setStatus("current")

# Managed Objects groups

ntcEtherConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 2, 2, 1)
)
ntcEtherConfGrpV1Standard.setObjects(
      *(("NEWTEC-ETHERNET-MIB", "ntcEtherLinkMgmtEnable"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherLinkMgmtMacAddress"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherLinkMgmtAutoNegotiation"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherLinkMgmtAdvertisedSpeeds"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherLinkMgmtForcedSpeed"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherLinkMgmtLinkState"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherLinkMgmtMtu"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherLinkDataEnable"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherLinkDataMacAddress"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherLinkDataAutoNegotiation"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherLinkDataAdvertisedSpeeds"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherLinkDataForcedSpeed"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherLinkDataLinkState"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherLinkDataMtu"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherStatMgmtInputBytes"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherStatMgmtInputPackets"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherStatMgmtInputDropped"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherStatMgmtOutputBytes"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherStatMgmtOutputPackets"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherStatMgmtOutputDropped"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherStatMgmtInputErrors"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherStatMgmtOutputerrors"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherStatDataInputBytes"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherStatDataInputPackets"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherStatDataInputDropped"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherStatDataOutputBytes"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherStatDataOutputPackets"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherStatDataOutputDropped"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherStatDataInputErrors"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherStatDataOutputerrors"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherIfRedMgmtSwitchOrder"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherIfRedMgmtSwitchCount"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherIfRedMgmtActiveInterface"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherIfRedDataSwitchOrder"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherIfRedDataSwitchCount"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherIfRedDataActiveInterface"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherIfRedDataGwUnreachImpact"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherIfRedSatSwitchOrder"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherIfRedSatSwitchCount"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherIfRedSatActiveInterface"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherAlmMgmt1EthLinkFail"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherAlmMgmt1EthHalfDuplex"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherAlmMgmt2EthLinkFail"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherAlmMgmt2EthHalfDuplex"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherAlmData1EthLinkFail"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherAlmData1EthHalfDuplex"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherAlmData2EthLinkFail"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherAlmData2EthHalfDuplex"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherAlmMgmtFpEthLinkFail"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherAlmMgmtFpEthHalfDuplex"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherAlmMgmtEthInterfaceFail"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherAlmDataEthInterfaceFail"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherAlmSat1EthLinkFail"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherAlmSat1EthHalfDuplex"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherAlmSat2EthLinkFail"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherAlmSat2EthHalfDuplex"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherAlmSatEthInterfaceFail"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherAlmMgmtEthGenIfFail"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherAlmDataEthGenIfFail"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherAlmSatEthGenIfFail"),
        ("NEWTEC-ETHERNET-MIB", "ntcEtherDataIgmpVersion"))
)
if mibBuilder.loadTexts:
    ntcEtherConfGrpV1Standard.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcEtherConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 500, 2, 1, 1)
)
ntcEtherConfCompV1Standard.setObjects(
    ("NEWTEC-ETHERNET-MIB", "ntcEtherConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcEtherConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-ETHERNET-MIB",
    **{"ntcEthernet": ntcEthernet,
       "ntcEtherObjects": ntcEtherObjects,
       "ntcEtherLinkMgmtTable": ntcEtherLinkMgmtTable,
       "ntcEtherLinkMgmtEntry": ntcEtherLinkMgmtEntry,
       "ntcEtherLinkMgmtInterface": ntcEtherLinkMgmtInterface,
       "ntcEtherLinkMgmtEnable": ntcEtherLinkMgmtEnable,
       "ntcEtherLinkMgmtMacAddress": ntcEtherLinkMgmtMacAddress,
       "ntcEtherLinkMgmtAutoNegotiation": ntcEtherLinkMgmtAutoNegotiation,
       "ntcEtherLinkMgmtAdvertisedSpeeds": ntcEtherLinkMgmtAdvertisedSpeeds,
       "ntcEtherLinkMgmtForcedSpeed": ntcEtherLinkMgmtForcedSpeed,
       "ntcEtherLinkMgmtLinkState": ntcEtherLinkMgmtLinkState,
       "ntcEtherLinkMgmtMtu": ntcEtherLinkMgmtMtu,
       "ntcEtherLinkDataTable": ntcEtherLinkDataTable,
       "ntcEtherLinkDataEntry": ntcEtherLinkDataEntry,
       "ntcEtherLinkDataInterface": ntcEtherLinkDataInterface,
       "ntcEtherLinkDataEnable": ntcEtherLinkDataEnable,
       "ntcEtherLinkDataMacAddress": ntcEtherLinkDataMacAddress,
       "ntcEtherLinkDataAutoNegotiation": ntcEtherLinkDataAutoNegotiation,
       "ntcEtherLinkDataAdvertisedSpeeds": ntcEtherLinkDataAdvertisedSpeeds,
       "ntcEtherLinkDataForcedSpeed": ntcEtherLinkDataForcedSpeed,
       "ntcEtherLinkDataLinkState": ntcEtherLinkDataLinkState,
       "ntcEtherLinkDataMtu": ntcEtherLinkDataMtu,
       "ntcEtherStatMgmtTable": ntcEtherStatMgmtTable,
       "ntcEtherStatMgmtEntry": ntcEtherStatMgmtEntry,
       "ntcEtherStatMgmtInterface": ntcEtherStatMgmtInterface,
       "ntcEtherStatMgmtInputBytes": ntcEtherStatMgmtInputBytes,
       "ntcEtherStatMgmtInputPackets": ntcEtherStatMgmtInputPackets,
       "ntcEtherStatMgmtInputDropped": ntcEtherStatMgmtInputDropped,
       "ntcEtherStatMgmtOutputBytes": ntcEtherStatMgmtOutputBytes,
       "ntcEtherStatMgmtOutputPackets": ntcEtherStatMgmtOutputPackets,
       "ntcEtherStatMgmtOutputDropped": ntcEtherStatMgmtOutputDropped,
       "ntcEtherStatMgmtInputErrors": ntcEtherStatMgmtInputErrors,
       "ntcEtherStatMgmtOutputerrors": ntcEtherStatMgmtOutputerrors,
       "ntcEtherStatDataTable": ntcEtherStatDataTable,
       "ntcEtherStatDataEntry": ntcEtherStatDataEntry,
       "ntcEtherStatDataInterface": ntcEtherStatDataInterface,
       "ntcEtherStatDataInputBytes": ntcEtherStatDataInputBytes,
       "ntcEtherStatDataInputPackets": ntcEtherStatDataInputPackets,
       "ntcEtherStatDataInputDropped": ntcEtherStatDataInputDropped,
       "ntcEtherStatDataOutputBytes": ntcEtherStatDataOutputBytes,
       "ntcEtherStatDataOutputPackets": ntcEtherStatDataOutputPackets,
       "ntcEtherStatDataOutputDropped": ntcEtherStatDataOutputDropped,
       "ntcEtherStatDataInputErrors": ntcEtherStatDataInputErrors,
       "ntcEtherStatDataOutputerrors": ntcEtherStatDataOutputerrors,
       "ntcEtherInterfaceRedundancy": ntcEtherInterfaceRedundancy,
       "ntcEtherIfRedMgmt": ntcEtherIfRedMgmt,
       "ntcEtherIfRedMgmtSwitchOrder": ntcEtherIfRedMgmtSwitchOrder,
       "ntcEtherIfRedMgmtSwitchCount": ntcEtherIfRedMgmtSwitchCount,
       "ntcEtherIfRedMgmtActiveInterface": ntcEtherIfRedMgmtActiveInterface,
       "ntcEtherIfRedData": ntcEtherIfRedData,
       "ntcEtherIfRedDataSwitchOrder": ntcEtherIfRedDataSwitchOrder,
       "ntcEtherIfRedDataSwitchCount": ntcEtherIfRedDataSwitchCount,
       "ntcEtherIfRedDataActiveInterface": ntcEtherIfRedDataActiveInterface,
       "ntcEtherIfRedDataGwUnreachImpact": ntcEtherIfRedDataGwUnreachImpact,
       "ntcEtherIfRedSat": ntcEtherIfRedSat,
       "ntcEtherIfRedSatSwitchOrder": ntcEtherIfRedSatSwitchOrder,
       "ntcEtherIfRedSatSwitchCount": ntcEtherIfRedSatSwitchCount,
       "ntcEtherIfRedSatActiveInterface": ntcEtherIfRedSatActiveInterface,
       "ntcEtherAlarm": ntcEtherAlarm,
       "ntcEtherAlmMgmt1EthLinkFail": ntcEtherAlmMgmt1EthLinkFail,
       "ntcEtherAlmMgmt1EthHalfDuplex": ntcEtherAlmMgmt1EthHalfDuplex,
       "ntcEtherAlmMgmt2EthLinkFail": ntcEtherAlmMgmt2EthLinkFail,
       "ntcEtherAlmMgmt2EthHalfDuplex": ntcEtherAlmMgmt2EthHalfDuplex,
       "ntcEtherAlmData1EthLinkFail": ntcEtherAlmData1EthLinkFail,
       "ntcEtherAlmData1EthHalfDuplex": ntcEtherAlmData1EthHalfDuplex,
       "ntcEtherAlmData2EthLinkFail": ntcEtherAlmData2EthLinkFail,
       "ntcEtherAlmData2EthHalfDuplex": ntcEtherAlmData2EthHalfDuplex,
       "ntcEtherAlmMgmtFpEthLinkFail": ntcEtherAlmMgmtFpEthLinkFail,
       "ntcEtherAlmMgmtFpEthHalfDuplex": ntcEtherAlmMgmtFpEthHalfDuplex,
       "ntcEtherAlmMgmtEthInterfaceFail": ntcEtherAlmMgmtEthInterfaceFail,
       "ntcEtherAlmDataEthInterfaceFail": ntcEtherAlmDataEthInterfaceFail,
       "ntcEtherAlmSat1EthLinkFail": ntcEtherAlmSat1EthLinkFail,
       "ntcEtherAlmSat1EthHalfDuplex": ntcEtherAlmSat1EthHalfDuplex,
       "ntcEtherAlmSat2EthLinkFail": ntcEtherAlmSat2EthLinkFail,
       "ntcEtherAlmSat2EthHalfDuplex": ntcEtherAlmSat2EthHalfDuplex,
       "ntcEtherAlmSatEthInterfaceFail": ntcEtherAlmSatEthInterfaceFail,
       "ntcEtherAlmMgmtEthGenIfFail": ntcEtherAlmMgmtEthGenIfFail,
       "ntcEtherAlmDataEthGenIfFail": ntcEtherAlmDataEthGenIfFail,
       "ntcEtherAlmSatEthGenIfFail": ntcEtherAlmSatEthGenIfFail,
       "ntcEtherDataIgmpVersion": ntcEtherDataIgmpVersion,
       "ntcEtherConformance": ntcEtherConformance,
       "ntcEtherConfCompliance": ntcEtherConfCompliance,
       "ntcEtherConfCompV1Standard": ntcEtherConfCompV1Standard,
       "ntcEtherConfGroup": ntcEtherConfGroup,
       "ntcEtherConfGrpV1Standard": ntcEtherConfGrpV1Standard}
)
