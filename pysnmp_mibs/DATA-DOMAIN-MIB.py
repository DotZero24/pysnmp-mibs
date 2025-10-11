# SNMP MIB module (DATA-DOMAIN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/datadomain/DATA-DOMAIN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:54:58 2025
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

(ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

dataDomainMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 19746)
)
if mibBuilder.loadTexts:
    dataDomainMib.setRevisions(
        ("2015-10-29 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EnclosureID(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class Temperature(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"


class Minutes(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"


class Percentage(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class PercentageStr(TextualConvention, OctetString):
    status = "current"
    displayHint = "20a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )



class KBytesPerSecond(TextualConvention, Counter32):
    status = "current"
    displayHint = "d"


class OpsPerSecond(TextualConvention, Counter32):
    status = "current"
    displayHint = "d"


class ErrorCount(TextualConvention, Counter32):
    status = "current"
    displayHint = "d"


class DDMibTableIndexTC(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class DDMibTableString32TC(TextualConvention, OctetString):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class DDMibTableString64TC(TextualConvention, OctetString):
    status = "current"
    displayHint = "64a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class DDMibTableString128TC(TextualConvention, OctetString):
    status = "current"
    displayHint = "128a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )



class DDMibTableString256TC(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class DDMibTableString512TC(TextualConvention, OctetString):
    status = "current"
    displayHint = "512a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )



class DDMibTableString1024TC(TextualConvention, OctetString):
    status = "current"
    displayHint = "1024a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )



class DDMibString96TC(TextualConvention, OctetString):
    status = "current"
    displayHint = "96a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 96),
    )



class DDMibTableSizeGibTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "20a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )



class DDMibTableSizeMiBTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class DDMibDateTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "16a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class DDMibMemorySizeTC(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"


class DDMibTimeStampTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "64a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class DDMibVersionTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "64a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class DDMibTableEnabledTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )



class DDMibInteger32TC(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"


class DDMibCompressionFactorTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "20a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )



class DDMibAlertSeverityTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "64a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class DDMibTrafficBytesTC(TextualConvention, Counter64):
    status = "current"
    displayHint = "d"


class DDMibStatusTC(TextualConvention, Integer32):
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



class PowerModuleIndexTC(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class PowerModuleDescriptionTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "64a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class PowerModuleStatusTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              99)
        )
    )
    namedValues = NamedValues(
        *(("absent", 0),
          ("ok", 1),
          ("failed", 2),
          ("faulty", 3),
          ("acnone", 4),
          ("unknown", 99))
    )



class TempSensorIndexTC(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class TempSensorDescriptionTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "64a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class TempSensorStatusTC(TextualConvention, Integer32):
    status = "current"
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
        *(("failed", 0),
          ("ok", 1),
          ("notfound", 2),
          ("overheatWarning", 3),
          ("overheatCritical", 4))
    )



class FanIndexTC(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class FanDescriptionTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "64a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class FanLevelTC(TextualConvention, Integer32):
    status = "current"
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
        *(("unknown", 0),
          ("low", 1),
          ("medium", 2),
          ("high", 3))
    )



class FanStatusTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notfound", 0),
          ("ok", 1),
          ("fail", 2))
    )



class NvramIndexTC(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class NvramMemorySizeTC(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"


class NvramHCPropertyBytesTC(TextualConvention, Counter64):
    status = "current"
    displayHint = "d"


class NvramWindowSizeTC(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"


class NvramBatteryIndexTC(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class NvramBatteryStatusTC(TextualConvention, Integer32):
    status = "current"
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
        *(("ok", 0),
          ("disabled", 1),
          ("discharged", 2),
          ("softdisabled", 3))
    )



class DiskIndexTC(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class DiskModelTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "64a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class DiskFirmwareVersionTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "64a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class DiskSerialNumberTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "64a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class DiskCapacityTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "20a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )



class DiskStateTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("unknown", 2),
          ("absent", 3),
          ("failed", 4),
          ("spare", 5),
          ("available", 6))
    )



class DiskPackTC(TextualConvention, Integer32):
    status = "current"
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
        *(("notapplicable", 0),
          ("pack1", 1),
          ("pack2", 2),
          ("pack3", 3),
          ("pack4", 4))
    )



class DiskSectorsPerSecondTC(TextualConvention, Counter32):
    status = "current"
    displayHint = "d"


class FileSystemStatusTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("running", 3),
          ("unknown", 4),
          ("error", 5),
          ("cleaning", 6))
    )



class FileSystemResourceIndexTC(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class FileSystemResourceNameTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "64a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class FileSystemSpaceUnitTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "20a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )



class FileSystemCompressionSizeTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "20a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )



class FileSystemCompressionFactorTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "20a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )



class FileSystemCompressionPeriodTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "20a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )



class DateTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "16a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class FileSystemOptionsIndexTC(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class FileSystemOptionsNameTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "128a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )



class FileSystemOptionsValueTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "128a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )



class FileSystemCleanIndexTC(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class FileSystemCleanStatusTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "128a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )



class FileSystemCleanScheduleTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "128a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )



class FileSystemCleanThrottleTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "128a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )



class AlertIndexTC(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class AlertTimestampTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "64a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class AlertDescriptionTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class SystemStatsIndexTC(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class RaidDiskStateTC(TextualConvention, Integer32):
    status = "current"
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("inuse", 1),
          ("notinuse", 2),
          ("spare", 3),
          ("absent", 4),
          ("failed", 5),
          ("invalid", 6),
          ("foreign", 7),
          ("known", 8),
          ("available", 9),
          ("unknown", 99))
    )



class ReplicationStateTC(TextualConvention, Integer32):
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
        *(("initializing", 1),
          ("normal", 2),
          ("recovering", 3),
          ("uninitialized", 4))
    )



class ReplicationStatusTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("disconnected", 2),
          ("migrating", 3),
          ("suspended", 4),
          ("neverConnected", 5),
          ("idle", 6))
    )



class ReplicationConnectTimeTC(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"


class ReplicationPathTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "254a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )



class ReplicationTrafficTC(TextualConvention, Counter64):
    status = "current"
    displayHint = "d"


class ReplicationThrottleTC(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"


class ReplicationSyncedTimeTC(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"


class ReplicationContextTC(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class ReplicationConfigIndexTC(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class ReplicationConfigContextIdTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class ReplicationConfigSourceTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class ReplicationConfigDestTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class ReplicationConfigConnHostTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class ReplicationConfigConnPortTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class ReplicationConfigLowBWOptimTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )



class ReplicationConfigEnabledTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )



class NfsStatusTC(TextualConvention, Integer32):
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



class NfsClientIndexTC(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class NfsClientPathTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "1024a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )



class NfsClientClientsTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "1024a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )



class NfsClientOptionsTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "254a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )



class NfsStatsIndexTC(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class NfsStatsExportPointTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "254a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )



class NfsStatsFilesystemTypeTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class NfsStatsCacheEntryTC(TextualConvention, Counter32):
    status = "current"
    displayHint = "d"


class NfsStatsFileHandleLookupTC(TextualConvention, Counter32):
    status = "current"
    displayHint = "d"


class NfsStatsMaxCacheSizeTC(TextualConvention, Counter32):
    status = "current"
    displayHint = "d"


class NfsStatsCurrentOpenStreamsTC(TextualConvention, Counter32):
    status = "current"
    displayHint = "d"


class VtlAdminStateTC(TextualConvention, Integer32):
    status = "current"
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
        *(("unknown", 0),
          ("enabled", 1),
          ("disabled", 2),
          ("failed", 3))
    )



class VtlProcessStateTC(TextualConvention, Integer32):
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("stopped", 1),
          ("starting", 2),
          ("running", 3),
          ("timingout", 4),
          ("stopping", 5),
          ("stuck", 6))
    )



class VtlLibraryIndexTC(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )



class VtlLibraryNameTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "64a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class VtlLibraryVendorTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "64a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class VtlLibraryModelTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "64a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class VtlLibraryRevisionTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "64a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class VtlLibrarySerialTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "64a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class VtlLibraryTotalDrivesTC(TextualConvention, Counter32):
    status = "current"
    displayHint = "d"


class VtlLibraryTotalSlotsTC(TextualConvention, Counter32):
    status = "current"
    displayHint = "d"


class VtlLibraryTotalCapsTC(TextualConvention, Counter32):
    status = "current"
    displayHint = "d"


class VtlLibraryStatusTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("online", 1),
          ("offline", 2))
    )



class VtlDriveIndexTC(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )



class VtlDriveNameTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "64a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class VtlDriveVendorTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "64a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class VtlDriveModelTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "64a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class VtlDriveRevisionTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "64a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class VtlDriveSerialTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "64a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class VtlDriveStatusTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("online", 1),
          ("offline", 2))
    )



class VtlDriveTapeVolumeTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "64a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class VtlPortIndexTC(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )



class VtlPortNameTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class VtlPortIDTC(TextualConvention, Counter32):
    status = "current"
    displayHint = "d"


class VtlPortModelTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class VtlPortFirmwareTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class VtlPortWWNNTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "64a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class VtlPortWWPNTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "64a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class VtlPortConnectionTypeTC(TextualConvention, Integer32):
    status = "current"
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
        *(("nPORT", 0),
          ("loop", 1),
          ("pointToPoint", 2),
          ("fabricLoop", 3),
          ("unknown", 4))
    )



class VtlPortSpeedTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("zeroGBPS", 0),
          ("oneGBPS", 1),
          ("twoGBPS", 2),
          ("fourGBPS", 3),
          ("eightGBPS", 4),
          ("unknown", 6))
    )



class VtlPortEnabledTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("unknown", 2))
    )



class VtlPortStatusTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offline", 0),
          ("online", 1),
          ("unknown", 2))
    )



class VtlTapeIndexTC(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250000),
    )



class VtlTapeBarCodeTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "64a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class VtlTapePoolTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class VtlTapeLocationTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class VtlTapeStateTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class VtlTapeSizeTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class VtlTapeUsedTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class VtlTapeCompTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class VtlTapeModTimeTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class VtlStatsIndexTC(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class VtlStatsPortTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class VtlStatsConrolCommandsTC(TextualConvention, Counter64):
    status = "current"
    displayHint = "d"


class VtlStatsWriteCommandsTC(TextualConvention, Counter64):
    status = "current"
    displayHint = "d"


class VtlStatsReadCommandsTC(TextualConvention, Counter64):
    status = "current"
    displayHint = "d"


class VtlStatsInTC(TextualConvention, Counter64):
    status = "current"
    displayHint = "d"


class VtlStatsOutTC(TextualConvention, Counter64):
    status = "current"
    displayHint = "d"


class VtlStatsLinkFailuresTC(TextualConvention, Counter64):
    status = "current"
    displayHint = "d"


class VtlStatsLIPCountTC(TextualConvention, Counter64):
    status = "current"
    displayHint = "d"


class VtlStatsSyncLossesTC(TextualConvention, Counter64):
    status = "current"
    displayHint = "d"


class VtlStatsSignalLossesTC(TextualConvention, Counter64):
    status = "current"
    displayHint = "d"


class VtlStatsPrimSeqProtoErrorsTC(TextualConvention, Counter64):
    status = "current"
    displayHint = "d"


class VtlStatsInvalidTxWordsTC(TextualConvention, Counter64):
    status = "current"
    displayHint = "d"


class VtlStatsInvalidCRCsTC(TextualConvention, Counter64):
    status = "current"
    displayHint = "d"


class CifsStatusTC(TextualConvention, Integer32):
    status = "current"
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
        *(("enabled", 1),
          ("enabledRunning", 2),
          ("enabledNotRunning", 3),
          ("enabledWindbindNotRun", 4),
          ("disabled", 5))
    )



class CifsConfigModeTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "64a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class CifsConfigWINSServerTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "1024a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )



class CifsConfigNetBIOSHostnameTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class CifsConfigDomainControllerTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "1024a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )



class CifsConfigDNSTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "1024a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )



class CifsConfigGroupNameTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class CifsConfigMaxConnectionTC(TextualConvention, Counter32):
    status = "current"
    displayHint = "d"


class CifsConfigMaxOpenFilesPerConnectionTC(TextualConvention, Counter32):
    status = "current"
    displayHint = "d"


class CifsShareIndexTC(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class CifsShareNameTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class CifsSharePathTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "1024a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )



class CifsShareMaxConnectionTC(TextualConvention, Counter32):
    status = "current"
    displayHint = "d"


class CifsShareClientsTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "1024a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )



class CifsShareBrowsingTC(TextualConvention, Integer32):
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



class CifsShareWriteableTC(TextualConvention, Integer32):
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



class CifsShareUserTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "1024a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )



class CifsShareCommentTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class CifsStatsSummaryIndexTC(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class CifsStatsDetailsIndexTC(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class CifsOptionsIndexTC(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class CifsOptionsNameTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "128a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )



class CifsOptionsValueTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "128a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )



class DDboostStatsIndexTC(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class DDboostStatusTC(TextualConvention, Integer32):
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



class DDboostUserTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "1024a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )



class SystemSerialNumberTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "128a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )



class SystemTimeZoneNameTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "64a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class SystemNotesTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "1024a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )



class FileSystemArchiveUnitStateTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("new", 1),
          ("target", 2),
          ("sealed", 3))
    )



class FileSystemArchiveUnitStatusTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("disabled", 2))
    )



class MtreeListStatusTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("deleted", 1),
          ("readOnly", 2),
          ("readWrite", 3),
          ("replicationDestination", 4),
          ("retentionLockEnabled", 5),
          ("retentionLockDisabled", 6))
    )



class MtreeRetentionLockStatusTC(TextualConvention, Integer32):
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



class TenantUnitMgmtUserListUserRoleTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tenantAdmin", 1),
          ("tenantUser", 2))
    )



class TenantUnitMgmtGroupTypeTC(TextualConvention, Integer32):
    status = "current"
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
          ("unknown", 1),
          ("local", 2),
          ("ad", 3),
          ("nis", 4),
          ("ldap", 5))
    )



class SmtStatusTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )



class TenantUnitSecurityModeTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("strict", 1),
          ("default", 2))
    )



class DDStatusTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )



class DdboostAccessClientsEncryStrengthTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("medium", 2),
          ("high", 3))
    )



class DdboostAccessClientsAuthModeTC(TextualConvention, Integer32):
    status = "current"
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
          ("oneWay", 1),
          ("twoWay", 2),
          ("anonymous", 3))
    )



# MIB Managed Objects in the order of their OIDs

_DataDomainMibConformance_ObjectIdentity = ObjectIdentity
dataDomainMibConformance = _DataDomainMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 0)
)
_DataDomainMibCompliances_ObjectIdentity = ObjectIdentity
dataDomainMibCompliances = _DataDomainMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 0, 1)
)
_DataDomainMibGroups_ObjectIdentity = ObjectIdentity
dataDomainMibGroups = _DataDomainMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 0, 2)
)
_DataDomainMibObjects_ObjectIdentity = ObjectIdentity
dataDomainMibObjects = _DataDomainMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1)
)
_Environmentals_ObjectIdentity = ObjectIdentity
environmentals = _Environmentals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1)
)
_Power_ObjectIdentity = ObjectIdentity
power = _Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 1)
)
_PowerModules_ObjectIdentity = ObjectIdentity
powerModules = _PowerModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 1, 1)
)
_PowerModuleTable_Object = MibTable
powerModuleTable = _PowerModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    powerModuleTable.setStatus("current")
_PowerModuleEntry_Object = MibTableRow
powerModuleEntry = _PowerModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 1, 1, 1, 1)
)
powerModuleEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "powerEnclosureID"),
    (0, "DATA-DOMAIN-MIB", "powerModuleIndex"),
)
if mibBuilder.loadTexts:
    powerModuleEntry.setStatus("current")
_PowerEnclosureID_Type = EnclosureID
_PowerEnclosureID_Object = MibTableColumn
powerEnclosureID = _PowerEnclosureID_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 1, 1, 1, 1, 1),
    _PowerEnclosureID_Type()
)
powerEnclosureID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    powerEnclosureID.setStatus("current")
_PowerModuleIndex_Type = PowerModuleIndexTC
_PowerModuleIndex_Object = MibTableColumn
powerModuleIndex = _PowerModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 1, 1, 1, 1, 2),
    _PowerModuleIndex_Type()
)
powerModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    powerModuleIndex.setStatus("current")
_PowerModuleDescription_Type = PowerModuleDescriptionTC
_PowerModuleDescription_Object = MibTableColumn
powerModuleDescription = _PowerModuleDescription_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 1, 1, 1, 1, 3),
    _PowerModuleDescription_Type()
)
powerModuleDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerModuleDescription.setStatus("current")
_PowerModuleStatus_Type = PowerModuleStatusTC
_PowerModuleStatus_Object = MibTableColumn
powerModuleStatus = _PowerModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 1, 1, 1, 1, 4),
    _PowerModuleStatus_Type()
)
powerModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerModuleStatus.setStatus("current")
_Temperatures_ObjectIdentity = ObjectIdentity
temperatures = _Temperatures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 2)
)
_TemperatureSensors_ObjectIdentity = ObjectIdentity
temperatureSensors = _TemperatureSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1)
)
_TemperatureSensorTable_Object = MibTable
temperatureSensorTable = _TemperatureSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    temperatureSensorTable.setStatus("current")
_TemperatureSensorEntry_Object = MibTableRow
temperatureSensorEntry = _TemperatureSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1, 1, 1)
)
temperatureSensorEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "tempEnclosureID"),
    (0, "DATA-DOMAIN-MIB", "tempSensorIndex"),
)
if mibBuilder.loadTexts:
    temperatureSensorEntry.setStatus("current")
_TempEnclosureID_Type = EnclosureID
_TempEnclosureID_Object = MibTableColumn
tempEnclosureID = _TempEnclosureID_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1, 1, 1, 1),
    _TempEnclosureID_Type()
)
tempEnclosureID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tempEnclosureID.setStatus("current")
_TempSensorIndex_Type = TempSensorIndexTC
_TempSensorIndex_Object = MibTableColumn
tempSensorIndex = _TempSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1, 1, 1, 2),
    _TempSensorIndex_Type()
)
tempSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tempSensorIndex.setStatus("current")
_TempSensorTrapIndex_Type = TempSensorIndexTC
_TempSensorTrapIndex_Object = MibTableColumn
tempSensorTrapIndex = _TempSensorTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1, 1, 1, 3),
    _TempSensorTrapIndex_Type()
)
tempSensorTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorTrapIndex.setStatus("current")
_TempSensorDescription_Type = TempSensorDescriptionTC
_TempSensorDescription_Object = MibTableColumn
tempSensorDescription = _TempSensorDescription_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1, 1, 1, 4),
    _TempSensorDescription_Type()
)
tempSensorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorDescription.setStatus("current")
_TempSensorCurrentValue_Type = Temperature
_TempSensorCurrentValue_Object = MibTableColumn
tempSensorCurrentValue = _TempSensorCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1, 1, 1, 5),
    _TempSensorCurrentValue_Type()
)
tempSensorCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorCurrentValue.setStatus("current")
_TempSensorStatus_Type = TempSensorStatusTC
_TempSensorStatus_Object = MibTableColumn
tempSensorStatus = _TempSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1, 1, 1, 6),
    _TempSensorStatus_Type()
)
tempSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorStatus.setStatus("current")
_Fans_ObjectIdentity = ObjectIdentity
fans = _Fans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 3)
)
_FanProperties_ObjectIdentity = ObjectIdentity
fanProperties = _FanProperties_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1)
)
_FanPropertiesTable_Object = MibTable
fanPropertiesTable = _FanPropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    fanPropertiesTable.setStatus("current")
_FanPropertiesEntry_Object = MibTableRow
fanPropertiesEntry = _FanPropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1, 1, 1)
)
fanPropertiesEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "fanEnclosureID"),
    (0, "DATA-DOMAIN-MIB", "fanIndex"),
)
if mibBuilder.loadTexts:
    fanPropertiesEntry.setStatus("current")
_FanEnclosureID_Type = EnclosureID
_FanEnclosureID_Object = MibTableColumn
fanEnclosureID = _FanEnclosureID_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1, 1, 1, 1),
    _FanEnclosureID_Type()
)
fanEnclosureID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fanEnclosureID.setStatus("current")
_FanIndex_Type = FanIndexTC
_FanIndex_Object = MibTableColumn
fanIndex = _FanIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1, 1, 1, 2),
    _FanIndex_Type()
)
fanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fanIndex.setStatus("current")
_FanTrapIndex_Type = FanIndexTC
_FanTrapIndex_Object = MibTableColumn
fanTrapIndex = _FanTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1, 1, 1, 3),
    _FanTrapIndex_Type()
)
fanTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanTrapIndex.setStatus("current")
_FanDescription_Type = FanDescriptionTC
_FanDescription_Object = MibTableColumn
fanDescription = _FanDescription_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1, 1, 1, 4),
    _FanDescription_Type()
)
fanDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanDescription.setStatus("current")
_FanLevel_Type = FanLevelTC
_FanLevel_Object = MibTableColumn
fanLevel = _FanLevel_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1, 1, 1, 5),
    _FanLevel_Type()
)
fanLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanLevel.setStatus("current")
_FanStatus_Type = FanStatusTC
_FanStatus_Object = MibTableColumn
fanStatus = _FanStatus_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1, 1, 1, 6),
    _FanStatus_Type()
)
fanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanStatus.setStatus("current")
_Nvram_ObjectIdentity = ObjectIdentity
nvram = _Nvram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 2)
)
_NvramProperties_ObjectIdentity = ObjectIdentity
nvramProperties = _NvramProperties_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 2, 1)
)
_NvramPropertiesTable_Object = MibTable
nvramPropertiesTable = _NvramPropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    nvramPropertiesTable.setStatus("current")
_NvramPropertiesEntry_Object = MibTableRow
nvramPropertiesEntry = _NvramPropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 2, 1, 1, 1)
)
nvramPropertiesEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "nvramPropertiesIndex"),
)
if mibBuilder.loadTexts:
    nvramPropertiesEntry.setStatus("current")
_NvramPropertiesIndex_Type = NvramIndexTC
_NvramPropertiesIndex_Object = MibTableColumn
nvramPropertiesIndex = _NvramPropertiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 2, 1, 1, 1, 1),
    _NvramPropertiesIndex_Type()
)
nvramPropertiesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nvramPropertiesIndex.setStatus("current")
_NvramMemorySize_Type = NvramMemorySizeTC
_NvramMemorySize_Object = MibTableColumn
nvramMemorySize = _NvramMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 2, 1, 1, 1, 2),
    _NvramMemorySize_Type()
)
nvramMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvramMemorySize.setStatus("current")
_NvramWindowSize_Type = NvramWindowSizeTC
_NvramWindowSize_Object = MibTableColumn
nvramWindowSize = _NvramWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 2, 1, 1, 1, 3),
    _NvramWindowSize_Type()
)
nvramWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvramWindowSize.setStatus("current")
_NvramHCMemorySize_Type = NvramHCPropertyBytesTC
_NvramHCMemorySize_Object = MibTableColumn
nvramHCMemorySize = _NvramHCMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 2, 1, 1, 1, 4),
    _NvramHCMemorySize_Type()
)
nvramHCMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvramHCMemorySize.setStatus("current")
_NvramStats_ObjectIdentity = ObjectIdentity
nvramStats = _NvramStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 2, 2)
)
_NvramStatsTable_Object = MibTable
nvramStatsTable = _NvramStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    nvramStatsTable.setStatus("current")
_NvramStatsEntry_Object = MibTableRow
nvramStatsEntry = _NvramStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 2, 2, 1, 1)
)
nvramStatsEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "nvramStatsIndex"),
)
if mibBuilder.loadTexts:
    nvramStatsEntry.setStatus("current")
_NvramStatsIndex_Type = NvramIndexTC
_NvramStatsIndex_Object = MibTableColumn
nvramStatsIndex = _NvramStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 2, 2, 1, 1, 1),
    _NvramStatsIndex_Type()
)
nvramStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nvramStatsIndex.setStatus("current")
_NvramPCIErrorCount_Type = ErrorCount
_NvramPCIErrorCount_Object = MibTableColumn
nvramPCIErrorCount = _NvramPCIErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 2, 2, 1, 1, 2),
    _NvramPCIErrorCount_Type()
)
nvramPCIErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvramPCIErrorCount.setStatus("current")
_NvramMemoryErrorCount_Type = ErrorCount
_NvramMemoryErrorCount_Object = MibTableColumn
nvramMemoryErrorCount = _NvramMemoryErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 2, 2, 1, 1, 3),
    _NvramMemoryErrorCount_Type()
)
nvramMemoryErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvramMemoryErrorCount.setStatus("current")
_NvramBatteries_ObjectIdentity = ObjectIdentity
nvramBatteries = _NvramBatteries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 2, 3)
)
_NvramBatteryTable_Object = MibTable
nvramBatteryTable = _NvramBatteryTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    nvramBatteryTable.setStatus("current")
_NvramBatteryEntry_Object = MibTableRow
nvramBatteryEntry = _NvramBatteryEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 2, 3, 1, 1)
)
nvramBatteryEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "nvramBatteriesIndex"),
    (0, "DATA-DOMAIN-MIB", "nvramBatteryIndex"),
)
if mibBuilder.loadTexts:
    nvramBatteryEntry.setStatus("current")
_NvramBatteriesIndex_Type = NvramIndexTC
_NvramBatteriesIndex_Object = MibTableColumn
nvramBatteriesIndex = _NvramBatteriesIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 2, 3, 1, 1, 1),
    _NvramBatteriesIndex_Type()
)
nvramBatteriesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nvramBatteriesIndex.setStatus("current")
_NvramBatteryIndex_Type = NvramBatteryIndexTC
_NvramBatteryIndex_Object = MibTableColumn
nvramBatteryIndex = _NvramBatteryIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 2, 3, 1, 1, 2),
    _NvramBatteryIndex_Type()
)
nvramBatteryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nvramBatteryIndex.setStatus("current")
_NvramBatteryStatus_Type = NvramBatteryStatusTC
_NvramBatteryStatus_Object = MibTableColumn
nvramBatteryStatus = _NvramBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 2, 3, 1, 1, 3),
    _NvramBatteryStatus_Type()
)
nvramBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvramBatteryStatus.setStatus("current")
_NvramBatteryCharge_Type = Percentage
_NvramBatteryCharge_Object = MibTableColumn
nvramBatteryCharge = _NvramBatteryCharge_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 2, 3, 1, 1, 4),
    _NvramBatteryCharge_Type()
)
nvramBatteryCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvramBatteryCharge.setStatus("current")
_FileSystem_ObjectIdentity = ObjectIdentity
fileSystem = _FileSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3)
)
_FileSystemProperties_ObjectIdentity = ObjectIdentity
fileSystemProperties = _FileSystemProperties_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 1)
)
_FileSystemStatus_Type = FileSystemStatusTC
_FileSystemStatus_Object = MibScalar
fileSystemStatus = _FileSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 1, 1),
    _FileSystemStatus_Type()
)
fileSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemStatus.setStatus("current")
_FileSystemVirtualSpace_Type = FileSystemSpaceUnitTC
_FileSystemVirtualSpace_Object = MibScalar
fileSystemVirtualSpace = _FileSystemVirtualSpace_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 1, 2),
    _FileSystemVirtualSpace_Type()
)
fileSystemVirtualSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemVirtualSpace.setStatus("current")
_FileSystemUpTime_Type = DDMibTimeStampTC
_FileSystemUpTime_Object = MibScalar
fileSystemUpTime = _FileSystemUpTime_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 1, 3),
    _FileSystemUpTime_Type()
)
fileSystemUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemUpTime.setStatus("current")
_FileSystemStatusMessage_Type = DDMibTableString256TC
_FileSystemStatusMessage_Object = MibScalar
fileSystemStatusMessage = _FileSystemStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 1, 4),
    _FileSystemStatusMessage_Type()
)
fileSystemStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemStatusMessage.setStatus("current")
_FileSystemSpace_ObjectIdentity = ObjectIdentity
fileSystemSpace = _FileSystemSpace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 2)
)
_FileSystemSpaceTable_Object = MibTable
fileSystemSpaceTable = _FileSystemSpaceTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    fileSystemSpaceTable.setStatus("current")
_FileSystemSpaceEntry_Object = MibTableRow
fileSystemSpaceEntry = _FileSystemSpaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1)
)
fileSystemSpaceEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "fileSystemResourceIndex"),
)
if mibBuilder.loadTexts:
    fileSystemSpaceEntry.setStatus("current")
_FileSystemResourceIndex_Type = FileSystemResourceIndexTC
_FileSystemResourceIndex_Object = MibTableColumn
fileSystemResourceIndex = _FileSystemResourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1, 1),
    _FileSystemResourceIndex_Type()
)
fileSystemResourceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fileSystemResourceIndex.setStatus("current")
_FileSystemResourceTrapIndex_Type = FileSystemResourceIndexTC
_FileSystemResourceTrapIndex_Object = MibTableColumn
fileSystemResourceTrapIndex = _FileSystemResourceTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1, 2),
    _FileSystemResourceTrapIndex_Type()
)
fileSystemResourceTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemResourceTrapIndex.setStatus("current")
_FileSystemResourceName_Type = FileSystemResourceNameTC
_FileSystemResourceName_Object = MibTableColumn
fileSystemResourceName = _FileSystemResourceName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1, 3),
    _FileSystemResourceName_Type()
)
fileSystemResourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemResourceName.setStatus("current")
_FileSystemSpaceSize_Type = FileSystemSpaceUnitTC
_FileSystemSpaceSize_Object = MibTableColumn
fileSystemSpaceSize = _FileSystemSpaceSize_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1, 4),
    _FileSystemSpaceSize_Type()
)
fileSystemSpaceSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemSpaceSize.setStatus("current")
_FileSystemSpaceUsed_Type = FileSystemSpaceUnitTC
_FileSystemSpaceUsed_Object = MibTableColumn
fileSystemSpaceUsed = _FileSystemSpaceUsed_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1, 5),
    _FileSystemSpaceUsed_Type()
)
fileSystemSpaceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemSpaceUsed.setStatus("current")
_FileSystemSpaceAvail_Type = FileSystemSpaceUnitTC
_FileSystemSpaceAvail_Object = MibTableColumn
fileSystemSpaceAvail = _FileSystemSpaceAvail_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1, 6),
    _FileSystemSpaceAvail_Type()
)
fileSystemSpaceAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemSpaceAvail.setStatus("current")
_FileSystemPercentUsed_Type = Percentage
_FileSystemPercentUsed_Object = MibTableColumn
fileSystemPercentUsed = _FileSystemPercentUsed_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1, 7),
    _FileSystemPercentUsed_Type()
)
fileSystemPercentUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemPercentUsed.setStatus("current")
_FileSystemSpaceCleanable_Type = FileSystemSpaceUnitTC
_FileSystemSpaceCleanable_Object = MibTableColumn
fileSystemSpaceCleanable = _FileSystemSpaceCleanable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1, 8),
    _FileSystemSpaceCleanable_Type()
)
fileSystemSpaceCleanable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemSpaceCleanable.setStatus("current")
_FileSystemResourceTier_Type = DDMibTableString128TC
_FileSystemResourceTier_Object = MibTableColumn
fileSystemResourceTier = _FileSystemResourceTier_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1, 9),
    _FileSystemResourceTier_Type()
)
fileSystemResourceTier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemResourceTier.setStatus("current")
_FileSystemCompression_ObjectIdentity = ObjectIdentity
fileSystemCompression = _FileSystemCompression_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 3)
)
_FileSystemCompressionTable_Object = MibTable
fileSystemCompressionTable = _FileSystemCompressionTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    fileSystemCompressionTable.setStatus("current")
_FileSystemCompressionEntry_Object = MibTableRow
fileSystemCompressionEntry = _FileSystemCompressionEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 3, 1, 1)
)
fileSystemCompressionEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "fileSystemCompressionIndex"),
)
if mibBuilder.loadTexts:
    fileSystemCompressionEntry.setStatus("current")
_FileSystemCompressionIndex_Type = FileSystemResourceIndexTC
_FileSystemCompressionIndex_Object = MibTableColumn
fileSystemCompressionIndex = _FileSystemCompressionIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 3, 1, 1, 1),
    _FileSystemCompressionIndex_Type()
)
fileSystemCompressionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fileSystemCompressionIndex.setStatus("current")
_FileSystemCompressionPeriod_Type = FileSystemCompressionPeriodTC
_FileSystemCompressionPeriod_Object = MibTableColumn
fileSystemCompressionPeriod = _FileSystemCompressionPeriod_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 3, 1, 1, 2),
    _FileSystemCompressionPeriod_Type()
)
fileSystemCompressionPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemCompressionPeriod.setStatus("current")
_FileSystemCompressionStartTime_Type = DateTC
_FileSystemCompressionStartTime_Object = MibTableColumn
fileSystemCompressionStartTime = _FileSystemCompressionStartTime_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 3, 1, 1, 3),
    _FileSystemCompressionStartTime_Type()
)
fileSystemCompressionStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemCompressionStartTime.setStatus("current")
_FileSystemCompressionEndTime_Type = DateTC
_FileSystemCompressionEndTime_Object = MibTableColumn
fileSystemCompressionEndTime = _FileSystemCompressionEndTime_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 3, 1, 1, 4),
    _FileSystemCompressionEndTime_Type()
)
fileSystemCompressionEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemCompressionEndTime.setStatus("current")
_FileSystemPreCompressionSize_Type = FileSystemCompressionSizeTC
_FileSystemPreCompressionSize_Object = MibTableColumn
fileSystemPreCompressionSize = _FileSystemPreCompressionSize_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 3, 1, 1, 5),
    _FileSystemPreCompressionSize_Type()
)
fileSystemPreCompressionSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemPreCompressionSize.setStatus("current")
_FileSystemPostCompressionSize_Type = FileSystemCompressionSizeTC
_FileSystemPostCompressionSize_Object = MibTableColumn
fileSystemPostCompressionSize = _FileSystemPostCompressionSize_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 3, 1, 1, 6),
    _FileSystemPostCompressionSize_Type()
)
fileSystemPostCompressionSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemPostCompressionSize.setStatus("current")
_FileSystemGlobalCompressionFactor_Type = FileSystemCompressionFactorTC
_FileSystemGlobalCompressionFactor_Object = MibTableColumn
fileSystemGlobalCompressionFactor = _FileSystemGlobalCompressionFactor_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 3, 1, 1, 7),
    _FileSystemGlobalCompressionFactor_Type()
)
fileSystemGlobalCompressionFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemGlobalCompressionFactor.setStatus("current")
_FileSystemLocalCompressionFactor_Type = FileSystemCompressionFactorTC
_FileSystemLocalCompressionFactor_Object = MibTableColumn
fileSystemLocalCompressionFactor = _FileSystemLocalCompressionFactor_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 3, 1, 1, 8),
    _FileSystemLocalCompressionFactor_Type()
)
fileSystemLocalCompressionFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemLocalCompressionFactor.setStatus("current")
_FileSystemTotalCompressionFactor_Type = FileSystemCompressionFactorTC
_FileSystemTotalCompressionFactor_Object = MibTableColumn
fileSystemTotalCompressionFactor = _FileSystemTotalCompressionFactor_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 3, 1, 1, 9),
    _FileSystemTotalCompressionFactor_Type()
)
fileSystemTotalCompressionFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemTotalCompressionFactor.setStatus("current")
_FileSystemReductionPercent_Type = Percentage
_FileSystemReductionPercent_Object = MibTableColumn
fileSystemReductionPercent = _FileSystemReductionPercent_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 3, 1, 1, 10),
    _FileSystemReductionPercent_Type()
)
fileSystemReductionPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemReductionPercent.setStatus("deprecated")
_FileSystemReductionPercent1_Type = PercentageStr
_FileSystemReductionPercent1_Object = MibTableColumn
fileSystemReductionPercent1 = _FileSystemReductionPercent1_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 3, 1, 1, 11),
    _FileSystemReductionPercent1_Type()
)
fileSystemReductionPercent1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemReductionPercent1.setStatus("current")
_FileSystemOptions_ObjectIdentity = ObjectIdentity
fileSystemOptions = _FileSystemOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 4)
)
_FileSystemOptionsTable_Object = MibTable
fileSystemOptionsTable = _FileSystemOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    fileSystemOptionsTable.setStatus("current")
_FileSystemOptionsEntry_Object = MibTableRow
fileSystemOptionsEntry = _FileSystemOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 4, 1, 1)
)
fileSystemOptionsEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "fileSystemOptionsIndex"),
)
if mibBuilder.loadTexts:
    fileSystemOptionsEntry.setStatus("current")
_FileSystemOptionsIndex_Type = FileSystemOptionsIndexTC
_FileSystemOptionsIndex_Object = MibTableColumn
fileSystemOptionsIndex = _FileSystemOptionsIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 4, 1, 1, 1),
    _FileSystemOptionsIndex_Type()
)
fileSystemOptionsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fileSystemOptionsIndex.setStatus("current")
_FileSystemOptionsName_Type = FileSystemOptionsNameTC
_FileSystemOptionsName_Object = MibTableColumn
fileSystemOptionsName = _FileSystemOptionsName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 4, 1, 1, 2),
    _FileSystemOptionsName_Type()
)
fileSystemOptionsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemOptionsName.setStatus("current")
_FileSystemOptionsValue_Type = FileSystemOptionsValueTC
_FileSystemOptionsValue_Object = MibTableColumn
fileSystemOptionsValue = _FileSystemOptionsValue_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 4, 1, 1, 3),
    _FileSystemOptionsValue_Type()
)
fileSystemOptionsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemOptionsValue.setStatus("current")
_FileSystemClean_ObjectIdentity = ObjectIdentity
fileSystemClean = _FileSystemClean_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 5)
)
_FileSystemCleanTable_Object = MibTable
fileSystemCleanTable = _FileSystemCleanTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 5, 1)
)
if mibBuilder.loadTexts:
    fileSystemCleanTable.setStatus("current")
_FileSystemCleanEntry_Object = MibTableRow
fileSystemCleanEntry = _FileSystemCleanEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 5, 1, 1)
)
fileSystemCleanEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "fileSystemCleanIndex"),
)
if mibBuilder.loadTexts:
    fileSystemCleanEntry.setStatus("current")
_FileSystemCleanIndex_Type = FileSystemCleanIndexTC
_FileSystemCleanIndex_Object = MibTableColumn
fileSystemCleanIndex = _FileSystemCleanIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 5, 1, 1, 1),
    _FileSystemCleanIndex_Type()
)
fileSystemCleanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fileSystemCleanIndex.setStatus("current")
_FileSystemCleanStatus_Type = FileSystemCleanStatusTC
_FileSystemCleanStatus_Object = MibTableColumn
fileSystemCleanStatus = _FileSystemCleanStatus_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 5, 1, 1, 2),
    _FileSystemCleanStatus_Type()
)
fileSystemCleanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemCleanStatus.setStatus("current")
_FileSystemCleanSchedule_Type = FileSystemCleanScheduleTC
_FileSystemCleanSchedule_Object = MibTableColumn
fileSystemCleanSchedule = _FileSystemCleanSchedule_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 5, 1, 1, 3),
    _FileSystemCleanSchedule_Type()
)
fileSystemCleanSchedule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemCleanSchedule.setStatus("current")
_FileSystemCleanThrottle_Type = FileSystemCleanThrottleTC
_FileSystemCleanThrottle_Object = MibTableColumn
fileSystemCleanThrottle = _FileSystemCleanThrottle_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 5, 1, 1, 4),
    _FileSystemCleanThrottle_Type()
)
fileSystemCleanThrottle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemCleanThrottle.setStatus("current")
_FileSystemArchiveUnit_ObjectIdentity = ObjectIdentity
fileSystemArchiveUnit = _FileSystemArchiveUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 6)
)
_FileSystemArchiveUnitTable_Object = MibTable
fileSystemArchiveUnitTable = _FileSystemArchiveUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 6, 1)
)
if mibBuilder.loadTexts:
    fileSystemArchiveUnitTable.setStatus("current")
_FileSystemArchiveUnitEntry_Object = MibTableRow
fileSystemArchiveUnitEntry = _FileSystemArchiveUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 6, 1, 1)
)
fileSystemArchiveUnitEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "fileSystemArchiveUnitIndex"),
)
if mibBuilder.loadTexts:
    fileSystemArchiveUnitEntry.setStatus("current")
_FileSystemArchiveUnitIndex_Type = DDMibTableIndexTC
_FileSystemArchiveUnitIndex_Object = MibTableColumn
fileSystemArchiveUnitIndex = _FileSystemArchiveUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 6, 1, 1, 1),
    _FileSystemArchiveUnitIndex_Type()
)
fileSystemArchiveUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fileSystemArchiveUnitIndex.setStatus("current")
_FileSystemArchiveUnitName_Type = DDMibTableString256TC
_FileSystemArchiveUnitName_Object = MibTableColumn
fileSystemArchiveUnitName = _FileSystemArchiveUnitName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 6, 1, 1, 2),
    _FileSystemArchiveUnitName_Type()
)
fileSystemArchiveUnitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemArchiveUnitName.setStatus("current")
_FileSystemArchiveUnitState_Type = FileSystemArchiveUnitStateTC
_FileSystemArchiveUnitState_Object = MibTableColumn
fileSystemArchiveUnitState = _FileSystemArchiveUnitState_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 6, 1, 1, 3),
    _FileSystemArchiveUnitState_Type()
)
fileSystemArchiveUnitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemArchiveUnitState.setStatus("current")
_FileSystemArchiveUnitStatus_Type = FileSystemArchiveUnitStatusTC
_FileSystemArchiveUnitStatus_Object = MibTableColumn
fileSystemArchiveUnitStatus = _FileSystemArchiveUnitStatus_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 6, 1, 1, 4),
    _FileSystemArchiveUnitStatus_Type()
)
fileSystemArchiveUnitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemArchiveUnitStatus.setStatus("current")
_FileSystemArchiveUnitStartTime_Type = DDMibTimeStampTC
_FileSystemArchiveUnitStartTime_Object = MibTableColumn
fileSystemArchiveUnitStartTime = _FileSystemArchiveUnitStartTime_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 6, 1, 1, 5),
    _FileSystemArchiveUnitStartTime_Type()
)
fileSystemArchiveUnitStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemArchiveUnitStartTime.setStatus("current")
_FileSystemArchiveUnitEndTime_Type = DDMibTimeStampTC
_FileSystemArchiveUnitEndTime_Object = MibTableColumn
fileSystemArchiveUnitEndTime = _FileSystemArchiveUnitEndTime_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 6, 1, 1, 6),
    _FileSystemArchiveUnitEndTime_Type()
)
fileSystemArchiveUnitEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemArchiveUnitEndTime.setStatus("current")
_FileSystemArchiveUnitSize_Type = DDMibTableSizeGibTC
_FileSystemArchiveUnitSize_Object = MibTableColumn
fileSystemArchiveUnitSize = _FileSystemArchiveUnitSize_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 6, 1, 1, 7),
    _FileSystemArchiveUnitSize_Type()
)
fileSystemArchiveUnitSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemArchiveUnitSize.setStatus("current")
_FileSystemArchiveUnitDiskGroups_Type = DDMibTableString1024TC
_FileSystemArchiveUnitDiskGroups_Object = MibTableColumn
fileSystemArchiveUnitDiskGroups = _FileSystemArchiveUnitDiskGroups_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 6, 1, 1, 8),
    _FileSystemArchiveUnitDiskGroups_Type()
)
fileSystemArchiveUnitDiskGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemArchiveUnitDiskGroups.setStatus("current")
_Alerts_ObjectIdentity = ObjectIdentity
alerts = _Alerts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 4)
)
_CurrentAlerts_ObjectIdentity = ObjectIdentity
currentAlerts = _CurrentAlerts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 4, 1)
)
_CurrentAlertTable_Object = MibTable
currentAlertTable = _CurrentAlertTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    currentAlertTable.setStatus("current")
_CurrentAlertEntry_Object = MibTableRow
currentAlertEntry = _CurrentAlertEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 4, 1, 1, 1)
)
currentAlertEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "currentAlertIndex"),
)
if mibBuilder.loadTexts:
    currentAlertEntry.setStatus("current")
_CurrentAlertIndex_Type = AlertIndexTC
_CurrentAlertIndex_Object = MibTableColumn
currentAlertIndex = _CurrentAlertIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 4, 1, 1, 1, 1),
    _CurrentAlertIndex_Type()
)
currentAlertIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    currentAlertIndex.setStatus("current")
_CurrentAlertTimestamp_Type = AlertTimestampTC
_CurrentAlertTimestamp_Object = MibTableColumn
currentAlertTimestamp = _CurrentAlertTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 4, 1, 1, 1, 2),
    _CurrentAlertTimestamp_Type()
)
currentAlertTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentAlertTimestamp.setStatus("current")
_CurrentAlertDescription_Type = AlertDescriptionTC
_CurrentAlertDescription_Object = MibTableColumn
currentAlertDescription = _CurrentAlertDescription_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 4, 1, 1, 1, 3),
    _CurrentAlertDescription_Type()
)
currentAlertDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentAlertDescription.setStatus("current")
_CurrentAlertSeverity_Type = DDMibAlertSeverityTC
_CurrentAlertSeverity_Object = MibTableColumn
currentAlertSeverity = _CurrentAlertSeverity_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 4, 1, 1, 1, 4),
    _CurrentAlertSeverity_Type()
)
currentAlertSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentAlertSeverity.setStatus("current")
_CurrentAlertID_Type = DDMibTableString32TC
_CurrentAlertID_Object = MibTableColumn
currentAlertID = _CurrentAlertID_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 4, 1, 1, 1, 5),
    _CurrentAlertID_Type()
)
currentAlertID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentAlertID.setStatus("current")
_AlertHistory_ObjectIdentity = ObjectIdentity
alertHistory = _AlertHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 4, 2)
)
_AlertHistoryTable_Object = MibTable
alertHistoryTable = _AlertHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    alertHistoryTable.setStatus("current")
_AlertHistoryEntry_Object = MibTableRow
alertHistoryEntry = _AlertHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 4, 2, 1, 1)
)
alertHistoryEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "alertHistoryIndex"),
)
if mibBuilder.loadTexts:
    alertHistoryEntry.setStatus("current")
_AlertHistoryIndex_Type = DDMibTableIndexTC
_AlertHistoryIndex_Object = MibTableColumn
alertHistoryIndex = _AlertHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 4, 2, 1, 1, 1),
    _AlertHistoryIndex_Type()
)
alertHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alertHistoryIndex.setStatus("current")
_AlertHistoryTimestamp_Type = DDMibTimeStampTC
_AlertHistoryTimestamp_Object = MibTableColumn
alertHistoryTimestamp = _AlertHistoryTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 4, 2, 1, 1, 2),
    _AlertHistoryTimestamp_Type()
)
alertHistoryTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertHistoryTimestamp.setStatus("current")
_AlertHistoryDescription_Type = DDMibTableString256TC
_AlertHistoryDescription_Object = MibTableColumn
alertHistoryDescription = _AlertHistoryDescription_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 4, 2, 1, 1, 3),
    _AlertHistoryDescription_Type()
)
alertHistoryDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertHistoryDescription.setStatus("current")
_AlertHistorySeverity_Type = DDMibAlertSeverityTC
_AlertHistorySeverity_Object = MibTableColumn
alertHistorySeverity = _AlertHistorySeverity_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 4, 2, 1, 1, 4),
    _AlertHistorySeverity_Type()
)
alertHistorySeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertHistorySeverity.setStatus("current")
_AlertHistoryStatus_Type = DDMibTableString64TC
_AlertHistoryStatus_Object = MibTableColumn
alertHistoryStatus = _AlertHistoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 4, 2, 1, 1, 5),
    _AlertHistoryStatus_Type()
)
alertHistoryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertHistoryStatus.setStatus("current")
_AlertInfo_ObjectIdentity = ObjectIdentity
alertInfo = _AlertInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 4, 3)
)
_AlertInfoTable_Object = MibTable
alertInfoTable = _AlertInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    alertInfoTable.setStatus("current")
_AlertInfoEntry_Object = MibTableRow
alertInfoEntry = _AlertInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 4, 3, 1, 1)
)
alertInfoEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "alertInfoIndex"),
)
if mibBuilder.loadTexts:
    alertInfoEntry.setStatus("current")
_AlertInfoIndex_Type = DDMibTableIndexTC
_AlertInfoIndex_Object = MibTableColumn
alertInfoIndex = _AlertInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 4, 3, 1, 1, 1),
    _AlertInfoIndex_Type()
)
alertInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alertInfoIndex.setStatus("current")
_AlertInfoDescription_Type = DDMibTableString256TC
_AlertInfoDescription_Object = MibTableColumn
alertInfoDescription = _AlertInfoDescription_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 4, 3, 1, 1, 2),
    _AlertInfoDescription_Type()
)
alertInfoDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertInfoDescription.setStatus("current")
_Statistics_ObjectIdentity = ObjectIdentity
statistics = _Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 5)
)
_SystemStats_ObjectIdentity = ObjectIdentity
systemStats = _SystemStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 5, 1)
)
_SystemStatsTable_Object = MibTable
systemStatsTable = _SystemStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    systemStatsTable.setStatus("current")
_SystemStatsEntry_Object = MibTableRow
systemStatsEntry = _SystemStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1)
)
systemStatsEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "systemStatsIndex"),
)
if mibBuilder.loadTexts:
    systemStatsEntry.setStatus("current")
_SystemStatsIndex_Type = SystemStatsIndexTC
_SystemStatsIndex_Object = MibTableColumn
systemStatsIndex = _SystemStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 1),
    _SystemStatsIndex_Type()
)
systemStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    systemStatsIndex.setStatus("current")
_CpuAvgPercentageBusy_Type = Percentage
_CpuAvgPercentageBusy_Object = MibTableColumn
cpuAvgPercentageBusy = _CpuAvgPercentageBusy_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 2),
    _CpuAvgPercentageBusy_Type()
)
cpuAvgPercentageBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuAvgPercentageBusy.setStatus("current")
_CpuMaxPercentageBusy_Type = Percentage
_CpuMaxPercentageBusy_Object = MibTableColumn
cpuMaxPercentageBusy = _CpuMaxPercentageBusy_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 3),
    _CpuMaxPercentageBusy_Type()
)
cpuMaxPercentageBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuMaxPercentageBusy.setStatus("current")
_NfsOpsPerSecond_Type = OpsPerSecond
_NfsOpsPerSecond_Object = MibTableColumn
nfsOpsPerSecond = _NfsOpsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 4),
    _NfsOpsPerSecond_Type()
)
nfsOpsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsOpsPerSecond.setStatus("current")
_NfsIdlePercentage_Type = Percentage
_NfsIdlePercentage_Object = MibTableColumn
nfsIdlePercentage = _NfsIdlePercentage_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 5),
    _NfsIdlePercentage_Type()
)
nfsIdlePercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsIdlePercentage.setStatus("current")
_NfsProcPercentage_Type = Percentage
_NfsProcPercentage_Object = MibTableColumn
nfsProcPercentage = _NfsProcPercentage_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 6),
    _NfsProcPercentage_Type()
)
nfsProcPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsProcPercentage.setStatus("current")
_NfsSendPercentage_Type = Percentage
_NfsSendPercentage_Object = MibTableColumn
nfsSendPercentage = _NfsSendPercentage_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 7),
    _NfsSendPercentage_Type()
)
nfsSendPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsSendPercentage.setStatus("current")
_NfsReceivePercentage_Type = Percentage
_NfsReceivePercentage_Object = MibTableColumn
nfsReceivePercentage = _NfsReceivePercentage_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 8),
    _NfsReceivePercentage_Type()
)
nfsReceivePercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsReceivePercentage.setStatus("current")
_CifsOpsPerSecond_Type = OpsPerSecond
_CifsOpsPerSecond_Object = MibTableColumn
cifsOpsPerSecond = _CifsOpsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 9),
    _CifsOpsPerSecond_Type()
)
cifsOpsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsOpsPerSecond.setStatus("current")
_DiskReadKBytesPerSecond_Type = KBytesPerSecond
_DiskReadKBytesPerSecond_Object = MibTableColumn
diskReadKBytesPerSecond = _DiskReadKBytesPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 10),
    _DiskReadKBytesPerSecond_Type()
)
diskReadKBytesPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskReadKBytesPerSecond.setStatus("current")
_DiskWriteKBytesPerSecond_Type = KBytesPerSecond
_DiskWriteKBytesPerSecond_Object = MibTableColumn
diskWriteKBytesPerSecond = _DiskWriteKBytesPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 11),
    _DiskWriteKBytesPerSecond_Type()
)
diskWriteKBytesPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskWriteKBytesPerSecond.setStatus("current")
_DiskBusyPercentage_Type = Percentage
_DiskBusyPercentage_Object = MibTableColumn
diskBusyPercentage = _DiskBusyPercentage_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 12),
    _DiskBusyPercentage_Type()
)
diskBusyPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskBusyPercentage.setStatus("current")
_NvramReadKBytesPerSecond_Type = KBytesPerSecond
_NvramReadKBytesPerSecond_Object = MibTableColumn
nvramReadKBytesPerSecond = _NvramReadKBytesPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 13),
    _NvramReadKBytesPerSecond_Type()
)
nvramReadKBytesPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvramReadKBytesPerSecond.setStatus("current")
_NvramWriteKBytesPerSecond_Type = KBytesPerSecond
_NvramWriteKBytesPerSecond_Object = MibTableColumn
nvramWriteKBytesPerSecond = _NvramWriteKBytesPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 14),
    _NvramWriteKBytesPerSecond_Type()
)
nvramWriteKBytesPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvramWriteKBytesPerSecond.setStatus("current")
_ReplInKBytesPerSecond_Type = KBytesPerSecond
_ReplInKBytesPerSecond_Object = MibTableColumn
replInKBytesPerSecond = _ReplInKBytesPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 15),
    _ReplInKBytesPerSecond_Type()
)
replInKBytesPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replInKBytesPerSecond.setStatus("current")
_ReplOutKBytesPerSecond_Type = KBytesPerSecond
_ReplOutKBytesPerSecond_Object = MibTableColumn
replOutKBytesPerSecond = _ReplOutKBytesPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 16),
    _ReplOutKBytesPerSecond_Type()
)
replOutKBytesPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replOutKBytesPerSecond.setStatus("current")
_DiskStorage_ObjectIdentity = ObjectIdentity
diskStorage = _DiskStorage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6)
)
_DiskProperties_ObjectIdentity = ObjectIdentity
diskProperties = _DiskProperties_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 1)
)
_DiskPropertiesTable_Object = MibTable
diskPropertiesTable = _DiskPropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    diskPropertiesTable.setStatus("current")
_DiskPropertiesEntry_Object = MibTableRow
diskPropertiesEntry = _DiskPropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1)
)
diskPropertiesEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "diskPropEnclosureID"),
    (0, "DATA-DOMAIN-MIB", "diskPropIndex"),
)
if mibBuilder.loadTexts:
    diskPropertiesEntry.setStatus("current")
_DiskPropEnclosureID_Type = EnclosureID
_DiskPropEnclosureID_Object = MibTableColumn
diskPropEnclosureID = _DiskPropEnclosureID_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 1),
    _DiskPropEnclosureID_Type()
)
diskPropEnclosureID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diskPropEnclosureID.setStatus("current")
_DiskPropIndex_Type = DiskIndexTC
_DiskPropIndex_Object = MibTableColumn
diskPropIndex = _DiskPropIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 2),
    _DiskPropIndex_Type()
)
diskPropIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diskPropIndex.setStatus("current")
_DiskPropTrapIndex_Type = DiskIndexTC
_DiskPropTrapIndex_Object = MibTableColumn
diskPropTrapIndex = _DiskPropTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 3),
    _DiskPropTrapIndex_Type()
)
diskPropTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskPropTrapIndex.setStatus("current")
_DiskModel_Type = DiskModelTC
_DiskModel_Object = MibTableColumn
diskModel = _DiskModel_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 4),
    _DiskModel_Type()
)
diskModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskModel.setStatus("current")
_DiskFirmwareVersion_Type = DiskFirmwareVersionTC
_DiskFirmwareVersion_Object = MibTableColumn
diskFirmwareVersion = _DiskFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 5),
    _DiskFirmwareVersion_Type()
)
diskFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskFirmwareVersion.setStatus("current")
_DiskSerialNumber_Type = DiskSerialNumberTC
_DiskSerialNumber_Object = MibTableColumn
diskSerialNumber = _DiskSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 6),
    _DiskSerialNumber_Type()
)
diskSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskSerialNumber.setStatus("current")
_DiskCapacity_Type = DiskCapacityTC
_DiskCapacity_Object = MibTableColumn
diskCapacity = _DiskCapacity_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 7),
    _DiskCapacity_Type()
)
diskCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskCapacity.setStatus("current")
_DiskPropState_Type = DiskStateTC
_DiskPropState_Object = MibTableColumn
diskPropState = _DiskPropState_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 8),
    _DiskPropState_Type()
)
diskPropState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskPropState.setStatus("current")
_DiskPack_Type = DiskPackTC
_DiskPack_Object = MibTableColumn
diskPack = _DiskPack_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 9),
    _DiskPack_Type()
)
diskPack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskPack.setStatus("current")
_DiskPerformance_ObjectIdentity = ObjectIdentity
diskPerformance = _DiskPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 2)
)
_DiskPerformanceTable_Object = MibTable
diskPerformanceTable = _DiskPerformanceTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1)
)
if mibBuilder.loadTexts:
    diskPerformanceTable.setStatus("current")
_DiskPerformanceEntry_Object = MibTableRow
diskPerformanceEntry = _DiskPerformanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1)
)
diskPerformanceEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "diskPerfEnclosureID"),
    (0, "DATA-DOMAIN-MIB", "diskPerfIndex"),
)
if mibBuilder.loadTexts:
    diskPerformanceEntry.setStatus("current")
_DiskPerfEnclosureID_Type = EnclosureID
_DiskPerfEnclosureID_Object = MibTableColumn
diskPerfEnclosureID = _DiskPerfEnclosureID_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1, 1),
    _DiskPerfEnclosureID_Type()
)
diskPerfEnclosureID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diskPerfEnclosureID.setStatus("current")
_DiskPerfIndex_Type = DiskIndexTC
_DiskPerfIndex_Object = MibTableColumn
diskPerfIndex = _DiskPerfIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1, 2),
    _DiskPerfIndex_Type()
)
diskPerfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diskPerfIndex.setStatus("current")
_DiskSectorsRead_Type = DiskSectorsPerSecondTC
_DiskSectorsRead_Object = MibTableColumn
diskSectorsRead = _DiskSectorsRead_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1, 3),
    _DiskSectorsRead_Type()
)
diskSectorsRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskSectorsRead.setStatus("current")
_DiskSectorsWritten_Type = DiskSectorsPerSecondTC
_DiskSectorsWritten_Object = MibTableColumn
diskSectorsWritten = _DiskSectorsWritten_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1, 4),
    _DiskSectorsWritten_Type()
)
diskSectorsWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskSectorsWritten.setStatus("current")
_DiskTotalKBytes_Type = KBytesPerSecond
_DiskTotalKBytes_Object = MibTableColumn
diskTotalKBytes = _DiskTotalKBytes_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1, 5),
    _DiskTotalKBytes_Type()
)
diskTotalKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskTotalKBytes.setStatus("current")
_DiskBusy_Type = Percentage
_DiskBusy_Object = MibTableColumn
diskBusy = _DiskBusy_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1, 6),
    _DiskBusy_Type()
)
diskBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskBusy.setStatus("current")
_DiskPerfState_Type = DiskStateTC
_DiskPerfState_Object = MibTableColumn
diskPerfState = _DiskPerfState_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1, 7),
    _DiskPerfState_Type()
)
diskPerfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskPerfState.setStatus("current")
_DiskReliability_ObjectIdentity = ObjectIdentity
diskReliability = _DiskReliability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 3)
)
_DiskReliabilityTable_Object = MibTable
diskReliabilityTable = _DiskReliabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1)
)
if mibBuilder.loadTexts:
    diskReliabilityTable.setStatus("current")
_DiskReliabilityEntry_Object = MibTableRow
diskReliabilityEntry = _DiskReliabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1)
)
diskReliabilityEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "diskErrEnclosureID"),
    (0, "DATA-DOMAIN-MIB", "diskErrIndex"),
)
if mibBuilder.loadTexts:
    diskReliabilityEntry.setStatus("current")
_DiskErrEnclosureID_Type = EnclosureID
_DiskErrEnclosureID_Object = MibTableColumn
diskErrEnclosureID = _DiskErrEnclosureID_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 1),
    _DiskErrEnclosureID_Type()
)
diskErrEnclosureID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diskErrEnclosureID.setStatus("current")
_DiskErrIndex_Type = DiskIndexTC
_DiskErrIndex_Object = MibTableColumn
diskErrIndex = _DiskErrIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 2),
    _DiskErrIndex_Type()
)
diskErrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diskErrIndex.setStatus("current")
_DiskErrTrapIndex_Type = DiskIndexTC
_DiskErrTrapIndex_Object = MibTableColumn
diskErrTrapIndex = _DiskErrTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 3),
    _DiskErrTrapIndex_Type()
)
diskErrTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskErrTrapIndex.setStatus("current")
_DiskTemperature_Type = Temperature
_DiskTemperature_Object = MibTableColumn
diskTemperature = _DiskTemperature_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 4),
    _DiskTemperature_Type()
)
diskTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskTemperature.setStatus("current")
_DiskTimeoutCount_Type = ErrorCount
_DiskTimeoutCount_Object = MibTableColumn
diskTimeoutCount = _DiskTimeoutCount_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 5),
    _DiskTimeoutCount_Type()
)
diskTimeoutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskTimeoutCount.setStatus("current")
_DiskReadFailCount_Type = ErrorCount
_DiskReadFailCount_Object = MibTableColumn
diskReadFailCount = _DiskReadFailCount_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 6),
    _DiskReadFailCount_Type()
)
diskReadFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskReadFailCount.setStatus("current")
_DiskWriteFailCount_Type = ErrorCount
_DiskWriteFailCount_Object = MibTableColumn
diskWriteFailCount = _DiskWriteFailCount_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 7),
    _DiskWriteFailCount_Type()
)
diskWriteFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskWriteFailCount.setStatus("current")
_DiskMiscFailCount_Type = ErrorCount
_DiskMiscFailCount_Object = MibTableColumn
diskMiscFailCount = _DiskMiscFailCount_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 8),
    _DiskMiscFailCount_Type()
)
diskMiscFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskMiscFailCount.setStatus("current")
_DiskOffTrackErrCount_Type = ErrorCount
_DiskOffTrackErrCount_Object = MibTableColumn
diskOffTrackErrCount = _DiskOffTrackErrCount_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 9),
    _DiskOffTrackErrCount_Type()
)
diskOffTrackErrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskOffTrackErrCount.setStatus("current")
_DiskSoftEccCount_Type = ErrorCount
_DiskSoftEccCount_Object = MibTableColumn
diskSoftEccCount = _DiskSoftEccCount_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 10),
    _DiskSoftEccCount_Type()
)
diskSoftEccCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskSoftEccCount.setStatus("current")
_DiskCrcErrCount_Type = ErrorCount
_DiskCrcErrCount_Object = MibTableColumn
diskCrcErrCount = _DiskCrcErrCount_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 11),
    _DiskCrcErrCount_Type()
)
diskCrcErrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskCrcErrCount.setStatus("current")
_DiskProbationalCount_Type = ErrorCount
_DiskProbationalCount_Object = MibTableColumn
diskProbationalCount = _DiskProbationalCount_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 12),
    _DiskProbationalCount_Type()
)
diskProbationalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskProbationalCount.setStatus("current")
_DiskReallocCount_Type = ErrorCount
_DiskReallocCount_Object = MibTableColumn
diskReallocCount = _DiskReallocCount_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 13),
    _DiskReallocCount_Type()
)
diskReallocCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskReallocCount.setStatus("current")
_DiskErrState_Type = DiskStateTC
_DiskErrState_Object = MibTableColumn
diskErrState = _DiskErrState_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 14),
    _DiskErrState_Type()
)
diskErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskErrState.setStatus("current")
_Replication_ObjectIdentity = ObjectIdentity
replication = _Replication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8)
)
_ReplicationInfo_ObjectIdentity = ObjectIdentity
replicationInfo = _ReplicationInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 1)
)
_ReplicationInfoTable_Object = MibTable
replicationInfoTable = _ReplicationInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1)
)
if mibBuilder.loadTexts:
    replicationInfoTable.setStatus("current")
_ReplicationInfoEntry_Object = MibTableRow
replicationInfoEntry = _ReplicationInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1)
)
replicationInfoEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "replContext"),
)
if mibBuilder.loadTexts:
    replicationInfoEntry.setStatus("current")
_ReplContext_Type = ReplicationContextTC
_ReplContext_Object = MibTableColumn
replContext = _ReplContext_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 1),
    _ReplContext_Type()
)
replContext.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    replContext.setStatus("current")
_ReplTrapContext_Type = ReplicationContextTC
_ReplTrapContext_Object = MibTableColumn
replTrapContext = _ReplTrapContext_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 2),
    _ReplTrapContext_Type()
)
replTrapContext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replTrapContext.setStatus("current")
_ReplState_Type = ReplicationStateTC
_ReplState_Object = MibTableColumn
replState = _ReplState_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 3),
    _ReplState_Type()
)
replState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replState.setStatus("current")
_ReplStatus_Type = ReplicationStatusTC
_ReplStatus_Object = MibTableColumn
replStatus = _ReplStatus_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 4),
    _ReplStatus_Type()
)
replStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replStatus.setStatus("current")
_ReplFileSysStatus_Type = FileSystemStatusTC
_ReplFileSysStatus_Object = MibTableColumn
replFileSysStatus = _ReplFileSysStatus_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 5),
    _ReplFileSysStatus_Type()
)
replFileSysStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replFileSysStatus.setStatus("current")
_ReplConnTime_Type = ReplicationConnectTimeTC
_ReplConnTime_Object = MibTableColumn
replConnTime = _ReplConnTime_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 6),
    _ReplConnTime_Type()
)
replConnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replConnTime.setStatus("current")
_ReplSource_Type = ReplicationPathTC
_ReplSource_Object = MibTableColumn
replSource = _ReplSource_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 7),
    _ReplSource_Type()
)
replSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replSource.setStatus("current")
_ReplDestination_Type = ReplicationPathTC
_ReplDestination_Object = MibTableColumn
replDestination = _ReplDestination_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 8),
    _ReplDestination_Type()
)
replDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replDestination.setStatus("current")
_ReplPreCompBytesSent_Type = ReplicationTrafficTC
_ReplPreCompBytesSent_Object = MibTableColumn
replPreCompBytesSent = _ReplPreCompBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 9),
    _ReplPreCompBytesSent_Type()
)
replPreCompBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replPreCompBytesSent.setStatus("current")
_ReplPostCompBytesSent_Type = ReplicationTrafficTC
_ReplPostCompBytesSent_Object = MibTableColumn
replPostCompBytesSent = _ReplPostCompBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 10),
    _ReplPostCompBytesSent_Type()
)
replPostCompBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replPostCompBytesSent.setStatus("current")
_ReplPreCompBytesRemaining_Type = ReplicationTrafficTC
_ReplPreCompBytesRemaining_Object = MibTableColumn
replPreCompBytesRemaining = _ReplPreCompBytesRemaining_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 11),
    _ReplPreCompBytesRemaining_Type()
)
replPreCompBytesRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replPreCompBytesRemaining.setStatus("current")
_ReplPostCompBytesReceived_Type = ReplicationTrafficTC
_ReplPostCompBytesReceived_Object = MibTableColumn
replPostCompBytesReceived = _ReplPostCompBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 12),
    _ReplPostCompBytesReceived_Type()
)
replPostCompBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replPostCompBytesReceived.setStatus("current")
_ReplThrottle_Type = ReplicationThrottleTC
_ReplThrottle_Object = MibTableColumn
replThrottle = _ReplThrottle_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 13),
    _ReplThrottle_Type()
)
replThrottle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replThrottle.setStatus("current")
_ReplSyncedAsOfTime_Type = ReplicationSyncedTimeTC
_ReplSyncedAsOfTime_Object = MibTableColumn
replSyncedAsOfTime = _ReplSyncedAsOfTime_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 14),
    _ReplSyncedAsOfTime_Type()
)
replSyncedAsOfTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replSyncedAsOfTime.setStatus("current")
_ReplicationConfig_ObjectIdentity = ObjectIdentity
replicationConfig = _ReplicationConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 2)
)
_ReplicationConfigTable_Object = MibTable
replicationConfigTable = _ReplicationConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 2, 1)
)
if mibBuilder.loadTexts:
    replicationConfigTable.setStatus("current")
_ReplicationConfigEntry_Object = MibTableRow
replicationConfigEntry = _ReplicationConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 2, 1, 1)
)
replicationConfigEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "replConfigIndex"),
)
if mibBuilder.loadTexts:
    replicationConfigEntry.setStatus("current")
_ReplConfigIndex_Type = ReplicationConfigIndexTC
_ReplConfigIndex_Object = MibTableColumn
replConfigIndex = _ReplConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 2, 1, 1, 1),
    _ReplConfigIndex_Type()
)
replConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    replConfigIndex.setStatus("current")
_ReplConfigContextId_Type = ReplicationConfigContextIdTC
_ReplConfigContextId_Object = MibTableColumn
replConfigContextId = _ReplConfigContextId_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 2, 1, 1, 2),
    _ReplConfigContextId_Type()
)
replConfigContextId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replConfigContextId.setStatus("current")
_ReplConfigSource_Type = ReplicationConfigSourceTC
_ReplConfigSource_Object = MibTableColumn
replConfigSource = _ReplConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 2, 1, 1, 3),
    _ReplConfigSource_Type()
)
replConfigSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replConfigSource.setStatus("current")
_ReplConfigDest_Type = ReplicationConfigDestTC
_ReplConfigDest_Object = MibTableColumn
replConfigDest = _ReplConfigDest_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 2, 1, 1, 4),
    _ReplConfigDest_Type()
)
replConfigDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replConfigDest.setStatus("current")
_ReplConfigConnHost_Type = ReplicationConfigConnHostTC
_ReplConfigConnHost_Object = MibTableColumn
replConfigConnHost = _ReplConfigConnHost_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 2, 1, 1, 5),
    _ReplConfigConnHost_Type()
)
replConfigConnHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replConfigConnHost.setStatus("current")
_ReplConfigConnPort_Type = ReplicationConfigConnPortTC
_ReplConfigConnPort_Object = MibTableColumn
replConfigConnPort = _ReplConfigConnPort_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 2, 1, 1, 6),
    _ReplConfigConnPort_Type()
)
replConfigConnPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replConfigConnPort.setStatus("current")
_ReplConfigLowBWOptim_Type = ReplicationConfigLowBWOptimTC
_ReplConfigLowBWOptim_Object = MibTableColumn
replConfigLowBWOptim = _ReplConfigLowBWOptim_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 2, 1, 1, 7),
    _ReplConfigLowBWOptim_Type()
)
replConfigLowBWOptim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replConfigLowBWOptim.setStatus("current")
_ReplConfigEnabled_Type = ReplicationConfigEnabledTC
_ReplConfigEnabled_Object = MibTableColumn
replConfigEnabled = _ReplConfigEnabled_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 2, 1, 1, 8),
    _ReplConfigEnabled_Type()
)
replConfigEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replConfigEnabled.setStatus("current")
_ReplConfigTenantUnit_Type = DDMibString96TC
_ReplConfigTenantUnit_Object = MibTableColumn
replConfigTenantUnit = _ReplConfigTenantUnit_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 2, 1, 1, 9),
    _ReplConfigTenantUnit_Type()
)
replConfigTenantUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replConfigTenantUnit.setStatus("current")
_ReplicationHistory_ObjectIdentity = ObjectIdentity
replicationHistory = _ReplicationHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 3)
)
_ReplicationHistoryTable_Object = MibTable
replicationHistoryTable = _ReplicationHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 3, 1)
)
if mibBuilder.loadTexts:
    replicationHistoryTable.setStatus("current")
_ReplicationHistoryEntry_Object = MibTableRow
replicationHistoryEntry = _ReplicationHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 3, 1, 1)
)
replicationHistoryEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "replHistoryContext"),
)
if mibBuilder.loadTexts:
    replicationHistoryEntry.setStatus("current")
_ReplHistoryContext_Type = DDMibTableIndexTC
_ReplHistoryContext_Object = MibTableColumn
replHistoryContext = _ReplHistoryContext_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 3, 1, 1, 1),
    _ReplHistoryContext_Type()
)
replHistoryContext.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    replHistoryContext.setStatus("current")
_ReplHistoryDate_Type = DDMibDateTC
_ReplHistoryDate_Object = MibTableColumn
replHistoryDate = _ReplHistoryDate_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 3, 1, 1, 2),
    _ReplHistoryDate_Type()
)
replHistoryDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replHistoryDate.setStatus("current")
_ReplHistoryTime_Type = DDMibTimeStampTC
_ReplHistoryTime_Object = MibTableColumn
replHistoryTime = _ReplHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 3, 1, 1, 3),
    _ReplHistoryTime_Type()
)
replHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replHistoryTime.setStatus("current")
_ReplHistoryPreCompWritten_Type = DDMibTrafficBytesTC
_ReplHistoryPreCompWritten_Object = MibTableColumn
replHistoryPreCompWritten = _ReplHistoryPreCompWritten_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 3, 1, 1, 4),
    _ReplHistoryPreCompWritten_Type()
)
replHistoryPreCompWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replHistoryPreCompWritten.setStatus("current")
_ReplHistoryPreCompRemaining_Type = DDMibTrafficBytesTC
_ReplHistoryPreCompRemaining_Object = MibTableColumn
replHistoryPreCompRemaining = _ReplHistoryPreCompRemaining_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 3, 1, 1, 5),
    _ReplHistoryPreCompRemaining_Type()
)
replHistoryPreCompRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replHistoryPreCompRemaining.setStatus("current")
_ReplHistoryPreCompressed_Type = DDMibTrafficBytesTC
_ReplHistoryPreCompressed_Object = MibTableColumn
replHistoryPreCompressed = _ReplHistoryPreCompressed_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 3, 1, 1, 6),
    _ReplHistoryPreCompressed_Type()
)
replHistoryPreCompressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replHistoryPreCompressed.setStatus("current")
_ReplHistoryPostFiltered_Type = DDMibTrafficBytesTC
_ReplHistoryPostFiltered_Object = MibTableColumn
replHistoryPostFiltered = _ReplHistoryPostFiltered_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 3, 1, 1, 7),
    _ReplHistoryPostFiltered_Type()
)
replHistoryPostFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replHistoryPostFiltered.setStatus("current")
_ReplHistoryPostLowBwOptim_Type = DDMibTrafficBytesTC
_ReplHistoryPostLowBwOptim_Object = MibTableColumn
replHistoryPostLowBwOptim = _ReplHistoryPostLowBwOptim_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 3, 1, 1, 8),
    _ReplHistoryPostLowBwOptim_Type()
)
replHistoryPostLowBwOptim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replHistoryPostLowBwOptim.setStatus("current")
_ReplHistoryPostLocalComp_Type = DDMibTrafficBytesTC
_ReplHistoryPostLocalComp_Object = MibTableColumn
replHistoryPostLocalComp = _ReplHistoryPostLocalComp_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 3, 1, 1, 9),
    _ReplHistoryPostLocalComp_Type()
)
replHistoryPostLocalComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replHistoryPostLocalComp.setStatus("current")
_ReplHistoryBytesNetwork_Type = DDMibTrafficBytesTC
_ReplHistoryBytesNetwork_Object = MibTableColumn
replHistoryBytesNetwork = _ReplHistoryBytesNetwork_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 3, 1, 1, 10),
    _ReplHistoryBytesNetwork_Type()
)
replHistoryBytesNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replHistoryBytesNetwork.setStatus("current")
_ReplHistorySyncedAsOfTime_Type = DDMibInteger32TC
_ReplHistorySyncedAsOfTime_Object = MibTableColumn
replHistorySyncedAsOfTime = _ReplHistorySyncedAsOfTime_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 3, 1, 1, 11),
    _ReplHistorySyncedAsOfTime_Type()
)
replHistorySyncedAsOfTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replHistorySyncedAsOfTime.setStatus("current")
_ReplicationPerformance_ObjectIdentity = ObjectIdentity
replicationPerformance = _ReplicationPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 4)
)
_ReplicationPerformanceTable_Object = MibTable
replicationPerformanceTable = _ReplicationPerformanceTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 4, 1)
)
if mibBuilder.loadTexts:
    replicationPerformanceTable.setStatus("current")
_ReplicationPerformanceEntry_Object = MibTableRow
replicationPerformanceEntry = _ReplicationPerformanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 4, 1, 1)
)
replicationPerformanceEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "replContext"),
)
if mibBuilder.loadTexts:
    replicationPerformanceEntry.setStatus("current")
_ReplPerformancePreCompKBPerSec_Type = DDMibInteger32TC
_ReplPerformancePreCompKBPerSec_Object = MibTableColumn
replPerformancePreCompKBPerSec = _ReplPerformancePreCompKBPerSec_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 4, 1, 1, 1),
    _ReplPerformancePreCompKBPerSec_Type()
)
replPerformancePreCompKBPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replPerformancePreCompKBPerSec.setStatus("current")
_ReplPerformanceNetworkKBPerSec_Type = DDMibInteger32TC
_ReplPerformanceNetworkKBPerSec_Object = MibTableColumn
replPerformanceNetworkKBPerSec = _ReplPerformanceNetworkKBPerSec_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 4, 1, 1, 2),
    _ReplPerformanceNetworkKBPerSec_Type()
)
replPerformanceNetworkKBPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replPerformanceNetworkKBPerSec.setStatus("current")
_ReplPerformanceStreams_Type = DDMibInteger32TC
_ReplPerformanceStreams_Object = MibTableColumn
replPerformanceStreams = _ReplPerformanceStreams_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 4, 1, 1, 3),
    _ReplPerformanceStreams_Type()
)
replPerformanceStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replPerformanceStreams.setStatus("current")
_ReplPerformanceBusyReading_Type = DDMibInteger32TC
_ReplPerformanceBusyReading_Object = MibTableColumn
replPerformanceBusyReading = _ReplPerformanceBusyReading_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 4, 1, 1, 4),
    _ReplPerformanceBusyReading_Type()
)
replPerformanceBusyReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replPerformanceBusyReading.setStatus("current")
_ReplPerformanceBusyMeta_Type = DDMibInteger32TC
_ReplPerformanceBusyMeta_Object = MibTableColumn
replPerformanceBusyMeta = _ReplPerformanceBusyMeta_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 4, 1, 1, 5),
    _ReplPerformanceBusyMeta_Type()
)
replPerformanceBusyMeta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replPerformanceBusyMeta.setStatus("current")
_ReplPerformanceWaitingDest_Type = DDMibInteger32TC
_ReplPerformanceWaitingDest_Object = MibTableColumn
replPerformanceWaitingDest = _ReplPerformanceWaitingDest_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 4, 1, 1, 6),
    _ReplPerformanceWaitingDest_Type()
)
replPerformanceWaitingDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replPerformanceWaitingDest.setStatus("current")
_ReplPerformanceWaitingNetwork_Type = DDMibInteger32TC
_ReplPerformanceWaitingNetwork_Object = MibTableColumn
replPerformanceWaitingNetwork = _ReplPerformanceWaitingNetwork_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 4, 1, 1, 7),
    _ReplPerformanceWaitingNetwork_Type()
)
replPerformanceWaitingNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replPerformanceWaitingNetwork.setStatus("current")
_Nfs_ObjectIdentity = ObjectIdentity
nfs = _Nfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 9)
)
_NfsProperties_ObjectIdentity = ObjectIdentity
nfsProperties = _NfsProperties_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 9, 1)
)
_NfsStatus_Type = NfsStatusTC
_NfsStatus_Object = MibScalar
nfsStatus = _NfsStatus_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 9, 1, 1),
    _NfsStatus_Type()
)
nfsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsStatus.setStatus("current")
_NfsClient_ObjectIdentity = ObjectIdentity
nfsClient = _NfsClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 9, 2)
)
_NfsClientTable_Object = MibTable
nfsClientTable = _NfsClientTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 9, 2, 1)
)
if mibBuilder.loadTexts:
    nfsClientTable.setStatus("current")
_NfsClientEntry_Object = MibTableRow
nfsClientEntry = _NfsClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 9, 2, 1, 1)
)
nfsClientEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "nfsClientIndex"),
)
if mibBuilder.loadTexts:
    nfsClientEntry.setStatus("current")
_NfsClientIndex_Type = NfsClientIndexTC
_NfsClientIndex_Object = MibTableColumn
nfsClientIndex = _NfsClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 9, 2, 1, 1, 1),
    _NfsClientIndex_Type()
)
nfsClientIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nfsClientIndex.setStatus("current")
_NfsClientPath_Type = NfsClientPathTC
_NfsClientPath_Object = MibTableColumn
nfsClientPath = _NfsClientPath_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 9, 2, 1, 1, 2),
    _NfsClientPath_Type()
)
nfsClientPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsClientPath.setStatus("current")
_NfsClientClients_Type = NfsClientClientsTC
_NfsClientClients_Object = MibTableColumn
nfsClientClients = _NfsClientClients_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 9, 2, 1, 1, 3),
    _NfsClientClients_Type()
)
nfsClientClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsClientClients.setStatus("current")
_NfsClientOptions_Type = NfsClientOptionsTC
_NfsClientOptions_Object = MibTableColumn
nfsClientOptions = _NfsClientOptions_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 9, 2, 1, 1, 4),
    _NfsClientOptions_Type()
)
nfsClientOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsClientOptions.setStatus("current")
_NfsStats_ObjectIdentity = ObjectIdentity
nfsStats = _NfsStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 9, 3)
)
_NfsStatsTable_Object = MibTable
nfsStatsTable = _NfsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 9, 3, 1)
)
if mibBuilder.loadTexts:
    nfsStatsTable.setStatus("current")
_NfsStatsEntry_Object = MibTableRow
nfsStatsEntry = _NfsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 9, 3, 1, 1)
)
nfsStatsEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "nfsStatsIndex"),
)
if mibBuilder.loadTexts:
    nfsStatsEntry.setStatus("current")
_NfsStatsIndex_Type = NfsStatsIndexTC
_NfsStatsIndex_Object = MibTableColumn
nfsStatsIndex = _NfsStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 9, 3, 1, 1, 1),
    _NfsStatsIndex_Type()
)
nfsStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nfsStatsIndex.setStatus("current")
_NfsStatsExportPoint_Type = NfsStatsExportPointTC
_NfsStatsExportPoint_Object = MibTableColumn
nfsStatsExportPoint = _NfsStatsExportPoint_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 9, 3, 1, 1, 2),
    _NfsStatsExportPoint_Type()
)
nfsStatsExportPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsStatsExportPoint.setStatus("current")
_NfsStatsFilesystemType_Type = NfsStatsFilesystemTypeTC
_NfsStatsFilesystemType_Object = MibTableColumn
nfsStatsFilesystemType = _NfsStatsFilesystemType_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 9, 3, 1, 1, 3),
    _NfsStatsFilesystemType_Type()
)
nfsStatsFilesystemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsStatsFilesystemType.setStatus("current")
_NfsStatsCacheEntry_Type = NfsStatsCacheEntryTC
_NfsStatsCacheEntry_Object = MibTableColumn
nfsStatsCacheEntry = _NfsStatsCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 9, 3, 1, 1, 4),
    _NfsStatsCacheEntry_Type()
)
nfsStatsCacheEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsStatsCacheEntry.setStatus("current")
_NfsStatsFileHandleLookup_Type = NfsStatsFileHandleLookupTC
_NfsStatsFileHandleLookup_Object = MibTableColumn
nfsStatsFileHandleLookup = _NfsStatsFileHandleLookup_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 9, 3, 1, 1, 5),
    _NfsStatsFileHandleLookup_Type()
)
nfsStatsFileHandleLookup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsStatsFileHandleLookup.setStatus("current")
_NfsStatsMaxCacheSize_Type = NfsStatsMaxCacheSizeTC
_NfsStatsMaxCacheSize_Object = MibTableColumn
nfsStatsMaxCacheSize = _NfsStatsMaxCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 9, 3, 1, 1, 6),
    _NfsStatsMaxCacheSize_Type()
)
nfsStatsMaxCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsStatsMaxCacheSize.setStatus("current")
_NfsStatsCurrentOpenStreams_Type = NfsStatsCurrentOpenStreamsTC
_NfsStatsCurrentOpenStreams_Object = MibTableColumn
nfsStatsCurrentOpenStreams = _NfsStatsCurrentOpenStreams_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 9, 3, 1, 1, 7),
    _NfsStatsCurrentOpenStreams_Type()
)
nfsStatsCurrentOpenStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsStatsCurrentOpenStreams.setStatus("current")
_NfsActive_ObjectIdentity = ObjectIdentity
nfsActive = _NfsActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 9, 4)
)
_NfsActiveTable_Object = MibTable
nfsActiveTable = _NfsActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 9, 4, 1)
)
if mibBuilder.loadTexts:
    nfsActiveTable.setStatus("current")
_NfsActiveEntry_Object = MibTableRow
nfsActiveEntry = _NfsActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 9, 4, 1, 1)
)
nfsActiveEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "nfsActiveIndex"),
)
if mibBuilder.loadTexts:
    nfsActiveEntry.setStatus("current")
_NfsActiveIndex_Type = DDMibTableIndexTC
_NfsActiveIndex_Object = MibTableColumn
nfsActiveIndex = _NfsActiveIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 9, 4, 1, 1, 1),
    _NfsActiveIndex_Type()
)
nfsActiveIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nfsActiveIndex.setStatus("current")
_NfsActivePath_Type = DDMibTableString1024TC
_NfsActivePath_Object = MibTableColumn
nfsActivePath = _NfsActivePath_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 9, 4, 1, 1, 2),
    _NfsActivePath_Type()
)
nfsActivePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsActivePath.setStatus("current")
_NfsActiveClients_Type = DDMibTableString1024TC
_NfsActiveClients_Object = MibTableColumn
nfsActiveClients = _NfsActiveClients_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 9, 4, 1, 1, 3),
    _NfsActiveClients_Type()
)
nfsActiveClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsActiveClients.setStatus("current")
_NfsPort_ObjectIdentity = ObjectIdentity
nfsPort = _NfsPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 9, 5)
)
_NfsPortTable_Object = MibTable
nfsPortTable = _NfsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 9, 5, 1)
)
if mibBuilder.loadTexts:
    nfsPortTable.setStatus("current")
_NfsPortEntry_Object = MibTableRow
nfsPortEntry = _NfsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 9, 5, 1, 1)
)
nfsPortEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "nfsPortIndex"),
)
if mibBuilder.loadTexts:
    nfsPortEntry.setStatus("current")
_NfsPortIndex_Type = DDMibTableIndexTC
_NfsPortIndex_Object = MibTableColumn
nfsPortIndex = _NfsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 9, 5, 1, 1, 1),
    _NfsPortIndex_Type()
)
nfsPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nfsPortIndex.setStatus("current")
_NfsPortService_Type = DDMibTableString32TC
_NfsPortService_Object = MibTableColumn
nfsPortService = _NfsPortService_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 9, 5, 1, 1, 2),
    _NfsPortService_Type()
)
nfsPortService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsPortService.setStatus("current")
_NfsPortPort_Type = DDMibTableString32TC
_NfsPortPort_Object = MibTableColumn
nfsPortPort = _NfsPortPort_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 9, 5, 1, 1, 3),
    _NfsPortPort_Type()
)
nfsPortPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsPortPort.setStatus("current")
_Cifs_ObjectIdentity = ObjectIdentity
cifs = _Cifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 10)
)
_CifsProperties_ObjectIdentity = ObjectIdentity
cifsProperties = _CifsProperties_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 10, 1)
)
_CifsStatus_Type = CifsStatusTC
_CifsStatus_Object = MibScalar
cifsStatus = _CifsStatus_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 10, 1, 1),
    _CifsStatus_Type()
)
cifsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsStatus.setStatus("current")
_CifsConfig_ObjectIdentity = ObjectIdentity
cifsConfig = _CifsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 10, 2)
)
_CifsConfigMode_Type = CifsConfigModeTC
_CifsConfigMode_Object = MibScalar
cifsConfigMode = _CifsConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 10, 2, 1),
    _CifsConfigMode_Type()
)
cifsConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsConfigMode.setStatus("current")
_CifsConfigWINSServer_Type = CifsConfigWINSServerTC
_CifsConfigWINSServer_Object = MibScalar
cifsConfigWINSServer = _CifsConfigWINSServer_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 10, 2, 2),
    _CifsConfigWINSServer_Type()
)
cifsConfigWINSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsConfigWINSServer.setStatus("current")
_CifsConfigNetBIOSHostname_Type = CifsConfigNetBIOSHostnameTC
_CifsConfigNetBIOSHostname_Object = MibScalar
cifsConfigNetBIOSHostname = _CifsConfigNetBIOSHostname_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 10, 2, 3),
    _CifsConfigNetBIOSHostname_Type()
)
cifsConfigNetBIOSHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsConfigNetBIOSHostname.setStatus("current")
_CifsConfigDomainController_Type = CifsConfigDomainControllerTC
_CifsConfigDomainController_Object = MibScalar
cifsConfigDomainController = _CifsConfigDomainController_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 10, 2, 4),
    _CifsConfigDomainController_Type()
)
cifsConfigDomainController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsConfigDomainController.setStatus("current")
_CifsConfigDNS_Type = CifsConfigDNSTC
_CifsConfigDNS_Object = MibScalar
cifsConfigDNS = _CifsConfigDNS_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 10, 2, 5),
    _CifsConfigDNS_Type()
)
cifsConfigDNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsConfigDNS.setStatus("current")
_CifsConfigGroupName_Type = CifsConfigGroupNameTC
_CifsConfigGroupName_Object = MibScalar
cifsConfigGroupName = _CifsConfigGroupName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 10, 2, 6),
    _CifsConfigGroupName_Type()
)
cifsConfigGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsConfigGroupName.setStatus("current")
_CifsConfigMaxConnection_Type = CifsConfigMaxConnectionTC
_CifsConfigMaxConnection_Object = MibScalar
cifsConfigMaxConnection = _CifsConfigMaxConnection_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 10, 2, 7),
    _CifsConfigMaxConnection_Type()
)
cifsConfigMaxConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsConfigMaxConnection.setStatus("current")
_CifsConfigMaxOpenFilesPerConnection_Type = CifsConfigMaxOpenFilesPerConnectionTC
_CifsConfigMaxOpenFilesPerConnection_Object = MibScalar
cifsConfigMaxOpenFilesPerConnection = _CifsConfigMaxOpenFilesPerConnection_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 10, 2, 8),
    _CifsConfigMaxOpenFilesPerConnection_Type()
)
cifsConfigMaxOpenFilesPerConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsConfigMaxOpenFilesPerConnection.setStatus("deprecated")
_CifsConfigMaxOpenFiles_Type = Counter32
_CifsConfigMaxOpenFiles_Object = MibScalar
cifsConfigMaxOpenFiles = _CifsConfigMaxOpenFiles_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 10, 2, 9),
    _CifsConfigMaxOpenFiles_Type()
)
cifsConfigMaxOpenFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsConfigMaxOpenFiles.setStatus("current")
_CifsShare_ObjectIdentity = ObjectIdentity
cifsShare = _CifsShare_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 10, 3)
)
_CifsShareTable_Object = MibTable
cifsShareTable = _CifsShareTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 10, 3, 1)
)
if mibBuilder.loadTexts:
    cifsShareTable.setStatus("current")
_CifsShareEntry_Object = MibTableRow
cifsShareEntry = _CifsShareEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 10, 3, 1, 1)
)
cifsShareEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "cifsShareIndex"),
)
if mibBuilder.loadTexts:
    cifsShareEntry.setStatus("current")
_CifsShareIndex_Type = CifsShareIndexTC
_CifsShareIndex_Object = MibTableColumn
cifsShareIndex = _CifsShareIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 10, 3, 1, 1, 1),
    _CifsShareIndex_Type()
)
cifsShareIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cifsShareIndex.setStatus("current")
_CifsShareName_Type = CifsShareNameTC
_CifsShareName_Object = MibTableColumn
cifsShareName = _CifsShareName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 10, 3, 1, 1, 2),
    _CifsShareName_Type()
)
cifsShareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsShareName.setStatus("current")
_CifsSharePath_Type = CifsSharePathTC
_CifsSharePath_Object = MibTableColumn
cifsSharePath = _CifsSharePath_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 10, 3, 1, 1, 3),
    _CifsSharePath_Type()
)
cifsSharePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsSharePath.setStatus("current")
_CifsShareClients_Type = CifsShareClientsTC
_CifsShareClients_Object = MibTableColumn
cifsShareClients = _CifsShareClients_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 10, 3, 1, 1, 4),
    _CifsShareClients_Type()
)
cifsShareClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsShareClients.setStatus("current")
_CifsShareUser_Type = CifsShareUserTC
_CifsShareUser_Object = MibTableColumn
cifsShareUser = _CifsShareUser_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 10, 3, 1, 1, 5),
    _CifsShareUser_Type()
)
cifsShareUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsShareUser.setStatus("current")
_CifsShareComment_Type = CifsShareCommentTC
_CifsShareComment_Object = MibTableColumn
cifsShareComment = _CifsShareComment_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 10, 3, 1, 1, 6),
    _CifsShareComment_Type()
)
cifsShareComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsShareComment.setStatus("current")
_CifsShareBrowsing_Type = CifsShareBrowsingTC
_CifsShareBrowsing_Object = MibTableColumn
cifsShareBrowsing = _CifsShareBrowsing_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 10, 3, 1, 1, 7),
    _CifsShareBrowsing_Type()
)
cifsShareBrowsing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsShareBrowsing.setStatus("current")
_CifsShareWriteable_Type = CifsShareWriteableTC
_CifsShareWriteable_Object = MibTableColumn
cifsShareWriteable = _CifsShareWriteable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 10, 3, 1, 1, 8),
    _CifsShareWriteable_Type()
)
cifsShareWriteable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsShareWriteable.setStatus("current")
_CifsShareMaxConnection_Type = CifsShareMaxConnectionTC
_CifsShareMaxConnection_Object = MibTableColumn
cifsShareMaxConnection = _CifsShareMaxConnection_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 10, 3, 1, 1, 9),
    _CifsShareMaxConnection_Type()
)
cifsShareMaxConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsShareMaxConnection.setStatus("current")
_CifsOptions_ObjectIdentity = ObjectIdentity
cifsOptions = _CifsOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 10, 5)
)
_CifsOptionsTable_Object = MibTable
cifsOptionsTable = _CifsOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 10, 5, 1)
)
if mibBuilder.loadTexts:
    cifsOptionsTable.setStatus("current")
_CifsOptionsEntry_Object = MibTableRow
cifsOptionsEntry = _CifsOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 10, 5, 1, 1)
)
cifsOptionsEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "cifsOptionsIndex"),
)
if mibBuilder.loadTexts:
    cifsOptionsEntry.setStatus("current")
_CifsOptionsIndex_Type = CifsOptionsIndexTC
_CifsOptionsIndex_Object = MibTableColumn
cifsOptionsIndex = _CifsOptionsIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 10, 5, 1, 1, 1),
    _CifsOptionsIndex_Type()
)
cifsOptionsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cifsOptionsIndex.setStatus("current")
_CifsOptionsName_Type = CifsOptionsNameTC
_CifsOptionsName_Object = MibTableColumn
cifsOptionsName = _CifsOptionsName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 10, 5, 1, 1, 2),
    _CifsOptionsName_Type()
)
cifsOptionsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsOptionsName.setStatus("current")
_CifsOptionsValue_Type = CifsOptionsValueTC
_CifsOptionsValue_Object = MibTableColumn
cifsOptionsValue = _CifsOptionsValue_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 10, 5, 1, 1, 3),
    _CifsOptionsValue_Type()
)
cifsOptionsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsOptionsValue.setStatus("current")
_Vtl_ObjectIdentity = ObjectIdentity
vtl = _Vtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11)
)
_VtlProperties_ObjectIdentity = ObjectIdentity
vtlProperties = _VtlProperties_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 1)
)
_VtlAdminState_Type = VtlAdminStateTC
_VtlAdminState_Object = MibScalar
vtlAdminState = _VtlAdminState_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 1, 1),
    _VtlAdminState_Type()
)
vtlAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlAdminState.setStatus("current")
_VtlProcessState_Type = VtlProcessStateTC
_VtlProcessState_Object = MibScalar
vtlProcessState = _VtlProcessState_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 1, 2),
    _VtlProcessState_Type()
)
vtlProcessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlProcessState.setStatus("current")
_VtlConfiguration_ObjectIdentity = ObjectIdentity
vtlConfiguration = _VtlConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2)
)
_VtlLibrary_ObjectIdentity = ObjectIdentity
vtlLibrary = _VtlLibrary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 1)
)
_VtlLibraryTable_Object = MibTable
vtlLibraryTable = _VtlLibraryTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 1, 1)
)
if mibBuilder.loadTexts:
    vtlLibraryTable.setStatus("current")
_VtlLibraryEntry_Object = MibTableRow
vtlLibraryEntry = _VtlLibraryEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 1, 1, 1)
)
vtlLibraryEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "vtlLibraryIndex"),
)
if mibBuilder.loadTexts:
    vtlLibraryEntry.setStatus("current")
_VtlLibraryIndex_Type = VtlLibraryIndexTC
_VtlLibraryIndex_Object = MibTableColumn
vtlLibraryIndex = _VtlLibraryIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 1, 1, 1, 1),
    _VtlLibraryIndex_Type()
)
vtlLibraryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vtlLibraryIndex.setStatus("current")
_VtlLibraryName_Type = VtlLibraryNameTC
_VtlLibraryName_Object = MibTableColumn
vtlLibraryName = _VtlLibraryName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 1, 1, 1, 2),
    _VtlLibraryName_Type()
)
vtlLibraryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlLibraryName.setStatus("current")
_VtlLibraryVendor_Type = VtlLibraryVendorTC
_VtlLibraryVendor_Object = MibTableColumn
vtlLibraryVendor = _VtlLibraryVendor_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 1, 1, 1, 3),
    _VtlLibraryVendor_Type()
)
vtlLibraryVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlLibraryVendor.setStatus("current")
_VtlLibraryModel_Type = VtlLibraryModelTC
_VtlLibraryModel_Object = MibTableColumn
vtlLibraryModel = _VtlLibraryModel_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 1, 1, 1, 4),
    _VtlLibraryModel_Type()
)
vtlLibraryModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlLibraryModel.setStatus("current")
_VtlLibraryRevision_Type = VtlLibraryRevisionTC
_VtlLibraryRevision_Object = MibTableColumn
vtlLibraryRevision = _VtlLibraryRevision_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 1, 1, 1, 5),
    _VtlLibraryRevision_Type()
)
vtlLibraryRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlLibraryRevision.setStatus("current")
_VtlLibrarySerial_Type = VtlLibrarySerialTC
_VtlLibrarySerial_Object = MibTableColumn
vtlLibrarySerial = _VtlLibrarySerial_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 1, 1, 1, 6),
    _VtlLibrarySerial_Type()
)
vtlLibrarySerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlLibrarySerial.setStatus("current")
_VtlLibraryTotalDrives_Type = VtlLibraryTotalDrivesTC
_VtlLibraryTotalDrives_Object = MibTableColumn
vtlLibraryTotalDrives = _VtlLibraryTotalDrives_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 1, 1, 1, 7),
    _VtlLibraryTotalDrives_Type()
)
vtlLibraryTotalDrives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlLibraryTotalDrives.setStatus("current")
_VtlLibraryTotalSlots_Type = VtlLibraryTotalSlotsTC
_VtlLibraryTotalSlots_Object = MibTableColumn
vtlLibraryTotalSlots = _VtlLibraryTotalSlots_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 1, 1, 1, 8),
    _VtlLibraryTotalSlots_Type()
)
vtlLibraryTotalSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlLibraryTotalSlots.setStatus("current")
_VtlLibraryTotalCaps_Type = VtlLibraryTotalCapsTC
_VtlLibraryTotalCaps_Object = MibTableColumn
vtlLibraryTotalCaps = _VtlLibraryTotalCaps_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 1, 1, 1, 9),
    _VtlLibraryTotalCaps_Type()
)
vtlLibraryTotalCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlLibraryTotalCaps.setStatus("current")
_VtlLibraryStatus_Type = VtlLibraryStatusTC
_VtlLibraryStatus_Object = MibTableColumn
vtlLibraryStatus = _VtlLibraryStatus_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 1, 1, 1, 10),
    _VtlLibraryStatus_Type()
)
vtlLibraryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlLibraryStatus.setStatus("current")
_VtlDrive_ObjectIdentity = ObjectIdentity
vtlDrive = _VtlDrive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 2)
)
_VtlDriveTable_Object = MibTable
vtlDriveTable = _VtlDriveTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 2, 1)
)
if mibBuilder.loadTexts:
    vtlDriveTable.setStatus("current")
_VtlDriveEntry_Object = MibTableRow
vtlDriveEntry = _VtlDriveEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 2, 1, 1)
)
vtlDriveEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "vtlDriveIndex"),
)
if mibBuilder.loadTexts:
    vtlDriveEntry.setStatus("current")
_VtlDriveIndex_Type = VtlDriveIndexTC
_VtlDriveIndex_Object = MibTableColumn
vtlDriveIndex = _VtlDriveIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 2, 1, 1, 1),
    _VtlDriveIndex_Type()
)
vtlDriveIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vtlDriveIndex.setStatus("current")
_VtlDriveName_Type = VtlDriveNameTC
_VtlDriveName_Object = MibTableColumn
vtlDriveName = _VtlDriveName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 2, 1, 1, 2),
    _VtlDriveName_Type()
)
vtlDriveName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlDriveName.setStatus("current")
_VtlDriveVendor_Type = VtlDriveVendorTC
_VtlDriveVendor_Object = MibTableColumn
vtlDriveVendor = _VtlDriveVendor_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 2, 1, 1, 3),
    _VtlDriveVendor_Type()
)
vtlDriveVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlDriveVendor.setStatus("current")
_VtlDriveModel_Type = VtlDriveModelTC
_VtlDriveModel_Object = MibTableColumn
vtlDriveModel = _VtlDriveModel_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 2, 1, 1, 4),
    _VtlDriveModel_Type()
)
vtlDriveModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlDriveModel.setStatus("current")
_VtlDriveRevision_Type = VtlDriveRevisionTC
_VtlDriveRevision_Object = MibTableColumn
vtlDriveRevision = _VtlDriveRevision_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 2, 1, 1, 5),
    _VtlDriveRevision_Type()
)
vtlDriveRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlDriveRevision.setStatus("current")
_VtlDriveSerial_Type = VtlDriveSerialTC
_VtlDriveSerial_Object = MibTableColumn
vtlDriveSerial = _VtlDriveSerial_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 2, 1, 1, 6),
    _VtlDriveSerial_Type()
)
vtlDriveSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlDriveSerial.setStatus("current")
_VtlDriveLibraryName_Type = VtlLibraryNameTC
_VtlDriveLibraryName_Object = MibTableColumn
vtlDriveLibraryName = _VtlDriveLibraryName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 2, 1, 1, 7),
    _VtlDriveLibraryName_Type()
)
vtlDriveLibraryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlDriveLibraryName.setStatus("current")
_VtlDriveStatus_Type = VtlDriveStatusTC
_VtlDriveStatus_Object = MibTableColumn
vtlDriveStatus = _VtlDriveStatus_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 2, 1, 1, 8),
    _VtlDriveStatus_Type()
)
vtlDriveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlDriveStatus.setStatus("current")
_VtlDriveTapeVolume_Type = VtlDriveTapeVolumeTC
_VtlDriveTapeVolume_Object = MibTableColumn
vtlDriveTapeVolume = _VtlDriveTapeVolume_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 2, 1, 1, 9),
    _VtlDriveTapeVolume_Type()
)
vtlDriveTapeVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlDriveTapeVolume.setStatus("current")
_VtlPort_ObjectIdentity = ObjectIdentity
vtlPort = _VtlPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 3)
)
_VtlPortTable_Object = MibTable
vtlPortTable = _VtlPortTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 3, 1)
)
if mibBuilder.loadTexts:
    vtlPortTable.setStatus("current")
_VtlPortEntry_Object = MibTableRow
vtlPortEntry = _VtlPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 3, 1, 1)
)
vtlPortEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "vtlPortIndex"),
)
if mibBuilder.loadTexts:
    vtlPortEntry.setStatus("current")
_VtlPortIndex_Type = VtlPortIndexTC
_VtlPortIndex_Object = MibTableColumn
vtlPortIndex = _VtlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 3, 1, 1, 1),
    _VtlPortIndex_Type()
)
vtlPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vtlPortIndex.setStatus("current")
_VtlPortName_Type = VtlPortNameTC
_VtlPortName_Object = MibTableColumn
vtlPortName = _VtlPortName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 3, 1, 1, 2),
    _VtlPortName_Type()
)
vtlPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlPortName.setStatus("current")
_VtlPortID_Type = VtlPortIDTC
_VtlPortID_Object = MibTableColumn
vtlPortID = _VtlPortID_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 3, 1, 1, 3),
    _VtlPortID_Type()
)
vtlPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlPortID.setStatus("current")
_VtlPortModel_Type = VtlPortModelTC
_VtlPortModel_Object = MibTableColumn
vtlPortModel = _VtlPortModel_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 3, 1, 1, 4),
    _VtlPortModel_Type()
)
vtlPortModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlPortModel.setStatus("current")
_VtlPortFirmware_Type = VtlPortFirmwareTC
_VtlPortFirmware_Object = MibTableColumn
vtlPortFirmware = _VtlPortFirmware_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 3, 1, 1, 5),
    _VtlPortFirmware_Type()
)
vtlPortFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlPortFirmware.setStatus("current")
_VtlPortWWNN_Type = VtlPortWWNNTC
_VtlPortWWNN_Object = MibTableColumn
vtlPortWWNN = _VtlPortWWNN_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 3, 1, 1, 6),
    _VtlPortWWNN_Type()
)
vtlPortWWNN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlPortWWNN.setStatus("current")
_VtlPortWWPN_Type = VtlPortWWPNTC
_VtlPortWWPN_Object = MibTableColumn
vtlPortWWPN = _VtlPortWWPN_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 3, 1, 1, 7),
    _VtlPortWWPN_Type()
)
vtlPortWWPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlPortWWPN.setStatus("current")
_VtlPortConnectionType_Type = VtlPortConnectionTypeTC
_VtlPortConnectionType_Object = MibTableColumn
vtlPortConnectionType = _VtlPortConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 3, 1, 1, 8),
    _VtlPortConnectionType_Type()
)
vtlPortConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlPortConnectionType.setStatus("current")
_VtlPortSpeed_Type = VtlPortSpeedTC
_VtlPortSpeed_Object = MibTableColumn
vtlPortSpeed = _VtlPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 3, 1, 1, 9),
    _VtlPortSpeed_Type()
)
vtlPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlPortSpeed.setStatus("current")
_VtlPortEnabled_Type = VtlPortEnabledTC
_VtlPortEnabled_Object = MibTableColumn
vtlPortEnabled = _VtlPortEnabled_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 3, 1, 1, 10),
    _VtlPortEnabled_Type()
)
vtlPortEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlPortEnabled.setStatus("current")
_VtlPortStatus_Type = VtlPortStatusTC
_VtlPortStatus_Object = MibTableColumn
vtlPortStatus = _VtlPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 3, 1, 1, 11),
    _VtlPortStatus_Type()
)
vtlPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlPortStatus.setStatus("current")
_VtlPortTrapIndex_Type = VtlPortIndexTC
_VtlPortTrapIndex_Object = MibTableColumn
vtlPortTrapIndex = _VtlPortTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 3, 1, 1, 12),
    _VtlPortTrapIndex_Type()
)
vtlPortTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlPortTrapIndex.setStatus("current")
_VtlTape_ObjectIdentity = ObjectIdentity
vtlTape = _VtlTape_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 4)
)
_VtlTapeTable_Object = MibTable
vtlTapeTable = _VtlTapeTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 4, 1)
)
if mibBuilder.loadTexts:
    vtlTapeTable.setStatus("current")
_VtlTapeEntry_Object = MibTableRow
vtlTapeEntry = _VtlTapeEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 4, 1, 1)
)
vtlTapeEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "vtlTapeIndex"),
)
if mibBuilder.loadTexts:
    vtlTapeEntry.setStatus("current")
_VtlTapeIndex_Type = VtlTapeIndexTC
_VtlTapeIndex_Object = MibTableColumn
vtlTapeIndex = _VtlTapeIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 4, 1, 1, 1),
    _VtlTapeIndex_Type()
)
vtlTapeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vtlTapeIndex.setStatus("current")
_VtlTapeBarCode_Type = VtlTapeBarCodeTC
_VtlTapeBarCode_Object = MibTableColumn
vtlTapeBarCode = _VtlTapeBarCode_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 4, 1, 1, 2),
    _VtlTapeBarCode_Type()
)
vtlTapeBarCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlTapeBarCode.setStatus("current")
_VtlTapePool_Type = VtlTapePoolTC
_VtlTapePool_Object = MibTableColumn
vtlTapePool = _VtlTapePool_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 4, 1, 1, 3),
    _VtlTapePool_Type()
)
vtlTapePool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlTapePool.setStatus("current")
_VtlTapeLocation_Type = VtlTapeLocationTC
_VtlTapeLocation_Object = MibTableColumn
vtlTapeLocation = _VtlTapeLocation_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 4, 1, 1, 4),
    _VtlTapeLocation_Type()
)
vtlTapeLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlTapeLocation.setStatus("current")
_VtlTapeState_Type = VtlTapeStateTC
_VtlTapeState_Object = MibTableColumn
vtlTapeState = _VtlTapeState_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 4, 1, 1, 5),
    _VtlTapeState_Type()
)
vtlTapeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlTapeState.setStatus("current")
_VtlTapeSize_Type = VtlTapeSizeTC
_VtlTapeSize_Object = MibTableColumn
vtlTapeSize = _VtlTapeSize_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 4, 1, 1, 6),
    _VtlTapeSize_Type()
)
vtlTapeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlTapeSize.setStatus("current")
_VtlTapeUsed_Type = VtlTapeUsedTC
_VtlTapeUsed_Object = MibTableColumn
vtlTapeUsed = _VtlTapeUsed_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 4, 1, 1, 7),
    _VtlTapeUsed_Type()
)
vtlTapeUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlTapeUsed.setStatus("current")
_VtlTapeComp_Type = VtlTapeCompTC
_VtlTapeComp_Object = MibTableColumn
vtlTapeComp = _VtlTapeComp_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 4, 1, 1, 8),
    _VtlTapeComp_Type()
)
vtlTapeComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlTapeComp.setStatus("current")
_VtlTapeModTime_Type = VtlTapeModTimeTC
_VtlTapeModTime_Object = MibTableColumn
vtlTapeModTime = _VtlTapeModTime_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 4, 1, 1, 9),
    _VtlTapeModTime_Type()
)
vtlTapeModTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlTapeModTime.setStatus("current")
_VtlPool_ObjectIdentity = ObjectIdentity
vtlPool = _VtlPool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 6)
)
_VtlPoolTable_Object = MibTable
vtlPoolTable = _VtlPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 6, 1)
)
if mibBuilder.loadTexts:
    vtlPoolTable.setStatus("current")
_VtlPoolEntry_Object = MibTableRow
vtlPoolEntry = _VtlPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 6, 1, 1)
)
vtlPoolEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "vtlPoolIndex"),
)
if mibBuilder.loadTexts:
    vtlPoolEntry.setStatus("current")
_VtlPoolIndex_Type = DDMibTableIndexTC
_VtlPoolIndex_Object = MibTableColumn
vtlPoolIndex = _VtlPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 6, 1, 1, 1),
    _VtlPoolIndex_Type()
)
vtlPoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vtlPoolIndex.setStatus("current")
_VtlPoolPool_Type = DDMibTableString64TC
_VtlPoolPool_Object = MibTableColumn
vtlPoolPool = _VtlPoolPool_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 6, 1, 1, 2),
    _VtlPoolPool_Type()
)
vtlPoolPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlPoolPool.setStatus("current")
_VtlPoolStatus_Type = DDMibTableString64TC
_VtlPoolStatus_Object = MibTableColumn
vtlPoolStatus = _VtlPoolStatus_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 6, 1, 1, 3),
    _VtlPoolStatus_Type()
)
vtlPoolStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlPoolStatus.setStatus("current")
_VtlPoolTapes_Type = DDMibTableString64TC
_VtlPoolTapes_Object = MibTableColumn
vtlPoolTapes = _VtlPoolTapes_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 6, 1, 1, 4),
    _VtlPoolTapes_Type()
)
vtlPoolTapes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlPoolTapes.setStatus("current")
_VtlPoolSize_Type = DDMibTableString64TC
_VtlPoolSize_Object = MibTableColumn
vtlPoolSize = _VtlPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 6, 1, 1, 5),
    _VtlPoolSize_Type()
)
vtlPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlPoolSize.setStatus("current")
_VtlPoolUsed_Type = DDMibTableString64TC
_VtlPoolUsed_Object = MibTableColumn
vtlPoolUsed = _VtlPoolUsed_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 6, 1, 1, 6),
    _VtlPoolUsed_Type()
)
vtlPoolUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlPoolUsed.setStatus("current")
_VtlPoolComp_Type = DDMibTableString64TC
_VtlPoolComp_Object = MibTableColumn
vtlPoolComp = _VtlPoolComp_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 6, 1, 1, 7),
    _VtlPoolComp_Type()
)
vtlPoolComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlPoolComp.setStatus("current")
_VtlGroups_ObjectIdentity = ObjectIdentity
vtlGroups = _VtlGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7)
)
_VtlGroupTable_Object = MibTable
vtlGroupTable = _VtlGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7, 1)
)
if mibBuilder.loadTexts:
    vtlGroupTable.setStatus("current")
_VtlGroupEntry_Object = MibTableRow
vtlGroupEntry = _VtlGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7, 1, 1)
)
vtlGroupEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "vtlGroupIndex"),
)
if mibBuilder.loadTexts:
    vtlGroupEntry.setStatus("current")
_VtlGroupIndex_Type = DDMibTableIndexTC
_VtlGroupIndex_Object = MibTableColumn
vtlGroupIndex = _VtlGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7, 1, 1, 1),
    _VtlGroupIndex_Type()
)
vtlGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vtlGroupIndex.setStatus("current")
_VtlGroupName_Type = DDMibTableString32TC
_VtlGroupName_Object = MibTableColumn
vtlGroupName = _VtlGroupName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7, 1, 1, 2),
    _VtlGroupName_Type()
)
vtlGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlGroupName.setStatus("current")
_VtlGroupInitiaterCount_Type = DDMibInteger32TC
_VtlGroupInitiaterCount_Object = MibTableColumn
vtlGroupInitiaterCount = _VtlGroupInitiaterCount_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7, 1, 1, 3),
    _VtlGroupInitiaterCount_Type()
)
vtlGroupInitiaterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlGroupInitiaterCount.setStatus("current")
_VtlGroupDeviceCount_Type = DDMibInteger32TC
_VtlGroupDeviceCount_Object = MibTableColumn
vtlGroupDeviceCount = _VtlGroupDeviceCount_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7, 1, 1, 4),
    _VtlGroupDeviceCount_Type()
)
vtlGroupDeviceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlGroupDeviceCount.setStatus("current")
_VtlGroupDeviceTable_Object = MibTable
vtlGroupDeviceTable = _VtlGroupDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7, 2)
)
if mibBuilder.loadTexts:
    vtlGroupDeviceTable.setStatus("current")
_VtlGroupDeviceEntry_Object = MibTableRow
vtlGroupDeviceEntry = _VtlGroupDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7, 2, 1)
)
vtlGroupDeviceEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "vtlGroupIndex"),
    (0, "DATA-DOMAIN-MIB", "vtlGroupDeviceIndex"),
)
if mibBuilder.loadTexts:
    vtlGroupDeviceEntry.setStatus("current")
_VtlGroupDeviceIndex_Type = DDMibTableIndexTC
_VtlGroupDeviceIndex_Object = MibTableColumn
vtlGroupDeviceIndex = _VtlGroupDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7, 2, 1, 2),
    _VtlGroupDeviceIndex_Type()
)
vtlGroupDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vtlGroupDeviceIndex.setStatus("current")
_VtlGroupDeviceGroupName_Type = DDMibTableString256TC
_VtlGroupDeviceGroupName_Object = MibTableColumn
vtlGroupDeviceGroupName = _VtlGroupDeviceGroupName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7, 2, 1, 3),
    _VtlGroupDeviceGroupName_Type()
)
vtlGroupDeviceGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlGroupDeviceGroupName.setStatus("current")
_VtlGroupDeviceDeviceName_Type = DDMibTableString256TC
_VtlGroupDeviceDeviceName_Object = MibTableColumn
vtlGroupDeviceDeviceName = _VtlGroupDeviceDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7, 2, 1, 4),
    _VtlGroupDeviceDeviceName_Type()
)
vtlGroupDeviceDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlGroupDeviceDeviceName.setStatus("current")
_VtlGroupDeviceLun_Type = DDMibInteger32TC
_VtlGroupDeviceLun_Object = MibTableColumn
vtlGroupDeviceLun = _VtlGroupDeviceLun_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7, 2, 1, 5),
    _VtlGroupDeviceLun_Type()
)
vtlGroupDeviceLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlGroupDeviceLun.setStatus("current")
_VtlGroupDevicePrimaryPorts_Type = DDMibTableString64TC
_VtlGroupDevicePrimaryPorts_Object = MibTableColumn
vtlGroupDevicePrimaryPorts = _VtlGroupDevicePrimaryPorts_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7, 2, 1, 6),
    _VtlGroupDevicePrimaryPorts_Type()
)
vtlGroupDevicePrimaryPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlGroupDevicePrimaryPorts.setStatus("current")
_VtlGroupDeviceSecondaryPorts_Type = DDMibTableString64TC
_VtlGroupDeviceSecondaryPorts_Object = MibTableColumn
vtlGroupDeviceSecondaryPorts = _VtlGroupDeviceSecondaryPorts_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7, 2, 1, 7),
    _VtlGroupDeviceSecondaryPorts_Type()
)
vtlGroupDeviceSecondaryPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlGroupDeviceSecondaryPorts.setStatus("current")
_VtlGroupDeviceInUsePorts_Type = DDMibTableString64TC
_VtlGroupDeviceInUsePorts_Object = MibTableColumn
vtlGroupDeviceInUsePorts = _VtlGroupDeviceInUsePorts_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7, 2, 1, 8),
    _VtlGroupDeviceInUsePorts_Type()
)
vtlGroupDeviceInUsePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlGroupDeviceInUsePorts.setStatus("current")
_VtlInitiator_ObjectIdentity = ObjectIdentity
vtlInitiator = _VtlInitiator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 8)
)
_VtlInitiatorTable_Object = MibTable
vtlInitiatorTable = _VtlInitiatorTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 8, 1)
)
if mibBuilder.loadTexts:
    vtlInitiatorTable.setStatus("current")
_VtlInitiatorEntry_Object = MibTableRow
vtlInitiatorEntry = _VtlInitiatorEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 8, 1, 1)
)
vtlInitiatorEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "vtlInitiatorIndex"),
)
if mibBuilder.loadTexts:
    vtlInitiatorEntry.setStatus("current")
_VtlInitiatorIndex_Type = DDMibTableIndexTC
_VtlInitiatorIndex_Object = MibTableColumn
vtlInitiatorIndex = _VtlInitiatorIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 8, 1, 1, 1),
    _VtlInitiatorIndex_Type()
)
vtlInitiatorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vtlInitiatorIndex.setStatus("current")
_VtlInitiatorName_Type = DDMibTableString32TC
_VtlInitiatorName_Object = MibTableColumn
vtlInitiatorName = _VtlInitiatorName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 8, 1, 1, 2),
    _VtlInitiatorName_Type()
)
vtlInitiatorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlInitiatorName.setStatus("current")
_VtlInitiatorStatus_Type = DDMibTableString32TC
_VtlInitiatorStatus_Object = MibTableColumn
vtlInitiatorStatus = _VtlInitiatorStatus_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 8, 1, 1, 3),
    _VtlInitiatorStatus_Type()
)
vtlInitiatorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlInitiatorStatus.setStatus("current")
_VtlInitiatorGroup_Type = DDMibTableString32TC
_VtlInitiatorGroup_Object = MibTableColumn
vtlInitiatorGroup = _VtlInitiatorGroup_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 8, 1, 1, 4),
    _VtlInitiatorGroup_Type()
)
vtlInitiatorGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlInitiatorGroup.setStatus("current")
_VtlInitiatorWWNN_Type = DDMibTableString64TC
_VtlInitiatorWWNN_Object = MibTableColumn
vtlInitiatorWWNN = _VtlInitiatorWWNN_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 8, 1, 1, 5),
    _VtlInitiatorWWNN_Type()
)
vtlInitiatorWWNN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlInitiatorWWNN.setStatus("current")
_VtlInitiatorWWPN_Type = DDMibTableString64TC
_VtlInitiatorWWPN_Object = MibTableColumn
vtlInitiatorWWPN = _VtlInitiatorWWPN_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 8, 1, 1, 6),
    _VtlInitiatorWWPN_Type()
)
vtlInitiatorWWPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlInitiatorWWPN.setStatus("current")
_VtlInitiatorPort_Type = DDMibTableString32TC
_VtlInitiatorPort_Object = MibTableColumn
vtlInitiatorPort = _VtlInitiatorPort_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 8, 1, 1, 7),
    _VtlInitiatorPort_Type()
)
vtlInitiatorPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlInitiatorPort.setStatus("current")
_VtlStats_ObjectIdentity = ObjectIdentity
vtlStats = _VtlStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 3)
)
_VtlStatsTable_Object = MibTable
vtlStatsTable = _VtlStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1)
)
if mibBuilder.loadTexts:
    vtlStatsTable.setStatus("current")
_VtlStatsEntry_Object = MibTableRow
vtlStatsEntry = _VtlStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1, 1)
)
vtlStatsEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "vtlStatsIndex"),
)
if mibBuilder.loadTexts:
    vtlStatsEntry.setStatus("current")
_VtlStatsIndex_Type = VtlStatsIndexTC
_VtlStatsIndex_Object = MibTableColumn
vtlStatsIndex = _VtlStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1, 1, 1),
    _VtlStatsIndex_Type()
)
vtlStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vtlStatsIndex.setStatus("current")
_VtlStatsPort_Type = VtlStatsPortTC
_VtlStatsPort_Object = MibTableColumn
vtlStatsPort = _VtlStatsPort_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1, 1, 2),
    _VtlStatsPort_Type()
)
vtlStatsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlStatsPort.setStatus("current")
_VtlStatsConrolCommands_Type = VtlStatsConrolCommandsTC
_VtlStatsConrolCommands_Object = MibTableColumn
vtlStatsConrolCommands = _VtlStatsConrolCommands_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1, 1, 3),
    _VtlStatsConrolCommands_Type()
)
vtlStatsConrolCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlStatsConrolCommands.setStatus("current")
_VtlStatsWriteCommands_Type = VtlStatsWriteCommandsTC
_VtlStatsWriteCommands_Object = MibTableColumn
vtlStatsWriteCommands = _VtlStatsWriteCommands_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1, 1, 4),
    _VtlStatsWriteCommands_Type()
)
vtlStatsWriteCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlStatsWriteCommands.setStatus("current")
_VtlStatsReadCommands_Type = VtlStatsReadCommandsTC
_VtlStatsReadCommands_Object = MibTableColumn
vtlStatsReadCommands = _VtlStatsReadCommands_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1, 1, 5),
    _VtlStatsReadCommands_Type()
)
vtlStatsReadCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlStatsReadCommands.setStatus("current")
_VtlStatsIn_Type = VtlStatsInTC
_VtlStatsIn_Object = MibTableColumn
vtlStatsIn = _VtlStatsIn_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1, 1, 6),
    _VtlStatsIn_Type()
)
vtlStatsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlStatsIn.setStatus("current")
_VtlStatsOut_Type = VtlStatsOutTC
_VtlStatsOut_Object = MibTableColumn
vtlStatsOut = _VtlStatsOut_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1, 1, 7),
    _VtlStatsOut_Type()
)
vtlStatsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlStatsOut.setStatus("current")
_VtlStatsLinkFailures_Type = VtlStatsLinkFailuresTC
_VtlStatsLinkFailures_Object = MibTableColumn
vtlStatsLinkFailures = _VtlStatsLinkFailures_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1, 1, 8),
    _VtlStatsLinkFailures_Type()
)
vtlStatsLinkFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlStatsLinkFailures.setStatus("current")
_VtlStatsLIPCount_Type = VtlStatsLIPCountTC
_VtlStatsLIPCount_Object = MibTableColumn
vtlStatsLIPCount = _VtlStatsLIPCount_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1, 1, 9),
    _VtlStatsLIPCount_Type()
)
vtlStatsLIPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlStatsLIPCount.setStatus("current")
_VtlStatsSyncLosses_Type = VtlStatsSyncLossesTC
_VtlStatsSyncLosses_Object = MibTableColumn
vtlStatsSyncLosses = _VtlStatsSyncLosses_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1, 1, 10),
    _VtlStatsSyncLosses_Type()
)
vtlStatsSyncLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlStatsSyncLosses.setStatus("current")
_VtlStatsSignalLosses_Type = VtlStatsSignalLossesTC
_VtlStatsSignalLosses_Object = MibTableColumn
vtlStatsSignalLosses = _VtlStatsSignalLosses_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1, 1, 11),
    _VtlStatsSignalLosses_Type()
)
vtlStatsSignalLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlStatsSignalLosses.setStatus("current")
_VtlStatsPrimSeqProtoErrors_Type = VtlStatsPrimSeqProtoErrorsTC
_VtlStatsPrimSeqProtoErrors_Object = MibTableColumn
vtlStatsPrimSeqProtoErrors = _VtlStatsPrimSeqProtoErrors_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1, 1, 12),
    _VtlStatsPrimSeqProtoErrors_Type()
)
vtlStatsPrimSeqProtoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlStatsPrimSeqProtoErrors.setStatus("current")
_VtlStatsInvalidTxWords_Type = VtlStatsInvalidTxWordsTC
_VtlStatsInvalidTxWords_Object = MibTableColumn
vtlStatsInvalidTxWords = _VtlStatsInvalidTxWords_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1, 1, 13),
    _VtlStatsInvalidTxWords_Type()
)
vtlStatsInvalidTxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlStatsInvalidTxWords.setStatus("current")
_VtlStatsInvalidCRCs_Type = VtlStatsInvalidCRCsTC
_VtlStatsInvalidCRCs_Object = MibTableColumn
vtlStatsInvalidCRCs = _VtlStatsInvalidCRCs_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1, 1, 14),
    _VtlStatsInvalidCRCs_Type()
)
vtlStatsInvalidCRCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtlStatsInvalidCRCs.setStatus("current")
_Ddboost_ObjectIdentity = ObjectIdentity
ddboost = _Ddboost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12)
)
_DdboostProperties_ObjectIdentity = ObjectIdentity
ddboostProperties = _DdboostProperties_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 1)
)
_DdboostStatus_Type = DDboostStatusTC
_DdboostStatus_Object = MibScalar
ddboostStatus = _DdboostStatus_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 1, 1),
    _DdboostStatus_Type()
)
ddboostStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostStatus.setStatus("current")
_DdboostUser_Type = DDboostUserTC
_DdboostUser_Object = MibScalar
ddboostUser = _DdboostUser_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 1, 2),
    _DdboostUser_Type()
)
ddboostUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostUser.setStatus("deprecated")
_DdboostIfGroupStatus_Type = DDMibStatusTC
_DdboostIfGroupStatus_Object = MibScalar
ddboostIfGroupStatus = _DdboostIfGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 1, 3),
    _DdboostIfGroupStatus_Type()
)
ddboostIfGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostIfGroupStatus.setStatus("deprecated")
_DdboostUserTable_Object = MibTable
ddboostUserTable = _DdboostUserTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 1, 4)
)
if mibBuilder.loadTexts:
    ddboostUserTable.setStatus("current")
_DdboostUserEntry_Object = MibTableRow
ddboostUserEntry = _DdboostUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 1, 4, 1)
)
ddboostUserEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "ddboostUserIdx"),
)
if mibBuilder.loadTexts:
    ddboostUserEntry.setStatus("current")
_DdboostUserIdx_Type = DDboostStatsIndexTC
_DdboostUserIdx_Object = MibTableColumn
ddboostUserIdx = _DdboostUserIdx_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 1, 4, 1, 1),
    _DdboostUserIdx_Type()
)
ddboostUserIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ddboostUserIdx.setStatus("current")
_DdboostUserName_Type = DDMibTableString256TC
_DdboostUserName_Object = MibTableColumn
ddboostUserName = _DdboostUserName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 1, 4, 1, 2),
    _DdboostUserName_Type()
)
ddboostUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostUserName.setStatus("current")
_DdboostUserDefaultTenantUnit_Type = DDMibTableString256TC
_DdboostUserDefaultTenantUnit_Object = MibTableColumn
ddboostUserDefaultTenantUnit = _DdboostUserDefaultTenantUnit_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 1, 4, 1, 3),
    _DdboostUserDefaultTenantUnit_Type()
)
ddboostUserDefaultTenantUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostUserDefaultTenantUnit.setStatus("current")
_DdboostIfGroupTable_Object = MibTable
ddboostIfGroupTable = _DdboostIfGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 1, 5)
)
if mibBuilder.loadTexts:
    ddboostIfGroupTable.setStatus("current")
_DdboostIfGroupEntry_Object = MibTableRow
ddboostIfGroupEntry = _DdboostIfGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 1, 5, 1)
)
ddboostIfGroupEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "ddboostIfGroupIdx"),
)
if mibBuilder.loadTexts:
    ddboostIfGroupEntry.setStatus("current")
_DdboostIfGroupIdx_Type = DDboostStatsIndexTC
_DdboostIfGroupIdx_Object = MibTableColumn
ddboostIfGroupIdx = _DdboostIfGroupIdx_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 1, 5, 1, 1),
    _DdboostIfGroupIdx_Type()
)
ddboostIfGroupIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ddboostIfGroupIdx.setStatus("current")
_DdboostIfGroupName_Type = DDMibTableString256TC
_DdboostIfGroupName_Object = MibTableColumn
ddboostIfGroupName = _DdboostIfGroupName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 1, 5, 1, 2),
    _DdboostIfGroupName_Type()
)
ddboostIfGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostIfGroupName.setStatus("current")
_DdboostIfGroupCurrentStatus_Type = DDMibStatusTC
_DdboostIfGroupCurrentStatus_Object = MibTableColumn
ddboostIfGroupCurrentStatus = _DdboostIfGroupCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 1, 5, 1, 3),
    _DdboostIfGroupCurrentStatus_Type()
)
ddboostIfGroupCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostIfGroupCurrentStatus.setStatus("current")
_DdboostStats_ObjectIdentity = ObjectIdentity
ddboostStats = _DdboostStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 2)
)
_DdboostStatsTable_Object = MibTable
ddboostStatsTable = _DdboostStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1)
)
if mibBuilder.loadTexts:
    ddboostStatsTable.setStatus("current")
_DdboostStatsEntry_Object = MibTableRow
ddboostStatsEntry = _DdboostStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1)
)
ddboostStatsEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "ddboostStatsIndex"),
)
if mibBuilder.loadTexts:
    ddboostStatsEntry.setStatus("current")
_DdboostStatsIndex_Type = DDboostStatsIndexTC
_DdboostStatsIndex_Object = MibTableColumn
ddboostStatsIndex = _DdboostStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 1),
    _DdboostStatsIndex_Type()
)
ddboostStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ddboostStatsIndex.setStatus("current")
_DdboostPreCompKBytesPerSecond_Type = KBytesPerSecond
_DdboostPreCompKBytesPerSecond_Object = MibTableColumn
ddboostPreCompKBytesPerSecond = _DdboostPreCompKBytesPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 2),
    _DdboostPreCompKBytesPerSecond_Type()
)
ddboostPreCompKBytesPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostPreCompKBytesPerSecond.setStatus("current")
_DdboostPostCompKBytesPerSecond_Type = KBytesPerSecond
_DdboostPostCompKBytesPerSecond_Object = MibTableColumn
ddboostPostCompKBytesPerSecond = _DdboostPostCompKBytesPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 3),
    _DdboostPostCompKBytesPerSecond_Type()
)
ddboostPostCompKBytesPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostPostCompKBytesPerSecond.setStatus("current")
_DdboostNetworkKBytesPerSecond_Type = KBytesPerSecond
_DdboostNetworkKBytesPerSecond_Object = MibTableColumn
ddboostNetworkKBytesPerSecond = _DdboostNetworkKBytesPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 4),
    _DdboostNetworkKBytesPerSecond_Type()
)
ddboostNetworkKBytesPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostNetworkKBytesPerSecond.setStatus("current")
_DdboostReadKBytesPerSecond_Type = KBytesPerSecond
_DdboostReadKBytesPerSecond_Object = MibTableColumn
ddboostReadKBytesPerSecond = _DdboostReadKBytesPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 5),
    _DdboostReadKBytesPerSecond_Type()
)
ddboostReadKBytesPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostReadKBytesPerSecond.setStatus("current")
_DdboostStatsBackupConn_Type = Counter64
_DdboostStatsBackupConn_Object = MibTableColumn
ddboostStatsBackupConn = _DdboostStatsBackupConn_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 6),
    _DdboostStatsBackupConn_Type()
)
ddboostStatsBackupConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostStatsBackupConn.setStatus("current")
_DdboostStatsRestoreConn_Type = Counter64
_DdboostStatsRestoreConn_Object = MibTableColumn
ddboostStatsRestoreConn = _DdboostStatsRestoreConn_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 7),
    _DdboostStatsRestoreConn_Type()
)
ddboostStatsRestoreConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostStatsRestoreConn.setStatus("current")
_DdboostStatsImageCreatesCount_Type = Counter64
_DdboostStatsImageCreatesCount_Object = MibTableColumn
ddboostStatsImageCreatesCount = _DdboostStatsImageCreatesCount_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 8),
    _DdboostStatsImageCreatesCount_Type()
)
ddboostStatsImageCreatesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostStatsImageCreatesCount.setStatus("current")
_DdboostStatsImageCreatesErrors_Type = Counter64
_DdboostStatsImageCreatesErrors_Object = MibTableColumn
ddboostStatsImageCreatesErrors = _DdboostStatsImageCreatesErrors_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 9),
    _DdboostStatsImageCreatesErrors_Type()
)
ddboostStatsImageCreatesErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostStatsImageCreatesErrors.setStatus("current")
_DdboostStatsImageDeletesCount_Type = Counter64
_DdboostStatsImageDeletesCount_Object = MibTableColumn
ddboostStatsImageDeletesCount = _DdboostStatsImageDeletesCount_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 10),
    _DdboostStatsImageDeletesCount_Type()
)
ddboostStatsImageDeletesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostStatsImageDeletesCount.setStatus("current")
_DdboostStatsImageDeletesErrors_Type = Counter64
_DdboostStatsImageDeletesErrors_Object = MibTableColumn
ddboostStatsImageDeletesErrors = _DdboostStatsImageDeletesErrors_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 11),
    _DdboostStatsImageDeletesErrors_Type()
)
ddboostStatsImageDeletesErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostStatsImageDeletesErrors.setStatus("current")
_DdboostStatsPrecompBytesReceived_Type = DDMibTrafficBytesTC
_DdboostStatsPrecompBytesReceived_Object = MibTableColumn
ddboostStatsPrecompBytesReceived = _DdboostStatsPrecompBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 12),
    _DdboostStatsPrecompBytesReceived_Type()
)
ddboostStatsPrecompBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostStatsPrecompBytesReceived.setStatus("current")
_DdboostStatsBytesAfterFiltering_Type = DDMibTrafficBytesTC
_DdboostStatsBytesAfterFiltering_Object = MibTableColumn
ddboostStatsBytesAfterFiltering = _DdboostStatsBytesAfterFiltering_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 13),
    _DdboostStatsBytesAfterFiltering_Type()
)
ddboostStatsBytesAfterFiltering.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostStatsBytesAfterFiltering.setStatus("current")
_DdboostStatsBytesAfterLc_Type = DDMibTrafficBytesTC
_DdboostStatsBytesAfterLc_Object = MibTableColumn
ddboostStatsBytesAfterLc = _DdboostStatsBytesAfterLc_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 14),
    _DdboostStatsBytesAfterLc_Type()
)
ddboostStatsBytesAfterLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostStatsBytesAfterLc.setStatus("current")
_DdboostStatsNetworkBytesReceived_Type = DDMibTrafficBytesTC
_DdboostStatsNetworkBytesReceived_Object = MibTableColumn
ddboostStatsNetworkBytesReceived = _DdboostStatsNetworkBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 15),
    _DdboostStatsNetworkBytesReceived_Type()
)
ddboostStatsNetworkBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostStatsNetworkBytesReceived.setStatus("current")
_DdboostStatsCompressionRatio_Type = DDMibTableString32TC
_DdboostStatsCompressionRatio_Object = MibTableColumn
ddboostStatsCompressionRatio = _DdboostStatsCompressionRatio_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 16),
    _DdboostStatsCompressionRatio_Type()
)
ddboostStatsCompressionRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostStatsCompressionRatio.setStatus("current")
_DdboostStatsTotalBytesReadCount_Type = DDMibTrafficBytesTC
_DdboostStatsTotalBytesReadCount_Object = MibTableColumn
ddboostStatsTotalBytesReadCount = _DdboostStatsTotalBytesReadCount_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 17),
    _DdboostStatsTotalBytesReadCount_Type()
)
ddboostStatsTotalBytesReadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostStatsTotalBytesReadCount.setStatus("current")
_DdboostStatsTotalBytesReadErrors_Type = DDMibTrafficBytesTC
_DdboostStatsTotalBytesReadErrors_Object = MibTableColumn
ddboostStatsTotalBytesReadErrors = _DdboostStatsTotalBytesReadErrors_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 18),
    _DdboostStatsTotalBytesReadErrors_Type()
)
ddboostStatsTotalBytesReadErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostStatsTotalBytesReadErrors.setStatus("current")
_DdboostConnections_ObjectIdentity = ObjectIdentity
ddboostConnections = _DdboostConnections_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 3)
)
_DdboostConnectionsTable_Object = MibTable
ddboostConnectionsTable = _DdboostConnectionsTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 3, 1)
)
if mibBuilder.loadTexts:
    ddboostConnectionsTable.setStatus("current")
_DdboostConnectionsEntry_Object = MibTableRow
ddboostConnectionsEntry = _DdboostConnectionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 3, 1, 1)
)
ddboostConnectionsEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "ddboostConnectionsIndex"),
)
if mibBuilder.loadTexts:
    ddboostConnectionsEntry.setStatus("current")
_DdboostConnectionsIndex_Type = DDMibTableIndexTC
_DdboostConnectionsIndex_Object = MibTableColumn
ddboostConnectionsIndex = _DdboostConnectionsIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 3, 1, 1, 1),
    _DdboostConnectionsIndex_Type()
)
ddboostConnectionsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ddboostConnectionsIndex.setStatus("current")
_DdboostInterface_Type = DDMibTableString64TC
_DdboostInterface_Object = MibTableColumn
ddboostInterface = _DdboostInterface_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 3, 1, 1, 2),
    _DdboostInterface_Type()
)
ddboostInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostInterface.setStatus("current")
_DdboostifGroupMember_Type = DDMibTableEnabledTC
_DdboostifGroupMember_Object = MibTableColumn
ddboostifGroupMember = _DdboostifGroupMember_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 3, 1, 1, 3),
    _DdboostifGroupMember_Type()
)
ddboostifGroupMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostifGroupMember.setStatus("current")
_DdboostBackupConnections_Type = DDMibInteger32TC
_DdboostBackupConnections_Object = MibTableColumn
ddboostBackupConnections = _DdboostBackupConnections_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 3, 1, 1, 4),
    _DdboostBackupConnections_Type()
)
ddboostBackupConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostBackupConnections.setStatus("current")
_DdboostRestoreConnections_Type = DDMibInteger32TC
_DdboostRestoreConnections_Object = MibTableColumn
ddboostRestoreConnections = _DdboostRestoreConnections_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 3, 1, 1, 5),
    _DdboostRestoreConnections_Type()
)
ddboostRestoreConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostRestoreConnections.setStatus("current")
_DdboostControlConnections_Type = DDMibInteger32TC
_DdboostControlConnections_Object = MibTableColumn
ddboostControlConnections = _DdboostControlConnections_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 3, 1, 1, 6),
    _DdboostControlConnections_Type()
)
ddboostControlConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostControlConnections.setStatus("current")
_DdboostTotalConnections_Type = DDMibInteger32TC
_DdboostTotalConnections_Object = MibTableColumn
ddboostTotalConnections = _DdboostTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 3, 1, 1, 7),
    _DdboostTotalConnections_Type()
)
ddboostTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostTotalConnections.setStatus("current")
_DdboostStorageUnit_ObjectIdentity = ObjectIdentity
ddboostStorageUnit = _DdboostStorageUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 4)
)
_DdboostStorageUnitTable_Object = MibTable
ddboostStorageUnitTable = _DdboostStorageUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 4, 1)
)
if mibBuilder.loadTexts:
    ddboostStorageUnitTable.setStatus("current")
_DdboostStorageUnitEntry_Object = MibTableRow
ddboostStorageUnitEntry = _DdboostStorageUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 4, 1, 1)
)
ddboostStorageUnitEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "ddboostStorageUnitIndex"),
)
if mibBuilder.loadTexts:
    ddboostStorageUnitEntry.setStatus("current")
_DdboostStorageUnitIndex_Type = DDMibTableIndexTC
_DdboostStorageUnitIndex_Object = MibTableColumn
ddboostStorageUnitIndex = _DdboostStorageUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 4, 1, 1, 1),
    _DdboostStorageUnitIndex_Type()
)
ddboostStorageUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ddboostStorageUnitIndex.setStatus("current")
_DdboostStorageUnitName_Type = DDMibTableString64TC
_DdboostStorageUnitName_Object = MibTableColumn
ddboostStorageUnitName = _DdboostStorageUnitName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 4, 1, 1, 2),
    _DdboostStorageUnitName_Type()
)
ddboostStorageUnitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostStorageUnitName.setStatus("current")
_DdboostStorageUnitBytes_Type = DDMibInteger32TC
_DdboostStorageUnitBytes_Object = MibTableColumn
ddboostStorageUnitBytes = _DdboostStorageUnitBytes_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 4, 1, 1, 3),
    _DdboostStorageUnitBytes_Type()
)
ddboostStorageUnitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostStorageUnitBytes.setStatus("current")
_DdboostStorageUnitGlobalComp_Type = DDMibInteger32TC
_DdboostStorageUnitGlobalComp_Object = MibTableColumn
ddboostStorageUnitGlobalComp = _DdboostStorageUnitGlobalComp_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 4, 1, 1, 4),
    _DdboostStorageUnitGlobalComp_Type()
)
ddboostStorageUnitGlobalComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostStorageUnitGlobalComp.setStatus("current")
_DdboostStorageUnitLocalComp_Type = DDMibInteger32TC
_DdboostStorageUnitLocalComp_Object = MibTableColumn
ddboostStorageUnitLocalComp = _DdboostStorageUnitLocalComp_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 4, 1, 1, 5),
    _DdboostStorageUnitLocalComp_Type()
)
ddboostStorageUnitLocalComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostStorageUnitLocalComp.setStatus("current")
_DdboostStorageUnitMetaData_Type = DDMibInteger32TC
_DdboostStorageUnitMetaData_Object = MibTableColumn
ddboostStorageUnitMetaData = _DdboostStorageUnitMetaData_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 4, 1, 1, 6),
    _DdboostStorageUnitMetaData_Type()
)
ddboostStorageUnitMetaData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostStorageUnitMetaData.setStatus("current")
_DdboostStorageUnitStatus_Type = DDMibTableString64TC
_DdboostStorageUnitStatus_Object = MibTableColumn
ddboostStorageUnitStatus = _DdboostStorageUnitStatus_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 4, 1, 1, 7),
    _DdboostStorageUnitStatus_Type()
)
ddboostStorageUnitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostStorageUnitStatus.setStatus("current")
_DdboostStorageUnitPreComp_Type = DDMibTableString64TC
_DdboostStorageUnitPreComp_Object = MibTableColumn
ddboostStorageUnitPreComp = _DdboostStorageUnitPreComp_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 4, 1, 1, 8),
    _DdboostStorageUnitPreComp_Type()
)
ddboostStorageUnitPreComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostStorageUnitPreComp.setStatus("current")
_DdboostStorageUnitUser_Type = DDMibTableString64TC
_DdboostStorageUnitUser_Object = MibTableColumn
ddboostStorageUnitUser = _DdboostStorageUnitUser_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 4, 1, 1, 9),
    _DdboostStorageUnitUser_Type()
)
ddboostStorageUnitUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostStorageUnitUser.setStatus("current")
_DdboostStorageUnitReportPhysicalSize_Type = DDMibInteger32TC
_DdboostStorageUnitReportPhysicalSize_Object = MibTableColumn
ddboostStorageUnitReportPhysicalSize = _DdboostStorageUnitReportPhysicalSize_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 4, 1, 1, 10),
    _DdboostStorageUnitReportPhysicalSize_Type()
)
ddboostStorageUnitReportPhysicalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostStorageUnitReportPhysicalSize.setStatus("current")
_DdboostFileReplicationStats_ObjectIdentity = ObjectIdentity
ddboostFileReplicationStats = _DdboostFileReplicationStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 5)
)
_DdboostFileReplicationStatsTable_Object = MibTable
ddboostFileReplicationStatsTable = _DdboostFileReplicationStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 5, 1)
)
if mibBuilder.loadTexts:
    ddboostFileReplicationStatsTable.setStatus("current")
_DdboostFileReplicationStatsEntry_Object = MibTableRow
ddboostFileReplicationStatsEntry = _DdboostFileReplicationStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 5, 1, 1)
)
ddboostFileReplicationStatsEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "ddboostFileReplStatsIndex"),
)
if mibBuilder.loadTexts:
    ddboostFileReplicationStatsEntry.setStatus("current")
_DdboostFileReplStatsIndex_Type = DDMibTableIndexTC
_DdboostFileReplStatsIndex_Object = MibTableColumn
ddboostFileReplStatsIndex = _DdboostFileReplStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 5, 1, 1, 1),
    _DdboostFileReplStatsIndex_Type()
)
ddboostFileReplStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ddboostFileReplStatsIndex.setStatus("current")
_DdboostFileReplStatsDirection_Type = DDMibTableString32TC
_DdboostFileReplStatsDirection_Object = MibTableColumn
ddboostFileReplStatsDirection = _DdboostFileReplStatsDirection_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 5, 1, 1, 2),
    _DdboostFileReplStatsDirection_Type()
)
ddboostFileReplStatsDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostFileReplStatsDirection.setStatus("current")
_DdboostFileReplStatsNetworkSent_Type = DDMibTrafficBytesTC
_DdboostFileReplStatsNetworkSent_Object = MibTableColumn
ddboostFileReplStatsNetworkSent = _DdboostFileReplStatsNetworkSent_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 5, 1, 1, 3),
    _DdboostFileReplStatsNetworkSent_Type()
)
ddboostFileReplStatsNetworkSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostFileReplStatsNetworkSent.setStatus("current")
_DdboostFileReplStatsPreCompSent_Type = DDMibTrafficBytesTC
_DdboostFileReplStatsPreCompSent_Object = MibTableColumn
ddboostFileReplStatsPreCompSent = _DdboostFileReplStatsPreCompSent_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 5, 1, 1, 4),
    _DdboostFileReplStatsPreCompSent_Type()
)
ddboostFileReplStatsPreCompSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostFileReplStatsPreCompSent.setStatus("current")
_DdboostFileReplStatsFiltered_Type = DDMibTrafficBytesTC
_DdboostFileReplStatsFiltered_Object = MibTableColumn
ddboostFileReplStatsFiltered = _DdboostFileReplStatsFiltered_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 5, 1, 1, 5),
    _DdboostFileReplStatsFiltered_Type()
)
ddboostFileReplStatsFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostFileReplStatsFiltered.setStatus("current")
_DdboostFileReplStatsLowBWOpt_Type = DDMibTrafficBytesTC
_DdboostFileReplStatsLowBWOpt_Object = MibTableColumn
ddboostFileReplStatsLowBWOpt = _DdboostFileReplStatsLowBWOpt_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 5, 1, 1, 6),
    _DdboostFileReplStatsLowBWOpt_Type()
)
ddboostFileReplStatsLowBWOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostFileReplStatsLowBWOpt.setStatus("current")
_DdboostFileReplStatsLocalComp_Type = DDMibTrafficBytesTC
_DdboostFileReplStatsLocalComp_Object = MibTableColumn
ddboostFileReplStatsLocalComp = _DdboostFileReplStatsLocalComp_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 5, 1, 1, 7),
    _DdboostFileReplStatsLocalComp_Type()
)
ddboostFileReplStatsLocalComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostFileReplStatsLocalComp.setStatus("current")
_DdboostFileReplStatsCompRatio_Type = DDMibTableString32TC
_DdboostFileReplStatsCompRatio_Object = MibTableColumn
ddboostFileReplStatsCompRatio = _DdboostFileReplStatsCompRatio_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 5, 1, 1, 8),
    _DdboostFileReplStatsCompRatio_Type()
)
ddboostFileReplStatsCompRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostFileReplStatsCompRatio.setStatus("current")
_DdboostFileReplicationHistory_ObjectIdentity = ObjectIdentity
ddboostFileReplicationHistory = _DdboostFileReplicationHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 6)
)
_DdboostFileReplicationHistoryTable_Object = MibTable
ddboostFileReplicationHistoryTable = _DdboostFileReplicationHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 6, 1)
)
if mibBuilder.loadTexts:
    ddboostFileReplicationHistoryTable.setStatus("current")
_DdboostFileReplicationHistoryEntry_Object = MibTableRow
ddboostFileReplicationHistoryEntry = _DdboostFileReplicationHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 6, 1, 1)
)
ddboostFileReplicationHistoryEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "ddboostFileReplHistoryIndex"),
)
if mibBuilder.loadTexts:
    ddboostFileReplicationHistoryEntry.setStatus("current")
_DdboostFileReplHistoryIndex_Type = DDMibTableIndexTC
_DdboostFileReplHistoryIndex_Object = MibTableColumn
ddboostFileReplHistoryIndex = _DdboostFileReplHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 6, 1, 1, 1),
    _DdboostFileReplHistoryIndex_Type()
)
ddboostFileReplHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ddboostFileReplHistoryIndex.setStatus("current")
_DdboostFileReplHistoryDirection_Type = DDMibTableString32TC
_DdboostFileReplHistoryDirection_Object = MibTableColumn
ddboostFileReplHistoryDirection = _DdboostFileReplHistoryDirection_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 6, 1, 1, 2),
    _DdboostFileReplHistoryDirection_Type()
)
ddboostFileReplHistoryDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostFileReplHistoryDirection.setStatus("current")
_DdboostFileReplHistoryNetwork_Type = DDMibTrafficBytesTC
_DdboostFileReplHistoryNetwork_Object = MibTableColumn
ddboostFileReplHistoryNetwork = _DdboostFileReplHistoryNetwork_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 6, 1, 1, 3),
    _DdboostFileReplHistoryNetwork_Type()
)
ddboostFileReplHistoryNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostFileReplHistoryNetwork.setStatus("current")
_DdboostFileReplHistoryPreComp_Type = DDMibTrafficBytesTC
_DdboostFileReplHistoryPreComp_Object = MibTableColumn
ddboostFileReplHistoryPreComp = _DdboostFileReplHistoryPreComp_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 6, 1, 1, 4),
    _DdboostFileReplHistoryPreComp_Type()
)
ddboostFileReplHistoryPreComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostFileReplHistoryPreComp.setStatus("current")
_DdboostFileReplHistoryPostComp_Type = DDMibTrafficBytesTC
_DdboostFileReplHistoryPostComp_Object = MibTableColumn
ddboostFileReplHistoryPostComp = _DdboostFileReplHistoryPostComp_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 6, 1, 1, 5),
    _DdboostFileReplHistoryPostComp_Type()
)
ddboostFileReplHistoryPostComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostFileReplHistoryPostComp.setStatus("current")
_DdboostFileReplHistoryLowBWOpt_Type = DDMibTableString32TC
_DdboostFileReplHistoryLowBWOpt_Object = MibTableColumn
ddboostFileReplHistoryLowBWOpt = _DdboostFileReplHistoryLowBWOpt_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 6, 1, 1, 6),
    _DdboostFileReplHistoryLowBWOpt_Type()
)
ddboostFileReplHistoryLowBWOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostFileReplHistoryLowBWOpt.setStatus("current")
_DdboostFileReplHistoryErrors_Type = DDMibTrafficBytesTC
_DdboostFileReplHistoryErrors_Object = MibTableColumn
ddboostFileReplHistoryErrors = _DdboostFileReplHistoryErrors_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 6, 1, 1, 7),
    _DdboostFileReplHistoryErrors_Type()
)
ddboostFileReplHistoryErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostFileReplHistoryErrors.setStatus("current")
_DdboostFileReplHistoryDate_Type = DDMibDateTC
_DdboostFileReplHistoryDate_Object = MibTableColumn
ddboostFileReplHistoryDate = _DdboostFileReplHistoryDate_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 6, 1, 1, 8),
    _DdboostFileReplHistoryDate_Type()
)
ddboostFileReplHistoryDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostFileReplHistoryDate.setStatus("current")
_DdboostFileReplHistoryTime_Type = DDMibDateTC
_DdboostFileReplHistoryTime_Object = MibTableColumn
ddboostFileReplHistoryTime = _DdboostFileReplHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 6, 1, 1, 9),
    _DdboostFileReplHistoryTime_Type()
)
ddboostFileReplHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostFileReplHistoryTime.setStatus("current")
_DdboostIfGroupConfig_ObjectIdentity = ObjectIdentity
ddboostIfGroupConfig = _DdboostIfGroupConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 7)
)
_DdboostIfGroupConfigTable_Object = MibTable
ddboostIfGroupConfigTable = _DdboostIfGroupConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 7, 1)
)
if mibBuilder.loadTexts:
    ddboostIfGroupConfigTable.setStatus("current")
_DdboostIfGroupConfigEntry_Object = MibTableRow
ddboostIfGroupConfigEntry = _DdboostIfGroupConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 7, 1, 1)
)
ddboostIfGroupConfigEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "ddboostIfGroupConfigIndex"),
)
if mibBuilder.loadTexts:
    ddboostIfGroupConfigEntry.setStatus("current")
_DdboostIfGroupConfigIndex_Type = DDMibTableIndexTC
_DdboostIfGroupConfigIndex_Object = MibTableColumn
ddboostIfGroupConfigIndex = _DdboostIfGroupConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 7, 1, 1, 1),
    _DdboostIfGroupConfigIndex_Type()
)
ddboostIfGroupConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ddboostIfGroupConfigIndex.setStatus("current")
_DdboostIfGroupInterface_Type = DDMibTableString64TC
_DdboostIfGroupInterface_Object = MibTableColumn
ddboostIfGroupInterface = _DdboostIfGroupInterface_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 7, 1, 1, 2),
    _DdboostIfGroupInterface_Type()
)
ddboostIfGroupInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostIfGroupInterface.setStatus("current")
_DdboostAccessClients_ObjectIdentity = ObjectIdentity
ddboostAccessClients = _DdboostAccessClients_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 8)
)
_DdboostAccessClientsTable_Object = MibTable
ddboostAccessClientsTable = _DdboostAccessClientsTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 8, 1)
)
if mibBuilder.loadTexts:
    ddboostAccessClientsTable.setStatus("current")
_DdboostAccessClientsEntry_Object = MibTableRow
ddboostAccessClientsEntry = _DdboostAccessClientsEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 8, 1, 1)
)
ddboostAccessClientsEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "ddboostAccessClientsIndex"),
)
if mibBuilder.loadTexts:
    ddboostAccessClientsEntry.setStatus("current")
_DdboostAccessClientsIndex_Type = DDMibTableIndexTC
_DdboostAccessClientsIndex_Object = MibTableColumn
ddboostAccessClientsIndex = _DdboostAccessClientsIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 8, 1, 1, 1),
    _DdboostAccessClientsIndex_Type()
)
ddboostAccessClientsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ddboostAccessClientsIndex.setStatus("current")
_DdboostAccessClientsName_Type = DDMibTableString64TC
_DdboostAccessClientsName_Object = MibTableColumn
ddboostAccessClientsName = _DdboostAccessClientsName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 8, 1, 1, 2),
    _DdboostAccessClientsName_Type()
)
ddboostAccessClientsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostAccessClientsName.setStatus("current")
_DdboostAccessClientsEncryStrength_Type = DdboostAccessClientsEncryStrengthTC
_DdboostAccessClientsEncryStrength_Object = MibTableColumn
ddboostAccessClientsEncryStrength = _DdboostAccessClientsEncryStrength_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 8, 1, 1, 3),
    _DdboostAccessClientsEncryStrength_Type()
)
ddboostAccessClientsEncryStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostAccessClientsEncryStrength.setStatus("current")
_DdboostAccessClientsAuthMode_Type = DdboostAccessClientsAuthModeTC
_DdboostAccessClientsAuthMode_Object = MibTableColumn
ddboostAccessClientsAuthMode = _DdboostAccessClientsAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 8, 1, 1, 4),
    _DdboostAccessClientsAuthMode_Type()
)
ddboostAccessClientsAuthMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostAccessClientsAuthMode.setStatus("current")
_DdboostOptions_ObjectIdentity = ObjectIdentity
ddboostOptions = _DdboostOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 9)
)
_DdboostOptionsTable_Object = MibTable
ddboostOptionsTable = _DdboostOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 9, 1)
)
if mibBuilder.loadTexts:
    ddboostOptionsTable.setStatus("current")
_DdboostOptionsEntry_Object = MibTableRow
ddboostOptionsEntry = _DdboostOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 9, 1, 1)
)
ddboostOptionsEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "ddboostOptionsIndex"),
)
if mibBuilder.loadTexts:
    ddboostOptionsEntry.setStatus("current")
_DdboostOptionsIndex_Type = DDMibTableIndexTC
_DdboostOptionsIndex_Object = MibTableColumn
ddboostOptionsIndex = _DdboostOptionsIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 9, 1, 1, 1),
    _DdboostOptionsIndex_Type()
)
ddboostOptionsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ddboostOptionsIndex.setStatus("current")
_DdboostOptionsName_Type = DDMibTableString64TC
_DdboostOptionsName_Object = MibTableColumn
ddboostOptionsName = _DdboostOptionsName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 9, 1, 1, 2),
    _DdboostOptionsName_Type()
)
ddboostOptionsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostOptionsName.setStatus("current")
_DdboostOptionsStatus_Type = DDMibStatusTC
_DdboostOptionsStatus_Object = MibTableColumn
ddboostOptionsStatus = _DdboostOptionsStatus_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 9, 1, 1, 3),
    _DdboostOptionsStatus_Type()
)
ddboostOptionsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostOptionsStatus.setStatus("current")
_DdboostFileReplicationPerformance_ObjectIdentity = ObjectIdentity
ddboostFileReplicationPerformance = _DdboostFileReplicationPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 10)
)
_DdboostFileRepliPerfInPreCompKBPerSec_Type = DDMibInteger32TC
_DdboostFileRepliPerfInPreCompKBPerSec_Object = MibScalar
ddboostFileRepliPerfInPreCompKBPerSec = _DdboostFileRepliPerfInPreCompKBPerSec_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 10, 1),
    _DdboostFileRepliPerfInPreCompKBPerSec_Type()
)
ddboostFileRepliPerfInPreCompKBPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostFileRepliPerfInPreCompKBPerSec.setStatus("current")
_DdboostFileRepliPerfInNetworkKBPerSec_Type = DDMibInteger32TC
_DdboostFileRepliPerfInNetworkKBPerSec_Object = MibScalar
ddboostFileRepliPerfInNetworkKBPerSec = _DdboostFileRepliPerfInNetworkKBPerSec_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 10, 2),
    _DdboostFileRepliPerfInNetworkKBPerSec_Type()
)
ddboostFileRepliPerfInNetworkKBPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostFileRepliPerfInNetworkKBPerSec.setStatus("current")
_DdboostFileRepliPerfOutPreCompKBPerSec_Type = DDMibInteger32TC
_DdboostFileRepliPerfOutPreCompKBPerSec_Object = MibScalar
ddboostFileRepliPerfOutPreCompKBPerSec = _DdboostFileRepliPerfOutPreCompKBPerSec_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 10, 3),
    _DdboostFileRepliPerfOutPreCompKBPerSec_Type()
)
ddboostFileRepliPerfOutPreCompKBPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostFileRepliPerfOutPreCompKBPerSec.setStatus("current")
_DdboostFileRepliPerfOutNetworkKBPerSec_Type = DDMibInteger32TC
_DdboostFileRepliPerfOutNetworkKBPerSec_Object = MibScalar
ddboostFileRepliPerfOutNetworkKBPerSec = _DdboostFileRepliPerfOutNetworkKBPerSec_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 12, 10, 4),
    _DdboostFileRepliPerfOutNetworkKBPerSec_Type()
)
ddboostFileRepliPerfOutNetworkKBPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddboostFileRepliPerfOutNetworkKBPerSec.setStatus("current")
_DataDomainSystem_ObjectIdentity = ObjectIdentity
dataDomainSystem = _DataDomainSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13)
)
_SystemProperties_ObjectIdentity = ObjectIdentity
systemProperties = _SystemProperties_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 1)
)
_SystemSerialNumber_Type = SystemSerialNumberTC
_SystemSerialNumber_Object = MibScalar
systemSerialNumber = _SystemSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 1, 1),
    _SystemSerialNumber_Type()
)
systemSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSerialNumber.setStatus("current")
_SystemCurrentTime_Type = DDMibTimeStampTC
_SystemCurrentTime_Object = MibScalar
systemCurrentTime = _SystemCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 1, 2),
    _SystemCurrentTime_Type()
)
systemCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemCurrentTime.setStatus("current")
_SystemVersion_Type = DDMibVersionTC
_SystemVersion_Object = MibScalar
systemVersion = _SystemVersion_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 1, 3),
    _SystemVersion_Type()
)
systemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemVersion.setStatus("current")
_SystemModelNumber_Type = DDMibTableString64TC
_SystemModelNumber_Object = MibScalar
systemModelNumber = _SystemModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 1, 4),
    _SystemModelNumber_Type()
)
systemModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemModelNumber.setStatus("current")
_SystemTimeZoneName_Type = SystemTimeZoneNameTC
_SystemTimeZoneName_Object = MibScalar
systemTimeZoneName = _SystemTimeZoneName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 1, 5),
    _SystemTimeZoneName_Type()
)
systemTimeZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTimeZoneName.setStatus("current")
_SysNotes_Type = SystemNotesTC
_SysNotes_Object = MibScalar
sysNotes = _SysNotes_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 1, 6),
    _SysNotes_Type()
)
sysNotes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysNotes.setStatus("current")
_SystemHardware_ObjectIdentity = ObjectIdentity
systemHardware = _SystemHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 2)
)
_SystemHardwareTable_Object = MibTable
systemHardwareTable = _SystemHardwareTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 2, 1)
)
if mibBuilder.loadTexts:
    systemHardwareTable.setStatus("current")
_SystemHardwareEntry_Object = MibTableRow
systemHardwareEntry = _SystemHardwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 2, 1, 1)
)
systemHardwareEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "systemHardwareIndex"),
)
if mibBuilder.loadTexts:
    systemHardwareEntry.setStatus("current")
_SystemHardwareIndex_Type = DDMibTableIndexTC
_SystemHardwareIndex_Object = MibTableColumn
systemHardwareIndex = _SystemHardwareIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 2, 1, 1, 1),
    _SystemHardwareIndex_Type()
)
systemHardwareIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    systemHardwareIndex.setStatus("current")
_SystemHardwareSlot_Type = DDMibInteger32TC
_SystemHardwareSlot_Object = MibTableColumn
systemHardwareSlot = _SystemHardwareSlot_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 2, 1, 1, 2),
    _SystemHardwareSlot_Type()
)
systemHardwareSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareSlot.setStatus("deprecated")
_SystemHardwareVendor_Type = DDMibTableString64TC
_SystemHardwareVendor_Object = MibTableColumn
systemHardwareVendor = _SystemHardwareVendor_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 2, 1, 1, 3),
    _SystemHardwareVendor_Type()
)
systemHardwareVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareVendor.setStatus("current")
_SystemHardwareDevice_Type = DDMibTableString128TC
_SystemHardwareDevice_Object = MibTableColumn
systemHardwareDevice = _SystemHardwareDevice_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 2, 1, 1, 4),
    _SystemHardwareDevice_Type()
)
systemHardwareDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareDevice.setStatus("current")
_SystemHardwarePorts_Type = DDMibTableString128TC
_SystemHardwarePorts_Object = MibTableColumn
systemHardwarePorts = _SystemHardwarePorts_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 2, 1, 1, 5),
    _SystemHardwarePorts_Type()
)
systemHardwarePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwarePorts.setStatus("current")


class _SystemHardwareSlotName_Type(DisplayString):
    """Custom type systemHardwareSlotName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_SystemHardwareSlotName_Type.__name__ = "DisplayString"
_SystemHardwareSlotName_Object = MibTableColumn
systemHardwareSlotName = _SystemHardwareSlotName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 2, 1, 1, 6),
    _SystemHardwareSlotName_Type()
)
systemHardwareSlotName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareSlotName.setStatus("current")
_SystemPorts_ObjectIdentity = ObjectIdentity
systemPorts = _SystemPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 3)
)
_SystemPortsTable_Object = MibTable
systemPortsTable = _SystemPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 3, 1)
)
if mibBuilder.loadTexts:
    systemPortsTable.setStatus("current")
_SystemPortsEntry_Object = MibTableRow
systemPortsEntry = _SystemPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 3, 1, 1)
)
systemPortsEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "systemPortsIndex"),
)
if mibBuilder.loadTexts:
    systemPortsEntry.setStatus("current")
_SystemPortsIndex_Type = DDMibTableIndexTC
_SystemPortsIndex_Object = MibTableColumn
systemPortsIndex = _SystemPortsIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 3, 1, 1, 1),
    _SystemPortsIndex_Type()
)
systemPortsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    systemPortsIndex.setStatus("current")
_SystemPortsPort_Type = DDMibTableString32TC
_SystemPortsPort_Object = MibTableColumn
systemPortsPort = _SystemPortsPort_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 3, 1, 1, 2),
    _SystemPortsPort_Type()
)
systemPortsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemPortsPort.setStatus("current")
_SystemPortsConnectionType_Type = DDMibTableString64TC
_SystemPortsConnectionType_Object = MibTableColumn
systemPortsConnectionType = _SystemPortsConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 3, 1, 1, 3),
    _SystemPortsConnectionType_Type()
)
systemPortsConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemPortsConnectionType.setStatus("current")
_SystemPortsLinkSpeed_Type = DDMibTableString128TC
_SystemPortsLinkSpeed_Object = MibTableColumn
systemPortsLinkSpeed = _SystemPortsLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 3, 1, 1, 4),
    _SystemPortsLinkSpeed_Type()
)
systemPortsLinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemPortsLinkSpeed.setStatus("current")
_SystemPortsFirmware_Type = DDMibTableString128TC
_SystemPortsFirmware_Object = MibTableColumn
systemPortsFirmware = _SystemPortsFirmware_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 3, 1, 1, 5),
    _SystemPortsFirmware_Type()
)
systemPortsFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemPortsFirmware.setStatus("current")
_SystemPortsHardwareAddress_Type = DDMibTableString64TC
_SystemPortsHardwareAddress_Object = MibTableColumn
systemPortsHardwareAddress = _SystemPortsHardwareAddress_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 3, 1, 1, 6),
    _SystemPortsHardwareAddress_Type()
)
systemPortsHardwareAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemPortsHardwareAddress.setStatus("current")
_SystemLicense_ObjectIdentity = ObjectIdentity
systemLicense = _SystemLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 4)
)
_SystemLicenseTable_Object = MibTable
systemLicenseTable = _SystemLicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 4, 1)
)
if mibBuilder.loadTexts:
    systemLicenseTable.setStatus("current")
_SystemLicenseEntry_Object = MibTableRow
systemLicenseEntry = _SystemLicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 4, 1, 1)
)
systemLicenseEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "systemLicenseIndex"),
)
if mibBuilder.loadTexts:
    systemLicenseEntry.setStatus("current")
_SystemLicenseIndex_Type = DDMibTableIndexTC
_SystemLicenseIndex_Object = MibTableColumn
systemLicenseIndex = _SystemLicenseIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 4, 1, 1, 1),
    _SystemLicenseIndex_Type()
)
systemLicenseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    systemLicenseIndex.setStatus("current")
_SystemLicenseKey_Type = DDMibTableString256TC
_SystemLicenseKey_Object = MibTableColumn
systemLicenseKey = _SystemLicenseKey_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 4, 1, 1, 2),
    _SystemLicenseKey_Type()
)
systemLicenseKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemLicenseKey.setStatus("current")
_SystemLicenseFeature_Type = DDMibTableString64TC
_SystemLicenseFeature_Object = MibTableColumn
systemLicenseFeature = _SystemLicenseFeature_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 4, 1, 1, 3),
    _SystemLicenseFeature_Type()
)
systemLicenseFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemLicenseFeature.setStatus("current")
_SystemCapacityLicense_ObjectIdentity = ObjectIdentity
systemCapacityLicense = _SystemCapacityLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 4, 2)
)
_SystemCapacityLicenseTable_Object = MibTable
systemCapacityLicenseTable = _SystemCapacityLicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 4, 2, 1)
)
if mibBuilder.loadTexts:
    systemCapacityLicenseTable.setStatus("current")
_SystemCapacityLicenseEntry_Object = MibTableRow
systemCapacityLicenseEntry = _SystemCapacityLicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 4, 2, 1, 1)
)
systemCapacityLicenseEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "systemCapacityLicenseIndex"),
)
if mibBuilder.loadTexts:
    systemCapacityLicenseEntry.setStatus("current")
_SystemCapacityLicenseIndex_Type = DDMibTableIndexTC
_SystemCapacityLicenseIndex_Object = MibTableColumn
systemCapacityLicenseIndex = _SystemCapacityLicenseIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 4, 2, 1, 1, 1),
    _SystemCapacityLicenseIndex_Type()
)
systemCapacityLicenseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    systemCapacityLicenseIndex.setStatus("current")
_SystemCapacityLicenseKey_Type = DDMibTableString256TC
_SystemCapacityLicenseKey_Object = MibTableColumn
systemCapacityLicenseKey = _SystemCapacityLicenseKey_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 4, 2, 1, 1, 2),
    _SystemCapacityLicenseKey_Type()
)
systemCapacityLicenseKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemCapacityLicenseKey.setStatus("current")
_SystemCapacityLicenseFeature_Type = DDMibTableString64TC
_SystemCapacityLicenseFeature_Object = MibTableColumn
systemCapacityLicenseFeature = _SystemCapacityLicenseFeature_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 4, 2, 1, 1, 3),
    _SystemCapacityLicenseFeature_Type()
)
systemCapacityLicenseFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemCapacityLicenseFeature.setStatus("current")
_SystemCapacityLicenseModel_Type = DDMibTableString32TC
_SystemCapacityLicenseModel_Object = MibTableColumn
systemCapacityLicenseModel = _SystemCapacityLicenseModel_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 4, 2, 1, 1, 4),
    _SystemCapacityLicenseModel_Type()
)
systemCapacityLicenseModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemCapacityLicenseModel.setStatus("current")
_SystemCapacityLicenseCapacity_Type = DDMibTableString32TC
_SystemCapacityLicenseCapacity_Object = MibTableColumn
systemCapacityLicenseCapacity = _SystemCapacityLicenseCapacity_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 4, 2, 1, 1, 5),
    _SystemCapacityLicenseCapacity_Type()
)
systemCapacityLicenseCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemCapacityLicenseCapacity.setStatus("current")
_SystemUser_ObjectIdentity = ObjectIdentity
systemUser = _SystemUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 5)
)
_SystemUserTable_Object = MibTable
systemUserTable = _SystemUserTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 5, 1)
)
if mibBuilder.loadTexts:
    systemUserTable.setStatus("current")
_SystemUserEntry_Object = MibTableRow
systemUserEntry = _SystemUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 5, 1, 1)
)
systemUserEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "systemUserIndex"),
)
if mibBuilder.loadTexts:
    systemUserEntry.setStatus("current")
_SystemUserIndex_Type = DDMibTableIndexTC
_SystemUserIndex_Object = MibTableColumn
systemUserIndex = _SystemUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 5, 1, 1, 1),
    _SystemUserIndex_Type()
)
systemUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    systemUserIndex.setStatus("current")
_SystemUserName_Type = DDMibTableString128TC
_SystemUserName_Object = MibTableColumn
systemUserName = _SystemUserName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 5, 1, 1, 2),
    _SystemUserName_Type()
)
systemUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUserName.setStatus("current")
_SystemUserUID_Type = DDMibInteger32TC
_SystemUserUID_Object = MibTableColumn
systemUserUID = _SystemUserUID_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 5, 1, 1, 3),
    _SystemUserUID_Type()
)
systemUserUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUserUID.setStatus("current")
_SystemUserRole_Type = DDMibTableString32TC
_SystemUserRole_Object = MibTableColumn
systemUserRole = _SystemUserRole_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 5, 1, 1, 4),
    _SystemUserRole_Type()
)
systemUserRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUserRole.setStatus("current")
_SystemUserStatus_Type = DDMibTableString32TC
_SystemUserStatus_Object = MibTableColumn
systemUserStatus = _SystemUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 5, 1, 1, 5),
    _SystemUserStatus_Type()
)
systemUserStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUserStatus.setStatus("current")
_SystemActiveUserTable_Object = MibTable
systemActiveUserTable = _SystemActiveUserTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 5, 2)
)
if mibBuilder.loadTexts:
    systemActiveUserTable.setStatus("current")
_SystemActiveUserEntry_Object = MibTableRow
systemActiveUserEntry = _SystemActiveUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 5, 2, 1)
)
systemActiveUserEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "systemActiveUserIndex"),
)
if mibBuilder.loadTexts:
    systemActiveUserEntry.setStatus("current")
_SystemActiveUserIndex_Type = DDMibTableIndexTC
_SystemActiveUserIndex_Object = MibTableColumn
systemActiveUserIndex = _SystemActiveUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 5, 2, 1, 1),
    _SystemActiveUserIndex_Type()
)
systemActiveUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    systemActiveUserIndex.setStatus("current")
_SystemActiveUserName_Type = DDMibTableString128TC
_SystemActiveUserName_Object = MibTableColumn
systemActiveUserName = _SystemActiveUserName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 5, 2, 1, 2),
    _SystemActiveUserName_Type()
)
systemActiveUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemActiveUserName.setStatus("current")
_SystemActiveUserIdleTime_Type = DDMibTableString32TC
_SystemActiveUserIdleTime_Object = MibTableColumn
systemActiveUserIdleTime = _SystemActiveUserIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 5, 2, 1, 3),
    _SystemActiveUserIdleTime_Type()
)
systemActiveUserIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemActiveUserIdleTime.setStatus("current")
_SystemActiveUserLoginTime_Type = DDMibTableString32TC
_SystemActiveUserLoginTime_Object = MibTableColumn
systemActiveUserLoginTime = _SystemActiveUserLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 5, 2, 1, 4),
    _SystemActiveUserLoginTime_Type()
)
systemActiveUserLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemActiveUserLoginTime.setStatus("current")
_SystemActiveUserLoginFrom_Type = DDMibTableString32TC
_SystemActiveUserLoginFrom_Object = MibTableColumn
systemActiveUserLoginFrom = _SystemActiveUserLoginFrom_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 5, 2, 1, 5),
    _SystemActiveUserLoginFrom_Type()
)
systemActiveUserLoginFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemActiveUserLoginFrom.setStatus("current")
_SystemActiveUserTty_Type = DDMibTableString32TC
_SystemActiveUserTty_Object = MibTableColumn
systemActiveUserTty = _SystemActiveUserTty_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 13, 5, 2, 1, 6),
    _SystemActiveUserTty_Type()
)
systemActiveUserTty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemActiveUserTty.setStatus("current")
_Art_ObjectIdentity = ObjectIdentity
art = _Art_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 14)
)
_ArtConfig_ObjectIdentity = ObjectIdentity
artConfig = _ArtConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 14, 1)
)
_ArtConfigTable_Object = MibTable
artConfigTable = _ArtConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 14, 1, 1)
)
if mibBuilder.loadTexts:
    artConfigTable.setStatus("current")
_ArtConfigEntry_Object = MibTableRow
artConfigEntry = _ArtConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 14, 1, 1, 1)
)
artConfigEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "artConfigIndex"),
)
if mibBuilder.loadTexts:
    artConfigEntry.setStatus("current")
_ArtConfigIndex_Type = DDMibTableIndexTC
_ArtConfigIndex_Object = MibTableColumn
artConfigIndex = _ArtConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 14, 1, 1, 1, 1),
    _ArtConfigIndex_Type()
)
artConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    artConfigIndex.setStatus("current")
_ArtConfigStatus_Type = DDMibTableEnabledTC
_ArtConfigStatus_Object = MibTableColumn
artConfigStatus = _ArtConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 14, 1, 1, 1, 2),
    _ArtConfigStatus_Type()
)
artConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artConfigStatus.setStatus("current")
_ArtConfigMigrationSchedule_Type = DDMibTableString128TC
_ArtConfigMigrationSchedule_Object = MibTableColumn
artConfigMigrationSchedule = _ArtConfigMigrationSchedule_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 14, 1, 1, 1, 3),
    _ArtConfigMigrationSchedule_Type()
)
artConfigMigrationSchedule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artConfigMigrationSchedule.setStatus("current")
_ArtConfigDefaultAge_Type = DDMibInteger32TC
_ArtConfigDefaultAge_Object = MibTableColumn
artConfigDefaultAge = _ArtConfigDefaultAge_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 14, 1, 1, 1, 4),
    _ArtConfigDefaultAge_Type()
)
artConfigDefaultAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artConfigDefaultAge.setStatus("current")
_ArtConfigFileSystemClean_Type = DDMibTableEnabledTC
_ArtConfigFileSystemClean_Object = MibTableColumn
artConfigFileSystemClean = _ArtConfigFileSystemClean_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 14, 1, 1, 1, 5),
    _ArtConfigFileSystemClean_Type()
)
artConfigFileSystemClean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artConfigFileSystemClean.setStatus("current")
_ArtConfigCompression_Type = DDMibTableString32TC
_ArtConfigCompression_Object = MibTableColumn
artConfigCompression = _ArtConfigCompression_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 14, 1, 1, 1, 6),
    _ArtConfigCompression_Type()
)
artConfigCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artConfigCompression.setStatus("current")
_ArtMigrationSchedule_ObjectIdentity = ObjectIdentity
artMigrationSchedule = _ArtMigrationSchedule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 14, 2)
)
_ArtMigrationScheduleTable_Object = MibTable
artMigrationScheduleTable = _ArtMigrationScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 14, 2, 1)
)
if mibBuilder.loadTexts:
    artMigrationScheduleTable.setStatus("current")
_ArtMigrationScheduleEntry_Object = MibTableRow
artMigrationScheduleEntry = _ArtMigrationScheduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 14, 2, 1, 1)
)
artMigrationScheduleEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "artMigrationScheduleIndex"),
)
if mibBuilder.loadTexts:
    artMigrationScheduleEntry.setStatus("current")
_ArtMigrationScheduleIndex_Type = DDMibTableIndexTC
_ArtMigrationScheduleIndex_Object = MibTableColumn
artMigrationScheduleIndex = _ArtMigrationScheduleIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 14, 2, 1, 1, 1),
    _ArtMigrationScheduleIndex_Type()
)
artMigrationScheduleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    artMigrationScheduleIndex.setStatus("current")
_ArtMigrationScheduleSchedule_Type = DDMibTableString512TC
_ArtMigrationScheduleSchedule_Object = MibTableColumn
artMigrationScheduleSchedule = _ArtMigrationScheduleSchedule_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 14, 2, 1, 1, 2),
    _ArtMigrationScheduleSchedule_Type()
)
artMigrationScheduleSchedule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artMigrationScheduleSchedule.setStatus("current")
_ArtMigrationScheduleStatus_Type = DDMibStatusTC
_ArtMigrationScheduleStatus_Object = MibTableColumn
artMigrationScheduleStatus = _ArtMigrationScheduleStatus_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 14, 2, 1, 1, 3),
    _ArtMigrationScheduleStatus_Type()
)
artMigrationScheduleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artMigrationScheduleStatus.setStatus("current")
_ArtMigrationPolicy_ObjectIdentity = ObjectIdentity
artMigrationPolicy = _ArtMigrationPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 14, 3)
)
_ArtMigrationPolicyTable_Object = MibTable
artMigrationPolicyTable = _ArtMigrationPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 14, 3, 1)
)
if mibBuilder.loadTexts:
    artMigrationPolicyTable.setStatus("current")
_ArtMigrationPolicyEntry_Object = MibTableRow
artMigrationPolicyEntry = _ArtMigrationPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 14, 3, 1, 1)
)
artMigrationPolicyEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "artMigrationPolicyIndex"),
)
if mibBuilder.loadTexts:
    artMigrationPolicyEntry.setStatus("current")
_ArtMigrationPolicyIndex_Type = DDMibTableIndexTC
_ArtMigrationPolicyIndex_Object = MibTableColumn
artMigrationPolicyIndex = _ArtMigrationPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 14, 3, 1, 1, 1),
    _ArtMigrationPolicyIndex_Type()
)
artMigrationPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    artMigrationPolicyIndex.setStatus("current")
_ArtMigrationPolicyMtreeName_Type = DDMibTableString256TC
_ArtMigrationPolicyMtreeName_Object = MibTableColumn
artMigrationPolicyMtreeName = _ArtMigrationPolicyMtreeName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 14, 3, 1, 1, 2),
    _ArtMigrationPolicyMtreeName_Type()
)
artMigrationPolicyMtreeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artMigrationPolicyMtreeName.setStatus("current")
_ArtMigrationPolicyDefaultAge_Type = DDMibInteger32TC
_ArtMigrationPolicyDefaultAge_Object = MibTableColumn
artMigrationPolicyDefaultAge = _ArtMigrationPolicyDefaultAge_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 14, 3, 1, 1, 3),
    _ArtMigrationPolicyDefaultAge_Type()
)
artMigrationPolicyDefaultAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artMigrationPolicyDefaultAge.setStatus("current")
_Mtree_ObjectIdentity = ObjectIdentity
mtree = _Mtree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 15)
)
_MtreeCompression_ObjectIdentity = ObjectIdentity
mtreeCompression = _MtreeCompression_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 15, 1)
)
_MtreeCompressionTable_Object = MibTable
mtreeCompressionTable = _MtreeCompressionTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 15, 1, 1)
)
if mibBuilder.loadTexts:
    mtreeCompressionTable.setStatus("current")
_MtreeCompressionEntry_Object = MibTableRow
mtreeCompressionEntry = _MtreeCompressionEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 15, 1, 1, 1)
)
mtreeCompressionEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "mtreeCompressionIndex"),
)
if mibBuilder.loadTexts:
    mtreeCompressionEntry.setStatus("current")
_MtreeCompressionIndex_Type = DDMibTableIndexTC
_MtreeCompressionIndex_Object = MibTableColumn
mtreeCompressionIndex = _MtreeCompressionIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 15, 1, 1, 1, 1),
    _MtreeCompressionIndex_Type()
)
mtreeCompressionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtreeCompressionIndex.setStatus("current")
_MtreeCompressionMtreePath_Type = DDMibTableString512TC
_MtreeCompressionMtreePath_Object = MibTableColumn
mtreeCompressionMtreePath = _MtreeCompressionMtreePath_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 15, 1, 1, 1, 2),
    _MtreeCompressionMtreePath_Type()
)
mtreeCompressionMtreePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtreeCompressionMtreePath.setStatus("current")
_MtreeCompressionPreCompGib_Type = DDMibTableSizeGibTC
_MtreeCompressionPreCompGib_Object = MibTableColumn
mtreeCompressionPreCompGib = _MtreeCompressionPreCompGib_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 15, 1, 1, 1, 3),
    _MtreeCompressionPreCompGib_Type()
)
mtreeCompressionPreCompGib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtreeCompressionPreCompGib.setStatus("current")
_MtreeCompressionPostCompGib_Type = DDMibTableSizeGibTC
_MtreeCompressionPostCompGib_Object = MibTableColumn
mtreeCompressionPostCompGib = _MtreeCompressionPostCompGib_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 15, 1, 1, 1, 4),
    _MtreeCompressionPostCompGib_Type()
)
mtreeCompressionPostCompGib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtreeCompressionPostCompGib.setStatus("current")
_MtreeCompressionGlobalCompFactor_Type = DDMibCompressionFactorTC
_MtreeCompressionGlobalCompFactor_Object = MibTableColumn
mtreeCompressionGlobalCompFactor = _MtreeCompressionGlobalCompFactor_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 15, 1, 1, 1, 5),
    _MtreeCompressionGlobalCompFactor_Type()
)
mtreeCompressionGlobalCompFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtreeCompressionGlobalCompFactor.setStatus("current")
_MtreeCompressionLocalCompFactor_Type = DDMibCompressionFactorTC
_MtreeCompressionLocalCompFactor_Object = MibTableColumn
mtreeCompressionLocalCompFactor = _MtreeCompressionLocalCompFactor_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 15, 1, 1, 1, 6),
    _MtreeCompressionLocalCompFactor_Type()
)
mtreeCompressionLocalCompFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtreeCompressionLocalCompFactor.setStatus("current")
_MtreeCompressionPostTotalCompFactor_Type = DDMibCompressionFactorTC
_MtreeCompressionPostTotalCompFactor_Object = MibTableColumn
mtreeCompressionPostTotalCompFactor = _MtreeCompressionPostTotalCompFactor_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 15, 1, 1, 1, 7),
    _MtreeCompressionPostTotalCompFactor_Type()
)
mtreeCompressionPostTotalCompFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtreeCompressionPostTotalCompFactor.setStatus("current")
_MtreeCompressionTimePeriod_Type = DDMibTableString128TC
_MtreeCompressionTimePeriod_Object = MibTableColumn
mtreeCompressionTimePeriod = _MtreeCompressionTimePeriod_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 15, 1, 1, 1, 8),
    _MtreeCompressionTimePeriod_Type()
)
mtreeCompressionTimePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtreeCompressionTimePeriod.setStatus("current")
_MtreeList_ObjectIdentity = ObjectIdentity
mtreeList = _MtreeList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 15, 2)
)
_MtreeListTable_Object = MibTable
mtreeListTable = _MtreeListTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 15, 2, 1)
)
if mibBuilder.loadTexts:
    mtreeListTable.setStatus("current")
_MtreeListEntry_Object = MibTableRow
mtreeListEntry = _MtreeListEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 15, 2, 1, 1)
)
mtreeListEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "mtreeListIndex"),
)
if mibBuilder.loadTexts:
    mtreeListEntry.setStatus("current")
_MtreeListIndex_Type = DDMibTableIndexTC
_MtreeListIndex_Object = MibTableColumn
mtreeListIndex = _MtreeListIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 15, 2, 1, 1, 1),
    _MtreeListIndex_Type()
)
mtreeListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtreeListIndex.setStatus("current")
_MtreeListMtreeName_Type = DDMibTableString512TC
_MtreeListMtreeName_Object = MibTableColumn
mtreeListMtreeName = _MtreeListMtreeName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 15, 2, 1, 1, 2),
    _MtreeListMtreeName_Type()
)
mtreeListMtreeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtreeListMtreeName.setStatus("current")
_MtreeListPreCompGib_Type = DDMibTableSizeGibTC
_MtreeListPreCompGib_Object = MibTableColumn
mtreeListPreCompGib = _MtreeListPreCompGib_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 15, 2, 1, 1, 3),
    _MtreeListPreCompGib_Type()
)
mtreeListPreCompGib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtreeListPreCompGib.setStatus("current")
_MtreeListStatus_Type = MtreeListStatusTC
_MtreeListStatus_Object = MibTableColumn
mtreeListStatus = _MtreeListStatus_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 15, 2, 1, 1, 4),
    _MtreeListStatus_Type()
)
mtreeListStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtreeListStatus.setStatus("current")
_MtreeRetentionLock_ObjectIdentity = ObjectIdentity
mtreeRetentionLock = _MtreeRetentionLock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 15, 4)
)
_MtreeRetentionLockTable_Object = MibTable
mtreeRetentionLockTable = _MtreeRetentionLockTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 15, 4, 1)
)
if mibBuilder.loadTexts:
    mtreeRetentionLockTable.setStatus("current")
_MtreeRetentionLockEntry_Object = MibTableRow
mtreeRetentionLockEntry = _MtreeRetentionLockEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 15, 4, 1, 1)
)
mtreeRetentionLockEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "mtreeRetentionLockIndex"),
)
if mibBuilder.loadTexts:
    mtreeRetentionLockEntry.setStatus("current")
_MtreeRetentionLockIndex_Type = DDMibTableIndexTC
_MtreeRetentionLockIndex_Object = MibTableColumn
mtreeRetentionLockIndex = _MtreeRetentionLockIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 15, 4, 1, 1, 1),
    _MtreeRetentionLockIndex_Type()
)
mtreeRetentionLockIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtreeRetentionLockIndex.setStatus("current")
_MtreeRetentionLockMtreeName_Type = DDMibTableString512TC
_MtreeRetentionLockMtreeName_Object = MibTableColumn
mtreeRetentionLockMtreeName = _MtreeRetentionLockMtreeName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 15, 4, 1, 1, 2),
    _MtreeRetentionLockMtreeName_Type()
)
mtreeRetentionLockMtreeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtreeRetentionLockMtreeName.setStatus("current")
_MtreeRetentionLockStatus_Type = MtreeRetentionLockStatusTC
_MtreeRetentionLockStatus_Object = MibTableColumn
mtreeRetentionLockStatus = _MtreeRetentionLockStatus_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 15, 4, 1, 1, 3),
    _MtreeRetentionLockStatus_Type()
)
mtreeRetentionLockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtreeRetentionLockStatus.setStatus("current")
_MtreeRetentionLockUUID_Type = DDMibTableString32TC
_MtreeRetentionLockUUID_Object = MibTableColumn
mtreeRetentionLockUUID = _MtreeRetentionLockUUID_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 15, 4, 1, 1, 4),
    _MtreeRetentionLockUUID_Type()
)
mtreeRetentionLockUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtreeRetentionLockUUID.setStatus("current")
_MtreeRetentionLockMinRetentionPeriod_Type = DDMibTableString32TC
_MtreeRetentionLockMinRetentionPeriod_Object = MibTableColumn
mtreeRetentionLockMinRetentionPeriod = _MtreeRetentionLockMinRetentionPeriod_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 15, 4, 1, 1, 5),
    _MtreeRetentionLockMinRetentionPeriod_Type()
)
mtreeRetentionLockMinRetentionPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtreeRetentionLockMinRetentionPeriod.setStatus("current")
_MtreeRetentionLockMaxRetentionPeriod_Type = DDMibTableString32TC
_MtreeRetentionLockMaxRetentionPeriod_Object = MibTableColumn
mtreeRetentionLockMaxRetentionPeriod = _MtreeRetentionLockMaxRetentionPeriod_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 15, 4, 1, 1, 6),
    _MtreeRetentionLockMaxRetentionPeriod_Type()
)
mtreeRetentionLockMaxRetentionPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtreeRetentionLockMaxRetentionPeriod.setStatus("current")
_Storage_ObjectIdentity = ObjectIdentity
storage = _Storage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 16)
)
_Enclosure_ObjectIdentity = ObjectIdentity
enclosure = _Enclosure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 17)
)
_EnclosureList_ObjectIdentity = ObjectIdentity
enclosureList = _EnclosureList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 17, 1)
)
_EnclosureListTable_Object = MibTable
enclosureListTable = _EnclosureListTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 17, 1, 1)
)
if mibBuilder.loadTexts:
    enclosureListTable.setStatus("current")
_EnclosureListEntry_Object = MibTableRow
enclosureListEntry = _EnclosureListEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 17, 1, 1, 1)
)
enclosureListEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "enclosureListIndex"),
)
if mibBuilder.loadTexts:
    enclosureListEntry.setStatus("current")
_EnclosureListIndex_Type = DDMibTableIndexTC
_EnclosureListIndex_Object = MibTableColumn
enclosureListIndex = _EnclosureListIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 17, 1, 1, 1, 1),
    _EnclosureListIndex_Type()
)
enclosureListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    enclosureListIndex.setStatus("current")
_EnclosureListNum_Type = DDMibInteger32TC
_EnclosureListNum_Object = MibTableColumn
enclosureListNum = _EnclosureListNum_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 17, 1, 1, 1, 2),
    _EnclosureListNum_Type()
)
enclosureListNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureListNum.setStatus("current")
_EnclosureListModel_Type = DDMibTableString64TC
_EnclosureListModel_Object = MibTableColumn
enclosureListModel = _EnclosureListModel_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 17, 1, 1, 1, 3),
    _EnclosureListModel_Type()
)
enclosureListModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureListModel.setStatus("current")
_EnclosureListSerialNum_Type = DDMibTableString128TC
_EnclosureListSerialNum_Object = MibTableColumn
enclosureListSerialNum = _EnclosureListSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 17, 1, 1, 1, 4),
    _EnclosureListSerialNum_Type()
)
enclosureListSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureListSerialNum.setStatus("current")
_EnclosureListOemName_Type = DDMibTableString128TC
_EnclosureListOemName_Object = MibTableColumn
enclosureListOemName = _EnclosureListOemName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 17, 1, 1, 1, 5),
    _EnclosureListOemName_Type()
)
enclosureListOemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureListOemName.setStatus("current")
_EnclosureListOemValue_Type = DDMibTableString128TC
_EnclosureListOemValue_Object = MibTableColumn
enclosureListOemValue = _EnclosureListOemValue_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 17, 1, 1, 1, 6),
    _EnclosureListOemValue_Type()
)
enclosureListOemValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureListOemValue.setStatus("current")
_EnclosureListCapacity_Type = DDMibTableString64TC
_EnclosureListCapacity_Object = MibTableColumn
enclosureListCapacity = _EnclosureListCapacity_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 17, 1, 1, 1, 7),
    _EnclosureListCapacity_Type()
)
enclosureListCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureListCapacity.setStatus("current")
_EnclosurePack_ObjectIdentity = ObjectIdentity
enclosurePack = _EnclosurePack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 17, 2)
)
_EnclosurePackTable_Object = MibTable
enclosurePackTable = _EnclosurePackTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 17, 2, 1)
)
if mibBuilder.loadTexts:
    enclosurePackTable.setStatus("current")
_EnclosurePackEntry_Object = MibTableRow
enclosurePackEntry = _EnclosurePackEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 17, 2, 1, 1)
)
enclosurePackEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "enclosureListIndex"),
    (0, "DATA-DOMAIN-MIB", "enclosurePackID"),
)
if mibBuilder.loadTexts:
    enclosurePackEntry.setStatus("current")
_EnclosurePackID_Type = DDMibTableIndexTC
_EnclosurePackID_Object = MibTableColumn
enclosurePackID = _EnclosurePackID_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 17, 2, 1, 1, 1),
    _EnclosurePackID_Type()
)
enclosurePackID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosurePackID.setStatus("current")
_Network_ObjectIdentity = ObjectIdentity
network = _Network_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 18)
)
_Dns_ObjectIdentity = ObjectIdentity
dns = _Dns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 18, 1)
)
_DnsTable_Object = MibTable
dnsTable = _DnsTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 18, 1, 1)
)
if mibBuilder.loadTexts:
    dnsTable.setStatus("current")
_DnsEntry_Object = MibTableRow
dnsEntry = _DnsEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 18, 1, 1, 1)
)
dnsEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "dnsIndex"),
)
if mibBuilder.loadTexts:
    dnsEntry.setStatus("current")
_DnsIndex_Type = DDMibTableIndexTC
_DnsIndex_Object = MibTableColumn
dnsIndex = _DnsIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 18, 1, 1, 1, 1),
    _DnsIndex_Type()
)
dnsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnsIndex.setStatus("current")
_DnsServer_Type = DDMibTableString32TC
_DnsServer_Object = MibTableColumn
dnsServer = _DnsServer_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 18, 1, 1, 1, 2),
    _DnsServer_Type()
)
dnsServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServer.setStatus("current")
_SearchDomains_ObjectIdentity = ObjectIdentity
searchDomains = _SearchDomains_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 18, 2)
)
_SearchDomainsTable_Object = MibTable
searchDomainsTable = _SearchDomainsTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 18, 2, 1)
)
if mibBuilder.loadTexts:
    searchDomainsTable.setStatus("current")
_SearchDomainsEntry_Object = MibTableRow
searchDomainsEntry = _SearchDomainsEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 18, 2, 1, 1)
)
searchDomainsEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "searchDomainsIndex"),
)
if mibBuilder.loadTexts:
    searchDomainsEntry.setStatus("current")
_SearchDomainsIndex_Type = DDMibTableIndexTC
_SearchDomainsIndex_Object = MibTableColumn
searchDomainsIndex = _SearchDomainsIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 18, 2, 1, 1, 1),
    _SearchDomainsIndex_Type()
)
searchDomainsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    searchDomainsIndex.setStatus("current")
_SearchDomainsName_Type = DDMibTableString128TC
_SearchDomainsName_Object = MibTableColumn
searchDomainsName = _SearchDomainsName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 18, 2, 1, 1, 2),
    _SearchDomainsName_Type()
)
searchDomainsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    searchDomainsName.setStatus("current")
_SnmpTrapHosts_ObjectIdentity = ObjectIdentity
snmpTrapHosts = _SnmpTrapHosts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 18, 3)
)
_SnmpTrapHostsTable_Object = MibTable
snmpTrapHostsTable = _SnmpTrapHostsTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 18, 3, 1)
)
if mibBuilder.loadTexts:
    snmpTrapHostsTable.setStatus("current")
_SnmpTrapHostsEntry_Object = MibTableRow
snmpTrapHostsEntry = _SnmpTrapHostsEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 18, 3, 1, 1)
)
snmpTrapHostsEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "snmpTrapHostsIndex"),
)
if mibBuilder.loadTexts:
    snmpTrapHostsEntry.setStatus("current")
_SnmpTrapHostsIndex_Type = DDMibTableIndexTC
_SnmpTrapHostsIndex_Object = MibTableColumn
snmpTrapHostsIndex = _SnmpTrapHostsIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 18, 3, 1, 1, 1),
    _SnmpTrapHostsIndex_Type()
)
snmpTrapHostsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snmpTrapHostsIndex.setStatus("current")
_SnmpTrapHostsName_Type = DDMibTableString256TC
_SnmpTrapHostsName_Object = MibTableColumn
snmpTrapHostsName = _SnmpTrapHostsName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 18, 3, 1, 1, 2),
    _SnmpTrapHostsName_Type()
)
snmpTrapHostsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTrapHostsName.setStatus("current")
_SnmpTrapHostsVersion_Type = DDMibTableString32TC
_SnmpTrapHostsVersion_Object = MibTableColumn
snmpTrapHostsVersion = _SnmpTrapHostsVersion_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 18, 3, 1, 1, 3),
    _SnmpTrapHostsVersion_Type()
)
snmpTrapHostsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTrapHostsVersion.setStatus("current")
_Nis_ObjectIdentity = ObjectIdentity
nis = _Nis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 18, 4)
)
_NisDomain_Type = DDMibTableString1024TC
_NisDomain_Object = MibScalar
nisDomain = _NisDomain_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 18, 4, 1),
    _NisDomain_Type()
)
nisDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nisDomain.setStatus("current")
_NisServers_Type = DDMibTableString1024TC
_NisServers_Object = MibScalar
nisServers = _NisServers_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 18, 4, 2),
    _NisServers_Type()
)
nisServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nisServers.setStatus("current")
_NisAdminGroups_Type = DDMibTableString1024TC
_NisAdminGroups_Object = MibScalar
nisAdminGroups = _NisAdminGroups_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 18, 4, 3),
    _NisAdminGroups_Type()
)
nisAdminGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nisAdminGroups.setStatus("current")
_NisUserGroups_Type = DDMibTableString1024TC
_NisUserGroups_Object = MibScalar
nisUserGroups = _NisUserGroups_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 18, 4, 4),
    _NisUserGroups_Type()
)
nisUserGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nisUserGroups.setStatus("current")
_NisBackupOperatorGroups_Type = DDMibTableString1024TC
_NisBackupOperatorGroups_Object = MibScalar
nisBackupOperatorGroups = _NisBackupOperatorGroups_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 18, 4, 5),
    _NisBackupOperatorGroups_Type()
)
nisBackupOperatorGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nisBackupOperatorGroups.setStatus("current")
_NisEnabled_Type = DDMibTableEnabledTC
_NisEnabled_Object = MibScalar
nisEnabled = _NisEnabled_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 18, 4, 6),
    _NisEnabled_Type()
)
nisEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nisEnabled.setStatus("current")
_NisStatus_Type = DDMibTableString1024TC
_NisStatus_Object = MibScalar
nisStatus = _NisStatus_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 18, 4, 7),
    _NisStatus_Type()
)
nisStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nisStatus.setStatus("current")
_Ddms_ObjectIdentity = ObjectIdentity
ddms = _Ddms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 19)
)
_ManagedSystem_ObjectIdentity = ObjectIdentity
managedSystem = _ManagedSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 19, 1)
)
_ManagedSystemTable_Object = MibTable
managedSystemTable = _ManagedSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 19, 1, 1)
)
if mibBuilder.loadTexts:
    managedSystemTable.setStatus("current")
_ManagedSystemEntry_Object = MibTableRow
managedSystemEntry = _ManagedSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 19, 1, 1, 1)
)
managedSystemEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "managedSystemIndex"),
)
if mibBuilder.loadTexts:
    managedSystemEntry.setStatus("current")
_ManagedSystemIndex_Type = DDMibTableIndexTC
_ManagedSystemIndex_Object = MibTableColumn
managedSystemIndex = _ManagedSystemIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 19, 1, 1, 1, 1),
    _ManagedSystemIndex_Type()
)
managedSystemIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    managedSystemIndex.setStatus("current")
_ManagedSystemHostname_Type = DDMibTableString256TC
_ManagedSystemHostname_Object = MibTableColumn
managedSystemHostname = _ManagedSystemHostname_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 19, 1, 1, 1, 2),
    _ManagedSystemHostname_Type()
)
managedSystemHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managedSystemHostname.setStatus("current")
_ManagedSystemSerial_Type = DDMibTableString32TC
_ManagedSystemSerial_Object = MibTableColumn
managedSystemSerial = _ManagedSystemSerial_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 19, 1, 1, 1, 3),
    _ManagedSystemSerial_Type()
)
managedSystemSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managedSystemSerial.setStatus("current")
_ManagedSystemState_Type = DDMibTableString32TC
_ManagedSystemState_Object = MibTableColumn
managedSystemState = _ManagedSystemState_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 19, 1, 1, 1, 4),
    _ManagedSystemState_Type()
)
managedSystemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managedSystemState.setStatus("current")
_ManagedSystemStatus_Type = DDMibTableString32TC
_ManagedSystemStatus_Object = MibTableColumn
managedSystemStatus = _ManagedSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 19, 1, 1, 1, 5),
    _ManagedSystemStatus_Type()
)
managedSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managedSystemStatus.setStatus("current")
_ManagedSystemDDOSVersion_Type = DDMibTableString32TC
_ManagedSystemDDOSVersion_Object = MibTableColumn
managedSystemDDOSVersion = _ManagedSystemDDOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 19, 1, 1, 1, 6),
    _ManagedSystemDDOSVersion_Type()
)
managedSystemDDOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managedSystemDDOSVersion.setStatus("current")
_ManagedSystemHDSyncTime_Type = DDMibTableString64TC
_ManagedSystemHDSyncTime_Object = MibTableColumn
managedSystemHDSyncTime = _ManagedSystemHDSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 19, 1, 1, 1, 7),
    _ManagedSystemHDSyncTime_Type()
)
managedSystemHDSyncTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managedSystemHDSyncTime.setStatus("current")
_ManagedSystemCDSyncTime_Type = DDMibTableString64TC
_ManagedSystemCDSyncTime_Object = MibTableColumn
managedSystemCDSyncTime = _ManagedSystemCDSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 19, 1, 1, 1, 8),
    _ManagedSystemCDSyncTime_Type()
)
managedSystemCDSyncTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managedSystemCDSyncTime.setStatus("current")
_TaskHistory_ObjectIdentity = ObjectIdentity
taskHistory = _TaskHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 19, 2)
)
_TaskHistoryTable_Object = MibTable
taskHistoryTable = _TaskHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 19, 2, 1)
)
if mibBuilder.loadTexts:
    taskHistoryTable.setStatus("current")
_TaskHistoryEntry_Object = MibTableRow
taskHistoryEntry = _TaskHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 19, 2, 1, 1)
)
taskHistoryEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "taskHistoryIndex"),
)
if mibBuilder.loadTexts:
    taskHistoryEntry.setStatus("current")
_TaskHistoryIndex_Type = DDMibTableIndexTC
_TaskHistoryIndex_Object = MibTableColumn
taskHistoryIndex = _TaskHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 19, 2, 1, 1, 1),
    _TaskHistoryIndex_Type()
)
taskHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    taskHistoryIndex.setStatus("current")
_TaskHistoryUser_Type = DDMibTableString64TC
_TaskHistoryUser_Object = MibTableColumn
taskHistoryUser = _TaskHistoryUser_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 19, 2, 1, 1, 2),
    _TaskHistoryUser_Type()
)
taskHistoryUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskHistoryUser.setStatus("current")
_TaskHistoryID_Type = DDMibTableString64TC
_TaskHistoryID_Object = MibTableColumn
taskHistoryID = _TaskHistoryID_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 19, 2, 1, 1, 3),
    _TaskHistoryID_Type()
)
taskHistoryID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskHistoryID.setStatus("current")
_TaskHistoryParent_Type = DDMibTableString64TC
_TaskHistoryParent_Object = MibTableColumn
taskHistoryParent = _TaskHistoryParent_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 19, 2, 1, 1, 4),
    _TaskHistoryParent_Type()
)
taskHistoryParent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskHistoryParent.setStatus("current")
_TaskHistoryName_Type = DDMibTableString64TC
_TaskHistoryName_Object = MibTableColumn
taskHistoryName = _TaskHistoryName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 19, 2, 1, 1, 5),
    _TaskHistoryName_Type()
)
taskHistoryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskHistoryName.setStatus("current")
_TaskHistoryState_Type = DDMibTableString64TC
_TaskHistoryState_Object = MibTableColumn
taskHistoryState = _TaskHistoryState_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 19, 2, 1, 1, 6),
    _TaskHistoryState_Type()
)
taskHistoryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskHistoryState.setStatus("current")
_TaskHistoryStartTime_Type = DDMibTableString64TC
_TaskHistoryStartTime_Object = MibTableColumn
taskHistoryStartTime = _TaskHistoryStartTime_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 19, 2, 1, 1, 7),
    _TaskHistoryStartTime_Type()
)
taskHistoryStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskHistoryStartTime.setStatus("current")
_TaskHistoryDuration_Type = DDMibTableString64TC
_TaskHistoryDuration_Object = MibTableColumn
taskHistoryDuration = _TaskHistoryDuration_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 19, 2, 1, 1, 8),
    _TaskHistoryDuration_Type()
)
taskHistoryDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskHistoryDuration.setStatus("current")
_TaskActive_ObjectIdentity = ObjectIdentity
taskActive = _TaskActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 19, 3)
)
_TaskActiveTable_Object = MibTable
taskActiveTable = _TaskActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 19, 3, 1)
)
if mibBuilder.loadTexts:
    taskActiveTable.setStatus("current")
_TaskActiveEntry_Object = MibTableRow
taskActiveEntry = _TaskActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 19, 3, 1, 1)
)
taskActiveEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "taskActiveIndex"),
)
if mibBuilder.loadTexts:
    taskActiveEntry.setStatus("current")
_TaskActiveIndex_Type = DDMibTableIndexTC
_TaskActiveIndex_Object = MibTableColumn
taskActiveIndex = _TaskActiveIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 19, 3, 1, 1, 1),
    _TaskActiveIndex_Type()
)
taskActiveIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    taskActiveIndex.setStatus("current")
_TaskActiveUser_Type = DDMibTableString64TC
_TaskActiveUser_Object = MibTableColumn
taskActiveUser = _TaskActiveUser_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 19, 3, 1, 1, 2),
    _TaskActiveUser_Type()
)
taskActiveUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskActiveUser.setStatus("current")
_TaskActiveID_Type = DDMibTableString64TC
_TaskActiveID_Object = MibTableColumn
taskActiveID = _TaskActiveID_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 19, 3, 1, 1, 3),
    _TaskActiveID_Type()
)
taskActiveID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskActiveID.setStatus("current")
_TaskActiveParent_Type = DDMibTableString64TC
_TaskActiveParent_Object = MibTableColumn
taskActiveParent = _TaskActiveParent_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 19, 3, 1, 1, 4),
    _TaskActiveParent_Type()
)
taskActiveParent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskActiveParent.setStatus("current")
_TaskActiveName_Type = DDMibTableString64TC
_TaskActiveName_Object = MibTableColumn
taskActiveName = _TaskActiveName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 19, 3, 1, 1, 5),
    _TaskActiveName_Type()
)
taskActiveName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskActiveName.setStatus("current")
_TaskActiveState_Type = DDMibTableString64TC
_TaskActiveState_Object = MibTableColumn
taskActiveState = _TaskActiveState_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 19, 3, 1, 1, 6),
    _TaskActiveState_Type()
)
taskActiveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskActiveState.setStatus("current")
_TaskActiveStartTime_Type = DDMibTableString64TC
_TaskActiveStartTime_Object = MibTableColumn
taskActiveStartTime = _TaskActiveStartTime_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 19, 3, 1, 1, 7),
    _TaskActiveStartTime_Type()
)
taskActiveStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskActiveStartTime.setStatus("current")
_TaskActiveDuration_Type = DDMibTableString64TC
_TaskActiveDuration_Object = MibTableColumn
taskActiveDuration = _TaskActiveDuration_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 19, 3, 1, 1, 8),
    _TaskActiveDuration_Type()
)
taskActiveDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskActiveDuration.setStatus("current")
_Smt_ObjectIdentity = ObjectIdentity
smt = _Smt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20)
)
_SmtProperties_ObjectIdentity = ObjectIdentity
smtProperties = _SmtProperties_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 1)
)
_SmtStatus_Type = SmtStatusTC
_SmtStatus_Object = MibScalar
smtStatus = _SmtStatus_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 1, 1),
    _SmtStatus_Type()
)
smtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtStatus.setStatus("current")
_TenantUnitList_ObjectIdentity = ObjectIdentity
tenantUnitList = _TenantUnitList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 2)
)
_TenantUnitListTable_Object = MibTable
tenantUnitListTable = _TenantUnitListTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 2, 1)
)
if mibBuilder.loadTexts:
    tenantUnitListTable.setStatus("current")
_TenantUnitListEntry_Object = MibTableRow
tenantUnitListEntry = _TenantUnitListEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 2, 1, 1)
)
tenantUnitListEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "tenantUnitListIdx"),
)
if mibBuilder.loadTexts:
    tenantUnitListEntry.setStatus("current")
_TenantUnitListIdx_Type = DDMibTableIndexTC
_TenantUnitListIdx_Object = MibTableColumn
tenantUnitListIdx = _TenantUnitListIdx_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 2, 1, 1, 1),
    _TenantUnitListIdx_Type()
)
tenantUnitListIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tenantUnitListIdx.setStatus("current")
_TenantUnitListName_Type = DDMibTableString256TC
_TenantUnitListName_Object = MibTableColumn
tenantUnitListName = _TenantUnitListName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 2, 1, 1, 2),
    _TenantUnitListName_Type()
)
tenantUnitListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tenantUnitListName.setStatus("current")
_TenantUnitListNumberOfMgmtUsers_Type = DDMibInteger32TC
_TenantUnitListNumberOfMgmtUsers_Object = MibTableColumn
tenantUnitListNumberOfMgmtUsers = _TenantUnitListNumberOfMgmtUsers_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 2, 1, 1, 3),
    _TenantUnitListNumberOfMgmtUsers_Type()
)
tenantUnitListNumberOfMgmtUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tenantUnitListNumberOfMgmtUsers.setStatus("current")
_TenantUnitListNumberOfMtrees_Type = DDMibInteger32TC
_TenantUnitListNumberOfMtrees_Object = MibTableColumn
tenantUnitListNumberOfMtrees = _TenantUnitListNumberOfMtrees_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 2, 1, 1, 4),
    _TenantUnitListNumberOfMtrees_Type()
)
tenantUnitListNumberOfMtrees.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tenantUnitListNumberOfMtrees.setStatus("current")
_TenantUnitListNumberOfDdboostStus_Type = DDMibInteger32TC
_TenantUnitListNumberOfDdboostStus_Object = MibTableColumn
tenantUnitListNumberOfDdboostStus = _TenantUnitListNumberOfDdboostStus_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 2, 1, 1, 5),
    _TenantUnitListNumberOfDdboostStus_Type()
)
tenantUnitListNumberOfDdboostStus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tenantUnitListNumberOfDdboostStus.setStatus("current")
_TenantUnitListTenantSelfServiceMode_Type = SmtStatusTC
_TenantUnitListTenantSelfServiceMode_Object = MibTableColumn
tenantUnitListTenantSelfServiceMode = _TenantUnitListTenantSelfServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 2, 1, 1, 6),
    _TenantUnitListTenantSelfServiceMode_Type()
)
tenantUnitListTenantSelfServiceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tenantUnitListTenantSelfServiceMode.setStatus("current")
_TenantUnitListParentTenantName_Type = DDMibTableString256TC
_TenantUnitListParentTenantName_Object = MibTableColumn
tenantUnitListParentTenantName = _TenantUnitListParentTenantName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 2, 1, 1, 7),
    _TenantUnitListParentTenantName_Type()
)
tenantUnitListParentTenantName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tenantUnitListParentTenantName.setStatus("current")
_TenantUnitListType_Type = DDMibTableString256TC
_TenantUnitListType_Object = MibTableColumn
tenantUnitListType = _TenantUnitListType_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 2, 1, 1, 8),
    _TenantUnitListType_Type()
)
tenantUnitListType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tenantUnitListType.setStatus("current")
_TenantUnitListSecurityMode_Type = TenantUnitSecurityModeTC
_TenantUnitListSecurityMode_Object = MibTableColumn
tenantUnitListSecurityMode = _TenantUnitListSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 2, 1, 1, 9),
    _TenantUnitListSecurityMode_Type()
)
tenantUnitListSecurityMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tenantUnitListSecurityMode.setStatus("current")
_TenantUnitListNumberOfMgmtGroups_Type = DDMibInteger32TC
_TenantUnitListNumberOfMgmtGroups_Object = MibTableColumn
tenantUnitListNumberOfMgmtGroups = _TenantUnitListNumberOfMgmtGroups_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 2, 1, 1, 10),
    _TenantUnitListNumberOfMgmtGroups_Type()
)
tenantUnitListNumberOfMgmtGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tenantUnitListNumberOfMgmtGroups.setStatus("current")
_TenantUnitMgmtUserList_ObjectIdentity = ObjectIdentity
tenantUnitMgmtUserList = _TenantUnitMgmtUserList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 3)
)
_TenantUnitMgmtUserListTable_Object = MibTable
tenantUnitMgmtUserListTable = _TenantUnitMgmtUserListTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 3, 1)
)
if mibBuilder.loadTexts:
    tenantUnitMgmtUserListTable.setStatus("current")
_TenantUnitMgmtUserListEntry_Object = MibTableRow
tenantUnitMgmtUserListEntry = _TenantUnitMgmtUserListEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 3, 1, 1)
)
tenantUnitMgmtUserListEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "tenantUnitListIdx"),
    (0, "DATA-DOMAIN-MIB", "tenantUnitMgmtUserListUserName"),
)
if mibBuilder.loadTexts:
    tenantUnitMgmtUserListEntry.setStatus("current")
_TenantUnitMgmtUserListUserName_Type = DDMibString96TC
_TenantUnitMgmtUserListUserName_Object = MibTableColumn
tenantUnitMgmtUserListUserName = _TenantUnitMgmtUserListUserName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 3, 1, 1, 2),
    _TenantUnitMgmtUserListUserName_Type()
)
tenantUnitMgmtUserListUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tenantUnitMgmtUserListUserName.setStatus("current")
_TenantUnitMgmtUserListUserRole_Type = TenantUnitMgmtUserListUserRoleTC
_TenantUnitMgmtUserListUserRole_Object = MibTableColumn
tenantUnitMgmtUserListUserRole = _TenantUnitMgmtUserListUserRole_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 3, 1, 1, 3),
    _TenantUnitMgmtUserListUserRole_Type()
)
tenantUnitMgmtUserListUserRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tenantUnitMgmtUserListUserRole.setStatus("current")
_TenantUnitMtreeList_ObjectIdentity = ObjectIdentity
tenantUnitMtreeList = _TenantUnitMtreeList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 4)
)
_TenantUnitMtreeListTable_Object = MibTable
tenantUnitMtreeListTable = _TenantUnitMtreeListTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 4, 1)
)
if mibBuilder.loadTexts:
    tenantUnitMtreeListTable.setStatus("current")
_TenantUnitMtreeListEntry_Object = MibTableRow
tenantUnitMtreeListEntry = _TenantUnitMtreeListEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 4, 1, 1)
)
tenantUnitMtreeListEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "tenantUnitListIdx"),
    (0, "DATA-DOMAIN-MIB", "tenantUnitMtreeListMtreeName"),
)
if mibBuilder.loadTexts:
    tenantUnitMtreeListEntry.setStatus("current")
_TenantUnitMtreeListMtreeName_Type = DDMibString96TC
_TenantUnitMtreeListMtreeName_Object = MibTableColumn
tenantUnitMtreeListMtreeName = _TenantUnitMtreeListMtreeName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 4, 1, 1, 2),
    _TenantUnitMtreeListMtreeName_Type()
)
tenantUnitMtreeListMtreeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tenantUnitMtreeListMtreeName.setStatus("current")
_TenantUnitDdboostStuList_ObjectIdentity = ObjectIdentity
tenantUnitDdboostStuList = _TenantUnitDdboostStuList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 5)
)
_TenantUnitDdboostStuListTable_Object = MibTable
tenantUnitDdboostStuListTable = _TenantUnitDdboostStuListTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 5, 1)
)
if mibBuilder.loadTexts:
    tenantUnitDdboostStuListTable.setStatus("current")
_TenantUnitDdboostStuListEntry_Object = MibTableRow
tenantUnitDdboostStuListEntry = _TenantUnitDdboostStuListEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 5, 1, 1)
)
tenantUnitDdboostStuListEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "tenantUnitListIdx"),
    (0, "DATA-DOMAIN-MIB", "tenantUnitDdboostStuListStuName"),
)
if mibBuilder.loadTexts:
    tenantUnitDdboostStuListEntry.setStatus("current")
_TenantUnitDdboostStuListStuName_Type = DDMibString96TC
_TenantUnitDdboostStuListStuName_Object = MibTableColumn
tenantUnitDdboostStuListStuName = _TenantUnitDdboostStuListStuName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 5, 1, 1, 2),
    _TenantUnitDdboostStuListStuName_Type()
)
tenantUnitDdboostStuListStuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tenantUnitDdboostStuListStuName.setStatus("current")
_TenantUnitAdminIpInfo_ObjectIdentity = ObjectIdentity
tenantUnitAdminIpInfo = _TenantUnitAdminIpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 6)
)
_TenantUnitAdminIpInfoTable_Object = MibTable
tenantUnitAdminIpInfoTable = _TenantUnitAdminIpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 6, 1)
)
if mibBuilder.loadTexts:
    tenantUnitAdminIpInfoTable.setStatus("current")
_TenantUnitAdminIpInfoEntry_Object = MibTableRow
tenantUnitAdminIpInfoEntry = _TenantUnitAdminIpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 6, 1, 1)
)
tenantUnitAdminIpInfoEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "tenantUnitListIdx"),
    (0, "DATA-DOMAIN-MIB", "tenantUnitAdminIpInfoAddr"),
)
if mibBuilder.loadTexts:
    tenantUnitAdminIpInfoEntry.setStatus("current")
_TenantUnitAdminIpInfoAddr_Type = DDMibString96TC
_TenantUnitAdminIpInfoAddr_Object = MibTableColumn
tenantUnitAdminIpInfoAddr = _TenantUnitAdminIpInfoAddr_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 6, 1, 1, 2),
    _TenantUnitAdminIpInfoAddr_Type()
)
tenantUnitAdminIpInfoAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tenantUnitAdminIpInfoAddr.setStatus("current")
_TenantUnitAdminIpInfoType_Type = DDMibString96TC
_TenantUnitAdminIpInfoType_Object = MibTableColumn
tenantUnitAdminIpInfoType = _TenantUnitAdminIpInfoType_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 6, 1, 1, 3),
    _TenantUnitAdminIpInfoType_Type()
)
tenantUnitAdminIpInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tenantUnitAdminIpInfoType.setStatus("current")
_TenantInfo_ObjectIdentity = ObjectIdentity
tenantInfo = _TenantInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 7)
)
_TenantInfoTable_Object = MibTable
tenantInfoTable = _TenantInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 7, 1)
)
if mibBuilder.loadTexts:
    tenantInfoTable.setStatus("current")
_TenantInfoEntry_Object = MibTableRow
tenantInfoEntry = _TenantInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 7, 1, 1)
)
tenantInfoEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "tenantInfoIdx"),
)
if mibBuilder.loadTexts:
    tenantInfoEntry.setStatus("current")
_TenantInfoIdx_Type = DDMibTableIndexTC
_TenantInfoIdx_Object = MibTableColumn
tenantInfoIdx = _TenantInfoIdx_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 7, 1, 1, 1),
    _TenantInfoIdx_Type()
)
tenantInfoIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tenantInfoIdx.setStatus("current")
_TenantInfoTenantName_Type = DDMibString96TC
_TenantInfoTenantName_Object = MibTableColumn
tenantInfoTenantName = _TenantInfoTenantName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 7, 1, 1, 2),
    _TenantInfoTenantName_Type()
)
tenantInfoTenantName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tenantInfoTenantName.setStatus("current")
_TenantInfoTenantUnitTable_Object = MibTable
tenantInfoTenantUnitTable = _TenantInfoTenantUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 7, 2)
)
if mibBuilder.loadTexts:
    tenantInfoTenantUnitTable.setStatus("current")
_TenantInfoTenantUnitEntry_Object = MibTableRow
tenantInfoTenantUnitEntry = _TenantInfoTenantUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 7, 2, 1)
)
tenantInfoTenantUnitEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "tenantInfoIdx"),
    (0, "DATA-DOMAIN-MIB", "tenantInfoTenantUnitName"),
)
if mibBuilder.loadTexts:
    tenantInfoTenantUnitEntry.setStatus("current")
_TenantInfoTenantUnitName_Type = DDMibString96TC
_TenantInfoTenantUnitName_Object = MibTableColumn
tenantInfoTenantUnitName = _TenantInfoTenantUnitName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 7, 2, 1, 2),
    _TenantInfoTenantUnitName_Type()
)
tenantInfoTenantUnitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tenantInfoTenantUnitName.setStatus("current")
_TenantUnitMgmtGroupList_ObjectIdentity = ObjectIdentity
tenantUnitMgmtGroupList = _TenantUnitMgmtGroupList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 8)
)
_TenantUnitMgmtGroupListTable_Object = MibTable
tenantUnitMgmtGroupListTable = _TenantUnitMgmtGroupListTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 8, 1)
)
if mibBuilder.loadTexts:
    tenantUnitMgmtGroupListTable.setStatus("current")
_TenantUnitMgmtGroupListEntry_Object = MibTableRow
tenantUnitMgmtGroupListEntry = _TenantUnitMgmtGroupListEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 8, 1, 1)
)
tenantUnitMgmtGroupListEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "tenantUnitListIdx"),
    (0, "DATA-DOMAIN-MIB", "tenantUnitMgmtGroupListGroupName"),
)
if mibBuilder.loadTexts:
    tenantUnitMgmtGroupListEntry.setStatus("current")
_TenantUnitMgmtGroupListGroupName_Type = DDMibString96TC
_TenantUnitMgmtGroupListGroupName_Object = MibTableColumn
tenantUnitMgmtGroupListGroupName = _TenantUnitMgmtGroupListGroupName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 8, 1, 1, 2),
    _TenantUnitMgmtGroupListGroupName_Type()
)
tenantUnitMgmtGroupListGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tenantUnitMgmtGroupListGroupName.setStatus("current")
_TenantUnitMgmtGroupListGroupRole_Type = TenantUnitMgmtUserListUserRoleTC
_TenantUnitMgmtGroupListGroupRole_Object = MibTableColumn
tenantUnitMgmtGroupListGroupRole = _TenantUnitMgmtGroupListGroupRole_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 8, 1, 1, 3),
    _TenantUnitMgmtGroupListGroupRole_Type()
)
tenantUnitMgmtGroupListGroupRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tenantUnitMgmtGroupListGroupRole.setStatus("current")
_TenantUnitMgmtGroupListGroupType_Type = TenantUnitMgmtGroupTypeTC
_TenantUnitMgmtGroupListGroupType_Object = MibTableColumn
tenantUnitMgmtGroupListGroupType = _TenantUnitMgmtGroupListGroupType_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 20, 8, 1, 1, 4),
    _TenantUnitMgmtGroupListGroupType_Type()
)
tenantUnitMgmtGroupListGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tenantUnitMgmtGroupListGroupType.setStatus("current")
_Quota_ObjectIdentity = ObjectIdentity
quota = _Quota_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 21)
)
_QuotaProperties_ObjectIdentity = ObjectIdentity
quotaProperties = _QuotaProperties_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 21, 1)
)
_QuotaCapacityStatus_Type = DDStatusTC
_QuotaCapacityStatus_Object = MibScalar
quotaCapacityStatus = _QuotaCapacityStatus_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 21, 1, 1),
    _QuotaCapacityStatus_Type()
)
quotaCapacityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    quotaCapacityStatus.setStatus("current")
_QuotaCapacity_ObjectIdentity = ObjectIdentity
quotaCapacity = _QuotaCapacity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 21, 2)
)
_QuotaCapacityTable_Object = MibTable
quotaCapacityTable = _QuotaCapacityTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 21, 2, 1)
)
if mibBuilder.loadTexts:
    quotaCapacityTable.setStatus("current")
_QuotaCapacityEntry_Object = MibTableRow
quotaCapacityEntry = _QuotaCapacityEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 21, 2, 1, 1)
)
quotaCapacityEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "quotaCapacityIndex"),
)
if mibBuilder.loadTexts:
    quotaCapacityEntry.setStatus("current")
_QuotaCapacityIndex_Type = DDMibTableIndexTC
_QuotaCapacityIndex_Object = MibTableColumn
quotaCapacityIndex = _QuotaCapacityIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 21, 2, 1, 1, 1),
    _QuotaCapacityIndex_Type()
)
quotaCapacityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    quotaCapacityIndex.setStatus("current")
_QuotaCapacityMtreeName_Type = DDMibTableString512TC
_QuotaCapacityMtreeName_Object = MibTableColumn
quotaCapacityMtreeName = _QuotaCapacityMtreeName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 21, 2, 1, 1, 2),
    _QuotaCapacityMtreeName_Type()
)
quotaCapacityMtreeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    quotaCapacityMtreeName.setStatus("current")
_QuotaCapacityPreCompMiB_Type = DDMibTableSizeMiBTC
_QuotaCapacityPreCompMiB_Object = MibTableColumn
quotaCapacityPreCompMiB = _QuotaCapacityPreCompMiB_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 21, 2, 1, 1, 3),
    _QuotaCapacityPreCompMiB_Type()
)
quotaCapacityPreCompMiB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    quotaCapacityPreCompMiB.setStatus("current")
_QuotaCapacitySoftLimitMiB_Type = DDMibTableSizeMiBTC
_QuotaCapacitySoftLimitMiB_Object = MibTableColumn
quotaCapacitySoftLimitMiB = _QuotaCapacitySoftLimitMiB_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 21, 2, 1, 1, 4),
    _QuotaCapacitySoftLimitMiB_Type()
)
quotaCapacitySoftLimitMiB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    quotaCapacitySoftLimitMiB.setStatus("current")
_QuotaCapacityHardLimitMiB_Type = DDMibTableSizeMiBTC
_QuotaCapacityHardLimitMiB_Object = MibTableColumn
quotaCapacityHardLimitMiB = _QuotaCapacityHardLimitMiB_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 21, 2, 1, 1, 5),
    _QuotaCapacityHardLimitMiB_Type()
)
quotaCapacityHardLimitMiB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    quotaCapacityHardLimitMiB.setStatus("current")
_QuotaCapacityTenantUnit_Type = DDMibTableString512TC
_QuotaCapacityTenantUnit_Object = MibTableColumn
quotaCapacityTenantUnit = _QuotaCapacityTenantUnit_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 21, 2, 1, 1, 6),
    _QuotaCapacityTenantUnit_Type()
)
quotaCapacityTenantUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    quotaCapacityTenantUnit.setStatus("current")
_HighAvailability_ObjectIdentity = ObjectIdentity
highAvailability = _HighAvailability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 22)
)
_HighAvailabilityStatus_ObjectIdentity = ObjectIdentity
highAvailabilityStatus = _HighAvailabilityStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 22, 1)
)
_HaSystemStatus_Type = DDMibString96TC
_HaSystemStatus_Object = MibScalar
haSystemStatus = _HaSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 22, 1, 1),
    _HaSystemStatus_Type()
)
haSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haSystemStatus.setStatus("current")
_LocalNodeRole_Type = DDMibString96TC
_LocalNodeRole_Object = MibScalar
localNodeRole = _LocalNodeRole_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 22, 1, 2),
    _LocalNodeRole_Type()
)
localNodeRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localNodeRole.setStatus("current")
_LocalHaState_Type = DDMibString96TC
_LocalHaState_Object = MibScalar
localHaState = _LocalHaState_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 22, 1, 3),
    _LocalHaState_Type()
)
localHaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localHaState.setStatus("current")
_PeerNodeRole_Type = DDMibString96TC
_PeerNodeRole_Object = MibScalar
peerNodeRole = _PeerNodeRole_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 22, 1, 4),
    _PeerNodeRole_Type()
)
peerNodeRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerNodeRole.setStatus("current")
_PeerHaState_Type = DDMibString96TC
_PeerHaState_Object = MibScalar
peerHaState = _PeerHaState_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 22, 1, 5),
    _PeerHaState_Type()
)
peerHaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerHaState.setStatus("current")
_HighAvailabilityConfig_ObjectIdentity = ObjectIdentity
highAvailabilityConfig = _HighAvailabilityConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 22, 2)
)
_HaConfiguredMode_Type = DDMibString96TC
_HaConfiguredMode_Object = MibScalar
haConfiguredMode = _HaConfiguredMode_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 22, 2, 1),
    _HaConfiguredMode_Type()
)
haConfiguredMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haConfiguredMode.setStatus("current")
_HaLocalPnodeId_Type = DDMibInteger32TC
_HaLocalPnodeId_Object = MibScalar
haLocalPnodeId = _HaLocalPnodeId_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 22, 2, 2),
    _HaLocalPnodeId_Type()
)
haLocalPnodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haLocalPnodeId.setStatus("current")
_Scsitarget_ObjectIdentity = ObjectIdentity
scsitarget = _Scsitarget_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23)
)
_ScsitargetProperties_ObjectIdentity = ObjectIdentity
scsitargetProperties = _ScsitargetProperties_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 1)
)
_ScsitargetAdminState_Type = DDMibString96TC
_ScsitargetAdminState_Object = MibScalar
scsitargetAdminState = _ScsitargetAdminState_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 1, 1),
    _ScsitargetAdminState_Type()
)
scsitargetAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetAdminState.setStatus("current")
_ScsitargetProcessState_Type = DDMibString96TC
_ScsitargetProcessState_Object = MibScalar
scsitargetProcessState = _ScsitargetProcessState_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 1, 2),
    _ScsitargetProcessState_Type()
)
scsitargetProcessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetProcessState.setStatus("current")
_ScsitargetGroup_ObjectIdentity = ObjectIdentity
scsitargetGroup = _ScsitargetGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 2)
)
_ScsitargetGroupTable_Object = MibTable
scsitargetGroupTable = _ScsitargetGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 2, 1)
)
if mibBuilder.loadTexts:
    scsitargetGroupTable.setStatus("current")
_ScsitargetGroupEntry_Object = MibTableRow
scsitargetGroupEntry = _ScsitargetGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 2, 1, 1)
)
scsitargetGroupEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "scsitargetGroupIndex"),
)
if mibBuilder.loadTexts:
    scsitargetGroupEntry.setStatus("current")
_ScsitargetGroupIndex_Type = DDMibTableIndexTC
_ScsitargetGroupIndex_Object = MibTableColumn
scsitargetGroupIndex = _ScsitargetGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 2, 1, 1, 1),
    _ScsitargetGroupIndex_Type()
)
scsitargetGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scsitargetGroupIndex.setStatus("current")
_ScsitargetGroupName_Type = DDMibTableString512TC
_ScsitargetGroupName_Object = MibTableColumn
scsitargetGroupName = _ScsitargetGroupName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 2, 1, 1, 2),
    _ScsitargetGroupName_Type()
)
scsitargetGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetGroupName.setStatus("current")
_ScsitargetGroupService_Type = DDMibTableString512TC
_ScsitargetGroupService_Object = MibTableColumn
scsitargetGroupService = _ScsitargetGroupService_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 2, 1, 1, 3),
    _ScsitargetGroupService_Type()
)
scsitargetGroupService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetGroupService.setStatus("current")
_ScsitargetGroupActiveState_Type = DDMibString96TC
_ScsitargetGroupActiveState_Object = MibTableColumn
scsitargetGroupActiveState = _ScsitargetGroupActiveState_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 2, 1, 1, 4),
    _ScsitargetGroupActiveState_Type()
)
scsitargetGroupActiveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetGroupActiveState.setStatus("current")
_ScsitargetGroupNumInitiators_Type = DDMibInteger32TC
_ScsitargetGroupNumInitiators_Object = MibTableColumn
scsitargetGroupNumInitiators = _ScsitargetGroupNumInitiators_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 2, 1, 1, 5),
    _ScsitargetGroupNumInitiators_Type()
)
scsitargetGroupNumInitiators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetGroupNumInitiators.setStatus("current")
_ScsitargetGroupNumDevices_Type = DDMibInteger32TC
_ScsitargetGroupNumDevices_Object = MibTableColumn
scsitargetGroupNumDevices = _ScsitargetGroupNumDevices_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 2, 1, 1, 6),
    _ScsitargetGroupNumDevices_Type()
)
scsitargetGroupNumDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetGroupNumDevices.setStatus("current")
_ScsitargetInitiator_ObjectIdentity = ObjectIdentity
scsitargetInitiator = _ScsitargetInitiator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 3)
)
_ScsitargetInitiatorTable_Object = MibTable
scsitargetInitiatorTable = _ScsitargetInitiatorTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 1)
)
if mibBuilder.loadTexts:
    scsitargetInitiatorTable.setStatus("current")
_ScsitargetInitiatorEntry_Object = MibTableRow
scsitargetInitiatorEntry = _ScsitargetInitiatorEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 1, 1)
)
scsitargetInitiatorEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "scsitargetInitiatorIndex"),
)
if mibBuilder.loadTexts:
    scsitargetInitiatorEntry.setStatus("current")
_ScsitargetInitiatorIndex_Type = DDMibTableIndexTC
_ScsitargetInitiatorIndex_Object = MibTableColumn
scsitargetInitiatorIndex = _ScsitargetInitiatorIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 1, 1, 1),
    _ScsitargetInitiatorIndex_Type()
)
scsitargetInitiatorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scsitargetInitiatorIndex.setStatus("current")
_ScsitargetInitiatorName_Type = DDMibTableString512TC
_ScsitargetInitiatorName_Object = MibTableColumn
scsitargetInitiatorName = _ScsitargetInitiatorName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 1, 1, 2),
    _ScsitargetInitiatorName_Type()
)
scsitargetInitiatorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetInitiatorName.setStatus("current")
_ScsitargetInitiatorSystemAddress_Type = DDMibTableString512TC
_ScsitargetInitiatorSystemAddress_Object = MibTableColumn
scsitargetInitiatorSystemAddress = _ScsitargetInitiatorSystemAddress_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 1, 1, 3),
    _ScsitargetInitiatorSystemAddress_Type()
)
scsitargetInitiatorSystemAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetInitiatorSystemAddress.setStatus("current")
_ScsitargetInitiatorGroup_Type = DDMibTableString512TC
_ScsitargetInitiatorGroup_Object = MibTableColumn
scsitargetInitiatorGroup = _ScsitargetInitiatorGroup_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 1, 1, 4),
    _ScsitargetInitiatorGroup_Type()
)
scsitargetInitiatorGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetInitiatorGroup.setStatus("current")
_ScsitargetInitiatorService_Type = DDMibTableString512TC
_ScsitargetInitiatorService_Object = MibTableColumn
scsitargetInitiatorService = _ScsitargetInitiatorService_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 1, 1, 5),
    _ScsitargetInitiatorService_Type()
)
scsitargetInitiatorService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetInitiatorService.setStatus("current")
_ScsitargetInitiatorAddressMethod_Type = DDMibTableString512TC
_ScsitargetInitiatorAddressMethod_Object = MibTableColumn
scsitargetInitiatorAddressMethod = _ScsitargetInitiatorAddressMethod_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 1, 1, 6),
    _ScsitargetInitiatorAddressMethod_Type()
)
scsitargetInitiatorAddressMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetInitiatorAddressMethod.setStatus("current")
_ScsitargetInitiatorTransport_Type = DDMibTableString512TC
_ScsitargetInitiatorTransport_Object = MibTableColumn
scsitargetInitiatorTransport = _ScsitargetInitiatorTransport_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 1, 1, 7),
    _ScsitargetInitiatorTransport_Type()
)
scsitargetInitiatorTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetInitiatorTransport.setStatus("current")
_ScsitargetInitiatorFcWwpn_Type = DDMibTableString512TC
_ScsitargetInitiatorFcWwpn_Object = MibTableColumn
scsitargetInitiatorFcWwpn = _ScsitargetInitiatorFcWwpn_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 1, 1, 8),
    _ScsitargetInitiatorFcWwpn_Type()
)
scsitargetInitiatorFcWwpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetInitiatorFcWwpn.setStatus("current")
_ScsitargetInitiatorFcWwnn_Type = DDMibTableString512TC
_ScsitargetInitiatorFcWwnn_Object = MibTableColumn
scsitargetInitiatorFcWwnn = _ScsitargetInitiatorFcWwnn_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 1, 1, 9),
    _ScsitargetInitiatorFcWwnn_Type()
)
scsitargetInitiatorFcWwnn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetInitiatorFcWwnn.setStatus("current")
_ScsitargetInitiatorFcSymbolicPortName_Type = DDMibTableString512TC
_ScsitargetInitiatorFcSymbolicPortName_Object = MibTableColumn
scsitargetInitiatorFcSymbolicPortName = _ScsitargetInitiatorFcSymbolicPortName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 1, 1, 10),
    _ScsitargetInitiatorFcSymbolicPortName_Type()
)
scsitargetInitiatorFcSymbolicPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetInitiatorFcSymbolicPortName.setStatus("current")
_ScsitargetInitiatorEndpTable_Object = MibTable
scsitargetInitiatorEndpTable = _ScsitargetInitiatorEndpTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 2)
)
if mibBuilder.loadTexts:
    scsitargetInitiatorEndpTable.setStatus("current")
_ScsitargetInitiatorEndpEntry_Object = MibTableRow
scsitargetInitiatorEndpEntry = _ScsitargetInitiatorEndpEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 2, 1)
)
scsitargetInitiatorEndpEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "scsitargetInitiatorEndpIndex"),
)
if mibBuilder.loadTexts:
    scsitargetInitiatorEndpEntry.setStatus("current")
_ScsitargetInitiatorEndpIndex_Type = DDMibTableIndexTC
_ScsitargetInitiatorEndpIndex_Object = MibTableColumn
scsitargetInitiatorEndpIndex = _ScsitargetInitiatorEndpIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 2, 1, 1),
    _ScsitargetInitiatorEndpIndex_Type()
)
scsitargetInitiatorEndpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scsitargetInitiatorEndpIndex.setStatus("current")
_ScsitargetInitiatorEndpInitiator_Type = DDMibTableString512TC
_ScsitargetInitiatorEndpInitiator_Object = MibTableColumn
scsitargetInitiatorEndpInitiator = _ScsitargetInitiatorEndpInitiator_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 2, 1, 2),
    _ScsitargetInitiatorEndpInitiator_Type()
)
scsitargetInitiatorEndpInitiator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetInitiatorEndpInitiator.setStatus("current")
_ScsitargetInitiatorEndpEndpoint_Type = DDMibTableString512TC
_ScsitargetInitiatorEndpEndpoint_Object = MibTableColumn
scsitargetInitiatorEndpEndpoint = _ScsitargetInitiatorEndpEndpoint_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 2, 1, 3),
    _ScsitargetInitiatorEndpEndpoint_Type()
)
scsitargetInitiatorEndpEndpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetInitiatorEndpEndpoint.setStatus("current")
_ScsitargetInitiatorEndpStatus_Type = DDMibString96TC
_ScsitargetInitiatorEndpStatus_Object = MibTableColumn
scsitargetInitiatorEndpStatus = _ScsitargetInitiatorEndpStatus_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 2, 1, 4),
    _ScsitargetInitiatorEndpStatus_Type()
)
scsitargetInitiatorEndpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetInitiatorEndpStatus.setStatus("current")
_ScsitargetEndpoint_ObjectIdentity = ObjectIdentity
scsitargetEndpoint = _ScsitargetEndpoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 4)
)
_ScsitargetEndpointTable_Object = MibTable
scsitargetEndpointTable = _ScsitargetEndpointTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 4, 1)
)
if mibBuilder.loadTexts:
    scsitargetEndpointTable.setStatus("current")
_ScsitargetEndpointEntry_Object = MibTableRow
scsitargetEndpointEntry = _ScsitargetEndpointEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 4, 1, 1)
)
scsitargetEndpointEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "scsitargetEndpointIndex"),
)
if mibBuilder.loadTexts:
    scsitargetEndpointEntry.setStatus("current")
_ScsitargetEndpointIndex_Type = DDMibTableIndexTC
_ScsitargetEndpointIndex_Object = MibTableColumn
scsitargetEndpointIndex = _ScsitargetEndpointIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 4, 1, 1, 1),
    _ScsitargetEndpointIndex_Type()
)
scsitargetEndpointIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scsitargetEndpointIndex.setStatus("current")
_ScsitargetEndpointName_Type = DDMibTableString512TC
_ScsitargetEndpointName_Object = MibTableColumn
scsitargetEndpointName = _ScsitargetEndpointName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 4, 1, 1, 2),
    _ScsitargetEndpointName_Type()
)
scsitargetEndpointName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetEndpointName.setStatus("current")
_ScsitargetEndpointCurrentSystemAddress_Type = DDMibTableString512TC
_ScsitargetEndpointCurrentSystemAddress_Object = MibTableColumn
scsitargetEndpointCurrentSystemAddress = _ScsitargetEndpointCurrentSystemAddress_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 4, 1, 1, 3),
    _ScsitargetEndpointCurrentSystemAddress_Type()
)
scsitargetEndpointCurrentSystemAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetEndpointCurrentSystemAddress.setStatus("current")
_ScsitargetEndpointPrimarySystemAddress_Type = DDMibTableString512TC
_ScsitargetEndpointPrimarySystemAddress_Object = MibTableColumn
scsitargetEndpointPrimarySystemAddress = _ScsitargetEndpointPrimarySystemAddress_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 4, 1, 1, 4),
    _ScsitargetEndpointPrimarySystemAddress_Type()
)
scsitargetEndpointPrimarySystemAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetEndpointPrimarySystemAddress.setStatus("current")
_ScsitargetEndpointSecondarySystemAddress_Type = DDMibTableString512TC
_ScsitargetEndpointSecondarySystemAddress_Object = MibTableColumn
scsitargetEndpointSecondarySystemAddress = _ScsitargetEndpointSecondarySystemAddress_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 4, 1, 1, 5),
    _ScsitargetEndpointSecondarySystemAddress_Type()
)
scsitargetEndpointSecondarySystemAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetEndpointSecondarySystemAddress.setStatus("current")
_ScsitargetEndpointEnabled_Type = DDStatusTC
_ScsitargetEndpointEnabled_Object = MibTableColumn
scsitargetEndpointEnabled = _ScsitargetEndpointEnabled_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 4, 1, 1, 6),
    _ScsitargetEndpointEnabled_Type()
)
scsitargetEndpointEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetEndpointEnabled.setStatus("current")
_ScsitargetEndpointStatus_Type = DDMibTableString512TC
_ScsitargetEndpointStatus_Object = MibTableColumn
scsitargetEndpointStatus = _ScsitargetEndpointStatus_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 4, 1, 1, 7),
    _ScsitargetEndpointStatus_Type()
)
scsitargetEndpointStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetEndpointStatus.setStatus("current")
_ScsitargetEndpointTransport_Type = DDMibTableString512TC
_ScsitargetEndpointTransport_Object = MibTableColumn
scsitargetEndpointTransport = _ScsitargetEndpointTransport_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 4, 1, 1, 8),
    _ScsitargetEndpointTransport_Type()
)
scsitargetEndpointTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetEndpointTransport.setStatus("current")
_ScsitargetEndpointFcWwnn_Type = DDMibTableString512TC
_ScsitargetEndpointFcWwnn_Object = MibTableColumn
scsitargetEndpointFcWwnn = _ScsitargetEndpointFcWwnn_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 4, 1, 1, 9),
    _ScsitargetEndpointFcWwnn_Type()
)
scsitargetEndpointFcWwnn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetEndpointFcWwnn.setStatus("current")
_ScsitargetEndpointFcWwpn_Type = DDMibTableString512TC
_ScsitargetEndpointFcWwpn_Object = MibTableColumn
scsitargetEndpointFcWwpn = _ScsitargetEndpointFcWwpn_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 4, 1, 1, 10),
    _ScsitargetEndpointFcWwpn_Type()
)
scsitargetEndpointFcWwpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetEndpointFcWwpn.setStatus("current")
_ScsitargetPort_ObjectIdentity = ObjectIdentity
scsitargetPort = _ScsitargetPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 5)
)
_ScsitargetPortTable_Object = MibTable
scsitargetPortTable = _ScsitargetPortTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1)
)
if mibBuilder.loadTexts:
    scsitargetPortTable.setStatus("current")
_ScsitargetPortEntry_Object = MibTableRow
scsitargetPortEntry = _ScsitargetPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1)
)
scsitargetPortEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "scsitargetPortIndex"),
)
if mibBuilder.loadTexts:
    scsitargetPortEntry.setStatus("current")
_ScsitargetPortIndex_Type = DDMibTableIndexTC
_ScsitargetPortIndex_Object = MibTableColumn
scsitargetPortIndex = _ScsitargetPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 1),
    _ScsitargetPortIndex_Type()
)
scsitargetPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scsitargetPortIndex.setStatus("current")
_ScsitargetPortSystemAddress_Type = DDMibTableString512TC
_ScsitargetPortSystemAddress_Object = MibTableColumn
scsitargetPortSystemAddress = _ScsitargetPortSystemAddress_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 2),
    _ScsitargetPortSystemAddress_Type()
)
scsitargetPortSystemAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetPortSystemAddress.setStatus("current")
_ScsitargetPortEnabled_Type = DDStatusTC
_ScsitargetPortEnabled_Object = MibTableColumn
scsitargetPortEnabled = _ScsitargetPortEnabled_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 3),
    _ScsitargetPortEnabled_Type()
)
scsitargetPortEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetPortEnabled.setStatus("current")
_ScsitargetPortStatus_Type = DDMibTableString512TC
_ScsitargetPortStatus_Object = MibTableColumn
scsitargetPortStatus = _ScsitargetPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 4),
    _ScsitargetPortStatus_Type()
)
scsitargetPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetPortStatus.setStatus("current")
_ScsitargetPortTransport_Type = DDMibTableString512TC
_ScsitargetPortTransport_Object = MibTableColumn
scsitargetPortTransport = _ScsitargetPortTransport_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 5),
    _ScsitargetPortTransport_Type()
)
scsitargetPortTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetPortTransport.setStatus("current")
_ScsitargetPortOperationalStatus_Type = DDMibTableString512TC
_ScsitargetPortOperationalStatus_Object = MibTableColumn
scsitargetPortOperationalStatus = _ScsitargetPortOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 6),
    _ScsitargetPortOperationalStatus_Type()
)
scsitargetPortOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetPortOperationalStatus.setStatus("current")
_ScsitargetPortFcNpiv_Type = DDMibTableString512TC
_ScsitargetPortFcNpiv_Object = MibTableColumn
scsitargetPortFcNpiv = _ScsitargetPortFcNpiv_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 7),
    _ScsitargetPortFcNpiv_Type()
)
scsitargetPortFcNpiv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetPortFcNpiv.setStatus("current")
_ScsitargetPortPortId_Type = DDMibTableString512TC
_ScsitargetPortPortId_Object = MibTableColumn
scsitargetPortPortId = _ScsitargetPortPortId_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 8),
    _ScsitargetPortPortId_Type()
)
scsitargetPortPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetPortPortId.setStatus("current")
_ScsitargetPortModel_Type = DDMibTableString512TC
_ScsitargetPortModel_Object = MibTableColumn
scsitargetPortModel = _ScsitargetPortModel_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 9),
    _ScsitargetPortModel_Type()
)
scsitargetPortModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetPortModel.setStatus("current")
_ScsitargetPortFirmware_Type = DDMibTableString512TC
_ScsitargetPortFirmware_Object = MibTableColumn
scsitargetPortFirmware = _ScsitargetPortFirmware_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 10),
    _ScsitargetPortFirmware_Type()
)
scsitargetPortFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetPortFirmware.setStatus("current")
_ScsitargetPortFcBaseWwnn_Type = DDMibTableString512TC
_ScsitargetPortFcBaseWwnn_Object = MibTableColumn
scsitargetPortFcBaseWwnn = _ScsitargetPortFcBaseWwnn_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 11),
    _ScsitargetPortFcBaseWwnn_Type()
)
scsitargetPortFcBaseWwnn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetPortFcBaseWwnn.setStatus("current")
_ScsitargetPortFcBaseWwpn_Type = DDMibTableString512TC
_ScsitargetPortFcBaseWwpn_Object = MibTableColumn
scsitargetPortFcBaseWwpn = _ScsitargetPortFcBaseWwpn_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 12),
    _ScsitargetPortFcBaseWwpn_Type()
)
scsitargetPortFcBaseWwpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetPortFcBaseWwpn.setStatus("current")
_ScsitargetPortFcCurrentWwnn_Type = DDMibTableString512TC
_ScsitargetPortFcCurrentWwnn_Object = MibTableColumn
scsitargetPortFcCurrentWwnn = _ScsitargetPortFcCurrentWwnn_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 13),
    _ScsitargetPortFcCurrentWwnn_Type()
)
scsitargetPortFcCurrentWwnn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetPortFcCurrentWwnn.setStatus("current")
_ScsitargetPortFcCurrentWwpn_Type = DDMibTableString512TC
_ScsitargetPortFcCurrentWwpn_Object = MibTableColumn
scsitargetPortFcCurrentWwpn = _ScsitargetPortFcCurrentWwpn_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 14),
    _ScsitargetPortFcCurrentWwpn_Type()
)
scsitargetPortFcCurrentWwpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetPortFcCurrentWwpn.setStatus("current")
_ScsitargetPortFcp2Retry_Type = DDMibTableString512TC
_ScsitargetPortFcp2Retry_Object = MibTableColumn
scsitargetPortFcp2Retry = _ScsitargetPortFcp2Retry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 15),
    _ScsitargetPortFcp2Retry_Type()
)
scsitargetPortFcp2Retry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetPortFcp2Retry.setStatus("current")
_ScsitargetPortConnectionType_Type = DDMibTableString512TC
_ScsitargetPortConnectionType_Object = MibTableColumn
scsitargetPortConnectionType = _ScsitargetPortConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 16),
    _ScsitargetPortConnectionType_Type()
)
scsitargetPortConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetPortConnectionType.setStatus("current")
_ScsitargetPortLinkSpeed_Type = DDMibTableString512TC
_ScsitargetPortLinkSpeed_Object = MibTableColumn
scsitargetPortLinkSpeed = _ScsitargetPortLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 17),
    _ScsitargetPortLinkSpeed_Type()
)
scsitargetPortLinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetPortLinkSpeed.setStatus("current")
_ScsitargetPortFcTopology_Type = DDMibTableString512TC
_ScsitargetPortFcTopology_Object = MibTableColumn
scsitargetPortFcTopology = _ScsitargetPortFcTopology_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 18),
    _ScsitargetPortFcTopology_Type()
)
scsitargetPortFcTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetPortFcTopology.setStatus("current")
_ScsitargetPortEndpTable_Object = MibTable
scsitargetPortEndpTable = _ScsitargetPortEndpTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 2)
)
if mibBuilder.loadTexts:
    scsitargetPortEndpTable.setStatus("current")
_ScsitargetPortEndpEntry_Object = MibTableRow
scsitargetPortEndpEntry = _ScsitargetPortEndpEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 2, 1)
)
scsitargetPortEndpEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "scsitargetPortEndpIndex"),
)
if mibBuilder.loadTexts:
    scsitargetPortEndpEntry.setStatus("current")
_ScsitargetPortEndpIndex_Type = DDMibTableIndexTC
_ScsitargetPortEndpIndex_Object = MibTableColumn
scsitargetPortEndpIndex = _ScsitargetPortEndpIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 2, 1, 1),
    _ScsitargetPortEndpIndex_Type()
)
scsitargetPortEndpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scsitargetPortEndpIndex.setStatus("current")
_ScsitargetPortEndpPort_Type = DDMibTableString512TC
_ScsitargetPortEndpPort_Object = MibTableColumn
scsitargetPortEndpPort = _ScsitargetPortEndpPort_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 2, 1, 2),
    _ScsitargetPortEndpPort_Type()
)
scsitargetPortEndpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetPortEndpPort.setStatus("current")
_ScsitargetPortEndpEndpoint_Type = DDMibTableString512TC
_ScsitargetPortEndpEndpoint_Object = MibTableColumn
scsitargetPortEndpEndpoint = _ScsitargetPortEndpEndpoint_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 2, 1, 3),
    _ScsitargetPortEndpEndpoint_Type()
)
scsitargetPortEndpEndpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetPortEndpEndpoint.setStatus("current")
_ScsitargetPortEndpEnabled_Type = DDStatusTC
_ScsitargetPortEndpEnabled_Object = MibTableColumn
scsitargetPortEndpEnabled = _ScsitargetPortEndpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 2, 1, 4),
    _ScsitargetPortEndpEnabled_Type()
)
scsitargetPortEndpEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetPortEndpEnabled.setStatus("current")
_ScsitargetPortEndpStatus_Type = DDMibString96TC
_ScsitargetPortEndpStatus_Object = MibTableColumn
scsitargetPortEndpStatus = _ScsitargetPortEndpStatus_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 2, 1, 5),
    _ScsitargetPortEndpStatus_Type()
)
scsitargetPortEndpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetPortEndpStatus.setStatus("current")
_ScsitargetPortEndpCurrentInstance_Type = DDMibTableString512TC
_ScsitargetPortEndpCurrentInstance_Object = MibTableColumn
scsitargetPortEndpCurrentInstance = _ScsitargetPortEndpCurrentInstance_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 2, 1, 6),
    _ScsitargetPortEndpCurrentInstance_Type()
)
scsitargetPortEndpCurrentInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetPortEndpCurrentInstance.setStatus("current")
_ScsitargetDevice_ObjectIdentity = ObjectIdentity
scsitargetDevice = _ScsitargetDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 6)
)
_ScsitargetDeviceTable_Object = MibTable
scsitargetDeviceTable = _ScsitargetDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 1)
)
if mibBuilder.loadTexts:
    scsitargetDeviceTable.setStatus("current")
_ScsitargetDeviceEntry_Object = MibTableRow
scsitargetDeviceEntry = _ScsitargetDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 1, 1)
)
scsitargetDeviceEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "scsitargetDeviceIndex"),
)
if mibBuilder.loadTexts:
    scsitargetDeviceEntry.setStatus("current")
_ScsitargetDeviceIndex_Type = DDMibTableIndexTC
_ScsitargetDeviceIndex_Object = MibTableColumn
scsitargetDeviceIndex = _ScsitargetDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 1, 1, 1),
    _ScsitargetDeviceIndex_Type()
)
scsitargetDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scsitargetDeviceIndex.setStatus("current")
_ScsitargetDeviceName_Type = DDMibTableString512TC
_ScsitargetDeviceName_Object = MibTableColumn
scsitargetDeviceName = _ScsitargetDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 1, 1, 2),
    _ScsitargetDeviceName_Type()
)
scsitargetDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetDeviceName.setStatus("current")
_ScsitargetDeviceService_Type = DDMibTableString512TC
_ScsitargetDeviceService_Object = MibTableColumn
scsitargetDeviceService = _ScsitargetDeviceService_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 1, 1, 3),
    _ScsitargetDeviceService_Type()
)
scsitargetDeviceService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetDeviceService.setStatus("current")
_ScsitargetDeviceActiveState_Type = DDMibString96TC
_ScsitargetDeviceActiveState_Object = MibTableColumn
scsitargetDeviceActiveState = _ScsitargetDeviceActiveState_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 1, 1, 4),
    _ScsitargetDeviceActiveState_Type()
)
scsitargetDeviceActiveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetDeviceActiveState.setStatus("current")
_ScsitargetDeviceAddress_Type = DDMibTableString512TC
_ScsitargetDeviceAddress_Object = MibTableColumn
scsitargetDeviceAddress = _ScsitargetDeviceAddress_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 1, 1, 5),
    _ScsitargetDeviceAddress_Type()
)
scsitargetDeviceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetDeviceAddress.setStatus("current")
_ScsitargetDeviceGrpTable_Object = MibTable
scsitargetDeviceGrpTable = _ScsitargetDeviceGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 2)
)
if mibBuilder.loadTexts:
    scsitargetDeviceGrpTable.setStatus("current")
_ScsitargetDeviceGrpEntry_Object = MibTableRow
scsitargetDeviceGrpEntry = _ScsitargetDeviceGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 2, 1)
)
scsitargetDeviceGrpEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "scsitargetDeviceGrpIndex"),
)
if mibBuilder.loadTexts:
    scsitargetDeviceGrpEntry.setStatus("current")
_ScsitargetDeviceGrpIndex_Type = DDMibTableIndexTC
_ScsitargetDeviceGrpIndex_Object = MibTableColumn
scsitargetDeviceGrpIndex = _ScsitargetDeviceGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 2, 1, 1),
    _ScsitargetDeviceGrpIndex_Type()
)
scsitargetDeviceGrpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scsitargetDeviceGrpIndex.setStatus("current")
_ScsitargetDeviceGrpDevice_Type = DDMibTableString512TC
_ScsitargetDeviceGrpDevice_Object = MibTableColumn
scsitargetDeviceGrpDevice = _ScsitargetDeviceGrpDevice_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 2, 1, 2),
    _ScsitargetDeviceGrpDevice_Type()
)
scsitargetDeviceGrpDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetDeviceGrpDevice.setStatus("current")
_ScsitargetDeviceGrpGroupName_Type = DDMibTableString512TC
_ScsitargetDeviceGrpGroupName_Object = MibTableColumn
scsitargetDeviceGrpGroupName = _ScsitargetDeviceGrpGroupName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 2, 1, 3),
    _ScsitargetDeviceGrpGroupName_Type()
)
scsitargetDeviceGrpGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetDeviceGrpGroupName.setStatus("current")
_ScsitargetDeviceGrpLun_Type = DDMibTableString512TC
_ScsitargetDeviceGrpLun_Object = MibTableColumn
scsitargetDeviceGrpLun = _ScsitargetDeviceGrpLun_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 2, 1, 4),
    _ScsitargetDeviceGrpLun_Type()
)
scsitargetDeviceGrpLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetDeviceGrpLun.setStatus("current")
_ScsitargetDeviceGrpPrimaryEndpoints_Type = DDMibTableString512TC
_ScsitargetDeviceGrpPrimaryEndpoints_Object = MibTableColumn
scsitargetDeviceGrpPrimaryEndpoints = _ScsitargetDeviceGrpPrimaryEndpoints_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 2, 1, 5),
    _ScsitargetDeviceGrpPrimaryEndpoints_Type()
)
scsitargetDeviceGrpPrimaryEndpoints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetDeviceGrpPrimaryEndpoints.setStatus("current")
_ScsitargetDeviceGrpSecondaryEndpoints_Type = DDMibTableString512TC
_ScsitargetDeviceGrpSecondaryEndpoints_Object = MibTableColumn
scsitargetDeviceGrpSecondaryEndpoints = _ScsitargetDeviceGrpSecondaryEndpoints_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 2, 1, 6),
    _ScsitargetDeviceGrpSecondaryEndpoints_Type()
)
scsitargetDeviceGrpSecondaryEndpoints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetDeviceGrpSecondaryEndpoints.setStatus("current")
_ScsitargetDeviceGrpInUseEndpoints_Type = DDMibTableString512TC
_ScsitargetDeviceGrpInUseEndpoints_Object = MibTableColumn
scsitargetDeviceGrpInUseEndpoints = _ScsitargetDeviceGrpInUseEndpoints_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 2, 1, 7),
    _ScsitargetDeviceGrpInUseEndpoints_Type()
)
scsitargetDeviceGrpInUseEndpoints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsitargetDeviceGrpInUseEndpoints.setStatus("current")
_DataDomainMibNotifications_ObjectIdentity = ObjectIdentity
dataDomainMibNotifications = _DataDomainMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 2)
)
_DataDomainMibTraps_ObjectIdentity = ObjectIdentity
dataDomainMibTraps = _DataDomainMibTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0)
)
_DataDomainMibProducts_ObjectIdentity = ObjectIdentity
dataDomainMibProducts = _DataDomainMibProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3)
)
_Restorer_ObjectIdentity = ObjectIdentity
restorer = _Restorer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1)
)
_Unknown_ObjectIdentity = ObjectIdentity
unknown = _Unknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 0)
)
_Dd200_ObjectIdentity = ObjectIdentity
dd200 = _Dd200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 1)
)
_Dd200Proto_ObjectIdentity = ObjectIdentity
dd200Proto = _Dd200Proto_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 2)
)
_Dd410_ObjectIdentity = ObjectIdentity
dd410 = _Dd410_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 3)
)
_Dd430_ObjectIdentity = ObjectIdentity
dd430 = _Dd430_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 4)
)
_Dd460_ObjectIdentity = ObjectIdentity
dd460 = _Dd460_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 5)
)
_Dd400g_ObjectIdentity = ObjectIdentity
dd400g = _Dd400g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 6)
)
_Dd460g_ObjectIdentity = ObjectIdentity
dd460g = _Dd460g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 7)
)
_Dd560_ObjectIdentity = ObjectIdentity
dd560 = _Dd560_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 8)
)
_Dd560g_ObjectIdentity = ObjectIdentity
dd560g = _Dd560g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 9)
)
_Dd580_ObjectIdentity = ObjectIdentity
dd580 = _Dd580_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 10)
)
_Dd580g_ObjectIdentity = ObjectIdentity
dd580g = _Dd580g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 11)
)
_Dd565_ObjectIdentity = ObjectIdentity
dd565 = _Dd565_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 12)
)
_Dd530_ObjectIdentity = ObjectIdentity
dd530 = _Dd530_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 13)
)
_Dd510_ObjectIdentity = ObjectIdentity
dd510 = _Dd510_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 14)
)
_Dd120_ObjectIdentity = ObjectIdentity
dd120 = _Dd120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 15)
)
_Dd690_ObjectIdentity = ObjectIdentity
dd690 = _Dd690_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 16)
)
_Dd690g_ObjectIdentity = ObjectIdentity
dd690g = _Dd690g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 17)
)
_Dd660_ObjectIdentity = ObjectIdentity
dd660 = _Dd660_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 18)
)
_Dd880_ObjectIdentity = ObjectIdentity
dd880 = _Dd880_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 19)
)
_Dd880g_ObjectIdentity = ObjectIdentity
dd880g = _Dd880g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 20)
)
_Dd610_ObjectIdentity = ObjectIdentity
dd610 = _Dd610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 21)
)
_Dd630_ObjectIdentity = ObjectIdentity
dd630 = _Dd630_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 22)
)
_Dd140_ObjectIdentity = ObjectIdentity
dd140 = _Dd140_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 23)
)
_Dd670_ObjectIdentity = ObjectIdentity
dd670 = _Dd670_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 24)
)
_Dd860_ObjectIdentity = ObjectIdentity
dd860 = _Dd860_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 25)
)
_Dd860g_ObjectIdentity = ObjectIdentity
dd860g = _Dd860g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 26)
)
_Dd890_ObjectIdentity = ObjectIdentity
dd890 = _Dd890_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 27)
)
_Dd640_ObjectIdentity = ObjectIdentity
dd640 = _Dd640_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 28)
)
_Dd620_ObjectIdentity = ObjectIdentity
dd620 = _Dd620_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 29)
)
_Dd160_ObjectIdentity = ObjectIdentity
dd160 = _Dd160_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 30)
)
_Ddintrepid_ObjectIdentity = ObjectIdentity
ddintrepid = _Ddintrepid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 31)
)
_Dd4500_ObjectIdentity = ObjectIdentity
dd4500 = _Dd4500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 32)
)
_Dd7200_ObjectIdentity = ObjectIdentity
dd7200 = _Dd7200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 33)
)
_Ddve_ObjectIdentity = ObjectIdentity
ddve = _Ddve_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 34)
)
_Dd990_ObjectIdentity = ObjectIdentity
dd990 = _Dd990_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 35)
)
_Dd2500_ObjectIdentity = ObjectIdentity
dd2500 = _Dd2500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 36)
)
_Dd4200_ObjectIdentity = ObjectIdentity
dd4200 = _Dd4200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 37)
)
_Ddkoalam1_ObjectIdentity = ObjectIdentity
ddkoalam1 = _Ddkoalam1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 38)
)
_Apollo_ObjectIdentity = ObjectIdentity
apollo = _Apollo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 39)
)
_Unset_ObjectIdentity = ObjectIdentity
unset = _Unset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 9999)
)

# Managed Objects groups

environmentalsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19746, 0, 2, 1)
)
environmentalsGroup.setObjects(
      *(("DATA-DOMAIN-MIB", "powerModuleDescription"),
        ("DATA-DOMAIN-MIB", "powerModuleStatus"),
        ("DATA-DOMAIN-MIB", "tempSensorDescription"),
        ("DATA-DOMAIN-MIB", "tempSensorCurrentValue"),
        ("DATA-DOMAIN-MIB", "tempSensorStatus"),
        ("DATA-DOMAIN-MIB", "fanDescription"),
        ("DATA-DOMAIN-MIB", "fanLevel"),
        ("DATA-DOMAIN-MIB", "fanStatus"),
        ("DATA-DOMAIN-MIB", "tempSensorTrapIndex"),
        ("DATA-DOMAIN-MIB", "fanTrapIndex"))
)
if mibBuilder.loadTexts:
    environmentalsGroup.setStatus("current")

nvramGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19746, 0, 2, 2)
)
nvramGroup.setObjects(
      *(("DATA-DOMAIN-MIB", "nvramMemorySize"),
        ("DATA-DOMAIN-MIB", "nvramWindowSize"),
        ("DATA-DOMAIN-MIB", "nvramPCIErrorCount"),
        ("DATA-DOMAIN-MIB", "nvramMemoryErrorCount"),
        ("DATA-DOMAIN-MIB", "nvramBatteryStatus"),
        ("DATA-DOMAIN-MIB", "nvramBatteryCharge"),
        ("DATA-DOMAIN-MIB", "nvramHCMemorySize"))
)
if mibBuilder.loadTexts:
    nvramGroup.setStatus("current")

fileSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19746, 0, 2, 3)
)
fileSystemGroup.setObjects(
      *(("DATA-DOMAIN-MIB", "fileSystemStatus"),
        ("DATA-DOMAIN-MIB", "fileSystemVirtualSpace"),
        ("DATA-DOMAIN-MIB", "fileSystemResourceName"),
        ("DATA-DOMAIN-MIB", "fileSystemSpaceSize"),
        ("DATA-DOMAIN-MIB", "fileSystemSpaceUsed"),
        ("DATA-DOMAIN-MIB", "fileSystemSpaceAvail"),
        ("DATA-DOMAIN-MIB", "fileSystemPercentUsed"),
        ("DATA-DOMAIN-MIB", "fileSystemSpaceCleanable"),
        ("DATA-DOMAIN-MIB", "fileSystemCompressionPeriod"),
        ("DATA-DOMAIN-MIB", "fileSystemCompressionStartTime"),
        ("DATA-DOMAIN-MIB", "fileSystemCompressionEndTime"),
        ("DATA-DOMAIN-MIB", "fileSystemPreCompressionSize"),
        ("DATA-DOMAIN-MIB", "fileSystemPostCompressionSize"),
        ("DATA-DOMAIN-MIB", "fileSystemGlobalCompressionFactor"),
        ("DATA-DOMAIN-MIB", "fileSystemLocalCompressionFactor"),
        ("DATA-DOMAIN-MIB", "fileSystemTotalCompressionFactor"),
        ("DATA-DOMAIN-MIB", "fileSystemReductionPercent"))
)
if mibBuilder.loadTexts:
    fileSystemGroup.setStatus("deprecated")

alertsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19746, 0, 2, 4)
)
alertsGroup.setObjects(
      *(("DATA-DOMAIN-MIB", "currentAlertTimestamp"),
        ("DATA-DOMAIN-MIB", "currentAlertDescription"),
        ("DATA-DOMAIN-MIB", "currentAlertSeverity"),
        ("DATA-DOMAIN-MIB", "currentAlertID"),
        ("DATA-DOMAIN-MIB", "alertHistoryTimestamp"),
        ("DATA-DOMAIN-MIB", "alertHistoryDescription"),
        ("DATA-DOMAIN-MIB", "alertHistorySeverity"),
        ("DATA-DOMAIN-MIB", "alertHistoryStatus"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    alertsGroup.setStatus("current")

statisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19746, 0, 2, 5)
)
statisticsGroup.setObjects(
      *(("DATA-DOMAIN-MIB", "cpuAvgPercentageBusy"),
        ("DATA-DOMAIN-MIB", "cpuMaxPercentageBusy"),
        ("DATA-DOMAIN-MIB", "nfsOpsPerSecond"),
        ("DATA-DOMAIN-MIB", "nfsIdlePercentage"),
        ("DATA-DOMAIN-MIB", "nfsProcPercentage"),
        ("DATA-DOMAIN-MIB", "nfsSendPercentage"),
        ("DATA-DOMAIN-MIB", "nfsReceivePercentage"),
        ("DATA-DOMAIN-MIB", "cifsOpsPerSecond"),
        ("DATA-DOMAIN-MIB", "diskReadKBytesPerSecond"),
        ("DATA-DOMAIN-MIB", "diskWriteKBytesPerSecond"),
        ("DATA-DOMAIN-MIB", "diskBusyPercentage"),
        ("DATA-DOMAIN-MIB", "nvramReadKBytesPerSecond"),
        ("DATA-DOMAIN-MIB", "nvramWriteKBytesPerSecond"),
        ("DATA-DOMAIN-MIB", "replInKBytesPerSecond"),
        ("DATA-DOMAIN-MIB", "replOutKBytesPerSecond"))
)
if mibBuilder.loadTexts:
    statisticsGroup.setStatus("current")

internalDiskStorageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19746, 0, 2, 7)
)
internalDiskStorageGroup.setObjects(
      *(("DATA-DOMAIN-MIB", "diskModel"),
        ("DATA-DOMAIN-MIB", "diskFirmwareVersion"),
        ("DATA-DOMAIN-MIB", "diskSerialNumber"),
        ("DATA-DOMAIN-MIB", "diskCapacity"),
        ("DATA-DOMAIN-MIB", "diskPropState"),
        ("DATA-DOMAIN-MIB", "diskPack"),
        ("DATA-DOMAIN-MIB", "diskSectorsRead"),
        ("DATA-DOMAIN-MIB", "diskSectorsWritten"),
        ("DATA-DOMAIN-MIB", "diskTotalKBytes"),
        ("DATA-DOMAIN-MIB", "diskBusy"),
        ("DATA-DOMAIN-MIB", "diskPerfState"),
        ("DATA-DOMAIN-MIB", "diskTemperature"),
        ("DATA-DOMAIN-MIB", "diskTimeoutCount"),
        ("DATA-DOMAIN-MIB", "diskReadFailCount"),
        ("DATA-DOMAIN-MIB", "diskWriteFailCount"),
        ("DATA-DOMAIN-MIB", "diskMiscFailCount"),
        ("DATA-DOMAIN-MIB", "diskOffTrackErrCount"),
        ("DATA-DOMAIN-MIB", "diskSoftEccCount"),
        ("DATA-DOMAIN-MIB", "diskCrcErrCount"),
        ("DATA-DOMAIN-MIB", "diskProbationalCount"),
        ("DATA-DOMAIN-MIB", "diskReallocCount"),
        ("DATA-DOMAIN-MIB", "diskErrState"))
)
if mibBuilder.loadTexts:
    internalDiskStorageGroup.setStatus("current")

externalUnmanagedDiskStorageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19746, 0, 2, 8)
)
externalUnmanagedDiskStorageGroup.setObjects(
      *(("DATA-DOMAIN-MIB", "diskModel"),
        ("DATA-DOMAIN-MIB", "diskFirmwareVersion"),
        ("DATA-DOMAIN-MIB", "diskSerialNumber"),
        ("DATA-DOMAIN-MIB", "diskCapacity"),
        ("DATA-DOMAIN-MIB", "diskPropState"),
        ("DATA-DOMAIN-MIB", "diskSectorsRead"),
        ("DATA-DOMAIN-MIB", "diskSectorsWritten"),
        ("DATA-DOMAIN-MIB", "diskTotalKBytes"),
        ("DATA-DOMAIN-MIB", "diskBusy"),
        ("DATA-DOMAIN-MIB", "diskPerfState"),
        ("DATA-DOMAIN-MIB", "diskPropTrapIndex"),
        ("DATA-DOMAIN-MIB", "diskErrTrapIndex"))
)
if mibBuilder.loadTexts:
    externalUnmanagedDiskStorageGroup.setStatus("current")

replGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19746, 0, 2, 11)
)
replGroup.setObjects(
      *(("DATA-DOMAIN-MIB", "replState"),
        ("DATA-DOMAIN-MIB", "replStatus"),
        ("DATA-DOMAIN-MIB", "replFileSysStatus"),
        ("DATA-DOMAIN-MIB", "replConnTime"),
        ("DATA-DOMAIN-MIB", "replSource"),
        ("DATA-DOMAIN-MIB", "replDestination"),
        ("DATA-DOMAIN-MIB", "replPreCompBytesSent"),
        ("DATA-DOMAIN-MIB", "replPostCompBytesSent"),
        ("DATA-DOMAIN-MIB", "replPreCompBytesRemaining"),
        ("DATA-DOMAIN-MIB", "replPostCompBytesReceived"),
        ("DATA-DOMAIN-MIB", "replThrottle"),
        ("DATA-DOMAIN-MIB", "replSyncedAsOfTime"),
        ("DATA-DOMAIN-MIB", "replConfigContextId"),
        ("DATA-DOMAIN-MIB", "replConfigSource"),
        ("DATA-DOMAIN-MIB", "replConfigDest"),
        ("DATA-DOMAIN-MIB", "replConfigConnHost"),
        ("DATA-DOMAIN-MIB", "replConfigConnPort"),
        ("DATA-DOMAIN-MIB", "replConfigLowBWOptim"),
        ("DATA-DOMAIN-MIB", "replConfigEnabled"),
        ("DATA-DOMAIN-MIB", "replConfigTenantUnit"),
        ("DATA-DOMAIN-MIB", "replHistoryDate"),
        ("DATA-DOMAIN-MIB", "replHistoryTime"),
        ("DATA-DOMAIN-MIB", "replHistoryPreCompWritten"),
        ("DATA-DOMAIN-MIB", "replHistoryPreCompRemaining"),
        ("DATA-DOMAIN-MIB", "replHistoryPreCompressed"),
        ("DATA-DOMAIN-MIB", "replHistoryPostFiltered"),
        ("DATA-DOMAIN-MIB", "replHistoryPostLowBwOptim"),
        ("DATA-DOMAIN-MIB", "replHistoryPostLocalComp"),
        ("DATA-DOMAIN-MIB", "replHistoryBytesNetwork"),
        ("DATA-DOMAIN-MIB", "replHistorySyncedAsOfTime"),
        ("DATA-DOMAIN-MIB", "replTrapContext"),
        ("DATA-DOMAIN-MIB", "replPerformancePreCompKBPerSec"),
        ("DATA-DOMAIN-MIB", "replPerformanceNetworkKBPerSec"),
        ("DATA-DOMAIN-MIB", "replPerformanceStreams"),
        ("DATA-DOMAIN-MIB", "replPerformanceBusyReading"),
        ("DATA-DOMAIN-MIB", "replPerformanceBusyMeta"),
        ("DATA-DOMAIN-MIB", "replPerformanceWaitingDest"),
        ("DATA-DOMAIN-MIB", "replPerformanceWaitingNetwork"))
)
if mibBuilder.loadTexts:
    replGroup.setStatus("current")

nfsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19746, 0, 2, 12)
)
nfsGroup.setObjects(
      *(("DATA-DOMAIN-MIB", "nfsStatus"),
        ("DATA-DOMAIN-MIB", "nfsClientPath"),
        ("DATA-DOMAIN-MIB", "nfsClientClients"),
        ("DATA-DOMAIN-MIB", "nfsClientOptions"),
        ("DATA-DOMAIN-MIB", "nfsStatsExportPoint"),
        ("DATA-DOMAIN-MIB", "nfsStatsFilesystemType"),
        ("DATA-DOMAIN-MIB", "nfsStatsCacheEntry"),
        ("DATA-DOMAIN-MIB", "nfsStatsFileHandleLookup"),
        ("DATA-DOMAIN-MIB", "nfsStatsMaxCacheSize"),
        ("DATA-DOMAIN-MIB", "nfsStatsCurrentOpenStreams"),
        ("DATA-DOMAIN-MIB", "nfsActivePath"),
        ("DATA-DOMAIN-MIB", "nfsActiveClients"),
        ("DATA-DOMAIN-MIB", "nfsPortService"),
        ("DATA-DOMAIN-MIB", "nfsPortPort"))
)
if mibBuilder.loadTexts:
    nfsGroup.setStatus("current")

cifsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19746, 0, 2, 13)
)
cifsGroup.setObjects(
      *(("DATA-DOMAIN-MIB", "cifsStatus"),
        ("DATA-DOMAIN-MIB", "cifsConfigMode"),
        ("DATA-DOMAIN-MIB", "cifsConfigWINSServer"),
        ("DATA-DOMAIN-MIB", "cifsConfigNetBIOSHostname"),
        ("DATA-DOMAIN-MIB", "cifsConfigDomainController"),
        ("DATA-DOMAIN-MIB", "cifsConfigDNS"),
        ("DATA-DOMAIN-MIB", "cifsConfigGroupName"),
        ("DATA-DOMAIN-MIB", "cifsConfigMaxConnection"),
        ("DATA-DOMAIN-MIB", "cifsConfigMaxOpenFilesPerConnection"),
        ("DATA-DOMAIN-MIB", "cifsShareName"),
        ("DATA-DOMAIN-MIB", "cifsSharePath"),
        ("DATA-DOMAIN-MIB", "cifsShareClients"),
        ("DATA-DOMAIN-MIB", "cifsShareUser"),
        ("DATA-DOMAIN-MIB", "cifsShareComment"),
        ("DATA-DOMAIN-MIB", "cifsShareBrowsing"),
        ("DATA-DOMAIN-MIB", "cifsShareWriteable"),
        ("DATA-DOMAIN-MIB", "cifsShareMaxConnection"),
        ("DATA-DOMAIN-MIB", "cifsOptionsName"),
        ("DATA-DOMAIN-MIB", "cifsOptionsValue"))
)
if mibBuilder.loadTexts:
    cifsGroup.setStatus("deprecated")

vtlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19746, 0, 2, 14)
)
vtlGroup.setObjects(
      *(("DATA-DOMAIN-MIB", "vtlAdminState"),
        ("DATA-DOMAIN-MIB", "vtlProcessState"),
        ("DATA-DOMAIN-MIB", "vtlLibraryName"),
        ("DATA-DOMAIN-MIB", "vtlLibraryVendor"),
        ("DATA-DOMAIN-MIB", "vtlLibraryModel"),
        ("DATA-DOMAIN-MIB", "vtlLibraryRevision"),
        ("DATA-DOMAIN-MIB", "vtlLibrarySerial"),
        ("DATA-DOMAIN-MIB", "vtlLibraryTotalDrives"),
        ("DATA-DOMAIN-MIB", "vtlLibraryTotalSlots"),
        ("DATA-DOMAIN-MIB", "vtlLibraryTotalCaps"),
        ("DATA-DOMAIN-MIB", "vtlLibraryStatus"),
        ("DATA-DOMAIN-MIB", "vtlDriveName"),
        ("DATA-DOMAIN-MIB", "vtlDriveVendor"),
        ("DATA-DOMAIN-MIB", "vtlDriveModel"),
        ("DATA-DOMAIN-MIB", "vtlDriveRevision"),
        ("DATA-DOMAIN-MIB", "vtlDriveSerial"),
        ("DATA-DOMAIN-MIB", "vtlDriveLibraryName"),
        ("DATA-DOMAIN-MIB", "vtlDriveStatus"),
        ("DATA-DOMAIN-MIB", "vtlDriveTapeVolume"),
        ("DATA-DOMAIN-MIB", "vtlGroupName"),
        ("DATA-DOMAIN-MIB", "vtlGroupInitiaterCount"),
        ("DATA-DOMAIN-MIB", "vtlGroupDeviceCount"),
        ("DATA-DOMAIN-MIB", "vtlGroupDeviceGroupName"),
        ("DATA-DOMAIN-MIB", "vtlGroupDeviceDeviceName"),
        ("DATA-DOMAIN-MIB", "vtlGroupDeviceLun"),
        ("DATA-DOMAIN-MIB", "vtlGroupDevicePrimaryPorts"),
        ("DATA-DOMAIN-MIB", "vtlGroupDeviceSecondaryPorts"),
        ("DATA-DOMAIN-MIB", "vtlGroupDeviceInUsePorts"),
        ("DATA-DOMAIN-MIB", "vtlInitiatorName"),
        ("DATA-DOMAIN-MIB", "vtlInitiatorStatus"),
        ("DATA-DOMAIN-MIB", "vtlInitiatorGroup"),
        ("DATA-DOMAIN-MIB", "vtlInitiatorWWNN"),
        ("DATA-DOMAIN-MIB", "vtlInitiatorWWPN"),
        ("DATA-DOMAIN-MIB", "vtlInitiatorPort"),
        ("DATA-DOMAIN-MIB", "vtlPoolPool"),
        ("DATA-DOMAIN-MIB", "vtlPoolStatus"),
        ("DATA-DOMAIN-MIB", "vtlPoolTapes"),
        ("DATA-DOMAIN-MIB", "vtlPoolSize"),
        ("DATA-DOMAIN-MIB", "vtlPoolUsed"),
        ("DATA-DOMAIN-MIB", "vtlPoolComp"),
        ("DATA-DOMAIN-MIB", "vtlPortName"),
        ("DATA-DOMAIN-MIB", "vtlPortID"),
        ("DATA-DOMAIN-MIB", "vtlPortModel"),
        ("DATA-DOMAIN-MIB", "vtlPortFirmware"),
        ("DATA-DOMAIN-MIB", "vtlPortWWNN"),
        ("DATA-DOMAIN-MIB", "vtlPortWWPN"),
        ("DATA-DOMAIN-MIB", "vtlPortConnectionType"),
        ("DATA-DOMAIN-MIB", "vtlPortSpeed"),
        ("DATA-DOMAIN-MIB", "vtlPortEnabled"),
        ("DATA-DOMAIN-MIB", "vtlPortStatus"),
        ("DATA-DOMAIN-MIB", "vtlPortTrapIndex"),
        ("DATA-DOMAIN-MIB", "vtlStatsPort"),
        ("DATA-DOMAIN-MIB", "vtlStatsConrolCommands"),
        ("DATA-DOMAIN-MIB", "vtlStatsWriteCommands"),
        ("DATA-DOMAIN-MIB", "vtlStatsReadCommands"),
        ("DATA-DOMAIN-MIB", "vtlStatsIn"),
        ("DATA-DOMAIN-MIB", "vtlStatsOut"),
        ("DATA-DOMAIN-MIB", "vtlStatsLinkFailures"),
        ("DATA-DOMAIN-MIB", "vtlStatsLIPCount"),
        ("DATA-DOMAIN-MIB", "vtlStatsSyncLosses"),
        ("DATA-DOMAIN-MIB", "vtlStatsSignalLosses"),
        ("DATA-DOMAIN-MIB", "vtlStatsPrimSeqProtoErrors"),
        ("DATA-DOMAIN-MIB", "vtlStatsInvalidTxWords"),
        ("DATA-DOMAIN-MIB", "vtlStatsInvalidCRCs"),
        ("DATA-DOMAIN-MIB", "vtlTapeBarCode"),
        ("DATA-DOMAIN-MIB", "vtlTapePool"),
        ("DATA-DOMAIN-MIB", "vtlTapeLocation"),
        ("DATA-DOMAIN-MIB", "vtlTapeState"),
        ("DATA-DOMAIN-MIB", "vtlTapeSize"),
        ("DATA-DOMAIN-MIB", "vtlTapeUsed"),
        ("DATA-DOMAIN-MIB", "vtlTapeComp"),
        ("DATA-DOMAIN-MIB", "vtlTapeModTime"))
)
if mibBuilder.loadTexts:
    vtlGroup.setStatus("current")

ddboostGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19746, 0, 2, 15)
)
ddboostGroup.setObjects(
      *(("DATA-DOMAIN-MIB", "ddboostAccessClientsName"),
        ("DATA-DOMAIN-MIB", "ddboostAccessClientsEncryStrength"),
        ("DATA-DOMAIN-MIB", "ddboostAccessClientsAuthMode"),
        ("DATA-DOMAIN-MIB", "ddboostInterface"),
        ("DATA-DOMAIN-MIB", "ddboostifGroupMember"),
        ("DATA-DOMAIN-MIB", "ddboostBackupConnections"),
        ("DATA-DOMAIN-MIB", "ddboostRestoreConnections"),
        ("DATA-DOMAIN-MIB", "ddboostControlConnections"),
        ("DATA-DOMAIN-MIB", "ddboostTotalConnections"),
        ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryDirection"),
        ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryNetwork"),
        ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryPreComp"),
        ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryPostComp"),
        ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryLowBWOpt"),
        ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryErrors"),
        ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryDate"),
        ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryTime"),
        ("DATA-DOMAIN-MIB", "ddboostFileReplStatsDirection"),
        ("DATA-DOMAIN-MIB", "ddboostFileReplStatsNetworkSent"),
        ("DATA-DOMAIN-MIB", "ddboostFileReplStatsPreCompSent"),
        ("DATA-DOMAIN-MIB", "ddboostFileReplStatsFiltered"),
        ("DATA-DOMAIN-MIB", "ddboostFileReplStatsLowBWOpt"),
        ("DATA-DOMAIN-MIB", "ddboostFileReplStatsLocalComp"),
        ("DATA-DOMAIN-MIB", "ddboostFileReplStatsCompRatio"),
        ("DATA-DOMAIN-MIB", "ddboostIfGroupInterface"),
        ("DATA-DOMAIN-MIB", "ddboostOptionsName"),
        ("DATA-DOMAIN-MIB", "ddboostOptionsStatus"),
        ("DATA-DOMAIN-MIB", "ddboostStatus"),
        ("DATA-DOMAIN-MIB", "ddboostUser"),
        ("DATA-DOMAIN-MIB", "ddboostIfGroupStatus"),
        ("DATA-DOMAIN-MIB", "ddboostPreCompKBytesPerSecond"),
        ("DATA-DOMAIN-MIB", "ddboostPostCompKBytesPerSecond"),
        ("DATA-DOMAIN-MIB", "ddboostNetworkKBytesPerSecond"),
        ("DATA-DOMAIN-MIB", "ddboostReadKBytesPerSecond"),
        ("DATA-DOMAIN-MIB", "ddboostStatsBackupConn"),
        ("DATA-DOMAIN-MIB", "ddboostStatsRestoreConn"),
        ("DATA-DOMAIN-MIB", "ddboostStatsImageCreatesCount"),
        ("DATA-DOMAIN-MIB", "ddboostStatsImageCreatesErrors"),
        ("DATA-DOMAIN-MIB", "ddboostStatsImageDeletesCount"),
        ("DATA-DOMAIN-MIB", "ddboostStatsImageDeletesErrors"),
        ("DATA-DOMAIN-MIB", "ddboostStatsPrecompBytesReceived"),
        ("DATA-DOMAIN-MIB", "ddboostStatsBytesAfterFiltering"),
        ("DATA-DOMAIN-MIB", "ddboostStatsBytesAfterLc"),
        ("DATA-DOMAIN-MIB", "ddboostStatsNetworkBytesReceived"),
        ("DATA-DOMAIN-MIB", "ddboostStatsCompressionRatio"),
        ("DATA-DOMAIN-MIB", "ddboostStatsTotalBytesReadCount"),
        ("DATA-DOMAIN-MIB", "ddboostStatsTotalBytesReadErrors"),
        ("DATA-DOMAIN-MIB", "ddboostStorageUnitName"),
        ("DATA-DOMAIN-MIB", "ddboostStorageUnitBytes"),
        ("DATA-DOMAIN-MIB", "ddboostStorageUnitGlobalComp"),
        ("DATA-DOMAIN-MIB", "ddboostStorageUnitLocalComp"),
        ("DATA-DOMAIN-MIB", "ddboostStorageUnitMetaData"),
        ("DATA-DOMAIN-MIB", "ddboostFileRepliPerfInPreCompKBPerSec"),
        ("DATA-DOMAIN-MIB", "ddboostFileRepliPerfInNetworkKBPerSec"),
        ("DATA-DOMAIN-MIB", "ddboostFileRepliPerfOutPreCompKBPerSec"),
        ("DATA-DOMAIN-MIB", "ddboostFileRepliPerfOutNetworkKBPerSec"))
)
if mibBuilder.loadTexts:
    ddboostGroup.setStatus("deprecated")

ddsystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19746, 0, 2, 16)
)
ddsystemGroup.setObjects(
      *(("DATA-DOMAIN-MIB", "systemLicenseKey"),
        ("DATA-DOMAIN-MIB", "systemLicenseFeature"),
        ("DATA-DOMAIN-MIB", "systemCapacityLicenseKey"),
        ("DATA-DOMAIN-MIB", "systemCapacityLicenseFeature"),
        ("DATA-DOMAIN-MIB", "systemCapacityLicenseModel"),
        ("DATA-DOMAIN-MIB", "systemCapacityLicenseCapacity"),
        ("DATA-DOMAIN-MIB", "systemHardwareSlot"),
        ("DATA-DOMAIN-MIB", "systemHardwareVendor"),
        ("DATA-DOMAIN-MIB", "systemHardwareDevice"),
        ("DATA-DOMAIN-MIB", "systemHardwarePorts"),
        ("DATA-DOMAIN-MIB", "systemPortsPort"),
        ("DATA-DOMAIN-MIB", "systemPortsConnectionType"),
        ("DATA-DOMAIN-MIB", "systemPortsLinkSpeed"),
        ("DATA-DOMAIN-MIB", "systemPortsFirmware"),
        ("DATA-DOMAIN-MIB", "systemPortsHardwareAddress"),
        ("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "systemCurrentTime"),
        ("DATA-DOMAIN-MIB", "systemVersion"),
        ("DATA-DOMAIN-MIB", "systemModelNumber"),
        ("DATA-DOMAIN-MIB", "sysNotes"),
        ("DATA-DOMAIN-MIB", "systemTimeZoneName"),
        ("DATA-DOMAIN-MIB", "systemUserName"),
        ("DATA-DOMAIN-MIB", "systemUserUID"),
        ("DATA-DOMAIN-MIB", "systemUserRole"),
        ("DATA-DOMAIN-MIB", "systemUserStatus"))
)
if mibBuilder.loadTexts:
    ddsystemGroup.setStatus("deprecated")

artGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19746, 0, 2, 17)
)
artGroup.setObjects(
      *(("DATA-DOMAIN-MIB", "artConfigStatus"),
        ("DATA-DOMAIN-MIB", "artConfigMigrationSchedule"),
        ("DATA-DOMAIN-MIB", "artConfigDefaultAge"),
        ("DATA-DOMAIN-MIB", "artConfigFileSystemClean"),
        ("DATA-DOMAIN-MIB", "artConfigCompression"),
        ("DATA-DOMAIN-MIB", "artMigrationPolicyMtreeName"),
        ("DATA-DOMAIN-MIB", "artMigrationPolicyDefaultAge"),
        ("DATA-DOMAIN-MIB", "artMigrationScheduleSchedule"),
        ("DATA-DOMAIN-MIB", "artMigrationScheduleStatus"))
)
if mibBuilder.loadTexts:
    artGroup.setStatus("current")

mtreeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19746, 0, 2, 18)
)
mtreeGroup.setObjects(
      *(("DATA-DOMAIN-MIB", "mtreeCompressionMtreePath"),
        ("DATA-DOMAIN-MIB", "mtreeCompressionPreCompGib"),
        ("DATA-DOMAIN-MIB", "mtreeCompressionPostCompGib"),
        ("DATA-DOMAIN-MIB", "mtreeCompressionGlobalCompFactor"),
        ("DATA-DOMAIN-MIB", "mtreeCompressionLocalCompFactor"),
        ("DATA-DOMAIN-MIB", "mtreeCompressionPostTotalCompFactor"),
        ("DATA-DOMAIN-MIB", "mtreeCompressionTimePeriod"),
        ("DATA-DOMAIN-MIB", "mtreeListMtreeName"),
        ("DATA-DOMAIN-MIB", "mtreeListPreCompGib"),
        ("DATA-DOMAIN-MIB", "mtreeListStatus"),
        ("DATA-DOMAIN-MIB", "mtreeRetentionLockMtreeName"),
        ("DATA-DOMAIN-MIB", "mtreeRetentionLockStatus"),
        ("DATA-DOMAIN-MIB", "mtreeRetentionLockUUID"),
        ("DATA-DOMAIN-MIB", "mtreeRetentionLockMinRetentionPeriod"),
        ("DATA-DOMAIN-MIB", "mtreeRetentionLockMaxRetentionPeriod"))
)
if mibBuilder.loadTexts:
    mtreeGroup.setStatus("current")

enclosureGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19746, 0, 2, 19)
)
enclosureGroup.setObjects(
      *(("DATA-DOMAIN-MIB", "enclosureListNum"),
        ("DATA-DOMAIN-MIB", "enclosureListModel"),
        ("DATA-DOMAIN-MIB", "enclosureListSerialNum"),
        ("DATA-DOMAIN-MIB", "enclosureListOemName"),
        ("DATA-DOMAIN-MIB", "enclosureListOemValue"),
        ("DATA-DOMAIN-MIB", "enclosureListCapacity"),
        ("DATA-DOMAIN-MIB", "enclosurePackID"))
)
if mibBuilder.loadTexts:
    enclosureGroup.setStatus("current")

managedObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19746, 0, 2, 20)
)
managedObjectsGroup.setObjects(
      *(("DATA-DOMAIN-MIB", "managedSystemHostname"),
        ("DATA-DOMAIN-MIB", "managedSystemSerial"),
        ("DATA-DOMAIN-MIB", "managedSystemState"),
        ("DATA-DOMAIN-MIB", "managedSystemStatus"),
        ("DATA-DOMAIN-MIB", "managedSystemDDOSVersion"),
        ("DATA-DOMAIN-MIB", "managedSystemHDSyncTime"),
        ("DATA-DOMAIN-MIB", "managedSystemCDSyncTime"),
        ("DATA-DOMAIN-MIB", "taskHistoryUser"),
        ("DATA-DOMAIN-MIB", "taskHistoryID"),
        ("DATA-DOMAIN-MIB", "taskHistoryParent"),
        ("DATA-DOMAIN-MIB", "taskHistoryName"),
        ("DATA-DOMAIN-MIB", "taskHistoryState"),
        ("DATA-DOMAIN-MIB", "taskHistoryStartTime"),
        ("DATA-DOMAIN-MIB", "taskHistoryDuration"),
        ("DATA-DOMAIN-MIB", "taskActiveUser"),
        ("DATA-DOMAIN-MIB", "taskActiveID"),
        ("DATA-DOMAIN-MIB", "taskActiveParent"),
        ("DATA-DOMAIN-MIB", "taskActiveName"),
        ("DATA-DOMAIN-MIB", "taskActiveState"),
        ("DATA-DOMAIN-MIB", "taskActiveStartTime"),
        ("DATA-DOMAIN-MIB", "taskActiveDuration"))
)
if mibBuilder.loadTexts:
    managedObjectsGroup.setStatus("current")

networkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19746, 0, 2, 21)
)
networkGroup.setObjects(
      *(("DATA-DOMAIN-MIB", "dnsServer"),
        ("DATA-DOMAIN-MIB", "searchDomainsName"),
        ("DATA-DOMAIN-MIB", "snmpTrapHostsName"),
        ("DATA-DOMAIN-MIB", "snmpTrapHostsVersion"),
        ("DATA-DOMAIN-MIB", "nisDomain"),
        ("DATA-DOMAIN-MIB", "nisServers"),
        ("DATA-DOMAIN-MIB", "nisAdminGroups"),
        ("DATA-DOMAIN-MIB", "nisUserGroups"),
        ("DATA-DOMAIN-MIB", "nisBackupOperatorGroups"),
        ("DATA-DOMAIN-MIB", "nisEnabled"),
        ("DATA-DOMAIN-MIB", "nisStatus"))
)
if mibBuilder.loadTexts:
    networkGroup.setStatus("current")

fileSystemGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19746, 0, 2, 22)
)
fileSystemGroupRev1.setObjects(
      *(("DATA-DOMAIN-MIB", "fileSystemStatus"),
        ("DATA-DOMAIN-MIB", "fileSystemVirtualSpace"),
        ("DATA-DOMAIN-MIB", "fileSystemResourceName"),
        ("DATA-DOMAIN-MIB", "fileSystemSpaceSize"),
        ("DATA-DOMAIN-MIB", "fileSystemSpaceUsed"),
        ("DATA-DOMAIN-MIB", "fileSystemSpaceAvail"),
        ("DATA-DOMAIN-MIB", "fileSystemPercentUsed"),
        ("DATA-DOMAIN-MIB", "fileSystemSpaceCleanable"),
        ("DATA-DOMAIN-MIB", "fileSystemResourceTier"),
        ("DATA-DOMAIN-MIB", "fileSystemCompressionPeriod"),
        ("DATA-DOMAIN-MIB", "fileSystemCompressionStartTime"),
        ("DATA-DOMAIN-MIB", "fileSystemCompressionEndTime"),
        ("DATA-DOMAIN-MIB", "fileSystemPreCompressionSize"),
        ("DATA-DOMAIN-MIB", "fileSystemPostCompressionSize"),
        ("DATA-DOMAIN-MIB", "fileSystemGlobalCompressionFactor"),
        ("DATA-DOMAIN-MIB", "fileSystemLocalCompressionFactor"),
        ("DATA-DOMAIN-MIB", "fileSystemTotalCompressionFactor"),
        ("DATA-DOMAIN-MIB", "fileSystemArchiveUnitName"),
        ("DATA-DOMAIN-MIB", "fileSystemArchiveUnitState"),
        ("DATA-DOMAIN-MIB", "fileSystemArchiveUnitStatus"),
        ("DATA-DOMAIN-MIB", "fileSystemArchiveUnitStartTime"),
        ("DATA-DOMAIN-MIB", "fileSystemArchiveUnitEndTime"),
        ("DATA-DOMAIN-MIB", "fileSystemArchiveUnitSize"),
        ("DATA-DOMAIN-MIB", "fileSystemArchiveUnitDiskGroups"),
        ("DATA-DOMAIN-MIB", "fileSystemCleanStatus"),
        ("DATA-DOMAIN-MIB", "fileSystemCleanSchedule"),
        ("DATA-DOMAIN-MIB", "fileSystemCleanThrottle"),
        ("DATA-DOMAIN-MIB", "fileSystemReductionPercent1"),
        ("DATA-DOMAIN-MIB", "fileSystemOptionsName"),
        ("DATA-DOMAIN-MIB", "fileSystemOptionsValue"),
        ("DATA-DOMAIN-MIB", "fileSystemUpTime"),
        ("DATA-DOMAIN-MIB", "fileSystemStatusMessage"),
        ("DATA-DOMAIN-MIB", "fileSystemResourceTrapIndex"))
)
if mibBuilder.loadTexts:
    fileSystemGroupRev1.setStatus("current")

ddsystemGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19746, 0, 2, 23)
)
ddsystemGroupRev1.setObjects(
      *(("DATA-DOMAIN-MIB", "systemLicenseKey"),
        ("DATA-DOMAIN-MIB", "systemLicenseFeature"),
        ("DATA-DOMAIN-MIB", "systemCapacityLicenseKey"),
        ("DATA-DOMAIN-MIB", "systemCapacityLicenseFeature"),
        ("DATA-DOMAIN-MIB", "systemCapacityLicenseModel"),
        ("DATA-DOMAIN-MIB", "systemCapacityLicenseCapacity"),
        ("DATA-DOMAIN-MIB", "systemHardwareVendor"),
        ("DATA-DOMAIN-MIB", "systemHardwareDevice"),
        ("DATA-DOMAIN-MIB", "systemHardwarePorts"),
        ("DATA-DOMAIN-MIB", "systemHardwareSlotName"),
        ("DATA-DOMAIN-MIB", "systemPortsPort"),
        ("DATA-DOMAIN-MIB", "systemPortsConnectionType"),
        ("DATA-DOMAIN-MIB", "systemPortsLinkSpeed"),
        ("DATA-DOMAIN-MIB", "systemPortsFirmware"),
        ("DATA-DOMAIN-MIB", "systemPortsHardwareAddress"),
        ("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "systemCurrentTime"),
        ("DATA-DOMAIN-MIB", "systemVersion"),
        ("DATA-DOMAIN-MIB", "systemModelNumber"),
        ("DATA-DOMAIN-MIB", "systemTimeZoneName"),
        ("DATA-DOMAIN-MIB", "systemUserName"),
        ("DATA-DOMAIN-MIB", "systemUserUID"),
        ("DATA-DOMAIN-MIB", "systemUserRole"),
        ("DATA-DOMAIN-MIB", "systemUserStatus"),
        ("DATA-DOMAIN-MIB", "systemActiveUserName"),
        ("DATA-DOMAIN-MIB", "systemActiveUserIdleTime"),
        ("DATA-DOMAIN-MIB", "systemActiveUserLoginTime"),
        ("DATA-DOMAIN-MIB", "systemActiveUserLoginFrom"),
        ("DATA-DOMAIN-MIB", "systemActiveUserTty"))
)
if mibBuilder.loadTexts:
    ddsystemGroupRev1.setStatus("current")

smtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19746, 0, 2, 24)
)
smtGroup.setObjects(
      *(("DATA-DOMAIN-MIB", "smtStatus"),
        ("DATA-DOMAIN-MIB", "tenantUnitListName"),
        ("DATA-DOMAIN-MIB", "tenantUnitListNumberOfMgmtUsers"),
        ("DATA-DOMAIN-MIB", "tenantUnitListNumberOfMtrees"),
        ("DATA-DOMAIN-MIB", "tenantUnitListNumberOfDdboostStus"),
        ("DATA-DOMAIN-MIB", "tenantUnitListTenantSelfServiceMode"),
        ("DATA-DOMAIN-MIB", "tenantUnitListParentTenantName"),
        ("DATA-DOMAIN-MIB", "tenantUnitListType"),
        ("DATA-DOMAIN-MIB", "tenantUnitListSecurityMode"),
        ("DATA-DOMAIN-MIB", "tenantUnitListNumberOfMgmtGroups"),
        ("DATA-DOMAIN-MIB", "tenantUnitMgmtUserListUserRole"),
        ("DATA-DOMAIN-MIB", "tenantUnitMtreeListMtreeName"),
        ("DATA-DOMAIN-MIB", "tenantUnitDdboostStuListStuName"),
        ("DATA-DOMAIN-MIB", "tenantUnitAdminIpInfoType"),
        ("DATA-DOMAIN-MIB", "tenantInfoTenantName"),
        ("DATA-DOMAIN-MIB", "tenantInfoTenantUnitName"),
        ("DATA-DOMAIN-MIB", "tenantUnitMgmtGroupListGroupRole"),
        ("DATA-DOMAIN-MIB", "tenantUnitMgmtGroupListGroupType"))
)
if mibBuilder.loadTexts:
    smtGroup.setStatus("current")

quotaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19746, 0, 2, 25)
)
quotaGroup.setObjects(
      *(("DATA-DOMAIN-MIB", "quotaCapacityStatus"),
        ("DATA-DOMAIN-MIB", "quotaCapacityMtreeName"),
        ("DATA-DOMAIN-MIB", "quotaCapacityPreCompMiB"),
        ("DATA-DOMAIN-MIB", "quotaCapacitySoftLimitMiB"),
        ("DATA-DOMAIN-MIB", "quotaCapacityHardLimitMiB"),
        ("DATA-DOMAIN-MIB", "quotaCapacityTenantUnit"))
)
if mibBuilder.loadTexts:
    quotaGroup.setStatus("current")

ddboostGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19746, 0, 2, 26)
)
ddboostGroupRev1.setObjects(
      *(("DATA-DOMAIN-MIB", "ddboostAccessClientsName"),
        ("DATA-DOMAIN-MIB", "ddboostInterface"),
        ("DATA-DOMAIN-MIB", "ddboostifGroupMember"),
        ("DATA-DOMAIN-MIB", "ddboostBackupConnections"),
        ("DATA-DOMAIN-MIB", "ddboostRestoreConnections"),
        ("DATA-DOMAIN-MIB", "ddboostControlConnections"),
        ("DATA-DOMAIN-MIB", "ddboostTotalConnections"),
        ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryDirection"),
        ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryNetwork"),
        ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryPreComp"),
        ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryPostComp"),
        ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryLowBWOpt"),
        ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryErrors"),
        ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryDate"),
        ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryTime"),
        ("DATA-DOMAIN-MIB", "ddboostFileReplStatsDirection"),
        ("DATA-DOMAIN-MIB", "ddboostFileReplStatsNetworkSent"),
        ("DATA-DOMAIN-MIB", "ddboostFileReplStatsPreCompSent"),
        ("DATA-DOMAIN-MIB", "ddboostFileReplStatsFiltered"),
        ("DATA-DOMAIN-MIB", "ddboostFileReplStatsLowBWOpt"),
        ("DATA-DOMAIN-MIB", "ddboostFileReplStatsLocalComp"),
        ("DATA-DOMAIN-MIB", "ddboostFileReplStatsCompRatio"),
        ("DATA-DOMAIN-MIB", "ddboostIfGroupInterface"),
        ("DATA-DOMAIN-MIB", "ddboostOptionsName"),
        ("DATA-DOMAIN-MIB", "ddboostOptionsStatus"),
        ("DATA-DOMAIN-MIB", "ddboostStatus"),
        ("DATA-DOMAIN-MIB", "ddboostUserName"),
        ("DATA-DOMAIN-MIB", "ddboostIfGroupStatus"),
        ("DATA-DOMAIN-MIB", "ddboostPreCompKBytesPerSecond"),
        ("DATA-DOMAIN-MIB", "ddboostPostCompKBytesPerSecond"),
        ("DATA-DOMAIN-MIB", "ddboostNetworkKBytesPerSecond"),
        ("DATA-DOMAIN-MIB", "ddboostReadKBytesPerSecond"),
        ("DATA-DOMAIN-MIB", "ddboostStatsBackupConn"),
        ("DATA-DOMAIN-MIB", "ddboostStatsRestoreConn"),
        ("DATA-DOMAIN-MIB", "ddboostStatsImageCreatesCount"),
        ("DATA-DOMAIN-MIB", "ddboostStatsImageCreatesErrors"),
        ("DATA-DOMAIN-MIB", "ddboostStatsImageDeletesCount"),
        ("DATA-DOMAIN-MIB", "ddboostStatsImageDeletesErrors"),
        ("DATA-DOMAIN-MIB", "ddboostStatsPrecompBytesReceived"),
        ("DATA-DOMAIN-MIB", "ddboostStatsBytesAfterFiltering"),
        ("DATA-DOMAIN-MIB", "ddboostStatsBytesAfterLc"),
        ("DATA-DOMAIN-MIB", "ddboostStatsNetworkBytesReceived"),
        ("DATA-DOMAIN-MIB", "ddboostStatsCompressionRatio"),
        ("DATA-DOMAIN-MIB", "ddboostStatsTotalBytesReadCount"),
        ("DATA-DOMAIN-MIB", "ddboostStatsTotalBytesReadErrors"),
        ("DATA-DOMAIN-MIB", "ddboostStorageUnitName"),
        ("DATA-DOMAIN-MIB", "ddboostStorageUnitBytes"),
        ("DATA-DOMAIN-MIB", "ddboostStorageUnitGlobalComp"),
        ("DATA-DOMAIN-MIB", "ddboostStorageUnitLocalComp"),
        ("DATA-DOMAIN-MIB", "ddboostStorageUnitMetaData"),
        ("DATA-DOMAIN-MIB", "ddboostFileRepliPerfInPreCompKBPerSec"),
        ("DATA-DOMAIN-MIB", "ddboostFileRepliPerfInNetworkKBPerSec"),
        ("DATA-DOMAIN-MIB", "ddboostFileRepliPerfOutPreCompKBPerSec"),
        ("DATA-DOMAIN-MIB", "ddboostFileRepliPerfOutNetworkKBPerSec"))
)
if mibBuilder.loadTexts:
    ddboostGroupRev1.setStatus("deprecated")

ddboostGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19746, 0, 2, 27)
)
ddboostGroupRev2.setObjects(
      *(("DATA-DOMAIN-MIB", "ddboostAccessClientsName"),
        ("DATA-DOMAIN-MIB", "ddboostInterface"),
        ("DATA-DOMAIN-MIB", "ddboostifGroupMember"),
        ("DATA-DOMAIN-MIB", "ddboostBackupConnections"),
        ("DATA-DOMAIN-MIB", "ddboostRestoreConnections"),
        ("DATA-DOMAIN-MIB", "ddboostControlConnections"),
        ("DATA-DOMAIN-MIB", "ddboostTotalConnections"),
        ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryDirection"),
        ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryNetwork"),
        ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryPreComp"),
        ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryPostComp"),
        ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryLowBWOpt"),
        ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryErrors"),
        ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryDate"),
        ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryTime"),
        ("DATA-DOMAIN-MIB", "ddboostFileReplStatsDirection"),
        ("DATA-DOMAIN-MIB", "ddboostFileReplStatsNetworkSent"),
        ("DATA-DOMAIN-MIB", "ddboostFileReplStatsPreCompSent"),
        ("DATA-DOMAIN-MIB", "ddboostFileReplStatsFiltered"),
        ("DATA-DOMAIN-MIB", "ddboostFileReplStatsLowBWOpt"),
        ("DATA-DOMAIN-MIB", "ddboostFileReplStatsLocalComp"),
        ("DATA-DOMAIN-MIB", "ddboostFileReplStatsCompRatio"),
        ("DATA-DOMAIN-MIB", "ddboostIfGroupInterface"),
        ("DATA-DOMAIN-MIB", "ddboostOptionsName"),
        ("DATA-DOMAIN-MIB", "ddboostOptionsStatus"),
        ("DATA-DOMAIN-MIB", "ddboostStatus"),
        ("DATA-DOMAIN-MIB", "ddboostUserName"),
        ("DATA-DOMAIN-MIB", "ddboostUserDefaultTenantUnit"),
        ("DATA-DOMAIN-MIB", "ddboostIfGroupName"),
        ("DATA-DOMAIN-MIB", "ddboostIfGroupCurrentStatus"),
        ("DATA-DOMAIN-MIB", "ddboostPreCompKBytesPerSecond"),
        ("DATA-DOMAIN-MIB", "ddboostPostCompKBytesPerSecond"),
        ("DATA-DOMAIN-MIB", "ddboostNetworkKBytesPerSecond"),
        ("DATA-DOMAIN-MIB", "ddboostReadKBytesPerSecond"),
        ("DATA-DOMAIN-MIB", "ddboostStatsBackupConn"),
        ("DATA-DOMAIN-MIB", "ddboostStatsRestoreConn"),
        ("DATA-DOMAIN-MIB", "ddboostStatsImageCreatesCount"),
        ("DATA-DOMAIN-MIB", "ddboostStatsImageCreatesErrors"),
        ("DATA-DOMAIN-MIB", "ddboostStatsImageDeletesCount"),
        ("DATA-DOMAIN-MIB", "ddboostStatsImageDeletesErrors"),
        ("DATA-DOMAIN-MIB", "ddboostStatsPrecompBytesReceived"),
        ("DATA-DOMAIN-MIB", "ddboostStatsBytesAfterFiltering"),
        ("DATA-DOMAIN-MIB", "ddboostStatsBytesAfterLc"),
        ("DATA-DOMAIN-MIB", "ddboostStatsNetworkBytesReceived"),
        ("DATA-DOMAIN-MIB", "ddboostStatsCompressionRatio"),
        ("DATA-DOMAIN-MIB", "ddboostStatsTotalBytesReadCount"),
        ("DATA-DOMAIN-MIB", "ddboostStatsTotalBytesReadErrors"),
        ("DATA-DOMAIN-MIB", "ddboostStorageUnitName"),
        ("DATA-DOMAIN-MIB", "ddboostStorageUnitBytes"),
        ("DATA-DOMAIN-MIB", "ddboostStorageUnitGlobalComp"),
        ("DATA-DOMAIN-MIB", "ddboostStorageUnitLocalComp"),
        ("DATA-DOMAIN-MIB", "ddboostStorageUnitMetaData"),
        ("DATA-DOMAIN-MIB", "ddboostStorageUnitStatus"),
        ("DATA-DOMAIN-MIB", "ddboostStorageUnitPreComp"),
        ("DATA-DOMAIN-MIB", "ddboostStorageUnitUser"),
        ("DATA-DOMAIN-MIB", "ddboostStorageUnitReportPhysicalSize"),
        ("DATA-DOMAIN-MIB", "ddboostFileRepliPerfInPreCompKBPerSec"),
        ("DATA-DOMAIN-MIB", "ddboostFileRepliPerfInNetworkKBPerSec"),
        ("DATA-DOMAIN-MIB", "ddboostFileRepliPerfOutPreCompKBPerSec"),
        ("DATA-DOMAIN-MIB", "ddboostFileRepliPerfOutNetworkKBPerSec"))
)
if mibBuilder.loadTexts:
    ddboostGroupRev2.setStatus("current")

highAvailabilityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19746, 0, 2, 28)
)
highAvailabilityGroup.setObjects(
      *(("DATA-DOMAIN-MIB", "haSystemStatus"),
        ("DATA-DOMAIN-MIB", "localNodeRole"),
        ("DATA-DOMAIN-MIB", "localHaState"),
        ("DATA-DOMAIN-MIB", "peerNodeRole"),
        ("DATA-DOMAIN-MIB", "peerHaState"),
        ("DATA-DOMAIN-MIB", "haConfiguredMode"),
        ("DATA-DOMAIN-MIB", "haLocalPnodeId"))
)
if mibBuilder.loadTexts:
    highAvailabilityGroup.setStatus("current")

scsitargetObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19746, 0, 2, 29)
)
scsitargetObjectGroup.setObjects(
      *(("DATA-DOMAIN-MIB", "scsitargetAdminState"),
        ("DATA-DOMAIN-MIB", "scsitargetProcessState"),
        ("DATA-DOMAIN-MIB", "scsitargetGroupName"),
        ("DATA-DOMAIN-MIB", "scsitargetGroupService"),
        ("DATA-DOMAIN-MIB", "scsitargetGroupActiveState"),
        ("DATA-DOMAIN-MIB", "scsitargetGroupNumInitiators"),
        ("DATA-DOMAIN-MIB", "scsitargetGroupNumDevices"),
        ("DATA-DOMAIN-MIB", "scsitargetInitiatorName"),
        ("DATA-DOMAIN-MIB", "scsitargetInitiatorSystemAddress"),
        ("DATA-DOMAIN-MIB", "scsitargetInitiatorGroup"),
        ("DATA-DOMAIN-MIB", "scsitargetInitiatorService"),
        ("DATA-DOMAIN-MIB", "scsitargetInitiatorAddressMethod"),
        ("DATA-DOMAIN-MIB", "scsitargetInitiatorTransport"),
        ("DATA-DOMAIN-MIB", "scsitargetInitiatorFcWwpn"),
        ("DATA-DOMAIN-MIB", "scsitargetInitiatorFcWwnn"),
        ("DATA-DOMAIN-MIB", "scsitargetInitiatorFcSymbolicPortName"),
        ("DATA-DOMAIN-MIB", "scsitargetInitiatorEndpInitiator"),
        ("DATA-DOMAIN-MIB", "scsitargetInitiatorEndpEndpoint"),
        ("DATA-DOMAIN-MIB", "scsitargetInitiatorEndpStatus"),
        ("DATA-DOMAIN-MIB", "scsitargetEndpointName"),
        ("DATA-DOMAIN-MIB", "scsitargetEndpointCurrentSystemAddress"),
        ("DATA-DOMAIN-MIB", "scsitargetEndpointPrimarySystemAddress"),
        ("DATA-DOMAIN-MIB", "scsitargetEndpointSecondarySystemAddress"),
        ("DATA-DOMAIN-MIB", "scsitargetEndpointEnabled"),
        ("DATA-DOMAIN-MIB", "scsitargetEndpointStatus"),
        ("DATA-DOMAIN-MIB", "scsitargetEndpointTransport"),
        ("DATA-DOMAIN-MIB", "scsitargetEndpointFcWwnn"),
        ("DATA-DOMAIN-MIB", "scsitargetEndpointFcWwpn"),
        ("DATA-DOMAIN-MIB", "scsitargetPortSystemAddress"),
        ("DATA-DOMAIN-MIB", "scsitargetPortEnabled"),
        ("DATA-DOMAIN-MIB", "scsitargetPortStatus"),
        ("DATA-DOMAIN-MIB", "scsitargetPortTransport"),
        ("DATA-DOMAIN-MIB", "scsitargetPortOperationalStatus"),
        ("DATA-DOMAIN-MIB", "scsitargetPortFcNpiv"),
        ("DATA-DOMAIN-MIB", "scsitargetPortPortId"),
        ("DATA-DOMAIN-MIB", "scsitargetPortModel"),
        ("DATA-DOMAIN-MIB", "scsitargetPortFirmware"),
        ("DATA-DOMAIN-MIB", "scsitargetPortFcBaseWwnn"),
        ("DATA-DOMAIN-MIB", "scsitargetPortFcBaseWwpn"),
        ("DATA-DOMAIN-MIB", "scsitargetPortFcCurrentWwnn"),
        ("DATA-DOMAIN-MIB", "scsitargetPortFcCurrentWwpn"),
        ("DATA-DOMAIN-MIB", "scsitargetPortFcp2Retry"),
        ("DATA-DOMAIN-MIB", "scsitargetPortConnectionType"),
        ("DATA-DOMAIN-MIB", "scsitargetPortLinkSpeed"),
        ("DATA-DOMAIN-MIB", "scsitargetPortFcTopology"),
        ("DATA-DOMAIN-MIB", "scsitargetPortEndpPort"),
        ("DATA-DOMAIN-MIB", "scsitargetPortEndpEndpoint"),
        ("DATA-DOMAIN-MIB", "scsitargetPortEndpEnabled"),
        ("DATA-DOMAIN-MIB", "scsitargetPortEndpStatus"),
        ("DATA-DOMAIN-MIB", "scsitargetPortEndpCurrentInstance"),
        ("DATA-DOMAIN-MIB", "scsitargetDeviceName"),
        ("DATA-DOMAIN-MIB", "scsitargetDeviceService"),
        ("DATA-DOMAIN-MIB", "scsitargetDeviceActiveState"),
        ("DATA-DOMAIN-MIB", "scsitargetDeviceAddress"),
        ("DATA-DOMAIN-MIB", "scsitargetDeviceGrpDevice"),
        ("DATA-DOMAIN-MIB", "scsitargetDeviceGrpGroupName"),
        ("DATA-DOMAIN-MIB", "scsitargetDeviceGrpLun"),
        ("DATA-DOMAIN-MIB", "scsitargetDeviceGrpPrimaryEndpoints"),
        ("DATA-DOMAIN-MIB", "scsitargetDeviceGrpSecondaryEndpoints"),
        ("DATA-DOMAIN-MIB", "scsitargetDeviceGrpInUseEndpoints"))
)
if mibBuilder.loadTexts:
    scsitargetObjectGroup.setStatus("current")

cifsGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19746, 0, 2, 30)
)
cifsGroupRev1.setObjects(
      *(("DATA-DOMAIN-MIB", "cifsStatus"),
        ("DATA-DOMAIN-MIB", "cifsConfigMode"),
        ("DATA-DOMAIN-MIB", "cifsConfigWINSServer"),
        ("DATA-DOMAIN-MIB", "cifsConfigNetBIOSHostname"),
        ("DATA-DOMAIN-MIB", "cifsConfigDomainController"),
        ("DATA-DOMAIN-MIB", "cifsConfigDNS"),
        ("DATA-DOMAIN-MIB", "cifsConfigGroupName"),
        ("DATA-DOMAIN-MIB", "cifsConfigMaxConnection"),
        ("DATA-DOMAIN-MIB", "cifsConfigMaxOpenFiles"),
        ("DATA-DOMAIN-MIB", "cifsShareName"),
        ("DATA-DOMAIN-MIB", "cifsSharePath"),
        ("DATA-DOMAIN-MIB", "cifsShareClients"),
        ("DATA-DOMAIN-MIB", "cifsShareUser"),
        ("DATA-DOMAIN-MIB", "cifsShareComment"),
        ("DATA-DOMAIN-MIB", "cifsShareBrowsing"),
        ("DATA-DOMAIN-MIB", "cifsShareWriteable"),
        ("DATA-DOMAIN-MIB", "cifsShareMaxConnection"),
        ("DATA-DOMAIN-MIB", "cifsOptionsName"),
        ("DATA-DOMAIN-MIB", "cifsOptionsValue"))
)
if mibBuilder.loadTexts:
    cifsGroupRev1.setStatus("current")


# Notification objects

powerSupplyFailedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 1)
)
if mibBuilder.loadTexts:
    powerSupplyFailedAlarm.setStatus(
        "deprecated"
    )

systemOverheatWarningAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 2)
)
systemOverheatWarningAlarm.setObjects(
    ("DATA-DOMAIN-MIB", "tempSensorDescription")
)
if mibBuilder.loadTexts:
    systemOverheatWarningAlarm.setStatus(
        "deprecated"
    )

systemOverheatAlertAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 3)
)
systemOverheatAlertAlarm.setObjects(
    ("DATA-DOMAIN-MIB", "tempSensorDescription")
)
if mibBuilder.loadTexts:
    systemOverheatAlertAlarm.setStatus(
        "deprecated"
    )

systemOverheatShutdownAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 4)
)
systemOverheatShutdownAlarm.setObjects(
    ("DATA-DOMAIN-MIB", "tempSensorDescription")
)
if mibBuilder.loadTexts:
    systemOverheatShutdownAlarm.setStatus(
        "deprecated"
    )

fanModuleFailedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5)
)
fanModuleFailedAlarm.setObjects(
    ("DATA-DOMAIN-MIB", "fanDescription")
)
if mibBuilder.loadTexts:
    fanModuleFailedAlarm.setStatus(
        "deprecated"
    )

nvramFailingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6)
)
if mibBuilder.loadTexts:
    nvramFailingAlarm.setStatus(
        "deprecated"
    )

fileSystemFailedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 7)
)
if mibBuilder.loadTexts:
    fileSystemFailedAlarm.setStatus(
        "deprecated"
    )

fileSpaceMaintenanceAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 8)
)
fileSpaceMaintenanceAlarm.setObjects(
    ("DATA-DOMAIN-MIB", "fileSystemResourceName")
)
if mibBuilder.loadTexts:
    fileSpaceMaintenanceAlarm.setStatus(
        "deprecated"
    )

fileSpacePreWarningAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 9)
)
fileSpacePreWarningAlarm.setObjects(
    ("DATA-DOMAIN-MIB", "fileSystemResourceName")
)
if mibBuilder.loadTexts:
    fileSpacePreWarningAlarm.setStatus(
        "deprecated"
    )

fileSpaceWarningAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 10)
)
fileSpaceWarningAlarm.setObjects(
    ("DATA-DOMAIN-MIB", "fileSystemResourceName")
)
if mibBuilder.loadTexts:
    fileSpaceWarningAlarm.setStatus(
        "deprecated"
    )

fileSpaceSevereAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 11)
)
fileSpaceSevereAlarm.setObjects(
    ("DATA-DOMAIN-MIB", "fileSystemResourceName")
)
if mibBuilder.loadTexts:
    fileSpaceSevereAlarm.setStatus(
        "deprecated"
    )

fileSpaceCriticalAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 12)
)
fileSpaceCriticalAlarm.setObjects(
    ("DATA-DOMAIN-MIB", "fileSystemResourceName")
)
if mibBuilder.loadTexts:
    fileSpaceCriticalAlarm.setStatus(
        "deprecated"
    )

diskFailedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 14)
)
diskFailedAlarm.setObjects(
    ("DATA-DOMAIN-MIB", "diskSerialNumber")
)
if mibBuilder.loadTexts:
    diskFailedAlarm.setStatus(
        "deprecated"
    )

diskOverheatWarningAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 15)
)
diskOverheatWarningAlarm.setObjects(
    ("DATA-DOMAIN-MIB", "diskTemperature")
)
if mibBuilder.loadTexts:
    diskOverheatWarningAlarm.setStatus(
        "deprecated"
    )

diskOverheatAlertAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 16)
)
diskOverheatAlertAlarm.setObjects(
    ("DATA-DOMAIN-MIB", "diskTemperature")
)
if mibBuilder.loadTexts:
    diskOverheatAlertAlarm.setStatus(
        "deprecated"
    )

diskOverheatShutdownAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 17)
)
diskOverheatShutdownAlarm.setObjects(
    ("DATA-DOMAIN-MIB", "diskTemperature")
)
if mibBuilder.loadTexts:
    diskOverheatShutdownAlarm.setStatus(
        "deprecated"
    )

raidReconSevereAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 18)
)
if mibBuilder.loadTexts:
    raidReconSevereAlarm.setStatus(
        "deprecated"
    )

raidReconCriticalAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 19)
)
if mibBuilder.loadTexts:
    raidReconCriticalAlarm.setStatus(
        "deprecated"
    )

raidReconCriticalShutdownAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 20)
)
if mibBuilder.loadTexts:
    raidReconCriticalShutdownAlarm.setStatus(
        "deprecated"
    )

raidGroupMissingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 21)
)
if mibBuilder.loadTexts:
    raidGroupMissingAlarm.setStatus(
        "deprecated"
    )

diskNoSpareAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 22)
)
if mibBuilder.loadTexts:
    diskNoSpareAlarm.setStatus(
        "deprecated"
    )

diskPathAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 23)
)
diskPathAlarm.setObjects(
    ("DATA-DOMAIN-MIB", "diskSerialNumber")
)
if mibBuilder.loadTexts:
    diskPathAlarm.setStatus(
        "deprecated"
    )

diskSASAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 24)
)
if mibBuilder.loadTexts:
    diskSASAlarm.setStatus(
        "deprecated"
    )

diskSASHBAAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 25)
)
diskSASHBAAlarm.setObjects(
    ("DATA-DOMAIN-MIB", "diskSerialNumber")
)
if mibBuilder.loadTexts:
    diskSASHBAAlarm.setStatus(
        "deprecated"
    )

snapshotFullAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 26)
)
if mibBuilder.loadTexts:
    snapshotFullAlarm.setStatus(
        "deprecated"
    )

snapshotHWMAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 27)
)
if mibBuilder.loadTexts:
    snapshotHWMAlarm.setStatus(
        "deprecated"
    )

clusterNodeAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 28)
)
if mibBuilder.loadTexts:
    clusterNodeAlarm.setStatus(
        "deprecated"
    )

clusterInterfaceAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 29)
)
if mibBuilder.loadTexts:
    clusterInterfaceAlarm.setStatus(
        "deprecated"
    )

replSyncAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 30)
)
replSyncAlarm.setObjects(
    ("DATA-DOMAIN-MIB", "replStatus")
)
if mibBuilder.loadTexts:
    replSyncAlarm.setStatus(
        "deprecated"
    )

systemStartupAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 31)
)
if mibBuilder.loadTexts:
    systemStartupAlarm.setStatus(
        "deprecated"
    )

filesysRelaunchAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 32)
)
if mibBuilder.loadTexts:
    filesysRelaunchAlarm.setStatus(
        "deprecated"
    )

filesysDDGCFailedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 33)
)
if mibBuilder.loadTexts:
    filesysDDGCFailedAlarm.setStatus(
        "deprecated"
    )

filesysGeneralProblemAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 34)
)
if mibBuilder.loadTexts:
    filesysGeneralProblemAlarm.setStatus(
        "deprecated"
    )

diskUnsupportedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 35)
)
diskUnsupportedAlarm.setObjects(
    ("DATA-DOMAIN-MIB", "diskSerialNumber")
)
if mibBuilder.loadTexts:
    diskUnsupportedAlarm.setStatus(
        "deprecated"
    )

eventIPMIUnmanageAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 36)
)
if mibBuilder.loadTexts:
    eventIPMIUnmanageAlarm.setStatus(
        "deprecated"
    )

controllerUnreachableAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5002)
)
controllerUnreachableAlert.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    controllerUnreachableAlert.setStatus(
        "current"
    )

controllerIfaceUnreachableAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5003)
)
controllerIfaceUnreachableAlert.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    controllerIfaceUnreachableAlert.setStatus(
        "current"
    )

correctableECCLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5004)
)
correctableECCLimitReached.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    correctableECCLimitReached.setStatus(
        "current"
    )

uncorrectableECCerror = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5005)
)
uncorrectableECCerror.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    uncorrectableECCerror.setStatus(
        "current"
    )

legacyChassisTempWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5006)
)
legacyChassisTempWarning.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    legacyChassisTempWarning.setStatus(
        "current"
    )

legacyChassisTempCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5007)
)
legacyChassisTempCritical.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    legacyChassisTempCritical.setStatus(
        "current"
    )

legacyPowerSupplyWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5008)
)
legacyPowerSupplyWarning.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "powerModuleDescription"))
)
if mibBuilder.loadTexts:
    legacyPowerSupplyWarning.setStatus(
        "current"
    )

legacyFanWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5009)
)
legacyFanWarning.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    legacyFanWarning.setStatus(
        "current"
    )

powerSupplyWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5010)
)
powerSupplyWarning.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    powerSupplyWarning.setStatus(
        "current"
    )

fanWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5011)
)
fanWarning.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    fanWarning.setStatus(
        "current"
    )

voltageWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5012)
)
voltageWarning.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    voltageWarning.setStatus(
        "current"
    )

powerWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5013)
)
powerWarning.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    powerWarning.setStatus(
        "current"
    )

correctECCWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5014)
)
correctECCWarning.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    correctECCWarning.setStatus(
        "current"
    )

processorWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5016)
)
processorWarning.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    processorWarning.setStatus(
        "current"
    )

powerUnitWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5017)
)
powerUnitWarning.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    powerUnitWarning.setStatus(
        "current"
    )

unCorrectECCWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5018)
)
unCorrectECCWarning.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    unCorrectECCWarning.setStatus(
        "current"
    )

chassisSensorCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5020)
)
chassisSensorCritical.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    chassisSensorCritical.setStatus(
        "current"
    )

chassisTempWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5021)
)
chassisTempWarning.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    chassisTempWarning.setStatus(
        "current"
    )

chassisTempCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5022)
)
chassisTempCritical.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    chassisTempCritical.setStatus(
        "current"
    )

cPUFailureWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5023)
)
cPUFailureWarning.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    cPUFailureWarning.setStatus(
        "current"
    )

legacyBMCHangCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5024)
)
legacyBMCHangCritical.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    legacyBMCHangCritical.setStatus(
        "current"
    )

bMCHangCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5025)
)
bMCHangCritical.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    bMCHangCritical.setStatus(
        "current"
    )

abnormalShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5026)
)
abnormalShutdown.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    abnormalShutdown.setStatus(
        "current"
    )

tooManyRelaunches = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5027)
)
tooManyRelaunches.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    tooManyRelaunches.setStatus(
        "current"
    )

filesystemProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5028)
)
filesystemProblem.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    filesystemProblem.setStatus(
        "current"
    )

dDFSFailedInShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5030)
)
dDFSFailedInShutdown.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    dDFSFailedInShutdown.setStatus(
        "current"
    )

dDFSNoHeartbeat = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5034)
)
dDFSNoHeartbeat.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    dDFSNoHeartbeat.setStatus(
        "current"
    )

dDFSDiedAfterReboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5036)
)
dDFSDiedAfterReboot.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    dDFSDiedAfterReboot.setStatus(
        "current"
    )

dDFSDied = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5037)
)
dDFSDied.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    dDFSDied.setStatus(
        "current"
    )

dDFSRebooted = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5038)
)
dDFSRebooted.setObjects(
    ("DATA-DOMAIN-MIB", "systemSerialNumber")
)
if mibBuilder.loadTexts:
    dDFSRebooted.setStatus(
        "current"
    )

dDFSRebootedDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5039)
)
dDFSRebootedDisabled.setObjects(
    ("DATA-DOMAIN-MIB", "systemSerialNumber")
)
if mibBuilder.loadTexts:
    dDFSRebootedDisabled.setStatus(
        "current"
    )

indexRebuildComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5040)
)
indexRebuildComplete.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    indexRebuildComplete.setStatus(
        "current"
    )

historicalDatabaseRecoverError = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5041)
)
historicalDatabaseRecoverError.setObjects(
    ("DATA-DOMAIN-MIB", "systemSerialNumber")
)
if mibBuilder.loadTexts:
    historicalDatabaseRecoverError.setStatus(
        "current"
    )

historicalDatabaseBackupError = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5042)
)
historicalDatabaseBackupError.setObjects(
    ("DATA-DOMAIN-MIB", "systemSerialNumber")
)
if mibBuilder.loadTexts:
    historicalDatabaseBackupError.setStatus(
        "current"
    )

historicalDatabaseUpgradeError = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5043)
)
historicalDatabaseUpgradeError.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    historicalDatabaseUpgradeError.setStatus(
        "current"
    )

historicalDatabasePruneError = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5044)
)
historicalDatabasePruneError.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    historicalDatabasePruneError.setStatus(
        "current"
    )

noHistoricalDatabaseError = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5045)
)
noHistoricalDatabaseError.setObjects(
    ("DATA-DOMAIN-MIB", "systemSerialNumber")
)
if mibBuilder.loadTexts:
    noHistoricalDatabaseError.setStatus(
        "current"
    )

hDTFileTransferFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5046)
)
hDTFileTransferFailed.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    hDTFileTransferFailed.setStatus(
        "current"
    )

hDTSystemError = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5047)
)
hDTSystemError.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    hDTSystemError.setStatus(
        "current"
    )

dIMMFailureAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5048)
)
dIMMFailureAlert.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    dIMMFailureAlert.setStatus(
        "current"
    )

memoryAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5049)
)
memoryAlert.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    memoryAlert.setStatus(
        "current"
    )

portPathDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5050)
)
portPathDisabled.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    portPathDisabled.setStatus(
        "current"
    )

diskPathRedundancy = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5051)
)
diskPathRedundancy.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    diskPathRedundancy.setStatus(
        "current"
    )

missingPortConnection = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5052)
)
missingPortConnection.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    missingPortConnection.setStatus(
        "current"
    )

missingLunPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5053)
)
missingLunPath.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    missingLunPath.setStatus(
        "current"
    )

missingDiskPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5054)
)
missingDiskPath.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "diskSerialNumber"))
)
if mibBuilder.loadTexts:
    missingDiskPath.setStatus(
        "current"
    )

missingEnclosurePath = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5055)
)
missingEnclosurePath.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    missingEnclosurePath.setStatus(
        "current"
    )

nvramWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5059)
)
nvramWarning.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    nvramWarning.setStatus(
        "current"
    )

nvramBatteryAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5060)
)
nvramBatteryAlert.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "nvramBatteryStatus"))
)
if mibBuilder.loadTexts:
    nvramBatteryAlert.setStatus(
        "current"
    )

nvramErrorAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5061)
)
nvramErrorAlert.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    nvramErrorAlert.setStatus(
        "current"
    )

phyalert = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5062)
)
phyalert.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    phyalert.setStatus(
        "current"
    )

replProgressThreshholdReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5063)
)
replProgressThreshholdReached.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "replStatus"))
)
if mibBuilder.loadTexts:
    replProgressThreshholdReached.setStatus(
        "current"
    )

replNeedResync = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5064)
)
replNeedResync.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "replStatus"))
)
if mibBuilder.loadTexts:
    replNeedResync.setStatus(
        "current"
    )

replLogFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5065)
)
replLogFull.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    replLogFull.setStatus(
        "current"
    )

replIncompatibleWorm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5066)
)
replIncompatibleWorm.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    replIncompatibleWorm.setStatus(
        "current"
    )

replDestNotConfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5067)
)
replDestNotConfigured.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "replConfigDest"))
)
if mibBuilder.loadTexts:
    replDestNotConfigured.setStatus(
        "current"
    )

replLagThreshholdReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5068)
)
replLagThreshholdReached.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    replLagThreshholdReached.setStatus(
        "current"
    )

sASEnclosureCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5069)
)
sASEnclosureCheck.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    sASEnclosureCheck.setStatus(
        "current"
    )

sASTopologyCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5070)
)
sASTopologyCheck.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    sASTopologyCheck.setStatus(
        "current"
    )

sASPortDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5071)
)
sASPortDisabled.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    sASPortDisabled.setStatus(
        "current"
    )

sSLCertificateCorrupted = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5072)
)
sSLCertificateCorrupted.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    sSLCertificateCorrupted.setStatus(
        "current"
    )

snapshotOver90Percent = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5075)
)
snapshotOver90Percent.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    snapshotOver90Percent.setStatus(
        "current"
    )

snapshotLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5076)
)
snapshotLimitReached.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    snapshotLimitReached.setStatus(
        "current"
    )

sNTZMultipleIterations = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5077)
)
sNTZMultipleIterations.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    sNTZMultipleIterations.setStatus(
        "current"
    )

coredumpWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5078)
)
coredumpWarning.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    coredumpWarning.setStatus(
        "current"
    )

coredumpDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5079)
)
coredumpDisabled.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    coredumpDisabled.setStatus(
        "current"
    )

spaceOver80Percent = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5080)
)
spaceOver80Percent.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "fileSystemSpaceUsed"))
)
if mibBuilder.loadTexts:
    spaceOver80Percent.setStatus(
        "current"
    )

spaceOver90Percent = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5081)
)
spaceOver90Percent.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "fileSystemSpaceUsed"))
)
if mibBuilder.loadTexts:
    spaceOver90Percent.setStatus(
        "current"
    )

diskAccessError = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5082)
)
diskAccessError.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "diskSerialNumber"))
)
if mibBuilder.loadTexts:
    diskAccessError.setStatus(
        "current"
    )

diskFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5083)
)
diskFailure.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "diskSerialNumber"))
)
if mibBuilder.loadTexts:
    diskFailure.setStatus(
        "current"
    )

diskTemperatureWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5084)
)
diskTemperatureWarning.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "diskTemperature"))
)
if mibBuilder.loadTexts:
    diskTemperatureWarning.setStatus(
        "current"
    )

diskTemperatureShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5085)
)
diskTemperatureShutdown.setObjects(
    ("DATA-DOMAIN-MIB", "systemSerialNumber")
)
if mibBuilder.loadTexts:
    diskTemperatureShutdown.setStatus(
        "current"
    )

unsupportedHardwareSpareSize = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5086)
)
unsupportedHardwareSpareSize.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "diskSerialNumber"))
)
if mibBuilder.loadTexts:
    unsupportedHardwareSpareSize.setStatus(
        "current"
    )

missingDiskGroup = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5087)
)
missingDiskGroup.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    missingDiskGroup.setStatus(
        "current"
    )

diskGroupReconstructionNoProgress = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5088)
)
diskGroupReconstructionNoProgress.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    diskGroupReconstructionNoProgress.setStatus(
        "current"
    )

diskGroupReconstruction = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5089)
)
diskGroupReconstruction.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    diskGroupReconstruction.setStatus(
        "current"
    )

diskGroupReconstructionShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5090)
)
diskGroupReconstructionShutdown.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    diskGroupReconstructionShutdown.setStatus(
        "current"
    )

diskGroupReconstructionCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5091)
)
diskGroupReconstructionCritical.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    diskGroupReconstructionCritical.setStatus(
        "current"
    )

diskUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5092)
)
diskUnknown.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    diskUnknown.setStatus(
        "current"
    )

lowSpares = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5094)
)
lowSpares.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    lowSpares.setStatus(
        "current"
    )

unsupportedConfigurationROL = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5095)
)
unsupportedConfigurationROL.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    unsupportedConfigurationROL.setStatus(
        "current"
    )

cpismissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5500)
)
cpismissing.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    cpismissing.setStatus(
        "current"
    )

containerMarkedInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5501)
)
containerMarkedInvalid.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    containerMarkedInvalid.setStatus(
        "current"
    )

smiMrc = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5502)
)
smiMrc.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    smiMrc.setStatus(
        "current"
    )

nvramBatteryLowChargeAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5508)
)
nvramBatteryLowChargeAlert.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    nvramBatteryLowChargeAlert.setStatus(
        "current"
    )

ext3NvlogDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5527)
)
ext3NvlogDisabled.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    ext3NvlogDisabled.setStatus(
        "current"
    )

enclosureMixType = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5528)
)
enclosureMixType.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    enclosureMixType.setStatus(
        "current"
    )

replPathTooLong = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 5531)
)
replPathTooLong.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    replPathTooLong.setStatus(
        "current"
    )

compromisedEncryptionKeys = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6001)
)
compromisedEncryptionKeys.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    compromisedEncryptionKeys.setStatus(
        "current"
    )

newEncryptionKey = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6002)
)
newEncryptionKey.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    newEncryptionKey.setStatus(
        "current"
    )

encryptionKeyTableFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6003)
)
encryptionKeyTableFull.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    encryptionKeyTableFull.setStatus(
        "current"
    )

uncertifiedFirmware = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6004)
)
uncertifiedFirmware.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    uncertifiedFirmware.setStatus(
        "current"
    )

filesystemNVRAMDataLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6005)
)
filesystemNVRAMDataLoss.setObjects(
    ("DATA-DOMAIN-MIB", "systemSerialNumber")
)
if mibBuilder.loadTexts:
    filesystemNVRAMDataLoss.setStatus(
        "current"
    )

mtreeQuotaSoftLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6007)
)
mtreeQuotaSoftLimit.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    mtreeQuotaSoftLimit.setStatus(
        "current"
    )

mtreeQuotaHardLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6008)
)
mtreeQuotaHardLimit.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    mtreeQuotaHardLimit.setStatus(
        "current"
    )

interfaceConnectivityDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6009)
)
interfaceConnectivityDown.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    interfaceConnectivityDown.setStatus(
        "current"
    )

interfaceConnectivityIntermittent = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6010)
)
interfaceConnectivityIntermittent.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    interfaceConnectivityIntermittent.setStatus(
        "current"
    )

interfaceMisconfiguration = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6011)
)
interfaceMisconfiguration.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    interfaceMisconfiguration.setStatus(
        "current"
    )

recoverFromNVRAMFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6013)
)
recoverFromNVRAMFailed.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    recoverFromNVRAMFailed.setStatus(
        "current"
    )

cleaningError = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6014)
)
cleaningError.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    cleaningError.setStatus(
        "current"
    )

bMCPartialHang = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6015)
)
bMCPartialHang.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    bMCPartialHang.setStatus(
        "current"
    )

fileMigrationError = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6016)
)
fileMigrationError.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    fileMigrationError.setStatus(
        "current"
    )

unusableHostCertificate = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6017)
)
unusableHostCertificate.setObjects(
    ("DATA-DOMAIN-MIB", "systemSerialNumber")
)
if mibBuilder.loadTexts:
    unusableHostCertificate.setStatus(
        "current"
    )

missingHostCertificate = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6018)
)
missingHostCertificate.setObjects(
    ("DATA-DOMAIN-MIB", "systemSerialNumber")
)
if mibBuilder.loadTexts:
    missingHostCertificate.setStatus(
        "current"
    )

foreignEnclosure = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6019)
)
foreignEnclosure.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "enclosureListNum"))
)
if mibBuilder.loadTexts:
    foreignEnclosure.setStatus(
        "current"
    )

interfaceConnectivityUpAndRunning = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6020)
)
interfaceConnectivityUpAndRunning.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    interfaceConnectivityUpAndRunning.setStatus(
        "current"
    )

tcpZeroWindowAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6101)
)
tcpZeroWindowAlert.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    tcpZeroWindowAlert.setStatus(
        "current"
    )

insecureEncryptedReplication = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6102)
)
insecureEncryptedReplication.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    insecureEncryptedReplication.setStatus(
        "current"
    )

nvramHWAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6504)
)
nvramHWAlert.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    nvramHWAlert.setStatus(
        "current"
    )

nvramEnvAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6505)
)
nvramEnvAlert.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    nvramEnvAlert.setStatus(
        "current"
    )

nvramEventHWAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6506)
)
nvramEventHWAlert.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    nvramEventHWAlert.setStatus(
        "current"
    )

nvramBattAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6507)
)
nvramBattAlert.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    nvramBattAlert.setStatus(
        "current"
    )

nvramCondAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6508)
)
nvramCondAlert.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    nvramCondAlert.setStatus(
        "current"
    )

upgradeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6509)
)
upgradeFailure.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    upgradeFailure.setStatus(
        "current"
    )

upgradeCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6510)
)
upgradeCompleted.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    upgradeCompleted.setStatus(
        "current"
    )

mailserverError = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6511)
)
mailserverError.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    mailserverError.setStatus(
        "current"
    )

invalidNICSlot = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6512)
)
invalidNICSlot.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    invalidNICSlot.setStatus(
        "current"
    )

unsupportedNIC = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6513)
)
unsupportedNIC.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    unsupportedNIC.setStatus(
        "current"
    )

sASHBAFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6514)
)
sASHBAFailure.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    sASHBAFailure.setStatus(
        "current"
    )

sASHBAErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6515)
)
sASHBAErrors.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    sASHBAErrors.setStatus(
        "current"
    )

unsupportedSASDevice = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6516)
)
unsupportedSASDevice.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    unsupportedSASDevice.setStatus(
        "current"
    )

fanFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6517)
)
fanFault.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    fanFault.setStatus(
        "current"
    )

powerSupplyInputFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6518)
)
powerSupplyInputFault.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    powerSupplyInputFault.setStatus(
        "current"
    )

powerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6519)
)
powerSupplyFailure.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    powerSupplyFailure.setStatus(
        "current"
    )

powerSupplyAbsent = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6520)
)
powerSupplyAbsent.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    powerSupplyAbsent.setStatus(
        "current"
    )

unsupportedACVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6521)
)
unsupportedACVoltage.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    unsupportedACVoltage.setStatus(
        "current"
    )

iOModuleFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6522)
)
iOModuleFault.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    iOModuleFault.setStatus(
        "current"
    )

iOModuleInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6523)
)
iOModuleInserted.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    iOModuleInserted.setStatus(
        "current"
    )

mgmtModuleFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6524)
)
mgmtModuleFault.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    mgmtModuleFault.setStatus(
        "current"
    )

dIMMFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6525)
)
dIMMFailure.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    dIMMFailure.setStatus(
        "current"
    )

sPFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6526)
)
sPFault.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    sPFault.setStatus(
        "current"
    )

chassisFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6527)
)
chassisFailure.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    chassisFailure.setStatus(
        "current"
    )

forcedControllerShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6528)
)
forcedControllerShutdown.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    forcedControllerShutdown.setStatus(
        "current"
    )

systemReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6529)
)
systemReset.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    systemReset.setStatus(
        "current"
    )

duplicateAddressDetection = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6530)
)
duplicateAddressDetection.setObjects(
    ("DATA-DOMAIN-MIB", "systemSerialNumber")
)
if mibBuilder.loadTexts:
    duplicateAddressDetection.setStatus(
        "current"
    )

spaceReclRestartFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6531)
)
spaceReclRestartFailed.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    spaceReclRestartFailed.setStatus(
        "current"
    )

spaceReclMissingUnit = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6532)
)
spaceReclMissingUnit.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    spaceReclMissingUnit.setStatus(
        "current"
    )

spaceReclUnitReclaimed = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6533)
)
spaceReclUnitReclaimed.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    spaceReclUnitReclaimed.setStatus(
        "current"
    )

spaceReclError = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6534)
)
spaceReclError.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    spaceReclError.setStatus(
        "current"
    )

enclosureHighTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6535)
)
enclosureHighTemp.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    enclosureHighTemp.setStatus(
        "current"
    )

unsupportedSystemType = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6536)
)
unsupportedSystemType.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    unsupportedSystemType.setStatus(
        "current"
    )

bMCHangShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6537)
)
bMCHangShutdown.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    bMCHangShutdown.setStatus(
        "current"
    )

expiredHostCertificate = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6538)
)
expiredHostCertificate.setObjects(
    ("DATA-DOMAIN-MIB", "systemSerialNumber")
)
if mibBuilder.loadTexts:
    expiredHostCertificate.setStatus(
        "current"
    )

sCSITGTInvalidRegistry = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6539)
)
sCSITGTInvalidRegistry.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    sCSITGTInvalidRegistry.setStatus(
        "current"
    )

encryptionKeyExportFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6540)
)
encryptionKeyExportFailed.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    encryptionKeyExportFailed.setStatus(
        "current"
    )

sSDEndOfLife = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6541)
)
sSDEndOfLife.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "diskSerialNumber"))
)
if mibBuilder.loadTexts:
    sSDEndOfLife.setStatus(
        "current"
    )

tapeReposition = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6542)
)
tapeReposition.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    tapeReposition.setStatus(
        "current"
    )

multipleDiskReadErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6543)
)
multipleDiskReadErrors.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    multipleDiskReadErrors.setStatus(
        "current"
    )

missingCreplUnits = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6544)
)
missingCreplUnits.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    missingCreplUnits.setStatus(
        "current"
    )

nvramBattEndOfLife = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 6545)
)
nvramBattEndOfLife.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    nvramBattEndOfLife.setStatus(
        "current"
    )

bMCFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 7000)
)
bMCFailure.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    bMCFailure.setStatus(
        "current"
    )

unsupportedDriveModel = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 7001)
)
unsupportedDriveModel.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    unsupportedDriveModel.setStatus(
        "current"
    )

driveMixType = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 7002)
)
driveMixType.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    driveMixType.setStatus(
        "current"
    )

sMSUnresponsive = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 7500)
)
sMSUnresponsive.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    sMSUnresponsive.setStatus(
        "current"
    )

nISCommFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 7501)
)
nISCommFailure.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    nISCommFailure.setStatus(
        "current"
    )

unsupportedHardwareConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 7502)
)
unsupportedHardwareConfig.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    unsupportedHardwareConfig.setStatus(
        "current"
    )

unsupportedVirtualCPU = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 7503)
)
unsupportedVirtualCPU.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    unsupportedVirtualCPU.setStatus(
        "current"
    )

dNSUnresponsive = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 7504)
)
dNSUnresponsive.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    dNSUnresponsive.setStatus(
        "current"
    )

nTPDFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 7505)
)
nTPDFailed.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    nTPDFailed.setStatus(
        "current"
    )

invalidEnclosureTopology = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 7506)
)
invalidEnclosureTopology.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    invalidEnclosureTopology.setStatus(
        "current"
    )

diskPathSpeedDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 7507)
)
diskPathSpeedDegraded.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    diskPathSpeedDegraded.setStatus(
        "current"
    )

targetDriverPortOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 7508)
)
targetDriverPortOffline.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    targetDriverPortOffline.setStatus(
        "current"
    )

targetDriverPortOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 7509)
)
targetDriverPortOnline.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    targetDriverPortOnline.setStatus(
        "current"
    )

targetDriverPortCore = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 7510)
)
targetDriverPortCore.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    targetDriverPortCore.setStatus(
        "current"
    )

targetDriverPortMultipleCore = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 7511)
)
targetDriverPortMultipleCore.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    targetDriverPortMultipleCore.setStatus(
        "current"
    )

targetDriverPortFWLoadFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 7512)
)
targetDriverPortFWLoadFailed.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    targetDriverPortFWLoadFailed.setStatus(
        "current"
    )

targetDriverPortUnreadable = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 7513)
)
targetDriverPortUnreadable.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    targetDriverPortUnreadable.setStatus(
        "current"
    )

targetDriverPortTooManyOsc = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 7514)
)
targetDriverPortTooManyOsc.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    targetDriverPortTooManyOsc.setStatus(
        "current"
    )

insufficientSpaceForEncryption = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 7515)
)
insufficientSpaceForEncryption.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    insufficientSpaceForEncryption.setStatus(
        "current"
    )

dDFSRequiresReboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 7516)
)
dDFSRequiresReboot.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    dDFSRequiresReboot.setStatus(
        "current"
    )

storageUnitStreamSoftLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 7517)
)
storageUnitStreamSoftLimit.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    storageUnitStreamSoftLimit.setStatus(
        "current"
    )

spaceReclSuspended = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 7518)
)
spaceReclSuspended.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    spaceReclSuspended.setStatus(
        "current"
    )

metadataWarningThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 7519)
)
metadataWarningThreshold.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    metadataWarningThreshold.setStatus(
        "current"
    )

mtreeCascadeNeedResync = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 7520)
)
mtreeCascadeNeedResync.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "replStatus"))
)
if mibBuilder.loadTexts:
    mtreeCascadeNeedResync.setStatus(
        "current"
    )

filesystemCorruption = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 7521)
)
filesystemCorruption.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    filesystemCorruption.setStatus(
        "current"
    )

missingTierStorage = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 7522)
)
missingTierStorage.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    missingTierStorage.setStatus(
        "current"
    )

spaceReclUnitError = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 7523)
)
spaceReclUnitError.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    spaceReclUnitError.setStatus(
        "current"
    )

bMCFailureSysBBU = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 7524)
)
bMCFailureSysBBU.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    bMCFailureSysBBU.setStatus(
        "current"
    )

licenseExpiring = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 8001)
)
licenseExpiring.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    licenseExpiring.setStatus(
        "current"
    )

licenseExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 8002)
)
licenseExpired.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    licenseExpired.setStatus(
        "current"
    )

unsupportedEnclosurePSU = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 10000)
)
unsupportedEnclosurePSU.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    unsupportedEnclosurePSU.setStatus(
        "current"
    )

unsupportedPowerSupply = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 10001)
)
unsupportedPowerSupply.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    unsupportedPowerSupply.setStatus(
        "current"
    )

openFanDrawer = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 10002)
)
openFanDrawer.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    openFanDrawer.setStatus(
        "current"
    )

memoryRiserFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 10003)
)
memoryRiserFault.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    memoryRiserFault.setStatus(
        "current"
    )

pCILinkDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 10004)
)
pCILinkDegraded.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    pCILinkDegraded.setStatus(
        "current"
    )

invalidHardwareCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 10005)
)
invalidHardwareCritical.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    invalidHardwareCritical.setStatus(
        "current"
    )

invalidHardwareWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 10006)
)
invalidHardwareWarning.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    invalidHardwareWarning.setStatus(
        "current"
    )

correctableErrorWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 10007)
)
correctableErrorWarning.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    correctableErrorWarning.setStatus(
        "current"
    )

spuriousInterruptDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 10008)
)
spuriousInterruptDisabled.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    spuriousInterruptDisabled.setStatus(
        "current"
    )

corruptEncryptionKeys = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 10009)
)
corruptEncryptionKeys.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    corruptEncryptionKeys.setStatus(
        "current"
    )

duplicateVTLPoolNames = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 10010)
)
duplicateVTLPoolNames.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    duplicateVTLPoolNames.setStatus(
        "current"
    )

generalHardwareFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 10011)
)
generalHardwareFailure.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    generalHardwareFailure.setStatus(
        "current"
    )

iOModuleMacFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 10013)
)
iOModuleMacFault.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    iOModuleMacFault.setStatus(
        "current"
    )

storageMigrationCannotResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 10500)
)
storageMigrationCannotResume.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    storageMigrationCannotResume.setStatus(
        "current"
    )

storageMigrationCopyComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 10501)
)
storageMigrationCopyComplete.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    storageMigrationCopyComplete.setStatus(
        "current"
    )

storageMigrationUserSuspend = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 10502)
)
storageMigrationUserSuspend.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    storageMigrationUserSuspend.setStatus(
        "current"
    )

cMTaskEnded = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 10503)
)
cMTaskEnded.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    cMTaskEnded.setStatus(
        "current"
    )

physicalCapacityMeasurementTasksLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 10504)
)
physicalCapacityMeasurementTasksLost.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    physicalCapacityMeasurementTasksLost.setStatus(
        "current"
    )

physicalCapacityMeasurementTasksLostMTree = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 10505)
)
physicalCapacityMeasurementTasksLostMTree.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    physicalCapacityMeasurementTasksLostMTree.setStatus(
        "current"
    )

physicalCapacityMeasurementScheduleFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 10506)
)
physicalCapacityMeasurementScheduleFailed.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    physicalCapacityMeasurementScheduleFailed.setStatus(
        "current"
    )

historicalDatabaseFailoverError = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 10507)
)
historicalDatabaseFailoverError.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    historicalDatabaseFailoverError.setStatus(
        "current"
    )

hAdegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 10508)
)
hAdegraded.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    hAdegraded.setStatus(
        "current"
    )

upgradeInProgress = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 10509)
)
upgradeInProgress.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    upgradeInProgress.setStatus(
        "current"
    )

hAofflineErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 10510)
)
hAofflineErrors.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    hAofflineErrors.setStatus(
        "current"
    )

suspendedMReplMissingUnits = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 10511)
)
suspendedMReplMissingUnits.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    suspendedMReplMissingUnits.setStatus(
        "current"
    )

foreignPack = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 10512)
)
foreignPack.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "enclosurePackID"))
)
if mibBuilder.loadTexts:
    foreignPack.setStatus(
        "current"
    )

vDiskSCSITargetMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 10513)
)
vDiskSCSITargetMismatch.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    vDiskSCSITargetMismatch.setStatus(
        "current"
    )

hATimeOutOfSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 10514)
)
hATimeOutOfSync.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    hATimeOutOfSync.setStatus(
        "current"
    )

enclosureMixDriveType = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 0, 10515)
)
enclosureMixDriveType.setObjects(
      *(("DATA-DOMAIN-MIB", "systemSerialNumber"),
        ("DATA-DOMAIN-MIB", "alertInfoDescription"))
)
if mibBuilder.loadTexts:
    enclosureMixDriveType.setStatus(
        "current"
    )


# Notifications groups

basicNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 19746, 0, 2, 9)
)
basicNotificationsGroup.setObjects(
      *(("DATA-DOMAIN-MIB", "powerSupplyFailedAlarm"),
        ("DATA-DOMAIN-MIB", "systemOverheatWarningAlarm"),
        ("DATA-DOMAIN-MIB", "systemOverheatAlertAlarm"),
        ("DATA-DOMAIN-MIB", "systemOverheatShutdownAlarm"),
        ("DATA-DOMAIN-MIB", "fanModuleFailedAlarm"),
        ("DATA-DOMAIN-MIB", "nvramFailingAlarm"),
        ("DATA-DOMAIN-MIB", "fileSystemFailedAlarm"),
        ("DATA-DOMAIN-MIB", "fileSpaceMaintenanceAlarm"),
        ("DATA-DOMAIN-MIB", "fileSpacePreWarningAlarm"),
        ("DATA-DOMAIN-MIB", "fileSpaceWarningAlarm"),
        ("DATA-DOMAIN-MIB", "fileSpaceSevereAlarm"),
        ("DATA-DOMAIN-MIB", "fileSpaceCriticalAlarm"),
        ("DATA-DOMAIN-MIB", "diskOverheatWarningAlarm"),
        ("DATA-DOMAIN-MIB", "diskOverheatAlertAlarm"),
        ("DATA-DOMAIN-MIB", "diskOverheatShutdownAlarm"),
        ("DATA-DOMAIN-MIB", "diskFailedAlarm"),
        ("DATA-DOMAIN-MIB", "diskNoSpareAlarm"),
        ("DATA-DOMAIN-MIB", "diskPathAlarm"),
        ("DATA-DOMAIN-MIB", "diskSASAlarm"),
        ("DATA-DOMAIN-MIB", "diskSASHBAAlarm"),
        ("DATA-DOMAIN-MIB", "snapshotFullAlarm"),
        ("DATA-DOMAIN-MIB", "snapshotHWMAlarm"),
        ("DATA-DOMAIN-MIB", "clusterNodeAlarm"),
        ("DATA-DOMAIN-MIB", "clusterInterfaceAlarm"),
        ("DATA-DOMAIN-MIB", "replSyncAlarm"),
        ("DATA-DOMAIN-MIB", "systemStartupAlarm"),
        ("DATA-DOMAIN-MIB", "filesysRelaunchAlarm"),
        ("DATA-DOMAIN-MIB", "filesysDDGCFailedAlarm"),
        ("DATA-DOMAIN-MIB", "filesysGeneralProblemAlarm"),
        ("DATA-DOMAIN-MIB", "diskUnsupportedAlarm"),
        ("DATA-DOMAIN-MIB", "eventIPMIUnmanageAlarm"),
        ("DATA-DOMAIN-MIB", "raidReconSevereAlarm"),
        ("DATA-DOMAIN-MIB", "raidReconCriticalAlarm"),
        ("DATA-DOMAIN-MIB", "raidReconCriticalShutdownAlarm"),
        ("DATA-DOMAIN-MIB", "raidGroupMissingAlarm"))
)
if mibBuilder.loadTexts:
    basicNotificationsGroup.setStatus(
        "deprecated"
    )

internalDiskStorageNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 19746, 0, 2, 10)
)
internalDiskStorageNotificationsGroup.setObjects(
      *(("DATA-DOMAIN-MIB", "diskFailedAlarm"),
        ("DATA-DOMAIN-MIB", "diskOverheatWarningAlarm"),
        ("DATA-DOMAIN-MIB", "diskOverheatAlertAlarm"),
        ("DATA-DOMAIN-MIB", "diskOverheatShutdownAlarm"))
)
if mibBuilder.loadTexts:
    internalDiskStorageNotificationsGroup.setStatus(
        "deprecated"
    )

generatedNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 19746, 0, 2, 5000)
)
generatedNotificationsGroup.setObjects(
      *(("DATA-DOMAIN-MIB", "cpismissing"),
        ("DATA-DOMAIN-MIB", "controllerUnreachableAlert"),
        ("DATA-DOMAIN-MIB", "controllerIfaceUnreachableAlert"),
        ("DATA-DOMAIN-MIB", "containerMarkedInvalid"),
        ("DATA-DOMAIN-MIB", "cMTaskEnded"),
        ("DATA-DOMAIN-MIB", "correctableECCLimitReached"),
        ("DATA-DOMAIN-MIB", "uncorrectableECCerror"),
        ("DATA-DOMAIN-MIB", "dIMMFailure"),
        ("DATA-DOMAIN-MIB", "compromisedEncryptionKeys"),
        ("DATA-DOMAIN-MIB", "newEncryptionKey"),
        ("DATA-DOMAIN-MIB", "encryptionKeyTableFull"),
        ("DATA-DOMAIN-MIB", "encryptionKeyExportFailed"),
        ("DATA-DOMAIN-MIB", "insufficientSpaceForEncryption"),
        ("DATA-DOMAIN-MIB", "corruptEncryptionKeys"),
        ("DATA-DOMAIN-MIB", "legacyChassisTempWarning"),
        ("DATA-DOMAIN-MIB", "legacyChassisTempCritical"),
        ("DATA-DOMAIN-MIB", "legacyPowerSupplyWarning"),
        ("DATA-DOMAIN-MIB", "legacyFanWarning"),
        ("DATA-DOMAIN-MIB", "powerSupplyWarning"),
        ("DATA-DOMAIN-MIB", "fanWarning"),
        ("DATA-DOMAIN-MIB", "voltageWarning"),
        ("DATA-DOMAIN-MIB", "powerWarning"),
        ("DATA-DOMAIN-MIB", "correctECCWarning"),
        ("DATA-DOMAIN-MIB", "processorWarning"),
        ("DATA-DOMAIN-MIB", "powerUnitWarning"),
        ("DATA-DOMAIN-MIB", "unCorrectECCWarning"),
        ("DATA-DOMAIN-MIB", "chassisSensorCritical"),
        ("DATA-DOMAIN-MIB", "chassisTempWarning"),
        ("DATA-DOMAIN-MIB", "chassisTempCritical"),
        ("DATA-DOMAIN-MIB", "cPUFailureWarning"),
        ("DATA-DOMAIN-MIB", "legacyBMCHangCritical"),
        ("DATA-DOMAIN-MIB", "bMCHangCritical"),
        ("DATA-DOMAIN-MIB", "abnormalShutdown"),
        ("DATA-DOMAIN-MIB", "smiMrc"),
        ("DATA-DOMAIN-MIB", "bMCPartialHang"),
        ("DATA-DOMAIN-MIB", "fanFault"),
        ("DATA-DOMAIN-MIB", "powerSupplyInputFault"),
        ("DATA-DOMAIN-MIB", "powerSupplyFailure"),
        ("DATA-DOMAIN-MIB", "powerSupplyAbsent"),
        ("DATA-DOMAIN-MIB", "unsupportedACVoltage"),
        ("DATA-DOMAIN-MIB", "iOModuleFault"),
        ("DATA-DOMAIN-MIB", "iOModuleInserted"),
        ("DATA-DOMAIN-MIB", "mgmtModuleFault"),
        ("DATA-DOMAIN-MIB", "sPFault"),
        ("DATA-DOMAIN-MIB", "chassisFailure"),
        ("DATA-DOMAIN-MIB", "forcedControllerShutdown"),
        ("DATA-DOMAIN-MIB", "systemReset"),
        ("DATA-DOMAIN-MIB", "enclosureHighTemp"),
        ("DATA-DOMAIN-MIB", "unsupportedSystemType"),
        ("DATA-DOMAIN-MIB", "bMCHangShutdown"),
        ("DATA-DOMAIN-MIB", "bMCFailure"),
        ("DATA-DOMAIN-MIB", "unsupportedHardwareConfig"),
        ("DATA-DOMAIN-MIB", "unsupportedVirtualCPU"),
        ("DATA-DOMAIN-MIB", "unsupportedPowerSupply"),
        ("DATA-DOMAIN-MIB", "openFanDrawer"),
        ("DATA-DOMAIN-MIB", "memoryRiserFault"),
        ("DATA-DOMAIN-MIB", "bMCFailureSysBBU"),
        ("DATA-DOMAIN-MIB", "unsupportedEnclosurePSU"),
        ("DATA-DOMAIN-MIB", "pCILinkDegraded"),
        ("DATA-DOMAIN-MIB", "invalidHardwareCritical"),
        ("DATA-DOMAIN-MIB", "invalidHardwareWarning"),
        ("DATA-DOMAIN-MIB", "correctableErrorWarning"),
        ("DATA-DOMAIN-MIB", "generalHardwareFailure"),
        ("DATA-DOMAIN-MIB", "targetDriverPortOffline"),
        ("DATA-DOMAIN-MIB", "targetDriverPortOnline"),
        ("DATA-DOMAIN-MIB", "targetDriverPortCore"),
        ("DATA-DOMAIN-MIB", "targetDriverPortMultipleCore"),
        ("DATA-DOMAIN-MIB", "targetDriverPortFWLoadFailed"),
        ("DATA-DOMAIN-MIB", "targetDriverPortUnreadable"),
        ("DATA-DOMAIN-MIB", "targetDriverPortTooManyOsc"),
        ("DATA-DOMAIN-MIB", "tooManyRelaunches"),
        ("DATA-DOMAIN-MIB", "filesystemProblem"),
        ("DATA-DOMAIN-MIB", "dDFSFailedInShutdown"),
        ("DATA-DOMAIN-MIB", "dDFSNoHeartbeat"),
        ("DATA-DOMAIN-MIB", "dDFSDiedAfterReboot"),
        ("DATA-DOMAIN-MIB", "dDFSDied"),
        ("DATA-DOMAIN-MIB", "dDFSRebooted"),
        ("DATA-DOMAIN-MIB", "dDFSRebootedDisabled"),
        ("DATA-DOMAIN-MIB", "indexRebuildComplete"),
        ("DATA-DOMAIN-MIB", "filesystemNVRAMDataLoss"),
        ("DATA-DOMAIN-MIB", "recoverFromNVRAMFailed"),
        ("DATA-DOMAIN-MIB", "dDFSRequiresReboot"),
        ("DATA-DOMAIN-MIB", "metadataWarningThreshold"),
        ("DATA-DOMAIN-MIB", "filesystemCorruption"),
        ("DATA-DOMAIN-MIB", "physicalCapacityMeasurementTasksLost"),
        ("DATA-DOMAIN-MIB", "physicalCapacityMeasurementTasksLostMTree"),
        ("DATA-DOMAIN-MIB", "physicalCapacityMeasurementScheduleFailed"),
        ("DATA-DOMAIN-MIB", "uncertifiedFirmware"),
        ("DATA-DOMAIN-MIB", "fileMigrationError"),
        ("DATA-DOMAIN-MIB", "cleaningError"),
        ("DATA-DOMAIN-MIB", "hAdegraded"),
        ("DATA-DOMAIN-MIB", "hAofflineErrors"),
        ("DATA-DOMAIN-MIB", "hATimeOutOfSync"),
        ("DATA-DOMAIN-MIB", "historicalDatabaseRecoverError"),
        ("DATA-DOMAIN-MIB", "historicalDatabaseBackupError"),
        ("DATA-DOMAIN-MIB", "historicalDatabaseUpgradeError"),
        ("DATA-DOMAIN-MIB", "historicalDatabasePruneError"),
        ("DATA-DOMAIN-MIB", "noHistoricalDatabaseError"),
        ("DATA-DOMAIN-MIB", "historicalDatabaseFailoverError"),
        ("DATA-DOMAIN-MIB", "hDTFileTransferFailed"),
        ("DATA-DOMAIN-MIB", "hDTSystemError"),
        ("DATA-DOMAIN-MIB", "spuriousInterruptDisabled"),
        ("DATA-DOMAIN-MIB", "licenseExpiring"),
        ("DATA-DOMAIN-MIB", "licenseExpired"),
        ("DATA-DOMAIN-MIB", "dIMMFailureAlert"),
        ("DATA-DOMAIN-MIB", "memoryAlert"),
        ("DATA-DOMAIN-MIB", "portPathDisabled"),
        ("DATA-DOMAIN-MIB", "diskPathRedundancy"),
        ("DATA-DOMAIN-MIB", "missingPortConnection"),
        ("DATA-DOMAIN-MIB", "missingLunPath"),
        ("DATA-DOMAIN-MIB", "missingDiskPath"),
        ("DATA-DOMAIN-MIB", "missingEnclosurePath"),
        ("DATA-DOMAIN-MIB", "interfaceConnectivityDown"),
        ("DATA-DOMAIN-MIB", "interfaceConnectivityIntermittent"),
        ("DATA-DOMAIN-MIB", "interfaceMisconfiguration"),
        ("DATA-DOMAIN-MIB", "interfaceConnectivityUpAndRunning"),
        ("DATA-DOMAIN-MIB", "duplicateAddressDetection"),
        ("DATA-DOMAIN-MIB", "invalidNICSlot"),
        ("DATA-DOMAIN-MIB", "unsupportedNIC"),
        ("DATA-DOMAIN-MIB", "tcpZeroWindowAlert"),
        ("DATA-DOMAIN-MIB", "dNSUnresponsive"),
        ("DATA-DOMAIN-MIB", "nISCommFailure"),
        ("DATA-DOMAIN-MIB", "iOModuleMacFault"),
        ("DATA-DOMAIN-MIB", "nTPDFailed"),
        ("DATA-DOMAIN-MIB", "nvramWarning"),
        ("DATA-DOMAIN-MIB", "nvramBatteryAlert"),
        ("DATA-DOMAIN-MIB", "nvramErrorAlert"),
        ("DATA-DOMAIN-MIB", "nvramBatteryLowChargeAlert"),
        ("DATA-DOMAIN-MIB", "ext3NvlogDisabled"),
        ("DATA-DOMAIN-MIB", "nvramHWAlert"),
        ("DATA-DOMAIN-MIB", "nvramBattAlert"),
        ("DATA-DOMAIN-MIB", "nvramEnvAlert"),
        ("DATA-DOMAIN-MIB", "nvramCondAlert"),
        ("DATA-DOMAIN-MIB", "nvramEventHWAlert"),
        ("DATA-DOMAIN-MIB", "nvramBattEndOfLife"),
        ("DATA-DOMAIN-MIB", "phyalert"),
        ("DATA-DOMAIN-MIB", "mtreeQuotaSoftLimit"),
        ("DATA-DOMAIN-MIB", "mtreeQuotaHardLimit"),
        ("DATA-DOMAIN-MIB", "storageUnitStreamSoftLimit"),
        ("DATA-DOMAIN-MIB", "replProgressThreshholdReached"),
        ("DATA-DOMAIN-MIB", "replNeedResync"),
        ("DATA-DOMAIN-MIB", "replLogFull"),
        ("DATA-DOMAIN-MIB", "replIncompatibleWorm"),
        ("DATA-DOMAIN-MIB", "replDestNotConfigured"),
        ("DATA-DOMAIN-MIB", "replLagThreshholdReached"),
        ("DATA-DOMAIN-MIB", "replPathTooLong"),
        ("DATA-DOMAIN-MIB", "missingCreplUnits"),
        ("DATA-DOMAIN-MIB", "mtreeCascadeNeedResync"),
        ("DATA-DOMAIN-MIB", "insecureEncryptedReplication"),
        ("DATA-DOMAIN-MIB", "suspendedMReplMissingUnits"),
        ("DATA-DOMAIN-MIB", "sASEnclosureCheck"),
        ("DATA-DOMAIN-MIB", "sASTopologyCheck"),
        ("DATA-DOMAIN-MIB", "sASPortDisabled"),
        ("DATA-DOMAIN-MIB", "sASHBAFailure"),
        ("DATA-DOMAIN-MIB", "sASHBAErrors"),
        ("DATA-DOMAIN-MIB", "unsupportedSASDevice"),
        ("DATA-DOMAIN-MIB", "invalidEnclosureTopology"),
        ("DATA-DOMAIN-MIB", "diskPathSpeedDegraded"),
        ("DATA-DOMAIN-MIB", "enclosureMixType"),
        ("DATA-DOMAIN-MIB", "enclosureMixDriveType"),
        ("DATA-DOMAIN-MIB", "sCSITGTInvalidRegistry"),
        ("DATA-DOMAIN-MIB", "sSLCertificateCorrupted"),
        ("DATA-DOMAIN-MIB", "unusableHostCertificate"),
        ("DATA-DOMAIN-MIB", "missingHostCertificate"),
        ("DATA-DOMAIN-MIB", "expiredHostCertificate"),
        ("DATA-DOMAIN-MIB", "sMSUnresponsive"),
        ("DATA-DOMAIN-MIB", "mailserverError"),
        ("DATA-DOMAIN-MIB", "snapshotOver90Percent"),
        ("DATA-DOMAIN-MIB", "snapshotLimitReached"),
        ("DATA-DOMAIN-MIB", "sNTZMultipleIterations"),
        ("DATA-DOMAIN-MIB", "coredumpWarning"),
        ("DATA-DOMAIN-MIB", "coredumpDisabled"),
        ("DATA-DOMAIN-MIB", "spaceOver80Percent"),
        ("DATA-DOMAIN-MIB", "spaceOver90Percent"),
        ("DATA-DOMAIN-MIB", "spaceReclRestartFailed"),
        ("DATA-DOMAIN-MIB", "spaceReclMissingUnit"),
        ("DATA-DOMAIN-MIB", "spaceReclUnitReclaimed"),
        ("DATA-DOMAIN-MIB", "spaceReclError"),
        ("DATA-DOMAIN-MIB", "spaceReclSuspended"),
        ("DATA-DOMAIN-MIB", "spaceReclUnitError"),
        ("DATA-DOMAIN-MIB", "diskAccessError"),
        ("DATA-DOMAIN-MIB", "diskFailure"),
        ("DATA-DOMAIN-MIB", "diskTemperatureWarning"),
        ("DATA-DOMAIN-MIB", "diskTemperatureShutdown"),
        ("DATA-DOMAIN-MIB", "unsupportedHardwareSpareSize"),
        ("DATA-DOMAIN-MIB", "missingDiskGroup"),
        ("DATA-DOMAIN-MIB", "diskGroupReconstructionNoProgress"),
        ("DATA-DOMAIN-MIB", "diskGroupReconstruction"),
        ("DATA-DOMAIN-MIB", "diskGroupReconstructionShutdown"),
        ("DATA-DOMAIN-MIB", "diskGroupReconstructionCritical"),
        ("DATA-DOMAIN-MIB", "diskUnknown"),
        ("DATA-DOMAIN-MIB", "lowSpares"),
        ("DATA-DOMAIN-MIB", "unsupportedConfigurationROL"),
        ("DATA-DOMAIN-MIB", "foreignEnclosure"),
        ("DATA-DOMAIN-MIB", "sSDEndOfLife"),
        ("DATA-DOMAIN-MIB", "multipleDiskReadErrors"),
        ("DATA-DOMAIN-MIB", "unsupportedDriveModel"),
        ("DATA-DOMAIN-MIB", "driveMixType"),
        ("DATA-DOMAIN-MIB", "missingTierStorage"),
        ("DATA-DOMAIN-MIB", "storageMigrationCopyComplete"),
        ("DATA-DOMAIN-MIB", "storageMigrationCannotResume"),
        ("DATA-DOMAIN-MIB", "storageMigrationUserSuspend"),
        ("DATA-DOMAIN-MIB", "foreignPack"),
        ("DATA-DOMAIN-MIB", "upgradeFailure"),
        ("DATA-DOMAIN-MIB", "upgradeCompleted"),
        ("DATA-DOMAIN-MIB", "upgradeInProgress"),
        ("DATA-DOMAIN-MIB", "vDiskSCSITargetMismatch"),
        ("DATA-DOMAIN-MIB", "tapeReposition"),
        ("DATA-DOMAIN-MIB", "duplicateVTLPoolNames"))
)
if mibBuilder.loadTexts:
    generatedNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

dataDomainMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 19746, 0, 1, 1)
)
dataDomainMibCompliance.setObjects(
      *(("DATA-DOMAIN-MIB", "environmentalsGroup"),
        ("DATA-DOMAIN-MIB", "nvramGroup"),
        ("DATA-DOMAIN-MIB", "fileSystemGroup"),
        ("DATA-DOMAIN-MIB", "alertsGroup"),
        ("DATA-DOMAIN-MIB", "statisticsGroup"),
        ("DATA-DOMAIN-MIB", "replGroup"),
        ("DATA-DOMAIN-MIB", "basicNotificationsGroup"),
        ("DATA-DOMAIN-MIB", "nfsGroup"),
        ("DATA-DOMAIN-MIB", "cifsGroup"),
        ("DATA-DOMAIN-MIB", "vtlGroup"),
        ("DATA-DOMAIN-MIB", "internalDiskStorageGroup"),
        ("DATA-DOMAIN-MIB", "internalDiskStorageNotificationsGroup"),
        ("DATA-DOMAIN-MIB", "externalUnmanagedDiskStorageGroup"))
)
if mibBuilder.loadTexts:
    dataDomainMibCompliance.setStatus(
        "deprecated"
    )

dataDomainMibComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 19746, 0, 1, 2)
)
dataDomainMibComplianceRev1.setObjects(
      *(("DATA-DOMAIN-MIB", "environmentalsGroup"),
        ("DATA-DOMAIN-MIB", "nvramGroup"),
        ("DATA-DOMAIN-MIB", "fileSystemGroupRev1"),
        ("DATA-DOMAIN-MIB", "alertsGroup"),
        ("DATA-DOMAIN-MIB", "statisticsGroup"),
        ("DATA-DOMAIN-MIB", "replGroup"),
        ("DATA-DOMAIN-MIB", "nfsGroup"),
        ("DATA-DOMAIN-MIB", "cifsGroup"),
        ("DATA-DOMAIN-MIB", "vtlGroup"),
        ("DATA-DOMAIN-MIB", "ddboostGroup"),
        ("DATA-DOMAIN-MIB", "ddsystemGroup"),
        ("DATA-DOMAIN-MIB", "artGroup"),
        ("DATA-DOMAIN-MIB", "mtreeGroup"),
        ("DATA-DOMAIN-MIB", "enclosureGroup"),
        ("DATA-DOMAIN-MIB", "networkGroup"),
        ("DATA-DOMAIN-MIB", "generatedNotificationsGroup"),
        ("DATA-DOMAIN-MIB", "internalDiskStorageGroup"),
        ("DATA-DOMAIN-MIB", "externalUnmanagedDiskStorageGroup"),
        ("DATA-DOMAIN-MIB", "managedObjectsGroup"))
)
if mibBuilder.loadTexts:
    dataDomainMibComplianceRev1.setStatus(
        "deprecated"
    )

dataDomainMibComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 19746, 0, 1, 3)
)
dataDomainMibComplianceRev2.setObjects(
      *(("DATA-DOMAIN-MIB", "environmentalsGroup"),
        ("DATA-DOMAIN-MIB", "nvramGroup"),
        ("DATA-DOMAIN-MIB", "fileSystemGroupRev1"),
        ("DATA-DOMAIN-MIB", "alertsGroup"),
        ("DATA-DOMAIN-MIB", "statisticsGroup"),
        ("DATA-DOMAIN-MIB", "replGroup"),
        ("DATA-DOMAIN-MIB", "nfsGroup"),
        ("DATA-DOMAIN-MIB", "cifsGroup"),
        ("DATA-DOMAIN-MIB", "vtlGroup"),
        ("DATA-DOMAIN-MIB", "ddboostGroup"),
        ("DATA-DOMAIN-MIB", "ddsystemGroupRev1"),
        ("DATA-DOMAIN-MIB", "artGroup"),
        ("DATA-DOMAIN-MIB", "mtreeGroup"),
        ("DATA-DOMAIN-MIB", "enclosureGroup"),
        ("DATA-DOMAIN-MIB", "networkGroup"),
        ("DATA-DOMAIN-MIB", "generatedNotificationsGroup"),
        ("DATA-DOMAIN-MIB", "internalDiskStorageGroup"),
        ("DATA-DOMAIN-MIB", "externalUnmanagedDiskStorageGroup"),
        ("DATA-DOMAIN-MIB", "managedObjectsGroup"))
)
if mibBuilder.loadTexts:
    dataDomainMibComplianceRev2.setStatus(
        "deprecated"
    )

dataDomainMibComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 19746, 0, 1, 4)
)
dataDomainMibComplianceRev3.setObjects(
      *(("DATA-DOMAIN-MIB", "environmentalsGroup"),
        ("DATA-DOMAIN-MIB", "nvramGroup"),
        ("DATA-DOMAIN-MIB", "fileSystemGroupRev1"),
        ("DATA-DOMAIN-MIB", "alertsGroup"),
        ("DATA-DOMAIN-MIB", "statisticsGroup"),
        ("DATA-DOMAIN-MIB", "replGroup"),
        ("DATA-DOMAIN-MIB", "nfsGroup"),
        ("DATA-DOMAIN-MIB", "cifsGroup"),
        ("DATA-DOMAIN-MIB", "vtlGroup"),
        ("DATA-DOMAIN-MIB", "ddboostGroupRev1"),
        ("DATA-DOMAIN-MIB", "ddsystemGroupRev1"),
        ("DATA-DOMAIN-MIB", "artGroup"),
        ("DATA-DOMAIN-MIB", "mtreeGroup"),
        ("DATA-DOMAIN-MIB", "enclosureGroup"),
        ("DATA-DOMAIN-MIB", "networkGroup"),
        ("DATA-DOMAIN-MIB", "generatedNotificationsGroup"),
        ("DATA-DOMAIN-MIB", "smtGroup"),
        ("DATA-DOMAIN-MIB", "quotaGroup"),
        ("DATA-DOMAIN-MIB", "internalDiskStorageGroup"),
        ("DATA-DOMAIN-MIB", "externalUnmanagedDiskStorageGroup"),
        ("DATA-DOMAIN-MIB", "managedObjectsGroup"))
)
if mibBuilder.loadTexts:
    dataDomainMibComplianceRev3.setStatus(
        "deprecated"
    )

dataDomainMibComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 19746, 0, 1, 5)
)
dataDomainMibComplianceRev4.setObjects(
      *(("DATA-DOMAIN-MIB", "environmentalsGroup"),
        ("DATA-DOMAIN-MIB", "nvramGroup"),
        ("DATA-DOMAIN-MIB", "fileSystemGroupRev1"),
        ("DATA-DOMAIN-MIB", "alertsGroup"),
        ("DATA-DOMAIN-MIB", "statisticsGroup"),
        ("DATA-DOMAIN-MIB", "replGroup"),
        ("DATA-DOMAIN-MIB", "nfsGroup"),
        ("DATA-DOMAIN-MIB", "cifsGroup"),
        ("DATA-DOMAIN-MIB", "vtlGroup"),
        ("DATA-DOMAIN-MIB", "ddboostGroupRev2"),
        ("DATA-DOMAIN-MIB", "ddsystemGroupRev1"),
        ("DATA-DOMAIN-MIB", "artGroup"),
        ("DATA-DOMAIN-MIB", "mtreeGroup"),
        ("DATA-DOMAIN-MIB", "enclosureGroup"),
        ("DATA-DOMAIN-MIB", "networkGroup"),
        ("DATA-DOMAIN-MIB", "generatedNotificationsGroup"),
        ("DATA-DOMAIN-MIB", "smtGroup"),
        ("DATA-DOMAIN-MIB", "quotaGroup"),
        ("DATA-DOMAIN-MIB", "highAvailabilityGroup"),
        ("DATA-DOMAIN-MIB", "scsitargetObjectGroup"),
        ("DATA-DOMAIN-MIB", "internalDiskStorageGroup"),
        ("DATA-DOMAIN-MIB", "externalUnmanagedDiskStorageGroup"),
        ("DATA-DOMAIN-MIB", "managedObjectsGroup"))
)
if mibBuilder.loadTexts:
    dataDomainMibComplianceRev4.setStatus(
        "deprecated"
    )

dataDomainMibComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 19746, 0, 1, 6)
)
dataDomainMibComplianceRev5.setObjects(
      *(("DATA-DOMAIN-MIB", "environmentalsGroup"),
        ("DATA-DOMAIN-MIB", "nvramGroup"),
        ("DATA-DOMAIN-MIB", "fileSystemGroupRev1"),
        ("DATA-DOMAIN-MIB", "alertsGroup"),
        ("DATA-DOMAIN-MIB", "statisticsGroup"),
        ("DATA-DOMAIN-MIB", "replGroup"),
        ("DATA-DOMAIN-MIB", "nfsGroup"),
        ("DATA-DOMAIN-MIB", "cifsGroupRev1"),
        ("DATA-DOMAIN-MIB", "vtlGroup"),
        ("DATA-DOMAIN-MIB", "ddboostGroupRev2"),
        ("DATA-DOMAIN-MIB", "ddsystemGroupRev1"),
        ("DATA-DOMAIN-MIB", "artGroup"),
        ("DATA-DOMAIN-MIB", "mtreeGroup"),
        ("DATA-DOMAIN-MIB", "enclosureGroup"),
        ("DATA-DOMAIN-MIB", "networkGroup"),
        ("DATA-DOMAIN-MIB", "generatedNotificationsGroup"),
        ("DATA-DOMAIN-MIB", "smtGroup"),
        ("DATA-DOMAIN-MIB", "quotaGroup"),
        ("DATA-DOMAIN-MIB", "highAvailabilityGroup"),
        ("DATA-DOMAIN-MIB", "scsitargetObjectGroup"),
        ("DATA-DOMAIN-MIB", "internalDiskStorageGroup"),
        ("DATA-DOMAIN-MIB", "externalUnmanagedDiskStorageGroup"),
        ("DATA-DOMAIN-MIB", "managedObjectsGroup"))
)
if mibBuilder.loadTexts:
    dataDomainMibComplianceRev5.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DATA-DOMAIN-MIB",
    **{"EnclosureID": EnclosureID,
       "Temperature": Temperature,
       "Minutes": Minutes,
       "Percentage": Percentage,
       "PercentageStr": PercentageStr,
       "KBytesPerSecond": KBytesPerSecond,
       "OpsPerSecond": OpsPerSecond,
       "ErrorCount": ErrorCount,
       "DDMibTableIndexTC": DDMibTableIndexTC,
       "DDMibTableString32TC": DDMibTableString32TC,
       "DDMibTableString64TC": DDMibTableString64TC,
       "DDMibTableString128TC": DDMibTableString128TC,
       "DDMibTableString256TC": DDMibTableString256TC,
       "DDMibTableString512TC": DDMibTableString512TC,
       "DDMibTableString1024TC": DDMibTableString1024TC,
       "DDMibString96TC": DDMibString96TC,
       "DDMibTableSizeGibTC": DDMibTableSizeGibTC,
       "DDMibTableSizeMiBTC": DDMibTableSizeMiBTC,
       "DDMibDateTC": DDMibDateTC,
       "DDMibMemorySizeTC": DDMibMemorySizeTC,
       "DDMibTimeStampTC": DDMibTimeStampTC,
       "DDMibVersionTC": DDMibVersionTC,
       "DDMibTableEnabledTC": DDMibTableEnabledTC,
       "DDMibInteger32TC": DDMibInteger32TC,
       "DDMibCompressionFactorTC": DDMibCompressionFactorTC,
       "DDMibAlertSeverityTC": DDMibAlertSeverityTC,
       "DDMibTrafficBytesTC": DDMibTrafficBytesTC,
       "DDMibStatusTC": DDMibStatusTC,
       "PowerModuleIndexTC": PowerModuleIndexTC,
       "PowerModuleDescriptionTC": PowerModuleDescriptionTC,
       "PowerModuleStatusTC": PowerModuleStatusTC,
       "TempSensorIndexTC": TempSensorIndexTC,
       "TempSensorDescriptionTC": TempSensorDescriptionTC,
       "TempSensorStatusTC": TempSensorStatusTC,
       "FanIndexTC": FanIndexTC,
       "FanDescriptionTC": FanDescriptionTC,
       "FanLevelTC": FanLevelTC,
       "FanStatusTC": FanStatusTC,
       "NvramIndexTC": NvramIndexTC,
       "NvramMemorySizeTC": NvramMemorySizeTC,
       "NvramHCPropertyBytesTC": NvramHCPropertyBytesTC,
       "NvramWindowSizeTC": NvramWindowSizeTC,
       "NvramBatteryIndexTC": NvramBatteryIndexTC,
       "NvramBatteryStatusTC": NvramBatteryStatusTC,
       "DiskIndexTC": DiskIndexTC,
       "DiskModelTC": DiskModelTC,
       "DiskFirmwareVersionTC": DiskFirmwareVersionTC,
       "DiskSerialNumberTC": DiskSerialNumberTC,
       "DiskCapacityTC": DiskCapacityTC,
       "DiskStateTC": DiskStateTC,
       "DiskPackTC": DiskPackTC,
       "DiskSectorsPerSecondTC": DiskSectorsPerSecondTC,
       "FileSystemStatusTC": FileSystemStatusTC,
       "FileSystemResourceIndexTC": FileSystemResourceIndexTC,
       "FileSystemResourceNameTC": FileSystemResourceNameTC,
       "FileSystemSpaceUnitTC": FileSystemSpaceUnitTC,
       "FileSystemCompressionSizeTC": FileSystemCompressionSizeTC,
       "FileSystemCompressionFactorTC": FileSystemCompressionFactorTC,
       "FileSystemCompressionPeriodTC": FileSystemCompressionPeriodTC,
       "DateTC": DateTC,
       "FileSystemOptionsIndexTC": FileSystemOptionsIndexTC,
       "FileSystemOptionsNameTC": FileSystemOptionsNameTC,
       "FileSystemOptionsValueTC": FileSystemOptionsValueTC,
       "FileSystemCleanIndexTC": FileSystemCleanIndexTC,
       "FileSystemCleanStatusTC": FileSystemCleanStatusTC,
       "FileSystemCleanScheduleTC": FileSystemCleanScheduleTC,
       "FileSystemCleanThrottleTC": FileSystemCleanThrottleTC,
       "AlertIndexTC": AlertIndexTC,
       "AlertTimestampTC": AlertTimestampTC,
       "AlertDescriptionTC": AlertDescriptionTC,
       "SystemStatsIndexTC": SystemStatsIndexTC,
       "RaidDiskStateTC": RaidDiskStateTC,
       "ReplicationStateTC": ReplicationStateTC,
       "ReplicationStatusTC": ReplicationStatusTC,
       "ReplicationConnectTimeTC": ReplicationConnectTimeTC,
       "ReplicationPathTC": ReplicationPathTC,
       "ReplicationTrafficTC": ReplicationTrafficTC,
       "ReplicationThrottleTC": ReplicationThrottleTC,
       "ReplicationSyncedTimeTC": ReplicationSyncedTimeTC,
       "ReplicationContextTC": ReplicationContextTC,
       "ReplicationConfigIndexTC": ReplicationConfigIndexTC,
       "ReplicationConfigContextIdTC": ReplicationConfigContextIdTC,
       "ReplicationConfigSourceTC": ReplicationConfigSourceTC,
       "ReplicationConfigDestTC": ReplicationConfigDestTC,
       "ReplicationConfigConnHostTC": ReplicationConfigConnHostTC,
       "ReplicationConfigConnPortTC": ReplicationConfigConnPortTC,
       "ReplicationConfigLowBWOptimTC": ReplicationConfigLowBWOptimTC,
       "ReplicationConfigEnabledTC": ReplicationConfigEnabledTC,
       "NfsStatusTC": NfsStatusTC,
       "NfsClientIndexTC": NfsClientIndexTC,
       "NfsClientPathTC": NfsClientPathTC,
       "NfsClientClientsTC": NfsClientClientsTC,
       "NfsClientOptionsTC": NfsClientOptionsTC,
       "NfsStatsIndexTC": NfsStatsIndexTC,
       "NfsStatsExportPointTC": NfsStatsExportPointTC,
       "NfsStatsFilesystemTypeTC": NfsStatsFilesystemTypeTC,
       "NfsStatsCacheEntryTC": NfsStatsCacheEntryTC,
       "NfsStatsFileHandleLookupTC": NfsStatsFileHandleLookupTC,
       "NfsStatsMaxCacheSizeTC": NfsStatsMaxCacheSizeTC,
       "NfsStatsCurrentOpenStreamsTC": NfsStatsCurrentOpenStreamsTC,
       "VtlAdminStateTC": VtlAdminStateTC,
       "VtlProcessStateTC": VtlProcessStateTC,
       "VtlLibraryIndexTC": VtlLibraryIndexTC,
       "VtlLibraryNameTC": VtlLibraryNameTC,
       "VtlLibraryVendorTC": VtlLibraryVendorTC,
       "VtlLibraryModelTC": VtlLibraryModelTC,
       "VtlLibraryRevisionTC": VtlLibraryRevisionTC,
       "VtlLibrarySerialTC": VtlLibrarySerialTC,
       "VtlLibraryTotalDrivesTC": VtlLibraryTotalDrivesTC,
       "VtlLibraryTotalSlotsTC": VtlLibraryTotalSlotsTC,
       "VtlLibraryTotalCapsTC": VtlLibraryTotalCapsTC,
       "VtlLibraryStatusTC": VtlLibraryStatusTC,
       "VtlDriveIndexTC": VtlDriveIndexTC,
       "VtlDriveNameTC": VtlDriveNameTC,
       "VtlDriveVendorTC": VtlDriveVendorTC,
       "VtlDriveModelTC": VtlDriveModelTC,
       "VtlDriveRevisionTC": VtlDriveRevisionTC,
       "VtlDriveSerialTC": VtlDriveSerialTC,
       "VtlDriveStatusTC": VtlDriveStatusTC,
       "VtlDriveTapeVolumeTC": VtlDriveTapeVolumeTC,
       "VtlPortIndexTC": VtlPortIndexTC,
       "VtlPortNameTC": VtlPortNameTC,
       "VtlPortIDTC": VtlPortIDTC,
       "VtlPortModelTC": VtlPortModelTC,
       "VtlPortFirmwareTC": VtlPortFirmwareTC,
       "VtlPortWWNNTC": VtlPortWWNNTC,
       "VtlPortWWPNTC": VtlPortWWPNTC,
       "VtlPortConnectionTypeTC": VtlPortConnectionTypeTC,
       "VtlPortSpeedTC": VtlPortSpeedTC,
       "VtlPortEnabledTC": VtlPortEnabledTC,
       "VtlPortStatusTC": VtlPortStatusTC,
       "VtlTapeIndexTC": VtlTapeIndexTC,
       "VtlTapeBarCodeTC": VtlTapeBarCodeTC,
       "VtlTapePoolTC": VtlTapePoolTC,
       "VtlTapeLocationTC": VtlTapeLocationTC,
       "VtlTapeStateTC": VtlTapeStateTC,
       "VtlTapeSizeTC": VtlTapeSizeTC,
       "VtlTapeUsedTC": VtlTapeUsedTC,
       "VtlTapeCompTC": VtlTapeCompTC,
       "VtlTapeModTimeTC": VtlTapeModTimeTC,
       "VtlStatsIndexTC": VtlStatsIndexTC,
       "VtlStatsPortTC": VtlStatsPortTC,
       "VtlStatsConrolCommandsTC": VtlStatsConrolCommandsTC,
       "VtlStatsWriteCommandsTC": VtlStatsWriteCommandsTC,
       "VtlStatsReadCommandsTC": VtlStatsReadCommandsTC,
       "VtlStatsInTC": VtlStatsInTC,
       "VtlStatsOutTC": VtlStatsOutTC,
       "VtlStatsLinkFailuresTC": VtlStatsLinkFailuresTC,
       "VtlStatsLIPCountTC": VtlStatsLIPCountTC,
       "VtlStatsSyncLossesTC": VtlStatsSyncLossesTC,
       "VtlStatsSignalLossesTC": VtlStatsSignalLossesTC,
       "VtlStatsPrimSeqProtoErrorsTC": VtlStatsPrimSeqProtoErrorsTC,
       "VtlStatsInvalidTxWordsTC": VtlStatsInvalidTxWordsTC,
       "VtlStatsInvalidCRCsTC": VtlStatsInvalidCRCsTC,
       "CifsStatusTC": CifsStatusTC,
       "CifsConfigModeTC": CifsConfigModeTC,
       "CifsConfigWINSServerTC": CifsConfigWINSServerTC,
       "CifsConfigNetBIOSHostnameTC": CifsConfigNetBIOSHostnameTC,
       "CifsConfigDomainControllerTC": CifsConfigDomainControllerTC,
       "CifsConfigDNSTC": CifsConfigDNSTC,
       "CifsConfigGroupNameTC": CifsConfigGroupNameTC,
       "CifsConfigMaxConnectionTC": CifsConfigMaxConnectionTC,
       "CifsConfigMaxOpenFilesPerConnectionTC": CifsConfigMaxOpenFilesPerConnectionTC,
       "CifsShareIndexTC": CifsShareIndexTC,
       "CifsShareNameTC": CifsShareNameTC,
       "CifsSharePathTC": CifsSharePathTC,
       "CifsShareMaxConnectionTC": CifsShareMaxConnectionTC,
       "CifsShareClientsTC": CifsShareClientsTC,
       "CifsShareBrowsingTC": CifsShareBrowsingTC,
       "CifsShareWriteableTC": CifsShareWriteableTC,
       "CifsShareUserTC": CifsShareUserTC,
       "CifsShareCommentTC": CifsShareCommentTC,
       "CifsStatsSummaryIndexTC": CifsStatsSummaryIndexTC,
       "CifsStatsDetailsIndexTC": CifsStatsDetailsIndexTC,
       "CifsOptionsIndexTC": CifsOptionsIndexTC,
       "CifsOptionsNameTC": CifsOptionsNameTC,
       "CifsOptionsValueTC": CifsOptionsValueTC,
       "DDboostStatsIndexTC": DDboostStatsIndexTC,
       "DDboostStatusTC": DDboostStatusTC,
       "DDboostUserTC": DDboostUserTC,
       "SystemSerialNumberTC": SystemSerialNumberTC,
       "SystemTimeZoneNameTC": SystemTimeZoneNameTC,
       "SystemNotesTC": SystemNotesTC,
       "FileSystemArchiveUnitStateTC": FileSystemArchiveUnitStateTC,
       "FileSystemArchiveUnitStatusTC": FileSystemArchiveUnitStatusTC,
       "MtreeListStatusTC": MtreeListStatusTC,
       "MtreeRetentionLockStatusTC": MtreeRetentionLockStatusTC,
       "TenantUnitMgmtUserListUserRoleTC": TenantUnitMgmtUserListUserRoleTC,
       "TenantUnitMgmtGroupTypeTC": TenantUnitMgmtGroupTypeTC,
       "SmtStatusTC": SmtStatusTC,
       "TenantUnitSecurityModeTC": TenantUnitSecurityModeTC,
       "DDStatusTC": DDStatusTC,
       "DdboostAccessClientsEncryStrengthTC": DdboostAccessClientsEncryStrengthTC,
       "DdboostAccessClientsAuthModeTC": DdboostAccessClientsAuthModeTC,
       "dataDomainMib": dataDomainMib,
       "dataDomainMibConformance": dataDomainMibConformance,
       "dataDomainMibCompliances": dataDomainMibCompliances,
       "dataDomainMibCompliance": dataDomainMibCompliance,
       "dataDomainMibComplianceRev1": dataDomainMibComplianceRev1,
       "dataDomainMibComplianceRev2": dataDomainMibComplianceRev2,
       "dataDomainMibComplianceRev3": dataDomainMibComplianceRev3,
       "dataDomainMibComplianceRev4": dataDomainMibComplianceRev4,
       "dataDomainMibComplianceRev5": dataDomainMibComplianceRev5,
       "dataDomainMibGroups": dataDomainMibGroups,
       "environmentalsGroup": environmentalsGroup,
       "nvramGroup": nvramGroup,
       "fileSystemGroup": fileSystemGroup,
       "alertsGroup": alertsGroup,
       "statisticsGroup": statisticsGroup,
       "internalDiskStorageGroup": internalDiskStorageGroup,
       "externalUnmanagedDiskStorageGroup": externalUnmanagedDiskStorageGroup,
       "basicNotificationsGroup": basicNotificationsGroup,
       "internalDiskStorageNotificationsGroup": internalDiskStorageNotificationsGroup,
       "replGroup": replGroup,
       "nfsGroup": nfsGroup,
       "cifsGroup": cifsGroup,
       "vtlGroup": vtlGroup,
       "ddboostGroup": ddboostGroup,
       "ddsystemGroup": ddsystemGroup,
       "artGroup": artGroup,
       "mtreeGroup": mtreeGroup,
       "enclosureGroup": enclosureGroup,
       "managedObjectsGroup": managedObjectsGroup,
       "networkGroup": networkGroup,
       "fileSystemGroupRev1": fileSystemGroupRev1,
       "ddsystemGroupRev1": ddsystemGroupRev1,
       "smtGroup": smtGroup,
       "quotaGroup": quotaGroup,
       "ddboostGroupRev1": ddboostGroupRev1,
       "ddboostGroupRev2": ddboostGroupRev2,
       "highAvailabilityGroup": highAvailabilityGroup,
       "scsitargetObjectGroup": scsitargetObjectGroup,
       "cifsGroupRev1": cifsGroupRev1,
       "generatedNotificationsGroup": generatedNotificationsGroup,
       "dataDomainMibObjects": dataDomainMibObjects,
       "environmentals": environmentals,
       "power": power,
       "powerModules": powerModules,
       "powerModuleTable": powerModuleTable,
       "powerModuleEntry": powerModuleEntry,
       "powerEnclosureID": powerEnclosureID,
       "powerModuleIndex": powerModuleIndex,
       "powerModuleDescription": powerModuleDescription,
       "powerModuleStatus": powerModuleStatus,
       "temperatures": temperatures,
       "temperatureSensors": temperatureSensors,
       "temperatureSensorTable": temperatureSensorTable,
       "temperatureSensorEntry": temperatureSensorEntry,
       "tempEnclosureID": tempEnclosureID,
       "tempSensorIndex": tempSensorIndex,
       "tempSensorTrapIndex": tempSensorTrapIndex,
       "tempSensorDescription": tempSensorDescription,
       "tempSensorCurrentValue": tempSensorCurrentValue,
       "tempSensorStatus": tempSensorStatus,
       "fans": fans,
       "fanProperties": fanProperties,
       "fanPropertiesTable": fanPropertiesTable,
       "fanPropertiesEntry": fanPropertiesEntry,
       "fanEnclosureID": fanEnclosureID,
       "fanIndex": fanIndex,
       "fanTrapIndex": fanTrapIndex,
       "fanDescription": fanDescription,
       "fanLevel": fanLevel,
       "fanStatus": fanStatus,
       "nvram": nvram,
       "nvramProperties": nvramProperties,
       "nvramPropertiesTable": nvramPropertiesTable,
       "nvramPropertiesEntry": nvramPropertiesEntry,
       "nvramPropertiesIndex": nvramPropertiesIndex,
       "nvramMemorySize": nvramMemorySize,
       "nvramWindowSize": nvramWindowSize,
       "nvramHCMemorySize": nvramHCMemorySize,
       "nvramStats": nvramStats,
       "nvramStatsTable": nvramStatsTable,
       "nvramStatsEntry": nvramStatsEntry,
       "nvramStatsIndex": nvramStatsIndex,
       "nvramPCIErrorCount": nvramPCIErrorCount,
       "nvramMemoryErrorCount": nvramMemoryErrorCount,
       "nvramBatteries": nvramBatteries,
       "nvramBatteryTable": nvramBatteryTable,
       "nvramBatteryEntry": nvramBatteryEntry,
       "nvramBatteriesIndex": nvramBatteriesIndex,
       "nvramBatteryIndex": nvramBatteryIndex,
       "nvramBatteryStatus": nvramBatteryStatus,
       "nvramBatteryCharge": nvramBatteryCharge,
       "fileSystem": fileSystem,
       "fileSystemProperties": fileSystemProperties,
       "fileSystemStatus": fileSystemStatus,
       "fileSystemVirtualSpace": fileSystemVirtualSpace,
       "fileSystemUpTime": fileSystemUpTime,
       "fileSystemStatusMessage": fileSystemStatusMessage,
       "fileSystemSpace": fileSystemSpace,
       "fileSystemSpaceTable": fileSystemSpaceTable,
       "fileSystemSpaceEntry": fileSystemSpaceEntry,
       "fileSystemResourceIndex": fileSystemResourceIndex,
       "fileSystemResourceTrapIndex": fileSystemResourceTrapIndex,
       "fileSystemResourceName": fileSystemResourceName,
       "fileSystemSpaceSize": fileSystemSpaceSize,
       "fileSystemSpaceUsed": fileSystemSpaceUsed,
       "fileSystemSpaceAvail": fileSystemSpaceAvail,
       "fileSystemPercentUsed": fileSystemPercentUsed,
       "fileSystemSpaceCleanable": fileSystemSpaceCleanable,
       "fileSystemResourceTier": fileSystemResourceTier,
       "fileSystemCompression": fileSystemCompression,
       "fileSystemCompressionTable": fileSystemCompressionTable,
       "fileSystemCompressionEntry": fileSystemCompressionEntry,
       "fileSystemCompressionIndex": fileSystemCompressionIndex,
       "fileSystemCompressionPeriod": fileSystemCompressionPeriod,
       "fileSystemCompressionStartTime": fileSystemCompressionStartTime,
       "fileSystemCompressionEndTime": fileSystemCompressionEndTime,
       "fileSystemPreCompressionSize": fileSystemPreCompressionSize,
       "fileSystemPostCompressionSize": fileSystemPostCompressionSize,
       "fileSystemGlobalCompressionFactor": fileSystemGlobalCompressionFactor,
       "fileSystemLocalCompressionFactor": fileSystemLocalCompressionFactor,
       "fileSystemTotalCompressionFactor": fileSystemTotalCompressionFactor,
       "fileSystemReductionPercent": fileSystemReductionPercent,
       "fileSystemReductionPercent1": fileSystemReductionPercent1,
       "fileSystemOptions": fileSystemOptions,
       "fileSystemOptionsTable": fileSystemOptionsTable,
       "fileSystemOptionsEntry": fileSystemOptionsEntry,
       "fileSystemOptionsIndex": fileSystemOptionsIndex,
       "fileSystemOptionsName": fileSystemOptionsName,
       "fileSystemOptionsValue": fileSystemOptionsValue,
       "fileSystemClean": fileSystemClean,
       "fileSystemCleanTable": fileSystemCleanTable,
       "fileSystemCleanEntry": fileSystemCleanEntry,
       "fileSystemCleanIndex": fileSystemCleanIndex,
       "fileSystemCleanStatus": fileSystemCleanStatus,
       "fileSystemCleanSchedule": fileSystemCleanSchedule,
       "fileSystemCleanThrottle": fileSystemCleanThrottle,
       "fileSystemArchiveUnit": fileSystemArchiveUnit,
       "fileSystemArchiveUnitTable": fileSystemArchiveUnitTable,
       "fileSystemArchiveUnitEntry": fileSystemArchiveUnitEntry,
       "fileSystemArchiveUnitIndex": fileSystemArchiveUnitIndex,
       "fileSystemArchiveUnitName": fileSystemArchiveUnitName,
       "fileSystemArchiveUnitState": fileSystemArchiveUnitState,
       "fileSystemArchiveUnitStatus": fileSystemArchiveUnitStatus,
       "fileSystemArchiveUnitStartTime": fileSystemArchiveUnitStartTime,
       "fileSystemArchiveUnitEndTime": fileSystemArchiveUnitEndTime,
       "fileSystemArchiveUnitSize": fileSystemArchiveUnitSize,
       "fileSystemArchiveUnitDiskGroups": fileSystemArchiveUnitDiskGroups,
       "alerts": alerts,
       "currentAlerts": currentAlerts,
       "currentAlertTable": currentAlertTable,
       "currentAlertEntry": currentAlertEntry,
       "currentAlertIndex": currentAlertIndex,
       "currentAlertTimestamp": currentAlertTimestamp,
       "currentAlertDescription": currentAlertDescription,
       "currentAlertSeverity": currentAlertSeverity,
       "currentAlertID": currentAlertID,
       "alertHistory": alertHistory,
       "alertHistoryTable": alertHistoryTable,
       "alertHistoryEntry": alertHistoryEntry,
       "alertHistoryIndex": alertHistoryIndex,
       "alertHistoryTimestamp": alertHistoryTimestamp,
       "alertHistoryDescription": alertHistoryDescription,
       "alertHistorySeverity": alertHistorySeverity,
       "alertHistoryStatus": alertHistoryStatus,
       "alertInfo": alertInfo,
       "alertInfoTable": alertInfoTable,
       "alertInfoEntry": alertInfoEntry,
       "alertInfoIndex": alertInfoIndex,
       "alertInfoDescription": alertInfoDescription,
       "statistics": statistics,
       "systemStats": systemStats,
       "systemStatsTable": systemStatsTable,
       "systemStatsEntry": systemStatsEntry,
       "systemStatsIndex": systemStatsIndex,
       "cpuAvgPercentageBusy": cpuAvgPercentageBusy,
       "cpuMaxPercentageBusy": cpuMaxPercentageBusy,
       "nfsOpsPerSecond": nfsOpsPerSecond,
       "nfsIdlePercentage": nfsIdlePercentage,
       "nfsProcPercentage": nfsProcPercentage,
       "nfsSendPercentage": nfsSendPercentage,
       "nfsReceivePercentage": nfsReceivePercentage,
       "cifsOpsPerSecond": cifsOpsPerSecond,
       "diskReadKBytesPerSecond": diskReadKBytesPerSecond,
       "diskWriteKBytesPerSecond": diskWriteKBytesPerSecond,
       "diskBusyPercentage": diskBusyPercentage,
       "nvramReadKBytesPerSecond": nvramReadKBytesPerSecond,
       "nvramWriteKBytesPerSecond": nvramWriteKBytesPerSecond,
       "replInKBytesPerSecond": replInKBytesPerSecond,
       "replOutKBytesPerSecond": replOutKBytesPerSecond,
       "diskStorage": diskStorage,
       "diskProperties": diskProperties,
       "diskPropertiesTable": diskPropertiesTable,
       "diskPropertiesEntry": diskPropertiesEntry,
       "diskPropEnclosureID": diskPropEnclosureID,
       "diskPropIndex": diskPropIndex,
       "diskPropTrapIndex": diskPropTrapIndex,
       "diskModel": diskModel,
       "diskFirmwareVersion": diskFirmwareVersion,
       "diskSerialNumber": diskSerialNumber,
       "diskCapacity": diskCapacity,
       "diskPropState": diskPropState,
       "diskPack": diskPack,
       "diskPerformance": diskPerformance,
       "diskPerformanceTable": diskPerformanceTable,
       "diskPerformanceEntry": diskPerformanceEntry,
       "diskPerfEnclosureID": diskPerfEnclosureID,
       "diskPerfIndex": diskPerfIndex,
       "diskSectorsRead": diskSectorsRead,
       "diskSectorsWritten": diskSectorsWritten,
       "diskTotalKBytes": diskTotalKBytes,
       "diskBusy": diskBusy,
       "diskPerfState": diskPerfState,
       "diskReliability": diskReliability,
       "diskReliabilityTable": diskReliabilityTable,
       "diskReliabilityEntry": diskReliabilityEntry,
       "diskErrEnclosureID": diskErrEnclosureID,
       "diskErrIndex": diskErrIndex,
       "diskErrTrapIndex": diskErrTrapIndex,
       "diskTemperature": diskTemperature,
       "diskTimeoutCount": diskTimeoutCount,
       "diskReadFailCount": diskReadFailCount,
       "diskWriteFailCount": diskWriteFailCount,
       "diskMiscFailCount": diskMiscFailCount,
       "diskOffTrackErrCount": diskOffTrackErrCount,
       "diskSoftEccCount": diskSoftEccCount,
       "diskCrcErrCount": diskCrcErrCount,
       "diskProbationalCount": diskProbationalCount,
       "diskReallocCount": diskReallocCount,
       "diskErrState": diskErrState,
       "replication": replication,
       "replicationInfo": replicationInfo,
       "replicationInfoTable": replicationInfoTable,
       "replicationInfoEntry": replicationInfoEntry,
       "replContext": replContext,
       "replTrapContext": replTrapContext,
       "replState": replState,
       "replStatus": replStatus,
       "replFileSysStatus": replFileSysStatus,
       "replConnTime": replConnTime,
       "replSource": replSource,
       "replDestination": replDestination,
       "replPreCompBytesSent": replPreCompBytesSent,
       "replPostCompBytesSent": replPostCompBytesSent,
       "replPreCompBytesRemaining": replPreCompBytesRemaining,
       "replPostCompBytesReceived": replPostCompBytesReceived,
       "replThrottle": replThrottle,
       "replSyncedAsOfTime": replSyncedAsOfTime,
       "replicationConfig": replicationConfig,
       "replicationConfigTable": replicationConfigTable,
       "replicationConfigEntry": replicationConfigEntry,
       "replConfigIndex": replConfigIndex,
       "replConfigContextId": replConfigContextId,
       "replConfigSource": replConfigSource,
       "replConfigDest": replConfigDest,
       "replConfigConnHost": replConfigConnHost,
       "replConfigConnPort": replConfigConnPort,
       "replConfigLowBWOptim": replConfigLowBWOptim,
       "replConfigEnabled": replConfigEnabled,
       "replConfigTenantUnit": replConfigTenantUnit,
       "replicationHistory": replicationHistory,
       "replicationHistoryTable": replicationHistoryTable,
       "replicationHistoryEntry": replicationHistoryEntry,
       "replHistoryContext": replHistoryContext,
       "replHistoryDate": replHistoryDate,
       "replHistoryTime": replHistoryTime,
       "replHistoryPreCompWritten": replHistoryPreCompWritten,
       "replHistoryPreCompRemaining": replHistoryPreCompRemaining,
       "replHistoryPreCompressed": replHistoryPreCompressed,
       "replHistoryPostFiltered": replHistoryPostFiltered,
       "replHistoryPostLowBwOptim": replHistoryPostLowBwOptim,
       "replHistoryPostLocalComp": replHistoryPostLocalComp,
       "replHistoryBytesNetwork": replHistoryBytesNetwork,
       "replHistorySyncedAsOfTime": replHistorySyncedAsOfTime,
       "replicationPerformance": replicationPerformance,
       "replicationPerformanceTable": replicationPerformanceTable,
       "replicationPerformanceEntry": replicationPerformanceEntry,
       "replPerformancePreCompKBPerSec": replPerformancePreCompKBPerSec,
       "replPerformanceNetworkKBPerSec": replPerformanceNetworkKBPerSec,
       "replPerformanceStreams": replPerformanceStreams,
       "replPerformanceBusyReading": replPerformanceBusyReading,
       "replPerformanceBusyMeta": replPerformanceBusyMeta,
       "replPerformanceWaitingDest": replPerformanceWaitingDest,
       "replPerformanceWaitingNetwork": replPerformanceWaitingNetwork,
       "nfs": nfs,
       "nfsProperties": nfsProperties,
       "nfsStatus": nfsStatus,
       "nfsClient": nfsClient,
       "nfsClientTable": nfsClientTable,
       "nfsClientEntry": nfsClientEntry,
       "nfsClientIndex": nfsClientIndex,
       "nfsClientPath": nfsClientPath,
       "nfsClientClients": nfsClientClients,
       "nfsClientOptions": nfsClientOptions,
       "nfsStats": nfsStats,
       "nfsStatsTable": nfsStatsTable,
       "nfsStatsEntry": nfsStatsEntry,
       "nfsStatsIndex": nfsStatsIndex,
       "nfsStatsExportPoint": nfsStatsExportPoint,
       "nfsStatsFilesystemType": nfsStatsFilesystemType,
       "nfsStatsCacheEntry": nfsStatsCacheEntry,
       "nfsStatsFileHandleLookup": nfsStatsFileHandleLookup,
       "nfsStatsMaxCacheSize": nfsStatsMaxCacheSize,
       "nfsStatsCurrentOpenStreams": nfsStatsCurrentOpenStreams,
       "nfsActive": nfsActive,
       "nfsActiveTable": nfsActiveTable,
       "nfsActiveEntry": nfsActiveEntry,
       "nfsActiveIndex": nfsActiveIndex,
       "nfsActivePath": nfsActivePath,
       "nfsActiveClients": nfsActiveClients,
       "nfsPort": nfsPort,
       "nfsPortTable": nfsPortTable,
       "nfsPortEntry": nfsPortEntry,
       "nfsPortIndex": nfsPortIndex,
       "nfsPortService": nfsPortService,
       "nfsPortPort": nfsPortPort,
       "cifs": cifs,
       "cifsProperties": cifsProperties,
       "cifsStatus": cifsStatus,
       "cifsConfig": cifsConfig,
       "cifsConfigMode": cifsConfigMode,
       "cifsConfigWINSServer": cifsConfigWINSServer,
       "cifsConfigNetBIOSHostname": cifsConfigNetBIOSHostname,
       "cifsConfigDomainController": cifsConfigDomainController,
       "cifsConfigDNS": cifsConfigDNS,
       "cifsConfigGroupName": cifsConfigGroupName,
       "cifsConfigMaxConnection": cifsConfigMaxConnection,
       "cifsConfigMaxOpenFilesPerConnection": cifsConfigMaxOpenFilesPerConnection,
       "cifsConfigMaxOpenFiles": cifsConfigMaxOpenFiles,
       "cifsShare": cifsShare,
       "cifsShareTable": cifsShareTable,
       "cifsShareEntry": cifsShareEntry,
       "cifsShareIndex": cifsShareIndex,
       "cifsShareName": cifsShareName,
       "cifsSharePath": cifsSharePath,
       "cifsShareClients": cifsShareClients,
       "cifsShareUser": cifsShareUser,
       "cifsShareComment": cifsShareComment,
       "cifsShareBrowsing": cifsShareBrowsing,
       "cifsShareWriteable": cifsShareWriteable,
       "cifsShareMaxConnection": cifsShareMaxConnection,
       "cifsOptions": cifsOptions,
       "cifsOptionsTable": cifsOptionsTable,
       "cifsOptionsEntry": cifsOptionsEntry,
       "cifsOptionsIndex": cifsOptionsIndex,
       "cifsOptionsName": cifsOptionsName,
       "cifsOptionsValue": cifsOptionsValue,
       "vtl": vtl,
       "vtlProperties": vtlProperties,
       "vtlAdminState": vtlAdminState,
       "vtlProcessState": vtlProcessState,
       "vtlConfiguration": vtlConfiguration,
       "vtlLibrary": vtlLibrary,
       "vtlLibraryTable": vtlLibraryTable,
       "vtlLibraryEntry": vtlLibraryEntry,
       "vtlLibraryIndex": vtlLibraryIndex,
       "vtlLibraryName": vtlLibraryName,
       "vtlLibraryVendor": vtlLibraryVendor,
       "vtlLibraryModel": vtlLibraryModel,
       "vtlLibraryRevision": vtlLibraryRevision,
       "vtlLibrarySerial": vtlLibrarySerial,
       "vtlLibraryTotalDrives": vtlLibraryTotalDrives,
       "vtlLibraryTotalSlots": vtlLibraryTotalSlots,
       "vtlLibraryTotalCaps": vtlLibraryTotalCaps,
       "vtlLibraryStatus": vtlLibraryStatus,
       "vtlDrive": vtlDrive,
       "vtlDriveTable": vtlDriveTable,
       "vtlDriveEntry": vtlDriveEntry,
       "vtlDriveIndex": vtlDriveIndex,
       "vtlDriveName": vtlDriveName,
       "vtlDriveVendor": vtlDriveVendor,
       "vtlDriveModel": vtlDriveModel,
       "vtlDriveRevision": vtlDriveRevision,
       "vtlDriveSerial": vtlDriveSerial,
       "vtlDriveLibraryName": vtlDriveLibraryName,
       "vtlDriveStatus": vtlDriveStatus,
       "vtlDriveTapeVolume": vtlDriveTapeVolume,
       "vtlPort": vtlPort,
       "vtlPortTable": vtlPortTable,
       "vtlPortEntry": vtlPortEntry,
       "vtlPortIndex": vtlPortIndex,
       "vtlPortName": vtlPortName,
       "vtlPortID": vtlPortID,
       "vtlPortModel": vtlPortModel,
       "vtlPortFirmware": vtlPortFirmware,
       "vtlPortWWNN": vtlPortWWNN,
       "vtlPortWWPN": vtlPortWWPN,
       "vtlPortConnectionType": vtlPortConnectionType,
       "vtlPortSpeed": vtlPortSpeed,
       "vtlPortEnabled": vtlPortEnabled,
       "vtlPortStatus": vtlPortStatus,
       "vtlPortTrapIndex": vtlPortTrapIndex,
       "vtlTape": vtlTape,
       "vtlTapeTable": vtlTapeTable,
       "vtlTapeEntry": vtlTapeEntry,
       "vtlTapeIndex": vtlTapeIndex,
       "vtlTapeBarCode": vtlTapeBarCode,
       "vtlTapePool": vtlTapePool,
       "vtlTapeLocation": vtlTapeLocation,
       "vtlTapeState": vtlTapeState,
       "vtlTapeSize": vtlTapeSize,
       "vtlTapeUsed": vtlTapeUsed,
       "vtlTapeComp": vtlTapeComp,
       "vtlTapeModTime": vtlTapeModTime,
       "vtlPool": vtlPool,
       "vtlPoolTable": vtlPoolTable,
       "vtlPoolEntry": vtlPoolEntry,
       "vtlPoolIndex": vtlPoolIndex,
       "vtlPoolPool": vtlPoolPool,
       "vtlPoolStatus": vtlPoolStatus,
       "vtlPoolTapes": vtlPoolTapes,
       "vtlPoolSize": vtlPoolSize,
       "vtlPoolUsed": vtlPoolUsed,
       "vtlPoolComp": vtlPoolComp,
       "vtlGroups": vtlGroups,
       "vtlGroupTable": vtlGroupTable,
       "vtlGroupEntry": vtlGroupEntry,
       "vtlGroupIndex": vtlGroupIndex,
       "vtlGroupName": vtlGroupName,
       "vtlGroupInitiaterCount": vtlGroupInitiaterCount,
       "vtlGroupDeviceCount": vtlGroupDeviceCount,
       "vtlGroupDeviceTable": vtlGroupDeviceTable,
       "vtlGroupDeviceEntry": vtlGroupDeviceEntry,
       "vtlGroupDeviceIndex": vtlGroupDeviceIndex,
       "vtlGroupDeviceGroupName": vtlGroupDeviceGroupName,
       "vtlGroupDeviceDeviceName": vtlGroupDeviceDeviceName,
       "vtlGroupDeviceLun": vtlGroupDeviceLun,
       "vtlGroupDevicePrimaryPorts": vtlGroupDevicePrimaryPorts,
       "vtlGroupDeviceSecondaryPorts": vtlGroupDeviceSecondaryPorts,
       "vtlGroupDeviceInUsePorts": vtlGroupDeviceInUsePorts,
       "vtlInitiator": vtlInitiator,
       "vtlInitiatorTable": vtlInitiatorTable,
       "vtlInitiatorEntry": vtlInitiatorEntry,
       "vtlInitiatorIndex": vtlInitiatorIndex,
       "vtlInitiatorName": vtlInitiatorName,
       "vtlInitiatorStatus": vtlInitiatorStatus,
       "vtlInitiatorGroup": vtlInitiatorGroup,
       "vtlInitiatorWWNN": vtlInitiatorWWNN,
       "vtlInitiatorWWPN": vtlInitiatorWWPN,
       "vtlInitiatorPort": vtlInitiatorPort,
       "vtlStats": vtlStats,
       "vtlStatsTable": vtlStatsTable,
       "vtlStatsEntry": vtlStatsEntry,
       "vtlStatsIndex": vtlStatsIndex,
       "vtlStatsPort": vtlStatsPort,
       "vtlStatsConrolCommands": vtlStatsConrolCommands,
       "vtlStatsWriteCommands": vtlStatsWriteCommands,
       "vtlStatsReadCommands": vtlStatsReadCommands,
       "vtlStatsIn": vtlStatsIn,
       "vtlStatsOut": vtlStatsOut,
       "vtlStatsLinkFailures": vtlStatsLinkFailures,
       "vtlStatsLIPCount": vtlStatsLIPCount,
       "vtlStatsSyncLosses": vtlStatsSyncLosses,
       "vtlStatsSignalLosses": vtlStatsSignalLosses,
       "vtlStatsPrimSeqProtoErrors": vtlStatsPrimSeqProtoErrors,
       "vtlStatsInvalidTxWords": vtlStatsInvalidTxWords,
       "vtlStatsInvalidCRCs": vtlStatsInvalidCRCs,
       "ddboost": ddboost,
       "ddboostProperties": ddboostProperties,
       "ddboostStatus": ddboostStatus,
       "ddboostUser": ddboostUser,
       "ddboostIfGroupStatus": ddboostIfGroupStatus,
       "ddboostUserTable": ddboostUserTable,
       "ddboostUserEntry": ddboostUserEntry,
       "ddboostUserIdx": ddboostUserIdx,
       "ddboostUserName": ddboostUserName,
       "ddboostUserDefaultTenantUnit": ddboostUserDefaultTenantUnit,
       "ddboostIfGroupTable": ddboostIfGroupTable,
       "ddboostIfGroupEntry": ddboostIfGroupEntry,
       "ddboostIfGroupIdx": ddboostIfGroupIdx,
       "ddboostIfGroupName": ddboostIfGroupName,
       "ddboostIfGroupCurrentStatus": ddboostIfGroupCurrentStatus,
       "ddboostStats": ddboostStats,
       "ddboostStatsTable": ddboostStatsTable,
       "ddboostStatsEntry": ddboostStatsEntry,
       "ddboostStatsIndex": ddboostStatsIndex,
       "ddboostPreCompKBytesPerSecond": ddboostPreCompKBytesPerSecond,
       "ddboostPostCompKBytesPerSecond": ddboostPostCompKBytesPerSecond,
       "ddboostNetworkKBytesPerSecond": ddboostNetworkKBytesPerSecond,
       "ddboostReadKBytesPerSecond": ddboostReadKBytesPerSecond,
       "ddboostStatsBackupConn": ddboostStatsBackupConn,
       "ddboostStatsRestoreConn": ddboostStatsRestoreConn,
       "ddboostStatsImageCreatesCount": ddboostStatsImageCreatesCount,
       "ddboostStatsImageCreatesErrors": ddboostStatsImageCreatesErrors,
       "ddboostStatsImageDeletesCount": ddboostStatsImageDeletesCount,
       "ddboostStatsImageDeletesErrors": ddboostStatsImageDeletesErrors,
       "ddboostStatsPrecompBytesReceived": ddboostStatsPrecompBytesReceived,
       "ddboostStatsBytesAfterFiltering": ddboostStatsBytesAfterFiltering,
       "ddboostStatsBytesAfterLc": ddboostStatsBytesAfterLc,
       "ddboostStatsNetworkBytesReceived": ddboostStatsNetworkBytesReceived,
       "ddboostStatsCompressionRatio": ddboostStatsCompressionRatio,
       "ddboostStatsTotalBytesReadCount": ddboostStatsTotalBytesReadCount,
       "ddboostStatsTotalBytesReadErrors": ddboostStatsTotalBytesReadErrors,
       "ddboostConnections": ddboostConnections,
       "ddboostConnectionsTable": ddboostConnectionsTable,
       "ddboostConnectionsEntry": ddboostConnectionsEntry,
       "ddboostConnectionsIndex": ddboostConnectionsIndex,
       "ddboostInterface": ddboostInterface,
       "ddboostifGroupMember": ddboostifGroupMember,
       "ddboostBackupConnections": ddboostBackupConnections,
       "ddboostRestoreConnections": ddboostRestoreConnections,
       "ddboostControlConnections": ddboostControlConnections,
       "ddboostTotalConnections": ddboostTotalConnections,
       "ddboostStorageUnit": ddboostStorageUnit,
       "ddboostStorageUnitTable": ddboostStorageUnitTable,
       "ddboostStorageUnitEntry": ddboostStorageUnitEntry,
       "ddboostStorageUnitIndex": ddboostStorageUnitIndex,
       "ddboostStorageUnitName": ddboostStorageUnitName,
       "ddboostStorageUnitBytes": ddboostStorageUnitBytes,
       "ddboostStorageUnitGlobalComp": ddboostStorageUnitGlobalComp,
       "ddboostStorageUnitLocalComp": ddboostStorageUnitLocalComp,
       "ddboostStorageUnitMetaData": ddboostStorageUnitMetaData,
       "ddboostStorageUnitStatus": ddboostStorageUnitStatus,
       "ddboostStorageUnitPreComp": ddboostStorageUnitPreComp,
       "ddboostStorageUnitUser": ddboostStorageUnitUser,
       "ddboostStorageUnitReportPhysicalSize": ddboostStorageUnitReportPhysicalSize,
       "ddboostFileReplicationStats": ddboostFileReplicationStats,
       "ddboostFileReplicationStatsTable": ddboostFileReplicationStatsTable,
       "ddboostFileReplicationStatsEntry": ddboostFileReplicationStatsEntry,
       "ddboostFileReplStatsIndex": ddboostFileReplStatsIndex,
       "ddboostFileReplStatsDirection": ddboostFileReplStatsDirection,
       "ddboostFileReplStatsNetworkSent": ddboostFileReplStatsNetworkSent,
       "ddboostFileReplStatsPreCompSent": ddboostFileReplStatsPreCompSent,
       "ddboostFileReplStatsFiltered": ddboostFileReplStatsFiltered,
       "ddboostFileReplStatsLowBWOpt": ddboostFileReplStatsLowBWOpt,
       "ddboostFileReplStatsLocalComp": ddboostFileReplStatsLocalComp,
       "ddboostFileReplStatsCompRatio": ddboostFileReplStatsCompRatio,
       "ddboostFileReplicationHistory": ddboostFileReplicationHistory,
       "ddboostFileReplicationHistoryTable": ddboostFileReplicationHistoryTable,
       "ddboostFileReplicationHistoryEntry": ddboostFileReplicationHistoryEntry,
       "ddboostFileReplHistoryIndex": ddboostFileReplHistoryIndex,
       "ddboostFileReplHistoryDirection": ddboostFileReplHistoryDirection,
       "ddboostFileReplHistoryNetwork": ddboostFileReplHistoryNetwork,
       "ddboostFileReplHistoryPreComp": ddboostFileReplHistoryPreComp,
       "ddboostFileReplHistoryPostComp": ddboostFileReplHistoryPostComp,
       "ddboostFileReplHistoryLowBWOpt": ddboostFileReplHistoryLowBWOpt,
       "ddboostFileReplHistoryErrors": ddboostFileReplHistoryErrors,
       "ddboostFileReplHistoryDate": ddboostFileReplHistoryDate,
       "ddboostFileReplHistoryTime": ddboostFileReplHistoryTime,
       "ddboostIfGroupConfig": ddboostIfGroupConfig,
       "ddboostIfGroupConfigTable": ddboostIfGroupConfigTable,
       "ddboostIfGroupConfigEntry": ddboostIfGroupConfigEntry,
       "ddboostIfGroupConfigIndex": ddboostIfGroupConfigIndex,
       "ddboostIfGroupInterface": ddboostIfGroupInterface,
       "ddboostAccessClients": ddboostAccessClients,
       "ddboostAccessClientsTable": ddboostAccessClientsTable,
       "ddboostAccessClientsEntry": ddboostAccessClientsEntry,
       "ddboostAccessClientsIndex": ddboostAccessClientsIndex,
       "ddboostAccessClientsName": ddboostAccessClientsName,
       "ddboostAccessClientsEncryStrength": ddboostAccessClientsEncryStrength,
       "ddboostAccessClientsAuthMode": ddboostAccessClientsAuthMode,
       "ddboostOptions": ddboostOptions,
       "ddboostOptionsTable": ddboostOptionsTable,
       "ddboostOptionsEntry": ddboostOptionsEntry,
       "ddboostOptionsIndex": ddboostOptionsIndex,
       "ddboostOptionsName": ddboostOptionsName,
       "ddboostOptionsStatus": ddboostOptionsStatus,
       "ddboostFileReplicationPerformance": ddboostFileReplicationPerformance,
       "ddboostFileRepliPerfInPreCompKBPerSec": ddboostFileRepliPerfInPreCompKBPerSec,
       "ddboostFileRepliPerfInNetworkKBPerSec": ddboostFileRepliPerfInNetworkKBPerSec,
       "ddboostFileRepliPerfOutPreCompKBPerSec": ddboostFileRepliPerfOutPreCompKBPerSec,
       "ddboostFileRepliPerfOutNetworkKBPerSec": ddboostFileRepliPerfOutNetworkKBPerSec,
       "dataDomainSystem": dataDomainSystem,
       "systemProperties": systemProperties,
       "systemSerialNumber": systemSerialNumber,
       "systemCurrentTime": systemCurrentTime,
       "systemVersion": systemVersion,
       "systemModelNumber": systemModelNumber,
       "systemTimeZoneName": systemTimeZoneName,
       "sysNotes": sysNotes,
       "systemHardware": systemHardware,
       "systemHardwareTable": systemHardwareTable,
       "systemHardwareEntry": systemHardwareEntry,
       "systemHardwareIndex": systemHardwareIndex,
       "systemHardwareSlot": systemHardwareSlot,
       "systemHardwareVendor": systemHardwareVendor,
       "systemHardwareDevice": systemHardwareDevice,
       "systemHardwarePorts": systemHardwarePorts,
       "systemHardwareSlotName": systemHardwareSlotName,
       "systemPorts": systemPorts,
       "systemPortsTable": systemPortsTable,
       "systemPortsEntry": systemPortsEntry,
       "systemPortsIndex": systemPortsIndex,
       "systemPortsPort": systemPortsPort,
       "systemPortsConnectionType": systemPortsConnectionType,
       "systemPortsLinkSpeed": systemPortsLinkSpeed,
       "systemPortsFirmware": systemPortsFirmware,
       "systemPortsHardwareAddress": systemPortsHardwareAddress,
       "systemLicense": systemLicense,
       "systemLicenseTable": systemLicenseTable,
       "systemLicenseEntry": systemLicenseEntry,
       "systemLicenseIndex": systemLicenseIndex,
       "systemLicenseKey": systemLicenseKey,
       "systemLicenseFeature": systemLicenseFeature,
       "systemCapacityLicense": systemCapacityLicense,
       "systemCapacityLicenseTable": systemCapacityLicenseTable,
       "systemCapacityLicenseEntry": systemCapacityLicenseEntry,
       "systemCapacityLicenseIndex": systemCapacityLicenseIndex,
       "systemCapacityLicenseKey": systemCapacityLicenseKey,
       "systemCapacityLicenseFeature": systemCapacityLicenseFeature,
       "systemCapacityLicenseModel": systemCapacityLicenseModel,
       "systemCapacityLicenseCapacity": systemCapacityLicenseCapacity,
       "systemUser": systemUser,
       "systemUserTable": systemUserTable,
       "systemUserEntry": systemUserEntry,
       "systemUserIndex": systemUserIndex,
       "systemUserName": systemUserName,
       "systemUserUID": systemUserUID,
       "systemUserRole": systemUserRole,
       "systemUserStatus": systemUserStatus,
       "systemActiveUserTable": systemActiveUserTable,
       "systemActiveUserEntry": systemActiveUserEntry,
       "systemActiveUserIndex": systemActiveUserIndex,
       "systemActiveUserName": systemActiveUserName,
       "systemActiveUserIdleTime": systemActiveUserIdleTime,
       "systemActiveUserLoginTime": systemActiveUserLoginTime,
       "systemActiveUserLoginFrom": systemActiveUserLoginFrom,
       "systemActiveUserTty": systemActiveUserTty,
       "art": art,
       "artConfig": artConfig,
       "artConfigTable": artConfigTable,
       "artConfigEntry": artConfigEntry,
       "artConfigIndex": artConfigIndex,
       "artConfigStatus": artConfigStatus,
       "artConfigMigrationSchedule": artConfigMigrationSchedule,
       "artConfigDefaultAge": artConfigDefaultAge,
       "artConfigFileSystemClean": artConfigFileSystemClean,
       "artConfigCompression": artConfigCompression,
       "artMigrationSchedule": artMigrationSchedule,
       "artMigrationScheduleTable": artMigrationScheduleTable,
       "artMigrationScheduleEntry": artMigrationScheduleEntry,
       "artMigrationScheduleIndex": artMigrationScheduleIndex,
       "artMigrationScheduleSchedule": artMigrationScheduleSchedule,
       "artMigrationScheduleStatus": artMigrationScheduleStatus,
       "artMigrationPolicy": artMigrationPolicy,
       "artMigrationPolicyTable": artMigrationPolicyTable,
       "artMigrationPolicyEntry": artMigrationPolicyEntry,
       "artMigrationPolicyIndex": artMigrationPolicyIndex,
       "artMigrationPolicyMtreeName": artMigrationPolicyMtreeName,
       "artMigrationPolicyDefaultAge": artMigrationPolicyDefaultAge,
       "mtree": mtree,
       "mtreeCompression": mtreeCompression,
       "mtreeCompressionTable": mtreeCompressionTable,
       "mtreeCompressionEntry": mtreeCompressionEntry,
       "mtreeCompressionIndex": mtreeCompressionIndex,
       "mtreeCompressionMtreePath": mtreeCompressionMtreePath,
       "mtreeCompressionPreCompGib": mtreeCompressionPreCompGib,
       "mtreeCompressionPostCompGib": mtreeCompressionPostCompGib,
       "mtreeCompressionGlobalCompFactor": mtreeCompressionGlobalCompFactor,
       "mtreeCompressionLocalCompFactor": mtreeCompressionLocalCompFactor,
       "mtreeCompressionPostTotalCompFactor": mtreeCompressionPostTotalCompFactor,
       "mtreeCompressionTimePeriod": mtreeCompressionTimePeriod,
       "mtreeList": mtreeList,
       "mtreeListTable": mtreeListTable,
       "mtreeListEntry": mtreeListEntry,
       "mtreeListIndex": mtreeListIndex,
       "mtreeListMtreeName": mtreeListMtreeName,
       "mtreeListPreCompGib": mtreeListPreCompGib,
       "mtreeListStatus": mtreeListStatus,
       "mtreeRetentionLock": mtreeRetentionLock,
       "mtreeRetentionLockTable": mtreeRetentionLockTable,
       "mtreeRetentionLockEntry": mtreeRetentionLockEntry,
       "mtreeRetentionLockIndex": mtreeRetentionLockIndex,
       "mtreeRetentionLockMtreeName": mtreeRetentionLockMtreeName,
       "mtreeRetentionLockStatus": mtreeRetentionLockStatus,
       "mtreeRetentionLockUUID": mtreeRetentionLockUUID,
       "mtreeRetentionLockMinRetentionPeriod": mtreeRetentionLockMinRetentionPeriod,
       "mtreeRetentionLockMaxRetentionPeriod": mtreeRetentionLockMaxRetentionPeriod,
       "storage": storage,
       "enclosure": enclosure,
       "enclosureList": enclosureList,
       "enclosureListTable": enclosureListTable,
       "enclosureListEntry": enclosureListEntry,
       "enclosureListIndex": enclosureListIndex,
       "enclosureListNum": enclosureListNum,
       "enclosureListModel": enclosureListModel,
       "enclosureListSerialNum": enclosureListSerialNum,
       "enclosureListOemName": enclosureListOemName,
       "enclosureListOemValue": enclosureListOemValue,
       "enclosureListCapacity": enclosureListCapacity,
       "enclosurePack": enclosurePack,
       "enclosurePackTable": enclosurePackTable,
       "enclosurePackEntry": enclosurePackEntry,
       "enclosurePackID": enclosurePackID,
       "network": network,
       "dns": dns,
       "dnsTable": dnsTable,
       "dnsEntry": dnsEntry,
       "dnsIndex": dnsIndex,
       "dnsServer": dnsServer,
       "searchDomains": searchDomains,
       "searchDomainsTable": searchDomainsTable,
       "searchDomainsEntry": searchDomainsEntry,
       "searchDomainsIndex": searchDomainsIndex,
       "searchDomainsName": searchDomainsName,
       "snmpTrapHosts": snmpTrapHosts,
       "snmpTrapHostsTable": snmpTrapHostsTable,
       "snmpTrapHostsEntry": snmpTrapHostsEntry,
       "snmpTrapHostsIndex": snmpTrapHostsIndex,
       "snmpTrapHostsName": snmpTrapHostsName,
       "snmpTrapHostsVersion": snmpTrapHostsVersion,
       "nis": nis,
       "nisDomain": nisDomain,
       "nisServers": nisServers,
       "nisAdminGroups": nisAdminGroups,
       "nisUserGroups": nisUserGroups,
       "nisBackupOperatorGroups": nisBackupOperatorGroups,
       "nisEnabled": nisEnabled,
       "nisStatus": nisStatus,
       "ddms": ddms,
       "managedSystem": managedSystem,
       "managedSystemTable": managedSystemTable,
       "managedSystemEntry": managedSystemEntry,
       "managedSystemIndex": managedSystemIndex,
       "managedSystemHostname": managedSystemHostname,
       "managedSystemSerial": managedSystemSerial,
       "managedSystemState": managedSystemState,
       "managedSystemStatus": managedSystemStatus,
       "managedSystemDDOSVersion": managedSystemDDOSVersion,
       "managedSystemHDSyncTime": managedSystemHDSyncTime,
       "managedSystemCDSyncTime": managedSystemCDSyncTime,
       "taskHistory": taskHistory,
       "taskHistoryTable": taskHistoryTable,
       "taskHistoryEntry": taskHistoryEntry,
       "taskHistoryIndex": taskHistoryIndex,
       "taskHistoryUser": taskHistoryUser,
       "taskHistoryID": taskHistoryID,
       "taskHistoryParent": taskHistoryParent,
       "taskHistoryName": taskHistoryName,
       "taskHistoryState": taskHistoryState,
       "taskHistoryStartTime": taskHistoryStartTime,
       "taskHistoryDuration": taskHistoryDuration,
       "taskActive": taskActive,
       "taskActiveTable": taskActiveTable,
       "taskActiveEntry": taskActiveEntry,
       "taskActiveIndex": taskActiveIndex,
       "taskActiveUser": taskActiveUser,
       "taskActiveID": taskActiveID,
       "taskActiveParent": taskActiveParent,
       "taskActiveName": taskActiveName,
       "taskActiveState": taskActiveState,
       "taskActiveStartTime": taskActiveStartTime,
       "taskActiveDuration": taskActiveDuration,
       "smt": smt,
       "smtProperties": smtProperties,
       "smtStatus": smtStatus,
       "tenantUnitList": tenantUnitList,
       "tenantUnitListTable": tenantUnitListTable,
       "tenantUnitListEntry": tenantUnitListEntry,
       "tenantUnitListIdx": tenantUnitListIdx,
       "tenantUnitListName": tenantUnitListName,
       "tenantUnitListNumberOfMgmtUsers": tenantUnitListNumberOfMgmtUsers,
       "tenantUnitListNumberOfMtrees": tenantUnitListNumberOfMtrees,
       "tenantUnitListNumberOfDdboostStus": tenantUnitListNumberOfDdboostStus,
       "tenantUnitListTenantSelfServiceMode": tenantUnitListTenantSelfServiceMode,
       "tenantUnitListParentTenantName": tenantUnitListParentTenantName,
       "tenantUnitListType": tenantUnitListType,
       "tenantUnitListSecurityMode": tenantUnitListSecurityMode,
       "tenantUnitListNumberOfMgmtGroups": tenantUnitListNumberOfMgmtGroups,
       "tenantUnitMgmtUserList": tenantUnitMgmtUserList,
       "tenantUnitMgmtUserListTable": tenantUnitMgmtUserListTable,
       "tenantUnitMgmtUserListEntry": tenantUnitMgmtUserListEntry,
       "tenantUnitMgmtUserListUserName": tenantUnitMgmtUserListUserName,
       "tenantUnitMgmtUserListUserRole": tenantUnitMgmtUserListUserRole,
       "tenantUnitMtreeList": tenantUnitMtreeList,
       "tenantUnitMtreeListTable": tenantUnitMtreeListTable,
       "tenantUnitMtreeListEntry": tenantUnitMtreeListEntry,
       "tenantUnitMtreeListMtreeName": tenantUnitMtreeListMtreeName,
       "tenantUnitDdboostStuList": tenantUnitDdboostStuList,
       "tenantUnitDdboostStuListTable": tenantUnitDdboostStuListTable,
       "tenantUnitDdboostStuListEntry": tenantUnitDdboostStuListEntry,
       "tenantUnitDdboostStuListStuName": tenantUnitDdboostStuListStuName,
       "tenantUnitAdminIpInfo": tenantUnitAdminIpInfo,
       "tenantUnitAdminIpInfoTable": tenantUnitAdminIpInfoTable,
       "tenantUnitAdminIpInfoEntry": tenantUnitAdminIpInfoEntry,
       "tenantUnitAdminIpInfoAddr": tenantUnitAdminIpInfoAddr,
       "tenantUnitAdminIpInfoType": tenantUnitAdminIpInfoType,
       "tenantInfo": tenantInfo,
       "tenantInfoTable": tenantInfoTable,
       "tenantInfoEntry": tenantInfoEntry,
       "tenantInfoIdx": tenantInfoIdx,
       "tenantInfoTenantName": tenantInfoTenantName,
       "tenantInfoTenantUnitTable": tenantInfoTenantUnitTable,
       "tenantInfoTenantUnitEntry": tenantInfoTenantUnitEntry,
       "tenantInfoTenantUnitName": tenantInfoTenantUnitName,
       "tenantUnitMgmtGroupList": tenantUnitMgmtGroupList,
       "tenantUnitMgmtGroupListTable": tenantUnitMgmtGroupListTable,
       "tenantUnitMgmtGroupListEntry": tenantUnitMgmtGroupListEntry,
       "tenantUnitMgmtGroupListGroupName": tenantUnitMgmtGroupListGroupName,
       "tenantUnitMgmtGroupListGroupRole": tenantUnitMgmtGroupListGroupRole,
       "tenantUnitMgmtGroupListGroupType": tenantUnitMgmtGroupListGroupType,
       "quota": quota,
       "quotaProperties": quotaProperties,
       "quotaCapacityStatus": quotaCapacityStatus,
       "quotaCapacity": quotaCapacity,
       "quotaCapacityTable": quotaCapacityTable,
       "quotaCapacityEntry": quotaCapacityEntry,
       "quotaCapacityIndex": quotaCapacityIndex,
       "quotaCapacityMtreeName": quotaCapacityMtreeName,
       "quotaCapacityPreCompMiB": quotaCapacityPreCompMiB,
       "quotaCapacitySoftLimitMiB": quotaCapacitySoftLimitMiB,
       "quotaCapacityHardLimitMiB": quotaCapacityHardLimitMiB,
       "quotaCapacityTenantUnit": quotaCapacityTenantUnit,
       "highAvailability": highAvailability,
       "highAvailabilityStatus": highAvailabilityStatus,
       "haSystemStatus": haSystemStatus,
       "localNodeRole": localNodeRole,
       "localHaState": localHaState,
       "peerNodeRole": peerNodeRole,
       "peerHaState": peerHaState,
       "highAvailabilityConfig": highAvailabilityConfig,
       "haConfiguredMode": haConfiguredMode,
       "haLocalPnodeId": haLocalPnodeId,
       "scsitarget": scsitarget,
       "scsitargetProperties": scsitargetProperties,
       "scsitargetAdminState": scsitargetAdminState,
       "scsitargetProcessState": scsitargetProcessState,
       "scsitargetGroup": scsitargetGroup,
       "scsitargetGroupTable": scsitargetGroupTable,
       "scsitargetGroupEntry": scsitargetGroupEntry,
       "scsitargetGroupIndex": scsitargetGroupIndex,
       "scsitargetGroupName": scsitargetGroupName,
       "scsitargetGroupService": scsitargetGroupService,
       "scsitargetGroupActiveState": scsitargetGroupActiveState,
       "scsitargetGroupNumInitiators": scsitargetGroupNumInitiators,
       "scsitargetGroupNumDevices": scsitargetGroupNumDevices,
       "scsitargetInitiator": scsitargetInitiator,
       "scsitargetInitiatorTable": scsitargetInitiatorTable,
       "scsitargetInitiatorEntry": scsitargetInitiatorEntry,
       "scsitargetInitiatorIndex": scsitargetInitiatorIndex,
       "scsitargetInitiatorName": scsitargetInitiatorName,
       "scsitargetInitiatorSystemAddress": scsitargetInitiatorSystemAddress,
       "scsitargetInitiatorGroup": scsitargetInitiatorGroup,
       "scsitargetInitiatorService": scsitargetInitiatorService,
       "scsitargetInitiatorAddressMethod": scsitargetInitiatorAddressMethod,
       "scsitargetInitiatorTransport": scsitargetInitiatorTransport,
       "scsitargetInitiatorFcWwpn": scsitargetInitiatorFcWwpn,
       "scsitargetInitiatorFcWwnn": scsitargetInitiatorFcWwnn,
       "scsitargetInitiatorFcSymbolicPortName": scsitargetInitiatorFcSymbolicPortName,
       "scsitargetInitiatorEndpTable": scsitargetInitiatorEndpTable,
       "scsitargetInitiatorEndpEntry": scsitargetInitiatorEndpEntry,
       "scsitargetInitiatorEndpIndex": scsitargetInitiatorEndpIndex,
       "scsitargetInitiatorEndpInitiator": scsitargetInitiatorEndpInitiator,
       "scsitargetInitiatorEndpEndpoint": scsitargetInitiatorEndpEndpoint,
       "scsitargetInitiatorEndpStatus": scsitargetInitiatorEndpStatus,
       "scsitargetEndpoint": scsitargetEndpoint,
       "scsitargetEndpointTable": scsitargetEndpointTable,
       "scsitargetEndpointEntry": scsitargetEndpointEntry,
       "scsitargetEndpointIndex": scsitargetEndpointIndex,
       "scsitargetEndpointName": scsitargetEndpointName,
       "scsitargetEndpointCurrentSystemAddress": scsitargetEndpointCurrentSystemAddress,
       "scsitargetEndpointPrimarySystemAddress": scsitargetEndpointPrimarySystemAddress,
       "scsitargetEndpointSecondarySystemAddress": scsitargetEndpointSecondarySystemAddress,
       "scsitargetEndpointEnabled": scsitargetEndpointEnabled,
       "scsitargetEndpointStatus": scsitargetEndpointStatus,
       "scsitargetEndpointTransport": scsitargetEndpointTransport,
       "scsitargetEndpointFcWwnn": scsitargetEndpointFcWwnn,
       "scsitargetEndpointFcWwpn": scsitargetEndpointFcWwpn,
       "scsitargetPort": scsitargetPort,
       "scsitargetPortTable": scsitargetPortTable,
       "scsitargetPortEntry": scsitargetPortEntry,
       "scsitargetPortIndex": scsitargetPortIndex,
       "scsitargetPortSystemAddress": scsitargetPortSystemAddress,
       "scsitargetPortEnabled": scsitargetPortEnabled,
       "scsitargetPortStatus": scsitargetPortStatus,
       "scsitargetPortTransport": scsitargetPortTransport,
       "scsitargetPortOperationalStatus": scsitargetPortOperationalStatus,
       "scsitargetPortFcNpiv": scsitargetPortFcNpiv,
       "scsitargetPortPortId": scsitargetPortPortId,
       "scsitargetPortModel": scsitargetPortModel,
       "scsitargetPortFirmware": scsitargetPortFirmware,
       "scsitargetPortFcBaseWwnn": scsitargetPortFcBaseWwnn,
       "scsitargetPortFcBaseWwpn": scsitargetPortFcBaseWwpn,
       "scsitargetPortFcCurrentWwnn": scsitargetPortFcCurrentWwnn,
       "scsitargetPortFcCurrentWwpn": scsitargetPortFcCurrentWwpn,
       "scsitargetPortFcp2Retry": scsitargetPortFcp2Retry,
       "scsitargetPortConnectionType": scsitargetPortConnectionType,
       "scsitargetPortLinkSpeed": scsitargetPortLinkSpeed,
       "scsitargetPortFcTopology": scsitargetPortFcTopology,
       "scsitargetPortEndpTable": scsitargetPortEndpTable,
       "scsitargetPortEndpEntry": scsitargetPortEndpEntry,
       "scsitargetPortEndpIndex": scsitargetPortEndpIndex,
       "scsitargetPortEndpPort": scsitargetPortEndpPort,
       "scsitargetPortEndpEndpoint": scsitargetPortEndpEndpoint,
       "scsitargetPortEndpEnabled": scsitargetPortEndpEnabled,
       "scsitargetPortEndpStatus": scsitargetPortEndpStatus,
       "scsitargetPortEndpCurrentInstance": scsitargetPortEndpCurrentInstance,
       "scsitargetDevice": scsitargetDevice,
       "scsitargetDeviceTable": scsitargetDeviceTable,
       "scsitargetDeviceEntry": scsitargetDeviceEntry,
       "scsitargetDeviceIndex": scsitargetDeviceIndex,
       "scsitargetDeviceName": scsitargetDeviceName,
       "scsitargetDeviceService": scsitargetDeviceService,
       "scsitargetDeviceActiveState": scsitargetDeviceActiveState,
       "scsitargetDeviceAddress": scsitargetDeviceAddress,
       "scsitargetDeviceGrpTable": scsitargetDeviceGrpTable,
       "scsitargetDeviceGrpEntry": scsitargetDeviceGrpEntry,
       "scsitargetDeviceGrpIndex": scsitargetDeviceGrpIndex,
       "scsitargetDeviceGrpDevice": scsitargetDeviceGrpDevice,
       "scsitargetDeviceGrpGroupName": scsitargetDeviceGrpGroupName,
       "scsitargetDeviceGrpLun": scsitargetDeviceGrpLun,
       "scsitargetDeviceGrpPrimaryEndpoints": scsitargetDeviceGrpPrimaryEndpoints,
       "scsitargetDeviceGrpSecondaryEndpoints": scsitargetDeviceGrpSecondaryEndpoints,
       "scsitargetDeviceGrpInUseEndpoints": scsitargetDeviceGrpInUseEndpoints,
       "dataDomainMibNotifications": dataDomainMibNotifications,
       "dataDomainMibTraps": dataDomainMibTraps,
       "powerSupplyFailedAlarm": powerSupplyFailedAlarm,
       "systemOverheatWarningAlarm": systemOverheatWarningAlarm,
       "systemOverheatAlertAlarm": systemOverheatAlertAlarm,
       "systemOverheatShutdownAlarm": systemOverheatShutdownAlarm,
       "fanModuleFailedAlarm": fanModuleFailedAlarm,
       "nvramFailingAlarm": nvramFailingAlarm,
       "fileSystemFailedAlarm": fileSystemFailedAlarm,
       "fileSpaceMaintenanceAlarm": fileSpaceMaintenanceAlarm,
       "fileSpacePreWarningAlarm": fileSpacePreWarningAlarm,
       "fileSpaceWarningAlarm": fileSpaceWarningAlarm,
       "fileSpaceSevereAlarm": fileSpaceSevereAlarm,
       "fileSpaceCriticalAlarm": fileSpaceCriticalAlarm,
       "diskFailedAlarm": diskFailedAlarm,
       "diskOverheatWarningAlarm": diskOverheatWarningAlarm,
       "diskOverheatAlertAlarm": diskOverheatAlertAlarm,
       "diskOverheatShutdownAlarm": diskOverheatShutdownAlarm,
       "raidReconSevereAlarm": raidReconSevereAlarm,
       "raidReconCriticalAlarm": raidReconCriticalAlarm,
       "raidReconCriticalShutdownAlarm": raidReconCriticalShutdownAlarm,
       "raidGroupMissingAlarm": raidGroupMissingAlarm,
       "diskNoSpareAlarm": diskNoSpareAlarm,
       "diskPathAlarm": diskPathAlarm,
       "diskSASAlarm": diskSASAlarm,
       "diskSASHBAAlarm": diskSASHBAAlarm,
       "snapshotFullAlarm": snapshotFullAlarm,
       "snapshotHWMAlarm": snapshotHWMAlarm,
       "clusterNodeAlarm": clusterNodeAlarm,
       "clusterInterfaceAlarm": clusterInterfaceAlarm,
       "replSyncAlarm": replSyncAlarm,
       "systemStartupAlarm": systemStartupAlarm,
       "filesysRelaunchAlarm": filesysRelaunchAlarm,
       "filesysDDGCFailedAlarm": filesysDDGCFailedAlarm,
       "filesysGeneralProblemAlarm": filesysGeneralProblemAlarm,
       "diskUnsupportedAlarm": diskUnsupportedAlarm,
       "eventIPMIUnmanageAlarm": eventIPMIUnmanageAlarm,
       "controllerUnreachableAlert": controllerUnreachableAlert,
       "controllerIfaceUnreachableAlert": controllerIfaceUnreachableAlert,
       "correctableECCLimitReached": correctableECCLimitReached,
       "uncorrectableECCerror": uncorrectableECCerror,
       "legacyChassisTempWarning": legacyChassisTempWarning,
       "legacyChassisTempCritical": legacyChassisTempCritical,
       "legacyPowerSupplyWarning": legacyPowerSupplyWarning,
       "legacyFanWarning": legacyFanWarning,
       "powerSupplyWarning": powerSupplyWarning,
       "fanWarning": fanWarning,
       "voltageWarning": voltageWarning,
       "powerWarning": powerWarning,
       "correctECCWarning": correctECCWarning,
       "processorWarning": processorWarning,
       "powerUnitWarning": powerUnitWarning,
       "unCorrectECCWarning": unCorrectECCWarning,
       "chassisSensorCritical": chassisSensorCritical,
       "chassisTempWarning": chassisTempWarning,
       "chassisTempCritical": chassisTempCritical,
       "cPUFailureWarning": cPUFailureWarning,
       "legacyBMCHangCritical": legacyBMCHangCritical,
       "bMCHangCritical": bMCHangCritical,
       "abnormalShutdown": abnormalShutdown,
       "tooManyRelaunches": tooManyRelaunches,
       "filesystemProblem": filesystemProblem,
       "dDFSFailedInShutdown": dDFSFailedInShutdown,
       "dDFSNoHeartbeat": dDFSNoHeartbeat,
       "dDFSDiedAfterReboot": dDFSDiedAfterReboot,
       "dDFSDied": dDFSDied,
       "dDFSRebooted": dDFSRebooted,
       "dDFSRebootedDisabled": dDFSRebootedDisabled,
       "indexRebuildComplete": indexRebuildComplete,
       "historicalDatabaseRecoverError": historicalDatabaseRecoverError,
       "historicalDatabaseBackupError": historicalDatabaseBackupError,
       "historicalDatabaseUpgradeError": historicalDatabaseUpgradeError,
       "historicalDatabasePruneError": historicalDatabasePruneError,
       "noHistoricalDatabaseError": noHistoricalDatabaseError,
       "hDTFileTransferFailed": hDTFileTransferFailed,
       "hDTSystemError": hDTSystemError,
       "dIMMFailureAlert": dIMMFailureAlert,
       "memoryAlert": memoryAlert,
       "portPathDisabled": portPathDisabled,
       "diskPathRedundancy": diskPathRedundancy,
       "missingPortConnection": missingPortConnection,
       "missingLunPath": missingLunPath,
       "missingDiskPath": missingDiskPath,
       "missingEnclosurePath": missingEnclosurePath,
       "nvramWarning": nvramWarning,
       "nvramBatteryAlert": nvramBatteryAlert,
       "nvramErrorAlert": nvramErrorAlert,
       "phyalert": phyalert,
       "replProgressThreshholdReached": replProgressThreshholdReached,
       "replNeedResync": replNeedResync,
       "replLogFull": replLogFull,
       "replIncompatibleWorm": replIncompatibleWorm,
       "replDestNotConfigured": replDestNotConfigured,
       "replLagThreshholdReached": replLagThreshholdReached,
       "sASEnclosureCheck": sASEnclosureCheck,
       "sASTopologyCheck": sASTopologyCheck,
       "sASPortDisabled": sASPortDisabled,
       "sSLCertificateCorrupted": sSLCertificateCorrupted,
       "snapshotOver90Percent": snapshotOver90Percent,
       "snapshotLimitReached": snapshotLimitReached,
       "sNTZMultipleIterations": sNTZMultipleIterations,
       "coredumpWarning": coredumpWarning,
       "coredumpDisabled": coredumpDisabled,
       "spaceOver80Percent": spaceOver80Percent,
       "spaceOver90Percent": spaceOver90Percent,
       "diskAccessError": diskAccessError,
       "diskFailure": diskFailure,
       "diskTemperatureWarning": diskTemperatureWarning,
       "diskTemperatureShutdown": diskTemperatureShutdown,
       "unsupportedHardwareSpareSize": unsupportedHardwareSpareSize,
       "missingDiskGroup": missingDiskGroup,
       "diskGroupReconstructionNoProgress": diskGroupReconstructionNoProgress,
       "diskGroupReconstruction": diskGroupReconstruction,
       "diskGroupReconstructionShutdown": diskGroupReconstructionShutdown,
       "diskGroupReconstructionCritical": diskGroupReconstructionCritical,
       "diskUnknown": diskUnknown,
       "lowSpares": lowSpares,
       "unsupportedConfigurationROL": unsupportedConfigurationROL,
       "cpismissing": cpismissing,
       "containerMarkedInvalid": containerMarkedInvalid,
       "smiMrc": smiMrc,
       "nvramBatteryLowChargeAlert": nvramBatteryLowChargeAlert,
       "ext3NvlogDisabled": ext3NvlogDisabled,
       "enclosureMixType": enclosureMixType,
       "replPathTooLong": replPathTooLong,
       "compromisedEncryptionKeys": compromisedEncryptionKeys,
       "newEncryptionKey": newEncryptionKey,
       "encryptionKeyTableFull": encryptionKeyTableFull,
       "uncertifiedFirmware": uncertifiedFirmware,
       "filesystemNVRAMDataLoss": filesystemNVRAMDataLoss,
       "mtreeQuotaSoftLimit": mtreeQuotaSoftLimit,
       "mtreeQuotaHardLimit": mtreeQuotaHardLimit,
       "interfaceConnectivityDown": interfaceConnectivityDown,
       "interfaceConnectivityIntermittent": interfaceConnectivityIntermittent,
       "interfaceMisconfiguration": interfaceMisconfiguration,
       "recoverFromNVRAMFailed": recoverFromNVRAMFailed,
       "cleaningError": cleaningError,
       "bMCPartialHang": bMCPartialHang,
       "fileMigrationError": fileMigrationError,
       "unusableHostCertificate": unusableHostCertificate,
       "missingHostCertificate": missingHostCertificate,
       "foreignEnclosure": foreignEnclosure,
       "interfaceConnectivityUpAndRunning": interfaceConnectivityUpAndRunning,
       "tcpZeroWindowAlert": tcpZeroWindowAlert,
       "insecureEncryptedReplication": insecureEncryptedReplication,
       "nvramHWAlert": nvramHWAlert,
       "nvramEnvAlert": nvramEnvAlert,
       "nvramEventHWAlert": nvramEventHWAlert,
       "nvramBattAlert": nvramBattAlert,
       "nvramCondAlert": nvramCondAlert,
       "upgradeFailure": upgradeFailure,
       "upgradeCompleted": upgradeCompleted,
       "mailserverError": mailserverError,
       "invalidNICSlot": invalidNICSlot,
       "unsupportedNIC": unsupportedNIC,
       "sASHBAFailure": sASHBAFailure,
       "sASHBAErrors": sASHBAErrors,
       "unsupportedSASDevice": unsupportedSASDevice,
       "fanFault": fanFault,
       "powerSupplyInputFault": powerSupplyInputFault,
       "powerSupplyFailure": powerSupplyFailure,
       "powerSupplyAbsent": powerSupplyAbsent,
       "unsupportedACVoltage": unsupportedACVoltage,
       "iOModuleFault": iOModuleFault,
       "iOModuleInserted": iOModuleInserted,
       "mgmtModuleFault": mgmtModuleFault,
       "dIMMFailure": dIMMFailure,
       "sPFault": sPFault,
       "chassisFailure": chassisFailure,
       "forcedControllerShutdown": forcedControllerShutdown,
       "systemReset": systemReset,
       "duplicateAddressDetection": duplicateAddressDetection,
       "spaceReclRestartFailed": spaceReclRestartFailed,
       "spaceReclMissingUnit": spaceReclMissingUnit,
       "spaceReclUnitReclaimed": spaceReclUnitReclaimed,
       "spaceReclError": spaceReclError,
       "enclosureHighTemp": enclosureHighTemp,
       "unsupportedSystemType": unsupportedSystemType,
       "bMCHangShutdown": bMCHangShutdown,
       "expiredHostCertificate": expiredHostCertificate,
       "sCSITGTInvalidRegistry": sCSITGTInvalidRegistry,
       "encryptionKeyExportFailed": encryptionKeyExportFailed,
       "sSDEndOfLife": sSDEndOfLife,
       "tapeReposition": tapeReposition,
       "multipleDiskReadErrors": multipleDiskReadErrors,
       "missingCreplUnits": missingCreplUnits,
       "nvramBattEndOfLife": nvramBattEndOfLife,
       "bMCFailure": bMCFailure,
       "unsupportedDriveModel": unsupportedDriveModel,
       "driveMixType": driveMixType,
       "sMSUnresponsive": sMSUnresponsive,
       "nISCommFailure": nISCommFailure,
       "unsupportedHardwareConfig": unsupportedHardwareConfig,
       "unsupportedVirtualCPU": unsupportedVirtualCPU,
       "dNSUnresponsive": dNSUnresponsive,
       "nTPDFailed": nTPDFailed,
       "invalidEnclosureTopology": invalidEnclosureTopology,
       "diskPathSpeedDegraded": diskPathSpeedDegraded,
       "targetDriverPortOffline": targetDriverPortOffline,
       "targetDriverPortOnline": targetDriverPortOnline,
       "targetDriverPortCore": targetDriverPortCore,
       "targetDriverPortMultipleCore": targetDriverPortMultipleCore,
       "targetDriverPortFWLoadFailed": targetDriverPortFWLoadFailed,
       "targetDriverPortUnreadable": targetDriverPortUnreadable,
       "targetDriverPortTooManyOsc": targetDriverPortTooManyOsc,
       "insufficientSpaceForEncryption": insufficientSpaceForEncryption,
       "dDFSRequiresReboot": dDFSRequiresReboot,
       "storageUnitStreamSoftLimit": storageUnitStreamSoftLimit,
       "spaceReclSuspended": spaceReclSuspended,
       "metadataWarningThreshold": metadataWarningThreshold,
       "mtreeCascadeNeedResync": mtreeCascadeNeedResync,
       "filesystemCorruption": filesystemCorruption,
       "missingTierStorage": missingTierStorage,
       "spaceReclUnitError": spaceReclUnitError,
       "bMCFailureSysBBU": bMCFailureSysBBU,
       "licenseExpiring": licenseExpiring,
       "licenseExpired": licenseExpired,
       "unsupportedEnclosurePSU": unsupportedEnclosurePSU,
       "unsupportedPowerSupply": unsupportedPowerSupply,
       "openFanDrawer": openFanDrawer,
       "memoryRiserFault": memoryRiserFault,
       "pCILinkDegraded": pCILinkDegraded,
       "invalidHardwareCritical": invalidHardwareCritical,
       "invalidHardwareWarning": invalidHardwareWarning,
       "correctableErrorWarning": correctableErrorWarning,
       "spuriousInterruptDisabled": spuriousInterruptDisabled,
       "corruptEncryptionKeys": corruptEncryptionKeys,
       "duplicateVTLPoolNames": duplicateVTLPoolNames,
       "generalHardwareFailure": generalHardwareFailure,
       "iOModuleMacFault": iOModuleMacFault,
       "storageMigrationCannotResume": storageMigrationCannotResume,
       "storageMigrationCopyComplete": storageMigrationCopyComplete,
       "storageMigrationUserSuspend": storageMigrationUserSuspend,
       "cMTaskEnded": cMTaskEnded,
       "physicalCapacityMeasurementTasksLost": physicalCapacityMeasurementTasksLost,
       "physicalCapacityMeasurementTasksLostMTree": physicalCapacityMeasurementTasksLostMTree,
       "physicalCapacityMeasurementScheduleFailed": physicalCapacityMeasurementScheduleFailed,
       "historicalDatabaseFailoverError": historicalDatabaseFailoverError,
       "hAdegraded": hAdegraded,
       "upgradeInProgress": upgradeInProgress,
       "hAofflineErrors": hAofflineErrors,
       "suspendedMReplMissingUnits": suspendedMReplMissingUnits,
       "foreignPack": foreignPack,
       "vDiskSCSITargetMismatch": vDiskSCSITargetMismatch,
       "hATimeOutOfSync": hATimeOutOfSync,
       "enclosureMixDriveType": enclosureMixDriveType,
       "dataDomainMibProducts": dataDomainMibProducts,
       "restorer": restorer,
       "unknown": unknown,
       "dd200": dd200,
       "dd200Proto": dd200Proto,
       "dd410": dd410,
       "dd430": dd430,
       "dd460": dd460,
       "dd400g": dd400g,
       "dd460g": dd460g,
       "dd560": dd560,
       "dd560g": dd560g,
       "dd580": dd580,
       "dd580g": dd580g,
       "dd565": dd565,
       "dd530": dd530,
       "dd510": dd510,
       "dd120": dd120,
       "dd690": dd690,
       "dd690g": dd690g,
       "dd660": dd660,
       "dd880": dd880,
       "dd880g": dd880g,
       "dd610": dd610,
       "dd630": dd630,
       "dd140": dd140,
       "dd670": dd670,
       "dd860": dd860,
       "dd860g": dd860g,
       "dd890": dd890,
       "dd640": dd640,
       "dd620": dd620,
       "dd160": dd160,
       "ddintrepid": ddintrepid,
       "dd4500": dd4500,
       "dd7200": dd7200,
       "ddve": ddve,
       "dd990": dd990,
       "dd2500": dd2500,
       "dd4200": dd4200,
       "ddkoalam1": ddkoalam1,
       "apollo": apollo,
       "unset": unset}
)
