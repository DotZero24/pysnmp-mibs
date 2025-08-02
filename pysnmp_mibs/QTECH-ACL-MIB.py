_AH='qtechAclMIBGroup'
_AG='qtechIfOutAclName'
_AF='qtechIfInAclName'
_AE='qtechAclIfCurruntEntryNum'
_AD='qtechAclIfMaxEntryNum'
_AC='qtechAceExtDestIp6WildCard'
_AB='qtechAceExtIfAnyDestIp6WildCard'
_AA='qtechAceExtDestIp6'
_A9='qtechAceExtIfAnyDestIp6'
_A8='qtechAceExtSourceIp6WildCard'
_A7='qtechAceExtIfAnySourceIp6WildCard'
_A6='qtechAceExtSourceIp6'
_A5='qtechAceExtIfAnySourceIp6'
_A4='qtechAceExtDestMacAddrWildCard'
_A3='qtechAceExtIfAnyDestMacAddrWildCard'
_A2='qtechAceExtSourceMacAddrWildCard'
_A1='qtechAceExtIfAnySourceMacAddrWildCard'
_A0='qtechAceExtTcpFlag'
_z='qtechAceExtIfAnyTcpFlag'
_y='qtechAceExtDscp'
_x='qtechAceExtIfAnyDscp'
_w='qtechAceExtIpPrec'
_v='qtechAceExtIfAnyIpPrec'
_u='qtechAceExtCos'
_t='qtechAceExtIfAnyCos'
_s='qtechAceExtDestProtocolPortRange'
_r='qtechAceExtDestPortOp'
_q='qtechAceExtSourceProtocolPortRange'
_p='qtechAceExtSourcePortOp'
_o='qtechAceExtTimeRangeName'
_n='qtechAceExtEntryStauts'
_m='qtechAceExtFlowAction'
_l='qtechAceExtDestProtocolPort'
_k='qtechAceExtSourceProtocolPort'
_j='qtechAceExtIpProtocolField'
_i='qtechAceExtIfAnyIpProtocolField'
_h='qtechAceExtEtherLikeType'
_g='qtechAceExtIfAnyEtherLikeType'
_f='qtechAceExtDestMacAddr'
_e='qtechAceExtIfAnyDestMacAddr'
_d='qtechAceExtDestIpWildCard'
_c='qtechAceExtIfAnyDestWildCard'
_b='qtechAceExtDestIp'
_a='qtechAceExtIfAnyDestIp'
_Z='qtechAceExtSourceMacAddr'
_Y='qtechAceExtIfAnySourceMacAddr'
_X='qtechAceExtSourceWildCard'
_W='qtechAceExtIfAnySourceWildCard'
_V='qtechAceExtSourceIp'
_U='qtechAceExtIfAnySourceIp'
_T='qtechAceExtVID'
_S='qtechAceExtIfAnyVID'
_R='qtechAclEntryStatus'
_Q='qtechAclMode'
_P='noOperator'
_O='Unsigned32'
_N='qtechAceExtProtocolType'
_M='qtechAceExtIndex'
_L='qtechAceExtAclName'
_K='qtechAclIfIndex'
_J='qtechAclName'
_I='OctetString'
_H='Integer32'
_G='read-only'
_F='DisplayString'
_E='TruthValue'
_D='read-create'
_C='read-write'
_B='QTECH-ACL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ConfigStatus,IfIndex=mibBuilder.importSymbols('QTECH-TC','ConfigStatus','IfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_O,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'MacAddress','PhysAddress','RowStatus','TextualConvention',_E)
qtechAclMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,17))
if mibBuilder.loadTexts:qtechAclMIB.setRevisions(('2002-03-20 00:00',))
_QtechAclMIBObjects_ObjectIdentity=ObjectIdentity
qtechAclMIBObjects=_QtechAclMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,17,1))
_QtechAclTable_Object=MibTable
qtechAclTable=_QtechAclTable_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,1))
if mibBuilder.loadTexts:qtechAclTable.setStatus(_A)
_QtechAclEntry_Object=MibTableRow
qtechAclEntry=_QtechAclEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,1,1))
qtechAclEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:qtechAclEntry.setStatus(_A)
class _QtechAclName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechAclName_Type.__name__=_F
_QtechAclName_Object=MibTableColumn
qtechAclName=_QtechAclName_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,1,1,1),_QtechAclName_Type())
qtechAclName.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechAclName.setStatus(_A)
class _QtechAclMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('acl-ip-standard',1),('acl-ip-extended',2),('acl-mac-extended',3),('acl-expert',4),('acl-ipv6-extended',5)))
_QtechAclMode_Type.__name__=_H
_QtechAclMode_Object=MibTableColumn
qtechAclMode=_QtechAclMode_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,1,1,2),_QtechAclMode_Type())
qtechAclMode.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechAclMode.setStatus(_A)
_QtechAclEntryStatus_Type=ConfigStatus
_QtechAclEntryStatus_Object=MibTableColumn
qtechAclEntryStatus=_QtechAclEntryStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,1,1,3),_QtechAclEntryStatus_Type())
qtechAclEntryStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechAclEntryStatus.setStatus(_A)
_QtechAclIfTable_Object=MibTable
qtechAclIfTable=_QtechAclIfTable_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,3))
if mibBuilder.loadTexts:qtechAclIfTable.setStatus(_A)
_QtechAclIfEntry_Object=MibTableRow
qtechAclIfEntry=_QtechAclIfEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,3,1))
qtechAclIfEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:qtechAclIfEntry.setStatus(_A)
_QtechAclIfIndex_Type=IfIndex
_QtechAclIfIndex_Object=MibTableColumn
qtechAclIfIndex=_QtechAclIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,3,1,1),_QtechAclIfIndex_Type())
qtechAclIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechAclIfIndex.setStatus(_A)
_QtechAclIfMaxEntryNum_Type=Integer32
_QtechAclIfMaxEntryNum_Object=MibTableColumn
qtechAclIfMaxEntryNum=_QtechAclIfMaxEntryNum_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,3,1,2),_QtechAclIfMaxEntryNum_Type())
qtechAclIfMaxEntryNum.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechAclIfMaxEntryNum.setStatus(_A)
_QtechAclIfCurruntEntryNum_Type=Integer32
_QtechAclIfCurruntEntryNum_Object=MibTableColumn
qtechAclIfCurruntEntryNum=_QtechAclIfCurruntEntryNum_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,3,1,3),_QtechAclIfCurruntEntryNum_Type())
qtechAclIfCurruntEntryNum.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechAclIfCurruntEntryNum.setStatus(_A)
class _QtechIfInAclName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechIfInAclName_Type.__name__=_F
_QtechIfInAclName_Object=MibTableColumn
qtechIfInAclName=_QtechIfInAclName_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,3,1,4),_QtechIfInAclName_Type())
qtechIfInAclName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfInAclName.setStatus(_A)
class _QtechIfOutAclName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechIfOutAclName_Type.__name__=_F
_QtechIfOutAclName_Object=MibTableColumn
qtechIfOutAclName=_QtechIfOutAclName_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,3,1,5),_QtechIfOutAclName_Type())
qtechIfOutAclName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfOutAclName.setStatus(_A)
_QtechAclIf6MaxEntryNum_Type=Integer32
_QtechAclIf6MaxEntryNum_Object=MibTableColumn
qtechAclIf6MaxEntryNum=_QtechAclIf6MaxEntryNum_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,3,1,6),_QtechAclIf6MaxEntryNum_Type())
qtechAclIf6MaxEntryNum.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechAclIf6MaxEntryNum.setStatus(_A)
_QtechAclIf6CurruntEntryNum_Type=Integer32
_QtechAclIf6CurruntEntryNum_Object=MibTableColumn
qtechAclIf6CurruntEntryNum=_QtechAclIf6CurruntEntryNum_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,3,1,7),_QtechAclIf6CurruntEntryNum_Type())
qtechAclIf6CurruntEntryNum.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechAclIf6CurruntEntryNum.setStatus(_A)
class _QtechIf6InAclName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechIf6InAclName_Type.__name__=_F
_QtechIf6InAclName_Object=MibTableColumn
qtechIf6InAclName=_QtechIf6InAclName_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,3,1,8),_QtechIf6InAclName_Type())
qtechIf6InAclName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIf6InAclName.setStatus(_A)
class _QtechIf6OutAclName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechIf6OutAclName_Type.__name__=_F
_QtechIf6OutAclName_Object=MibTableColumn
qtechIf6OutAclName=_QtechIf6OutAclName_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,3,1,9),_QtechIf6OutAclName_Type())
qtechIf6OutAclName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIf6OutAclName.setStatus(_A)
_QtechAceExtTable_Object=MibTable
qtechAceExtTable=_QtechAceExtTable_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4))
if mibBuilder.loadTexts:qtechAceExtTable.setStatus(_A)
_QtechAceExtEntry_Object=MibTableRow
qtechAceExtEntry=_QtechAceExtEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1))
qtechAceExtEntry.setIndexNames((0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:qtechAceExtEntry.setStatus(_A)
class _QtechAceExtAclName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechAceExtAclName_Type.__name__=_F
_QtechAceExtAclName_Object=MibTableColumn
qtechAceExtAclName=_QtechAceExtAclName_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,1),_QtechAceExtAclName_Type())
qtechAceExtAclName.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechAceExtAclName.setStatus(_A)
class _QtechAceExtIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_QtechAceExtIndex_Type.__name__=_H
_QtechAceExtIndex_Object=MibTableColumn
qtechAceExtIndex=_QtechAceExtIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,2),_QtechAceExtIndex_Type())
qtechAceExtIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechAceExtIndex.setStatus(_A)
class _QtechAceExtIfAnyVID_Type(TruthValue):defaultValue=1
_QtechAceExtIfAnyVID_Type.__name__=_E
_QtechAceExtIfAnyVID_Object=MibTableColumn
qtechAceExtIfAnyVID=_QtechAceExtIfAnyVID_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,3),_QtechAceExtIfAnyVID_Type())
qtechAceExtIfAnyVID.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechAceExtIfAnyVID.setStatus(_A)
class _QtechAceExtVID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_QtechAceExtVID_Type.__name__=_O
_QtechAceExtVID_Object=MibTableColumn
qtechAceExtVID=_QtechAceExtVID_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,4),_QtechAceExtVID_Type())
qtechAceExtVID.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechAceExtVID.setStatus(_A)
class _QtechAceExtIfAnySourceIp_Type(TruthValue):defaultValue=1
_QtechAceExtIfAnySourceIp_Type.__name__=_E
_QtechAceExtIfAnySourceIp_Object=MibTableColumn
qtechAceExtIfAnySourceIp=_QtechAceExtIfAnySourceIp_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,5),_QtechAceExtIfAnySourceIp_Type())
qtechAceExtIfAnySourceIp.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechAceExtIfAnySourceIp.setStatus(_A)
_QtechAceExtSourceIp_Type=IpAddress
_QtechAceExtSourceIp_Object=MibTableColumn
qtechAceExtSourceIp=_QtechAceExtSourceIp_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,6),_QtechAceExtSourceIp_Type())
qtechAceExtSourceIp.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechAceExtSourceIp.setStatus(_A)
class _QtechAceExtIfAnySourceWildCard_Type(TruthValue):defaultValue=1
_QtechAceExtIfAnySourceWildCard_Type.__name__=_E
_QtechAceExtIfAnySourceWildCard_Object=MibTableColumn
qtechAceExtIfAnySourceWildCard=_QtechAceExtIfAnySourceWildCard_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,7),_QtechAceExtIfAnySourceWildCard_Type())
qtechAceExtIfAnySourceWildCard.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechAceExtIfAnySourceWildCard.setStatus(_A)
_QtechAceExtSourceWildCard_Type=IpAddress
_QtechAceExtSourceWildCard_Object=MibTableColumn
qtechAceExtSourceWildCard=_QtechAceExtSourceWildCard_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,8),_QtechAceExtSourceWildCard_Type())
qtechAceExtSourceWildCard.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechAceExtSourceWildCard.setStatus(_A)
class _QtechAceExtIfAnySourceMacAddr_Type(TruthValue):defaultValue=1
_QtechAceExtIfAnySourceMacAddr_Type.__name__=_E
_QtechAceExtIfAnySourceMacAddr_Object=MibTableColumn
qtechAceExtIfAnySourceMacAddr=_QtechAceExtIfAnySourceMacAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,9),_QtechAceExtIfAnySourceMacAddr_Type())
qtechAceExtIfAnySourceMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechAceExtIfAnySourceMacAddr.setStatus(_A)
_QtechAceExtSourceMacAddr_Type=MacAddress
_QtechAceExtSourceMacAddr_Object=MibTableColumn
qtechAceExtSourceMacAddr=_QtechAceExtSourceMacAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,10),_QtechAceExtSourceMacAddr_Type())
qtechAceExtSourceMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechAceExtSourceMacAddr.setStatus(_A)
class _QtechAceExtIfAnyDestIp_Type(TruthValue):defaultValue=1
_QtechAceExtIfAnyDestIp_Type.__name__=_E
_QtechAceExtIfAnyDestIp_Object=MibTableColumn
qtechAceExtIfAnyDestIp=_QtechAceExtIfAnyDestIp_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,11),_QtechAceExtIfAnyDestIp_Type())
qtechAceExtIfAnyDestIp.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechAceExtIfAnyDestIp.setStatus(_A)
_QtechAceExtDestIp_Type=IpAddress
_QtechAceExtDestIp_Object=MibTableColumn
qtechAceExtDestIp=_QtechAceExtDestIp_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,12),_QtechAceExtDestIp_Type())
qtechAceExtDestIp.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechAceExtDestIp.setStatus(_A)
class _QtechAceExtIfAnyDestWildCard_Type(TruthValue):defaultValue=1
_QtechAceExtIfAnyDestWildCard_Type.__name__=_E
_QtechAceExtIfAnyDestWildCard_Object=MibTableColumn
qtechAceExtIfAnyDestWildCard=_QtechAceExtIfAnyDestWildCard_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,13),_QtechAceExtIfAnyDestWildCard_Type())
qtechAceExtIfAnyDestWildCard.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechAceExtIfAnyDestWildCard.setStatus(_A)
_QtechAceExtDestIpWildCard_Type=IpAddress
_QtechAceExtDestIpWildCard_Object=MibTableColumn
qtechAceExtDestIpWildCard=_QtechAceExtDestIpWildCard_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,14),_QtechAceExtDestIpWildCard_Type())
qtechAceExtDestIpWildCard.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechAceExtDestIpWildCard.setStatus(_A)
class _QtechAceExtIfAnyDestMacAddr_Type(TruthValue):defaultValue=1
_QtechAceExtIfAnyDestMacAddr_Type.__name__=_E
_QtechAceExtIfAnyDestMacAddr_Object=MibTableColumn
qtechAceExtIfAnyDestMacAddr=_QtechAceExtIfAnyDestMacAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,15),_QtechAceExtIfAnyDestMacAddr_Type())
qtechAceExtIfAnyDestMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechAceExtIfAnyDestMacAddr.setStatus(_A)
_QtechAceExtDestMacAddr_Type=MacAddress
_QtechAceExtDestMacAddr_Object=MibTableColumn
qtechAceExtDestMacAddr=_QtechAceExtDestMacAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,16),_QtechAceExtDestMacAddr_Type())
qtechAceExtDestMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechAceExtDestMacAddr.setStatus(_A)
class _QtechAceExtIfAnyEtherLikeType_Type(TruthValue):defaultValue=1
_QtechAceExtIfAnyEtherLikeType_Type.__name__=_E
_QtechAceExtIfAnyEtherLikeType_Object=MibTableColumn
qtechAceExtIfAnyEtherLikeType=_QtechAceExtIfAnyEtherLikeType_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,17),_QtechAceExtIfAnyEtherLikeType_Type())
qtechAceExtIfAnyEtherLikeType.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechAceExtIfAnyEtherLikeType.setStatus(_A)
_QtechAceExtEtherLikeType_Type=Integer32
_QtechAceExtEtherLikeType_Object=MibTableColumn
qtechAceExtEtherLikeType=_QtechAceExtEtherLikeType_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,18),_QtechAceExtEtherLikeType_Type())
qtechAceExtEtherLikeType.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechAceExtEtherLikeType.setStatus(_A)
class _QtechAceExtIfAnyIpProtocolField_Type(TruthValue):defaultValue=1
_QtechAceExtIfAnyIpProtocolField_Type.__name__=_E
_QtechAceExtIfAnyIpProtocolField_Object=MibTableColumn
qtechAceExtIfAnyIpProtocolField=_QtechAceExtIfAnyIpProtocolField_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,19),_QtechAceExtIfAnyIpProtocolField_Type())
qtechAceExtIfAnyIpProtocolField.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechAceExtIfAnyIpProtocolField.setStatus(_A)
_QtechAceExtIpProtocolField_Type=Integer32
_QtechAceExtIpProtocolField_Object=MibTableColumn
qtechAceExtIpProtocolField=_QtechAceExtIpProtocolField_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,20),_QtechAceExtIpProtocolField_Type())
qtechAceExtIpProtocolField.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechAceExtIpProtocolField.setStatus(_A)
_QtechAceExtSourceProtocolPort_Type=Integer32
_QtechAceExtSourceProtocolPort_Object=MibTableColumn
qtechAceExtSourceProtocolPort=_QtechAceExtSourceProtocolPort_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,21),_QtechAceExtSourceProtocolPort_Type())
qtechAceExtSourceProtocolPort.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechAceExtSourceProtocolPort.setStatus(_A)
_QtechAceExtDestProtocolPort_Type=Integer32
_QtechAceExtDestProtocolPort_Object=MibTableColumn
qtechAceExtDestProtocolPort=_QtechAceExtDestProtocolPort_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,22),_QtechAceExtDestProtocolPort_Type())
qtechAceExtDestProtocolPort.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechAceExtDestProtocolPort.setStatus(_A)
class _QtechAceExtIfAnyProtocolType_Type(TruthValue):defaultValue=1
_QtechAceExtIfAnyProtocolType_Type.__name__=_E
_QtechAceExtIfAnyProtocolType_Object=MibTableColumn
qtechAceExtIfAnyProtocolType=_QtechAceExtIfAnyProtocolType_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,23),_QtechAceExtIfAnyProtocolType_Type())
qtechAceExtIfAnyProtocolType.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechAceExtIfAnyProtocolType.setStatus(_A)
_QtechAceExtProtocolType_Type=Integer32
_QtechAceExtProtocolType_Object=MibTableColumn
qtechAceExtProtocolType=_QtechAceExtProtocolType_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,24),_QtechAceExtProtocolType_Type())
qtechAceExtProtocolType.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechAceExtProtocolType.setStatus(_A)
class _QtechAceExtFlowAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('permit',1),('deny',2)))
_QtechAceExtFlowAction_Type.__name__=_H
_QtechAceExtFlowAction_Object=MibTableColumn
qtechAceExtFlowAction=_QtechAceExtFlowAction_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,25),_QtechAceExtFlowAction_Type())
qtechAceExtFlowAction.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechAceExtFlowAction.setStatus(_A)
_QtechAceExtEntryStauts_Type=RowStatus
_QtechAceExtEntryStauts_Object=MibTableColumn
qtechAceExtEntryStauts=_QtechAceExtEntryStauts_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,26),_QtechAceExtEntryStauts_Type())
qtechAceExtEntryStauts.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechAceExtEntryStauts.setStatus(_A)
class _QtechAceExtTimeRangeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechAceExtTimeRangeName_Type.__name__=_F
_QtechAceExtTimeRangeName_Object=MibTableColumn
qtechAceExtTimeRangeName=_QtechAceExtTimeRangeName_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,27),_QtechAceExtTimeRangeName_Type())
qtechAceExtTimeRangeName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAceExtTimeRangeName.setStatus(_A)
class _QtechAceExtSourcePortOp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_P,1),('lt',2),('gt',3),('eq',4),('neq',5),('range',6)))
_QtechAceExtSourcePortOp_Type.__name__=_H
_QtechAceExtSourcePortOp_Object=MibTableColumn
qtechAceExtSourcePortOp=_QtechAceExtSourcePortOp_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,28),_QtechAceExtSourcePortOp_Type())
qtechAceExtSourcePortOp.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAceExtSourcePortOp.setStatus(_A)
_QtechAceExtSourceProtocolPortRange_Type=Integer32
_QtechAceExtSourceProtocolPortRange_Object=MibTableColumn
qtechAceExtSourceProtocolPortRange=_QtechAceExtSourceProtocolPortRange_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,29),_QtechAceExtSourceProtocolPortRange_Type())
qtechAceExtSourceProtocolPortRange.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAceExtSourceProtocolPortRange.setStatus(_A)
class _QtechAceExtDestPortOp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_P,1),('lt',2),('gt',3),('eq',4),('neq',5),('range',6)))
_QtechAceExtDestPortOp_Type.__name__=_H
_QtechAceExtDestPortOp_Object=MibTableColumn
qtechAceExtDestPortOp=_QtechAceExtDestPortOp_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,30),_QtechAceExtDestPortOp_Type())
qtechAceExtDestPortOp.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAceExtDestPortOp.setStatus(_A)
_QtechAceExtDestProtocolPortRange_Type=Integer32
_QtechAceExtDestProtocolPortRange_Object=MibTableColumn
qtechAceExtDestProtocolPortRange=_QtechAceExtDestProtocolPortRange_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,31),_QtechAceExtDestProtocolPortRange_Type())
qtechAceExtDestProtocolPortRange.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAceExtDestProtocolPortRange.setStatus(_A)
class _QtechAceExtIfAnyCos_Type(TruthValue):defaultValue=1
_QtechAceExtIfAnyCos_Type.__name__=_E
_QtechAceExtIfAnyCos_Object=MibTableColumn
qtechAceExtIfAnyCos=_QtechAceExtIfAnyCos_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,32),_QtechAceExtIfAnyCos_Type())
qtechAceExtIfAnyCos.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAceExtIfAnyCos.setStatus(_A)
_QtechAceExtCos_Type=Integer32
_QtechAceExtCos_Object=MibTableColumn
qtechAceExtCos=_QtechAceExtCos_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,33),_QtechAceExtCos_Type())
qtechAceExtCos.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAceExtCos.setStatus(_A)
class _QtechAceExtIfAnyIpPrec_Type(TruthValue):defaultValue=1
_QtechAceExtIfAnyIpPrec_Type.__name__=_E
_QtechAceExtIfAnyIpPrec_Object=MibTableColumn
qtechAceExtIfAnyIpPrec=_QtechAceExtIfAnyIpPrec_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,34),_QtechAceExtIfAnyIpPrec_Type())
qtechAceExtIfAnyIpPrec.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAceExtIfAnyIpPrec.setStatus(_A)
_QtechAceExtIpPrec_Type=Integer32
_QtechAceExtIpPrec_Object=MibTableColumn
qtechAceExtIpPrec=_QtechAceExtIpPrec_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,35),_QtechAceExtIpPrec_Type())
qtechAceExtIpPrec.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAceExtIpPrec.setStatus(_A)
class _QtechAceExtIfAnyDscp_Type(TruthValue):defaultValue=1
_QtechAceExtIfAnyDscp_Type.__name__=_E
_QtechAceExtIfAnyDscp_Object=MibTableColumn
qtechAceExtIfAnyDscp=_QtechAceExtIfAnyDscp_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,36),_QtechAceExtIfAnyDscp_Type())
qtechAceExtIfAnyDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAceExtIfAnyDscp.setStatus(_A)
_QtechAceExtDscp_Type=Integer32
_QtechAceExtDscp_Object=MibTableColumn
qtechAceExtDscp=_QtechAceExtDscp_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,37),_QtechAceExtDscp_Type())
qtechAceExtDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAceExtDscp.setStatus(_A)
class _QtechAceExtIfAnyTcpFlag_Type(TruthValue):defaultValue=1
_QtechAceExtIfAnyTcpFlag_Type.__name__=_E
_QtechAceExtIfAnyTcpFlag_Object=MibTableColumn
qtechAceExtIfAnyTcpFlag=_QtechAceExtIfAnyTcpFlag_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,38),_QtechAceExtIfAnyTcpFlag_Type())
qtechAceExtIfAnyTcpFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAceExtIfAnyTcpFlag.setStatus(_A)
_QtechAceExtTcpFlag_Type=Integer32
_QtechAceExtTcpFlag_Object=MibTableColumn
qtechAceExtTcpFlag=_QtechAceExtTcpFlag_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,39),_QtechAceExtTcpFlag_Type())
qtechAceExtTcpFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAceExtTcpFlag.setStatus(_A)
class _QtechAceExtIfAnySourceMacAddrWildCard_Type(TruthValue):defaultValue=1
_QtechAceExtIfAnySourceMacAddrWildCard_Type.__name__=_E
_QtechAceExtIfAnySourceMacAddrWildCard_Object=MibTableColumn
qtechAceExtIfAnySourceMacAddrWildCard=_QtechAceExtIfAnySourceMacAddrWildCard_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,40),_QtechAceExtIfAnySourceMacAddrWildCard_Type())
qtechAceExtIfAnySourceMacAddrWildCard.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAceExtIfAnySourceMacAddrWildCard.setStatus(_A)
_QtechAceExtSourceMacAddrWildCard_Type=MacAddress
_QtechAceExtSourceMacAddrWildCard_Object=MibTableColumn
qtechAceExtSourceMacAddrWildCard=_QtechAceExtSourceMacAddrWildCard_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,41),_QtechAceExtSourceMacAddrWildCard_Type())
qtechAceExtSourceMacAddrWildCard.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAceExtSourceMacAddrWildCard.setStatus(_A)
class _QtechAceExtIfAnyDestMacAddrWildCard_Type(TruthValue):defaultValue=1
_QtechAceExtIfAnyDestMacAddrWildCard_Type.__name__=_E
_QtechAceExtIfAnyDestMacAddrWildCard_Object=MibTableColumn
qtechAceExtIfAnyDestMacAddrWildCard=_QtechAceExtIfAnyDestMacAddrWildCard_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,42),_QtechAceExtIfAnyDestMacAddrWildCard_Type())
qtechAceExtIfAnyDestMacAddrWildCard.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAceExtIfAnyDestMacAddrWildCard.setStatus(_A)
_QtechAceExtDestMacAddrWildCard_Type=MacAddress
_QtechAceExtDestMacAddrWildCard_Object=MibTableColumn
qtechAceExtDestMacAddrWildCard=_QtechAceExtDestMacAddrWildCard_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,43),_QtechAceExtDestMacAddrWildCard_Type())
qtechAceExtDestMacAddrWildCard.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAceExtDestMacAddrWildCard.setStatus(_A)
class _QtechAceExtIfAnySourceIp6_Type(TruthValue):defaultValue=1
_QtechAceExtIfAnySourceIp6_Type.__name__=_E
_QtechAceExtIfAnySourceIp6_Object=MibTableColumn
qtechAceExtIfAnySourceIp6=_QtechAceExtIfAnySourceIp6_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,44),_QtechAceExtIfAnySourceIp6_Type())
qtechAceExtIfAnySourceIp6.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAceExtIfAnySourceIp6.setStatus(_A)
class _QtechAceExtSourceIp6_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_QtechAceExtSourceIp6_Type.__name__=_I
_QtechAceExtSourceIp6_Object=MibTableColumn
qtechAceExtSourceIp6=_QtechAceExtSourceIp6_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,45),_QtechAceExtSourceIp6_Type())
qtechAceExtSourceIp6.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAceExtSourceIp6.setStatus(_A)
class _QtechAceExtIfAnySourceIp6WildCard_Type(TruthValue):defaultValue=1
_QtechAceExtIfAnySourceIp6WildCard_Type.__name__=_E
_QtechAceExtIfAnySourceIp6WildCard_Object=MibTableColumn
qtechAceExtIfAnySourceIp6WildCard=_QtechAceExtIfAnySourceIp6WildCard_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,46),_QtechAceExtIfAnySourceIp6WildCard_Type())
qtechAceExtIfAnySourceIp6WildCard.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAceExtIfAnySourceIp6WildCard.setStatus(_A)
class _QtechAceExtSourceIp6WildCard_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_QtechAceExtSourceIp6WildCard_Type.__name__=_I
_QtechAceExtSourceIp6WildCard_Object=MibTableColumn
qtechAceExtSourceIp6WildCard=_QtechAceExtSourceIp6WildCard_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,47),_QtechAceExtSourceIp6WildCard_Type())
qtechAceExtSourceIp6WildCard.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAceExtSourceIp6WildCard.setStatus(_A)
class _QtechAceExtIfAnyDestIp6_Type(TruthValue):defaultValue=1
_QtechAceExtIfAnyDestIp6_Type.__name__=_E
_QtechAceExtIfAnyDestIp6_Object=MibTableColumn
qtechAceExtIfAnyDestIp6=_QtechAceExtIfAnyDestIp6_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,48),_QtechAceExtIfAnyDestIp6_Type())
qtechAceExtIfAnyDestIp6.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAceExtIfAnyDestIp6.setStatus(_A)
class _QtechAceExtDestIp6_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_QtechAceExtDestIp6_Type.__name__=_I
_QtechAceExtDestIp6_Object=MibTableColumn
qtechAceExtDestIp6=_QtechAceExtDestIp6_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,49),_QtechAceExtDestIp6_Type())
qtechAceExtDestIp6.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAceExtDestIp6.setStatus(_A)
class _QtechAceExtIfAnyDestIp6WildCard_Type(TruthValue):defaultValue=1
_QtechAceExtIfAnyDestIp6WildCard_Type.__name__=_E
_QtechAceExtIfAnyDestIp6WildCard_Object=MibTableColumn
qtechAceExtIfAnyDestIp6WildCard=_QtechAceExtIfAnyDestIp6WildCard_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,50),_QtechAceExtIfAnyDestIp6WildCard_Type())
qtechAceExtIfAnyDestIp6WildCard.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAceExtIfAnyDestIp6WildCard.setStatus(_A)
class _QtechAceExtDestIp6WildCard_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_QtechAceExtDestIp6WildCard_Type.__name__=_I
_QtechAceExtDestIp6WildCard_Object=MibTableColumn
qtechAceExtDestIp6WildCard=_QtechAceExtDestIp6WildCard_Object((1,3,6,1,4,1,27514,1,1,10,2,17,1,4,1,51),_QtechAceExtDestIp6WildCard_Type())
qtechAceExtDestIp6WildCard.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAceExtDestIp6WildCard.setStatus(_A)
_QtechAclMIBConformance_ObjectIdentity=ObjectIdentity
qtechAclMIBConformance=_QtechAclMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,17,2))
_QtechAclMIBCompliances_ObjectIdentity=ObjectIdentity
qtechAclMIBCompliances=_QtechAclMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,17,2,1))
_QtechAclMIBGroups_ObjectIdentity=ObjectIdentity
qtechAclMIBGroups=_QtechAclMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,17,2,2))
qtechAclMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,17,2,2,1))
qtechAclMIBGroup.setObjects(*((_B,_J),(_B,_Q),(_B,_R),(_B,_L),(_B,_M),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_N),(_B,_N),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_K),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG)))
if mibBuilder.loadTexts:qtechAclMIBGroup.setStatus(_A)
qtechAclMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,17,2,1,1))
qtechAclMIBCompliance.setObjects((_B,_AH))
if mibBuilder.loadTexts:qtechAclMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechAclMIB':qtechAclMIB,'qtechAclMIBObjects':qtechAclMIBObjects,'qtechAclTable':qtechAclTable,'qtechAclEntry':qtechAclEntry,_J:qtechAclName,_Q:qtechAclMode,_R:qtechAclEntryStatus,'qtechAclIfTable':qtechAclIfTable,'qtechAclIfEntry':qtechAclIfEntry,_K:qtechAclIfIndex,_AD:qtechAclIfMaxEntryNum,_AE:qtechAclIfCurruntEntryNum,_AF:qtechIfInAclName,_AG:qtechIfOutAclName,'qtechAclIf6MaxEntryNum':qtechAclIf6MaxEntryNum,'qtechAclIf6CurruntEntryNum':qtechAclIf6CurruntEntryNum,'qtechIf6InAclName':qtechIf6InAclName,'qtechIf6OutAclName':qtechIf6OutAclName,'qtechAceExtTable':qtechAceExtTable,'qtechAceExtEntry':qtechAceExtEntry,_L:qtechAceExtAclName,_M:qtechAceExtIndex,_S:qtechAceExtIfAnyVID,_T:qtechAceExtVID,_U:qtechAceExtIfAnySourceIp,_V:qtechAceExtSourceIp,_W:qtechAceExtIfAnySourceWildCard,_X:qtechAceExtSourceWildCard,_Y:qtechAceExtIfAnySourceMacAddr,_Z:qtechAceExtSourceMacAddr,_a:qtechAceExtIfAnyDestIp,_b:qtechAceExtDestIp,_c:qtechAceExtIfAnyDestWildCard,_d:qtechAceExtDestIpWildCard,_e:qtechAceExtIfAnyDestMacAddr,_f:qtechAceExtDestMacAddr,_g:qtechAceExtIfAnyEtherLikeType,_h:qtechAceExtEtherLikeType,_i:qtechAceExtIfAnyIpProtocolField,_j:qtechAceExtIpProtocolField,_k:qtechAceExtSourceProtocolPort,_l:qtechAceExtDestProtocolPort,'qtechAceExtIfAnyProtocolType':qtechAceExtIfAnyProtocolType,_N:qtechAceExtProtocolType,_m:qtechAceExtFlowAction,_n:qtechAceExtEntryStauts,_o:qtechAceExtTimeRangeName,_p:qtechAceExtSourcePortOp,_q:qtechAceExtSourceProtocolPortRange,_r:qtechAceExtDestPortOp,_s:qtechAceExtDestProtocolPortRange,_t:qtechAceExtIfAnyCos,_u:qtechAceExtCos,_v:qtechAceExtIfAnyIpPrec,_w:qtechAceExtIpPrec,_x:qtechAceExtIfAnyDscp,_y:qtechAceExtDscp,_z:qtechAceExtIfAnyTcpFlag,_A0:qtechAceExtTcpFlag,_A1:qtechAceExtIfAnySourceMacAddrWildCard,_A2:qtechAceExtSourceMacAddrWildCard,_A3:qtechAceExtIfAnyDestMacAddrWildCard,_A4:qtechAceExtDestMacAddrWildCard,_A5:qtechAceExtIfAnySourceIp6,_A6:qtechAceExtSourceIp6,_A7:qtechAceExtIfAnySourceIp6WildCard,_A8:qtechAceExtSourceIp6WildCard,_A9:qtechAceExtIfAnyDestIp6,_AA:qtechAceExtDestIp6,_AB:qtechAceExtIfAnyDestIp6WildCard,_AC:qtechAceExtDestIp6WildCard,'qtechAclMIBConformance':qtechAclMIBConformance,'qtechAclMIBCompliances':qtechAclMIBCompliances,'qtechAclMIBCompliance':qtechAclMIBCompliance,'qtechAclMIBGroups':qtechAclMIBGroups,_AH:qtechAclMIBGroup})