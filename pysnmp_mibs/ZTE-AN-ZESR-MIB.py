_L='zxAnZesrSecondaryPortState'
_K='zxAnZesrPrimaryPortState'
_J='zxAnZesrDomainState'
_I='forward'
_H='preforward'
_G='zxAnZesrCtrlVlanId'
_F='OctetString'
_E='read-only'
_D='ZTE-AN-ZESR-MIB'
_C='read-create'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
VlanId,ZxAnIfindex,zxAn=mibBuilder.importSymbols('ZTE-AN-TC-MIB','VlanId','ZxAnIfindex','zxAn')
zxAnZesrMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,9))
_ZxAnZesrObjects_ObjectIdentity=ObjectIdentity
zxAnZesrObjects=_ZxAnZesrObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,9,1))
_ZxAnZesrTable_Object=MibTable
zxAnZesrTable=_ZxAnZesrTable_Object((1,3,6,1,4,1,3902,1015,9,1,1))
if mibBuilder.loadTexts:zxAnZesrTable.setStatus(_A)
_ZxAnZesrEntry_Object=MibTableRow
zxAnZesrEntry=_ZxAnZesrEntry_Object((1,3,6,1,4,1,3902,1015,9,1,1,1))
zxAnZesrEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:zxAnZesrEntry.setStatus(_A)
_ZxAnZesrCtrlVlanId_Type=VlanId
_ZxAnZesrCtrlVlanId_Object=MibTableColumn
zxAnZesrCtrlVlanId=_ZxAnZesrCtrlVlanId_Object((1,3,6,1,4,1,3902,1015,9,1,1,1,1),_ZxAnZesrCtrlVlanId_Type())
zxAnZesrCtrlVlanId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:zxAnZesrCtrlVlanId.setStatus(_A)
class _ZxAnZesrCtrlVlanMstpInstance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_ZxAnZesrCtrlVlanMstpInstance_Type.__name__=_B
_ZxAnZesrCtrlVlanMstpInstance_Object=MibTableColumn
zxAnZesrCtrlVlanMstpInstance=_ZxAnZesrCtrlVlanMstpInstance_Object((1,3,6,1,4,1,3902,1015,9,1,1,1,2),_ZxAnZesrCtrlVlanMstpInstance_Type())
zxAnZesrCtrlVlanMstpInstance.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnZesrCtrlVlanMstpInstance.setStatus(_A)
class _ZxAnZesrNodeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('master',1),('transit',2)))
_ZxAnZesrNodeType_Type.__name__=_B
_ZxAnZesrNodeType_Object=MibTableColumn
zxAnZesrNodeType=_ZxAnZesrNodeType_Object((1,3,6,1,4,1,3902,1015,9,1,1,1,3),_ZxAnZesrNodeType_Type())
zxAnZesrNodeType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnZesrNodeType.setStatus(_A)
_ZxAnZesrPrimaryPort_Type=ZxAnIfindex
_ZxAnZesrPrimaryPort_Object=MibTableColumn
zxAnZesrPrimaryPort=_ZxAnZesrPrimaryPort_Object((1,3,6,1,4,1,3902,1015,9,1,1,1,4),_ZxAnZesrPrimaryPort_Type())
zxAnZesrPrimaryPort.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnZesrPrimaryPort.setStatus(_A)
_ZxAnZesrSecondaryPort_Type=ZxAnIfindex
_ZxAnZesrSecondaryPort_Object=MibTableColumn
zxAnZesrSecondaryPort=_ZxAnZesrSecondaryPort_Object((1,3,6,1,4,1,3902,1015,9,1,1,1,5),_ZxAnZesrSecondaryPort_Type())
zxAnZesrSecondaryPort.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnZesrSecondaryPort.setStatus(_A)
class _ZxAnZesrProtectVlanMstpInstance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_ZxAnZesrProtectVlanMstpInstance_Type.__name__=_B
_ZxAnZesrProtectVlanMstpInstance_Object=MibTableColumn
zxAnZesrProtectVlanMstpInstance=_ZxAnZesrProtectVlanMstpInstance_Object((1,3,6,1,4,1,3902,1015,9,1,1,1,6),_ZxAnZesrProtectVlanMstpInstance_Type())
zxAnZesrProtectVlanMstpInstance.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnZesrProtectVlanMstpInstance.setStatus(_A)
class _ZxAnZesrHealthCheckInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,1000))
_ZxAnZesrHealthCheckInterval_Type.__name__=_B
_ZxAnZesrHealthCheckInterval_Object=MibTableColumn
zxAnZesrHealthCheckInterval=_ZxAnZesrHealthCheckInterval_Object((1,3,6,1,4,1,3902,1015,9,1,1,1,7),_ZxAnZesrHealthCheckInterval_Type())
zxAnZesrHealthCheckInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnZesrHealthCheckInterval.setStatus(_A)
if mibBuilder.loadTexts:zxAnZesrHealthCheckInterval.setUnits('ms')
class _ZxAnZesrFailPeriodTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,3000))
_ZxAnZesrFailPeriodTime_Type.__name__=_B
_ZxAnZesrFailPeriodTime_Object=MibTableColumn
zxAnZesrFailPeriodTime=_ZxAnZesrFailPeriodTime_Object((1,3,6,1,4,1,3902,1015,9,1,1,1,8),_ZxAnZesrFailPeriodTime_Type())
zxAnZesrFailPeriodTime.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnZesrFailPeriodTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnZesrFailPeriodTime.setUnits('ms')
class _ZxAnZesrPreForwardingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,3000))
_ZxAnZesrPreForwardingTime_Type.__name__=_B
_ZxAnZesrPreForwardingTime_Object=MibTableColumn
zxAnZesrPreForwardingTime=_ZxAnZesrPreForwardingTime_Object((1,3,6,1,4,1,3902,1015,9,1,1,1,9),_ZxAnZesrPreForwardingTime_Type())
zxAnZesrPreForwardingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnZesrPreForwardingTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnZesrPreForwardingTime.setUnits('ms')
class _ZxAnZesrDomainState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('idle',1),('complete',2),('failed',3),('linksup',4),('linkdown',5),('preforwarding',6),('init',7)))
_ZxAnZesrDomainState_Type.__name__=_B
_ZxAnZesrDomainState_Object=MibTableColumn
zxAnZesrDomainState=_ZxAnZesrDomainState_Object((1,3,6,1,4,1,3902,1015,9,1,1,1,10),_ZxAnZesrDomainState_Type())
zxAnZesrDomainState.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnZesrDomainState.setStatus(_A)
class _ZxAnZesrPrimaryPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('block',1),(_H,2),(_I,3)))
_ZxAnZesrPrimaryPortState_Type.__name__=_B
_ZxAnZesrPrimaryPortState_Object=MibTableColumn
zxAnZesrPrimaryPortState=_ZxAnZesrPrimaryPortState_Object((1,3,6,1,4,1,3902,1015,9,1,1,1,11),_ZxAnZesrPrimaryPortState_Type())
zxAnZesrPrimaryPortState.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnZesrPrimaryPortState.setStatus(_A)
class _ZxAnZesrSecondaryPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('block',1),(_H,2),(_I,3)))
_ZxAnZesrSecondaryPortState_Type.__name__=_B
_ZxAnZesrSecondaryPortState_Object=MibTableColumn
zxAnZesrSecondaryPortState=_ZxAnZesrSecondaryPortState_Object((1,3,6,1,4,1,3902,1015,9,1,1,1,12),_ZxAnZesrSecondaryPortState_Type())
zxAnZesrSecondaryPortState.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnZesrSecondaryPortState.setStatus(_A)
class _ZxAnZesrProtectVlanList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,512));fixedLength=512
_ZxAnZesrProtectVlanList_Type.__name__=_F
_ZxAnZesrProtectVlanList_Object=MibTableColumn
zxAnZesrProtectVlanList=_ZxAnZesrProtectVlanList_Object((1,3,6,1,4,1,3902,1015,9,1,1,1,13),_ZxAnZesrProtectVlanList_Type())
zxAnZesrProtectVlanList.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnZesrProtectVlanList.setStatus(_A)
class _ZxAnZesrStandbyEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_ZxAnZesrStandbyEnable_Type.__name__=_B
_ZxAnZesrStandbyEnable_Object=MibTableColumn
zxAnZesrStandbyEnable=_ZxAnZesrStandbyEnable_Object((1,3,6,1,4,1,3902,1015,9,1,1,1,14),_ZxAnZesrStandbyEnable_Type())
zxAnZesrStandbyEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnZesrStandbyEnable.setStatus(_A)
_ZxAnZesrRowStatus_Type=RowStatus
_ZxAnZesrRowStatus_Object=MibTableColumn
zxAnZesrRowStatus=_ZxAnZesrRowStatus_Object((1,3,6,1,4,1,3902,1015,9,1,1,1,50),_ZxAnZesrRowStatus_Type())
zxAnZesrRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnZesrRowStatus.setStatus(_A)
_ZxAnZesrTraps_ObjectIdentity=ObjectIdentity
zxAnZesrTraps=_ZxAnZesrTraps_ObjectIdentity((1,3,6,1,4,1,3902,1015,9,2))
zxAnZesrSwappedTrap=NotificationType((1,3,6,1,4,1,3902,1015,9,2,1))
zxAnZesrSwappedTrap.setObjects(*((_D,_J),(_D,_K),(_D,_L)))
if mibBuilder.loadTexts:zxAnZesrSwappedTrap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'zxAnZesrMib':zxAnZesrMib,'zxAnZesrObjects':zxAnZesrObjects,'zxAnZesrTable':zxAnZesrTable,'zxAnZesrEntry':zxAnZesrEntry,_G:zxAnZesrCtrlVlanId,'zxAnZesrCtrlVlanMstpInstance':zxAnZesrCtrlVlanMstpInstance,'zxAnZesrNodeType':zxAnZesrNodeType,'zxAnZesrPrimaryPort':zxAnZesrPrimaryPort,'zxAnZesrSecondaryPort':zxAnZesrSecondaryPort,'zxAnZesrProtectVlanMstpInstance':zxAnZesrProtectVlanMstpInstance,'zxAnZesrHealthCheckInterval':zxAnZesrHealthCheckInterval,'zxAnZesrFailPeriodTime':zxAnZesrFailPeriodTime,'zxAnZesrPreForwardingTime':zxAnZesrPreForwardingTime,_J:zxAnZesrDomainState,_K:zxAnZesrPrimaryPortState,_L:zxAnZesrSecondaryPortState,'zxAnZesrProtectVlanList':zxAnZesrProtectVlanList,'zxAnZesrStandbyEnable':zxAnZesrStandbyEnable,'zxAnZesrRowStatus':zxAnZesrRowStatus,'zxAnZesrTraps':zxAnZesrTraps,'zxAnZesrSwappedTrap':zxAnZesrSwappedTrap})