_s='qtechVsuMIBTrapsGroup'
_r='qtechVsuMIBObjectsGroup'
_q='qtechVsuNotifyDad'
_p='qtechVsuNotifyDeviceRoleChange'
_o='qtechVsuNotifyDeviceChange'
_n='qtechVsuNotifyTopoChange'
_m='qtechVsuVersion'
_l='qtechVsuForwardEcmpllf'
_k='qtechVsuForwardApllf'
_j='qtechVsuDadBFDIfStatus'
_i='qtechVsuDadBFDEnable'
_h='qtechVsuDadAPMemberIfStatus'
_g='qtechVsuDadAPIfStatus'
_f='qtechVsuDadAPIfIndex'
_e='qtechVsuDadAPEnable'
_d='qtechVsuVslApUptime'
_c='qtechVsuVslPortPeerIfIndex'
_b='qtechVsuVslPortState'
_a='qtechVsuVslApIf'
_Z='qtechVsuDeviceStatus'
_Y='qtechVsuDeviceDescr'
_X='qtechVsuDevicePri'
_W='qtechVsuDeviceMac'
_V='qtechVsuDomainID'
_U='qtechVsuTopoConn'
_T='qtechVsuVslApIndex'
_S='qtechVsuDadResult'
_R='qtechVsuSlotID'
_Q='qtechVsuDeviceState'
_P='qtechVsuDeviceRole'
_O='qtechVsuTopoShape'
_N='accessible-for-notify'
_M='qtechVsuDadBFDIfIndex2'
_L='qtechVsuDadBFDIfIndex1'
_K='qtechVsuDadAPRelayIfIndex'
_J='qtechVsuDadAPMemberIfindex'
_I='qtechVsuDadExIfIndex'
_H='qtechVsuVslPortIfIndex'
_G='up'
_F='down'
_E='qtechVsuDeviceID'
_D='Integer32'
_C='read-only'
_B='QTECH-VSU-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
qtechVsuMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,102))
if mibBuilder.loadTexts:qtechVsuMIB.setRevisions(('2011-06-21 00:00',))
_QtechVsuMIBObjects_ObjectIdentity=ObjectIdentity
qtechVsuMIBObjects=_QtechVsuMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,102,1))
_QtechVsuTopo_ObjectIdentity=ObjectIdentity
qtechVsuTopo=_QtechVsuTopo_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,102,1,1))
class _QtechVsuTopoShape_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('chain',1),('ring',2)))
_QtechVsuTopoShape_Type.__name__=_D
_QtechVsuTopoShape_Object=MibScalar
qtechVsuTopoShape=_QtechVsuTopoShape_Object((1,3,6,1,4,1,27514,1,1,10,2,102,1,1,1),_QtechVsuTopoShape_Type())
qtechVsuTopoShape.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVsuTopoShape.setStatus(_A)
_QtechVsuTopoConn_Type=DisplayString
_QtechVsuTopoConn_Object=MibScalar
qtechVsuTopoConn=_QtechVsuTopoConn_Object((1,3,6,1,4,1,27514,1,1,10,2,102,1,1,2),_QtechVsuTopoConn_Type())
qtechVsuTopoConn.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVsuTopoConn.setStatus(_A)
_QtechVsuDeviceInfo_ObjectIdentity=ObjectIdentity
qtechVsuDeviceInfo=_QtechVsuDeviceInfo_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,102,1,2))
_QtechVsuDomainID_Type=Integer32
_QtechVsuDomainID_Object=MibScalar
qtechVsuDomainID=_QtechVsuDomainID_Object((1,3,6,1,4,1,27514,1,1,10,2,102,1,2,1),_QtechVsuDomainID_Type())
qtechVsuDomainID.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVsuDomainID.setStatus(_A)
_QtechVsuDeviceTable_Object=MibTable
qtechVsuDeviceTable=_QtechVsuDeviceTable_Object((1,3,6,1,4,1,27514,1,1,10,2,102,1,2,2))
if mibBuilder.loadTexts:qtechVsuDeviceTable.setStatus(_A)
_QtechVsuDeviceEntry_Object=MibTableRow
qtechVsuDeviceEntry=_QtechVsuDeviceEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,102,1,2,2,1))
qtechVsuDeviceEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:qtechVsuDeviceEntry.setStatus(_A)
_QtechVsuDeviceID_Type=Integer32
_QtechVsuDeviceID_Object=MibTableColumn
qtechVsuDeviceID=_QtechVsuDeviceID_Object((1,3,6,1,4,1,27514,1,1,10,2,102,1,2,2,1,1),_QtechVsuDeviceID_Type())
qtechVsuDeviceID.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVsuDeviceID.setStatus(_A)
_QtechVsuDeviceMac_Type=MacAddress
_QtechVsuDeviceMac_Object=MibTableColumn
qtechVsuDeviceMac=_QtechVsuDeviceMac_Object((1,3,6,1,4,1,27514,1,1,10,2,102,1,2,2,1,2),_QtechVsuDeviceMac_Type())
qtechVsuDeviceMac.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVsuDeviceMac.setStatus(_A)
_QtechVsuDevicePri_Type=Integer32
_QtechVsuDevicePri_Object=MibTableColumn
qtechVsuDevicePri=_QtechVsuDevicePri_Object((1,3,6,1,4,1,27514,1,1,10,2,102,1,2,2,1,3),_QtechVsuDevicePri_Type())
qtechVsuDevicePri.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVsuDevicePri.setStatus(_A)
_QtechVsuDeviceDescr_Type=DisplayString
_QtechVsuDeviceDescr_Object=MibTableColumn
qtechVsuDeviceDescr=_QtechVsuDeviceDescr_Object((1,3,6,1,4,1,27514,1,1,10,2,102,1,2,2,1,4),_QtechVsuDeviceDescr_Type())
qtechVsuDeviceDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVsuDeviceDescr.setStatus(_A)
class _QtechVsuDeviceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ok',1),('recovery',2)))
_QtechVsuDeviceStatus_Type.__name__=_D
_QtechVsuDeviceStatus_Object=MibTableColumn
qtechVsuDeviceStatus=_QtechVsuDeviceStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,102,1,2,2,1,5),_QtechVsuDeviceStatus_Type())
qtechVsuDeviceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVsuDeviceStatus.setStatus(_A)
class _QtechVsuDeviceRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('active',1),('standby',2),('candidate',3)))
_QtechVsuDeviceRole_Type.__name__=_D
_QtechVsuDeviceRole_Object=MibTableColumn
qtechVsuDeviceRole=_QtechVsuDeviceRole_Object((1,3,6,1,4,1,27514,1,1,10,2,102,1,2,2,1,6),_QtechVsuDeviceRole_Type())
qtechVsuDeviceRole.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVsuDeviceRole.setStatus(_A)
_QtechVsuVsl_ObjectIdentity=ObjectIdentity
qtechVsuVsl=_QtechVsuVsl_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,102,1,3))
_QtechVsuVslPortTable_Object=MibTable
qtechVsuVslPortTable=_QtechVsuVslPortTable_Object((1,3,6,1,4,1,27514,1,1,10,2,102,1,3,1))
if mibBuilder.loadTexts:qtechVsuVslPortTable.setStatus(_A)
_QtechVsuVslPortEntry_Object=MibTableRow
qtechVsuVslPortEntry=_QtechVsuVslPortEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,102,1,3,1,1))
qtechVsuVslPortEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:qtechVsuVslPortEntry.setStatus(_A)
_QtechVsuVslPortIfIndex_Type=Integer32
_QtechVsuVslPortIfIndex_Object=MibTableColumn
qtechVsuVslPortIfIndex=_QtechVsuVslPortIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,102,1,3,1,1,1),_QtechVsuVslPortIfIndex_Type())
qtechVsuVslPortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVsuVslPortIfIndex.setStatus(_A)
_QtechVsuVslApIf_Type=DisplayString
_QtechVsuVslApIf_Object=MibTableColumn
qtechVsuVslApIf=_QtechVsuVslApIf_Object((1,3,6,1,4,1,27514,1,1,10,2,102,1,3,1,1,2),_QtechVsuVslApIf_Type())
qtechVsuVslApIf.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVsuVslApIf.setStatus(_A)
class _QtechVsuVslPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_G,2),('ok',3),('disable',4),('aged',5)))
_QtechVsuVslPortState_Type.__name__=_D
_QtechVsuVslPortState_Object=MibTableColumn
qtechVsuVslPortState=_QtechVsuVslPortState_Object((1,3,6,1,4,1,27514,1,1,10,2,102,1,3,1,1,3),_QtechVsuVslPortState_Type())
qtechVsuVslPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVsuVslPortState.setStatus(_A)
_QtechVsuVslPortPeerIfIndex_Type=Integer32
_QtechVsuVslPortPeerIfIndex_Object=MibTableColumn
qtechVsuVslPortPeerIfIndex=_QtechVsuVslPortPeerIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,102,1,3,1,1,4),_QtechVsuVslPortPeerIfIndex_Type())
qtechVsuVslPortPeerIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVsuVslPortPeerIfIndex.setStatus(_A)
_QtechVsuVslTable_Object=MibTable
qtechVsuVslTable=_QtechVsuVslTable_Object((1,3,6,1,4,1,27514,1,1,10,2,102,1,3,2))
if mibBuilder.loadTexts:qtechVsuVslTable.setStatus(_A)
_QtechVsuVslEntry_Object=MibTableRow
qtechVsuVslEntry=_QtechVsuVslEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,102,1,3,2,1))
qtechVsuVslEntry.setIndexNames((0,_B,_T))
if mibBuilder.loadTexts:qtechVsuVslEntry.setStatus(_A)
_QtechVsuVslApIndex_Type=Integer32
_QtechVsuVslApIndex_Object=MibTableColumn
qtechVsuVslApIndex=_QtechVsuVslApIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,102,1,3,2,1,1),_QtechVsuVslApIndex_Type())
qtechVsuVslApIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVsuVslApIndex.setStatus(_A)
_QtechVsuVslApUptime_Type=DisplayString
_QtechVsuVslApUptime_Object=MibTableColumn
qtechVsuVslApUptime=_QtechVsuVslApUptime_Object((1,3,6,1,4,1,27514,1,1,10,2,102,1,3,2,1,2),_QtechVsuVslApUptime_Type())
qtechVsuVslApUptime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVsuVslApUptime.setStatus(_A)
_QtechVsuDad_ObjectIdentity=ObjectIdentity
qtechVsuDad=_QtechVsuDad_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,102,1,4))
_QtechVsuDadExIntfTable_Object=MibTable
qtechVsuDadExIntfTable=_QtechVsuDadExIntfTable_Object((1,3,6,1,4,1,27514,1,1,10,2,102,1,4,1))
if mibBuilder.loadTexts:qtechVsuDadExIntfTable.setStatus(_A)
_QtechVsuDadExIntfEntry_Object=MibTableRow
qtechVsuDadExIntfEntry=_QtechVsuDadExIntfEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,102,1,4,1,1))
qtechVsuDadExIntfEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:qtechVsuDadExIntfEntry.setStatus(_A)
_QtechVsuDadExIfIndex_Type=Integer32
_QtechVsuDadExIfIndex_Object=MibTableColumn
qtechVsuDadExIfIndex=_QtechVsuDadExIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,102,1,4,1,1,1),_QtechVsuDadExIfIndex_Type())
qtechVsuDadExIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVsuDadExIfIndex.setStatus(_A)
_QtechVsuDadAP_ObjectIdentity=ObjectIdentity
qtechVsuDadAP=_QtechVsuDadAP_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,102,1,4,2))
class _QtechVsuDadAPEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_QtechVsuDadAPEnable_Type.__name__=_D
_QtechVsuDadAPEnable_Object=MibScalar
qtechVsuDadAPEnable=_QtechVsuDadAPEnable_Object((1,3,6,1,4,1,27514,1,1,10,2,102,1,4,2,1),_QtechVsuDadAPEnable_Type())
qtechVsuDadAPEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVsuDadAPEnable.setStatus(_A)
_QtechVsuDadAPIfIndex_Type=Integer32
_QtechVsuDadAPIfIndex_Object=MibScalar
qtechVsuDadAPIfIndex=_QtechVsuDadAPIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,102,1,4,2,2),_QtechVsuDadAPIfIndex_Type())
qtechVsuDadAPIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVsuDadAPIfIndex.setStatus(_A)
class _QtechVsuDadAPIfStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_QtechVsuDadAPIfStatus_Type.__name__=_D
_QtechVsuDadAPIfStatus_Object=MibScalar
qtechVsuDadAPIfStatus=_QtechVsuDadAPIfStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,102,1,4,2,3),_QtechVsuDadAPIfStatus_Type())
qtechVsuDadAPIfStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVsuDadAPIfStatus.setStatus(_A)
_QtechVsuDadAPMemberIfTable_Object=MibTable
qtechVsuDadAPMemberIfTable=_QtechVsuDadAPMemberIfTable_Object((1,3,6,1,4,1,27514,1,1,10,2,102,1,4,2,4))
if mibBuilder.loadTexts:qtechVsuDadAPMemberIfTable.setStatus(_A)
_QtechVsuDadAPMemberIfEntry_Object=MibTableRow
qtechVsuDadAPMemberIfEntry=_QtechVsuDadAPMemberIfEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,102,1,4,2,4,1))
qtechVsuDadAPMemberIfEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:qtechVsuDadAPMemberIfEntry.setStatus(_A)
_QtechVsuDadAPMemberIfindex_Type=Integer32
_QtechVsuDadAPMemberIfindex_Object=MibTableColumn
qtechVsuDadAPMemberIfindex=_QtechVsuDadAPMemberIfindex_Object((1,3,6,1,4,1,27514,1,1,10,2,102,1,4,2,4,1,1),_QtechVsuDadAPMemberIfindex_Type())
qtechVsuDadAPMemberIfindex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVsuDadAPMemberIfindex.setStatus(_A)
class _QtechVsuDadAPMemberIfStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_QtechVsuDadAPMemberIfStatus_Type.__name__=_D
_QtechVsuDadAPMemberIfStatus_Object=MibTableColumn
qtechVsuDadAPMemberIfStatus=_QtechVsuDadAPMemberIfStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,102,1,4,2,4,1,2),_QtechVsuDadAPMemberIfStatus_Type())
qtechVsuDadAPMemberIfStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVsuDadAPMemberIfStatus.setStatus(_A)
_QtechVsuDadAPRelayIfTable_Object=MibTable
qtechVsuDadAPRelayIfTable=_QtechVsuDadAPRelayIfTable_Object((1,3,6,1,4,1,27514,1,1,10,2,102,1,4,2,5))
if mibBuilder.loadTexts:qtechVsuDadAPRelayIfTable.setStatus(_A)
_QtechVsuDadAPRelayIfEntry_Object=MibTableRow
qtechVsuDadAPRelayIfEntry=_QtechVsuDadAPRelayIfEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,102,1,4,2,5,1))
qtechVsuDadAPRelayIfEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:qtechVsuDadAPRelayIfEntry.setStatus(_A)
_QtechVsuDadAPRelayIfIndex_Type=Integer32
_QtechVsuDadAPRelayIfIndex_Object=MibTableColumn
qtechVsuDadAPRelayIfIndex=_QtechVsuDadAPRelayIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,102,1,4,2,5,1,1),_QtechVsuDadAPRelayIfIndex_Type())
qtechVsuDadAPRelayIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVsuDadAPRelayIfIndex.setStatus(_A)
_QtechVsuDadBFD_ObjectIdentity=ObjectIdentity
qtechVsuDadBFD=_QtechVsuDadBFD_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,102,1,4,3))
class _QtechVsuDadBFDEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_QtechVsuDadBFDEnable_Type.__name__=_D
_QtechVsuDadBFDEnable_Object=MibScalar
qtechVsuDadBFDEnable=_QtechVsuDadBFDEnable_Object((1,3,6,1,4,1,27514,1,1,10,2,102,1,4,3,1),_QtechVsuDadBFDEnable_Type())
qtechVsuDadBFDEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVsuDadBFDEnable.setStatus(_A)
_QtechVsuDadBFDIfTable_Object=MibTable
qtechVsuDadBFDIfTable=_QtechVsuDadBFDIfTable_Object((1,3,6,1,4,1,27514,1,1,10,2,102,1,4,3,2))
if mibBuilder.loadTexts:qtechVsuDadBFDIfTable.setStatus(_A)
_QtechVsuDadBFDIfEntry_Object=MibTableRow
qtechVsuDadBFDIfEntry=_QtechVsuDadBFDIfEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,102,1,4,3,2,1))
qtechVsuDadBFDIfEntry.setIndexNames((0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:qtechVsuDadBFDIfEntry.setStatus(_A)
_QtechVsuDadBFDIfIndex1_Type=Integer32
_QtechVsuDadBFDIfIndex1_Object=MibTableColumn
qtechVsuDadBFDIfIndex1=_QtechVsuDadBFDIfIndex1_Object((1,3,6,1,4,1,27514,1,1,10,2,102,1,4,3,2,1,1),_QtechVsuDadBFDIfIndex1_Type())
qtechVsuDadBFDIfIndex1.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVsuDadBFDIfIndex1.setStatus(_A)
_QtechVsuDadBFDIfIndex2_Type=Integer32
_QtechVsuDadBFDIfIndex2_Object=MibTableColumn
qtechVsuDadBFDIfIndex2=_QtechVsuDadBFDIfIndex2_Object((1,3,6,1,4,1,27514,1,1,10,2,102,1,4,3,2,1,2),_QtechVsuDadBFDIfIndex2_Type())
qtechVsuDadBFDIfIndex2.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVsuDadBFDIfIndex2.setStatus(_A)
class _QtechVsuDadBFDIfStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_QtechVsuDadBFDIfStatus_Type.__name__=_D
_QtechVsuDadBFDIfStatus_Object=MibTableColumn
qtechVsuDadBFDIfStatus=_QtechVsuDadBFDIfStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,102,1,4,3,2,1,3),_QtechVsuDadBFDIfStatus_Type())
qtechVsuDadBFDIfStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVsuDadBFDIfStatus.setStatus(_A)
_QtechVsuForward_ObjectIdentity=ObjectIdentity
qtechVsuForward=_QtechVsuForward_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,102,1,5))
class _QtechVsuForwardApllf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_QtechVsuForwardApllf_Type.__name__=_D
_QtechVsuForwardApllf_Object=MibScalar
qtechVsuForwardApllf=_QtechVsuForwardApllf_Object((1,3,6,1,4,1,27514,1,1,10,2,102,1,5,1),_QtechVsuForwardApllf_Type())
qtechVsuForwardApllf.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVsuForwardApllf.setStatus(_A)
class _QtechVsuForwardEcmpllf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_QtechVsuForwardEcmpllf_Type.__name__=_D
_QtechVsuForwardEcmpllf_Object=MibScalar
qtechVsuForwardEcmpllf=_QtechVsuForwardEcmpllf_Object((1,3,6,1,4,1,27514,1,1,10,2,102,1,5,2),_QtechVsuForwardEcmpllf_Type())
qtechVsuForwardEcmpllf.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVsuForwardEcmpllf.setStatus(_A)
_QtechVsuVersion_Type=DisplayString
_QtechVsuVersion_Object=MibScalar
qtechVsuVersion=_QtechVsuVersion_Object((1,3,6,1,4,1,27514,1,1,10,2,102,1,6),_QtechVsuVersion_Type())
qtechVsuVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVsuVersion.setStatus(_A)
_QtechVsuMIBTraps_ObjectIdentity=ObjectIdentity
qtechVsuMIBTraps=_QtechVsuMIBTraps_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,102,2))
_QtechVsuTrapsNtfObjects_ObjectIdentity=ObjectIdentity
qtechVsuTrapsNtfObjects=_QtechVsuTrapsNtfObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,102,2,1))
class _QtechVsuDeviceState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('plugin',1),('remove',2)))
_QtechVsuDeviceState_Type.__name__=_D
_QtechVsuDeviceState_Object=MibScalar
qtechVsuDeviceState=_QtechVsuDeviceState_Object((1,3,6,1,4,1,27514,1,1,10,2,102,2,1,1),_QtechVsuDeviceState_Type())
qtechVsuDeviceState.setMaxAccess(_N)
if mibBuilder.loadTexts:qtechVsuDeviceState.setStatus(_A)
_QtechVsuSlotID_Type=Integer32
_QtechVsuSlotID_Object=MibScalar
qtechVsuSlotID=_QtechVsuSlotID_Object((1,3,6,1,4,1,27514,1,1,10,2,102,2,1,2),_QtechVsuSlotID_Type())
qtechVsuSlotID.setMaxAccess(_N)
if mibBuilder.loadTexts:qtechVsuSlotID.setStatus(_A)
class _QtechVsuDadResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('good',1),('bad',2)))
_QtechVsuDadResult_Type.__name__=_D
_QtechVsuDadResult_Object=MibScalar
qtechVsuDadResult=_QtechVsuDadResult_Object((1,3,6,1,4,1,27514,1,1,10,2,102,2,1,3),_QtechVsuDadResult_Type())
qtechVsuDadResult.setMaxAccess(_N)
if mibBuilder.loadTexts:qtechVsuDadResult.setStatus(_A)
_QtechVsuTrapsNotifications_ObjectIdentity=ObjectIdentity
qtechVsuTrapsNotifications=_QtechVsuTrapsNotifications_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,102,2,2))
_QtechVsuMIBConformance_ObjectIdentity=ObjectIdentity
qtechVsuMIBConformance=_QtechVsuMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,102,3))
_QtechVsuMIBCompliances_ObjectIdentity=ObjectIdentity
qtechVsuMIBCompliances=_QtechVsuMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,102,3,1))
_QtechVsuMIBGroups_ObjectIdentity=ObjectIdentity
qtechVsuMIBGroups=_QtechVsuMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,102,3,2))
qtechVsuMIBObjectsGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,102,3,2,1))
qtechVsuMIBObjectsGroup.setObjects(*((_B,_O),(_B,_U),(_B,_V),(_B,_E),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_P),(_B,_H),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_I),(_B,_e),(_B,_f),(_B,_g),(_B,_J),(_B,_h),(_B,_K),(_B,_i),(_B,_L),(_B,_M),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:qtechVsuMIBObjectsGroup.setStatus(_A)
qtechVsuNotifyTopoChange=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,102,2,2,1))
qtechVsuNotifyTopoChange.setObjects((_B,_O))
if mibBuilder.loadTexts:qtechVsuNotifyTopoChange.setStatus(_A)
qtechVsuNotifyDeviceChange=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,102,2,2,2))
qtechVsuNotifyDeviceChange.setObjects(*((_B,_E),(_B,_Q)))
if mibBuilder.loadTexts:qtechVsuNotifyDeviceChange.setStatus(_A)
qtechVsuNotifyDeviceRoleChange=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,102,2,2,3))
qtechVsuNotifyDeviceRoleChange.setObjects(*((_B,_E),(_B,_R),(_B,_P)))
if mibBuilder.loadTexts:qtechVsuNotifyDeviceRoleChange.setStatus(_A)
qtechVsuNotifyDad=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,102,2,2,4))
qtechVsuNotifyDad.setObjects((_B,_S))
if mibBuilder.loadTexts:qtechVsuNotifyDad.setStatus(_A)
qtechVsuMIBTrapsGroup=NotificationGroup((1,3,6,1,4,1,27514,1,1,10,2,102,3,2,2))
qtechVsuMIBTrapsGroup.setObjects(*((_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:qtechVsuMIBTrapsGroup.setStatus(_A)
qtechVsuMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,102,3,1,1))
qtechVsuMIBCompliance.setObjects(*((_B,_r),(_B,_s)))
if mibBuilder.loadTexts:qtechVsuMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechVsuMIB':qtechVsuMIB,'qtechVsuMIBObjects':qtechVsuMIBObjects,'qtechVsuTopo':qtechVsuTopo,_O:qtechVsuTopoShape,_U:qtechVsuTopoConn,'qtechVsuDeviceInfo':qtechVsuDeviceInfo,_V:qtechVsuDomainID,'qtechVsuDeviceTable':qtechVsuDeviceTable,'qtechVsuDeviceEntry':qtechVsuDeviceEntry,_E:qtechVsuDeviceID,_W:qtechVsuDeviceMac,_X:qtechVsuDevicePri,_Y:qtechVsuDeviceDescr,_Z:qtechVsuDeviceStatus,_P:qtechVsuDeviceRole,'qtechVsuVsl':qtechVsuVsl,'qtechVsuVslPortTable':qtechVsuVslPortTable,'qtechVsuVslPortEntry':qtechVsuVslPortEntry,_H:qtechVsuVslPortIfIndex,_a:qtechVsuVslApIf,_b:qtechVsuVslPortState,_c:qtechVsuVslPortPeerIfIndex,'qtechVsuVslTable':qtechVsuVslTable,'qtechVsuVslEntry':qtechVsuVslEntry,_T:qtechVsuVslApIndex,_d:qtechVsuVslApUptime,'qtechVsuDad':qtechVsuDad,'qtechVsuDadExIntfTable':qtechVsuDadExIntfTable,'qtechVsuDadExIntfEntry':qtechVsuDadExIntfEntry,_I:qtechVsuDadExIfIndex,'qtechVsuDadAP':qtechVsuDadAP,_e:qtechVsuDadAPEnable,_f:qtechVsuDadAPIfIndex,_g:qtechVsuDadAPIfStatus,'qtechVsuDadAPMemberIfTable':qtechVsuDadAPMemberIfTable,'qtechVsuDadAPMemberIfEntry':qtechVsuDadAPMemberIfEntry,_J:qtechVsuDadAPMemberIfindex,_h:qtechVsuDadAPMemberIfStatus,'qtechVsuDadAPRelayIfTable':qtechVsuDadAPRelayIfTable,'qtechVsuDadAPRelayIfEntry':qtechVsuDadAPRelayIfEntry,_K:qtechVsuDadAPRelayIfIndex,'qtechVsuDadBFD':qtechVsuDadBFD,_i:qtechVsuDadBFDEnable,'qtechVsuDadBFDIfTable':qtechVsuDadBFDIfTable,'qtechVsuDadBFDIfEntry':qtechVsuDadBFDIfEntry,_L:qtechVsuDadBFDIfIndex1,_M:qtechVsuDadBFDIfIndex2,_j:qtechVsuDadBFDIfStatus,'qtechVsuForward':qtechVsuForward,_k:qtechVsuForwardApllf,_l:qtechVsuForwardEcmpllf,_m:qtechVsuVersion,'qtechVsuMIBTraps':qtechVsuMIBTraps,'qtechVsuTrapsNtfObjects':qtechVsuTrapsNtfObjects,_Q:qtechVsuDeviceState,_R:qtechVsuSlotID,_S:qtechVsuDadResult,'qtechVsuTrapsNotifications':qtechVsuTrapsNotifications,_n:qtechVsuNotifyTopoChange,_o:qtechVsuNotifyDeviceChange,_p:qtechVsuNotifyDeviceRoleChange,_q:qtechVsuNotifyDad,'qtechVsuMIBConformance':qtechVsuMIBConformance,'qtechVsuMIBCompliances':qtechVsuMIBCompliances,'qtechVsuMIBCompliance':qtechVsuMIBCompliance,'qtechVsuMIBGroups':qtechVsuMIBGroups,_r:qtechVsuMIBObjectsGroup,_s:qtechVsuMIBTrapsGroup})