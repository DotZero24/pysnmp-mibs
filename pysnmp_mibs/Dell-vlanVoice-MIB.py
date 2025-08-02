_V='vlanVoiceOUIBasedPrefix'
_U='default'
_T='vlanVoiceUcDeviceInterface'
_S='vlanVoiceUcDeviceMacAddress'
_R='vlanVoiceUcDeviceType'
_Q='oui-enabled'
_P='auto-triggered'
_O='auto-enabled'
_N='2010-09-26 00:00'
_M='VlanIndex'
_L='ifIndex'
_K='IF-MIB'
_J='OctetString'
_I='disabled'
_H='DisplayString'
_G='VlanPriority'
_F='Dell-vlanVoice-MIB'
_E='TruthValue'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
VlanPriority,=mibBuilder.importSymbols('Dell-MIB',_G)
vlan,=mibBuilder.importSymbols('Dell-vlan-MIB','vlan')
ifIndex,=mibBuilder.importSymbols(_K,_L)
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB',_M)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_H,'MacAddress','PhysAddress','RowStatus','TextualConvention',_E)
vlanVoice=ModuleIdentity((1,3,6,1,4,1,89,48,54))
if mibBuilder.loadTexts:vlanVoice.setRevisions((_N,_N))
class _VlanVoiceAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_I,0),(_O,1),(_P,2),(_Q,3)))
_VlanVoiceAdminState_Type.__name__=_B
_VlanVoiceAdminState_Object=MibScalar
vlanVoiceAdminState=_VlanVoiceAdminState_Object((1,3,6,1,4,1,89,48,54,6),_VlanVoiceAdminState_Type())
vlanVoiceAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanVoiceAdminState.setStatus(_A)
class _VlanVoiceOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_I,0),(_O,1),(_P,2),(_Q,3)))
_VlanVoiceOperState_Type.__name__=_B
_VlanVoiceOperState_Object=MibScalar
vlanVoiceOperState=_VlanVoiceOperState_Object((1,3,6,1,4,1,89,48,54,7),_VlanVoiceOperState_Type())
vlanVoiceOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanVoiceOperState.setStatus(_A)
class _VlanVoiceAdminVid_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_VlanVoiceAdminVid_Type.__name__=_B
_VlanVoiceAdminVid_Object=MibScalar
vlanVoiceAdminVid=_VlanVoiceAdminVid_Object((1,3,6,1,4,1,89,48,54,8),_VlanVoiceAdminVid_Type())
vlanVoiceAdminVid.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanVoiceAdminVid.setStatus(_A)
class _VlanVoiceOperVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_VlanVoiceOperVid_Type.__name__=_B
_VlanVoiceOperVid_Object=MibScalar
vlanVoiceOperVid=_VlanVoiceOperVid_Object((1,3,6,1,4,1,89,48,54,9),_VlanVoiceOperVid_Type())
vlanVoiceOperVid.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanVoiceOperVid.setStatus(_A)
_VlanVoiceUcDeviceTable_Object=MibTable
vlanVoiceUcDeviceTable=_VlanVoiceUcDeviceTable_Object((1,3,6,1,4,1,89,48,54,10))
if mibBuilder.loadTexts:vlanVoiceUcDeviceTable.setStatus(_A)
_VlanVoiceUcDeviceEntry_Object=MibTableRow
vlanVoiceUcDeviceEntry=_VlanVoiceUcDeviceEntry_Object((1,3,6,1,4,1,89,48,54,10,1))
vlanVoiceUcDeviceEntry.setIndexNames((0,_F,_R),(0,_F,_S),(0,_F,_T))
if mibBuilder.loadTexts:vlanVoiceUcDeviceEntry.setStatus(_A)
class _VlanVoiceUcDeviceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_U,0),('static',1),('uc',2)))
_VlanVoiceUcDeviceType_Type.__name__=_B
_VlanVoiceUcDeviceType_Object=MibTableColumn
vlanVoiceUcDeviceType=_VlanVoiceUcDeviceType_Object((1,3,6,1,4,1,89,48,54,10,1,1),_VlanVoiceUcDeviceType_Type())
vlanVoiceUcDeviceType.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanVoiceUcDeviceType.setStatus(_A)
_VlanVoiceUcDeviceMacAddress_Type=MacAddress
_VlanVoiceUcDeviceMacAddress_Object=MibTableColumn
vlanVoiceUcDeviceMacAddress=_VlanVoiceUcDeviceMacAddress_Object((1,3,6,1,4,1,89,48,54,10,1,2),_VlanVoiceUcDeviceMacAddress_Type())
vlanVoiceUcDeviceMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanVoiceUcDeviceMacAddress.setStatus(_A)
_VlanVoiceUcDeviceInterface_Type=Integer32
_VlanVoiceUcDeviceInterface_Object=MibTableColumn
vlanVoiceUcDeviceInterface=_VlanVoiceUcDeviceInterface_Object((1,3,6,1,4,1,89,48,54,10,1,3),_VlanVoiceUcDeviceInterface_Type())
vlanVoiceUcDeviceInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanVoiceUcDeviceInterface.setStatus(_A)
class _VlanVoiceUcDeviceVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_VlanVoiceUcDeviceVid_Type.__name__=_B
_VlanVoiceUcDeviceVid_Object=MibTableColumn
vlanVoiceUcDeviceVid=_VlanVoiceUcDeviceVid_Object((1,3,6,1,4,1,89,48,54,10,1,4),_VlanVoiceUcDeviceVid_Type())
vlanVoiceUcDeviceVid.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanVoiceUcDeviceVid.setStatus(_A)
class _VlanVoiceUcDeviceVpt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_VlanVoiceUcDeviceVpt_Type.__name__=_B
_VlanVoiceUcDeviceVpt_Object=MibTableColumn
vlanVoiceUcDeviceVpt=_VlanVoiceUcDeviceVpt_Object((1,3,6,1,4,1,89,48,54,10,1,5),_VlanVoiceUcDeviceVpt_Type())
vlanVoiceUcDeviceVpt.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanVoiceUcDeviceVpt.setStatus(_A)
class _VlanVoiceUcDeviceDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_VlanVoiceUcDeviceDscp_Type.__name__=_B
_VlanVoiceUcDeviceDscp_Object=MibTableColumn
vlanVoiceUcDeviceDscp=_VlanVoiceUcDeviceDscp_Object((1,3,6,1,4,1,89,48,54,10,1,6),_VlanVoiceUcDeviceDscp_Type())
vlanVoiceUcDeviceDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanVoiceUcDeviceDscp.setStatus(_A)
_VlanVoiceUcDeviceIsBest_Type=TruthValue
_VlanVoiceUcDeviceIsBest_Object=MibTableColumn
vlanVoiceUcDeviceIsBest=_VlanVoiceUcDeviceIsBest_Object((1,3,6,1,4,1,89,48,54,10,1,7),_VlanVoiceUcDeviceIsBest_Type())
vlanVoiceUcDeviceIsBest.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanVoiceUcDeviceIsBest.setStatus(_A)
_VlanVoiceAuto_ObjectIdentity=ObjectIdentity
vlanVoiceAuto=_VlanVoiceAuto_ObjectIdentity((1,3,6,1,4,1,89,48,54,11))
_VlanVoiceAutoAdmin_ObjectIdentity=ObjectIdentity
vlanVoiceAutoAdmin=_VlanVoiceAutoAdmin_ObjectIdentity((1,3,6,1,4,1,89,48,54,11,1))
class _VlanVoiceAutoAdminVpt_Type(VlanPriority):defaultValue=0
_VlanVoiceAutoAdminVpt_Type.__name__=_G
_VlanVoiceAutoAdminVpt_Object=MibScalar
vlanVoiceAutoAdminVpt=_VlanVoiceAutoAdminVpt_Object((1,3,6,1,4,1,89,48,54,11,1,1),_VlanVoiceAutoAdminVpt_Type())
vlanVoiceAutoAdminVpt.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanVoiceAutoAdminVpt.setStatus(_A)
class _VlanVoiceAutoAdminDscp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_VlanVoiceAutoAdminDscp_Type.__name__=_B
_VlanVoiceAutoAdminDscp_Object=MibScalar
vlanVoiceAutoAdminDscp=_VlanVoiceAutoAdminDscp_Object((1,3,6,1,4,1,89,48,54,11,1,2),_VlanVoiceAutoAdminDscp_Type())
vlanVoiceAutoAdminDscp.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanVoiceAutoAdminDscp.setStatus(_A)
_VlanVoiceAutoOper_ObjectIdentity=ObjectIdentity
vlanVoiceAutoOper=_VlanVoiceAutoOper_ObjectIdentity((1,3,6,1,4,1,89,48,54,11,2))
_VlanVoiceAutoOperVpt_Type=VlanPriority
_VlanVoiceAutoOperVpt_Object=MibScalar
vlanVoiceAutoOperVpt=_VlanVoiceAutoOperVpt_Object((1,3,6,1,4,1,89,48,54,11,2,1),_VlanVoiceAutoOperVpt_Type())
vlanVoiceAutoOperVpt.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanVoiceAutoOperVpt.setStatus(_A)
class _VlanVoiceAutoOperDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_VlanVoiceAutoOperDscp_Type.__name__=_B
_VlanVoiceAutoOperDscp_Object=MibScalar
vlanVoiceAutoOperDscp=_VlanVoiceAutoOperDscp_Object((1,3,6,1,4,1,89,48,54,11,2,2),_VlanVoiceAutoOperDscp_Type())
vlanVoiceAutoOperDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanVoiceAutoOperDscp.setStatus(_A)
_VlanVoiceAutoOperSource_Type=MacAddress
_VlanVoiceAutoOperSource_Object=MibScalar
vlanVoiceAutoOperSource=_VlanVoiceAutoOperSource_Object((1,3,6,1,4,1,89,48,54,11,2,3),_VlanVoiceAutoOperSource_Type())
vlanVoiceAutoOperSource.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanVoiceAutoOperSource.setStatus(_A)
class _VlanVoiceAutoOperPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,6,10)));namedValues=NamedValues(*(('staticActive',0),('staticInActive',1),('ucActive',2),('ucInActive',3),(_U,6),(_I,10)))
_VlanVoiceAutoOperPriority_Type.__name__=_B
_VlanVoiceAutoOperPriority_Object=MibScalar
vlanVoiceAutoOperPriority=_VlanVoiceAutoOperPriority_Object((1,3,6,1,4,1,89,48,54,11,2,4),_VlanVoiceAutoOperPriority_Type())
vlanVoiceAutoOperPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanVoiceAutoOperPriority.setStatus(_A)
_VlanVoiceAutoRefresh_Type=TruthValue
_VlanVoiceAutoRefresh_Object=MibScalar
vlanVoiceAutoRefresh=_VlanVoiceAutoRefresh_Object((1,3,6,1,4,1,89,48,54,11,3),_VlanVoiceAutoRefresh_Type())
vlanVoiceAutoRefresh.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanVoiceAutoRefresh.setStatus(_A)
class _VlanVoiceAutoAgreedVlanLastChange_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(12,12));fixedLength=12
_VlanVoiceAutoAgreedVlanLastChange_Type.__name__=_H
_VlanVoiceAutoAgreedVlanLastChange_Object=MibScalar
vlanVoiceAutoAgreedVlanLastChange=_VlanVoiceAutoAgreedVlanLastChange_Object((1,3,6,1,4,1,89,48,54,11,4),_VlanVoiceAutoAgreedVlanLastChange_Type())
vlanVoiceAutoAgreedVlanLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanVoiceAutoAgreedVlanLastChange.setStatus(_A)
_VlanVoiceOUIBased_ObjectIdentity=ObjectIdentity
vlanVoiceOUIBased=_VlanVoiceOUIBased_ObjectIdentity((1,3,6,1,4,1,89,48,54,12))
class _VlanVoiceOUIBasedAdminPriority_Type(VlanPriority):defaultValue=6
_VlanVoiceOUIBasedAdminPriority_Type.__name__=_G
_VlanVoiceOUIBasedAdminPriority_Object=MibScalar
vlanVoiceOUIBasedAdminPriority=_VlanVoiceOUIBasedAdminPriority_Object((1,3,6,1,4,1,89,48,54,12,1),_VlanVoiceOUIBasedAdminPriority_Type())
vlanVoiceOUIBasedAdminPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanVoiceOUIBasedAdminPriority.setStatus(_A)
class _VlanVoiceOUIBasedAdminRemark_Type(TruthValue):defaultValue=2
_VlanVoiceOUIBasedAdminRemark_Type.__name__=_E
_VlanVoiceOUIBasedAdminRemark_Object=MibScalar
vlanVoiceOUIBasedAdminRemark=_VlanVoiceOUIBasedAdminRemark_Object((1,3,6,1,4,1,89,48,54,12,2),_VlanVoiceOUIBasedAdminRemark_Type())
vlanVoiceOUIBasedAdminRemark.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanVoiceOUIBasedAdminRemark.setStatus(_A)
class _VlanVoiceOUIBasedSetToDefault_Type(TruthValue):defaultValue=2
_VlanVoiceOUIBasedSetToDefault_Type.__name__=_E
_VlanVoiceOUIBasedSetToDefault_Object=MibScalar
vlanVoiceOUIBasedSetToDefault=_VlanVoiceOUIBasedSetToDefault_Object((1,3,6,1,4,1,89,48,54,12,3),_VlanVoiceOUIBasedSetToDefault_Type())
vlanVoiceOUIBasedSetToDefault.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanVoiceOUIBasedSetToDefault.setStatus(_A)
_VlanVoiceOUIBasedTable_Object=MibTable
vlanVoiceOUIBasedTable=_VlanVoiceOUIBasedTable_Object((1,3,6,1,4,1,89,48,54,12,4))
if mibBuilder.loadTexts:vlanVoiceOUIBasedTable.setStatus(_A)
_VlanVoiceOUIBasedEntry_Object=MibTableRow
vlanVoiceOUIBasedEntry=_VlanVoiceOUIBasedEntry_Object((1,3,6,1,4,1,89,48,54,12,4,1))
vlanVoiceOUIBasedEntry.setIndexNames((0,_F,_V))
if mibBuilder.loadTexts:vlanVoiceOUIBasedEntry.setStatus(_A)
class _VlanVoiceOUIBasedPrefix_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_VlanVoiceOUIBasedPrefix_Type.__name__=_J
_VlanVoiceOUIBasedPrefix_Object=MibTableColumn
vlanVoiceOUIBasedPrefix=_VlanVoiceOUIBasedPrefix_Object((1,3,6,1,4,1,89,48,54,12,4,1,1),_VlanVoiceOUIBasedPrefix_Type())
vlanVoiceOUIBasedPrefix.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:vlanVoiceOUIBasedPrefix.setStatus(_A)
class _VlanVoiceOUIBasedDescription_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_VlanVoiceOUIBasedDescription_Type.__name__=_H
_VlanVoiceOUIBasedDescription_Object=MibTableColumn
vlanVoiceOUIBasedDescription=_VlanVoiceOUIBasedDescription_Object((1,3,6,1,4,1,89,48,54,12,4,1,2),_VlanVoiceOUIBasedDescription_Type())
vlanVoiceOUIBasedDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanVoiceOUIBasedDescription.setStatus(_A)
_VlanVoiceOUIBasedEntryRowStatus_Type=RowStatus
_VlanVoiceOUIBasedEntryRowStatus_Object=MibTableColumn
vlanVoiceOUIBasedEntryRowStatus=_VlanVoiceOUIBasedEntryRowStatus_Object((1,3,6,1,4,1,89,48,54,12,4,1,3),_VlanVoiceOUIBasedEntryRowStatus_Type())
vlanVoiceOUIBasedEntryRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:vlanVoiceOUIBasedEntryRowStatus.setStatus(_A)
_VlanVoiceOUIBasedPortTable_Object=MibTable
vlanVoiceOUIBasedPortTable=_VlanVoiceOUIBasedPortTable_Object((1,3,6,1,4,1,89,48,54,12,5))
if mibBuilder.loadTexts:vlanVoiceOUIBasedPortTable.setStatus(_A)
_VlanVoiceOUIBasedPortEntry_Object=MibTableRow
vlanVoiceOUIBasedPortEntry=_VlanVoiceOUIBasedPortEntry_Object((1,3,6,1,4,1,89,48,54,12,5,1))
vlanVoiceOUIBasedPortEntry.setIndexNames((0,_K,_L))
if mibBuilder.loadTexts:vlanVoiceOUIBasedPortEntry.setStatus(_A)
class _VlanVoiceOUIBasedPortEnable_Type(TruthValue):defaultValue=2
_VlanVoiceOUIBasedPortEnable_Type.__name__=_E
_VlanVoiceOUIBasedPortEnable_Object=MibTableColumn
vlanVoiceOUIBasedPortEnable=_VlanVoiceOUIBasedPortEnable_Object((1,3,6,1,4,1,89,48,54,12,5,1,1),_VlanVoiceOUIBasedPortEnable_Type())
vlanVoiceOUIBasedPortEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanVoiceOUIBasedPortEnable.setStatus(_A)
class _VlanVoiceOUIBasedPortVlanIndex_Type(VlanIndex):defaultValue=4095
_VlanVoiceOUIBasedPortVlanIndex_Type.__name__=_M
_VlanVoiceOUIBasedPortVlanIndex_Object=MibTableColumn
vlanVoiceOUIBasedPortVlanIndex=_VlanVoiceOUIBasedPortVlanIndex_Object((1,3,6,1,4,1,89,48,54,12,5,1,2),_VlanVoiceOUIBasedPortVlanIndex_Type())
vlanVoiceOUIBasedPortVlanIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanVoiceOUIBasedPortVlanIndex.setStatus(_A)
class _VlanVoiceOUIBasedPortSecure_Type(TruthValue):defaultValue=2
_VlanVoiceOUIBasedPortSecure_Type.__name__=_E
_VlanVoiceOUIBasedPortSecure_Object=MibTableColumn
vlanVoiceOUIBasedPortSecure=_VlanVoiceOUIBasedPortSecure_Object((1,3,6,1,4,1,89,48,54,12,5,1,3),_VlanVoiceOUIBasedPortSecure_Type())
vlanVoiceOUIBasedPortSecure.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanVoiceOUIBasedPortSecure.setStatus(_A)
class _VlanVoiceOUIBasedPortCurrentMembership_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('notActive',2)))
_VlanVoiceOUIBasedPortCurrentMembership_Type.__name__=_B
_VlanVoiceOUIBasedPortCurrentMembership_Object=MibTableColumn
vlanVoiceOUIBasedPortCurrentMembership=_VlanVoiceOUIBasedPortCurrentMembership_Object((1,3,6,1,4,1,89,48,54,12,5,1,4),_VlanVoiceOUIBasedPortCurrentMembership_Type())
vlanVoiceOUIBasedPortCurrentMembership.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanVoiceOUIBasedPortCurrentMembership.setStatus(_A)
class _VlanVoiceOUIBasedPortQosMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('src',1),('all',2)))
_VlanVoiceOUIBasedPortQosMode_Type.__name__=_B
_VlanVoiceOUIBasedPortQosMode_Object=MibTableColumn
vlanVoiceOUIBasedPortQosMode=_VlanVoiceOUIBasedPortQosMode_Object((1,3,6,1,4,1,89,48,54,12,5,1,5),_VlanVoiceOUIBasedPortQosMode_Type())
vlanVoiceOUIBasedPortQosMode.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanVoiceOUIBasedPortQosMode.setStatus(_A)
class _VlanVoiceOUIBasedAgingTimeout_Type(Integer32):defaultValue=1440;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,43200))
_VlanVoiceOUIBasedAgingTimeout_Type.__name__=_B
_VlanVoiceOUIBasedAgingTimeout_Object=MibScalar
vlanVoiceOUIBasedAgingTimeout=_VlanVoiceOUIBasedAgingTimeout_Object((1,3,6,1,4,1,89,48,54,12,6),_VlanVoiceOUIBasedAgingTimeout_Type())
vlanVoiceOUIBasedAgingTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanVoiceOUIBasedAgingTimeout.setStatus(_A)
if mibBuilder.loadTexts:vlanVoiceOUIBasedAgingTimeout.setUnits('minutes')
mibBuilder.exportSymbols(_F,**{'vlanVoice':vlanVoice,'vlanVoiceAdminState':vlanVoiceAdminState,'vlanVoiceOperState':vlanVoiceOperState,'vlanVoiceAdminVid':vlanVoiceAdminVid,'vlanVoiceOperVid':vlanVoiceOperVid,'vlanVoiceUcDeviceTable':vlanVoiceUcDeviceTable,'vlanVoiceUcDeviceEntry':vlanVoiceUcDeviceEntry,_R:vlanVoiceUcDeviceType,_S:vlanVoiceUcDeviceMacAddress,_T:vlanVoiceUcDeviceInterface,'vlanVoiceUcDeviceVid':vlanVoiceUcDeviceVid,'vlanVoiceUcDeviceVpt':vlanVoiceUcDeviceVpt,'vlanVoiceUcDeviceDscp':vlanVoiceUcDeviceDscp,'vlanVoiceUcDeviceIsBest':vlanVoiceUcDeviceIsBest,'vlanVoiceAuto':vlanVoiceAuto,'vlanVoiceAutoAdmin':vlanVoiceAutoAdmin,'vlanVoiceAutoAdminVpt':vlanVoiceAutoAdminVpt,'vlanVoiceAutoAdminDscp':vlanVoiceAutoAdminDscp,'vlanVoiceAutoOper':vlanVoiceAutoOper,'vlanVoiceAutoOperVpt':vlanVoiceAutoOperVpt,'vlanVoiceAutoOperDscp':vlanVoiceAutoOperDscp,'vlanVoiceAutoOperSource':vlanVoiceAutoOperSource,'vlanVoiceAutoOperPriority':vlanVoiceAutoOperPriority,'vlanVoiceAutoRefresh':vlanVoiceAutoRefresh,'vlanVoiceAutoAgreedVlanLastChange':vlanVoiceAutoAgreedVlanLastChange,'vlanVoiceOUIBased':vlanVoiceOUIBased,'vlanVoiceOUIBasedAdminPriority':vlanVoiceOUIBasedAdminPriority,'vlanVoiceOUIBasedAdminRemark':vlanVoiceOUIBasedAdminRemark,'vlanVoiceOUIBasedSetToDefault':vlanVoiceOUIBasedSetToDefault,'vlanVoiceOUIBasedTable':vlanVoiceOUIBasedTable,'vlanVoiceOUIBasedEntry':vlanVoiceOUIBasedEntry,_V:vlanVoiceOUIBasedPrefix,'vlanVoiceOUIBasedDescription':vlanVoiceOUIBasedDescription,'vlanVoiceOUIBasedEntryRowStatus':vlanVoiceOUIBasedEntryRowStatus,'vlanVoiceOUIBasedPortTable':vlanVoiceOUIBasedPortTable,'vlanVoiceOUIBasedPortEntry':vlanVoiceOUIBasedPortEntry,'vlanVoiceOUIBasedPortEnable':vlanVoiceOUIBasedPortEnable,'vlanVoiceOUIBasedPortVlanIndex':vlanVoiceOUIBasedPortVlanIndex,'vlanVoiceOUIBasedPortSecure':vlanVoiceOUIBasedPortSecure,'vlanVoiceOUIBasedPortCurrentMembership':vlanVoiceOUIBasedPortCurrentMembership,'vlanVoiceOUIBasedPortQosMode':vlanVoiceOUIBasedPortQosMode,'vlanVoiceOUIBasedAgingTimeout':vlanVoiceOUIBasedAgingTimeout})