# SNMP MIB module (DHCP-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/DHCP-CLIENT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:36:25 2025
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

(iscomSwitch,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "iscomSwitch")

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

(Vlanset,) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "Vlanset")


# MODULE-IDENTITY

rcDhcpClient = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 25)
)
if mibBuilder.loadTexts:
    rcDhcpClient.setRevisions(
        ("2007-08-30 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcDhcpClientMibObjects_ObjectIdentity = ObjectIdentity
rcDhcpClientMibObjects = _RcDhcpClientMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 25, 1)
)
_RcDhcpClientRequestTable_Object = MibTable
rcDhcpClientRequestTable = _RcDhcpClientRequestTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 25, 1, 1)
)
if mibBuilder.loadTexts:
    rcDhcpClientRequestTable.setStatus("current")
_RcDhcpClientRequestEntry_Object = MibTableRow
rcDhcpClientRequestEntry = _RcDhcpClientRequestEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 25, 1, 1, 1)
)
rcDhcpClientRequestEntry.setIndexNames(
    (0, "DHCP-CLIENT-MIB", "rcDhcpClientRequestIfIndex"),
)
if mibBuilder.loadTexts:
    rcDhcpClientRequestEntry.setStatus("current")
_RcDhcpClientRequestIfIndex_Type = Integer32
_RcDhcpClientRequestIfIndex_Object = MibTableColumn
rcDhcpClientRequestIfIndex = _RcDhcpClientRequestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 25, 1, 1, 1, 1),
    _RcDhcpClientRequestIfIndex_Type()
)
rcDhcpClientRequestIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcDhcpClientRequestIfIndex.setStatus("current")


class _RcDhcpClientRequestHostname_Type(OctetString):
    """Custom type rcDhcpClientRequestHostname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RcDhcpClientRequestHostname_Type.__name__ = "OctetString"
_RcDhcpClientRequestHostname_Object = MibTableColumn
rcDhcpClientRequestHostname = _RcDhcpClientRequestHostname_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 25, 1, 1, 1, 2),
    _RcDhcpClientRequestHostname_Type()
)
rcDhcpClientRequestHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDhcpClientRequestHostname.setStatus("current")


class _RcDhcpClientRequestClassid_Type(OctetString):
    """Custom type rcDhcpClientRequestClassid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RcDhcpClientRequestClassid_Type.__name__ = "OctetString"
_RcDhcpClientRequestClassid_Object = MibTableColumn
rcDhcpClientRequestClassid = _RcDhcpClientRequestClassid_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 25, 1, 1, 1, 3),
    _RcDhcpClientRequestClassid_Type()
)
rcDhcpClientRequestClassid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDhcpClientRequestClassid.setStatus("current")


class _RcDhcpClientRequestClientid_Type(OctetString):
    """Custom type rcDhcpClientRequestClientid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RcDhcpClientRequestClientid_Type.__name__ = "OctetString"
_RcDhcpClientRequestClientid_Object = MibTableColumn
rcDhcpClientRequestClientid = _RcDhcpClientRequestClientid_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 25, 1, 1, 1, 4),
    _RcDhcpClientRequestClientid_Type()
)
rcDhcpClientRequestClientid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDhcpClientRequestClientid.setStatus("current")
_RcDhcpClientRequestVlans_Type = Vlanset
_RcDhcpClientRequestVlans_Object = MibTableColumn
rcDhcpClientRequestVlans = _RcDhcpClientRequestVlans_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 25, 1, 1, 1, 5),
    _RcDhcpClientRequestVlans_Type()
)
rcDhcpClientRequestVlans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDhcpClientRequestVlans.setStatus("deprecated")


class _RcDhcpClientRequestOperationType_Type(Integer32):
    """Custom type rcDhcpClientRequestOperationType based on Integer32"""
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
        *(("none", 1),
          ("request", 2),
          ("renew", 3),
          ("release", 4))
    )


_RcDhcpClientRequestOperationType_Type.__name__ = "Integer32"
_RcDhcpClientRequestOperationType_Object = MibTableColumn
rcDhcpClientRequestOperationType = _RcDhcpClientRequestOperationType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 25, 1, 1, 1, 6),
    _RcDhcpClientRequestOperationType_Type()
)
rcDhcpClientRequestOperationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDhcpClientRequestOperationType.setStatus("current")


class _RcDhcpClientRequestOperationStates_Type(Integer32):
    """Custom type rcDhcpClientRequestOperationStates based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("initialize", 1),
          ("requesting", 2),
          ("requestsuccessfully", 3),
          ("requestgetfailed", 4),
          ("requestconfigfailed", 5),
          ("renewing", 6),
          ("renewsuccessfully", 7),
          ("renewfailed", 8))
    )


_RcDhcpClientRequestOperationStates_Type.__name__ = "Integer32"
_RcDhcpClientRequestOperationStates_Object = MibTableColumn
rcDhcpClientRequestOperationStates = _RcDhcpClientRequestOperationStates_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 25, 1, 1, 1, 7),
    _RcDhcpClientRequestOperationStates_Type()
)
rcDhcpClientRequestOperationStates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpClientRequestOperationStates.setStatus("current")
_RcDhcpClientRequestIpAddress_Type = IpAddress
_RcDhcpClientRequestIpAddress_Object = MibTableColumn
rcDhcpClientRequestIpAddress = _RcDhcpClientRequestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 25, 1, 1, 1, 8),
    _RcDhcpClientRequestIpAddress_Type()
)
rcDhcpClientRequestIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpClientRequestIpAddress.setStatus("current")
_RcDhcpClientRequestDefaultGateway_Type = IpAddress
_RcDhcpClientRequestDefaultGateway_Object = MibTableColumn
rcDhcpClientRequestDefaultGateway = _RcDhcpClientRequestDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 25, 1, 1, 1, 9),
    _RcDhcpClientRequestDefaultGateway_Type()
)
rcDhcpClientRequestDefaultGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpClientRequestDefaultGateway.setStatus("current")
_RcDhcpClientRequestSubnetMask_Type = IpAddress
_RcDhcpClientRequestSubnetMask_Object = MibTableColumn
rcDhcpClientRequestSubnetMask = _RcDhcpClientRequestSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 25, 1, 1, 1, 10),
    _RcDhcpClientRequestSubnetMask_Type()
)
rcDhcpClientRequestSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpClientRequestSubnetMask.setStatus("current")
_RcDhcpClientRequestLeaseStarts_Type = Unsigned32
_RcDhcpClientRequestLeaseStarts_Object = MibTableColumn
rcDhcpClientRequestLeaseStarts = _RcDhcpClientRequestLeaseStarts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 25, 1, 1, 1, 11),
    _RcDhcpClientRequestLeaseStarts_Type()
)
rcDhcpClientRequestLeaseStarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpClientRequestLeaseStarts.setStatus("current")
_RcDhcpClientRequestLeaseEnds_Type = Unsigned32
_RcDhcpClientRequestLeaseEnds_Object = MibTableColumn
rcDhcpClientRequestLeaseEnds = _RcDhcpClientRequestLeaseEnds_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 25, 1, 1, 1, 12),
    _RcDhcpClientRequestLeaseEnds_Type()
)
rcDhcpClientRequestLeaseEnds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpClientRequestLeaseEnds.setStatus("current")
_RcDhcpClientRequestLeaseDuration_Type = Unsigned32
_RcDhcpClientRequestLeaseDuration_Object = MibTableColumn
rcDhcpClientRequestLeaseDuration = _RcDhcpClientRequestLeaseDuration_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 25, 1, 1, 1, 13),
    _RcDhcpClientRequestLeaseDuration_Type()
)
rcDhcpClientRequestLeaseDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpClientRequestLeaseDuration.setStatus("current")
_RcDhcpClientRequestDhcpSvr_Type = IpAddress
_RcDhcpClientRequestDhcpSvr_Object = MibTableColumn
rcDhcpClientRequestDhcpSvr = _RcDhcpClientRequestDhcpSvr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 25, 1, 1, 1, 14),
    _RcDhcpClientRequestDhcpSvr_Type()
)
rcDhcpClientRequestDhcpSvr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpClientRequestDhcpSvr.setStatus("current")


class _RcDhcpClientRequestTftpSvrName_Type(OctetString):
    """Custom type rcDhcpClientRequestTftpSvrName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RcDhcpClientRequestTftpSvrName_Type.__name__ = "OctetString"
_RcDhcpClientRequestTftpSvrName_Object = MibTableColumn
rcDhcpClientRequestTftpSvrName = _RcDhcpClientRequestTftpSvrName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 25, 1, 1, 1, 15),
    _RcDhcpClientRequestTftpSvrName_Type()
)
rcDhcpClientRequestTftpSvrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpClientRequestTftpSvrName.setStatus("current")
_RcDhcpClientRequestTftpSvrAddr_Type = IpAddress
_RcDhcpClientRequestTftpSvrAddr_Object = MibTableColumn
rcDhcpClientRequestTftpSvrAddr = _RcDhcpClientRequestTftpSvrAddr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 25, 1, 1, 1, 16),
    _RcDhcpClientRequestTftpSvrAddr_Type()
)
rcDhcpClientRequestTftpSvrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpClientRequestTftpSvrAddr.setStatus("current")


class _RcDhcpClientRequestStartupConfFile_Type(OctetString):
    """Custom type rcDhcpClientRequestStartupConfFile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RcDhcpClientRequestStartupConfFile_Type.__name__ = "OctetString"
_RcDhcpClientRequestStartupConfFile_Object = MibTableColumn
rcDhcpClientRequestStartupConfFile = _RcDhcpClientRequestStartupConfFile_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 25, 1, 1, 1, 17),
    _RcDhcpClientRequestStartupConfFile_Type()
)
rcDhcpClientRequestStartupConfFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpClientRequestStartupConfFile.setStatus("current")


class _RcDhcpClientRequestResultStates_Type(Integer32):
    """Custom type rcDhcpClientRequestResultStates based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unavailable", 1),
          ("available", 2))
    )


_RcDhcpClientRequestResultStates_Type.__name__ = "Integer32"
_RcDhcpClientRequestResultStates_Object = MibTableColumn
rcDhcpClientRequestResultStates = _RcDhcpClientRequestResultStates_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 25, 1, 1, 1, 18),
    _RcDhcpClientRequestResultStates_Type()
)
rcDhcpClientRequestResultStates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpClientRequestResultStates.setStatus("current")
_RcDhcpClientRequestSpecifySvr_Type = IpAddress
_RcDhcpClientRequestSpecifySvr_Object = MibTableColumn
rcDhcpClientRequestSpecifySvr = _RcDhcpClientRequestSpecifySvr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 25, 1, 1, 1, 19),
    _RcDhcpClientRequestSpecifySvr_Type()
)
rcDhcpClientRequestSpecifySvr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpClientRequestSpecifySvr.setStatus("current")


class _RcDhcpClientRequestRootPath_Type(OctetString):
    """Custom type rcDhcpClientRequestRootPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RcDhcpClientRequestRootPath_Type.__name__ = "OctetString"
_RcDhcpClientRequestRootPath_Object = MibTableColumn
rcDhcpClientRequestRootPath = _RcDhcpClientRequestRootPath_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 25, 1, 1, 1, 20),
    _RcDhcpClientRequestRootPath_Type()
)
rcDhcpClientRequestRootPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpClientRequestRootPath.setStatus("current")
_RcDhcpClientRequestNtpServer_Type = IpAddress
_RcDhcpClientRequestNtpServer_Object = MibTableColumn
rcDhcpClientRequestNtpServer = _RcDhcpClientRequestNtpServer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 25, 1, 1, 1, 21),
    _RcDhcpClientRequestNtpServer_Type()
)
rcDhcpClientRequestNtpServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpClientRequestNtpServer.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DHCP-CLIENT-MIB",
    **{"rcDhcpClient": rcDhcpClient,
       "rcDhcpClientMibObjects": rcDhcpClientMibObjects,
       "rcDhcpClientRequestTable": rcDhcpClientRequestTable,
       "rcDhcpClientRequestEntry": rcDhcpClientRequestEntry,
       "rcDhcpClientRequestIfIndex": rcDhcpClientRequestIfIndex,
       "rcDhcpClientRequestHostname": rcDhcpClientRequestHostname,
       "rcDhcpClientRequestClassid": rcDhcpClientRequestClassid,
       "rcDhcpClientRequestClientid": rcDhcpClientRequestClientid,
       "rcDhcpClientRequestVlans": rcDhcpClientRequestVlans,
       "rcDhcpClientRequestOperationType": rcDhcpClientRequestOperationType,
       "rcDhcpClientRequestOperationStates": rcDhcpClientRequestOperationStates,
       "rcDhcpClientRequestIpAddress": rcDhcpClientRequestIpAddress,
       "rcDhcpClientRequestDefaultGateway": rcDhcpClientRequestDefaultGateway,
       "rcDhcpClientRequestSubnetMask": rcDhcpClientRequestSubnetMask,
       "rcDhcpClientRequestLeaseStarts": rcDhcpClientRequestLeaseStarts,
       "rcDhcpClientRequestLeaseEnds": rcDhcpClientRequestLeaseEnds,
       "rcDhcpClientRequestLeaseDuration": rcDhcpClientRequestLeaseDuration,
       "rcDhcpClientRequestDhcpSvr": rcDhcpClientRequestDhcpSvr,
       "rcDhcpClientRequestTftpSvrName": rcDhcpClientRequestTftpSvrName,
       "rcDhcpClientRequestTftpSvrAddr": rcDhcpClientRequestTftpSvrAddr,
       "rcDhcpClientRequestStartupConfFile": rcDhcpClientRequestStartupConfFile,
       "rcDhcpClientRequestResultStates": rcDhcpClientRequestResultStates,
       "rcDhcpClientRequestSpecifySvr": rcDhcpClientRequestSpecifySvr,
       "rcDhcpClientRequestRootPath": rcDhcpClientRequestRootPath,
       "rcDhcpClientRequestNtpServer": rcDhcpClientRequestNtpServer}
)
