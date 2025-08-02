_s='fsEghaMIBTrapsGroup'
_r='fsEghaMIBObjectsGroup'
_q='fsEghaNotifyDad'
_p='fsEghaNotifyDeviceRoleChange'
_o='fsEghaNotifyDeviceChange'
_n='fsEghaNotifyTopoChange'
_m='fsEghaVersion'
_l='fsEghaForwardEcmpllf'
_k='fsEghaForwardApllf'
_j='fsEghaDadBFDIfStatus'
_i='fsEghaDadBFDEnable'
_h='fsEghaDadAPMemberIfStatus'
_g='fsEghaDadAPIfStatus'
_f='fsEghaDadAPIfIndex'
_e='fsEghaDadAPEnable'
_d='fsEghaApUptime'
_c='fsEghaPortPeerIfIndex'
_b='fsEghaPortState'
_a='fsEghaApIf'
_Z='fsEghaDeviceStatus'
_Y='fsEghaDeviceDescr'
_X='fsEghaDevicePri'
_W='fsEghaDeviceMac'
_V='fsEghaDomainID'
_U='fsEghaTopoConn'
_T='fsEghaApIndex'
_S='fsEghaDadResult'
_R='fsEghaSlotID'
_Q='fsEghaDeviceState'
_P='fsEghaDeviceRole'
_O='fsEghaTopoShape'
_N='accessible-for-notify'
_M='fsEghaDadBFDIfIndex2'
_L='fsEghaDadBFDIfIndex1'
_K='fsEghaDadAPRelayIfIndex'
_J='fsEghaDadAPMemberIfindex'
_I='fsEghaDadExIfIndex'
_H='fsEghaPortIfIndex'
_G='up'
_F='down'
_E='fsEghaDeviceID'
_D='Integer32'
_C='read-only'
_B='FS-EGHA-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
fsEghaMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,139))
if mibBuilder.loadTexts:fsEghaMIB.setRevisions(('2015-06-01 00:00',))
_FsEghaMIBObjects_ObjectIdentity=ObjectIdentity
fsEghaMIBObjects=_FsEghaMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,139,1))
_FsEghaTopo_ObjectIdentity=ObjectIdentity
fsEghaTopo=_FsEghaTopo_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,139,1,1))
class _FsEghaTopoShape_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('chain',1),('ring',2)))
_FsEghaTopoShape_Type.__name__=_D
_FsEghaTopoShape_Object=MibScalar
fsEghaTopoShape=_FsEghaTopoShape_Object((1,3,6,1,4,1,52642,1,1,10,2,139,1,1,1),_FsEghaTopoShape_Type())
fsEghaTopoShape.setMaxAccess(_C)
if mibBuilder.loadTexts:fsEghaTopoShape.setStatus(_A)
_FsEghaTopoConn_Type=DisplayString
_FsEghaTopoConn_Object=MibScalar
fsEghaTopoConn=_FsEghaTopoConn_Object((1,3,6,1,4,1,52642,1,1,10,2,139,1,1,2),_FsEghaTopoConn_Type())
fsEghaTopoConn.setMaxAccess(_C)
if mibBuilder.loadTexts:fsEghaTopoConn.setStatus(_A)
_FsEghaDeviceInfo_ObjectIdentity=ObjectIdentity
fsEghaDeviceInfo=_FsEghaDeviceInfo_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,139,1,2))
_FsEghaDomainID_Type=Integer32
_FsEghaDomainID_Object=MibScalar
fsEghaDomainID=_FsEghaDomainID_Object((1,3,6,1,4,1,52642,1,1,10,2,139,1,2,1),_FsEghaDomainID_Type())
fsEghaDomainID.setMaxAccess(_C)
if mibBuilder.loadTexts:fsEghaDomainID.setStatus(_A)
_FsEghaDeviceTable_Object=MibTable
fsEghaDeviceTable=_FsEghaDeviceTable_Object((1,3,6,1,4,1,52642,1,1,10,2,139,1,2,2))
if mibBuilder.loadTexts:fsEghaDeviceTable.setStatus(_A)
_FsEghaDeviceEntry_Object=MibTableRow
fsEghaDeviceEntry=_FsEghaDeviceEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,139,1,2,2,1))
fsEghaDeviceEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:fsEghaDeviceEntry.setStatus(_A)
_FsEghaDeviceID_Type=Integer32
_FsEghaDeviceID_Object=MibTableColumn
fsEghaDeviceID=_FsEghaDeviceID_Object((1,3,6,1,4,1,52642,1,1,10,2,139,1,2,2,1,1),_FsEghaDeviceID_Type())
fsEghaDeviceID.setMaxAccess(_C)
if mibBuilder.loadTexts:fsEghaDeviceID.setStatus(_A)
_FsEghaDeviceMac_Type=MacAddress
_FsEghaDeviceMac_Object=MibTableColumn
fsEghaDeviceMac=_FsEghaDeviceMac_Object((1,3,6,1,4,1,52642,1,1,10,2,139,1,2,2,1,2),_FsEghaDeviceMac_Type())
fsEghaDeviceMac.setMaxAccess(_C)
if mibBuilder.loadTexts:fsEghaDeviceMac.setStatus(_A)
_FsEghaDevicePri_Type=Integer32
_FsEghaDevicePri_Object=MibTableColumn
fsEghaDevicePri=_FsEghaDevicePri_Object((1,3,6,1,4,1,52642,1,1,10,2,139,1,2,2,1,3),_FsEghaDevicePri_Type())
fsEghaDevicePri.setMaxAccess(_C)
if mibBuilder.loadTexts:fsEghaDevicePri.setStatus(_A)
_FsEghaDeviceDescr_Type=DisplayString
_FsEghaDeviceDescr_Object=MibTableColumn
fsEghaDeviceDescr=_FsEghaDeviceDescr_Object((1,3,6,1,4,1,52642,1,1,10,2,139,1,2,2,1,4),_FsEghaDeviceDescr_Type())
fsEghaDeviceDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:fsEghaDeviceDescr.setStatus(_A)
class _FsEghaDeviceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ok',1),('recovery',2)))
_FsEghaDeviceStatus_Type.__name__=_D
_FsEghaDeviceStatus_Object=MibTableColumn
fsEghaDeviceStatus=_FsEghaDeviceStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,139,1,2,2,1,5),_FsEghaDeviceStatus_Type())
fsEghaDeviceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsEghaDeviceStatus.setStatus(_A)
class _FsEghaDeviceRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('active',1),('standby',2),('candidate',3)))
_FsEghaDeviceRole_Type.__name__=_D
_FsEghaDeviceRole_Object=MibTableColumn
fsEghaDeviceRole=_FsEghaDeviceRole_Object((1,3,6,1,4,1,52642,1,1,10,2,139,1,2,2,1,6),_FsEghaDeviceRole_Type())
fsEghaDeviceRole.setMaxAccess(_C)
if mibBuilder.loadTexts:fsEghaDeviceRole.setStatus(_A)
_FsEghaLink_ObjectIdentity=ObjectIdentity
fsEghaLink=_FsEghaLink_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,139,1,3))
_FsEghaPortTable_Object=MibTable
fsEghaPortTable=_FsEghaPortTable_Object((1,3,6,1,4,1,52642,1,1,10,2,139,1,3,1))
if mibBuilder.loadTexts:fsEghaPortTable.setStatus(_A)
_FsEghaPortEntry_Object=MibTableRow
fsEghaPortEntry=_FsEghaPortEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,139,1,3,1,1))
fsEghaPortEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:fsEghaPortEntry.setStatus(_A)
_FsEghaPortIfIndex_Type=Integer32
_FsEghaPortIfIndex_Object=MibTableColumn
fsEghaPortIfIndex=_FsEghaPortIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,139,1,3,1,1,1),_FsEghaPortIfIndex_Type())
fsEghaPortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsEghaPortIfIndex.setStatus(_A)
_FsEghaApIf_Type=DisplayString
_FsEghaApIf_Object=MibTableColumn
fsEghaApIf=_FsEghaApIf_Object((1,3,6,1,4,1,52642,1,1,10,2,139,1,3,1,1,2),_FsEghaApIf_Type())
fsEghaApIf.setMaxAccess(_C)
if mibBuilder.loadTexts:fsEghaApIf.setStatus(_A)
class _FsEghaPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_G,2),('ok',3),('disable',4),('aged',5)))
_FsEghaPortState_Type.__name__=_D
_FsEghaPortState_Object=MibTableColumn
fsEghaPortState=_FsEghaPortState_Object((1,3,6,1,4,1,52642,1,1,10,2,139,1,3,1,1,3),_FsEghaPortState_Type())
fsEghaPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:fsEghaPortState.setStatus(_A)
_FsEghaPortPeerIfIndex_Type=Integer32
_FsEghaPortPeerIfIndex_Object=MibTableColumn
fsEghaPortPeerIfIndex=_FsEghaPortPeerIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,139,1,3,1,1,4),_FsEghaPortPeerIfIndex_Type())
fsEghaPortPeerIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsEghaPortPeerIfIndex.setStatus(_A)
_FsEghaApTable_Object=MibTable
fsEghaApTable=_FsEghaApTable_Object((1,3,6,1,4,1,52642,1,1,10,2,139,1,3,2))
if mibBuilder.loadTexts:fsEghaApTable.setStatus(_A)
_FsEghaApEntry_Object=MibTableRow
fsEghaApEntry=_FsEghaApEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,139,1,3,2,1))
fsEghaApEntry.setIndexNames((0,_B,_T))
if mibBuilder.loadTexts:fsEghaApEntry.setStatus(_A)
_FsEghaApIndex_Type=Integer32
_FsEghaApIndex_Object=MibTableColumn
fsEghaApIndex=_FsEghaApIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,139,1,3,2,1,1),_FsEghaApIndex_Type())
fsEghaApIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsEghaApIndex.setStatus(_A)
_FsEghaApUptime_Type=DisplayString
_FsEghaApUptime_Object=MibTableColumn
fsEghaApUptime=_FsEghaApUptime_Object((1,3,6,1,4,1,52642,1,1,10,2,139,1,3,2,1,2),_FsEghaApUptime_Type())
fsEghaApUptime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsEghaApUptime.setStatus(_A)
_FsEghaDad_ObjectIdentity=ObjectIdentity
fsEghaDad=_FsEghaDad_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,139,1,4))
_FsEghaDadExIntfTable_Object=MibTable
fsEghaDadExIntfTable=_FsEghaDadExIntfTable_Object((1,3,6,1,4,1,52642,1,1,10,2,139,1,4,1))
if mibBuilder.loadTexts:fsEghaDadExIntfTable.setStatus(_A)
_FsEghaDadExIntfEntry_Object=MibTableRow
fsEghaDadExIntfEntry=_FsEghaDadExIntfEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,139,1,4,1,1))
fsEghaDadExIntfEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:fsEghaDadExIntfEntry.setStatus(_A)
_FsEghaDadExIfIndex_Type=Integer32
_FsEghaDadExIfIndex_Object=MibTableColumn
fsEghaDadExIfIndex=_FsEghaDadExIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,139,1,4,1,1,1),_FsEghaDadExIfIndex_Type())
fsEghaDadExIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsEghaDadExIfIndex.setStatus(_A)
_FsEghaDadAP_ObjectIdentity=ObjectIdentity
fsEghaDadAP=_FsEghaDadAP_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,139,1,4,2))
class _FsEghaDadAPEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_FsEghaDadAPEnable_Type.__name__=_D
_FsEghaDadAPEnable_Object=MibScalar
fsEghaDadAPEnable=_FsEghaDadAPEnable_Object((1,3,6,1,4,1,52642,1,1,10,2,139,1,4,2,1),_FsEghaDadAPEnable_Type())
fsEghaDadAPEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:fsEghaDadAPEnable.setStatus(_A)
_FsEghaDadAPIfIndex_Type=Integer32
_FsEghaDadAPIfIndex_Object=MibScalar
fsEghaDadAPIfIndex=_FsEghaDadAPIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,139,1,4,2,2),_FsEghaDadAPIfIndex_Type())
fsEghaDadAPIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsEghaDadAPIfIndex.setStatus(_A)
class _FsEghaDadAPIfStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_FsEghaDadAPIfStatus_Type.__name__=_D
_FsEghaDadAPIfStatus_Object=MibScalar
fsEghaDadAPIfStatus=_FsEghaDadAPIfStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,139,1,4,2,3),_FsEghaDadAPIfStatus_Type())
fsEghaDadAPIfStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsEghaDadAPIfStatus.setStatus(_A)
_FsEghaDadAPMemberIfTable_Object=MibTable
fsEghaDadAPMemberIfTable=_FsEghaDadAPMemberIfTable_Object((1,3,6,1,4,1,52642,1,1,10,2,139,1,4,2,4))
if mibBuilder.loadTexts:fsEghaDadAPMemberIfTable.setStatus(_A)
_FsEghaDadAPMemberIfEntry_Object=MibTableRow
fsEghaDadAPMemberIfEntry=_FsEghaDadAPMemberIfEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,139,1,4,2,4,1))
fsEghaDadAPMemberIfEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:fsEghaDadAPMemberIfEntry.setStatus(_A)
_FsEghaDadAPMemberIfindex_Type=Integer32
_FsEghaDadAPMemberIfindex_Object=MibTableColumn
fsEghaDadAPMemberIfindex=_FsEghaDadAPMemberIfindex_Object((1,3,6,1,4,1,52642,1,1,10,2,139,1,4,2,4,1,1),_FsEghaDadAPMemberIfindex_Type())
fsEghaDadAPMemberIfindex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsEghaDadAPMemberIfindex.setStatus(_A)
class _FsEghaDadAPMemberIfStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_FsEghaDadAPMemberIfStatus_Type.__name__=_D
_FsEghaDadAPMemberIfStatus_Object=MibTableColumn
fsEghaDadAPMemberIfStatus=_FsEghaDadAPMemberIfStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,139,1,4,2,4,1,2),_FsEghaDadAPMemberIfStatus_Type())
fsEghaDadAPMemberIfStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsEghaDadAPMemberIfStatus.setStatus(_A)
_FsEghaDadAPRelayIfTable_Object=MibTable
fsEghaDadAPRelayIfTable=_FsEghaDadAPRelayIfTable_Object((1,3,6,1,4,1,52642,1,1,10,2,139,1,4,2,5))
if mibBuilder.loadTexts:fsEghaDadAPRelayIfTable.setStatus(_A)
_FsEghaDadAPRelayIfEntry_Object=MibTableRow
fsEghaDadAPRelayIfEntry=_FsEghaDadAPRelayIfEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,139,1,4,2,5,1))
fsEghaDadAPRelayIfEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:fsEghaDadAPRelayIfEntry.setStatus(_A)
_FsEghaDadAPRelayIfIndex_Type=Integer32
_FsEghaDadAPRelayIfIndex_Object=MibTableColumn
fsEghaDadAPRelayIfIndex=_FsEghaDadAPRelayIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,139,1,4,2,5,1,1),_FsEghaDadAPRelayIfIndex_Type())
fsEghaDadAPRelayIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsEghaDadAPRelayIfIndex.setStatus(_A)
_FsEghaDadBFD_ObjectIdentity=ObjectIdentity
fsEghaDadBFD=_FsEghaDadBFD_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,139,1,4,3))
class _FsEghaDadBFDEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_FsEghaDadBFDEnable_Type.__name__=_D
_FsEghaDadBFDEnable_Object=MibScalar
fsEghaDadBFDEnable=_FsEghaDadBFDEnable_Object((1,3,6,1,4,1,52642,1,1,10,2,139,1,4,3,1),_FsEghaDadBFDEnable_Type())
fsEghaDadBFDEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:fsEghaDadBFDEnable.setStatus(_A)
_FsEghaDadBFDIfTable_Object=MibTable
fsEghaDadBFDIfTable=_FsEghaDadBFDIfTable_Object((1,3,6,1,4,1,52642,1,1,10,2,139,1,4,3,2))
if mibBuilder.loadTexts:fsEghaDadBFDIfTable.setStatus(_A)
_FsEghaDadBFDIfEntry_Object=MibTableRow
fsEghaDadBFDIfEntry=_FsEghaDadBFDIfEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,139,1,4,3,2,1))
fsEghaDadBFDIfEntry.setIndexNames((0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:fsEghaDadBFDIfEntry.setStatus(_A)
_FsEghaDadBFDIfIndex1_Type=Integer32
_FsEghaDadBFDIfIndex1_Object=MibTableColumn
fsEghaDadBFDIfIndex1=_FsEghaDadBFDIfIndex1_Object((1,3,6,1,4,1,52642,1,1,10,2,139,1,4,3,2,1,1),_FsEghaDadBFDIfIndex1_Type())
fsEghaDadBFDIfIndex1.setMaxAccess(_C)
if mibBuilder.loadTexts:fsEghaDadBFDIfIndex1.setStatus(_A)
_FsEghaDadBFDIfIndex2_Type=Integer32
_FsEghaDadBFDIfIndex2_Object=MibTableColumn
fsEghaDadBFDIfIndex2=_FsEghaDadBFDIfIndex2_Object((1,3,6,1,4,1,52642,1,1,10,2,139,1,4,3,2,1,2),_FsEghaDadBFDIfIndex2_Type())
fsEghaDadBFDIfIndex2.setMaxAccess(_C)
if mibBuilder.loadTexts:fsEghaDadBFDIfIndex2.setStatus(_A)
class _FsEghaDadBFDIfStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_FsEghaDadBFDIfStatus_Type.__name__=_D
_FsEghaDadBFDIfStatus_Object=MibTableColumn
fsEghaDadBFDIfStatus=_FsEghaDadBFDIfStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,139,1,4,3,2,1,3),_FsEghaDadBFDIfStatus_Type())
fsEghaDadBFDIfStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsEghaDadBFDIfStatus.setStatus(_A)
_FsEghaForward_ObjectIdentity=ObjectIdentity
fsEghaForward=_FsEghaForward_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,139,1,5))
class _FsEghaForwardApllf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_FsEghaForwardApllf_Type.__name__=_D
_FsEghaForwardApllf_Object=MibScalar
fsEghaForwardApllf=_FsEghaForwardApllf_Object((1,3,6,1,4,1,52642,1,1,10,2,139,1,5,1),_FsEghaForwardApllf_Type())
fsEghaForwardApllf.setMaxAccess(_C)
if mibBuilder.loadTexts:fsEghaForwardApllf.setStatus(_A)
class _FsEghaForwardEcmpllf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_FsEghaForwardEcmpllf_Type.__name__=_D
_FsEghaForwardEcmpllf_Object=MibScalar
fsEghaForwardEcmpllf=_FsEghaForwardEcmpllf_Object((1,3,6,1,4,1,52642,1,1,10,2,139,1,5,2),_FsEghaForwardEcmpllf_Type())
fsEghaForwardEcmpllf.setMaxAccess(_C)
if mibBuilder.loadTexts:fsEghaForwardEcmpllf.setStatus(_A)
_FsEghaVersion_Type=DisplayString
_FsEghaVersion_Object=MibScalar
fsEghaVersion=_FsEghaVersion_Object((1,3,6,1,4,1,52642,1,1,10,2,139,1,6),_FsEghaVersion_Type())
fsEghaVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:fsEghaVersion.setStatus(_A)
_FsEghaMIBTraps_ObjectIdentity=ObjectIdentity
fsEghaMIBTraps=_FsEghaMIBTraps_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,139,2))
_FsEghaTrapsNtfObjects_ObjectIdentity=ObjectIdentity
fsEghaTrapsNtfObjects=_FsEghaTrapsNtfObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,139,2,1))
class _FsEghaDeviceState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('plugin',1),('remove',2)))
_FsEghaDeviceState_Type.__name__=_D
_FsEghaDeviceState_Object=MibScalar
fsEghaDeviceState=_FsEghaDeviceState_Object((1,3,6,1,4,1,52642,1,1,10,2,139,2,1,1),_FsEghaDeviceState_Type())
fsEghaDeviceState.setMaxAccess(_N)
if mibBuilder.loadTexts:fsEghaDeviceState.setStatus(_A)
_FsEghaSlotID_Type=Integer32
_FsEghaSlotID_Object=MibScalar
fsEghaSlotID=_FsEghaSlotID_Object((1,3,6,1,4,1,52642,1,1,10,2,139,2,1,2),_FsEghaSlotID_Type())
fsEghaSlotID.setMaxAccess(_N)
if mibBuilder.loadTexts:fsEghaSlotID.setStatus(_A)
class _FsEghaDadResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('good',1),('bad',2)))
_FsEghaDadResult_Type.__name__=_D
_FsEghaDadResult_Object=MibScalar
fsEghaDadResult=_FsEghaDadResult_Object((1,3,6,1,4,1,52642,1,1,10,2,139,2,1,3),_FsEghaDadResult_Type())
fsEghaDadResult.setMaxAccess(_N)
if mibBuilder.loadTexts:fsEghaDadResult.setStatus(_A)
_FsEghaTrapsNotifications_ObjectIdentity=ObjectIdentity
fsEghaTrapsNotifications=_FsEghaTrapsNotifications_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,139,2,2))
_FsEghaMIBConformance_ObjectIdentity=ObjectIdentity
fsEghaMIBConformance=_FsEghaMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,139,3))
_FsEghaMIBCompliances_ObjectIdentity=ObjectIdentity
fsEghaMIBCompliances=_FsEghaMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,139,3,1))
_FsEghaMIBGroups_ObjectIdentity=ObjectIdentity
fsEghaMIBGroups=_FsEghaMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,139,3,2))
fsEghaMIBObjectsGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,139,3,2,1))
fsEghaMIBObjectsGroup.setObjects(*((_B,_O),(_B,_U),(_B,_V),(_B,_E),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_P),(_B,_H),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_I),(_B,_e),(_B,_f),(_B,_g),(_B,_J),(_B,_h),(_B,_K),(_B,_i),(_B,_L),(_B,_M),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:fsEghaMIBObjectsGroup.setStatus(_A)
fsEghaNotifyTopoChange=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,139,2,2,1))
fsEghaNotifyTopoChange.setObjects((_B,_O))
if mibBuilder.loadTexts:fsEghaNotifyTopoChange.setStatus(_A)
fsEghaNotifyDeviceChange=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,139,2,2,2))
fsEghaNotifyDeviceChange.setObjects(*((_B,_E),(_B,_Q)))
if mibBuilder.loadTexts:fsEghaNotifyDeviceChange.setStatus(_A)
fsEghaNotifyDeviceRoleChange=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,139,2,2,3))
fsEghaNotifyDeviceRoleChange.setObjects(*((_B,_E),(_B,_R),(_B,_P)))
if mibBuilder.loadTexts:fsEghaNotifyDeviceRoleChange.setStatus(_A)
fsEghaNotifyDad=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,139,2,2,4))
fsEghaNotifyDad.setObjects((_B,_S))
if mibBuilder.loadTexts:fsEghaNotifyDad.setStatus(_A)
fsEghaMIBTrapsGroup=NotificationGroup((1,3,6,1,4,1,52642,1,1,10,2,139,3,2,2))
fsEghaMIBTrapsGroup.setObjects(*((_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:fsEghaMIBTrapsGroup.setStatus(_A)
fsEghaMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,139,3,1,1))
fsEghaMIBCompliance.setObjects(*((_B,_r),(_B,_s)))
if mibBuilder.loadTexts:fsEghaMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsEghaMIB':fsEghaMIB,'fsEghaMIBObjects':fsEghaMIBObjects,'fsEghaTopo':fsEghaTopo,_O:fsEghaTopoShape,_U:fsEghaTopoConn,'fsEghaDeviceInfo':fsEghaDeviceInfo,_V:fsEghaDomainID,'fsEghaDeviceTable':fsEghaDeviceTable,'fsEghaDeviceEntry':fsEghaDeviceEntry,_E:fsEghaDeviceID,_W:fsEghaDeviceMac,_X:fsEghaDevicePri,_Y:fsEghaDeviceDescr,_Z:fsEghaDeviceStatus,_P:fsEghaDeviceRole,'fsEghaLink':fsEghaLink,'fsEghaPortTable':fsEghaPortTable,'fsEghaPortEntry':fsEghaPortEntry,_H:fsEghaPortIfIndex,_a:fsEghaApIf,_b:fsEghaPortState,_c:fsEghaPortPeerIfIndex,'fsEghaApTable':fsEghaApTable,'fsEghaApEntry':fsEghaApEntry,_T:fsEghaApIndex,_d:fsEghaApUptime,'fsEghaDad':fsEghaDad,'fsEghaDadExIntfTable':fsEghaDadExIntfTable,'fsEghaDadExIntfEntry':fsEghaDadExIntfEntry,_I:fsEghaDadExIfIndex,'fsEghaDadAP':fsEghaDadAP,_e:fsEghaDadAPEnable,_f:fsEghaDadAPIfIndex,_g:fsEghaDadAPIfStatus,'fsEghaDadAPMemberIfTable':fsEghaDadAPMemberIfTable,'fsEghaDadAPMemberIfEntry':fsEghaDadAPMemberIfEntry,_J:fsEghaDadAPMemberIfindex,_h:fsEghaDadAPMemberIfStatus,'fsEghaDadAPRelayIfTable':fsEghaDadAPRelayIfTable,'fsEghaDadAPRelayIfEntry':fsEghaDadAPRelayIfEntry,_K:fsEghaDadAPRelayIfIndex,'fsEghaDadBFD':fsEghaDadBFD,_i:fsEghaDadBFDEnable,'fsEghaDadBFDIfTable':fsEghaDadBFDIfTable,'fsEghaDadBFDIfEntry':fsEghaDadBFDIfEntry,_L:fsEghaDadBFDIfIndex1,_M:fsEghaDadBFDIfIndex2,_j:fsEghaDadBFDIfStatus,'fsEghaForward':fsEghaForward,_k:fsEghaForwardApllf,_l:fsEghaForwardEcmpllf,_m:fsEghaVersion,'fsEghaMIBTraps':fsEghaMIBTraps,'fsEghaTrapsNtfObjects':fsEghaTrapsNtfObjects,_Q:fsEghaDeviceState,_R:fsEghaSlotID,_S:fsEghaDadResult,'fsEghaTrapsNotifications':fsEghaTrapsNotifications,_n:fsEghaNotifyTopoChange,_o:fsEghaNotifyDeviceChange,_p:fsEghaNotifyDeviceRoleChange,_q:fsEghaNotifyDad,'fsEghaMIBConformance':fsEghaMIBConformance,'fsEghaMIBCompliances':fsEghaMIBCompliances,'fsEghaMIBCompliance':fsEghaMIBCompliance,'fsEghaMIBGroups':fsEghaMIBGroups,_r:fsEghaMIBObjectsGroup,_s:fsEghaMIBTrapsGroup})