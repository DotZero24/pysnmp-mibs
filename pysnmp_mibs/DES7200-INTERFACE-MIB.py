_A2='myIfAvailableBWMibGroup'
_A1='myIfLineDetectGroup'
_A0='myIfMTUMibGroup'
_z='myPortTypeChooseMibGroup'
_y='myInterfaceMIBGroup'
_x='lineDetectPosition'
_w='lineDetectStatus'
_v='myIfAvailableBWIfBW'
_u='myIfLineDetect'
_t='myIfMTU'
_s='myPortTypeChooseType'
_r='myGlobalIfDisableRecovery'
_q='myIfErrorStatus'
_p='myIfStatusLoopBackExamine'
_o='myIfIpEntryStatus'
_n='myIfIpMask'
_m='myIfMediumType'
_l='myIfEntryStatus'
_k='myIfCounterClear'
_j='myIfMode'
_i='myIfLayer'
_h='myIfIpBroadcast'
_g='myIfManageStatus'
_f='myIfOperDuplex'
_e='myIfOperSpeed'
_d='myIfAdminDuplex'
_c='myIfAdminSpeed'
_b='myIfFlowControlOperStatus'
_a='myIfFlowControlAdminStatus'
_Z='myIfPortType'
_Y='accessible-for-notify'
_X='copper'
_W='read-create'
_V='speed10Gb'
_U='speed1000Mb'
_T='speed100Mb'
_S='speed10Mb'
_R='EnabledStatus'
_Q='ifIndex'
_P='IF-MIB'
_O='myIfAvailableBWIfIndex'
_N='myIfMTUIndex'
_M='myPortTypeChooseIndex'
_L='myIfStatusIndex'
_K='myIfIp'
_J='myIfIpId'
_I='myIfIpIfIndex'
_H='autonego'
_G='myIfIndex'
_F='unknown'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='DES7200-INTERFACE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
myMgmt,=mibBuilder.importSymbols('DES7200-SMI','myMgmt')
ConfigStatus,IfIndex,MemberMap=mibBuilder.importSymbols('DES7200-TC','ConfigStatus','IfIndex','MemberMap')
ifIndex,=mibBuilder.importSymbols(_P,_Q)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_R)
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
myInterfaceMIB=ModuleIdentity((1,3,6,1,4,1,171,10,97,2,10))
if mibBuilder.loadTexts:myInterfaceMIB.setRevisions(('2002-03-20 00:00',))
_MyIfConfigMIBObjects_ObjectIdentity=ObjectIdentity
myIfConfigMIBObjects=_MyIfConfigMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,10,1))
_MyIfTable_Object=MibTable
myIfTable=_MyIfTable_Object((1,3,6,1,4,1,171,10,97,2,10,1,1))
if mibBuilder.loadTexts:myIfTable.setStatus(_A)
_MyIfEntry_Object=MibTableRow
myIfEntry=_MyIfEntry_Object((1,3,6,1,4,1,171,10,97,2,10,1,1,1))
myIfEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:myIfEntry.setStatus(_A)
_MyIfIndex_Type=IfIndex
_MyIfIndex_Object=MibTableColumn
myIfIndex=_MyIfIndex_Object((1,3,6,1,4,1,171,10,97,2,10,1,1,1,1),_MyIfIndex_Type())
myIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:myIfIndex.setStatus(_A)
class _MyIfPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)));namedValues=NamedValues(*((_F,1),('port10M100MBASETX',2),('port100MBASEFXL',3),('port100MBASEFXS',4),('port1000MBASESX',5),('port1000MBASELX',6),('port1000MBASETX',7),('portGBIC',8),('port100MBASEFX',9),('port1000MBASEFX',10),('portSFP',11),('port10GBASESR',12),('port10GBASELR',13),('port10GBASEER',14),('port10GBASELX4',15),('port10GBASESW',16),('port10GBASELW',17),('port10GBASEEW',18),('port10GBASE',19)))
_MyIfPortType_Type.__name__=_D
_MyIfPortType_Object=MibTableColumn
myIfPortType=_MyIfPortType_Object((1,3,6,1,4,1,171,10,97,2,10,1,1,1,2),_MyIfPortType_Type())
myIfPortType.setMaxAccess(_C)
if mibBuilder.loadTexts:myIfPortType.setStatus(_A)
class _MyIfFlowControlAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('enabled',1),('disabled',2),(_H,3),(_F,4)))
_MyIfFlowControlAdminStatus_Type.__name__=_D
_MyIfFlowControlAdminStatus_Object=MibTableColumn
myIfFlowControlAdminStatus=_MyIfFlowControlAdminStatus_Object((1,3,6,1,4,1,171,10,97,2,10,1,1,1,3),_MyIfFlowControlAdminStatus_Type())
myIfFlowControlAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:myIfFlowControlAdminStatus.setStatus(_A)
_MyIfFlowControlOperStatus_Type=EnabledStatus
_MyIfFlowControlOperStatus_Object=MibTableColumn
myIfFlowControlOperStatus=_MyIfFlowControlOperStatus_Object((1,3,6,1,4,1,171,10,97,2,10,1,1,1,4),_MyIfFlowControlOperStatus_Type())
myIfFlowControlOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:myIfFlowControlOperStatus.setStatus(_A)
class _MyIfAdminSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_S,1),(_T,2),(_U,3),(_H,4),(_V,5),(_F,6)))
_MyIfAdminSpeed_Type.__name__=_D
_MyIfAdminSpeed_Object=MibTableColumn
myIfAdminSpeed=_MyIfAdminSpeed_Object((1,3,6,1,4,1,171,10,97,2,10,1,1,1,5),_MyIfAdminSpeed_Type())
myIfAdminSpeed.setMaxAccess(_E)
if mibBuilder.loadTexts:myIfAdminSpeed.setStatus(_A)
class _MyIfAdminDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('full',1),('half',2),(_H,3),(_F,4)))
_MyIfAdminDuplex_Type.__name__=_D
_MyIfAdminDuplex_Object=MibTableColumn
myIfAdminDuplex=_MyIfAdminDuplex_Object((1,3,6,1,4,1,171,10,97,2,10,1,1,1,6),_MyIfAdminDuplex_Type())
myIfAdminDuplex.setMaxAccess(_E)
if mibBuilder.loadTexts:myIfAdminDuplex.setStatus(_A)
class _MyIfOperSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_S,1),(_T,2),(_U,3),(_F,4),(_V,5)))
_MyIfOperSpeed_Type.__name__=_D
_MyIfOperSpeed_Object=MibTableColumn
myIfOperSpeed=_MyIfOperSpeed_Object((1,3,6,1,4,1,171,10,97,2,10,1,1,1,7),_MyIfOperSpeed_Type())
myIfOperSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:myIfOperSpeed.setStatus(_A)
class _MyIfOperDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('full',1),('half',2),(_F,3)))
_MyIfOperDuplex_Type.__name__=_D
_MyIfOperDuplex_Object=MibTableColumn
myIfOperDuplex=_MyIfOperDuplex_Object((1,3,6,1,4,1,171,10,97,2,10,1,1,1,8),_MyIfOperDuplex_Type())
myIfOperDuplex.setMaxAccess(_C)
if mibBuilder.loadTexts:myIfOperDuplex.setStatus(_A)
class _MyIfManageStatus_Type(EnabledStatus):defaultValue=1
_MyIfManageStatus_Type.__name__=_R
_MyIfManageStatus_Object=MibTableColumn
myIfManageStatus=_MyIfManageStatus_Object((1,3,6,1,4,1,171,10,97,2,10,1,1,1,9),_MyIfManageStatus_Type())
myIfManageStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:myIfManageStatus.setStatus(_A)
_MyIfIpBroadcast_Type=IpAddress
_MyIfIpBroadcast_Object=MibTableColumn
myIfIpBroadcast=_MyIfIpBroadcast_Object((1,3,6,1,4,1,171,10,97,2,10,1,1,1,10),_MyIfIpBroadcast_Type())
myIfIpBroadcast.setMaxAccess(_E)
if mibBuilder.loadTexts:myIfIpBroadcast.setStatus(_A)
class _MyIfLayer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('layer-2',1),('layer-3',2)))
_MyIfLayer_Type.__name__=_D
_MyIfLayer_Object=MibTableColumn
myIfLayer=_MyIfLayer_Object((1,3,6,1,4,1,171,10,97,2,10,1,1,1,11),_MyIfLayer_Type())
myIfLayer.setMaxAccess(_E)
if mibBuilder.loadTexts:myIfLayer.setStatus(_A)
class _MyIfMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('access',1),('trunk',2),('dot1q-tunnel',3),('hybrid',4),('other',5),('uplink',6),('host',7),('promiscuous',8)))
_MyIfMode_Type.__name__=_D
_MyIfMode_Object=MibTableColumn
myIfMode=_MyIfMode_Object((1,3,6,1,4,1,171,10,97,2,10,1,1,1,12),_MyIfMode_Type())
myIfMode.setMaxAccess(_E)
if mibBuilder.loadTexts:myIfMode.setStatus(_A)
_MyIfCounterClear_Type=Integer32
_MyIfCounterClear_Object=MibTableColumn
myIfCounterClear=_MyIfCounterClear_Object((1,3,6,1,4,1,171,10,97,2,10,1,1,1,13),_MyIfCounterClear_Type())
myIfCounterClear.setMaxAccess(_E)
if mibBuilder.loadTexts:myIfCounterClear.setStatus(_A)
_MyIfEntryStatus_Type=ConfigStatus
_MyIfEntryStatus_Object=MibTableColumn
myIfEntryStatus=_MyIfEntryStatus_Object((1,3,6,1,4,1,171,10,97,2,10,1,1,1,14),_MyIfEntryStatus_Type())
myIfEntryStatus.setMaxAccess(_W)
if mibBuilder.loadTexts:myIfEntryStatus.setStatus(_A)
class _MyIfMediumType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_X,1),('fiber',2)))
_MyIfMediumType_Type.__name__=_D
_MyIfMediumType_Object=MibTableColumn
myIfMediumType=_MyIfMediumType_Object((1,3,6,1,4,1,171,10,97,2,10,1,1,1,15),_MyIfMediumType_Type())
myIfMediumType.setMaxAccess(_E)
if mibBuilder.loadTexts:myIfMediumType.setStatus(_A)
_MyIfIpTable_Object=MibTable
myIfIpTable=_MyIfIpTable_Object((1,3,6,1,4,1,171,10,97,2,10,1,2))
if mibBuilder.loadTexts:myIfIpTable.setStatus(_A)
_MyIfIpEntry_Object=MibTableRow
myIfIpEntry=_MyIfIpEntry_Object((1,3,6,1,4,1,171,10,97,2,10,1,2,1))
myIfIpEntry.setIndexNames((0,_B,_I),(0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:myIfIpEntry.setStatus(_A)
_MyIfIpIfIndex_Type=IfIndex
_MyIfIpIfIndex_Object=MibTableColumn
myIfIpIfIndex=_MyIfIpIfIndex_Object((1,3,6,1,4,1,171,10,97,2,10,1,2,1,1),_MyIfIpIfIndex_Type())
myIfIpIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:myIfIpIfIndex.setStatus(_A)
class _MyIfIpId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('primary',1),('secondary',2)))
_MyIfIpId_Type.__name__=_D
_MyIfIpId_Object=MibTableColumn
myIfIpId=_MyIfIpId_Object((1,3,6,1,4,1,171,10,97,2,10,1,2,1,2),_MyIfIpId_Type())
myIfIpId.setMaxAccess(_C)
if mibBuilder.loadTexts:myIfIpId.setStatus(_A)
_MyIfIp_Type=IpAddress
_MyIfIp_Object=MibTableColumn
myIfIp=_MyIfIp_Object((1,3,6,1,4,1,171,10,97,2,10,1,2,1,3),_MyIfIp_Type())
myIfIp.setMaxAccess(_C)
if mibBuilder.loadTexts:myIfIp.setStatus(_A)
_MyIfIpMask_Type=IpAddress
_MyIfIpMask_Object=MibTableColumn
myIfIpMask=_MyIfIpMask_Object((1,3,6,1,4,1,171,10,97,2,10,1,2,1,4),_MyIfIpMask_Type())
myIfIpMask.setMaxAccess(_E)
if mibBuilder.loadTexts:myIfIpMask.setStatus(_A)
_MyIfIpEntryStatus_Type=RowStatus
_MyIfIpEntryStatus_Object=MibTableColumn
myIfIpEntryStatus=_MyIfIpEntryStatus_Object((1,3,6,1,4,1,171,10,97,2,10,1,2,1,5),_MyIfIpEntryStatus_Type())
myIfIpEntryStatus.setMaxAccess(_W)
if mibBuilder.loadTexts:myIfIpEntryStatus.setStatus(_A)
_MyIfStatusTable_Object=MibTable
myIfStatusTable=_MyIfStatusTable_Object((1,3,6,1,4,1,171,10,97,2,10,1,3))
if mibBuilder.loadTexts:myIfStatusTable.setStatus(_A)
_MyIfStatusEntry_Object=MibTableRow
myIfStatusEntry=_MyIfStatusEntry_Object((1,3,6,1,4,1,171,10,97,2,10,1,3,1))
myIfStatusEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:myIfStatusEntry.setStatus(_A)
_MyIfStatusIndex_Type=IfIndex
_MyIfStatusIndex_Object=MibTableColumn
myIfStatusIndex=_MyIfStatusIndex_Object((1,3,6,1,4,1,171,10,97,2,10,1,3,1,1),_MyIfStatusIndex_Type())
myIfStatusIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:myIfStatusIndex.setStatus(_A)
_MyIfStatusLoopBackExamine_Type=Integer32
_MyIfStatusLoopBackExamine_Object=MibTableColumn
myIfStatusLoopBackExamine=_MyIfStatusLoopBackExamine_Object((1,3,6,1,4,1,171,10,97,2,10,1,3,1,2),_MyIfStatusLoopBackExamine_Type())
myIfStatusLoopBackExamine.setMaxAccess(_E)
if mibBuilder.loadTexts:myIfStatusLoopBackExamine.setStatus(_A)
class _MyIfErrorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('no-error',1),('err-disable-bpduguard',2),('err-disable-ptsecurity',3)))
_MyIfErrorStatus_Type.__name__=_D
_MyIfErrorStatus_Object=MibTableColumn
myIfErrorStatus=_MyIfErrorStatus_Object((1,3,6,1,4,1,171,10,97,2,10,1,3,1,3),_MyIfErrorStatus_Type())
myIfErrorStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:myIfErrorStatus.setStatus(_A)
_MyIfLineDetect_Type=Integer32
_MyIfLineDetect_Object=MibTableColumn
myIfLineDetect=_MyIfLineDetect_Object((1,3,6,1,4,1,171,10,97,2,10,1,3,1,4),_MyIfLineDetect_Type())
myIfLineDetect.setMaxAccess(_C)
if mibBuilder.loadTexts:myIfLineDetect.setStatus(_A)
_MyGlobalIfDisableRecovery_Type=Integer32
_MyGlobalIfDisableRecovery_Object=MibScalar
myGlobalIfDisableRecovery=_MyGlobalIfDisableRecovery_Object((1,3,6,1,4,1,171,10,97,2,10,1,4),_MyGlobalIfDisableRecovery_Type())
myGlobalIfDisableRecovery.setMaxAccess(_E)
if mibBuilder.loadTexts:myGlobalIfDisableRecovery.setStatus(_A)
_MyPortTypeChooseTable_Object=MibTable
myPortTypeChooseTable=_MyPortTypeChooseTable_Object((1,3,6,1,4,1,171,10,97,2,10,1,5))
if mibBuilder.loadTexts:myPortTypeChooseTable.setStatus(_A)
_MyPortTypeChooseEntry_Object=MibTableRow
myPortTypeChooseEntry=_MyPortTypeChooseEntry_Object((1,3,6,1,4,1,171,10,97,2,10,1,5,1))
myPortTypeChooseEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:myPortTypeChooseEntry.setStatus(_A)
_MyPortTypeChooseIndex_Type=IfIndex
_MyPortTypeChooseIndex_Object=MibTableColumn
myPortTypeChooseIndex=_MyPortTypeChooseIndex_Object((1,3,6,1,4,1,171,10,97,2,10,1,5,1,1),_MyPortTypeChooseIndex_Type())
myPortTypeChooseIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:myPortTypeChooseIndex.setStatus(_A)
class _MyPortTypeChooseType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fiber',1),(_X,2)))
_MyPortTypeChooseType_Type.__name__=_D
_MyPortTypeChooseType_Object=MibTableColumn
myPortTypeChooseType=_MyPortTypeChooseType_Object((1,3,6,1,4,1,171,10,97,2,10,1,5,1,2),_MyPortTypeChooseType_Type())
myPortTypeChooseType.setMaxAccess(_C)
if mibBuilder.loadTexts:myPortTypeChooseType.setStatus(_A)
_MyIfMTUTable_Object=MibTable
myIfMTUTable=_MyIfMTUTable_Object((1,3,6,1,4,1,171,10,97,2,10,1,6))
if mibBuilder.loadTexts:myIfMTUTable.setStatus(_A)
_MyIfMTUEntry_Object=MibTableRow
myIfMTUEntry=_MyIfMTUEntry_Object((1,3,6,1,4,1,171,10,97,2,10,1,6,1))
myIfMTUEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:myIfMTUEntry.setStatus(_A)
_MyIfMTUIndex_Type=IfIndex
_MyIfMTUIndex_Object=MibTableColumn
myIfMTUIndex=_MyIfMTUIndex_Object((1,3,6,1,4,1,171,10,97,2,10,1,6,1,1),_MyIfMTUIndex_Type())
myIfMTUIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:myIfMTUIndex.setStatus(_A)
_MyIfMTU_Type=Integer32
_MyIfMTU_Object=MibTableColumn
myIfMTU=_MyIfMTU_Object((1,3,6,1,4,1,171,10,97,2,10,1,6,1,2),_MyIfMTU_Type())
myIfMTU.setMaxAccess(_E)
if mibBuilder.loadTexts:myIfMTU.setStatus(_A)
_MyIfAvailableBWTable_Object=MibTable
myIfAvailableBWTable=_MyIfAvailableBWTable_Object((1,3,6,1,4,1,171,10,97,2,10,1,7))
if mibBuilder.loadTexts:myIfAvailableBWTable.setStatus(_A)
_MyIfAvailableBWEntry_Object=MibTableRow
myIfAvailableBWEntry=_MyIfAvailableBWEntry_Object((1,3,6,1,4,1,171,10,97,2,10,1,7,1))
myIfAvailableBWEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:myIfAvailableBWEntry.setStatus(_A)
_MyIfAvailableBWIfIndex_Type=IfIndex
_MyIfAvailableBWIfIndex_Object=MibTableColumn
myIfAvailableBWIfIndex=_MyIfAvailableBWIfIndex_Object((1,3,6,1,4,1,171,10,97,2,10,1,7,1,1),_MyIfAvailableBWIfIndex_Type())
myIfAvailableBWIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:myIfAvailableBWIfIndex.setStatus(_A)
_MyIfAvailableBWIfBW_Type=Gauge32
_MyIfAvailableBWIfBW_Object=MibTableColumn
myIfAvailableBWIfBW=_MyIfAvailableBWIfBW_Object((1,3,6,1,4,1,171,10,97,2,10,1,7,1,2),_MyIfAvailableBWIfBW_Type())
myIfAvailableBWIfBW.setMaxAccess(_C)
if mibBuilder.loadTexts:myIfAvailableBWIfBW.setStatus(_A)
_MyInterfaceTraps_ObjectIdentity=ObjectIdentity
myInterfaceTraps=_MyInterfaceTraps_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,10,2))
class _LineDetectStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ok',1),('open',2),('short',3)))
_LineDetectStatus_Type.__name__=_D
_LineDetectStatus_Object=MibScalar
lineDetectStatus=_LineDetectStatus_Object((1,3,6,1,4,1,171,10,97,2,10,2,1),_LineDetectStatus_Type())
lineDetectStatus.setMaxAccess(_Y)
if mibBuilder.loadTexts:lineDetectStatus.setStatus(_A)
_LineDetectPosition_Type=Integer32
_LineDetectPosition_Object=MibScalar
lineDetectPosition=_LineDetectPosition_Object((1,3,6,1,4,1,171,10,97,2,10,2,2),_LineDetectPosition_Type())
lineDetectPosition.setMaxAccess(_Y)
if mibBuilder.loadTexts:lineDetectPosition.setStatus(_A)
_MyInterfaceMIBConformance_ObjectIdentity=ObjectIdentity
myInterfaceMIBConformance=_MyInterfaceMIBConformance_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,10,3))
_MyInterfaceMIBCompliances_ObjectIdentity=ObjectIdentity
myInterfaceMIBCompliances=_MyInterfaceMIBCompliances_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,10,3,1))
_MyInterfaceMIBGroups_ObjectIdentity=ObjectIdentity
myInterfaceMIBGroups=_MyInterfaceMIBGroups_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,10,3,2))
myInterfaceMIBGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,10,3,2,1))
myInterfaceMIBGroup.setObjects(*((_B,_G),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_I),(_B,_J),(_B,_K),(_B,_n),(_B,_o),(_B,_L),(_B,_p),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:myInterfaceMIBGroup.setStatus(_A)
myPortTypeChooseMibGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,10,3,2,2))
myPortTypeChooseMibGroup.setObjects(*((_B,_M),(_B,_s)))
if mibBuilder.loadTexts:myPortTypeChooseMibGroup.setStatus(_A)
myIfMTUMibGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,10,3,2,3))
myIfMTUMibGroup.setObjects(*((_B,_N),(_B,_t)))
if mibBuilder.loadTexts:myIfMTUMibGroup.setStatus(_A)
myIfLineDetectGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,10,3,2,4))
myIfLineDetectGroup.setObjects((_B,_u))
if mibBuilder.loadTexts:myIfLineDetectGroup.setStatus(_A)
myIfAvailableBWMibGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,10,3,2,5))
myIfAvailableBWMibGroup.setObjects(*((_B,_O),(_B,_v)))
if mibBuilder.loadTexts:myIfAvailableBWMibGroup.setStatus(_A)
lineQualityDetect=NotificationType((1,3,6,1,4,1,171,10,97,2,10,2,3))
lineQualityDetect.setObjects(*((_P,_Q),(_B,_w),(_B,_x)))
if mibBuilder.loadTexts:lineQualityDetect.setStatus(_A)
myInterfaceMIBCompliance=ModuleCompliance((1,3,6,1,4,1,171,10,97,2,10,3,1,1))
myInterfaceMIBCompliance.setObjects(*((_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:myInterfaceMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'myInterfaceMIB':myInterfaceMIB,'myIfConfigMIBObjects':myIfConfigMIBObjects,'myIfTable':myIfTable,'myIfEntry':myIfEntry,_G:myIfIndex,_Z:myIfPortType,_a:myIfFlowControlAdminStatus,_b:myIfFlowControlOperStatus,_c:myIfAdminSpeed,_d:myIfAdminDuplex,_e:myIfOperSpeed,_f:myIfOperDuplex,_g:myIfManageStatus,_h:myIfIpBroadcast,_i:myIfLayer,_j:myIfMode,_k:myIfCounterClear,_l:myIfEntryStatus,_m:myIfMediumType,'myIfIpTable':myIfIpTable,'myIfIpEntry':myIfIpEntry,_I:myIfIpIfIndex,_J:myIfIpId,_K:myIfIp,_n:myIfIpMask,_o:myIfIpEntryStatus,'myIfStatusTable':myIfStatusTable,'myIfStatusEntry':myIfStatusEntry,_L:myIfStatusIndex,_p:myIfStatusLoopBackExamine,_q:myIfErrorStatus,_u:myIfLineDetect,_r:myGlobalIfDisableRecovery,'myPortTypeChooseTable':myPortTypeChooseTable,'myPortTypeChooseEntry':myPortTypeChooseEntry,_M:myPortTypeChooseIndex,_s:myPortTypeChooseType,'myIfMTUTable':myIfMTUTable,'myIfMTUEntry':myIfMTUEntry,_N:myIfMTUIndex,_t:myIfMTU,'myIfAvailableBWTable':myIfAvailableBWTable,'myIfAvailableBWEntry':myIfAvailableBWEntry,_O:myIfAvailableBWIfIndex,_v:myIfAvailableBWIfBW,'myInterfaceTraps':myInterfaceTraps,_w:lineDetectStatus,_x:lineDetectPosition,'lineQualityDetect':lineQualityDetect,'myInterfaceMIBConformance':myInterfaceMIBConformance,'myInterfaceMIBCompliances':myInterfaceMIBCompliances,'myInterfaceMIBCompliance':myInterfaceMIBCompliance,'myInterfaceMIBGroups':myInterfaceMIBGroups,_y:myInterfaceMIBGroup,_z:myPortTypeChooseMibGroup,_A0:myIfMTUMibGroup,_A1:myIfLineDetectGroup,_A2:myIfAvailableBWMibGroup})