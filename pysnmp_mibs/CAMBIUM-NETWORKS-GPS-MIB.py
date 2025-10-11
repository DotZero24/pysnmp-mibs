# SNMP MIB module (CAMBIUM-NETWORKS-GPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/cambium/CAMBIUM-NETWORKS-GPS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:07:47 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cnGpsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 24, 5)
)
if mibBuilder.loadTexts:
    cnGpsMib.setRevisions(
        ("2020-06-29 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CnGpsObjects_ObjectIdentity = ObjectIdentity
cnGpsObjects = _CnGpsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 24, 5, 0)
)


class _CnGpsInternalSourceAdminStatus_Type(Integer32):
    """Custom type cnGpsInternalSourceAdminStatus based on Integer32"""
    defaultValue = 1

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


_CnGpsInternalSourceAdminStatus_Type.__name__ = "Integer32"
_CnGpsInternalSourceAdminStatus_Object = MibScalar
cnGpsInternalSourceAdminStatus = _CnGpsInternalSourceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 5, 0, 1),
    _CnGpsInternalSourceAdminStatus_Type()
)
cnGpsInternalSourceAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnGpsInternalSourceAdminStatus.setStatus("current")


class _CnGpsExternalSourceAdminStatus_Type(Integer32):
    """Custom type cnGpsExternalSourceAdminStatus based on Integer32"""
    defaultValue = 1

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


_CnGpsExternalSourceAdminStatus_Type.__name__ = "Integer32"
_CnGpsExternalSourceAdminStatus_Object = MibScalar
cnGpsExternalSourceAdminStatus = _CnGpsExternalSourceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 5, 0, 2),
    _CnGpsExternalSourceAdminStatus_Type()
)
cnGpsExternalSourceAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnGpsExternalSourceAdminStatus.setStatus("current")
_CnGpsPortTable_Object = MibTable
cnGpsPortTable = _CnGpsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 5, 0, 3)
)
if mibBuilder.loadTexts:
    cnGpsPortTable.setStatus("current")
_CnGpsPortEntry_Object = MibTableRow
cnGpsPortEntry = _CnGpsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 5, 0, 3, 1)
)
cnGpsPortEntry.setIndexNames(
    (0, "CAMBIUM-NETWORKS-GPS-MIB", "cnGpsPortIndex"),
)
if mibBuilder.loadTexts:
    cnGpsPortEntry.setStatus("current")


class _CnGpsPortIndex_Type(Integer32):
    """Custom type cnGpsPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CnGpsPortIndex_Type.__name__ = "Integer32"
_CnGpsPortIndex_Object = MibTableColumn
cnGpsPortIndex = _CnGpsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 5, 0, 3, 1, 1),
    _CnGpsPortIndex_Type()
)
cnGpsPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnGpsPortIndex.setStatus("current")


class _CnGpsPortOutputAdminStatus_Type(Integer32):
    """Custom type cnGpsPortOutputAdminStatus based on Integer32"""
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


_CnGpsPortOutputAdminStatus_Type.__name__ = "Integer32"
_CnGpsPortOutputAdminStatus_Object = MibTableColumn
cnGpsPortOutputAdminStatus = _CnGpsPortOutputAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 5, 0, 3, 1, 2),
    _CnGpsPortOutputAdminStatus_Type()
)
cnGpsPortOutputAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnGpsPortOutputAdminStatus.setStatus("current")


class _CnGpsSignalStatus_Type(Integer32):
    """Custom type cnGpsSignalStatus based on Integer32"""
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
        *(("not-set", 0),
          ("not-enabled-sources", 1),
          ("not-acquired", 2),
          ("acquired", 3))
    )


_CnGpsSignalStatus_Type.__name__ = "Integer32"
_CnGpsSignalStatus_Object = MibScalar
cnGpsSignalStatus = _CnGpsSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 5, 0, 4),
    _CnGpsSignalStatus_Type()
)
cnGpsSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnGpsSignalStatus.setStatus("current")


class _CnGpsSourcePowerCycle_Type(Integer32):
    """Custom type cnGpsSourcePowerCycle based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-set", 0),
          ("internal", 1),
          ("external", 2))
    )


_CnGpsSourcePowerCycle_Type.__name__ = "Integer32"
_CnGpsSourcePowerCycle_Object = MibScalar
cnGpsSourcePowerCycle = _CnGpsSourcePowerCycle_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 5, 0, 6),
    _CnGpsSourcePowerCycle_Type()
)
cnGpsSourcePowerCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnGpsSourcePowerCycle.setStatus("current")


class _CnGpsInternalTime_Type(OctetString):
    """Custom type cnGpsInternalTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CnGpsInternalTime_Type.__name__ = "OctetString"
_CnGpsInternalTime_Object = MibScalar
cnGpsInternalTime = _CnGpsInternalTime_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 5, 0, 7),
    _CnGpsInternalTime_Type()
)
cnGpsInternalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnGpsInternalTime.setStatus("current")


class _CnGpsExternalTime_Type(OctetString):
    """Custom type cnGpsExternalTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CnGpsExternalTime_Type.__name__ = "OctetString"
_CnGpsExternalTime_Object = MibScalar
cnGpsExternalTime = _CnGpsExternalTime_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 5, 0, 8),
    _CnGpsExternalTime_Type()
)
cnGpsExternalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnGpsExternalTime.setStatus("current")


class _CnGpsInternalLatitude_Type(OctetString):
    """Custom type cnGpsInternalLatitude based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CnGpsInternalLatitude_Type.__name__ = "OctetString"
_CnGpsInternalLatitude_Object = MibScalar
cnGpsInternalLatitude = _CnGpsInternalLatitude_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 5, 0, 9),
    _CnGpsInternalLatitude_Type()
)
cnGpsInternalLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnGpsInternalLatitude.setStatus("current")


class _CnGpsExternalLatitude_Type(OctetString):
    """Custom type cnGpsExternalLatitude based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CnGpsExternalLatitude_Type.__name__ = "OctetString"
_CnGpsExternalLatitude_Object = MibScalar
cnGpsExternalLatitude = _CnGpsExternalLatitude_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 5, 0, 10),
    _CnGpsExternalLatitude_Type()
)
cnGpsExternalLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnGpsExternalLatitude.setStatus("current")


class _CnGpsInternalLongitude_Type(OctetString):
    """Custom type cnGpsInternalLongitude based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CnGpsInternalLongitude_Type.__name__ = "OctetString"
_CnGpsInternalLongitude_Object = MibScalar
cnGpsInternalLongitude = _CnGpsInternalLongitude_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 5, 0, 11),
    _CnGpsInternalLongitude_Type()
)
cnGpsInternalLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnGpsInternalLongitude.setStatus("current")


class _CnGpsExternalLongitude_Type(OctetString):
    """Custom type cnGpsExternalLongitude based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CnGpsExternalLongitude_Type.__name__ = "OctetString"
_CnGpsExternalLongitude_Object = MibScalar
cnGpsExternalLongitude = _CnGpsExternalLongitude_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 5, 0, 12),
    _CnGpsExternalLongitude_Type()
)
cnGpsExternalLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnGpsExternalLongitude.setStatus("current")


class _CnGpsInternalSignalQuality_Type(Integer32):
    """Custom type cnGpsInternalSignalQuality based on Integer32"""
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
        *(("fix-not-valid", 1),
          ("gps-fix", 2),
          ("diff-gps-fix", 3),
          ("rtk-fixed", 4),
          ("rtk-float", 5))
    )


_CnGpsInternalSignalQuality_Type.__name__ = "Integer32"
_CnGpsInternalSignalQuality_Object = MibScalar
cnGpsInternalSignalQuality = _CnGpsInternalSignalQuality_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 5, 0, 13),
    _CnGpsInternalSignalQuality_Type()
)
cnGpsInternalSignalQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnGpsInternalSignalQuality.setStatus("current")


class _CnGpsExternalSignalQuality_Type(Integer32):
    """Custom type cnGpsExternalSignalQuality based on Integer32"""
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
        *(("fix-not-valid", 1),
          ("gps-fix", 2),
          ("diff-gps-fix", 3),
          ("rtk-fixed", 4),
          ("rtk-float", 5))
    )


_CnGpsExternalSignalQuality_Type.__name__ = "Integer32"
_CnGpsExternalSignalQuality_Object = MibScalar
cnGpsExternalSignalQuality = _CnGpsExternalSignalQuality_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 5, 0, 14),
    _CnGpsExternalSignalQuality_Type()
)
cnGpsExternalSignalQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnGpsExternalSignalQuality.setStatus("current")


class _CnGpsInternalAntennaAltitude_Type(OctetString):
    """Custom type cnGpsInternalAntennaAltitude based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CnGpsInternalAntennaAltitude_Type.__name__ = "OctetString"
_CnGpsInternalAntennaAltitude_Object = MibScalar
cnGpsInternalAntennaAltitude = _CnGpsInternalAntennaAltitude_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 5, 0, 15),
    _CnGpsInternalAntennaAltitude_Type()
)
cnGpsInternalAntennaAltitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnGpsInternalAntennaAltitude.setStatus("current")


class _CnGpsExternalAntennaAltitude_Type(OctetString):
    """Custom type cnGpsExternalAntennaAltitude based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CnGpsExternalAntennaAltitude_Type.__name__ = "OctetString"
_CnGpsExternalAntennaAltitude_Object = MibScalar
cnGpsExternalAntennaAltitude = _CnGpsExternalAntennaAltitude_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 5, 0, 16),
    _CnGpsExternalAntennaAltitude_Type()
)
cnGpsExternalAntennaAltitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnGpsExternalAntennaAltitude.setStatus("current")


class _CnGpsInternalAntennaBaseAltitude_Type(OctetString):
    """Custom type cnGpsInternalAntennaBaseAltitude based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CnGpsInternalAntennaBaseAltitude_Type.__name__ = "OctetString"
_CnGpsInternalAntennaBaseAltitude_Object = MibScalar
cnGpsInternalAntennaBaseAltitude = _CnGpsInternalAntennaBaseAltitude_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 5, 0, 17),
    _CnGpsInternalAntennaBaseAltitude_Type()
)
cnGpsInternalAntennaBaseAltitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnGpsInternalAntennaBaseAltitude.setStatus("current")


class _CnGpsExternalAntennaBaseAltitude_Type(OctetString):
    """Custom type cnGpsExternalAntennaBaseAltitude based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CnGpsExternalAntennaBaseAltitude_Type.__name__ = "OctetString"
_CnGpsExternalAntennaBaseAltitude_Object = MibScalar
cnGpsExternalAntennaBaseAltitude = _CnGpsExternalAntennaBaseAltitude_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 5, 0, 18),
    _CnGpsExternalAntennaBaseAltitude_Type()
)
cnGpsExternalAntennaBaseAltitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnGpsExternalAntennaBaseAltitude.setStatus("current")


class _CnGpsInternalSelectionMode_Type(Integer32):
    """Custom type cnGpsInternalSelectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_CnGpsInternalSelectionMode_Type.__name__ = "Integer32"
_CnGpsInternalSelectionMode_Object = MibScalar
cnGpsInternalSelectionMode = _CnGpsInternalSelectionMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 5, 0, 19),
    _CnGpsInternalSelectionMode_Type()
)
cnGpsInternalSelectionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnGpsInternalSelectionMode.setStatus("current")


class _CnGpsExternalSelectionMode_Type(Integer32):
    """Custom type cnGpsExternalSelectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_CnGpsExternalSelectionMode_Type.__name__ = "Integer32"
_CnGpsExternalSelectionMode_Object = MibScalar
cnGpsExternalSelectionMode = _CnGpsExternalSelectionMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 5, 0, 20),
    _CnGpsExternalSelectionMode_Type()
)
cnGpsExternalSelectionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnGpsExternalSelectionMode.setStatus("current")


class _CnGpsInternalLocalizationType_Type(Integer32):
    """Custom type cnGpsInternalLocalizationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no-fix", 1),
          ("two-D", 2),
          ("three-D", 3))
    )


_CnGpsInternalLocalizationType_Type.__name__ = "Integer32"
_CnGpsInternalLocalizationType_Object = MibScalar
cnGpsInternalLocalizationType = _CnGpsInternalLocalizationType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 5, 0, 21),
    _CnGpsInternalLocalizationType_Type()
)
cnGpsInternalLocalizationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnGpsInternalLocalizationType.setStatus("current")


class _CnGpsExternalLocalizationType_Type(Integer32):
    """Custom type cnGpsExternalLocalizationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no-fix", 1),
          ("two-D", 2),
          ("three-D", 3))
    )


_CnGpsExternalLocalizationType_Type.__name__ = "Integer32"
_CnGpsExternalLocalizationType_Object = MibScalar
cnGpsExternalLocalizationType = _CnGpsExternalLocalizationType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 5, 0, 22),
    _CnGpsExternalLocalizationType_Type()
)
cnGpsExternalLocalizationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnGpsExternalLocalizationType.setStatus("current")


class _CnGpsInternalPdop_Type(OctetString):
    """Custom type cnGpsInternalPdop based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CnGpsInternalPdop_Type.__name__ = "OctetString"
_CnGpsInternalPdop_Object = MibScalar
cnGpsInternalPdop = _CnGpsInternalPdop_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 5, 0, 23),
    _CnGpsInternalPdop_Type()
)
cnGpsInternalPdop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnGpsInternalPdop.setStatus("current")


class _CnGpsExternalPdop_Type(OctetString):
    """Custom type cnGpsExternalPdop based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CnGpsExternalPdop_Type.__name__ = "OctetString"
_CnGpsExternalPdop_Object = MibScalar
cnGpsExternalPdop = _CnGpsExternalPdop_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 5, 0, 24),
    _CnGpsExternalPdop_Type()
)
cnGpsExternalPdop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnGpsExternalPdop.setStatus("current")


class _CnGpsInternalHdop_Type(OctetString):
    """Custom type cnGpsInternalHdop based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CnGpsInternalHdop_Type.__name__ = "OctetString"
_CnGpsInternalHdop_Object = MibScalar
cnGpsInternalHdop = _CnGpsInternalHdop_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 5, 0, 25),
    _CnGpsInternalHdop_Type()
)
cnGpsInternalHdop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnGpsInternalHdop.setStatus("current")


class _CnGpsExternalHdop_Type(OctetString):
    """Custom type cnGpsExternalHdop based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CnGpsExternalHdop_Type.__name__ = "OctetString"
_CnGpsExternalHdop_Object = MibScalar
cnGpsExternalHdop = _CnGpsExternalHdop_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 5, 0, 26),
    _CnGpsExternalHdop_Type()
)
cnGpsExternalHdop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnGpsExternalHdop.setStatus("current")


class _CnGpsInternalVdop_Type(OctetString):
    """Custom type cnGpsInternalVdop based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CnGpsInternalVdop_Type.__name__ = "OctetString"
_CnGpsInternalVdop_Object = MibScalar
cnGpsInternalVdop = _CnGpsInternalVdop_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 5, 0, 27),
    _CnGpsInternalVdop_Type()
)
cnGpsInternalVdop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnGpsInternalVdop.setStatus("current")


class _CnGpsExternalVdop_Type(OctetString):
    """Custom type cnGpsExternalVdop based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CnGpsExternalVdop_Type.__name__ = "OctetString"
_CnGpsExternalVdop_Object = MibScalar
cnGpsExternalVdop = _CnGpsExternalVdop_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 5, 0, 28),
    _CnGpsExternalVdop_Type()
)
cnGpsExternalVdop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnGpsExternalVdop.setStatus("current")


class _CnGpsInternalSv_Type(Integer32):
    """Custom type cnGpsInternalSv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_CnGpsInternalSv_Type.__name__ = "Integer32"
_CnGpsInternalSv_Object = MibScalar
cnGpsInternalSv = _CnGpsInternalSv_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 5, 0, 29),
    _CnGpsInternalSv_Type()
)
cnGpsInternalSv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnGpsInternalSv.setStatus("current")


class _CnGpsExternalSv_Type(Integer32):
    """Custom type cnGpsExternalSv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_CnGpsExternalSv_Type.__name__ = "Integer32"
_CnGpsExternalSv_Object = MibScalar
cnGpsExternalSv = _CnGpsExternalSv_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 5, 0, 30),
    _CnGpsExternalSv_Type()
)
cnGpsExternalSv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnGpsExternalSv.setStatus("current")


class _CnGpsInternalSu_Type(Integer32):
    """Custom type cnGpsInternalSu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_CnGpsInternalSu_Type.__name__ = "Integer32"
_CnGpsInternalSu_Object = MibScalar
cnGpsInternalSu = _CnGpsInternalSu_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 5, 0, 31),
    _CnGpsInternalSu_Type()
)
cnGpsInternalSu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnGpsInternalSu.setStatus("current")


class _CnGpsExternalSu_Type(Integer32):
    """Custom type cnGpsExternalSu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_CnGpsExternalSu_Type.__name__ = "Integer32"
_CnGpsExternalSu_Object = MibScalar
cnGpsExternalSu = _CnGpsExternalSu_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 5, 0, 32),
    _CnGpsExternalSu_Type()
)
cnGpsExternalSu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnGpsExternalSu.setStatus("current")


class _CnGpsExternalSourcePower_Type(Integer32):
    """Custom type cnGpsExternalSourcePower based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("power-on", 1),
          ("power-off", 2))
    )


_CnGpsExternalSourcePower_Type.__name__ = "Integer32"
_CnGpsExternalSourcePower_Object = MibScalar
cnGpsExternalSourcePower = _CnGpsExternalSourcePower_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 5, 0, 33),
    _CnGpsExternalSourcePower_Type()
)
cnGpsExternalSourcePower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnGpsExternalSourcePower.setStatus("current")

# Managed Objects groups


# Notification objects

cnGpsTrapMsg = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 24, 5, 0, 5)
)
cnGpsTrapMsg.setObjects(
    ("CAMBIUM-NETWORKS-GPS-MIB", "cnGpsSignalStatus")
)
if mibBuilder.loadTexts:
    cnGpsTrapMsg.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CAMBIUM-NETWORKS-GPS-MIB",
    **{"cnGpsMib": cnGpsMib,
       "cnGpsObjects": cnGpsObjects,
       "cnGpsInternalSourceAdminStatus": cnGpsInternalSourceAdminStatus,
       "cnGpsExternalSourceAdminStatus": cnGpsExternalSourceAdminStatus,
       "cnGpsPortTable": cnGpsPortTable,
       "cnGpsPortEntry": cnGpsPortEntry,
       "cnGpsPortIndex": cnGpsPortIndex,
       "cnGpsPortOutputAdminStatus": cnGpsPortOutputAdminStatus,
       "cnGpsSignalStatus": cnGpsSignalStatus,
       "cnGpsTrapMsg": cnGpsTrapMsg,
       "cnGpsSourcePowerCycle": cnGpsSourcePowerCycle,
       "cnGpsInternalTime": cnGpsInternalTime,
       "cnGpsExternalTime": cnGpsExternalTime,
       "cnGpsInternalLatitude": cnGpsInternalLatitude,
       "cnGpsExternalLatitude": cnGpsExternalLatitude,
       "cnGpsInternalLongitude": cnGpsInternalLongitude,
       "cnGpsExternalLongitude": cnGpsExternalLongitude,
       "cnGpsInternalSignalQuality": cnGpsInternalSignalQuality,
       "cnGpsExternalSignalQuality": cnGpsExternalSignalQuality,
       "cnGpsInternalAntennaAltitude": cnGpsInternalAntennaAltitude,
       "cnGpsExternalAntennaAltitude": cnGpsExternalAntennaAltitude,
       "cnGpsInternalAntennaBaseAltitude": cnGpsInternalAntennaBaseAltitude,
       "cnGpsExternalAntennaBaseAltitude": cnGpsExternalAntennaBaseAltitude,
       "cnGpsInternalSelectionMode": cnGpsInternalSelectionMode,
       "cnGpsExternalSelectionMode": cnGpsExternalSelectionMode,
       "cnGpsInternalLocalizationType": cnGpsInternalLocalizationType,
       "cnGpsExternalLocalizationType": cnGpsExternalLocalizationType,
       "cnGpsInternalPdop": cnGpsInternalPdop,
       "cnGpsExternalPdop": cnGpsExternalPdop,
       "cnGpsInternalHdop": cnGpsInternalHdop,
       "cnGpsExternalHdop": cnGpsExternalHdop,
       "cnGpsInternalVdop": cnGpsInternalVdop,
       "cnGpsExternalVdop": cnGpsExternalVdop,
       "cnGpsInternalSv": cnGpsInternalSv,
       "cnGpsExternalSv": cnGpsExternalSv,
       "cnGpsInternalSu": cnGpsInternalSu,
       "cnGpsExternalSu": cnGpsExternalSu,
       "cnGpsExternalSourcePower": cnGpsExternalSourcePower}
)
