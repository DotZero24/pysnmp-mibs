# SNMP MIB module (HP-PAGEWIDE-PRO-477DW-MFP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/HP-PAGEWIDE-PRO-477DW-MFP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:32:39 2025
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

(InternationalDisplayString,
 KBytes,
 ProductID) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "InternationalDisplayString",
    "KBytes",
    "ProductID")

(IANACharset,) = mibBuilder.importSymbols(
    "IANA-CHARSET-MIB",
    "IANACharset")

(PrtChannelTypeTC,
 PrtCoverStatusTC,
 PrtGeneralResetTC,
 PrtInputTypeTC,
 PrtInterpreterLangFamilyTC,
 PrtMarkerMarkTechTC,
 PrtMarkerSuppliesTypeTC,
 PrtMediaPathTypeTC,
 PrtOutputTypeTC) = mibBuilder.importSymbols(
    "IANA-PRINTER-MIB",
    "PrtChannelTypeTC",
    "PrtCoverStatusTC",
    "PrtGeneralResetTC",
    "PrtInputTypeTC",
    "PrtInterpreterLangFamilyTC",
    "PrtMarkerMarkTechTC",
    "PrtMarkerSuppliesTypeTC",
    "PrtMediaPathTypeTC",
    "PrtOutputTypeTC")

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(WEPKeytype,) = mibBuilder.importSymbols(
    "IEEE802dot11-MIB",
    "WEPKeytype")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress")

(PresentOnOff,
 PrtCapacityUnitTC,
 PrtChannelStateTC,
 PrtConsoleDescriptionStringTC,
 PrtInterpreterTwoWayTC,
 PrtLocalizedDescriptionStringTC,
 PrtMarkerAddressabilityUnitTC,
 PrtMarkerColorantRoleTC,
 PrtMarkerCounterUnitTC,
 PrtMarkerSuppliesClassTC,
 PrtMarkerSuppliesSupplyUnitTC,
 PrtMediaPathMaxSpeedPrintUnitTC,
 PrtMediaUnitTC,
 PrtOutputPageDeliveryOrientationTC,
 PrtOutputStackingOrderTC,
 PrtPrintOrientationTC,
 PrtSubUnitStatusTC) = mibBuilder.importSymbols(
    "Printer-MIB",
    "PresentOnOff",
    "PrtCapacityUnitTC",
    "PrtChannelStateTC",
    "PrtConsoleDescriptionStringTC",
    "PrtInterpreterTwoWayTC",
    "PrtLocalizedDescriptionStringTC",
    "PrtMarkerAddressabilityUnitTC",
    "PrtMarkerColorantRoleTC",
    "PrtMarkerCounterUnitTC",
    "PrtMarkerSuppliesClassTC",
    "PrtMarkerSuppliesSupplyUnitTC",
    "PrtMediaPathMaxSpeedPrintUnitTC",
    "PrtMediaUnitTC",
    "PrtOutputPageDeliveryOrientationTC",
    "PrtOutputStackingOrderTC",
    "PrtPrintOrientationTC",
    "PrtSubUnitStatusTC")

(SnmpAdminString,
 SnmpEngineID) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString",
    "SnmpEngineID")

(KeyChange,) = mibBuilder.importSymbols(
    "SNMP-USER-BASED-SM-MIB",
    "KeyChange")

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

(AutonomousType,
 DateAndTime,
 DisplayString,
 PhysAddress,
 RowPointer,
 RowStatus,
 StorageType,
 TextualConvention,
 TestAndIncr,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ieee802dot11_ObjectIdentity = ObjectIdentity
ieee802dot11 = _Ieee802dot11_ObjectIdentity(
    (1, 2, 840, 10036)
)
_Dot11smt_ObjectIdentity = ObjectIdentity
dot11smt = _Dot11smt_ObjectIdentity(
    (1, 2, 840, 10036, 1)
)
_Dot11StationConfigTable_ObjectIdentity = ObjectIdentity
dot11StationConfigTable = _Dot11StationConfigTable_ObjectIdentity(
    (1, 2, 840, 10036, 1, 1)
)
_Dot11StationConfigEntry_ObjectIdentity = ObjectIdentity
dot11StationConfigEntry = _Dot11StationConfigEntry_ObjectIdentity(
    (1, 2, 840, 10036, 1, 1, 1)
)


class _Dot11DesiredSSID_Type(OctetString):
    """Custom type dot11DesiredSSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Dot11DesiredSSID_Type.__name__ = "OctetString"
_Dot11DesiredSSID_Object = MibScalar
dot11DesiredSSID = _Dot11DesiredSSID_Object(
    (1, 2, 840, 10036, 1, 1, 1, 9),
    _Dot11DesiredSSID_Type()
)
dot11DesiredSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DesiredSSID.setStatus("current")


class _Dot11DesiredBSSType_Type(Integer32):
    """Custom type dot11DesiredBSSType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("infrastructure", 1),
          ("independent", 2),
          ("any", 3))
    )


_Dot11DesiredBSSType_Type.__name__ = "Integer32"
_Dot11DesiredBSSType_Object = MibScalar
dot11DesiredBSSType = _Dot11DesiredBSSType_Object(
    (1, 2, 840, 10036, 1, 1, 1, 10),
    _Dot11DesiredBSSType_Type()
)
dot11DesiredBSSType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DesiredBSSType.setStatus("current")
_Dot11AuthenticationAlgorithmsTable_ObjectIdentity = ObjectIdentity
dot11AuthenticationAlgorithmsTable = _Dot11AuthenticationAlgorithmsTable_ObjectIdentity(
    (1, 2, 840, 10036, 1, 2)
)
_Dot11AuthenticationAlgorithmsEntry_ObjectIdentity = ObjectIdentity
dot11AuthenticationAlgorithmsEntry = _Dot11AuthenticationAlgorithmsEntry_ObjectIdentity(
    (1, 2, 840, 10036, 1, 2, 1)
)


class _Dot11AuthenticationAlgorithm_Type(Integer32):
    """Custom type dot11AuthenticationAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("openSystem", 1),
          ("sharedKey", 2))
    )


_Dot11AuthenticationAlgorithm_Type.__name__ = "Integer32"
_Dot11AuthenticationAlgorithm_Object = MibScalar
dot11AuthenticationAlgorithm = _Dot11AuthenticationAlgorithm_Object(
    (1, 2, 840, 10036, 1, 2, 1, 2),
    _Dot11AuthenticationAlgorithm_Type()
)
dot11AuthenticationAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11AuthenticationAlgorithm.setStatus("current")
_Dot11AuthenticationAlgorithmsEnable_Type = TruthValue
_Dot11AuthenticationAlgorithmsEnable_Object = MibScalar
dot11AuthenticationAlgorithmsEnable = _Dot11AuthenticationAlgorithmsEnable_Object(
    (1, 2, 840, 10036, 1, 2, 1, 3),
    _Dot11AuthenticationAlgorithmsEnable_Type()
)
dot11AuthenticationAlgorithmsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11AuthenticationAlgorithmsEnable.setStatus("current")
_Dot11WEPDefaultKeysTable_ObjectIdentity = ObjectIdentity
dot11WEPDefaultKeysTable = _Dot11WEPDefaultKeysTable_ObjectIdentity(
    (1, 2, 840, 10036, 1, 3)
)
_Dot11WEPDefaultKeysEntry_ObjectIdentity = ObjectIdentity
dot11WEPDefaultKeysEntry = _Dot11WEPDefaultKeysEntry_ObjectIdentity(
    (1, 2, 840, 10036, 1, 3, 1)
)
_Dot11WEPDefaultKeyValue_Type = WEPKeytype
_Dot11WEPDefaultKeyValue_Object = MibScalar
dot11WEPDefaultKeyValue = _Dot11WEPDefaultKeyValue_Object(
    (1, 2, 840, 10036, 1, 3, 1, 2),
    _Dot11WEPDefaultKeyValue_Type()
)
dot11WEPDefaultKeyValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11WEPDefaultKeyValue.setStatus("current")
_Dot11PrivacyTable_ObjectIdentity = ObjectIdentity
dot11PrivacyTable = _Dot11PrivacyTable_ObjectIdentity(
    (1, 2, 840, 10036, 1, 5)
)
_Dot11PrivacyEntry_ObjectIdentity = ObjectIdentity
dot11PrivacyEntry = _Dot11PrivacyEntry_ObjectIdentity(
    (1, 2, 840, 10036, 1, 5, 1)
)
_Dot11PrivacyInvoked_Type = TruthValue
_Dot11PrivacyInvoked_Object = MibScalar
dot11PrivacyInvoked = _Dot11PrivacyInvoked_Object(
    (1, 2, 840, 10036, 1, 5, 1, 1),
    _Dot11PrivacyInvoked_Type()
)
dot11PrivacyInvoked.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11PrivacyInvoked.setStatus("current")


class _Dot11WEPDefaultKeyID_Type(Integer32):
    """Custom type dot11WEPDefaultKeyID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Dot11WEPDefaultKeyID_Type.__name__ = "Integer32"
_Dot11WEPDefaultKeyID_Object = MibScalar
dot11WEPDefaultKeyID = _Dot11WEPDefaultKeyID_Object(
    (1, 2, 840, 10036, 1, 5, 1, 2),
    _Dot11WEPDefaultKeyID_Type()
)
dot11WEPDefaultKeyID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11WEPDefaultKeyID.setStatus("current")
_Dot11phy_ObjectIdentity = ObjectIdentity
dot11phy = _Dot11phy_ObjectIdentity(
    (1, 2, 840, 10036, 4)
)
_Dot11PhyOperationTable_ObjectIdentity = ObjectIdentity
dot11PhyOperationTable = _Dot11PhyOperationTable_ObjectIdentity(
    (1, 2, 840, 10036, 4, 1)
)
_Dot11PhyOperationEntry_ObjectIdentity = ObjectIdentity
dot11PhyOperationEntry = _Dot11PhyOperationEntry_ObjectIdentity(
    (1, 2, 840, 10036, 4, 1, 1)
)


class _Dot11CurrentRegDomain_Type(Integer32):
    """Custom type dot11CurrentRegDomain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              32,
              48,
              49,
              50,
              64,
              65)
        )
    )
    namedValues = NamedValues(
        *(("fcc", 16),
          ("doc", 32),
          ("etsi", 48),
          ("spain", 49),
          ("france", 50),
          ("mkk", 64),
          ("japan", 65))
    )


_Dot11CurrentRegDomain_Type.__name__ = "Integer32"
_Dot11CurrentRegDomain_Object = MibScalar
dot11CurrentRegDomain = _Dot11CurrentRegDomain_Object(
    (1, 2, 840, 10036, 4, 1, 1, 2),
    _Dot11CurrentRegDomain_Type()
)
dot11CurrentRegDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CurrentRegDomain.setStatus("current")
_Ieee802dot11i_ObjectIdentity = ObjectIdentity
ieee802dot11i = _Ieee802dot11i_ObjectIdentity(
    (1, 2, 840, 10036, 7)
)
_Dot11RSNConfigAuthenticationSuitesTable_ObjectIdentity = ObjectIdentity
dot11RSNConfigAuthenticationSuitesTable = _Dot11RSNConfigAuthenticationSuitesTable_ObjectIdentity(
    (1, 2, 840, 10036, 7, 3)
)
_Dot11RSNConfigAuthenticationSuitesEntry_ObjectIdentity = ObjectIdentity
dot11RSNConfigAuthenticationSuitesEntry = _Dot11RSNConfigAuthenticationSuitesEntry_ObjectIdentity(
    (1, 2, 840, 10036, 7, 3, 1)
)


class _Dot11RSNConfigAuthenticationSuite_Type(OctetString):
    """Custom type dot11RSNConfigAuthenticationSuite based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_Dot11RSNConfigAuthenticationSuite_Type.__name__ = "OctetString"
_Dot11RSNConfigAuthenticationSuite_Object = MibScalar
dot11RSNConfigAuthenticationSuite = _Dot11RSNConfigAuthenticationSuite_Object(
    (1, 2, 840, 10036, 7, 3, 1, 2),
    _Dot11RSNConfigAuthenticationSuite_Type()
)
dot11RSNConfigAuthenticationSuite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RSNConfigAuthenticationSuite.setStatus("current")
_Dot11RSNConfigAuthenticationSuiteEnabled_Type = TruthValue
_Dot11RSNConfigAuthenticationSuiteEnabled_Object = MibScalar
dot11RSNConfigAuthenticationSuiteEnabled = _Dot11RSNConfigAuthenticationSuiteEnabled_Object(
    (1, 2, 840, 10036, 7, 3, 1, 3),
    _Dot11RSNConfigAuthenticationSuiteEnabled_Type()
)
dot11RSNConfigAuthenticationSuiteEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RSNConfigAuthenticationSuiteEnabled.setStatus("current")
_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Mgmt_ObjectIdentity = ObjectIdentity
mgmt = _Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 2)
)
_Mib_2_ObjectIdentity = ObjectIdentity
mib_2 = _Mib_2_ObjectIdentity(
    (1, 3, 6, 1, 2, 1)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 1)
)


class _SysDescr_Type(DisplayString):
    """Custom type sysDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysDescr_Type.__name__ = "DisplayString"
_SysDescr_Object = MibScalar
sysDescr = _SysDescr_Object(
    (1, 3, 6, 1, 2, 1, 1, 1),
    _SysDescr_Type()
)
sysDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDescr.setStatus("mandatory")
_SysObjectID_Type = ObjectIdentifier
_SysObjectID_Object = MibScalar
sysObjectID = _SysObjectID_Object(
    (1, 3, 6, 1, 2, 1, 1, 2),
    _SysObjectID_Type()
)
sysObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysObjectID.setStatus("mandatory")
_SysUpTime_Type = TimeTicks
_SysUpTime_Object = MibScalar
sysUpTime = _SysUpTime_Object(
    (1, 3, 6, 1, 2, 1, 1, 3),
    _SysUpTime_Type()
)
sysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysUpTime.setStatus("mandatory")


class _SysContact_Type(DisplayString):
    """Custom type sysContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysContact_Type.__name__ = "DisplayString"
_SysContact_Object = MibScalar
sysContact = _SysContact_Object(
    (1, 3, 6, 1, 2, 1, 1, 4),
    _SysContact_Type()
)
sysContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysContact.setStatus("mandatory")


class _SysName_Type(DisplayString):
    """Custom type sysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysName_Type.__name__ = "DisplayString"
_SysName_Object = MibScalar
sysName = _SysName_Object(
    (1, 3, 6, 1, 2, 1, 1, 5),
    _SysName_Type()
)
sysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysName.setStatus("mandatory")


class _SysLocation_Type(DisplayString):
    """Custom type sysLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysLocation_Type.__name__ = "DisplayString"
_SysLocation_Object = MibScalar
sysLocation = _SysLocation_Object(
    (1, 3, 6, 1, 2, 1, 1, 6),
    _SysLocation_Type()
)
sysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLocation.setStatus("mandatory")


class _SysServices_Type(Integer32):
    """Custom type sysServices based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SysServices_Type.__name__ = "Integer32"
_SysServices_Object = MibScalar
sysServices = _SysServices_Object(
    (1, 3, 6, 1, 2, 1, 1, 7),
    _SysServices_Type()
)
sysServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysServices.setStatus("mandatory")
_SysORLastChange_Type = TimeStamp
_SysORLastChange_Object = MibScalar
sysORLastChange = _SysORLastChange_Object(
    (1, 3, 6, 1, 2, 1, 1, 8),
    _SysORLastChange_Type()
)
sysORLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysORLastChange.setStatus("current")
_Interfaces_ObjectIdentity = ObjectIdentity
interfaces = _Interfaces_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 2)
)
_IfNumber_Type = Integer32
_IfNumber_Object = MibScalar
ifNumber = _IfNumber_Object(
    (1, 3, 6, 1, 2, 1, 2, 1),
    _IfNumber_Type()
)
ifNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifNumber.setStatus("current")
_IfTable_ObjectIdentity = ObjectIdentity
ifTable = _IfTable_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 2, 2)
)
_IfEntry_ObjectIdentity = ObjectIdentity
ifEntry = _IfEntry_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 2, 2, 1)
)
_IfIndex_Type = InterfaceIndex
_IfIndex_Object = MibScalar
ifIndex = _IfIndex_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 1),
    _IfIndex_Type()
)
ifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIndex.setStatus("current")


class _IfDescr_Type(DisplayString):
    """Custom type ifDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IfDescr_Type.__name__ = "DisplayString"
_IfDescr_Object = MibScalar
ifDescr = _IfDescr_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 2),
    _IfDescr_Type()
)
ifDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifDescr.setStatus("current")
_IfType_Type = IANAifType
_IfType_Object = MibScalar
ifType = _IfType_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 3),
    _IfType_Type()
)
ifType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifType.setStatus("current")
_IfMtu_Type = Integer32
_IfMtu_Object = MibScalar
ifMtu = _IfMtu_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 4),
    _IfMtu_Type()
)
ifMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMtu.setStatus("current")
_IfSpeed_Type = Gauge32
_IfSpeed_Object = MibScalar
ifSpeed = _IfSpeed_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 5),
    _IfSpeed_Type()
)
ifSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSpeed.setStatus("current")
_IfPhysAddress_Type = PhysAddress
_IfPhysAddress_Object = MibScalar
ifPhysAddress = _IfPhysAddress_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 6),
    _IfPhysAddress_Type()
)
ifPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhysAddress.setStatus("current")


class _IfAdminStatus_Type(Integer32):
    """Custom type ifAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_IfAdminStatus_Type.__name__ = "Integer32"
_IfAdminStatus_Object = MibScalar
ifAdminStatus = _IfAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 7),
    _IfAdminStatus_Type()
)
ifAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifAdminStatus.setStatus("current")


class _IfOperStatus_Type(Integer32):
    """Custom type ifOperStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("unknown", 4),
          ("dormant", 5),
          ("notPresent", 6),
          ("lowerLayerDown", 7))
    )


_IfOperStatus_Type.__name__ = "Integer32"
_IfOperStatus_Object = MibScalar
ifOperStatus = _IfOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 8),
    _IfOperStatus_Type()
)
ifOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOperStatus.setStatus("current")
_IfLastChange_Type = TimeTicks
_IfLastChange_Object = MibScalar
ifLastChange = _IfLastChange_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 9),
    _IfLastChange_Type()
)
ifLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifLastChange.setStatus("current")
_IfInOctets_Type = Counter32
_IfInOctets_Object = MibScalar
ifInOctets = _IfInOctets_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 10),
    _IfInOctets_Type()
)
ifInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInOctets.setStatus("current")
_IfInUcastPkts_Type = Counter32
_IfInUcastPkts_Object = MibScalar
ifInUcastPkts = _IfInUcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 11),
    _IfInUcastPkts_Type()
)
ifInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInUcastPkts.setStatus("current")
_IfInNUcastPkts_Type = Counter32
_IfInNUcastPkts_Object = MibScalar
ifInNUcastPkts = _IfInNUcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 12),
    _IfInNUcastPkts_Type()
)
ifInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInNUcastPkts.setStatus("deprecated")
_IfInDiscards_Type = Counter32
_IfInDiscards_Object = MibScalar
ifInDiscards = _IfInDiscards_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 13),
    _IfInDiscards_Type()
)
ifInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInDiscards.setStatus("current")
_IfInErrors_Type = Counter32
_IfInErrors_Object = MibScalar
ifInErrors = _IfInErrors_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 14),
    _IfInErrors_Type()
)
ifInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInErrors.setStatus("current")
_IfInUnknownProtos_Type = Counter32
_IfInUnknownProtos_Object = MibScalar
ifInUnknownProtos = _IfInUnknownProtos_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 15),
    _IfInUnknownProtos_Type()
)
ifInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInUnknownProtos.setStatus("current")
_IfOutOctets_Type = Counter32
_IfOutOctets_Object = MibScalar
ifOutOctets = _IfOutOctets_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 16),
    _IfOutOctets_Type()
)
ifOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOutOctets.setStatus("current")
_IfOutUcastPkts_Type = Counter32
_IfOutUcastPkts_Object = MibScalar
ifOutUcastPkts = _IfOutUcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 17),
    _IfOutUcastPkts_Type()
)
ifOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOutUcastPkts.setStatus("current")
_IfOutNUcastPkts_Type = Counter32
_IfOutNUcastPkts_Object = MibScalar
ifOutNUcastPkts = _IfOutNUcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 18),
    _IfOutNUcastPkts_Type()
)
ifOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOutNUcastPkts.setStatus("deprecated")
_IfOutDiscards_Type = Counter32
_IfOutDiscards_Object = MibScalar
ifOutDiscards = _IfOutDiscards_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 19),
    _IfOutDiscards_Type()
)
ifOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOutDiscards.setStatus("current")
_IfOutErrors_Type = Counter32
_IfOutErrors_Object = MibScalar
ifOutErrors = _IfOutErrors_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 20),
    _IfOutErrors_Type()
)
ifOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOutErrors.setStatus("current")
_IfOutQLen_Type = Gauge32
_IfOutQLen_Object = MibScalar
ifOutQLen = _IfOutQLen_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 21),
    _IfOutQLen_Type()
)
ifOutQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOutQLen.setStatus("deprecated")
_IfSpecific_Type = ObjectIdentifier
_IfSpecific_Object = MibScalar
ifSpecific = _IfSpecific_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 22),
    _IfSpecific_Type()
)
ifSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSpecific.setStatus("deprecated")
_Ip_ObjectIdentity = ObjectIdentity
ip = _Ip_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 4)
)


class _IpForwarding_Type(Integer32):
    """Custom type ipForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 1),
          ("not-forwarding", 2))
    )


_IpForwarding_Type.__name__ = "Integer32"
_IpForwarding_Object = MibScalar
ipForwarding = _IpForwarding_Object(
    (1, 3, 6, 1, 2, 1, 4, 1),
    _IpForwarding_Type()
)
ipForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipForwarding.setStatus("mandatory")
_IpDefaultTTL_Type = Integer32
_IpDefaultTTL_Object = MibScalar
ipDefaultTTL = _IpDefaultTTL_Object(
    (1, 3, 6, 1, 2, 1, 4, 2),
    _IpDefaultTTL_Type()
)
ipDefaultTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDefaultTTL.setStatus("mandatory")
_IpInReceives_Type = Counter32
_IpInReceives_Object = MibScalar
ipInReceives = _IpInReceives_Object(
    (1, 3, 6, 1, 2, 1, 4, 3),
    _IpInReceives_Type()
)
ipInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInReceives.setStatus("mandatory")
_IpInHdrErrors_Type = Counter32
_IpInHdrErrors_Object = MibScalar
ipInHdrErrors = _IpInHdrErrors_Object(
    (1, 3, 6, 1, 2, 1, 4, 4),
    _IpInHdrErrors_Type()
)
ipInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInHdrErrors.setStatus("mandatory")
_IpInAddrErrors_Type = Counter32
_IpInAddrErrors_Object = MibScalar
ipInAddrErrors = _IpInAddrErrors_Object(
    (1, 3, 6, 1, 2, 1, 4, 5),
    _IpInAddrErrors_Type()
)
ipInAddrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInAddrErrors.setStatus("mandatory")
_IpForwDatagrams_Type = Counter32
_IpForwDatagrams_Object = MibScalar
ipForwDatagrams = _IpForwDatagrams_Object(
    (1, 3, 6, 1, 2, 1, 4, 6),
    _IpForwDatagrams_Type()
)
ipForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipForwDatagrams.setStatus("mandatory")
_IpInUnknownProtos_Type = Counter32
_IpInUnknownProtos_Object = MibScalar
ipInUnknownProtos = _IpInUnknownProtos_Object(
    (1, 3, 6, 1, 2, 1, 4, 7),
    _IpInUnknownProtos_Type()
)
ipInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInUnknownProtos.setStatus("mandatory")
_IpInDiscards_Type = Counter32
_IpInDiscards_Object = MibScalar
ipInDiscards = _IpInDiscards_Object(
    (1, 3, 6, 1, 2, 1, 4, 8),
    _IpInDiscards_Type()
)
ipInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInDiscards.setStatus("mandatory")
_IpInDelivers_Type = Counter32
_IpInDelivers_Object = MibScalar
ipInDelivers = _IpInDelivers_Object(
    (1, 3, 6, 1, 2, 1, 4, 9),
    _IpInDelivers_Type()
)
ipInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInDelivers.setStatus("mandatory")
_IpOutRequests_Type = Counter32
_IpOutRequests_Object = MibScalar
ipOutRequests = _IpOutRequests_Object(
    (1, 3, 6, 1, 2, 1, 4, 10),
    _IpOutRequests_Type()
)
ipOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOutRequests.setStatus("mandatory")
_IpOutDiscards_Type = Counter32
_IpOutDiscards_Object = MibScalar
ipOutDiscards = _IpOutDiscards_Object(
    (1, 3, 6, 1, 2, 1, 4, 11),
    _IpOutDiscards_Type()
)
ipOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOutDiscards.setStatus("mandatory")
_IpOutNoRoutes_Type = Counter32
_IpOutNoRoutes_Object = MibScalar
ipOutNoRoutes = _IpOutNoRoutes_Object(
    (1, 3, 6, 1, 2, 1, 4, 12),
    _IpOutNoRoutes_Type()
)
ipOutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOutNoRoutes.setStatus("mandatory")
_IpReasmTimeout_Type = Integer32
_IpReasmTimeout_Object = MibScalar
ipReasmTimeout = _IpReasmTimeout_Object(
    (1, 3, 6, 1, 2, 1, 4, 13),
    _IpReasmTimeout_Type()
)
ipReasmTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipReasmTimeout.setStatus("mandatory")
_IpReasmReqds_Type = Counter32
_IpReasmReqds_Object = MibScalar
ipReasmReqds = _IpReasmReqds_Object(
    (1, 3, 6, 1, 2, 1, 4, 14),
    _IpReasmReqds_Type()
)
ipReasmReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipReasmReqds.setStatus("mandatory")
_IpReasmOKs_Type = Counter32
_IpReasmOKs_Object = MibScalar
ipReasmOKs = _IpReasmOKs_Object(
    (1, 3, 6, 1, 2, 1, 4, 15),
    _IpReasmOKs_Type()
)
ipReasmOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipReasmOKs.setStatus("mandatory")
_IpReasmFails_Type = Counter32
_IpReasmFails_Object = MibScalar
ipReasmFails = _IpReasmFails_Object(
    (1, 3, 6, 1, 2, 1, 4, 16),
    _IpReasmFails_Type()
)
ipReasmFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipReasmFails.setStatus("mandatory")
_IpFragOKs_Type = Counter32
_IpFragOKs_Object = MibScalar
ipFragOKs = _IpFragOKs_Object(
    (1, 3, 6, 1, 2, 1, 4, 17),
    _IpFragOKs_Type()
)
ipFragOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFragOKs.setStatus("mandatory")
_IpFragFails_Type = Counter32
_IpFragFails_Object = MibScalar
ipFragFails = _IpFragFails_Object(
    (1, 3, 6, 1, 2, 1, 4, 18),
    _IpFragFails_Type()
)
ipFragFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFragFails.setStatus("mandatory")
_IpFragCreates_Type = Counter32
_IpFragCreates_Object = MibScalar
ipFragCreates = _IpFragCreates_Object(
    (1, 3, 6, 1, 2, 1, 4, 19),
    _IpFragCreates_Type()
)
ipFragCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFragCreates.setStatus("mandatory")
_IpAddrTable_ObjectIdentity = ObjectIdentity
ipAddrTable = _IpAddrTable_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 4, 20)
)
_IpAddrEntry_ObjectIdentity = ObjectIdentity
ipAddrEntry = _IpAddrEntry_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 4, 20, 1)
)
_IpAdEntAddr_Type = IpAddress
_IpAdEntAddr_Object = MibScalar
ipAdEntAddr = _IpAdEntAddr_Object(
    (1, 3, 6, 1, 2, 1, 4, 20, 1, 1),
    _IpAdEntAddr_Type()
)
ipAdEntAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAdEntAddr.setStatus("mandatory")
_IpAdEntIfIndex_Type = Integer32
_IpAdEntIfIndex_Object = MibScalar
ipAdEntIfIndex = _IpAdEntIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 4, 20, 1, 2),
    _IpAdEntIfIndex_Type()
)
ipAdEntIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAdEntIfIndex.setStatus("mandatory")
_IpAdEntNetMask_Type = IpAddress
_IpAdEntNetMask_Object = MibScalar
ipAdEntNetMask = _IpAdEntNetMask_Object(
    (1, 3, 6, 1, 2, 1, 4, 20, 1, 3),
    _IpAdEntNetMask_Type()
)
ipAdEntNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAdEntNetMask.setStatus("mandatory")
_IpAdEntBcastAddr_Type = Integer32
_IpAdEntBcastAddr_Object = MibScalar
ipAdEntBcastAddr = _IpAdEntBcastAddr_Object(
    (1, 3, 6, 1, 2, 1, 4, 20, 1, 4),
    _IpAdEntBcastAddr_Type()
)
ipAdEntBcastAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAdEntBcastAddr.setStatus("mandatory")
_IpRouteTable_ObjectIdentity = ObjectIdentity
ipRouteTable = _IpRouteTable_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 4, 21)
)
_IpRouteEntry_ObjectIdentity = ObjectIdentity
ipRouteEntry = _IpRouteEntry_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 4, 21, 1)
)
_IpRouteDest_Type = IpAddress
_IpRouteDest_Object = MibScalar
ipRouteDest = _IpRouteDest_Object(
    (1, 3, 6, 1, 2, 1, 4, 21, 1, 1),
    _IpRouteDest_Type()
)
ipRouteDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouteDest.setStatus("mandatory")
_IpRouteIfIndex_Type = Integer32
_IpRouteIfIndex_Object = MibScalar
ipRouteIfIndex = _IpRouteIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 4, 21, 1, 2),
    _IpRouteIfIndex_Type()
)
ipRouteIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouteIfIndex.setStatus("mandatory")
_IpRouteMetric1_Type = Integer32
_IpRouteMetric1_Object = MibScalar
ipRouteMetric1 = _IpRouteMetric1_Object(
    (1, 3, 6, 1, 2, 1, 4, 21, 1, 3),
    _IpRouteMetric1_Type()
)
ipRouteMetric1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouteMetric1.setStatus("mandatory")
_IpRouteNextHop_Type = IpAddress
_IpRouteNextHop_Object = MibScalar
ipRouteNextHop = _IpRouteNextHop_Object(
    (1, 3, 6, 1, 2, 1, 4, 21, 1, 7),
    _IpRouteNextHop_Type()
)
ipRouteNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouteNextHop.setStatus("mandatory")


class _IpRouteType_Type(Integer32):
    """Custom type ipRouteType based on Integer32"""
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
        *(("other", 1),
          ("invalid", 2),
          ("direct", 3),
          ("indirect", 4))
    )


_IpRouteType_Type.__name__ = "Integer32"
_IpRouteType_Object = MibScalar
ipRouteType = _IpRouteType_Object(
    (1, 3, 6, 1, 2, 1, 4, 21, 1, 8),
    _IpRouteType_Type()
)
ipRouteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouteType.setStatus("mandatory")


class _IpRouteProto_Type(Integer32):
    """Custom type ipRouteProto based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("local", 2),
          ("netmgmt", 3),
          ("icmp", 4),
          ("egp", 5),
          ("ggp", 6),
          ("hello", 7),
          ("rip", 8),
          ("is-is", 9),
          ("es-is", 10),
          ("ciscoIgrp", 11),
          ("bbnSpfIgp", 12),
          ("ospf", 13),
          ("bgp", 14))
    )


_IpRouteProto_Type.__name__ = "Integer32"
_IpRouteProto_Object = MibScalar
ipRouteProto = _IpRouteProto_Object(
    (1, 3, 6, 1, 2, 1, 4, 21, 1, 9),
    _IpRouteProto_Type()
)
ipRouteProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteProto.setStatus("mandatory")
_IpRouteMask_Type = IpAddress
_IpRouteMask_Object = MibScalar
ipRouteMask = _IpRouteMask_Object(
    (1, 3, 6, 1, 2, 1, 4, 21, 1, 11),
    _IpRouteMask_Type()
)
ipRouteMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouteMask.setStatus("mandatory")
_IpRouteInfo_Type = ObjectIdentifier
_IpRouteInfo_Object = MibScalar
ipRouteInfo = _IpRouteInfo_Object(
    (1, 3, 6, 1, 2, 1, 4, 21, 1, 13),
    _IpRouteInfo_Type()
)
ipRouteInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteInfo.setStatus("mandatory")
_IpNetToMediaTable_ObjectIdentity = ObjectIdentity
ipNetToMediaTable = _IpNetToMediaTable_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 4, 22)
)
_IpNetToMediaEntry_ObjectIdentity = ObjectIdentity
ipNetToMediaEntry = _IpNetToMediaEntry_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 4, 22, 1)
)
_IpNetToMediaIfIndex_Type = Integer32
_IpNetToMediaIfIndex_Object = MibScalar
ipNetToMediaIfIndex = _IpNetToMediaIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 4, 22, 1, 1),
    _IpNetToMediaIfIndex_Type()
)
ipNetToMediaIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNetToMediaIfIndex.setStatus("mandatory")
_IpNetToMediaPhysAddress_Type = PhysAddress
_IpNetToMediaPhysAddress_Object = MibScalar
ipNetToMediaPhysAddress = _IpNetToMediaPhysAddress_Object(
    (1, 3, 6, 1, 2, 1, 4, 22, 1, 2),
    _IpNetToMediaPhysAddress_Type()
)
ipNetToMediaPhysAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNetToMediaPhysAddress.setStatus("mandatory")
_IpNetToMediaNetAddress_Type = IpAddress
_IpNetToMediaNetAddress_Object = MibScalar
ipNetToMediaNetAddress = _IpNetToMediaNetAddress_Object(
    (1, 3, 6, 1, 2, 1, 4, 22, 1, 3),
    _IpNetToMediaNetAddress_Type()
)
ipNetToMediaNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNetToMediaNetAddress.setStatus("mandatory")


class _IpNetToMediaType_Type(Integer32):
    """Custom type ipNetToMediaType based on Integer32"""
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
        *(("other", 1),
          ("invalid", 2),
          ("dynamic", 3),
          ("static", 4))
    )


_IpNetToMediaType_Type.__name__ = "Integer32"
_IpNetToMediaType_Object = MibScalar
ipNetToMediaType = _IpNetToMediaType_Object(
    (1, 3, 6, 1, 2, 1, 4, 22, 1, 4),
    _IpNetToMediaType_Type()
)
ipNetToMediaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNetToMediaType.setStatus("mandatory")
_IpRoutingDiscards_Type = Counter32
_IpRoutingDiscards_Object = MibScalar
ipRoutingDiscards = _IpRoutingDiscards_Object(
    (1, 3, 6, 1, 2, 1, 4, 23),
    _IpRoutingDiscards_Type()
)
ipRoutingDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRoutingDiscards.setStatus("mandatory")
_Snmp_ObjectIdentity = ObjectIdentity
snmp = _Snmp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 11)
)
_SnmpInPkts_Type = Counter32
_SnmpInPkts_Object = MibScalar
snmpInPkts = _SnmpInPkts_Object(
    (1, 3, 6, 1, 2, 1, 11, 1),
    _SnmpInPkts_Type()
)
snmpInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInPkts.setStatus("mandatory")
_SnmpOutPkts_Type = Counter32
_SnmpOutPkts_Object = MibScalar
snmpOutPkts = _SnmpOutPkts_Object(
    (1, 3, 6, 1, 2, 1, 11, 2),
    _SnmpOutPkts_Type()
)
snmpOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpOutPkts.setStatus("mandatory")
_SnmpInBadVersions_Type = Counter32
_SnmpInBadVersions_Object = MibScalar
snmpInBadVersions = _SnmpInBadVersions_Object(
    (1, 3, 6, 1, 2, 1, 11, 3),
    _SnmpInBadVersions_Type()
)
snmpInBadVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInBadVersions.setStatus("mandatory")
_SnmpInBadCommunityNames_Type = Counter32
_SnmpInBadCommunityNames_Object = MibScalar
snmpInBadCommunityNames = _SnmpInBadCommunityNames_Object(
    (1, 3, 6, 1, 2, 1, 11, 4),
    _SnmpInBadCommunityNames_Type()
)
snmpInBadCommunityNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInBadCommunityNames.setStatus("mandatory")
_SnmpInBadCommunityUses_Type = Counter32
_SnmpInBadCommunityUses_Object = MibScalar
snmpInBadCommunityUses = _SnmpInBadCommunityUses_Object(
    (1, 3, 6, 1, 2, 1, 11, 5),
    _SnmpInBadCommunityUses_Type()
)
snmpInBadCommunityUses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInBadCommunityUses.setStatus("mandatory")
_SnmpInASNParseErrs_Type = Counter32
_SnmpInASNParseErrs_Object = MibScalar
snmpInASNParseErrs = _SnmpInASNParseErrs_Object(
    (1, 3, 6, 1, 2, 1, 11, 6),
    _SnmpInASNParseErrs_Type()
)
snmpInASNParseErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInASNParseErrs.setStatus("mandatory")
_SnmpInTooBigs_Type = Counter32
_SnmpInTooBigs_Object = MibScalar
snmpInTooBigs = _SnmpInTooBigs_Object(
    (1, 3, 6, 1, 2, 1, 11, 8),
    _SnmpInTooBigs_Type()
)
snmpInTooBigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInTooBigs.setStatus("mandatory")
_SnmpInNoSuchNames_Type = Counter32
_SnmpInNoSuchNames_Object = MibScalar
snmpInNoSuchNames = _SnmpInNoSuchNames_Object(
    (1, 3, 6, 1, 2, 1, 11, 9),
    _SnmpInNoSuchNames_Type()
)
snmpInNoSuchNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInNoSuchNames.setStatus("mandatory")
_SnmpInBadValues_Type = Counter32
_SnmpInBadValues_Object = MibScalar
snmpInBadValues = _SnmpInBadValues_Object(
    (1, 3, 6, 1, 2, 1, 11, 10),
    _SnmpInBadValues_Type()
)
snmpInBadValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInBadValues.setStatus("mandatory")
_SnmpInReadOnlys_Type = Counter32
_SnmpInReadOnlys_Object = MibScalar
snmpInReadOnlys = _SnmpInReadOnlys_Object(
    (1, 3, 6, 1, 2, 1, 11, 11),
    _SnmpInReadOnlys_Type()
)
snmpInReadOnlys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInReadOnlys.setStatus("mandatory")
_SnmpInGenErrs_Type = Counter32
_SnmpInGenErrs_Object = MibScalar
snmpInGenErrs = _SnmpInGenErrs_Object(
    (1, 3, 6, 1, 2, 1, 11, 12),
    _SnmpInGenErrs_Type()
)
snmpInGenErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInGenErrs.setStatus("mandatory")
_SnmpInTotalReqVars_Type = Counter32
_SnmpInTotalReqVars_Object = MibScalar
snmpInTotalReqVars = _SnmpInTotalReqVars_Object(
    (1, 3, 6, 1, 2, 1, 11, 13),
    _SnmpInTotalReqVars_Type()
)
snmpInTotalReqVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInTotalReqVars.setStatus("mandatory")
_SnmpInTotalSetVars_Type = Counter32
_SnmpInTotalSetVars_Object = MibScalar
snmpInTotalSetVars = _SnmpInTotalSetVars_Object(
    (1, 3, 6, 1, 2, 1, 11, 14),
    _SnmpInTotalSetVars_Type()
)
snmpInTotalSetVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInTotalSetVars.setStatus("mandatory")
_SnmpInGetRequests_Type = Counter32
_SnmpInGetRequests_Object = MibScalar
snmpInGetRequests = _SnmpInGetRequests_Object(
    (1, 3, 6, 1, 2, 1, 11, 15),
    _SnmpInGetRequests_Type()
)
snmpInGetRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInGetRequests.setStatus("mandatory")
_SnmpInGetNexts_Type = Counter32
_SnmpInGetNexts_Object = MibScalar
snmpInGetNexts = _SnmpInGetNexts_Object(
    (1, 3, 6, 1, 2, 1, 11, 16),
    _SnmpInGetNexts_Type()
)
snmpInGetNexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInGetNexts.setStatus("mandatory")
_SnmpInSetRequests_Type = Counter32
_SnmpInSetRequests_Object = MibScalar
snmpInSetRequests = _SnmpInSetRequests_Object(
    (1, 3, 6, 1, 2, 1, 11, 17),
    _SnmpInSetRequests_Type()
)
snmpInSetRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInSetRequests.setStatus("mandatory")
_SnmpInGetResponses_Type = Counter32
_SnmpInGetResponses_Object = MibScalar
snmpInGetResponses = _SnmpInGetResponses_Object(
    (1, 3, 6, 1, 2, 1, 11, 18),
    _SnmpInGetResponses_Type()
)
snmpInGetResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInGetResponses.setStatus("mandatory")
_SnmpInTraps_Type = Counter32
_SnmpInTraps_Object = MibScalar
snmpInTraps = _SnmpInTraps_Object(
    (1, 3, 6, 1, 2, 1, 11, 19),
    _SnmpInTraps_Type()
)
snmpInTraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInTraps.setStatus("mandatory")
_SnmpOutTooBigs_Type = Counter32
_SnmpOutTooBigs_Object = MibScalar
snmpOutTooBigs = _SnmpOutTooBigs_Object(
    (1, 3, 6, 1, 2, 1, 11, 20),
    _SnmpOutTooBigs_Type()
)
snmpOutTooBigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpOutTooBigs.setStatus("mandatory")
_SnmpOutNoSuchNames_Type = Counter32
_SnmpOutNoSuchNames_Object = MibScalar
snmpOutNoSuchNames = _SnmpOutNoSuchNames_Object(
    (1, 3, 6, 1, 2, 1, 11, 21),
    _SnmpOutNoSuchNames_Type()
)
snmpOutNoSuchNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpOutNoSuchNames.setStatus("mandatory")
_SnmpOutBadValues_Type = Counter32
_SnmpOutBadValues_Object = MibScalar
snmpOutBadValues = _SnmpOutBadValues_Object(
    (1, 3, 6, 1, 2, 1, 11, 22),
    _SnmpOutBadValues_Type()
)
snmpOutBadValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpOutBadValues.setStatus("mandatory")
_SnmpOutGenErrs_Type = Counter32
_SnmpOutGenErrs_Object = MibScalar
snmpOutGenErrs = _SnmpOutGenErrs_Object(
    (1, 3, 6, 1, 2, 1, 11, 24),
    _SnmpOutGenErrs_Type()
)
snmpOutGenErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpOutGenErrs.setStatus("mandatory")
_SnmpOutGetRequests_Type = Counter32
_SnmpOutGetRequests_Object = MibScalar
snmpOutGetRequests = _SnmpOutGetRequests_Object(
    (1, 3, 6, 1, 2, 1, 11, 25),
    _SnmpOutGetRequests_Type()
)
snmpOutGetRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpOutGetRequests.setStatus("mandatory")
_SnmpOutGetNexts_Type = Counter32
_SnmpOutGetNexts_Object = MibScalar
snmpOutGetNexts = _SnmpOutGetNexts_Object(
    (1, 3, 6, 1, 2, 1, 11, 26),
    _SnmpOutGetNexts_Type()
)
snmpOutGetNexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpOutGetNexts.setStatus("mandatory")
_SnmpOutSetRequests_Type = Counter32
_SnmpOutSetRequests_Object = MibScalar
snmpOutSetRequests = _SnmpOutSetRequests_Object(
    (1, 3, 6, 1, 2, 1, 11, 27),
    _SnmpOutSetRequests_Type()
)
snmpOutSetRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpOutSetRequests.setStatus("mandatory")
_SnmpOutGetResponses_Type = Counter32
_SnmpOutGetResponses_Object = MibScalar
snmpOutGetResponses = _SnmpOutGetResponses_Object(
    (1, 3, 6, 1, 2, 1, 11, 28),
    _SnmpOutGetResponses_Type()
)
snmpOutGetResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpOutGetResponses.setStatus("mandatory")
_SnmpOutTraps_Type = Counter32
_SnmpOutTraps_Object = MibScalar
snmpOutTraps = _SnmpOutTraps_Object(
    (1, 3, 6, 1, 2, 1, 11, 29),
    _SnmpOutTraps_Type()
)
snmpOutTraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpOutTraps.setStatus("mandatory")


class _SnmpEnableAuthenTraps_Type(Integer32):
    """Custom type snmpEnableAuthenTraps based on Integer32"""
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


_SnmpEnableAuthenTraps_Type.__name__ = "Integer32"
_SnmpEnableAuthenTraps_Object = MibScalar
snmpEnableAuthenTraps = _SnmpEnableAuthenTraps_Object(
    (1, 3, 6, 1, 2, 1, 11, 30),
    _SnmpEnableAuthenTraps_Type()
)
snmpEnableAuthenTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpEnableAuthenTraps.setStatus("mandatory")
_SnmpSilentDrops_Type = Counter32
_SnmpSilentDrops_Object = MibScalar
snmpSilentDrops = _SnmpSilentDrops_Object(
    (1, 3, 6, 1, 2, 1, 11, 31),
    _SnmpSilentDrops_Type()
)
snmpSilentDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpSilentDrops.setStatus("current")
_SnmpProxyDrops_Type = Counter32
_SnmpProxyDrops_Object = MibScalar
snmpProxyDrops = _SnmpProxyDrops_Object(
    (1, 3, 6, 1, 2, 1, 11, 32),
    _SnmpProxyDrops_Type()
)
snmpProxyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpProxyDrops.setStatus("current")
_Host_ObjectIdentity = ObjectIdentity
host = _Host_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25)
)
_HrSystem_ObjectIdentity = ObjectIdentity
hrSystem = _HrSystem_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 1)
)
_HrSystemUptime_Type = TimeTicks
_HrSystemUptime_Object = MibScalar
hrSystemUptime = _HrSystemUptime_Object(
    (1, 3, 6, 1, 2, 1, 25, 1, 1),
    _HrSystemUptime_Type()
)
hrSystemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrSystemUptime.setStatus("current")
_HrSystemDate_Type = DateAndTime
_HrSystemDate_Object = MibScalar
hrSystemDate = _HrSystemDate_Object(
    (1, 3, 6, 1, 2, 1, 25, 1, 2),
    _HrSystemDate_Type()
)
hrSystemDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hrSystemDate.setStatus("current")


class _HrSystemInitialLoadDevice_Type(Integer32):
    """Custom type hrSystemInitialLoadDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HrSystemInitialLoadDevice_Type.__name__ = "Integer32"
_HrSystemInitialLoadDevice_Object = MibScalar
hrSystemInitialLoadDevice = _HrSystemInitialLoadDevice_Object(
    (1, 3, 6, 1, 2, 1, 25, 1, 3),
    _HrSystemInitialLoadDevice_Type()
)
hrSystemInitialLoadDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hrSystemInitialLoadDevice.setStatus("current")


class _HrSystemInitialLoadParameters_Type(InternationalDisplayString):
    """Custom type hrSystemInitialLoadParameters based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HrSystemInitialLoadParameters_Type.__name__ = "InternationalDisplayString"
_HrSystemInitialLoadParameters_Object = MibScalar
hrSystemInitialLoadParameters = _HrSystemInitialLoadParameters_Object(
    (1, 3, 6, 1, 2, 1, 25, 1, 4),
    _HrSystemInitialLoadParameters_Type()
)
hrSystemInitialLoadParameters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hrSystemInitialLoadParameters.setStatus("current")
_HrSystemNumUsers_Type = Gauge32
_HrSystemNumUsers_Object = MibScalar
hrSystemNumUsers = _HrSystemNumUsers_Object(
    (1, 3, 6, 1, 2, 1, 25, 1, 5),
    _HrSystemNumUsers_Type()
)
hrSystemNumUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrSystemNumUsers.setStatus("current")
_HrSystemProcesses_Type = Gauge32
_HrSystemProcesses_Object = MibScalar
hrSystemProcesses = _HrSystemProcesses_Object(
    (1, 3, 6, 1, 2, 1, 25, 1, 6),
    _HrSystemProcesses_Type()
)
hrSystemProcesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrSystemProcesses.setStatus("current")


class _HrSystemMaxProcesses_Type(Integer32):
    """Custom type hrSystemMaxProcesses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HrSystemMaxProcesses_Type.__name__ = "Integer32"
_HrSystemMaxProcesses_Object = MibScalar
hrSystemMaxProcesses = _HrSystemMaxProcesses_Object(
    (1, 3, 6, 1, 2, 1, 25, 1, 7),
    _HrSystemMaxProcesses_Type()
)
hrSystemMaxProcesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrSystemMaxProcesses.setStatus("current")
_HrStorage_ObjectIdentity = ObjectIdentity
hrStorage = _HrStorage_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 2)
)
_HrMemorySize_Type = KBytes
_HrMemorySize_Object = MibScalar
hrMemorySize = _HrMemorySize_Object(
    (1, 3, 6, 1, 2, 1, 25, 2, 2),
    _HrMemorySize_Type()
)
hrMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrMemorySize.setStatus("current")
if mibBuilder.loadTexts:
    hrMemorySize.setUnits("KBytes")
_HrStorageTable_ObjectIdentity = ObjectIdentity
hrStorageTable = _HrStorageTable_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 2, 3)
)
_HrStorageEntry_ObjectIdentity = ObjectIdentity
hrStorageEntry = _HrStorageEntry_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 2, 3, 1)
)


class _HrStorageIndex_Type(Integer32):
    """Custom type hrStorageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HrStorageIndex_Type.__name__ = "Integer32"
_HrStorageIndex_Object = MibScalar
hrStorageIndex = _HrStorageIndex_Object(
    (1, 3, 6, 1, 2, 1, 25, 2, 3, 1, 1),
    _HrStorageIndex_Type()
)
hrStorageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrStorageIndex.setStatus("current")
_HrStorageType_Type = AutonomousType
_HrStorageType_Object = MibScalar
hrStorageType = _HrStorageType_Object(
    (1, 3, 6, 1, 2, 1, 25, 2, 3, 1, 2),
    _HrStorageType_Type()
)
hrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrStorageType.setStatus("current")
_HrStorageDescr_Type = DisplayString
_HrStorageDescr_Object = MibScalar
hrStorageDescr = _HrStorageDescr_Object(
    (1, 3, 6, 1, 2, 1, 25, 2, 3, 1, 3),
    _HrStorageDescr_Type()
)
hrStorageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrStorageDescr.setStatus("current")


class _HrStorageAllocationUnits_Type(Integer32):
    """Custom type hrStorageAllocationUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HrStorageAllocationUnits_Type.__name__ = "Integer32"
_HrStorageAllocationUnits_Object = MibScalar
hrStorageAllocationUnits = _HrStorageAllocationUnits_Object(
    (1, 3, 6, 1, 2, 1, 25, 2, 3, 1, 4),
    _HrStorageAllocationUnits_Type()
)
hrStorageAllocationUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrStorageAllocationUnits.setStatus("current")
if mibBuilder.loadTexts:
    hrStorageAllocationUnits.setUnits("Bytes")


class _HrStorageSize_Type(Integer32):
    """Custom type hrStorageSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HrStorageSize_Type.__name__ = "Integer32"
_HrStorageSize_Object = MibScalar
hrStorageSize = _HrStorageSize_Object(
    (1, 3, 6, 1, 2, 1, 25, 2, 3, 1, 5),
    _HrStorageSize_Type()
)
hrStorageSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hrStorageSize.setStatus("current")


class _HrStorageUsed_Type(Integer32):
    """Custom type hrStorageUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HrStorageUsed_Type.__name__ = "Integer32"
_HrStorageUsed_Object = MibScalar
hrStorageUsed = _HrStorageUsed_Object(
    (1, 3, 6, 1, 2, 1, 25, 2, 3, 1, 6),
    _HrStorageUsed_Type()
)
hrStorageUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrStorageUsed.setStatus("current")
_HrDevice_ObjectIdentity = ObjectIdentity
hrDevice = _HrDevice_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3)
)
_HrDeviceTable_ObjectIdentity = ObjectIdentity
hrDeviceTable = _HrDeviceTable_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 2)
)
_HrDeviceEntry_ObjectIdentity = ObjectIdentity
hrDeviceEntry = _HrDeviceEntry_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 2, 1)
)


class _HrDeviceIndex_Type(Integer32):
    """Custom type hrDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HrDeviceIndex_Type.__name__ = "Integer32"
_HrDeviceIndex_Object = MibScalar
hrDeviceIndex = _HrDeviceIndex_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 2, 1, 1),
    _HrDeviceIndex_Type()
)
hrDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrDeviceIndex.setStatus("current")
_HrDeviceType_Type = AutonomousType
_HrDeviceType_Object = MibScalar
hrDeviceType = _HrDeviceType_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 2, 1, 2),
    _HrDeviceType_Type()
)
hrDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrDeviceType.setStatus("current")


class _HrDeviceDescr_Type(DisplayString):
    """Custom type hrDeviceDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HrDeviceDescr_Type.__name__ = "DisplayString"
_HrDeviceDescr_Object = MibScalar
hrDeviceDescr = _HrDeviceDescr_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 2, 1, 3),
    _HrDeviceDescr_Type()
)
hrDeviceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrDeviceDescr.setStatus("current")
_HrDeviceID_Type = ProductID
_HrDeviceID_Object = MibScalar
hrDeviceID = _HrDeviceID_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 2, 1, 4),
    _HrDeviceID_Type()
)
hrDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrDeviceID.setStatus("current")


class _HrDeviceStatus_Type(Integer32):
    """Custom type hrDeviceStatus based on Integer32"""
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
        *(("unknown", 1),
          ("running", 2),
          ("warning", 3),
          ("testing", 4),
          ("down", 5))
    )


_HrDeviceStatus_Type.__name__ = "Integer32"
_HrDeviceStatus_Object = MibScalar
hrDeviceStatus = _HrDeviceStatus_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 2, 1, 5),
    _HrDeviceStatus_Type()
)
hrDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrDeviceStatus.setStatus("current")
_HrDeviceErrors_Type = Counter32
_HrDeviceErrors_Object = MibScalar
hrDeviceErrors = _HrDeviceErrors_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 2, 1, 6),
    _HrDeviceErrors_Type()
)
hrDeviceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrDeviceErrors.setStatus("current")
_HrPrinterTable_ObjectIdentity = ObjectIdentity
hrPrinterTable = _HrPrinterTable_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 5)
)
_HrPrinterEntry_ObjectIdentity = ObjectIdentity
hrPrinterEntry = _HrPrinterEntry_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 5, 1)
)


class _HrPrinterStatus_Type(Integer32):
    """Custom type hrPrinterStatus based on Integer32"""
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
        *(("other", 1),
          ("unknown", 2),
          ("idle", 3),
          ("printing", 4),
          ("warmup", 5))
    )


_HrPrinterStatus_Type.__name__ = "Integer32"
_HrPrinterStatus_Object = MibScalar
hrPrinterStatus = _HrPrinterStatus_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 5, 1, 1),
    _HrPrinterStatus_Type()
)
hrPrinterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrPrinterStatus.setStatus("current")
_HrPrinterDetectedErrorState_Type = OctetString
_HrPrinterDetectedErrorState_Object = MibScalar
hrPrinterDetectedErrorState = _HrPrinterDetectedErrorState_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 5, 1, 2),
    _HrPrinterDetectedErrorState_Type()
)
hrPrinterDetectedErrorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrPrinterDetectedErrorState.setStatus("current")
_IfMIB_ObjectIdentity = ObjectIdentity
ifMIB = _IfMIB_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 31)
)
_IfMIBObjects_ObjectIdentity = ObjectIdentity
ifMIBObjects = _IfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 31, 1)
)
_IfTableLastChange_Type = TimeTicks
_IfTableLastChange_Object = MibScalar
ifTableLastChange = _IfTableLastChange_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 5),
    _IfTableLastChange_Type()
)
ifTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTableLastChange.setStatus("current")
_Printmib_ObjectIdentity = ObjectIdentity
printmib = _Printmib_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43)
)
_PrtGeneral_ObjectIdentity = ObjectIdentity
prtGeneral = _PrtGeneral_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 5)
)
_PrtGeneralTable_ObjectIdentity = ObjectIdentity
prtGeneralTable = _PrtGeneralTable_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 5, 1)
)
_PrtGeneralEntry_ObjectIdentity = ObjectIdentity
prtGeneralEntry = _PrtGeneralEntry_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 5, 1, 1)
)
_PrtGeneralConfigChanges_Type = Counter32
_PrtGeneralConfigChanges_Object = MibScalar
prtGeneralConfigChanges = _PrtGeneralConfigChanges_Object(
    (1, 3, 6, 1, 2, 1, 43, 5, 1, 1, 1),
    _PrtGeneralConfigChanges_Type()
)
prtGeneralConfigChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtGeneralConfigChanges.setStatus("current")


class _PrtGeneralCurrentLocalization_Type(Integer32):
    """Custom type prtGeneralCurrentLocalization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PrtGeneralCurrentLocalization_Type.__name__ = "Integer32"
_PrtGeneralCurrentLocalization_Object = MibScalar
prtGeneralCurrentLocalization = _PrtGeneralCurrentLocalization_Object(
    (1, 3, 6, 1, 2, 1, 43, 5, 1, 1, 2),
    _PrtGeneralCurrentLocalization_Type()
)
prtGeneralCurrentLocalization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtGeneralCurrentLocalization.setStatus("current")
_PrtGeneralReset_Type = PrtGeneralResetTC
_PrtGeneralReset_Object = MibScalar
prtGeneralReset = _PrtGeneralReset_Object(
    (1, 3, 6, 1, 2, 1, 43, 5, 1, 1, 3),
    _PrtGeneralReset_Type()
)
prtGeneralReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtGeneralReset.setStatus("current")


class _PrtGeneralCurrentOperator_Type(OctetString):
    """Custom type prtGeneralCurrentOperator based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_PrtGeneralCurrentOperator_Type.__name__ = "OctetString"
_PrtGeneralCurrentOperator_Object = MibScalar
prtGeneralCurrentOperator = _PrtGeneralCurrentOperator_Object(
    (1, 3, 6, 1, 2, 1, 43, 5, 1, 1, 4),
    _PrtGeneralCurrentOperator_Type()
)
prtGeneralCurrentOperator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtGeneralCurrentOperator.setStatus("current")


class _PrtGeneralServicePerson_Type(OctetString):
    """Custom type prtGeneralServicePerson based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_PrtGeneralServicePerson_Type.__name__ = "OctetString"
_PrtGeneralServicePerson_Object = MibScalar
prtGeneralServicePerson = _PrtGeneralServicePerson_Object(
    (1, 3, 6, 1, 2, 1, 43, 5, 1, 1, 5),
    _PrtGeneralServicePerson_Type()
)
prtGeneralServicePerson.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtGeneralServicePerson.setStatus("current")


class _PrtInputDefaultIndex_Type(Integer32):
    """Custom type prtInputDefaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PrtInputDefaultIndex_Type.__name__ = "Integer32"
_PrtInputDefaultIndex_Object = MibScalar
prtInputDefaultIndex = _PrtInputDefaultIndex_Object(
    (1, 3, 6, 1, 2, 1, 43, 5, 1, 1, 6),
    _PrtInputDefaultIndex_Type()
)
prtInputDefaultIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInputDefaultIndex.setStatus("current")


class _PrtOutputDefaultIndex_Type(Integer32):
    """Custom type prtOutputDefaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PrtOutputDefaultIndex_Type.__name__ = "Integer32"
_PrtOutputDefaultIndex_Object = MibScalar
prtOutputDefaultIndex = _PrtOutputDefaultIndex_Object(
    (1, 3, 6, 1, 2, 1, 43, 5, 1, 1, 7),
    _PrtOutputDefaultIndex_Type()
)
prtOutputDefaultIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtOutputDefaultIndex.setStatus("current")


class _PrtMarkerDefaultIndex_Type(Integer32):
    """Custom type prtMarkerDefaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PrtMarkerDefaultIndex_Type.__name__ = "Integer32"
_PrtMarkerDefaultIndex_Object = MibScalar
prtMarkerDefaultIndex = _PrtMarkerDefaultIndex_Object(
    (1, 3, 6, 1, 2, 1, 43, 5, 1, 1, 8),
    _PrtMarkerDefaultIndex_Type()
)
prtMarkerDefaultIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtMarkerDefaultIndex.setStatus("current")


class _PrtMediaPathDefaultIndex_Type(Integer32):
    """Custom type prtMediaPathDefaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PrtMediaPathDefaultIndex_Type.__name__ = "Integer32"
_PrtMediaPathDefaultIndex_Object = MibScalar
prtMediaPathDefaultIndex = _PrtMediaPathDefaultIndex_Object(
    (1, 3, 6, 1, 2, 1, 43, 5, 1, 1, 9),
    _PrtMediaPathDefaultIndex_Type()
)
prtMediaPathDefaultIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtMediaPathDefaultIndex.setStatus("current")


class _PrtConsoleLocalization_Type(Integer32):
    """Custom type prtConsoleLocalization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PrtConsoleLocalization_Type.__name__ = "Integer32"
_PrtConsoleLocalization_Object = MibScalar
prtConsoleLocalization = _PrtConsoleLocalization_Object(
    (1, 3, 6, 1, 2, 1, 43, 5, 1, 1, 10),
    _PrtConsoleLocalization_Type()
)
prtConsoleLocalization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtConsoleLocalization.setStatus("current")


class _PrtConsoleNumberOfDisplayLines_Type(Integer32):
    """Custom type prtConsoleNumberOfDisplayLines based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PrtConsoleNumberOfDisplayLines_Type.__name__ = "Integer32"
_PrtConsoleNumberOfDisplayLines_Object = MibScalar
prtConsoleNumberOfDisplayLines = _PrtConsoleNumberOfDisplayLines_Object(
    (1, 3, 6, 1, 2, 1, 43, 5, 1, 1, 11),
    _PrtConsoleNumberOfDisplayLines_Type()
)
prtConsoleNumberOfDisplayLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtConsoleNumberOfDisplayLines.setStatus("current")


class _PrtGeneralPrinterName_Type(OctetString):
    """Custom type prtGeneralPrinterName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_PrtGeneralPrinterName_Type.__name__ = "OctetString"
_PrtGeneralPrinterName_Object = MibScalar
prtGeneralPrinterName = _PrtGeneralPrinterName_Object(
    (1, 3, 6, 1, 2, 1, 43, 5, 1, 1, 16),
    _PrtGeneralPrinterName_Type()
)
prtGeneralPrinterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtGeneralPrinterName.setStatus("current")


class _PrtGeneralSerialNumber_Type(OctetString):
    """Custom type prtGeneralSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PrtGeneralSerialNumber_Type.__name__ = "OctetString"
_PrtGeneralSerialNumber_Object = MibScalar
prtGeneralSerialNumber = _PrtGeneralSerialNumber_Object(
    (1, 3, 6, 1, 2, 1, 43, 5, 1, 1, 17),
    _PrtGeneralSerialNumber_Type()
)
prtGeneralSerialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtGeneralSerialNumber.setStatus("current")
_PrtCover_ObjectIdentity = ObjectIdentity
prtCover = _PrtCover_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 6)
)
_PrtCoverTable_ObjectIdentity = ObjectIdentity
prtCoverTable = _PrtCoverTable_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 6, 1)
)
_PrtCoverEntry_ObjectIdentity = ObjectIdentity
prtCoverEntry = _PrtCoverEntry_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 6, 1, 1)
)
_PrtCoverDescription_Type = PrtLocalizedDescriptionStringTC
_PrtCoverDescription_Object = MibScalar
prtCoverDescription = _PrtCoverDescription_Object(
    (1, 3, 6, 1, 2, 1, 43, 6, 1, 1, 2),
    _PrtCoverDescription_Type()
)
prtCoverDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtCoverDescription.setStatus("current")
_PrtCoverStatus_Type = PrtCoverStatusTC
_PrtCoverStatus_Object = MibScalar
prtCoverStatus = _PrtCoverStatus_Object(
    (1, 3, 6, 1, 2, 1, 43, 6, 1, 1, 3),
    _PrtCoverStatus_Type()
)
prtCoverStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtCoverStatus.setStatus("current")
_PrtLocalization_ObjectIdentity = ObjectIdentity
prtLocalization = _PrtLocalization_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 7)
)
_PrtLocalizationTable_ObjectIdentity = ObjectIdentity
prtLocalizationTable = _PrtLocalizationTable_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 7, 1)
)
_PrtLocalizationEntry_ObjectIdentity = ObjectIdentity
prtLocalizationEntry = _PrtLocalizationEntry_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 7, 1, 1)
)


class _PrtLocalizationLanguage_Type(OctetString):
    """Custom type prtLocalizationLanguage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_PrtLocalizationLanguage_Type.__name__ = "OctetString"
_PrtLocalizationLanguage_Object = MibScalar
prtLocalizationLanguage = _PrtLocalizationLanguage_Object(
    (1, 3, 6, 1, 2, 1, 43, 7, 1, 1, 2),
    _PrtLocalizationLanguage_Type()
)
prtLocalizationLanguage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtLocalizationLanguage.setStatus("current")


class _PrtLocalizationCountry_Type(OctetString):
    """Custom type prtLocalizationCountry based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_PrtLocalizationCountry_Type.__name__ = "OctetString"
_PrtLocalizationCountry_Object = MibScalar
prtLocalizationCountry = _PrtLocalizationCountry_Object(
    (1, 3, 6, 1, 2, 1, 43, 7, 1, 1, 3),
    _PrtLocalizationCountry_Type()
)
prtLocalizationCountry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtLocalizationCountry.setStatus("current")
_PrtLocalizationCharacterSet_Type = IANACharset
_PrtLocalizationCharacterSet_Object = MibScalar
prtLocalizationCharacterSet = _PrtLocalizationCharacterSet_Object(
    (1, 3, 6, 1, 2, 1, 43, 7, 1, 1, 4),
    _PrtLocalizationCharacterSet_Type()
)
prtLocalizationCharacterSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtLocalizationCharacterSet.setStatus("current")
_PrtInput_ObjectIdentity = ObjectIdentity
prtInput = _PrtInput_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 8)
)
_PrtInputTable_ObjectIdentity = ObjectIdentity
prtInputTable = _PrtInputTable_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 8, 2)
)
_PrtInputEntry_ObjectIdentity = ObjectIdentity
prtInputEntry = _PrtInputEntry_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1)
)
_PrtInputType_Type = PrtInputTypeTC
_PrtInputType_Object = MibScalar
prtInputType = _PrtInputType_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 2),
    _PrtInputType_Type()
)
prtInputType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInputType.setStatus("current")
_PrtInputDimUnit_Type = PrtMediaUnitTC
_PrtInputDimUnit_Object = MibScalar
prtInputDimUnit = _PrtInputDimUnit_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 3),
    _PrtInputDimUnit_Type()
)
prtInputDimUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInputDimUnit.setStatus("current")


class _PrtInputMediaDimFeedDirDeclared_Type(Integer32):
    """Custom type prtInputMediaDimFeedDirDeclared based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtInputMediaDimFeedDirDeclared_Type.__name__ = "Integer32"
_PrtInputMediaDimFeedDirDeclared_Object = MibScalar
prtInputMediaDimFeedDirDeclared = _PrtInputMediaDimFeedDirDeclared_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 4),
    _PrtInputMediaDimFeedDirDeclared_Type()
)
prtInputMediaDimFeedDirDeclared.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInputMediaDimFeedDirDeclared.setStatus("current")


class _PrtInputMediaDimXFeedDirDeclared_Type(Integer32):
    """Custom type prtInputMediaDimXFeedDirDeclared based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtInputMediaDimXFeedDirDeclared_Type.__name__ = "Integer32"
_PrtInputMediaDimXFeedDirDeclared_Object = MibScalar
prtInputMediaDimXFeedDirDeclared = _PrtInputMediaDimXFeedDirDeclared_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 5),
    _PrtInputMediaDimXFeedDirDeclared_Type()
)
prtInputMediaDimXFeedDirDeclared.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInputMediaDimXFeedDirDeclared.setStatus("current")


class _PrtInputMediaDimFeedDirChosen_Type(Integer32):
    """Custom type prtInputMediaDimFeedDirChosen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtInputMediaDimFeedDirChosen_Type.__name__ = "Integer32"
_PrtInputMediaDimFeedDirChosen_Object = MibScalar
prtInputMediaDimFeedDirChosen = _PrtInputMediaDimFeedDirChosen_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 6),
    _PrtInputMediaDimFeedDirChosen_Type()
)
prtInputMediaDimFeedDirChosen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInputMediaDimFeedDirChosen.setStatus("current")


class _PrtInputMediaDimXFeedDirChosen_Type(Integer32):
    """Custom type prtInputMediaDimXFeedDirChosen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtInputMediaDimXFeedDirChosen_Type.__name__ = "Integer32"
_PrtInputMediaDimXFeedDirChosen_Object = MibScalar
prtInputMediaDimXFeedDirChosen = _PrtInputMediaDimXFeedDirChosen_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 7),
    _PrtInputMediaDimXFeedDirChosen_Type()
)
prtInputMediaDimXFeedDirChosen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInputMediaDimXFeedDirChosen.setStatus("current")
_PrtInputCapacityUnit_Type = PrtCapacityUnitTC
_PrtInputCapacityUnit_Object = MibScalar
prtInputCapacityUnit = _PrtInputCapacityUnit_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 8),
    _PrtInputCapacityUnit_Type()
)
prtInputCapacityUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInputCapacityUnit.setStatus("current")


class _PrtInputMaxCapacity_Type(Integer32):
    """Custom type prtInputMaxCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtInputMaxCapacity_Type.__name__ = "Integer32"
_PrtInputMaxCapacity_Object = MibScalar
prtInputMaxCapacity = _PrtInputMaxCapacity_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 9),
    _PrtInputMaxCapacity_Type()
)
prtInputMaxCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInputMaxCapacity.setStatus("current")


class _PrtInputCurrentLevel_Type(Integer32):
    """Custom type prtInputCurrentLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-3, 2147483647),
    )


_PrtInputCurrentLevel_Type.__name__ = "Integer32"
_PrtInputCurrentLevel_Object = MibScalar
prtInputCurrentLevel = _PrtInputCurrentLevel_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 10),
    _PrtInputCurrentLevel_Type()
)
prtInputCurrentLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInputCurrentLevel.setStatus("current")
_PrtInputStatus_Type = PrtSubUnitStatusTC
_PrtInputStatus_Object = MibScalar
prtInputStatus = _PrtInputStatus_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 11),
    _PrtInputStatus_Type()
)
prtInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInputStatus.setStatus("current")


class _PrtInputMediaName_Type(OctetString):
    """Custom type prtInputMediaName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PrtInputMediaName_Type.__name__ = "OctetString"
_PrtInputMediaName_Object = MibScalar
prtInputMediaName = _PrtInputMediaName_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 12),
    _PrtInputMediaName_Type()
)
prtInputMediaName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInputMediaName.setStatus("current")


class _PrtInputName_Type(OctetString):
    """Custom type prtInputName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PrtInputName_Type.__name__ = "OctetString"
_PrtInputName_Object = MibScalar
prtInputName = _PrtInputName_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 13),
    _PrtInputName_Type()
)
prtInputName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInputName.setStatus("current")


class _PrtInputVendorName_Type(OctetString):
    """Custom type prtInputVendorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PrtInputVendorName_Type.__name__ = "OctetString"
_PrtInputVendorName_Object = MibScalar
prtInputVendorName = _PrtInputVendorName_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 14),
    _PrtInputVendorName_Type()
)
prtInputVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInputVendorName.setStatus("current")


class _PrtInputModel_Type(OctetString):
    """Custom type prtInputModel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PrtInputModel_Type.__name__ = "OctetString"
_PrtInputModel_Object = MibScalar
prtInputModel = _PrtInputModel_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 15),
    _PrtInputModel_Type()
)
prtInputModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInputModel.setStatus("current")


class _PrtInputVersion_Type(OctetString):
    """Custom type prtInputVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PrtInputVersion_Type.__name__ = "OctetString"
_PrtInputVersion_Object = MibScalar
prtInputVersion = _PrtInputVersion_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 16),
    _PrtInputVersion_Type()
)
prtInputVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInputVersion.setStatus("current")


class _PrtInputSerialNumber_Type(OctetString):
    """Custom type prtInputSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PrtInputSerialNumber_Type.__name__ = "OctetString"
_PrtInputSerialNumber_Object = MibScalar
prtInputSerialNumber = _PrtInputSerialNumber_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 17),
    _PrtInputSerialNumber_Type()
)
prtInputSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInputSerialNumber.setStatus("current")
_PrtInputDescription_Type = PrtLocalizedDescriptionStringTC
_PrtInputDescription_Object = MibScalar
prtInputDescription = _PrtInputDescription_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 18),
    _PrtInputDescription_Type()
)
prtInputDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInputDescription.setStatus("current")
_PrtInputSecurity_Type = PresentOnOff
_PrtInputSecurity_Object = MibScalar
prtInputSecurity = _PrtInputSecurity_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 19),
    _PrtInputSecurity_Type()
)
prtInputSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInputSecurity.setStatus("current")


class _PrtInputMediaWeight_Type(Integer32):
    """Custom type prtInputMediaWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtInputMediaWeight_Type.__name__ = "Integer32"
_PrtInputMediaWeight_Object = MibScalar
prtInputMediaWeight = _PrtInputMediaWeight_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 20),
    _PrtInputMediaWeight_Type()
)
prtInputMediaWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInputMediaWeight.setStatus("current")


class _PrtInputMediaType_Type(OctetString):
    """Custom type prtInputMediaType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PrtInputMediaType_Type.__name__ = "OctetString"
_PrtInputMediaType_Object = MibScalar
prtInputMediaType = _PrtInputMediaType_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 21),
    _PrtInputMediaType_Type()
)
prtInputMediaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInputMediaType.setStatus("current")


class _PrtInputMediaColor_Type(OctetString):
    """Custom type prtInputMediaColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PrtInputMediaColor_Type.__name__ = "OctetString"
_PrtInputMediaColor_Object = MibScalar
prtInputMediaColor = _PrtInputMediaColor_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 22),
    _PrtInputMediaColor_Type()
)
prtInputMediaColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInputMediaColor.setStatus("current")


class _PrtInputMediaFormParts_Type(Integer32):
    """Custom type prtInputMediaFormParts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtInputMediaFormParts_Type.__name__ = "Integer32"
_PrtInputMediaFormParts_Object = MibScalar
prtInputMediaFormParts = _PrtInputMediaFormParts_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 23),
    _PrtInputMediaFormParts_Type()
)
prtInputMediaFormParts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInputMediaFormParts.setStatus("current")


class _PrtInputMediaLoadTimeout_Type(Integer32):
    """Custom type prtInputMediaLoadTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtInputMediaLoadTimeout_Type.__name__ = "Integer32"
_PrtInputMediaLoadTimeout_Object = MibScalar
prtInputMediaLoadTimeout = _PrtInputMediaLoadTimeout_Object(
    (1, 3, 6, 1, 2, 1, 43, 8, 2, 1, 24),
    _PrtInputMediaLoadTimeout_Type()
)
prtInputMediaLoadTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInputMediaLoadTimeout.setStatus("current")
_PrtOutput_ObjectIdentity = ObjectIdentity
prtOutput = _PrtOutput_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 9)
)
_PrtOutputTable_ObjectIdentity = ObjectIdentity
prtOutputTable = _PrtOutputTable_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 9, 2)
)
_PrtOutputEntry_ObjectIdentity = ObjectIdentity
prtOutputEntry = _PrtOutputEntry_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1)
)
_PrtOutputType_Type = PrtOutputTypeTC
_PrtOutputType_Object = MibScalar
prtOutputType = _PrtOutputType_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 2),
    _PrtOutputType_Type()
)
prtOutputType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtOutputType.setStatus("current")
_PrtOutputCapacityUnit_Type = PrtCapacityUnitTC
_PrtOutputCapacityUnit_Object = MibScalar
prtOutputCapacityUnit = _PrtOutputCapacityUnit_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 3),
    _PrtOutputCapacityUnit_Type()
)
prtOutputCapacityUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtOutputCapacityUnit.setStatus("current")


class _PrtOutputMaxCapacity_Type(Integer32):
    """Custom type prtOutputMaxCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtOutputMaxCapacity_Type.__name__ = "Integer32"
_PrtOutputMaxCapacity_Object = MibScalar
prtOutputMaxCapacity = _PrtOutputMaxCapacity_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 4),
    _PrtOutputMaxCapacity_Type()
)
prtOutputMaxCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtOutputMaxCapacity.setStatus("current")


class _PrtOutputRemainingCapacity_Type(Integer32):
    """Custom type prtOutputRemainingCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-3, 2147483647),
    )


_PrtOutputRemainingCapacity_Type.__name__ = "Integer32"
_PrtOutputRemainingCapacity_Object = MibScalar
prtOutputRemainingCapacity = _PrtOutputRemainingCapacity_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 5),
    _PrtOutputRemainingCapacity_Type()
)
prtOutputRemainingCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtOutputRemainingCapacity.setStatus("current")
_PrtOutputStatus_Type = PrtSubUnitStatusTC
_PrtOutputStatus_Object = MibScalar
prtOutputStatus = _PrtOutputStatus_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 6),
    _PrtOutputStatus_Type()
)
prtOutputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtOutputStatus.setStatus("current")


class _PrtOutputName_Type(OctetString):
    """Custom type prtOutputName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PrtOutputName_Type.__name__ = "OctetString"
_PrtOutputName_Object = MibScalar
prtOutputName = _PrtOutputName_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 7),
    _PrtOutputName_Type()
)
prtOutputName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtOutputName.setStatus("current")


class _PrtOutputVendorName_Type(OctetString):
    """Custom type prtOutputVendorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PrtOutputVendorName_Type.__name__ = "OctetString"
_PrtOutputVendorName_Object = MibScalar
prtOutputVendorName = _PrtOutputVendorName_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 8),
    _PrtOutputVendorName_Type()
)
prtOutputVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtOutputVendorName.setStatus("current")


class _PrtOutputModel_Type(OctetString):
    """Custom type prtOutputModel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PrtOutputModel_Type.__name__ = "OctetString"
_PrtOutputModel_Object = MibScalar
prtOutputModel = _PrtOutputModel_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 9),
    _PrtOutputModel_Type()
)
prtOutputModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtOutputModel.setStatus("current")


class _PrtOutputVersion_Type(OctetString):
    """Custom type prtOutputVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PrtOutputVersion_Type.__name__ = "OctetString"
_PrtOutputVersion_Object = MibScalar
prtOutputVersion = _PrtOutputVersion_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 10),
    _PrtOutputVersion_Type()
)
prtOutputVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtOutputVersion.setStatus("current")


class _PrtOutputSerialNumber_Type(OctetString):
    """Custom type prtOutputSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PrtOutputSerialNumber_Type.__name__ = "OctetString"
_PrtOutputSerialNumber_Object = MibScalar
prtOutputSerialNumber = _PrtOutputSerialNumber_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 11),
    _PrtOutputSerialNumber_Type()
)
prtOutputSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtOutputSerialNumber.setStatus("current")
_PrtOutputDescription_Type = PrtLocalizedDescriptionStringTC
_PrtOutputDescription_Object = MibScalar
prtOutputDescription = _PrtOutputDescription_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 12),
    _PrtOutputDescription_Type()
)
prtOutputDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtOutputDescription.setStatus("current")
_PrtOutputSecurity_Type = PresentOnOff
_PrtOutputSecurity_Object = MibScalar
prtOutputSecurity = _PrtOutputSecurity_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 13),
    _PrtOutputSecurity_Type()
)
prtOutputSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtOutputSecurity.setStatus("current")
_PrtOutputDimUnit_Type = PrtMediaUnitTC
_PrtOutputDimUnit_Object = MibScalar
prtOutputDimUnit = _PrtOutputDimUnit_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 14),
    _PrtOutputDimUnit_Type()
)
prtOutputDimUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtOutputDimUnit.setStatus("current")


class _PrtOutputMaxDimFeedDir_Type(Integer32):
    """Custom type prtOutputMaxDimFeedDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtOutputMaxDimFeedDir_Type.__name__ = "Integer32"
_PrtOutputMaxDimFeedDir_Object = MibScalar
prtOutputMaxDimFeedDir = _PrtOutputMaxDimFeedDir_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 15),
    _PrtOutputMaxDimFeedDir_Type()
)
prtOutputMaxDimFeedDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtOutputMaxDimFeedDir.setStatus("current")


class _PrtOutputMaxDimXFeedDir_Type(Integer32):
    """Custom type prtOutputMaxDimXFeedDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtOutputMaxDimXFeedDir_Type.__name__ = "Integer32"
_PrtOutputMaxDimXFeedDir_Object = MibScalar
prtOutputMaxDimXFeedDir = _PrtOutputMaxDimXFeedDir_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 16),
    _PrtOutputMaxDimXFeedDir_Type()
)
prtOutputMaxDimXFeedDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtOutputMaxDimXFeedDir.setStatus("current")


class _PrtOutputMinDimFeedDir_Type(Integer32):
    """Custom type prtOutputMinDimFeedDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtOutputMinDimFeedDir_Type.__name__ = "Integer32"
_PrtOutputMinDimFeedDir_Object = MibScalar
prtOutputMinDimFeedDir = _PrtOutputMinDimFeedDir_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 17),
    _PrtOutputMinDimFeedDir_Type()
)
prtOutputMinDimFeedDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtOutputMinDimFeedDir.setStatus("current")


class _PrtOutputMinDimXFeedDir_Type(Integer32):
    """Custom type prtOutputMinDimXFeedDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtOutputMinDimXFeedDir_Type.__name__ = "Integer32"
_PrtOutputMinDimXFeedDir_Object = MibScalar
prtOutputMinDimXFeedDir = _PrtOutputMinDimXFeedDir_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 18),
    _PrtOutputMinDimXFeedDir_Type()
)
prtOutputMinDimXFeedDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtOutputMinDimXFeedDir.setStatus("current")
_PrtOutputStackingOrder_Type = PrtOutputStackingOrderTC
_PrtOutputStackingOrder_Object = MibScalar
prtOutputStackingOrder = _PrtOutputStackingOrder_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 19),
    _PrtOutputStackingOrder_Type()
)
prtOutputStackingOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtOutputStackingOrder.setStatus("current")
_PrtOutputPageDeliveryOrientation_Type = PrtOutputPageDeliveryOrientationTC
_PrtOutputPageDeliveryOrientation_Object = MibScalar
prtOutputPageDeliveryOrientation = _PrtOutputPageDeliveryOrientation_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 20),
    _PrtOutputPageDeliveryOrientation_Type()
)
prtOutputPageDeliveryOrientation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtOutputPageDeliveryOrientation.setStatus("current")
_PrtOutputBursting_Type = PresentOnOff
_PrtOutputBursting_Object = MibScalar
prtOutputBursting = _PrtOutputBursting_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 21),
    _PrtOutputBursting_Type()
)
prtOutputBursting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtOutputBursting.setStatus("current")
_PrtOutputDecollating_Type = PresentOnOff
_PrtOutputDecollating_Object = MibScalar
prtOutputDecollating = _PrtOutputDecollating_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 22),
    _PrtOutputDecollating_Type()
)
prtOutputDecollating.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtOutputDecollating.setStatus("current")
_PrtOutputPageCollated_Type = PresentOnOff
_PrtOutputPageCollated_Object = MibScalar
prtOutputPageCollated = _PrtOutputPageCollated_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 23),
    _PrtOutputPageCollated_Type()
)
prtOutputPageCollated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtOutputPageCollated.setStatus("current")
_PrtOutputOffsetStacking_Type = PresentOnOff
_PrtOutputOffsetStacking_Object = MibScalar
prtOutputOffsetStacking = _PrtOutputOffsetStacking_Object(
    (1, 3, 6, 1, 2, 1, 43, 9, 2, 1, 24),
    _PrtOutputOffsetStacking_Type()
)
prtOutputOffsetStacking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtOutputOffsetStacking.setStatus("current")
_PrtMarker_ObjectIdentity = ObjectIdentity
prtMarker = _PrtMarker_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 10)
)
_PrtMarkerTable_ObjectIdentity = ObjectIdentity
prtMarkerTable = _PrtMarkerTable_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 10, 2)
)
_PrtMarkerEntry_ObjectIdentity = ObjectIdentity
prtMarkerEntry = _PrtMarkerEntry_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 10, 2, 1)
)
_PrtMarkerMarkTech_Type = PrtMarkerMarkTechTC
_PrtMarkerMarkTech_Object = MibScalar
prtMarkerMarkTech = _PrtMarkerMarkTech_Object(
    (1, 3, 6, 1, 2, 1, 43, 10, 2, 1, 2),
    _PrtMarkerMarkTech_Type()
)
prtMarkerMarkTech.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerMarkTech.setStatus("current")
_PrtMarkerCounterUnit_Type = PrtMarkerCounterUnitTC
_PrtMarkerCounterUnit_Object = MibScalar
prtMarkerCounterUnit = _PrtMarkerCounterUnit_Object(
    (1, 3, 6, 1, 2, 1, 43, 10, 2, 1, 3),
    _PrtMarkerCounterUnit_Type()
)
prtMarkerCounterUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerCounterUnit.setStatus("current")
_PrtMarkerLifeCount_Type = Counter32
_PrtMarkerLifeCount_Object = MibScalar
prtMarkerLifeCount = _PrtMarkerLifeCount_Object(
    (1, 3, 6, 1, 2, 1, 43, 10, 2, 1, 4),
    _PrtMarkerLifeCount_Type()
)
prtMarkerLifeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerLifeCount.setStatus("current")
_PrtMarkerPowerOnCount_Type = Counter32
_PrtMarkerPowerOnCount_Object = MibScalar
prtMarkerPowerOnCount = _PrtMarkerPowerOnCount_Object(
    (1, 3, 6, 1, 2, 1, 43, 10, 2, 1, 5),
    _PrtMarkerPowerOnCount_Type()
)
prtMarkerPowerOnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerPowerOnCount.setStatus("current")


class _PrtMarkerProcessColorants_Type(Integer32):
    """Custom type prtMarkerProcessColorants based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PrtMarkerProcessColorants_Type.__name__ = "Integer32"
_PrtMarkerProcessColorants_Object = MibScalar
prtMarkerProcessColorants = _PrtMarkerProcessColorants_Object(
    (1, 3, 6, 1, 2, 1, 43, 10, 2, 1, 6),
    _PrtMarkerProcessColorants_Type()
)
prtMarkerProcessColorants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerProcessColorants.setStatus("current")


class _PrtMarkerSpotColorants_Type(Integer32):
    """Custom type prtMarkerSpotColorants based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PrtMarkerSpotColorants_Type.__name__ = "Integer32"
_PrtMarkerSpotColorants_Object = MibScalar
prtMarkerSpotColorants = _PrtMarkerSpotColorants_Object(
    (1, 3, 6, 1, 2, 1, 43, 10, 2, 1, 7),
    _PrtMarkerSpotColorants_Type()
)
prtMarkerSpotColorants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerSpotColorants.setStatus("current")
_PrtMarkerAddressabilityUnit_Type = PrtMarkerAddressabilityUnitTC
_PrtMarkerAddressabilityUnit_Object = MibScalar
prtMarkerAddressabilityUnit = _PrtMarkerAddressabilityUnit_Object(
    (1, 3, 6, 1, 2, 1, 43, 10, 2, 1, 8),
    _PrtMarkerAddressabilityUnit_Type()
)
prtMarkerAddressabilityUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerAddressabilityUnit.setStatus("current")


class _PrtMarkerAddressabilityFeedDir_Type(Integer32):
    """Custom type prtMarkerAddressabilityFeedDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtMarkerAddressabilityFeedDir_Type.__name__ = "Integer32"
_PrtMarkerAddressabilityFeedDir_Object = MibScalar
prtMarkerAddressabilityFeedDir = _PrtMarkerAddressabilityFeedDir_Object(
    (1, 3, 6, 1, 2, 1, 43, 10, 2, 1, 9),
    _PrtMarkerAddressabilityFeedDir_Type()
)
prtMarkerAddressabilityFeedDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerAddressabilityFeedDir.setStatus("current")


class _PrtMarkerAddressabilityXFeedDir_Type(Integer32):
    """Custom type prtMarkerAddressabilityXFeedDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtMarkerAddressabilityXFeedDir_Type.__name__ = "Integer32"
_PrtMarkerAddressabilityXFeedDir_Object = MibScalar
prtMarkerAddressabilityXFeedDir = _PrtMarkerAddressabilityXFeedDir_Object(
    (1, 3, 6, 1, 2, 1, 43, 10, 2, 1, 10),
    _PrtMarkerAddressabilityXFeedDir_Type()
)
prtMarkerAddressabilityXFeedDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerAddressabilityXFeedDir.setStatus("current")


class _PrtMarkerNorthMargin_Type(Integer32):
    """Custom type prtMarkerNorthMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtMarkerNorthMargin_Type.__name__ = "Integer32"
_PrtMarkerNorthMargin_Object = MibScalar
prtMarkerNorthMargin = _PrtMarkerNorthMargin_Object(
    (1, 3, 6, 1, 2, 1, 43, 10, 2, 1, 11),
    _PrtMarkerNorthMargin_Type()
)
prtMarkerNorthMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerNorthMargin.setStatus("current")


class _PrtMarkerSouthMargin_Type(Integer32):
    """Custom type prtMarkerSouthMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtMarkerSouthMargin_Type.__name__ = "Integer32"
_PrtMarkerSouthMargin_Object = MibScalar
prtMarkerSouthMargin = _PrtMarkerSouthMargin_Object(
    (1, 3, 6, 1, 2, 1, 43, 10, 2, 1, 12),
    _PrtMarkerSouthMargin_Type()
)
prtMarkerSouthMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerSouthMargin.setStatus("current")


class _PrtMarkerWestMargin_Type(Integer32):
    """Custom type prtMarkerWestMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtMarkerWestMargin_Type.__name__ = "Integer32"
_PrtMarkerWestMargin_Object = MibScalar
prtMarkerWestMargin = _PrtMarkerWestMargin_Object(
    (1, 3, 6, 1, 2, 1, 43, 10, 2, 1, 13),
    _PrtMarkerWestMargin_Type()
)
prtMarkerWestMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerWestMargin.setStatus("current")


class _PrtMarkerEastMargin_Type(Integer32):
    """Custom type prtMarkerEastMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtMarkerEastMargin_Type.__name__ = "Integer32"
_PrtMarkerEastMargin_Object = MibScalar
prtMarkerEastMargin = _PrtMarkerEastMargin_Object(
    (1, 3, 6, 1, 2, 1, 43, 10, 2, 1, 14),
    _PrtMarkerEastMargin_Type()
)
prtMarkerEastMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerEastMargin.setStatus("current")
_PrtMarkerStatus_Type = PrtSubUnitStatusTC
_PrtMarkerStatus_Object = MibScalar
prtMarkerStatus = _PrtMarkerStatus_Object(
    (1, 3, 6, 1, 2, 1, 43, 10, 2, 1, 15),
    _PrtMarkerStatus_Type()
)
prtMarkerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerStatus.setStatus("current")
_PrtMarkerSupplies_ObjectIdentity = ObjectIdentity
prtMarkerSupplies = _PrtMarkerSupplies_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 11)
)
_PrtMarkerSuppliesTable_ObjectIdentity = ObjectIdentity
prtMarkerSuppliesTable = _PrtMarkerSuppliesTable_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 11, 1)
)
_PrtMarkerSuppliesEntry_ObjectIdentity = ObjectIdentity
prtMarkerSuppliesEntry = _PrtMarkerSuppliesEntry_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 11, 1, 1)
)


class _PrtMarkerSuppliesMarkerIndex_Type(Integer32):
    """Custom type prtMarkerSuppliesMarkerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PrtMarkerSuppliesMarkerIndex_Type.__name__ = "Integer32"
_PrtMarkerSuppliesMarkerIndex_Object = MibScalar
prtMarkerSuppliesMarkerIndex = _PrtMarkerSuppliesMarkerIndex_Object(
    (1, 3, 6, 1, 2, 1, 43, 11, 1, 1, 2),
    _PrtMarkerSuppliesMarkerIndex_Type()
)
prtMarkerSuppliesMarkerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerSuppliesMarkerIndex.setStatus("current")


class _PrtMarkerSuppliesColorantIndex_Type(Integer32):
    """Custom type prtMarkerSuppliesColorantIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PrtMarkerSuppliesColorantIndex_Type.__name__ = "Integer32"
_PrtMarkerSuppliesColorantIndex_Object = MibScalar
prtMarkerSuppliesColorantIndex = _PrtMarkerSuppliesColorantIndex_Object(
    (1, 3, 6, 1, 2, 1, 43, 11, 1, 1, 3),
    _PrtMarkerSuppliesColorantIndex_Type()
)
prtMarkerSuppliesColorantIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerSuppliesColorantIndex.setStatus("current")
_PrtMarkerSuppliesClass_Type = PrtMarkerSuppliesClassTC
_PrtMarkerSuppliesClass_Object = MibScalar
prtMarkerSuppliesClass = _PrtMarkerSuppliesClass_Object(
    (1, 3, 6, 1, 2, 1, 43, 11, 1, 1, 4),
    _PrtMarkerSuppliesClass_Type()
)
prtMarkerSuppliesClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerSuppliesClass.setStatus("current")
_PrtMarkerSuppliesType_Type = PrtMarkerSuppliesTypeTC
_PrtMarkerSuppliesType_Object = MibScalar
prtMarkerSuppliesType = _PrtMarkerSuppliesType_Object(
    (1, 3, 6, 1, 2, 1, 43, 11, 1, 1, 5),
    _PrtMarkerSuppliesType_Type()
)
prtMarkerSuppliesType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerSuppliesType.setStatus("current")
_PrtMarkerSuppliesDescription_Type = PrtLocalizedDescriptionStringTC
_PrtMarkerSuppliesDescription_Object = MibScalar
prtMarkerSuppliesDescription = _PrtMarkerSuppliesDescription_Object(
    (1, 3, 6, 1, 2, 1, 43, 11, 1, 1, 6),
    _PrtMarkerSuppliesDescription_Type()
)
prtMarkerSuppliesDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerSuppliesDescription.setStatus("current")
_PrtMarkerSuppliesSupplyUnit_Type = PrtMarkerSuppliesSupplyUnitTC
_PrtMarkerSuppliesSupplyUnit_Object = MibScalar
prtMarkerSuppliesSupplyUnit = _PrtMarkerSuppliesSupplyUnit_Object(
    (1, 3, 6, 1, 2, 1, 43, 11, 1, 1, 7),
    _PrtMarkerSuppliesSupplyUnit_Type()
)
prtMarkerSuppliesSupplyUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerSuppliesSupplyUnit.setStatus("current")


class _PrtMarkerSuppliesMaxCapacity_Type(Integer32):
    """Custom type prtMarkerSuppliesMaxCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtMarkerSuppliesMaxCapacity_Type.__name__ = "Integer32"
_PrtMarkerSuppliesMaxCapacity_Object = MibScalar
prtMarkerSuppliesMaxCapacity = _PrtMarkerSuppliesMaxCapacity_Object(
    (1, 3, 6, 1, 2, 1, 43, 11, 1, 1, 8),
    _PrtMarkerSuppliesMaxCapacity_Type()
)
prtMarkerSuppliesMaxCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtMarkerSuppliesMaxCapacity.setStatus("current")


class _PrtMarkerSuppliesLevel_Type(Integer32):
    """Custom type prtMarkerSuppliesLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-3, 2147483647),
    )


_PrtMarkerSuppliesLevel_Type.__name__ = "Integer32"
_PrtMarkerSuppliesLevel_Object = MibScalar
prtMarkerSuppliesLevel = _PrtMarkerSuppliesLevel_Object(
    (1, 3, 6, 1, 2, 1, 43, 11, 1, 1, 9),
    _PrtMarkerSuppliesLevel_Type()
)
prtMarkerSuppliesLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtMarkerSuppliesLevel.setStatus("current")
_PrtMarkerColorant_ObjectIdentity = ObjectIdentity
prtMarkerColorant = _PrtMarkerColorant_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 12)
)
_PrtMarkerColorantTable_ObjectIdentity = ObjectIdentity
prtMarkerColorantTable = _PrtMarkerColorantTable_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 12, 1)
)
_PrtMarkerColorantEntry_ObjectIdentity = ObjectIdentity
prtMarkerColorantEntry = _PrtMarkerColorantEntry_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 12, 1, 1)
)


class _PrtMarkerColorantMarkerIndex_Type(Integer32):
    """Custom type prtMarkerColorantMarkerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PrtMarkerColorantMarkerIndex_Type.__name__ = "Integer32"
_PrtMarkerColorantMarkerIndex_Object = MibScalar
prtMarkerColorantMarkerIndex = _PrtMarkerColorantMarkerIndex_Object(
    (1, 3, 6, 1, 2, 1, 43, 12, 1, 1, 2),
    _PrtMarkerColorantMarkerIndex_Type()
)
prtMarkerColorantMarkerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerColorantMarkerIndex.setStatus("current")
_PrtMarkerColorantRole_Type = PrtMarkerColorantRoleTC
_PrtMarkerColorantRole_Object = MibScalar
prtMarkerColorantRole = _PrtMarkerColorantRole_Object(
    (1, 3, 6, 1, 2, 1, 43, 12, 1, 1, 3),
    _PrtMarkerColorantRole_Type()
)
prtMarkerColorantRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerColorantRole.setStatus("current")


class _PrtMarkerColorantValue_Type(OctetString):
    """Custom type prtMarkerColorantValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PrtMarkerColorantValue_Type.__name__ = "OctetString"
_PrtMarkerColorantValue_Object = MibScalar
prtMarkerColorantValue = _PrtMarkerColorantValue_Object(
    (1, 3, 6, 1, 2, 1, 43, 12, 1, 1, 4),
    _PrtMarkerColorantValue_Type()
)
prtMarkerColorantValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerColorantValue.setStatus("current")


class _PrtMarkerColorantTonality_Type(Integer32):
    """Custom type prtMarkerColorantTonality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2147483647),
    )


_PrtMarkerColorantTonality_Type.__name__ = "Integer32"
_PrtMarkerColorantTonality_Object = MibScalar
prtMarkerColorantTonality = _PrtMarkerColorantTonality_Object(
    (1, 3, 6, 1, 2, 1, 43, 12, 1, 1, 5),
    _PrtMarkerColorantTonality_Type()
)
prtMarkerColorantTonality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMarkerColorantTonality.setStatus("current")
_PrtMediaPath_ObjectIdentity = ObjectIdentity
prtMediaPath = _PrtMediaPath_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 13)
)
_PrtMediaPathTable_ObjectIdentity = ObjectIdentity
prtMediaPathTable = _PrtMediaPathTable_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 13, 4)
)
_PrtMediaPathEntry_ObjectIdentity = ObjectIdentity
prtMediaPathEntry = _PrtMediaPathEntry_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 13, 4, 1)
)
_PrtMediaPathMaxSpeedPrintUnit_Type = PrtMediaPathMaxSpeedPrintUnitTC
_PrtMediaPathMaxSpeedPrintUnit_Object = MibScalar
prtMediaPathMaxSpeedPrintUnit = _PrtMediaPathMaxSpeedPrintUnit_Object(
    (1, 3, 6, 1, 2, 1, 43, 13, 4, 1, 2),
    _PrtMediaPathMaxSpeedPrintUnit_Type()
)
prtMediaPathMaxSpeedPrintUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMediaPathMaxSpeedPrintUnit.setStatus("current")
_PrtMediaPathMediaSizeUnit_Type = PrtMediaUnitTC
_PrtMediaPathMediaSizeUnit_Object = MibScalar
prtMediaPathMediaSizeUnit = _PrtMediaPathMediaSizeUnit_Object(
    (1, 3, 6, 1, 2, 1, 43, 13, 4, 1, 3),
    _PrtMediaPathMediaSizeUnit_Type()
)
prtMediaPathMediaSizeUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMediaPathMediaSizeUnit.setStatus("current")


class _PrtMediaPathMaxSpeed_Type(Integer32):
    """Custom type prtMediaPathMaxSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtMediaPathMaxSpeed_Type.__name__ = "Integer32"
_PrtMediaPathMaxSpeed_Object = MibScalar
prtMediaPathMaxSpeed = _PrtMediaPathMaxSpeed_Object(
    (1, 3, 6, 1, 2, 1, 43, 13, 4, 1, 4),
    _PrtMediaPathMaxSpeed_Type()
)
prtMediaPathMaxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMediaPathMaxSpeed.setStatus("current")


class _PrtMediaPathMaxMediaFeedDir_Type(Integer32):
    """Custom type prtMediaPathMaxMediaFeedDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtMediaPathMaxMediaFeedDir_Type.__name__ = "Integer32"
_PrtMediaPathMaxMediaFeedDir_Object = MibScalar
prtMediaPathMaxMediaFeedDir = _PrtMediaPathMaxMediaFeedDir_Object(
    (1, 3, 6, 1, 2, 1, 43, 13, 4, 1, 5),
    _PrtMediaPathMaxMediaFeedDir_Type()
)
prtMediaPathMaxMediaFeedDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMediaPathMaxMediaFeedDir.setStatus("current")


class _PrtMediaPathMaxMediaXFeedDir_Type(Integer32):
    """Custom type prtMediaPathMaxMediaXFeedDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtMediaPathMaxMediaXFeedDir_Type.__name__ = "Integer32"
_PrtMediaPathMaxMediaXFeedDir_Object = MibScalar
prtMediaPathMaxMediaXFeedDir = _PrtMediaPathMaxMediaXFeedDir_Object(
    (1, 3, 6, 1, 2, 1, 43, 13, 4, 1, 6),
    _PrtMediaPathMaxMediaXFeedDir_Type()
)
prtMediaPathMaxMediaXFeedDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMediaPathMaxMediaXFeedDir.setStatus("current")


class _PrtMediaPathMinMediaFeedDir_Type(Integer32):
    """Custom type prtMediaPathMinMediaFeedDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtMediaPathMinMediaFeedDir_Type.__name__ = "Integer32"
_PrtMediaPathMinMediaFeedDir_Object = MibScalar
prtMediaPathMinMediaFeedDir = _PrtMediaPathMinMediaFeedDir_Object(
    (1, 3, 6, 1, 2, 1, 43, 13, 4, 1, 7),
    _PrtMediaPathMinMediaFeedDir_Type()
)
prtMediaPathMinMediaFeedDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMediaPathMinMediaFeedDir.setStatus("current")


class _PrtMediaPathMinMediaXFeedDir_Type(Integer32):
    """Custom type prtMediaPathMinMediaXFeedDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtMediaPathMinMediaXFeedDir_Type.__name__ = "Integer32"
_PrtMediaPathMinMediaXFeedDir_Object = MibScalar
prtMediaPathMinMediaXFeedDir = _PrtMediaPathMinMediaXFeedDir_Object(
    (1, 3, 6, 1, 2, 1, 43, 13, 4, 1, 8),
    _PrtMediaPathMinMediaXFeedDir_Type()
)
prtMediaPathMinMediaXFeedDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMediaPathMinMediaXFeedDir.setStatus("current")
_PrtMediaPathType_Type = PrtMediaPathTypeTC
_PrtMediaPathType_Object = MibScalar
prtMediaPathType = _PrtMediaPathType_Object(
    (1, 3, 6, 1, 2, 1, 43, 13, 4, 1, 9),
    _PrtMediaPathType_Type()
)
prtMediaPathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMediaPathType.setStatus("current")
_PrtMediaPathDescription_Type = PrtLocalizedDescriptionStringTC
_PrtMediaPathDescription_Object = MibScalar
prtMediaPathDescription = _PrtMediaPathDescription_Object(
    (1, 3, 6, 1, 2, 1, 43, 13, 4, 1, 10),
    _PrtMediaPathDescription_Type()
)
prtMediaPathDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMediaPathDescription.setStatus("current")
_PrtMediaPathStatus_Type = PrtSubUnitStatusTC
_PrtMediaPathStatus_Object = MibScalar
prtMediaPathStatus = _PrtMediaPathStatus_Object(
    (1, 3, 6, 1, 2, 1, 43, 13, 4, 1, 11),
    _PrtMediaPathStatus_Type()
)
prtMediaPathStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMediaPathStatus.setStatus("current")
_PrtChannel_ObjectIdentity = ObjectIdentity
prtChannel = _PrtChannel_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 14)
)
_PrtChannelTable_ObjectIdentity = ObjectIdentity
prtChannelTable = _PrtChannelTable_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 14, 1)
)
_PrtChannelEntry_ObjectIdentity = ObjectIdentity
prtChannelEntry = _PrtChannelEntry_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 14, 1, 1)
)
_PrtChannelType_Type = PrtChannelTypeTC
_PrtChannelType_Object = MibScalar
prtChannelType = _PrtChannelType_Object(
    (1, 3, 6, 1, 2, 1, 43, 14, 1, 1, 2),
    _PrtChannelType_Type()
)
prtChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtChannelType.setStatus("current")


class _PrtChannelProtocolVersion_Type(OctetString):
    """Custom type prtChannelProtocolVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PrtChannelProtocolVersion_Type.__name__ = "OctetString"
_PrtChannelProtocolVersion_Object = MibScalar
prtChannelProtocolVersion = _PrtChannelProtocolVersion_Object(
    (1, 3, 6, 1, 2, 1, 43, 14, 1, 1, 3),
    _PrtChannelProtocolVersion_Type()
)
prtChannelProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtChannelProtocolVersion.setStatus("current")


class _PrtChannelCurrentJobCntlLangIndex_Type(Integer32):
    """Custom type prtChannelCurrentJobCntlLangIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PrtChannelCurrentJobCntlLangIndex_Type.__name__ = "Integer32"
_PrtChannelCurrentJobCntlLangIndex_Object = MibScalar
prtChannelCurrentJobCntlLangIndex = _PrtChannelCurrentJobCntlLangIndex_Object(
    (1, 3, 6, 1, 2, 1, 43, 14, 1, 1, 4),
    _PrtChannelCurrentJobCntlLangIndex_Type()
)
prtChannelCurrentJobCntlLangIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtChannelCurrentJobCntlLangIndex.setStatus("current")


class _PrtChannelDefaultPageDescLangIndex_Type(Integer32):
    """Custom type prtChannelDefaultPageDescLangIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PrtChannelDefaultPageDescLangIndex_Type.__name__ = "Integer32"
_PrtChannelDefaultPageDescLangIndex_Object = MibScalar
prtChannelDefaultPageDescLangIndex = _PrtChannelDefaultPageDescLangIndex_Object(
    (1, 3, 6, 1, 2, 1, 43, 14, 1, 1, 5),
    _PrtChannelDefaultPageDescLangIndex_Type()
)
prtChannelDefaultPageDescLangIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtChannelDefaultPageDescLangIndex.setStatus("current")
_PrtChannelState_Type = PrtChannelStateTC
_PrtChannelState_Object = MibScalar
prtChannelState = _PrtChannelState_Object(
    (1, 3, 6, 1, 2, 1, 43, 14, 1, 1, 6),
    _PrtChannelState_Type()
)
prtChannelState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtChannelState.setStatus("current")
_PrtChannelIfIndex_Type = InterfaceIndexOrZero
_PrtChannelIfIndex_Object = MibScalar
prtChannelIfIndex = _PrtChannelIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 43, 14, 1, 1, 7),
    _PrtChannelIfIndex_Type()
)
prtChannelIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtChannelIfIndex.setStatus("current")
_PrtChannelStatus_Type = PrtSubUnitStatusTC
_PrtChannelStatus_Object = MibScalar
prtChannelStatus = _PrtChannelStatus_Object(
    (1, 3, 6, 1, 2, 1, 43, 14, 1, 1, 8),
    _PrtChannelStatus_Type()
)
prtChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtChannelStatus.setStatus("current")


class _PrtChannelInformation_Type(OctetString):
    """Custom type prtChannelInformation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PrtChannelInformation_Type.__name__ = "OctetString"
_PrtChannelInformation_Object = MibScalar
prtChannelInformation = _PrtChannelInformation_Object(
    (1, 3, 6, 1, 2, 1, 43, 14, 1, 1, 9),
    _PrtChannelInformation_Type()
)
prtChannelInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtChannelInformation.setStatus("current")
_PrtInterpreter_ObjectIdentity = ObjectIdentity
prtInterpreter = _PrtInterpreter_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 15)
)
_PrtInterpreterTable_ObjectIdentity = ObjectIdentity
prtInterpreterTable = _PrtInterpreterTable_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 15, 1)
)
_PrtInterpreterEntry_ObjectIdentity = ObjectIdentity
prtInterpreterEntry = _PrtInterpreterEntry_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 15, 1, 1)
)
_PrtInterpreterLangFamily_Type = PrtInterpreterLangFamilyTC
_PrtInterpreterLangFamily_Object = MibScalar
prtInterpreterLangFamily = _PrtInterpreterLangFamily_Object(
    (1, 3, 6, 1, 2, 1, 43, 15, 1, 1, 2),
    _PrtInterpreterLangFamily_Type()
)
prtInterpreterLangFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInterpreterLangFamily.setStatus("current")


class _PrtInterpreterLangLevel_Type(OctetString):
    """Custom type prtInterpreterLangLevel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PrtInterpreterLangLevel_Type.__name__ = "OctetString"
_PrtInterpreterLangLevel_Object = MibScalar
prtInterpreterLangLevel = _PrtInterpreterLangLevel_Object(
    (1, 3, 6, 1, 2, 1, 43, 15, 1, 1, 3),
    _PrtInterpreterLangLevel_Type()
)
prtInterpreterLangLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInterpreterLangLevel.setStatus("current")


class _PrtInterpreterLangVersion_Type(OctetString):
    """Custom type prtInterpreterLangVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PrtInterpreterLangVersion_Type.__name__ = "OctetString"
_PrtInterpreterLangVersion_Object = MibScalar
prtInterpreterLangVersion = _PrtInterpreterLangVersion_Object(
    (1, 3, 6, 1, 2, 1, 43, 15, 1, 1, 4),
    _PrtInterpreterLangVersion_Type()
)
prtInterpreterLangVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInterpreterLangVersion.setStatus("current")
_PrtInterpreterDescription_Type = PrtLocalizedDescriptionStringTC
_PrtInterpreterDescription_Object = MibScalar
prtInterpreterDescription = _PrtInterpreterDescription_Object(
    (1, 3, 6, 1, 2, 1, 43, 15, 1, 1, 5),
    _PrtInterpreterDescription_Type()
)
prtInterpreterDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInterpreterDescription.setStatus("current")


class _PrtInterpreterVersion_Type(OctetString):
    """Custom type prtInterpreterVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PrtInterpreterVersion_Type.__name__ = "OctetString"
_PrtInterpreterVersion_Object = MibScalar
prtInterpreterVersion = _PrtInterpreterVersion_Object(
    (1, 3, 6, 1, 2, 1, 43, 15, 1, 1, 6),
    _PrtInterpreterVersion_Type()
)
prtInterpreterVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInterpreterVersion.setStatus("current")
_PrtInterpreterDefaultOrientation_Type = PrtPrintOrientationTC
_PrtInterpreterDefaultOrientation_Object = MibScalar
prtInterpreterDefaultOrientation = _PrtInterpreterDefaultOrientation_Object(
    (1, 3, 6, 1, 2, 1, 43, 15, 1, 1, 7),
    _PrtInterpreterDefaultOrientation_Type()
)
prtInterpreterDefaultOrientation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInterpreterDefaultOrientation.setStatus("current")


class _PrtInterpreterFeedAddressability_Type(Integer32):
    """Custom type prtInterpreterFeedAddressability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtInterpreterFeedAddressability_Type.__name__ = "Integer32"
_PrtInterpreterFeedAddressability_Object = MibScalar
prtInterpreterFeedAddressability = _PrtInterpreterFeedAddressability_Object(
    (1, 3, 6, 1, 2, 1, 43, 15, 1, 1, 8),
    _PrtInterpreterFeedAddressability_Type()
)
prtInterpreterFeedAddressability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInterpreterFeedAddressability.setStatus("current")


class _PrtInterpreterXFeedAddressability_Type(Integer32):
    """Custom type prtInterpreterXFeedAddressability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PrtInterpreterXFeedAddressability_Type.__name__ = "Integer32"
_PrtInterpreterXFeedAddressability_Object = MibScalar
prtInterpreterXFeedAddressability = _PrtInterpreterXFeedAddressability_Object(
    (1, 3, 6, 1, 2, 1, 43, 15, 1, 1, 9),
    _PrtInterpreterXFeedAddressability_Type()
)
prtInterpreterXFeedAddressability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInterpreterXFeedAddressability.setStatus("current")
_PrtInterpreterDefaultCharSetIn_Type = IANACharset
_PrtInterpreterDefaultCharSetIn_Object = MibScalar
prtInterpreterDefaultCharSetIn = _PrtInterpreterDefaultCharSetIn_Object(
    (1, 3, 6, 1, 2, 1, 43, 15, 1, 1, 10),
    _PrtInterpreterDefaultCharSetIn_Type()
)
prtInterpreterDefaultCharSetIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInterpreterDefaultCharSetIn.setStatus("current")
_PrtInterpreterDefaultCharSetOut_Type = IANACharset
_PrtInterpreterDefaultCharSetOut_Object = MibScalar
prtInterpreterDefaultCharSetOut = _PrtInterpreterDefaultCharSetOut_Object(
    (1, 3, 6, 1, 2, 1, 43, 15, 1, 1, 11),
    _PrtInterpreterDefaultCharSetOut_Type()
)
prtInterpreterDefaultCharSetOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInterpreterDefaultCharSetOut.setStatus("current")
_PrtInterpreterTwoWay_Type = PrtInterpreterTwoWayTC
_PrtInterpreterTwoWay_Object = MibScalar
prtInterpreterTwoWay = _PrtInterpreterTwoWay_Object(
    (1, 3, 6, 1, 2, 1, 43, 15, 1, 1, 12),
    _PrtInterpreterTwoWay_Type()
)
prtInterpreterTwoWay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInterpreterTwoWay.setStatus("current")
_PrtConsoleDisplayBuffer_ObjectIdentity = ObjectIdentity
prtConsoleDisplayBuffer = _PrtConsoleDisplayBuffer_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 16)
)
_PrtConsoleDisplayBufferTable_ObjectIdentity = ObjectIdentity
prtConsoleDisplayBufferTable = _PrtConsoleDisplayBufferTable_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 16, 5)
)
_PrtConsoleDisplayBufferEntry_ObjectIdentity = ObjectIdentity
prtConsoleDisplayBufferEntry = _PrtConsoleDisplayBufferEntry_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 43, 16, 5, 1)
)
_PrtConsoleDisplayBufferText_Type = PrtConsoleDescriptionStringTC
_PrtConsoleDisplayBufferText_Object = MibScalar
prtConsoleDisplayBufferText = _PrtConsoleDisplayBufferText_Object(
    (1, 3, 6, 1, 2, 1, 43, 16, 5, 1, 2),
    _PrtConsoleDisplayBufferText_Type()
)
prtConsoleDisplayBufferText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtConsoleDisplayBufferText.setStatus("current")
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_HpPrintServer_ObjectIdentity = ObjectIdentity
hpPrintServer = _HpPrintServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_Nm_system_ObjectIdentity = ObjectIdentity
nm_system = _Nm_system_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3)
)
_NetPeripheral_ObjectIdentity = ObjectIdentity
netPeripheral = _NetPeripheral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9)
)
_NetPrinter_ObjectIdentity = ObjectIdentity
netPrinter = _NetPrinter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1)
)
_GeneralDeviceStatus_ObjectIdentity = ObjectIdentity
generalDeviceStatus = _GeneralDeviceStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1)
)
_GdStatusEntry_ObjectIdentity = ObjectIdentity
gdStatusEntry = _GdStatusEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 2)
)


class _GdStatusLineState_Type(Integer32):
    """Custom type gdStatusLineState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GdStatusLineState_Type.__name__ = "Integer32"
_GdStatusLineState_Object = MibScalar
gdStatusLineState = _GdStatusLineState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 2, 1),
    _GdStatusLineState_Type()
)
gdStatusLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdStatusLineState.setStatus("current")
_GdStatusPaperOut_Type = Integer32
_GdStatusPaperOut_Object = MibScalar
gdStatusPaperOut = _GdStatusPaperOut_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 2, 8),
    _GdStatusPaperOut_Type()
)
gdStatusPaperOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdStatusPaperOut.setStatus("current")
_GdStatusPaperJam_Type = Integer32
_GdStatusPaperJam_Object = MibScalar
gdStatusPaperJam = _GdStatusPaperJam_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 2, 9),
    _GdStatusPaperJam_Type()
)
gdStatusPaperJam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdStatusPaperJam.setStatus("current")


class _GdStatusBusy_Type(Integer32):
    """Custom type gdStatusBusy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GdStatusBusy_Type.__name__ = "Integer32"
_GdStatusBusy_Object = MibScalar
gdStatusBusy = _GdStatusBusy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 2, 14),
    _GdStatusBusy_Type()
)
gdStatusBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdStatusBusy.setStatus("current")


class _GdStatusWait_Type(Integer32):
    """Custom type gdStatusWait based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GdStatusWait_Type.__name__ = "Integer32"
_GdStatusWait_Object = MibScalar
gdStatusWait = _GdStatusWait_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 2, 15),
    _GdStatusWait_Type()
)
gdStatusWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdStatusWait.setStatus("current")
_GdStatusInitialize_Type = Integer32
_GdStatusInitialize_Object = MibScalar
gdStatusInitialize = _GdStatusInitialize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 2, 16),
    _GdStatusInitialize_Type()
)
gdStatusInitialize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdStatusInitialize.setStatus("current")


class _GdStatusDoorOpen_Type(Integer32):
    """Custom type gdStatusDoorOpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GdStatusDoorOpen_Type.__name__ = "Integer32"
_GdStatusDoorOpen_Object = MibScalar
gdStatusDoorOpen = _GdStatusDoorOpen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 2, 17),
    _GdStatusDoorOpen_Type()
)
gdStatusDoorOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdStatusDoorOpen.setStatus("current")
_GdStatusPrinting_Type = Integer32
_GdStatusPrinting_Object = MibScalar
gdStatusPrinting = _GdStatusPrinting_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 2, 18),
    _GdStatusPrinting_Type()
)
gdStatusPrinting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdStatusPrinting.setStatus("current")
_GdStatusPaperOutput_Type = Integer32
_GdStatusPaperOutput_Object = MibScalar
gdStatusPaperOutput = _GdStatusPaperOutput_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 2, 19),
    _GdStatusPaperOutput_Type()
)
gdStatusPaperOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdStatusPaperOutput.setStatus("current")
_GdStatusDisplay_Type = DisplayString
_GdStatusDisplay_Object = MibScalar
gdStatusDisplay = _GdStatusDisplay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 3),
    _GdStatusDisplay_Type()
)
gdStatusDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdStatusDisplay.setStatus("current")


class _GdStatusId_Type(OctetString):
    """Custom type gdStatusId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_GdStatusId_Type.__name__ = "OctetString"
_GdStatusId_Object = MibScalar
gdStatusId = _GdStatusId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 7),
    _GdStatusId_Type()
)
gdStatusId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdStatusId.setStatus("current")
_GdStatusJobTimeout_Type = Integer32
_GdStatusJobTimeout_Object = MibScalar
gdStatusJobTimeout = _GdStatusJobTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 10),
    _GdStatusJobTimeout_Type()
)
gdStatusJobTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdStatusJobTimeout.setStatus("obsolete")


class _GdPasswords_Type(OctetString):
    """Custom type gdPasswords based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GdPasswords_Type.__name__ = "OctetString"
_GdPasswords_Object = MibScalar
gdPasswords = _GdPasswords_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 13),
    _GdPasswords_Type()
)
gdPasswords.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdPasswords.setStatus("current")
_NetPML_ObjectIdentity = ObjectIdentity
netPML = _NetPML_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4)
)
_NetPMLmgmt_ObjectIdentity = ObjectIdentity
netPMLmgmt = _NetPMLmgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2)
)
_Device_ObjectIdentity = ObjectIdentity
device = _Device_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1)
)
_Device_system_ObjectIdentity = ObjectIdentity
device_system = _Device_system_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1)
)
_Settings_system_ObjectIdentity = ObjectIdentity
settings_system = _Settings_system_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1)
)
_Energy_star_Type = Integer32
_Energy_star_Object = MibScalar
energy_star = _Energy_star_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 1),
    _Energy_star_Type()
)
energy_star.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    energy_star.setStatus("optional")


class _Sleep_mode_Type(Integer32):
    """Custom type sleep_mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eFalse", 1),
          ("eTrue", 2))
    )


_Sleep_mode_Type.__name__ = "Integer32"
_Sleep_mode_Object = MibScalar
sleep_mode = _Sleep_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 2),
    _Sleep_mode_Type()
)
sleep_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleep_mode.setStatus("optional")


class _Speed_energy_usage_Type(Integer32):
    """Custom type speed_energy_usage based on Integer32"""
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
        *(("eFasterFirstPage", 1),
          ("eSaveEnergy", 2),
          ("eSaveMostEnergy", 3),
          ("eSaveMoreEnergy", 4))
    )


_Speed_energy_usage_Type.__name__ = "Integer32"
_Speed_energy_usage_Object = MibScalar
speed_energy_usage = _Speed_energy_usage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 50),
    _Speed_energy_usage_Type()
)
speed_energy_usage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speed_energy_usage.setStatus("optional")


class _Start_engine_early_warmup_Type(Integer32):
    """Custom type start_engine_early_warmup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("eValue1", 1)
    )


_Start_engine_early_warmup_Type.__name__ = "Integer32"
_Start_engine_early_warmup_Object = MibScalar
start_engine_early_warmup = _Start_engine_early_warmup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 99),
    _Start_engine_early_warmup_Type()
)
start_engine_early_warmup.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    start_engine_early_warmup.setStatus("mandatory")


class _Enable_engine_early_warmup_Type(Integer32):
    """Custom type enable_engine_early_warmup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eDisable", 1),
          ("eEnable", 2))
    )


_Enable_engine_early_warmup_Type.__name__ = "Integer32"
_Enable_engine_early_warmup_Object = MibScalar
enable_engine_early_warmup = _Enable_engine_early_warmup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 101),
    _Enable_engine_early_warmup_Type()
)
enable_engine_early_warmup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enable_engine_early_warmup.setStatus("optional")
_Status_system_ObjectIdentity = ObjectIdentity
status_system = _Status_system_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2)
)


class _Install_date_Type(DisplayString):
    """Custom type install_date based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )
    fixed_length = 13


_Install_date_Type.__name__ = "DisplayString"
_Install_date_Object = MibScalar
install_date = _Install_date_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 8),
    _Install_date_Type()
)
install_date.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    install_date.setStatus("optional")
_Date_and_time_Type = OctetString
_Date_and_time_Object = MibScalar
date_and_time = _Date_and_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 17),
    _Date_and_time_Type()
)
date_and_time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    date_and_time.setStatus("optional")
_Id_ObjectIdentity = ObjectIdentity
id = _Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 3)
)
_Model_number_Type = DisplayString
_Model_number_Object = MibScalar
model_number = _Model_number_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 3, 1),
    _Model_number_Type()
)
model_number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    model_number.setStatus("optional")


class _Model_name_Type(DisplayString):
    """Custom type model_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Model_name_Type.__name__ = "DisplayString"
_Model_name_Object = MibScalar
model_name = _Model_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 3, 2),
    _Model_name_Type()
)
model_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    model_name.setStatus("optional")


class _Serial_number_Type(DisplayString):
    """Custom type serial_number based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Serial_number_Type.__name__ = "DisplayString"
_Serial_number_Object = MibScalar
serial_number = _Serial_number_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 3, 3),
    _Serial_number_Type()
)
serial_number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serial_number.setStatus("optional")
_Fw_rom_datecode_Type = DisplayString
_Fw_rom_datecode_Object = MibScalar
fw_rom_datecode = _Fw_rom_datecode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 3, 5),
    _Fw_rom_datecode_Type()
)
fw_rom_datecode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fw_rom_datecode.setStatus("optional")
_Fw_rom_revision_Type = DisplayString
_Fw_rom_revision_Object = MibScalar
fw_rom_revision = _Fw_rom_revision_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 3, 6),
    _Fw_rom_revision_Type()
)
fw_rom_revision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fw_rom_revision.setStatus("optional")


class _Device_name_Type(DisplayString):
    """Custom type device_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Device_name_Type.__name__ = "DisplayString"
_Device_name_Object = MibScalar
device_name = _Device_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 3, 10),
    _Device_name_Type()
)
device_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    device_name.setStatus("optional")
_Device_location_Type = DisplayString
_Device_location_Object = MibScalar
device_location = _Device_location_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 3, 11),
    _Device_location_Type()
)
device_location.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    device_location.setStatus("optional")
_Asset_number_Type = DisplayString
_Asset_number_Object = MibScalar
asset_number = _Asset_number_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 3, 12),
    _Asset_number_Type()
)
asset_number.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asset_number.setStatus("optional")
_Test_ObjectIdentity = ObjectIdentity
test = _Test_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 5)
)


class _Print_internal_page_Type(Integer32):
    """Custom type print_internal_page based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              7,
              8,
              9,
              100,
              101,
              254,
              255,
              256,
              350,
              450)
        )
    )
    namedValues = NamedValues(
        *(("eNotPrintingAnInternalPage", 1),
          ("ePrintingAnUnknownInternalPage", 2),
          ("eDeviceDemoPage1ConfigurationPage", 3),
          ("eDeviceDemoPage2", 4),
          ("eDeviceDemoPage5ErrorLog", 7),
          ("eDeviceDemoPage6FileSystemDirectoryListing", 8),
          ("eDeviceDemoPage7MenuMap", 9),
          ("ePrintUsagePage", 100),
          ("eSuppliesPage", 101),
          ("eDevicePaperPathTest", 254),
          ("eDevicePageRegistrationPage", 255),
          ("ePrintQualityPages", 256),
          ("ePCLFontList1", 350),
          ("ePSFontList", 450))
    )


_Print_internal_page_Type.__name__ = "Integer32"
_Print_internal_page_Object = MibScalar
print_internal_page = _Print_internal_page_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 5, 2),
    _Print_internal_page_Type()
)
print_internal_page.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    print_internal_page.setStatus("optional")
_Job_ObjectIdentity = ObjectIdentity
job = _Job_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6)
)
_Settings_job_ObjectIdentity = ObjectIdentity
settings_job = _Settings_job_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 1)
)


class _Cancel_job_Type(Integer32):
    """Custom type cancel_job based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_Cancel_job_Type.__name__ = "Integer32"
_Cancel_job_Object = MibScalar
cancel_job = _Cancel_job_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 1, 2),
    _Cancel_job_Type()
)
cancel_job.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cancel_job.setStatus("optional")


class _Encryption_password_type_Type(Integer32):
    """Custom type encryption_password_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eFalse", 0),
          ("eTrue", 1))
    )


_Encryption_password_type_Type.__name__ = "Integer32"
_Encryption_password_type_Object = MibScalar
encryption_password_type = _Encryption_password_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 1, 15),
    _Encryption_password_type_Type()
)
encryption_password_type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    encryption_password_type.setStatus("optional")
_Encryption_password_max_length_Type = Integer32
_Encryption_password_max_length_Object = MibScalar
encryption_password_max_length = _Encryption_password_max_length_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 1, 16),
    _Encryption_password_max_length_Type()
)
encryption_password_max_length.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    encryption_password_max_length.setStatus("optional")
_Encryption_password_min_length_Type = Integer32
_Encryption_password_min_length_Object = MibScalar
encryption_password_min_length = _Encryption_password_min_length_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 1, 17),
    _Encryption_password_min_length_Type()
)
encryption_password_min_length.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    encryption_password_min_length.setStatus("optional")


class _Job_storage_supported_Type(Integer32):
    """Custom type job_storage_supported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eFalse", 0),
          ("eTrue", 1))
    )


_Job_storage_supported_Type.__name__ = "Integer32"
_Job_storage_supported_Object = MibScalar
job_storage_supported = _Job_storage_supported_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 1, 18),
    _Job_storage_supported_Type()
)
job_storage_supported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    job_storage_supported.setStatus("optional")
_Job_storage_type_Type = OctetString
_Job_storage_type_Object = MibScalar
job_storage_type = _Job_storage_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 1, 19),
    _Job_storage_type_Type()
)
job_storage_type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    job_storage_type.setStatus("optional")
_Job_storage_mode_Type = OctetString
_Job_storage_mode_Object = MibScalar
job_storage_mode = _Job_storage_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 1, 20),
    _Job_storage_mode_Type()
)
job_storage_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    job_storage_mode.setStatus("optional")


class _Job_storage_available_Type(Integer32):
    """Custom type job_storage_available based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eFalse", 0),
          ("eTrue", 1))
    )


_Job_storage_available_Type.__name__ = "Integer32"
_Job_storage_available_Object = MibScalar
job_storage_available = _Job_storage_available_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 1, 21),
    _Job_storage_available_Type()
)
job_storage_available.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    job_storage_available.setStatus("optional")
_Job_storage_encryption_Type = OctetString
_Job_storage_encryption_Object = MibScalar
job_storage_encryption = _Job_storage_encryption_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 1, 22),
    _Job_storage_encryption_Type()
)
job_storage_encryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    job_storage_encryption.setStatus("optional")
_Active_print_jobs_ObjectIdentity = ObjectIdentity
active_print_jobs = _Active_print_jobs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 2)
)
_Job_being_parsed_ObjectIdentity = ObjectIdentity
job_being_parsed = _Job_being_parsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 2, 1)
)


class _Current_job_parsing_id_Type(Integer32):
    """Custom type current_job_parsing_id based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_Current_job_parsing_id_Type.__name__ = "Integer32"
_Current_job_parsing_id_Object = MibScalar
current_job_parsing_id = _Current_job_parsing_id_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 2, 1, 1),
    _Current_job_parsing_id_Type()
)
current_job_parsing_id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    current_job_parsing_id.setStatus("optional")
_Errorlog_ObjectIdentity = ObjectIdentity
errorlog = _Errorlog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11)
)
_Error1_ObjectIdentity = ObjectIdentity
error1 = _Error1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 1)
)
_Error1_time_stamp_Type = Integer32
_Error1_time_stamp_Object = MibScalar
error1_time_stamp = _Error1_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 1, 1),
    _Error1_time_stamp_Type()
)
error1_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error1_time_stamp.setStatus("optional")
_Error1_code_Type = Integer32
_Error1_code_Object = MibScalar
error1_code = _Error1_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 1, 2),
    _Error1_code_Type()
)
error1_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error1_code.setStatus("optional")
_Error1_date_time_Type = OctetString
_Error1_date_time_Object = MibScalar
error1_date_time = _Error1_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 1, 3),
    _Error1_date_time_Type()
)
error1_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error1_date_time.setStatus("optional")
_Error2_ObjectIdentity = ObjectIdentity
error2 = _Error2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 2)
)
_Error2_time_stamp_Type = Integer32
_Error2_time_stamp_Object = MibScalar
error2_time_stamp = _Error2_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 2, 1),
    _Error2_time_stamp_Type()
)
error2_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error2_time_stamp.setStatus("optional")
_Error2_code_Type = Integer32
_Error2_code_Object = MibScalar
error2_code = _Error2_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 2, 2),
    _Error2_code_Type()
)
error2_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error2_code.setStatus("optional")
_Error2_date_time_Type = OctetString
_Error2_date_time_Object = MibScalar
error2_date_time = _Error2_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 2, 3),
    _Error2_date_time_Type()
)
error2_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error2_date_time.setStatus("optional")
_Error3_ObjectIdentity = ObjectIdentity
error3 = _Error3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 3)
)
_Error3_time_stamp_Type = Integer32
_Error3_time_stamp_Object = MibScalar
error3_time_stamp = _Error3_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 3, 1),
    _Error3_time_stamp_Type()
)
error3_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error3_time_stamp.setStatus("optional")
_Error3_code_Type = Integer32
_Error3_code_Object = MibScalar
error3_code = _Error3_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 3, 2),
    _Error3_code_Type()
)
error3_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error3_code.setStatus("optional")
_Error3_date_time_Type = OctetString
_Error3_date_time_Object = MibScalar
error3_date_time = _Error3_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 3, 3),
    _Error3_date_time_Type()
)
error3_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error3_date_time.setStatus("optional")
_Error4_ObjectIdentity = ObjectIdentity
error4 = _Error4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 4)
)
_Error4_time_stamp_Type = Integer32
_Error4_time_stamp_Object = MibScalar
error4_time_stamp = _Error4_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 4, 1),
    _Error4_time_stamp_Type()
)
error4_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error4_time_stamp.setStatus("optional")
_Error4_code_Type = Integer32
_Error4_code_Object = MibScalar
error4_code = _Error4_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 4, 2),
    _Error4_code_Type()
)
error4_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error4_code.setStatus("optional")
_Error4_date_time_Type = OctetString
_Error4_date_time_Object = MibScalar
error4_date_time = _Error4_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 4, 3),
    _Error4_date_time_Type()
)
error4_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error4_date_time.setStatus("optional")
_Error5_ObjectIdentity = ObjectIdentity
error5 = _Error5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 5)
)
_Error5_time_stamp_Type = Integer32
_Error5_time_stamp_Object = MibScalar
error5_time_stamp = _Error5_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 5, 1),
    _Error5_time_stamp_Type()
)
error5_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error5_time_stamp.setStatus("optional")
_Error5_code_Type = Integer32
_Error5_code_Object = MibScalar
error5_code = _Error5_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 5, 2),
    _Error5_code_Type()
)
error5_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error5_code.setStatus("optional")
_Error5_date_time_Type = OctetString
_Error5_date_time_Object = MibScalar
error5_date_time = _Error5_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 5, 3),
    _Error5_date_time_Type()
)
error5_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error5_date_time.setStatus("optional")
_Error6_ObjectIdentity = ObjectIdentity
error6 = _Error6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 6)
)
_Error6_time_stamp_Type = Integer32
_Error6_time_stamp_Object = MibScalar
error6_time_stamp = _Error6_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 6, 1),
    _Error6_time_stamp_Type()
)
error6_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error6_time_stamp.setStatus("optional")
_Error6_code_Type = Integer32
_Error6_code_Object = MibScalar
error6_code = _Error6_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 6, 2),
    _Error6_code_Type()
)
error6_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error6_code.setStatus("optional")
_Error6_date_time_Type = OctetString
_Error6_date_time_Object = MibScalar
error6_date_time = _Error6_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 6, 3),
    _Error6_date_time_Type()
)
error6_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error6_date_time.setStatus("optional")
_Error7_ObjectIdentity = ObjectIdentity
error7 = _Error7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 7)
)
_Error7_time_stamp_Type = Integer32
_Error7_time_stamp_Object = MibScalar
error7_time_stamp = _Error7_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 7, 1),
    _Error7_time_stamp_Type()
)
error7_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error7_time_stamp.setStatus("optional")
_Error7_code_Type = Integer32
_Error7_code_Object = MibScalar
error7_code = _Error7_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 7, 2),
    _Error7_code_Type()
)
error7_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error7_code.setStatus("optional")
_Error7_date_time_Type = OctetString
_Error7_date_time_Object = MibScalar
error7_date_time = _Error7_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 7, 3),
    _Error7_date_time_Type()
)
error7_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error7_date_time.setStatus("optional")
_Error8_ObjectIdentity = ObjectIdentity
error8 = _Error8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 8)
)
_Error8_time_stamp_Type = Integer32
_Error8_time_stamp_Object = MibScalar
error8_time_stamp = _Error8_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 8, 1),
    _Error8_time_stamp_Type()
)
error8_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error8_time_stamp.setStatus("optional")
_Error8_code_Type = Integer32
_Error8_code_Object = MibScalar
error8_code = _Error8_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 8, 2),
    _Error8_code_Type()
)
error8_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error8_code.setStatus("optional")
_Error8_date_time_Type = OctetString
_Error8_date_time_Object = MibScalar
error8_date_time = _Error8_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 8, 3),
    _Error8_date_time_Type()
)
error8_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error8_date_time.setStatus("optional")
_Error9_ObjectIdentity = ObjectIdentity
error9 = _Error9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 9)
)
_Error9_time_stamp_Type = Integer32
_Error9_time_stamp_Object = MibScalar
error9_time_stamp = _Error9_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 9, 1),
    _Error9_time_stamp_Type()
)
error9_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error9_time_stamp.setStatus("optional")
_Error9_code_Type = Integer32
_Error9_code_Object = MibScalar
error9_code = _Error9_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 9, 2),
    _Error9_code_Type()
)
error9_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error9_code.setStatus("optional")
_Error9_date_time_Type = OctetString
_Error9_date_time_Object = MibScalar
error9_date_time = _Error9_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 9, 3),
    _Error9_date_time_Type()
)
error9_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error9_date_time.setStatus("optional")
_Error10_ObjectIdentity = ObjectIdentity
error10 = _Error10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 10)
)
_Error10_time_stamp_Type = Integer32
_Error10_time_stamp_Object = MibScalar
error10_time_stamp = _Error10_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 10, 1),
    _Error10_time_stamp_Type()
)
error10_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error10_time_stamp.setStatus("optional")
_Error10_code_Type = Integer32
_Error10_code_Object = MibScalar
error10_code = _Error10_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 10, 2),
    _Error10_code_Type()
)
error10_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error10_code.setStatus("optional")
_Error10_date_time_Type = OctetString
_Error10_date_time_Object = MibScalar
error10_date_time = _Error10_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 10, 3),
    _Error10_date_time_Type()
)
error10_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error10_date_time.setStatus("optional")
_Error11_ObjectIdentity = ObjectIdentity
error11 = _Error11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 11)
)
_Error11_time_stamp_Type = Integer32
_Error11_time_stamp_Object = MibScalar
error11_time_stamp = _Error11_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 11, 1),
    _Error11_time_stamp_Type()
)
error11_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error11_time_stamp.setStatus("optional")
_Error11_code_Type = Integer32
_Error11_code_Object = MibScalar
error11_code = _Error11_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 11, 2),
    _Error11_code_Type()
)
error11_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error11_code.setStatus("optional")
_Error11_date_time_Type = OctetString
_Error11_date_time_Object = MibScalar
error11_date_time = _Error11_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 11, 3),
    _Error11_date_time_Type()
)
error11_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error11_date_time.setStatus("optional")
_Error12_ObjectIdentity = ObjectIdentity
error12 = _Error12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 12)
)
_Error12_time_stamp_Type = Integer32
_Error12_time_stamp_Object = MibScalar
error12_time_stamp = _Error12_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 12, 1),
    _Error12_time_stamp_Type()
)
error12_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error12_time_stamp.setStatus("optional")
_Error12_code_Type = Integer32
_Error12_code_Object = MibScalar
error12_code = _Error12_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 12, 2),
    _Error12_code_Type()
)
error12_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error12_code.setStatus("optional")
_Error12_date_time_Type = OctetString
_Error12_date_time_Object = MibScalar
error12_date_time = _Error12_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 12, 3),
    _Error12_date_time_Type()
)
error12_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error12_date_time.setStatus("optional")
_Error13_ObjectIdentity = ObjectIdentity
error13 = _Error13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 13)
)
_Error13_time_stamp_Type = Integer32
_Error13_time_stamp_Object = MibScalar
error13_time_stamp = _Error13_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 13, 1),
    _Error13_time_stamp_Type()
)
error13_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error13_time_stamp.setStatus("optional")
_Error13_code_Type = Integer32
_Error13_code_Object = MibScalar
error13_code = _Error13_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 13, 2),
    _Error13_code_Type()
)
error13_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error13_code.setStatus("optional")
_Error13_date_time_Type = OctetString
_Error13_date_time_Object = MibScalar
error13_date_time = _Error13_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 13, 3),
    _Error13_date_time_Type()
)
error13_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error13_date_time.setStatus("optional")
_Error14_ObjectIdentity = ObjectIdentity
error14 = _Error14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 14)
)
_Error14_time_stamp_Type = Integer32
_Error14_time_stamp_Object = MibScalar
error14_time_stamp = _Error14_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 14, 1),
    _Error14_time_stamp_Type()
)
error14_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error14_time_stamp.setStatus("optional")
_Error14_code_Type = Integer32
_Error14_code_Object = MibScalar
error14_code = _Error14_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 14, 2),
    _Error14_code_Type()
)
error14_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error14_code.setStatus("optional")
_Error14_date_time_Type = OctetString
_Error14_date_time_Object = MibScalar
error14_date_time = _Error14_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 14, 3),
    _Error14_date_time_Type()
)
error14_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error14_date_time.setStatus("optional")
_Error15_ObjectIdentity = ObjectIdentity
error15 = _Error15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 15)
)
_Error15_time_stamp_Type = Integer32
_Error15_time_stamp_Object = MibScalar
error15_time_stamp = _Error15_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 15, 1),
    _Error15_time_stamp_Type()
)
error15_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error15_time_stamp.setStatus("optional")
_Error15_code_Type = Integer32
_Error15_code_Object = MibScalar
error15_code = _Error15_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 15, 2),
    _Error15_code_Type()
)
error15_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error15_code.setStatus("optional")
_Error15_date_time_Type = OctetString
_Error15_date_time_Object = MibScalar
error15_date_time = _Error15_date_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 15, 3),
    _Error15_date_time_Type()
)
error15_date_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error15_date_time.setStatus("optional")
_Accounting_ObjectIdentity = ObjectIdentity
accounting = _Accounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16)
)
_Printer_accounting_ObjectIdentity = ObjectIdentity
printer_accounting = _Printer_accounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1)
)
_Printed_media_usage_ObjectIdentity = ObjectIdentity
printed_media_usage = _Printed_media_usage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 1)
)


class _Printed_media_simplex_count_Type(Integer32):
    """Custom type printed_media_simplex_count based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 930576247),
    )


_Printed_media_simplex_count_Type.__name__ = "Integer32"
_Printed_media_simplex_count_Object = MibScalar
printed_media_simplex_count = _Printed_media_simplex_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 1, 1),
    _Printed_media_simplex_count_Type()
)
printed_media_simplex_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printed_media_simplex_count.setStatus("optional")


class _Printed_media_duplex_count_Type(Integer32):
    """Custom type printed_media_duplex_count based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 930576247),
    )


_Printed_media_duplex_count_Type.__name__ = "Integer32"
_Printed_media_duplex_count_Object = MibScalar
printed_media_duplex_count = _Printed_media_duplex_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 1, 3),
    _Printed_media_duplex_count_Type()
)
printed_media_duplex_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printed_media_duplex_count.setStatus("optional")
_Usage_printer_total_charge_Type = OctetString
_Usage_printer_total_charge_Object = MibScalar
usage_printer_total_charge = _Usage_printer_total_charge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 2),
    _Usage_printer_total_charge_Type()
)
usage_printer_total_charge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usage_printer_total_charge.setStatus("optional")
_Usage_average_toner_coverage_Type = OctetString
_Usage_average_toner_coverage_Object = MibScalar
usage_average_toner_coverage = _Usage_average_toner_coverage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 3),
    _Usage_average_toner_coverage_Type()
)
usage_average_toner_coverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usage_average_toner_coverage.setStatus("optional")


class _Usage_staple_count_Type(Integer32):
    """Custom type usage_staple_count based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 930576247),
    )


_Usage_staple_count_Type.__name__ = "Integer32"
_Usage_staple_count_Object = MibScalar
usage_staple_count = _Usage_staple_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 4),
    _Usage_staple_count_Type()
)
usage_staple_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usage_staple_count.setStatus("optional")
_Usage_printer_mono_total_charge_Type = OctetString
_Usage_printer_mono_total_charge_Object = MibScalar
usage_printer_mono_total_charge = _Usage_printer_mono_total_charge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 12),
    _Usage_printer_mono_total_charge_Type()
)
usage_printer_mono_total_charge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usage_printer_mono_total_charge.setStatus("optional")
_Usage_printer_color_total_charge_Type = OctetString
_Usage_printer_color_total_charge_Object = MibScalar
usage_printer_color_total_charge = _Usage_printer_color_total_charge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 13),
    _Usage_printer_color_total_charge_Type()
)
usage_printer_color_total_charge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usage_printer_color_total_charge.setStatus("optional")
_Print_meter_equivalent_impression_count_Type = OctetString
_Print_meter_equivalent_impression_count_Object = MibScalar
print_meter_equivalent_impression_count = _Print_meter_equivalent_impression_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 44),
    _Print_meter_equivalent_impression_count_Type()
)
print_meter_equivalent_impression_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    print_meter_equivalent_impression_count.setStatus("optional")
_Scanner_accounting_ObjectIdentity = ObjectIdentity
scanner_accounting = _Scanner_accounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 2)
)
_Usage_scanner_total_charge_Type = OctetString
_Usage_scanner_total_charge_Object = MibScalar
usage_scanner_total_charge = _Usage_scanner_total_charge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 2, 2),
    _Usage_scanner_total_charge_Type()
)
usage_scanner_total_charge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usage_scanner_total_charge.setStatus("optional")
_Printer_color_accounting_ObjectIdentity = ObjectIdentity
printer_color_accounting = _Printer_color_accounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 3)
)
_Printed_media_color_usage_ObjectIdentity = ObjectIdentity
printed_media_color_usage = _Printed_media_color_usage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 3, 1)
)
_Printed_media_color_simplex_count_Type = Integer32
_Printed_media_color_simplex_count_Object = MibScalar
printed_media_color_simplex_count = _Printed_media_color_simplex_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 3, 1, 1),
    _Printed_media_color_simplex_count_Type()
)
printed_media_color_simplex_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printed_media_color_simplex_count.setStatus("optional")
_Printed_media_color_duplex_count_Type = Integer32
_Printed_media_color_duplex_count_Object = MibScalar
printed_media_color_duplex_count = _Printed_media_color_duplex_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 3, 1, 3),
    _Printed_media_color_duplex_count_Type()
)
printed_media_color_duplex_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printed_media_color_duplex_count.setStatus("optional")
_Source_subsystem_ObjectIdentity = ObjectIdentity
source_subsystem = _Source_subsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2)
)
_Scanner_ObjectIdentity = ObjectIdentity
scanner = _Scanner_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2)
)
_Settings_scanner_ObjectIdentity = ObjectIdentity
settings_scanner = _Settings_scanner_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1)
)


class _Scanner_accessory_adf_sheet_count_Type(Integer32):
    """Custom type scanner_accessory_adf_sheet_count based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Scanner_accessory_adf_sheet_count_Type.__name__ = "Integer32"
_Scanner_accessory_adf_sheet_count_Object = MibScalar
scanner_accessory_adf_sheet_count = _Scanner_accessory_adf_sheet_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 20),
    _Scanner_accessory_adf_sheet_count_Type()
)
scanner_accessory_adf_sheet_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_adf_sheet_count.setStatus("optional")


class _Scanner_accessory_flatbed_scan_count_Type(Integer32):
    """Custom type scanner_accessory_flatbed_scan_count based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Scanner_accessory_flatbed_scan_count_Type.__name__ = "Integer32"
_Scanner_accessory_flatbed_scan_count_Object = MibScalar
scanner_accessory_flatbed_scan_count = _Scanner_accessory_flatbed_scan_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 21),
    _Scanner_accessory_flatbed_scan_count_Type()
)
scanner_accessory_flatbed_scan_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_flatbed_scan_count.setStatus("optional")
_Scanner_accessory_copy_job_scan_count_Type = Integer32
_Scanner_accessory_copy_job_scan_count_Object = MibScalar
scanner_accessory_copy_job_scan_count = _Scanner_accessory_copy_job_scan_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 61),
    _Scanner_accessory_copy_job_scan_count_Type()
)
scanner_accessory_copy_job_scan_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_copy_job_scan_count.setStatus("optional")
_Scanner_accessory_send_job_scan_count_Type = Integer32
_Scanner_accessory_send_job_scan_count_Object = MibScalar
scanner_accessory_send_job_scan_count = _Scanner_accessory_send_job_scan_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 62),
    _Scanner_accessory_send_job_scan_count_Type()
)
scanner_accessory_send_job_scan_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_send_job_scan_count.setStatus("optional")
_Scanner_accessory_total_copy_pages_printed_Type = Integer32
_Scanner_accessory_total_copy_pages_printed_Object = MibScalar
scanner_accessory_total_copy_pages_printed = _Scanner_accessory_total_copy_pages_printed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 63),
    _Scanner_accessory_total_copy_pages_printed_Type()
)
scanner_accessory_total_copy_pages_printed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_total_copy_pages_printed.setStatus("optional")


class _Scan_to_folder_count_Type(Integer32):
    """Custom type scan_to_folder_count based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999999),
    )


_Scan_to_folder_count_Type.__name__ = "Integer32"
_Scan_to_folder_count_Object = MibScalar
scan_to_folder_count = _Scan_to_folder_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 89),
    _Scan_to_folder_count_Type()
)
scan_to_folder_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scan_to_folder_count.setStatus("optional")


class _Fax_job_scan_count_Type(Integer32):
    """Custom type fax_job_scan_count based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999999),
    )


_Fax_job_scan_count_Type.__name__ = "Integer32"
_Fax_job_scan_count_Object = MibScalar
fax_job_scan_count = _Fax_job_scan_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 90),
    _Fax_job_scan_count_Type()
)
fax_job_scan_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fax_job_scan_count.setStatus("optional")
_Scanner_accessory_total_copy_mono_pages_printed_Type = Integer32
_Scanner_accessory_total_copy_mono_pages_printed_Object = MibScalar
scanner_accessory_total_copy_mono_pages_printed = _Scanner_accessory_total_copy_mono_pages_printed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 122),
    _Scanner_accessory_total_copy_mono_pages_printed_Type()
)
scanner_accessory_total_copy_mono_pages_printed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_total_copy_mono_pages_printed.setStatus("optional")
_Scanner_accessory_total_copy_color_pages_printed_Type = Integer32
_Scanner_accessory_total_copy_color_pages_printed_Object = MibScalar
scanner_accessory_total_copy_color_pages_printed = _Scanner_accessory_total_copy_color_pages_printed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 123),
    _Scanner_accessory_total_copy_color_pages_printed_Type()
)
scanner_accessory_total_copy_color_pages_printed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_total_copy_color_pages_printed.setStatus("optional")
_Processing_subsystem_ObjectIdentity = ObjectIdentity
processing_subsystem = _Processing_subsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3)
)
_Pdl_ObjectIdentity = ObjectIdentity
pdl = _Pdl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3)
)
_Pdl_pcl_ObjectIdentity = ObjectIdentity
pdl_pcl = _Pdl_pcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 3)
)
_Pcl_total_page_count_Type = Integer32
_Pcl_total_page_count_Object = MibScalar
pcl_total_page_count = _Pcl_total_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 3, 5),
    _Pcl_total_page_count_Type()
)
pcl_total_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcl_total_page_count.setStatus("optional")
_Pdl_postscript_ObjectIdentity = ObjectIdentity
pdl_postscript = _Pdl_postscript_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 4)
)
_Postscript_total_page_count_Type = Integer32
_Postscript_total_page_count_Object = MibScalar
postscript_total_page_count = _Postscript_total_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 4, 5),
    _Postscript_total_page_count_Type()
)
postscript_total_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    postscript_total_page_count.setStatus("optional")
_Fax_proc_sub_ObjectIdentity = ObjectIdentity
fax_proc_sub = _Fax_proc_sub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7)
)
_Settings_fax_proc_sub_ObjectIdentity = ObjectIdentity
settings_fax_proc_sub = _Settings_fax_proc_sub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1)
)
_Fax_print_page_count_Type = Integer32
_Fax_print_page_count_Object = MibScalar
fax_print_page_count = _Fax_print_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 32),
    _Fax_print_page_count_Type()
)
fax_print_page_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_print_page_count.setStatus("optional")
_Status_fax_proc_sub_ObjectIdentity = ObjectIdentity
status_fax_proc_sub = _Status_fax_proc_sub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 2)
)
_Afax_send_page_count_Type = Integer32
_Afax_send_page_count_Object = MibScalar
afax_send_page_count = _Afax_send_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 2, 11),
    _Afax_send_page_count_Type()
)
afax_send_page_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    afax_send_page_count.setStatus("optional")
_Afax_recv_page_count_Type = Integer32
_Afax_recv_page_count_Object = MibScalar
afax_recv_page_count = _Afax_recv_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 2, 12),
    _Afax_recv_page_count_Type()
)
afax_recv_page_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    afax_recv_page_count.setStatus("optional")
_Destination_subsystem_ObjectIdentity = ObjectIdentity
destination_subsystem = _Destination_subsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4)
)
_Print_engine_ObjectIdentity = ObjectIdentity
print_engine = _Print_engine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1)
)
_Status_prt_eng_ObjectIdentity = ObjectIdentity
status_prt_eng = _Status_prt_eng_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 2)
)
_Total_engine_page_count_Type = Integer32
_Total_engine_page_count_Object = MibScalar
total_engine_page_count = _Total_engine_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 2, 5),
    _Total_engine_page_count_Type()
)
total_engine_page_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    total_engine_page_count.setStatus("optional")
_Total_mono_page_count_Type = Integer32
_Total_mono_page_count_Object = MibScalar
total_mono_page_count = _Total_mono_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 2, 6),
    _Total_mono_page_count_Type()
)
total_mono_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    total_mono_page_count.setStatus("optional")
_Total_color_page_count_Type = Integer32
_Total_color_page_count_Object = MibScalar
total_color_page_count = _Total_color_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 2, 7),
    _Total_color_page_count_Type()
)
total_color_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    total_color_page_count.setStatus("optional")
_Duplex_page_count_Type = Integer32
_Duplex_page_count_Object = MibScalar
duplex_page_count = _Duplex_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 2, 22),
    _Duplex_page_count_Type()
)
duplex_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    duplex_page_count.setStatus("optional")
_Intray_ObjectIdentity = ObjectIdentity
intray = _Intray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3)
)
_Status_intray_ObjectIdentity = ObjectIdentity
status_intray = _Status_intray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 2)
)
_Not_ready_tray_empty_Type = OctetString
_Not_ready_tray_empty_Object = MibScalar
not_ready_tray_empty = _Not_ready_tray_empty_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 2, 2),
    _Not_ready_tray_empty_Type()
)
not_ready_tray_empty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    not_ready_tray_empty.setStatus("optional")
_Intrays_ObjectIdentity = ObjectIdentity
intrays = _Intrays_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3)
)
_Intray1_ObjectIdentity = ObjectIdentity
intray1 = _Intray1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 1)
)


class _Tray1_media_size_loaded_Type(Integer32):
    """Custom type tray1_media_size_loaded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10,
              15,
              17,
              24,
              25,
              26,
              34,
              44,
              45,
              71,
              74,
              75,
              78,
              80,
              81,
              89,
              90,
              91,
              92,
              100,
              101,
              110,
              111,
              118,
              121,
              122,
              127,
              328,
              32765)
        )
    )
    namedValues = NamedValues(
        *(("eUSExecutive", 1),
          ("eUSLetter", 2),
          ("eUSLegal", 3),
          ("eFoolscap", 10),
          ("eStatement", 15),
          ("eROC16K", 17),
          ("eISOandJISA6", 24),
          ("eISOandJISA5", 25),
          ("eISOandJISA4", 26),
          ("ePRC16K195X270", 34),
          ("eJISB6", 44),
          ("eJISB5", 45),
          ("eJapansePostcardSingle", 71),
          ("eIndexCard4x6", 74),
          ("eIndexCard5x8", 75),
          ("eIndexCard3x5", 78),
          ("eMonarch", 80),
          ("eCommercial10", 81),
          ("ePRC16K184X260", 89),
          ("eInternationalDL", 90),
          ("eInternationalC5", 91),
          ("eInternationalC6", 92),
          ("eInternationalB5", 100),
          ("eCustom", 101),
          ("eJapanseEnvLong3", 110),
          ("eJapanseEnvLong4", 111),
          ("ePhoto10x15", 118),
          ("ePhotoLSizeCard", 121),
          ("eIndexCard5x7", 122),
          ("eLegal216x340", 127),
          ("eJapanseOufuku148x200", 328),
          ("eAnySize", 32765))
    )


_Tray1_media_size_loaded_Type.__name__ = "Integer32"
_Tray1_media_size_loaded_Object = MibScalar
tray1_media_size_loaded = _Tray1_media_size_loaded_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 1, 1),
    _Tray1_media_size_loaded_Type()
)
tray1_media_size_loaded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tray1_media_size_loaded.setStatus("optional")
_Tray1_media_name_Type = OctetString
_Tray1_media_name_Object = MibScalar
tray1_media_name = _Tray1_media_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 1, 4),
    _Tray1_media_name_Type()
)
tray1_media_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tray1_media_name.setStatus("optional")
_Tray1_custom_media_width_Type = Integer32
_Tray1_custom_media_width_Object = MibScalar
tray1_custom_media_width = _Tray1_custom_media_width_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 1, 10),
    _Tray1_custom_media_width_Type()
)
tray1_custom_media_width.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray1_custom_media_width.setStatus("optional")
_Tray1_custom_media_length_Type = Integer32
_Tray1_custom_media_length_Object = MibScalar
tray1_custom_media_length = _Tray1_custom_media_length_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 1, 11),
    _Tray1_custom_media_length_Type()
)
tray1_custom_media_length.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray1_custom_media_length.setStatus("optional")


class _Tray1_type_Type(Integer32):
    """Custom type tray1_type based on Integer32"""
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
        *(("eTray", 1),
          ("eManualRoll", 2),
          ("eArss", 3),
          ("eManualSheet", 4))
    )


_Tray1_type_Type.__name__ = "Integer32"
_Tray1_type_Object = MibScalar
tray1_type = _Tray1_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 1, 17),
    _Tray1_type_Type()
)
tray1_type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tray1_type.setStatus("optional")
_Tray1_media_key_Type = OctetString
_Tray1_media_key_Object = MibScalar
tray1_media_key = _Tray1_media_key_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 1, 20),
    _Tray1_media_key_Type()
)
tray1_media_key.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray1_media_key.setStatus("optional")
_Intray2_ObjectIdentity = ObjectIdentity
intray2 = _Intray2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 2)
)


class _Tray2_media_size_loaded_Type(Integer32):
    """Custom type tray2_media_size_loaded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              15,
              17,
              25,
              26,
              34,
              45,
              81,
              89,
              90,
              91,
              100,
              101,
              110)
        )
    )
    namedValues = NamedValues(
        *(("eUSExecutive", 1),
          ("eUSLetter", 2),
          ("eStatement", 15),
          ("eROC16K", 17),
          ("eISOandJISA5", 25),
          ("eISOandJISA4", 26),
          ("ePRC16K195X270", 34),
          ("eJISB5", 45),
          ("eCommercial10", 81),
          ("ePRC16K184X260", 89),
          ("eInternationalDL", 90),
          ("eInternationalC5", 91),
          ("eInternationalB5", 100),
          ("eCustom", 101),
          ("eJapanseEnvLong3", 110))
    )


_Tray2_media_size_loaded_Type.__name__ = "Integer32"
_Tray2_media_size_loaded_Object = MibScalar
tray2_media_size_loaded = _Tray2_media_size_loaded_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 2, 1),
    _Tray2_media_size_loaded_Type()
)
tray2_media_size_loaded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tray2_media_size_loaded.setStatus("optional")
_Tray2_media_name_Type = OctetString
_Tray2_media_name_Object = MibScalar
tray2_media_name = _Tray2_media_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 2, 4),
    _Tray2_media_name_Type()
)
tray2_media_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tray2_media_name.setStatus("optional")
_Tray2_custom_media_width_Type = Integer32
_Tray2_custom_media_width_Object = MibScalar
tray2_custom_media_width = _Tray2_custom_media_width_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 2, 10),
    _Tray2_custom_media_width_Type()
)
tray2_custom_media_width.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray2_custom_media_width.setStatus("optional")
_Tray2_custom_media_length_Type = Integer32
_Tray2_custom_media_length_Object = MibScalar
tray2_custom_media_length = _Tray2_custom_media_length_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 2, 11),
    _Tray2_custom_media_length_Type()
)
tray2_custom_media_length.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray2_custom_media_length.setStatus("optional")


class _Tray2_type_Type(Integer32):
    """Custom type tray2_type based on Integer32"""
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
        *(("eTray", 1),
          ("eManualRoll", 2),
          ("eArss", 3),
          ("eManualSheet", 4))
    )


_Tray2_type_Type.__name__ = "Integer32"
_Tray2_type_Object = MibScalar
tray2_type = _Tray2_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 2, 17),
    _Tray2_type_Type()
)
tray2_type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tray2_type.setStatus("optional")
_Tray2_media_key_Type = OctetString
_Tray2_media_key_Object = MibScalar
tray2_media_key = _Tray2_media_key_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 2, 20),
    _Tray2_media_key_Type()
)
tray2_media_key.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray2_media_key.setStatus("optional")
_Intray3_ObjectIdentity = ObjectIdentity
intray3 = _Intray3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 3)
)


class _Tray3_media_size_loaded_Type(Integer32):
    """Custom type tray3_media_size_loaded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10,
              15,
              17,
              25,
              26,
              34,
              45,
              89,
              101,
              127)
        )
    )
    namedValues = NamedValues(
        *(("eUSExecutive", 1),
          ("eUSLetter", 2),
          ("eUSLegal", 3),
          ("eFoolscap", 10),
          ("eStatement", 15),
          ("eROC16K", 17),
          ("eISOandJISA5", 25),
          ("eISOandJISA4", 26),
          ("ePRC16K195X270", 34),
          ("eJISB5", 45),
          ("ePRC16K184X260", 89),
          ("eCustom", 101),
          ("eLegal216x340", 127))
    )


_Tray3_media_size_loaded_Type.__name__ = "Integer32"
_Tray3_media_size_loaded_Object = MibScalar
tray3_media_size_loaded = _Tray3_media_size_loaded_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 3, 1),
    _Tray3_media_size_loaded_Type()
)
tray3_media_size_loaded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tray3_media_size_loaded.setStatus("optional")
_Tray3_media_name_Type = OctetString
_Tray3_media_name_Object = MibScalar
tray3_media_name = _Tray3_media_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 3, 4),
    _Tray3_media_name_Type()
)
tray3_media_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tray3_media_name.setStatus("optional")
_Tray3_custom_media_width_Type = Integer32
_Tray3_custom_media_width_Object = MibScalar
tray3_custom_media_width = _Tray3_custom_media_width_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 3, 10),
    _Tray3_custom_media_width_Type()
)
tray3_custom_media_width.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray3_custom_media_width.setStatus("optional")
_Tray3_custom_media_length_Type = Integer32
_Tray3_custom_media_length_Object = MibScalar
tray3_custom_media_length = _Tray3_custom_media_length_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 3, 11),
    _Tray3_custom_media_length_Type()
)
tray3_custom_media_length.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray3_custom_media_length.setStatus("optional")


class _Tray3_type_Type(Integer32):
    """Custom type tray3_type based on Integer32"""
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
        *(("eTray", 1),
          ("eManualRoll", 2),
          ("eArss", 3),
          ("eManualSheet", 4))
    )


_Tray3_type_Type.__name__ = "Integer32"
_Tray3_type_Object = MibScalar
tray3_type = _Tray3_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 3, 17),
    _Tray3_type_Type()
)
tray3_type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tray3_type.setStatus("optional")
_Tray3_media_key_Type = OctetString
_Tray3_media_key_Object = MibScalar
tray3_media_key = _Tray3_media_key_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 3, 20),
    _Tray3_media_key_Type()
)
tray3_media_key.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray3_media_key.setStatus("optional")
_Intray5_ObjectIdentity = ObjectIdentity
intray5 = _Intray5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 5)
)


class _Tray5_media_size_loaded_Type(Integer32):
    """Custom type tray5_media_size_loaded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10,
              15,
              17,
              25,
              26,
              34,
              45,
              89,
              101,
              127)
        )
    )
    namedValues = NamedValues(
        *(("eUSExecutive", 1),
          ("eUSLetter", 2),
          ("eUSLegal", 3),
          ("eFoolscap", 10),
          ("eStatement", 15),
          ("eROC16K", 17),
          ("eISOandJISA5", 25),
          ("eISOandJISA4", 26),
          ("ePRC16K195X270", 34),
          ("eJISB5", 45),
          ("ePRC16K184X260", 89),
          ("eCustom", 101),
          ("eLegal216x340", 127))
    )


_Tray5_media_size_loaded_Type.__name__ = "Integer32"
_Tray5_media_size_loaded_Object = MibScalar
tray5_media_size_loaded = _Tray5_media_size_loaded_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 5, 1),
    _Tray5_media_size_loaded_Type()
)
tray5_media_size_loaded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tray5_media_size_loaded.setStatus("optional")
_Tray5_media_name_Type = OctetString
_Tray5_media_name_Object = MibScalar
tray5_media_name = _Tray5_media_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 5, 4),
    _Tray5_media_name_Type()
)
tray5_media_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tray5_media_name.setStatus("optional")
_Tray5_custom_media_width_Type = Integer32
_Tray5_custom_media_width_Object = MibScalar
tray5_custom_media_width = _Tray5_custom_media_width_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 5, 10),
    _Tray5_custom_media_width_Type()
)
tray5_custom_media_width.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray5_custom_media_width.setStatus("optional")
_Tray5_custom_media_length_Type = Integer32
_Tray5_custom_media_length_Object = MibScalar
tray5_custom_media_length = _Tray5_custom_media_length_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 5, 11),
    _Tray5_custom_media_length_Type()
)
tray5_custom_media_length.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray5_custom_media_length.setStatus("optional")


class _Tray5_type_Type(Integer32):
    """Custom type tray5_type based on Integer32"""
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
        *(("eTray", 1),
          ("eManualRoll", 2),
          ("eArss", 3),
          ("eManualSheet", 4))
    )


_Tray5_type_Type.__name__ = "Integer32"
_Tray5_type_Object = MibScalar
tray5_type = _Tray5_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 5, 17),
    _Tray5_type_Type()
)
tray5_type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tray5_type.setStatus("optional")
_Tray5_media_key_Type = OctetString
_Tray5_media_key_Object = MibScalar
tray5_media_key = _Tray5_media_key_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 5, 20),
    _Tray5_media_key_Type()
)
tray5_media_key.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray5_media_key.setStatus("optional")
_Print_media_ObjectIdentity = ObjectIdentity
print_media = _Print_media_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8)
)
_Settings_print_media_ObjectIdentity = ObjectIdentity
settings_print_media = _Settings_print_media_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 1)
)
_Media_names_enabled_Type = OctetString
_Media_names_enabled_Object = MibScalar
media_names_enabled = _Media_names_enabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 1, 3),
    _Media_names_enabled_Type()
)
media_names_enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media_names_enabled.setStatus("optional")
_Media_info_ObjectIdentity = ObjectIdentity
media_info = _Media_info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3)
)
_Media1_ObjectIdentity = ObjectIdentity
media1 = _Media1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 1)
)


class _Media1_name_Type(DisplayString):
    """Custom type media1_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media1_name_Type.__name__ = "DisplayString"
_Media1_name_Object = MibScalar
media1_name = _Media1_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 1, 1),
    _Media1_name_Type()
)
media1_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media1_name.setStatus("optional")
_Media2_ObjectIdentity = ObjectIdentity
media2 = _Media2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 2)
)


class _Media2_name_Type(DisplayString):
    """Custom type media2_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media2_name_Type.__name__ = "DisplayString"
_Media2_name_Object = MibScalar
media2_name = _Media2_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 2, 1),
    _Media2_name_Type()
)
media2_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media2_name.setStatus("optional")
_Media3_ObjectIdentity = ObjectIdentity
media3 = _Media3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 3)
)


class _Media3_name_Type(DisplayString):
    """Custom type media3_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media3_name_Type.__name__ = "DisplayString"
_Media3_name_Object = MibScalar
media3_name = _Media3_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 3, 1),
    _Media3_name_Type()
)
media3_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media3_name.setStatus("optional")
_Media4_ObjectIdentity = ObjectIdentity
media4 = _Media4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 4)
)


class _Media4_name_Type(DisplayString):
    """Custom type media4_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media4_name_Type.__name__ = "DisplayString"
_Media4_name_Object = MibScalar
media4_name = _Media4_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 4, 1),
    _Media4_name_Type()
)
media4_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media4_name.setStatus("optional")
_Media5_ObjectIdentity = ObjectIdentity
media5 = _Media5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 5)
)


class _Media5_name_Type(DisplayString):
    """Custom type media5_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media5_name_Type.__name__ = "DisplayString"
_Media5_name_Object = MibScalar
media5_name = _Media5_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 5, 1),
    _Media5_name_Type()
)
media5_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media5_name.setStatus("optional")
_Media6_ObjectIdentity = ObjectIdentity
media6 = _Media6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 6)
)


class _Media6_name_Type(DisplayString):
    """Custom type media6_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media6_name_Type.__name__ = "DisplayString"
_Media6_name_Object = MibScalar
media6_name = _Media6_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 6, 1),
    _Media6_name_Type()
)
media6_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media6_name.setStatus("optional")
_Media7_ObjectIdentity = ObjectIdentity
media7 = _Media7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 7)
)


class _Media7_name_Type(DisplayString):
    """Custom type media7_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media7_name_Type.__name__ = "DisplayString"
_Media7_name_Object = MibScalar
media7_name = _Media7_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 7, 1),
    _Media7_name_Type()
)
media7_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media7_name.setStatus("optional")
_Media8_ObjectIdentity = ObjectIdentity
media8 = _Media8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 8)
)


class _Media8_name_Type(DisplayString):
    """Custom type media8_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media8_name_Type.__name__ = "DisplayString"
_Media8_name_Object = MibScalar
media8_name = _Media8_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 8, 1),
    _Media8_name_Type()
)
media8_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media8_name.setStatus("optional")
_Media9_ObjectIdentity = ObjectIdentity
media9 = _Media9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 9)
)


class _Media9_name_Type(DisplayString):
    """Custom type media9_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media9_name_Type.__name__ = "DisplayString"
_Media9_name_Object = MibScalar
media9_name = _Media9_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 9, 1),
    _Media9_name_Type()
)
media9_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media9_name.setStatus("optional")
_Media10_ObjectIdentity = ObjectIdentity
media10 = _Media10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 10)
)


class _Media10_name_Type(DisplayString):
    """Custom type media10_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media10_name_Type.__name__ = "DisplayString"
_Media10_name_Object = MibScalar
media10_name = _Media10_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 10, 1),
    _Media10_name_Type()
)
media10_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media10_name.setStatus("optional")
_Media11_ObjectIdentity = ObjectIdentity
media11 = _Media11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 11)
)


class _Media11_name_Type(DisplayString):
    """Custom type media11_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media11_name_Type.__name__ = "DisplayString"
_Media11_name_Object = MibScalar
media11_name = _Media11_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 11, 1),
    _Media11_name_Type()
)
media11_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media11_name.setStatus("optional")
_Media12_ObjectIdentity = ObjectIdentity
media12 = _Media12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 12)
)


class _Media12_name_Type(DisplayString):
    """Custom type media12_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media12_name_Type.__name__ = "DisplayString"
_Media12_name_Object = MibScalar
media12_name = _Media12_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 12, 1),
    _Media12_name_Type()
)
media12_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media12_name.setStatus("optional")
_Media13_ObjectIdentity = ObjectIdentity
media13 = _Media13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 13)
)


class _Media13_name_Type(DisplayString):
    """Custom type media13_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media13_name_Type.__name__ = "DisplayString"
_Media13_name_Object = MibScalar
media13_name = _Media13_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 13, 1),
    _Media13_name_Type()
)
media13_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media13_name.setStatus("optional")
_Media14_ObjectIdentity = ObjectIdentity
media14 = _Media14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 14)
)


class _Media14_name_Type(DisplayString):
    """Custom type media14_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media14_name_Type.__name__ = "DisplayString"
_Media14_name_Object = MibScalar
media14_name = _Media14_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 14, 1),
    _Media14_name_Type()
)
media14_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media14_name.setStatus("optional")
_Media15_ObjectIdentity = ObjectIdentity
media15 = _Media15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 15)
)


class _Media15_name_Type(DisplayString):
    """Custom type media15_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media15_name_Type.__name__ = "DisplayString"
_Media15_name_Object = MibScalar
media15_name = _Media15_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 15, 1),
    _Media15_name_Type()
)
media15_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media15_name.setStatus("optional")
_Media16_ObjectIdentity = ObjectIdentity
media16 = _Media16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 16)
)


class _Media16_name_Type(DisplayString):
    """Custom type media16_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media16_name_Type.__name__ = "DisplayString"
_Media16_name_Object = MibScalar
media16_name = _Media16_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 16, 1),
    _Media16_name_Type()
)
media16_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media16_name.setStatus("optional")
_Media17_ObjectIdentity = ObjectIdentity
media17 = _Media17_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 17)
)


class _Media17_name_Type(DisplayString):
    """Custom type media17_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media17_name_Type.__name__ = "DisplayString"
_Media17_name_Object = MibScalar
media17_name = _Media17_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 17, 1),
    _Media17_name_Type()
)
media17_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media17_name.setStatus("optional")
_Media18_ObjectIdentity = ObjectIdentity
media18 = _Media18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 18)
)


class _Media18_name_Type(DisplayString):
    """Custom type media18_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media18_name_Type.__name__ = "DisplayString"
_Media18_name_Object = MibScalar
media18_name = _Media18_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 18, 1),
    _Media18_name_Type()
)
media18_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media18_name.setStatus("optional")
_Media19_ObjectIdentity = ObjectIdentity
media19 = _Media19_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 19)
)


class _Media19_name_Type(DisplayString):
    """Custom type media19_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media19_name_Type.__name__ = "DisplayString"
_Media19_name_Object = MibScalar
media19_name = _Media19_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 19, 1),
    _Media19_name_Type()
)
media19_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media19_name.setStatus("optional")
_Consumables_ObjectIdentity = ObjectIdentity
consumables = _Consumables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10)
)
_Consumables_1_ObjectIdentity = ObjectIdentity
consumables_1 = _Consumables_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 1)
)
_Consumable_status_ObjectIdentity = ObjectIdentity
consumable_status = _Consumable_status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 1, 1)
)


class _Consumable_status_cartridge_model_Type(DisplayString):
    """Custom type consumable_status_cartridge_model based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_Consumable_status_cartridge_model_Type.__name__ = "DisplayString"
_Consumable_status_cartridge_model_Object = MibScalar
consumable_status_cartridge_model = _Consumable_status_cartridge_model_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 1, 1, 1),
    _Consumable_status_cartridge_model_Type()
)
consumable_status_cartridge_model.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consumable_status_cartridge_model.setStatus("optional")


class _Consumable_status_manufacturing_date_Type(DisplayString):
    """Custom type consumable_status_manufacturing_date based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_Consumable_status_manufacturing_date_Type.__name__ = "DisplayString"
_Consumable_status_manufacturing_date_Object = MibScalar
consumable_status_manufacturing_date = _Consumable_status_manufacturing_date_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 1, 1, 2),
    _Consumable_status_manufacturing_date_Type()
)
consumable_status_manufacturing_date.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consumable_status_manufacturing_date.setStatus("optional")


class _Consumable_status_serial_number_Type(DisplayString):
    """Custom type consumable_status_serial_number based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_Consumable_status_serial_number_Type.__name__ = "DisplayString"
_Consumable_status_serial_number_Object = MibScalar
consumable_status_serial_number = _Consumable_status_serial_number_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 1, 1, 3),
    _Consumable_status_serial_number_Type()
)
consumable_status_serial_number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consumable_status_serial_number.setStatus("optional")


class _Consumable_status_first_install_date_Type(DisplayString):
    """Custom type consumable_status_first_install_date based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_Consumable_status_first_install_date_Type.__name__ = "DisplayString"
_Consumable_status_first_install_date_Object = MibScalar
consumable_status_first_install_date = _Consumable_status_first_install_date_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 1, 1, 8),
    _Consumable_status_first_install_date_Type()
)
consumable_status_first_install_date.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consumable_status_first_install_date.setStatus("optional")
_Interface_ObjectIdentity = ObjectIdentity
interface = _Interface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 4)
)
_NpCard_ObjectIdentity = ObjectIdentity
npCard = _NpCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3)
)
_NpSys_ObjectIdentity = ObjectIdentity
npSys = _NpSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 1)
)


class _NpSysModelNumber_Type(OctetString):
    """Custom type npSysModelNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_NpSysModelNumber_Type.__name__ = "OctetString"
_NpSysModelNumber_Object = MibScalar
npSysModelNumber = _NpSysModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 1, 10),
    _NpSysModelNumber_Type()
)
npSysModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npSysModelNumber.setStatus("current")
_NpSysCardServices1_Type = Integer32
_NpSysCardServices1_Object = MibScalar
npSysCardServices1 = _NpSysCardServices1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 1, 16),
    _NpSysCardServices1_Type()
)
npSysCardServices1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npSysCardServices1.setStatus("current")
_NpSysCardServices2_Type = Integer32
_NpSysCardServices2_Object = MibScalar
npSysCardServices2 = _NpSysCardServices2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 1, 17),
    _NpSysCardServices2_Type()
)
npSysCardServices2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npSysCardServices2.setStatus("current")
_NpSysCardServices3_Type = Integer32
_NpSysCardServices3_Object = MibScalar
npSysCardServices3 = _NpSysCardServices3_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 1, 22),
    _NpSysCardServices3_Type()
)
npSysCardServices3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npSysCardServices3.setStatus("current")
_NpCfg_ObjectIdentity = ObjectIdentity
npCfg = _NpCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 5)
)


class _NpCfgSource_Type(Integer32):
    """Custom type npCfgSource based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("manual-one", 1),
          ("bootp-two", 2),
          ("manual-three", 3),
          ("bootp-four", 4),
          ("dhcp", 5),
          ("not-configured", 6),
          ("default-config", 7),
          ("rarp", 8),
          ("read-only", 9),
          ("auto-ip", 10))
    )


_NpCfgSource_Type.__name__ = "Integer32"
_NpCfgSource_Object = MibScalar
npCfgSource = _NpCfgSource_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 5, 1),
    _NpCfgSource_Type()
)
npCfgSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCfgSource.setStatus("current")
_NpCfgYiaddr_Type = IpAddress
_NpCfgYiaddr_Object = MibScalar
npCfgYiaddr = _NpCfgYiaddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 5, 2),
    _NpCfgYiaddr_Type()
)
npCfgYiaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCfgYiaddr.setStatus("current")
_NpCfgSiaddr_Type = IpAddress
_NpCfgSiaddr_Object = MibScalar
npCfgSiaddr = _NpCfgSiaddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 5, 3),
    _NpCfgSiaddr_Type()
)
npCfgSiaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npCfgSiaddr.setStatus("current")
_NpCfgLogServer_Type = IpAddress
_NpCfgLogServer_Object = MibScalar
npCfgLogServer = _NpCfgLogServer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 5, 5),
    _NpCfgLogServer_Type()
)
npCfgLogServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCfgLogServer.setStatus("current")
_NpCfgSubnetMask_Type = IpAddress
_NpCfgSubnetMask_Object = MibScalar
npCfgSubnetMask = _NpCfgSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 5, 12),
    _NpCfgSubnetMask_Type()
)
npCfgSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCfgSubnetMask.setStatus("current")
_NpCfgDefaultGateway_Type = IpAddress
_NpCfgDefaultGateway_Object = MibScalar
npCfgDefaultGateway = _NpCfgDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 5, 13),
    _NpCfgDefaultGateway_Type()
)
npCfgDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCfgDefaultGateway.setStatus("current")


class _NpCfgDomainName_Type(OctetString):
    """Custom type npCfgDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NpCfgDomainName_Type.__name__ = "OctetString"
_NpCfgDomainName_Object = MibScalar
npCfgDomainName = _NpCfgDomainName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 5, 16),
    _NpCfgDomainName_Type()
)
npCfgDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCfgDomainName.setStatus("current")
_NpCfgIPP_Type = Integer32
_NpCfgIPP_Object = MibScalar
npCfgIPP = _NpCfgIPP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 5, 18),
    _NpCfgIPP_Type()
)
npCfgIPP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCfgIPP.setStatus("current")
_NpCfgDNSNameServerId_Type = IpAddress
_NpCfgDNSNameServerId_Object = MibScalar
npCfgDNSNameServerId = _NpCfgDNSNameServerId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 5, 21),
    _NpCfgDNSNameServerId_Type()
)
npCfgDNSNameServerId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCfgDNSNameServerId.setStatus("current")
_NpCfgWINSNameServerIdPri_Type = IpAddress
_NpCfgWINSNameServerIdPri_Object = MibScalar
npCfgWINSNameServerIdPri = _NpCfgWINSNameServerIdPri_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 5, 22),
    _NpCfgWINSNameServerIdPri_Type()
)
npCfgWINSNameServerIdPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCfgWINSNameServerIdPri.setStatus("current")
_NpCfgWINSNameServerIdSec_Type = IpAddress
_NpCfgWINSNameServerIdSec_Object = MibScalar
npCfgWINSNameServerIdSec = _NpCfgWINSNameServerIdSec_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 5, 23),
    _NpCfgWINSNameServerIdSec_Type()
)
npCfgWINSNameServerIdSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCfgWINSNameServerIdSec.setStatus("current")
_NpCfgPasswd1_Type = DisplayString
_NpCfgPasswd1_Object = MibScalar
npCfgPasswd1 = _NpCfgPasswd1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 5, 29),
    _NpCfgPasswd1_Type()
)
npCfgPasswd1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCfgPasswd1.setStatus("current")


class _NpCfgLinkType_Type(Integer32):
    """Custom type npCfgLinkType based on Integer32"""
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
        *(("autoNegotiate", 1),
          ("full10T", 2),
          ("half10T", 3),
          ("full100T", 4),
          ("half100T", 5),
          ("auto100T", 6),
          ("full1000T", 7))
    )


_NpCfgLinkType_Type.__name__ = "Integer32"
_NpCfgLinkType_Object = MibScalar
npCfgLinkType = _NpCfgLinkType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 5, 35),
    _NpCfgLinkType_Type()
)
npCfgLinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCfgLinkType.setStatus("current")


class _NpCfgSnmpDefaultReadCmnty_Type(Integer32):
    """Custom type npCfgSnmpDefaultReadCmnty based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NpCfgSnmpDefaultReadCmnty_Type.__name__ = "Integer32"
_NpCfgSnmpDefaultReadCmnty_Object = MibScalar
npCfgSnmpDefaultReadCmnty = _NpCfgSnmpDefaultReadCmnty_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 5, 40),
    _NpCfgSnmpDefaultReadCmnty_Type()
)
npCfgSnmpDefaultReadCmnty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCfgSnmpDefaultReadCmnty.setStatus("current")


class _NpCfgBonjourServiceName_Type(OctetString):
    """Custom type npCfgBonjourServiceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_NpCfgBonjourServiceName_Type.__name__ = "OctetString"
_NpCfgBonjourServiceName_Object = MibScalar
npCfgBonjourServiceName = _NpCfgBonjourServiceName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 5, 44),
    _NpCfgBonjourServiceName_Type()
)
npCfgBonjourServiceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCfgBonjourServiceName.setStatus("current")


class _NpCfgBonjourHighestPriorityService_Type(Integer32):
    """Custom type npCfgBonjourHighestPriorityService based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("p9100-Printing", 1),
          ("IPP-Printing", 2),
          ("lPD-Printing-RAW", 3),
          ("lPD-Printing-TEXT", 4),
          ("lPD-Printing-AUTO", 5),
          ("lPD-Printing-BINPS", 6),
          ("lPD-Printing-Queue5", 7),
          ("lPD-Printing-Queue6", 8),
          ("lPD-Printing-Queue7", 9),
          ("lPD-Printing-Queue8", 10),
          ("lPD-Printing-Queue9", 11),
          ("lPD-Printing-Queue10", 12),
          ("IPPS-Printing", 16))
    )


_NpCfgBonjourHighestPriorityService_Type.__name__ = "Integer32"
_NpCfgBonjourHighestPriorityService_Object = MibScalar
npCfgBonjourHighestPriorityService = _NpCfgBonjourHighestPriorityService_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 5, 45),
    _NpCfgBonjourHighestPriorityService_Type()
)
npCfgBonjourHighestPriorityService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCfgBonjourHighestPriorityService.setStatus("current")


class _NpCfgBonjourDomainName_Type(OctetString):
    """Custom type npCfgBonjourDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NpCfgBonjourDomainName_Type.__name__ = "OctetString"
_NpCfgBonjourDomainName_Object = MibScalar
npCfgBonjourDomainName = _NpCfgBonjourDomainName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 5, 46),
    _NpCfgBonjourDomainName_Type()
)
npCfgBonjourDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npCfgBonjourDomainName.setStatus("current")
_NpCfgDNSNameServerIdSecondary_Type = IpAddress
_NpCfgDNSNameServerIdSecondary_Object = MibScalar
npCfgDNSNameServerIdSecondary = _NpCfgDNSNameServerIdSecondary_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 5, 47),
    _NpCfgDNSNameServerIdSecondary_Type()
)
npCfgDNSNameServerIdSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCfgDNSNameServerIdSecondary.setStatus("current")


class _NpCfgIPv6ConfigState_Type(Integer32):
    """Custom type npCfgIPv6ConfigState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ipv6-going-down", 0),
          ("ipv6-is-up", 1))
    )


_NpCfgIPv6ConfigState_Type.__name__ = "Integer32"
_NpCfgIPv6ConfigState_Object = MibScalar
npCfgIPv6ConfigState = _NpCfgIPv6ConfigState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 5, 50),
    _NpCfgIPv6ConfigState_Type()
)
npCfgIPv6ConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npCfgIPv6ConfigState.setStatus("current")
_NpCfgIPv6DNSAddr1_Type = InetAddress
_NpCfgIPv6DNSAddr1_Object = MibScalar
npCfgIPv6DNSAddr1 = _NpCfgIPv6DNSAddr1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 5, 56),
    _NpCfgIPv6DNSAddr1_Type()
)
npCfgIPv6DNSAddr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCfgIPv6DNSAddr1.setStatus("current")
_NpCfgIPv6DNSAddr2_Type = InetAddress
_NpCfgIPv6DNSAddr2_Object = MibScalar
npCfgIPv6DNSAddr2 = _NpCfgIPv6DNSAddr2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 5, 57),
    _NpCfgIPv6DNSAddr2_Type()
)
npCfgIPv6DNSAddr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCfgIPv6DNSAddr2.setStatus("current")
_NpCfgIPConfigPrecedence_Type = OctetString
_NpCfgIPConfigPrecedence_Object = MibScalar
npCfgIPConfigPrecedence = _NpCfgIPConfigPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 5, 59),
    _NpCfgIPConfigPrecedence_Type()
)
npCfgIPConfigPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCfgIPConfigPrecedence.setStatus("current")


class _NpCfgSTAWirelessMode_Type(Integer32):
    """Custom type npCfgSTAWirelessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bg-Mode", 0),
          ("bgn-Mode", 1))
    )


_NpCfgSTAWirelessMode_Type.__name__ = "Integer32"
_NpCfgSTAWirelessMode_Object = MibScalar
npCfgSTAWirelessMode = _NpCfgSTAWirelessMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 5, 72),
    _NpCfgSTAWirelessMode_Type()
)
npCfgSTAWirelessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCfgSTAWirelessMode.setStatus("current")


class _NpCfgWiFiDirectChannelNumber_Type(Integer32):
    """Custom type npCfgWiFiDirectChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 13),
    )


_NpCfgWiFiDirectChannelNumber_Type.__name__ = "Integer32"
_NpCfgWiFiDirectChannelNumber_Object = MibScalar
npCfgWiFiDirectChannelNumber = _NpCfgWiFiDirectChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 5, 85),
    _NpCfgWiFiDirectChannelNumber_Type()
)
npCfgWiFiDirectChannelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCfgWiFiDirectChannelNumber.setStatus("current")


class _NpCfgWiFiDirectSSIDPrefix_Type(OctetString):
    """Custom type npCfgWiFiDirectSSIDPrefix based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 13),
    )


_NpCfgWiFiDirectSSIDPrefix_Type.__name__ = "OctetString"
_NpCfgWiFiDirectSSIDPrefix_Object = MibScalar
npCfgWiFiDirectSSIDPrefix = _NpCfgWiFiDirectSSIDPrefix_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 5, 86),
    _NpCfgWiFiDirectSSIDPrefix_Type()
)
npCfgWiFiDirectSSIDPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npCfgWiFiDirectSSIDPrefix.setStatus("current")


class _NpCfgWiFiDirectSSIDSuffix_Type(OctetString):
    """Custom type npCfgWiFiDirectSSIDSuffix based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_NpCfgWiFiDirectSSIDSuffix_Type.__name__ = "OctetString"
_NpCfgWiFiDirectSSIDSuffix_Object = MibScalar
npCfgWiFiDirectSSIDSuffix = _NpCfgWiFiDirectSSIDSuffix_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 5, 87),
    _NpCfgWiFiDirectSSIDSuffix_Type()
)
npCfgWiFiDirectSSIDSuffix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCfgWiFiDirectSSIDSuffix.setStatus("current")


class _NpCfgWiFiDirectConnectionSecurity_Type(Integer32):
    """Custom type npCfgWiFiDirectConnectionSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("Automatic", 0),
          ("Manual", 1),
          ("Advanced", 2))
    )


_NpCfgWiFiDirectConnectionSecurity_Type.__name__ = "Integer32"
_NpCfgWiFiDirectConnectionSecurity_Object = MibScalar
npCfgWiFiDirectConnectionSecurity = _NpCfgWiFiDirectConnectionSecurity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 5, 88),
    _NpCfgWiFiDirectConnectionSecurity_Type()
)
npCfgWiFiDirectConnectionSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCfgWiFiDirectConnectionSecurity.setStatus("optional")


class _NpCfgSysLogProtocol_Type(Integer32):
    """Custom type npCfgSysLogProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              17)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 6),
          ("udp", 17))
    )


_NpCfgSysLogProtocol_Type.__name__ = "Integer32"
_NpCfgSysLogProtocol_Object = MibScalar
npCfgSysLogProtocol = _NpCfgSysLogProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 5, 97),
    _NpCfgSysLogProtocol_Type()
)
npCfgSysLogProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCfgSysLogProtocol.setStatus("current")


class _NpCfgSysLogPort_Type(Integer32):
    """Custom type npCfgSysLogPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NpCfgSysLogPort_Type.__name__ = "Integer32"
_NpCfgSysLogPort_Object = MibScalar
npCfgSysLogPort = _NpCfgSysLogPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 5, 98),
    _NpCfgSysLogPort_Type()
)
npCfgSysLogPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCfgSysLogPort.setStatus("current")
_NpCfgHpDAPAgentManualServerAddr_Type = InetAddress
_NpCfgHpDAPAgentManualServerAddr_Object = MibScalar
npCfgHpDAPAgentManualServerAddr = _NpCfgHpDAPAgentManualServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 5, 99),
    _NpCfgHpDAPAgentManualServerAddr_Type()
)
npCfgHpDAPAgentManualServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCfgHpDAPAgentManualServerAddr.setStatus("current")
_NpTcp_ObjectIdentity = ObjectIdentity
npTcp = _NpTcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 6)
)


class _NpTcpSyslogMax_Type(Integer32):
    """Custom type npTcpSyslogMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_NpTcpSyslogMax_Type.__name__ = "Integer32"
_NpTcpSyslogMax_Object = MibScalar
npTcpSyslogMax = _NpTcpSyslogMax_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 6, 11),
    _NpTcpSyslogMax_Type()
)
npTcpSyslogMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npTcpSyslogMax.setStatus("current")


class _NpTcpAppSyslogPriority_Type(Integer32):
    """Custom type npTcpAppSyslogPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_NpTcpAppSyslogPriority_Type.__name__ = "Integer32"
_NpTcpAppSyslogPriority_Object = MibScalar
npTcpAppSyslogPriority = _NpTcpAppSyslogPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 6, 12),
    _NpTcpAppSyslogPriority_Type()
)
npTcpAppSyslogPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npTcpAppSyslogPriority.setStatus("current")
_NpCtl_ObjectIdentity = ObjectIdentity
npCtl = _NpCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 7)
)


class _NpCtlSLP_Type(Integer32):
    """Custom type npCtlSLP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NpCtlSLP_Type.__name__ = "Integer32"
_NpCtlSLP_Object = MibScalar
npCtlSLP = _NpCtlSLP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 7, 21),
    _NpCtlSLP_Type()
)
npCtlSLP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCtlSLP.setStatus("current")


class _NpCtlLPD_Type(Integer32):
    """Custom type npCtlLPD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NpCtlLPD_Type.__name__ = "Integer32"
_NpCtlLPD_Object = MibScalar
npCtlLPD = _NpCtlLPD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 7, 22),
    _NpCtlLPD_Type()
)
npCtlLPD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCtlLPD.setStatus("current")


class _NpCtl9100_Type(Integer32):
    """Custom type npCtl9100 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NpCtl9100_Type.__name__ = "Integer32"
_NpCtl9100_Object = MibScalar
npCtl9100 = _NpCtl9100_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 7, 24),
    _NpCtl9100_Type()
)
npCtl9100.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCtl9100.setStatus("current")


class _NpCtlSysLog_Type(Integer32):
    """Custom type npCtlSysLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NpCtlSysLog_Type.__name__ = "Integer32"
_NpCtlSysLog_Object = MibScalar
npCtlSysLog = _NpCtlSysLog_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 7, 26),
    _NpCtlSysLog_Type()
)
npCtlSysLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCtlSysLog.setStatus("current")


class _NpCtlSnmpVersionAccess_Type(Integer32):
    """Custom type npCtlSnmpVersionAccess based on Integer32"""
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
        *(("snmpV1RW-snmpV3RW", 1),
          ("snmpV1RO-snmpV3RW", 2),
          ("snmpV1NoAccess-snmpV3RW", 3),
          ("snmpV1RW-snmpV3NoAccess", 4),
          ("snmpV1RO-snmpV3NoAccess", 5))
    )


_NpCtlSnmpVersionAccess_Type.__name__ = "Integer32"
_NpCtlSnmpVersionAccess_Object = MibScalar
npCtlSnmpVersionAccess = _NpCtlSnmpVersionAccess_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 7, 27),
    _NpCtlSnmpVersionAccess_Type()
)
npCtlSnmpVersionAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCtlSnmpVersionAccess.setStatus("current")


class _NpCtlSnmpV3InitAccount_Type(Integer32):
    """Custom type npCtlSnmpV3InitAccount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4)
        )
    )
    namedValues = NamedValues(
        *(("Destroy", 0),
          ("blockInitEncrypt", 4))
    )


_NpCtlSnmpV3InitAccount_Type.__name__ = "Integer32"
_NpCtlSnmpV3InitAccount_Object = MibScalar
npCtlSnmpV3InitAccount = _NpCtlSnmpV3InitAccount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 7, 28),
    _NpCtlSnmpV3InitAccount_Type()
)
npCtlSnmpV3InitAccount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCtlSnmpV3InitAccount.setStatus("current")


class _NpCtlBonjour_Type(Integer32):
    """Custom type npCtlBonjour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NpCtlBonjour_Type.__name__ = "Integer32"
_NpCtlBonjour_Object = MibScalar
npCtlBonjour = _NpCtlBonjour_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 7, 29),
    _NpCtlBonjour_Type()
)
npCtlBonjour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCtlBonjour.setStatus("current")


class _NpCtlNetworkConnectionMode_Type(Integer32):
    """Custom type npCtlNetworkConnectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto-cable-detect", 1),
          ("disable-radio", 2),
          ("disable-wired", 3))
    )


_NpCtlNetworkConnectionMode_Type.__name__ = "Integer32"
_NpCtlNetworkConnectionMode_Object = MibScalar
npCtlNetworkConnectionMode = _NpCtlNetworkConnectionMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 7, 32),
    _NpCtlNetworkConnectionMode_Type()
)
npCtlNetworkConnectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCtlNetworkConnectionMode.setStatus("current")


class _NpCtlWSDiscovery_Type(Integer32):
    """Custom type npCtlWSDiscovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_NpCtlWSDiscovery_Type.__name__ = "Integer32"
_NpCtlWSDiscovery_Object = MibScalar
npCtlWSDiscovery = _NpCtlWSDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 7, 36),
    _NpCtlWSDiscovery_Type()
)
npCtlWSDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCtlWSDiscovery.setStatus("current")


class _NpCtlWSPrint_Type(Integer32):
    """Custom type npCtlWSPrint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_NpCtlWSPrint_Type.__name__ = "Integer32"
_NpCtlWSPrint_Object = MibScalar
npCtlWSPrint = _NpCtlWSPrint_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 7, 37),
    _NpCtlWSPrint_Type()
)
npCtlWSPrint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCtlWSPrint.setStatus("current")


class _NpCtlLLMNR_Type(Integer32):
    """Custom type npCtlLLMNR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_NpCtlLLMNR_Type.__name__ = "Integer32"
_NpCtlLLMNR_Object = MibScalar
npCtlLLMNR = _NpCtlLLMNR_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 7, 38),
    _NpCtlLLMNR_Type()
)
npCtlLLMNR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCtlLLMNR.setStatus("current")


class _NpCtlWPAD_Type(Integer32):
    """Custom type npCtlWPAD based on Integer32"""
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
        *(("disable", 0),
          ("automatic-Web-Proxy", 1),
          ("manual-url", 2),
          ("manual-proxy-settings", 3))
    )


_NpCtlWPAD_Type.__name__ = "Integer32"
_NpCtlWPAD_Object = MibScalar
npCtlWPAD = _NpCtlWPAD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 7, 39),
    _NpCtlWPAD_Type()
)
npCtlWPAD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCtlWPAD.setStatus("current")


class _NpCtlFpDot11WirelessState_Type(Integer32):
    """Custom type npCtlFpDot11WirelessState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("Disable", 0),
          ("Enable", 1))
    )


_NpCtlFpDot11WirelessState_Type.__name__ = "Integer32"
_NpCtlFpDot11WirelessState_Object = MibScalar
npCtlFpDot11WirelessState = _NpCtlFpDot11WirelessState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 7, 47),
    _NpCtlFpDot11WirelessState_Type()
)
npCtlFpDot11WirelessState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCtlFpDot11WirelessState.setStatus("current")


class _NpCtlDot11nSTAGuardInterval_Type(Integer32):
    """Custom type npCtlDot11nSTAGuardInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("Auto", 0),
          ("Short", 1),
          ("Long", 2))
    )


_NpCtlDot11nSTAGuardInterval_Type.__name__ = "Integer32"
_NpCtlDot11nSTAGuardInterval_Object = MibScalar
npCtlDot11nSTAGuardInterval = _NpCtlDot11nSTAGuardInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 7, 51),
    _NpCtlDot11nSTAGuardInterval_Type()
)
npCtlDot11nSTAGuardInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCtlDot11nSTAGuardInterval.setStatus("current")


class _NpCtlDot11nSTAAMSDUAggregation_Type(Integer32):
    """Custom type npCtlDot11nSTAAMSDUAggregation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("Disable", 0),
          ("Enable", 1))
    )


_NpCtlDot11nSTAAMSDUAggregation_Type.__name__ = "Integer32"
_NpCtlDot11nSTAAMSDUAggregation_Object = MibScalar
npCtlDot11nSTAAMSDUAggregation = _NpCtlDot11nSTAAMSDUAggregation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 7, 52),
    _NpCtlDot11nSTAAMSDUAggregation_Type()
)
npCtlDot11nSTAAMSDUAggregation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCtlDot11nSTAAMSDUAggregation.setStatus("current")


class _NpCtlDot11nSTABlockACKs_Type(Integer32):
    """Custom type npCtlDot11nSTABlockACKs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("Disable", 0),
          ("Enable", 1))
    )


_NpCtlDot11nSTABlockACKs_Type.__name__ = "Integer32"
_NpCtlDot11nSTABlockACKs_Object = MibScalar
npCtlDot11nSTABlockACKs = _NpCtlDot11nSTABlockACKs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 7, 53),
    _NpCtlDot11nSTABlockACKs_Type()
)
npCtlDot11nSTABlockACKs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCtlDot11nSTABlockACKs.setStatus("current")


class _NpCtlDot11nSTAAMPDUAggregation_Type(Integer32):
    """Custom type npCtlDot11nSTAAMPDUAggregation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("Disable", 0),
          ("Enable", 1))
    )


_NpCtlDot11nSTAAMPDUAggregation_Type.__name__ = "Integer32"
_NpCtlDot11nSTAAMPDUAggregation_Object = MibScalar
npCtlDot11nSTAAMPDUAggregation = _NpCtlDot11nSTAAMPDUAggregation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 7, 54),
    _NpCtlDot11nSTAAMPDUAggregation_Type()
)
npCtlDot11nSTAAMPDUAggregation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCtlDot11nSTAAMPDUAggregation.setStatus("current")


class _NpCtlWiFiDirectSSIDBroadcast_Type(Integer32):
    """Custom type npCtlWiFiDirectSSIDBroadcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-allowed", 0),
          ("allowed", 1))
    )


_NpCtlWiFiDirectSSIDBroadcast_Type.__name__ = "Integer32"
_NpCtlWiFiDirectSSIDBroadcast_Object = MibScalar
npCtlWiFiDirectSSIDBroadcast = _NpCtlWiFiDirectSSIDBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 7, 57),
    _NpCtlWiFiDirectSSIDBroadcast_Type()
)
npCtlWiFiDirectSSIDBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCtlWiFiDirectSSIDBroadcast.setStatus("current")


class _NpCtlWiFiDirectHidePassphrase_Type(Integer32):
    """Custom type npCtlWiFiDirectHidePassphrase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("show", 0),
          ("hide", 1))
    )


_NpCtlWiFiDirectHidePassphrase_Type.__name__ = "Integer32"
_NpCtlWiFiDirectHidePassphrase_Object = MibScalar
npCtlWiFiDirectHidePassphrase = _NpCtlWiFiDirectHidePassphrase_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 7, 58),
    _NpCtlWiFiDirectHidePassphrase_Type()
)
npCtlWiFiDirectHidePassphrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCtlWiFiDirectHidePassphrase.setStatus("optional")


class _NpCtlWiFiDirectHideSsid_Type(Integer32):
    """Custom type npCtlWiFiDirectHideSsid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("show", 0),
          ("hide", 1))
    )


_NpCtlWiFiDirectHideSsid_Type.__name__ = "Integer32"
_NpCtlWiFiDirectHideSsid_Object = MibScalar
npCtlWiFiDirectHideSsid = _NpCtlWiFiDirectHideSsid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 7, 59),
    _NpCtlWiFiDirectHideSsid_Type()
)
npCtlWiFiDirectHideSsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCtlWiFiDirectHideSsid.setStatus("optional")


class _NpCtlHpDAPAgentAnnounceState_Type(Integer32):
    """Custom type npCtlHpDAPAgentAnnounceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("Disable", 0),
          ("Enable", 1))
    )


_NpCtlHpDAPAgentAnnounceState_Type.__name__ = "Integer32"
_NpCtlHpDAPAgentAnnounceState_Object = MibScalar
npCtlHpDAPAgentAnnounceState = _NpCtlHpDAPAgentAnnounceState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 7, 65),
    _NpCtlHpDAPAgentAnnounceState_Type()
)
npCtlHpDAPAgentAnnounceState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCtlHpDAPAgentAnnounceState.setStatus("current")


class _NpCtlHpDAPAgentRequireTrustedAuth_Type(Integer32):
    """Custom type npCtlHpDAPAgentRequireTrustedAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("Disable", 0),
          ("Enable", 1))
    )


_NpCtlHpDAPAgentRequireTrustedAuth_Type.__name__ = "Integer32"
_NpCtlHpDAPAgentRequireTrustedAuth_Object = MibScalar
npCtlHpDAPAgentRequireTrustedAuth = _NpCtlHpDAPAgentRequireTrustedAuth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 7, 66),
    _NpCtlHpDAPAgentRequireTrustedAuth_Type()
)
npCtlHpDAPAgentRequireTrustedAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCtlHpDAPAgentRequireTrustedAuth.setStatus("current")


class _NpCtlDeviceMode_Type(Integer32):
    """Custom type npCtlDeviceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("WiredStationMode", 1),
          ("WirelessStationMode", 2),
          ("AccessPointMode", 3))
    )


_NpCtlDeviceMode_Type.__name__ = "Integer32"
_NpCtlDeviceMode_Object = MibScalar
npCtlDeviceMode = _NpCtlDeviceMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 7, 67),
    _NpCtlDeviceMode_Type()
)
npCtlDeviceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npCtlDeviceMode.setStatus("current")


class _NpCtlAirPrintStatus_Type(Integer32):
    """Custom type npCtlAirPrintStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("Disable", 0),
          ("Enable", 1))
    )


_NpCtlAirPrintStatus_Type.__name__ = "Integer32"
_NpCtlAirPrintStatus_Object = MibScalar
npCtlAirPrintStatus = _NpCtlAirPrintStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 7, 68),
    _NpCtlAirPrintStatus_Type()
)
npCtlAirPrintStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCtlAirPrintStatus.setStatus("current")


class _NpCtlWirelessSTAState_Type(Integer32):
    """Custom type npCtlWirelessSTAState based on Integer32"""
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


_NpCtlWirelessSTAState_Type.__name__ = "Integer32"
_NpCtlWirelessSTAState_Object = MibScalar
npCtlWirelessSTAState = _NpCtlWirelessSTAState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 7, 73),
    _NpCtlWirelessSTAState_Type()
)
npCtlWirelessSTAState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCtlWirelessSTAState.setStatus("current")


class _NpCtlWiFiDirectState_Type(Integer32):
    """Custom type npCtlWiFiDirectState based on Integer32"""
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


_NpCtlWiFiDirectState_Type.__name__ = "Integer32"
_NpCtlWiFiDirectState_Object = MibScalar
npCtlWiFiDirectState = _NpCtlWiFiDirectState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 7, 74),
    _NpCtlWiFiDirectState_Type()
)
npCtlWiFiDirectState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCtlWiFiDirectState.setStatus("current")
_NpCtlAirScan_Type = Integer32
_NpCtlAirScan_Object = MibScalar
npCtlAirScan = _NpCtlAirScan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 7, 79),
    _NpCtlAirScan_Type()
)
npCtlAirScan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCtlAirScan.setStatus("optional")


class _NpCtlAirFax_Type(Integer32):
    """Custom type npCtlAirFax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_NpCtlAirFax_Type.__name__ = "Integer32"
_NpCtlAirFax_Object = MibScalar
npCtlAirFax = _NpCtlAirFax_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 7, 80),
    _NpCtlAirFax_Type()
)
npCtlAirFax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCtlAirFax.setStatus("optional")


class _NpCtlGCPrint_Type(Integer32):
    """Custom type npCtlGCPrint based on Integer32"""
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
          ("remove", 2))
    )


_NpCtlGCPrint_Type.__name__ = "Integer32"
_NpCtlGCPrint_Object = MibScalar
npCtlGCPrint = _NpCtlGCPrint_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 7, 81),
    _NpCtlGCPrint_Type()
)
npCtlGCPrint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCtlGCPrint.setStatus("optional")


class _NpCtlRebootMode_Type(Integer32):
    """Custom type npCtlRebootMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("recovery", 1))
    )


_NpCtlRebootMode_Type.__name__ = "Integer32"
_NpCtlRebootMode_Object = MibScalar
npCtlRebootMode = _NpCtlRebootMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 7, 83),
    _NpCtlRebootMode_Type()
)
npCtlRebootMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCtlRebootMode.setStatus("optional")
_NpNpi_ObjectIdentity = ObjectIdentity
npNpi = _NpNpi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 8)
)
_NpNpiPeripheralAttributeEntry_ObjectIdentity = ObjectIdentity
npNpiPeripheralAttributeEntry = _NpNpiPeripheralAttributeEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 8, 3)
)


class _NpNpiPaeClass_Type(Integer32):
    """Custom type npNpiPaeClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("printer", 1),
          ("plotter", 2),
          ("xStation", 3))
    )


_NpNpiPaeClass_Type.__name__ = "Integer32"
_NpNpiPaeClass_Object = MibScalar
npNpiPaeClass = _NpNpiPaeClass_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 8, 3, 2),
    _NpNpiPaeClass_Type()
)
npNpiPaeClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npNpiPaeClass.setStatus("current")


class _NpNpiPaeIdentification_Type(Integer32):
    """Custom type npNpiPaeIdentification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5)
        )
    )
    namedValues = NamedValues(
        *(("laserjet-IIISI", 1),
          ("laserjet-4SI", 5))
    )


_NpNpiPaeIdentification_Type.__name__ = "Integer32"
_NpNpiPaeIdentification_Object = MibScalar
npNpiPaeIdentification = _NpNpiPaeIdentification_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 8, 3, 3),
    _NpNpiPaeIdentification_Type()
)
npNpiPaeIdentification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npNpiPaeIdentification.setStatus("current")
_NpIpx_ObjectIdentity = ObjectIdentity
npIpx = _NpIpx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 10)
)
_NpIpxSapInfo_Type = OctetString
_NpIpxSapInfo_Object = MibScalar
npIpxSapInfo = _NpIpxSapInfo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 10, 6),
    _NpIpxSapInfo_Type()
)
npIpxSapInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIpxSapInfo.setStatus("current")
_NpPort_ObjectIdentity = ObjectIdentity
npPort = _NpPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 13)
)


class _NpPortNumPorts_Type(Integer32):
    """Custom type npPortNumPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NpPortNumPorts_Type.__name__ = "Integer32"
_NpPortNumPorts_Object = MibScalar
npPortNumPorts = _NpPortNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 13, 1),
    _NpPortNumPorts_Type()
)
npPortNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npPortNumPorts.setStatus("current")
_NpDhcp_ObjectIdentity = ObjectIdentity
npDhcp = _NpDhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 16)
)


class _NpDhcpFQDNBehavior_Type(Integer32):
    """Custom type npDhcpFQDNBehavior based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("Present-JD-Behavior", 0),
          ("RFC4702-compliant-Behavior", 1))
    )


_NpDhcpFQDNBehavior_Type.__name__ = "Integer32"
_NpDhcpFQDNBehavior_Object = MibScalar
npDhcpFQDNBehavior = _NpDhcpFQDNBehavior_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 16, 4),
    _NpDhcpFQDNBehavior_Type()
)
npDhcpFQDNBehavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npDhcpFQDNBehavior.setStatus("current")
_NpWeb_ObjectIdentity = ObjectIdentity
npWeb = _NpWeb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 18)
)


class _NpWebProxyServerId_Type(OctetString):
    """Custom type npWebProxyServerId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NpWebProxyServerId_Type.__name__ = "OctetString"
_NpWebProxyServerId_Object = MibScalar
npWebProxyServerId = _NpWebProxyServerId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 18, 12),
    _NpWebProxyServerId_Type()
)
npWebProxyServerId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npWebProxyServerId.setStatus("current")
_NpWebProxyServerPort_Type = Integer32
_NpWebProxyServerPort_Object = MibScalar
npWebProxyServerPort = _NpWebProxyServerPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 18, 13),
    _NpWebProxyServerPort_Type()
)
npWebProxyServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npWebProxyServerPort.setStatus("current")


class _NpWebProxyUserName_Type(OctetString):
    """Custom type npWebProxyUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NpWebProxyUserName_Type.__name__ = "OctetString"
_NpWebProxyUserName_Object = MibScalar
npWebProxyUserName = _NpWebProxyUserName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 18, 14),
    _NpWebProxyUserName_Type()
)
npWebProxyUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npWebProxyUserName.setStatus("current")


class _NpWebProxyUserPasswd_Type(OctetString):
    """Custom type npWebProxyUserPasswd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NpWebProxyUserPasswd_Type.__name__ = "OctetString"
_NpWebProxyUserPasswd_Object = MibScalar
npWebProxyUserPasswd = _NpWebProxyUserPasswd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 18, 15),
    _NpWebProxyUserPasswd_Type()
)
npWebProxyUserPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npWebProxyUserPasswd.setStatus("current")
_NpSecurity_ObjectIdentity = ObjectIdentity
npSecurity = _NpSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 20)
)


class _NpSecurityDot11ServerAuthentication_Type(Integer32):
    """Custom type npSecurityDot11ServerAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("eap-md5", 1),
          ("eap-tls", 2),
          ("leap", 4),
          ("peap", 8),
          ("ttls", 16))
    )


_NpSecurityDot11ServerAuthentication_Type.__name__ = "Integer32"
_NpSecurityDot11ServerAuthentication_Object = MibScalar
npSecurityDot11ServerAuthentication = _NpSecurityDot11ServerAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 20, 1),
    _NpSecurityDot11ServerAuthentication_Type()
)
npSecurityDot11ServerAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npSecurityDot11ServerAuthentication.setStatus("current")


class _NpSecurityDot1xEapMd5Identity_Type(OctetString):
    """Custom type npSecurityDot1xEapMd5Identity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 130),
    )


_NpSecurityDot1xEapMd5Identity_Type.__name__ = "OctetString"
_NpSecurityDot1xEapMd5Identity_Object = MibScalar
npSecurityDot1xEapMd5Identity = _NpSecurityDot1xEapMd5Identity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 20, 2),
    _NpSecurityDot1xEapMd5Identity_Type()
)
npSecurityDot1xEapMd5Identity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npSecurityDot1xEapMd5Identity.setStatus("current")


class _NpSecurityDot1xTLSAuthServerId_Type(OctetString):
    """Custom type npSecurityDot1xTLSAuthServerId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NpSecurityDot1xTLSAuthServerId_Type.__name__ = "OctetString"
_NpSecurityDot1xTLSAuthServerId_Object = MibScalar
npSecurityDot1xTLSAuthServerId = _NpSecurityDot1xTLSAuthServerId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 20, 3),
    _NpSecurityDot1xTLSAuthServerId_Type()
)
npSecurityDot1xTLSAuthServerId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npSecurityDot1xTLSAuthServerId.setStatus("current")


class _NpSecurityPublicKey_Type(OctetString):
    """Custom type npSecurityPublicKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NpSecurityPublicKey_Type.__name__ = "OctetString"
_NpSecurityPublicKey_Object = MibScalar
npSecurityPublicKey = _NpSecurityPublicKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 20, 4),
    _NpSecurityPublicKey_Type()
)
npSecurityPublicKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npSecurityPublicKey.setStatus("current")


class _NpSecurityDot11EncryptedDot1xEapMd5Secret_Type(OctetString):
    """Custom type npSecurityDot11EncryptedDot1xEapMd5Secret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 130),
    )


_NpSecurityDot11EncryptedDot1xEapMd5Secret_Type.__name__ = "OctetString"
_NpSecurityDot11EncryptedDot1xEapMd5Secret_Object = MibScalar
npSecurityDot11EncryptedDot1xEapMd5Secret = _NpSecurityDot11EncryptedDot1xEapMd5Secret_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 20, 6),
    _NpSecurityDot11EncryptedDot1xEapMd5Secret_Type()
)
npSecurityDot11EncryptedDot1xEapMd5Secret.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    npSecurityDot11EncryptedDot1xEapMd5Secret.setStatus("current")
_NpSecurityDot11EncryptedWEPKeyTable_ObjectIdentity = ObjectIdentity
npSecurityDot11EncryptedWEPKeyTable = _NpSecurityDot11EncryptedWEPKeyTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 20, 7)
)
_NpSecurityDot11EncryptedWEPKeyEntry_ObjectIdentity = ObjectIdentity
npSecurityDot11EncryptedWEPKeyEntry = _NpSecurityDot11EncryptedWEPKeyEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 20, 7, 1)
)


class _NpSecurityDot11EncryptedWEPKey_Type(OctetString):
    """Custom type npSecurityDot11EncryptedWEPKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_NpSecurityDot11EncryptedWEPKey_Type.__name__ = "OctetString"
_NpSecurityDot11EncryptedWEPKey_Object = MibScalar
npSecurityDot11EncryptedWEPKey = _NpSecurityDot11EncryptedWEPKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 20, 7, 1, 2),
    _NpSecurityDot11EncryptedWEPKey_Type()
)
npSecurityDot11EncryptedWEPKey.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    npSecurityDot11EncryptedWEPKey.setStatus("current")


class _NpSecurityDot11SignalStrength_Type(Integer32):
    """Custom type npSecurityDot11SignalStrength based on Integer32"""
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
        *(("level-1-TBD", 1),
          ("level-2-TBD", 2),
          ("level-3-TBD", 3),
          ("level-4-TBD", 4),
          ("level-5-TBD", 5))
    )


_NpSecurityDot11SignalStrength_Type.__name__ = "Integer32"
_NpSecurityDot11SignalStrength_Object = MibScalar
npSecurityDot11SignalStrength = _NpSecurityDot11SignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 20, 8),
    _NpSecurityDot11SignalStrength_Type()
)
npSecurityDot11SignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npSecurityDot11SignalStrength.setStatus("current")
_NpSecurityDot11SSIDTable_ObjectIdentity = ObjectIdentity
npSecurityDot11SSIDTable = _NpSecurityDot11SSIDTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 20, 9)
)
_NpSecurityDot11SSIDEntry_ObjectIdentity = ObjectIdentity
npSecurityDot11SSIDEntry = _NpSecurityDot11SSIDEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 20, 9, 1)
)


class _NpSecurityDot11SSID_Type(OctetString):
    """Custom type npSecurityDot11SSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NpSecurityDot11SSID_Type.__name__ = "OctetString"
_NpSecurityDot11SSID_Object = MibScalar
npSecurityDot11SSID = _NpSecurityDot11SSID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 20, 9, 1, 2),
    _NpSecurityDot11SSID_Type()
)
npSecurityDot11SSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npSecurityDot11SSID.setStatus("current")
_NpSecurityDot11SSIDTableNumEntries_Type = Integer32
_NpSecurityDot11SSIDTableNumEntries_Object = MibScalar
npSecurityDot11SSIDTableNumEntries = _NpSecurityDot11SSIDTableNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 20, 10),
    _NpSecurityDot11SSIDTableNumEntries_Type()
)
npSecurityDot11SSIDTableNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npSecurityDot11SSIDTableNumEntries.setStatus("current")


class _NpSecuritySnmpV3EncryptedUserName_Type(OctetString):
    """Custom type npSecuritySnmpV3EncryptedUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )
    fixed_length = 256


_NpSecuritySnmpV3EncryptedUserName_Type.__name__ = "OctetString"
_NpSecuritySnmpV3EncryptedUserName_Object = MibScalar
npSecuritySnmpV3EncryptedUserName = _NpSecuritySnmpV3EncryptedUserName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 20, 13),
    _NpSecuritySnmpV3EncryptedUserName_Type()
)
npSecuritySnmpV3EncryptedUserName.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    npSecuritySnmpV3EncryptedUserName.setStatus("current")


class _NpSecuritySnmpV3AuthKeyPassPhrase_Type(OctetString):
    """Custom type npSecuritySnmpV3AuthKeyPassPhrase based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )
    fixed_length = 256


_NpSecuritySnmpV3AuthKeyPassPhrase_Type.__name__ = "OctetString"
_NpSecuritySnmpV3AuthKeyPassPhrase_Object = MibScalar
npSecuritySnmpV3AuthKeyPassPhrase = _NpSecuritySnmpV3AuthKeyPassPhrase_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 20, 14),
    _NpSecuritySnmpV3AuthKeyPassPhrase_Type()
)
npSecuritySnmpV3AuthKeyPassPhrase.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    npSecuritySnmpV3AuthKeyPassPhrase.setStatus("current")


class _NpSecuritySnmpV3PrivKeyPassPhrase_Type(OctetString):
    """Custom type npSecuritySnmpV3PrivKeyPassPhrase based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )
    fixed_length = 256


_NpSecuritySnmpV3PrivKeyPassPhrase_Type.__name__ = "OctetString"
_NpSecuritySnmpV3PrivKeyPassPhrase_Object = MibScalar
npSecuritySnmpV3PrivKeyPassPhrase = _NpSecuritySnmpV3PrivKeyPassPhrase_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 20, 15),
    _NpSecuritySnmpV3PrivKeyPassPhrase_Type()
)
npSecuritySnmpV3PrivKeyPassPhrase.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    npSecuritySnmpV3PrivKeyPassPhrase.setStatus("current")


class _NpSecurityDot11ExactMatchServerId_Type(Integer32):
    """Custom type npSecurityDot11ExactMatchServerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_NpSecurityDot11ExactMatchServerId_Type.__name__ = "Integer32"
_NpSecurityDot11ExactMatchServerId_Object = MibScalar
npSecurityDot11ExactMatchServerId = _NpSecurityDot11ExactMatchServerId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 20, 19),
    _NpSecurityDot11ExactMatchServerId_Type()
)
npSecurityDot11ExactMatchServerId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npSecurityDot11ExactMatchServerId.setStatus("current")


class _NpSecurityDot11EncryptionStrength_Type(Integer32):
    """Custom type npSecurityDot11EncryptionStrength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("medium", 2),
          ("high", 3))
    )


_NpSecurityDot11EncryptionStrength_Type.__name__ = "Integer32"
_NpSecurityDot11EncryptionStrength_Object = MibScalar
npSecurityDot11EncryptionStrength = _NpSecurityDot11EncryptionStrength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 20, 20),
    _NpSecurityDot11EncryptionStrength_Type()
)
npSecurityDot11EncryptionStrength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npSecurityDot11EncryptionStrength.setStatus("current")


class _NpSecuritySslRedirection_Type(Integer32):
    """Custom type npSecuritySslRedirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("redirectionEnabled", 1),
          ("redirectionDisabled", 2))
    )


_NpSecuritySslRedirection_Type.__name__ = "Integer32"
_NpSecuritySslRedirection_Object = MibScalar
npSecuritySslRedirection = _NpSecuritySslRedirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 20, 23),
    _NpSecuritySslRedirection_Type()
)
npSecuritySslRedirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npSecuritySslRedirection.setStatus("current")
_NpSecurityServicesSupported_Type = Integer32
_NpSecurityServicesSupported_Object = MibScalar
npSecurityServicesSupported = _NpSecurityServicesSupported_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 20, 27),
    _NpSecurityServicesSupported_Type()
)
npSecurityServicesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npSecurityServicesSupported.setStatus("current")
_NpSecurityDot11Encryption_Type = Integer32
_NpSecurityDot11Encryption_Object = MibScalar
npSecurityDot11Encryption = _NpSecurityDot11Encryption_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 20, 28),
    _NpSecurityDot11Encryption_Type()
)
npSecurityDot11Encryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npSecurityDot11Encryption.setStatus("current")
_NpSecurityDot11MulticastCipher_Type = Integer32
_NpSecurityDot11MulticastCipher_Object = MibScalar
npSecurityDot11MulticastCipher = _NpSecurityDot11MulticastCipher_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 20, 29),
    _NpSecurityDot11MulticastCipher_Type()
)
npSecurityDot11MulticastCipher.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npSecurityDot11MulticastCipher.setStatus("current")


class _NpSecurityDot11EncryptedWPAConfigPSKPassPhrase_Type(OctetString):
    """Custom type npSecurityDot11EncryptedWPAConfigPSKPassPhrase based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 63),
    )


_NpSecurityDot11EncryptedWPAConfigPSKPassPhrase_Type.__name__ = "OctetString"
_NpSecurityDot11EncryptedWPAConfigPSKPassPhrase_Object = MibScalar
npSecurityDot11EncryptedWPAConfigPSKPassPhrase = _NpSecurityDot11EncryptedWPAConfigPSKPassPhrase_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 20, 36),
    _NpSecurityDot11EncryptedWPAConfigPSKPassPhrase_Type()
)
npSecurityDot11EncryptedWPAConfigPSKPassPhrase.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    npSecurityDot11EncryptedWPAConfigPSKPassPhrase.setStatus("current")


class _NpSecuritySslEncryptionStrength_Type(Integer32):
    """Custom type npSecuritySslEncryptionStrength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("medium", 2),
          ("high", 3))
    )


_NpSecuritySslEncryptionStrength_Type.__name__ = "Integer32"
_NpSecuritySslEncryptionStrength_Object = MibScalar
npSecuritySslEncryptionStrength = _NpSecuritySslEncryptionStrength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 20, 40),
    _NpSecuritySslEncryptionStrength_Type()
)
npSecuritySslEncryptionStrength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npSecuritySslEncryptionStrength.setStatus("current")


class _NpSecurityDot11DynamicEncryption_Type(Integer32):
    """Custom type npSecurityDot11DynamicEncryption based on Integer32"""
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
        *(("NONE", 0),
          ("BASIC", 1),
          ("WPA", 2),
          ("WPA2", 3),
          ("AUTO", 4))
    )


_NpSecurityDot11DynamicEncryption_Type.__name__ = "Integer32"
_NpSecurityDot11DynamicEncryption_Object = MibScalar
npSecurityDot11DynamicEncryption = _NpSecurityDot11DynamicEncryption_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 20, 42),
    _NpSecurityDot11DynamicEncryption_Type()
)
npSecurityDot11DynamicEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npSecurityDot11DynamicEncryption.setStatus("current")


class _NpSecurityDot11LinkAuthentication_Type(Integer32):
    """Custom type npSecurityDot11LinkAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              128,
              143)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("shared-key", 2),
          ("leap", 128),
          ("auto", 143))
    )


_NpSecurityDot11LinkAuthentication_Type.__name__ = "Integer32"
_NpSecurityDot11LinkAuthentication_Object = MibScalar
npSecurityDot11LinkAuthentication = _NpSecurityDot11LinkAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 20, 43),
    _NpSecurityDot11LinkAuthentication_Type()
)
npSecurityDot11LinkAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npSecurityDot11LinkAuthentication.setStatus("current")


class _NpSecuritySnmpV3AuthAlgorithm_Type(Integer32):
    """Custom type npSecuritySnmpV3AuthAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("md5", 2),
          ("sha-1", 3))
    )


_NpSecuritySnmpV3AuthAlgorithm_Type.__name__ = "Integer32"
_NpSecuritySnmpV3AuthAlgorithm_Object = MibScalar
npSecuritySnmpV3AuthAlgorithm = _NpSecuritySnmpV3AuthAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 20, 44),
    _NpSecuritySnmpV3AuthAlgorithm_Type()
)
npSecuritySnmpV3AuthAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npSecuritySnmpV3AuthAlgorithm.setStatus("current")


class _NpSecuritySnmpV3PrivAlgorithm_Type(Integer32):
    """Custom type npSecuritySnmpV3PrivAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("des", 2),
          ("aes-128", 3))
    )


_NpSecuritySnmpV3PrivAlgorithm_Type.__name__ = "Integer32"
_NpSecuritySnmpV3PrivAlgorithm_Object = MibScalar
npSecuritySnmpV3PrivAlgorithm = _NpSecuritySnmpV3PrivAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 20, 45),
    _NpSecuritySnmpV3PrivAlgorithm_Type()
)
npSecuritySnmpV3PrivAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npSecuritySnmpV3PrivAlgorithm.setStatus("current")


class _NpSecuritySnmpV3PassPhrase_Type(Integer32):
    """Custom type npSecuritySnmpV3PassPhrase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("key", 0),
          ("passphrase", 1))
    )


_NpSecuritySnmpV3PassPhrase_Type.__name__ = "Integer32"
_NpSecuritySnmpV3PassPhrase_Object = MibScalar
npSecuritySnmpV3PassPhrase = _NpSecuritySnmpV3PassPhrase_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 20, 46),
    _NpSecuritySnmpV3PassPhrase_Type()
)
npSecuritySnmpV3PassPhrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npSecuritySnmpV3PassPhrase.setStatus("current")


class _NpSecurityWirelessDirectEncryptedPassPhrase_Type(OctetString):
    """Custom type npSecurityWirelessDirectEncryptedPassPhrase based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_NpSecurityWirelessDirectEncryptedPassPhrase_Type.__name__ = "OctetString"
_NpSecurityWirelessDirectEncryptedPassPhrase_Object = MibScalar
npSecurityWirelessDirectEncryptedPassPhrase = _NpSecurityWirelessDirectEncryptedPassPhrase_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 20, 55),
    _NpSecurityWirelessDirectEncryptedPassPhrase_Type()
)
npSecurityWirelessDirectEncryptedPassPhrase.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    npSecurityWirelessDirectEncryptedPassPhrase.setStatus("current")


class _NpSecurityDot1xFailSafe_Type(Integer32):
    """Custom type npSecurityDot1xFailSafe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("Disable", 0),
          ("Enable", 1))
    )


_NpSecurityDot1xFailSafe_Type.__name__ = "Integer32"
_NpSecurityDot1xFailSafe_Object = MibScalar
npSecurityDot1xFailSafe = _NpSecurityDot1xFailSafe_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 20, 57),
    _NpSecurityDot1xFailSafe_Type()
)
npSecurityDot1xFailSafe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npSecurityDot1xFailSafe.setStatus("current")
_NpSecuritySSLProtocol_Type = Integer32
_NpSecuritySSLProtocol_Object = MibScalar
npSecuritySSLProtocol = _NpSecuritySSLProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 3, 20, 58),
    _NpSecuritySSLProtocol_Type()
)
npSecuritySSLProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npSecuritySSLProtocol.setStatus("current")
_Trap_ObjectIdentity = ObjectIdentity
trap = _Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 13)
)
_TrapDest_ObjectIdentity = ObjectIdentity
trapDest = _TrapDest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 1)
)
_TrapDestinationNum_Type = Integer32
_TrapDestinationNum_Object = MibScalar
trapDestinationNum = _TrapDestinationNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 1, 1),
    _TrapDestinationNum_Type()
)
trapDestinationNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDestinationNum.setStatus("current")
_TrapTest_Type = Integer32
_TrapTest_Object = MibScalar
trapTest = _TrapTest_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 1, 3),
    _TrapTest_Type()
)
trapTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapTest.setStatus("current")
_TrapSource_Type = Integer32
_TrapSource_Object = MibScalar
trapSource = _TrapSource_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 1, 4),
    _TrapSource_Type()
)
trapSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapSource.setStatus("current")
_TrapFilterDelay_Type = Integer32
_TrapFilterDelay_Object = MibScalar
trapFilterDelay = _TrapFilterDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 1, 5),
    _TrapFilterDelay_Type()
)
trapFilterDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapFilterDelay.setStatus("current")
_TrapFQDNNum_Type = Integer32
_TrapFQDNNum_Object = MibScalar
trapFQDNNum = _TrapFQDNNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 1, 6),
    _TrapFQDNNum_Type()
)
trapFQDNNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapFQDNNum.setStatus("current")
_SnmpAccess_ObjectIdentity = ObjectIdentity
snmpAccess = _SnmpAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 15)
)
_Community_ObjectIdentity = ObjectIdentity
community = _Community_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 15, 1)
)


class _SetCommunityName_Type(OctetString):
    """Custom type setCommunityName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SetCommunityName_Type.__name__ = "OctetString"
_SetCommunityName_Object = MibScalar
setCommunityName = _SetCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 15, 1, 1),
    _SetCommunityName_Type()
)
setCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setCommunityName.setStatus("current")


class _GetCommunityName_Type(OctetString):
    """Custom type getCommunityName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GetCommunityName_Type.__name__ = "OctetString"
_GetCommunityName_Object = MibScalar
getCommunityName = _GetCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 15, 1, 2),
    _GetCommunityName_Type()
)
getCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    getCommunityName.setStatus("current")
_PpmMIB_ObjectIdentity = ObjectIdentity
ppmMIB = _PpmMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2)
)
_PpmMIBObjects_ObjectIdentity = ObjectIdentity
ppmMIBObjects = _PpmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1)
)
_PpmGeneral_ObjectIdentity = ObjectIdentity
ppmGeneral = _PpmGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 1)
)


class _PpmGeneralNaturalLanguage_Type(SnmpAdminString):
    """Custom type ppmGeneralNaturalLanguage based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PpmGeneralNaturalLanguage_Type.__name__ = "SnmpAdminString"
_PpmGeneralNaturalLanguage_Object = MibScalar
ppmGeneralNaturalLanguage = _PpmGeneralNaturalLanguage_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 1, 1),
    _PpmGeneralNaturalLanguage_Type()
)
ppmGeneralNaturalLanguage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppmGeneralNaturalLanguage.setStatus("current")


class _PpmGeneralNumberOfPrinters_Type(Gauge32):
    """Custom type ppmGeneralNumberOfPrinters based on Gauge32"""
    defaultValue = 0


_PpmGeneralNumberOfPrinters_Type.__name__ = "Gauge32"
_PpmGeneralNumberOfPrinters_Object = MibScalar
ppmGeneralNumberOfPrinters = _PpmGeneralNumberOfPrinters_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 1, 2),
    _PpmGeneralNumberOfPrinters_Type()
)
ppmGeneralNumberOfPrinters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppmGeneralNumberOfPrinters.setStatus("current")


class _PpmGeneralNumberOfPorts_Type(Gauge32):
    """Custom type ppmGeneralNumberOfPorts based on Gauge32"""
    defaultValue = 0


_PpmGeneralNumberOfPorts_Type.__name__ = "Gauge32"
_PpmGeneralNumberOfPorts_Object = MibScalar
ppmGeneralNumberOfPorts = _PpmGeneralNumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 1, 3),
    _PpmGeneralNumberOfPorts_Type()
)
ppmGeneralNumberOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppmGeneralNumberOfPorts.setStatus("current")
_PpmPrinter_ObjectIdentity = ObjectIdentity
ppmPrinter = _PpmPrinter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 2)
)
_PpmPrinterTable_ObjectIdentity = ObjectIdentity
ppmPrinterTable = _PpmPrinterTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 2, 1)
)
_PpmPrinterEntry_ObjectIdentity = ObjectIdentity
ppmPrinterEntry = _PpmPrinterEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 2, 1, 1)
)


class _PpmPrinterName_Type(SnmpAdminString):
    """Custom type ppmPrinterName based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_PpmPrinterName_Type.__name__ = "SnmpAdminString"
_PpmPrinterName_Object = MibScalar
ppmPrinterName = _PpmPrinterName_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 2, 1, 1, 2),
    _PpmPrinterName_Type()
)
ppmPrinterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppmPrinterName.setStatus("current")


class _PpmPrinterIEEE1284DeviceId_Type(OctetString):
    """Custom type ppmPrinterIEEE1284DeviceId based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1023),
    )


_PpmPrinterIEEE1284DeviceId_Type.__name__ = "OctetString"
_PpmPrinterIEEE1284DeviceId_Object = MibScalar
ppmPrinterIEEE1284DeviceId = _PpmPrinterIEEE1284DeviceId_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 2, 1, 1, 3),
    _PpmPrinterIEEE1284DeviceId_Type()
)
ppmPrinterIEEE1284DeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppmPrinterIEEE1284DeviceId.setStatus("current")


class _PpmPrinterNumberOfPorts_Type(Gauge32):
    """Custom type ppmPrinterNumberOfPorts based on Gauge32"""
    defaultValue = 0


_PpmPrinterNumberOfPorts_Type.__name__ = "Gauge32"
_PpmPrinterNumberOfPorts_Object = MibScalar
ppmPrinterNumberOfPorts = _PpmPrinterNumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 2, 1, 1, 4),
    _PpmPrinterNumberOfPorts_Type()
)
ppmPrinterNumberOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppmPrinterNumberOfPorts.setStatus("current")


class _PpmPrinterPreferredPortIndex_Type(Integer32):
    """Custom type ppmPrinterPreferredPortIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PpmPrinterPreferredPortIndex_Type.__name__ = "Integer32"
_PpmPrinterPreferredPortIndex_Object = MibScalar
ppmPrinterPreferredPortIndex = _PpmPrinterPreferredPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 2, 1, 1, 5),
    _PpmPrinterPreferredPortIndex_Type()
)
ppmPrinterPreferredPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppmPrinterPreferredPortIndex.setStatus("current")


class _PpmPrinterHrDeviceIndex_Type(Integer32):
    """Custom type ppmPrinterHrDeviceIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PpmPrinterHrDeviceIndex_Type.__name__ = "Integer32"
_PpmPrinterHrDeviceIndex_Object = MibScalar
ppmPrinterHrDeviceIndex = _PpmPrinterHrDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 2, 1, 1, 6),
    _PpmPrinterHrDeviceIndex_Type()
)
ppmPrinterHrDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppmPrinterHrDeviceIndex.setStatus("current")


class _PpmPrinterSnmpCommunityName_Type(OctetString):
    """Custom type ppmPrinterSnmpCommunityName based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PpmPrinterSnmpCommunityName_Type.__name__ = "OctetString"
_PpmPrinterSnmpCommunityName_Object = MibScalar
ppmPrinterSnmpCommunityName = _PpmPrinterSnmpCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 2, 1, 1, 7),
    _PpmPrinterSnmpCommunityName_Type()
)
ppmPrinterSnmpCommunityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppmPrinterSnmpCommunityName.setStatus("current")


class _PpmPrinterSnmpQueryEnabled_Type(TruthValue):
    """Custom type ppmPrinterSnmpQueryEnabled based on TruthValue"""
    defaultValue = 2


_PpmPrinterSnmpQueryEnabled_Type.__name__ = "TruthValue"
_PpmPrinterSnmpQueryEnabled_Object = MibScalar
ppmPrinterSnmpQueryEnabled = _PpmPrinterSnmpQueryEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 2, 1, 1, 8),
    _PpmPrinterSnmpQueryEnabled_Type()
)
ppmPrinterSnmpQueryEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppmPrinterSnmpQueryEnabled.setStatus("current")
_PpmPort_ObjectIdentity = ObjectIdentity
ppmPort = _PpmPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 3)
)
_PpmPortTable_ObjectIdentity = ObjectIdentity
ppmPortTable = _PpmPortTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 3, 1)
)
_PpmPortEntry_ObjectIdentity = ObjectIdentity
ppmPortEntry = _PpmPortEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 3, 1, 1)
)


class _PpmPortEnabled_Type(TruthValue):
    """Custom type ppmPortEnabled based on TruthValue"""
    defaultValue = 2


_PpmPortEnabled_Type.__name__ = "TruthValue"
_PpmPortEnabled_Object = MibScalar
ppmPortEnabled = _PpmPortEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 3, 1, 1, 2),
    _PpmPortEnabled_Type()
)
ppmPortEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppmPortEnabled.setStatus("current")


class _PpmPortName_Type(SnmpAdminString):
    """Custom type ppmPortName based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_PpmPortName_Type.__name__ = "SnmpAdminString"
_PpmPortName_Object = MibScalar
ppmPortName = _PpmPortName_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 3, 1, 1, 3),
    _PpmPortName_Type()
)
ppmPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppmPortName.setStatus("current")


class _PpmPortServiceNameOrURI_Type(SnmpAdminString):
    """Custom type ppmPortServiceNameOrURI based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PpmPortServiceNameOrURI_Type.__name__ = "SnmpAdminString"
_PpmPortServiceNameOrURI_Object = MibScalar
ppmPortServiceNameOrURI = _PpmPortServiceNameOrURI_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 3, 1, 1, 4),
    _PpmPortServiceNameOrURI_Type()
)
ppmPortServiceNameOrURI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppmPortServiceNameOrURI.setStatus("current")


class _PpmPortProtocolType_Type(Integer32):
    """Custom type ppmPortProtocolType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PpmPortProtocolType_Type.__name__ = "Integer32"
_PpmPortProtocolType_Object = MibScalar
ppmPortProtocolType = _PpmPortProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 3, 1, 1, 5),
    _PpmPortProtocolType_Type()
)
ppmPortProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppmPortProtocolType.setStatus("current")


class _PpmPortProtocolTargetPort_Type(Integer32):
    """Custom type ppmPortProtocolTargetPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PpmPortProtocolTargetPort_Type.__name__ = "Integer32"
_PpmPortProtocolTargetPort_Object = MibScalar
ppmPortProtocolTargetPort = _PpmPortProtocolTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 3, 1, 1, 6),
    _PpmPortProtocolTargetPort_Type()
)
ppmPortProtocolTargetPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppmPortProtocolTargetPort.setStatus("current")


class _PpmPortProtocolAltSourceEnabled_Type(TruthValue):
    """Custom type ppmPortProtocolAltSourceEnabled based on TruthValue"""
    defaultValue = 2


_PpmPortProtocolAltSourceEnabled_Type.__name__ = "TruthValue"
_PpmPortProtocolAltSourceEnabled_Object = MibScalar
ppmPortProtocolAltSourceEnabled = _PpmPortProtocolAltSourceEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 3, 1, 1, 7),
    _PpmPortProtocolAltSourceEnabled_Type()
)
ppmPortProtocolAltSourceEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppmPortProtocolAltSourceEnabled.setStatus("current")


class _PpmPortPrtChannelIndex_Type(Integer32):
    """Custom type ppmPortPrtChannelIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PpmPortPrtChannelIndex_Type.__name__ = "Integer32"
_PpmPortPrtChannelIndex_Object = MibScalar
ppmPortPrtChannelIndex = _PpmPortPrtChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 3, 1, 1, 8),
    _PpmPortPrtChannelIndex_Type()
)
ppmPortPrtChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppmPortPrtChannelIndex.setStatus("current")


class _PpmPortLprByteCountEnabled_Type(TruthValue):
    """Custom type ppmPortLprByteCountEnabled based on TruthValue"""
    defaultValue = 2


_PpmPortLprByteCountEnabled_Type.__name__ = "TruthValue"
_PpmPortLprByteCountEnabled_Object = MibScalar
ppmPortLprByteCountEnabled = _PpmPortLprByteCountEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 3, 1, 1, 9),
    _PpmPortLprByteCountEnabled_Type()
)
ppmPortLprByteCountEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppmPortLprByteCountEnabled.setStatus("current")
_SnmpV2_ObjectIdentity = ObjectIdentity
snmpV2 = _SnmpV2_ObjectIdentity(
    (1, 3, 6, 1, 6)
)
_SnmpModules_ObjectIdentity = ObjectIdentity
snmpModules = _SnmpModules_ObjectIdentity(
    (1, 3, 6, 1, 6, 3)
)
_SnmpFrameworkMIB_ObjectIdentity = ObjectIdentity
snmpFrameworkMIB = _SnmpFrameworkMIB_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 10)
)
_SnmpFrameworkMIBObjects_ObjectIdentity = ObjectIdentity
snmpFrameworkMIBObjects = _SnmpFrameworkMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 10, 2)
)
_SnmpEngine_ObjectIdentity = ObjectIdentity
snmpEngine = _SnmpEngine_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 10, 2, 1)
)
_SnmpEngineID_Type = SnmpEngineID
_SnmpEngineID_Object = MibScalar
snmpEngineID = _SnmpEngineID_Object(
    (1, 3, 6, 1, 6, 3, 10, 2, 1, 1),
    _SnmpEngineID_Type()
)
snmpEngineID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpEngineID.setStatus("current")


class _SnmpEngineBoots_Type(Integer32):
    """Custom type snmpEngineBoots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SnmpEngineBoots_Type.__name__ = "Integer32"
_SnmpEngineBoots_Object = MibScalar
snmpEngineBoots = _SnmpEngineBoots_Object(
    (1, 3, 6, 1, 6, 3, 10, 2, 1, 2),
    _SnmpEngineBoots_Type()
)
snmpEngineBoots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpEngineBoots.setStatus("current")


class _SnmpEngineTime_Type(Integer32):
    """Custom type snmpEngineTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SnmpEngineTime_Type.__name__ = "Integer32"
_SnmpEngineTime_Object = MibScalar
snmpEngineTime = _SnmpEngineTime_Object(
    (1, 3, 6, 1, 6, 3, 10, 2, 1, 3),
    _SnmpEngineTime_Type()
)
snmpEngineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpEngineTime.setStatus("current")
if mibBuilder.loadTexts:
    snmpEngineTime.setUnits("seconds")


class _SnmpEngineMaxMessageSize_Type(Integer32):
    """Custom type snmpEngineMaxMessageSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(484, 2147483647),
    )


_SnmpEngineMaxMessageSize_Type.__name__ = "Integer32"
_SnmpEngineMaxMessageSize_Object = MibScalar
snmpEngineMaxMessageSize = _SnmpEngineMaxMessageSize_Object(
    (1, 3, 6, 1, 6, 3, 10, 2, 1, 4),
    _SnmpEngineMaxMessageSize_Type()
)
snmpEngineMaxMessageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpEngineMaxMessageSize.setStatus("current")
_SnmpMPDMIB_ObjectIdentity = ObjectIdentity
snmpMPDMIB = _SnmpMPDMIB_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 11)
)
_SnmpMPDMIBObjects_ObjectIdentity = ObjectIdentity
snmpMPDMIBObjects = _SnmpMPDMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 11, 2)
)
_SnmpMPDStats_ObjectIdentity = ObjectIdentity
snmpMPDStats = _SnmpMPDStats_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 11, 2, 1)
)
_SnmpUnknownSecurityModels_Type = Counter32
_SnmpUnknownSecurityModels_Object = MibScalar
snmpUnknownSecurityModels = _SnmpUnknownSecurityModels_Object(
    (1, 3, 6, 1, 6, 3, 11, 2, 1, 1),
    _SnmpUnknownSecurityModels_Type()
)
snmpUnknownSecurityModels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpUnknownSecurityModels.setStatus("current")
_SnmpInvalidMsgs_Type = Counter32
_SnmpInvalidMsgs_Object = MibScalar
snmpInvalidMsgs = _SnmpInvalidMsgs_Object(
    (1, 3, 6, 1, 6, 3, 11, 2, 1, 2),
    _SnmpInvalidMsgs_Type()
)
snmpInvalidMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInvalidMsgs.setStatus("current")
_SnmpUnknownPDUHandlers_Type = Counter32
_SnmpUnknownPDUHandlers_Object = MibScalar
snmpUnknownPDUHandlers = _SnmpUnknownPDUHandlers_Object(
    (1, 3, 6, 1, 6, 3, 11, 2, 1, 3),
    _SnmpUnknownPDUHandlers_Type()
)
snmpUnknownPDUHandlers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpUnknownPDUHandlers.setStatus("current")
_SnmpUsmMIB_ObjectIdentity = ObjectIdentity
snmpUsmMIB = _SnmpUsmMIB_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 15)
)
_UsmMIBObjects_ObjectIdentity = ObjectIdentity
usmMIBObjects = _UsmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 15, 1)
)
_UsmStats_ObjectIdentity = ObjectIdentity
usmStats = _UsmStats_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 15, 1, 1)
)
_UsmStatsUnsupportedSecLevels_Type = Counter32
_UsmStatsUnsupportedSecLevels_Object = MibScalar
usmStatsUnsupportedSecLevels = _UsmStatsUnsupportedSecLevels_Object(
    (1, 3, 6, 1, 6, 3, 15, 1, 1, 1),
    _UsmStatsUnsupportedSecLevels_Type()
)
usmStatsUnsupportedSecLevels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usmStatsUnsupportedSecLevels.setStatus("current")
_UsmStatsNotInTimeWindows_Type = Counter32
_UsmStatsNotInTimeWindows_Object = MibScalar
usmStatsNotInTimeWindows = _UsmStatsNotInTimeWindows_Object(
    (1, 3, 6, 1, 6, 3, 15, 1, 1, 2),
    _UsmStatsNotInTimeWindows_Type()
)
usmStatsNotInTimeWindows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usmStatsNotInTimeWindows.setStatus("current")
_UsmStatsUnknownUserNames_Type = Counter32
_UsmStatsUnknownUserNames_Object = MibScalar
usmStatsUnknownUserNames = _UsmStatsUnknownUserNames_Object(
    (1, 3, 6, 1, 6, 3, 15, 1, 1, 3),
    _UsmStatsUnknownUserNames_Type()
)
usmStatsUnknownUserNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usmStatsUnknownUserNames.setStatus("current")
_UsmStatsUnknownEngineIDs_Type = Counter32
_UsmStatsUnknownEngineIDs_Object = MibScalar
usmStatsUnknownEngineIDs = _UsmStatsUnknownEngineIDs_Object(
    (1, 3, 6, 1, 6, 3, 15, 1, 1, 4),
    _UsmStatsUnknownEngineIDs_Type()
)
usmStatsUnknownEngineIDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usmStatsUnknownEngineIDs.setStatus("current")
_UsmStatsWrongDigests_Type = Counter32
_UsmStatsWrongDigests_Object = MibScalar
usmStatsWrongDigests = _UsmStatsWrongDigests_Object(
    (1, 3, 6, 1, 6, 3, 15, 1, 1, 5),
    _UsmStatsWrongDigests_Type()
)
usmStatsWrongDigests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usmStatsWrongDigests.setStatus("current")
_UsmStatsDecryptionErrors_Type = Counter32
_UsmStatsDecryptionErrors_Object = MibScalar
usmStatsDecryptionErrors = _UsmStatsDecryptionErrors_Object(
    (1, 3, 6, 1, 6, 3, 15, 1, 1, 6),
    _UsmStatsDecryptionErrors_Type()
)
usmStatsDecryptionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usmStatsDecryptionErrors.setStatus("current")
_UsmUser_ObjectIdentity = ObjectIdentity
usmUser = _UsmUser_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 15, 1, 2)
)
_UsmUserSpinLock_Type = TestAndIncr
_UsmUserSpinLock_Object = MibScalar
usmUserSpinLock = _UsmUserSpinLock_Object(
    (1, 3, 6, 1, 6, 3, 15, 1, 2, 1),
    _UsmUserSpinLock_Type()
)
usmUserSpinLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usmUserSpinLock.setStatus("current")
_UsmUserTable_ObjectIdentity = ObjectIdentity
usmUserTable = _UsmUserTable_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 15, 1, 2, 2)
)
_UsmUserEntry_ObjectIdentity = ObjectIdentity
usmUserEntry = _UsmUserEntry_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1)
)
_UsmUserSecurityName_Type = SnmpAdminString
_UsmUserSecurityName_Object = MibScalar
usmUserSecurityName = _UsmUserSecurityName_Object(
    (1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 3),
    _UsmUserSecurityName_Type()
)
usmUserSecurityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usmUserSecurityName.setStatus("current")
_UsmUserCloneFrom_Type = RowPointer
_UsmUserCloneFrom_Object = MibScalar
usmUserCloneFrom = _UsmUserCloneFrom_Object(
    (1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 4),
    _UsmUserCloneFrom_Type()
)
usmUserCloneFrom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usmUserCloneFrom.setStatus("current")
_UsmUserAuthProtocol_Type = AutonomousType
_UsmUserAuthProtocol_Object = MibScalar
usmUserAuthProtocol = _UsmUserAuthProtocol_Object(
    (1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 5),
    _UsmUserAuthProtocol_Type()
)
usmUserAuthProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usmUserAuthProtocol.setStatus("current")


class _UsmUserAuthKeyChange_Type(KeyChange):
    """Custom type usmUserAuthKeyChange based on KeyChange"""
    defaultHexValue = ""


_UsmUserAuthKeyChange_Type.__name__ = "KeyChange"
_UsmUserAuthKeyChange_Object = MibScalar
usmUserAuthKeyChange = _UsmUserAuthKeyChange_Object(
    (1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 6),
    _UsmUserAuthKeyChange_Type()
)
usmUserAuthKeyChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usmUserAuthKeyChange.setStatus("current")


class _UsmUserOwnAuthKeyChange_Type(KeyChange):
    """Custom type usmUserOwnAuthKeyChange based on KeyChange"""
    defaultHexValue = ""


_UsmUserOwnAuthKeyChange_Type.__name__ = "KeyChange"
_UsmUserOwnAuthKeyChange_Object = MibScalar
usmUserOwnAuthKeyChange = _UsmUserOwnAuthKeyChange_Object(
    (1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 7),
    _UsmUserOwnAuthKeyChange_Type()
)
usmUserOwnAuthKeyChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usmUserOwnAuthKeyChange.setStatus("current")
_UsmUserPrivProtocol_Type = AutonomousType
_UsmUserPrivProtocol_Object = MibScalar
usmUserPrivProtocol = _UsmUserPrivProtocol_Object(
    (1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 8),
    _UsmUserPrivProtocol_Type()
)
usmUserPrivProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usmUserPrivProtocol.setStatus("current")


class _UsmUserPrivKeyChange_Type(KeyChange):
    """Custom type usmUserPrivKeyChange based on KeyChange"""
    defaultHexValue = ""


_UsmUserPrivKeyChange_Type.__name__ = "KeyChange"
_UsmUserPrivKeyChange_Object = MibScalar
usmUserPrivKeyChange = _UsmUserPrivKeyChange_Object(
    (1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 9),
    _UsmUserPrivKeyChange_Type()
)
usmUserPrivKeyChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usmUserPrivKeyChange.setStatus("current")


class _UsmUserOwnPrivKeyChange_Type(KeyChange):
    """Custom type usmUserOwnPrivKeyChange based on KeyChange"""
    defaultHexValue = ""


_UsmUserOwnPrivKeyChange_Type.__name__ = "KeyChange"
_UsmUserOwnPrivKeyChange_Object = MibScalar
usmUserOwnPrivKeyChange = _UsmUserOwnPrivKeyChange_Object(
    (1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 10),
    _UsmUserOwnPrivKeyChange_Type()
)
usmUserOwnPrivKeyChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usmUserOwnPrivKeyChange.setStatus("current")


class _UsmUserPublic_Type(OctetString):
    """Custom type usmUserPublic based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UsmUserPublic_Type.__name__ = "OctetString"
_UsmUserPublic_Object = MibScalar
usmUserPublic = _UsmUserPublic_Object(
    (1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 11),
    _UsmUserPublic_Type()
)
usmUserPublic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usmUserPublic.setStatus("current")


class _UsmUserStorageType_Type(StorageType):
    """Custom type usmUserStorageType based on StorageType"""
    defaultValue = 3


_UsmUserStorageType_Type.__name__ = "StorageType"
_UsmUserStorageType_Object = MibScalar
usmUserStorageType = _UsmUserStorageType_Object(
    (1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 12),
    _UsmUserStorageType_Type()
)
usmUserStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usmUserStorageType.setStatus("current")
_UsmUserStatus_Type = RowStatus
_UsmUserStatus_Object = MibScalar
usmUserStatus = _UsmUserStatus_Object(
    (1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 13),
    _UsmUserStatus_Type()
)
usmUserStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usmUserStatus.setStatus("current")
_SnmpVacmMIB_ObjectIdentity = ObjectIdentity
snmpVacmMIB = _SnmpVacmMIB_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 16)
)
_VacmMIBObjects_ObjectIdentity = ObjectIdentity
vacmMIBObjects = _VacmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 16, 1)
)
_VacmContextTable_ObjectIdentity = ObjectIdentity
vacmContextTable = _VacmContextTable_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 16, 1, 1)
)
_VacmContextEntry_ObjectIdentity = ObjectIdentity
vacmContextEntry = _VacmContextEntry_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 16, 1, 1, 1)
)


class _VacmContextName_Type(SnmpAdminString):
    """Custom type vacmContextName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VacmContextName_Type.__name__ = "SnmpAdminString"
_VacmContextName_Object = MibScalar
vacmContextName = _VacmContextName_Object(
    (1, 3, 6, 1, 6, 3, 16, 1, 1, 1, 1),
    _VacmContextName_Type()
)
vacmContextName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vacmContextName.setStatus("current")
_VacmSecurityToGroupTable_ObjectIdentity = ObjectIdentity
vacmSecurityToGroupTable = _VacmSecurityToGroupTable_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 16, 1, 2)
)
_VacmSecurityToGroupEntry_ObjectIdentity = ObjectIdentity
vacmSecurityToGroupEntry = _VacmSecurityToGroupEntry_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 16, 1, 2, 1)
)


class _VacmGroupName_Type(SnmpAdminString):
    """Custom type vacmGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_VacmGroupName_Type.__name__ = "SnmpAdminString"
_VacmGroupName_Object = MibScalar
vacmGroupName = _VacmGroupName_Object(
    (1, 3, 6, 1, 6, 3, 16, 1, 2, 1, 3),
    _VacmGroupName_Type()
)
vacmGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vacmGroupName.setStatus("current")


class _VacmSecurityToGroupStorageType_Type(StorageType):
    """Custom type vacmSecurityToGroupStorageType based on StorageType"""
    defaultValue = 3


_VacmSecurityToGroupStorageType_Type.__name__ = "StorageType"
_VacmSecurityToGroupStorageType_Object = MibScalar
vacmSecurityToGroupStorageType = _VacmSecurityToGroupStorageType_Object(
    (1, 3, 6, 1, 6, 3, 16, 1, 2, 1, 4),
    _VacmSecurityToGroupStorageType_Type()
)
vacmSecurityToGroupStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vacmSecurityToGroupStorageType.setStatus("current")
_VacmSecurityToGroupStatus_Type = RowStatus
_VacmSecurityToGroupStatus_Object = MibScalar
vacmSecurityToGroupStatus = _VacmSecurityToGroupStatus_Object(
    (1, 3, 6, 1, 6, 3, 16, 1, 2, 1, 5),
    _VacmSecurityToGroupStatus_Type()
)
vacmSecurityToGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vacmSecurityToGroupStatus.setStatus("current")
_VacmAccessTable_ObjectIdentity = ObjectIdentity
vacmAccessTable = _VacmAccessTable_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 16, 1, 4)
)
_VacmAccessEntry_ObjectIdentity = ObjectIdentity
vacmAccessEntry = _VacmAccessEntry_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 16, 1, 4, 1)
)


class _VacmAccessContextMatch_Type(Integer32):
    """Custom type vacmAccessContextMatch based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exact", 1),
          ("prefix", 2))
    )


_VacmAccessContextMatch_Type.__name__ = "Integer32"
_VacmAccessContextMatch_Object = MibScalar
vacmAccessContextMatch = _VacmAccessContextMatch_Object(
    (1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 4),
    _VacmAccessContextMatch_Type()
)
vacmAccessContextMatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vacmAccessContextMatch.setStatus("current")


class _VacmAccessReadViewName_Type(SnmpAdminString):
    """Custom type vacmAccessReadViewName based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VacmAccessReadViewName_Type.__name__ = "SnmpAdminString"
_VacmAccessReadViewName_Object = MibScalar
vacmAccessReadViewName = _VacmAccessReadViewName_Object(
    (1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 5),
    _VacmAccessReadViewName_Type()
)
vacmAccessReadViewName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vacmAccessReadViewName.setStatus("current")


class _VacmAccessWriteViewName_Type(SnmpAdminString):
    """Custom type vacmAccessWriteViewName based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VacmAccessWriteViewName_Type.__name__ = "SnmpAdminString"
_VacmAccessWriteViewName_Object = MibScalar
vacmAccessWriteViewName = _VacmAccessWriteViewName_Object(
    (1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 6),
    _VacmAccessWriteViewName_Type()
)
vacmAccessWriteViewName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vacmAccessWriteViewName.setStatus("current")


class _VacmAccessNotifyViewName_Type(SnmpAdminString):
    """Custom type vacmAccessNotifyViewName based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VacmAccessNotifyViewName_Type.__name__ = "SnmpAdminString"
_VacmAccessNotifyViewName_Object = MibScalar
vacmAccessNotifyViewName = _VacmAccessNotifyViewName_Object(
    (1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 7),
    _VacmAccessNotifyViewName_Type()
)
vacmAccessNotifyViewName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vacmAccessNotifyViewName.setStatus("current")


class _VacmAccessStorageType_Type(StorageType):
    """Custom type vacmAccessStorageType based on StorageType"""
    defaultValue = 3


_VacmAccessStorageType_Type.__name__ = "StorageType"
_VacmAccessStorageType_Object = MibScalar
vacmAccessStorageType = _VacmAccessStorageType_Object(
    (1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 8),
    _VacmAccessStorageType_Type()
)
vacmAccessStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vacmAccessStorageType.setStatus("current")
_VacmAccessStatus_Type = RowStatus
_VacmAccessStatus_Object = MibScalar
vacmAccessStatus = _VacmAccessStatus_Object(
    (1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 9),
    _VacmAccessStatus_Type()
)
vacmAccessStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vacmAccessStatus.setStatus("current")
_VacmMIBViews_ObjectIdentity = ObjectIdentity
vacmMIBViews = _VacmMIBViews_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 16, 1, 5)
)
_VacmViewSpinLock_Type = TestAndIncr
_VacmViewSpinLock_Object = MibScalar
vacmViewSpinLock = _VacmViewSpinLock_Object(
    (1, 3, 6, 1, 6, 3, 16, 1, 5, 1),
    _VacmViewSpinLock_Type()
)
vacmViewSpinLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vacmViewSpinLock.setStatus("current")
_VacmViewTreeFamilyTable_ObjectIdentity = ObjectIdentity
vacmViewTreeFamilyTable = _VacmViewTreeFamilyTable_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 16, 1, 5, 2)
)
_VacmViewTreeFamilyEntry_ObjectIdentity = ObjectIdentity
vacmViewTreeFamilyEntry = _VacmViewTreeFamilyEntry_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 16, 1, 5, 2, 1)
)


class _VacmViewTreeFamilyMask_Type(OctetString):
    """Custom type vacmViewTreeFamilyMask based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VacmViewTreeFamilyMask_Type.__name__ = "OctetString"
_VacmViewTreeFamilyMask_Object = MibScalar
vacmViewTreeFamilyMask = _VacmViewTreeFamilyMask_Object(
    (1, 3, 6, 1, 6, 3, 16, 1, 5, 2, 1, 3),
    _VacmViewTreeFamilyMask_Type()
)
vacmViewTreeFamilyMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vacmViewTreeFamilyMask.setStatus("current")


class _VacmViewTreeFamilyType_Type(Integer32):
    """Custom type vacmViewTreeFamilyType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("included", 1),
          ("excluded", 2))
    )


_VacmViewTreeFamilyType_Type.__name__ = "Integer32"
_VacmViewTreeFamilyType_Object = MibScalar
vacmViewTreeFamilyType = _VacmViewTreeFamilyType_Object(
    (1, 3, 6, 1, 6, 3, 16, 1, 5, 2, 1, 4),
    _VacmViewTreeFamilyType_Type()
)
vacmViewTreeFamilyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vacmViewTreeFamilyType.setStatus("current")


class _VacmViewTreeFamilyStorageType_Type(StorageType):
    """Custom type vacmViewTreeFamilyStorageType based on StorageType"""
    defaultValue = 3


_VacmViewTreeFamilyStorageType_Type.__name__ = "StorageType"
_VacmViewTreeFamilyStorageType_Object = MibScalar
vacmViewTreeFamilyStorageType = _VacmViewTreeFamilyStorageType_Object(
    (1, 3, 6, 1, 6, 3, 16, 1, 5, 2, 1, 5),
    _VacmViewTreeFamilyStorageType_Type()
)
vacmViewTreeFamilyStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vacmViewTreeFamilyStorageType.setStatus("current")
_VacmViewTreeFamilyStatus_Type = RowStatus
_VacmViewTreeFamilyStatus_Object = MibScalar
vacmViewTreeFamilyStatus = _VacmViewTreeFamilyStatus_Object(
    (1, 3, 6, 1, 6, 3, 16, 1, 5, 2, 1, 6),
    _VacmViewTreeFamilyStatus_Type()
)
vacmViewTreeFamilyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vacmViewTreeFamilyStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-PAGEWIDE-PRO-477DW-MFP-MIB",
    **{"ieee802dot11": ieee802dot11,
       "dot11smt": dot11smt,
       "dot11StationConfigTable": dot11StationConfigTable,
       "dot11StationConfigEntry": dot11StationConfigEntry,
       "dot11DesiredSSID": dot11DesiredSSID,
       "dot11DesiredBSSType": dot11DesiredBSSType,
       "dot11AuthenticationAlgorithmsTable": dot11AuthenticationAlgorithmsTable,
       "dot11AuthenticationAlgorithmsEntry": dot11AuthenticationAlgorithmsEntry,
       "dot11AuthenticationAlgorithm": dot11AuthenticationAlgorithm,
       "dot11AuthenticationAlgorithmsEnable": dot11AuthenticationAlgorithmsEnable,
       "dot11WEPDefaultKeysTable": dot11WEPDefaultKeysTable,
       "dot11WEPDefaultKeysEntry": dot11WEPDefaultKeysEntry,
       "dot11WEPDefaultKeyValue": dot11WEPDefaultKeyValue,
       "dot11PrivacyTable": dot11PrivacyTable,
       "dot11PrivacyEntry": dot11PrivacyEntry,
       "dot11PrivacyInvoked": dot11PrivacyInvoked,
       "dot11WEPDefaultKeyID": dot11WEPDefaultKeyID,
       "dot11phy": dot11phy,
       "dot11PhyOperationTable": dot11PhyOperationTable,
       "dot11PhyOperationEntry": dot11PhyOperationEntry,
       "dot11CurrentRegDomain": dot11CurrentRegDomain,
       "ieee802dot11i": ieee802dot11i,
       "dot11RSNConfigAuthenticationSuitesTable": dot11RSNConfigAuthenticationSuitesTable,
       "dot11RSNConfigAuthenticationSuitesEntry": dot11RSNConfigAuthenticationSuitesEntry,
       "dot11RSNConfigAuthenticationSuite": dot11RSNConfigAuthenticationSuite,
       "dot11RSNConfigAuthenticationSuiteEnabled": dot11RSNConfigAuthenticationSuiteEnabled,
       "org": org,
       "dod": dod,
       "internet": internet,
       "mgmt": mgmt,
       "mib-2": mib_2,
       "system": system,
       "sysDescr": sysDescr,
       "sysObjectID": sysObjectID,
       "sysUpTime": sysUpTime,
       "sysContact": sysContact,
       "sysName": sysName,
       "sysLocation": sysLocation,
       "sysServices": sysServices,
       "sysORLastChange": sysORLastChange,
       "interfaces": interfaces,
       "ifNumber": ifNumber,
       "ifTable": ifTable,
       "ifEntry": ifEntry,
       "ifIndex": ifIndex,
       "ifDescr": ifDescr,
       "ifType": ifType,
       "ifMtu": ifMtu,
       "ifSpeed": ifSpeed,
       "ifPhysAddress": ifPhysAddress,
       "ifAdminStatus": ifAdminStatus,
       "ifOperStatus": ifOperStatus,
       "ifLastChange": ifLastChange,
       "ifInOctets": ifInOctets,
       "ifInUcastPkts": ifInUcastPkts,
       "ifInNUcastPkts": ifInNUcastPkts,
       "ifInDiscards": ifInDiscards,
       "ifInErrors": ifInErrors,
       "ifInUnknownProtos": ifInUnknownProtos,
       "ifOutOctets": ifOutOctets,
       "ifOutUcastPkts": ifOutUcastPkts,
       "ifOutNUcastPkts": ifOutNUcastPkts,
       "ifOutDiscards": ifOutDiscards,
       "ifOutErrors": ifOutErrors,
       "ifOutQLen": ifOutQLen,
       "ifSpecific": ifSpecific,
       "ip": ip,
       "ipForwarding": ipForwarding,
       "ipDefaultTTL": ipDefaultTTL,
       "ipInReceives": ipInReceives,
       "ipInHdrErrors": ipInHdrErrors,
       "ipInAddrErrors": ipInAddrErrors,
       "ipForwDatagrams": ipForwDatagrams,
       "ipInUnknownProtos": ipInUnknownProtos,
       "ipInDiscards": ipInDiscards,
       "ipInDelivers": ipInDelivers,
       "ipOutRequests": ipOutRequests,
       "ipOutDiscards": ipOutDiscards,
       "ipOutNoRoutes": ipOutNoRoutes,
       "ipReasmTimeout": ipReasmTimeout,
       "ipReasmReqds": ipReasmReqds,
       "ipReasmOKs": ipReasmOKs,
       "ipReasmFails": ipReasmFails,
       "ipFragOKs": ipFragOKs,
       "ipFragFails": ipFragFails,
       "ipFragCreates": ipFragCreates,
       "ipAddrTable": ipAddrTable,
       "ipAddrEntry": ipAddrEntry,
       "ipAdEntAddr": ipAdEntAddr,
       "ipAdEntIfIndex": ipAdEntIfIndex,
       "ipAdEntNetMask": ipAdEntNetMask,
       "ipAdEntBcastAddr": ipAdEntBcastAddr,
       "ipRouteTable": ipRouteTable,
       "ipRouteEntry": ipRouteEntry,
       "ipRouteDest": ipRouteDest,
       "ipRouteIfIndex": ipRouteIfIndex,
       "ipRouteMetric1": ipRouteMetric1,
       "ipRouteNextHop": ipRouteNextHop,
       "ipRouteType": ipRouteType,
       "ipRouteProto": ipRouteProto,
       "ipRouteMask": ipRouteMask,
       "ipRouteInfo": ipRouteInfo,
       "ipNetToMediaTable": ipNetToMediaTable,
       "ipNetToMediaEntry": ipNetToMediaEntry,
       "ipNetToMediaIfIndex": ipNetToMediaIfIndex,
       "ipNetToMediaPhysAddress": ipNetToMediaPhysAddress,
       "ipNetToMediaNetAddress": ipNetToMediaNetAddress,
       "ipNetToMediaType": ipNetToMediaType,
       "ipRoutingDiscards": ipRoutingDiscards,
       "snmp": snmp,
       "snmpInPkts": snmpInPkts,
       "snmpOutPkts": snmpOutPkts,
       "snmpInBadVersions": snmpInBadVersions,
       "snmpInBadCommunityNames": snmpInBadCommunityNames,
       "snmpInBadCommunityUses": snmpInBadCommunityUses,
       "snmpInASNParseErrs": snmpInASNParseErrs,
       "snmpInTooBigs": snmpInTooBigs,
       "snmpInNoSuchNames": snmpInNoSuchNames,
       "snmpInBadValues": snmpInBadValues,
       "snmpInReadOnlys": snmpInReadOnlys,
       "snmpInGenErrs": snmpInGenErrs,
       "snmpInTotalReqVars": snmpInTotalReqVars,
       "snmpInTotalSetVars": snmpInTotalSetVars,
       "snmpInGetRequests": snmpInGetRequests,
       "snmpInGetNexts": snmpInGetNexts,
       "snmpInSetRequests": snmpInSetRequests,
       "snmpInGetResponses": snmpInGetResponses,
       "snmpInTraps": snmpInTraps,
       "snmpOutTooBigs": snmpOutTooBigs,
       "snmpOutNoSuchNames": snmpOutNoSuchNames,
       "snmpOutBadValues": snmpOutBadValues,
       "snmpOutGenErrs": snmpOutGenErrs,
       "snmpOutGetRequests": snmpOutGetRequests,
       "snmpOutGetNexts": snmpOutGetNexts,
       "snmpOutSetRequests": snmpOutSetRequests,
       "snmpOutGetResponses": snmpOutGetResponses,
       "snmpOutTraps": snmpOutTraps,
       "snmpEnableAuthenTraps": snmpEnableAuthenTraps,
       "snmpSilentDrops": snmpSilentDrops,
       "snmpProxyDrops": snmpProxyDrops,
       "host": host,
       "hrSystem": hrSystem,
       "hrSystemUptime": hrSystemUptime,
       "hrSystemDate": hrSystemDate,
       "hrSystemInitialLoadDevice": hrSystemInitialLoadDevice,
       "hrSystemInitialLoadParameters": hrSystemInitialLoadParameters,
       "hrSystemNumUsers": hrSystemNumUsers,
       "hrSystemProcesses": hrSystemProcesses,
       "hrSystemMaxProcesses": hrSystemMaxProcesses,
       "hrStorage": hrStorage,
       "hrMemorySize": hrMemorySize,
       "hrStorageTable": hrStorageTable,
       "hrStorageEntry": hrStorageEntry,
       "hrStorageIndex": hrStorageIndex,
       "hrStorageType": hrStorageType,
       "hrStorageDescr": hrStorageDescr,
       "hrStorageAllocationUnits": hrStorageAllocationUnits,
       "hrStorageSize": hrStorageSize,
       "hrStorageUsed": hrStorageUsed,
       "hrDevice": hrDevice,
       "hrDeviceTable": hrDeviceTable,
       "hrDeviceEntry": hrDeviceEntry,
       "hrDeviceIndex": hrDeviceIndex,
       "hrDeviceType": hrDeviceType,
       "hrDeviceDescr": hrDeviceDescr,
       "hrDeviceID": hrDeviceID,
       "hrDeviceStatus": hrDeviceStatus,
       "hrDeviceErrors": hrDeviceErrors,
       "hrPrinterTable": hrPrinterTable,
       "hrPrinterEntry": hrPrinterEntry,
       "hrPrinterStatus": hrPrinterStatus,
       "hrPrinterDetectedErrorState": hrPrinterDetectedErrorState,
       "ifMIB": ifMIB,
       "ifMIBObjects": ifMIBObjects,
       "ifTableLastChange": ifTableLastChange,
       "printmib": printmib,
       "prtGeneral": prtGeneral,
       "prtGeneralTable": prtGeneralTable,
       "prtGeneralEntry": prtGeneralEntry,
       "prtGeneralConfigChanges": prtGeneralConfigChanges,
       "prtGeneralCurrentLocalization": prtGeneralCurrentLocalization,
       "prtGeneralReset": prtGeneralReset,
       "prtGeneralCurrentOperator": prtGeneralCurrentOperator,
       "prtGeneralServicePerson": prtGeneralServicePerson,
       "prtInputDefaultIndex": prtInputDefaultIndex,
       "prtOutputDefaultIndex": prtOutputDefaultIndex,
       "prtMarkerDefaultIndex": prtMarkerDefaultIndex,
       "prtMediaPathDefaultIndex": prtMediaPathDefaultIndex,
       "prtConsoleLocalization": prtConsoleLocalization,
       "prtConsoleNumberOfDisplayLines": prtConsoleNumberOfDisplayLines,
       "prtGeneralPrinterName": prtGeneralPrinterName,
       "prtGeneralSerialNumber": prtGeneralSerialNumber,
       "prtCover": prtCover,
       "prtCoverTable": prtCoverTable,
       "prtCoverEntry": prtCoverEntry,
       "prtCoverDescription": prtCoverDescription,
       "prtCoverStatus": prtCoverStatus,
       "prtLocalization": prtLocalization,
       "prtLocalizationTable": prtLocalizationTable,
       "prtLocalizationEntry": prtLocalizationEntry,
       "prtLocalizationLanguage": prtLocalizationLanguage,
       "prtLocalizationCountry": prtLocalizationCountry,
       "prtLocalizationCharacterSet": prtLocalizationCharacterSet,
       "prtInput": prtInput,
       "prtInputTable": prtInputTable,
       "prtInputEntry": prtInputEntry,
       "prtInputType": prtInputType,
       "prtInputDimUnit": prtInputDimUnit,
       "prtInputMediaDimFeedDirDeclared": prtInputMediaDimFeedDirDeclared,
       "prtInputMediaDimXFeedDirDeclared": prtInputMediaDimXFeedDirDeclared,
       "prtInputMediaDimFeedDirChosen": prtInputMediaDimFeedDirChosen,
       "prtInputMediaDimXFeedDirChosen": prtInputMediaDimXFeedDirChosen,
       "prtInputCapacityUnit": prtInputCapacityUnit,
       "prtInputMaxCapacity": prtInputMaxCapacity,
       "prtInputCurrentLevel": prtInputCurrentLevel,
       "prtInputStatus": prtInputStatus,
       "prtInputMediaName": prtInputMediaName,
       "prtInputName": prtInputName,
       "prtInputVendorName": prtInputVendorName,
       "prtInputModel": prtInputModel,
       "prtInputVersion": prtInputVersion,
       "prtInputSerialNumber": prtInputSerialNumber,
       "prtInputDescription": prtInputDescription,
       "prtInputSecurity": prtInputSecurity,
       "prtInputMediaWeight": prtInputMediaWeight,
       "prtInputMediaType": prtInputMediaType,
       "prtInputMediaColor": prtInputMediaColor,
       "prtInputMediaFormParts": prtInputMediaFormParts,
       "prtInputMediaLoadTimeout": prtInputMediaLoadTimeout,
       "prtOutput": prtOutput,
       "prtOutputTable": prtOutputTable,
       "prtOutputEntry": prtOutputEntry,
       "prtOutputType": prtOutputType,
       "prtOutputCapacityUnit": prtOutputCapacityUnit,
       "prtOutputMaxCapacity": prtOutputMaxCapacity,
       "prtOutputRemainingCapacity": prtOutputRemainingCapacity,
       "prtOutputStatus": prtOutputStatus,
       "prtOutputName": prtOutputName,
       "prtOutputVendorName": prtOutputVendorName,
       "prtOutputModel": prtOutputModel,
       "prtOutputVersion": prtOutputVersion,
       "prtOutputSerialNumber": prtOutputSerialNumber,
       "prtOutputDescription": prtOutputDescription,
       "prtOutputSecurity": prtOutputSecurity,
       "prtOutputDimUnit": prtOutputDimUnit,
       "prtOutputMaxDimFeedDir": prtOutputMaxDimFeedDir,
       "prtOutputMaxDimXFeedDir": prtOutputMaxDimXFeedDir,
       "prtOutputMinDimFeedDir": prtOutputMinDimFeedDir,
       "prtOutputMinDimXFeedDir": prtOutputMinDimXFeedDir,
       "prtOutputStackingOrder": prtOutputStackingOrder,
       "prtOutputPageDeliveryOrientation": prtOutputPageDeliveryOrientation,
       "prtOutputBursting": prtOutputBursting,
       "prtOutputDecollating": prtOutputDecollating,
       "prtOutputPageCollated": prtOutputPageCollated,
       "prtOutputOffsetStacking": prtOutputOffsetStacking,
       "prtMarker": prtMarker,
       "prtMarkerTable": prtMarkerTable,
       "prtMarkerEntry": prtMarkerEntry,
       "prtMarkerMarkTech": prtMarkerMarkTech,
       "prtMarkerCounterUnit": prtMarkerCounterUnit,
       "prtMarkerLifeCount": prtMarkerLifeCount,
       "prtMarkerPowerOnCount": prtMarkerPowerOnCount,
       "prtMarkerProcessColorants": prtMarkerProcessColorants,
       "prtMarkerSpotColorants": prtMarkerSpotColorants,
       "prtMarkerAddressabilityUnit": prtMarkerAddressabilityUnit,
       "prtMarkerAddressabilityFeedDir": prtMarkerAddressabilityFeedDir,
       "prtMarkerAddressabilityXFeedDir": prtMarkerAddressabilityXFeedDir,
       "prtMarkerNorthMargin": prtMarkerNorthMargin,
       "prtMarkerSouthMargin": prtMarkerSouthMargin,
       "prtMarkerWestMargin": prtMarkerWestMargin,
       "prtMarkerEastMargin": prtMarkerEastMargin,
       "prtMarkerStatus": prtMarkerStatus,
       "prtMarkerSupplies": prtMarkerSupplies,
       "prtMarkerSuppliesTable": prtMarkerSuppliesTable,
       "prtMarkerSuppliesEntry": prtMarkerSuppliesEntry,
       "prtMarkerSuppliesMarkerIndex": prtMarkerSuppliesMarkerIndex,
       "prtMarkerSuppliesColorantIndex": prtMarkerSuppliesColorantIndex,
       "prtMarkerSuppliesClass": prtMarkerSuppliesClass,
       "prtMarkerSuppliesType": prtMarkerSuppliesType,
       "prtMarkerSuppliesDescription": prtMarkerSuppliesDescription,
       "prtMarkerSuppliesSupplyUnit": prtMarkerSuppliesSupplyUnit,
       "prtMarkerSuppliesMaxCapacity": prtMarkerSuppliesMaxCapacity,
       "prtMarkerSuppliesLevel": prtMarkerSuppliesLevel,
       "prtMarkerColorant": prtMarkerColorant,
       "prtMarkerColorantTable": prtMarkerColorantTable,
       "prtMarkerColorantEntry": prtMarkerColorantEntry,
       "prtMarkerColorantMarkerIndex": prtMarkerColorantMarkerIndex,
       "prtMarkerColorantRole": prtMarkerColorantRole,
       "prtMarkerColorantValue": prtMarkerColorantValue,
       "prtMarkerColorantTonality": prtMarkerColorantTonality,
       "prtMediaPath": prtMediaPath,
       "prtMediaPathTable": prtMediaPathTable,
       "prtMediaPathEntry": prtMediaPathEntry,
       "prtMediaPathMaxSpeedPrintUnit": prtMediaPathMaxSpeedPrintUnit,
       "prtMediaPathMediaSizeUnit": prtMediaPathMediaSizeUnit,
       "prtMediaPathMaxSpeed": prtMediaPathMaxSpeed,
       "prtMediaPathMaxMediaFeedDir": prtMediaPathMaxMediaFeedDir,
       "prtMediaPathMaxMediaXFeedDir": prtMediaPathMaxMediaXFeedDir,
       "prtMediaPathMinMediaFeedDir": prtMediaPathMinMediaFeedDir,
       "prtMediaPathMinMediaXFeedDir": prtMediaPathMinMediaXFeedDir,
       "prtMediaPathType": prtMediaPathType,
       "prtMediaPathDescription": prtMediaPathDescription,
       "prtMediaPathStatus": prtMediaPathStatus,
       "prtChannel": prtChannel,
       "prtChannelTable": prtChannelTable,
       "prtChannelEntry": prtChannelEntry,
       "prtChannelType": prtChannelType,
       "prtChannelProtocolVersion": prtChannelProtocolVersion,
       "prtChannelCurrentJobCntlLangIndex": prtChannelCurrentJobCntlLangIndex,
       "prtChannelDefaultPageDescLangIndex": prtChannelDefaultPageDescLangIndex,
       "prtChannelState": prtChannelState,
       "prtChannelIfIndex": prtChannelIfIndex,
       "prtChannelStatus": prtChannelStatus,
       "prtChannelInformation": prtChannelInformation,
       "prtInterpreter": prtInterpreter,
       "prtInterpreterTable": prtInterpreterTable,
       "prtInterpreterEntry": prtInterpreterEntry,
       "prtInterpreterLangFamily": prtInterpreterLangFamily,
       "prtInterpreterLangLevel": prtInterpreterLangLevel,
       "prtInterpreterLangVersion": prtInterpreterLangVersion,
       "prtInterpreterDescription": prtInterpreterDescription,
       "prtInterpreterVersion": prtInterpreterVersion,
       "prtInterpreterDefaultOrientation": prtInterpreterDefaultOrientation,
       "prtInterpreterFeedAddressability": prtInterpreterFeedAddressability,
       "prtInterpreterXFeedAddressability": prtInterpreterXFeedAddressability,
       "prtInterpreterDefaultCharSetIn": prtInterpreterDefaultCharSetIn,
       "prtInterpreterDefaultCharSetOut": prtInterpreterDefaultCharSetOut,
       "prtInterpreterTwoWay": prtInterpreterTwoWay,
       "prtConsoleDisplayBuffer": prtConsoleDisplayBuffer,
       "prtConsoleDisplayBufferTable": prtConsoleDisplayBufferTable,
       "prtConsoleDisplayBufferEntry": prtConsoleDisplayBufferEntry,
       "prtConsoleDisplayBufferText": prtConsoleDisplayBufferText,
       "private": private,
       "enterprises": enterprises,
       "hpPrintServer": hpPrintServer,
       "nm": nm,
       "nm-system": nm_system,
       "netPeripheral": netPeripheral,
       "netPrinter": netPrinter,
       "generalDeviceStatus": generalDeviceStatus,
       "gdStatusEntry": gdStatusEntry,
       "gdStatusLineState": gdStatusLineState,
       "gdStatusPaperOut": gdStatusPaperOut,
       "gdStatusPaperJam": gdStatusPaperJam,
       "gdStatusBusy": gdStatusBusy,
       "gdStatusWait": gdStatusWait,
       "gdStatusInitialize": gdStatusInitialize,
       "gdStatusDoorOpen": gdStatusDoorOpen,
       "gdStatusPrinting": gdStatusPrinting,
       "gdStatusPaperOutput": gdStatusPaperOutput,
       "gdStatusDisplay": gdStatusDisplay,
       "gdStatusId": gdStatusId,
       "gdStatusJobTimeout": gdStatusJobTimeout,
       "gdPasswords": gdPasswords,
       "netPML": netPML,
       "netPMLmgmt": netPMLmgmt,
       "device": device,
       "device-system": device_system,
       "settings-system": settings_system,
       "energy-star": energy_star,
       "sleep-mode": sleep_mode,
       "speed-energy-usage": speed_energy_usage,
       "start-engine-early-warmup": start_engine_early_warmup,
       "enable-engine-early-warmup": enable_engine_early_warmup,
       "status-system": status_system,
       "install-date": install_date,
       "date-and-time": date_and_time,
       "id": id,
       "model-number": model_number,
       "model-name": model_name,
       "serial-number": serial_number,
       "fw-rom-datecode": fw_rom_datecode,
       "fw-rom-revision": fw_rom_revision,
       "device-name": device_name,
       "device-location": device_location,
       "asset-number": asset_number,
       "test": test,
       "print-internal-page": print_internal_page,
       "job": job,
       "settings-job": settings_job,
       "cancel-job": cancel_job,
       "encryption-password-type": encryption_password_type,
       "encryption-password-max-length": encryption_password_max_length,
       "encryption-password-min-length": encryption_password_min_length,
       "job-storage-supported": job_storage_supported,
       "job-storage-type": job_storage_type,
       "job-storage-mode": job_storage_mode,
       "job-storage-available": job_storage_available,
       "job-storage-encryption": job_storage_encryption,
       "active-print-jobs": active_print_jobs,
       "job-being-parsed": job_being_parsed,
       "current-job-parsing-id": current_job_parsing_id,
       "errorlog": errorlog,
       "error1": error1,
       "error1-time-stamp": error1_time_stamp,
       "error1-code": error1_code,
       "error1-date-time": error1_date_time,
       "error2": error2,
       "error2-time-stamp": error2_time_stamp,
       "error2-code": error2_code,
       "error2-date-time": error2_date_time,
       "error3": error3,
       "error3-time-stamp": error3_time_stamp,
       "error3-code": error3_code,
       "error3-date-time": error3_date_time,
       "error4": error4,
       "error4-time-stamp": error4_time_stamp,
       "error4-code": error4_code,
       "error4-date-time": error4_date_time,
       "error5": error5,
       "error5-time-stamp": error5_time_stamp,
       "error5-code": error5_code,
       "error5-date-time": error5_date_time,
       "error6": error6,
       "error6-time-stamp": error6_time_stamp,
       "error6-code": error6_code,
       "error6-date-time": error6_date_time,
       "error7": error7,
       "error7-time-stamp": error7_time_stamp,
       "error7-code": error7_code,
       "error7-date-time": error7_date_time,
       "error8": error8,
       "error8-time-stamp": error8_time_stamp,
       "error8-code": error8_code,
       "error8-date-time": error8_date_time,
       "error9": error9,
       "error9-time-stamp": error9_time_stamp,
       "error9-code": error9_code,
       "error9-date-time": error9_date_time,
       "error10": error10,
       "error10-time-stamp": error10_time_stamp,
       "error10-code": error10_code,
       "error10-date-time": error10_date_time,
       "error11": error11,
       "error11-time-stamp": error11_time_stamp,
       "error11-code": error11_code,
       "error11-date-time": error11_date_time,
       "error12": error12,
       "error12-time-stamp": error12_time_stamp,
       "error12-code": error12_code,
       "error12-date-time": error12_date_time,
       "error13": error13,
       "error13-time-stamp": error13_time_stamp,
       "error13-code": error13_code,
       "error13-date-time": error13_date_time,
       "error14": error14,
       "error14-time-stamp": error14_time_stamp,
       "error14-code": error14_code,
       "error14-date-time": error14_date_time,
       "error15": error15,
       "error15-time-stamp": error15_time_stamp,
       "error15-code": error15_code,
       "error15-date-time": error15_date_time,
       "accounting": accounting,
       "printer-accounting": printer_accounting,
       "printed-media-usage": printed_media_usage,
       "printed-media-simplex-count": printed_media_simplex_count,
       "printed-media-duplex-count": printed_media_duplex_count,
       "usage-printer-total-charge": usage_printer_total_charge,
       "usage-average-toner-coverage": usage_average_toner_coverage,
       "usage-staple-count": usage_staple_count,
       "usage-printer-mono-total-charge": usage_printer_mono_total_charge,
       "usage-printer-color-total-charge": usage_printer_color_total_charge,
       "print-meter-equivalent-impression-count": print_meter_equivalent_impression_count,
       "scanner-accounting": scanner_accounting,
       "usage-scanner-total-charge": usage_scanner_total_charge,
       "printer-color-accounting": printer_color_accounting,
       "printed-media-color-usage": printed_media_color_usage,
       "printed-media-color-simplex-count": printed_media_color_simplex_count,
       "printed-media-color-duplex-count": printed_media_color_duplex_count,
       "source-subsystem": source_subsystem,
       "scanner": scanner,
       "settings-scanner": settings_scanner,
       "scanner-accessory-adf-sheet-count": scanner_accessory_adf_sheet_count,
       "scanner-accessory-flatbed-scan-count": scanner_accessory_flatbed_scan_count,
       "scanner-accessory-copy-job-scan-count": scanner_accessory_copy_job_scan_count,
       "scanner-accessory-send-job-scan-count": scanner_accessory_send_job_scan_count,
       "scanner-accessory-total-copy-pages-printed": scanner_accessory_total_copy_pages_printed,
       "scan-to-folder-count": scan_to_folder_count,
       "fax-job-scan-count": fax_job_scan_count,
       "scanner-accessory-total-copy-mono-pages-printed": scanner_accessory_total_copy_mono_pages_printed,
       "scanner-accessory-total-copy-color-pages-printed": scanner_accessory_total_copy_color_pages_printed,
       "processing-subsystem": processing_subsystem,
       "pdl": pdl,
       "pdl-pcl": pdl_pcl,
       "pcl-total-page-count": pcl_total_page_count,
       "pdl-postscript": pdl_postscript,
       "postscript-total-page-count": postscript_total_page_count,
       "fax-proc-sub": fax_proc_sub,
       "settings-fax-proc-sub": settings_fax_proc_sub,
       "fax-print-page-count": fax_print_page_count,
       "status-fax-proc-sub": status_fax_proc_sub,
       "afax-send-page-count": afax_send_page_count,
       "afax-recv-page-count": afax_recv_page_count,
       "destination-subsystem": destination_subsystem,
       "print-engine": print_engine,
       "status-prt-eng": status_prt_eng,
       "total-engine-page-count": total_engine_page_count,
       "total-mono-page-count": total_mono_page_count,
       "total-color-page-count": total_color_page_count,
       "duplex-page-count": duplex_page_count,
       "intray": intray,
       "status-intray": status_intray,
       "not-ready-tray-empty": not_ready_tray_empty,
       "intrays": intrays,
       "intray1": intray1,
       "tray1-media-size-loaded": tray1_media_size_loaded,
       "tray1-media-name": tray1_media_name,
       "tray1-custom-media-width": tray1_custom_media_width,
       "tray1-custom-media-length": tray1_custom_media_length,
       "tray1-type": tray1_type,
       "tray1-media-key": tray1_media_key,
       "intray2": intray2,
       "tray2-media-size-loaded": tray2_media_size_loaded,
       "tray2-media-name": tray2_media_name,
       "tray2-custom-media-width": tray2_custom_media_width,
       "tray2-custom-media-length": tray2_custom_media_length,
       "tray2-type": tray2_type,
       "tray2-media-key": tray2_media_key,
       "intray3": intray3,
       "tray3-media-size-loaded": tray3_media_size_loaded,
       "tray3-media-name": tray3_media_name,
       "tray3-custom-media-width": tray3_custom_media_width,
       "tray3-custom-media-length": tray3_custom_media_length,
       "tray3-type": tray3_type,
       "tray3-media-key": tray3_media_key,
       "intray5": intray5,
       "tray5-media-size-loaded": tray5_media_size_loaded,
       "tray5-media-name": tray5_media_name,
       "tray5-custom-media-width": tray5_custom_media_width,
       "tray5-custom-media-length": tray5_custom_media_length,
       "tray5-type": tray5_type,
       "tray5-media-key": tray5_media_key,
       "print-media": print_media,
       "settings-print-media": settings_print_media,
       "media-names-enabled": media_names_enabled,
       "media-info": media_info,
       "media1": media1,
       "media1-name": media1_name,
       "media2": media2,
       "media2-name": media2_name,
       "media3": media3,
       "media3-name": media3_name,
       "media4": media4,
       "media4-name": media4_name,
       "media5": media5,
       "media5-name": media5_name,
       "media6": media6,
       "media6-name": media6_name,
       "media7": media7,
       "media7-name": media7_name,
       "media8": media8,
       "media8-name": media8_name,
       "media9": media9,
       "media9-name": media9_name,
       "media10": media10,
       "media10-name": media10_name,
       "media11": media11,
       "media11-name": media11_name,
       "media12": media12,
       "media12-name": media12_name,
       "media13": media13,
       "media13-name": media13_name,
       "media14": media14,
       "media14-name": media14_name,
       "media15": media15,
       "media15-name": media15_name,
       "media16": media16,
       "media16-name": media16_name,
       "media17": media17,
       "media17-name": media17_name,
       "media18": media18,
       "media18-name": media18_name,
       "media19": media19,
       "media19-name": media19_name,
       "consumables": consumables,
       "consumables-1": consumables_1,
       "consumable-status": consumable_status,
       "consumable-status-cartridge-model": consumable_status_cartridge_model,
       "consumable-status-manufacturing-date": consumable_status_manufacturing_date,
       "consumable-status-serial-number": consumable_status_serial_number,
       "consumable-status-first-install-date": consumable_status_first_install_date,
       "interface": interface,
       "npCard": npCard,
       "npSys": npSys,
       "npSysModelNumber": npSysModelNumber,
       "npSysCardServices1": npSysCardServices1,
       "npSysCardServices2": npSysCardServices2,
       "npSysCardServices3": npSysCardServices3,
       "npCfg": npCfg,
       "npCfgSource": npCfgSource,
       "npCfgYiaddr": npCfgYiaddr,
       "npCfgSiaddr": npCfgSiaddr,
       "npCfgLogServer": npCfgLogServer,
       "npCfgSubnetMask": npCfgSubnetMask,
       "npCfgDefaultGateway": npCfgDefaultGateway,
       "npCfgDomainName": npCfgDomainName,
       "npCfgIPP": npCfgIPP,
       "npCfgDNSNameServerId": npCfgDNSNameServerId,
       "npCfgWINSNameServerIdPri": npCfgWINSNameServerIdPri,
       "npCfgWINSNameServerIdSec": npCfgWINSNameServerIdSec,
       "npCfgPasswd1": npCfgPasswd1,
       "npCfgLinkType": npCfgLinkType,
       "npCfgSnmpDefaultReadCmnty": npCfgSnmpDefaultReadCmnty,
       "npCfgBonjourServiceName": npCfgBonjourServiceName,
       "npCfgBonjourHighestPriorityService": npCfgBonjourHighestPriorityService,
       "npCfgBonjourDomainName": npCfgBonjourDomainName,
       "npCfgDNSNameServerIdSecondary": npCfgDNSNameServerIdSecondary,
       "npCfgIPv6ConfigState": npCfgIPv6ConfigState,
       "npCfgIPv6DNSAddr1": npCfgIPv6DNSAddr1,
       "npCfgIPv6DNSAddr2": npCfgIPv6DNSAddr2,
       "npCfgIPConfigPrecedence": npCfgIPConfigPrecedence,
       "npCfgSTAWirelessMode": npCfgSTAWirelessMode,
       "npCfgWiFiDirectChannelNumber": npCfgWiFiDirectChannelNumber,
       "npCfgWiFiDirectSSIDPrefix": npCfgWiFiDirectSSIDPrefix,
       "npCfgWiFiDirectSSIDSuffix": npCfgWiFiDirectSSIDSuffix,
       "npCfgWiFiDirectConnectionSecurity": npCfgWiFiDirectConnectionSecurity,
       "npCfgSysLogProtocol": npCfgSysLogProtocol,
       "npCfgSysLogPort": npCfgSysLogPort,
       "npCfgHpDAPAgentManualServerAddr": npCfgHpDAPAgentManualServerAddr,
       "npTcp": npTcp,
       "npTcpSyslogMax": npTcpSyslogMax,
       "npTcpAppSyslogPriority": npTcpAppSyslogPriority,
       "npCtl": npCtl,
       "npCtlSLP": npCtlSLP,
       "npCtlLPD": npCtlLPD,
       "npCtl9100": npCtl9100,
       "npCtlSysLog": npCtlSysLog,
       "npCtlSnmpVersionAccess": npCtlSnmpVersionAccess,
       "npCtlSnmpV3InitAccount": npCtlSnmpV3InitAccount,
       "npCtlBonjour": npCtlBonjour,
       "npCtlNetworkConnectionMode": npCtlNetworkConnectionMode,
       "npCtlWSDiscovery": npCtlWSDiscovery,
       "npCtlWSPrint": npCtlWSPrint,
       "npCtlLLMNR": npCtlLLMNR,
       "npCtlWPAD": npCtlWPAD,
       "npCtlFpDot11WirelessState": npCtlFpDot11WirelessState,
       "npCtlDot11nSTAGuardInterval": npCtlDot11nSTAGuardInterval,
       "npCtlDot11nSTAAMSDUAggregation": npCtlDot11nSTAAMSDUAggregation,
       "npCtlDot11nSTABlockACKs": npCtlDot11nSTABlockACKs,
       "npCtlDot11nSTAAMPDUAggregation": npCtlDot11nSTAAMPDUAggregation,
       "npCtlWiFiDirectSSIDBroadcast": npCtlWiFiDirectSSIDBroadcast,
       "npCtlWiFiDirectHidePassphrase": npCtlWiFiDirectHidePassphrase,
       "npCtlWiFiDirectHideSsid": npCtlWiFiDirectHideSsid,
       "npCtlHpDAPAgentAnnounceState": npCtlHpDAPAgentAnnounceState,
       "npCtlHpDAPAgentRequireTrustedAuth": npCtlHpDAPAgentRequireTrustedAuth,
       "npCtlDeviceMode": npCtlDeviceMode,
       "npCtlAirPrintStatus": npCtlAirPrintStatus,
       "npCtlWirelessSTAState": npCtlWirelessSTAState,
       "npCtlWiFiDirectState": npCtlWiFiDirectState,
       "npCtlAirScan": npCtlAirScan,
       "npCtlAirFax": npCtlAirFax,
       "npCtlGCPrint": npCtlGCPrint,
       "npCtlRebootMode": npCtlRebootMode,
       "npNpi": npNpi,
       "npNpiPeripheralAttributeEntry": npNpiPeripheralAttributeEntry,
       "npNpiPaeClass": npNpiPaeClass,
       "npNpiPaeIdentification": npNpiPaeIdentification,
       "npIpx": npIpx,
       "npIpxSapInfo": npIpxSapInfo,
       "npPort": npPort,
       "npPortNumPorts": npPortNumPorts,
       "npDhcp": npDhcp,
       "npDhcpFQDNBehavior": npDhcpFQDNBehavior,
       "npWeb": npWeb,
       "npWebProxyServerId": npWebProxyServerId,
       "npWebProxyServerPort": npWebProxyServerPort,
       "npWebProxyUserName": npWebProxyUserName,
       "npWebProxyUserPasswd": npWebProxyUserPasswd,
       "npSecurity": npSecurity,
       "npSecurityDot11ServerAuthentication": npSecurityDot11ServerAuthentication,
       "npSecurityDot1xEapMd5Identity": npSecurityDot1xEapMd5Identity,
       "npSecurityDot1xTLSAuthServerId": npSecurityDot1xTLSAuthServerId,
       "npSecurityPublicKey": npSecurityPublicKey,
       "npSecurityDot11EncryptedDot1xEapMd5Secret": npSecurityDot11EncryptedDot1xEapMd5Secret,
       "npSecurityDot11EncryptedWEPKeyTable": npSecurityDot11EncryptedWEPKeyTable,
       "npSecurityDot11EncryptedWEPKeyEntry": npSecurityDot11EncryptedWEPKeyEntry,
       "npSecurityDot11EncryptedWEPKey": npSecurityDot11EncryptedWEPKey,
       "npSecurityDot11SignalStrength": npSecurityDot11SignalStrength,
       "npSecurityDot11SSIDTable": npSecurityDot11SSIDTable,
       "npSecurityDot11SSIDEntry": npSecurityDot11SSIDEntry,
       "npSecurityDot11SSID": npSecurityDot11SSID,
       "npSecurityDot11SSIDTableNumEntries": npSecurityDot11SSIDTableNumEntries,
       "npSecuritySnmpV3EncryptedUserName": npSecuritySnmpV3EncryptedUserName,
       "npSecuritySnmpV3AuthKeyPassPhrase": npSecuritySnmpV3AuthKeyPassPhrase,
       "npSecuritySnmpV3PrivKeyPassPhrase": npSecuritySnmpV3PrivKeyPassPhrase,
       "npSecurityDot11ExactMatchServerId": npSecurityDot11ExactMatchServerId,
       "npSecurityDot11EncryptionStrength": npSecurityDot11EncryptionStrength,
       "npSecuritySslRedirection": npSecuritySslRedirection,
       "npSecurityServicesSupported": npSecurityServicesSupported,
       "npSecurityDot11Encryption": npSecurityDot11Encryption,
       "npSecurityDot11MulticastCipher": npSecurityDot11MulticastCipher,
       "npSecurityDot11EncryptedWPAConfigPSKPassPhrase": npSecurityDot11EncryptedWPAConfigPSKPassPhrase,
       "npSecuritySslEncryptionStrength": npSecuritySslEncryptionStrength,
       "npSecurityDot11DynamicEncryption": npSecurityDot11DynamicEncryption,
       "npSecurityDot11LinkAuthentication": npSecurityDot11LinkAuthentication,
       "npSecuritySnmpV3AuthAlgorithm": npSecuritySnmpV3AuthAlgorithm,
       "npSecuritySnmpV3PrivAlgorithm": npSecuritySnmpV3PrivAlgorithm,
       "npSecuritySnmpV3PassPhrase": npSecuritySnmpV3PassPhrase,
       "npSecurityWirelessDirectEncryptedPassPhrase": npSecurityWirelessDirectEncryptedPassPhrase,
       "npSecurityDot1xFailSafe": npSecurityDot1xFailSafe,
       "npSecuritySSLProtocol": npSecuritySSLProtocol,
       "trap": trap,
       "trapDest": trapDest,
       "trapDestinationNum": trapDestinationNum,
       "trapTest": trapTest,
       "trapSource": trapSource,
       "trapFilterDelay": trapFilterDelay,
       "trapFQDNNum": trapFQDNNum,
       "snmpAccess": snmpAccess,
       "community": community,
       "setCommunityName": setCommunityName,
       "getCommunityName": getCommunityName,
       "ppmMIB": ppmMIB,
       "ppmMIBObjects": ppmMIBObjects,
       "ppmGeneral": ppmGeneral,
       "ppmGeneralNaturalLanguage": ppmGeneralNaturalLanguage,
       "ppmGeneralNumberOfPrinters": ppmGeneralNumberOfPrinters,
       "ppmGeneralNumberOfPorts": ppmGeneralNumberOfPorts,
       "ppmPrinter": ppmPrinter,
       "ppmPrinterTable": ppmPrinterTable,
       "ppmPrinterEntry": ppmPrinterEntry,
       "ppmPrinterName": ppmPrinterName,
       "ppmPrinterIEEE1284DeviceId": ppmPrinterIEEE1284DeviceId,
       "ppmPrinterNumberOfPorts": ppmPrinterNumberOfPorts,
       "ppmPrinterPreferredPortIndex": ppmPrinterPreferredPortIndex,
       "ppmPrinterHrDeviceIndex": ppmPrinterHrDeviceIndex,
       "ppmPrinterSnmpCommunityName": ppmPrinterSnmpCommunityName,
       "ppmPrinterSnmpQueryEnabled": ppmPrinterSnmpQueryEnabled,
       "ppmPort": ppmPort,
       "ppmPortTable": ppmPortTable,
       "ppmPortEntry": ppmPortEntry,
       "ppmPortEnabled": ppmPortEnabled,
       "ppmPortName": ppmPortName,
       "ppmPortServiceNameOrURI": ppmPortServiceNameOrURI,
       "ppmPortProtocolType": ppmPortProtocolType,
       "ppmPortProtocolTargetPort": ppmPortProtocolTargetPort,
       "ppmPortProtocolAltSourceEnabled": ppmPortProtocolAltSourceEnabled,
       "ppmPortPrtChannelIndex": ppmPortPrtChannelIndex,
       "ppmPortLprByteCountEnabled": ppmPortLprByteCountEnabled,
       "snmpV2": snmpV2,
       "snmpModules": snmpModules,
       "snmpFrameworkMIB": snmpFrameworkMIB,
       "snmpFrameworkMIBObjects": snmpFrameworkMIBObjects,
       "snmpEngine": snmpEngine,
       "snmpEngineID": snmpEngineID,
       "snmpEngineBoots": snmpEngineBoots,
       "snmpEngineTime": snmpEngineTime,
       "snmpEngineMaxMessageSize": snmpEngineMaxMessageSize,
       "snmpMPDMIB": snmpMPDMIB,
       "snmpMPDMIBObjects": snmpMPDMIBObjects,
       "snmpMPDStats": snmpMPDStats,
       "snmpUnknownSecurityModels": snmpUnknownSecurityModels,
       "snmpInvalidMsgs": snmpInvalidMsgs,
       "snmpUnknownPDUHandlers": snmpUnknownPDUHandlers,
       "snmpUsmMIB": snmpUsmMIB,
       "usmMIBObjects": usmMIBObjects,
       "usmStats": usmStats,
       "usmStatsUnsupportedSecLevels": usmStatsUnsupportedSecLevels,
       "usmStatsNotInTimeWindows": usmStatsNotInTimeWindows,
       "usmStatsUnknownUserNames": usmStatsUnknownUserNames,
       "usmStatsUnknownEngineIDs": usmStatsUnknownEngineIDs,
       "usmStatsWrongDigests": usmStatsWrongDigests,
       "usmStatsDecryptionErrors": usmStatsDecryptionErrors,
       "usmUser": usmUser,
       "usmUserSpinLock": usmUserSpinLock,
       "usmUserTable": usmUserTable,
       "usmUserEntry": usmUserEntry,
       "usmUserSecurityName": usmUserSecurityName,
       "usmUserCloneFrom": usmUserCloneFrom,
       "usmUserAuthProtocol": usmUserAuthProtocol,
       "usmUserAuthKeyChange": usmUserAuthKeyChange,
       "usmUserOwnAuthKeyChange": usmUserOwnAuthKeyChange,
       "usmUserPrivProtocol": usmUserPrivProtocol,
       "usmUserPrivKeyChange": usmUserPrivKeyChange,
       "usmUserOwnPrivKeyChange": usmUserOwnPrivKeyChange,
       "usmUserPublic": usmUserPublic,
       "usmUserStorageType": usmUserStorageType,
       "usmUserStatus": usmUserStatus,
       "snmpVacmMIB": snmpVacmMIB,
       "vacmMIBObjects": vacmMIBObjects,
       "vacmContextTable": vacmContextTable,
       "vacmContextEntry": vacmContextEntry,
       "vacmContextName": vacmContextName,
       "vacmSecurityToGroupTable": vacmSecurityToGroupTable,
       "vacmSecurityToGroupEntry": vacmSecurityToGroupEntry,
       "vacmGroupName": vacmGroupName,
       "vacmSecurityToGroupStorageType": vacmSecurityToGroupStorageType,
       "vacmSecurityToGroupStatus": vacmSecurityToGroupStatus,
       "vacmAccessTable": vacmAccessTable,
       "vacmAccessEntry": vacmAccessEntry,
       "vacmAccessContextMatch": vacmAccessContextMatch,
       "vacmAccessReadViewName": vacmAccessReadViewName,
       "vacmAccessWriteViewName": vacmAccessWriteViewName,
       "vacmAccessNotifyViewName": vacmAccessNotifyViewName,
       "vacmAccessStorageType": vacmAccessStorageType,
       "vacmAccessStatus": vacmAccessStatus,
       "vacmMIBViews": vacmMIBViews,
       "vacmViewSpinLock": vacmViewSpinLock,
       "vacmViewTreeFamilyTable": vacmViewTreeFamilyTable,
       "vacmViewTreeFamilyEntry": vacmViewTreeFamilyEntry,
       "vacmViewTreeFamilyMask": vacmViewTreeFamilyMask,
       "vacmViewTreeFamilyType": vacmViewTreeFamilyType,
       "vacmViewTreeFamilyStorageType": vacmViewTreeFamilyStorageType,
       "vacmViewTreeFamilyStatus": vacmViewTreeFamilyStatus}
)
