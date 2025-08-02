_Ag='ciscoCipTgCmgrGroup'
_Af='ciscoCipTgIpGroup'
_Ae='ciscoCipTgLlcGroupRev1'
_Ad='ciscoCipTgLlcGroup'
_Ac='cipTgCmgrOperConnStatus'
_Ab='cipTgCmgrOperVcStatus'
_Aa='cipTgCmgrOperRemoteConnToken'
_AZ='cipTgCmgrOperLocalConnToken'
_AY='cipTgCmgrOperRemoteVcToken'
_AX='cipTgCmgrOperLocalVcToken'
_AW='cipTgCmgrOperRemoteGrToken'
_AV='cipTgCmgrOperLocalGrToken'
_AU='cipTgCmgrOperType'
_AT='cipTgIpStatsHCBytesOut'
_AS='cipTgIpStatsBytesOut'
_AR='cipTgIpStatsPacketsOut'
_AQ='cipTgIpStatsHCBytesIn'
_AP='cipTgIpStatsBytesIn'
_AO='cipTgIpStatsPacketsIn'
_AN='cipTgIpOperConnStatus'
_AM='cipTgIpOperVcStatus'
_AL='cipTgIpOperRemoteConnToken'
_AK='cipTgIpOperLocalConnToken'
_AJ='cipTgIpOperRemoteVcToken'
_AI='cipTgIpOperLocalVcToken'
_AH='cipTgIpAdminRowStatus'
_AG='cipTgIpAdminBroadcast'
_AF='cipTgIpAdminLocalIpAddr'
_AE='cipTgIpAdminRemoteIpAddr'
_AD='cipTgIpAdminType'
_AC='cipTgLlcStatsConnNumberSent'
_AB='cipTgLlcStatsConnNumberRecv'
_AA='cipTgLlcOperConnStatus'
_A9='cipTgLlcOperVcStatus'
_A8='cipTgLlcOperRemoteConnToken'
_A7='cipTgLlcOperLocalConnToken'
_A6='cipTgLlcOperRemoteVcToken'
_A5='cipTgLlcOperLocalVcToken'
_A4='cipTgIpStatsEntry'
_A3='cipTgIpOperEntry'
_A2='cipTgLlcStatsEntry'
_A1='cipTgLlcOperEntry'
_A0='cipTgCmgrOperName'
_z='cipTgIpAdminName'
_y='pendingActive'
_x='connRequestSent'
_w='cipTgLlcAdminName'
_v='SAPType'
_u='OctetString'
_t='cipTgLlcStatsXidRspsOut'
_s='cipTgLlcStatsXidRspsIn'
_r='cipTgLlcStatsXidCmdsOut'
_q='cipTgLlcStatsXidCmdsIn'
_p='cipTgLlcStatsTestRspsIn'
_o='cipTgLlcStatsTestCmdsOut'
_n='cipTgLlcStatsHCUIFrameBytesOut'
_m='cipTgLlcStatsUIFrameBytesOut'
_l='cipTgLlcStatsUIFramesOut'
_k='cipTgLlcStatsHCUIFrameBytesIn'
_j='cipTgLlcStatsUIFrameBytesIn'
_i='cipTgLlcStatsUIFramesIn'
_h='cipTgLlcStatsHCIFrameBytesOut'
_g='cipTgLlcStatsIFrameBytesOut'
_f='cipTgLlcStatsIFramesOut'
_e='cipTgLlcStatsHCIFrameBytesIn'
_d='cipTgLlcStatsIFrameBytesIn'
_c='cipTgLlcStatsIFramesIn'
_b='cipTgLlcOperRIF'
_a='cipTgLlcOperHprRSAP'
_Z='cipTgLlcOperHprLSAP'
_Y='cipTgLlcOperHpr'
_X='cipTgLlcOperMaxOut'
_W='cipTgLlcOperMaxIn'
_V='cipTgLlcOperRemoteCP'
_U='cipTgLlcOperLocalCP'
_T='cipTgLlcOperTGN'
_S='cipTgLlcOperState'
_R='cipTgLlcAdminRowStatus'
_Q='cipTgLlcAdminRSAP'
_P='cipTgLlcAdminRMAC'
_O='cipTgLlcAdminLSAP'
_N='cipTgLlcAdminAdaptNo'
_M='cipTgLlcAdminLanType'
_L='not-accessible'
_K='DisplayString'
_J='ifIndex'
_I='IF-MIB'
_H='active'
_G='reset'
_F='octets'
_E='read-create'
_D='Integer32'
_C='read-only'
_B='current'
_A='CISCO-CIPTG-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_u,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
SAPType,=mibBuilder.importSymbols('CISCO-TC',_v)
ifIndex,=mibBuilder.importSymbols(_I,_J)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_K,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
ciscoCipTgMIB=ModuleIdentity((1,3,6,1,4,1,9,9,73))
if mibBuilder.loadTexts:ciscoCipTgMIB.setRevisions(('1999-01-25 00:00','1998-01-06 00:00','1997-02-09 00:00','1997-03-14 00:00'))
class ChannelTgName(DisplayString):status=_B;subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class ChannelTgToken(DisplayString):status=_B;subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_CipTgObjects_ObjectIdentity=ObjectIdentity
cipTgObjects=_CipTgObjects_ObjectIdentity((1,3,6,1,4,1,9,9,73,1))
_CipTgLlc_ObjectIdentity=ObjectIdentity
cipTgLlc=_CipTgLlc_ObjectIdentity((1,3,6,1,4,1,9,9,73,1,1))
_CipTgLlcAdminTable_Object=MibTable
cipTgLlcAdminTable=_CipTgLlcAdminTable_Object((1,3,6,1,4,1,9,9,73,1,1,1))
if mibBuilder.loadTexts:cipTgLlcAdminTable.setStatus(_B)
_CipTgLlcAdminEntry_Object=MibTableRow
cipTgLlcAdminEntry=_CipTgLlcAdminEntry_Object((1,3,6,1,4,1,9,9,73,1,1,1,1))
cipTgLlcAdminEntry.setIndexNames((0,_I,_J),(0,_A,_w))
if mibBuilder.loadTexts:cipTgLlcAdminEntry.setStatus(_B)
_CipTgLlcAdminName_Type=ChannelTgName
_CipTgLlcAdminName_Object=MibTableColumn
cipTgLlcAdminName=_CipTgLlcAdminName_Object((1,3,6,1,4,1,9,9,73,1,1,1,1,1),_CipTgLlcAdminName_Type())
cipTgLlcAdminName.setMaxAccess(_L)
if mibBuilder.loadTexts:cipTgLlcAdminName.setStatus(_B)
class _CipTgLlcAdminLanType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('iso88023csmacd',1),('iso88025tokenRing',2),('fddi',3)))
_CipTgLlcAdminLanType_Type.__name__=_D
_CipTgLlcAdminLanType_Object=MibTableColumn
cipTgLlcAdminLanType=_CipTgLlcAdminLanType_Object((1,3,6,1,4,1,9,9,73,1,1,1,1,2),_CipTgLlcAdminLanType_Type())
cipTgLlcAdminLanType.setMaxAccess(_E)
if mibBuilder.loadTexts:cipTgLlcAdminLanType.setStatus(_B)
class _CipTgLlcAdminAdaptNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_CipTgLlcAdminAdaptNo_Type.__name__=_D
_CipTgLlcAdminAdaptNo_Object=MibTableColumn
cipTgLlcAdminAdaptNo=_CipTgLlcAdminAdaptNo_Object((1,3,6,1,4,1,9,9,73,1,1,1,1,3),_CipTgLlcAdminAdaptNo_Type())
cipTgLlcAdminAdaptNo.setMaxAccess(_E)
if mibBuilder.loadTexts:cipTgLlcAdminAdaptNo.setStatus(_B)
_CipTgLlcAdminLSAP_Type=SAPType
_CipTgLlcAdminLSAP_Object=MibTableColumn
cipTgLlcAdminLSAP=_CipTgLlcAdminLSAP_Object((1,3,6,1,4,1,9,9,73,1,1,1,1,4),_CipTgLlcAdminLSAP_Type())
cipTgLlcAdminLSAP.setMaxAccess(_E)
if mibBuilder.loadTexts:cipTgLlcAdminLSAP.setStatus(_B)
_CipTgLlcAdminRMAC_Type=MacAddress
_CipTgLlcAdminRMAC_Object=MibTableColumn
cipTgLlcAdminRMAC=_CipTgLlcAdminRMAC_Object((1,3,6,1,4,1,9,9,73,1,1,1,1,5),_CipTgLlcAdminRMAC_Type())
cipTgLlcAdminRMAC.setMaxAccess(_E)
if mibBuilder.loadTexts:cipTgLlcAdminRMAC.setStatus(_B)
class _CipTgLlcAdminRSAP_Type(SAPType):defaultValue=4
_CipTgLlcAdminRSAP_Type.__name__=_v
_CipTgLlcAdminRSAP_Object=MibTableColumn
cipTgLlcAdminRSAP=_CipTgLlcAdminRSAP_Object((1,3,6,1,4,1,9,9,73,1,1,1,1,6),_CipTgLlcAdminRSAP_Type())
cipTgLlcAdminRSAP.setMaxAccess(_E)
if mibBuilder.loadTexts:cipTgLlcAdminRSAP.setStatus(_B)
_CipTgLlcAdminRowStatus_Type=RowStatus
_CipTgLlcAdminRowStatus_Object=MibTableColumn
cipTgLlcAdminRowStatus=_CipTgLlcAdminRowStatus_Object((1,3,6,1,4,1,9,9,73,1,1,1,1,7),_CipTgLlcAdminRowStatus_Type())
cipTgLlcAdminRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cipTgLlcAdminRowStatus.setStatus(_B)
_CipTgLlcOperTable_Object=MibTable
cipTgLlcOperTable=_CipTgLlcOperTable_Object((1,3,6,1,4,1,9,9,73,1,1,2))
if mibBuilder.loadTexts:cipTgLlcOperTable.setStatus(_B)
_CipTgLlcOperEntry_Object=MibTableRow
cipTgLlcOperEntry=_CipTgLlcOperEntry_Object((1,3,6,1,4,1,9,9,73,1,1,2,1))
if mibBuilder.loadTexts:cipTgLlcOperEntry.setStatus(_B)
class _CipTgLlcOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('shutdown',1),(_G,2),('locatePeer',3),('peerLocated',4),('negotiation',5),('contactPending',6),(_H,7)))
_CipTgLlcOperState_Type.__name__=_D
_CipTgLlcOperState_Object=MibTableColumn
cipTgLlcOperState=_CipTgLlcOperState_Object((1,3,6,1,4,1,9,9,73,1,1,2,1,1),_CipTgLlcOperState_Type())
cipTgLlcOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgLlcOperState.setStatus(_B)
_CipTgLlcOperTGN_Type=Integer32
_CipTgLlcOperTGN_Object=MibTableColumn
cipTgLlcOperTGN=_CipTgLlcOperTGN_Object((1,3,6,1,4,1,9,9,73,1,1,2,1,2),_CipTgLlcOperTGN_Type())
cipTgLlcOperTGN.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgLlcOperTGN.setStatus(_B)
class _CipTgLlcOperLocalCP_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_CipTgLlcOperLocalCP_Type.__name__=_K
_CipTgLlcOperLocalCP_Object=MibTableColumn
cipTgLlcOperLocalCP=_CipTgLlcOperLocalCP_Object((1,3,6,1,4,1,9,9,73,1,1,2,1,3),_CipTgLlcOperLocalCP_Type())
cipTgLlcOperLocalCP.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgLlcOperLocalCP.setStatus(_B)
class _CipTgLlcOperRemoteCP_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_CipTgLlcOperRemoteCP_Type.__name__=_K
_CipTgLlcOperRemoteCP_Object=MibTableColumn
cipTgLlcOperRemoteCP=_CipTgLlcOperRemoteCP_Object((1,3,6,1,4,1,9,9,73,1,1,2,1,4),_CipTgLlcOperRemoteCP_Type())
cipTgLlcOperRemoteCP.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgLlcOperRemoteCP.setStatus(_B)
_CipTgLlcOperMaxIn_Type=Integer32
_CipTgLlcOperMaxIn_Object=MibTableColumn
cipTgLlcOperMaxIn=_CipTgLlcOperMaxIn_Object((1,3,6,1,4,1,9,9,73,1,1,2,1,5),_CipTgLlcOperMaxIn_Type())
cipTgLlcOperMaxIn.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgLlcOperMaxIn.setStatus(_B)
_CipTgLlcOperMaxOut_Type=Integer32
_CipTgLlcOperMaxOut_Object=MibTableColumn
cipTgLlcOperMaxOut=_CipTgLlcOperMaxOut_Object((1,3,6,1,4,1,9,9,73,1,1,2,1,6),_CipTgLlcOperMaxOut_Type())
cipTgLlcOperMaxOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgLlcOperMaxOut.setStatus(_B)
_CipTgLlcOperHpr_Type=TruthValue
_CipTgLlcOperHpr_Object=MibTableColumn
cipTgLlcOperHpr=_CipTgLlcOperHpr_Object((1,3,6,1,4,1,9,9,73,1,1,2,1,7),_CipTgLlcOperHpr_Type())
cipTgLlcOperHpr.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgLlcOperHpr.setStatus(_B)
_CipTgLlcOperHprLSAP_Type=SAPType
_CipTgLlcOperHprLSAP_Object=MibTableColumn
cipTgLlcOperHprLSAP=_CipTgLlcOperHprLSAP_Object((1,3,6,1,4,1,9,9,73,1,1,2,1,8),_CipTgLlcOperHprLSAP_Type())
cipTgLlcOperHprLSAP.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgLlcOperHprLSAP.setStatus(_B)
_CipTgLlcOperHprRSAP_Type=SAPType
_CipTgLlcOperHprRSAP_Object=MibTableColumn
cipTgLlcOperHprRSAP=_CipTgLlcOperHprRSAP_Object((1,3,6,1,4,1,9,9,73,1,1,2,1,9),_CipTgLlcOperHprRSAP_Type())
cipTgLlcOperHprRSAP.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgLlcOperHprRSAP.setStatus(_B)
class _CipTgLlcOperRIF_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,18))
_CipTgLlcOperRIF_Type.__name__=_u
_CipTgLlcOperRIF_Object=MibTableColumn
cipTgLlcOperRIF=_CipTgLlcOperRIF_Object((1,3,6,1,4,1,9,9,73,1,1,2,1,10),_CipTgLlcOperRIF_Type())
cipTgLlcOperRIF.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgLlcOperRIF.setStatus(_B)
_CipTgLlcOperLocalVcToken_Type=ChannelTgToken
_CipTgLlcOperLocalVcToken_Object=MibTableColumn
cipTgLlcOperLocalVcToken=_CipTgLlcOperLocalVcToken_Object((1,3,6,1,4,1,9,9,73,1,1,2,1,11),_CipTgLlcOperLocalVcToken_Type())
cipTgLlcOperLocalVcToken.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgLlcOperLocalVcToken.setStatus(_B)
_CipTgLlcOperRemoteVcToken_Type=ChannelTgToken
_CipTgLlcOperRemoteVcToken_Object=MibTableColumn
cipTgLlcOperRemoteVcToken=_CipTgLlcOperRemoteVcToken_Object((1,3,6,1,4,1,9,9,73,1,1,2,1,12),_CipTgLlcOperRemoteVcToken_Type())
cipTgLlcOperRemoteVcToken.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgLlcOperRemoteVcToken.setStatus(_B)
_CipTgLlcOperLocalConnToken_Type=ChannelTgToken
_CipTgLlcOperLocalConnToken_Object=MibTableColumn
cipTgLlcOperLocalConnToken=_CipTgLlcOperLocalConnToken_Object((1,3,6,1,4,1,9,9,73,1,1,2,1,13),_CipTgLlcOperLocalConnToken_Type())
cipTgLlcOperLocalConnToken.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgLlcOperLocalConnToken.setStatus(_B)
_CipTgLlcOperRemoteConnToken_Type=ChannelTgToken
_CipTgLlcOperRemoteConnToken_Object=MibTableColumn
cipTgLlcOperRemoteConnToken=_CipTgLlcOperRemoteConnToken_Object((1,3,6,1,4,1,9,9,73,1,1,2,1,14),_CipTgLlcOperRemoteConnToken_Type())
cipTgLlcOperRemoteConnToken.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgLlcOperRemoteConnToken.setStatus(_B)
class _CipTgLlcOperVcStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_CipTgLlcOperVcStatus_Type.__name__=_D
_CipTgLlcOperVcStatus_Object=MibTableColumn
cipTgLlcOperVcStatus=_CipTgLlcOperVcStatus_Object((1,3,6,1,4,1,9,9,73,1,1,2,1,15),_CipTgLlcOperVcStatus_Type())
cipTgLlcOperVcStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgLlcOperVcStatus.setStatus(_B)
class _CipTgLlcOperConnStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_x,2),(_y,3),(_H,4)))
_CipTgLlcOperConnStatus_Type.__name__=_D
_CipTgLlcOperConnStatus_Object=MibTableColumn
cipTgLlcOperConnStatus=_CipTgLlcOperConnStatus_Object((1,3,6,1,4,1,9,9,73,1,1,2,1,16),_CipTgLlcOperConnStatus_Type())
cipTgLlcOperConnStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgLlcOperConnStatus.setStatus(_B)
_CipTgLlcStatsTable_Object=MibTable
cipTgLlcStatsTable=_CipTgLlcStatsTable_Object((1,3,6,1,4,1,9,9,73,1,1,3))
if mibBuilder.loadTexts:cipTgLlcStatsTable.setStatus(_B)
_CipTgLlcStatsEntry_Object=MibTableRow
cipTgLlcStatsEntry=_CipTgLlcStatsEntry_Object((1,3,6,1,4,1,9,9,73,1,1,3,1))
if mibBuilder.loadTexts:cipTgLlcStatsEntry.setStatus(_B)
_CipTgLlcStatsIFramesIn_Type=Counter32
_CipTgLlcStatsIFramesIn_Object=MibTableColumn
cipTgLlcStatsIFramesIn=_CipTgLlcStatsIFramesIn_Object((1,3,6,1,4,1,9,9,73,1,1,3,1,1),_CipTgLlcStatsIFramesIn_Type())
cipTgLlcStatsIFramesIn.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgLlcStatsIFramesIn.setStatus(_B)
_CipTgLlcStatsIFrameBytesIn_Type=Counter32
_CipTgLlcStatsIFrameBytesIn_Object=MibTableColumn
cipTgLlcStatsIFrameBytesIn=_CipTgLlcStatsIFrameBytesIn_Object((1,3,6,1,4,1,9,9,73,1,1,3,1,2),_CipTgLlcStatsIFrameBytesIn_Type())
cipTgLlcStatsIFrameBytesIn.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgLlcStatsIFrameBytesIn.setStatus(_B)
if mibBuilder.loadTexts:cipTgLlcStatsIFrameBytesIn.setUnits(_F)
_CipTgLlcStatsHCIFrameBytesIn_Type=Counter64
_CipTgLlcStatsHCIFrameBytesIn_Object=MibTableColumn
cipTgLlcStatsHCIFrameBytesIn=_CipTgLlcStatsHCIFrameBytesIn_Object((1,3,6,1,4,1,9,9,73,1,1,3,1,3),_CipTgLlcStatsHCIFrameBytesIn_Type())
cipTgLlcStatsHCIFrameBytesIn.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgLlcStatsHCIFrameBytesIn.setStatus(_B)
_CipTgLlcStatsIFramesOut_Type=Counter32
_CipTgLlcStatsIFramesOut_Object=MibTableColumn
cipTgLlcStatsIFramesOut=_CipTgLlcStatsIFramesOut_Object((1,3,6,1,4,1,9,9,73,1,1,3,1,4),_CipTgLlcStatsIFramesOut_Type())
cipTgLlcStatsIFramesOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgLlcStatsIFramesOut.setStatus(_B)
_CipTgLlcStatsIFrameBytesOut_Type=Counter32
_CipTgLlcStatsIFrameBytesOut_Object=MibTableColumn
cipTgLlcStatsIFrameBytesOut=_CipTgLlcStatsIFrameBytesOut_Object((1,3,6,1,4,1,9,9,73,1,1,3,1,5),_CipTgLlcStatsIFrameBytesOut_Type())
cipTgLlcStatsIFrameBytesOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgLlcStatsIFrameBytesOut.setStatus(_B)
if mibBuilder.loadTexts:cipTgLlcStatsIFrameBytesOut.setUnits(_F)
_CipTgLlcStatsHCIFrameBytesOut_Type=Counter64
_CipTgLlcStatsHCIFrameBytesOut_Object=MibTableColumn
cipTgLlcStatsHCIFrameBytesOut=_CipTgLlcStatsHCIFrameBytesOut_Object((1,3,6,1,4,1,9,9,73,1,1,3,1,6),_CipTgLlcStatsHCIFrameBytesOut_Type())
cipTgLlcStatsHCIFrameBytesOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgLlcStatsHCIFrameBytesOut.setStatus(_B)
_CipTgLlcStatsUIFramesIn_Type=Counter32
_CipTgLlcStatsUIFramesIn_Object=MibTableColumn
cipTgLlcStatsUIFramesIn=_CipTgLlcStatsUIFramesIn_Object((1,3,6,1,4,1,9,9,73,1,1,3,1,7),_CipTgLlcStatsUIFramesIn_Type())
cipTgLlcStatsUIFramesIn.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgLlcStatsUIFramesIn.setStatus(_B)
_CipTgLlcStatsUIFrameBytesIn_Type=Counter32
_CipTgLlcStatsUIFrameBytesIn_Object=MibTableColumn
cipTgLlcStatsUIFrameBytesIn=_CipTgLlcStatsUIFrameBytesIn_Object((1,3,6,1,4,1,9,9,73,1,1,3,1,8),_CipTgLlcStatsUIFrameBytesIn_Type())
cipTgLlcStatsUIFrameBytesIn.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgLlcStatsUIFrameBytesIn.setStatus(_B)
if mibBuilder.loadTexts:cipTgLlcStatsUIFrameBytesIn.setUnits(_F)
_CipTgLlcStatsHCUIFrameBytesIn_Type=Counter64
_CipTgLlcStatsHCUIFrameBytesIn_Object=MibTableColumn
cipTgLlcStatsHCUIFrameBytesIn=_CipTgLlcStatsHCUIFrameBytesIn_Object((1,3,6,1,4,1,9,9,73,1,1,3,1,9),_CipTgLlcStatsHCUIFrameBytesIn_Type())
cipTgLlcStatsHCUIFrameBytesIn.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgLlcStatsHCUIFrameBytesIn.setStatus(_B)
_CipTgLlcStatsUIFramesOut_Type=Counter32
_CipTgLlcStatsUIFramesOut_Object=MibTableColumn
cipTgLlcStatsUIFramesOut=_CipTgLlcStatsUIFramesOut_Object((1,3,6,1,4,1,9,9,73,1,1,3,1,10),_CipTgLlcStatsUIFramesOut_Type())
cipTgLlcStatsUIFramesOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgLlcStatsUIFramesOut.setStatus(_B)
_CipTgLlcStatsUIFrameBytesOut_Type=Counter32
_CipTgLlcStatsUIFrameBytesOut_Object=MibTableColumn
cipTgLlcStatsUIFrameBytesOut=_CipTgLlcStatsUIFrameBytesOut_Object((1,3,6,1,4,1,9,9,73,1,1,3,1,11),_CipTgLlcStatsUIFrameBytesOut_Type())
cipTgLlcStatsUIFrameBytesOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgLlcStatsUIFrameBytesOut.setStatus(_B)
if mibBuilder.loadTexts:cipTgLlcStatsUIFrameBytesOut.setUnits(_F)
_CipTgLlcStatsHCUIFrameBytesOut_Type=Counter64
_CipTgLlcStatsHCUIFrameBytesOut_Object=MibTableColumn
cipTgLlcStatsHCUIFrameBytesOut=_CipTgLlcStatsHCUIFrameBytesOut_Object((1,3,6,1,4,1,9,9,73,1,1,3,1,12),_CipTgLlcStatsHCUIFrameBytesOut_Type())
cipTgLlcStatsHCUIFrameBytesOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgLlcStatsHCUIFrameBytesOut.setStatus(_B)
_CipTgLlcStatsTestCmdsOut_Type=Counter32
_CipTgLlcStatsTestCmdsOut_Object=MibTableColumn
cipTgLlcStatsTestCmdsOut=_CipTgLlcStatsTestCmdsOut_Object((1,3,6,1,4,1,9,9,73,1,1,3,1,13),_CipTgLlcStatsTestCmdsOut_Type())
cipTgLlcStatsTestCmdsOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgLlcStatsTestCmdsOut.setStatus(_B)
_CipTgLlcStatsTestRspsIn_Type=Counter32
_CipTgLlcStatsTestRspsIn_Object=MibTableColumn
cipTgLlcStatsTestRspsIn=_CipTgLlcStatsTestRspsIn_Object((1,3,6,1,4,1,9,9,73,1,1,3,1,14),_CipTgLlcStatsTestRspsIn_Type())
cipTgLlcStatsTestRspsIn.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgLlcStatsTestRspsIn.setStatus(_B)
_CipTgLlcStatsXidCmdsIn_Type=Counter32
_CipTgLlcStatsXidCmdsIn_Object=MibTableColumn
cipTgLlcStatsXidCmdsIn=_CipTgLlcStatsXidCmdsIn_Object((1,3,6,1,4,1,9,9,73,1,1,3,1,15),_CipTgLlcStatsXidCmdsIn_Type())
cipTgLlcStatsXidCmdsIn.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgLlcStatsXidCmdsIn.setStatus(_B)
_CipTgLlcStatsXidCmdsOut_Type=Counter32
_CipTgLlcStatsXidCmdsOut_Object=MibTableColumn
cipTgLlcStatsXidCmdsOut=_CipTgLlcStatsXidCmdsOut_Object((1,3,6,1,4,1,9,9,73,1,1,3,1,16),_CipTgLlcStatsXidCmdsOut_Type())
cipTgLlcStatsXidCmdsOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgLlcStatsXidCmdsOut.setStatus(_B)
_CipTgLlcStatsXidRspsIn_Type=Counter32
_CipTgLlcStatsXidRspsIn_Object=MibTableColumn
cipTgLlcStatsXidRspsIn=_CipTgLlcStatsXidRspsIn_Object((1,3,6,1,4,1,9,9,73,1,1,3,1,17),_CipTgLlcStatsXidRspsIn_Type())
cipTgLlcStatsXidRspsIn.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgLlcStatsXidRspsIn.setStatus(_B)
_CipTgLlcStatsXidRspsOut_Type=Counter32
_CipTgLlcStatsXidRspsOut_Object=MibTableColumn
cipTgLlcStatsXidRspsOut=_CipTgLlcStatsXidRspsOut_Object((1,3,6,1,4,1,9,9,73,1,1,3,1,18),_CipTgLlcStatsXidRspsOut_Type())
cipTgLlcStatsXidRspsOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgLlcStatsXidRspsOut.setStatus(_B)
_CipTgLlcStatsConnNumberRecv_Type=Counter32
_CipTgLlcStatsConnNumberRecv_Object=MibTableColumn
cipTgLlcStatsConnNumberRecv=_CipTgLlcStatsConnNumberRecv_Object((1,3,6,1,4,1,9,9,73,1,1,3,1,19),_CipTgLlcStatsConnNumberRecv_Type())
cipTgLlcStatsConnNumberRecv.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgLlcStatsConnNumberRecv.setStatus(_B)
_CipTgLlcStatsConnNumberSent_Type=Counter32
_CipTgLlcStatsConnNumberSent_Object=MibTableColumn
cipTgLlcStatsConnNumberSent=_CipTgLlcStatsConnNumberSent_Object((1,3,6,1,4,1,9,9,73,1,1,3,1,20),_CipTgLlcStatsConnNumberSent_Type())
cipTgLlcStatsConnNumberSent.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgLlcStatsConnNumberSent.setStatus(_B)
_CipTgIp_ObjectIdentity=ObjectIdentity
cipTgIp=_CipTgIp_ObjectIdentity((1,3,6,1,4,1,9,9,73,1,2))
_CipTgIpAdminTable_Object=MibTable
cipTgIpAdminTable=_CipTgIpAdminTable_Object((1,3,6,1,4,1,9,9,73,1,2,1))
if mibBuilder.loadTexts:cipTgIpAdminTable.setStatus(_B)
_CipTgIpAdminEntry_Object=MibTableRow
cipTgIpAdminEntry=_CipTgIpAdminEntry_Object((1,3,6,1,4,1,9,9,73,1,2,1,1))
cipTgIpAdminEntry.setIndexNames((0,_I,_J),(0,_A,_z))
if mibBuilder.loadTexts:cipTgIpAdminEntry.setStatus(_B)
_CipTgIpAdminName_Type=ChannelTgName
_CipTgIpAdminName_Object=MibTableColumn
cipTgIpAdminName=_CipTgIpAdminName_Object((1,3,6,1,4,1,9,9,73,1,2,1,1,1),_CipTgIpAdminName_Type())
cipTgIpAdminName.setMaxAccess(_L)
if mibBuilder.loadTexts:cipTgIpAdminName.setStatus(_B)
class _CipTgIpAdminType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tcpIp',1),('hsas',2)))
_CipTgIpAdminType_Type.__name__=_D
_CipTgIpAdminType_Object=MibTableColumn
cipTgIpAdminType=_CipTgIpAdminType_Object((1,3,6,1,4,1,9,9,73,1,2,1,1,2),_CipTgIpAdminType_Type())
cipTgIpAdminType.setMaxAccess(_E)
if mibBuilder.loadTexts:cipTgIpAdminType.setStatus(_B)
_CipTgIpAdminRemoteIpAddr_Type=IpAddress
_CipTgIpAdminRemoteIpAddr_Object=MibTableColumn
cipTgIpAdminRemoteIpAddr=_CipTgIpAdminRemoteIpAddr_Object((1,3,6,1,4,1,9,9,73,1,2,1,1,3),_CipTgIpAdminRemoteIpAddr_Type())
cipTgIpAdminRemoteIpAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:cipTgIpAdminRemoteIpAddr.setStatus(_B)
_CipTgIpAdminLocalIpAddr_Type=IpAddress
_CipTgIpAdminLocalIpAddr_Object=MibTableColumn
cipTgIpAdminLocalIpAddr=_CipTgIpAdminLocalIpAddr_Object((1,3,6,1,4,1,9,9,73,1,2,1,1,4),_CipTgIpAdminLocalIpAddr_Type())
cipTgIpAdminLocalIpAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:cipTgIpAdminLocalIpAddr.setStatus(_B)
_CipTgIpAdminBroadcast_Type=TruthValue
_CipTgIpAdminBroadcast_Object=MibTableColumn
cipTgIpAdminBroadcast=_CipTgIpAdminBroadcast_Object((1,3,6,1,4,1,9,9,73,1,2,1,1,5),_CipTgIpAdminBroadcast_Type())
cipTgIpAdminBroadcast.setMaxAccess(_E)
if mibBuilder.loadTexts:cipTgIpAdminBroadcast.setStatus(_B)
_CipTgIpAdminRowStatus_Type=RowStatus
_CipTgIpAdminRowStatus_Object=MibTableColumn
cipTgIpAdminRowStatus=_CipTgIpAdminRowStatus_Object((1,3,6,1,4,1,9,9,73,1,2,1,1,6),_CipTgIpAdminRowStatus_Type())
cipTgIpAdminRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cipTgIpAdminRowStatus.setStatus(_B)
_CipTgIpOperTable_Object=MibTable
cipTgIpOperTable=_CipTgIpOperTable_Object((1,3,6,1,4,1,9,9,73,1,2,2))
if mibBuilder.loadTexts:cipTgIpOperTable.setStatus(_B)
_CipTgIpOperEntry_Object=MibTableRow
cipTgIpOperEntry=_CipTgIpOperEntry_Object((1,3,6,1,4,1,9,9,73,1,2,2,1))
if mibBuilder.loadTexts:cipTgIpOperEntry.setStatus(_B)
_CipTgIpOperLocalVcToken_Type=ChannelTgToken
_CipTgIpOperLocalVcToken_Object=MibTableColumn
cipTgIpOperLocalVcToken=_CipTgIpOperLocalVcToken_Object((1,3,6,1,4,1,9,9,73,1,2,2,1,1),_CipTgIpOperLocalVcToken_Type())
cipTgIpOperLocalVcToken.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgIpOperLocalVcToken.setStatus(_B)
_CipTgIpOperRemoteVcToken_Type=ChannelTgToken
_CipTgIpOperRemoteVcToken_Object=MibTableColumn
cipTgIpOperRemoteVcToken=_CipTgIpOperRemoteVcToken_Object((1,3,6,1,4,1,9,9,73,1,2,2,1,2),_CipTgIpOperRemoteVcToken_Type())
cipTgIpOperRemoteVcToken.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgIpOperRemoteVcToken.setStatus(_B)
_CipTgIpOperLocalConnToken_Type=ChannelTgToken
_CipTgIpOperLocalConnToken_Object=MibTableColumn
cipTgIpOperLocalConnToken=_CipTgIpOperLocalConnToken_Object((1,3,6,1,4,1,9,9,73,1,2,2,1,3),_CipTgIpOperLocalConnToken_Type())
cipTgIpOperLocalConnToken.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgIpOperLocalConnToken.setStatus(_B)
_CipTgIpOperRemoteConnToken_Type=ChannelTgToken
_CipTgIpOperRemoteConnToken_Object=MibTableColumn
cipTgIpOperRemoteConnToken=_CipTgIpOperRemoteConnToken_Object((1,3,6,1,4,1,9,9,73,1,2,2,1,4),_CipTgIpOperRemoteConnToken_Type())
cipTgIpOperRemoteConnToken.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgIpOperRemoteConnToken.setStatus(_B)
class _CipTgIpOperVcStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_CipTgIpOperVcStatus_Type.__name__=_D
_CipTgIpOperVcStatus_Object=MibTableColumn
cipTgIpOperVcStatus=_CipTgIpOperVcStatus_Object((1,3,6,1,4,1,9,9,73,1,2,2,1,5),_CipTgIpOperVcStatus_Type())
cipTgIpOperVcStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgIpOperVcStatus.setStatus(_B)
class _CipTgIpOperConnStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_x,2),(_y,3),(_H,4)))
_CipTgIpOperConnStatus_Type.__name__=_D
_CipTgIpOperConnStatus_Object=MibTableColumn
cipTgIpOperConnStatus=_CipTgIpOperConnStatus_Object((1,3,6,1,4,1,9,9,73,1,2,2,1,6),_CipTgIpOperConnStatus_Type())
cipTgIpOperConnStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgIpOperConnStatus.setStatus(_B)
_CipTgIpStatsTable_Object=MibTable
cipTgIpStatsTable=_CipTgIpStatsTable_Object((1,3,6,1,4,1,9,9,73,1,2,3))
if mibBuilder.loadTexts:cipTgIpStatsTable.setStatus(_B)
_CipTgIpStatsEntry_Object=MibTableRow
cipTgIpStatsEntry=_CipTgIpStatsEntry_Object((1,3,6,1,4,1,9,9,73,1,2,3,1))
if mibBuilder.loadTexts:cipTgIpStatsEntry.setStatus(_B)
_CipTgIpStatsPacketsIn_Type=Counter32
_CipTgIpStatsPacketsIn_Object=MibTableColumn
cipTgIpStatsPacketsIn=_CipTgIpStatsPacketsIn_Object((1,3,6,1,4,1,9,9,73,1,2,3,1,1),_CipTgIpStatsPacketsIn_Type())
cipTgIpStatsPacketsIn.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgIpStatsPacketsIn.setStatus(_B)
_CipTgIpStatsBytesIn_Type=Counter32
_CipTgIpStatsBytesIn_Object=MibTableColumn
cipTgIpStatsBytesIn=_CipTgIpStatsBytesIn_Object((1,3,6,1,4,1,9,9,73,1,2,3,1,2),_CipTgIpStatsBytesIn_Type())
cipTgIpStatsBytesIn.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgIpStatsBytesIn.setStatus(_B)
if mibBuilder.loadTexts:cipTgIpStatsBytesIn.setUnits(_F)
_CipTgIpStatsHCBytesIn_Type=Counter64
_CipTgIpStatsHCBytesIn_Object=MibTableColumn
cipTgIpStatsHCBytesIn=_CipTgIpStatsHCBytesIn_Object((1,3,6,1,4,1,9,9,73,1,2,3,1,3),_CipTgIpStatsHCBytesIn_Type())
cipTgIpStatsHCBytesIn.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgIpStatsHCBytesIn.setStatus(_B)
if mibBuilder.loadTexts:cipTgIpStatsHCBytesIn.setUnits(_F)
_CipTgIpStatsPacketsOut_Type=Counter32
_CipTgIpStatsPacketsOut_Object=MibTableColumn
cipTgIpStatsPacketsOut=_CipTgIpStatsPacketsOut_Object((1,3,6,1,4,1,9,9,73,1,2,3,1,4),_CipTgIpStatsPacketsOut_Type())
cipTgIpStatsPacketsOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgIpStatsPacketsOut.setStatus(_B)
_CipTgIpStatsBytesOut_Type=Counter32
_CipTgIpStatsBytesOut_Object=MibTableColumn
cipTgIpStatsBytesOut=_CipTgIpStatsBytesOut_Object((1,3,6,1,4,1,9,9,73,1,2,3,1,5),_CipTgIpStatsBytesOut_Type())
cipTgIpStatsBytesOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgIpStatsBytesOut.setStatus(_B)
if mibBuilder.loadTexts:cipTgIpStatsBytesOut.setUnits(_F)
_CipTgIpStatsHCBytesOut_Type=Counter64
_CipTgIpStatsHCBytesOut_Object=MibTableColumn
cipTgIpStatsHCBytesOut=_CipTgIpStatsHCBytesOut_Object((1,3,6,1,4,1,9,9,73,1,2,3,1,6),_CipTgIpStatsHCBytesOut_Type())
cipTgIpStatsHCBytesOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgIpStatsHCBytesOut.setStatus(_B)
if mibBuilder.loadTexts:cipTgIpStatsHCBytesOut.setUnits(_F)
_CipTgCmgr_ObjectIdentity=ObjectIdentity
cipTgCmgr=_CipTgCmgr_ObjectIdentity((1,3,6,1,4,1,9,9,73,1,3))
_CipTgCmgrOperTable_Object=MibTable
cipTgCmgrOperTable=_CipTgCmgrOperTable_Object((1,3,6,1,4,1,9,9,73,1,3,1))
if mibBuilder.loadTexts:cipTgCmgrOperTable.setStatus(_B)
_CipTgCmgrOperEntry_Object=MibTableRow
cipTgCmgrOperEntry=_CipTgCmgrOperEntry_Object((1,3,6,1,4,1,9,9,73,1,3,1,1))
cipTgCmgrOperEntry.setIndexNames((0,_I,_J),(0,_A,_A0))
if mibBuilder.loadTexts:cipTgCmgrOperEntry.setStatus(_B)
_CipTgCmgrOperName_Type=ChannelTgName
_CipTgCmgrOperName_Object=MibTableColumn
cipTgCmgrOperName=_CipTgCmgrOperName_Object((1,3,6,1,4,1,9,9,73,1,3,1,1,1),_CipTgCmgrOperName_Type())
cipTgCmgrOperName.setMaxAccess(_L)
if mibBuilder.loadTexts:cipTgCmgrOperName.setStatus(_B)
class _CipTgCmgrOperType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pointToPoint',1),('pointToMultiPoint',2)))
_CipTgCmgrOperType_Type.__name__=_D
_CipTgCmgrOperType_Object=MibTableColumn
cipTgCmgrOperType=_CipTgCmgrOperType_Object((1,3,6,1,4,1,9,9,73,1,3,1,1,2),_CipTgCmgrOperType_Type())
cipTgCmgrOperType.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgCmgrOperType.setStatus(_B)
_CipTgCmgrOperLocalGrToken_Type=ChannelTgToken
_CipTgCmgrOperLocalGrToken_Object=MibTableColumn
cipTgCmgrOperLocalGrToken=_CipTgCmgrOperLocalGrToken_Object((1,3,6,1,4,1,9,9,73,1,3,1,1,3),_CipTgCmgrOperLocalGrToken_Type())
cipTgCmgrOperLocalGrToken.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgCmgrOperLocalGrToken.setStatus(_B)
_CipTgCmgrOperRemoteGrToken_Type=ChannelTgToken
_CipTgCmgrOperRemoteGrToken_Object=MibTableColumn
cipTgCmgrOperRemoteGrToken=_CipTgCmgrOperRemoteGrToken_Object((1,3,6,1,4,1,9,9,73,1,3,1,1,4),_CipTgCmgrOperRemoteGrToken_Type())
cipTgCmgrOperRemoteGrToken.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgCmgrOperRemoteGrToken.setStatus(_B)
_CipTgCmgrOperLocalVcToken_Type=ChannelTgToken
_CipTgCmgrOperLocalVcToken_Object=MibTableColumn
cipTgCmgrOperLocalVcToken=_CipTgCmgrOperLocalVcToken_Object((1,3,6,1,4,1,9,9,73,1,3,1,1,5),_CipTgCmgrOperLocalVcToken_Type())
cipTgCmgrOperLocalVcToken.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgCmgrOperLocalVcToken.setStatus(_B)
_CipTgCmgrOperRemoteVcToken_Type=ChannelTgToken
_CipTgCmgrOperRemoteVcToken_Object=MibTableColumn
cipTgCmgrOperRemoteVcToken=_CipTgCmgrOperRemoteVcToken_Object((1,3,6,1,4,1,9,9,73,1,3,1,1,6),_CipTgCmgrOperRemoteVcToken_Type())
cipTgCmgrOperRemoteVcToken.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgCmgrOperRemoteVcToken.setStatus(_B)
_CipTgCmgrOperLocalConnToken_Type=ChannelTgToken
_CipTgCmgrOperLocalConnToken_Object=MibTableColumn
cipTgCmgrOperLocalConnToken=_CipTgCmgrOperLocalConnToken_Object((1,3,6,1,4,1,9,9,73,1,3,1,1,7),_CipTgCmgrOperLocalConnToken_Type())
cipTgCmgrOperLocalConnToken.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgCmgrOperLocalConnToken.setStatus(_B)
_CipTgCmgrOperRemoteConnToken_Type=ChannelTgToken
_CipTgCmgrOperRemoteConnToken_Object=MibTableColumn
cipTgCmgrOperRemoteConnToken=_CipTgCmgrOperRemoteConnToken_Object((1,3,6,1,4,1,9,9,73,1,3,1,1,8),_CipTgCmgrOperRemoteConnToken_Type())
cipTgCmgrOperRemoteConnToken.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgCmgrOperRemoteConnToken.setStatus(_B)
class _CipTgCmgrOperVcStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_CipTgCmgrOperVcStatus_Type.__name__=_D
_CipTgCmgrOperVcStatus_Object=MibTableColumn
cipTgCmgrOperVcStatus=_CipTgCmgrOperVcStatus_Object((1,3,6,1,4,1,9,9,73,1,3,1,1,9),_CipTgCmgrOperVcStatus_Type())
cipTgCmgrOperVcStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgCmgrOperVcStatus.setStatus(_B)
class _CipTgCmgrOperConnStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_CipTgCmgrOperConnStatus_Type.__name__=_D
_CipTgCmgrOperConnStatus_Object=MibTableColumn
cipTgCmgrOperConnStatus=_CipTgCmgrOperConnStatus_Object((1,3,6,1,4,1,9,9,73,1,3,1,1,10),_CipTgCmgrOperConnStatus_Type())
cipTgCmgrOperConnStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cipTgCmgrOperConnStatus.setStatus(_B)
_CiscoCipTgMibConformance_ObjectIdentity=ObjectIdentity
ciscoCipTgMibConformance=_CiscoCipTgMibConformance_ObjectIdentity((1,3,6,1,4,1,9,9,73,3))
_CiscoCipTgMibCompliances_ObjectIdentity=ObjectIdentity
ciscoCipTgMibCompliances=_CiscoCipTgMibCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,73,3,1))
_CiscoCipTgMibGroups_ObjectIdentity=ObjectIdentity
ciscoCipTgMibGroups=_CiscoCipTgMibGroups_ObjectIdentity((1,3,6,1,4,1,9,9,73,3,2))
cipTgLlcAdminEntry.registerAugmentions((_A,_A1))
cipTgLlcOperEntry.setIndexNames(*cipTgLlcAdminEntry.getIndexNames())
cipTgLlcAdminEntry.registerAugmentions((_A,_A2))
cipTgLlcStatsEntry.setIndexNames(*cipTgLlcAdminEntry.getIndexNames())
cipTgIpAdminEntry.registerAugmentions((_A,_A3))
cipTgIpOperEntry.setIndexNames(*cipTgIpAdminEntry.getIndexNames())
cipTgIpAdminEntry.registerAugmentions((_A,_A4))
cipTgIpStatsEntry.setIndexNames(*cipTgIpAdminEntry.getIndexNames())
ciscoCipTgLlcGroup=ObjectGroup((1,3,6,1,4,1,9,9,73,3,2,2))
ciscoCipTgLlcGroup.setObjects(*((_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t)))
if mibBuilder.loadTexts:ciscoCipTgLlcGroup.setStatus('obsolete')
ciscoCipTgLlcGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,73,3,2,3))
ciscoCipTgLlcGroupRev1.setObjects(*((_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_AB),(_A,_AC)))
if mibBuilder.loadTexts:ciscoCipTgLlcGroupRev1.setStatus(_B)
ciscoCipTgIpGroup=ObjectGroup((1,3,6,1,4,1,9,9,73,3,2,4))
ciscoCipTgIpGroup.setObjects(*((_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT)))
if mibBuilder.loadTexts:ciscoCipTgIpGroup.setStatus(_B)
ciscoCipTgCmgrGroup=ObjectGroup((1,3,6,1,4,1,9,9,73,3,2,5))
ciscoCipTgCmgrGroup.setObjects(*((_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac)))
if mibBuilder.loadTexts:ciscoCipTgCmgrGroup.setStatus(_B)
ciscoCipTgMibCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,73,3,1,1))
ciscoCipTgMibCompliance.setObjects((_A,_Ad))
if mibBuilder.loadTexts:ciscoCipTgMibCompliance.setStatus('obsolete')
ciscoCipTgMibComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,73,3,1,2))
ciscoCipTgMibComplianceRev1.setObjects(*((_A,_Ae),(_A,_Af),(_A,_Ag)))
if mibBuilder.loadTexts:ciscoCipTgMibComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ChannelTgName':ChannelTgName,'ChannelTgToken':ChannelTgToken,'ciscoCipTgMIB':ciscoCipTgMIB,'cipTgObjects':cipTgObjects,'cipTgLlc':cipTgLlc,'cipTgLlcAdminTable':cipTgLlcAdminTable,'cipTgLlcAdminEntry':cipTgLlcAdminEntry,_w:cipTgLlcAdminName,_M:cipTgLlcAdminLanType,_N:cipTgLlcAdminAdaptNo,_O:cipTgLlcAdminLSAP,_P:cipTgLlcAdminRMAC,_Q:cipTgLlcAdminRSAP,_R:cipTgLlcAdminRowStatus,'cipTgLlcOperTable':cipTgLlcOperTable,_A1:cipTgLlcOperEntry,_S:cipTgLlcOperState,_T:cipTgLlcOperTGN,_U:cipTgLlcOperLocalCP,_V:cipTgLlcOperRemoteCP,_W:cipTgLlcOperMaxIn,_X:cipTgLlcOperMaxOut,_Y:cipTgLlcOperHpr,_Z:cipTgLlcOperHprLSAP,_a:cipTgLlcOperHprRSAP,_b:cipTgLlcOperRIF,_A5:cipTgLlcOperLocalVcToken,_A6:cipTgLlcOperRemoteVcToken,_A7:cipTgLlcOperLocalConnToken,_A8:cipTgLlcOperRemoteConnToken,_A9:cipTgLlcOperVcStatus,_AA:cipTgLlcOperConnStatus,'cipTgLlcStatsTable':cipTgLlcStatsTable,_A2:cipTgLlcStatsEntry,_c:cipTgLlcStatsIFramesIn,_d:cipTgLlcStatsIFrameBytesIn,_e:cipTgLlcStatsHCIFrameBytesIn,_f:cipTgLlcStatsIFramesOut,_g:cipTgLlcStatsIFrameBytesOut,_h:cipTgLlcStatsHCIFrameBytesOut,_i:cipTgLlcStatsUIFramesIn,_j:cipTgLlcStatsUIFrameBytesIn,_k:cipTgLlcStatsHCUIFrameBytesIn,_l:cipTgLlcStatsUIFramesOut,_m:cipTgLlcStatsUIFrameBytesOut,_n:cipTgLlcStatsHCUIFrameBytesOut,_o:cipTgLlcStatsTestCmdsOut,_p:cipTgLlcStatsTestRspsIn,_q:cipTgLlcStatsXidCmdsIn,_r:cipTgLlcStatsXidCmdsOut,_s:cipTgLlcStatsXidRspsIn,_t:cipTgLlcStatsXidRspsOut,_AB:cipTgLlcStatsConnNumberRecv,_AC:cipTgLlcStatsConnNumberSent,'cipTgIp':cipTgIp,'cipTgIpAdminTable':cipTgIpAdminTable,'cipTgIpAdminEntry':cipTgIpAdminEntry,_z:cipTgIpAdminName,_AD:cipTgIpAdminType,_AE:cipTgIpAdminRemoteIpAddr,_AF:cipTgIpAdminLocalIpAddr,_AG:cipTgIpAdminBroadcast,_AH:cipTgIpAdminRowStatus,'cipTgIpOperTable':cipTgIpOperTable,_A3:cipTgIpOperEntry,_AI:cipTgIpOperLocalVcToken,_AJ:cipTgIpOperRemoteVcToken,_AK:cipTgIpOperLocalConnToken,_AL:cipTgIpOperRemoteConnToken,_AM:cipTgIpOperVcStatus,_AN:cipTgIpOperConnStatus,'cipTgIpStatsTable':cipTgIpStatsTable,_A4:cipTgIpStatsEntry,_AO:cipTgIpStatsPacketsIn,_AP:cipTgIpStatsBytesIn,_AQ:cipTgIpStatsHCBytesIn,_AR:cipTgIpStatsPacketsOut,_AS:cipTgIpStatsBytesOut,_AT:cipTgIpStatsHCBytesOut,'cipTgCmgr':cipTgCmgr,'cipTgCmgrOperTable':cipTgCmgrOperTable,'cipTgCmgrOperEntry':cipTgCmgrOperEntry,_A0:cipTgCmgrOperName,_AU:cipTgCmgrOperType,_AV:cipTgCmgrOperLocalGrToken,_AW:cipTgCmgrOperRemoteGrToken,_AX:cipTgCmgrOperLocalVcToken,_AY:cipTgCmgrOperRemoteVcToken,_AZ:cipTgCmgrOperLocalConnToken,_Aa:cipTgCmgrOperRemoteConnToken,_Ab:cipTgCmgrOperVcStatus,_Ac:cipTgCmgrOperConnStatus,'ciscoCipTgMibConformance':ciscoCipTgMibConformance,'ciscoCipTgMibCompliances':ciscoCipTgMibCompliances,'ciscoCipTgMibCompliance':ciscoCipTgMibCompliance,'ciscoCipTgMibComplianceRev1':ciscoCipTgMibComplianceRev1,'ciscoCipTgMibGroups':ciscoCipTgMibGroups,_Ad:ciscoCipTgLlcGroup,_Ae:ciscoCipTgLlcGroupRev1,_Af:ciscoCipTgIpGroup,_Ag:ciscoCipTgCmgrGroup})