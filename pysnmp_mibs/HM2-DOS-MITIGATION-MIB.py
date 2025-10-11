# SNMP MIB module (HM2-DOS-MITIGATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hirschmann/HM2-DOS-MITIGATION-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:53:21 2025
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

(HmEnabledStatus,
 hm2ConfigurationMibs) = mibBuilder.importSymbols(
    "HM2-TC-MIB",
    "HmEnabledStatus",
    "hm2ConfigurationMibs")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hm2DosMitigationMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 82)
)
if mibBuilder.loadTexts:
    hm2DosMitigationMib.setRevisions(
        ("2012-09-18 00:00",
         "2012-08-20 00:00",
         "2012-06-06 00:00",
         "2012-03-19 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DosFeatureValue(TextualConvention, Integer32):
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
        *(("hw", 1),
          ("sw", 2),
          ("noSup", 3))
    )



# MIB Managed Objects in the order of their OIDs

_Hm2DosMitigationNotifications_ObjectIdentity = ObjectIdentity
hm2DosMitigationNotifications = _Hm2DosMitigationNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 0)
)
_Hm2DosMitigationObjects_ObjectIdentity = ObjectIdentity
hm2DosMitigationObjects = _Hm2DosMitigationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 1)
)
_Hm2DosMitigationGeneralSettings_ObjectIdentity = ObjectIdentity
hm2DosMitigationGeneralSettings = _Hm2DosMitigationGeneralSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 1, 1)
)
_Hm2DosMitigationCapabilities_ObjectIdentity = ObjectIdentity
hm2DosMitigationCapabilities = _Hm2DosMitigationCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 1, 1, 0)
)
_Hm2DosMitigationTcpHdrChecksSup_Type = DosFeatureValue
_Hm2DosMitigationTcpHdrChecksSup_Object = MibScalar
hm2DosMitigationTcpHdrChecksSup = _Hm2DosMitigationTcpHdrChecksSup_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 1, 1, 0, 1),
    _Hm2DosMitigationTcpHdrChecksSup_Type()
)
hm2DosMitigationTcpHdrChecksSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DosMitigationTcpHdrChecksSup.setStatus("current")
_Hm2DosMitigationIcmpChecksSup_Type = DosFeatureValue
_Hm2DosMitigationIcmpChecksSup_Object = MibScalar
hm2DosMitigationIcmpChecksSup = _Hm2DosMitigationIcmpChecksSup_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 1, 1, 0, 2),
    _Hm2DosMitigationIcmpChecksSup_Type()
)
hm2DosMitigationIcmpChecksSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DosMitigationIcmpChecksSup.setStatus("current")
_Hm2DosMitigationTcpSynLimitSup_Type = DosFeatureValue
_Hm2DosMitigationTcpSynLimitSup_Object = MibScalar
hm2DosMitigationTcpSynLimitSup = _Hm2DosMitigationTcpSynLimitSup_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 1, 1, 0, 3),
    _Hm2DosMitigationTcpSynLimitSup_Type()
)
hm2DosMitigationTcpSynLimitSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DosMitigationTcpSynLimitSup.setStatus("current")
_Hm2DosMitigationArpLimitSup_Type = DosFeatureValue
_Hm2DosMitigationArpLimitSup_Object = MibScalar
hm2DosMitigationArpLimitSup = _Hm2DosMitigationArpLimitSup_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 1, 1, 0, 4),
    _Hm2DosMitigationArpLimitSup_Type()
)
hm2DosMitigationArpLimitSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DosMitigationArpLimitSup.setStatus("current")
_Hm2DosMitigationTcpNullScanSup_Type = DosFeatureValue
_Hm2DosMitigationTcpNullScanSup_Object = MibScalar
hm2DosMitigationTcpNullScanSup = _Hm2DosMitigationTcpNullScanSup_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 1, 1, 0, 5),
    _Hm2DosMitigationTcpNullScanSup_Type()
)
hm2DosMitigationTcpNullScanSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DosMitigationTcpNullScanSup.setStatus("current")
_Hm2DosMitigationTcpXmasSup_Type = DosFeatureValue
_Hm2DosMitigationTcpXmasSup_Object = MibScalar
hm2DosMitigationTcpXmasSup = _Hm2DosMitigationTcpXmasSup_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 1, 1, 0, 6),
    _Hm2DosMitigationTcpXmasSup_Type()
)
hm2DosMitigationTcpXmasSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DosMitigationTcpXmasSup.setStatus("current")
_Hm2DosMitigationTcpLandSup_Type = DosFeatureValue
_Hm2DosMitigationTcpLandSup_Object = MibScalar
hm2DosMitigationTcpLandSup = _Hm2DosMitigationTcpLandSup_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 1, 1, 0, 7),
    _Hm2DosMitigationTcpLandSup_Type()
)
hm2DosMitigationTcpLandSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DosMitigationTcpLandSup.setStatus("current")
_Hm2DosMitigationTcpHdrChecks_ObjectIdentity = ObjectIdentity
hm2DosMitigationTcpHdrChecks = _Hm2DosMitigationTcpHdrChecks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 1, 1, 1)
)


class _Hm2DosMitigationTcpNullScan_Type(HmEnabledStatus):
    """Custom type hm2DosMitigationTcpNullScan based on HmEnabledStatus"""
    defaultValue = 2


_Hm2DosMitigationTcpNullScan_Type.__name__ = "HmEnabledStatus"
_Hm2DosMitigationTcpNullScan_Object = MibScalar
hm2DosMitigationTcpNullScan = _Hm2DosMitigationTcpNullScan_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 1, 1, 1, 1),
    _Hm2DosMitigationTcpNullScan_Type()
)
hm2DosMitigationTcpNullScan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DosMitigationTcpNullScan.setStatus("current")


class _Hm2DosMitigationTcpXmasScan_Type(HmEnabledStatus):
    """Custom type hm2DosMitigationTcpXmasScan based on HmEnabledStatus"""
    defaultValue = 2


_Hm2DosMitigationTcpXmasScan_Type.__name__ = "HmEnabledStatus"
_Hm2DosMitigationTcpXmasScan_Object = MibScalar
hm2DosMitigationTcpXmasScan = _Hm2DosMitigationTcpXmasScan_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 1, 1, 1, 4),
    _Hm2DosMitigationTcpXmasScan_Type()
)
hm2DosMitigationTcpXmasScan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DosMitigationTcpXmasScan.setStatus("current")


class _Hm2DosMitigationTcpSynFinScan_Type(HmEnabledStatus):
    """Custom type hm2DosMitigationTcpSynFinScan based on HmEnabledStatus"""
    defaultValue = 2


_Hm2DosMitigationTcpSynFinScan_Type.__name__ = "HmEnabledStatus"
_Hm2DosMitigationTcpSynFinScan_Object = MibScalar
hm2DosMitigationTcpSynFinScan = _Hm2DosMitigationTcpSynFinScan_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 1, 1, 1, 7),
    _Hm2DosMitigationTcpSynFinScan_Type()
)
hm2DosMitigationTcpSynFinScan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DosMitigationTcpSynFinScan.setStatus("current")


class _Hm2DosMitigationTcpMinimalHeader_Type(HmEnabledStatus):
    """Custom type hm2DosMitigationTcpMinimalHeader based on HmEnabledStatus"""
    defaultValue = 2


_Hm2DosMitigationTcpMinimalHeader_Type.__name__ = "HmEnabledStatus"
_Hm2DosMitigationTcpMinimalHeader_Object = MibScalar
hm2DosMitigationTcpMinimalHeader = _Hm2DosMitigationTcpMinimalHeader_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 1, 1, 1, 10),
    _Hm2DosMitigationTcpMinimalHeader_Type()
)
hm2DosMitigationTcpMinimalHeader.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DosMitigationTcpMinimalHeader.setStatus("current")


class _Hm2DosMitigationTcpMinimalHeaderSize_Type(Unsigned32):
    """Custom type hm2DosMitigationTcpMinimalHeaderSize based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 255),
    )


_Hm2DosMitigationTcpMinimalHeaderSize_Type.__name__ = "Unsigned32"
_Hm2DosMitigationTcpMinimalHeaderSize_Object = MibScalar
hm2DosMitigationTcpMinimalHeaderSize = _Hm2DosMitigationTcpMinimalHeaderSize_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 1, 1, 1, 11),
    _Hm2DosMitigationTcpMinimalHeaderSize_Type()
)
hm2DosMitigationTcpMinimalHeaderSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DosMitigationTcpMinimalHeaderSize.setStatus("current")


class _Hm2DosMitigationLandAttack_Type(HmEnabledStatus):
    """Custom type hm2DosMitigationLandAttack based on HmEnabledStatus"""
    defaultValue = 2


_Hm2DosMitigationLandAttack_Type.__name__ = "HmEnabledStatus"
_Hm2DosMitigationLandAttack_Object = MibScalar
hm2DosMitigationLandAttack = _Hm2DosMitigationLandAttack_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 1, 1, 1, 13),
    _Hm2DosMitigationLandAttack_Type()
)
hm2DosMitigationLandAttack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DosMitigationLandAttack.setStatus("current")


class _Hm2DosMitigationTcpOffsetEqu1_Type(HmEnabledStatus):
    """Custom type hm2DosMitigationTcpOffsetEqu1 based on HmEnabledStatus"""
    defaultValue = 2


_Hm2DosMitigationTcpOffsetEqu1_Type.__name__ = "HmEnabledStatus"
_Hm2DosMitigationTcpOffsetEqu1_Object = MibScalar
hm2DosMitigationTcpOffsetEqu1 = _Hm2DosMitigationTcpOffsetEqu1_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 1, 1, 1, 14),
    _Hm2DosMitigationTcpOffsetEqu1_Type()
)
hm2DosMitigationTcpOffsetEqu1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DosMitigationTcpOffsetEqu1.setStatus("current")


class _Hm2DosMitigationTcpPrivilegedSrcPort_Type(HmEnabledStatus):
    """Custom type hm2DosMitigationTcpPrivilegedSrcPort based on HmEnabledStatus"""
    defaultValue = 2


_Hm2DosMitigationTcpPrivilegedSrcPort_Type.__name__ = "HmEnabledStatus"
_Hm2DosMitigationTcpPrivilegedSrcPort_Object = MibScalar
hm2DosMitigationTcpPrivilegedSrcPort = _Hm2DosMitigationTcpPrivilegedSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 1, 1, 1, 15),
    _Hm2DosMitigationTcpPrivilegedSrcPort_Type()
)
hm2DosMitigationTcpPrivilegedSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DosMitigationTcpPrivilegedSrcPort.setStatus("current")


class _Hm2DosMitigationTcpSrcDstPortEqu_Type(HmEnabledStatus):
    """Custom type hm2DosMitigationTcpSrcDstPortEqu based on HmEnabledStatus"""
    defaultValue = 2


_Hm2DosMitigationTcpSrcDstPortEqu_Type.__name__ = "HmEnabledStatus"
_Hm2DosMitigationTcpSrcDstPortEqu_Object = MibScalar
hm2DosMitigationTcpSrcDstPortEqu = _Hm2DosMitigationTcpSrcDstPortEqu_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 1, 1, 1, 16),
    _Hm2DosMitigationTcpSrcDstPortEqu_Type()
)
hm2DosMitigationTcpSrcDstPortEqu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DosMitigationTcpSrcDstPortEqu.setStatus("current")
_Hm2DosMitigationIcmpChecks_ObjectIdentity = ObjectIdentity
hm2DosMitigationIcmpChecks = _Hm2DosMitigationIcmpChecks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 1, 1, 2)
)


class _Hm2DosMitigationIcmpFrags_Type(HmEnabledStatus):
    """Custom type hm2DosMitigationIcmpFrags based on HmEnabledStatus"""
    defaultValue = 2


_Hm2DosMitigationIcmpFrags_Type.__name__ = "HmEnabledStatus"
_Hm2DosMitigationIcmpFrags_Object = MibScalar
hm2DosMitigationIcmpFrags = _Hm2DosMitigationIcmpFrags_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 1, 1, 2, 1),
    _Hm2DosMitigationIcmpFrags_Type()
)
hm2DosMitigationIcmpFrags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DosMitigationIcmpFrags.setStatus("current")


class _Hm2DosMitigationIcmpPacketSize_Type(Unsigned32):
    """Custom type hm2DosMitigationIcmpPacketSize based on Unsigned32"""
    defaultValue = 512

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1472),
    )


_Hm2DosMitigationIcmpPacketSize_Type.__name__ = "Unsigned32"
_Hm2DosMitigationIcmpPacketSize_Object = MibScalar
hm2DosMitigationIcmpPacketSize = _Hm2DosMitigationIcmpPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 1, 1, 2, 4),
    _Hm2DosMitigationIcmpPacketSize_Type()
)
hm2DosMitigationIcmpPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DosMitigationIcmpPacketSize.setStatus("current")


class _Hm2DosMitigationIcmpPacketSizeMode_Type(HmEnabledStatus):
    """Custom type hm2DosMitigationIcmpPacketSizeMode based on HmEnabledStatus"""
    defaultValue = 2


_Hm2DosMitigationIcmpPacketSizeMode_Type.__name__ = "HmEnabledStatus"
_Hm2DosMitigationIcmpPacketSizeMode_Object = MibScalar
hm2DosMitigationIcmpPacketSizeMode = _Hm2DosMitigationIcmpPacketSizeMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 1, 1, 2, 5),
    _Hm2DosMitigationIcmpPacketSizeMode_Type()
)
hm2DosMitigationIcmpPacketSizeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DosMitigationIcmpPacketSizeMode.setStatus("current")


class _Hm2DosMitigationIcmpSmurfAttack_Type(HmEnabledStatus):
    """Custom type hm2DosMitigationIcmpSmurfAttack based on HmEnabledStatus"""
    defaultValue = 2


_Hm2DosMitigationIcmpSmurfAttack_Type.__name__ = "HmEnabledStatus"
_Hm2DosMitigationIcmpSmurfAttack_Object = MibScalar
hm2DosMitigationIcmpSmurfAttack = _Hm2DosMitigationIcmpSmurfAttack_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 1, 1, 2, 6),
    _Hm2DosMitigationIcmpSmurfAttack_Type()
)
hm2DosMitigationIcmpSmurfAttack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DosMitigationIcmpSmurfAttack.setStatus("current")
_Hm2DosMitigationL2Checks_ObjectIdentity = ObjectIdentity
hm2DosMitigationL2Checks = _Hm2DosMitigationL2Checks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 1, 1, 3)
)


class _Hm2DosMitigationSMacDMac_Type(HmEnabledStatus):
    """Custom type hm2DosMitigationSMacDMac based on HmEnabledStatus"""
    defaultValue = 1


_Hm2DosMitigationSMacDMac_Type.__name__ = "HmEnabledStatus"
_Hm2DosMitigationSMacDMac_Object = MibScalar
hm2DosMitigationSMacDMac = _Hm2DosMitigationSMacDMac_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 1, 1, 3, 7),
    _Hm2DosMitigationSMacDMac_Type()
)
hm2DosMitigationSMacDMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DosMitigationSMacDMac.setStatus("current")
_Hm2DosMitigationIpHdrChecks_ObjectIdentity = ObjectIdentity
hm2DosMitigationIpHdrChecks = _Hm2DosMitigationIpHdrChecks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 1, 1, 4)
)


class _Hm2DosMitigationDropIpSrcRoute_Type(HmEnabledStatus):
    """Custom type hm2DosMitigationDropIpSrcRoute based on HmEnabledStatus"""
    defaultValue = 1


_Hm2DosMitigationDropIpSrcRoute_Type.__name__ = "HmEnabledStatus"
_Hm2DosMitigationDropIpSrcRoute_Object = MibScalar
hm2DosMitigationDropIpSrcRoute = _Hm2DosMitigationDropIpSrcRoute_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 1, 1, 4, 1),
    _Hm2DosMitigationDropIpSrcRoute_Type()
)
hm2DosMitigationDropIpSrcRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DosMitigationDropIpSrcRoute.setStatus("current")
_Hm2DosMitigationLimiter_ObjectIdentity = ObjectIdentity
hm2DosMitigationLimiter = _Hm2DosMitigationLimiter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 1, 2)
)
_Hm2DosMitigationLimiterObjects_ObjectIdentity = ObjectIdentity
hm2DosMitigationLimiterObjects = _Hm2DosMitigationLimiterObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 1, 2, 1)
)
_Hm2DosMitigationLimiterRules_ObjectIdentity = ObjectIdentity
hm2DosMitigationLimiterRules = _Hm2DosMitigationLimiterRules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 1, 2, 2)
)
_Hm2DosMitigationLimiterRuleTable_Object = MibTable
hm2DosMitigationLimiterRuleTable = _Hm2DosMitigationLimiterRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hm2DosMitigationLimiterRuleTable.setStatus("current")
_Hm2DosMitigationLimiterRuleEntry_Object = MibTableRow
hm2DosMitigationLimiterRuleEntry = _Hm2DosMitigationLimiterRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 1, 2, 2, 1, 1)
)
hm2DosMitigationLimiterRuleEntry.setIndexNames(
    (0, "HM2-DOS-MITIGATION-MIB", "hm2DosMitigationLimiterInterface"),
)
if mibBuilder.loadTexts:
    hm2DosMitigationLimiterRuleEntry.setStatus("current")
_Hm2DosMitigationLimiterInterface_Type = InterfaceIndex
_Hm2DosMitigationLimiterInterface_Object = MibTableColumn
hm2DosMitigationLimiterInterface = _Hm2DosMitigationLimiterInterface_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 1, 2, 2, 1, 1, 1),
    _Hm2DosMitigationLimiterInterface_Type()
)
hm2DosMitigationLimiterInterface.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hm2DosMitigationLimiterInterface.setStatus("current")
_Hm2DosMitigationLimiterTcpSynLimit_Type = Unsigned32
_Hm2DosMitigationLimiterTcpSynLimit_Object = MibTableColumn
hm2DosMitigationLimiterTcpSynLimit = _Hm2DosMitigationLimiterTcpSynLimit_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 1, 2, 2, 1, 1, 2),
    _Hm2DosMitigationLimiterTcpSynLimit_Type()
)
hm2DosMitigationLimiterTcpSynLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DosMitigationLimiterTcpSynLimit.setStatus("current")
_Hm2DosMitigationLimiterArpLimit_Type = Unsigned32
_Hm2DosMitigationLimiterArpLimit_Object = MibTableColumn
hm2DosMitigationLimiterArpLimit = _Hm2DosMitigationLimiterArpLimit_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 1, 2, 2, 1, 1, 3),
    _Hm2DosMitigationLimiterArpLimit_Type()
)
hm2DosMitigationLimiterArpLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DosMitigationLimiterArpLimit.setStatus("current")
_Hm2DosMitigationLimiterRowStatus_Type = RowStatus
_Hm2DosMitigationLimiterRowStatus_Object = MibTableColumn
hm2DosMitigationLimiterRowStatus = _Hm2DosMitigationLimiterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 1, 2, 2, 1, 1, 4),
    _Hm2DosMitigationLimiterRowStatus_Type()
)
hm2DosMitigationLimiterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DosMitigationLimiterRowStatus.setStatus("current")
_Hm2DosMitigationStatistics_ObjectIdentity = ObjectIdentity
hm2DosMitigationStatistics = _Hm2DosMitigationStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 1, 3)
)
_Hm2DosMitigationGlobalDropCounter_Type = Counter64
_Hm2DosMitigationGlobalDropCounter_Object = MibScalar
hm2DosMitigationGlobalDropCounter = _Hm2DosMitigationGlobalDropCounter_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 1, 3, 1),
    _Hm2DosMitigationGlobalDropCounter_Type()
)
hm2DosMitigationGlobalDropCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DosMitigationGlobalDropCounter.setStatus("current")
_Hm2DosMitigationStatisticsPortTable_Object = MibTable
hm2DosMitigationStatisticsPortTable = _Hm2DosMitigationStatisticsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hm2DosMitigationStatisticsPortTable.setStatus("current")
_Hm2DosMitigationStatisticsPortEntry_Object = MibTableRow
hm2DosMitigationStatisticsPortEntry = _Hm2DosMitigationStatisticsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 1, 3, 2, 1)
)
hm2DosMitigationStatisticsPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hm2DosMitigationStatisticsPortEntry.setStatus("current")
_Hm2DosMitigationPortDropCounter_Type = Counter64
_Hm2DosMitigationPortDropCounter_Object = MibTableColumn
hm2DosMitigationPortDropCounter = _Hm2DosMitigationPortDropCounter_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 1, 3, 2, 1, 1),
    _Hm2DosMitigationPortDropCounter_Type()
)
hm2DosMitigationPortDropCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DosMitigationPortDropCounter.setStatus("current")
_Hm2DosMitigationConformance_ObjectIdentity = ObjectIdentity
hm2DosMitigationConformance = _Hm2DosMitigationConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 2)
)
_Hm2DosMitigationCompliances_ObjectIdentity = ObjectIdentity
hm2DosMitigationCompliances = _Hm2DosMitigationCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 2, 1)
)
_Hm2DosMitigationGroups_ObjectIdentity = ObjectIdentity
hm2DosMitigationGroups = _Hm2DosMitigationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 2, 2)
)

# Managed Objects groups

hm2DosMitigationGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 2, 2, 1)
)
hm2DosMitigationGeneralGroup.setObjects(
      *(("HM2-DOS-MITIGATION-MIB", "hm2DosMitigationTcpSynFinScan"),
        ("HM2-DOS-MITIGATION-MIB", "hm2DosMitigationTcpNullScan"),
        ("HM2-DOS-MITIGATION-MIB", "hm2DosMitigationTcpXmasScan"),
        ("HM2-DOS-MITIGATION-MIB", "hm2DosMitigationTcpMinimalHeader"),
        ("HM2-DOS-MITIGATION-MIB", "hm2DosMitigationTcpMinimalHeaderSize"),
        ("HM2-DOS-MITIGATION-MIB", "hm2DosMitigationLandAttack"),
        ("HM2-DOS-MITIGATION-MIB", "hm2DosMitigationTcpOffsetEqu1"),
        ("HM2-DOS-MITIGATION-MIB", "hm2DosMitigationTcpPrivilegedSrcPort"),
        ("HM2-DOS-MITIGATION-MIB", "hm2DosMitigationTcpSrcDstPortEqu"),
        ("HM2-DOS-MITIGATION-MIB", "hm2DosMitigationIcmpFrags"),
        ("HM2-DOS-MITIGATION-MIB", "hm2DosMitigationIcmpPacketSize"),
        ("HM2-DOS-MITIGATION-MIB", "hm2DosMitigationIcmpPacketSizeMode"),
        ("HM2-DOS-MITIGATION-MIB", "hm2DosMitigationSMacDMac"),
        ("HM2-DOS-MITIGATION-MIB", "hm2DosMitigationDropIpSrcRoute"),
        ("HM2-DOS-MITIGATION-MIB", "hm2DosMitigationTcpHdrChecksSup"),
        ("HM2-DOS-MITIGATION-MIB", "hm2DosMitigationIcmpChecksSup"),
        ("HM2-DOS-MITIGATION-MIB", "hm2DosMitigationTcpSynLimitSup"),
        ("HM2-DOS-MITIGATION-MIB", "hm2DosMitigationArpLimitSup"),
        ("HM2-DOS-MITIGATION-MIB", "hm2DosMitigationLimiterInterface"),
        ("HM2-DOS-MITIGATION-MIB", "hm2DosMitigationLimiterTcpSynLimit"),
        ("HM2-DOS-MITIGATION-MIB", "hm2DosMitigationLimiterArpLimit"),
        ("HM2-DOS-MITIGATION-MIB", "hm2DosMitigationLimiterRowStatus"),
        ("HM2-DOS-MITIGATION-MIB", "hm2DosMitigationTcpXmasSup"),
        ("HM2-DOS-MITIGATION-MIB", "hm2DosMitigationTcpNullScanSup"),
        ("HM2-DOS-MITIGATION-MIB", "hm2DosMitigationTcpLandSup"))
)
if mibBuilder.loadTexts:
    hm2DosMitigationGeneralGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hm2DosMitigationCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 248, 11, 82, 2, 1, 1)
)
hm2DosMitigationCompliance.setObjects(
    ("HM2-DOS-MITIGATION-MIB", "hm2DosMitigationGeneralGroup")
)
if mibBuilder.loadTexts:
    hm2DosMitigationCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-DOS-MITIGATION-MIB",
    **{"DosFeatureValue": DosFeatureValue,
       "hm2DosMitigationMib": hm2DosMitigationMib,
       "hm2DosMitigationNotifications": hm2DosMitigationNotifications,
       "hm2DosMitigationObjects": hm2DosMitigationObjects,
       "hm2DosMitigationGeneralSettings": hm2DosMitigationGeneralSettings,
       "hm2DosMitigationCapabilities": hm2DosMitigationCapabilities,
       "hm2DosMitigationTcpHdrChecksSup": hm2DosMitigationTcpHdrChecksSup,
       "hm2DosMitigationIcmpChecksSup": hm2DosMitigationIcmpChecksSup,
       "hm2DosMitigationTcpSynLimitSup": hm2DosMitigationTcpSynLimitSup,
       "hm2DosMitigationArpLimitSup": hm2DosMitigationArpLimitSup,
       "hm2DosMitigationTcpNullScanSup": hm2DosMitigationTcpNullScanSup,
       "hm2DosMitigationTcpXmasSup": hm2DosMitigationTcpXmasSup,
       "hm2DosMitigationTcpLandSup": hm2DosMitigationTcpLandSup,
       "hm2DosMitigationTcpHdrChecks": hm2DosMitigationTcpHdrChecks,
       "hm2DosMitigationTcpNullScan": hm2DosMitigationTcpNullScan,
       "hm2DosMitigationTcpXmasScan": hm2DosMitigationTcpXmasScan,
       "hm2DosMitigationTcpSynFinScan": hm2DosMitigationTcpSynFinScan,
       "hm2DosMitigationTcpMinimalHeader": hm2DosMitigationTcpMinimalHeader,
       "hm2DosMitigationTcpMinimalHeaderSize": hm2DosMitigationTcpMinimalHeaderSize,
       "hm2DosMitigationLandAttack": hm2DosMitigationLandAttack,
       "hm2DosMitigationTcpOffsetEqu1": hm2DosMitigationTcpOffsetEqu1,
       "hm2DosMitigationTcpPrivilegedSrcPort": hm2DosMitigationTcpPrivilegedSrcPort,
       "hm2DosMitigationTcpSrcDstPortEqu": hm2DosMitigationTcpSrcDstPortEqu,
       "hm2DosMitigationIcmpChecks": hm2DosMitigationIcmpChecks,
       "hm2DosMitigationIcmpFrags": hm2DosMitigationIcmpFrags,
       "hm2DosMitigationIcmpPacketSize": hm2DosMitigationIcmpPacketSize,
       "hm2DosMitigationIcmpPacketSizeMode": hm2DosMitigationIcmpPacketSizeMode,
       "hm2DosMitigationIcmpSmurfAttack": hm2DosMitigationIcmpSmurfAttack,
       "hm2DosMitigationL2Checks": hm2DosMitigationL2Checks,
       "hm2DosMitigationSMacDMac": hm2DosMitigationSMacDMac,
       "hm2DosMitigationIpHdrChecks": hm2DosMitigationIpHdrChecks,
       "hm2DosMitigationDropIpSrcRoute": hm2DosMitigationDropIpSrcRoute,
       "hm2DosMitigationLimiter": hm2DosMitigationLimiter,
       "hm2DosMitigationLimiterObjects": hm2DosMitigationLimiterObjects,
       "hm2DosMitigationLimiterRules": hm2DosMitigationLimiterRules,
       "hm2DosMitigationLimiterRuleTable": hm2DosMitigationLimiterRuleTable,
       "hm2DosMitigationLimiterRuleEntry": hm2DosMitigationLimiterRuleEntry,
       "hm2DosMitigationLimiterInterface": hm2DosMitigationLimiterInterface,
       "hm2DosMitigationLimiterTcpSynLimit": hm2DosMitigationLimiterTcpSynLimit,
       "hm2DosMitigationLimiterArpLimit": hm2DosMitigationLimiterArpLimit,
       "hm2DosMitigationLimiterRowStatus": hm2DosMitigationLimiterRowStatus,
       "hm2DosMitigationStatistics": hm2DosMitigationStatistics,
       "hm2DosMitigationGlobalDropCounter": hm2DosMitigationGlobalDropCounter,
       "hm2DosMitigationStatisticsPortTable": hm2DosMitigationStatisticsPortTable,
       "hm2DosMitigationStatisticsPortEntry": hm2DosMitigationStatisticsPortEntry,
       "hm2DosMitigationPortDropCounter": hm2DosMitigationPortDropCounter,
       "hm2DosMitigationConformance": hm2DosMitigationConformance,
       "hm2DosMitigationCompliances": hm2DosMitigationCompliances,
       "hm2DosMitigationCompliance": hm2DosMitigationCompliance,
       "hm2DosMitigationGroups": hm2DosMitigationGroups,
       "hm2DosMitigationGeneralGroup": hm2DosMitigationGeneralGroup}
)
