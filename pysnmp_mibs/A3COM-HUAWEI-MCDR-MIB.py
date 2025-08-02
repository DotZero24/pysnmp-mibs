_H='h3cMultUserRecordID'
_G='A3COM-HUAWEI-MCDR-MIB'
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
h3cCommon,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cCommon')
ifIndex,=mibBuilder.importSymbols(_E,_F)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
h3cMultCDR=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,86))
if mibBuilder.loadTexts:h3cMultCDR.setRevisions(('2007-12-15 00:00',))
_H3cMultCDRCfgObject_ObjectIdentity=ObjectIdentity
h3cMultCDRCfgObject=_H3cMultCDRCfgObject_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,86,1))
class _H3cMultCDRStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_H3cMultCDRStatus_Type.__name__=_C
_H3cMultCDRStatus_Object=MibScalar
h3cMultCDRStatus=_H3cMultCDRStatus_Object((1,3,6,1,4,1,43,45,1,10,2,86,1,1),_H3cMultCDRStatus_Type())
h3cMultCDRStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cMultCDRStatus.setStatus(_A)
class _H3cMultCDRReportInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,600))
_H3cMultCDRReportInterval_Type.__name__=_C
_H3cMultCDRReportInterval_Object=MibScalar
h3cMultCDRReportInterval=_H3cMultCDRReportInterval_Object((1,3,6,1,4,1,43,45,1,10,2,86,1,2),_H3cMultCDRReportInterval_Type())
h3cMultCDRReportInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cMultCDRReportInterval.setStatus(_A)
class _H3cMultCDRCacheLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,1024))
_H3cMultCDRCacheLimit_Type.__name__=_C
_H3cMultCDRCacheLimit_Object=MibScalar
h3cMultCDRCacheLimit=_H3cMultCDRCacheLimit_Object((1,3,6,1,4,1,43,45,1,10,2,86,1,3),_H3cMultCDRCacheLimit_Type())
h3cMultCDRCacheLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cMultCDRCacheLimit.setStatus(_A)
class _H3cMultCDRRecordDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,600))
_H3cMultCDRRecordDelay_Type.__name__=_C
_H3cMultCDRRecordDelay_Object=MibScalar
h3cMultCDRRecordDelay=_H3cMultCDRRecordDelay_Object((1,3,6,1,4,1,43,45,1,10,2,86,1,4),_H3cMultCDRRecordDelay_Type())
h3cMultCDRRecordDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cMultCDRRecordDelay.setStatus(_A)
class _H3cMultCDRRecordSend_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('send',1),('caching',2)))
_H3cMultCDRRecordSend_Type.__name__=_C
_H3cMultCDRRecordSend_Object=MibScalar
h3cMultCDRRecordSend=_H3cMultCDRRecordSend_Object((1,3,6,1,4,1,43,45,1,10,2,86,1,5),_H3cMultCDRRecordSend_Type())
h3cMultCDRRecordSend.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cMultCDRRecordSend.setStatus(_A)
_H3cMultUserOnlineInfoTable_Object=MibTable
h3cMultUserOnlineInfoTable=_H3cMultUserOnlineInfoTable_Object((1,3,6,1,4,1,43,45,1,10,2,86,2))
if mibBuilder.loadTexts:h3cMultUserOnlineInfoTable.setStatus(_A)
_H3cMultUserOnlineInfoEntry_Object=MibTableRow
h3cMultUserOnlineInfoEntry=_H3cMultUserOnlineInfoEntry_Object((1,3,6,1,4,1,43,45,1,10,2,86,2,1))
h3cMultUserOnlineInfoEntry.setIndexNames((0,_E,_F),(0,_G,_H))
if mibBuilder.loadTexts:h3cMultUserOnlineInfoEntry.setStatus(_A)
_H3cMultUserRecordID_Type=Unsigned32
_H3cMultUserRecordID_Object=MibTableColumn
h3cMultUserRecordID=_H3cMultUserRecordID_Object((1,3,6,1,4,1,43,45,1,10,2,86,2,1,1),_H3cMultUserRecordID_Type())
h3cMultUserRecordID.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:h3cMultUserRecordID.setStatus(_A)
_H3cMultUserSubIfIndex_Type=Unsigned32
_H3cMultUserSubIfIndex_Object=MibTableColumn
h3cMultUserSubIfIndex=_H3cMultUserSubIfIndex_Object((1,3,6,1,4,1,43,45,1,10,2,86,2,1,2),_H3cMultUserSubIfIndex_Type())
h3cMultUserSubIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMultUserSubIfIndex.setStatus(_A)
_H3cMultUserVlanID_Type=VlanId
_H3cMultUserVlanID_Object=MibTableColumn
h3cMultUserVlanID=_H3cMultUserVlanID_Object((1,3,6,1,4,1,43,45,1,10,2,86,2,1,3),_H3cMultUserVlanID_Type())
h3cMultUserVlanID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMultUserVlanID.setStatus(_A)
_H3cMultUserJoinGAddrType_Type=InetAddressType
_H3cMultUserJoinGAddrType_Object=MibTableColumn
h3cMultUserJoinGAddrType=_H3cMultUserJoinGAddrType_Object((1,3,6,1,4,1,43,45,1,10,2,86,2,1,4),_H3cMultUserJoinGAddrType_Type())
h3cMultUserJoinGAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMultUserJoinGAddrType.setStatus(_A)
_H3cMultUserJoinGAddr_Type=InetAddress
_H3cMultUserJoinGAddr_Object=MibTableColumn
h3cMultUserJoinGAddr=_H3cMultUserJoinGAddr_Object((1,3,6,1,4,1,43,45,1,10,2,86,2,1,5),_H3cMultUserJoinGAddr_Type())
h3cMultUserJoinGAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMultUserJoinGAddr.setStatus(_A)
_H3cMultUserJoinSAddrType_Type=InetAddressType
_H3cMultUserJoinSAddrType_Object=MibTableColumn
h3cMultUserJoinSAddrType=_H3cMultUserJoinSAddrType_Object((1,3,6,1,4,1,43,45,1,10,2,86,2,1,6),_H3cMultUserJoinSAddrType_Type())
h3cMultUserJoinSAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMultUserJoinSAddrType.setStatus(_A)
_H3cMultUserJoinSAddr_Type=InetAddress
_H3cMultUserJoinSAddr_Object=MibTableColumn
h3cMultUserJoinSAddr=_H3cMultUserJoinSAddr_Object((1,3,6,1,4,1,43,45,1,10,2,86,2,1,7),_H3cMultUserJoinSAddr_Type())
h3cMultUserJoinSAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMultUserJoinSAddr.setStatus(_A)
class _H3cMultUserStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('permit',1),('preview',2)))
_H3cMultUserStatus_Type.__name__=_C
_H3cMultUserStatus_Object=MibTableColumn
h3cMultUserStatus=_H3cMultUserStatus_Object((1,3,6,1,4,1,43,45,1,10,2,86,2,1,8),_H3cMultUserStatus_Type())
h3cMultUserStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMultUserStatus.setStatus(_A)
_H3cMultUserJoinTime_Type=DateAndTime
_H3cMultUserJoinTime_Object=MibTableColumn
h3cMultUserJoinTime=_H3cMultUserJoinTime_Object((1,3,6,1,4,1,43,45,1,10,2,86,2,1,9),_H3cMultUserJoinTime_Type())
h3cMultUserJoinTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMultUserJoinTime.setStatus(_A)
_H3cMultUserPreviewTimes_Type=Unsigned32
_H3cMultUserPreviewTimes_Object=MibTableColumn
h3cMultUserPreviewTimes=_H3cMultUserPreviewTimes_Object((1,3,6,1,4,1,43,45,1,10,2,86,2,1,10),_H3cMultUserPreviewTimes_Type())
h3cMultUserPreviewTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMultUserPreviewTimes.setStatus(_A)
_H3cMultUserPreviewRemain_Type=Unsigned32
_H3cMultUserPreviewRemain_Object=MibTableColumn
h3cMultUserPreviewRemain=_H3cMultUserPreviewRemain_Object((1,3,6,1,4,1,43,45,1,10,2,86,2,1,11),_H3cMultUserPreviewRemain_Type())
h3cMultUserPreviewRemain.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMultUserPreviewRemain.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'h3cMultCDR':h3cMultCDR,'h3cMultCDRCfgObject':h3cMultCDRCfgObject,'h3cMultCDRStatus':h3cMultCDRStatus,'h3cMultCDRReportInterval':h3cMultCDRReportInterval,'h3cMultCDRCacheLimit':h3cMultCDRCacheLimit,'h3cMultCDRRecordDelay':h3cMultCDRRecordDelay,'h3cMultCDRRecordSend':h3cMultCDRRecordSend,'h3cMultUserOnlineInfoTable':h3cMultUserOnlineInfoTable,'h3cMultUserOnlineInfoEntry':h3cMultUserOnlineInfoEntry,_H:h3cMultUserRecordID,'h3cMultUserSubIfIndex':h3cMultUserSubIfIndex,'h3cMultUserVlanID':h3cMultUserVlanID,'h3cMultUserJoinGAddrType':h3cMultUserJoinGAddrType,'h3cMultUserJoinGAddr':h3cMultUserJoinGAddr,'h3cMultUserJoinSAddrType':h3cMultUserJoinSAddrType,'h3cMultUserJoinSAddr':h3cMultUserJoinSAddr,'h3cMultUserStatus':h3cMultUserStatus,'h3cMultUserJoinTime':h3cMultUserJoinTime,'h3cMultUserPreviewTimes':h3cMultUserPreviewTimes,'h3cMultUserPreviewRemain':h3cMultUserPreviewRemain})