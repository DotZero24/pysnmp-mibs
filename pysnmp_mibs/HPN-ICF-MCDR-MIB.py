_H='hpnicfMultUserRecordID'
_G='HPN-ICF-MCDR-MIB'
_F='ifIndex'
_E='IF-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ifIndex,=mibBuilder.importSymbols(_E,_F)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
hpnicfMultCDR=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,86))
if mibBuilder.loadTexts:hpnicfMultCDR.setRevisions(('2007-12-15 00:00',))
_HpnicfMultCDRCfgObject_ObjectIdentity=ObjectIdentity
hpnicfMultCDRCfgObject=_HpnicfMultCDRCfgObject_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,86,1))
class _HpnicfMultCDRStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_HpnicfMultCDRStatus_Type.__name__=_C
_HpnicfMultCDRStatus_Object=MibScalar
hpnicfMultCDRStatus=_HpnicfMultCDRStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,86,1,1),_HpnicfMultCDRStatus_Type())
hpnicfMultCDRStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfMultCDRStatus.setStatus(_A)
class _HpnicfMultCDRReportInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,600))
_HpnicfMultCDRReportInterval_Type.__name__=_C
_HpnicfMultCDRReportInterval_Object=MibScalar
hpnicfMultCDRReportInterval=_HpnicfMultCDRReportInterval_Object((1,3,6,1,4,1,11,2,14,11,15,2,86,1,2),_HpnicfMultCDRReportInterval_Type())
hpnicfMultCDRReportInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfMultCDRReportInterval.setStatus(_A)
class _HpnicfMultCDRCacheLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,1024))
_HpnicfMultCDRCacheLimit_Type.__name__=_C
_HpnicfMultCDRCacheLimit_Object=MibScalar
hpnicfMultCDRCacheLimit=_HpnicfMultCDRCacheLimit_Object((1,3,6,1,4,1,11,2,14,11,15,2,86,1,3),_HpnicfMultCDRCacheLimit_Type())
hpnicfMultCDRCacheLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfMultCDRCacheLimit.setStatus(_A)
class _HpnicfMultCDRRecordDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,600))
_HpnicfMultCDRRecordDelay_Type.__name__=_C
_HpnicfMultCDRRecordDelay_Object=MibScalar
hpnicfMultCDRRecordDelay=_HpnicfMultCDRRecordDelay_Object((1,3,6,1,4,1,11,2,14,11,15,2,86,1,4),_HpnicfMultCDRRecordDelay_Type())
hpnicfMultCDRRecordDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfMultCDRRecordDelay.setStatus(_A)
class _HpnicfMultCDRRecordSend_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('send',1),('caching',2)))
_HpnicfMultCDRRecordSend_Type.__name__=_C
_HpnicfMultCDRRecordSend_Object=MibScalar
hpnicfMultCDRRecordSend=_HpnicfMultCDRRecordSend_Object((1,3,6,1,4,1,11,2,14,11,15,2,86,1,5),_HpnicfMultCDRRecordSend_Type())
hpnicfMultCDRRecordSend.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfMultCDRRecordSend.setStatus(_A)
_HpnicfMultUserOnlineInfoTable_Object=MibTable
hpnicfMultUserOnlineInfoTable=_HpnicfMultUserOnlineInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,86,2))
if mibBuilder.loadTexts:hpnicfMultUserOnlineInfoTable.setStatus(_A)
_HpnicfMultUserOnlineInfoEntry_Object=MibTableRow
hpnicfMultUserOnlineInfoEntry=_HpnicfMultUserOnlineInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,86,2,1))
hpnicfMultUserOnlineInfoEntry.setIndexNames((0,_E,_F),(0,_G,_H))
if mibBuilder.loadTexts:hpnicfMultUserOnlineInfoEntry.setStatus(_A)
_HpnicfMultUserRecordID_Type=Unsigned32
_HpnicfMultUserRecordID_Object=MibTableColumn
hpnicfMultUserRecordID=_HpnicfMultUserRecordID_Object((1,3,6,1,4,1,11,2,14,11,15,2,86,2,1,1),_HpnicfMultUserRecordID_Type())
hpnicfMultUserRecordID.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hpnicfMultUserRecordID.setStatus(_A)
_HpnicfMultUserSubIfIndex_Type=Unsigned32
_HpnicfMultUserSubIfIndex_Object=MibTableColumn
hpnicfMultUserSubIfIndex=_HpnicfMultUserSubIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,86,2,1,2),_HpnicfMultUserSubIfIndex_Type())
hpnicfMultUserSubIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMultUserSubIfIndex.setStatus(_A)
_HpnicfMultUserVlanID_Type=VlanId
_HpnicfMultUserVlanID_Object=MibTableColumn
hpnicfMultUserVlanID=_HpnicfMultUserVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,2,86,2,1,3),_HpnicfMultUserVlanID_Type())
hpnicfMultUserVlanID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMultUserVlanID.setStatus(_A)
_HpnicfMultUserJoinGAddrType_Type=InetAddressType
_HpnicfMultUserJoinGAddrType_Object=MibTableColumn
hpnicfMultUserJoinGAddrType=_HpnicfMultUserJoinGAddrType_Object((1,3,6,1,4,1,11,2,14,11,15,2,86,2,1,4),_HpnicfMultUserJoinGAddrType_Type())
hpnicfMultUserJoinGAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMultUserJoinGAddrType.setStatus(_A)
_HpnicfMultUserJoinGAddr_Type=InetAddress
_HpnicfMultUserJoinGAddr_Object=MibTableColumn
hpnicfMultUserJoinGAddr=_HpnicfMultUserJoinGAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,86,2,1,5),_HpnicfMultUserJoinGAddr_Type())
hpnicfMultUserJoinGAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMultUserJoinGAddr.setStatus(_A)
_HpnicfMultUserJoinSAddrType_Type=InetAddressType
_HpnicfMultUserJoinSAddrType_Object=MibTableColumn
hpnicfMultUserJoinSAddrType=_HpnicfMultUserJoinSAddrType_Object((1,3,6,1,4,1,11,2,14,11,15,2,86,2,1,6),_HpnicfMultUserJoinSAddrType_Type())
hpnicfMultUserJoinSAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMultUserJoinSAddrType.setStatus(_A)
_HpnicfMultUserJoinSAddr_Type=InetAddress
_HpnicfMultUserJoinSAddr_Object=MibTableColumn
hpnicfMultUserJoinSAddr=_HpnicfMultUserJoinSAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,86,2,1,7),_HpnicfMultUserJoinSAddr_Type())
hpnicfMultUserJoinSAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMultUserJoinSAddr.setStatus(_A)
class _HpnicfMultUserStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('permit',1),('preview',2)))
_HpnicfMultUserStatus_Type.__name__=_C
_HpnicfMultUserStatus_Object=MibTableColumn
hpnicfMultUserStatus=_HpnicfMultUserStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,86,2,1,8),_HpnicfMultUserStatus_Type())
hpnicfMultUserStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMultUserStatus.setStatus(_A)
_HpnicfMultUserJoinTime_Type=DateAndTime
_HpnicfMultUserJoinTime_Object=MibTableColumn
hpnicfMultUserJoinTime=_HpnicfMultUserJoinTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,86,2,1,9),_HpnicfMultUserJoinTime_Type())
hpnicfMultUserJoinTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMultUserJoinTime.setStatus(_A)
_HpnicfMultUserPreviewTimes_Type=Unsigned32
_HpnicfMultUserPreviewTimes_Object=MibTableColumn
hpnicfMultUserPreviewTimes=_HpnicfMultUserPreviewTimes_Object((1,3,6,1,4,1,11,2,14,11,15,2,86,2,1,10),_HpnicfMultUserPreviewTimes_Type())
hpnicfMultUserPreviewTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMultUserPreviewTimes.setStatus(_A)
_HpnicfMultUserPreviewRemain_Type=Unsigned32
_HpnicfMultUserPreviewRemain_Object=MibTableColumn
hpnicfMultUserPreviewRemain=_HpnicfMultUserPreviewRemain_Object((1,3,6,1,4,1,11,2,14,11,15,2,86,2,1,11),_HpnicfMultUserPreviewRemain_Type())
hpnicfMultUserPreviewRemain.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMultUserPreviewRemain.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'hpnicfMultCDR':hpnicfMultCDR,'hpnicfMultCDRCfgObject':hpnicfMultCDRCfgObject,'hpnicfMultCDRStatus':hpnicfMultCDRStatus,'hpnicfMultCDRReportInterval':hpnicfMultCDRReportInterval,'hpnicfMultCDRCacheLimit':hpnicfMultCDRCacheLimit,'hpnicfMultCDRRecordDelay':hpnicfMultCDRRecordDelay,'hpnicfMultCDRRecordSend':hpnicfMultCDRRecordSend,'hpnicfMultUserOnlineInfoTable':hpnicfMultUserOnlineInfoTable,'hpnicfMultUserOnlineInfoEntry':hpnicfMultUserOnlineInfoEntry,_H:hpnicfMultUserRecordID,'hpnicfMultUserSubIfIndex':hpnicfMultUserSubIfIndex,'hpnicfMultUserVlanID':hpnicfMultUserVlanID,'hpnicfMultUserJoinGAddrType':hpnicfMultUserJoinGAddrType,'hpnicfMultUserJoinGAddr':hpnicfMultUserJoinGAddr,'hpnicfMultUserJoinSAddrType':hpnicfMultUserJoinSAddrType,'hpnicfMultUserJoinSAddr':hpnicfMultUserJoinSAddr,'hpnicfMultUserStatus':hpnicfMultUserStatus,'hpnicfMultUserJoinTime':hpnicfMultUserJoinTime,'hpnicfMultUserPreviewTimes':hpnicfMultUserPreviewTimes,'hpnicfMultUserPreviewRemain':hpnicfMultUserPreviewRemain})