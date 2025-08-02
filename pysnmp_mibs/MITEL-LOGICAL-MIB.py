_L='mitelWanRetryThreshold'
_K='mitelLogWanPortTblStatus'
_J='mitelLogWanPortTblIndex'
_I='disabled'
_H='OctetString'
_G='mitelLogicalTblIndex'
_F='DisplayString'
_E='read-only'
_D='MITEL-LOGICAL-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention')
mitelRouterLogicalGroup=ModuleIdentity((1,3,6,1,4,1,1027,4,8,1,4))
if mibBuilder.loadTexts:mitelRouterLogicalGroup.setRevisions(('2003-03-24 09:47','1999-03-01 00:00'))
_Mitel_ObjectIdentity=ObjectIdentity
mitel=_Mitel_ObjectIdentity((1,3,6,1,4,1,1027))
_MitelIdentification_ObjectIdentity=ObjectIdentity
mitelIdentification=_MitelIdentification_ObjectIdentity((1,3,6,1,4,1,1027,1))
_MitelIdCallServers_ObjectIdentity=ObjectIdentity
mitelIdCallServers=_MitelIdCallServers_ObjectIdentity((1,3,6,1,4,1,1027,1,2))
_MitelIdCsIpera1000_ObjectIdentity=ObjectIdentity
mitelIdCsIpera1000=_MitelIdCsIpera1000_ObjectIdentity((1,3,6,1,4,1,1027,1,2,4))
_MitelProprietary_ObjectIdentity=ObjectIdentity
mitelProprietary=_MitelProprietary_ObjectIdentity((1,3,6,1,4,1,1027,4))
_MitelPropIpNetworking_ObjectIdentity=ObjectIdentity
mitelPropIpNetworking=_MitelPropIpNetworking_ObjectIdentity((1,3,6,1,4,1,1027,4,8))
_MitelIpNetRouter_ObjectIdentity=ObjectIdentity
mitelIpNetRouter=_MitelIpNetRouter_ObjectIdentity((1,3,6,1,4,1,1027,4,8,1))
_MitelLogGrpLogicalTable_Object=MibTable
mitelLogGrpLogicalTable=_MitelLogGrpLogicalTable_Object((1,3,6,1,4,1,1027,4,8,1,4,1))
if mibBuilder.loadTexts:mitelLogGrpLogicalTable.setStatus(_A)
_MitelLogGrpLogicalEntry_Object=MibTableRow
mitelLogGrpLogicalEntry=_MitelLogGrpLogicalEntry_Object((1,3,6,1,4,1,1027,4,8,1,4,1,1))
mitelLogGrpLogicalEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:mitelLogGrpLogicalEntry.setStatus(_A)
_MitelLogicalTblIndex_Type=Integer32
_MitelLogicalTblIndex_Object=MibTableColumn
mitelLogicalTblIndex=_MitelLogicalTblIndex_Object((1,3,6,1,4,1,1027,4,8,1,4,1,1,1),_MitelLogicalTblIndex_Type())
mitelLogicalTblIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:mitelLogicalTblIndex.setStatus(_A)
class _MitelLogicalTblDestName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_MitelLogicalTblDestName_Type.__name__=_F
_MitelLogicalTblDestName_Object=MibTableColumn
mitelLogicalTblDestName=_MitelLogicalTblDestName_Object((1,3,6,1,4,1,1027,4,8,1,4,1,1,2),_MitelLogicalTblDestName_Type())
mitelLogicalTblDestName.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelLogicalTblDestName.setStatus(_A)
class _MitelLogicalTblType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),('remote',2)))
_MitelLogicalTblType_Type.__name__=_B
_MitelLogicalTblType_Object=MibTableColumn
mitelLogicalTblType=_MitelLogicalTblType_Object((1,3,6,1,4,1,1027,4,8,1,4,1,1,3),_MitelLogicalTblType_Type())
mitelLogicalTblType.setMaxAccess(_E)
if mibBuilder.loadTexts:mitelLogicalTblType.setStatus(_A)
class _MitelLogicalTblAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_MitelLogicalTblAdminStatus_Type.__name__=_B
_MitelLogicalTblAdminStatus_Object=MibTableColumn
mitelLogicalTblAdminStatus=_MitelLogicalTblAdminStatus_Object((1,3,6,1,4,1,1027,4,8,1,4,1,1,4),_MitelLogicalTblAdminStatus_Type())
mitelLogicalTblAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelLogicalTblAdminStatus.setStatus(_A)
_MitelLogGrpLogicalWanTable_Object=MibTable
mitelLogGrpLogicalWanTable=_MitelLogGrpLogicalWanTable_Object((1,3,6,1,4,1,1027,4,8,1,4,2))
if mibBuilder.loadTexts:mitelLogGrpLogicalWanTable.setStatus(_A)
_MitelLogGrpLogicalWanEntry_Object=MibTableRow
mitelLogGrpLogicalWanEntry=_MitelLogGrpLogicalWanEntry_Object((1,3,6,1,4,1,1027,4,8,1,4,2,1))
mitelLogGrpLogicalWanEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:mitelLogGrpLogicalWanEntry.setStatus(_A)
class _MitelLogWanTblCmprsn_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('any',2),('gandalf',3),('stac',4)))
_MitelLogWanTblCmprsn_Type.__name__=_B
_MitelLogWanTblCmprsn_Object=MibTableColumn
mitelLogWanTblCmprsn=_MitelLogWanTblCmprsn_Object((1,3,6,1,4,1,1027,4,8,1,4,2,1,1),_MitelLogWanTblCmprsn_Type())
mitelLogWanTblCmprsn.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelLogWanTblCmprsn.setStatus(_A)
class _MitelLogWanTblCmprsnStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('none',1),('fza',2),('fzap',3),('concryption',4),('encryption',5),('stacNoCheckMode',6),('stacLCBCheckMode',7),('stacCRCCheckMode',8),('stacSeqNumbers',9),('stacExtendedMode',10),('stacAscendLCBMode',11)))
_MitelLogWanTblCmprsnStatus_Type.__name__=_B
_MitelLogWanTblCmprsnStatus_Object=MibTableColumn
mitelLogWanTblCmprsnStatus=_MitelLogWanTblCmprsnStatus_Object((1,3,6,1,4,1,1027,4,8,1,4,2,1,2),_MitelLogWanTblCmprsnStatus_Type())
mitelLogWanTblCmprsnStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:mitelLogWanTblCmprsnStatus.setStatus(_A)
class _MitelLogWanTblEncryptn_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),(_I,2)))
_MitelLogWanTblEncryptn_Type.__name__=_B
_MitelLogWanTblEncryptn_Object=MibTableColumn
mitelLogWanTblEncryptn=_MitelLogWanTblEncryptn_Object((1,3,6,1,4,1,1027,4,8,1,4,2,1,3),_MitelLogWanTblEncryptn_Type())
mitelLogWanTblEncryptn.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelLogWanTblEncryptn.setStatus(_A)
class _MitelLogWanTblBackupOvrflow_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),('backup',2),('overflow',3)))
_MitelLogWanTblBackupOvrflow_Type.__name__=_B
_MitelLogWanTblBackupOvrflow_Object=MibTableColumn
mitelLogWanTblBackupOvrflow=_MitelLogWanTblBackupOvrflow_Object((1,3,6,1,4,1,1027,4,8,1,4,2,1,4),_MitelLogWanTblBackupOvrflow_Type())
mitelLogWanTblBackupOvrflow.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelLogWanTblBackupOvrflow.setStatus(_A)
class _MitelLogWanTblThshld_Type(Integer32):defaultValue=80;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_MitelLogWanTblThshld_Type.__name__=_B
_MitelLogWanTblThshld_Object=MibTableColumn
mitelLogWanTblThshld=_MitelLogWanTblThshld_Object((1,3,6,1,4,1,1027,4,8,1,4,2,1,5),_MitelLogWanTblThshld_Type())
mitelLogWanTblThshld.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelLogWanTblThshld.setStatus(_A)
class _MitelLogWanTblConnTimer_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_MitelLogWanTblConnTimer_Type.__name__=_B
_MitelLogWanTblConnTimer_Object=MibTableColumn
mitelLogWanTblConnTimer=_MitelLogWanTblConnTimer_Object((1,3,6,1,4,1,1027,4,8,1,4,2,1,6),_MitelLogWanTblConnTimer_Type())
mitelLogWanTblConnTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelLogWanTblConnTimer.setStatus(_A)
class _MitelLogWanTblDiscTimer_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_MitelLogWanTblDiscTimer_Type.__name__=_B
_MitelLogWanTblDiscTimer_Object=MibTableColumn
mitelLogWanTblDiscTimer=_MitelLogWanTblDiscTimer_Object((1,3,6,1,4,1,1027,4,8,1,4,2,1,7),_MitelLogWanTblDiscTimer_Type())
mitelLogWanTblDiscTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelLogWanTblDiscTimer.setStatus(_A)
class _MitelLogWanTblProtocolType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ppp',1),('framerelay',2),('x25',3)))
_MitelLogWanTblProtocolType_Type.__name__=_B
_MitelLogWanTblProtocolType_Object=MibTableColumn
mitelLogWanTblProtocolType=_MitelLogWanTblProtocolType_Object((1,3,6,1,4,1,1027,4,8,1,4,2,1,8),_MitelLogWanTblProtocolType_Type())
mitelLogWanTblProtocolType.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelLogWanTblProtocolType.setStatus(_A)
_MitelLogGrpLogicalWanPortTable_Object=MibTable
mitelLogGrpLogicalWanPortTable=_MitelLogGrpLogicalWanPortTable_Object((1,3,6,1,4,1,1027,4,8,1,4,3))
if mibBuilder.loadTexts:mitelLogGrpLogicalWanPortTable.setStatus(_A)
_MitelLogGrpLogicalWanPortEntry_Object=MibTableRow
mitelLogGrpLogicalWanPortEntry=_MitelLogGrpLogicalWanPortEntry_Object((1,3,6,1,4,1,1027,4,8,1,4,3,1))
mitelLogGrpLogicalWanPortEntry.setIndexNames((0,_D,_G),(0,_D,_J))
if mibBuilder.loadTexts:mitelLogGrpLogicalWanPortEntry.setStatus(_A)
_MitelLogWanPortTblIndex_Type=Integer32
_MitelLogWanPortTblIndex_Object=MibTableColumn
mitelLogWanPortTblIndex=_MitelLogWanPortTblIndex_Object((1,3,6,1,4,1,1027,4,8,1,4,3,1,1),_MitelLogWanPortTblIndex_Type())
mitelLogWanPortTblIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:mitelLogWanPortTblIndex.setStatus(_A)
class _MitelLogWanPortTblWanType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('permanent',1),('ondemand',2),('incomming',3),('outgoing',4)))
_MitelLogWanPortTblWanType_Type.__name__=_B
_MitelLogWanPortTblWanType_Object=MibTableColumn
mitelLogWanPortTblWanType=_MitelLogWanPortTblWanType_Object((1,3,6,1,4,1,1027,4,8,1,4,3,1,2),_MitelLogWanPortTblWanType_Type())
mitelLogWanPortTblWanType.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelLogWanPortTblWanType.setStatus(_A)
class _MitelLogWanPortTblTransType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('hdlc',1),('modem',2),('ethernet',3)))
_MitelLogWanPortTblTransType_Type.__name__=_B
_MitelLogWanPortTblTransType_Object=MibTableColumn
mitelLogWanPortTblTransType=_MitelLogWanPortTblTransType_Object((1,3,6,1,4,1,1027,4,8,1,4,3,1,3),_MitelLogWanPortTblTransType_Type())
mitelLogWanPortTblTransType.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelLogWanPortTblTransType.setStatus(_A)
class _MitelLogWanPortTblRetry_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_MitelLogWanPortTblRetry_Type.__name__=_B
_MitelLogWanPortTblRetry_Object=MibTableColumn
mitelLogWanPortTblRetry=_MitelLogWanPortTblRetry_Object((1,3,6,1,4,1,1027,4,8,1,4,3,1,4),_MitelLogWanPortTblRetry_Type())
mitelLogWanPortTblRetry.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelLogWanPortTblRetry.setStatus(_A)
class _MitelLogWanPortTblRetryPeriod_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_MitelLogWanPortTblRetryPeriod_Type.__name__=_B
_MitelLogWanPortTblRetryPeriod_Object=MibTableColumn
mitelLogWanPortTblRetryPeriod=_MitelLogWanPortTblRetryPeriod_Object((1,3,6,1,4,1,1027,4,8,1,4,3,1,5),_MitelLogWanPortTblRetryPeriod_Type())
mitelLogWanPortTblRetryPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelLogWanPortTblRetryPeriod.setStatus(_A)
class _MitelLogWanPortTblPrepend_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_MitelLogWanPortTblPrepend_Type.__name__=_H
_MitelLogWanPortTblPrepend_Object=MibTableColumn
mitelLogWanPortTblPrepend=_MitelLogWanPortTblPrepend_Object((1,3,6,1,4,1,1027,4,8,1,4,3,1,6),_MitelLogWanPortTblPrepend_Type())
mitelLogWanPortTblPrepend.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelLogWanPortTblPrepend.setStatus(_A)
class _MitelLogWanPortTblDestAddr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_MitelLogWanPortTblDestAddr_Type.__name__=_F
_MitelLogWanPortTblDestAddr_Object=MibTableColumn
mitelLogWanPortTblDestAddr=_MitelLogWanPortTblDestAddr_Object((1,3,6,1,4,1,1027,4,8,1,4,3,1,7),_MitelLogWanPortTblDestAddr_Type())
mitelLogWanPortTblDestAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelLogWanPortTblDestAddr.setStatus(_A)
class _MitelLogWanPortTblNextDestAddr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_MitelLogWanPortTblNextDestAddr_Type.__name__=_F
_MitelLogWanPortTblNextDestAddr_Object=MibTableColumn
mitelLogWanPortTblNextDestAddr=_MitelLogWanPortTblNextDestAddr_Object((1,3,6,1,4,1,1027,4,8,1,4,3,1,8),_MitelLogWanPortTblNextDestAddr_Type())
mitelLogWanPortTblNextDestAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelLogWanPortTblNextDestAddr.setStatus(_A)
class _MitelLogWanPortTblChId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MitelLogWanPortTblChId_Type.__name__=_B
_MitelLogWanPortTblChId_Object=MibTableColumn
mitelLogWanPortTblChId=_MitelLogWanPortTblChId_Object((1,3,6,1,4,1,1027,4,8,1,4,3,1,9),_MitelLogWanPortTblChId_Type())
mitelLogWanPortTblChId.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelLogWanPortTblChId.setStatus(_A)
class _MitelLogWanPortTblDialback_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_MitelLogWanPortTblDialback_Type.__name__=_B
_MitelLogWanPortTblDialback_Object=MibTableColumn
mitelLogWanPortTblDialback=_MitelLogWanPortTblDialback_Object((1,3,6,1,4,1,1027,4,8,1,4,3,1,10),_MitelLogWanPortTblDialback_Type())
mitelLogWanPortTblDialback.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelLogWanPortTblDialback.setStatus(_A)
class _MitelLogWanPortTblAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_MitelLogWanPortTblAdminStatus_Type.__name__=_B
_MitelLogWanPortTblAdminStatus_Object=MibTableColumn
mitelLogWanPortTblAdminStatus=_MitelLogWanPortTblAdminStatus_Object((1,3,6,1,4,1,1027,4,8,1,4,3,1,11),_MitelLogWanPortTblAdminStatus_Type())
mitelLogWanPortTblAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelLogWanPortTblAdminStatus.setStatus(_A)
class _MitelLogWanPortTblOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('connecting',1),('connected',2),('disconnecting',3),('disconnected',4),('retryExhausted',5)))
_MitelLogWanPortTblOperStatus_Type.__name__=_B
_MitelLogWanPortTblOperStatus_Object=MibTableColumn
mitelLogWanPortTblOperStatus=_MitelLogWanPortTblOperStatus_Object((1,3,6,1,4,1,1027,4,8,1,4,3,1,12),_MitelLogWanPortTblOperStatus_Type())
mitelLogWanPortTblOperStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:mitelLogWanPortTblOperStatus.setStatus(_A)
_MitelLogWanPortTblStatus_Type=RowStatus
_MitelLogWanPortTblStatus_Object=MibTableColumn
mitelLogWanPortTblStatus=_MitelLogWanPortTblStatus_Object((1,3,6,1,4,1,1027,4,8,1,4,3,1,13),_MitelLogWanPortTblStatus_Type())
mitelLogWanPortTblStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:mitelLogWanPortTblStatus.setStatus(_A)
mitelWanRetryThreshold=NotificationType((1,3,6,1,4,1,1027,1,2,4,0,403))
mitelWanRetryThreshold.setObjects((_D,_K))
if mibBuilder.loadTexts:mitelWanRetryThreshold.setStatus(_A)
mitelIpera1000Notifications=NotificationGroup((1,3,6,1,4,1,1027,1,2,4,0))
mitelIpera1000Notifications.setObjects((_D,_L))
if mibBuilder.loadTexts:mitelIpera1000Notifications.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'mitel':mitel,'mitelIdentification':mitelIdentification,'mitelIdCallServers':mitelIdCallServers,'mitelIdCsIpera1000':mitelIdCsIpera1000,'mitelIpera1000Notifications':mitelIpera1000Notifications,_L:mitelWanRetryThreshold,'mitelProprietary':mitelProprietary,'mitelPropIpNetworking':mitelPropIpNetworking,'mitelIpNetRouter':mitelIpNetRouter,'mitelRouterLogicalGroup':mitelRouterLogicalGroup,'mitelLogGrpLogicalTable':mitelLogGrpLogicalTable,'mitelLogGrpLogicalEntry':mitelLogGrpLogicalEntry,_G:mitelLogicalTblIndex,'mitelLogicalTblDestName':mitelLogicalTblDestName,'mitelLogicalTblType':mitelLogicalTblType,'mitelLogicalTblAdminStatus':mitelLogicalTblAdminStatus,'mitelLogGrpLogicalWanTable':mitelLogGrpLogicalWanTable,'mitelLogGrpLogicalWanEntry':mitelLogGrpLogicalWanEntry,'mitelLogWanTblCmprsn':mitelLogWanTblCmprsn,'mitelLogWanTblCmprsnStatus':mitelLogWanTblCmprsnStatus,'mitelLogWanTblEncryptn':mitelLogWanTblEncryptn,'mitelLogWanTblBackupOvrflow':mitelLogWanTblBackupOvrflow,'mitelLogWanTblThshld':mitelLogWanTblThshld,'mitelLogWanTblConnTimer':mitelLogWanTblConnTimer,'mitelLogWanTblDiscTimer':mitelLogWanTblDiscTimer,'mitelLogWanTblProtocolType':mitelLogWanTblProtocolType,'mitelLogGrpLogicalWanPortTable':mitelLogGrpLogicalWanPortTable,'mitelLogGrpLogicalWanPortEntry':mitelLogGrpLogicalWanPortEntry,_J:mitelLogWanPortTblIndex,'mitelLogWanPortTblWanType':mitelLogWanPortTblWanType,'mitelLogWanPortTblTransType':mitelLogWanPortTblTransType,'mitelLogWanPortTblRetry':mitelLogWanPortTblRetry,'mitelLogWanPortTblRetryPeriod':mitelLogWanPortTblRetryPeriod,'mitelLogWanPortTblPrepend':mitelLogWanPortTblPrepend,'mitelLogWanPortTblDestAddr':mitelLogWanPortTblDestAddr,'mitelLogWanPortTblNextDestAddr':mitelLogWanPortTblNextDestAddr,'mitelLogWanPortTblChId':mitelLogWanPortTblChId,'mitelLogWanPortTblDialback':mitelLogWanPortTblDialback,'mitelLogWanPortTblAdminStatus':mitelLogWanPortTblAdminStatus,'mitelLogWanPortTblOperStatus':mitelLogWanPortTblOperStatus,_K:mitelLogWanPortTblStatus})