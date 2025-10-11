# SNMP MIB module (ALCATEL-ENT1-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/alcatel-ent1/ALCATEL-ENT1-SYSTEM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:10:31 2025
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

(hardentIND1System,) = mibBuilder.importSymbols(
    "ALCATEL-ENT1-BASE",
    "hardentIND1System")

(VirtualOperChassisId,
 virtualChassisOperChasId) = mibBuilder.importSymbols(
    "ALCATEL-ENT1-VIRTUAL-CHASSIS-MIB",
    "VirtualOperChassisId",
    "virtualChassisOperChasId")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

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

alcatelIND1SystemMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1SystemMIB.setRevisions(
        ("2011-01-23 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SystemFileType(TextualConvention, Integer32):
    status = "current"
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
        *(("file", 1),
          ("directory", 2),
          ("undefined", 3),
          ("tarArchive", 4))
    )



class SwitchLoggingIndex(TextualConvention, Integer32):
    status = "current"
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
        *(("console", 1),
          ("flash", 2),
          ("socket", 3),
          ("ipaddr", 4))
    )



class AppIdIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )



class Enable(TextualConvention, Integer32):
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



class FileSystemIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flash", 1),
          ("uflash", 2))
    )



class SeverityLevel(TextualConvention, Integer32):
    status = "current"
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
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("severityLevelOff", 0),
          ("severityLevelAlarm", 1),
          ("severityLevelError", 2),
          ("severityLevelAlert", 3),
          ("severityLevelWarn", 4),
          ("severityLevelInfo", 5),
          ("severityLevelDbg1", 6),
          ("severityLevelDbg2", 7),
          ("severityLevelDbg3", 8))
    )



class SysLogFacilityId(TextualConvention, Integer32):
    status = "current"
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
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("uucp", 0),
          ("user", 1),
          ("system", 2),
          ("syslog", 3),
          ("secAuth2", 4),
          ("secAuth1", 5),
          ("ntp", 6),
          ("netNews", 7),
          ("mail", 8),
          ("lptr", 9),
          ("logAudit", 10),
          ("logAlert", 11),
          ("local7", 12),
          ("local6", 13),
          ("local5", 14),
          ("local4", 15),
          ("local3", 16),
          ("local2", 17),
          ("local1", 18),
          ("local0", 19),
          ("kernel", 20),
          ("ftp", 21),
          ("clock2", 22),
          ("clock1", 23))
    )



class CommandPercentComplete(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class VrfId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )



class AgeLimit(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1SystemMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1SystemMIBObjects = _AlcatelIND1SystemMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1SystemMIBObjects.setStatus("current")
_SystemMicrocode_ObjectIdentity = ObjectIdentity
systemMicrocode = _SystemMicrocode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 1)
)
_SystemMicrocodePackageTable_Object = MibTable
systemMicrocodePackageTable = _SystemMicrocodePackageTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    systemMicrocodePackageTable.setStatus("current")
_SystemMicrocodePackageEntry_Object = MibTableRow
systemMicrocodePackageEntry = _SystemMicrocodePackageEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 1, 1, 1)
)
systemMicrocodePackageEntry.setIndexNames(
    (0, "ALCATEL-ENT1-SYSTEM-MIB", "systemMicrocodePackageDirectoryIndex"),
    (0, "ALCATEL-ENT1-SYSTEM-MIB", "systemMicrocodePackageDirectory"),
    (0, "ALCATEL-ENT1-SYSTEM-MIB", "systemMicrocodePackageIndex"),
)
if mibBuilder.loadTexts:
    systemMicrocodePackageEntry.setStatus("current")
_SystemMicrocodePackageDirectoryIndex_Type = Unsigned32
_SystemMicrocodePackageDirectoryIndex_Object = MibTableColumn
systemMicrocodePackageDirectoryIndex = _SystemMicrocodePackageDirectoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1),
    _SystemMicrocodePackageDirectoryIndex_Type()
)
systemMicrocodePackageDirectoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    systemMicrocodePackageDirectoryIndex.setStatus("current")


class _SystemMicrocodePackageDirectory_Type(SnmpAdminString):
    """Custom type systemMicrocodePackageDirectory based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 108),
    )


_SystemMicrocodePackageDirectory_Type.__name__ = "SnmpAdminString"
_SystemMicrocodePackageDirectory_Object = MibTableColumn
systemMicrocodePackageDirectory = _SystemMicrocodePackageDirectory_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2),
    _SystemMicrocodePackageDirectory_Type()
)
systemMicrocodePackageDirectory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    systemMicrocodePackageDirectory.setStatus("current")
_SystemMicrocodePackageIndex_Type = Unsigned32
_SystemMicrocodePackageIndex_Object = MibTableColumn
systemMicrocodePackageIndex = _SystemMicrocodePackageIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 1, 1, 1, 3),
    _SystemMicrocodePackageIndex_Type()
)
systemMicrocodePackageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    systemMicrocodePackageIndex.setStatus("current")


class _SystemMicrocodePackageVersion_Type(SnmpAdminString):
    """Custom type systemMicrocodePackageVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemMicrocodePackageVersion_Type.__name__ = "SnmpAdminString"
_SystemMicrocodePackageVersion_Object = MibTableColumn
systemMicrocodePackageVersion = _SystemMicrocodePackageVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 1, 1, 1, 4),
    _SystemMicrocodePackageVersion_Type()
)
systemMicrocodePackageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemMicrocodePackageVersion.setStatus("current")


class _SystemMicrocodePackageName_Type(SnmpAdminString):
    """Custom type systemMicrocodePackageName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemMicrocodePackageName_Type.__name__ = "SnmpAdminString"
_SystemMicrocodePackageName_Object = MibTableColumn
systemMicrocodePackageName = _SystemMicrocodePackageName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 1, 1, 1, 5),
    _SystemMicrocodePackageName_Type()
)
systemMicrocodePackageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemMicrocodePackageName.setStatus("current")


class _SystemMicrocodePackageDescription_Type(SnmpAdminString):
    """Custom type systemMicrocodePackageDescription based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemMicrocodePackageDescription_Type.__name__ = "SnmpAdminString"
_SystemMicrocodePackageDescription_Object = MibTableColumn
systemMicrocodePackageDescription = _SystemMicrocodePackageDescription_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 1, 1, 1, 6),
    _SystemMicrocodePackageDescription_Type()
)
systemMicrocodePackageDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemMicrocodePackageDescription.setStatus("current")


class _SystemMicrocodePackageStatus_Type(Integer32):
    """Custom type systemMicrocodePackageStatus based on Integer32"""
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
        *(("undefined", 1),
          ("ok", 2),
          ("inuse", 3))
    )


_SystemMicrocodePackageStatus_Type.__name__ = "Integer32"
_SystemMicrocodePackageStatus_Object = MibTableColumn
systemMicrocodePackageStatus = _SystemMicrocodePackageStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 1, 1, 1, 7),
    _SystemMicrocodePackageStatus_Type()
)
systemMicrocodePackageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemMicrocodePackageStatus.setStatus("current")


class _SystemMicrocodePackageSize_Type(Unsigned32):
    """Custom type systemMicrocodePackageSize based on Unsigned32"""
    defaultValue = 0


_SystemMicrocodePackageSize_Type.__name__ = "Unsigned32"
_SystemMicrocodePackageSize_Object = MibTableColumn
systemMicrocodePackageSize = _SystemMicrocodePackageSize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 1, 1, 1, 8),
    _SystemMicrocodePackageSize_Type()
)
systemMicrocodePackageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemMicrocodePackageSize.setStatus("current")
_SystemMicrocodeLoadedTable_Object = MibTable
systemMicrocodeLoadedTable = _SystemMicrocodeLoadedTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    systemMicrocodeLoadedTable.setStatus("current")
_SystemMicrocodeLoadedEntry_Object = MibTableRow
systemMicrocodeLoadedEntry = _SystemMicrocodeLoadedEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 1, 2, 1)
)
systemMicrocodeLoadedEntry.setIndexNames(
    (0, "ALCATEL-ENT1-SYSTEM-MIB", "systemMicrocodeLoadedIndex"),
)
if mibBuilder.loadTexts:
    systemMicrocodeLoadedEntry.setStatus("current")
_SystemMicrocodeLoadedIndex_Type = Unsigned32
_SystemMicrocodeLoadedIndex_Object = MibTableColumn
systemMicrocodeLoadedIndex = _SystemMicrocodeLoadedIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1),
    _SystemMicrocodeLoadedIndex_Type()
)
systemMicrocodeLoadedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    systemMicrocodeLoadedIndex.setStatus("current")


class _SystemMicrocodeLoadedDirectory_Type(SnmpAdminString):
    """Custom type systemMicrocodeLoadedDirectory based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 108),
    )


_SystemMicrocodeLoadedDirectory_Type.__name__ = "SnmpAdminString"
_SystemMicrocodeLoadedDirectory_Object = MibTableColumn
systemMicrocodeLoadedDirectory = _SystemMicrocodeLoadedDirectory_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2),
    _SystemMicrocodeLoadedDirectory_Type()
)
systemMicrocodeLoadedDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemMicrocodeLoadedDirectory.setStatus("current")


class _SystemMicrocodeLoadedVersion_Type(SnmpAdminString):
    """Custom type systemMicrocodeLoadedVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemMicrocodeLoadedVersion_Type.__name__ = "SnmpAdminString"
_SystemMicrocodeLoadedVersion_Object = MibTableColumn
systemMicrocodeLoadedVersion = _SystemMicrocodeLoadedVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 1, 2, 1, 3),
    _SystemMicrocodeLoadedVersion_Type()
)
systemMicrocodeLoadedVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemMicrocodeLoadedVersion.setStatus("current")


class _SystemMicrocodeLoadedName_Type(SnmpAdminString):
    """Custom type systemMicrocodeLoadedName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemMicrocodeLoadedName_Type.__name__ = "SnmpAdminString"
_SystemMicrocodeLoadedName_Object = MibTableColumn
systemMicrocodeLoadedName = _SystemMicrocodeLoadedName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 1, 2, 1, 4),
    _SystemMicrocodeLoadedName_Type()
)
systemMicrocodeLoadedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemMicrocodeLoadedName.setStatus("current")


class _SystemMicrocodeLoadedDescription_Type(SnmpAdminString):
    """Custom type systemMicrocodeLoadedDescription based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemMicrocodeLoadedDescription_Type.__name__ = "SnmpAdminString"
_SystemMicrocodeLoadedDescription_Object = MibTableColumn
systemMicrocodeLoadedDescription = _SystemMicrocodeLoadedDescription_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 1, 2, 1, 5),
    _SystemMicrocodeLoadedDescription_Type()
)
systemMicrocodeLoadedDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemMicrocodeLoadedDescription.setStatus("current")


class _SystemMicrocodeLoadedSize_Type(Unsigned32):
    """Custom type systemMicrocodeLoadedSize based on Unsigned32"""
    defaultValue = 0


_SystemMicrocodeLoadedSize_Type.__name__ = "Unsigned32"
_SystemMicrocodeLoadedSize_Object = MibTableColumn
systemMicrocodeLoadedSize = _SystemMicrocodeLoadedSize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 1, 2, 1, 6),
    _SystemMicrocodeLoadedSize_Type()
)
systemMicrocodeLoadedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemMicrocodeLoadedSize.setStatus("current")
_SystemBootParams_ObjectIdentity = ObjectIdentity
systemBootParams = _SystemBootParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 2)
)
_SystemBootNetwork_Type = IpAddress
_SystemBootNetwork_Object = MibScalar
systemBootNetwork = _SystemBootNetwork_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 2, 1),
    _SystemBootNetwork_Type()
)
systemBootNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBootNetwork.setStatus("current")
_SystemBootNetworkGateway_Type = IpAddress
_SystemBootNetworkGateway_Object = MibScalar
systemBootNetworkGateway = _SystemBootNetworkGateway_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 2, 2),
    _SystemBootNetworkGateway_Type()
)
systemBootNetworkGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBootNetworkGateway.setStatus("current")
_SystemBootNetworkNetmask_Type = IpAddress
_SystemBootNetworkNetmask_Object = MibScalar
systemBootNetworkNetmask = _SystemBootNetworkNetmask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 2, 3),
    _SystemBootNetworkNetmask_Type()
)
systemBootNetworkNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBootNetworkNetmask.setStatus("current")
_SystemHardware_ObjectIdentity = ObjectIdentity
systemHardware = _SystemHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3)
)


class _SystemHardwareFlashMfg_Type(Integer32):
    """Custom type systemHardwareFlashMfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              13)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("amd", 2),
          ("intel", 3),
          ("atmel", 4),
          ("micron", 5),
          ("kingston", 6),
          ("toshiba", 7),
          ("sandisk", 8),
          ("sst", 9),
          ("spansion", 10),
          ("wintec", 13))
    )


_SystemHardwareFlashMfg_Type.__name__ = "Integer32"
_SystemHardwareFlashMfg_Object = MibScalar
systemHardwareFlashMfg = _SystemHardwareFlashMfg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 1),
    _SystemHardwareFlashMfg_Type()
)
systemHardwareFlashMfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareFlashMfg.setStatus("current")
_SystemHardwareFlashSize_Type = Unsigned32
_SystemHardwareFlashSize_Object = MibScalar
systemHardwareFlashSize = _SystemHardwareFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 2),
    _SystemHardwareFlashSize_Type()
)
systemHardwareFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareFlashSize.setStatus("current")


class _SystemHardwareMemoryMfg_Type(Integer32):
    """Custom type systemHardwareMemoryMfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("amd", 2),
          ("intel", 3),
          ("atmel", 4),
          ("micron", 5),
          ("kingston", 6),
          ("toshiba", 7),
          ("agilent", 8),
          ("dataram", 10),
          ("interward", 11),
          ("notreadable", 12))
    )


_SystemHardwareMemoryMfg_Type.__name__ = "Integer32"
_SystemHardwareMemoryMfg_Object = MibScalar
systemHardwareMemoryMfg = _SystemHardwareMemoryMfg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 3),
    _SystemHardwareMemoryMfg_Type()
)
systemHardwareMemoryMfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareMemoryMfg.setStatus("current")
_SystemHardwareMemorySize_Type = Unsigned32
_SystemHardwareMemorySize_Object = MibScalar
systemHardwareMemorySize = _SystemHardwareMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 4),
    _SystemHardwareMemorySize_Type()
)
systemHardwareMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareMemorySize.setStatus("current")
_SystemHardwareNVRAMBatteryLow_Type = TruthValue
_SystemHardwareNVRAMBatteryLow_Object = MibScalar
systemHardwareNVRAMBatteryLow = _SystemHardwareNVRAMBatteryLow_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 5),
    _SystemHardwareNVRAMBatteryLow_Type()
)
systemHardwareNVRAMBatteryLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareNVRAMBatteryLow.setStatus("current")


class _SystemHardwareBootCpuType_Type(Integer32):
    """Custom type systemHardwareBootCpuType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("sparc380", 2),
          ("sparcV9", 3),
          ("ppc", 4),
          ("ppc8540", 5),
          ("ppc8572", 6),
          ("arm", 7))
    )


_SystemHardwareBootCpuType_Type.__name__ = "Integer32"
_SystemHardwareBootCpuType_Object = MibScalar
systemHardwareBootCpuType = _SystemHardwareBootCpuType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 6),
    _SystemHardwareBootCpuType_Type()
)
systemHardwareBootCpuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareBootCpuType.setStatus("current")


class _SystemHardwareJumperInterruptBoot_Type(TruthValue):
    """Custom type systemHardwareJumperInterruptBoot based on TruthValue"""
    defaultValue = 2


_SystemHardwareJumperInterruptBoot_Type.__name__ = "TruthValue"
_SystemHardwareJumperInterruptBoot_Object = MibScalar
systemHardwareJumperInterruptBoot = _SystemHardwareJumperInterruptBoot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 7),
    _SystemHardwareJumperInterruptBoot_Type()
)
systemHardwareJumperInterruptBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareJumperInterruptBoot.setStatus("current")


class _SystemHardwareJumperForceUartDefaults_Type(TruthValue):
    """Custom type systemHardwareJumperForceUartDefaults based on TruthValue"""
    defaultValue = 2


_SystemHardwareJumperForceUartDefaults_Type.__name__ = "TruthValue"
_SystemHardwareJumperForceUartDefaults_Object = MibScalar
systemHardwareJumperForceUartDefaults = _SystemHardwareJumperForceUartDefaults_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 8),
    _SystemHardwareJumperForceUartDefaults_Type()
)
systemHardwareJumperForceUartDefaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareJumperForceUartDefaults.setStatus("current")


class _SystemHardwareJumperRunExtendedMemoryDiagnostics_Type(TruthValue):
    """Custom type systemHardwareJumperRunExtendedMemoryDiagnostics based on TruthValue"""
    defaultValue = 2


_SystemHardwareJumperRunExtendedMemoryDiagnostics_Type.__name__ = "TruthValue"
_SystemHardwareJumperRunExtendedMemoryDiagnostics_Object = MibScalar
systemHardwareJumperRunExtendedMemoryDiagnostics = _SystemHardwareJumperRunExtendedMemoryDiagnostics_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 9),
    _SystemHardwareJumperRunExtendedMemoryDiagnostics_Type()
)
systemHardwareJumperRunExtendedMemoryDiagnostics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareJumperRunExtendedMemoryDiagnostics.setStatus("current")


class _SystemHardwareJumperSpare_Type(TruthValue):
    """Custom type systemHardwareJumperSpare based on TruthValue"""
    defaultValue = 2


_SystemHardwareJumperSpare_Type.__name__ = "TruthValue"
_SystemHardwareJumperSpare_Object = MibScalar
systemHardwareJumperSpare = _SystemHardwareJumperSpare_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 10),
    _SystemHardwareJumperSpare_Type()
)
systemHardwareJumperSpare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareJumperSpare.setStatus("current")
_SystemHardwareFpgaVersionTable_Object = MibTable
systemHardwareFpgaVersionTable = _SystemHardwareFpgaVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 11)
)
if mibBuilder.loadTexts:
    systemHardwareFpgaVersionTable.setStatus("current")
_SystemHardwareFpgaVersionEntry_Object = MibTableRow
systemHardwareFpgaVersionEntry = _SystemHardwareFpgaVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 11, 1)
)
systemHardwareFpgaVersionEntry.setIndexNames(
    (0, "ALCATEL-ENT1-SYSTEM-MIB", "systemHardwareFpgaVersionIndex"),
)
if mibBuilder.loadTexts:
    systemHardwareFpgaVersionEntry.setStatus("current")


class _SystemHardwareFpgaVersionIndex_Type(Integer32):
    """Custom type systemHardwareFpgaVersionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SystemHardwareFpgaVersionIndex_Type.__name__ = "Integer32"
_SystemHardwareFpgaVersionIndex_Object = MibTableColumn
systemHardwareFpgaVersionIndex = _SystemHardwareFpgaVersionIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 11, 1, 1),
    _SystemHardwareFpgaVersionIndex_Type()
)
systemHardwareFpgaVersionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareFpgaVersionIndex.setStatus("current")
_SystemHardwareFpgaVersion_Type = Unsigned32
_SystemHardwareFpgaVersion_Object = MibTableColumn
systemHardwareFpgaVersion = _SystemHardwareFpgaVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 11, 1, 2),
    _SystemHardwareFpgaVersion_Type()
)
systemHardwareFpgaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareFpgaVersion.setStatus("current")


class _SystemHardwareBootRomVersion_Type(SnmpAdminString):
    """Custom type systemHardwareBootRomVersion based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemHardwareBootRomVersion_Type.__name__ = "SnmpAdminString"
_SystemHardwareBootRomVersion_Object = MibScalar
systemHardwareBootRomVersion = _SystemHardwareBootRomVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 12),
    _SystemHardwareBootRomVersion_Type()
)
systemHardwareBootRomVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareBootRomVersion.setStatus("current")


class _SystemHardwareBackupMiniBootVersion_Type(SnmpAdminString):
    """Custom type systemHardwareBackupMiniBootVersion based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemHardwareBackupMiniBootVersion_Type.__name__ = "SnmpAdminString"
_SystemHardwareBackupMiniBootVersion_Object = MibScalar
systemHardwareBackupMiniBootVersion = _SystemHardwareBackupMiniBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 13),
    _SystemHardwareBackupMiniBootVersion_Type()
)
systemHardwareBackupMiniBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareBackupMiniBootVersion.setStatus("current")


class _SystemHardwareDefaultMiniBootVersion_Type(SnmpAdminString):
    """Custom type systemHardwareDefaultMiniBootVersion based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemHardwareDefaultMiniBootVersion_Type.__name__ = "SnmpAdminString"
_SystemHardwareDefaultMiniBootVersion_Object = MibScalar
systemHardwareDefaultMiniBootVersion = _SystemHardwareDefaultMiniBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 14),
    _SystemHardwareDefaultMiniBootVersion_Type()
)
systemHardwareDefaultMiniBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareDefaultMiniBootVersion.setStatus("current")


class _SystemHardwareMinorFpgaVersion_Type(SnmpAdminString):
    """Custom type systemHardwareMinorFpgaVersion based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemHardwareMinorFpgaVersion_Type.__name__ = "SnmpAdminString"
_SystemHardwareMinorFpgaVersion_Object = MibScalar
systemHardwareMinorFpgaVersion = _SystemHardwareMinorFpgaVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 15),
    _SystemHardwareMinorFpgaVersion_Type()
)
systemHardwareMinorFpgaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareMinorFpgaVersion.setStatus("current")


class _SystemHardwareCpldVersion_Type(SnmpAdminString):
    """Custom type systemHardwareCpldVersion based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemHardwareCpldVersion_Type.__name__ = "SnmpAdminString"
_SystemHardwareCpldVersion_Object = MibScalar
systemHardwareCpldVersion = _SystemHardwareCpldVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 16),
    _SystemHardwareCpldVersion_Type()
)
systemHardwareCpldVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareCpldVersion.setStatus("current")


class _SystemHardwareUbootVersion_Type(SnmpAdminString):
    """Custom type systemHardwareUbootVersion based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemHardwareUbootVersion_Type.__name__ = "SnmpAdminString"
_SystemHardwareUbootVersion_Object = MibScalar
systemHardwareUbootVersion = _SystemHardwareUbootVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 17),
    _SystemHardwareUbootVersion_Type()
)
systemHardwareUbootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareUbootVersion.setStatus("current")


class _SystemHardwareProdRegId_Type(SnmpAdminString):
    """Custom type systemHardwareProdRegId based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemHardwareProdRegId_Type.__name__ = "SnmpAdminString"
_SystemHardwareProdRegId_Object = MibScalar
systemHardwareProdRegId = _SystemHardwareProdRegId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 18),
    _SystemHardwareProdRegId_Type()
)
systemHardwareProdRegId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareProdRegId.setStatus("current")


class _SystemHardwareRevisionRegister_Type(SnmpAdminString):
    """Custom type systemHardwareRevisionRegister based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemHardwareRevisionRegister_Type.__name__ = "SnmpAdminString"
_SystemHardwareRevisionRegister_Object = MibScalar
systemHardwareRevisionRegister = _SystemHardwareRevisionRegister_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 19),
    _SystemHardwareRevisionRegister_Type()
)
systemHardwareRevisionRegister.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareRevisionRegister.setStatus("current")


class _SystemHardwareXfpId_Type(SnmpAdminString):
    """Custom type systemHardwareXfpId based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemHardwareXfpId_Type.__name__ = "SnmpAdminString"
_SystemHardwareXfpId_Object = MibScalar
systemHardwareXfpId = _SystemHardwareXfpId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 20),
    _SystemHardwareXfpId_Type()
)
systemHardwareXfpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareXfpId.setStatus("current")


class _SystemHardwareUbootMinibootVersion_Type(SnmpAdminString):
    """Custom type systemHardwareUbootMinibootVersion based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemHardwareUbootMinibootVersion_Type.__name__ = "SnmpAdminString"
_SystemHardwareUbootMinibootVersion_Object = MibScalar
systemHardwareUbootMinibootVersion = _SystemHardwareUbootMinibootVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 3, 21),
    _SystemHardwareUbootMinibootVersion_Type()
)
systemHardwareUbootMinibootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareUbootMinibootVersion.setStatus("current")
_SystemFileSystem_ObjectIdentity = ObjectIdentity
systemFileSystem = _SystemFileSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 4)
)
_SystemFileSystemTable_Object = MibTable
systemFileSystemTable = _SystemFileSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    systemFileSystemTable.setStatus("current")
_SystemFileSystemEntry_Object = MibTableRow
systemFileSystemEntry = _SystemFileSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 4, 1, 1)
)
systemFileSystemEntry.setIndexNames(
    (0, "ALCATEL-ENT1-SYSTEM-MIB", "systemFileSystemIndex"),
)
if mibBuilder.loadTexts:
    systemFileSystemEntry.setStatus("current")
_SystemFileSystemIndex_Type = FileSystemIndex
_SystemFileSystemIndex_Object = MibTableColumn
systemFileSystemIndex = _SystemFileSystemIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 4, 1, 1, 1),
    _SystemFileSystemIndex_Type()
)
systemFileSystemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFileSystemIndex.setStatus("current")


class _SystemFileSystemName_Type(SnmpAdminString):
    """Custom type systemFileSystemName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemFileSystemName_Type.__name__ = "SnmpAdminString"
_SystemFileSystemName_Object = MibTableColumn
systemFileSystemName = _SystemFileSystemName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 4, 1, 1, 2),
    _SystemFileSystemName_Type()
)
systemFileSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFileSystemName.setStatus("current")


class _SystemFileSystemFreeSpace_Type(Unsigned32):
    """Custom type systemFileSystemFreeSpace based on Unsigned32"""
    defaultValue = 0


_SystemFileSystemFreeSpace_Type.__name__ = "Unsigned32"
_SystemFileSystemFreeSpace_Object = MibTableColumn
systemFileSystemFreeSpace = _SystemFileSystemFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 4, 1, 1, 3),
    _SystemFileSystemFreeSpace_Type()
)
systemFileSystemFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFileSystemFreeSpace.setStatus("current")


class _SystemFileSystemDirectoryName_Type(SnmpAdminString):
    """Custom type systemFileSystemDirectoryName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemFileSystemDirectoryName_Type.__name__ = "SnmpAdminString"
_SystemFileSystemDirectoryName_Object = MibScalar
systemFileSystemDirectoryName = _SystemFileSystemDirectoryName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 4, 2),
    _SystemFileSystemDirectoryName_Type()
)
systemFileSystemDirectoryName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemFileSystemDirectoryName.setStatus("current")


class _SystemFileSystemDirectoryDateTime_Type(SnmpAdminString):
    """Custom type systemFileSystemDirectoryDateTime based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemFileSystemDirectoryDateTime_Type.__name__ = "SnmpAdminString"
_SystemFileSystemDirectoryDateTime_Object = MibScalar
systemFileSystemDirectoryDateTime = _SystemFileSystemDirectoryDateTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 4, 3),
    _SystemFileSystemDirectoryDateTime_Type()
)
systemFileSystemDirectoryDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFileSystemDirectoryDateTime.setStatus("current")
_SystemFileSystemFileTable_Object = MibTable
systemFileSystemFileTable = _SystemFileSystemFileTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 4, 4)
)
if mibBuilder.loadTexts:
    systemFileSystemFileTable.setStatus("current")
_SystemFileSystemFileEntry_Object = MibTableRow
systemFileSystemFileEntry = _SystemFileSystemFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 4, 4, 1)
)
systemFileSystemFileEntry.setIndexNames(
    (0, "ALCATEL-ENT1-SYSTEM-MIB", "systemFileSystemFileIndex"),
)
if mibBuilder.loadTexts:
    systemFileSystemFileEntry.setStatus("current")
_SystemFileSystemFileIndex_Type = Unsigned32
_SystemFileSystemFileIndex_Object = MibTableColumn
systemFileSystemFileIndex = _SystemFileSystemFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 4, 4, 1, 1),
    _SystemFileSystemFileIndex_Type()
)
systemFileSystemFileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFileSystemFileIndex.setStatus("current")


class _SystemFileSystemFileName_Type(SnmpAdminString):
    """Custom type systemFileSystemFileName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemFileSystemFileName_Type.__name__ = "SnmpAdminString"
_SystemFileSystemFileName_Object = MibTableColumn
systemFileSystemFileName = _SystemFileSystemFileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 4, 4, 1, 2),
    _SystemFileSystemFileName_Type()
)
systemFileSystemFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFileSystemFileName.setStatus("current")


class _SystemFileSystemFileType_Type(SystemFileType):
    """Custom type systemFileSystemFileType based on SystemFileType"""
    defaultValue = 3


_SystemFileSystemFileType_Type.__name__ = "SystemFileType"
_SystemFileSystemFileType_Object = MibTableColumn
systemFileSystemFileType = _SystemFileSystemFileType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 4, 4, 1, 3),
    _SystemFileSystemFileType_Type()
)
systemFileSystemFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFileSystemFileType.setStatus("current")


class _SystemFileSystemFileSize_Type(Unsigned32):
    """Custom type systemFileSystemFileSize based on Unsigned32"""
    defaultValue = 0


_SystemFileSystemFileSize_Type.__name__ = "Unsigned32"
_SystemFileSystemFileSize_Object = MibTableColumn
systemFileSystemFileSize = _SystemFileSystemFileSize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 4, 4, 1, 4),
    _SystemFileSystemFileSize_Type()
)
systemFileSystemFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFileSystemFileSize.setStatus("current")


class _SystemFileSystemFileAttr_Type(Integer32):
    """Custom type systemFileSystemFileAttr based on Integer32"""
    defaultValue = 1

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
        *(("undefined", 1),
          ("readOnly", 2),
          ("readWrite", 3),
          ("writeOnly", 4))
    )


_SystemFileSystemFileAttr_Type.__name__ = "Integer32"
_SystemFileSystemFileAttr_Object = MibTableColumn
systemFileSystemFileAttr = _SystemFileSystemFileAttr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 4, 4, 1, 5),
    _SystemFileSystemFileAttr_Type()
)
systemFileSystemFileAttr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFileSystemFileAttr.setStatus("current")


class _SystemFileSystemFileDateTime_Type(SnmpAdminString):
    """Custom type systemFileSystemFileDateTime based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemFileSystemFileDateTime_Type.__name__ = "SnmpAdminString"
_SystemFileSystemFileDateTime_Object = MibTableColumn
systemFileSystemFileDateTime = _SystemFileSystemFileDateTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 4, 4, 1, 6),
    _SystemFileSystemFileDateTime_Type()
)
systemFileSystemFileDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFileSystemFileDateTime.setStatus("current")
_SystemServices_ObjectIdentity = ObjectIdentity
systemServices = _SystemServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5)
)


class _SystemServicesDate_Type(SnmpAdminString):
    """Custom type systemServicesDate based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemServicesDate_Type.__name__ = "SnmpAdminString"
_SystemServicesDate_Object = MibScalar
systemServicesDate = _SystemServicesDate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 1),
    _SystemServicesDate_Type()
)
systemServicesDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesDate.setStatus("current")


class _SystemServicesTime_Type(SnmpAdminString):
    """Custom type systemServicesTime based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemServicesTime_Type.__name__ = "SnmpAdminString"
_SystemServicesTime_Object = MibScalar
systemServicesTime = _SystemServicesTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 2),
    _SystemServicesTime_Type()
)
systemServicesTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesTime.setStatus("current")


class _SystemServicesTimezone_Type(SnmpAdminString):
    """Custom type systemServicesTimezone based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemServicesTimezone_Type.__name__ = "SnmpAdminString"
_SystemServicesTimezone_Object = MibScalar
systemServicesTimezone = _SystemServicesTimezone_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 3),
    _SystemServicesTimezone_Type()
)
systemServicesTimezone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesTimezone.setStatus("current")


class _SystemServicesTimezoneStartWeek_Type(Unsigned32):
    """Custom type systemServicesTimezoneStartWeek based on Unsigned32"""
    defaultValue = 0


_SystemServicesTimezoneStartWeek_Type.__name__ = "Unsigned32"
_SystemServicesTimezoneStartWeek_Object = MibScalar
systemServicesTimezoneStartWeek = _SystemServicesTimezoneStartWeek_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 4),
    _SystemServicesTimezoneStartWeek_Type()
)
systemServicesTimezoneStartWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesTimezoneStartWeek.setStatus("current")


class _SystemServicesTimezoneStartDay_Type(Unsigned32):
    """Custom type systemServicesTimezoneStartDay based on Unsigned32"""
    defaultValue = 0


_SystemServicesTimezoneStartDay_Type.__name__ = "Unsigned32"
_SystemServicesTimezoneStartDay_Object = MibScalar
systemServicesTimezoneStartDay = _SystemServicesTimezoneStartDay_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 5),
    _SystemServicesTimezoneStartDay_Type()
)
systemServicesTimezoneStartDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesTimezoneStartDay.setStatus("current")


class _SystemServicesTimezoneStartMonth_Type(Unsigned32):
    """Custom type systemServicesTimezoneStartMonth based on Unsigned32"""
    defaultValue = 0


_SystemServicesTimezoneStartMonth_Type.__name__ = "Unsigned32"
_SystemServicesTimezoneStartMonth_Object = MibScalar
systemServicesTimezoneStartMonth = _SystemServicesTimezoneStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 6),
    _SystemServicesTimezoneStartMonth_Type()
)
systemServicesTimezoneStartMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesTimezoneStartMonth.setStatus("current")


class _SystemServicesTimezoneStartTime_Type(Unsigned32):
    """Custom type systemServicesTimezoneStartTime based on Unsigned32"""
    defaultValue = 0


_SystemServicesTimezoneStartTime_Type.__name__ = "Unsigned32"
_SystemServicesTimezoneStartTime_Object = MibScalar
systemServicesTimezoneStartTime = _SystemServicesTimezoneStartTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 7),
    _SystemServicesTimezoneStartTime_Type()
)
systemServicesTimezoneStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesTimezoneStartTime.setStatus("current")


class _SystemServicesTimezoneOffset_Type(Unsigned32):
    """Custom type systemServicesTimezoneOffset based on Unsigned32"""
    defaultValue = 0


_SystemServicesTimezoneOffset_Type.__name__ = "Unsigned32"
_SystemServicesTimezoneOffset_Object = MibScalar
systemServicesTimezoneOffset = _SystemServicesTimezoneOffset_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 8),
    _SystemServicesTimezoneOffset_Type()
)
systemServicesTimezoneOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesTimezoneOffset.setStatus("current")


class _SystemServicesTimezoneEndWeek_Type(Unsigned32):
    """Custom type systemServicesTimezoneEndWeek based on Unsigned32"""
    defaultValue = 0


_SystemServicesTimezoneEndWeek_Type.__name__ = "Unsigned32"
_SystemServicesTimezoneEndWeek_Object = MibScalar
systemServicesTimezoneEndWeek = _SystemServicesTimezoneEndWeek_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 9),
    _SystemServicesTimezoneEndWeek_Type()
)
systemServicesTimezoneEndWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesTimezoneEndWeek.setStatus("current")


class _SystemServicesTimezoneEndDay_Type(Unsigned32):
    """Custom type systemServicesTimezoneEndDay based on Unsigned32"""
    defaultValue = 0


_SystemServicesTimezoneEndDay_Type.__name__ = "Unsigned32"
_SystemServicesTimezoneEndDay_Object = MibScalar
systemServicesTimezoneEndDay = _SystemServicesTimezoneEndDay_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 10),
    _SystemServicesTimezoneEndDay_Type()
)
systemServicesTimezoneEndDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesTimezoneEndDay.setStatus("current")


class _SystemServicesTimezoneEndMonth_Type(Unsigned32):
    """Custom type systemServicesTimezoneEndMonth based on Unsigned32"""
    defaultValue = 0


_SystemServicesTimezoneEndMonth_Type.__name__ = "Unsigned32"
_SystemServicesTimezoneEndMonth_Object = MibScalar
systemServicesTimezoneEndMonth = _SystemServicesTimezoneEndMonth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 11),
    _SystemServicesTimezoneEndMonth_Type()
)
systemServicesTimezoneEndMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesTimezoneEndMonth.setStatus("current")


class _SystemServicesTimezoneEndTime_Type(Unsigned32):
    """Custom type systemServicesTimezoneEndTime based on Unsigned32"""
    defaultValue = 0


_SystemServicesTimezoneEndTime_Type.__name__ = "Unsigned32"
_SystemServicesTimezoneEndTime_Object = MibScalar
systemServicesTimezoneEndTime = _SystemServicesTimezoneEndTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 12),
    _SystemServicesTimezoneEndTime_Type()
)
systemServicesTimezoneEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesTimezoneEndTime.setStatus("current")


class _SystemServicesEnableDST_Type(Enable):
    """Custom type systemServicesEnableDST based on Enable"""
    defaultValue = 2


_SystemServicesEnableDST_Type.__name__ = "Enable"
_SystemServicesEnableDST_Object = MibScalar
systemServicesEnableDST = _SystemServicesEnableDST_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 13),
    _SystemServicesEnableDST_Type()
)
systemServicesEnableDST.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesEnableDST.setStatus("current")


class _SystemServicesWorkingDirectory_Type(SnmpAdminString):
    """Custom type systemServicesWorkingDirectory based on SnmpAdminString"""
    defaultValue = OctetString("/flash")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemServicesWorkingDirectory_Type.__name__ = "SnmpAdminString"
_SystemServicesWorkingDirectory_Object = MibScalar
systemServicesWorkingDirectory = _SystemServicesWorkingDirectory_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 14),
    _SystemServicesWorkingDirectory_Type()
)
systemServicesWorkingDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesWorkingDirectory.setStatus("current")


class _SystemServicesArg1_Type(SnmpAdminString):
    """Custom type systemServicesArg1 based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemServicesArg1_Type.__name__ = "SnmpAdminString"
_SystemServicesArg1_Object = MibScalar
systemServicesArg1 = _SystemServicesArg1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 15),
    _SystemServicesArg1_Type()
)
systemServicesArg1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesArg1.setStatus("current")


class _SystemServicesArg2_Type(SnmpAdminString):
    """Custom type systemServicesArg2 based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemServicesArg2_Type.__name__ = "SnmpAdminString"
_SystemServicesArg2_Object = MibScalar
systemServicesArg2 = _SystemServicesArg2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 16),
    _SystemServicesArg2_Type()
)
systemServicesArg2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesArg2.setStatus("current")


class _SystemServicesArg3_Type(SnmpAdminString):
    """Custom type systemServicesArg3 based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemServicesArg3_Type.__name__ = "SnmpAdminString"
_SystemServicesArg3_Object = MibScalar
systemServicesArg3 = _SystemServicesArg3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 17),
    _SystemServicesArg3_Type()
)
systemServicesArg3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesArg3.setStatus("current")


class _SystemServicesArg4_Type(SnmpAdminString):
    """Custom type systemServicesArg4 based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemServicesArg4_Type.__name__ = "SnmpAdminString"
_SystemServicesArg4_Object = MibScalar
systemServicesArg4 = _SystemServicesArg4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 18),
    _SystemServicesArg4_Type()
)
systemServicesArg4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesArg4.setStatus("current")


class _SystemServicesArg5_Type(SnmpAdminString):
    """Custom type systemServicesArg5 based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemServicesArg5_Type.__name__ = "SnmpAdminString"
_SystemServicesArg5_Object = MibScalar
systemServicesArg5 = _SystemServicesArg5_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 19),
    _SystemServicesArg5_Type()
)
systemServicesArg5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesArg5.setStatus("current")


class _SystemServicesArg6_Type(SnmpAdminString):
    """Custom type systemServicesArg6 based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemServicesArg6_Type.__name__ = "SnmpAdminString"
_SystemServicesArg6_Object = MibScalar
systemServicesArg6 = _SystemServicesArg6_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 20),
    _SystemServicesArg6_Type()
)
systemServicesArg6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesArg6.setStatus("current")


class _SystemServicesArg7_Type(SnmpAdminString):
    """Custom type systemServicesArg7 based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemServicesArg7_Type.__name__ = "SnmpAdminString"
_SystemServicesArg7_Object = MibScalar
systemServicesArg7 = _SystemServicesArg7_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 21),
    _SystemServicesArg7_Type()
)
systemServicesArg7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesArg7.setStatus("current")


class _SystemServicesArg8_Type(SnmpAdminString):
    """Custom type systemServicesArg8 based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemServicesArg8_Type.__name__ = "SnmpAdminString"
_SystemServicesArg8_Object = MibScalar
systemServicesArg8 = _SystemServicesArg8_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 22),
    _SystemServicesArg8_Type()
)
systemServicesArg8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesArg8.setStatus("current")


class _SystemServicesArg9_Type(SnmpAdminString):
    """Custom type systemServicesArg9 based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemServicesArg9_Type.__name__ = "SnmpAdminString"
_SystemServicesArg9_Object = MibScalar
systemServicesArg9 = _SystemServicesArg9_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 23),
    _SystemServicesArg9_Type()
)
systemServicesArg9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesArg9.setStatus("current")


class _SystemServicesAction_Type(Integer32):
    """Custom type systemServicesAction based on Integer32"""
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
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49)
        )
    )
    namedValues = NamedValues(
        *(("noaction", 0),
          ("mkdir", 1),
          ("rmdir", 2),
          ("mv", 3),
          ("rm", 4),
          ("rmr", 5),
          ("cp", 6),
          ("cpr", 7),
          ("chmodpw", 8),
          ("chmodmw", 9),
          ("fsck", 10),
          ("ftp", 11),
          ("rz", 12),
          ("vi", 13),
          ("telnet", 14),
          ("install", 15),
          ("ed", 16),
          ("more", 17),
          ("newfs", 18),
          ("dshell", 19),
          ("view", 20),
          ("modbootparams", 21),
          ("filedir", 22),
          ("ssh", 23),
          ("sftp", 24),
          ("debugPmdNi", 25),
          ("bootrom", 26),
          ("defaultminiboot", 27),
          ("backupminiboot", 28),
          ("fpgacmm", 29),
          ("ubootcmm", 30),
          ("ubootni", 31),
          ("scp", 32),
          ("aclman", 33),
          ("ubootMinibootAllSlots", 34),
          ("miniboot", 35),
          ("upgradeLicence", 36),
          ("restoreLicence", 37),
          ("updateDSineXtroller", 38),
          ("ftp6", 39),
          ("telnet6", 40),
          ("ssh6", 41),
          ("sftp6", 42),
          ("mount", 43),
          ("unmount", 44),
          ("backup", 45),
          ("restore", 46),
          ("tftp", 47),
          ("fscollect", 48),
          ("fpgani", 49))
    )


_SystemServicesAction_Type.__name__ = "Integer32"
_SystemServicesAction_Object = MibScalar
systemServicesAction = _SystemServicesAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 24),
    _SystemServicesAction_Type()
)
systemServicesAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesAction.setStatus("current")
_SystemServicesResultCode_Type = Unsigned32
_SystemServicesResultCode_Object = MibScalar
systemServicesResultCode = _SystemServicesResultCode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 25),
    _SystemServicesResultCode_Type()
)
systemServicesResultCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemServicesResultCode.setStatus("current")


class _SystemServicesResultString_Type(SnmpAdminString):
    """Custom type systemServicesResultString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemServicesResultString_Type.__name__ = "SnmpAdminString"
_SystemServicesResultString_Object = MibScalar
systemServicesResultString = _SystemServicesResultString_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 26),
    _SystemServicesResultString_Type()
)
systemServicesResultString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemServicesResultString.setStatus("current")


class _SystemServicesKtraceEnable_Type(Enable):
    """Custom type systemServicesKtraceEnable based on Enable"""
    defaultValue = 1


_SystemServicesKtraceEnable_Type.__name__ = "Enable"
_SystemServicesKtraceEnable_Object = MibScalar
systemServicesKtraceEnable = _SystemServicesKtraceEnable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 27),
    _SystemServicesKtraceEnable_Type()
)
systemServicesKtraceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesKtraceEnable.setStatus("obsolete")


class _SystemServicesSystraceEnable_Type(Enable):
    """Custom type systemServicesSystraceEnable based on Enable"""
    defaultValue = 1


_SystemServicesSystraceEnable_Type.__name__ = "Enable"
_SystemServicesSystraceEnable_Object = MibScalar
systemServicesSystraceEnable = _SystemServicesSystraceEnable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 28),
    _SystemServicesSystraceEnable_Type()
)
systemServicesSystraceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesSystraceEnable.setStatus("obsolete")


class _SystemServicesTtyLines_Type(Unsigned32):
    """Custom type systemServicesTtyLines based on Unsigned32"""
    defaultValue = 24

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SystemServicesTtyLines_Type.__name__ = "Unsigned32"
_SystemServicesTtyLines_Object = MibScalar
systemServicesTtyLines = _SystemServicesTtyLines_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 29),
    _SystemServicesTtyLines_Type()
)
systemServicesTtyLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemServicesTtyLines.setStatus("current")


class _SystemServicesTtyColumns_Type(Unsigned32):
    """Custom type systemServicesTtyColumns based on Unsigned32"""
    defaultValue = 80

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SystemServicesTtyColumns_Type.__name__ = "Unsigned32"
_SystemServicesTtyColumns_Object = MibScalar
systemServicesTtyColumns = _SystemServicesTtyColumns_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 30),
    _SystemServicesTtyColumns_Type()
)
systemServicesTtyColumns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemServicesTtyColumns.setStatus("current")


class _SystemServicesMemMonitorEnable_Type(Enable):
    """Custom type systemServicesMemMonitorEnable based on Enable"""
    defaultValue = 1


_SystemServicesMemMonitorEnable_Type.__name__ = "Enable"
_SystemServicesMemMonitorEnable_Object = MibScalar
systemServicesMemMonitorEnable = _SystemServicesMemMonitorEnable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 31),
    _SystemServicesMemMonitorEnable_Type()
)
systemServicesMemMonitorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesMemMonitorEnable.setStatus("current")
_SystemServicesKtraceLevelTable_Object = MibTable
systemServicesKtraceLevelTable = _SystemServicesKtraceLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 32)
)
if mibBuilder.loadTexts:
    systemServicesKtraceLevelTable.setStatus("obsolete")
_SystemServicesKtraceLevelEntry_Object = MibTableRow
systemServicesKtraceLevelEntry = _SystemServicesKtraceLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 32, 1)
)
systemServicesKtraceLevelEntry.setIndexNames(
    (0, "ALCATEL-ENT1-SYSTEM-MIB", "systemServicesKtraceLevelAppId"),
)
if mibBuilder.loadTexts:
    systemServicesKtraceLevelEntry.setStatus("obsolete")
_SystemServicesKtraceLevelAppId_Type = AppIdIndex
_SystemServicesKtraceLevelAppId_Object = MibTableColumn
systemServicesKtraceLevelAppId = _SystemServicesKtraceLevelAppId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 32, 1, 1),
    _SystemServicesKtraceLevelAppId_Type()
)
systemServicesKtraceLevelAppId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemServicesKtraceLevelAppId.setStatus("obsolete")


class _SystemServicesKtraceLevel_Type(SeverityLevel):
    """Custom type systemServicesKtraceLevel based on SeverityLevel"""
    defaultValue = 8


_SystemServicesKtraceLevel_Type.__name__ = "SeverityLevel"
_SystemServicesKtraceLevel_Object = MibTableColumn
systemServicesKtraceLevel = _SystemServicesKtraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 32, 1, 2),
    _SystemServicesKtraceLevel_Type()
)
systemServicesKtraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesKtraceLevel.setStatus("obsolete")
_SystemServicesSystraceLevelTable_Object = MibTable
systemServicesSystraceLevelTable = _SystemServicesSystraceLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 33)
)
if mibBuilder.loadTexts:
    systemServicesSystraceLevelTable.setStatus("obsolete")
_SystemServicesSystraceLevelEntry_Object = MibTableRow
systemServicesSystraceLevelEntry = _SystemServicesSystraceLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 33, 1)
)
systemServicesSystraceLevelEntry.setIndexNames(
    (0, "ALCATEL-ENT1-SYSTEM-MIB", "systemServicesSystraceLevelAppId"),
)
if mibBuilder.loadTexts:
    systemServicesSystraceLevelEntry.setStatus("obsolete")
_SystemServicesSystraceLevelAppId_Type = AppIdIndex
_SystemServicesSystraceLevelAppId_Object = MibTableColumn
systemServicesSystraceLevelAppId = _SystemServicesSystraceLevelAppId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 33, 1, 1),
    _SystemServicesSystraceLevelAppId_Type()
)
systemServicesSystraceLevelAppId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemServicesSystraceLevelAppId.setStatus("obsolete")


class _SystemServicesSystraceLevel_Type(SeverityLevel):
    """Custom type systemServicesSystraceLevel based on SeverityLevel"""
    defaultValue = 8


_SystemServicesSystraceLevel_Type.__name__ = "SeverityLevel"
_SystemServicesSystraceLevel_Object = MibTableColumn
systemServicesSystraceLevel = _SystemServicesSystraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 33, 1, 2),
    _SystemServicesSystraceLevel_Type()
)
systemServicesSystraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesSystraceLevel.setStatus("obsolete")
_SystemUpdateStatusTable_Object = MibTable
systemUpdateStatusTable = _SystemUpdateStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 34)
)
if mibBuilder.loadTexts:
    systemUpdateStatusTable.setStatus("current")
_SystemUpdateStatusEntry_Object = MibTableRow
systemUpdateStatusEntry = _SystemUpdateStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 34, 1)
)
systemUpdateStatusEntry.setIndexNames(
    (0, "ALCATEL-ENT1-SYSTEM-MIB", "systemUpdateIndex"),
)
if mibBuilder.loadTexts:
    systemUpdateStatusEntry.setStatus("current")


class _SystemUpdateIndex_Type(Integer32):
    """Custom type systemUpdateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 72),
    )


_SystemUpdateIndex_Type.__name__ = "Integer32"
_SystemUpdateIndex_Object = MibTableColumn
systemUpdateIndex = _SystemUpdateIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 34, 1, 1),
    _SystemUpdateIndex_Type()
)
systemUpdateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    systemUpdateIndex.setStatus("current")


class _SystemUpdateStatus_Type(Integer32):
    """Custom type systemUpdateStatus based on Integer32"""
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
        *(("inProgress", 1),
          ("doneOk", 2),
          ("doneNok", 3),
          ("noOp", 4))
    )


_SystemUpdateStatus_Type.__name__ = "Integer32"
_SystemUpdateStatus_Object = MibTableColumn
systemUpdateStatus = _SystemUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 34, 1, 2),
    _SystemUpdateStatus_Type()
)
systemUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUpdateStatus.setStatus("current")


class _SystemUpdateErrorCode_Type(Integer32):
    """Custom type systemUpdateErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28)
        )
    )
    namedValues = NamedValues(
        *(("msgSendIpcErr", 1),
          ("fXferOPenErr", 2),
          ("fXferFtpErr", 3),
          ("fXferReadErr", 4),
          ("fXferWriteErr", 5),
          ("fXferReplyErr", 6),
          ("fXferQuitErr", 7),
          ("fXferFcloseErr", 8),
          ("fileNameErr", 9),
          ("rmFileErr", 10),
          ("noInstallComp", 11),
          ("notSysResource", 12),
          ("notSupported", 13),
          ("invalidValue", 14),
          ("waitMsgMaxTry", 15),
          ("installDrvErr", 16),
          ("fileNotFound", 17),
          ("notPrimary", 18),
          ("commandBlocked", 19),
          ("noError", 20),
          ("invalidNi", 21),
          ("niNotPresent", 22),
          ("dupSerialNum", 23),
          ("upToDate", 24),
          ("invalidModType", 25),
          ("maxFaiCount", 26),
          ("invalidKey", 27),
          ("niLocked", 28))
    )


_SystemUpdateErrorCode_Type.__name__ = "Integer32"
_SystemUpdateErrorCode_Object = MibTableColumn
systemUpdateErrorCode = _SystemUpdateErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 34, 1, 3),
    _SystemUpdateErrorCode_Type()
)
systemUpdateErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUpdateErrorCode.setStatus("current")
_SystemServicesActionPercentComplete_Type = CommandPercentComplete
_SystemServicesActionPercentComplete_Object = MibScalar
systemServicesActionPercentComplete = _SystemServicesActionPercentComplete_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 35),
    _SystemServicesActionPercentComplete_Type()
)
systemServicesActionPercentComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemServicesActionPercentComplete.setStatus("current")


class _SystemServicesCurrentArchivePathName_Type(SnmpAdminString):
    """Custom type systemServicesCurrentArchivePathName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemServicesCurrentArchivePathName_Type.__name__ = "SnmpAdminString"
_SystemServicesCurrentArchivePathName_Object = MibScalar
systemServicesCurrentArchivePathName = _SystemServicesCurrentArchivePathName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 36),
    _SystemServicesCurrentArchivePathName_Type()
)
systemServicesCurrentArchivePathName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesCurrentArchivePathName.setStatus("current")
_SystemServicesArchiveTable_Object = MibTable
systemServicesArchiveTable = _SystemServicesArchiveTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 37)
)
if mibBuilder.loadTexts:
    systemServicesArchiveTable.setStatus("current")
_SystemServicesArchiveEntry_Object = MibTableRow
systemServicesArchiveEntry = _SystemServicesArchiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 37, 1)
)
systemServicesArchiveEntry.setIndexNames(
    (0, "ALCATEL-ENT1-SYSTEM-MIB", "systemServicesArchiveIndex"),
)
if mibBuilder.loadTexts:
    systemServicesArchiveEntry.setStatus("current")
_SystemServicesArchiveIndex_Type = Unsigned32
_SystemServicesArchiveIndex_Object = MibTableColumn
systemServicesArchiveIndex = _SystemServicesArchiveIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 37, 1, 1),
    _SystemServicesArchiveIndex_Type()
)
systemServicesArchiveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemServicesArchiveIndex.setStatus("current")


class _SystemServicesArchiveName_Type(SnmpAdminString):
    """Custom type systemServicesArchiveName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemServicesArchiveName_Type.__name__ = "SnmpAdminString"
_SystemServicesArchiveName_Object = MibTableColumn
systemServicesArchiveName = _SystemServicesArchiveName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 37, 1, 2),
    _SystemServicesArchiveName_Type()
)
systemServicesArchiveName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemServicesArchiveName.setStatus("current")


class _SystemServicesArchiveType_Type(SystemFileType):
    """Custom type systemServicesArchiveType based on SystemFileType"""
    defaultValue = 3


_SystemServicesArchiveType_Type.__name__ = "SystemFileType"
_SystemServicesArchiveType_Object = MibTableColumn
systemServicesArchiveType = _SystemServicesArchiveType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 37, 1, 3),
    _SystemServicesArchiveType_Type()
)
systemServicesArchiveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemServicesArchiveType.setStatus("current")


class _SystemServicesArchiveSize_Type(Unsigned32):
    """Custom type systemServicesArchiveSize based on Unsigned32"""
    defaultValue = 0


_SystemServicesArchiveSize_Type.__name__ = "Unsigned32"
_SystemServicesArchiveSize_Object = MibTableColumn
systemServicesArchiveSize = _SystemServicesArchiveSize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 37, 1, 4),
    _SystemServicesArchiveSize_Type()
)
systemServicesArchiveSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemServicesArchiveSize.setStatus("current")


class _SystemServicesArchiveAttr_Type(Integer32):
    """Custom type systemServicesArchiveAttr based on Integer32"""
    defaultValue = 1

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
        *(("undefined", 1),
          ("readOnly", 2),
          ("readWrite", 3),
          ("writeOnly", 4))
    )


_SystemServicesArchiveAttr_Type.__name__ = "Integer32"
_SystemServicesArchiveAttr_Object = MibTableColumn
systemServicesArchiveAttr = _SystemServicesArchiveAttr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 37, 1, 5),
    _SystemServicesArchiveAttr_Type()
)
systemServicesArchiveAttr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemServicesArchiveAttr.setStatus("current")


class _SystemServicesUsbEnable_Type(Integer32):
    """Custom type systemServicesUsbEnable based on Integer32"""
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
        *(("enableasync", 1),
          ("disable", 2),
          ("enablesync", 3))
    )


_SystemServicesUsbEnable_Type.__name__ = "Integer32"
_SystemServicesUsbEnable_Object = MibScalar
systemServicesUsbEnable = _SystemServicesUsbEnable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 38),
    _SystemServicesUsbEnable_Type()
)
systemServicesUsbEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesUsbEnable.setStatus("current")
_SystemServicesUsbAutoCopyEnable_Type = Enable
_SystemServicesUsbAutoCopyEnable_Object = MibScalar
systemServicesUsbAutoCopyEnable = _SystemServicesUsbAutoCopyEnable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 39),
    _SystemServicesUsbAutoCopyEnable_Type()
)
systemServicesUsbAutoCopyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesUsbAutoCopyEnable.setStatus("current")
_SystemServicesUsbMounted_Type = Enable
_SystemServicesUsbMounted_Object = MibScalar
systemServicesUsbMounted = _SystemServicesUsbMounted_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 5, 40),
    _SystemServicesUsbMounted_Type()
)
systemServicesUsbMounted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemServicesUsbMounted.setStatus("current")
_SystemSwitchLogging_ObjectIdentity = ObjectIdentity
systemSwitchLogging = _SystemSwitchLogging_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6)
)


class _SystemSwitchLoggingIndex_Type(SwitchLoggingIndex):
    """Custom type systemSwitchLoggingIndex based on SwitchLoggingIndex"""
    defaultValue = 2


_SystemSwitchLoggingIndex_Type.__name__ = "SwitchLoggingIndex"
_SystemSwitchLoggingIndex_Object = MibScalar
systemSwitchLoggingIndex = _SystemSwitchLoggingIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 1),
    _SystemSwitchLoggingIndex_Type()
)
systemSwitchLoggingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSwitchLoggingIndex.setStatus("current")


class _SystemSwitchLoggingEnable_Type(Enable):
    """Custom type systemSwitchLoggingEnable based on Enable"""
    defaultValue = 1


_SystemSwitchLoggingEnable_Type.__name__ = "Enable"
_SystemSwitchLoggingEnable_Object = MibScalar
systemSwitchLoggingEnable = _SystemSwitchLoggingEnable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 2),
    _SystemSwitchLoggingEnable_Type()
)
systemSwitchLoggingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSwitchLoggingEnable.setStatus("current")


class _SystemSwitchLoggingFlash_Type(Enable):
    """Custom type systemSwitchLoggingFlash based on Enable"""
    defaultValue = 1


_SystemSwitchLoggingFlash_Type.__name__ = "Enable"
_SystemSwitchLoggingFlash_Object = MibScalar
systemSwitchLoggingFlash = _SystemSwitchLoggingFlash_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 3),
    _SystemSwitchLoggingFlash_Type()
)
systemSwitchLoggingFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSwitchLoggingFlash.setStatus("current")


class _SystemSwitchLoggingSocket_Type(Enable):
    """Custom type systemSwitchLoggingSocket based on Enable"""
    defaultValue = 2


_SystemSwitchLoggingSocket_Type.__name__ = "Enable"
_SystemSwitchLoggingSocket_Object = MibScalar
systemSwitchLoggingSocket = _SystemSwitchLoggingSocket_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 4),
    _SystemSwitchLoggingSocket_Type()
)
systemSwitchLoggingSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSwitchLoggingSocket.setStatus("current")
_SystemSwitchLoggingSocketIpAddr_Type = IpAddress
_SystemSwitchLoggingSocketIpAddr_Object = MibScalar
systemSwitchLoggingSocketIpAddr = _SystemSwitchLoggingSocketIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 5),
    _SystemSwitchLoggingSocketIpAddr_Type()
)
systemSwitchLoggingSocketIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSwitchLoggingSocketIpAddr.setStatus("deprecated")


class _SystemSwitchLoggingConsole_Type(Enable):
    """Custom type systemSwitchLoggingConsole based on Enable"""
    defaultValue = 2


_SystemSwitchLoggingConsole_Type.__name__ = "Enable"
_SystemSwitchLoggingConsole_Object = MibScalar
systemSwitchLoggingConsole = _SystemSwitchLoggingConsole_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 6),
    _SystemSwitchLoggingConsole_Type()
)
systemSwitchLoggingConsole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSwitchLoggingConsole.setStatus("current")
_SystemSwitchLoggingApplicationTable_Object = MibTable
systemSwitchLoggingApplicationTable = _SystemSwitchLoggingApplicationTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 7)
)
if mibBuilder.loadTexts:
    systemSwitchLoggingApplicationTable.setStatus("current")
_SystemSwitchLoggingLevelEntry_Object = MibTableRow
systemSwitchLoggingLevelEntry = _SystemSwitchLoggingLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 7, 1)
)
systemSwitchLoggingLevelEntry.setIndexNames(
    (0, "ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingApplicationAppId"),
    (0, "ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingApplicationSubAppId"),
    (0, "ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingApplicationSubAppVrfLevelIndex"),
)
if mibBuilder.loadTexts:
    systemSwitchLoggingLevelEntry.setStatus("current")
_SystemSwitchLoggingApplicationAppId_Type = AppIdIndex
_SystemSwitchLoggingApplicationAppId_Object = MibTableColumn
systemSwitchLoggingApplicationAppId = _SystemSwitchLoggingApplicationAppId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 7, 1, 1),
    _SystemSwitchLoggingApplicationAppId_Type()
)
systemSwitchLoggingApplicationAppId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSwitchLoggingApplicationAppId.setStatus("current")
_SystemSwitchLoggingApplicationSubAppId_Type = AppIdIndex
_SystemSwitchLoggingApplicationSubAppId_Object = MibTableColumn
systemSwitchLoggingApplicationSubAppId = _SystemSwitchLoggingApplicationSubAppId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 7, 1, 2),
    _SystemSwitchLoggingApplicationSubAppId_Type()
)
systemSwitchLoggingApplicationSubAppId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSwitchLoggingApplicationSubAppId.setStatus("current")


class _SystemSwitchLoggingApplicationSubAppVrfLevelIndex_Type(Integer32):
    """Custom type systemSwitchLoggingApplicationSubAppVrfLevelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_SystemSwitchLoggingApplicationSubAppVrfLevelIndex_Type.__name__ = "Integer32"
_SystemSwitchLoggingApplicationSubAppVrfLevelIndex_Object = MibTableColumn
systemSwitchLoggingApplicationSubAppVrfLevelIndex = _SystemSwitchLoggingApplicationSubAppVrfLevelIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 7, 1, 3),
    _SystemSwitchLoggingApplicationSubAppVrfLevelIndex_Type()
)
systemSwitchLoggingApplicationSubAppVrfLevelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSwitchLoggingApplicationSubAppVrfLevelIndex.setStatus("current")


class _SystemSwitchLoggingApplicationAppName_Type(SnmpAdminString):
    """Custom type systemSwitchLoggingApplicationAppName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemSwitchLoggingApplicationAppName_Type.__name__ = "SnmpAdminString"
_SystemSwitchLoggingApplicationAppName_Object = MibTableColumn
systemSwitchLoggingApplicationAppName = _SystemSwitchLoggingApplicationAppName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 7, 1, 4),
    _SystemSwitchLoggingApplicationAppName_Type()
)
systemSwitchLoggingApplicationAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSwitchLoggingApplicationAppName.setStatus("current")


class _SystemSwitchLoggingApplicationSubAppName_Type(SnmpAdminString):
    """Custom type systemSwitchLoggingApplicationSubAppName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemSwitchLoggingApplicationSubAppName_Type.__name__ = "SnmpAdminString"
_SystemSwitchLoggingApplicationSubAppName_Object = MibTableColumn
systemSwitchLoggingApplicationSubAppName = _SystemSwitchLoggingApplicationSubAppName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 7, 1, 5),
    _SystemSwitchLoggingApplicationSubAppName_Type()
)
systemSwitchLoggingApplicationSubAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSwitchLoggingApplicationSubAppName.setStatus("current")


class _SystemSwitchLoggingApplicationSubAppLevel_Type(SeverityLevel):
    """Custom type systemSwitchLoggingApplicationSubAppLevel based on SeverityLevel"""
    defaultValue = 0


_SystemSwitchLoggingApplicationSubAppLevel_Type.__name__ = "SeverityLevel"
_SystemSwitchLoggingApplicationSubAppLevel_Object = MibTableColumn
systemSwitchLoggingApplicationSubAppLevel = _SystemSwitchLoggingApplicationSubAppLevel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 7, 1, 6),
    _SystemSwitchLoggingApplicationSubAppLevel_Type()
)
systemSwitchLoggingApplicationSubAppLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSwitchLoggingApplicationSubAppLevel.setStatus("current")


class _SystemSwitchLoggingApplicationSubAppVrfLevelString_Type(SnmpAdminString):
    """Custom type systemSwitchLoggingApplicationSubAppVrfLevelString based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemSwitchLoggingApplicationSubAppVrfLevelString_Type.__name__ = "SnmpAdminString"
_SystemSwitchLoggingApplicationSubAppVrfLevelString_Object = MibTableColumn
systemSwitchLoggingApplicationSubAppVrfLevelString = _SystemSwitchLoggingApplicationSubAppVrfLevelString_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 7, 1, 7),
    _SystemSwitchLoggingApplicationSubAppVrfLevelString_Type()
)
systemSwitchLoggingApplicationSubAppVrfLevelString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSwitchLoggingApplicationSubAppVrfLevelString.setStatus("current")
_SystemSwitchLoggingClear_Type = Unsigned32
_SystemSwitchLoggingClear_Object = MibScalar
systemSwitchLoggingClear = _SystemSwitchLoggingClear_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 8),
    _SystemSwitchLoggingClear_Type()
)
systemSwitchLoggingClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSwitchLoggingClear.setStatus("current")
_SystemSwitchLoggingFileSize_Type = Unsigned32
_SystemSwitchLoggingFileSize_Object = MibScalar
systemSwitchLoggingFileSize = _SystemSwitchLoggingFileSize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 9),
    _SystemSwitchLoggingFileSize_Type()
)
systemSwitchLoggingFileSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSwitchLoggingFileSize.setStatus("current")
_SystemSwitchLoggingHostTable_Object = MibTable
systemSwitchLoggingHostTable = _SystemSwitchLoggingHostTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 10)
)
if mibBuilder.loadTexts:
    systemSwitchLoggingHostTable.setStatus("current")
_SystemSwitchLoggingHostEntry_Object = MibTableRow
systemSwitchLoggingHostEntry = _SystemSwitchLoggingHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 10, 1)
)
systemSwitchLoggingHostEntry.setIndexNames(
    (0, "ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingHostIpAddr"),
)
if mibBuilder.loadTexts:
    systemSwitchLoggingHostEntry.setStatus("current")
_SystemSwitchLoggingHostIpAddr_Type = IpAddress
_SystemSwitchLoggingHostIpAddr_Object = MibTableColumn
systemSwitchLoggingHostIpAddr = _SystemSwitchLoggingHostIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 10, 1, 1),
    _SystemSwitchLoggingHostIpAddr_Type()
)
systemSwitchLoggingHostIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSwitchLoggingHostIpAddr.setStatus("current")


class _SystemSwitchLoggingHostPort_Type(Integer32):
    """Custom type systemSwitchLoggingHostPort based on Integer32"""
    defaultValue = 514

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SystemSwitchLoggingHostPort_Type.__name__ = "Integer32"
_SystemSwitchLoggingHostPort_Object = MibTableColumn
systemSwitchLoggingHostPort = _SystemSwitchLoggingHostPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 10, 1, 2),
    _SystemSwitchLoggingHostPort_Type()
)
systemSwitchLoggingHostPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    systemSwitchLoggingHostPort.setStatus("current")
_SystemSwitchLoggingHostStatus_Type = RowStatus
_SystemSwitchLoggingHostStatus_Object = MibTableColumn
systemSwitchLoggingHostStatus = _SystemSwitchLoggingHostStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 10, 1, 3),
    _SystemSwitchLoggingHostStatus_Type()
)
systemSwitchLoggingHostStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    systemSwitchLoggingHostStatus.setStatus("current")


class _SystemSwitchLoggingHostUserCommandHost_Type(Enable):
    """Custom type systemSwitchLoggingHostUserCommandHost based on Enable"""
    defaultValue = 2


_SystemSwitchLoggingHostUserCommandHost_Type.__name__ = "Enable"
_SystemSwitchLoggingHostUserCommandHost_Object = MibTableColumn
systemSwitchLoggingHostUserCommandHost = _SystemSwitchLoggingHostUserCommandHost_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 10, 1, 4),
    _SystemSwitchLoggingHostUserCommandHost_Type()
)
systemSwitchLoggingHostUserCommandHost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    systemSwitchLoggingHostUserCommandHost.setStatus("current")


class _SystemSwitchLoggingHostVrfName_Type(SnmpAdminString):
    """Custom type systemSwitchLoggingHostVrfName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SystemSwitchLoggingHostVrfName_Type.__name__ = "SnmpAdminString"
_SystemSwitchLoggingHostVrfName_Object = MibTableColumn
systemSwitchLoggingHostVrfName = _SystemSwitchLoggingHostVrfName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 10, 1, 5),
    _SystemSwitchLoggingHostVrfName_Type()
)
systemSwitchLoggingHostVrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    systemSwitchLoggingHostVrfName.setStatus("current")
_SystemSwitchLoggingHostv6Table_Object = MibTable
systemSwitchLoggingHostv6Table = _SystemSwitchLoggingHostv6Table_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 11)
)
if mibBuilder.loadTexts:
    systemSwitchLoggingHostv6Table.setStatus("current")
_SystemSwitchLoggingHostv6Entry_Object = MibTableRow
systemSwitchLoggingHostv6Entry = _SystemSwitchLoggingHostv6Entry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 11, 1)
)
systemSwitchLoggingHostv6Entry.setIndexNames(
    (0, "ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingHostv6IpAddr"),
)
if mibBuilder.loadTexts:
    systemSwitchLoggingHostv6Entry.setStatus("current")
_SystemSwitchLoggingHostv6IpAddr_Type = Ipv6Address
_SystemSwitchLoggingHostv6IpAddr_Object = MibTableColumn
systemSwitchLoggingHostv6IpAddr = _SystemSwitchLoggingHostv6IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 11, 1, 1),
    _SystemSwitchLoggingHostv6IpAddr_Type()
)
systemSwitchLoggingHostv6IpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSwitchLoggingHostv6IpAddr.setStatus("current")


class _SystemSwitchLoggingHostv6Port_Type(Integer32):
    """Custom type systemSwitchLoggingHostv6Port based on Integer32"""
    defaultValue = 514

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SystemSwitchLoggingHostv6Port_Type.__name__ = "Integer32"
_SystemSwitchLoggingHostv6Port_Object = MibTableColumn
systemSwitchLoggingHostv6Port = _SystemSwitchLoggingHostv6Port_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 11, 1, 2),
    _SystemSwitchLoggingHostv6Port_Type()
)
systemSwitchLoggingHostv6Port.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    systemSwitchLoggingHostv6Port.setStatus("current")
_SystemSwitchLoggingHostv6Status_Type = RowStatus
_SystemSwitchLoggingHostv6Status_Object = MibTableColumn
systemSwitchLoggingHostv6Status = _SystemSwitchLoggingHostv6Status_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 11, 1, 3),
    _SystemSwitchLoggingHostv6Status_Type()
)
systemSwitchLoggingHostv6Status.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    systemSwitchLoggingHostv6Status.setStatus("current")


class _SystemSwitchLoggingHostv6UserCommandHost_Type(Enable):
    """Custom type systemSwitchLoggingHostv6UserCommandHost based on Enable"""
    defaultValue = 2


_SystemSwitchLoggingHostv6UserCommandHost_Type.__name__ = "Enable"
_SystemSwitchLoggingHostv6UserCommandHost_Object = MibTableColumn
systemSwitchLoggingHostv6UserCommandHost = _SystemSwitchLoggingHostv6UserCommandHost_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 11, 1, 4),
    _SystemSwitchLoggingHostv6UserCommandHost_Type()
)
systemSwitchLoggingHostv6UserCommandHost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    systemSwitchLoggingHostv6UserCommandHost.setStatus("current")


class _SystemSwitchLoggingHostv6VrfName_Type(SnmpAdminString):
    """Custom type systemSwitchLoggingHostv6VrfName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SystemSwitchLoggingHostv6VrfName_Type.__name__ = "SnmpAdminString"
_SystemSwitchLoggingHostv6VrfName_Object = MibTableColumn
systemSwitchLoggingHostv6VrfName = _SystemSwitchLoggingHostv6VrfName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 11, 1, 5),
    _SystemSwitchLoggingHostv6VrfName_Type()
)
systemSwitchLoggingHostv6VrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    systemSwitchLoggingHostv6VrfName.setStatus("current")


class _SystemSwitchLoggingHostCount_Type(Integer32):
    """Custom type systemSwitchLoggingHostCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_SystemSwitchLoggingHostCount_Type.__name__ = "Integer32"
_SystemSwitchLoggingHostCount_Object = MibScalar
systemSwitchLoggingHostCount = _SystemSwitchLoggingHostCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 12),
    _SystemSwitchLoggingHostCount_Type()
)
systemSwitchLoggingHostCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSwitchLoggingHostCount.setStatus("current")


class _SystemSwitchLoggingConsoleLevel_Type(SeverityLevel):
    """Custom type systemSwitchLoggingConsoleLevel based on SeverityLevel"""
    defaultValue = 4


_SystemSwitchLoggingConsoleLevel_Type.__name__ = "SeverityLevel"
_SystemSwitchLoggingConsoleLevel_Object = MibScalar
systemSwitchLoggingConsoleLevel = _SystemSwitchLoggingConsoleLevel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 13),
    _SystemSwitchLoggingConsoleLevel_Type()
)
systemSwitchLoggingConsoleLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    systemSwitchLoggingConsoleLevel.setStatus("current")


class _SystemSwitchLoggingUserCommandStatus_Type(Enable):
    """Custom type systemSwitchLoggingUserCommandStatus based on Enable"""
    defaultValue = 2


_SystemSwitchLoggingUserCommandStatus_Type.__name__ = "Enable"
_SystemSwitchLoggingUserCommandStatus_Object = MibScalar
systemSwitchLoggingUserCommandStatus = _SystemSwitchLoggingUserCommandStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 14),
    _SystemSwitchLoggingUserCommandStatus_Type()
)
systemSwitchLoggingUserCommandStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    systemSwitchLoggingUserCommandStatus.setStatus("current")


class _SystemSwitchLoggingSysLogFacilityId_Type(SysLogFacilityId):
    """Custom type systemSwitchLoggingSysLogFacilityId based on SysLogFacilityId"""
    defaultValue = 0


_SystemSwitchLoggingSysLogFacilityId_Type.__name__ = "SysLogFacilityId"
_SystemSwitchLoggingSysLogFacilityId_Object = MibScalar
systemSwitchLoggingSysLogFacilityId = _SystemSwitchLoggingSysLogFacilityId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 15),
    _SystemSwitchLoggingSysLogFacilityId_Type()
)
systemSwitchLoggingSysLogFacilityId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSwitchLoggingSysLogFacilityId.setStatus("current")
_SystemSwitchLoggingLevel_Type = SeverityLevel
_SystemSwitchLoggingLevel_Object = MibScalar
systemSwitchLoggingLevel = _SystemSwitchLoggingLevel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 16),
    _SystemSwitchLoggingLevel_Type()
)
systemSwitchLoggingLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSwitchLoggingLevel.setStatus("current")


class _SystemSwitchLoggingAppName_Type(SnmpAdminString):
    """Custom type systemSwitchLoggingAppName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemSwitchLoggingAppName_Type.__name__ = "SnmpAdminString"
_SystemSwitchLoggingAppName_Object = MibScalar
systemSwitchLoggingAppName = _SystemSwitchLoggingAppName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 17),
    _SystemSwitchLoggingAppName_Type()
)
systemSwitchLoggingAppName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSwitchLoggingAppName.setStatus("current")


class _SystemSwitchLoggingDuplicateDetect_Type(Enable):
    """Custom type systemSwitchLoggingDuplicateDetect based on Enable"""
    defaultValue = 1


_SystemSwitchLoggingDuplicateDetect_Type.__name__ = "Enable"
_SystemSwitchLoggingDuplicateDetect_Object = MibScalar
systemSwitchLoggingDuplicateDetect = _SystemSwitchLoggingDuplicateDetect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 18),
    _SystemSwitchLoggingDuplicateDetect_Type()
)
systemSwitchLoggingDuplicateDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSwitchLoggingDuplicateDetect.setStatus("current")


class _SystemSwitchLoggingPreamble_Type(Enable):
    """Custom type systemSwitchLoggingPreamble based on Enable"""
    defaultValue = 1


_SystemSwitchLoggingPreamble_Type.__name__ = "Enable"
_SystemSwitchLoggingPreamble_Object = MibScalar
systemSwitchLoggingPreamble = _SystemSwitchLoggingPreamble_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 19),
    _SystemSwitchLoggingPreamble_Type()
)
systemSwitchLoggingPreamble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSwitchLoggingPreamble.setStatus("current")


class _SystemSwitchLoggingDebug_Type(Enable):
    """Custom type systemSwitchLoggingDebug based on Enable"""
    defaultValue = 1


_SystemSwitchLoggingDebug_Type.__name__ = "Enable"
_SystemSwitchLoggingDebug_Object = MibScalar
systemSwitchLoggingDebug = _SystemSwitchLoggingDebug_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 20),
    _SystemSwitchLoggingDebug_Type()
)
systemSwitchLoggingDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSwitchLoggingDebug.setStatus("current")


class _SystemSwitchLoggingVrf_Type(VrfId):
    """Custom type systemSwitchLoggingVrf based on VrfId"""
    defaultValue = 1


_SystemSwitchLoggingVrf_Type.__name__ = "VrfId"
_SystemSwitchLoggingVrf_Object = MibScalar
systemSwitchLoggingVrf = _SystemSwitchLoggingVrf_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 21),
    _SystemSwitchLoggingVrf_Type()
)
systemSwitchLoggingVrf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSwitchLoggingVrf.setStatus("current")


class _SystemSwitchLoggingHashAgeLimit_Type(AgeLimit):
    """Custom type systemSwitchLoggingHashAgeLimit based on AgeLimit"""
    defaultValue = 1


_SystemSwitchLoggingHashAgeLimit_Type.__name__ = "AgeLimit"
_SystemSwitchLoggingHashAgeLimit_Object = MibScalar
systemSwitchLoggingHashAgeLimit = _SystemSwitchLoggingHashAgeLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 22),
    _SystemSwitchLoggingHashAgeLimit_Type()
)
systemSwitchLoggingHashAgeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSwitchLoggingHashAgeLimit.setStatus("current")


class _SystemSwitchLoggingTty_Type(Enable):
    """Custom type systemSwitchLoggingTty based on Enable"""
    defaultValue = 2


_SystemSwitchLoggingTty_Type.__name__ = "Enable"
_SystemSwitchLoggingTty_Object = MibScalar
systemSwitchLoggingTty = _SystemSwitchLoggingTty_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 23),
    _SystemSwitchLoggingTty_Type()
)
systemSwitchLoggingTty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSwitchLoggingTty.setStatus("current")
_SystemSwitchLoggingSubAppNbr_Type = AppIdIndex
_SystemSwitchLoggingSubAppNbr_Object = MibScalar
systemSwitchLoggingSubAppNbr = _SystemSwitchLoggingSubAppNbr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 24),
    _SystemSwitchLoggingSubAppNbr_Type()
)
systemSwitchLoggingSubAppNbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSwitchLoggingSubAppNbr.setStatus("current")


class _SystemSwitchLoggingLibraryName_Type(SnmpAdminString):
    """Custom type systemSwitchLoggingLibraryName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemSwitchLoggingLibraryName_Type.__name__ = "SnmpAdminString"
_SystemSwitchLoggingLibraryName_Object = MibScalar
systemSwitchLoggingLibraryName = _SystemSwitchLoggingLibraryName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 25),
    _SystemSwitchLoggingLibraryName_Type()
)
systemSwitchLoggingLibraryName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSwitchLoggingLibraryName.setStatus("current")


class _SystemSwitchLoggingLoopback0_Type(Enable):
    """Custom type systemSwitchLoggingLoopback0 based on Enable"""
    defaultValue = 2


_SystemSwitchLoggingLoopback0_Type.__name__ = "Enable"
_SystemSwitchLoggingLoopback0_Object = MibScalar
systemSwitchLoggingLoopback0 = _SystemSwitchLoggingLoopback0_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 26),
    _SystemSwitchLoggingLoopback0_Type()
)
systemSwitchLoggingLoopback0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSwitchLoggingLoopback0.setStatus("current")
_SystemSwitchLoggingDgHostTable_Object = MibTable
systemSwitchLoggingDgHostTable = _SystemSwitchLoggingDgHostTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 27)
)
if mibBuilder.loadTexts:
    systemSwitchLoggingDgHostTable.setStatus("current")
_SystemSwitchLoggingDgHostEntry_Object = MibTableRow
systemSwitchLoggingDgHostEntry = _SystemSwitchLoggingDgHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 27, 1)
)
systemSwitchLoggingDgHostEntry.setIndexNames(
    (0, "ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingDgHostIndex"),
)
if mibBuilder.loadTexts:
    systemSwitchLoggingDgHostEntry.setStatus("current")


class _SystemSwitchLoggingDgHostIndex_Type(Integer32):
    """Custom type systemSwitchLoggingDgHostIndex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SystemSwitchLoggingDgHostIndex_Type.__name__ = "Integer32"
_SystemSwitchLoggingDgHostIndex_Object = MibTableColumn
systemSwitchLoggingDgHostIndex = _SystemSwitchLoggingDgHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 27, 1, 1),
    _SystemSwitchLoggingDgHostIndex_Type()
)
systemSwitchLoggingDgHostIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    systemSwitchLoggingDgHostIndex.setStatus("current")
_SystemSwitchLoggingDgHostIpType_Type = InetAddressType
_SystemSwitchLoggingDgHostIpType_Object = MibTableColumn
systemSwitchLoggingDgHostIpType = _SystemSwitchLoggingDgHostIpType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 27, 1, 2),
    _SystemSwitchLoggingDgHostIpType_Type()
)
systemSwitchLoggingDgHostIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSwitchLoggingDgHostIpType.setStatus("current")
_SystemSwitchLoggingDgHostIpAddr_Type = InetAddress
_SystemSwitchLoggingDgHostIpAddr_Object = MibTableColumn
systemSwitchLoggingDgHostIpAddr = _SystemSwitchLoggingDgHostIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 6, 27, 1, 3),
    _SystemSwitchLoggingDgHostIpAddr_Type()
)
systemSwitchLoggingDgHostIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSwitchLoggingDgHostIpAddr.setStatus("current")
_SystemDNS_ObjectIdentity = ObjectIdentity
systemDNS = _SystemDNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 7)
)


class _SystemDNSEnableDnsResolver_Type(Enable):
    """Custom type systemDNSEnableDnsResolver based on Enable"""
    defaultValue = 2


_SystemDNSEnableDnsResolver_Type.__name__ = "Enable"
_SystemDNSEnableDnsResolver_Object = MibScalar
systemDNSEnableDnsResolver = _SystemDNSEnableDnsResolver_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 7, 1),
    _SystemDNSEnableDnsResolver_Type()
)
systemDNSEnableDnsResolver.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    systemDNSEnableDnsResolver.setStatus("current")


class _SystemDNSDomainName_Type(SnmpAdminString):
    """Custom type systemDNSDomainName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemDNSDomainName_Type.__name__ = "SnmpAdminString"
_SystemDNSDomainName_Object = MibScalar
systemDNSDomainName = _SystemDNSDomainName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 7, 2),
    _SystemDNSDomainName_Type()
)
systemDNSDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    systemDNSDomainName.setStatus("current")


class _SystemDNSNsAddr1_Type(IpAddress):
    """Custom type systemDNSNsAddr1 based on IpAddress"""
    defaultHexValue = "00000000"


_SystemDNSNsAddr1_Type.__name__ = "IpAddress"
_SystemDNSNsAddr1_Object = MibScalar
systemDNSNsAddr1 = _SystemDNSNsAddr1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 7, 3),
    _SystemDNSNsAddr1_Type()
)
systemDNSNsAddr1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    systemDNSNsAddr1.setStatus("current")


class _SystemDNSNsAddr2_Type(IpAddress):
    """Custom type systemDNSNsAddr2 based on IpAddress"""
    defaultHexValue = "00000000"


_SystemDNSNsAddr2_Type.__name__ = "IpAddress"
_SystemDNSNsAddr2_Object = MibScalar
systemDNSNsAddr2 = _SystemDNSNsAddr2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 7, 4),
    _SystemDNSNsAddr2_Type()
)
systemDNSNsAddr2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    systemDNSNsAddr2.setStatus("current")


class _SystemDNSNsAddr3_Type(IpAddress):
    """Custom type systemDNSNsAddr3 based on IpAddress"""
    defaultHexValue = "00000000"


_SystemDNSNsAddr3_Type.__name__ = "IpAddress"
_SystemDNSNsAddr3_Object = MibScalar
systemDNSNsAddr3 = _SystemDNSNsAddr3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 7, 5),
    _SystemDNSNsAddr3_Type()
)
systemDNSNsAddr3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    systemDNSNsAddr3.setStatus("current")


class _SystemDNSNsIPv6Addr1_Type(Ipv6Address):
    """Custom type systemDNSNsIPv6Addr1 based on Ipv6Address"""
    defaultHexValue = "00000000000000000000000000000000"


_SystemDNSNsIPv6Addr1_Type.__name__ = "Ipv6Address"
_SystemDNSNsIPv6Addr1_Object = MibScalar
systemDNSNsIPv6Addr1 = _SystemDNSNsIPv6Addr1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 7, 6),
    _SystemDNSNsIPv6Addr1_Type()
)
systemDNSNsIPv6Addr1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    systemDNSNsIPv6Addr1.setStatus("current")


class _SystemDNSNsIPv6Addr2_Type(Ipv6Address):
    """Custom type systemDNSNsIPv6Addr2 based on Ipv6Address"""
    defaultHexValue = "00000000000000000000000000000000"


_SystemDNSNsIPv6Addr2_Type.__name__ = "Ipv6Address"
_SystemDNSNsIPv6Addr2_Object = MibScalar
systemDNSNsIPv6Addr2 = _SystemDNSNsIPv6Addr2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 7, 7),
    _SystemDNSNsIPv6Addr2_Type()
)
systemDNSNsIPv6Addr2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    systemDNSNsIPv6Addr2.setStatus("current")


class _SystemDNSNsIPv6Addr3_Type(Ipv6Address):
    """Custom type systemDNSNsIPv6Addr3 based on Ipv6Address"""
    defaultHexValue = "00000000000000000000000000000000"


_SystemDNSNsIPv6Addr3_Type.__name__ = "Ipv6Address"
_SystemDNSNsIPv6Addr3_Object = MibScalar
systemDNSNsIPv6Addr3 = _SystemDNSNsIPv6Addr3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 7, 8),
    _SystemDNSNsIPv6Addr3_Type()
)
systemDNSNsIPv6Addr3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    systemDNSNsIPv6Addr3.setStatus("current")
_SystemBlueToothServices_ObjectIdentity = ObjectIdentity
systemBlueToothServices = _SystemBlueToothServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 8)
)


class _SystemServicesBluetoothEnable_Type(Enable):
    """Custom type systemServicesBluetoothEnable based on Enable"""
    defaultValue = 1


_SystemServicesBluetoothEnable_Type.__name__ = "Enable"
_SystemServicesBluetoothEnable_Object = MibScalar
systemServicesBluetoothEnable = _SystemServicesBluetoothEnable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 8, 1),
    _SystemServicesBluetoothEnable_Type()
)
systemServicesBluetoothEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesBluetoothEnable.setStatus("current")


class _SystemServicesBluetoothTxPower_Type(Integer32):
    """Custom type systemServicesBluetoothTxPower based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("high", 2))
    )


_SystemServicesBluetoothTxPower_Type.__name__ = "Integer32"
_SystemServicesBluetoothTxPower_Object = MibScalar
systemServicesBluetoothTxPower = _SystemServicesBluetoothTxPower_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 8, 2),
    _SystemServicesBluetoothTxPower_Type()
)
systemServicesBluetoothTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServicesBluetoothTxPower.setStatus("current")
_SystemServicesBluetoothTable_Object = MibTable
systemServicesBluetoothTable = _SystemServicesBluetoothTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 8, 3)
)
if mibBuilder.loadTexts:
    systemServicesBluetoothTable.setStatus("current")
_SystemServicesBluetoothEntry_Object = MibTableRow
systemServicesBluetoothEntry = _SystemServicesBluetoothEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 8, 3, 1)
)
systemServicesBluetoothEntry.setIndexNames(
    (0, "ALCATEL-ENT1-SYSTEM-MIB", "systemServicesBluetoothChassisId"),
)
if mibBuilder.loadTexts:
    systemServicesBluetoothEntry.setStatus("current")
_SystemServicesBluetoothChassisId_Type = VirtualOperChassisId
_SystemServicesBluetoothChassisId_Object = MibTableColumn
systemServicesBluetoothChassisId = _SystemServicesBluetoothChassisId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 8, 3, 1, 1),
    _SystemServicesBluetoothChassisId_Type()
)
systemServicesBluetoothChassisId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    systemServicesBluetoothChassisId.setStatus("current")


class _SystemServicesBluetoothStatus_Type(Integer32):
    """Custom type systemServicesBluetoothStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 1),
          ("connectionInactive", 2),
          ("connectionActive", 3))
    )


_SystemServicesBluetoothStatus_Type.__name__ = "Integer32"
_SystemServicesBluetoothStatus_Object = MibTableColumn
systemServicesBluetoothStatus = _SystemServicesBluetoothStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 8, 3, 1, 2),
    _SystemServicesBluetoothStatus_Type()
)
systemServicesBluetoothStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemServicesBluetoothStatus.setStatus("current")
_SystemFips_ObjectIdentity = ObjectIdentity
systemFips = _SystemFips_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 9)
)


class _SystemFipsAdminState_Type(Enable):
    """Custom type systemFipsAdminState based on Enable"""
    defaultValue = 2


_SystemFipsAdminState_Type.__name__ = "Enable"
_SystemFipsAdminState_Object = MibScalar
systemFipsAdminState = _SystemFipsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 9, 1),
    _SystemFipsAdminState_Type()
)
systemFipsAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemFipsAdminState.setStatus("current")
_SystemFipsOperState_Type = Enable
_SystemFipsOperState_Object = MibScalar
systemFipsOperState = _SystemFipsOperState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 9, 2),
    _SystemFipsOperState_Type()
)
systemFipsOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFipsOperState.setStatus("current")
_SystemVcHardware_ObjectIdentity = ObjectIdentity
systemVcHardware = _SystemVcHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 10)
)
_SystemVcHardwareTable_Object = MibTable
systemVcHardwareTable = _SystemVcHardwareTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 10, 1)
)
if mibBuilder.loadTexts:
    systemVcHardwareTable.setStatus("current")
_SystemVcHardwareEntry_Object = MibTableRow
systemVcHardwareEntry = _SystemVcHardwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 10, 1, 1)
)
systemVcHardwareEntry.setIndexNames(
    (0, "ALCATEL-ENT1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperChasId"),
)
if mibBuilder.loadTexts:
    systemVcHardwareEntry.setStatus("current")


class _SystemVcHardwareCpuVendor_Type(SnmpAdminString):
    """Custom type systemVcHardwareCpuVendor based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemVcHardwareCpuVendor_Type.__name__ = "SnmpAdminString"
_SystemVcHardwareCpuVendor_Object = MibTableColumn
systemVcHardwareCpuVendor = _SystemVcHardwareCpuVendor_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 10, 1, 1, 1),
    _SystemVcHardwareCpuVendor_Type()
)
systemVcHardwareCpuVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemVcHardwareCpuVendor.setStatus("current")


class _SystemVcHardwareCpuModel_Type(SnmpAdminString):
    """Custom type systemVcHardwareCpuModel based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemVcHardwareCpuModel_Type.__name__ = "SnmpAdminString"
_SystemVcHardwareCpuModel_Object = MibTableColumn
systemVcHardwareCpuModel = _SystemVcHardwareCpuModel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 10, 1, 1, 2),
    _SystemVcHardwareCpuModel_Type()
)
systemVcHardwareCpuModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemVcHardwareCpuModel.setStatus("current")


class _SystemVcHardwareFlashMfg_Type(Integer32):
    """Custom type systemVcHardwareFlashMfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              13)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("amd", 2),
          ("intel", 3),
          ("atmel", 4),
          ("micron", 5),
          ("kingston", 6),
          ("toshiba", 7),
          ("sandisk", 8),
          ("sst", 9),
          ("spansion", 10),
          ("wintec", 13))
    )


_SystemVcHardwareFlashMfg_Type.__name__ = "Integer32"
_SystemVcHardwareFlashMfg_Object = MibTableColumn
systemVcHardwareFlashMfg = _SystemVcHardwareFlashMfg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 10, 1, 1, 3),
    _SystemVcHardwareFlashMfg_Type()
)
systemVcHardwareFlashMfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemVcHardwareFlashMfg.setStatus("current")
_SystemVcHardwareFlashSize_Type = Counter64
_SystemVcHardwareFlashSize_Object = MibTableColumn
systemVcHardwareFlashSize = _SystemVcHardwareFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 10, 1, 1, 4),
    _SystemVcHardwareFlashSize_Type()
)
systemVcHardwareFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemVcHardwareFlashSize.setStatus("current")


class _SystemVcHardwareMemoryMfg_Type(Integer32):
    """Custom type systemVcHardwareMemoryMfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("amd", 2),
          ("intel", 3),
          ("atmel", 4),
          ("micron", 5),
          ("kingston", 6),
          ("toshiba", 7),
          ("agilent", 8),
          ("dataram", 10),
          ("interward", 11),
          ("notreadable", 12))
    )


_SystemVcHardwareMemoryMfg_Type.__name__ = "Integer32"
_SystemVcHardwareMemoryMfg_Object = MibTableColumn
systemVcHardwareMemoryMfg = _SystemVcHardwareMemoryMfg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 10, 1, 1, 5),
    _SystemVcHardwareMemoryMfg_Type()
)
systemVcHardwareMemoryMfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemVcHardwareMemoryMfg.setStatus("current")
_SystemVcHardwareMemorySize_Type = Counter64
_SystemVcHardwareMemorySize_Object = MibTableColumn
systemVcHardwareMemorySize = _SystemVcHardwareMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 10, 1, 1, 6),
    _SystemVcHardwareMemorySize_Type()
)
systemVcHardwareMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemVcHardwareMemorySize.setStatus("current")


class _SystemVcHardwareUbootVersion_Type(SnmpAdminString):
    """Custom type systemVcHardwareUbootVersion based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemVcHardwareUbootVersion_Type.__name__ = "SnmpAdminString"
_SystemVcHardwareUbootVersion_Object = MibTableColumn
systemVcHardwareUbootVersion = _SystemVcHardwareUbootVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 10, 1, 1, 7),
    _SystemVcHardwareUbootVersion_Type()
)
systemVcHardwareUbootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemVcHardwareUbootVersion.setStatus("current")


class _SystemVcHardwareFpga1Version_Type(SnmpAdminString):
    """Custom type systemVcHardwareFpga1Version based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemVcHardwareFpga1Version_Type.__name__ = "SnmpAdminString"
_SystemVcHardwareFpga1Version_Object = MibTableColumn
systemVcHardwareFpga1Version = _SystemVcHardwareFpga1Version_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 10, 1, 1, 8),
    _SystemVcHardwareFpga1Version_Type()
)
systemVcHardwareFpga1Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemVcHardwareFpga1Version.setStatus("current")


class _SystemVcHardwareFpga2Version_Type(SnmpAdminString):
    """Custom type systemVcHardwareFpga2Version based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemVcHardwareFpga2Version_Type.__name__ = "SnmpAdminString"
_SystemVcHardwareFpga2Version_Object = MibTableColumn
systemVcHardwareFpga2Version = _SystemVcHardwareFpga2Version_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 10, 1, 1, 9),
    _SystemVcHardwareFpga2Version_Type()
)
systemVcHardwareFpga2Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemVcHardwareFpga2Version.setStatus("current")


class _SystemVcHardwarePowerSuppliesPresent_Type(Bits):
    """Custom type systemVcHardwarePowerSuppliesPresent based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("ps1", 0),
          ("ps2", 1),
          ("ps3", 2),
          ("ps4", 3),
          ("ps5", 4),
          ("ps6", 5),
          ("ps7", 6),
          ("ps8", 7),
          ("ps9", 8),
          ("ps10", 9),
          ("ps11", 10),
          ("ps12", 11),
          ("ps13", 12),
          ("ps14", 13),
          ("ps15", 14),
          ("ps16", 15))
    )

_SystemVcHardwarePowerSuppliesPresent_Type.__name__ = "Bits"
_SystemVcHardwarePowerSuppliesPresent_Object = MibTableColumn
systemVcHardwarePowerSuppliesPresent = _SystemVcHardwarePowerSuppliesPresent_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 10, 1, 1, 10),
    _SystemVcHardwarePowerSuppliesPresent_Type()
)
systemVcHardwarePowerSuppliesPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemVcHardwarePowerSuppliesPresent.setStatus("current")


class _SystemVcHardwareNisPresent_Type(Bits):
    """Custom type systemVcHardwareNisPresent based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("ni1", 0),
          ("ni2", 1),
          ("ni3", 2),
          ("ni4", 3),
          ("ni5", 4),
          ("ni6", 5),
          ("ni7", 6),
          ("ni8", 7),
          ("ni9", 8),
          ("ni10", 9),
          ("ni11", 10),
          ("ni12", 11),
          ("ni13", 12),
          ("ni14", 13),
          ("ni15", 14),
          ("ni16", 15))
    )

_SystemVcHardwareNisPresent_Type.__name__ = "Bits"
_SystemVcHardwareNisPresent_Object = MibTableColumn
systemVcHardwareNisPresent = _SystemVcHardwareNisPresent_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 10, 1, 1, 11),
    _SystemVcHardwareNisPresent_Type()
)
systemVcHardwareNisPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemVcHardwareNisPresent.setStatus("current")


class _SystemVcHardwareCFMsPresent_Type(Bits):
    """Custom type systemVcHardwareCFMsPresent based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("cfm1", 0),
          ("cfm2", 1),
          ("cfm3", 2),
          ("cfm4", 3),
          ("cfm5", 4),
          ("cfm6", 5),
          ("cfm7", 6),
          ("cfm8", 7))
    )

_SystemVcHardwareCFMsPresent_Type.__name__ = "Bits"
_SystemVcHardwareCFMsPresent_Object = MibTableColumn
systemVcHardwareCFMsPresent = _SystemVcHardwareCFMsPresent_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 10, 1, 1, 12),
    _SystemVcHardwareCFMsPresent_Type()
)
systemVcHardwareCFMsPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemVcHardwareCFMsPresent.setStatus("current")


class _SystemVcHardwareFanTraysPresent_Type(Bits):
    """Custom type systemVcHardwareFanTraysPresent based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("fanTray1", 0),
          ("fanTray2", 1),
          ("fanTray3", 2),
          ("fanTray4", 3),
          ("fanTray5", 4),
          ("fanTray6", 5),
          ("fanTray7", 6),
          ("fanTray8", 7))
    )

_SystemVcHardwareFanTraysPresent_Type.__name__ = "Bits"
_SystemVcHardwareFanTraysPresent_Object = MibTableColumn
systemVcHardwareFanTraysPresent = _SystemVcHardwareFanTraysPresent_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 1, 10, 1, 1, 13),
    _SystemVcHardwareFanTraysPresent_Type()
)
systemVcHardwareFanTraysPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemVcHardwareFanTraysPresent.setStatus("current")
_AlcatelIND1SystemMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1SystemMIBConformance = _AlcatelIND1SystemMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1SystemMIBConformance.setStatus("current")
_AlcatelIND1SystemMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1SystemMIBGroups = _AlcatelIND1SystemMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1SystemMIBGroups.setStatus("current")
_AlcatelIND1SystemMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1SystemMIBCompliances = _AlcatelIND1SystemMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1SystemMIBCompliances.setStatus("current")
_AlcatelIND1SystemMIBTrapObjects_ObjectIdentity = ObjectIdentity
alcatelIND1SystemMIBTrapObjects = _AlcatelIND1SystemMIBTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    alcatelIND1SystemMIBTrapObjects.setStatus("current")


class _SystemSwlogName_Type(SnmpAdminString):
    """Custom type systemSwlogName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemSwlogName_Type.__name__ = "SnmpAdminString"
_SystemSwlogName_Object = MibScalar
systemSwlogName = _SystemSwlogName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 3, 1),
    _SystemSwlogName_Type()
)
systemSwlogName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSwlogName.setStatus("current")
_AlcatelIND1SystemMIBTraps_ObjectIdentity = ObjectIdentity
alcatelIND1SystemMIBTraps = _AlcatelIND1SystemMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 4)
)
if mibBuilder.loadTexts:
    alcatelIND1SystemMIBTraps.setStatus("current")

# Managed Objects groups

systemMicrocodeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 2, 1, 1)
)
systemMicrocodeGroup.setObjects(
      *(("ALCATEL-ENT1-SYSTEM-MIB", "systemMicrocodePackageVersion"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemMicrocodePackageName"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemMicrocodePackageDescription"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemMicrocodePackageStatus"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemMicrocodePackageSize"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemMicrocodeLoadedDirectory"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemMicrocodeLoadedVersion"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemMicrocodeLoadedName"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemMicrocodeLoadedDescription"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemMicrocodeLoadedSize"))
)
if mibBuilder.loadTexts:
    systemMicrocodeGroup.setStatus("current")

systemBootParamsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 2, 1, 2)
)
systemBootParamsGroup.setObjects(
      *(("ALCATEL-ENT1-SYSTEM-MIB", "systemBootNetwork"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemBootNetworkGateway"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemBootNetworkNetmask"))
)
if mibBuilder.loadTexts:
    systemBootParamsGroup.setStatus("current")

systemHardwareGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 2, 1, 3)
)
systemHardwareGroup.setObjects(
      *(("ALCATEL-ENT1-SYSTEM-MIB", "systemHardwareFlashMfg"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemHardwareFlashSize"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemHardwareMemoryMfg"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemHardwareMemorySize"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemHardwareNVRAMBatteryLow"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemHardwareBootCpuType"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemHardwareJumperInterruptBoot"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemHardwareJumperForceUartDefaults"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemHardwareJumperRunExtendedMemoryDiagnostics"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemHardwareJumperSpare"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemHardwareFpgaVersionIndex"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemHardwareFpgaVersion"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemHardwareBootRomVersion"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemHardwareDefaultMiniBootVersion"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemHardwareBackupMiniBootVersion"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemHardwareCpldVersion"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemHardwareMinorFpgaVersion"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemHardwareProdRegId"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemHardwareRevisionRegister"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemHardwareUbootMinibootVersion"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemHardwareUbootVersion"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemHardwareXfpId"))
)
if mibBuilder.loadTexts:
    systemHardwareGroup.setStatus("current")

systemServicesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 2, 1, 4)
)
systemServicesGroup.setObjects(
      *(("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesDate"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesTime"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesTimezone"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesTimezoneStartWeek"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesTimezoneStartDay"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesTimezoneStartMonth"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesTimezoneStartTime"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesTimezoneOffset"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesTimezoneEndWeek"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesTimezoneEndDay"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesTimezoneEndMonth"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesTimezoneEndTime"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesEnableDST"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesWorkingDirectory"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesArg1"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesArg2"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesArg3"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesArg4"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesArg5"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesArg6"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesArg7"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesArg8"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesArg9"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesAction"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesResultCode"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesResultString"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesKtraceEnable"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesSystraceEnable"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesTtyLines"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesTtyColumns"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesMemMonitorEnable"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesKtraceLevelAppId"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesKtraceLevel"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesSystraceLevelAppId"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesSystraceLevel"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemUpdateStatus"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemUpdateErrorCode"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesActionPercentComplete"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesArchiveName"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesArchiveType"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesArchiveSize"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesArchiveAttr"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesUsbEnable"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesUsbAutoCopyEnable"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesUsbMounted"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesArchiveIndex"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesCurrentArchivePathName"))
)
if mibBuilder.loadTexts:
    systemServicesGroup.setStatus("current")

systemFileSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 2, 1, 5)
)
systemFileSystemGroup.setObjects(
      *(("ALCATEL-ENT1-SYSTEM-MIB", "systemFileSystemIndex"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemFileSystemFreeSpace"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemFileSystemName"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemFileSystemDirectoryName"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemFileSystemDirectoryDateTime"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemFileSystemFileIndex"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemFileSystemFileName"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemFileSystemFileType"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemFileSystemFileSize"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemFileSystemFileAttr"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemFileSystemFileDateTime"))
)
if mibBuilder.loadTexts:
    systemFileSystemGroup.setStatus("current")

systemSwitchLoggingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 2, 1, 6)
)
systemSwitchLoggingGroup.setObjects(
      *(("ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingIndex"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingEnable"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingFlash"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingSocket"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingSocketIpAddr"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingConsole"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingClear"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingFileSize"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingLevel"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingApplicationAppId"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingApplicationAppName"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingApplicationSubAppId"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingApplicationSubAppName"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingApplicationSubAppLevel"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingApplicationSubAppVrfLevelIndex"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingApplicationSubAppVrfLevelString"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingAppName"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingDuplicateDetect"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingPreamble"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingDebug"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingVrf"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingHashAgeLimit"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingTty"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingSubAppNbr"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingLibraryName"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingLoopback0"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingConsoleLevel"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingHostCount"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingUserCommandStatus"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingSysLogFacilityId"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingHostIpAddr"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingHostPort"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingHostStatus"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingHostUserCommandHost"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingHostVrfName"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingHostv6IpAddr"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingHostv6Port"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingHostv6Status"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingHostv6UserCommandHost"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingHostv6VrfName"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingDgHostIpType"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingDgHostIpAddr"))
)
if mibBuilder.loadTexts:
    systemSwitchLoggingGroup.setStatus("current")

systemDNSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 2, 1, 7)
)
systemDNSGroup.setObjects(
      *(("ALCATEL-ENT1-SYSTEM-MIB", "systemDNSEnableDnsResolver"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemDNSDomainName"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemDNSNsAddr1"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemDNSNsAddr2"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemDNSNsAddr3"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemDNSNsIPv6Addr1"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemDNSNsIPv6Addr2"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemDNSNsIPv6Addr3"))
)
if mibBuilder.loadTexts:
    systemDNSGroup.setStatus("current")

systemBlueToothServicesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 2, 1, 8)
)
systemBlueToothServicesGroup.setObjects(
      *(("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesBluetoothEnable"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesBluetoothTxPower"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesBluetoothStatus"))
)
if mibBuilder.loadTexts:
    systemBlueToothServicesGroup.setStatus("current")

systemFipsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 2, 1, 9)
)
systemFipsGroup.setObjects(
      *(("ALCATEL-ENT1-SYSTEM-MIB", "systemFipsAdminState"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemFipsOperState"))
)
if mibBuilder.loadTexts:
    systemFipsGroup.setStatus("current")

systemVcHardwareGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 2, 1, 10)
)
systemVcHardwareGroup.setObjects(
      *(("ALCATEL-ENT1-SYSTEM-MIB", "systemVcHardwareCpuVendor"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemVcHardwareCpuModel"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemVcHardwareFlashMfg"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemVcHardwareFlashSize"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemVcHardwareMemoryMfg"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemVcHardwareMemorySize"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemVcHardwareUbootVersion"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemVcHardwareFpga1Version"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemVcHardwareFpga2Version"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemVcHardwarePowerSuppliesPresent"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemVcHardwareNisPresent"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemVcHardwareCFMsPresent"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemVcHardwareFanTraysPresent"))
)
if mibBuilder.loadTexts:
    systemVcHardwareGroup.setStatus("current")

systemSwlogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 2, 1, 11)
)
systemSwlogGroup.setObjects(
    ("ALCATEL-ENT1-SYSTEM-MIB", "systemSwlogName")
)
if mibBuilder.loadTexts:
    systemSwlogGroup.setStatus("current")


# Notification objects

systemSwlogSizeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 4, 0, 1)
)
systemSwlogSizeTrap.setObjects(
    ("ALCATEL-ENT1-SYSTEM-MIB", "systemSwlogName")
)
if mibBuilder.loadTexts:
    systemSwlogSizeTrap.setStatus(
        "current"
    )


# Notifications groups

systemNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 2, 1, 12)
)
systemNotificationGroup.setObjects(
    ("ALCATEL-ENT1-SYSTEM-MIB", "systemSwlogSizeTrap")
)
if mibBuilder.loadTexts:
    systemNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alcatelIND1SystemMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2, 1, 2, 2, 1)
)
alcatelIND1SystemMIBCompliance.setObjects(
      *(("ALCATEL-ENT1-SYSTEM-MIB", "systemMicrocodeGroup"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemBootParamsGroup"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemHardwareGroup"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemServicesGroup"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemFileSystemGroup"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemSwitchLoggingGroup"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemDNSGroup"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemBlueToothServicesGroup"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemFipsGroup"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemVcHardwareGroup"),
        ("ALCATEL-ENT1-SYSTEM-MIB", "systemNotificationGroup"))
)
if mibBuilder.loadTexts:
    alcatelIND1SystemMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-ENT1-SYSTEM-MIB",
    **{"SystemFileType": SystemFileType,
       "SwitchLoggingIndex": SwitchLoggingIndex,
       "AppIdIndex": AppIdIndex,
       "Enable": Enable,
       "FileSystemIndex": FileSystemIndex,
       "SeverityLevel": SeverityLevel,
       "SysLogFacilityId": SysLogFacilityId,
       "CommandPercentComplete": CommandPercentComplete,
       "VrfId": VrfId,
       "AgeLimit": AgeLimit,
       "alcatelIND1SystemMIB": alcatelIND1SystemMIB,
       "alcatelIND1SystemMIBObjects": alcatelIND1SystemMIBObjects,
       "systemMicrocode": systemMicrocode,
       "systemMicrocodePackageTable": systemMicrocodePackageTable,
       "systemMicrocodePackageEntry": systemMicrocodePackageEntry,
       "systemMicrocodePackageDirectoryIndex": systemMicrocodePackageDirectoryIndex,
       "systemMicrocodePackageDirectory": systemMicrocodePackageDirectory,
       "systemMicrocodePackageIndex": systemMicrocodePackageIndex,
       "systemMicrocodePackageVersion": systemMicrocodePackageVersion,
       "systemMicrocodePackageName": systemMicrocodePackageName,
       "systemMicrocodePackageDescription": systemMicrocodePackageDescription,
       "systemMicrocodePackageStatus": systemMicrocodePackageStatus,
       "systemMicrocodePackageSize": systemMicrocodePackageSize,
       "systemMicrocodeLoadedTable": systemMicrocodeLoadedTable,
       "systemMicrocodeLoadedEntry": systemMicrocodeLoadedEntry,
       "systemMicrocodeLoadedIndex": systemMicrocodeLoadedIndex,
       "systemMicrocodeLoadedDirectory": systemMicrocodeLoadedDirectory,
       "systemMicrocodeLoadedVersion": systemMicrocodeLoadedVersion,
       "systemMicrocodeLoadedName": systemMicrocodeLoadedName,
       "systemMicrocodeLoadedDescription": systemMicrocodeLoadedDescription,
       "systemMicrocodeLoadedSize": systemMicrocodeLoadedSize,
       "systemBootParams": systemBootParams,
       "systemBootNetwork": systemBootNetwork,
       "systemBootNetworkGateway": systemBootNetworkGateway,
       "systemBootNetworkNetmask": systemBootNetworkNetmask,
       "systemHardware": systemHardware,
       "systemHardwareFlashMfg": systemHardwareFlashMfg,
       "systemHardwareFlashSize": systemHardwareFlashSize,
       "systemHardwareMemoryMfg": systemHardwareMemoryMfg,
       "systemHardwareMemorySize": systemHardwareMemorySize,
       "systemHardwareNVRAMBatteryLow": systemHardwareNVRAMBatteryLow,
       "systemHardwareBootCpuType": systemHardwareBootCpuType,
       "systemHardwareJumperInterruptBoot": systemHardwareJumperInterruptBoot,
       "systemHardwareJumperForceUartDefaults": systemHardwareJumperForceUartDefaults,
       "systemHardwareJumperRunExtendedMemoryDiagnostics": systemHardwareJumperRunExtendedMemoryDiagnostics,
       "systemHardwareJumperSpare": systemHardwareJumperSpare,
       "systemHardwareFpgaVersionTable": systemHardwareFpgaVersionTable,
       "systemHardwareFpgaVersionEntry": systemHardwareFpgaVersionEntry,
       "systemHardwareFpgaVersionIndex": systemHardwareFpgaVersionIndex,
       "systemHardwareFpgaVersion": systemHardwareFpgaVersion,
       "systemHardwareBootRomVersion": systemHardwareBootRomVersion,
       "systemHardwareBackupMiniBootVersion": systemHardwareBackupMiniBootVersion,
       "systemHardwareDefaultMiniBootVersion": systemHardwareDefaultMiniBootVersion,
       "systemHardwareMinorFpgaVersion": systemHardwareMinorFpgaVersion,
       "systemHardwareCpldVersion": systemHardwareCpldVersion,
       "systemHardwareUbootVersion": systemHardwareUbootVersion,
       "systemHardwareProdRegId": systemHardwareProdRegId,
       "systemHardwareRevisionRegister": systemHardwareRevisionRegister,
       "systemHardwareXfpId": systemHardwareXfpId,
       "systemHardwareUbootMinibootVersion": systemHardwareUbootMinibootVersion,
       "systemFileSystem": systemFileSystem,
       "systemFileSystemTable": systemFileSystemTable,
       "systemFileSystemEntry": systemFileSystemEntry,
       "systemFileSystemIndex": systemFileSystemIndex,
       "systemFileSystemName": systemFileSystemName,
       "systemFileSystemFreeSpace": systemFileSystemFreeSpace,
       "systemFileSystemDirectoryName": systemFileSystemDirectoryName,
       "systemFileSystemDirectoryDateTime": systemFileSystemDirectoryDateTime,
       "systemFileSystemFileTable": systemFileSystemFileTable,
       "systemFileSystemFileEntry": systemFileSystemFileEntry,
       "systemFileSystemFileIndex": systemFileSystemFileIndex,
       "systemFileSystemFileName": systemFileSystemFileName,
       "systemFileSystemFileType": systemFileSystemFileType,
       "systemFileSystemFileSize": systemFileSystemFileSize,
       "systemFileSystemFileAttr": systemFileSystemFileAttr,
       "systemFileSystemFileDateTime": systemFileSystemFileDateTime,
       "systemServices": systemServices,
       "systemServicesDate": systemServicesDate,
       "systemServicesTime": systemServicesTime,
       "systemServicesTimezone": systemServicesTimezone,
       "systemServicesTimezoneStartWeek": systemServicesTimezoneStartWeek,
       "systemServicesTimezoneStartDay": systemServicesTimezoneStartDay,
       "systemServicesTimezoneStartMonth": systemServicesTimezoneStartMonth,
       "systemServicesTimezoneStartTime": systemServicesTimezoneStartTime,
       "systemServicesTimezoneOffset": systemServicesTimezoneOffset,
       "systemServicesTimezoneEndWeek": systemServicesTimezoneEndWeek,
       "systemServicesTimezoneEndDay": systemServicesTimezoneEndDay,
       "systemServicesTimezoneEndMonth": systemServicesTimezoneEndMonth,
       "systemServicesTimezoneEndTime": systemServicesTimezoneEndTime,
       "systemServicesEnableDST": systemServicesEnableDST,
       "systemServicesWorkingDirectory": systemServicesWorkingDirectory,
       "systemServicesArg1": systemServicesArg1,
       "systemServicesArg2": systemServicesArg2,
       "systemServicesArg3": systemServicesArg3,
       "systemServicesArg4": systemServicesArg4,
       "systemServicesArg5": systemServicesArg5,
       "systemServicesArg6": systemServicesArg6,
       "systemServicesArg7": systemServicesArg7,
       "systemServicesArg8": systemServicesArg8,
       "systemServicesArg9": systemServicesArg9,
       "systemServicesAction": systemServicesAction,
       "systemServicesResultCode": systemServicesResultCode,
       "systemServicesResultString": systemServicesResultString,
       "systemServicesKtraceEnable": systemServicesKtraceEnable,
       "systemServicesSystraceEnable": systemServicesSystraceEnable,
       "systemServicesTtyLines": systemServicesTtyLines,
       "systemServicesTtyColumns": systemServicesTtyColumns,
       "systemServicesMemMonitorEnable": systemServicesMemMonitorEnable,
       "systemServicesKtraceLevelTable": systemServicesKtraceLevelTable,
       "systemServicesKtraceLevelEntry": systemServicesKtraceLevelEntry,
       "systemServicesKtraceLevelAppId": systemServicesKtraceLevelAppId,
       "systemServicesKtraceLevel": systemServicesKtraceLevel,
       "systemServicesSystraceLevelTable": systemServicesSystraceLevelTable,
       "systemServicesSystraceLevelEntry": systemServicesSystraceLevelEntry,
       "systemServicesSystraceLevelAppId": systemServicesSystraceLevelAppId,
       "systemServicesSystraceLevel": systemServicesSystraceLevel,
       "systemUpdateStatusTable": systemUpdateStatusTable,
       "systemUpdateStatusEntry": systemUpdateStatusEntry,
       "systemUpdateIndex": systemUpdateIndex,
       "systemUpdateStatus": systemUpdateStatus,
       "systemUpdateErrorCode": systemUpdateErrorCode,
       "systemServicesActionPercentComplete": systemServicesActionPercentComplete,
       "systemServicesCurrentArchivePathName": systemServicesCurrentArchivePathName,
       "systemServicesArchiveTable": systemServicesArchiveTable,
       "systemServicesArchiveEntry": systemServicesArchiveEntry,
       "systemServicesArchiveIndex": systemServicesArchiveIndex,
       "systemServicesArchiveName": systemServicesArchiveName,
       "systemServicesArchiveType": systemServicesArchiveType,
       "systemServicesArchiveSize": systemServicesArchiveSize,
       "systemServicesArchiveAttr": systemServicesArchiveAttr,
       "systemServicesUsbEnable": systemServicesUsbEnable,
       "systemServicesUsbAutoCopyEnable": systemServicesUsbAutoCopyEnable,
       "systemServicesUsbMounted": systemServicesUsbMounted,
       "systemSwitchLogging": systemSwitchLogging,
       "systemSwitchLoggingIndex": systemSwitchLoggingIndex,
       "systemSwitchLoggingEnable": systemSwitchLoggingEnable,
       "systemSwitchLoggingFlash": systemSwitchLoggingFlash,
       "systemSwitchLoggingSocket": systemSwitchLoggingSocket,
       "systemSwitchLoggingSocketIpAddr": systemSwitchLoggingSocketIpAddr,
       "systemSwitchLoggingConsole": systemSwitchLoggingConsole,
       "systemSwitchLoggingApplicationTable": systemSwitchLoggingApplicationTable,
       "systemSwitchLoggingLevelEntry": systemSwitchLoggingLevelEntry,
       "systemSwitchLoggingApplicationAppId": systemSwitchLoggingApplicationAppId,
       "systemSwitchLoggingApplicationSubAppId": systemSwitchLoggingApplicationSubAppId,
       "systemSwitchLoggingApplicationSubAppVrfLevelIndex": systemSwitchLoggingApplicationSubAppVrfLevelIndex,
       "systemSwitchLoggingApplicationAppName": systemSwitchLoggingApplicationAppName,
       "systemSwitchLoggingApplicationSubAppName": systemSwitchLoggingApplicationSubAppName,
       "systemSwitchLoggingApplicationSubAppLevel": systemSwitchLoggingApplicationSubAppLevel,
       "systemSwitchLoggingApplicationSubAppVrfLevelString": systemSwitchLoggingApplicationSubAppVrfLevelString,
       "systemSwitchLoggingClear": systemSwitchLoggingClear,
       "systemSwitchLoggingFileSize": systemSwitchLoggingFileSize,
       "systemSwitchLoggingHostTable": systemSwitchLoggingHostTable,
       "systemSwitchLoggingHostEntry": systemSwitchLoggingHostEntry,
       "systemSwitchLoggingHostIpAddr": systemSwitchLoggingHostIpAddr,
       "systemSwitchLoggingHostPort": systemSwitchLoggingHostPort,
       "systemSwitchLoggingHostStatus": systemSwitchLoggingHostStatus,
       "systemSwitchLoggingHostUserCommandHost": systemSwitchLoggingHostUserCommandHost,
       "systemSwitchLoggingHostVrfName": systemSwitchLoggingHostVrfName,
       "systemSwitchLoggingHostv6Table": systemSwitchLoggingHostv6Table,
       "systemSwitchLoggingHostv6Entry": systemSwitchLoggingHostv6Entry,
       "systemSwitchLoggingHostv6IpAddr": systemSwitchLoggingHostv6IpAddr,
       "systemSwitchLoggingHostv6Port": systemSwitchLoggingHostv6Port,
       "systemSwitchLoggingHostv6Status": systemSwitchLoggingHostv6Status,
       "systemSwitchLoggingHostv6UserCommandHost": systemSwitchLoggingHostv6UserCommandHost,
       "systemSwitchLoggingHostv6VrfName": systemSwitchLoggingHostv6VrfName,
       "systemSwitchLoggingHostCount": systemSwitchLoggingHostCount,
       "systemSwitchLoggingConsoleLevel": systemSwitchLoggingConsoleLevel,
       "systemSwitchLoggingUserCommandStatus": systemSwitchLoggingUserCommandStatus,
       "systemSwitchLoggingSysLogFacilityId": systemSwitchLoggingSysLogFacilityId,
       "systemSwitchLoggingLevel": systemSwitchLoggingLevel,
       "systemSwitchLoggingAppName": systemSwitchLoggingAppName,
       "systemSwitchLoggingDuplicateDetect": systemSwitchLoggingDuplicateDetect,
       "systemSwitchLoggingPreamble": systemSwitchLoggingPreamble,
       "systemSwitchLoggingDebug": systemSwitchLoggingDebug,
       "systemSwitchLoggingVrf": systemSwitchLoggingVrf,
       "systemSwitchLoggingHashAgeLimit": systemSwitchLoggingHashAgeLimit,
       "systemSwitchLoggingTty": systemSwitchLoggingTty,
       "systemSwitchLoggingSubAppNbr": systemSwitchLoggingSubAppNbr,
       "systemSwitchLoggingLibraryName": systemSwitchLoggingLibraryName,
       "systemSwitchLoggingLoopback0": systemSwitchLoggingLoopback0,
       "systemSwitchLoggingDgHostTable": systemSwitchLoggingDgHostTable,
       "systemSwitchLoggingDgHostEntry": systemSwitchLoggingDgHostEntry,
       "systemSwitchLoggingDgHostIndex": systemSwitchLoggingDgHostIndex,
       "systemSwitchLoggingDgHostIpType": systemSwitchLoggingDgHostIpType,
       "systemSwitchLoggingDgHostIpAddr": systemSwitchLoggingDgHostIpAddr,
       "systemDNS": systemDNS,
       "systemDNSEnableDnsResolver": systemDNSEnableDnsResolver,
       "systemDNSDomainName": systemDNSDomainName,
       "systemDNSNsAddr1": systemDNSNsAddr1,
       "systemDNSNsAddr2": systemDNSNsAddr2,
       "systemDNSNsAddr3": systemDNSNsAddr3,
       "systemDNSNsIPv6Addr1": systemDNSNsIPv6Addr1,
       "systemDNSNsIPv6Addr2": systemDNSNsIPv6Addr2,
       "systemDNSNsIPv6Addr3": systemDNSNsIPv6Addr3,
       "systemBlueToothServices": systemBlueToothServices,
       "systemServicesBluetoothEnable": systemServicesBluetoothEnable,
       "systemServicesBluetoothTxPower": systemServicesBluetoothTxPower,
       "systemServicesBluetoothTable": systemServicesBluetoothTable,
       "systemServicesBluetoothEntry": systemServicesBluetoothEntry,
       "systemServicesBluetoothChassisId": systemServicesBluetoothChassisId,
       "systemServicesBluetoothStatus": systemServicesBluetoothStatus,
       "systemFips": systemFips,
       "systemFipsAdminState": systemFipsAdminState,
       "systemFipsOperState": systemFipsOperState,
       "systemVcHardware": systemVcHardware,
       "systemVcHardwareTable": systemVcHardwareTable,
       "systemVcHardwareEntry": systemVcHardwareEntry,
       "systemVcHardwareCpuVendor": systemVcHardwareCpuVendor,
       "systemVcHardwareCpuModel": systemVcHardwareCpuModel,
       "systemVcHardwareFlashMfg": systemVcHardwareFlashMfg,
       "systemVcHardwareFlashSize": systemVcHardwareFlashSize,
       "systemVcHardwareMemoryMfg": systemVcHardwareMemoryMfg,
       "systemVcHardwareMemorySize": systemVcHardwareMemorySize,
       "systemVcHardwareUbootVersion": systemVcHardwareUbootVersion,
       "systemVcHardwareFpga1Version": systemVcHardwareFpga1Version,
       "systemVcHardwareFpga2Version": systemVcHardwareFpga2Version,
       "systemVcHardwarePowerSuppliesPresent": systemVcHardwarePowerSuppliesPresent,
       "systemVcHardwareNisPresent": systemVcHardwareNisPresent,
       "systemVcHardwareCFMsPresent": systemVcHardwareCFMsPresent,
       "systemVcHardwareFanTraysPresent": systemVcHardwareFanTraysPresent,
       "alcatelIND1SystemMIBConformance": alcatelIND1SystemMIBConformance,
       "alcatelIND1SystemMIBGroups": alcatelIND1SystemMIBGroups,
       "systemMicrocodeGroup": systemMicrocodeGroup,
       "systemBootParamsGroup": systemBootParamsGroup,
       "systemHardwareGroup": systemHardwareGroup,
       "systemServicesGroup": systemServicesGroup,
       "systemFileSystemGroup": systemFileSystemGroup,
       "systemSwitchLoggingGroup": systemSwitchLoggingGroup,
       "systemDNSGroup": systemDNSGroup,
       "systemBlueToothServicesGroup": systemBlueToothServicesGroup,
       "systemFipsGroup": systemFipsGroup,
       "systemVcHardwareGroup": systemVcHardwareGroup,
       "systemSwlogGroup": systemSwlogGroup,
       "systemNotificationGroup": systemNotificationGroup,
       "alcatelIND1SystemMIBCompliances": alcatelIND1SystemMIBCompliances,
       "alcatelIND1SystemMIBCompliance": alcatelIND1SystemMIBCompliance,
       "alcatelIND1SystemMIBTrapObjects": alcatelIND1SystemMIBTrapObjects,
       "systemSwlogName": systemSwlogName,
       "alcatelIND1SystemMIBTraps": alcatelIND1SystemMIBTraps,
       "systemSwlogSizeTrap": systemSwlogSizeTrap}
)
