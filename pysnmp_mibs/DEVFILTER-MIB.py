_P='aniDevFilterIfIdentifier'
_O='wireless-port6'
_N='wireless-port5'
_M='wireless-port4'
_L='wireless-port3'
_K='wireless-port2'
_J='wireless-port1'
_I='ethernet'
_H='aniDevFilterIdentifier'
_G='aniDevFilterIfIndex'
_F='DisplayString'
_E='OctetString'
_D='DEVFILTER-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
device,=mibBuilder.importSymbols('ANIROOT-MIB','device')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'MacAddress','PhysAddress','RowStatus','TextualConvention')
aniDevFilter=ModuleIdentity((1,3,6,1,4,1,4325,2,8))
_AniDevFilterTable_Object=MibTable
aniDevFilterTable=_AniDevFilterTable_Object((1,3,6,1,4,1,4325,2,8,1))
if mibBuilder.loadTexts:aniDevFilterTable.setStatus(_A)
_AniDevFilterEntry_Object=MibTableRow
aniDevFilterEntry=_AniDevFilterEntry_Object((1,3,6,1,4,1,4325,2,8,1,1))
aniDevFilterEntry.setIndexNames((0,_D,_G),(0,_D,_H))
if mibBuilder.loadTexts:aniDevFilterEntry.setStatus(_A)
class _AniDevFilterIfIndex_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),(_L,4),(_M,5),(_N,6),(_O,7)))
_AniDevFilterIfIndex_Type.__name__=_C
_AniDevFilterIfIndex_Object=MibTableColumn
aniDevFilterIfIndex=_AniDevFilterIfIndex_Object((1,3,6,1,4,1,4325,2,8,1,1,1),_AniDevFilterIfIndex_Type())
aniDevFilterIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevFilterIfIndex.setStatus(_A)
class _AniDevFilterIdentifier_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AniDevFilterIdentifier_Type.__name__=_C
_AniDevFilterIdentifier_Object=MibTableColumn
aniDevFilterIdentifier=_AniDevFilterIdentifier_Object((1,3,6,1,4,1,4325,2,8,1,1,2),_AniDevFilterIdentifier_Type())
aniDevFilterIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevFilterIdentifier.setStatus(_A)
class _AniDevFilterName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_AniDevFilterName_Type.__name__=_F
_AniDevFilterName_Object=MibTableColumn
aniDevFilterName=_AniDevFilterName_Object((1,3,6,1,4,1,4325,2,8,1,1,3),_AniDevFilterName_Type())
aniDevFilterName.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevFilterName.setStatus(_A)
class _AniDevFilterPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AniDevFilterPriority_Type.__name__=_C
_AniDevFilterPriority_Object=MibTableColumn
aniDevFilterPriority=_AniDevFilterPriority_Object((1,3,6,1,4,1,4325,2,8,1,1,4),_AniDevFilterPriority_Type())
aniDevFilterPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevFilterPriority.setStatus(_A)
class _AniDevFilterActivationState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inactive',1),('active',2)))
_AniDevFilterActivationState_Type.__name__=_C
_AniDevFilterActivationState_Object=MibTableColumn
aniDevFilterActivationState=_AniDevFilterActivationState_Object((1,3,6,1,4,1,4325,2,8,1,1,5),_AniDevFilterActivationState_Type())
aniDevFilterActivationState.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevFilterActivationState.setStatus(_A)
class _AniDevFilterPermission_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('block',1),('pass',2)))
_AniDevFilterPermission_Type.__name__=_C
_AniDevFilterPermission_Object=MibTableColumn
aniDevFilterPermission=_AniDevFilterPermission_Object((1,3,6,1,4,1,4325,2,8,1,1,6),_AniDevFilterPermission_Type())
aniDevFilterPermission.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevFilterPermission.setStatus(_A)
class _AniDevFilterIpProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,257))
_AniDevFilterIpProtocol_Type.__name__=_C
_AniDevFilterIpProtocol_Object=MibTableColumn
aniDevFilterIpProtocol=_AniDevFilterIpProtocol_Object((1,3,6,1,4,1,4325,2,8,1,1,7),_AniDevFilterIpProtocol_Type())
aniDevFilterIpProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevFilterIpProtocol.setStatus(_A)
_AniDevFilterIpSaddr_Type=IpAddress
_AniDevFilterIpSaddr_Object=MibTableColumn
aniDevFilterIpSaddr=_AniDevFilterIpSaddr_Object((1,3,6,1,4,1,4325,2,8,1,1,8),_AniDevFilterIpSaddr_Type())
aniDevFilterIpSaddr.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevFilterIpSaddr.setStatus(_A)
_AniDevFilterIpSmask_Type=IpAddress
_AniDevFilterIpSmask_Object=MibTableColumn
aniDevFilterIpSmask=_AniDevFilterIpSmask_Object((1,3,6,1,4,1,4325,2,8,1,1,9),_AniDevFilterIpSmask_Type())
aniDevFilterIpSmask.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevFilterIpSmask.setStatus(_A)
_AniDevFilterIpDaddr_Type=IpAddress
_AniDevFilterIpDaddr_Object=MibTableColumn
aniDevFilterIpDaddr=_AniDevFilterIpDaddr_Object((1,3,6,1,4,1,4325,2,8,1,1,10),_AniDevFilterIpDaddr_Type())
aniDevFilterIpDaddr.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevFilterIpDaddr.setStatus(_A)
_AniDevFilterIpDmask_Type=IpAddress
_AniDevFilterIpDmask_Object=MibTableColumn
aniDevFilterIpDmask=_AniDevFilterIpDmask_Object((1,3,6,1,4,1,4325,2,8,1,1,11),_AniDevFilterIpDmask_Type())
aniDevFilterIpDmask.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevFilterIpDmask.setStatus(_A)
class _AniDevFilterIpSourceStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AniDevFilterIpSourceStart_Type.__name__=_C
_AniDevFilterIpSourceStart_Object=MibTableColumn
aniDevFilterIpSourceStart=_AniDevFilterIpSourceStart_Object((1,3,6,1,4,1,4325,2,8,1,1,12),_AniDevFilterIpSourceStart_Type())
aniDevFilterIpSourceStart.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevFilterIpSourceStart.setStatus(_A)
class _AniDevFilterIpSourceEnd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AniDevFilterIpSourceEnd_Type.__name__=_C
_AniDevFilterIpSourceEnd_Object=MibTableColumn
aniDevFilterIpSourceEnd=_AniDevFilterIpSourceEnd_Object((1,3,6,1,4,1,4325,2,8,1,1,13),_AniDevFilterIpSourceEnd_Type())
aniDevFilterIpSourceEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevFilterIpSourceEnd.setStatus(_A)
class _AniDevFilterIpDestStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AniDevFilterIpDestStart_Type.__name__=_C
_AniDevFilterIpDestStart_Object=MibTableColumn
aniDevFilterIpDestStart=_AniDevFilterIpDestStart_Object((1,3,6,1,4,1,4325,2,8,1,1,14),_AniDevFilterIpDestStart_Type())
aniDevFilterIpDestStart.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevFilterIpDestStart.setStatus(_A)
class _AniDevFilterIpDestEnd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AniDevFilterIpDestEnd_Type.__name__=_C
_AniDevFilterIpDestEnd_Object=MibTableColumn
aniDevFilterIpDestEnd=_AniDevFilterIpDestEnd_Object((1,3,6,1,4,1,4325,2,8,1,1,15),_AniDevFilterIpDestEnd_Type())
aniDevFilterIpDestEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevFilterIpDestEnd.setStatus(_A)
_AniDevFilterIpOptions_Type=Integer32
_AniDevFilterIpOptions_Object=MibTableColumn
aniDevFilterIpOptions=_AniDevFilterIpOptions_Object((1,3,6,1,4,1,4325,2,8,1,1,16),_AniDevFilterIpOptions_Type())
aniDevFilterIpOptions.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevFilterIpOptions.setStatus(_A)
class _AniDevFilterIpSecOptions_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('top-secret',1),('secret',2),('confidential',3),('unclassified',4)))
_AniDevFilterIpSecOptions_Type.__name__=_C
_AniDevFilterIpSecOptions_Object=MibTableColumn
aniDevFilterIpSecOptions=_AniDevFilterIpSecOptions_Object((1,3,6,1,4,1,4325,2,8,1,1,17),_AniDevFilterIpSecOptions_Type())
aniDevFilterIpSecOptions.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevFilterIpSecOptions.setStatus(_A)
_AniDevFilterIcmpMsgType_Type=Integer32
_AniDevFilterIcmpMsgType_Object=MibTableColumn
aniDevFilterIcmpMsgType=_AniDevFilterIcmpMsgType_Object((1,3,6,1,4,1,4325,2,8,1,1,18),_AniDevFilterIcmpMsgType_Type())
aniDevFilterIcmpMsgType.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevFilterIcmpMsgType.setStatus(_A)
_AniDevFilterIcmpSubcode_Type=Integer32
_AniDevFilterIcmpSubcode_Object=MibTableColumn
aniDevFilterIcmpSubcode=_AniDevFilterIcmpSubcode_Object((1,3,6,1,4,1,4325,2,8,1,1,19),_AniDevFilterIcmpSubcode_Type())
aniDevFilterIcmpSubcode.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevFilterIcmpSubcode.setStatus(_A)
_AniDevFilterTcpFlags_Type=Integer32
_AniDevFilterTcpFlags_Object=MibTableColumn
aniDevFilterTcpFlags=_AniDevFilterTcpFlags_Object((1,3,6,1,4,1,4325,2,8,1,1,20),_AniDevFilterTcpFlags_Type())
aniDevFilterTcpFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevFilterTcpFlags.setStatus(_A)
class _AniDevFilterDestMacMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_AniDevFilterDestMacMask_Type.__name__=_E
_AniDevFilterDestMacMask_Object=MibTableColumn
aniDevFilterDestMacMask=_AniDevFilterDestMacMask_Object((1,3,6,1,4,1,4325,2,8,1,1,21),_AniDevFilterDestMacMask_Type())
aniDevFilterDestMacMask.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevFilterDestMacMask.setStatus(_A)
_AniDevFilterSourceMac_Type=MacAddress
_AniDevFilterSourceMac_Object=MibTableColumn
aniDevFilterSourceMac=_AniDevFilterSourceMac_Object((1,3,6,1,4,1,4325,2,8,1,1,22),_AniDevFilterSourceMac_Type())
aniDevFilterSourceMac.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevFilterSourceMac.setStatus(_A)
_AniDevFilterEnetType_Type=DisplayString
_AniDevFilterEnetType_Object=MibTableColumn
aniDevFilterEnetType=_AniDevFilterEnetType_Object((1,3,6,1,4,1,4325,2,8,1,1,23),_AniDevFilterEnetType_Type())
aniDevFilterEnetType.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevFilterEnetType.setStatus(_A)
_AniDevFilterLlcDSAP_Type=DisplayString
_AniDevFilterLlcDSAP_Object=MibTableColumn
aniDevFilterLlcDSAP=_AniDevFilterLlcDSAP_Object((1,3,6,1,4,1,4325,2,8,1,1,24),_AniDevFilterLlcDSAP_Type())
aniDevFilterLlcDSAP.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevFilterLlcDSAP.setStatus(_A)
_AniDevFilterLlcSSAP_Type=DisplayString
_AniDevFilterLlcSSAP_Object=MibTableColumn
aniDevFilterLlcSSAP=_AniDevFilterLlcSSAP_Object((1,3,6,1,4,1,4325,2,8,1,1,25),_AniDevFilterLlcSSAP_Type())
aniDevFilterLlcSSAP.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevFilterLlcSSAP.setStatus(_A)
_AniDevFilterLlcControl_Type=DisplayString
_AniDevFilterLlcControl_Object=MibTableColumn
aniDevFilterLlcControl=_AniDevFilterLlcControl_Object((1,3,6,1,4,1,4325,2,8,1,1,26),_AniDevFilterLlcControl_Type())
aniDevFilterLlcControl.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevFilterLlcControl.setStatus(_A)
_AniDevFilterLocalCode_Type=DisplayString
_AniDevFilterLocalCode_Object=MibTableColumn
aniDevFilterLocalCode=_AniDevFilterLocalCode_Object((1,3,6,1,4,1,4325,2,8,1,1,27),_AniDevFilterLocalCode_Type())
aniDevFilterLocalCode.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevFilterLocalCode.setStatus(_A)
_AniDevFilterRowStatus_Type=RowStatus
_AniDevFilterRowStatus_Object=MibTableColumn
aniDevFilterRowStatus=_AniDevFilterRowStatus_Object((1,3,6,1,4,1,4325,2,8,1,1,28),_AniDevFilterRowStatus_Type())
aniDevFilterRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevFilterRowStatus.setStatus(_A)
class _AniDevFilterUserPriorityHi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AniDevFilterUserPriorityHi_Type.__name__=_C
_AniDevFilterUserPriorityHi_Object=MibTableColumn
aniDevFilterUserPriorityHi=_AniDevFilterUserPriorityHi_Object((1,3,6,1,4,1,4325,2,8,1,1,29),_AniDevFilterUserPriorityHi_Type())
aniDevFilterUserPriorityHi.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevFilterUserPriorityHi.setStatus(_A)
class _AniDevFilterUserPriorityLo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AniDevFilterUserPriorityLo_Type.__name__=_C
_AniDevFilterUserPriorityLo_Object=MibTableColumn
aniDevFilterUserPriorityLo=_AniDevFilterUserPriorityLo_Object((1,3,6,1,4,1,4325,2,8,1,1,30),_AniDevFilterUserPriorityLo_Type())
aniDevFilterUserPriorityLo.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevFilterUserPriorityLo.setStatus(_A)
class _AniDevFilterVlanIdStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_AniDevFilterVlanIdStart_Type.__name__=_C
_AniDevFilterVlanIdStart_Object=MibTableColumn
aniDevFilterVlanIdStart=_AniDevFilterVlanIdStart_Object((1,3,6,1,4,1,4325,2,8,1,1,31),_AniDevFilterVlanIdStart_Type())
aniDevFilterVlanIdStart.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevFilterVlanIdStart.setStatus(_A)
class _AniDevFilterVlanIdEnd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_AniDevFilterVlanIdEnd_Type.__name__=_C
_AniDevFilterVlanIdEnd_Object=MibTableColumn
aniDevFilterVlanIdEnd=_AniDevFilterVlanIdEnd_Object((1,3,6,1,4,1,4325,2,8,1,1,32),_AniDevFilterVlanIdEnd_Type())
aniDevFilterVlanIdEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevFilterVlanIdEnd.setStatus(_A)
_AniDevFilterIfTable_Object=MibTable
aniDevFilterIfTable=_AniDevFilterIfTable_Object((1,3,6,1,4,1,4325,2,8,2))
if mibBuilder.loadTexts:aniDevFilterIfTable.setStatus(_A)
_AniDevFilterIfEntry_Object=MibTableRow
aniDevFilterIfEntry=_AniDevFilterIfEntry_Object((1,3,6,1,4,1,4325,2,8,2,1))
aniDevFilterIfEntry.setIndexNames((0,_D,_P))
if mibBuilder.loadTexts:aniDevFilterIfEntry.setStatus(_A)
class _AniDevFilterIfIdentifier_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),(_L,4),(_M,5),(_N,6),(_O,7)))
_AniDevFilterIfIdentifier_Type.__name__=_C
_AniDevFilterIfIdentifier_Object=MibTableColumn
aniDevFilterIfIdentifier=_AniDevFilterIfIdentifier_Object((1,3,6,1,4,1,4325,2,8,2,1,1),_AniDevFilterIfIdentifier_Type())
aniDevFilterIfIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevFilterIfIdentifier.setStatus(_A)
class _AniDevFilterIfFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_AniDevFilterIfFlag_Type.__name__=_C
_AniDevFilterIfFlag_Object=MibTableColumn
aniDevFilterIfFlag=_AniDevFilterIfFlag_Object((1,3,6,1,4,1,4325,2,8,2,1,2),_AniDevFilterIfFlag_Type())
aniDevFilterIfFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevFilterIfFlag.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'aniDevFilter':aniDevFilter,'aniDevFilterTable':aniDevFilterTable,'aniDevFilterEntry':aniDevFilterEntry,_G:aniDevFilterIfIndex,_H:aniDevFilterIdentifier,'aniDevFilterName':aniDevFilterName,'aniDevFilterPriority':aniDevFilterPriority,'aniDevFilterActivationState':aniDevFilterActivationState,'aniDevFilterPermission':aniDevFilterPermission,'aniDevFilterIpProtocol':aniDevFilterIpProtocol,'aniDevFilterIpSaddr':aniDevFilterIpSaddr,'aniDevFilterIpSmask':aniDevFilterIpSmask,'aniDevFilterIpDaddr':aniDevFilterIpDaddr,'aniDevFilterIpDmask':aniDevFilterIpDmask,'aniDevFilterIpSourceStart':aniDevFilterIpSourceStart,'aniDevFilterIpSourceEnd':aniDevFilterIpSourceEnd,'aniDevFilterIpDestStart':aniDevFilterIpDestStart,'aniDevFilterIpDestEnd':aniDevFilterIpDestEnd,'aniDevFilterIpOptions':aniDevFilterIpOptions,'aniDevFilterIpSecOptions':aniDevFilterIpSecOptions,'aniDevFilterIcmpMsgType':aniDevFilterIcmpMsgType,'aniDevFilterIcmpSubcode':aniDevFilterIcmpSubcode,'aniDevFilterTcpFlags':aniDevFilterTcpFlags,'aniDevFilterDestMacMask':aniDevFilterDestMacMask,'aniDevFilterSourceMac':aniDevFilterSourceMac,'aniDevFilterEnetType':aniDevFilterEnetType,'aniDevFilterLlcDSAP':aniDevFilterLlcDSAP,'aniDevFilterLlcSSAP':aniDevFilterLlcSSAP,'aniDevFilterLlcControl':aniDevFilterLlcControl,'aniDevFilterLocalCode':aniDevFilterLocalCode,'aniDevFilterRowStatus':aniDevFilterRowStatus,'aniDevFilterUserPriorityHi':aniDevFilterUserPriorityHi,'aniDevFilterUserPriorityLo':aniDevFilterUserPriorityLo,'aniDevFilterVlanIdStart':aniDevFilterVlanIdStart,'aniDevFilterVlanIdEnd':aniDevFilterVlanIdEnd,'aniDevFilterIfTable':aniDevFilterIfTable,'aniDevFilterIfEntry':aniDevFilterIfEntry,_P:aniDevFilterIfIdentifier,'aniDevFilterIfFlag':aniDevFilterIfFlag})