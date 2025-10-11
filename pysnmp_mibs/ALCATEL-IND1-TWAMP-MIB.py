# SNMP MIB module (ALCATEL-IND1-TWAMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/alcatel/ALCATEL-IND1-TWAMP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:07:50 2025
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

(softentIND1TWAMP,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1TWAMP")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

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
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1TWAMPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 71, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1TWAMPMIB.setRevisions(
        ("2014-10-07 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1TWAMPMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1TWAMPMIBObjects = _AlcatelIND1TWAMPMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 71, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1TWAMPMIBObjects.setStatus("current")
_TwampServerMIB_ObjectIdentity = ObjectIdentity
twampServerMIB = _TwampServerMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 71, 1, 1, 1)
)
_TwampServerTable_Object = MibTable
twampServerTable = _TwampServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 71, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    twampServerTable.setStatus("current")
_TwampServerTableEntry_Object = MibTableRow
twampServerTableEntry = _TwampServerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 71, 1, 1, 1, 1, 1)
)
twampServerTableEntry.setIndexNames(
    (0, "ALCATEL-IND1-TWAMP-MIB", "twampClientIpaddress"),
    (0, "ALCATEL-IND1-TWAMP-MIB", "twampClientIpaddressMask"),
)
if mibBuilder.loadTexts:
    twampServerTableEntry.setStatus("current")


class _TwampPortNumber_Type(Integer32):
    """Custom type twampPortNumber based on Integer32"""
    defaultValue = 862

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_TwampPortNumber_Type.__name__ = "Integer32"
_TwampPortNumber_Object = MibTableColumn
twampPortNumber = _TwampPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 71, 1, 1, 1, 1, 1, 1),
    _TwampPortNumber_Type()
)
twampPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampPortNumber.setStatus("current")


class _TwampInactivityTimeout_Type(Integer32):
    """Custom type twampInactivityTimeout based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_TwampInactivityTimeout_Type.__name__ = "Integer32"
_TwampInactivityTimeout_Object = MibTableColumn
twampInactivityTimeout = _TwampInactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 71, 1, 1, 1, 1, 1, 2),
    _TwampInactivityTimeout_Type()
)
twampInactivityTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampInactivityTimeout.setStatus("current")
_TwampClientIpaddress_Type = IpAddress
_TwampClientIpaddress_Object = MibTableColumn
twampClientIpaddress = _TwampClientIpaddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 71, 1, 1, 1, 1, 1, 3),
    _TwampClientIpaddress_Type()
)
twampClientIpaddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampClientIpaddress.setStatus("current")
_TwampClientIpaddressMask_Type = IpAddress
_TwampClientIpaddressMask_Object = MibTableColumn
twampClientIpaddressMask = _TwampClientIpaddressMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 71, 1, 1, 1, 1, 1, 4),
    _TwampClientIpaddressMask_Type()
)
twampClientIpaddressMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampClientIpaddressMask.setStatus("current")
_TwampRowStatus_Type = RowStatus
_TwampRowStatus_Object = MibTableColumn
twampRowStatus = _TwampRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 71, 1, 1, 1, 1, 1, 5),
    _TwampRowStatus_Type()
)
twampRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    twampRowStatus.setStatus("current")
_TwampServerConnectionTable_Object = MibTable
twampServerConnectionTable = _TwampServerConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 71, 1, 1, 2)
)
if mibBuilder.loadTexts:
    twampServerConnectionTable.setStatus("current")
_TwampServerConnectionTableEntry_Object = MibTableRow
twampServerConnectionTableEntry = _TwampServerConnectionTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 71, 1, 1, 2, 1)
)
twampServerConnectionTableEntry.setIndexNames(
    (0, "ALCATEL-IND1-TWAMP-MIB", "twampServerConnClientIP"),
)
if mibBuilder.loadTexts:
    twampServerConnectionTableEntry.setStatus("current")
_TwampServerConnClientIP_Type = IpAddress
_TwampServerConnClientIP_Object = MibTableColumn
twampServerConnClientIP = _TwampServerConnClientIP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 71, 1, 1, 2, 1, 1),
    _TwampServerConnClientIP_Type()
)
twampServerConnClientIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampServerConnClientIP.setStatus("current")
_TwampServerConnSessionId_Type = SnmpAdminString
_TwampServerConnSessionId_Object = MibTableColumn
twampServerConnSessionId = _TwampServerConnSessionId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 71, 1, 1, 2, 1, 2),
    _TwampServerConnSessionId_Type()
)
twampServerConnSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampServerConnSessionId.setStatus("current")
_TwampServerConnTimeOfLastRun_Type = DisplayString
_TwampServerConnTimeOfLastRun_Object = MibTableColumn
twampServerConnTimeOfLastRun = _TwampServerConnTimeOfLastRun_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 71, 1, 1, 2, 1, 3),
    _TwampServerConnTimeOfLastRun_Type()
)
twampServerConnTimeOfLastRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampServerConnTimeOfLastRun.setStatus("current")
_TwampServerConnPktsSent_Type = Integer32
_TwampServerConnPktsSent_Object = MibTableColumn
twampServerConnPktsSent = _TwampServerConnPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 71, 1, 1, 2, 1, 4),
    _TwampServerConnPktsSent_Type()
)
twampServerConnPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampServerConnPktsSent.setStatus("current")
_TwampServerConnPktsRecvd_Type = Integer32
_TwampServerConnPktsRecvd_Object = MibTableColumn
twampServerConnPktsRecvd = _TwampServerConnPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 71, 1, 1, 2, 1, 5),
    _TwampServerConnPktsRecvd_Type()
)
twampServerConnPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampServerConnPktsRecvd.setStatus("current")
_TwampServerConnectionStatus_Type = DisplayString
_TwampServerConnectionStatus_Object = MibTableColumn
twampServerConnectionStatus = _TwampServerConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 71, 1, 1, 2, 1, 6),
    _TwampServerConnectionStatus_Type()
)
twampServerConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampServerConnectionStatus.setStatus("current")
_AlcatelIND1TWAMPMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1TWAMPMIBConformance = _AlcatelIND1TWAMPMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 71, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1TWAMPMIBConformance.setStatus("current")
_AlcatelIND1TWAMPMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1TWAMPMIBGroups = _AlcatelIND1TWAMPMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 71, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1TWAMPMIBGroups.setStatus("current")
_AlcatelIND1TWAMPMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1TWAMPMIBCompliances = _AlcatelIND1TWAMPMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 71, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1TWAMPMIBCompliances.setStatus("current")

# Managed Objects groups

twampServerMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 71, 1, 2, 1, 1)
)
twampServerMIBGroup.setObjects(
      *(("ALCATEL-IND1-TWAMP-MIB", "twampPortNumber"),
        ("ALCATEL-IND1-TWAMP-MIB", "twampInactivityTimeout"),
        ("ALCATEL-IND1-TWAMP-MIB", "twampClientIpaddress"),
        ("ALCATEL-IND1-TWAMP-MIB", "twampClientIpaddressMask"),
        ("ALCATEL-IND1-TWAMP-MIB", "twampRowStatus"))
)
if mibBuilder.loadTexts:
    twampServerMIBGroup.setStatus("current")

twampServerConnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 71, 1, 2, 1, 2)
)
twampServerConnGroup.setObjects(
      *(("ALCATEL-IND1-TWAMP-MIB", "twampServerConnClientIP"),
        ("ALCATEL-IND1-TWAMP-MIB", "twampServerConnSessionId"),
        ("ALCATEL-IND1-TWAMP-MIB", "twampServerConnTimeOfLastRun"),
        ("ALCATEL-IND1-TWAMP-MIB", "twampServerConnPktsSent"),
        ("ALCATEL-IND1-TWAMP-MIB", "twampServerConnPktsRecvd"),
        ("ALCATEL-IND1-TWAMP-MIB", "twampServerConnectionStatus"))
)
if mibBuilder.loadTexts:
    twampServerConnGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alcatelIND1TWAMPMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 71, 1, 2, 2, 1)
)
alcatelIND1TWAMPMIBCompliance.setObjects(
      *(("ALCATEL-IND1-TWAMP-MIB", "twampServerMIBGroup"),
        ("ALCATEL-IND1-TWAMP-MIB", "twampServerConnGroup"))
)
if mibBuilder.loadTexts:
    alcatelIND1TWAMPMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-TWAMP-MIB",
    **{"alcatelIND1TWAMPMIB": alcatelIND1TWAMPMIB,
       "alcatelIND1TWAMPMIBObjects": alcatelIND1TWAMPMIBObjects,
       "twampServerMIB": twampServerMIB,
       "twampServerTable": twampServerTable,
       "twampServerTableEntry": twampServerTableEntry,
       "twampPortNumber": twampPortNumber,
       "twampInactivityTimeout": twampInactivityTimeout,
       "twampClientIpaddress": twampClientIpaddress,
       "twampClientIpaddressMask": twampClientIpaddressMask,
       "twampRowStatus": twampRowStatus,
       "twampServerConnectionTable": twampServerConnectionTable,
       "twampServerConnectionTableEntry": twampServerConnectionTableEntry,
       "twampServerConnClientIP": twampServerConnClientIP,
       "twampServerConnSessionId": twampServerConnSessionId,
       "twampServerConnTimeOfLastRun": twampServerConnTimeOfLastRun,
       "twampServerConnPktsSent": twampServerConnPktsSent,
       "twampServerConnPktsRecvd": twampServerConnPktsRecvd,
       "twampServerConnectionStatus": twampServerConnectionStatus,
       "alcatelIND1TWAMPMIBConformance": alcatelIND1TWAMPMIBConformance,
       "alcatelIND1TWAMPMIBGroups": alcatelIND1TWAMPMIBGroups,
       "twampServerMIBGroup": twampServerMIBGroup,
       "twampServerConnGroup": twampServerConnGroup,
       "alcatelIND1TWAMPMIBCompliances": alcatelIND1TWAMPMIBCompliances,
       "alcatelIND1TWAMPMIBCompliance": alcatelIND1TWAMPMIBCompliance}
)
