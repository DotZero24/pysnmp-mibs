# SNMP MIB module (CAMBIUM-CNMAESTRO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/cambium/CAMBIUM-CNMAESTRO-MIB
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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

cnMaestroMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 23)
)
if mibBuilder.loadTexts:
    cnMaestroMIB.setRevisions(
        ("2017-05-01 08:08",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cambium_ObjectIdentity = ObjectIdentity
cambium = _Cambium_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713)
)
_CnMaestroTrap_ObjectIdentity = ObjectIdentity
cnMaestroTrap = _CnMaestroTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 23, 1)
)


class _CnMaestroTrapName_Type(DisplayString):
    """Custom type cnMaestroTrapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CnMaestroTrapName_Type.__name__ = "DisplayString"
_CnMaestroTrapName_Object = MibScalar
cnMaestroTrapName = _CnMaestroTrapName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 1, 1),
    _CnMaestroTrapName_Type()
)
cnMaestroTrapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnMaestroTrapName.setStatus("current")


class _CnMaestroTrapCategory_Type(DisplayString):
    """Custom type cnMaestroTrapCategory based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CnMaestroTrapCategory_Type.__name__ = "DisplayString"
_CnMaestroTrapCategory_Object = MibScalar
cnMaestroTrapCategory = _CnMaestroTrapCategory_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 1, 2),
    _CnMaestroTrapCategory_Type()
)
cnMaestroTrapCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnMaestroTrapCategory.setStatus("current")


class _CnMaestroTrapSource_Type(DisplayString):
    """Custom type cnMaestroTrapSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CnMaestroTrapSource_Type.__name__ = "DisplayString"
_CnMaestroTrapSource_Object = MibScalar
cnMaestroTrapSource = _CnMaestroTrapSource_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 1, 3),
    _CnMaestroTrapSource_Type()
)
cnMaestroTrapSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnMaestroTrapSource.setStatus("current")


class _CnMaestroTrapSourceType_Type(Integer32):
    """Custom type cnMaestroTrapSourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("device", 0)
    )


_CnMaestroTrapSourceType_Type.__name__ = "Integer32"
_CnMaestroTrapSourceType_Object = MibScalar
cnMaestroTrapSourceType = _CnMaestroTrapSourceType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 1, 4),
    _CnMaestroTrapSourceType_Type()
)
cnMaestroTrapSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnMaestroTrapSourceType.setStatus("current")


class _CnMaestroTrapMessage_Type(DisplayString):
    """Custom type cnMaestroTrapMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CnMaestroTrapMessage_Type.__name__ = "DisplayString"
_CnMaestroTrapMessage_Object = MibScalar
cnMaestroTrapMessage = _CnMaestroTrapMessage_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 1, 5),
    _CnMaestroTrapMessage_Type()
)
cnMaestroTrapMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnMaestroTrapMessage.setStatus("current")


class _CnMaestroTrapSeverity_Type(Integer32):
    """Custom type cnMaestroTrapSeverity based on Integer32"""
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
        *(("critical", 0),
          ("major", 1),
          ("minor", 2),
          ("clear", 3))
    )


_CnMaestroTrapSeverity_Type.__name__ = "Integer32"
_CnMaestroTrapSeverity_Object = MibScalar
cnMaestroTrapSeverity = _CnMaestroTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 1, 6),
    _CnMaestroTrapSeverity_Type()
)
cnMaestroTrapSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnMaestroTrapSeverity.setStatus("current")
_CnMaestroTrapTime_Type = Counter32
_CnMaestroTrapTime_Object = MibScalar
cnMaestroTrapTime = _CnMaestroTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 1, 7),
    _CnMaestroTrapTime_Type()
)
cnMaestroTrapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnMaestroTrapTime.setStatus("current")
_CnMaestroTrapDeviceMAC_Type = MacAddress
_CnMaestroTrapDeviceMAC_Object = MibScalar
cnMaestroTrapDeviceMAC = _CnMaestroTrapDeviceMAC_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 1, 8),
    _CnMaestroTrapDeviceMAC_Type()
)
cnMaestroTrapDeviceMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnMaestroTrapDeviceMAC.setStatus("current")
_CnMaestroTrapClientMAC_Type = MacAddress
_CnMaestroTrapClientMAC_Object = MibScalar
cnMaestroTrapClientMAC = _CnMaestroTrapClientMAC_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 1, 9),
    _CnMaestroTrapClientMAC_Type()
)
cnMaestroTrapClientMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnMaestroTrapClientMAC.setStatus("current")
_CnMaestroServer_ObjectIdentity = ObjectIdentity
cnMaestroServer = _CnMaestroServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 23, 2)
)
_CnMaestroServerTrap_ObjectIdentity = ObjectIdentity
cnMaestroServerTrap = _CnMaestroServerTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 23, 2, 3)
)
_CnMaestroDevice_ObjectIdentity = ObjectIdentity
cnMaestroDevice = _CnMaestroDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 23, 4)
)
_CnMaestroDeviceTable_Object = MibTable
cnMaestroDeviceTable = _CnMaestroDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 4, 1)
)
if mibBuilder.loadTexts:
    cnMaestroDeviceTable.setStatus("current")
_CnMaestroDeviceEntry_Object = MibTableRow
cnMaestroDeviceEntry = _CnMaestroDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 4, 1, 1)
)
cnMaestroDeviceEntry.setIndexNames(
    (0, "CAMBIUM-CNMAESTRO-MIB", "cnMaestroDeviceMAC"),
)
if mibBuilder.loadTexts:
    cnMaestroDeviceEntry.setStatus("current")
_CnMaestroDeviceMAC_Type = MacAddress
_CnMaestroDeviceMAC_Object = MibTableColumn
cnMaestroDeviceMAC = _CnMaestroDeviceMAC_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 4, 1, 1, 1),
    _CnMaestroDeviceMAC_Type()
)
cnMaestroDeviceMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnMaestroDeviceMAC.setStatus("current")


class _CnMaestroDeviceName_Type(DisplayString):
    """Custom type cnMaestroDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CnMaestroDeviceName_Type.__name__ = "DisplayString"
_CnMaestroDeviceName_Object = MibTableColumn
cnMaestroDeviceName = _CnMaestroDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 4, 1, 1, 2),
    _CnMaestroDeviceName_Type()
)
cnMaestroDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnMaestroDeviceName.setStatus("current")


class _CnMaestroDeviceType_Type(DisplayString):
    """Custom type cnMaestroDeviceType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CnMaestroDeviceType_Type.__name__ = "DisplayString"
_CnMaestroDeviceType_Object = MibTableColumn
cnMaestroDeviceType = _CnMaestroDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 4, 1, 1, 3),
    _CnMaestroDeviceType_Type()
)
cnMaestroDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnMaestroDeviceType.setStatus("current")
_CnMaestroDeviceIP_Type = DisplayString
_CnMaestroDeviceIP_Object = MibTableColumn
cnMaestroDeviceIP = _CnMaestroDeviceIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 4, 1, 1, 4),
    _CnMaestroDeviceIP_Type()
)
cnMaestroDeviceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnMaestroDeviceIP.setStatus("current")


class _CnMaestroDeviceStatus_Type(Integer32):
    """Custom type cnMaestroDeviceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("online", 0),
          ("offline", 1),
          ("onboarding", 3))
    )


_CnMaestroDeviceStatus_Type.__name__ = "Integer32"
_CnMaestroDeviceStatus_Object = MibTableColumn
cnMaestroDeviceStatus = _CnMaestroDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 4, 1, 1, 5),
    _CnMaestroDeviceStatus_Type()
)
cnMaestroDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnMaestroDeviceStatus.setStatus("current")
_CnMaestroDeviceStatusInterval_Type = Counter64
_CnMaestroDeviceStatusInterval_Object = MibTableColumn
cnMaestroDeviceStatusInterval = _CnMaestroDeviceStatusInterval_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 4, 1, 1, 6),
    _CnMaestroDeviceStatusInterval_Type()
)
cnMaestroDeviceStatusInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnMaestroDeviceStatusInterval.setStatus("current")


class _CnMaestroDeviceSWVersion_Type(DisplayString):
    """Custom type cnMaestroDeviceSWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CnMaestroDeviceSWVersion_Type.__name__ = "DisplayString"
_CnMaestroDeviceSWVersion_Object = MibTableColumn
cnMaestroDeviceSWVersion = _CnMaestroDeviceSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 4, 1, 1, 7),
    _CnMaestroDeviceSWVersion_Type()
)
cnMaestroDeviceSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnMaestroDeviceSWVersion.setStatus("current")


class _CnMaestroDeviceHWVersion_Type(DisplayString):
    """Custom type cnMaestroDeviceHWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CnMaestroDeviceHWVersion_Type.__name__ = "DisplayString"
_CnMaestroDeviceHWVersion_Object = MibTableColumn
cnMaestroDeviceHWVersion = _CnMaestroDeviceHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 4, 1, 1, 8),
    _CnMaestroDeviceHWVersion_Type()
)
cnMaestroDeviceHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnMaestroDeviceHWVersion.setStatus("current")


class _CnMaestroDeviceCountry_Type(DisplayString):
    """Custom type cnMaestroDeviceCountry based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CnMaestroDeviceCountry_Type.__name__ = "DisplayString"
_CnMaestroDeviceCountry_Object = MibTableColumn
cnMaestroDeviceCountry = _CnMaestroDeviceCountry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 4, 1, 1, 9),
    _CnMaestroDeviceCountry_Type()
)
cnMaestroDeviceCountry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnMaestroDeviceCountry.setStatus("current")


class _CnMaestroDeviceLatitude_Type(DisplayString):
    """Custom type cnMaestroDeviceLatitude based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CnMaestroDeviceLatitude_Type.__name__ = "DisplayString"
_CnMaestroDeviceLatitude_Object = MibTableColumn
cnMaestroDeviceLatitude = _CnMaestroDeviceLatitude_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 4, 1, 1, 10),
    _CnMaestroDeviceLatitude_Type()
)
cnMaestroDeviceLatitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnMaestroDeviceLatitude.setStatus("current")


class _CnMaestroDeviceLongitude_Type(DisplayString):
    """Custom type cnMaestroDeviceLongitude based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CnMaestroDeviceLongitude_Type.__name__ = "DisplayString"
_CnMaestroDeviceLongitude_Object = MibTableColumn
cnMaestroDeviceLongitude = _CnMaestroDeviceLongitude_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 4, 1, 1, 11),
    _CnMaestroDeviceLongitude_Type()
)
cnMaestroDeviceLongitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnMaestroDeviceLongitude.setStatus("current")
_CnMaestroCnPilot_ObjectIdentity = ObjectIdentity
cnMaestroCnPilot = _CnMaestroCnPilot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 23, 4, 2)
)
_CnMaestroCnPilotAPTable_Object = MibTable
cnMaestroCnPilotAPTable = _CnMaestroCnPilotAPTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 4, 2, 1)
)
if mibBuilder.loadTexts:
    cnMaestroCnPilotAPTable.setStatus("current")
_CnMaestroCnPilotAPEntry_Object = MibTableRow
cnMaestroCnPilotAPEntry = _CnMaestroCnPilotAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 4, 2, 1, 1)
)
cnMaestroCnPilotAPEntry.setIndexNames(
    (0, "CAMBIUM-CNMAESTRO-MIB", "cnMaestroCnPilotAPMAC"),
)
if mibBuilder.loadTexts:
    cnMaestroCnPilotAPEntry.setStatus("current")
_CnMaestroCnPilotAPMAC_Type = MacAddress
_CnMaestroCnPilotAPMAC_Object = MibTableColumn
cnMaestroCnPilotAPMAC = _CnMaestroCnPilotAPMAC_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 4, 2, 1, 1, 1),
    _CnMaestroCnPilotAPMAC_Type()
)
cnMaestroCnPilotAPMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnMaestroCnPilotAPMAC.setStatus("current")


class _CnMaestroCnPilotAPName_Type(DisplayString):
    """Custom type cnMaestroCnPilotAPName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CnMaestroCnPilotAPName_Type.__name__ = "DisplayString"
_CnMaestroCnPilotAPName_Object = MibTableColumn
cnMaestroCnPilotAPName = _CnMaestroCnPilotAPName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 4, 2, 1, 1, 2),
    _CnMaestroCnPilotAPName_Type()
)
cnMaestroCnPilotAPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnMaestroCnPilotAPName.setStatus("current")
_CnMaestroCnPilotAPIP_Type = DisplayString
_CnMaestroCnPilotAPIP_Object = MibTableColumn
cnMaestroCnPilotAPIP = _CnMaestroCnPilotAPIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 4, 2, 1, 1, 3),
    _CnMaestroCnPilotAPIP_Type()
)
cnMaestroCnPilotAPIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnMaestroCnPilotAPIP.setStatus("current")


class _CnMaestroCnPilotAPSerialNumber_Type(DisplayString):
    """Custom type cnMaestroCnPilotAPSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CnMaestroCnPilotAPSerialNumber_Type.__name__ = "DisplayString"
_CnMaestroCnPilotAPSerialNumber_Object = MibTableColumn
cnMaestroCnPilotAPSerialNumber = _CnMaestroCnPilotAPSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 4, 2, 1, 1, 4),
    _CnMaestroCnPilotAPSerialNumber_Type()
)
cnMaestroCnPilotAPSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnMaestroCnPilotAPSerialNumber.setStatus("current")


class _CnMaestroCnPilotAPModel_Type(DisplayString):
    """Custom type cnMaestroCnPilotAPModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CnMaestroCnPilotAPModel_Type.__name__ = "DisplayString"
_CnMaestroCnPilotAPModel_Object = MibTableColumn
cnMaestroCnPilotAPModel = _CnMaestroCnPilotAPModel_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 4, 2, 1, 1, 5),
    _CnMaestroCnPilotAPModel_Type()
)
cnMaestroCnPilotAPModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnMaestroCnPilotAPModel.setStatus("current")


class _CnMaestroCnPilotAPCPUUtilization_Type(Integer32):
    """Custom type cnMaestroCnPilotAPCPUUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CnMaestroCnPilotAPCPUUtilization_Type.__name__ = "Integer32"
_CnMaestroCnPilotAPCPUUtilization_Object = MibTableColumn
cnMaestroCnPilotAPCPUUtilization = _CnMaestroCnPilotAPCPUUtilization_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 4, 2, 1, 1, 6),
    _CnMaestroCnPilotAPCPUUtilization_Type()
)
cnMaestroCnPilotAPCPUUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnMaestroCnPilotAPCPUUtilization.setStatus("current")


class _CnMaestroCnPilotAPSWVersion_Type(DisplayString):
    """Custom type cnMaestroCnPilotAPSWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CnMaestroCnPilotAPSWVersion_Type.__name__ = "DisplayString"
_CnMaestroCnPilotAPSWVersion_Object = MibTableColumn
cnMaestroCnPilotAPSWVersion = _CnMaestroCnPilotAPSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 4, 2, 1, 1, 7),
    _CnMaestroCnPilotAPSWVersion_Type()
)
cnMaestroCnPilotAPSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnMaestroCnPilotAPSWVersion.setStatus("current")
_CnMaestroCnPilotAPUptime_Type = Counter64
_CnMaestroCnPilotAPUptime_Object = MibTableColumn
cnMaestroCnPilotAPUptime = _CnMaestroCnPilotAPUptime_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 4, 2, 1, 1, 8),
    _CnMaestroCnPilotAPUptime_Type()
)
cnMaestroCnPilotAPUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnMaestroCnPilotAPUptime.setStatus("current")


class _CnMaestroCnPilotAPHWType_Type(DisplayString):
    """Custom type cnMaestroCnPilotAPHWType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CnMaestroCnPilotAPHWType_Type.__name__ = "DisplayString"
_CnMaestroCnPilotAPHWType_Object = MibTableColumn
cnMaestroCnPilotAPHWType = _CnMaestroCnPilotAPHWType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 4, 2, 1, 1, 9),
    _CnMaestroCnPilotAPHWType_Type()
)
cnMaestroCnPilotAPHWType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnMaestroCnPilotAPHWType.setStatus("current")


class _CnMaestroCnPilotAPTotalClients_Type(Integer32):
    """Custom type cnMaestroCnPilotAPTotalClients based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_CnMaestroCnPilotAPTotalClients_Type.__name__ = "Integer32"
_CnMaestroCnPilotAPTotalClients_Object = MibTableColumn
cnMaestroCnPilotAPTotalClients = _CnMaestroCnPilotAPTotalClients_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 4, 2, 1, 1, 10),
    _CnMaestroCnPilotAPTotalClients_Type()
)
cnMaestroCnPilotAPTotalClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnMaestroCnPilotAPTotalClients.setStatus("current")
_CnMaestroCnPilotRadioTable_Object = MibTable
cnMaestroCnPilotRadioTable = _CnMaestroCnPilotRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 4, 2, 2)
)
if mibBuilder.loadTexts:
    cnMaestroCnPilotRadioTable.setStatus("current")
_CnMaestroCnPilotRadioEntry_Object = MibTableRow
cnMaestroCnPilotRadioEntry = _CnMaestroCnPilotRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 4, 2, 2, 1)
)
cnMaestroCnPilotRadioEntry.setIndexNames(
    (0, "CAMBIUM-CNMAESTRO-MIB", "cnMaestroCnPilotRadioAPMAC"),
    (0, "CAMBIUM-CNMAESTRO-MIB", "cnMaestroCnPilotRadioIndex"),
)
if mibBuilder.loadTexts:
    cnMaestroCnPilotRadioEntry.setStatus("current")
_CnMaestroCnPilotRadioAPMAC_Type = MacAddress
_CnMaestroCnPilotRadioAPMAC_Object = MibTableColumn
cnMaestroCnPilotRadioAPMAC = _CnMaestroCnPilotRadioAPMAC_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 4, 2, 2, 1, 1),
    _CnMaestroCnPilotRadioAPMAC_Type()
)
cnMaestroCnPilotRadioAPMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnMaestroCnPilotRadioAPMAC.setStatus("current")


class _CnMaestroCnPilotRadioIndex_Type(Integer32):
    """Custom type cnMaestroCnPilotRadioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_CnMaestroCnPilotRadioIndex_Type.__name__ = "Integer32"
_CnMaestroCnPilotRadioIndex_Object = MibTableColumn
cnMaestroCnPilotRadioIndex = _CnMaestroCnPilotRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 4, 2, 2, 1, 2),
    _CnMaestroCnPilotRadioIndex_Type()
)
cnMaestroCnPilotRadioIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnMaestroCnPilotRadioIndex.setStatus("current")
_CnMaestroCnPilotRadioMAC_Type = MacAddress
_CnMaestroCnPilotRadioMAC_Object = MibTableColumn
cnMaestroCnPilotRadioMAC = _CnMaestroCnPilotRadioMAC_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 4, 2, 2, 1, 3),
    _CnMaestroCnPilotRadioMAC_Type()
)
cnMaestroCnPilotRadioMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnMaestroCnPilotRadioMAC.setStatus("current")


class _CnMaestroCnPilotRadioBandType_Type(DisplayString):
    """Custom type cnMaestroCnPilotRadioBandType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CnMaestroCnPilotRadioBandType_Type.__name__ = "DisplayString"
_CnMaestroCnPilotRadioBandType_Object = MibTableColumn
cnMaestroCnPilotRadioBandType = _CnMaestroCnPilotRadioBandType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 4, 2, 2, 1, 4),
    _CnMaestroCnPilotRadioBandType_Type()
)
cnMaestroCnPilotRadioBandType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnMaestroCnPilotRadioBandType.setStatus("current")


class _CnMaestroCnPilotRadioWLAN_Type(Integer32):
    """Custom type cnMaestroCnPilotRadioWLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CnMaestroCnPilotRadioWLAN_Type.__name__ = "Integer32"
_CnMaestroCnPilotRadioWLAN_Object = MibTableColumn
cnMaestroCnPilotRadioWLAN = _CnMaestroCnPilotRadioWLAN_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 4, 2, 2, 1, 5),
    _CnMaestroCnPilotRadioWLAN_Type()
)
cnMaestroCnPilotRadioWLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnMaestroCnPilotRadioWLAN.setStatus("current")


class _CnMaestroCnPilotRadioNumClients_Type(Integer32):
    """Custom type cnMaestroCnPilotRadioNumClients based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_CnMaestroCnPilotRadioNumClients_Type.__name__ = "Integer32"
_CnMaestroCnPilotRadioNumClients_Object = MibTableColumn
cnMaestroCnPilotRadioNumClients = _CnMaestroCnPilotRadioNumClients_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 4, 2, 2, 1, 6),
    _CnMaestroCnPilotRadioNumClients_Type()
)
cnMaestroCnPilotRadioNumClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnMaestroCnPilotRadioNumClients.setStatus("current")


class _CnMaestroCnPilotRadioChannel_Type(DisplayString):
    """Custom type cnMaestroCnPilotRadioChannel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CnMaestroCnPilotRadioChannel_Type.__name__ = "DisplayString"
_CnMaestroCnPilotRadioChannel_Object = MibTableColumn
cnMaestroCnPilotRadioChannel = _CnMaestroCnPilotRadioChannel_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 4, 2, 2, 1, 7),
    _CnMaestroCnPilotRadioChannel_Type()
)
cnMaestroCnPilotRadioChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnMaestroCnPilotRadioChannel.setStatus("current")


class _CnMaestroCnPilotRadioTransmitPower_Type(Integer32):
    """Custom type cnMaestroCnPilotRadioTransmitPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_CnMaestroCnPilotRadioTransmitPower_Type.__name__ = "Integer32"
_CnMaestroCnPilotRadioTransmitPower_Object = MibTableColumn
cnMaestroCnPilotRadioTransmitPower = _CnMaestroCnPilotRadioTransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 4, 2, 2, 1, 8),
    _CnMaestroCnPilotRadioTransmitPower_Type()
)
cnMaestroCnPilotRadioTransmitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnMaestroCnPilotRadioTransmitPower.setStatus("current")
_CnMaestroCnPilotRadioTxDataBytes_Type = Counter64
_CnMaestroCnPilotRadioTxDataBytes_Object = MibTableColumn
cnMaestroCnPilotRadioTxDataBytes = _CnMaestroCnPilotRadioTxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 4, 2, 2, 1, 9),
    _CnMaestroCnPilotRadioTxDataBytes_Type()
)
cnMaestroCnPilotRadioTxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnMaestroCnPilotRadioTxDataBytes.setStatus("current")
_CnMaestroCnPilotRadioRxDataBytes_Type = Counter64
_CnMaestroCnPilotRadioRxDataBytes_Object = MibTableColumn
cnMaestroCnPilotRadioRxDataBytes = _CnMaestroCnPilotRadioRxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 4, 2, 2, 1, 10),
    _CnMaestroCnPilotRadioRxDataBytes_Type()
)
cnMaestroCnPilotRadioRxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnMaestroCnPilotRadioRxDataBytes.setStatus("current")


class _CnMaestroCnPilotRadioState_Type(Integer32):
    """Custom type cnMaestroCnPilotRadioState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("on", 0),
          ("off", 1))
    )


_CnMaestroCnPilotRadioState_Type.__name__ = "Integer32"
_CnMaestroCnPilotRadioState_Object = MibTableColumn
cnMaestroCnPilotRadioState = _CnMaestroCnPilotRadioState_Object(
    (1, 3, 6, 1, 4, 1, 17713, 23, 4, 2, 2, 1, 11),
    _CnMaestroCnPilotRadioState_Type()
)
cnMaestroCnPilotRadioState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnMaestroCnPilotRadioState.setStatus("current")

# Managed Objects groups


# Notification objects

cnMaestroServerTrapDeviceOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 23, 2, 3, 1)
)
cnMaestroServerTrapDeviceOnline.setObjects(
      *(("CAMBIUM-CNMAESTRO-MIB", "cnMaestroTrapName"),
        ("CAMBIUM-CNMAESTRO-MIB", "cnMaestroTrapCategory"),
        ("CAMBIUM-CNMAESTRO-MIB", "cnMaestroTrapSource"),
        ("CAMBIUM-CNMAESTRO-MIB", "cnMaestroTrapSourceType"),
        ("CAMBIUM-CNMAESTRO-MIB", "cnMaestroTrapMessage"),
        ("CAMBIUM-CNMAESTRO-MIB", "cnMaestroTrapSeverity"),
        ("CAMBIUM-CNMAESTRO-MIB", "cnMaestroTrapTime"),
        ("CAMBIUM-CNMAESTRO-MIB", "cnMaestroTrapDeviceMAC"))
)
if mibBuilder.loadTexts:
    cnMaestroServerTrapDeviceOnline.setStatus(
        "current"
    )

cnMaestroServerTrapDeviceOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 23, 2, 3, 2)
)
cnMaestroServerTrapDeviceOffline.setObjects(
      *(("CAMBIUM-CNMAESTRO-MIB", "cnMaestroTrapName"),
        ("CAMBIUM-CNMAESTRO-MIB", "cnMaestroTrapCategory"),
        ("CAMBIUM-CNMAESTRO-MIB", "cnMaestroTrapSource"),
        ("CAMBIUM-CNMAESTRO-MIB", "cnMaestroTrapSourceType"),
        ("CAMBIUM-CNMAESTRO-MIB", "cnMaestroTrapMessage"),
        ("CAMBIUM-CNMAESTRO-MIB", "cnMaestroTrapSeverity"),
        ("CAMBIUM-CNMAESTRO-MIB", "cnMaestroTrapTime"),
        ("CAMBIUM-CNMAESTRO-MIB", "cnMaestroTrapDeviceMAC"))
)
if mibBuilder.loadTexts:
    cnMaestroServerTrapDeviceOffline.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CAMBIUM-CNMAESTRO-MIB",
    **{"cambium": cambium,
       "cnMaestroMIB": cnMaestroMIB,
       "cnMaestroTrap": cnMaestroTrap,
       "cnMaestroTrapName": cnMaestroTrapName,
       "cnMaestroTrapCategory": cnMaestroTrapCategory,
       "cnMaestroTrapSource": cnMaestroTrapSource,
       "cnMaestroTrapSourceType": cnMaestroTrapSourceType,
       "cnMaestroTrapMessage": cnMaestroTrapMessage,
       "cnMaestroTrapSeverity": cnMaestroTrapSeverity,
       "cnMaestroTrapTime": cnMaestroTrapTime,
       "cnMaestroTrapDeviceMAC": cnMaestroTrapDeviceMAC,
       "cnMaestroTrapClientMAC": cnMaestroTrapClientMAC,
       "cnMaestroServer": cnMaestroServer,
       "cnMaestroServerTrap": cnMaestroServerTrap,
       "cnMaestroServerTrapDeviceOnline": cnMaestroServerTrapDeviceOnline,
       "cnMaestroServerTrapDeviceOffline": cnMaestroServerTrapDeviceOffline,
       "cnMaestroDevice": cnMaestroDevice,
       "cnMaestroDeviceTable": cnMaestroDeviceTable,
       "cnMaestroDeviceEntry": cnMaestroDeviceEntry,
       "cnMaestroDeviceMAC": cnMaestroDeviceMAC,
       "cnMaestroDeviceName": cnMaestroDeviceName,
       "cnMaestroDeviceType": cnMaestroDeviceType,
       "cnMaestroDeviceIP": cnMaestroDeviceIP,
       "cnMaestroDeviceStatus": cnMaestroDeviceStatus,
       "cnMaestroDeviceStatusInterval": cnMaestroDeviceStatusInterval,
       "cnMaestroDeviceSWVersion": cnMaestroDeviceSWVersion,
       "cnMaestroDeviceHWVersion": cnMaestroDeviceHWVersion,
       "cnMaestroDeviceCountry": cnMaestroDeviceCountry,
       "cnMaestroDeviceLatitude": cnMaestroDeviceLatitude,
       "cnMaestroDeviceLongitude": cnMaestroDeviceLongitude,
       "cnMaestroCnPilot": cnMaestroCnPilot,
       "cnMaestroCnPilotAPTable": cnMaestroCnPilotAPTable,
       "cnMaestroCnPilotAPEntry": cnMaestroCnPilotAPEntry,
       "cnMaestroCnPilotAPMAC": cnMaestroCnPilotAPMAC,
       "cnMaestroCnPilotAPName": cnMaestroCnPilotAPName,
       "cnMaestroCnPilotAPIP": cnMaestroCnPilotAPIP,
       "cnMaestroCnPilotAPSerialNumber": cnMaestroCnPilotAPSerialNumber,
       "cnMaestroCnPilotAPModel": cnMaestroCnPilotAPModel,
       "cnMaestroCnPilotAPCPUUtilization": cnMaestroCnPilotAPCPUUtilization,
       "cnMaestroCnPilotAPSWVersion": cnMaestroCnPilotAPSWVersion,
       "cnMaestroCnPilotAPUptime": cnMaestroCnPilotAPUptime,
       "cnMaestroCnPilotAPHWType": cnMaestroCnPilotAPHWType,
       "cnMaestroCnPilotAPTotalClients": cnMaestroCnPilotAPTotalClients,
       "cnMaestroCnPilotRadioTable": cnMaestroCnPilotRadioTable,
       "cnMaestroCnPilotRadioEntry": cnMaestroCnPilotRadioEntry,
       "cnMaestroCnPilotRadioAPMAC": cnMaestroCnPilotRadioAPMAC,
       "cnMaestroCnPilotRadioIndex": cnMaestroCnPilotRadioIndex,
       "cnMaestroCnPilotRadioMAC": cnMaestroCnPilotRadioMAC,
       "cnMaestroCnPilotRadioBandType": cnMaestroCnPilotRadioBandType,
       "cnMaestroCnPilotRadioWLAN": cnMaestroCnPilotRadioWLAN,
       "cnMaestroCnPilotRadioNumClients": cnMaestroCnPilotRadioNumClients,
       "cnMaestroCnPilotRadioChannel": cnMaestroCnPilotRadioChannel,
       "cnMaestroCnPilotRadioTransmitPower": cnMaestroCnPilotRadioTransmitPower,
       "cnMaestroCnPilotRadioTxDataBytes": cnMaestroCnPilotRadioTxDataBytes,
       "cnMaestroCnPilotRadioRxDataBytes": cnMaestroCnPilotRadioRxDataBytes,
       "cnMaestroCnPilotRadioState": cnMaestroCnPilotRadioState}
)
