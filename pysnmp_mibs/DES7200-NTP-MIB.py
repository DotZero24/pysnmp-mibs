# SNMP MIB module (DES7200-NTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DES7200-NTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:51:00 2025
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

(myMgmt,) = mibBuilder.importSymbols(
    "DES7200-SMI",
    "myMgmt")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 NotificationType,
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
    "NotificationType",
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

myNtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49)
)
if mibBuilder.loadTexts:
    myNtpMIB.setRevisions(
        ("2009-05-14 00:00",)
    )


# Types definitions



class NTPTimeStamp(OctetString):
    """Custom type NTPTimeStamp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8





class NTPLeapIndicator(Integer32):
    """Custom type NTPLeapIndicator based on Integer32"""
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
        *(("noWarning", 0),
          ("addSecond", 1),
          ("subtractSecond", 2),
          ("alarm", 3))
    )





class NTPSignedTimeValue(OctetString):
    """Custom type NTPSignedTimeValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4





class NTPUnsignedTimeValue(OctetString):
    """Custom type NTPUnsignedTimeValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4





class NTPStratum(Integer32):
    """Custom type NTPStratum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )





class NTPRefId(OctetString):
    """Custom type NTPRefId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MyNtpMIBObjects_ObjectIdentity = ObjectIdentity
myNtpMIBObjects = _MyNtpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 1)
)
_MyntpSystem_ObjectIdentity = ObjectIdentity
myntpSystem = _MyntpSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 1, 1)
)
_MyntpSysLeap_Type = NTPLeapIndicator
_MyntpSysLeap_Object = MibScalar
myntpSysLeap = _MyntpSysLeap_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 1, 1, 1),
    _MyntpSysLeap_Type()
)
myntpSysLeap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myntpSysLeap.setStatus("mandatory")
_MyntpSysStratum_Type = NTPStratum
_MyntpSysStratum_Object = MibScalar
myntpSysStratum = _MyntpSysStratum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 1, 1, 2),
    _MyntpSysStratum_Type()
)
myntpSysStratum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myntpSysStratum.setStatus("mandatory")


class _MyntpSysPrecision_Type(Integer32):
    """Custom type myntpSysPrecision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-24, 24),
    )


_MyntpSysPrecision_Type.__name__ = "Integer32"
_MyntpSysPrecision_Object = MibScalar
myntpSysPrecision = _MyntpSysPrecision_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 1, 1, 3),
    _MyntpSysPrecision_Type()
)
myntpSysPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myntpSysPrecision.setStatus("mandatory")
_MyntpSysRootDelay_Type = NTPSignedTimeValue
_MyntpSysRootDelay_Object = MibScalar
myntpSysRootDelay = _MyntpSysRootDelay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 1, 1, 4),
    _MyntpSysRootDelay_Type()
)
myntpSysRootDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myntpSysRootDelay.setStatus("mandatory")
_MyntpSysRootDispersion_Type = NTPUnsignedTimeValue
_MyntpSysRootDispersion_Object = MibScalar
myntpSysRootDispersion = _MyntpSysRootDispersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 1, 1, 5),
    _MyntpSysRootDispersion_Type()
)
myntpSysRootDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myntpSysRootDispersion.setStatus("mandatory")
_MyntpSysRefId_Type = NTPRefId
_MyntpSysRefId_Object = MibScalar
myntpSysRefId = _MyntpSysRefId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 1, 1, 6),
    _MyntpSysRefId_Type()
)
myntpSysRefId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myntpSysRefId.setStatus("mandatory")
_MyntpSysRefTime_Type = NTPTimeStamp
_MyntpSysRefTime_Object = MibScalar
myntpSysRefTime = _MyntpSysRefTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 1, 1, 7),
    _MyntpSysRefTime_Type()
)
myntpSysRefTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myntpSysRefTime.setStatus("mandatory")
_MyNtpMIBConformance_ObjectIdentity = ObjectIdentity
myNtpMIBConformance = _MyNtpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 2)
)
_MyNtpMIBCompliances_ObjectIdentity = ObjectIdentity
myNtpMIBCompliances = _MyNtpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 2, 1)
)
_MyNtpMIBGroups_ObjectIdentity = ObjectIdentity
myNtpMIBGroups = _MyNtpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 2, 2)
)

# Managed Objects groups

myNtpSysGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 2, 2, 1)
)
myNtpSysGroup.setObjects(
      *(("DES7200-NTP-MIB", "myntpSysLeap"),
        ("DES7200-NTP-MIB", "myntpSysStratum"),
        ("DES7200-NTP-MIB", "myntpSysPrecision"),
        ("DES7200-NTP-MIB", "myntpSysRootDelay"),
        ("DES7200-NTP-MIB", "myntpSysRootDispersion"),
        ("DES7200-NTP-MIB", "myntpSysRefId"),
        ("DES7200-NTP-MIB", "myntpSysRefTime"))
)
if mibBuilder.loadTexts:
    myNtpSysGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

myNtpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 2, 1, 1)
)
myNtpMIBCompliance.setObjects(
    ("DES7200-NTP-MIB", "myNtpMIBGroups")
)
if mibBuilder.loadTexts:
    myNtpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DES7200-NTP-MIB",
    **{"NTPTimeStamp": NTPTimeStamp,
       "NTPLeapIndicator": NTPLeapIndicator,
       "NTPSignedTimeValue": NTPSignedTimeValue,
       "NTPUnsignedTimeValue": NTPUnsignedTimeValue,
       "NTPStratum": NTPStratum,
       "NTPRefId": NTPRefId,
       "myNtpMIB": myNtpMIB,
       "myNtpMIBObjects": myNtpMIBObjects,
       "myntpSystem": myntpSystem,
       "myntpSysLeap": myntpSysLeap,
       "myntpSysStratum": myntpSysStratum,
       "myntpSysPrecision": myntpSysPrecision,
       "myntpSysRootDelay": myntpSysRootDelay,
       "myntpSysRootDispersion": myntpSysRootDispersion,
       "myntpSysRefId": myntpSysRefId,
       "myntpSysRefTime": myntpSysRefTime,
       "myNtpMIBConformance": myNtpMIBConformance,
       "myNtpMIBCompliances": myNtpMIBCompliances,
       "myNtpMIBCompliance": myNtpMIBCompliance,
       "myNtpMIBGroups": myNtpMIBGroups,
       "myNtpSysGroup": myNtpSysGroup}
)
