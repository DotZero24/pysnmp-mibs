_f='zxAnSyncTimeOutputPort'
_e='zxAnSyncTimeOutputSlot'
_d='zxAnSyncTimeOutputShelf'
_c='zxAnSyncTimeOutputRack'
_b='zxAnSyncTimeTodSrcPort'
_a='zxAnSyncTimeTodSrcSlot'
_Z='zxAnSyncTimeTodSrcShelf'
_Y='zxAnSyncTimeTodSrcRack'
_X='signalLos'
_W='normal'
_V='zxAnSyncTime1ppsSrcId'
_U='zxAnSyncTime1ppsSrcSlot'
_T='zxAnSyncTime1ppsSrcShelf'
_S='zxAnSyncTime1ppsSrcRack'
_R='standby'
_Q='active'
_P='zxAnPtpRemoteSrcIpAddress'
_O='zxAnPtpRemoteSrcIpAddrType'
_N='DisplayString'
_M='zxAnPtpId'
_L='zxAnPtpSlot'
_K='zxAnPtpShelf'
_J='zxAnPtpRack'
_I='TruthValue'
_H='InetAddressType'
_G='none'
_F='read-only'
_E='not-accessible'
_D='ZTE-AN-IEEE1588-MIB'
_C='read-create'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_H)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_N,'PhysAddress','RowStatus','TextualConvention',_I)
zxAn,=mibBuilder.importSymbols('ZTE-AN-TC-MIB','zxAn')
zxAnIeee1588Mib=ModuleIdentity((1,3,6,1,4,1,3902,1015,66))
_ZxAnPtpMgmt_ObjectIdentity=ObjectIdentity
zxAnPtpMgmt=_ZxAnPtpMgmt_ObjectIdentity((1,3,6,1,4,1,3902,1015,66,1))
_ZxAnPtpTable_Object=MibTable
zxAnPtpTable=_ZxAnPtpTable_Object((1,3,6,1,4,1,3902,1015,66,1,2))
if mibBuilder.loadTexts:zxAnPtpTable.setStatus(_A)
_ZxAnPtpEntry_Object=MibTableRow
zxAnPtpEntry=_ZxAnPtpEntry_Object((1,3,6,1,4,1,3902,1015,66,1,2,1))
zxAnPtpEntry.setIndexNames((0,_D,_J),(0,_D,_K),(0,_D,_L),(0,_D,_M))
if mibBuilder.loadTexts:zxAnPtpEntry.setStatus(_A)
_ZxAnPtpRack_Type=Integer32
_ZxAnPtpRack_Object=MibTableColumn
zxAnPtpRack=_ZxAnPtpRack_Object((1,3,6,1,4,1,3902,1015,66,1,2,1,1),_ZxAnPtpRack_Type())
zxAnPtpRack.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnPtpRack.setStatus(_A)
_ZxAnPtpShelf_Type=Integer32
_ZxAnPtpShelf_Object=MibTableColumn
zxAnPtpShelf=_ZxAnPtpShelf_Object((1,3,6,1,4,1,3902,1015,66,1,2,1,2),_ZxAnPtpShelf_Type())
zxAnPtpShelf.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnPtpShelf.setStatus(_A)
_ZxAnPtpSlot_Type=Integer32
_ZxAnPtpSlot_Object=MibTableColumn
zxAnPtpSlot=_ZxAnPtpSlot_Object((1,3,6,1,4,1,3902,1015,66,1,2,1,3),_ZxAnPtpSlot_Type())
zxAnPtpSlot.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnPtpSlot.setStatus(_A)
class _ZxAnPtpId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_ZxAnPtpId_Type.__name__=_B
_ZxAnPtpId_Object=MibTableColumn
zxAnPtpId=_ZxAnPtpId_Object((1,3,6,1,4,1,3902,1015,66,1,2,1,4),_ZxAnPtpId_Type())
zxAnPtpId.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnPtpId.setStatus(_A)
class _ZxAnPtpClockType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ordinary',1),('boundary',2)))
_ZxAnPtpClockType_Type.__name__=_B
_ZxAnPtpClockType_Object=MibTableColumn
zxAnPtpClockType=_ZxAnPtpClockType_Object((1,3,6,1,4,1,3902,1015,66,1,2,1,5),_ZxAnPtpClockType_Type())
zxAnPtpClockType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPtpClockType.setStatus(_A)
class _ZxAnPtpSlaveOnly_Type(TruthValue):defaultValue=1
_ZxAnPtpSlaveOnly_Type.__name__=_I
_ZxAnPtpSlaveOnly_Object=MibTableColumn
zxAnPtpSlaveOnly=_ZxAnPtpSlaveOnly_Object((1,3,6,1,4,1,3902,1015,66,1,2,1,6),_ZxAnPtpSlaveOnly_Type())
zxAnPtpSlaveOnly.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPtpSlaveOnly.setStatus(_A)
class _ZxAnPtpDomainNumber_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZxAnPtpDomainNumber_Type.__name__=_B
_ZxAnPtpDomainNumber_Object=MibTableColumn
zxAnPtpDomainNumber=_ZxAnPtpDomainNumber_Object((1,3,6,1,4,1,3902,1015,66,1,2,1,7),_ZxAnPtpDomainNumber_Type())
zxAnPtpDomainNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPtpDomainNumber.setStatus(_A)
class _ZxAnPtpProtocolIpAddrType_Type(InetAddressType):defaultValue=1
_ZxAnPtpProtocolIpAddrType_Type.__name__=_H
_ZxAnPtpProtocolIpAddrType_Object=MibTableColumn
zxAnPtpProtocolIpAddrType=_ZxAnPtpProtocolIpAddrType_Object((1,3,6,1,4,1,3902,1015,66,1,2,1,8),_ZxAnPtpProtocolIpAddrType_Type())
zxAnPtpProtocolIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPtpProtocolIpAddrType.setStatus(_A)
_ZxAnPtpProtocolIpAddress_Type=InetAddress
_ZxAnPtpProtocolIpAddress_Object=MibTableColumn
zxAnPtpProtocolIpAddress=_ZxAnPtpProtocolIpAddress_Object((1,3,6,1,4,1,3902,1015,66,1,2,1,9),_ZxAnPtpProtocolIpAddress_Type())
zxAnPtpProtocolIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPtpProtocolIpAddress.setStatus(_A)
class _ZxAnPtpEthWorkMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('syncE',1),('notSyncE',2)))
_ZxAnPtpEthWorkMode_Type.__name__=_B
_ZxAnPtpEthWorkMode_Object=MibTableColumn
zxAnPtpEthWorkMode=_ZxAnPtpEthWorkMode_Object((1,3,6,1,4,1,3902,1015,66,1,2,1,10),_ZxAnPtpEthWorkMode_Type())
zxAnPtpEthWorkMode.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPtpEthWorkMode.setStatus(_A)
class _ZxAnPtpPacketsMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unicast',1),('multicast',2),('broadcast',3)))
_ZxAnPtpPacketsMode_Type.__name__=_B
_ZxAnPtpPacketsMode_Object=MibTableColumn
zxAnPtpPacketsMode=_ZxAnPtpPacketsMode_Object((1,3,6,1,4,1,3902,1015,66,1,2,1,11),_ZxAnPtpPacketsMode_Type())
zxAnPtpPacketsMode.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPtpPacketsMode.setStatus(_A)
class _ZxAnPtpTwoStepFlag_Type(TruthValue):defaultValue=2
_ZxAnPtpTwoStepFlag_Type.__name__=_I
_ZxAnPtpTwoStepFlag_Object=MibTableColumn
zxAnPtpTwoStepFlag=_ZxAnPtpTwoStepFlag_Object((1,3,6,1,4,1,3902,1015,66,1,2,1,12),_ZxAnPtpTwoStepFlag_Type())
zxAnPtpTwoStepFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPtpTwoStepFlag.setStatus(_A)
class _ZxAnPtpSendPacketsRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_ZxAnPtpSendPacketsRate_Type.__name__=_B
_ZxAnPtpSendPacketsRate_Object=MibTableColumn
zxAnPtpSendPacketsRate=_ZxAnPtpSendPacketsRate_Object((1,3,6,1,4,1,3902,1015,66,1,2,1,13),_ZxAnPtpSendPacketsRate_Type())
zxAnPtpSendPacketsRate.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPtpSendPacketsRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnPtpSendPacketsRate.setUnits('pps')
class _ZxAnPtpClockStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('freeRun',1),('holdover',2),('acquisition',3),('locked',4)))
_ZxAnPtpClockStatus_Type.__name__=_B
_ZxAnPtpClockStatus_Object=MibTableColumn
zxAnPtpClockStatus=_ZxAnPtpClockStatus_Object((1,3,6,1,4,1,3902,1015,66,1,2,1,14),_ZxAnPtpClockStatus_Type())
zxAnPtpClockStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnPtpClockStatus.setStatus(_A)
class _ZxAnPtpUtcTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,19))
_ZxAnPtpUtcTime_Type.__name__=_N
_ZxAnPtpUtcTime_Object=MibTableColumn
zxAnPtpUtcTime=_ZxAnPtpUtcTime_Object((1,3,6,1,4,1,3902,1015,66,1,2,1,15),_ZxAnPtpUtcTime_Type())
zxAnPtpUtcTime.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnPtpUtcTime.setStatus(_A)
_ZxAnPtpRowStatus_Type=RowStatus
_ZxAnPtpRowStatus_Object=MibTableColumn
zxAnPtpRowStatus=_ZxAnPtpRowStatus_Object((1,3,6,1,4,1,3902,1015,66,1,2,1,50),_ZxAnPtpRowStatus_Type())
zxAnPtpRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPtpRowStatus.setStatus(_A)
_ZxAnPtpRemoteSrcTable_Object=MibTable
zxAnPtpRemoteSrcTable=_ZxAnPtpRemoteSrcTable_Object((1,3,6,1,4,1,3902,1015,66,1,3))
if mibBuilder.loadTexts:zxAnPtpRemoteSrcTable.setStatus(_A)
_ZxAnPtpRemoteSrcEntry_Object=MibTableRow
zxAnPtpRemoteSrcEntry=_ZxAnPtpRemoteSrcEntry_Object((1,3,6,1,4,1,3902,1015,66,1,3,1))
zxAnPtpRemoteSrcEntry.setIndexNames((0,_D,_J),(0,_D,_K),(0,_D,_L),(0,_D,_M),(0,_D,_O),(0,_D,_P))
if mibBuilder.loadTexts:zxAnPtpRemoteSrcEntry.setStatus(_A)
class _ZxAnPtpRemoteSrcIpAddrType_Type(InetAddressType):defaultValue=1
_ZxAnPtpRemoteSrcIpAddrType_Type.__name__=_H
_ZxAnPtpRemoteSrcIpAddrType_Object=MibTableColumn
zxAnPtpRemoteSrcIpAddrType=_ZxAnPtpRemoteSrcIpAddrType_Object((1,3,6,1,4,1,3902,1015,66,1,3,1,1),_ZxAnPtpRemoteSrcIpAddrType_Type())
zxAnPtpRemoteSrcIpAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnPtpRemoteSrcIpAddrType.setStatus(_A)
_ZxAnPtpRemoteSrcIpAddress_Type=InetAddress
_ZxAnPtpRemoteSrcIpAddress_Object=MibTableColumn
zxAnPtpRemoteSrcIpAddress=_ZxAnPtpRemoteSrcIpAddress_Object((1,3,6,1,4,1,3902,1015,66,1,3,1,2),_ZxAnPtpRemoteSrcIpAddress_Type())
zxAnPtpRemoteSrcIpAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnPtpRemoteSrcIpAddress.setStatus(_A)
class _ZxAnPtpRemoteSrcDomainNumber_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZxAnPtpRemoteSrcDomainNumber_Type.__name__=_B
_ZxAnPtpRemoteSrcDomainNumber_Object=MibTableColumn
zxAnPtpRemoteSrcDomainNumber=_ZxAnPtpRemoteSrcDomainNumber_Object((1,3,6,1,4,1,3902,1015,66,1,3,1,3),_ZxAnPtpRemoteSrcDomainNumber_Type())
zxAnPtpRemoteSrcDomainNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPtpRemoteSrcDomainNumber.setStatus(_A)
class _ZxAnPtpRemoteSrcPathDelayAdjust_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000000,1000000))
_ZxAnPtpRemoteSrcPathDelayAdjust_Type.__name__=_B
_ZxAnPtpRemoteSrcPathDelayAdjust_Object=MibTableColumn
zxAnPtpRemoteSrcPathDelayAdjust=_ZxAnPtpRemoteSrcPathDelayAdjust_Object((1,3,6,1,4,1,3902,1015,66,1,3,1,4),_ZxAnPtpRemoteSrcPathDelayAdjust_Type())
zxAnPtpRemoteSrcPathDelayAdjust.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPtpRemoteSrcPathDelayAdjust.setStatus(_A)
if mibBuilder.loadTexts:zxAnPtpRemoteSrcPathDelayAdjust.setUnits('ns')
class _ZxAnPtpRemoteSrcWorkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_Q,2),(_R,3)))
_ZxAnPtpRemoteSrcWorkStatus_Type.__name__=_B
_ZxAnPtpRemoteSrcWorkStatus_Object=MibTableColumn
zxAnPtpRemoteSrcWorkStatus=_ZxAnPtpRemoteSrcWorkStatus_Object((1,3,6,1,4,1,3902,1015,66,1,3,1,5),_ZxAnPtpRemoteSrcWorkStatus_Type())
zxAnPtpRemoteSrcWorkStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnPtpRemoteSrcWorkStatus.setStatus(_A)
_ZxAnPtpRemoteSrcRowStatus_Type=RowStatus
_ZxAnPtpRemoteSrcRowStatus_Object=MibTableColumn
zxAnPtpRemoteSrcRowStatus=_ZxAnPtpRemoteSrcRowStatus_Object((1,3,6,1,4,1,3902,1015,66,1,3,1,50),_ZxAnPtpRemoteSrcRowStatus_Type())
zxAnPtpRemoteSrcRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPtpRemoteSrcRowStatus.setStatus(_A)
_ZxAnSyncTimeClkSrcMgmt_ObjectIdentity=ObjectIdentity
zxAnSyncTimeClkSrcMgmt=_ZxAnSyncTimeClkSrcMgmt_ObjectIdentity((1,3,6,1,4,1,3902,1015,66,2))
_ZxAnSyncTime1ppsSrcTable_Object=MibTable
zxAnSyncTime1ppsSrcTable=_ZxAnSyncTime1ppsSrcTable_Object((1,3,6,1,4,1,3902,1015,66,2,3))
if mibBuilder.loadTexts:zxAnSyncTime1ppsSrcTable.setStatus(_A)
_ZxAnSyncTime1ppsSrcEntry_Object=MibTableRow
zxAnSyncTime1ppsSrcEntry=_ZxAnSyncTime1ppsSrcEntry_Object((1,3,6,1,4,1,3902,1015,66,2,3,1))
zxAnSyncTime1ppsSrcEntry.setIndexNames((0,_D,_S),(0,_D,_T),(0,_D,_U),(0,_D,_V))
if mibBuilder.loadTexts:zxAnSyncTime1ppsSrcEntry.setStatus(_A)
_ZxAnSyncTime1ppsSrcRack_Type=Integer32
_ZxAnSyncTime1ppsSrcRack_Object=MibTableColumn
zxAnSyncTime1ppsSrcRack=_ZxAnSyncTime1ppsSrcRack_Object((1,3,6,1,4,1,3902,1015,66,2,3,1,1),_ZxAnSyncTime1ppsSrcRack_Type())
zxAnSyncTime1ppsSrcRack.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnSyncTime1ppsSrcRack.setStatus(_A)
_ZxAnSyncTime1ppsSrcShelf_Type=Integer32
_ZxAnSyncTime1ppsSrcShelf_Object=MibTableColumn
zxAnSyncTime1ppsSrcShelf=_ZxAnSyncTime1ppsSrcShelf_Object((1,3,6,1,4,1,3902,1015,66,2,3,1,2),_ZxAnSyncTime1ppsSrcShelf_Type())
zxAnSyncTime1ppsSrcShelf.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnSyncTime1ppsSrcShelf.setStatus(_A)
_ZxAnSyncTime1ppsSrcSlot_Type=Integer32
_ZxAnSyncTime1ppsSrcSlot_Object=MibTableColumn
zxAnSyncTime1ppsSrcSlot=_ZxAnSyncTime1ppsSrcSlot_Object((1,3,6,1,4,1,3902,1015,66,2,3,1,3),_ZxAnSyncTime1ppsSrcSlot_Type())
zxAnSyncTime1ppsSrcSlot.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnSyncTime1ppsSrcSlot.setStatus(_A)
class _ZxAnSyncTime1ppsSrcId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_ZxAnSyncTime1ppsSrcId_Type.__name__=_B
_ZxAnSyncTime1ppsSrcId_Object=MibTableColumn
zxAnSyncTime1ppsSrcId=_ZxAnSyncTime1ppsSrcId_Object((1,3,6,1,4,1,3902,1015,66,2,3,1,4),_ZxAnSyncTime1ppsSrcId_Type())
zxAnSyncTime1ppsSrcId.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnSyncTime1ppsSrcId.setStatus(_A)
class _ZxAnSyncTime1ppsSrcSignalType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ptp',1),('onepps',2)))
_ZxAnSyncTime1ppsSrcSignalType_Type.__name__=_B
_ZxAnSyncTime1ppsSrcSignalType_Object=MibTableColumn
zxAnSyncTime1ppsSrcSignalType=_ZxAnSyncTime1ppsSrcSignalType_Object((1,3,6,1,4,1,3902,1015,66,2,3,1,5),_ZxAnSyncTime1ppsSrcSignalType_Type())
zxAnSyncTime1ppsSrcSignalType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSyncTime1ppsSrcSignalType.setStatus(_A)
class _ZxAnSyncTime1ppsSrcPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ZxAnSyncTime1ppsSrcPriority_Type.__name__=_B
_ZxAnSyncTime1ppsSrcPriority_Object=MibTableColumn
zxAnSyncTime1ppsSrcPriority=_ZxAnSyncTime1ppsSrcPriority_Object((1,3,6,1,4,1,3902,1015,66,2,3,1,6),_ZxAnSyncTime1ppsSrcPriority_Type())
zxAnSyncTime1ppsSrcPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSyncTime1ppsSrcPriority.setStatus(_A)
class _ZxAnSyncTime1ppsSrcPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('typeTtl',1),('type422',2)))
_ZxAnSyncTime1ppsSrcPortType_Type.__name__=_B
_ZxAnSyncTime1ppsSrcPortType_Object=MibTableColumn
zxAnSyncTime1ppsSrcPortType=_ZxAnSyncTime1ppsSrcPortType_Object((1,3,6,1,4,1,3902,1015,66,2,3,1,7),_ZxAnSyncTime1ppsSrcPortType_Type())
zxAnSyncTime1ppsSrcPortType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSyncTime1ppsSrcPortType.setStatus(_A)
class _ZxAnSyncTime1ppsSrcPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_ZxAnSyncTime1ppsSrcPort_Type.__name__=_B
_ZxAnSyncTime1ppsSrcPort_Object=MibTableColumn
zxAnSyncTime1ppsSrcPort=_ZxAnSyncTime1ppsSrcPort_Object((1,3,6,1,4,1,3902,1015,66,2,3,1,8),_ZxAnSyncTime1ppsSrcPort_Type())
zxAnSyncTime1ppsSrcPort.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSyncTime1ppsSrcPort.setStatus(_A)
class _ZxAnSyncTime1ppsSrcWorkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_Q,2),(_R,3)))
_ZxAnSyncTime1ppsSrcWorkStatus_Type.__name__=_B
_ZxAnSyncTime1ppsSrcWorkStatus_Object=MibTableColumn
zxAnSyncTime1ppsSrcWorkStatus=_ZxAnSyncTime1ppsSrcWorkStatus_Object((1,3,6,1,4,1,3902,1015,66,2,3,1,9),_ZxAnSyncTime1ppsSrcWorkStatus_Type())
zxAnSyncTime1ppsSrcWorkStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnSyncTime1ppsSrcWorkStatus.setStatus(_A)
class _ZxAnSyncTime1ppsSrcValidStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),('invalid',2)))
_ZxAnSyncTime1ppsSrcValidStatus_Type.__name__=_B
_ZxAnSyncTime1ppsSrcValidStatus_Object=MibTableColumn
zxAnSyncTime1ppsSrcValidStatus=_ZxAnSyncTime1ppsSrcValidStatus_Object((1,3,6,1,4,1,3902,1015,66,2,3,1,10),_ZxAnSyncTime1ppsSrcValidStatus_Type())
zxAnSyncTime1ppsSrcValidStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnSyncTime1ppsSrcValidStatus.setStatus(_A)
class _ZxAnSyncTime1ppsSrcPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_W,2),(_X,3)))
_ZxAnSyncTime1ppsSrcPortStatus_Type.__name__=_B
_ZxAnSyncTime1ppsSrcPortStatus_Object=MibTableColumn
zxAnSyncTime1ppsSrcPortStatus=_ZxAnSyncTime1ppsSrcPortStatus_Object((1,3,6,1,4,1,3902,1015,66,2,3,1,11),_ZxAnSyncTime1ppsSrcPortStatus_Type())
zxAnSyncTime1ppsSrcPortStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnSyncTime1ppsSrcPortStatus.setStatus(_A)
_ZxAnSyncTime1ppsSrcRowStatus_Type=RowStatus
_ZxAnSyncTime1ppsSrcRowStatus_Object=MibTableColumn
zxAnSyncTime1ppsSrcRowStatus=_ZxAnSyncTime1ppsSrcRowStatus_Object((1,3,6,1,4,1,3902,1015,66,2,3,1,30),_ZxAnSyncTime1ppsSrcRowStatus_Type())
zxAnSyncTime1ppsSrcRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSyncTime1ppsSrcRowStatus.setStatus(_A)
_ZxAnSyncTimeTodSrcTable_Object=MibTable
zxAnSyncTimeTodSrcTable=_ZxAnSyncTimeTodSrcTable_Object((1,3,6,1,4,1,3902,1015,66,2,4))
if mibBuilder.loadTexts:zxAnSyncTimeTodSrcTable.setStatus(_A)
_ZxAnSyncTimeTodSrcEntry_Object=MibTableRow
zxAnSyncTimeTodSrcEntry=_ZxAnSyncTimeTodSrcEntry_Object((1,3,6,1,4,1,3902,1015,66,2,4,1))
zxAnSyncTimeTodSrcEntry.setIndexNames((0,_D,_Y),(0,_D,_Z),(0,_D,_a),(0,_D,_b))
if mibBuilder.loadTexts:zxAnSyncTimeTodSrcEntry.setStatus(_A)
_ZxAnSyncTimeTodSrcRack_Type=Integer32
_ZxAnSyncTimeTodSrcRack_Object=MibTableColumn
zxAnSyncTimeTodSrcRack=_ZxAnSyncTimeTodSrcRack_Object((1,3,6,1,4,1,3902,1015,66,2,4,1,1),_ZxAnSyncTimeTodSrcRack_Type())
zxAnSyncTimeTodSrcRack.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnSyncTimeTodSrcRack.setStatus(_A)
_ZxAnSyncTimeTodSrcShelf_Type=Integer32
_ZxAnSyncTimeTodSrcShelf_Object=MibTableColumn
zxAnSyncTimeTodSrcShelf=_ZxAnSyncTimeTodSrcShelf_Object((1,3,6,1,4,1,3902,1015,66,2,4,1,2),_ZxAnSyncTimeTodSrcShelf_Type())
zxAnSyncTimeTodSrcShelf.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnSyncTimeTodSrcShelf.setStatus(_A)
_ZxAnSyncTimeTodSrcSlot_Type=Integer32
_ZxAnSyncTimeTodSrcSlot_Object=MibTableColumn
zxAnSyncTimeTodSrcSlot=_ZxAnSyncTimeTodSrcSlot_Object((1,3,6,1,4,1,3902,1015,66,2,4,1,3),_ZxAnSyncTimeTodSrcSlot_Type())
zxAnSyncTimeTodSrcSlot.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnSyncTimeTodSrcSlot.setStatus(_A)
_ZxAnSyncTimeTodSrcPort_Type=Integer32
_ZxAnSyncTimeTodSrcPort_Object=MibTableColumn
zxAnSyncTimeTodSrcPort=_ZxAnSyncTimeTodSrcPort_Object((1,3,6,1,4,1,3902,1015,66,2,4,1,4),_ZxAnSyncTimeTodSrcPort_Type())
zxAnSyncTimeTodSrcPort.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnSyncTimeTodSrcPort.setStatus(_A)
class _ZxAnSyncTimeTodSrcSignalType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('gps',1),('chinaMobile',2),('chinaUnicom',3),('chinaTelecom',4)))
_ZxAnSyncTimeTodSrcSignalType_Type.__name__=_B
_ZxAnSyncTimeTodSrcSignalType_Object=MibTableColumn
zxAnSyncTimeTodSrcSignalType=_ZxAnSyncTimeTodSrcSignalType_Object((1,3,6,1,4,1,3902,1015,66,2,4,1,5),_ZxAnSyncTimeTodSrcSignalType_Type())
zxAnSyncTimeTodSrcSignalType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSyncTimeTodSrcSignalType.setStatus(_A)
class _ZxAnSyncTimeTodSrcYearAdjust_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2050))
_ZxAnSyncTimeTodSrcYearAdjust_Type.__name__=_B
_ZxAnSyncTimeTodSrcYearAdjust_Object=MibTableColumn
zxAnSyncTimeTodSrcYearAdjust=_ZxAnSyncTimeTodSrcYearAdjust_Object((1,3,6,1,4,1,3902,1015,66,2,4,1,6),_ZxAnSyncTimeTodSrcYearAdjust_Type())
zxAnSyncTimeTodSrcYearAdjust.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSyncTimeTodSrcYearAdjust.setStatus(_A)
if mibBuilder.loadTexts:zxAnSyncTimeTodSrcYearAdjust.setUnits('year')
class _ZxAnSyncTimeTodSrcPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_W,2),(_X,3)))
_ZxAnSyncTimeTodSrcPortStatus_Type.__name__=_B
_ZxAnSyncTimeTodSrcPortStatus_Object=MibTableColumn
zxAnSyncTimeTodSrcPortStatus=_ZxAnSyncTimeTodSrcPortStatus_Object((1,3,6,1,4,1,3902,1015,66,2,4,1,7),_ZxAnSyncTimeTodSrcPortStatus_Type())
zxAnSyncTimeTodSrcPortStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnSyncTimeTodSrcPortStatus.setStatus(_A)
_ZxAnSyncTimeTodSrcRowStatus_Type=RowStatus
_ZxAnSyncTimeTodSrcRowStatus_Object=MibTableColumn
zxAnSyncTimeTodSrcRowStatus=_ZxAnSyncTimeTodSrcRowStatus_Object((1,3,6,1,4,1,3902,1015,66,2,4,1,30),_ZxAnSyncTimeTodSrcRowStatus_Type())
zxAnSyncTimeTodSrcRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSyncTimeTodSrcRowStatus.setStatus(_A)
_ZxAnSyncTimeOutputPortTable_Object=MibTable
zxAnSyncTimeOutputPortTable=_ZxAnSyncTimeOutputPortTable_Object((1,3,6,1,4,1,3902,1015,66,2,5))
if mibBuilder.loadTexts:zxAnSyncTimeOutputPortTable.setStatus(_A)
_ZxAnSyncTimeOutputPortEntry_Object=MibTableRow
zxAnSyncTimeOutputPortEntry=_ZxAnSyncTimeOutputPortEntry_Object((1,3,6,1,4,1,3902,1015,66,2,5,1))
zxAnSyncTimeOutputPortEntry.setIndexNames((0,_D,_c),(0,_D,_d),(0,_D,_e),(0,_D,_f))
if mibBuilder.loadTexts:zxAnSyncTimeOutputPortEntry.setStatus(_A)
_ZxAnSyncTimeOutputRack_Type=Integer32
_ZxAnSyncTimeOutputRack_Object=MibTableColumn
zxAnSyncTimeOutputRack=_ZxAnSyncTimeOutputRack_Object((1,3,6,1,4,1,3902,1015,66,2,5,1,1),_ZxAnSyncTimeOutputRack_Type())
zxAnSyncTimeOutputRack.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnSyncTimeOutputRack.setStatus(_A)
_ZxAnSyncTimeOutputShelf_Type=Integer32
_ZxAnSyncTimeOutputShelf_Object=MibTableColumn
zxAnSyncTimeOutputShelf=_ZxAnSyncTimeOutputShelf_Object((1,3,6,1,4,1,3902,1015,66,2,5,1,2),_ZxAnSyncTimeOutputShelf_Type())
zxAnSyncTimeOutputShelf.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnSyncTimeOutputShelf.setStatus(_A)
_ZxAnSyncTimeOutputSlot_Type=Integer32
_ZxAnSyncTimeOutputSlot_Object=MibTableColumn
zxAnSyncTimeOutputSlot=_ZxAnSyncTimeOutputSlot_Object((1,3,6,1,4,1,3902,1015,66,2,5,1,3),_ZxAnSyncTimeOutputSlot_Type())
zxAnSyncTimeOutputSlot.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnSyncTimeOutputSlot.setStatus(_A)
_ZxAnSyncTimeOutputPort_Type=Integer32
_ZxAnSyncTimeOutputPort_Object=MibTableColumn
zxAnSyncTimeOutputPort=_ZxAnSyncTimeOutputPort_Object((1,3,6,1,4,1,3902,1015,66,2,5,1,4),_ZxAnSyncTimeOutputPort_Type())
zxAnSyncTimeOutputPort.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnSyncTimeOutputPort.setStatus(_A)
class _ZxAnSyncTimeOutputPortEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_ZxAnSyncTimeOutputPortEnable_Type.__name__=_B
_ZxAnSyncTimeOutputPortEnable_Object=MibTableColumn
zxAnSyncTimeOutputPortEnable=_ZxAnSyncTimeOutputPortEnable_Object((1,3,6,1,4,1,3902,1015,66,2,5,1,5),_ZxAnSyncTimeOutputPortEnable_Type())
zxAnSyncTimeOutputPortEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSyncTimeOutputPortEnable.setStatus(_A)
class _ZxAnSyncTimeOutputPortPhaseAdjus_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000000,1000000))
_ZxAnSyncTimeOutputPortPhaseAdjus_Type.__name__=_B
_ZxAnSyncTimeOutputPortPhaseAdjus_Object=MibTableColumn
zxAnSyncTimeOutputPortPhaseAdjus=_ZxAnSyncTimeOutputPortPhaseAdjus_Object((1,3,6,1,4,1,3902,1015,66,2,5,1,6),_ZxAnSyncTimeOutputPortPhaseAdjus_Type())
zxAnSyncTimeOutputPortPhaseAdjus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSyncTimeOutputPortPhaseAdjus.setStatus(_A)
if mibBuilder.loadTexts:zxAnSyncTimeOutputPortPhaseAdjus.setUnits('ns')
_ZxAnSyncTimeOutputPortRowStatus_Type=RowStatus
_ZxAnSyncTimeOutputPortRowStatus_Object=MibTableColumn
zxAnSyncTimeOutputPortRowStatus=_ZxAnSyncTimeOutputPortRowStatus_Object((1,3,6,1,4,1,3902,1015,66,2,5,1,30),_ZxAnSyncTimeOutputPortRowStatus_Type())
zxAnSyncTimeOutputPortRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSyncTimeOutputPortRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'zxAnIeee1588Mib':zxAnIeee1588Mib,'zxAnPtpMgmt':zxAnPtpMgmt,'zxAnPtpTable':zxAnPtpTable,'zxAnPtpEntry':zxAnPtpEntry,_J:zxAnPtpRack,_K:zxAnPtpShelf,_L:zxAnPtpSlot,_M:zxAnPtpId,'zxAnPtpClockType':zxAnPtpClockType,'zxAnPtpSlaveOnly':zxAnPtpSlaveOnly,'zxAnPtpDomainNumber':zxAnPtpDomainNumber,'zxAnPtpProtocolIpAddrType':zxAnPtpProtocolIpAddrType,'zxAnPtpProtocolIpAddress':zxAnPtpProtocolIpAddress,'zxAnPtpEthWorkMode':zxAnPtpEthWorkMode,'zxAnPtpPacketsMode':zxAnPtpPacketsMode,'zxAnPtpTwoStepFlag':zxAnPtpTwoStepFlag,'zxAnPtpSendPacketsRate':zxAnPtpSendPacketsRate,'zxAnPtpClockStatus':zxAnPtpClockStatus,'zxAnPtpUtcTime':zxAnPtpUtcTime,'zxAnPtpRowStatus':zxAnPtpRowStatus,'zxAnPtpRemoteSrcTable':zxAnPtpRemoteSrcTable,'zxAnPtpRemoteSrcEntry':zxAnPtpRemoteSrcEntry,_O:zxAnPtpRemoteSrcIpAddrType,_P:zxAnPtpRemoteSrcIpAddress,'zxAnPtpRemoteSrcDomainNumber':zxAnPtpRemoteSrcDomainNumber,'zxAnPtpRemoteSrcPathDelayAdjust':zxAnPtpRemoteSrcPathDelayAdjust,'zxAnPtpRemoteSrcWorkStatus':zxAnPtpRemoteSrcWorkStatus,'zxAnPtpRemoteSrcRowStatus':zxAnPtpRemoteSrcRowStatus,'zxAnSyncTimeClkSrcMgmt':zxAnSyncTimeClkSrcMgmt,'zxAnSyncTime1ppsSrcTable':zxAnSyncTime1ppsSrcTable,'zxAnSyncTime1ppsSrcEntry':zxAnSyncTime1ppsSrcEntry,_S:zxAnSyncTime1ppsSrcRack,_T:zxAnSyncTime1ppsSrcShelf,_U:zxAnSyncTime1ppsSrcSlot,_V:zxAnSyncTime1ppsSrcId,'zxAnSyncTime1ppsSrcSignalType':zxAnSyncTime1ppsSrcSignalType,'zxAnSyncTime1ppsSrcPriority':zxAnSyncTime1ppsSrcPriority,'zxAnSyncTime1ppsSrcPortType':zxAnSyncTime1ppsSrcPortType,'zxAnSyncTime1ppsSrcPort':zxAnSyncTime1ppsSrcPort,'zxAnSyncTime1ppsSrcWorkStatus':zxAnSyncTime1ppsSrcWorkStatus,'zxAnSyncTime1ppsSrcValidStatus':zxAnSyncTime1ppsSrcValidStatus,'zxAnSyncTime1ppsSrcPortStatus':zxAnSyncTime1ppsSrcPortStatus,'zxAnSyncTime1ppsSrcRowStatus':zxAnSyncTime1ppsSrcRowStatus,'zxAnSyncTimeTodSrcTable':zxAnSyncTimeTodSrcTable,'zxAnSyncTimeTodSrcEntry':zxAnSyncTimeTodSrcEntry,_Y:zxAnSyncTimeTodSrcRack,_Z:zxAnSyncTimeTodSrcShelf,_a:zxAnSyncTimeTodSrcSlot,_b:zxAnSyncTimeTodSrcPort,'zxAnSyncTimeTodSrcSignalType':zxAnSyncTimeTodSrcSignalType,'zxAnSyncTimeTodSrcYearAdjust':zxAnSyncTimeTodSrcYearAdjust,'zxAnSyncTimeTodSrcPortStatus':zxAnSyncTimeTodSrcPortStatus,'zxAnSyncTimeTodSrcRowStatus':zxAnSyncTimeTodSrcRowStatus,'zxAnSyncTimeOutputPortTable':zxAnSyncTimeOutputPortTable,'zxAnSyncTimeOutputPortEntry':zxAnSyncTimeOutputPortEntry,_c:zxAnSyncTimeOutputRack,_d:zxAnSyncTimeOutputShelf,_e:zxAnSyncTimeOutputSlot,_f:zxAnSyncTimeOutputPort,'zxAnSyncTimeOutputPortEnable':zxAnSyncTimeOutputPortEnable,'zxAnSyncTimeOutputPortPhaseAdjus':zxAnSyncTimeOutputPortPhaseAdjus,'zxAnSyncTimeOutputPortRowStatus':zxAnSyncTimeOutputPortRowStatus})