_J='biboBrrpStatsVrId'
_I='biboBrrpStatsIfIndex'
_H='biboBrrpOperVrId'
_G='biboBrrpVirtIfIndex'
_F='OctetString'
_E='BRRP-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Bintec_ObjectIdentity=ObjectIdentity
bintec=_Bintec_ObjectIdentity((1,3,6,1,4,1,272))
_Bibo_ObjectIdentity=ObjectIdentity
bibo=_Bibo_ObjectIdentity((1,3,6,1,4,1,272,4))
_Brrp_ObjectIdentity=ObjectIdentity
brrp=_Brrp_ObjectIdentity((1,3,6,1,4,1,272,4,40))
_BiboBrrpOperTable_Object=MibTable
biboBrrpOperTable=_BiboBrrpOperTable_Object((1,3,6,1,4,1,272,4,40,1))
if mibBuilder.loadTexts:biboBrrpOperTable.setStatus(_A)
_BiboBrrpOperEntry_Object=MibTableRow
biboBrrpOperEntry=_BiboBrrpOperEntry_Object((1,3,6,1,4,1,272,4,40,1,1))
biboBrrpOperEntry.setIndexNames((0,_E,_G),(0,_E,_H))
if mibBuilder.loadTexts:biboBrrpOperEntry.setStatus(_A)
class _BiboBrrpOperVrId_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_BiboBrrpOperVrId_Type.__name__=_C
_BiboBrrpOperVrId_Object=MibTableColumn
biboBrrpOperVrId=_BiboBrrpOperVrId_Object((1,3,6,1,4,1,272,4,40,1,1,1),_BiboBrrpOperVrId_Type())
biboBrrpOperVrId.setMaxAccess(_D)
if mibBuilder.loadTexts:biboBrrpOperVrId.setStatus(_A)
_BiboBrrpVirtIfIndex_Type=Integer32
_BiboBrrpVirtIfIndex_Object=MibTableColumn
biboBrrpVirtIfIndex=_BiboBrrpVirtIfIndex_Object((1,3,6,1,4,1,272,4,40,1,1,2),_BiboBrrpVirtIfIndex_Type())
biboBrrpVirtIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:biboBrrpVirtIfIndex.setStatus(_A)
_BiboBrrpOperMasterIpAddr_Type=IpAddress
_BiboBrrpOperMasterIpAddr_Object=MibTableColumn
biboBrrpOperMasterIpAddr=_BiboBrrpOperMasterIpAddr_Object((1,3,6,1,4,1,272,4,40,1,1,3),_BiboBrrpOperMasterIpAddr_Type())
biboBrrpOperMasterIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:biboBrrpOperMasterIpAddr.setStatus(_A)
class _BiboBrrpOperState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('initialize',1),('backup',2),('master',3)))
_BiboBrrpOperState_Type.__name__=_C
_BiboBrrpOperState_Object=MibTableColumn
biboBrrpOperState=_BiboBrrpOperState_Object((1,3,6,1,4,1,272,4,40,1,1,4),_BiboBrrpOperState_Type())
biboBrrpOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:biboBrrpOperState.setStatus(_A)
class _BiboBrrpOperAdminState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),('delete',3)))
_BiboBrrpOperAdminState_Type.__name__=_C
_BiboBrrpOperAdminState_Object=MibTableColumn
biboBrrpOperAdminState=_BiboBrrpOperAdminState_Object((1,3,6,1,4,1,272,4,40,1,1,5),_BiboBrrpOperAdminState_Type())
biboBrrpOperAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:biboBrrpOperAdminState.setStatus(_A)
class _BiboBrrpOperPriority_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_BiboBrrpOperPriority_Type.__name__=_C
_BiboBrrpOperPriority_Object=MibTableColumn
biboBrrpOperPriority=_BiboBrrpOperPriority_Object((1,3,6,1,4,1,272,4,40,1,1,6),_BiboBrrpOperPriority_Type())
biboBrrpOperPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:biboBrrpOperPriority.setStatus(_A)
class _BiboBrrpOperAuthType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noAuthentication',1),('simpleTextPassword',2),('ipAuthenticationHeader',3)))
_BiboBrrpOperAuthType_Type.__name__=_C
_BiboBrrpOperAuthType_Object=MibTableColumn
biboBrrpOperAuthType=_BiboBrrpOperAuthType_Object((1,3,6,1,4,1,272,4,40,1,1,7),_BiboBrrpOperAuthType_Type())
biboBrrpOperAuthType.setMaxAccess(_D)
if mibBuilder.loadTexts:biboBrrpOperAuthType.setStatus(_A)
class _BiboBrrpOperAuthKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_BiboBrrpOperAuthKey_Type.__name__=_F
_BiboBrrpOperAuthKey_Object=MibTableColumn
biboBrrpOperAuthKey=_BiboBrrpOperAuthKey_Object((1,3,6,1,4,1,272,4,40,1,1,8),_BiboBrrpOperAuthKey_Type())
biboBrrpOperAuthKey.setMaxAccess(_D)
if mibBuilder.loadTexts:biboBrrpOperAuthKey.setStatus(_A)
class _BiboBrrpOperAdvertisementInterval_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_BiboBrrpOperAdvertisementInterval_Type.__name__=_C
_BiboBrrpOperAdvertisementInterval_Object=MibTableColumn
biboBrrpOperAdvertisementInterval=_BiboBrrpOperAdvertisementInterval_Object((1,3,6,1,4,1,272,4,40,1,1,9),_BiboBrrpOperAdvertisementInterval_Type())
biboBrrpOperAdvertisementInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:biboBrrpOperAdvertisementInterval.setStatus(_A)
class _BiboBrrpOperMasterDownRetries_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_BiboBrrpOperMasterDownRetries_Type.__name__=_C
_BiboBrrpOperMasterDownRetries_Object=MibTableColumn
biboBrrpOperMasterDownRetries=_BiboBrrpOperMasterDownRetries_Object((1,3,6,1,4,1,272,4,40,1,1,10),_BiboBrrpOperMasterDownRetries_Type())
biboBrrpOperMasterDownRetries.setMaxAccess(_D)
if mibBuilder.loadTexts:biboBrrpOperMasterDownRetries.setStatus(_A)
class _BiboBrrpOperPreemptMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('false',1),('true',2)))
_BiboBrrpOperPreemptMode_Type.__name__=_C
_BiboBrrpOperPreemptMode_Object=MibTableColumn
biboBrrpOperPreemptMode=_BiboBrrpOperPreemptMode_Object((1,3,6,1,4,1,272,4,40,1,1,11),_BiboBrrpOperPreemptMode_Type())
biboBrrpOperPreemptMode.setMaxAccess(_D)
if mibBuilder.loadTexts:biboBrrpOperPreemptMode.setStatus(_A)
_BiboBrrpOperVirtualRouterUpTime_Type=TimeTicks
_BiboBrrpOperVirtualRouterUpTime_Object=MibTableColumn
biboBrrpOperVirtualRouterUpTime=_BiboBrrpOperVirtualRouterUpTime_Object((1,3,6,1,4,1,272,4,40,1,1,12),_BiboBrrpOperVirtualRouterUpTime_Type())
biboBrrpOperVirtualRouterUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:biboBrrpOperVirtualRouterUpTime.setStatus(_A)
_BiboBrrpMasterIfIndex_Type=Integer32
_BiboBrrpMasterIfIndex_Object=MibTableColumn
biboBrrpMasterIfIndex=_BiboBrrpMasterIfIndex_Object((1,3,6,1,4,1,272,4,40,1,1,14),_BiboBrrpMasterIfIndex_Type())
biboBrrpMasterIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:biboBrrpMasterIfIndex.setStatus(_A)
class _BiboBrrpOperDecrPrio_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BiboBrrpOperDecrPrio_Type.__name__=_C
_BiboBrrpOperDecrPrio_Object=MibTableColumn
biboBrrpOperDecrPrio=_BiboBrrpOperDecrPrio_Object((1,3,6,1,4,1,272,4,40,1,1,15),_BiboBrrpOperDecrPrio_Type())
biboBrrpOperDecrPrio.setMaxAccess(_B)
if mibBuilder.loadTexts:biboBrrpOperDecrPrio.setStatus(_A)
_BiboBrrpRouterStatsTable_Object=MibTable
biboBrrpRouterStatsTable=_BiboBrrpRouterStatsTable_Object((1,3,6,1,4,1,272,4,40,2))
if mibBuilder.loadTexts:biboBrrpRouterStatsTable.setStatus(_A)
_BiboBrrpRouterStatsEntry_Object=MibTableRow
biboBrrpRouterStatsEntry=_BiboBrrpRouterStatsEntry_Object((1,3,6,1,4,1,272,4,40,2,1))
biboBrrpRouterStatsEntry.setIndexNames((0,_E,_I),(0,_E,_J))
if mibBuilder.loadTexts:biboBrrpRouterStatsEntry.setStatus(_A)
class _BiboBrrpStatsVrId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_BiboBrrpStatsVrId_Type.__name__=_C
_BiboBrrpStatsVrId_Object=MibTableColumn
biboBrrpStatsVrId=_BiboBrrpStatsVrId_Object((1,3,6,1,4,1,272,4,40,2,1,1),_BiboBrrpStatsVrId_Type())
biboBrrpStatsVrId.setMaxAccess(_B)
if mibBuilder.loadTexts:biboBrrpStatsVrId.setStatus(_A)
_BiboBrrpStatsIfIndex_Type=Integer32
_BiboBrrpStatsIfIndex_Object=MibTableColumn
biboBrrpStatsIfIndex=_BiboBrrpStatsIfIndex_Object((1,3,6,1,4,1,272,4,40,2,1,2),_BiboBrrpStatsIfIndex_Type())
biboBrrpStatsIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:biboBrrpStatsIfIndex.setStatus(_A)
_BiboBrrpStatsBecomeMaster_Type=Counter32
_BiboBrrpStatsBecomeMaster_Object=MibTableColumn
biboBrrpStatsBecomeMaster=_BiboBrrpStatsBecomeMaster_Object((1,3,6,1,4,1,272,4,40,2,1,3),_BiboBrrpStatsBecomeMaster_Type())
biboBrrpStatsBecomeMaster.setMaxAccess(_B)
if mibBuilder.loadTexts:biboBrrpStatsBecomeMaster.setStatus(_A)
_BiboBrrpStatsAdvertiseRcvd_Type=Counter32
_BiboBrrpStatsAdvertiseRcvd_Object=MibTableColumn
biboBrrpStatsAdvertiseRcvd=_BiboBrrpStatsAdvertiseRcvd_Object((1,3,6,1,4,1,272,4,40,2,1,4),_BiboBrrpStatsAdvertiseRcvd_Type())
biboBrrpStatsAdvertiseRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:biboBrrpStatsAdvertiseRcvd.setStatus(_A)
_BiboBrrpStatsAdvertiseIntervalErrors_Type=Counter32
_BiboBrrpStatsAdvertiseIntervalErrors_Object=MibTableColumn
biboBrrpStatsAdvertiseIntervalErrors=_BiboBrrpStatsAdvertiseIntervalErrors_Object((1,3,6,1,4,1,272,4,40,2,1,5),_BiboBrrpStatsAdvertiseIntervalErrors_Type())
biboBrrpStatsAdvertiseIntervalErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:biboBrrpStatsAdvertiseIntervalErrors.setStatus(_A)
_BiboBrrpStatsAuthFailures_Type=Counter32
_BiboBrrpStatsAuthFailures_Object=MibTableColumn
biboBrrpStatsAuthFailures=_BiboBrrpStatsAuthFailures_Object((1,3,6,1,4,1,272,4,40,2,1,6),_BiboBrrpStatsAuthFailures_Type())
biboBrrpStatsAuthFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:biboBrrpStatsAuthFailures.setStatus(_A)
_BiboBrrpStatsIpTtlErrors_Type=Counter32
_BiboBrrpStatsIpTtlErrors_Object=MibTableColumn
biboBrrpStatsIpTtlErrors=_BiboBrrpStatsIpTtlErrors_Object((1,3,6,1,4,1,272,4,40,2,1,7),_BiboBrrpStatsIpTtlErrors_Type())
biboBrrpStatsIpTtlErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:biboBrrpStatsIpTtlErrors.setStatus(_A)
_BiboBrrpStatsInvalidTypePktsRcvd_Type=Counter32
_BiboBrrpStatsInvalidTypePktsRcvd_Object=MibTableColumn
biboBrrpStatsInvalidTypePktsRcvd=_BiboBrrpStatsInvalidTypePktsRcvd_Object((1,3,6,1,4,1,272,4,40,2,1,8),_BiboBrrpStatsInvalidTypePktsRcvd_Type())
biboBrrpStatsInvalidTypePktsRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:biboBrrpStatsInvalidTypePktsRcvd.setStatus(_A)
_BiboBrrpStatsInvalidAuthType_Type=Counter32
_BiboBrrpStatsInvalidAuthType_Object=MibTableColumn
biboBrrpStatsInvalidAuthType=_BiboBrrpStatsInvalidAuthType_Object((1,3,6,1,4,1,272,4,40,2,1,9),_BiboBrrpStatsInvalidAuthType_Type())
biboBrrpStatsInvalidAuthType.setMaxAccess(_B)
if mibBuilder.loadTexts:biboBrrpStatsInvalidAuthType.setStatus(_A)
_BiboBrrpStatsAuthTypeMismatch_Type=Counter32
_BiboBrrpStatsAuthTypeMismatch_Object=MibTableColumn
biboBrrpStatsAuthTypeMismatch=_BiboBrrpStatsAuthTypeMismatch_Object((1,3,6,1,4,1,272,4,40,2,1,10),_BiboBrrpStatsAuthTypeMismatch_Type())
biboBrrpStatsAuthTypeMismatch.setMaxAccess(_B)
if mibBuilder.loadTexts:biboBrrpStatsAuthTypeMismatch.setStatus(_A)
_BiboBrrpStatsPacketLengthErrors_Type=Counter32
_BiboBrrpStatsPacketLengthErrors_Object=MibTableColumn
biboBrrpStatsPacketLengthErrors=_BiboBrrpStatsPacketLengthErrors_Object((1,3,6,1,4,1,272,4,40,2,1,11),_BiboBrrpStatsPacketLengthErrors_Type())
biboBrrpStatsPacketLengthErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:biboBrrpStatsPacketLengthErrors.setStatus(_A)
_BiboBrrpStatsChecksumErrors_Type=Counter32
_BiboBrrpStatsChecksumErrors_Object=MibTableColumn
biboBrrpStatsChecksumErrors=_BiboBrrpStatsChecksumErrors_Object((1,3,6,1,4,1,272,4,40,2,1,12),_BiboBrrpStatsChecksumErrors_Type())
biboBrrpStatsChecksumErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:biboBrrpStatsChecksumErrors.setStatus(_A)
_BiboBrrpStatsVersionErrors_Type=Counter32
_BiboBrrpStatsVersionErrors_Object=MibTableColumn
biboBrrpStatsVersionErrors=_BiboBrrpStatsVersionErrors_Object((1,3,6,1,4,1,272,4,40,2,1,13),_BiboBrrpStatsVersionErrors_Type())
biboBrrpStatsVersionErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:biboBrrpStatsVersionErrors.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'bintec':bintec,'bibo':bibo,'brrp':brrp,'biboBrrpOperTable':biboBrrpOperTable,'biboBrrpOperEntry':biboBrrpOperEntry,_H:biboBrrpOperVrId,_G:biboBrrpVirtIfIndex,'biboBrrpOperMasterIpAddr':biboBrrpOperMasterIpAddr,'biboBrrpOperState':biboBrrpOperState,'biboBrrpOperAdminState':biboBrrpOperAdminState,'biboBrrpOperPriority':biboBrrpOperPriority,'biboBrrpOperAuthType':biboBrrpOperAuthType,'biboBrrpOperAuthKey':biboBrrpOperAuthKey,'biboBrrpOperAdvertisementInterval':biboBrrpOperAdvertisementInterval,'biboBrrpOperMasterDownRetries':biboBrrpOperMasterDownRetries,'biboBrrpOperPreemptMode':biboBrrpOperPreemptMode,'biboBrrpOperVirtualRouterUpTime':biboBrrpOperVirtualRouterUpTime,'biboBrrpMasterIfIndex':biboBrrpMasterIfIndex,'biboBrrpOperDecrPrio':biboBrrpOperDecrPrio,'biboBrrpRouterStatsTable':biboBrrpRouterStatsTable,'biboBrrpRouterStatsEntry':biboBrrpRouterStatsEntry,_J:biboBrrpStatsVrId,_I:biboBrrpStatsIfIndex,'biboBrrpStatsBecomeMaster':biboBrrpStatsBecomeMaster,'biboBrrpStatsAdvertiseRcvd':biboBrrpStatsAdvertiseRcvd,'biboBrrpStatsAdvertiseIntervalErrors':biboBrrpStatsAdvertiseIntervalErrors,'biboBrrpStatsAuthFailures':biboBrrpStatsAuthFailures,'biboBrrpStatsIpTtlErrors':biboBrrpStatsIpTtlErrors,'biboBrrpStatsInvalidTypePktsRcvd':biboBrrpStatsInvalidTypePktsRcvd,'biboBrrpStatsInvalidAuthType':biboBrrpStatsInvalidAuthType,'biboBrrpStatsAuthTypeMismatch':biboBrrpStatsAuthTypeMismatch,'biboBrrpStatsPacketLengthErrors':biboBrrpStatsPacketLengthErrors,'biboBrrpStatsChecksumErrors':biboBrrpStatsChecksumErrors,'biboBrrpStatsVersionErrors':biboBrrpStatsVersionErrors})