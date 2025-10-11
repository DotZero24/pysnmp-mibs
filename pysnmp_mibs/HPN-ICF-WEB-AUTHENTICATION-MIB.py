# SNMP MIB module (HPN-ICF-WEB-AUTHENTICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/HPN-ICF-WEB-AUTHENTICATION-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:40:21 2025
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

(ifDescr,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

hpnicfWebAuthentication = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 93)
)
if mibBuilder.loadTexts:
    hpnicfWebAuthentication.setRevisions(
        ("2008-06-25 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfWaTrapObjects_ObjectIdentity = ObjectIdentity
hpnicfWaTrapObjects = _HpnicfWaTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 93, 1)
)
_HpnicfWaVlanID_Type = Integer32
_HpnicfWaVlanID_Object = MibScalar
hpnicfWaVlanID = _HpnicfWaVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 93, 1, 1),
    _HpnicfWaVlanID_Type()
)
hpnicfWaVlanID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfWaVlanID.setStatus("current")


class _HpnicfWaReasonCode_Type(Integer32):
    """Custom type hpnicfWaReasonCode based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("globalNumberMax", 1),
          ("configNumberMax", 2),
          ("portNumberMax", 3),
          ("invalidUsername", 4),
          ("authFail", 5),
          ("setACLFail", 6),
          ("changeVlanFail", 7),
          ("other", 8),
          ("onlineOverTime", 9),
          ("noTransferData", 10),
          ("cutOperation", 11),
          ("portDisabled", 12),
          ("portDown", 13),
          ("userLogout", 14),
          ("vlanChanged", 15),
          ("vlanDelted", 16))
    )


_HpnicfWaReasonCode_Type.__name__ = "Integer32"
_HpnicfWaReasonCode_Object = MibScalar
hpnicfWaReasonCode = _HpnicfWaReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 93, 1, 2),
    _HpnicfWaReasonCode_Type()
)
hpnicfWaReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfWaReasonCode.setStatus("current")


class _HpnicfWaActionCode_Type(Integer32):
    """Custom type hpnicfWaActionCode based on Integer32"""
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


_HpnicfWaActionCode_Type.__name__ = "Integer32"
_HpnicfWaActionCode_Object = MibScalar
hpnicfWaActionCode = _HpnicfWaActionCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 93, 1, 3),
    _HpnicfWaActionCode_Type()
)
hpnicfWaActionCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfWaActionCode.setStatus("current")
_HpnicfWaClientMacAddr_Type = MacAddress
_HpnicfWaClientMacAddr_Object = MibScalar
hpnicfWaClientMacAddr = _HpnicfWaClientMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 93, 1, 4),
    _HpnicfWaClientMacAddr_Type()
)
hpnicfWaClientMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfWaClientMacAddr.setStatus("current")
_HpnicfWaTrap_ObjectIdentity = ObjectIdentity
hpnicfWaTrap = _HpnicfWaTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 93, 2)
)
_HpnicfWaTrapPrefix_ObjectIdentity = ObjectIdentity
hpnicfWaTrapPrefix = _HpnicfWaTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 93, 2, 0)
)

# Managed Objects groups


# Notification objects

hpnicfWaClientLogon = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 93, 2, 0, 1)
)
hpnicfWaClientLogon.setObjects(
      *(("HPN-ICF-WEB-AUTHENTICATION-MIB", "hpnicfWaClientMacAddr"),
        ("IF-MIB", "ifDescr"),
        ("HPN-ICF-WEB-AUTHENTICATION-MIB", "hpnicfWaVlanID"))
)
if mibBuilder.loadTexts:
    hpnicfWaClientLogon.setStatus(
        "current"
    )

hpnicfWaClientLogonFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 93, 2, 0, 2)
)
hpnicfWaClientLogonFail.setObjects(
      *(("HPN-ICF-WEB-AUTHENTICATION-MIB", "hpnicfWaClientMacAddr"),
        ("IF-MIB", "ifDescr"),
        ("HPN-ICF-WEB-AUTHENTICATION-MIB", "hpnicfWaVlanID"),
        ("HPN-ICF-WEB-AUTHENTICATION-MIB", "hpnicfWaReasonCode"))
)
if mibBuilder.loadTexts:
    hpnicfWaClientLogonFail.setStatus(
        "current"
    )

hpnicfWaClientLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 93, 2, 0, 3)
)
hpnicfWaClientLogout.setObjects(
      *(("HPN-ICF-WEB-AUTHENTICATION-MIB", "hpnicfWaClientMacAddr"),
        ("IF-MIB", "ifDescr"),
        ("HPN-ICF-WEB-AUTHENTICATION-MIB", "hpnicfWaVlanID"),
        ("HPN-ICF-WEB-AUTHENTICATION-MIB", "hpnicfWaReasonCode"))
)
if mibBuilder.loadTexts:
    hpnicfWaClientLogout.setStatus(
        "current"
    )

hpnicfWaSysAction = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 93, 2, 0, 4)
)
hpnicfWaSysAction.setObjects(
    ("HPN-ICF-WEB-AUTHENTICATION-MIB", "hpnicfWaActionCode")
)
if mibBuilder.loadTexts:
    hpnicfWaSysAction.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-WEB-AUTHENTICATION-MIB",
    **{"hpnicfWebAuthentication": hpnicfWebAuthentication,
       "hpnicfWaTrapObjects": hpnicfWaTrapObjects,
       "hpnicfWaVlanID": hpnicfWaVlanID,
       "hpnicfWaReasonCode": hpnicfWaReasonCode,
       "hpnicfWaActionCode": hpnicfWaActionCode,
       "hpnicfWaClientMacAddr": hpnicfWaClientMacAddr,
       "hpnicfWaTrap": hpnicfWaTrap,
       "hpnicfWaTrapPrefix": hpnicfWaTrapPrefix,
       "hpnicfWaClientLogon": hpnicfWaClientLogon,
       "hpnicfWaClientLogonFail": hpnicfWaClientLogonFail,
       "hpnicfWaClientLogout": hpnicfWaClientLogout,
       "hpnicfWaSysAction": hpnicfWaSysAction}
)
