# SNMP MIB module (ADTRAN-GEN-DHCP-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GEN-DHCP-CLIENT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:33:11 2025
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

(adGenDhcpClient,
 adGenDhcpClientId) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-DHCP-MIB",
    "adGenDhcpClient",
    "adGenDhcpClientId")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

adGenDhcpClientMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 80, 1, 1)
)
if mibBuilder.loadTexts:
    adGenDhcpClientMib.setRevisions(
        ("2009-08-13 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AdGenDhcpClientState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("init", 1),
          ("selecting", 2),
          ("requesting", 3),
          ("bound", 4),
          ("renewing", 5),
          ("rebinding", 6))
    )



# MIB Managed Objects in the order of their OIDs

_AdGenDhcpClientMIBObjects_ObjectIdentity = ObjectIdentity
adGenDhcpClientMIBObjects = _AdGenDhcpClientMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 80, 1, 1)
)
_AdGenDhcpClientStatus_ObjectIdentity = ObjectIdentity
adGenDhcpClientStatus = _AdGenDhcpClientStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 80, 1, 1, 1)
)
_AdGenDhcpClientStatusTable_Object = MibTable
adGenDhcpClientStatusTable = _AdGenDhcpClientStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 80, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    adGenDhcpClientStatusTable.setStatus("current")
_AdGenDhcpClientStatusEntry_Object = MibTableRow
adGenDhcpClientStatusEntry = _AdGenDhcpClientStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 80, 1, 1, 1, 1, 1)
)
adGenDhcpClientStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenDhcpClientStatusEntry.setStatus("current")
_AdGenDhcpClientStatusState_Type = AdGenDhcpClientState
_AdGenDhcpClientStatusState_Object = MibTableColumn
adGenDhcpClientStatusState = _AdGenDhcpClientStatusState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 80, 1, 1, 1, 1, 1, 1),
    _AdGenDhcpClientStatusState_Type()
)
adGenDhcpClientStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDhcpClientStatusState.setStatus("current")


class _AdGenDhcpClientStatusClientIdentifier_Type(OctetString):
    """Custom type adGenDhcpClientStatusClientIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 80),
    )


_AdGenDhcpClientStatusClientIdentifier_Type.__name__ = "OctetString"
_AdGenDhcpClientStatusClientIdentifier_Object = MibTableColumn
adGenDhcpClientStatusClientIdentifier = _AdGenDhcpClientStatusClientIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 80, 1, 1, 1, 1, 1, 2),
    _AdGenDhcpClientStatusClientIdentifier_Type()
)
adGenDhcpClientStatusClientIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDhcpClientStatusClientIdentifier.setStatus("current")


class _AdGenDhcpClientStatusHostName_Type(OctetString):
    """Custom type adGenDhcpClientStatusHostName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 35),
    )


_AdGenDhcpClientStatusHostName_Type.__name__ = "OctetString"
_AdGenDhcpClientStatusHostName_Object = MibTableColumn
adGenDhcpClientStatusHostName = _AdGenDhcpClientStatusHostName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 80, 1, 1, 1, 1, 1, 3),
    _AdGenDhcpClientStatusHostName_Type()
)
adGenDhcpClientStatusHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDhcpClientStatusHostName.setStatus("current")
_AdGenDhcpClientStatusIpAddressType_Type = InetAddressType
_AdGenDhcpClientStatusIpAddressType_Object = MibTableColumn
adGenDhcpClientStatusIpAddressType = _AdGenDhcpClientStatusIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 80, 1, 1, 1, 1, 1, 4),
    _AdGenDhcpClientStatusIpAddressType_Type()
)
adGenDhcpClientStatusIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDhcpClientStatusIpAddressType.setStatus("current")
_AdGenDhcpClientStatusIpAddress_Type = InetAddress
_AdGenDhcpClientStatusIpAddress_Object = MibTableColumn
adGenDhcpClientStatusIpAddress = _AdGenDhcpClientStatusIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 80, 1, 1, 1, 1, 1, 5),
    _AdGenDhcpClientStatusIpAddress_Type()
)
adGenDhcpClientStatusIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDhcpClientStatusIpAddress.setStatus("current")
_AdGenDhcpClientStatusSubnetMaskType_Type = InetAddressType
_AdGenDhcpClientStatusSubnetMaskType_Object = MibTableColumn
adGenDhcpClientStatusSubnetMaskType = _AdGenDhcpClientStatusSubnetMaskType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 80, 1, 1, 1, 1, 1, 6),
    _AdGenDhcpClientStatusSubnetMaskType_Type()
)
adGenDhcpClientStatusSubnetMaskType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDhcpClientStatusSubnetMaskType.setStatus("current")
_AdGenDhcpClientStatusSubnetMask_Type = InetAddress
_AdGenDhcpClientStatusSubnetMask_Object = MibTableColumn
adGenDhcpClientStatusSubnetMask = _AdGenDhcpClientStatusSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 80, 1, 1, 1, 1, 1, 7),
    _AdGenDhcpClientStatusSubnetMask_Type()
)
adGenDhcpClientStatusSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDhcpClientStatusSubnetMask.setStatus("current")
_AdGenDhcpClientStatusDhcpLeaseServerType_Type = InetAddressType
_AdGenDhcpClientStatusDhcpLeaseServerType_Object = MibTableColumn
adGenDhcpClientStatusDhcpLeaseServerType = _AdGenDhcpClientStatusDhcpLeaseServerType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 80, 1, 1, 1, 1, 1, 8),
    _AdGenDhcpClientStatusDhcpLeaseServerType_Type()
)
adGenDhcpClientStatusDhcpLeaseServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDhcpClientStatusDhcpLeaseServerType.setStatus("current")
_AdGenDhcpClientStatusDhcpLeaseServer_Type = InetAddress
_AdGenDhcpClientStatusDhcpLeaseServer_Object = MibTableColumn
adGenDhcpClientStatusDhcpLeaseServer = _AdGenDhcpClientStatusDhcpLeaseServer_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 80, 1, 1, 1, 1, 1, 9),
    _AdGenDhcpClientStatusDhcpLeaseServer_Type()
)
adGenDhcpClientStatusDhcpLeaseServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDhcpClientStatusDhcpLeaseServer.setStatus("current")
_AdGenDhcpClientStatusLease_Type = Unsigned32
_AdGenDhcpClientStatusLease_Object = MibTableColumn
adGenDhcpClientStatusLease = _AdGenDhcpClientStatusLease_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 80, 1, 1, 1, 1, 1, 10),
    _AdGenDhcpClientStatusLease_Type()
)
adGenDhcpClientStatusLease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDhcpClientStatusLease.setStatus("current")
_AdGenDhcpClientStatusLeaseRemaining_Type = Unsigned32
_AdGenDhcpClientStatusLeaseRemaining_Object = MibTableColumn
adGenDhcpClientStatusLeaseRemaining = _AdGenDhcpClientStatusLeaseRemaining_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 80, 1, 1, 1, 1, 1, 11),
    _AdGenDhcpClientStatusLeaseRemaining_Type()
)
adGenDhcpClientStatusLeaseRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDhcpClientStatusLeaseRemaining.setStatus("current")
_AdGenDhcpClientStatusPrimaryDNSType_Type = InetAddressType
_AdGenDhcpClientStatusPrimaryDNSType_Object = MibTableColumn
adGenDhcpClientStatusPrimaryDNSType = _AdGenDhcpClientStatusPrimaryDNSType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 80, 1, 1, 1, 1, 1, 12),
    _AdGenDhcpClientStatusPrimaryDNSType_Type()
)
adGenDhcpClientStatusPrimaryDNSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDhcpClientStatusPrimaryDNSType.setStatus("current")
_AdGenDhcpClientStatusPrimaryDNS_Type = InetAddress
_AdGenDhcpClientStatusPrimaryDNS_Object = MibTableColumn
adGenDhcpClientStatusPrimaryDNS = _AdGenDhcpClientStatusPrimaryDNS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 80, 1, 1, 1, 1, 1, 13),
    _AdGenDhcpClientStatusPrimaryDNS_Type()
)
adGenDhcpClientStatusPrimaryDNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDhcpClientStatusPrimaryDNS.setStatus("current")
_AdGenDhcpClientStatusSecondaryDNSType_Type = InetAddressType
_AdGenDhcpClientStatusSecondaryDNSType_Object = MibTableColumn
adGenDhcpClientStatusSecondaryDNSType = _AdGenDhcpClientStatusSecondaryDNSType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 80, 1, 1, 1, 1, 1, 14),
    _AdGenDhcpClientStatusSecondaryDNSType_Type()
)
adGenDhcpClientStatusSecondaryDNSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDhcpClientStatusSecondaryDNSType.setStatus("current")
_AdGenDhcpClientStatusSecondaryDNS_Type = InetAddress
_AdGenDhcpClientStatusSecondaryDNS_Object = MibTableColumn
adGenDhcpClientStatusSecondaryDNS = _AdGenDhcpClientStatusSecondaryDNS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 80, 1, 1, 1, 1, 1, 15),
    _AdGenDhcpClientStatusSecondaryDNS_Type()
)
adGenDhcpClientStatusSecondaryDNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDhcpClientStatusSecondaryDNS.setStatus("current")
_AdGenDhcpClientStatusRoutersType_Type = InetAddressType
_AdGenDhcpClientStatusRoutersType_Object = MibTableColumn
adGenDhcpClientStatusRoutersType = _AdGenDhcpClientStatusRoutersType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 80, 1, 1, 1, 1, 1, 16),
    _AdGenDhcpClientStatusRoutersType_Type()
)
adGenDhcpClientStatusRoutersType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDhcpClientStatusRoutersType.setStatus("current")
_AdGenDhcpClientStatusRouters_Type = InetAddress
_AdGenDhcpClientStatusRouters_Object = MibTableColumn
adGenDhcpClientStatusRouters = _AdGenDhcpClientStatusRouters_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 80, 1, 1, 1, 1, 1, 17),
    _AdGenDhcpClientStatusRouters_Type()
)
adGenDhcpClientStatusRouters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDhcpClientStatusRouters.setStatus("current")
_AdGenDhcpClientStatusTxDiscovery_Type = Counter32
_AdGenDhcpClientStatusTxDiscovery_Object = MibTableColumn
adGenDhcpClientStatusTxDiscovery = _AdGenDhcpClientStatusTxDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 80, 1, 1, 1, 1, 1, 18),
    _AdGenDhcpClientStatusTxDiscovery_Type()
)
adGenDhcpClientStatusTxDiscovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDhcpClientStatusTxDiscovery.setStatus("current")
_AdGenDhcpClientStatusTxRequest_Type = Counter32
_AdGenDhcpClientStatusTxRequest_Object = MibTableColumn
adGenDhcpClientStatusTxRequest = _AdGenDhcpClientStatusTxRequest_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 80, 1, 1, 1, 1, 1, 19),
    _AdGenDhcpClientStatusTxRequest_Type()
)
adGenDhcpClientStatusTxRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDhcpClientStatusTxRequest.setStatus("current")
_AdGenDhcpClientStatusTxDecline_Type = Counter32
_AdGenDhcpClientStatusTxDecline_Object = MibTableColumn
adGenDhcpClientStatusTxDecline = _AdGenDhcpClientStatusTxDecline_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 80, 1, 1, 1, 1, 1, 20),
    _AdGenDhcpClientStatusTxDecline_Type()
)
adGenDhcpClientStatusTxDecline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDhcpClientStatusTxDecline.setStatus("current")
_AdGenDhcpClientStatusTxRelease_Type = Counter32
_AdGenDhcpClientStatusTxRelease_Object = MibTableColumn
adGenDhcpClientStatusTxRelease = _AdGenDhcpClientStatusTxRelease_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 80, 1, 1, 1, 1, 1, 21),
    _AdGenDhcpClientStatusTxRelease_Type()
)
adGenDhcpClientStatusTxRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDhcpClientStatusTxRelease.setStatus("current")
_AdGenDhcpClientStatusTxInform_Type = Counter32
_AdGenDhcpClientStatusTxInform_Object = MibTableColumn
adGenDhcpClientStatusTxInform = _AdGenDhcpClientStatusTxInform_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 80, 1, 1, 1, 1, 1, 22),
    _AdGenDhcpClientStatusTxInform_Type()
)
adGenDhcpClientStatusTxInform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDhcpClientStatusTxInform.setStatus("current")
_AdGenDhcpClientStatusRxOffer_Type = Counter32
_AdGenDhcpClientStatusRxOffer_Object = MibTableColumn
adGenDhcpClientStatusRxOffer = _AdGenDhcpClientStatusRxOffer_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 80, 1, 1, 1, 1, 1, 23),
    _AdGenDhcpClientStatusRxOffer_Type()
)
adGenDhcpClientStatusRxOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDhcpClientStatusRxOffer.setStatus("current")
_AdGenDhcpClientStatusRxAck_Type = Counter32
_AdGenDhcpClientStatusRxAck_Object = MibTableColumn
adGenDhcpClientStatusRxAck = _AdGenDhcpClientStatusRxAck_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 80, 1, 1, 1, 1, 1, 24),
    _AdGenDhcpClientStatusRxAck_Type()
)
adGenDhcpClientStatusRxAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDhcpClientStatusRxAck.setStatus("current")
_AdGenDhcpClientStatusRxNak_Type = Counter32
_AdGenDhcpClientStatusRxNak_Object = MibTableColumn
adGenDhcpClientStatusRxNak = _AdGenDhcpClientStatusRxNak_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 80, 1, 1, 1, 1, 1, 25),
    _AdGenDhcpClientStatusRxNak_Type()
)
adGenDhcpClientStatusRxNak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDhcpClientStatusRxNak.setStatus("current")
_AdGenDhcpClientStatusRxRunt_Type = Counter32
_AdGenDhcpClientStatusRxRunt_Object = MibTableColumn
adGenDhcpClientStatusRxRunt = _AdGenDhcpClientStatusRxRunt_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 80, 1, 1, 1, 1, 1, 26),
    _AdGenDhcpClientStatusRxRunt_Type()
)
adGenDhcpClientStatusRxRunt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDhcpClientStatusRxRunt.setStatus("current")
_AdGenDhcpClientStatusRxInvalid_Type = Counter32
_AdGenDhcpClientStatusRxInvalid_Object = MibTableColumn
adGenDhcpClientStatusRxInvalid = _AdGenDhcpClientStatusRxInvalid_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 80, 1, 1, 1, 1, 1, 27),
    _AdGenDhcpClientStatusRxInvalid_Type()
)
adGenDhcpClientStatusRxInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDhcpClientStatusRxInvalid.setStatus("current")
_AdGenDhcpClientStatusRxOos_Type = Counter32
_AdGenDhcpClientStatusRxOos_Object = MibTableColumn
adGenDhcpClientStatusRxOos = _AdGenDhcpClientStatusRxOos_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 80, 1, 1, 1, 1, 1, 28),
    _AdGenDhcpClientStatusRxOos_Type()
)
adGenDhcpClientStatusRxOos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDhcpClientStatusRxOos.setStatus("current")
_AdGenDhcpClientCommand_ObjectIdentity = ObjectIdentity
adGenDhcpClientCommand = _AdGenDhcpClientCommand_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 80, 1, 1, 2)
)
_AdGenDhcpClientCommandTable_Object = MibTable
adGenDhcpClientCommandTable = _AdGenDhcpClientCommandTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 80, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    adGenDhcpClientCommandTable.setStatus("current")
_AdGenDhcpClientCommandEntry_Object = MibTableRow
adGenDhcpClientCommandEntry = _AdGenDhcpClientCommandEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 80, 1, 1, 2, 1, 1)
)
adGenDhcpClientCommandEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenDhcpClientCommandEntry.setStatus("current")


class _AdGenDhcpClientCommandRenew_Type(Integer32):
    """Custom type adGenDhcpClientCommandRenew based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("renew", 1)
    )


_AdGenDhcpClientCommandRenew_Type.__name__ = "Integer32"
_AdGenDhcpClientCommandRenew_Object = MibTableColumn
adGenDhcpClientCommandRenew = _AdGenDhcpClientCommandRenew_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 80, 1, 1, 2, 1, 1, 1),
    _AdGenDhcpClientCommandRenew_Type()
)
adGenDhcpClientCommandRenew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenDhcpClientCommandRenew.setStatus("current")


class _AdGenDhcpClientCommandRelease_Type(Integer32):
    """Custom type adGenDhcpClientCommandRelease based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("release", 1)
    )


_AdGenDhcpClientCommandRelease_Type.__name__ = "Integer32"
_AdGenDhcpClientCommandRelease_Object = MibTableColumn
adGenDhcpClientCommandRelease = _AdGenDhcpClientCommandRelease_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 80, 1, 1, 2, 1, 1, 2),
    _AdGenDhcpClientCommandRelease_Type()
)
adGenDhcpClientCommandRelease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenDhcpClientCommandRelease.setStatus("current")


class _AdGenDhcpClientCommandResetStats_Type(Integer32):
    """Custom type adGenDhcpClientCommandResetStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdGenDhcpClientCommandResetStats_Type.__name__ = "Integer32"
_AdGenDhcpClientCommandResetStats_Object = MibTableColumn
adGenDhcpClientCommandResetStats = _AdGenDhcpClientCommandResetStats_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 80, 1, 1, 2, 1, 1, 3),
    _AdGenDhcpClientCommandResetStats_Type()
)
adGenDhcpClientCommandResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenDhcpClientCommandResetStats.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GEN-DHCP-CLIENT-MIB",
    **{"AdGenDhcpClientState": AdGenDhcpClientState,
       "adGenDhcpClientMIBObjects": adGenDhcpClientMIBObjects,
       "adGenDhcpClientStatus": adGenDhcpClientStatus,
       "adGenDhcpClientStatusTable": adGenDhcpClientStatusTable,
       "adGenDhcpClientStatusEntry": adGenDhcpClientStatusEntry,
       "adGenDhcpClientStatusState": adGenDhcpClientStatusState,
       "adGenDhcpClientStatusClientIdentifier": adGenDhcpClientStatusClientIdentifier,
       "adGenDhcpClientStatusHostName": adGenDhcpClientStatusHostName,
       "adGenDhcpClientStatusIpAddressType": adGenDhcpClientStatusIpAddressType,
       "adGenDhcpClientStatusIpAddress": adGenDhcpClientStatusIpAddress,
       "adGenDhcpClientStatusSubnetMaskType": adGenDhcpClientStatusSubnetMaskType,
       "adGenDhcpClientStatusSubnetMask": adGenDhcpClientStatusSubnetMask,
       "adGenDhcpClientStatusDhcpLeaseServerType": adGenDhcpClientStatusDhcpLeaseServerType,
       "adGenDhcpClientStatusDhcpLeaseServer": adGenDhcpClientStatusDhcpLeaseServer,
       "adGenDhcpClientStatusLease": adGenDhcpClientStatusLease,
       "adGenDhcpClientStatusLeaseRemaining": adGenDhcpClientStatusLeaseRemaining,
       "adGenDhcpClientStatusPrimaryDNSType": adGenDhcpClientStatusPrimaryDNSType,
       "adGenDhcpClientStatusPrimaryDNS": adGenDhcpClientStatusPrimaryDNS,
       "adGenDhcpClientStatusSecondaryDNSType": adGenDhcpClientStatusSecondaryDNSType,
       "adGenDhcpClientStatusSecondaryDNS": adGenDhcpClientStatusSecondaryDNS,
       "adGenDhcpClientStatusRoutersType": adGenDhcpClientStatusRoutersType,
       "adGenDhcpClientStatusRouters": adGenDhcpClientStatusRouters,
       "adGenDhcpClientStatusTxDiscovery": adGenDhcpClientStatusTxDiscovery,
       "adGenDhcpClientStatusTxRequest": adGenDhcpClientStatusTxRequest,
       "adGenDhcpClientStatusTxDecline": adGenDhcpClientStatusTxDecline,
       "adGenDhcpClientStatusTxRelease": adGenDhcpClientStatusTxRelease,
       "adGenDhcpClientStatusTxInform": adGenDhcpClientStatusTxInform,
       "adGenDhcpClientStatusRxOffer": adGenDhcpClientStatusRxOffer,
       "adGenDhcpClientStatusRxAck": adGenDhcpClientStatusRxAck,
       "adGenDhcpClientStatusRxNak": adGenDhcpClientStatusRxNak,
       "adGenDhcpClientStatusRxRunt": adGenDhcpClientStatusRxRunt,
       "adGenDhcpClientStatusRxInvalid": adGenDhcpClientStatusRxInvalid,
       "adGenDhcpClientStatusRxOos": adGenDhcpClientStatusRxOos,
       "adGenDhcpClientCommand": adGenDhcpClientCommand,
       "adGenDhcpClientCommandTable": adGenDhcpClientCommandTable,
       "adGenDhcpClientCommandEntry": adGenDhcpClientCommandEntry,
       "adGenDhcpClientCommandRenew": adGenDhcpClientCommandRenew,
       "adGenDhcpClientCommandRelease": adGenDhcpClientCommandRelease,
       "adGenDhcpClientCommandResetStats": adGenDhcpClientCommandResetStats,
       "adGenDhcpClientMib": adGenDhcpClientMib}
)
