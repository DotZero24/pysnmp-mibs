# SNMP MIB module (AVAYA-WLAN-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nortel/AVAYA-WLAN-TC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:20:10 2025
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(avayaWlanMibs,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "avayaWlanMibs")


# MODULE-IDENTITY

avayaWlanTcMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 7, 1)
)
if mibBuilder.loadTexts:
    avayaWlanTcMib.setRevisions(
        ("2011-12-15 00:00",
         "2011-11-21 00:00",
         "2011-10-11 00:00",
         "2011-07-23 00:00",
         "2011-01-07 00:00",
         "2010-06-25 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AvWlanDomainRole(TextualConvention, Integer32):
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
        *(("activeMdc", 1),
          ("backupMdc", 2),
          ("peerWc", 3),
          ("standalone", 4))
    )



class AvWlanControllerModel(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("wc8180", 1)
    )



class AvWlanSwitchModel(TextualConvention, Integer32):
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
        *(("wc8180", 1),
          ("wsp8180", 2),
          ("ers8800", 3))
    )



class AvWlanNumberAPsPerWC(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )



class AvWlanAPModel(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ap8120", 2),
          ("ap8120-E", 3),
          ("ap8120-O", 4))
    )



class AvWlanAPModelOrNone(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ap8120", 2),
          ("ap8120-E", 3),
          ("ap8120-O", 4),
          ("none", 255))
    )



class AvWlanAPStatus(TextualConvention, Integer32):
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
        *(("managed", 1),
          ("unknown", 2),
          ("standalone", 3),
          ("rogue", 4),
          ("knownForeign", 5))
    )



class AvWlanRadioChannel(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
        ValueRangeConstraint(34, 34),
        ValueRangeConstraint(36, 36),
        ValueRangeConstraint(38, 38),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(42, 42),
        ValueRangeConstraint(44, 44),
        ValueRangeConstraint(46, 46),
        ValueRangeConstraint(48, 48),
        ValueRangeConstraint(52, 52),
        ValueRangeConstraint(56, 56),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(104, 104),
        ValueRangeConstraint(108, 108),
        ValueRangeConstraint(112, 112),
        ValueRangeConstraint(116, 116),
        ValueRangeConstraint(120, 120),
        ValueRangeConstraint(124, 124),
        ValueRangeConstraint(128, 128),
        ValueRangeConstraint(132, 132),
        ValueRangeConstraint(136, 136),
        ValueRangeConstraint(140, 140),
        ValueRangeConstraint(149, 149),
        ValueRangeConstraint(153, 153),
        ValueRangeConstraint(157, 157),
        ValueRangeConstraint(161, 161),
        ValueRangeConstraint(165, 165),
        ValueRangeConstraint(184, 184),
        ValueRangeConstraint(188, 188),
        ValueRangeConstraint(192, 192),
        ValueRangeConstraint(196, 196),
        ValueRangeConstraint(200, 200),
        ValueRangeConstraint(204, 204),
        ValueRangeConstraint(208, 208),
        ValueRangeConstraint(212, 212),
        ValueRangeConstraint(216, 216),
    )



class AvWlanRadioChannelOrZero(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
        ValueRangeConstraint(34, 34),
        ValueRangeConstraint(36, 36),
        ValueRangeConstraint(38, 38),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(42, 42),
        ValueRangeConstraint(44, 44),
        ValueRangeConstraint(46, 46),
        ValueRangeConstraint(48, 48),
        ValueRangeConstraint(52, 52),
        ValueRangeConstraint(56, 56),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(104, 104),
        ValueRangeConstraint(108, 108),
        ValueRangeConstraint(112, 112),
        ValueRangeConstraint(116, 116),
        ValueRangeConstraint(120, 120),
        ValueRangeConstraint(124, 124),
        ValueRangeConstraint(128, 128),
        ValueRangeConstraint(132, 132),
        ValueRangeConstraint(136, 136),
        ValueRangeConstraint(140, 140),
        ValueRangeConstraint(149, 149),
        ValueRangeConstraint(153, 153),
        ValueRangeConstraint(157, 157),
        ValueRangeConstraint(161, 161),
        ValueRangeConstraint(165, 165),
        ValueRangeConstraint(184, 184),
        ValueRangeConstraint(188, 188),
        ValueRangeConstraint(192, 192),
        ValueRangeConstraint(196, 196),
        ValueRangeConstraint(200, 200),
        ValueRangeConstraint(204, 204),
        ValueRangeConstraint(208, 208),
        ValueRangeConstraint(212, 212),
        ValueRangeConstraint(216, 216),
    )



class AvWlanRadioPower(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class AvWlanRadioAntenna(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("wl81AT070E6", 2),
          ("wl81AT180E6", 4))
    )



class AvWlanRadioAntennaOrNone(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("wl81AT070E6", 2),
          ("wl81AT180E6", 4),
          ("none", 255))
    )



class AvWlanRadioExtCable(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ft3", 1),
          ("ft10", 2))
    )



class AvWlanRadioExtCableOrNone(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ft3", 1),
          ("ft10", 2),
          ("none", 255))
    )



class AvWlanRadioOperationMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accessWids", 1),
          ("widsWips", 2))
    )



class AvWlanRadioInterface(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )



class AvWlanRadioInterfaceOrZero(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )



class AvWlanDataRateSet(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class AvWlanChannelSet(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class AvWlanRPTimeOfDay(TextualConvention, OctetString):
    status = "current"
    displayHint = "255t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class AvWlanOui(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3



class AvWlanTspecSuppAccessCategory(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("voice", 1),
          ("video", 2))
    )



class AvWlanConfigSyncComponents(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("apDatabase", 0),
          ("apProfile", 1),
          ("radioProfile", 2),
          ("networkProfile", 3),
          ("autoRF", 4),
          ("domainConfig", 5),
          ("captivePortal", 6),
          ("qosAcl", 7),
          ("qosDiffserv", 8),
          ("radiusGlobal", 9),
          ("radiusAuth", 10),
          ("radiusAcct", 11),
          ("mobilityVlan", 12),
          ("e911Config", 13),
          ("widsWips", 14),
          ("widsKnownAp", 15),
          ("securityUserDb", 16),
          ("securityMacDb", 17),
          ("radiusProfile", 18),
          ("radiusProfileServer", 19),
          ("crypto", 20),
          ("captureProfile", 21))
    )


class AvWlanAPLicenseCapacity(TextualConvention, Integer32):
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
        *(("none", 1),
          ("sixteenLocked", 2),
          ("unlimited", 3))
    )



class AvWlanLogMsgLevel(TextualConvention, Integer32):
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
        *(("critical", 1),
          ("serious", 2),
          ("informational", 3),
          ("none", 4))
    )



class AvWlanCountryCode(SnmpAdminString):
    status = "current"
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(2, 2),
    )



class AvWlanImageFileOrNone(TextualConvention, Integer32):
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("account", 2),
          ("brand", 3),
          ("background", 4),
          ("logout", 5),
          ("pkgfile", 6),
          ("none", 255))
    )



class AvWlanFileUpdateStatus(TextualConvention, Integer32):
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("success", 2),
          ("transferFailed", 3),
          ("inProgress", 4),
          ("fileProcFailed", 5),
          ("fileNotFound", 6),
          ("internalError", 7),
          ("noSuchProfile", 8),
          ("noSuchLocale", 9),
          ("noSuchController", 10),
          ("maxFileSizeExceed", 11),
          ("maxProfileSizeExceed", 12))
    )



class AvWlanPacketCaptureFilterMask(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("beacons", 0),
          ("probes", 1),
          ("data", 2),
          ("mgmt", 3),
          ("control", 4))
    )


class AvWlanLoadBalanceMetric(TextualConvention, Integer32):
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
        *(("preferred", 1),
          ("alternate", 2),
          ("leastLoad", 3),
          ("cbfs", 4))
    )



class AvWlanMobVlanRole(TextualConvention, Integer32):
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
        *(("server", 1),
          ("staticClient", 2),
          ("dynamicClient", 3),
          ("none", 4))
    )



class AvWlanMobVlanState(TextualConvention, Integer32):
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



class AvWlanSwitchNotifAuxLimitsMap(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("vlanMapTableFull", 0),
          ("tunnelTableFull", 1),
          ("multicastTableFull", 2))
    )


# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AVAYA-WLAN-TC-MIB",
    **{"AvWlanDomainRole": AvWlanDomainRole,
       "AvWlanControllerModel": AvWlanControllerModel,
       "AvWlanSwitchModel": AvWlanSwitchModel,
       "AvWlanNumberAPsPerWC": AvWlanNumberAPsPerWC,
       "AvWlanAPModel": AvWlanAPModel,
       "AvWlanAPModelOrNone": AvWlanAPModelOrNone,
       "AvWlanAPStatus": AvWlanAPStatus,
       "AvWlanRadioChannel": AvWlanRadioChannel,
       "AvWlanRadioChannelOrZero": AvWlanRadioChannelOrZero,
       "AvWlanRadioPower": AvWlanRadioPower,
       "AvWlanRadioAntenna": AvWlanRadioAntenna,
       "AvWlanRadioAntennaOrNone": AvWlanRadioAntennaOrNone,
       "AvWlanRadioExtCable": AvWlanRadioExtCable,
       "AvWlanRadioExtCableOrNone": AvWlanRadioExtCableOrNone,
       "AvWlanRadioOperationMode": AvWlanRadioOperationMode,
       "AvWlanRadioInterface": AvWlanRadioInterface,
       "AvWlanRadioInterfaceOrZero": AvWlanRadioInterfaceOrZero,
       "AvWlanDataRateSet": AvWlanDataRateSet,
       "AvWlanChannelSet": AvWlanChannelSet,
       "AvWlanRPTimeOfDay": AvWlanRPTimeOfDay,
       "AvWlanOui": AvWlanOui,
       "AvWlanTspecSuppAccessCategory": AvWlanTspecSuppAccessCategory,
       "AvWlanConfigSyncComponents": AvWlanConfigSyncComponents,
       "AvWlanAPLicenseCapacity": AvWlanAPLicenseCapacity,
       "AvWlanLogMsgLevel": AvWlanLogMsgLevel,
       "AvWlanCountryCode": AvWlanCountryCode,
       "AvWlanImageFileOrNone": AvWlanImageFileOrNone,
       "AvWlanFileUpdateStatus": AvWlanFileUpdateStatus,
       "AvWlanPacketCaptureFilterMask": AvWlanPacketCaptureFilterMask,
       "AvWlanLoadBalanceMetric": AvWlanLoadBalanceMetric,
       "AvWlanMobVlanRole": AvWlanMobVlanRole,
       "AvWlanMobVlanState": AvWlanMobVlanState,
       "AvWlanSwitchNotifAuxLimitsMap": AvWlanSwitchNotifAuxLimitsMap,
       "avayaWlanTcMib": avayaWlanTcMib}
)
