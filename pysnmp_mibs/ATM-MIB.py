_Ay='atmTrafficDescrGroup2'
_Ax='atmInterfaceConfGroup2'
_Aw='atmTrafficDescrGroup'
_Av='atmInterfaceConfGroup'
_Au='atmTrafficDescrParamIndexNext'
_At='atmTrafficFrameDiscard'
_As='atmServiceCategory'
_Ar='atmInterfaceSubscrAddress'
_Aq='atmInterfaceCurrentMaxVciBits'
_Ap='atmInterfaceCurrentMaxVpiBits'
_Ao='aal5VccOverSizedSDUs'
_An='aal5VccSarTimeOuts'
_Am='aal5VccCrcErrors'
_Al='atmVccAal5EncapsType'
_Ak='atmVccAal5CpcsReceiveSduSize'
_Aj='atmVccAal5CpcsTransmitSduSize'
_Ai='atmInterfaceTCAlarmState'
_Ah='atmInterfaceOCDEvents'
_Ag='atmInterfaceDs3PlcpUASs'
_Af='atmInterfaceDs3PlcpAlarmState'
_Ae='atmInterfaceDs3PlcpSEFSs'
_Ad='atmTrafficQoSClass'
_Ac='atmInterfaceAdminAddress'
_Ab='atmInterfaceAddressType'
_Aa='aal5VccVci'
_AZ='aal5VccVpi'
_AY='atmVcCrossConnectHighVci'
_AX='atmVcCrossConnectHighVpi'
_AW='atmVcCrossConnectHighIfIndex'
_AV='atmVcCrossConnectLowVci'
_AU='atmVcCrossConnectLowVpi'
_AT='atmVcCrossConnectLowIfIndex'
_AS='atmVcCrossConnectIndex'
_AR='atmVpCrossConnectHighVpi'
_AQ='atmVpCrossConnectHighIfIndex'
_AP='atmVpCrossConnectLowVpi'
_AO='atmVpCrossConnectLowIfIndex'
_AN='atmVpCrossConnectIndex'
_AM='atmVclVci'
_AL='atmVclVpi'
_AK='atmVplVpi'
_AJ='atmTrafficDescrParamIndex'
_AI='TruthValue'
_AH='AtmVpIdentifier'
_AG='AtmVcIdentifier'
_AF='AtmServiceCategory'
_AE='ObjectIdentifier'
_AD='atmVclConnKind'
_AC='atmVclCastType'
_AB='atmVplConnKind'
_AA='atmVplCastType'
_A9='atmVcCrossConnectIndexNext'
_A8='atmVclCrossConnectIdentifier'
_A7='atmVcCrossConnectRowStatus'
_A6='atmVcCrossConnectH2LLastChange'
_A5='atmVcCrossConnectL2HLastChange'
_A4='atmVcCrossConnectH2LOperStatus'
_A3='atmVcCrossConnectL2HOperStatus'
_A2='atmVcCrossConnectAdminStatus'
_A1='atmVpCrossConnectIndexNext'
_A0='atmVplCrossConnectIdentifier'
_z='atmVpCrossConnectRowStatus'
_y='atmVpCrossConnectH2LLastChange'
_x='atmVpCrossConnectL2HLastChange'
_w='atmVpCrossConnectH2LOperStatus'
_v='atmVpCrossConnectL2HOperStatus'
_u='atmVpCrossConnectAdminStatus'
_t='atmVccAalType'
_s='atmVclAdminStatus'
_r='atmVplAdminStatus'
_q='atmTrafficDescrRowStatus'
_p='atmTrafficDescrParam5'
_o='atmTrafficDescrParam4'
_n='atmTrafficDescrParam3'
_m='atmTrafficDescrParam2'
_l='atmTrafficDescrParam1'
_k='atmTrafficDescrType'
_j='atmInterfaceMyNeighborIfName'
_i='atmInterfaceMyNeighborIpAddress'
_h='atmInterfaceIlmiVci'
_g='atmInterfaceIlmiVpi'
_f='atmInterfaceMaxActiveVciBits'
_e='atmInterfaceMaxActiveVpiBits'
_d='atmInterfaceConfVccs'
_c='atmInterfaceConfVpcs'
_b='atmInterfaceMaxVccs'
_a='atmInterfaceMaxVpcs'
_Z='other'
_Y='AtmConnKind'
_X='AtmConnCastType'
_W='atmVclLastChange'
_V='atmVplLastChange'
_U='atmVclRowStatus'
_T='atmVclTransmitTrafficDescrIndex'
_S='atmVclReceiveTrafficDescrIndex'
_R='atmVclOperStatus'
_Q='atmVplRowStatus'
_P='atmVplTransmitTrafficDescrIndex'
_O='atmVplReceiveTrafficDescrIndex'
_N='atmVplOperStatus'
_M='AtmVorXAdminStatus'
_L='RowStatus'
_K='AtmTrafficDescrParamIndex'
_J='ifIndex'
_I='IF-MIB'
_H='read-write'
_G='deprecated'
_F='not-accessible'
_E='Integer32'
_D='read-create'
_C='read-only'
_B='current'
_A='ATM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString',_AE)
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AtmAddr,AtmConnCastType,AtmConnKind,AtmServiceCategory,AtmTrafficDescrParamIndex,AtmVcIdentifier,AtmVorXAdminStatus,AtmVorXLastChange,AtmVorXOperStatus,AtmVpIdentifier,atmNoClpNoScr=mibBuilder.importSymbols('ATM-TC-MIB','AtmAddr',_X,_Y,_AF,_K,_AG,_M,'AtmVorXLastChange','AtmVorXOperStatus',_AH,'atmNoClpNoScr')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_I,'InterfaceIndex',_J)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress',_L,'TextualConvention',_AI)
atmMIB=ModuleIdentity((1,3,6,1,2,1,37))
if mibBuilder.loadTexts:atmMIB.setRevisions(('1998-10-19 12:00','1994-06-07 22:45'))
_AtmMIBObjects_ObjectIdentity=ObjectIdentity
atmMIBObjects=_AtmMIBObjects_ObjectIdentity((1,3,6,1,2,1,37,1))
_AtmInterfaceConfTable_Object=MibTable
atmInterfaceConfTable=_AtmInterfaceConfTable_Object((1,3,6,1,2,1,37,1,2))
if mibBuilder.loadTexts:atmInterfaceConfTable.setStatus(_B)
_AtmInterfaceConfEntry_Object=MibTableRow
atmInterfaceConfEntry=_AtmInterfaceConfEntry_Object((1,3,6,1,2,1,37,1,2,1))
atmInterfaceConfEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:atmInterfaceConfEntry.setStatus(_B)
class _AtmInterfaceMaxVpcs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4096))
_AtmInterfaceMaxVpcs_Type.__name__=_E
_AtmInterfaceMaxVpcs_Object=MibTableColumn
atmInterfaceMaxVpcs=_AtmInterfaceMaxVpcs_Object((1,3,6,1,2,1,37,1,2,1,1),_AtmInterfaceMaxVpcs_Type())
atmInterfaceMaxVpcs.setMaxAccess(_H)
if mibBuilder.loadTexts:atmInterfaceMaxVpcs.setStatus(_B)
class _AtmInterfaceMaxVccs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_AtmInterfaceMaxVccs_Type.__name__=_E
_AtmInterfaceMaxVccs_Object=MibTableColumn
atmInterfaceMaxVccs=_AtmInterfaceMaxVccs_Object((1,3,6,1,2,1,37,1,2,1,2),_AtmInterfaceMaxVccs_Type())
atmInterfaceMaxVccs.setMaxAccess(_H)
if mibBuilder.loadTexts:atmInterfaceMaxVccs.setStatus(_B)
class _AtmInterfaceConfVpcs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4096))
_AtmInterfaceConfVpcs_Type.__name__=_E
_AtmInterfaceConfVpcs_Object=MibTableColumn
atmInterfaceConfVpcs=_AtmInterfaceConfVpcs_Object((1,3,6,1,2,1,37,1,2,1,3),_AtmInterfaceConfVpcs_Type())
atmInterfaceConfVpcs.setMaxAccess(_C)
if mibBuilder.loadTexts:atmInterfaceConfVpcs.setStatus(_B)
class _AtmInterfaceConfVccs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_AtmInterfaceConfVccs_Type.__name__=_E
_AtmInterfaceConfVccs_Object=MibTableColumn
atmInterfaceConfVccs=_AtmInterfaceConfVccs_Object((1,3,6,1,2,1,37,1,2,1,4),_AtmInterfaceConfVccs_Type())
atmInterfaceConfVccs.setMaxAccess(_C)
if mibBuilder.loadTexts:atmInterfaceConfVccs.setStatus(_B)
class _AtmInterfaceMaxActiveVpiBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_AtmInterfaceMaxActiveVpiBits_Type.__name__=_E
_AtmInterfaceMaxActiveVpiBits_Object=MibTableColumn
atmInterfaceMaxActiveVpiBits=_AtmInterfaceMaxActiveVpiBits_Object((1,3,6,1,2,1,37,1,2,1,5),_AtmInterfaceMaxActiveVpiBits_Type())
atmInterfaceMaxActiveVpiBits.setMaxAccess(_H)
if mibBuilder.loadTexts:atmInterfaceMaxActiveVpiBits.setStatus(_B)
class _AtmInterfaceMaxActiveVciBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_AtmInterfaceMaxActiveVciBits_Type.__name__=_E
_AtmInterfaceMaxActiveVciBits_Object=MibTableColumn
atmInterfaceMaxActiveVciBits=_AtmInterfaceMaxActiveVciBits_Object((1,3,6,1,2,1,37,1,2,1,6),_AtmInterfaceMaxActiveVciBits_Type())
atmInterfaceMaxActiveVciBits.setMaxAccess(_H)
if mibBuilder.loadTexts:atmInterfaceMaxActiveVciBits.setStatus(_B)
class _AtmInterfaceIlmiVpi_Type(AtmVpIdentifier):defaultValue=0
_AtmInterfaceIlmiVpi_Type.__name__=_AH
_AtmInterfaceIlmiVpi_Object=MibTableColumn
atmInterfaceIlmiVpi=_AtmInterfaceIlmiVpi_Object((1,3,6,1,2,1,37,1,2,1,7),_AtmInterfaceIlmiVpi_Type())
atmInterfaceIlmiVpi.setMaxAccess(_H)
if mibBuilder.loadTexts:atmInterfaceIlmiVpi.setStatus(_B)
class _AtmInterfaceIlmiVci_Type(AtmVcIdentifier):defaultValue=16
_AtmInterfaceIlmiVci_Type.__name__=_AG
_AtmInterfaceIlmiVci_Object=MibTableColumn
atmInterfaceIlmiVci=_AtmInterfaceIlmiVci_Object((1,3,6,1,2,1,37,1,2,1,8),_AtmInterfaceIlmiVci_Type())
atmInterfaceIlmiVci.setMaxAccess(_H)
if mibBuilder.loadTexts:atmInterfaceIlmiVci.setStatus(_B)
class _AtmInterfaceAddressType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('private',1),('nsapE164',2),('nativeE164',3),(_Z,4)))
_AtmInterfaceAddressType_Type.__name__=_E
_AtmInterfaceAddressType_Object=MibTableColumn
atmInterfaceAddressType=_AtmInterfaceAddressType_Object((1,3,6,1,2,1,37,1,2,1,9),_AtmInterfaceAddressType_Type())
atmInterfaceAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:atmInterfaceAddressType.setStatus(_G)
_AtmInterfaceAdminAddress_Type=AtmAddr
_AtmInterfaceAdminAddress_Object=MibTableColumn
atmInterfaceAdminAddress=_AtmInterfaceAdminAddress_Object((1,3,6,1,2,1,37,1,2,1,10),_AtmInterfaceAdminAddress_Type())
atmInterfaceAdminAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:atmInterfaceAdminAddress.setStatus(_G)
_AtmInterfaceMyNeighborIpAddress_Type=IpAddress
_AtmInterfaceMyNeighborIpAddress_Object=MibTableColumn
atmInterfaceMyNeighborIpAddress=_AtmInterfaceMyNeighborIpAddress_Object((1,3,6,1,2,1,37,1,2,1,11),_AtmInterfaceMyNeighborIpAddress_Type())
atmInterfaceMyNeighborIpAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:atmInterfaceMyNeighborIpAddress.setStatus(_B)
_AtmInterfaceMyNeighborIfName_Type=DisplayString
_AtmInterfaceMyNeighborIfName_Object=MibTableColumn
atmInterfaceMyNeighborIfName=_AtmInterfaceMyNeighborIfName_Object((1,3,6,1,2,1,37,1,2,1,12),_AtmInterfaceMyNeighborIfName_Type())
atmInterfaceMyNeighborIfName.setMaxAccess(_H)
if mibBuilder.loadTexts:atmInterfaceMyNeighborIfName.setStatus(_B)
class _AtmInterfaceCurrentMaxVpiBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_AtmInterfaceCurrentMaxVpiBits_Type.__name__=_E
_AtmInterfaceCurrentMaxVpiBits_Object=MibTableColumn
atmInterfaceCurrentMaxVpiBits=_AtmInterfaceCurrentMaxVpiBits_Object((1,3,6,1,2,1,37,1,2,1,13),_AtmInterfaceCurrentMaxVpiBits_Type())
atmInterfaceCurrentMaxVpiBits.setMaxAccess(_C)
if mibBuilder.loadTexts:atmInterfaceCurrentMaxVpiBits.setStatus(_B)
class _AtmInterfaceCurrentMaxVciBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_AtmInterfaceCurrentMaxVciBits_Type.__name__=_E
_AtmInterfaceCurrentMaxVciBits_Object=MibTableColumn
atmInterfaceCurrentMaxVciBits=_AtmInterfaceCurrentMaxVciBits_Object((1,3,6,1,2,1,37,1,2,1,14),_AtmInterfaceCurrentMaxVciBits_Type())
atmInterfaceCurrentMaxVciBits.setMaxAccess(_C)
if mibBuilder.loadTexts:atmInterfaceCurrentMaxVciBits.setStatus(_B)
_AtmInterfaceSubscrAddress_Type=AtmAddr
_AtmInterfaceSubscrAddress_Object=MibTableColumn
atmInterfaceSubscrAddress=_AtmInterfaceSubscrAddress_Object((1,3,6,1,2,1,37,1,2,1,15),_AtmInterfaceSubscrAddress_Type())
atmInterfaceSubscrAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:atmInterfaceSubscrAddress.setStatus(_B)
_AtmInterfaceDs3PlcpTable_Object=MibTable
atmInterfaceDs3PlcpTable=_AtmInterfaceDs3PlcpTable_Object((1,3,6,1,2,1,37,1,3))
if mibBuilder.loadTexts:atmInterfaceDs3PlcpTable.setStatus(_B)
_AtmInterfaceDs3PlcpEntry_Object=MibTableRow
atmInterfaceDs3PlcpEntry=_AtmInterfaceDs3PlcpEntry_Object((1,3,6,1,2,1,37,1,3,1))
atmInterfaceDs3PlcpEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:atmInterfaceDs3PlcpEntry.setStatus(_B)
_AtmInterfaceDs3PlcpSEFSs_Type=Counter32
_AtmInterfaceDs3PlcpSEFSs_Object=MibTableColumn
atmInterfaceDs3PlcpSEFSs=_AtmInterfaceDs3PlcpSEFSs_Object((1,3,6,1,2,1,37,1,3,1,1),_AtmInterfaceDs3PlcpSEFSs_Type())
atmInterfaceDs3PlcpSEFSs.setMaxAccess(_C)
if mibBuilder.loadTexts:atmInterfaceDs3PlcpSEFSs.setStatus(_B)
class _AtmInterfaceDs3PlcpAlarmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noAlarm',1),('receivedFarEndAlarm',2),('incomingLOF',3)))
_AtmInterfaceDs3PlcpAlarmState_Type.__name__=_E
_AtmInterfaceDs3PlcpAlarmState_Object=MibTableColumn
atmInterfaceDs3PlcpAlarmState=_AtmInterfaceDs3PlcpAlarmState_Object((1,3,6,1,2,1,37,1,3,1,2),_AtmInterfaceDs3PlcpAlarmState_Type())
atmInterfaceDs3PlcpAlarmState.setMaxAccess(_C)
if mibBuilder.loadTexts:atmInterfaceDs3PlcpAlarmState.setStatus(_B)
_AtmInterfaceDs3PlcpUASs_Type=Counter32
_AtmInterfaceDs3PlcpUASs_Object=MibTableColumn
atmInterfaceDs3PlcpUASs=_AtmInterfaceDs3PlcpUASs_Object((1,3,6,1,2,1,37,1,3,1,3),_AtmInterfaceDs3PlcpUASs_Type())
atmInterfaceDs3PlcpUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:atmInterfaceDs3PlcpUASs.setStatus(_B)
_AtmInterfaceTCTable_Object=MibTable
atmInterfaceTCTable=_AtmInterfaceTCTable_Object((1,3,6,1,2,1,37,1,4))
if mibBuilder.loadTexts:atmInterfaceTCTable.setStatus(_B)
_AtmInterfaceTCEntry_Object=MibTableRow
atmInterfaceTCEntry=_AtmInterfaceTCEntry_Object((1,3,6,1,2,1,37,1,4,1))
atmInterfaceTCEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:atmInterfaceTCEntry.setStatus(_B)
_AtmInterfaceOCDEvents_Type=Counter32
_AtmInterfaceOCDEvents_Object=MibTableColumn
atmInterfaceOCDEvents=_AtmInterfaceOCDEvents_Object((1,3,6,1,2,1,37,1,4,1,1),_AtmInterfaceOCDEvents_Type())
atmInterfaceOCDEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:atmInterfaceOCDEvents.setStatus(_B)
class _AtmInterfaceTCAlarmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noAlarm',1),('lcdFailure',2)))
_AtmInterfaceTCAlarmState_Type.__name__=_E
_AtmInterfaceTCAlarmState_Object=MibTableColumn
atmInterfaceTCAlarmState=_AtmInterfaceTCAlarmState_Object((1,3,6,1,2,1,37,1,4,1,2),_AtmInterfaceTCAlarmState_Type())
atmInterfaceTCAlarmState.setMaxAccess(_C)
if mibBuilder.loadTexts:atmInterfaceTCAlarmState.setStatus(_B)
_AtmTrafficDescrParamTable_Object=MibTable
atmTrafficDescrParamTable=_AtmTrafficDescrParamTable_Object((1,3,6,1,2,1,37,1,5))
if mibBuilder.loadTexts:atmTrafficDescrParamTable.setStatus(_B)
_AtmTrafficDescrParamEntry_Object=MibTableRow
atmTrafficDescrParamEntry=_AtmTrafficDescrParamEntry_Object((1,3,6,1,2,1,37,1,5,1))
atmTrafficDescrParamEntry.setIndexNames((0,_A,_AJ))
if mibBuilder.loadTexts:atmTrafficDescrParamEntry.setStatus(_B)
class _AtmTrafficDescrParamIndex_Type(AtmTrafficDescrParamIndex):subtypeSpec=AtmTrafficDescrParamIndex.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AtmTrafficDescrParamIndex_Type.__name__=_K
_AtmTrafficDescrParamIndex_Object=MibTableColumn
atmTrafficDescrParamIndex=_AtmTrafficDescrParamIndex_Object((1,3,6,1,2,1,37,1,5,1,1),_AtmTrafficDescrParamIndex_Type())
atmTrafficDescrParamIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:atmTrafficDescrParamIndex.setStatus(_B)
class _AtmTrafficDescrType_Type(ObjectIdentifier):defaultValue=1,3,6,1,2,1,37,1,1,2
_AtmTrafficDescrType_Type.__name__=_AE
_AtmTrafficDescrType_Object=MibTableColumn
atmTrafficDescrType=_AtmTrafficDescrType_Object((1,3,6,1,2,1,37,1,5,1,2),_AtmTrafficDescrType_Type())
atmTrafficDescrType.setMaxAccess(_D)
if mibBuilder.loadTexts:atmTrafficDescrType.setStatus(_B)
class _AtmTrafficDescrParam1_Type(Integer32):defaultValue=0
_AtmTrafficDescrParam1_Type.__name__=_E
_AtmTrafficDescrParam1_Object=MibTableColumn
atmTrafficDescrParam1=_AtmTrafficDescrParam1_Object((1,3,6,1,2,1,37,1,5,1,3),_AtmTrafficDescrParam1_Type())
atmTrafficDescrParam1.setMaxAccess(_D)
if mibBuilder.loadTexts:atmTrafficDescrParam1.setStatus(_B)
class _AtmTrafficDescrParam2_Type(Integer32):defaultValue=0
_AtmTrafficDescrParam2_Type.__name__=_E
_AtmTrafficDescrParam2_Object=MibTableColumn
atmTrafficDescrParam2=_AtmTrafficDescrParam2_Object((1,3,6,1,2,1,37,1,5,1,4),_AtmTrafficDescrParam2_Type())
atmTrafficDescrParam2.setMaxAccess(_D)
if mibBuilder.loadTexts:atmTrafficDescrParam2.setStatus(_B)
class _AtmTrafficDescrParam3_Type(Integer32):defaultValue=0
_AtmTrafficDescrParam3_Type.__name__=_E
_AtmTrafficDescrParam3_Object=MibTableColumn
atmTrafficDescrParam3=_AtmTrafficDescrParam3_Object((1,3,6,1,2,1,37,1,5,1,5),_AtmTrafficDescrParam3_Type())
atmTrafficDescrParam3.setMaxAccess(_D)
if mibBuilder.loadTexts:atmTrafficDescrParam3.setStatus(_B)
class _AtmTrafficDescrParam4_Type(Integer32):defaultValue=0
_AtmTrafficDescrParam4_Type.__name__=_E
_AtmTrafficDescrParam4_Object=MibTableColumn
atmTrafficDescrParam4=_AtmTrafficDescrParam4_Object((1,3,6,1,2,1,37,1,5,1,6),_AtmTrafficDescrParam4_Type())
atmTrafficDescrParam4.setMaxAccess(_D)
if mibBuilder.loadTexts:atmTrafficDescrParam4.setStatus(_B)
class _AtmTrafficDescrParam5_Type(Integer32):defaultValue=0
_AtmTrafficDescrParam5_Type.__name__=_E
_AtmTrafficDescrParam5_Object=MibTableColumn
atmTrafficDescrParam5=_AtmTrafficDescrParam5_Object((1,3,6,1,2,1,37,1,5,1,7),_AtmTrafficDescrParam5_Type())
atmTrafficDescrParam5.setMaxAccess(_D)
if mibBuilder.loadTexts:atmTrafficDescrParam5.setStatus(_B)
class _AtmTrafficQoSClass_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AtmTrafficQoSClass_Type.__name__=_E
_AtmTrafficQoSClass_Object=MibTableColumn
atmTrafficQoSClass=_AtmTrafficQoSClass_Object((1,3,6,1,2,1,37,1,5,1,8),_AtmTrafficQoSClass_Type())
atmTrafficQoSClass.setMaxAccess(_D)
if mibBuilder.loadTexts:atmTrafficQoSClass.setStatus(_G)
class _AtmTrafficDescrRowStatus_Type(RowStatus):defaultValue=1
_AtmTrafficDescrRowStatus_Type.__name__=_L
_AtmTrafficDescrRowStatus_Object=MibTableColumn
atmTrafficDescrRowStatus=_AtmTrafficDescrRowStatus_Object((1,3,6,1,2,1,37,1,5,1,9),_AtmTrafficDescrRowStatus_Type())
atmTrafficDescrRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:atmTrafficDescrRowStatus.setStatus(_B)
class _AtmServiceCategory_Type(AtmServiceCategory):defaultValue=6
_AtmServiceCategory_Type.__name__=_AF
_AtmServiceCategory_Object=MibTableColumn
atmServiceCategory=_AtmServiceCategory_Object((1,3,6,1,2,1,37,1,5,1,10),_AtmServiceCategory_Type())
atmServiceCategory.setMaxAccess(_D)
if mibBuilder.loadTexts:atmServiceCategory.setStatus(_B)
class _AtmTrafficFrameDiscard_Type(TruthValue):defaultValue=1
_AtmTrafficFrameDiscard_Type.__name__=_AI
_AtmTrafficFrameDiscard_Object=MibTableColumn
atmTrafficFrameDiscard=_AtmTrafficFrameDiscard_Object((1,3,6,1,2,1,37,1,5,1,11),_AtmTrafficFrameDiscard_Type())
atmTrafficFrameDiscard.setMaxAccess(_D)
if mibBuilder.loadTexts:atmTrafficFrameDiscard.setStatus(_B)
_AtmVplTable_Object=MibTable
atmVplTable=_AtmVplTable_Object((1,3,6,1,2,1,37,1,6))
if mibBuilder.loadTexts:atmVplTable.setStatus(_B)
_AtmVplEntry_Object=MibTableRow
atmVplEntry=_AtmVplEntry_Object((1,3,6,1,2,1,37,1,6,1))
atmVplEntry.setIndexNames((0,_I,_J),(0,_A,_AK))
if mibBuilder.loadTexts:atmVplEntry.setStatus(_B)
_AtmVplVpi_Type=AtmVpIdentifier
_AtmVplVpi_Object=MibTableColumn
atmVplVpi=_AtmVplVpi_Object((1,3,6,1,2,1,37,1,6,1,1),_AtmVplVpi_Type())
atmVplVpi.setMaxAccess(_F)
if mibBuilder.loadTexts:atmVplVpi.setStatus(_B)
class _AtmVplAdminStatus_Type(AtmVorXAdminStatus):defaultValue=2
_AtmVplAdminStatus_Type.__name__=_M
_AtmVplAdminStatus_Object=MibTableColumn
atmVplAdminStatus=_AtmVplAdminStatus_Object((1,3,6,1,2,1,37,1,6,1,2),_AtmVplAdminStatus_Type())
atmVplAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:atmVplAdminStatus.setStatus(_B)
_AtmVplOperStatus_Type=AtmVorXOperStatus
_AtmVplOperStatus_Object=MibTableColumn
atmVplOperStatus=_AtmVplOperStatus_Object((1,3,6,1,2,1,37,1,6,1,3),_AtmVplOperStatus_Type())
atmVplOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:atmVplOperStatus.setStatus(_B)
_AtmVplLastChange_Type=AtmVorXLastChange
_AtmVplLastChange_Object=MibTableColumn
atmVplLastChange=_AtmVplLastChange_Object((1,3,6,1,2,1,37,1,6,1,4),_AtmVplLastChange_Type())
atmVplLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:atmVplLastChange.setStatus(_B)
class _AtmVplReceiveTrafficDescrIndex_Type(AtmTrafficDescrParamIndex):defaultValue=0
_AtmVplReceiveTrafficDescrIndex_Type.__name__=_K
_AtmVplReceiveTrafficDescrIndex_Object=MibTableColumn
atmVplReceiveTrafficDescrIndex=_AtmVplReceiveTrafficDescrIndex_Object((1,3,6,1,2,1,37,1,6,1,5),_AtmVplReceiveTrafficDescrIndex_Type())
atmVplReceiveTrafficDescrIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:atmVplReceiveTrafficDescrIndex.setStatus(_B)
class _AtmVplTransmitTrafficDescrIndex_Type(AtmTrafficDescrParamIndex):defaultValue=0
_AtmVplTransmitTrafficDescrIndex_Type.__name__=_K
_AtmVplTransmitTrafficDescrIndex_Object=MibTableColumn
atmVplTransmitTrafficDescrIndex=_AtmVplTransmitTrafficDescrIndex_Object((1,3,6,1,2,1,37,1,6,1,6),_AtmVplTransmitTrafficDescrIndex_Type())
atmVplTransmitTrafficDescrIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:atmVplTransmitTrafficDescrIndex.setStatus(_B)
class _AtmVplCrossConnectIdentifier_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmVplCrossConnectIdentifier_Type.__name__=_E
_AtmVplCrossConnectIdentifier_Object=MibTableColumn
atmVplCrossConnectIdentifier=_AtmVplCrossConnectIdentifier_Object((1,3,6,1,2,1,37,1,6,1,7),_AtmVplCrossConnectIdentifier_Type())
atmVplCrossConnectIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:atmVplCrossConnectIdentifier.setStatus(_B)
class _AtmVplRowStatus_Type(RowStatus):defaultValue=5
_AtmVplRowStatus_Type.__name__=_L
_AtmVplRowStatus_Object=MibTableColumn
atmVplRowStatus=_AtmVplRowStatus_Object((1,3,6,1,2,1,37,1,6,1,8),_AtmVplRowStatus_Type())
atmVplRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:atmVplRowStatus.setStatus(_B)
class _AtmVplCastType_Type(AtmConnCastType):defaultValue=1
_AtmVplCastType_Type.__name__=_X
_AtmVplCastType_Object=MibTableColumn
atmVplCastType=_AtmVplCastType_Object((1,3,6,1,2,1,37,1,6,1,9),_AtmVplCastType_Type())
atmVplCastType.setMaxAccess(_D)
if mibBuilder.loadTexts:atmVplCastType.setStatus(_B)
class _AtmVplConnKind_Type(AtmConnKind):defaultValue=1
_AtmVplConnKind_Type.__name__=_Y
_AtmVplConnKind_Object=MibTableColumn
atmVplConnKind=_AtmVplConnKind_Object((1,3,6,1,2,1,37,1,6,1,10),_AtmVplConnKind_Type())
atmVplConnKind.setMaxAccess(_D)
if mibBuilder.loadTexts:atmVplConnKind.setStatus(_B)
_AtmVclTable_Object=MibTable
atmVclTable=_AtmVclTable_Object((1,3,6,1,2,1,37,1,7))
if mibBuilder.loadTexts:atmVclTable.setStatus(_B)
_AtmVclEntry_Object=MibTableRow
atmVclEntry=_AtmVclEntry_Object((1,3,6,1,2,1,37,1,7,1))
atmVclEntry.setIndexNames((0,_I,_J),(0,_A,_AL),(0,_A,_AM))
if mibBuilder.loadTexts:atmVclEntry.setStatus(_B)
_AtmVclVpi_Type=AtmVpIdentifier
_AtmVclVpi_Object=MibTableColumn
atmVclVpi=_AtmVclVpi_Object((1,3,6,1,2,1,37,1,7,1,1),_AtmVclVpi_Type())
atmVclVpi.setMaxAccess(_F)
if mibBuilder.loadTexts:atmVclVpi.setStatus(_B)
_AtmVclVci_Type=AtmVcIdentifier
_AtmVclVci_Object=MibTableColumn
atmVclVci=_AtmVclVci_Object((1,3,6,1,2,1,37,1,7,1,2),_AtmVclVci_Type())
atmVclVci.setMaxAccess(_F)
if mibBuilder.loadTexts:atmVclVci.setStatus(_B)
class _AtmVclAdminStatus_Type(AtmVorXAdminStatus):defaultValue=2
_AtmVclAdminStatus_Type.__name__=_M
_AtmVclAdminStatus_Object=MibTableColumn
atmVclAdminStatus=_AtmVclAdminStatus_Object((1,3,6,1,2,1,37,1,7,1,3),_AtmVclAdminStatus_Type())
atmVclAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:atmVclAdminStatus.setStatus(_B)
_AtmVclOperStatus_Type=AtmVorXOperStatus
_AtmVclOperStatus_Object=MibTableColumn
atmVclOperStatus=_AtmVclOperStatus_Object((1,3,6,1,2,1,37,1,7,1,4),_AtmVclOperStatus_Type())
atmVclOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:atmVclOperStatus.setStatus(_B)
_AtmVclLastChange_Type=AtmVorXLastChange
_AtmVclLastChange_Object=MibTableColumn
atmVclLastChange=_AtmVclLastChange_Object((1,3,6,1,2,1,37,1,7,1,5),_AtmVclLastChange_Type())
atmVclLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:atmVclLastChange.setStatus(_B)
class _AtmVclReceiveTrafficDescrIndex_Type(AtmTrafficDescrParamIndex):defaultValue=0
_AtmVclReceiveTrafficDescrIndex_Type.__name__=_K
_AtmVclReceiveTrafficDescrIndex_Object=MibTableColumn
atmVclReceiveTrafficDescrIndex=_AtmVclReceiveTrafficDescrIndex_Object((1,3,6,1,2,1,37,1,7,1,6),_AtmVclReceiveTrafficDescrIndex_Type())
atmVclReceiveTrafficDescrIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:atmVclReceiveTrafficDescrIndex.setStatus(_B)
class _AtmVclTransmitTrafficDescrIndex_Type(AtmTrafficDescrParamIndex):defaultValue=0
_AtmVclTransmitTrafficDescrIndex_Type.__name__=_K
_AtmVclTransmitTrafficDescrIndex_Object=MibTableColumn
atmVclTransmitTrafficDescrIndex=_AtmVclTransmitTrafficDescrIndex_Object((1,3,6,1,2,1,37,1,7,1,7),_AtmVclTransmitTrafficDescrIndex_Type())
atmVclTransmitTrafficDescrIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:atmVclTransmitTrafficDescrIndex.setStatus(_B)
class _AtmVccAalType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('aal1',1),('aal34',2),('aal5',3),(_Z,4),('unknown',5),('aal2',6)))
_AtmVccAalType_Type.__name__=_E
_AtmVccAalType_Object=MibTableColumn
atmVccAalType=_AtmVccAalType_Object((1,3,6,1,2,1,37,1,7,1,8),_AtmVccAalType_Type())
atmVccAalType.setMaxAccess(_D)
if mibBuilder.loadTexts:atmVccAalType.setStatus(_B)
class _AtmVccAal5CpcsTransmitSduSize_Type(Integer32):defaultValue=9188;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AtmVccAal5CpcsTransmitSduSize_Type.__name__=_E
_AtmVccAal5CpcsTransmitSduSize_Object=MibTableColumn
atmVccAal5CpcsTransmitSduSize=_AtmVccAal5CpcsTransmitSduSize_Object((1,3,6,1,2,1,37,1,7,1,9),_AtmVccAal5CpcsTransmitSduSize_Type())
atmVccAal5CpcsTransmitSduSize.setMaxAccess(_D)
if mibBuilder.loadTexts:atmVccAal5CpcsTransmitSduSize.setStatus(_B)
class _AtmVccAal5CpcsReceiveSduSize_Type(Integer32):defaultValue=9188;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AtmVccAal5CpcsReceiveSduSize_Type.__name__=_E
_AtmVccAal5CpcsReceiveSduSize_Object=MibTableColumn
atmVccAal5CpcsReceiveSduSize=_AtmVccAal5CpcsReceiveSduSize_Object((1,3,6,1,2,1,37,1,7,1,10),_AtmVccAal5CpcsReceiveSduSize_Type())
atmVccAal5CpcsReceiveSduSize.setMaxAccess(_D)
if mibBuilder.loadTexts:atmVccAal5CpcsReceiveSduSize.setStatus(_B)
class _AtmVccAal5EncapsType_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('vcMultiplexRoutedProtocol',1),('vcMultiplexBridgedProtocol8023',2),('vcMultiplexBridgedProtocol8025',3),('vcMultiplexBridgedProtocol8026',4),('vcMultiplexLANemulation8023',5),('vcMultiplexLANemulation8025',6),('llcEncapsulation',7),('multiprotocolFrameRelaySscs',8),(_Z,9),('unknown',10)))
_AtmVccAal5EncapsType_Type.__name__=_E
_AtmVccAal5EncapsType_Object=MibTableColumn
atmVccAal5EncapsType=_AtmVccAal5EncapsType_Object((1,3,6,1,2,1,37,1,7,1,11),_AtmVccAal5EncapsType_Type())
atmVccAal5EncapsType.setMaxAccess(_D)
if mibBuilder.loadTexts:atmVccAal5EncapsType.setStatus(_B)
class _AtmVclCrossConnectIdentifier_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmVclCrossConnectIdentifier_Type.__name__=_E
_AtmVclCrossConnectIdentifier_Object=MibTableColumn
atmVclCrossConnectIdentifier=_AtmVclCrossConnectIdentifier_Object((1,3,6,1,2,1,37,1,7,1,12),_AtmVclCrossConnectIdentifier_Type())
atmVclCrossConnectIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:atmVclCrossConnectIdentifier.setStatus(_B)
class _AtmVclRowStatus_Type(RowStatus):defaultValue=5
_AtmVclRowStatus_Type.__name__=_L
_AtmVclRowStatus_Object=MibTableColumn
atmVclRowStatus=_AtmVclRowStatus_Object((1,3,6,1,2,1,37,1,7,1,13),_AtmVclRowStatus_Type())
atmVclRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:atmVclRowStatus.setStatus(_B)
class _AtmVclCastType_Type(AtmConnCastType):defaultValue=1
_AtmVclCastType_Type.__name__=_X
_AtmVclCastType_Object=MibTableColumn
atmVclCastType=_AtmVclCastType_Object((1,3,6,1,2,1,37,1,7,1,14),_AtmVclCastType_Type())
atmVclCastType.setMaxAccess(_D)
if mibBuilder.loadTexts:atmVclCastType.setStatus(_B)
class _AtmVclConnKind_Type(AtmConnKind):defaultValue=1
_AtmVclConnKind_Type.__name__=_Y
_AtmVclConnKind_Object=MibTableColumn
atmVclConnKind=_AtmVclConnKind_Object((1,3,6,1,2,1,37,1,7,1,15),_AtmVclConnKind_Type())
atmVclConnKind.setMaxAccess(_D)
if mibBuilder.loadTexts:atmVclConnKind.setStatus(_B)
class _AtmVpCrossConnectIndexNext_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmVpCrossConnectIndexNext_Type.__name__=_E
_AtmVpCrossConnectIndexNext_Object=MibScalar
atmVpCrossConnectIndexNext=_AtmVpCrossConnectIndexNext_Object((1,3,6,1,2,1,37,1,8),_AtmVpCrossConnectIndexNext_Type())
atmVpCrossConnectIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:atmVpCrossConnectIndexNext.setStatus(_B)
_AtmVpCrossConnectTable_Object=MibTable
atmVpCrossConnectTable=_AtmVpCrossConnectTable_Object((1,3,6,1,2,1,37,1,9))
if mibBuilder.loadTexts:atmVpCrossConnectTable.setStatus(_B)
_AtmVpCrossConnectEntry_Object=MibTableRow
atmVpCrossConnectEntry=_AtmVpCrossConnectEntry_Object((1,3,6,1,2,1,37,1,9,1))
atmVpCrossConnectEntry.setIndexNames((0,_A,_AN),(0,_A,_AO),(0,_A,_AP),(0,_A,_AQ),(0,_A,_AR))
if mibBuilder.loadTexts:atmVpCrossConnectEntry.setStatus(_B)
class _AtmVpCrossConnectIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AtmVpCrossConnectIndex_Type.__name__=_E
_AtmVpCrossConnectIndex_Object=MibTableColumn
atmVpCrossConnectIndex=_AtmVpCrossConnectIndex_Object((1,3,6,1,2,1,37,1,9,1,1),_AtmVpCrossConnectIndex_Type())
atmVpCrossConnectIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:atmVpCrossConnectIndex.setStatus(_B)
_AtmVpCrossConnectLowIfIndex_Type=InterfaceIndex
_AtmVpCrossConnectLowIfIndex_Object=MibTableColumn
atmVpCrossConnectLowIfIndex=_AtmVpCrossConnectLowIfIndex_Object((1,3,6,1,2,1,37,1,9,1,2),_AtmVpCrossConnectLowIfIndex_Type())
atmVpCrossConnectLowIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:atmVpCrossConnectLowIfIndex.setStatus(_B)
_AtmVpCrossConnectLowVpi_Type=AtmVpIdentifier
_AtmVpCrossConnectLowVpi_Object=MibTableColumn
atmVpCrossConnectLowVpi=_AtmVpCrossConnectLowVpi_Object((1,3,6,1,2,1,37,1,9,1,3),_AtmVpCrossConnectLowVpi_Type())
atmVpCrossConnectLowVpi.setMaxAccess(_F)
if mibBuilder.loadTexts:atmVpCrossConnectLowVpi.setStatus(_B)
_AtmVpCrossConnectHighIfIndex_Type=InterfaceIndex
_AtmVpCrossConnectHighIfIndex_Object=MibTableColumn
atmVpCrossConnectHighIfIndex=_AtmVpCrossConnectHighIfIndex_Object((1,3,6,1,2,1,37,1,9,1,4),_AtmVpCrossConnectHighIfIndex_Type())
atmVpCrossConnectHighIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:atmVpCrossConnectHighIfIndex.setStatus(_B)
_AtmVpCrossConnectHighVpi_Type=AtmVpIdentifier
_AtmVpCrossConnectHighVpi_Object=MibTableColumn
atmVpCrossConnectHighVpi=_AtmVpCrossConnectHighVpi_Object((1,3,6,1,2,1,37,1,9,1,5),_AtmVpCrossConnectHighVpi_Type())
atmVpCrossConnectHighVpi.setMaxAccess(_F)
if mibBuilder.loadTexts:atmVpCrossConnectHighVpi.setStatus(_B)
class _AtmVpCrossConnectAdminStatus_Type(AtmVorXAdminStatus):defaultValue=2
_AtmVpCrossConnectAdminStatus_Type.__name__=_M
_AtmVpCrossConnectAdminStatus_Object=MibTableColumn
atmVpCrossConnectAdminStatus=_AtmVpCrossConnectAdminStatus_Object((1,3,6,1,2,1,37,1,9,1,6),_AtmVpCrossConnectAdminStatus_Type())
atmVpCrossConnectAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:atmVpCrossConnectAdminStatus.setStatus(_B)
_AtmVpCrossConnectL2HOperStatus_Type=AtmVorXOperStatus
_AtmVpCrossConnectL2HOperStatus_Object=MibTableColumn
atmVpCrossConnectL2HOperStatus=_AtmVpCrossConnectL2HOperStatus_Object((1,3,6,1,2,1,37,1,9,1,7),_AtmVpCrossConnectL2HOperStatus_Type())
atmVpCrossConnectL2HOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:atmVpCrossConnectL2HOperStatus.setStatus(_B)
_AtmVpCrossConnectH2LOperStatus_Type=AtmVorXOperStatus
_AtmVpCrossConnectH2LOperStatus_Object=MibTableColumn
atmVpCrossConnectH2LOperStatus=_AtmVpCrossConnectH2LOperStatus_Object((1,3,6,1,2,1,37,1,9,1,8),_AtmVpCrossConnectH2LOperStatus_Type())
atmVpCrossConnectH2LOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:atmVpCrossConnectH2LOperStatus.setStatus(_B)
_AtmVpCrossConnectL2HLastChange_Type=AtmVorXLastChange
_AtmVpCrossConnectL2HLastChange_Object=MibTableColumn
atmVpCrossConnectL2HLastChange=_AtmVpCrossConnectL2HLastChange_Object((1,3,6,1,2,1,37,1,9,1,9),_AtmVpCrossConnectL2HLastChange_Type())
atmVpCrossConnectL2HLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:atmVpCrossConnectL2HLastChange.setStatus(_B)
_AtmVpCrossConnectH2LLastChange_Type=AtmVorXLastChange
_AtmVpCrossConnectH2LLastChange_Object=MibTableColumn
atmVpCrossConnectH2LLastChange=_AtmVpCrossConnectH2LLastChange_Object((1,3,6,1,2,1,37,1,9,1,10),_AtmVpCrossConnectH2LLastChange_Type())
atmVpCrossConnectH2LLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:atmVpCrossConnectH2LLastChange.setStatus(_B)
class _AtmVpCrossConnectRowStatus_Type(RowStatus):defaultValue=5
_AtmVpCrossConnectRowStatus_Type.__name__=_L
_AtmVpCrossConnectRowStatus_Object=MibTableColumn
atmVpCrossConnectRowStatus=_AtmVpCrossConnectRowStatus_Object((1,3,6,1,2,1,37,1,9,1,11),_AtmVpCrossConnectRowStatus_Type())
atmVpCrossConnectRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:atmVpCrossConnectRowStatus.setStatus(_B)
class _AtmVcCrossConnectIndexNext_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmVcCrossConnectIndexNext_Type.__name__=_E
_AtmVcCrossConnectIndexNext_Object=MibScalar
atmVcCrossConnectIndexNext=_AtmVcCrossConnectIndexNext_Object((1,3,6,1,2,1,37,1,10),_AtmVcCrossConnectIndexNext_Type())
atmVcCrossConnectIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:atmVcCrossConnectIndexNext.setStatus(_B)
_AtmVcCrossConnectTable_Object=MibTable
atmVcCrossConnectTable=_AtmVcCrossConnectTable_Object((1,3,6,1,2,1,37,1,11))
if mibBuilder.loadTexts:atmVcCrossConnectTable.setStatus(_B)
_AtmVcCrossConnectEntry_Object=MibTableRow
atmVcCrossConnectEntry=_AtmVcCrossConnectEntry_Object((1,3,6,1,2,1,37,1,11,1))
atmVcCrossConnectEntry.setIndexNames((0,_A,_AS),(0,_A,_AT),(0,_A,_AU),(0,_A,_AV),(0,_A,_AW),(0,_A,_AX),(0,_A,_AY))
if mibBuilder.loadTexts:atmVcCrossConnectEntry.setStatus(_B)
class _AtmVcCrossConnectIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AtmVcCrossConnectIndex_Type.__name__=_E
_AtmVcCrossConnectIndex_Object=MibTableColumn
atmVcCrossConnectIndex=_AtmVcCrossConnectIndex_Object((1,3,6,1,2,1,37,1,11,1,1),_AtmVcCrossConnectIndex_Type())
atmVcCrossConnectIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:atmVcCrossConnectIndex.setStatus(_B)
_AtmVcCrossConnectLowIfIndex_Type=InterfaceIndex
_AtmVcCrossConnectLowIfIndex_Object=MibTableColumn
atmVcCrossConnectLowIfIndex=_AtmVcCrossConnectLowIfIndex_Object((1,3,6,1,2,1,37,1,11,1,2),_AtmVcCrossConnectLowIfIndex_Type())
atmVcCrossConnectLowIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:atmVcCrossConnectLowIfIndex.setStatus(_B)
_AtmVcCrossConnectLowVpi_Type=AtmVpIdentifier
_AtmVcCrossConnectLowVpi_Object=MibTableColumn
atmVcCrossConnectLowVpi=_AtmVcCrossConnectLowVpi_Object((1,3,6,1,2,1,37,1,11,1,3),_AtmVcCrossConnectLowVpi_Type())
atmVcCrossConnectLowVpi.setMaxAccess(_F)
if mibBuilder.loadTexts:atmVcCrossConnectLowVpi.setStatus(_B)
_AtmVcCrossConnectLowVci_Type=AtmVcIdentifier
_AtmVcCrossConnectLowVci_Object=MibTableColumn
atmVcCrossConnectLowVci=_AtmVcCrossConnectLowVci_Object((1,3,6,1,2,1,37,1,11,1,4),_AtmVcCrossConnectLowVci_Type())
atmVcCrossConnectLowVci.setMaxAccess(_F)
if mibBuilder.loadTexts:atmVcCrossConnectLowVci.setStatus(_B)
_AtmVcCrossConnectHighIfIndex_Type=InterfaceIndex
_AtmVcCrossConnectHighIfIndex_Object=MibTableColumn
atmVcCrossConnectHighIfIndex=_AtmVcCrossConnectHighIfIndex_Object((1,3,6,1,2,1,37,1,11,1,5),_AtmVcCrossConnectHighIfIndex_Type())
atmVcCrossConnectHighIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:atmVcCrossConnectHighIfIndex.setStatus(_B)
_AtmVcCrossConnectHighVpi_Type=AtmVpIdentifier
_AtmVcCrossConnectHighVpi_Object=MibTableColumn
atmVcCrossConnectHighVpi=_AtmVcCrossConnectHighVpi_Object((1,3,6,1,2,1,37,1,11,1,6),_AtmVcCrossConnectHighVpi_Type())
atmVcCrossConnectHighVpi.setMaxAccess(_F)
if mibBuilder.loadTexts:atmVcCrossConnectHighVpi.setStatus(_B)
_AtmVcCrossConnectHighVci_Type=AtmVcIdentifier
_AtmVcCrossConnectHighVci_Object=MibTableColumn
atmVcCrossConnectHighVci=_AtmVcCrossConnectHighVci_Object((1,3,6,1,2,1,37,1,11,1,7),_AtmVcCrossConnectHighVci_Type())
atmVcCrossConnectHighVci.setMaxAccess(_F)
if mibBuilder.loadTexts:atmVcCrossConnectHighVci.setStatus(_B)
class _AtmVcCrossConnectAdminStatus_Type(AtmVorXAdminStatus):defaultValue=2
_AtmVcCrossConnectAdminStatus_Type.__name__=_M
_AtmVcCrossConnectAdminStatus_Object=MibTableColumn
atmVcCrossConnectAdminStatus=_AtmVcCrossConnectAdminStatus_Object((1,3,6,1,2,1,37,1,11,1,8),_AtmVcCrossConnectAdminStatus_Type())
atmVcCrossConnectAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:atmVcCrossConnectAdminStatus.setStatus(_B)
_AtmVcCrossConnectL2HOperStatus_Type=AtmVorXOperStatus
_AtmVcCrossConnectL2HOperStatus_Object=MibTableColumn
atmVcCrossConnectL2HOperStatus=_AtmVcCrossConnectL2HOperStatus_Object((1,3,6,1,2,1,37,1,11,1,9),_AtmVcCrossConnectL2HOperStatus_Type())
atmVcCrossConnectL2HOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:atmVcCrossConnectL2HOperStatus.setStatus(_B)
_AtmVcCrossConnectH2LOperStatus_Type=AtmVorXOperStatus
_AtmVcCrossConnectH2LOperStatus_Object=MibTableColumn
atmVcCrossConnectH2LOperStatus=_AtmVcCrossConnectH2LOperStatus_Object((1,3,6,1,2,1,37,1,11,1,10),_AtmVcCrossConnectH2LOperStatus_Type())
atmVcCrossConnectH2LOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:atmVcCrossConnectH2LOperStatus.setStatus(_B)
_AtmVcCrossConnectL2HLastChange_Type=AtmVorXLastChange
_AtmVcCrossConnectL2HLastChange_Object=MibTableColumn
atmVcCrossConnectL2HLastChange=_AtmVcCrossConnectL2HLastChange_Object((1,3,6,1,2,1,37,1,11,1,11),_AtmVcCrossConnectL2HLastChange_Type())
atmVcCrossConnectL2HLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:atmVcCrossConnectL2HLastChange.setStatus(_B)
_AtmVcCrossConnectH2LLastChange_Type=AtmVorXLastChange
_AtmVcCrossConnectH2LLastChange_Object=MibTableColumn
atmVcCrossConnectH2LLastChange=_AtmVcCrossConnectH2LLastChange_Object((1,3,6,1,2,1,37,1,11,1,12),_AtmVcCrossConnectH2LLastChange_Type())
atmVcCrossConnectH2LLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:atmVcCrossConnectH2LLastChange.setStatus(_B)
class _AtmVcCrossConnectRowStatus_Type(RowStatus):defaultValue=5
_AtmVcCrossConnectRowStatus_Type.__name__=_L
_AtmVcCrossConnectRowStatus_Object=MibTableColumn
atmVcCrossConnectRowStatus=_AtmVcCrossConnectRowStatus_Object((1,3,6,1,2,1,37,1,11,1,13),_AtmVcCrossConnectRowStatus_Type())
atmVcCrossConnectRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:atmVcCrossConnectRowStatus.setStatus(_B)
_Aal5VccTable_Object=MibTable
aal5VccTable=_Aal5VccTable_Object((1,3,6,1,2,1,37,1,12))
if mibBuilder.loadTexts:aal5VccTable.setStatus(_B)
_Aal5VccEntry_Object=MibTableRow
aal5VccEntry=_Aal5VccEntry_Object((1,3,6,1,2,1,37,1,12,1))
aal5VccEntry.setIndexNames((0,_I,_J),(0,_A,_AZ),(0,_A,_Aa))
if mibBuilder.loadTexts:aal5VccEntry.setStatus(_B)
_Aal5VccVpi_Type=AtmVpIdentifier
_Aal5VccVpi_Object=MibTableColumn
aal5VccVpi=_Aal5VccVpi_Object((1,3,6,1,2,1,37,1,12,1,1),_Aal5VccVpi_Type())
aal5VccVpi.setMaxAccess(_F)
if mibBuilder.loadTexts:aal5VccVpi.setStatus(_B)
_Aal5VccVci_Type=AtmVcIdentifier
_Aal5VccVci_Object=MibTableColumn
aal5VccVci=_Aal5VccVci_Object((1,3,6,1,2,1,37,1,12,1,2),_Aal5VccVci_Type())
aal5VccVci.setMaxAccess(_F)
if mibBuilder.loadTexts:aal5VccVci.setStatus(_B)
_Aal5VccCrcErrors_Type=Counter32
_Aal5VccCrcErrors_Object=MibTableColumn
aal5VccCrcErrors=_Aal5VccCrcErrors_Object((1,3,6,1,2,1,37,1,12,1,3),_Aal5VccCrcErrors_Type())
aal5VccCrcErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:aal5VccCrcErrors.setStatus(_B)
_Aal5VccSarTimeOuts_Type=Counter32
_Aal5VccSarTimeOuts_Object=MibTableColumn
aal5VccSarTimeOuts=_Aal5VccSarTimeOuts_Object((1,3,6,1,2,1,37,1,12,1,4),_Aal5VccSarTimeOuts_Type())
aal5VccSarTimeOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:aal5VccSarTimeOuts.setStatus(_B)
_Aal5VccOverSizedSDUs_Type=Counter32
_Aal5VccOverSizedSDUs_Object=MibTableColumn
aal5VccOverSizedSDUs=_Aal5VccOverSizedSDUs_Object((1,3,6,1,2,1,37,1,12,1,5),_Aal5VccOverSizedSDUs_Type())
aal5VccOverSizedSDUs.setMaxAccess(_C)
if mibBuilder.loadTexts:aal5VccOverSizedSDUs.setStatus(_B)
class _AtmTrafficDescrParamIndexNext_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmTrafficDescrParamIndexNext_Type.__name__=_E
_AtmTrafficDescrParamIndexNext_Object=MibScalar
atmTrafficDescrParamIndexNext=_AtmTrafficDescrParamIndexNext_Object((1,3,6,1,2,1,37,1,13),_AtmTrafficDescrParamIndexNext_Type())
atmTrafficDescrParamIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:atmTrafficDescrParamIndexNext.setStatus(_B)
_AtmMIBConformance_ObjectIdentity=ObjectIdentity
atmMIBConformance=_AtmMIBConformance_ObjectIdentity((1,3,6,1,2,1,37,2))
_AtmMIBGroups_ObjectIdentity=ObjectIdentity
atmMIBGroups=_AtmMIBGroups_ObjectIdentity((1,3,6,1,2,1,37,2,1))
_AtmMIBCompliances_ObjectIdentity=ObjectIdentity
atmMIBCompliances=_AtmMIBCompliances_ObjectIdentity((1,3,6,1,2,1,37,2,2))
atmInterfaceConfGroup=ObjectGroup((1,3,6,1,2,1,37,2,1,1))
atmInterfaceConfGroup.setObjects(*((_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_Ab),(_A,_Ac),(_A,_i),(_A,_j)))
if mibBuilder.loadTexts:atmInterfaceConfGroup.setStatus(_G)
atmTrafficDescrGroup=ObjectGroup((1,3,6,1,2,1,37,2,1,2))
atmTrafficDescrGroup.setObjects(*((_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_Ad),(_A,_q)))
if mibBuilder.loadTexts:atmTrafficDescrGroup.setStatus(_G)
atmInterfaceDs3PlcpGroup=ObjectGroup((1,3,6,1,2,1,37,2,1,3))
atmInterfaceDs3PlcpGroup.setObjects(*((_A,_Ae),(_A,_Af),(_A,_Ag)))
if mibBuilder.loadTexts:atmInterfaceDs3PlcpGroup.setStatus(_B)
atmInterfaceTCGroup=ObjectGroup((1,3,6,1,2,1,37,2,1,4))
atmInterfaceTCGroup.setObjects(*((_A,_Ah),(_A,_Ai)))
if mibBuilder.loadTexts:atmInterfaceTCGroup.setStatus(_B)
atmVpcTerminationGroup=ObjectGroup((1,3,6,1,2,1,37,2,1,5))
atmVpcTerminationGroup.setObjects(*((_A,_N),(_A,_r),(_A,_V),(_A,_O),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:atmVpcTerminationGroup.setStatus(_G)
atmVccTerminationGroup=ObjectGroup((1,3,6,1,2,1,37,2,1,6))
atmVccTerminationGroup.setObjects(*((_A,_R),(_A,_s),(_A,_W),(_A,_S),(_A,_T),(_A,_t),(_A,_U)))
if mibBuilder.loadTexts:atmVccTerminationGroup.setStatus(_G)
atmVpCrossConnectGroup=ObjectGroup((1,3,6,1,2,1,37,2,1,7))
atmVpCrossConnectGroup.setObjects(*((_A,_O),(_A,_P),(_A,_N),(_A,_Q),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:atmVpCrossConnectGroup.setStatus(_G)
atmVcCrossConnectGroup=ObjectGroup((1,3,6,1,2,1,37,2,1,8))
atmVcCrossConnectGroup.setObjects(*((_A,_S),(_A,_T),(_A,_R),(_A,_U),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9)))
if mibBuilder.loadTexts:atmVcCrossConnectGroup.setStatus(_G)
aal5VccGroup=ObjectGroup((1,3,6,1,2,1,37,2,1,9))
aal5VccGroup.setObjects(*((_A,_Aj),(_A,_Ak),(_A,_Al),(_A,_Am),(_A,_An),(_A,_Ao)))
if mibBuilder.loadTexts:aal5VccGroup.setStatus(_B)
atmInterfaceConfGroup2=ObjectGroup((1,3,6,1,2,1,37,2,1,10))
atmInterfaceConfGroup2.setObjects(*((_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_Ap),(_A,_Aq),(_A,_Ar)))
if mibBuilder.loadTexts:atmInterfaceConfGroup2.setStatus(_B)
atmTrafficDescrGroup2=ObjectGroup((1,3,6,1,2,1,37,2,1,11))
atmTrafficDescrGroup2.setObjects(*((_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_As),(_A,_At),(_A,_Au)))
if mibBuilder.loadTexts:atmTrafficDescrGroup2.setStatus(_B)
atmVpcTerminationGroup2=ObjectGroup((1,3,6,1,2,1,37,2,1,12))
atmVpcTerminationGroup2.setObjects(*((_A,_N),(_A,_r),(_A,_V),(_A,_O),(_A,_P),(_A,_Q),(_A,_AA),(_A,_AB)))
if mibBuilder.loadTexts:atmVpcTerminationGroup2.setStatus(_B)
atmVccTerminationGroup2=ObjectGroup((1,3,6,1,2,1,37,2,1,13))
atmVccTerminationGroup2.setObjects(*((_A,_R),(_A,_s),(_A,_W),(_A,_S),(_A,_T),(_A,_t),(_A,_U),(_A,_AC),(_A,_AD)))
if mibBuilder.loadTexts:atmVccTerminationGroup2.setStatus(_B)
atmVplCrossConnectGroup=ObjectGroup((1,3,6,1,2,1,37,2,1,14))
atmVplCrossConnectGroup.setObjects(*((_A,_O),(_A,_P),(_A,_N),(_A,_V),(_A,_Q),(_A,_AA),(_A,_AB)))
if mibBuilder.loadTexts:atmVplCrossConnectGroup.setStatus(_B)
atmVpPvcCrossConnectGroup=ObjectGroup((1,3,6,1,2,1,37,2,1,15))
atmVpPvcCrossConnectGroup.setObjects(*((_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:atmVpPvcCrossConnectGroup.setStatus(_B)
atmVclCrossConnectGroup=ObjectGroup((1,3,6,1,2,1,37,2,1,16))
atmVclCrossConnectGroup.setObjects(*((_A,_S),(_A,_T),(_A,_R),(_A,_W),(_A,_U),(_A,_AC),(_A,_AD)))
if mibBuilder.loadTexts:atmVclCrossConnectGroup.setStatus(_B)
atmVcPvcCrossConnectGroup=ObjectGroup((1,3,6,1,2,1,37,2,1,17))
atmVcPvcCrossConnectGroup.setObjects(*((_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9)))
if mibBuilder.loadTexts:atmVcPvcCrossConnectGroup.setStatus(_B)
atmMIBCompliance=ModuleCompliance((1,3,6,1,2,1,37,2,2,1))
atmMIBCompliance.setObjects(*((_A,_Av),(_A,_Aw)))
if mibBuilder.loadTexts:atmMIBCompliance.setStatus(_G)
atmMIBCompliance2=ModuleCompliance((1,3,6,1,2,1,37,2,2,2))
atmMIBCompliance2.setObjects(*((_A,_Ax),(_A,_Ay)))
if mibBuilder.loadTexts:atmMIBCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'atmMIB':atmMIB,'atmMIBObjects':atmMIBObjects,'atmInterfaceConfTable':atmInterfaceConfTable,'atmInterfaceConfEntry':atmInterfaceConfEntry,_a:atmInterfaceMaxVpcs,_b:atmInterfaceMaxVccs,_c:atmInterfaceConfVpcs,_d:atmInterfaceConfVccs,_e:atmInterfaceMaxActiveVpiBits,_f:atmInterfaceMaxActiveVciBits,_g:atmInterfaceIlmiVpi,_h:atmInterfaceIlmiVci,_Ab:atmInterfaceAddressType,_Ac:atmInterfaceAdminAddress,_i:atmInterfaceMyNeighborIpAddress,_j:atmInterfaceMyNeighborIfName,_Ap:atmInterfaceCurrentMaxVpiBits,_Aq:atmInterfaceCurrentMaxVciBits,_Ar:atmInterfaceSubscrAddress,'atmInterfaceDs3PlcpTable':atmInterfaceDs3PlcpTable,'atmInterfaceDs3PlcpEntry':atmInterfaceDs3PlcpEntry,_Ae:atmInterfaceDs3PlcpSEFSs,_Af:atmInterfaceDs3PlcpAlarmState,_Ag:atmInterfaceDs3PlcpUASs,'atmInterfaceTCTable':atmInterfaceTCTable,'atmInterfaceTCEntry':atmInterfaceTCEntry,_Ah:atmInterfaceOCDEvents,_Ai:atmInterfaceTCAlarmState,'atmTrafficDescrParamTable':atmTrafficDescrParamTable,'atmTrafficDescrParamEntry':atmTrafficDescrParamEntry,_AJ:atmTrafficDescrParamIndex,_k:atmTrafficDescrType,_l:atmTrafficDescrParam1,_m:atmTrafficDescrParam2,_n:atmTrafficDescrParam3,_o:atmTrafficDescrParam4,_p:atmTrafficDescrParam5,_Ad:atmTrafficQoSClass,_q:atmTrafficDescrRowStatus,_As:atmServiceCategory,_At:atmTrafficFrameDiscard,'atmVplTable':atmVplTable,'atmVplEntry':atmVplEntry,_AK:atmVplVpi,_r:atmVplAdminStatus,_N:atmVplOperStatus,_V:atmVplLastChange,_O:atmVplReceiveTrafficDescrIndex,_P:atmVplTransmitTrafficDescrIndex,_A0:atmVplCrossConnectIdentifier,_Q:atmVplRowStatus,_AA:atmVplCastType,_AB:atmVplConnKind,'atmVclTable':atmVclTable,'atmVclEntry':atmVclEntry,_AL:atmVclVpi,_AM:atmVclVci,_s:atmVclAdminStatus,_R:atmVclOperStatus,_W:atmVclLastChange,_S:atmVclReceiveTrafficDescrIndex,_T:atmVclTransmitTrafficDescrIndex,_t:atmVccAalType,_Aj:atmVccAal5CpcsTransmitSduSize,_Ak:atmVccAal5CpcsReceiveSduSize,_Al:atmVccAal5EncapsType,_A8:atmVclCrossConnectIdentifier,_U:atmVclRowStatus,_AC:atmVclCastType,_AD:atmVclConnKind,_A1:atmVpCrossConnectIndexNext,'atmVpCrossConnectTable':atmVpCrossConnectTable,'atmVpCrossConnectEntry':atmVpCrossConnectEntry,_AN:atmVpCrossConnectIndex,_AO:atmVpCrossConnectLowIfIndex,_AP:atmVpCrossConnectLowVpi,_AQ:atmVpCrossConnectHighIfIndex,_AR:atmVpCrossConnectHighVpi,_u:atmVpCrossConnectAdminStatus,_v:atmVpCrossConnectL2HOperStatus,_w:atmVpCrossConnectH2LOperStatus,_x:atmVpCrossConnectL2HLastChange,_y:atmVpCrossConnectH2LLastChange,_z:atmVpCrossConnectRowStatus,_A9:atmVcCrossConnectIndexNext,'atmVcCrossConnectTable':atmVcCrossConnectTable,'atmVcCrossConnectEntry':atmVcCrossConnectEntry,_AS:atmVcCrossConnectIndex,_AT:atmVcCrossConnectLowIfIndex,_AU:atmVcCrossConnectLowVpi,_AV:atmVcCrossConnectLowVci,_AW:atmVcCrossConnectHighIfIndex,_AX:atmVcCrossConnectHighVpi,_AY:atmVcCrossConnectHighVci,_A2:atmVcCrossConnectAdminStatus,_A3:atmVcCrossConnectL2HOperStatus,_A4:atmVcCrossConnectH2LOperStatus,_A5:atmVcCrossConnectL2HLastChange,_A6:atmVcCrossConnectH2LLastChange,_A7:atmVcCrossConnectRowStatus,'aal5VccTable':aal5VccTable,'aal5VccEntry':aal5VccEntry,_AZ:aal5VccVpi,_Aa:aal5VccVci,_Am:aal5VccCrcErrors,_An:aal5VccSarTimeOuts,_Ao:aal5VccOverSizedSDUs,_Au:atmTrafficDescrParamIndexNext,'atmMIBConformance':atmMIBConformance,'atmMIBGroups':atmMIBGroups,_Av:atmInterfaceConfGroup,_Aw:atmTrafficDescrGroup,'atmInterfaceDs3PlcpGroup':atmInterfaceDs3PlcpGroup,'atmInterfaceTCGroup':atmInterfaceTCGroup,'atmVpcTerminationGroup':atmVpcTerminationGroup,'atmVccTerminationGroup':atmVccTerminationGroup,'atmVpCrossConnectGroup':atmVpCrossConnectGroup,'atmVcCrossConnectGroup':atmVcCrossConnectGroup,'aal5VccGroup':aal5VccGroup,_Ax:atmInterfaceConfGroup2,_Ay:atmTrafficDescrGroup2,'atmVpcTerminationGroup2':atmVpcTerminationGroup2,'atmVccTerminationGroup2':atmVccTerminationGroup2,'atmVplCrossConnectGroup':atmVplCrossConnectGroup,'atmVpPvcCrossConnectGroup':atmVpPvcCrossConnectGroup,'atmVclCrossConnectGroup':atmVclCrossConnectGroup,'atmVcPvcCrossConnectGroup':atmVcPvcCrossConnectGroup,'atmMIBCompliances':atmMIBCompliances,'atmMIBCompliance':atmMIBCompliance,'atmMIBCompliance2':atmMIBCompliance2})