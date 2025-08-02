_AO='nbVifSecurity'
_AN='nbVifConfigType'
_AM='nbVifPeer'
_AL='nbVifPortList'
_AK='nbVifMask'
_AJ='nbVifIpAddress'
_AI='nbVifName'
_AH='nbVifState'
_AG='nbVifProtocol'
_AF='nbVifPhysType'
_AE='nbVifAdminStatus'
_AD='nbVifDevName'
_AC='nbRtPoliceActionVifName'
_AB='nbRtPoliceActionVifDirection'
_AA='nbRtPoliceRateLimitCoSlevel'
_A9='nbRtPoliceRateLimitName'
_A8='redAllnoCoS'
_A7='redTCPnoCoS'
_A6='noREDnoCoS'
_A5='nbRtPoliceActionName'
_A4='nbRtActionListName'
_A3='nbRtPortTagId'
_A2='nbAclVifId'
_A1='nbAclVifDirection'
_A0='nbRtVifPortId'
_z='nbRtDiffServDscpMapPrflInValueId'
_y='nbRtDiffServDscpMapPrflNameId'
_x='nbRtDiffServDscpMapNameId'
_w='nbRtDiffServVptMapPrflInValueId'
_v='nbRtDiffServVptMapPrflNameId'
_u='restoreDefaultConfig'
_t='nbRtDiffServVptMapNameId'
_s='nbRtVifDiffServDirect'
_r='nbRtFibEntryProtocol'
_q='nbRtFibEntryIpMask'
_p='nbRtFibEntryIpAddress'
_o='nbVifAliasLimitDevNo'
_n='nbVifAliasLimitType'
_m='nbVifLimitType'
_l='secure'
_k='unsecure'
_j='manual'
_i='create'
_h='portsIF'
_g='ipV4IF'
_f='nbRtVifId'
_e='supported'
_d='notSupported'
_c='NotificationType'
_b='ifIndex'
_a='IF-MIB'
_Z='disabled'
_Y='paused'
_X='clear'
_W='resume'
_V='pause'
_U='nbRtAccVifDirection'
_T='notActive'
_S='wanFrameRelay'
_R='wanPPP'
_Q='lanEthernet'
_P='DisplayString'
_O='active'
_N='invalid'
_M='valid'
_L='nbVifAliasDev'
_K='nbVifIsAlias'
_J='nbVifDevNo'
_I='nbVifType'
_H='disable'
_G='enable'
_F='other'
_E='Integer32'
_D='RT-CFG-MIB'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_a,_b)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier',_c,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_c,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_P,'PhysAddress','TextualConvention')
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class ActionListName(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
class DirectionType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('ingress',2),('egress',3)))
class AccountCouter(Counter32):0
class AccountCounter64(Counter64):0
_Nbase_ObjectIdentity=ObjectIdentity
nbase=_Nbase_ObjectIdentity((1,3,6,1,4,1,629))
_NbSwitchG1_ObjectIdentity=ObjectIdentity
nbSwitchG1=_NbSwitchG1_ObjectIdentity((1,3,6,1,4,1,629,1))
_NbSwitchG1Il_ObjectIdentity=ObjectIdentity
nbSwitchG1Il=_NbSwitchG1Il_ObjectIdentity((1,3,6,1,4,1,629,1,50))
_NbRouterConfig_ObjectIdentity=ObjectIdentity
nbRouterConfig=_NbRouterConfig_ObjectIdentity((1,3,6,1,4,1,629,1,50,12))
_NbRtConfigGen_ObjectIdentity=ObjectIdentity
nbRtConfigGen=_NbRtConfigGen_ObjectIdentity((1,3,6,1,4,1,629,1,50,12,1))
class _NbRtDevDiffServMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('none',2),('byTOS',3),('byTag',4)))
_NbRtDevDiffServMode_Type.__name__=_E
_NbRtDevDiffServMode_Object=MibScalar
nbRtDevDiffServMode=_NbRtDevDiffServMode_Object((1,3,6,1,4,1,629,1,50,12,1,1),_NbRtDevDiffServMode_Type())
nbRtDevDiffServMode.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtDevDiffServMode.setStatus(_A)
class _NbRtDevDiffServMappingSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_d,1),(_e,2)))
_NbRtDevDiffServMappingSupport_Type.__name__=_E
_NbRtDevDiffServMappingSupport_Object=MibScalar
nbRtDevDiffServMappingSupport=_NbRtDevDiffServMappingSupport_Object((1,3,6,1,4,1,629,1,50,12,1,2),_NbRtDevDiffServMappingSupport_Type())
nbRtDevDiffServMappingSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtDevDiffServMappingSupport.setStatus(_A)
_NbRtVifTable_Object=MibTable
nbRtVifTable=_NbRtVifTable_Object((1,3,6,1,4,1,629,1,50,12,2))
if mibBuilder.loadTexts:nbRtVifTable.setStatus(_A)
_NbRtVifEntry_Object=MibTableRow
nbRtVifEntry=_NbRtVifEntry_Object((1,3,6,1,4,1,629,1,50,12,2,1))
nbRtVifEntry.setIndexNames((0,_D,_f))
if mibBuilder.loadTexts:nbRtVifEntry.setStatus(_A)
_NbRtVifId_Type=DisplayString
_NbRtVifId_Object=MibTableColumn
nbRtVifId=_NbRtVifId_Object((1,3,6,1,4,1,629,1,50,12,2,1,1),_NbRtVifId_Type())
nbRtVifId.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtVifId.setStatus(_A)
_NbRtVifIpAddress_Type=IpAddress
_NbRtVifIpAddress_Object=MibTableColumn
nbRtVifIpAddress=_NbRtVifIpAddress_Object((1,3,6,1,4,1,629,1,50,12,2,1,2),_NbRtVifIpAddress_Type())
nbRtVifIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtVifIpAddress.setStatus(_A)
_NbRtVifMask_Type=IpAddress
_NbRtVifMask_Object=MibTableColumn
nbRtVifMask=_NbRtVifMask_Object((1,3,6,1,4,1,629,1,50,12,2,1,3),_NbRtVifMask_Type())
nbRtVifMask.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtVifMask.setStatus(_A)
class _NbRtVifProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_g,2),('ipxIF',3),(_h,4)))
_NbRtVifProtocol_Type.__name__=_E
_NbRtVifProtocol_Object=MibTableColumn
nbRtVifProtocol=_NbRtVifProtocol_Object((1,3,6,1,4,1,629,1,50,12,2,1,4),_NbRtVifProtocol_Type())
nbRtVifProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtVifProtocol.setStatus(_A)
_NbRtVifName_Type=DisplayString
_NbRtVifName_Object=MibTableColumn
nbRtVifName=_NbRtVifName_Object((1,3,6,1,4,1,629,1,50,12,2,1,5),_NbRtVifName_Type())
nbRtVifName.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtVifName.setStatus(_A)
_NbRtVifPortList_Type=OctetString
_NbRtVifPortList_Object=MibTableColumn
nbRtVifPortList=_NbRtVifPortList_Object((1,3,6,1,4,1,629,1,50,12,2,1,6),_NbRtVifPortList_Type())
nbRtVifPortList.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtVifPortList.setStatus(_A)
_NbRtVifMac_Type=MacAddress
_NbRtVifMac_Object=MibTableColumn
nbRtVifMac=_NbRtVifMac_Object((1,3,6,1,4,1,629,1,50,12,2,1,7),_NbRtVifMac_Type())
nbRtVifMac.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtVifMac.setStatus(_A)
class _NbRtVifAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4)));namedValues=NamedValues(*((_M,1),(_N,2),(_i,4)))
_NbRtVifAdminStatus_Type.__name__=_E
_NbRtVifAdminStatus_Object=MibTableColumn
nbRtVifAdminStatus=_NbRtVifAdminStatus_Object((1,3,6,1,4,1,629,1,50,12,2,1,8),_NbRtVifAdminStatus_Type())
nbRtVifAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtVifAdminStatus.setStatus(_A)
class _NbRtVifConfigType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('auto',1),(_j,2)))
_NbRtVifConfigType_Type.__name__=_E
_NbRtVifConfigType_Object=MibTableColumn
nbRtVifConfigType=_NbRtVifConfigType_Object((1,3,6,1,4,1,629,1,50,12,2,1,9),_NbRtVifConfigType_Type())
nbRtVifConfigType.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtVifConfigType.setStatus(_A)
class _NbRtVifSecurity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_k,2),(_l,3)))
_NbRtVifSecurity_Type.__name__=_E
_NbRtVifSecurity_Object=MibTableColumn
nbRtVifSecurity=_NbRtVifSecurity_Object((1,3,6,1,4,1,629,1,50,12,2,1,10),_NbRtVifSecurity_Type())
nbRtVifSecurity.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtVifSecurity.setStatus(_A)
class _NbRtVifIsTagged_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),('yes',1)))
_NbRtVifIsTagged_Type.__name__=_E
_NbRtVifIsTagged_Object=MibTableColumn
nbRtVifIsTagged=_NbRtVifIsTagged_Object((1,3,6,1,4,1,629,1,50,12,2,1,15),_NbRtVifIsTagged_Type())
nbRtVifIsTagged.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtVifIsTagged.setStatus(_A)
class _NbRtVifTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4080))
_NbRtVifTag_Type.__name__=_E
_NbRtVifTag_Object=MibTableColumn
nbRtVifTag=_NbRtVifTag_Object((1,3,6,1,4,1,629,1,50,12,2,1,16),_NbRtVifTag_Type())
nbRtVifTag.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtVifTag.setStatus(_A)
_NbRtVifGroup_ObjectIdentity=ObjectIdentity
nbRtVifGroup=_NbRtVifGroup_ObjectIdentity((1,3,6,1,4,1,629,1,50,12,3))
_NbVifTableSize_Type=Integer32
_NbVifTableSize_Object=MibScalar
nbVifTableSize=_NbVifTableSize_Object((1,3,6,1,4,1,629,1,50,12,3,1),_NbVifTableSize_Type())
nbVifTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVifTableSize.setStatus(_A)
_NbVifDeviceLimitTable_Object=MibTable
nbVifDeviceLimitTable=_NbVifDeviceLimitTable_Object((1,3,6,1,4,1,629,1,50,12,3,2))
if mibBuilder.loadTexts:nbVifDeviceLimitTable.setStatus(_A)
_NbVifDeviceLimitEntry_Object=MibTableRow
nbVifDeviceLimitEntry=_NbVifDeviceLimitEntry_Object((1,3,6,1,4,1,629,1,50,12,3,2,1))
nbVifDeviceLimitEntry.setIndexNames((0,_D,_m))
if mibBuilder.loadTexts:nbVifDeviceLimitEntry.setStatus(_A)
class _NbVifLimitType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_Q,2),(_R,3),(_S,4)))
_NbVifLimitType_Type.__name__=_E
_NbVifLimitType_Object=MibTableColumn
nbVifLimitType=_NbVifLimitType_Object((1,3,6,1,4,1,629,1,50,12,3,2,1,1),_NbVifLimitType_Type())
nbVifLimitType.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVifLimitType.setStatus(_A)
_NbVifDevNoMin_Type=Integer32
_NbVifDevNoMin_Object=MibTableColumn
nbVifDevNoMin=_NbVifDevNoMin_Object((1,3,6,1,4,1,629,1,50,12,3,2,1,2),_NbVifDevNoMin_Type())
nbVifDevNoMin.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVifDevNoMin.setStatus(_A)
_NbVifDevNoMax_Type=Integer32
_NbVifDevNoMax_Object=MibTableColumn
nbVifDevNoMax=_NbVifDevNoMax_Object((1,3,6,1,4,1,629,1,50,12,3,2,1,3),_NbVifDevNoMax_Type())
nbVifDevNoMax.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVifDevNoMax.setStatus(_A)
_NbVifDevNoFirstEmpty_Type=Integer32
_NbVifDevNoFirstEmpty_Object=MibTableColumn
nbVifDevNoFirstEmpty=_NbVifDevNoFirstEmpty_Object((1,3,6,1,4,1,629,1,50,12,3,2,1,4),_NbVifDevNoFirstEmpty_Type())
nbVifDevNoFirstEmpty.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVifDevNoFirstEmpty.setStatus(_A)
_NbVifAliasDLimitTable_Object=MibTable
nbVifAliasDLimitTable=_NbVifAliasDLimitTable_Object((1,3,6,1,4,1,629,1,50,12,3,3))
if mibBuilder.loadTexts:nbVifAliasDLimitTable.setStatus(_A)
_NbVifAliasDLimitEntry_Object=MibTableRow
nbVifAliasDLimitEntry=_NbVifAliasDLimitEntry_Object((1,3,6,1,4,1,629,1,50,12,3,3,1))
nbVifAliasDLimitEntry.setIndexNames((0,_D,_n),(0,_D,_o))
if mibBuilder.loadTexts:nbVifAliasDLimitEntry.setStatus(_A)
class _NbVifAliasLimitType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_Q,2),(_R,3),(_S,4)))
_NbVifAliasLimitType_Type.__name__=_E
_NbVifAliasLimitType_Object=MibTableColumn
nbVifAliasLimitType=_NbVifAliasLimitType_Object((1,3,6,1,4,1,629,1,50,12,3,3,1,1),_NbVifAliasLimitType_Type())
nbVifAliasLimitType.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVifAliasLimitType.setStatus(_A)
_NbVifAliasLimitDevNo_Type=Integer32
_NbVifAliasLimitDevNo_Object=MibTableColumn
nbVifAliasLimitDevNo=_NbVifAliasLimitDevNo_Object((1,3,6,1,4,1,629,1,50,12,3,3,1,2),_NbVifAliasLimitDevNo_Type())
nbVifAliasLimitDevNo.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVifAliasLimitDevNo.setStatus(_A)
_NbVifAliasLimitDevAliasMin_Type=Integer32
_NbVifAliasLimitDevAliasMin_Object=MibTableColumn
nbVifAliasLimitDevAliasMin=_NbVifAliasLimitDevAliasMin_Object((1,3,6,1,4,1,629,1,50,12,3,3,1,3),_NbVifAliasLimitDevAliasMin_Type())
nbVifAliasLimitDevAliasMin.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVifAliasLimitDevAliasMin.setStatus(_A)
_NbVifAliasLimitDevAliasMax_Type=Integer32
_NbVifAliasLimitDevAliasMax_Object=MibTableColumn
nbVifAliasLimitDevAliasMax=_NbVifAliasLimitDevAliasMax_Object((1,3,6,1,4,1,629,1,50,12,3,3,1,4),_NbVifAliasLimitDevAliasMax_Type())
nbVifAliasLimitDevAliasMax.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVifAliasLimitDevAliasMax.setStatus(_A)
_NbVifAliasLimitDevAliasFirstEmpty_Type=Integer32
_NbVifAliasLimitDevAliasFirstEmpty_Object=MibTableColumn
nbVifAliasLimitDevAliasFirstEmpty=_NbVifAliasLimitDevAliasFirstEmpty_Object((1,3,6,1,4,1,629,1,50,12,3,3,1,5),_NbVifAliasLimitDevAliasFirstEmpty_Type())
nbVifAliasLimitDevAliasFirstEmpty.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVifAliasLimitDevAliasFirstEmpty.setStatus(_A)
_NbVifTable_Object=MibTable
nbVifTable=_NbVifTable_Object((1,3,6,1,4,1,629,1,50,12,3,11))
if mibBuilder.loadTexts:nbVifTable.setStatus(_A)
_NbVifEntry_Object=MibTableRow
nbVifEntry=_NbVifEntry_Object((1,3,6,1,4,1,629,1,50,12,3,11,1))
nbVifEntry.setIndexNames((0,_D,_I),(0,_D,_J),(0,_D,_K),(0,_D,_L))
if mibBuilder.loadTexts:nbVifEntry.setStatus(_A)
class _NbVifType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,12)));namedValues=NamedValues(*((_F,1),(_Q,2),(_R,3),(_S,4),('bridge',5),('loopback',6),('dummy',7),('logical',8),('outOfBand',12)))
_NbVifType_Type.__name__=_E
_NbVifType_Object=MibTableColumn
nbVifType=_NbVifType_Object((1,3,6,1,4,1,629,1,50,12,3,11,1,1),_NbVifType_Type())
nbVifType.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVifType.setStatus(_A)
_NbVifDevNo_Type=Integer32
_NbVifDevNo_Object=MibTableColumn
nbVifDevNo=_NbVifDevNo_Object((1,3,6,1,4,1,629,1,50,12,3,11,1,2),_NbVifDevNo_Type())
nbVifDevNo.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVifDevNo.setStatus(_A)
class _NbVifIsAlias_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('primary',2),('alias',3)))
_NbVifIsAlias_Type.__name__=_E
_NbVifIsAlias_Object=MibTableColumn
nbVifIsAlias=_NbVifIsAlias_Object((1,3,6,1,4,1,629,1,50,12,3,11,1,3),_NbVifIsAlias_Type())
nbVifIsAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVifIsAlias.setStatus(_A)
_NbVifAliasDev_Type=Integer32
_NbVifAliasDev_Object=MibTableColumn
nbVifAliasDev=_NbVifAliasDev_Object((1,3,6,1,4,1,629,1,50,12,3,11,1,4),_NbVifAliasDev_Type())
nbVifAliasDev.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVifAliasDev.setStatus(_A)
_NbVifDevName_Type=DisplayString
_NbVifDevName_Object=MibTableColumn
nbVifDevName=_NbVifDevName_Object((1,3,6,1,4,1,629,1,50,12,3,11,1,5),_NbVifDevName_Type())
nbVifDevName.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVifDevName.setStatus(_A)
_NbVifIpAddress_Type=IpAddress
_NbVifIpAddress_Object=MibTableColumn
nbVifIpAddress=_NbVifIpAddress_Object((1,3,6,1,4,1,629,1,50,12,3,11,1,6),_NbVifIpAddress_Type())
nbVifIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:nbVifIpAddress.setStatus(_A)
_NbVifMask_Type=IpAddress
_NbVifMask_Object=MibTableColumn
nbVifMask=_NbVifMask_Object((1,3,6,1,4,1,629,1,50,12,3,11,1,7),_NbVifMask_Type())
nbVifMask.setMaxAccess(_C)
if mibBuilder.loadTexts:nbVifMask.setStatus(_A)
_NbVifPeer_Type=IpAddress
_NbVifPeer_Object=MibTableColumn
nbVifPeer=_NbVifPeer_Object((1,3,6,1,4,1,629,1,50,12,3,11,1,8),_NbVifPeer_Type())
nbVifPeer.setMaxAccess(_C)
if mibBuilder.loadTexts:nbVifPeer.setStatus(_A)
class _NbVifPhysType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('eth0',2),('wp1',3)))
_NbVifPhysType_Type.__name__=_E
_NbVifPhysType_Object=MibTableColumn
nbVifPhysType=_NbVifPhysType_Object((1,3,6,1,4,1,629,1,50,12,3,11,1,9),_NbVifPhysType_Type())
nbVifPhysType.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVifPhysType.setStatus(_A)
class _NbVifProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_g,2),('ipxIF',3),(_h,4)))
_NbVifProtocol_Type.__name__=_E
_NbVifProtocol_Object=MibTableColumn
nbVifProtocol=_NbVifProtocol_Object((1,3,6,1,4,1,629,1,50,12,3,11,1,10),_NbVifProtocol_Type())
nbVifProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:nbVifProtocol.setStatus(_A)
_NbVifName_Type=DisplayString
_NbVifName_Object=MibTableColumn
nbVifName=_NbVifName_Object((1,3,6,1,4,1,629,1,50,12,3,11,1,11),_NbVifName_Type())
nbVifName.setMaxAccess(_C)
if mibBuilder.loadTexts:nbVifName.setStatus(_A)
_NbVifPortList_Type=OctetString
_NbVifPortList_Object=MibTableColumn
nbVifPortList=_NbVifPortList_Object((1,3,6,1,4,1,629,1,50,12,3,11,1,12),_NbVifPortList_Type())
nbVifPortList.setMaxAccess(_C)
if mibBuilder.loadTexts:nbVifPortList.setStatus(_A)
_NbVifMac_Type=MacAddress
_NbVifMac_Object=MibTableColumn
nbVifMac=_NbVifMac_Object((1,3,6,1,4,1,629,1,50,12,3,11,1,13),_NbVifMac_Type())
nbVifMac.setMaxAccess(_C)
if mibBuilder.loadTexts:nbVifMac.setStatus(_A)
class _NbVifState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('up',2),('down',3),('adminDown',4)))
_NbVifState_Type.__name__=_E
_NbVifState_Object=MibTableColumn
nbVifState=_NbVifState_Object((1,3,6,1,4,1,629,1,50,12,3,11,1,14),_NbVifState_Type())
nbVifState.setMaxAccess(_C)
if mibBuilder.loadTexts:nbVifState.setStatus(_A)
class _NbVifAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4)));namedValues=NamedValues(*((_M,1),(_N,2),(_i,4)))
_NbVifAdminStatus_Type.__name__=_E
_NbVifAdminStatus_Object=MibTableColumn
nbVifAdminStatus=_NbVifAdminStatus_Object((1,3,6,1,4,1,629,1,50,12,3,11,1,15),_NbVifAdminStatus_Type())
nbVifAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nbVifAdminStatus.setStatus(_A)
class _NbVifConfigType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('auto',1),(_j,2)))
_NbVifConfigType_Type.__name__=_E
_NbVifConfigType_Object=MibTableColumn
nbVifConfigType=_NbVifConfigType_Object((1,3,6,1,4,1,629,1,50,12,3,11,1,16),_NbVifConfigType_Type())
nbVifConfigType.setMaxAccess(_C)
if mibBuilder.loadTexts:nbVifConfigType.setStatus(_A)
class _NbVifSecurity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_k,2),(_l,3)))
_NbVifSecurity_Type.__name__=_E
_NbVifSecurity_Object=MibTableColumn
nbVifSecurity=_NbVifSecurity_Object((1,3,6,1,4,1,629,1,50,12,3,11,1,17),_NbVifSecurity_Type())
nbVifSecurity.setMaxAccess(_C)
if mibBuilder.loadTexts:nbVifSecurity.setStatus(_A)
class _NbVifIsTagged_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),('yes',1)))
_NbVifIsTagged_Type.__name__=_E
_NbVifIsTagged_Object=MibTableColumn
nbVifIsTagged=_NbVifIsTagged_Object((1,3,6,1,4,1,629,1,50,12,3,11,1,20),_NbVifIsTagged_Type())
nbVifIsTagged.setMaxAccess(_C)
if mibBuilder.loadTexts:nbVifIsTagged.setStatus(_A)
class _NbVifTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4080))
_NbVifTag_Type.__name__=_E
_NbVifTag_Object=MibTableColumn
nbVifTag=_NbVifTag_Object((1,3,6,1,4,1,629,1,50,12,3,11,1,21),_NbVifTag_Type())
nbVifTag.setMaxAccess(_C)
if mibBuilder.loadTexts:nbVifTag.setStatus(_A)
class _NbVifDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_NbVifDescr_Type.__name__=_P
_NbVifDescr_Object=MibTableColumn
nbVifDescr=_NbVifDescr_Object((1,3,6,1,4,1,629,1,50,12,3,11,1,22),_NbVifDescr_Type())
nbVifDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:nbVifDescr.setStatus(_A)
_NbVifLastChange_Type=TimeTicks
_NbVifLastChange_Object=MibTableColumn
nbVifLastChange=_NbVifLastChange_Object((1,3,6,1,4,1,629,1,50,12,3,11,1,23),_NbVifLastChange_Type())
nbVifLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:nbVifLastChange.setStatus(_A)
class _NbVifL2SwitchingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_H,2),('interfaceTagFlood',3),('unicastToLinux',4)))
_NbVifL2SwitchingMode_Type.__name__=_E
_NbVifL2SwitchingMode_Object=MibTableColumn
nbVifL2SwitchingMode=_NbVifL2SwitchingMode_Object((1,3,6,1,4,1,629,1,50,12,3,11,1,24),_NbVifL2SwitchingMode_Type())
nbVifL2SwitchingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:nbVifL2SwitchingMode.setStatus(_A)
class _NbVifProxyArpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),('enableAll',3)))
_NbVifProxyArpMode_Type.__name__=_E
_NbVifProxyArpMode_Object=MibTableColumn
nbVifProxyArpMode=_NbVifProxyArpMode_Object((1,3,6,1,4,1,629,1,50,12,3,11,1,25),_NbVifProxyArpMode_Type())
nbVifProxyArpMode.setMaxAccess(_C)
if mibBuilder.loadTexts:nbVifProxyArpMode.setStatus(_A)
class _NbVifIpOnlyMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_NbVifIpOnlyMode_Type.__name__=_E
_NbVifIpOnlyMode_Object=MibTableColumn
nbVifIpOnlyMode=_NbVifIpOnlyMode_Object((1,3,6,1,4,1,629,1,50,12,3,11,1,26),_NbVifIpOnlyMode_Type())
nbVifIpOnlyMode.setMaxAccess(_C)
if mibBuilder.loadTexts:nbVifIpOnlyMode.setStatus(_A)
class _NbVifIpForwardingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_NbVifIpForwardingMode_Type.__name__=_E
_NbVifIpForwardingMode_Object=MibTableColumn
nbVifIpForwardingMode=_NbVifIpForwardingMode_Object((1,3,6,1,4,1,629,1,50,12,3,11,1,27),_NbVifIpForwardingMode_Type())
nbVifIpForwardingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:nbVifIpForwardingMode.setStatus(_A)
_NbRtFib_ObjectIdentity=ObjectIdentity
nbRtFib=_NbRtFib_ObjectIdentity((1,3,6,1,4,1,629,1,50,12,4))
_NbRtFibNumEntries_Type=Integer32
_NbRtFibNumEntries_Object=MibScalar
nbRtFibNumEntries=_NbRtFibNumEntries_Object((1,3,6,1,4,1,629,1,50,12,4,1),_NbRtFibNumEntries_Type())
nbRtFibNumEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtFibNumEntries.setStatus(_A)
_NbRtFibTable_Object=MibTable
nbRtFibTable=_NbRtFibTable_Object((1,3,6,1,4,1,629,1,50,12,4,2))
if mibBuilder.loadTexts:nbRtFibTable.setStatus(_A)
_NbRtFibEntry_Object=MibTableRow
nbRtFibEntry=_NbRtFibEntry_Object((1,3,6,1,4,1,629,1,50,12,4,2,1))
nbRtFibEntry.setIndexNames((0,_D,_p),(0,_D,_q),(0,_D,_r))
if mibBuilder.loadTexts:nbRtFibEntry.setStatus(_A)
_NbRtFibEntryIpAddress_Type=IpAddress
_NbRtFibEntryIpAddress_Object=MibTableColumn
nbRtFibEntryIpAddress=_NbRtFibEntryIpAddress_Object((1,3,6,1,4,1,629,1,50,12,4,2,1,1),_NbRtFibEntryIpAddress_Type())
nbRtFibEntryIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtFibEntryIpAddress.setStatus(_A)
_NbRtFibEntryIpMask_Type=IpAddress
_NbRtFibEntryIpMask_Object=MibTableColumn
nbRtFibEntryIpMask=_NbRtFibEntryIpMask_Object((1,3,6,1,4,1,629,1,50,12,4,2,1,2),_NbRtFibEntryIpMask_Type())
nbRtFibEntryIpMask.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtFibEntryIpMask.setStatus(_A)
class _NbRtFibEntryProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*((_F,1),('direct',2),('netmgmt',3),('icmp',4),('egp',5),('ggp',6),('hello',7),('rip',8),('is-is',9),('es-is',10),('ciscoIgrp',11),('bbnSpfIgp',12),('ospf',13),('bgp',14),('arp',15),('larp',16)))
_NbRtFibEntryProtocol_Type.__name__=_E
_NbRtFibEntryProtocol_Object=MibTableColumn
nbRtFibEntryProtocol=_NbRtFibEntryProtocol_Object((1,3,6,1,4,1,629,1,50,12,4,2,1,3),_NbRtFibEntryProtocol_Type())
nbRtFibEntryProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtFibEntryProtocol.setStatus(_A)
_NbRtFibEntryNextHop_Type=IpAddress
_NbRtFibEntryNextHop_Object=MibTableColumn
nbRtFibEntryNextHop=_NbRtFibEntryNextHop_Object((1,3,6,1,4,1,629,1,50,12,4,2,1,4),_NbRtFibEntryNextHop_Type())
nbRtFibEntryNextHop.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtFibEntryNextHop.setStatus(_A)
_NbRtFibEntryNextPhysAddress_Type=MacAddress
_NbRtFibEntryNextPhysAddress_Object=MibTableColumn
nbRtFibEntryNextPhysAddress=_NbRtFibEntryNextPhysAddress_Object((1,3,6,1,4,1,629,1,50,12,4,2,1,5),_NbRtFibEntryNextPhysAddress_Type())
nbRtFibEntryNextPhysAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtFibEntryNextPhysAddress.setStatus(_A)
_NbRtFibEntryNextPort_Type=Integer32
_NbRtFibEntryNextPort_Object=MibTableColumn
nbRtFibEntryNextPort=_NbRtFibEntryNextPort_Object((1,3,6,1,4,1,629,1,50,12,4,2,1,6),_NbRtFibEntryNextPort_Type())
nbRtFibEntryNextPort.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtFibEntryNextPort.setStatus(_A)
_NbRtFibEntryLastChTime_Type=Integer32
_NbRtFibEntryLastChTime_Object=MibTableColumn
nbRtFibEntryLastChTime=_NbRtFibEntryLastChTime_Object((1,3,6,1,4,1,629,1,50,12,4,2,1,7),_NbRtFibEntryLastChTime_Type())
nbRtFibEntryLastChTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtFibEntryLastChTime.setStatus(_A)
_NbRtFibEntryAge_Type=Integer32
_NbRtFibEntryAge_Object=MibTableColumn
nbRtFibEntryAge=_NbRtFibEntryAge_Object((1,3,6,1,4,1,629,1,50,12,4,2,1,8),_NbRtFibEntryAge_Type())
nbRtFibEntryAge.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtFibEntryAge.setStatus(_A)
_NbRtFibEntryMetric_Type=Integer32
_NbRtFibEntryMetric_Object=MibTableColumn
nbRtFibEntryMetric=_NbRtFibEntryMetric_Object((1,3,6,1,4,1,629,1,50,12,4,2,1,9),_NbRtFibEntryMetric_Type())
nbRtFibEntryMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtFibEntryMetric.setStatus(_A)
class _NbRtFibEntryAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_NbRtFibEntryAdminStatus_Type.__name__=_E
_NbRtFibEntryAdminStatus_Object=MibTableColumn
nbRtFibEntryAdminStatus=_NbRtFibEntryAdminStatus_Object((1,3,6,1,4,1,629,1,50,12,4,2,1,10),_NbRtFibEntryAdminStatus_Type())
nbRtFibEntryAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtFibEntryAdminStatus.setStatus(_A)
class _NbRtFibEntryTag_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4080))
_NbRtFibEntryTag_Type.__name__=_E
_NbRtFibEntryTag_Object=MibTableColumn
nbRtFibEntryTag=_NbRtFibEntryTag_Object((1,3,6,1,4,1,629,1,50,12,4,2,1,15),_NbRtFibEntryTag_Type())
nbRtFibEntryTag.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtFibEntryTag.setStatus(_A)
_NbRtDiffServ_ObjectIdentity=ObjectIdentity
nbRtDiffServ=_NbRtDiffServ_ObjectIdentity((1,3,6,1,4,1,629,1,50,12,5))
_NbRtDiffServTable_Object=MibTable
nbRtDiffServTable=_NbRtDiffServTable_Object((1,3,6,1,4,1,629,1,50,12,5,2))
if mibBuilder.loadTexts:nbRtDiffServTable.setStatus(_A)
_NbRtDiffServEntry_Object=MibTableRow
nbRtDiffServEntry=_NbRtDiffServEntry_Object((1,3,6,1,4,1,629,1,50,12,5,2,1))
nbRtDiffServEntry.setIndexNames((0,_D,_I),(0,_D,_J),(0,_D,_K),(0,_D,_L))
if mibBuilder.loadTexts:nbRtDiffServEntry.setStatus(_A)
class _NbRtDiffServMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,10)));namedValues=NamedValues(*((_F,1),('none',2),('byTOS',3),('byTag',4),('asGlobal',10)))
_NbRtDiffServMode_Type.__name__=_E
_NbRtDiffServMode_Object=MibTableColumn
nbRtDiffServMode=_NbRtDiffServMode_Object((1,3,6,1,4,1,629,1,50,12,5,2,1,2),_NbRtDiffServMode_Type())
nbRtDiffServMode.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtDiffServMode.setStatus(_A)
_NbRtDiffServVptMapNameIndex_Type=Integer32
_NbRtDiffServVptMapNameIndex_Object=MibTableColumn
nbRtDiffServVptMapNameIndex=_NbRtDiffServVptMapNameIndex_Object((1,3,6,1,4,1,629,1,50,12,5,2,1,3),_NbRtDiffServVptMapNameIndex_Type())
nbRtDiffServVptMapNameIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtDiffServVptMapNameIndex.setStatus(_A)
_NbRtDiffServDscpMapNameIndex_Type=Integer32
_NbRtDiffServDscpMapNameIndex_Object=MibTableColumn
nbRtDiffServDscpMapNameIndex=_NbRtDiffServDscpMapNameIndex_Object((1,3,6,1,4,1,629,1,50,12,5,2,1,4),_NbRtDiffServDscpMapNameIndex_Type())
nbRtDiffServDscpMapNameIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtDiffServDscpMapNameIndex.setStatus(_A)
_NbRtDiffServMgmtVptMapNameIndex_Type=Integer32
_NbRtDiffServMgmtVptMapNameIndex_Object=MibTableColumn
nbRtDiffServMgmtVptMapNameIndex=_NbRtDiffServMgmtVptMapNameIndex_Object((1,3,6,1,4,1,629,1,50,12,5,2,1,5),_NbRtDiffServMgmtVptMapNameIndex_Type())
nbRtDiffServMgmtVptMapNameIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtDiffServMgmtVptMapNameIndex.setStatus(_A)
_NbRtDiffServMgmtDscpMapNameIndex_Type=Integer32
_NbRtDiffServMgmtDscpMapNameIndex_Object=MibTableColumn
nbRtDiffServMgmtDscpMapNameIndex=_NbRtDiffServMgmtDscpMapNameIndex_Object((1,3,6,1,4,1,629,1,50,12,5,2,1,6),_NbRtDiffServMgmtDscpMapNameIndex_Type())
nbRtDiffServMgmtDscpMapNameIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtDiffServMgmtDscpMapNameIndex.setStatus(_A)
_NbRtVifDiffServRateLimitTable_Object=MibTable
nbRtVifDiffServRateLimitTable=_NbRtVifDiffServRateLimitTable_Object((1,3,6,1,4,1,629,1,50,12,5,4))
if mibBuilder.loadTexts:nbRtVifDiffServRateLimitTable.setStatus(_A)
_NbRtVifDiffServRateLimitEntry_Object=MibTableRow
nbRtVifDiffServRateLimitEntry=_NbRtVifDiffServRateLimitEntry_Object((1,3,6,1,4,1,629,1,50,12,5,4,1))
nbRtVifDiffServRateLimitEntry.setIndexNames((0,_D,_I),(0,_D,_J),(0,_D,_K),(0,_D,_L),(0,_a,_b),(0,_D,_s))
if mibBuilder.loadTexts:nbRtVifDiffServRateLimitEntry.setStatus(_A)
_NbRtVifDiffServDirect_Type=DirectionType
_NbRtVifDiffServDirect_Object=MibTableColumn
nbRtVifDiffServDirect=_NbRtVifDiffServDirect_Object((1,3,6,1,4,1,629,1,50,12,5,4,1,1),_NbRtVifDiffServDirect_Type())
nbRtVifDiffServDirect.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:nbRtVifDiffServDirect.setStatus(_A)
_NbRtVifDiffServBuckRate_Type=Integer32
_NbRtVifDiffServBuckRate_Object=MibTableColumn
nbRtVifDiffServBuckRate=_NbRtVifDiffServBuckRate_Object((1,3,6,1,4,1,629,1,50,12,5,4,1,2),_NbRtVifDiffServBuckRate_Type())
nbRtVifDiffServBuckRate.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtVifDiffServBuckRate.setStatus(_A)
_NbRtVifDiffServBuckSize_Type=Integer32
_NbRtVifDiffServBuckSize_Object=MibTableColumn
nbRtVifDiffServBuckSize=_NbRtVifDiffServBuckSize_Object((1,3,6,1,4,1,629,1,50,12,5,4,1,3),_NbRtVifDiffServBuckSize_Type())
nbRtVifDiffServBuckSize.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtVifDiffServBuckSize.setStatus(_A)
class _NbRtVifDiffServREDmode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_NbRtVifDiffServREDmode_Type.__name__=_E
_NbRtVifDiffServREDmode_Object=MibTableColumn
nbRtVifDiffServREDmode=_NbRtVifDiffServREDmode_Object((1,3,6,1,4,1,629,1,50,12,5,4,1,4),_NbRtVifDiffServREDmode_Type())
nbRtVifDiffServREDmode.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtVifDiffServREDmode.setStatus(_A)
class _NbRtVifDiffServAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),('createOrModify',2),('delete',3),('exist',4),('absent',5)))
_NbRtVifDiffServAdminStatus_Type.__name__=_E
_NbRtVifDiffServAdminStatus_Object=MibTableColumn
nbRtVifDiffServAdminStatus=_NbRtVifDiffServAdminStatus_Object((1,3,6,1,4,1,629,1,50,12,5,4,1,10),_NbRtVifDiffServAdminStatus_Type())
nbRtVifDiffServAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtVifDiffServAdminStatus.setStatus(_A)
_NbRtDiffServVptMapTable_Object=MibTable
nbRtDiffServVptMapTable=_NbRtDiffServVptMapTable_Object((1,3,6,1,4,1,629,1,50,12,5,6))
if mibBuilder.loadTexts:nbRtDiffServVptMapTable.setStatus(_A)
_NbRtDiffServVptMapEntry_Object=MibTableRow
nbRtDiffServVptMapEntry=_NbRtDiffServVptMapEntry_Object((1,3,6,1,4,1,629,1,50,12,5,6,1))
nbRtDiffServVptMapEntry.setIndexNames((0,_D,_t))
if mibBuilder.loadTexts:nbRtDiffServVptMapEntry.setStatus(_A)
_NbRtDiffServVptMapNameId_Type=Integer32
_NbRtDiffServVptMapNameId_Object=MibTableColumn
nbRtDiffServVptMapNameId=_NbRtDiffServVptMapNameId_Object((1,3,6,1,4,1,629,1,50,12,5,6,1,1),_NbRtDiffServVptMapNameId_Type())
nbRtDiffServVptMapNameId.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtDiffServVptMapNameId.setStatus(_A)
class _NbRtDiffServVptMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_NbRtDiffServVptMapName_Type.__name__=_P
_NbRtDiffServVptMapName_Object=MibTableColumn
nbRtDiffServVptMapName=_NbRtDiffServVptMapName_Object((1,3,6,1,4,1,629,1,50,12,5,6,1,2),_NbRtDiffServVptMapName_Type())
nbRtDiffServVptMapName.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtDiffServVptMapName.setStatus(_A)
class _NbRtDiffServVptMapStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_O,2),(_T,3)))
_NbRtDiffServVptMapStatus_Type.__name__=_E
_NbRtDiffServVptMapStatus_Object=MibTableColumn
nbRtDiffServVptMapStatus=_NbRtDiffServVptMapStatus_Object((1,3,6,1,4,1,629,1,50,12,5,6,1,3),_NbRtDiffServVptMapStatus_Type())
nbRtDiffServVptMapStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtDiffServVptMapStatus.setStatus(_A)
class _NbRtDiffServVptMapAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_u,3)))
_NbRtDiffServVptMapAdminStatus_Type.__name__=_E
_NbRtDiffServVptMapAdminStatus_Object=MibTableColumn
nbRtDiffServVptMapAdminStatus=_NbRtDiffServVptMapAdminStatus_Object((1,3,6,1,4,1,629,1,50,12,5,6,1,4),_NbRtDiffServVptMapAdminStatus_Type())
nbRtDiffServVptMapAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtDiffServVptMapAdminStatus.setStatus(_A)
_NbRtDiffServVptMapPrflTable_Object=MibTable
nbRtDiffServVptMapPrflTable=_NbRtDiffServVptMapPrflTable_Object((1,3,6,1,4,1,629,1,50,12,5,8))
if mibBuilder.loadTexts:nbRtDiffServVptMapPrflTable.setStatus(_A)
_NbRtDiffServVptMapPrflEntry_Object=MibTableRow
nbRtDiffServVptMapPrflEntry=_NbRtDiffServVptMapPrflEntry_Object((1,3,6,1,4,1,629,1,50,12,5,8,1))
nbRtDiffServVptMapPrflEntry.setIndexNames((0,_D,_v),(0,_D,_w))
if mibBuilder.loadTexts:nbRtDiffServVptMapPrflEntry.setStatus(_A)
_NbRtDiffServVptMapPrflNameId_Type=Integer32
_NbRtDiffServVptMapPrflNameId_Object=MibTableColumn
nbRtDiffServVptMapPrflNameId=_NbRtDiffServVptMapPrflNameId_Object((1,3,6,1,4,1,629,1,50,12,5,8,1,1),_NbRtDiffServVptMapPrflNameId_Type())
nbRtDiffServVptMapPrflNameId.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtDiffServVptMapPrflNameId.setStatus(_A)
_NbRtDiffServVptMapPrflInValueId_Type=Integer32
_NbRtDiffServVptMapPrflInValueId_Object=MibTableColumn
nbRtDiffServVptMapPrflInValueId=_NbRtDiffServVptMapPrflInValueId_Object((1,3,6,1,4,1,629,1,50,12,5,8,1,2),_NbRtDiffServVptMapPrflInValueId_Type())
nbRtDiffServVptMapPrflInValueId.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtDiffServVptMapPrflInValueId.setStatus(_A)
_NbRtDiffServVptMapPrflInValue_Type=Integer32
_NbRtDiffServVptMapPrflInValue_Object=MibTableColumn
nbRtDiffServVptMapPrflInValue=_NbRtDiffServVptMapPrflInValue_Object((1,3,6,1,4,1,629,1,50,12,5,8,1,3),_NbRtDiffServVptMapPrflInValue_Type())
nbRtDiffServVptMapPrflInValue.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtDiffServVptMapPrflInValue.setStatus(_A)
_NbRtDiffServVptMapPrflSl_Type=Integer32
_NbRtDiffServVptMapPrflSl_Object=MibTableColumn
nbRtDiffServVptMapPrflSl=_NbRtDiffServVptMapPrflSl_Object((1,3,6,1,4,1,629,1,50,12,5,8,1,4),_NbRtDiffServVptMapPrflSl_Type())
nbRtDiffServVptMapPrflSl.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtDiffServVptMapPrflSl.setStatus(_A)
_NbRtDiffServVptMapPrflOutValue_Type=Integer32
_NbRtDiffServVptMapPrflOutValue_Object=MibTableColumn
nbRtDiffServVptMapPrflOutValue=_NbRtDiffServVptMapPrflOutValue_Object((1,3,6,1,4,1,629,1,50,12,5,8,1,5),_NbRtDiffServVptMapPrflOutValue_Type())
nbRtDiffServVptMapPrflOutValue.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtDiffServVptMapPrflOutValue.setStatus(_A)
_NbRtDiffServDscpMapTable_Object=MibTable
nbRtDiffServDscpMapTable=_NbRtDiffServDscpMapTable_Object((1,3,6,1,4,1,629,1,50,12,5,10))
if mibBuilder.loadTexts:nbRtDiffServDscpMapTable.setStatus(_A)
_NbRtDiffServDscpMapEntry_Object=MibTableRow
nbRtDiffServDscpMapEntry=_NbRtDiffServDscpMapEntry_Object((1,3,6,1,4,1,629,1,50,12,5,10,1))
nbRtDiffServDscpMapEntry.setIndexNames((0,_D,_x))
if mibBuilder.loadTexts:nbRtDiffServDscpMapEntry.setStatus(_A)
_NbRtDiffServDscpMapNameId_Type=Integer32
_NbRtDiffServDscpMapNameId_Object=MibTableColumn
nbRtDiffServDscpMapNameId=_NbRtDiffServDscpMapNameId_Object((1,3,6,1,4,1,629,1,50,12,5,10,1,1),_NbRtDiffServDscpMapNameId_Type())
nbRtDiffServDscpMapNameId.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtDiffServDscpMapNameId.setStatus(_A)
class _NbRtDiffServDscpMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_NbRtDiffServDscpMapName_Type.__name__=_P
_NbRtDiffServDscpMapName_Object=MibTableColumn
nbRtDiffServDscpMapName=_NbRtDiffServDscpMapName_Object((1,3,6,1,4,1,629,1,50,12,5,10,1,2),_NbRtDiffServDscpMapName_Type())
nbRtDiffServDscpMapName.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtDiffServDscpMapName.setStatus(_A)
class _NbRtDiffServDscpMapStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_O,2),(_T,3)))
_NbRtDiffServDscpMapStatus_Type.__name__=_E
_NbRtDiffServDscpMapStatus_Object=MibTableColumn
nbRtDiffServDscpMapStatus=_NbRtDiffServDscpMapStatus_Object((1,3,6,1,4,1,629,1,50,12,5,10,1,3),_NbRtDiffServDscpMapStatus_Type())
nbRtDiffServDscpMapStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtDiffServDscpMapStatus.setStatus(_A)
class _NbRtDiffServDscpMapAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_u,3)))
_NbRtDiffServDscpMapAdminStatus_Type.__name__=_E
_NbRtDiffServDscpMapAdminStatus_Object=MibTableColumn
nbRtDiffServDscpMapAdminStatus=_NbRtDiffServDscpMapAdminStatus_Object((1,3,6,1,4,1,629,1,50,12,5,10,1,4),_NbRtDiffServDscpMapAdminStatus_Type())
nbRtDiffServDscpMapAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtDiffServDscpMapAdminStatus.setStatus(_A)
_NbRtDiffServDscpMapPrflTable_Object=MibTable
nbRtDiffServDscpMapPrflTable=_NbRtDiffServDscpMapPrflTable_Object((1,3,6,1,4,1,629,1,50,12,5,12))
if mibBuilder.loadTexts:nbRtDiffServDscpMapPrflTable.setStatus(_A)
_NbRtDiffServDscpMapPrflEntry_Object=MibTableRow
nbRtDiffServDscpMapPrflEntry=_NbRtDiffServDscpMapPrflEntry_Object((1,3,6,1,4,1,629,1,50,12,5,12,1))
nbRtDiffServDscpMapPrflEntry.setIndexNames((0,_D,_y),(0,_D,_z))
if mibBuilder.loadTexts:nbRtDiffServDscpMapPrflEntry.setStatus(_A)
_NbRtDiffServDscpMapPrflNameId_Type=Integer32
_NbRtDiffServDscpMapPrflNameId_Object=MibTableColumn
nbRtDiffServDscpMapPrflNameId=_NbRtDiffServDscpMapPrflNameId_Object((1,3,6,1,4,1,629,1,50,12,5,12,1,1),_NbRtDiffServDscpMapPrflNameId_Type())
nbRtDiffServDscpMapPrflNameId.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtDiffServDscpMapPrflNameId.setStatus(_A)
_NbRtDiffServDscpMapPrflInValueId_Type=Integer32
_NbRtDiffServDscpMapPrflInValueId_Object=MibTableColumn
nbRtDiffServDscpMapPrflInValueId=_NbRtDiffServDscpMapPrflInValueId_Object((1,3,6,1,4,1,629,1,50,12,5,12,1,2),_NbRtDiffServDscpMapPrflInValueId_Type())
nbRtDiffServDscpMapPrflInValueId.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtDiffServDscpMapPrflInValueId.setStatus(_A)
_NbRtDiffServDscpMapPrflInValue_Type=Integer32
_NbRtDiffServDscpMapPrflInValue_Object=MibTableColumn
nbRtDiffServDscpMapPrflInValue=_NbRtDiffServDscpMapPrflInValue_Object((1,3,6,1,4,1,629,1,50,12,5,12,1,3),_NbRtDiffServDscpMapPrflInValue_Type())
nbRtDiffServDscpMapPrflInValue.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtDiffServDscpMapPrflInValue.setStatus(_A)
_NbRtDiffServDscpMapPrflSl_Type=Integer32
_NbRtDiffServDscpMapPrflSl_Object=MibTableColumn
nbRtDiffServDscpMapPrflSl=_NbRtDiffServDscpMapPrflSl_Object((1,3,6,1,4,1,629,1,50,12,5,12,1,4),_NbRtDiffServDscpMapPrflSl_Type())
nbRtDiffServDscpMapPrflSl.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtDiffServDscpMapPrflSl.setStatus(_A)
_NbRtDiffServDscpMapPrflOutValue_Type=Integer32
_NbRtDiffServDscpMapPrflOutValue_Object=MibTableColumn
nbRtDiffServDscpMapPrflOutValue=_NbRtDiffServDscpMapPrflOutValue_Object((1,3,6,1,4,1,629,1,50,12,5,12,1,5),_NbRtDiffServDscpMapPrflOutValue_Type())
nbRtDiffServDscpMapPrflOutValue.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtDiffServDscpMapPrflOutValue.setStatus(_A)
_NbRtAccounting_ObjectIdentity=ObjectIdentity
nbRtAccounting=_NbRtAccounting_ObjectIdentity((1,3,6,1,4,1,629,1,50,12,6))
_NbRtAccVifTable_Object=MibTable
nbRtAccVifTable=_NbRtAccVifTable_Object((1,3,6,1,4,1,629,1,50,12,6,10))
if mibBuilder.loadTexts:nbRtAccVifTable.setStatus(_A)
_NbRtAccVifEntry_Object=MibTableRow
nbRtAccVifEntry=_NbRtAccVifEntry_Object((1,3,6,1,4,1,629,1,50,12,6,10,1))
nbRtAccVifEntry.setIndexNames((0,_D,_I),(0,_D,_J),(0,_D,_K),(0,_D,_L),(0,_D,_U))
if mibBuilder.loadTexts:nbRtAccVifEntry.setStatus(_A)
_NbRtAccVifDirection_Type=DirectionType
_NbRtAccVifDirection_Object=MibTableColumn
nbRtAccVifDirection=_NbRtAccVifDirection_Object((1,3,6,1,4,1,629,1,50,12,6,10,1,1),_NbRtAccVifDirection_Type())
nbRtAccVifDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccVifDirection.setStatus(_A)
class _NbRtAccVifAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),(_V,4),(_W,5),(_X,6)))
_NbRtAccVifAdminStatus_Type.__name__=_E
_NbRtAccVifAdminStatus_Object=MibTableColumn
nbRtAccVifAdminStatus=_NbRtAccVifAdminStatus_Object((1,3,6,1,4,1,629,1,50,12,6,10,1,3),_NbRtAccVifAdminStatus_Type())
nbRtAccVifAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtAccVifAdminStatus.setStatus(_A)
class _NbRtAccVifOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_O,2),(_Y,3),(_Z,4)))
_NbRtAccVifOperStatus_Type.__name__=_E
_NbRtAccVifOperStatus_Object=MibTableColumn
nbRtAccVifOperStatus=_NbRtAccVifOperStatus_Object((1,3,6,1,4,1,629,1,50,12,6,10,1,4),_NbRtAccVifOperStatus_Type())
nbRtAccVifOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccVifOperStatus.setStatus(_A)
_NbRtAccVifConformingBytes_Type=AccountCouter
_NbRtAccVifConformingBytes_Object=MibTableColumn
nbRtAccVifConformingBytes=_NbRtAccVifConformingBytes_Object((1,3,6,1,4,1,629,1,50,12,6,10,1,6),_NbRtAccVifConformingBytes_Type())
nbRtAccVifConformingBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccVifConformingBytes.setStatus(_A)
_NbRtAccVifExceedingBytes_Type=AccountCouter
_NbRtAccVifExceedingBytes_Object=MibTableColumn
nbRtAccVifExceedingBytes=_NbRtAccVifExceedingBytes_Object((1,3,6,1,4,1,629,1,50,12,6,10,1,7),_NbRtAccVifExceedingBytes_Type())
nbRtAccVifExceedingBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccVifExceedingBytes.setStatus(_A)
_NbRtAccVifConformingPackets_Type=AccountCouter
_NbRtAccVifConformingPackets_Object=MibTableColumn
nbRtAccVifConformingPackets=_NbRtAccVifConformingPackets_Object((1,3,6,1,4,1,629,1,50,12,6,10,1,8),_NbRtAccVifConformingPackets_Type())
nbRtAccVifConformingPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccVifConformingPackets.setStatus(_A)
_NbRtAccVifExceedingPackets_Type=AccountCouter
_NbRtAccVifExceedingPackets_Object=MibTableColumn
nbRtAccVifExceedingPackets=_NbRtAccVifExceedingPackets_Object((1,3,6,1,4,1,629,1,50,12,6,10,1,9),_NbRtAccVifExceedingPackets_Type())
nbRtAccVifExceedingPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccVifExceedingPackets.setStatus(_A)
_NbRtAccVifHighConformingBytes_Type=Counter32
_NbRtAccVifHighConformingBytes_Object=MibTableColumn
nbRtAccVifHighConformingBytes=_NbRtAccVifHighConformingBytes_Object((1,3,6,1,4,1,629,1,50,12,6,10,1,11),_NbRtAccVifHighConformingBytes_Type())
nbRtAccVifHighConformingBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccVifHighConformingBytes.setStatus(_A)
_NbRtAccVifHighExceedingBytes_Type=Counter32
_NbRtAccVifHighExceedingBytes_Object=MibTableColumn
nbRtAccVifHighExceedingBytes=_NbRtAccVifHighExceedingBytes_Object((1,3,6,1,4,1,629,1,50,12,6,10,1,12),_NbRtAccVifHighExceedingBytes_Type())
nbRtAccVifHighExceedingBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccVifHighExceedingBytes.setStatus(_A)
_NbRtAccVifHighConformingPackets_Type=Counter32
_NbRtAccVifHighConformingPackets_Object=MibTableColumn
nbRtAccVifHighConformingPackets=_NbRtAccVifHighConformingPackets_Object((1,3,6,1,4,1,629,1,50,12,6,10,1,13),_NbRtAccVifHighConformingPackets_Type())
nbRtAccVifHighConformingPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccVifHighConformingPackets.setStatus(_A)
_NbRtAccVifHighExceedingPackets_Type=Counter32
_NbRtAccVifHighExceedingPackets_Object=MibTableColumn
nbRtAccVifHighExceedingPackets=_NbRtAccVifHighExceedingPackets_Object((1,3,6,1,4,1,629,1,50,12,6,10,1,14),_NbRtAccVifHighExceedingPackets_Type())
nbRtAccVifHighExceedingPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccVifHighExceedingPackets.setStatus(_A)
_NbRtAccVifLowConformingBytes_Type=Counter32
_NbRtAccVifLowConformingBytes_Object=MibTableColumn
nbRtAccVifLowConformingBytes=_NbRtAccVifLowConformingBytes_Object((1,3,6,1,4,1,629,1,50,12,6,10,1,15),_NbRtAccVifLowConformingBytes_Type())
nbRtAccVifLowConformingBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccVifLowConformingBytes.setStatus(_A)
_NbRtAccVifLowExceedingBytes_Type=Counter32
_NbRtAccVifLowExceedingBytes_Object=MibTableColumn
nbRtAccVifLowExceedingBytes=_NbRtAccVifLowExceedingBytes_Object((1,3,6,1,4,1,629,1,50,12,6,10,1,16),_NbRtAccVifLowExceedingBytes_Type())
nbRtAccVifLowExceedingBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccVifLowExceedingBytes.setStatus(_A)
_NbRtAccVifLowConformingPackets_Type=Counter32
_NbRtAccVifLowConformingPackets_Object=MibTableColumn
nbRtAccVifLowConformingPackets=_NbRtAccVifLowConformingPackets_Object((1,3,6,1,4,1,629,1,50,12,6,10,1,17),_NbRtAccVifLowConformingPackets_Type())
nbRtAccVifLowConformingPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccVifLowConformingPackets.setStatus(_A)
_NbRtAccVifLowExceedingPackets_Type=Counter32
_NbRtAccVifLowExceedingPackets_Object=MibTableColumn
nbRtAccVifLowExceedingPackets=_NbRtAccVifLowExceedingPackets_Object((1,3,6,1,4,1,629,1,50,12,6,10,1,18),_NbRtAccVifLowExceedingPackets_Type())
nbRtAccVifLowExceedingPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccVifLowExceedingPackets.setStatus(_A)
_NbRtAccVif64ConformingBytes_Type=AccountCounter64
_NbRtAccVif64ConformingBytes_Object=MibTableColumn
nbRtAccVif64ConformingBytes=_NbRtAccVif64ConformingBytes_Object((1,3,6,1,4,1,629,1,50,12,6,10,1,19),_NbRtAccVif64ConformingBytes_Type())
nbRtAccVif64ConformingBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccVif64ConformingBytes.setStatus(_A)
_NbRtAccVif64ExceedingBytes_Type=AccountCounter64
_NbRtAccVif64ExceedingBytes_Object=MibTableColumn
nbRtAccVif64ExceedingBytes=_NbRtAccVif64ExceedingBytes_Object((1,3,6,1,4,1,629,1,50,12,6,10,1,20),_NbRtAccVif64ExceedingBytes_Type())
nbRtAccVif64ExceedingBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccVif64ExceedingBytes.setStatus(_A)
_NbRtAccVifConformingUcastPackets_Type=AccountCouter
_NbRtAccVifConformingUcastPackets_Object=MibTableColumn
nbRtAccVifConformingUcastPackets=_NbRtAccVifConformingUcastPackets_Object((1,3,6,1,4,1,629,1,50,12,6,10,1,21),_NbRtAccVifConformingUcastPackets_Type())
nbRtAccVifConformingUcastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccVifConformingUcastPackets.setStatus(_A)
_NbRtAccVifHighConformingUcastPackets_Type=Counter32
_NbRtAccVifHighConformingUcastPackets_Object=MibTableColumn
nbRtAccVifHighConformingUcastPackets=_NbRtAccVifHighConformingUcastPackets_Object((1,3,6,1,4,1,629,1,50,12,6,10,1,22),_NbRtAccVifHighConformingUcastPackets_Type())
nbRtAccVifHighConformingUcastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccVifHighConformingUcastPackets.setStatus(_A)
_NbRtAccVifLowConformingUcastPackets_Type=Counter32
_NbRtAccVifLowConformingUcastPackets_Object=MibTableColumn
nbRtAccVifLowConformingUcastPackets=_NbRtAccVifLowConformingUcastPackets_Object((1,3,6,1,4,1,629,1,50,12,6,10,1,23),_NbRtAccVifLowConformingUcastPackets_Type())
nbRtAccVifLowConformingUcastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccVifLowConformingUcastPackets.setStatus(_A)
_NbRtAccVif64ConformingUcastPackets_Type=AccountCounter64
_NbRtAccVif64ConformingUcastPackets_Object=MibTableColumn
nbRtAccVif64ConformingUcastPackets=_NbRtAccVif64ConformingUcastPackets_Object((1,3,6,1,4,1,629,1,50,12,6,10,1,24),_NbRtAccVif64ConformingUcastPackets_Type())
nbRtAccVif64ConformingUcastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccVif64ConformingUcastPackets.setStatus(_A)
_NbRtAccVifConformingMcastPackets_Type=AccountCouter
_NbRtAccVifConformingMcastPackets_Object=MibTableColumn
nbRtAccVifConformingMcastPackets=_NbRtAccVifConformingMcastPackets_Object((1,3,6,1,4,1,629,1,50,12,6,10,1,25),_NbRtAccVifConformingMcastPackets_Type())
nbRtAccVifConformingMcastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccVifConformingMcastPackets.setStatus(_A)
_NbRtAccVifHighConformingMcastPackets_Type=Counter32
_NbRtAccVifHighConformingMcastPackets_Object=MibTableColumn
nbRtAccVifHighConformingMcastPackets=_NbRtAccVifHighConformingMcastPackets_Object((1,3,6,1,4,1,629,1,50,12,6,10,1,26),_NbRtAccVifHighConformingMcastPackets_Type())
nbRtAccVifHighConformingMcastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccVifHighConformingMcastPackets.setStatus(_A)
_NbRtAccVifLowConformingMcastPackets_Type=Counter32
_NbRtAccVifLowConformingMcastPackets_Object=MibTableColumn
nbRtAccVifLowConformingMcastPackets=_NbRtAccVifLowConformingMcastPackets_Object((1,3,6,1,4,1,629,1,50,12,6,10,1,27),_NbRtAccVifLowConformingMcastPackets_Type())
nbRtAccVifLowConformingMcastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccVifLowConformingMcastPackets.setStatus(_A)
_NbRtAccVif64ConformingMcastPackets_Type=AccountCounter64
_NbRtAccVif64ConformingMcastPackets_Object=MibTableColumn
nbRtAccVif64ConformingMcastPackets=_NbRtAccVif64ConformingMcastPackets_Object((1,3,6,1,4,1,629,1,50,12,6,10,1,28),_NbRtAccVif64ConformingMcastPackets_Type())
nbRtAccVif64ConformingMcastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccVif64ConformingMcastPackets.setStatus(_A)
_NbRtAccVifConformingBcastPackets_Type=AccountCouter
_NbRtAccVifConformingBcastPackets_Object=MibTableColumn
nbRtAccVifConformingBcastPackets=_NbRtAccVifConformingBcastPackets_Object((1,3,6,1,4,1,629,1,50,12,6,10,1,29),_NbRtAccVifConformingBcastPackets_Type())
nbRtAccVifConformingBcastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccVifConformingBcastPackets.setStatus(_A)
_NbRtAccVifHighConformingBcastPackets_Type=Counter32
_NbRtAccVifHighConformingBcastPackets_Object=MibTableColumn
nbRtAccVifHighConformingBcastPackets=_NbRtAccVifHighConformingBcastPackets_Object((1,3,6,1,4,1,629,1,50,12,6,10,1,30),_NbRtAccVifHighConformingBcastPackets_Type())
nbRtAccVifHighConformingBcastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccVifHighConformingBcastPackets.setStatus(_A)
_NbRtAccVifLowConformingBcastPackets_Type=Counter32
_NbRtAccVifLowConformingBcastPackets_Object=MibTableColumn
nbRtAccVifLowConformingBcastPackets=_NbRtAccVifLowConformingBcastPackets_Object((1,3,6,1,4,1,629,1,50,12,6,10,1,31),_NbRtAccVifLowConformingBcastPackets_Type())
nbRtAccVifLowConformingBcastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccVifLowConformingBcastPackets.setStatus(_A)
_NbRtAccVif64ConformingBcastPackets_Type=AccountCounter64
_NbRtAccVif64ConformingBcastPackets_Object=MibTableColumn
nbRtAccVif64ConformingBcastPackets=_NbRtAccVif64ConformingBcastPackets_Object((1,3,6,1,4,1,629,1,50,12,6,10,1,32),_NbRtAccVif64ConformingBcastPackets_Type())
nbRtAccVif64ConformingBcastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccVif64ConformingBcastPackets.setStatus(_A)
_NbRtAccVifPortTable_Object=MibTable
nbRtAccVifPortTable=_NbRtAccVifPortTable_Object((1,3,6,1,4,1,629,1,50,12,6,12))
if mibBuilder.loadTexts:nbRtAccVifPortTable.setStatus(_A)
_NbRtAccVifPortEntry_Object=MibTableRow
nbRtAccVifPortEntry=_NbRtAccVifPortEntry_Object((1,3,6,1,4,1,629,1,50,12,6,12,1))
nbRtAccVifPortEntry.setIndexNames((0,_D,_I),(0,_D,_J),(0,_D,_K),(0,_D,_L),(0,_D,_A0),(0,_D,_U))
if mibBuilder.loadTexts:nbRtAccVifPortEntry.setStatus(_A)
_NbRtVifPortId_Type=Integer32
_NbRtVifPortId_Object=MibTableColumn
nbRtVifPortId=_NbRtVifPortId_Object((1,3,6,1,4,1,629,1,50,12,6,12,1,1),_NbRtVifPortId_Type())
nbRtVifPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtVifPortId.setStatus(_A)
class _NbRtAccPortAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),(_V,4),(_W,5),(_X,6)))
_NbRtAccPortAdminStatus_Type.__name__=_E
_NbRtAccPortAdminStatus_Object=MibTableColumn
nbRtAccPortAdminStatus=_NbRtAccPortAdminStatus_Object((1,3,6,1,4,1,629,1,50,12,6,12,1,2),_NbRtAccPortAdminStatus_Type())
nbRtAccPortAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtAccPortAdminStatus.setStatus(_A)
class _NbRtAccPortOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_O,2),(_Y,3),(_Z,4)))
_NbRtAccPortOperStatus_Type.__name__=_E
_NbRtAccPortOperStatus_Object=MibTableColumn
nbRtAccPortOperStatus=_NbRtAccPortOperStatus_Object((1,3,6,1,4,1,629,1,50,12,6,12,1,3),_NbRtAccPortOperStatus_Type())
nbRtAccPortOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccPortOperStatus.setStatus(_A)
_NbRtAccPortConformingBytes_Type=AccountCouter
_NbRtAccPortConformingBytes_Object=MibTableColumn
nbRtAccPortConformingBytes=_NbRtAccPortConformingBytes_Object((1,3,6,1,4,1,629,1,50,12,6,12,1,6),_NbRtAccPortConformingBytes_Type())
nbRtAccPortConformingBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccPortConformingBytes.setStatus(_A)
_NbRtAccPortExceedingBytes_Type=AccountCouter
_NbRtAccPortExceedingBytes_Object=MibTableColumn
nbRtAccPortExceedingBytes=_NbRtAccPortExceedingBytes_Object((1,3,6,1,4,1,629,1,50,12,6,12,1,7),_NbRtAccPortExceedingBytes_Type())
nbRtAccPortExceedingBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccPortExceedingBytes.setStatus(_A)
_NbRtAccPortConformingPackets_Type=AccountCouter
_NbRtAccPortConformingPackets_Object=MibTableColumn
nbRtAccPortConformingPackets=_NbRtAccPortConformingPackets_Object((1,3,6,1,4,1,629,1,50,12,6,12,1,8),_NbRtAccPortConformingPackets_Type())
nbRtAccPortConformingPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccPortConformingPackets.setStatus(_A)
_NbRtAccPortExceedingPackets_Type=AccountCouter
_NbRtAccPortExceedingPackets_Object=MibTableColumn
nbRtAccPortExceedingPackets=_NbRtAccPortExceedingPackets_Object((1,3,6,1,4,1,629,1,50,12,6,12,1,9),_NbRtAccPortExceedingPackets_Type())
nbRtAccPortExceedingPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccPortExceedingPackets.setStatus(_A)
_NbRtAccPortHighConformingBytes_Type=Counter32
_NbRtAccPortHighConformingBytes_Object=MibTableColumn
nbRtAccPortHighConformingBytes=_NbRtAccPortHighConformingBytes_Object((1,3,6,1,4,1,629,1,50,12,6,12,1,11),_NbRtAccPortHighConformingBytes_Type())
nbRtAccPortHighConformingBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccPortHighConformingBytes.setStatus(_A)
_NbRtAccPortHighExceedingBytes_Type=Counter32
_NbRtAccPortHighExceedingBytes_Object=MibTableColumn
nbRtAccPortHighExceedingBytes=_NbRtAccPortHighExceedingBytes_Object((1,3,6,1,4,1,629,1,50,12,6,12,1,12),_NbRtAccPortHighExceedingBytes_Type())
nbRtAccPortHighExceedingBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccPortHighExceedingBytes.setStatus(_A)
_NbRtAccPortHighConformingPackets_Type=Counter32
_NbRtAccPortHighConformingPackets_Object=MibTableColumn
nbRtAccPortHighConformingPackets=_NbRtAccPortHighConformingPackets_Object((1,3,6,1,4,1,629,1,50,12,6,12,1,13),_NbRtAccPortHighConformingPackets_Type())
nbRtAccPortHighConformingPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccPortHighConformingPackets.setStatus(_A)
_NbRtAccPortHighExceedingPackets_Type=Counter32
_NbRtAccPortHighExceedingPackets_Object=MibTableColumn
nbRtAccPortHighExceedingPackets=_NbRtAccPortHighExceedingPackets_Object((1,3,6,1,4,1,629,1,50,12,6,12,1,14),_NbRtAccPortHighExceedingPackets_Type())
nbRtAccPortHighExceedingPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccPortHighExceedingPackets.setStatus(_A)
_NbRtAccPortLowConformingBytes_Type=Counter32
_NbRtAccPortLowConformingBytes_Object=MibTableColumn
nbRtAccPortLowConformingBytes=_NbRtAccPortLowConformingBytes_Object((1,3,6,1,4,1,629,1,50,12,6,12,1,15),_NbRtAccPortLowConformingBytes_Type())
nbRtAccPortLowConformingBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccPortLowConformingBytes.setStatus(_A)
_NbRtAccPortLowExceedingBytes_Type=Counter32
_NbRtAccPortLowExceedingBytes_Object=MibTableColumn
nbRtAccPortLowExceedingBytes=_NbRtAccPortLowExceedingBytes_Object((1,3,6,1,4,1,629,1,50,12,6,12,1,16),_NbRtAccPortLowExceedingBytes_Type())
nbRtAccPortLowExceedingBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccPortLowExceedingBytes.setStatus(_A)
_NbRtAccPortLowConformingPackets_Type=Counter32
_NbRtAccPortLowConformingPackets_Object=MibTableColumn
nbRtAccPortLowConformingPackets=_NbRtAccPortLowConformingPackets_Object((1,3,6,1,4,1,629,1,50,12,6,12,1,17),_NbRtAccPortLowConformingPackets_Type())
nbRtAccPortLowConformingPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccPortLowConformingPackets.setStatus(_A)
_NbRtAccPortLowExceedingPackets_Type=Counter32
_NbRtAccPortLowExceedingPackets_Object=MibTableColumn
nbRtAccPortLowExceedingPackets=_NbRtAccPortLowExceedingPackets_Object((1,3,6,1,4,1,629,1,50,12,6,12,1,18),_NbRtAccPortLowExceedingPackets_Type())
nbRtAccPortLowExceedingPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccPortLowExceedingPackets.setStatus(_A)
_NbRtAccPortVif64ConformingBytes_Type=AccountCounter64
_NbRtAccPortVif64ConformingBytes_Object=MibTableColumn
nbRtAccPortVif64ConformingBytes=_NbRtAccPortVif64ConformingBytes_Object((1,3,6,1,4,1,629,1,50,12,6,12,1,19),_NbRtAccPortVif64ConformingBytes_Type())
nbRtAccPortVif64ConformingBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccPortVif64ConformingBytes.setStatus(_A)
_NbRtAccPortVif64ExceedingBytes_Type=AccountCounter64
_NbRtAccPortVif64ExceedingBytes_Object=MibTableColumn
nbRtAccPortVif64ExceedingBytes=_NbRtAccPortVif64ExceedingBytes_Object((1,3,6,1,4,1,629,1,50,12,6,12,1,20),_NbRtAccPortVif64ExceedingBytes_Type())
nbRtAccPortVif64ExceedingBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccPortVif64ExceedingBytes.setStatus(_A)
_NbRtAccPortConformingUcastPackets_Type=AccountCouter
_NbRtAccPortConformingUcastPackets_Object=MibTableColumn
nbRtAccPortConformingUcastPackets=_NbRtAccPortConformingUcastPackets_Object((1,3,6,1,4,1,629,1,50,12,6,12,1,21),_NbRtAccPortConformingUcastPackets_Type())
nbRtAccPortConformingUcastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccPortConformingUcastPackets.setStatus(_A)
_NbRtAccPortHighConformingUcastPackets_Type=Counter32
_NbRtAccPortHighConformingUcastPackets_Object=MibTableColumn
nbRtAccPortHighConformingUcastPackets=_NbRtAccPortHighConformingUcastPackets_Object((1,3,6,1,4,1,629,1,50,12,6,12,1,22),_NbRtAccPortHighConformingUcastPackets_Type())
nbRtAccPortHighConformingUcastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccPortHighConformingUcastPackets.setStatus(_A)
_NbRtAccPortLowConformingUcastPackets_Type=Counter32
_NbRtAccPortLowConformingUcastPackets_Object=MibTableColumn
nbRtAccPortLowConformingUcastPackets=_NbRtAccPortLowConformingUcastPackets_Object((1,3,6,1,4,1,629,1,50,12,6,12,1,23),_NbRtAccPortLowConformingUcastPackets_Type())
nbRtAccPortLowConformingUcastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccPortLowConformingUcastPackets.setStatus(_A)
_NbRtAccPort64ConformingUcastPackets_Type=AccountCounter64
_NbRtAccPort64ConformingUcastPackets_Object=MibTableColumn
nbRtAccPort64ConformingUcastPackets=_NbRtAccPort64ConformingUcastPackets_Object((1,3,6,1,4,1,629,1,50,12,6,12,1,24),_NbRtAccPort64ConformingUcastPackets_Type())
nbRtAccPort64ConformingUcastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccPort64ConformingUcastPackets.setStatus(_A)
_NbRtAccPortConformingMcastPackets_Type=AccountCouter
_NbRtAccPortConformingMcastPackets_Object=MibTableColumn
nbRtAccPortConformingMcastPackets=_NbRtAccPortConformingMcastPackets_Object((1,3,6,1,4,1,629,1,50,12,6,12,1,25),_NbRtAccPortConformingMcastPackets_Type())
nbRtAccPortConformingMcastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccPortConformingMcastPackets.setStatus(_A)
_NbRtAccPortHighConformingMcastPackets_Type=Counter32
_NbRtAccPortHighConformingMcastPackets_Object=MibTableColumn
nbRtAccPortHighConformingMcastPackets=_NbRtAccPortHighConformingMcastPackets_Object((1,3,6,1,4,1,629,1,50,12,6,12,1,26),_NbRtAccPortHighConformingMcastPackets_Type())
nbRtAccPortHighConformingMcastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccPortHighConformingMcastPackets.setStatus(_A)
_NbRtAccPortLowConformingMcastPackets_Type=Counter32
_NbRtAccPortLowConformingMcastPackets_Object=MibTableColumn
nbRtAccPortLowConformingMcastPackets=_NbRtAccPortLowConformingMcastPackets_Object((1,3,6,1,4,1,629,1,50,12,6,12,1,27),_NbRtAccPortLowConformingMcastPackets_Type())
nbRtAccPortLowConformingMcastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccPortLowConformingMcastPackets.setStatus(_A)
_NbRtAccPort64ConformingMcastPackets_Type=AccountCounter64
_NbRtAccPort64ConformingMcastPackets_Object=MibTableColumn
nbRtAccPort64ConformingMcastPackets=_NbRtAccPort64ConformingMcastPackets_Object((1,3,6,1,4,1,629,1,50,12,6,12,1,28),_NbRtAccPort64ConformingMcastPackets_Type())
nbRtAccPort64ConformingMcastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccPort64ConformingMcastPackets.setStatus(_A)
_NbRtAccPortConformingBcastPackets_Type=AccountCouter
_NbRtAccPortConformingBcastPackets_Object=MibTableColumn
nbRtAccPortConformingBcastPackets=_NbRtAccPortConformingBcastPackets_Object((1,3,6,1,4,1,629,1,50,12,6,12,1,29),_NbRtAccPortConformingBcastPackets_Type())
nbRtAccPortConformingBcastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccPortConformingBcastPackets.setStatus(_A)
_NbRtAccPortHighConformingBcastPackets_Type=Counter32
_NbRtAccPortHighConformingBcastPackets_Object=MibTableColumn
nbRtAccPortHighConformingBcastPackets=_NbRtAccPortHighConformingBcastPackets_Object((1,3,6,1,4,1,629,1,50,12,6,12,1,30),_NbRtAccPortHighConformingBcastPackets_Type())
nbRtAccPortHighConformingBcastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccPortHighConformingBcastPackets.setStatus(_A)
_NbRtAccPortLowConformingBcastPackets_Type=Counter32
_NbRtAccPortLowConformingBcastPackets_Object=MibTableColumn
nbRtAccPortLowConformingBcastPackets=_NbRtAccPortLowConformingBcastPackets_Object((1,3,6,1,4,1,629,1,50,12,6,12,1,31),_NbRtAccPortLowConformingBcastPackets_Type())
nbRtAccPortLowConformingBcastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccPortLowConformingBcastPackets.setStatus(_A)
_NbRtAccPort64ConformingBcastPackets_Type=AccountCounter64
_NbRtAccPort64ConformingBcastPackets_Object=MibTableColumn
nbRtAccPort64ConformingBcastPackets=_NbRtAccPort64ConformingBcastPackets_Object((1,3,6,1,4,1,629,1,50,12,6,12,1,32),_NbRtAccPort64ConformingBcastPackets_Type())
nbRtAccPort64ConformingBcastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtAccPort64ConformingBcastPackets.setStatus(_A)
_NbRtAccessLists_ObjectIdentity=ObjectIdentity
nbRtAccessLists=_NbRtAccessLists_ObjectIdentity((1,3,6,1,4,1,629,1,50,12,7))
_NbAclVifTable_Object=MibTable
nbAclVifTable=_NbAclVifTable_Object((1,3,6,1,4,1,629,1,50,12,7,5))
if mibBuilder.loadTexts:nbAclVifTable.setStatus(_A)
_NbAclVifEntry_Object=MibTableRow
nbAclVifEntry=_NbAclVifEntry_Object((1,3,6,1,4,1,629,1,50,12,7,5,1))
nbAclVifEntry.setIndexNames((0,_D,_I),(0,_D,_J),(0,_D,_K),(0,_D,_L),(0,_D,_A1),(0,_D,_A2))
if mibBuilder.loadTexts:nbAclVifEntry.setStatus(_A)
_NbAclVifDirection_Type=DirectionType
_NbAclVifDirection_Object=MibTableColumn
nbAclVifDirection=_NbAclVifDirection_Object((1,3,6,1,4,1,629,1,50,12,7,5,1,5),_NbAclVifDirection_Type())
nbAclVifDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:nbAclVifDirection.setStatus(_A)
_NbAclVifId_Type=Integer32
_NbAclVifId_Object=MibTableColumn
nbAclVifId=_NbAclVifId_Object((1,3,6,1,4,1,629,1,50,12,7,5,1,6),_NbAclVifId_Type())
nbAclVifId.setMaxAccess(_B)
if mibBuilder.loadTexts:nbAclVifId.setStatus(_A)
_NbAclVifAccessListName_Type=DisplayString
_NbAclVifAccessListName_Object=MibTableColumn
nbAclVifAccessListName=_NbAclVifAccessListName_Object((1,3,6,1,4,1,629,1,50,12,7,5,1,7),_NbAclVifAccessListName_Type())
nbAclVifAccessListName.setMaxAccess(_C)
if mibBuilder.loadTexts:nbAclVifAccessListName.setStatus(_A)
class _NbAclVifBindingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('bind',1),('unbind',2)))
_NbAclVifBindingStatus_Type.__name__=_E
_NbAclVifBindingStatus_Object=MibTableColumn
nbAclVifBindingStatus=_NbAclVifBindingStatus_Object((1,3,6,1,4,1,629,1,50,12,7,5,1,8),_NbAclVifBindingStatus_Type())
nbAclVifBindingStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nbAclVifBindingStatus.setStatus(_A)
_NbRtPortTagGroup_ObjectIdentity=ObjectIdentity
nbRtPortTagGroup=_NbRtPortTagGroup_ObjectIdentity((1,3,6,1,4,1,629,1,50,12,8))
_NbRtPortTagTable_Object=MibTable
nbRtPortTagTable=_NbRtPortTagTable_Object((1,3,6,1,4,1,629,1,50,12,8,5))
if mibBuilder.loadTexts:nbRtPortTagTable.setStatus(_A)
_NbRtPortTagEntry_Object=MibTableRow
nbRtPortTagEntry=_NbRtPortTagEntry_Object((1,3,6,1,4,1,629,1,50,12,8,5,1))
nbRtPortTagEntry.setIndexNames((0,_D,_A3))
if mibBuilder.loadTexts:nbRtPortTagEntry.setStatus(_A)
_NbRtPortTagId_Type=Integer32
_NbRtPortTagId_Object=MibTableColumn
nbRtPortTagId=_NbRtPortTagId_Object((1,3,6,1,4,1,629,1,50,12,8,5,1,1),_NbRtPortTagId_Type())
nbRtPortTagId.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtPortTagId.setStatus(_A)
class _NbRtPortTagAwareMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_F,1),('tagged',2),('untagged',3),('hybrid',4),('qInQtagged',5),('qInQuntagged',6),('qInQuntagged2',7)))
_NbRtPortTagAwareMode_Type.__name__=_E
_NbRtPortTagAwareMode_Object=MibTableColumn
nbRtPortTagAwareMode=_NbRtPortTagAwareMode_Object((1,3,6,1,4,1,629,1,50,12,8,5,1,2),_NbRtPortTagAwareMode_Type())
nbRtPortTagAwareMode.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtPortTagAwareMode.setStatus(_A)
class _NbRtPortTagEtherType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NbRtPortTagEtherType_Type.__name__=_E
_NbRtPortTagEtherType_Object=MibTableColumn
nbRtPortTagEtherType=_NbRtPortTagEtherType_Object((1,3,6,1,4,1,629,1,50,12,8,5,1,3),_NbRtPortTagEtherType_Type())
nbRtPortTagEtherType.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtPortTagEtherType.setStatus(_A)
class _NbRtPortTagIpDefTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4080))
_NbRtPortTagIpDefTag_Type.__name__=_E
_NbRtPortTagIpDefTag_Object=MibTableColumn
nbRtPortTagIpDefTag=_NbRtPortTagIpDefTag_Object((1,3,6,1,4,1,629,1,50,12,8,5,1,4),_NbRtPortTagIpDefTag_Type())
nbRtPortTagIpDefTag.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtPortTagIpDefTag.setStatus(_A)
class _NbRtPortTagPortDefTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4080))
_NbRtPortTagPortDefTag_Type.__name__=_E
_NbRtPortTagPortDefTag_Object=MibTableColumn
nbRtPortTagPortDefTag=_NbRtPortTagPortDefTag_Object((1,3,6,1,4,1,629,1,50,12,8,5,1,5),_NbRtPortTagPortDefTag_Type())
nbRtPortTagPortDefTag.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtPortTagPortDefTag.setStatus(_A)
class _NbRtPortTagVmanDefTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4080))
_NbRtPortTagVmanDefTag_Type.__name__=_E
_NbRtPortTagVmanDefTag_Object=MibTableColumn
nbRtPortTagVmanDefTag=_NbRtPortTagVmanDefTag_Object((1,3,6,1,4,1,629,1,50,12,8,5,1,6),_NbRtPortTagVmanDefTag_Type())
nbRtPortTagVmanDefTag.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtPortTagVmanDefTag.setStatus(_A)
_NbRtPortTagNumberOfTags_Type=Integer32
_NbRtPortTagNumberOfTags_Object=MibTableColumn
nbRtPortTagNumberOfTags=_NbRtPortTagNumberOfTags_Object((1,3,6,1,4,1,629,1,50,12,8,5,1,7),_NbRtPortTagNumberOfTags_Type())
nbRtPortTagNumberOfTags.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtPortTagNumberOfTags.setStatus(_A)
class _NbRtPortTagMplsForceMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('mplsForceTag',2),('noMplsForceTag',3)))
_NbRtPortTagMplsForceMode_Type.__name__=_E
_NbRtPortTagMplsForceMode_Object=MibTableColumn
nbRtPortTagMplsForceMode=_NbRtPortTagMplsForceMode_Object((1,3,6,1,4,1,629,1,50,12,8,5,1,8),_NbRtPortTagMplsForceMode_Type())
nbRtPortTagMplsForceMode.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtPortTagMplsForceMode.setStatus(_A)
_NbRtActionLists_ObjectIdentity=ObjectIdentity
nbRtActionLists=_NbRtActionLists_ObjectIdentity((1,3,6,1,4,1,629,1,50,12,9))
class _NbRtActionListSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_d,1),(_e,2)))
_NbRtActionListSupport_Type.__name__=_E
_NbRtActionListSupport_Object=MibScalar
nbRtActionListSupport=_NbRtActionListSupport_Object((1,3,6,1,4,1,629,1,50,12,9,1),_NbRtActionListSupport_Type())
nbRtActionListSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtActionListSupport.setStatus(_A)
_NbRtActionListTable_Object=MibTable
nbRtActionListTable=_NbRtActionListTable_Object((1,3,6,1,4,1,629,1,50,12,9,2))
if mibBuilder.loadTexts:nbRtActionListTable.setStatus(_A)
_NbRtActionListEntry_Object=MibTableRow
nbRtActionListEntry=_NbRtActionListEntry_Object((1,3,6,1,4,1,629,1,50,12,9,2,1))
nbRtActionListEntry.setIndexNames((0,_D,_A4))
if mibBuilder.loadTexts:nbRtActionListEntry.setStatus(_A)
_NbRtActionListName_Type=ActionListName
_NbRtActionListName_Object=MibTableColumn
nbRtActionListName=_NbRtActionListName_Object((1,3,6,1,4,1,629,1,50,12,9,2,1,1),_NbRtActionListName_Type())
nbRtActionListName.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtActionListName.setStatus(_A)
class _NbRtActionListAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_NbRtActionListAdminStatus_Type.__name__=_E
_NbRtActionListAdminStatus_Object=MibTableColumn
nbRtActionListAdminStatus=_NbRtActionListAdminStatus_Object((1,3,6,1,4,1,629,1,50,12,9,2,1,2),_NbRtActionListAdminStatus_Type())
nbRtActionListAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtActionListAdminStatus.setStatus(_A)
class _NbRtActionListOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_T,2)))
_NbRtActionListOperStatus_Type.__name__=_E
_NbRtActionListOperStatus_Object=MibTableColumn
nbRtActionListOperStatus=_NbRtActionListOperStatus_Object((1,3,6,1,4,1,629,1,50,12,9,2,1,3),_NbRtActionListOperStatus_Type())
nbRtActionListOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtActionListOperStatus.setStatus(_A)
class _NbRtActionListPoliceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_NbRtActionListPoliceType_Type.__name__=_E
_NbRtActionListPoliceType_Object=MibTableColumn
nbRtActionListPoliceType=_NbRtActionListPoliceType_Object((1,3,6,1,4,1,629,1,50,12,9,2,1,4),_NbRtActionListPoliceType_Type())
nbRtActionListPoliceType.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtActionListPoliceType.setStatus(_A)
class _NbRtActionListMplsType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_NbRtActionListMplsType_Type.__name__=_E
_NbRtActionListMplsType_Object=MibTableColumn
nbRtActionListMplsType=_NbRtActionListMplsType_Object((1,3,6,1,4,1,629,1,50,12,9,2,1,5),_NbRtActionListMplsType_Type())
nbRtActionListMplsType.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtActionListMplsType.setStatus(_A)
_NbRtPoliceAction_ObjectIdentity=ObjectIdentity
nbRtPoliceAction=_NbRtPoliceAction_ObjectIdentity((1,3,6,1,4,1,629,1,50,12,9,3))
_NbRtPoliceActionTable_Object=MibTable
nbRtPoliceActionTable=_NbRtPoliceActionTable_Object((1,3,6,1,4,1,629,1,50,12,9,3,1))
if mibBuilder.loadTexts:nbRtPoliceActionTable.setStatus(_A)
_NbRtPoliceActionEntry_Object=MibTableRow
nbRtPoliceActionEntry=_NbRtPoliceActionEntry_Object((1,3,6,1,4,1,629,1,50,12,9,3,1,1))
nbRtPoliceActionEntry.setIndexNames((0,_D,_A5))
if mibBuilder.loadTexts:nbRtPoliceActionEntry.setStatus(_A)
_NbRtPoliceActionName_Type=ActionListName
_NbRtPoliceActionName_Object=MibTableColumn
nbRtPoliceActionName=_NbRtPoliceActionName_Object((1,3,6,1,4,1,629,1,50,12,9,3,1,1,1),_NbRtPoliceActionName_Type())
nbRtPoliceActionName.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtPoliceActionName.setStatus(_A)
class _NbRtPoliceActionOperMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_A6,2),(_A7,3),(_A8,4),('coSaware',5)))
_NbRtPoliceActionOperMode_Type.__name__=_E
_NbRtPoliceActionOperMode_Object=MibTableColumn
nbRtPoliceActionOperMode=_NbRtPoliceActionOperMode_Object((1,3,6,1,4,1,629,1,50,12,9,3,1,1,2),_NbRtPoliceActionOperMode_Type())
nbRtPoliceActionOperMode.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtPoliceActionOperMode.setStatus(_A)
class _NbRtPoliceActionSharingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_NbRtPoliceActionSharingMode_Type.__name__=_E
_NbRtPoliceActionSharingMode_Object=MibTableColumn
nbRtPoliceActionSharingMode=_NbRtPoliceActionSharingMode_Object((1,3,6,1,4,1,629,1,50,12,9,3,1,1,3),_NbRtPoliceActionSharingMode_Type())
nbRtPoliceActionSharingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtPoliceActionSharingMode.setStatus(_A)
class _NbRtPoliceActionAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_NbRtPoliceActionAdminStatus_Type.__name__=_E
_NbRtPoliceActionAdminStatus_Object=MibTableColumn
nbRtPoliceActionAdminStatus=_NbRtPoliceActionAdminStatus_Object((1,3,6,1,4,1,629,1,50,12,9,3,1,1,4),_NbRtPoliceActionAdminStatus_Type())
nbRtPoliceActionAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtPoliceActionAdminStatus.setStatus(_A)
class _NbRtPoliceActionExceedCntAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),(_V,4),(_W,5),(_X,6)))
_NbRtPoliceActionExceedCntAdminStatus_Type.__name__=_E
_NbRtPoliceActionExceedCntAdminStatus_Object=MibTableColumn
nbRtPoliceActionExceedCntAdminStatus=_NbRtPoliceActionExceedCntAdminStatus_Object((1,3,6,1,4,1,629,1,50,12,9,3,1,1,5),_NbRtPoliceActionExceedCntAdminStatus_Type())
nbRtPoliceActionExceedCntAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtPoliceActionExceedCntAdminStatus.setStatus(_A)
class _NbRtPoliceActionExceedCntOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_O,2),(_Y,3),(_Z,4)))
_NbRtPoliceActionExceedCntOperStatus_Type.__name__=_E
_NbRtPoliceActionExceedCntOperStatus_Object=MibTableColumn
nbRtPoliceActionExceedCntOperStatus=_NbRtPoliceActionExceedCntOperStatus_Object((1,3,6,1,4,1,629,1,50,12,9,3,1,1,6),_NbRtPoliceActionExceedCntOperStatus_Type())
nbRtPoliceActionExceedCntOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtPoliceActionExceedCntOperStatus.setStatus(_A)
_NbRtPoliceActionTotalExceedBytesCnt_Type=AccountCounter64
_NbRtPoliceActionTotalExceedBytesCnt_Object=MibTableColumn
nbRtPoliceActionTotalExceedBytesCnt=_NbRtPoliceActionTotalExceedBytesCnt_Object((1,3,6,1,4,1,629,1,50,12,9,3,1,1,7),_NbRtPoliceActionTotalExceedBytesCnt_Type())
nbRtPoliceActionTotalExceedBytesCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtPoliceActionTotalExceedBytesCnt.setStatus(_A)
_NbRtPoliceActionTotalExceedFramesCnt_Type=AccountCounter64
_NbRtPoliceActionTotalExceedFramesCnt_Object=MibTableColumn
nbRtPoliceActionTotalExceedFramesCnt=_NbRtPoliceActionTotalExceedFramesCnt_Object((1,3,6,1,4,1,629,1,50,12,9,3,1,1,8),_NbRtPoliceActionTotalExceedFramesCnt_Type())
nbRtPoliceActionTotalExceedFramesCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtPoliceActionTotalExceedFramesCnt.setStatus(_A)
_NbRtPoliceActionTotalHighExceedBytes32_Type=Counter32
_NbRtPoliceActionTotalHighExceedBytes32_Object=MibTableColumn
nbRtPoliceActionTotalHighExceedBytes32=_NbRtPoliceActionTotalHighExceedBytes32_Object((1,3,6,1,4,1,629,1,50,12,9,3,1,1,9),_NbRtPoliceActionTotalHighExceedBytes32_Type())
nbRtPoliceActionTotalHighExceedBytes32.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtPoliceActionTotalHighExceedBytes32.setStatus(_A)
_NbRtPoliceActionTotalLowExceedBytes32_Type=Counter32
_NbRtPoliceActionTotalLowExceedBytes32_Object=MibTableColumn
nbRtPoliceActionTotalLowExceedBytes32=_NbRtPoliceActionTotalLowExceedBytes32_Object((1,3,6,1,4,1,629,1,50,12,9,3,1,1,10),_NbRtPoliceActionTotalLowExceedBytes32_Type())
nbRtPoliceActionTotalLowExceedBytes32.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtPoliceActionTotalLowExceedBytes32.setStatus(_A)
_NbRtPoliceActionTotalHighExceedFrames32_Type=Counter32
_NbRtPoliceActionTotalHighExceedFrames32_Object=MibTableColumn
nbRtPoliceActionTotalHighExceedFrames32=_NbRtPoliceActionTotalHighExceedFrames32_Object((1,3,6,1,4,1,629,1,50,12,9,3,1,1,11),_NbRtPoliceActionTotalHighExceedFrames32_Type())
nbRtPoliceActionTotalHighExceedFrames32.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtPoliceActionTotalHighExceedFrames32.setStatus(_A)
_NbRtPoliceActionTotalLowExceedFrames32_Type=Counter32
_NbRtPoliceActionTotalLowExceedFrames32_Object=MibTableColumn
nbRtPoliceActionTotalLowExceedFrames32=_NbRtPoliceActionTotalLowExceedFrames32_Object((1,3,6,1,4,1,629,1,50,12,9,3,1,1,12),_NbRtPoliceActionTotalLowExceedFrames32_Type())
nbRtPoliceActionTotalLowExceedFrames32.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtPoliceActionTotalLowExceedFrames32.setStatus(_A)
_NbRtPoliceRateLimitTable_Object=MibTable
nbRtPoliceRateLimitTable=_NbRtPoliceRateLimitTable_Object((1,3,6,1,4,1,629,1,50,12,9,3,2))
if mibBuilder.loadTexts:nbRtPoliceRateLimitTable.setStatus(_A)
_NbRtPoliceRateLimitEntry_Object=MibTableRow
nbRtPoliceRateLimitEntry=_NbRtPoliceRateLimitEntry_Object((1,3,6,1,4,1,629,1,50,12,9,3,2,1))
nbRtPoliceRateLimitEntry.setIndexNames((0,_D,_A9),(0,_D,_AA))
if mibBuilder.loadTexts:nbRtPoliceRateLimitEntry.setStatus(_A)
_NbRtPoliceRateLimitName_Type=ActionListName
_NbRtPoliceRateLimitName_Object=MibTableColumn
nbRtPoliceRateLimitName=_NbRtPoliceRateLimitName_Object((1,3,6,1,4,1,629,1,50,12,9,3,2,1,1),_NbRtPoliceRateLimitName_Type())
nbRtPoliceRateLimitName.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtPoliceRateLimitName.setStatus(_A)
_NbRtPoliceRateLimitCoSlevel_Type=Integer32
_NbRtPoliceRateLimitCoSlevel_Object=MibTableColumn
nbRtPoliceRateLimitCoSlevel=_NbRtPoliceRateLimitCoSlevel_Object((1,3,6,1,4,1,629,1,50,12,9,3,2,1,2),_NbRtPoliceRateLimitCoSlevel_Type())
nbRtPoliceRateLimitCoSlevel.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtPoliceRateLimitCoSlevel.setStatus(_A)
_NbRtPoliceRateLimitBuckRate_Type=Integer32
_NbRtPoliceRateLimitBuckRate_Object=MibTableColumn
nbRtPoliceRateLimitBuckRate=_NbRtPoliceRateLimitBuckRate_Object((1,3,6,1,4,1,629,1,50,12,9,3,2,1,3),_NbRtPoliceRateLimitBuckRate_Type())
nbRtPoliceRateLimitBuckRate.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtPoliceRateLimitBuckRate.setStatus(_A)
_NbRtPoliceRateLimitBuckSize_Type=Integer32
_NbRtPoliceRateLimitBuckSize_Object=MibTableColumn
nbRtPoliceRateLimitBuckSize=_NbRtPoliceRateLimitBuckSize_Object((1,3,6,1,4,1,629,1,50,12,9,3,2,1,4),_NbRtPoliceRateLimitBuckSize_Type())
nbRtPoliceRateLimitBuckSize.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtPoliceRateLimitBuckSize.setStatus(_A)
class _NbRtPoliceRateLimitOperMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_F,1),(_A6,2),(_A7,3),(_A8,4),('coSnoRED',5),('coSguarantee',6),('coSREDtcp',7),('coSREDall',8),('coSguaranteeREDtcp',9),('coSguaranteeREDall',10)))
_NbRtPoliceRateLimitOperMode_Type.__name__=_E
_NbRtPoliceRateLimitOperMode_Object=MibTableColumn
nbRtPoliceRateLimitOperMode=_NbRtPoliceRateLimitOperMode_Object((1,3,6,1,4,1,629,1,50,12,9,3,2,1,5),_NbRtPoliceRateLimitOperMode_Type())
nbRtPoliceRateLimitOperMode.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtPoliceRateLimitOperMode.setStatus(_A)
_NbRtPoliceRateLimitExceedBytesCnt_Type=AccountCounter64
_NbRtPoliceRateLimitExceedBytesCnt_Object=MibTableColumn
nbRtPoliceRateLimitExceedBytesCnt=_NbRtPoliceRateLimitExceedBytesCnt_Object((1,3,6,1,4,1,629,1,50,12,9,3,2,1,6),_NbRtPoliceRateLimitExceedBytesCnt_Type())
nbRtPoliceRateLimitExceedBytesCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtPoliceRateLimitExceedBytesCnt.setStatus(_A)
_NbRtPoliceRateLimitExceedFramesCnt_Type=AccountCounter64
_NbRtPoliceRateLimitExceedFramesCnt_Object=MibTableColumn
nbRtPoliceRateLimitExceedFramesCnt=_NbRtPoliceRateLimitExceedFramesCnt_Object((1,3,6,1,4,1,629,1,50,12,9,3,2,1,7),_NbRtPoliceRateLimitExceedFramesCnt_Type())
nbRtPoliceRateLimitExceedFramesCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtPoliceRateLimitExceedFramesCnt.setStatus(_A)
_NbRtPoliceRateLimitHighExceedBytes32_Type=Counter32
_NbRtPoliceRateLimitHighExceedBytes32_Object=MibTableColumn
nbRtPoliceRateLimitHighExceedBytes32=_NbRtPoliceRateLimitHighExceedBytes32_Object((1,3,6,1,4,1,629,1,50,12,9,3,2,1,8),_NbRtPoliceRateLimitHighExceedBytes32_Type())
nbRtPoliceRateLimitHighExceedBytes32.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtPoliceRateLimitHighExceedBytes32.setStatus(_A)
_NbRtPoliceRateLimitLowExceedBytes32_Type=Counter32
_NbRtPoliceRateLimitLowExceedBytes32_Object=MibTableColumn
nbRtPoliceRateLimitLowExceedBytes32=_NbRtPoliceRateLimitLowExceedBytes32_Object((1,3,6,1,4,1,629,1,50,12,9,3,2,1,9),_NbRtPoliceRateLimitLowExceedBytes32_Type())
nbRtPoliceRateLimitLowExceedBytes32.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtPoliceRateLimitLowExceedBytes32.setStatus(_A)
_NbRtPoliceRateLimitHighExceedFrames32_Type=Counter32
_NbRtPoliceRateLimitHighExceedFrames32_Object=MibTableColumn
nbRtPoliceRateLimitHighExceedFrames32=_NbRtPoliceRateLimitHighExceedFrames32_Object((1,3,6,1,4,1,629,1,50,12,9,3,2,1,10),_NbRtPoliceRateLimitHighExceedFrames32_Type())
nbRtPoliceRateLimitHighExceedFrames32.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtPoliceRateLimitHighExceedFrames32.setStatus(_A)
_NbRtPoliceRateLimitLowExceedFrames32_Type=Counter32
_NbRtPoliceRateLimitLowExceedFrames32_Object=MibTableColumn
nbRtPoliceRateLimitLowExceedFrames32=_NbRtPoliceRateLimitLowExceedFrames32_Object((1,3,6,1,4,1,629,1,50,12,9,3,2,1,11),_NbRtPoliceRateLimitLowExceedFrames32_Type())
nbRtPoliceRateLimitLowExceedFrames32.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtPoliceRateLimitLowExceedFrames32.setStatus(_A)
_NbRtPoliceActionVifTable_Object=MibTable
nbRtPoliceActionVifTable=_NbRtPoliceActionVifTable_Object((1,3,6,1,4,1,629,1,50,12,9,4))
if mibBuilder.loadTexts:nbRtPoliceActionVifTable.setStatus(_A)
_NbRtPoliceActionVifEntry_Object=MibTableRow
nbRtPoliceActionVifEntry=_NbRtPoliceActionVifEntry_Object((1,3,6,1,4,1,629,1,50,12,9,4,1))
nbRtPoliceActionVifEntry.setIndexNames((0,_D,_I),(0,_D,_J),(0,_D,_K),(0,_D,_L),(0,_D,_AB),(0,_D,_AC))
if mibBuilder.loadTexts:nbRtPoliceActionVifEntry.setStatus(_A)
_NbRtPoliceActionVifDirection_Type=DirectionType
_NbRtPoliceActionVifDirection_Object=MibTableColumn
nbRtPoliceActionVifDirection=_NbRtPoliceActionVifDirection_Object((1,3,6,1,4,1,629,1,50,12,9,4,1,1),_NbRtPoliceActionVifDirection_Type())
nbRtPoliceActionVifDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtPoliceActionVifDirection.setStatus(_A)
_NbRtPoliceActionVifName_Type=ActionListName
_NbRtPoliceActionVifName_Object=MibTableColumn
nbRtPoliceActionVifName=_NbRtPoliceActionVifName_Object((1,3,6,1,4,1,629,1,50,12,9,4,1,2),_NbRtPoliceActionVifName_Type())
nbRtPoliceActionVifName.setMaxAccess(_B)
if mibBuilder.loadTexts:nbRtPoliceActionVifName.setStatus(_A)
_NbRtPoliceActionVifPortList_Type=OctetString
_NbRtPoliceActionVifPortList_Object=MibTableColumn
nbRtPoliceActionVifPortList=_NbRtPoliceActionVifPortList_Object((1,3,6,1,4,1,629,1,50,12,9,4,1,3),_NbRtPoliceActionVifPortList_Type())
nbRtPoliceActionVifPortList.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtPoliceActionVifPortList.setStatus(_A)
class _NbRtPoliceActionVifBindingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('addNewBind',1),('unbind',2),('editExistingBind',3)))
_NbRtPoliceActionVifBindingStatus_Type.__name__=_E
_NbRtPoliceActionVifBindingStatus_Object=MibTableColumn
nbRtPoliceActionVifBindingStatus=_NbRtPoliceActionVifBindingStatus_Object((1,3,6,1,4,1,629,1,50,12,9,4,1,4),_NbRtPoliceActionVifBindingStatus_Type())
nbRtPoliceActionVifBindingStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nbRtPoliceActionVifBindingStatus.setStatus(_A)
_NbRtMplsAction_ObjectIdentity=ObjectIdentity
nbRtMplsAction=_NbRtMplsAction_ObjectIdentity((1,3,6,1,4,1,629,1,50,12,9,5))
nbVifModify=NotificationType((1,3,6,1,4,1,629,1,50,12,0,11))
nbVifModify.setObjects(*((_D,_AD),(_D,_AE),(_D,_AF),(_D,_AG),(_D,_AH),(_D,_AI),(_D,_AJ),(_D,_AK),(_D,_AL),(_D,'nbVifMac'),(_D,_AM),(_D,_AN),(_D,_AO)))
if mibBuilder.loadTexts:nbVifModify.setStatus('')
mibBuilder.exportSymbols(_D,**{'MacAddress':MacAddress,'ActionListName':ActionListName,'DirectionType':DirectionType,'AccountCouter':AccountCouter,'AccountCounter64':AccountCounter64,'nbase':nbase,'nbSwitchG1':nbSwitchG1,'nbSwitchG1Il':nbSwitchG1Il,'nbRouterConfig':nbRouterConfig,'nbVifModify':nbVifModify,'nbRtConfigGen':nbRtConfigGen,'nbRtDevDiffServMode':nbRtDevDiffServMode,'nbRtDevDiffServMappingSupport':nbRtDevDiffServMappingSupport,'nbRtVifTable':nbRtVifTable,'nbRtVifEntry':nbRtVifEntry,_f:nbRtVifId,'nbRtVifIpAddress':nbRtVifIpAddress,'nbRtVifMask':nbRtVifMask,'nbRtVifProtocol':nbRtVifProtocol,'nbRtVifName':nbRtVifName,'nbRtVifPortList':nbRtVifPortList,'nbRtVifMac':nbRtVifMac,'nbRtVifAdminStatus':nbRtVifAdminStatus,'nbRtVifConfigType':nbRtVifConfigType,'nbRtVifSecurity':nbRtVifSecurity,'nbRtVifIsTagged':nbRtVifIsTagged,'nbRtVifTag':nbRtVifTag,'nbRtVifGroup':nbRtVifGroup,'nbVifTableSize':nbVifTableSize,'nbVifDeviceLimitTable':nbVifDeviceLimitTable,'nbVifDeviceLimitEntry':nbVifDeviceLimitEntry,_m:nbVifLimitType,'nbVifDevNoMin':nbVifDevNoMin,'nbVifDevNoMax':nbVifDevNoMax,'nbVifDevNoFirstEmpty':nbVifDevNoFirstEmpty,'nbVifAliasDLimitTable':nbVifAliasDLimitTable,'nbVifAliasDLimitEntry':nbVifAliasDLimitEntry,_n:nbVifAliasLimitType,_o:nbVifAliasLimitDevNo,'nbVifAliasLimitDevAliasMin':nbVifAliasLimitDevAliasMin,'nbVifAliasLimitDevAliasMax':nbVifAliasLimitDevAliasMax,'nbVifAliasLimitDevAliasFirstEmpty':nbVifAliasLimitDevAliasFirstEmpty,'nbVifTable':nbVifTable,'nbVifEntry':nbVifEntry,_I:nbVifType,_J:nbVifDevNo,_K:nbVifIsAlias,_L:nbVifAliasDev,_AD:nbVifDevName,_AJ:nbVifIpAddress,_AK:nbVifMask,_AM:nbVifPeer,_AF:nbVifPhysType,_AG:nbVifProtocol,_AI:nbVifName,_AL:nbVifPortList,'nbVifMac':nbVifMac,_AH:nbVifState,_AE:nbVifAdminStatus,_AN:nbVifConfigType,_AO:nbVifSecurity,'nbVifIsTagged':nbVifIsTagged,'nbVifTag':nbVifTag,'nbVifDescr':nbVifDescr,'nbVifLastChange':nbVifLastChange,'nbVifL2SwitchingMode':nbVifL2SwitchingMode,'nbVifProxyArpMode':nbVifProxyArpMode,'nbVifIpOnlyMode':nbVifIpOnlyMode,'nbVifIpForwardingMode':nbVifIpForwardingMode,'nbRtFib':nbRtFib,'nbRtFibNumEntries':nbRtFibNumEntries,'nbRtFibTable':nbRtFibTable,'nbRtFibEntry':nbRtFibEntry,_p:nbRtFibEntryIpAddress,_q:nbRtFibEntryIpMask,_r:nbRtFibEntryProtocol,'nbRtFibEntryNextHop':nbRtFibEntryNextHop,'nbRtFibEntryNextPhysAddress':nbRtFibEntryNextPhysAddress,'nbRtFibEntryNextPort':nbRtFibEntryNextPort,'nbRtFibEntryLastChTime':nbRtFibEntryLastChTime,'nbRtFibEntryAge':nbRtFibEntryAge,'nbRtFibEntryMetric':nbRtFibEntryMetric,'nbRtFibEntryAdminStatus':nbRtFibEntryAdminStatus,'nbRtFibEntryTag':nbRtFibEntryTag,'nbRtDiffServ':nbRtDiffServ,'nbRtDiffServTable':nbRtDiffServTable,'nbRtDiffServEntry':nbRtDiffServEntry,'nbRtDiffServMode':nbRtDiffServMode,'nbRtDiffServVptMapNameIndex':nbRtDiffServVptMapNameIndex,'nbRtDiffServDscpMapNameIndex':nbRtDiffServDscpMapNameIndex,'nbRtDiffServMgmtVptMapNameIndex':nbRtDiffServMgmtVptMapNameIndex,'nbRtDiffServMgmtDscpMapNameIndex':nbRtDiffServMgmtDscpMapNameIndex,'nbRtVifDiffServRateLimitTable':nbRtVifDiffServRateLimitTable,'nbRtVifDiffServRateLimitEntry':nbRtVifDiffServRateLimitEntry,_s:nbRtVifDiffServDirect,'nbRtVifDiffServBuckRate':nbRtVifDiffServBuckRate,'nbRtVifDiffServBuckSize':nbRtVifDiffServBuckSize,'nbRtVifDiffServREDmode':nbRtVifDiffServREDmode,'nbRtVifDiffServAdminStatus':nbRtVifDiffServAdminStatus,'nbRtDiffServVptMapTable':nbRtDiffServVptMapTable,'nbRtDiffServVptMapEntry':nbRtDiffServVptMapEntry,_t:nbRtDiffServVptMapNameId,'nbRtDiffServVptMapName':nbRtDiffServVptMapName,'nbRtDiffServVptMapStatus':nbRtDiffServVptMapStatus,'nbRtDiffServVptMapAdminStatus':nbRtDiffServVptMapAdminStatus,'nbRtDiffServVptMapPrflTable':nbRtDiffServVptMapPrflTable,'nbRtDiffServVptMapPrflEntry':nbRtDiffServVptMapPrflEntry,_v:nbRtDiffServVptMapPrflNameId,_w:nbRtDiffServVptMapPrflInValueId,'nbRtDiffServVptMapPrflInValue':nbRtDiffServVptMapPrflInValue,'nbRtDiffServVptMapPrflSl':nbRtDiffServVptMapPrflSl,'nbRtDiffServVptMapPrflOutValue':nbRtDiffServVptMapPrflOutValue,'nbRtDiffServDscpMapTable':nbRtDiffServDscpMapTable,'nbRtDiffServDscpMapEntry':nbRtDiffServDscpMapEntry,_x:nbRtDiffServDscpMapNameId,'nbRtDiffServDscpMapName':nbRtDiffServDscpMapName,'nbRtDiffServDscpMapStatus':nbRtDiffServDscpMapStatus,'nbRtDiffServDscpMapAdminStatus':nbRtDiffServDscpMapAdminStatus,'nbRtDiffServDscpMapPrflTable':nbRtDiffServDscpMapPrflTable,'nbRtDiffServDscpMapPrflEntry':nbRtDiffServDscpMapPrflEntry,_y:nbRtDiffServDscpMapPrflNameId,_z:nbRtDiffServDscpMapPrflInValueId,'nbRtDiffServDscpMapPrflInValue':nbRtDiffServDscpMapPrflInValue,'nbRtDiffServDscpMapPrflSl':nbRtDiffServDscpMapPrflSl,'nbRtDiffServDscpMapPrflOutValue':nbRtDiffServDscpMapPrflOutValue,'nbRtAccounting':nbRtAccounting,'nbRtAccVifTable':nbRtAccVifTable,'nbRtAccVifEntry':nbRtAccVifEntry,_U:nbRtAccVifDirection,'nbRtAccVifAdminStatus':nbRtAccVifAdminStatus,'nbRtAccVifOperStatus':nbRtAccVifOperStatus,'nbRtAccVifConformingBytes':nbRtAccVifConformingBytes,'nbRtAccVifExceedingBytes':nbRtAccVifExceedingBytes,'nbRtAccVifConformingPackets':nbRtAccVifConformingPackets,'nbRtAccVifExceedingPackets':nbRtAccVifExceedingPackets,'nbRtAccVifHighConformingBytes':nbRtAccVifHighConformingBytes,'nbRtAccVifHighExceedingBytes':nbRtAccVifHighExceedingBytes,'nbRtAccVifHighConformingPackets':nbRtAccVifHighConformingPackets,'nbRtAccVifHighExceedingPackets':nbRtAccVifHighExceedingPackets,'nbRtAccVifLowConformingBytes':nbRtAccVifLowConformingBytes,'nbRtAccVifLowExceedingBytes':nbRtAccVifLowExceedingBytes,'nbRtAccVifLowConformingPackets':nbRtAccVifLowConformingPackets,'nbRtAccVifLowExceedingPackets':nbRtAccVifLowExceedingPackets,'nbRtAccVif64ConformingBytes':nbRtAccVif64ConformingBytes,'nbRtAccVif64ExceedingBytes':nbRtAccVif64ExceedingBytes,'nbRtAccVifConformingUcastPackets':nbRtAccVifConformingUcastPackets,'nbRtAccVifHighConformingUcastPackets':nbRtAccVifHighConformingUcastPackets,'nbRtAccVifLowConformingUcastPackets':nbRtAccVifLowConformingUcastPackets,'nbRtAccVif64ConformingUcastPackets':nbRtAccVif64ConformingUcastPackets,'nbRtAccVifConformingMcastPackets':nbRtAccVifConformingMcastPackets,'nbRtAccVifHighConformingMcastPackets':nbRtAccVifHighConformingMcastPackets,'nbRtAccVifLowConformingMcastPackets':nbRtAccVifLowConformingMcastPackets,'nbRtAccVif64ConformingMcastPackets':nbRtAccVif64ConformingMcastPackets,'nbRtAccVifConformingBcastPackets':nbRtAccVifConformingBcastPackets,'nbRtAccVifHighConformingBcastPackets':nbRtAccVifHighConformingBcastPackets,'nbRtAccVifLowConformingBcastPackets':nbRtAccVifLowConformingBcastPackets,'nbRtAccVif64ConformingBcastPackets':nbRtAccVif64ConformingBcastPackets,'nbRtAccVifPortTable':nbRtAccVifPortTable,'nbRtAccVifPortEntry':nbRtAccVifPortEntry,_A0:nbRtVifPortId,'nbRtAccPortAdminStatus':nbRtAccPortAdminStatus,'nbRtAccPortOperStatus':nbRtAccPortOperStatus,'nbRtAccPortConformingBytes':nbRtAccPortConformingBytes,'nbRtAccPortExceedingBytes':nbRtAccPortExceedingBytes,'nbRtAccPortConformingPackets':nbRtAccPortConformingPackets,'nbRtAccPortExceedingPackets':nbRtAccPortExceedingPackets,'nbRtAccPortHighConformingBytes':nbRtAccPortHighConformingBytes,'nbRtAccPortHighExceedingBytes':nbRtAccPortHighExceedingBytes,'nbRtAccPortHighConformingPackets':nbRtAccPortHighConformingPackets,'nbRtAccPortHighExceedingPackets':nbRtAccPortHighExceedingPackets,'nbRtAccPortLowConformingBytes':nbRtAccPortLowConformingBytes,'nbRtAccPortLowExceedingBytes':nbRtAccPortLowExceedingBytes,'nbRtAccPortLowConformingPackets':nbRtAccPortLowConformingPackets,'nbRtAccPortLowExceedingPackets':nbRtAccPortLowExceedingPackets,'nbRtAccPortVif64ConformingBytes':nbRtAccPortVif64ConformingBytes,'nbRtAccPortVif64ExceedingBytes':nbRtAccPortVif64ExceedingBytes,'nbRtAccPortConformingUcastPackets':nbRtAccPortConformingUcastPackets,'nbRtAccPortHighConformingUcastPackets':nbRtAccPortHighConformingUcastPackets,'nbRtAccPortLowConformingUcastPackets':nbRtAccPortLowConformingUcastPackets,'nbRtAccPort64ConformingUcastPackets':nbRtAccPort64ConformingUcastPackets,'nbRtAccPortConformingMcastPackets':nbRtAccPortConformingMcastPackets,'nbRtAccPortHighConformingMcastPackets':nbRtAccPortHighConformingMcastPackets,'nbRtAccPortLowConformingMcastPackets':nbRtAccPortLowConformingMcastPackets,'nbRtAccPort64ConformingMcastPackets':nbRtAccPort64ConformingMcastPackets,'nbRtAccPortConformingBcastPackets':nbRtAccPortConformingBcastPackets,'nbRtAccPortHighConformingBcastPackets':nbRtAccPortHighConformingBcastPackets,'nbRtAccPortLowConformingBcastPackets':nbRtAccPortLowConformingBcastPackets,'nbRtAccPort64ConformingBcastPackets':nbRtAccPort64ConformingBcastPackets,'nbRtAccessLists':nbRtAccessLists,'nbAclVifTable':nbAclVifTable,'nbAclVifEntry':nbAclVifEntry,_A1:nbAclVifDirection,_A2:nbAclVifId,'nbAclVifAccessListName':nbAclVifAccessListName,'nbAclVifBindingStatus':nbAclVifBindingStatus,'nbRtPortTagGroup':nbRtPortTagGroup,'nbRtPortTagTable':nbRtPortTagTable,'nbRtPortTagEntry':nbRtPortTagEntry,_A3:nbRtPortTagId,'nbRtPortTagAwareMode':nbRtPortTagAwareMode,'nbRtPortTagEtherType':nbRtPortTagEtherType,'nbRtPortTagIpDefTag':nbRtPortTagIpDefTag,'nbRtPortTagPortDefTag':nbRtPortTagPortDefTag,'nbRtPortTagVmanDefTag':nbRtPortTagVmanDefTag,'nbRtPortTagNumberOfTags':nbRtPortTagNumberOfTags,'nbRtPortTagMplsForceMode':nbRtPortTagMplsForceMode,'nbRtActionLists':nbRtActionLists,'nbRtActionListSupport':nbRtActionListSupport,'nbRtActionListTable':nbRtActionListTable,'nbRtActionListEntry':nbRtActionListEntry,_A4:nbRtActionListName,'nbRtActionListAdminStatus':nbRtActionListAdminStatus,'nbRtActionListOperStatus':nbRtActionListOperStatus,'nbRtActionListPoliceType':nbRtActionListPoliceType,'nbRtActionListMplsType':nbRtActionListMplsType,'nbRtPoliceAction':nbRtPoliceAction,'nbRtPoliceActionTable':nbRtPoliceActionTable,'nbRtPoliceActionEntry':nbRtPoliceActionEntry,_A5:nbRtPoliceActionName,'nbRtPoliceActionOperMode':nbRtPoliceActionOperMode,'nbRtPoliceActionSharingMode':nbRtPoliceActionSharingMode,'nbRtPoliceActionAdminStatus':nbRtPoliceActionAdminStatus,'nbRtPoliceActionExceedCntAdminStatus':nbRtPoliceActionExceedCntAdminStatus,'nbRtPoliceActionExceedCntOperStatus':nbRtPoliceActionExceedCntOperStatus,'nbRtPoliceActionTotalExceedBytesCnt':nbRtPoliceActionTotalExceedBytesCnt,'nbRtPoliceActionTotalExceedFramesCnt':nbRtPoliceActionTotalExceedFramesCnt,'nbRtPoliceActionTotalHighExceedBytes32':nbRtPoliceActionTotalHighExceedBytes32,'nbRtPoliceActionTotalLowExceedBytes32':nbRtPoliceActionTotalLowExceedBytes32,'nbRtPoliceActionTotalHighExceedFrames32':nbRtPoliceActionTotalHighExceedFrames32,'nbRtPoliceActionTotalLowExceedFrames32':nbRtPoliceActionTotalLowExceedFrames32,'nbRtPoliceRateLimitTable':nbRtPoliceRateLimitTable,'nbRtPoliceRateLimitEntry':nbRtPoliceRateLimitEntry,_A9:nbRtPoliceRateLimitName,_AA:nbRtPoliceRateLimitCoSlevel,'nbRtPoliceRateLimitBuckRate':nbRtPoliceRateLimitBuckRate,'nbRtPoliceRateLimitBuckSize':nbRtPoliceRateLimitBuckSize,'nbRtPoliceRateLimitOperMode':nbRtPoliceRateLimitOperMode,'nbRtPoliceRateLimitExceedBytesCnt':nbRtPoliceRateLimitExceedBytesCnt,'nbRtPoliceRateLimitExceedFramesCnt':nbRtPoliceRateLimitExceedFramesCnt,'nbRtPoliceRateLimitHighExceedBytes32':nbRtPoliceRateLimitHighExceedBytes32,'nbRtPoliceRateLimitLowExceedBytes32':nbRtPoliceRateLimitLowExceedBytes32,'nbRtPoliceRateLimitHighExceedFrames32':nbRtPoliceRateLimitHighExceedFrames32,'nbRtPoliceRateLimitLowExceedFrames32':nbRtPoliceRateLimitLowExceedFrames32,'nbRtPoliceActionVifTable':nbRtPoliceActionVifTable,'nbRtPoliceActionVifEntry':nbRtPoliceActionVifEntry,_AB:nbRtPoliceActionVifDirection,_AC:nbRtPoliceActionVifName,'nbRtPoliceActionVifPortList':nbRtPoliceActionVifPortList,'nbRtPoliceActionVifBindingStatus':nbRtPoliceActionVifBindingStatus,'nbRtMplsAction':nbRtMplsAction})