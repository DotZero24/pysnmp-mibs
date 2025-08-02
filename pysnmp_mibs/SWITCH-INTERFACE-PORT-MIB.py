_f='not-accessible'
_e='rcComboPortMedia'
_d='rcComboPortId'
_c='fiber10000'
_b='fiber1000'
_a='fiber100'
_Z='speed-10G'
_Y='OctetString'
_X='auto-negotiate'
_W='fiber'
_V='xover'
_U='normal'
_T='full'
_S='half'
_R='speed-1000M'
_Q='speed-100M'
_P='speed-10M'
_O='illegal'
_N='rcIfPortMAUIndex'
_M='EnableVar'
_L='copper'
_K='rcIfPortPHYIndex'
_J='enable'
_I='disable'
_H='mandatory'
_G='unknown'
_F='SWITCH-INTERFACE-PORT-MIB'
_E='not-support'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_Y,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
rcSystem,=mibBuilder.importSymbols('SWITCH-SYSTEM-MIB','rcSystem')
EnableVar,=mibBuilder.importSymbols('SWITCH-TC',_M)
rcIfPortInfoConfig=ModuleIdentity((1,3,6,1,4,1,8886,6,1,1,7))
if mibBuilder.loadTexts:rcIfPortInfoConfig.setRevisions(('1908-12-03 00:00',))
_RcIfPortPHYInfoConfig_ObjectIdentity=ObjectIdentity
rcIfPortPHYInfoConfig=_RcIfPortPHYInfoConfig_ObjectIdentity((1,3,6,1,4,1,8886,6,1,1,7,1))
_RcIfPortPHYNotifications_ObjectIdentity=ObjectIdentity
rcIfPortPHYNotifications=_RcIfPortPHYNotifications_ObjectIdentity((1,3,6,1,4,1,8886,6,1,1,7,1,1))
_RcIfPortPHYInfomation_ObjectIdentity=ObjectIdentity
rcIfPortPHYInfomation=_RcIfPortPHYInfomation_ObjectIdentity((1,3,6,1,4,1,8886,6,1,1,7,1,2))
_RcIfPortPHYTable_Object=MibTable
rcIfPortPHYTable=_RcIfPortPHYTable_Object((1,3,6,1,4,1,8886,6,1,1,7,1,2,1))
if mibBuilder.loadTexts:rcIfPortPHYTable.setStatus(_A)
_RcIfPortPHYEntry_Object=MibTableRow
rcIfPortPHYEntry=_RcIfPortPHYEntry_Object((1,3,6,1,4,1,8886,6,1,1,7,1,2,1,1))
rcIfPortPHYEntry.setIndexNames((0,_F,_K))
if mibBuilder.loadTexts:rcIfPortPHYEntry.setStatus(_A)
_RcIfPortPHYIndex_Type=Integer32
_RcIfPortPHYIndex_Object=MibTableColumn
rcIfPortPHYIndex=_RcIfPortPHYIndex_Object((1,3,6,1,4,1,8886,6,1,1,7,1,2,1,1,1),_RcIfPortPHYIndex_Type())
rcIfPortPHYIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:rcIfPortPHYIndex.setStatus(_A)
_RcIfPortPHYExistence_Type=TruthValue
_RcIfPortPHYExistence_Object=MibTableColumn
rcIfPortPHYExistence=_RcIfPortPHYExistence_Object((1,3,6,1,4,1,8886,6,1,1,7,1,2,1,1,2),_RcIfPortPHYExistence_Type())
rcIfPortPHYExistence.setMaxAccess(_D)
if mibBuilder.loadTexts:rcIfPortPHYExistence.setStatus(_A)
_RcIfPortPHYMAUNum_Type=Integer32
_RcIfPortPHYMAUNum_Object=MibTableColumn
rcIfPortPHYMAUNum=_RcIfPortPHYMAUNum_Object((1,3,6,1,4,1,8886,6,1,1,7,1,2,1,1,3),_RcIfPortPHYMAUNum_Type())
rcIfPortPHYMAUNum.setMaxAccess(_D)
if mibBuilder.loadTexts:rcIfPortPHYMAUNum.setStatus(_A)
class _RcIfPortPHYAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_RcIfPortPHYAdminStatus_Type.__name__=_B
_RcIfPortPHYAdminStatus_Object=MibTableColumn
rcIfPortPHYAdminStatus=_RcIfPortPHYAdminStatus_Object((1,3,6,1,4,1,8886,6,1,1,7,1,2,1,1,4),_RcIfPortPHYAdminStatus_Type())
rcIfPortPHYAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rcIfPortPHYAdminStatus.setStatus(_A)
class _RcIfPortPHYOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_RcIfPortPHYOperStatus_Type.__name__=_B
_RcIfPortPHYOperStatus_Object=MibTableColumn
rcIfPortPHYOperStatus=_RcIfPortPHYOperStatus_Object((1,3,6,1,4,1,8886,6,1,1,7,1,2,1,1,5),_RcIfPortPHYOperStatus_Type())
rcIfPortPHYOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcIfPortPHYOperStatus.setStatus(_A)
class _RcIfPortPHYSpeedGet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_O,0),(_G,1),(_P,2),(_Q,3),(_R,4),(_Z,5)))
_RcIfPortPHYSpeedGet_Type.__name__=_B
_RcIfPortPHYSpeedGet_Object=MibTableColumn
rcIfPortPHYSpeedGet=_RcIfPortPHYSpeedGet_Object((1,3,6,1,4,1,8886,6,1,1,7,1,2,1,1,6),_RcIfPortPHYSpeedGet_Type())
rcIfPortPHYSpeedGet.setMaxAccess(_D)
if mibBuilder.loadTexts:rcIfPortPHYSpeedGet.setStatus(_A)
class _RcIfPortPHYDuplexGet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_O,0),(_G,1),(_S,2),(_T,3)))
_RcIfPortPHYDuplexGet_Type.__name__=_B
_RcIfPortPHYDuplexGet_Object=MibTableColumn
rcIfPortPHYDuplexGet=_RcIfPortPHYDuplexGet_Object((1,3,6,1,4,1,8886,6,1,1,7,1,2,1,1,7),_RcIfPortPHYDuplexGet_Type())
rcIfPortPHYDuplexGet.setMaxAccess(_D)
if mibBuilder.loadTexts:rcIfPortPHYDuplexGet.setStatus(_A)
_RcIfPortPHYFlowControlRecvStatus_Type=EnableVar
_RcIfPortPHYFlowControlRecvStatus_Object=MibTableColumn
rcIfPortPHYFlowControlRecvStatus=_RcIfPortPHYFlowControlRecvStatus_Object((1,3,6,1,4,1,8886,6,1,1,7,1,2,1,1,8),_RcIfPortPHYFlowControlRecvStatus_Type())
rcIfPortPHYFlowControlRecvStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcIfPortPHYFlowControlRecvStatus.setStatus(_A)
_RcIfPortPHYFlowControlSendStatus_Type=EnableVar
_RcIfPortPHYFlowControlSendStatus_Object=MibTableColumn
rcIfPortPHYFlowControlSendStatus=_RcIfPortPHYFlowControlSendStatus_Object((1,3,6,1,4,1,8886,6,1,1,7,1,2,1,1,9),_RcIfPortPHYFlowControlSendStatus_Type())
rcIfPortPHYFlowControlSendStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcIfPortPHYFlowControlSendStatus.setStatus(_A)
class _RcIfPortPHYMdiStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_O,0),(_G,1),(_U,2),(_V,3)))
_RcIfPortPHYMdiStatus_Type.__name__=_B
_RcIfPortPHYMdiStatus_Object=MibTableColumn
rcIfPortPHYMdiStatus=_RcIfPortPHYMdiStatus_Object((1,3,6,1,4,1,8886,6,1,1,7,1,2,1,1,10),_RcIfPortPHYMdiStatus_Type())
rcIfPortPHYMdiStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcIfPortPHYMdiStatus.setStatus(_A)
_RcIfPortPHYActiveMAUIndex_Type=Integer32
_RcIfPortPHYActiveMAUIndex_Object=MibTableColumn
rcIfPortPHYActiveMAUIndex=_RcIfPortPHYActiveMAUIndex_Object((1,3,6,1,4,1,8886,6,1,1,7,1,2,1,1,11),_RcIfPortPHYActiveMAUIndex_Type())
rcIfPortPHYActiveMAUIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:rcIfPortPHYActiveMAUIndex.setStatus(_A)
class _RcComboPortMediaMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_E,0),('auto',1),('fiber-forced',2),('copper-forced',3)))
_RcComboPortMediaMode_Type.__name__=_B
_RcComboPortMediaMode_Object=MibTableColumn
rcComboPortMediaMode=_RcComboPortMediaMode_Object((1,3,6,1,4,1,8886,6,1,1,7,1,2,1,1,12),_RcComboPortMediaMode_Type())
rcComboPortMediaMode.setMaxAccess(_C)
if mibBuilder.loadTexts:rcComboPortMediaMode.setStatus(_H)
class _RcComboPortMediaPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),(_W,1),(_L,2)))
_RcComboPortMediaPriority_Type.__name__=_B
_RcComboPortMediaPriority_Object=MibTableColumn
rcComboPortMediaPriority=_RcComboPortMediaPriority_Object((1,3,6,1,4,1,8886,6,1,1,7,1,2,1,1,13),_RcComboPortMediaPriority_Type())
rcComboPortMediaPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:rcComboPortMediaPriority.setStatus(_H)
class _RcComboPortMediaActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('unavailable',0),(_W,1),(_L,2)))
_RcComboPortMediaActive_Type.__name__=_B
_RcComboPortMediaActive_Object=MibTableColumn
rcComboPortMediaActive=_RcComboPortMediaActive_Object((1,3,6,1,4,1,8886,6,1,1,7,1,2,1,1,14),_RcComboPortMediaActive_Type())
rcComboPortMediaActive.setMaxAccess(_D)
if mibBuilder.loadTexts:rcComboPortMediaActive.setStatus(_A)
class _RcIfPortSfpAutoDetect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_RcIfPortSfpAutoDetect_Type.__name__=_B
_RcIfPortSfpAutoDetect_Object=MibTableColumn
rcIfPortSfpAutoDetect=_RcIfPortSfpAutoDetect_Object((1,3,6,1,4,1,8886,6,1,1,7,1,2,1,1,15),_RcIfPortSfpAutoDetect_Type())
rcIfPortSfpAutoDetect.setMaxAccess(_C)
if mibBuilder.loadTexts:rcIfPortSfpAutoDetect.setStatus(_H)
class _RcIfPortSfpPortTypeGet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_G,0),(_L,1),(_a,2),(_b,3),(_c,4)))
_RcIfPortSfpPortTypeGet_Type.__name__=_B
_RcIfPortSfpPortTypeGet_Object=MibTableColumn
rcIfPortSfpPortTypeGet=_RcIfPortSfpPortTypeGet_Object((1,3,6,1,4,1,8886,6,1,1,7,1,2,1,1,16),_RcIfPortSfpPortTypeGet_Type())
rcIfPortSfpPortTypeGet.setMaxAccess(_D)
if mibBuilder.loadTexts:rcIfPortSfpPortTypeGet.setStatus(_H)
class _RcIfPortPHYEEEAutoGet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),(_J,1),(_I,2)))
_RcIfPortPHYEEEAutoGet_Type.__name__=_B
_RcIfPortPHYEEEAutoGet_Object=MibTableColumn
rcIfPortPHYEEEAutoGet=_RcIfPortPHYEEEAutoGet_Object((1,3,6,1,4,1,8886,6,1,1,7,1,2,1,1,17),_RcIfPortPHYEEEAutoGet_Type())
rcIfPortPHYEEEAutoGet.setMaxAccess(_D)
if mibBuilder.loadTexts:rcIfPortPHYEEEAutoGet.setStatus(_H)
_RcIfPortMAUTable_Object=MibTable
rcIfPortMAUTable=_RcIfPortMAUTable_Object((1,3,6,1,4,1,8886,6,1,1,7,1,2,2))
if mibBuilder.loadTexts:rcIfPortMAUTable.setStatus(_A)
_RcIfPortMAUEntry_Object=MibTableRow
rcIfPortMAUEntry=_RcIfPortMAUEntry_Object((1,3,6,1,4,1,8886,6,1,1,7,1,2,2,1))
rcIfPortMAUEntry.setIndexNames((0,_F,_K),(0,_F,_N))
if mibBuilder.loadTexts:rcIfPortMAUEntry.setStatus(_A)
_RcIfPortMAUIndex_Type=Integer32
_RcIfPortMAUIndex_Object=MibTableColumn
rcIfPortMAUIndex=_RcIfPortMAUIndex_Object((1,3,6,1,4,1,8886,6,1,1,7,1,2,2,1,1),_RcIfPortMAUIndex_Type())
rcIfPortMAUIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:rcIfPortMAUIndex.setStatus(_A)
class _RcIfPortMAUType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,5,16,18,22,30,31,33,37,99,100,101)));namedValues=NamedValues(*((_G,0),('dot3-10BASE-T',5),('dot3-100BASE-TX',16),('dot3-100BASE-FX',18),('dot3-1000BASE-X',22),('dot3-1000BASE-T',30),('dot3-10GBASE-X',31),('dot3-10GBASE-R',33),('dot3-10GBASE-W',37),('rc-1000BASE-P',99),('dot3-1000BASE-T1',100),('dot3-1000BASE-T2',101)))
_RcIfPortMAUType_Type.__name__=_B
_RcIfPortMAUType_Object=MibTableColumn
rcIfPortMAUType=_RcIfPortMAUType_Object((1,3,6,1,4,1,8886,6,1,1,7,1,2,2,1,2),_RcIfPortMAUType_Type())
rcIfPortMAUType.setMaxAccess(_D)
if mibBuilder.loadTexts:rcIfPortMAUType.setStatus(_A)
class _RcIfPortMAUConnectorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_G,0),('other',1),('sfp',2),('sfp-plus',3)))
_RcIfPortMAUConnectorType_Type.__name__=_B
_RcIfPortMAUConnectorType_Object=MibTableColumn
rcIfPortMAUConnectorType=_RcIfPortMAUConnectorType_Object((1,3,6,1,4,1,8886,6,1,1,7,1,2,2,1,3),_RcIfPortMAUConnectorType_Type())
rcIfPortMAUConnectorType.setMaxAccess(_D)
if mibBuilder.loadTexts:rcIfPortMAUConnectorType.setStatus(_A)
class _RcIfPortMAUConnectorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_G,0),('error',1),('not-present',2),('present',3)))
_RcIfPortMAUConnectorStatus_Type.__name__=_B
_RcIfPortMAUConnectorStatus_Object=MibTableColumn
rcIfPortMAUConnectorStatus=_RcIfPortMAUConnectorStatus_Object((1,3,6,1,4,1,8886,6,1,1,7,1,2,2,1,4),_RcIfPortMAUConnectorStatus_Type())
rcIfPortMAUConnectorStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcIfPortMAUConnectorStatus.setStatus(_A)
class _RcIfPortMAUSpeedSet_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_X,1),(_P,2),(_Q,3),(_R,4),(_Z,5)))
_RcIfPortMAUSpeedSet_Type.__name__=_B
_RcIfPortMAUSpeedSet_Object=MibTableColumn
rcIfPortMAUSpeedSet=_RcIfPortMAUSpeedSet_Object((1,3,6,1,4,1,8886,6,1,1,7,1,2,2,1,5),_RcIfPortMAUSpeedSet_Type())
rcIfPortMAUSpeedSet.setMaxAccess(_C)
if mibBuilder.loadTexts:rcIfPortMAUSpeedSet.setStatus(_A)
class _RcIfPortMAUDuplexSet_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_X,1),(_S,2),(_T,3)))
_RcIfPortMAUDuplexSet_Type.__name__=_B
_RcIfPortMAUDuplexSet_Object=MibTableColumn
rcIfPortMAUDuplexSet=_RcIfPortMAUDuplexSet_Object((1,3,6,1,4,1,8886,6,1,1,7,1,2,2,1,6),_RcIfPortMAUDuplexSet_Type())
rcIfPortMAUDuplexSet.setMaxAccess(_C)
if mibBuilder.loadTexts:rcIfPortMAUDuplexSet.setStatus(_A)
class _RcIfPortMAUFlowControlEnable_Type(EnableVar):defaultValue=2
_RcIfPortMAUFlowControlEnable_Type.__name__=_M
_RcIfPortMAUFlowControlEnable_Object=MibTableColumn
rcIfPortMAUFlowControlEnable=_RcIfPortMAUFlowControlEnable_Object((1,3,6,1,4,1,8886,6,1,1,7,1,2,2,1,7),_RcIfPortMAUFlowControlEnable_Type())
rcIfPortMAUFlowControlEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rcIfPortMAUFlowControlEnable.setStatus(_A)
class _RcIfPortMAUFlowControlRecvEnable_Type(EnableVar):defaultValue=2
_RcIfPortMAUFlowControlRecvEnable_Type.__name__=_M
_RcIfPortMAUFlowControlRecvEnable_Object=MibTableColumn
rcIfPortMAUFlowControlRecvEnable=_RcIfPortMAUFlowControlRecvEnable_Object((1,3,6,1,4,1,8886,6,1,1,7,1,2,2,1,8),_RcIfPortMAUFlowControlRecvEnable_Type())
rcIfPortMAUFlowControlRecvEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rcIfPortMAUFlowControlRecvEnable.setStatus(_A)
class _RcIfPortMAUFlowControlSendEnable_Type(EnableVar):defaultValue=2
_RcIfPortMAUFlowControlSendEnable_Type.__name__=_M
_RcIfPortMAUFlowControlSendEnable_Object=MibTableColumn
rcIfPortMAUFlowControlSendEnable=_RcIfPortMAUFlowControlSendEnable_Object((1,3,6,1,4,1,8886,6,1,1,7,1,2,2,1,9),_RcIfPortMAUFlowControlSendEnable_Type())
rcIfPortMAUFlowControlSendEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rcIfPortMAUFlowControlSendEnable.setStatus(_A)
class _RcIfPortMAUMdiMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('auto-detect',1),(_U,2),(_V,3)))
_RcIfPortMAUMdiMode_Type.__name__=_B
_RcIfPortMAUMdiMode_Object=MibTableColumn
rcIfPortMAUMdiMode=_RcIfPortMAUMdiMode_Object((1,3,6,1,4,1,8886,6,1,1,7,1,2,2,1,10),_RcIfPortMAUMdiMode_Type())
rcIfPortMAUMdiMode.setMaxAccess(_C)
if mibBuilder.loadTexts:rcIfPortMAUMdiMode.setStatus(_A)
class _RcIfPortMAUStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('suspend',2)))
_RcIfPortMAUStatus_Type.__name__=_B
_RcIfPortMAUStatus_Object=MibTableColumn
rcIfPortMAUStatus=_RcIfPortMAUStatus_Object((1,3,6,1,4,1,8886,6,1,1,7,1,2,2,1,11),_RcIfPortMAUStatus_Type())
rcIfPortMAUStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rcIfPortMAUStatus.setStatus(_A)
class _RcIfPortMAUSfpPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('autodetect',0),(_L,1),(_a,2),(_b,3),(_c,4)))
_RcIfPortMAUSfpPortType_Type.__name__=_B
_RcIfPortMAUSfpPortType_Object=MibTableColumn
rcIfPortMAUSfpPortType=_RcIfPortMAUSfpPortType_Object((1,3,6,1,4,1,8886,6,1,1,7,1,2,2,1,12),_RcIfPortMAUSfpPortType_Type())
rcIfPortMAUSfpPortType.setMaxAccess(_C)
if mibBuilder.loadTexts:rcIfPortMAUSfpPortType.setStatus(_H)
class _RcIfPortEEEAutoMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),(_J,1),(_I,2)))
_RcIfPortEEEAutoMode_Type.__name__=_B
_RcIfPortEEEAutoMode_Object=MibTableColumn
rcIfPortEEEAutoMode=_RcIfPortEEEAutoMode_Object((1,3,6,1,4,1,8886,6,1,1,7,1,2,2,1,13),_RcIfPortEEEAutoMode_Type())
rcIfPortEEEAutoMode.setMaxAccess(_C)
if mibBuilder.loadTexts:rcIfPortEEEAutoMode.setStatus(_H)
_RcComboMediaTable_Object=MibTable
rcComboMediaTable=_RcComboMediaTable_Object((1,3,6,1,4,1,8886,6,1,1,7,1,2,3))
if mibBuilder.loadTexts:rcComboMediaTable.setStatus(_A)
_RcComboMediaEntry_Object=MibTableRow
rcComboMediaEntry=_RcComboMediaEntry_Object((1,3,6,1,4,1,8886,6,1,1,7,1,2,3,1))
rcComboMediaEntry.setIndexNames((0,_F,_d),(0,_F,_e))
if mibBuilder.loadTexts:rcComboMediaEntry.setStatus(_A)
_RcComboPortId_Type=Integer32
_RcComboPortId_Object=MibTableColumn
rcComboPortId=_RcComboPortId_Object((1,3,6,1,4,1,8886,6,1,1,7,1,2,3,1,1),_RcComboPortId_Type())
rcComboPortId.setMaxAccess(_f)
if mibBuilder.loadTexts:rcComboPortId.setStatus(_A)
class _RcComboPortMedia_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),(_W,1),(_L,2)))
_RcComboPortMedia_Type.__name__=_B
_RcComboPortMedia_Object=MibTableColumn
rcComboPortMedia=_RcComboPortMedia_Object((1,3,6,1,4,1,8886,6,1,1,7,1,2,3,1,2),_RcComboPortMedia_Type())
rcComboPortMedia.setMaxAccess(_f)
if mibBuilder.loadTexts:rcComboPortMedia.setStatus(_A)
class _RcComboPortDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_RcComboPortDescription_Type.__name__=_Y
_RcComboPortDescription_Object=MibTableColumn
rcComboPortDescription=_RcComboPortDescription_Object((1,3,6,1,4,1,8886,6,1,1,7,1,2,3,1,3),_RcComboPortDescription_Type())
rcComboPortDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:rcComboPortDescription.setStatus(_A)
class _RcComboPortSpeed_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_E,0),('Auto-negotiate',1),(_P,2),(_Q,3),(_R,4)))
_RcComboPortSpeed_Type.__name__=_B
_RcComboPortSpeed_Object=MibTableColumn
rcComboPortSpeed=_RcComboPortSpeed_Object((1,3,6,1,4,1,8886,6,1,1,7,1,2,3,1,4),_RcComboPortSpeed_Type())
rcComboPortSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:rcComboPortSpeed.setStatus(_A)
class _RcComboPortDuplex_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_E,0),(_X,1),(_S,2),(_T,3)))
_RcComboPortDuplex_Type.__name__=_B
_RcComboPortDuplex_Object=MibTableColumn
rcComboPortDuplex=_RcComboPortDuplex_Object((1,3,6,1,4,1,8886,6,1,1,7,1,2,3,1,5),_RcComboPortDuplex_Type())
rcComboPortDuplex.setMaxAccess(_C)
if mibBuilder.loadTexts:rcComboPortDuplex.setStatus(_A)
class _RcComboPortFlowCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),(_J,1),(_I,2)))
_RcComboPortFlowCtrl_Type.__name__=_B
_RcComboPortFlowCtrl_Object=MibTableColumn
rcComboPortFlowCtrl=_RcComboPortFlowCtrl_Object((1,3,6,1,4,1,8886,6,1,1,7,1,2,3,1,6),_RcComboPortFlowCtrl_Type())
rcComboPortFlowCtrl.setMaxAccess(_C)
if mibBuilder.loadTexts:rcComboPortFlowCtrl.setStatus(_A)
class _RcComboPortSendFlowCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),(_J,1),(_I,2)))
_RcComboPortSendFlowCtrl_Type.__name__=_B
_RcComboPortSendFlowCtrl_Object=MibTableColumn
rcComboPortSendFlowCtrl=_RcComboPortSendFlowCtrl_Object((1,3,6,1,4,1,8886,6,1,1,7,1,2,3,1,7),_RcComboPortSendFlowCtrl_Type())
rcComboPortSendFlowCtrl.setMaxAccess(_C)
if mibBuilder.loadTexts:rcComboPortSendFlowCtrl.setStatus(_A)
class _RcComboPortRecvFlowCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),(_J,1),(_I,2)))
_RcComboPortRecvFlowCtrl_Type.__name__=_B
_RcComboPortRecvFlowCtrl_Object=MibTableColumn
rcComboPortRecvFlowCtrl=_RcComboPortRecvFlowCtrl_Object((1,3,6,1,4,1,8886,6,1,1,7,1,2,3,1,8),_RcComboPortRecvFlowCtrl_Type())
rcComboPortRecvFlowCtrl.setMaxAccess(_C)
if mibBuilder.loadTexts:rcComboPortRecvFlowCtrl.setStatus(_A)
class _RcComboPortMdiXMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_E,0),('auto',1),(_U,2),(_V,3)))
_RcComboPortMdiXMode_Type.__name__=_B
_RcComboPortMdiXMode_Object=MibTableColumn
rcComboPortMdiXMode=_RcComboPortMdiXMode_Object((1,3,6,1,4,1,8886,6,1,1,7,1,2,3,1,9),_RcComboPortMdiXMode_Type())
rcComboPortMdiXMode.setMaxAccess(_C)
if mibBuilder.loadTexts:rcComboPortMdiXMode.setStatus(_A)
rcIfPortConnectorInsertTrap=NotificationType((1,3,6,1,4,1,8886,6,1,1,7,1,1,1))
rcIfPortConnectorInsertTrap.setObjects(*((_F,_K),(_F,_N)))
if mibBuilder.loadTexts:rcIfPortConnectorInsertTrap.setStatus(_A)
rcIfPortConnectorRemoveTrap=NotificationType((1,3,6,1,4,1,8886,6,1,1,7,1,1,2))
rcIfPortConnectorRemoveTrap.setObjects(*((_F,_K),(_F,_N)))
if mibBuilder.loadTexts:rcIfPortConnectorRemoveTrap.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'rcIfPortInfoConfig':rcIfPortInfoConfig,'rcIfPortPHYInfoConfig':rcIfPortPHYInfoConfig,'rcIfPortPHYNotifications':rcIfPortPHYNotifications,'rcIfPortConnectorInsertTrap':rcIfPortConnectorInsertTrap,'rcIfPortConnectorRemoveTrap':rcIfPortConnectorRemoveTrap,'rcIfPortPHYInfomation':rcIfPortPHYInfomation,'rcIfPortPHYTable':rcIfPortPHYTable,'rcIfPortPHYEntry':rcIfPortPHYEntry,_K:rcIfPortPHYIndex,'rcIfPortPHYExistence':rcIfPortPHYExistence,'rcIfPortPHYMAUNum':rcIfPortPHYMAUNum,'rcIfPortPHYAdminStatus':rcIfPortPHYAdminStatus,'rcIfPortPHYOperStatus':rcIfPortPHYOperStatus,'rcIfPortPHYSpeedGet':rcIfPortPHYSpeedGet,'rcIfPortPHYDuplexGet':rcIfPortPHYDuplexGet,'rcIfPortPHYFlowControlRecvStatus':rcIfPortPHYFlowControlRecvStatus,'rcIfPortPHYFlowControlSendStatus':rcIfPortPHYFlowControlSendStatus,'rcIfPortPHYMdiStatus':rcIfPortPHYMdiStatus,'rcIfPortPHYActiveMAUIndex':rcIfPortPHYActiveMAUIndex,'rcComboPortMediaMode':rcComboPortMediaMode,'rcComboPortMediaPriority':rcComboPortMediaPriority,'rcComboPortMediaActive':rcComboPortMediaActive,'rcIfPortSfpAutoDetect':rcIfPortSfpAutoDetect,'rcIfPortSfpPortTypeGet':rcIfPortSfpPortTypeGet,'rcIfPortPHYEEEAutoGet':rcIfPortPHYEEEAutoGet,'rcIfPortMAUTable':rcIfPortMAUTable,'rcIfPortMAUEntry':rcIfPortMAUEntry,_N:rcIfPortMAUIndex,'rcIfPortMAUType':rcIfPortMAUType,'rcIfPortMAUConnectorType':rcIfPortMAUConnectorType,'rcIfPortMAUConnectorStatus':rcIfPortMAUConnectorStatus,'rcIfPortMAUSpeedSet':rcIfPortMAUSpeedSet,'rcIfPortMAUDuplexSet':rcIfPortMAUDuplexSet,'rcIfPortMAUFlowControlEnable':rcIfPortMAUFlowControlEnable,'rcIfPortMAUFlowControlRecvEnable':rcIfPortMAUFlowControlRecvEnable,'rcIfPortMAUFlowControlSendEnable':rcIfPortMAUFlowControlSendEnable,'rcIfPortMAUMdiMode':rcIfPortMAUMdiMode,'rcIfPortMAUStatus':rcIfPortMAUStatus,'rcIfPortMAUSfpPortType':rcIfPortMAUSfpPortType,'rcIfPortEEEAutoMode':rcIfPortEEEAutoMode,'rcComboMediaTable':rcComboMediaTable,'rcComboMediaEntry':rcComboMediaEntry,_d:rcComboPortId,_e:rcComboPortMedia,'rcComboPortDescription':rcComboPortDescription,'rcComboPortSpeed':rcComboPortSpeed,'rcComboPortDuplex':rcComboPortDuplex,'rcComboPortFlowCtrl':rcComboPortFlowCtrl,'rcComboPortSendFlowCtrl':rcComboPortSendFlowCtrl,'rcComboPortRecvFlowCtrl':rcComboPortRecvFlowCtrl,'rcComboPortMdiXMode':rcComboPortMdiXMode})