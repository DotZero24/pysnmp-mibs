# SNMP MIB module (LUM-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-SYSTEM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:56 2025
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

(lumModules,
 lumSystemMIB) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumModules",
    "lumSystemMIB")

(CommandString,
 EnableDisable,
 FaultStatus,
 OnOff,
 Platform) = mibBuilder.importSymbols(
    "LUM-TC",
    "CommandString",
    "EnableDisable",
    "FaultStatus",
    "OnOff",
    "Platform")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TestAndIncr) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr")


# MODULE-IDENTITY

lumSystemMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 4)
)
if mibBuilder.loadTexts:
    lumSystemMIBModule.setRevisions(
        ("2018-12-21 00:00",
         "2018-09-28 00:00",
         "2017-12-08 00:00",
         "2017-06-15 00:00",
         "2016-11-30 00:00",
         "2016-06-14 00:00",
         "2014-05-16 00:00",
         "2013-11-15 00:00",
         "2010-08-03 00:00",
         "2008-08-05 00:00",
         "2005-09-14 00:00",
         "2004-10-01 00:00",
         "2004-06-30 00:00",
         "2004-05-26 00:00",
         "2003-08-03 00:00",
         "2002-12-13 00:00",
         "2002-04-18 00:00",
         "2002-01-11 00:00",
         "2001-08-14 00:00",
         "2001-07-26 00:00",
         "2001-04-26 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LumSystemConfs_ObjectIdentity = ObjectIdentity
lumSystemConfs = _LumSystemConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1)
)
_LumSystemGroups_ObjectIdentity = ObjectIdentity
lumSystemGroups = _LumSystemGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1)
)
_LumSystemCompl_ObjectIdentity = ObjectIdentity
lumSystemCompl = _LumSystemCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2)
)
_LumSystemMinimalGroups_ObjectIdentity = ObjectIdentity
lumSystemMinimalGroups = _LumSystemMinimalGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 3)
)
_LumSystemMinimalCompl_ObjectIdentity = ObjectIdentity
lumSystemMinimalCompl = _LumSystemMinimalCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 4)
)
_LumSystemMIBObjects_ObjectIdentity = ObjectIdentity
lumSystemMIBObjects = _LumSystemMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2)
)
_SysGeneral_ObjectIdentity = ObjectIdentity
sysGeneral = _SysGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 1)
)
_SysGeneralTestAndIncr_Type = TestAndIncr
_SysGeneralTestAndIncr_Object = MibScalar
sysGeneralTestAndIncr = _SysGeneralTestAndIncr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 1, 1),
    _SysGeneralTestAndIncr_Type()
)
sysGeneralTestAndIncr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysGeneralTestAndIncr.setStatus("current")


class _SysGeneralMibSpecVersion_Type(DisplayString):
    """Custom type sysGeneralMibSpecVersion based on DisplayString"""
    defaultValue = OctetString("")


_SysGeneralMibSpecVersion_Type.__name__ = "DisplayString"
_SysGeneralMibSpecVersion_Object = MibScalar
sysGeneralMibSpecVersion = _SysGeneralMibSpecVersion_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 1, 2),
    _SysGeneralMibSpecVersion_Type()
)
sysGeneralMibSpecVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysGeneralMibSpecVersion.setStatus("current")


class _SysGeneralMibImplVersion_Type(DisplayString):
    """Custom type sysGeneralMibImplVersion based on DisplayString"""
    defaultValue = OctetString("")


_SysGeneralMibImplVersion_Type.__name__ = "DisplayString"
_SysGeneralMibImplVersion_Object = MibScalar
sysGeneralMibImplVersion = _SysGeneralMibImplVersion_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 1, 3),
    _SysGeneralMibImplVersion_Type()
)
sysGeneralMibImplVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysGeneralMibImplVersion.setStatus("current")
_SysGeneralLastChangeTime_Type = DateAndTime
_SysGeneralLastChangeTime_Object = MibScalar
sysGeneralLastChangeTime = _SysGeneralLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 1, 4),
    _SysGeneralLastChangeTime_Type()
)
sysGeneralLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysGeneralLastChangeTime.setStatus("current")


class _SysGeneralTest_Type(Integer32):
    """Custom type sysGeneralTest based on Integer32"""
    defaultValue = 0


_SysGeneralTest_Type.__name__ = "Integer32"
_SysGeneralTest_Object = MibScalar
sysGeneralTest = _SysGeneralTest_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 1, 5),
    _SysGeneralTest_Type()
)
sysGeneralTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysGeneralTest.setStatus("deprecated")
_SysGeneralConfigLastChangeTime_Type = DateAndTime
_SysGeneralConfigLastChangeTime_Object = MibScalar
sysGeneralConfigLastChangeTime = _SysGeneralConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 1, 6),
    _SysGeneralConfigLastChangeTime_Type()
)
sysGeneralConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysGeneralConfigLastChangeTime.setStatus("current")


class _SysGeneralLoginRecords_Type(Integer32):
    """Custom type sysGeneralLoginRecords based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_SysGeneralLoginRecords_Type.__name__ = "Integer32"
_SysGeneralLoginRecords_Object = MibScalar
sysGeneralLoginRecords = _SysGeneralLoginRecords_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 1, 7),
    _SysGeneralLoginRecords_Type()
)
sysGeneralLoginRecords.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysGeneralLoginRecords.setStatus("current")
_SysGeneralUserTableSize_Type = Unsigned32
_SysGeneralUserTableSize_Object = MibScalar
sysGeneralUserTableSize = _SysGeneralUserTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 1, 8),
    _SysGeneralUserTableSize_Type()
)
sysGeneralUserTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysGeneralUserTableSize.setStatus("current")


class _SysGeneralWriteTest_Type(DisplayString):
    """Custom type sysGeneralWriteTest based on DisplayString"""
    defaultValue = OctetString("")


_SysGeneralWriteTest_Type.__name__ = "DisplayString"
_SysGeneralWriteTest_Object = MibScalar
sysGeneralWriteTest = _SysGeneralWriteTest_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 1, 9),
    _SysGeneralWriteTest_Type()
)
sysGeneralWriteTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysGeneralWriteTest.setStatus("current")
_SysNode_ObjectIdentity = ObjectIdentity
sysNode = _SysNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 2)
)


class _SysNodeName_Type(DisplayString):
    """Custom type sysNodeName based on DisplayString"""
    defaultValue = OctetString("localhost.localdomain")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SysNodeName_Type.__name__ = "DisplayString"
_SysNodeName_Object = MibScalar
sysNodeName = _SysNodeName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 2, 1),
    _SysNodeName_Type()
)
sysNodeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysNodeName.setStatus("current")


class _SysNodeContact_Type(DisplayString):
    """Custom type sysNodeContact based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysNodeContact_Type.__name__ = "DisplayString"
_SysNodeContact_Object = MibScalar
sysNodeContact = _SysNodeContact_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 2, 2),
    _SysNodeContact_Type()
)
sysNodeContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysNodeContact.setStatus("current")


class _SysNodeLocation_Type(DisplayString):
    """Custom type sysNodeLocation based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysNodeLocation_Type.__name__ = "DisplayString"
_SysNodeLocation_Object = MibScalar
sysNodeLocation = _SysNodeLocation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 2, 3),
    _SysNodeLocation_Type()
)
sysNodeLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysNodeLocation.setStatus("current")
_SysNodeObjectId_Type = ObjectIdentifier
_SysNodeObjectId_Object = MibScalar
sysNodeObjectId = _SysNodeObjectId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 2, 4),
    _SysNodeObjectId_Type()
)
sysNodeObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysNodeObjectId.setStatus("current")


class _SysNodePrimaryNameServer_Type(DisplayString):
    """Custom type sysNodePrimaryNameServer based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysNodePrimaryNameServer_Type.__name__ = "DisplayString"
_SysNodePrimaryNameServer_Object = MibScalar
sysNodePrimaryNameServer = _SysNodePrimaryNameServer_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 2, 5),
    _SysNodePrimaryNameServer_Type()
)
sysNodePrimaryNameServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysNodePrimaryNameServer.setStatus("current")


class _SysNodeRunLevel_Type(Integer32):
    """Custom type sysNodeRunLevel based on Integer32"""
    defaultValue = 3

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
        *(("undefined", 0),
          ("halt", 1),
          ("single", 2),
          ("normal", 3),
          ("reboot", 4))
    )


_SysNodeRunLevel_Type.__name__ = "Integer32"
_SysNodeRunLevel_Object = MibScalar
sysNodeRunLevel = _SysNodeRunLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 2, 6),
    _SysNodeRunLevel_Type()
)
sysNodeRunLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysNodeRunLevel.setStatus("deprecated")


class _SysNodeSecondaryNameServer_Type(DisplayString):
    """Custom type sysNodeSecondaryNameServer based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysNodeSecondaryNameServer_Type.__name__ = "DisplayString"
_SysNodeSecondaryNameServer_Object = MibScalar
sysNodeSecondaryNameServer = _SysNodeSecondaryNameServer_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 2, 7),
    _SysNodeSecondaryNameServer_Type()
)
sysNodeSecondaryNameServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysNodeSecondaryNameServer.setStatus("current")


class _SysNodeUptime_Type(DisplayString):
    """Custom type sysNodeUptime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysNodeUptime_Type.__name__ = "DisplayString"
_SysNodeUptime_Object = MibScalar
sysNodeUptime = _SysNodeUptime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 2, 8),
    _SysNodeUptime_Type()
)
sysNodeUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysNodeUptime.setStatus("current")


class _SysNodeNeType_Type(DisplayString):
    """Custom type sysNodeNeType based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysNodeNeType_Type.__name__ = "DisplayString"
_SysNodeNeType_Object = MibScalar
sysNodeNeType = _SysNodeNeType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 2, 9),
    _SysNodeNeType_Type()
)
sysNodeNeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysNodeNeType.setStatus("current")


class _SysNodeNeUserName_Type(DisplayString):
    """Custom type sysNodeNeUserName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysNodeNeUserName_Type.__name__ = "DisplayString"
_SysNodeNeUserName_Object = MibScalar
sysNodeNeUserName = _SysNodeNeUserName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 2, 10),
    _SysNodeNeUserName_Type()
)
sysNodeNeUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysNodeNeUserName.setStatus("current")


class _SysNodeNeDistinguishedName_Type(DisplayString):
    """Custom type sysNodeNeDistinguishedName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysNodeNeDistinguishedName_Type.__name__ = "DisplayString"
_SysNodeNeDistinguishedName_Object = MibScalar
sysNodeNeDistinguishedName = _SysNodeNeDistinguishedName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 2, 11),
    _SysNodeNeDistinguishedName_Type()
)
sysNodeNeDistinguishedName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysNodeNeDistinguishedName.setStatus("current")
_SysNodeBootTime_Type = DateAndTime
_SysNodeBootTime_Object = MibScalar
sysNodeBootTime = _SysNodeBootTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 2, 12),
    _SysNodeBootTime_Type()
)
sysNodeBootTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysNodeBootTime.setStatus("current")


class _SysNodeLocale_Type(DisplayString):
    """Custom type sysNodeLocale based on DisplayString"""
    defaultValue = OctetString("C")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysNodeLocale_Type.__name__ = "DisplayString"
_SysNodeLocale_Object = MibScalar
sysNodeLocale = _SysNodeLocale_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 2, 13),
    _SysNodeLocale_Type()
)
sysNodeLocale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysNodeLocale.setStatus("current")


class _SysNodeVersion_Type(DisplayString):
    """Custom type sysNodeVersion based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysNodeVersion_Type.__name__ = "DisplayString"
_SysNodeVersion_Object = MibScalar
sysNodeVersion = _SysNodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 2, 14),
    _SysNodeVersion_Type()
)
sysNodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysNodeVersion.setStatus("current")


class _SysNodeCLLI_Type(DisplayString):
    """Custom type sysNodeCLLI based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysNodeCLLI_Type.__name__ = "DisplayString"
_SysNodeCLLI_Object = MibScalar
sysNodeCLLI = _SysNodeCLLI_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 2, 15),
    _SysNodeCLLI_Type()
)
sysNodeCLLI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysNodeCLLI.setStatus("current")


class _SysNodeFIC_Type(DisplayString):
    """Custom type sysNodeFIC based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysNodeFIC_Type.__name__ = "DisplayString"
_SysNodeFIC_Object = MibScalar
sysNodeFIC = _SysNodeFIC_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 2, 16),
    _SysNodeFIC_Type()
)
sysNodeFIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysNodeFIC.setStatus("current")


class _SysNodeTID_Type(DisplayString):
    """Custom type sysNodeTID based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysNodeTID_Type.__name__ = "DisplayString"
_SysNodeTID_Object = MibScalar
sysNodeTID = _SysNodeTID_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 2, 17),
    _SysNodeTID_Type()
)
sysNodeTID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysNodeTID.setStatus("current")


class _SysNodeLatitude_Type(DisplayString):
    """Custom type sysNodeLatitude based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysNodeLatitude_Type.__name__ = "DisplayString"
_SysNodeLatitude_Object = MibScalar
sysNodeLatitude = _SysNodeLatitude_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 2, 18),
    _SysNodeLatitude_Type()
)
sysNodeLatitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysNodeLatitude.setStatus("current")


class _SysNodeLongitude_Type(DisplayString):
    """Custom type sysNodeLongitude based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysNodeLongitude_Type.__name__ = "DisplayString"
_SysNodeLongitude_Object = MibScalar
sysNodeLongitude = _SysNodeLongitude_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 2, 19),
    _SysNodeLongitude_Type()
)
sysNodeLongitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysNodeLongitude.setStatus("current")
_SysHostList_ObjectIdentity = ObjectIdentity
sysHostList = _SysHostList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 3)
)
_SysHostTable_Object = MibTable
sysHostTable = _SysHostTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    sysHostTable.setStatus("current")
_SysHostEntry_Object = MibTableRow
sysHostEntry = _SysHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 3, 1, 1)
)
sysHostEntry.setIndexNames(
    (0, "LUM-SYSTEM-MIB", "sysHostIndex"),
)
if mibBuilder.loadTexts:
    sysHostEntry.setStatus("current")


class _SysHostIndex_Type(Unsigned32):
    """Custom type sysHostIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SysHostIndex_Type.__name__ = "Unsigned32"
_SysHostIndex_Object = MibTableColumn
sysHostIndex = _SysHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 3, 1, 1, 1),
    _SysHostIndex_Type()
)
sysHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHostIndex.setStatus("current")


class _SysHostIpAddress_Type(DisplayString):
    """Custom type sysHostIpAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysHostIpAddress_Type.__name__ = "DisplayString"
_SysHostIpAddress_Object = MibTableColumn
sysHostIpAddress = _SysHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 3, 1, 1, 2),
    _SysHostIpAddress_Type()
)
sysHostIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysHostIpAddress.setStatus("current")


class _SysHostNames_Type(DisplayString):
    """Custom type sysHostNames based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysHostNames_Type.__name__ = "DisplayString"
_SysHostNames_Object = MibTableColumn
sysHostNames = _SysHostNames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 3, 1, 1, 3),
    _SysHostNames_Type()
)
sysHostNames.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysHostNames.setStatus("current")
_SysHostRowStatus_Type = RowStatus
_SysHostRowStatus_Object = MibTableColumn
sysHostRowStatus = _SysHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 3, 1, 1, 4),
    _SysHostRowStatus_Type()
)
sysHostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysHostRowStatus.setStatus("current")
_SysTime_ObjectIdentity = ObjectIdentity
sysTime = _SysTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 4)
)
_SysTimeLocal_Type = DateAndTime
_SysTimeLocal_Object = MibScalar
sysTimeLocal = _SysTimeLocal_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 4, 1),
    _SysTimeLocal_Type()
)
sysTimeLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTimeLocal.setStatus("current")


class _SysTimeZone_Type(DisplayString):
    """Custom type sysTimeZone based on DisplayString"""
    defaultValue = OctetString("CET")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysTimeZone_Type.__name__ = "DisplayString"
_SysTimeZone_Object = MibScalar
sysTimeZone = _SysTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 4, 2),
    _SysTimeZone_Type()
)
sysTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeZone.setStatus("current")


class _SysTimePrimaryServer_Type(DisplayString):
    """Custom type sysTimePrimaryServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysTimePrimaryServer_Type.__name__ = "DisplayString"
_SysTimePrimaryServer_Object = MibScalar
sysTimePrimaryServer = _SysTimePrimaryServer_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 4, 3),
    _SysTimePrimaryServer_Type()
)
sysTimePrimaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimePrimaryServer.setStatus("deprecated")


class _SysTimeSecondaryServer_Type(DisplayString):
    """Custom type sysTimeSecondaryServer based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysTimeSecondaryServer_Type.__name__ = "DisplayString"
_SysTimeSecondaryServer_Object = MibScalar
sysTimeSecondaryServer = _SysTimeSecondaryServer_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 4, 4),
    _SysTimeSecondaryServer_Type()
)
sysTimeSecondaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeSecondaryServer.setStatus("deprecated")
_SysTimeChangeLocalTime_Type = CommandString
_SysTimeChangeLocalTime_Object = MibScalar
sysTimeChangeLocalTime = _SysTimeChangeLocalTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 4, 5),
    _SysTimeChangeLocalTime_Type()
)
sysTimeChangeLocalTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeChangeLocalTime.setStatus("current")
_SysTimePrimaryIpAddress_Type = IpAddress
_SysTimePrimaryIpAddress_Object = MibScalar
sysTimePrimaryIpAddress = _SysTimePrimaryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 4, 6),
    _SysTimePrimaryIpAddress_Type()
)
sysTimePrimaryIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimePrimaryIpAddress.setStatus("current")
_SysTimeSecondaryIpAddress_Type = IpAddress
_SysTimeSecondaryIpAddress_Object = MibScalar
sysTimeSecondaryIpAddress = _SysTimeSecondaryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 4, 7),
    _SysTimeSecondaryIpAddress_Type()
)
sysTimeSecondaryIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeSecondaryIpAddress.setStatus("current")
_SysLogList_ObjectIdentity = ObjectIdentity
sysLogList = _SysLogList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 5)
)
_SysLogTable_Object = MibTable
sysLogTable = _SysLogTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 5, 1)
)
if mibBuilder.loadTexts:
    sysLogTable.setStatus("deprecated")
_SysLogEntry_Object = MibTableRow
sysLogEntry = _SysLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 5, 1, 1)
)
sysLogEntry.setIndexNames(
    (0, "LUM-SYSTEM-MIB", "sysLogIndex"),
)
if mibBuilder.loadTexts:
    sysLogEntry.setStatus("deprecated")


class _SysLogIndex_Type(Unsigned32):
    """Custom type sysLogIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SysLogIndex_Type.__name__ = "Unsigned32"
_SysLogIndex_Object = MibTableColumn
sysLogIndex = _SysLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 5, 1, 1, 1),
    _SysLogIndex_Type()
)
sysLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLogIndex.setStatus("deprecated")


class _SysLogSelection_Type(DisplayString):
    """Custom type sysLogSelection based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysLogSelection_Type.__name__ = "DisplayString"
_SysLogSelection_Object = MibTableColumn
sysLogSelection = _SysLogSelection_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 5, 1, 1, 2),
    _SysLogSelection_Type()
)
sysLogSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogSelection.setStatus("deprecated")


class _SysLogAction_Type(DisplayString):
    """Custom type sysLogAction based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysLogAction_Type.__name__ = "DisplayString"
_SysLogAction_Object = MibTableColumn
sysLogAction = _SysLogAction_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 5, 1, 1, 3),
    _SysLogAction_Type()
)
sysLogAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogAction.setStatus("deprecated")
_SysLogRowStatus_Type = RowStatus
_SysLogRowStatus_Object = MibTableColumn
sysLogRowStatus = _SysLogRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 5, 1, 1, 4),
    _SysLogRowStatus_Type()
)
sysLogRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogRowStatus.setStatus("deprecated")
_SysUserList_ObjectIdentity = ObjectIdentity
sysUserList = _SysUserList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 6)
)
_SysUserTable_Object = MibTable
sysUserTable = _SysUserTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 6, 1)
)
if mibBuilder.loadTexts:
    sysUserTable.setStatus("current")
_SysUserEntry_Object = MibTableRow
sysUserEntry = _SysUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 6, 1, 1)
)
sysUserEntry.setIndexNames(
    (0, "LUM-SYSTEM-MIB", "sysUserIndex"),
)
if mibBuilder.loadTexts:
    sysUserEntry.setStatus("current")


class _SysUserIndex_Type(Unsigned32):
    """Custom type sysUserIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SysUserIndex_Type.__name__ = "Unsigned32"
_SysUserIndex_Object = MibTableColumn
sysUserIndex = _SysUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 6, 1, 1, 1),
    _SysUserIndex_Type()
)
sysUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysUserIndex.setStatus("current")


class _SysUserName_Type(DisplayString):
    """Custom type sysUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SysUserName_Type.__name__ = "DisplayString"
_SysUserName_Object = MibTableColumn
sysUserName = _SysUserName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 6, 1, 1, 2),
    _SysUserName_Type()
)
sysUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysUserName.setStatus("current")


class _SysUserPasswd_Type(DisplayString):
    """Custom type sysUserPasswd based on DisplayString"""
    defaultValue = OctetString("1234567890")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysUserPasswd_Type.__name__ = "DisplayString"
_SysUserPasswd_Object = MibTableColumn
sysUserPasswd = _SysUserPasswd_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 6, 1, 1, 3),
    _SysUserPasswd_Type()
)
sysUserPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysUserPasswd.setStatus("deprecated")


class _SysUserDescr_Type(DisplayString):
    """Custom type sysUserDescr based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysUserDescr_Type.__name__ = "DisplayString"
_SysUserDescr_Object = MibTableColumn
sysUserDescr = _SysUserDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 6, 1, 1, 4),
    _SysUserDescr_Type()
)
sysUserDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysUserDescr.setStatus("current")
_SysUserLastChangeTime_Type = DateAndTime
_SysUserLastChangeTime_Object = MibTableColumn
sysUserLastChangeTime = _SysUserLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 6, 1, 1, 5),
    _SysUserLastChangeTime_Type()
)
sysUserLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysUserLastChangeTime.setStatus("deprecated")
_SysUserExpireTime_Type = DateAndTime
_SysUserExpireTime_Object = MibTableColumn
sysUserExpireTime = _SysUserExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 6, 1, 1, 6),
    _SysUserExpireTime_Type()
)
sysUserExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysUserExpireTime.setStatus("deprecated")
_SysUserRowStatus_Type = RowStatus
_SysUserRowStatus_Object = MibTableColumn
sysUserRowStatus = _SysUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 6, 1, 1, 7),
    _SysUserRowStatus_Type()
)
sysUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysUserRowStatus.setStatus("deprecated")


class _SysUserProfile_Type(DisplayString):
    """Custom type sysUserProfile based on DisplayString"""
    defaultValue = OctetString("operator")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysUserProfile_Type.__name__ = "DisplayString"
_SysUserProfile_Object = MibTableColumn
sysUserProfile = _SysUserProfile_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 6, 1, 1, 8),
    _SysUserProfile_Type()
)
sysUserProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysUserProfile.setStatus("current")
_SysUserUid_Type = Unsigned32
_SysUserUid_Object = MibTableColumn
sysUserUid = _SysUserUid_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 6, 1, 1, 9),
    _SysUserUid_Type()
)
sysUserUid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysUserUid.setStatus("current")


class _SysUserChangePassword_Type(CommandString):
    """Custom type sysUserChangePassword based on CommandString"""
    defaultValue = OctetString("1234567890")


_SysUserChangePassword_Type.__name__ = "CommandString"
_SysUserChangePassword_Object = MibTableColumn
sysUserChangePassword = _SysUserChangePassword_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 6, 1, 1, 10),
    _SysUserChangePassword_Type()
)
sysUserChangePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysUserChangePassword.setStatus("current")
_SysUserClearPassword_Type = CommandString
_SysUserClearPassword_Object = MibTableColumn
sysUserClearPassword = _SysUserClearPassword_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 6, 1, 1, 11),
    _SysUserClearPassword_Type()
)
sysUserClearPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysUserClearPassword.setStatus("current")
_SysUserDisable_Type = CommandString
_SysUserDisable_Object = MibTableColumn
sysUserDisable = _SysUserDisable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 6, 1, 1, 12),
    _SysUserDisable_Type()
)
sysUserDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysUserDisable.setStatus("current")
_SysUserEnable_Type = CommandString
_SysUserEnable_Object = MibTableColumn
sysUserEnable = _SysUserEnable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 6, 1, 1, 13),
    _SysUserEnable_Type()
)
sysUserEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysUserEnable.setStatus("current")


class _SysUserMode_Type(Integer32):
    """Custom type sysUserMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SysUserMode_Type.__name__ = "Integer32"
_SysUserMode_Object = MibTableColumn
sysUserMode = _SysUserMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 6, 1, 1, 14),
    _SysUserMode_Type()
)
sysUserMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysUserMode.setStatus("current")
_SysRadius_ObjectIdentity = ObjectIdentity
sysRadius = _SysRadius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 7)
)


class _SysRadiusPrimaryServer_Type(DisplayString):
    """Custom type sysRadiusPrimaryServer based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysRadiusPrimaryServer_Type.__name__ = "DisplayString"
_SysRadiusPrimaryServer_Object = MibScalar
sysRadiusPrimaryServer = _SysRadiusPrimaryServer_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 7, 1),
    _SysRadiusPrimaryServer_Type()
)
sysRadiusPrimaryServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysRadiusPrimaryServer.setStatus("deprecated")


class _SysRadiusPrimarySecret_Type(DisplayString):
    """Custom type sysRadiusPrimarySecret based on DisplayString"""
    defaultValue = OctetString("1234567890")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysRadiusPrimarySecret_Type.__name__ = "DisplayString"
_SysRadiusPrimarySecret_Object = MibScalar
sysRadiusPrimarySecret = _SysRadiusPrimarySecret_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 7, 2),
    _SysRadiusPrimarySecret_Type()
)
sysRadiusPrimarySecret.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysRadiusPrimarySecret.setStatus("current")


class _SysRadiusSecondaryServer_Type(DisplayString):
    """Custom type sysRadiusSecondaryServer based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysRadiusSecondaryServer_Type.__name__ = "DisplayString"
_SysRadiusSecondaryServer_Object = MibScalar
sysRadiusSecondaryServer = _SysRadiusSecondaryServer_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 7, 3),
    _SysRadiusSecondaryServer_Type()
)
sysRadiusSecondaryServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysRadiusSecondaryServer.setStatus("deprecated")


class _SysRadiusSecondarySecret_Type(DisplayString):
    """Custom type sysRadiusSecondarySecret based on DisplayString"""
    defaultValue = OctetString("1234567890")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysRadiusSecondarySecret_Type.__name__ = "DisplayString"
_SysRadiusSecondarySecret_Object = MibScalar
sysRadiusSecondarySecret = _SysRadiusSecondarySecret_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 7, 4),
    _SysRadiusSecondarySecret_Type()
)
sysRadiusSecondarySecret.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysRadiusSecondarySecret.setStatus("current")
_SysRadiusPrimaryIpAddress_Type = IpAddress
_SysRadiusPrimaryIpAddress_Object = MibScalar
sysRadiusPrimaryIpAddress = _SysRadiusPrimaryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 7, 5),
    _SysRadiusPrimaryIpAddress_Type()
)
sysRadiusPrimaryIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysRadiusPrimaryIpAddress.setStatus("current")
_SysRadiusSecondaryIpAddress_Type = IpAddress
_SysRadiusSecondaryIpAddress_Object = MibScalar
sysRadiusSecondaryIpAddress = _SysRadiusSecondaryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 7, 6),
    _SysRadiusSecondaryIpAddress_Type()
)
sysRadiusSecondaryIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysRadiusSecondaryIpAddress.setStatus("current")


class _SysRadiusPrimaryPort_Type(Unsigned32):
    """Custom type sysRadiusPrimaryPort based on Unsigned32"""
    defaultValue = 1812

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SysRadiusPrimaryPort_Type.__name__ = "Unsigned32"
_SysRadiusPrimaryPort_Object = MibScalar
sysRadiusPrimaryPort = _SysRadiusPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 7, 7),
    _SysRadiusPrimaryPort_Type()
)
sysRadiusPrimaryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysRadiusPrimaryPort.setStatus("current")


class _SysRadiusSecondaryPort_Type(Unsigned32):
    """Custom type sysRadiusSecondaryPort based on Unsigned32"""
    defaultValue = 1812

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SysRadiusSecondaryPort_Type.__name__ = "Unsigned32"
_SysRadiusSecondaryPort_Object = MibScalar
sysRadiusSecondaryPort = _SysRadiusSecondaryPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 7, 8),
    _SysRadiusSecondaryPort_Type()
)
sysRadiusSecondaryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysRadiusSecondaryPort.setStatus("current")


class _SysRadiusDefaultUserProfile_Type(DisplayString):
    """Custom type sysRadiusDefaultUserProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysRadiusDefaultUserProfile_Type.__name__ = "DisplayString"
_SysRadiusDefaultUserProfile_Object = MibScalar
sysRadiusDefaultUserProfile = _SysRadiusDefaultUserProfile_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 7, 9),
    _SysRadiusDefaultUserProfile_Type()
)
sysRadiusDefaultUserProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysRadiusDefaultUserProfile.setStatus("current")
_SysLicense_ObjectIdentity = ObjectIdentity
sysLicense = _SysLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 8)
)
_SysLicenseExpireDate_Type = DateAndTime
_SysLicenseExpireDate_Object = MibScalar
sysLicenseExpireDate = _SysLicenseExpireDate_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 8, 1),
    _SysLicenseExpireDate_Type()
)
sysLicenseExpireDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLicenseExpireDate.setStatus("current")


class _SysLicenseCustomer_Type(DisplayString):
    """Custom type sysLicenseCustomer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysLicenseCustomer_Type.__name__ = "DisplayString"
_SysLicenseCustomer_Object = MibScalar
sysLicenseCustomer = _SysLicenseCustomer_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 8, 2),
    _SysLicenseCustomer_Type()
)
sysLicenseCustomer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLicenseCustomer.setStatus("current")
_SysLicenseExpiresSoon_Type = FaultStatus
_SysLicenseExpiresSoon_Object = MibScalar
sysLicenseExpiresSoon = _SysLicenseExpiresSoon_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 8, 3),
    _SysLicenseExpiresSoon_Type()
)
sysLicenseExpiresSoon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLicenseExpiresSoon.setStatus("current")
_SysLicenseExpired_Type = FaultStatus
_SysLicenseExpired_Object = MibScalar
sysLicenseExpired = _SysLicenseExpired_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 8, 4),
    _SysLicenseExpired_Type()
)
sysLicenseExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLicenseExpired.setStatus("current")


class _SysLicenseExpiredCause_Type(Integer32):
    """Custom type sysLicenseExpiredCause based on Integer32"""
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
        *(("none", 0),
          ("missing", 1),
          ("invalid", 2),
          ("corrupt", 3),
          ("expired", 4))
    )


_SysLicenseExpiredCause_Type.__name__ = "Integer32"
_SysLicenseExpiredCause_Object = MibScalar
sysLicenseExpiredCause = _SysLicenseExpiredCause_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 8, 5),
    _SysLicenseExpiredCause_Type()
)
sysLicenseExpiredCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLicenseExpiredCause.setStatus("current")


class _SysLicenseFeatureEws_Type(Integer32):
    """Custom type sysLicenseFeatureEws based on Integer32"""
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
        *(("disabled", 1),
          ("enabled", 2),
          ("demo", 3),
          ("corrupt", 4),
          ("expired", 5))
    )


_SysLicenseFeatureEws_Type.__name__ = "Integer32"
_SysLicenseFeatureEws_Object = MibScalar
sysLicenseFeatureEws = _SysLicenseFeatureEws_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 8, 6),
    _SysLicenseFeatureEws_Type()
)
sysLicenseFeatureEws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLicenseFeatureEws.setStatus("current")


class _SysLicenseFeatureOspf_Type(Integer32):
    """Custom type sysLicenseFeatureOspf based on Integer32"""
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
        *(("disabled", 1),
          ("enabled", 2),
          ("demo", 3),
          ("corrupt", 4),
          ("expired", 5))
    )


_SysLicenseFeatureOspf_Type.__name__ = "Integer32"
_SysLicenseFeatureOspf_Object = MibScalar
sysLicenseFeatureOspf = _SysLicenseFeatureOspf_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 8, 7),
    _SysLicenseFeatureOspf_Type()
)
sysLicenseFeatureOspf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLicenseFeatureOspf.setStatus("current")


class _SysLicenseFeatureSnmp_Type(Integer32):
    """Custom type sysLicenseFeatureSnmp based on Integer32"""
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
        *(("disabled", 1),
          ("enabled", 2),
          ("demo", 3),
          ("corrupt", 4),
          ("expired", 5))
    )


_SysLicenseFeatureSnmp_Type.__name__ = "Integer32"
_SysLicenseFeatureSnmp_Object = MibScalar
sysLicenseFeatureSnmp = _SysLicenseFeatureSnmp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 8, 8),
    _SysLicenseFeatureSnmp_Type()
)
sysLicenseFeatureSnmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLicenseFeatureSnmp.setStatus("current")


class _SysLicenseFeatureGmpls_Type(Integer32):
    """Custom type sysLicenseFeatureGmpls based on Integer32"""
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
        *(("disabled", 1),
          ("enabled", 2),
          ("demo", 3),
          ("corrupt", 4),
          ("expired", 5))
    )


_SysLicenseFeatureGmpls_Type.__name__ = "Integer32"
_SysLicenseFeatureGmpls_Object = MibScalar
sysLicenseFeatureGmpls = _SysLicenseFeatureGmpls_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 8, 9),
    _SysLicenseFeatureGmpls_Type()
)
sysLicenseFeatureGmpls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLicenseFeatureGmpls.setStatus("current")


class _SysLicenseFeatureRudb_Type(Integer32):
    """Custom type sysLicenseFeatureRudb based on Integer32"""
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
        *(("disabled", 1),
          ("enabled", 2),
          ("demo", 3),
          ("corrupt", 4),
          ("expired", 5))
    )


_SysLicenseFeatureRudb_Type.__name__ = "Integer32"
_SysLicenseFeatureRudb_Object = MibScalar
sysLicenseFeatureRudb = _SysLicenseFeatureRudb_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 8, 10),
    _SysLicenseFeatureRudb_Type()
)
sysLicenseFeatureRudb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLicenseFeatureRudb.setStatus("current")
_SysLicenseInstallLicenseFile_Type = CommandString
_SysLicenseInstallLicenseFile_Object = MibScalar
sysLicenseInstallLicenseFile = _SysLicenseInstallLicenseFile_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 8, 11),
    _SysLicenseInstallLicenseFile_Type()
)
sysLicenseInstallLicenseFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLicenseInstallLicenseFile.setStatus("current")
_SysTacacs_ObjectIdentity = ObjectIdentity
sysTacacs = _SysTacacs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 9)
)


class _SysTacacsPrimaryServer_Type(DisplayString):
    """Custom type sysTacacsPrimaryServer based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysTacacsPrimaryServer_Type.__name__ = "DisplayString"
_SysTacacsPrimaryServer_Object = MibScalar
sysTacacsPrimaryServer = _SysTacacsPrimaryServer_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 9, 1),
    _SysTacacsPrimaryServer_Type()
)
sysTacacsPrimaryServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTacacsPrimaryServer.setStatus("deprecated")


class _SysTacacsSecondaryServer_Type(DisplayString):
    """Custom type sysTacacsSecondaryServer based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysTacacsSecondaryServer_Type.__name__ = "DisplayString"
_SysTacacsSecondaryServer_Object = MibScalar
sysTacacsSecondaryServer = _SysTacacsSecondaryServer_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 9, 2),
    _SysTacacsSecondaryServer_Type()
)
sysTacacsSecondaryServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTacacsSecondaryServer.setStatus("deprecated")


class _SysTacacsSecret_Type(DisplayString):
    """Custom type sysTacacsSecret based on DisplayString"""
    defaultValue = OctetString("1234567890")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysTacacsSecret_Type.__name__ = "DisplayString"
_SysTacacsSecret_Object = MibScalar
sysTacacsSecret = _SysTacacsSecret_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 9, 3),
    _SysTacacsSecret_Type()
)
sysTacacsSecret.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTacacsSecret.setStatus("current")


class _SysTacacsSecondarySecret_Type(DisplayString):
    """Custom type sysTacacsSecondarySecret based on DisplayString"""
    defaultValue = OctetString("1234567890")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysTacacsSecondarySecret_Type.__name__ = "DisplayString"
_SysTacacsSecondarySecret_Object = MibScalar
sysTacacsSecondarySecret = _SysTacacsSecondarySecret_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 9, 4),
    _SysTacacsSecondarySecret_Type()
)
sysTacacsSecondarySecret.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTacacsSecondarySecret.setStatus("current")
_SysTacacsPrimaryIpAddress_Type = IpAddress
_SysTacacsPrimaryIpAddress_Object = MibScalar
sysTacacsPrimaryIpAddress = _SysTacacsPrimaryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 9, 5),
    _SysTacacsPrimaryIpAddress_Type()
)
sysTacacsPrimaryIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTacacsPrimaryIpAddress.setStatus("current")
_SysTacacsSecondaryIpAddress_Type = IpAddress
_SysTacacsSecondaryIpAddress_Object = MibScalar
sysTacacsSecondaryIpAddress = _SysTacacsSecondaryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 9, 6),
    _SysTacacsSecondaryIpAddress_Type()
)
sysTacacsSecondaryIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTacacsSecondaryIpAddress.setStatus("current")
_SysAudit_ObjectIdentity = ObjectIdentity
sysAudit = _SysAudit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 10)
)
_SysSecurity_ObjectIdentity = ObjectIdentity
sysSecurity = _SysSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 11)
)


class _SysSecurityLocalConsoleAccess_Type(Integer32):
    """Custom type sysSecurityLocalConsoleAccess based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("bootdisabled", 3))
    )


_SysSecurityLocalConsoleAccess_Type.__name__ = "Integer32"
_SysSecurityLocalConsoleAccess_Object = MibScalar
sysSecurityLocalConsoleAccess = _SysSecurityLocalConsoleAccess_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 11, 1),
    _SysSecurityLocalConsoleAccess_Type()
)
sysSecurityLocalConsoleAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSecurityLocalConsoleAccess.setStatus("current")
_SysSecurityChangeLocalConsoleAccess_Type = CommandString
_SysSecurityChangeLocalConsoleAccess_Object = MibScalar
sysSecurityChangeLocalConsoleAccess = _SysSecurityChangeLocalConsoleAccess_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 11, 2),
    _SysSecurityChangeLocalConsoleAccess_Type()
)
sysSecurityChangeLocalConsoleAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSecurityChangeLocalConsoleAccess.setStatus("current")


class _SysSecurityIpTablesStatus_Type(Integer32):
    """Custom type sysSecurityIpTablesStatus based on Integer32"""
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
        *(("unavailable", 1),
          ("unsecure", 2),
          ("secure", 3))
    )


_SysSecurityIpTablesStatus_Type.__name__ = "Integer32"
_SysSecurityIpTablesStatus_Object = MibScalar
sysSecurityIpTablesStatus = _SysSecurityIpTablesStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 11, 3),
    _SysSecurityIpTablesStatus_Type()
)
sysSecurityIpTablesStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSecurityIpTablesStatus.setStatus("current")


class _SysSecurityLocalCraftAccess_Type(EnableDisable):
    """Custom type sysSecurityLocalCraftAccess based on EnableDisable"""
    defaultValue = 2


_SysSecurityLocalCraftAccess_Type.__name__ = "EnableDisable"
_SysSecurityLocalCraftAccess_Object = MibScalar
sysSecurityLocalCraftAccess = _SysSecurityLocalCraftAccess_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 11, 4),
    _SysSecurityLocalCraftAccess_Type()
)
sysSecurityLocalCraftAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSecurityLocalCraftAccess.setStatus("current")
_SysSecurityChangeLocalCraftAccess_Type = CommandString
_SysSecurityChangeLocalCraftAccess_Object = MibScalar
sysSecurityChangeLocalCraftAccess = _SysSecurityChangeLocalCraftAccess_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 11, 5),
    _SysSecurityChangeLocalCraftAccess_Type()
)
sysSecurityChangeLocalCraftAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSecurityChangeLocalCraftAccess.setStatus("current")


class _SysSecurityAuthenticationOrder_Type(Integer32):
    """Custom type sysSecurityAuthenticationOrder based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("localFirst", 1),
          ("remoteFirst", 2),
          ("strictRemoteFirst", 3))
    )


_SysSecurityAuthenticationOrder_Type.__name__ = "Integer32"
_SysSecurityAuthenticationOrder_Object = MibScalar
sysSecurityAuthenticationOrder = _SysSecurityAuthenticationOrder_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 11, 6),
    _SysSecurityAuthenticationOrder_Type()
)
sysSecurityAuthenticationOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSecurityAuthenticationOrder.setStatus("current")


class _SysSecurityFileSystemAccessRestrictions_Type(EnableDisable):
    """Custom type sysSecurityFileSystemAccessRestrictions based on EnableDisable"""
    defaultValue = 1


_SysSecurityFileSystemAccessRestrictions_Type.__name__ = "EnableDisable"
_SysSecurityFileSystemAccessRestrictions_Object = MibScalar
sysSecurityFileSystemAccessRestrictions = _SysSecurityFileSystemAccessRestrictions_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 11, 7),
    _SysSecurityFileSystemAccessRestrictions_Type()
)
sysSecurityFileSystemAccessRestrictions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSecurityFileSystemAccessRestrictions.setStatus("current")


class _SysSecurityCUFrontICNPortAccess_Type(EnableDisable):
    """Custom type sysSecurityCUFrontICNPortAccess based on EnableDisable"""
    defaultValue = 2


_SysSecurityCUFrontICNPortAccess_Type.__name__ = "EnableDisable"
_SysSecurityCUFrontICNPortAccess_Object = MibScalar
sysSecurityCUFrontICNPortAccess = _SysSecurityCUFrontICNPortAccess_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 11, 8),
    _SysSecurityCUFrontICNPortAccess_Type()
)
sysSecurityCUFrontICNPortAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSecurityCUFrontICNPortAccess.setStatus("current")
_SysSecurityChangeCUFrontICNPortAccess_Type = CommandString
_SysSecurityChangeCUFrontICNPortAccess_Object = MibScalar
sysSecurityChangeCUFrontICNPortAccess = _SysSecurityChangeCUFrontICNPortAccess_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 11, 9),
    _SysSecurityChangeCUFrontICNPortAccess_Type()
)
sysSecurityChangeCUFrontICNPortAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSecurityChangeCUFrontICNPortAccess.setStatus("current")


class _SysSecuritySubrackICNPortAccess_Type(EnableDisable):
    """Custom type sysSecuritySubrackICNPortAccess based on EnableDisable"""
    defaultValue = 2


_SysSecuritySubrackICNPortAccess_Type.__name__ = "EnableDisable"
_SysSecuritySubrackICNPortAccess_Object = MibScalar
sysSecuritySubrackICNPortAccess = _SysSecuritySubrackICNPortAccess_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 11, 10),
    _SysSecuritySubrackICNPortAccess_Type()
)
sysSecuritySubrackICNPortAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSecuritySubrackICNPortAccess.setStatus("current")
_SysSecurityChangeSubrackICNPortAccess_Type = CommandString
_SysSecurityChangeSubrackICNPortAccess_Object = MibScalar
sysSecurityChangeSubrackICNPortAccess = _SysSecurityChangeSubrackICNPortAccess_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 11, 11),
    _SysSecurityChangeSubrackICNPortAccess_Type()
)
sysSecurityChangeSubrackICNPortAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSecurityChangeSubrackICNPortAccess.setStatus("current")


class _SysSecurityMgmtAccessProofOfConnStatus_Type(Integer32):
    """Custom type sysSecurityMgmtAccessProofOfConnStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("connected", 1),
          ("disconnected", 2))
    )


_SysSecurityMgmtAccessProofOfConnStatus_Type.__name__ = "Integer32"
_SysSecurityMgmtAccessProofOfConnStatus_Object = MibScalar
sysSecurityMgmtAccessProofOfConnStatus = _SysSecurityMgmtAccessProofOfConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 11, 12),
    _SysSecurityMgmtAccessProofOfConnStatus_Type()
)
sysSecurityMgmtAccessProofOfConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSecurityMgmtAccessProofOfConnStatus.setStatus("current")


class _SysSecurityMgmtAccessProofOfConnectivity_Type(Integer32):
    """Custom type sysSecurityMgmtAccessProofOfConnectivity based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 720),
    )


_SysSecurityMgmtAccessProofOfConnectivity_Type.__name__ = "Integer32"
_SysSecurityMgmtAccessProofOfConnectivity_Object = MibScalar
sysSecurityMgmtAccessProofOfConnectivity = _SysSecurityMgmtAccessProofOfConnectivity_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 11, 13),
    _SysSecurityMgmtAccessProofOfConnectivity_Type()
)
sysSecurityMgmtAccessProofOfConnectivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSecurityMgmtAccessProofOfConnectivity.setStatus("current")


class _SysSecurityAutoEnableBlockedMgmtPorts_Type(OnOff):
    """Custom type sysSecurityAutoEnableBlockedMgmtPorts based on OnOff"""
    defaultValue = 2


_SysSecurityAutoEnableBlockedMgmtPorts_Type.__name__ = "OnOff"
_SysSecurityAutoEnableBlockedMgmtPorts_Object = MibScalar
sysSecurityAutoEnableBlockedMgmtPorts = _SysSecurityAutoEnableBlockedMgmtPorts_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 11, 14),
    _SysSecurityAutoEnableBlockedMgmtPorts_Type()
)
sysSecurityAutoEnableBlockedMgmtPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSecurityAutoEnableBlockedMgmtPorts.setStatus("current")
_SysSecurityBlockedMgmtPortsUnblocked_Type = FaultStatus
_SysSecurityBlockedMgmtPortsUnblocked_Object = MibScalar
sysSecurityBlockedMgmtPortsUnblocked = _SysSecurityBlockedMgmtPortsUnblocked_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 11, 15),
    _SysSecurityBlockedMgmtPortsUnblocked_Type()
)
sysSecurityBlockedMgmtPortsUnblocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSecurityBlockedMgmtPortsUnblocked.setStatus("current")
_SysManager_ObjectIdentity = ObjectIdentity
sysManager = _SysManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 12)
)


class _SysManagerName_Type(DisplayString):
    """Custom type sysManagerName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SysManagerName_Type.__name__ = "DisplayString"
_SysManagerName_Object = MibScalar
sysManagerName = _SysManagerName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 12, 1),
    _SysManagerName_Type()
)
sysManagerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysManagerName.setStatus("current")


class _SysManagerIPAddress_Type(DisplayString):
    """Custom type sysManagerIPAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysManagerIPAddress_Type.__name__ = "DisplayString"
_SysManagerIPAddress_Object = MibScalar
sysManagerIPAddress = _SysManagerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 12, 2),
    _SysManagerIPAddress_Type()
)
sysManagerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysManagerIPAddress.setStatus("current")


class _SysManagerPolicyName_Type(DisplayString):
    """Custom type sysManagerPolicyName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SysManagerPolicyName_Type.__name__ = "DisplayString"
_SysManagerPolicyName_Object = MibScalar
sysManagerPolicyName = _SysManagerPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 12, 3),
    _SysManagerPolicyName_Type()
)
sysManagerPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysManagerPolicyName.setStatus("current")


class _SysManagerPlatform_Type(Platform):
    """Custom type sysManagerPlatform based on Platform"""
    defaultValue = 0


_SysManagerPlatform_Type.__name__ = "Platform"
_SysManagerPlatform_Object = MibScalar
sysManagerPlatform = _SysManagerPlatform_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 12, 4),
    _SysManagerPlatform_Type()
)
sysManagerPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysManagerPlatform.setStatus("current")

# Managed Objects groups

sysGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 1)
)
sysGeneralGroup.setObjects(
      *(("LUM-SYSTEM-MIB", "sysGeneralTestAndIncr"),
        ("LUM-SYSTEM-MIB", "sysGeneralMibSpecVersion"),
        ("LUM-SYSTEM-MIB", "sysGeneralMibImplVersion"))
)
if mibBuilder.loadTexts:
    sysGeneralGroup.setStatus("deprecated")

sysNodeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 2)
)
sysNodeGroup.setObjects(
      *(("LUM-SYSTEM-MIB", "sysNodeName"),
        ("LUM-SYSTEM-MIB", "sysNodeContact"),
        ("LUM-SYSTEM-MIB", "sysNodeLocation"),
        ("LUM-SYSTEM-MIB", "sysNodeObjectId"),
        ("LUM-SYSTEM-MIB", "sysNodePrimaryNameServer"),
        ("LUM-SYSTEM-MIB", "sysNodeRunLevel"))
)
if mibBuilder.loadTexts:
    sysNodeGroup.setStatus("deprecated")

sysHostListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 3)
)
sysHostListGroup.setObjects(
      *(("LUM-SYSTEM-MIB", "sysHostIndex"),
        ("LUM-SYSTEM-MIB", "sysHostIpAddress"),
        ("LUM-SYSTEM-MIB", "sysHostNames"),
        ("LUM-SYSTEM-MIB", "sysHostRowStatus"))
)
if mibBuilder.loadTexts:
    sysHostListGroup.setStatus("current")

sysTimeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 4)
)
sysTimeGroup.setObjects(
      *(("LUM-SYSTEM-MIB", "sysTimeLocal"),
        ("LUM-SYSTEM-MIB", "sysTimeZone"),
        ("LUM-SYSTEM-MIB", "sysTimePrimaryServer"),
        ("LUM-SYSTEM-MIB", "sysTimeSecondaryServer"))
)
if mibBuilder.loadTexts:
    sysTimeGroup.setStatus("deprecated")

sysLogListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 5)
)
sysLogListGroup.setObjects(
      *(("LUM-SYSTEM-MIB", "sysLogIndex"),
        ("LUM-SYSTEM-MIB", "sysLogSelection"),
        ("LUM-SYSTEM-MIB", "sysLogAction"),
        ("LUM-SYSTEM-MIB", "sysLogRowStatus"))
)
if mibBuilder.loadTexts:
    sysLogListGroup.setStatus("deprecated")

sysGeneralGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 6)
)
sysGeneralGroupV2.setObjects(
    ("LUM-SYSTEM-MIB", "sysGeneralLastChangeTime")
)
if mibBuilder.loadTexts:
    sysGeneralGroupV2.setStatus("deprecated")

sysNodeGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 7)
)
sysNodeGroupV2.setObjects(
      *(("LUM-SYSTEM-MIB", "sysNodeName"),
        ("LUM-SYSTEM-MIB", "sysNodeContact"),
        ("LUM-SYSTEM-MIB", "sysNodeLocation"),
        ("LUM-SYSTEM-MIB", "sysNodeObjectId"),
        ("LUM-SYSTEM-MIB", "sysNodePrimaryNameServer"),
        ("LUM-SYSTEM-MIB", "sysNodeRunLevel"),
        ("LUM-SYSTEM-MIB", "sysNodeSecondaryNameServer"))
)
if mibBuilder.loadTexts:
    sysNodeGroupV2.setStatus("deprecated")

sysUserGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 8)
)
sysUserGroup.setObjects(
      *(("LUM-SYSTEM-MIB", "sysUserIndex"),
        ("LUM-SYSTEM-MIB", "sysUserName"),
        ("LUM-SYSTEM-MIB", "sysUserPasswd"),
        ("LUM-SYSTEM-MIB", "sysUserDescr"),
        ("LUM-SYSTEM-MIB", "sysUserLastChangeTime"),
        ("LUM-SYSTEM-MIB", "sysUserExpireTime"),
        ("LUM-SYSTEM-MIB", "sysUserRowStatus"))
)
if mibBuilder.loadTexts:
    sysUserGroup.setStatus("deprecated")

sysNodeGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 9)
)
sysNodeGroupV3.setObjects(
      *(("LUM-SYSTEM-MIB", "sysNodeName"),
        ("LUM-SYSTEM-MIB", "sysNodeContact"),
        ("LUM-SYSTEM-MIB", "sysNodeLocation"),
        ("LUM-SYSTEM-MIB", "sysNodeObjectId"),
        ("LUM-SYSTEM-MIB", "sysNodePrimaryNameServer"),
        ("LUM-SYSTEM-MIB", "sysNodeRunLevel"),
        ("LUM-SYSTEM-MIB", "sysNodeSecondaryNameServer"),
        ("LUM-SYSTEM-MIB", "sysNodeUptime"))
)
if mibBuilder.loadTexts:
    sysNodeGroupV3.setStatus("deprecated")

sysGeneralGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 10)
)
sysGeneralGroupV3.setObjects(
      *(("LUM-SYSTEM-MIB", "sysGeneralLastChangeTime"),
        ("LUM-SYSTEM-MIB", "sysGeneralTest"))
)
if mibBuilder.loadTexts:
    sysGeneralGroupV3.setStatus("current")

sysNodeGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 11)
)
sysNodeGroupV4.setObjects(
      *(("LUM-SYSTEM-MIB", "sysNodeName"),
        ("LUM-SYSTEM-MIB", "sysNodeContact"),
        ("LUM-SYSTEM-MIB", "sysNodeLocation"),
        ("LUM-SYSTEM-MIB", "sysNodeObjectId"),
        ("LUM-SYSTEM-MIB", "sysNodePrimaryNameServer"),
        ("LUM-SYSTEM-MIB", "sysNodeRunLevel"),
        ("LUM-SYSTEM-MIB", "sysNodeSecondaryNameServer"),
        ("LUM-SYSTEM-MIB", "sysNodeUptime"),
        ("LUM-SYSTEM-MIB", "sysNodeNeDistinguishedName"),
        ("LUM-SYSTEM-MIB", "sysNodeNeUserName"),
        ("LUM-SYSTEM-MIB", "sysNodeNeType"))
)
if mibBuilder.loadTexts:
    sysNodeGroupV4.setStatus("deprecated")

sysGeneralGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 12)
)
sysGeneralGroupV4.setObjects(
      *(("LUM-SYSTEM-MIB", "sysGeneralLastChangeTime"),
        ("LUM-SYSTEM-MIB", "sysGeneralTest"),
        ("LUM-SYSTEM-MIB", "sysGeneralConfigLastChangeTime"))
)
if mibBuilder.loadTexts:
    sysGeneralGroupV4.setStatus("deprecated")

sysNodeGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 15)
)
sysNodeGroupV5.setObjects(
      *(("LUM-SYSTEM-MIB", "sysNodeName"),
        ("LUM-SYSTEM-MIB", "sysNodeContact"),
        ("LUM-SYSTEM-MIB", "sysNodeLocation"),
        ("LUM-SYSTEM-MIB", "sysNodeObjectId"),
        ("LUM-SYSTEM-MIB", "sysNodePrimaryNameServer"),
        ("LUM-SYSTEM-MIB", "sysNodeSecondaryNameServer"),
        ("LUM-SYSTEM-MIB", "sysNodeUptime"),
        ("LUM-SYSTEM-MIB", "sysNodeNeDistinguishedName"),
        ("LUM-SYSTEM-MIB", "sysNodeNeUserName"),
        ("LUM-SYSTEM-MIB", "sysNodeNeType"),
        ("LUM-SYSTEM-MIB", "sysNodeBootTime"))
)
if mibBuilder.loadTexts:
    sysNodeGroupV5.setStatus("deprecated")

sysRadiusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 16)
)
sysRadiusGroup.setObjects(
      *(("LUM-SYSTEM-MIB", "sysRadiusPrimaryServer"),
        ("LUM-SYSTEM-MIB", "sysRadiusPrimarySecret"),
        ("LUM-SYSTEM-MIB", "sysRadiusSecondaryServer"),
        ("LUM-SYSTEM-MIB", "sysRadiusSecondarySecret"))
)
if mibBuilder.loadTexts:
    sysRadiusGroup.setStatus("deprecated")

sysNodeGroupV6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 17)
)
sysNodeGroupV6.setObjects(
      *(("LUM-SYSTEM-MIB", "sysNodeName"),
        ("LUM-SYSTEM-MIB", "sysNodeContact"),
        ("LUM-SYSTEM-MIB", "sysNodeLocation"),
        ("LUM-SYSTEM-MIB", "sysNodeObjectId"),
        ("LUM-SYSTEM-MIB", "sysNodePrimaryNameServer"),
        ("LUM-SYSTEM-MIB", "sysNodeSecondaryNameServer"),
        ("LUM-SYSTEM-MIB", "sysNodeUptime"),
        ("LUM-SYSTEM-MIB", "sysNodeNeDistinguishedName"),
        ("LUM-SYSTEM-MIB", "sysNodeNeUserName"),
        ("LUM-SYSTEM-MIB", "sysNodeNeType"),
        ("LUM-SYSTEM-MIB", "sysNodeBootTime"),
        ("LUM-SYSTEM-MIB", "sysNodeLocale"))
)
if mibBuilder.loadTexts:
    sysNodeGroupV6.setStatus("deprecated")

sysTimeGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 18)
)
sysTimeGroupV2.setObjects(
      *(("LUM-SYSTEM-MIB", "sysTimeLocal"),
        ("LUM-SYSTEM-MIB", "sysTimeZone"),
        ("LUM-SYSTEM-MIB", "sysTimePrimaryServer"),
        ("LUM-SYSTEM-MIB", "sysTimeSecondaryServer"),
        ("LUM-SYSTEM-MIB", "sysTimeChangeLocalTime"))
)
if mibBuilder.loadTexts:
    sysTimeGroupV2.setStatus("deprecated")

sysLicenseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 19)
)
sysLicenseGroup.setObjects(
      *(("LUM-SYSTEM-MIB", "sysLicenseExpireDate"),
        ("LUM-SYSTEM-MIB", "sysLicenseCustomer"),
        ("LUM-SYSTEM-MIB", "sysLicenseExpiresSoon"),
        ("LUM-SYSTEM-MIB", "sysLicenseExpired"),
        ("LUM-SYSTEM-MIB", "sysLicenseExpiredCause"),
        ("LUM-SYSTEM-MIB", "sysLicenseFeatureEws"),
        ("LUM-SYSTEM-MIB", "sysLicenseFeatureEws"),
        ("LUM-SYSTEM-MIB", "sysLicenseFeatureOspf"),
        ("LUM-SYSTEM-MIB", "sysLicenseFeatureSnmp"),
        ("LUM-SYSTEM-MIB", "sysLicenseFeatureGmpls"),
        ("LUM-SYSTEM-MIB", "sysLicenseFeatureRudb"),
        ("LUM-SYSTEM-MIB", "sysLicenseInstallLicenseFile"))
)
if mibBuilder.loadTexts:
    sysLicenseGroup.setStatus("current")

sysTacacsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 20)
)
sysTacacsGroup.setObjects(
      *(("LUM-SYSTEM-MIB", "sysTacacsPrimaryServer"),
        ("LUM-SYSTEM-MIB", "sysTacacsSecondaryServer"),
        ("LUM-SYSTEM-MIB", "sysTacacsSecret"))
)
if mibBuilder.loadTexts:
    sysTacacsGroup.setStatus("deprecated")

sysUserGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 21)
)
sysUserGroupV2.setObjects(
      *(("LUM-SYSTEM-MIB", "sysUserIndex"),
        ("LUM-SYSTEM-MIB", "sysUserName"),
        ("LUM-SYSTEM-MIB", "sysUserDescr"),
        ("LUM-SYSTEM-MIB", "sysUserProfile"),
        ("LUM-SYSTEM-MIB", "sysUserUid"))
)
if mibBuilder.loadTexts:
    sysUserGroupV2.setStatus("current")

sysGeneralGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 22)
)
sysGeneralGroupV5.setObjects(
      *(("LUM-SYSTEM-MIB", "sysGeneralLastChangeTime"),
        ("LUM-SYSTEM-MIB", "sysGeneralTest"),
        ("LUM-SYSTEM-MIB", "sysGeneralConfigLastChangeTime"),
        ("LUM-SYSTEM-MIB", "sysGeneralLoginRecords"))
)
if mibBuilder.loadTexts:
    sysGeneralGroupV5.setStatus("deprecated")

sysUserGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 23)
)
sysUserGroupV3.setObjects(
      *(("LUM-SYSTEM-MIB", "sysUserIndex"),
        ("LUM-SYSTEM-MIB", "sysUserName"),
        ("LUM-SYSTEM-MIB", "sysUserDescr"),
        ("LUM-SYSTEM-MIB", "sysUserProfile"),
        ("LUM-SYSTEM-MIB", "sysUserUid"),
        ("LUM-SYSTEM-MIB", "sysUserChangePassword"),
        ("LUM-SYSTEM-MIB", "sysUserClearPassword"),
        ("LUM-SYSTEM-MIB", "sysUserDisable"))
)
if mibBuilder.loadTexts:
    sysUserGroupV3.setStatus("deprecated")

sysTacacsGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 24)
)
sysTacacsGroupV2.setObjects(
      *(("LUM-SYSTEM-MIB", "sysTacacsPrimaryServer"),
        ("LUM-SYSTEM-MIB", "sysTacacsSecondaryServer"),
        ("LUM-SYSTEM-MIB", "sysTacacsSecret"),
        ("LUM-SYSTEM-MIB", "sysTacacsSecondarySecret"))
)
if mibBuilder.loadTexts:
    sysTacacsGroupV2.setStatus("deprecated")

sysGeneralGroupV6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 25)
)
sysGeneralGroupV6.setObjects(
      *(("LUM-SYSTEM-MIB", "sysGeneralLastChangeTime"),
        ("LUM-SYSTEM-MIB", "sysGeneralTest"),
        ("LUM-SYSTEM-MIB", "sysGeneralConfigLastChangeTime"),
        ("LUM-SYSTEM-MIB", "sysGeneralLoginRecords"),
        ("LUM-SYSTEM-MIB", "sysGeneralUserTableSize"))
)
if mibBuilder.loadTexts:
    sysGeneralGroupV6.setStatus("deprecated")

sysUserGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 26)
)
sysUserGroupV4.setObjects(
      *(("LUM-SYSTEM-MIB", "sysUserIndex"),
        ("LUM-SYSTEM-MIB", "sysUserName"),
        ("LUM-SYSTEM-MIB", "sysUserDescr"),
        ("LUM-SYSTEM-MIB", "sysUserProfile"),
        ("LUM-SYSTEM-MIB", "sysUserUid"),
        ("LUM-SYSTEM-MIB", "sysUserChangePassword"),
        ("LUM-SYSTEM-MIB", "sysUserClearPassword"),
        ("LUM-SYSTEM-MIB", "sysUserDisable"),
        ("LUM-SYSTEM-MIB", "sysUserMode"),
        ("LUM-SYSTEM-MIB", "sysUserEnable"))
)
if mibBuilder.loadTexts:
    sysUserGroupV4.setStatus("current")

sysSecurityGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 27)
)
sysSecurityGroupV1.setObjects(
      *(("LUM-SYSTEM-MIB", "sysSecurityLocalConsoleAccess"),
        ("LUM-SYSTEM-MIB", "sysSecurityChangeLocalConsoleAccess"))
)
if mibBuilder.loadTexts:
    sysSecurityGroupV1.setStatus("deprecated")

sysNodeGroupV7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 28)
)
sysNodeGroupV7.setObjects(
      *(("LUM-SYSTEM-MIB", "sysNodeName"),
        ("LUM-SYSTEM-MIB", "sysNodeContact"),
        ("LUM-SYSTEM-MIB", "sysNodeLocation"),
        ("LUM-SYSTEM-MIB", "sysNodeObjectId"),
        ("LUM-SYSTEM-MIB", "sysNodePrimaryNameServer"),
        ("LUM-SYSTEM-MIB", "sysNodeSecondaryNameServer"),
        ("LUM-SYSTEM-MIB", "sysNodeUptime"),
        ("LUM-SYSTEM-MIB", "sysNodeNeDistinguishedName"),
        ("LUM-SYSTEM-MIB", "sysNodeNeUserName"),
        ("LUM-SYSTEM-MIB", "sysNodeNeType"),
        ("LUM-SYSTEM-MIB", "sysNodeBootTime"),
        ("LUM-SYSTEM-MIB", "sysNodeLocale"),
        ("LUM-SYSTEM-MIB", "sysNodeVersion"))
)
if mibBuilder.loadTexts:
    sysNodeGroupV7.setStatus("deprecated")

sysTacacsGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 29)
)
sysTacacsGroupV3.setObjects(
      *(("LUM-SYSTEM-MIB", "sysTacacsSecret"),
        ("LUM-SYSTEM-MIB", "sysTacacsSecondarySecret"),
        ("LUM-SYSTEM-MIB", "sysTacacsPrimaryIpAddress"),
        ("LUM-SYSTEM-MIB", "sysTacacsSecondaryIpAddress"))
)
if mibBuilder.loadTexts:
    sysTacacsGroupV3.setStatus("current")

sysRadiusGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 30)
)
sysRadiusGroupV2.setObjects(
      *(("LUM-SYSTEM-MIB", "sysRadiusPrimarySecret"),
        ("LUM-SYSTEM-MIB", "sysRadiusSecondarySecret"),
        ("LUM-SYSTEM-MIB", "sysRadiusPrimaryIpAddress"),
        ("LUM-SYSTEM-MIB", "sysRadiusSecondaryIpAddress"))
)
if mibBuilder.loadTexts:
    sysRadiusGroupV2.setStatus("deprecated")

sysTimeGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 31)
)
sysTimeGroupV3.setObjects(
      *(("LUM-SYSTEM-MIB", "sysTimeLocal"),
        ("LUM-SYSTEM-MIB", "sysTimeZone"),
        ("LUM-SYSTEM-MIB", "sysTimeChangeLocalTime"),
        ("LUM-SYSTEM-MIB", "sysTimePrimaryIpAddress"),
        ("LUM-SYSTEM-MIB", "sysTimeSecondaryIpAddress"))
)
if mibBuilder.loadTexts:
    sysTimeGroupV3.setStatus("current")

sysSecurityGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 32)
)
sysSecurityGroupV2.setObjects(
      *(("LUM-SYSTEM-MIB", "sysSecurityLocalConsoleAccess"),
        ("LUM-SYSTEM-MIB", "sysSecurityChangeLocalConsoleAccess"),
        ("LUM-SYSTEM-MIB", "sysSecurityIpTablesStatus"))
)
if mibBuilder.loadTexts:
    sysSecurityGroupV2.setStatus("deprecated")

sysRadiusGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 33)
)
sysRadiusGroupV3.setObjects(
      *(("LUM-SYSTEM-MIB", "sysRadiusPrimarySecret"),
        ("LUM-SYSTEM-MIB", "sysRadiusSecondarySecret"),
        ("LUM-SYSTEM-MIB", "sysRadiusPrimaryIpAddress"),
        ("LUM-SYSTEM-MIB", "sysRadiusSecondaryIpAddress"),
        ("LUM-SYSTEM-MIB", "sysRadiusPrimaryPort"),
        ("LUM-SYSTEM-MIB", "sysRadiusSecondaryPort"))
)
if mibBuilder.loadTexts:
    sysRadiusGroupV3.setStatus("deprecated")

sysRadiusGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 34)
)
sysRadiusGroupV4.setObjects(
      *(("LUM-SYSTEM-MIB", "sysRadiusPrimarySecret"),
        ("LUM-SYSTEM-MIB", "sysRadiusSecondarySecret"),
        ("LUM-SYSTEM-MIB", "sysRadiusPrimaryIpAddress"),
        ("LUM-SYSTEM-MIB", "sysRadiusSecondaryIpAddress"),
        ("LUM-SYSTEM-MIB", "sysRadiusPrimaryPort"),
        ("LUM-SYSTEM-MIB", "sysRadiusSecondaryPort"),
        ("LUM-SYSTEM-MIB", "sysRadiusDefaultUserProfile"))
)
if mibBuilder.loadTexts:
    sysRadiusGroupV4.setStatus("current")

sysGeneralGroupV7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 35)
)
sysGeneralGroupV7.setObjects(
      *(("LUM-SYSTEM-MIB", "sysGeneralLastChangeTime"),
        ("LUM-SYSTEM-MIB", "sysGeneralConfigLastChangeTime"),
        ("LUM-SYSTEM-MIB", "sysGeneralLoginRecords"),
        ("LUM-SYSTEM-MIB", "sysGeneralUserTableSize"),
        ("LUM-SYSTEM-MIB", "sysGeneralWriteTest"))
)
if mibBuilder.loadTexts:
    sysGeneralGroupV7.setStatus("current")

sysSecurityGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 36)
)
sysSecurityGroupV3.setObjects(
      *(("LUM-SYSTEM-MIB", "sysSecurityLocalConsoleAccess"),
        ("LUM-SYSTEM-MIB", "sysSecurityChangeLocalConsoleAccess"),
        ("LUM-SYSTEM-MIB", "sysSecurityLocalCraftAccess"),
        ("LUM-SYSTEM-MIB", "sysSecurityChangeLocalCraftAccess"),
        ("LUM-SYSTEM-MIB", "sysSecurityIpTablesStatus"),
        ("LUM-SYSTEM-MIB", "sysSecurityAuthenticationOrder"))
)
if mibBuilder.loadTexts:
    sysSecurityGroupV3.setStatus("deprecated")

sysNodeGroupV8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 37)
)
sysNodeGroupV8.setObjects(
      *(("LUM-SYSTEM-MIB", "sysNodeName"),
        ("LUM-SYSTEM-MIB", "sysNodeContact"),
        ("LUM-SYSTEM-MIB", "sysNodeLocation"),
        ("LUM-SYSTEM-MIB", "sysNodeObjectId"),
        ("LUM-SYSTEM-MIB", "sysNodePrimaryNameServer"),
        ("LUM-SYSTEM-MIB", "sysNodeSecondaryNameServer"),
        ("LUM-SYSTEM-MIB", "sysNodeUptime"),
        ("LUM-SYSTEM-MIB", "sysNodeNeDistinguishedName"),
        ("LUM-SYSTEM-MIB", "sysNodeNeUserName"),
        ("LUM-SYSTEM-MIB", "sysNodeNeType"),
        ("LUM-SYSTEM-MIB", "sysNodeBootTime"),
        ("LUM-SYSTEM-MIB", "sysNodeLocale"),
        ("LUM-SYSTEM-MIB", "sysNodeVersion"),
        ("LUM-SYSTEM-MIB", "sysNodeCLLI"),
        ("LUM-SYSTEM-MIB", "sysNodeFIC"),
        ("LUM-SYSTEM-MIB", "sysNodeTID"),
        ("LUM-SYSTEM-MIB", "sysNodeLatitude"),
        ("LUM-SYSTEM-MIB", "sysNodeLongitude"))
)
if mibBuilder.loadTexts:
    sysNodeGroupV8.setStatus("current")

sysSecurityGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 38)
)
sysSecurityGroupV4.setObjects(
      *(("LUM-SYSTEM-MIB", "sysSecurityLocalConsoleAccess"),
        ("LUM-SYSTEM-MIB", "sysSecurityChangeLocalConsoleAccess"),
        ("LUM-SYSTEM-MIB", "sysSecurityLocalCraftAccess"),
        ("LUM-SYSTEM-MIB", "sysSecurityChangeLocalCraftAccess"),
        ("LUM-SYSTEM-MIB", "sysSecurityIpTablesStatus"),
        ("LUM-SYSTEM-MIB", "sysSecurityAuthenticationOrder"),
        ("LUM-SYSTEM-MIB", "sysSecurityFileSystemAccessRestrictions"))
)
if mibBuilder.loadTexts:
    sysSecurityGroupV4.setStatus("deprecated")

sysSecurityGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 39)
)
sysSecurityGroupV5.setObjects(
      *(("LUM-SYSTEM-MIB", "sysSecurityLocalConsoleAccess"),
        ("LUM-SYSTEM-MIB", "sysSecurityChangeLocalConsoleAccess"),
        ("LUM-SYSTEM-MIB", "sysSecurityLocalCraftAccess"),
        ("LUM-SYSTEM-MIB", "sysSecurityChangeLocalCraftAccess"),
        ("LUM-SYSTEM-MIB", "sysSecurityIpTablesStatus"),
        ("LUM-SYSTEM-MIB", "sysSecurityAuthenticationOrder"),
        ("LUM-SYSTEM-MIB", "sysSecurityFileSystemAccessRestrictions"),
        ("LUM-SYSTEM-MIB", "sysSecurityCUFrontICNPortAccess"),
        ("LUM-SYSTEM-MIB", "sysSecurityChangeCUFrontICNPortAccess"),
        ("LUM-SYSTEM-MIB", "sysSecuritySubrackICNPortAccess"),
        ("LUM-SYSTEM-MIB", "sysSecurityChangeSubrackICNPortAccess"),
        ("LUM-SYSTEM-MIB", "sysSecurityMgmtAccessProofOfConnStatus"),
        ("LUM-SYSTEM-MIB", "sysSecurityMgmtAccessProofOfConnectivity"),
        ("LUM-SYSTEM-MIB", "sysSecurityAutoEnableBlockedMgmtPorts"),
        ("LUM-SYSTEM-MIB", "sysSecurityBlockedMgmtPortsUnblocked"))
)
if mibBuilder.loadTexts:
    sysSecurityGroupV5.setStatus("deprecated")

sysSecurityGroupV6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 40)
)
sysSecurityGroupV6.setObjects(
      *(("LUM-SYSTEM-MIB", "sysSecurityLocalConsoleAccess"),
        ("LUM-SYSTEM-MIB", "sysSecurityChangeLocalConsoleAccess"),
        ("LUM-SYSTEM-MIB", "sysSecurityLocalCraftAccess"),
        ("LUM-SYSTEM-MIB", "sysSecurityChangeLocalCraftAccess"),
        ("LUM-SYSTEM-MIB", "sysSecurityIpTablesStatus"),
        ("LUM-SYSTEM-MIB", "sysSecurityAuthenticationOrder"),
        ("LUM-SYSTEM-MIB", "sysSecurityFileSystemAccessRestrictions"),
        ("LUM-SYSTEM-MIB", "sysSecurityCUFrontICNPortAccess"),
        ("LUM-SYSTEM-MIB", "sysSecurityChangeCUFrontICNPortAccess"),
        ("LUM-SYSTEM-MIB", "sysSecuritySubrackICNPortAccess"),
        ("LUM-SYSTEM-MIB", "sysSecurityChangeSubrackICNPortAccess"),
        ("LUM-SYSTEM-MIB", "sysSecurityMgmtAccessProofOfConnStatus"),
        ("LUM-SYSTEM-MIB", "sysSecurityMgmtAccessProofOfConnectivity"),
        ("LUM-SYSTEM-MIB", "sysSecurityAutoEnableBlockedMgmtPorts"),
        ("LUM-SYSTEM-MIB", "sysSecurityBlockedMgmtPortsUnblocked"))
)
if mibBuilder.loadTexts:
    sysSecurityGroupV6.setStatus("current")

sysManagerGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 41)
)
sysManagerGroupV1.setObjects(
      *(("LUM-SYSTEM-MIB", "sysManagerName"),
        ("LUM-SYSTEM-MIB", "sysManagerIPAddress"),
        ("LUM-SYSTEM-MIB", "sysManagerPolicyName"),
        ("LUM-SYSTEM-MIB", "sysManagerPlatform"))
)
if mibBuilder.loadTexts:
    sysManagerGroupV1.setStatus("current")

sysGeneralMinimalGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 3, 1)
)
sysGeneralMinimalGroupV1.setObjects(
      *(("LUM-SYSTEM-MIB", "sysGeneralLastChangeTime"),
        ("LUM-SYSTEM-MIB", "sysGeneralConfigLastChangeTime"))
)
if mibBuilder.loadTexts:
    sysGeneralMinimalGroupV1.setStatus("current")

sysNodeMinimalGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 3, 2)
)
sysNodeMinimalGroupV1.setObjects(
      *(("LUM-SYSTEM-MIB", "sysNodeName"),
        ("LUM-SYSTEM-MIB", "sysNodeNeUserName"),
        ("LUM-SYSTEM-MIB", "sysNodeBootTime"))
)
if mibBuilder.loadTexts:
    sysNodeMinimalGroupV1.setStatus("deprecated")

sysTimeMinimalGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 3, 3)
)
sysTimeMinimalGroupV1.setObjects(
    ("LUM-SYSTEM-MIB", "sysTimeLocal")
)
if mibBuilder.loadTexts:
    sysTimeMinimalGroupV1.setStatus("deprecated")

sysNodeMinimalGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 3, 4)
)
sysNodeMinimalGroupV2.setObjects(
      *(("LUM-SYSTEM-MIB", "sysNodeName"),
        ("LUM-SYSTEM-MIB", "sysNodeNeUserName"),
        ("LUM-SYSTEM-MIB", "sysNodeLocation"),
        ("LUM-SYSTEM-MIB", "sysNodeContact"),
        ("LUM-SYSTEM-MIB", "sysNodeBootTime"))
)
if mibBuilder.loadTexts:
    sysNodeMinimalGroupV2.setStatus("current")

sysTimeMinimalGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 3, 5)
)
sysTimeMinimalGroupV2.setObjects(
      *(("LUM-SYSTEM-MIB", "sysTimeLocal"),
        ("LUM-SYSTEM-MIB", "sysTimeZone"),
        ("LUM-SYSTEM-MIB", "sysTimePrimaryServer"))
)
if mibBuilder.loadTexts:
    sysTimeMinimalGroupV2.setStatus("deprecated")

sysRadiusMinimalGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 3, 6)
)
sysRadiusMinimalGroupV1.setObjects(
      *(("LUM-SYSTEM-MIB", "sysRadiusPrimaryServer"),
        ("LUM-SYSTEM-MIB", "sysRadiusPrimarySecret"),
        ("LUM-SYSTEM-MIB", "sysRadiusSecondaryServer"),
        ("LUM-SYSTEM-MIB", "sysRadiusSecondarySecret"))
)
if mibBuilder.loadTexts:
    sysRadiusMinimalGroupV1.setStatus("deprecated")

sysTimeMinimalGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 3, 7)
)
sysTimeMinimalGroupV3.setObjects(
      *(("LUM-SYSTEM-MIB", "sysTimeLocal"),
        ("LUM-SYSTEM-MIB", "sysTimeZone"),
        ("LUM-SYSTEM-MIB", "sysTimePrimaryIpAddress"))
)
if mibBuilder.loadTexts:
    sysTimeMinimalGroupV3.setStatus("current")

sysRadiusMinimalGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 3, 8)
)
sysRadiusMinimalGroupV2.setObjects(
      *(("LUM-SYSTEM-MIB", "sysRadiusPrimarySecret"),
        ("LUM-SYSTEM-MIB", "sysRadiusSecondarySecret"),
        ("LUM-SYSTEM-MIB", "sysRadiusPrimaryIpAddress"),
        ("LUM-SYSTEM-MIB", "sysRadiusSecondaryIpAddress"))
)
if mibBuilder.loadTexts:
    sysRadiusMinimalGroupV2.setStatus("deprecated")

sysRadiusMinimalGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 3, 9)
)
sysRadiusMinimalGroupV3.setObjects(
      *(("LUM-SYSTEM-MIB", "sysRadiusPrimarySecret"),
        ("LUM-SYSTEM-MIB", "sysRadiusSecondarySecret"),
        ("LUM-SYSTEM-MIB", "sysRadiusPrimaryIpAddress"),
        ("LUM-SYSTEM-MIB", "sysRadiusSecondaryIpAddress"),
        ("LUM-SYSTEM-MIB", "sysRadiusPrimaryPort"),
        ("LUM-SYSTEM-MIB", "sysRadiusSecondaryPort"))
)
if mibBuilder.loadTexts:
    sysRadiusMinimalGroupV3.setStatus("deprecated")

sysRadiusMinimalGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 3, 10)
)
sysRadiusMinimalGroupV4.setObjects(
      *(("LUM-SYSTEM-MIB", "sysRadiusPrimarySecret"),
        ("LUM-SYSTEM-MIB", "sysRadiusSecondarySecret"),
        ("LUM-SYSTEM-MIB", "sysRadiusPrimaryIpAddress"),
        ("LUM-SYSTEM-MIB", "sysRadiusSecondaryIpAddress"),
        ("LUM-SYSTEM-MIB", "sysRadiusPrimaryPort"),
        ("LUM-SYSTEM-MIB", "sysRadiusSecondaryPort"),
        ("LUM-SYSTEM-MIB", "sysRadiusDefaultUserProfile"))
)
if mibBuilder.loadTexts:
    sysRadiusMinimalGroupV4.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumSystemBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 1)
)
lumSystemBasicComplV1.setObjects(
      *(("LUM-SYSTEM-MIB", "sysGeneralGroup"),
        ("LUM-SYSTEM-MIB", "sysNodeGroup"),
        ("LUM-SYSTEM-MIB", "sysTimeGroup"),
        ("LUM-SYSTEM-MIB", "sysLogListGroup"),
        ("LUM-SYSTEM-MIB", "sysHostListGroup"))
)
if mibBuilder.loadTexts:
    lumSystemBasicComplV1.setStatus(
        "deprecated"
    )

lumSystemBasicComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 2)
)
lumSystemBasicComplV2.setObjects(
      *(("LUM-SYSTEM-MIB", "sysGeneralGroupV2"),
        ("LUM-SYSTEM-MIB", "sysTimeGroup"),
        ("LUM-SYSTEM-MIB", "sysNodeGroup"))
)
if mibBuilder.loadTexts:
    lumSystemBasicComplV2.setStatus(
        "deprecated"
    )

lumSystemBasicComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 3)
)
lumSystemBasicComplV3.setObjects(
      *(("LUM-SYSTEM-MIB", "sysGeneralGroupV2"),
        ("LUM-SYSTEM-MIB", "sysTimeGroup"),
        ("LUM-SYSTEM-MIB", "sysNodeGroupV2"),
        ("LUM-SYSTEM-MIB", "sysUserGroup"))
)
if mibBuilder.loadTexts:
    lumSystemBasicComplV3.setStatus(
        "deprecated"
    )

lumSystemBasicComplV4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 4)
)
lumSystemBasicComplV4.setObjects(
      *(("LUM-SYSTEM-MIB", "sysGeneralGroupV2"),
        ("LUM-SYSTEM-MIB", "sysTimeGroup"),
        ("LUM-SYSTEM-MIB", "sysNodeGroupV3"),
        ("LUM-SYSTEM-MIB", "sysUserGroup"))
)
if mibBuilder.loadTexts:
    lumSystemBasicComplV4.setStatus(
        "deprecated"
    )

lumSystemBasicComplV5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 5)
)
lumSystemBasicComplV5.setObjects(
      *(("LUM-SYSTEM-MIB", "sysGeneralGroupV3"),
        ("LUM-SYSTEM-MIB", "sysTimeGroup"),
        ("LUM-SYSTEM-MIB", "sysNodeGroupV3"),
        ("LUM-SYSTEM-MIB", "sysUserGroup"))
)
if mibBuilder.loadTexts:
    lumSystemBasicComplV5.setStatus(
        "deprecated"
    )

lumSystemBasicComplV6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 6)
)
lumSystemBasicComplV6.setObjects(
      *(("LUM-SYSTEM-MIB", "sysGeneralGroupV3"),
        ("LUM-SYSTEM-MIB", "sysTimeGroup"),
        ("LUM-SYSTEM-MIB", "sysNodeGroupV4"),
        ("LUM-SYSTEM-MIB", "sysUserGroup"))
)
if mibBuilder.loadTexts:
    lumSystemBasicComplV6.setStatus(
        "deprecated"
    )

lumSystemBasicComplV7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 7)
)
lumSystemBasicComplV7.setObjects(
      *(("LUM-SYSTEM-MIB", "sysGeneralGroupV4"),
        ("LUM-SYSTEM-MIB", "sysTimeGroup"),
        ("LUM-SYSTEM-MIB", "sysNodeGroupV5"),
        ("LUM-SYSTEM-MIB", "sysUserGroup"))
)
if mibBuilder.loadTexts:
    lumSystemBasicComplV7.setStatus(
        "deprecated"
    )

lumSystemBasicComplV8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 8)
)
lumSystemBasicComplV8.setObjects(
      *(("LUM-SYSTEM-MIB", "sysGeneralGroupV4"),
        ("LUM-SYSTEM-MIB", "sysTimeGroup"),
        ("LUM-SYSTEM-MIB", "sysNodeGroupV5"),
        ("LUM-SYSTEM-MIB", "sysUserGroup"),
        ("LUM-SYSTEM-MIB", "sysRadiusGroup"))
)
if mibBuilder.loadTexts:
    lumSystemBasicComplV8.setStatus(
        "deprecated"
    )

lumSystemBasicComplV9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 9)
)
lumSystemBasicComplV9.setObjects(
      *(("LUM-SYSTEM-MIB", "sysGeneralGroupV4"),
        ("LUM-SYSTEM-MIB", "sysTimeGroup"),
        ("LUM-SYSTEM-MIB", "sysNodeGroupV6"),
        ("LUM-SYSTEM-MIB", "sysUserGroup"),
        ("LUM-SYSTEM-MIB", "sysRadiusGroup"))
)
if mibBuilder.loadTexts:
    lumSystemBasicComplV9.setStatus(
        "deprecated"
    )

lumSystemBasicComplV10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 10)
)
lumSystemBasicComplV10.setObjects(
      *(("LUM-SYSTEM-MIB", "sysGeneralGroupV4"),
        ("LUM-SYSTEM-MIB", "sysTimeGroupV2"),
        ("LUM-SYSTEM-MIB", "sysNodeGroupV6"),
        ("LUM-SYSTEM-MIB", "sysRadiusGroup"),
        ("LUM-SYSTEM-MIB", "sysLicenseGroup"))
)
if mibBuilder.loadTexts:
    lumSystemBasicComplV10.setStatus(
        "deprecated"
    )

lumSystemBasicComplV11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 11)
)
lumSystemBasicComplV11.setObjects(
      *(("LUM-SYSTEM-MIB", "sysGeneralGroupV4"),
        ("LUM-SYSTEM-MIB", "sysTimeGroupV2"),
        ("LUM-SYSTEM-MIB", "sysNodeGroupV6"),
        ("LUM-SYSTEM-MIB", "sysRadiusGroup"),
        ("LUM-SYSTEM-MIB", "sysLicenseGroup"),
        ("LUM-SYSTEM-MIB", "sysTacacsGroup"))
)
if mibBuilder.loadTexts:
    lumSystemBasicComplV11.setStatus(
        "deprecated"
    )

lumSystemBasicComplV12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 12)
)
lumSystemBasicComplV12.setObjects(
      *(("LUM-SYSTEM-MIB", "sysGeneralGroupV4"),
        ("LUM-SYSTEM-MIB", "sysTimeGroupV2"),
        ("LUM-SYSTEM-MIB", "sysNodeGroupV6"),
        ("LUM-SYSTEM-MIB", "sysRadiusGroup"),
        ("LUM-SYSTEM-MIB", "sysLicenseGroup"),
        ("LUM-SYSTEM-MIB", "sysTacacsGroup"),
        ("LUM-SYSTEM-MIB", "sysUserGroupV2"))
)
if mibBuilder.loadTexts:
    lumSystemBasicComplV12.setStatus(
        "deprecated"
    )

lumSystemBasicComplV13 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 13)
)
lumSystemBasicComplV13.setObjects(
      *(("LUM-SYSTEM-MIB", "sysGeneralGroupV5"),
        ("LUM-SYSTEM-MIB", "sysTimeGroupV2"),
        ("LUM-SYSTEM-MIB", "sysNodeGroupV6"),
        ("LUM-SYSTEM-MIB", "sysRadiusGroup"),
        ("LUM-SYSTEM-MIB", "sysLicenseGroup"),
        ("LUM-SYSTEM-MIB", "sysTacacsGroup"),
        ("LUM-SYSTEM-MIB", "sysUserGroupV2"))
)
if mibBuilder.loadTexts:
    lumSystemBasicComplV13.setStatus(
        "deprecated"
    )

lumSystemBasicComplV14 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 14)
)
lumSystemBasicComplV14.setObjects(
      *(("LUM-SYSTEM-MIB", "sysGeneralGroupV6"),
        ("LUM-SYSTEM-MIB", "sysTimeGroupV2"),
        ("LUM-SYSTEM-MIB", "sysNodeGroupV6"),
        ("LUM-SYSTEM-MIB", "sysRadiusGroup"),
        ("LUM-SYSTEM-MIB", "sysLicenseGroup"),
        ("LUM-SYSTEM-MIB", "sysTacacsGroupV2"),
        ("LUM-SYSTEM-MIB", "sysUserGroupV3"))
)
if mibBuilder.loadTexts:
    lumSystemBasicComplV14.setStatus(
        "deprecated"
    )

lumSystemBasicComplV15 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 15)
)
lumSystemBasicComplV15.setObjects(
      *(("LUM-SYSTEM-MIB", "sysGeneralGroupV6"),
        ("LUM-SYSTEM-MIB", "sysTimeGroupV2"),
        ("LUM-SYSTEM-MIB", "sysNodeGroupV6"),
        ("LUM-SYSTEM-MIB", "sysRadiusGroup"),
        ("LUM-SYSTEM-MIB", "sysLicenseGroup"),
        ("LUM-SYSTEM-MIB", "sysTacacsGroupV2"),
        ("LUM-SYSTEM-MIB", "sysUserGroupV4"))
)
if mibBuilder.loadTexts:
    lumSystemBasicComplV15.setStatus(
        "deprecated"
    )

lumSystemBasicComplV16 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 16)
)
lumSystemBasicComplV16.setObjects(
      *(("LUM-SYSTEM-MIB", "sysGeneralGroupV6"),
        ("LUM-SYSTEM-MIB", "sysTimeGroupV2"),
        ("LUM-SYSTEM-MIB", "sysNodeGroupV6"),
        ("LUM-SYSTEM-MIB", "sysRadiusGroup"),
        ("LUM-SYSTEM-MIB", "sysLicenseGroup"),
        ("LUM-SYSTEM-MIB", "sysTacacsGroupV2"),
        ("LUM-SYSTEM-MIB", "sysUserGroupV4"),
        ("LUM-SYSTEM-MIB", "sysSecurityGroupV1"))
)
if mibBuilder.loadTexts:
    lumSystemBasicComplV16.setStatus(
        "deprecated"
    )

lumSystemBasicComplV17 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 17)
)
lumSystemBasicComplV17.setObjects(
      *(("LUM-SYSTEM-MIB", "sysGeneralGroupV6"),
        ("LUM-SYSTEM-MIB", "sysTimeGroupV2"),
        ("LUM-SYSTEM-MIB", "sysNodeGroupV7"),
        ("LUM-SYSTEM-MIB", "sysRadiusGroup"),
        ("LUM-SYSTEM-MIB", "sysLicenseGroup"),
        ("LUM-SYSTEM-MIB", "sysTacacsGroupV2"),
        ("LUM-SYSTEM-MIB", "sysUserGroupV4"),
        ("LUM-SYSTEM-MIB", "sysSecurityGroupV1"))
)
if mibBuilder.loadTexts:
    lumSystemBasicComplV17.setStatus(
        "deprecated"
    )

lumSystemBasicComplV18 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 18)
)
lumSystemBasicComplV18.setObjects(
      *(("LUM-SYSTEM-MIB", "sysGeneralGroupV6"),
        ("LUM-SYSTEM-MIB", "sysTimeGroupV3"),
        ("LUM-SYSTEM-MIB", "sysNodeGroupV7"),
        ("LUM-SYSTEM-MIB", "sysRadiusGroupV2"),
        ("LUM-SYSTEM-MIB", "sysLicenseGroup"),
        ("LUM-SYSTEM-MIB", "sysTacacsGroupV3"),
        ("LUM-SYSTEM-MIB", "sysUserGroupV4"),
        ("LUM-SYSTEM-MIB", "sysSecurityGroupV1"))
)
if mibBuilder.loadTexts:
    lumSystemBasicComplV18.setStatus(
        "deprecated"
    )

lumSystemBasicComplV19 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 19)
)
lumSystemBasicComplV19.setObjects(
      *(("LUM-SYSTEM-MIB", "sysGeneralGroupV6"),
        ("LUM-SYSTEM-MIB", "sysTimeGroupV3"),
        ("LUM-SYSTEM-MIB", "sysNodeGroupV7"),
        ("LUM-SYSTEM-MIB", "sysRadiusGroupV2"),
        ("LUM-SYSTEM-MIB", "sysLicenseGroup"),
        ("LUM-SYSTEM-MIB", "sysTacacsGroupV3"),
        ("LUM-SYSTEM-MIB", "sysUserGroupV4"),
        ("LUM-SYSTEM-MIB", "sysSecurityGroupV2"))
)
if mibBuilder.loadTexts:
    lumSystemBasicComplV19.setStatus(
        "deprecated"
    )

lumSystemBasicComplV20 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 20)
)
lumSystemBasicComplV20.setObjects(
      *(("LUM-SYSTEM-MIB", "sysGeneralGroupV6"),
        ("LUM-SYSTEM-MIB", "sysTimeGroupV3"),
        ("LUM-SYSTEM-MIB", "sysNodeGroupV7"),
        ("LUM-SYSTEM-MIB", "sysRadiusGroupV3"),
        ("LUM-SYSTEM-MIB", "sysLicenseGroup"),
        ("LUM-SYSTEM-MIB", "sysTacacsGroupV3"),
        ("LUM-SYSTEM-MIB", "sysUserGroupV4"),
        ("LUM-SYSTEM-MIB", "sysSecurityGroupV2"))
)
if mibBuilder.loadTexts:
    lumSystemBasicComplV20.setStatus(
        "deprecated"
    )

lumSystemBasicComplV21 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 21)
)
lumSystemBasicComplV21.setObjects(
      *(("LUM-SYSTEM-MIB", "sysGeneralGroupV6"),
        ("LUM-SYSTEM-MIB", "sysTimeGroupV3"),
        ("LUM-SYSTEM-MIB", "sysNodeGroupV7"),
        ("LUM-SYSTEM-MIB", "sysRadiusGroupV4"),
        ("LUM-SYSTEM-MIB", "sysLicenseGroup"),
        ("LUM-SYSTEM-MIB", "sysTacacsGroupV3"),
        ("LUM-SYSTEM-MIB", "sysUserGroupV4"),
        ("LUM-SYSTEM-MIB", "sysSecurityGroupV2"))
)
if mibBuilder.loadTexts:
    lumSystemBasicComplV21.setStatus(
        "deprecated"
    )

lumSystemBasicComplV22 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 22)
)
lumSystemBasicComplV22.setObjects(
      *(("LUM-SYSTEM-MIB", "sysGeneralGroupV7"),
        ("LUM-SYSTEM-MIB", "sysTimeGroupV3"),
        ("LUM-SYSTEM-MIB", "sysNodeGroupV7"),
        ("LUM-SYSTEM-MIB", "sysRadiusGroupV4"),
        ("LUM-SYSTEM-MIB", "sysLicenseGroup"),
        ("LUM-SYSTEM-MIB", "sysTacacsGroupV3"),
        ("LUM-SYSTEM-MIB", "sysUserGroupV4"),
        ("LUM-SYSTEM-MIB", "sysSecurityGroupV2"))
)
if mibBuilder.loadTexts:
    lumSystemBasicComplV22.setStatus(
        "deprecated"
    )

lumSystemBasicComplV23 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 23)
)
lumSystemBasicComplV23.setObjects(
      *(("LUM-SYSTEM-MIB", "sysGeneralGroupV7"),
        ("LUM-SYSTEM-MIB", "sysTimeGroupV3"),
        ("LUM-SYSTEM-MIB", "sysNodeGroupV8"),
        ("LUM-SYSTEM-MIB", "sysRadiusGroupV4"),
        ("LUM-SYSTEM-MIB", "sysLicenseGroup"),
        ("LUM-SYSTEM-MIB", "sysTacacsGroupV3"),
        ("LUM-SYSTEM-MIB", "sysUserGroupV4"),
        ("LUM-SYSTEM-MIB", "sysSecurityGroupV2"))
)
if mibBuilder.loadTexts:
    lumSystemBasicComplV23.setStatus(
        "deprecated"
    )

lumSystemBasicComplV24 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 24)
)
lumSystemBasicComplV24.setObjects(
      *(("LUM-SYSTEM-MIB", "sysGeneralGroupV7"),
        ("LUM-SYSTEM-MIB", "sysTimeGroupV3"),
        ("LUM-SYSTEM-MIB", "sysNodeGroupV8"),
        ("LUM-SYSTEM-MIB", "sysRadiusGroupV4"),
        ("LUM-SYSTEM-MIB", "sysLicenseGroup"),
        ("LUM-SYSTEM-MIB", "sysTacacsGroupV3"),
        ("LUM-SYSTEM-MIB", "sysUserGroupV4"),
        ("LUM-SYSTEM-MIB", "sysSecurityGroupV4"))
)
if mibBuilder.loadTexts:
    lumSystemBasicComplV24.setStatus(
        "deprecated"
    )

lumSystemBasicComplV25 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 25)
)
lumSystemBasicComplV25.setObjects(
      *(("LUM-SYSTEM-MIB", "sysGeneralGroupV7"),
        ("LUM-SYSTEM-MIB", "sysTimeGroupV3"),
        ("LUM-SYSTEM-MIB", "sysNodeGroupV8"),
        ("LUM-SYSTEM-MIB", "sysRadiusGroupV4"),
        ("LUM-SYSTEM-MIB", "sysLicenseGroup"),
        ("LUM-SYSTEM-MIB", "sysTacacsGroupV3"),
        ("LUM-SYSTEM-MIB", "sysUserGroupV4"),
        ("LUM-SYSTEM-MIB", "sysSecurityGroupV5"))
)
if mibBuilder.loadTexts:
    lumSystemBasicComplV25.setStatus(
        "deprecated"
    )

lumSystemBasicComplV26 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 26)
)
lumSystemBasicComplV26.setObjects(
      *(("LUM-SYSTEM-MIB", "sysGeneralGroupV7"),
        ("LUM-SYSTEM-MIB", "sysTimeGroupV3"),
        ("LUM-SYSTEM-MIB", "sysNodeGroupV8"),
        ("LUM-SYSTEM-MIB", "sysRadiusGroupV4"),
        ("LUM-SYSTEM-MIB", "sysLicenseGroup"),
        ("LUM-SYSTEM-MIB", "sysTacacsGroupV3"),
        ("LUM-SYSTEM-MIB", "sysUserGroupV4"),
        ("LUM-SYSTEM-MIB", "sysSecurityGroupV5"))
)
if mibBuilder.loadTexts:
    lumSystemBasicComplV26.setStatus(
        "deprecated"
    )

lumSystemBasicComplV27 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 27)
)
lumSystemBasicComplV27.setObjects(
      *(("LUM-SYSTEM-MIB", "sysGeneralGroupV7"),
        ("LUM-SYSTEM-MIB", "sysTimeGroupV3"),
        ("LUM-SYSTEM-MIB", "sysNodeGroupV8"),
        ("LUM-SYSTEM-MIB", "sysRadiusGroupV4"),
        ("LUM-SYSTEM-MIB", "sysLicenseGroup"),
        ("LUM-SYSTEM-MIB", "sysTacacsGroupV3"),
        ("LUM-SYSTEM-MIB", "sysUserGroupV4"),
        ("LUM-SYSTEM-MIB", "sysSecurityGroupV6"))
)
if mibBuilder.loadTexts:
    lumSystemBasicComplV27.setStatus(
        "deprecated"
    )

lumSystemBasicComplV28 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 28)
)
lumSystemBasicComplV28.setObjects(
      *(("LUM-SYSTEM-MIB", "sysGeneralGroupV7"),
        ("LUM-SYSTEM-MIB", "sysTimeGroupV3"),
        ("LUM-SYSTEM-MIB", "sysNodeGroupV8"),
        ("LUM-SYSTEM-MIB", "sysRadiusGroupV4"),
        ("LUM-SYSTEM-MIB", "sysLicenseGroup"),
        ("LUM-SYSTEM-MIB", "sysTacacsGroupV3"),
        ("LUM-SYSTEM-MIB", "sysUserGroupV4"),
        ("LUM-SYSTEM-MIB", "sysSecurityGroupV6"),
        ("LUM-SYSTEM-MIB", "sysManagerGroupV1"))
)
if mibBuilder.loadTexts:
    lumSystemBasicComplV28.setStatus(
        "current"
    )

lumSystemMinimalComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 4, 1)
)
lumSystemMinimalComplV1.setObjects(
      *(("LUM-SYSTEM-MIB", "sysGeneralMinimalGroupV1"),
        ("LUM-SYSTEM-MIB", "sysTimeMinimalGroupV1"),
        ("LUM-SYSTEM-MIB", "sysNodeMinimalGroupV1"))
)
if mibBuilder.loadTexts:
    lumSystemMinimalComplV1.setStatus(
        "deprecated"
    )

lumSystemMinimalComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 4, 2)
)
lumSystemMinimalComplV2.setObjects(
      *(("LUM-SYSTEM-MIB", "sysGeneralMinimalGroupV1"),
        ("LUM-SYSTEM-MIB", "sysTimeMinimalGroupV1"),
        ("LUM-SYSTEM-MIB", "sysNodeMinimalGroupV2"))
)
if mibBuilder.loadTexts:
    lumSystemMinimalComplV2.setStatus(
        "deprecated"
    )

lumSystemMinimalComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 4, 3)
)
lumSystemMinimalComplV3.setObjects(
      *(("LUM-SYSTEM-MIB", "sysGeneralMinimalGroupV1"),
        ("LUM-SYSTEM-MIB", "sysTimeMinimalGroupV2"),
        ("LUM-SYSTEM-MIB", "sysNodeMinimalGroupV2"),
        ("LUM-SYSTEM-MIB", "sysRadiusMinimalGroupV1"))
)
if mibBuilder.loadTexts:
    lumSystemMinimalComplV3.setStatus(
        "deprecated"
    )

lumSystemMinimalComplV4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 4, 4)
)
lumSystemMinimalComplV4.setObjects(
      *(("LUM-SYSTEM-MIB", "sysGeneralMinimalGroupV1"),
        ("LUM-SYSTEM-MIB", "sysTimeMinimalGroupV3"),
        ("LUM-SYSTEM-MIB", "sysNodeMinimalGroupV2"),
        ("LUM-SYSTEM-MIB", "sysRadiusMinimalGroupV2"))
)
if mibBuilder.loadTexts:
    lumSystemMinimalComplV4.setStatus(
        "deprecated"
    )

lumSystemMinimalComplV5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 4, 5)
)
lumSystemMinimalComplV5.setObjects(
      *(("LUM-SYSTEM-MIB", "sysGeneralMinimalGroupV1"),
        ("LUM-SYSTEM-MIB", "sysTimeMinimalGroupV3"),
        ("LUM-SYSTEM-MIB", "sysNodeMinimalGroupV2"),
        ("LUM-SYSTEM-MIB", "sysRadiusMinimalGroupV3"))
)
if mibBuilder.loadTexts:
    lumSystemMinimalComplV5.setStatus(
        "deprecated"
    )

lumSystemMinimalComplV6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 4, 6)
)
lumSystemMinimalComplV6.setObjects(
      *(("LUM-SYSTEM-MIB", "sysGeneralMinimalGroupV1"),
        ("LUM-SYSTEM-MIB", "sysTimeMinimalGroupV3"),
        ("LUM-SYSTEM-MIB", "sysNodeMinimalGroupV2"),
        ("LUM-SYSTEM-MIB", "sysRadiusMinimalGroupV4"))
)
if mibBuilder.loadTexts:
    lumSystemMinimalComplV6.setStatus(
        "current"
    )

lumSystemMinimalComplV7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 4, 7)
)
lumSystemMinimalComplV7.setObjects(
      *(("LUM-SYSTEM-MIB", "sysGeneralMinimalGroupV1"),
        ("LUM-SYSTEM-MIB", "sysTimeMinimalGroupV3"),
        ("LUM-SYSTEM-MIB", "sysNodeMinimalGroupV2"),
        ("LUM-SYSTEM-MIB", "sysRadiusMinimalGroupV4"))
)
if mibBuilder.loadTexts:
    lumSystemMinimalComplV7.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-SYSTEM-MIB",
    **{"lumSystemMIBModule": lumSystemMIBModule,
       "lumSystemConfs": lumSystemConfs,
       "lumSystemGroups": lumSystemGroups,
       "sysGeneralGroup": sysGeneralGroup,
       "sysNodeGroup": sysNodeGroup,
       "sysHostListGroup": sysHostListGroup,
       "sysTimeGroup": sysTimeGroup,
       "sysLogListGroup": sysLogListGroup,
       "sysGeneralGroupV2": sysGeneralGroupV2,
       "sysNodeGroupV2": sysNodeGroupV2,
       "sysUserGroup": sysUserGroup,
       "sysNodeGroupV3": sysNodeGroupV3,
       "sysGeneralGroupV3": sysGeneralGroupV3,
       "sysNodeGroupV4": sysNodeGroupV4,
       "sysGeneralGroupV4": sysGeneralGroupV4,
       "sysNodeGroupV5": sysNodeGroupV5,
       "sysRadiusGroup": sysRadiusGroup,
       "sysNodeGroupV6": sysNodeGroupV6,
       "sysTimeGroupV2": sysTimeGroupV2,
       "sysLicenseGroup": sysLicenseGroup,
       "sysTacacsGroup": sysTacacsGroup,
       "sysUserGroupV2": sysUserGroupV2,
       "sysGeneralGroupV5": sysGeneralGroupV5,
       "sysUserGroupV3": sysUserGroupV3,
       "sysTacacsGroupV2": sysTacacsGroupV2,
       "sysGeneralGroupV6": sysGeneralGroupV6,
       "sysUserGroupV4": sysUserGroupV4,
       "sysSecurityGroupV1": sysSecurityGroupV1,
       "sysNodeGroupV7": sysNodeGroupV7,
       "sysTacacsGroupV3": sysTacacsGroupV3,
       "sysRadiusGroupV2": sysRadiusGroupV2,
       "sysTimeGroupV3": sysTimeGroupV3,
       "sysSecurityGroupV2": sysSecurityGroupV2,
       "sysRadiusGroupV3": sysRadiusGroupV3,
       "sysRadiusGroupV4": sysRadiusGroupV4,
       "sysGeneralGroupV7": sysGeneralGroupV7,
       "sysSecurityGroupV3": sysSecurityGroupV3,
       "sysNodeGroupV8": sysNodeGroupV8,
       "sysSecurityGroupV4": sysSecurityGroupV4,
       "sysSecurityGroupV5": sysSecurityGroupV5,
       "sysSecurityGroupV6": sysSecurityGroupV6,
       "sysManagerGroupV1": sysManagerGroupV1,
       "lumSystemCompl": lumSystemCompl,
       "lumSystemBasicComplV1": lumSystemBasicComplV1,
       "lumSystemBasicComplV2": lumSystemBasicComplV2,
       "lumSystemBasicComplV3": lumSystemBasicComplV3,
       "lumSystemBasicComplV4": lumSystemBasicComplV4,
       "lumSystemBasicComplV5": lumSystemBasicComplV5,
       "lumSystemBasicComplV6": lumSystemBasicComplV6,
       "lumSystemBasicComplV7": lumSystemBasicComplV7,
       "lumSystemBasicComplV8": lumSystemBasicComplV8,
       "lumSystemBasicComplV9": lumSystemBasicComplV9,
       "lumSystemBasicComplV10": lumSystemBasicComplV10,
       "lumSystemBasicComplV11": lumSystemBasicComplV11,
       "lumSystemBasicComplV12": lumSystemBasicComplV12,
       "lumSystemBasicComplV13": lumSystemBasicComplV13,
       "lumSystemBasicComplV14": lumSystemBasicComplV14,
       "lumSystemBasicComplV15": lumSystemBasicComplV15,
       "lumSystemBasicComplV16": lumSystemBasicComplV16,
       "lumSystemBasicComplV17": lumSystemBasicComplV17,
       "lumSystemBasicComplV18": lumSystemBasicComplV18,
       "lumSystemBasicComplV19": lumSystemBasicComplV19,
       "lumSystemBasicComplV20": lumSystemBasicComplV20,
       "lumSystemBasicComplV21": lumSystemBasicComplV21,
       "lumSystemBasicComplV22": lumSystemBasicComplV22,
       "lumSystemBasicComplV23": lumSystemBasicComplV23,
       "lumSystemBasicComplV24": lumSystemBasicComplV24,
       "lumSystemBasicComplV25": lumSystemBasicComplV25,
       "lumSystemBasicComplV26": lumSystemBasicComplV26,
       "lumSystemBasicComplV27": lumSystemBasicComplV27,
       "lumSystemBasicComplV28": lumSystemBasicComplV28,
       "lumSystemMinimalGroups": lumSystemMinimalGroups,
       "sysGeneralMinimalGroupV1": sysGeneralMinimalGroupV1,
       "sysNodeMinimalGroupV1": sysNodeMinimalGroupV1,
       "sysTimeMinimalGroupV1": sysTimeMinimalGroupV1,
       "sysNodeMinimalGroupV2": sysNodeMinimalGroupV2,
       "sysTimeMinimalGroupV2": sysTimeMinimalGroupV2,
       "sysRadiusMinimalGroupV1": sysRadiusMinimalGroupV1,
       "sysTimeMinimalGroupV3": sysTimeMinimalGroupV3,
       "sysRadiusMinimalGroupV2": sysRadiusMinimalGroupV2,
       "sysRadiusMinimalGroupV3": sysRadiusMinimalGroupV3,
       "sysRadiusMinimalGroupV4": sysRadiusMinimalGroupV4,
       "lumSystemMinimalCompl": lumSystemMinimalCompl,
       "lumSystemMinimalComplV1": lumSystemMinimalComplV1,
       "lumSystemMinimalComplV2": lumSystemMinimalComplV2,
       "lumSystemMinimalComplV3": lumSystemMinimalComplV3,
       "lumSystemMinimalComplV4": lumSystemMinimalComplV4,
       "lumSystemMinimalComplV5": lumSystemMinimalComplV5,
       "lumSystemMinimalComplV6": lumSystemMinimalComplV6,
       "lumSystemMinimalComplV7": lumSystemMinimalComplV7,
       "lumSystemMIBObjects": lumSystemMIBObjects,
       "sysGeneral": sysGeneral,
       "sysGeneralTestAndIncr": sysGeneralTestAndIncr,
       "sysGeneralMibSpecVersion": sysGeneralMibSpecVersion,
       "sysGeneralMibImplVersion": sysGeneralMibImplVersion,
       "sysGeneralLastChangeTime": sysGeneralLastChangeTime,
       "sysGeneralTest": sysGeneralTest,
       "sysGeneralConfigLastChangeTime": sysGeneralConfigLastChangeTime,
       "sysGeneralLoginRecords": sysGeneralLoginRecords,
       "sysGeneralUserTableSize": sysGeneralUserTableSize,
       "sysGeneralWriteTest": sysGeneralWriteTest,
       "sysNode": sysNode,
       "sysNodeName": sysNodeName,
       "sysNodeContact": sysNodeContact,
       "sysNodeLocation": sysNodeLocation,
       "sysNodeObjectId": sysNodeObjectId,
       "sysNodePrimaryNameServer": sysNodePrimaryNameServer,
       "sysNodeRunLevel": sysNodeRunLevel,
       "sysNodeSecondaryNameServer": sysNodeSecondaryNameServer,
       "sysNodeUptime": sysNodeUptime,
       "sysNodeNeType": sysNodeNeType,
       "sysNodeNeUserName": sysNodeNeUserName,
       "sysNodeNeDistinguishedName": sysNodeNeDistinguishedName,
       "sysNodeBootTime": sysNodeBootTime,
       "sysNodeLocale": sysNodeLocale,
       "sysNodeVersion": sysNodeVersion,
       "sysNodeCLLI": sysNodeCLLI,
       "sysNodeFIC": sysNodeFIC,
       "sysNodeTID": sysNodeTID,
       "sysNodeLatitude": sysNodeLatitude,
       "sysNodeLongitude": sysNodeLongitude,
       "sysHostList": sysHostList,
       "sysHostTable": sysHostTable,
       "sysHostEntry": sysHostEntry,
       "sysHostIndex": sysHostIndex,
       "sysHostIpAddress": sysHostIpAddress,
       "sysHostNames": sysHostNames,
       "sysHostRowStatus": sysHostRowStatus,
       "sysTime": sysTime,
       "sysTimeLocal": sysTimeLocal,
       "sysTimeZone": sysTimeZone,
       "sysTimePrimaryServer": sysTimePrimaryServer,
       "sysTimeSecondaryServer": sysTimeSecondaryServer,
       "sysTimeChangeLocalTime": sysTimeChangeLocalTime,
       "sysTimePrimaryIpAddress": sysTimePrimaryIpAddress,
       "sysTimeSecondaryIpAddress": sysTimeSecondaryIpAddress,
       "sysLogList": sysLogList,
       "sysLogTable": sysLogTable,
       "sysLogEntry": sysLogEntry,
       "sysLogIndex": sysLogIndex,
       "sysLogSelection": sysLogSelection,
       "sysLogAction": sysLogAction,
       "sysLogRowStatus": sysLogRowStatus,
       "sysUserList": sysUserList,
       "sysUserTable": sysUserTable,
       "sysUserEntry": sysUserEntry,
       "sysUserIndex": sysUserIndex,
       "sysUserName": sysUserName,
       "sysUserPasswd": sysUserPasswd,
       "sysUserDescr": sysUserDescr,
       "sysUserLastChangeTime": sysUserLastChangeTime,
       "sysUserExpireTime": sysUserExpireTime,
       "sysUserRowStatus": sysUserRowStatus,
       "sysUserProfile": sysUserProfile,
       "sysUserUid": sysUserUid,
       "sysUserChangePassword": sysUserChangePassword,
       "sysUserClearPassword": sysUserClearPassword,
       "sysUserDisable": sysUserDisable,
       "sysUserEnable": sysUserEnable,
       "sysUserMode": sysUserMode,
       "sysRadius": sysRadius,
       "sysRadiusPrimaryServer": sysRadiusPrimaryServer,
       "sysRadiusPrimarySecret": sysRadiusPrimarySecret,
       "sysRadiusSecondaryServer": sysRadiusSecondaryServer,
       "sysRadiusSecondarySecret": sysRadiusSecondarySecret,
       "sysRadiusPrimaryIpAddress": sysRadiusPrimaryIpAddress,
       "sysRadiusSecondaryIpAddress": sysRadiusSecondaryIpAddress,
       "sysRadiusPrimaryPort": sysRadiusPrimaryPort,
       "sysRadiusSecondaryPort": sysRadiusSecondaryPort,
       "sysRadiusDefaultUserProfile": sysRadiusDefaultUserProfile,
       "sysLicense": sysLicense,
       "sysLicenseExpireDate": sysLicenseExpireDate,
       "sysLicenseCustomer": sysLicenseCustomer,
       "sysLicenseExpiresSoon": sysLicenseExpiresSoon,
       "sysLicenseExpired": sysLicenseExpired,
       "sysLicenseExpiredCause": sysLicenseExpiredCause,
       "sysLicenseFeatureEws": sysLicenseFeatureEws,
       "sysLicenseFeatureOspf": sysLicenseFeatureOspf,
       "sysLicenseFeatureSnmp": sysLicenseFeatureSnmp,
       "sysLicenseFeatureGmpls": sysLicenseFeatureGmpls,
       "sysLicenseFeatureRudb": sysLicenseFeatureRudb,
       "sysLicenseInstallLicenseFile": sysLicenseInstallLicenseFile,
       "sysTacacs": sysTacacs,
       "sysTacacsPrimaryServer": sysTacacsPrimaryServer,
       "sysTacacsSecondaryServer": sysTacacsSecondaryServer,
       "sysTacacsSecret": sysTacacsSecret,
       "sysTacacsSecondarySecret": sysTacacsSecondarySecret,
       "sysTacacsPrimaryIpAddress": sysTacacsPrimaryIpAddress,
       "sysTacacsSecondaryIpAddress": sysTacacsSecondaryIpAddress,
       "sysAudit": sysAudit,
       "sysSecurity": sysSecurity,
       "sysSecurityLocalConsoleAccess": sysSecurityLocalConsoleAccess,
       "sysSecurityChangeLocalConsoleAccess": sysSecurityChangeLocalConsoleAccess,
       "sysSecurityIpTablesStatus": sysSecurityIpTablesStatus,
       "sysSecurityLocalCraftAccess": sysSecurityLocalCraftAccess,
       "sysSecurityChangeLocalCraftAccess": sysSecurityChangeLocalCraftAccess,
       "sysSecurityAuthenticationOrder": sysSecurityAuthenticationOrder,
       "sysSecurityFileSystemAccessRestrictions": sysSecurityFileSystemAccessRestrictions,
       "sysSecurityCUFrontICNPortAccess": sysSecurityCUFrontICNPortAccess,
       "sysSecurityChangeCUFrontICNPortAccess": sysSecurityChangeCUFrontICNPortAccess,
       "sysSecuritySubrackICNPortAccess": sysSecuritySubrackICNPortAccess,
       "sysSecurityChangeSubrackICNPortAccess": sysSecurityChangeSubrackICNPortAccess,
       "sysSecurityMgmtAccessProofOfConnStatus": sysSecurityMgmtAccessProofOfConnStatus,
       "sysSecurityMgmtAccessProofOfConnectivity": sysSecurityMgmtAccessProofOfConnectivity,
       "sysSecurityAutoEnableBlockedMgmtPorts": sysSecurityAutoEnableBlockedMgmtPorts,
       "sysSecurityBlockedMgmtPortsUnblocked": sysSecurityBlockedMgmtPortsUnblocked,
       "sysManager": sysManager,
       "sysManagerName": sysManagerName,
       "sysManagerIPAddress": sysManagerIPAddress,
       "sysManagerPolicyName": sysManagerPolicyName,
       "sysManagerPlatform": sysManagerPlatform}
)
