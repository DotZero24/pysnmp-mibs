# SNMP MIB module (TALARI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/oracle/TALARI-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:07:34 2025
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

(AutonomousType,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

talari = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 34086)
)
if mibBuilder.loadTexts:
    talari.setRevisions(
        ("2018-08-20 00:00",
         "2018-07-18 00:00",
         "2017-09-06 00:00",
         "2017-06-06 00:00",
         "2017-01-23 00:00",
         "2017-01-19 00:00",
         "2017-01-10 00:00",
         "2016-02-19 00:00",
         "2016-02-03 00:00",
         "2015-10-15 00:00",
         "2015-04-01 00:00",
         "2015-01-19 00:00",
         "2014-09-05 00:00",
         "2014-06-30 00:00",
         "2014-06-06 00:00",
         "2014-03-13 00:00",
         "2014-01-02 00:00",
         "2013-11-12 00:00",
         "2013-11-08 00:00",
         "2013-10-09 00:00",
         "2013-09-10 00:00",
         "2013-08-12 00:00",
         "2013-06-24 00:00",
         "2013-06-07 00:00",
         "2013-05-20 00:00",
         "2013-05-13 00:00",
         "2013-05-09 00:00",
         "2013-05-07 00:00",
         "2012-07-16 00:00",
         "2011-07-21 00:00",
         "2011-06-13 00:00",
         "2011-03-24 00:00",
         "2010-12-08 00:00",
         "2010-08-12 00:00",
         "2009-10-26 00:00",
         "2008-11-18 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TalariEventObjectTypeEnum(TextualConvention, Integer32):
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
              1001,
              1002,
              1003,
              1004,
              1005)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 1),
          ("service", 2),
          ("conduit", 3),
          ("wanlink", 4),
          ("path", 5),
          ("harddisk", 6),
          ("fan", 7),
          ("apna", 8),
          ("apnuser", 9),
          ("powersupply", 10),
          ("configupdate", 11),
          ("softwareupdate", 12),
          ("proxyarp", 13),
          ("ethernet", 14),
          ("watchdog", 15),
          ("dynamicconduit", 16),
          ("waningresspath", 17),
          ("wanegresspath", 18),
          ("appliancesettingsupdate", 19),
          ("discoveredmtu", 20),
          ("wanlinkcongestion", 21),
          ("usagecongestion", 22),
          ("langretunnel", 23),
          ("ipsectunnel", 24),
          ("virtualinterface", 25),
          ("licensesubsystem", 26),
          ("dynamicrouting", 27),
          ("wanop", 28),
          ("wanlinkusagethreshold", 29),
          ("awaresystem", 1001),
          ("awareuser", 1002),
          ("awarestorage", 1003),
          ("awaredatabase", 1004),
          ("connectiontoapna", 1005))
    )



class TalariEventSeverityEnum(TextualConvention, Integer32):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("debug", 1),
          ("info", 2),
          ("notice", 3),
          ("warning", 4),
          ("error", 5),
          ("critical", 6),
          ("alert", 7),
          ("emergency", 8))
    )



class TalariEventStateEnum(TextualConvention, Integer32):
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
              49,
              50,
              51,
              52,
              1001,
              1002,
              1003,
              1004)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 1),
          ("disabled", 2),
          ("dead", 3),
          ("bad", 4),
          ("good", 5),
          ("warning", 6),
          ("error", 7),
          ("restart", 8),
          ("reboot", 9),
          ("active", 10),
          ("standby", 11),
          ("success", 12),
          ("failure", 13),
          ("enabled", 14),
          ("pending", 15),
          ("created", 16),
          ("removed", 17),
          ("systemerror", 18),
          ("activeha", 19),
          ("standbyha", 20),
          ("activencn", 21),
          ("standbyncn", 22),
          ("congested", 23),
          ("uncongested", 24),
          ("viplearned", 25),
          ("vipreleased", 26),
          ("vipexpired", 27),
          ("vipgwnorsp", 28),
          ("viprcvdnak", 29),
          ("vipdetecteddup", 30),
          ("vipdhcpsnorsp", 31),
          ("licenseexpired", 32),
          ("featuremismatch", 33),
          ("configlicensemismatch", 34),
          ("unlicensedappliance", 35),
          ("licenseactive", 36),
          ("licensebankunreachable", 37),
          ("licensebankreachable", 38),
          ("bandwidthexceeded", 39),
          ("awareclientunlicensed", 40),
          ("hasecondaryunlicensed", 41),
          ("servicecontractunlicensed", 42),
          ("vipduplicate", 43),
          ("vipnotduplicate", 44),
          ("waningressusagelowerthresholdexceeded", 45),
          ("waningressusagelowerthresholdok", 46),
          ("wanegressusagelowerthresholdexceeded", 47),
          ("wanegressusagelowerthresholdok", 48),
          ("waningressusagehigherthresholdexceeded", 49),
          ("waningressusagehigherthresholdok", 50),
          ("wanegressusagehigherthresholdexceeded", 51),
          ("wanegressusagehigherthresholdok", 52),
          ("thresholdok", 1001),
          ("thresholdexceeded", 1002),
          ("pollingthresholdok", 1003),
          ("pollingthresholdexceeded", 1004))
    )



# MIB Managed Objects in the order of their OIDs

_TalariObjects_ObjectIdentity = ObjectIdentity
talariObjects = _TalariObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 2)
)
_TalariConfiguration_ObjectIdentity = ObjectIdentity
talariConfiguration = _TalariConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 2, 1)
)
_TalariStatistics_ObjectIdentity = ObjectIdentity
talariStatistics = _TalariStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2)
)
_TnStatsAppliances_ObjectIdentity = ObjectIdentity
tnStatsAppliances = _TnStatsAppliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 12)
)
_TnStatsApplianceScalars_ObjectIdentity = ObjectIdentity
tnStatsApplianceScalars = _TnStatsApplianceScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 12, 1)
)
_TnStatsApplianceName_Type = DisplayString
_TnStatsApplianceName_Object = MibScalar
tnStatsApplianceName = _TnStatsApplianceName_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 12, 1, 1),
    _TnStatsApplianceName_Type()
)
tnStatsApplianceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsApplianceName.setStatus("current")
_TnStatsApplianceModel_Type = ObjectIdentifier
_TnStatsApplianceModel_Object = MibScalar
tnStatsApplianceModel = _TnStatsApplianceModel_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 12, 1, 2),
    _TnStatsApplianceModel_Type()
)
tnStatsApplianceModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsApplianceModel.setStatus("current")
_TnStatsApplianceModelName_Type = DisplayString
_TnStatsApplianceModelName_Object = MibScalar
tnStatsApplianceModelName = _TnStatsApplianceModelName_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 12, 1, 3),
    _TnStatsApplianceModelName_Type()
)
tnStatsApplianceModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsApplianceModelName.setStatus("current")
_TnStatsApplianceBytesSent_Type = Counter64
_TnStatsApplianceBytesSent_Object = MibScalar
tnStatsApplianceBytesSent = _TnStatsApplianceBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 12, 1, 4),
    _TnStatsApplianceBytesSent_Type()
)
tnStatsApplianceBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsApplianceBytesSent.setStatus("current")
_TnStatsAppliancePacketsSent_Type = Counter64
_TnStatsAppliancePacketsSent_Object = MibScalar
tnStatsAppliancePacketsSent = _TnStatsAppliancePacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 12, 1, 5),
    _TnStatsAppliancePacketsSent_Type()
)
tnStatsAppliancePacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsAppliancePacketsSent.setStatus("current")
_TnStatsApplianceBytesReceived_Type = Counter64
_TnStatsApplianceBytesReceived_Object = MibScalar
tnStatsApplianceBytesReceived = _TnStatsApplianceBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 12, 1, 6),
    _TnStatsApplianceBytesReceived_Type()
)
tnStatsApplianceBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsApplianceBytesReceived.setStatus("current")
_TnStatsAppliancePacketsReceived_Type = Counter64
_TnStatsAppliancePacketsReceived_Object = MibScalar
tnStatsAppliancePacketsReceived = _TnStatsAppliancePacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 12, 1, 7),
    _TnStatsAppliancePacketsReceived_Type()
)
tnStatsAppliancePacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsAppliancePacketsReceived.setStatus("current")
_TnStatsApplianceBytesDropped_Type = Counter64
_TnStatsApplianceBytesDropped_Object = MibScalar
tnStatsApplianceBytesDropped = _TnStatsApplianceBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 12, 1, 8),
    _TnStatsApplianceBytesDropped_Type()
)
tnStatsApplianceBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsApplianceBytesDropped.setStatus("current")
_TnStatsAppliancePacketsDropped_Type = Counter64
_TnStatsAppliancePacketsDropped_Object = MibScalar
tnStatsAppliancePacketsDropped = _TnStatsAppliancePacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 12, 1, 9),
    _TnStatsAppliancePacketsDropped_Type()
)
tnStatsAppliancePacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsAppliancePacketsDropped.setStatus("current")


class _TnStatsApplianceState_Type(Integer32):
    """Custom type tnStatsApplianceState based on Integer32"""
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
          ("disabled", 1),
          ("enabled", 2))
    )


_TnStatsApplianceState_Type.__name__ = "Integer32"
_TnStatsApplianceState_Object = MibScalar
tnStatsApplianceState = _TnStatsApplianceState_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 12, 1, 10),
    _TnStatsApplianceState_Type()
)
tnStatsApplianceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsApplianceState.setStatus("current")


class _TnStatsApplianceHAState_Type(Integer32):
    """Custom type tnStatsApplianceHAState based on Integer32"""
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
        *(("undefined", 0),
          ("notConfigured", 1),
          ("active", 2),
          ("standby", 3))
    )


_TnStatsApplianceHAState_Type.__name__ = "Integer32"
_TnStatsApplianceHAState_Object = MibScalar
tnStatsApplianceHAState = _TnStatsApplianceHAState_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 12, 1, 11),
    _TnStatsApplianceHAState_Type()
)
tnStatsApplianceHAState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsApplianceHAState.setStatus("current")
_TnStatsApplianceSerialNumber_Type = DisplayString
_TnStatsApplianceSerialNumber_Object = MibScalar
tnStatsApplianceSerialNumber = _TnStatsApplianceSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 12, 1, 12),
    _TnStatsApplianceSerialNumber_Type()
)
tnStatsApplianceSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsApplianceSerialNumber.setStatus("current")
_TnStatsApplianceOSVersion_Type = DisplayString
_TnStatsApplianceOSVersion_Object = MibScalar
tnStatsApplianceOSVersion = _TnStatsApplianceOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 12, 1, 13),
    _TnStatsApplianceOSVersion_Type()
)
tnStatsApplianceOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsApplianceOSVersion.setStatus("current")
_TnStatsApplianceSoftwareVersion_Type = DisplayString
_TnStatsApplianceSoftwareVersion_Object = MibScalar
tnStatsApplianceSoftwareVersion = _TnStatsApplianceSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 12, 1, 14),
    _TnStatsApplianceSoftwareVersion_Type()
)
tnStatsApplianceSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsApplianceSoftwareVersion.setStatus("current")
_TnStatsApplianceConfigCreatedOn_Type = DisplayString
_TnStatsApplianceConfigCreatedOn_Object = MibScalar
tnStatsApplianceConfigCreatedOn = _TnStatsApplianceConfigCreatedOn_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 12, 1, 15),
    _TnStatsApplianceConfigCreatedOn_Type()
)
tnStatsApplianceConfigCreatedOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsApplianceConfigCreatedOn.setStatus("current")
_TnStatsEthernetInterfaces_ObjectIdentity = ObjectIdentity
tnStatsEthernetInterfaces = _TnStatsEthernetInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 13)
)
_TnStatsEthernetInterfaceScalars_ObjectIdentity = ObjectIdentity
tnStatsEthernetInterfaceScalars = _TnStatsEthernetInterfaceScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 13, 1)
)


class _TnStatsNumEthernetInterfaces_Type(Integer32):
    """Custom type tnStatsNumEthernetInterfaces based on Integer32"""
    defaultValue = 0


_TnStatsNumEthernetInterfaces_Type.__name__ = "Integer32"
_TnStatsNumEthernetInterfaces_Object = MibScalar
tnStatsNumEthernetInterfaces = _TnStatsNumEthernetInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 13, 1, 1),
    _TnStatsNumEthernetInterfaces_Type()
)
tnStatsNumEthernetInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsNumEthernetInterfaces.setStatus("current")
_TnStatsEthernetInterfaceTable_Object = MibTable
tnStatsEthernetInterfaceTable = _TnStatsEthernetInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 13, 2)
)
if mibBuilder.loadTexts:
    tnStatsEthernetInterfaceTable.setStatus("current")
_TnStatsEthernetInterfaceEntry_Object = MibTableRow
tnStatsEthernetInterfaceEntry = _TnStatsEthernetInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 13, 2, 1)
)
tnStatsEthernetInterfaceEntry.setIndexNames(
    (0, "TALARI-MIB", "tnStatsEthernetInterfaceIndex"),
)
if mibBuilder.loadTexts:
    tnStatsEthernetInterfaceEntry.setStatus("current")
_TnStatsEthernetInterfaceIndex_Type = Integer32
_TnStatsEthernetInterfaceIndex_Object = MibTableColumn
tnStatsEthernetInterfaceIndex = _TnStatsEthernetInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 13, 2, 1, 1),
    _TnStatsEthernetInterfaceIndex_Type()
)
tnStatsEthernetInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsEthernetInterfaceIndex.setStatus("current")
_TnStatsEthernetInterfaceIfIndex_Type = Integer32
_TnStatsEthernetInterfaceIfIndex_Object = MibTableColumn
tnStatsEthernetInterfaceIfIndex = _TnStatsEthernetInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 13, 2, 1, 2),
    _TnStatsEthernetInterfaceIfIndex_Type()
)
tnStatsEthernetInterfaceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsEthernetInterfaceIfIndex.setStatus("current")
_TnStatsEthernetInterfaceName_Type = DisplayString
_TnStatsEthernetInterfaceName_Object = MibTableColumn
tnStatsEthernetInterfaceName = _TnStatsEthernetInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 13, 2, 1, 3),
    _TnStatsEthernetInterfaceName_Type()
)
tnStatsEthernetInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsEthernetInterfaceName.setStatus("current")
_TnStatsEthernetInterfaceBytesSent_Type = Counter64
_TnStatsEthernetInterfaceBytesSent_Object = MibTableColumn
tnStatsEthernetInterfaceBytesSent = _TnStatsEthernetInterfaceBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 13, 2, 1, 4),
    _TnStatsEthernetInterfaceBytesSent_Type()
)
tnStatsEthernetInterfaceBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsEthernetInterfaceBytesSent.setStatus("current")
_TnStatsEthernetInterfacePacketsSent_Type = Counter64
_TnStatsEthernetInterfacePacketsSent_Object = MibTableColumn
tnStatsEthernetInterfacePacketsSent = _TnStatsEthernetInterfacePacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 13, 2, 1, 5),
    _TnStatsEthernetInterfacePacketsSent_Type()
)
tnStatsEthernetInterfacePacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsEthernetInterfacePacketsSent.setStatus("current")
_TnStatsEthernetInterfaceBytesReceived_Type = Counter64
_TnStatsEthernetInterfaceBytesReceived_Object = MibTableColumn
tnStatsEthernetInterfaceBytesReceived = _TnStatsEthernetInterfaceBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 13, 2, 1, 6),
    _TnStatsEthernetInterfaceBytesReceived_Type()
)
tnStatsEthernetInterfaceBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsEthernetInterfaceBytesReceived.setStatus("current")
_TnStatsEthernetInterfacePacketsReceived_Type = Counter64
_TnStatsEthernetInterfacePacketsReceived_Object = MibTableColumn
tnStatsEthernetInterfacePacketsReceived = _TnStatsEthernetInterfacePacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 13, 2, 1, 7),
    _TnStatsEthernetInterfacePacketsReceived_Type()
)
tnStatsEthernetInterfacePacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsEthernetInterfacePacketsReceived.setStatus("current")
_TnStatsEthernetInterfaceBytesDropped_Type = Counter64
_TnStatsEthernetInterfaceBytesDropped_Object = MibTableColumn
tnStatsEthernetInterfaceBytesDropped = _TnStatsEthernetInterfaceBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 13, 2, 1, 8),
    _TnStatsEthernetInterfaceBytesDropped_Type()
)
tnStatsEthernetInterfaceBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsEthernetInterfaceBytesDropped.setStatus("current")
_TnStatsEthernetInterfacePacketsDropped_Type = Counter64
_TnStatsEthernetInterfacePacketsDropped_Object = MibTableColumn
tnStatsEthernetInterfacePacketsDropped = _TnStatsEthernetInterfacePacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 13, 2, 1, 9),
    _TnStatsEthernetInterfacePacketsDropped_Type()
)
tnStatsEthernetInterfacePacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsEthernetInterfacePacketsDropped.setStatus("current")
_TnStatsRoutes_ObjectIdentity = ObjectIdentity
tnStatsRoutes = _TnStatsRoutes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 14)
)
_TnStatsRouteTable_Object = MibTable
tnStatsRouteTable = _TnStatsRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 14, 2)
)
if mibBuilder.loadTexts:
    tnStatsRouteTable.setStatus("obsolete")
_TnStatsRouteEntry_Object = MibTableRow
tnStatsRouteEntry = _TnStatsRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 14, 2, 1)
)
tnStatsRouteEntry.setIndexNames(
    (0, "TALARI-MIB", "tnStatsRouteIndex"),
)
if mibBuilder.loadTexts:
    tnStatsRouteEntry.setStatus("obsolete")
_TnStatsRouteIndex_Type = Integer32
_TnStatsRouteIndex_Object = MibTableColumn
tnStatsRouteIndex = _TnStatsRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 14, 2, 1, 1),
    _TnStatsRouteIndex_Type()
)
tnStatsRouteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsRouteIndex.setStatus("obsolete")
_TnStatsRouteID_Type = Integer32
_TnStatsRouteID_Object = MibTableColumn
tnStatsRouteID = _TnStatsRouteID_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 14, 2, 1, 2),
    _TnStatsRouteID_Type()
)
tnStatsRouteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsRouteID.setStatus("obsolete")
_TnStatsRouteHitCount_Type = Counter64
_TnStatsRouteHitCount_Object = MibTableColumn
tnStatsRouteHitCount = _TnStatsRouteHitCount_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 14, 2, 1, 3),
    _TnStatsRouteHitCount_Type()
)
tnStatsRouteHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsRouteHitCount.setStatus("obsolete")
_TnStatsRules_ObjectIdentity = ObjectIdentity
tnStatsRules = _TnStatsRules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 15)
)
_TnStatsRuleScalars_ObjectIdentity = ObjectIdentity
tnStatsRuleScalars = _TnStatsRuleScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 15, 1)
)


class _TnStatsNumRules_Type(Integer32):
    """Custom type tnStatsNumRules based on Integer32"""
    defaultValue = 0


_TnStatsNumRules_Type.__name__ = "Integer32"
_TnStatsNumRules_Object = MibScalar
tnStatsNumRules = _TnStatsNumRules_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 15, 1, 1),
    _TnStatsNumRules_Type()
)
tnStatsNumRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsNumRules.setStatus("current")
_TnStatsRuleTable_Object = MibTable
tnStatsRuleTable = _TnStatsRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 15, 2)
)
if mibBuilder.loadTexts:
    tnStatsRuleTable.setStatus("current")
_TnStatsRuleEntry_Object = MibTableRow
tnStatsRuleEntry = _TnStatsRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 15, 2, 1)
)
tnStatsRuleEntry.setIndexNames(
    (0, "TALARI-MIB", "tnStatsRuleIndex"),
)
if mibBuilder.loadTexts:
    tnStatsRuleEntry.setStatus("current")
_TnStatsRuleIndex_Type = Integer32
_TnStatsRuleIndex_Object = MibTableColumn
tnStatsRuleIndex = _TnStatsRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 15, 2, 1, 1),
    _TnStatsRuleIndex_Type()
)
tnStatsRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsRuleIndex.setStatus("current")
_TnStatsRuleID_Type = Integer32
_TnStatsRuleID_Object = MibTableColumn
tnStatsRuleID = _TnStatsRuleID_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 15, 2, 1, 2),
    _TnStatsRuleID_Type()
)
tnStatsRuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsRuleID.setStatus("current")
_TnStatsRuleApplicationName_Type = DisplayString
_TnStatsRuleApplicationName_Object = MibTableColumn
tnStatsRuleApplicationName = _TnStatsRuleApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 15, 2, 1, 3),
    _TnStatsRuleApplicationName_Type()
)
tnStatsRuleApplicationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsRuleApplicationName.setStatus("current")
_TnStatsRuleWANIngressHitCount_Type = Gauge32
_TnStatsRuleWANIngressHitCount_Object = MibTableColumn
tnStatsRuleWANIngressHitCount = _TnStatsRuleWANIngressHitCount_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 15, 2, 1, 4),
    _TnStatsRuleWANIngressHitCount_Type()
)
tnStatsRuleWANIngressHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsRuleWANIngressHitCount.setStatus("current")
_TnStatsRuleWANEgressHitCount_Type = Gauge32
_TnStatsRuleWANEgressHitCount_Object = MibTableColumn
tnStatsRuleWANEgressHitCount = _TnStatsRuleWANEgressHitCount_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 15, 2, 1, 5),
    _TnStatsRuleWANEgressHitCount_Type()
)
tnStatsRuleWANEgressHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsRuleWANEgressHitCount.setStatus("current")
_TnStatsRuleBytesSent_Type = Gauge32
_TnStatsRuleBytesSent_Object = MibTableColumn
tnStatsRuleBytesSent = _TnStatsRuleBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 15, 2, 1, 6),
    _TnStatsRuleBytesSent_Type()
)
tnStatsRuleBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsRuleBytesSent.setStatus("current")
_TnStatsRulePacketsSent_Type = Gauge32
_TnStatsRulePacketsSent_Object = MibTableColumn
tnStatsRulePacketsSent = _TnStatsRulePacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 15, 2, 1, 7),
    _TnStatsRulePacketsSent_Type()
)
tnStatsRulePacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsRulePacketsSent.setStatus("current")
_TnStatsRuleBytesReceived_Type = Gauge32
_TnStatsRuleBytesReceived_Object = MibTableColumn
tnStatsRuleBytesReceived = _TnStatsRuleBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 15, 2, 1, 8),
    _TnStatsRuleBytesReceived_Type()
)
tnStatsRuleBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsRuleBytesReceived.setStatus("current")
_TnStatsRulePacketsReceived_Type = Gauge32
_TnStatsRulePacketsReceived_Object = MibTableColumn
tnStatsRulePacketsReceived = _TnStatsRulePacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 15, 2, 1, 9),
    _TnStatsRulePacketsReceived_Type()
)
tnStatsRulePacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsRulePacketsReceived.setStatus("current")
_TnStatsRuleBytesDropped_Type = Gauge32
_TnStatsRuleBytesDropped_Object = MibTableColumn
tnStatsRuleBytesDropped = _TnStatsRuleBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 15, 2, 1, 10),
    _TnStatsRuleBytesDropped_Type()
)
tnStatsRuleBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsRuleBytesDropped.setStatus("current")
_TnStatsRulePacketsDropped_Type = Gauge32
_TnStatsRulePacketsDropped_Object = MibTableColumn
tnStatsRulePacketsDropped = _TnStatsRulePacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 15, 2, 1, 11),
    _TnStatsRulePacketsDropped_Type()
)
tnStatsRulePacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsRulePacketsDropped.setStatus("current")
_TnStatsRuleLastActiveNMinuteAgo_Type = TimeTicks
_TnStatsRuleLastActiveNMinuteAgo_Object = MibTableColumn
tnStatsRuleLastActiveNMinuteAgo = _TnStatsRuleLastActiveNMinuteAgo_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 15, 2, 1, 12),
    _TnStatsRuleLastActiveNMinuteAgo_Type()
)
tnStatsRuleLastActiveNMinuteAgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsRuleLastActiveNMinuteAgo.setStatus("current")
_TnStatsWANLinks_ObjectIdentity = ObjectIdentity
tnStatsWANLinks = _TnStatsWANLinks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 16)
)
_TnStatsWANLinkScalars_ObjectIdentity = ObjectIdentity
tnStatsWANLinkScalars = _TnStatsWANLinkScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 16, 1)
)


class _TnStatsNumWANLinks_Type(Integer32):
    """Custom type tnStatsNumWANLinks based on Integer32"""
    defaultValue = 0


_TnStatsNumWANLinks_Type.__name__ = "Integer32"
_TnStatsNumWANLinks_Object = MibScalar
tnStatsNumWANLinks = _TnStatsNumWANLinks_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 16, 1, 1),
    _TnStatsNumWANLinks_Type()
)
tnStatsNumWANLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsNumWANLinks.setStatus("current")
_TnStatsWANLinkTable_Object = MibTable
tnStatsWANLinkTable = _TnStatsWANLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 16, 2)
)
if mibBuilder.loadTexts:
    tnStatsWANLinkTable.setStatus("current")
_TnStatsWANLinkEntry_Object = MibTableRow
tnStatsWANLinkEntry = _TnStatsWANLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 16, 2, 1)
)
tnStatsWANLinkEntry.setIndexNames(
    (0, "TALARI-MIB", "tnStatsWANLinkIndex"),
)
if mibBuilder.loadTexts:
    tnStatsWANLinkEntry.setStatus("current")
_TnStatsWANLinkIndex_Type = Integer32
_TnStatsWANLinkIndex_Object = MibTableColumn
tnStatsWANLinkIndex = _TnStatsWANLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 16, 2, 1, 1),
    _TnStatsWANLinkIndex_Type()
)
tnStatsWANLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsWANLinkIndex.setStatus("current")
_TnStatsWANLinkID_Type = Integer32
_TnStatsWANLinkID_Object = MibTableColumn
tnStatsWANLinkID = _TnStatsWANLinkID_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 16, 2, 1, 2),
    _TnStatsWANLinkID_Type()
)
tnStatsWANLinkID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsWANLinkID.setStatus("current")
_TnStatsWANLinkName_Type = DisplayString
_TnStatsWANLinkName_Object = MibTableColumn
tnStatsWANLinkName = _TnStatsWANLinkName_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 16, 2, 1, 3),
    _TnStatsWANLinkName_Type()
)
tnStatsWANLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsWANLinkName.setStatus("current")


class _TnStatsWANLinkState_Type(Integer32):
    """Custom type tnStatsWANLinkState based on Integer32"""
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
          ("disabled", 1),
          ("dead", 2),
          ("bad", 3),
          ("good", 4))
    )


_TnStatsWANLinkState_Type.__name__ = "Integer32"
_TnStatsWANLinkState_Object = MibTableColumn
tnStatsWANLinkState = _TnStatsWANLinkState_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 16, 2, 1, 4),
    _TnStatsWANLinkState_Type()
)
tnStatsWANLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsWANLinkState.setStatus("current")
_TnStatsWANLinkBytesSent_Type = Counter64
_TnStatsWANLinkBytesSent_Object = MibTableColumn
tnStatsWANLinkBytesSent = _TnStatsWANLinkBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 16, 2, 1, 5),
    _TnStatsWANLinkBytesSent_Type()
)
tnStatsWANLinkBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsWANLinkBytesSent.setStatus("current")
_TnStatsWANLinkPacketsSent_Type = Counter64
_TnStatsWANLinkPacketsSent_Object = MibTableColumn
tnStatsWANLinkPacketsSent = _TnStatsWANLinkPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 16, 2, 1, 6),
    _TnStatsWANLinkPacketsSent_Type()
)
tnStatsWANLinkPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsWANLinkPacketsSent.setStatus("current")
_TnStatsWANLinkBytesReceived_Type = Counter64
_TnStatsWANLinkBytesReceived_Object = MibTableColumn
tnStatsWANLinkBytesReceived = _TnStatsWANLinkBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 16, 2, 1, 7),
    _TnStatsWANLinkBytesReceived_Type()
)
tnStatsWANLinkBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsWANLinkBytesReceived.setStatus("current")
_TnStatsWANLinkPacketsReceived_Type = Counter64
_TnStatsWANLinkPacketsReceived_Object = MibTableColumn
tnStatsWANLinkPacketsReceived = _TnStatsWANLinkPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 16, 2, 1, 8),
    _TnStatsWANLinkPacketsReceived_Type()
)
tnStatsWANLinkPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsWANLinkPacketsReceived.setStatus("current")
_TnStatsWANLinkBytesDropped_Type = Counter64
_TnStatsWANLinkBytesDropped_Object = MibTableColumn
tnStatsWANLinkBytesDropped = _TnStatsWANLinkBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 16, 2, 1, 9),
    _TnStatsWANLinkBytesDropped_Type()
)
tnStatsWANLinkBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsWANLinkBytesDropped.setStatus("current")
_TnStatsWANLinkPacketsDropped_Type = Counter64
_TnStatsWANLinkPacketsDropped_Object = MibTableColumn
tnStatsWANLinkPacketsDropped = _TnStatsWANLinkPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 16, 2, 1, 10),
    _TnStatsWANLinkPacketsDropped_Type()
)
tnStatsWANLinkPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsWANLinkPacketsDropped.setStatus("current")
_TnStatsConduits_ObjectIdentity = ObjectIdentity
tnStatsConduits = _TnStatsConduits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17)
)
_TnStatsConduitScalars_ObjectIdentity = ObjectIdentity
tnStatsConduitScalars = _TnStatsConduitScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 1)
)


class _TnStatsNumConduits_Type(Integer32):
    """Custom type tnStatsNumConduits based on Integer32"""
    defaultValue = 0


_TnStatsNumConduits_Type.__name__ = "Integer32"
_TnStatsNumConduits_Object = MibScalar
tnStatsNumConduits = _TnStatsNumConduits_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 1, 1),
    _TnStatsNumConduits_Type()
)
tnStatsNumConduits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsNumConduits.setStatus("current")
_TnStatsConduitTable_Object = MibTable
tnStatsConduitTable = _TnStatsConduitTable_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 2)
)
if mibBuilder.loadTexts:
    tnStatsConduitTable.setStatus("current")
_TnStatsConduitEntry_Object = MibTableRow
tnStatsConduitEntry = _TnStatsConduitEntry_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 2, 1)
)
tnStatsConduitEntry.setIndexNames(
    (0, "TALARI-MIB", "tnStatsConduitIndex"),
)
if mibBuilder.loadTexts:
    tnStatsConduitEntry.setStatus("current")
_TnStatsConduitIndex_Type = Integer32
_TnStatsConduitIndex_Object = MibTableColumn
tnStatsConduitIndex = _TnStatsConduitIndex_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 2, 1, 1),
    _TnStatsConduitIndex_Type()
)
tnStatsConduitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitIndex.setStatus("current")
_TnStatsConduitID_Type = Integer32
_TnStatsConduitID_Object = MibTableColumn
tnStatsConduitID = _TnStatsConduitID_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 2, 1, 2),
    _TnStatsConduitID_Type()
)
tnStatsConduitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitID.setStatus("current")
_TnStatsConduitName_Type = DisplayString
_TnStatsConduitName_Object = MibTableColumn
tnStatsConduitName = _TnStatsConduitName_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 2, 1, 3),
    _TnStatsConduitName_Type()
)
tnStatsConduitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitName.setStatus("current")


class _TnStatsConduitState_Type(Integer32):
    """Custom type tnStatsConduitState based on Integer32"""
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
          ("disabled", 1),
          ("dead", 2),
          ("bad", 3),
          ("good", 4))
    )


_TnStatsConduitState_Type.__name__ = "Integer32"
_TnStatsConduitState_Object = MibTableColumn
tnStatsConduitState = _TnStatsConduitState_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 2, 1, 4),
    _TnStatsConduitState_Type()
)
tnStatsConduitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitState.setStatus("current")
_TnStatsConduitBytesSent_Type = Counter64
_TnStatsConduitBytesSent_Object = MibTableColumn
tnStatsConduitBytesSent = _TnStatsConduitBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 2, 1, 5),
    _TnStatsConduitBytesSent_Type()
)
tnStatsConduitBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitBytesSent.setStatus("current")
_TnStatsConduitPacketsSent_Type = Counter64
_TnStatsConduitPacketsSent_Object = MibTableColumn
tnStatsConduitPacketsSent = _TnStatsConduitPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 2, 1, 6),
    _TnStatsConduitPacketsSent_Type()
)
tnStatsConduitPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitPacketsSent.setStatus("current")
_TnStatsConduitBytesReceived_Type = Counter64
_TnStatsConduitBytesReceived_Object = MibTableColumn
tnStatsConduitBytesReceived = _TnStatsConduitBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 2, 1, 7),
    _TnStatsConduitBytesReceived_Type()
)
tnStatsConduitBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitBytesReceived.setStatus("current")
_TnStatsConduitPacketsReceived_Type = Counter64
_TnStatsConduitPacketsReceived_Object = MibTableColumn
tnStatsConduitPacketsReceived = _TnStatsConduitPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 2, 1, 8),
    _TnStatsConduitPacketsReceived_Type()
)
tnStatsConduitPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitPacketsReceived.setStatus("current")
_TnStatsConduitBytesDropped_Type = Counter64
_TnStatsConduitBytesDropped_Object = MibTableColumn
tnStatsConduitBytesDropped = _TnStatsConduitBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 2, 1, 9),
    _TnStatsConduitBytesDropped_Type()
)
tnStatsConduitBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitBytesDropped.setStatus("obsolete")
_TnStatsConduitPacketsDropped_Type = Counter64
_TnStatsConduitPacketsDropped_Object = MibTableColumn
tnStatsConduitPacketsDropped = _TnStatsConduitPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 2, 1, 10),
    _TnStatsConduitPacketsDropped_Type()
)
tnStatsConduitPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitPacketsDropped.setStatus("obsolete")
_TnStatsConduitBOWTms_Type = Gauge32
_TnStatsConduitBOWTms_Object = MibTableColumn
tnStatsConduitBOWTms = _TnStatsConduitBOWTms_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 2, 1, 11),
    _TnStatsConduitBOWTms_Type()
)
tnStatsConduitBOWTms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitBOWTms.setStatus("obsolete")
_TnStatsConduitJitterms_Type = Gauge32
_TnStatsConduitJitterms_Object = MibTableColumn
tnStatsConduitJitterms = _TnStatsConduitJitterms_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 2, 1, 12),
    _TnStatsConduitJitterms_Type()
)
tnStatsConduitJitterms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitJitterms.setStatus("obsolete")
_TnStatsConduitNumPaths_Type = Integer32
_TnStatsConduitNumPaths_Object = MibTableColumn
tnStatsConduitNumPaths = _TnStatsConduitNumPaths_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 2, 1, 13),
    _TnStatsConduitNumPaths_Type()
)
tnStatsConduitNumPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitNumPaths.setStatus("current")
_TnStatsConduitNumRules_Type = Integer32
_TnStatsConduitNumRules_Object = MibTableColumn
tnStatsConduitNumRules = _TnStatsConduitNumRules_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 2, 1, 14),
    _TnStatsConduitNumRules_Type()
)
tnStatsConduitNumRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitNumRules.setStatus("current")
_TnStatsConduitPacketsLost_Type = Counter64
_TnStatsConduitPacketsLost_Object = MibTableColumn
tnStatsConduitPacketsLost = _TnStatsConduitPacketsLost_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 2, 1, 15),
    _TnStatsConduitPacketsLost_Type()
)
tnStatsConduitPacketsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitPacketsLost.setStatus("obsolete")
_TnStatsConduitSendBytesDropped_Type = Counter64
_TnStatsConduitSendBytesDropped_Object = MibTableColumn
tnStatsConduitSendBytesDropped = _TnStatsConduitSendBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 2, 1, 16),
    _TnStatsConduitSendBytesDropped_Type()
)
tnStatsConduitSendBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitSendBytesDropped.setStatus("current")
_TnStatsConduitSendPacketsDropped_Type = Counter64
_TnStatsConduitSendPacketsDropped_Object = MibTableColumn
tnStatsConduitSendPacketsDropped = _TnStatsConduitSendPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 2, 1, 17),
    _TnStatsConduitSendPacketsDropped_Type()
)
tnStatsConduitSendPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitSendPacketsDropped.setStatus("current")
_TnStatsConduitSendPacketsLost_Type = Counter64
_TnStatsConduitSendPacketsLost_Object = MibTableColumn
tnStatsConduitSendPacketsLost = _TnStatsConduitSendPacketsLost_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 2, 1, 18),
    _TnStatsConduitSendPacketsLost_Type()
)
tnStatsConduitSendPacketsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitSendPacketsLost.setStatus("current")
_TnStatsConduitSendPacketsOOO_Type = Counter64
_TnStatsConduitSendPacketsOOO_Object = MibTableColumn
tnStatsConduitSendPacketsOOO = _TnStatsConduitSendPacketsOOO_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 2, 1, 19),
    _TnStatsConduitSendPacketsOOO_Type()
)
tnStatsConduitSendPacketsOOO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitSendPacketsOOO.setStatus("current")
_TnStatsConduitSendBOWTms_Type = Gauge32
_TnStatsConduitSendBOWTms_Object = MibTableColumn
tnStatsConduitSendBOWTms = _TnStatsConduitSendBOWTms_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 2, 1, 20),
    _TnStatsConduitSendBOWTms_Type()
)
tnStatsConduitSendBOWTms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitSendBOWTms.setStatus("current")
_TnStatsConduitSendJitterms_Type = Gauge32
_TnStatsConduitSendJitterms_Object = MibTableColumn
tnStatsConduitSendJitterms = _TnStatsConduitSendJitterms_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 2, 1, 21),
    _TnStatsConduitSendJitterms_Type()
)
tnStatsConduitSendJitterms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitSendJitterms.setStatus("current")
_TnStatsConduitReceiveBytesDropped_Type = Counter64
_TnStatsConduitReceiveBytesDropped_Object = MibTableColumn
tnStatsConduitReceiveBytesDropped = _TnStatsConduitReceiveBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 2, 1, 22),
    _TnStatsConduitReceiveBytesDropped_Type()
)
tnStatsConduitReceiveBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitReceiveBytesDropped.setStatus("current")
_TnStatsConduitReceivePacketsDropped_Type = Counter64
_TnStatsConduitReceivePacketsDropped_Object = MibTableColumn
tnStatsConduitReceivePacketsDropped = _TnStatsConduitReceivePacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 2, 1, 23),
    _TnStatsConduitReceivePacketsDropped_Type()
)
tnStatsConduitReceivePacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitReceivePacketsDropped.setStatus("current")
_TnStatsConduitReceivePacketsLost_Type = Counter64
_TnStatsConduitReceivePacketsLost_Object = MibTableColumn
tnStatsConduitReceivePacketsLost = _TnStatsConduitReceivePacketsLost_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 2, 1, 24),
    _TnStatsConduitReceivePacketsLost_Type()
)
tnStatsConduitReceivePacketsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitReceivePacketsLost.setStatus("current")
_TnStatsConduitReceivePacketsOOO_Type = Counter64
_TnStatsConduitReceivePacketsOOO_Object = MibTableColumn
tnStatsConduitReceivePacketsOOO = _TnStatsConduitReceivePacketsOOO_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 2, 1, 25),
    _TnStatsConduitReceivePacketsOOO_Type()
)
tnStatsConduitReceivePacketsOOO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitReceivePacketsOOO.setStatus("current")
_TnStatsConduitReceiveBOWTms_Type = Gauge32
_TnStatsConduitReceiveBOWTms_Object = MibTableColumn
tnStatsConduitReceiveBOWTms = _TnStatsConduitReceiveBOWTms_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 2, 1, 26),
    _TnStatsConduitReceiveBOWTms_Type()
)
tnStatsConduitReceiveBOWTms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitReceiveBOWTms.setStatus("current")
_TnStatsConduitReceiveJitterms_Type = Gauge32
_TnStatsConduitReceiveJitterms_Object = MibTableColumn
tnStatsConduitReceiveJitterms = _TnStatsConduitReceiveJitterms_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 2, 1, 27),
    _TnStatsConduitReceiveJitterms_Type()
)
tnStatsConduitReceiveJitterms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitReceiveJitterms.setStatus("current")
_TnStatsConduitPaths_ObjectIdentity = ObjectIdentity
tnStatsConduitPaths = _TnStatsConduitPaths_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 3)
)
_TnStatsConduitPathTable_Object = MibTable
tnStatsConduitPathTable = _TnStatsConduitPathTable_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 3, 1)
)
if mibBuilder.loadTexts:
    tnStatsConduitPathTable.setStatus("current")
_TnStatsConduitPathEntry_Object = MibTableRow
tnStatsConduitPathEntry = _TnStatsConduitPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 3, 1, 1)
)
tnStatsConduitPathEntry.setIndexNames(
    (0, "TALARI-MIB", "tnStatsConduitPathConduitIndex"),
    (0, "TALARI-MIB", "tnStatsConduitPathPathIndex"),
)
if mibBuilder.loadTexts:
    tnStatsConduitPathEntry.setStatus("current")
_TnStatsConduitPathConduitIndex_Type = Integer32
_TnStatsConduitPathConduitIndex_Object = MibTableColumn
tnStatsConduitPathConduitIndex = _TnStatsConduitPathConduitIndex_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 3, 1, 1, 1),
    _TnStatsConduitPathConduitIndex_Type()
)
tnStatsConduitPathConduitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitPathConduitIndex.setStatus("current")
_TnStatsConduitPathPathIndex_Type = Integer32
_TnStatsConduitPathPathIndex_Object = MibTableColumn
tnStatsConduitPathPathIndex = _TnStatsConduitPathPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 3, 1, 1, 2),
    _TnStatsConduitPathPathIndex_Type()
)
tnStatsConduitPathPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitPathPathIndex.setStatus("current")
_TnStatsConduitPathConduitID_Type = Integer32
_TnStatsConduitPathConduitID_Object = MibTableColumn
tnStatsConduitPathConduitID = _TnStatsConduitPathConduitID_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 3, 1, 1, 3),
    _TnStatsConduitPathConduitID_Type()
)
tnStatsConduitPathConduitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitPathConduitID.setStatus("current")
_TnStatsConduitPathPathID_Type = Integer32
_TnStatsConduitPathPathID_Object = MibTableColumn
tnStatsConduitPathPathID = _TnStatsConduitPathPathID_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 3, 1, 1, 4),
    _TnStatsConduitPathPathID_Type()
)
tnStatsConduitPathPathID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitPathPathID.setStatus("current")
_TnStatsConduitPathName_Type = DisplayString
_TnStatsConduitPathName_Object = MibTableColumn
tnStatsConduitPathName = _TnStatsConduitPathName_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 3, 1, 1, 5),
    _TnStatsConduitPathName_Type()
)
tnStatsConduitPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitPathName.setStatus("current")


class _TnStatsConduitPathState_Type(Integer32):
    """Custom type tnStatsConduitPathState based on Integer32"""
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
          ("disabled", 1),
          ("dead", 2),
          ("bad", 3),
          ("good", 4))
    )


_TnStatsConduitPathState_Type.__name__ = "Integer32"
_TnStatsConduitPathState_Object = MibTableColumn
tnStatsConduitPathState = _TnStatsConduitPathState_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 3, 1, 1, 6),
    _TnStatsConduitPathState_Type()
)
tnStatsConduitPathState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitPathState.setStatus("current")
_TnStatsConduitPathBytesSent_Type = Counter64
_TnStatsConduitPathBytesSent_Object = MibTableColumn
tnStatsConduitPathBytesSent = _TnStatsConduitPathBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 3, 1, 1, 7),
    _TnStatsConduitPathBytesSent_Type()
)
tnStatsConduitPathBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitPathBytesSent.setStatus("current")
_TnStatsConduitPathPacketsSent_Type = Counter64
_TnStatsConduitPathPacketsSent_Object = MibTableColumn
tnStatsConduitPathPacketsSent = _TnStatsConduitPathPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 3, 1, 1, 8),
    _TnStatsConduitPathPacketsSent_Type()
)
tnStatsConduitPathPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitPathPacketsSent.setStatus("current")
_TnStatsConduitPathBytesReceived_Type = Counter64
_TnStatsConduitPathBytesReceived_Object = MibTableColumn
tnStatsConduitPathBytesReceived = _TnStatsConduitPathBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 3, 1, 1, 9),
    _TnStatsConduitPathBytesReceived_Type()
)
tnStatsConduitPathBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitPathBytesReceived.setStatus("current")
_TnStatsConduitPathPacketsReceived_Type = Counter64
_TnStatsConduitPathPacketsReceived_Object = MibTableColumn
tnStatsConduitPathPacketsReceived = _TnStatsConduitPathPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 3, 1, 1, 10),
    _TnStatsConduitPathPacketsReceived_Type()
)
tnStatsConduitPathPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitPathPacketsReceived.setStatus("current")
_TnStatsConduitPathBytesDropped_Type = Counter64
_TnStatsConduitPathBytesDropped_Object = MibTableColumn
tnStatsConduitPathBytesDropped = _TnStatsConduitPathBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 3, 1, 1, 11),
    _TnStatsConduitPathBytesDropped_Type()
)
tnStatsConduitPathBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitPathBytesDropped.setStatus("obsolete")
_TnStatsConduitPathPacketsDropped_Type = Counter64
_TnStatsConduitPathPacketsDropped_Object = MibTableColumn
tnStatsConduitPathPacketsDropped = _TnStatsConduitPathPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 3, 1, 1, 12),
    _TnStatsConduitPathPacketsDropped_Type()
)
tnStatsConduitPathPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitPathPacketsDropped.setStatus("obsolete")
_TnStatsConduitPathBOWTms_Type = Gauge32
_TnStatsConduitPathBOWTms_Object = MibTableColumn
tnStatsConduitPathBOWTms = _TnStatsConduitPathBOWTms_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 3, 1, 1, 13),
    _TnStatsConduitPathBOWTms_Type()
)
tnStatsConduitPathBOWTms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitPathBOWTms.setStatus("current")
_TnStatsConduitPathJitterms_Type = Gauge32
_TnStatsConduitPathJitterms_Object = MibTableColumn
tnStatsConduitPathJitterms = _TnStatsConduitPathJitterms_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 3, 1, 1, 14),
    _TnStatsConduitPathJitterms_Type()
)
tnStatsConduitPathJitterms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitPathJitterms.setStatus("current")
_TnStatsConduitPathPacketsLost_Type = Counter64
_TnStatsConduitPathPacketsLost_Object = MibTableColumn
tnStatsConduitPathPacketsLost = _TnStatsConduitPathPacketsLost_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 3, 1, 1, 15),
    _TnStatsConduitPathPacketsLost_Type()
)
tnStatsConduitPathPacketsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitPathPacketsLost.setStatus("current")
_TnStatsConduitPathPacketsOOO_Type = Counter64
_TnStatsConduitPathPacketsOOO_Object = MibTableColumn
tnStatsConduitPathPacketsOOO = _TnStatsConduitPathPacketsOOO_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 3, 1, 1, 16),
    _TnStatsConduitPathPacketsOOO_Type()
)
tnStatsConduitPathPacketsOOO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitPathPacketsOOO.setStatus("current")
_TnStatsConduitClasses_ObjectIdentity = ObjectIdentity
tnStatsConduitClasses = _TnStatsConduitClasses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 4)
)
_TnStatsConduitClassTable_Object = MibTable
tnStatsConduitClassTable = _TnStatsConduitClassTable_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 4, 1)
)
if mibBuilder.loadTexts:
    tnStatsConduitClassTable.setStatus("current")
_TnStatsConduitClassEntry_Object = MibTableRow
tnStatsConduitClassEntry = _TnStatsConduitClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 4, 1, 1)
)
tnStatsConduitClassEntry.setIndexNames(
    (0, "TALARI-MIB", "tnStatsConduitClassConduitIndex"),
    (0, "TALARI-MIB", "tnStatsConduitClassClassIndex"),
)
if mibBuilder.loadTexts:
    tnStatsConduitClassEntry.setStatus("current")
_TnStatsConduitClassConduitIndex_Type = Integer32
_TnStatsConduitClassConduitIndex_Object = MibTableColumn
tnStatsConduitClassConduitIndex = _TnStatsConduitClassConduitIndex_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 4, 1, 1, 1),
    _TnStatsConduitClassConduitIndex_Type()
)
tnStatsConduitClassConduitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitClassConduitIndex.setStatus("current")
_TnStatsConduitClassClassIndex_Type = Integer32
_TnStatsConduitClassClassIndex_Object = MibTableColumn
tnStatsConduitClassClassIndex = _TnStatsConduitClassClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 4, 1, 1, 2),
    _TnStatsConduitClassClassIndex_Type()
)
tnStatsConduitClassClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitClassClassIndex.setStatus("current")
_TnStatsConduitClassConduitID_Type = Integer32
_TnStatsConduitClassConduitID_Object = MibTableColumn
tnStatsConduitClassConduitID = _TnStatsConduitClassConduitID_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 4, 1, 1, 3),
    _TnStatsConduitClassConduitID_Type()
)
tnStatsConduitClassConduitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitClassConduitID.setStatus("current")
_TnStatsConduitClassClassID_Type = Integer32
_TnStatsConduitClassClassID_Object = MibTableColumn
tnStatsConduitClassClassID = _TnStatsConduitClassClassID_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 4, 1, 1, 4),
    _TnStatsConduitClassClassID_Type()
)
tnStatsConduitClassClassID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitClassClassID.setStatus("current")
_TnStatsConduitClassName_Type = DisplayString
_TnStatsConduitClassName_Object = MibTableColumn
tnStatsConduitClassName = _TnStatsConduitClassName_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 4, 1, 1, 5),
    _TnStatsConduitClassName_Type()
)
tnStatsConduitClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitClassName.setStatus("current")


class _TnStatsConduitClassType_Type(Integer32):
    """Custom type tnStatsConduitClassType based on Integer32"""
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
        *(("realtime", 1),
          ("interactive", 2),
          ("bulk", 3),
          ("unknown", 4))
    )


_TnStatsConduitClassType_Type.__name__ = "Integer32"
_TnStatsConduitClassType_Object = MibTableColumn
tnStatsConduitClassType = _TnStatsConduitClassType_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 4, 1, 1, 6),
    _TnStatsConduitClassType_Type()
)
tnStatsConduitClassType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitClassType.setStatus("current")
_TnStatsConduitClassBytesSent_Type = Counter64
_TnStatsConduitClassBytesSent_Object = MibTableColumn
tnStatsConduitClassBytesSent = _TnStatsConduitClassBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 4, 1, 1, 7),
    _TnStatsConduitClassBytesSent_Type()
)
tnStatsConduitClassBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitClassBytesSent.setStatus("current")
_TnStatsConduitClassPacketsSent_Type = Counter64
_TnStatsConduitClassPacketsSent_Object = MibTableColumn
tnStatsConduitClassPacketsSent = _TnStatsConduitClassPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 4, 1, 1, 8),
    _TnStatsConduitClassPacketsSent_Type()
)
tnStatsConduitClassPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitClassPacketsSent.setStatus("current")
_TnStatsConduitClassBytesPending_Type = Counter64
_TnStatsConduitClassBytesPending_Object = MibTableColumn
tnStatsConduitClassBytesPending = _TnStatsConduitClassBytesPending_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 4, 1, 1, 9),
    _TnStatsConduitClassBytesPending_Type()
)
tnStatsConduitClassBytesPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitClassBytesPending.setStatus("current")
_TnStatsConduitClassPacketsPending_Type = Counter64
_TnStatsConduitClassPacketsPending_Object = MibTableColumn
tnStatsConduitClassPacketsPending = _TnStatsConduitClassPacketsPending_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 4, 1, 1, 10),
    _TnStatsConduitClassPacketsPending_Type()
)
tnStatsConduitClassPacketsPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitClassPacketsPending.setStatus("current")
_TnStatsConduitClassBytesDropped_Type = Counter64
_TnStatsConduitClassBytesDropped_Object = MibTableColumn
tnStatsConduitClassBytesDropped = _TnStatsConduitClassBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 4, 1, 1, 11),
    _TnStatsConduitClassBytesDropped_Type()
)
tnStatsConduitClassBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitClassBytesDropped.setStatus("current")
_TnStatsConduitClassPacketsDropped_Type = Counter64
_TnStatsConduitClassPacketsDropped_Object = MibTableColumn
tnStatsConduitClassPacketsDropped = _TnStatsConduitClassPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 4, 1, 1, 12),
    _TnStatsConduitClassPacketsDropped_Type()
)
tnStatsConduitClassPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitClassPacketsDropped.setStatus("current")
_TnStatsConduitRules_ObjectIdentity = ObjectIdentity
tnStatsConduitRules = _TnStatsConduitRules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 5)
)
_TnStatsConduitRuleTable_Object = MibTable
tnStatsConduitRuleTable = _TnStatsConduitRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 5, 1)
)
if mibBuilder.loadTexts:
    tnStatsConduitRuleTable.setStatus("current")
_TnStatsConduitRuleEntry_Object = MibTableRow
tnStatsConduitRuleEntry = _TnStatsConduitRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 5, 1, 1)
)
tnStatsConduitRuleEntry.setIndexNames(
    (0, "TALARI-MIB", "tnStatsConduitRuleConduitIndex"),
    (0, "TALARI-MIB", "tnStatsConduitRuleRuleIndex"),
)
if mibBuilder.loadTexts:
    tnStatsConduitRuleEntry.setStatus("current")
_TnStatsConduitRuleConduitIndex_Type = Integer32
_TnStatsConduitRuleConduitIndex_Object = MibTableColumn
tnStatsConduitRuleConduitIndex = _TnStatsConduitRuleConduitIndex_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 5, 1, 1, 1),
    _TnStatsConduitRuleConduitIndex_Type()
)
tnStatsConduitRuleConduitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitRuleConduitIndex.setStatus("current")
_TnStatsConduitRuleRuleIndex_Type = Integer32
_TnStatsConduitRuleRuleIndex_Object = MibTableColumn
tnStatsConduitRuleRuleIndex = _TnStatsConduitRuleRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 5, 1, 1, 2),
    _TnStatsConduitRuleRuleIndex_Type()
)
tnStatsConduitRuleRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitRuleRuleIndex.setStatus("current")
_TnStatsConduitRuleConduitID_Type = Integer32
_TnStatsConduitRuleConduitID_Object = MibTableColumn
tnStatsConduitRuleConduitID = _TnStatsConduitRuleConduitID_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 5, 1, 1, 3),
    _TnStatsConduitRuleConduitID_Type()
)
tnStatsConduitRuleConduitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitRuleConduitID.setStatus("current")
_TnStatsConduitRuleRuleID_Type = Integer32
_TnStatsConduitRuleRuleID_Object = MibTableColumn
tnStatsConduitRuleRuleID = _TnStatsConduitRuleRuleID_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 5, 1, 1, 4),
    _TnStatsConduitRuleRuleID_Type()
)
tnStatsConduitRuleRuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitRuleRuleID.setStatus("current")
_TnStatsConduitRuleGlobalRuleIndex_Type = Integer32
_TnStatsConduitRuleGlobalRuleIndex_Object = MibTableColumn
tnStatsConduitRuleGlobalRuleIndex = _TnStatsConduitRuleGlobalRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 5, 1, 1, 5),
    _TnStatsConduitRuleGlobalRuleIndex_Type()
)
tnStatsConduitRuleGlobalRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitRuleGlobalRuleIndex.setStatus("current")
_TnStatsConduitRuleApplicationName_Type = DisplayString
_TnStatsConduitRuleApplicationName_Object = MibTableColumn
tnStatsConduitRuleApplicationName = _TnStatsConduitRuleApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 5, 1, 1, 6),
    _TnStatsConduitRuleApplicationName_Type()
)
tnStatsConduitRuleApplicationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitRuleApplicationName.setStatus("current")
_TnStatsConduitRuleWANIngressHitCount_Type = Gauge32
_TnStatsConduitRuleWANIngressHitCount_Object = MibTableColumn
tnStatsConduitRuleWANIngressHitCount = _TnStatsConduitRuleWANIngressHitCount_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 5, 1, 1, 7),
    _TnStatsConduitRuleWANIngressHitCount_Type()
)
tnStatsConduitRuleWANIngressHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitRuleWANIngressHitCount.setStatus("current")
_TnStatsConduitRuleWANEgressHitCount_Type = Gauge32
_TnStatsConduitRuleWANEgressHitCount_Object = MibTableColumn
tnStatsConduitRuleWANEgressHitCount = _TnStatsConduitRuleWANEgressHitCount_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 5, 1, 1, 8),
    _TnStatsConduitRuleWANEgressHitCount_Type()
)
tnStatsConduitRuleWANEgressHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitRuleWANEgressHitCount.setStatus("current")
_TnStatsConduitRuleBytesSent_Type = Gauge32
_TnStatsConduitRuleBytesSent_Object = MibTableColumn
tnStatsConduitRuleBytesSent = _TnStatsConduitRuleBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 5, 1, 1, 9),
    _TnStatsConduitRuleBytesSent_Type()
)
tnStatsConduitRuleBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitRuleBytesSent.setStatus("current")
_TnStatsConduitRulePacketsSent_Type = Gauge32
_TnStatsConduitRulePacketsSent_Object = MibTableColumn
tnStatsConduitRulePacketsSent = _TnStatsConduitRulePacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 5, 1, 1, 10),
    _TnStatsConduitRulePacketsSent_Type()
)
tnStatsConduitRulePacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitRulePacketsSent.setStatus("current")
_TnStatsConduitRuleBytesReceived_Type = Gauge32
_TnStatsConduitRuleBytesReceived_Object = MibTableColumn
tnStatsConduitRuleBytesReceived = _TnStatsConduitRuleBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 5, 1, 1, 11),
    _TnStatsConduitRuleBytesReceived_Type()
)
tnStatsConduitRuleBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitRuleBytesReceived.setStatus("current")
_TnStatsConduitRulePacketsReceived_Type = Gauge32
_TnStatsConduitRulePacketsReceived_Object = MibTableColumn
tnStatsConduitRulePacketsReceived = _TnStatsConduitRulePacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 5, 1, 1, 12),
    _TnStatsConduitRulePacketsReceived_Type()
)
tnStatsConduitRulePacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitRulePacketsReceived.setStatus("current")
_TnStatsConduitRuleBytesDropped_Type = Gauge32
_TnStatsConduitRuleBytesDropped_Object = MibTableColumn
tnStatsConduitRuleBytesDropped = _TnStatsConduitRuleBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 5, 1, 1, 13),
    _TnStatsConduitRuleBytesDropped_Type()
)
tnStatsConduitRuleBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitRuleBytesDropped.setStatus("current")
_TnStatsConduitRulePacketsDropped_Type = Gauge32
_TnStatsConduitRulePacketsDropped_Object = MibTableColumn
tnStatsConduitRulePacketsDropped = _TnStatsConduitRulePacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 5, 1, 1, 14),
    _TnStatsConduitRulePacketsDropped_Type()
)
tnStatsConduitRulePacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitRulePacketsDropped.setStatus("current")
_TnStatsConduitRuleLastActiveNMinuteAgo_Type = TimeTicks
_TnStatsConduitRuleLastActiveNMinuteAgo_Object = MibTableColumn
tnStatsConduitRuleLastActiveNMinuteAgo = _TnStatsConduitRuleLastActiveNMinuteAgo_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 17, 5, 1, 1, 15),
    _TnStatsConduitRuleLastActiveNMinuteAgo_Type()
)
tnStatsConduitRuleLastActiveNMinuteAgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsConduitRuleLastActiveNMinuteAgo.setStatus("current")
_TnStatsInternet_ObjectIdentity = ObjectIdentity
tnStatsInternet = _TnStatsInternet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 18)
)
_TnStatsInternetScalars_ObjectIdentity = ObjectIdentity
tnStatsInternetScalars = _TnStatsInternetScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 18, 1)
)


class _TnStatsInternetBytesSent_Type(Counter64):
    """Custom type tnStatsInternetBytesSent based on Counter64"""
    defaultValue = 0


_TnStatsInternetBytesSent_Type.__name__ = "Counter64"
_TnStatsInternetBytesSent_Object = MibScalar
tnStatsInternetBytesSent = _TnStatsInternetBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 18, 1, 1),
    _TnStatsInternetBytesSent_Type()
)
tnStatsInternetBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsInternetBytesSent.setStatus("current")


class _TnStatsInternetPacketsSent_Type(Counter64):
    """Custom type tnStatsInternetPacketsSent based on Counter64"""
    defaultValue = 0


_TnStatsInternetPacketsSent_Type.__name__ = "Counter64"
_TnStatsInternetPacketsSent_Object = MibScalar
tnStatsInternetPacketsSent = _TnStatsInternetPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 18, 1, 2),
    _TnStatsInternetPacketsSent_Type()
)
tnStatsInternetPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsInternetPacketsSent.setStatus("current")


class _TnStatsInternetBytesReceived_Type(Counter64):
    """Custom type tnStatsInternetBytesReceived based on Counter64"""
    defaultValue = 0


_TnStatsInternetBytesReceived_Type.__name__ = "Counter64"
_TnStatsInternetBytesReceived_Object = MibScalar
tnStatsInternetBytesReceived = _TnStatsInternetBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 18, 1, 3),
    _TnStatsInternetBytesReceived_Type()
)
tnStatsInternetBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsInternetBytesReceived.setStatus("current")


class _TnStatsInternetPacketsReceived_Type(Counter64):
    """Custom type tnStatsInternetPacketsReceived based on Counter64"""
    defaultValue = 0


_TnStatsInternetPacketsReceived_Type.__name__ = "Counter64"
_TnStatsInternetPacketsReceived_Object = MibScalar
tnStatsInternetPacketsReceived = _TnStatsInternetPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 18, 1, 4),
    _TnStatsInternetPacketsReceived_Type()
)
tnStatsInternetPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsInternetPacketsReceived.setStatus("current")


class _TnStatsInternetBytesDropped_Type(Counter64):
    """Custom type tnStatsInternetBytesDropped based on Counter64"""
    defaultValue = 0


_TnStatsInternetBytesDropped_Type.__name__ = "Counter64"
_TnStatsInternetBytesDropped_Object = MibScalar
tnStatsInternetBytesDropped = _TnStatsInternetBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 18, 1, 5),
    _TnStatsInternetBytesDropped_Type()
)
tnStatsInternetBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsInternetBytesDropped.setStatus("current")


class _TnStatsInternetPacketsDropped_Type(Counter64):
    """Custom type tnStatsInternetPacketsDropped based on Counter64"""
    defaultValue = 0


_TnStatsInternetPacketsDropped_Type.__name__ = "Counter64"
_TnStatsInternetPacketsDropped_Object = MibScalar
tnStatsInternetPacketsDropped = _TnStatsInternetPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 18, 1, 6),
    _TnStatsInternetPacketsDropped_Type()
)
tnStatsInternetPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsInternetPacketsDropped.setStatus("current")


class _TnStatsInternetNumRules_Type(Integer32):
    """Custom type tnStatsInternetNumRules based on Integer32"""
    defaultValue = 0


_TnStatsInternetNumRules_Type.__name__ = "Integer32"
_TnStatsInternetNumRules_Object = MibScalar
tnStatsInternetNumRules = _TnStatsInternetNumRules_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 18, 1, 7),
    _TnStatsInternetNumRules_Type()
)
tnStatsInternetNumRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsInternetNumRules.setStatus("current")
_TnStatsInternetRuleTable_Object = MibTable
tnStatsInternetRuleTable = _TnStatsInternetRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 18, 2)
)
if mibBuilder.loadTexts:
    tnStatsInternetRuleTable.setStatus("current")
_TnStatsInternetRuleEntry_Object = MibTableRow
tnStatsInternetRuleEntry = _TnStatsInternetRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 18, 2, 1)
)
tnStatsInternetRuleEntry.setIndexNames(
    (0, "TALARI-MIB", "tnStatsInternetRuleIndex"),
)
if mibBuilder.loadTexts:
    tnStatsInternetRuleEntry.setStatus("current")
_TnStatsInternetRuleIndex_Type = Integer32
_TnStatsInternetRuleIndex_Object = MibTableColumn
tnStatsInternetRuleIndex = _TnStatsInternetRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 18, 2, 1, 1),
    _TnStatsInternetRuleIndex_Type()
)
tnStatsInternetRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsInternetRuleIndex.setStatus("current")
_TnStatsInternetRuleID_Type = Integer32
_TnStatsInternetRuleID_Object = MibTableColumn
tnStatsInternetRuleID = _TnStatsInternetRuleID_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 18, 2, 1, 2),
    _TnStatsInternetRuleID_Type()
)
tnStatsInternetRuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsInternetRuleID.setStatus("current")
_TnStatsInternetRuleGlobalRuleIndex_Type = Integer32
_TnStatsInternetRuleGlobalRuleIndex_Object = MibTableColumn
tnStatsInternetRuleGlobalRuleIndex = _TnStatsInternetRuleGlobalRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 18, 2, 1, 3),
    _TnStatsInternetRuleGlobalRuleIndex_Type()
)
tnStatsInternetRuleGlobalRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsInternetRuleGlobalRuleIndex.setStatus("current")
_TnStatsInternetRuleApplicationName_Type = DisplayString
_TnStatsInternetRuleApplicationName_Object = MibTableColumn
tnStatsInternetRuleApplicationName = _TnStatsInternetRuleApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 18, 2, 1, 4),
    _TnStatsInternetRuleApplicationName_Type()
)
tnStatsInternetRuleApplicationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsInternetRuleApplicationName.setStatus("current")
_TnStatsInternetRuleWANIngressHitCount_Type = Gauge32
_TnStatsInternetRuleWANIngressHitCount_Object = MibTableColumn
tnStatsInternetRuleWANIngressHitCount = _TnStatsInternetRuleWANIngressHitCount_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 18, 2, 1, 5),
    _TnStatsInternetRuleWANIngressHitCount_Type()
)
tnStatsInternetRuleWANIngressHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsInternetRuleWANIngressHitCount.setStatus("current")
_TnStatsInternetRuleWANEgressHitCount_Type = Gauge32
_TnStatsInternetRuleWANEgressHitCount_Object = MibTableColumn
tnStatsInternetRuleWANEgressHitCount = _TnStatsInternetRuleWANEgressHitCount_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 18, 2, 1, 6),
    _TnStatsInternetRuleWANEgressHitCount_Type()
)
tnStatsInternetRuleWANEgressHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsInternetRuleWANEgressHitCount.setStatus("current")
_TnStatsInternetRuleBytesSent_Type = Gauge32
_TnStatsInternetRuleBytesSent_Object = MibTableColumn
tnStatsInternetRuleBytesSent = _TnStatsInternetRuleBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 18, 2, 1, 7),
    _TnStatsInternetRuleBytesSent_Type()
)
tnStatsInternetRuleBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsInternetRuleBytesSent.setStatus("current")
_TnStatsInternetRulePacketsSent_Type = Gauge32
_TnStatsInternetRulePacketsSent_Object = MibTableColumn
tnStatsInternetRulePacketsSent = _TnStatsInternetRulePacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 18, 2, 1, 8),
    _TnStatsInternetRulePacketsSent_Type()
)
tnStatsInternetRulePacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsInternetRulePacketsSent.setStatus("current")
_TnStatsInternetRuleBytesReceived_Type = Gauge32
_TnStatsInternetRuleBytesReceived_Object = MibTableColumn
tnStatsInternetRuleBytesReceived = _TnStatsInternetRuleBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 18, 2, 1, 9),
    _TnStatsInternetRuleBytesReceived_Type()
)
tnStatsInternetRuleBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsInternetRuleBytesReceived.setStatus("current")
_TnStatsInternetRulePacketsReceived_Type = Gauge32
_TnStatsInternetRulePacketsReceived_Object = MibTableColumn
tnStatsInternetRulePacketsReceived = _TnStatsInternetRulePacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 18, 2, 1, 10),
    _TnStatsInternetRulePacketsReceived_Type()
)
tnStatsInternetRulePacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsInternetRulePacketsReceived.setStatus("current")
_TnStatsInternetRuleBytesDropped_Type = Gauge32
_TnStatsInternetRuleBytesDropped_Object = MibTableColumn
tnStatsInternetRuleBytesDropped = _TnStatsInternetRuleBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 18, 2, 1, 11),
    _TnStatsInternetRuleBytesDropped_Type()
)
tnStatsInternetRuleBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsInternetRuleBytesDropped.setStatus("current")
_TnStatsInternetRulePacketsDropped_Type = Gauge32
_TnStatsInternetRulePacketsDropped_Object = MibTableColumn
tnStatsInternetRulePacketsDropped = _TnStatsInternetRulePacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 18, 2, 1, 12),
    _TnStatsInternetRulePacketsDropped_Type()
)
tnStatsInternetRulePacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsInternetRulePacketsDropped.setStatus("current")
_TnStatsInternetRuleLastActiveNMinuteAgo_Type = TimeTicks
_TnStatsInternetRuleLastActiveNMinuteAgo_Object = MibTableColumn
tnStatsInternetRuleLastActiveNMinuteAgo = _TnStatsInternetRuleLastActiveNMinuteAgo_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 18, 2, 1, 13),
    _TnStatsInternetRuleLastActiveNMinuteAgo_Type()
)
tnStatsInternetRuleLastActiveNMinuteAgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsInternetRuleLastActiveNMinuteAgo.setStatus("current")
_TnStatsIntranet_ObjectIdentity = ObjectIdentity
tnStatsIntranet = _TnStatsIntranet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 19)
)
_TnStatsIntranetScalars_ObjectIdentity = ObjectIdentity
tnStatsIntranetScalars = _TnStatsIntranetScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 19, 1)
)


class _TnStatsIntranetNumIntranetServices_Type(Integer32):
    """Custom type tnStatsIntranetNumIntranetServices based on Integer32"""
    defaultValue = 0


_TnStatsIntranetNumIntranetServices_Type.__name__ = "Integer32"
_TnStatsIntranetNumIntranetServices_Object = MibScalar
tnStatsIntranetNumIntranetServices = _TnStatsIntranetNumIntranetServices_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 19, 1, 8),
    _TnStatsIntranetNumIntranetServices_Type()
)
tnStatsIntranetNumIntranetServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsIntranetNumIntranetServices.setStatus("current")
_TnStatsIntranetsTable_Object = MibTable
tnStatsIntranetsTable = _TnStatsIntranetsTable_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 19, 3)
)
if mibBuilder.loadTexts:
    tnStatsIntranetsTable.setStatus("current")
_TnStatsIntranetsEntry_Object = MibTableRow
tnStatsIntranetsEntry = _TnStatsIntranetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 19, 3, 1)
)
tnStatsIntranetsEntry.setIndexNames(
    (0, "TALARI-MIB", "tnStatsIntranetsIndex"),
)
if mibBuilder.loadTexts:
    tnStatsIntranetsEntry.setStatus("current")
_TnStatsIntranetsIndex_Type = Integer32
_TnStatsIntranetsIndex_Object = MibTableColumn
tnStatsIntranetsIndex = _TnStatsIntranetsIndex_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 19, 3, 1, 1),
    _TnStatsIntranetsIndex_Type()
)
tnStatsIntranetsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsIntranetsIndex.setStatus("current")
_TnStatsIntranetsID_Type = Integer32
_TnStatsIntranetsID_Object = MibTableColumn
tnStatsIntranetsID = _TnStatsIntranetsID_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 19, 3, 1, 2),
    _TnStatsIntranetsID_Type()
)
tnStatsIntranetsID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsIntranetsID.setStatus("current")
_TnStatsIntranetsName_Type = DisplayString
_TnStatsIntranetsName_Object = MibTableColumn
tnStatsIntranetsName = _TnStatsIntranetsName_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 19, 3, 1, 3),
    _TnStatsIntranetsName_Type()
)
tnStatsIntranetsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsIntranetsName.setStatus("current")
_TnStatsIntranetsBytesSent_Type = Counter64
_TnStatsIntranetsBytesSent_Object = MibTableColumn
tnStatsIntranetsBytesSent = _TnStatsIntranetsBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 19, 3, 1, 4),
    _TnStatsIntranetsBytesSent_Type()
)
tnStatsIntranetsBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsIntranetsBytesSent.setStatus("current")
_TnStatsIntranetsPacketsSent_Type = Counter64
_TnStatsIntranetsPacketsSent_Object = MibTableColumn
tnStatsIntranetsPacketsSent = _TnStatsIntranetsPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 19, 3, 1, 5),
    _TnStatsIntranetsPacketsSent_Type()
)
tnStatsIntranetsPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsIntranetsPacketsSent.setStatus("current")
_TnStatsIntranetsBytesReceived_Type = Counter64
_TnStatsIntranetsBytesReceived_Object = MibTableColumn
tnStatsIntranetsBytesReceived = _TnStatsIntranetsBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 19, 3, 1, 6),
    _TnStatsIntranetsBytesReceived_Type()
)
tnStatsIntranetsBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsIntranetsBytesReceived.setStatus("current")
_TnStatsIntranetsPacketsReceived_Type = Counter64
_TnStatsIntranetsPacketsReceived_Object = MibTableColumn
tnStatsIntranetsPacketsReceived = _TnStatsIntranetsPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 19, 3, 1, 7),
    _TnStatsIntranetsPacketsReceived_Type()
)
tnStatsIntranetsPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsIntranetsPacketsReceived.setStatus("current")
_TnStatsIntranetsBytesDropped_Type = Counter64
_TnStatsIntranetsBytesDropped_Object = MibTableColumn
tnStatsIntranetsBytesDropped = _TnStatsIntranetsBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 19, 3, 1, 8),
    _TnStatsIntranetsBytesDropped_Type()
)
tnStatsIntranetsBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsIntranetsBytesDropped.setStatus("current")
_TnStatsIntranetsPacketsDropped_Type = Counter64
_TnStatsIntranetsPacketsDropped_Object = MibTableColumn
tnStatsIntranetsPacketsDropped = _TnStatsIntranetsPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 19, 3, 1, 9),
    _TnStatsIntranetsPacketsDropped_Type()
)
tnStatsIntranetsPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsIntranetsPacketsDropped.setStatus("current")
_TnStatsIntranetsNumRules_Type = Integer32
_TnStatsIntranetsNumRules_Object = MibTableColumn
tnStatsIntranetsNumRules = _TnStatsIntranetsNumRules_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 19, 3, 1, 10),
    _TnStatsIntranetsNumRules_Type()
)
tnStatsIntranetsNumRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsIntranetsNumRules.setStatus("current")
_TnStatsIntranetsRoutingDomainName_Type = DisplayString
_TnStatsIntranetsRoutingDomainName_Object = MibTableColumn
tnStatsIntranetsRoutingDomainName = _TnStatsIntranetsRoutingDomainName_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 19, 3, 1, 11),
    _TnStatsIntranetsRoutingDomainName_Type()
)
tnStatsIntranetsRoutingDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsIntranetsRoutingDomainName.setStatus("current")
_TnStatsIntranetRulesTable_Object = MibTable
tnStatsIntranetRulesTable = _TnStatsIntranetRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 19, 4)
)
if mibBuilder.loadTexts:
    tnStatsIntranetRulesTable.setStatus("current")
_TnStatsIntranetRulesEntry_Object = MibTableRow
tnStatsIntranetRulesEntry = _TnStatsIntranetRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 19, 4, 1)
)
tnStatsIntranetRulesEntry.setIndexNames(
    (0, "TALARI-MIB", "tnStatsIntranetRulesIntranetIndex"),
    (0, "TALARI-MIB", "tnStatsIntranetRulesRuleIndex"),
)
if mibBuilder.loadTexts:
    tnStatsIntranetRulesEntry.setStatus("current")
_TnStatsIntranetRulesIntranetIndex_Type = Integer32
_TnStatsIntranetRulesIntranetIndex_Object = MibTableColumn
tnStatsIntranetRulesIntranetIndex = _TnStatsIntranetRulesIntranetIndex_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 19, 4, 1, 1),
    _TnStatsIntranetRulesIntranetIndex_Type()
)
tnStatsIntranetRulesIntranetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsIntranetRulesIntranetIndex.setStatus("current")
_TnStatsIntranetRulesRuleIndex_Type = Integer32
_TnStatsIntranetRulesRuleIndex_Object = MibTableColumn
tnStatsIntranetRulesRuleIndex = _TnStatsIntranetRulesRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 19, 4, 1, 2),
    _TnStatsIntranetRulesRuleIndex_Type()
)
tnStatsIntranetRulesRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsIntranetRulesRuleIndex.setStatus("current")
_TnStatsIntranetRulesID_Type = Integer32
_TnStatsIntranetRulesID_Object = MibTableColumn
tnStatsIntranetRulesID = _TnStatsIntranetRulesID_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 19, 4, 1, 3),
    _TnStatsIntranetRulesID_Type()
)
tnStatsIntranetRulesID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsIntranetRulesID.setStatus("current")
_TnStatsIntranetRulesGlobalRuleIndex_Type = Integer32
_TnStatsIntranetRulesGlobalRuleIndex_Object = MibTableColumn
tnStatsIntranetRulesGlobalRuleIndex = _TnStatsIntranetRulesGlobalRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 19, 4, 1, 4),
    _TnStatsIntranetRulesGlobalRuleIndex_Type()
)
tnStatsIntranetRulesGlobalRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsIntranetRulesGlobalRuleIndex.setStatus("current")
_TnStatsIntranetRulesIntranetName_Type = DisplayString
_TnStatsIntranetRulesIntranetName_Object = MibTableColumn
tnStatsIntranetRulesIntranetName = _TnStatsIntranetRulesIntranetName_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 19, 4, 1, 5),
    _TnStatsIntranetRulesIntranetName_Type()
)
tnStatsIntranetRulesIntranetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsIntranetRulesIntranetName.setStatus("current")
_TnStatsIntranetRulesApplicationName_Type = DisplayString
_TnStatsIntranetRulesApplicationName_Object = MibTableColumn
tnStatsIntranetRulesApplicationName = _TnStatsIntranetRulesApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 19, 4, 1, 6),
    _TnStatsIntranetRulesApplicationName_Type()
)
tnStatsIntranetRulesApplicationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsIntranetRulesApplicationName.setStatus("current")
_TnStatsIntranetRulesWANIngressHitCount_Type = Gauge32
_TnStatsIntranetRulesWANIngressHitCount_Object = MibTableColumn
tnStatsIntranetRulesWANIngressHitCount = _TnStatsIntranetRulesWANIngressHitCount_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 19, 4, 1, 7),
    _TnStatsIntranetRulesWANIngressHitCount_Type()
)
tnStatsIntranetRulesWANIngressHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsIntranetRulesWANIngressHitCount.setStatus("current")
_TnStatsIntranetRulesWANEgressHitCount_Type = Gauge32
_TnStatsIntranetRulesWANEgressHitCount_Object = MibTableColumn
tnStatsIntranetRulesWANEgressHitCount = _TnStatsIntranetRulesWANEgressHitCount_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 19, 4, 1, 8),
    _TnStatsIntranetRulesWANEgressHitCount_Type()
)
tnStatsIntranetRulesWANEgressHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsIntranetRulesWANEgressHitCount.setStatus("current")
_TnStatsIntranetRulesBytesSent_Type = Gauge32
_TnStatsIntranetRulesBytesSent_Object = MibTableColumn
tnStatsIntranetRulesBytesSent = _TnStatsIntranetRulesBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 19, 4, 1, 9),
    _TnStatsIntranetRulesBytesSent_Type()
)
tnStatsIntranetRulesBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsIntranetRulesBytesSent.setStatus("current")
_TnStatsIntranetRulesPacketsSent_Type = Gauge32
_TnStatsIntranetRulesPacketsSent_Object = MibTableColumn
tnStatsIntranetRulesPacketsSent = _TnStatsIntranetRulesPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 19, 4, 1, 10),
    _TnStatsIntranetRulesPacketsSent_Type()
)
tnStatsIntranetRulesPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsIntranetRulesPacketsSent.setStatus("current")
_TnStatsIntranetRulesBytesReceived_Type = Gauge32
_TnStatsIntranetRulesBytesReceived_Object = MibTableColumn
tnStatsIntranetRulesBytesReceived = _TnStatsIntranetRulesBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 19, 4, 1, 11),
    _TnStatsIntranetRulesBytesReceived_Type()
)
tnStatsIntranetRulesBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsIntranetRulesBytesReceived.setStatus("current")
_TnStatsIntranetRulesPacketsReceived_Type = Gauge32
_TnStatsIntranetRulesPacketsReceived_Object = MibTableColumn
tnStatsIntranetRulesPacketsReceived = _TnStatsIntranetRulesPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 19, 4, 1, 12),
    _TnStatsIntranetRulesPacketsReceived_Type()
)
tnStatsIntranetRulesPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsIntranetRulesPacketsReceived.setStatus("current")
_TnStatsIntranetRulesBytesDropped_Type = Gauge32
_TnStatsIntranetRulesBytesDropped_Object = MibTableColumn
tnStatsIntranetRulesBytesDropped = _TnStatsIntranetRulesBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 19, 4, 1, 13),
    _TnStatsIntranetRulesBytesDropped_Type()
)
tnStatsIntranetRulesBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsIntranetRulesBytesDropped.setStatus("current")
_TnStatsIntranetRulesPacketsDropped_Type = Gauge32
_TnStatsIntranetRulesPacketsDropped_Object = MibTableColumn
tnStatsIntranetRulesPacketsDropped = _TnStatsIntranetRulesPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 19, 4, 1, 14),
    _TnStatsIntranetRulesPacketsDropped_Type()
)
tnStatsIntranetRulesPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsIntranetRulesPacketsDropped.setStatus("current")
_TnStatsIntranetRulesLastActiveNMinuteAgo_Type = TimeTicks
_TnStatsIntranetRulesLastActiveNMinuteAgo_Object = MibTableColumn
tnStatsIntranetRulesLastActiveNMinuteAgo = _TnStatsIntranetRulesLastActiveNMinuteAgo_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 19, 4, 1, 15),
    _TnStatsIntranetRulesLastActiveNMinuteAgo_Type()
)
tnStatsIntranetRulesLastActiveNMinuteAgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsIntranetRulesLastActiveNMinuteAgo.setStatus("current")
_TnStatsPassthrough_ObjectIdentity = ObjectIdentity
tnStatsPassthrough = _TnStatsPassthrough_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 20)
)
_TnStatsPassthroughScalars_ObjectIdentity = ObjectIdentity
tnStatsPassthroughScalars = _TnStatsPassthroughScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 20, 1)
)


class _TnStatsPassthroughBytesSent_Type(Counter64):
    """Custom type tnStatsPassthroughBytesSent based on Counter64"""
    defaultValue = 0


_TnStatsPassthroughBytesSent_Type.__name__ = "Counter64"
_TnStatsPassthroughBytesSent_Object = MibScalar
tnStatsPassthroughBytesSent = _TnStatsPassthroughBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 20, 1, 1),
    _TnStatsPassthroughBytesSent_Type()
)
tnStatsPassthroughBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsPassthroughBytesSent.setStatus("current")


class _TnStatsPassthroughPacketsSent_Type(Counter64):
    """Custom type tnStatsPassthroughPacketsSent based on Counter64"""
    defaultValue = 0


_TnStatsPassthroughPacketsSent_Type.__name__ = "Counter64"
_TnStatsPassthroughPacketsSent_Object = MibScalar
tnStatsPassthroughPacketsSent = _TnStatsPassthroughPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 20, 1, 2),
    _TnStatsPassthroughPacketsSent_Type()
)
tnStatsPassthroughPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsPassthroughPacketsSent.setStatus("current")


class _TnStatsPassthroughBytesReceived_Type(Counter64):
    """Custom type tnStatsPassthroughBytesReceived based on Counter64"""
    defaultValue = 0


_TnStatsPassthroughBytesReceived_Type.__name__ = "Counter64"
_TnStatsPassthroughBytesReceived_Object = MibScalar
tnStatsPassthroughBytesReceived = _TnStatsPassthroughBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 20, 1, 3),
    _TnStatsPassthroughBytesReceived_Type()
)
tnStatsPassthroughBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsPassthroughBytesReceived.setStatus("current")


class _TnStatsPassthroughPacketsReceived_Type(Counter64):
    """Custom type tnStatsPassthroughPacketsReceived based on Counter64"""
    defaultValue = 0


_TnStatsPassthroughPacketsReceived_Type.__name__ = "Counter64"
_TnStatsPassthroughPacketsReceived_Object = MibScalar
tnStatsPassthroughPacketsReceived = _TnStatsPassthroughPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 20, 1, 4),
    _TnStatsPassthroughPacketsReceived_Type()
)
tnStatsPassthroughPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsPassthroughPacketsReceived.setStatus("current")


class _TnStatsPassthroughBytesDropped_Type(Counter64):
    """Custom type tnStatsPassthroughBytesDropped based on Counter64"""
    defaultValue = 0


_TnStatsPassthroughBytesDropped_Type.__name__ = "Counter64"
_TnStatsPassthroughBytesDropped_Object = MibScalar
tnStatsPassthroughBytesDropped = _TnStatsPassthroughBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 20, 1, 5),
    _TnStatsPassthroughBytesDropped_Type()
)
tnStatsPassthroughBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsPassthroughBytesDropped.setStatus("current")


class _TnStatsPassthroughPacketsDropped_Type(Counter64):
    """Custom type tnStatsPassthroughPacketsDropped based on Counter64"""
    defaultValue = 0


_TnStatsPassthroughPacketsDropped_Type.__name__ = "Counter64"
_TnStatsPassthroughPacketsDropped_Object = MibScalar
tnStatsPassthroughPacketsDropped = _TnStatsPassthroughPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 20, 1, 6),
    _TnStatsPassthroughPacketsDropped_Type()
)
tnStatsPassthroughPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsPassthroughPacketsDropped.setStatus("current")
_TnStatsRoutesV2_ObjectIdentity = ObjectIdentity
tnStatsRoutesV2 = _TnStatsRoutesV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 21)
)
_TnStatsRouteScalars_ObjectIdentity = ObjectIdentity
tnStatsRouteScalars = _TnStatsRouteScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 21, 1)
)


class _TnStatsNumRoutesV2_Type(Gauge32):
    """Custom type tnStatsNumRoutesV2 based on Gauge32"""
    defaultValue = 0


_TnStatsNumRoutesV2_Type.__name__ = "Gauge32"
_TnStatsNumRoutesV2_Object = MibScalar
tnStatsNumRoutesV2 = _TnStatsNumRoutesV2_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 21, 1, 1),
    _TnStatsNumRoutesV2_Type()
)
tnStatsNumRoutesV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsNumRoutesV2.setStatus("current")
_TnStatsRouteTableV2_Object = MibTable
tnStatsRouteTableV2 = _TnStatsRouteTableV2_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 21, 2)
)
if mibBuilder.loadTexts:
    tnStatsRouteTableV2.setStatus("current")
_TnStatsRouteEntryV2_Object = MibTableRow
tnStatsRouteEntryV2 = _TnStatsRouteEntryV2_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 21, 2, 1)
)
tnStatsRouteEntryV2.setIndexNames(
    (0, "TALARI-MIB", "tnStatsRouteIndexV2"),
)
if mibBuilder.loadTexts:
    tnStatsRouteEntryV2.setStatus("current")
_TnStatsRouteIndexV2_Type = Integer32
_TnStatsRouteIndexV2_Object = MibTableColumn
tnStatsRouteIndexV2 = _TnStatsRouteIndexV2_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 21, 2, 1, 1),
    _TnStatsRouteIndexV2_Type()
)
tnStatsRouteIndexV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsRouteIndexV2.setStatus("current")
_TnStatsRouteNetworkAddr_Type = IpAddress
_TnStatsRouteNetworkAddr_Object = MibTableColumn
tnStatsRouteNetworkAddr = _TnStatsRouteNetworkAddr_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 21, 2, 1, 2),
    _TnStatsRouteNetworkAddr_Type()
)
tnStatsRouteNetworkAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsRouteNetworkAddr.setStatus("current")
_TnStatsRouteNetworkPrefix_Type = Integer32
_TnStatsRouteNetworkPrefix_Object = MibTableColumn
tnStatsRouteNetworkPrefix = _TnStatsRouteNetworkPrefix_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 21, 2, 1, 3),
    _TnStatsRouteNetworkPrefix_Type()
)
tnStatsRouteNetworkPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsRouteNetworkPrefix.setStatus("current")
_TnStatsRouteGateway_Type = IpAddress
_TnStatsRouteGateway_Object = MibTableColumn
tnStatsRouteGateway = _TnStatsRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 21, 2, 1, 4),
    _TnStatsRouteGateway_Type()
)
tnStatsRouteGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsRouteGateway.setStatus("current")


class _TnStatsRouteFallback_Type(Integer32):
    """Custom type tnStatsRouteFallback based on Integer32"""
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


_TnStatsRouteFallback_Type.__name__ = "Integer32"
_TnStatsRouteFallback_Object = MibTableColumn
tnStatsRouteFallback = _TnStatsRouteFallback_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 21, 2, 1, 5),
    _TnStatsRouteFallback_Type()
)
tnStatsRouteFallback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsRouteFallback.setStatus("obsolete")


class _TnStatsRouteServiceType_Type(Integer32):
    """Custom type tnStatsRouteServiceType based on Integer32"""
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
        *(("discard", 0),
          ("passthrough", 1),
          ("internet", 2),
          ("intranet", 3),
          ("conduit", 4),
          ("langretunnel", 5),
          ("lanipsectunnel", 6),
          ("local", 7),
          ("iphost", 8))
    )


_TnStatsRouteServiceType_Type.__name__ = "Integer32"
_TnStatsRouteServiceType_Object = MibTableColumn
tnStatsRouteServiceType = _TnStatsRouteServiceType_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 21, 2, 1, 6),
    _TnStatsRouteServiceType_Type()
)
tnStatsRouteServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsRouteServiceType.setStatus("current")
_TnStatsRouteServiceID_Type = Integer32
_TnStatsRouteServiceID_Object = MibTableColumn
tnStatsRouteServiceID = _TnStatsRouteServiceID_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 21, 2, 1, 7),
    _TnStatsRouteServiceID_Type()
)
tnStatsRouteServiceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsRouteServiceID.setStatus("current")
_TnStatsRouteServiceName_Type = DisplayString
_TnStatsRouteServiceName_Object = MibTableColumn
tnStatsRouteServiceName = _TnStatsRouteServiceName_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 21, 2, 1, 8),
    _TnStatsRouteServiceName_Type()
)
tnStatsRouteServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsRouteServiceName.setStatus("current")


class _TnStatsRouteReachable_Type(Integer32):
    """Custom type tnStatsRouteReachable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1),
          ("na", 2))
    )


_TnStatsRouteReachable_Type.__name__ = "Integer32"
_TnStatsRouteReachable_Object = MibTableColumn
tnStatsRouteReachable = _TnStatsRouteReachable_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 21, 2, 1, 9),
    _TnStatsRouteReachable_Type()
)
tnStatsRouteReachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsRouteReachable.setStatus("current")
_TnStatsRouteSiteName_Type = DisplayString
_TnStatsRouteSiteName_Object = MibTableColumn
tnStatsRouteSiteName = _TnStatsRouteSiteName_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 21, 2, 1, 10),
    _TnStatsRouteSiteName_Type()
)
tnStatsRouteSiteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsRouteSiteName.setStatus("current")


class _TnStatsRouteType_Type(Integer32):
    """Custom type tnStatsRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 0),
          ("dynamic", 1),
          ("dynamicConduit", 2))
    )


_TnStatsRouteType_Type.__name__ = "Integer32"
_TnStatsRouteType_Object = MibTableColumn
tnStatsRouteType = _TnStatsRouteType_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 21, 2, 1, 11),
    _TnStatsRouteType_Type()
)
tnStatsRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsRouteType.setStatus("current")


class _TnStatsRouteNeighborDirect_Type(Integer32):
    """Custom type tnStatsRouteNeighborDirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("directNeighbor", 1),
          ("indirectNeighbor", 2))
    )


_TnStatsRouteNeighborDirect_Type.__name__ = "Integer32"
_TnStatsRouteNeighborDirect_Object = MibTableColumn
tnStatsRouteNeighborDirect = _TnStatsRouteNeighborDirect_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 21, 2, 1, 12),
    _TnStatsRouteNeighborDirect_Type()
)
tnStatsRouteNeighborDirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsRouteNeighborDirect.setStatus("current")
_TnStatsRouteCost_Type = Integer32
_TnStatsRouteCost_Object = MibTableColumn
tnStatsRouteCost = _TnStatsRouteCost_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 21, 2, 1, 13),
    _TnStatsRouteCost_Type()
)
tnStatsRouteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsRouteCost.setStatus("current")
_TnStatsRouteHitCountV2_Type = Counter64
_TnStatsRouteHitCountV2_Object = MibTableColumn
tnStatsRouteHitCountV2 = _TnStatsRouteHitCountV2_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 21, 2, 1, 14),
    _TnStatsRouteHitCountV2_Type()
)
tnStatsRouteHitCountV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsRouteHitCountV2.setStatus("current")
_TnStatsRouteEligible_Type = DisplayString
_TnStatsRouteEligible_Object = MibTableColumn
tnStatsRouteEligible = _TnStatsRouteEligible_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 21, 2, 1, 15),
    _TnStatsRouteEligible_Type()
)
tnStatsRouteEligible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsRouteEligible.setStatus("current")
_TnStatsRouteEligibilityType_Type = DisplayString
_TnStatsRouteEligibilityType_Object = MibTableColumn
tnStatsRouteEligibilityType = _TnStatsRouteEligibilityType_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 21, 2, 1, 16),
    _TnStatsRouteEligibilityType_Type()
)
tnStatsRouteEligibilityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsRouteEligibilityType.setStatus("current")
_TnStatsRouteEligibilityValue_Type = DisplayString
_TnStatsRouteEligibilityValue_Object = MibTableColumn
tnStatsRouteEligibilityValue = _TnStatsRouteEligibilityValue_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 21, 2, 1, 17),
    _TnStatsRouteEligibilityValue_Type()
)
tnStatsRouteEligibilityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsRouteEligibilityValue.setStatus("current")


class _TnStatsRouteProtocol_Type(Integer32):
    """Custom type tnStatsRouteProtocol based on Integer32"""
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
        *(("na", 0),
          ("bgp", 1),
          ("ospf", 2),
          ("apn", 3))
    )


_TnStatsRouteProtocol_Type.__name__ = "Integer32"
_TnStatsRouteProtocol_Object = MibTableColumn
tnStatsRouteProtocol = _TnStatsRouteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 21, 2, 1, 18),
    _TnStatsRouteProtocol_Type()
)
tnStatsRouteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsRouteProtocol.setStatus("current")
_TnStatsRouteRoutingDomainName_Type = DisplayString
_TnStatsRouteRoutingDomainName_Object = MibTableColumn
tnStatsRouteRoutingDomainName = _TnStatsRouteRoutingDomainName_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 21, 2, 1, 19),
    _TnStatsRouteRoutingDomainName_Type()
)
tnStatsRouteRoutingDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsRouteRoutingDomainName.setStatus("current")
_TnStatsDynamicConduits_ObjectIdentity = ObjectIdentity
tnStatsDynamicConduits = _TnStatsDynamicConduits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22)
)
_TnStatsDynamicConduitScalars_ObjectIdentity = ObjectIdentity
tnStatsDynamicConduitScalars = _TnStatsDynamicConduitScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 1)
)


class _TnStatsNumDynamicConduits_Type(Gauge32):
    """Custom type tnStatsNumDynamicConduits based on Gauge32"""
    defaultValue = 0


_TnStatsNumDynamicConduits_Type.__name__ = "Gauge32"
_TnStatsNumDynamicConduits_Object = MibScalar
tnStatsNumDynamicConduits = _TnStatsNumDynamicConduits_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 1, 1),
    _TnStatsNumDynamicConduits_Type()
)
tnStatsNumDynamicConduits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsNumDynamicConduits.setStatus("current")
_TnStatsDynamicConduitTable_Object = MibTable
tnStatsDynamicConduitTable = _TnStatsDynamicConduitTable_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 2)
)
if mibBuilder.loadTexts:
    tnStatsDynamicConduitTable.setStatus("current")
_TnStatsDynamicConduitEntry_Object = MibTableRow
tnStatsDynamicConduitEntry = _TnStatsDynamicConduitEntry_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 2, 1)
)
tnStatsDynamicConduitEntry.setIndexNames(
    (0, "TALARI-MIB", "tnStatsDynamicConduitIndex"),
)
if mibBuilder.loadTexts:
    tnStatsDynamicConduitEntry.setStatus("current")
_TnStatsDynamicConduitIndex_Type = Integer32
_TnStatsDynamicConduitIndex_Object = MibTableColumn
tnStatsDynamicConduitIndex = _TnStatsDynamicConduitIndex_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 2, 1, 1),
    _TnStatsDynamicConduitIndex_Type()
)
tnStatsDynamicConduitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitIndex.setStatus("current")
_TnStatsDynamicConduitID_Type = Integer32
_TnStatsDynamicConduitID_Object = MibTableColumn
tnStatsDynamicConduitID = _TnStatsDynamicConduitID_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 2, 1, 2),
    _TnStatsDynamicConduitID_Type()
)
tnStatsDynamicConduitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitID.setStatus("current")
_TnStatsDynamicConduitName_Type = DisplayString
_TnStatsDynamicConduitName_Object = MibTableColumn
tnStatsDynamicConduitName = _TnStatsDynamicConduitName_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 2, 1, 3),
    _TnStatsDynamicConduitName_Type()
)
tnStatsDynamicConduitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitName.setStatus("current")


class _TnStatsDynamicConduitState_Type(Integer32):
    """Custom type tnStatsDynamicConduitState based on Integer32"""
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
          ("disabled", 1),
          ("dead", 2),
          ("bad", 3),
          ("good", 4))
    )


_TnStatsDynamicConduitState_Type.__name__ = "Integer32"
_TnStatsDynamicConduitState_Object = MibTableColumn
tnStatsDynamicConduitState = _TnStatsDynamicConduitState_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 2, 1, 4),
    _TnStatsDynamicConduitState_Type()
)
tnStatsDynamicConduitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitState.setStatus("current")
_TnStatsDynamicConduitTimeSinceCreation_Type = Counter64
_TnStatsDynamicConduitTimeSinceCreation_Object = MibTableColumn
tnStatsDynamicConduitTimeSinceCreation = _TnStatsDynamicConduitTimeSinceCreation_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 2, 1, 5),
    _TnStatsDynamicConduitTimeSinceCreation_Type()
)
tnStatsDynamicConduitTimeSinceCreation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitTimeSinceCreation.setStatus("current")
_TnStatsDynamicConduitBytesSent_Type = Counter64
_TnStatsDynamicConduitBytesSent_Object = MibTableColumn
tnStatsDynamicConduitBytesSent = _TnStatsDynamicConduitBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 2, 1, 6),
    _TnStatsDynamicConduitBytesSent_Type()
)
tnStatsDynamicConduitBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitBytesSent.setStatus("current")
_TnStatsDynamicConduitPacketsSent_Type = Counter64
_TnStatsDynamicConduitPacketsSent_Object = MibTableColumn
tnStatsDynamicConduitPacketsSent = _TnStatsDynamicConduitPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 2, 1, 7),
    _TnStatsDynamicConduitPacketsSent_Type()
)
tnStatsDynamicConduitPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitPacketsSent.setStatus("current")
_TnStatsDynamicConduitSendBytesDropped_Type = Counter64
_TnStatsDynamicConduitSendBytesDropped_Object = MibTableColumn
tnStatsDynamicConduitSendBytesDropped = _TnStatsDynamicConduitSendBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 2, 1, 8),
    _TnStatsDynamicConduitSendBytesDropped_Type()
)
tnStatsDynamicConduitSendBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitSendBytesDropped.setStatus("current")
_TnStatsDynamicConduitSendPacketsDropped_Type = Counter64
_TnStatsDynamicConduitSendPacketsDropped_Object = MibTableColumn
tnStatsDynamicConduitSendPacketsDropped = _TnStatsDynamicConduitSendPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 2, 1, 9),
    _TnStatsDynamicConduitSendPacketsDropped_Type()
)
tnStatsDynamicConduitSendPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitSendPacketsDropped.setStatus("current")
_TnStatsDynamicConduitSendPacketsLost_Type = Counter64
_TnStatsDynamicConduitSendPacketsLost_Object = MibTableColumn
tnStatsDynamicConduitSendPacketsLost = _TnStatsDynamicConduitSendPacketsLost_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 2, 1, 10),
    _TnStatsDynamicConduitSendPacketsLost_Type()
)
tnStatsDynamicConduitSendPacketsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitSendPacketsLost.setStatus("current")
_TnStatsDynamicConduitSendPacketsOOO_Type = Counter64
_TnStatsDynamicConduitSendPacketsOOO_Object = MibTableColumn
tnStatsDynamicConduitSendPacketsOOO = _TnStatsDynamicConduitSendPacketsOOO_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 2, 1, 11),
    _TnStatsDynamicConduitSendPacketsOOO_Type()
)
tnStatsDynamicConduitSendPacketsOOO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitSendPacketsOOO.setStatus("current")
_TnStatsDynamicConduitSendBOWTms_Type = Gauge32
_TnStatsDynamicConduitSendBOWTms_Object = MibTableColumn
tnStatsDynamicConduitSendBOWTms = _TnStatsDynamicConduitSendBOWTms_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 2, 1, 12),
    _TnStatsDynamicConduitSendBOWTms_Type()
)
tnStatsDynamicConduitSendBOWTms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitSendBOWTms.setStatus("current")
_TnStatsDynamicConduitSendJitterms_Type = Gauge32
_TnStatsDynamicConduitSendJitterms_Object = MibTableColumn
tnStatsDynamicConduitSendJitterms = _TnStatsDynamicConduitSendJitterms_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 2, 1, 13),
    _TnStatsDynamicConduitSendJitterms_Type()
)
tnStatsDynamicConduitSendJitterms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitSendJitterms.setStatus("current")
_TnStatsDynamicConduitBytesReceived_Type = Counter64
_TnStatsDynamicConduitBytesReceived_Object = MibTableColumn
tnStatsDynamicConduitBytesReceived = _TnStatsDynamicConduitBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 2, 1, 14),
    _TnStatsDynamicConduitBytesReceived_Type()
)
tnStatsDynamicConduitBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitBytesReceived.setStatus("current")
_TnStatsDynamicConduitPacketsReceived_Type = Counter64
_TnStatsDynamicConduitPacketsReceived_Object = MibTableColumn
tnStatsDynamicConduitPacketsReceived = _TnStatsDynamicConduitPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 2, 1, 15),
    _TnStatsDynamicConduitPacketsReceived_Type()
)
tnStatsDynamicConduitPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitPacketsReceived.setStatus("current")
_TnStatsDynamicConduitReceiveBytesDropped_Type = Counter64
_TnStatsDynamicConduitReceiveBytesDropped_Object = MibTableColumn
tnStatsDynamicConduitReceiveBytesDropped = _TnStatsDynamicConduitReceiveBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 2, 1, 16),
    _TnStatsDynamicConduitReceiveBytesDropped_Type()
)
tnStatsDynamicConduitReceiveBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitReceiveBytesDropped.setStatus("current")
_TnStatsDynamicConduitReceivePacketsDropped_Type = Counter64
_TnStatsDynamicConduitReceivePacketsDropped_Object = MibTableColumn
tnStatsDynamicConduitReceivePacketsDropped = _TnStatsDynamicConduitReceivePacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 2, 1, 17),
    _TnStatsDynamicConduitReceivePacketsDropped_Type()
)
tnStatsDynamicConduitReceivePacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitReceivePacketsDropped.setStatus("current")
_TnStatsDynamicConduitReceivePacketsLost_Type = Counter64
_TnStatsDynamicConduitReceivePacketsLost_Object = MibTableColumn
tnStatsDynamicConduitReceivePacketsLost = _TnStatsDynamicConduitReceivePacketsLost_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 2, 1, 18),
    _TnStatsDynamicConduitReceivePacketsLost_Type()
)
tnStatsDynamicConduitReceivePacketsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitReceivePacketsLost.setStatus("current")
_TnStatsDynamicConduitReceivePacketsOOO_Type = Counter64
_TnStatsDynamicConduitReceivePacketsOOO_Object = MibTableColumn
tnStatsDynamicConduitReceivePacketsOOO = _TnStatsDynamicConduitReceivePacketsOOO_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 2, 1, 19),
    _TnStatsDynamicConduitReceivePacketsOOO_Type()
)
tnStatsDynamicConduitReceivePacketsOOO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitReceivePacketsOOO.setStatus("current")
_TnStatsDynamicConduitReceiveBOWTms_Type = Gauge32
_TnStatsDynamicConduitReceiveBOWTms_Object = MibTableColumn
tnStatsDynamicConduitReceiveBOWTms = _TnStatsDynamicConduitReceiveBOWTms_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 2, 1, 20),
    _TnStatsDynamicConduitReceiveBOWTms_Type()
)
tnStatsDynamicConduitReceiveBOWTms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitReceiveBOWTms.setStatus("current")
_TnStatsDynamicConduitReceiveJitterms_Type = Gauge32
_TnStatsDynamicConduitReceiveJitterms_Object = MibTableColumn
tnStatsDynamicConduitReceiveJitterms = _TnStatsDynamicConduitReceiveJitterms_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 2, 1, 21),
    _TnStatsDynamicConduitReceiveJitterms_Type()
)
tnStatsDynamicConduitReceiveJitterms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitReceiveJitterms.setStatus("current")
_TnStatsDynamicConduitNumPaths_Type = Integer32
_TnStatsDynamicConduitNumPaths_Object = MibTableColumn
tnStatsDynamicConduitNumPaths = _TnStatsDynamicConduitNumPaths_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 2, 1, 22),
    _TnStatsDynamicConduitNumPaths_Type()
)
tnStatsDynamicConduitNumPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitNumPaths.setStatus("current")
_TnStatsDynamicConduitNumRules_Type = Integer32
_TnStatsDynamicConduitNumRules_Object = MibTableColumn
tnStatsDynamicConduitNumRules = _TnStatsDynamicConduitNumRules_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 2, 1, 23),
    _TnStatsDynamicConduitNumRules_Type()
)
tnStatsDynamicConduitNumRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitNumRules.setStatus("current")
_TnStatsDynamicConduitPaths_ObjectIdentity = ObjectIdentity
tnStatsDynamicConduitPaths = _TnStatsDynamicConduitPaths_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 3)
)
_TnStatsDynamicConduitPathTable_Object = MibTable
tnStatsDynamicConduitPathTable = _TnStatsDynamicConduitPathTable_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 3, 1)
)
if mibBuilder.loadTexts:
    tnStatsDynamicConduitPathTable.setStatus("current")
_TnStatsDynamicConduitPathEntry_Object = MibTableRow
tnStatsDynamicConduitPathEntry = _TnStatsDynamicConduitPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 3, 1, 1)
)
tnStatsDynamicConduitPathEntry.setIndexNames(
    (0, "TALARI-MIB", "tnStatsDynamicConduitPathConduitIndex"),
    (0, "TALARI-MIB", "tnStatsDynamicConduitPathPathIndex"),
)
if mibBuilder.loadTexts:
    tnStatsDynamicConduitPathEntry.setStatus("current")
_TnStatsDynamicConduitPathConduitIndex_Type = Integer32
_TnStatsDynamicConduitPathConduitIndex_Object = MibTableColumn
tnStatsDynamicConduitPathConduitIndex = _TnStatsDynamicConduitPathConduitIndex_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 3, 1, 1, 1),
    _TnStatsDynamicConduitPathConduitIndex_Type()
)
tnStatsDynamicConduitPathConduitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitPathConduitIndex.setStatus("current")
_TnStatsDynamicConduitPathPathIndex_Type = Integer32
_TnStatsDynamicConduitPathPathIndex_Object = MibTableColumn
tnStatsDynamicConduitPathPathIndex = _TnStatsDynamicConduitPathPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 3, 1, 1, 2),
    _TnStatsDynamicConduitPathPathIndex_Type()
)
tnStatsDynamicConduitPathPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitPathPathIndex.setStatus("current")
_TnStatsDynamicConduitPathConduitID_Type = Integer32
_TnStatsDynamicConduitPathConduitID_Object = MibTableColumn
tnStatsDynamicConduitPathConduitID = _TnStatsDynamicConduitPathConduitID_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 3, 1, 1, 3),
    _TnStatsDynamicConduitPathConduitID_Type()
)
tnStatsDynamicConduitPathConduitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitPathConduitID.setStatus("current")
_TnStatsDynamicConduitPathPathID_Type = Integer32
_TnStatsDynamicConduitPathPathID_Object = MibTableColumn
tnStatsDynamicConduitPathPathID = _TnStatsDynamicConduitPathPathID_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 3, 1, 1, 4),
    _TnStatsDynamicConduitPathPathID_Type()
)
tnStatsDynamicConduitPathPathID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitPathPathID.setStatus("current")
_TnStatsDynamicConduitPathName_Type = DisplayString
_TnStatsDynamicConduitPathName_Object = MibTableColumn
tnStatsDynamicConduitPathName = _TnStatsDynamicConduitPathName_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 3, 1, 1, 5),
    _TnStatsDynamicConduitPathName_Type()
)
tnStatsDynamicConduitPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitPathName.setStatus("current")


class _TnStatsDynamicConduitPathState_Type(Integer32):
    """Custom type tnStatsDynamicConduitPathState based on Integer32"""
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
          ("disabled", 1),
          ("dead", 2),
          ("bad", 3),
          ("good", 4))
    )


_TnStatsDynamicConduitPathState_Type.__name__ = "Integer32"
_TnStatsDynamicConduitPathState_Object = MibTableColumn
tnStatsDynamicConduitPathState = _TnStatsDynamicConduitPathState_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 3, 1, 1, 6),
    _TnStatsDynamicConduitPathState_Type()
)
tnStatsDynamicConduitPathState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitPathState.setStatus("current")
_TnStatsDynamicConduitPathBytesSent_Type = Counter64
_TnStatsDynamicConduitPathBytesSent_Object = MibTableColumn
tnStatsDynamicConduitPathBytesSent = _TnStatsDynamicConduitPathBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 3, 1, 1, 7),
    _TnStatsDynamicConduitPathBytesSent_Type()
)
tnStatsDynamicConduitPathBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitPathBytesSent.setStatus("current")
_TnStatsDynamicConduitPathPacketsSent_Type = Counter64
_TnStatsDynamicConduitPathPacketsSent_Object = MibTableColumn
tnStatsDynamicConduitPathPacketsSent = _TnStatsDynamicConduitPathPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 3, 1, 1, 8),
    _TnStatsDynamicConduitPathPacketsSent_Type()
)
tnStatsDynamicConduitPathPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitPathPacketsSent.setStatus("current")
_TnStatsDynamicConduitPathBytesReceived_Type = Counter64
_TnStatsDynamicConduitPathBytesReceived_Object = MibTableColumn
tnStatsDynamicConduitPathBytesReceived = _TnStatsDynamicConduitPathBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 3, 1, 1, 9),
    _TnStatsDynamicConduitPathBytesReceived_Type()
)
tnStatsDynamicConduitPathBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitPathBytesReceived.setStatus("current")
_TnStatsDynamicConduitPathPacketsReceived_Type = Counter64
_TnStatsDynamicConduitPathPacketsReceived_Object = MibTableColumn
tnStatsDynamicConduitPathPacketsReceived = _TnStatsDynamicConduitPathPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 3, 1, 1, 10),
    _TnStatsDynamicConduitPathPacketsReceived_Type()
)
tnStatsDynamicConduitPathPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitPathPacketsReceived.setStatus("current")
_TnStatsDynamicConduitPathBytesDropped_Type = Counter64
_TnStatsDynamicConduitPathBytesDropped_Object = MibTableColumn
tnStatsDynamicConduitPathBytesDropped = _TnStatsDynamicConduitPathBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 3, 1, 1, 11),
    _TnStatsDynamicConduitPathBytesDropped_Type()
)
tnStatsDynamicConduitPathBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitPathBytesDropped.setStatus("current")
_TnStatsDynamicConduitPathPacketsDropped_Type = Counter64
_TnStatsDynamicConduitPathPacketsDropped_Object = MibTableColumn
tnStatsDynamicConduitPathPacketsDropped = _TnStatsDynamicConduitPathPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 3, 1, 1, 12),
    _TnStatsDynamicConduitPathPacketsDropped_Type()
)
tnStatsDynamicConduitPathPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitPathPacketsDropped.setStatus("current")
_TnStatsDynamicConduitPathBOWTms_Type = Gauge32
_TnStatsDynamicConduitPathBOWTms_Object = MibTableColumn
tnStatsDynamicConduitPathBOWTms = _TnStatsDynamicConduitPathBOWTms_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 3, 1, 1, 13),
    _TnStatsDynamicConduitPathBOWTms_Type()
)
tnStatsDynamicConduitPathBOWTms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitPathBOWTms.setStatus("current")
_TnStatsDynamicConduitPathJitterms_Type = Gauge32
_TnStatsDynamicConduitPathJitterms_Object = MibTableColumn
tnStatsDynamicConduitPathJitterms = _TnStatsDynamicConduitPathJitterms_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 3, 1, 1, 14),
    _TnStatsDynamicConduitPathJitterms_Type()
)
tnStatsDynamicConduitPathJitterms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitPathJitterms.setStatus("current")
_TnStatsDynamicConduitPathPacketsLost_Type = Counter64
_TnStatsDynamicConduitPathPacketsLost_Object = MibTableColumn
tnStatsDynamicConduitPathPacketsLost = _TnStatsDynamicConduitPathPacketsLost_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 3, 1, 1, 15),
    _TnStatsDynamicConduitPathPacketsLost_Type()
)
tnStatsDynamicConduitPathPacketsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitPathPacketsLost.setStatus("current")
_TnStatsDynamicConduitPathPacketsOOO_Type = Counter64
_TnStatsDynamicConduitPathPacketsOOO_Object = MibTableColumn
tnStatsDynamicConduitPathPacketsOOO = _TnStatsDynamicConduitPathPacketsOOO_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 3, 1, 1, 16),
    _TnStatsDynamicConduitPathPacketsOOO_Type()
)
tnStatsDynamicConduitPathPacketsOOO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitPathPacketsOOO.setStatus("current")
_TnStatsDynamicConduitClasses_ObjectIdentity = ObjectIdentity
tnStatsDynamicConduitClasses = _TnStatsDynamicConduitClasses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 4)
)
_TnStatsDynamicConduitClassTable_Object = MibTable
tnStatsDynamicConduitClassTable = _TnStatsDynamicConduitClassTable_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 4, 1)
)
if mibBuilder.loadTexts:
    tnStatsDynamicConduitClassTable.setStatus("current")
_TnStatsDynamicConduitClassEntry_Object = MibTableRow
tnStatsDynamicConduitClassEntry = _TnStatsDynamicConduitClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 4, 1, 1)
)
tnStatsDynamicConduitClassEntry.setIndexNames(
    (0, "TALARI-MIB", "tnStatsDynamicConduitClassConduitIndex"),
    (0, "TALARI-MIB", "tnStatsDynamicConduitClassClassIndex"),
)
if mibBuilder.loadTexts:
    tnStatsDynamicConduitClassEntry.setStatus("current")
_TnStatsDynamicConduitClassConduitIndex_Type = Integer32
_TnStatsDynamicConduitClassConduitIndex_Object = MibTableColumn
tnStatsDynamicConduitClassConduitIndex = _TnStatsDynamicConduitClassConduitIndex_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 4, 1, 1, 1),
    _TnStatsDynamicConduitClassConduitIndex_Type()
)
tnStatsDynamicConduitClassConduitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitClassConduitIndex.setStatus("current")
_TnStatsDynamicConduitClassClassIndex_Type = Integer32
_TnStatsDynamicConduitClassClassIndex_Object = MibTableColumn
tnStatsDynamicConduitClassClassIndex = _TnStatsDynamicConduitClassClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 4, 1, 1, 2),
    _TnStatsDynamicConduitClassClassIndex_Type()
)
tnStatsDynamicConduitClassClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitClassClassIndex.setStatus("current")
_TnStatsDynamicConduitClassConduitID_Type = Integer32
_TnStatsDynamicConduitClassConduitID_Object = MibTableColumn
tnStatsDynamicConduitClassConduitID = _TnStatsDynamicConduitClassConduitID_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 4, 1, 1, 3),
    _TnStatsDynamicConduitClassConduitID_Type()
)
tnStatsDynamicConduitClassConduitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitClassConduitID.setStatus("current")
_TnStatsDynamicConduitClassClassID_Type = Integer32
_TnStatsDynamicConduitClassClassID_Object = MibTableColumn
tnStatsDynamicConduitClassClassID = _TnStatsDynamicConduitClassClassID_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 4, 1, 1, 4),
    _TnStatsDynamicConduitClassClassID_Type()
)
tnStatsDynamicConduitClassClassID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitClassClassID.setStatus("current")
_TnStatsDynamicConduitClassName_Type = DisplayString
_TnStatsDynamicConduitClassName_Object = MibTableColumn
tnStatsDynamicConduitClassName = _TnStatsDynamicConduitClassName_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 4, 1, 1, 5),
    _TnStatsDynamicConduitClassName_Type()
)
tnStatsDynamicConduitClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitClassName.setStatus("current")


class _TnStatsDynamicConduitClassType_Type(Integer32):
    """Custom type tnStatsDynamicConduitClassType based on Integer32"""
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
        *(("realtime", 1),
          ("interactive", 2),
          ("bulk", 3),
          ("unknown", 4))
    )


_TnStatsDynamicConduitClassType_Type.__name__ = "Integer32"
_TnStatsDynamicConduitClassType_Object = MibTableColumn
tnStatsDynamicConduitClassType = _TnStatsDynamicConduitClassType_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 4, 1, 1, 6),
    _TnStatsDynamicConduitClassType_Type()
)
tnStatsDynamicConduitClassType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitClassType.setStatus("current")
_TnStatsDynamicConduitClassBytesSent_Type = Counter64
_TnStatsDynamicConduitClassBytesSent_Object = MibTableColumn
tnStatsDynamicConduitClassBytesSent = _TnStatsDynamicConduitClassBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 4, 1, 1, 7),
    _TnStatsDynamicConduitClassBytesSent_Type()
)
tnStatsDynamicConduitClassBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitClassBytesSent.setStatus("current")
_TnStatsDynamicConduitClassPacketsSent_Type = Counter64
_TnStatsDynamicConduitClassPacketsSent_Object = MibTableColumn
tnStatsDynamicConduitClassPacketsSent = _TnStatsDynamicConduitClassPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 4, 1, 1, 8),
    _TnStatsDynamicConduitClassPacketsSent_Type()
)
tnStatsDynamicConduitClassPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitClassPacketsSent.setStatus("current")
_TnStatsDynamicConduitClassBytesPending_Type = Counter64
_TnStatsDynamicConduitClassBytesPending_Object = MibTableColumn
tnStatsDynamicConduitClassBytesPending = _TnStatsDynamicConduitClassBytesPending_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 4, 1, 1, 9),
    _TnStatsDynamicConduitClassBytesPending_Type()
)
tnStatsDynamicConduitClassBytesPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitClassBytesPending.setStatus("current")
_TnStatsDynamicConduitClassPacketsPending_Type = Counter64
_TnStatsDynamicConduitClassPacketsPending_Object = MibTableColumn
tnStatsDynamicConduitClassPacketsPending = _TnStatsDynamicConduitClassPacketsPending_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 4, 1, 1, 10),
    _TnStatsDynamicConduitClassPacketsPending_Type()
)
tnStatsDynamicConduitClassPacketsPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitClassPacketsPending.setStatus("current")
_TnStatsDynamicConduitClassBytesDropped_Type = Counter64
_TnStatsDynamicConduitClassBytesDropped_Object = MibTableColumn
tnStatsDynamicConduitClassBytesDropped = _TnStatsDynamicConduitClassBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 4, 1, 1, 11),
    _TnStatsDynamicConduitClassBytesDropped_Type()
)
tnStatsDynamicConduitClassBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitClassBytesDropped.setStatus("current")
_TnStatsDynamicConduitClassPacketsDropped_Type = Counter64
_TnStatsDynamicConduitClassPacketsDropped_Object = MibTableColumn
tnStatsDynamicConduitClassPacketsDropped = _TnStatsDynamicConduitClassPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 4, 1, 1, 12),
    _TnStatsDynamicConduitClassPacketsDropped_Type()
)
tnStatsDynamicConduitClassPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitClassPacketsDropped.setStatus("current")
_TnStatsDynamicConduitRules_ObjectIdentity = ObjectIdentity
tnStatsDynamicConduitRules = _TnStatsDynamicConduitRules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 5)
)
_TnStatsDynamicConduitRuleTable_Object = MibTable
tnStatsDynamicConduitRuleTable = _TnStatsDynamicConduitRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 5, 1)
)
if mibBuilder.loadTexts:
    tnStatsDynamicConduitRuleTable.setStatus("current")
_TnStatsDynamicConduitRuleEntry_Object = MibTableRow
tnStatsDynamicConduitRuleEntry = _TnStatsDynamicConduitRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 5, 1, 1)
)
tnStatsDynamicConduitRuleEntry.setIndexNames(
    (0, "TALARI-MIB", "tnStatsDynamicConduitRuleConduitIndex"),
    (0, "TALARI-MIB", "tnStatsDynamicConduitRuleRuleIndex"),
)
if mibBuilder.loadTexts:
    tnStatsDynamicConduitRuleEntry.setStatus("current")
_TnStatsDynamicConduitRuleConduitIndex_Type = Integer32
_TnStatsDynamicConduitRuleConduitIndex_Object = MibTableColumn
tnStatsDynamicConduitRuleConduitIndex = _TnStatsDynamicConduitRuleConduitIndex_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 5, 1, 1, 1),
    _TnStatsDynamicConduitRuleConduitIndex_Type()
)
tnStatsDynamicConduitRuleConduitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitRuleConduitIndex.setStatus("current")
_TnStatsDynamicConduitRuleRuleIndex_Type = Integer32
_TnStatsDynamicConduitRuleRuleIndex_Object = MibTableColumn
tnStatsDynamicConduitRuleRuleIndex = _TnStatsDynamicConduitRuleRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 5, 1, 1, 2),
    _TnStatsDynamicConduitRuleRuleIndex_Type()
)
tnStatsDynamicConduitRuleRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitRuleRuleIndex.setStatus("current")
_TnStatsDynamicConduitRuleConduitID_Type = Integer32
_TnStatsDynamicConduitRuleConduitID_Object = MibTableColumn
tnStatsDynamicConduitRuleConduitID = _TnStatsDynamicConduitRuleConduitID_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 5, 1, 1, 3),
    _TnStatsDynamicConduitRuleConduitID_Type()
)
tnStatsDynamicConduitRuleConduitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitRuleConduitID.setStatus("current")
_TnStatsDynamicConduitRuleRuleID_Type = Integer32
_TnStatsDynamicConduitRuleRuleID_Object = MibTableColumn
tnStatsDynamicConduitRuleRuleID = _TnStatsDynamicConduitRuleRuleID_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 5, 1, 1, 4),
    _TnStatsDynamicConduitRuleRuleID_Type()
)
tnStatsDynamicConduitRuleRuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitRuleRuleID.setStatus("current")
_TnStatsDynamicConduitRuleGlobalRuleIndex_Type = Integer32
_TnStatsDynamicConduitRuleGlobalRuleIndex_Object = MibTableColumn
tnStatsDynamicConduitRuleGlobalRuleIndex = _TnStatsDynamicConduitRuleGlobalRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 5, 1, 1, 5),
    _TnStatsDynamicConduitRuleGlobalRuleIndex_Type()
)
tnStatsDynamicConduitRuleGlobalRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitRuleGlobalRuleIndex.setStatus("current")
_TnStatsDynamicConduitRuleApplicationName_Type = DisplayString
_TnStatsDynamicConduitRuleApplicationName_Object = MibTableColumn
tnStatsDynamicConduitRuleApplicationName = _TnStatsDynamicConduitRuleApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 5, 1, 1, 6),
    _TnStatsDynamicConduitRuleApplicationName_Type()
)
tnStatsDynamicConduitRuleApplicationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitRuleApplicationName.setStatus("current")
_TnStatsDynamicConduitRuleWANIngressHitCount_Type = Gauge32
_TnStatsDynamicConduitRuleWANIngressHitCount_Object = MibTableColumn
tnStatsDynamicConduitRuleWANIngressHitCount = _TnStatsDynamicConduitRuleWANIngressHitCount_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 5, 1, 1, 7),
    _TnStatsDynamicConduitRuleWANIngressHitCount_Type()
)
tnStatsDynamicConduitRuleWANIngressHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitRuleWANIngressHitCount.setStatus("current")
_TnStatsDynamicConduitRuleWANEgressHitCount_Type = Gauge32
_TnStatsDynamicConduitRuleWANEgressHitCount_Object = MibTableColumn
tnStatsDynamicConduitRuleWANEgressHitCount = _TnStatsDynamicConduitRuleWANEgressHitCount_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 5, 1, 1, 8),
    _TnStatsDynamicConduitRuleWANEgressHitCount_Type()
)
tnStatsDynamicConduitRuleWANEgressHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitRuleWANEgressHitCount.setStatus("current")
_TnStatsDynamicConduitRuleBytesSent_Type = Gauge32
_TnStatsDynamicConduitRuleBytesSent_Object = MibTableColumn
tnStatsDynamicConduitRuleBytesSent = _TnStatsDynamicConduitRuleBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 5, 1, 1, 9),
    _TnStatsDynamicConduitRuleBytesSent_Type()
)
tnStatsDynamicConduitRuleBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitRuleBytesSent.setStatus("current")
_TnStatsDynamicConduitRulePacketsSent_Type = Gauge32
_TnStatsDynamicConduitRulePacketsSent_Object = MibTableColumn
tnStatsDynamicConduitRulePacketsSent = _TnStatsDynamicConduitRulePacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 5, 1, 1, 10),
    _TnStatsDynamicConduitRulePacketsSent_Type()
)
tnStatsDynamicConduitRulePacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitRulePacketsSent.setStatus("current")
_TnStatsDynamicConduitRuleBytesReceived_Type = Gauge32
_TnStatsDynamicConduitRuleBytesReceived_Object = MibTableColumn
tnStatsDynamicConduitRuleBytesReceived = _TnStatsDynamicConduitRuleBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 5, 1, 1, 11),
    _TnStatsDynamicConduitRuleBytesReceived_Type()
)
tnStatsDynamicConduitRuleBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitRuleBytesReceived.setStatus("current")
_TnStatsDynamicConduitRulePacketsReceived_Type = Gauge32
_TnStatsDynamicConduitRulePacketsReceived_Object = MibTableColumn
tnStatsDynamicConduitRulePacketsReceived = _TnStatsDynamicConduitRulePacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 5, 1, 1, 12),
    _TnStatsDynamicConduitRulePacketsReceived_Type()
)
tnStatsDynamicConduitRulePacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitRulePacketsReceived.setStatus("current")
_TnStatsDynamicConduitRuleBytesDropped_Type = Gauge32
_TnStatsDynamicConduitRuleBytesDropped_Object = MibTableColumn
tnStatsDynamicConduitRuleBytesDropped = _TnStatsDynamicConduitRuleBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 5, 1, 1, 13),
    _TnStatsDynamicConduitRuleBytesDropped_Type()
)
tnStatsDynamicConduitRuleBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitRuleBytesDropped.setStatus("current")
_TnStatsDynamicConduitRulePacketsDropped_Type = Gauge32
_TnStatsDynamicConduitRulePacketsDropped_Object = MibTableColumn
tnStatsDynamicConduitRulePacketsDropped = _TnStatsDynamicConduitRulePacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 5, 1, 1, 14),
    _TnStatsDynamicConduitRulePacketsDropped_Type()
)
tnStatsDynamicConduitRulePacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitRulePacketsDropped.setStatus("current")
_TnStatsDynamicConduitRuleLastActiveNMinuteAgo_Type = TimeTicks
_TnStatsDynamicConduitRuleLastActiveNMinuteAgo_Object = MibTableColumn
tnStatsDynamicConduitRuleLastActiveNMinuteAgo = _TnStatsDynamicConduitRuleLastActiveNMinuteAgo_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 22, 5, 1, 1, 15),
    _TnStatsDynamicConduitRuleLastActiveNMinuteAgo_Type()
)
tnStatsDynamicConduitRuleLastActiveNMinuteAgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsDynamicConduitRuleLastActiveNMinuteAgo.setStatus("current")
_TnStatsArp_ObjectIdentity = ObjectIdentity
tnStatsArp = _TnStatsArp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 23)
)
_TnStatsArpScalars_ObjectIdentity = ObjectIdentity
tnStatsArpScalars = _TnStatsArpScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 23, 1)
)


class _TnStatsNumArpEntries_Type(Integer32):
    """Custom type tnStatsNumArpEntries based on Integer32"""
    defaultValue = 0


_TnStatsNumArpEntries_Type.__name__ = "Integer32"
_TnStatsNumArpEntries_Object = MibScalar
tnStatsNumArpEntries = _TnStatsNumArpEntries_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 23, 1, 1),
    _TnStatsNumArpEntries_Type()
)
tnStatsNumArpEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsNumArpEntries.setStatus("current")
_TnStatsArpTable_Object = MibTable
tnStatsArpTable = _TnStatsArpTable_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 23, 2)
)
if mibBuilder.loadTexts:
    tnStatsArpTable.setStatus("current")
_TnStatsArpEntry_Object = MibTableRow
tnStatsArpEntry = _TnStatsArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 23, 2, 1)
)
tnStatsArpEntry.setIndexNames(
    (0, "TALARI-MIB", "tnStatsArpID"),
)
if mibBuilder.loadTexts:
    tnStatsArpEntry.setStatus("current")
_TnStatsArpID_Type = Integer32
_TnStatsArpID_Object = MibTableColumn
tnStatsArpID = _TnStatsArpID_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 23, 2, 1, 1),
    _TnStatsArpID_Type()
)
tnStatsArpID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsArpID.setStatus("current")
_TnStatsArpIfIndex_Type = DisplayString
_TnStatsArpIfIndex_Object = MibTableColumn
tnStatsArpIfIndex = _TnStatsArpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 23, 2, 1, 2),
    _TnStatsArpIfIndex_Type()
)
tnStatsArpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsArpIfIndex.setStatus("current")
_TnStatsArpVlanTag_Type = Counter64
_TnStatsArpVlanTag_Object = MibTableColumn
tnStatsArpVlanTag = _TnStatsArpVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 23, 2, 1, 3),
    _TnStatsArpVlanTag_Type()
)
tnStatsArpVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsArpVlanTag.setStatus("current")
_TnStatsArpIpAddr_Type = IpAddress
_TnStatsArpIpAddr_Object = MibTableColumn
tnStatsArpIpAddr = _TnStatsArpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 23, 2, 1, 4),
    _TnStatsArpIpAddr_Type()
)
tnStatsArpIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsArpIpAddr.setStatus("current")
_TnStatsArpPhysAddr_Type = PhysAddress
_TnStatsArpPhysAddr_Object = MibTableColumn
tnStatsArpPhysAddr = _TnStatsArpPhysAddr_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 23, 2, 1, 5),
    _TnStatsArpPhysAddr_Type()
)
tnStatsArpPhysAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsArpPhysAddr.setStatus("current")
_TnStatsArpState_Type = DisplayString
_TnStatsArpState_Object = MibTableColumn
tnStatsArpState = _TnStatsArpState_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 23, 2, 1, 6),
    _TnStatsArpState_Type()
)
tnStatsArpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsArpState.setStatus("current")
_TnStatsArpType_Type = DisplayString
_TnStatsArpType_Object = MibTableColumn
tnStatsArpType = _TnStatsArpType_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 23, 2, 1, 7),
    _TnStatsArpType_Type()
)
tnStatsArpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsArpType.setStatus("current")
_TnStatsArpReplyAgeMs_Type = Counter64
_TnStatsArpReplyAgeMs_Object = MibTableColumn
tnStatsArpReplyAgeMs = _TnStatsArpReplyAgeMs_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 23, 2, 1, 8),
    _TnStatsArpReplyAgeMs_Type()
)
tnStatsArpReplyAgeMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsArpReplyAgeMs.setStatus("current")
_TnStatsLanGRETunnels_ObjectIdentity = ObjectIdentity
tnStatsLanGRETunnels = _TnStatsLanGRETunnels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 24)
)
_TnStatsLanGRETunnelScalars_ObjectIdentity = ObjectIdentity
tnStatsLanGRETunnelScalars = _TnStatsLanGRETunnelScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 24, 1)
)


class _TnStatsNumLanGRETunnels_Type(Integer32):
    """Custom type tnStatsNumLanGRETunnels based on Integer32"""
    defaultValue = 0


_TnStatsNumLanGRETunnels_Type.__name__ = "Integer32"
_TnStatsNumLanGRETunnels_Object = MibScalar
tnStatsNumLanGRETunnels = _TnStatsNumLanGRETunnels_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 24, 1, 1),
    _TnStatsNumLanGRETunnels_Type()
)
tnStatsNumLanGRETunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsNumLanGRETunnels.setStatus("current")
_TnStatsLanGRETunnelTable_Object = MibTable
tnStatsLanGRETunnelTable = _TnStatsLanGRETunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 24, 2)
)
if mibBuilder.loadTexts:
    tnStatsLanGRETunnelTable.setStatus("current")
_TnStatsLanGRETunnelEntry_Object = MibTableRow
tnStatsLanGRETunnelEntry = _TnStatsLanGRETunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 24, 2, 1)
)
tnStatsLanGRETunnelEntry.setIndexNames(
    (0, "TALARI-MIB", "tnStatsLanGRETunnelIndex"),
)
if mibBuilder.loadTexts:
    tnStatsLanGRETunnelEntry.setStatus("current")
_TnStatsLanGRETunnelIndex_Type = Integer32
_TnStatsLanGRETunnelIndex_Object = MibTableColumn
tnStatsLanGRETunnelIndex = _TnStatsLanGRETunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 24, 2, 1, 1),
    _TnStatsLanGRETunnelIndex_Type()
)
tnStatsLanGRETunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsLanGRETunnelIndex.setStatus("current")
_TnStatsLanGRETunnelName_Type = DisplayString
_TnStatsLanGRETunnelName_Object = MibTableColumn
tnStatsLanGRETunnelName = _TnStatsLanGRETunnelName_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 24, 2, 1, 2),
    _TnStatsLanGRETunnelName_Type()
)
tnStatsLanGRETunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsLanGRETunnelName.setStatus("current")
_TnStatsLanGRETunnelState_Type = DisplayString
_TnStatsLanGRETunnelState_Object = MibTableColumn
tnStatsLanGRETunnelState = _TnStatsLanGRETunnelState_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 24, 2, 1, 3),
    _TnStatsLanGRETunnelState_Type()
)
tnStatsLanGRETunnelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsLanGRETunnelState.setStatus("current")
_TnStatsLanGRETunnelKeepaliveRequestSent_Type = Counter64
_TnStatsLanGRETunnelKeepaliveRequestSent_Object = MibTableColumn
tnStatsLanGRETunnelKeepaliveRequestSent = _TnStatsLanGRETunnelKeepaliveRequestSent_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 24, 2, 1, 4),
    _TnStatsLanGRETunnelKeepaliveRequestSent_Type()
)
tnStatsLanGRETunnelKeepaliveRequestSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsLanGRETunnelKeepaliveRequestSent.setStatus("current")
_TnStatsLanGRETunnelKeepaliveReplyReceived_Type = Counter64
_TnStatsLanGRETunnelKeepaliveReplyReceived_Object = MibTableColumn
tnStatsLanGRETunnelKeepaliveReplyReceived = _TnStatsLanGRETunnelKeepaliveReplyReceived_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 24, 2, 1, 5),
    _TnStatsLanGRETunnelKeepaliveReplyReceived_Type()
)
tnStatsLanGRETunnelKeepaliveReplyReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsLanGRETunnelKeepaliveReplyReceived.setStatus("current")
_TnStatsLanGRETunnelKeepaliveReplySent_Type = Counter64
_TnStatsLanGRETunnelKeepaliveReplySent_Object = MibTableColumn
tnStatsLanGRETunnelKeepaliveReplySent = _TnStatsLanGRETunnelKeepaliveReplySent_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 24, 2, 1, 6),
    _TnStatsLanGRETunnelKeepaliveReplySent_Type()
)
tnStatsLanGRETunnelKeepaliveReplySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsLanGRETunnelKeepaliveReplySent.setStatus("current")
_TnStatsLanGRETunnelPacketsSent_Type = Counter64
_TnStatsLanGRETunnelPacketsSent_Object = MibTableColumn
tnStatsLanGRETunnelPacketsSent = _TnStatsLanGRETunnelPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 24, 2, 1, 7),
    _TnStatsLanGRETunnelPacketsSent_Type()
)
tnStatsLanGRETunnelPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsLanGRETunnelPacketsSent.setStatus("current")
_TnStatsLanGRETunnelBytesSent_Type = Counter64
_TnStatsLanGRETunnelBytesSent_Object = MibTableColumn
tnStatsLanGRETunnelBytesSent = _TnStatsLanGRETunnelBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 24, 2, 1, 8),
    _TnStatsLanGRETunnelBytesSent_Type()
)
tnStatsLanGRETunnelBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsLanGRETunnelBytesSent.setStatus("current")
_TnStatsLanGRETunnelPacketsSentDropped_Type = Counter64
_TnStatsLanGRETunnelPacketsSentDropped_Object = MibTableColumn
tnStatsLanGRETunnelPacketsSentDropped = _TnStatsLanGRETunnelPacketsSentDropped_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 24, 2, 1, 9),
    _TnStatsLanGRETunnelPacketsSentDropped_Type()
)
tnStatsLanGRETunnelPacketsSentDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsLanGRETunnelPacketsSentDropped.setStatus("current")
_TnStatsLanGRETunnelBytesSentDropped_Type = Counter64
_TnStatsLanGRETunnelBytesSentDropped_Object = MibTableColumn
tnStatsLanGRETunnelBytesSentDropped = _TnStatsLanGRETunnelBytesSentDropped_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 24, 2, 1, 10),
    _TnStatsLanGRETunnelBytesSentDropped_Type()
)
tnStatsLanGRETunnelBytesSentDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsLanGRETunnelBytesSentDropped.setStatus("current")
_TnStatsLanGRETunnelPacketsSentFragmented_Type = Counter64
_TnStatsLanGRETunnelPacketsSentFragmented_Object = MibTableColumn
tnStatsLanGRETunnelPacketsSentFragmented = _TnStatsLanGRETunnelPacketsSentFragmented_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 24, 2, 1, 11),
    _TnStatsLanGRETunnelPacketsSentFragmented_Type()
)
tnStatsLanGRETunnelPacketsSentFragmented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsLanGRETunnelPacketsSentFragmented.setStatus("current")
_TnStatsLanGRETunnelPacketsReceived_Type = Counter64
_TnStatsLanGRETunnelPacketsReceived_Object = MibTableColumn
tnStatsLanGRETunnelPacketsReceived = _TnStatsLanGRETunnelPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 24, 2, 1, 12),
    _TnStatsLanGRETunnelPacketsReceived_Type()
)
tnStatsLanGRETunnelPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsLanGRETunnelPacketsReceived.setStatus("current")
_TnStatsLanGRETunnelBytesReceived_Type = Counter64
_TnStatsLanGRETunnelBytesReceived_Object = MibTableColumn
tnStatsLanGRETunnelBytesReceived = _TnStatsLanGRETunnelBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 24, 2, 1, 13),
    _TnStatsLanGRETunnelBytesReceived_Type()
)
tnStatsLanGRETunnelBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsLanGRETunnelBytesReceived.setStatus("current")
_TnStatsLanGRETunnelPacketsReceivedDropped_Type = Counter64
_TnStatsLanGRETunnelPacketsReceivedDropped_Object = MibTableColumn
tnStatsLanGRETunnelPacketsReceivedDropped = _TnStatsLanGRETunnelPacketsReceivedDropped_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 24, 2, 1, 14),
    _TnStatsLanGRETunnelPacketsReceivedDropped_Type()
)
tnStatsLanGRETunnelPacketsReceivedDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsLanGRETunnelPacketsReceivedDropped.setStatus("current")
_TnStatsLanGRETunnelBytesReceivedDropped_Type = Counter64
_TnStatsLanGRETunnelBytesReceivedDropped_Object = MibTableColumn
tnStatsLanGRETunnelBytesReceivedDropped = _TnStatsLanGRETunnelBytesReceivedDropped_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 24, 2, 1, 15),
    _TnStatsLanGRETunnelBytesReceivedDropped_Type()
)
tnStatsLanGRETunnelBytesReceivedDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsLanGRETunnelBytesReceivedDropped.setStatus("current")
_TnStatsLanGRETunnelRoutingDomainName_Type = DisplayString
_TnStatsLanGRETunnelRoutingDomainName_Object = MibTableColumn
tnStatsLanGRETunnelRoutingDomainName = _TnStatsLanGRETunnelRoutingDomainName_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 2, 24, 2, 1, 16),
    _TnStatsLanGRETunnelRoutingDomainName_Type()
)
tnStatsLanGRETunnelRoutingDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStatsLanGRETunnelRoutingDomainName.setStatus("current")
_TalariEvents_ObjectIdentity = ObjectIdentity
talariEvents = _TalariEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 2, 3)
)
_TalariEventScalars_ObjectIdentity = ObjectIdentity
talariEventScalars = _TalariEventScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 2, 3, 1)
)


class _TalariNumEvents_Type(Gauge32):
    """Custom type talariNumEvents based on Gauge32"""
    defaultValue = 0


_TalariNumEvents_Type.__name__ = "Gauge32"
_TalariNumEvents_Object = MibScalar
talariNumEvents = _TalariNumEvents_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 3, 1, 1),
    _TalariNumEvents_Type()
)
talariNumEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    talariNumEvents.setStatus("current")
_TalariEventTable_Object = MibTable
talariEventTable = _TalariEventTable_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 3, 2)
)
if mibBuilder.loadTexts:
    talariEventTable.setStatus("current")
_TalariEventEntry_Object = MibTableRow
talariEventEntry = _TalariEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 3, 2, 1)
)
talariEventEntry.setIndexNames(
    (0, "TALARI-MIB", "talariEventIndex"),
)
if mibBuilder.loadTexts:
    talariEventEntry.setStatus("current")
_TalariEventIndex_Type = Integer32
_TalariEventIndex_Object = MibTableColumn
talariEventIndex = _TalariEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 3, 2, 1, 1),
    _TalariEventIndex_Type()
)
talariEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    talariEventIndex.setStatus("current")
_TalariEventID_Type = Integer32
_TalariEventID_Object = MibTableColumn
talariEventID = _TalariEventID_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 3, 2, 1, 2),
    _TalariEventID_Type()
)
talariEventID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    talariEventID.setStatus("current")
_TalariEventObjectID_Type = Integer32
_TalariEventObjectID_Object = MibTableColumn
talariEventObjectID = _TalariEventObjectID_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 3, 2, 1, 3),
    _TalariEventObjectID_Type()
)
talariEventObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    talariEventObjectID.setStatus("current")
_TalariEventObjectName_Type = DisplayString
_TalariEventObjectName_Object = MibTableColumn
talariEventObjectName = _TalariEventObjectName_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 3, 2, 1, 4),
    _TalariEventObjectName_Type()
)
talariEventObjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    talariEventObjectName.setStatus("current")
_TalariEventObjectType_Type = TalariEventObjectTypeEnum
_TalariEventObjectType_Object = MibTableColumn
talariEventObjectType = _TalariEventObjectType_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 3, 2, 1, 5),
    _TalariEventObjectType_Type()
)
talariEventObjectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    talariEventObjectType.setStatus("current")
_TalariEventTime_Type = DisplayString
_TalariEventTime_Object = MibTableColumn
talariEventTime = _TalariEventTime_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 3, 2, 1, 6),
    _TalariEventTime_Type()
)
talariEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    talariEventTime.setStatus("current")
_TalariEventType_Type = TalariEventStateEnum
_TalariEventType_Object = MibTableColumn
talariEventType = _TalariEventType_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 3, 2, 1, 7),
    _TalariEventType_Type()
)
talariEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    talariEventType.setStatus("current")
_TalariEventSeverity_Type = TalariEventSeverityEnum
_TalariEventSeverity_Object = MibTableColumn
talariEventSeverity = _TalariEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 3, 2, 1, 8),
    _TalariEventSeverity_Type()
)
talariEventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    talariEventSeverity.setStatus("current")
_TalariEventDescription_Type = DisplayString
_TalariEventDescription_Object = MibTableColumn
talariEventDescription = _TalariEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 3, 2, 1, 9),
    _TalariEventDescription_Type()
)
talariEventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    talariEventDescription.setStatus("current")
_TalariNetworkEventScalars_ObjectIdentity = ObjectIdentity
talariNetworkEventScalars = _TalariNetworkEventScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 2, 3, 3)
)
_TalariNetworkEventAPNID_Type = Integer32
_TalariNetworkEventAPNID_Object = MibScalar
talariNetworkEventAPNID = _TalariNetworkEventAPNID_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 3, 3, 1),
    _TalariNetworkEventAPNID_Type()
)
talariNetworkEventAPNID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    talariNetworkEventAPNID.setStatus("current")
_TalariNetworkEventSiteID_Type = Integer32
_TalariNetworkEventSiteID_Object = MibScalar
talariNetworkEventSiteID = _TalariNetworkEventSiteID_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 3, 3, 2),
    _TalariNetworkEventSiteID_Type()
)
talariNetworkEventSiteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    talariNetworkEventSiteID.setStatus("current")
_TalariNetworkEventApplianceID_Type = Integer32
_TalariNetworkEventApplianceID_Object = MibScalar
talariNetworkEventApplianceID = _TalariNetworkEventApplianceID_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 3, 3, 3),
    _TalariNetworkEventApplianceID_Type()
)
talariNetworkEventApplianceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    talariNetworkEventApplianceID.setStatus("current")
_TalariNetworkEventSiteName_Type = DisplayString
_TalariNetworkEventSiteName_Object = MibScalar
talariNetworkEventSiteName = _TalariNetworkEventSiteName_Object(
    (1, 3, 6, 1, 4, 1, 34086, 2, 3, 3, 4),
    _TalariNetworkEventSiteName_Type()
)
talariNetworkEventSiteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    talariNetworkEventSiteName.setStatus("current")
_TalariNotifs_ObjectIdentity = ObjectIdentity
talariNotifs = _TalariNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 3)
)
_TalariConform_ObjectIdentity = ObjectIdentity
talariConform = _TalariConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 4)
)
_TalariAgentOIDs_ObjectIdentity = ObjectIdentity
talariAgentOIDs = _TalariAgentOIDs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 5)
)
_TalariAPNAppliance_ObjectIdentity = ObjectIdentity
talariAPNAppliance = _TalariAPNAppliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 5, 1)
)
_TalariT200_ObjectIdentity = ObjectIdentity
talariT200 = _TalariT200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 5, 2)
)
_TalariT700_ObjectIdentity = ObjectIdentity
talariT700 = _TalariT700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 5, 3)
)
_TalariT730_ObjectIdentity = ObjectIdentity
talariT730 = _TalariT730_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 5, 4)
)
_TalariT750_ObjectIdentity = ObjectIdentity
talariT750 = _TalariT750_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 5, 5)
)
_TalariT3000_ObjectIdentity = ObjectIdentity
talariT3000 = _TalariT3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 5, 6)
)
_TalariVT100_ObjectIdentity = ObjectIdentity
talariVT100 = _TalariVT100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 5, 7)
)
_TalariT510_ObjectIdentity = ObjectIdentity
talariT510 = _TalariT510_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 5, 8)
)
_TalariT5000_ObjectIdentity = ObjectIdentity
talariT5000 = _TalariT5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 5, 9)
)
_TalariT3010_ObjectIdentity = ObjectIdentity
talariT3010 = _TalariT3010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 5, 10)
)
_TalariT860_ObjectIdentity = ObjectIdentity
talariT860 = _TalariT860_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 5, 11)
)
_TalariCT800_ObjectIdentity = ObjectIdentity
talariCT800 = _TalariCT800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 5, 12)
)
_TalariVT500_ObjectIdentity = ObjectIdentity
talariVT500 = _TalariVT500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 5, 13)
)
_TalariT5200_ObjectIdentity = ObjectIdentity
talariT5200 = _TalariT5200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 5, 14)
)
_TalariVT800_ObjectIdentity = ObjectIdentity
talariVT800 = _TalariVT800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 5, 15)
)
_TalariE100_ObjectIdentity = ObjectIdentity
talariE100 = _TalariE100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 5, 16)
)
_TalariVCN800_ObjectIdentity = ObjectIdentity
talariVCN800 = _TalariVCN800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 5, 17)
)
_TalariE1000_ObjectIdentity = ObjectIdentity
talariE1000 = _TalariE1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 5, 18)
)
_TalariE50_ObjectIdentity = ObjectIdentity
talariE50 = _TalariE50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 5, 19)
)
_TalariE500_ObjectIdentity = ObjectIdentity
talariE500 = _TalariE500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 5, 20)
)
_TalariVT800128_ObjectIdentity = ObjectIdentity
talariVT800128 = _TalariVT800128_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 5, 21)
)
_TalariCT800128_ObjectIdentity = ObjectIdentity
talariCT800128 = _TalariCT800128_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34086, 5, 22)
)

# Managed Objects groups


# Notification objects

talariEventNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 34086, 3, 1)
)
talariEventNotification.setObjects(
      *(("TALARI-MIB", "talariEventIndex"),
        ("TALARI-MIB", "talariEventID"),
        ("TALARI-MIB", "talariEventObjectID"),
        ("TALARI-MIB", "talariEventObjectName"),
        ("TALARI-MIB", "talariEventObjectType"),
        ("TALARI-MIB", "talariEventTime"),
        ("TALARI-MIB", "talariEventType"),
        ("TALARI-MIB", "talariEventSeverity"),
        ("TALARI-MIB", "talariEventDescription"))
)
if mibBuilder.loadTexts:
    talariEventNotification.setStatus(
        "current"
    )

talariNetworkEventNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 34086, 3, 2)
)
talariNetworkEventNotification.setObjects(
      *(("TALARI-MIB", "talariNetworkEventAPNID"),
        ("TALARI-MIB", "talariNetworkEventSiteID"),
        ("TALARI-MIB", "talariNetworkEventApplianceID"),
        ("TALARI-MIB", "talariNetworkEventSiteName"),
        ("TALARI-MIB", "talariEventID"),
        ("TALARI-MIB", "talariEventObjectID"),
        ("TALARI-MIB", "talariEventObjectName"),
        ("TALARI-MIB", "talariEventObjectType"),
        ("TALARI-MIB", "talariEventTime"),
        ("TALARI-MIB", "talariEventType"),
        ("TALARI-MIB", "talariEventSeverity"),
        ("TALARI-MIB", "talariEventDescription"))
)
if mibBuilder.loadTexts:
    talariNetworkEventNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TALARI-MIB",
    **{"TalariEventObjectTypeEnum": TalariEventObjectTypeEnum,
       "TalariEventSeverityEnum": TalariEventSeverityEnum,
       "TalariEventStateEnum": TalariEventStateEnum,
       "talari": talari,
       "talariObjects": talariObjects,
       "talariConfiguration": talariConfiguration,
       "talariStatistics": talariStatistics,
       "tnStatsAppliances": tnStatsAppliances,
       "tnStatsApplianceScalars": tnStatsApplianceScalars,
       "tnStatsApplianceName": tnStatsApplianceName,
       "tnStatsApplianceModel": tnStatsApplianceModel,
       "tnStatsApplianceModelName": tnStatsApplianceModelName,
       "tnStatsApplianceBytesSent": tnStatsApplianceBytesSent,
       "tnStatsAppliancePacketsSent": tnStatsAppliancePacketsSent,
       "tnStatsApplianceBytesReceived": tnStatsApplianceBytesReceived,
       "tnStatsAppliancePacketsReceived": tnStatsAppliancePacketsReceived,
       "tnStatsApplianceBytesDropped": tnStatsApplianceBytesDropped,
       "tnStatsAppliancePacketsDropped": tnStatsAppliancePacketsDropped,
       "tnStatsApplianceState": tnStatsApplianceState,
       "tnStatsApplianceHAState": tnStatsApplianceHAState,
       "tnStatsApplianceSerialNumber": tnStatsApplianceSerialNumber,
       "tnStatsApplianceOSVersion": tnStatsApplianceOSVersion,
       "tnStatsApplianceSoftwareVersion": tnStatsApplianceSoftwareVersion,
       "tnStatsApplianceConfigCreatedOn": tnStatsApplianceConfigCreatedOn,
       "tnStatsEthernetInterfaces": tnStatsEthernetInterfaces,
       "tnStatsEthernetInterfaceScalars": tnStatsEthernetInterfaceScalars,
       "tnStatsNumEthernetInterfaces": tnStatsNumEthernetInterfaces,
       "tnStatsEthernetInterfaceTable": tnStatsEthernetInterfaceTable,
       "tnStatsEthernetInterfaceEntry": tnStatsEthernetInterfaceEntry,
       "tnStatsEthernetInterfaceIndex": tnStatsEthernetInterfaceIndex,
       "tnStatsEthernetInterfaceIfIndex": tnStatsEthernetInterfaceIfIndex,
       "tnStatsEthernetInterfaceName": tnStatsEthernetInterfaceName,
       "tnStatsEthernetInterfaceBytesSent": tnStatsEthernetInterfaceBytesSent,
       "tnStatsEthernetInterfacePacketsSent": tnStatsEthernetInterfacePacketsSent,
       "tnStatsEthernetInterfaceBytesReceived": tnStatsEthernetInterfaceBytesReceived,
       "tnStatsEthernetInterfacePacketsReceived": tnStatsEthernetInterfacePacketsReceived,
       "tnStatsEthernetInterfaceBytesDropped": tnStatsEthernetInterfaceBytesDropped,
       "tnStatsEthernetInterfacePacketsDropped": tnStatsEthernetInterfacePacketsDropped,
       "tnStatsRoutes": tnStatsRoutes,
       "tnStatsRouteTable": tnStatsRouteTable,
       "tnStatsRouteEntry": tnStatsRouteEntry,
       "tnStatsRouteIndex": tnStatsRouteIndex,
       "tnStatsRouteID": tnStatsRouteID,
       "tnStatsRouteHitCount": tnStatsRouteHitCount,
       "tnStatsRules": tnStatsRules,
       "tnStatsRuleScalars": tnStatsRuleScalars,
       "tnStatsNumRules": tnStatsNumRules,
       "tnStatsRuleTable": tnStatsRuleTable,
       "tnStatsRuleEntry": tnStatsRuleEntry,
       "tnStatsRuleIndex": tnStatsRuleIndex,
       "tnStatsRuleID": tnStatsRuleID,
       "tnStatsRuleApplicationName": tnStatsRuleApplicationName,
       "tnStatsRuleWANIngressHitCount": tnStatsRuleWANIngressHitCount,
       "tnStatsRuleWANEgressHitCount": tnStatsRuleWANEgressHitCount,
       "tnStatsRuleBytesSent": tnStatsRuleBytesSent,
       "tnStatsRulePacketsSent": tnStatsRulePacketsSent,
       "tnStatsRuleBytesReceived": tnStatsRuleBytesReceived,
       "tnStatsRulePacketsReceived": tnStatsRulePacketsReceived,
       "tnStatsRuleBytesDropped": tnStatsRuleBytesDropped,
       "tnStatsRulePacketsDropped": tnStatsRulePacketsDropped,
       "tnStatsRuleLastActiveNMinuteAgo": tnStatsRuleLastActiveNMinuteAgo,
       "tnStatsWANLinks": tnStatsWANLinks,
       "tnStatsWANLinkScalars": tnStatsWANLinkScalars,
       "tnStatsNumWANLinks": tnStatsNumWANLinks,
       "tnStatsWANLinkTable": tnStatsWANLinkTable,
       "tnStatsWANLinkEntry": tnStatsWANLinkEntry,
       "tnStatsWANLinkIndex": tnStatsWANLinkIndex,
       "tnStatsWANLinkID": tnStatsWANLinkID,
       "tnStatsWANLinkName": tnStatsWANLinkName,
       "tnStatsWANLinkState": tnStatsWANLinkState,
       "tnStatsWANLinkBytesSent": tnStatsWANLinkBytesSent,
       "tnStatsWANLinkPacketsSent": tnStatsWANLinkPacketsSent,
       "tnStatsWANLinkBytesReceived": tnStatsWANLinkBytesReceived,
       "tnStatsWANLinkPacketsReceived": tnStatsWANLinkPacketsReceived,
       "tnStatsWANLinkBytesDropped": tnStatsWANLinkBytesDropped,
       "tnStatsWANLinkPacketsDropped": tnStatsWANLinkPacketsDropped,
       "tnStatsConduits": tnStatsConduits,
       "tnStatsConduitScalars": tnStatsConduitScalars,
       "tnStatsNumConduits": tnStatsNumConduits,
       "tnStatsConduitTable": tnStatsConduitTable,
       "tnStatsConduitEntry": tnStatsConduitEntry,
       "tnStatsConduitIndex": tnStatsConduitIndex,
       "tnStatsConduitID": tnStatsConduitID,
       "tnStatsConduitName": tnStatsConduitName,
       "tnStatsConduitState": tnStatsConduitState,
       "tnStatsConduitBytesSent": tnStatsConduitBytesSent,
       "tnStatsConduitPacketsSent": tnStatsConduitPacketsSent,
       "tnStatsConduitBytesReceived": tnStatsConduitBytesReceived,
       "tnStatsConduitPacketsReceived": tnStatsConduitPacketsReceived,
       "tnStatsConduitBytesDropped": tnStatsConduitBytesDropped,
       "tnStatsConduitPacketsDropped": tnStatsConduitPacketsDropped,
       "tnStatsConduitBOWTms": tnStatsConduitBOWTms,
       "tnStatsConduitJitterms": tnStatsConduitJitterms,
       "tnStatsConduitNumPaths": tnStatsConduitNumPaths,
       "tnStatsConduitNumRules": tnStatsConduitNumRules,
       "tnStatsConduitPacketsLost": tnStatsConduitPacketsLost,
       "tnStatsConduitSendBytesDropped": tnStatsConduitSendBytesDropped,
       "tnStatsConduitSendPacketsDropped": tnStatsConduitSendPacketsDropped,
       "tnStatsConduitSendPacketsLost": tnStatsConduitSendPacketsLost,
       "tnStatsConduitSendPacketsOOO": tnStatsConduitSendPacketsOOO,
       "tnStatsConduitSendBOWTms": tnStatsConduitSendBOWTms,
       "tnStatsConduitSendJitterms": tnStatsConduitSendJitterms,
       "tnStatsConduitReceiveBytesDropped": tnStatsConduitReceiveBytesDropped,
       "tnStatsConduitReceivePacketsDropped": tnStatsConduitReceivePacketsDropped,
       "tnStatsConduitReceivePacketsLost": tnStatsConduitReceivePacketsLost,
       "tnStatsConduitReceivePacketsOOO": tnStatsConduitReceivePacketsOOO,
       "tnStatsConduitReceiveBOWTms": tnStatsConduitReceiveBOWTms,
       "tnStatsConduitReceiveJitterms": tnStatsConduitReceiveJitterms,
       "tnStatsConduitPaths": tnStatsConduitPaths,
       "tnStatsConduitPathTable": tnStatsConduitPathTable,
       "tnStatsConduitPathEntry": tnStatsConduitPathEntry,
       "tnStatsConduitPathConduitIndex": tnStatsConduitPathConduitIndex,
       "tnStatsConduitPathPathIndex": tnStatsConduitPathPathIndex,
       "tnStatsConduitPathConduitID": tnStatsConduitPathConduitID,
       "tnStatsConduitPathPathID": tnStatsConduitPathPathID,
       "tnStatsConduitPathName": tnStatsConduitPathName,
       "tnStatsConduitPathState": tnStatsConduitPathState,
       "tnStatsConduitPathBytesSent": tnStatsConduitPathBytesSent,
       "tnStatsConduitPathPacketsSent": tnStatsConduitPathPacketsSent,
       "tnStatsConduitPathBytesReceived": tnStatsConduitPathBytesReceived,
       "tnStatsConduitPathPacketsReceived": tnStatsConduitPathPacketsReceived,
       "tnStatsConduitPathBytesDropped": tnStatsConduitPathBytesDropped,
       "tnStatsConduitPathPacketsDropped": tnStatsConduitPathPacketsDropped,
       "tnStatsConduitPathBOWTms": tnStatsConduitPathBOWTms,
       "tnStatsConduitPathJitterms": tnStatsConduitPathJitterms,
       "tnStatsConduitPathPacketsLost": tnStatsConduitPathPacketsLost,
       "tnStatsConduitPathPacketsOOO": tnStatsConduitPathPacketsOOO,
       "tnStatsConduitClasses": tnStatsConduitClasses,
       "tnStatsConduitClassTable": tnStatsConduitClassTable,
       "tnStatsConduitClassEntry": tnStatsConduitClassEntry,
       "tnStatsConduitClassConduitIndex": tnStatsConduitClassConduitIndex,
       "tnStatsConduitClassClassIndex": tnStatsConduitClassClassIndex,
       "tnStatsConduitClassConduitID": tnStatsConduitClassConduitID,
       "tnStatsConduitClassClassID": tnStatsConduitClassClassID,
       "tnStatsConduitClassName": tnStatsConduitClassName,
       "tnStatsConduitClassType": tnStatsConduitClassType,
       "tnStatsConduitClassBytesSent": tnStatsConduitClassBytesSent,
       "tnStatsConduitClassPacketsSent": tnStatsConduitClassPacketsSent,
       "tnStatsConduitClassBytesPending": tnStatsConduitClassBytesPending,
       "tnStatsConduitClassPacketsPending": tnStatsConduitClassPacketsPending,
       "tnStatsConduitClassBytesDropped": tnStatsConduitClassBytesDropped,
       "tnStatsConduitClassPacketsDropped": tnStatsConduitClassPacketsDropped,
       "tnStatsConduitRules": tnStatsConduitRules,
       "tnStatsConduitRuleTable": tnStatsConduitRuleTable,
       "tnStatsConduitRuleEntry": tnStatsConduitRuleEntry,
       "tnStatsConduitRuleConduitIndex": tnStatsConduitRuleConduitIndex,
       "tnStatsConduitRuleRuleIndex": tnStatsConduitRuleRuleIndex,
       "tnStatsConduitRuleConduitID": tnStatsConduitRuleConduitID,
       "tnStatsConduitRuleRuleID": tnStatsConduitRuleRuleID,
       "tnStatsConduitRuleGlobalRuleIndex": tnStatsConduitRuleGlobalRuleIndex,
       "tnStatsConduitRuleApplicationName": tnStatsConduitRuleApplicationName,
       "tnStatsConduitRuleWANIngressHitCount": tnStatsConduitRuleWANIngressHitCount,
       "tnStatsConduitRuleWANEgressHitCount": tnStatsConduitRuleWANEgressHitCount,
       "tnStatsConduitRuleBytesSent": tnStatsConduitRuleBytesSent,
       "tnStatsConduitRulePacketsSent": tnStatsConduitRulePacketsSent,
       "tnStatsConduitRuleBytesReceived": tnStatsConduitRuleBytesReceived,
       "tnStatsConduitRulePacketsReceived": tnStatsConduitRulePacketsReceived,
       "tnStatsConduitRuleBytesDropped": tnStatsConduitRuleBytesDropped,
       "tnStatsConduitRulePacketsDropped": tnStatsConduitRulePacketsDropped,
       "tnStatsConduitRuleLastActiveNMinuteAgo": tnStatsConduitRuleLastActiveNMinuteAgo,
       "tnStatsInternet": tnStatsInternet,
       "tnStatsInternetScalars": tnStatsInternetScalars,
       "tnStatsInternetBytesSent": tnStatsInternetBytesSent,
       "tnStatsInternetPacketsSent": tnStatsInternetPacketsSent,
       "tnStatsInternetBytesReceived": tnStatsInternetBytesReceived,
       "tnStatsInternetPacketsReceived": tnStatsInternetPacketsReceived,
       "tnStatsInternetBytesDropped": tnStatsInternetBytesDropped,
       "tnStatsInternetPacketsDropped": tnStatsInternetPacketsDropped,
       "tnStatsInternetNumRules": tnStatsInternetNumRules,
       "tnStatsInternetRuleTable": tnStatsInternetRuleTable,
       "tnStatsInternetRuleEntry": tnStatsInternetRuleEntry,
       "tnStatsInternetRuleIndex": tnStatsInternetRuleIndex,
       "tnStatsInternetRuleID": tnStatsInternetRuleID,
       "tnStatsInternetRuleGlobalRuleIndex": tnStatsInternetRuleGlobalRuleIndex,
       "tnStatsInternetRuleApplicationName": tnStatsInternetRuleApplicationName,
       "tnStatsInternetRuleWANIngressHitCount": tnStatsInternetRuleWANIngressHitCount,
       "tnStatsInternetRuleWANEgressHitCount": tnStatsInternetRuleWANEgressHitCount,
       "tnStatsInternetRuleBytesSent": tnStatsInternetRuleBytesSent,
       "tnStatsInternetRulePacketsSent": tnStatsInternetRulePacketsSent,
       "tnStatsInternetRuleBytesReceived": tnStatsInternetRuleBytesReceived,
       "tnStatsInternetRulePacketsReceived": tnStatsInternetRulePacketsReceived,
       "tnStatsInternetRuleBytesDropped": tnStatsInternetRuleBytesDropped,
       "tnStatsInternetRulePacketsDropped": tnStatsInternetRulePacketsDropped,
       "tnStatsInternetRuleLastActiveNMinuteAgo": tnStatsInternetRuleLastActiveNMinuteAgo,
       "tnStatsIntranet": tnStatsIntranet,
       "tnStatsIntranetScalars": tnStatsIntranetScalars,
       "tnStatsIntranetNumIntranetServices": tnStatsIntranetNumIntranetServices,
       "tnStatsIntranetsTable": tnStatsIntranetsTable,
       "tnStatsIntranetsEntry": tnStatsIntranetsEntry,
       "tnStatsIntranetsIndex": tnStatsIntranetsIndex,
       "tnStatsIntranetsID": tnStatsIntranetsID,
       "tnStatsIntranetsName": tnStatsIntranetsName,
       "tnStatsIntranetsBytesSent": tnStatsIntranetsBytesSent,
       "tnStatsIntranetsPacketsSent": tnStatsIntranetsPacketsSent,
       "tnStatsIntranetsBytesReceived": tnStatsIntranetsBytesReceived,
       "tnStatsIntranetsPacketsReceived": tnStatsIntranetsPacketsReceived,
       "tnStatsIntranetsBytesDropped": tnStatsIntranetsBytesDropped,
       "tnStatsIntranetsPacketsDropped": tnStatsIntranetsPacketsDropped,
       "tnStatsIntranetsNumRules": tnStatsIntranetsNumRules,
       "tnStatsIntranetsRoutingDomainName": tnStatsIntranetsRoutingDomainName,
       "tnStatsIntranetRulesTable": tnStatsIntranetRulesTable,
       "tnStatsIntranetRulesEntry": tnStatsIntranetRulesEntry,
       "tnStatsIntranetRulesIntranetIndex": tnStatsIntranetRulesIntranetIndex,
       "tnStatsIntranetRulesRuleIndex": tnStatsIntranetRulesRuleIndex,
       "tnStatsIntranetRulesID": tnStatsIntranetRulesID,
       "tnStatsIntranetRulesGlobalRuleIndex": tnStatsIntranetRulesGlobalRuleIndex,
       "tnStatsIntranetRulesIntranetName": tnStatsIntranetRulesIntranetName,
       "tnStatsIntranetRulesApplicationName": tnStatsIntranetRulesApplicationName,
       "tnStatsIntranetRulesWANIngressHitCount": tnStatsIntranetRulesWANIngressHitCount,
       "tnStatsIntranetRulesWANEgressHitCount": tnStatsIntranetRulesWANEgressHitCount,
       "tnStatsIntranetRulesBytesSent": tnStatsIntranetRulesBytesSent,
       "tnStatsIntranetRulesPacketsSent": tnStatsIntranetRulesPacketsSent,
       "tnStatsIntranetRulesBytesReceived": tnStatsIntranetRulesBytesReceived,
       "tnStatsIntranetRulesPacketsReceived": tnStatsIntranetRulesPacketsReceived,
       "tnStatsIntranetRulesBytesDropped": tnStatsIntranetRulesBytesDropped,
       "tnStatsIntranetRulesPacketsDropped": tnStatsIntranetRulesPacketsDropped,
       "tnStatsIntranetRulesLastActiveNMinuteAgo": tnStatsIntranetRulesLastActiveNMinuteAgo,
       "tnStatsPassthrough": tnStatsPassthrough,
       "tnStatsPassthroughScalars": tnStatsPassthroughScalars,
       "tnStatsPassthroughBytesSent": tnStatsPassthroughBytesSent,
       "tnStatsPassthroughPacketsSent": tnStatsPassthroughPacketsSent,
       "tnStatsPassthroughBytesReceived": tnStatsPassthroughBytesReceived,
       "tnStatsPassthroughPacketsReceived": tnStatsPassthroughPacketsReceived,
       "tnStatsPassthroughBytesDropped": tnStatsPassthroughBytesDropped,
       "tnStatsPassthroughPacketsDropped": tnStatsPassthroughPacketsDropped,
       "tnStatsRoutesV2": tnStatsRoutesV2,
       "tnStatsRouteScalars": tnStatsRouteScalars,
       "tnStatsNumRoutesV2": tnStatsNumRoutesV2,
       "tnStatsRouteTableV2": tnStatsRouteTableV2,
       "tnStatsRouteEntryV2": tnStatsRouteEntryV2,
       "tnStatsRouteIndexV2": tnStatsRouteIndexV2,
       "tnStatsRouteNetworkAddr": tnStatsRouteNetworkAddr,
       "tnStatsRouteNetworkPrefix": tnStatsRouteNetworkPrefix,
       "tnStatsRouteGateway": tnStatsRouteGateway,
       "tnStatsRouteFallback": tnStatsRouteFallback,
       "tnStatsRouteServiceType": tnStatsRouteServiceType,
       "tnStatsRouteServiceID": tnStatsRouteServiceID,
       "tnStatsRouteServiceName": tnStatsRouteServiceName,
       "tnStatsRouteReachable": tnStatsRouteReachable,
       "tnStatsRouteSiteName": tnStatsRouteSiteName,
       "tnStatsRouteType": tnStatsRouteType,
       "tnStatsRouteNeighborDirect": tnStatsRouteNeighborDirect,
       "tnStatsRouteCost": tnStatsRouteCost,
       "tnStatsRouteHitCountV2": tnStatsRouteHitCountV2,
       "tnStatsRouteEligible": tnStatsRouteEligible,
       "tnStatsRouteEligibilityType": tnStatsRouteEligibilityType,
       "tnStatsRouteEligibilityValue": tnStatsRouteEligibilityValue,
       "tnStatsRouteProtocol": tnStatsRouteProtocol,
       "tnStatsRouteRoutingDomainName": tnStatsRouteRoutingDomainName,
       "tnStatsDynamicConduits": tnStatsDynamicConduits,
       "tnStatsDynamicConduitScalars": tnStatsDynamicConduitScalars,
       "tnStatsNumDynamicConduits": tnStatsNumDynamicConduits,
       "tnStatsDynamicConduitTable": tnStatsDynamicConduitTable,
       "tnStatsDynamicConduitEntry": tnStatsDynamicConduitEntry,
       "tnStatsDynamicConduitIndex": tnStatsDynamicConduitIndex,
       "tnStatsDynamicConduitID": tnStatsDynamicConduitID,
       "tnStatsDynamicConduitName": tnStatsDynamicConduitName,
       "tnStatsDynamicConduitState": tnStatsDynamicConduitState,
       "tnStatsDynamicConduitTimeSinceCreation": tnStatsDynamicConduitTimeSinceCreation,
       "tnStatsDynamicConduitBytesSent": tnStatsDynamicConduitBytesSent,
       "tnStatsDynamicConduitPacketsSent": tnStatsDynamicConduitPacketsSent,
       "tnStatsDynamicConduitSendBytesDropped": tnStatsDynamicConduitSendBytesDropped,
       "tnStatsDynamicConduitSendPacketsDropped": tnStatsDynamicConduitSendPacketsDropped,
       "tnStatsDynamicConduitSendPacketsLost": tnStatsDynamicConduitSendPacketsLost,
       "tnStatsDynamicConduitSendPacketsOOO": tnStatsDynamicConduitSendPacketsOOO,
       "tnStatsDynamicConduitSendBOWTms": tnStatsDynamicConduitSendBOWTms,
       "tnStatsDynamicConduitSendJitterms": tnStatsDynamicConduitSendJitterms,
       "tnStatsDynamicConduitBytesReceived": tnStatsDynamicConduitBytesReceived,
       "tnStatsDynamicConduitPacketsReceived": tnStatsDynamicConduitPacketsReceived,
       "tnStatsDynamicConduitReceiveBytesDropped": tnStatsDynamicConduitReceiveBytesDropped,
       "tnStatsDynamicConduitReceivePacketsDropped": tnStatsDynamicConduitReceivePacketsDropped,
       "tnStatsDynamicConduitReceivePacketsLost": tnStatsDynamicConduitReceivePacketsLost,
       "tnStatsDynamicConduitReceivePacketsOOO": tnStatsDynamicConduitReceivePacketsOOO,
       "tnStatsDynamicConduitReceiveBOWTms": tnStatsDynamicConduitReceiveBOWTms,
       "tnStatsDynamicConduitReceiveJitterms": tnStatsDynamicConduitReceiveJitterms,
       "tnStatsDynamicConduitNumPaths": tnStatsDynamicConduitNumPaths,
       "tnStatsDynamicConduitNumRules": tnStatsDynamicConduitNumRules,
       "tnStatsDynamicConduitPaths": tnStatsDynamicConduitPaths,
       "tnStatsDynamicConduitPathTable": tnStatsDynamicConduitPathTable,
       "tnStatsDynamicConduitPathEntry": tnStatsDynamicConduitPathEntry,
       "tnStatsDynamicConduitPathConduitIndex": tnStatsDynamicConduitPathConduitIndex,
       "tnStatsDynamicConduitPathPathIndex": tnStatsDynamicConduitPathPathIndex,
       "tnStatsDynamicConduitPathConduitID": tnStatsDynamicConduitPathConduitID,
       "tnStatsDynamicConduitPathPathID": tnStatsDynamicConduitPathPathID,
       "tnStatsDynamicConduitPathName": tnStatsDynamicConduitPathName,
       "tnStatsDynamicConduitPathState": tnStatsDynamicConduitPathState,
       "tnStatsDynamicConduitPathBytesSent": tnStatsDynamicConduitPathBytesSent,
       "tnStatsDynamicConduitPathPacketsSent": tnStatsDynamicConduitPathPacketsSent,
       "tnStatsDynamicConduitPathBytesReceived": tnStatsDynamicConduitPathBytesReceived,
       "tnStatsDynamicConduitPathPacketsReceived": tnStatsDynamicConduitPathPacketsReceived,
       "tnStatsDynamicConduitPathBytesDropped": tnStatsDynamicConduitPathBytesDropped,
       "tnStatsDynamicConduitPathPacketsDropped": tnStatsDynamicConduitPathPacketsDropped,
       "tnStatsDynamicConduitPathBOWTms": tnStatsDynamicConduitPathBOWTms,
       "tnStatsDynamicConduitPathJitterms": tnStatsDynamicConduitPathJitterms,
       "tnStatsDynamicConduitPathPacketsLost": tnStatsDynamicConduitPathPacketsLost,
       "tnStatsDynamicConduitPathPacketsOOO": tnStatsDynamicConduitPathPacketsOOO,
       "tnStatsDynamicConduitClasses": tnStatsDynamicConduitClasses,
       "tnStatsDynamicConduitClassTable": tnStatsDynamicConduitClassTable,
       "tnStatsDynamicConduitClassEntry": tnStatsDynamicConduitClassEntry,
       "tnStatsDynamicConduitClassConduitIndex": tnStatsDynamicConduitClassConduitIndex,
       "tnStatsDynamicConduitClassClassIndex": tnStatsDynamicConduitClassClassIndex,
       "tnStatsDynamicConduitClassConduitID": tnStatsDynamicConduitClassConduitID,
       "tnStatsDynamicConduitClassClassID": tnStatsDynamicConduitClassClassID,
       "tnStatsDynamicConduitClassName": tnStatsDynamicConduitClassName,
       "tnStatsDynamicConduitClassType": tnStatsDynamicConduitClassType,
       "tnStatsDynamicConduitClassBytesSent": tnStatsDynamicConduitClassBytesSent,
       "tnStatsDynamicConduitClassPacketsSent": tnStatsDynamicConduitClassPacketsSent,
       "tnStatsDynamicConduitClassBytesPending": tnStatsDynamicConduitClassBytesPending,
       "tnStatsDynamicConduitClassPacketsPending": tnStatsDynamicConduitClassPacketsPending,
       "tnStatsDynamicConduitClassBytesDropped": tnStatsDynamicConduitClassBytesDropped,
       "tnStatsDynamicConduitClassPacketsDropped": tnStatsDynamicConduitClassPacketsDropped,
       "tnStatsDynamicConduitRules": tnStatsDynamicConduitRules,
       "tnStatsDynamicConduitRuleTable": tnStatsDynamicConduitRuleTable,
       "tnStatsDynamicConduitRuleEntry": tnStatsDynamicConduitRuleEntry,
       "tnStatsDynamicConduitRuleConduitIndex": tnStatsDynamicConduitRuleConduitIndex,
       "tnStatsDynamicConduitRuleRuleIndex": tnStatsDynamicConduitRuleRuleIndex,
       "tnStatsDynamicConduitRuleConduitID": tnStatsDynamicConduitRuleConduitID,
       "tnStatsDynamicConduitRuleRuleID": tnStatsDynamicConduitRuleRuleID,
       "tnStatsDynamicConduitRuleGlobalRuleIndex": tnStatsDynamicConduitRuleGlobalRuleIndex,
       "tnStatsDynamicConduitRuleApplicationName": tnStatsDynamicConduitRuleApplicationName,
       "tnStatsDynamicConduitRuleWANIngressHitCount": tnStatsDynamicConduitRuleWANIngressHitCount,
       "tnStatsDynamicConduitRuleWANEgressHitCount": tnStatsDynamicConduitRuleWANEgressHitCount,
       "tnStatsDynamicConduitRuleBytesSent": tnStatsDynamicConduitRuleBytesSent,
       "tnStatsDynamicConduitRulePacketsSent": tnStatsDynamicConduitRulePacketsSent,
       "tnStatsDynamicConduitRuleBytesReceived": tnStatsDynamicConduitRuleBytesReceived,
       "tnStatsDynamicConduitRulePacketsReceived": tnStatsDynamicConduitRulePacketsReceived,
       "tnStatsDynamicConduitRuleBytesDropped": tnStatsDynamicConduitRuleBytesDropped,
       "tnStatsDynamicConduitRulePacketsDropped": tnStatsDynamicConduitRulePacketsDropped,
       "tnStatsDynamicConduitRuleLastActiveNMinuteAgo": tnStatsDynamicConduitRuleLastActiveNMinuteAgo,
       "tnStatsArp": tnStatsArp,
       "tnStatsArpScalars": tnStatsArpScalars,
       "tnStatsNumArpEntries": tnStatsNumArpEntries,
       "tnStatsArpTable": tnStatsArpTable,
       "tnStatsArpEntry": tnStatsArpEntry,
       "tnStatsArpID": tnStatsArpID,
       "tnStatsArpIfIndex": tnStatsArpIfIndex,
       "tnStatsArpVlanTag": tnStatsArpVlanTag,
       "tnStatsArpIpAddr": tnStatsArpIpAddr,
       "tnStatsArpPhysAddr": tnStatsArpPhysAddr,
       "tnStatsArpState": tnStatsArpState,
       "tnStatsArpType": tnStatsArpType,
       "tnStatsArpReplyAgeMs": tnStatsArpReplyAgeMs,
       "tnStatsLanGRETunnels": tnStatsLanGRETunnels,
       "tnStatsLanGRETunnelScalars": tnStatsLanGRETunnelScalars,
       "tnStatsNumLanGRETunnels": tnStatsNumLanGRETunnels,
       "tnStatsLanGRETunnelTable": tnStatsLanGRETunnelTable,
       "tnStatsLanGRETunnelEntry": tnStatsLanGRETunnelEntry,
       "tnStatsLanGRETunnelIndex": tnStatsLanGRETunnelIndex,
       "tnStatsLanGRETunnelName": tnStatsLanGRETunnelName,
       "tnStatsLanGRETunnelState": tnStatsLanGRETunnelState,
       "tnStatsLanGRETunnelKeepaliveRequestSent": tnStatsLanGRETunnelKeepaliveRequestSent,
       "tnStatsLanGRETunnelKeepaliveReplyReceived": tnStatsLanGRETunnelKeepaliveReplyReceived,
       "tnStatsLanGRETunnelKeepaliveReplySent": tnStatsLanGRETunnelKeepaliveReplySent,
       "tnStatsLanGRETunnelPacketsSent": tnStatsLanGRETunnelPacketsSent,
       "tnStatsLanGRETunnelBytesSent": tnStatsLanGRETunnelBytesSent,
       "tnStatsLanGRETunnelPacketsSentDropped": tnStatsLanGRETunnelPacketsSentDropped,
       "tnStatsLanGRETunnelBytesSentDropped": tnStatsLanGRETunnelBytesSentDropped,
       "tnStatsLanGRETunnelPacketsSentFragmented": tnStatsLanGRETunnelPacketsSentFragmented,
       "tnStatsLanGRETunnelPacketsReceived": tnStatsLanGRETunnelPacketsReceived,
       "tnStatsLanGRETunnelBytesReceived": tnStatsLanGRETunnelBytesReceived,
       "tnStatsLanGRETunnelPacketsReceivedDropped": tnStatsLanGRETunnelPacketsReceivedDropped,
       "tnStatsLanGRETunnelBytesReceivedDropped": tnStatsLanGRETunnelBytesReceivedDropped,
       "tnStatsLanGRETunnelRoutingDomainName": tnStatsLanGRETunnelRoutingDomainName,
       "talariEvents": talariEvents,
       "talariEventScalars": talariEventScalars,
       "talariNumEvents": talariNumEvents,
       "talariEventTable": talariEventTable,
       "talariEventEntry": talariEventEntry,
       "talariEventIndex": talariEventIndex,
       "talariEventID": talariEventID,
       "talariEventObjectID": talariEventObjectID,
       "talariEventObjectName": talariEventObjectName,
       "talariEventObjectType": talariEventObjectType,
       "talariEventTime": talariEventTime,
       "talariEventType": talariEventType,
       "talariEventSeverity": talariEventSeverity,
       "talariEventDescription": talariEventDescription,
       "talariNetworkEventScalars": talariNetworkEventScalars,
       "talariNetworkEventAPNID": talariNetworkEventAPNID,
       "talariNetworkEventSiteID": talariNetworkEventSiteID,
       "talariNetworkEventApplianceID": talariNetworkEventApplianceID,
       "talariNetworkEventSiteName": talariNetworkEventSiteName,
       "talariNotifs": talariNotifs,
       "talariEventNotification": talariEventNotification,
       "talariNetworkEventNotification": talariNetworkEventNotification,
       "talariConform": talariConform,
       "talariAgentOIDs": talariAgentOIDs,
       "talariAPNAppliance": talariAPNAppliance,
       "talariT200": talariT200,
       "talariT700": talariT700,
       "talariT730": talariT730,
       "talariT750": talariT750,
       "talariT3000": talariT3000,
       "talariVT100": talariVT100,
       "talariT510": talariT510,
       "talariT5000": talariT5000,
       "talariT3010": talariT3010,
       "talariT860": talariT860,
       "talariCT800": talariCT800,
       "talariVT500": talariVT500,
       "talariT5200": talariT5200,
       "talariVT800": talariVT800,
       "talariE100": talariE100,
       "talariVCN800": talariVCN800,
       "talariE1000": talariE1000,
       "talariE50": talariE50,
       "talariE500": talariE500,
       "talariVT800128": talariVT800128,
       "talariCT800128": talariCT800128}
)
