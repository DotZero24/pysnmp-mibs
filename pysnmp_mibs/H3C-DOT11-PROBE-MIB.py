# SNMP MIB module (H3C-DOT11-PROBE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-DOT11-PROBE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:17:33 2025
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

(h3cDot11,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
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

h3cDot11PROBE = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17)
)
if mibBuilder.loadTexts:
    h3cDot11PROBE.setRevisions(
        ("2016-03-28 09:51",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class H3cDot11PROBEEnabledStatus(TextualConvention, Integer32):
    status = "current"
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



class H3cDot11PROBERadioType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128)
        )
    )
    namedValues = NamedValues(
        *(("dot11a", 1),
          ("dot11b", 2),
          ("dot11g", 4),
          ("dot11n", 8),
          ("dot11gn", 16),
          ("dot11an", 32),
          ("dot11ac", 64),
          ("dot11gac", 128))
    )



class H3cDot11PROBEDevStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )



class H3cDot11PROBEChannel(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 224),
    )



class H3cDot11PROBEEncryptMethod(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class H3cDot11PROBEAuthMethod(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class H3cDot11PROBESecurityType(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



# MIB Managed Objects in the order of their OIDs

_H3cDot11PROBEConfigGroup_ObjectIdentity = ObjectIdentity
h3cDot11PROBEConfigGroup = _H3cDot11PROBEConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 1)
)
_H3cDot11PROBERadioCfgTable_Object = MibTable
h3cDot11PROBERadioCfgTable = _H3cDot11PROBERadioCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 1, 1)
)
if mibBuilder.loadTexts:
    h3cDot11PROBERadioCfgTable.setStatus("current")
_H3cDot11PROBERadioCfgEntry_Object = MibTableRow
h3cDot11PROBERadioCfgEntry = _H3cDot11PROBERadioCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 1, 1, 1)
)
h3cDot11PROBERadioCfgEntry.setIndexNames(
    (0, "H3C-DOT11-PROBE-MIB", "h3cDot11PROBERadioCfgApName"),
    (0, "H3C-DOT11-PROBE-MIB", "h3cDot11PROBERadioCfgRadioId"),
)
if mibBuilder.loadTexts:
    h3cDot11PROBERadioCfgEntry.setStatus("current")


class _H3cDot11PROBERadioCfgApName_Type(OctetString):
    """Custom type h3cDot11PROBERadioCfgApName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_H3cDot11PROBERadioCfgApName_Type.__name__ = "OctetString"
_H3cDot11PROBERadioCfgApName_Object = MibTableColumn
h3cDot11PROBERadioCfgApName = _H3cDot11PROBERadioCfgApName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 1, 1, 1, 1),
    _H3cDot11PROBERadioCfgApName_Type()
)
h3cDot11PROBERadioCfgApName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11PROBERadioCfgApName.setStatus("current")


class _H3cDot11PROBERadioCfgRadioId_Type(Integer32):
    """Custom type h3cDot11PROBERadioCfgRadioId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_H3cDot11PROBERadioCfgRadioId_Type.__name__ = "Integer32"
_H3cDot11PROBERadioCfgRadioId_Object = MibTableColumn
h3cDot11PROBERadioCfgRadioId = _H3cDot11PROBERadioCfgRadioId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 1, 1, 1, 2),
    _H3cDot11PROBERadioCfgRadioId_Type()
)
h3cDot11PROBERadioCfgRadioId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11PROBERadioCfgRadioId.setStatus("current")
_H3cDot11PROBERadioCfgStatus_Type = H3cDot11PROBEEnabledStatus
_H3cDot11PROBERadioCfgStatus_Object = MibTableColumn
h3cDot11PROBERadioCfgStatus = _H3cDot11PROBERadioCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 1, 1, 1, 3),
    _H3cDot11PROBERadioCfgStatus_Type()
)
h3cDot11PROBERadioCfgStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11PROBERadioCfgStatus.setStatus("current")
_H3cDot11PROBEDataGroup_ObjectIdentity = ObjectIdentity
h3cDot11PROBEDataGroup = _H3cDot11PROBEDataGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2)
)
_H3cDot11PROBEClientTable_Object = MibTable
h3cDot11PROBEClientTable = _H3cDot11PROBEClientTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 1)
)
if mibBuilder.loadTexts:
    h3cDot11PROBEClientTable.setStatus("current")
_H3cDot11PROBEClientEntry_Object = MibTableRow
h3cDot11PROBEClientEntry = _H3cDot11PROBEClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 1, 1)
)
h3cDot11PROBEClientEntry.setIndexNames(
    (0, "H3C-DOT11-PROBE-MIB", "h3cDot11PROBEClientMac"),
)
if mibBuilder.loadTexts:
    h3cDot11PROBEClientEntry.setStatus("current")
_H3cDot11PROBEClientMac_Type = MacAddress
_H3cDot11PROBEClientMac_Object = MibTableColumn
h3cDot11PROBEClientMac = _H3cDot11PROBEClientMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 1, 1, 1),
    _H3cDot11PROBEClientMac_Type()
)
h3cDot11PROBEClientMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11PROBEClientMac.setStatus("current")
_H3cDot11PROBEClientBSSID_Type = MacAddress
_H3cDot11PROBEClientBSSID_Object = MibTableColumn
h3cDot11PROBEClientBSSID = _H3cDot11PROBEClientBSSID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 1, 1, 2),
    _H3cDot11PROBEClientBSSID_Type()
)
h3cDot11PROBEClientBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBEClientBSSID.setStatus("current")


class _H3cDot11PROBEClientSSID_Type(OctetString):
    """Custom type h3cDot11PROBEClientSSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cDot11PROBEClientSSID_Type.__name__ = "OctetString"
_H3cDot11PROBEClientSSID_Object = MibTableColumn
h3cDot11PROBEClientSSID = _H3cDot11PROBEClientSSID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 1, 1, 3),
    _H3cDot11PROBEClientSSID_Type()
)
h3cDot11PROBEClientSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBEClientSSID.setStatus("current")
_H3cDot11PROBEClientIsDiss_Type = TruthValue
_H3cDot11PROBEClientIsDiss_Object = MibTableColumn
h3cDot11PROBEClientIsDiss = _H3cDot11PROBEClientIsDiss_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 1, 1, 4),
    _H3cDot11PROBEClientIsDiss_Type()
)
h3cDot11PROBEClientIsDiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBEClientIsDiss.setStatus("current")
_H3cDot11PROBEClientStatus_Type = H3cDot11PROBEDevStatus
_H3cDot11PROBEClientStatus_Object = MibTableColumn
h3cDot11PROBEClientStatus = _H3cDot11PROBEClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 1, 1, 5),
    _H3cDot11PROBEClientStatus_Type()
)
h3cDot11PROBEClientStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBEClientStatus.setStatus("current")
_H3cDot11PROBEClientDuratTime_Type = TimeTicks
_H3cDot11PROBEClientDuratTime_Object = MibTableColumn
h3cDot11PROBEClientDuratTime = _H3cDot11PROBEClientDuratTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 1, 1, 6),
    _H3cDot11PROBEClientDuratTime_Type()
)
h3cDot11PROBEClientDuratTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBEClientDuratTime.setStatus("current")


class _H3cDot11PROBEClientVendor_Type(OctetString):
    """Custom type h3cDot11PROBEClientVendor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_H3cDot11PROBEClientVendor_Type.__name__ = "OctetString"
_H3cDot11PROBEClientVendor_Object = MibTableColumn
h3cDot11PROBEClientVendor = _H3cDot11PROBEClientVendor_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 1, 1, 7),
    _H3cDot11PROBEClientVendor_Type()
)
h3cDot11PROBEClientVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBEClientVendor.setStatus("current")
_H3cDot11PROBEClientRptApNum_Type = Integer32
_H3cDot11PROBEClientRptApNum_Object = MibTableColumn
h3cDot11PROBEClientRptApNum = _H3cDot11PROBEClientRptApNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 1, 1, 8),
    _H3cDot11PROBEClientRptApNum_Type()
)
h3cDot11PROBEClientRptApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBEClientRptApNum.setStatus("current")
_H3cDot11PROBEClientWorkChannel_Type = H3cDot11PROBEChannel
_H3cDot11PROBEClientWorkChannel_Object = MibTableColumn
h3cDot11PROBEClientWorkChannel = _H3cDot11PROBEClientWorkChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 1, 1, 9),
    _H3cDot11PROBEClientWorkChannel_Type()
)
h3cDot11PROBEClientWorkChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBEClientWorkChannel.setStatus("current")
_H3cDot11PROBEClientRSSIMax_Type = Integer32
_H3cDot11PROBEClientRSSIMax_Object = MibTableColumn
h3cDot11PROBEClientRSSIMax = _H3cDot11PROBEClientRSSIMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 1, 1, 10),
    _H3cDot11PROBEClientRSSIMax_Type()
)
h3cDot11PROBEClientRSSIMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBEClientRSSIMax.setStatus("current")
_H3cDot11PROBEClientRSSIMin_Type = Integer32
_H3cDot11PROBEClientRSSIMin_Object = MibTableColumn
h3cDot11PROBEClientRSSIMin = _H3cDot11PROBEClientRSSIMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 1, 1, 11),
    _H3cDot11PROBEClientRSSIMin_Type()
)
h3cDot11PROBEClientRSSIMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBEClientRSSIMin.setStatus("current")
_H3cDot11PROBEClientRSSI_Type = Integer32
_H3cDot11PROBEClientRSSI_Object = MibTableColumn
h3cDot11PROBEClientRSSI = _H3cDot11PROBEClientRSSI_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 1, 1, 12),
    _H3cDot11PROBEClientRSSI_Type()
)
h3cDot11PROBEClientRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBEClientRSSI.setStatus("current")


class _H3cDot11PROBEClientFirstTime_Type(OctetString):
    """Custom type h3cDot11PROBEClientFirstTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_H3cDot11PROBEClientFirstTime_Type.__name__ = "OctetString"
_H3cDot11PROBEClientFirstTime_Object = MibTableColumn
h3cDot11PROBEClientFirstTime = _H3cDot11PROBEClientFirstTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 1, 1, 13),
    _H3cDot11PROBEClientFirstTime_Type()
)
h3cDot11PROBEClientFirstTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBEClientFirstTime.setStatus("current")


class _H3cDot11PROBEClientLastTime_Type(OctetString):
    """Custom type h3cDot11PROBEClientLastTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_H3cDot11PROBEClientLastTime_Type.__name__ = "OctetString"
_H3cDot11PROBEClientLastTime_Object = MibTableColumn
h3cDot11PROBEClientLastTime = _H3cDot11PROBEClientLastTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 1, 1, 14),
    _H3cDot11PROBEClientLastTime_Type()
)
h3cDot11PROBEClientLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBEClientLastTime.setStatus("current")
_H3cDot11PROBEStatTable_Object = MibTable
h3cDot11PROBEStatTable = _H3cDot11PROBEStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 2)
)
if mibBuilder.loadTexts:
    h3cDot11PROBEStatTable.setStatus("current")
_H3cDot11PROBEStatEntry_Object = MibTableRow
h3cDot11PROBEStatEntry = _H3cDot11PROBEStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 2, 1)
)
h3cDot11PROBEStatEntry.setIndexNames(
    (0, "H3C-DOT11-PROBE-MIB", "h3cDot11PROBEStatTime"),
)
if mibBuilder.loadTexts:
    h3cDot11PROBEStatEntry.setStatus("current")


class _H3cDot11PROBEStatTime_Type(OctetString):
    """Custom type h3cDot11PROBEStatTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_H3cDot11PROBEStatTime_Type.__name__ = "OctetString"
_H3cDot11PROBEStatTime_Object = MibTableColumn
h3cDot11PROBEStatTime = _H3cDot11PROBEStatTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 2, 1, 1),
    _H3cDot11PROBEStatTime_Type()
)
h3cDot11PROBEStatTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11PROBEStatTime.setStatus("current")
_H3cDot11PROBEStatRssiMaxNum_Type = Integer32
_H3cDot11PROBEStatRssiMaxNum_Object = MibTableColumn
h3cDot11PROBEStatRssiMaxNum = _H3cDot11PROBEStatRssiMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 2, 1, 2),
    _H3cDot11PROBEStatRssiMaxNum_Type()
)
h3cDot11PROBEStatRssiMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBEStatRssiMaxNum.setStatus("current")
_H3cDot11PROBEStatRssiMiddleNum_Type = Integer32
_H3cDot11PROBEStatRssiMiddleNum_Object = MibTableColumn
h3cDot11PROBEStatRssiMiddleNum = _H3cDot11PROBEStatRssiMiddleNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 2, 1, 3),
    _H3cDot11PROBEStatRssiMiddleNum_Type()
)
h3cDot11PROBEStatRssiMiddleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBEStatRssiMiddleNum.setStatus("current")
_H3cDot11PROBEStatRssiMinNum_Type = Integer32
_H3cDot11PROBEStatRssiMinNum_Object = MibTableColumn
h3cDot11PROBEStatRssiMinNum = _H3cDot11PROBEStatRssiMinNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 2, 1, 4),
    _H3cDot11PROBEStatRssiMinNum_Type()
)
h3cDot11PROBEStatRssiMinNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBEStatRssiMinNum.setStatus("current")
_H3cDot11PROBEStatTotalNum_Type = Integer32
_H3cDot11PROBEStatTotalNum_Object = MibTableColumn
h3cDot11PROBEStatTotalNum = _H3cDot11PROBEStatTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 2, 1, 5),
    _H3cDot11PROBEStatTotalNum_Type()
)
h3cDot11PROBEStatTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBEStatTotalNum.setStatus("current")
_H3cDot11PROBEStatAssocNum_Type = Integer32
_H3cDot11PROBEStatAssocNum_Object = MibTableColumn
h3cDot11PROBEStatAssocNum = _H3cDot11PROBEStatAssocNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 2, 1, 6),
    _H3cDot11PROBEStatAssocNum_Type()
)
h3cDot11PROBEStatAssocNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBEStatAssocNum.setStatus("current")
_H3cDot11PROBEStatDissocNum_Type = Integer32
_H3cDot11PROBEStatDissocNum_Object = MibTableColumn
h3cDot11PROBEStatDissocNum = _H3cDot11PROBEStatDissocNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 2, 1, 7),
    _H3cDot11PROBEStatDissocNum_Type()
)
h3cDot11PROBEStatDissocNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBEStatDissocNum.setStatus("current")
_H3cDot11PROBEApTable_Object = MibTable
h3cDot11PROBEApTable = _H3cDot11PROBEApTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 3)
)
if mibBuilder.loadTexts:
    h3cDot11PROBEApTable.setStatus("current")
_H3cDot11PROBEApEntry_Object = MibTableRow
h3cDot11PROBEApEntry = _H3cDot11PROBEApEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 3, 1)
)
h3cDot11PROBEApEntry.setIndexNames(
    (0, "H3C-DOT11-PROBE-MIB", "h3cDot11PROBEApMacAddress"),
)
if mibBuilder.loadTexts:
    h3cDot11PROBEApEntry.setStatus("current")
_H3cDot11PROBEApMacAddress_Type = MacAddress
_H3cDot11PROBEApMacAddress_Object = MibTableColumn
h3cDot11PROBEApMacAddress = _H3cDot11PROBEApMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 3, 1, 1),
    _H3cDot11PROBEApMacAddress_Type()
)
h3cDot11PROBEApMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11PROBEApMacAddress.setStatus("current")


class _H3cDot11PROBEApSsid_Type(OctetString):
    """Custom type h3cDot11PROBEApSsid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cDot11PROBEApSsid_Type.__name__ = "OctetString"
_H3cDot11PROBEApSsid_Object = MibTableColumn
h3cDot11PROBEApSsid = _H3cDot11PROBEApSsid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 3, 1, 2),
    _H3cDot11PROBEApSsid_Type()
)
h3cDot11PROBEApSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBEApSsid.setStatus("current")
_H3cDot11PROBEApStatus_Type = H3cDot11PROBEDevStatus
_H3cDot11PROBEApStatus_Object = MibTableColumn
h3cDot11PROBEApStatus = _H3cDot11PROBEApStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 3, 1, 3),
    _H3cDot11PROBEApStatus_Type()
)
h3cDot11PROBEApStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBEApStatus.setStatus("current")
_H3cDot11PROBEApStatusDuTime_Type = TimeTicks
_H3cDot11PROBEApStatusDuTime_Object = MibTableColumn
h3cDot11PROBEApStatusDuTime = _H3cDot11PROBEApStatusDuTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 3, 1, 4),
    _H3cDot11PROBEApStatusDuTime_Type()
)
h3cDot11PROBEApStatusDuTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBEApStatusDuTime.setStatus("current")


class _H3cDot11PROBEApVendor_Type(OctetString):
    """Custom type h3cDot11PROBEApVendor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_H3cDot11PROBEApVendor_Type.__name__ = "OctetString"
_H3cDot11PROBEApVendor_Object = MibTableColumn
h3cDot11PROBEApVendor = _H3cDot11PROBEApVendor_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 3, 1, 5),
    _H3cDot11PROBEApVendor_Type()
)
h3cDot11PROBEApVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBEApVendor.setStatus("current")
_H3cDot11PROBEApRadioType_Type = H3cDot11PROBERadioType
_H3cDot11PROBEApRadioType_Object = MibTableColumn
h3cDot11PROBEApRadioType = _H3cDot11PROBEApRadioType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 3, 1, 6),
    _H3cDot11PROBEApRadioType_Type()
)
h3cDot11PROBEApRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBEApRadioType.setStatus("current")
_H3cDot11PROBEApSecurityType_Type = H3cDot11PROBESecurityType
_H3cDot11PROBEApSecurityType_Object = MibTableColumn
h3cDot11PROBEApSecurityType = _H3cDot11PROBEApSecurityType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 3, 1, 7),
    _H3cDot11PROBEApSecurityType_Type()
)
h3cDot11PROBEApSecurityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBEApSecurityType.setStatus("current")
_H3cDot11PROBEApEncryMethod_Type = H3cDot11PROBEEncryptMethod
_H3cDot11PROBEApEncryMethod_Object = MibTableColumn
h3cDot11PROBEApEncryMethod = _H3cDot11PROBEApEncryMethod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 3, 1, 8),
    _H3cDot11PROBEApEncryMethod_Type()
)
h3cDot11PROBEApEncryMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBEApEncryMethod.setStatus("current")
_H3cDot11PROBEApAuthMethod_Type = H3cDot11PROBEAuthMethod
_H3cDot11PROBEApAuthMethod_Object = MibTableColumn
h3cDot11PROBEApAuthMethod = _H3cDot11PROBEApAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 3, 1, 9),
    _H3cDot11PROBEApAuthMethod_Type()
)
h3cDot11PROBEApAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBEApAuthMethod.setStatus("current")
_H3cDot11PROBEApIsBroadSSID_Type = TruthValue
_H3cDot11PROBEApIsBroadSSID_Object = MibTableColumn
h3cDot11PROBEApIsBroadSSID = _H3cDot11PROBEApIsBroadSSID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 3, 1, 10),
    _H3cDot11PROBEApIsBroadSSID_Type()
)
h3cDot11PROBEApIsBroadSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBEApIsBroadSSID.setStatus("current")
_H3cDot11PROBEApQosSupport_Type = TruthValue
_H3cDot11PROBEApQosSupport_Object = MibTableColumn
h3cDot11PROBEApQosSupport = _H3cDot11PROBEApQosSupport_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 3, 1, 11),
    _H3cDot11PROBEApQosSupport_Type()
)
h3cDot11PROBEApQosSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBEApQosSupport.setStatus("current")
_H3cDot11PROBEApBeaconIntvl_Type = Integer32
_H3cDot11PROBEApBeaconIntvl_Object = MibTableColumn
h3cDot11PROBEApBeaconIntvl = _H3cDot11PROBEApBeaconIntvl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 3, 1, 12),
    _H3cDot11PROBEApBeaconIntvl_Type()
)
h3cDot11PROBEApBeaconIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBEApBeaconIntvl.setStatus("current")
_H3cDot11PROBEApUpDuration_Type = TimeTicks
_H3cDot11PROBEApUpDuration_Object = MibTableColumn
h3cDot11PROBEApUpDuration = _H3cDot11PROBEApUpDuration_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 3, 1, 13),
    _H3cDot11PROBEApUpDuration_Type()
)
h3cDot11PROBEApUpDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBEApUpDuration.setStatus("current")
_H3cDot11PROBEApSCWS_Type = TruthValue
_H3cDot11PROBEApSCWS_Object = MibTableColumn
h3cDot11PROBEApSCWS = _H3cDot11PROBEApSCWS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 3, 1, 14),
    _H3cDot11PROBEApSCWS_Type()
)
h3cDot11PROBEApSCWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBEApSCWS.setStatus("current")
_H3cDot11PROBEApRptSensorNum_Type = Integer32
_H3cDot11PROBEApRptSensorNum_Object = MibTableColumn
h3cDot11PROBEApRptSensorNum = _H3cDot11PROBEApRptSensorNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 3, 1, 15),
    _H3cDot11PROBEApRptSensorNum_Type()
)
h3cDot11PROBEApRptSensorNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBEApRptSensorNum.setStatus("current")
_H3cDot11PROBEApChannel_Type = H3cDot11PROBEChannel
_H3cDot11PROBEApChannel_Object = MibTableColumn
h3cDot11PROBEApChannel = _H3cDot11PROBEApChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 3, 1, 16),
    _H3cDot11PROBEApChannel_Type()
)
h3cDot11PROBEApChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBEApChannel.setStatus("current")
_H3cDot11PROBEApRSSIMax_Type = Integer32
_H3cDot11PROBEApRSSIMax_Object = MibTableColumn
h3cDot11PROBEApRSSIMax = _H3cDot11PROBEApRSSIMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 3, 1, 17),
    _H3cDot11PROBEApRSSIMax_Type()
)
h3cDot11PROBEApRSSIMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBEApRSSIMax.setStatus("current")
_H3cDot11PROBEApRSSIMin_Type = Integer32
_H3cDot11PROBEApRSSIMin_Object = MibTableColumn
h3cDot11PROBEApRSSIMin = _H3cDot11PROBEApRSSIMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 3, 1, 18),
    _H3cDot11PROBEApRSSIMin_Type()
)
h3cDot11PROBEApRSSIMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBEApRSSIMin.setStatus("current")
_H3cDot11PROBEApRSSI_Type = Integer32
_H3cDot11PROBEApRSSI_Object = MibTableColumn
h3cDot11PROBEApRSSI = _H3cDot11PROBEApRSSI_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 3, 1, 19),
    _H3cDot11PROBEApRSSI_Type()
)
h3cDot11PROBEApRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBEApRSSI.setStatus("current")


class _H3cDot11PROBEApFirstRptTime_Type(OctetString):
    """Custom type h3cDot11PROBEApFirstRptTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_H3cDot11PROBEApFirstRptTime_Type.__name__ = "OctetString"
_H3cDot11PROBEApFirstRptTime_Object = MibTableColumn
h3cDot11PROBEApFirstRptTime = _H3cDot11PROBEApFirstRptTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 3, 1, 20),
    _H3cDot11PROBEApFirstRptTime_Type()
)
h3cDot11PROBEApFirstRptTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBEApFirstRptTime.setStatus("current")


class _H3cDot11PROBEApLastRptTime_Type(OctetString):
    """Custom type h3cDot11PROBEApLastRptTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_H3cDot11PROBEApLastRptTime_Type.__name__ = "OctetString"
_H3cDot11PROBEApLastRptTime_Object = MibTableColumn
h3cDot11PROBEApLastRptTime = _H3cDot11PROBEApLastRptTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 3, 1, 21),
    _H3cDot11PROBEApLastRptTime_Type()
)
h3cDot11PROBEApLastRptTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBEApLastRptTime.setStatus("current")
_H3cDot11PROBEApAssoCltTable_Object = MibTable
h3cDot11PROBEApAssoCltTable = _H3cDot11PROBEApAssoCltTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 4)
)
if mibBuilder.loadTexts:
    h3cDot11PROBEApAssoCltTable.setStatus("current")
_H3cDot11PROBEApAssoCltEntry_Object = MibTableRow
h3cDot11PROBEApAssoCltEntry = _H3cDot11PROBEApAssoCltEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 4, 1)
)
h3cDot11PROBEApAssoCltEntry.setIndexNames(
    (0, "H3C-DOT11-PROBE-MIB", "h3cDot11PROBEApAssoCltApMac"),
    (0, "H3C-DOT11-PROBE-MIB", "h3cDot11PROBEApAssoCltCltMac"),
)
if mibBuilder.loadTexts:
    h3cDot11PROBEApAssoCltEntry.setStatus("current")
_H3cDot11PROBEApAssoCltApMac_Type = MacAddress
_H3cDot11PROBEApAssoCltApMac_Object = MibTableColumn
h3cDot11PROBEApAssoCltApMac = _H3cDot11PROBEApAssoCltApMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 4, 1, 1),
    _H3cDot11PROBEApAssoCltApMac_Type()
)
h3cDot11PROBEApAssoCltApMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11PROBEApAssoCltApMac.setStatus("current")
_H3cDot11PROBEApAssoCltCltMac_Type = MacAddress
_H3cDot11PROBEApAssoCltCltMac_Object = MibTableColumn
h3cDot11PROBEApAssoCltCltMac = _H3cDot11PROBEApAssoCltCltMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 4, 1, 2),
    _H3cDot11PROBEApAssoCltCltMac_Type()
)
h3cDot11PROBEApAssoCltCltMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11PROBEApAssoCltCltMac.setStatus("current")
_H3cDot11PROBEApAssoCltIsAsso_Type = TruthValue
_H3cDot11PROBEApAssoCltIsAsso_Object = MibTableColumn
h3cDot11PROBEApAssoCltIsAsso = _H3cDot11PROBEApAssoCltIsAsso_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 4, 1, 3),
    _H3cDot11PROBEApAssoCltIsAsso_Type()
)
h3cDot11PROBEApAssoCltIsAsso.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBEApAssoCltIsAsso.setStatus("current")
_H3cDot11PROBEApRepSenTable_Object = MibTable
h3cDot11PROBEApRepSenTable = _H3cDot11PROBEApRepSenTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 5)
)
if mibBuilder.loadTexts:
    h3cDot11PROBEApRepSenTable.setStatus("current")
_H3cDot11PROBEApRepSenEntry_Object = MibTableRow
h3cDot11PROBEApRepSenEntry = _H3cDot11PROBEApRepSenEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 5, 1)
)
h3cDot11PROBEApRepSenEntry.setIndexNames(
    (0, "H3C-DOT11-PROBE-MIB", "h3cDot11PROBEApRepSenApMac"),
    (0, "H3C-DOT11-PROBE-MIB", "h3cDot11PROBEApRepSenSenName"),
)
if mibBuilder.loadTexts:
    h3cDot11PROBEApRepSenEntry.setStatus("current")
_H3cDot11PROBEApRepSenApMac_Type = MacAddress
_H3cDot11PROBEApRepSenApMac_Object = MibTableColumn
h3cDot11PROBEApRepSenApMac = _H3cDot11PROBEApRepSenApMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 5, 1, 1),
    _H3cDot11PROBEApRepSenApMac_Type()
)
h3cDot11PROBEApRepSenApMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11PROBEApRepSenApMac.setStatus("current")


class _H3cDot11PROBEApRepSenSenName_Type(OctetString):
    """Custom type h3cDot11PROBEApRepSenSenName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_H3cDot11PROBEApRepSenSenName_Type.__name__ = "OctetString"
_H3cDot11PROBEApRepSenSenName_Object = MibTableColumn
h3cDot11PROBEApRepSenSenName = _H3cDot11PROBEApRepSenSenName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 5, 1, 2),
    _H3cDot11PROBEApRepSenSenName_Type()
)
h3cDot11PROBEApRepSenSenName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11PROBEApRepSenSenName.setStatus("current")


class _H3cDot11PROBEApRepSenRadioId_Type(Integer32):
    """Custom type h3cDot11PROBEApRepSenRadioId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_H3cDot11PROBEApRepSenRadioId_Type.__name__ = "Integer32"
_H3cDot11PROBEApRepSenRadioId_Object = MibTableColumn
h3cDot11PROBEApRepSenRadioId = _H3cDot11PROBEApRepSenRadioId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 5, 1, 3),
    _H3cDot11PROBEApRepSenRadioId_Type()
)
h3cDot11PROBEApRepSenRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBEApRepSenRadioId.setStatus("current")
_H3cDot11PROBEApRepSenRssi_Type = Integer32
_H3cDot11PROBEApRepSenRssi_Object = MibTableColumn
h3cDot11PROBEApRepSenRssi = _H3cDot11PROBEApRepSenRssi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 5, 1, 4),
    _H3cDot11PROBEApRepSenRssi_Type()
)
h3cDot11PROBEApRepSenRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBEApRepSenRssi.setStatus("current")
_H3cDot11PROBEApRepSenChannel_Type = H3cDot11PROBEChannel
_H3cDot11PROBEApRepSenChannel_Object = MibTableColumn
h3cDot11PROBEApRepSenChannel = _H3cDot11PROBEApRepSenChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 5, 1, 5),
    _H3cDot11PROBEApRepSenChannel_Type()
)
h3cDot11PROBEApRepSenChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBEApRepSenChannel.setStatus("current")


class _H3cDot11PROBEApRepSenFirRepTim_Type(OctetString):
    """Custom type h3cDot11PROBEApRepSenFirRepTim based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_H3cDot11PROBEApRepSenFirRepTim_Type.__name__ = "OctetString"
_H3cDot11PROBEApRepSenFirRepTim_Object = MibTableColumn
h3cDot11PROBEApRepSenFirRepTim = _H3cDot11PROBEApRepSenFirRepTim_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 5, 1, 6),
    _H3cDot11PROBEApRepSenFirRepTim_Type()
)
h3cDot11PROBEApRepSenFirRepTim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBEApRepSenFirRepTim.setStatus("current")


class _H3cDot11PROBEApRepSenLasRepTim_Type(OctetString):
    """Custom type h3cDot11PROBEApRepSenLasRepTim based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_H3cDot11PROBEApRepSenLasRepTim_Type.__name__ = "OctetString"
_H3cDot11PROBEApRepSenLasRepTim_Object = MibTableColumn
h3cDot11PROBEApRepSenLasRepTim = _H3cDot11PROBEApRepSenLasRepTim_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 5, 1, 7),
    _H3cDot11PROBEApRepSenLasRepTim_Type()
)
h3cDot11PROBEApRepSenLasRepTim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBEApRepSenLasRepTim.setStatus("current")
_H3cDot11PROBECliRepSenTable_Object = MibTable
h3cDot11PROBECliRepSenTable = _H3cDot11PROBECliRepSenTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 6)
)
if mibBuilder.loadTexts:
    h3cDot11PROBECliRepSenTable.setStatus("current")
_H3cDot11PROBECliRepSenEntry_Object = MibTableRow
h3cDot11PROBECliRepSenEntry = _H3cDot11PROBECliRepSenEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 6, 1)
)
h3cDot11PROBECliRepSenEntry.setIndexNames(
    (0, "H3C-DOT11-PROBE-MIB", "h3cDot11PROBECliRepSenCliMac"),
    (0, "H3C-DOT11-PROBE-MIB", "h3cDot11PROBECliRepSenSenName"),
)
if mibBuilder.loadTexts:
    h3cDot11PROBECliRepSenEntry.setStatus("current")
_H3cDot11PROBECliRepSenCliMac_Type = MacAddress
_H3cDot11PROBECliRepSenCliMac_Object = MibTableColumn
h3cDot11PROBECliRepSenCliMac = _H3cDot11PROBECliRepSenCliMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 6, 1, 1),
    _H3cDot11PROBECliRepSenCliMac_Type()
)
h3cDot11PROBECliRepSenCliMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11PROBECliRepSenCliMac.setStatus("current")


class _H3cDot11PROBECliRepSenSenName_Type(OctetString):
    """Custom type h3cDot11PROBECliRepSenSenName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_H3cDot11PROBECliRepSenSenName_Type.__name__ = "OctetString"
_H3cDot11PROBECliRepSenSenName_Object = MibTableColumn
h3cDot11PROBECliRepSenSenName = _H3cDot11PROBECliRepSenSenName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 6, 1, 2),
    _H3cDot11PROBECliRepSenSenName_Type()
)
h3cDot11PROBECliRepSenSenName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11PROBECliRepSenSenName.setStatus("current")


class _H3cDot11PROBECliRepSenRadioId_Type(Integer32):
    """Custom type h3cDot11PROBECliRepSenRadioId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_H3cDot11PROBECliRepSenRadioId_Type.__name__ = "Integer32"
_H3cDot11PROBECliRepSenRadioId_Object = MibTableColumn
h3cDot11PROBECliRepSenRadioId = _H3cDot11PROBECliRepSenRadioId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 6, 1, 3),
    _H3cDot11PROBECliRepSenRadioId_Type()
)
h3cDot11PROBECliRepSenRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBECliRepSenRadioId.setStatus("current")
_H3cDot11PROBECliRepSenRssi_Type = Integer32
_H3cDot11PROBECliRepSenRssi_Object = MibTableColumn
h3cDot11PROBECliRepSenRssi = _H3cDot11PROBECliRepSenRssi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 6, 1, 4),
    _H3cDot11PROBECliRepSenRssi_Type()
)
h3cDot11PROBECliRepSenRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBECliRepSenRssi.setStatus("current")
_H3cDot11PROBECliRepSenChannel_Type = H3cDot11PROBEChannel
_H3cDot11PROBECliRepSenChannel_Object = MibTableColumn
h3cDot11PROBECliRepSenChannel = _H3cDot11PROBECliRepSenChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 6, 1, 5),
    _H3cDot11PROBECliRepSenChannel_Type()
)
h3cDot11PROBECliRepSenChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBECliRepSenChannel.setStatus("current")


class _H3cDot11PROBECliRepSenFRepTime_Type(OctetString):
    """Custom type h3cDot11PROBECliRepSenFRepTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_H3cDot11PROBECliRepSenFRepTime_Type.__name__ = "OctetString"
_H3cDot11PROBECliRepSenFRepTime_Object = MibTableColumn
h3cDot11PROBECliRepSenFRepTime = _H3cDot11PROBECliRepSenFRepTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 6, 1, 6),
    _H3cDot11PROBECliRepSenFRepTime_Type()
)
h3cDot11PROBECliRepSenFRepTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBECliRepSenFRepTime.setStatus("current")


class _H3cDot11PROBECliRepSenLRepTime_Type(OctetString):
    """Custom type h3cDot11PROBECliRepSenLRepTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_H3cDot11PROBECliRepSenLRepTime_Type.__name__ = "OctetString"
_H3cDot11PROBECliRepSenLRepTime_Object = MibTableColumn
h3cDot11PROBECliRepSenLRepTime = _H3cDot11PROBECliRepSenLRepTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 6, 1, 7),
    _H3cDot11PROBECliRepSenLRepTime_Type()
)
h3cDot11PROBECliRepSenLRepTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBECliRepSenLRepTime.setStatus("current")
_H3cDot11PROBECliRepSenAssAPMac_Type = MacAddress
_H3cDot11PROBECliRepSenAssAPMac_Object = MibTableColumn
h3cDot11PROBECliRepSenAssAPMac = _H3cDot11PROBECliRepSenAssAPMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 17, 2, 6, 1, 8),
    _H3cDot11PROBECliRepSenAssAPMac_Type()
)
h3cDot11PROBECliRepSenAssAPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PROBECliRepSenAssAPMac.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-DOT11-PROBE-MIB",
    **{"H3cDot11PROBEEnabledStatus": H3cDot11PROBEEnabledStatus,
       "H3cDot11PROBERadioType": H3cDot11PROBERadioType,
       "H3cDot11PROBEDevStatus": H3cDot11PROBEDevStatus,
       "H3cDot11PROBEChannel": H3cDot11PROBEChannel,
       "H3cDot11PROBEEncryptMethod": H3cDot11PROBEEncryptMethod,
       "H3cDot11PROBEAuthMethod": H3cDot11PROBEAuthMethod,
       "H3cDot11PROBESecurityType": H3cDot11PROBESecurityType,
       "h3cDot11PROBE": h3cDot11PROBE,
       "h3cDot11PROBEConfigGroup": h3cDot11PROBEConfigGroup,
       "h3cDot11PROBERadioCfgTable": h3cDot11PROBERadioCfgTable,
       "h3cDot11PROBERadioCfgEntry": h3cDot11PROBERadioCfgEntry,
       "h3cDot11PROBERadioCfgApName": h3cDot11PROBERadioCfgApName,
       "h3cDot11PROBERadioCfgRadioId": h3cDot11PROBERadioCfgRadioId,
       "h3cDot11PROBERadioCfgStatus": h3cDot11PROBERadioCfgStatus,
       "h3cDot11PROBEDataGroup": h3cDot11PROBEDataGroup,
       "h3cDot11PROBEClientTable": h3cDot11PROBEClientTable,
       "h3cDot11PROBEClientEntry": h3cDot11PROBEClientEntry,
       "h3cDot11PROBEClientMac": h3cDot11PROBEClientMac,
       "h3cDot11PROBEClientBSSID": h3cDot11PROBEClientBSSID,
       "h3cDot11PROBEClientSSID": h3cDot11PROBEClientSSID,
       "h3cDot11PROBEClientIsDiss": h3cDot11PROBEClientIsDiss,
       "h3cDot11PROBEClientStatus": h3cDot11PROBEClientStatus,
       "h3cDot11PROBEClientDuratTime": h3cDot11PROBEClientDuratTime,
       "h3cDot11PROBEClientVendor": h3cDot11PROBEClientVendor,
       "h3cDot11PROBEClientRptApNum": h3cDot11PROBEClientRptApNum,
       "h3cDot11PROBEClientWorkChannel": h3cDot11PROBEClientWorkChannel,
       "h3cDot11PROBEClientRSSIMax": h3cDot11PROBEClientRSSIMax,
       "h3cDot11PROBEClientRSSIMin": h3cDot11PROBEClientRSSIMin,
       "h3cDot11PROBEClientRSSI": h3cDot11PROBEClientRSSI,
       "h3cDot11PROBEClientFirstTime": h3cDot11PROBEClientFirstTime,
       "h3cDot11PROBEClientLastTime": h3cDot11PROBEClientLastTime,
       "h3cDot11PROBEStatTable": h3cDot11PROBEStatTable,
       "h3cDot11PROBEStatEntry": h3cDot11PROBEStatEntry,
       "h3cDot11PROBEStatTime": h3cDot11PROBEStatTime,
       "h3cDot11PROBEStatRssiMaxNum": h3cDot11PROBEStatRssiMaxNum,
       "h3cDot11PROBEStatRssiMiddleNum": h3cDot11PROBEStatRssiMiddleNum,
       "h3cDot11PROBEStatRssiMinNum": h3cDot11PROBEStatRssiMinNum,
       "h3cDot11PROBEStatTotalNum": h3cDot11PROBEStatTotalNum,
       "h3cDot11PROBEStatAssocNum": h3cDot11PROBEStatAssocNum,
       "h3cDot11PROBEStatDissocNum": h3cDot11PROBEStatDissocNum,
       "h3cDot11PROBEApTable": h3cDot11PROBEApTable,
       "h3cDot11PROBEApEntry": h3cDot11PROBEApEntry,
       "h3cDot11PROBEApMacAddress": h3cDot11PROBEApMacAddress,
       "h3cDot11PROBEApSsid": h3cDot11PROBEApSsid,
       "h3cDot11PROBEApStatus": h3cDot11PROBEApStatus,
       "h3cDot11PROBEApStatusDuTime": h3cDot11PROBEApStatusDuTime,
       "h3cDot11PROBEApVendor": h3cDot11PROBEApVendor,
       "h3cDot11PROBEApRadioType": h3cDot11PROBEApRadioType,
       "h3cDot11PROBEApSecurityType": h3cDot11PROBEApSecurityType,
       "h3cDot11PROBEApEncryMethod": h3cDot11PROBEApEncryMethod,
       "h3cDot11PROBEApAuthMethod": h3cDot11PROBEApAuthMethod,
       "h3cDot11PROBEApIsBroadSSID": h3cDot11PROBEApIsBroadSSID,
       "h3cDot11PROBEApQosSupport": h3cDot11PROBEApQosSupport,
       "h3cDot11PROBEApBeaconIntvl": h3cDot11PROBEApBeaconIntvl,
       "h3cDot11PROBEApUpDuration": h3cDot11PROBEApUpDuration,
       "h3cDot11PROBEApSCWS": h3cDot11PROBEApSCWS,
       "h3cDot11PROBEApRptSensorNum": h3cDot11PROBEApRptSensorNum,
       "h3cDot11PROBEApChannel": h3cDot11PROBEApChannel,
       "h3cDot11PROBEApRSSIMax": h3cDot11PROBEApRSSIMax,
       "h3cDot11PROBEApRSSIMin": h3cDot11PROBEApRSSIMin,
       "h3cDot11PROBEApRSSI": h3cDot11PROBEApRSSI,
       "h3cDot11PROBEApFirstRptTime": h3cDot11PROBEApFirstRptTime,
       "h3cDot11PROBEApLastRptTime": h3cDot11PROBEApLastRptTime,
       "h3cDot11PROBEApAssoCltTable": h3cDot11PROBEApAssoCltTable,
       "h3cDot11PROBEApAssoCltEntry": h3cDot11PROBEApAssoCltEntry,
       "h3cDot11PROBEApAssoCltApMac": h3cDot11PROBEApAssoCltApMac,
       "h3cDot11PROBEApAssoCltCltMac": h3cDot11PROBEApAssoCltCltMac,
       "h3cDot11PROBEApAssoCltIsAsso": h3cDot11PROBEApAssoCltIsAsso,
       "h3cDot11PROBEApRepSenTable": h3cDot11PROBEApRepSenTable,
       "h3cDot11PROBEApRepSenEntry": h3cDot11PROBEApRepSenEntry,
       "h3cDot11PROBEApRepSenApMac": h3cDot11PROBEApRepSenApMac,
       "h3cDot11PROBEApRepSenSenName": h3cDot11PROBEApRepSenSenName,
       "h3cDot11PROBEApRepSenRadioId": h3cDot11PROBEApRepSenRadioId,
       "h3cDot11PROBEApRepSenRssi": h3cDot11PROBEApRepSenRssi,
       "h3cDot11PROBEApRepSenChannel": h3cDot11PROBEApRepSenChannel,
       "h3cDot11PROBEApRepSenFirRepTim": h3cDot11PROBEApRepSenFirRepTim,
       "h3cDot11PROBEApRepSenLasRepTim": h3cDot11PROBEApRepSenLasRepTim,
       "h3cDot11PROBECliRepSenTable": h3cDot11PROBECliRepSenTable,
       "h3cDot11PROBECliRepSenEntry": h3cDot11PROBECliRepSenEntry,
       "h3cDot11PROBECliRepSenCliMac": h3cDot11PROBECliRepSenCliMac,
       "h3cDot11PROBECliRepSenSenName": h3cDot11PROBECliRepSenSenName,
       "h3cDot11PROBECliRepSenRadioId": h3cDot11PROBECliRepSenRadioId,
       "h3cDot11PROBECliRepSenRssi": h3cDot11PROBECliRepSenRssi,
       "h3cDot11PROBECliRepSenChannel": h3cDot11PROBECliRepSenChannel,
       "h3cDot11PROBECliRepSenFRepTime": h3cDot11PROBECliRepSenFRepTime,
       "h3cDot11PROBECliRepSenLRepTime": h3cDot11PROBECliRepSenLRepTime,
       "h3cDot11PROBECliRepSenAssAPMac": h3cDot11PROBECliRepSenAssAPMac}
)
