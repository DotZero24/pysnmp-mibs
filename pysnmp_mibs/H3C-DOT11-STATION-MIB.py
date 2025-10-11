# SNMP MIB module (H3C-DOT11-STATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-DOT11-STATION-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:19:39 2025
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

(H3cDot11AKMType,
 H3cDot11AssocFailType,
 H3cDot11AuthenType,
 H3cDot11AuthorFailType,
 H3cDot11ChannelScopeType,
 H3cDot11CipherType,
 H3cDot11ObjectIDType,
 H3cDot11RadioScopeType,
 H3cDot11RadioType,
 H3cDot11RadioType2,
 H3cDot11SSIDEncryptModeType,
 H3cDot11SSIDStringType,
 H3cDot11SecIEStatusType,
 h3cDot11) = mibBuilder.importSymbols(
    "H3C-DOT11-REF-MIB",
    "H3cDot11AKMType",
    "H3cDot11AssocFailType",
    "H3cDot11AuthenType",
    "H3cDot11AuthorFailType",
    "H3cDot11ChannelScopeType",
    "H3cDot11CipherType",
    "H3cDot11ObjectIDType",
    "H3cDot11RadioScopeType",
    "H3cDot11RadioType",
    "H3cDot11RadioType2",
    "H3cDot11SSIDEncryptModeType",
    "H3cDot11SSIDStringType",
    "H3cDot11SecIEStatusType",
    "h3cDot11")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3cDot11STATION = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3)
)
if mibBuilder.loadTexts:
    h3cDot11STATION.setRevisions(
        ("2017-10-09 18:00",
         "2017-02-24 18:00",
         "2016-03-11 18:00",
         "2015-04-13 18:00",
         "2010-09-02 18:00",
         "2010-02-23 18:00",
         "2009-12-01 18:00",
         "2009-08-07 18:00",
         "2009-07-29 18:00",
         "2009-05-07 20:00",
         "2008-11-07 17:30",
         "2008-02-25 18:00",
         "2007-12-21 18:00",
         "2007-06-21 20:00",
         "2007-04-27 20:00",
         "2006-05-10 16:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cDot11StationMtGroup_ObjectIdentity = ObjectIdentity
h3cDot11StationMtGroup = _H3cDot11StationMtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1)
)
_H3cDot11StationAssociateTable_Object = MibTable
h3cDot11StationAssociateTable = _H3cDot11StationAssociateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 1)
)
if mibBuilder.loadTexts:
    h3cDot11StationAssociateTable.setStatus("current")
_H3cDot11StationAssociateEntry_Object = MibTableRow
h3cDot11StationAssociateEntry = _H3cDot11StationAssociateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 1, 1)
)
h3cDot11StationAssociateEntry.setIndexNames(
    (0, "H3C-DOT11-STATION-MIB", "h3cDot11StationMAC"),
)
if mibBuilder.loadTexts:
    h3cDot11StationAssociateEntry.setStatus("current")
_H3cDot11StationMAC_Type = MacAddress
_H3cDot11StationMAC_Object = MibTableColumn
h3cDot11StationMAC = _H3cDot11StationMAC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 1, 1, 1),
    _H3cDot11StationMAC_Type()
)
h3cDot11StationMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11StationMAC.setStatus("current")
_H3cDot11StationIPAddress_Type = IpAddress
_H3cDot11StationIPAddress_Object = MibTableColumn
h3cDot11StationIPAddress = _H3cDot11StationIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 1, 1, 2),
    _H3cDot11StationIPAddress_Type()
)
h3cDot11StationIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationIPAddress.setStatus("current")
_H3cDot11StationUserName_Type = OctetString
_H3cDot11StationUserName_Object = MibTableColumn
h3cDot11StationUserName = _H3cDot11StationUserName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 1, 1, 3),
    _H3cDot11StationUserName_Type()
)
h3cDot11StationUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationUserName.setStatus("current")
_H3cDot11StationTxRateSet_Type = OctetString
_H3cDot11StationTxRateSet_Object = MibTableColumn
h3cDot11StationTxRateSet = _H3cDot11StationTxRateSet_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 1, 1, 4),
    _H3cDot11StationTxRateSet_Type()
)
h3cDot11StationTxRateSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationTxRateSet.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11StationTxRateSet.setUnits("Mbps")
_H3cDot11StationUpTime_Type = Unsigned32
_H3cDot11StationUpTime_Object = MibTableColumn
h3cDot11StationUpTime = _H3cDot11StationUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 1, 1, 5),
    _H3cDot11StationUpTime_Type()
)
h3cDot11StationUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationUpTime.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11StationUpTime.setUnits("second")
_H3cDot11StationSignalStrength_Type = Integer32
_H3cDot11StationSignalStrength_Object = MibTableColumn
h3cDot11StationSignalStrength = _H3cDot11StationSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 1, 1, 6),
    _H3cDot11StationSignalStrength_Type()
)
h3cDot11StationSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationSignalStrength.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11StationSignalStrength.setUnits("dBm")
_H3cDot11StationRSSI_Type = Integer32
_H3cDot11StationRSSI_Object = MibTableColumn
h3cDot11StationRSSI = _H3cDot11StationRSSI_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 1, 1, 7),
    _H3cDot11StationRSSI_Type()
)
h3cDot11StationRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationRSSI.setStatus("current")
_H3cDot11StationChannel_Type = H3cDot11ChannelScopeType
_H3cDot11StationChannel_Object = MibTableColumn
h3cDot11StationChannel = _H3cDot11StationChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 1, 1, 8),
    _H3cDot11StationChannel_Type()
)
h3cDot11StationChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationChannel.setStatus("current")


class _H3cDot11StationPowerSaveMode_Type(Integer32):
    """Custom type h3cDot11StationPowerSaveMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("powersave", 2))
    )


_H3cDot11StationPowerSaveMode_Type.__name__ = "Integer32"
_H3cDot11StationPowerSaveMode_Object = MibTableColumn
h3cDot11StationPowerSaveMode = _H3cDot11StationPowerSaveMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 1, 1, 9),
    _H3cDot11StationPowerSaveMode_Type()
)
h3cDot11StationPowerSaveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationPowerSaveMode.setStatus("current")
_H3cDot11StationAid_Type = Integer32
_H3cDot11StationAid_Object = MibTableColumn
h3cDot11StationAid = _H3cDot11StationAid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 1, 1, 10),
    _H3cDot11StationAid_Type()
)
h3cDot11StationAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationAid.setStatus("current")
_H3cDot11StationVlanId_Type = Integer32
_H3cDot11StationVlanId_Object = MibTableColumn
h3cDot11StationVlanId = _H3cDot11StationVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 1, 1, 11),
    _H3cDot11StationVlanId_Type()
)
h3cDot11StationVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationVlanId.setStatus("current")
_H3cDot11StationSSIDName_Type = H3cDot11SSIDStringType
_H3cDot11StationSSIDName_Object = MibTableColumn
h3cDot11StationSSIDName = _H3cDot11StationSSIDName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 1, 1, 12),
    _H3cDot11StationSSIDName_Type()
)
h3cDot11StationSSIDName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationSSIDName.setStatus("current")
_H3cDot11StationAuthenMode_Type = H3cDot11AuthenType
_H3cDot11StationAuthenMode_Object = MibTableColumn
h3cDot11StationAuthenMode = _H3cDot11StationAuthenMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 1, 1, 13),
    _H3cDot11StationAuthenMode_Type()
)
h3cDot11StationAuthenMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationAuthenMode.setStatus("current")
_H3cDot11StationAKMMode_Type = H3cDot11AKMType
_H3cDot11StationAKMMode_Object = MibTableColumn
h3cDot11StationAKMMode = _H3cDot11StationAKMMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 1, 1, 14),
    _H3cDot11StationAKMMode_Type()
)
h3cDot11StationAKMMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationAKMMode.setStatus("current")
_H3cDot11StationSecurityCiphers_Type = H3cDot11CipherType
_H3cDot11StationSecurityCiphers_Object = MibTableColumn
h3cDot11StationSecurityCiphers = _H3cDot11StationSecurityCiphers_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 1, 1, 15),
    _H3cDot11StationSecurityCiphers_Type()
)
h3cDot11StationSecurityCiphers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationSecurityCiphers.setStatus("current")


class _H3cDot11StationSSIDEncryptMode_Type(H3cDot11SSIDEncryptModeType):
    """Custom type h3cDot11StationSSIDEncryptMode based on H3cDot11SSIDEncryptModeType"""
    defaultValue = 2


_H3cDot11StationSSIDEncryptMode_Type.__name__ = "H3cDot11SSIDEncryptModeType"
_H3cDot11StationSSIDEncryptMode_Object = MibTableColumn
h3cDot11StationSSIDEncryptMode = _H3cDot11StationSSIDEncryptMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 1, 1, 16),
    _H3cDot11StationSSIDEncryptMode_Type()
)
h3cDot11StationSSIDEncryptMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationSSIDEncryptMode.setStatus("current")
_H3cDot11StationRxSNR_Type = Integer32
_H3cDot11StationRxSNR_Object = MibTableColumn
h3cDot11StationRxSNR = _H3cDot11StationRxSNR_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 1, 1, 17),
    _H3cDot11StationRxSNR_Type()
)
h3cDot11StationRxSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationRxSNR.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11StationRxSNR.setUnits("One Percent")
_H3cDot11StationTxRate_Type = Integer32
_H3cDot11StationTxRate_Object = MibTableColumn
h3cDot11StationTxRate = _H3cDot11StationTxRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 1, 1, 18),
    _H3cDot11StationTxRate_Type()
)
h3cDot11StationTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationTxRate.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11StationTxRate.setUnits("Mbps")
_H3cDot11StationRxRate_Type = Integer32
_H3cDot11StationRxRate_Object = MibTableColumn
h3cDot11StationRxRate = _H3cDot11StationRxRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 1, 1, 19),
    _H3cDot11StationRxRate_Type()
)
h3cDot11StationRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationRxRate.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11StationRxRate.setUnits("Mbps")


class _H3cDot11StationVendorName_Type(OctetString):
    """Custom type h3cDot11StationVendorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_H3cDot11StationVendorName_Type.__name__ = "OctetString"
_H3cDot11StationVendorName_Object = MibTableColumn
h3cDot11StationVendorName = _H3cDot11StationVendorName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 1, 1, 20),
    _H3cDot11StationVendorName_Type()
)
h3cDot11StationVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationVendorName.setStatus("current")
_H3cDot11StationRadioMode_Type = H3cDot11RadioType
_H3cDot11StationRadioMode_Object = MibTableColumn
h3cDot11StationRadioMode = _H3cDot11StationRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 1, 1, 21),
    _H3cDot11StationRadioMode_Type()
)
h3cDot11StationRadioMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationRadioMode.setStatus("current")
_H3cDot11StationRxNoise_Type = Integer32
_H3cDot11StationRxNoise_Object = MibTableColumn
h3cDot11StationRxNoise = _H3cDot11StationRxNoise_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 1, 1, 22),
    _H3cDot11StationRxNoise_Type()
)
h3cDot11StationRxNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationRxNoise.setStatus("current")
_H3cDot11StationMACAddress_Type = MacAddress
_H3cDot11StationMACAddress_Object = MibTableColumn
h3cDot11StationMACAddress = _H3cDot11StationMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 1, 1, 23),
    _H3cDot11StationMACAddress_Type()
)
h3cDot11StationMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationMACAddress.setStatus("current")
_H3cDot11StationTxSpeed_Type = Integer32
_H3cDot11StationTxSpeed_Object = MibTableColumn
h3cDot11StationTxSpeed = _H3cDot11StationTxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 1, 1, 24),
    _H3cDot11StationTxSpeed_Type()
)
h3cDot11StationTxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationTxSpeed.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11StationTxSpeed.setUnits("byte/s")
_H3cDot11StationRxSpeed_Type = Integer32
_H3cDot11StationRxSpeed_Object = MibTableColumn
h3cDot11StationRxSpeed = _H3cDot11StationRxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 1, 1, 25),
    _H3cDot11StationRxSpeed_Type()
)
h3cDot11StationRxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationRxSpeed.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11StationRxSpeed.setUnits("byte/s")


class _H3cDot11StationWmmMode_Type(Integer32):
    """Custom type h3cDot11StationWmmMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wmm", 1),
          ("nonwmm", 2))
    )


_H3cDot11StationWmmMode_Type.__name__ = "Integer32"
_H3cDot11StationWmmMode_Object = MibTableColumn
h3cDot11StationWmmMode = _H3cDot11StationWmmMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 1, 1, 26),
    _H3cDot11StationWmmMode_Type()
)
h3cDot11StationWmmMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationWmmMode.setStatus("current")
_H3cDot11StationSecIEStatus_Type = H3cDot11SecIEStatusType
_H3cDot11StationSecIEStatus_Object = MibTableColumn
h3cDot11StationSecIEStatus = _H3cDot11StationSecIEStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 1, 1, 27),
    _H3cDot11StationSecIEStatus_Type()
)
h3cDot11StationSecIEStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationSecIEStatus.setStatus("current")
_H3cDot11StationUpTimeTicks_Type = TimeTicks
_H3cDot11StationUpTimeTicks_Object = MibTableColumn
h3cDot11StationUpTimeTicks = _H3cDot11StationUpTimeTicks_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 1, 1, 28),
    _H3cDot11StationUpTimeTicks_Type()
)
h3cDot11StationUpTimeTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationUpTimeTicks.setStatus("current")
_H3cDot11StationRadioMode2_Type = H3cDot11RadioType2
_H3cDot11StationRadioMode2_Object = MibTableColumn
h3cDot11StationRadioMode2 = _H3cDot11StationRadioMode2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 1, 1, 29),
    _H3cDot11StationRadioMode2_Type()
)
h3cDot11StationRadioMode2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationRadioMode2.setStatus("current")
_H3cDot11StationAssTime_Type = DateAndTime
_H3cDot11StationAssTime_Object = MibTableColumn
h3cDot11StationAssTime = _H3cDot11StationAssTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 1, 1, 30),
    _H3cDot11StationAssTime_Type()
)
h3cDot11StationAssTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationAssTime.setStatus("current")


class _H3cDot11StationUserAuthType_Type(Integer32):
    """Custom type h3cDot11StationUserAuthType based on Integer32"""
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
        *(("portalAuth", 1),
          ("authFree", 2),
          ("associateAuth", 3),
          ("macAuth", 4))
    )


_H3cDot11StationUserAuthType_Type.__name__ = "Integer32"
_H3cDot11StationUserAuthType_Object = MibTableColumn
h3cDot11StationUserAuthType = _H3cDot11StationUserAuthType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 1, 1, 31),
    _H3cDot11StationUserAuthType_Type()
)
h3cDot11StationUserAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationUserAuthType.setStatus("current")
_H3cDot11StationRfPingTest_Type = TruthValue
_H3cDot11StationRfPingTest_Object = MibTableColumn
h3cDot11StationRfPingTest = _H3cDot11StationRfPingTest_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 1, 1, 32),
    _H3cDot11StationRfPingTest_Type()
)
h3cDot11StationRfPingTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11StationRfPingTest.setStatus("current")
_H3cDot11StationMaxRate_Type = Integer32
_H3cDot11StationMaxRate_Object = MibTableColumn
h3cDot11StationMaxRate = _H3cDot11StationMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 1, 1, 33),
    _H3cDot11StationMaxRate_Type()
)
h3cDot11StationMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11StationMaxRate.setUnits("Mbps")


class _H3cDot11StationPowerSaveModeCM_Type(Integer32):
    """Custom type h3cDot11StationPowerSaveModeCM based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("powersave", 1))
    )


_H3cDot11StationPowerSaveModeCM_Type.__name__ = "Integer32"
_H3cDot11StationPowerSaveModeCM_Object = MibTableColumn
h3cDot11StationPowerSaveModeCM = _H3cDot11StationPowerSaveModeCM_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 1, 1, 34),
    _H3cDot11StationPowerSaveModeCM_Type()
)
h3cDot11StationPowerSaveModeCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationPowerSaveModeCM.setStatus("current")


class _H3cDot11StationAuthenModeCM_Type(Integer32):
    """Custom type h3cDot11StationAuthenModeCM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("opensystem", 0),
          ("sharedkey", 1))
    )


_H3cDot11StationAuthenModeCM_Type.__name__ = "Integer32"
_H3cDot11StationAuthenModeCM_Object = MibTableColumn
h3cDot11StationAuthenModeCM = _H3cDot11StationAuthenModeCM_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 1, 1, 35),
    _H3cDot11StationAuthenModeCM_Type()
)
h3cDot11StationAuthenModeCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationAuthenModeCM.setStatus("current")


class _H3cDot11StationAKMModeCM_Type(Integer32):
    """Custom type h3cDot11StationAKMModeCM based on Integer32"""
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
          ("psk", 1),
          ("radius", 2),
          ("wlanex", 3))
    )


_H3cDot11StationAKMModeCM_Type.__name__ = "Integer32"
_H3cDot11StationAKMModeCM_Object = MibTableColumn
h3cDot11StationAKMModeCM = _H3cDot11StationAKMModeCM_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 1, 1, 36),
    _H3cDot11StationAKMModeCM_Type()
)
h3cDot11StationAKMModeCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationAKMModeCM.setStatus("current")


class _H3cDot11StationSecurityCiphersCM_Type(Integer32):
    """Custom type h3cDot11StationSecurityCiphersCM based on Integer32"""
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
          ("wep40", 1),
          ("wep104", 2),
          ("tkip", 3),
          ("aesccmp", 4),
          ("wpisms4", 5))
    )


_H3cDot11StationSecurityCiphersCM_Type.__name__ = "Integer32"
_H3cDot11StationSecurityCiphersCM_Object = MibTableColumn
h3cDot11StationSecurityCiphersCM = _H3cDot11StationSecurityCiphersCM_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 1, 1, 37),
    _H3cDot11StationSecurityCiphersCM_Type()
)
h3cDot11StationSecurityCiphersCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationSecurityCiphersCM.setStatus("current")


class _H3cDot11StationSecIEStatusCM_Type(Integer32):
    """Custom type h3cDot11StationSecIEStatusCM based on Integer32"""
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
          ("wpa", 1),
          ("wpa2", 2),
          ("wlanex", 3))
    )


_H3cDot11StationSecIEStatusCM_Type.__name__ = "Integer32"
_H3cDot11StationSecIEStatusCM_Object = MibTableColumn
h3cDot11StationSecIEStatusCM = _H3cDot11StationSecIEStatusCM_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 1, 1, 38),
    _H3cDot11StationSecIEStatusCM_Type()
)
h3cDot11StationSecIEStatusCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationSecIEStatusCM.setStatus("current")
_H3cDot11StationIPv6Address_Type = OctetString
_H3cDot11StationIPv6Address_Object = MibTableColumn
h3cDot11StationIPv6Address = _H3cDot11StationIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 1, 1, 39),
    _H3cDot11StationIPv6Address_Type()
)
h3cDot11StationIPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationIPv6Address.setStatus("current")
_H3cDot11StationAssociateAPMACAddressCM_Type = MacAddress
_H3cDot11StationAssociateAPMACAddressCM_Object = MibTableColumn
h3cDot11StationAssociateAPMACAddressCM = _H3cDot11StationAssociateAPMACAddressCM_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 1, 1, 40),
    _H3cDot11StationAssociateAPMACAddressCM_Type()
)
h3cDot11StationAssociateAPMACAddressCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationAssociateAPMACAddressCM.setStatus("current")
_H3cDot11StationDeviceType_Type = OctetString
_H3cDot11StationDeviceType_Object = MibTableColumn
h3cDot11StationDeviceType = _H3cDot11StationDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 1, 1, 41),
    _H3cDot11StationDeviceType_Type()
)
h3cDot11StationDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationDeviceType.setStatus("current")
_H3cDot11StationTxRateCM_Type = OctetString
_H3cDot11StationTxRateCM_Object = MibTableColumn
h3cDot11StationTxRateCM = _H3cDot11StationTxRateCM_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 1, 1, 42),
    _H3cDot11StationTxRateCM_Type()
)
h3cDot11StationTxRateCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationTxRateCM.setStatus("current")
_H3cDot11StationRxRateCM_Type = OctetString
_H3cDot11StationRxRateCM_Object = MibTableColumn
h3cDot11StationRxRateCM = _H3cDot11StationRxRateCM_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 1, 1, 43),
    _H3cDot11StationRxRateCM_Type()
)
h3cDot11StationRxRateCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationRxRateCM.setStatus("current")
_H3cDot11StationAPRelationTable_Object = MibTable
h3cDot11StationAPRelationTable = _H3cDot11StationAPRelationTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 2)
)
if mibBuilder.loadTexts:
    h3cDot11StationAPRelationTable.setStatus("current")
_H3cDot11StationAPRelationEntry_Object = MibTableRow
h3cDot11StationAPRelationEntry = _H3cDot11StationAPRelationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 2, 1)
)
h3cDot11StationAPRelationEntry.setIndexNames(
    (0, "H3C-DOT11-STATION-MIB", "h3cDot11StationMAC"),
)
if mibBuilder.loadTexts:
    h3cDot11StationAPRelationEntry.setStatus("current")
_H3cDot11CurrAPID_Type = H3cDot11ObjectIDType
_H3cDot11CurrAPID_Object = MibTableColumn
h3cDot11CurrAPID = _H3cDot11CurrAPID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 2, 1, 1),
    _H3cDot11CurrAPID_Type()
)
h3cDot11CurrAPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11CurrAPID.setStatus("current")
_H3cDot11CurrRadioID_Type = H3cDot11RadioScopeType
_H3cDot11CurrRadioID_Object = MibTableColumn
h3cDot11CurrRadioID = _H3cDot11CurrRadioID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 2, 1, 2),
    _H3cDot11CurrRadioID_Type()
)
h3cDot11CurrRadioID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11CurrRadioID.setStatus("current")
_H3cDot11CurrWlanID_Type = Integer32
_H3cDot11CurrWlanID_Object = MibTableColumn
h3cDot11CurrWlanID = _H3cDot11CurrWlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 2, 1, 3),
    _H3cDot11CurrWlanID_Type()
)
h3cDot11CurrWlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11CurrWlanID.setStatus("current")
_H3cDot11CurrAntennaID_Type = Integer32
_H3cDot11CurrAntennaID_Object = MibTableColumn
h3cDot11CurrAntennaID = _H3cDot11CurrAntennaID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 2, 1, 4),
    _H3cDot11CurrAntennaID_Type()
)
h3cDot11CurrAntennaID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11CurrAntennaID.setStatus("current")
_H3cDot11StationStatisTable_Object = MibTable
h3cDot11StationStatisTable = _H3cDot11StationStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 3)
)
if mibBuilder.loadTexts:
    h3cDot11StationStatisTable.setStatus("current")
_H3cDot11StationStatisEntry_Object = MibTableRow
h3cDot11StationStatisEntry = _H3cDot11StationStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 3, 1)
)
h3cDot11StationStatisEntry.setIndexNames(
    (0, "H3C-DOT11-STATION-MIB", "h3cDot11StationMAC"),
)
if mibBuilder.loadTexts:
    h3cDot11StationStatisEntry.setStatus("current")
_H3cDot11StationRxFrameCnt_Type = Counter32
_H3cDot11StationRxFrameCnt_Object = MibTableColumn
h3cDot11StationRxFrameCnt = _H3cDot11StationRxFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 3, 1, 1),
    _H3cDot11StationRxFrameCnt_Type()
)
h3cDot11StationRxFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationRxFrameCnt.setStatus("current")
_H3cDot11StationTxFrameCnt_Type = Counter32
_H3cDot11StationTxFrameCnt_Object = MibTableColumn
h3cDot11StationTxFrameCnt = _H3cDot11StationTxFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 3, 1, 2),
    _H3cDot11StationTxFrameCnt_Type()
)
h3cDot11StationTxFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationTxFrameCnt.setStatus("current")
_H3cDot11StationDropFrameCnt_Type = Counter32
_H3cDot11StationDropFrameCnt_Object = MibTableColumn
h3cDot11StationDropFrameCnt = _H3cDot11StationDropFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 3, 1, 3),
    _H3cDot11StationDropFrameCnt_Type()
)
h3cDot11StationDropFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationDropFrameCnt.setStatus("current")
_H3cDot11StationRxFrameBytes_Type = Counter64
_H3cDot11StationRxFrameBytes_Object = MibTableColumn
h3cDot11StationRxFrameBytes = _H3cDot11StationRxFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 3, 1, 4),
    _H3cDot11StationRxFrameBytes_Type()
)
h3cDot11StationRxFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationRxFrameBytes.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11StationRxFrameBytes.setUnits("bytes")
_H3cDot11StationTxFrameBytes_Type = Counter64
_H3cDot11StationTxFrameBytes_Object = MibTableColumn
h3cDot11StationTxFrameBytes = _H3cDot11StationTxFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 3, 1, 5),
    _H3cDot11StationTxFrameBytes_Type()
)
h3cDot11StationTxFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationTxFrameBytes.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11StationTxFrameBytes.setUnits("bytes")
_H3cDot11StationDropFrameBytes_Type = Counter64
_H3cDot11StationDropFrameBytes_Object = MibTableColumn
h3cDot11StationDropFrameBytes = _H3cDot11StationDropFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 3, 1, 6),
    _H3cDot11StationDropFrameBytes_Type()
)
h3cDot11StationDropFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationDropFrameBytes.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11StationDropFrameBytes.setUnits("bytes")
_H3cDot11StationRxRetryPkts_Type = Counter32
_H3cDot11StationRxRetryPkts_Object = MibTableColumn
h3cDot11StationRxRetryPkts = _H3cDot11StationRxRetryPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 3, 1, 7),
    _H3cDot11StationRxRetryPkts_Type()
)
h3cDot11StationRxRetryPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationRxRetryPkts.setStatus("current")
_H3cDot11StationTxRetryPkts_Type = Counter32
_H3cDot11StationTxRetryPkts_Object = MibTableColumn
h3cDot11StationTxRetryPkts = _H3cDot11StationTxRetryPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 3, 1, 8),
    _H3cDot11StationTxRetryPkts_Type()
)
h3cDot11StationTxRetryPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationTxRetryPkts.setStatus("current")
_H3cDot11StationRxRetryBytes_Type = Counter64
_H3cDot11StationRxRetryBytes_Object = MibTableColumn
h3cDot11StationRxRetryBytes = _H3cDot11StationRxRetryBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 3, 1, 9),
    _H3cDot11StationRxRetryBytes_Type()
)
h3cDot11StationRxRetryBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationRxRetryBytes.setStatus("current")
_H3cDot11StationTxRetryBytes_Type = Counter64
_H3cDot11StationTxRetryBytes_Object = MibTableColumn
h3cDot11StationTxRetryBytes = _H3cDot11StationTxRetryBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 3, 1, 10),
    _H3cDot11StationTxRetryBytes_Type()
)
h3cDot11StationTxRetryBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationTxRetryBytes.setStatus("current")
_H3cDot11StationThroughput_Type = Counter64
_H3cDot11StationThroughput_Object = MibTableColumn
h3cDot11StationThroughput = _H3cDot11StationThroughput_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 3, 1, 11),
    _H3cDot11StationThroughput_Type()
)
h3cDot11StationThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationThroughput.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11StationThroughput.setUnits("bytes")
_H3cDot11StationSuccessTxCnt_Type = Counter32
_H3cDot11StationSuccessTxCnt_Object = MibTableColumn
h3cDot11StationSuccessTxCnt = _H3cDot11StationSuccessTxCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 3, 1, 12),
    _H3cDot11StationSuccessTxCnt_Type()
)
h3cDot11StationSuccessTxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationSuccessTxCnt.setStatus("current")
_H3cDot11StationSuccessTxDataCnt_Type = Counter32
_H3cDot11StationSuccessTxDataCnt_Object = MibTableColumn
h3cDot11StationSuccessTxDataCnt = _H3cDot11StationSuccessTxDataCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 3, 1, 13),
    _H3cDot11StationSuccessTxDataCnt_Type()
)
h3cDot11StationSuccessTxDataCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationSuccessTxDataCnt.setStatus("current")
_H3cDot11StationRxDataFrameCnt_Type = Counter32
_H3cDot11StationRxDataFrameCnt_Object = MibTableColumn
h3cDot11StationRxDataFrameCnt = _H3cDot11StationRxDataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 3, 1, 14),
    _H3cDot11StationRxDataFrameCnt_Type()
)
h3cDot11StationRxDataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationRxDataFrameCnt.setStatus("current")
_H3cDot11StationTxDataFrameCnt_Type = Counter32
_H3cDot11StationTxDataFrameCnt_Object = MibTableColumn
h3cDot11StationTxDataFrameCnt = _H3cDot11StationTxDataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 3, 1, 15),
    _H3cDot11StationTxDataFrameCnt_Type()
)
h3cDot11StationTxDataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationTxDataFrameCnt.setStatus("current")
_H3cDot11StationRxDataFrameBytes_Type = Counter64
_H3cDot11StationRxDataFrameBytes_Object = MibTableColumn
h3cDot11StationRxDataFrameBytes = _H3cDot11StationRxDataFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 3, 1, 16),
    _H3cDot11StationRxDataFrameBytes_Type()
)
h3cDot11StationRxDataFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationRxDataFrameBytes.setStatus("current")
_H3cDot11StationTxDataFrameBytes_Type = Counter64
_H3cDot11StationTxDataFrameBytes_Object = MibTableColumn
h3cDot11StationTxDataFrameBytes = _H3cDot11StationTxDataFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 3, 1, 17),
    _H3cDot11StationTxDataFrameBytes_Type()
)
h3cDot11StationTxDataFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationTxDataFrameBytes.setStatus("current")
_H3cDot11StationRxFragCnt_Type = Counter32
_H3cDot11StationRxFragCnt_Object = MibTableColumn
h3cDot11StationRxFragCnt = _H3cDot11StationRxFragCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 3, 1, 18),
    _H3cDot11StationRxFragCnt_Type()
)
h3cDot11StationRxFragCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationRxFragCnt.setStatus("current")
_H3cDot11StaRxErrDataFrameCnt_Type = Counter64
_H3cDot11StaRxErrDataFrameCnt_Object = MibTableColumn
h3cDot11StaRxErrDataFrameCnt = _H3cDot11StaRxErrDataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 3, 1, 19),
    _H3cDot11StaRxErrDataFrameCnt_Type()
)
h3cDot11StaRxErrDataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StaRxErrDataFrameCnt.setStatus("current")
_H3cDot11StaTxRetryDataFrameCnt_Type = Counter64
_H3cDot11StaTxRetryDataFrameCnt_Object = MibTableColumn
h3cDot11StaTxRetryDataFrameCnt = _H3cDot11StaTxRetryDataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 3, 1, 20),
    _H3cDot11StaTxRetryDataFrameCnt_Type()
)
h3cDot11StaTxRetryDataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StaTxRetryDataFrameCnt.setStatus("current")
_H3cDot11StaTxDataRatePkts_Type = OctetString
_H3cDot11StaTxDataRatePkts_Object = MibTableColumn
h3cDot11StaTxDataRatePkts = _H3cDot11StaTxDataRatePkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 3, 1, 21),
    _H3cDot11StaTxDataRatePkts_Type()
)
h3cDot11StaTxDataRatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StaTxDataRatePkts.setStatus("current")
_H3cDot11StaRxDataRatePkts_Type = OctetString
_H3cDot11StaRxDataRatePkts_Object = MibTableColumn
h3cDot11StaRxDataRatePkts = _H3cDot11StaRxDataRatePkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 3, 1, 22),
    _H3cDot11StaRxDataRatePkts_Type()
)
h3cDot11StaRxDataRatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StaRxDataRatePkts.setStatus("current")
_H3cDot11StaTxSignalStrengthPkts_Type = OctetString
_H3cDot11StaTxSignalStrengthPkts_Object = MibTableColumn
h3cDot11StaTxSignalStrengthPkts = _H3cDot11StaTxSignalStrengthPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 3, 1, 23),
    _H3cDot11StaTxSignalStrengthPkts_Type()
)
h3cDot11StaTxSignalStrengthPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StaTxSignalStrengthPkts.setStatus("current")
_H3cDot11StaInternetRxFrameBytes_Type = Counter64
_H3cDot11StaInternetRxFrameBytes_Object = MibTableColumn
h3cDot11StaInternetRxFrameBytes = _H3cDot11StaInternetRxFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 3, 1, 24),
    _H3cDot11StaInternetRxFrameBytes_Type()
)
h3cDot11StaInternetRxFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StaInternetRxFrameBytes.setStatus("current")
_H3cDot11StaInternetTxFrameBytes_Type = Counter64
_H3cDot11StaInternetTxFrameBytes_Object = MibTableColumn
h3cDot11StaInternetTxFrameBytes = _H3cDot11StaInternetTxFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 3, 1, 25),
    _H3cDot11StaInternetTxFrameBytes_Type()
)
h3cDot11StaInternetTxFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StaInternetTxFrameBytes.setStatus("current")
_H3cDot11StaLocalRxFrameBytes_Type = Counter64
_H3cDot11StaLocalRxFrameBytes_Object = MibTableColumn
h3cDot11StaLocalRxFrameBytes = _H3cDot11StaLocalRxFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 3, 1, 26),
    _H3cDot11StaLocalRxFrameBytes_Type()
)
h3cDot11StaLocalRxFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StaLocalRxFrameBytes.setStatus("current")
_H3cDot11StaLocalTxFrameBytes_Type = Counter64
_H3cDot11StaLocalTxFrameBytes_Object = MibTableColumn
h3cDot11StaLocalTxFrameBytes = _H3cDot11StaLocalTxFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 3, 1, 27),
    _H3cDot11StaLocalTxFrameBytes_Type()
)
h3cDot11StaLocalTxFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StaLocalTxFrameBytes.setStatus("current")
_H3cDot11StationRfPingTable_Object = MibTable
h3cDot11StationRfPingTable = _H3cDot11StationRfPingTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 4)
)
if mibBuilder.loadTexts:
    h3cDot11StationRfPingTable.setStatus("current")
_H3cDot11StationRfPingEntry_Object = MibTableRow
h3cDot11StationRfPingEntry = _H3cDot11StationRfPingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 4, 1)
)
h3cDot11StationRfPingEntry.setIndexNames(
    (0, "H3C-DOT11-STATION-MIB", "h3cDot11StationMAC"),
    (0, "H3C-DOT11-STATION-MIB", "h3cDot11StationRfPingIndex"),
)
if mibBuilder.loadTexts:
    h3cDot11StationRfPingEntry.setStatus("current")


class _H3cDot11StationRfPingIndex_Type(Integer32):
    """Custom type h3cDot11StationRfPingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 214783647),
    )


_H3cDot11StationRfPingIndex_Type.__name__ = "Integer32"
_H3cDot11StationRfPingIndex_Object = MibTableColumn
h3cDot11StationRfPingIndex = _H3cDot11StationRfPingIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 4, 1, 1),
    _H3cDot11StationRfPingIndex_Type()
)
h3cDot11StationRfPingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11StationRfPingIndex.setStatus("current")
_H3cDot11StationRfPingRate_Type = OctetString
_H3cDot11StationRfPingRate_Object = MibTableColumn
h3cDot11StationRfPingRate = _H3cDot11StationRfPingRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 4, 1, 2),
    _H3cDot11StationRfPingRate_Type()
)
h3cDot11StationRfPingRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationRfPingRate.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11StationRfPingRate.setUnits("Mbps")
_H3cDot11StationRfPingTxCnt_Type = Integer32
_H3cDot11StationRfPingTxCnt_Object = MibTableColumn
h3cDot11StationRfPingTxCnt = _H3cDot11StationRfPingTxCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 4, 1, 3),
    _H3cDot11StationRfPingTxCnt_Type()
)
h3cDot11StationRfPingTxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationRfPingTxCnt.setStatus("current")
_H3cDot11StationRfPingRxCnt_Type = Integer32
_H3cDot11StationRfPingRxCnt_Object = MibTableColumn
h3cDot11StationRfPingRxCnt = _H3cDot11StationRfPingRxCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 4, 1, 4),
    _H3cDot11StationRfPingRxCnt_Type()
)
h3cDot11StationRfPingRxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationRfPingRxCnt.setStatus("current")
_H3cDot11StationRfPingRssi_Type = Integer32
_H3cDot11StationRfPingRssi_Object = MibTableColumn
h3cDot11StationRfPingRssi = _H3cDot11StationRfPingRssi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 4, 1, 5),
    _H3cDot11StationRfPingRssi_Type()
)
h3cDot11StationRfPingRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationRfPingRssi.setStatus("current")
_H3cDot11StationRfPingRetries_Type = Integer32
_H3cDot11StationRfPingRetries_Object = MibTableColumn
h3cDot11StationRfPingRetries = _H3cDot11StationRfPingRetries_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 4, 1, 6),
    _H3cDot11StationRfPingRetries_Type()
)
h3cDot11StationRfPingRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationRfPingRetries.setStatus("current")
_H3cDot11StationRfPingRtt_Type = Integer32
_H3cDot11StationRfPingRtt_Object = MibTableColumn
h3cDot11StationRfPingRtt = _H3cDot11StationRfPingRtt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 1, 4, 1, 7),
    _H3cDot11StationRfPingRtt_Type()
)
h3cDot11StationRfPingRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationRfPingRtt.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11StationRfPingRtt.setUnits("ms")
_H3cDot11StationNotifyGroup_ObjectIdentity = ObjectIdentity
h3cDot11StationNotifyGroup = _H3cDot11StationNotifyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 2)
)
_H3cDot11StationTraps_ObjectIdentity = ObjectIdentity
h3cDot11StationTraps = _H3cDot11StationTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 2, 0)
)
_H3cDot11StationTrapVarObjects_ObjectIdentity = ObjectIdentity
h3cDot11StationTrapVarObjects = _H3cDot11StationTrapVarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 2, 1)
)
_H3cDot11StationTrapBSSID_Type = MacAddress
_H3cDot11StationTrapBSSID_Object = MibScalar
h3cDot11StationTrapBSSID = _H3cDot11StationTrapBSSID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 2, 1, 1),
    _H3cDot11StationTrapBSSID_Type()
)
h3cDot11StationTrapBSSID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11StationTrapBSSID.setStatus("current")
_H3cDot11StationTrapStaMAC_Type = MacAddress
_H3cDot11StationTrapStaMAC_Object = MibScalar
h3cDot11StationTrapStaMAC = _H3cDot11StationTrapStaMAC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 2, 1, 2),
    _H3cDot11StationTrapStaMAC_Type()
)
h3cDot11StationTrapStaMAC.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11StationTrapStaMAC.setStatus("current")
_H3cDot11StationSessionStartTime_Type = DateAndTime
_H3cDot11StationSessionStartTime_Object = MibScalar
h3cDot11StationSessionStartTime = _H3cDot11StationSessionStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 2, 1, 3),
    _H3cDot11StationSessionStartTime_Type()
)
h3cDot11StationSessionStartTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11StationSessionStartTime.setStatus("current")
_H3cDot11StationAssocFailCause_Type = H3cDot11AssocFailType
_H3cDot11StationAssocFailCause_Object = MibScalar
h3cDot11StationAssocFailCause = _H3cDot11StationAssocFailCause_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 2, 1, 4),
    _H3cDot11StationAssocFailCause_Type()
)
h3cDot11StationAssocFailCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11StationAssocFailCause.setStatus("current")
_H3cDot11StationAuthorFailCause_Type = H3cDot11AuthorFailType
_H3cDot11StationAuthorFailCause_Object = MibScalar
h3cDot11StationAuthorFailCause = _H3cDot11StationAuthorFailCause_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 2, 1, 5),
    _H3cDot11StationAuthorFailCause_Type()
)
h3cDot11StationAuthorFailCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11StationAuthorFailCause.setStatus("current")


class _H3cDot11StationFailCauseDesc_Type(OctetString):
    """Custom type h3cDot11StationFailCauseDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cDot11StationFailCauseDesc_Type.__name__ = "OctetString"
_H3cDot11StationFailCauseDesc_Object = MibScalar
h3cDot11StationFailCauseDesc = _H3cDot11StationFailCauseDesc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 2, 1, 6),
    _H3cDot11StationFailCauseDesc_Type()
)
h3cDot11StationFailCauseDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11StationFailCauseDesc.setStatus("current")
_H3cDot11StationSessionDuration_Type = Unsigned32
_H3cDot11StationSessionDuration_Object = MibScalar
h3cDot11StationSessionDuration = _H3cDot11StationSessionDuration_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 2, 1, 7),
    _H3cDot11StationSessionDuration_Type()
)
h3cDot11StationSessionDuration.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11StationSessionDuration.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11StationSessionDuration.setUnits("second")
_H3cDot11StationRoamingTime_Type = Unsigned32
_H3cDot11StationRoamingTime_Object = MibScalar
h3cDot11StationRoamingTime = _H3cDot11StationRoamingTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 2, 1, 8),
    _H3cDot11StationRoamingTime_Type()
)
h3cDot11StationRoamingTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11StationRoamingTime.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11StationRoamingTime.setUnits("second")
_H3cDot11StationACIPAddress_Type = IpAddress
_H3cDot11StationACIPAddress_Object = MibScalar
h3cDot11StationACIPAddress = _H3cDot11StationACIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 2, 1, 9),
    _H3cDot11StationACIPAddress_Type()
)
h3cDot11StationACIPAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11StationACIPAddress.setStatus("current")
_H3cDot11StationAPName_Type = OctetString
_H3cDot11StationAPName_Object = MibScalar
h3cDot11StationAPName = _H3cDot11StationAPName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 2, 1, 10),
    _H3cDot11StationAPName_Type()
)
h3cDot11StationAPName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11StationAPName.setStatus("current")
_H3cDot11StationBSSID_Type = MacAddress
_H3cDot11StationBSSID_Object = MibScalar
h3cDot11StationBSSID = _H3cDot11StationBSSID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 2, 1, 11),
    _H3cDot11StationBSSID_Type()
)
h3cDot11StationBSSID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11StationBSSID.setStatus("current")
_H3cDot11StaDisconnectReason_Type = OctetString
_H3cDot11StaDisconnectReason_Object = MibScalar
h3cDot11StaDisconnectReason = _H3cDot11StaDisconnectReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 2, 1, 12),
    _H3cDot11StaDisconnectReason_Type()
)
h3cDot11StaDisconnectReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11StaDisconnectReason.setStatus("current")


class _H3cDot11StationAuthMode_Type(Integer32):
    """Custom type h3cDot11StationAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("opensystem", 1),
          ("sharedkey", 2))
    )


_H3cDot11StationAuthMode_Type.__name__ = "Integer32"
_H3cDot11StationAuthMode_Object = MibScalar
h3cDot11StationAuthMode = _H3cDot11StationAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 2, 1, 13),
    _H3cDot11StationAuthMode_Type()
)
h3cDot11StationAuthMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11StationAuthMode.setStatus("current")
_H3cDot11StationACIPv6Add_Type = OctetString
_H3cDot11StationACIPv6Add_Object = MibScalar
h3cDot11StationACIPv6Add = _H3cDot11StationACIPv6Add_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 2, 1, 14),
    _H3cDot11StationACIPv6Add_Type()
)
h3cDot11StationACIPv6Add.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11StationACIPv6Add.setStatus("current")
_H3cDot11UserName_Type = OctetString
_H3cDot11UserName_Object = MibScalar
h3cDot11UserName = _H3cDot11UserName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 2, 1, 15),
    _H3cDot11UserName_Type()
)
h3cDot11UserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11UserName.setStatus("current")
_H3cDot11StationTrapAPMacAddress_Type = MacAddress
_H3cDot11StationTrapAPMacAddress_Object = MibScalar
h3cDot11StationTrapAPMacAddress = _H3cDot11StationTrapAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 2, 1, 16),
    _H3cDot11StationTrapAPMacAddress_Type()
)
h3cDot11StationTrapAPMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11StationTrapAPMacAddress.setStatus("current")
_H3cDot11StationTrapOldAntennaID_Type = Integer32
_H3cDot11StationTrapOldAntennaID_Object = MibScalar
h3cDot11StationTrapOldAntennaID = _H3cDot11StationTrapOldAntennaID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 2, 1, 17),
    _H3cDot11StationTrapOldAntennaID_Type()
)
h3cDot11StationTrapOldAntennaID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11StationTrapOldAntennaID.setStatus("current")
_H3cDot11StationTrapNewAntennaID_Type = Integer32
_H3cDot11StationTrapNewAntennaID_Object = MibScalar
h3cDot11StationTrapNewAntennaID = _H3cDot11StationTrapNewAntennaID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 2, 1, 18),
    _H3cDot11StationTrapNewAntennaID_Type()
)
h3cDot11StationTrapNewAntennaID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11StationTrapNewAntennaID.setStatus("current")
_H3cDot11StationTrapAPIPAddress_Type = IpAddress
_H3cDot11StationTrapAPIPAddress_Object = MibScalar
h3cDot11StationTrapAPIPAddress = _H3cDot11StationTrapAPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 2, 1, 19),
    _H3cDot11StationTrapAPIPAddress_Type()
)
h3cDot11StationTrapAPIPAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11StationTrapAPIPAddress.setStatus("current")
_H3cDot11StationTrapStartTime_Type = Unsigned32
_H3cDot11StationTrapStartTime_Object = MibScalar
h3cDot11StationTrapStartTime = _H3cDot11StationTrapStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 2, 1, 20),
    _H3cDot11StationTrapStartTime_Type()
)
h3cDot11StationTrapStartTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11StationTrapStartTime.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11StationTrapStartTime.setUnits("second")
_H3cDot11StationAuditTrapOpType_Type = Unsigned32
_H3cDot11StationAuditTrapOpType_Object = MibScalar
h3cDot11StationAuditTrapOpType = _H3cDot11StationAuditTrapOpType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 2, 1, 21),
    _H3cDot11StationAuditTrapOpType_Type()
)
h3cDot11StationAuditTrapOpType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11StationAuditTrapOpType.setStatus("current")
_H3cDot11StationTrapStaIPAddress_Type = IpAddress
_H3cDot11StationTrapStaIPAddress_Object = MibScalar
h3cDot11StationTrapStaIPAddress = _H3cDot11StationTrapStaIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 2, 1, 22),
    _H3cDot11StationTrapStaIPAddress_Type()
)
h3cDot11StationTrapStaIPAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11StationTrapStaIPAddress.setStatus("current")
_H3cDot11StationTrapRadioID_Type = H3cDot11RadioScopeType
_H3cDot11StationTrapRadioID_Object = MibScalar
h3cDot11StationTrapRadioID = _H3cDot11StationTrapRadioID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 2, 1, 23),
    _H3cDot11StationTrapRadioID_Type()
)
h3cDot11StationTrapRadioID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11StationTrapRadioID.setStatus("current")
_H3cDot11StationTrapRadioMode_Type = H3cDot11RadioType2
_H3cDot11StationTrapRadioMode_Object = MibScalar
h3cDot11StationTrapRadioMode = _H3cDot11StationTrapRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 2, 1, 24),
    _H3cDot11StationTrapRadioMode_Type()
)
h3cDot11StationTrapRadioMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11StationTrapRadioMode.setStatus("current")
_H3cDot11StationTrapWlanID_Type = Integer32
_H3cDot11StationTrapWlanID_Object = MibScalar
h3cDot11StationTrapWlanID = _H3cDot11StationTrapWlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 2, 1, 25),
    _H3cDot11StationTrapWlanID_Type()
)
h3cDot11StationTrapWlanID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11StationTrapWlanID.setStatus("current")
_H3cDot11StationTrapSSIDName_Type = H3cDot11SSIDStringType
_H3cDot11StationTrapSSIDName_Object = MibScalar
h3cDot11StationTrapSSIDName = _H3cDot11StationTrapSSIDName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 2, 1, 26),
    _H3cDot11StationTrapSSIDName_Type()
)
h3cDot11StationTrapSSIDName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11StationTrapSSIDName.setStatus("current")
_H3cDot11StationTrapVlan_Type = Integer32
_H3cDot11StationTrapVlan_Object = MibScalar
h3cDot11StationTrapVlan = _H3cDot11StationTrapVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 2, 1, 27),
    _H3cDot11StationTrapVlan_Type()
)
h3cDot11StationTrapVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11StationTrapVlan.setStatus("current")
_H3cDot11StationTrapChannel_Type = H3cDot11ChannelScopeType
_H3cDot11StationTrapChannel_Object = MibScalar
h3cDot11StationTrapChannel = _H3cDot11StationTrapChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 2, 1, 28),
    _H3cDot11StationTrapChannel_Type()
)
h3cDot11StationTrapChannel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11StationTrapChannel.setStatus("current")
_H3cDot11StationTrapRSSI_Type = Integer32
_H3cDot11StationTrapRSSI_Object = MibScalar
h3cDot11StationTrapRSSI = _H3cDot11StationTrapRSSI_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 2, 1, 29),
    _H3cDot11StationTrapRSSI_Type()
)
h3cDot11StationTrapRSSI.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11StationTrapRSSI.setStatus("current")
_H3cDot11StationTrapRxFrameKbit_Type = Counter64
_H3cDot11StationTrapRxFrameKbit_Object = MibScalar
h3cDot11StationTrapRxFrameKbit = _H3cDot11StationTrapRxFrameKbit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 2, 1, 30),
    _H3cDot11StationTrapRxFrameKbit_Type()
)
h3cDot11StationTrapRxFrameKbit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11StationTrapRxFrameKbit.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11StationTrapRxFrameKbit.setUnits("kbit")
_H3cDot11StationTrapTxFrameKbit_Type = Counter64
_H3cDot11StationTrapTxFrameKbit_Object = MibScalar
h3cDot11StationTrapTxFrameKbit = _H3cDot11StationTrapTxFrameKbit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 2, 1, 31),
    _H3cDot11StationTrapTxFrameKbit_Type()
)
h3cDot11StationTrapTxFrameKbit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11StationTrapTxFrameKbit.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11StationTrapTxFrameKbit.setUnits("kbit")

# Managed Objects groups


# Notification objects

h3cDot11StationMICErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 2, 0, 1)
)
h3cDot11StationMICErrorTrap.setObjects(
      *(("H3C-DOT11-STATION-MIB", "h3cDot11CurrAPID"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11CurrRadioID"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationTrapBSSID"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationSSIDName"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationTrapStaMAC"))
)
if mibBuilder.loadTexts:
    h3cDot11StationMICErrorTrap.setStatus(
        "current"
    )

h3cDot11StationAuthenErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 2, 0, 2)
)
h3cDot11StationAuthenErrorTrap.setObjects(
      *(("H3C-DOT11-STATION-MIB", "h3cDot11CurrAPID"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11CurrRadioID"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationTrapBSSID"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationSSIDName"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationTrapStaMAC"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationAuthenMode"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationAKMMode"))
)
if mibBuilder.loadTexts:
    h3cDot11StationAuthenErrorTrap.setStatus(
        "current"
    )

h3cDot11StationAuthorFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 2, 0, 3)
)
h3cDot11StationAuthorFailTrap.setObjects(
      *(("H3C-DOT11-STATION-MIB", "h3cDot11StationUserName"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationTrapStaMAC"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11CurrRadioID"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationSSIDName"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationAuthorFailCause"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationFailCauseDesc"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11CurrAPID"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationBSSID"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationAuthMode"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    h3cDot11StationAuthorFailTrap.setStatus(
        "current"
    )

h3cDot11StationAssocFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 2, 0, 4)
)
h3cDot11StationAssocFailTrap.setObjects(
      *(("H3C-DOT11-STATION-MIB", "h3cDot11StationTrapStaMAC"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11CurrRadioID"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationSSIDName"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationAssocFailCause"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationFailCauseDesc"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11CurrAPID"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationTrapAPMacAddress"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationBSSID"))
)
if mibBuilder.loadTexts:
    h3cDot11StationAssocFailTrap.setStatus(
        "current"
    )

h3cDot11StationDeAssocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 2, 0, 5)
)
h3cDot11StationDeAssocTrap.setObjects(
      *(("H3C-DOT11-STATION-MIB", "h3cDot11StationUserName"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationTrapStaMAC"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationVlanId"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11CurrRadioID"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationSSIDName"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationSessionDuration"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11CurrAPID"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationAPName"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationBSSID"))
)
if mibBuilder.loadTexts:
    h3cDot11StationDeAssocTrap.setStatus(
        "current"
    )

h3cDot11StationAuthorSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 2, 0, 6)
)
h3cDot11StationAuthorSuccTrap.setObjects(
      *(("H3C-DOT11-STATION-MIB", "h3cDot11StationUserName"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationTrapStaMAC"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationVlanId"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationSessionStartTime"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11CurrRadioID"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationSSIDName"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11CurrAPID"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationAPName"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationBSSID"))
)
if mibBuilder.loadTexts:
    h3cDot11StationAuthorSuccTrap.setStatus(
        "current"
    )

h3cDot11StationRoamingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 2, 0, 7)
)
h3cDot11StationRoamingTrap.setObjects(
      *(("H3C-DOT11-STATION-MIB", "h3cDot11CurrAPID"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationUserName"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationTrapStaMAC"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationVlanId"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationRoamingTime"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11CurrRadioID"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationSSIDName"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationACIPAddress"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationACIPv6Add"))
)
if mibBuilder.loadTexts:
    h3cDot11StationRoamingTrap.setStatus(
        "current"
    )

h3cDot11StationDisconnectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 2, 0, 8)
)
h3cDot11StationDisconnectTrap.setObjects(
      *(("H3C-DOT11-STATION-MIB", "h3cDot11StationAPName"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationBSSID"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationSSIDName"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationSessionDuration"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationVlanId"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11CurrAPID"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11CurrRadioID"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StaDisconnectReason"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationTrapStaMAC"))
)
if mibBuilder.loadTexts:
    h3cDot11StationDisconnectTrap.setStatus(
        "current"
    )

h3cDot11UserDisconnectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 2, 0, 9)
)
h3cDot11UserDisconnectTrap.setObjects(
      *(("H3C-DOT11-STATION-MIB", "h3cDot11StationAPName"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationTrapStaMAC"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11UserName"))
)
if mibBuilder.loadTexts:
    h3cDot11UserDisconnectTrap.setStatus(
        "current"
    )

h3cDot11StaAntennaChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 2, 0, 10)
)
h3cDot11StaAntennaChgTrap.setObjects(
      *(("H3C-DOT11-STATION-MIB", "h3cDot11CurrAPID"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11CurrRadioID"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationTrapBSSID"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationSSIDName"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationTrapStaMAC"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationTrapOldAntennaID"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationTrapNewAntennaID"))
)
if mibBuilder.loadTexts:
    h3cDot11StaAntennaChgTrap.setStatus(
        "current"
    )

h3cDot11StationAuditTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 3, 2, 0, 11)
)
h3cDot11StationAuditTrap.setObjects(
      *(("H3C-DOT11-STATION-MIB", "h3cDot11StationAuditTrapOpType"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationTrapStaMAC"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationTrapStaIPAddress"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationTrapAPMacAddress"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationTrapAPIPAddress"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationTrapRadioID"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationTrapRadioMode"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationTrapWlanID"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationTrapSSIDName"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationTrapVlan"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationTrapChannel"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationTrapRSSI"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationTrapStartTime"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationSessionDuration"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationTrapRxFrameKbit"),
        ("H3C-DOT11-STATION-MIB", "h3cDot11StationTrapTxFrameKbit"))
)
if mibBuilder.loadTexts:
    h3cDot11StationAuditTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-DOT11-STATION-MIB",
    **{"h3cDot11STATION": h3cDot11STATION,
       "h3cDot11StationMtGroup": h3cDot11StationMtGroup,
       "h3cDot11StationAssociateTable": h3cDot11StationAssociateTable,
       "h3cDot11StationAssociateEntry": h3cDot11StationAssociateEntry,
       "h3cDot11StationMAC": h3cDot11StationMAC,
       "h3cDot11StationIPAddress": h3cDot11StationIPAddress,
       "h3cDot11StationUserName": h3cDot11StationUserName,
       "h3cDot11StationTxRateSet": h3cDot11StationTxRateSet,
       "h3cDot11StationUpTime": h3cDot11StationUpTime,
       "h3cDot11StationSignalStrength": h3cDot11StationSignalStrength,
       "h3cDot11StationRSSI": h3cDot11StationRSSI,
       "h3cDot11StationChannel": h3cDot11StationChannel,
       "h3cDot11StationPowerSaveMode": h3cDot11StationPowerSaveMode,
       "h3cDot11StationAid": h3cDot11StationAid,
       "h3cDot11StationVlanId": h3cDot11StationVlanId,
       "h3cDot11StationSSIDName": h3cDot11StationSSIDName,
       "h3cDot11StationAuthenMode": h3cDot11StationAuthenMode,
       "h3cDot11StationAKMMode": h3cDot11StationAKMMode,
       "h3cDot11StationSecurityCiphers": h3cDot11StationSecurityCiphers,
       "h3cDot11StationSSIDEncryptMode": h3cDot11StationSSIDEncryptMode,
       "h3cDot11StationRxSNR": h3cDot11StationRxSNR,
       "h3cDot11StationTxRate": h3cDot11StationTxRate,
       "h3cDot11StationRxRate": h3cDot11StationRxRate,
       "h3cDot11StationVendorName": h3cDot11StationVendorName,
       "h3cDot11StationRadioMode": h3cDot11StationRadioMode,
       "h3cDot11StationRxNoise": h3cDot11StationRxNoise,
       "h3cDot11StationMACAddress": h3cDot11StationMACAddress,
       "h3cDot11StationTxSpeed": h3cDot11StationTxSpeed,
       "h3cDot11StationRxSpeed": h3cDot11StationRxSpeed,
       "h3cDot11StationWmmMode": h3cDot11StationWmmMode,
       "h3cDot11StationSecIEStatus": h3cDot11StationSecIEStatus,
       "h3cDot11StationUpTimeTicks": h3cDot11StationUpTimeTicks,
       "h3cDot11StationRadioMode2": h3cDot11StationRadioMode2,
       "h3cDot11StationAssTime": h3cDot11StationAssTime,
       "h3cDot11StationUserAuthType": h3cDot11StationUserAuthType,
       "h3cDot11StationRfPingTest": h3cDot11StationRfPingTest,
       "h3cDot11StationMaxRate": h3cDot11StationMaxRate,
       "h3cDot11StationPowerSaveModeCM": h3cDot11StationPowerSaveModeCM,
       "h3cDot11StationAuthenModeCM": h3cDot11StationAuthenModeCM,
       "h3cDot11StationAKMModeCM": h3cDot11StationAKMModeCM,
       "h3cDot11StationSecurityCiphersCM": h3cDot11StationSecurityCiphersCM,
       "h3cDot11StationSecIEStatusCM": h3cDot11StationSecIEStatusCM,
       "h3cDot11StationIPv6Address": h3cDot11StationIPv6Address,
       "h3cDot11StationAssociateAPMACAddressCM": h3cDot11StationAssociateAPMACAddressCM,
       "h3cDot11StationDeviceType": h3cDot11StationDeviceType,
       "h3cDot11StationTxRateCM": h3cDot11StationTxRateCM,
       "h3cDot11StationRxRateCM": h3cDot11StationRxRateCM,
       "h3cDot11StationAPRelationTable": h3cDot11StationAPRelationTable,
       "h3cDot11StationAPRelationEntry": h3cDot11StationAPRelationEntry,
       "h3cDot11CurrAPID": h3cDot11CurrAPID,
       "h3cDot11CurrRadioID": h3cDot11CurrRadioID,
       "h3cDot11CurrWlanID": h3cDot11CurrWlanID,
       "h3cDot11CurrAntennaID": h3cDot11CurrAntennaID,
       "h3cDot11StationStatisTable": h3cDot11StationStatisTable,
       "h3cDot11StationStatisEntry": h3cDot11StationStatisEntry,
       "h3cDot11StationRxFrameCnt": h3cDot11StationRxFrameCnt,
       "h3cDot11StationTxFrameCnt": h3cDot11StationTxFrameCnt,
       "h3cDot11StationDropFrameCnt": h3cDot11StationDropFrameCnt,
       "h3cDot11StationRxFrameBytes": h3cDot11StationRxFrameBytes,
       "h3cDot11StationTxFrameBytes": h3cDot11StationTxFrameBytes,
       "h3cDot11StationDropFrameBytes": h3cDot11StationDropFrameBytes,
       "h3cDot11StationRxRetryPkts": h3cDot11StationRxRetryPkts,
       "h3cDot11StationTxRetryPkts": h3cDot11StationTxRetryPkts,
       "h3cDot11StationRxRetryBytes": h3cDot11StationRxRetryBytes,
       "h3cDot11StationTxRetryBytes": h3cDot11StationTxRetryBytes,
       "h3cDot11StationThroughput": h3cDot11StationThroughput,
       "h3cDot11StationSuccessTxCnt": h3cDot11StationSuccessTxCnt,
       "h3cDot11StationSuccessTxDataCnt": h3cDot11StationSuccessTxDataCnt,
       "h3cDot11StationRxDataFrameCnt": h3cDot11StationRxDataFrameCnt,
       "h3cDot11StationTxDataFrameCnt": h3cDot11StationTxDataFrameCnt,
       "h3cDot11StationRxDataFrameBytes": h3cDot11StationRxDataFrameBytes,
       "h3cDot11StationTxDataFrameBytes": h3cDot11StationTxDataFrameBytes,
       "h3cDot11StationRxFragCnt": h3cDot11StationRxFragCnt,
       "h3cDot11StaRxErrDataFrameCnt": h3cDot11StaRxErrDataFrameCnt,
       "h3cDot11StaTxRetryDataFrameCnt": h3cDot11StaTxRetryDataFrameCnt,
       "h3cDot11StaTxDataRatePkts": h3cDot11StaTxDataRatePkts,
       "h3cDot11StaRxDataRatePkts": h3cDot11StaRxDataRatePkts,
       "h3cDot11StaTxSignalStrengthPkts": h3cDot11StaTxSignalStrengthPkts,
       "h3cDot11StaInternetRxFrameBytes": h3cDot11StaInternetRxFrameBytes,
       "h3cDot11StaInternetTxFrameBytes": h3cDot11StaInternetTxFrameBytes,
       "h3cDot11StaLocalRxFrameBytes": h3cDot11StaLocalRxFrameBytes,
       "h3cDot11StaLocalTxFrameBytes": h3cDot11StaLocalTxFrameBytes,
       "h3cDot11StationRfPingTable": h3cDot11StationRfPingTable,
       "h3cDot11StationRfPingEntry": h3cDot11StationRfPingEntry,
       "h3cDot11StationRfPingIndex": h3cDot11StationRfPingIndex,
       "h3cDot11StationRfPingRate": h3cDot11StationRfPingRate,
       "h3cDot11StationRfPingTxCnt": h3cDot11StationRfPingTxCnt,
       "h3cDot11StationRfPingRxCnt": h3cDot11StationRfPingRxCnt,
       "h3cDot11StationRfPingRssi": h3cDot11StationRfPingRssi,
       "h3cDot11StationRfPingRetries": h3cDot11StationRfPingRetries,
       "h3cDot11StationRfPingRtt": h3cDot11StationRfPingRtt,
       "h3cDot11StationNotifyGroup": h3cDot11StationNotifyGroup,
       "h3cDot11StationTraps": h3cDot11StationTraps,
       "h3cDot11StationMICErrorTrap": h3cDot11StationMICErrorTrap,
       "h3cDot11StationAuthenErrorTrap": h3cDot11StationAuthenErrorTrap,
       "h3cDot11StationAuthorFailTrap": h3cDot11StationAuthorFailTrap,
       "h3cDot11StationAssocFailTrap": h3cDot11StationAssocFailTrap,
       "h3cDot11StationDeAssocTrap": h3cDot11StationDeAssocTrap,
       "h3cDot11StationAuthorSuccTrap": h3cDot11StationAuthorSuccTrap,
       "h3cDot11StationRoamingTrap": h3cDot11StationRoamingTrap,
       "h3cDot11StationDisconnectTrap": h3cDot11StationDisconnectTrap,
       "h3cDot11UserDisconnectTrap": h3cDot11UserDisconnectTrap,
       "h3cDot11StaAntennaChgTrap": h3cDot11StaAntennaChgTrap,
       "h3cDot11StationAuditTrap": h3cDot11StationAuditTrap,
       "h3cDot11StationTrapVarObjects": h3cDot11StationTrapVarObjects,
       "h3cDot11StationTrapBSSID": h3cDot11StationTrapBSSID,
       "h3cDot11StationTrapStaMAC": h3cDot11StationTrapStaMAC,
       "h3cDot11StationSessionStartTime": h3cDot11StationSessionStartTime,
       "h3cDot11StationAssocFailCause": h3cDot11StationAssocFailCause,
       "h3cDot11StationAuthorFailCause": h3cDot11StationAuthorFailCause,
       "h3cDot11StationFailCauseDesc": h3cDot11StationFailCauseDesc,
       "h3cDot11StationSessionDuration": h3cDot11StationSessionDuration,
       "h3cDot11StationRoamingTime": h3cDot11StationRoamingTime,
       "h3cDot11StationACIPAddress": h3cDot11StationACIPAddress,
       "h3cDot11StationAPName": h3cDot11StationAPName,
       "h3cDot11StationBSSID": h3cDot11StationBSSID,
       "h3cDot11StaDisconnectReason": h3cDot11StaDisconnectReason,
       "h3cDot11StationAuthMode": h3cDot11StationAuthMode,
       "h3cDot11StationACIPv6Add": h3cDot11StationACIPv6Add,
       "h3cDot11UserName": h3cDot11UserName,
       "h3cDot11StationTrapAPMacAddress": h3cDot11StationTrapAPMacAddress,
       "h3cDot11StationTrapOldAntennaID": h3cDot11StationTrapOldAntennaID,
       "h3cDot11StationTrapNewAntennaID": h3cDot11StationTrapNewAntennaID,
       "h3cDot11StationTrapAPIPAddress": h3cDot11StationTrapAPIPAddress,
       "h3cDot11StationTrapStartTime": h3cDot11StationTrapStartTime,
       "h3cDot11StationAuditTrapOpType": h3cDot11StationAuditTrapOpType,
       "h3cDot11StationTrapStaIPAddress": h3cDot11StationTrapStaIPAddress,
       "h3cDot11StationTrapRadioID": h3cDot11StationTrapRadioID,
       "h3cDot11StationTrapRadioMode": h3cDot11StationTrapRadioMode,
       "h3cDot11StationTrapWlanID": h3cDot11StationTrapWlanID,
       "h3cDot11StationTrapSSIDName": h3cDot11StationTrapSSIDName,
       "h3cDot11StationTrapVlan": h3cDot11StationTrapVlan,
       "h3cDot11StationTrapChannel": h3cDot11StationTrapChannel,
       "h3cDot11StationTrapRSSI": h3cDot11StationTrapRSSI,
       "h3cDot11StationTrapRxFrameKbit": h3cDot11StationTrapRxFrameKbit,
       "h3cDot11StationTrapTxFrameKbit": h3cDot11StationTrapTxFrameKbit}
)
