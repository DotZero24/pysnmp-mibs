_K='btvAdapterIndex'
_J='btvTeamIndex'
_I='btpAdapterIndex'
_H='btpTeamIndex'
_G='standby'
_F='btTeamIndex'
_E='not-accessible'
_D='QLASP-Config-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Qlogic_ObjectIdentity=ObjectIdentity
qlogic=_Qlogic_ObjectIdentity((1,3,6,1,4,1,3873))
_Enet_ObjectIdentity=ObjectIdentity
enet=_Enet_ObjectIdentity((1,3,6,1,4,1,3873,1))
_Qlasp_ObjectIdentity=ObjectIdentity
qlasp=_Qlasp_ObjectIdentity((1,3,6,1,4,1,3873,1,2))
_QlaspConfig_ObjectIdentity=ObjectIdentity
qlaspConfig=_QlaspConfig_ObjectIdentity((1,3,6,1,4,1,3873,1,2,1))
_QlaspTeam_ObjectIdentity=ObjectIdentity
qlaspTeam=_QlaspTeam_ObjectIdentity((1,3,6,1,4,1,3873,1,2,1,1))
_BtTeamNumber_Type=Integer32
_BtTeamNumber_Object=MibScalar
btTeamNumber=_BtTeamNumber_Object((1,3,6,1,4,1,3873,1,2,1,1,1),_BtTeamNumber_Type())
btTeamNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:btTeamNumber.setStatus(_A)
_BtTeamTable_Object=MibTable
btTeamTable=_BtTeamTable_Object((1,3,6,1,4,1,3873,1,2,1,1,2))
if mibBuilder.loadTexts:btTeamTable.setStatus(_A)
_BtTeamEntry_Object=MibTableRow
btTeamEntry=_BtTeamEntry_Object((1,3,6,1,4,1,3873,1,2,1,1,2,1))
btTeamEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:btTeamEntry.setStatus(_A)
class _BtTeamIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BtTeamIndex_Type.__name__=_C
_BtTeamIndex_Object=MibTableColumn
btTeamIndex=_BtTeamIndex_Object((1,3,6,1,4,1,3873,1,2,1,1,2,1,1),_BtTeamIndex_Type())
btTeamIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:btTeamIndex.setStatus(_A)
_BtTeamName_Type=DisplayString
_BtTeamName_Object=MibTableColumn
btTeamName=_BtTeamName_Object((1,3,6,1,4,1,3873,1,2,1,1,2,1,2),_BtTeamName_Type())
btTeamName.setMaxAccess(_B)
if mibBuilder.loadTexts:btTeamName.setStatus(_A)
class _BtTeamType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,101,102,104)));namedValues=NamedValues(*(('team-SLB',100),('team-FEC-GEC',101),('team-802-3-AD',102),('team-SLB-AFD',104)))
_BtTeamType_Type.__name__=_C
_BtTeamType_Object=MibTableColumn
btTeamType=_BtTeamType_Object((1,3,6,1,4,1,3873,1,2,1,1,2,1,3),_BtTeamType_Type())
btTeamType.setMaxAccess(_B)
if mibBuilder.loadTexts:btTeamType.setStatus(_A)
_BtTeamMacAddress_Type=PhysAddress
_BtTeamMacAddress_Object=MibTableColumn
btTeamMacAddress=_BtTeamMacAddress_Object((1,3,6,1,4,1,3873,1,2,1,1,2,1,4),_BtTeamMacAddress_Type())
btTeamMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:btTeamMacAddress.setStatus(_A)
_BtPhyNumber_Type=Integer32
_BtPhyNumber_Object=MibTableColumn
btPhyNumber=_BtPhyNumber_Object((1,3,6,1,4,1,3873,1,2,1,1,2,1,5),_BtPhyNumber_Type())
btPhyNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:btPhyNumber.setStatus(_A)
_BtVirNumber_Type=Integer32
_BtVirNumber_Object=MibTableColumn
btVirNumber=_BtVirNumber_Object((1,3,6,1,4,1,3873,1,2,1,1,2,1,6),_BtVirNumber_Type())
btVirNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:btVirNumber.setStatus(_A)
class _BtMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('primaryMode',1),(_G,2)))
_BtMode_Type.__name__=_C
_BtMode_Object=MibTableColumn
btMode=_BtMode_Object((1,3,6,1,4,1,3873,1,2,1,1,2,1,7),_BtMode_Type())
btMode.setMaxAccess(_B)
if mibBuilder.loadTexts:btMode.setStatus(_A)
class _BtLiveLinkEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disabled',1),('enabled',2)))
_BtLiveLinkEnable_Type.__name__=_C
_BtLiveLinkEnable_Object=MibTableColumn
btLiveLinkEnable=_BtLiveLinkEnable_Object((1,3,6,1,4,1,3873,1,2,1,1,2,1,8),_BtLiveLinkEnable_Type())
btLiveLinkEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:btLiveLinkEnable.setStatus(_A)
_BtLinkPacketFrequency_Type=Integer32
_BtLinkPacketFrequency_Object=MibTableColumn
btLinkPacketFrequency=_BtLinkPacketFrequency_Object((1,3,6,1,4,1,3873,1,2,1,1,2,1,9),_BtLinkPacketFrequency_Type())
btLinkPacketFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:btLinkPacketFrequency.setStatus(_A)
_BtLinkMaxRetry_Type=Integer32
_BtLinkMaxRetry_Object=MibTableColumn
btLinkMaxRetry=_BtLinkMaxRetry_Object((1,3,6,1,4,1,3873,1,2,1,1,2,1,10),_BtLinkMaxRetry_Type())
btLinkMaxRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:btLinkMaxRetry.setStatus(_A)
_BtLinkRetryFrequency_Type=Integer32
_BtLinkRetryFrequency_Object=MibTableColumn
btLinkRetryFrequency=_BtLinkRetryFrequency_Object((1,3,6,1,4,1,3873,1,2,1,1,2,1,11),_BtLinkRetryFrequency_Type())
btLinkRetryFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:btLinkRetryFrequency.setStatus(_A)
_BtLinkTargetIpAddress1_Type=IpAddress
_BtLinkTargetIpAddress1_Object=MibTableColumn
btLinkTargetIpAddress1=_BtLinkTargetIpAddress1_Object((1,3,6,1,4,1,3873,1,2,1,1,2,1,12),_BtLinkTargetIpAddress1_Type())
btLinkTargetIpAddress1.setMaxAccess(_B)
if mibBuilder.loadTexts:btLinkTargetIpAddress1.setStatus(_A)
_BtLinkTargetIpAddress2_Type=IpAddress
_BtLinkTargetIpAddress2_Object=MibTableColumn
btLinkTargetIpAddress2=_BtLinkTargetIpAddress2_Object((1,3,6,1,4,1,3873,1,2,1,1,2,1,13),_BtLinkTargetIpAddress2_Type())
btLinkTargetIpAddress2.setMaxAccess(_B)
if mibBuilder.loadTexts:btLinkTargetIpAddress2.setStatus(_A)
_BtLinkTargetIpAddress3_Type=IpAddress
_BtLinkTargetIpAddress3_Object=MibTableColumn
btLinkTargetIpAddress3=_BtLinkTargetIpAddress3_Object((1,3,6,1,4,1,3873,1,2,1,1,2,1,14),_BtLinkTargetIpAddress3_Type())
btLinkTargetIpAddress3.setMaxAccess(_B)
if mibBuilder.loadTexts:btLinkTargetIpAddress3.setStatus(_A)
_BtLinkTargetIpAddress4_Type=IpAddress
_BtLinkTargetIpAddress4_Object=MibTableColumn
btLinkTargetIpAddress4=_BtLinkTargetIpAddress4_Object((1,3,6,1,4,1,3873,1,2,1,1,2,1,15),_BtLinkTargetIpAddress4_Type())
btLinkTargetIpAddress4.setMaxAccess(_B)
if mibBuilder.loadTexts:btLinkTargetIpAddress4.setStatus(_A)
_QlaspPhyAdapter_ObjectIdentity=ObjectIdentity
qlaspPhyAdapter=_QlaspPhyAdapter_ObjectIdentity((1,3,6,1,4,1,3873,1,2,1,2))
_BtPhyAdapterNumber_Type=Integer32
_BtPhyAdapterNumber_Object=MibScalar
btPhyAdapterNumber=_BtPhyAdapterNumber_Object((1,3,6,1,4,1,3873,1,2,1,2,1),_BtPhyAdapterNumber_Type())
btPhyAdapterNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:btPhyAdapterNumber.setStatus(_A)
_BtPhyAdapterTable_Object=MibTable
btPhyAdapterTable=_BtPhyAdapterTable_Object((1,3,6,1,4,1,3873,1,2,1,2,2))
if mibBuilder.loadTexts:btPhyAdapterTable.setStatus(_A)
_BtPhyAdapterEntry_Object=MibTableRow
btPhyAdapterEntry=_BtPhyAdapterEntry_Object((1,3,6,1,4,1,3873,1,2,1,2,2,1))
btPhyAdapterEntry.setIndexNames((0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:btPhyAdapterEntry.setStatus(_A)
class _BtpTeamIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BtpTeamIndex_Type.__name__=_C
_BtpTeamIndex_Object=MibTableColumn
btpTeamIndex=_BtpTeamIndex_Object((1,3,6,1,4,1,3873,1,2,1,2,2,1,1),_BtpTeamIndex_Type())
btpTeamIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:btpTeamIndex.setStatus(_A)
class _BtpAdapterIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BtpAdapterIndex_Type.__name__=_C
_BtpAdapterIndex_Object=MibTableColumn
btpAdapterIndex=_BtpAdapterIndex_Object((1,3,6,1,4,1,3873,1,2,1,2,2,1,2),_BtpAdapterIndex_Type())
btpAdapterIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:btpAdapterIndex.setStatus(_A)
_BtpAdapterDesc_Type=DisplayString
_BtpAdapterDesc_Object=MibTableColumn
btpAdapterDesc=_BtpAdapterDesc_Object((1,3,6,1,4,1,3873,1,2,1,2,2,1,3),_BtpAdapterDesc_Type())
btpAdapterDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:btpAdapterDesc.setStatus(_A)
class _BtpMemberType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,101)));namedValues=NamedValues(*(('load-balance',100),(_G,101)))
_BtpMemberType_Type.__name__=_C
_BtpMemberType_Object=MibTableColumn
btpMemberType=_BtpMemberType_Object((1,3,6,1,4,1,3873,1,2,1,2,2,1,4),_BtpMemberType_Type())
btpMemberType.setMaxAccess(_B)
if mibBuilder.loadTexts:btpMemberType.setStatus(_A)
_BtpMacAddress_Type=PhysAddress
_BtpMacAddress_Object=MibTableColumn
btpMacAddress=_BtpMacAddress_Object((1,3,6,1,4,1,3873,1,2,1,2,2,1,5),_BtpMacAddress_Type())
btpMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:btpMacAddress.setStatus(_A)
class _BtpMemberState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unknown',1),('link-up-not-join-traffic',2),('disable-not-join-traffic',3),('join-traffic',4)))
_BtpMemberState_Type.__name__=_C
_BtpMemberState_Object=MibTableColumn
btpMemberState=_BtpMemberState_Object((1,3,6,1,4,1,3873,1,2,1,2,2,1,6),_BtpMemberState_Type())
btpMemberState.setMaxAccess(_B)
if mibBuilder.loadTexts:btpMemberState.setStatus(_A)
_BtpLiveLinkIp_Type=IpAddress
_BtpLiveLinkIp_Object=MibTableColumn
btpLiveLinkIp=_BtpLiveLinkIp_Object((1,3,6,1,4,1,3873,1,2,1,2,2,1,7),_BtpLiveLinkIp_Type())
btpLiveLinkIp.setMaxAccess(_B)
if mibBuilder.loadTexts:btpLiveLinkIp.setStatus(_A)
_QlaspVirAdapter_ObjectIdentity=ObjectIdentity
qlaspVirAdapter=_QlaspVirAdapter_ObjectIdentity((1,3,6,1,4,1,3873,1,2,1,3))
_BtVirAdapterNumber_Type=Integer32
_BtVirAdapterNumber_Object=MibScalar
btVirAdapterNumber=_BtVirAdapterNumber_Object((1,3,6,1,4,1,3873,1,2,1,3,1),_BtVirAdapterNumber_Type())
btVirAdapterNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:btVirAdapterNumber.setStatus(_A)
_BtVirAdapterTable_Object=MibTable
btVirAdapterTable=_BtVirAdapterTable_Object((1,3,6,1,4,1,3873,1,2,1,3,2))
if mibBuilder.loadTexts:btVirAdapterTable.setStatus(_A)
_BtVirAdapterEntry_Object=MibTableRow
btVirAdapterEntry=_BtVirAdapterEntry_Object((1,3,6,1,4,1,3873,1,2,1,3,2,1))
btVirAdapterEntry.setIndexNames((0,_D,_J),(0,_D,_K))
if mibBuilder.loadTexts:btVirAdapterEntry.setStatus(_A)
class _BtvTeamIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BtvTeamIndex_Type.__name__=_C
_BtvTeamIndex_Object=MibTableColumn
btvTeamIndex=_BtvTeamIndex_Object((1,3,6,1,4,1,3873,1,2,1,3,2,1,1),_BtvTeamIndex_Type())
btvTeamIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:btvTeamIndex.setStatus(_A)
class _BtvAdapterIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BtvAdapterIndex_Type.__name__=_C
_BtvAdapterIndex_Object=MibTableColumn
btvAdapterIndex=_BtvAdapterIndex_Object((1,3,6,1,4,1,3873,1,2,1,3,2,1,2),_BtvAdapterIndex_Type())
btvAdapterIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:btvAdapterIndex.setStatus(_A)
_BtvAdapterDesc_Type=DisplayString
_BtvAdapterDesc_Object=MibTableColumn
btvAdapterDesc=_BtvAdapterDesc_Object((1,3,6,1,4,1,3873,1,2,1,3,2,1,3),_BtvAdapterDesc_Type())
btvAdapterDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:btvAdapterDesc.setStatus(_A)
_BtvVlanId_Type=Integer32
_BtvVlanId_Object=MibTableColumn
btvVlanId=_BtvVlanId_Object((1,3,6,1,4,1,3873,1,2,1,3,2,1,4),_BtvVlanId_Type())
btvVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:btvVlanId.setStatus(_A)
class _BtvLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('link-up',1),('link-fail',2)))
_BtvLinkStatus_Type.__name__=_C
_BtvLinkStatus_Object=MibTableColumn
btvLinkStatus=_BtvLinkStatus_Object((1,3,6,1,4,1,3873,1,2,1,3,2,1,5),_BtvLinkStatus_Type())
btvLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:btvLinkStatus.setStatus(_A)
_BtvIPAddress_Type=IpAddress
_BtvIPAddress_Object=MibTableColumn
btvIPAddress=_BtvIPAddress_Object((1,3,6,1,4,1,3873,1,2,1,3,2,1,6),_BtvIPAddress_Type())
btvIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:btvIPAddress.setStatus(_A)
_BtvSubnetMask_Type=IpAddress
_BtvSubnetMask_Object=MibTableColumn
btvSubnetMask=_BtvSubnetMask_Object((1,3,6,1,4,1,3873,1,2,1,3,2,1,7),_BtvSubnetMask_Type())
btvSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:btvSubnetMask.setStatus(_A)
_BtvPhysAddress_Type=PhysAddress
_BtvPhysAddress_Object=MibTableColumn
btvPhysAddress=_BtvPhysAddress_Object((1,3,6,1,4,1,3873,1,2,1,3,2,1,8),_BtvPhysAddress_Type())
btvPhysAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:btvPhysAddress.setStatus(_A)
_BtvLineSpeed_Type=DisplayString
_BtvLineSpeed_Object=MibTableColumn
btvLineSpeed=_BtvLineSpeed_Object((1,3,6,1,4,1,3873,1,2,1,3,2,1,9),_BtvLineSpeed_Type())
btvLineSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:btvLineSpeed.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'qlogic':qlogic,'enet':enet,'qlasp':qlasp,'qlaspConfig':qlaspConfig,'qlaspTeam':qlaspTeam,'btTeamNumber':btTeamNumber,'btTeamTable':btTeamTable,'btTeamEntry':btTeamEntry,_F:btTeamIndex,'btTeamName':btTeamName,'btTeamType':btTeamType,'btTeamMacAddress':btTeamMacAddress,'btPhyNumber':btPhyNumber,'btVirNumber':btVirNumber,'btMode':btMode,'btLiveLinkEnable':btLiveLinkEnable,'btLinkPacketFrequency':btLinkPacketFrequency,'btLinkMaxRetry':btLinkMaxRetry,'btLinkRetryFrequency':btLinkRetryFrequency,'btLinkTargetIpAddress1':btLinkTargetIpAddress1,'btLinkTargetIpAddress2':btLinkTargetIpAddress2,'btLinkTargetIpAddress3':btLinkTargetIpAddress3,'btLinkTargetIpAddress4':btLinkTargetIpAddress4,'qlaspPhyAdapter':qlaspPhyAdapter,'btPhyAdapterNumber':btPhyAdapterNumber,'btPhyAdapterTable':btPhyAdapterTable,'btPhyAdapterEntry':btPhyAdapterEntry,_H:btpTeamIndex,_I:btpAdapterIndex,'btpAdapterDesc':btpAdapterDesc,'btpMemberType':btpMemberType,'btpMacAddress':btpMacAddress,'btpMemberState':btpMemberState,'btpLiveLinkIp':btpLiveLinkIp,'qlaspVirAdapter':qlaspVirAdapter,'btVirAdapterNumber':btVirAdapterNumber,'btVirAdapterTable':btVirAdapterTable,'btVirAdapterEntry':btVirAdapterEntry,_J:btvTeamIndex,_K:btvAdapterIndex,'btvAdapterDesc':btvAdapterDesc,'btvVlanId':btvVlanId,'btvLinkStatus':btvLinkStatus,'btvIPAddress':btvIPAddress,'btvSubnetMask':btvSubnetMask,'btvPhysAddress':btvPhysAddress,'btvLineSpeed':btvLineSpeed})