# SNMP MIB module (ALCATEL-ENT1-SIP-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/alcatel-ent1/ALCATEL-ENT1-SIP-SNOOPING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:08:57 2025
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

(softentIND1SIPSnooping,) = mibBuilder.importSymbols(
    "ALCATEL-ENT1-BASE",
    "softentIND1SIPSnooping")

(physicalIndex,) = mibBuilder.importSymbols(
    "ALCATEL-ENT1-CHASSIS-MIB",
    "physicalIndex")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

aluSIPSnoopingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1)
)
if mibBuilder.loadTexts:
    aluSIPSnoopingMIB.setRevisions(
        ("2012-05-04 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AluSIPSnoopingMIBNotifications_ObjectIdentity = ObjectIdentity
aluSIPSnoopingMIBNotifications = _AluSIPSnoopingMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 0)
)
_AluSIPSnoopingMIBObjects_ObjectIdentity = ObjectIdentity
aluSIPSnoopingMIBObjects = _AluSIPSnoopingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1)
)
if mibBuilder.loadTexts:
    aluSIPSnoopingMIBObjects.setStatus("current")
_AluSIPSnoopingConfig_ObjectIdentity = ObjectIdentity
aluSIPSnoopingConfig = _AluSIPSnoopingConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1)
)


class _AluSIPSnoopingStatus_Type(Integer32):
    """Custom type aluSIPSnoopingStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AluSIPSnoopingStatus_Type.__name__ = "Integer32"
_AluSIPSnoopingStatus_Object = MibScalar
aluSIPSnoopingStatus = _AluSIPSnoopingStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 1),
    _AluSIPSnoopingStatus_Type()
)
aluSIPSnoopingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingStatus.setStatus("current")


class _AluSIPSnoopingSIPTrustedServerIPAddress1Type_Type(InetAddressType):
    """Custom type aluSIPSnoopingSIPTrustedServerIPAddress1Type based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ipv4", 1)
    )


_AluSIPSnoopingSIPTrustedServerIPAddress1Type_Type.__name__ = "InetAddressType"
_AluSIPSnoopingSIPTrustedServerIPAddress1Type_Object = MibScalar
aluSIPSnoopingSIPTrustedServerIPAddress1Type = _AluSIPSnoopingSIPTrustedServerIPAddress1Type_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 2),
    _AluSIPSnoopingSIPTrustedServerIPAddress1Type_Type()
)
aluSIPSnoopingSIPTrustedServerIPAddress1Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingSIPTrustedServerIPAddress1Type.setStatus("current")


class _AluSIPSnoopingSIPTrustedServerIPAddress1_Type(InetAddress):
    """Custom type aluSIPSnoopingSIPTrustedServerIPAddress1 based on InetAddress"""
    defaultHexValue = "00000000"


_AluSIPSnoopingSIPTrustedServerIPAddress1_Type.__name__ = "InetAddress"
_AluSIPSnoopingSIPTrustedServerIPAddress1_Object = MibScalar
aluSIPSnoopingSIPTrustedServerIPAddress1 = _AluSIPSnoopingSIPTrustedServerIPAddress1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 3),
    _AluSIPSnoopingSIPTrustedServerIPAddress1_Type()
)
aluSIPSnoopingSIPTrustedServerIPAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingSIPTrustedServerIPAddress1.setStatus("current")


class _AluSIPSnoopingSIPTrustedServerIPAddress2Type_Type(InetAddressType):
    """Custom type aluSIPSnoopingSIPTrustedServerIPAddress2Type based on InetAddressType"""
    defaultValue = 1

    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ipv4", 1)
    )


_AluSIPSnoopingSIPTrustedServerIPAddress2Type_Type.__name__ = "InetAddressType"
_AluSIPSnoopingSIPTrustedServerIPAddress2Type_Object = MibScalar
aluSIPSnoopingSIPTrustedServerIPAddress2Type = _AluSIPSnoopingSIPTrustedServerIPAddress2Type_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 4),
    _AluSIPSnoopingSIPTrustedServerIPAddress2Type_Type()
)
aluSIPSnoopingSIPTrustedServerIPAddress2Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingSIPTrustedServerIPAddress2Type.setStatus("current")


class _AluSIPSnoopingSIPTrustedServerIPAddress2_Type(InetAddress):
    """Custom type aluSIPSnoopingSIPTrustedServerIPAddress2 based on InetAddress"""
    defaultHexValue = "00000000"


_AluSIPSnoopingSIPTrustedServerIPAddress2_Type.__name__ = "InetAddress"
_AluSIPSnoopingSIPTrustedServerIPAddress2_Object = MibScalar
aluSIPSnoopingSIPTrustedServerIPAddress2 = _AluSIPSnoopingSIPTrustedServerIPAddress2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 5),
    _AluSIPSnoopingSIPTrustedServerIPAddress2_Type()
)
aluSIPSnoopingSIPTrustedServerIPAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingSIPTrustedServerIPAddress2.setStatus("current")


class _AluSIPSnoopingSIPTrustedServerIPAddress3Type_Type(InetAddressType):
    """Custom type aluSIPSnoopingSIPTrustedServerIPAddress3Type based on InetAddressType"""
    defaultValue = 1

    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ipv4", 1)
    )


_AluSIPSnoopingSIPTrustedServerIPAddress3Type_Type.__name__ = "InetAddressType"
_AluSIPSnoopingSIPTrustedServerIPAddress3Type_Object = MibScalar
aluSIPSnoopingSIPTrustedServerIPAddress3Type = _AluSIPSnoopingSIPTrustedServerIPAddress3Type_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 6),
    _AluSIPSnoopingSIPTrustedServerIPAddress3Type_Type()
)
aluSIPSnoopingSIPTrustedServerIPAddress3Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingSIPTrustedServerIPAddress3Type.setStatus("current")


class _AluSIPSnoopingSIPTrustedServerIPAddress3_Type(InetAddress):
    """Custom type aluSIPSnoopingSIPTrustedServerIPAddress3 based on InetAddress"""
    defaultHexValue = "00000000"


_AluSIPSnoopingSIPTrustedServerIPAddress3_Type.__name__ = "InetAddress"
_AluSIPSnoopingSIPTrustedServerIPAddress3_Object = MibScalar
aluSIPSnoopingSIPTrustedServerIPAddress3 = _AluSIPSnoopingSIPTrustedServerIPAddress3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 7),
    _AluSIPSnoopingSIPTrustedServerIPAddress3_Type()
)
aluSIPSnoopingSIPTrustedServerIPAddress3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingSIPTrustedServerIPAddress3.setStatus("current")


class _AluSIPSnoopingSIPTrustedServerIPAddress4Type_Type(InetAddressType):
    """Custom type aluSIPSnoopingSIPTrustedServerIPAddress4Type based on InetAddressType"""
    defaultValue = 1

    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ipv4", 1)
    )


_AluSIPSnoopingSIPTrustedServerIPAddress4Type_Type.__name__ = "InetAddressType"
_AluSIPSnoopingSIPTrustedServerIPAddress4Type_Object = MibScalar
aluSIPSnoopingSIPTrustedServerIPAddress4Type = _AluSIPSnoopingSIPTrustedServerIPAddress4Type_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 8),
    _AluSIPSnoopingSIPTrustedServerIPAddress4Type_Type()
)
aluSIPSnoopingSIPTrustedServerIPAddress4Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingSIPTrustedServerIPAddress4Type.setStatus("current")


class _AluSIPSnoopingSIPTrustedServerIPAddress4_Type(InetAddress):
    """Custom type aluSIPSnoopingSIPTrustedServerIPAddress4 based on InetAddress"""
    defaultHexValue = "00000000"


_AluSIPSnoopingSIPTrustedServerIPAddress4_Type.__name__ = "InetAddress"
_AluSIPSnoopingSIPTrustedServerIPAddress4_Object = MibScalar
aluSIPSnoopingSIPTrustedServerIPAddress4 = _AluSIPSnoopingSIPTrustedServerIPAddress4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 9),
    _AluSIPSnoopingSIPTrustedServerIPAddress4_Type()
)
aluSIPSnoopingSIPTrustedServerIPAddress4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingSIPTrustedServerIPAddress4.setStatus("current")


class _AluSIPSnoopingSIPTrustedServerIPAddress5Type_Type(InetAddressType):
    """Custom type aluSIPSnoopingSIPTrustedServerIPAddress5Type based on InetAddressType"""
    defaultValue = 1

    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ipv4", 1)
    )


_AluSIPSnoopingSIPTrustedServerIPAddress5Type_Type.__name__ = "InetAddressType"
_AluSIPSnoopingSIPTrustedServerIPAddress5Type_Object = MibScalar
aluSIPSnoopingSIPTrustedServerIPAddress5Type = _AluSIPSnoopingSIPTrustedServerIPAddress5Type_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 10),
    _AluSIPSnoopingSIPTrustedServerIPAddress5Type_Type()
)
aluSIPSnoopingSIPTrustedServerIPAddress5Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingSIPTrustedServerIPAddress5Type.setStatus("current")


class _AluSIPSnoopingSIPTrustedServerIPAddress5_Type(InetAddress):
    """Custom type aluSIPSnoopingSIPTrustedServerIPAddress5 based on InetAddress"""
    defaultHexValue = "00000000"


_AluSIPSnoopingSIPTrustedServerIPAddress5_Type.__name__ = "InetAddress"
_AluSIPSnoopingSIPTrustedServerIPAddress5_Object = MibScalar
aluSIPSnoopingSIPTrustedServerIPAddress5 = _AluSIPSnoopingSIPTrustedServerIPAddress5_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 11),
    _AluSIPSnoopingSIPTrustedServerIPAddress5_Type()
)
aluSIPSnoopingSIPTrustedServerIPAddress5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingSIPTrustedServerIPAddress5.setStatus("current")


class _AluSIPSnoopingSIPTrustedServerIPAddress6Type_Type(InetAddressType):
    """Custom type aluSIPSnoopingSIPTrustedServerIPAddress6Type based on InetAddressType"""
    defaultValue = 1

    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ipv4", 1)
    )


_AluSIPSnoopingSIPTrustedServerIPAddress6Type_Type.__name__ = "InetAddressType"
_AluSIPSnoopingSIPTrustedServerIPAddress6Type_Object = MibScalar
aluSIPSnoopingSIPTrustedServerIPAddress6Type = _AluSIPSnoopingSIPTrustedServerIPAddress6Type_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 12),
    _AluSIPSnoopingSIPTrustedServerIPAddress6Type_Type()
)
aluSIPSnoopingSIPTrustedServerIPAddress6Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingSIPTrustedServerIPAddress6Type.setStatus("current")


class _AluSIPSnoopingSIPTrustedServerIPAddress6_Type(InetAddress):
    """Custom type aluSIPSnoopingSIPTrustedServerIPAddress6 based on InetAddress"""
    defaultHexValue = "00000000"


_AluSIPSnoopingSIPTrustedServerIPAddress6_Type.__name__ = "InetAddress"
_AluSIPSnoopingSIPTrustedServerIPAddress6_Object = MibScalar
aluSIPSnoopingSIPTrustedServerIPAddress6 = _AluSIPSnoopingSIPTrustedServerIPAddress6_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 13),
    _AluSIPSnoopingSIPTrustedServerIPAddress6_Type()
)
aluSIPSnoopingSIPTrustedServerIPAddress6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingSIPTrustedServerIPAddress6.setStatus("current")


class _AluSIPSnoopingSIPTrustedServerIPAddress7Type_Type(InetAddressType):
    """Custom type aluSIPSnoopingSIPTrustedServerIPAddress7Type based on InetAddressType"""
    defaultValue = 1

    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ipv4", 1)
    )


_AluSIPSnoopingSIPTrustedServerIPAddress7Type_Type.__name__ = "InetAddressType"
_AluSIPSnoopingSIPTrustedServerIPAddress7Type_Object = MibScalar
aluSIPSnoopingSIPTrustedServerIPAddress7Type = _AluSIPSnoopingSIPTrustedServerIPAddress7Type_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 14),
    _AluSIPSnoopingSIPTrustedServerIPAddress7Type_Type()
)
aluSIPSnoopingSIPTrustedServerIPAddress7Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingSIPTrustedServerIPAddress7Type.setStatus("current")


class _AluSIPSnoopingSIPTrustedServerIPAddress7_Type(InetAddress):
    """Custom type aluSIPSnoopingSIPTrustedServerIPAddress7 based on InetAddress"""
    defaultHexValue = "00000000"


_AluSIPSnoopingSIPTrustedServerIPAddress7_Type.__name__ = "InetAddress"
_AluSIPSnoopingSIPTrustedServerIPAddress7_Object = MibScalar
aluSIPSnoopingSIPTrustedServerIPAddress7 = _AluSIPSnoopingSIPTrustedServerIPAddress7_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 15),
    _AluSIPSnoopingSIPTrustedServerIPAddress7_Type()
)
aluSIPSnoopingSIPTrustedServerIPAddress7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingSIPTrustedServerIPAddress7.setStatus("current")


class _AluSIPSnoopingSIPTrustedServerIPAddress8Type_Type(InetAddressType):
    """Custom type aluSIPSnoopingSIPTrustedServerIPAddress8Type based on InetAddressType"""
    defaultValue = 1

    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ipv4", 1)
    )


_AluSIPSnoopingSIPTrustedServerIPAddress8Type_Type.__name__ = "InetAddressType"
_AluSIPSnoopingSIPTrustedServerIPAddress8Type_Object = MibScalar
aluSIPSnoopingSIPTrustedServerIPAddress8Type = _AluSIPSnoopingSIPTrustedServerIPAddress8Type_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 16),
    _AluSIPSnoopingSIPTrustedServerIPAddress8Type_Type()
)
aluSIPSnoopingSIPTrustedServerIPAddress8Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingSIPTrustedServerIPAddress8Type.setStatus("current")


class _AluSIPSnoopingSIPTrustedServerIPAddress8_Type(InetAddress):
    """Custom type aluSIPSnoopingSIPTrustedServerIPAddress8 based on InetAddress"""
    defaultHexValue = "00000000"


_AluSIPSnoopingSIPTrustedServerIPAddress8_Type.__name__ = "InetAddress"
_AluSIPSnoopingSIPTrustedServerIPAddress8_Object = MibScalar
aluSIPSnoopingSIPTrustedServerIPAddress8 = _AluSIPSnoopingSIPTrustedServerIPAddress8_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 17),
    _AluSIPSnoopingSIPTrustedServerIPAddress8_Type()
)
aluSIPSnoopingSIPTrustedServerIPAddress8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingSIPTrustedServerIPAddress8.setStatus("current")


class _AluSIPSnoopingSIPControlDSCP_Type(Integer32):
    """Custom type aluSIPSnoopingSIPControlDSCP based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AluSIPSnoopingSIPControlDSCP_Type.__name__ = "Integer32"
_AluSIPSnoopingSIPControlDSCP_Object = MibScalar
aluSIPSnoopingSIPControlDSCP = _AluSIPSnoopingSIPControlDSCP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 18),
    _AluSIPSnoopingSIPControlDSCP_Type()
)
aluSIPSnoopingSIPControlDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingSIPControlDSCP.setStatus("current")


class _AluSIPSnoopingSOSCallNumber1_Type(SnmpAdminString):
    """Custom type aluSIPSnoopingSOSCallNumber1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AluSIPSnoopingSOSCallNumber1_Type.__name__ = "SnmpAdminString"
_AluSIPSnoopingSOSCallNumber1_Object = MibScalar
aluSIPSnoopingSOSCallNumber1 = _AluSIPSnoopingSOSCallNumber1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 19),
    _AluSIPSnoopingSOSCallNumber1_Type()
)
aluSIPSnoopingSOSCallNumber1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingSOSCallNumber1.setStatus("current")


class _AluSIPSnoopingSOSCallNumber2_Type(SnmpAdminString):
    """Custom type aluSIPSnoopingSOSCallNumber2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AluSIPSnoopingSOSCallNumber2_Type.__name__ = "SnmpAdminString"
_AluSIPSnoopingSOSCallNumber2_Object = MibScalar
aluSIPSnoopingSOSCallNumber2 = _AluSIPSnoopingSOSCallNumber2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 20),
    _AluSIPSnoopingSOSCallNumber2_Type()
)
aluSIPSnoopingSOSCallNumber2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingSOSCallNumber2.setStatus("current")


class _AluSIPSnoopingSOSCallNumber3_Type(SnmpAdminString):
    """Custom type aluSIPSnoopingSOSCallNumber3 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AluSIPSnoopingSOSCallNumber3_Type.__name__ = "SnmpAdminString"
_AluSIPSnoopingSOSCallNumber3_Object = MibScalar
aluSIPSnoopingSOSCallNumber3 = _AluSIPSnoopingSOSCallNumber3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 21),
    _AluSIPSnoopingSOSCallNumber3_Type()
)
aluSIPSnoopingSOSCallNumber3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingSOSCallNumber3.setStatus("current")


class _AluSIPSnoopingSOSCallNumber4_Type(SnmpAdminString):
    """Custom type aluSIPSnoopingSOSCallNumber4 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AluSIPSnoopingSOSCallNumber4_Type.__name__ = "SnmpAdminString"
_AluSIPSnoopingSOSCallNumber4_Object = MibScalar
aluSIPSnoopingSOSCallNumber4 = _AluSIPSnoopingSOSCallNumber4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 22),
    _AluSIPSnoopingSOSCallNumber4_Type()
)
aluSIPSnoopingSOSCallNumber4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingSOSCallNumber4.setStatus("current")


class _AluSIPSnoopingSOSCallRTPDSCP_Type(Integer32):
    """Custom type aluSIPSnoopingSOSCallRTPDSCP based on Integer32"""
    defaultValue = 46

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AluSIPSnoopingSOSCallRTPDSCP_Type.__name__ = "Integer32"
_AluSIPSnoopingSOSCallRTPDSCP_Object = MibScalar
aluSIPSnoopingSOSCallRTPDSCP = _AluSIPSnoopingSOSCallRTPDSCP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 23),
    _AluSIPSnoopingSOSCallRTPDSCP_Type()
)
aluSIPSnoopingSOSCallRTPDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingSOSCallRTPDSCP.setStatus("current")


class _AluSIPSnoopingThresholdNumberOfCalls_Type(Integer32):
    """Custom type aluSIPSnoopingThresholdNumberOfCalls based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 500),
    )


_AluSIPSnoopingThresholdNumberOfCalls_Type.__name__ = "Integer32"
_AluSIPSnoopingThresholdNumberOfCalls_Object = MibScalar
aluSIPSnoopingThresholdNumberOfCalls = _AluSIPSnoopingThresholdNumberOfCalls_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 24),
    _AluSIPSnoopingThresholdNumberOfCalls_Type()
)
aluSIPSnoopingThresholdNumberOfCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingThresholdNumberOfCalls.setStatus("current")


class _AluSIPSnoopingClearStats_Type(Integer32):
    """Custom type aluSIPSnoopingClearStats based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AluSIPSnoopingClearStats_Type.__name__ = "Integer32"
_AluSIPSnoopingClearStats_Object = MibScalar
aluSIPSnoopingClearStats = _AluSIPSnoopingClearStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 25),
    _AluSIPSnoopingClearStats_Type()
)
aluSIPSnoopingClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingClearStats.setStatus("current")


class _AluSIPSnoopingSIPUdpPort1_Type(Integer32):
    """Custom type aluSIPSnoopingSIPUdpPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AluSIPSnoopingSIPUdpPort1_Type.__name__ = "Integer32"
_AluSIPSnoopingSIPUdpPort1_Object = MibScalar
aluSIPSnoopingSIPUdpPort1 = _AluSIPSnoopingSIPUdpPort1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 26),
    _AluSIPSnoopingSIPUdpPort1_Type()
)
aluSIPSnoopingSIPUdpPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingSIPUdpPort1.setStatus("current")


class _AluSIPSnoopingSIPUdpPort2_Type(Integer32):
    """Custom type aluSIPSnoopingSIPUdpPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AluSIPSnoopingSIPUdpPort2_Type.__name__ = "Integer32"
_AluSIPSnoopingSIPUdpPort2_Object = MibScalar
aluSIPSnoopingSIPUdpPort2 = _AluSIPSnoopingSIPUdpPort2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 27),
    _AluSIPSnoopingSIPUdpPort2_Type()
)
aluSIPSnoopingSIPUdpPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingSIPUdpPort2.setStatus("current")


class _AluSIPSnoopingSIPUdpPort3_Type(Integer32):
    """Custom type aluSIPSnoopingSIPUdpPort3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AluSIPSnoopingSIPUdpPort3_Type.__name__ = "Integer32"
_AluSIPSnoopingSIPUdpPort3_Object = MibScalar
aluSIPSnoopingSIPUdpPort3 = _AluSIPSnoopingSIPUdpPort3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 28),
    _AluSIPSnoopingSIPUdpPort3_Type()
)
aluSIPSnoopingSIPUdpPort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingSIPUdpPort3.setStatus("current")


class _AluSIPSnoopingSIPUdpPort4_Type(Integer32):
    """Custom type aluSIPSnoopingSIPUdpPort4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AluSIPSnoopingSIPUdpPort4_Type.__name__ = "Integer32"
_AluSIPSnoopingSIPUdpPort4_Object = MibScalar
aluSIPSnoopingSIPUdpPort4 = _AluSIPSnoopingSIPUdpPort4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 29),
    _AluSIPSnoopingSIPUdpPort4_Type()
)
aluSIPSnoopingSIPUdpPort4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingSIPUdpPort4.setStatus("current")


class _AluSIPSnoopingSIPUdpPort5_Type(Integer32):
    """Custom type aluSIPSnoopingSIPUdpPort5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AluSIPSnoopingSIPUdpPort5_Type.__name__ = "Integer32"
_AluSIPSnoopingSIPUdpPort5_Object = MibScalar
aluSIPSnoopingSIPUdpPort5 = _AluSIPSnoopingSIPUdpPort5_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 30),
    _AluSIPSnoopingSIPUdpPort5_Type()
)
aluSIPSnoopingSIPUdpPort5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingSIPUdpPort5.setStatus("current")


class _AluSIPSnoopingSIPUdpPort6_Type(Integer32):
    """Custom type aluSIPSnoopingSIPUdpPort6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AluSIPSnoopingSIPUdpPort6_Type.__name__ = "Integer32"
_AluSIPSnoopingSIPUdpPort6_Object = MibScalar
aluSIPSnoopingSIPUdpPort6 = _AluSIPSnoopingSIPUdpPort6_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 31),
    _AluSIPSnoopingSIPUdpPort6_Type()
)
aluSIPSnoopingSIPUdpPort6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingSIPUdpPort6.setStatus("current")


class _AluSIPSnoopingSIPUdpPort7_Type(Integer32):
    """Custom type aluSIPSnoopingSIPUdpPort7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AluSIPSnoopingSIPUdpPort7_Type.__name__ = "Integer32"
_AluSIPSnoopingSIPUdpPort7_Object = MibScalar
aluSIPSnoopingSIPUdpPort7 = _AluSIPSnoopingSIPUdpPort7_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 32),
    _AluSIPSnoopingSIPUdpPort7_Type()
)
aluSIPSnoopingSIPUdpPort7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingSIPUdpPort7.setStatus("current")


class _AluSIPSnoopingSIPUdpPort8_Type(Integer32):
    """Custom type aluSIPSnoopingSIPUdpPort8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AluSIPSnoopingSIPUdpPort8_Type.__name__ = "Integer32"
_AluSIPSnoopingSIPUdpPort8_Object = MibScalar
aluSIPSnoopingSIPUdpPort8 = _AluSIPSnoopingSIPUdpPort8_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 33),
    _AluSIPSnoopingSIPUdpPort8_Type()
)
aluSIPSnoopingSIPUdpPort8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingSIPUdpPort8.setStatus("current")
_AluSIPSnoopingTotalCallsProcessed_Type = Counter64
_AluSIPSnoopingTotalCallsProcessed_Object = MibScalar
aluSIPSnoopingTotalCallsProcessed = _AluSIPSnoopingTotalCallsProcessed_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 34),
    _AluSIPSnoopingTotalCallsProcessed_Type()
)
aluSIPSnoopingTotalCallsProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingTotalCallsProcessed.setStatus("current")
_AluSIPSnoopingTotalAudioStreams_Type = Counter64
_AluSIPSnoopingTotalAudioStreams_Object = MibScalar
aluSIPSnoopingTotalAudioStreams = _AluSIPSnoopingTotalAudioStreams_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 35),
    _AluSIPSnoopingTotalAudioStreams_Type()
)
aluSIPSnoopingTotalAudioStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingTotalAudioStreams.setStatus("current")
_AluSIPSnoopingTotalVideoStreams_Type = Counter64
_AluSIPSnoopingTotalVideoStreams_Object = MibScalar
aluSIPSnoopingTotalVideoStreams = _AluSIPSnoopingTotalVideoStreams_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 36),
    _AluSIPSnoopingTotalVideoStreams_Type()
)
aluSIPSnoopingTotalVideoStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingTotalVideoStreams.setStatus("current")
_AluSIPSnoopingTotalOtherStreams_Type = Counter64
_AluSIPSnoopingTotalOtherStreams_Object = MibScalar
aluSIPSnoopingTotalOtherStreams = _AluSIPSnoopingTotalOtherStreams_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 37),
    _AluSIPSnoopingTotalOtherStreams_Type()
)
aluSIPSnoopingTotalOtherStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingTotalOtherStreams.setStatus("current")
_AluSIPSnoopingAudioStreamsBeyondThreshold_Type = Counter64
_AluSIPSnoopingAudioStreamsBeyondThreshold_Object = MibScalar
aluSIPSnoopingAudioStreamsBeyondThreshold = _AluSIPSnoopingAudioStreamsBeyondThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 38),
    _AluSIPSnoopingAudioStreamsBeyondThreshold_Type()
)
aluSIPSnoopingAudioStreamsBeyondThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingAudioStreamsBeyondThreshold.setStatus("current")
_AluSIPSnoopingVideoStreamsBeyondThreshold_Type = Counter64
_AluSIPSnoopingVideoStreamsBeyondThreshold_Object = MibScalar
aluSIPSnoopingVideoStreamsBeyondThreshold = _AluSIPSnoopingVideoStreamsBeyondThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 39),
    _AluSIPSnoopingVideoStreamsBeyondThreshold_Type()
)
aluSIPSnoopingVideoStreamsBeyondThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingVideoStreamsBeyondThreshold.setStatus("current")
_AluSIPSnoopingOtherStreamsBeyondThreshold_Type = Counter64
_AluSIPSnoopingOtherStreamsBeyondThreshold_Object = MibScalar
aluSIPSnoopingOtherStreamsBeyondThreshold = _AluSIPSnoopingOtherStreamsBeyondThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 40),
    _AluSIPSnoopingOtherStreamsBeyondThreshold_Type()
)
aluSIPSnoopingOtherStreamsBeyondThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingOtherStreamsBeyondThreshold.setStatus("current")
_AluSIPSnoopingActiveStreamsBeyondThreshold_Type = Counter64
_AluSIPSnoopingActiveStreamsBeyondThreshold_Object = MibScalar
aluSIPSnoopingActiveStreamsBeyondThreshold = _AluSIPSnoopingActiveStreamsBeyondThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 41),
    _AluSIPSnoopingActiveStreamsBeyondThreshold_Type()
)
aluSIPSnoopingActiveStreamsBeyondThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveStreamsBeyondThreshold.setStatus("current")
_AluSIPSnoopingActiveAudioStreams_Type = Counter64
_AluSIPSnoopingActiveAudioStreams_Object = MibScalar
aluSIPSnoopingActiveAudioStreams = _AluSIPSnoopingActiveAudioStreams_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 42),
    _AluSIPSnoopingActiveAudioStreams_Type()
)
aluSIPSnoopingActiveAudioStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveAudioStreams.setStatus("current")
_AluSIPSnoopingActiveVideoStreams_Type = Counter64
_AluSIPSnoopingActiveVideoStreams_Object = MibScalar
aluSIPSnoopingActiveVideoStreams = _AluSIPSnoopingActiveVideoStreams_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 43),
    _AluSIPSnoopingActiveVideoStreams_Type()
)
aluSIPSnoopingActiveVideoStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveVideoStreams.setStatus("current")
_AluSIPSnoopingActiveOtherStreams_Type = Counter64
_AluSIPSnoopingActiveOtherStreams_Object = MibScalar
aluSIPSnoopingActiveOtherStreams = _AluSIPSnoopingActiveOtherStreams_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 44),
    _AluSIPSnoopingActiveOtherStreams_Type()
)
aluSIPSnoopingActiveOtherStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveOtherStreams.setStatus("current")
_AluSIPSnoopingHardwareSIPPackets_Type = Counter64
_AluSIPSnoopingHardwareSIPPackets_Object = MibScalar
aluSIPSnoopingHardwareSIPPackets = _AluSIPSnoopingHardwareSIPPackets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 45),
    _AluSIPSnoopingHardwareSIPPackets_Type()
)
aluSIPSnoopingHardwareSIPPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingHardwareSIPPackets.setStatus("current")
_AluSIPSnoopingSoftwareSIPPackets_Type = Counter64
_AluSIPSnoopingSoftwareSIPPackets_Object = MibScalar
aluSIPSnoopingSoftwareSIPPackets = _AluSIPSnoopingSoftwareSIPPackets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 46),
    _AluSIPSnoopingSoftwareSIPPackets_Type()
)
aluSIPSnoopingSoftwareSIPPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingSoftwareSIPPackets.setStatus("current")
_AluSIPSnoopingSIPInvitePackets_Type = Counter64
_AluSIPSnoopingSIPInvitePackets_Object = MibScalar
aluSIPSnoopingSIPInvitePackets = _AluSIPSnoopingSIPInvitePackets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 47),
    _AluSIPSnoopingSIPInvitePackets_Type()
)
aluSIPSnoopingSIPInvitePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingSIPInvitePackets.setStatus("current")
_AluSIPSnoopingSIPAckPackets_Type = Counter64
_AluSIPSnoopingSIPAckPackets_Object = MibScalar
aluSIPSnoopingSIPAckPackets = _AluSIPSnoopingSIPAckPackets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 48),
    _AluSIPSnoopingSIPAckPackets_Type()
)
aluSIPSnoopingSIPAckPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingSIPAckPackets.setStatus("current")
_AluSIPSnoopingSIPByePackets_Type = Counter64
_AluSIPSnoopingSIPByePackets_Object = MibScalar
aluSIPSnoopingSIPByePackets = _AluSIPSnoopingSIPByePackets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 49),
    _AluSIPSnoopingSIPByePackets_Type()
)
aluSIPSnoopingSIPByePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingSIPByePackets.setStatus("current")
_AluSIPSnoopingSIPUpdatePackets_Type = Counter64
_AluSIPSnoopingSIPUpdatePackets_Object = MibScalar
aluSIPSnoopingSIPUpdatePackets = _AluSIPSnoopingSIPUpdatePackets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 50),
    _AluSIPSnoopingSIPUpdatePackets_Type()
)
aluSIPSnoopingSIPUpdatePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingSIPUpdatePackets.setStatus("current")
_AluSIPSnoopingSIPPrackPackets_Type = Counter64
_AluSIPSnoopingSIPPrackPackets_Object = MibScalar
aluSIPSnoopingSIPPrackPackets = _AluSIPSnoopingSIPPrackPackets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 51),
    _AluSIPSnoopingSIPPrackPackets_Type()
)
aluSIPSnoopingSIPPrackPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingSIPPrackPackets.setStatus("current")
_AluSIPSnoopingSIPRecvdResponsePackets_Type = Counter64
_AluSIPSnoopingSIPRecvdResponsePackets_Object = MibScalar
aluSIPSnoopingSIPRecvdResponsePackets = _AluSIPSnoopingSIPRecvdResponsePackets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 52),
    _AluSIPSnoopingSIPRecvdResponsePackets_Type()
)
aluSIPSnoopingSIPRecvdResponsePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingSIPRecvdResponsePackets.setStatus("current")
_AluSIPSnoopingSIPDiscardedPackets_Type = Counter64
_AluSIPSnoopingSIPDiscardedPackets_Object = MibScalar
aluSIPSnoopingSIPDiscardedPackets = _AluSIPSnoopingSIPDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 53),
    _AluSIPSnoopingSIPDiscardedPackets_Type()
)
aluSIPSnoopingSIPDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingSIPDiscardedPackets.setStatus("current")
_AluSIPSnoopingSIPDiscardedNoTrustServerPackets_Type = Counter64
_AluSIPSnoopingSIPDiscardedNoTrustServerPackets_Object = MibScalar
aluSIPSnoopingSIPDiscardedNoTrustServerPackets = _AluSIPSnoopingSIPDiscardedNoTrustServerPackets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 54),
    _AluSIPSnoopingSIPDiscardedNoTrustServerPackets_Type()
)
aluSIPSnoopingSIPDiscardedNoTrustServerPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingSIPDiscardedNoTrustServerPackets.setStatus("current")
_AluSIPSnoopingSIPDroppedSWErrorPackets_Type = Counter64
_AluSIPSnoopingSIPDroppedSWErrorPackets_Object = MibScalar
aluSIPSnoopingSIPDroppedSWErrorPackets = _AluSIPSnoopingSIPDroppedSWErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 55),
    _AluSIPSnoopingSIPDroppedSWErrorPackets_Type()
)
aluSIPSnoopingSIPDroppedSWErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingSIPDroppedSWErrorPackets.setStatus("current")
_AluSIPSnoopingTotalEmergencyCalls_Type = Counter64
_AluSIPSnoopingTotalEmergencyCalls_Object = MibScalar
aluSIPSnoopingTotalEmergencyCalls = _AluSIPSnoopingTotalEmergencyCalls_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 56),
    _AluSIPSnoopingTotalEmergencyCalls_Type()
)
aluSIPSnoopingTotalEmergencyCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingTotalEmergencyCalls.setStatus("current")


class _AluSIPSnoopingSIPTcpPort1_Type(Integer32):
    """Custom type aluSIPSnoopingSIPTcpPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AluSIPSnoopingSIPTcpPort1_Type.__name__ = "Integer32"
_AluSIPSnoopingSIPTcpPort1_Object = MibScalar
aluSIPSnoopingSIPTcpPort1 = _AluSIPSnoopingSIPTcpPort1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 57),
    _AluSIPSnoopingSIPTcpPort1_Type()
)
aluSIPSnoopingSIPTcpPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingSIPTcpPort1.setStatus("current")


class _AluSIPSnoopingSIPTcpPort2_Type(Integer32):
    """Custom type aluSIPSnoopingSIPTcpPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AluSIPSnoopingSIPTcpPort2_Type.__name__ = "Integer32"
_AluSIPSnoopingSIPTcpPort2_Object = MibScalar
aluSIPSnoopingSIPTcpPort2 = _AluSIPSnoopingSIPTcpPort2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 58),
    _AluSIPSnoopingSIPTcpPort2_Type()
)
aluSIPSnoopingSIPTcpPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingSIPTcpPort2.setStatus("current")


class _AluSIPSnoopingSIPTcpPort3_Type(Integer32):
    """Custom type aluSIPSnoopingSIPTcpPort3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AluSIPSnoopingSIPTcpPort3_Type.__name__ = "Integer32"
_AluSIPSnoopingSIPTcpPort3_Object = MibScalar
aluSIPSnoopingSIPTcpPort3 = _AluSIPSnoopingSIPTcpPort3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 59),
    _AluSIPSnoopingSIPTcpPort3_Type()
)
aluSIPSnoopingSIPTcpPort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingSIPTcpPort3.setStatus("current")


class _AluSIPSnoopingSIPTcpPort4_Type(Integer32):
    """Custom type aluSIPSnoopingSIPTcpPort4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AluSIPSnoopingSIPTcpPort4_Type.__name__ = "Integer32"
_AluSIPSnoopingSIPTcpPort4_Object = MibScalar
aluSIPSnoopingSIPTcpPort4 = _AluSIPSnoopingSIPTcpPort4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 60),
    _AluSIPSnoopingSIPTcpPort4_Type()
)
aluSIPSnoopingSIPTcpPort4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingSIPTcpPort4.setStatus("current")


class _AluSIPSnoopingSIPTcpPort5_Type(Integer32):
    """Custom type aluSIPSnoopingSIPTcpPort5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AluSIPSnoopingSIPTcpPort5_Type.__name__ = "Integer32"
_AluSIPSnoopingSIPTcpPort5_Object = MibScalar
aluSIPSnoopingSIPTcpPort5 = _AluSIPSnoopingSIPTcpPort5_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 61),
    _AluSIPSnoopingSIPTcpPort5_Type()
)
aluSIPSnoopingSIPTcpPort5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingSIPTcpPort5.setStatus("current")


class _AluSIPSnoopingSIPTcpPort6_Type(Integer32):
    """Custom type aluSIPSnoopingSIPTcpPort6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AluSIPSnoopingSIPTcpPort6_Type.__name__ = "Integer32"
_AluSIPSnoopingSIPTcpPort6_Object = MibScalar
aluSIPSnoopingSIPTcpPort6 = _AluSIPSnoopingSIPTcpPort6_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 62),
    _AluSIPSnoopingSIPTcpPort6_Type()
)
aluSIPSnoopingSIPTcpPort6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingSIPTcpPort6.setStatus("current")


class _AluSIPSnoopingSIPTcpPort7_Type(Integer32):
    """Custom type aluSIPSnoopingSIPTcpPort7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AluSIPSnoopingSIPTcpPort7_Type.__name__ = "Integer32"
_AluSIPSnoopingSIPTcpPort7_Object = MibScalar
aluSIPSnoopingSIPTcpPort7 = _AluSIPSnoopingSIPTcpPort7_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 63),
    _AluSIPSnoopingSIPTcpPort7_Type()
)
aluSIPSnoopingSIPTcpPort7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingSIPTcpPort7.setStatus("current")


class _AluSIPSnoopingSIPTcpPort8_Type(Integer32):
    """Custom type aluSIPSnoopingSIPTcpPort8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AluSIPSnoopingSIPTcpPort8_Type.__name__ = "Integer32"
_AluSIPSnoopingSIPTcpPort8_Object = MibScalar
aluSIPSnoopingSIPTcpPort8 = _AluSIPSnoopingSIPTcpPort8_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 64),
    _AluSIPSnoopingSIPTcpPort8_Type()
)
aluSIPSnoopingSIPTcpPort8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingSIPTcpPort8.setStatus("current")


class _AluSIPSnoopingClearEndedCalls_Type(Integer32):
    """Custom type aluSIPSnoopingClearEndedCalls based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AluSIPSnoopingClearEndedCalls_Type.__name__ = "Integer32"
_AluSIPSnoopingClearEndedCalls_Object = MibScalar
aluSIPSnoopingClearEndedCalls = _AluSIPSnoopingClearEndedCalls_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 65),
    _AluSIPSnoopingClearEndedCalls_Type()
)
aluSIPSnoopingClearEndedCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingClearEndedCalls.setStatus("current")


class _AlaSIPSnoopingRsvdHwResources_Type(Integer32):
    """Custom type alaSIPSnoopingRsvdHwResources based on Integer32"""
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
        *(("oneX", 1),
          ("twoX", 2),
          ("threeX", 3),
          ("fourX", 4))
    )


_AlaSIPSnoopingRsvdHwResources_Type.__name__ = "Integer32"
_AlaSIPSnoopingRsvdHwResources_Object = MibScalar
alaSIPSnoopingRsvdHwResources = _AlaSIPSnoopingRsvdHwResources_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 66),
    _AlaSIPSnoopingRsvdHwResources_Type()
)
alaSIPSnoopingRsvdHwResources.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaSIPSnoopingRsvdHwResources.setStatus("current")


class _AlaSIPSnoopingSIPCpuRateLimit_Type(Integer32):
    """Custom type alaSIPSnoopingSIPCpuRateLimit based on Integer32"""
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
        *(("oneMbps", 1),
          ("twoMbps", 2),
          ("threeMbps", 3),
          ("fourMbps", 4))
    )


_AlaSIPSnoopingSIPCpuRateLimit_Type.__name__ = "Integer32"
_AlaSIPSnoopingSIPCpuRateLimit_Object = MibScalar
alaSIPSnoopingSIPCpuRateLimit = _AlaSIPSnoopingSIPCpuRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 1, 67),
    _AlaSIPSnoopingSIPCpuRateLimit_Type()
)
alaSIPSnoopingSIPCpuRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaSIPSnoopingSIPCpuRateLimit.setStatus("current")
_AluSIPSnoopingPortConfigTable_Object = MibTable
aluSIPSnoopingPortConfigTable = _AluSIPSnoopingPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 2)
)
if mibBuilder.loadTexts:
    aluSIPSnoopingPortConfigTable.setStatus("current")
_AluSIPSnoopingPortConfigEntry_Object = MibTableRow
aluSIPSnoopingPortConfigEntry = _AluSIPSnoopingPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 2, 1)
)
aluSIPSnoopingPortConfigEntry.setIndexNames(
    (0, "ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingPortConfigSlotPortIndex"),
)
if mibBuilder.loadTexts:
    aluSIPSnoopingPortConfigEntry.setStatus("current")
_AluSIPSnoopingPortConfigSlotPortIndex_Type = InterfaceIndex
_AluSIPSnoopingPortConfigSlotPortIndex_Object = MibTableColumn
aluSIPSnoopingPortConfigSlotPortIndex = _AluSIPSnoopingPortConfigSlotPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 2, 1, 1),
    _AluSIPSnoopingPortConfigSlotPortIndex_Type()
)
aluSIPSnoopingPortConfigSlotPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluSIPSnoopingPortConfigSlotPortIndex.setStatus("current")


class _AluSIPSnoopingPortConfigPortStatus_Type(Integer32):
    """Custom type aluSIPSnoopingPortConfigPortStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AluSIPSnoopingPortConfigPortStatus_Type.__name__ = "Integer32"
_AluSIPSnoopingPortConfigPortStatus_Object = MibTableColumn
aluSIPSnoopingPortConfigPortStatus = _AluSIPSnoopingPortConfigPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 2, 1, 2),
    _AluSIPSnoopingPortConfigPortStatus_Type()
)
aluSIPSnoopingPortConfigPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingPortConfigPortStatus.setStatus("current")


class _AluSIPSnoopingPortConfigPortMode_Type(Integer32):
    """Custom type aluSIPSnoopingPortConfigPortMode based on Integer32"""
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
        *(("forceEdge", 1),
          ("forceNonEdge", 2),
          ("automatic", 3))
    )


_AluSIPSnoopingPortConfigPortMode_Type.__name__ = "Integer32"
_AluSIPSnoopingPortConfigPortMode_Object = MibTableColumn
aluSIPSnoopingPortConfigPortMode = _AluSIPSnoopingPortConfigPortMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 2, 1, 3),
    _AluSIPSnoopingPortConfigPortMode_Type()
)
aluSIPSnoopingPortConfigPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingPortConfigPortMode.setStatus("current")
_AluSIPSnoopingThresholdTable_Object = MibTable
aluSIPSnoopingThresholdTable = _AluSIPSnoopingThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 3)
)
if mibBuilder.loadTexts:
    aluSIPSnoopingThresholdTable.setStatus("current")
_AluSIPSnoopingThresholdEntry_Object = MibTableRow
aluSIPSnoopingThresholdEntry = _AluSIPSnoopingThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 3, 1)
)
aluSIPSnoopingThresholdEntry.setIndexNames(
    (0, "ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingThresholdMediumIndex"),
)
if mibBuilder.loadTexts:
    aluSIPSnoopingThresholdEntry.setStatus("current")


class _AluSIPSnoopingThresholdMediumIndex_Type(Integer32):
    """Custom type aluSIPSnoopingThresholdMediumIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("audio", 2),
          ("video", 3))
    )


_AluSIPSnoopingThresholdMediumIndex_Type.__name__ = "Integer32"
_AluSIPSnoopingThresholdMediumIndex_Object = MibTableColumn
aluSIPSnoopingThresholdMediumIndex = _AluSIPSnoopingThresholdMediumIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 3, 1, 1),
    _AluSIPSnoopingThresholdMediumIndex_Type()
)
aluSIPSnoopingThresholdMediumIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluSIPSnoopingThresholdMediumIndex.setStatus("current")


class _AluSIPSnoopingThresholdJitter_Type(Integer32):
    """Custom type aluSIPSnoopingThresholdJitter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_AluSIPSnoopingThresholdJitter_Type.__name__ = "Integer32"
_AluSIPSnoopingThresholdJitter_Object = MibTableColumn
aluSIPSnoopingThresholdJitter = _AluSIPSnoopingThresholdJitter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 3, 1, 2),
    _AluSIPSnoopingThresholdJitter_Type()
)
aluSIPSnoopingThresholdJitter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingThresholdJitter.setStatus("current")


class _AluSIPSnoopingThresholdPacketLost_Type(Integer32):
    """Custom type aluSIPSnoopingThresholdPacketLost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AluSIPSnoopingThresholdPacketLost_Type.__name__ = "Integer32"
_AluSIPSnoopingThresholdPacketLost_Object = MibTableColumn
aluSIPSnoopingThresholdPacketLost = _AluSIPSnoopingThresholdPacketLost_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 3, 1, 3),
    _AluSIPSnoopingThresholdPacketLost_Type()
)
aluSIPSnoopingThresholdPacketLost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingThresholdPacketLost.setStatus("current")


class _AluSIPSnoopingThresholdRoundTripDelay_Type(Integer32):
    """Custom type aluSIPSnoopingThresholdRoundTripDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_AluSIPSnoopingThresholdRoundTripDelay_Type.__name__ = "Integer32"
_AluSIPSnoopingThresholdRoundTripDelay_Object = MibTableColumn
aluSIPSnoopingThresholdRoundTripDelay = _AluSIPSnoopingThresholdRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 3, 1, 4),
    _AluSIPSnoopingThresholdRoundTripDelay_Type()
)
aluSIPSnoopingThresholdRoundTripDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingThresholdRoundTripDelay.setStatus("current")


class _AluSIPSnoopingThresholdRFactor_Type(Integer32):
    """Custom type aluSIPSnoopingThresholdRFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AluSIPSnoopingThresholdRFactor_Type.__name__ = "Integer32"
_AluSIPSnoopingThresholdRFactor_Object = MibTableColumn
aluSIPSnoopingThresholdRFactor = _AluSIPSnoopingThresholdRFactor_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 3, 1, 5),
    _AluSIPSnoopingThresholdRFactor_Type()
)
aluSIPSnoopingThresholdRFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingThresholdRFactor.setStatus("current")


class _AluSIPSnoopingThresholdMOS_Type(Integer32):
    """Custom type aluSIPSnoopingThresholdMOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_AluSIPSnoopingThresholdMOS_Type.__name__ = "Integer32"
_AluSIPSnoopingThresholdMOS_Object = MibTableColumn
aluSIPSnoopingThresholdMOS = _AluSIPSnoopingThresholdMOS_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 3, 1, 6),
    _AluSIPSnoopingThresholdMOS_Type()
)
aluSIPSnoopingThresholdMOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSIPSnoopingThresholdMOS.setStatus("current")
if mibBuilder.loadTexts:
    aluSIPSnoopingThresholdMOS.setUnits("tenths of value")
_AluSIPSnoopingActiveCallSummaryTable_Object = MibTable
aluSIPSnoopingActiveCallSummaryTable = _AluSIPSnoopingActiveCallSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 4)
)
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallSummaryTable.setStatus("current")
_AluSIPSnoopingActiveCallSummaryEntry_Object = MibTableRow
aluSIPSnoopingActiveCallSummaryEntry = _AluSIPSnoopingActiveCallSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 4, 1)
)
aluSIPSnoopingActiveCallSummaryEntry.setIndexNames(
    (0, "ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallIndex"),
)
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallSummaryEntry.setStatus("current")


class _AluSIPSnoopingActiveCallIndex_Type(Integer32):
    """Custom type aluSIPSnoopingActiveCallIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8000),
    )


_AluSIPSnoopingActiveCallIndex_Type.__name__ = "Integer32"
_AluSIPSnoopingActiveCallIndex_Object = MibTableColumn
aluSIPSnoopingActiveCallIndex = _AluSIPSnoopingActiveCallIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 4, 1, 1),
    _AluSIPSnoopingActiveCallIndex_Type()
)
aluSIPSnoopingActiveCallIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallIndex.setStatus("current")


class _AluSIPSnoopingActiveCallTagA_Type(SnmpAdminString):
    """Custom type aluSIPSnoopingActiveCallTagA based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AluSIPSnoopingActiveCallTagA_Type.__name__ = "SnmpAdminString"
_AluSIPSnoopingActiveCallTagA_Object = MibTableColumn
aluSIPSnoopingActiveCallTagA = _AluSIPSnoopingActiveCallTagA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 4, 1, 2),
    _AluSIPSnoopingActiveCallTagA_Type()
)
aluSIPSnoopingActiveCallTagA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallTagA.setStatus("current")


class _AluSIPSnoopingActiveCallTagB_Type(SnmpAdminString):
    """Custom type aluSIPSnoopingActiveCallTagB based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AluSIPSnoopingActiveCallTagB_Type.__name__ = "SnmpAdminString"
_AluSIPSnoopingActiveCallTagB_Object = MibTableColumn
aluSIPSnoopingActiveCallTagB = _AluSIPSnoopingActiveCallTagB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 4, 1, 3),
    _AluSIPSnoopingActiveCallTagB_Type()
)
aluSIPSnoopingActiveCallTagB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallTagB.setStatus("current")


class _AluSIPSnoopingActiveCallIpAddrAType_Type(InetAddressType):
    """Custom type aluSIPSnoopingActiveCallIpAddrAType based on InetAddressType"""
    defaultValue = 1

    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ipv4", 1)
    )


_AluSIPSnoopingActiveCallIpAddrAType_Type.__name__ = "InetAddressType"
_AluSIPSnoopingActiveCallIpAddrAType_Object = MibTableColumn
aluSIPSnoopingActiveCallIpAddrAType = _AluSIPSnoopingActiveCallIpAddrAType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 4, 1, 4),
    _AluSIPSnoopingActiveCallIpAddrAType_Type()
)
aluSIPSnoopingActiveCallIpAddrAType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallIpAddrAType.setStatus("current")
_AluSIPSnoopingActiveCallIpAddrA_Type = InetAddress
_AluSIPSnoopingActiveCallIpAddrA_Object = MibTableColumn
aluSIPSnoopingActiveCallIpAddrA = _AluSIPSnoopingActiveCallIpAddrA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 4, 1, 5),
    _AluSIPSnoopingActiveCallIpAddrA_Type()
)
aluSIPSnoopingActiveCallIpAddrA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallIpAddrA.setStatus("current")


class _AluSIPSnoopingActiveCallIpAddrBType_Type(InetAddressType):
    """Custom type aluSIPSnoopingActiveCallIpAddrBType based on InetAddressType"""
    defaultValue = 1

    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ipv4", 1)
    )


_AluSIPSnoopingActiveCallIpAddrBType_Type.__name__ = "InetAddressType"
_AluSIPSnoopingActiveCallIpAddrBType_Object = MibTableColumn
aluSIPSnoopingActiveCallIpAddrBType = _AluSIPSnoopingActiveCallIpAddrBType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 4, 1, 6),
    _AluSIPSnoopingActiveCallIpAddrBType_Type()
)
aluSIPSnoopingActiveCallIpAddrBType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallIpAddrBType.setStatus("current")
_AluSIPSnoopingActiveCallIpAddrB_Type = InetAddress
_AluSIPSnoopingActiveCallIpAddrB_Object = MibTableColumn
aluSIPSnoopingActiveCallIpAddrB = _AluSIPSnoopingActiveCallIpAddrB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 4, 1, 7),
    _AluSIPSnoopingActiveCallIpAddrB_Type()
)
aluSIPSnoopingActiveCallIpAddrB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallIpAddrB.setStatus("current")


class _AluSIPSnoopingActiveCallL4portA_Type(Integer32):
    """Custom type aluSIPSnoopingActiveCallL4portA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AluSIPSnoopingActiveCallL4portA_Type.__name__ = "Integer32"
_AluSIPSnoopingActiveCallL4portA_Object = MibTableColumn
aluSIPSnoopingActiveCallL4portA = _AluSIPSnoopingActiveCallL4portA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 4, 1, 8),
    _AluSIPSnoopingActiveCallL4portA_Type()
)
aluSIPSnoopingActiveCallL4portA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallL4portA.setStatus("current")


class _AluSIPSnoopingActiveCallL4portB_Type(Integer32):
    """Custom type aluSIPSnoopingActiveCallL4portB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AluSIPSnoopingActiveCallL4portB_Type.__name__ = "Integer32"
_AluSIPSnoopingActiveCallL4portB_Object = MibTableColumn
aluSIPSnoopingActiveCallL4portB = _AluSIPSnoopingActiveCallL4portB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 4, 1, 9),
    _AluSIPSnoopingActiveCallL4portB_Type()
)
aluSIPSnoopingActiveCallL4portB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallL4portB.setStatus("current")
_AluSIPSnoopingActiveCallSipMediaType_Type = SnmpAdminString
_AluSIPSnoopingActiveCallSipMediaType_Object = MibTableColumn
aluSIPSnoopingActiveCallSipMediaType = _AluSIPSnoopingActiveCallSipMediaType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 4, 1, 10),
    _AluSIPSnoopingActiveCallSipMediaType_Type()
)
aluSIPSnoopingActiveCallSipMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallSipMediaType.setStatus("current")
_AluSIPSnoopingActiveCallStart_Type = DateAndTime
_AluSIPSnoopingActiveCallStart_Object = MibTableColumn
aluSIPSnoopingActiveCallStart = _AluSIPSnoopingActiveCallStart_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 4, 1, 11),
    _AluSIPSnoopingActiveCallStart_Type()
)
aluSIPSnoopingActiveCallStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStart.setStatus("current")
_AluSIPSnoopingActiveCallRtpCountA_Type = Counter64
_AluSIPSnoopingActiveCallRtpCountA_Object = MibTableColumn
aluSIPSnoopingActiveCallRtpCountA = _AluSIPSnoopingActiveCallRtpCountA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 4, 1, 12),
    _AluSIPSnoopingActiveCallRtpCountA_Type()
)
aluSIPSnoopingActiveCallRtpCountA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallRtpCountA.setStatus("current")
_AluSIPSnoopingActiveCallRtcpCountA_Type = Counter64
_AluSIPSnoopingActiveCallRtcpCountA_Object = MibTableColumn
aluSIPSnoopingActiveCallRtcpCountA = _AluSIPSnoopingActiveCallRtcpCountA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 4, 1, 13),
    _AluSIPSnoopingActiveCallRtcpCountA_Type()
)
aluSIPSnoopingActiveCallRtcpCountA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallRtcpCountA.setStatus("current")
_AluSIPSnoopingActiveCallRuleNameA_Type = SnmpAdminString
_AluSIPSnoopingActiveCallRuleNameA_Object = MibTableColumn
aluSIPSnoopingActiveCallRuleNameA = _AluSIPSnoopingActiveCallRuleNameA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 4, 1, 14),
    _AluSIPSnoopingActiveCallRuleNameA_Type()
)
aluSIPSnoopingActiveCallRuleNameA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallRuleNameA.setStatus("current")
_AluSIPSnoopingActiveCallRtpCountB_Type = Counter64
_AluSIPSnoopingActiveCallRtpCountB_Object = MibTableColumn
aluSIPSnoopingActiveCallRtpCountB = _AluSIPSnoopingActiveCallRtpCountB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 4, 1, 15),
    _AluSIPSnoopingActiveCallRtpCountB_Type()
)
aluSIPSnoopingActiveCallRtpCountB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallRtpCountB.setStatus("current")
_AluSIPSnoopingActiveCallRtcpCountB_Type = Counter64
_AluSIPSnoopingActiveCallRtcpCountB_Object = MibTableColumn
aluSIPSnoopingActiveCallRtcpCountB = _AluSIPSnoopingActiveCallRtcpCountB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 4, 1, 16),
    _AluSIPSnoopingActiveCallRtcpCountB_Type()
)
aluSIPSnoopingActiveCallRtcpCountB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallRtcpCountB.setStatus("current")
_AluSIPSnoopingActiveCallRuleNameB_Type = SnmpAdminString
_AluSIPSnoopingActiveCallRuleNameB_Object = MibTableColumn
aluSIPSnoopingActiveCallRuleNameB = _AluSIPSnoopingActiveCallRuleNameB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 4, 1, 17),
    _AluSIPSnoopingActiveCallRuleNameB_Type()
)
aluSIPSnoopingActiveCallRuleNameB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallRuleNameB.setStatus("current")


class _AluSIPSnoopingActiveCallId_Type(SnmpAdminString):
    """Custom type aluSIPSnoopingActiveCallId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AluSIPSnoopingActiveCallId_Type.__name__ = "SnmpAdminString"
_AluSIPSnoopingActiveCallId_Object = MibTableColumn
aluSIPSnoopingActiveCallId = _AluSIPSnoopingActiveCallId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 4, 1, 18),
    _AluSIPSnoopingActiveCallId_Type()
)
aluSIPSnoopingActiveCallId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallId.setStatus("current")


class _AluSIPSnoopingActiveCallTrustDSCPStatusA_Type(Integer32):
    """Custom type aluSIPSnoopingActiveCallTrustDSCPStatusA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AluSIPSnoopingActiveCallTrustDSCPStatusA_Type.__name__ = "Integer32"
_AluSIPSnoopingActiveCallTrustDSCPStatusA_Object = MibTableColumn
aluSIPSnoopingActiveCallTrustDSCPStatusA = _AluSIPSnoopingActiveCallTrustDSCPStatusA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 4, 1, 19),
    _AluSIPSnoopingActiveCallTrustDSCPStatusA_Type()
)
aluSIPSnoopingActiveCallTrustDSCPStatusA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallTrustDSCPStatusA.setStatus("current")


class _AluSIPSnoopingActiveCallTrustDSCPStatusB_Type(Integer32):
    """Custom type aluSIPSnoopingActiveCallTrustDSCPStatusB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AluSIPSnoopingActiveCallTrustDSCPStatusB_Type.__name__ = "Integer32"
_AluSIPSnoopingActiveCallTrustDSCPStatusB_Object = MibTableColumn
aluSIPSnoopingActiveCallTrustDSCPStatusB = _AluSIPSnoopingActiveCallTrustDSCPStatusB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 4, 1, 20),
    _AluSIPSnoopingActiveCallTrustDSCPStatusB_Type()
)
aluSIPSnoopingActiveCallTrustDSCPStatusB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallTrustDSCPStatusB.setStatus("current")
_AluSIPSnoopingActiveCallPacketCountA_Type = Counter64
_AluSIPSnoopingActiveCallPacketCountA_Object = MibTableColumn
aluSIPSnoopingActiveCallPacketCountA = _AluSIPSnoopingActiveCallPacketCountA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 4, 1, 21),
    _AluSIPSnoopingActiveCallPacketCountA_Type()
)
aluSIPSnoopingActiveCallPacketCountA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallPacketCountA.setStatus("current")
_AluSIPSnoopingActiveCallPacketCountB_Type = Counter64
_AluSIPSnoopingActiveCallPacketCountB_Object = MibTableColumn
aluSIPSnoopingActiveCallPacketCountB = _AluSIPSnoopingActiveCallPacketCountB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 4, 1, 22),
    _AluSIPSnoopingActiveCallPacketCountB_Type()
)
aluSIPSnoopingActiveCallPacketCountB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallPacketCountB.setStatus("current")
_AluSIPSnoopingActiveCallStatsTable_Object = MibTable
aluSIPSnoopingActiveCallStatsTable = _AluSIPSnoopingActiveCallStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 5)
)
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsTable.setStatus("current")
_AluSIPSnoopingActiveCallStatsEntry_Object = MibTableRow
aluSIPSnoopingActiveCallStatsEntry = _AluSIPSnoopingActiveCallStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 5, 1)
)
aluSIPSnoopingActiveCallStatsEntry.setIndexNames(
    (0, "ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallIndex"),
)
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsEntry.setStatus("current")


class _AluSIPSnoopingActiveCallStatsJitterViolationsA_Type(Integer32):
    """Custom type aluSIPSnoopingActiveCallStatsJitterViolationsA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AluSIPSnoopingActiveCallStatsJitterViolationsA_Type.__name__ = "Integer32"
_AluSIPSnoopingActiveCallStatsJitterViolationsA_Object = MibTableColumn
aluSIPSnoopingActiveCallStatsJitterViolationsA = _AluSIPSnoopingActiveCallStatsJitterViolationsA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 5, 1, 1),
    _AluSIPSnoopingActiveCallStatsJitterViolationsA_Type()
)
aluSIPSnoopingActiveCallStatsJitterViolationsA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsJitterViolationsA.setStatus("current")


class _AluSIPSnoopingActiveCallStatsJitterViolationsB_Type(Integer32):
    """Custom type aluSIPSnoopingActiveCallStatsJitterViolationsB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AluSIPSnoopingActiveCallStatsJitterViolationsB_Type.__name__ = "Integer32"
_AluSIPSnoopingActiveCallStatsJitterViolationsB_Object = MibTableColumn
aluSIPSnoopingActiveCallStatsJitterViolationsB = _AluSIPSnoopingActiveCallStatsJitterViolationsB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 5, 1, 2),
    _AluSIPSnoopingActiveCallStatsJitterViolationsB_Type()
)
aluSIPSnoopingActiveCallStatsJitterViolationsB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsJitterViolationsB.setStatus("current")


class _AluSIPSnoopingActiveCallStatsRtdViolationsA_Type(Integer32):
    """Custom type aluSIPSnoopingActiveCallStatsRtdViolationsA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AluSIPSnoopingActiveCallStatsRtdViolationsA_Type.__name__ = "Integer32"
_AluSIPSnoopingActiveCallStatsRtdViolationsA_Object = MibTableColumn
aluSIPSnoopingActiveCallStatsRtdViolationsA = _AluSIPSnoopingActiveCallStatsRtdViolationsA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 5, 1, 3),
    _AluSIPSnoopingActiveCallStatsRtdViolationsA_Type()
)
aluSIPSnoopingActiveCallStatsRtdViolationsA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsRtdViolationsA.setStatus("current")


class _AluSIPSnoopingActiveCallStatsRtdViolationsB_Type(Integer32):
    """Custom type aluSIPSnoopingActiveCallStatsRtdViolationsB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AluSIPSnoopingActiveCallStatsRtdViolationsB_Type.__name__ = "Integer32"
_AluSIPSnoopingActiveCallStatsRtdViolationsB_Object = MibTableColumn
aluSIPSnoopingActiveCallStatsRtdViolationsB = _AluSIPSnoopingActiveCallStatsRtdViolationsB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 5, 1, 4),
    _AluSIPSnoopingActiveCallStatsRtdViolationsB_Type()
)
aluSIPSnoopingActiveCallStatsRtdViolationsB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsRtdViolationsB.setStatus("current")


class _AluSIPSnoopingActiveCallStatsPktLossViolationsA_Type(Integer32):
    """Custom type aluSIPSnoopingActiveCallStatsPktLossViolationsA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AluSIPSnoopingActiveCallStatsPktLossViolationsA_Type.__name__ = "Integer32"
_AluSIPSnoopingActiveCallStatsPktLossViolationsA_Object = MibTableColumn
aluSIPSnoopingActiveCallStatsPktLossViolationsA = _AluSIPSnoopingActiveCallStatsPktLossViolationsA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 5, 1, 5),
    _AluSIPSnoopingActiveCallStatsPktLossViolationsA_Type()
)
aluSIPSnoopingActiveCallStatsPktLossViolationsA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsPktLossViolationsA.setStatus("current")


class _AluSIPSnoopingActiveCallStatsPktLossViolationsB_Type(Integer32):
    """Custom type aluSIPSnoopingActiveCallStatsPktLossViolationsB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AluSIPSnoopingActiveCallStatsPktLossViolationsB_Type.__name__ = "Integer32"
_AluSIPSnoopingActiveCallStatsPktLossViolationsB_Object = MibTableColumn
aluSIPSnoopingActiveCallStatsPktLossViolationsB = _AluSIPSnoopingActiveCallStatsPktLossViolationsB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 5, 1, 6),
    _AluSIPSnoopingActiveCallStatsPktLossViolationsB_Type()
)
aluSIPSnoopingActiveCallStatsPktLossViolationsB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsPktLossViolationsB.setStatus("current")


class _AluSIPSnoopingActiveCallStatsMosViolationsA_Type(Integer32):
    """Custom type aluSIPSnoopingActiveCallStatsMosViolationsA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AluSIPSnoopingActiveCallStatsMosViolationsA_Type.__name__ = "Integer32"
_AluSIPSnoopingActiveCallStatsMosViolationsA_Object = MibTableColumn
aluSIPSnoopingActiveCallStatsMosViolationsA = _AluSIPSnoopingActiveCallStatsMosViolationsA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 5, 1, 7),
    _AluSIPSnoopingActiveCallStatsMosViolationsA_Type()
)
aluSIPSnoopingActiveCallStatsMosViolationsA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsMosViolationsA.setStatus("current")


class _AluSIPSnoopingActiveCallStatsMosViolationsB_Type(Integer32):
    """Custom type aluSIPSnoopingActiveCallStatsMosViolationsB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AluSIPSnoopingActiveCallStatsMosViolationsB_Type.__name__ = "Integer32"
_AluSIPSnoopingActiveCallStatsMosViolationsB_Object = MibTableColumn
aluSIPSnoopingActiveCallStatsMosViolationsB = _AluSIPSnoopingActiveCallStatsMosViolationsB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 5, 1, 8),
    _AluSIPSnoopingActiveCallStatsMosViolationsB_Type()
)
aluSIPSnoopingActiveCallStatsMosViolationsB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsMosViolationsB.setStatus("current")


class _AluSIPSnoopingActiveCallStatsRfactorViolationsA_Type(Integer32):
    """Custom type aluSIPSnoopingActiveCallStatsRfactorViolationsA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AluSIPSnoopingActiveCallStatsRfactorViolationsA_Type.__name__ = "Integer32"
_AluSIPSnoopingActiveCallStatsRfactorViolationsA_Object = MibTableColumn
aluSIPSnoopingActiveCallStatsRfactorViolationsA = _AluSIPSnoopingActiveCallStatsRfactorViolationsA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 5, 1, 9),
    _AluSIPSnoopingActiveCallStatsRfactorViolationsA_Type()
)
aluSIPSnoopingActiveCallStatsRfactorViolationsA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsRfactorViolationsA.setStatus("current")


class _AluSIPSnoopingActiveCallStatsRfactorViolationsB_Type(Integer32):
    """Custom type aluSIPSnoopingActiveCallStatsRfactorViolationsB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AluSIPSnoopingActiveCallStatsRfactorViolationsB_Type.__name__ = "Integer32"
_AluSIPSnoopingActiveCallStatsRfactorViolationsB_Object = MibTableColumn
aluSIPSnoopingActiveCallStatsRfactorViolationsB = _AluSIPSnoopingActiveCallStatsRfactorViolationsB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 5, 1, 10),
    _AluSIPSnoopingActiveCallStatsRfactorViolationsB_Type()
)
aluSIPSnoopingActiveCallStatsRfactorViolationsB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsRfactorViolationsB.setStatus("current")


class _AluSIPSnoopingActiveCallStatsJitterMaxA_Type(Integer32):
    """Custom type aluSIPSnoopingActiveCallStatsJitterMaxA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_AluSIPSnoopingActiveCallStatsJitterMaxA_Type.__name__ = "Integer32"
_AluSIPSnoopingActiveCallStatsJitterMaxA_Object = MibTableColumn
aluSIPSnoopingActiveCallStatsJitterMaxA = _AluSIPSnoopingActiveCallStatsJitterMaxA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 5, 1, 11),
    _AluSIPSnoopingActiveCallStatsJitterMaxA_Type()
)
aluSIPSnoopingActiveCallStatsJitterMaxA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsJitterMaxA.setStatus("current")


class _AluSIPSnoopingActiveCallStatsJitterMinA_Type(Integer32):
    """Custom type aluSIPSnoopingActiveCallStatsJitterMinA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_AluSIPSnoopingActiveCallStatsJitterMinA_Type.__name__ = "Integer32"
_AluSIPSnoopingActiveCallStatsJitterMinA_Object = MibTableColumn
aluSIPSnoopingActiveCallStatsJitterMinA = _AluSIPSnoopingActiveCallStatsJitterMinA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 5, 1, 12),
    _AluSIPSnoopingActiveCallStatsJitterMinA_Type()
)
aluSIPSnoopingActiveCallStatsJitterMinA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsJitterMinA.setStatus("current")


class _AluSIPSnoopingActiveCallStatsJitterAvgA_Type(Integer32):
    """Custom type aluSIPSnoopingActiveCallStatsJitterAvgA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_AluSIPSnoopingActiveCallStatsJitterAvgA_Type.__name__ = "Integer32"
_AluSIPSnoopingActiveCallStatsJitterAvgA_Object = MibTableColumn
aluSIPSnoopingActiveCallStatsJitterAvgA = _AluSIPSnoopingActiveCallStatsJitterAvgA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 5, 1, 13),
    _AluSIPSnoopingActiveCallStatsJitterAvgA_Type()
)
aluSIPSnoopingActiveCallStatsJitterAvgA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsJitterAvgA.setStatus("current")


class _AluSIPSnoopingActiveCallStatsJitterMaxB_Type(Integer32):
    """Custom type aluSIPSnoopingActiveCallStatsJitterMaxB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_AluSIPSnoopingActiveCallStatsJitterMaxB_Type.__name__ = "Integer32"
_AluSIPSnoopingActiveCallStatsJitterMaxB_Object = MibTableColumn
aluSIPSnoopingActiveCallStatsJitterMaxB = _AluSIPSnoopingActiveCallStatsJitterMaxB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 5, 1, 14),
    _AluSIPSnoopingActiveCallStatsJitterMaxB_Type()
)
aluSIPSnoopingActiveCallStatsJitterMaxB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsJitterMaxB.setStatus("current")


class _AluSIPSnoopingActiveCallStatsJitterMinB_Type(Integer32):
    """Custom type aluSIPSnoopingActiveCallStatsJitterMinB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_AluSIPSnoopingActiveCallStatsJitterMinB_Type.__name__ = "Integer32"
_AluSIPSnoopingActiveCallStatsJitterMinB_Object = MibTableColumn
aluSIPSnoopingActiveCallStatsJitterMinB = _AluSIPSnoopingActiveCallStatsJitterMinB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 5, 1, 15),
    _AluSIPSnoopingActiveCallStatsJitterMinB_Type()
)
aluSIPSnoopingActiveCallStatsJitterMinB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsJitterMinB.setStatus("current")


class _AluSIPSnoopingActiveCallStatsJitterAvgB_Type(Integer32):
    """Custom type aluSIPSnoopingActiveCallStatsJitterAvgB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_AluSIPSnoopingActiveCallStatsJitterAvgB_Type.__name__ = "Integer32"
_AluSIPSnoopingActiveCallStatsJitterAvgB_Object = MibTableColumn
aluSIPSnoopingActiveCallStatsJitterAvgB = _AluSIPSnoopingActiveCallStatsJitterAvgB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 5, 1, 16),
    _AluSIPSnoopingActiveCallStatsJitterAvgB_Type()
)
aluSIPSnoopingActiveCallStatsJitterAvgB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsJitterAvgB.setStatus("current")


class _AluSIPSnoopingActiveCallStatsRtdMaxA_Type(Integer32):
    """Custom type aluSIPSnoopingActiveCallStatsRtdMaxA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_AluSIPSnoopingActiveCallStatsRtdMaxA_Type.__name__ = "Integer32"
_AluSIPSnoopingActiveCallStatsRtdMaxA_Object = MibTableColumn
aluSIPSnoopingActiveCallStatsRtdMaxA = _AluSIPSnoopingActiveCallStatsRtdMaxA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 5, 1, 17),
    _AluSIPSnoopingActiveCallStatsRtdMaxA_Type()
)
aluSIPSnoopingActiveCallStatsRtdMaxA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsRtdMaxA.setStatus("current")


class _AluSIPSnoopingActiveCallStatsRtdMinA_Type(Integer32):
    """Custom type aluSIPSnoopingActiveCallStatsRtdMinA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_AluSIPSnoopingActiveCallStatsRtdMinA_Type.__name__ = "Integer32"
_AluSIPSnoopingActiveCallStatsRtdMinA_Object = MibTableColumn
aluSIPSnoopingActiveCallStatsRtdMinA = _AluSIPSnoopingActiveCallStatsRtdMinA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 5, 1, 18),
    _AluSIPSnoopingActiveCallStatsRtdMinA_Type()
)
aluSIPSnoopingActiveCallStatsRtdMinA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsRtdMinA.setStatus("current")


class _AluSIPSnoopingActiveCallStatsRtdAvgA_Type(Integer32):
    """Custom type aluSIPSnoopingActiveCallStatsRtdAvgA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_AluSIPSnoopingActiveCallStatsRtdAvgA_Type.__name__ = "Integer32"
_AluSIPSnoopingActiveCallStatsRtdAvgA_Object = MibTableColumn
aluSIPSnoopingActiveCallStatsRtdAvgA = _AluSIPSnoopingActiveCallStatsRtdAvgA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 5, 1, 19),
    _AluSIPSnoopingActiveCallStatsRtdAvgA_Type()
)
aluSIPSnoopingActiveCallStatsRtdAvgA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsRtdAvgA.setStatus("current")


class _AluSIPSnoopingActiveCallStatsRtdMaxB_Type(Integer32):
    """Custom type aluSIPSnoopingActiveCallStatsRtdMaxB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_AluSIPSnoopingActiveCallStatsRtdMaxB_Type.__name__ = "Integer32"
_AluSIPSnoopingActiveCallStatsRtdMaxB_Object = MibTableColumn
aluSIPSnoopingActiveCallStatsRtdMaxB = _AluSIPSnoopingActiveCallStatsRtdMaxB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 5, 1, 20),
    _AluSIPSnoopingActiveCallStatsRtdMaxB_Type()
)
aluSIPSnoopingActiveCallStatsRtdMaxB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsRtdMaxB.setStatus("current")


class _AluSIPSnoopingActiveCallStatsRtdMinB_Type(Integer32):
    """Custom type aluSIPSnoopingActiveCallStatsRtdMinB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_AluSIPSnoopingActiveCallStatsRtdMinB_Type.__name__ = "Integer32"
_AluSIPSnoopingActiveCallStatsRtdMinB_Object = MibTableColumn
aluSIPSnoopingActiveCallStatsRtdMinB = _AluSIPSnoopingActiveCallStatsRtdMinB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 5, 1, 21),
    _AluSIPSnoopingActiveCallStatsRtdMinB_Type()
)
aluSIPSnoopingActiveCallStatsRtdMinB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsRtdMinB.setStatus("current")


class _AluSIPSnoopingActiveCallStatsRtdAvgB_Type(Integer32):
    """Custom type aluSIPSnoopingActiveCallStatsRtdAvgB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_AluSIPSnoopingActiveCallStatsRtdAvgB_Type.__name__ = "Integer32"
_AluSIPSnoopingActiveCallStatsRtdAvgB_Object = MibTableColumn
aluSIPSnoopingActiveCallStatsRtdAvgB = _AluSIPSnoopingActiveCallStatsRtdAvgB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 5, 1, 22),
    _AluSIPSnoopingActiveCallStatsRtdAvgB_Type()
)
aluSIPSnoopingActiveCallStatsRtdAvgB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsRtdAvgB.setStatus("current")


class _AluSIPSnoopingActiveCallStatsPktLossMaxA_Type(Integer32):
    """Custom type aluSIPSnoopingActiveCallStatsPktLossMaxA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AluSIPSnoopingActiveCallStatsPktLossMaxA_Type.__name__ = "Integer32"
_AluSIPSnoopingActiveCallStatsPktLossMaxA_Object = MibTableColumn
aluSIPSnoopingActiveCallStatsPktLossMaxA = _AluSIPSnoopingActiveCallStatsPktLossMaxA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 5, 1, 23),
    _AluSIPSnoopingActiveCallStatsPktLossMaxA_Type()
)
aluSIPSnoopingActiveCallStatsPktLossMaxA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsPktLossMaxA.setStatus("current")


class _AluSIPSnoopingActiveCallStatsPktLossMinA_Type(Integer32):
    """Custom type aluSIPSnoopingActiveCallStatsPktLossMinA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AluSIPSnoopingActiveCallStatsPktLossMinA_Type.__name__ = "Integer32"
_AluSIPSnoopingActiveCallStatsPktLossMinA_Object = MibTableColumn
aluSIPSnoopingActiveCallStatsPktLossMinA = _AluSIPSnoopingActiveCallStatsPktLossMinA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 5, 1, 24),
    _AluSIPSnoopingActiveCallStatsPktLossMinA_Type()
)
aluSIPSnoopingActiveCallStatsPktLossMinA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsPktLossMinA.setStatus("current")


class _AluSIPSnoopingActiveCallStatsPktLossAvgA_Type(Integer32):
    """Custom type aluSIPSnoopingActiveCallStatsPktLossAvgA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AluSIPSnoopingActiveCallStatsPktLossAvgA_Type.__name__ = "Integer32"
_AluSIPSnoopingActiveCallStatsPktLossAvgA_Object = MibTableColumn
aluSIPSnoopingActiveCallStatsPktLossAvgA = _AluSIPSnoopingActiveCallStatsPktLossAvgA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 5, 1, 25),
    _AluSIPSnoopingActiveCallStatsPktLossAvgA_Type()
)
aluSIPSnoopingActiveCallStatsPktLossAvgA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsPktLossAvgA.setStatus("current")


class _AluSIPSnoopingActiveCallStatsPktLossMaxB_Type(Integer32):
    """Custom type aluSIPSnoopingActiveCallStatsPktLossMaxB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AluSIPSnoopingActiveCallStatsPktLossMaxB_Type.__name__ = "Integer32"
_AluSIPSnoopingActiveCallStatsPktLossMaxB_Object = MibTableColumn
aluSIPSnoopingActiveCallStatsPktLossMaxB = _AluSIPSnoopingActiveCallStatsPktLossMaxB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 5, 1, 26),
    _AluSIPSnoopingActiveCallStatsPktLossMaxB_Type()
)
aluSIPSnoopingActiveCallStatsPktLossMaxB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsPktLossMaxB.setStatus("current")


class _AluSIPSnoopingActiveCallStatsPktLossMinB_Type(Integer32):
    """Custom type aluSIPSnoopingActiveCallStatsPktLossMinB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AluSIPSnoopingActiveCallStatsPktLossMinB_Type.__name__ = "Integer32"
_AluSIPSnoopingActiveCallStatsPktLossMinB_Object = MibTableColumn
aluSIPSnoopingActiveCallStatsPktLossMinB = _AluSIPSnoopingActiveCallStatsPktLossMinB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 5, 1, 27),
    _AluSIPSnoopingActiveCallStatsPktLossMinB_Type()
)
aluSIPSnoopingActiveCallStatsPktLossMinB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsPktLossMinB.setStatus("current")


class _AluSIPSnoopingActiveCallStatsPktLossAvgB_Type(Integer32):
    """Custom type aluSIPSnoopingActiveCallStatsPktLossAvgB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AluSIPSnoopingActiveCallStatsPktLossAvgB_Type.__name__ = "Integer32"
_AluSIPSnoopingActiveCallStatsPktLossAvgB_Object = MibTableColumn
aluSIPSnoopingActiveCallStatsPktLossAvgB = _AluSIPSnoopingActiveCallStatsPktLossAvgB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 5, 1, 28),
    _AluSIPSnoopingActiveCallStatsPktLossAvgB_Type()
)
aluSIPSnoopingActiveCallStatsPktLossAvgB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsPktLossAvgB.setStatus("current")


class _AluSIPSnoopingActiveCallStatsRfactorMaxA_Type(Integer32):
    """Custom type aluSIPSnoopingActiveCallStatsRfactorMaxA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AluSIPSnoopingActiveCallStatsRfactorMaxA_Type.__name__ = "Integer32"
_AluSIPSnoopingActiveCallStatsRfactorMaxA_Object = MibTableColumn
aluSIPSnoopingActiveCallStatsRfactorMaxA = _AluSIPSnoopingActiveCallStatsRfactorMaxA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 5, 1, 29),
    _AluSIPSnoopingActiveCallStatsRfactorMaxA_Type()
)
aluSIPSnoopingActiveCallStatsRfactorMaxA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsRfactorMaxA.setStatus("current")


class _AluSIPSnoopingActiveCallStatsRfactorMinA_Type(Integer32):
    """Custom type aluSIPSnoopingActiveCallStatsRfactorMinA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AluSIPSnoopingActiveCallStatsRfactorMinA_Type.__name__ = "Integer32"
_AluSIPSnoopingActiveCallStatsRfactorMinA_Object = MibTableColumn
aluSIPSnoopingActiveCallStatsRfactorMinA = _AluSIPSnoopingActiveCallStatsRfactorMinA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 5, 1, 30),
    _AluSIPSnoopingActiveCallStatsRfactorMinA_Type()
)
aluSIPSnoopingActiveCallStatsRfactorMinA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsRfactorMinA.setStatus("current")


class _AluSIPSnoopingActiveCallStatsRfactorAvgA_Type(Integer32):
    """Custom type aluSIPSnoopingActiveCallStatsRfactorAvgA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AluSIPSnoopingActiveCallStatsRfactorAvgA_Type.__name__ = "Integer32"
_AluSIPSnoopingActiveCallStatsRfactorAvgA_Object = MibTableColumn
aluSIPSnoopingActiveCallStatsRfactorAvgA = _AluSIPSnoopingActiveCallStatsRfactorAvgA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 5, 1, 31),
    _AluSIPSnoopingActiveCallStatsRfactorAvgA_Type()
)
aluSIPSnoopingActiveCallStatsRfactorAvgA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsRfactorAvgA.setStatus("current")


class _AluSIPSnoopingActiveCallStatsRfactorMaxB_Type(Integer32):
    """Custom type aluSIPSnoopingActiveCallStatsRfactorMaxB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AluSIPSnoopingActiveCallStatsRfactorMaxB_Type.__name__ = "Integer32"
_AluSIPSnoopingActiveCallStatsRfactorMaxB_Object = MibTableColumn
aluSIPSnoopingActiveCallStatsRfactorMaxB = _AluSIPSnoopingActiveCallStatsRfactorMaxB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 5, 1, 32),
    _AluSIPSnoopingActiveCallStatsRfactorMaxB_Type()
)
aluSIPSnoopingActiveCallStatsRfactorMaxB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsRfactorMaxB.setStatus("current")


class _AluSIPSnoopingActiveCallStatsRfactorMinB_Type(Integer32):
    """Custom type aluSIPSnoopingActiveCallStatsRfactorMinB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AluSIPSnoopingActiveCallStatsRfactorMinB_Type.__name__ = "Integer32"
_AluSIPSnoopingActiveCallStatsRfactorMinB_Object = MibTableColumn
aluSIPSnoopingActiveCallStatsRfactorMinB = _AluSIPSnoopingActiveCallStatsRfactorMinB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 5, 1, 33),
    _AluSIPSnoopingActiveCallStatsRfactorMinB_Type()
)
aluSIPSnoopingActiveCallStatsRfactorMinB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsRfactorMinB.setStatus("current")


class _AluSIPSnoopingActiveCallStatsRfactorAvgB_Type(Integer32):
    """Custom type aluSIPSnoopingActiveCallStatsRfactorAvgB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AluSIPSnoopingActiveCallStatsRfactorAvgB_Type.__name__ = "Integer32"
_AluSIPSnoopingActiveCallStatsRfactorAvgB_Object = MibTableColumn
aluSIPSnoopingActiveCallStatsRfactorAvgB = _AluSIPSnoopingActiveCallStatsRfactorAvgB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 5, 1, 34),
    _AluSIPSnoopingActiveCallStatsRfactorAvgB_Type()
)
aluSIPSnoopingActiveCallStatsRfactorAvgB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsRfactorAvgB.setStatus("current")


class _AluSIPSnoopingActiveCallStatsMosMaxA_Type(Integer32):
    """Custom type aluSIPSnoopingActiveCallStatsMosMaxA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_AluSIPSnoopingActiveCallStatsMosMaxA_Type.__name__ = "Integer32"
_AluSIPSnoopingActiveCallStatsMosMaxA_Object = MibTableColumn
aluSIPSnoopingActiveCallStatsMosMaxA = _AluSIPSnoopingActiveCallStatsMosMaxA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 5, 1, 35),
    _AluSIPSnoopingActiveCallStatsMosMaxA_Type()
)
aluSIPSnoopingActiveCallStatsMosMaxA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsMosMaxA.setStatus("current")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsMosMaxA.setUnits("tenths of value")


class _AluSIPSnoopingActiveCallStatsMosMinA_Type(Integer32):
    """Custom type aluSIPSnoopingActiveCallStatsMosMinA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_AluSIPSnoopingActiveCallStatsMosMinA_Type.__name__ = "Integer32"
_AluSIPSnoopingActiveCallStatsMosMinA_Object = MibTableColumn
aluSIPSnoopingActiveCallStatsMosMinA = _AluSIPSnoopingActiveCallStatsMosMinA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 5, 1, 36),
    _AluSIPSnoopingActiveCallStatsMosMinA_Type()
)
aluSIPSnoopingActiveCallStatsMosMinA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsMosMinA.setStatus("current")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsMosMinA.setUnits("tenths of value")


class _AluSIPSnoopingActiveCallStatsMosAvgA_Type(Integer32):
    """Custom type aluSIPSnoopingActiveCallStatsMosAvgA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_AluSIPSnoopingActiveCallStatsMosAvgA_Type.__name__ = "Integer32"
_AluSIPSnoopingActiveCallStatsMosAvgA_Object = MibTableColumn
aluSIPSnoopingActiveCallStatsMosAvgA = _AluSIPSnoopingActiveCallStatsMosAvgA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 5, 1, 37),
    _AluSIPSnoopingActiveCallStatsMosAvgA_Type()
)
aluSIPSnoopingActiveCallStatsMosAvgA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsMosAvgA.setStatus("current")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsMosAvgA.setUnits("tenths of value")


class _AluSIPSnoopingActiveCallStatsMosMaxB_Type(Integer32):
    """Custom type aluSIPSnoopingActiveCallStatsMosMaxB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_AluSIPSnoopingActiveCallStatsMosMaxB_Type.__name__ = "Integer32"
_AluSIPSnoopingActiveCallStatsMosMaxB_Object = MibTableColumn
aluSIPSnoopingActiveCallStatsMosMaxB = _AluSIPSnoopingActiveCallStatsMosMaxB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 5, 1, 38),
    _AluSIPSnoopingActiveCallStatsMosMaxB_Type()
)
aluSIPSnoopingActiveCallStatsMosMaxB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsMosMaxB.setStatus("current")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsMosMaxB.setUnits("tenths of value")


class _AluSIPSnoopingActiveCallStatsMosMinB_Type(Integer32):
    """Custom type aluSIPSnoopingActiveCallStatsMosMinB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_AluSIPSnoopingActiveCallStatsMosMinB_Type.__name__ = "Integer32"
_AluSIPSnoopingActiveCallStatsMosMinB_Object = MibTableColumn
aluSIPSnoopingActiveCallStatsMosMinB = _AluSIPSnoopingActiveCallStatsMosMinB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 5, 1, 39),
    _AluSIPSnoopingActiveCallStatsMosMinB_Type()
)
aluSIPSnoopingActiveCallStatsMosMinB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsMosMinB.setStatus("current")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsMosMinB.setUnits("tenths of value")


class _AluSIPSnoopingActiveCallStatsMosAvgB_Type(Integer32):
    """Custom type aluSIPSnoopingActiveCallStatsMosAvgB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_AluSIPSnoopingActiveCallStatsMosAvgB_Type.__name__ = "Integer32"
_AluSIPSnoopingActiveCallStatsMosAvgB_Object = MibTableColumn
aluSIPSnoopingActiveCallStatsMosAvgB = _AluSIPSnoopingActiveCallStatsMosAvgB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 5, 1, 40),
    _AluSIPSnoopingActiveCallStatsMosAvgB_Type()
)
aluSIPSnoopingActiveCallStatsMosAvgB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsMosAvgB.setStatus("current")
if mibBuilder.loadTexts:
    aluSIPSnoopingActiveCallStatsMosAvgB.setUnits("tenths of value")
_AluSIPSnoopingEndedCallSummaryTable_Object = MibTable
aluSIPSnoopingEndedCallSummaryTable = _AluSIPSnoopingEndedCallSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 6)
)
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallSummaryTable.setStatus("current")
_AluSIPSnoopingEndedCallSummaryEntry_Object = MibTableRow
aluSIPSnoopingEndedCallSummaryEntry = _AluSIPSnoopingEndedCallSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 6, 1)
)
aluSIPSnoopingEndedCallSummaryEntry.setIndexNames(
    (0, "ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallIndex"),
)
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallSummaryEntry.setStatus("current")


class _AluSIPSnoopingEndedCallIndex_Type(Integer32):
    """Custom type aluSIPSnoopingEndedCallIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8000),
    )


_AluSIPSnoopingEndedCallIndex_Type.__name__ = "Integer32"
_AluSIPSnoopingEndedCallIndex_Object = MibTableColumn
aluSIPSnoopingEndedCallIndex = _AluSIPSnoopingEndedCallIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 6, 1, 1),
    _AluSIPSnoopingEndedCallIndex_Type()
)
aluSIPSnoopingEndedCallIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallIndex.setStatus("current")


class _AluSIPSnoopingEndedCallId_Type(SnmpAdminString):
    """Custom type aluSIPSnoopingEndedCallId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AluSIPSnoopingEndedCallId_Type.__name__ = "SnmpAdminString"
_AluSIPSnoopingEndedCallId_Object = MibTableColumn
aluSIPSnoopingEndedCallId = _AluSIPSnoopingEndedCallId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 6, 1, 2),
    _AluSIPSnoopingEndedCallId_Type()
)
aluSIPSnoopingEndedCallId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallId.setStatus("current")


class _AluSIPSnoopingEndedCallTagA_Type(SnmpAdminString):
    """Custom type aluSIPSnoopingEndedCallTagA based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AluSIPSnoopingEndedCallTagA_Type.__name__ = "SnmpAdminString"
_AluSIPSnoopingEndedCallTagA_Object = MibTableColumn
aluSIPSnoopingEndedCallTagA = _AluSIPSnoopingEndedCallTagA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 6, 1, 3),
    _AluSIPSnoopingEndedCallTagA_Type()
)
aluSIPSnoopingEndedCallTagA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallTagA.setStatus("current")


class _AluSIPSnoopingEndedCallTagB_Type(SnmpAdminString):
    """Custom type aluSIPSnoopingEndedCallTagB based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AluSIPSnoopingEndedCallTagB_Type.__name__ = "SnmpAdminString"
_AluSIPSnoopingEndedCallTagB_Object = MibTableColumn
aluSIPSnoopingEndedCallTagB = _AluSIPSnoopingEndedCallTagB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 6, 1, 4),
    _AluSIPSnoopingEndedCallTagB_Type()
)
aluSIPSnoopingEndedCallTagB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallTagB.setStatus("current")


class _AluSIPSnoopingEndedCallIpAddrAType_Type(InetAddressType):
    """Custom type aluSIPSnoopingEndedCallIpAddrAType based on InetAddressType"""
    defaultValue = 1

    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ipv4", 1)
    )


_AluSIPSnoopingEndedCallIpAddrAType_Type.__name__ = "InetAddressType"
_AluSIPSnoopingEndedCallIpAddrAType_Object = MibTableColumn
aluSIPSnoopingEndedCallIpAddrAType = _AluSIPSnoopingEndedCallIpAddrAType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 6, 1, 5),
    _AluSIPSnoopingEndedCallIpAddrAType_Type()
)
aluSIPSnoopingEndedCallIpAddrAType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallIpAddrAType.setStatus("current")
_AluSIPSnoopingEndedCallIpAddrA_Type = InetAddress
_AluSIPSnoopingEndedCallIpAddrA_Object = MibTableColumn
aluSIPSnoopingEndedCallIpAddrA = _AluSIPSnoopingEndedCallIpAddrA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 6, 1, 6),
    _AluSIPSnoopingEndedCallIpAddrA_Type()
)
aluSIPSnoopingEndedCallIpAddrA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallIpAddrA.setStatus("current")


class _AluSIPSnoopingEndedCallIpAddrBType_Type(InetAddressType):
    """Custom type aluSIPSnoopingEndedCallIpAddrBType based on InetAddressType"""
    defaultValue = 1

    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ipv4", 1)
    )


_AluSIPSnoopingEndedCallIpAddrBType_Type.__name__ = "InetAddressType"
_AluSIPSnoopingEndedCallIpAddrBType_Object = MibTableColumn
aluSIPSnoopingEndedCallIpAddrBType = _AluSIPSnoopingEndedCallIpAddrBType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 6, 1, 7),
    _AluSIPSnoopingEndedCallIpAddrBType_Type()
)
aluSIPSnoopingEndedCallIpAddrBType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallIpAddrBType.setStatus("current")
_AluSIPSnoopingEndedCallIpAddrB_Type = InetAddress
_AluSIPSnoopingEndedCallIpAddrB_Object = MibTableColumn
aluSIPSnoopingEndedCallIpAddrB = _AluSIPSnoopingEndedCallIpAddrB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 6, 1, 8),
    _AluSIPSnoopingEndedCallIpAddrB_Type()
)
aluSIPSnoopingEndedCallIpAddrB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallIpAddrB.setStatus("current")


class _AluSIPSnoopingEndedCallL4portA_Type(Integer32):
    """Custom type aluSIPSnoopingEndedCallL4portA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AluSIPSnoopingEndedCallL4portA_Type.__name__ = "Integer32"
_AluSIPSnoopingEndedCallL4portA_Object = MibTableColumn
aluSIPSnoopingEndedCallL4portA = _AluSIPSnoopingEndedCallL4portA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 6, 1, 9),
    _AluSIPSnoopingEndedCallL4portA_Type()
)
aluSIPSnoopingEndedCallL4portA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallL4portA.setStatus("current")


class _AluSIPSnoopingEndedCallL4portB_Type(Integer32):
    """Custom type aluSIPSnoopingEndedCallL4portB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AluSIPSnoopingEndedCallL4portB_Type.__name__ = "Integer32"
_AluSIPSnoopingEndedCallL4portB_Object = MibTableColumn
aluSIPSnoopingEndedCallL4portB = _AluSIPSnoopingEndedCallL4portB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 6, 1, 10),
    _AluSIPSnoopingEndedCallL4portB_Type()
)
aluSIPSnoopingEndedCallL4portB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallL4portB.setStatus("current")
_AluSIPSnoopingEndedCallSipMediaType_Type = SnmpAdminString
_AluSIPSnoopingEndedCallSipMediaType_Object = MibTableColumn
aluSIPSnoopingEndedCallSipMediaType = _AluSIPSnoopingEndedCallSipMediaType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 6, 1, 11),
    _AluSIPSnoopingEndedCallSipMediaType_Type()
)
aluSIPSnoopingEndedCallSipMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallSipMediaType.setStatus("current")
_AluSIPSnoopingEndedCallStart_Type = DateAndTime
_AluSIPSnoopingEndedCallStart_Object = MibTableColumn
aluSIPSnoopingEndedCallStart = _AluSIPSnoopingEndedCallStart_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 6, 1, 12),
    _AluSIPSnoopingEndedCallStart_Type()
)
aluSIPSnoopingEndedCallStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStart.setStatus("current")
_AluSIPSnoopingEndedCallEnd_Type = DateAndTime
_AluSIPSnoopingEndedCallEnd_Object = MibTableColumn
aluSIPSnoopingEndedCallEnd = _AluSIPSnoopingEndedCallEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 6, 1, 13),
    _AluSIPSnoopingEndedCallEnd_Type()
)
aluSIPSnoopingEndedCallEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallEnd.setStatus("current")
_AluSIPSnoopingEndedCallRtpCountA_Type = Counter64
_AluSIPSnoopingEndedCallRtpCountA_Object = MibTableColumn
aluSIPSnoopingEndedCallRtpCountA = _AluSIPSnoopingEndedCallRtpCountA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 6, 1, 14),
    _AluSIPSnoopingEndedCallRtpCountA_Type()
)
aluSIPSnoopingEndedCallRtpCountA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallRtpCountA.setStatus("current")
_AluSIPSnoopingEndedCallRtcpCountA_Type = Counter64
_AluSIPSnoopingEndedCallRtcpCountA_Object = MibTableColumn
aluSIPSnoopingEndedCallRtcpCountA = _AluSIPSnoopingEndedCallRtcpCountA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 6, 1, 15),
    _AluSIPSnoopingEndedCallRtcpCountA_Type()
)
aluSIPSnoopingEndedCallRtcpCountA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallRtcpCountA.setStatus("current")
_AluSIPSnoopingEndedCallRuleNameA_Type = SnmpAdminString
_AluSIPSnoopingEndedCallRuleNameA_Object = MibTableColumn
aluSIPSnoopingEndedCallRuleNameA = _AluSIPSnoopingEndedCallRuleNameA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 6, 1, 16),
    _AluSIPSnoopingEndedCallRuleNameA_Type()
)
aluSIPSnoopingEndedCallRuleNameA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallRuleNameA.setStatus("current")
_AluSIPSnoopingEndedCallRtpCountB_Type = Counter64
_AluSIPSnoopingEndedCallRtpCountB_Object = MibTableColumn
aluSIPSnoopingEndedCallRtpCountB = _AluSIPSnoopingEndedCallRtpCountB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 6, 1, 17),
    _AluSIPSnoopingEndedCallRtpCountB_Type()
)
aluSIPSnoopingEndedCallRtpCountB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallRtpCountB.setStatus("current")
_AluSIPSnoopingEndedCallRtcpCountB_Type = Counter64
_AluSIPSnoopingEndedCallRtcpCountB_Object = MibTableColumn
aluSIPSnoopingEndedCallRtcpCountB = _AluSIPSnoopingEndedCallRtcpCountB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 6, 1, 18),
    _AluSIPSnoopingEndedCallRtcpCountB_Type()
)
aluSIPSnoopingEndedCallRtcpCountB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallRtcpCountB.setStatus("current")
_AluSIPSnoopingEndedCallRuleNameB_Type = SnmpAdminString
_AluSIPSnoopingEndedCallRuleNameB_Object = MibTableColumn
aluSIPSnoopingEndedCallRuleNameB = _AluSIPSnoopingEndedCallRuleNameB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 6, 1, 19),
    _AluSIPSnoopingEndedCallRuleNameB_Type()
)
aluSIPSnoopingEndedCallRuleNameB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallRuleNameB.setStatus("current")
_AluSIPSnoopingEndedCallEndReason_Type = SnmpAdminString
_AluSIPSnoopingEndedCallEndReason_Object = MibTableColumn
aluSIPSnoopingEndedCallEndReason = _AluSIPSnoopingEndedCallEndReason_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 6, 1, 20),
    _AluSIPSnoopingEndedCallEndReason_Type()
)
aluSIPSnoopingEndedCallEndReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallEndReason.setStatus("current")


class _AluSIPSnoopingEndedCallTrustDSCPStatusA_Type(Integer32):
    """Custom type aluSIPSnoopingEndedCallTrustDSCPStatusA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AluSIPSnoopingEndedCallTrustDSCPStatusA_Type.__name__ = "Integer32"
_AluSIPSnoopingEndedCallTrustDSCPStatusA_Object = MibTableColumn
aluSIPSnoopingEndedCallTrustDSCPStatusA = _AluSIPSnoopingEndedCallTrustDSCPStatusA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 6, 1, 21),
    _AluSIPSnoopingEndedCallTrustDSCPStatusA_Type()
)
aluSIPSnoopingEndedCallTrustDSCPStatusA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallTrustDSCPStatusA.setStatus("current")


class _AluSIPSnoopingEndedCallTrustDSCPStatusB_Type(Integer32):
    """Custom type aluSIPSnoopingEndedCallTrustDSCPStatusB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AluSIPSnoopingEndedCallTrustDSCPStatusB_Type.__name__ = "Integer32"
_AluSIPSnoopingEndedCallTrustDSCPStatusB_Object = MibTableColumn
aluSIPSnoopingEndedCallTrustDSCPStatusB = _AluSIPSnoopingEndedCallTrustDSCPStatusB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 6, 1, 22),
    _AluSIPSnoopingEndedCallTrustDSCPStatusB_Type()
)
aluSIPSnoopingEndedCallTrustDSCPStatusB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallTrustDSCPStatusB.setStatus("current")
_AluSIPSnoopingEndedCallPacketCountA_Type = Counter64
_AluSIPSnoopingEndedCallPacketCountA_Object = MibTableColumn
aluSIPSnoopingEndedCallPacketCountA = _AluSIPSnoopingEndedCallPacketCountA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 6, 1, 23),
    _AluSIPSnoopingEndedCallPacketCountA_Type()
)
aluSIPSnoopingEndedCallPacketCountA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallPacketCountA.setStatus("current")
_AluSIPSnoopingEndedCallPacketCountB_Type = Counter64
_AluSIPSnoopingEndedCallPacketCountB_Object = MibTableColumn
aluSIPSnoopingEndedCallPacketCountB = _AluSIPSnoopingEndedCallPacketCountB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 6, 1, 24),
    _AluSIPSnoopingEndedCallPacketCountB_Type()
)
aluSIPSnoopingEndedCallPacketCountB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallPacketCountB.setStatus("current")
_AluSIPSnoopingEndedCallStatsTable_Object = MibTable
aluSIPSnoopingEndedCallStatsTable = _AluSIPSnoopingEndedCallStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 7)
)
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsTable.setStatus("current")
_AluSIPSnoopingEndedCallStatsEntry_Object = MibTableRow
aluSIPSnoopingEndedCallStatsEntry = _AluSIPSnoopingEndedCallStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 7, 1)
)
aluSIPSnoopingEndedCallStatsEntry.setIndexNames(
    (0, "ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallIndex"),
)
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsEntry.setStatus("current")


class _AluSIPSnoopingEndedCallStatsJitterViolationsA_Type(Integer32):
    """Custom type aluSIPSnoopingEndedCallStatsJitterViolationsA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AluSIPSnoopingEndedCallStatsJitterViolationsA_Type.__name__ = "Integer32"
_AluSIPSnoopingEndedCallStatsJitterViolationsA_Object = MibTableColumn
aluSIPSnoopingEndedCallStatsJitterViolationsA = _AluSIPSnoopingEndedCallStatsJitterViolationsA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 7, 1, 1),
    _AluSIPSnoopingEndedCallStatsJitterViolationsA_Type()
)
aluSIPSnoopingEndedCallStatsJitterViolationsA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsJitterViolationsA.setStatus("current")


class _AluSIPSnoopingEndedCallStatsJitterViolationsB_Type(Integer32):
    """Custom type aluSIPSnoopingEndedCallStatsJitterViolationsB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AluSIPSnoopingEndedCallStatsJitterViolationsB_Type.__name__ = "Integer32"
_AluSIPSnoopingEndedCallStatsJitterViolationsB_Object = MibTableColumn
aluSIPSnoopingEndedCallStatsJitterViolationsB = _AluSIPSnoopingEndedCallStatsJitterViolationsB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 7, 1, 2),
    _AluSIPSnoopingEndedCallStatsJitterViolationsB_Type()
)
aluSIPSnoopingEndedCallStatsJitterViolationsB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsJitterViolationsB.setStatus("current")


class _AluSIPSnoopingEndedCallStatsRtdViolationsA_Type(Integer32):
    """Custom type aluSIPSnoopingEndedCallStatsRtdViolationsA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AluSIPSnoopingEndedCallStatsRtdViolationsA_Type.__name__ = "Integer32"
_AluSIPSnoopingEndedCallStatsRtdViolationsA_Object = MibTableColumn
aluSIPSnoopingEndedCallStatsRtdViolationsA = _AluSIPSnoopingEndedCallStatsRtdViolationsA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 7, 1, 3),
    _AluSIPSnoopingEndedCallStatsRtdViolationsA_Type()
)
aluSIPSnoopingEndedCallStatsRtdViolationsA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsRtdViolationsA.setStatus("current")


class _AluSIPSnoopingEndedCallStatsRtdViolationsB_Type(Integer32):
    """Custom type aluSIPSnoopingEndedCallStatsRtdViolationsB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AluSIPSnoopingEndedCallStatsRtdViolationsB_Type.__name__ = "Integer32"
_AluSIPSnoopingEndedCallStatsRtdViolationsB_Object = MibTableColumn
aluSIPSnoopingEndedCallStatsRtdViolationsB = _AluSIPSnoopingEndedCallStatsRtdViolationsB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 7, 1, 4),
    _AluSIPSnoopingEndedCallStatsRtdViolationsB_Type()
)
aluSIPSnoopingEndedCallStatsRtdViolationsB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsRtdViolationsB.setStatus("current")


class _AluSIPSnoopingEndedCallStatsPktLossViolationsA_Type(Integer32):
    """Custom type aluSIPSnoopingEndedCallStatsPktLossViolationsA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AluSIPSnoopingEndedCallStatsPktLossViolationsA_Type.__name__ = "Integer32"
_AluSIPSnoopingEndedCallStatsPktLossViolationsA_Object = MibTableColumn
aluSIPSnoopingEndedCallStatsPktLossViolationsA = _AluSIPSnoopingEndedCallStatsPktLossViolationsA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 7, 1, 5),
    _AluSIPSnoopingEndedCallStatsPktLossViolationsA_Type()
)
aluSIPSnoopingEndedCallStatsPktLossViolationsA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsPktLossViolationsA.setStatus("current")


class _AluSIPSnoopingEndedCallStatsPktLossViolationsB_Type(Integer32):
    """Custom type aluSIPSnoopingEndedCallStatsPktLossViolationsB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AluSIPSnoopingEndedCallStatsPktLossViolationsB_Type.__name__ = "Integer32"
_AluSIPSnoopingEndedCallStatsPktLossViolationsB_Object = MibTableColumn
aluSIPSnoopingEndedCallStatsPktLossViolationsB = _AluSIPSnoopingEndedCallStatsPktLossViolationsB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 7, 1, 6),
    _AluSIPSnoopingEndedCallStatsPktLossViolationsB_Type()
)
aluSIPSnoopingEndedCallStatsPktLossViolationsB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsPktLossViolationsB.setStatus("current")


class _AluSIPSnoopingEndedCallStatsMosViolationsA_Type(Integer32):
    """Custom type aluSIPSnoopingEndedCallStatsMosViolationsA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AluSIPSnoopingEndedCallStatsMosViolationsA_Type.__name__ = "Integer32"
_AluSIPSnoopingEndedCallStatsMosViolationsA_Object = MibTableColumn
aluSIPSnoopingEndedCallStatsMosViolationsA = _AluSIPSnoopingEndedCallStatsMosViolationsA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 7, 1, 7),
    _AluSIPSnoopingEndedCallStatsMosViolationsA_Type()
)
aluSIPSnoopingEndedCallStatsMosViolationsA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsMosViolationsA.setStatus("current")


class _AluSIPSnoopingEndedCallStatsMosViolationsB_Type(Integer32):
    """Custom type aluSIPSnoopingEndedCallStatsMosViolationsB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AluSIPSnoopingEndedCallStatsMosViolationsB_Type.__name__ = "Integer32"
_AluSIPSnoopingEndedCallStatsMosViolationsB_Object = MibTableColumn
aluSIPSnoopingEndedCallStatsMosViolationsB = _AluSIPSnoopingEndedCallStatsMosViolationsB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 7, 1, 8),
    _AluSIPSnoopingEndedCallStatsMosViolationsB_Type()
)
aluSIPSnoopingEndedCallStatsMosViolationsB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsMosViolationsB.setStatus("current")


class _AluSIPSnoopingEndedCallStatsRfactorViolationsA_Type(Integer32):
    """Custom type aluSIPSnoopingEndedCallStatsRfactorViolationsA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AluSIPSnoopingEndedCallStatsRfactorViolationsA_Type.__name__ = "Integer32"
_AluSIPSnoopingEndedCallStatsRfactorViolationsA_Object = MibTableColumn
aluSIPSnoopingEndedCallStatsRfactorViolationsA = _AluSIPSnoopingEndedCallStatsRfactorViolationsA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 7, 1, 9),
    _AluSIPSnoopingEndedCallStatsRfactorViolationsA_Type()
)
aluSIPSnoopingEndedCallStatsRfactorViolationsA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsRfactorViolationsA.setStatus("current")


class _AluSIPSnoopingEndedCallStatsRfactorViolationsB_Type(Integer32):
    """Custom type aluSIPSnoopingEndedCallStatsRfactorViolationsB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AluSIPSnoopingEndedCallStatsRfactorViolationsB_Type.__name__ = "Integer32"
_AluSIPSnoopingEndedCallStatsRfactorViolationsB_Object = MibTableColumn
aluSIPSnoopingEndedCallStatsRfactorViolationsB = _AluSIPSnoopingEndedCallStatsRfactorViolationsB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 7, 1, 10),
    _AluSIPSnoopingEndedCallStatsRfactorViolationsB_Type()
)
aluSIPSnoopingEndedCallStatsRfactorViolationsB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsRfactorViolationsB.setStatus("current")


class _AluSIPSnoopingEndedCallStatsJitterMaxA_Type(Integer32):
    """Custom type aluSIPSnoopingEndedCallStatsJitterMaxA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_AluSIPSnoopingEndedCallStatsJitterMaxA_Type.__name__ = "Integer32"
_AluSIPSnoopingEndedCallStatsJitterMaxA_Object = MibTableColumn
aluSIPSnoopingEndedCallStatsJitterMaxA = _AluSIPSnoopingEndedCallStatsJitterMaxA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 7, 1, 11),
    _AluSIPSnoopingEndedCallStatsJitterMaxA_Type()
)
aluSIPSnoopingEndedCallStatsJitterMaxA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsJitterMaxA.setStatus("current")


class _AluSIPSnoopingEndedCallStatsJitterMinA_Type(Integer32):
    """Custom type aluSIPSnoopingEndedCallStatsJitterMinA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_AluSIPSnoopingEndedCallStatsJitterMinA_Type.__name__ = "Integer32"
_AluSIPSnoopingEndedCallStatsJitterMinA_Object = MibTableColumn
aluSIPSnoopingEndedCallStatsJitterMinA = _AluSIPSnoopingEndedCallStatsJitterMinA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 7, 1, 12),
    _AluSIPSnoopingEndedCallStatsJitterMinA_Type()
)
aluSIPSnoopingEndedCallStatsJitterMinA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsJitterMinA.setStatus("current")


class _AluSIPSnoopingEndedCallStatsJitterAvgA_Type(Integer32):
    """Custom type aluSIPSnoopingEndedCallStatsJitterAvgA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_AluSIPSnoopingEndedCallStatsJitterAvgA_Type.__name__ = "Integer32"
_AluSIPSnoopingEndedCallStatsJitterAvgA_Object = MibTableColumn
aluSIPSnoopingEndedCallStatsJitterAvgA = _AluSIPSnoopingEndedCallStatsJitterAvgA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 7, 1, 13),
    _AluSIPSnoopingEndedCallStatsJitterAvgA_Type()
)
aluSIPSnoopingEndedCallStatsJitterAvgA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsJitterAvgA.setStatus("current")


class _AluSIPSnoopingEndedCallStatsJitterMaxB_Type(Integer32):
    """Custom type aluSIPSnoopingEndedCallStatsJitterMaxB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_AluSIPSnoopingEndedCallStatsJitterMaxB_Type.__name__ = "Integer32"
_AluSIPSnoopingEndedCallStatsJitterMaxB_Object = MibTableColumn
aluSIPSnoopingEndedCallStatsJitterMaxB = _AluSIPSnoopingEndedCallStatsJitterMaxB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 7, 1, 14),
    _AluSIPSnoopingEndedCallStatsJitterMaxB_Type()
)
aluSIPSnoopingEndedCallStatsJitterMaxB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsJitterMaxB.setStatus("current")


class _AluSIPSnoopingEndedCallStatsJitterMinB_Type(Integer32):
    """Custom type aluSIPSnoopingEndedCallStatsJitterMinB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_AluSIPSnoopingEndedCallStatsJitterMinB_Type.__name__ = "Integer32"
_AluSIPSnoopingEndedCallStatsJitterMinB_Object = MibTableColumn
aluSIPSnoopingEndedCallStatsJitterMinB = _AluSIPSnoopingEndedCallStatsJitterMinB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 7, 1, 15),
    _AluSIPSnoopingEndedCallStatsJitterMinB_Type()
)
aluSIPSnoopingEndedCallStatsJitterMinB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsJitterMinB.setStatus("current")


class _AluSIPSnoopingEndedCallStatsJitterAvgB_Type(Integer32):
    """Custom type aluSIPSnoopingEndedCallStatsJitterAvgB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_AluSIPSnoopingEndedCallStatsJitterAvgB_Type.__name__ = "Integer32"
_AluSIPSnoopingEndedCallStatsJitterAvgB_Object = MibTableColumn
aluSIPSnoopingEndedCallStatsJitterAvgB = _AluSIPSnoopingEndedCallStatsJitterAvgB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 7, 1, 16),
    _AluSIPSnoopingEndedCallStatsJitterAvgB_Type()
)
aluSIPSnoopingEndedCallStatsJitterAvgB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsJitterAvgB.setStatus("current")


class _AluSIPSnoopingEndedCallStatsRtdMaxA_Type(Integer32):
    """Custom type aluSIPSnoopingEndedCallStatsRtdMaxA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_AluSIPSnoopingEndedCallStatsRtdMaxA_Type.__name__ = "Integer32"
_AluSIPSnoopingEndedCallStatsRtdMaxA_Object = MibTableColumn
aluSIPSnoopingEndedCallStatsRtdMaxA = _AluSIPSnoopingEndedCallStatsRtdMaxA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 7, 1, 17),
    _AluSIPSnoopingEndedCallStatsRtdMaxA_Type()
)
aluSIPSnoopingEndedCallStatsRtdMaxA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsRtdMaxA.setStatus("current")


class _AluSIPSnoopingEndedCallStatsRtdMinA_Type(Integer32):
    """Custom type aluSIPSnoopingEndedCallStatsRtdMinA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_AluSIPSnoopingEndedCallStatsRtdMinA_Type.__name__ = "Integer32"
_AluSIPSnoopingEndedCallStatsRtdMinA_Object = MibTableColumn
aluSIPSnoopingEndedCallStatsRtdMinA = _AluSIPSnoopingEndedCallStatsRtdMinA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 7, 1, 18),
    _AluSIPSnoopingEndedCallStatsRtdMinA_Type()
)
aluSIPSnoopingEndedCallStatsRtdMinA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsRtdMinA.setStatus("current")


class _AluSIPSnoopingEndedCallStatsRtdAvgA_Type(Integer32):
    """Custom type aluSIPSnoopingEndedCallStatsRtdAvgA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_AluSIPSnoopingEndedCallStatsRtdAvgA_Type.__name__ = "Integer32"
_AluSIPSnoopingEndedCallStatsRtdAvgA_Object = MibTableColumn
aluSIPSnoopingEndedCallStatsRtdAvgA = _AluSIPSnoopingEndedCallStatsRtdAvgA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 7, 1, 19),
    _AluSIPSnoopingEndedCallStatsRtdAvgA_Type()
)
aluSIPSnoopingEndedCallStatsRtdAvgA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsRtdAvgA.setStatus("current")


class _AluSIPSnoopingEndedCallStatsRtdMaxB_Type(Integer32):
    """Custom type aluSIPSnoopingEndedCallStatsRtdMaxB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_AluSIPSnoopingEndedCallStatsRtdMaxB_Type.__name__ = "Integer32"
_AluSIPSnoopingEndedCallStatsRtdMaxB_Object = MibTableColumn
aluSIPSnoopingEndedCallStatsRtdMaxB = _AluSIPSnoopingEndedCallStatsRtdMaxB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 7, 1, 20),
    _AluSIPSnoopingEndedCallStatsRtdMaxB_Type()
)
aluSIPSnoopingEndedCallStatsRtdMaxB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsRtdMaxB.setStatus("current")


class _AluSIPSnoopingEndedCallStatsRtdMinB_Type(Integer32):
    """Custom type aluSIPSnoopingEndedCallStatsRtdMinB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_AluSIPSnoopingEndedCallStatsRtdMinB_Type.__name__ = "Integer32"
_AluSIPSnoopingEndedCallStatsRtdMinB_Object = MibTableColumn
aluSIPSnoopingEndedCallStatsRtdMinB = _AluSIPSnoopingEndedCallStatsRtdMinB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 7, 1, 21),
    _AluSIPSnoopingEndedCallStatsRtdMinB_Type()
)
aluSIPSnoopingEndedCallStatsRtdMinB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsRtdMinB.setStatus("current")


class _AluSIPSnoopingEndedCallStatsRtdAvgB_Type(Integer32):
    """Custom type aluSIPSnoopingEndedCallStatsRtdAvgB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_AluSIPSnoopingEndedCallStatsRtdAvgB_Type.__name__ = "Integer32"
_AluSIPSnoopingEndedCallStatsRtdAvgB_Object = MibTableColumn
aluSIPSnoopingEndedCallStatsRtdAvgB = _AluSIPSnoopingEndedCallStatsRtdAvgB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 7, 1, 22),
    _AluSIPSnoopingEndedCallStatsRtdAvgB_Type()
)
aluSIPSnoopingEndedCallStatsRtdAvgB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsRtdAvgB.setStatus("current")


class _AluSIPSnoopingEndedCallStatsPktLossMaxA_Type(Integer32):
    """Custom type aluSIPSnoopingEndedCallStatsPktLossMaxA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AluSIPSnoopingEndedCallStatsPktLossMaxA_Type.__name__ = "Integer32"
_AluSIPSnoopingEndedCallStatsPktLossMaxA_Object = MibTableColumn
aluSIPSnoopingEndedCallStatsPktLossMaxA = _AluSIPSnoopingEndedCallStatsPktLossMaxA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 7, 1, 23),
    _AluSIPSnoopingEndedCallStatsPktLossMaxA_Type()
)
aluSIPSnoopingEndedCallStatsPktLossMaxA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsPktLossMaxA.setStatus("current")


class _AluSIPSnoopingEndedCallStatsPktLossMinA_Type(Integer32):
    """Custom type aluSIPSnoopingEndedCallStatsPktLossMinA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AluSIPSnoopingEndedCallStatsPktLossMinA_Type.__name__ = "Integer32"
_AluSIPSnoopingEndedCallStatsPktLossMinA_Object = MibTableColumn
aluSIPSnoopingEndedCallStatsPktLossMinA = _AluSIPSnoopingEndedCallStatsPktLossMinA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 7, 1, 24),
    _AluSIPSnoopingEndedCallStatsPktLossMinA_Type()
)
aluSIPSnoopingEndedCallStatsPktLossMinA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsPktLossMinA.setStatus("current")


class _AluSIPSnoopingEndedCallStatsPktLossAvgA_Type(Integer32):
    """Custom type aluSIPSnoopingEndedCallStatsPktLossAvgA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AluSIPSnoopingEndedCallStatsPktLossAvgA_Type.__name__ = "Integer32"
_AluSIPSnoopingEndedCallStatsPktLossAvgA_Object = MibTableColumn
aluSIPSnoopingEndedCallStatsPktLossAvgA = _AluSIPSnoopingEndedCallStatsPktLossAvgA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 7, 1, 25),
    _AluSIPSnoopingEndedCallStatsPktLossAvgA_Type()
)
aluSIPSnoopingEndedCallStatsPktLossAvgA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsPktLossAvgA.setStatus("current")


class _AluSIPSnoopingEndedCallStatsPktLossMaxB_Type(Integer32):
    """Custom type aluSIPSnoopingEndedCallStatsPktLossMaxB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AluSIPSnoopingEndedCallStatsPktLossMaxB_Type.__name__ = "Integer32"
_AluSIPSnoopingEndedCallStatsPktLossMaxB_Object = MibTableColumn
aluSIPSnoopingEndedCallStatsPktLossMaxB = _AluSIPSnoopingEndedCallStatsPktLossMaxB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 7, 1, 26),
    _AluSIPSnoopingEndedCallStatsPktLossMaxB_Type()
)
aluSIPSnoopingEndedCallStatsPktLossMaxB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsPktLossMaxB.setStatus("current")


class _AluSIPSnoopingEndedCallStatsPktLossMinB_Type(Integer32):
    """Custom type aluSIPSnoopingEndedCallStatsPktLossMinB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AluSIPSnoopingEndedCallStatsPktLossMinB_Type.__name__ = "Integer32"
_AluSIPSnoopingEndedCallStatsPktLossMinB_Object = MibTableColumn
aluSIPSnoopingEndedCallStatsPktLossMinB = _AluSIPSnoopingEndedCallStatsPktLossMinB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 7, 1, 27),
    _AluSIPSnoopingEndedCallStatsPktLossMinB_Type()
)
aluSIPSnoopingEndedCallStatsPktLossMinB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsPktLossMinB.setStatus("current")


class _AluSIPSnoopingEndedCallStatsPktLossAvgB_Type(Integer32):
    """Custom type aluSIPSnoopingEndedCallStatsPktLossAvgB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AluSIPSnoopingEndedCallStatsPktLossAvgB_Type.__name__ = "Integer32"
_AluSIPSnoopingEndedCallStatsPktLossAvgB_Object = MibTableColumn
aluSIPSnoopingEndedCallStatsPktLossAvgB = _AluSIPSnoopingEndedCallStatsPktLossAvgB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 7, 1, 28),
    _AluSIPSnoopingEndedCallStatsPktLossAvgB_Type()
)
aluSIPSnoopingEndedCallStatsPktLossAvgB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsPktLossAvgB.setStatus("current")


class _AluSIPSnoopingEndedCallStatsRfactorMaxA_Type(Integer32):
    """Custom type aluSIPSnoopingEndedCallStatsRfactorMaxA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AluSIPSnoopingEndedCallStatsRfactorMaxA_Type.__name__ = "Integer32"
_AluSIPSnoopingEndedCallStatsRfactorMaxA_Object = MibTableColumn
aluSIPSnoopingEndedCallStatsRfactorMaxA = _AluSIPSnoopingEndedCallStatsRfactorMaxA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 7, 1, 29),
    _AluSIPSnoopingEndedCallStatsRfactorMaxA_Type()
)
aluSIPSnoopingEndedCallStatsRfactorMaxA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsRfactorMaxA.setStatus("current")


class _AluSIPSnoopingEndedCallStatsRfactorMinA_Type(Integer32):
    """Custom type aluSIPSnoopingEndedCallStatsRfactorMinA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AluSIPSnoopingEndedCallStatsRfactorMinA_Type.__name__ = "Integer32"
_AluSIPSnoopingEndedCallStatsRfactorMinA_Object = MibTableColumn
aluSIPSnoopingEndedCallStatsRfactorMinA = _AluSIPSnoopingEndedCallStatsRfactorMinA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 7, 1, 30),
    _AluSIPSnoopingEndedCallStatsRfactorMinA_Type()
)
aluSIPSnoopingEndedCallStatsRfactorMinA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsRfactorMinA.setStatus("current")


class _AluSIPSnoopingEndedCallStatsRfactorAvgA_Type(Integer32):
    """Custom type aluSIPSnoopingEndedCallStatsRfactorAvgA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AluSIPSnoopingEndedCallStatsRfactorAvgA_Type.__name__ = "Integer32"
_AluSIPSnoopingEndedCallStatsRfactorAvgA_Object = MibTableColumn
aluSIPSnoopingEndedCallStatsRfactorAvgA = _AluSIPSnoopingEndedCallStatsRfactorAvgA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 7, 1, 31),
    _AluSIPSnoopingEndedCallStatsRfactorAvgA_Type()
)
aluSIPSnoopingEndedCallStatsRfactorAvgA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsRfactorAvgA.setStatus("current")


class _AluSIPSnoopingEndedCallStatsRfactorMaxB_Type(Integer32):
    """Custom type aluSIPSnoopingEndedCallStatsRfactorMaxB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AluSIPSnoopingEndedCallStatsRfactorMaxB_Type.__name__ = "Integer32"
_AluSIPSnoopingEndedCallStatsRfactorMaxB_Object = MibTableColumn
aluSIPSnoopingEndedCallStatsRfactorMaxB = _AluSIPSnoopingEndedCallStatsRfactorMaxB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 7, 1, 32),
    _AluSIPSnoopingEndedCallStatsRfactorMaxB_Type()
)
aluSIPSnoopingEndedCallStatsRfactorMaxB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsRfactorMaxB.setStatus("current")


class _AluSIPSnoopingEndedCallStatsRfactorMinB_Type(Integer32):
    """Custom type aluSIPSnoopingEndedCallStatsRfactorMinB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AluSIPSnoopingEndedCallStatsRfactorMinB_Type.__name__ = "Integer32"
_AluSIPSnoopingEndedCallStatsRfactorMinB_Object = MibTableColumn
aluSIPSnoopingEndedCallStatsRfactorMinB = _AluSIPSnoopingEndedCallStatsRfactorMinB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 7, 1, 33),
    _AluSIPSnoopingEndedCallStatsRfactorMinB_Type()
)
aluSIPSnoopingEndedCallStatsRfactorMinB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsRfactorMinB.setStatus("current")


class _AluSIPSnoopingEndedCallStatsRfactorAvgB_Type(Integer32):
    """Custom type aluSIPSnoopingEndedCallStatsRfactorAvgB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AluSIPSnoopingEndedCallStatsRfactorAvgB_Type.__name__ = "Integer32"
_AluSIPSnoopingEndedCallStatsRfactorAvgB_Object = MibTableColumn
aluSIPSnoopingEndedCallStatsRfactorAvgB = _AluSIPSnoopingEndedCallStatsRfactorAvgB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 7, 1, 34),
    _AluSIPSnoopingEndedCallStatsRfactorAvgB_Type()
)
aluSIPSnoopingEndedCallStatsRfactorAvgB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsRfactorAvgB.setStatus("current")


class _AluSIPSnoopingEndedCallStatsMosMaxA_Type(Integer32):
    """Custom type aluSIPSnoopingEndedCallStatsMosMaxA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_AluSIPSnoopingEndedCallStatsMosMaxA_Type.__name__ = "Integer32"
_AluSIPSnoopingEndedCallStatsMosMaxA_Object = MibTableColumn
aluSIPSnoopingEndedCallStatsMosMaxA = _AluSIPSnoopingEndedCallStatsMosMaxA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 7, 1, 35),
    _AluSIPSnoopingEndedCallStatsMosMaxA_Type()
)
aluSIPSnoopingEndedCallStatsMosMaxA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsMosMaxA.setStatus("current")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsMosMaxA.setUnits("tenths of value")


class _AluSIPSnoopingEndedCallStatsMosMinA_Type(Integer32):
    """Custom type aluSIPSnoopingEndedCallStatsMosMinA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_AluSIPSnoopingEndedCallStatsMosMinA_Type.__name__ = "Integer32"
_AluSIPSnoopingEndedCallStatsMosMinA_Object = MibTableColumn
aluSIPSnoopingEndedCallStatsMosMinA = _AluSIPSnoopingEndedCallStatsMosMinA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 7, 1, 36),
    _AluSIPSnoopingEndedCallStatsMosMinA_Type()
)
aluSIPSnoopingEndedCallStatsMosMinA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsMosMinA.setStatus("current")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsMosMinA.setUnits("tenths of value")


class _AluSIPSnoopingEndedCallStatsMosAvgA_Type(Integer32):
    """Custom type aluSIPSnoopingEndedCallStatsMosAvgA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_AluSIPSnoopingEndedCallStatsMosAvgA_Type.__name__ = "Integer32"
_AluSIPSnoopingEndedCallStatsMosAvgA_Object = MibTableColumn
aluSIPSnoopingEndedCallStatsMosAvgA = _AluSIPSnoopingEndedCallStatsMosAvgA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 7, 1, 37),
    _AluSIPSnoopingEndedCallStatsMosAvgA_Type()
)
aluSIPSnoopingEndedCallStatsMosAvgA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsMosAvgA.setStatus("current")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsMosAvgA.setUnits("tenths of value")


class _AluSIPSnoopingEndedCallStatsMosMaxB_Type(Integer32):
    """Custom type aluSIPSnoopingEndedCallStatsMosMaxB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_AluSIPSnoopingEndedCallStatsMosMaxB_Type.__name__ = "Integer32"
_AluSIPSnoopingEndedCallStatsMosMaxB_Object = MibTableColumn
aluSIPSnoopingEndedCallStatsMosMaxB = _AluSIPSnoopingEndedCallStatsMosMaxB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 7, 1, 38),
    _AluSIPSnoopingEndedCallStatsMosMaxB_Type()
)
aluSIPSnoopingEndedCallStatsMosMaxB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsMosMaxB.setStatus("current")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsMosMaxB.setUnits("tenths of value")


class _AluSIPSnoopingEndedCallStatsMosMinB_Type(Integer32):
    """Custom type aluSIPSnoopingEndedCallStatsMosMinB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_AluSIPSnoopingEndedCallStatsMosMinB_Type.__name__ = "Integer32"
_AluSIPSnoopingEndedCallStatsMosMinB_Object = MibTableColumn
aluSIPSnoopingEndedCallStatsMosMinB = _AluSIPSnoopingEndedCallStatsMosMinB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 7, 1, 39),
    _AluSIPSnoopingEndedCallStatsMosMinB_Type()
)
aluSIPSnoopingEndedCallStatsMosMinB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsMosMinB.setStatus("current")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsMosMinB.setUnits("tenths of value")


class _AluSIPSnoopingEndedCallStatsMosAvgB_Type(Integer32):
    """Custom type aluSIPSnoopingEndedCallStatsMosAvgB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_AluSIPSnoopingEndedCallStatsMosAvgB_Type.__name__ = "Integer32"
_AluSIPSnoopingEndedCallStatsMosAvgB_Object = MibTableColumn
aluSIPSnoopingEndedCallStatsMosAvgB = _AluSIPSnoopingEndedCallStatsMosAvgB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 7, 1, 40),
    _AluSIPSnoopingEndedCallStatsMosAvgB_Type()
)
aluSIPSnoopingEndedCallStatsMosAvgB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsMosAvgB.setStatus("current")
if mibBuilder.loadTexts:
    aluSIPSnoopingEndedCallStatsMosAvgB.setUnits("tenths of value")
_AluSIPSnoopingNotificationObjects_ObjectIdentity = ObjectIdentity
aluSIPSnoopingNotificationObjects = _AluSIPSnoopingNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 8)
)


class _AlaSIPSnoopingCallViolationType_Type(Integer32):
    """Custom type alaSIPSnoopingCallViolationType based on Integer32"""
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
        *(("jitterViolation", 1),
          ("rtdViolation", 2),
          ("mosViolation", 3),
          ("rFactorViolation", 4),
          ("pktLossViolation", 5))
    )


_AlaSIPSnoopingCallViolationType_Type.__name__ = "Integer32"
_AlaSIPSnoopingCallViolationType_Object = MibScalar
alaSIPSnoopingCallViolationType = _AlaSIPSnoopingCallViolationType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 8, 1),
    _AlaSIPSnoopingCallViolationType_Type()
)
alaSIPSnoopingCallViolationType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaSIPSnoopingCallViolationType.setStatus("current")
_AlaSIPSnoopingRegisteredClientsTable_Object = MibTable
alaSIPSnoopingRegisteredClientsTable = _AlaSIPSnoopingRegisteredClientsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 9)
)
if mibBuilder.loadTexts:
    alaSIPSnoopingRegisteredClientsTable.setStatus("current")
_AlaSIPSnoopingRegisteredClientsEntry_Object = MibTableRow
alaSIPSnoopingRegisteredClientsEntry = _AlaSIPSnoopingRegisteredClientsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 9, 1)
)
alaSIPSnoopingRegisteredClientsEntry.setIndexNames(
    (0, "ALCATEL-ENT1-SIP-SNOOPING-MIB", "alaSIPSnoopingRegisteredClientNumber"),
)
if mibBuilder.loadTexts:
    alaSIPSnoopingRegisteredClientsEntry.setStatus("current")


class _AlaSIPSnoopingRegisteredClientNumber_Type(Integer32):
    """Custom type alaSIPSnoopingRegisteredClientNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_AlaSIPSnoopingRegisteredClientNumber_Type.__name__ = "Integer32"
_AlaSIPSnoopingRegisteredClientNumber_Object = MibTableColumn
alaSIPSnoopingRegisteredClientNumber = _AlaSIPSnoopingRegisteredClientNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 9, 1, 1),
    _AlaSIPSnoopingRegisteredClientNumber_Type()
)
alaSIPSnoopingRegisteredClientNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaSIPSnoopingRegisteredClientNumber.setStatus("current")


class _AlaSIPSnoopingRegisteredClientAddrType_Type(InetAddressType):
    """Custom type alaSIPSnoopingRegisteredClientAddrType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ipv4", 1)
    )


_AlaSIPSnoopingRegisteredClientAddrType_Type.__name__ = "InetAddressType"
_AlaSIPSnoopingRegisteredClientAddrType_Object = MibTableColumn
alaSIPSnoopingRegisteredClientAddrType = _AlaSIPSnoopingRegisteredClientAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 9, 1, 2),
    _AlaSIPSnoopingRegisteredClientAddrType_Type()
)
alaSIPSnoopingRegisteredClientAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSIPSnoopingRegisteredClientAddrType.setStatus("current")
_AlaSIPSnoopingRegisteredClientAddr_Type = InetAddress
_AlaSIPSnoopingRegisteredClientAddr_Object = MibTableColumn
alaSIPSnoopingRegisteredClientAddr = _AlaSIPSnoopingRegisteredClientAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 1, 9, 1, 3),
    _AlaSIPSnoopingRegisteredClientAddr_Type()
)
alaSIPSnoopingRegisteredClientAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSIPSnoopingRegisteredClientAddr.setStatus("current")
_AluSIPSnoopingMIBConformance_ObjectIdentity = ObjectIdentity
aluSIPSnoopingMIBConformance = _AluSIPSnoopingMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 2)
)
if mibBuilder.loadTexts:
    aluSIPSnoopingMIBConformance.setStatus("current")
_AluSIPSnoopingMIBGroups_ObjectIdentity = ObjectIdentity
aluSIPSnoopingMIBGroups = _AluSIPSnoopingMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 2, 1)
)
if mibBuilder.loadTexts:
    aluSIPSnoopingMIBGroups.setStatus("current")
_AluSIPSnoopingMIBCompliances_ObjectIdentity = ObjectIdentity
aluSIPSnoopingMIBCompliances = _AluSIPSnoopingMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 2, 2)
)
if mibBuilder.loadTexts:
    aluSIPSnoopingMIBCompliances.setStatus("current")

# Managed Objects groups

aluSIPSnoopingPortConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 2, 1, 1)
)
aluSIPSnoopingPortConfigGroup.setObjects(
      *(("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingPortConfigPortStatus"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingPortConfigPortMode"))
)
if mibBuilder.loadTexts:
    aluSIPSnoopingPortConfigGroup.setStatus("current")

aluSIPSnoopingThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 2, 1, 2)
)
aluSIPSnoopingThresholdGroup.setObjects(
      *(("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingThresholdJitter"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingThresholdPacketLost"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingThresholdRoundTripDelay"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingThresholdRFactor"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingThresholdMOS"))
)
if mibBuilder.loadTexts:
    aluSIPSnoopingThresholdGroup.setStatus("current")

aluSIPSnoopingConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 2, 1, 3)
)
aluSIPSnoopingConfigGroup.setObjects(
      *(("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingStatus"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSIPTrustedServerIPAddress1"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSIPTrustedServerIPAddress1Type"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSIPTrustedServerIPAddress2"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSIPTrustedServerIPAddress2Type"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSIPTrustedServerIPAddress3"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSIPTrustedServerIPAddress3Type"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSIPTrustedServerIPAddress4"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSIPTrustedServerIPAddress4Type"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSIPTrustedServerIPAddress5"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSIPTrustedServerIPAddress5Type"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSIPTrustedServerIPAddress6"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSIPTrustedServerIPAddress6Type"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSIPTrustedServerIPAddress7"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSIPTrustedServerIPAddress7Type"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSIPTrustedServerIPAddress8"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSIPTrustedServerIPAddress8Type"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSIPControlDSCP"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSOSCallNumber1"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSOSCallNumber2"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSOSCallNumber3"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSOSCallNumber4"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSOSCallRTPDSCP"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingThresholdNumberOfCalls"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingClearStats"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingTotalCallsProcessed"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingTotalAudioStreams"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingTotalVideoStreams"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingTotalOtherStreams"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingAudioStreamsBeyondThreshold"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingVideoStreamsBeyondThreshold"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingOtherStreamsBeyondThreshold"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveStreamsBeyondThreshold"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveAudioStreams"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveVideoStreams"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveOtherStreams"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingHardwareSIPPackets"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSoftwareSIPPackets"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSIPInvitePackets"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSIPAckPackets"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSIPByePackets"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSIPUpdatePackets"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSIPPrackPackets"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSIPRecvdResponsePackets"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSIPDiscardedPackets"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSIPDiscardedNoTrustServerPackets"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSIPDroppedSWErrorPackets"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingTotalEmergencyCalls"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingThresholdJitter"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingThresholdPacketLost"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingThresholdRoundTripDelay"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingThresholdRFactor"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingThresholdMOS"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSIPUdpPort1"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSIPUdpPort2"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSIPUdpPort3"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSIPUdpPort4"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSIPUdpPort5"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSIPUdpPort6"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSIPUdpPort7"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSIPUdpPort8"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSIPTcpPort1"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSIPTcpPort2"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSIPTcpPort3"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSIPTcpPort4"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSIPTcpPort5"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSIPTcpPort6"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSIPTcpPort7"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSIPTcpPort8"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingClearEndedCalls"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "alaSIPSnoopingRsvdHwResources"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "alaSIPSnoopingCallViolationType"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "alaSIPSnoopingSIPCpuRateLimit"))
)
if mibBuilder.loadTexts:
    aluSIPSnoopingConfigGroup.setStatus("current")

aluSIPSnoopingSummaryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 2, 1, 4)
)
aluSIPSnoopingSummaryGroup.setObjects(
      *(("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallId"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallTagA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallTagB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallIpAddrA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallIpAddrAType"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallIpAddrB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallIpAddrBType"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallL4portA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallL4portB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallSipMediaType"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallStart"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallRtpCountA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallRtcpCountA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallRuleNameA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallRtpCountB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallRtcpCountB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallRuleNameB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallTrustDSCPStatusA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallTrustDSCPStatusB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallPacketCountA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallPacketCountB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallTagA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallTagB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallIpAddrA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallIpAddrAType"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallIpAddrB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallIpAddrBType"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallL4portA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallL4portB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallSipMediaType"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallStart"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallEnd"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallRtpCountA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallRtcpCountA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallRuleNameA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallRtpCountB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallRtcpCountB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallRuleNameB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallEndReason"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallId"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallTrustDSCPStatusA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallTrustDSCPStatusB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallPacketCountA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallPacketCountB"))
)
if mibBuilder.loadTexts:
    aluSIPSnoopingSummaryGroup.setStatus("current")

aluSIPSnoopingStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 2, 1, 5)
)
aluSIPSnoopingStatsGroup.setObjects(
      *(("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallStatsJitterViolationsA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallStatsJitterViolationsB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallStatsRtdViolationsA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallStatsRtdViolationsB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallStatsPktLossViolationsA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallStatsPktLossViolationsB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallStatsMosViolationsA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallStatsMosViolationsB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallStatsRfactorViolationsA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallStatsRfactorViolationsB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallStatsJitterMaxA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallStatsJitterMinA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallStatsJitterAvgA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallStatsJitterMaxB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallStatsJitterMinB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallStatsJitterAvgB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallStatsRtdMaxA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallStatsRtdMinA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallStatsRtdAvgA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallStatsRtdMaxB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallStatsRtdMinB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallStatsRtdAvgB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallStatsPktLossMaxA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallStatsPktLossMinA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallStatsPktLossAvgA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallStatsPktLossMaxB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallStatsPktLossMinB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallStatsPktLossAvgB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallStatsRfactorMaxA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallStatsRfactorMinA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallStatsRfactorAvgA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallStatsRfactorMaxB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallStatsRfactorMinB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallStatsRfactorAvgB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallStatsMosMaxA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallStatsMosMinA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallStatsMosAvgA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallStatsMosMaxB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallStatsMosMinB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallStatsMosAvgB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallStatsJitterViolationsA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallStatsJitterViolationsB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallStatsRtdViolationsA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallStatsRtdViolationsB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallStatsPktLossViolationsA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallStatsPktLossViolationsB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallStatsMosViolationsA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallStatsMosViolationsB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallStatsRfactorViolationsA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallStatsRfactorViolationsB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallStatsJitterMaxA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallStatsJitterMinA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallStatsJitterAvgA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallStatsJitterMaxB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallStatsJitterMinB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallStatsJitterAvgB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallStatsRtdMaxA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallStatsRtdMinA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallStatsRtdAvgA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallStatsRtdMaxB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallStatsRtdMinB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallStatsRtdAvgB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallStatsPktLossMaxA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallStatsPktLossMinA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallStatsPktLossAvgA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallStatsPktLossMaxB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallStatsPktLossMinB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallStatsPktLossAvgB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallStatsRfactorMaxA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallStatsRfactorMinA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallStatsRfactorAvgA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallStatsRfactorMaxB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallStatsRfactorMinB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallStatsRfactorAvgB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallStatsMosMaxA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallStatsMosMinA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallStatsMosAvgA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallStatsMosMaxB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallStatsMosMinB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallStatsMosAvgB"))
)
if mibBuilder.loadTexts:
    aluSIPSnoopingStatsGroup.setStatus("current")

alaSIPSnoopingRegisteredClientsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 2, 1, 7)
)
alaSIPSnoopingRegisteredClientsGroup.setObjects(
      *(("ALCATEL-ENT1-SIP-SNOOPING-MIB", "alaSIPSnoopingRegisteredClientAddrType"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "alaSIPSnoopingRegisteredClientAddr"))
)
if mibBuilder.loadTexts:
    alaSIPSnoopingRegisteredClientsGroup.setStatus("current")


# Notification objects

alaSIPSnoopingRTCPOverThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 0, 1)
)
alaSIPSnoopingRTCPOverThreshold.setObjects(
      *(("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallIpAddrA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallIpAddrB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallL4portB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingActiveCallSipMediaType"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "alaSIPSnoopingCallViolationType"))
)
if mibBuilder.loadTexts:
    alaSIPSnoopingRTCPOverThreshold.setStatus(
        "current"
    )

alaSIPSnoopingSignallingLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 0, 2)
)
alaSIPSnoopingSignallingLost.setObjects(
    ("ALCATEL-ENT1-CHASSIS-MIB", "physicalIndex")
)
if mibBuilder.loadTexts:
    alaSIPSnoopingSignallingLost.setStatus(
        "current"
    )

alaSIPSnoopingRTCPPktsLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 0, 3)
)
alaSIPSnoopingRTCPPktsLost.setObjects(
    ("ALCATEL-ENT1-CHASSIS-MIB", "physicalIndex")
)
if mibBuilder.loadTexts:
    alaSIPSnoopingRTCPPktsLost.setStatus(
        "current"
    )

alaSIPSnoopingACLPreemptedBySOSCall = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 0, 4)
)
alaSIPSnoopingACLPreemptedBySOSCall.setObjects(
      *(("ALCATEL-ENT1-CHASSIS-MIB", "physicalIndex"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallIpAddrA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallIpAddrB"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallL4portA"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingEndedCallL4portB"))
)
if mibBuilder.loadTexts:
    alaSIPSnoopingACLPreemptedBySOSCall.setStatus(
        "current"
    )

alaSIPSnoopingCallRecordsFileMoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 0, 5)
)
alaSIPSnoopingCallRecordsFileMoved.setObjects(
    ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingThresholdNumberOfCalls")
)
if mibBuilder.loadTexts:
    alaSIPSnoopingCallRecordsFileMoved.setStatus(
        "current"
    )


# Notifications groups

alaSIPSnoopingNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 2, 1, 6)
)
alaSIPSnoopingNotificationGroup.setObjects(
      *(("ALCATEL-ENT1-SIP-SNOOPING-MIB", "alaSIPSnoopingRTCPOverThreshold"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "alaSIPSnoopingSignallingLost"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "alaSIPSnoopingRTCPPktsLost"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "alaSIPSnoopingACLPreemptedBySOSCall"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "alaSIPSnoopingCallRecordsFileMoved"))
)
if mibBuilder.loadTexts:
    alaSIPSnoopingNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

aluSIPSnoopingMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76, 1, 2, 2, 1)
)
aluSIPSnoopingMIBCompliance.setObjects(
      *(("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingPortConfigGroup"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingThresholdGroup"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingConfigGroup"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingSummaryGroup"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "aluSIPSnoopingStatsGroup"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "alaSIPSnoopingNotificationGroup"),
        ("ALCATEL-ENT1-SIP-SNOOPING-MIB", "alaSIPSnoopingRegisteredClientsGroup"))
)
if mibBuilder.loadTexts:
    aluSIPSnoopingMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-ENT1-SIP-SNOOPING-MIB",
    **{"aluSIPSnoopingMIB": aluSIPSnoopingMIB,
       "aluSIPSnoopingMIBNotifications": aluSIPSnoopingMIBNotifications,
       "alaSIPSnoopingRTCPOverThreshold": alaSIPSnoopingRTCPOverThreshold,
       "alaSIPSnoopingSignallingLost": alaSIPSnoopingSignallingLost,
       "alaSIPSnoopingRTCPPktsLost": alaSIPSnoopingRTCPPktsLost,
       "alaSIPSnoopingACLPreemptedBySOSCall": alaSIPSnoopingACLPreemptedBySOSCall,
       "alaSIPSnoopingCallRecordsFileMoved": alaSIPSnoopingCallRecordsFileMoved,
       "aluSIPSnoopingMIBObjects": aluSIPSnoopingMIBObjects,
       "aluSIPSnoopingConfig": aluSIPSnoopingConfig,
       "aluSIPSnoopingStatus": aluSIPSnoopingStatus,
       "aluSIPSnoopingSIPTrustedServerIPAddress1Type": aluSIPSnoopingSIPTrustedServerIPAddress1Type,
       "aluSIPSnoopingSIPTrustedServerIPAddress1": aluSIPSnoopingSIPTrustedServerIPAddress1,
       "aluSIPSnoopingSIPTrustedServerIPAddress2Type": aluSIPSnoopingSIPTrustedServerIPAddress2Type,
       "aluSIPSnoopingSIPTrustedServerIPAddress2": aluSIPSnoopingSIPTrustedServerIPAddress2,
       "aluSIPSnoopingSIPTrustedServerIPAddress3Type": aluSIPSnoopingSIPTrustedServerIPAddress3Type,
       "aluSIPSnoopingSIPTrustedServerIPAddress3": aluSIPSnoopingSIPTrustedServerIPAddress3,
       "aluSIPSnoopingSIPTrustedServerIPAddress4Type": aluSIPSnoopingSIPTrustedServerIPAddress4Type,
       "aluSIPSnoopingSIPTrustedServerIPAddress4": aluSIPSnoopingSIPTrustedServerIPAddress4,
       "aluSIPSnoopingSIPTrustedServerIPAddress5Type": aluSIPSnoopingSIPTrustedServerIPAddress5Type,
       "aluSIPSnoopingSIPTrustedServerIPAddress5": aluSIPSnoopingSIPTrustedServerIPAddress5,
       "aluSIPSnoopingSIPTrustedServerIPAddress6Type": aluSIPSnoopingSIPTrustedServerIPAddress6Type,
       "aluSIPSnoopingSIPTrustedServerIPAddress6": aluSIPSnoopingSIPTrustedServerIPAddress6,
       "aluSIPSnoopingSIPTrustedServerIPAddress7Type": aluSIPSnoopingSIPTrustedServerIPAddress7Type,
       "aluSIPSnoopingSIPTrustedServerIPAddress7": aluSIPSnoopingSIPTrustedServerIPAddress7,
       "aluSIPSnoopingSIPTrustedServerIPAddress8Type": aluSIPSnoopingSIPTrustedServerIPAddress8Type,
       "aluSIPSnoopingSIPTrustedServerIPAddress8": aluSIPSnoopingSIPTrustedServerIPAddress8,
       "aluSIPSnoopingSIPControlDSCP": aluSIPSnoopingSIPControlDSCP,
       "aluSIPSnoopingSOSCallNumber1": aluSIPSnoopingSOSCallNumber1,
       "aluSIPSnoopingSOSCallNumber2": aluSIPSnoopingSOSCallNumber2,
       "aluSIPSnoopingSOSCallNumber3": aluSIPSnoopingSOSCallNumber3,
       "aluSIPSnoopingSOSCallNumber4": aluSIPSnoopingSOSCallNumber4,
       "aluSIPSnoopingSOSCallRTPDSCP": aluSIPSnoopingSOSCallRTPDSCP,
       "aluSIPSnoopingThresholdNumberOfCalls": aluSIPSnoopingThresholdNumberOfCalls,
       "aluSIPSnoopingClearStats": aluSIPSnoopingClearStats,
       "aluSIPSnoopingSIPUdpPort1": aluSIPSnoopingSIPUdpPort1,
       "aluSIPSnoopingSIPUdpPort2": aluSIPSnoopingSIPUdpPort2,
       "aluSIPSnoopingSIPUdpPort3": aluSIPSnoopingSIPUdpPort3,
       "aluSIPSnoopingSIPUdpPort4": aluSIPSnoopingSIPUdpPort4,
       "aluSIPSnoopingSIPUdpPort5": aluSIPSnoopingSIPUdpPort5,
       "aluSIPSnoopingSIPUdpPort6": aluSIPSnoopingSIPUdpPort6,
       "aluSIPSnoopingSIPUdpPort7": aluSIPSnoopingSIPUdpPort7,
       "aluSIPSnoopingSIPUdpPort8": aluSIPSnoopingSIPUdpPort8,
       "aluSIPSnoopingTotalCallsProcessed": aluSIPSnoopingTotalCallsProcessed,
       "aluSIPSnoopingTotalAudioStreams": aluSIPSnoopingTotalAudioStreams,
       "aluSIPSnoopingTotalVideoStreams": aluSIPSnoopingTotalVideoStreams,
       "aluSIPSnoopingTotalOtherStreams": aluSIPSnoopingTotalOtherStreams,
       "aluSIPSnoopingAudioStreamsBeyondThreshold": aluSIPSnoopingAudioStreamsBeyondThreshold,
       "aluSIPSnoopingVideoStreamsBeyondThreshold": aluSIPSnoopingVideoStreamsBeyondThreshold,
       "aluSIPSnoopingOtherStreamsBeyondThreshold": aluSIPSnoopingOtherStreamsBeyondThreshold,
       "aluSIPSnoopingActiveStreamsBeyondThreshold": aluSIPSnoopingActiveStreamsBeyondThreshold,
       "aluSIPSnoopingActiveAudioStreams": aluSIPSnoopingActiveAudioStreams,
       "aluSIPSnoopingActiveVideoStreams": aluSIPSnoopingActiveVideoStreams,
       "aluSIPSnoopingActiveOtherStreams": aluSIPSnoopingActiveOtherStreams,
       "aluSIPSnoopingHardwareSIPPackets": aluSIPSnoopingHardwareSIPPackets,
       "aluSIPSnoopingSoftwareSIPPackets": aluSIPSnoopingSoftwareSIPPackets,
       "aluSIPSnoopingSIPInvitePackets": aluSIPSnoopingSIPInvitePackets,
       "aluSIPSnoopingSIPAckPackets": aluSIPSnoopingSIPAckPackets,
       "aluSIPSnoopingSIPByePackets": aluSIPSnoopingSIPByePackets,
       "aluSIPSnoopingSIPUpdatePackets": aluSIPSnoopingSIPUpdatePackets,
       "aluSIPSnoopingSIPPrackPackets": aluSIPSnoopingSIPPrackPackets,
       "aluSIPSnoopingSIPRecvdResponsePackets": aluSIPSnoopingSIPRecvdResponsePackets,
       "aluSIPSnoopingSIPDiscardedPackets": aluSIPSnoopingSIPDiscardedPackets,
       "aluSIPSnoopingSIPDiscardedNoTrustServerPackets": aluSIPSnoopingSIPDiscardedNoTrustServerPackets,
       "aluSIPSnoopingSIPDroppedSWErrorPackets": aluSIPSnoopingSIPDroppedSWErrorPackets,
       "aluSIPSnoopingTotalEmergencyCalls": aluSIPSnoopingTotalEmergencyCalls,
       "aluSIPSnoopingSIPTcpPort1": aluSIPSnoopingSIPTcpPort1,
       "aluSIPSnoopingSIPTcpPort2": aluSIPSnoopingSIPTcpPort2,
       "aluSIPSnoopingSIPTcpPort3": aluSIPSnoopingSIPTcpPort3,
       "aluSIPSnoopingSIPTcpPort4": aluSIPSnoopingSIPTcpPort4,
       "aluSIPSnoopingSIPTcpPort5": aluSIPSnoopingSIPTcpPort5,
       "aluSIPSnoopingSIPTcpPort6": aluSIPSnoopingSIPTcpPort6,
       "aluSIPSnoopingSIPTcpPort7": aluSIPSnoopingSIPTcpPort7,
       "aluSIPSnoopingSIPTcpPort8": aluSIPSnoopingSIPTcpPort8,
       "aluSIPSnoopingClearEndedCalls": aluSIPSnoopingClearEndedCalls,
       "alaSIPSnoopingRsvdHwResources": alaSIPSnoopingRsvdHwResources,
       "alaSIPSnoopingSIPCpuRateLimit": alaSIPSnoopingSIPCpuRateLimit,
       "aluSIPSnoopingPortConfigTable": aluSIPSnoopingPortConfigTable,
       "aluSIPSnoopingPortConfigEntry": aluSIPSnoopingPortConfigEntry,
       "aluSIPSnoopingPortConfigSlotPortIndex": aluSIPSnoopingPortConfigSlotPortIndex,
       "aluSIPSnoopingPortConfigPortStatus": aluSIPSnoopingPortConfigPortStatus,
       "aluSIPSnoopingPortConfigPortMode": aluSIPSnoopingPortConfigPortMode,
       "aluSIPSnoopingThresholdTable": aluSIPSnoopingThresholdTable,
       "aluSIPSnoopingThresholdEntry": aluSIPSnoopingThresholdEntry,
       "aluSIPSnoopingThresholdMediumIndex": aluSIPSnoopingThresholdMediumIndex,
       "aluSIPSnoopingThresholdJitter": aluSIPSnoopingThresholdJitter,
       "aluSIPSnoopingThresholdPacketLost": aluSIPSnoopingThresholdPacketLost,
       "aluSIPSnoopingThresholdRoundTripDelay": aluSIPSnoopingThresholdRoundTripDelay,
       "aluSIPSnoopingThresholdRFactor": aluSIPSnoopingThresholdRFactor,
       "aluSIPSnoopingThresholdMOS": aluSIPSnoopingThresholdMOS,
       "aluSIPSnoopingActiveCallSummaryTable": aluSIPSnoopingActiveCallSummaryTable,
       "aluSIPSnoopingActiveCallSummaryEntry": aluSIPSnoopingActiveCallSummaryEntry,
       "aluSIPSnoopingActiveCallIndex": aluSIPSnoopingActiveCallIndex,
       "aluSIPSnoopingActiveCallTagA": aluSIPSnoopingActiveCallTagA,
       "aluSIPSnoopingActiveCallTagB": aluSIPSnoopingActiveCallTagB,
       "aluSIPSnoopingActiveCallIpAddrAType": aluSIPSnoopingActiveCallIpAddrAType,
       "aluSIPSnoopingActiveCallIpAddrA": aluSIPSnoopingActiveCallIpAddrA,
       "aluSIPSnoopingActiveCallIpAddrBType": aluSIPSnoopingActiveCallIpAddrBType,
       "aluSIPSnoopingActiveCallIpAddrB": aluSIPSnoopingActiveCallIpAddrB,
       "aluSIPSnoopingActiveCallL4portA": aluSIPSnoopingActiveCallL4portA,
       "aluSIPSnoopingActiveCallL4portB": aluSIPSnoopingActiveCallL4portB,
       "aluSIPSnoopingActiveCallSipMediaType": aluSIPSnoopingActiveCallSipMediaType,
       "aluSIPSnoopingActiveCallStart": aluSIPSnoopingActiveCallStart,
       "aluSIPSnoopingActiveCallRtpCountA": aluSIPSnoopingActiveCallRtpCountA,
       "aluSIPSnoopingActiveCallRtcpCountA": aluSIPSnoopingActiveCallRtcpCountA,
       "aluSIPSnoopingActiveCallRuleNameA": aluSIPSnoopingActiveCallRuleNameA,
       "aluSIPSnoopingActiveCallRtpCountB": aluSIPSnoopingActiveCallRtpCountB,
       "aluSIPSnoopingActiveCallRtcpCountB": aluSIPSnoopingActiveCallRtcpCountB,
       "aluSIPSnoopingActiveCallRuleNameB": aluSIPSnoopingActiveCallRuleNameB,
       "aluSIPSnoopingActiveCallId": aluSIPSnoopingActiveCallId,
       "aluSIPSnoopingActiveCallTrustDSCPStatusA": aluSIPSnoopingActiveCallTrustDSCPStatusA,
       "aluSIPSnoopingActiveCallTrustDSCPStatusB": aluSIPSnoopingActiveCallTrustDSCPStatusB,
       "aluSIPSnoopingActiveCallPacketCountA": aluSIPSnoopingActiveCallPacketCountA,
       "aluSIPSnoopingActiveCallPacketCountB": aluSIPSnoopingActiveCallPacketCountB,
       "aluSIPSnoopingActiveCallStatsTable": aluSIPSnoopingActiveCallStatsTable,
       "aluSIPSnoopingActiveCallStatsEntry": aluSIPSnoopingActiveCallStatsEntry,
       "aluSIPSnoopingActiveCallStatsJitterViolationsA": aluSIPSnoopingActiveCallStatsJitterViolationsA,
       "aluSIPSnoopingActiveCallStatsJitterViolationsB": aluSIPSnoopingActiveCallStatsJitterViolationsB,
       "aluSIPSnoopingActiveCallStatsRtdViolationsA": aluSIPSnoopingActiveCallStatsRtdViolationsA,
       "aluSIPSnoopingActiveCallStatsRtdViolationsB": aluSIPSnoopingActiveCallStatsRtdViolationsB,
       "aluSIPSnoopingActiveCallStatsPktLossViolationsA": aluSIPSnoopingActiveCallStatsPktLossViolationsA,
       "aluSIPSnoopingActiveCallStatsPktLossViolationsB": aluSIPSnoopingActiveCallStatsPktLossViolationsB,
       "aluSIPSnoopingActiveCallStatsMosViolationsA": aluSIPSnoopingActiveCallStatsMosViolationsA,
       "aluSIPSnoopingActiveCallStatsMosViolationsB": aluSIPSnoopingActiveCallStatsMosViolationsB,
       "aluSIPSnoopingActiveCallStatsRfactorViolationsA": aluSIPSnoopingActiveCallStatsRfactorViolationsA,
       "aluSIPSnoopingActiveCallStatsRfactorViolationsB": aluSIPSnoopingActiveCallStatsRfactorViolationsB,
       "aluSIPSnoopingActiveCallStatsJitterMaxA": aluSIPSnoopingActiveCallStatsJitterMaxA,
       "aluSIPSnoopingActiveCallStatsJitterMinA": aluSIPSnoopingActiveCallStatsJitterMinA,
       "aluSIPSnoopingActiveCallStatsJitterAvgA": aluSIPSnoopingActiveCallStatsJitterAvgA,
       "aluSIPSnoopingActiveCallStatsJitterMaxB": aluSIPSnoopingActiveCallStatsJitterMaxB,
       "aluSIPSnoopingActiveCallStatsJitterMinB": aluSIPSnoopingActiveCallStatsJitterMinB,
       "aluSIPSnoopingActiveCallStatsJitterAvgB": aluSIPSnoopingActiveCallStatsJitterAvgB,
       "aluSIPSnoopingActiveCallStatsRtdMaxA": aluSIPSnoopingActiveCallStatsRtdMaxA,
       "aluSIPSnoopingActiveCallStatsRtdMinA": aluSIPSnoopingActiveCallStatsRtdMinA,
       "aluSIPSnoopingActiveCallStatsRtdAvgA": aluSIPSnoopingActiveCallStatsRtdAvgA,
       "aluSIPSnoopingActiveCallStatsRtdMaxB": aluSIPSnoopingActiveCallStatsRtdMaxB,
       "aluSIPSnoopingActiveCallStatsRtdMinB": aluSIPSnoopingActiveCallStatsRtdMinB,
       "aluSIPSnoopingActiveCallStatsRtdAvgB": aluSIPSnoopingActiveCallStatsRtdAvgB,
       "aluSIPSnoopingActiveCallStatsPktLossMaxA": aluSIPSnoopingActiveCallStatsPktLossMaxA,
       "aluSIPSnoopingActiveCallStatsPktLossMinA": aluSIPSnoopingActiveCallStatsPktLossMinA,
       "aluSIPSnoopingActiveCallStatsPktLossAvgA": aluSIPSnoopingActiveCallStatsPktLossAvgA,
       "aluSIPSnoopingActiveCallStatsPktLossMaxB": aluSIPSnoopingActiveCallStatsPktLossMaxB,
       "aluSIPSnoopingActiveCallStatsPktLossMinB": aluSIPSnoopingActiveCallStatsPktLossMinB,
       "aluSIPSnoopingActiveCallStatsPktLossAvgB": aluSIPSnoopingActiveCallStatsPktLossAvgB,
       "aluSIPSnoopingActiveCallStatsRfactorMaxA": aluSIPSnoopingActiveCallStatsRfactorMaxA,
       "aluSIPSnoopingActiveCallStatsRfactorMinA": aluSIPSnoopingActiveCallStatsRfactorMinA,
       "aluSIPSnoopingActiveCallStatsRfactorAvgA": aluSIPSnoopingActiveCallStatsRfactorAvgA,
       "aluSIPSnoopingActiveCallStatsRfactorMaxB": aluSIPSnoopingActiveCallStatsRfactorMaxB,
       "aluSIPSnoopingActiveCallStatsRfactorMinB": aluSIPSnoopingActiveCallStatsRfactorMinB,
       "aluSIPSnoopingActiveCallStatsRfactorAvgB": aluSIPSnoopingActiveCallStatsRfactorAvgB,
       "aluSIPSnoopingActiveCallStatsMosMaxA": aluSIPSnoopingActiveCallStatsMosMaxA,
       "aluSIPSnoopingActiveCallStatsMosMinA": aluSIPSnoopingActiveCallStatsMosMinA,
       "aluSIPSnoopingActiveCallStatsMosAvgA": aluSIPSnoopingActiveCallStatsMosAvgA,
       "aluSIPSnoopingActiveCallStatsMosMaxB": aluSIPSnoopingActiveCallStatsMosMaxB,
       "aluSIPSnoopingActiveCallStatsMosMinB": aluSIPSnoopingActiveCallStatsMosMinB,
       "aluSIPSnoopingActiveCallStatsMosAvgB": aluSIPSnoopingActiveCallStatsMosAvgB,
       "aluSIPSnoopingEndedCallSummaryTable": aluSIPSnoopingEndedCallSummaryTable,
       "aluSIPSnoopingEndedCallSummaryEntry": aluSIPSnoopingEndedCallSummaryEntry,
       "aluSIPSnoopingEndedCallIndex": aluSIPSnoopingEndedCallIndex,
       "aluSIPSnoopingEndedCallId": aluSIPSnoopingEndedCallId,
       "aluSIPSnoopingEndedCallTagA": aluSIPSnoopingEndedCallTagA,
       "aluSIPSnoopingEndedCallTagB": aluSIPSnoopingEndedCallTagB,
       "aluSIPSnoopingEndedCallIpAddrAType": aluSIPSnoopingEndedCallIpAddrAType,
       "aluSIPSnoopingEndedCallIpAddrA": aluSIPSnoopingEndedCallIpAddrA,
       "aluSIPSnoopingEndedCallIpAddrBType": aluSIPSnoopingEndedCallIpAddrBType,
       "aluSIPSnoopingEndedCallIpAddrB": aluSIPSnoopingEndedCallIpAddrB,
       "aluSIPSnoopingEndedCallL4portA": aluSIPSnoopingEndedCallL4portA,
       "aluSIPSnoopingEndedCallL4portB": aluSIPSnoopingEndedCallL4portB,
       "aluSIPSnoopingEndedCallSipMediaType": aluSIPSnoopingEndedCallSipMediaType,
       "aluSIPSnoopingEndedCallStart": aluSIPSnoopingEndedCallStart,
       "aluSIPSnoopingEndedCallEnd": aluSIPSnoopingEndedCallEnd,
       "aluSIPSnoopingEndedCallRtpCountA": aluSIPSnoopingEndedCallRtpCountA,
       "aluSIPSnoopingEndedCallRtcpCountA": aluSIPSnoopingEndedCallRtcpCountA,
       "aluSIPSnoopingEndedCallRuleNameA": aluSIPSnoopingEndedCallRuleNameA,
       "aluSIPSnoopingEndedCallRtpCountB": aluSIPSnoopingEndedCallRtpCountB,
       "aluSIPSnoopingEndedCallRtcpCountB": aluSIPSnoopingEndedCallRtcpCountB,
       "aluSIPSnoopingEndedCallRuleNameB": aluSIPSnoopingEndedCallRuleNameB,
       "aluSIPSnoopingEndedCallEndReason": aluSIPSnoopingEndedCallEndReason,
       "aluSIPSnoopingEndedCallTrustDSCPStatusA": aluSIPSnoopingEndedCallTrustDSCPStatusA,
       "aluSIPSnoopingEndedCallTrustDSCPStatusB": aluSIPSnoopingEndedCallTrustDSCPStatusB,
       "aluSIPSnoopingEndedCallPacketCountA": aluSIPSnoopingEndedCallPacketCountA,
       "aluSIPSnoopingEndedCallPacketCountB": aluSIPSnoopingEndedCallPacketCountB,
       "aluSIPSnoopingEndedCallStatsTable": aluSIPSnoopingEndedCallStatsTable,
       "aluSIPSnoopingEndedCallStatsEntry": aluSIPSnoopingEndedCallStatsEntry,
       "aluSIPSnoopingEndedCallStatsJitterViolationsA": aluSIPSnoopingEndedCallStatsJitterViolationsA,
       "aluSIPSnoopingEndedCallStatsJitterViolationsB": aluSIPSnoopingEndedCallStatsJitterViolationsB,
       "aluSIPSnoopingEndedCallStatsRtdViolationsA": aluSIPSnoopingEndedCallStatsRtdViolationsA,
       "aluSIPSnoopingEndedCallStatsRtdViolationsB": aluSIPSnoopingEndedCallStatsRtdViolationsB,
       "aluSIPSnoopingEndedCallStatsPktLossViolationsA": aluSIPSnoopingEndedCallStatsPktLossViolationsA,
       "aluSIPSnoopingEndedCallStatsPktLossViolationsB": aluSIPSnoopingEndedCallStatsPktLossViolationsB,
       "aluSIPSnoopingEndedCallStatsMosViolationsA": aluSIPSnoopingEndedCallStatsMosViolationsA,
       "aluSIPSnoopingEndedCallStatsMosViolationsB": aluSIPSnoopingEndedCallStatsMosViolationsB,
       "aluSIPSnoopingEndedCallStatsRfactorViolationsA": aluSIPSnoopingEndedCallStatsRfactorViolationsA,
       "aluSIPSnoopingEndedCallStatsRfactorViolationsB": aluSIPSnoopingEndedCallStatsRfactorViolationsB,
       "aluSIPSnoopingEndedCallStatsJitterMaxA": aluSIPSnoopingEndedCallStatsJitterMaxA,
       "aluSIPSnoopingEndedCallStatsJitterMinA": aluSIPSnoopingEndedCallStatsJitterMinA,
       "aluSIPSnoopingEndedCallStatsJitterAvgA": aluSIPSnoopingEndedCallStatsJitterAvgA,
       "aluSIPSnoopingEndedCallStatsJitterMaxB": aluSIPSnoopingEndedCallStatsJitterMaxB,
       "aluSIPSnoopingEndedCallStatsJitterMinB": aluSIPSnoopingEndedCallStatsJitterMinB,
       "aluSIPSnoopingEndedCallStatsJitterAvgB": aluSIPSnoopingEndedCallStatsJitterAvgB,
       "aluSIPSnoopingEndedCallStatsRtdMaxA": aluSIPSnoopingEndedCallStatsRtdMaxA,
       "aluSIPSnoopingEndedCallStatsRtdMinA": aluSIPSnoopingEndedCallStatsRtdMinA,
       "aluSIPSnoopingEndedCallStatsRtdAvgA": aluSIPSnoopingEndedCallStatsRtdAvgA,
       "aluSIPSnoopingEndedCallStatsRtdMaxB": aluSIPSnoopingEndedCallStatsRtdMaxB,
       "aluSIPSnoopingEndedCallStatsRtdMinB": aluSIPSnoopingEndedCallStatsRtdMinB,
       "aluSIPSnoopingEndedCallStatsRtdAvgB": aluSIPSnoopingEndedCallStatsRtdAvgB,
       "aluSIPSnoopingEndedCallStatsPktLossMaxA": aluSIPSnoopingEndedCallStatsPktLossMaxA,
       "aluSIPSnoopingEndedCallStatsPktLossMinA": aluSIPSnoopingEndedCallStatsPktLossMinA,
       "aluSIPSnoopingEndedCallStatsPktLossAvgA": aluSIPSnoopingEndedCallStatsPktLossAvgA,
       "aluSIPSnoopingEndedCallStatsPktLossMaxB": aluSIPSnoopingEndedCallStatsPktLossMaxB,
       "aluSIPSnoopingEndedCallStatsPktLossMinB": aluSIPSnoopingEndedCallStatsPktLossMinB,
       "aluSIPSnoopingEndedCallStatsPktLossAvgB": aluSIPSnoopingEndedCallStatsPktLossAvgB,
       "aluSIPSnoopingEndedCallStatsRfactorMaxA": aluSIPSnoopingEndedCallStatsRfactorMaxA,
       "aluSIPSnoopingEndedCallStatsRfactorMinA": aluSIPSnoopingEndedCallStatsRfactorMinA,
       "aluSIPSnoopingEndedCallStatsRfactorAvgA": aluSIPSnoopingEndedCallStatsRfactorAvgA,
       "aluSIPSnoopingEndedCallStatsRfactorMaxB": aluSIPSnoopingEndedCallStatsRfactorMaxB,
       "aluSIPSnoopingEndedCallStatsRfactorMinB": aluSIPSnoopingEndedCallStatsRfactorMinB,
       "aluSIPSnoopingEndedCallStatsRfactorAvgB": aluSIPSnoopingEndedCallStatsRfactorAvgB,
       "aluSIPSnoopingEndedCallStatsMosMaxA": aluSIPSnoopingEndedCallStatsMosMaxA,
       "aluSIPSnoopingEndedCallStatsMosMinA": aluSIPSnoopingEndedCallStatsMosMinA,
       "aluSIPSnoopingEndedCallStatsMosAvgA": aluSIPSnoopingEndedCallStatsMosAvgA,
       "aluSIPSnoopingEndedCallStatsMosMaxB": aluSIPSnoopingEndedCallStatsMosMaxB,
       "aluSIPSnoopingEndedCallStatsMosMinB": aluSIPSnoopingEndedCallStatsMosMinB,
       "aluSIPSnoopingEndedCallStatsMosAvgB": aluSIPSnoopingEndedCallStatsMosAvgB,
       "aluSIPSnoopingNotificationObjects": aluSIPSnoopingNotificationObjects,
       "alaSIPSnoopingCallViolationType": alaSIPSnoopingCallViolationType,
       "alaSIPSnoopingRegisteredClientsTable": alaSIPSnoopingRegisteredClientsTable,
       "alaSIPSnoopingRegisteredClientsEntry": alaSIPSnoopingRegisteredClientsEntry,
       "alaSIPSnoopingRegisteredClientNumber": alaSIPSnoopingRegisteredClientNumber,
       "alaSIPSnoopingRegisteredClientAddrType": alaSIPSnoopingRegisteredClientAddrType,
       "alaSIPSnoopingRegisteredClientAddr": alaSIPSnoopingRegisteredClientAddr,
       "aluSIPSnoopingMIBConformance": aluSIPSnoopingMIBConformance,
       "aluSIPSnoopingMIBGroups": aluSIPSnoopingMIBGroups,
       "aluSIPSnoopingPortConfigGroup": aluSIPSnoopingPortConfigGroup,
       "aluSIPSnoopingThresholdGroup": aluSIPSnoopingThresholdGroup,
       "aluSIPSnoopingConfigGroup": aluSIPSnoopingConfigGroup,
       "aluSIPSnoopingSummaryGroup": aluSIPSnoopingSummaryGroup,
       "aluSIPSnoopingStatsGroup": aluSIPSnoopingStatsGroup,
       "alaSIPSnoopingNotificationGroup": alaSIPSnoopingNotificationGroup,
       "alaSIPSnoopingRegisteredClientsGroup": alaSIPSnoopingRegisteredClientsGroup,
       "aluSIPSnoopingMIBCompliances": aluSIPSnoopingMIBCompliances,
       "aluSIPSnoopingMIBCompliance": aluSIPSnoopingMIBCompliance}
)
