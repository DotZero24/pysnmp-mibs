_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cmtsC3,=mibBuilder.importSymbols('ARRIS-MIB','cmtsC3')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
cmtsC3TFTPDMIB=ModuleIdentity((1,3,6,1,4,1,4115,1,4,3,9))
_DcxTFTPDObjects_ObjectIdentity=ObjectIdentity
dcxTFTPDObjects=_DcxTFTPDObjects_ObjectIdentity((1,3,6,1,4,1,4115,1,4,3,9,1))
class _DcxTFTPDServerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('inactive',0),('active',1)))
_DcxTFTPDServerState_Type.__name__=_D
_DcxTFTPDServerState_Object=MibScalar
dcxTFTPDServerState=_DcxTFTPDServerState_Object((1,3,6,1,4,1,4115,1,4,3,9,1,1),_DcxTFTPDServerState_Type())
dcxTFTPDServerState.setMaxAccess(_C)
if mibBuilder.loadTexts:dcxTFTPDServerState.setStatus(_A)
_DcxTFTPDCurrentDirectory_Type=DisplayString
_DcxTFTPDCurrentDirectory_Object=MibScalar
dcxTFTPDCurrentDirectory=_DcxTFTPDCurrentDirectory_Object((1,3,6,1,4,1,4115,1,4,3,9,1,2),_DcxTFTPDCurrentDirectory_Type())
dcxTFTPDCurrentDirectory.setMaxAccess(_C)
if mibBuilder.loadTexts:dcxTFTPDCurrentDirectory.setStatus(_A)
class _DcxTFTPDIpVerification_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disabled',0),('enabled',1)))
_DcxTFTPDIpVerification_Type.__name__=_D
_DcxTFTPDIpVerification_Object=MibScalar
dcxTFTPDIpVerification=_DcxTFTPDIpVerification_Object((1,3,6,1,4,1,4115,1,4,3,9,1,3),_DcxTFTPDIpVerification_Type())
dcxTFTPDIpVerification.setMaxAccess(_C)
if mibBuilder.loadTexts:dcxTFTPDIpVerification.setStatus(_A)
_DcxTFTPDClearCache_Type=TruthValue
_DcxTFTPDClearCache_Object=MibScalar
dcxTFTPDClearCache=_DcxTFTPDClearCache_Object((1,3,6,1,4,1,4115,1,4,3,9,1,4),_DcxTFTPDClearCache_Type())
dcxTFTPDClearCache.setMaxAccess(_C)
if mibBuilder.loadTexts:dcxTFTPDClearCache.setStatus(_A)
_DcxTFTPDReadRequests_Type=Counter32
_DcxTFTPDReadRequests_Object=MibScalar
dcxTFTPDReadRequests=_DcxTFTPDReadRequests_Object((1,3,6,1,4,1,4115,1,4,3,9,1,5),_DcxTFTPDReadRequests_Type())
dcxTFTPDReadRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxTFTPDReadRequests.setStatus(_A)
_DcxTFTPDReadRequestsDropped_Type=Counter32
_DcxTFTPDReadRequestsDropped_Object=MibScalar
dcxTFTPDReadRequestsDropped=_DcxTFTPDReadRequestsDropped_Object((1,3,6,1,4,1,4115,1,4,3,9,1,6),_DcxTFTPDReadRequestsDropped_Type())
dcxTFTPDReadRequestsDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxTFTPDReadRequestsDropped.setStatus(_A)
_DcxTFTPDReadRequestsFailed_Type=Counter32
_DcxTFTPDReadRequestsFailed_Object=MibScalar
dcxTFTPDReadRequestsFailed=_DcxTFTPDReadRequestsFailed_Object((1,3,6,1,4,1,4115,1,4,3,9,1,7),_DcxTFTPDReadRequestsFailed_Type())
dcxTFTPDReadRequestsFailed.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxTFTPDReadRequestsFailed.setStatus(_A)
_DcxTFTPDReadBytes_Type=Counter32
_DcxTFTPDReadBytes_Object=MibScalar
dcxTFTPDReadBytes=_DcxTFTPDReadBytes_Object((1,3,6,1,4,1,4115,1,4,3,9,1,8),_DcxTFTPDReadBytes_Type())
dcxTFTPDReadBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxTFTPDReadBytes.setStatus(_A)
_DcxTFTPDWriteRequests_Type=Counter32
_DcxTFTPDWriteRequests_Object=MibScalar
dcxTFTPDWriteRequests=_DcxTFTPDWriteRequests_Object((1,3,6,1,4,1,4115,1,4,3,9,1,9),_DcxTFTPDWriteRequests_Type())
dcxTFTPDWriteRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxTFTPDWriteRequests.setStatus(_A)
_DcxTFTPDWriteRequestsDropped_Type=Counter32
_DcxTFTPDWriteRequestsDropped_Object=MibScalar
dcxTFTPDWriteRequestsDropped=_DcxTFTPDWriteRequestsDropped_Object((1,3,6,1,4,1,4115,1,4,3,9,1,10),_DcxTFTPDWriteRequestsDropped_Type())
dcxTFTPDWriteRequestsDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxTFTPDWriteRequestsDropped.setStatus(_A)
_DcxTFTPDWriteRequestsFailed_Type=Counter32
_DcxTFTPDWriteRequestsFailed_Object=MibScalar
dcxTFTPDWriteRequestsFailed=_DcxTFTPDWriteRequestsFailed_Object((1,3,6,1,4,1,4115,1,4,3,9,1,11),_DcxTFTPDWriteRequestsFailed_Type())
dcxTFTPDWriteRequestsFailed.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxTFTPDWriteRequestsFailed.setStatus(_A)
_DcxTFTPDWriteBytes_Type=Counter32
_DcxTFTPDWriteBytes_Object=MibScalar
dcxTFTPDWriteBytes=_DcxTFTPDWriteBytes_Object((1,3,6,1,4,1,4115,1,4,3,9,1,12),_DcxTFTPDWriteBytes_Type())
dcxTFTPDWriteBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxTFTPDWriteBytes.setStatus(_A)
mibBuilder.exportSymbols('ARRIS-C3-TFTPD-MIB',**{'cmtsC3TFTPDMIB':cmtsC3TFTPDMIB,'dcxTFTPDObjects':dcxTFTPDObjects,'dcxTFTPDServerState':dcxTFTPDServerState,'dcxTFTPDCurrentDirectory':dcxTFTPDCurrentDirectory,'dcxTFTPDIpVerification':dcxTFTPDIpVerification,'dcxTFTPDClearCache':dcxTFTPDClearCache,'dcxTFTPDReadRequests':dcxTFTPDReadRequests,'dcxTFTPDReadRequestsDropped':dcxTFTPDReadRequestsDropped,'dcxTFTPDReadRequestsFailed':dcxTFTPDReadRequestsFailed,'dcxTFTPDReadBytes':dcxTFTPDReadBytes,'dcxTFTPDWriteRequests':dcxTFTPDWriteRequests,'dcxTFTPDWriteRequestsDropped':dcxTFTPDWriteRequestsDropped,'dcxTFTPDWriteRequestsFailed':dcxTFTPDWriteRequestsFailed,'dcxTFTPDWriteBytes':dcxTFTPDWriteBytes})