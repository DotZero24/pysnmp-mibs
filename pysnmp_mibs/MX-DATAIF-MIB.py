# SNMP MIB module (MX-DATAIF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-DATAIF-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:05:52 2025
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

(mediatrixConfig,) = mibBuilder.importSymbols(
    "MX-SMI",
    "mediatrixConfig")

(MxEnableState,) = mibBuilder.importSymbols(
    "MX-TC",
    "MxEnableState")

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

dataIfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 35)
)
if mibBuilder.loadTexts:
    dataIfMIB.setRevisions(
        ("2010-02-16 00:00",
         "2009-09-10 00:00",
         "2009-06-12 00:00",
         "2005-05-10 00:00",
         "2005-04-29 00:00",
         "2005-04-28 00:00",
         "2005-04-19 00:00",
         "2005-03-17 00:00",
         "2005-03-16 00:00",
         "2005-03-15 00:00",
         "2005-02-18 00:00",
         "2004-02-18 00:00",
         "2003-10-27 00:00",
         "2003-10-22 00:00",
         "2003-10-02 00:00",
         "2003-09-15 00:00",
         "2003-02-20 00:00",
         "2003-12-18 00:00",
         "2002-09-30 00:00",
         "2002-07-24 00:00",
         "2002-04-26 00:00",
         "2001-08-22 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DataIfMIBObjects_ObjectIdentity = ObjectIdentity
dataIfMIBObjects = _DataIfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 35, 1)
)


class _DataIfT38BasePort_Type(Unsigned32):
    """Custom type dataIfT38BasePort based on Unsigned32"""
    defaultValue = 6004

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 64535),
    )


_DataIfT38BasePort_Type.__name__ = "Unsigned32"
_DataIfT38BasePort_Object = MibScalar
dataIfT38BasePort = _DataIfT38BasePort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 35, 1, 15),
    _DataIfT38BasePort_Type()
)
dataIfT38BasePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataIfT38BasePort.setStatus("current")
_DataIfTable_Object = MibTable
dataIfTable = _DataIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 35, 1, 18)
)
if mibBuilder.loadTexts:
    dataIfTable.setStatus("current")
_DataIfEntry_Object = MibTableRow
dataIfEntry = _DataIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 35, 1, 18, 50)
)
dataIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dataIfEntry.setStatus("current")


class _DataIfCngToneDetectionEnable_Type(MxEnableState):
    """Custom type dataIfCngToneDetectionEnable based on MxEnableState"""
    defaultValue = 1


_DataIfCngToneDetectionEnable_Type.__name__ = "MxEnableState"
_DataIfCngToneDetectionEnable_Object = MibTableColumn
dataIfCngToneDetectionEnable = _DataIfCngToneDetectionEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 35, 1, 18, 50, 50),
    _DataIfCngToneDetectionEnable_Type()
)
dataIfCngToneDetectionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataIfCngToneDetectionEnable.setStatus("current")


class _DataIfCedFaxToneEnable_Type(MxEnableState):
    """Custom type dataIfCedFaxToneEnable based on MxEnableState"""
    defaultValue = 0


_DataIfCedFaxToneEnable_Type.__name__ = "MxEnableState"
_DataIfCedFaxToneEnable_Object = MibTableColumn
dataIfCedFaxToneEnable = _DataIfCedFaxToneEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 35, 1, 18, 50, 100),
    _DataIfCedFaxToneEnable_Type()
)
dataIfCedFaxToneEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataIfCedFaxToneEnable.setStatus("current")


class _DataIfAnalogCedDetectionBehavior_Type(Integer32):
    """Custom type dataIfAnalogCedDetectionBehavior based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("passthrough", 100),
          ("faxmode", 200))
    )


_DataIfAnalogCedDetectionBehavior_Type.__name__ = "Integer32"
_DataIfAnalogCedDetectionBehavior_Object = MibTableColumn
dataIfAnalogCedDetectionBehavior = _DataIfAnalogCedDetectionBehavior_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 35, 1, 18, 50, 150),
    _DataIfAnalogCedDetectionBehavior_Type()
)
dataIfAnalogCedDetectionBehavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataIfAnalogCedDetectionBehavior.setStatus("current")
_DataIfCodecTable_Object = MibTable
dataIfCodecTable = _DataIfCodecTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 35, 1, 20)
)
if mibBuilder.loadTexts:
    dataIfCodecTable.setStatus("current")
_DataIfCodecEntry_Object = MibTableRow
dataIfCodecEntry = _DataIfCodecEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 35, 1, 20, 1)
)
dataIfCodecEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dataIfCodecEntry.setStatus("current")


class _DataIfCodecMediaTypeImageEnable_Type(Integer32):
    """Custom type dataIfCodecMediaTypeImageEnable based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("pcmu", 1),
          ("pcma", 2),
          ("pcmu-pcma", 3),
          ("g726", 4),
          ("pcmu-g726", 5),
          ("pcma-g726", 6),
          ("pcmu-pcma-g726", 7))
    )


_DataIfCodecMediaTypeImageEnable_Type.__name__ = "Integer32"
_DataIfCodecMediaTypeImageEnable_Object = MibTableColumn
dataIfCodecMediaTypeImageEnable = _DataIfCodecMediaTypeImageEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 35, 1, 20, 1, 1),
    _DataIfCodecMediaTypeImageEnable_Type()
)
dataIfCodecMediaTypeImageEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataIfCodecMediaTypeImageEnable.setStatus("current")


class _DataIfClearChannelCodecPreferred_Type(Integer32):
    """Custom type dataIfClearChannelCodecPreferred based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("pcmu", 1),
          ("pcma", 2),
          ("g726-32kbs", 5),
          ("g726-40kbs", 6),
          ("noPreferredCodec", 7))
    )


_DataIfClearChannelCodecPreferred_Type.__name__ = "Integer32"
_DataIfClearChannelCodecPreferred_Object = MibTableColumn
dataIfClearChannelCodecPreferred = _DataIfClearChannelCodecPreferred_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 35, 1, 20, 1, 2),
    _DataIfClearChannelCodecPreferred_Type()
)
dataIfClearChannelCodecPreferred.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataIfClearChannelCodecPreferred.setStatus("current")


class _DataIfCodecT38Enable_Type(Integer32):
    """Custom type dataIfCodecT38Enable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("signalingProtocolDependent", 2))
    )


_DataIfCodecT38Enable_Type.__name__ = "Integer32"
_DataIfCodecT38Enable_Object = MibTableColumn
dataIfCodecT38Enable = _DataIfCodecT38Enable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 35, 1, 20, 1, 5),
    _DataIfCodecT38Enable_Type()
)
dataIfCodecT38Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataIfCodecT38Enable.setStatus("current")


class _DataIfCodecT38ProtectionLevel_Type(Unsigned32):
    """Custom type dataIfCodecT38ProtectionLevel based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_DataIfCodecT38ProtectionLevel_Type.__name__ = "Unsigned32"
_DataIfCodecT38ProtectionLevel_Object = MibTableColumn
dataIfCodecT38ProtectionLevel = _DataIfCodecT38ProtectionLevel_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 35, 1, 20, 1, 6),
    _DataIfCodecT38ProtectionLevel_Type()
)
dataIfCodecT38ProtectionLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataIfCodecT38ProtectionLevel.setStatus("current")


class _DataIfT38FinalFramesRedundancy_Type(Unsigned32):
    """Custom type dataIfT38FinalFramesRedundancy based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_DataIfT38FinalFramesRedundancy_Type.__name__ = "Unsigned32"
_DataIfT38FinalFramesRedundancy_Object = MibScalar
dataIfT38FinalFramesRedundancy = _DataIfT38FinalFramesRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 35, 1, 40),
    _DataIfT38FinalFramesRedundancy_Type()
)
dataIfT38FinalFramesRedundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataIfT38FinalFramesRedundancy.setStatus("current")


class _DataIfT38NoSignalEnable_Type(MxEnableState):
    """Custom type dataIfT38NoSignalEnable based on MxEnableState"""
    defaultValue = 0


_DataIfT38NoSignalEnable_Type.__name__ = "MxEnableState"
_DataIfT38NoSignalEnable_Object = MibScalar
dataIfT38NoSignalEnable = _DataIfT38NoSignalEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 35, 1, 90),
    _DataIfT38NoSignalEnable_Type()
)
dataIfT38NoSignalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataIfT38NoSignalEnable.setStatus("current")


class _DataIfT38NoSignalTimeout_Type(Unsigned32):
    """Custom type dataIfT38NoSignalTimeout based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DataIfT38NoSignalTimeout_Type.__name__ = "Unsigned32"
_DataIfT38NoSignalTimeout_Object = MibScalar
dataIfT38NoSignalTimeout = _DataIfT38NoSignalTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 35, 1, 140),
    _DataIfT38NoSignalTimeout_Type()
)
dataIfT38NoSignalTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataIfT38NoSignalTimeout.setStatus("current")
_DataIfConformance_ObjectIdentity = ObjectIdentity
dataIfConformance = _DataIfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 35, 2)
)
_DataIfCompliances_ObjectIdentity = ObjectIdentity
dataIfCompliances = _DataIfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 35, 2, 1)
)
_DataIfGroups_ObjectIdentity = ObjectIdentity
dataIfGroups = _DataIfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 35, 2, 2)
)

# Managed Objects groups

dataIfGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 35, 2, 2, 1)
)
dataIfGroupVer1.setObjects(
      *(("MX-DATAIF-MIB", "dataIfCngToneDetectionEnable"),
        ("MX-DATAIF-MIB", "dataIfCedFaxToneEnable"),
        ("MX-DATAIF-MIB", "dataIfAnalogCedDetectionBehavior"),
        ("MX-DATAIF-MIB", "dataIfCodecT38Enable"),
        ("MX-DATAIF-MIB", "dataIfCodecMediaTypeImageEnable"),
        ("MX-DATAIF-MIB", "dataIfClearChannelCodecPreferred"),
        ("MX-DATAIF-MIB", "dataIfCodecT38ProtectionLevel"),
        ("MX-DATAIF-MIB", "dataIfT38FinalFramesRedundancy"),
        ("MX-DATAIF-MIB", "dataIfT38NoSignalEnable"),
        ("MX-DATAIF-MIB", "dataIfT38NoSignalTimeout"),
        ("MX-DATAIF-MIB", "dataIfT38BasePort"))
)
if mibBuilder.loadTexts:
    dataIfGroupVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dataIfComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 15, 35, 2, 1, 1)
)
dataIfComplVer1.setObjects(
    ("MX-DATAIF-MIB", "dataIfGroupVer1")
)
if mibBuilder.loadTexts:
    dataIfComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-DATAIF-MIB",
    **{"dataIfMIB": dataIfMIB,
       "dataIfMIBObjects": dataIfMIBObjects,
       "dataIfT38BasePort": dataIfT38BasePort,
       "dataIfTable": dataIfTable,
       "dataIfEntry": dataIfEntry,
       "dataIfCngToneDetectionEnable": dataIfCngToneDetectionEnable,
       "dataIfCedFaxToneEnable": dataIfCedFaxToneEnable,
       "dataIfAnalogCedDetectionBehavior": dataIfAnalogCedDetectionBehavior,
       "dataIfCodecTable": dataIfCodecTable,
       "dataIfCodecEntry": dataIfCodecEntry,
       "dataIfCodecMediaTypeImageEnable": dataIfCodecMediaTypeImageEnable,
       "dataIfClearChannelCodecPreferred": dataIfClearChannelCodecPreferred,
       "dataIfCodecT38Enable": dataIfCodecT38Enable,
       "dataIfCodecT38ProtectionLevel": dataIfCodecT38ProtectionLevel,
       "dataIfT38FinalFramesRedundancy": dataIfT38FinalFramesRedundancy,
       "dataIfT38NoSignalEnable": dataIfT38NoSignalEnable,
       "dataIfT38NoSignalTimeout": dataIfT38NoSignalTimeout,
       "dataIfConformance": dataIfConformance,
       "dataIfCompliances": dataIfCompliances,
       "dataIfComplVer1": dataIfComplVer1,
       "dataIfGroups": dataIfGroups,
       "dataIfGroupVer1": dataIfGroupVer1}
)
