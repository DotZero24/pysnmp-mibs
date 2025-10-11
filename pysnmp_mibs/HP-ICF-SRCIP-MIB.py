# SNMP MIB module (HP-ICF-SRCIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/HP-ICF-SRCIP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:36:04 2025
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

(hpicfCommon,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpicfCommon")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

hpicfSrcIpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 13)
)
if mibBuilder.loadTexts:
    hpicfSrcIpMIB.setRevisions(
        ("2020-06-20 00:00",
         "2016-08-29 00:00",
         "2011-07-21 00:00",
         "2009-04-30 00:00",
         "2008-10-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfSrcIpConfig_ObjectIdentity = ObjectIdentity
hpicfSrcIpConfig = _HpicfSrcIpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 13, 1)
)
_HpicfSrcIpAddrPolicyTable_Object = MibTable
hpicfSrcIpAddrPolicyTable = _HpicfSrcIpAddrPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 13, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfSrcIpAddrPolicyTable.setStatus("current")
_HpicfSrcIpAddrPolicyEntry_Object = MibTableRow
hpicfSrcIpAddrPolicyEntry = _HpicfSrcIpAddrPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 13, 1, 1, 1)
)
hpicfSrcIpAddrPolicyEntry.setIndexNames(
    (0, "HP-ICF-SRCIP-MIB", "hpicfSrcIpAddressType"),
    (0, "HP-ICF-SRCIP-MIB", "hpicfSrcIpProtocolIndex"),
)
if mibBuilder.loadTexts:
    hpicfSrcIpAddrPolicyEntry.setStatus("current")
_HpicfSrcIpAddressType_Type = InetAddressType
_HpicfSrcIpAddressType_Object = MibTableColumn
hpicfSrcIpAddressType = _HpicfSrcIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 13, 1, 1, 1, 1),
    _HpicfSrcIpAddressType_Type()
)
hpicfSrcIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfSrcIpAddressType.setStatus("current")


class _HpicfSrcIpProtocolIndex_Type(Integer32):
    """Custom type hpicfSrcIpProtocolIndex based on Integer32"""
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
        *(("tacacs", 1),
          ("radius", 2),
          ("syslog", 3),
          ("telnet", 4),
          ("tftp", 5),
          ("sntp", 6),
          ("sflow", 7),
          ("tunnelednodeserver", 8),
          ("radsec", 9),
          ("central", 10))
    )


_HpicfSrcIpProtocolIndex_Type.__name__ = "Integer32"
_HpicfSrcIpProtocolIndex_Object = MibTableColumn
hpicfSrcIpProtocolIndex = _HpicfSrcIpProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 13, 1, 1, 1, 2),
    _HpicfSrcIpProtocolIndex_Type()
)
hpicfSrcIpProtocolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfSrcIpProtocolIndex.setStatus("current")


class _HpicfSrcIpAddrPolicy_Type(Integer32):
    """Custom type hpicfSrcIpAddrPolicy based on Integer32"""
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
        *(("outgoingInterface", 1),
          ("configuredIpAddr", 2),
          ("configuredInterface", 3))
    )


_HpicfSrcIpAddrPolicy_Type.__name__ = "Integer32"
_HpicfSrcIpAddrPolicy_Object = MibTableColumn
hpicfSrcIpAddrPolicy = _HpicfSrcIpAddrPolicy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 13, 1, 1, 1, 3),
    _HpicfSrcIpAddrPolicy_Type()
)
hpicfSrcIpAddrPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfSrcIpAddrPolicy.setStatus("current")
_HpicfSrcIpAddrIfIndex_Type = InterfaceIndexOrZero
_HpicfSrcIpAddrIfIndex_Object = MibTableColumn
hpicfSrcIpAddrIfIndex = _HpicfSrcIpAddrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 13, 1, 1, 1, 4),
    _HpicfSrcIpAddrIfIndex_Type()
)
hpicfSrcIpAddrIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfSrcIpAddrIfIndex.setStatus("current")
_HpicfSrcIpAddress_Type = InetAddress
_HpicfSrcIpAddress_Object = MibTableColumn
hpicfSrcIpAddress = _HpicfSrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 13, 1, 1, 1, 5),
    _HpicfSrcIpAddress_Type()
)
hpicfSrcIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfSrcIpAddress.setStatus("current")
_HpicfSrcIpConformance_ObjectIdentity = ObjectIdentity
hpicfSrcIpConformance = _HpicfSrcIpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 13, 2)
)
_HpicfSrcIpGroups_ObjectIdentity = ObjectIdentity
hpicfSrcIpGroups = _HpicfSrcIpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 13, 2, 1)
)
_HpicfSrcIpCompliances_ObjectIdentity = ObjectIdentity
hpicfSrcIpCompliances = _HpicfSrcIpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 13, 2, 2)
)

# Managed Objects groups

hpicfSrcIpBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 13, 2, 1, 1)
)
hpicfSrcIpBaseGroup.setObjects(
      *(("HP-ICF-SRCIP-MIB", "hpicfSrcIpAddrPolicy"),
        ("HP-ICF-SRCIP-MIB", "hpicfSrcIpAddrIfIndex"),
        ("HP-ICF-SRCIP-MIB", "hpicfSrcIpAddress"))
)
if mibBuilder.loadTexts:
    hpicfSrcIpBaseGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfSrcIpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 13, 2, 2, 1)
)
hpicfSrcIpCompliance.setObjects(
    ("HP-ICF-SRCIP-MIB", "hpicfSrcIpBaseGroup")
)
if mibBuilder.loadTexts:
    hpicfSrcIpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-SRCIP-MIB",
    **{"hpicfSrcIpMIB": hpicfSrcIpMIB,
       "hpicfSrcIpConfig": hpicfSrcIpConfig,
       "hpicfSrcIpAddrPolicyTable": hpicfSrcIpAddrPolicyTable,
       "hpicfSrcIpAddrPolicyEntry": hpicfSrcIpAddrPolicyEntry,
       "hpicfSrcIpAddressType": hpicfSrcIpAddressType,
       "hpicfSrcIpProtocolIndex": hpicfSrcIpProtocolIndex,
       "hpicfSrcIpAddrPolicy": hpicfSrcIpAddrPolicy,
       "hpicfSrcIpAddrIfIndex": hpicfSrcIpAddrIfIndex,
       "hpicfSrcIpAddress": hpicfSrcIpAddress,
       "hpicfSrcIpConformance": hpicfSrcIpConformance,
       "hpicfSrcIpGroups": hpicfSrcIpGroups,
       "hpicfSrcIpBaseGroup": hpicfSrcIpBaseGroup,
       "hpicfSrcIpCompliances": hpicfSrcIpCompliances,
       "hpicfSrcIpCompliance": hpicfSrcIpCompliance}
)
