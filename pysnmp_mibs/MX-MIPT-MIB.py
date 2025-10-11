# SNMP MIB module (MX-MIPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-MIPT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:01 2025
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

(mediatrixServices,) = mibBuilder.importSymbols(
    "MX-SMI2",
    "mediatrixServices")

(MxActivationState,
 MxAdvancedIpPort,
 MxDigitMap,
 MxEnableState,
 MxIpAddress,
 MxIpHostName,
 MxIpPort,
 MxIpSubnetMask) = mibBuilder.importSymbols(
    "MX-TC",
    "MxActivationState",
    "MxAdvancedIpPort",
    "MxDigitMap",
    "MxEnableState",
    "MxIpAddress",
    "MxIpHostName",
    "MxIpPort",
    "MxIpSubnetMask")

(MxFloat32,
 MxIpAddr,
 MxIpAddrMask,
 MxIpAddrPort,
 MxIpHostNamePort,
 MxUInt64,
 MxUri,
 MxUrl) = mibBuilder.importSymbols(
    "MX-TC2",
    "MxFloat32",
    "MxIpAddr",
    "MxIpAddrMask",
    "MxIpAddrPort",
    "MxIpHostNamePort",
    "MxUInt64",
    "MxUri",
    "MxUrl")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

miptMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MiptMIBObjects_ObjectIdentity = ObjectIdentity
miptMIBObjects = _MiptMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1)
)
_CodecGroup_ObjectIdentity = ObjectIdentity
codecGroup = _CodecGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100)
)


class _DefaultCodecGenericVoiceActivityDetection_Type(Integer32):
    """Custom type defaultCodecGenericVoiceActivityDetection based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300)
        )
    )
    namedValues = NamedValues(
        *(("disable", 100),
          ("transparent", 200),
          ("conservative", 300))
    )


_DefaultCodecGenericVoiceActivityDetection_Type.__name__ = "Integer32"
_DefaultCodecGenericVoiceActivityDetection_Object = MibScalar
defaultCodecGenericVoiceActivityDetection = _DefaultCodecGenericVoiceActivityDetection_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 100),
    _DefaultCodecGenericVoiceActivityDetection_Type()
)
defaultCodecGenericVoiceActivityDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecGenericVoiceActivityDetection.setStatus("current")
_EpSpecificCodecTable_Object = MibTable
epSpecificCodecTable = _EpSpecificCodecTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 200)
)
if mibBuilder.loadTexts:
    epSpecificCodecTable.setStatus("current")
_EpSpecificCodecEntry_Object = MibTableRow
epSpecificCodecEntry = _EpSpecificCodecEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 200, 1)
)
epSpecificCodecEntry.setIndexNames(
    (0, "MX-MIPT-MIB", "epSpecificCodecEpId"),
)
if mibBuilder.loadTexts:
    epSpecificCodecEntry.setStatus("current")
_EpSpecificCodecEpId_Type = OctetString
_EpSpecificCodecEpId_Object = MibTableColumn
epSpecificCodecEpId = _EpSpecificCodecEpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 200, 1, 100),
    _EpSpecificCodecEpId_Type()
)
epSpecificCodecEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epSpecificCodecEpId.setStatus("current")


class _EpSpecificCodecEnableConfig_Type(MxEnableState):
    """Custom type epSpecificCodecEnableConfig based on MxEnableState"""
    defaultValue = 0


_EpSpecificCodecEnableConfig_Type.__name__ = "MxEnableState"
_EpSpecificCodecEnableConfig_Object = MibTableColumn
epSpecificCodecEnableConfig = _EpSpecificCodecEnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 200, 1, 200),
    _EpSpecificCodecEnableConfig_Type()
)
epSpecificCodecEnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecEnableConfig.setStatus("current")


class _EpSpecificCodecGenericVoiceActivityDetection_Type(Integer32):
    """Custom type epSpecificCodecGenericVoiceActivityDetection based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300)
        )
    )
    namedValues = NamedValues(
        *(("disable", 100),
          ("transparent", 200),
          ("conservative", 300))
    )


_EpSpecificCodecGenericVoiceActivityDetection_Type.__name__ = "Integer32"
_EpSpecificCodecGenericVoiceActivityDetection_Object = MibTableColumn
epSpecificCodecGenericVoiceActivityDetection = _EpSpecificCodecGenericVoiceActivityDetection_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 200, 1, 300),
    _EpSpecificCodecGenericVoiceActivityDetection_Type()
)
epSpecificCodecGenericVoiceActivityDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecGenericVoiceActivityDetection.setStatus("current")
_CodecG711Group_ObjectIdentity = ObjectIdentity
codecG711Group = _CodecG711Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 300)
)
_CodecG711MulawGroup_ObjectIdentity = ObjectIdentity
codecG711MulawGroup = _CodecG711MulawGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 300, 100)
)


class _DefaultCodecG711MulawVoiceEnable_Type(MxEnableState):
    """Custom type defaultCodecG711MulawVoiceEnable based on MxEnableState"""
    defaultValue = 1


_DefaultCodecG711MulawVoiceEnable_Type.__name__ = "MxEnableState"
_DefaultCodecG711MulawVoiceEnable_Object = MibScalar
defaultCodecG711MulawVoiceEnable = _DefaultCodecG711MulawVoiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 300, 100, 100),
    _DefaultCodecG711MulawVoiceEnable_Type()
)
defaultCodecG711MulawVoiceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG711MulawVoiceEnable.setStatus("current")


class _DefaultCodecG711MulawVoicePriority_Type(Unsigned32):
    """Custom type defaultCodecG711MulawVoicePriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_DefaultCodecG711MulawVoicePriority_Type.__name__ = "Unsigned32"
_DefaultCodecG711MulawVoicePriority_Object = MibScalar
defaultCodecG711MulawVoicePriority = _DefaultCodecG711MulawVoicePriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 300, 100, 200),
    _DefaultCodecG711MulawVoicePriority_Type()
)
defaultCodecG711MulawVoicePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG711MulawVoicePriority.setStatus("current")


class _DefaultCodecG711MulawDataEnable_Type(MxEnableState):
    """Custom type defaultCodecG711MulawDataEnable based on MxEnableState"""
    defaultValue = 1


_DefaultCodecG711MulawDataEnable_Type.__name__ = "MxEnableState"
_DefaultCodecG711MulawDataEnable_Object = MibScalar
defaultCodecG711MulawDataEnable = _DefaultCodecG711MulawDataEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 300, 100, 300),
    _DefaultCodecG711MulawDataEnable_Type()
)
defaultCodecG711MulawDataEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG711MulawDataEnable.setStatus("current")


class _DefaultCodecG711MulawDataPriority_Type(Unsigned32):
    """Custom type defaultCodecG711MulawDataPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_DefaultCodecG711MulawDataPriority_Type.__name__ = "Unsigned32"
_DefaultCodecG711MulawDataPriority_Object = MibScalar
defaultCodecG711MulawDataPriority = _DefaultCodecG711MulawDataPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 300, 100, 400),
    _DefaultCodecG711MulawDataPriority_Type()
)
defaultCodecG711MulawDataPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG711MulawDataPriority.setStatus("current")


class _DefaultCodecG711MulawMinPTime_Type(Unsigned32):
    """Custom type defaultCodecG711MulawMinPTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_DefaultCodecG711MulawMinPTime_Type.__name__ = "Unsigned32"
_DefaultCodecG711MulawMinPTime_Object = MibScalar
defaultCodecG711MulawMinPTime = _DefaultCodecG711MulawMinPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 300, 100, 500),
    _DefaultCodecG711MulawMinPTime_Type()
)
defaultCodecG711MulawMinPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG711MulawMinPTime.setStatus("current")


class _DefaultCodecG711MulawMaxPTime_Type(Unsigned32):
    """Custom type defaultCodecG711MulawMaxPTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_DefaultCodecG711MulawMaxPTime_Type.__name__ = "Unsigned32"
_DefaultCodecG711MulawMaxPTime_Object = MibScalar
defaultCodecG711MulawMaxPTime = _DefaultCodecG711MulawMaxPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 300, 100, 600),
    _DefaultCodecG711MulawMaxPTime_Type()
)
defaultCodecG711MulawMaxPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG711MulawMaxPTime.setStatus("current")
_EpSpecificCodecG711MulawTable_Object = MibTable
epSpecificCodecG711MulawTable = _EpSpecificCodecG711MulawTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 300, 100, 700)
)
if mibBuilder.loadTexts:
    epSpecificCodecG711MulawTable.setStatus("current")
_EpSpecificCodecG711MulawEntry_Object = MibTableRow
epSpecificCodecG711MulawEntry = _EpSpecificCodecG711MulawEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 300, 100, 700, 1)
)
epSpecificCodecG711MulawEntry.setIndexNames(
    (0, "MX-MIPT-MIB", "epSpecificCodecG711MulawEpId"),
)
if mibBuilder.loadTexts:
    epSpecificCodecG711MulawEntry.setStatus("current")
_EpSpecificCodecG711MulawEpId_Type = OctetString
_EpSpecificCodecG711MulawEpId_Object = MibTableColumn
epSpecificCodecG711MulawEpId = _EpSpecificCodecG711MulawEpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 300, 100, 700, 1, 100),
    _EpSpecificCodecG711MulawEpId_Type()
)
epSpecificCodecG711MulawEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epSpecificCodecG711MulawEpId.setStatus("current")


class _EpSpecificCodecG711MulawEnableConfig_Type(MxEnableState):
    """Custom type epSpecificCodecG711MulawEnableConfig based on MxEnableState"""
    defaultValue = 0


_EpSpecificCodecG711MulawEnableConfig_Type.__name__ = "MxEnableState"
_EpSpecificCodecG711MulawEnableConfig_Object = MibTableColumn
epSpecificCodecG711MulawEnableConfig = _EpSpecificCodecG711MulawEnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 300, 100, 700, 1, 200),
    _EpSpecificCodecG711MulawEnableConfig_Type()
)
epSpecificCodecG711MulawEnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG711MulawEnableConfig.setStatus("current")


class _EpSpecificCodecG711MulawVoiceEnable_Type(MxEnableState):
    """Custom type epSpecificCodecG711MulawVoiceEnable based on MxEnableState"""
    defaultValue = 1


_EpSpecificCodecG711MulawVoiceEnable_Type.__name__ = "MxEnableState"
_EpSpecificCodecG711MulawVoiceEnable_Object = MibTableColumn
epSpecificCodecG711MulawVoiceEnable = _EpSpecificCodecG711MulawVoiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 300, 100, 700, 1, 300),
    _EpSpecificCodecG711MulawVoiceEnable_Type()
)
epSpecificCodecG711MulawVoiceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG711MulawVoiceEnable.setStatus("current")


class _EpSpecificCodecG711MulawVoicePriority_Type(Unsigned32):
    """Custom type epSpecificCodecG711MulawVoicePriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_EpSpecificCodecG711MulawVoicePriority_Type.__name__ = "Unsigned32"
_EpSpecificCodecG711MulawVoicePriority_Object = MibTableColumn
epSpecificCodecG711MulawVoicePriority = _EpSpecificCodecG711MulawVoicePriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 300, 100, 700, 1, 400),
    _EpSpecificCodecG711MulawVoicePriority_Type()
)
epSpecificCodecG711MulawVoicePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG711MulawVoicePriority.setStatus("current")


class _EpSpecificCodecG711MulawDataEnable_Type(MxEnableState):
    """Custom type epSpecificCodecG711MulawDataEnable based on MxEnableState"""
    defaultValue = 1


_EpSpecificCodecG711MulawDataEnable_Type.__name__ = "MxEnableState"
_EpSpecificCodecG711MulawDataEnable_Object = MibTableColumn
epSpecificCodecG711MulawDataEnable = _EpSpecificCodecG711MulawDataEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 300, 100, 700, 1, 500),
    _EpSpecificCodecG711MulawDataEnable_Type()
)
epSpecificCodecG711MulawDataEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG711MulawDataEnable.setStatus("current")


class _EpSpecificCodecG711MulawDataPriority_Type(Unsigned32):
    """Custom type epSpecificCodecG711MulawDataPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_EpSpecificCodecG711MulawDataPriority_Type.__name__ = "Unsigned32"
_EpSpecificCodecG711MulawDataPriority_Object = MibTableColumn
epSpecificCodecG711MulawDataPriority = _EpSpecificCodecG711MulawDataPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 300, 100, 700, 1, 600),
    _EpSpecificCodecG711MulawDataPriority_Type()
)
epSpecificCodecG711MulawDataPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG711MulawDataPriority.setStatus("current")


class _EpSpecificCodecG711MulawMinPTime_Type(Unsigned32):
    """Custom type epSpecificCodecG711MulawMinPTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_EpSpecificCodecG711MulawMinPTime_Type.__name__ = "Unsigned32"
_EpSpecificCodecG711MulawMinPTime_Object = MibTableColumn
epSpecificCodecG711MulawMinPTime = _EpSpecificCodecG711MulawMinPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 300, 100, 700, 1, 700),
    _EpSpecificCodecG711MulawMinPTime_Type()
)
epSpecificCodecG711MulawMinPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG711MulawMinPTime.setStatus("current")


class _EpSpecificCodecG711MulawMaxPTime_Type(Unsigned32):
    """Custom type epSpecificCodecG711MulawMaxPTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_EpSpecificCodecG711MulawMaxPTime_Type.__name__ = "Unsigned32"
_EpSpecificCodecG711MulawMaxPTime_Object = MibTableColumn
epSpecificCodecG711MulawMaxPTime = _EpSpecificCodecG711MulawMaxPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 300, 100, 700, 1, 800),
    _EpSpecificCodecG711MulawMaxPTime_Type()
)
epSpecificCodecG711MulawMaxPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG711MulawMaxPTime.setStatus("current")
_CodecG711AlawGroup_ObjectIdentity = ObjectIdentity
codecG711AlawGroup = _CodecG711AlawGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 300, 200)
)


class _DefaultCodecG711AlawVoiceEnable_Type(MxEnableState):
    """Custom type defaultCodecG711AlawVoiceEnable based on MxEnableState"""
    defaultValue = 1


_DefaultCodecG711AlawVoiceEnable_Type.__name__ = "MxEnableState"
_DefaultCodecG711AlawVoiceEnable_Object = MibScalar
defaultCodecG711AlawVoiceEnable = _DefaultCodecG711AlawVoiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 300, 200, 100),
    _DefaultCodecG711AlawVoiceEnable_Type()
)
defaultCodecG711AlawVoiceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG711AlawVoiceEnable.setStatus("current")


class _DefaultCodecG711AlawVoicePriority_Type(Unsigned32):
    """Custom type defaultCodecG711AlawVoicePriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_DefaultCodecG711AlawVoicePriority_Type.__name__ = "Unsigned32"
_DefaultCodecG711AlawVoicePriority_Object = MibScalar
defaultCodecG711AlawVoicePriority = _DefaultCodecG711AlawVoicePriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 300, 200, 200),
    _DefaultCodecG711AlawVoicePriority_Type()
)
defaultCodecG711AlawVoicePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG711AlawVoicePriority.setStatus("current")


class _DefaultCodecG711AlawDataEnable_Type(MxEnableState):
    """Custom type defaultCodecG711AlawDataEnable based on MxEnableState"""
    defaultValue = 1


_DefaultCodecG711AlawDataEnable_Type.__name__ = "MxEnableState"
_DefaultCodecG711AlawDataEnable_Object = MibScalar
defaultCodecG711AlawDataEnable = _DefaultCodecG711AlawDataEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 300, 200, 300),
    _DefaultCodecG711AlawDataEnable_Type()
)
defaultCodecG711AlawDataEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG711AlawDataEnable.setStatus("current")


class _DefaultCodecG711AlawDataPriority_Type(Unsigned32):
    """Custom type defaultCodecG711AlawDataPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_DefaultCodecG711AlawDataPriority_Type.__name__ = "Unsigned32"
_DefaultCodecG711AlawDataPriority_Object = MibScalar
defaultCodecG711AlawDataPriority = _DefaultCodecG711AlawDataPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 300, 200, 400),
    _DefaultCodecG711AlawDataPriority_Type()
)
defaultCodecG711AlawDataPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG711AlawDataPriority.setStatus("current")


class _DefaultCodecG711AlawMinPTime_Type(Unsigned32):
    """Custom type defaultCodecG711AlawMinPTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_DefaultCodecG711AlawMinPTime_Type.__name__ = "Unsigned32"
_DefaultCodecG711AlawMinPTime_Object = MibScalar
defaultCodecG711AlawMinPTime = _DefaultCodecG711AlawMinPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 300, 200, 500),
    _DefaultCodecG711AlawMinPTime_Type()
)
defaultCodecG711AlawMinPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG711AlawMinPTime.setStatus("current")


class _DefaultCodecG711AlawMaxPTime_Type(Unsigned32):
    """Custom type defaultCodecG711AlawMaxPTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_DefaultCodecG711AlawMaxPTime_Type.__name__ = "Unsigned32"
_DefaultCodecG711AlawMaxPTime_Object = MibScalar
defaultCodecG711AlawMaxPTime = _DefaultCodecG711AlawMaxPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 300, 200, 600),
    _DefaultCodecG711AlawMaxPTime_Type()
)
defaultCodecG711AlawMaxPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG711AlawMaxPTime.setStatus("current")
_EpSpecificCodecG711AlawTable_Object = MibTable
epSpecificCodecG711AlawTable = _EpSpecificCodecG711AlawTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 300, 200, 700)
)
if mibBuilder.loadTexts:
    epSpecificCodecG711AlawTable.setStatus("current")
_EpSpecificCodecG711AlawEntry_Object = MibTableRow
epSpecificCodecG711AlawEntry = _EpSpecificCodecG711AlawEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 300, 200, 700, 1)
)
epSpecificCodecG711AlawEntry.setIndexNames(
    (0, "MX-MIPT-MIB", "epSpecificCodecG711AlawEpId"),
)
if mibBuilder.loadTexts:
    epSpecificCodecG711AlawEntry.setStatus("current")
_EpSpecificCodecG711AlawEpId_Type = OctetString
_EpSpecificCodecG711AlawEpId_Object = MibTableColumn
epSpecificCodecG711AlawEpId = _EpSpecificCodecG711AlawEpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 300, 200, 700, 1, 100),
    _EpSpecificCodecG711AlawEpId_Type()
)
epSpecificCodecG711AlawEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epSpecificCodecG711AlawEpId.setStatus("current")


class _EpSpecificCodecG711AlawEnableConfig_Type(MxEnableState):
    """Custom type epSpecificCodecG711AlawEnableConfig based on MxEnableState"""
    defaultValue = 0


_EpSpecificCodecG711AlawEnableConfig_Type.__name__ = "MxEnableState"
_EpSpecificCodecG711AlawEnableConfig_Object = MibTableColumn
epSpecificCodecG711AlawEnableConfig = _EpSpecificCodecG711AlawEnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 300, 200, 700, 1, 200),
    _EpSpecificCodecG711AlawEnableConfig_Type()
)
epSpecificCodecG711AlawEnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG711AlawEnableConfig.setStatus("current")


class _EpSpecificCodecG711AlawVoiceEnable_Type(MxEnableState):
    """Custom type epSpecificCodecG711AlawVoiceEnable based on MxEnableState"""
    defaultValue = 1


_EpSpecificCodecG711AlawVoiceEnable_Type.__name__ = "MxEnableState"
_EpSpecificCodecG711AlawVoiceEnable_Object = MibTableColumn
epSpecificCodecG711AlawVoiceEnable = _EpSpecificCodecG711AlawVoiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 300, 200, 700, 1, 300),
    _EpSpecificCodecG711AlawVoiceEnable_Type()
)
epSpecificCodecG711AlawVoiceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG711AlawVoiceEnable.setStatus("current")


class _EpSpecificCodecG711AlawVoicePriority_Type(Unsigned32):
    """Custom type epSpecificCodecG711AlawVoicePriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_EpSpecificCodecG711AlawVoicePriority_Type.__name__ = "Unsigned32"
_EpSpecificCodecG711AlawVoicePriority_Object = MibTableColumn
epSpecificCodecG711AlawVoicePriority = _EpSpecificCodecG711AlawVoicePriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 300, 200, 700, 1, 400),
    _EpSpecificCodecG711AlawVoicePriority_Type()
)
epSpecificCodecG711AlawVoicePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG711AlawVoicePriority.setStatus("current")


class _EpSpecificCodecG711AlawDataEnable_Type(MxEnableState):
    """Custom type epSpecificCodecG711AlawDataEnable based on MxEnableState"""
    defaultValue = 1


_EpSpecificCodecG711AlawDataEnable_Type.__name__ = "MxEnableState"
_EpSpecificCodecG711AlawDataEnable_Object = MibTableColumn
epSpecificCodecG711AlawDataEnable = _EpSpecificCodecG711AlawDataEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 300, 200, 700, 1, 500),
    _EpSpecificCodecG711AlawDataEnable_Type()
)
epSpecificCodecG711AlawDataEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG711AlawDataEnable.setStatus("current")


class _EpSpecificCodecG711AlawDataPriority_Type(Unsigned32):
    """Custom type epSpecificCodecG711AlawDataPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_EpSpecificCodecG711AlawDataPriority_Type.__name__ = "Unsigned32"
_EpSpecificCodecG711AlawDataPriority_Object = MibTableColumn
epSpecificCodecG711AlawDataPriority = _EpSpecificCodecG711AlawDataPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 300, 200, 700, 1, 600),
    _EpSpecificCodecG711AlawDataPriority_Type()
)
epSpecificCodecG711AlawDataPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG711AlawDataPriority.setStatus("current")


class _EpSpecificCodecG711AlawMinPTime_Type(Unsigned32):
    """Custom type epSpecificCodecG711AlawMinPTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_EpSpecificCodecG711AlawMinPTime_Type.__name__ = "Unsigned32"
_EpSpecificCodecG711AlawMinPTime_Object = MibTableColumn
epSpecificCodecG711AlawMinPTime = _EpSpecificCodecG711AlawMinPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 300, 200, 700, 1, 700),
    _EpSpecificCodecG711AlawMinPTime_Type()
)
epSpecificCodecG711AlawMinPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG711AlawMinPTime.setStatus("current")


class _EpSpecificCodecG711AlawMaxPTime_Type(Unsigned32):
    """Custom type epSpecificCodecG711AlawMaxPTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_EpSpecificCodecG711AlawMaxPTime_Type.__name__ = "Unsigned32"
_EpSpecificCodecG711AlawMaxPTime_Object = MibTableColumn
epSpecificCodecG711AlawMaxPTime = _EpSpecificCodecG711AlawMaxPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 300, 200, 700, 1, 800),
    _EpSpecificCodecG711AlawMaxPTime_Type()
)
epSpecificCodecG711AlawMaxPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG711AlawMaxPTime.setStatus("current")
_CodecG722Group_ObjectIdentity = ObjectIdentity
codecG722Group = _CodecG722Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 350)
)


class _DefaultCodecG722VoiceEnable_Type(MxEnableState):
    """Custom type defaultCodecG722VoiceEnable based on MxEnableState"""
    defaultValue = 1


_DefaultCodecG722VoiceEnable_Type.__name__ = "MxEnableState"
_DefaultCodecG722VoiceEnable_Object = MibScalar
defaultCodecG722VoiceEnable = _DefaultCodecG722VoiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 350, 100),
    _DefaultCodecG722VoiceEnable_Type()
)
defaultCodecG722VoiceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG722VoiceEnable.setStatus("current")


class _DefaultCodecG722VoicePriority_Type(Unsigned32):
    """Custom type defaultCodecG722VoicePriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_DefaultCodecG722VoicePriority_Type.__name__ = "Unsigned32"
_DefaultCodecG722VoicePriority_Object = MibScalar
defaultCodecG722VoicePriority = _DefaultCodecG722VoicePriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 350, 200),
    _DefaultCodecG722VoicePriority_Type()
)
defaultCodecG722VoicePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG722VoicePriority.setStatus("current")


class _DefaultCodecG722MinPTime_Type(Unsigned32):
    """Custom type defaultCodecG722MinPTime based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 20),
    )


_DefaultCodecG722MinPTime_Type.__name__ = "Unsigned32"
_DefaultCodecG722MinPTime_Object = MibScalar
defaultCodecG722MinPTime = _DefaultCodecG722MinPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 350, 300),
    _DefaultCodecG722MinPTime_Type()
)
defaultCodecG722MinPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG722MinPTime.setStatus("current")


class _DefaultCodecG722MaxPTime_Type(Unsigned32):
    """Custom type defaultCodecG722MaxPTime based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 20),
    )


_DefaultCodecG722MaxPTime_Type.__name__ = "Unsigned32"
_DefaultCodecG722MaxPTime_Object = MibScalar
defaultCodecG722MaxPTime = _DefaultCodecG722MaxPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 350, 400),
    _DefaultCodecG722MaxPTime_Type()
)
defaultCodecG722MaxPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG722MaxPTime.setStatus("current")
_EpSpecificCodecG722Table_Object = MibTable
epSpecificCodecG722Table = _EpSpecificCodecG722Table_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 350, 500)
)
if mibBuilder.loadTexts:
    epSpecificCodecG722Table.setStatus("current")
_EpSpecificCodecG722Entry_Object = MibTableRow
epSpecificCodecG722Entry = _EpSpecificCodecG722Entry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 350, 500, 1)
)
epSpecificCodecG722Entry.setIndexNames(
    (0, "MX-MIPT-MIB", "epSpecificCodecG722EpId"),
)
if mibBuilder.loadTexts:
    epSpecificCodecG722Entry.setStatus("current")
_EpSpecificCodecG722EpId_Type = OctetString
_EpSpecificCodecG722EpId_Object = MibTableColumn
epSpecificCodecG722EpId = _EpSpecificCodecG722EpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 350, 500, 1, 100),
    _EpSpecificCodecG722EpId_Type()
)
epSpecificCodecG722EpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epSpecificCodecG722EpId.setStatus("current")


class _EpSpecificCodecG722EnableConfig_Type(MxEnableState):
    """Custom type epSpecificCodecG722EnableConfig based on MxEnableState"""
    defaultValue = 0


_EpSpecificCodecG722EnableConfig_Type.__name__ = "MxEnableState"
_EpSpecificCodecG722EnableConfig_Object = MibTableColumn
epSpecificCodecG722EnableConfig = _EpSpecificCodecG722EnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 350, 500, 1, 200),
    _EpSpecificCodecG722EnableConfig_Type()
)
epSpecificCodecG722EnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG722EnableConfig.setStatus("current")


class _EpSpecificCodecG722VoiceEnable_Type(MxEnableState):
    """Custom type epSpecificCodecG722VoiceEnable based on MxEnableState"""
    defaultValue = 1


_EpSpecificCodecG722VoiceEnable_Type.__name__ = "MxEnableState"
_EpSpecificCodecG722VoiceEnable_Object = MibTableColumn
epSpecificCodecG722VoiceEnable = _EpSpecificCodecG722VoiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 350, 500, 1, 300),
    _EpSpecificCodecG722VoiceEnable_Type()
)
epSpecificCodecG722VoiceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG722VoiceEnable.setStatus("current")


class _EpSpecificCodecG722VoicePriority_Type(Unsigned32):
    """Custom type epSpecificCodecG722VoicePriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_EpSpecificCodecG722VoicePriority_Type.__name__ = "Unsigned32"
_EpSpecificCodecG722VoicePriority_Object = MibTableColumn
epSpecificCodecG722VoicePriority = _EpSpecificCodecG722VoicePriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 350, 500, 1, 400),
    _EpSpecificCodecG722VoicePriority_Type()
)
epSpecificCodecG722VoicePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG722VoicePriority.setStatus("current")


class _EpSpecificCodecG722MinPTime_Type(Unsigned32):
    """Custom type epSpecificCodecG722MinPTime based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 20),
    )


_EpSpecificCodecG722MinPTime_Type.__name__ = "Unsigned32"
_EpSpecificCodecG722MinPTime_Object = MibTableColumn
epSpecificCodecG722MinPTime = _EpSpecificCodecG722MinPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 350, 500, 1, 500),
    _EpSpecificCodecG722MinPTime_Type()
)
epSpecificCodecG722MinPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG722MinPTime.setStatus("current")


class _EpSpecificCodecG722MaxPTime_Type(Unsigned32):
    """Custom type epSpecificCodecG722MaxPTime based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 20),
    )


_EpSpecificCodecG722MaxPTime_Type.__name__ = "Unsigned32"
_EpSpecificCodecG722MaxPTime_Object = MibTableColumn
epSpecificCodecG722MaxPTime = _EpSpecificCodecG722MaxPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 350, 500, 1, 600),
    _EpSpecificCodecG722MaxPTime_Type()
)
epSpecificCodecG722MaxPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG722MaxPTime.setStatus("current")
_CodecG723Group_ObjectIdentity = ObjectIdentity
codecG723Group = _CodecG723Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 400)
)


class _DefaultCodecG723VoiceEnable_Type(MxEnableState):
    """Custom type defaultCodecG723VoiceEnable based on MxEnableState"""
    defaultValue = 1


_DefaultCodecG723VoiceEnable_Type.__name__ = "MxEnableState"
_DefaultCodecG723VoiceEnable_Object = MibScalar
defaultCodecG723VoiceEnable = _DefaultCodecG723VoiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 400, 100),
    _DefaultCodecG723VoiceEnable_Type()
)
defaultCodecG723VoiceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG723VoiceEnable.setStatus("current")


class _DefaultCodecG723VoicePriority_Type(Unsigned32):
    """Custom type defaultCodecG723VoicePriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_DefaultCodecG723VoicePriority_Type.__name__ = "Unsigned32"
_DefaultCodecG723VoicePriority_Object = MibScalar
defaultCodecG723VoicePriority = _DefaultCodecG723VoicePriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 400, 200),
    _DefaultCodecG723VoicePriority_Type()
)
defaultCodecG723VoicePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG723VoicePriority.setStatus("current")


class _DefaultCodecG723Bitrate_Type(Integer32):
    """Custom type defaultCodecG723Bitrate based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("rate53kbps", 100),
          ("rate63kbps", 200))
    )


_DefaultCodecG723Bitrate_Type.__name__ = "Integer32"
_DefaultCodecG723Bitrate_Object = MibScalar
defaultCodecG723Bitrate = _DefaultCodecG723Bitrate_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 400, 300),
    _DefaultCodecG723Bitrate_Type()
)
defaultCodecG723Bitrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG723Bitrate.setStatus("current")


class _DefaultCodecG723MinPTime_Type(Unsigned32):
    """Custom type defaultCodecG723MinPTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(60, 60),
    )


_DefaultCodecG723MinPTime_Type.__name__ = "Unsigned32"
_DefaultCodecG723MinPTime_Object = MibScalar
defaultCodecG723MinPTime = _DefaultCodecG723MinPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 400, 400),
    _DefaultCodecG723MinPTime_Type()
)
defaultCodecG723MinPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG723MinPTime.setStatus("current")


class _DefaultCodecG723MaxPTime_Type(Unsigned32):
    """Custom type defaultCodecG723MaxPTime based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(60, 60),
    )


_DefaultCodecG723MaxPTime_Type.__name__ = "Unsigned32"
_DefaultCodecG723MaxPTime_Object = MibScalar
defaultCodecG723MaxPTime = _DefaultCodecG723MaxPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 400, 500),
    _DefaultCodecG723MaxPTime_Type()
)
defaultCodecG723MaxPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG723MaxPTime.setStatus("current")
_EpSpecificCodecG723Table_Object = MibTable
epSpecificCodecG723Table = _EpSpecificCodecG723Table_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 400, 700)
)
if mibBuilder.loadTexts:
    epSpecificCodecG723Table.setStatus("current")
_EpSpecificCodecG723Entry_Object = MibTableRow
epSpecificCodecG723Entry = _EpSpecificCodecG723Entry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 400, 700, 1)
)
epSpecificCodecG723Entry.setIndexNames(
    (0, "MX-MIPT-MIB", "epSpecificCodecG723EpId"),
)
if mibBuilder.loadTexts:
    epSpecificCodecG723Entry.setStatus("current")
_EpSpecificCodecG723EpId_Type = OctetString
_EpSpecificCodecG723EpId_Object = MibTableColumn
epSpecificCodecG723EpId = _EpSpecificCodecG723EpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 400, 700, 1, 100),
    _EpSpecificCodecG723EpId_Type()
)
epSpecificCodecG723EpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epSpecificCodecG723EpId.setStatus("current")


class _EpSpecificCodecG723EnableConfig_Type(MxEnableState):
    """Custom type epSpecificCodecG723EnableConfig based on MxEnableState"""
    defaultValue = 0


_EpSpecificCodecG723EnableConfig_Type.__name__ = "MxEnableState"
_EpSpecificCodecG723EnableConfig_Object = MibTableColumn
epSpecificCodecG723EnableConfig = _EpSpecificCodecG723EnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 400, 700, 1, 200),
    _EpSpecificCodecG723EnableConfig_Type()
)
epSpecificCodecG723EnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG723EnableConfig.setStatus("current")


class _EpSpecificCodecG723VoiceEnable_Type(MxEnableState):
    """Custom type epSpecificCodecG723VoiceEnable based on MxEnableState"""
    defaultValue = 1


_EpSpecificCodecG723VoiceEnable_Type.__name__ = "MxEnableState"
_EpSpecificCodecG723VoiceEnable_Object = MibTableColumn
epSpecificCodecG723VoiceEnable = _EpSpecificCodecG723VoiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 400, 700, 1, 300),
    _EpSpecificCodecG723VoiceEnable_Type()
)
epSpecificCodecG723VoiceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG723VoiceEnable.setStatus("current")


class _EpSpecificCodecG723VoicePriority_Type(Unsigned32):
    """Custom type epSpecificCodecG723VoicePriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_EpSpecificCodecG723VoicePriority_Type.__name__ = "Unsigned32"
_EpSpecificCodecG723VoicePriority_Object = MibTableColumn
epSpecificCodecG723VoicePriority = _EpSpecificCodecG723VoicePriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 400, 700, 1, 400),
    _EpSpecificCodecG723VoicePriority_Type()
)
epSpecificCodecG723VoicePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG723VoicePriority.setStatus("current")


class _EpSpecificCodecG723Bitrate_Type(Integer32):
    """Custom type epSpecificCodecG723Bitrate based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("rate53kbps", 100),
          ("rate63kbps", 200))
    )


_EpSpecificCodecG723Bitrate_Type.__name__ = "Integer32"
_EpSpecificCodecG723Bitrate_Object = MibTableColumn
epSpecificCodecG723Bitrate = _EpSpecificCodecG723Bitrate_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 400, 700, 1, 500),
    _EpSpecificCodecG723Bitrate_Type()
)
epSpecificCodecG723Bitrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG723Bitrate.setStatus("current")


class _EpSpecificCodecG723MinPTime_Type(Unsigned32):
    """Custom type epSpecificCodecG723MinPTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(60, 60),
    )


_EpSpecificCodecG723MinPTime_Type.__name__ = "Unsigned32"
_EpSpecificCodecG723MinPTime_Object = MibTableColumn
epSpecificCodecG723MinPTime = _EpSpecificCodecG723MinPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 400, 700, 1, 600),
    _EpSpecificCodecG723MinPTime_Type()
)
epSpecificCodecG723MinPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG723MinPTime.setStatus("current")


class _EpSpecificCodecG723MaxPTime_Type(Unsigned32):
    """Custom type epSpecificCodecG723MaxPTime based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(60, 60),
    )


_EpSpecificCodecG723MaxPTime_Type.__name__ = "Unsigned32"
_EpSpecificCodecG723MaxPTime_Object = MibTableColumn
epSpecificCodecG723MaxPTime = _EpSpecificCodecG723MaxPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 400, 700, 1, 700),
    _EpSpecificCodecG723MaxPTime_Type()
)
epSpecificCodecG723MaxPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG723MaxPTime.setStatus("current")
_CodecG726Group_ObjectIdentity = ObjectIdentity
codecG726Group = _CodecG726Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500)
)
_CodecG726r16kbpsGroup_ObjectIdentity = ObjectIdentity
codecG726r16kbpsGroup = _CodecG726r16kbpsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 100)
)


class _DefaultCodecG726r16kbpsVoiceEnable_Type(MxEnableState):
    """Custom type defaultCodecG726r16kbpsVoiceEnable based on MxEnableState"""
    defaultValue = 0


_DefaultCodecG726r16kbpsVoiceEnable_Type.__name__ = "MxEnableState"
_DefaultCodecG726r16kbpsVoiceEnable_Object = MibScalar
defaultCodecG726r16kbpsVoiceEnable = _DefaultCodecG726r16kbpsVoiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 100, 100),
    _DefaultCodecG726r16kbpsVoiceEnable_Type()
)
defaultCodecG726r16kbpsVoiceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG726r16kbpsVoiceEnable.setStatus("current")


class _DefaultCodecG726r16kbpsVoicePriority_Type(Unsigned32):
    """Custom type defaultCodecG726r16kbpsVoicePriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_DefaultCodecG726r16kbpsVoicePriority_Type.__name__ = "Unsigned32"
_DefaultCodecG726r16kbpsVoicePriority_Object = MibScalar
defaultCodecG726r16kbpsVoicePriority = _DefaultCodecG726r16kbpsVoicePriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 100, 200),
    _DefaultCodecG726r16kbpsVoicePriority_Type()
)
defaultCodecG726r16kbpsVoicePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG726r16kbpsVoicePriority.setStatus("current")


class _DefaultCodecG726r16kbpsPayloadType_Type(Unsigned32):
    """Custom type defaultCodecG726r16kbpsPayloadType based on Unsigned32"""
    defaultValue = 97

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(96, 127),
    )


_DefaultCodecG726r16kbpsPayloadType_Type.__name__ = "Unsigned32"
_DefaultCodecG726r16kbpsPayloadType_Object = MibScalar
defaultCodecG726r16kbpsPayloadType = _DefaultCodecG726r16kbpsPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 100, 300),
    _DefaultCodecG726r16kbpsPayloadType_Type()
)
defaultCodecG726r16kbpsPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG726r16kbpsPayloadType.setStatus("current")


class _DefaultCodecG726r16kbpsMinPTime_Type(Unsigned32):
    """Custom type defaultCodecG726r16kbpsMinPTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_DefaultCodecG726r16kbpsMinPTime_Type.__name__ = "Unsigned32"
_DefaultCodecG726r16kbpsMinPTime_Object = MibScalar
defaultCodecG726r16kbpsMinPTime = _DefaultCodecG726r16kbpsMinPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 100, 400),
    _DefaultCodecG726r16kbpsMinPTime_Type()
)
defaultCodecG726r16kbpsMinPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG726r16kbpsMinPTime.setStatus("current")


class _DefaultCodecG726r16kbpsMaxPTime_Type(Unsigned32):
    """Custom type defaultCodecG726r16kbpsMaxPTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_DefaultCodecG726r16kbpsMaxPTime_Type.__name__ = "Unsigned32"
_DefaultCodecG726r16kbpsMaxPTime_Object = MibScalar
defaultCodecG726r16kbpsMaxPTime = _DefaultCodecG726r16kbpsMaxPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 100, 500),
    _DefaultCodecG726r16kbpsMaxPTime_Type()
)
defaultCodecG726r16kbpsMaxPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG726r16kbpsMaxPTime.setStatus("current")
_EpSpecificCodecG726r16kbpsTable_Object = MibTable
epSpecificCodecG726r16kbpsTable = _EpSpecificCodecG726r16kbpsTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 100, 600)
)
if mibBuilder.loadTexts:
    epSpecificCodecG726r16kbpsTable.setStatus("current")
_EpSpecificCodecG726r16kbpsEntry_Object = MibTableRow
epSpecificCodecG726r16kbpsEntry = _EpSpecificCodecG726r16kbpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 100, 600, 1)
)
epSpecificCodecG726r16kbpsEntry.setIndexNames(
    (0, "MX-MIPT-MIB", "epSpecificCodecG726r16kbpsEpId"),
)
if mibBuilder.loadTexts:
    epSpecificCodecG726r16kbpsEntry.setStatus("current")
_EpSpecificCodecG726r16kbpsEpId_Type = OctetString
_EpSpecificCodecG726r16kbpsEpId_Object = MibTableColumn
epSpecificCodecG726r16kbpsEpId = _EpSpecificCodecG726r16kbpsEpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 100, 600, 1, 100),
    _EpSpecificCodecG726r16kbpsEpId_Type()
)
epSpecificCodecG726r16kbpsEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epSpecificCodecG726r16kbpsEpId.setStatus("current")


class _EpSpecificCodecG726r16kbpsEnableConfig_Type(MxEnableState):
    """Custom type epSpecificCodecG726r16kbpsEnableConfig based on MxEnableState"""
    defaultValue = 0


_EpSpecificCodecG726r16kbpsEnableConfig_Type.__name__ = "MxEnableState"
_EpSpecificCodecG726r16kbpsEnableConfig_Object = MibTableColumn
epSpecificCodecG726r16kbpsEnableConfig = _EpSpecificCodecG726r16kbpsEnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 100, 600, 1, 200),
    _EpSpecificCodecG726r16kbpsEnableConfig_Type()
)
epSpecificCodecG726r16kbpsEnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG726r16kbpsEnableConfig.setStatus("current")


class _EpSpecificCodecG726r16kbpsVoiceEnable_Type(MxEnableState):
    """Custom type epSpecificCodecG726r16kbpsVoiceEnable based on MxEnableState"""
    defaultValue = 0


_EpSpecificCodecG726r16kbpsVoiceEnable_Type.__name__ = "MxEnableState"
_EpSpecificCodecG726r16kbpsVoiceEnable_Object = MibTableColumn
epSpecificCodecG726r16kbpsVoiceEnable = _EpSpecificCodecG726r16kbpsVoiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 100, 600, 1, 300),
    _EpSpecificCodecG726r16kbpsVoiceEnable_Type()
)
epSpecificCodecG726r16kbpsVoiceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG726r16kbpsVoiceEnable.setStatus("current")


class _EpSpecificCodecG726r16kbpsVoicePriority_Type(Unsigned32):
    """Custom type epSpecificCodecG726r16kbpsVoicePriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_EpSpecificCodecG726r16kbpsVoicePriority_Type.__name__ = "Unsigned32"
_EpSpecificCodecG726r16kbpsVoicePriority_Object = MibTableColumn
epSpecificCodecG726r16kbpsVoicePriority = _EpSpecificCodecG726r16kbpsVoicePriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 100, 600, 1, 400),
    _EpSpecificCodecG726r16kbpsVoicePriority_Type()
)
epSpecificCodecG726r16kbpsVoicePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG726r16kbpsVoicePriority.setStatus("current")


class _EpSpecificCodecG726r16kbpsPayloadType_Type(Unsigned32):
    """Custom type epSpecificCodecG726r16kbpsPayloadType based on Unsigned32"""
    defaultValue = 97

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(96, 127),
    )


_EpSpecificCodecG726r16kbpsPayloadType_Type.__name__ = "Unsigned32"
_EpSpecificCodecG726r16kbpsPayloadType_Object = MibTableColumn
epSpecificCodecG726r16kbpsPayloadType = _EpSpecificCodecG726r16kbpsPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 100, 600, 1, 500),
    _EpSpecificCodecG726r16kbpsPayloadType_Type()
)
epSpecificCodecG726r16kbpsPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG726r16kbpsPayloadType.setStatus("current")


class _EpSpecificCodecG726r16kbpsMinPTime_Type(Unsigned32):
    """Custom type epSpecificCodecG726r16kbpsMinPTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_EpSpecificCodecG726r16kbpsMinPTime_Type.__name__ = "Unsigned32"
_EpSpecificCodecG726r16kbpsMinPTime_Object = MibTableColumn
epSpecificCodecG726r16kbpsMinPTime = _EpSpecificCodecG726r16kbpsMinPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 100, 600, 1, 600),
    _EpSpecificCodecG726r16kbpsMinPTime_Type()
)
epSpecificCodecG726r16kbpsMinPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG726r16kbpsMinPTime.setStatus("current")


class _EpSpecificCodecG726r16kbpsMaxPTime_Type(Unsigned32):
    """Custom type epSpecificCodecG726r16kbpsMaxPTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_EpSpecificCodecG726r16kbpsMaxPTime_Type.__name__ = "Unsigned32"
_EpSpecificCodecG726r16kbpsMaxPTime_Object = MibTableColumn
epSpecificCodecG726r16kbpsMaxPTime = _EpSpecificCodecG726r16kbpsMaxPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 100, 600, 1, 700),
    _EpSpecificCodecG726r16kbpsMaxPTime_Type()
)
epSpecificCodecG726r16kbpsMaxPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG726r16kbpsMaxPTime.setStatus("current")
_CodecG726r24kbpsGroup_ObjectIdentity = ObjectIdentity
codecG726r24kbpsGroup = _CodecG726r24kbpsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 200)
)


class _DefaultCodecG726r24kbpsVoiceEnable_Type(MxEnableState):
    """Custom type defaultCodecG726r24kbpsVoiceEnable based on MxEnableState"""
    defaultValue = 0


_DefaultCodecG726r24kbpsVoiceEnable_Type.__name__ = "MxEnableState"
_DefaultCodecG726r24kbpsVoiceEnable_Object = MibScalar
defaultCodecG726r24kbpsVoiceEnable = _DefaultCodecG726r24kbpsVoiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 200, 100),
    _DefaultCodecG726r24kbpsVoiceEnable_Type()
)
defaultCodecG726r24kbpsVoiceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG726r24kbpsVoiceEnable.setStatus("current")


class _DefaultCodecG726r24kbpsVoicePriority_Type(Unsigned32):
    """Custom type defaultCodecG726r24kbpsVoicePriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_DefaultCodecG726r24kbpsVoicePriority_Type.__name__ = "Unsigned32"
_DefaultCodecG726r24kbpsVoicePriority_Object = MibScalar
defaultCodecG726r24kbpsVoicePriority = _DefaultCodecG726r24kbpsVoicePriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 200, 200),
    _DefaultCodecG726r24kbpsVoicePriority_Type()
)
defaultCodecG726r24kbpsVoicePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG726r24kbpsVoicePriority.setStatus("current")


class _DefaultCodecG726r24kbpsPayloadType_Type(Unsigned32):
    """Custom type defaultCodecG726r24kbpsPayloadType based on Unsigned32"""
    defaultValue = 98

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(96, 127),
    )


_DefaultCodecG726r24kbpsPayloadType_Type.__name__ = "Unsigned32"
_DefaultCodecG726r24kbpsPayloadType_Object = MibScalar
defaultCodecG726r24kbpsPayloadType = _DefaultCodecG726r24kbpsPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 200, 300),
    _DefaultCodecG726r24kbpsPayloadType_Type()
)
defaultCodecG726r24kbpsPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG726r24kbpsPayloadType.setStatus("current")


class _DefaultCodecG726r24kbpsMinPTime_Type(Unsigned32):
    """Custom type defaultCodecG726r24kbpsMinPTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_DefaultCodecG726r24kbpsMinPTime_Type.__name__ = "Unsigned32"
_DefaultCodecG726r24kbpsMinPTime_Object = MibScalar
defaultCodecG726r24kbpsMinPTime = _DefaultCodecG726r24kbpsMinPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 200, 400),
    _DefaultCodecG726r24kbpsMinPTime_Type()
)
defaultCodecG726r24kbpsMinPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG726r24kbpsMinPTime.setStatus("current")


class _DefaultCodecG726r24kbpsMaxPTime_Type(Unsigned32):
    """Custom type defaultCodecG726r24kbpsMaxPTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_DefaultCodecG726r24kbpsMaxPTime_Type.__name__ = "Unsigned32"
_DefaultCodecG726r24kbpsMaxPTime_Object = MibScalar
defaultCodecG726r24kbpsMaxPTime = _DefaultCodecG726r24kbpsMaxPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 200, 500),
    _DefaultCodecG726r24kbpsMaxPTime_Type()
)
defaultCodecG726r24kbpsMaxPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG726r24kbpsMaxPTime.setStatus("current")
_EpSpecificCodecG726r24kbpsTable_Object = MibTable
epSpecificCodecG726r24kbpsTable = _EpSpecificCodecG726r24kbpsTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 200, 600)
)
if mibBuilder.loadTexts:
    epSpecificCodecG726r24kbpsTable.setStatus("current")
_EpSpecificCodecG726r24kbpsEntry_Object = MibTableRow
epSpecificCodecG726r24kbpsEntry = _EpSpecificCodecG726r24kbpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 200, 600, 1)
)
epSpecificCodecG726r24kbpsEntry.setIndexNames(
    (0, "MX-MIPT-MIB", "epSpecificCodecG726r24kbpsEpId"),
)
if mibBuilder.loadTexts:
    epSpecificCodecG726r24kbpsEntry.setStatus("current")
_EpSpecificCodecG726r24kbpsEpId_Type = OctetString
_EpSpecificCodecG726r24kbpsEpId_Object = MibTableColumn
epSpecificCodecG726r24kbpsEpId = _EpSpecificCodecG726r24kbpsEpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 200, 600, 1, 100),
    _EpSpecificCodecG726r24kbpsEpId_Type()
)
epSpecificCodecG726r24kbpsEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epSpecificCodecG726r24kbpsEpId.setStatus("current")


class _EpSpecificCodecG726r24kbpsEnableConfig_Type(MxEnableState):
    """Custom type epSpecificCodecG726r24kbpsEnableConfig based on MxEnableState"""
    defaultValue = 0


_EpSpecificCodecG726r24kbpsEnableConfig_Type.__name__ = "MxEnableState"
_EpSpecificCodecG726r24kbpsEnableConfig_Object = MibTableColumn
epSpecificCodecG726r24kbpsEnableConfig = _EpSpecificCodecG726r24kbpsEnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 200, 600, 1, 200),
    _EpSpecificCodecG726r24kbpsEnableConfig_Type()
)
epSpecificCodecG726r24kbpsEnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG726r24kbpsEnableConfig.setStatus("current")


class _EpSpecificCodecG726r24kbpsVoiceEnable_Type(MxEnableState):
    """Custom type epSpecificCodecG726r24kbpsVoiceEnable based on MxEnableState"""
    defaultValue = 0


_EpSpecificCodecG726r24kbpsVoiceEnable_Type.__name__ = "MxEnableState"
_EpSpecificCodecG726r24kbpsVoiceEnable_Object = MibTableColumn
epSpecificCodecG726r24kbpsVoiceEnable = _EpSpecificCodecG726r24kbpsVoiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 200, 600, 1, 300),
    _EpSpecificCodecG726r24kbpsVoiceEnable_Type()
)
epSpecificCodecG726r24kbpsVoiceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG726r24kbpsVoiceEnable.setStatus("current")


class _EpSpecificCodecG726r24kbpsVoicePriority_Type(Unsigned32):
    """Custom type epSpecificCodecG726r24kbpsVoicePriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_EpSpecificCodecG726r24kbpsVoicePriority_Type.__name__ = "Unsigned32"
_EpSpecificCodecG726r24kbpsVoicePriority_Object = MibTableColumn
epSpecificCodecG726r24kbpsVoicePriority = _EpSpecificCodecG726r24kbpsVoicePriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 200, 600, 1, 400),
    _EpSpecificCodecG726r24kbpsVoicePriority_Type()
)
epSpecificCodecG726r24kbpsVoicePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG726r24kbpsVoicePriority.setStatus("current")


class _EpSpecificCodecG726r24kbpsPayloadType_Type(Unsigned32):
    """Custom type epSpecificCodecG726r24kbpsPayloadType based on Unsigned32"""
    defaultValue = 98

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(96, 127),
    )


_EpSpecificCodecG726r24kbpsPayloadType_Type.__name__ = "Unsigned32"
_EpSpecificCodecG726r24kbpsPayloadType_Object = MibTableColumn
epSpecificCodecG726r24kbpsPayloadType = _EpSpecificCodecG726r24kbpsPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 200, 600, 1, 500),
    _EpSpecificCodecG726r24kbpsPayloadType_Type()
)
epSpecificCodecG726r24kbpsPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG726r24kbpsPayloadType.setStatus("current")


class _EpSpecificCodecG726r24kbpsMinPTime_Type(Unsigned32):
    """Custom type epSpecificCodecG726r24kbpsMinPTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_EpSpecificCodecG726r24kbpsMinPTime_Type.__name__ = "Unsigned32"
_EpSpecificCodecG726r24kbpsMinPTime_Object = MibTableColumn
epSpecificCodecG726r24kbpsMinPTime = _EpSpecificCodecG726r24kbpsMinPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 200, 600, 1, 600),
    _EpSpecificCodecG726r24kbpsMinPTime_Type()
)
epSpecificCodecG726r24kbpsMinPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG726r24kbpsMinPTime.setStatus("current")


class _EpSpecificCodecG726r24kbpsMaxPTime_Type(Unsigned32):
    """Custom type epSpecificCodecG726r24kbpsMaxPTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_EpSpecificCodecG726r24kbpsMaxPTime_Type.__name__ = "Unsigned32"
_EpSpecificCodecG726r24kbpsMaxPTime_Object = MibTableColumn
epSpecificCodecG726r24kbpsMaxPTime = _EpSpecificCodecG726r24kbpsMaxPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 200, 600, 1, 700),
    _EpSpecificCodecG726r24kbpsMaxPTime_Type()
)
epSpecificCodecG726r24kbpsMaxPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG726r24kbpsMaxPTime.setStatus("current")
_CodecG726r32kbpsGroup_ObjectIdentity = ObjectIdentity
codecG726r32kbpsGroup = _CodecG726r32kbpsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 300)
)


class _DefaultCodecG726r32kbpsVoiceEnable_Type(MxEnableState):
    """Custom type defaultCodecG726r32kbpsVoiceEnable based on MxEnableState"""
    defaultValue = 0


_DefaultCodecG726r32kbpsVoiceEnable_Type.__name__ = "MxEnableState"
_DefaultCodecG726r32kbpsVoiceEnable_Object = MibScalar
defaultCodecG726r32kbpsVoiceEnable = _DefaultCodecG726r32kbpsVoiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 300, 100),
    _DefaultCodecG726r32kbpsVoiceEnable_Type()
)
defaultCodecG726r32kbpsVoiceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG726r32kbpsVoiceEnable.setStatus("current")


class _DefaultCodecG726r32kbpsVoicePriority_Type(Unsigned32):
    """Custom type defaultCodecG726r32kbpsVoicePriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_DefaultCodecG726r32kbpsVoicePriority_Type.__name__ = "Unsigned32"
_DefaultCodecG726r32kbpsVoicePriority_Object = MibScalar
defaultCodecG726r32kbpsVoicePriority = _DefaultCodecG726r32kbpsVoicePriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 300, 200),
    _DefaultCodecG726r32kbpsVoicePriority_Type()
)
defaultCodecG726r32kbpsVoicePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG726r32kbpsVoicePriority.setStatus("current")


class _DefaultCodecG726r32kbpsDataEnable_Type(MxEnableState):
    """Custom type defaultCodecG726r32kbpsDataEnable based on MxEnableState"""
    defaultValue = 0


_DefaultCodecG726r32kbpsDataEnable_Type.__name__ = "MxEnableState"
_DefaultCodecG726r32kbpsDataEnable_Object = MibScalar
defaultCodecG726r32kbpsDataEnable = _DefaultCodecG726r32kbpsDataEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 300, 300),
    _DefaultCodecG726r32kbpsDataEnable_Type()
)
defaultCodecG726r32kbpsDataEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG726r32kbpsDataEnable.setStatus("current")


class _DefaultCodecG726r32kbpsDataPriority_Type(Unsigned32):
    """Custom type defaultCodecG726r32kbpsDataPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_DefaultCodecG726r32kbpsDataPriority_Type.__name__ = "Unsigned32"
_DefaultCodecG726r32kbpsDataPriority_Object = MibScalar
defaultCodecG726r32kbpsDataPriority = _DefaultCodecG726r32kbpsDataPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 300, 400),
    _DefaultCodecG726r32kbpsDataPriority_Type()
)
defaultCodecG726r32kbpsDataPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG726r32kbpsDataPriority.setStatus("current")


class _DefaultCodecG726r32kbpsPayloadType_Type(Unsigned32):
    """Custom type defaultCodecG726r32kbpsPayloadType based on Unsigned32"""
    defaultValue = 99

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(96, 127),
    )


_DefaultCodecG726r32kbpsPayloadType_Type.__name__ = "Unsigned32"
_DefaultCodecG726r32kbpsPayloadType_Object = MibScalar
defaultCodecG726r32kbpsPayloadType = _DefaultCodecG726r32kbpsPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 300, 500),
    _DefaultCodecG726r32kbpsPayloadType_Type()
)
defaultCodecG726r32kbpsPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG726r32kbpsPayloadType.setStatus("current")


class _DefaultCodecG726r32kbpsMinPTime_Type(Unsigned32):
    """Custom type defaultCodecG726r32kbpsMinPTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_DefaultCodecG726r32kbpsMinPTime_Type.__name__ = "Unsigned32"
_DefaultCodecG726r32kbpsMinPTime_Object = MibScalar
defaultCodecG726r32kbpsMinPTime = _DefaultCodecG726r32kbpsMinPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 300, 600),
    _DefaultCodecG726r32kbpsMinPTime_Type()
)
defaultCodecG726r32kbpsMinPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG726r32kbpsMinPTime.setStatus("current")


class _DefaultCodecG726r32kbpsMaxPTime_Type(Unsigned32):
    """Custom type defaultCodecG726r32kbpsMaxPTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_DefaultCodecG726r32kbpsMaxPTime_Type.__name__ = "Unsigned32"
_DefaultCodecG726r32kbpsMaxPTime_Object = MibScalar
defaultCodecG726r32kbpsMaxPTime = _DefaultCodecG726r32kbpsMaxPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 300, 700),
    _DefaultCodecG726r32kbpsMaxPTime_Type()
)
defaultCodecG726r32kbpsMaxPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG726r32kbpsMaxPTime.setStatus("current")
_EpSpecificCodecG726r32kbpsTable_Object = MibTable
epSpecificCodecG726r32kbpsTable = _EpSpecificCodecG726r32kbpsTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 300, 800)
)
if mibBuilder.loadTexts:
    epSpecificCodecG726r32kbpsTable.setStatus("current")
_EpSpecificCodecG726r32kbpsEntry_Object = MibTableRow
epSpecificCodecG726r32kbpsEntry = _EpSpecificCodecG726r32kbpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 300, 800, 1)
)
epSpecificCodecG726r32kbpsEntry.setIndexNames(
    (0, "MX-MIPT-MIB", "epSpecificCodecG726r32kbpsEpId"),
)
if mibBuilder.loadTexts:
    epSpecificCodecG726r32kbpsEntry.setStatus("current")
_EpSpecificCodecG726r32kbpsEpId_Type = OctetString
_EpSpecificCodecG726r32kbpsEpId_Object = MibTableColumn
epSpecificCodecG726r32kbpsEpId = _EpSpecificCodecG726r32kbpsEpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 300, 800, 1, 100),
    _EpSpecificCodecG726r32kbpsEpId_Type()
)
epSpecificCodecG726r32kbpsEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epSpecificCodecG726r32kbpsEpId.setStatus("current")


class _EpSpecificCodecG726r32kbpsEnableConfig_Type(MxEnableState):
    """Custom type epSpecificCodecG726r32kbpsEnableConfig based on MxEnableState"""
    defaultValue = 0


_EpSpecificCodecG726r32kbpsEnableConfig_Type.__name__ = "MxEnableState"
_EpSpecificCodecG726r32kbpsEnableConfig_Object = MibTableColumn
epSpecificCodecG726r32kbpsEnableConfig = _EpSpecificCodecG726r32kbpsEnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 300, 800, 1, 200),
    _EpSpecificCodecG726r32kbpsEnableConfig_Type()
)
epSpecificCodecG726r32kbpsEnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG726r32kbpsEnableConfig.setStatus("current")


class _EpSpecificCodecG726r32kbpsVoiceEnable_Type(MxEnableState):
    """Custom type epSpecificCodecG726r32kbpsVoiceEnable based on MxEnableState"""
    defaultValue = 0


_EpSpecificCodecG726r32kbpsVoiceEnable_Type.__name__ = "MxEnableState"
_EpSpecificCodecG726r32kbpsVoiceEnable_Object = MibTableColumn
epSpecificCodecG726r32kbpsVoiceEnable = _EpSpecificCodecG726r32kbpsVoiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 300, 800, 1, 300),
    _EpSpecificCodecG726r32kbpsVoiceEnable_Type()
)
epSpecificCodecG726r32kbpsVoiceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG726r32kbpsVoiceEnable.setStatus("current")


class _EpSpecificCodecG726r32kbpsVoicePriority_Type(Unsigned32):
    """Custom type epSpecificCodecG726r32kbpsVoicePriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_EpSpecificCodecG726r32kbpsVoicePriority_Type.__name__ = "Unsigned32"
_EpSpecificCodecG726r32kbpsVoicePriority_Object = MibTableColumn
epSpecificCodecG726r32kbpsVoicePriority = _EpSpecificCodecG726r32kbpsVoicePriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 300, 800, 1, 400),
    _EpSpecificCodecG726r32kbpsVoicePriority_Type()
)
epSpecificCodecG726r32kbpsVoicePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG726r32kbpsVoicePriority.setStatus("current")


class _EpSpecificCodecG726r32kbpsDataEnable_Type(MxEnableState):
    """Custom type epSpecificCodecG726r32kbpsDataEnable based on MxEnableState"""
    defaultValue = 0


_EpSpecificCodecG726r32kbpsDataEnable_Type.__name__ = "MxEnableState"
_EpSpecificCodecG726r32kbpsDataEnable_Object = MibTableColumn
epSpecificCodecG726r32kbpsDataEnable = _EpSpecificCodecG726r32kbpsDataEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 300, 800, 1, 500),
    _EpSpecificCodecG726r32kbpsDataEnable_Type()
)
epSpecificCodecG726r32kbpsDataEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG726r32kbpsDataEnable.setStatus("current")


class _EpSpecificCodecG726r32kbpsDataPriority_Type(Unsigned32):
    """Custom type epSpecificCodecG726r32kbpsDataPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_EpSpecificCodecG726r32kbpsDataPriority_Type.__name__ = "Unsigned32"
_EpSpecificCodecG726r32kbpsDataPriority_Object = MibTableColumn
epSpecificCodecG726r32kbpsDataPriority = _EpSpecificCodecG726r32kbpsDataPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 300, 800, 1, 600),
    _EpSpecificCodecG726r32kbpsDataPriority_Type()
)
epSpecificCodecG726r32kbpsDataPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG726r32kbpsDataPriority.setStatus("current")


class _EpSpecificCodecG726r32kbpsPayloadType_Type(Unsigned32):
    """Custom type epSpecificCodecG726r32kbpsPayloadType based on Unsigned32"""
    defaultValue = 99

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(96, 127),
    )


_EpSpecificCodecG726r32kbpsPayloadType_Type.__name__ = "Unsigned32"
_EpSpecificCodecG726r32kbpsPayloadType_Object = MibTableColumn
epSpecificCodecG726r32kbpsPayloadType = _EpSpecificCodecG726r32kbpsPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 300, 800, 1, 700),
    _EpSpecificCodecG726r32kbpsPayloadType_Type()
)
epSpecificCodecG726r32kbpsPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG726r32kbpsPayloadType.setStatus("current")


class _EpSpecificCodecG726r32kbpsMinPTime_Type(Unsigned32):
    """Custom type epSpecificCodecG726r32kbpsMinPTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_EpSpecificCodecG726r32kbpsMinPTime_Type.__name__ = "Unsigned32"
_EpSpecificCodecG726r32kbpsMinPTime_Object = MibTableColumn
epSpecificCodecG726r32kbpsMinPTime = _EpSpecificCodecG726r32kbpsMinPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 300, 800, 1, 800),
    _EpSpecificCodecG726r32kbpsMinPTime_Type()
)
epSpecificCodecG726r32kbpsMinPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG726r32kbpsMinPTime.setStatus("current")


class _EpSpecificCodecG726r32kbpsMaxPTime_Type(Unsigned32):
    """Custom type epSpecificCodecG726r32kbpsMaxPTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_EpSpecificCodecG726r32kbpsMaxPTime_Type.__name__ = "Unsigned32"
_EpSpecificCodecG726r32kbpsMaxPTime_Object = MibTableColumn
epSpecificCodecG726r32kbpsMaxPTime = _EpSpecificCodecG726r32kbpsMaxPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 300, 800, 1, 900),
    _EpSpecificCodecG726r32kbpsMaxPTime_Type()
)
epSpecificCodecG726r32kbpsMaxPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG726r32kbpsMaxPTime.setStatus("current")
_CodecG726r40kbpsGroup_ObjectIdentity = ObjectIdentity
codecG726r40kbpsGroup = _CodecG726r40kbpsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 400)
)


class _DefaultCodecG726r40kbpsVoiceEnable_Type(MxEnableState):
    """Custom type defaultCodecG726r40kbpsVoiceEnable based on MxEnableState"""
    defaultValue = 0


_DefaultCodecG726r40kbpsVoiceEnable_Type.__name__ = "MxEnableState"
_DefaultCodecG726r40kbpsVoiceEnable_Object = MibScalar
defaultCodecG726r40kbpsVoiceEnable = _DefaultCodecG726r40kbpsVoiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 400, 100),
    _DefaultCodecG726r40kbpsVoiceEnable_Type()
)
defaultCodecG726r40kbpsVoiceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG726r40kbpsVoiceEnable.setStatus("current")


class _DefaultCodecG726r40kbpsVoicePriority_Type(Unsigned32):
    """Custom type defaultCodecG726r40kbpsVoicePriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_DefaultCodecG726r40kbpsVoicePriority_Type.__name__ = "Unsigned32"
_DefaultCodecG726r40kbpsVoicePriority_Object = MibScalar
defaultCodecG726r40kbpsVoicePriority = _DefaultCodecG726r40kbpsVoicePriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 400, 200),
    _DefaultCodecG726r40kbpsVoicePriority_Type()
)
defaultCodecG726r40kbpsVoicePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG726r40kbpsVoicePriority.setStatus("current")


class _DefaultCodecG726r40kbpsDataEnable_Type(MxEnableState):
    """Custom type defaultCodecG726r40kbpsDataEnable based on MxEnableState"""
    defaultValue = 0


_DefaultCodecG726r40kbpsDataEnable_Type.__name__ = "MxEnableState"
_DefaultCodecG726r40kbpsDataEnable_Object = MibScalar
defaultCodecG726r40kbpsDataEnable = _DefaultCodecG726r40kbpsDataEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 400, 300),
    _DefaultCodecG726r40kbpsDataEnable_Type()
)
defaultCodecG726r40kbpsDataEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG726r40kbpsDataEnable.setStatus("current")


class _DefaultCodecG726r40kbpsDataPriority_Type(Unsigned32):
    """Custom type defaultCodecG726r40kbpsDataPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_DefaultCodecG726r40kbpsDataPriority_Type.__name__ = "Unsigned32"
_DefaultCodecG726r40kbpsDataPriority_Object = MibScalar
defaultCodecG726r40kbpsDataPriority = _DefaultCodecG726r40kbpsDataPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 400, 400),
    _DefaultCodecG726r40kbpsDataPriority_Type()
)
defaultCodecG726r40kbpsDataPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG726r40kbpsDataPriority.setStatus("current")


class _DefaultCodecG726r40kbpsPayloadType_Type(Unsigned32):
    """Custom type defaultCodecG726r40kbpsPayloadType based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(96, 127),
    )


_DefaultCodecG726r40kbpsPayloadType_Type.__name__ = "Unsigned32"
_DefaultCodecG726r40kbpsPayloadType_Object = MibScalar
defaultCodecG726r40kbpsPayloadType = _DefaultCodecG726r40kbpsPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 400, 500),
    _DefaultCodecG726r40kbpsPayloadType_Type()
)
defaultCodecG726r40kbpsPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG726r40kbpsPayloadType.setStatus("current")


class _DefaultCodecG726r40kbpsMinPTime_Type(Unsigned32):
    """Custom type defaultCodecG726r40kbpsMinPTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_DefaultCodecG726r40kbpsMinPTime_Type.__name__ = "Unsigned32"
_DefaultCodecG726r40kbpsMinPTime_Object = MibScalar
defaultCodecG726r40kbpsMinPTime = _DefaultCodecG726r40kbpsMinPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 400, 600),
    _DefaultCodecG726r40kbpsMinPTime_Type()
)
defaultCodecG726r40kbpsMinPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG726r40kbpsMinPTime.setStatus("current")


class _DefaultCodecG726r40kbpsMaxPTime_Type(Unsigned32):
    """Custom type defaultCodecG726r40kbpsMaxPTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_DefaultCodecG726r40kbpsMaxPTime_Type.__name__ = "Unsigned32"
_DefaultCodecG726r40kbpsMaxPTime_Object = MibScalar
defaultCodecG726r40kbpsMaxPTime = _DefaultCodecG726r40kbpsMaxPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 400, 700),
    _DefaultCodecG726r40kbpsMaxPTime_Type()
)
defaultCodecG726r40kbpsMaxPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG726r40kbpsMaxPTime.setStatus("current")
_EpSpecificCodecG726r40kbpsTable_Object = MibTable
epSpecificCodecG726r40kbpsTable = _EpSpecificCodecG726r40kbpsTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 400, 800)
)
if mibBuilder.loadTexts:
    epSpecificCodecG726r40kbpsTable.setStatus("current")
_EpSpecificCodecG726r40kbpsEntry_Object = MibTableRow
epSpecificCodecG726r40kbpsEntry = _EpSpecificCodecG726r40kbpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 400, 800, 1)
)
epSpecificCodecG726r40kbpsEntry.setIndexNames(
    (0, "MX-MIPT-MIB", "epSpecificCodecG726r40kbpsEpId"),
)
if mibBuilder.loadTexts:
    epSpecificCodecG726r40kbpsEntry.setStatus("current")
_EpSpecificCodecG726r40kbpsEpId_Type = OctetString
_EpSpecificCodecG726r40kbpsEpId_Object = MibTableColumn
epSpecificCodecG726r40kbpsEpId = _EpSpecificCodecG726r40kbpsEpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 400, 800, 1, 100),
    _EpSpecificCodecG726r40kbpsEpId_Type()
)
epSpecificCodecG726r40kbpsEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epSpecificCodecG726r40kbpsEpId.setStatus("current")


class _EpSpecificCodecG726r40kbpsEnableConfig_Type(MxEnableState):
    """Custom type epSpecificCodecG726r40kbpsEnableConfig based on MxEnableState"""
    defaultValue = 0


_EpSpecificCodecG726r40kbpsEnableConfig_Type.__name__ = "MxEnableState"
_EpSpecificCodecG726r40kbpsEnableConfig_Object = MibTableColumn
epSpecificCodecG726r40kbpsEnableConfig = _EpSpecificCodecG726r40kbpsEnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 400, 800, 1, 200),
    _EpSpecificCodecG726r40kbpsEnableConfig_Type()
)
epSpecificCodecG726r40kbpsEnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG726r40kbpsEnableConfig.setStatus("current")


class _EpSpecificCodecG726r40kbpsVoiceEnable_Type(MxEnableState):
    """Custom type epSpecificCodecG726r40kbpsVoiceEnable based on MxEnableState"""
    defaultValue = 0


_EpSpecificCodecG726r40kbpsVoiceEnable_Type.__name__ = "MxEnableState"
_EpSpecificCodecG726r40kbpsVoiceEnable_Object = MibTableColumn
epSpecificCodecG726r40kbpsVoiceEnable = _EpSpecificCodecG726r40kbpsVoiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 400, 800, 1, 300),
    _EpSpecificCodecG726r40kbpsVoiceEnable_Type()
)
epSpecificCodecG726r40kbpsVoiceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG726r40kbpsVoiceEnable.setStatus("current")


class _EpSpecificCodecG726r40kbpsVoicePriority_Type(Unsigned32):
    """Custom type epSpecificCodecG726r40kbpsVoicePriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_EpSpecificCodecG726r40kbpsVoicePriority_Type.__name__ = "Unsigned32"
_EpSpecificCodecG726r40kbpsVoicePriority_Object = MibTableColumn
epSpecificCodecG726r40kbpsVoicePriority = _EpSpecificCodecG726r40kbpsVoicePriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 400, 800, 1, 400),
    _EpSpecificCodecG726r40kbpsVoicePriority_Type()
)
epSpecificCodecG726r40kbpsVoicePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG726r40kbpsVoicePriority.setStatus("current")


class _EpSpecificCodecG726r40kbpsDataEnable_Type(MxEnableState):
    """Custom type epSpecificCodecG726r40kbpsDataEnable based on MxEnableState"""
    defaultValue = 0


_EpSpecificCodecG726r40kbpsDataEnable_Type.__name__ = "MxEnableState"
_EpSpecificCodecG726r40kbpsDataEnable_Object = MibTableColumn
epSpecificCodecG726r40kbpsDataEnable = _EpSpecificCodecG726r40kbpsDataEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 400, 800, 1, 500),
    _EpSpecificCodecG726r40kbpsDataEnable_Type()
)
epSpecificCodecG726r40kbpsDataEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG726r40kbpsDataEnable.setStatus("current")


class _EpSpecificCodecG726r40kbpsDataPriority_Type(Unsigned32):
    """Custom type epSpecificCodecG726r40kbpsDataPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_EpSpecificCodecG726r40kbpsDataPriority_Type.__name__ = "Unsigned32"
_EpSpecificCodecG726r40kbpsDataPriority_Object = MibTableColumn
epSpecificCodecG726r40kbpsDataPriority = _EpSpecificCodecG726r40kbpsDataPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 400, 800, 1, 600),
    _EpSpecificCodecG726r40kbpsDataPriority_Type()
)
epSpecificCodecG726r40kbpsDataPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG726r40kbpsDataPriority.setStatus("current")


class _EpSpecificCodecG726r40kbpsPayloadType_Type(Unsigned32):
    """Custom type epSpecificCodecG726r40kbpsPayloadType based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(96, 127),
    )


_EpSpecificCodecG726r40kbpsPayloadType_Type.__name__ = "Unsigned32"
_EpSpecificCodecG726r40kbpsPayloadType_Object = MibTableColumn
epSpecificCodecG726r40kbpsPayloadType = _EpSpecificCodecG726r40kbpsPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 400, 800, 1, 700),
    _EpSpecificCodecG726r40kbpsPayloadType_Type()
)
epSpecificCodecG726r40kbpsPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG726r40kbpsPayloadType.setStatus("current")


class _EpSpecificCodecG726r40kbpsMinPTime_Type(Unsigned32):
    """Custom type epSpecificCodecG726r40kbpsMinPTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_EpSpecificCodecG726r40kbpsMinPTime_Type.__name__ = "Unsigned32"
_EpSpecificCodecG726r40kbpsMinPTime_Object = MibTableColumn
epSpecificCodecG726r40kbpsMinPTime = _EpSpecificCodecG726r40kbpsMinPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 400, 800, 1, 800),
    _EpSpecificCodecG726r40kbpsMinPTime_Type()
)
epSpecificCodecG726r40kbpsMinPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG726r40kbpsMinPTime.setStatus("current")


class _EpSpecificCodecG726r40kbpsMaxPTime_Type(Unsigned32):
    """Custom type epSpecificCodecG726r40kbpsMaxPTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_EpSpecificCodecG726r40kbpsMaxPTime_Type.__name__ = "Unsigned32"
_EpSpecificCodecG726r40kbpsMaxPTime_Object = MibTableColumn
epSpecificCodecG726r40kbpsMaxPTime = _EpSpecificCodecG726r40kbpsMaxPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 500, 400, 800, 1, 900),
    _EpSpecificCodecG726r40kbpsMaxPTime_Type()
)
epSpecificCodecG726r40kbpsMaxPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG726r40kbpsMaxPTime.setStatus("current")
_CodecG729Group_ObjectIdentity = ObjectIdentity
codecG729Group = _CodecG729Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 600)
)


class _DefaultCodecG729VoiceEnable_Type(MxEnableState):
    """Custom type defaultCodecG729VoiceEnable based on MxEnableState"""
    defaultValue = 1


_DefaultCodecG729VoiceEnable_Type.__name__ = "MxEnableState"
_DefaultCodecG729VoiceEnable_Object = MibScalar
defaultCodecG729VoiceEnable = _DefaultCodecG729VoiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 600, 100),
    _DefaultCodecG729VoiceEnable_Type()
)
defaultCodecG729VoiceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG729VoiceEnable.setStatus("current")


class _DefaultCodecG729VoicePriority_Type(Unsigned32):
    """Custom type defaultCodecG729VoicePriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_DefaultCodecG729VoicePriority_Type.__name__ = "Unsigned32"
_DefaultCodecG729VoicePriority_Object = MibScalar
defaultCodecG729VoicePriority = _DefaultCodecG729VoicePriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 600, 200),
    _DefaultCodecG729VoicePriority_Type()
)
defaultCodecG729VoicePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG729VoicePriority.setStatus("current")


class _DefaultCodecG729MinPTime_Type(Unsigned32):
    """Custom type defaultCodecG729MinPTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(70, 70),
        ValueRangeConstraint(80, 80),
    )


_DefaultCodecG729MinPTime_Type.__name__ = "Unsigned32"
_DefaultCodecG729MinPTime_Object = MibScalar
defaultCodecG729MinPTime = _DefaultCodecG729MinPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 600, 300),
    _DefaultCodecG729MinPTime_Type()
)
defaultCodecG729MinPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG729MinPTime.setStatus("current")


class _DefaultCodecG729MaxPTime_Type(Unsigned32):
    """Custom type defaultCodecG729MaxPTime based on Unsigned32"""
    defaultValue = 80

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(70, 70),
        ValueRangeConstraint(80, 80),
    )


_DefaultCodecG729MaxPTime_Type.__name__ = "Unsigned32"
_DefaultCodecG729MaxPTime_Object = MibScalar
defaultCodecG729MaxPTime = _DefaultCodecG729MaxPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 600, 400),
    _DefaultCodecG729MaxPTime_Type()
)
defaultCodecG729MaxPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG729MaxPTime.setStatus("current")


class _DefaultCodecG729VoiceActivityDetection_Type(MxEnableState):
    """Custom type defaultCodecG729VoiceActivityDetection based on MxEnableState"""
    defaultValue = 1


_DefaultCodecG729VoiceActivityDetection_Type.__name__ = "MxEnableState"
_DefaultCodecG729VoiceActivityDetection_Object = MibScalar
defaultCodecG729VoiceActivityDetection = _DefaultCodecG729VoiceActivityDetection_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 600, 500),
    _DefaultCodecG729VoiceActivityDetection_Type()
)
defaultCodecG729VoiceActivityDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecG729VoiceActivityDetection.setStatus("current")
_EpSpecificCodecG729Table_Object = MibTable
epSpecificCodecG729Table = _EpSpecificCodecG729Table_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 600, 600)
)
if mibBuilder.loadTexts:
    epSpecificCodecG729Table.setStatus("current")
_EpSpecificCodecG729Entry_Object = MibTableRow
epSpecificCodecG729Entry = _EpSpecificCodecG729Entry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 600, 600, 1)
)
epSpecificCodecG729Entry.setIndexNames(
    (0, "MX-MIPT-MIB", "epSpecificCodecG729EpId"),
)
if mibBuilder.loadTexts:
    epSpecificCodecG729Entry.setStatus("current")
_EpSpecificCodecG729EpId_Type = OctetString
_EpSpecificCodecG729EpId_Object = MibTableColumn
epSpecificCodecG729EpId = _EpSpecificCodecG729EpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 600, 600, 1, 100),
    _EpSpecificCodecG729EpId_Type()
)
epSpecificCodecG729EpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epSpecificCodecG729EpId.setStatus("current")


class _EpSpecificCodecG729EnableConfig_Type(MxEnableState):
    """Custom type epSpecificCodecG729EnableConfig based on MxEnableState"""
    defaultValue = 0


_EpSpecificCodecG729EnableConfig_Type.__name__ = "MxEnableState"
_EpSpecificCodecG729EnableConfig_Object = MibTableColumn
epSpecificCodecG729EnableConfig = _EpSpecificCodecG729EnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 600, 600, 1, 200),
    _EpSpecificCodecG729EnableConfig_Type()
)
epSpecificCodecG729EnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG729EnableConfig.setStatus("current")


class _EpSpecificCodecG729VoiceEnable_Type(MxEnableState):
    """Custom type epSpecificCodecG729VoiceEnable based on MxEnableState"""
    defaultValue = 1


_EpSpecificCodecG729VoiceEnable_Type.__name__ = "MxEnableState"
_EpSpecificCodecG729VoiceEnable_Object = MibTableColumn
epSpecificCodecG729VoiceEnable = _EpSpecificCodecG729VoiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 600, 600, 1, 300),
    _EpSpecificCodecG729VoiceEnable_Type()
)
epSpecificCodecG729VoiceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG729VoiceEnable.setStatus("current")


class _EpSpecificCodecG729VoicePriority_Type(Unsigned32):
    """Custom type epSpecificCodecG729VoicePriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_EpSpecificCodecG729VoicePriority_Type.__name__ = "Unsigned32"
_EpSpecificCodecG729VoicePriority_Object = MibTableColumn
epSpecificCodecG729VoicePriority = _EpSpecificCodecG729VoicePriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 600, 600, 1, 400),
    _EpSpecificCodecG729VoicePriority_Type()
)
epSpecificCodecG729VoicePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG729VoicePriority.setStatus("current")


class _EpSpecificCodecG729MinPTime_Type(Unsigned32):
    """Custom type epSpecificCodecG729MinPTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(70, 70),
        ValueRangeConstraint(80, 80),
    )


_EpSpecificCodecG729MinPTime_Type.__name__ = "Unsigned32"
_EpSpecificCodecG729MinPTime_Object = MibTableColumn
epSpecificCodecG729MinPTime = _EpSpecificCodecG729MinPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 600, 600, 1, 500),
    _EpSpecificCodecG729MinPTime_Type()
)
epSpecificCodecG729MinPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG729MinPTime.setStatus("current")


class _EpSpecificCodecG729MaxPTime_Type(Unsigned32):
    """Custom type epSpecificCodecG729MaxPTime based on Unsigned32"""
    defaultValue = 80

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(70, 70),
        ValueRangeConstraint(80, 80),
    )


_EpSpecificCodecG729MaxPTime_Type.__name__ = "Unsigned32"
_EpSpecificCodecG729MaxPTime_Object = MibTableColumn
epSpecificCodecG729MaxPTime = _EpSpecificCodecG729MaxPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 600, 600, 1, 600),
    _EpSpecificCodecG729MaxPTime_Type()
)
epSpecificCodecG729MaxPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG729MaxPTime.setStatus("current")


class _EpSpecificCodecG729VoiceActivityDetection_Type(MxEnableState):
    """Custom type epSpecificCodecG729VoiceActivityDetection based on MxEnableState"""
    defaultValue = 1


_EpSpecificCodecG729VoiceActivityDetection_Type.__name__ = "MxEnableState"
_EpSpecificCodecG729VoiceActivityDetection_Object = MibTableColumn
epSpecificCodecG729VoiceActivityDetection = _EpSpecificCodecG729VoiceActivityDetection_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 600, 600, 1, 700),
    _EpSpecificCodecG729VoiceActivityDetection_Type()
)
epSpecificCodecG729VoiceActivityDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecG729VoiceActivityDetection.setStatus("current")
_CodecT38Group_ObjectIdentity = ObjectIdentity
codecT38Group = _CodecT38Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 700)
)


class _DefaultCodecT38DataEnable_Type(MxEnableState):
    """Custom type defaultCodecT38DataEnable based on MxEnableState"""
    defaultValue = 1


_DefaultCodecT38DataEnable_Type.__name__ = "MxEnableState"
_DefaultCodecT38DataEnable_Object = MibScalar
defaultCodecT38DataEnable = _DefaultCodecT38DataEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 700, 100),
    _DefaultCodecT38DataEnable_Type()
)
defaultCodecT38DataEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecT38DataEnable.setStatus("current")


class _DefaultCodecT38DataPriority_Type(Unsigned32):
    """Custom type defaultCodecT38DataPriority based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
    )


_DefaultCodecT38DataPriority_Type.__name__ = "Unsigned32"
_DefaultCodecT38DataPriority_Object = MibScalar
defaultCodecT38DataPriority = _DefaultCodecT38DataPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 700, 200),
    _DefaultCodecT38DataPriority_Type()
)
defaultCodecT38DataPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecT38DataPriority.setStatus("current")


class _DefaultCodecT38RedundancyLevel_Type(Unsigned32):
    """Custom type defaultCodecT38RedundancyLevel based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_DefaultCodecT38RedundancyLevel_Type.__name__ = "Unsigned32"
_DefaultCodecT38RedundancyLevel_Object = MibScalar
defaultCodecT38RedundancyLevel = _DefaultCodecT38RedundancyLevel_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 700, 400),
    _DefaultCodecT38RedundancyLevel_Type()
)
defaultCodecT38RedundancyLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecT38RedundancyLevel.setStatus("current")


class _DefaultCodecT38FinalFramesRedundancy_Type(Unsigned32):
    """Custom type defaultCodecT38FinalFramesRedundancy based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_DefaultCodecT38FinalFramesRedundancy_Type.__name__ = "Unsigned32"
_DefaultCodecT38FinalFramesRedundancy_Object = MibScalar
defaultCodecT38FinalFramesRedundancy = _DefaultCodecT38FinalFramesRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 700, 500),
    _DefaultCodecT38FinalFramesRedundancy_Type()
)
defaultCodecT38FinalFramesRedundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecT38FinalFramesRedundancy.setStatus("current")


class _DefaultCodecT38NoSignalEnable_Type(MxEnableState):
    """Custom type defaultCodecT38NoSignalEnable based on MxEnableState"""
    defaultValue = 0


_DefaultCodecT38NoSignalEnable_Type.__name__ = "MxEnableState"
_DefaultCodecT38NoSignalEnable_Object = MibScalar
defaultCodecT38NoSignalEnable = _DefaultCodecT38NoSignalEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 700, 600),
    _DefaultCodecT38NoSignalEnable_Type()
)
defaultCodecT38NoSignalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecT38NoSignalEnable.setStatus("current")


class _DefaultCodecT38NoSignalTimeout_Type(Unsigned32):
    """Custom type defaultCodecT38NoSignalTimeout based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DefaultCodecT38NoSignalTimeout_Type.__name__ = "Unsigned32"
_DefaultCodecT38NoSignalTimeout_Object = MibScalar
defaultCodecT38NoSignalTimeout = _DefaultCodecT38NoSignalTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 700, 700),
    _DefaultCodecT38NoSignalTimeout_Type()
)
defaultCodecT38NoSignalTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecT38NoSignalTimeout.setStatus("current")


class _DefaultCodecT38DetectionThreshold_Type(Integer32):
    """Custom type defaultCodecT38DetectionThreshold based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300)
        )
    )
    namedValues = NamedValues(
        *(("default", 100),
          ("low", 200),
          ("lowest", 300))
    )


_DefaultCodecT38DetectionThreshold_Type.__name__ = "Integer32"
_DefaultCodecT38DetectionThreshold_Object = MibScalar
defaultCodecT38DetectionThreshold = _DefaultCodecT38DetectionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 700, 750),
    _DefaultCodecT38DetectionThreshold_Type()
)
defaultCodecT38DetectionThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecT38DetectionThreshold.setStatus("current")
_EpSpecificCodecT38Table_Object = MibTable
epSpecificCodecT38Table = _EpSpecificCodecT38Table_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 700, 800)
)
if mibBuilder.loadTexts:
    epSpecificCodecT38Table.setStatus("current")
_EpSpecificCodecT38Entry_Object = MibTableRow
epSpecificCodecT38Entry = _EpSpecificCodecT38Entry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 700, 800, 1)
)
epSpecificCodecT38Entry.setIndexNames(
    (0, "MX-MIPT-MIB", "epSpecificCodecT38EpId"),
)
if mibBuilder.loadTexts:
    epSpecificCodecT38Entry.setStatus("current")
_EpSpecificCodecT38EpId_Type = OctetString
_EpSpecificCodecT38EpId_Object = MibTableColumn
epSpecificCodecT38EpId = _EpSpecificCodecT38EpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 700, 800, 1, 100),
    _EpSpecificCodecT38EpId_Type()
)
epSpecificCodecT38EpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epSpecificCodecT38EpId.setStatus("current")


class _EpSpecificCodecT38EnableConfig_Type(MxEnableState):
    """Custom type epSpecificCodecT38EnableConfig based on MxEnableState"""
    defaultValue = 0


_EpSpecificCodecT38EnableConfig_Type.__name__ = "MxEnableState"
_EpSpecificCodecT38EnableConfig_Object = MibTableColumn
epSpecificCodecT38EnableConfig = _EpSpecificCodecT38EnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 700, 800, 1, 200),
    _EpSpecificCodecT38EnableConfig_Type()
)
epSpecificCodecT38EnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecT38EnableConfig.setStatus("current")


class _EpSpecificCodecT38DataEnable_Type(MxEnableState):
    """Custom type epSpecificCodecT38DataEnable based on MxEnableState"""
    defaultValue = 1


_EpSpecificCodecT38DataEnable_Type.__name__ = "MxEnableState"
_EpSpecificCodecT38DataEnable_Object = MibTableColumn
epSpecificCodecT38DataEnable = _EpSpecificCodecT38DataEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 700, 800, 1, 300),
    _EpSpecificCodecT38DataEnable_Type()
)
epSpecificCodecT38DataEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecT38DataEnable.setStatus("current")


class _EpSpecificCodecT38DataPriority_Type(Unsigned32):
    """Custom type epSpecificCodecT38DataPriority based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
    )


_EpSpecificCodecT38DataPriority_Type.__name__ = "Unsigned32"
_EpSpecificCodecT38DataPriority_Object = MibTableColumn
epSpecificCodecT38DataPriority = _EpSpecificCodecT38DataPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 700, 800, 1, 400),
    _EpSpecificCodecT38DataPriority_Type()
)
epSpecificCodecT38DataPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecT38DataPriority.setStatus("current")


class _EpSpecificCodecT38RedundancyLevel_Type(Unsigned32):
    """Custom type epSpecificCodecT38RedundancyLevel based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_EpSpecificCodecT38RedundancyLevel_Type.__name__ = "Unsigned32"
_EpSpecificCodecT38RedundancyLevel_Object = MibTableColumn
epSpecificCodecT38RedundancyLevel = _EpSpecificCodecT38RedundancyLevel_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 700, 800, 1, 600),
    _EpSpecificCodecT38RedundancyLevel_Type()
)
epSpecificCodecT38RedundancyLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecT38RedundancyLevel.setStatus("current")


class _EpSpecificCodecT38DetectionThreshold_Type(Integer32):
    """Custom type epSpecificCodecT38DetectionThreshold based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300)
        )
    )
    namedValues = NamedValues(
        *(("default", 100),
          ("low", 200),
          ("lowest", 300))
    )


_EpSpecificCodecT38DetectionThreshold_Type.__name__ = "Integer32"
_EpSpecificCodecT38DetectionThreshold_Object = MibTableColumn
epSpecificCodecT38DetectionThreshold = _EpSpecificCodecT38DetectionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 700, 800, 1, 700),
    _EpSpecificCodecT38DetectionThreshold_Type()
)
epSpecificCodecT38DetectionThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecT38DetectionThreshold.setStatus("current")
_CodecClearModeGroup_ObjectIdentity = ObjectIdentity
codecClearModeGroup = _CodecClearModeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 800)
)


class _DefaultCodecClearModeVoiceEnable_Type(MxEnableState):
    """Custom type defaultCodecClearModeVoiceEnable based on MxEnableState"""
    defaultValue = 0


_DefaultCodecClearModeVoiceEnable_Type.__name__ = "MxEnableState"
_DefaultCodecClearModeVoiceEnable_Object = MibScalar
defaultCodecClearModeVoiceEnable = _DefaultCodecClearModeVoiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 800, 100),
    _DefaultCodecClearModeVoiceEnable_Type()
)
defaultCodecClearModeVoiceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecClearModeVoiceEnable.setStatus("current")


class _DefaultCodecClearModeVoicePriority_Type(Unsigned32):
    """Custom type defaultCodecClearModeVoicePriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_DefaultCodecClearModeVoicePriority_Type.__name__ = "Unsigned32"
_DefaultCodecClearModeVoicePriority_Object = MibScalar
defaultCodecClearModeVoicePriority = _DefaultCodecClearModeVoicePriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 800, 200),
    _DefaultCodecClearModeVoicePriority_Type()
)
defaultCodecClearModeVoicePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecClearModeVoicePriority.setStatus("current")


class _DefaultCodecClearModeDataEnable_Type(MxEnableState):
    """Custom type defaultCodecClearModeDataEnable based on MxEnableState"""
    defaultValue = 0


_DefaultCodecClearModeDataEnable_Type.__name__ = "MxEnableState"
_DefaultCodecClearModeDataEnable_Object = MibScalar
defaultCodecClearModeDataEnable = _DefaultCodecClearModeDataEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 800, 300),
    _DefaultCodecClearModeDataEnable_Type()
)
defaultCodecClearModeDataEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecClearModeDataEnable.setStatus("current")


class _DefaultCodecClearModeDataPriority_Type(Unsigned32):
    """Custom type defaultCodecClearModeDataPriority based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_DefaultCodecClearModeDataPriority_Type.__name__ = "Unsigned32"
_DefaultCodecClearModeDataPriority_Object = MibScalar
defaultCodecClearModeDataPriority = _DefaultCodecClearModeDataPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 800, 400),
    _DefaultCodecClearModeDataPriority_Type()
)
defaultCodecClearModeDataPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecClearModeDataPriority.setStatus("current")


class _DefaultCodecClearModePayloadType_Type(Unsigned32):
    """Custom type defaultCodecClearModePayloadType based on Unsigned32"""
    defaultValue = 124

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(96, 127),
    )


_DefaultCodecClearModePayloadType_Type.__name__ = "Unsigned32"
_DefaultCodecClearModePayloadType_Object = MibScalar
defaultCodecClearModePayloadType = _DefaultCodecClearModePayloadType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 800, 500),
    _DefaultCodecClearModePayloadType_Type()
)
defaultCodecClearModePayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecClearModePayloadType.setStatus("current")


class _DefaultCodecClearModeMinPTime_Type(Unsigned32):
    """Custom type defaultCodecClearModeMinPTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_DefaultCodecClearModeMinPTime_Type.__name__ = "Unsigned32"
_DefaultCodecClearModeMinPTime_Object = MibScalar
defaultCodecClearModeMinPTime = _DefaultCodecClearModeMinPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 800, 600),
    _DefaultCodecClearModeMinPTime_Type()
)
defaultCodecClearModeMinPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecClearModeMinPTime.setStatus("current")


class _DefaultCodecClearModeMaxPTime_Type(Unsigned32):
    """Custom type defaultCodecClearModeMaxPTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_DefaultCodecClearModeMaxPTime_Type.__name__ = "Unsigned32"
_DefaultCodecClearModeMaxPTime_Object = MibScalar
defaultCodecClearModeMaxPTime = _DefaultCodecClearModeMaxPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 800, 700),
    _DefaultCodecClearModeMaxPTime_Type()
)
defaultCodecClearModeMaxPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecClearModeMaxPTime.setStatus("current")
_EpSpecificCodecClearModeTable_Object = MibTable
epSpecificCodecClearModeTable = _EpSpecificCodecClearModeTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 800, 800)
)
if mibBuilder.loadTexts:
    epSpecificCodecClearModeTable.setStatus("current")
_EpSpecificCodecClearModeEntry_Object = MibTableRow
epSpecificCodecClearModeEntry = _EpSpecificCodecClearModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 800, 800, 1)
)
epSpecificCodecClearModeEntry.setIndexNames(
    (0, "MX-MIPT-MIB", "epSpecificCodecClearModeEpId"),
)
if mibBuilder.loadTexts:
    epSpecificCodecClearModeEntry.setStatus("current")
_EpSpecificCodecClearModeEpId_Type = OctetString
_EpSpecificCodecClearModeEpId_Object = MibTableColumn
epSpecificCodecClearModeEpId = _EpSpecificCodecClearModeEpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 800, 800, 1, 100),
    _EpSpecificCodecClearModeEpId_Type()
)
epSpecificCodecClearModeEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epSpecificCodecClearModeEpId.setStatus("current")


class _EpSpecificCodecClearModeEnableConfig_Type(MxEnableState):
    """Custom type epSpecificCodecClearModeEnableConfig based on MxEnableState"""
    defaultValue = 0


_EpSpecificCodecClearModeEnableConfig_Type.__name__ = "MxEnableState"
_EpSpecificCodecClearModeEnableConfig_Object = MibTableColumn
epSpecificCodecClearModeEnableConfig = _EpSpecificCodecClearModeEnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 800, 800, 1, 200),
    _EpSpecificCodecClearModeEnableConfig_Type()
)
epSpecificCodecClearModeEnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecClearModeEnableConfig.setStatus("current")


class _EpSpecificCodecClearModeVoiceEnable_Type(MxEnableState):
    """Custom type epSpecificCodecClearModeVoiceEnable based on MxEnableState"""
    defaultValue = 0


_EpSpecificCodecClearModeVoiceEnable_Type.__name__ = "MxEnableState"
_EpSpecificCodecClearModeVoiceEnable_Object = MibTableColumn
epSpecificCodecClearModeVoiceEnable = _EpSpecificCodecClearModeVoiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 800, 800, 1, 300),
    _EpSpecificCodecClearModeVoiceEnable_Type()
)
epSpecificCodecClearModeVoiceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecClearModeVoiceEnable.setStatus("current")


class _EpSpecificCodecClearModeVoicePriority_Type(Unsigned32):
    """Custom type epSpecificCodecClearModeVoicePriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_EpSpecificCodecClearModeVoicePriority_Type.__name__ = "Unsigned32"
_EpSpecificCodecClearModeVoicePriority_Object = MibTableColumn
epSpecificCodecClearModeVoicePriority = _EpSpecificCodecClearModeVoicePriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 800, 800, 1, 400),
    _EpSpecificCodecClearModeVoicePriority_Type()
)
epSpecificCodecClearModeVoicePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecClearModeVoicePriority.setStatus("current")


class _EpSpecificCodecClearModeDataEnable_Type(MxEnableState):
    """Custom type epSpecificCodecClearModeDataEnable based on MxEnableState"""
    defaultValue = 0


_EpSpecificCodecClearModeDataEnable_Type.__name__ = "MxEnableState"
_EpSpecificCodecClearModeDataEnable_Object = MibTableColumn
epSpecificCodecClearModeDataEnable = _EpSpecificCodecClearModeDataEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 800, 800, 1, 500),
    _EpSpecificCodecClearModeDataEnable_Type()
)
epSpecificCodecClearModeDataEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecClearModeDataEnable.setStatus("current")


class _EpSpecificCodecClearModeDataPriority_Type(Unsigned32):
    """Custom type epSpecificCodecClearModeDataPriority based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_EpSpecificCodecClearModeDataPriority_Type.__name__ = "Unsigned32"
_EpSpecificCodecClearModeDataPriority_Object = MibTableColumn
epSpecificCodecClearModeDataPriority = _EpSpecificCodecClearModeDataPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 800, 800, 1, 600),
    _EpSpecificCodecClearModeDataPriority_Type()
)
epSpecificCodecClearModeDataPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecClearModeDataPriority.setStatus("current")


class _EpSpecificCodecClearModePayloadType_Type(Unsigned32):
    """Custom type epSpecificCodecClearModePayloadType based on Unsigned32"""
    defaultValue = 124

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(96, 127),
    )


_EpSpecificCodecClearModePayloadType_Type.__name__ = "Unsigned32"
_EpSpecificCodecClearModePayloadType_Object = MibTableColumn
epSpecificCodecClearModePayloadType = _EpSpecificCodecClearModePayloadType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 800, 800, 1, 700),
    _EpSpecificCodecClearModePayloadType_Type()
)
epSpecificCodecClearModePayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecClearModePayloadType.setStatus("current")


class _EpSpecificCodecClearModeMinPTime_Type(Unsigned32):
    """Custom type epSpecificCodecClearModeMinPTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_EpSpecificCodecClearModeMinPTime_Type.__name__ = "Unsigned32"
_EpSpecificCodecClearModeMinPTime_Object = MibTableColumn
epSpecificCodecClearModeMinPTime = _EpSpecificCodecClearModeMinPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 800, 800, 1, 800),
    _EpSpecificCodecClearModeMinPTime_Type()
)
epSpecificCodecClearModeMinPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecClearModeMinPTime.setStatus("current")


class _EpSpecificCodecClearModeMaxPTime_Type(Unsigned32):
    """Custom type epSpecificCodecClearModeMaxPTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_EpSpecificCodecClearModeMaxPTime_Type.__name__ = "Unsigned32"
_EpSpecificCodecClearModeMaxPTime_Object = MibTableColumn
epSpecificCodecClearModeMaxPTime = _EpSpecificCodecClearModeMaxPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 800, 800, 1, 900),
    _EpSpecificCodecClearModeMaxPTime_Type()
)
epSpecificCodecClearModeMaxPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecClearModeMaxPTime.setStatus("current")
_CodecClearChannelGroup_ObjectIdentity = ObjectIdentity
codecClearChannelGroup = _CodecClearChannelGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 900)
)


class _DefaultCodecClearChannelVoiceEnable_Type(MxEnableState):
    """Custom type defaultCodecClearChannelVoiceEnable based on MxEnableState"""
    defaultValue = 0


_DefaultCodecClearChannelVoiceEnable_Type.__name__ = "MxEnableState"
_DefaultCodecClearChannelVoiceEnable_Object = MibScalar
defaultCodecClearChannelVoiceEnable = _DefaultCodecClearChannelVoiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 900, 100),
    _DefaultCodecClearChannelVoiceEnable_Type()
)
defaultCodecClearChannelVoiceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecClearChannelVoiceEnable.setStatus("current")


class _DefaultCodecClearChannelVoicePriority_Type(Unsigned32):
    """Custom type defaultCodecClearChannelVoicePriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_DefaultCodecClearChannelVoicePriority_Type.__name__ = "Unsigned32"
_DefaultCodecClearChannelVoicePriority_Object = MibScalar
defaultCodecClearChannelVoicePriority = _DefaultCodecClearChannelVoicePriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 900, 200),
    _DefaultCodecClearChannelVoicePriority_Type()
)
defaultCodecClearChannelVoicePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecClearChannelVoicePriority.setStatus("current")


class _DefaultCodecClearChannelDataEnable_Type(MxEnableState):
    """Custom type defaultCodecClearChannelDataEnable based on MxEnableState"""
    defaultValue = 0


_DefaultCodecClearChannelDataEnable_Type.__name__ = "MxEnableState"
_DefaultCodecClearChannelDataEnable_Object = MibScalar
defaultCodecClearChannelDataEnable = _DefaultCodecClearChannelDataEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 900, 300),
    _DefaultCodecClearChannelDataEnable_Type()
)
defaultCodecClearChannelDataEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecClearChannelDataEnable.setStatus("current")


class _DefaultCodecClearChannelDataPriority_Type(Unsigned32):
    """Custom type defaultCodecClearChannelDataPriority based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_DefaultCodecClearChannelDataPriority_Type.__name__ = "Unsigned32"
_DefaultCodecClearChannelDataPriority_Object = MibScalar
defaultCodecClearChannelDataPriority = _DefaultCodecClearChannelDataPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 900, 400),
    _DefaultCodecClearChannelDataPriority_Type()
)
defaultCodecClearChannelDataPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecClearChannelDataPriority.setStatus("current")


class _DefaultCodecClearChannelPayloadType_Type(Unsigned32):
    """Custom type defaultCodecClearChannelPayloadType based on Unsigned32"""
    defaultValue = 125

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(96, 127),
    )


_DefaultCodecClearChannelPayloadType_Type.__name__ = "Unsigned32"
_DefaultCodecClearChannelPayloadType_Object = MibScalar
defaultCodecClearChannelPayloadType = _DefaultCodecClearChannelPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 900, 500),
    _DefaultCodecClearChannelPayloadType_Type()
)
defaultCodecClearChannelPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecClearChannelPayloadType.setStatus("current")


class _DefaultCodecClearChannelMinPTime_Type(Unsigned32):
    """Custom type defaultCodecClearChannelMinPTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_DefaultCodecClearChannelMinPTime_Type.__name__ = "Unsigned32"
_DefaultCodecClearChannelMinPTime_Object = MibScalar
defaultCodecClearChannelMinPTime = _DefaultCodecClearChannelMinPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 900, 600),
    _DefaultCodecClearChannelMinPTime_Type()
)
defaultCodecClearChannelMinPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecClearChannelMinPTime.setStatus("current")


class _DefaultCodecClearChannelMaxPTime_Type(Unsigned32):
    """Custom type defaultCodecClearChannelMaxPTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_DefaultCodecClearChannelMaxPTime_Type.__name__ = "Unsigned32"
_DefaultCodecClearChannelMaxPTime_Object = MibScalar
defaultCodecClearChannelMaxPTime = _DefaultCodecClearChannelMaxPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 900, 700),
    _DefaultCodecClearChannelMaxPTime_Type()
)
defaultCodecClearChannelMaxPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecClearChannelMaxPTime.setStatus("current")
_EpSpecificCodecClearChannelTable_Object = MibTable
epSpecificCodecClearChannelTable = _EpSpecificCodecClearChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 900, 800)
)
if mibBuilder.loadTexts:
    epSpecificCodecClearChannelTable.setStatus("current")
_EpSpecificCodecClearChannelEntry_Object = MibTableRow
epSpecificCodecClearChannelEntry = _EpSpecificCodecClearChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 900, 800, 1)
)
epSpecificCodecClearChannelEntry.setIndexNames(
    (0, "MX-MIPT-MIB", "epSpecificCodecClearChannelEpId"),
)
if mibBuilder.loadTexts:
    epSpecificCodecClearChannelEntry.setStatus("current")
_EpSpecificCodecClearChannelEpId_Type = OctetString
_EpSpecificCodecClearChannelEpId_Object = MibTableColumn
epSpecificCodecClearChannelEpId = _EpSpecificCodecClearChannelEpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 900, 800, 1, 100),
    _EpSpecificCodecClearChannelEpId_Type()
)
epSpecificCodecClearChannelEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epSpecificCodecClearChannelEpId.setStatus("current")


class _EpSpecificCodecClearChannelEnableConfig_Type(MxEnableState):
    """Custom type epSpecificCodecClearChannelEnableConfig based on MxEnableState"""
    defaultValue = 0


_EpSpecificCodecClearChannelEnableConfig_Type.__name__ = "MxEnableState"
_EpSpecificCodecClearChannelEnableConfig_Object = MibTableColumn
epSpecificCodecClearChannelEnableConfig = _EpSpecificCodecClearChannelEnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 900, 800, 1, 200),
    _EpSpecificCodecClearChannelEnableConfig_Type()
)
epSpecificCodecClearChannelEnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecClearChannelEnableConfig.setStatus("current")


class _EpSpecificCodecClearChannelVoiceEnable_Type(MxEnableState):
    """Custom type epSpecificCodecClearChannelVoiceEnable based on MxEnableState"""
    defaultValue = 0


_EpSpecificCodecClearChannelVoiceEnable_Type.__name__ = "MxEnableState"
_EpSpecificCodecClearChannelVoiceEnable_Object = MibTableColumn
epSpecificCodecClearChannelVoiceEnable = _EpSpecificCodecClearChannelVoiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 900, 800, 1, 300),
    _EpSpecificCodecClearChannelVoiceEnable_Type()
)
epSpecificCodecClearChannelVoiceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecClearChannelVoiceEnable.setStatus("current")


class _EpSpecificCodecClearChannelVoicePriority_Type(Unsigned32):
    """Custom type epSpecificCodecClearChannelVoicePriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_EpSpecificCodecClearChannelVoicePriority_Type.__name__ = "Unsigned32"
_EpSpecificCodecClearChannelVoicePriority_Object = MibTableColumn
epSpecificCodecClearChannelVoicePriority = _EpSpecificCodecClearChannelVoicePriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 900, 800, 1, 400),
    _EpSpecificCodecClearChannelVoicePriority_Type()
)
epSpecificCodecClearChannelVoicePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecClearChannelVoicePriority.setStatus("current")


class _EpSpecificCodecClearChannelDataEnable_Type(MxEnableState):
    """Custom type epSpecificCodecClearChannelDataEnable based on MxEnableState"""
    defaultValue = 0


_EpSpecificCodecClearChannelDataEnable_Type.__name__ = "MxEnableState"
_EpSpecificCodecClearChannelDataEnable_Object = MibTableColumn
epSpecificCodecClearChannelDataEnable = _EpSpecificCodecClearChannelDataEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 900, 800, 1, 500),
    _EpSpecificCodecClearChannelDataEnable_Type()
)
epSpecificCodecClearChannelDataEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecClearChannelDataEnable.setStatus("current")


class _EpSpecificCodecClearChannelDataPriority_Type(Unsigned32):
    """Custom type epSpecificCodecClearChannelDataPriority based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_EpSpecificCodecClearChannelDataPriority_Type.__name__ = "Unsigned32"
_EpSpecificCodecClearChannelDataPriority_Object = MibTableColumn
epSpecificCodecClearChannelDataPriority = _EpSpecificCodecClearChannelDataPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 900, 800, 1, 600),
    _EpSpecificCodecClearChannelDataPriority_Type()
)
epSpecificCodecClearChannelDataPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecClearChannelDataPriority.setStatus("current")


class _EpSpecificCodecClearChannelPayloadType_Type(Unsigned32):
    """Custom type epSpecificCodecClearChannelPayloadType based on Unsigned32"""
    defaultValue = 125

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(96, 127),
    )


_EpSpecificCodecClearChannelPayloadType_Type.__name__ = "Unsigned32"
_EpSpecificCodecClearChannelPayloadType_Object = MibTableColumn
epSpecificCodecClearChannelPayloadType = _EpSpecificCodecClearChannelPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 900, 800, 1, 700),
    _EpSpecificCodecClearChannelPayloadType_Type()
)
epSpecificCodecClearChannelPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecClearChannelPayloadType.setStatus("current")


class _EpSpecificCodecClearChannelMinPTime_Type(Unsigned32):
    """Custom type epSpecificCodecClearChannelMinPTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_EpSpecificCodecClearChannelMinPTime_Type.__name__ = "Unsigned32"
_EpSpecificCodecClearChannelMinPTime_Object = MibTableColumn
epSpecificCodecClearChannelMinPTime = _EpSpecificCodecClearChannelMinPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 900, 800, 1, 800),
    _EpSpecificCodecClearChannelMinPTime_Type()
)
epSpecificCodecClearChannelMinPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecClearChannelMinPTime.setStatus("current")


class _EpSpecificCodecClearChannelMaxPTime_Type(Unsigned32):
    """Custom type epSpecificCodecClearChannelMaxPTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_EpSpecificCodecClearChannelMaxPTime_Type.__name__ = "Unsigned32"
_EpSpecificCodecClearChannelMaxPTime_Object = MibTableColumn
epSpecificCodecClearChannelMaxPTime = _EpSpecificCodecClearChannelMaxPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 900, 800, 1, 900),
    _EpSpecificCodecClearChannelMaxPTime_Type()
)
epSpecificCodecClearChannelMaxPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecClearChannelMaxPTime.setStatus("current")
_CodecXCCDGroup_ObjectIdentity = ObjectIdentity
codecXCCDGroup = _CodecXCCDGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 1000)
)


class _DefaultCodecXCCDVoiceEnable_Type(MxEnableState):
    """Custom type defaultCodecXCCDVoiceEnable based on MxEnableState"""
    defaultValue = 0


_DefaultCodecXCCDVoiceEnable_Type.__name__ = "MxEnableState"
_DefaultCodecXCCDVoiceEnable_Object = MibScalar
defaultCodecXCCDVoiceEnable = _DefaultCodecXCCDVoiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 1000, 100),
    _DefaultCodecXCCDVoiceEnable_Type()
)
defaultCodecXCCDVoiceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecXCCDVoiceEnable.setStatus("current")


class _DefaultCodecXCCDVoicePriority_Type(Unsigned32):
    """Custom type defaultCodecXCCDVoicePriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_DefaultCodecXCCDVoicePriority_Type.__name__ = "Unsigned32"
_DefaultCodecXCCDVoicePriority_Object = MibScalar
defaultCodecXCCDVoicePriority = _DefaultCodecXCCDVoicePriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 1000, 200),
    _DefaultCodecXCCDVoicePriority_Type()
)
defaultCodecXCCDVoicePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecXCCDVoicePriority.setStatus("current")


class _DefaultCodecXCCDDataEnable_Type(MxEnableState):
    """Custom type defaultCodecXCCDDataEnable based on MxEnableState"""
    defaultValue = 0


_DefaultCodecXCCDDataEnable_Type.__name__ = "MxEnableState"
_DefaultCodecXCCDDataEnable_Object = MibScalar
defaultCodecXCCDDataEnable = _DefaultCodecXCCDDataEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 1000, 300),
    _DefaultCodecXCCDDataEnable_Type()
)
defaultCodecXCCDDataEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecXCCDDataEnable.setStatus("current")


class _DefaultCodecXCCDDataPriority_Type(Unsigned32):
    """Custom type defaultCodecXCCDDataPriority based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_DefaultCodecXCCDDataPriority_Type.__name__ = "Unsigned32"
_DefaultCodecXCCDDataPriority_Object = MibScalar
defaultCodecXCCDDataPriority = _DefaultCodecXCCDDataPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 1000, 400),
    _DefaultCodecXCCDDataPriority_Type()
)
defaultCodecXCCDDataPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecXCCDDataPriority.setStatus("current")


class _DefaultCodecXCCDPayloadType_Type(Unsigned32):
    """Custom type defaultCodecXCCDPayloadType based on Unsigned32"""
    defaultValue = 126

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(96, 127),
    )


_DefaultCodecXCCDPayloadType_Type.__name__ = "Unsigned32"
_DefaultCodecXCCDPayloadType_Object = MibScalar
defaultCodecXCCDPayloadType = _DefaultCodecXCCDPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 1000, 500),
    _DefaultCodecXCCDPayloadType_Type()
)
defaultCodecXCCDPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecXCCDPayloadType.setStatus("current")


class _DefaultCodecXCCDMinPTime_Type(Unsigned32):
    """Custom type defaultCodecXCCDMinPTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_DefaultCodecXCCDMinPTime_Type.__name__ = "Unsigned32"
_DefaultCodecXCCDMinPTime_Object = MibScalar
defaultCodecXCCDMinPTime = _DefaultCodecXCCDMinPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 1000, 600),
    _DefaultCodecXCCDMinPTime_Type()
)
defaultCodecXCCDMinPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecXCCDMinPTime.setStatus("current")


class _DefaultCodecXCCDMaxPTime_Type(Unsigned32):
    """Custom type defaultCodecXCCDMaxPTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_DefaultCodecXCCDMaxPTime_Type.__name__ = "Unsigned32"
_DefaultCodecXCCDMaxPTime_Object = MibScalar
defaultCodecXCCDMaxPTime = _DefaultCodecXCCDMaxPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 1000, 700),
    _DefaultCodecXCCDMaxPTime_Type()
)
defaultCodecXCCDMaxPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecXCCDMaxPTime.setStatus("current")
_EpSpecificCodecXCCDTable_Object = MibTable
epSpecificCodecXCCDTable = _EpSpecificCodecXCCDTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 1000, 800)
)
if mibBuilder.loadTexts:
    epSpecificCodecXCCDTable.setStatus("current")
_EpSpecificCodecXCCDEntry_Object = MibTableRow
epSpecificCodecXCCDEntry = _EpSpecificCodecXCCDEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 1000, 800, 1)
)
epSpecificCodecXCCDEntry.setIndexNames(
    (0, "MX-MIPT-MIB", "epSpecificCodecXCCDEpId"),
)
if mibBuilder.loadTexts:
    epSpecificCodecXCCDEntry.setStatus("current")
_EpSpecificCodecXCCDEpId_Type = OctetString
_EpSpecificCodecXCCDEpId_Object = MibTableColumn
epSpecificCodecXCCDEpId = _EpSpecificCodecXCCDEpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 1000, 800, 1, 100),
    _EpSpecificCodecXCCDEpId_Type()
)
epSpecificCodecXCCDEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epSpecificCodecXCCDEpId.setStatus("current")


class _EpSpecificCodecXCCDEnableConfig_Type(MxEnableState):
    """Custom type epSpecificCodecXCCDEnableConfig based on MxEnableState"""
    defaultValue = 0


_EpSpecificCodecXCCDEnableConfig_Type.__name__ = "MxEnableState"
_EpSpecificCodecXCCDEnableConfig_Object = MibTableColumn
epSpecificCodecXCCDEnableConfig = _EpSpecificCodecXCCDEnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 1000, 800, 1, 200),
    _EpSpecificCodecXCCDEnableConfig_Type()
)
epSpecificCodecXCCDEnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecXCCDEnableConfig.setStatus("current")


class _EpSpecificCodecXCCDVoiceEnable_Type(MxEnableState):
    """Custom type epSpecificCodecXCCDVoiceEnable based on MxEnableState"""
    defaultValue = 0


_EpSpecificCodecXCCDVoiceEnable_Type.__name__ = "MxEnableState"
_EpSpecificCodecXCCDVoiceEnable_Object = MibTableColumn
epSpecificCodecXCCDVoiceEnable = _EpSpecificCodecXCCDVoiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 1000, 800, 1, 300),
    _EpSpecificCodecXCCDVoiceEnable_Type()
)
epSpecificCodecXCCDVoiceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecXCCDVoiceEnable.setStatus("current")


class _EpSpecificCodecXCCDVoicePriority_Type(Unsigned32):
    """Custom type epSpecificCodecXCCDVoicePriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_EpSpecificCodecXCCDVoicePriority_Type.__name__ = "Unsigned32"
_EpSpecificCodecXCCDVoicePriority_Object = MibTableColumn
epSpecificCodecXCCDVoicePriority = _EpSpecificCodecXCCDVoicePriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 1000, 800, 1, 400),
    _EpSpecificCodecXCCDVoicePriority_Type()
)
epSpecificCodecXCCDVoicePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecXCCDVoicePriority.setStatus("current")


class _EpSpecificCodecXCCDDataEnable_Type(MxEnableState):
    """Custom type epSpecificCodecXCCDDataEnable based on MxEnableState"""
    defaultValue = 0


_EpSpecificCodecXCCDDataEnable_Type.__name__ = "MxEnableState"
_EpSpecificCodecXCCDDataEnable_Object = MibTableColumn
epSpecificCodecXCCDDataEnable = _EpSpecificCodecXCCDDataEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 1000, 800, 1, 500),
    _EpSpecificCodecXCCDDataEnable_Type()
)
epSpecificCodecXCCDDataEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecXCCDDataEnable.setStatus("current")


class _EpSpecificCodecXCCDDataPriority_Type(Unsigned32):
    """Custom type epSpecificCodecXCCDDataPriority based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_EpSpecificCodecXCCDDataPriority_Type.__name__ = "Unsigned32"
_EpSpecificCodecXCCDDataPriority_Object = MibTableColumn
epSpecificCodecXCCDDataPriority = _EpSpecificCodecXCCDDataPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 1000, 800, 1, 600),
    _EpSpecificCodecXCCDDataPriority_Type()
)
epSpecificCodecXCCDDataPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecXCCDDataPriority.setStatus("current")


class _EpSpecificCodecXCCDPayloadType_Type(Unsigned32):
    """Custom type epSpecificCodecXCCDPayloadType based on Unsigned32"""
    defaultValue = 126

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(96, 127),
    )


_EpSpecificCodecXCCDPayloadType_Type.__name__ = "Unsigned32"
_EpSpecificCodecXCCDPayloadType_Object = MibTableColumn
epSpecificCodecXCCDPayloadType = _EpSpecificCodecXCCDPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 1000, 800, 1, 700),
    _EpSpecificCodecXCCDPayloadType_Type()
)
epSpecificCodecXCCDPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecXCCDPayloadType.setStatus("current")


class _EpSpecificCodecXCCDMinPTime_Type(Unsigned32):
    """Custom type epSpecificCodecXCCDMinPTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_EpSpecificCodecXCCDMinPTime_Type.__name__ = "Unsigned32"
_EpSpecificCodecXCCDMinPTime_Object = MibTableColumn
epSpecificCodecXCCDMinPTime = _EpSpecificCodecXCCDMinPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 1000, 800, 1, 800),
    _EpSpecificCodecXCCDMinPTime_Type()
)
epSpecificCodecXCCDMinPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecXCCDMinPTime.setStatus("current")


class _EpSpecificCodecXCCDMaxPTime_Type(Unsigned32):
    """Custom type epSpecificCodecXCCDMaxPTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_EpSpecificCodecXCCDMaxPTime_Type.__name__ = "Unsigned32"
_EpSpecificCodecXCCDMaxPTime_Object = MibTableColumn
epSpecificCodecXCCDMaxPTime = _EpSpecificCodecXCCDMaxPTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 100, 1000, 800, 1, 900),
    _EpSpecificCodecXCCDMaxPTime_Type()
)
epSpecificCodecXCCDMaxPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCodecXCCDMaxPTime.setStatus("current")
_JitterBufferGroup_ObjectIdentity = ObjectIdentity
jitterBufferGroup = _JitterBufferGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 200)
)


class _DefaultJitterBufferLevel_Type(Integer32):
    """Custom type defaultJitterBufferLevel based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400,
              500)
        )
    )
    namedValues = NamedValues(
        *(("optimizeLatency", 100),
          ("normal", 200),
          ("optimizeQuality", 300),
          ("faxModem", 400),
          ("custom", 500))
    )


_DefaultJitterBufferLevel_Type.__name__ = "Integer32"
_DefaultJitterBufferLevel_Object = MibScalar
defaultJitterBufferLevel = _DefaultJitterBufferLevel_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 200, 100),
    _DefaultJitterBufferLevel_Type()
)
defaultJitterBufferLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultJitterBufferLevel.setStatus("current")


class _DefaultJitterBufferCustomMinLength_Type(Unsigned32):
    """Custom type defaultJitterBufferCustomMinLength based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_DefaultJitterBufferCustomMinLength_Type.__name__ = "Unsigned32"
_DefaultJitterBufferCustomMinLength_Object = MibScalar
defaultJitterBufferCustomMinLength = _DefaultJitterBufferCustomMinLength_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 200, 200),
    _DefaultJitterBufferCustomMinLength_Type()
)
defaultJitterBufferCustomMinLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultJitterBufferCustomMinLength.setStatus("current")


class _DefaultJitterBufferCustomNomLength_Type(Unsigned32):
    """Custom type defaultJitterBufferCustomNomLength based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_DefaultJitterBufferCustomNomLength_Type.__name__ = "Unsigned32"
_DefaultJitterBufferCustomNomLength_Object = MibScalar
defaultJitterBufferCustomNomLength = _DefaultJitterBufferCustomNomLength_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 200, 210),
    _DefaultJitterBufferCustomNomLength_Type()
)
defaultJitterBufferCustomNomLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultJitterBufferCustomNomLength.setStatus("current")


class _DefaultJitterBufferCustomMaxLength_Type(Unsigned32):
    """Custom type defaultJitterBufferCustomMaxLength based on Unsigned32"""
    defaultValue = 125

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_DefaultJitterBufferCustomMaxLength_Type.__name__ = "Unsigned32"
_DefaultJitterBufferCustomMaxLength_Object = MibScalar
defaultJitterBufferCustomMaxLength = _DefaultJitterBufferCustomMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 200, 300),
    _DefaultJitterBufferCustomMaxLength_Type()
)
defaultJitterBufferCustomMaxLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultJitterBufferCustomMaxLength.setStatus("current")


class _DefaultVbdJitterBufferCustomMinLength_Type(Unsigned32):
    """Custom type defaultVbdJitterBufferCustomMinLength based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_DefaultVbdJitterBufferCustomMinLength_Type.__name__ = "Unsigned32"
_DefaultVbdJitterBufferCustomMinLength_Object = MibScalar
defaultVbdJitterBufferCustomMinLength = _DefaultVbdJitterBufferCustomMinLength_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 200, 310),
    _DefaultVbdJitterBufferCustomMinLength_Type()
)
defaultVbdJitterBufferCustomMinLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultVbdJitterBufferCustomMinLength.setStatus("current")


class _DefaultVbdJitterBufferCustomNomLength_Type(Unsigned32):
    """Custom type defaultVbdJitterBufferCustomNomLength based on Unsigned32"""
    defaultValue = 67

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_DefaultVbdJitterBufferCustomNomLength_Type.__name__ = "Unsigned32"
_DefaultVbdJitterBufferCustomNomLength_Object = MibScalar
defaultVbdJitterBufferCustomNomLength = _DefaultVbdJitterBufferCustomNomLength_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 200, 320),
    _DefaultVbdJitterBufferCustomNomLength_Type()
)
defaultVbdJitterBufferCustomNomLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultVbdJitterBufferCustomNomLength.setStatus("current")


class _DefaultVbdJitterBufferCustomMaxLength_Type(Unsigned32):
    """Custom type defaultVbdJitterBufferCustomMaxLength based on Unsigned32"""
    defaultValue = 135

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_DefaultVbdJitterBufferCustomMaxLength_Type.__name__ = "Unsigned32"
_DefaultVbdJitterBufferCustomMaxLength_Object = MibScalar
defaultVbdJitterBufferCustomMaxLength = _DefaultVbdJitterBufferCustomMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 200, 330),
    _DefaultVbdJitterBufferCustomMaxLength_Type()
)
defaultVbdJitterBufferCustomMaxLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultVbdJitterBufferCustomMaxLength.setStatus("current")


class _DefaultVbdJitterBufferType_Type(Integer32):
    """Custom type defaultVbdJitterBufferType based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300)
        )
    )
    namedValues = NamedValues(
        *(("adaptiveImmediately", 100),
          ("adaptiveSilence", 200),
          ("fixed", 300))
    )


_DefaultVbdJitterBufferType_Type.__name__ = "Integer32"
_DefaultVbdJitterBufferType_Object = MibScalar
defaultVbdJitterBufferType = _DefaultVbdJitterBufferType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 200, 340),
    _DefaultVbdJitterBufferType_Type()
)
defaultVbdJitterBufferType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultVbdJitterBufferType.setStatus("current")
_EpSpecificJitterBufferTable_Object = MibTable
epSpecificJitterBufferTable = _EpSpecificJitterBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 200, 400)
)
if mibBuilder.loadTexts:
    epSpecificJitterBufferTable.setStatus("current")
_EpSpecificJitterBufferEntry_Object = MibTableRow
epSpecificJitterBufferEntry = _EpSpecificJitterBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 200, 400, 1)
)
epSpecificJitterBufferEntry.setIndexNames(
    (0, "MX-MIPT-MIB", "epSpecificJitterBufferEpId"),
)
if mibBuilder.loadTexts:
    epSpecificJitterBufferEntry.setStatus("current")
_EpSpecificJitterBufferEpId_Type = OctetString
_EpSpecificJitterBufferEpId_Object = MibTableColumn
epSpecificJitterBufferEpId = _EpSpecificJitterBufferEpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 200, 400, 1, 100),
    _EpSpecificJitterBufferEpId_Type()
)
epSpecificJitterBufferEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epSpecificJitterBufferEpId.setStatus("current")


class _EpSpecificJitterBufferEnableConfig_Type(MxEnableState):
    """Custom type epSpecificJitterBufferEnableConfig based on MxEnableState"""
    defaultValue = 0


_EpSpecificJitterBufferEnableConfig_Type.__name__ = "MxEnableState"
_EpSpecificJitterBufferEnableConfig_Object = MibTableColumn
epSpecificJitterBufferEnableConfig = _EpSpecificJitterBufferEnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 200, 400, 1, 200),
    _EpSpecificJitterBufferEnableConfig_Type()
)
epSpecificJitterBufferEnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificJitterBufferEnableConfig.setStatus("current")


class _EpSpecificJitterBufferLevel_Type(Integer32):
    """Custom type epSpecificJitterBufferLevel based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400,
              500)
        )
    )
    namedValues = NamedValues(
        *(("optimizeLatency", 100),
          ("normal", 200),
          ("optimizeQuality", 300),
          ("faxModem", 400),
          ("custom", 500))
    )


_EpSpecificJitterBufferLevel_Type.__name__ = "Integer32"
_EpSpecificJitterBufferLevel_Object = MibTableColumn
epSpecificJitterBufferLevel = _EpSpecificJitterBufferLevel_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 200, 400, 1, 300),
    _EpSpecificJitterBufferLevel_Type()
)
epSpecificJitterBufferLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificJitterBufferLevel.setStatus("current")


class _EpSpecificJitterBufferCustomMinLength_Type(Unsigned32):
    """Custom type epSpecificJitterBufferCustomMinLength based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_EpSpecificJitterBufferCustomMinLength_Type.__name__ = "Unsigned32"
_EpSpecificJitterBufferCustomMinLength_Object = MibTableColumn
epSpecificJitterBufferCustomMinLength = _EpSpecificJitterBufferCustomMinLength_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 200, 400, 1, 400),
    _EpSpecificJitterBufferCustomMinLength_Type()
)
epSpecificJitterBufferCustomMinLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificJitterBufferCustomMinLength.setStatus("current")


class _EpSpecificJitterBufferCustomNomLength_Type(Unsigned32):
    """Custom type epSpecificJitterBufferCustomNomLength based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_EpSpecificJitterBufferCustomNomLength_Type.__name__ = "Unsigned32"
_EpSpecificJitterBufferCustomNomLength_Object = MibTableColumn
epSpecificJitterBufferCustomNomLength = _EpSpecificJitterBufferCustomNomLength_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 200, 400, 1, 410),
    _EpSpecificJitterBufferCustomNomLength_Type()
)
epSpecificJitterBufferCustomNomLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificJitterBufferCustomNomLength.setStatus("current")


class _EpSpecificJitterBufferCustomMaxLength_Type(Unsigned32):
    """Custom type epSpecificJitterBufferCustomMaxLength based on Unsigned32"""
    defaultValue = 125

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_EpSpecificJitterBufferCustomMaxLength_Type.__name__ = "Unsigned32"
_EpSpecificJitterBufferCustomMaxLength_Object = MibTableColumn
epSpecificJitterBufferCustomMaxLength = _EpSpecificJitterBufferCustomMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 200, 400, 1, 500),
    _EpSpecificJitterBufferCustomMaxLength_Type()
)
epSpecificJitterBufferCustomMaxLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificJitterBufferCustomMaxLength.setStatus("current")


class _EpSpecificJitterBufferCustomVbdMinLength_Type(Unsigned32):
    """Custom type epSpecificJitterBufferCustomVbdMinLength based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_EpSpecificJitterBufferCustomVbdMinLength_Type.__name__ = "Unsigned32"
_EpSpecificJitterBufferCustomVbdMinLength_Object = MibTableColumn
epSpecificJitterBufferCustomVbdMinLength = _EpSpecificJitterBufferCustomVbdMinLength_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 200, 400, 1, 600),
    _EpSpecificJitterBufferCustomVbdMinLength_Type()
)
epSpecificJitterBufferCustomVbdMinLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificJitterBufferCustomVbdMinLength.setStatus("current")


class _EpSpecificJitterBufferCustomVbdNomLength_Type(Unsigned32):
    """Custom type epSpecificJitterBufferCustomVbdNomLength based on Unsigned32"""
    defaultValue = 67

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_EpSpecificJitterBufferCustomVbdNomLength_Type.__name__ = "Unsigned32"
_EpSpecificJitterBufferCustomVbdNomLength_Object = MibTableColumn
epSpecificJitterBufferCustomVbdNomLength = _EpSpecificJitterBufferCustomVbdNomLength_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 200, 400, 1, 700),
    _EpSpecificJitterBufferCustomVbdNomLength_Type()
)
epSpecificJitterBufferCustomVbdNomLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificJitterBufferCustomVbdNomLength.setStatus("current")


class _EpSpecificJitterBufferCustomVbdMaxLength_Type(Unsigned32):
    """Custom type epSpecificJitterBufferCustomVbdMaxLength based on Unsigned32"""
    defaultValue = 125

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_EpSpecificJitterBufferCustomVbdMaxLength_Type.__name__ = "Unsigned32"
_EpSpecificJitterBufferCustomVbdMaxLength_Object = MibTableColumn
epSpecificJitterBufferCustomVbdMaxLength = _EpSpecificJitterBufferCustomVbdMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 200, 400, 1, 800),
    _EpSpecificJitterBufferCustomVbdMaxLength_Type()
)
epSpecificJitterBufferCustomVbdMaxLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificJitterBufferCustomVbdMaxLength.setStatus("current")


class _EpSpecificJitterBufferCustomVbdJitterBufferType_Type(Integer32):
    """Custom type epSpecificJitterBufferCustomVbdJitterBufferType based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300)
        )
    )
    namedValues = NamedValues(
        *(("adaptiveImmediately", 100),
          ("adaptiveSilence", 200),
          ("fixed", 300))
    )


_EpSpecificJitterBufferCustomVbdJitterBufferType_Type.__name__ = "Integer32"
_EpSpecificJitterBufferCustomVbdJitterBufferType_Object = MibTableColumn
epSpecificJitterBufferCustomVbdJitterBufferType = _EpSpecificJitterBufferCustomVbdJitterBufferType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 200, 400, 1, 900),
    _EpSpecificJitterBufferCustomVbdJitterBufferType_Type()
)
epSpecificJitterBufferCustomVbdJitterBufferType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificJitterBufferCustomVbdJitterBufferType.setStatus("current")
_DtmfTransportGroup_ObjectIdentity = ObjectIdentity
dtmfTransportGroup = _DtmfTransportGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 300)
)


class _DefaultDtmfTransportMethod_Type(Integer32):
    """Custom type defaultDtmfTransportMethod based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400)
        )
    )
    namedValues = NamedValues(
        *(("inBand", 100),
          ("outOfBandUsingRtp", 200),
          ("outOfBandUsingSignalingProtocol", 300),
          ("signalingProtocolDependent", 400))
    )


_DefaultDtmfTransportMethod_Type.__name__ = "Integer32"
_DefaultDtmfTransportMethod_Object = MibScalar
defaultDtmfTransportMethod = _DefaultDtmfTransportMethod_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 300, 100),
    _DefaultDtmfTransportMethod_Type()
)
defaultDtmfTransportMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultDtmfTransportMethod.setStatus("current")


class _DefaultDtmfTransportPayloadType_Type(Unsigned32):
    """Custom type defaultDtmfTransportPayloadType based on Unsigned32"""
    defaultValue = 96

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(96, 127),
    )


_DefaultDtmfTransportPayloadType_Type.__name__ = "Unsigned32"
_DefaultDtmfTransportPayloadType_Object = MibScalar
defaultDtmfTransportPayloadType = _DefaultDtmfTransportPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 300, 200),
    _DefaultDtmfTransportPayloadType_Type()
)
defaultDtmfTransportPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultDtmfTransportPayloadType.setStatus("current")
_EpSpecificDtmfTransportTable_Object = MibTable
epSpecificDtmfTransportTable = _EpSpecificDtmfTransportTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 300, 300)
)
if mibBuilder.loadTexts:
    epSpecificDtmfTransportTable.setStatus("current")
_EpSpecificDtmfTransportEntry_Object = MibTableRow
epSpecificDtmfTransportEntry = _EpSpecificDtmfTransportEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 300, 300, 1)
)
epSpecificDtmfTransportEntry.setIndexNames(
    (0, "MX-MIPT-MIB", "epSpecificDtmfTransportEpId"),
)
if mibBuilder.loadTexts:
    epSpecificDtmfTransportEntry.setStatus("current")
_EpSpecificDtmfTransportEpId_Type = OctetString
_EpSpecificDtmfTransportEpId_Object = MibTableColumn
epSpecificDtmfTransportEpId = _EpSpecificDtmfTransportEpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 300, 300, 1, 100),
    _EpSpecificDtmfTransportEpId_Type()
)
epSpecificDtmfTransportEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epSpecificDtmfTransportEpId.setStatus("current")


class _EpSpecificDtmfTransportEnableConfig_Type(MxEnableState):
    """Custom type epSpecificDtmfTransportEnableConfig based on MxEnableState"""
    defaultValue = 0


_EpSpecificDtmfTransportEnableConfig_Type.__name__ = "MxEnableState"
_EpSpecificDtmfTransportEnableConfig_Object = MibTableColumn
epSpecificDtmfTransportEnableConfig = _EpSpecificDtmfTransportEnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 300, 300, 1, 200),
    _EpSpecificDtmfTransportEnableConfig_Type()
)
epSpecificDtmfTransportEnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificDtmfTransportEnableConfig.setStatus("current")


class _EpSpecificDtmfTransportMethod_Type(Integer32):
    """Custom type epSpecificDtmfTransportMethod based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400)
        )
    )
    namedValues = NamedValues(
        *(("inBand", 100),
          ("outOfBandUsingRtp", 200),
          ("outOfBandUsingSignalingProtocol", 300),
          ("signalingProtocolDependent", 400))
    )


_EpSpecificDtmfTransportMethod_Type.__name__ = "Integer32"
_EpSpecificDtmfTransportMethod_Object = MibTableColumn
epSpecificDtmfTransportMethod = _EpSpecificDtmfTransportMethod_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 300, 300, 1, 300),
    _EpSpecificDtmfTransportMethod_Type()
)
epSpecificDtmfTransportMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificDtmfTransportMethod.setStatus("current")


class _EpSpecificDtmfTransportPayloadType_Type(Unsigned32):
    """Custom type epSpecificDtmfTransportPayloadType based on Unsigned32"""
    defaultValue = 96

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(96, 127),
    )


_EpSpecificDtmfTransportPayloadType_Type.__name__ = "Unsigned32"
_EpSpecificDtmfTransportPayloadType_Object = MibTableColumn
epSpecificDtmfTransportPayloadType = _EpSpecificDtmfTransportPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 300, 300, 1, 400),
    _EpSpecificDtmfTransportPayloadType_Type()
)
epSpecificDtmfTransportPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificDtmfTransportPayloadType.setStatus("current")
_IpTransportGroup_ObjectIdentity = ObjectIdentity
ipTransportGroup = _IpTransportGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 400)
)
_IpTransportRtpGroup_ObjectIdentity = ObjectIdentity
ipTransportRtpGroup = _IpTransportRtpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 400, 100)
)


class _IpTransportRtpBasePort_Type(Unsigned32):
    """Custom type ipTransportRtpBasePort based on Unsigned32"""
    defaultValue = 5004

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65435),
    )


_IpTransportRtpBasePort_Type.__name__ = "Unsigned32"
_IpTransportRtpBasePort_Object = MibScalar
ipTransportRtpBasePort = _IpTransportRtpBasePort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 400, 100, 100),
    _IpTransportRtpBasePort_Type()
)
ipTransportRtpBasePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTransportRtpBasePort.setStatus("current")


class _IpTransportSrtpBasePort_Type(Unsigned32):
    """Custom type ipTransportSrtpBasePort based on Unsigned32"""
    defaultValue = 5004

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1025, 65435),
    )


_IpTransportSrtpBasePort_Type.__name__ = "Unsigned32"
_IpTransportSrtpBasePort_Object = MibScalar
ipTransportSrtpBasePort = _IpTransportSrtpBasePort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 400, 100, 200),
    _IpTransportSrtpBasePort_Type()
)
ipTransportSrtpBasePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTransportSrtpBasePort.setStatus("current")
_IpTransportT38Group_ObjectIdentity = ObjectIdentity
ipTransportT38Group = _IpTransportT38Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 400, 200)
)


class _IpTransportT38BasePort_Type(Unsigned32):
    """Custom type ipTransportT38BasePort based on Unsigned32"""
    defaultValue = 6004

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65435),
    )


_IpTransportT38BasePort_Type.__name__ = "Unsigned32"
_IpTransportT38BasePort_Object = MibScalar
ipTransportT38BasePort = _IpTransportT38BasePort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 400, 200, 100),
    _IpTransportT38BasePort_Type()
)
ipTransportT38BasePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTransportT38BasePort.setStatus("current")
_CodecVsBearerCapabilitiesMapping_ObjectIdentity = ObjectIdentity
codecVsBearerCapabilitiesMapping = _CodecVsBearerCapabilitiesMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 500)
)
_DefaultCodecVsBearerCapabilitiesMappingTable_Object = MibTable
defaultCodecVsBearerCapabilitiesMappingTable = _DefaultCodecVsBearerCapabilitiesMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 500, 100)
)
if mibBuilder.loadTexts:
    defaultCodecVsBearerCapabilitiesMappingTable.setStatus("current")
_DefaultCodecVsBearerCapabilitiesMappingEntry_Object = MibTableRow
defaultCodecVsBearerCapabilitiesMappingEntry = _DefaultCodecVsBearerCapabilitiesMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 500, 100, 1)
)
defaultCodecVsBearerCapabilitiesMappingEntry.setIndexNames(
    (0, "MX-MIPT-MIB", "defaultCodecVsBearerCapabilitiesMappingIndex"),
)
if mibBuilder.loadTexts:
    defaultCodecVsBearerCapabilitiesMappingEntry.setStatus("current")


class _DefaultCodecVsBearerCapabilitiesMappingIndex_Type(Unsigned32):
    """Custom type defaultCodecVsBearerCapabilitiesMappingIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_DefaultCodecVsBearerCapabilitiesMappingIndex_Type.__name__ = "Unsigned32"
_DefaultCodecVsBearerCapabilitiesMappingIndex_Object = MibTableColumn
defaultCodecVsBearerCapabilitiesMappingIndex = _DefaultCodecVsBearerCapabilitiesMappingIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 500, 100, 1, 100),
    _DefaultCodecVsBearerCapabilitiesMappingIndex_Type()
)
defaultCodecVsBearerCapabilitiesMappingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultCodecVsBearerCapabilitiesMappingIndex.setStatus("current")


class _DefaultCodecVsBearerCapabilitiesMappingEnableMap_Type(MxEnableState):
    """Custom type defaultCodecVsBearerCapabilitiesMappingEnableMap based on MxEnableState"""
    defaultValue = 0


_DefaultCodecVsBearerCapabilitiesMappingEnableMap_Type.__name__ = "MxEnableState"
_DefaultCodecVsBearerCapabilitiesMappingEnableMap_Object = MibTableColumn
defaultCodecVsBearerCapabilitiesMappingEnableMap = _DefaultCodecVsBearerCapabilitiesMappingEnableMap_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 500, 100, 1, 200),
    _DefaultCodecVsBearerCapabilitiesMappingEnableMap_Type()
)
defaultCodecVsBearerCapabilitiesMappingEnableMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecVsBearerCapabilitiesMappingEnableMap.setStatus("current")


class _DefaultCodecVsBearerCapabilitiesMappingCodec_Type(Integer32):
    """Custom type defaultCodecVsBearerCapabilitiesMappingCodec based on Integer32"""
    defaultValue = 800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              250,
              300,
              400,
              500,
              600,
              700,
              800,
              900,
              1000,
              1100)
        )
    )
    namedValues = NamedValues(
        *(("g711alaw", 100),
          ("g711ulaw", 200),
          ("g722", 250),
          ("g723", 300),
          ("g72616kbps", 400),
          ("g72624kbps", 500),
          ("g72632kbps", 600),
          ("g72640kbps", 700),
          ("g729", 800),
          ("clearMode", 900),
          ("clearChannel", 1000),
          ("xCCD", 1100))
    )


_DefaultCodecVsBearerCapabilitiesMappingCodec_Type.__name__ = "Integer32"
_DefaultCodecVsBearerCapabilitiesMappingCodec_Object = MibTableColumn
defaultCodecVsBearerCapabilitiesMappingCodec = _DefaultCodecVsBearerCapabilitiesMappingCodec_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 500, 100, 1, 300),
    _DefaultCodecVsBearerCapabilitiesMappingCodec_Type()
)
defaultCodecVsBearerCapabilitiesMappingCodec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecVsBearerCapabilitiesMappingCodec.setStatus("current")


class _DefaultCodecVsBearerCapabilitiesMappingInformationTransferCap_Type(Integer32):
    """Custom type defaultCodecVsBearerCapabilitiesMappingInformationTransferCap based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300)
        )
    )
    namedValues = NamedValues(
        *(("audio31kHz", 100),
          ("speech", 200),
          ("unrestricted", 300))
    )


_DefaultCodecVsBearerCapabilitiesMappingInformationTransferCap_Type.__name__ = "Integer32"
_DefaultCodecVsBearerCapabilitiesMappingInformationTransferCap_Object = MibTableColumn
defaultCodecVsBearerCapabilitiesMappingInformationTransferCap = _DefaultCodecVsBearerCapabilitiesMappingInformationTransferCap_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 500, 100, 1, 400),
    _DefaultCodecVsBearerCapabilitiesMappingInformationTransferCap_Type()
)
defaultCodecVsBearerCapabilitiesMappingInformationTransferCap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecVsBearerCapabilitiesMappingInformationTransferCap.setStatus("current")


class _DefaultCodecVsBearerCapabilitiesMappingMappingType_Type(Integer32):
    """Custom type defaultCodecVsBearerCapabilitiesMappingMappingType based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("prioritize", 100),
          ("select", 200))
    )


_DefaultCodecVsBearerCapabilitiesMappingMappingType_Type.__name__ = "Integer32"
_DefaultCodecVsBearerCapabilitiesMappingMappingType_Object = MibTableColumn
defaultCodecVsBearerCapabilitiesMappingMappingType = _DefaultCodecVsBearerCapabilitiesMappingMappingType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 500, 100, 1, 500),
    _DefaultCodecVsBearerCapabilitiesMappingMappingType_Type()
)
defaultCodecVsBearerCapabilitiesMappingMappingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCodecVsBearerCapabilitiesMappingMappingType.setStatus("current")
_SecurityGroup_ObjectIdentity = ObjectIdentity
securityGroup = _SecurityGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 600)
)


class _DefaultSecurityRtpMode_Type(Integer32):
    """Custom type defaultSecurityRtpMode based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300)
        )
    )
    namedValues = NamedValues(
        *(("unsecure", 100),
          ("secure", 200),
          ("secureWithFallback", 300))
    )


_DefaultSecurityRtpMode_Type.__name__ = "Integer32"
_DefaultSecurityRtpMode_Object = MibScalar
defaultSecurityRtpMode = _DefaultSecurityRtpMode_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 600, 100),
    _DefaultSecurityRtpMode_Type()
)
defaultSecurityRtpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultSecurityRtpMode.setStatus("current")


class _DefaultSecurityKeyManagement_Type(Integer32):
    """Custom type defaultSecurityKeyManagement based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("mikey", 100),
          ("sdes", 200))
    )


_DefaultSecurityKeyManagement_Type.__name__ = "Integer32"
_DefaultSecurityKeyManagement_Object = MibScalar
defaultSecurityKeyManagement = _DefaultSecurityKeyManagement_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 600, 150),
    _DefaultSecurityKeyManagement_Type()
)
defaultSecurityKeyManagement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultSecurityKeyManagement.setStatus("current")


class _DefaultSecurityRtpEncryption_Type(Integer32):
    """Custom type defaultSecurityRtpEncryption based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("null", 100),
          ("aesCm128", 200))
    )


_DefaultSecurityRtpEncryption_Type.__name__ = "Integer32"
_DefaultSecurityRtpEncryption_Object = MibScalar
defaultSecurityRtpEncryption = _DefaultSecurityRtpEncryption_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 600, 200),
    _DefaultSecurityRtpEncryption_Type()
)
defaultSecurityRtpEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultSecurityRtpEncryption.setStatus("current")


class _AllowUnsecureT38WithSrtp_Type(MxEnableState):
    """Custom type allowUnsecureT38WithSrtp based on MxEnableState"""
    defaultValue = 0


_AllowUnsecureT38WithSrtp_Type.__name__ = "MxEnableState"
_AllowUnsecureT38WithSrtp_Object = MibScalar
allowUnsecureT38WithSrtp = _AllowUnsecureT38WithSrtp_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 600, 300),
    _AllowUnsecureT38WithSrtp_Type()
)
allowUnsecureT38WithSrtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    allowUnsecureT38WithSrtp.setStatus("current")


class _SessionUpdateCryptoMode_Type(Integer32):
    """Custom type sessionUpdateCryptoMode based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("regenerate", 100),
          ("keep", 200))
    )


_SessionUpdateCryptoMode_Type.__name__ = "Integer32"
_SessionUpdateCryptoMode_Object = MibScalar
sessionUpdateCryptoMode = _SessionUpdateCryptoMode_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 600, 350),
    _SessionUpdateCryptoMode_Type()
)
sessionUpdateCryptoMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sessionUpdateCryptoMode.setStatus("current")
_EpSpecificSecurityTable_Object = MibTable
epSpecificSecurityTable = _EpSpecificSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 600, 400)
)
if mibBuilder.loadTexts:
    epSpecificSecurityTable.setStatus("current")
_EpSpecificSecurityEntry_Object = MibTableRow
epSpecificSecurityEntry = _EpSpecificSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 600, 400, 1)
)
epSpecificSecurityEntry.setIndexNames(
    (0, "MX-MIPT-MIB", "epSpecificSecurityEpId"),
)
if mibBuilder.loadTexts:
    epSpecificSecurityEntry.setStatus("current")
_EpSpecificSecurityEpId_Type = OctetString
_EpSpecificSecurityEpId_Object = MibTableColumn
epSpecificSecurityEpId = _EpSpecificSecurityEpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 600, 400, 1, 100),
    _EpSpecificSecurityEpId_Type()
)
epSpecificSecurityEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epSpecificSecurityEpId.setStatus("current")


class _EpSpecificSecurityEnableConfig_Type(MxEnableState):
    """Custom type epSpecificSecurityEnableConfig based on MxEnableState"""
    defaultValue = 0


_EpSpecificSecurityEnableConfig_Type.__name__ = "MxEnableState"
_EpSpecificSecurityEnableConfig_Object = MibTableColumn
epSpecificSecurityEnableConfig = _EpSpecificSecurityEnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 600, 400, 1, 200),
    _EpSpecificSecurityEnableConfig_Type()
)
epSpecificSecurityEnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificSecurityEnableConfig.setStatus("current")


class _EpSpecificSecurityRtpMode_Type(Integer32):
    """Custom type epSpecificSecurityRtpMode based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300)
        )
    )
    namedValues = NamedValues(
        *(("unsecure", 100),
          ("secure", 200),
          ("secureWithFallback", 300))
    )


_EpSpecificSecurityRtpMode_Type.__name__ = "Integer32"
_EpSpecificSecurityRtpMode_Object = MibTableColumn
epSpecificSecurityRtpMode = _EpSpecificSecurityRtpMode_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 600, 400, 1, 300),
    _EpSpecificSecurityRtpMode_Type()
)
epSpecificSecurityRtpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificSecurityRtpMode.setStatus("current")


class _EpSpecificSecurityKeyManagement_Type(Integer32):
    """Custom type epSpecificSecurityKeyManagement based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("mikey", 100),
          ("sdes", 200))
    )


_EpSpecificSecurityKeyManagement_Type.__name__ = "Integer32"
_EpSpecificSecurityKeyManagement_Object = MibTableColumn
epSpecificSecurityKeyManagement = _EpSpecificSecurityKeyManagement_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 600, 400, 1, 350),
    _EpSpecificSecurityKeyManagement_Type()
)
epSpecificSecurityKeyManagement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificSecurityKeyManagement.setStatus("current")


class _EpSpecificSecurityRtpEncryption_Type(Integer32):
    """Custom type epSpecificSecurityRtpEncryption based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("null", 100),
          ("aesCm128", 200))
    )


_EpSpecificSecurityRtpEncryption_Type.__name__ = "Integer32"
_EpSpecificSecurityRtpEncryption_Object = MibTableColumn
epSpecificSecurityRtpEncryption = _EpSpecificSecurityRtpEncryption_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 600, 400, 1, 400),
    _EpSpecificSecurityRtpEncryption_Type()
)
epSpecificSecurityRtpEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificSecurityRtpEncryption.setStatus("current")
_StatisticsGroup_ObjectIdentity = ObjectIdentity
statisticsGroup = _StatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 700)
)
_LastConnectionsStatsTable_Object = MibTable
lastConnectionsStatsTable = _LastConnectionsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 700, 100)
)
if mibBuilder.loadTexts:
    lastConnectionsStatsTable.setStatus("current")
_LastConnectionsStatsEntry_Object = MibTableRow
lastConnectionsStatsEntry = _LastConnectionsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 700, 100, 1)
)
lastConnectionsStatsEntry.setIndexNames(
    (0, "MX-MIPT-MIB", "lastConnectionsStatsConnectionsIndex"),
)
if mibBuilder.loadTexts:
    lastConnectionsStatsEntry.setStatus("current")


class _LastConnectionsStatsConnectionsIndex_Type(Unsigned32):
    """Custom type lastConnectionsStatsConnectionsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_LastConnectionsStatsConnectionsIndex_Type.__name__ = "Unsigned32"
_LastConnectionsStatsConnectionsIndex_Object = MibTableColumn
lastConnectionsStatsConnectionsIndex = _LastConnectionsStatsConnectionsIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 700, 100, 1, 100),
    _LastConnectionsStatsConnectionsIndex_Type()
)
lastConnectionsStatsConnectionsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastConnectionsStatsConnectionsIndex.setStatus("current")
_LastConnectionsStatsOctetsTransmitted_Type = MxUInt64
_LastConnectionsStatsOctetsTransmitted_Object = MibTableColumn
lastConnectionsStatsOctetsTransmitted = _LastConnectionsStatsOctetsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 700, 100, 1, 200),
    _LastConnectionsStatsOctetsTransmitted_Type()
)
lastConnectionsStatsOctetsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastConnectionsStatsOctetsTransmitted.setStatus("current")
_LastConnectionsStatsOctetsReceived_Type = MxUInt64
_LastConnectionsStatsOctetsReceived_Object = MibTableColumn
lastConnectionsStatsOctetsReceived = _LastConnectionsStatsOctetsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 700, 100, 1, 300),
    _LastConnectionsStatsOctetsReceived_Type()
)
lastConnectionsStatsOctetsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastConnectionsStatsOctetsReceived.setStatus("current")
_LastConnectionsStatsPacketsTransmitted_Type = MxUInt64
_LastConnectionsStatsPacketsTransmitted_Object = MibTableColumn
lastConnectionsStatsPacketsTransmitted = _LastConnectionsStatsPacketsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 700, 100, 1, 400),
    _LastConnectionsStatsPacketsTransmitted_Type()
)
lastConnectionsStatsPacketsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastConnectionsStatsPacketsTransmitted.setStatus("current")
_LastConnectionsStatsPacketsReceived_Type = MxUInt64
_LastConnectionsStatsPacketsReceived_Object = MibTableColumn
lastConnectionsStatsPacketsReceived = _LastConnectionsStatsPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 700, 100, 1, 500),
    _LastConnectionsStatsPacketsReceived_Type()
)
lastConnectionsStatsPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastConnectionsStatsPacketsReceived.setStatus("current")
_LastConnectionsStatsPacketsLost_Type = Unsigned32
_LastConnectionsStatsPacketsLost_Object = MibTableColumn
lastConnectionsStatsPacketsLost = _LastConnectionsStatsPacketsLost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 700, 100, 1, 600),
    _LastConnectionsStatsPacketsLost_Type()
)
lastConnectionsStatsPacketsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastConnectionsStatsPacketsLost.setStatus("current")
_LastConnectionsStatsMinimumInterarrivalJitter_Type = Unsigned32
_LastConnectionsStatsMinimumInterarrivalJitter_Object = MibTableColumn
lastConnectionsStatsMinimumInterarrivalJitter = _LastConnectionsStatsMinimumInterarrivalJitter_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 700, 100, 1, 700),
    _LastConnectionsStatsMinimumInterarrivalJitter_Type()
)
lastConnectionsStatsMinimumInterarrivalJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastConnectionsStatsMinimumInterarrivalJitter.setStatus("current")
_LastConnectionsStatsMaximumInterarrivalJitter_Type = Unsigned32
_LastConnectionsStatsMaximumInterarrivalJitter_Object = MibTableColumn
lastConnectionsStatsMaximumInterarrivalJitter = _LastConnectionsStatsMaximumInterarrivalJitter_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 700, 100, 1, 800),
    _LastConnectionsStatsMaximumInterarrivalJitter_Type()
)
lastConnectionsStatsMaximumInterarrivalJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastConnectionsStatsMaximumInterarrivalJitter.setStatus("current")
_LastConnectionsStatsAverageInterarrivalJitter_Type = Unsigned32
_LastConnectionsStatsAverageInterarrivalJitter_Object = MibTableColumn
lastConnectionsStatsAverageInterarrivalJitter = _LastConnectionsStatsAverageInterarrivalJitter_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 700, 100, 1, 900),
    _LastConnectionsStatsAverageInterarrivalJitter_Type()
)
lastConnectionsStatsAverageInterarrivalJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastConnectionsStatsAverageInterarrivalJitter.setStatus("current")
_LastConnectionsStatsMinimumLatency_Type = Unsigned32
_LastConnectionsStatsMinimumLatency_Object = MibTableColumn
lastConnectionsStatsMinimumLatency = _LastConnectionsStatsMinimumLatency_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 700, 100, 1, 1000),
    _LastConnectionsStatsMinimumLatency_Type()
)
lastConnectionsStatsMinimumLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastConnectionsStatsMinimumLatency.setStatus("current")
_LastConnectionsStatsMaximumLatency_Type = Unsigned32
_LastConnectionsStatsMaximumLatency_Object = MibTableColumn
lastConnectionsStatsMaximumLatency = _LastConnectionsStatsMaximumLatency_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 700, 100, 1, 1100),
    _LastConnectionsStatsMaximumLatency_Type()
)
lastConnectionsStatsMaximumLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastConnectionsStatsMaximumLatency.setStatus("current")
_LastConnectionsStatsAverageLatency_Type = Unsigned32
_LastConnectionsStatsAverageLatency_Object = MibTableColumn
lastConnectionsStatsAverageLatency = _LastConnectionsStatsAverageLatency_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 700, 100, 1, 1200),
    _LastConnectionsStatsAverageLatency_Type()
)
lastConnectionsStatsAverageLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastConnectionsStatsAverageLatency.setStatus("current")
_LastPeriodsStatsTable_Object = MibTable
lastPeriodsStatsTable = _LastPeriodsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 700, 200)
)
if mibBuilder.loadTexts:
    lastPeriodsStatsTable.setStatus("current")
_LastPeriodsStatsEntry_Object = MibTableRow
lastPeriodsStatsEntry = _LastPeriodsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 700, 200, 1)
)
lastPeriodsStatsEntry.setIndexNames(
    (0, "MX-MIPT-MIB", "lastPeriodsStatsPeriodIndex"),
)
if mibBuilder.loadTexts:
    lastPeriodsStatsEntry.setStatus("current")


class _LastPeriodsStatsPeriodIndex_Type(Unsigned32):
    """Custom type lastPeriodsStatsPeriodIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_LastPeriodsStatsPeriodIndex_Type.__name__ = "Unsigned32"
_LastPeriodsStatsPeriodIndex_Object = MibTableColumn
lastPeriodsStatsPeriodIndex = _LastPeriodsStatsPeriodIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 700, 200, 1, 100),
    _LastPeriodsStatsPeriodIndex_Type()
)
lastPeriodsStatsPeriodIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastPeriodsStatsPeriodIndex.setStatus("current")
_LastPeriodsStatsOctetsTransmitted_Type = MxUInt64
_LastPeriodsStatsOctetsTransmitted_Object = MibTableColumn
lastPeriodsStatsOctetsTransmitted = _LastPeriodsStatsOctetsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 700, 200, 1, 200),
    _LastPeriodsStatsOctetsTransmitted_Type()
)
lastPeriodsStatsOctetsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastPeriodsStatsOctetsTransmitted.setStatus("current")
_LastPeriodsStatsOctetsReceived_Type = MxUInt64
_LastPeriodsStatsOctetsReceived_Object = MibTableColumn
lastPeriodsStatsOctetsReceived = _LastPeriodsStatsOctetsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 700, 200, 1, 300),
    _LastPeriodsStatsOctetsReceived_Type()
)
lastPeriodsStatsOctetsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastPeriodsStatsOctetsReceived.setStatus("current")
_LastPeriodsStatsPacketsTransmitted_Type = MxUInt64
_LastPeriodsStatsPacketsTransmitted_Object = MibTableColumn
lastPeriodsStatsPacketsTransmitted = _LastPeriodsStatsPacketsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 700, 200, 1, 400),
    _LastPeriodsStatsPacketsTransmitted_Type()
)
lastPeriodsStatsPacketsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastPeriodsStatsPacketsTransmitted.setStatus("current")
_LastPeriodsStatsPacketsReceived_Type = MxUInt64
_LastPeriodsStatsPacketsReceived_Object = MibTableColumn
lastPeriodsStatsPacketsReceived = _LastPeriodsStatsPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 700, 200, 1, 500),
    _LastPeriodsStatsPacketsReceived_Type()
)
lastPeriodsStatsPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastPeriodsStatsPacketsReceived.setStatus("current")
_LastPeriodsStatsPacketsLost_Type = Unsigned32
_LastPeriodsStatsPacketsLost_Object = MibTableColumn
lastPeriodsStatsPacketsLost = _LastPeriodsStatsPacketsLost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 700, 200, 1, 600),
    _LastPeriodsStatsPacketsLost_Type()
)
lastPeriodsStatsPacketsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastPeriodsStatsPacketsLost.setStatus("current")
_LastPeriodsStatsMinimumInterarrivalJitter_Type = Unsigned32
_LastPeriodsStatsMinimumInterarrivalJitter_Object = MibTableColumn
lastPeriodsStatsMinimumInterarrivalJitter = _LastPeriodsStatsMinimumInterarrivalJitter_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 700, 200, 1, 700),
    _LastPeriodsStatsMinimumInterarrivalJitter_Type()
)
lastPeriodsStatsMinimumInterarrivalJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastPeriodsStatsMinimumInterarrivalJitter.setStatus("current")
_LastPeriodsStatsMaximumInterarrivalJitter_Type = Unsigned32
_LastPeriodsStatsMaximumInterarrivalJitter_Object = MibTableColumn
lastPeriodsStatsMaximumInterarrivalJitter = _LastPeriodsStatsMaximumInterarrivalJitter_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 700, 200, 1, 800),
    _LastPeriodsStatsMaximumInterarrivalJitter_Type()
)
lastPeriodsStatsMaximumInterarrivalJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastPeriodsStatsMaximumInterarrivalJitter.setStatus("current")
_LastPeriodsStatsAverageInterarrivalJitter_Type = Unsigned32
_LastPeriodsStatsAverageInterarrivalJitter_Object = MibTableColumn
lastPeriodsStatsAverageInterarrivalJitter = _LastPeriodsStatsAverageInterarrivalJitter_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 700, 200, 1, 900),
    _LastPeriodsStatsAverageInterarrivalJitter_Type()
)
lastPeriodsStatsAverageInterarrivalJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastPeriodsStatsAverageInterarrivalJitter.setStatus("current")
_LastPeriodsStatsMinimumLatency_Type = Unsigned32
_LastPeriodsStatsMinimumLatency_Object = MibTableColumn
lastPeriodsStatsMinimumLatency = _LastPeriodsStatsMinimumLatency_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 700, 200, 1, 1000),
    _LastPeriodsStatsMinimumLatency_Type()
)
lastPeriodsStatsMinimumLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastPeriodsStatsMinimumLatency.setStatus("current")
_LastPeriodsStatsMaximumLatency_Type = Unsigned32
_LastPeriodsStatsMaximumLatency_Object = MibTableColumn
lastPeriodsStatsMaximumLatency = _LastPeriodsStatsMaximumLatency_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 700, 200, 1, 1100),
    _LastPeriodsStatsMaximumLatency_Type()
)
lastPeriodsStatsMaximumLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastPeriodsStatsMaximumLatency.setStatus("current")
_LastPeriodsStatsAverageLatency_Type = Unsigned32
_LastPeriodsStatsAverageLatency_Object = MibTableColumn
lastPeriodsStatsAverageLatency = _LastPeriodsStatsAverageLatency_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 700, 200, 1, 1200),
    _LastPeriodsStatsAverageLatency_Type()
)
lastPeriodsStatsAverageLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastPeriodsStatsAverageLatency.setStatus("current")
_LastPeriodsStatsPeriodBeginning_Type = OctetString
_LastPeriodsStatsPeriodBeginning_Object = MibTableColumn
lastPeriodsStatsPeriodBeginning = _LastPeriodsStatsPeriodBeginning_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 700, 200, 1, 1300),
    _LastPeriodsStatsPeriodBeginning_Type()
)
lastPeriodsStatsPeriodBeginning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastPeriodsStatsPeriodBeginning.setStatus("current")
_LastPeriodsStatsPeriodEnd_Type = OctetString
_LastPeriodsStatsPeriodEnd_Object = MibTableColumn
lastPeriodsStatsPeriodEnd = _LastPeriodsStatsPeriodEnd_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 700, 200, 1, 1400),
    _LastPeriodsStatsPeriodEnd_Type()
)
lastPeriodsStatsPeriodEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastPeriodsStatsPeriodEnd.setStatus("current")
_ChannelStatisticsTable_Object = MibTable
channelStatisticsTable = _ChannelStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 700, 250)
)
if mibBuilder.loadTexts:
    channelStatisticsTable.setStatus("current")
_ChannelStatisticsEntry_Object = MibTableRow
channelStatisticsEntry = _ChannelStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 700, 250, 1)
)
channelStatisticsEntry.setIndexNames(
    (0, "MX-MIPT-MIB", "channelStatisticsEpChannelId"),
)
if mibBuilder.loadTexts:
    channelStatisticsEntry.setStatus("current")
_ChannelStatisticsEpChannelId_Type = OctetString
_ChannelStatisticsEpChannelId_Object = MibTableColumn
channelStatisticsEpChannelId = _ChannelStatisticsEpChannelId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 700, 250, 1, 100),
    _ChannelStatisticsEpChannelId_Type()
)
channelStatisticsEpChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelStatisticsEpChannelId.setStatus("current")
_ChannelStatisticsPacketsSent_Type = Unsigned32
_ChannelStatisticsPacketsSent_Object = MibTableColumn
channelStatisticsPacketsSent = _ChannelStatisticsPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 700, 250, 1, 200),
    _ChannelStatisticsPacketsSent_Type()
)
channelStatisticsPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelStatisticsPacketsSent.setStatus("current")
_ChannelStatisticsPacketsReceived_Type = Unsigned32
_ChannelStatisticsPacketsReceived_Object = MibTableColumn
channelStatisticsPacketsReceived = _ChannelStatisticsPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 700, 250, 1, 300),
    _ChannelStatisticsPacketsReceived_Type()
)
channelStatisticsPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelStatisticsPacketsReceived.setStatus("current")
_ChannelStatisticsBytesSent_Type = Unsigned32
_ChannelStatisticsBytesSent_Object = MibTableColumn
channelStatisticsBytesSent = _ChannelStatisticsBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 700, 250, 1, 400),
    _ChannelStatisticsBytesSent_Type()
)
channelStatisticsBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelStatisticsBytesSent.setStatus("current")
_ChannelStatisticsBytesReceived_Type = Unsigned32
_ChannelStatisticsBytesReceived_Object = MibTableColumn
channelStatisticsBytesReceived = _ChannelStatisticsBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 700, 250, 1, 500),
    _ChannelStatisticsBytesReceived_Type()
)
channelStatisticsBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelStatisticsBytesReceived.setStatus("current")
_ChannelStatisticsAverageReceiveInterarrivalJitter_Type = Unsigned32
_ChannelStatisticsAverageReceiveInterarrivalJitter_Object = MibTableColumn
channelStatisticsAverageReceiveInterarrivalJitter = _ChannelStatisticsAverageReceiveInterarrivalJitter_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 700, 250, 1, 600),
    _ChannelStatisticsAverageReceiveInterarrivalJitter_Type()
)
channelStatisticsAverageReceiveInterarrivalJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelStatisticsAverageReceiveInterarrivalJitter.setStatus("current")


class _ChannelStatisticsReset_Type(Integer32):
    """Custom type channelStatisticsReset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("reset", 10))
    )


_ChannelStatisticsReset_Type.__name__ = "Integer32"
_ChannelStatisticsReset_Object = MibTableColumn
channelStatisticsReset = _ChannelStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 700, 250, 1, 900),
    _ChannelStatisticsReset_Type()
)
channelStatisticsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelStatisticsReset.setStatus("current")


class _StatsCollectionPeriodDuration_Type(Unsigned32):
    """Custom type statsCollectionPeriodDuration based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 44640),
    )


_StatsCollectionPeriodDuration_Type.__name__ = "Unsigned32"
_StatsCollectionPeriodDuration_Object = MibScalar
statsCollectionPeriodDuration = _StatsCollectionPeriodDuration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 700, 300),
    _StatsCollectionPeriodDuration_Type()
)
statsCollectionPeriodDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statsCollectionPeriodDuration.setStatus("current")


class _StatsPerConnectionNotificationEnable_Type(MxEnableState):
    """Custom type statsPerConnectionNotificationEnable based on MxEnableState"""
    defaultValue = 0


_StatsPerConnectionNotificationEnable_Type.__name__ = "MxEnableState"
_StatsPerConnectionNotificationEnable_Object = MibScalar
statsPerConnectionNotificationEnable = _StatsPerConnectionNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 700, 400),
    _StatsPerConnectionNotificationEnable_Type()
)
statsPerConnectionNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statsPerConnectionNotificationEnable.setStatus("current")


class _StatsPerPeriodNotificationEnable_Type(MxEnableState):
    """Custom type statsPerPeriodNotificationEnable based on MxEnableState"""
    defaultValue = 0


_StatsPerPeriodNotificationEnable_Type.__name__ = "MxEnableState"
_StatsPerPeriodNotificationEnable_Object = MibScalar
statsPerPeriodNotificationEnable = _StatsPerPeriodNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 700, 500),
    _StatsPerPeriodNotificationEnable_Type()
)
statsPerPeriodNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statsPerPeriodNotificationEnable.setStatus("current")
_InteropGroup_ObjectIdentity = ObjectIdentity
interopGroup = _InteropGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 40000)
)


class _EnforceSymmetricRtpEnable_Type(MxEnableState):
    """Custom type enforceSymmetricRtpEnable based on MxEnableState"""
    defaultValue = 0


_EnforceSymmetricRtpEnable_Type.__name__ = "MxEnableState"
_EnforceSymmetricRtpEnable_Object = MibScalar
enforceSymmetricRtpEnable = _EnforceSymmetricRtpEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 40000, 100),
    _EnforceSymmetricRtpEnable_Type()
)
enforceSymmetricRtpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enforceSymmetricRtpEnable.setStatus("current")


class _InteropDtmfRtpInitialPacketQty_Type(Unsigned32):
    """Custom type interopDtmfRtpInitialPacketQty based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_InteropDtmfRtpInitialPacketQty_Type.__name__ = "Unsigned32"
_InteropDtmfRtpInitialPacketQty_Object = MibScalar
interopDtmfRtpInitialPacketQty = _InteropDtmfRtpInitialPacketQty_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 40000, 200),
    _InteropDtmfRtpInitialPacketQty_Type()
)
interopDtmfRtpInitialPacketQty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopDtmfRtpInitialPacketQty.setStatus("current")


class _InteropPacketReceptionMode_Type(Integer32):
    """Custom type interopPacketReceptionMode based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("mode0", 100),
          ("mode1", 200))
    )


_InteropPacketReceptionMode_Type.__name__ = "Integer32"
_InteropPacketReceptionMode_Object = MibScalar
interopPacketReceptionMode = _InteropPacketReceptionMode_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 40000, 300),
    _InteropPacketReceptionMode_Type()
)
interopPacketReceptionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopPacketReceptionMode.setStatus("current")
_DebugGroup_ObjectIdentity = ObjectIdentity
debugGroup = _DebugGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 50000)
)
_PcmCaptureGroup_ObjectIdentity = ObjectIdentity
pcmCaptureGroup = _PcmCaptureGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 50000, 100)
)


class _PcmCaptureEnable_Type(MxEnableState):
    """Custom type pcmCaptureEnable based on MxEnableState"""
    defaultValue = 0


_PcmCaptureEnable_Type.__name__ = "MxEnableState"
_PcmCaptureEnable_Object = MibScalar
pcmCaptureEnable = _PcmCaptureEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 50000, 100, 100),
    _PcmCaptureEnable_Type()
)
pcmCaptureEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcmCaptureEnable.setStatus("current")


class _PcmCaptureEndpoint_Type(OctetString):
    """Custom type pcmCaptureEndpoint based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PcmCaptureEndpoint_Type.__name__ = "OctetString"
_PcmCaptureEndpoint_Object = MibScalar
pcmCaptureEndpoint = _PcmCaptureEndpoint_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 50000, 100, 200),
    _PcmCaptureEndpoint_Type()
)
pcmCaptureEndpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcmCaptureEndpoint.setStatus("current")


class _PcmCaptureIpAddr_Type(MxIpAddress):
    """Custom type pcmCaptureIpAddr based on MxIpAddress"""
    defaultValue = OctetString("")


_PcmCaptureIpAddr_Type.__name__ = "MxIpAddress"
_PcmCaptureIpAddr_Object = MibScalar
pcmCaptureIpAddr = _PcmCaptureIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 50000, 100, 300),
    _PcmCaptureIpAddr_Type()
)
pcmCaptureIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcmCaptureIpAddr.setStatus("current")
_DspTracingGroup_ObjectIdentity = ObjectIdentity
dspTracingGroup = _DspTracingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 50000, 200)
)


class _DspTracingEnable_Type(MxEnableState):
    """Custom type dspTracingEnable based on MxEnableState"""
    defaultValue = 0


_DspTracingEnable_Type.__name__ = "MxEnableState"
_DspTracingEnable_Object = MibScalar
dspTracingEnable = _DspTracingEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 50000, 200, 100),
    _DspTracingEnable_Type()
)
dspTracingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dspTracingEnable.setStatus("current")
_DspStatsGroup_ObjectIdentity = ObjectIdentity
dspStatsGroup = _DspStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 50000, 300)
)


class _DspStatsEnable_Type(MxEnableState):
    """Custom type dspStatsEnable based on MxEnableState"""
    defaultValue = 0


_DspStatsEnable_Type.__name__ = "MxEnableState"
_DspStatsEnable_Object = MibScalar
dspStatsEnable = _DspStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 50000, 300, 100),
    _DspStatsEnable_Type()
)
dspStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dspStatsEnable.setStatus("current")


class _DspStatsInterval_Type(Unsigned32):
    """Custom type dspStatsInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_DspStatsInterval_Type.__name__ = "Unsigned32"
_DspStatsInterval_Object = MibScalar
dspStatsInterval = _DspStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 50000, 300, 200),
    _DspStatsInterval_Type()
)
dspStatsInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dspStatsInterval.setStatus("current")


class _DspStatsFilter_Type(Unsigned32):
    """Custom type dspStatsFilter based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DspStatsFilter_Type.__name__ = "Unsigned32"
_DspStatsFilter_Object = MibScalar
dspStatsFilter = _DspStatsFilter_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 50000, 300, 300),
    _DspStatsFilter_Type()
)
dspStatsFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dspStatsFilter.setStatus("current")
_NotificationsGroup_ObjectIdentity = ObjectIdentity
notificationsGroup = _NotificationsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 60010)
)


class _MinSeverity_Type(Integer32):
    """Custom type minSeverity based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              100,
              200,
              300,
              400,
              500)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("debug", 100),
          ("info", 200),
          ("warning", 300),
          ("error", 400),
          ("critical", 500))
    )


_MinSeverity_Type.__name__ = "Integer32"
_MinSeverity_Object = MibScalar
minSeverity = _MinSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 60010, 100),
    _MinSeverity_Type()
)
minSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minSeverity.setStatus("current")
_ConfigurationGroup_ObjectIdentity = ObjectIdentity
configurationGroup = _ConfigurationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 60020)
)


class _NeedRestartInfo_Type(Integer32):
    """Custom type needRestartInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              100)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 100))
    )


_NeedRestartInfo_Type.__name__ = "Integer32"
_NeedRestartInfo_Object = MibScalar
needRestartInfo = _NeedRestartInfo_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1600, 1, 60020, 100),
    _NeedRestartInfo_Type()
)
needRestartInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    needRestartInfo.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-MIPT-MIB",
    **{"miptMIB": miptMIB,
       "miptMIBObjects": miptMIBObjects,
       "codecGroup": codecGroup,
       "defaultCodecGenericVoiceActivityDetection": defaultCodecGenericVoiceActivityDetection,
       "epSpecificCodecTable": epSpecificCodecTable,
       "epSpecificCodecEntry": epSpecificCodecEntry,
       "epSpecificCodecEpId": epSpecificCodecEpId,
       "epSpecificCodecEnableConfig": epSpecificCodecEnableConfig,
       "epSpecificCodecGenericVoiceActivityDetection": epSpecificCodecGenericVoiceActivityDetection,
       "codecG711Group": codecG711Group,
       "codecG711MulawGroup": codecG711MulawGroup,
       "defaultCodecG711MulawVoiceEnable": defaultCodecG711MulawVoiceEnable,
       "defaultCodecG711MulawVoicePriority": defaultCodecG711MulawVoicePriority,
       "defaultCodecG711MulawDataEnable": defaultCodecG711MulawDataEnable,
       "defaultCodecG711MulawDataPriority": defaultCodecG711MulawDataPriority,
       "defaultCodecG711MulawMinPTime": defaultCodecG711MulawMinPTime,
       "defaultCodecG711MulawMaxPTime": defaultCodecG711MulawMaxPTime,
       "epSpecificCodecG711MulawTable": epSpecificCodecG711MulawTable,
       "epSpecificCodecG711MulawEntry": epSpecificCodecG711MulawEntry,
       "epSpecificCodecG711MulawEpId": epSpecificCodecG711MulawEpId,
       "epSpecificCodecG711MulawEnableConfig": epSpecificCodecG711MulawEnableConfig,
       "epSpecificCodecG711MulawVoiceEnable": epSpecificCodecG711MulawVoiceEnable,
       "epSpecificCodecG711MulawVoicePriority": epSpecificCodecG711MulawVoicePriority,
       "epSpecificCodecG711MulawDataEnable": epSpecificCodecG711MulawDataEnable,
       "epSpecificCodecG711MulawDataPriority": epSpecificCodecG711MulawDataPriority,
       "epSpecificCodecG711MulawMinPTime": epSpecificCodecG711MulawMinPTime,
       "epSpecificCodecG711MulawMaxPTime": epSpecificCodecG711MulawMaxPTime,
       "codecG711AlawGroup": codecG711AlawGroup,
       "defaultCodecG711AlawVoiceEnable": defaultCodecG711AlawVoiceEnable,
       "defaultCodecG711AlawVoicePriority": defaultCodecG711AlawVoicePriority,
       "defaultCodecG711AlawDataEnable": defaultCodecG711AlawDataEnable,
       "defaultCodecG711AlawDataPriority": defaultCodecG711AlawDataPriority,
       "defaultCodecG711AlawMinPTime": defaultCodecG711AlawMinPTime,
       "defaultCodecG711AlawMaxPTime": defaultCodecG711AlawMaxPTime,
       "epSpecificCodecG711AlawTable": epSpecificCodecG711AlawTable,
       "epSpecificCodecG711AlawEntry": epSpecificCodecG711AlawEntry,
       "epSpecificCodecG711AlawEpId": epSpecificCodecG711AlawEpId,
       "epSpecificCodecG711AlawEnableConfig": epSpecificCodecG711AlawEnableConfig,
       "epSpecificCodecG711AlawVoiceEnable": epSpecificCodecG711AlawVoiceEnable,
       "epSpecificCodecG711AlawVoicePriority": epSpecificCodecG711AlawVoicePriority,
       "epSpecificCodecG711AlawDataEnable": epSpecificCodecG711AlawDataEnable,
       "epSpecificCodecG711AlawDataPriority": epSpecificCodecG711AlawDataPriority,
       "epSpecificCodecG711AlawMinPTime": epSpecificCodecG711AlawMinPTime,
       "epSpecificCodecG711AlawMaxPTime": epSpecificCodecG711AlawMaxPTime,
       "codecG722Group": codecG722Group,
       "defaultCodecG722VoiceEnable": defaultCodecG722VoiceEnable,
       "defaultCodecG722VoicePriority": defaultCodecG722VoicePriority,
       "defaultCodecG722MinPTime": defaultCodecG722MinPTime,
       "defaultCodecG722MaxPTime": defaultCodecG722MaxPTime,
       "epSpecificCodecG722Table": epSpecificCodecG722Table,
       "epSpecificCodecG722Entry": epSpecificCodecG722Entry,
       "epSpecificCodecG722EpId": epSpecificCodecG722EpId,
       "epSpecificCodecG722EnableConfig": epSpecificCodecG722EnableConfig,
       "epSpecificCodecG722VoiceEnable": epSpecificCodecG722VoiceEnable,
       "epSpecificCodecG722VoicePriority": epSpecificCodecG722VoicePriority,
       "epSpecificCodecG722MinPTime": epSpecificCodecG722MinPTime,
       "epSpecificCodecG722MaxPTime": epSpecificCodecG722MaxPTime,
       "codecG723Group": codecG723Group,
       "defaultCodecG723VoiceEnable": defaultCodecG723VoiceEnable,
       "defaultCodecG723VoicePriority": defaultCodecG723VoicePriority,
       "defaultCodecG723Bitrate": defaultCodecG723Bitrate,
       "defaultCodecG723MinPTime": defaultCodecG723MinPTime,
       "defaultCodecG723MaxPTime": defaultCodecG723MaxPTime,
       "epSpecificCodecG723Table": epSpecificCodecG723Table,
       "epSpecificCodecG723Entry": epSpecificCodecG723Entry,
       "epSpecificCodecG723EpId": epSpecificCodecG723EpId,
       "epSpecificCodecG723EnableConfig": epSpecificCodecG723EnableConfig,
       "epSpecificCodecG723VoiceEnable": epSpecificCodecG723VoiceEnable,
       "epSpecificCodecG723VoicePriority": epSpecificCodecG723VoicePriority,
       "epSpecificCodecG723Bitrate": epSpecificCodecG723Bitrate,
       "epSpecificCodecG723MinPTime": epSpecificCodecG723MinPTime,
       "epSpecificCodecG723MaxPTime": epSpecificCodecG723MaxPTime,
       "codecG726Group": codecG726Group,
       "codecG726r16kbpsGroup": codecG726r16kbpsGroup,
       "defaultCodecG726r16kbpsVoiceEnable": defaultCodecG726r16kbpsVoiceEnable,
       "defaultCodecG726r16kbpsVoicePriority": defaultCodecG726r16kbpsVoicePriority,
       "defaultCodecG726r16kbpsPayloadType": defaultCodecG726r16kbpsPayloadType,
       "defaultCodecG726r16kbpsMinPTime": defaultCodecG726r16kbpsMinPTime,
       "defaultCodecG726r16kbpsMaxPTime": defaultCodecG726r16kbpsMaxPTime,
       "epSpecificCodecG726r16kbpsTable": epSpecificCodecG726r16kbpsTable,
       "epSpecificCodecG726r16kbpsEntry": epSpecificCodecG726r16kbpsEntry,
       "epSpecificCodecG726r16kbpsEpId": epSpecificCodecG726r16kbpsEpId,
       "epSpecificCodecG726r16kbpsEnableConfig": epSpecificCodecG726r16kbpsEnableConfig,
       "epSpecificCodecG726r16kbpsVoiceEnable": epSpecificCodecG726r16kbpsVoiceEnable,
       "epSpecificCodecG726r16kbpsVoicePriority": epSpecificCodecG726r16kbpsVoicePriority,
       "epSpecificCodecG726r16kbpsPayloadType": epSpecificCodecG726r16kbpsPayloadType,
       "epSpecificCodecG726r16kbpsMinPTime": epSpecificCodecG726r16kbpsMinPTime,
       "epSpecificCodecG726r16kbpsMaxPTime": epSpecificCodecG726r16kbpsMaxPTime,
       "codecG726r24kbpsGroup": codecG726r24kbpsGroup,
       "defaultCodecG726r24kbpsVoiceEnable": defaultCodecG726r24kbpsVoiceEnable,
       "defaultCodecG726r24kbpsVoicePriority": defaultCodecG726r24kbpsVoicePriority,
       "defaultCodecG726r24kbpsPayloadType": defaultCodecG726r24kbpsPayloadType,
       "defaultCodecG726r24kbpsMinPTime": defaultCodecG726r24kbpsMinPTime,
       "defaultCodecG726r24kbpsMaxPTime": defaultCodecG726r24kbpsMaxPTime,
       "epSpecificCodecG726r24kbpsTable": epSpecificCodecG726r24kbpsTable,
       "epSpecificCodecG726r24kbpsEntry": epSpecificCodecG726r24kbpsEntry,
       "epSpecificCodecG726r24kbpsEpId": epSpecificCodecG726r24kbpsEpId,
       "epSpecificCodecG726r24kbpsEnableConfig": epSpecificCodecG726r24kbpsEnableConfig,
       "epSpecificCodecG726r24kbpsVoiceEnable": epSpecificCodecG726r24kbpsVoiceEnable,
       "epSpecificCodecG726r24kbpsVoicePriority": epSpecificCodecG726r24kbpsVoicePriority,
       "epSpecificCodecG726r24kbpsPayloadType": epSpecificCodecG726r24kbpsPayloadType,
       "epSpecificCodecG726r24kbpsMinPTime": epSpecificCodecG726r24kbpsMinPTime,
       "epSpecificCodecG726r24kbpsMaxPTime": epSpecificCodecG726r24kbpsMaxPTime,
       "codecG726r32kbpsGroup": codecG726r32kbpsGroup,
       "defaultCodecG726r32kbpsVoiceEnable": defaultCodecG726r32kbpsVoiceEnable,
       "defaultCodecG726r32kbpsVoicePriority": defaultCodecG726r32kbpsVoicePriority,
       "defaultCodecG726r32kbpsDataEnable": defaultCodecG726r32kbpsDataEnable,
       "defaultCodecG726r32kbpsDataPriority": defaultCodecG726r32kbpsDataPriority,
       "defaultCodecG726r32kbpsPayloadType": defaultCodecG726r32kbpsPayloadType,
       "defaultCodecG726r32kbpsMinPTime": defaultCodecG726r32kbpsMinPTime,
       "defaultCodecG726r32kbpsMaxPTime": defaultCodecG726r32kbpsMaxPTime,
       "epSpecificCodecG726r32kbpsTable": epSpecificCodecG726r32kbpsTable,
       "epSpecificCodecG726r32kbpsEntry": epSpecificCodecG726r32kbpsEntry,
       "epSpecificCodecG726r32kbpsEpId": epSpecificCodecG726r32kbpsEpId,
       "epSpecificCodecG726r32kbpsEnableConfig": epSpecificCodecG726r32kbpsEnableConfig,
       "epSpecificCodecG726r32kbpsVoiceEnable": epSpecificCodecG726r32kbpsVoiceEnable,
       "epSpecificCodecG726r32kbpsVoicePriority": epSpecificCodecG726r32kbpsVoicePriority,
       "epSpecificCodecG726r32kbpsDataEnable": epSpecificCodecG726r32kbpsDataEnable,
       "epSpecificCodecG726r32kbpsDataPriority": epSpecificCodecG726r32kbpsDataPriority,
       "epSpecificCodecG726r32kbpsPayloadType": epSpecificCodecG726r32kbpsPayloadType,
       "epSpecificCodecG726r32kbpsMinPTime": epSpecificCodecG726r32kbpsMinPTime,
       "epSpecificCodecG726r32kbpsMaxPTime": epSpecificCodecG726r32kbpsMaxPTime,
       "codecG726r40kbpsGroup": codecG726r40kbpsGroup,
       "defaultCodecG726r40kbpsVoiceEnable": defaultCodecG726r40kbpsVoiceEnable,
       "defaultCodecG726r40kbpsVoicePriority": defaultCodecG726r40kbpsVoicePriority,
       "defaultCodecG726r40kbpsDataEnable": defaultCodecG726r40kbpsDataEnable,
       "defaultCodecG726r40kbpsDataPriority": defaultCodecG726r40kbpsDataPriority,
       "defaultCodecG726r40kbpsPayloadType": defaultCodecG726r40kbpsPayloadType,
       "defaultCodecG726r40kbpsMinPTime": defaultCodecG726r40kbpsMinPTime,
       "defaultCodecG726r40kbpsMaxPTime": defaultCodecG726r40kbpsMaxPTime,
       "epSpecificCodecG726r40kbpsTable": epSpecificCodecG726r40kbpsTable,
       "epSpecificCodecG726r40kbpsEntry": epSpecificCodecG726r40kbpsEntry,
       "epSpecificCodecG726r40kbpsEpId": epSpecificCodecG726r40kbpsEpId,
       "epSpecificCodecG726r40kbpsEnableConfig": epSpecificCodecG726r40kbpsEnableConfig,
       "epSpecificCodecG726r40kbpsVoiceEnable": epSpecificCodecG726r40kbpsVoiceEnable,
       "epSpecificCodecG726r40kbpsVoicePriority": epSpecificCodecG726r40kbpsVoicePriority,
       "epSpecificCodecG726r40kbpsDataEnable": epSpecificCodecG726r40kbpsDataEnable,
       "epSpecificCodecG726r40kbpsDataPriority": epSpecificCodecG726r40kbpsDataPriority,
       "epSpecificCodecG726r40kbpsPayloadType": epSpecificCodecG726r40kbpsPayloadType,
       "epSpecificCodecG726r40kbpsMinPTime": epSpecificCodecG726r40kbpsMinPTime,
       "epSpecificCodecG726r40kbpsMaxPTime": epSpecificCodecG726r40kbpsMaxPTime,
       "codecG729Group": codecG729Group,
       "defaultCodecG729VoiceEnable": defaultCodecG729VoiceEnable,
       "defaultCodecG729VoicePriority": defaultCodecG729VoicePriority,
       "defaultCodecG729MinPTime": defaultCodecG729MinPTime,
       "defaultCodecG729MaxPTime": defaultCodecG729MaxPTime,
       "defaultCodecG729VoiceActivityDetection": defaultCodecG729VoiceActivityDetection,
       "epSpecificCodecG729Table": epSpecificCodecG729Table,
       "epSpecificCodecG729Entry": epSpecificCodecG729Entry,
       "epSpecificCodecG729EpId": epSpecificCodecG729EpId,
       "epSpecificCodecG729EnableConfig": epSpecificCodecG729EnableConfig,
       "epSpecificCodecG729VoiceEnable": epSpecificCodecG729VoiceEnable,
       "epSpecificCodecG729VoicePriority": epSpecificCodecG729VoicePriority,
       "epSpecificCodecG729MinPTime": epSpecificCodecG729MinPTime,
       "epSpecificCodecG729MaxPTime": epSpecificCodecG729MaxPTime,
       "epSpecificCodecG729VoiceActivityDetection": epSpecificCodecG729VoiceActivityDetection,
       "codecT38Group": codecT38Group,
       "defaultCodecT38DataEnable": defaultCodecT38DataEnable,
       "defaultCodecT38DataPriority": defaultCodecT38DataPriority,
       "defaultCodecT38RedundancyLevel": defaultCodecT38RedundancyLevel,
       "defaultCodecT38FinalFramesRedundancy": defaultCodecT38FinalFramesRedundancy,
       "defaultCodecT38NoSignalEnable": defaultCodecT38NoSignalEnable,
       "defaultCodecT38NoSignalTimeout": defaultCodecT38NoSignalTimeout,
       "defaultCodecT38DetectionThreshold": defaultCodecT38DetectionThreshold,
       "epSpecificCodecT38Table": epSpecificCodecT38Table,
       "epSpecificCodecT38Entry": epSpecificCodecT38Entry,
       "epSpecificCodecT38EpId": epSpecificCodecT38EpId,
       "epSpecificCodecT38EnableConfig": epSpecificCodecT38EnableConfig,
       "epSpecificCodecT38DataEnable": epSpecificCodecT38DataEnable,
       "epSpecificCodecT38DataPriority": epSpecificCodecT38DataPriority,
       "epSpecificCodecT38RedundancyLevel": epSpecificCodecT38RedundancyLevel,
       "epSpecificCodecT38DetectionThreshold": epSpecificCodecT38DetectionThreshold,
       "codecClearModeGroup": codecClearModeGroup,
       "defaultCodecClearModeVoiceEnable": defaultCodecClearModeVoiceEnable,
       "defaultCodecClearModeVoicePriority": defaultCodecClearModeVoicePriority,
       "defaultCodecClearModeDataEnable": defaultCodecClearModeDataEnable,
       "defaultCodecClearModeDataPriority": defaultCodecClearModeDataPriority,
       "defaultCodecClearModePayloadType": defaultCodecClearModePayloadType,
       "defaultCodecClearModeMinPTime": defaultCodecClearModeMinPTime,
       "defaultCodecClearModeMaxPTime": defaultCodecClearModeMaxPTime,
       "epSpecificCodecClearModeTable": epSpecificCodecClearModeTable,
       "epSpecificCodecClearModeEntry": epSpecificCodecClearModeEntry,
       "epSpecificCodecClearModeEpId": epSpecificCodecClearModeEpId,
       "epSpecificCodecClearModeEnableConfig": epSpecificCodecClearModeEnableConfig,
       "epSpecificCodecClearModeVoiceEnable": epSpecificCodecClearModeVoiceEnable,
       "epSpecificCodecClearModeVoicePriority": epSpecificCodecClearModeVoicePriority,
       "epSpecificCodecClearModeDataEnable": epSpecificCodecClearModeDataEnable,
       "epSpecificCodecClearModeDataPriority": epSpecificCodecClearModeDataPriority,
       "epSpecificCodecClearModePayloadType": epSpecificCodecClearModePayloadType,
       "epSpecificCodecClearModeMinPTime": epSpecificCodecClearModeMinPTime,
       "epSpecificCodecClearModeMaxPTime": epSpecificCodecClearModeMaxPTime,
       "codecClearChannelGroup": codecClearChannelGroup,
       "defaultCodecClearChannelVoiceEnable": defaultCodecClearChannelVoiceEnable,
       "defaultCodecClearChannelVoicePriority": defaultCodecClearChannelVoicePriority,
       "defaultCodecClearChannelDataEnable": defaultCodecClearChannelDataEnable,
       "defaultCodecClearChannelDataPriority": defaultCodecClearChannelDataPriority,
       "defaultCodecClearChannelPayloadType": defaultCodecClearChannelPayloadType,
       "defaultCodecClearChannelMinPTime": defaultCodecClearChannelMinPTime,
       "defaultCodecClearChannelMaxPTime": defaultCodecClearChannelMaxPTime,
       "epSpecificCodecClearChannelTable": epSpecificCodecClearChannelTable,
       "epSpecificCodecClearChannelEntry": epSpecificCodecClearChannelEntry,
       "epSpecificCodecClearChannelEpId": epSpecificCodecClearChannelEpId,
       "epSpecificCodecClearChannelEnableConfig": epSpecificCodecClearChannelEnableConfig,
       "epSpecificCodecClearChannelVoiceEnable": epSpecificCodecClearChannelVoiceEnable,
       "epSpecificCodecClearChannelVoicePriority": epSpecificCodecClearChannelVoicePriority,
       "epSpecificCodecClearChannelDataEnable": epSpecificCodecClearChannelDataEnable,
       "epSpecificCodecClearChannelDataPriority": epSpecificCodecClearChannelDataPriority,
       "epSpecificCodecClearChannelPayloadType": epSpecificCodecClearChannelPayloadType,
       "epSpecificCodecClearChannelMinPTime": epSpecificCodecClearChannelMinPTime,
       "epSpecificCodecClearChannelMaxPTime": epSpecificCodecClearChannelMaxPTime,
       "codecXCCDGroup": codecXCCDGroup,
       "defaultCodecXCCDVoiceEnable": defaultCodecXCCDVoiceEnable,
       "defaultCodecXCCDVoicePriority": defaultCodecXCCDVoicePriority,
       "defaultCodecXCCDDataEnable": defaultCodecXCCDDataEnable,
       "defaultCodecXCCDDataPriority": defaultCodecXCCDDataPriority,
       "defaultCodecXCCDPayloadType": defaultCodecXCCDPayloadType,
       "defaultCodecXCCDMinPTime": defaultCodecXCCDMinPTime,
       "defaultCodecXCCDMaxPTime": defaultCodecXCCDMaxPTime,
       "epSpecificCodecXCCDTable": epSpecificCodecXCCDTable,
       "epSpecificCodecXCCDEntry": epSpecificCodecXCCDEntry,
       "epSpecificCodecXCCDEpId": epSpecificCodecXCCDEpId,
       "epSpecificCodecXCCDEnableConfig": epSpecificCodecXCCDEnableConfig,
       "epSpecificCodecXCCDVoiceEnable": epSpecificCodecXCCDVoiceEnable,
       "epSpecificCodecXCCDVoicePriority": epSpecificCodecXCCDVoicePriority,
       "epSpecificCodecXCCDDataEnable": epSpecificCodecXCCDDataEnable,
       "epSpecificCodecXCCDDataPriority": epSpecificCodecXCCDDataPriority,
       "epSpecificCodecXCCDPayloadType": epSpecificCodecXCCDPayloadType,
       "epSpecificCodecXCCDMinPTime": epSpecificCodecXCCDMinPTime,
       "epSpecificCodecXCCDMaxPTime": epSpecificCodecXCCDMaxPTime,
       "jitterBufferGroup": jitterBufferGroup,
       "defaultJitterBufferLevel": defaultJitterBufferLevel,
       "defaultJitterBufferCustomMinLength": defaultJitterBufferCustomMinLength,
       "defaultJitterBufferCustomNomLength": defaultJitterBufferCustomNomLength,
       "defaultJitterBufferCustomMaxLength": defaultJitterBufferCustomMaxLength,
       "defaultVbdJitterBufferCustomMinLength": defaultVbdJitterBufferCustomMinLength,
       "defaultVbdJitterBufferCustomNomLength": defaultVbdJitterBufferCustomNomLength,
       "defaultVbdJitterBufferCustomMaxLength": defaultVbdJitterBufferCustomMaxLength,
       "defaultVbdJitterBufferType": defaultVbdJitterBufferType,
       "epSpecificJitterBufferTable": epSpecificJitterBufferTable,
       "epSpecificJitterBufferEntry": epSpecificJitterBufferEntry,
       "epSpecificJitterBufferEpId": epSpecificJitterBufferEpId,
       "epSpecificJitterBufferEnableConfig": epSpecificJitterBufferEnableConfig,
       "epSpecificJitterBufferLevel": epSpecificJitterBufferLevel,
       "epSpecificJitterBufferCustomMinLength": epSpecificJitterBufferCustomMinLength,
       "epSpecificJitterBufferCustomNomLength": epSpecificJitterBufferCustomNomLength,
       "epSpecificJitterBufferCustomMaxLength": epSpecificJitterBufferCustomMaxLength,
       "epSpecificJitterBufferCustomVbdMinLength": epSpecificJitterBufferCustomVbdMinLength,
       "epSpecificJitterBufferCustomVbdNomLength": epSpecificJitterBufferCustomVbdNomLength,
       "epSpecificJitterBufferCustomVbdMaxLength": epSpecificJitterBufferCustomVbdMaxLength,
       "epSpecificJitterBufferCustomVbdJitterBufferType": epSpecificJitterBufferCustomVbdJitterBufferType,
       "dtmfTransportGroup": dtmfTransportGroup,
       "defaultDtmfTransportMethod": defaultDtmfTransportMethod,
       "defaultDtmfTransportPayloadType": defaultDtmfTransportPayloadType,
       "epSpecificDtmfTransportTable": epSpecificDtmfTransportTable,
       "epSpecificDtmfTransportEntry": epSpecificDtmfTransportEntry,
       "epSpecificDtmfTransportEpId": epSpecificDtmfTransportEpId,
       "epSpecificDtmfTransportEnableConfig": epSpecificDtmfTransportEnableConfig,
       "epSpecificDtmfTransportMethod": epSpecificDtmfTransportMethod,
       "epSpecificDtmfTransportPayloadType": epSpecificDtmfTransportPayloadType,
       "ipTransportGroup": ipTransportGroup,
       "ipTransportRtpGroup": ipTransportRtpGroup,
       "ipTransportRtpBasePort": ipTransportRtpBasePort,
       "ipTransportSrtpBasePort": ipTransportSrtpBasePort,
       "ipTransportT38Group": ipTransportT38Group,
       "ipTransportT38BasePort": ipTransportT38BasePort,
       "codecVsBearerCapabilitiesMapping": codecVsBearerCapabilitiesMapping,
       "defaultCodecVsBearerCapabilitiesMappingTable": defaultCodecVsBearerCapabilitiesMappingTable,
       "defaultCodecVsBearerCapabilitiesMappingEntry": defaultCodecVsBearerCapabilitiesMappingEntry,
       "defaultCodecVsBearerCapabilitiesMappingIndex": defaultCodecVsBearerCapabilitiesMappingIndex,
       "defaultCodecVsBearerCapabilitiesMappingEnableMap": defaultCodecVsBearerCapabilitiesMappingEnableMap,
       "defaultCodecVsBearerCapabilitiesMappingCodec": defaultCodecVsBearerCapabilitiesMappingCodec,
       "defaultCodecVsBearerCapabilitiesMappingInformationTransferCap": defaultCodecVsBearerCapabilitiesMappingInformationTransferCap,
       "defaultCodecVsBearerCapabilitiesMappingMappingType": defaultCodecVsBearerCapabilitiesMappingMappingType,
       "securityGroup": securityGroup,
       "defaultSecurityRtpMode": defaultSecurityRtpMode,
       "defaultSecurityKeyManagement": defaultSecurityKeyManagement,
       "defaultSecurityRtpEncryption": defaultSecurityRtpEncryption,
       "allowUnsecureT38WithSrtp": allowUnsecureT38WithSrtp,
       "sessionUpdateCryptoMode": sessionUpdateCryptoMode,
       "epSpecificSecurityTable": epSpecificSecurityTable,
       "epSpecificSecurityEntry": epSpecificSecurityEntry,
       "epSpecificSecurityEpId": epSpecificSecurityEpId,
       "epSpecificSecurityEnableConfig": epSpecificSecurityEnableConfig,
       "epSpecificSecurityRtpMode": epSpecificSecurityRtpMode,
       "epSpecificSecurityKeyManagement": epSpecificSecurityKeyManagement,
       "epSpecificSecurityRtpEncryption": epSpecificSecurityRtpEncryption,
       "statisticsGroup": statisticsGroup,
       "lastConnectionsStatsTable": lastConnectionsStatsTable,
       "lastConnectionsStatsEntry": lastConnectionsStatsEntry,
       "lastConnectionsStatsConnectionsIndex": lastConnectionsStatsConnectionsIndex,
       "lastConnectionsStatsOctetsTransmitted": lastConnectionsStatsOctetsTransmitted,
       "lastConnectionsStatsOctetsReceived": lastConnectionsStatsOctetsReceived,
       "lastConnectionsStatsPacketsTransmitted": lastConnectionsStatsPacketsTransmitted,
       "lastConnectionsStatsPacketsReceived": lastConnectionsStatsPacketsReceived,
       "lastConnectionsStatsPacketsLost": lastConnectionsStatsPacketsLost,
       "lastConnectionsStatsMinimumInterarrivalJitter": lastConnectionsStatsMinimumInterarrivalJitter,
       "lastConnectionsStatsMaximumInterarrivalJitter": lastConnectionsStatsMaximumInterarrivalJitter,
       "lastConnectionsStatsAverageInterarrivalJitter": lastConnectionsStatsAverageInterarrivalJitter,
       "lastConnectionsStatsMinimumLatency": lastConnectionsStatsMinimumLatency,
       "lastConnectionsStatsMaximumLatency": lastConnectionsStatsMaximumLatency,
       "lastConnectionsStatsAverageLatency": lastConnectionsStatsAverageLatency,
       "lastPeriodsStatsTable": lastPeriodsStatsTable,
       "lastPeriodsStatsEntry": lastPeriodsStatsEntry,
       "lastPeriodsStatsPeriodIndex": lastPeriodsStatsPeriodIndex,
       "lastPeriodsStatsOctetsTransmitted": lastPeriodsStatsOctetsTransmitted,
       "lastPeriodsStatsOctetsReceived": lastPeriodsStatsOctetsReceived,
       "lastPeriodsStatsPacketsTransmitted": lastPeriodsStatsPacketsTransmitted,
       "lastPeriodsStatsPacketsReceived": lastPeriodsStatsPacketsReceived,
       "lastPeriodsStatsPacketsLost": lastPeriodsStatsPacketsLost,
       "lastPeriodsStatsMinimumInterarrivalJitter": lastPeriodsStatsMinimumInterarrivalJitter,
       "lastPeriodsStatsMaximumInterarrivalJitter": lastPeriodsStatsMaximumInterarrivalJitter,
       "lastPeriodsStatsAverageInterarrivalJitter": lastPeriodsStatsAverageInterarrivalJitter,
       "lastPeriodsStatsMinimumLatency": lastPeriodsStatsMinimumLatency,
       "lastPeriodsStatsMaximumLatency": lastPeriodsStatsMaximumLatency,
       "lastPeriodsStatsAverageLatency": lastPeriodsStatsAverageLatency,
       "lastPeriodsStatsPeriodBeginning": lastPeriodsStatsPeriodBeginning,
       "lastPeriodsStatsPeriodEnd": lastPeriodsStatsPeriodEnd,
       "channelStatisticsTable": channelStatisticsTable,
       "channelStatisticsEntry": channelStatisticsEntry,
       "channelStatisticsEpChannelId": channelStatisticsEpChannelId,
       "channelStatisticsPacketsSent": channelStatisticsPacketsSent,
       "channelStatisticsPacketsReceived": channelStatisticsPacketsReceived,
       "channelStatisticsBytesSent": channelStatisticsBytesSent,
       "channelStatisticsBytesReceived": channelStatisticsBytesReceived,
       "channelStatisticsAverageReceiveInterarrivalJitter": channelStatisticsAverageReceiveInterarrivalJitter,
       "channelStatisticsReset": channelStatisticsReset,
       "statsCollectionPeriodDuration": statsCollectionPeriodDuration,
       "statsPerConnectionNotificationEnable": statsPerConnectionNotificationEnable,
       "statsPerPeriodNotificationEnable": statsPerPeriodNotificationEnable,
       "interopGroup": interopGroup,
       "enforceSymmetricRtpEnable": enforceSymmetricRtpEnable,
       "interopDtmfRtpInitialPacketQty": interopDtmfRtpInitialPacketQty,
       "interopPacketReceptionMode": interopPacketReceptionMode,
       "debugGroup": debugGroup,
       "pcmCaptureGroup": pcmCaptureGroup,
       "pcmCaptureEnable": pcmCaptureEnable,
       "pcmCaptureEndpoint": pcmCaptureEndpoint,
       "pcmCaptureIpAddr": pcmCaptureIpAddr,
       "dspTracingGroup": dspTracingGroup,
       "dspTracingEnable": dspTracingEnable,
       "dspStatsGroup": dspStatsGroup,
       "dspStatsEnable": dspStatsEnable,
       "dspStatsInterval": dspStatsInterval,
       "dspStatsFilter": dspStatsFilter,
       "notificationsGroup": notificationsGroup,
       "minSeverity": minSeverity,
       "configurationGroup": configurationGroup,
       "needRestartInfo": needRestartInfo}
)
