_u='fsVsuMIBTrapsGroup'
_t='fsVsuMIBObjectsGroup'
_s='fsVsuNotifyDeviceLeave'
_r='fsVsuNotifyDeviceJoin'
_q='fsVsuNotifyDad'
_p='fsVsuNotifyDeviceRoleChange'
_o='fsVsuNotifyDeviceChange'
_n='fsVsuNotifyTopoChange'
_m='fsVsuVersion'
_l='fsVsuForwardEcmpllf'
_k='fsVsuForwardApllf'
_j='fsVsuDadBFDIfStatus'
_i='fsVsuDadBFDEnable'
_h='fsVsuDadAPMemberIfStatus'
_g='fsVsuDadAPIfStatus'
_f='fsVsuDadAPIfIndex'
_e='fsVsuDadAPEnable'
_d='fsVsuVslApUptime'
_c='fsVsuVslPortPeerIfIndex'
_b='fsVsuVslPortState'
_a='fsVsuVslApIf'
_Z='fsVsuDeviceStatus'
_Y='fsVsuDeviceDescr'
_X='fsVsuDevicePri'
_W='fsVsuDeviceMac'
_V='fsVsuDomainID'
_U='fsVsuTopoConn'
_T='fsVsuVslApIndex'
_S='fsVsuDadResult'
_R='fsVsuSlotID'
_Q='fsVsuDeviceState'
_P='fsVsuDeviceRole'
_O='fsVsuTopoShape'
_N='accessible-for-notify'
_M='fsVsuDadBFDIfIndex2'
_L='fsVsuDadBFDIfIndex1'
_K='fsVsuDadAPRelayIfIndex'
_J='fsVsuDadAPMemberIfindex'
_I='fsVsuDadExIfIndex'
_H='fsVsuVslPortIfIndex'
_G='up'
_F='down'
_E='fsVsuDeviceID'
_D='Integer32'
_C='read-only'
_B='current'
_A='FS-VSU-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
fsVsuMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,102))
if mibBuilder.loadTexts:fsVsuMIB.setRevisions(('2011-06-21 00:00',))
_FsVsuMIBObjects_ObjectIdentity=ObjectIdentity
fsVsuMIBObjects=_FsVsuMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,102,1))
_FsVsuTopo_ObjectIdentity=ObjectIdentity
fsVsuTopo=_FsVsuTopo_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,102,1,1))
class _FsVsuTopoShape_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('chain',1),('ring',2)))
_FsVsuTopoShape_Type.__name__=_D
_FsVsuTopoShape_Object=MibScalar
fsVsuTopoShape=_FsVsuTopoShape_Object((1,3,6,1,4,1,52642,1,1,10,2,102,1,1,1),_FsVsuTopoShape_Type())
fsVsuTopoShape.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVsuTopoShape.setStatus(_B)
_FsVsuTopoConn_Type=DisplayString
_FsVsuTopoConn_Object=MibScalar
fsVsuTopoConn=_FsVsuTopoConn_Object((1,3,6,1,4,1,52642,1,1,10,2,102,1,1,2),_FsVsuTopoConn_Type())
fsVsuTopoConn.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVsuTopoConn.setStatus(_B)
_FsVsuDeviceInfo_ObjectIdentity=ObjectIdentity
fsVsuDeviceInfo=_FsVsuDeviceInfo_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,102,1,2))
_FsVsuDomainID_Type=Integer32
_FsVsuDomainID_Object=MibScalar
fsVsuDomainID=_FsVsuDomainID_Object((1,3,6,1,4,1,52642,1,1,10,2,102,1,2,1),_FsVsuDomainID_Type())
fsVsuDomainID.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVsuDomainID.setStatus(_B)
_FsVsuDeviceTable_Object=MibTable
fsVsuDeviceTable=_FsVsuDeviceTable_Object((1,3,6,1,4,1,52642,1,1,10,2,102,1,2,2))
if mibBuilder.loadTexts:fsVsuDeviceTable.setStatus(_B)
_FsVsuDeviceEntry_Object=MibTableRow
fsVsuDeviceEntry=_FsVsuDeviceEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,102,1,2,2,1))
fsVsuDeviceEntry.setIndexNames((0,_A,_E))
if mibBuilder.loadTexts:fsVsuDeviceEntry.setStatus(_B)
_FsVsuDeviceID_Type=Integer32
_FsVsuDeviceID_Object=MibTableColumn
fsVsuDeviceID=_FsVsuDeviceID_Object((1,3,6,1,4,1,52642,1,1,10,2,102,1,2,2,1,1),_FsVsuDeviceID_Type())
fsVsuDeviceID.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVsuDeviceID.setStatus(_B)
_FsVsuDeviceMac_Type=MacAddress
_FsVsuDeviceMac_Object=MibTableColumn
fsVsuDeviceMac=_FsVsuDeviceMac_Object((1,3,6,1,4,1,52642,1,1,10,2,102,1,2,2,1,2),_FsVsuDeviceMac_Type())
fsVsuDeviceMac.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVsuDeviceMac.setStatus(_B)
_FsVsuDevicePri_Type=Integer32
_FsVsuDevicePri_Object=MibTableColumn
fsVsuDevicePri=_FsVsuDevicePri_Object((1,3,6,1,4,1,52642,1,1,10,2,102,1,2,2,1,3),_FsVsuDevicePri_Type())
fsVsuDevicePri.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVsuDevicePri.setStatus(_B)
_FsVsuDeviceDescr_Type=DisplayString
_FsVsuDeviceDescr_Object=MibTableColumn
fsVsuDeviceDescr=_FsVsuDeviceDescr_Object((1,3,6,1,4,1,52642,1,1,10,2,102,1,2,2,1,4),_FsVsuDeviceDescr_Type())
fsVsuDeviceDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVsuDeviceDescr.setStatus(_B)
class _FsVsuDeviceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ok',1),('recovery',2)))
_FsVsuDeviceStatus_Type.__name__=_D
_FsVsuDeviceStatus_Object=MibTableColumn
fsVsuDeviceStatus=_FsVsuDeviceStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,102,1,2,2,1,5),_FsVsuDeviceStatus_Type())
fsVsuDeviceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVsuDeviceStatus.setStatus(_B)
class _FsVsuDeviceRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('active',1),('standby',2),('candidate',3)))
_FsVsuDeviceRole_Type.__name__=_D
_FsVsuDeviceRole_Object=MibTableColumn
fsVsuDeviceRole=_FsVsuDeviceRole_Object((1,3,6,1,4,1,52642,1,1,10,2,102,1,2,2,1,6),_FsVsuDeviceRole_Type())
fsVsuDeviceRole.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVsuDeviceRole.setStatus(_B)
_FsVsuVsl_ObjectIdentity=ObjectIdentity
fsVsuVsl=_FsVsuVsl_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,102,1,3))
_FsVsuVslPortTable_Object=MibTable
fsVsuVslPortTable=_FsVsuVslPortTable_Object((1,3,6,1,4,1,52642,1,1,10,2,102,1,3,1))
if mibBuilder.loadTexts:fsVsuVslPortTable.setStatus(_B)
_FsVsuVslPortEntry_Object=MibTableRow
fsVsuVslPortEntry=_FsVsuVslPortEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,102,1,3,1,1))
fsVsuVslPortEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:fsVsuVslPortEntry.setStatus(_B)
_FsVsuVslPortIfIndex_Type=Integer32
_FsVsuVslPortIfIndex_Object=MibTableColumn
fsVsuVslPortIfIndex=_FsVsuVslPortIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,102,1,3,1,1,1),_FsVsuVslPortIfIndex_Type())
fsVsuVslPortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVsuVslPortIfIndex.setStatus(_B)
_FsVsuVslApIf_Type=DisplayString
_FsVsuVslApIf_Object=MibTableColumn
fsVsuVslApIf=_FsVsuVslApIf_Object((1,3,6,1,4,1,52642,1,1,10,2,102,1,3,1,1,2),_FsVsuVslApIf_Type())
fsVsuVslApIf.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVsuVslApIf.setStatus(_B)
class _FsVsuVslPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_G,2),('ok',3),('disable',4),('aged',5)))
_FsVsuVslPortState_Type.__name__=_D
_FsVsuVslPortState_Object=MibTableColumn
fsVsuVslPortState=_FsVsuVslPortState_Object((1,3,6,1,4,1,52642,1,1,10,2,102,1,3,1,1,3),_FsVsuVslPortState_Type())
fsVsuVslPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVsuVslPortState.setStatus(_B)
_FsVsuVslPortPeerIfIndex_Type=Integer32
_FsVsuVslPortPeerIfIndex_Object=MibTableColumn
fsVsuVslPortPeerIfIndex=_FsVsuVslPortPeerIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,102,1,3,1,1,4),_FsVsuVslPortPeerIfIndex_Type())
fsVsuVslPortPeerIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVsuVslPortPeerIfIndex.setStatus(_B)
_FsVsuVslTable_Object=MibTable
fsVsuVslTable=_FsVsuVslTable_Object((1,3,6,1,4,1,52642,1,1,10,2,102,1,3,2))
if mibBuilder.loadTexts:fsVsuVslTable.setStatus(_B)
_FsVsuVslEntry_Object=MibTableRow
fsVsuVslEntry=_FsVsuVslEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,102,1,3,2,1))
fsVsuVslEntry.setIndexNames((0,_A,_T))
if mibBuilder.loadTexts:fsVsuVslEntry.setStatus(_B)
_FsVsuVslApIndex_Type=Integer32
_FsVsuVslApIndex_Object=MibTableColumn
fsVsuVslApIndex=_FsVsuVslApIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,102,1,3,2,1,1),_FsVsuVslApIndex_Type())
fsVsuVslApIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVsuVslApIndex.setStatus(_B)
_FsVsuVslApUptime_Type=DisplayString
_FsVsuVslApUptime_Object=MibTableColumn
fsVsuVslApUptime=_FsVsuVslApUptime_Object((1,3,6,1,4,1,52642,1,1,10,2,102,1,3,2,1,2),_FsVsuVslApUptime_Type())
fsVsuVslApUptime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVsuVslApUptime.setStatus(_B)
_FsVsuDad_ObjectIdentity=ObjectIdentity
fsVsuDad=_FsVsuDad_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,102,1,4))
_FsVsuDadExIntfTable_Object=MibTable
fsVsuDadExIntfTable=_FsVsuDadExIntfTable_Object((1,3,6,1,4,1,52642,1,1,10,2,102,1,4,1))
if mibBuilder.loadTexts:fsVsuDadExIntfTable.setStatus(_B)
_FsVsuDadExIntfEntry_Object=MibTableRow
fsVsuDadExIntfEntry=_FsVsuDadExIntfEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,102,1,4,1,1))
fsVsuDadExIntfEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:fsVsuDadExIntfEntry.setStatus(_B)
_FsVsuDadExIfIndex_Type=Integer32
_FsVsuDadExIfIndex_Object=MibTableColumn
fsVsuDadExIfIndex=_FsVsuDadExIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,102,1,4,1,1,1),_FsVsuDadExIfIndex_Type())
fsVsuDadExIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVsuDadExIfIndex.setStatus(_B)
_FsVsuDadAP_ObjectIdentity=ObjectIdentity
fsVsuDadAP=_FsVsuDadAP_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,102,1,4,2))
class _FsVsuDadAPEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_FsVsuDadAPEnable_Type.__name__=_D
_FsVsuDadAPEnable_Object=MibScalar
fsVsuDadAPEnable=_FsVsuDadAPEnable_Object((1,3,6,1,4,1,52642,1,1,10,2,102,1,4,2,1),_FsVsuDadAPEnable_Type())
fsVsuDadAPEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVsuDadAPEnable.setStatus(_B)
_FsVsuDadAPIfIndex_Type=Integer32
_FsVsuDadAPIfIndex_Object=MibScalar
fsVsuDadAPIfIndex=_FsVsuDadAPIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,102,1,4,2,2),_FsVsuDadAPIfIndex_Type())
fsVsuDadAPIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVsuDadAPIfIndex.setStatus(_B)
class _FsVsuDadAPIfStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_FsVsuDadAPIfStatus_Type.__name__=_D
_FsVsuDadAPIfStatus_Object=MibScalar
fsVsuDadAPIfStatus=_FsVsuDadAPIfStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,102,1,4,2,3),_FsVsuDadAPIfStatus_Type())
fsVsuDadAPIfStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVsuDadAPIfStatus.setStatus(_B)
_FsVsuDadAPMemberIfTable_Object=MibTable
fsVsuDadAPMemberIfTable=_FsVsuDadAPMemberIfTable_Object((1,3,6,1,4,1,52642,1,1,10,2,102,1,4,2,4))
if mibBuilder.loadTexts:fsVsuDadAPMemberIfTable.setStatus(_B)
_FsVsuDadAPMemberIfEntry_Object=MibTableRow
fsVsuDadAPMemberIfEntry=_FsVsuDadAPMemberIfEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,102,1,4,2,4,1))
fsVsuDadAPMemberIfEntry.setIndexNames((0,_A,_J))
if mibBuilder.loadTexts:fsVsuDadAPMemberIfEntry.setStatus(_B)
_FsVsuDadAPMemberIfindex_Type=Integer32
_FsVsuDadAPMemberIfindex_Object=MibTableColumn
fsVsuDadAPMemberIfindex=_FsVsuDadAPMemberIfindex_Object((1,3,6,1,4,1,52642,1,1,10,2,102,1,4,2,4,1,1),_FsVsuDadAPMemberIfindex_Type())
fsVsuDadAPMemberIfindex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVsuDadAPMemberIfindex.setStatus(_B)
class _FsVsuDadAPMemberIfStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_FsVsuDadAPMemberIfStatus_Type.__name__=_D
_FsVsuDadAPMemberIfStatus_Object=MibTableColumn
fsVsuDadAPMemberIfStatus=_FsVsuDadAPMemberIfStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,102,1,4,2,4,1,2),_FsVsuDadAPMemberIfStatus_Type())
fsVsuDadAPMemberIfStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVsuDadAPMemberIfStatus.setStatus(_B)
_FsVsuDadAPRelayIfTable_Object=MibTable
fsVsuDadAPRelayIfTable=_FsVsuDadAPRelayIfTable_Object((1,3,6,1,4,1,52642,1,1,10,2,102,1,4,2,5))
if mibBuilder.loadTexts:fsVsuDadAPRelayIfTable.setStatus(_B)
_FsVsuDadAPRelayIfEntry_Object=MibTableRow
fsVsuDadAPRelayIfEntry=_FsVsuDadAPRelayIfEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,102,1,4,2,5,1))
fsVsuDadAPRelayIfEntry.setIndexNames((0,_A,_K))
if mibBuilder.loadTexts:fsVsuDadAPRelayIfEntry.setStatus(_B)
_FsVsuDadAPRelayIfIndex_Type=Integer32
_FsVsuDadAPRelayIfIndex_Object=MibTableColumn
fsVsuDadAPRelayIfIndex=_FsVsuDadAPRelayIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,102,1,4,2,5,1,1),_FsVsuDadAPRelayIfIndex_Type())
fsVsuDadAPRelayIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVsuDadAPRelayIfIndex.setStatus(_B)
_FsVsuDadBFD_ObjectIdentity=ObjectIdentity
fsVsuDadBFD=_FsVsuDadBFD_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,102,1,4,3))
class _FsVsuDadBFDEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_FsVsuDadBFDEnable_Type.__name__=_D
_FsVsuDadBFDEnable_Object=MibScalar
fsVsuDadBFDEnable=_FsVsuDadBFDEnable_Object((1,3,6,1,4,1,52642,1,1,10,2,102,1,4,3,1),_FsVsuDadBFDEnable_Type())
fsVsuDadBFDEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVsuDadBFDEnable.setStatus(_B)
_FsVsuDadBFDIfTable_Object=MibTable
fsVsuDadBFDIfTable=_FsVsuDadBFDIfTable_Object((1,3,6,1,4,1,52642,1,1,10,2,102,1,4,3,2))
if mibBuilder.loadTexts:fsVsuDadBFDIfTable.setStatus(_B)
_FsVsuDadBFDIfEntry_Object=MibTableRow
fsVsuDadBFDIfEntry=_FsVsuDadBFDIfEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,102,1,4,3,2,1))
fsVsuDadBFDIfEntry.setIndexNames((0,_A,_L),(0,_A,_M))
if mibBuilder.loadTexts:fsVsuDadBFDIfEntry.setStatus(_B)
_FsVsuDadBFDIfIndex1_Type=Integer32
_FsVsuDadBFDIfIndex1_Object=MibTableColumn
fsVsuDadBFDIfIndex1=_FsVsuDadBFDIfIndex1_Object((1,3,6,1,4,1,52642,1,1,10,2,102,1,4,3,2,1,1),_FsVsuDadBFDIfIndex1_Type())
fsVsuDadBFDIfIndex1.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVsuDadBFDIfIndex1.setStatus(_B)
_FsVsuDadBFDIfIndex2_Type=Integer32
_FsVsuDadBFDIfIndex2_Object=MibTableColumn
fsVsuDadBFDIfIndex2=_FsVsuDadBFDIfIndex2_Object((1,3,6,1,4,1,52642,1,1,10,2,102,1,4,3,2,1,2),_FsVsuDadBFDIfIndex2_Type())
fsVsuDadBFDIfIndex2.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVsuDadBFDIfIndex2.setStatus(_B)
class _FsVsuDadBFDIfStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_FsVsuDadBFDIfStatus_Type.__name__=_D
_FsVsuDadBFDIfStatus_Object=MibTableColumn
fsVsuDadBFDIfStatus=_FsVsuDadBFDIfStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,102,1,4,3,2,1,3),_FsVsuDadBFDIfStatus_Type())
fsVsuDadBFDIfStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVsuDadBFDIfStatus.setStatus(_B)
_FsVsuForward_ObjectIdentity=ObjectIdentity
fsVsuForward=_FsVsuForward_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,102,1,5))
class _FsVsuForwardApllf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_FsVsuForwardApllf_Type.__name__=_D
_FsVsuForwardApllf_Object=MibScalar
fsVsuForwardApllf=_FsVsuForwardApllf_Object((1,3,6,1,4,1,52642,1,1,10,2,102,1,5,1),_FsVsuForwardApllf_Type())
fsVsuForwardApllf.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVsuForwardApllf.setStatus(_B)
class _FsVsuForwardEcmpllf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_FsVsuForwardEcmpllf_Type.__name__=_D
_FsVsuForwardEcmpllf_Object=MibScalar
fsVsuForwardEcmpllf=_FsVsuForwardEcmpllf_Object((1,3,6,1,4,1,52642,1,1,10,2,102,1,5,2),_FsVsuForwardEcmpllf_Type())
fsVsuForwardEcmpllf.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVsuForwardEcmpllf.setStatus(_B)
_FsVsuVersion_Type=DisplayString
_FsVsuVersion_Object=MibScalar
fsVsuVersion=_FsVsuVersion_Object((1,3,6,1,4,1,52642,1,1,10,2,102,1,6),_FsVsuVersion_Type())
fsVsuVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVsuVersion.setStatus(_B)
_FsVsuMIBTraps_ObjectIdentity=ObjectIdentity
fsVsuMIBTraps=_FsVsuMIBTraps_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,102,2))
_FsVsuTrapsNtfObjects_ObjectIdentity=ObjectIdentity
fsVsuTrapsNtfObjects=_FsVsuTrapsNtfObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,102,2,1))
class _FsVsuDeviceState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('plugin',1),('remove',2)))
_FsVsuDeviceState_Type.__name__=_D
_FsVsuDeviceState_Object=MibScalar
fsVsuDeviceState=_FsVsuDeviceState_Object((1,3,6,1,4,1,52642,1,1,10,2,102,2,1,1),_FsVsuDeviceState_Type())
fsVsuDeviceState.setMaxAccess(_N)
if mibBuilder.loadTexts:fsVsuDeviceState.setStatus(_B)
_FsVsuSlotID_Type=Integer32
_FsVsuSlotID_Object=MibScalar
fsVsuSlotID=_FsVsuSlotID_Object((1,3,6,1,4,1,52642,1,1,10,2,102,2,1,2),_FsVsuSlotID_Type())
fsVsuSlotID.setMaxAccess(_N)
if mibBuilder.loadTexts:fsVsuSlotID.setStatus(_B)
class _FsVsuDadResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('good',1),('bad',2)))
_FsVsuDadResult_Type.__name__=_D
_FsVsuDadResult_Object=MibScalar
fsVsuDadResult=_FsVsuDadResult_Object((1,3,6,1,4,1,52642,1,1,10,2,102,2,1,3),_FsVsuDadResult_Type())
fsVsuDadResult.setMaxAccess(_N)
if mibBuilder.loadTexts:fsVsuDadResult.setStatus(_B)
_FsVsuTrapsNotifications_ObjectIdentity=ObjectIdentity
fsVsuTrapsNotifications=_FsVsuTrapsNotifications_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,102,2,2))
_FsVsuMIBConformance_ObjectIdentity=ObjectIdentity
fsVsuMIBConformance=_FsVsuMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,102,3))
_FsVsuMIBCompliances_ObjectIdentity=ObjectIdentity
fsVsuMIBCompliances=_FsVsuMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,102,3,1))
_FsVsuMIBGroups_ObjectIdentity=ObjectIdentity
fsVsuMIBGroups=_FsVsuMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,102,3,2))
fsVsuMIBObjectsGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,102,3,2,1))
fsVsuMIBObjectsGroup.setObjects(*((_A,_O),(_A,_U),(_A,_V),(_A,_E),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_P),(_A,_H),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_I),(_A,_e),(_A,_f),(_A,_g),(_A,_J),(_A,_h),(_A,_K),(_A,_i),(_A,_L),(_A,_M),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:fsVsuMIBObjectsGroup.setStatus(_B)
fsVsuNotifyTopoChange=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,102,2,2,1))
fsVsuNotifyTopoChange.setObjects((_A,_O))
if mibBuilder.loadTexts:fsVsuNotifyTopoChange.setStatus(_B)
fsVsuNotifyDeviceChange=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,102,2,2,2))
fsVsuNotifyDeviceChange.setObjects(*((_A,_E),(_A,_Q)))
if mibBuilder.loadTexts:fsVsuNotifyDeviceChange.setStatus(_B)
fsVsuNotifyDeviceRoleChange=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,102,2,2,3))
fsVsuNotifyDeviceRoleChange.setObjects(*((_A,_E),(_A,_R),(_A,_P)))
if mibBuilder.loadTexts:fsVsuNotifyDeviceRoleChange.setStatus(_B)
fsVsuNotifyDad=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,102,2,2,4))
fsVsuNotifyDad.setObjects((_A,_S))
if mibBuilder.loadTexts:fsVsuNotifyDad.setStatus(_B)
fsVsuNotifyDeviceJoin=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,102,2,2,5))
fsVsuNotifyDeviceJoin.setObjects((_A,_E))
if mibBuilder.loadTexts:fsVsuNotifyDeviceJoin.setStatus(_B)
fsVsuNotifyDeviceLeave=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,102,2,2,6))
fsVsuNotifyDeviceLeave.setObjects((_A,_E))
if mibBuilder.loadTexts:fsVsuNotifyDeviceLeave.setStatus(_B)
fsVsuMIBTrapsGroup=NotificationGroup((1,3,6,1,4,1,52642,1,1,10,2,102,3,2,2))
fsVsuMIBTrapsGroup.setObjects(*((_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:fsVsuMIBTrapsGroup.setStatus(_B)
fsVsuMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,102,3,1,1))
fsVsuMIBCompliance.setObjects(*((_A,_t),(_A,_u)))
if mibBuilder.loadTexts:fsVsuMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'fsVsuMIB':fsVsuMIB,'fsVsuMIBObjects':fsVsuMIBObjects,'fsVsuTopo':fsVsuTopo,_O:fsVsuTopoShape,_U:fsVsuTopoConn,'fsVsuDeviceInfo':fsVsuDeviceInfo,_V:fsVsuDomainID,'fsVsuDeviceTable':fsVsuDeviceTable,'fsVsuDeviceEntry':fsVsuDeviceEntry,_E:fsVsuDeviceID,_W:fsVsuDeviceMac,_X:fsVsuDevicePri,_Y:fsVsuDeviceDescr,_Z:fsVsuDeviceStatus,_P:fsVsuDeviceRole,'fsVsuVsl':fsVsuVsl,'fsVsuVslPortTable':fsVsuVslPortTable,'fsVsuVslPortEntry':fsVsuVslPortEntry,_H:fsVsuVslPortIfIndex,_a:fsVsuVslApIf,_b:fsVsuVslPortState,_c:fsVsuVslPortPeerIfIndex,'fsVsuVslTable':fsVsuVslTable,'fsVsuVslEntry':fsVsuVslEntry,_T:fsVsuVslApIndex,_d:fsVsuVslApUptime,'fsVsuDad':fsVsuDad,'fsVsuDadExIntfTable':fsVsuDadExIntfTable,'fsVsuDadExIntfEntry':fsVsuDadExIntfEntry,_I:fsVsuDadExIfIndex,'fsVsuDadAP':fsVsuDadAP,_e:fsVsuDadAPEnable,_f:fsVsuDadAPIfIndex,_g:fsVsuDadAPIfStatus,'fsVsuDadAPMemberIfTable':fsVsuDadAPMemberIfTable,'fsVsuDadAPMemberIfEntry':fsVsuDadAPMemberIfEntry,_J:fsVsuDadAPMemberIfindex,_h:fsVsuDadAPMemberIfStatus,'fsVsuDadAPRelayIfTable':fsVsuDadAPRelayIfTable,'fsVsuDadAPRelayIfEntry':fsVsuDadAPRelayIfEntry,_K:fsVsuDadAPRelayIfIndex,'fsVsuDadBFD':fsVsuDadBFD,_i:fsVsuDadBFDEnable,'fsVsuDadBFDIfTable':fsVsuDadBFDIfTable,'fsVsuDadBFDIfEntry':fsVsuDadBFDIfEntry,_L:fsVsuDadBFDIfIndex1,_M:fsVsuDadBFDIfIndex2,_j:fsVsuDadBFDIfStatus,'fsVsuForward':fsVsuForward,_k:fsVsuForwardApllf,_l:fsVsuForwardEcmpllf,_m:fsVsuVersion,'fsVsuMIBTraps':fsVsuMIBTraps,'fsVsuTrapsNtfObjects':fsVsuTrapsNtfObjects,_Q:fsVsuDeviceState,_R:fsVsuSlotID,_S:fsVsuDadResult,'fsVsuTrapsNotifications':fsVsuTrapsNotifications,_n:fsVsuNotifyTopoChange,_o:fsVsuNotifyDeviceChange,_p:fsVsuNotifyDeviceRoleChange,_q:fsVsuNotifyDad,_r:fsVsuNotifyDeviceJoin,_s:fsVsuNotifyDeviceLeave,'fsVsuMIBConformance':fsVsuMIBConformance,'fsVsuMIBCompliances':fsVsuMIBCompliances,'fsVsuMIBCompliance':fsVsuMIBCompliance,'fsVsuMIBGroups':fsVsuMIBGroups,_t:fsVsuMIBObjectsGroup,_u:fsVsuMIBTrapsGroup})