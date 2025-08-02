_H='read-create'
_G='smtpMailReceiverAddrIndex'
_F='SMTP-MIB'
_E='read-only'
_D='DisplayString'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','RowStatus','TextualConvention')
swSMTPMIB=ModuleIdentity((1,3,6,1,4,1,171,12,29))
class VlanId(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
class PortList(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_SwSMTPCtrl_ObjectIdentity=ObjectIdentity
swSMTPCtrl=_SwSMTPCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,29,1))
class _SmtpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('disabled',2),('enabled',3)))
_SmtpStatus_Type.__name__=_C
_SmtpStatus_Object=MibScalar
smtpStatus=_SmtpStatus_Object((1,3,6,1,4,1,171,12,29,1,1),_SmtpStatus_Type())
smtpStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:smtpStatus.setStatus(_A)
_SmtpSrvAddr_Type=IpAddress
_SmtpSrvAddr_Object=MibScalar
smtpSrvAddr=_SmtpSrvAddr_Object((1,3,6,1,4,1,171,12,29,1,2),_SmtpSrvAddr_Type())
smtpSrvAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:smtpSrvAddr.setStatus(_A)
class _SmtpSrvPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SmtpSrvPort_Type.__name__=_C
_SmtpSrvPort_Object=MibScalar
smtpSrvPort=_SmtpSrvPort_Object((1,3,6,1,4,1,171,12,29,1,3),_SmtpSrvPort_Type())
smtpSrvPort.setMaxAccess(_B)
if mibBuilder.loadTexts:smtpSrvPort.setStatus(_A)
class _SmtpSelfMailAddr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,254))
_SmtpSelfMailAddr_Type.__name__=_D
_SmtpSelfMailAddr_Object=MibScalar
smtpSelfMailAddr=_SmtpSelfMailAddr_Object((1,3,6,1,4,1,171,12,29,1,4),_SmtpSelfMailAddr_Type())
smtpSelfMailAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:smtpSelfMailAddr.setStatus(_A)
class _SmtpTestMsgSubject_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_SmtpTestMsgSubject_Type.__name__=_D
_SmtpTestMsgSubject_Object=MibScalar
smtpTestMsgSubject=_SmtpTestMsgSubject_Object((1,3,6,1,4,1,171,12,29,1,5),_SmtpTestMsgSubject_Type())
smtpTestMsgSubject.setMaxAccess(_B)
if mibBuilder.loadTexts:smtpTestMsgSubject.setStatus(_A)
class _SmtpTestMsgContent_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_SmtpTestMsgContent_Type.__name__=_D
_SmtpTestMsgContent_Object=MibScalar
smtpTestMsgContent=_SmtpTestMsgContent_Object((1,3,6,1,4,1,171,12,29,1,6),_SmtpTestMsgContent_Type())
smtpTestMsgContent.setMaxAccess(_B)
if mibBuilder.loadTexts:smtpTestMsgContent.setStatus(_A)
class _SmtpSendTestMsg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('send',1),('noAction',2)))
_SmtpSendTestMsg_Type.__name__=_C
_SmtpSendTestMsg_Object=MibScalar
smtpSendTestMsg=_SmtpSendTestMsg_Object((1,3,6,1,4,1,171,12,29,1,7),_SmtpSendTestMsg_Type())
smtpSendTestMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:smtpSendTestMsg.setStatus(_A)
_SwSMTPInfo_ObjectIdentity=ObjectIdentity
swSMTPInfo=_SwSMTPInfo_ObjectIdentity((1,3,6,1,4,1,171,12,29,2))
class _SmtpSendTestStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('success',1),('failed',2),('in-processing',3)))
_SmtpSendTestStatus_Type.__name__=_C
_SmtpSendTestStatus_Object=MibScalar
smtpSendTestStatus=_SmtpSendTestStatus_Object((1,3,6,1,4,1,171,12,29,2,1),_SmtpSendTestStatus_Type())
smtpSendTestStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:smtpSendTestStatus.setStatus(_A)
_SwSMTPMgmt_ObjectIdentity=ObjectIdentity
swSMTPMgmt=_SwSMTPMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,29,3))
_SmtpMailReceiverTable_Object=MibTable
smtpMailReceiverTable=_SmtpMailReceiverTable_Object((1,3,6,1,4,1,171,12,29,3,1))
if mibBuilder.loadTexts:smtpMailReceiverTable.setStatus(_A)
_SmtpReceiverAddrEntry_Object=MibTableRow
smtpReceiverAddrEntry=_SmtpReceiverAddrEntry_Object((1,3,6,1,4,1,171,12,29,3,1,1))
smtpReceiverAddrEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:smtpReceiverAddrEntry.setStatus(_A)
class _SmtpMailReceiverAddrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_SmtpMailReceiverAddrIndex_Type.__name__=_C
_SmtpMailReceiverAddrIndex_Object=MibTableColumn
smtpMailReceiverAddrIndex=_SmtpMailReceiverAddrIndex_Object((1,3,6,1,4,1,171,12,29,3,1,1,1),_SmtpMailReceiverAddrIndex_Type())
smtpMailReceiverAddrIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:smtpMailReceiverAddrIndex.setStatus(_A)
class _SmtpMailReceiverAddr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,254))
_SmtpMailReceiverAddr_Type.__name__=_D
_SmtpMailReceiverAddr_Object=MibTableColumn
smtpMailReceiverAddr=_SmtpMailReceiverAddr_Object((1,3,6,1,4,1,171,12,29,3,1,1,2),_SmtpMailReceiverAddr_Type())
smtpMailReceiverAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:smtpMailReceiverAddr.setStatus(_A)
_SmtpMailReceiverAddrState_Type=RowStatus
_SmtpMailReceiverAddrState_Object=MibTableColumn
smtpMailReceiverAddrState=_SmtpMailReceiverAddrState_Object((1,3,6,1,4,1,171,12,29,3,1,1,3),_SmtpMailReceiverAddrState_Type())
smtpMailReceiverAddrState.setMaxAccess(_H)
if mibBuilder.loadTexts:smtpMailReceiverAddrState.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'VlanId':VlanId,'PortList':PortList,'MacAddress':MacAddress,'swSMTPMIB':swSMTPMIB,'swSMTPCtrl':swSMTPCtrl,'smtpStatus':smtpStatus,'smtpSrvAddr':smtpSrvAddr,'smtpSrvPort':smtpSrvPort,'smtpSelfMailAddr':smtpSelfMailAddr,'smtpTestMsgSubject':smtpTestMsgSubject,'smtpTestMsgContent':smtpTestMsgContent,'smtpSendTestMsg':smtpSendTestMsg,'swSMTPInfo':swSMTPInfo,'smtpSendTestStatus':smtpSendTestStatus,'swSMTPMgmt':swSMTPMgmt,'smtpMailReceiverTable':smtpMailReceiverTable,'smtpReceiverAddrEntry':smtpReceiverAddrEntry,_G:smtpMailReceiverAddrIndex,'smtpMailReceiverAddr':smtpMailReceiverAddr,'smtpMailReceiverAddrState':smtpMailReceiverAddrState})