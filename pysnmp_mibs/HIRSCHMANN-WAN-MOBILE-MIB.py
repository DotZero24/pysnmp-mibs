# SNMP MIB module (HIRSCHMANN-WAN-MOBILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hirschmann/HIRSCHMANN-WAN-MOBILE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:53:04 2025
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

(hmWanMgmt,) = mibBuilder.importSymbols(
    "HIRSCHMANN-WAN-MIB",
    "hmWanMgmt")

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

hmWanMobileMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 4)
)
if mibBuilder.loadTexts:
    hmWanMobileMib.setRevisions(
        ("2016-08-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _HmWanMobileTechnology_Type(Integer32):
    """Custom type hmWanMobileTechnology based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4,
              6,
              8,
              10,
              12,
              14,
              16,
              18,
              20,
              22,
              24)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("gprs", 2),
          ("edge", 4),
          ("umts", 6),
          ("hsdpa", 8),
          ("hsupa", 10),
          ("hspa", 12),
          ("lte", 14),
          ("cdma", 16),
          ("evdo", 18),
          ("evdo0", 20),
          ("evdoA", 22),
          ("evdoB", 24))
    )


_HmWanMobileTechnology_Type.__name__ = "Integer32"
_HmWanMobileTechnology_Object = MibScalar
hmWanMobileTechnology = _HmWanMobileTechnology_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 4, 1),
    _HmWanMobileTechnology_Type()
)
hmWanMobileTechnology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanMobileTechnology.setStatus("current")
_HmWanMobilePLMN_Type = OctetString
_HmWanMobilePLMN_Object = MibScalar
hmWanMobilePLMN = _HmWanMobilePLMN_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 4, 2),
    _HmWanMobilePLMN_Type()
)
hmWanMobilePLMN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanMobilePLMN.setStatus("current")
_HmWanMobileCell_Type = OctetString
_HmWanMobileCell_Object = MibScalar
hmWanMobileCell = _HmWanMobileCell_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 4, 3),
    _HmWanMobileCell_Type()
)
hmWanMobileCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanMobileCell.setStatus("current")
_HmWanMobileChannel_Type = OctetString
_HmWanMobileChannel_Object = MibScalar
hmWanMobileChannel = _HmWanMobileChannel_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 4, 4),
    _HmWanMobileChannel_Type()
)
hmWanMobileChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanMobileChannel.setStatus("current")
_HmWanMobileSignalStrength_Type = Integer32
_HmWanMobileSignalStrength_Object = MibScalar
hmWanMobileSignalStrength = _HmWanMobileSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 4, 5),
    _HmWanMobileSignalStrength_Type()
)
hmWanMobileSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanMobileSignalStrength.setStatus("current")
_HmWanMobileChannelN1_Type = OctetString
_HmWanMobileChannelN1_Object = MibScalar
hmWanMobileChannelN1 = _HmWanMobileChannelN1_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 4, 6),
    _HmWanMobileChannelN1_Type()
)
hmWanMobileChannelN1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanMobileChannelN1.setStatus("current")
_HmWanMobileSignalStrengthN1_Type = Integer32
_HmWanMobileSignalStrengthN1_Object = MibScalar
hmWanMobileSignalStrengthN1 = _HmWanMobileSignalStrengthN1_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 4, 7),
    _HmWanMobileSignalStrengthN1_Type()
)
hmWanMobileSignalStrengthN1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanMobileSignalStrengthN1.setStatus("current")
_HmWanMobileChannelN2_Type = OctetString
_HmWanMobileChannelN2_Object = MibScalar
hmWanMobileChannelN2 = _HmWanMobileChannelN2_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 4, 8),
    _HmWanMobileChannelN2_Type()
)
hmWanMobileChannelN2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanMobileChannelN2.setStatus("current")
_HmWanMobileSignalStrengthN2_Type = Integer32
_HmWanMobileSignalStrengthN2_Object = MibScalar
hmWanMobileSignalStrengthN2 = _HmWanMobileSignalStrengthN2_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 4, 9),
    _HmWanMobileSignalStrengthN2_Type()
)
hmWanMobileSignalStrengthN2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanMobileSignalStrengthN2.setStatus("current")
_HmWanMobileChannelN3_Type = OctetString
_HmWanMobileChannelN3_Object = MibScalar
hmWanMobileChannelN3 = _HmWanMobileChannelN3_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 4, 10),
    _HmWanMobileChannelN3_Type()
)
hmWanMobileChannelN3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanMobileChannelN3.setStatus("current")
_HmWanMobileSignalStrengthN3_Type = Integer32
_HmWanMobileSignalStrengthN3_Object = MibScalar
hmWanMobileSignalStrengthN3 = _HmWanMobileSignalStrengthN3_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 4, 11),
    _HmWanMobileSignalStrengthN3_Type()
)
hmWanMobileSignalStrengthN3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanMobileSignalStrengthN3.setStatus("current")
_HmWanMobileChannelN4_Type = OctetString
_HmWanMobileChannelN4_Object = MibScalar
hmWanMobileChannelN4 = _HmWanMobileChannelN4_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 4, 12),
    _HmWanMobileChannelN4_Type()
)
hmWanMobileChannelN4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanMobileChannelN4.setStatus("current")
_HmWanMobileSignalStrengthN4_Type = Integer32
_HmWanMobileSignalStrengthN4_Object = MibScalar
hmWanMobileSignalStrengthN4 = _HmWanMobileSignalStrengthN4_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 4, 13),
    _HmWanMobileSignalStrengthN4_Type()
)
hmWanMobileSignalStrengthN4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanMobileSignalStrengthN4.setStatus("current")
_HmWanMobileChannelN5_Type = OctetString
_HmWanMobileChannelN5_Object = MibScalar
hmWanMobileChannelN5 = _HmWanMobileChannelN5_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 4, 14),
    _HmWanMobileChannelN5_Type()
)
hmWanMobileChannelN5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanMobileChannelN5.setStatus("current")
_HmWanMobileSignalStrengthN5_Type = Integer32
_HmWanMobileSignalStrengthN5_Object = MibScalar
hmWanMobileSignalStrengthN5 = _HmWanMobileSignalStrengthN5_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 4, 15),
    _HmWanMobileSignalStrengthN5_Type()
)
hmWanMobileSignalStrengthN5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanMobileSignalStrengthN5.setStatus("current")
_HmWanMobileUpTime_Type = TimeTicks
_HmWanMobileUpTime_Object = MibScalar
hmWanMobileUpTime = _HmWanMobileUpTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 4, 16),
    _HmWanMobileUpTime_Type()
)
hmWanMobileUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanMobileUpTime.setStatus("current")
_HmWanMobileConnect_Type = Counter32
_HmWanMobileConnect_Object = MibScalar
hmWanMobileConnect = _HmWanMobileConnect_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 4, 17),
    _HmWanMobileConnect_Type()
)
hmWanMobileConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanMobileConnect.setStatus("current")
_HmWanMobileDisconnect_Type = Counter32
_HmWanMobileDisconnect_Object = MibScalar
hmWanMobileDisconnect = _HmWanMobileDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 4, 18),
    _HmWanMobileDisconnect_Type()
)
hmWanMobileDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanMobileDisconnect.setStatus("current")


class _HmWanMobileCard_Type(Integer32):
    """Custom type hmWanMobileCard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 0),
          ("secondary", 1),
          ("tertiary", 2))
    )


_HmWanMobileCard_Type.__name__ = "Integer32"
_HmWanMobileCard_Object = MibScalar
hmWanMobileCard = _HmWanMobileCard_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 4, 19),
    _HmWanMobileCard_Type()
)
hmWanMobileCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanMobileCard.setStatus("current")
_HmWanMobileIPAddress_Type = IpAddress
_HmWanMobileIPAddress_Object = MibScalar
hmWanMobileIPAddress = _HmWanMobileIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 4, 20),
    _HmWanMobileIPAddress_Type()
)
hmWanMobileIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanMobileIPAddress.setStatus("current")
_HmWanMobileLatency_Type = Integer32
_HmWanMobileLatency_Object = MibScalar
hmWanMobileLatency = _HmWanMobileLatency_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 4, 21),
    _HmWanMobileLatency_Type()
)
hmWanMobileLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanMobileLatency.setStatus("current")
_HmWanMobileReportPeriod_Type = Integer32
_HmWanMobileReportPeriod_Object = MibScalar
hmWanMobileReportPeriod = _HmWanMobileReportPeriod_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 4, 22),
    _HmWanMobileReportPeriod_Type()
)
hmWanMobileReportPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanMobileReportPeriod.setStatus("current")


class _HmWanMobileRegistration_Type(Integer32):
    """Custom type hmWanMobileRegistration based on Integer32"""
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
        *(("unknown", 0),
          ("idle", 1),
          ("search", 2),
          ("denied", 3),
          ("home", 4),
          ("foregien", 5))
    )


_HmWanMobileRegistration_Type.__name__ = "Integer32"
_HmWanMobileRegistration_Object = MibScalar
hmWanMobileRegistration = _HmWanMobileRegistration_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 4, 23),
    _HmWanMobileRegistration_Type()
)
hmWanMobileRegistration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanMobileRegistration.setStatus("current")
_HmWanMobileOperator_Type = OctetString
_HmWanMobileOperator_Object = MibScalar
hmWanMobileOperator = _HmWanMobileOperator_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 4, 24),
    _HmWanMobileOperator_Type()
)
hmWanMobileOperator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanMobileOperator.setStatus("current")
_HmWanMobileLAC_Type = OctetString
_HmWanMobileLAC_Object = MibScalar
hmWanMobileLAC = _HmWanMobileLAC_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 4, 25),
    _HmWanMobileLAC_Type()
)
hmWanMobileLAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanMobileLAC.setStatus("current")
_HmWanMobileSignalQuality_Type = Integer32
_HmWanMobileSignalQuality_Object = MibScalar
hmWanMobileSignalQuality = _HmWanMobileSignalQuality_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 4, 26),
    _HmWanMobileSignalQuality_Type()
)
hmWanMobileSignalQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanMobileSignalQuality.setStatus("current")
_HmWanMobileCSQ_Type = Integer32
_HmWanMobileCSQ_Object = MibScalar
hmWanMobileCSQ = _HmWanMobileCSQ_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 4, 27),
    _HmWanMobileCSQ_Type()
)
hmWanMobileCSQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanMobileCSQ.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HIRSCHMANN-WAN-MOBILE-MIB",
    **{"hmWanMobileMib": hmWanMobileMib,
       "hmWanMobileTechnology": hmWanMobileTechnology,
       "hmWanMobilePLMN": hmWanMobilePLMN,
       "hmWanMobileCell": hmWanMobileCell,
       "hmWanMobileChannel": hmWanMobileChannel,
       "hmWanMobileSignalStrength": hmWanMobileSignalStrength,
       "hmWanMobileChannelN1": hmWanMobileChannelN1,
       "hmWanMobileSignalStrengthN1": hmWanMobileSignalStrengthN1,
       "hmWanMobileChannelN2": hmWanMobileChannelN2,
       "hmWanMobileSignalStrengthN2": hmWanMobileSignalStrengthN2,
       "hmWanMobileChannelN3": hmWanMobileChannelN3,
       "hmWanMobileSignalStrengthN3": hmWanMobileSignalStrengthN3,
       "hmWanMobileChannelN4": hmWanMobileChannelN4,
       "hmWanMobileSignalStrengthN4": hmWanMobileSignalStrengthN4,
       "hmWanMobileChannelN5": hmWanMobileChannelN5,
       "hmWanMobileSignalStrengthN5": hmWanMobileSignalStrengthN5,
       "hmWanMobileUpTime": hmWanMobileUpTime,
       "hmWanMobileConnect": hmWanMobileConnect,
       "hmWanMobileDisconnect": hmWanMobileDisconnect,
       "hmWanMobileCard": hmWanMobileCard,
       "hmWanMobileIPAddress": hmWanMobileIPAddress,
       "hmWanMobileLatency": hmWanMobileLatency,
       "hmWanMobileReportPeriod": hmWanMobileReportPeriod,
       "hmWanMobileRegistration": hmWanMobileRegistration,
       "hmWanMobileOperator": hmWanMobileOperator,
       "hmWanMobileLAC": hmWanMobileLAC,
       "hmWanMobileSignalQuality": hmWanMobileSignalQuality,
       "hmWanMobileCSQ": hmWanMobileCSQ}
)
