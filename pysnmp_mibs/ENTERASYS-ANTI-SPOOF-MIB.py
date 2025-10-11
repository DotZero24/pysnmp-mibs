# SNMP MIB module (ENTERASYS-ANTI-SPOOF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/enterasys/ENTERASYS-ANTI-SPOOF-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:47:01 2025
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

etsysAntiSpoofMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96)
)
if mibBuilder.loadTexts:
    etsysAntiSpoofMIB.setRevisions(
        ("2013-01-15 16:31",
         "2012-10-31 13:55")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AntiSpoofPortAction(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("generateSyslog", 0),
          ("generateNotification", 1),
          ("quarantineUser", 2))
    )


class AntiSpoofInspectionType(TextualConvention, Integer32):
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
        *(("enabled", 1),
          ("disabled", 2),
          ("inspectionOnly", 3))
    )



class AntiSpoofThresholdType(TextualConvention, Integer32):
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
        *(("ipv4Change", 1),
          ("ipv6Change", 2),
          ("portChange", 3))
    )



class AntiSpoofPortType(TextualConvention, Integer32):
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
        *(("trusted", 1),
          ("bypass", 2),
          ("untrusted", 3))
    )



class AntiSpoofBindingType(TextualConvention, Integer32):
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
        *(("dhcp", 1),
          ("arp", 2),
          ("ip", 3))
    )



class EtsysInstanceOID(TextualConvention, ObjectIdentifier):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_EtsysAntiSpoofObjects_ObjectIdentity = ObjectIdentity
etsysAntiSpoofObjects = _EtsysAntiSpoofObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1)
)
_EtsysAntiSpoofNotificationBranch_ObjectIdentity = ObjectIdentity
etsysAntiSpoofNotificationBranch = _EtsysAntiSpoofNotificationBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 0)
)
_EtsysAntiSpoofSystemBranch_ObjectIdentity = ObjectIdentity
etsysAntiSpoofSystemBranch = _EtsysAntiSpoofSystemBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 1)
)


class _EtsysAntiSpoofSystemState_Type(EnabledStatus):
    """Custom type etsysAntiSpoofSystemState based on EnabledStatus"""
    defaultValue = 2


_EtsysAntiSpoofSystemState_Type.__name__ = "EnabledStatus"
_EtsysAntiSpoofSystemState_Object = MibScalar
etsysAntiSpoofSystemState = _EtsysAntiSpoofSystemState_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 1, 1),
    _EtsysAntiSpoofSystemState_Type()
)
etsysAntiSpoofSystemState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysAntiSpoofSystemState.setStatus("current")
_EtsysAntiSpoofMaxClassIndex_Type = Unsigned32
_EtsysAntiSpoofMaxClassIndex_Object = MibScalar
etsysAntiSpoofMaxClassIndex = _EtsysAntiSpoofMaxClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 1, 2),
    _EtsysAntiSpoofMaxClassIndex_Type()
)
etsysAntiSpoofMaxClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysAntiSpoofMaxClassIndex.setStatus("current")
_EtsysAntiSpoofMaxClassThresholdIndex_Type = Unsigned32
_EtsysAntiSpoofMaxClassThresholdIndex_Object = MibScalar
etsysAntiSpoofMaxClassThresholdIndex = _EtsysAntiSpoofMaxClassThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 1, 3),
    _EtsysAntiSpoofMaxClassThresholdIndex_Type()
)
etsysAntiSpoofMaxClassThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysAntiSpoofMaxClassThresholdIndex.setStatus("current")


class _EtsysAntiSpoofSystemSnmpNotifications_Type(EnabledStatus):
    """Custom type etsysAntiSpoofSystemSnmpNotifications based on EnabledStatus"""
    defaultValue = 1


_EtsysAntiSpoofSystemSnmpNotifications_Type.__name__ = "EnabledStatus"
_EtsysAntiSpoofSystemSnmpNotifications_Object = MibScalar
etsysAntiSpoofSystemSnmpNotifications = _EtsysAntiSpoofSystemSnmpNotifications_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 1, 4),
    _EtsysAntiSpoofSystemSnmpNotifications_Type()
)
etsysAntiSpoofSystemSnmpNotifications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysAntiSpoofSystemSnmpNotifications.setStatus("current")


class _EtsysAntiSpoofSystemNotificationInterval_Type(Unsigned32):
    """Custom type etsysAntiSpoofSystemNotificationInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_EtsysAntiSpoofSystemNotificationInterval_Type.__name__ = "Unsigned32"
_EtsysAntiSpoofSystemNotificationInterval_Object = MibScalar
etsysAntiSpoofSystemNotificationInterval = _EtsysAntiSpoofSystemNotificationInterval_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 1, 5),
    _EtsysAntiSpoofSystemNotificationInterval_Type()
)
etsysAntiSpoofSystemNotificationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysAntiSpoofSystemNotificationInterval.setStatus("current")
if mibBuilder.loadTexts:
    etsysAntiSpoofSystemNotificationInterval.setUnits("seconds")


class _EtsysAntiSpoofDuplicateIpControl_Type(EnabledStatus):
    """Custom type etsysAntiSpoofDuplicateIpControl based on EnabledStatus"""
    defaultValue = 2


_EtsysAntiSpoofDuplicateIpControl_Type.__name__ = "EnabledStatus"
_EtsysAntiSpoofDuplicateIpControl_Object = MibScalar
etsysAntiSpoofDuplicateIpControl = _EtsysAntiSpoofDuplicateIpControl_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 1, 6),
    _EtsysAntiSpoofDuplicateIpControl_Type()
)
etsysAntiSpoofDuplicateIpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysAntiSpoofDuplicateIpControl.setStatus("current")
_EtsysAntiSpoofSupportedActionTypes_Type = AntiSpoofPortAction
_EtsysAntiSpoofSupportedActionTypes_Object = MibScalar
etsysAntiSpoofSupportedActionTypes = _EtsysAntiSpoofSupportedActionTypes_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 1, 7),
    _EtsysAntiSpoofSupportedActionTypes_Type()
)
etsysAntiSpoofSupportedActionTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysAntiSpoofSupportedActionTypes.setStatus("current")


class _EtsysAntiSpoofSupportedThresholdTypes_Type(Bits):
    """Custom type etsysAntiSpoofSupportedThresholdTypes based on Bits"""
    namedValues = NamedValues(
        *(("ipv4Change", 0),
          ("ipv6Change", 1),
          ("portChange", 2))
    )

_EtsysAntiSpoofSupportedThresholdTypes_Type.__name__ = "Bits"
_EtsysAntiSpoofSupportedThresholdTypes_Object = MibScalar
etsysAntiSpoofSupportedThresholdTypes = _EtsysAntiSpoofSupportedThresholdTypes_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 1, 8),
    _EtsysAntiSpoofSupportedThresholdTypes_Type()
)
etsysAntiSpoofSupportedThresholdTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysAntiSpoofSupportedThresholdTypes.setStatus("current")


class _EtsysAntiSpoofSupportedBindingTypes_Type(Bits):
    """Custom type etsysAntiSpoofSupportedBindingTypes based on Bits"""
    namedValues = NamedValues(
        *(("dhcp", 0),
          ("arp", 1),
          ("ip", 2))
    )

_EtsysAntiSpoofSupportedBindingTypes_Type.__name__ = "Bits"
_EtsysAntiSpoofSupportedBindingTypes_Object = MibScalar
etsysAntiSpoofSupportedBindingTypes = _EtsysAntiSpoofSupportedBindingTypes_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 1, 9),
    _EtsysAntiSpoofSupportedBindingTypes_Type()
)
etsysAntiSpoofSupportedBindingTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysAntiSpoofSupportedBindingTypes.setStatus("current")
_EtsysAntiSpoofClassBranch_ObjectIdentity = ObjectIdentity
etsysAntiSpoofClassBranch = _EtsysAntiSpoofClassBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 2)
)
_EtsysAntiSpoofClassTable_Object = MibTable
etsysAntiSpoofClassTable = _EtsysAntiSpoofClassTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 2, 1)
)
if mibBuilder.loadTexts:
    etsysAntiSpoofClassTable.setStatus("current")
_EtsysAntiSpoofClassEntry_Object = MibTableRow
etsysAntiSpoofClassEntry = _EtsysAntiSpoofClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 2, 1, 1)
)
etsysAntiSpoofClassEntry.setIndexNames(
    (0, "ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofClassIndex"),
)
if mibBuilder.loadTexts:
    etsysAntiSpoofClassEntry.setStatus("current")
_EtsysAntiSpoofClassIndex_Type = Unsigned32
_EtsysAntiSpoofClassIndex_Object = MibTableColumn
etsysAntiSpoofClassIndex = _EtsysAntiSpoofClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 2, 1, 1, 1),
    _EtsysAntiSpoofClassIndex_Type()
)
etsysAntiSpoofClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysAntiSpoofClassIndex.setStatus("current")


class _EtsysAntiSpoofClassName_Type(SnmpAdminString):
    """Custom type etsysAntiSpoofClassName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EtsysAntiSpoofClassName_Type.__name__ = "SnmpAdminString"
_EtsysAntiSpoofClassName_Object = MibTableColumn
etsysAntiSpoofClassName = _EtsysAntiSpoofClassName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 2, 1, 1, 2),
    _EtsysAntiSpoofClassName_Type()
)
etsysAntiSpoofClassName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysAntiSpoofClassName.setStatus("current")


class _EtsysAntiSpoofClassTimeout_Type(Unsigned32):
    """Custom type etsysAntiSpoofClassTimeout based on Unsigned32"""
    defaultValue = 600


_EtsysAntiSpoofClassTimeout_Type.__name__ = "Unsigned32"
_EtsysAntiSpoofClassTimeout_Object = MibTableColumn
etsysAntiSpoofClassTimeout = _EtsysAntiSpoofClassTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 2, 1, 1, 3),
    _EtsysAntiSpoofClassTimeout_Type()
)
etsysAntiSpoofClassTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysAntiSpoofClassTimeout.setStatus("current")
if mibBuilder.loadTexts:
    etsysAntiSpoofClassTimeout.setUnits("seconds")
_EtsysAntiSpoofThresholdTable_Object = MibTable
etsysAntiSpoofThresholdTable = _EtsysAntiSpoofThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 2, 2)
)
if mibBuilder.loadTexts:
    etsysAntiSpoofThresholdTable.setStatus("current")
_EtsysAntiSpoofThresholdEntry_Object = MibTableRow
etsysAntiSpoofThresholdEntry = _EtsysAntiSpoofThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 2, 2, 1)
)
etsysAntiSpoofThresholdEntry.setIndexNames(
    (0, "ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofClassIndex"),
    (0, "ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofThresholdIndex"),
)
if mibBuilder.loadTexts:
    etsysAntiSpoofThresholdEntry.setStatus("current")
_EtsysAntiSpoofThresholdIndex_Type = Unsigned32
_EtsysAntiSpoofThresholdIndex_Object = MibTableColumn
etsysAntiSpoofThresholdIndex = _EtsysAntiSpoofThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 2, 2, 1, 1),
    _EtsysAntiSpoofThresholdIndex_Type()
)
etsysAntiSpoofThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysAntiSpoofThresholdIndex.setStatus("current")
_EtsysAntiSpoofThresholdValue_Type = Unsigned32
_EtsysAntiSpoofThresholdValue_Object = MibTableColumn
etsysAntiSpoofThresholdValue = _EtsysAntiSpoofThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 2, 2, 1, 2),
    _EtsysAntiSpoofThresholdValue_Type()
)
etsysAntiSpoofThresholdValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysAntiSpoofThresholdValue.setStatus("current")
_EtsysAntiSpoofThresholdActionMask_Type = AntiSpoofPortAction
_EtsysAntiSpoofThresholdActionMask_Object = MibTableColumn
etsysAntiSpoofThresholdActionMask = _EtsysAntiSpoofThresholdActionMask_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 2, 2, 1, 3),
    _EtsysAntiSpoofThresholdActionMask_Type()
)
etsysAntiSpoofThresholdActionMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysAntiSpoofThresholdActionMask.setStatus("current")
_EtsysAntiSpoofThresholdActionQuarantineValue_Type = Integer32
_EtsysAntiSpoofThresholdActionQuarantineValue_Object = MibTableColumn
etsysAntiSpoofThresholdActionQuarantineValue = _EtsysAntiSpoofThresholdActionQuarantineValue_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 2, 2, 1, 4),
    _EtsysAntiSpoofThresholdActionQuarantineValue_Type()
)
etsysAntiSpoofThresholdActionQuarantineValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysAntiSpoofThresholdActionQuarantineValue.setStatus("current")
_EtsysAntiSpoofThresholdType_Type = AntiSpoofThresholdType
_EtsysAntiSpoofThresholdType_Object = MibTableColumn
etsysAntiSpoofThresholdType = _EtsysAntiSpoofThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 2, 2, 1, 5),
    _EtsysAntiSpoofThresholdType_Type()
)
etsysAntiSpoofThresholdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysAntiSpoofThresholdType.setStatus("current")
_EtsysAntiSpoofPortBranch_ObjectIdentity = ObjectIdentity
etsysAntiSpoofPortBranch = _EtsysAntiSpoofPortBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 3)
)
_EtsysAntiSpoofPortConfigTable_Object = MibTable
etsysAntiSpoofPortConfigTable = _EtsysAntiSpoofPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 3, 1)
)
if mibBuilder.loadTexts:
    etsysAntiSpoofPortConfigTable.setStatus("current")
_EtsysAntiSpoofPortConfigEntry_Object = MibTableRow
etsysAntiSpoofPortConfigEntry = _EtsysAntiSpoofPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 3, 1, 1)
)
etsysAntiSpoofPortConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    etsysAntiSpoofPortConfigEntry.setStatus("current")


class _EtsysAntiSpoofDHCPMode_Type(EnabledStatus):
    """Custom type etsysAntiSpoofDHCPMode based on EnabledStatus"""
    defaultValue = 2


_EtsysAntiSpoofDHCPMode_Type.__name__ = "EnabledStatus"
_EtsysAntiSpoofDHCPMode_Object = MibTableColumn
etsysAntiSpoofDHCPMode = _EtsysAntiSpoofDHCPMode_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 3, 1, 1, 1),
    _EtsysAntiSpoofDHCPMode_Type()
)
etsysAntiSpoofDHCPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysAntiSpoofDHCPMode.setStatus("current")


class _EtsysAntiSpoofDHCPMacVerify_Type(EnabledStatus):
    """Custom type etsysAntiSpoofDHCPMacVerify based on EnabledStatus"""
    defaultValue = 2


_EtsysAntiSpoofDHCPMacVerify_Type.__name__ = "EnabledStatus"
_EtsysAntiSpoofDHCPMacVerify_Object = MibTableColumn
etsysAntiSpoofDHCPMacVerify = _EtsysAntiSpoofDHCPMacVerify_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 3, 1, 1, 2),
    _EtsysAntiSpoofDHCPMacVerify_Type()
)
etsysAntiSpoofDHCPMacVerify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysAntiSpoofDHCPMacVerify.setStatus("current")


class _EtsysAntiSpoofArpInspection_Type(AntiSpoofInspectionType):
    """Custom type etsysAntiSpoofArpInspection based on AntiSpoofInspectionType"""
    defaultValue = 2


_EtsysAntiSpoofArpInspection_Type.__name__ = "AntiSpoofInspectionType"
_EtsysAntiSpoofArpInspection_Object = MibTableColumn
etsysAntiSpoofArpInspection = _EtsysAntiSpoofArpInspection_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 3, 1, 1, 3),
    _EtsysAntiSpoofArpInspection_Type()
)
etsysAntiSpoofArpInspection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysAntiSpoofArpInspection.setStatus("current")


class _EtsysAntiSpoofIpInspection_Type(AntiSpoofInspectionType):
    """Custom type etsysAntiSpoofIpInspection based on AntiSpoofInspectionType"""
    defaultValue = 2


_EtsysAntiSpoofIpInspection_Type.__name__ = "AntiSpoofInspectionType"
_EtsysAntiSpoofIpInspection_Object = MibTableColumn
etsysAntiSpoofIpInspection = _EtsysAntiSpoofIpInspection_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 3, 1, 1, 4),
    _EtsysAntiSpoofIpInspection_Type()
)
etsysAntiSpoofIpInspection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysAntiSpoofIpInspection.setStatus("current")


class _EtsysAntiSpoofPortClassIndex_Type(Unsigned32):
    """Custom type etsysAntiSpoofPortClassIndex based on Unsigned32"""
    defaultValue = 0


_EtsysAntiSpoofPortClassIndex_Type.__name__ = "Unsigned32"
_EtsysAntiSpoofPortClassIndex_Object = MibTableColumn
etsysAntiSpoofPortClassIndex = _EtsysAntiSpoofPortClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 3, 1, 1, 5),
    _EtsysAntiSpoofPortClassIndex_Type()
)
etsysAntiSpoofPortClassIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysAntiSpoofPortClassIndex.setStatus("current")
_EtsysAntiSpoofUntrustedTrafficPacketCounter_Type = Counter32
_EtsysAntiSpoofUntrustedTrafficPacketCounter_Object = MibTableColumn
etsysAntiSpoofUntrustedTrafficPacketCounter = _EtsysAntiSpoofUntrustedTrafficPacketCounter_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 3, 1, 1, 6),
    _EtsysAntiSpoofUntrustedTrafficPacketCounter_Type()
)
etsysAntiSpoofUntrustedTrafficPacketCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysAntiSpoofUntrustedTrafficPacketCounter.setStatus("current")
_EtsysAntiSpoofPortTypeTable_Object = MibTable
etsysAntiSpoofPortTypeTable = _EtsysAntiSpoofPortTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 3, 2)
)
if mibBuilder.loadTexts:
    etsysAntiSpoofPortTypeTable.setStatus("current")
_EtsysAntiSpoofPortTypeEntry_Object = MibTableRow
etsysAntiSpoofPortTypeEntry = _EtsysAntiSpoofPortTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 3, 2, 1)
)
etsysAntiSpoofPortTypeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    etsysAntiSpoofPortTypeEntry.setStatus("current")


class _EtsysAntiSpoofPortType_Type(AntiSpoofPortType):
    """Custom type etsysAntiSpoofPortType based on AntiSpoofPortType"""
    defaultValue = 3


_EtsysAntiSpoofPortType_Type.__name__ = "AntiSpoofPortType"
_EtsysAntiSpoofPortType_Object = MibTableColumn
etsysAntiSpoofPortType = _EtsysAntiSpoofPortType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 3, 2, 1, 1),
    _EtsysAntiSpoofPortType_Type()
)
etsysAntiSpoofPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysAntiSpoofPortType.setStatus("current")
_EtsysAntiSpoofBindingBranch_ObjectIdentity = ObjectIdentity
etsysAntiSpoofBindingBranch = _EtsysAntiSpoofBindingBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 4)
)
_EtsysAntiSpoofStationBindingTable_Object = MibTable
etsysAntiSpoofStationBindingTable = _EtsysAntiSpoofStationBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 4, 1)
)
if mibBuilder.loadTexts:
    etsysAntiSpoofStationBindingTable.setStatus("current")
_EtsysAntiSpoofStationBindingEntry_Object = MibTableRow
etsysAntiSpoofStationBindingEntry = _EtsysAntiSpoofStationBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 4, 1, 1)
)
etsysAntiSpoofStationBindingEntry.setIndexNames(
    (0, "ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofStationBindingEntryIndex"),
)
if mibBuilder.loadTexts:
    etsysAntiSpoofStationBindingEntry.setStatus("current")
_EtsysAntiSpoofStationBindingEntryIndex_Type = EtsysInstanceOID
_EtsysAntiSpoofStationBindingEntryIndex_Object = MibTableColumn
etsysAntiSpoofStationBindingEntryIndex = _EtsysAntiSpoofStationBindingEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 4, 1, 1, 1),
    _EtsysAntiSpoofStationBindingEntryIndex_Type()
)
etsysAntiSpoofStationBindingEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysAntiSpoofStationBindingEntryIndex.setStatus("current")
_EtsysAntiSpoofStationBindingEntryMacAddr_Type = MacAddress
_EtsysAntiSpoofStationBindingEntryMacAddr_Object = MibTableColumn
etsysAntiSpoofStationBindingEntryMacAddr = _EtsysAntiSpoofStationBindingEntryMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 4, 1, 1, 2),
    _EtsysAntiSpoofStationBindingEntryMacAddr_Type()
)
etsysAntiSpoofStationBindingEntryMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysAntiSpoofStationBindingEntryMacAddr.setStatus("current")
_EtsysAntiSpoofStationBindingEntryInetAddrType_Type = InetAddressType
_EtsysAntiSpoofStationBindingEntryInetAddrType_Object = MibTableColumn
etsysAntiSpoofStationBindingEntryInetAddrType = _EtsysAntiSpoofStationBindingEntryInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 4, 1, 1, 3),
    _EtsysAntiSpoofStationBindingEntryInetAddrType_Type()
)
etsysAntiSpoofStationBindingEntryInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysAntiSpoofStationBindingEntryInetAddrType.setStatus("current")
_EtsysAntiSpoofStationBindingEntryInetAddr_Type = InetAddress
_EtsysAntiSpoofStationBindingEntryInetAddr_Object = MibTableColumn
etsysAntiSpoofStationBindingEntryInetAddr = _EtsysAntiSpoofStationBindingEntryInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 4, 1, 1, 4),
    _EtsysAntiSpoofStationBindingEntryInetAddr_Type()
)
etsysAntiSpoofStationBindingEntryInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysAntiSpoofStationBindingEntryInetAddr.setStatus("current")
_EtsysAntiSpoofStationBindingEntryIfIndex_Type = InterfaceIndex
_EtsysAntiSpoofStationBindingEntryIfIndex_Object = MibTableColumn
etsysAntiSpoofStationBindingEntryIfIndex = _EtsysAntiSpoofStationBindingEntryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 4, 1, 1, 5),
    _EtsysAntiSpoofStationBindingEntryIfIndex_Type()
)
etsysAntiSpoofStationBindingEntryIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysAntiSpoofStationBindingEntryIfIndex.setStatus("current")
_EtsysAntiSpoofStationBindingEntryInetCounter_Type = Counter32
_EtsysAntiSpoofStationBindingEntryInetCounter_Object = MibTableColumn
etsysAntiSpoofStationBindingEntryInetCounter = _EtsysAntiSpoofStationBindingEntryInetCounter_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 4, 1, 1, 6),
    _EtsysAntiSpoofStationBindingEntryInetCounter_Type()
)
etsysAntiSpoofStationBindingEntryInetCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysAntiSpoofStationBindingEntryInetCounter.setStatus("current")
_EtsysAntiSpoofStationBindingEntryClearInetCounter_Type = TruthValue
_EtsysAntiSpoofStationBindingEntryClearInetCounter_Object = MibTableColumn
etsysAntiSpoofStationBindingEntryClearInetCounter = _EtsysAntiSpoofStationBindingEntryClearInetCounter_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 4, 1, 1, 7),
    _EtsysAntiSpoofStationBindingEntryClearInetCounter_Type()
)
etsysAntiSpoofStationBindingEntryClearInetCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysAntiSpoofStationBindingEntryClearInetCounter.setStatus("current")
_EtsysAntiSpoofStationBindingEntryPortCounter_Type = Counter32
_EtsysAntiSpoofStationBindingEntryPortCounter_Object = MibTableColumn
etsysAntiSpoofStationBindingEntryPortCounter = _EtsysAntiSpoofStationBindingEntryPortCounter_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 4, 1, 1, 8),
    _EtsysAntiSpoofStationBindingEntryPortCounter_Type()
)
etsysAntiSpoofStationBindingEntryPortCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysAntiSpoofStationBindingEntryPortCounter.setStatus("current")
_EtsysAntiSpoofStationBindingEntryClearPortCounter_Type = TruthValue
_EtsysAntiSpoofStationBindingEntryClearPortCounter_Object = MibTableColumn
etsysAntiSpoofStationBindingEntryClearPortCounter = _EtsysAntiSpoofStationBindingEntryClearPortCounter_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 4, 1, 1, 9),
    _EtsysAntiSpoofStationBindingEntryClearPortCounter_Type()
)
etsysAntiSpoofStationBindingEntryClearPortCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysAntiSpoofStationBindingEntryClearPortCounter.setStatus("current")
_EtsysAntiSpoofStationBindingEntryClearBinding_Type = TruthValue
_EtsysAntiSpoofStationBindingEntryClearBinding_Object = MibTableColumn
etsysAntiSpoofStationBindingEntryClearBinding = _EtsysAntiSpoofStationBindingEntryClearBinding_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 4, 1, 1, 10),
    _EtsysAntiSpoofStationBindingEntryClearBinding_Type()
)
etsysAntiSpoofStationBindingEntryClearBinding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysAntiSpoofStationBindingEntryClearBinding.setStatus("current")
_EtsysAntiSpoofStationBindingEntryBindingType_Type = AntiSpoofBindingType
_EtsysAntiSpoofStationBindingEntryBindingType_Object = MibTableColumn
etsysAntiSpoofStationBindingEntryBindingType = _EtsysAntiSpoofStationBindingEntryBindingType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 4, 1, 1, 11),
    _EtsysAntiSpoofStationBindingEntryBindingType_Type()
)
etsysAntiSpoofStationBindingEntryBindingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysAntiSpoofStationBindingEntryBindingType.setStatus("current")
_EtsysAntiSpoofStationBindingEntryDurationTime_Type = Unsigned32
_EtsysAntiSpoofStationBindingEntryDurationTime_Object = MibTableColumn
etsysAntiSpoofStationBindingEntryDurationTime = _EtsysAntiSpoofStationBindingEntryDurationTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 4, 1, 1, 12),
    _EtsysAntiSpoofStationBindingEntryDurationTime_Type()
)
etsysAntiSpoofStationBindingEntryDurationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysAntiSpoofStationBindingEntryDurationTime.setStatus("current")
if mibBuilder.loadTexts:
    etsysAntiSpoofStationBindingEntryDurationTime.setUnits("seconds")
_EtsysAntiSpoofStationBindingEntryExpirationTime_Type = Unsigned32
_EtsysAntiSpoofStationBindingEntryExpirationTime_Object = MibTableColumn
etsysAntiSpoofStationBindingEntryExpirationTime = _EtsysAntiSpoofStationBindingEntryExpirationTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 4, 1, 1, 13),
    _EtsysAntiSpoofStationBindingEntryExpirationTime_Type()
)
etsysAntiSpoofStationBindingEntryExpirationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysAntiSpoofStationBindingEntryExpirationTime.setStatus("current")
if mibBuilder.loadTexts:
    etsysAntiSpoofStationBindingEntryExpirationTime.setUnits("seconds")
_EtsysAntiSpoofMacBindingTable_Object = MibTable
etsysAntiSpoofMacBindingTable = _EtsysAntiSpoofMacBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 4, 2)
)
if mibBuilder.loadTexts:
    etsysAntiSpoofMacBindingTable.setStatus("current")
_EtsysAntiSpoofMacBindingEntry_Object = MibTableRow
etsysAntiSpoofMacBindingEntry = _EtsysAntiSpoofMacBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 4, 2, 1)
)
etsysAntiSpoofMacBindingEntry.setIndexNames(
    (0, "ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofStationBindingEntryMacAddr"),
    (0, "ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofStationBindingEntryInetAddrType"),
    (0, "ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofStationBindingEntryInetAddr"),
    (0, "ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofStationBindingInterface"),
)
if mibBuilder.loadTexts:
    etsysAntiSpoofMacBindingEntry.setStatus("current")
_EtsysAntiSpoofStationBindingInterface_Type = InterfaceIndexOrZero
_EtsysAntiSpoofStationBindingInterface_Object = MibTableColumn
etsysAntiSpoofStationBindingInterface = _EtsysAntiSpoofStationBindingInterface_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 4, 2, 1, 1),
    _EtsysAntiSpoofStationBindingInterface_Type()
)
etsysAntiSpoofStationBindingInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysAntiSpoofStationBindingInterface.setStatus("current")
_EtsysAntiSpoofMacStationBindingIndex_Type = EtsysInstanceOID
_EtsysAntiSpoofMacStationBindingIndex_Object = MibTableColumn
etsysAntiSpoofMacStationBindingIndex = _EtsysAntiSpoofMacStationBindingIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 4, 2, 1, 2),
    _EtsysAntiSpoofMacStationBindingIndex_Type()
)
etsysAntiSpoofMacStationBindingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysAntiSpoofMacStationBindingIndex.setStatus("current")
_EtsysAntiSpoofMacBindingClearBinding_Type = TruthValue
_EtsysAntiSpoofMacBindingClearBinding_Object = MibTableColumn
etsysAntiSpoofMacBindingClearBinding = _EtsysAntiSpoofMacBindingClearBinding_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 4, 2, 1, 3),
    _EtsysAntiSpoofMacBindingClearBinding_Type()
)
etsysAntiSpoofMacBindingClearBinding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysAntiSpoofMacBindingClearBinding.setStatus("current")
_EtsysAntiSpoofIpBindingTable_Object = MibTable
etsysAntiSpoofIpBindingTable = _EtsysAntiSpoofIpBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 4, 3)
)
if mibBuilder.loadTexts:
    etsysAntiSpoofIpBindingTable.setStatus("current")
_EtsysAntiSpoofIpBindingEntry_Object = MibTableRow
etsysAntiSpoofIpBindingEntry = _EtsysAntiSpoofIpBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 4, 3, 1)
)
etsysAntiSpoofIpBindingEntry.setIndexNames(
    (0, "ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofStationBindingEntryInetAddrType"),
    (0, "ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofStationBindingEntryInetAddr"),
    (0, "ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofStationBindingEntryMacAddr"),
    (0, "ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofStationBindingInterface"),
)
if mibBuilder.loadTexts:
    etsysAntiSpoofIpBindingEntry.setStatus("current")
_EtsysAntiSpoofIpStationBindingIndex_Type = EtsysInstanceOID
_EtsysAntiSpoofIpStationBindingIndex_Object = MibTableColumn
etsysAntiSpoofIpStationBindingIndex = _EtsysAntiSpoofIpStationBindingIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 4, 3, 1, 1),
    _EtsysAntiSpoofIpStationBindingIndex_Type()
)
etsysAntiSpoofIpStationBindingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysAntiSpoofIpStationBindingIndex.setStatus("current")
_EtsysAntiSpoofIpBindingClearBinding_Type = TruthValue
_EtsysAntiSpoofIpBindingClearBinding_Object = MibTableColumn
etsysAntiSpoofIpBindingClearBinding = _EtsysAntiSpoofIpBindingClearBinding_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 4, 3, 1, 2),
    _EtsysAntiSpoofIpBindingClearBinding_Type()
)
etsysAntiSpoofIpBindingClearBinding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysAntiSpoofIpBindingClearBinding.setStatus("current")
_EtsysAntiSpoofPortBindingTable_Object = MibTable
etsysAntiSpoofPortBindingTable = _EtsysAntiSpoofPortBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 4, 4)
)
if mibBuilder.loadTexts:
    etsysAntiSpoofPortBindingTable.setStatus("current")
_EtsysAntiSpoofPortBindingEntry_Object = MibTableRow
etsysAntiSpoofPortBindingEntry = _EtsysAntiSpoofPortBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 4, 4, 1)
)
etsysAntiSpoofPortBindingEntry.setIndexNames(
    (0, "ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofStationBindingInterface"),
    (0, "ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofStationBindingEntryMacAddr"),
    (0, "ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofStationBindingEntryInetAddrType"),
    (0, "ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofStationBindingEntryInetAddr"),
)
if mibBuilder.loadTexts:
    etsysAntiSpoofPortBindingEntry.setStatus("current")
_EtsysAntiSpoofPortStationBindingIndex_Type = EtsysInstanceOID
_EtsysAntiSpoofPortStationBindingIndex_Object = MibTableColumn
etsysAntiSpoofPortStationBindingIndex = _EtsysAntiSpoofPortStationBindingIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 4, 4, 1, 1),
    _EtsysAntiSpoofPortStationBindingIndex_Type()
)
etsysAntiSpoofPortStationBindingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysAntiSpoofPortStationBindingIndex.setStatus("current")
_EtsysAntiSpoofPortBindingClearBinding_Type = TruthValue
_EtsysAntiSpoofPortBindingClearBinding_Object = MibTableColumn
etsysAntiSpoofPortBindingClearBinding = _EtsysAntiSpoofPortBindingClearBinding_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 4, 4, 1, 2),
    _EtsysAntiSpoofPortBindingClearBinding_Type()
)
etsysAntiSpoofPortBindingClearBinding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysAntiSpoofPortBindingClearBinding.setStatus("current")
_EtsysAntiSpoofConformance_ObjectIdentity = ObjectIdentity
etsysAntiSpoofConformance = _EtsysAntiSpoofConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 2)
)
_EtsysAntiSpoofGroups_ObjectIdentity = ObjectIdentity
etsysAntiSpoofGroups = _EtsysAntiSpoofGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 2, 1)
)
_EtsysAntiSpoofCompliances_ObjectIdentity = ObjectIdentity
etsysAntiSpoofCompliances = _EtsysAntiSpoofCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 2, 2)
)

# Managed Objects groups

etsysAntiSpoofSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 2, 1, 1)
)
etsysAntiSpoofSystemGroup.setObjects(
      *(("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofSystemState"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofMaxClassIndex"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofMaxClassThresholdIndex"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofSystemSnmpNotifications"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofSystemNotificationInterval"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofDuplicateIpControl"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofSupportedActionTypes"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofSupportedThresholdTypes"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofSupportedBindingTypes"))
)
if mibBuilder.loadTexts:
    etsysAntiSpoofSystemGroup.setStatus("current")

etsysAntiSpoofClassGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 2, 1, 2)
)
etsysAntiSpoofClassGroup.setObjects(
      *(("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofClassName"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofClassTimeout"))
)
if mibBuilder.loadTexts:
    etsysAntiSpoofClassGroup.setStatus("current")

etsysAntiSpoofThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 2, 1, 3)
)
etsysAntiSpoofThresholdGroup.setObjects(
      *(("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofThresholdValue"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofThresholdActionMask"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofThresholdActionQuarantineValue"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofThresholdType"))
)
if mibBuilder.loadTexts:
    etsysAntiSpoofThresholdGroup.setStatus("current")

etsysAntiSpoofPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 2, 1, 4)
)
etsysAntiSpoofPortGroup.setObjects(
      *(("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofDHCPMode"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofDHCPMacVerify"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofArpInspection"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofIpInspection"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofPortClassIndex"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofUntrustedTrafficPacketCounter"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofPortType"))
)
if mibBuilder.loadTexts:
    etsysAntiSpoofPortGroup.setStatus("current")

etsysAntiSpoofStationBindingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 2, 1, 5)
)
etsysAntiSpoofStationBindingGroup.setObjects(
      *(("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofStationBindingEntryMacAddr"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofStationBindingEntryInetAddrType"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofStationBindingEntryInetAddr"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofStationBindingEntryInetCounter"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofStationBindingEntryClearInetCounter"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofStationBindingEntryIfIndex"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofStationBindingEntryPortCounter"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofStationBindingEntryClearPortCounter"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofStationBindingEntryClearBinding"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofStationBindingEntryBindingType"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofStationBindingEntryDurationTime"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofStationBindingEntryExpirationTime"))
)
if mibBuilder.loadTexts:
    etsysAntiSpoofStationBindingGroup.setStatus("current")

etsysAntiSpoofMacBindingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 2, 1, 6)
)
etsysAntiSpoofMacBindingGroup.setObjects(
      *(("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofMacStationBindingIndex"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofMacBindingClearBinding"))
)
if mibBuilder.loadTexts:
    etsysAntiSpoofMacBindingGroup.setStatus("current")

etsysAntiSpoofIpBindingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 2, 1, 7)
)
etsysAntiSpoofIpBindingGroup.setObjects(
      *(("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofIpStationBindingIndex"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofIpBindingClearBinding"))
)
if mibBuilder.loadTexts:
    etsysAntiSpoofIpBindingGroup.setStatus("current")

etsysAntiSpoofPortBindingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 2, 1, 8)
)
etsysAntiSpoofPortBindingGroup.setObjects(
      *(("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofPortStationBindingIndex"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofPortBindingClearBinding"))
)
if mibBuilder.loadTexts:
    etsysAntiSpoofPortBindingGroup.setStatus("current")


# Notification objects

etsysAntiSpoofClassNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 0, 1)
)
etsysAntiSpoofClassNotification.setObjects(
      *(("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofThresholdValue"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofStationBindingEntryMacAddr"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofStationBindingEntryInetAddrType"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofStationBindingEntryInetAddr"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofStationBindingEntryIfIndex"))
)
if mibBuilder.loadTexts:
    etsysAntiSpoofClassNotification.setStatus(
        "current"
    )

etsysAntiSpoofDuplicateIpNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 1, 0, 2)
)
etsysAntiSpoofDuplicateIpNotification.setObjects(
      *(("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofStationBindingEntryMacAddr"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofStationBindingEntryIfIndex"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofStationBindingEntryInetAddrType"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofStationBindingEntryInetAddr"))
)
if mibBuilder.loadTexts:
    etsysAntiSpoofDuplicateIpNotification.setStatus(
        "current"
    )


# Notifications groups

etsysAntiSpoofNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 2, 1, 9)
)
etsysAntiSpoofNotificationGroup.setObjects(
      *(("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofClassNotification"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofDuplicateIpNotification"))
)
if mibBuilder.loadTexts:
    etsysAntiSpoofNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

etsysAntiSpoofCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 96, 2, 2, 1)
)
etsysAntiSpoofCompliance.setObjects(
      *(("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofSystemGroup"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofClassGroup"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofThresholdGroup"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofPortGroup"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofStationBindingGroup"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofMacBindingGroup"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofPortBindingGroup"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofIpBindingGroup"),
        ("ENTERASYS-ANTI-SPOOF-MIB", "etsysAntiSpoofNotificationGroup"))
)
if mibBuilder.loadTexts:
    etsysAntiSpoofCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-ANTI-SPOOF-MIB",
    **{"AntiSpoofPortAction": AntiSpoofPortAction,
       "AntiSpoofInspectionType": AntiSpoofInspectionType,
       "AntiSpoofThresholdType": AntiSpoofThresholdType,
       "AntiSpoofPortType": AntiSpoofPortType,
       "AntiSpoofBindingType": AntiSpoofBindingType,
       "EtsysInstanceOID": EtsysInstanceOID,
       "etsysAntiSpoofMIB": etsysAntiSpoofMIB,
       "etsysAntiSpoofObjects": etsysAntiSpoofObjects,
       "etsysAntiSpoofNotificationBranch": etsysAntiSpoofNotificationBranch,
       "etsysAntiSpoofClassNotification": etsysAntiSpoofClassNotification,
       "etsysAntiSpoofDuplicateIpNotification": etsysAntiSpoofDuplicateIpNotification,
       "etsysAntiSpoofSystemBranch": etsysAntiSpoofSystemBranch,
       "etsysAntiSpoofSystemState": etsysAntiSpoofSystemState,
       "etsysAntiSpoofMaxClassIndex": etsysAntiSpoofMaxClassIndex,
       "etsysAntiSpoofMaxClassThresholdIndex": etsysAntiSpoofMaxClassThresholdIndex,
       "etsysAntiSpoofSystemSnmpNotifications": etsysAntiSpoofSystemSnmpNotifications,
       "etsysAntiSpoofSystemNotificationInterval": etsysAntiSpoofSystemNotificationInterval,
       "etsysAntiSpoofDuplicateIpControl": etsysAntiSpoofDuplicateIpControl,
       "etsysAntiSpoofSupportedActionTypes": etsysAntiSpoofSupportedActionTypes,
       "etsysAntiSpoofSupportedThresholdTypes": etsysAntiSpoofSupportedThresholdTypes,
       "etsysAntiSpoofSupportedBindingTypes": etsysAntiSpoofSupportedBindingTypes,
       "etsysAntiSpoofClassBranch": etsysAntiSpoofClassBranch,
       "etsysAntiSpoofClassTable": etsysAntiSpoofClassTable,
       "etsysAntiSpoofClassEntry": etsysAntiSpoofClassEntry,
       "etsysAntiSpoofClassIndex": etsysAntiSpoofClassIndex,
       "etsysAntiSpoofClassName": etsysAntiSpoofClassName,
       "etsysAntiSpoofClassTimeout": etsysAntiSpoofClassTimeout,
       "etsysAntiSpoofThresholdTable": etsysAntiSpoofThresholdTable,
       "etsysAntiSpoofThresholdEntry": etsysAntiSpoofThresholdEntry,
       "etsysAntiSpoofThresholdIndex": etsysAntiSpoofThresholdIndex,
       "etsysAntiSpoofThresholdValue": etsysAntiSpoofThresholdValue,
       "etsysAntiSpoofThresholdActionMask": etsysAntiSpoofThresholdActionMask,
       "etsysAntiSpoofThresholdActionQuarantineValue": etsysAntiSpoofThresholdActionQuarantineValue,
       "etsysAntiSpoofThresholdType": etsysAntiSpoofThresholdType,
       "etsysAntiSpoofPortBranch": etsysAntiSpoofPortBranch,
       "etsysAntiSpoofPortConfigTable": etsysAntiSpoofPortConfigTable,
       "etsysAntiSpoofPortConfigEntry": etsysAntiSpoofPortConfigEntry,
       "etsysAntiSpoofDHCPMode": etsysAntiSpoofDHCPMode,
       "etsysAntiSpoofDHCPMacVerify": etsysAntiSpoofDHCPMacVerify,
       "etsysAntiSpoofArpInspection": etsysAntiSpoofArpInspection,
       "etsysAntiSpoofIpInspection": etsysAntiSpoofIpInspection,
       "etsysAntiSpoofPortClassIndex": etsysAntiSpoofPortClassIndex,
       "etsysAntiSpoofUntrustedTrafficPacketCounter": etsysAntiSpoofUntrustedTrafficPacketCounter,
       "etsysAntiSpoofPortTypeTable": etsysAntiSpoofPortTypeTable,
       "etsysAntiSpoofPortTypeEntry": etsysAntiSpoofPortTypeEntry,
       "etsysAntiSpoofPortType": etsysAntiSpoofPortType,
       "etsysAntiSpoofBindingBranch": etsysAntiSpoofBindingBranch,
       "etsysAntiSpoofStationBindingTable": etsysAntiSpoofStationBindingTable,
       "etsysAntiSpoofStationBindingEntry": etsysAntiSpoofStationBindingEntry,
       "etsysAntiSpoofStationBindingEntryIndex": etsysAntiSpoofStationBindingEntryIndex,
       "etsysAntiSpoofStationBindingEntryMacAddr": etsysAntiSpoofStationBindingEntryMacAddr,
       "etsysAntiSpoofStationBindingEntryInetAddrType": etsysAntiSpoofStationBindingEntryInetAddrType,
       "etsysAntiSpoofStationBindingEntryInetAddr": etsysAntiSpoofStationBindingEntryInetAddr,
       "etsysAntiSpoofStationBindingEntryIfIndex": etsysAntiSpoofStationBindingEntryIfIndex,
       "etsysAntiSpoofStationBindingEntryInetCounter": etsysAntiSpoofStationBindingEntryInetCounter,
       "etsysAntiSpoofStationBindingEntryClearInetCounter": etsysAntiSpoofStationBindingEntryClearInetCounter,
       "etsysAntiSpoofStationBindingEntryPortCounter": etsysAntiSpoofStationBindingEntryPortCounter,
       "etsysAntiSpoofStationBindingEntryClearPortCounter": etsysAntiSpoofStationBindingEntryClearPortCounter,
       "etsysAntiSpoofStationBindingEntryClearBinding": etsysAntiSpoofStationBindingEntryClearBinding,
       "etsysAntiSpoofStationBindingEntryBindingType": etsysAntiSpoofStationBindingEntryBindingType,
       "etsysAntiSpoofStationBindingEntryDurationTime": etsysAntiSpoofStationBindingEntryDurationTime,
       "etsysAntiSpoofStationBindingEntryExpirationTime": etsysAntiSpoofStationBindingEntryExpirationTime,
       "etsysAntiSpoofMacBindingTable": etsysAntiSpoofMacBindingTable,
       "etsysAntiSpoofMacBindingEntry": etsysAntiSpoofMacBindingEntry,
       "etsysAntiSpoofStationBindingInterface": etsysAntiSpoofStationBindingInterface,
       "etsysAntiSpoofMacStationBindingIndex": etsysAntiSpoofMacStationBindingIndex,
       "etsysAntiSpoofMacBindingClearBinding": etsysAntiSpoofMacBindingClearBinding,
       "etsysAntiSpoofIpBindingTable": etsysAntiSpoofIpBindingTable,
       "etsysAntiSpoofIpBindingEntry": etsysAntiSpoofIpBindingEntry,
       "etsysAntiSpoofIpStationBindingIndex": etsysAntiSpoofIpStationBindingIndex,
       "etsysAntiSpoofIpBindingClearBinding": etsysAntiSpoofIpBindingClearBinding,
       "etsysAntiSpoofPortBindingTable": etsysAntiSpoofPortBindingTable,
       "etsysAntiSpoofPortBindingEntry": etsysAntiSpoofPortBindingEntry,
       "etsysAntiSpoofPortStationBindingIndex": etsysAntiSpoofPortStationBindingIndex,
       "etsysAntiSpoofPortBindingClearBinding": etsysAntiSpoofPortBindingClearBinding,
       "etsysAntiSpoofConformance": etsysAntiSpoofConformance,
       "etsysAntiSpoofGroups": etsysAntiSpoofGroups,
       "etsysAntiSpoofSystemGroup": etsysAntiSpoofSystemGroup,
       "etsysAntiSpoofClassGroup": etsysAntiSpoofClassGroup,
       "etsysAntiSpoofThresholdGroup": etsysAntiSpoofThresholdGroup,
       "etsysAntiSpoofPortGroup": etsysAntiSpoofPortGroup,
       "etsysAntiSpoofStationBindingGroup": etsysAntiSpoofStationBindingGroup,
       "etsysAntiSpoofMacBindingGroup": etsysAntiSpoofMacBindingGroup,
       "etsysAntiSpoofIpBindingGroup": etsysAntiSpoofIpBindingGroup,
       "etsysAntiSpoofPortBindingGroup": etsysAntiSpoofPortBindingGroup,
       "etsysAntiSpoofNotificationGroup": etsysAntiSpoofNotificationGroup,
       "etsysAntiSpoofCompliances": etsysAntiSpoofCompliances,
       "etsysAntiSpoofCompliance": etsysAntiSpoofCompliance}
)
