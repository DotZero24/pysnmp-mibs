_Z='h3cL2vpnPwId'
_Y='h3cL2vpnPwPeerIp'
_X='h3cL2vpnAcSrvId'
_W='h3cL2vpnAcIfIndex'
_V='h3cL2vpnXcgAcEvcSrvInstId'
_U='h3cL2vpnXcgAcIfIndex'
_T='h3cL2vpnLinkLinkID'
_S='h3cL2vpnLinkVsiIndex'
_R='ethernet'
_Q='h3cL2vpnPwcName'
_P='TruthValue'
_O='accessible-for-notify'
_N='h3cL2vpnXcgConnName'
_M='unknown'
_L='h3cL2vpnXcgPwPwID'
_K='h3cL2vpnXcgPwPeerIp'
_J='h3cL2vpnXcgName'
_I='h3cL2vpnXcgPwIndex'
_H='OctetString'
_G='DisplayString'
_F='not-accessible'
_E='Integer32'
_D='read-create'
_C='read-only'
_B='H3C-L2VPN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','RowStatus','TextualConvention',_P)
h3cL2vpn=ModuleIdentity((1,3,6,1,4,1,2011,10,2,162))
if mibBuilder.loadTexts:h3cL2vpn.setRevisions(('2018-01-17 15:00','2017-11-21 15:00','2016-09-30 18:00','2015-01-16 00:00'))
_H3cL2vpnPwNotifications_ObjectIdentity=ObjectIdentity
h3cL2vpnPwNotifications=_H3cL2vpnPwNotifications_ObjectIdentity((1,3,6,1,4,1,2011,10,2,162,0))
_H3cL2vpnGlobalTable_ObjectIdentity=ObjectIdentity
h3cL2vpnGlobalTable=_H3cL2vpnGlobalTable_ObjectIdentity((1,3,6,1,4,1,2011,10,2,162,2))
_H3cL2vpnPwcTable_Object=MibTable
h3cL2vpnPwcTable=_H3cL2vpnPwcTable_Object((1,3,6,1,4,1,2011,10,2,162,2,1))
if mibBuilder.loadTexts:h3cL2vpnPwcTable.setStatus(_A)
_H3cL2vpnPwcEntry_Object=MibTableRow
h3cL2vpnPwcEntry=_H3cL2vpnPwcEntry_Object((1,3,6,1,4,1,2011,10,2,162,2,1,1))
h3cL2vpnPwcEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:h3cL2vpnPwcEntry.setStatus(_A)
class _H3cL2vpnPwcName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,19))
_H3cL2vpnPwcName_Type.__name__=_H
_H3cL2vpnPwcName_Object=MibTableColumn
h3cL2vpnPwcName=_H3cL2vpnPwcName_Object((1,3,6,1,4,1,2011,10,2,162,2,1,1,1),_H3cL2vpnPwcName_Type())
h3cL2vpnPwcName.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cL2vpnPwcName.setStatus(_A)
class _H3cL2vpnPwcCvType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),('bfd',2),('rawBFD',3)))
_H3cL2vpnPwcCvType_Type.__name__=_E
_H3cL2vpnPwcCvType_Object=MibTableColumn
h3cL2vpnPwcCvType=_H3cL2vpnPwcCvType_Object((1,3,6,1,4,1,2011,10,2,162,2,1,1,2),_H3cL2vpnPwcCvType_Type())
h3cL2vpnPwcCvType.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cL2vpnPwcCvType.setStatus(_A)
class _H3cL2vpnPwcCcType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),('controlWord',2),('routerAlert',3),('ttl',4)))
_H3cL2vpnPwcCcType_Type.__name__=_E
_H3cL2vpnPwcCcType_Object=MibTableColumn
h3cL2vpnPwcCcType=_H3cL2vpnPwcCcType_Object((1,3,6,1,4,1,2011,10,2,162,2,1,1,3),_H3cL2vpnPwcCcType_Type())
h3cL2vpnPwcCcType.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cL2vpnPwcCcType.setStatus(_A)
class _H3cL2vpnPwcControlWord_Type(TruthValue):defaultValue=2
_H3cL2vpnPwcControlWord_Type.__name__=_P
_H3cL2vpnPwcControlWord_Object=MibTableColumn
h3cL2vpnPwcControlWord=_H3cL2vpnPwcControlWord_Object((1,3,6,1,4,1,2011,10,2,162,2,1,1,4),_H3cL2vpnPwcControlWord_Type())
h3cL2vpnPwcControlWord.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cL2vpnPwcControlWord.setStatus(_A)
class _H3cL2vpnPwcPwType_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(4,5)));namedValues=NamedValues(*(('vlan',4),(_R,5)))
_H3cL2vpnPwcPwType_Type.__name__=_E
_H3cL2vpnPwcPwType_Object=MibTableColumn
h3cL2vpnPwcPwType=_H3cL2vpnPwcPwType_Object((1,3,6,1,4,1,2011,10,2,162,2,1,1,5),_H3cL2vpnPwcPwType_Type())
h3cL2vpnPwcPwType.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cL2vpnPwcPwType.setStatus(_A)
_H3cL2vpnPwcRowStatus_Type=RowStatus
_H3cL2vpnPwcRowStatus_Object=MibTableColumn
h3cL2vpnPwcRowStatus=_H3cL2vpnPwcRowStatus_Object((1,3,6,1,4,1,2011,10,2,162,2,1,1,6),_H3cL2vpnPwcRowStatus_Type())
h3cL2vpnPwcRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cL2vpnPwcRowStatus.setStatus(_A)
class _H3cL2vpnPwcFlowLabel_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),('send',2),('receive',3),('both',4)))
_H3cL2vpnPwcFlowLabel_Type.__name__=_E
_H3cL2vpnPwcFlowLabel_Object=MibTableColumn
h3cL2vpnPwcFlowLabel=_H3cL2vpnPwcFlowLabel_Object((1,3,6,1,4,1,2011,10,2,162,2,1,1,7),_H3cL2vpnPwcFlowLabel_Type())
h3cL2vpnPwcFlowLabel.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cL2vpnPwcFlowLabel.setStatus(_A)
_H3cL2vpnLinkTable_Object=MibTable
h3cL2vpnLinkTable=_H3cL2vpnLinkTable_Object((1,3,6,1,4,1,2011,10,2,162,2,2))
if mibBuilder.loadTexts:h3cL2vpnLinkTable.setStatus(_A)
_H3cL2vpnLinkEntry_Object=MibTableRow
h3cL2vpnLinkEntry=_H3cL2vpnLinkEntry_Object((1,3,6,1,4,1,2011,10,2,162,2,2,1))
h3cL2vpnLinkEntry.setIndexNames((0,_B,_S),(0,_B,_T))
if mibBuilder.loadTexts:h3cL2vpnLinkEntry.setStatus(_A)
_H3cL2vpnLinkVsiIndex_Type=Unsigned32
_H3cL2vpnLinkVsiIndex_Object=MibTableColumn
h3cL2vpnLinkVsiIndex=_H3cL2vpnLinkVsiIndex_Object((1,3,6,1,4,1,2011,10,2,162,2,2,1,1),_H3cL2vpnLinkVsiIndex_Type())
h3cL2vpnLinkVsiIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cL2vpnLinkVsiIndex.setStatus(_A)
_H3cL2vpnLinkLinkID_Type=Unsigned32
_H3cL2vpnLinkLinkID_Object=MibTableColumn
h3cL2vpnLinkLinkID=_H3cL2vpnLinkLinkID_Object((1,3,6,1,4,1,2011,10,2,162,2,2,1,2),_H3cL2vpnLinkLinkID_Type())
h3cL2vpnLinkLinkID.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cL2vpnLinkLinkID.setStatus(_A)
class _H3cL2vpnLinkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),('ac',2),('tunnel',3)))
_H3cL2vpnLinkType_Type.__name__=_E
_H3cL2vpnLinkType_Object=MibTableColumn
h3cL2vpnLinkType=_H3cL2vpnLinkType_Object((1,3,6,1,4,1,2011,10,2,162,2,2,1,3),_H3cL2vpnLinkType_Type())
h3cL2vpnLinkType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cL2vpnLinkType.setStatus(_A)
_H3cL2vpnLinkIfIndex_Type=InterfaceIndex
_H3cL2vpnLinkIfIndex_Object=MibTableColumn
h3cL2vpnLinkIfIndex=_H3cL2vpnLinkIfIndex_Object((1,3,6,1,4,1,2011,10,2,162,2,2,1,4),_H3cL2vpnLinkIfIndex_Type())
h3cL2vpnLinkIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cL2vpnLinkIfIndex.setStatus(_A)
_H3cL2vpnLinkSrvID_Type=Unsigned32
_H3cL2vpnLinkSrvID_Object=MibTableColumn
h3cL2vpnLinkSrvID=_H3cL2vpnLinkSrvID_Object((1,3,6,1,4,1,2011,10,2,162,2,2,1,5),_H3cL2vpnLinkSrvID_Type())
h3cL2vpnLinkSrvID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cL2vpnLinkSrvID.setStatus(_A)
_H3cL2vpnLinkTunnelID_Type=Unsigned32
_H3cL2vpnLinkTunnelID_Object=MibTableColumn
h3cL2vpnLinkTunnelID=_H3cL2vpnLinkTunnelID_Object((1,3,6,1,4,1,2011,10,2,162,2,2,1,6),_H3cL2vpnLinkTunnelID_Type())
h3cL2vpnLinkTunnelID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cL2vpnLinkTunnelID.setStatus(_A)
_H3cL2vpnVpwsTable_ObjectIdentity=ObjectIdentity
h3cL2vpnVpwsTable=_H3cL2vpnVpwsTable_ObjectIdentity((1,3,6,1,4,1,2011,10,2,162,3))
_H3cL2vpnXcgTable_Object=MibTable
h3cL2vpnXcgTable=_H3cL2vpnXcgTable_Object((1,3,6,1,4,1,2011,10,2,162,3,1))
if mibBuilder.loadTexts:h3cL2vpnXcgTable.setStatus(_A)
_H3cL2vpnXcgEntry_Object=MibTableRow
h3cL2vpnXcgEntry=_H3cL2vpnXcgEntry_Object((1,3,6,1,4,1,2011,10,2,162,3,1,1))
h3cL2vpnXcgEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:h3cL2vpnXcgEntry.setStatus(_A)
class _H3cL2vpnXcgName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_H3cL2vpnXcgName_Type.__name__=_H
_H3cL2vpnXcgName_Object=MibTableColumn
h3cL2vpnXcgName=_H3cL2vpnXcgName_Object((1,3,6,1,4,1,2011,10,2,162,3,1,1,1),_H3cL2vpnXcgName_Type())
h3cL2vpnXcgName.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cL2vpnXcgName.setStatus(_A)
class _H3cL2vpnXcgAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('adminUp',1),('adminDown',2)))
_H3cL2vpnXcgAdminState_Type.__name__=_E
_H3cL2vpnXcgAdminState_Object=MibTableColumn
h3cL2vpnXcgAdminState=_H3cL2vpnXcgAdminState_Object((1,3,6,1,4,1,2011,10,2,162,3,1,1,2),_H3cL2vpnXcgAdminState_Type())
h3cL2vpnXcgAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cL2vpnXcgAdminState.setStatus(_A)
_H3cL2vpnXcgRowStatus_Type=RowStatus
_H3cL2vpnXcgRowStatus_Object=MibTableColumn
h3cL2vpnXcgRowStatus=_H3cL2vpnXcgRowStatus_Object((1,3,6,1,4,1,2011,10,2,162,3,1,1,3),_H3cL2vpnXcgRowStatus_Type())
h3cL2vpnXcgRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cL2vpnXcgRowStatus.setStatus(_A)
_H3cL2vpnXcgConnTable_Object=MibTable
h3cL2vpnXcgConnTable=_H3cL2vpnXcgConnTable_Object((1,3,6,1,4,1,2011,10,2,162,3,2))
if mibBuilder.loadTexts:h3cL2vpnXcgConnTable.setStatus(_A)
_H3cL2vpnXcgConnEntry_Object=MibTableRow
h3cL2vpnXcgConnEntry=_H3cL2vpnXcgConnEntry_Object((1,3,6,1,4,1,2011,10,2,162,3,2,1))
h3cL2vpnXcgConnEntry.setIndexNames((0,_B,_J),(0,_B,_N))
if mibBuilder.loadTexts:h3cL2vpnXcgConnEntry.setStatus(_A)
class _H3cL2vpnXcgConnName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_H3cL2vpnXcgConnName_Type.__name__=_H
_H3cL2vpnXcgConnName_Object=MibTableColumn
h3cL2vpnXcgConnName=_H3cL2vpnXcgConnName_Object((1,3,6,1,4,1,2011,10,2,162,3,2,1,1),_H3cL2vpnXcgConnName_Type())
h3cL2vpnXcgConnName.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cL2vpnXcgConnName.setStatus(_A)
_H3cL2vpnXcgConnRowStatus_Type=RowStatus
_H3cL2vpnXcgConnRowStatus_Object=MibTableColumn
h3cL2vpnXcgConnRowStatus=_H3cL2vpnXcgConnRowStatus_Object((1,3,6,1,4,1,2011,10,2,162,3,2,1,2),_H3cL2vpnXcgConnRowStatus_Type())
h3cL2vpnXcgConnRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cL2vpnXcgConnRowStatus.setStatus(_A)
_H3cL2vpnXcgAcTable_Object=MibTable
h3cL2vpnXcgAcTable=_H3cL2vpnXcgAcTable_Object((1,3,6,1,4,1,2011,10,2,162,3,3))
if mibBuilder.loadTexts:h3cL2vpnXcgAcTable.setStatus(_A)
_H3cL2vpnXcgAcEntry_Object=MibTableRow
h3cL2vpnXcgAcEntry=_H3cL2vpnXcgAcEntry_Object((1,3,6,1,4,1,2011,10,2,162,3,3,1))
h3cL2vpnXcgAcEntry.setIndexNames((0,_B,_J),(0,_B,_N),(0,_B,_U),(0,_B,_V))
if mibBuilder.loadTexts:h3cL2vpnXcgAcEntry.setStatus(_A)
_H3cL2vpnXcgAcIfIndex_Type=InterfaceIndex
_H3cL2vpnXcgAcIfIndex_Object=MibTableColumn
h3cL2vpnXcgAcIfIndex=_H3cL2vpnXcgAcIfIndex_Object((1,3,6,1,4,1,2011,10,2,162,3,3,1,1),_H3cL2vpnXcgAcIfIndex_Type())
h3cL2vpnXcgAcIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cL2vpnXcgAcIfIndex.setStatus(_A)
_H3cL2vpnXcgAcEvcSrvInstId_Type=Unsigned32
_H3cL2vpnXcgAcEvcSrvInstId_Object=MibTableColumn
h3cL2vpnXcgAcEvcSrvInstId=_H3cL2vpnXcgAcEvcSrvInstId_Object((1,3,6,1,4,1,2011,10,2,162,3,3,1,2),_H3cL2vpnXcgAcEvcSrvInstId_Type())
h3cL2vpnXcgAcEvcSrvInstId.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cL2vpnXcgAcEvcSrvInstId.setStatus(_A)
class _H3cL2vpnXcgAcAccessMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('vlan',1),(_R,2)))
_H3cL2vpnXcgAcAccessMode_Type.__name__=_E
_H3cL2vpnXcgAcAccessMode_Object=MibTableColumn
h3cL2vpnXcgAcAccessMode=_H3cL2vpnXcgAcAccessMode_Object((1,3,6,1,4,1,2011,10,2,162,3,3,1,3),_H3cL2vpnXcgAcAccessMode_Type())
h3cL2vpnXcgAcAccessMode.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cL2vpnXcgAcAccessMode.setStatus(_A)
_H3cL2vpnXcgAcRowStatus_Type=RowStatus
_H3cL2vpnXcgAcRowStatus_Object=MibTableColumn
h3cL2vpnXcgAcRowStatus=_H3cL2vpnXcgAcRowStatus_Object((1,3,6,1,4,1,2011,10,2,162,3,3,1,4),_H3cL2vpnXcgAcRowStatus_Type())
h3cL2vpnXcgAcRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cL2vpnXcgAcRowStatus.setStatus(_A)
_H3cL2vpnXcgPwTable_Object=MibTable
h3cL2vpnXcgPwTable=_H3cL2vpnXcgPwTable_Object((1,3,6,1,4,1,2011,10,2,162,3,4))
if mibBuilder.loadTexts:h3cL2vpnXcgPwTable.setStatus(_A)
_H3cL2vpnXcgPwEntry_Object=MibTableRow
h3cL2vpnXcgPwEntry=_H3cL2vpnXcgPwEntry_Object((1,3,6,1,4,1,2011,10,2,162,3,4,1))
h3cL2vpnXcgPwEntry.setIndexNames((0,_B,_J),(0,_B,_N),(0,_B,_I))
if mibBuilder.loadTexts:h3cL2vpnXcgPwEntry.setStatus(_A)
_H3cL2vpnXcgPwIndex_Type=Unsigned32
_H3cL2vpnXcgPwIndex_Object=MibTableColumn
h3cL2vpnXcgPwIndex=_H3cL2vpnXcgPwIndex_Object((1,3,6,1,4,1,2011,10,2,162,3,4,1,1),_H3cL2vpnXcgPwIndex_Type())
h3cL2vpnXcgPwIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:h3cL2vpnXcgPwIndex.setStatus(_A)
class _H3cL2vpnXcgPwCfgType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('primary',1),('backup',2)))
_H3cL2vpnXcgPwCfgType_Type.__name__=_E
_H3cL2vpnXcgPwCfgType_Object=MibTableColumn
h3cL2vpnXcgPwCfgType=_H3cL2vpnXcgPwCfgType_Object((1,3,6,1,4,1,2011,10,2,162,3,4,1,2),_H3cL2vpnXcgPwCfgType_Type())
h3cL2vpnXcgPwCfgType.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cL2vpnXcgPwCfgType.setStatus(_A)
class _H3cL2vpnXcgPwClassName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,19))
_H3cL2vpnXcgPwClassName_Type.__name__=_H
_H3cL2vpnXcgPwClassName_Object=MibTableColumn
h3cL2vpnXcgPwClassName=_H3cL2vpnXcgPwClassName_Object((1,3,6,1,4,1,2011,10,2,162,3,4,1,3),_H3cL2vpnXcgPwClassName_Type())
h3cL2vpnXcgPwClassName.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cL2vpnXcgPwClassName.setStatus(_A)
class _H3cL2vpnXcgPwTunnelPolicy_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,19))
_H3cL2vpnXcgPwTunnelPolicy_Type.__name__=_H
_H3cL2vpnXcgPwTunnelPolicy_Object=MibTableColumn
h3cL2vpnXcgPwTunnelPolicy=_H3cL2vpnXcgPwTunnelPolicy_Object((1,3,6,1,4,1,2011,10,2,162,3,4,1,4),_H3cL2vpnXcgPwTunnelPolicy_Type())
h3cL2vpnXcgPwTunnelPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cL2vpnXcgPwTunnelPolicy.setStatus(_A)
_H3cL2vpnXcgPwPeerIp_Type=IpAddress
_H3cL2vpnXcgPwPeerIp_Object=MibTableColumn
h3cL2vpnXcgPwPeerIp=_H3cL2vpnXcgPwPeerIp_Object((1,3,6,1,4,1,2011,10,2,162,3,4,1,5),_H3cL2vpnXcgPwPeerIp_Type())
h3cL2vpnXcgPwPeerIp.setMaxAccess(_O)
if mibBuilder.loadTexts:h3cL2vpnXcgPwPeerIp.setStatus(_A)
_H3cL2vpnXcgPwPwID_Type=Unsigned32
_H3cL2vpnXcgPwPwID_Object=MibTableColumn
h3cL2vpnXcgPwPwID=_H3cL2vpnXcgPwPwID_Object((1,3,6,1,4,1,2011,10,2,162,3,4,1,6),_H3cL2vpnXcgPwPwID_Type())
h3cL2vpnXcgPwPwID.setMaxAccess(_O)
if mibBuilder.loadTexts:h3cL2vpnXcgPwPwID.setStatus(_A)
_H3cL2vpnXcgPwRowStatus_Type=RowStatus
_H3cL2vpnXcgPwRowStatus_Object=MibTableColumn
h3cL2vpnXcgPwRowStatus=_H3cL2vpnXcgPwRowStatus_Object((1,3,6,1,4,1,2011,10,2,162,3,4,1,7),_H3cL2vpnXcgPwRowStatus_Type())
h3cL2vpnXcgPwRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cL2vpnXcgPwRowStatus.setStatus(_A)
_H3cL2vpnAcTable_ObjectIdentity=ObjectIdentity
h3cL2vpnAcTable=_H3cL2vpnAcTable_ObjectIdentity((1,3,6,1,4,1,2011,10,2,162,4))
_H3cL2vpnAcCfgTable_Object=MibTable
h3cL2vpnAcCfgTable=_H3cL2vpnAcCfgTable_Object((1,3,6,1,4,1,2011,10,2,162,4,1))
if mibBuilder.loadTexts:h3cL2vpnAcCfgTable.setStatus(_A)
_H3cL2vpnAcCfgEntry_Object=MibTableRow
h3cL2vpnAcCfgEntry=_H3cL2vpnAcCfgEntry_Object((1,3,6,1,4,1,2011,10,2,162,4,1,1))
h3cL2vpnAcCfgEntry.setIndexNames((0,_B,_W),(0,_B,_X))
if mibBuilder.loadTexts:h3cL2vpnAcCfgEntry.setStatus(_A)
_H3cL2vpnAcIfIndex_Type=InterfaceIndex
_H3cL2vpnAcIfIndex_Object=MibTableColumn
h3cL2vpnAcIfIndex=_H3cL2vpnAcIfIndex_Object((1,3,6,1,4,1,2011,10,2,162,4,1,1,1),_H3cL2vpnAcIfIndex_Type())
h3cL2vpnAcIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cL2vpnAcIfIndex.setStatus(_A)
_H3cL2vpnAcSrvId_Type=Unsigned32
_H3cL2vpnAcSrvId_Object=MibTableColumn
h3cL2vpnAcSrvId=_H3cL2vpnAcSrvId_Object((1,3,6,1,4,1,2011,10,2,162,4,1,1,2),_H3cL2vpnAcSrvId_Type())
h3cL2vpnAcSrvId.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cL2vpnAcSrvId.setStatus(_A)
class _H3cL2vpnAcIfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cL2vpnAcIfName_Type.__name__=_G
_H3cL2vpnAcIfName_Object=MibTableColumn
h3cL2vpnAcIfName=_H3cL2vpnAcIfName_Object((1,3,6,1,4,1,2011,10,2,162,4,1,1,3),_H3cL2vpnAcIfName_Type())
h3cL2vpnAcIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cL2vpnAcIfName.setStatus(_A)
class _H3cL2vpnAcVsiName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cL2vpnAcVsiName_Type.__name__=_G
_H3cL2vpnAcVsiName_Object=MibTableColumn
h3cL2vpnAcVsiName=_H3cL2vpnAcVsiName_Object((1,3,6,1,4,1,2011,10,2,162,4,1,1,4),_H3cL2vpnAcVsiName_Type())
h3cL2vpnAcVsiName.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cL2vpnAcVsiName.setStatus(_A)
class _H3cL2vpnAcXcgName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cL2vpnAcXcgName_Type.__name__=_G
_H3cL2vpnAcXcgName_Object=MibTableColumn
h3cL2vpnAcXcgName=_H3cL2vpnAcXcgName_Object((1,3,6,1,4,1,2011,10,2,162,4,1,1,5),_H3cL2vpnAcXcgName_Type())
h3cL2vpnAcXcgName.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cL2vpnAcXcgName.setStatus(_A)
class _H3cL2vpnAcXcgConnName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cL2vpnAcXcgConnName_Type.__name__=_G
_H3cL2vpnAcXcgConnName_Object=MibTableColumn
h3cL2vpnAcXcgConnName=_H3cL2vpnAcXcgConnName_Object((1,3,6,1,4,1,2011,10,2,162,4,1,1,6),_H3cL2vpnAcXcgConnName_Type())
h3cL2vpnAcXcgConnName.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cL2vpnAcXcgConnName.setStatus(_A)
class _H3cL2vpnAcDot1qType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('default',2),('singletag',3)))
_H3cL2vpnAcDot1qType_Type.__name__=_E
_H3cL2vpnAcDot1qType_Object=MibTableColumn
h3cL2vpnAcDot1qType=_H3cL2vpnAcDot1qType_Object((1,3,6,1,4,1,2011,10,2,162,4,1,1,7),_H3cL2vpnAcDot1qType_Type())
h3cL2vpnAcDot1qType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cL2vpnAcDot1qType.setStatus(_A)
_H3cL2vpnAcVLANID_Type=Unsigned32
_H3cL2vpnAcVLANID_Object=MibTableColumn
h3cL2vpnAcVLANID=_H3cL2vpnAcVLANID_Object((1,3,6,1,4,1,2011,10,2,162,4,1,1,8),_H3cL2vpnAcVLANID_Type())
h3cL2vpnAcVLANID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cL2vpnAcVLANID.setStatus(_A)
_H3cL2vpnPwTable_ObjectIdentity=ObjectIdentity
h3cL2vpnPwTable=_H3cL2vpnPwTable_ObjectIdentity((1,3,6,1,4,1,2011,10,2,162,5))
_H3cL2vpnPwCfgTable_Object=MibTable
h3cL2vpnPwCfgTable=_H3cL2vpnPwCfgTable_Object((1,3,6,1,4,1,2011,10,2,162,5,1))
if mibBuilder.loadTexts:h3cL2vpnPwCfgTable.setStatus(_A)
_H3cL2vpnPwCfgEntry_Object=MibTableRow
h3cL2vpnPwCfgEntry=_H3cL2vpnPwCfgEntry_Object((1,3,6,1,4,1,2011,10,2,162,5,1,1))
h3cL2vpnPwCfgEntry.setIndexNames((0,_B,_Y),(0,_B,_Z))
if mibBuilder.loadTexts:h3cL2vpnPwCfgEntry.setStatus(_A)
_H3cL2vpnPwPeerIp_Type=IpAddress
_H3cL2vpnPwPeerIp_Object=MibTableColumn
h3cL2vpnPwPeerIp=_H3cL2vpnPwPeerIp_Object((1,3,6,1,4,1,2011,10,2,162,5,1,1,1),_H3cL2vpnPwPeerIp_Type())
h3cL2vpnPwPeerIp.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cL2vpnPwPeerIp.setStatus(_A)
_H3cL2vpnPwId_Type=Unsigned32
_H3cL2vpnPwId_Object=MibTableColumn
h3cL2vpnPwId=_H3cL2vpnPwId_Object((1,3,6,1,4,1,2011,10,2,162,5,1,1,2),_H3cL2vpnPwId_Type())
h3cL2vpnPwId.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cL2vpnPwId.setStatus(_A)
_H3cL2vpnPwAcIfIndex_Type=InterfaceIndexOrZero
_H3cL2vpnPwAcIfIndex_Object=MibTableColumn
h3cL2vpnPwAcIfIndex=_H3cL2vpnPwAcIfIndex_Object((1,3,6,1,4,1,2011,10,2,162,5,1,1,3),_H3cL2vpnPwAcIfIndex_Type())
h3cL2vpnPwAcIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cL2vpnPwAcIfIndex.setStatus(_A)
class _H3cL2vpnPwAcIfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cL2vpnPwAcIfName_Type.__name__=_G
_H3cL2vpnPwAcIfName_Object=MibTableColumn
h3cL2vpnPwAcIfName=_H3cL2vpnPwAcIfName_Object((1,3,6,1,4,1,2011,10,2,162,5,1,1,4),_H3cL2vpnPwAcIfName_Type())
h3cL2vpnPwAcIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cL2vpnPwAcIfName.setStatus(_A)
_H3cL2vpnPwAcSrvId_Type=Unsigned32
_H3cL2vpnPwAcSrvId_Object=MibTableColumn
h3cL2vpnPwAcSrvId=_H3cL2vpnPwAcSrvId_Object((1,3,6,1,4,1,2011,10,2,162,5,1,1,5),_H3cL2vpnPwAcSrvId_Type())
h3cL2vpnPwAcSrvId.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cL2vpnPwAcSrvId.setStatus(_A)
class _H3cL2vpnPwVsiName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cL2vpnPwVsiName_Type.__name__=_G
_H3cL2vpnPwVsiName_Object=MibTableColumn
h3cL2vpnPwVsiName=_H3cL2vpnPwVsiName_Object((1,3,6,1,4,1,2011,10,2,162,5,1,1,6),_H3cL2vpnPwVsiName_Type())
h3cL2vpnPwVsiName.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cL2vpnPwVsiName.setStatus(_A)
class _H3cL2vpnPwXcgName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cL2vpnPwXcgName_Type.__name__=_G
_H3cL2vpnPwXcgName_Object=MibTableColumn
h3cL2vpnPwXcgName=_H3cL2vpnPwXcgName_Object((1,3,6,1,4,1,2011,10,2,162,5,1,1,7),_H3cL2vpnPwXcgName_Type())
h3cL2vpnPwXcgName.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cL2vpnPwXcgName.setStatus(_A)
class _H3cL2vpnPwXcgConnName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cL2vpnPwXcgConnName_Type.__name__=_G
_H3cL2vpnPwXcgConnName_Object=MibTableColumn
h3cL2vpnPwXcgConnName=_H3cL2vpnPwXcgConnName_Object((1,3,6,1,4,1,2011,10,2,162,5,1,1,8),_H3cL2vpnPwXcgConnName_Type())
h3cL2vpnPwXcgConnName.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cL2vpnPwXcgConnName.setStatus(_A)
class _H3cL2vpnPwQosDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('inbound',2),('outbound',3),('both',4)))
_H3cL2vpnPwQosDirection_Type.__name__=_E
_H3cL2vpnPwQosDirection_Object=MibTableColumn
h3cL2vpnPwQosDirection=_H3cL2vpnPwQosDirection_Object((1,3,6,1,4,1,2011,10,2,162,5,1,1,9),_H3cL2vpnPwQosDirection_Type())
h3cL2vpnPwQosDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cL2vpnPwQosDirection.setStatus(_A)
_H3cL2vpnPwInboundQosCir_Type=Unsigned32
_H3cL2vpnPwInboundQosCir_Object=MibTableColumn
h3cL2vpnPwInboundQosCir=_H3cL2vpnPwInboundQosCir_Object((1,3,6,1,4,1,2011,10,2,162,5,1,1,10),_H3cL2vpnPwInboundQosCir_Type())
h3cL2vpnPwInboundQosCir.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cL2vpnPwInboundQosCir.setStatus(_A)
_H3cL2vpnPwInboundQosCbs_Type=Unsigned32
_H3cL2vpnPwInboundQosCbs_Object=MibTableColumn
h3cL2vpnPwInboundQosCbs=_H3cL2vpnPwInboundQosCbs_Object((1,3,6,1,4,1,2011,10,2,162,5,1,1,11),_H3cL2vpnPwInboundQosCbs_Type())
h3cL2vpnPwInboundQosCbs.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cL2vpnPwInboundQosCbs.setStatus(_A)
_H3cL2vpnPwInboundQosEbs_Type=Unsigned32
_H3cL2vpnPwInboundQosEbs_Object=MibTableColumn
h3cL2vpnPwInboundQosEbs=_H3cL2vpnPwInboundQosEbs_Object((1,3,6,1,4,1,2011,10,2,162,5,1,1,12),_H3cL2vpnPwInboundQosEbs_Type())
h3cL2vpnPwInboundQosEbs.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cL2vpnPwInboundQosEbs.setStatus(_A)
_H3cL2vpnPwOutboundQosCir_Type=Unsigned32
_H3cL2vpnPwOutboundQosCir_Object=MibTableColumn
h3cL2vpnPwOutboundQosCir=_H3cL2vpnPwOutboundQosCir_Object((1,3,6,1,4,1,2011,10,2,162,5,1,1,13),_H3cL2vpnPwOutboundQosCir_Type())
h3cL2vpnPwOutboundQosCir.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cL2vpnPwOutboundQosCir.setStatus(_A)
_H3cL2vpnPwOutboundQosCbs_Type=Unsigned32
_H3cL2vpnPwOutboundQosCbs_Object=MibTableColumn
h3cL2vpnPwOutboundQosCbs=_H3cL2vpnPwOutboundQosCbs_Object((1,3,6,1,4,1,2011,10,2,162,5,1,1,14),_H3cL2vpnPwOutboundQosCbs_Type())
h3cL2vpnPwOutboundQosCbs.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cL2vpnPwOutboundQosCbs.setStatus(_A)
_H3cL2vpnPwOutboundQosEbs_Type=Unsigned32
_H3cL2vpnPwOutboundQosEbs_Object=MibTableColumn
h3cL2vpnPwOutboundQosEbs=_H3cL2vpnPwOutboundQosEbs_Object((1,3,6,1,4,1,2011,10,2,162,5,1,1,15),_H3cL2vpnPwOutboundQosEbs_Type())
h3cL2vpnPwOutboundQosEbs.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cL2vpnPwOutboundQosEbs.setStatus(_A)
h3cL2vpnPwSwitchPtoB=NotificationType((1,3,6,1,4,1,2011,10,2,162,0,1))
h3cL2vpnPwSwitchPtoB.setObjects(*((_B,_I),(_B,_K),(_B,_L),(_B,_I),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:h3cL2vpnPwSwitchPtoB.setStatus(_A)
h3cL2vpnPwSwitchBtoP=NotificationType((1,3,6,1,4,1,2011,10,2,162,0,2))
h3cL2vpnPwSwitchBtoP.setObjects(*((_B,_I),(_B,_K),(_B,_L),(_B,_I),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:h3cL2vpnPwSwitchBtoP.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h3cL2vpn':h3cL2vpn,'h3cL2vpnPwNotifications':h3cL2vpnPwNotifications,'h3cL2vpnPwSwitchPtoB':h3cL2vpnPwSwitchPtoB,'h3cL2vpnPwSwitchBtoP':h3cL2vpnPwSwitchBtoP,'h3cL2vpnGlobalTable':h3cL2vpnGlobalTable,'h3cL2vpnPwcTable':h3cL2vpnPwcTable,'h3cL2vpnPwcEntry':h3cL2vpnPwcEntry,_Q:h3cL2vpnPwcName,'h3cL2vpnPwcCvType':h3cL2vpnPwcCvType,'h3cL2vpnPwcCcType':h3cL2vpnPwcCcType,'h3cL2vpnPwcControlWord':h3cL2vpnPwcControlWord,'h3cL2vpnPwcPwType':h3cL2vpnPwcPwType,'h3cL2vpnPwcRowStatus':h3cL2vpnPwcRowStatus,'h3cL2vpnPwcFlowLabel':h3cL2vpnPwcFlowLabel,'h3cL2vpnLinkTable':h3cL2vpnLinkTable,'h3cL2vpnLinkEntry':h3cL2vpnLinkEntry,_S:h3cL2vpnLinkVsiIndex,_T:h3cL2vpnLinkLinkID,'h3cL2vpnLinkType':h3cL2vpnLinkType,'h3cL2vpnLinkIfIndex':h3cL2vpnLinkIfIndex,'h3cL2vpnLinkSrvID':h3cL2vpnLinkSrvID,'h3cL2vpnLinkTunnelID':h3cL2vpnLinkTunnelID,'h3cL2vpnVpwsTable':h3cL2vpnVpwsTable,'h3cL2vpnXcgTable':h3cL2vpnXcgTable,'h3cL2vpnXcgEntry':h3cL2vpnXcgEntry,_J:h3cL2vpnXcgName,'h3cL2vpnXcgAdminState':h3cL2vpnXcgAdminState,'h3cL2vpnXcgRowStatus':h3cL2vpnXcgRowStatus,'h3cL2vpnXcgConnTable':h3cL2vpnXcgConnTable,'h3cL2vpnXcgConnEntry':h3cL2vpnXcgConnEntry,_N:h3cL2vpnXcgConnName,'h3cL2vpnXcgConnRowStatus':h3cL2vpnXcgConnRowStatus,'h3cL2vpnXcgAcTable':h3cL2vpnXcgAcTable,'h3cL2vpnXcgAcEntry':h3cL2vpnXcgAcEntry,_U:h3cL2vpnXcgAcIfIndex,_V:h3cL2vpnXcgAcEvcSrvInstId,'h3cL2vpnXcgAcAccessMode':h3cL2vpnXcgAcAccessMode,'h3cL2vpnXcgAcRowStatus':h3cL2vpnXcgAcRowStatus,'h3cL2vpnXcgPwTable':h3cL2vpnXcgPwTable,'h3cL2vpnXcgPwEntry':h3cL2vpnXcgPwEntry,_I:h3cL2vpnXcgPwIndex,'h3cL2vpnXcgPwCfgType':h3cL2vpnXcgPwCfgType,'h3cL2vpnXcgPwClassName':h3cL2vpnXcgPwClassName,'h3cL2vpnXcgPwTunnelPolicy':h3cL2vpnXcgPwTunnelPolicy,_K:h3cL2vpnXcgPwPeerIp,_L:h3cL2vpnXcgPwPwID,'h3cL2vpnXcgPwRowStatus':h3cL2vpnXcgPwRowStatus,'h3cL2vpnAcTable':h3cL2vpnAcTable,'h3cL2vpnAcCfgTable':h3cL2vpnAcCfgTable,'h3cL2vpnAcCfgEntry':h3cL2vpnAcCfgEntry,_W:h3cL2vpnAcIfIndex,_X:h3cL2vpnAcSrvId,'h3cL2vpnAcIfName':h3cL2vpnAcIfName,'h3cL2vpnAcVsiName':h3cL2vpnAcVsiName,'h3cL2vpnAcXcgName':h3cL2vpnAcXcgName,'h3cL2vpnAcXcgConnName':h3cL2vpnAcXcgConnName,'h3cL2vpnAcDot1qType':h3cL2vpnAcDot1qType,'h3cL2vpnAcVLANID':h3cL2vpnAcVLANID,'h3cL2vpnPwTable':h3cL2vpnPwTable,'h3cL2vpnPwCfgTable':h3cL2vpnPwCfgTable,'h3cL2vpnPwCfgEntry':h3cL2vpnPwCfgEntry,_Y:h3cL2vpnPwPeerIp,_Z:h3cL2vpnPwId,'h3cL2vpnPwAcIfIndex':h3cL2vpnPwAcIfIndex,'h3cL2vpnPwAcIfName':h3cL2vpnPwAcIfName,'h3cL2vpnPwAcSrvId':h3cL2vpnPwAcSrvId,'h3cL2vpnPwVsiName':h3cL2vpnPwVsiName,'h3cL2vpnPwXcgName':h3cL2vpnPwXcgName,'h3cL2vpnPwXcgConnName':h3cL2vpnPwXcgConnName,'h3cL2vpnPwQosDirection':h3cL2vpnPwQosDirection,'h3cL2vpnPwInboundQosCir':h3cL2vpnPwInboundQosCir,'h3cL2vpnPwInboundQosCbs':h3cL2vpnPwInboundQosCbs,'h3cL2vpnPwInboundQosEbs':h3cL2vpnPwInboundQosEbs,'h3cL2vpnPwOutboundQosCir':h3cL2vpnPwOutboundQosCir,'h3cL2vpnPwOutboundQosCbs':h3cL2vpnPwOutboundQosCbs,'h3cL2vpnPwOutboundQosEbs':h3cL2vpnPwOutboundQosEbs})